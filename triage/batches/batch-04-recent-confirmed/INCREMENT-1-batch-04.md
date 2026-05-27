# Claude Code increment — batch-04-recent-confirmed, INCREMENT 1

> Read alongside CLAUDE_CODE_BRIEF.md (binding) and each issue_<id>.md verdict.
> Standing rules apply: trust the verdict over the title; resolve addon-vs-core
> by reproducing; repro-or-close before fixing; check merged AND closed PRs;
> one logical fix per issue with a test in the same change; STOP after writing
> results (no push/PR/ready-mark — Eduard's review gate).

## Batch-04 POSTURE (read before starting — this batch behaves differently)
This is a recent-pool fix-oriented batch, but the scraped threads showed a high
rate of NON-fix outcomes. Adjust default posture accordingly:

1. **Confirm-and-close is expected, not exceptional.** Many items are already
   fixed, have an open/merged PR, or are by-design. For any item whose verdict
   says "verify upstream isn't ahead" or "ALREADY FIXED", the FIRST action is the
   verification, not a fix. Only write a fix if the check shows the defect is
   still live on the target branch.
2. **An existing PR means VERIFY, not rewrite.** If a verdict links a PR
   (13966→#913, 13326→#2330), assess its state + branch (mind gramps60-vs-61),
   then confirm-and-close (merged) or review-and-note (open). Do NOT open a
   competing PR. (See playbook 04 step 4.)
3. **Respect cluster-split notes.** Where a verdict pairs two issues "verify
   shared cause, DO NOT bundle" (13864/13865 Dashboard; 13174/13906 addon-mgr),
   confirm the cause is actually shared before treating as one fix — two items
   can share a symptom and differ in cause.
4. **Some bugs need a built fixture.** example.gramps does NOT trigger several of
   these; the verdict says so. Build a minimal synthetic fixture at
   `tests/interface/data/bug_<id>_minimal.gramps` (or an addon test fixture) —
   e.g. a prefixed surname (13406-class), a duplicate-ancestor pedigree collapse
   (14051-class), a long note (13268). Never use Eduard's real data.

## Increment-1 items (strongest core fixes, all → maintenance/gramps61)
Worked in this order. All have in-thread or description-level root cause.

### 13819 — Family Edit reorders parent families (MAJOR) — LEAD
Pre-diagnosed in note 1: child-ref lists compared by Python IDENTITY not handle,
so set.difference() marks every child both removed and re-added. Fix: compare by
handle. PRE-FLIGHT: note 1 author said "plan to work on this today" — CHECK for an
already-landed fix/PR (merged AND closed) before writing. If live, core fix +
unittest on the child-ref diff (equal-handle/different-instance objects).

### 13747 — saving unmodified DB changes it on disk
Root cause in note 3: metadata stored as Python sets (unordered) re-serialize in a
different order each close. Fix: deterministic ordering (sort before store / ordered
structure). SCOPE: ordering only — do NOT bundle the read-only-export split (13748).
Test: serialize metadata twice, assert byte-stable.

### 13716 — sidebar Filter gramplet Type popup not updated
Root cause in note 3 (maintainer): sidebar filter Type selector built once at
view-open, never refreshed. Fix: generalize the place-sidebar-filter refresh from
PR #809 (READ #809 FIRST) to the other sidebar filters. Test: core unittest on the
type-list refresh.

### 13832 — Gramps-Web UUID hyphen handles break Graph View
Root cause notes 5-10: Gramps-Web creates UUIDv4 handles WITH hyphens; a core path
fails on them. dstraub (note 10): schema allows any ≤50-char string, so not handling
them is a bug. Fix: handle arbitrary schema-valid handles (hyphens). Distinct from
13830 (path-to-home short-circuit). Repro: import the reporter's example.gramps
(note 1) with hyphenated handles. Test: core unittest with a hyphenated handle.

### 13418 — LaTeX report str_incr TypeError
Root cause is in the DESCRIPTION traceback (latexdoc.py:512 str_incr —
`if lili[i] < "z"` with i a string). CORRECTION: note 1's familygroup.py stack is
the DIFFERENT bug 13417 (KeyError: 9) — do not chase it. codefarmer (note 3)
confirms 13418 repros on 5.2.2 without the 13417 changes. Fix: index str_incr by
int, not the string element. Test: headless core unittest in plugins/docgen/test/.
PRE-FLIGHT: confirm PR 1762 / bug 13417 state on gramps61 and that str_incr is
independent (it is).

### 13326 — Forms gallery AttributeError (CORE teardown race) — VERIFY PR 2330 FIRST
Eduard's note 5 already contains the full triage + names gramps PR #2330. FIRST
ACTION: verify PR 2330's state on gramps61. If merged → confirm-and-close. If open
→ review-and-note, do not rewrite. If somehow absent → the fix is: restore the
'selection-changed' disconnect in GalleryTab.clean_up() guarded by
GObject.signal_handler_is_connected; tests in
gramps/gui/editors/displaytabs/test/gallerytab_test.py (per note 5). NOT the Forms
addon — core, gramps61. Same teardown-race family as 13059.

## Per-item: write results/issue_<id>/ then STOP
Each item: SUMMARY.md (root cause, fix/close, test, repo+branch, outcome),
patch.diff (if a fix), pr-description.md (if a PR is warranted), mantis-comment.md
(ALWAYS), MANUAL-VERIFICATION.md (only if a manual-work outcome — none expected in
this increment). STOP for review; no push/PR/ready-mark.

## Expected increment-1 shape
Likely a mix: 13819/13747/13716/13832/13418 as real core fixes (if the pre-flights
confirm them live), and 13326 most likely a verify-PR-2330 confirm-and-close. That
is a normal, successful increment — fixes and evidenced closes both count.
