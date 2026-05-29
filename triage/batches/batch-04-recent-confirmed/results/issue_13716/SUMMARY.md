# Issue 13716 — Filter gramplet Type popup not updated after custom types added

**Outcome: ANALYSIS + designed fix → taking the design to Discourse first.**
No patch shipped yet: the verdict's reference plan ("generalize PR #809") rests
on infrastructure that never landed, the real fix is a multi-file GUI
generalization, and it is GUI-only (test must be a testbed interface test).
Because this reopens a design prculley already worked through once, the agreed
next step is a maintainer discussion — see `discourse-post.md` (ready to post on
gramps.discourse.group). Implementation waits on that outcome. STOPPED for review.

## Root cause (confirmed — matches maintainer note 3)
The sidebar Filter gramplet builds its **Type** selector once, in each filter
subclass's `__init__`, from a snapshot of the db's custom types, and never
rebuilds it:

- `NoteSidebarFilter.__init__` (and the event/family/person/place/repo filters)
  reads `self.custom_types = dbstate.db.get_note_types()` (etc.) **once**, then
  hands it to `widgets.MonitoredDataType(self.ntype, …, self.custom_types)`,
  which builds the combo's `StandardCustomSelector` model at construction time.
- The base `SidebarFilter` (`gramps/gui/filters/sidebar/_sidebarfilter.py`)
  already wires `dbstate.connect("database-changed", self._db_changed)`, which
  calls the overridable hook `on_db_changed(db)` — but every type-bearing
  subclass leaves `on_db_changed` as the base no-op, so the Type combo is never
  refreshed, even on db open/switch.

Two distinct failure windows follow:
1. **Within-session** (the reporter's headline repro): importing a GEDCOM adds
   note records with the "GEDCOM import" custom type. `commit_note`
   (`gramps/gen/db/generic.py:2230`) updates the db's `note_types` set live, so
   `get_note_types()` is fresh — but no widget refresh happens, so the combo
   never shows it.
2. **After restart** (reporter: "STILL no GEDCOM import type"): when the Notes
   view is the active view at startup, its filter is constructed before the db
   finishes loading, so `dbstate.is_open()` is False and `custom_types = []`;
   the later `database-changed` does not rebuild it.

The data layer is fine; this is purely the GUI selector not refreshing.

## Why the verdict's "generalize PR #809" plan does NOT apply
Note 3 points at PR #809's place-sidebar-filter refresh. I fetched
`_placesidebarfilter.py` from prculley's `places1` branch (PR #809 head
`cbfe9d7`). Its refresh depends on **two pieces of new infrastructure that were
never merged** (PR #809 is CLOSED — the GEPS-045 enhanced-places effort):
- a new db signal **`custom-type-changed`** (`grep` confirms it does not exist
  anywhere in current `gramps/gen` or `gramps/gui`), and
- a new **`PlaceTypeSelector`** widget with `fill_models()` / `update_models()`.

So #809 cannot be copied; current core has neither. `MonitoredDataType` also has
no public "rebuild from new custom_values" method — refreshing means
re-instantiating it on the existing combo.

## Designed fix (achievable with current infrastructure)
Generalise via the hooks that DO exist:

1. **Base `SidebarFilter`**: add a no-op hook `rebuild_type_filters(self)` and
   call it (a) from `_db_changed` (covers restart / db-switch — failure window
   2), and (b) from a per-namespace set of object-change db signals registered
   through the existing `callman`/`signal_map` mechanism (e.g. `note-add`,
   `note-update`, `note-rebuild` for the Note namespace; the matching
   `event-*`, `place-*`, … for the others) so an import refreshes the combo
   (failure window 1). The namespace→signal mapping keys off `self.namespace`.
2. **Each type-bearing subclass** (note, event, family ×2, person, place, repo)
   overrides `rebuild_type_filters()` to re-read `get_<x>_types()` and rebuild
   its `MonitoredDataType` on the same combo widget, preserving the current
   text selection.

This is ~7 files. It is the "generalisation the maintainer never did" (note 3),
implemented against today's signals rather than #809's unmerged signal.

## Test approach
GUI-only. A core unittest is impractical (the filters are Gtk-coupled and
`MonitoredDataType` builds a `StandardCustomSelector`). The right vehicle is a
**testbed interface test**
(`tests/interface/test_bug_13716_filter_type_refresh.py`, subclassing
`GrampsInterfaceTestCase`): open a tree, note the Notes filter Type options, add
a Note with a custom type (or import a small fixture creating one), assert the
Type popup now lists it without a restart.

## DECISION NEEDED (why this is flagged, not shipped)
- The fix is materially larger and different from the verdict's framing (a
  one-spot "copy #809", which is impossible).
- It touches 7 core GUI files and adds per-namespace db-signal wiring — higher
  blast radius than the other increment-1 items.
- It is GUI-only; verification requires an interface test in the Docker harness,
  not a quick headless unit test.

Shipping a sprawling, only-interface-testable GUI refactor unreviewed would
violate the "one well-scoped, verifiable change" discipline. Recommend Eduard
decide: (a) proceed with the full generalisation + interface test now, or
(b) ship a contained first step (override `on_db_changed` to rebuild — fixes the
restart window only) and track the within-session refresh separately, or
(c) defer. Confirmed core, `maintenance/gramps61`, not the Forms-style addon.

## Check-upstream result
No merged or open/closed PR generalises the sidebar-filter type refresh
(`13716` not in gramps61/master log except an unrelated typo commit; PR #809
closed). The bug is live.

## Files
- `SUMMARY.md` (this file)
- `mantis-comment.md` — tracker comment, Eduard's voice (confirmed + in design)
- no `patch.diff` yet — pending the scope decision above.
