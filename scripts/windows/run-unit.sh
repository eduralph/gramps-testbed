#!/usr/bin/env bash
# Run gramps' own unit test suite (*_test.py under gramps/**/test/) on
# Windows under MSYS2 UCRT64. No display, no AT-SPI — unit tests
# construct in-memory fixtures only.
#
# Companion to scripts/windows/run-addon-unit.sh. The Windows runners
# mirror scripts/ubuntu/ but run directly on the host (no Docker), since
# the AIO build chain Gramps already uses is MSYS2 — there is no Docker
# image equivalent for the Windows side of the testbed.
#
# UCRT64 (vs the older MINGW64) is required: MINGW64's Python target
# triple `mingw_x86_64_msvcrt_gnu` is rejected by orjson's maturin
# backend, blocking `pip install -e gramps[testing]`. UCRT64's `ucrt`
# triple resolves orjson on PyPI. Migrated upstream by gramps PR #2198
# (merged on maintenance/gramps61 2026-04-19).
#
# Prerequisites:
#   - MSYS2 installed (https://www.msys2.org/), and this script invoked
#     from the "MSYS2 UCRT64" shell ($MSYSTEM == UCRT64).
#   - The pacman package list below is auto-installed via
#     `pacman -S --needed --noconfirm`; safe to re-run.
#
# Workspace layout matches the Ubuntu runners: this script's grandparent
# is the gramps-testbed checkout, and ../gramps lives next to it.

set -euo pipefail

if [[ "${MSYSTEM:-}" != "UCRT64" ]]; then
  echo "× This script must be run from the MSYS2 UCRT64 shell (MSYSTEM=UCRT64)." >&2
  echo "  Open 'MSYS2 UCRT64' from the Start menu and re-run." >&2
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
  mingw-w64-ucrt-x86_64-python
  mingw-w64-ucrt-x86_64-python-pip
  mingw-w64-ucrt-x86_64-python-gobject
  mingw-w64-ucrt-x86_64-python-cairo
  mingw-w64-ucrt-x86_64-python-icu
  mingw-w64-ucrt-x86_64-python-lxml
  mingw-w64-ucrt-x86_64-python-jsonschema
  mingw-w64-ucrt-x86_64-python-pillow
  mingw-w64-ucrt-x86_64-gexiv2
  mingw-w64-ucrt-x86_64-gtk3
  mingw-w64-ucrt-x86_64-osm-gps-map
  mingw-w64-ucrt-x86_64-goocanvas
  mingw-w64-ucrt-x86_64-gettext
  intltool
)

# Pinned-URL packages — graphviz/gspell/enchant ship newer versions in
# the MSYS2 main repos that break pygraphviz and spellcheck, so
# aio/build.sh pins the 6.0.8-era artefacts via `pacman -U` from
# repo.msys2.org. Keep these URLs in sync with aio/build.sh when AIO
# bumps the versions. (gexiv2 is no longer pinned post-#2198 — it now
# comes from the regular UCRT64 install set, with exiv2 as a
# transitive dep.)
PACMAN_URL_PKGS=(
  https://repo.msys2.org/mingw/ucrt64/mingw-w64-ucrt-x86_64-enchant-2.6.7-5-any.pkg.tar.zst
  https://repo.msys2.org/mingw/ucrt64/mingw-w64-ucrt-x86_64-graphviz-12.2.1-4-any.pkg.tar.zst
  https://repo.msys2.org/mingw/ucrt64/mingw-w64-ucrt-x86_64-gspell-1.14.0-4-any.pkg.tar.zst
)

echo "→ ensuring MSYS2 packages are installed"
pacman -S --needed --noconfirm "${PACMAN_PKGS[@]}"
pacman -U --needed --noconfirm "${PACMAN_URL_PKGS[@]}"

# --system-site-packages keeps pip installs in the venv but inherits
# pacman-provided bindings (gi, cairo, icu, lxml, …). Same shape as the
# Ubuntu apt+venv arrangement; without it, gramps.gen's `import gi`
# blows up at test-collection time.
VENV="$WORKSPACE/.venv-windows"
if [[ ! -d "$VENV" ]]; then
  echo "→ creating venv at $VENV"
  /ucrt64/bin/python -m venv --system-site-packages "$VENV"
fi
# MSYS2 UCRT64 Python uses POSIX venv layout (bin/), not Windows
# CPython's Scripts/ — see windows-unit-tests.yml for rationale.
# shellcheck disable=SC1091
source "$VENV/bin/activate"
python -m pip install --upgrade pip

# orjson==3.11.7 pre-pin mirrors aio/build.sh:83 on
# maintenance/gramps61 (Steve Youngs, commit 3d99a8d9, "Pin orjson to
# 3.11.7"). orjson has no MSYS2 wheel at any version — pip always
# source-builds via maturin. Under UCRT64 Python 3.14 the unpinned
# latest (3.11.9) pulls in a maturin version whose own source build
# fails; 3.11.7 builds cleanly. Without this pre-pin,
# `pip install -e gramps[testing]` resolves orjson transitively and
# dies on the maturin build. Keep in sync with aio/build.sh.
pip install --upgrade 'orjson==3.11.7'
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
# is required because /ucrt64/bin/python is a Windows-native binary —
# POSIX-style paths from MSYS2 bash are not understood by Python's os
# layer when handed in via env or argv.
cd "$WORKSPACE/gramps"
GRAMPS_RESOURCES=. python -m xmlrunner discover \
  -p '*_test.py' \
  -o "$(cygpath -w "$RESULTS_DIR")" \
  -v
