#!/usr/bin/env bash
# Run per-addon unit test suites (addons-source/<addon>/tests/test_*.py)
# locally on the Ubuntu Docker base, using the same commands as CI.
# No display, no dbus, no AT-SPI — these tests construct in-memory fixtures
# and/or exercise pure-logic helpers from the addon.
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

# Positional args are passed through to the container as a whitespace-
# separated list. Empty = "discover all addons with tests/test_*.py".
TARGET_ADDONS="$*"

docker run --rm \
  -v "$WORKSPACE":/workspace \
  -w /workspace \
  -e "TARGET_ADDONS=$TARGET_ADDONS" \
  "$IMAGE" \
  bash -lc '
    set -e
    # [testing] extras pulls in jsonschema/mock/lxml from gramps setup.py,
    # which some addon tests also import transitively. pip rejects the
    # extras syntax against absolute paths, so resolve via a relative path.
    (cd /workspace && pip install --break-system-packages --user -e "./gramps[testing]")
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
    if [ -n "$addon_mods" ]; then
      echo "→ addon deps: $addon_mods"
      # Install one at a time so a single failing build (pygraphviz
      # without graphviz-dev, psycopg2 without libpq-dev, etc.) does
      # not abort the batch. The affected addon''s tests will skip or
      # fail in isolation without blocking the rest.
      for mod in $addon_mods; do
        pip install --break-system-packages --user "$mod" \
          || echo "× $mod failed to install (continuing)"
      done
    fi

    # Compile .mo translations so gramps.gen imports do not emit
    # "Missing or invalid localedir" during addon test collection.
    if [ ! -f /workspace/gramps/build/mo/de/LC_MESSAGES/gramps.mo ]; then
      echo "→ compiling translations"
      for po in /workspace/gramps/po/*.po; do
        lang=$(basename "$po" .po)
        dest="/workspace/gramps/build/mo/$lang/LC_MESSAGES"
        mkdir -p "$dest"
        msgfmt "$po" -o "$dest/gramps.mo"
      done
    fi

    # Clear stale XMLs so accumulated runs do not pollute JUnit summaries.
    rm -rf /workspace/gramps-testbed/test-results
    mkdir -p /workspace/gramps-testbed/test-results

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
    for addon in "${addons[@]}"; do
      test_dir="/workspace/addons-source/$addon/tests"
      if [ ! -d "$test_dir" ]; then
        echo "× $addon: addons-source/$addon/tests/ not found" >&2
        fail=1
        continue
      fi
      echo
      echo "=== $addon ==="
      # Each addon gets its own results subdir so JUnit class/file names do
      # not collide across addons. GRAMPS_RESOURCES pins the resource root
      # for any addon test that touches gramps.gen resource loading.
      out_dir="/workspace/gramps-testbed/test-results/$addon"
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
      modules=()
      for f in /workspace/addons-source/"$addon"/tests/test_*.py; do
        [ -f "$f" ] || continue
        rel="${f#/workspace/addons-source/}"
        mod="${rel%.py}"
        mod="${mod//\//.}"
        modules+=( "$mod" )
      done
      if [ ${#modules[@]} -eq 0 ]; then
        echo "× $addon: no test_*.py in tests/" >&2
        fail=1
        continue
      fi
      (
        cd /workspace/addons-source
        GRAMPS_RESOURCES=/workspace/gramps \
          python3 -m xmlrunner "${modules[@]}" \
            -o "$out_dir" \
            -v
      ) || fail=1
    done
    exit $fail
  '
