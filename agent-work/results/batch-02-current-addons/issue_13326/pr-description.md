## Root cause
`GalleryTab.clean_up()` calls `super().clean_up()`, which removes
`self.iconlist` via `track_ref_for_deletion("iconlist")`, but never
disconnects the `'selection-changed'` signal handler on the iconlist
widget. When the parent dialog tears down on Cancel — the Forms
addon's GalleryTab-in-a-dialog path exercises this reliably — GTK
dispatches a final `selection-changed` to the still-live widget; the
handler calls `self.get_selected()` → `self.iconlist.get_selected_items()`
and raises `AttributeError: 'GalleryTab' object has no attribute
'iconlist'`.

## Fix
Capture the `'selection-changed'` handler id in `build_interface`,
then disconnect it at the head of `clean_up()` — before
`super().clean_up()` removes the attribute. Guard the disconnect
with `GObject.signal_handler_is_connected` so the already-disposed
case (the reason the original disconnect was removed in 37395da262)
stays silent.

## Verified against
- `gramps/gui/editors/displaytabs/gallerytab.py:232,659-660` — the
  unguarded `connect` and the no-op `clean_up` that the reported
  trace fingers.
- `gramps/gui/editors/displaytabs/buttontab.py:319` — the call site
  in the inherited `_selection_changed` callback that reaches into
  `self.get_selected()`.
- The 2012 disconnect (svn r20849 / `51a53ccebd`) — same defect
  class, same fix shape; removed in `37395da262` to silence a GTK
  warning on the normal close path. The new
  `signal_handler_is_connected` guard keeps that path silent while
  restoring teardown-race safety.

## Test
`gramps/gui/editors/displaytabs/test/gallerytab_test.py` covers both
the bug and the warning the original disconnect was removed to
silence:

- `test_clean_up_disconnects_selection_changed` constructs a real
  `GalleryTab`, records the `'selection-changed'` signal id, and
  asserts via `GObject.signal_handler_find` that no handler remains
  after `clean_up()`. Pre-fix `42 != 0`; post-fix passes.
- `test_clean_up_after_iconlist_destroyed_emits_no_warning` destroys
  the iconlist widget before `clean_up()` — the normal close path
  where commit 37395da262 was seeing the GTK critical — and asserts
  via `warnings.catch_warnings` that no `instance '...' has no
  handler with id '...'` warning is recorded. Mutating the fix to
  drop the `signal_handler_is_connected` guard surfaces exactly that
  warning, so future removals of the guard regress here.

Both need a display (`Gtk.IconView`), so run under `xvfb-run`:

```
xvfb-run -a python3 -m unittest \
    gramps.gui.editors.displaytabs.test.gallerytab_test -v
```

Fixes #13326
