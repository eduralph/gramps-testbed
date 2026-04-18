#!/usr/bin/env bash
# Run the interface test suite locally, using the same commands as CI.
# Requires: docker, and sibling clones of gramps/ and addons-source/
# (run ./scripts/bootstrap-forks.sh first).

set -euo pipefail

WORKSPACE="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$WORKSPACE"

IMAGE="${GRAMPS_TESTBED_IMAGE:-gramps-testbed:latest}"

if ! docker image inspect "$IMAGE" >/dev/null 2>&1; then
  echo "→ building $IMAGE"
  docker build -f gramps-testbed/docker/Dockerfile.testbed -t "$IMAGE" gramps-testbed
fi

docker run --rm -it \
  -v "$WORKSPACE":/workspace \
  -w /workspace/gramps-testbed \
  "$IMAGE" \
  bash -lc '
    set -e
    pip install --break-system-packages --user -e /workspace/gramps
    # build + install all addons into the user plugin directory
    cd /workspace/addons-source
    python3 make.py gramps60 build all
    mkdir -p ~/.gramps/gramps60/plugins
    for addon in */; do
      [ -f "$addon/${addon%/}.gpr.py" ] && cp -r "$addon" ~/.gramps/gramps60/plugins/
    done
    # seed example tree
    gramps -C TestTree -i /workspace/gramps/example/gramps/example.gramps || true
    # run the interface suite under Xvfb + dbus + AT-SPI
    cd /workspace/gramps-testbed
    xvfb-run -a --server-args="-screen 0 1920x1080x24" \
      dbus-run-session -- bash -c "
        gsettings set org.gnome.desktop.interface toolkit-accessibility true
        /usr/libexec/at-spi-bus-launcher --launch-immediately &
        sleep 2
        python3 -m xmlrunner discover -s tests/interface -o test-results/ -v
      "
  '
