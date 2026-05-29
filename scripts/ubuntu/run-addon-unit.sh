#!/usr/bin/env bash
# Run per-addon unit test suites (addons-source/<addon>/tests/test_*.py)
# locally on the Ubuntu Docker base, using the same commands as CI.
# No display, no dbus, no AT-SPI — these tests construct in-memory fixtures
# and/or exercise pure-logic helpers from the addon.
#
# After the per-addon suites, a translation-catalog gate runs msgfmt over
# every addons-source/<addon>/po/*.po — the step `make.py build` itself
# performs — so a catalog regression that would abort an addon build is
# caught here too.
#
# Companion to scripts/ubuntu/run-unit.sh (gramps core unit suite) and
# scripts/ubuntu/run-interface.sh (GUI tests via dogtail).
#
# Addon tests follow Python stdlib convention (test_*.py) rather than
# gramps' own (*_test.py). Most addons add their containing dir to sys.path
# inside the test file, so discover runs from the tests/ directory directly.
#
# Usage:
#   ./scripts/ubuntu/run-addon-unit.sh                    # all addons with tests/
#   ./scripts/ubuntu/run-addon-unit.sh TMGimporter        # one addon
#   ./scripts/ubuntu/run-addon-unit.sh TMGimporter Form   # several addons

set -euo pipefail

WORKSPACE="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." && pwd)"
cd "$WORKSPACE"

if [[ ! -d "$WORKSPACE/addons-source" ]]; then
  echo "addons-source/ is missing — run ./scripts/bootstrap-forks.sh first." >&2
  exit 1
fi

# Tag the image with platform + Gramps version so multiple versions can
# coexist on the same machine. Read VERSION_TUPLE from gramps' own
# source-of-truth.
GRAMPS_VERSION="$(sed -nE 's/^VERSION_TUPLE *= *\(([0-9]+), *([0-9]+), *([0-9]+)\).*$/\1.\2.\3/p' "$WORKSPACE/gramps/gramps/version.py")"
: "${GRAMPS_VERSION:?could not detect Gramps version from gramps/version.py}"
IMAGE="${GRAMPS_TESTBED_IMAGE:-gramps-testbed:ubuntu-$GRAMPS_VERSION}"

if ! docker image inspect "$IMAGE" >/dev/null 2>&1; then
  echo "→ building $IMAGE"
  docker build -f gramps-testbed/docker/Dockerfile.ubuntu -t "$IMAGE" gramps-testbed
fi

# Auto-clean stale gramps/build/ before the in-container pip install.
# gramps' build_hook rmtrees this dir at install time and dies with
# PermissionError when prior runs left it owned by a uid that doesn't
# match the host user (typical when the container's `runner` uid=1000
# != the host uid, or after a one-off `docker run -u root` left
# root-owned artefacts). clean-build.sh picks host-side rm or
# container-as-root rm based on actual permissions.
build_dir="$WORKSPACE/gramps/build"
if [[ -d "$build_dir" ]] && [[ "$(stat -c %u "$build_dir" 2>/dev/null || echo 0)" != "$(id -u)" ]]; then
  echo "→ stale gramps/build/ detected (uid mismatch); calling clean-build.sh"
  "$WORKSPACE/gramps-testbed/scripts/ubuntu/clean-build.sh"
fi

# Positional args are passed through to the container as a whitespace-
# separated list. Empty = "discover all addons with tests/test_*.py".
TARGET_ADDONS="$*"

docker run --rm \
  -v "$WORKSPACE":/workspace \
  -w /workspace \
  -e "TARGET_ADDONS=$TARGET_ADDONS" \
  "$IMAGE" \
  bash -c '
    set -e
    # Clear stale XMLs / logs so accumulated runs do not pollute the summary.
    # Created early so pip install logs land under install-logs/ too.
    results_dir="/workspace/gramps-testbed/test-results"
    install_logs="$results_dir/install-logs"
    rm -rf "$results_dir"
    mkdir -p "$install_logs"

    # [testing] extras pulls in jsonschema/mock/lxml from gramps setup.py,
    # which some addon tests also import transitively. pip rejects the
    # extras syntax against absolute paths, so resolve via a relative path.
    # Quiet mode + log capture: on failure we tail the log and surface the
    # path; on success nothing is printed so the runs-for-every-invocation
    # noise does not drown the actual test output.
    gramps_log="$install_logs/gramps-testing.log"
    if ! (cd /workspace && pip install --break-system-packages --user \
            --progress-bar off -q --no-warn-script-location \
            -e "./gramps[testing]") \
            >"$gramps_log" 2>&1; then
      echo "× gramps[testing] install failed — last 40 lines of $gramps_log:" >&2
      tail -n 40 "$gramps_log" >&2
      exit 1
    fi
    export PATH="$HOME/.local/bin:$PATH"

    # Auto-derive addon Python deps from requires_mod in every .gpr.py
    # under addons-source/, then pip-install the union. Mirrors what
    # Gramps Addon Manager does for an end user on Install click (see
    # gramps/gui/plug/_windows.py __on_install_clicked → req.install →
    # gen/utils/requirements.py). The .gpr.py files are the single
    # source of truth — this keeps the test environment in sync with
    # whatever the currently-checked-out addons-source declares, so
    # new addon deps do not need a parallel update here.
    echo "→ discovering addon deps from requires_mod declarations"
    addon_mods=$(python3 - <<"PY"
import ast, glob, re
pat = re.compile(r"requires_mod\s*=\s*(\[[^\]]*\])")
mods = set()
for f in glob.glob("/workspace/addons-source/*/*.gpr.py"):
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
    if [ -n "$addon_mods" ]; then
      echo "→ addon deps: $addon_mods"
      # Install one at a time so a single failing build (pygraphviz
      # without graphviz-dev, psycopg2 without libpq-dev, etc.) does
      # not abort the batch. The affected addon''s tests will skip or
      # fail in isolation without blocking the rest. Each install
      # streams to its own log; only failures print to the terminal.
      for mod in $addon_mods; do
        mod_log="$install_logs/$mod.log"
        if pip install --break-system-packages --user \
             --progress-bar off -q --no-warn-script-location \
             "$mod" >"$mod_log" 2>&1; then
          :
        else
          pip_failures+=( "$mod" )
          echo "  × $mod failed — see install-logs/$mod.log"
        fi
      done
    fi
    # Drop zero-byte logs so install-logs/ retains only real failures.
    find "$install_logs" -type f -empty -delete 2>/dev/null || true

    # Compile .mo translations so gramps.gen imports do not emit
    # "Missing or invalid localedir" during addon test collection.
    if [ ! -f /workspace/gramps/build/mo/de/LC_MESSAGES/gramps.mo ]; then
      echo "→ compiling translations"
      for po in /workspace/gramps/po/*.po; do
        lang=$(basename "$po" .po)
        dest="/workspace/gramps/build/mo/$lang/LC_MESSAGES"
        mkdir -p "$dest"
        # A single malformed upstream catalog (e.g. po/mn.po with mismatched
        # plural \n entries) must not abort the addon-unit run under set -e
        # before any test executes. Skip it, drop any partial .mo, and carry
        # on — that locale just falls back to English, which does not affect
        # the addon test suites. Mirrors run-manual.sh.
        if ! msgfmt "$po" -o "$dest/gramps.mo" 2>/dev/null; then
          echo "  ⚠ skipping $lang — msgfmt rejected $po (malformed catalog)"
          rm -f "$dest/gramps.mo"
        fi
      done
    fi

    # Resolve target addon list.
    if [ -n "${TARGET_ADDONS:-}" ]; then
      addons=( $TARGET_ADDONS )
    else
      addons=()
      for d in /workspace/addons-source/*/tests; do
        [ -d "$d" ] || continue
        # Skip addons-source/tests/ — top-level helpers, not an addon.
        parent_name=$(basename "$(dirname "$d")")
        [ "$parent_name" = "addons-source" ] && continue
        # Must contain at least one test_*.py.
        compgen -G "$d/test_*.py" >/dev/null || continue
        addons+=( "$parent_name" )
      done
    fi

    if [ ${#addons[@]} -eq 0 ]; then
      echo "no addons with tests/test_*.py were found" >&2
      exit 1
    fi

    echo "→ addon unit tests: ${addons[*]}"

    fail=0
    summary_lines=()
    for addon in "${addons[@]}"; do
      test_dir="/workspace/addons-source/$addon/tests"
      if [ ! -d "$test_dir" ]; then
        echo "× $addon: addons-source/$addon/tests/ not found" >&2
        summary_lines+=( "$(printf "  %-30s  SKIP (tests/ not found)" "$addon")" )
        fail=1
        continue
      fi
      echo
      echo "=== $addon ==="
      # Each addon gets its own results subdir so JUnit class/file names do
      # not collide across addons. GRAMPS_RESOURCES pins the resource root
      # for any addon test that touches gramps.gen resource loading.
      out_dir="$results_dir/$addon"
      mkdir -p "$out_dir"
      # Collect dotted module paths (<Addon>.tests.<module>) and invoke
      # unittest/xmlrunner with the module list, running from
      # addons-source/. This mirrors how addons-source/.github/workflows/
      # ci.yml calls the suite and how contributors invoke
      # "python3 -m unittest <Addon>.tests.test_..." locally. Critically,
      # loading a test via its dotted path — not via "discover" inside
      # tests/ — puts the addon on sys.modules as a namespace package
      # before the test body runs. That is the exact arrangement that
      # surfaces package-shadowing bugs like bug 0012691, where
      # "from <Addon> import <Addon>" binds the submodule instead of the
      # class. Discover-from-tests/ hides the trap.
      # Filename convention (mirrors addons-source/.github/workflows/ci.yml):
      #   test_*.py              general — every platform
      #   test_linux_*.py        Linux-only
      #   test_windows_*.py      Windows-only (skipped here)
      #   test_integration_*.py  Linux-only, full-pipeline/DB-backed
      # This is the Ubuntu runner, so test_windows_* is excluded. When
      # scripts/windows/run-addon-unit.sh is added it will do the inverse
      # (skip test_linux_*/test_integration_*).
      modules=()
      for f in /workspace/addons-source/"$addon"/tests/test_*.py; do
        [ -f "$f" ] || continue
        case "$(basename "$f")" in
          test_windows_*) continue ;;
        esac
        rel="${f#/workspace/addons-source/}"
        mod="${rel%.py}"
        mod="${mod//\//.}"
        modules+=( "$mod" )
      done
      if [ ${#modules[@]} -eq 0 ]; then
        echo "× $addon: no test_*.py in tests/" >&2
        summary_lines+=( "$(printf "  %-30s  SKIP (no test_*.py)" "$addon")" )
        fail=1
        continue
      fi
      # Tee xmlrunner output to a per-addon log so the summary at the end
      # can point at a file with the full -v trace, including failures.
      run_log="$out_dir/_run.log"
      (
        cd /workspace/addons-source
        # Run under Xvfb (mirrors run-interface.sh). Some addons import Gtk
        # modules that create a style context at import time, which needs a
        # display connection; without one the interpreter aborts with a
        # Gtk-ERROR about being unable to create a GtkStyleContext, rather
        # than letting the import guard in the test skip cleanly. Headless
        # addon tests are unaffected by the extra display.
        # (No raw apostrophes in this block: it runs inside docker bash -c.)
        GRAMPS_RESOURCES=/workspace/gramps \
          xvfb-run -a --server-args="-screen 0 1920x1080x24" \
            python3 -m xmlrunner "${modules[@]}" \
              -o "$out_dir" \
              -v
      ) 2>&1 | tee "$run_log"
      rc=${PIPESTATUS[0]}
      # Parse "Ran N tests in Xs" and the trailing OK/FAILED line to build
      # a one-line summary entry. Tolerant of Python-exception aborts that
      # produce no "Ran" line at all (ran stays "?").
      ran=$(grep -oE "Ran [0-9]+ tests" "$run_log" | tail -n 1 | grep -oE "[0-9]+" || true)
      ran="${ran:-?}"
      if [ "$rc" -eq 0 ]; then
        summary_lines+=( "$(printf "  %-30s  PASS  (%s tests)" "$addon" "$ran")" )
      else
        fail=1
        detail=$(grep -oE "FAILED \([^)]*\)" "$run_log" | tail -n 1 || true)
        detail="${detail:-crashed}"
        summary_lines+=( "$(printf "  %-30s  FAIL  (%s tests, %s)" "$addon" "$ran" "$detail")" )
      fi
    done

    # Translation-catalog gate: every addons-source/<addon>/po/*.po must
    # compile with msgfmt — the same step `make.py build` runs. A rejected
    # catalog aborts the addon build (Mantis bug 14234), and addons-source
    # has no unit-test CI of its own, so this testbed check is the only
    # automated guard. PIPESTATUS (not pipefail) keeps the tee from
    # masking the real xmlrunner exit code, as in the loop above.
    echo
    echo "=== addon translation catalogs ==="
    cat_out="$results_dir/_po-catalogs"
    mkdir -p "$cat_out"
    cat_log="$cat_out/_run.log"
    (
      cd /workspace/gramps-testbed
      ADDONS_SOURCE=/workspace/addons-source \
        python3 -m xmlrunner tests.test_addon_po_catalogs -o "$cat_out" -v
    ) 2>&1 | tee "$cat_log"
    if [ "${PIPESTATUS[0]}" -eq 0 ]; then
      summary_lines+=( "$(printf "  %-30s  PASS" "po-catalogs")" )
    else
      fail=1
      summary_lines+=( "$(printf "  %-30s  FAIL  (see _po-catalogs/_run.log)" "po-catalogs")" )
    fi

    # System-dependency drift gate: every requires_gi / requires_exe an addon
    # declares must be mapped in scripts/lib/addon_system_deps.py, and every
    # such dep of a tested addon must be present in this image (GRAMPS_TESTBED
    # is set in the image so the presence check runs). Catches the per-platform
    # drift that left graphviz/`dot` out of the image.
    echo
    echo "=== addon system dependencies ==="
    sysdeps_out="$results_dir/_system-deps"
    mkdir -p "$sysdeps_out"
    sysdeps_log="$sysdeps_out/_run.log"
    (
      cd /workspace/gramps-testbed
      ADDONS_SOURCE=/workspace/addons-source \
        python3 -m xmlrunner tests.test_addon_system_deps -o "$sysdeps_out" -v
    ) 2>&1 | tee "$sysdeps_log"
    if [ "${PIPESTATUS[0]}" -eq 0 ]; then
      summary_lines+=( "$(printf "  %-30s  PASS" "system-deps")" )
    else
      fail=1
      summary_lines+=( "$(printf "  %-30s  FAIL  (see _system-deps/_run.log)" "system-deps")" )
    fi

    echo
    echo "=== Summary ==="
    for line in "${summary_lines[@]}"; do
      echo "$line"
    done
    echo
    echo "→ JUnit XMLs + per-addon _run.log: gramps-testbed/test-results/<addon>/"
    if [ ${#pip_failures[@]} -gt 0 ]; then
      echo "→ pip install logs (${#pip_failures[@]} failure(s)): gramps-testbed/test-results/install-logs/"
    fi
    exit $fail
  '
