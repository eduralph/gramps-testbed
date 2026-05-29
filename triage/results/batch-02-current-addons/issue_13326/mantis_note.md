# Mantis 13326 — draft note (Eduard to paste once the PR is opened)

(Bare bug numbers per the no-`#`-prefix convention; PR linked with
`p:gramps:` for gramps core.)

---

Triage finding: this is in gramps core, not in the Forms addon. The
entire traceback (`gallerytab.py:292`, `buttontab.py:319`) terminates
inside core display-tab code; Forms only hosts a `GalleryTab` in its
form-editor dialog and calls its `clean_up()` correctly.

Root cause is a teardown race. `GalleryTab.clean_up()` calls
`super().clean_up()`, which removes `self.iconlist` via
`track_ref_for_deletion("iconlist")`, but it does not disconnect the
`'selection-changed'` signal handler on the still-live `Gtk.IconView`
widget. When the parent dialog tears down on Cancel the widget
receives a final `selection-changed`; the connected handler reaches
`self.get_selected()` → `self.iconlist.get_selected_items()`, which
raises `AttributeError: 'GalleryTab' object has no attribute
'iconlist'`. The Forms editor exposes this reliably because its
Cancel/close path tears the dialog down right after `clean_up()`
runs.

This is a regression that was already fixed once. The original
disconnect was added in svn r20849 (commit 51a53ccebd, 2012) for the
same defect class. Commit 37395da262 (2023, "Avoid signal warning
during editor clean up") removed it to silence a GTK warning on the
normal close path — which reintroduced the teardown-race window.

Fix in PR p:gramps:2330: restore the disconnect by capturing the
handler id when connecting, then disconnecting at the head of
`clean_up()`, guarded by `GObject.signal_handler_is_connected` so the
already-disposed case (the reason the original disconnect was
removed) stays silent. Targets `maintenance/gramps61`.

Regression tests ship in the same PR
(`gramps/gui/editors/displaytabs/test/gallerytab_test.py`). One
case captures the `'selection-changed'` signal id on a live
iconlist, runs `clean_up()`, and asserts via
`GObject.signal_handler_find` that no handler remains — fails
pre-fix (handler still connected), passes post-fix. A second case
guards against the warning commit 37395da262 was avoiding: destroy
the iconlist widget before `clean_up()` and assert via
`warnings.catch_warnings` that no `instance '...' has no handler
with id '...'` warning is recorded. Mutating the fix to drop the
`signal_handler_is_connected` guard surfaces exactly that warning,
so future removals of the guard regress here.

Reproducer mirrors steveyoungs' note 4: install Forms, configure a
Source as a form, new form, switch to the gallery tab, add an image,
select it, click Cancel.

Suggested tracker action: leave as confirmed until the PR merges;
set Fixed in version 6.1.x once shipped.
