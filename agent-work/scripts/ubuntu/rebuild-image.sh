#!/usr/bin/env bash
# Force-rebuild the gramps-testbed:ubuntu Docker image.
#
# run-interface.sh / run-unit.sh / run-manual.sh only build when the image
# is missing, so Dockerfile changes aren't picked up automatically. Use this
# after editing docker/Dockerfile.ubuntu (new apt packages, locale tweaks, etc.).
#
# Part of the agent-work/scripts/ubuntu/ family — future Fedora/Arch Dockerfiles will
# get their own rebuild helpers under agent-work/scripts/<distro>/.
#
# Usage:
#   ./agent-work/scripts/ubuntu/rebuild-image.sh            # remove + rebuild
#   ./agent-work/scripts/ubuntu/rebuild-image.sh --no-cache # also bust Docker layer cache

set -euo pipefail

TESTBED="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
WORKSPACE="$(cd "$TESTBED/.." && pwd)"

# Tag the image with platform + Gramps version so multiple versions can
# coexist on the same machine. Read VERSION_TUPLE from gramps' own
# source-of-truth.
GRAMPS_VERSION="$(sed -nE 's/^VERSION_TUPLE *= *\(([0-9]+), *([0-9]+), *([0-9]+)\).*$/\1.\2.\3/p' "$WORKSPACE/gramps/gramps/version.py")"
: "${GRAMPS_VERSION:?could not detect Gramps version from gramps/version.py}"
IMAGE="${GRAMPS_TESTBED_IMAGE:-gramps-testbed:ubuntu-$GRAMPS_VERSION}"

BUILD_ARGS=()
case "${1:-}" in
  "")          ;;
  --no-cache)  BUILD_ARGS+=(--no-cache) ;;
  *)
    echo "unknown argument: $1" >&2
    echo "usage: $0 [--no-cache]" >&2
    exit 2
    ;;
esac

if docker image inspect "$IMAGE" >/dev/null 2>&1; then
  echo "→ removing $IMAGE"
  docker rmi -f "$IMAGE" >/dev/null
fi

echo "→ building $IMAGE"
docker build "${BUILD_ARGS[@]}" -f "$TESTBED/docker/Dockerfile.ubuntu" -t "$IMAGE" "$TESTBED"

echo
echo "Done. Re-run ./agent-work/scripts/ubuntu/run-{interface,unit,manual}.sh."
