# WordleGramplet — confirm-and-close (already fixed upstream)

## Status
**Closed as duplicate / already fixed.** No new fix written.

## Verification
The increment-1 addendum flagged this item as "LIKELY ALREADY FIXED" and asked
for a confirm-and-close. Triage on 2026-05-25 verified:

- `grep -rn 'imap' WordleGramplet/*.py` → empty. The bare `from itertools
  import imap` flagged by the detector is gone from the addon source.
- `WordleGramplet/tests/test_wordlegramplet_imports.py` exists and is the
  regression guard for exactly this fix (docstring references the original
  `cannot import name 'imap' from 'itertools'` failure).
- `git log upstream/maintenance/gramps60 -- WordleGramplet/` head is
  `d333c6597 WordleGramplet: migrate Py2 / Gramps-3 era imports to Gramps
  5+`, merged via gramps-project/addons-source PR
  [#875](https://github.com/gramps-project/addons-source/pull/875)
  (2026-05-15 to maintenance/gramps60).
- Forward-merged to upstream/maintenance/gramps61 as commit
  `9e59e4003` (same commit message).

The PR-875 fix migrated all four stale imports in one logical change
(`imap` → `map`, `gen.plug` → `gramps.gen.plug`, etc.) and added the
regression test the detector's failure-mode now points at — the loop is
closed.

## Repo and branch
- Repo: `addons-source` (upstream `gramps-project/addons-source`)
- Branch: `maintenance/gramps60` (and `maintenance/gramps61` via forward
  merge)
- Reference commit: `d333c6597` (PR 875, merged 2026-05-15)
- This batch: no new commit; no patch.diff or pr-description.md.

## Mantis link
None — detector-sourced (c)-bucket; no Mantis issue to update.

## Note on the addendum's lead
The addendum's task list explicitly anticipated this outcome ("If source
is clean and the import test passes → confirm-and-close, link the
PR/commit that already fixed it. Do NOT write a duplicate fix."). Done.
