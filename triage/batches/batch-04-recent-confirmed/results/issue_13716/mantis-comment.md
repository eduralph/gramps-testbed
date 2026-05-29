Confirmed, and it is in core, as note 3 describes. The sidebar Filter gramplet
builds its Type selector once, when the view's filter is first created, from a
snapshot of the database's custom types, and never rebuilds it. Importing a
GEDCOM (or otherwise adding a custom type) updates the database immediately, but
the already-built Type combo is not refreshed, so the new type does not appear.
The combo can also start empty after a restart when the view is the active one
at startup, because its filter is built before the database finishes loading.

The place sidebar filter refresh referenced in note 3 was part of the enhanced
places work (PR 809), which was not merged and relied on a new
"custom-type-changed" database signal that does not exist in the released code,
so it cannot simply be reused. A general fix is being developed that rebuilds the
Type selector when the database changes and when objects of the relevant type are
added or updated, so the popup tracks custom types added during a session without
needing to reopen the gramplet or restart.

This is core, targeting the maintenance/gramps61 branch.
