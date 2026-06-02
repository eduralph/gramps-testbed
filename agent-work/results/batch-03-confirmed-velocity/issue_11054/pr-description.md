## Root cause
The Form editor has no protection against changes made outside it
while it is open. If a Source / Person / Family the form references is
deleted in another window mid-edit, **OK** writes a citation with a
None-target reference; Check & Repair later flags the dangling handle
as db corruption. nick_h documents this on notes 5/7 of the tracker
issue as a known limitation of the snapshot/write-back design and
calls out an acceptable narrow fix that avoids the wider architectural
change.

## Fix
Implement nick_h's narrow save-time guards verbatim — no behaviour
change when the references are intact:

* `EditForm.save` (source path): if the citation's source handle no
  longer resolves, create a replacement `Source` and repoint the
  citation at it rather than commit a None-target reference.
* `MultiSection.save` (person rows + removed-people loop): skip rows
  whose person handle no longer resolves, both in the row-update loop
  and the detach loop.
* `PersonSection.save`: early-return when the attached person handle
  no longer resolves; skip the detach step when the initial handle is
  gone.
* `FamilySection.save`: same shape as `PersonSection.save`, on family.

Architecture-level fixes (snapshot / per-form locking / JSON-patch
write-back — all discussed on the tracker) are **explicitly out of
scope** per nick_h.

## Verified against
- `Form/editform.py:EditForm.save` — insertion point between
  `add_event` and `commit_citation`; the source handle is read here.
- `Form/editform.py:MultiSection.save` — row-update loop (handle
  comes from `row[0]` in the model) and removed-people detach loop
  (handles come from `set(initial_people) - set(all_people)`).
- `Form/editform.py:PersonSection.save` — `self.handle` is the
  current person, `self.initial_handle` the previously-attached one.
- `Form/editform.py:FamilySection.save` — same shape on family.

## Test
`Form/tests/test_editform_save_guards.py` — eight cases across four
`TestCase` classes:

* `EditFormSourceGuardTest` — drives `EditForm.save` via
  `__new__`-bypass with `DbTxn` patched at the module level;
  asserts `add_source` + `set_reference_handle` fire when the source
  is gone, and don't fire on the happy path.
* `MultiSectionPersonGuardTest` — drives `MultiSection.save` against
  a mock model + a mock db whose `get_person_from_handle` returns
  `None` for dead handles. Asserts the dead row is skipped (commit
  count = live row count) and the dead-removed-person case commits
  nothing.
* `PersonSectionGuardTest` — drives `PersonSection.save`; asserts
  dead `self.handle` short-circuits with no commits, and a live
  attached + dead initial handle commits the attached person and
  skips the detach.
* `FamilySectionGuardTest` — same shape as PersonSection, on family.

Pre-fix: 2 failures + 5 errors among the eight cases (i.e. each guard
is load-bearing). Post-fix: green.

Verified locally via the gramps-testbed addon-unit runner
(`scripts/ubuntu/run-addon-unit.sh Form`): 56 tests OK with the patch
applied.

Fixes #11054
