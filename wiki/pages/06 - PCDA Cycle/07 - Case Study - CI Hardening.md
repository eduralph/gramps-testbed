---
title: "Case Study — CI hardening, one cycle three turns"
categories: []
managed: false
status: active
---

> A worked example of the PDCA cycle from [[01 - The Quality Cycle]]
> applied to the Gramps testbed CI itself. Three brief versions track
> one contribution-batch through three turns of activity: **Plan v1**
> (initial spec) → **iterate-to-Plan v2** (in-cycle spec revision
> after the builder reviewed v1) → **v3** (mixed Check sign-off on
> open items + one genuine Act-class process delta). The case study
> demonstrates two things the model insists on:
>
> 1. **In-cycle iteration is not Act.** v2 revising v1 is a Plan re-do
>    on the same contribution-batch (the [[02 - Cycle Artifacts]] §9
>    iterate-to-Plan path), not process improvement.
> 2. **A spec being wrong is Act material.** v3's Item C — "the
>    template demanded an exec-shim that empirical evidence showed
>    was never needed" — is the process baseline being adjusted, not
>    the contribution being adjudicated.
>
> A parallel example at the end of the doc contrasts the brief-shaped
> CI-hardening Plan with a design-shaped Plan (GEPS 049 — *Versioned
> Addon API surface and 2 axis lifecycle model*), showing what Plan
> looks like at the larger end of its scope range
> ([[01 - The Quality Cycle]] §Solution-approach design).

## What the cycle was for

Fix the divergences and gaps identified in a CI review of the
gramps-testbed `main` branch: hardcoded fork owner; branch-target
default drift; copy-pasted `requires_mod` extractor; missing degraded-
coverage guard on Windows; no `concurrency` control; an unrestricted
`push:` trigger; copy-pasted step bodies (msgfmt loop, venv setup, repo
resolution); missing timeout caps.

One logical change → one PR; draft only; cite path:line; per-item
`agent-work/results/ci-hardening/ci-<slug>/{SUMMARY.md,patch.diff}`; STOP after each. The
spec-and-marching-orders shape that [[02 - Cycle Artifacts]] names
`brief.md`.

## Turn 1 — Plan (v1 brief)

`CLAUDE_CODE_BRIEF-ci-hardening.md` (v1) opened seven items:

1. Fix the hardcoded fork owner in `upstream-sync.yml`.
2. **Reconcile branch-target defaults — DECISION REQUIRED.** Laid out
   options, recommended one, marked the decision yours.
3. Single-source the `requires_mod` extractor (kill the duplication
   between `addon-unit-tests.yml` and `windows-addon-unit-tests.yml`).
4. Port the degraded-coverage guard to the Windows addon job.
5. Add `concurrency` control to all workflows (blanket cancel).
6. Scope `dev-tooling.yml`'s `push:` trigger.
7. DRY the duplicated step bodies into composite actions.

Plus a "Not in scope" list documenting third-party action pinning and
fork-PR reporting limitation as record-only.

This is a textbook Plan artifact: spec per item, success criterion
("`actionlint` clean", "byte-level behavioral equivalence"), branch
target named explicitly (the testbed's `main`, not addon → gramps60),
scope discipline ("one logical fix per PR; bundling hides mistakes"),
honest oracle limits ("`actionlint` does **not** validate runtime
behavior — say so").

## Turn 2 — iterate-to-Plan (v2 brief, in-cycle spec revision)

The builder (Claude Code) reviewed v1 in-repo
(`ci-hardening-brief-review.md`, 2026-06-01) and surfaced findings the
v1 spec hadn't anticipated. Rather than build against v1 anyway, the
cycle **revised the brief in place** before continuing — the
[[02 - Cycle Artifacts]] §9 *iterate-to-Plan* path: the contribution
stays the same (still the CI hardening batch), the **spec for that
contribution** is re-authored, then Do re-runs.

The amendments (preserved verbatim from v2's "Changes from v1"
preamble):

- **Item 2 is no longer open-ended DECISION-REQUIRED.** The review
  found the authoritative doc (`CLAUDE.md` / its imported
  `CLAUDE-pr-rules.md`) is self-contradictory on the addon branch
  target, and that contradiction is the root cause of the YAML drift.
  The addon-dev guidelines (doc 16) already adjudicate it: **addon
  work targets `maintenance/gramps60`**; the maintainer cherry-picks
  forward to gramps61. Item 2 is now a settled fix (addon-test jobs →
  gramps60, plus a `CLAUDE.md` correction), with **one** genuinely-open
  sub-question left (the `dev-tooling` analyzer branch).
- **Item 1 gains caveat A**: the YAML owner swap is coupled to the
  `FORK_SYNC_TOKEN` PAT scope. Verify the fork remotes' owner *before*
  editing.
- **Item 5 changes the idiom**: `cancel-in-progress` is now conditional
  so post-merge `main` runs always complete.
- **Item 3 softened**: don't claim a live regex bug without a real
  example; the copy-paste drift justifies the change on its own. Name
  that the exec-shim runs arbitrary code.
- **New Item 8**: add the two missing `timeout-minutes` (most jobs
  already have them — narrow gap, not systemic).
- **Appendix expanded**: third-party action pinning recorded as
  record-do-not-fix.

**Why this is iterate-to-Plan, not Act.** The amendments are about
*this contribution batch's* spec, not about the project's process
baseline:

- Item 2's framing change ("decision-required" → "settled, with a
  different root-cause fix") edits the v1 brief for the CI-hardening
  contribution. It does not edit the `brief.md` template that the next
  unrelated contribution would inherit from.
- Item 1's caveat A is an additional check inside this brief, not a
  new clause in the standing process documentation.
- Item 3's softening narrows the spec's claim ("regex bug" → "copy-
  paste drift") for this fix, not for all future deduplication fixes.

If any of these *were* generalized into a process delta — e.g.
"every brief that touches CLAUDE.md must verify the doc isn't self-
contradictory first" — that would be Act material. As written they
are not; they revise this batch's spec only.

The v2 brief also added an explicit **Sequencing** section:

> 1. Item 2a first — patch `CLAUDE.md` (the authoritative source). The
>    root-cause fix; everything downstream points at it.
> 2. Item 2b, Items 1, 4, 6, 8 in parallel — independent quick wins.
> 3. Item 5 — uniform `concurrency` change.
> 4. Item 3 — self-contained, has a real pass/fail test.
> 5. Item 7 — last regardless; one PR per extracted action;
>    repo-resolution extraction last / DECISION-REQUIRED.

The sequencing is a Plan-time spec choice: which items the body can
fan out on in parallel, which must serialize, which carry a deferred
sub-decision. The driver in [[03 - Cycle Automation]] consumes this as
the per-issue queue order inside the batch.

## Turn 3 — v3 brief: Check sign-off + one Act-class delta

`CLAUDE_CODE_BRIEF-ci-decisions.md` (v3) addressed three items that v2
implemented but reached a DECISION/deviation and **stopped for human
adjudication**. In the new model, that adjudication splits cleanly
between **Check sign-off** (per-item dispositions for the
contribution-batch) and **Act** (process-baseline deltas observed
along the way):

| v2 open item | v3 action | Cycle beat |
|---|---|---|
| 2b — addon `addons_ref` flip (v2 declined: "incoherent 61/60 pair") | Reversed the prior decline, flipped `addons_ref`→gramps60 | **iterate-to-Plan** on this item (sub-brief revised) |
| 2 #3 — analyzer branch (v2 recommended gramps61, left unimplemented) | Ratified gramps61 | **Check sign-off** (accept the v2 recommendation) |
| 3 — regex vs exec-shim deviation | Ratified the regex deviation; **the v2 spec's exec-shim requirement was wrong** | **Check sign-off + Act-class process delta** |
| 1, 4, 5, 6, 8 (done) | Accept; await Eduard dispatch runs | **Check sign-off** (instrumented, manual-run pending) |
| 7 (partial) | Accept partial; local-action path needs a dispatch run | **Check sign-off**, partial |

### Item A — reversing your own prior decline (iterate-to-Plan)

V2 results recorded that you had declined the `addons_ref` flip on the
grounds that "61/60 pair is incoherent." Two facts surfaced after that
which changed the basis:

1. `maintenance/gramps61` *does* exist on `addons-source` — both addon
   branches are real.
2. The addon-unit-tests job header *states the purpose*: catch
   "addon-side import/ABI regressions against fresh upstream … while
   addons-source's own CI stays green."

From those facts, the **stated job is the gap between** addons-source's
two CIs: as-authored gramps60 addon against fresh gramps61 core.
Status-quo 61/61 duplicates addons-source's gramps61 CI and cannot be
an early warning. The "ships nowhere" property of 61-core/60-addon is
*the point of a forward-compat test*, not a defect.

V3's instruction to the builder is therefore: **verify the basis
first, and if after verifying both facts you still judge the flip
wrong — STOP and write why in SUMMARY.md instead of implementing.**

This is **iterate-to-Plan** on the sub-item: the spec for Item 2b is
being revised in light of evidence that surfaced after the v2 attempt,
and the cycle re-enters Do with the new sub-brief. It is not Act,
because the change is local to this contribution-batch — a different
batch wouldn't inherit "always reconsider declined items when new
evidence appears" as a written rule from this turn. (That generalization
*could* become Act if the pattern recurs across batches.)

### Item B — ratifying a recommendation (Check sign-off)

V2 left the `dev-tooling` analyzer branch as one open sub-question.
V3 ratified gramps61: the analyzers are core-subject — they scan
gramps core source and their findings become *core* PRs, which target
gramps61. So the analyzer job should analyze the branch core fixes
land on.

This is straightforward **Check sign-off**: the v2 brief produced a
recommendation, the human signs off accepting it as the disposition
for this sub-item. (The Family-B framing of
[[04 - Validation Tooling]] is what makes the decision tractable —
name the family first, the branch follows — but applying it here is
sign-off, not Act.)

### Item C — the spec was wrong, ratify the build and adjust the process (Check sign-off + Act delta)

V2 specced an exec-shim-based `requires_mod` extractor. V2 results
delivered a regex + `literal_eval` deviation — strictly speaking a
deviation from spec. V3's adjudication has **two parts in two
different beats**:

**Check sign-off (this contribution).** The deviation is accepted as
the disposition for Item 3 in this batch. Concrete action: append one
line to that item's `SUMMARY.md` recording the deviation as ratified.
The evidence is in §9 (sign-off) and §7 (proven by 14/14 literal-form
audit; unproven for any future addon that *does* declare a computed
`requires_mod`).

**Act delta (the process).** The v2 brief's framing — "exec-shim is
correctness insurance" — was wrong in the way that *briefs of this
shape* tend to be wrong: it demanded a specific implementation
mechanism when empirical reality (14/14 flat literals) made the
mechanism unnecessary. This is a process observation:

> *"Briefs should distinguish 'this is the correct implementation
> mechanism' from 'this is the correct outcome'. When a brief specifies
> a mechanism, it should cite the evidence that simpler mechanisms
> fail."*

That observation belongs in the **next Act review**'s `act-log.md`
entry, as a candidate spec-template clarification. The v2 brief itself
modelled the discipline ("don't claim a live regex bug without a real
example") for the *claim* part; the *mechanism* part needed the same
discipline and didn't get it. That's the Act delta.

In the [[02 - Cycle Artifacts]] §10 sense, this would have been
flagged on Item 3's `SUMMARY.md` §10 ("Act candidate: spec demanded a
mechanism we have no evidence was needed") at v2 sign-off; the next
Act review would have picked it up across however many bundles
exhibited similar mechanism-overshoot, and either updated the brief
template or written a new check ("brief mechanism clauses must cite
falsifying evidence for simpler alternatives").

### Item D — manual-run queue (Check sign-off, instrumented)

Five items needed Eduard's manual `workflow_dispatch` runs (token-
scoped sync, all-skipped guard on real Windows, cancellation
semantics, local-action path, the 60-addon/61-core build). Two Item-7
sub-extractions were deferred (composite-action shape decisions).

These are all **Check sign-off with §7 unproven**: the deterministic
gates have done what they can, the disposition is accepted, but the
oracle limits mean specific manual runs are needed to fully prove the
result. The sign-off is conditional — "merged-wider after these
dispatch runs come back green" — and the bundle remains AWAITING_
SIGNOFF in a queue sense, with the dispatch runs as the gating step.

## What the case study illustrates, mapped back to the model

- **In-cycle iteration vs Act.** Turn 2 looks like Act (the spec was
  reconsidered, learnings were applied) but is actually iterate-to-Plan
  *within the same contribution-batch cycle*. The contribution hasn't
  shipped; the spec is being revised so Do can produce a buildable
  patch. Act would be: this turn revealed something about the
  *process* that should be permanently changed. Most of v2 doesn't
  generalize that way.
- **Check sign-off does most of the closing work.** Items 1, 4, 5, 6,
  8 (the "quick wins"), Item B (analyzer branch ratification), the
  acceptance part of Item C, and the conditional-on-dispatch Item D
  cases are all Check sign-off — the human reading the result document
  and applying §9. None of them are Act; the cycle's process baseline
  doesn't move because of them.
- **One genuine Act-class delta surfaces (Item C's mechanism
  observation).** The spec template's pattern of demanding
  implementation mechanisms without falsifying-evidence-required for
  alternatives is process-level. It belongs in `act-log.md`, with a
  delta either to the brief template or to a new conformance check on
  brief authoring. Whether it gets applied depends on the next Act
  review; this case study flags the candidate.
- **The collapse rule** ([[01 - The Quality Cycle]] §Where the stages
  touch and collapse) — most v1/v2 items are *conformance-defect*
  fixes (wiring drift, copy-paste). Correctness reduces to conformance:
  `actionlint` clean is the oracle. Item 3 is the exception — it ships
  a real `unittest.TestCase` with fixtures because the extractor logic
  is the only item with genuine pass/fail behavior to test. The
  briefs say this explicitly: "this is the item's real pass/fail
  evidence; `actionlint` covers only the YAML wiring."
- **The oracle principle** — every brief item names what its mechanical
  check *proves* and what it *leaves unproven*. "Proves the YAML; it
  does **not** prove the 60/61 pairing actually builds — that needs a
  `workflow_dispatch` (Eduard's step)." Honest oracle accounting is the
  same discipline that fills §7 of `SUMMARY.md`.
- **The independence contract holds even when the builder reviews its
  own brief.** v2 was Plan-side feedback (does the spec make sense?),
  not Check-side verification (does the built artifact match the
  spec?). The reviewer's independence is about Check, not Plan; the
  builder can legitimately critique a spec it will later implement,
  because that critique runs *before* the artifact exists.

## What this would look like under full automation

Today this cycle ran with the human authoring each brief turn and
adjudicating each item. Under L3 of [[03 - Cycle Automation]]'s
maturity ladder, the contribution-batch shape persists:

- Plan v1 is human (brief authoring is irreducible).
- The driver fans Do + Check + assemble across the seven items in
  parallel where the sequencing allows, writing N
  `agent-work/results/ci-hardening/ci-<slug>/SUMMARY.md`.
- Items 2 #3, 3 (deviation), and 2b (declined-then-revisited) surface
  in §6 NEEDS-HUMAN with the reviewer's grounded evidence. The
  builder's brief-review output (a Plan-side artifact, distinct from
  the Check-side `check-review.md`) surfaces the v2 amendments as
  candidate spec edits.
- The sign-off queue presents the items cheap-first. Items 1, 4, 5, 6,
  8, 2a, B confirm in one keystroke each. Items A and Item C
  (acceptance part) become a single sign-off pass — the iterate-to-Plan
  sub-edit for Item A, the accept-with-deviation for Item C.
- Item C's *process delta* — the spec-template mechanism observation —
  is jotted into the Item 3 SUMMARY.md §10 as an Act candidate. It
  sits there frozen until the next L4 Act review collects it across
  whatever other bundles surfaced similar observations.

The driver does not collapse three turns into one — the iterate-to-Plan
edge is irreducible. What it does collapse is the *bookkeeping*: which
items are awaiting what, which dispositions are conditional on which
dispatch runs, which §10 observations are awaiting Act review. The
cycle's shape is preserved; only the friction is removed.

## Parallel example — a design-shaped Plan (GEPS 049)

The CI-hardening cycle above is a **brief-shaped Plan**: one bullet
list of seven items, each a one-fix scope. For the design-shaped end
of Plan's range
([[01 - The Quality Cycle]] §Solution-approach design), GEPS 049 —
*Versioned Addon API surface and 2 axis lifecycle model* — is the
contrast.

**Caveat on framing.** GEPS 049 was authored as an upstream Gramps
wiki proposal in its project's normal proposal workflow; it was not
generated *by* this cycle. It is retrofitted here as an **illustration
of the shape** a design-shaped Plan takes — same beat (Plan), same
role (a human author), same output type (a contribution spec) — at a
scope that spans many implementation cycles. Use it for the section
structure (Goals, Non-goals, Decomposition, Migration, Objections-
and-responses, Impact assessment, De-risking, Open questions, Future
Work) and the Plan-internal grounding investigation, *not* as evidence
this cycle produces GEPS-shaped artifacts.

What makes GEPS 049 a *design-shaped* Plan rather than a brief:

- **Coordinated multi-part scope.** Four coupled parts (API surface,
  lifecycle states, repository structure, dependency declarations).
  Each part is independently landable, but their composition matters
  — the "single-sourcing story" only works when all four cooperate.
  No single `brief.md` would correctly spec this; the per-part briefs
  derive from the GEPS, not the other way around.
- **Phased migration with safe stall points.** Four phases (1
  Foundations, 2 API version, 3 Lifecycle states, 4 Repository
  consolidation). Each prefix of phases leaves the ecosystem strictly
  better than the status quo. If the work stops at any phase
  boundary, no rollback is needed — that's the safe-stall property
  Plan-as-design buys.
- **Goals / Non-goals explicit.** Seven goals, four non-goals
  ("**Not** replacing Gramps's existing major/feature/maintenance
  versioning scheme with semver. … **Not** silently auto-migrating
  user data"). The non-goals do real work: they bound what later Do
  beats may attempt against this design.
- **Terminology and scope.** A dedicated section disambiguating
  "addon" vs "plugin" so the rest of the proposal can use the terms
  precisely. Plan-time vocabulary control.
- **Objections and responses (anticipated Check).** Two named
  objections from review (Kulath, Nick Hall) carried forward in the
  proposal body with explicit responses — the Plan-time anticipation
  of Check's later judgments. Documented opposition that has been
  weighed reads differently from opposition that has been ignored.
- **Impact assessment (anticipated validation).** A frank
  user-experience-vs-addon-quality reading where the honest
  conclusion is "trade-off, not clear win" — Plan stress-testing its
  own fitness-to-purpose ahead of Check.
- **De-risking section.** Five concrete mitigations (sequencing, CI
  as checklist, addon-author friction, UI complexity, field
  staleness) — Plan addressing the failure modes it can foresee.
- **Open questions.** Seven items Plan explicitly could not resolve,
  flagged for the review cycle on the proposal itself. The Plan-side
  analogue of `SUMMARY.md` §6 NEEDS-HUMAN, written ex-ante.
- **Future Work.** Seven items that this design *enables* but does
  not include (Part 5 state migration, JSON registration, DBAPI,
  developer tooling, supersedes-built-in, Addon Manager enhancements,
  governance). Plan also says what is *not* in the next several
  cycles.
- **Plan-internal grounding investigation.** The "Versioning scheme"
  section cites a griffe analysis run across the existing Gramps
  release history — a scoped, Do-shape sub-investigation done *in
  service of* Plan, whose empirical output (0 breakages in 6.0.0→6.0.4
  maintenance; 224 across the 5.x→6.x major bump) grounds the
  proposal's recommendation. The "Reference Implementation" section
  notes this is one of two parts with working code today; the rest is
  specified-but-not-built.
- **The proposal's own review cycle.** "Status: Draft — under review.
  Background discussion at Discourse thread 9491 and GitHub Discussion
  #2297. Current review thread for this proposal: GitHub Discussion
  #2311." The proposal has draft/under-review/accepted states of its
  own, and a dedicated "Review discussion and open questions" section
  consolidating the iterate-within-Plan history. Distinct from the
  iterate-to-Plan path in a per-contribution cycle: this is Plan
  iterating on *the design*, before any child brief is authored.

What the two examples share, despite the scale difference:

- **The human owns Plan.** GEPS 049's authorship — "Eduard Ralph
  (eduralph) — proposal, specification, and analysis. Claude
  (Anthropic) — drafting, structural editing, and the griffe
  API-stability analysis" — mirrors the CI-hardening cycle's: the
  validation-first judgment is yours; the model assists with
  drafting and grounding investigations. Plan's irreducible step is
  the same at both scales.
- **STOP discipline through to Check sign-off.** The GEPS is "Draft
  — under review"; no implementation merges until the proposal is
  accepted and child briefs run their cycles. The CI-hardening
  brief's STOP discipline — push and draft-PR-open MAY happen during
  the cycle (CI feedback, work-in-progress visibility); ready-mark
  MUST NOT happen before Check sign-off — is the same discipline at
  smaller scope.
- **Downstream beats unchanged.** Each phase of GEPS 049 will, at
  implementation time, spawn one or more `brief.md`-scale child
  cycles; each child cycle runs through Do, Check (gates + reviewer
  + sign-off), and contributes to the next Act review like any other
  cycle. The cycle's machinery is one machine, fed by either Plan
  shape.

**The lesson the contrast carries:** Plan's range is wider than the
"author a brief.md" framing first suggests. The model is the same;
the artifact stretches to fit the work. When a contribution is one
fix, Plan is one brief. When a contribution is a design with phased
implementation, Plan is a design proposal that spawns N briefs. Same
beat, same role, different stationery.

## See also

- The three source briefs (CI hardening, brief-shaped Plan), preserved
  verbatim:
  - `~/Downloads/Folds2/CLAUDE_CODE_BRIEF-ci-hardening.md` (v1)
  - `~/Downloads/Folds2/CLAUDE_CODE_BRIEF-ci-hardening-v2.md` (v2)
  - `~/Downloads/Folds2/CLAUDE_CODE_BRIEF-ci-decisions.md` (v3)
- The CI substrate this cycle modified: `~/Downloads/Folds2/02b-ci-workflows.md`.
- GEPS 049 (design-shaped Plan):
  `~/Downloads/GEPS 049_ Versioned Addon API surface and 2 axis lifecyle model - Gramps.pdf`
  and its live source at
  https://gramps-project.org/wiki/index.php/GEPS_049:_Versioned_Addon_API_surface_and_2_axis_lifecyle_model
- The model — [[01 - The Quality Cycle]], [[02 - Cycle Artifacts]],
  [[03 - Cycle Automation]], [[04 - Validation Tooling]].
