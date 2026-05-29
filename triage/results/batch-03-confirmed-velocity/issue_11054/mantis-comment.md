PR open against addons-source `maintenance/gramps60`:
https://github.com/gramps-project/addons-source/pull/NNN — implements
the narrow save-time guard from notes 5 and 7 verbatim:

* EditForm.save (source path): when the citation's source handle no
  longer resolves, write a replacement Source rather than commit a
  None-target reference.
* MultiSection.save: skip rows whose person handle no longer
  resolves, in both the row-update loop and the removed-people detach
  loop.
* PersonSection.save / FamilySection.save: early-return when the
  attached handle is dead, skip the detach when the initial handle is
  dead.

No behaviour change when references are intact. Architecture-level
fixes (snapshot/locking/JSON-patch) discussed on the ticket remain
out of scope as agreed.

Regression test in Form/tests/test_editform_save_guards.py — eight
cases driving each save method via __new__-bypass; pre-fix 2
failures + 5 errors, post-fix green. Verified locally via the
gramps-testbed addon-unit runner.
