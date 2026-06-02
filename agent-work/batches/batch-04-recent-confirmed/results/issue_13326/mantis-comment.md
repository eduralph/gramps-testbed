This is a core bug, not a Forms problem. The whole traceback runs in core
display-tab code (buttontab.py _selection_changed -> gallerytab.py get_selected
-> self.iconlist); Forms only hosts a GalleryTab in its form editor and tears it
down correctly. The Forms editor just exposes it reliably because its Cancel
path destroys the dialog right after clean_up() runs.

Root cause is a teardown race. GalleryTab.clean_up() lets super().clean_up()
delete self.iconlist (via track_ref_for_deletion) without first disconnecting the
'selection-changed' handler on the still-live Gtk.IconView. When the dialog tears
down on Cancel the widget emits one last selection-changed, which re-enters
_selection_changed -> get_selected() -> self.iconlist and raises the
AttributeError. The original disconnect existed (svn r20849, 2012) but was
removed in 2023 (commit 37395da262) to silence a GTK warning, which reopened the
window.

A fix is up for review that captures the handler id at connect time and
disconnects it at the head of clean_up(), guarded by
GObject.signal_handler_is_connected so the already-disposed case (the reason the
2023 commit removed it) stays warning-free. It targets the maintenance/gramps61
branch and ships regression tests for both the missing-disconnect crash and the
no-warning case:

https://github.com/gramps-project/gramps/pull/2330
