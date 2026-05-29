"""Drift-guard for addon *system* dependencies (requires_gi / requires_exe).

Addon Python deps (``requires_mod``) are auto-derived from the ``.gpr.py``
files and pip-installed at run start, so they cannot drift. Addon *system*
deps — GI typelibs (``requires_gi``) and executables (``requires_exe``) — are
not pip-installable and must be provided by the environment (the Docker image,
the apt step in CI, the MSYS2 pacman lists). Those lists were hand-maintained
per platform and silently drifted: the Ubuntu image lacked ``graphviz`` while
Windows had it, and an addon whose import needs a missing typelib does not fail
loudly — it skips, leaving green CI that tested nothing.

``scripts/lib/addon_system_deps.py`` is now the single source mapping each
declared dependency to its per-platform package. This test guards it two ways:

* **completeness** — every GI namespace / executable any addon declares has a
  map entry, so a newly-added dependency forces a (one-line) map update instead
  of silently going uninstalled. Always runs; pure static check.

* **presence** — for every addon that ships a test suite (i.e. whose module the
  runner actually imports), each declared GI namespace is importable and each
  executable is on ``PATH``. This is what catches an image/CI that is missing a
  package an exercised addon needs. Gated on ``$GRAMPS_TESTBED`` so it asserts
  only in the official test environment (the image / CI export it); on a bare
  developer box without the addon GI stack it skips rather than false-failing.
"""

from __future__ import annotations

import glob
import importlib
import os
import shutil
import sys
import unittest
from pathlib import Path

# scripts/lib holds the single-source map; make it importable.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts" / "lib"))
import addon_system_deps as deps  # noqa: E402


def _find_addons_source() -> Path | None:
    for var in ("ADDONS_SOURCE", "ADDONS_SOURCE_DIR"):
        val = os.environ.get(var)
        if val and Path(val).is_dir():
            return Path(val).resolve()
    sibling = Path(__file__).resolve().parents[2] / "addons-source"
    return sibling if sibling.is_dir() else None


ADDONS_SOURCE = _find_addons_source()
# Set in the testbed image / CI; absent on a bare dev box.
IN_TEST_ENV = bool(os.environ.get("GRAMPS_TESTBED"))


def _addons_with_tests(root: Path) -> list[Path]:
    dirs = {
        Path(p).parent.parent
        for p in glob.glob(str(root / "*" / "tests" / "test_*.py"))
    }
    return sorted(dirs)


# ------------------------------------------------------------
#
# AddonSystemDepsCompletenessTest
#
# ------------------------------------------------------------
@unittest.skipUnless(ADDONS_SOURCE, "addons-source checkout not found")
class AddonSystemDepsCompletenessTest(unittest.TestCase):
    """Every declared system dependency must be known to the map."""

    def test_all_declared_deps_are_mapped(self) -> None:
        gi_unmapped, exe_unmapped = deps.unmapped(str(ADDONS_SOURCE))
        self.assertEqual(
            (gi_unmapped, exe_unmapped),
            (set(), set()),
            "Addon(s) declare system deps with no entry in "
            "scripts/lib/addon_system_deps.py. Add a row mapping each to its "
            "per-platform package:\n"
            f"  unmapped requires_gi:  {sorted(gi_unmapped)}\n"
            f"  unmapped requires_exe: {sorted(exe_unmapped)}",
        )


# ------------------------------------------------------------
#
# AddonSystemDepsPresenceTest
#
# ------------------------------------------------------------
@unittest.skipUnless(ADDONS_SOURCE, "addons-source checkout not found")
@unittest.skipUnless(
    IN_TEST_ENV,
    "presence check runs only in the testbed image/CI ($GRAMPS_TESTBED); "
    "skipped on hosts that need not provide the addon GI stack",
)
class AddonSystemDepsPresenceTest(unittest.TestCase):
    """Tested addons must find their declared GI typelibs and executables."""

    def test_tested_addon_gi_typelibs_present(self) -> None:
        try:
            import gi  # noqa: F401
        except ImportError:
            self.skipTest("PyGObject (gi) not importable")
        for addon_dir in _addons_with_tests(ADDONS_SOURCE):
            for ns, ver in deps.scan_addon_gi_specs(str(addon_dir)):
                with self.subTest(addon=addon_dir.name, gi=ns, version=ver):
                    self.assertTrue(
                        _gi_available(ns, ver),
                        f"{addon_dir.name} declares requires_gi {ns} {ver!r}, "
                        f"but no matching typelib is importable. Ensure the "
                        f"package from addon_system_deps.GI_PACKAGES[{ns!r}] is "
                        f"installed in this environment.",
                    )

    def test_tested_addon_executables_present(self) -> None:
        for addon_dir in _addons_with_tests(ADDONS_SOURCE):
            _gi, exes = deps.scan_addon_requirements(str(addon_dir))
            for exe in sorted(exes):
                with self.subTest(addon=addon_dir.name, exe=exe):
                    self.assertTrue(
                        shutil.which(exe),
                        f"{addon_dir.name} declares requires_exe [{exe!r}], but "
                        f"it is not on PATH. Ensure the package from "
                        f"addon_system_deps.EXE_PACKAGES[{exe!r}] is installed.",
                    )


def _gi_available(namespace: str, version: str) -> bool:
    """True if the GI namespace imports at any of its declared versions."""
    import gi

    versions = [v.strip() for v in version.split(",") if v.strip()] or [None]
    for ver in versions:
        try:
            if ver:
                gi.require_version(namespace, ver)
            importlib.import_module(f"gi.repository.{namespace}")
            return True
        except (ValueError, ImportError):
            continue
    return False


if __name__ == "__main__":
    unittest.main()
