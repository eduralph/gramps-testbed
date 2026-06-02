# Sidebar Filter gramplet: how should we refresh the Type selector when custom types change? (bug 13716)

I'd like some guidance on the right design before I write a fix for bug 13716
("Filter gramplets does not update the Type pop-up menu after adding Custom
Types"). prculley sketched the cause in the tracker (note 3) and pointed at the
place-filter refresh he wrote for the enhanced-places PR, but that PR didn't land
and the approach relied on infrastructure we don't have, so I want to agree on a
direction rather than guess.

## What happens

Each sidebar filter (Notes, Events, People, Places, …) builds its **Type**
selector once, in the filter subclass's `__init__`, from a one-time snapshot of
the database's custom types, e.g. in `NoteSidebarFilter`:

```python
if dbstate.is_open():
    self.custom_types = dbstate.db.get_note_types()
else:
    self.custom_types = []
self.event_menu = widgets.MonitoredDataType(
    self.ntype, self.note.set_type, self.note.get_type, False, self.custom_types
)
```

`MonitoredDataType` builds its `StandardCustomSelector` model at construction and
is never rebuilt, so the Type popup is frozen at whatever the custom types were
when the view's filter was first created. Two visible symptoms:

1. **During a session:** import a GEDCOM that creates "GEDCOM import" note types
   (or otherwise add a custom type). `commit_note()` updates the database's
   `note_types` set straight away, so `get_note_types()` is current — but the
   Type combo isn't refreshed, so the new type never appears until you remove
   and re-add the gramplet.
2. **After a restart:** if the Notes view is the active view at startup, its
   filter is constructed before the database has finished loading, so
   `dbstate.is_open()` is False, `custom_types` is empty, and nothing rebuilds it
   later — which is why even restarting doesn't help.

The base `SidebarFilter` already connects `database-changed` and exposes an
`on_db_changed(db)` hook, but the type-bearing subclasses don't override it, so
the selector is never refreshed even on db open/switch.

## Why I can't just reuse the enhanced-places approach

prculley's place-filter refresh (PR 809, "GEPS 045 – enhanced places") wired the
place Type selector to a **`custom-type-changed`** database signal via a new
`PlaceTypeSelector` widget (`fill_models()` / `update_models()`). PR 809 was
closed and neither piece is in the released code — there's no `custom-type-changed`
signal anywhere in `gen`/`gui` today, and `MonitoredDataType` has no public
"rebuild from a new value list" entry point. So the concept is right but it can't
be lifted as-is.

## Options I see

**A. Override `on_db_changed` only.** Each type-bearing filter overrides
`on_db_changed` to re-read `get_<x>_types()` and rebuild its `MonitoredDataType`.
Smallest change; fixes the restart/db-switch case (symptom 2) but **not** the
within-session import (symptom 1), since `database-changed` doesn't fire then.

**B. Add per-namespace object-change refresh.** As in A, plus register the
relevant object signals (`note-add`/`note-update`/`note-rebuild`, and the
event/place/… equivalents) through the existing `callman`/`signal_map`
machinery, keyed off `self.namespace`, to rebuild the selector when objects of
that type change. Covers both symptoms; more signal wiring, and it rebuilds on
every add even when no *new* type appeared.

**C. Introduce a real `custom-type-changed` db signal in core.** Emit it from
the `commit_*` paths in `gen/db/generic.py` when a custom type is first added to
one of the type sets, and have the filters (and potentially other type selectors)
subscribe. This is essentially prculley's original idea, done standalone and
minimally. Cleanest and most reusable, but it touches `gen/db` and needs a small
amount of care to fire only on genuinely new types.

I lean towards **C** as the proper long-term fix (a single, cheap, semantically
correct signal that any type selector can use), with **A** as the obvious interim
if we'd rather keep the change in the GUI layer. But since this reopens a design
prculley already worked through once, I'd rather hear the preference —
particularly whether a `custom-type-changed` signal in core is wanted, and if so
where it should be emitted from.

Targeting `maintenance/gramps61`. Happy to write whichever approach we settle on,
with a regression test.
