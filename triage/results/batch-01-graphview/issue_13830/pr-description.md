## Root cause
The fix for Mantis 13830 already shipped in commit 48a6cbfb05 (2025-08-09):
`init_list` had `for person_handle in firstList and secondList:`, which
Python evaluates as `secondList` via short-circuit `and`, causing
`firstMap[person_handle]` to raise `KeyError` on handles reachable from
the second root but not the first. The fix renamed `firstList`/`secondList`
to `firstSet`/`secondSet` and corrected the loop to use set intersection.
However the rule still has no direct test, so the regression could
reappear unnoticed.

## Fix
Test-only. Adds `test_relationshippathbetween` to
`gramps/gen/filters/rules/test/person_rules_test.py`, exercising the
rule with two example.gramps persons that share no ancestor — the exact
configuration that triggered the previous `KeyError`.

## Verified against
- `gramps/gen/filters/rules/person/_relationshippathbetween.py:127` —
  current `init_list` uses `firstSet & secondSet`, confirming the fix is
  live on this branch.
- Pre-fix file (checked out at `48a6cbfb05^`): the new test fails with
  `KeyError` at `_relationshippathbetween.py:130` — same exception class
  and same line cited in the reporter's traceback.
- Regression-introducing commit: `1280aa45a5` ("Refactor, fix, and
  optimize filters/rules").
- Fix commit (already on this branch): `48a6cbfb05` ("Fix regression in
  relationship path between people filter").

## Test
`test_relationshippathbetween` — passes on current branch (88/88 tests
in `person_rules_test.py` pass), fails on the pre-fix file with the
original `KeyError`.

Fixes #13830.
