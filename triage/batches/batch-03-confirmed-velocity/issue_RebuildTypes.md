# RebuildTypes — ModuleNotFoundError: No module named 'gui' (bare import should be gramps.gui)

| field | value |
|---|---|
| Source | detector (c)-bucket, NOT a Mantis confirmed scrape |
| Addon | RebuildTypes — verify in-tree addons-source |
| Failure | `ModuleNotFoundError: No module named 'gui'` |

## What the detector found
RebuildTypes fails isolated load with `ModuleNotFoundError: No module named 'gui'`.
A bare `import gui` (or `from gui import ...`) resolves only if `gui` is top-level on
sys.path — which it was under old Gramps packaging but is not now; the correct path is
`gramps.gui`. This is a stale import that breaks under current packaging / in isolation.

## ===== TRIAGE VERDICT =====
- **Actionable?** yes — near-certain one-line fix.
- **Where:** addons-source (in-tree). Confirm dir, branch maintenance/gramps61.
- **Root cause:** a bare `gui` import that should be `gramps.gui`. Find it
  (`grep -n 'import gui' RebuildTypes/`) and qualify it to `gramps.gui`.
- **Fix sketch:** change `import gui` → `from gramps import gui` (or
  `from gramps.gui... import ...` matching the actual usage). Check for sibling bare
  imports in the same file (`gen`, `gui`, `cli` without the `gramps.` prefix) — same class.
  Fix the import path(s) only.
- **Repro:** import the module — fails pre-fix, succeeds post-fix. NOTE: the module imports
  Gtk via gramps.gui, so the import test may need a display — gate on display like the
  batch-02 PluginManager test, or test under xvfb.
- **Test:** detector is the regression guard. Optional gated import test in
  `RebuildTypes/tests/`.
- **Check upstream isn't ahead:** grep history/open PRs; overlaps PR #820 lint/compile
  spin-offs — check that series before committing.
