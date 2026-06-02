# Issue 13830 — [Graph View] "Show path to home person" KeyError

## Outcome
**Already fixed upstream.** No code change to ship. Deliverable here is a
regression test that covers the previously-untested core rule.

## Verdict revision
The triage VERDICT correctly redirected from the reporter's
config-key-casing workaround to the path-to-home filter logic, and
correctly noted "addon vs core" as a decision point. It was wrong about
the root cause within core — the bug was not "handle absent due to
disconnected sub-graphs" but a short-circuit-`and` typo in `init_list`.
The fix locus is **gramps core**, and the fix has shipped.

## Root cause
`gramps/gen/filters/rules/person/_relationshippathbetween.py` —
`init_list()` contained

```python
for person_handle in firstList and secondList:
    new_rank = firstMap[person_handle]
```

Python evaluates `firstList and secondList` as `secondList` (short-circuit
`and` on two non-empty sets returns the right operand). The loop therefore
iterated over `secondList` (ancestors of the *home* person) and read
`firstMap[person_handle]` (built from ancestors of the *active* person).
`KeyError` fired on the first handle in `secondList` that was not also in
`firstMap` — essentially any time the two persons did not share their
entire ancestor set.

Regression introduced by gramps commit `1280aa45a5` ("Refactor, fix, and
optimize filters/rules", 2025-02-03) — the prior version (`bf4b3962bc`)
correctly used `firstList & secondList`.

## Fix already in upstream
gramps commit `48a6cbfb05` ("Fix regression in relationship path between
people filter", 2025-08-09) renames `firstList` → `firstSet`,
`secondList` → `secondSet`, and restores `firstSet & secondSet`. The
commit is on `maintenance/gramps60`, `maintenance/gramps61`, and `master`;
shipped in tags `v6.0.4` through `v6.0.8` and `v6.1.0-beta1`.

Verified on local `maintenance/gramps61` tip
(`c51b573ccd Fix missing repo for new chardet module.`):
`gramps/gen/filters/rules/person/_relationshippathbetween.py:127` reads
`for person_handle in firstSet & secondSet:`.

## Why the reporter's workaround was a red herring
daleathan's "deleting the GraphView ini settings fixed it" report
pointed at commit `6357efb` (case change of `interface.graphview-show-id`
keys). That commit is real but unrelated — current
`addons-source/maintenance/gramps61` GraphView/graphview.py:155, 193, 674,
754, 2383 already use the lowercase form, and the KeyError traceback
terminates inside gramps core, not in GraphView code.

## Repo + branch targeted
- repo: `gramps-project/gramps`
- branch: `maintenance/gramps61`
- change scope: test-only (regression guard for a fix that already shipped)
- file: `gramps/gen/filters/rules/test/person_rules_test.py`

`RelationshipPathBetween` had no direct test coverage; only the wrapper
`RelationshipPathBetweenBookmarks` was tested.

## Test
Added `BaseTest.test_relationshippathbetween` constructing the rule with
two persons from example.gramps that share no ancestor (`I0044`, the home
person, and `I2127`, a member of the unrelated Δεληπέτρου family). On
the fixed code the rule returns the two endpoints; on the buggy code it
raises `KeyError` at `_relationshippathbetween.py:130` — same line and
same exception class the reporter saw. The specific handle in the
`KeyError` varies between runs (set-iteration order under Python's hash
randomization) but is always a handle in the unrelated Δεληπέτρου family.

Verified:

- Fixed source (current `maintenance/gramps61`): test passes.
- Buggy source (file checked out at `48a6cbfb05^`): test fails with the
  reported `KeyError` at the reported line.
- Full `person_rules_test.py` suite (88 tests) still passes.

`black --check` is clean for the modified file.

## Tracker action (Eduard)
Bug is fixed in shipped releases; Mantis 13830 can be resolved with
"Fixed in version" set to the appropriate release on the relevant project
(Gramps 6.0 project → 6.0.4; Gramps 6.1 project → 6.1.0).

## Files in this directory
- `SUMMARY.md` — this file
- `patch.diff` — the regression-test addition (against
  `gramps-project/gramps:maintenance/gramps61`); uncommitted in the
  sibling repo
- `pr-description.md` — body to use if Eduard chooses to send a
  test-only PR
