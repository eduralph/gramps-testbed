---
title: "The Quality Cycle (PDCA)"
categories: []
managed: false
status: active
---

> The top-level model. It sits above [[02 - Cycle Artifacts]] (the
> operational layer) and [[04 - Validation Tooling]] (the tier × home
> decomposition), and explains why those exist, how they connect, and
> who owns each part. Living document.

# The model in one line

One contribution turns one PDCA cycle: **Plan** (author the spec) →
**Do** (implement) → **Check** (verify the built artifact against the
spec — correctness, conformance, *and* validation) → **Act** (process
improvement: adjust the spec template, ruleset, or workflow so the
issues this cycle exposed do not recur) → back to **Plan** with a
better baseline.

```
         ┌─── Act: adjust the PROCESS (spec template, ruleset, ──┐
         │      workflow) so this class of issue does not recur  │
         ▼                                                        │
   PLAN  ── author the spec for this contribution ──── you        │
         │                                                        │
         ▼                                                        │
   DO    ── implement the fix ────────────── builder              │
         │                                                        │
         ▼                                                        │
   CHECK ── verify the built artifact against the spec:           │
            • correctness (5-step chain)                          │
            • conformance (5-tier stack)                          │
            • validation  (1 indivisible act — fitness-to-purpose)│
            verdict on THIS contribution: ship / close / iterate  │
         │                                                        │
         ▼                                                        │
   ACT   ── inspect what Do and Check exposed about the           │
            PROCESS itself; modify spec template, ruleset,        │
            agent skills, gates so the cycle returns to Plan      │
            with a better baseline ────────────── you ────────────┘
```

Two beats own *the contribution*: **Do** builds it, **Check** decides
whether to ship/close/iterate it. Two beats own *the process*: **Plan**
draws from the current process baseline to spec this contribution, and
**Act** reviews what this cycle revealed about the process baseline and
adjusts it. The next Plan starts from Act's adjusted baseline.

**Work in the next Do phase should not recreate the issues identified
in this Act.** If it does, the Act was not effective.

## The four beats are the four roles

PDCA earns its place here because it is not decoration over the
architecture — it *is* the role partition. Each beat is a single kind
of work with a single owner:

| Beat | Activity | Owner | Subject |
|---|---|---|---|
| **Plan** | author the spec for this contribution; triage (repro-or-close, scope, success criterion) | **you** | the contribution |
| **Do** | implement the fix — production only | **builder** (e.g. Claude Code) | the contribution |
| **Check** | run the correctness chain, the conformance stack, and the validation act against the built artifact | **deterministic gates + advisory reviewer + human sign-off** | the contribution |
| **Act** | inspect what Do and Check exposed about the PROCESS; modify the spec template, ruleset, gates, or agent skills so the next cycle starts from a better baseline | **you** | the process |

Two role-axis observations the table makes explicit:

1. **Plan and Act are both yours, but they are not the same act.** Plan
   draws from the process baseline to write a contribution-level spec
   (forward-looking, contribution-subject). Act looks back at the
   completed cycle and edits the process baseline itself (backward-
   looking, process-subject). They share an owner because both require
   the kind of judgment no oracle holds, but their **subjects differ**.
2. **Check is where the contribution is adjudicated.** Validation —
   *is this the right thing* — is part of Check, not a separate beat.
   The reviewer participates in all of Check, advisory; the human
   completes Check by clearing what neither gates nor reviewer could
   decide.

## Contribution work vs process work

The line between the cycle's two halves matters because the work and
the questions are different on each side:

- **Plan + Do + Check** operate on **the contribution**: this bug, this
  fix, this artifact. The questions are: what should be built, build
  it, did it work.
- **Act** operates on **the process**: this ruleset, this spec
  template, this workflow, these gates. The question is: what did this
  cycle reveal about the system that produced it, and what should
  change so the next cycle is better.

That seam is what keeps Act focused. Act is **not** a re-vote on
whether this contribution should ship — Check decided that. Act is the
audit on what the cycle's record (the bug report, the builder's
rationale, the reviewer's findings, the deterministic gate output, the
human sign-off) shows about the *process*: a rule that should be
written down, a gate that should be added, a spec-template field that
turned out to be ambiguous, an agent skill that needs sharpening, a
wontfix policy that needs adjusting.

When Check fails and the contribution needs another attempt, that
iteration goes back to **Do** (rebuild) or **Plan** (re-spec) — it is
not an Act. Act fires once per completed cycle and asks one question:
did we learn anything here that should change the baseline?

## The advisory reviewer's permission boundary

An advisory reviewer (different model family, decorrelated by file
withholding — see [[02 - Cycle Artifacts]]) is permitted **everything
inside Check**, advisory: it may opine on correctness causal-adequacy,
on conformance Tier-5 scope judgment, and on validation fitness-to-
purpose. It re-runs evidence and grounds citations; it produces per-
item `PASS / FAIL / NEEDS-HUMAN`. It does not gate — deterministic gates
do that — and it does not write the fix.

The reviewer is **not** permitted inside Act. Process improvement —
what rule to add, which spec-template field to revise, whether to
retire a check — is yours. The reviewer evaluates this contribution
against this spec; you decide whether the spec and ruleset themselves
need adjusting.

# The model in detail
## Plan - detailed steps

Plan's job is to convert *a problem report into a contribution spec*.
Its input is the **current process baseline** (the `brief.md` template,
the conformance ruleset, the branch-target rules, the agent skill
files — all maintained by Act); its output is one filled `brief.md`
ready to hand to Do. Everything in Plan is human work the agent-work
scaffolding can draft but not finish.

**Triage — repro-or-close, is it worth doing.** The first question is
not *how do we fix this* but *is there a defect at all, and is the cost
of fixing it justified*. Reproduce against the canonical fixture on
the target branch; if the report doesn't repro, close the cycle here
with a confirm-and-close disposition rather than handing Do an
unfounded spec. (Closed-without-fix is a successful PDCA cycle outcome,
not a failure: Plan asked "is this worth doing" and answered "no".)

**Spec authoring — what "fixed" means.** When the cycle does proceed,
Plan writes the spec Check will later measure against. Every required
field (defect, success criterion, branch target, scope-and-out-of-
scope, repro instruction, test requirement, citations expected, STOP
discipline, disposition hint) maps to a question Check, Do, or Act
will subsequently rely on. The success criterion is the
load-bearing field: it is *the* sentence "did this work" tests
against, and a vague success criterion makes Check unable to
adjudicate. Plan is where the irreducibly-human decisions get made
ahead of time — what to build, what shape it should take, what counts
as done — so Do and Check have something concrete to operate on.

**Disposition hint, not verdict.** Plan may guess at the eventual
disposition (POSSIBLY-FIXED → verify first; likely-fix; likely-close),
but the guess is a hint to Do/Check, not a binding. If Do or Check
finds evidence overturning the hint, the hint loses. Hints save time
on the common cases without short-circuiting evidence on the
uncommon ones.

**STOP discipline.** Plan's output goes to Do as a draft. *Pushing to
feature/draft branches and opening draft PRs MAY happen at any point
during the cycle* — both are useful for triggering CI gates and
surfacing work-in-progress. *What MUST NOT happen before Check sign-off
accepts is the ready-mark* (the explicit "this is ready to merge"
signal). The discipline is named in Plan because Plan is where the
contract with the human (sign-off is yours, irreducibly) is established
for this cycle. Operationally the ready-mark constraint is enforced by
tool scope in Do; see [[02 - Cycle Artifacts]] §PLAN for the per-field
detail and Do's subagent-scope mechanism.

### Solution-approach design (when the spec is more than one fix)

Not every contribution is one fix. Sometimes the right Plan output is
a **design proposal** — a multi-part architectural design with phased
sequencing, scope discipline, anticipated objections, and an explicit
list of what it does *not* attempt. The `brief.md` shape collapses;
the spec grows substructure of its own.

This is still Plan: same beat, same human authorship, same
validation-first judgment. The difference is *scope*. A brief specs
one fix that Do will implement in one patch; a design proposal specs a
coordinated set of changes, each of which will later spawn its own
`brief.md`-scale cycle. **One Plan, many child cycles.** The design
proposal is the meta-spec the child briefs derive from.

A design-proposal-shaped Plan typically grows sections a
one-contribution brief does not need:

- **Goals / Non-goals.** Explicit forward-looking commitments and
  explicit forward-looking refusals. Non-goals do real work: they
  prevent scope drift in the Do/Check beats that later run against
  this design.
- **Terminology and scope.** The vocabulary the rest of the proposal
  relies on, named once so downstream consumers do not improvise.
- **Decomposition into independently-landable parts.** Each part
  ships value alone; rejecting or deferring a part leaves a coherent
  intermediate state. This is the same anti-bundle discipline that
  "one logical fix per PR" enforces at brief.md scale, applied at
  design scale.
- **Migration / phased rollout with safe stall points.** Sequencing
  such that any prefix of phases leaves the system strictly better
  than the status quo. If the work runs out of bandwidth, the
  intermediate state still ships value.
- **Objections and responses.** Plan-time anticipation of Check's
  later judgments. This *does not* replace Check (which evaluates a
  built artifact); it sharpens the spec by stress-testing it before
  Do begins. Documented opposition that has been weighed reads
  differently from opposition that has been ignored, and the
  difference shows up at Check sign-off.
- **Impact assessment.** Plan-time anticipation of the validation act
  Check will later perform: is this the right thing to do at all,
  given what it costs users, authors, maintainers? The honest answer
  often has "trade-off, not clear win" in it.
- **De-risking.** Concrete mitigations for the cross-cutting risks
  Plan identifies. Often shaped as "if this fails, what does failure
  look like, and what catches it."
- **Open questions.** Items Plan honestly could not resolve, marked
  for the review cycle on the proposal itself, or deferred to a
  later turn. Plan's ex-ante analogue of `SUMMARY.md` §6
  NEEDS-HUMAN.
- **Future Work.** What this design *enables* but does not include.
  Boundary maintenance: a Plan also says what is *not* the work of
  the next several cycles.

**Plan-internal grounding investigations.** A design-proposal-shaped
Plan can spawn small, scoped Do-shape sub-investigations whose output
feeds back into the spec — a measurement, an audit, an analysis run
to ground a recommendation in evidence before the main Do begins.
These are Do-shape work in service of Plan; their output is data the
spec consumes, not a contribution the cycle ships. They keep Plan
honest by making "I think this is true" into "I measured it."

**The design proposal has its own review cycle.** Before any child
brief is authored, the proposal goes through review (a discussion
thread, draft status, reviewer feedback, consensus). That review is
*iterate-within-Plan* — analogous to the iterate-to-Plan path inside
a per-contribution cycle ([[02 - Cycle Artifacts]] §9), but operating
on the design rather than on a single brief. The proposal's draft /
under-review / accepted state is itself a Plan-internal lifecycle.

**Illustration of the shape.** GEPS 049 (*Versioned Addon API surface
and 2 axis lifecycle model*) is a useful **illustration** of what a
design-shaped Plan looks like — not evidence this cycle *produced*
it. The GEPS was authored as an upstream Gramps wiki proposal in its
project's normal proposal workflow, then retrofitted here as a
worked-example contrast to the brief-shaped Plan in
[[07 - Case Study - CI Hardening]]. Read it for the section structure (Goals /
Non-goals; Terminology and scope; Objections-and-responses; Impact
assessment; De-risking; Open questions; Future Work; Reference
Implementation; Review discussion) — that *is* the shape a
design-shaped Plan takes when this cycle authors one. The
"Reference Implementation" section in particular illustrates
**Plan-internal grounding investigations**: a scoped griffe analysis
was run to produce the empirical breakage counts that ground the
proposal's recommendation, before the main Do begins. Each part and
each phase, *if* this cycle adopted the proposal, would spawn its own
`brief.md`-scale child cycle.

The brief-vs-design distinction is not a bright line. Most cycles are
brief.md-sized; some are GEPS-sized; the boundary is "how many
coordinated Do/Check turns does this need." When in doubt, start with
a brief; promote to a design proposal if Plan-internal iteration
reveals coordination Do cannot resolve alone.

### What Plan inherits from Act

Plan does not start from nothing each cycle. Its template, ruleset,
branch-target rules, and the agent skills it relies on are the
**output of every prior Act**. The closing edge of the PDCA diagram —
*Act → back to Plan with a better baseline* — is literal: the
`brief.md` template Plan fills today is exactly the version Act last
adjusted, and any spec-template ambiguity Act resolved last batch is
the ambiguity Plan does not have to navigate this cycle. Plan's
quality is bounded above by the quality of the baseline Act maintains
for it.

## Do - detailed steps

Do is the single beat in the cycle that does *production work only* —
it builds the change the brief specs, ships the test, and stops.
Nothing in Do adjudicates, defends, or evaluates the change; those
roles belong to Check. The clean separation is what lets the cycle's
control flow stay deterministic: Do produces an artifact, Check
decides about it, and the decision never feeds back into the
production step within the same beat.

**Input — `brief.md` only.** Do reads the spec, the success criterion,
the scope-and-out-of-scope, the repro instruction, the test
requirement, and the STOP discipline. It does not read prior cycles'
records, the conformance ruleset (which Check applies, not Do), or the
project's broader context beyond what the brief cites. This narrow
input is deliberate: it keeps Do focused on *this contribution* and
lets Check's later evaluation rest on whether the build actually
matches the brief.

**Output — three files, in lockstep.** `patch.diff` is the change
itself; the *test* (at the location the brief named) is shipped in the
same change and must fail pre-fix, pass post-fix; `build-notes.md`
records the builder's rationale — why this change, what was tried,
what was ruled out. The three are produced together: a patch without
its test, or a build without its rationale, fails the brief's
requirements before Check even runs.

**STOP discipline — mechanical, not asked nicely.** Do MAY push to
feature/draft branches and MAY open draft PRs (both useful for letting
CI gates run on the actual artifact and for surfacing the
work-in-progress). Do has **no ready-mark capability**. The ready-mark
constraint is enforced by **tool scope** on the builder subagent
(`.claude/agents/`), not by instruction — the model can push commits
and open draft PRs but cannot transition a PR out of draft state.
Anything in the brief that would require *marking the PR ready* is a
brief defect (or a Check-sign-off step), not a builder permission to
expand.

**`build-notes.md` is for the human signing off Check, not the
reviewer.** This is the first appearance of the **independence
contract** (developed in [[02 - Cycle Artifacts]] §Independence
contract and enforced operationally by the driver in
[[03 - Cycle Automation]] §Independence is enforced by the
orchestrator): the builder's framing of *why* the change is correct
must not anchor the advisory reviewer who later evaluates whether the
change *is* correct. So `build-notes.md` is withheld from the reviewer
by the driver's file-input list. The human signing off Check sees it
alongside the reviewer's independent verdict; the reviewer never does.

## Check - The inner anatomy: 5 / 5 / 1

PDCA names the four beats and the loop; it says nothing about the
shape *inside* each beat. The Check beat has internal structure — the
5 / 5 / 1 — and that is where the deterministic-vs-human boundary
sits.

**Correctness — five steps, a chain.** Spec → reproduction → change →
verification → causal adequacy. Ordered and dependent: you cannot
verify without a reproduction, cannot reproduce without a spec. The
spec (step 1) is the hinge artifact — authored in Plan, consumed here.
Answers *is it right*; "right" is always relative to the spec.

**Conformance — five tiers, a stack.** Structure → shape → runtime →
contribution → judgment. *Not* a chain: independent layers checked in
parallel, not prerequisites of one another. Tier 1 passing does not
gate Tier 3. Answers *is it well-formed*. "Tiers" is exact; "steps"
would be wrong. (See [[04 - Validation Tooling]] for tier × home
decomposition.)

**Validation — one act, singular.** Is this the right thing to do at
all (given the spec, given the bug report, given everything the cycle
has produced)? It does not decompose into five of anything, and that is
the point: judgment of fitness-to-purpose is not a checklist, so it
stays indivisible while the checkable stages break apart. The "1" is
load-bearing — it marks the irreducible. In contribution-terms, this
is "ship this fix / close as wontfix / iterate".

| Stage (within Check) | Shape | Count | Structure | Answers | Owner |
|---|---|---|---|---|---|
| Correctness | chain | 5 steps | ordered, dependent | is it right | gates + advisory |
| Conformance | stack | 5 tiers | independent layers | is it well-formed | deterministic gates |
| Validation | act | 1 | indivisible | is it the right thing | advisory + human sign-off |

All three stages produce their evidence inside Check. The human's
Check-completion step (clearing NEEDS-HUMAN, accepting the verdict on
the contribution) closes Check and hands off to Act.

Do carries no 5/5/1 number because it is production, not evaluation.
Plan and Act carry no 5/5/1 number because they operate on the
*process* shape, which has its own (slower) structure. The 5/5/1 *is*
the deterministic-vs-human boundary inside the contribution-evaluation
beat.

**On the symmetry — don't over-lean on it.** The "5 / 5 / 1" pattern
is partly mnemonic, not load-bearing taxonomy:

- *Correctness is a 5-step chain* as written, but step 1 (Spec) and
  step 3 (Change) are **inputs** to Check from Plan and Do, not work
  Check performs. As performed *inside* Check, correctness is 3 steps
  (reproduction → verification → causal adequacy) plus two inputs.
  See [[04 - Validation Tooling]]'s observation #1 on the same point.
- *Correctness step 5 (causal adequacy), Conformance Tier 5
  (judgment), and the Validation act* all resolve to the same place:
  advisory reviewer + human sign-off ([[04 - Validation Tooling]]
  matrix collapses these into one judgment cell). Three labels, one
  judgment act.

The numbers are useful as scaffolding for teaching — they name where
the stages break apart and where they don't — but treat the symmetry
as a presentation choice, not a deep claim about Check's shape.

### Where the stages touch, and where they collapse

**Two touch-points only, both in Check.**

1. *The test suite does double duty.* Running it is Tier-3
   **conformance** ("declared runtime resolves, headless run works");
   what it proves about behavior is **correctness** ("existing behavior
   preserved"). One instrument, two readings.
2. *Judgment sits at the top of every Check stage* — correctness
   causal-adequacy, conformance Tier-5, and the validation act itself.
   All three go to the advisory reviewer (annotation) and to the human
   (final sign-off). The reviewer never gates; the human never edits
   the fix at Check time.

**The collapse rule.** For a *conformance-defect* fix (a missing
`tests/__init__.py`, a banned import), correctness reduces to
conformance: the conformance check *is* the oracle, "correct" just
means "the check now passes," no behavioral spec needed. For a
*behavioral-defect* fix, correctness is fully independent and needs
its own evidence chain. Validation is independent in both cases: even
a clean conformance pass can be the wrong fix.

### The oracle principle (cross-cutting, inside Check)

Every Check claim is only as strong as the oracle that decided it. A
green test proves correctness *of the path it exercises* — nothing
more. Oracle hierarchy, strongest to weakest: a conformance check
(decides a rule), a written test (only as strong as its coverage), the
existing suite (catches regressions in *covered* behavior only), human
or advisory-LLM judgment (last resort). "A green check is evidence of
that narrow check, not of correctness" is a statement about this
principle — and a reminder that passing the gates is not the same as
passing validation.

## Act - detailed steps

Act's input is **the cycle's record** — `brief.md`, `patch.diff`,
`build-notes.md`, `check-gates.json`, `check-review.md`, the completed
`SUMMARY.md` (see [[02 - Cycle Artifacts]]). Its output is **deltas to
the process baseline**:

- **Spec-template deltas.** A field in `brief.md` that turned out to be
  ambiguous, missing, or systematically misread. The next Plan uses the
  improved template.
- **Ruleset deltas.** A rule in the conformance ruleset that should be
  added, retired, relaxed, or tightened — based on what this cycle
  exposed. ("This rule fired on a false positive that wasted Do time"
  → relax. "This bug class wasn't caught by any tier" → add a rule.)
- **Gate deltas.** A check that should be added to Tiers 1–4, or
  promoted from advisory to gating, or moved between homes (see
  [[04 - Validation Tooling]]).
- **Agent-skill deltas.** A pattern the builder or reviewer repeatedly
  got wrong — refined into the `SKILL.md` / `AGENTS.md`.
- **Workflow / orchestration deltas.** A state the driver should have
  surfaced earlier, an Act-queue ordering issue, an independence-
  contract gap.

What Act does **not** do:

- Re-decide the contribution's disposition. Check did that.
- Run the validator or the suite. Check did that.
- Author the next contribution's spec. The *next* Plan does that, with
  Act's improved baseline as its starting point.

Act is most useful when **batched** — process improvements made one
cycle at a time can be noisy and reactive. Reviewing N cycles' records
together surfaces patterns ("three of these bugs share a root cause we
have no rule for") that any single cycle would miss. The cycle's
records are stable on-disk artifacts (see
[[02 - Cycle Artifacts]] §Bundle layout) precisely so Act can look
across many of them.

### When effectiveness is judged

The honest test of an Act is whether the next Do phase recreates the
issue this Act tried to eliminate. If a Plan/Do/Check sequence in a
subsequent cycle hits the same problem, the Act was not effective —
the rule wasn't strong enough, the spec-template change didn't
address the real ambiguity, the gate wasn't in the right place. That
discovery is itself an input to the next Act, and the wheel turns
again with a sharper question.

This is why Act is *the* process-improvement beat and not a per-
contribution decision: its value compounds across cycles, and its
quality is measured against cycles that come after it.

# Per repo (worked example)

In the Gramps testbed both `gramps` and `addons-source` owe the full
cycle — the same spec authoring, the same Check stages, the same
process-improvement Act. What differs is **maturity**, not structure:
`addons-source` has a written conformance ruleset (addon-dev guidelines)
and started its tooling; `gramps` core has conformance tooling (the
analyzers) enforcing rules nobody has written down yet, and a Tier-3
surface partly running but not yet gated. The cycle is the same; the
cells are filled to different depths, and each Act has different
process-debt to chip away at. This pattern generalizes — most projects
start with one repo/area further along than the others.

# How this maps to neighboring docs

- The contribution-side beats (Plan, Do, Check) — operational
  expression in [[02 - Cycle Artifacts]] (`brief.md`, `patch.diff`,
  `check-gates`, `check-review.md`, the nine-section `SUMMARY.md`).
- The conformance stack (5 tiers in Check) — tier × home
  decomposition in [[04 - Validation Tooling]].
- The mechanical components (Do, plus Check's gates and reviewer)
  automated; Plan, Check's sign-off step, and Act preserved as the
  three human touch points — the driver in [[03 - Cycle Automation]].
- A worked end-to-end example — [[07 - Case Study - CI Hardening]].

# On the vocabulary

PDCA (the Deming/Shewhart wheel) is adopted as the outer cycle because
it is load-bearing, not gravitas: its four beats name the contribution
half (Plan, Do, Check) and the process half (Act), and the return-to-
Plan edge carries the improved baseline forward. Act's standard name in
some PDCA literature is "Adjust" precisely because the act is to modify
the process, not to revisit the just-completed contribution. What PDCA
does *not* carry is the inner anatomy of Check — it is silent on why
correctness is an ordered 5-step chain, conformance an independent
5-tier stack, validation singular. So PDCA and the 5/5/1 compose: PDCA
is the macro rhythm and the role assignment; 5/5/1 is the micro shape
inside Check, and the marker of the deterministic/human boundary.
Other borrowed terms keep their standard meaning: *correctness* spec-
relative (formal methods), *oracle* (the test-oracle problem),
*conformance* (conformance-to-a-standard), *verification vs.
validation* (build-it-right / build-the-right-thing — both poles live
in Check; Act is downstream of both). Local to this model: the five
conformance tiers (sorted from rule mechanism — see
[[04 - Validation Tooling]]) and the correctness-chain naming.
