# Claude Code increment — batch-04-recent-confirmed, INCREMENT 3

> Read alongside CLAUDE_CODE_BRIEF.md (binding) and each issue_<id>.md verdict.
> Standing rules apply: trust the verdict over the title; resolve addon-vs-core
> by reproducing; repro-or-close before fixing; check merged AND closed PRs;
> one logical fix per issue with a test in the same change; STOP after writing
> results (no push/PR/ready-mark — Eduard's review gate).

## Batch-04 POSTURE (carried from increment 1 — still applies)
1. **Confirm-and-close is expected, not exceptional.** This increment is
   confirm-and-close HEAVY: half the items carry POSSIBLY-FIXED, EXTERNAL-REPO,
   UPSTREAM, or "verify PR isn't ahead" flags. The DEFAULT first action on
   each is the verification, not a fix.
2. **An existing PR means VERIFY, not rewrite.** 13966 links PR #913 (open).
   Assess state + branch (mind gramps60-vs-61), confirm-and-close (merged) or
   review-and-note (open). Do NOT open a competing PR.
3. **EXTERNAL-REPO is RECORD-AND-STOP, not a fix here.** 13920 is filed under
   FamilyTreeView, which lives at github.com/Nick-Hall/FamilyTreeView — NOT
   in addons-source. We cannot land a fix in this repo for an addon hosted
   elsewhere; the outcome is a tracker comment pointing to the correct repo.
4. **Resolve addon-vs-core BY REPRODUCING for items flagged CORE-TRACE.**
   13830 and 13888 carry CORE-TRACE; 14051's verdict says "RESOLVE addon-vs-core
   by repro". If the fix lands in `gramps/...` rather than the addon, the
   branch target shifts gramps60 → gramps61. DEFER such items to increment 4
   rather than mixing repos mid-increment.

## Increment-3 items (9 items, expected target → maintenance/gramps60)
Confirm-and-close items first so context-heavy verifications happen while
fresh. Order:

### 13920 — [FTV] TypeError: Pango.extents_to_pixels() — LEAD (verify-and-close)
EXTERNAL-REPO + UPSTREAM + POSSIBLY-FIXED. Three independent reasons this
will not be fixed here:
- FamilyTreeView lives at github.com/Nick-Hall/FamilyTreeView, not in
  gramps-project/addons-source. Even if the fix is small, it can't land here.
- `Pango.extents_to_pixels()` is a GTK/Pango upstream API; signature changes
  there propagate downstream. The flag is "Pango took N args, was passed M".
- POSSIBLY-FIXED suggests a comment already references a release that
  resolves it.

FIRST ACTION: check the FTV repo for a fix referencing 13920 or the
Pango.extents_to_pixels call site; check the comment thread for the
referenced release. Outcome is almost certainly:
- mantis-comment.md: "fixed in FTV vX.Y.Z (link to FTV PR/commit); not an
  addons-source defect — FTV is hosted at github.com/Nick-Hall/FamilyTreeView"
- SUMMARY.md: EXTERNAL-REPO close with citations
- No patch.

### 13966 — Closing family tree → Prerequisites Checker error — VERIFY PR #913
Per INCREMENT-1's verdict footer, PR #913 in addons-source is open and
addresses this. FIRST ACTION:
- Pull addons-source PR #913 metadata: target branch, files changed, state.
- Verify the fix shape is correct for the bug as described in issue_13966.md.
- If merged to maintenance/gramps60 → confirm-and-close citing PR + commit.
- If still open → review-and-note in SUMMARY.md (correctness, branch, gaps);
  do NOT write a competing PR. Defer to Eduard on whether to push #913
  forward.

### 13830 — [Graph View] "Show path to home person" doesn't work
CORE-TRACE + POSSIBLY-FIXED. Two-part pre-flight:
- POSSIBLY-FIXED: check addons-source maintenance/gramps60 history and
  closed PRs for "graph view" / "path to home". If already fixed, close.
- CORE-TRACE: if still live, REPRODUCE FIRST. If the traceback bottoms out
  in `gramps/...`, this is a core fix and the branch target shifts to
  gramps61 — DEFER TO INCREMENT 4, don't try to mid-stream the repo split.

If neither pre-flight diverts it: addon fix in GraphView, test in
`addons-source/GraphView/tests/test_<slug>.py` (create `tests/__init__.py`
if absent — same pattern as other addons in this batch).

Distinct from bug 13832 (Gramps-Web hyphenated handles in inc 1) — different
root cause even though both surface in GraphView/path code.

### 13888 — [GenealogyTree] LaTeX images referred wrong
CORE-TRACE. Repro: run the GenealogyTree LaTeX report on example.gramps with
at least one media reference. If the wrong-path is constructed in the addon's
LaTeX template/writer, it's an addon fix (gramps60). If the path comes
already-malformed from the core docgen layer, branch target shifts to
gramps61 — defer to inc 4.

Watch for shared root cause with 13418 (inc 1: `str_incr` TypeError in
latexdoc.py). If increment 1's results show 13418 fixed and the SAME
latexdoc.py path is implicated here, there's a docgen-cluster story to
flag back to Eduard. Otherwise treat as independent.

### 13589 — [Family sheet] extra page
11 notes, UPSTREAM flag. Read the thread before acting — UPSTREAM here
likely means reportlab pagination behaviour, not a Gramps bug. If the
thread already pins it to a reportlab version/behaviour, outcome is
record-and-stop with a comment citing the upstream issue. If the addon
has a pagination workaround it could apply, that's an addon fix
(addons-source/FamilySheet, gramps60). Likely outcome: record-and-stop
or a narrow workaround in the FamilySheet pagination logic.

### 14051 — DetailedDescendantBookReport AttributeError
13 notes; "RESOLVE addon-vs-core by repro" per BATCH_INDEX. The Book Report
machinery is core (gramps/plugins/textreport/) but DetailedDescendantReport
specifically may be a Book-only wrapper. Repro on example.gramps; trace the
AttributeError to its source. If the attribute is missing on a core object,
fix is core/gramps61 — DEFER to inc 4. If it's a Book-wrapper-side wiring
bug, fix is core but specifically in the Book Report code (still gramps61
in practice).

If the verdict in issue_14051.md is unambiguous on repo target, follow it;
otherwise repro first.

### 13979 — PostgreSQL Enhanced load error in Addon Manager
3 notes. PostgreSQL Enhanced lives in addons-source. The error is on the
addon manager's load path for this specific addon — likely a `requires_mod`
declaration mismatch (psycopg2 vs psycopg, or missing psycopg in the .gpr.py),
or a Python-version-conditional import. Repro: install via Addon Manager,
observe the error. Fix in the addon's .gpr.py or its top-level imports.
Test: addon unit test that loads the addon module via plugin manager and
asserts no ImportError.

### 13707 — Lib WebConnect install inconsistency
4 notes; description mentions a specific missing line. Lib WebConnect is in
addons-source. Likely cause: a packaging or .gpr.py declaration that omits
something other webconnect addons declare correctly. Read the notes for the
specific "need the line: ..." finding and apply. Test: addon structure test
asserting the file or line is present.

### 13694 — make.py listing addon with include_in_listing=False
2 notes. addons-source TOOLING fix, not an addon fix. make.py's listing
logic respects `include_in_listing` for some paths but not for the listing-
generation path. Fix in `addons-source/make.py`. Test: a small unit test
on the listing generator with a fixture containing one
`include_in_listing=False` addon, asserting it's excluded. Pure-Python,
runs on Linux + Windows under PR #820's CI.

## Per-item: write results/issue_<id>/ then STOP
Each item: SUMMARY.md (root cause, fix/close, test, repo+branch, outcome),
patch.diff (if a fix), pr-description.md (if a PR is warranted),
mantis-comment.md (ALWAYS), MANUAL-VERIFICATION.md only if a manual-work
outcome surfaces (none expected in this increment — flag if one emerges).
STOP for review; no push/PR/ready-mark.

## Expected increment-3 shape
Confirm-and-close dominant. Likely:
- 13920: EXTERNAL-REPO close (almost certain).
- 13966: confirm-and-close on PR #913 OR review-and-note (depends on #913 state).
- 13830: POSSIBLY-FIXED close OR deferred to inc 4 if core.
- 13888: addon fix OR deferred to inc 4 if core (and possibly clustered with 13418).
- 13589: UPSTREAM close OR narrow workaround.
- 14051: deferred to inc 4 if core; addon fix if not.
- 13979, 13707, 13694: real addon fixes.

So roughly 3-4 real addon fixes, 3-4 closes, 1-3 deferrals to inc 4 for
items that resolve to core. Deferrals are a normal outcome — DO NOT try
to "rescue" by branching to gramps61 within this increment.

## Decision points worth flagging back to Eduard
- 13920 (FTV): the mantis comment should point at the upstream FTV repo
  and ask the reporter to refile there. Confirm Eduard wants that phrasing
  before posting — some maintainers prefer to file the upstream issue
  themselves.
- 13966 + PR #913: if #913 looks correct but stalled, an Eduard ping to
  the PR author is the unblock, not a competing PR.
- Any deferral to inc 4: SUMMARY.md must say WHY (repo target shifted to
  core/gramps61) so inc 4's planning knows it's incoming.
