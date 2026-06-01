"""Unit tests for ``scripts/lib/addon_python_deps.py``.

The addon-unit CI jobs (Linux + Windows) install each addon's ``requires_mod``
Python deps before running its tests. That derivation used to be a regex
heredoc copy-pasted into both workflows; it now lives once in
``addon_python_deps.py``. These tests pin the extractor's contract on
controlled ``.gpr.py`` fixtures so a future change to the scanner can't
silently drop a declared module.

Scope of what is asserted, matching the deliberate regex + ``ast.literal_eval``
design (same mechanism as the sibling ``addon_system_deps.py``; no execution of
the ``.gpr.py``):

* literal ``requires_mod`` lists across multiple addons are unioned and sorted;
* a ``.gpr.py`` whose top level would *raise if executed* is still parsed (the
  regex reads the source, it never runs it) — a concrete robustness win over an
  exec-based shim;
* a non-literal ``requires_mod`` (a name/expression inside the brackets) is
  skipped tolerantly without aborting the batch — every real addons-source
  declaration is a flat literal, so this only guards the odd-file path.
"""

from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

# scripts/lib holds the extractor; make it importable (mirrors
# tests/test_addon_system_deps.py).
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts" / "lib"))
import addon_python_deps as deps  # noqa: E402


def _write_addon(root: Path, name: str, gpr_body: str) -> None:
    """Create ``root/<name>/<name>.gpr.py`` containing *gpr_body*."""
    addon = root / name
    addon.mkdir(parents=True)
    (addon / f"{name}.gpr.py").write_text(gpr_body, encoding="utf-8")


class RequiresModUnionTest(unittest.TestCase):
    def test_literal_lists_unioned_and_sorted(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            _write_addon(root, "AddonA",
                         'register(GRAMPLET, requires_mod=["zlib_mod", '
                         '"alpha_mod"])\n')
            _write_addon(root, "AddonB",
                         "register(TOOL, requires_mod=['beta_mod'])\n")
            self.assertEqual(
                deps.requires_mod_union(str(root)),
                ["alpha_mod", "beta_mod", "zlib_mod"],
            )

    def test_duplicate_modules_collapse(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            _write_addon(root, "AddonA", 'register(requires_mod=["dbf"])\n')
            _write_addon(root, "AddonB", 'register(requires_mod=["dbf"])\n')
            self.assertEqual(deps.requires_mod_union(str(root)), ["dbf"])

    def test_file_that_would_raise_on_exec_is_still_parsed(self) -> None:
        # A .gpr.py that raises at import/exec time. The regex reads the
        # source without executing it, so the literal requires_mod is still
        # captured — an exec-based shim would have lost this addon's deps.
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            _write_addon(root, "Boomer",
                         'raise RuntimeError("boom at module top level")\n'
                         'register(requires_mod=["gamma_mod"])\n')
            self.assertEqual(deps.requires_mod_union(str(root)), ["gamma_mod"])

    def test_non_literal_requires_mod_is_skipped_without_aborting(self) -> None:
        # A non-literal value inside the brackets (a bare name) can't be
        # literal_eval'd; it must be skipped while the sibling addon's literal
        # list is still returned.
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            _write_addon(root, "Computed",
                         "_BASE = 'x'\nregister(requires_mod=[_BASE])\n")
            _write_addon(root, "Literal",
                         'register(requires_mod=["good_mod"])\n')
            self.assertEqual(deps.requires_mod_union(str(root)), ["good_mod"])

    def test_no_gpr_files_returns_empty(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            self.assertEqual(deps.requires_mod_union(tmp), [])

    def test_gpr_without_requires_mod_is_ignored(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            _write_addon(root, "NoDeps", "register(GRAMPLET, id='x')\n")
            self.assertEqual(deps.requires_mod_union(str(root)), [])


if __name__ == "__main__":
    unittest.main()
