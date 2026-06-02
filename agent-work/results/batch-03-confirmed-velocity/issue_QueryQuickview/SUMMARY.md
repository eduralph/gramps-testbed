# QueryQuickview — confirm-and-close (already fixed upstream)

## Status
**Closed as duplicate / already fixed.** No new fix written.

## Verification
The increment-1 addendum flagged this item as "DIRECTORY NOT FOUND" and
asked to first resolve the addon's real name. Triage on 2026-05-25:

- `ls -d */ | grep -i query` → `Query/`. The addon is named **Query**;
  the detector's `QueryQuickview` label is the module name
  (`Query/QueryQuickview.py`), not the addon directory.
- `python3 -m py_compile Query/QueryQuickview.py` (and `QueryGramplet.py`
  and `Query.gpr.py`) → all compile cleanly on the current
  `upstream/maintenance/gramps60`. No `SyntaxError: '(' was never closed`.
- `git log upstream/maintenance/gramps60 -- Query/` → most recent
  functional commit is `724d4aa18 Query: fix missing closing paren in
  QueryQuickview (line 347)`, merged via gramps-project/addons-source
  PR [#834](https://github.com/gramps-project/addons-source/pull/834)
  (2026-05-14 to maintenance/gramps60). One commit further back is
  `7b817bbe4 Query: import sys in QueryGramplet`, both in PR 834.

PR 834 was the unbalanced-paren fix flagged by the detector. The loop
is closed.

## Repo and branch
- Repo: `addons-source` (upstream `gramps-project/addons-source`)
- Branch: `maintenance/gramps60`
- Reference commit: `724d4aa18` (PR 834, merged 2026-05-14)
- This batch: no new commit; no patch.diff or pr-description.md.

## Mantis link
None — detector-sourced (c)-bucket; no Mantis issue to update.

## Note on the addendum's lead
The addendum's task list explicitly anticipated this outcome ("If it
exists under another name/case → … keep the fix to the syntax error
ONLY"). The directory rename clarifies the detector label
(addon=`Query`, module=`QueryQuickview.py`) and the fix is already in
the tree, so no new change is needed.
