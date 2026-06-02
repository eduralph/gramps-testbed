## Root cause
`SelectionWidget._button_release_event` (`gramps/gui/widgets/selectionwidget.py:779`)
called `self.current.set_coords(*self.selection)` unconditionally from its
`else: # update current selection` branch. Under the Mantis 13059 / 12659
sequence — drag a box edge to resize, release, then single CLICK (no drag)
inside the same box — that branch fires with `self.selection is None`,
because the prior resize-release left `self.grabber == INSIDE` and the
no-motion click never rebuilt `selection`. `*None` is not iterable, so the
release raises `TypeError`. Duplicate 12659 (2022) closed as
"cannot reproduce" at the time; mihle's note on 13059 gives the exact
reproducer.

## Fix
Guard both `set_coords(*self.selection)` call sites in the release handler
with `if self.selection is not None:`. The safe no-op for the no-selection
case is to leave the region's stored coordinates alone — the user clicked
without moving, the region shouldn't move. Conservative guard, no
restructuring of the widget (matches the defensive-guard pattern from the
13966 / 13326 teardown-family fixes).

Both call sites guarded for defense in depth:
- line 770, grabber-edge branch — `_modify_selection` always populates
  `self.selection` today, so this is a future-regression guard, not a
  known bug path.
- line 779, INSIDE-click branch — the actual 13059 path.

## Verified against
- `gramps/gui/widgets/selectionwidget.py:760-789` — the branch structure
  the fix targets; the `else:` arm is where 13059 lands.
- `gramps/gui/widgets/selectionwidget.py:878-890` — `_modify_selection`
  always writes `self.selection = order_coordinates(...)`, confirming
  the line-770 guard is defense-in-depth.
- `gramps/gui/widgets/grabbers.py:43` — `INSIDE = 0`, the constant
  the branch selector compares against.

## Test
`gramps/gui/widgets/test/selectionwidget_test.py` (new; stdlib
`unittest`, plus an empty `gramps/gui/widgets/test/__init__.py` —
`gramps/gui/widgets/` had no `test/` package yet). Three cases built
via `__new__`-bypass with `self.current` / `self.selection` / `self.grabber`
injected and `emit` mocked, exercising the release-event handler without
any live GTK display:

  1. `test_click_after_resize_with_none_selection_does_not_raise` — the
     13059 path (`grabber == INSIDE`, `selection == None`). Asserts no
     `TypeError` and that the region's coords don't move.
  2. `test_grabber_edge_release_with_none_selection_does_not_raise` —
     same shape on the grabber-edge branch.
  3. `test_click_with_valid_selection_still_updates_region` — sanity
     check that a valid selection still updates the region's coords
     and emits `region-modified`.

  Before fix: `test_click_after_resize_with_none_selection_does_not_raise`
              fails with
              `TypeError: set_coords() argument after * must be an
              iterable, not NoneType`
  After fix:  3 tests, OK

Fixes #13059. Fixes #12659.
