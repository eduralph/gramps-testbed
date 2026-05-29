Confirmed and fixed.

Mihle's reproducer (resize a box edge → release → single click inside the
same box) lands in `SelectionWidget._button_release_event`'s
`else: # update current selection` branch (the path that fires when
`self.grabber == INSIDE`). That branch called
`self.current.set_coords(*self.selection)` unconditionally, but after the
resize-release the click that follows never rebuilds `self.selection` — so
the unpack hits `*None` and raises `TypeError`. The defect is in gramps
core (`gramps/gui/widgets/selectionwidget.py`), not in the Photo Tagging
addon — the addon just hosts the SelectionWidget.

Fixed by guarding both `set_coords(*self.selection)` call sites in the
release handler with `if self.selection is not None:`. The safe no-op for
a no-motion click is to leave the region's stored coordinates alone.

A regression test ships with the fix at
`gramps/gui/widgets/test/selectionwidget_test.py` (headless `unittest`
exercising the buggy path with `selection=None`).

Pull request:

p:gramps:2334:

This also closes 0012659 (the 2022 "could not reproduce" duplicate of
this issue) — the reproducer on 13059 fires through 12659's path too.

Fixes #13059. Fixes #12659.
