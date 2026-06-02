#!/usr/bin/env bash
# Run per-addon unit test suites (addons-source/<addon>/tests/test_*.py
# and test_windows_*.py) on Windows under MSYS2 UCRT64. No display,
# no AT-SPI — these tests construct in-memory fixtures and/or exercise
# pure-logic helpers from the addon.
#
# Companion to agent-work/scripts/windows/run-unit.sh. Mirrors
# agent-work/scripts/ubuntu/run-addon-unit.sh, but runs directly on the host (no
# Docker) and inverts the OS-prefix filter:
#   test_*.py              general — runs here
#   test_linux_*.py        Linux-only — skipped here
#   test_windows_*.py      Windows-only — runs here
#   test_integration_*.py  Linux-only, full-pipeline — skipped here
#
# UCRT64 (vs MINGW64): required for orjson — see run-unit.sh for the
# longer rationale and the upstream #2198 reference.
#
# Usage:
#   ./agent-work/scripts/windows/run-addon-unit.sh                  # all addons with tests/
#   ./agent-work/scripts/windows/run-addon-unit.sh TMGimporter      # one addon
#   ./agent-work/scripts/windows/run-addon-unit.sh TMGimporter Form # several addons

set -euo pipefail

if [[ "${MSYSTEM:-}" != "UCRT64" ]]; then
  echo "× This script must be run from the MSYS2 UCRT64 shell (MSYSTEM=UCRT64)." >&2
  echo "  Open 'MSYS2 UCRT64' from the Start menu and re-run." >&2
  exit 1
fi

WORKSPACE="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." && pwd)"
cd "$WORKSPACE"

if [[ ! -d "$WORKSPACE/addons-source" ]]; then
  echo "× addons-source/ is missing — clone it next to gramps-testbed/ first." >&2
  exit 1
fi

# Pacman package list — kept in sync with agent-work/scripts/windows/run-unit.sh.
# Authoritative reference is aio/build.sh on maintenance/gramps61; this
# is the trimmed runtime subset (no cx_freeze / NSIS / dictionary
# tooling).
PACMAN_PKGS=(
  mingw-w64-ucrt-x86_64-python
  mingw-w64-ucrt-x86_64-python-pip
  mingw-w64-ucrt-x86_64-python-gobject
  mingw-w64-ucrt-x86_64-python-cairo
  mingw-w64-ucrt-x86_64-python-icu
  mingw-w64-ucrt-x86_64-python-lxml
  mingw-w64-ucrt-x86_64-python-jsonschema
  mingw-w64-ucrt-x86_64-python-pillow
  # python-maturin + rust: needed for orjson source build on UCRT64 —
  # see agent-work/scripts/windows/run-unit.sh for the full rationale.
  mingw-w64-ucrt-x86_64-python-maturin
  mingw-w64-ucrt-x86_64-rust
  mingw-w64-ucrt-x86_64-gtk3
  # Addon system deps (requires_gi). These are the Windows packages mapped in
  # agent-work/scripts/lib/addon_system_deps.py — the single source shared with the Ubuntu
  # image. Keep them equal to `addon_system_deps.py --platform windows`
  # (the drift-guard test_addon_system_deps enforces every dep is mapped).
  # Not derived inline here because the MSYS2 bootstrap installs python via
  # this very list, so python is not yet available to run the deriver; wiring
  # that two-phase install is a follow-up (needs a Windows host to verify).
  mingw-w64-ucrt-x86_64-osm-gps-map
  mingw-w64-ucrt-x86_64-goocanvas
  mingw-w64-ucrt-x86_64-gexiv2
  mingw-w64-ucrt-x86_64-gettext
  intltool
)

# Pinned-URL packages — see agent-work/scripts/windows/run-unit.sh for rationale.
# Kept in sync with aio/build.sh.
PACMAN_URL_PKGS=(
  https://repo.msys2.org/mingw/ucrt64/mingw-w64-ucrt-x86_64-enchant-2.6.7-5-any.pkg.tar.zst
  https://repo.msys2.org/mingw/ucrt64/mingw-w64-ucrt-x86_64-graphviz-12.2.1-4-any.pkg.tar.zst
  https://repo.msys2.org/mingw/ucrt64/mingw-w64-ucrt-x86_64-gspell-1.14.0-4-any.pkg.tar.zst
)

echo "→ ensuring MSYS2 packages are installed"
pacman -S --needed --noconfirm "${PACMAN_PKGS[@]}"
pacman -U --needed --noconfirm "${PACMAN_URL_PKGS[@]}"

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

TARGET_ADDONS="$*"

RESULTS_DIR="$WORKSPACE/gramps-testbed/test-results"
INSTALL_LOGS="$RESULTS_DIR/install-logs"
rm -rf "$RESULTS_DIR"
mkdir -p "$INSTALL_LOGS"

# orjson==3.11.7 build via pacman-supplied maturin (--no-build-isolation).
# See agent-work/scripts/windows/run-unit.sh for the full rationale around why this
# detour is necessary on UCRT64 Python 3.14 (no PyPI wheel + PyPI maturin
# source build also fails).
orjson_log="$INSTALL_LOGS/orjson-build.log"
{
  maturin --version
  python -c "import maturin; print('maturin', maturin.__file__)"
} >"$orjson_log" 2>&1 || {
  echo "× maturin import probe failed — last 40 lines of $orjson_log:" >&2
  tail -n 40 "$orjson_log" >&2
  exit 1
}
if ! pip install --progress-bar off -q --no-warn-script-location \
        --no-build-isolation --upgrade 'orjson==3.11.7' >>"$orjson_log" 2>&1; then
  echo "× orjson==3.11.7 build failed — last 40 lines of $orjson_log:" >&2
  tail -n 40 "$orjson_log" >&2
  exit 1
fi
# Smoke-test orjson — a Rust extension can install against the wrong ABI
# and segfault on import. Catch here, not deep into a test run.
if ! python -c "import orjson; orjson.dumps({'x':1}); orjson.loads(b'{\"y\":2}')" \
        >>"$orjson_log" 2>&1; then
  echo "× orjson import smoke-test failed — last 40 lines of $orjson_log:" >&2
  tail -n 40 "$orjson_log" >&2
  exit 1
fi

# Quiet mode + log capture for the gramps install: on failure we tail
# the log and surface the path; on success nothing is printed.
gramps_log="$INSTALL_LOGS/gramps-testing.log"
if ! (cd "$WORKSPACE" && pip install --progress-bar off -q \
        --no-warn-script-location -e "./gramps[testing]") \
        >"$gramps_log" 2>&1; then
  echo "× gramps[testing] install failed — last 40 lines of $gramps_log:" >&2
  tail -n 40 "$gramps_log" >&2
  exit 1
fi

# Auto-derive addon Python deps from requires_mod in every .gpr.py
# under addons-source/, then pip-install the union. Mirrors what
# Gramps Addon Manager does for an end user on Install click. The
# .gpr.py files are the single source of truth — keeps the test
# environment in sync with whatever the currently-checked-out
# addons-source declares.
echo "→ discovering addon deps from requires_mod declarations"
addon_mods=$(python - <<"PY"
import ast, glob, re
pat = re.compile(r"requires_mod\s*=\s*(\[[^\]]*\])")
mods = set()
for f in glob.glob("addons-source/*/*.gpr.py"):
    try:
        text = open(f, encoding="utf-8").read()
    except OSError:
        continue
    for m in pat.finditer(text):
        try:
            mods.update(ast.literal_eval(m.group(1)))
        except (ValueError, SyntaxError):
            pass
print(" ".join(sorted(mods)))
PY
)
pip_failures=()
if [[ -n "$addon_mods" ]]; then
  echo "→ addon deps: $addon_mods"
  # Install one at a time so a single failing build (psycopg2 without
  # libpq, pygraphviz without graphviz, etc.) does not abort the batch.
  # The affected addon's tests will skip or fail in isolation without
  # blocking the rest. Each install streams to its own log.
  for mod in $addon_mods; do
    mod_log="$INSTALL_LOGS/$mod.log"
    if pip install --progress-bar off -q --no-warn-script-location \
         "$mod" >"$mod_log" 2>&1; then
      :
    else
      pip_failures+=( "$mod" )
      echo "  × $mod failed — see install-logs/$mod.log"
    fi
  done
fi
find "$INSTALL_LOGS" -type f -empty -delete 2>/dev/null || true

# Compile .mo translations so gramps.gen imports do not emit
# "Missing or invalid localedir" during addon test collection.
if [[ ! -f "$WORKSPACE/gramps/build/mo/de/LC_MESSAGES/gramps.mo" ]]; then
  echo "→ compiling translations"
  for po in "$WORKSPACE"/gramps/po/*.po; do
    lang=$(basename "$po" .po)
    dest="$WORKSPACE/gramps/build/mo/$lang/LC_MESSAGES"
    mkdir -p "$dest"
    msgfmt "$po" -o "$dest/gramps.mo"
  done
fi

# Resolve target addon list.
if [[ -n "${TARGET_ADDONS:-}" ]]; then
  read -r -a addons <<< "$TARGET_ADDONS"
else
  addons=()
  for d in "$WORKSPACE"/addons-source/*/tests; do
    [[ -d "$d" ]] || continue
    parent_name=$(basename "$(dirname "$d")")
    [[ "$parent_name" == "addons-source" ]] && continue
    compgen -G "$d/test_*.py" >/dev/null || continue
    addons+=( "$parent_name" )
  done
fi

if [[ ${#addons[@]} -eq 0 ]]; then
  echo "no addons with tests/test_*.py were found" >&2
  exit 1
fi

echo "→ addon unit tests: ${addons[*]}"

# GRAMPS_RESOURCES needs a Windows path because /ucrt64/bin/python is
# Windows-native and does not understand POSIX-style /c/... paths.
GRAMPS_RESOURCES_WIN="$(cygpath -w "$WORKSPACE/gramps")"

fail=0
summary_lines=()
for addon in "${addons[@]}"; do
  test_dir="$WORKSPACE/addons-source/$addon/tests"
  if [[ ! -d "$test_dir" ]]; then
    echo "× $addon: addons-source/$addon/tests/ not found" >&2
    summary_lines+=( "$(printf "  %-30s  SKIP (tests/ not found)" "$addon")" )
    fail=1
    continue
  fi
  echo
  echo "=== $addon ==="
  out_dir="$RESULTS_DIR/$addon"
  mkdir -p "$out_dir"
  # Filename convention (mirrors
  # addons-source/.github/workflows/ci.yml). This is the Windows
  # runner, so test_linux_* and test_integration_* are excluded;
  # test_windows_* is included alongside the platform-neutral test_*.
  modules=()
  for f in "$WORKSPACE"/addons-source/"$addon"/tests/test_*.py; do
    [[ -f "$f" ]] || continue
    case "$(basename "$f")" in
      test_linux_*|test_integration_*) continue ;;
    esac
    rel="${f#$WORKSPACE/addons-source/}"
    mod="${rel%.py}"
    mod="${mod//\//.}"
    modules+=( "$mod" )
  done
  if [[ ${#modules[@]} -eq 0 ]]; then
    echo "× $addon: no Windows-eligible test_*.py in tests/" >&2
    summary_lines+=( "$(printf "  %-30s  SKIP (no test_*.py)" "$addon")" )
    fail=1
    continue
  fi
  run_log="$out_dir/_run.log"
  out_dir_win="$(cygpath -w "$out_dir")"
  (
    cd "$WORKSPACE/addons-source"
    GRAMPS_RESOURCES="$GRAMPS_RESOURCES_WIN" \
      python -m xmlrunner "${modules[@]}" \
        -o "$out_dir_win" \
        -v
  ) 2>&1 | tee "$run_log"
  rc=${PIPESTATUS[0]}
  ran=$(grep -oE "Ran [0-9]+ tests" "$run_log" | tail -n 1 | grep -oE "[0-9]+" || true)
  ran="${ran:-?}"
  if [[ "$rc" -eq 0 ]]; then
    summary_lines+=( "$(printf "  %-30s  PASS  (%s tests)" "$addon" "$ran")" )
  else
    fail=1
    detail=$(grep -oE "FAILED \([^)]*\)" "$run_log" | tail -n 1 || true)
    detail="${detail:-crashed}"
    summary_lines+=( "$(printf "  %-30s  FAIL  (%s tests, %s)" "$addon" "$ran" "$detail")" )
  fi
done

echo
echo "=== Summary ==="
for line in "${summary_lines[@]}"; do
  echo "$line"
done
echo
echo "→ JUnit XMLs + per-addon _run.log: gramps-testbed/test-results/<addon>/"
if [[ ${#pip_failures[@]} -gt 0 ]]; then
  echo "→ pip install logs (${#pip_failures[@]} failure(s)): gramps-testbed/test-results/install-logs/"
fi
exit $fail
