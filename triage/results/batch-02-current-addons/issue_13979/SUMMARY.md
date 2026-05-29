# Issue 13979 — PluginManager Enhanced: IndexError on PostgreSQL Enhanced row

## Root cause
`PluginStatus.__info` in the PluginManager Enhanced addon iterates
`Requirements().info(addon)` output as `[label, table]` pairs and
joins the first row with `txt = " ".join(req_lst[0])`. Gramps core's
`Requirements.info` (`gramps/gen/utils/requirements.py:146-172`)
emits a label + empty table whenever the addon listing carries a
present-but-empty requires key — e.g. `"re": []`. Indexing
`req_lst[0]` on an empty table raises `IndexError: list index out of
range`.

PostgreSQL Enhanced declares `requires_exe=[]` in its `.gpr.py`,
which lands in `addons-en.json` as `"re": []`. A scan of the live
`addons/gramps61/listings/addons-en.json` confirms it is the **only**
addon currently carrying a present-but-empty requires key — matching
the user's "only the PostgreSQL Enhanced row crashes" symptom.

## Repo settled
- "Plugin Manager Enhanced" addon lives in `addons-source/PluginManager/`
  (not an external repo). PR targets addons-source `maintenance/gramps61`.
- The traceback's call site `PluginManager/PluginManager.py:655` is in
  the addon, not gramps core. (The core `Requirements.info` shape is
  a contributing factor — see "Follow-up notes" below.)

## Fix
Skip the iteration when `req_lst` is empty: indexing it fails, and
there is nothing meaningful to render anyway. Three-line guard at the
top of the iteration body in `PluginManager.py`.

## Test
`PluginManager/tests/test_info_empty_requires.py` (new, with
`tests/__init__.py`). Uses the `__new__`-bypass pattern to build a
`PluginStatus` without running its Gtk-heavy `__init__`, stubs
`_preg`/`_pmgr`/`_bufin`, then calls the name-mangled
`_PluginStatus__info("postgresqlenhanced")` against an addon dict
shaped exactly like the live listing entry (`"rm": ["psycopg"]`,
`"re": []`).

Two assertions:
1. No `IndexError` raised.
2. The non-empty `"Python modules"` entry is still rendered while the
   empty `"Executables"` entry is **not** rendered (verifies the
   `continue` only skips the empty case, not all requirements).

Pre-fix mutation test produces exactly the reported traceback:
`File ".../PluginManager.py", line 655, in __info / txt = " ".join(req_lst[0]) / IndexError: list index out of range`.

The test class is gated on `_has_gtk_display()` (mirrors the bug
13326 test), so it skips cleanly in CI environments without a
display — `PluginManager.py` imports Gtk at module load. Under
`xvfb-run` (testbed / a real desktop) both assertions run.

`xvfb-run -a python3 -m unittest PluginManager.tests.test_info_empty_requires -v` → PASS (1 test).

## Repo and branch
- Repo: `addons-source` (in-tree `PluginManager/`)
- Branch: `fix/bug-13979-pluginmanager-empty-requires-exe` based on
  `upstream/maintenance/gramps61`
- Commit: `39a4dfdde Fix IndexError when an addon declares an empty
  requires_exe.`

## Follow-up notes (not in scope of this PR)
- gramps core's `Requirements.info` (`gramps/gen/utils/requirements.py:146`)
  emits a label + empty table when the addon dict has `"rm"`/`"rg"`/`"re"`
  as keys with empty-list values. Cleaner API contract would be "only
  emit pairs that have at least one entry". A separate gramps-core PR
  could harden that — but the user-visible crash is in the addon, so
  the addon fix is the one-PR-per-bug answer per CLAUDE.md.
- lordemannd's note 2 mentions a SECOND symptom: the core Addon
  Manager reports "install succeeded" but doesn't actually install.
  Per CLAUDE.md "one issue per ticket", that is a separate defect and
  is not addressed here. Worth filing as its own Mantis if it still
  reproduces.

## Notes for review
- Addon version not bumped per [[feedback_addons_source_no_version_bump]].
- The fix is one-line-of-logic + an explanatory comment; the
  surrounding 4 lines of context are unchanged.
- The test uses `__new__`-bypass like the
  `PrerequisitesCheckerGramplet` / `LinesOfDescendency` regression
  tests on the fork — established pattern in this batch's cluster.
