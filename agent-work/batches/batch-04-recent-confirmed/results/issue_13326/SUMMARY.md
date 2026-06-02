# Issue 13326 — GalleryTab AttributeError 'iconlist' on parent-dialog close (Forms)

**Outcome: review-and-note. Fix already exists as OPEN PR
gramps-project/gramps#2330 (correct branch, CI green, tests included).**
No competing PR written. Defer to Eduard on pushing 2330 forward.

## Verification done
- **PR 2330 state:** OPEN, base `maintenance/gramps61`, not a draft, CI **green**
  (build pass, lint pass). Title: "Fix AttributeError on iconlist when GalleryTab
  parent dialog closes (bug 13326)".
- **Bug still live on gramps61:** `gallerytab.py` `clean_up()` on
  `maintenance/gramps61` is just `super(ButtonTab, self).clean_up()` — no
  `selection-changed` disconnect. `build_interface()` connects the handler
  (`gallerytab.py:232`) but never captures its id, so the teardown race is
  present. Confirms a fix is warranted; PR 2330 supplies it.
- **Repo question resolved:** core, not Forms. The whole traceback
  (`buttontab.py:320 _selection_changed → gallerytab.py:292 get_selected →
  self.iconlist`) is core display-tab code; Forms only hosts a GalleryTab and
  calls `clean_up()` correctly (note 5).

## Review of PR 2330 (looks complete and correct)
Fix matches the note-5 diagnosis precisely:
- `build_interface()` now captures the handler id:
  `self._sel_changed_handler = self.iconlist.connect("selection-changed", …)`.
- `clean_up()` disconnects it **before** `super().clean_up()` deletes
  `self.iconlist` via `track_ref_for_deletion`, guarded by
  `getattr(self, "_sel_changed_handler", None)`, `hasattr(self, "iconlist")`
  and `GObject.signal_handler_is_connected(...)`. The triple guard correctly
  covers (a) handler never set, (b) iconlist already deleted, (c) widget
  GObject already disposed — the last being exactly the case commit
  `37395da262` (2023) removed the original disconnect to avoid.
- Tests: `gramps/gui/editors/displaytabs/test/gallerytab_test.py` (+ empty
  `test/__init__.py`).
  - `test_clean_up_disconnects_selection_changed` — captures the signal id on a
    live iconlist, runs `clean_up()`, asserts `signal_handler_find` returns 0.
    Fails pre-fix (handler still wired), passes post-fix.
  - `test_clean_up_after_iconlist_destroyed_emits_no_warning` — destroys the
    iconlist first, asserts no `"has no handler with id"` warning under
    `warnings.catch_warnings`. Guards against re-introducing the `37395da262`
    warning if the `signal_handler_is_connected` guard is ever dropped.
  - Both gated by `@unittest.skipUnless(_HAS_GTK_DISPLAY, …)` — gramps CI sets
    `GDK_BACKEND=-` and a NULL-screen `Gtk.IconView` segfaults at cleanup, so the
    suite skips cleanly there and runs under `xvfb-run`/a real desktop. Sensible.

No correctness or branch issues found. The PR is the right fix on the right
branch with adequate regression coverage. Recommendation: this is the fix —
do **not** open a competing PR; Eduard decides whether to push 2330 forward
(it is his own PR per the file copyright + note 5).

## Related (not part of this fix)
- svn r20849 / `51a53ccebd` (2012) — original disconnect for this defect class.
- `37395da262` (2023) — removed it to silence a GTK warning → reintroduced the
  race. PR 2330's guard reconciles both.
- Bug 13059 (selectionwidget) — same teardown-race family.

## Files
- `SUMMARY.md` (this file)
- `mantis-comment.md` — tracker comment, Eduard's voice
- no `patch.diff` / `pr-description.md` — fix is the existing PR 2330; not duplicated.
