# Claude Code increment — batch-04-recent-confirmed, INCREMENT 2

> Read alongside CLAUDE_CODE_BRIEF.md (binding) and each issue_<id>.md verdict.
> Standing rules apply: trust the verdict over the title; resolve addon-vs-core
> by reproducing; repro-or-close before fixing; check merged AND closed PRs;
> one logical fix per issue with a test in the same change; STOP after writing
> results (no push/PR/ready-mark — Eduard's review gate).

## Batch-04 POSTURE (carried from increment 1 — still applies)
1. **Confirm-and-close is expected, not exceptional.** For any item flagged
   POSSIBLY-FIXED or whose verdict says "verify upstream isn't ahead", the
   FIRST action is the verification, not a fix. Only write a fix if the check
   shows the defect is still live on the target branch.
2. **An existing PR means VERIFY, not rewrite.** Assess state + branch (mind
   gramps60-vs-61), confirm-and-close (merged) or review-and-note (open). Do
   NOT open a competing PR.
3. **Respect cluster-split notes.** Increment 2 has TWO cluster pairs
   (13864/13865 Dashboard; 13906/13174 addon-mgr). Confirm shared cause from
   the notes BEFORE treating as one fix — two items can share a symptom and
   differ in cause.
4. **Some bugs need a built fixture.** 13268 (long note in Notes editor) needs
   a synthetic fixture; example.gramps does not trigger it. Build at
   `tests/interface/data/bug_<id>_minimal.gramps` (or an addon test fixture).
   Never use Eduard's real data.

## Increment-2 items (10 items, all → maintenance/gramps61)
This is the heaviest increment — two clusters to verify and one 19-note thread.
Work in this order; clusters together, NO-NOTES items last so the bulk of the
context comes from the heavily-discussed items first.

### 14033 — Frequent spurious "Place cycle detected" errors — LEAD
19 notes; the root cause is almost certainly in the thread, not the
description. READ ALL 19 NOTES FIRST. Likely hypotheses to verify against the
notes: detector is over-eager on legitimate enclosed-by chains, OR the
traversal is failing to mark visited nodes correctly so a non-cyclic chain
trips the detector. Determine WHICH from the notes before reproducing. Fix:
core — `gramps/gen/lib/place*.py` or the place-merge / enclosed-by traversal.
Test: headless `unittest.TestCase` constructing a synthetic enclosed-by chain
that the current code falsely flags. PRE-FLIGHT: merged AND closed PRs for
"place cycle" / "enclosed_by" on gramps61.

### 13744 — Empty dates saved in a non-round-tripping format
Same data-integrity family as 13747 (inc 1: deterministic-ordering fix on
metadata sets) but DISTINCT root cause — verify before assuming overlap. Fix
the empty-date serializer to produce a form the deserializer accepts.
Round-trip test: serialize an empty date, deserialize, assert byte-equality
on the next serialize. SCOPE: empty-date round-trip only — do not bundle
non-empty date format work even if related code is touched.

### 13864 — Dashboard crashes & locks family tree (with "Gramplet L...")
Cluster candidate with 13865 (both Dashboard). VERIFY SHARED CAUSE FIRST:
read notes on both; if 13864 is gramplet-add crash and 13865 is column-count
crash, they're different bugs that happen to share the Dashboard surface.
Repro on example.gramps (add gramplets until lock; identify the exact action
that locks). Fix scope: core (gramps/plugins/gramplet/ or gramps/gui/widgets/
grampletbar). Test: GUI interface test in
`gramps-testbed/tests/interface/test_bug_13864_<slug>.py` subclassing
`GrampsInterfaceTestCase` — dogtail-driven gramplet add until lock or
assertion of correct state.

### 13865 — Dashboard: Number of Columns 20 / Added Gramplet ap...
Paired with 13864 only by surface; treat as separate until shared cause
confirmed from notes. The "20 columns" framing suggests a bounds/layout bug
in the column-count handler. Repro: open dashboard, set columns to 20, add a
gramplet, observe failure. Fix likely in column allocation /
grampletbar.set_column_count or its callers. Test: state-assertion after
setting and reloading dashboard config — does NOT require GUI if the
layout logic is testable headlessly via the dashboard model.

### 13876 — Citation Tree view mode fails to delete citations
NO-NOTES, so description is the only signal. Repro from description: open
Citation view in Tree mode, select a citation, attempt delete. Likely cause:
Tree-view branch of the delete handler missing or branched-off-by-mistake
in citation_view delete path. Fix in `gramps/plugins/view/citationtreeview.py`
or its parent. Test: headless unittest on the delete handler if reachable
without the GUI; else interface test in gramps-testbed.

### 13205 — Merging citations triggers MergeError
NO-NOTES, CORE-TRACE. The description should carry the traceback. Citation
merge has its own merge_citation_query path; the MergeError is raised when
the merge logic detects an unmergeable state. From the trace, identify
WHICH precondition is failing. Repro: build two citations in
example.gramps that share a source, attempt merge, observe the error. Test:
headless unittest in `gramps/gen/merge/test/` exercising the citation merge
path with the failing precondition.

### 13413 — Fan Chart Report font size inconsistent across generations
6 notes; root cause likely identified or narrowed in the thread. The Fan
Chart Report is core (gramps/plugins/drawreport/fanchart.py). Likely cause:
per-generation font sizing computed without anchoring to a base size, or
truncated to int at small generations producing pixel-rounding visible as
inconsistency. Fix in the font-size compute path. Test: headless unit test
calling the sizing function with N generations, asserting monotonic /
proportional sizing across the range.

### 13268 — Notes editor: Undo action scrolls/scrambles
2 notes. FIXTURE NEEDED: long-note fixture (a note long enough to require
scrolling) — example.gramps's notes are too short. Build a minimal seeded
tree with one long note. Repro: open the note, make an edit near the bottom,
undo, observe scroll/content corruption. Fix likely in the Undo handler of
the notes editor (gramps/gui/editors/editnote.py or the GtkTextView
undo-stack integration). Test: interface test in gramps-testbed driving
the note editor; assertion on cursor/scroll position after undo.

### 13906 — Addon Manager fails to update isotammi addons
12 notes, UPSTREAM + CORE-TRACE. Cluster with 13174 (same symptom, older
version) — VERIFY shared cause from notes before treating as one. The
UPSTREAM flag is real: if root cause is in github.com/Taapeli/isotammi-addons
packaging (the source repo for those addons, NOT gramps-project/addons-source),
this is RECORD-AND-STOP, not a fix. The CORE-TRACE says the proximate failure
is in Addon Manager code — fix there if it can be made robust to the upstream
quirk. Repro: install an isotammi addon via Addon Manager (URL or local
build), attempt update, observe failure. Fix in `gramps/gui/plug/_windows.py`
or `gramps/gen/plug/_pluginreg.py` if the path is core; otherwise comment
and close as external.

### 13174 — Addon Manager fails to update isotammi addons (5.2.0-rc1)
Cluster pair with 13906. Same workflow but on 5.2.0-rc1. If 13906 is fixed
on gramps61, verify whether the fix back-applies to gramps60 (where 13174's
era would be patched). If shared cause confirmed, ONE fix + ONE test; close
13174 against the same PR.

## Per-item: write results/issue_<id>/ then STOP
Each item: SUMMARY.md (root cause, fix/close, test, repo+branch, outcome),
patch.diff (if a fix), pr-description.md (if a PR is warranted),
mantis-comment.md (ALWAYS), MANUAL-VERIFICATION.md only if a manual-work
outcome surfaces (none expected in this increment — flag if one emerges).
STOP for review; no push/PR/ready-mark.

## Expected increment-2 shape
A mix dominated by real core fixes. Likely shape: 14033/13744/13413/13268
as real fixes (long notes / clear root cause); 13864/13865 split into two
fixes after the cluster check; 13876/13205 either real fixes (if the
descriptions yield clean repros) or repro-or-close if not; 13906/13174
either ONE fix or record-and-stop on external, depending on the UPSTREAM
flag's outcome. 7-9 real fixes plus 1-3 closes is a normal outcome.

## Decision points worth flagging back to Eduard
- If the addon-mgr cluster resolves to UPSTREAM (Taapeli packaging), the
  fix path needs an Eduard decision: defer, or open an issue at
  Taapeli/isotammi-addons? Flag in SUMMARY.md, do not act unilaterally.
- If 13864 or 13865 suggests a Dashboard UX redesign (e.g. clamping max
  columns), STOP after diagnosis — UX direction is Eduard's call.
