# Issue 13966 — PrerequisitesCheckerGramplet: AttributeError on tree close

## Root cause
`PrerequisitesCheckerGramplet.main()` (a generator stepped by the
framework's `_updater` → `next(self._generator)`) reads
`self.uistate.viewmanager.active_page.bottombar` unguarded. When the
family tree is closed while the gramplet's generator is still in
flight, `viewmanager.active_page` is `None`, so the read raises
`AttributeError: 'NoneType' object has no attribute 'bottombar'`. The
gramplet assumed an active page always exists while it's running; on
tree close that no longer holds.

Per the reporter, the trace also reproduces on Gramps 5.2.4 — long-
standing, NOT a 6.0 regression.

## Fix
Pull `active_page` into a local, return early if it's `None`, then
proceed with the existing `bottombar / db-open / count<3` short-
circuit chain. No behaviour change while a tree is open. On tree
close the gramplet simply yields nothing further until the framework
stops the generator.

## Test
`PrerequisitesCheckerGramplet/tests/test_main_active_page_none.py`
(new; stdlib `unittest`). Three cases:

1. `active_page = None` (the bug 13966 trace) → must not raise; the
   generator returns cleanly (asserted via `StopIteration` on first
   `next()`). Pre-fix this fails with the exact bug 13966 traceback.
2. Non-dashboard view + closed DB → existing short-circuit holds
   (returns on first `next()` — same `StopIteration` as before).
3. Dashboard + pending upstream-version fetch → `main()` enters the
   `while … is False: yield True` loop and yields `True` on first
   `next()`.

The module file shares its name with the package directory, so the
test loads it directly via `importlib.util.spec_from_file_location`
to sidestep the bug 0012691 namespace-package trap referenced in
gramps-testbed/CLAUDE.md.

`./scripts/ubuntu/run-addon-unit.sh PrerequisitesCheckerGramplet` →
PASS (3 tests).

## Repo and branch
- Repo: `addons-source` (in-tree addon
  `PrerequisitesCheckerGramplet/`)
- Branch: `fix/bug-13966-prerequisites-active-page-none` based on
  `upstream/maintenance/gramps61`
- Commit: `3d91c9f1b PrerequisitesCheckerGramplet: guard active_page
  on tree close`

## Notes for review
- Addon version not bumped per
  [[feedback_addons_source_no_version_bump]].
- This sits in the teardown-ordering cluster called out by the
  verdict (also issues 13326 / others) — the guard pattern is
  minimal and per-call-site rather than a general framework change.
