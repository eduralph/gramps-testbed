#!/usr/bin/env python3
"""
Single source of truth for addon *Python* dependencies (``requires_mod``).

Sibling to ``addon_system_deps.py`` (which covers the *system* deps —
``requires_gi`` typelibs and ``requires_exe`` executables). This module covers
the third kind a Gramps addon declares in its ``.gpr.py``:

* ``requires_mod`` — importable, pip-installable Python modules
  (e.g. ``["psycopg2"]``, ``["life_line_chart", "svgwrite"]``).

The addon-unit CI jobs (``addon-unit-tests.yml`` and
``windows-addon-unit-tests.yml``) install these before running each addon's
test suite. Both jobs previously inlined an identical
``requires_mod\\s*=\\s*(\\[[^\\]]*\\])`` heredoc; that copy-paste is the drift
this module removes — the ``.gpr.py`` files stay the single source of truth and
both platforms now derive the list from one place.

Scanning approach matches ``addon_system_deps.py`` deliberately: a regex to
find each ``requires_mod = [...]`` assignment, then ``ast.literal_eval`` on the
bracketed list. Both sibling scanners therefore use the same mechanism, and the
module stays pure stdlib (no Gramps import, no executing the ``.gpr.py``), so it
can run at image-build time before Gramps is installed. Every real
``requires_mod`` in addons-source is a flat string literal, so a literal-eval
parse covers them all; a non-literal or unreadable declaration is skipped
tolerantly (logged to stderr) rather than aborting the batch — mirroring the
old inline behaviour.

CLI::

    addon_python_deps.py <addons-source-dir>     # space-separated sorted union
"""

from __future__ import annotations

import argparse
import ast
import glob
import os
import re
import sys

# Matches a single-line ``requires_mod = ["a", "b"]`` assignment. Flat string
# lists only — the same shape addon_system_deps.py's _GI_RE/_EXE_RE assume, and
# the only shape that occurs in addons-source.
_MOD_RE = re.compile(r"requires_mod\s*=\s*(\[[^\]]*\])")


def _gpr_files(addons_dir: str) -> list[str]:
    return sorted(glob.glob(os.path.join(addons_dir, "*", "*.gpr.py")))


def requires_mod_union(addons_dir: str) -> list[str]:
    """Return the sorted union of ``requires_mod`` across every addon's
    ``.gpr.py`` under *addons_dir*.

    Best-effort and tolerant: a file that cannot be read, or a
    ``requires_mod`` value that is not a literal list, is skipped (with a note
    to stderr) instead of aborting — the addon-unit jobs would rather install
    the modules they *can* resolve than fail the whole step on one odd file.
    """
    mods: set[str] = set()
    for path in _gpr_files(addons_dir):
        try:
            with open(path, encoding="utf-8") as fh:
                text = fh.read()
        except OSError as exc:
            print(f"addon_python_deps: skipping unreadable {path}: {exc}",
                  file=sys.stderr)
            continue
        for m in _MOD_RE.finditer(text):
            try:
                value = ast.literal_eval(m.group(1))
            except (ValueError, SyntaxError):
                print(f"addon_python_deps: skipping non-literal requires_mod "
                      f"in {path}: {m.group(1)!r}", file=sys.stderr)
                continue
            for mod in value:
                if mod:
                    mods.add(mod)
    return sorted(mods)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "addons_dir",
        help="path to the addons-source checkout (scans <dir>/*/*.gpr.py)",
    )
    args = parser.parse_args(argv)
    print(" ".join(requires_mod_union(args.addons_dir)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
