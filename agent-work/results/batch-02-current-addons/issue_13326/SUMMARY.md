# Issue 13326 — Forms addon → GalleryTab AttributeError ('iconlist')

## Root cause
`GalleryTab.clean_up()` deletes the `iconlist` attribute via
`track_ref_for_deletion("iconlist")` → `super().clean_up()`'s
`delattr(self, "iconlist")`, but it does **not** disconnect the
`'selection-changed'` signal handler that was wired on the
`Gtk.IconView` widget. The widget can outlive the Python attribute
(GTK holds its own refs while the parent dialog is tearing down).
When the parent dialog dispatches the deselection on close, the
still-connected handler calls `self._selection_changed` →
`self.get_selected()` → `self.iconlist.get_selected_items()` and
crashes with `AttributeError: 'GalleryTab' object has no attribute
'iconlist'`.

The original 2012 fix (svn r20849 / `51a53ccebd`) added the
disconnect. Nick Hall's 2023 commit `37395da262` removed it ("the
signal no longer exists to disconnect from at this point") to silence
a GTK warning seen on the normal-close path — but that regressed the
Cancel/teardown-race path the Forms addon happens to exercise.

This is the batch's "core-vs-addon" call: **the entire traceback is
in gramps core (gallerytab.py / buttontab.py); the Forms addon merely
hosts the GalleryTab and calls its `clean_up()` correctly**. The fix
goes in `../gramps`, not addons-source.

## Fix
Capture the `'selection-changed'` handler id when connecting in
`build_interface`, then disconnect it at the head of `clean_up()`
(before `super().clean_up()` removes the attribute). Guard the
disconnect with `GObject.signal_handler_is_connected` so the
already-disposed case Nick was working around stays silent.

## Test
`gramps/gui/editors/displaytabs/test/gallerytab_test.py` (new;
stdlib `unittest`). Two cases, both run under `xvfb-run` since
constructing a real `Gtk.IconView` needs a display:

1. **`test_clean_up_disconnects_selection_changed`** — the bug 13326
   case. Builds a real `GalleryTab` against an in-memory sqlite db,
   captures the `'selection-changed'` signal id on the live iconlist,
   then asserts via `GObject.signal_handler_find` that no handler
   for that signal remains after `clean_up()`. Pre-fix the assertion
   fails (`42 != 0`, handler still connected); post-fix it passes.

2. **`test_clean_up_after_iconlist_destroyed_emits_no_warning`** —
   regression guard for Nick Hall's silenced warning. Calls
   `iconlist.destroy()` before `clean_up()` (simulating the normal
   close path where GTK has already disposed the widget) and asserts
   via `warnings.catch_warnings` that no PyGObject warning of the
   shape `instance '...' has no handler with id '...'` is recorded.
   Mutating the fix to drop the `signal_handler_is_connected` guard
   surfaces exactly that warning, so this test would fail if anyone
   later removes the guard while keeping the disconnect.

```
xvfb-run -a python3 -m unittest \
    gramps.gui.editors.displaytabs.test.gallerytab_test -v
```
→ PASS (2 tests).

Black `--check` clean on the changed files.

## Repo and branch
- Repo: `gramps` (in-tree, gramps core)
- Branch: `fix/bug-13326-gallerytab-iconlist-cleanup` based on
  `upstream/maintenance/gramps61`
- Commit: `f452e7a2d Fix AttributeError on iconlist when GalleryTab
  parent dialog closes.`

## Notes for review
- Sits in the teardown-ordering cluster (13966 in this batch is a
  sibling: `active_page` going `None` mid-teardown).
- The fix doesn't reintroduce Nick Hall's warning because
  `signal_handler_is_connected` short-circuits the disconnect when
  the underlying GObject has been disposed.
- The PR description follows CLAUDE.md format and ends with the
  `Fixes #13326` trailer per [[feedback_mantis_fixes_trailer]].
