## Root cause
`PrerequisitesCheckerGramplet.main()` is a generator the framework
steps via `_updater` → `next(self._generator)`. It reads
`self.uistate.viewmanager.active_page.bottombar` unguarded; when the
family tree is closed while the generator is still mid-flight,
`active_page` is `None` and the read raises
`AttributeError: 'NoneType' object has no attribute 'bottombar'`.

## Fix
Pull `active_page` into a local, return early if it's `None`, then
fall through to the existing bottombar / db-open / count<3 short-
circuit chain. No behaviour change while a tree is open.

## Verified against
- `PrerequisitesCheckerGramplet/PrerequisitesCheckerGramplet.py:170-177`
  — the unguarded read at the head of `main()`. The traceback line
  numbers in the report match this site.
- The reporter notes the trace also reproduces on Gramps 5.2.4, so
  this is long-standing rather than a 6.0 regression; the same
  guard is appropriate on `maintenance/gramps61`.

## Test
`PrerequisitesCheckerGramplet/tests/test_main_active_page_none.py`
drives `main()` once with a stub `uistate` whose `active_page` is
`None` and asserts the generator exits cleanly. Two regression-guard
cases lock the existing dashboard / non-dashboard short-circuit
behaviour. Pre-fix the first case fails with the exact bug 13966
traceback; all three pass post-fix.

Fixes #13966
