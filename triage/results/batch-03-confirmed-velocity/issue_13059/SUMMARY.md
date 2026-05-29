# Issue 13059 — Photo Tagging click-after-resize TypeError (gramps CORE)

## Status
**Real fix shipped** — draft PR [gramps#2334](https://github.com/gramps-project/gramps/pull/2334) on `maintenance/gramps61`. Linux verification done (the headless unit test in `gramps/gui/widgets/test/selectionwidget_test.py` passes; pre-fix it raises `TypeError`).

**Post-merge manual work — see `MANUAL-VERIFICATION.md` in this folder.**
After gramps#2334 merges and a GrampsAIO build picks it up, run mihle's
GUI reproducer on Windows to confirm the fix lands correctly through
the bundled GTK. Outcome gates the Mantis close: success → paste
`mantis-comment.md` and set Fixed in version; failure → reopen with
the new traceback. The same close handles 0012659 (the 2022 duplicate).

## Root cause
`SelectionWidget._button_release_event` in
[`gramps/gui/widgets/selectionwidget.py:779`](../../../../../../gramps/gramps/gui/widgets/selectionwidget.py#L779)
(upstream/maintenance/gramps61) unconditionally calls
`self.current.set_coords(*self.selection)` from its
`else: # update current selection` branch. That branch fires on a left-button
release when `self.current is not None` and `self.grabber == INSIDE`. Under
mihle's exact repro for Mantis 13059 (drag a box edge to resize → release →
single CLICK inside the same box, no drag) that path lands with
`self.selection is None`. `*None` is not iterable → `TypeError`. Duplicate
of 0012659 (2022).

The verdict in `issue_13059.md` correctly identified this as a **gramps CORE
defect**, not a Photo Tagging addon bug — the Photo Tagging addon hosts the
SelectionWidget but every frame in the traceback is in `gramps/gui/widgets/`.
PR targets `../gramps`, branch `maintenance/gramps61`, not addons-source.

## Fix
Guard both `set_coords(*self.selection)` call sites in `_button_release_event`
with `if self.selection is not None:`. The conservative no-op when selection
is None on this branch is to leave the region's stored coords as-is — the
click was a no-motion event, the region didn't move. Mirrors the
defensive-guard pattern from the 13966 / 13326 teardown-family fixes
(per the verdict: "Conservative guard ... do not restructure the widget").

Both call sites guarded for defense in depth:
- Line 770 (grabber-edge branch): `_modify_selection(dx, dy)` is supposed
  to populate `self.selection` before the call, but a future regression
  there shouldn't crash gramps. Guard.
- Line 779 (INSIDE-click branch): the actual 13059 path.

## Verified against
- `gramps/gui/widgets/selectionwidget.py:760-789` (`maintenance/gramps61`) —
  the branch structure the fix targets; the `else:` arm is where 13059 lands.
- `gramps/gui/widgets/selectionwidget.py:878-890` — `_modify_selection`
  always writes `self.selection = order_coordinates(...)`, never None, so
  guarding line 770 is defense-in-depth rather than a known bug path.
- `gramps/gui/widgets/grabbers.py:43` — `INSIDE = 0`, the constant
  the branch selector compares against.
- Git history check (`git log upstream/maintenance/gramps61 -- gramps/gui/widgets/selectionwidget.py`):
  the relevant branching was introduced by commit
  [`f17892c4`](../../../../../../gramps/gramps/gui/widgets/selectionwidget.py)
  ("Fix click/drag in media reference editor", 2017) — the fix that
  added the `else: # update current selection` branch but didn't guard
  it. No later commit on `maintenance/gramps61` addresses this path;
  the upstream is not ahead of us.

## Test
`gramps/gui/widgets/test/selectionwidget_test.py` (new; stdlib `unittest`,
with `gramps/gui/widgets/test/__init__.py` so the package is loadable).
Three cases:

1. **`test_click_after_resize_with_none_selection_does_not_raise`** — the
   bug-13059 path. Sets `current = Region(0, 0, 10, 10)`, `selection = None`,
   `grabber = INSIDE`, then calls `_button_release_event` with a synthesized
   left-button event. Pre-fix: `TypeError`. Post-fix: no raise; the
   region's stored coords are unchanged.
2. **`test_grabber_edge_release_with_none_selection_does_not_raise`** —
   defense-in-depth on line 770. Same shape with a non-INSIDE, non-None
   grabber.
3. **`test_click_with_valid_selection_still_updates_region`** — sanity
   check that the guard is conservative. With a valid selection, the
   normal update path still runs and the region's coords move to the
   selection's coords.

Headless — constructs `SelectionWidget` via `__new__` (bypassing
`__init__` which needs a live GTK display), pins
`gi.require_version("Gtk", "3.0")` before the gramps.gui import so the
chain loads against the right ABI, mocks `emit` / `image.queue_draw`.

Verified via the testbed's Docker harness
(`./scripts/ubuntu/run-unit.sh` after temporarily moving
`po/mn.po` aside — that file has 7 unrelated msgfmt errors blocking
translation compile, NOT introduced by this PR):

```
test_click_after_resize_with_none_selection_does_not_raise ... ok (0.000s)
test_click_with_valid_selection_still_updates_region ... ok (0.000s)
test_grabber_edge_release_with_none_selection_does_not_raise ... ok (0.000s)
```

## Repo and branch
- Repo: `gramps` (upstream `gramps-project/gramps`)
- Branch: `maintenance/gramps61` (per CLAUDE.md: gramps core bug fixes go to
  the maintenance branch, not master)
- Local branch in `../gramps`: `fix/bug-13059-selectionwidget-guard` (off
  `upstream/maintenance/gramps61`; uncommitted working-tree diff per the
  testbed convention — patch.diff captures the change for review)

## Mantis link
- Tracker: https://gramps-project.org/bugs/view.php?id=13059
- Duplicate to close together: https://gramps-project.org/bugs/view.php?id=12659 (2022, "could not reproduce" at the time)
- Status to set on close: resolved / fixed
- Fixed in version: next 6.1.x release on maintenance/gramps61
- Comment: see `mantis-comment.md`

## Notes for next reviewer
- The headless test deliberately uses `__new__`-bypass + attribute injection
  to avoid needing a real Gtk display. Same pattern that exists elsewhere
  in gramps' GUI tests (`gramps/gui/editors/test/editreference_test.py`
  uses `Mock` for the same reason).
- I did NOT attempt a dogtail / `tests/interface/` regression test for
  this bug, because the headless unit test exercises exactly the buggy
  path (`set_coords(*None)`) without any GTK display or AT-SPI rig —
  cheaper, faster, upstreamable as-is. The verdict's "Try the headless
  unit path first (cheaper, upstreamable); fall back to interface test"
  guidance favours this choice.
