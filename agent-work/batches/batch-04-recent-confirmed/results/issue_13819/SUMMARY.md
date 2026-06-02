# Issue 13819 — Family Edit window changes the order of parent families

**Outcome: ALREADY FIXED upstream — confirm-and-close.**

## Root cause
In `EditFamily.save()` the transaction that commits family edits diffed the
child-reference lists with set operations on the `ChildRef` *objects*. Python
compares those objects by identity, and `original.get_child_ref_list()` /
`self.obj.get_child_ref_list()` hold *different instances* representing the same
children. So `orig_set.difference(new_set)` reported every existing child as
both removed and re-added; the resulting `remove_parent_family_handle` /
`add_parent_family_handle` cycle re-appended the family to each child, losing
the (significant) parent-family ordering.

This is exactly the diagnosis the reporter gave (description + note 1).

## Resolution — no new fix written
The defect is **not live** on the target branch. A fix had already landed:

- **PR:** gramps-project/gramps#2266 — "Ensure family order is unaffected by
  family edits"
- **Commit:** `f7c6444a34273f421b11cab3bbe635de612649be` (Ian Davis, the note-1
  author "aviansid" who wrote "I plan to work on this today")
- **Merged:** 2026-05-28 → `maintenance/gramps61` (the correct target per the
  verdict)
- **Fixes #13819** is in the commit message (Mantis cross-link present).

The fix is the one the verdict sketched: compare by handle, not object identity.

```
-                orig_set = set(original.get_child_ref_list())
-                new_set = set(self.obj.get_child_ref_list())
+                orig_handles = set(ref.ref for ref in original.get_child_ref_list())
+                new_handles = set(ref.ref for ref in self.obj.get_child_ref_list())
```
(and the two `for` loops iterate handles, fetching the person by handle directly).

Verified against `maintenance/gramps61` @ `f7c6444a34`,
`gramps/gui/editors/editfamily.py:1318-1332`: the diff now keys on `ref.ref`, so
an edit that leaves the child set unchanged produces empty difference sets and no
remove/add cycle — ordering is preserved.

## Branch / forward-merge state
- On `maintenance/gramps61`: **yes** (`git merge-base --is-ancestor` confirms).
- On `master`: **not yet** forward-merged. Forward-merge from the maintenance
  branch to master is the developer's responsibility (per gramps-testbed
  CLAUDE.md), not part of this triage. Flagging it so the resolver does not mark
  the bug fully resolved until it has reached master.
- **Fixed in version:** 6.1.0 (current gramps61 head is 6.1.0-beta1).

## Test
PR #2266 merged **without** a regression test — the only changed file is
`editfamily.py`. The behaviour is GUI-driven (Family Editor save path), so the
natural coverage is a testbed interface test
(`tests/interface/test_bug_13819_family_order.py`) that opens a family with ≥2
parent families, edits + OKs, and asserts the parent-family order is unchanged.

This is **not** written here: the increment-1 posture is verify-first for
ALREADY-FIXED items, and the fix is already merged. Recommending the regression
test as an optional testbed follow-up for Eduard to decide on (precedent: the
14100 hardening test PR #27). Not blocking the close.

## Files in this result dir
- `SUMMARY.md` (this file)
- `mantis-comment.md` — ready-to-paste tracker close, Eduard's voice
- no `patch.diff` / `pr-description.md` — fix exists upstream, nothing to author.
