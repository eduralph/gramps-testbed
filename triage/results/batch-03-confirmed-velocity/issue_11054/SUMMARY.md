# Mantis 11054 — Forms gramplet: db corruption from editing referenced objects mid-form

## Verdict
**FIX SHIPPED** — implement nick_h's narrow save-time guards
(triage brief verbatim scope): on save, verify each referenced
Source / Person / Family handle still resolves; on miss, either
create a replacement (source) or drop the row (person, family).
Architectural fixes (snapshot/locking/JSON-patch) discussed on the
ticket are **explicitly out of scope** per nick_h's notes 5/7.

## Branch + PR
- **fork branch:** `eduralph/addons-source:fix/bug-11054-forms-save-guards`
- **target:** `gramps-project/addons-source:maintenance/gramps60`
- **status:** PR **addons-source#926** opened, marked ready, and **verified** (2026-05-29). Awaiting upstream merge.

## Files
- `Form/editform.py` — four guards added:
  * `EditForm.save` (Source): replacement-source path when the
    citation's source handle no longer resolves.
  * `MultiSection.save` (Person, rows + removed-people loop): skip
    rows / detach entries where `get_person_from_handle` returns
    `None`.
  * `PersonSection.save` (Person, attached + initial): early-return
    when current handle dead; skip detach when initial dead.
  * `FamilySection.save` (Family, attached + initial): same shape on
    family.
- `Form/tests/test_editform_save_guards.py` — eight test cases across
  four `TestCase` classes, all driving the section save methods via
  `__new__`-bypass with a mocked db.

## Test
Run via testbed `scripts/ubuntu/run-addon-unit.sh Form`. With the fix:
PASS (56 tests). Without the fix (`git checkout -- Form/editform.py`
then re-run): FAIL (2 failures, 5 errors among the eight new cases —
proving the guards are load-bearing and not just exercising mocks).

## Manual work
None for the unit-test layer — guards have direct regression coverage.
A future end-to-end repro (open form → delete source in another
window → OK form → run Check & Repair → assert no dangling reference)
would be a useful interface-test follow-up but is not gated on the
patch landing.
