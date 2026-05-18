#!/usr/bin/env bash
# Run gramps' own unit test suite (*_test.py under gramps/**/test/) on
# Windows under MSYS2 MINGW64. No display, no AT-SPI — unit tests
# construct in-memory fixtures only.
#
# Companion to scripts/windows/run-addon-unit.sh. The Windows runners
# mirror scripts/ubuntu/ but run directly on the host (no Docker), since
# the AIO build chain Gramps already uses is MSYS2 — there is no Docker
# image equivalent for the Windows side of the testbed.
#
# Prerequisites:
#   - MSYS2 installed (https://www.msys2.org/), and this script invoked
#     from the "MSYS2 MINGW64" shell ($MSYSTEM == MINGW64).
#   - The pacman package list below is auto-installed via
#     `pacman -S --needed --noconfirm`; safe to re-run.
#
# Workspace layout matches the Ubuntu runners: this script's grandparent
# is the gramps-testbed checkout, and ../gramps lives next to it.

set -euo pipefail

if [[ "${MSYSTEM:-}" != "MINGW64" ]]; then
  echo "× This script must be run from the MSYS2 MINGW64 shell (MSYSTEM=MINGW64)." >&2
  echo "  Open 'MSYS2 MINGW64' from the Start menu and re-run." >&2
  exit 1
fi

WORKSPACE="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." && pwd)"
cd "$WORKSPACE"

# Pacman package list — minimal subset of aio/build.sh sufficient to
# import gramps.gen and run the *_test.py suite. The AIO build list is
# the authoritative source for what Gramps needs on Windows; this is a
# trimmed view that drops the cx_freeze / NSIS / dictionary tooling
# the runtime tests do not exercise.
PACMAN_PKGS=(
  mingw-w64-x86_64-python
  mingw-w64-x86_64-python-pip
  mingw-w64-x86_64-python-gobject
  mingw-w64-x86_64-python-cairo
  mingw-w64-x86_64-python-icu
  mingw-w64-x86_64-python-lxml
  mingw-w64-x86_64-python-jsonschema
  mingw-w64-x86_64-python-pillow
  mingw-w64-x86_64-gtk3
  mingw-w64-x86_64-osm-gps-map
  mingw-w64-x86_64-goocanvas
  mingw-w64-x86_64-gexiv2
  mingw-w64-x86_64-gettext
  intltool
)

echo "→ ensuring MSYS2 packages are installed"
pacman -S --needed --noconfirm "${PACMAN_PKGS[@]}"

# --system-site-packages keeps pip installs in the venv but inherits
# pacman-provided bindings (gi, cairo, icu, lxml, …). Same shape as the
# Ubuntu apt+venv arrangement; without it, gramps.gen's `import gi`
# blows up at test-collection time.
VENV="$WORKSPACE/.venv-windows"
if [[ ! -d "$VENV" ]]; then
  echo "→ creating venv at $VENV"
  /mingw64/bin/python -m venv --system-site-packages "$VENV"
fi
# shellcheck disable=SC1091
source "$VENV/Scripts/activate"
python -m pip install --upgrade pip

pip install -r "$WORKSPACE/gramps-testbed/requirements-test.txt"
# [testing] extras pulls in jsonschema/mock/lxml from gramps setup.py,
# matching scripts/ubuntu/run-unit.sh. pip rejects extras syntax on
# absolute paths, so cd in first.
(cd "$WORKSPACE" && pip install -e "./gramps[testing]")

# Compile .mo translations so gramps.gen imports do not emit
# "Missing or invalid localedir" warnings during collection.
if [[ ! -f "$WORKSPACE/gramps/build/mo/de/LC_MESSAGES/gramps.mo" ]]; then
  echo "→ compiling translations"
  for po in "$WORKSPACE"/gramps/po/*.po; do
    lang=$(basename "$po" .po)
    dest="$WORKSPACE/gramps/build/mo/$lang/LC_MESSAGES"
    mkdir -p "$dest"
    msgfmt "$po" -o "$dest/gramps.mo"
  done
fi

# Clear stale XMLs so accumulated runs do not pollute JUnit summaries.
RESULTS_DIR="$WORKSPACE/gramps-testbed/test-results"
rm -rf "$RESULTS_DIR"
mkdir -p "$RESULTS_DIR"

# Mirrors the canonical command from ../gramps/AGENTS.md:
#   GRAMPS_RESOURCES=. python3 -m unittest discover -p "*_test.py"
# xmlrunner is a drop-in replacement that writes JUnit XML. cygpath -w
# is required because /mingw64/bin/python is a Windows-native binary —
# POSIX-style paths from MSYS2 bash are not understood by Python's os
# layer when handed in via env or argv.
cd "$WORKSPACE/gramps"
GRAMPS_RESOURCES=. python -m xmlrunner discover \
  -p '*_test.py' \
  -o "$(cygpath -w "$RESULTS_DIR")" \
  -v
