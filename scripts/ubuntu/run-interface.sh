#!/usr/bin/env bash
# Run the interface test suite locally on an Ubuntu Docker base, using the
# same commands as CI. Requires: docker, and sibling clones of gramps/ and
# addons-source/ (run ./scripts/bootstrap-forks.sh first).
#
# Part of the scripts/ubuntu/ family — equivalents for other Linux distros
# and for macOS / Windows will live under their own scripts/<platform>/
# directories as those testbeds are added.

set -euo pipefail

WORKSPACE="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." && pwd)"
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
  -w /workspace/gramps-testbed \
  "$IMAGE" \
  bash -c '
    set -e
    # Extras syntax rejects absolute paths — resolve via a relative path.
    (cd /workspace && pip install --break-system-packages --user -e "./gramps[testing]")
    export PATH="$HOME/.local/bin:$PATH"
    # Compile .mo translations into gramps/build/mo (gitignored in the fork).
    # pip install -e skips setup.py build, so without this Gramps logs
    # "Missing or invalid localedir" on every launch and UI strings never
    # get translated. Idempotent — subsequent runs reuse the bind-mounted
    # build dir.
    if [ ! -f /workspace/gramps/build/mo/de/LC_MESSAGES/gramps.mo ]; then
      echo "→ compiling translations"
      for po in /workspace/gramps/po/*.po; do
        lang=$(basename "$po" .po)
        dest="/workspace/gramps/build/mo/$lang/LC_MESSAGES"
        mkdir -p "$dest"
        msgfmt "$po" -o "$dest/gramps.mo"
      done
    fi
    # Bulk addon install is intentionally skipped for the smoke suite:
    #   * make.py mutates tracked .gpr.py files (version bumps), which would
    #     dirty the addons-source fork — it is expected to stay a pure mirror
    #     of upstream.
    #   * Installing all 149 addons blocks Gramps GUI startup during plugin
    #     registration anyway.
    # Individual addons that have dedicated interface tests are installed
    # below by copying the source directory straight into USER_PLUGINS — no
    # make.py invocation, no mutation of addons-source. Keep this list as
    # tight as the tests require; every entry adds startup cost.
    USER_PLUGINS="$(python3 -c "from gramps.gen.const import USER_PLUGINS; print(USER_PLUGINS)")"
    mkdir -p "$USER_PLUGINS"
    for addon in QuiltView; do
      src="/workspace/addons-source/$addon"
      if [ -d "$src" ]; then
        rm -rf "$USER_PLUGINS/$addon"
        cp -a "$src" "$USER_PLUGINS/$addon"
        echo "→ installed addon: $addon"
      else
        echo "WARN: addon source not found: $src (skipping install)"
      fi
    done
    # seed trees
    gramps -C TestTree -i /workspace/gramps/example/gramps/example.gramps
    gramps -C QuiltViewTree \
           -i /workspace/gramps-testbed/tests/interface/data/quiltview_minimal.gramps
    gramps -C Bug14100Tree \
           -i /workspace/gramps-testbed/tests/interface/data/bug_0014100_minimal.gramps
    # Clear stale XMLs so accumulated runs do not pollute JUnit summaries.
    rm -rf /workspace/gramps-testbed/test-results
    mkdir -p /workspace/gramps-testbed/test-results
    # run the interface suite under Xvfb + dbus + AT-SPI
    cd /workspace/gramps-testbed
    xvfb-run -a --server-args="-screen 0 1920x1080x24" \
      dbus-run-session -- bash -c "
        gsettings set org.gnome.desktop.interface toolkit-accessibility true
        /usr/libexec/at-spi-bus-launcher --launch-immediately &
        sleep 2
        python3 -m xmlrunner discover -s tests -p 'test_*.py' -o test-results/ -v
      "
  '
