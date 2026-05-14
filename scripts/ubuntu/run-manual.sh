#!/usr/bin/env bash
# Launch Gramps interactively inside the Ubuntu testbed container with
# display forwarding. Companion to scripts/ubuntu/run-interface.sh — use
# this for manual QA or exploratory dogtail selector hunting; tests still
# go through run-interface.sh (GUI) / run-unit.sh (gramps unit suite).
#
# Part of the scripts/ubuntu/ family — equivalent entry points for other
# Linux distros and for macOS / Windows will live under their own
# scripts/<platform>/ directories as those testbeds are added.
#
# Auto-detects display server:
#   * Wayland host → mounts the Wayland socket + uses GDK_BACKEND=wayland.
#     This is the preferred path on modern GNOME/KDE because XWayland drops
#     ConfigureNotify events on resize, leaving Gramps content unpainted
#     when the user resizes the window.
#   * X11 host → falls back to forwarding the X11 socket + $XAUTHORITY.
#
# Usage:
#   ./scripts/ubuntu/run-manual.sh          # launches `gramps -O TestTree`
#   ./scripts/ubuntu/run-manual.sh --shell  # drops into interactive bash

set -euo pipefail

TESTBED="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
WORKSPACE="$(cd "$TESTBED/.." && pwd)"

if [[ "$(uname -s)" != "Linux" ]]; then
  echo "scripts/ubuntu/run-manual.sh requires a Linux host." >&2
  echo "macOS and Windows equivalents will live under scripts/macos/ and" >&2
  echo "scripts/windows/ when those testbeds are added." >&2
  exit 1
fi

if [[ -z "${DISPLAY:-}" && -z "${WAYLAND_DISPLAY:-}" ]]; then
  echo "Neither DISPLAY nor WAYLAND_DISPLAY is set — no display to forward." >&2
  exit 1
fi

MODE="launch"
case "${1:-}" in
  "")         ;;
  --shell)    MODE="shell" ;;
  *)
    echo "unknown argument: $1" >&2
    echo "usage: $0 [--shell]" >&2
    exit 2
    ;;
esac

# Tag the image with platform + Gramps version so multiple versions can
# coexist on the same machine (e.g. switching branches between 6.0.x and
# a future 6.1.x). Read VERSION_TUPLE from gramps' own source-of-truth.
GRAMPS_VERSION="$(sed -nE 's/^VERSION_TUPLE *= *\(([0-9]+), *([0-9]+), *([0-9]+)\).*$/\1.\2.\3/p' "$WORKSPACE/gramps/gramps/version.py")"
: "${GRAMPS_VERSION:?could not detect Gramps version from gramps/version.py}"
IMAGE="${GRAMPS_TESTBED_IMAGE:-gramps-testbed:ubuntu-$GRAMPS_VERSION}"
if ! docker image inspect "$IMAGE" >/dev/null 2>&1; then
  echo "→ building $IMAGE"
  docker build -f "$TESTBED/docker/Dockerfile.ubuntu" -t "$IMAGE" "$TESTBED"
fi

# Persistent Gramps home so TestTree + user-level settings survive runs.
# GRAMPSHOME collapses USER_HOME/USER_DATA/USER_CONFIG into this single dir
# (see gramps/gen/const.py), so one bind mount captures the tree DB, config,
# and plugins. Without it, modern Gramps spreads data across XDG dirs
# (~/.local/share/gramps, ~/.config/gramps) which the legacy ~/.gramps mount
# would miss.
GRAMPS_HOME="$TESTBED/.run/gramps-home"
mkdir -p "$GRAMPS_HOME"

# Display forwarding: prefer Wayland when available, fall back to X11.
# On Wayland, we still also mount the X socket — some GTK helpers probe it
# even when GDK_BACKEND=wayland, and it's harmless if unused.
DISPLAY_ARGS=()
RUNTIME_DIR="${XDG_RUNTIME_DIR:-/run/user/$(id -u)}"
if [[ -n "${WAYLAND_DISPLAY:-}" && -S "$RUNTIME_DIR/$WAYLAND_DISPLAY" ]]; then
  # Mount the whole runtime dir (not just the socket) so XDG_RUNTIME_DIR
  # permissions (0700) are preserved; GLib warns loudly otherwise. Also
  # gives Gramps access to host dbus/pulse sockets for free.
  DISPLAY_ARGS+=(
    -v "$RUNTIME_DIR:/run/user/1000"
    -e "WAYLAND_DISPLAY=$WAYLAND_DISPLAY"
    -e "XDG_RUNTIME_DIR=/run/user/1000"
    -e "GDK_BACKEND=wayland"
  )
fi
if [[ -d /tmp/.X11-unix ]]; then
  DISPLAY_ARGS+=(-v /tmp/.X11-unix:/tmp/.X11-unix)
fi
if [[ -n "${DISPLAY:-}" ]]; then
  DISPLAY_ARGS+=(-e "DISPLAY=$DISPLAY")
fi
# MIT-MAGIC-COOKIE auth for X11. Harmless on pure-Wayland launches.
XAUTH="${XAUTHORITY:-$HOME/.Xauthority}"
if [[ -f "$XAUTH" ]]; then
  DISPLAY_ARGS+=(
    -v "$XAUTH:/home/runner/.Xauthority:ro"
    -e "XAUTHORITY=/home/runner/.Xauthority"
  )
fi

INNER='
  set -e
  (cd /workspace && pip install --break-system-packages --user -e "./gramps[testing]" >/dev/null)
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
  if ! gramps -l 2>/dev/null | grep -qw TestTree; then
    echo "→ seeding TestTree from example.gramps"
    gramps -C TestTree -i /workspace/gramps/example/gramps/example.gramps
  fi
'
case "$MODE" in
  launch) INNER="${INNER}"$'\nexec gramps -O TestTree' ;;
  shell)  INNER="${INNER}"$'\nexec bash' ;;
esac

docker run --rm -it \
  -v "$WORKSPACE":/workspace \
  -v "$GRAMPS_HOME:/home/runner/gramps-home" \
  "${DISPLAY_ARGS[@]}" \
  -e "GRAMPSHOME=/home/runner/gramps-home" \
  -w /workspace/gramps-testbed \
  "$IMAGE" \
  bash -c "$INNER"
