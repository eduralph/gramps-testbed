#!/usr/bin/env bash
# Run gramps' own unit test suite (*_test.py under gramps/**/test/) locally
# on the Ubuntu Docker base, using the same commands as CI. No display,
# no dbus, no AT-SPI — unit tests construct in-memory fixtures only.
#
# Companion to agent-work/scripts/ubuntu/run-interface.sh (GUI tests via dogtail).
# Part of the agent-work/scripts/ubuntu/ family — equivalents for other Linux distros
# and for macOS / Windows will live under their own agent-work/scripts/<platform>/
# directories as those testbeds are added.

set -euo pipefail

# Repo root via git (depth-independent — a fixed-depth ../.. walk silently
# breaks on directory moves; see test_runner_workspace_root.py). WORKSPACE
# is its parent, holding the sibling gramps/ checkout.
WORKSPACE="$(cd "$(git -C "$(dirname "${BASH_SOURCE[0]}")" rev-parse --show-toplevel)/.." && pwd)"
cd "$WORKSPACE"

# Tag the image with platform + Gramps version so multiple versions can
# coexist on the same machine (e.g. switching branches between 6.0.x and
# a future 6.1.x). Read VERSION_TUPLE from gramps' own source-of-truth.
GRAMPS_VERSION="$(sed -nE 's/^VERSION_TUPLE *= *\(([0-9]+), *([0-9]+), *([0-9]+)\).*$/\1.\2.\3/p' "$WORKSPACE/gramps/gramps/version.py")"
: "${GRAMPS_VERSION:?could not detect Gramps version from gramps/version.py}"
IMAGE="${GRAMPS_TESTBED_IMAGE:-gramps-testbed:ubuntu-$GRAMPS_VERSION}"

if ! docker image inspect "$IMAGE" >/dev/null 2>&1; then
  echo "→ building $IMAGE"
  docker build -f gramps-testbed/docker/Dockerfile.ubuntu -t "$IMAGE" gramps-testbed
fi

docker run --rm \
  -v "$WORKSPACE":/workspace \
  -w /workspace/gramps \
  "$IMAGE" \
  bash -c '
    set -e
    # [testing] extras pulls in jsonschema/mock/lxml from gramps setup.py,
    # which some of the upstream *_test.py files import. pip rejects the
    # extras syntax against absolute paths, so resolve via a relative path.
    (cd /workspace && pip install --break-system-packages --user -e "./gramps[testing]")
    export PATH="$HOME/.local/bin:$PATH"
    # Compile .mo translations so gramps.gen imports do not emit
    # "Missing or invalid localedir" warnings during collection.
    if [ ! -f /workspace/gramps/build/mo/de/LC_MESSAGES/gramps.mo ]; then
      echo "→ compiling translations"
      for po in /workspace/gramps/po/*.po; do
        lang=$(basename "$po" .po)
        dest="/workspace/gramps/build/mo/$lang/LC_MESSAGES"
        mkdir -p "$dest"
        msgfmt "$po" -o "$dest/gramps.mo"
      done
    fi
    # Mirrors the canonical command from ../gramps/AGENTS.md:
    #   GRAMPS_RESOURCES=. python3 -m unittest discover -p "*_test.py"
    # We swap unittest for xmlrunner (drop-in replacement) so CI gets
    # JUnit XML for reporting. GRAMPS_RESOURCES=. is load-bearing —
    # without it, several plugin tests fail to locate resource files.
    # Clear stale XMLs so accumulated runs do not pollute JUnit summaries.
    rm -rf /workspace/gramps-testbed/test-results
    mkdir -p /workspace/gramps-testbed/test-results
    cd /workspace/gramps
    GRAMPS_RESOURCES=. python3 -m xmlrunner discover \
      -p "*_test.py" \
      -o /workspace/gramps-testbed/test-results/ \
      -v
  '
