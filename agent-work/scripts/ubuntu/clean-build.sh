#!/usr/bin/env bash
# Clean the gramps/build/ dir left behind by docker-based test runs.
#
# The in-container `pip install -e ./gramps[testing]` step the runners
# perform (run-unit.sh / run-interface.sh / run-addon-unit.sh) writes
# build artefacts under ./gramps/build/, which then survive on the
# bind-mounted host directory. On the next run, gramps' build_hook
# tries to `rmtree(build_dir)` and dies with `PermissionError` whenever
# those files are owned by a uid the current host user can't write to
# (typically: the host uid does not match the container's `runner`
# user (uid=1000), or some earlier run was made with `-u root` and
# left root-owned artefacts).
#
# This helper removes the dir, preferring a host-side `rm -rf` when
# permissions allow and falling back to a container running as root
# when they don't. Idempotent; safe to invoke at any time.
#
# Invoked automatically by run-addon-unit.sh when it detects a uid
# mismatch on gramps/build/; also fine to run by hand:
#
#   ./scripts/ubuntu/clean-build.sh

set -euo pipefail

# Repo root via git (depth-independent — a fixed-depth ../.. walk silently
# breaks on directory moves; see test_runner_workspace_root.py). WORKSPACE
# is its parent, holding the sibling gramps/ checkout.
WORKSPACE="$(cd "$(git -C "$(dirname "${BASH_SOURCE[0]}")" rev-parse --show-toplevel)/.." && pwd)"
cd "$WORKSPACE"

build_dir="$WORKSPACE/gramps/build"

if [[ ! -d "$build_dir" ]]; then
  echo "→ no gramps/build/ — nothing to clean"
  exit 0
fi

# Fast path: if the host user owns the dir, plain rm works and we can
# skip the docker round-trip entirely.
if rm -rf "$build_dir" 2>/dev/null; then
  echo "→ removed gramps/build/ (host-side)"
  exit 0
fi

# Slow path: ownership blocks host-side removal. Use the testbed image
# running as root inside the container — same uid that originally
# created the artefacts, so it can delete them. Resolve the image with
# the same logic the runners use (per-Gramps-version tag).
GRAMPS_VERSION="$(sed -nE 's/^VERSION_TUPLE *= *\(([0-9]+), *([0-9]+), *([0-9]+)\).*$/\1.\2.\3/p' "$WORKSPACE/gramps/gramps/version.py")"
: "${GRAMPS_VERSION:?could not detect Gramps version from gramps/version.py}"
IMAGE="${GRAMPS_TESTBED_IMAGE:-gramps-testbed:ubuntu-$GRAMPS_VERSION}"

if ! docker image inspect "$IMAGE" >/dev/null 2>&1; then
  echo "→ building $IMAGE (needed for root-owned cleanup)"
  docker build -f gramps-testbed/docker/Dockerfile.ubuntu -t "$IMAGE" gramps-testbed
fi

owner_uid="$(stat -c %u "$build_dir" 2>/dev/null || echo "?")"
echo "→ gramps/build/ owned by uid=$owner_uid; removing via $IMAGE running as root"
docker run --rm -u root -v "$WORKSPACE/gramps:/g" "$IMAGE" rm -rf /g/build
echo "→ cleaned"
