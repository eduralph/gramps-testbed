---
title: "Cycle Automation (orchestration layer)"
categories: []
managed: false
status: active
---

> One level below [[02 - Cycle Artifacts]]. How the PDCA cycle runs as a pipeline. Core principle: **automate where the work is mechanical (Do, plus Check's gates and reviewer), instrument where the work is human (Plan, Check's sign-off step, Act), never automate the human work away.** The pipeline runs unattended from the brief to the sign-off queue (where Check stops for the human) and resumes only when the human signs off Check; Act fires later, on a cadence, across batches of completed cycles. Living document.

> **Maturity legend** — every major mechanism in this doc is tagged: **[built]** = exists and runs today; **[partial]** = some pieces implemented, others not (cells in [[04 - Validation Tooling]] §Status today have the breakdown); **[planned]** = designed only, no implementation yet. The pipeline as a whole is currently around L1 (scripted handoff) — see [[#Maturity ladder]]; the L2/L3 driver, the single-sourced gate runner, the headless reviewer, the sign-off queue, and the Act-log tooling are all **[planned]** at time of writing. The agent-work scaffolding (`agent-work/run-batch.sh`, `agent-work/scripts/make_handoff.py`, templates under `agent-work/templates/`) is **[built]** — it is what runs today.

## What can and cannot be automated

PDCA has four beats; automation is described per beat. Where a beat has internal components that automate at different levels, the Automation column names each.

| Beat | Owner ([[01 - The Quality Cycle]]) | Automation | Maturity | Cadence |
|---|---|---|---|---|
| Plan | human | **instrumented** — agent-work scaffolding produces brief drafts; the human authors the spec/verdict | scaffolder **[built]**; human step is the design | per cycle |
| Do | builder | **full** — headless agent (e.g. `claude -p`), builder subagent scope | builder subagent config **[planned]**; runs today by hand-invoking Claude Code | per cycle |
| Check | deterministic gates + advisory reviewer + human sign-off | mixed — **gates: full** (deterministic, unattended); **reviewer: full** (headless, advisory); **sign-off: instrumented** (result document + one-command capture, human completes Check) | gates **[partial]** (see [[04 - Validation Tooling]] Status-today column: T3 most mature, T1 partly upstream, T2 not yet written, T4 greenfield); reviewer **[planned]**; sign-off queue **[planned]** | per cycle |
| Act | human | **instrumented** — process-baseline tooling (template diff, rule-add scaffold, act-log generator) | tooling **[planned]** (L4); manual Act fine indefinitely | **cross-cycle**, batched |

**Human touch points vs beats.** Four rows, four beats — but the human appears at three different places, not four. The three **human touch points** in the cycle are *Plan-authoring*, *Check sign-off*, and *Act* — but these are *not* three beats. Plan and Act are two fully-human beats; Check sign-off is the human-instrumented *step inside* the Check beat (Check's gates and reviewer run unattended; sign-off is the human completion). Do is the fourth beat and has no human touch point. The 4-beat structure is preserved; the three human touches are how humans participate across the three beats that contain human work. The pipeline's job is to make each human touch **rare** (only genuine NEEDS-HUMAN items reach sign-off; Act fires once per batch, not once per cycle) and **fast** (everything pre-assembled, the common confirm-and-close is one keystroke).

The crucial cadence split: **Plan and Check (including sign-off) are per-cycle** (one of each per contribution); **Act is per-batch** (one Act review covers many cycles). The driver's state machine only carries the per-cycle work; Act runs as a separate process.

## The orchestrator is a state machine over the per-cycle bundle

> **Maturity: [planned].** The driver described in this section is the design for L2/L3 of the [[#Maturity ladder]]. Today the cycle runs at L1 (scripted handoff): the `run-batch.sh` + `make_handoff.py` scaffolding **[built]** produces the per-issue bundle directories and the brief drafts, but the per-beat advancement is hand-driven — no `state()` / `advance()` loop runs unattended yet.

Do not build a monolith. Each issue's **state is its files** in `results/issue_<id>/`, and a driver advances issues idempotently:

```
(no bundle)        →  PLAN   →  brief.md present
brief.md           →  DO     →  patch.diff + test + build-notes.md present
patch.diff         →  CHECK  →  check-gates + check-review + SUMMARY.md present
SUMMARY.md         →  (AWAITING_SIGNOFF)  ← pipeline STOPS here
SUMMARY.md §9 set  →  sign-off applied:
                       accept           → cycle COMPLETE  (frozen bundle)
                       iterate-to-Do    → driver clears every Do+Check
                                          artifact; state ← PLANNED
                                          (re-run Do against same brief)
                       iterate-to-Plan  → driver versions brief.md →
                                          brief.vN.md and clears every
                                          downstream artifact; state ←
                                          UNPLANNED (human authors a
                                          new brief.md, then Do re-runs)
```

The driver stops the issue at AWAITING_SIGNOFF every time — including on iteration. After sign-off, an accepted bundle is **frozen**: it becomes input for the *next* Act review (a separate, cross-cycle pass — see below).

Properties this buys, cheaply:

- **Resumable.** A crash mid-batch resumes from file state; nothing re-runs that already produced its artifact.
- **No-clobber, with a named exception.** Idempotent `advance` never destroys an artifact it already produced or a verdict already filled. The iterate transitions are a **deliberate clear**, not an idempotency violation: they unlink everything downstream of the re-entry point so a rebuild starts from clean state. Brief versions are *preserved* on iterate-to-Plan (renamed to `brief.vN.md`); see the case study's CLAUDE_CODE_BRIEF v1/v2/v3 sequence for the precedent the skeleton matches.
- **Inspectable.** "What state is issue N in" is a directory listing, not a database.

The driver is a thin loop: for each issue, look at which files exist, run the next beat's command, write its artifact, advance. Stop the issue when it reaches AWAITING_SIGNOFF.

## Per-beat automation

### Plan — instrumented (agent-work scaffolding + human)

Reuse an existing scrape / handoff pipeline as the Plan scaffolder (scrape → emit a `brief.md` with a TRIAGE VERDICT scaffold and auto-flags), drawn from the **current process-baseline spec template** that Act maintains. That *is* the draft `brief.md`. The human fills the spec + success criterion + resolved branch target and confirms/overrides the disposition hint. Automated: everything except the judgment. Not automated: the judgment.

### Do — full (headless builder, subagent scope)

Driver invokes the builder agent non-interactively with `brief.md` as input, builder subagent scope (read repos, write patch+test, MAY push to feature/draft branches, MAY open draft PRs, **MUST NOT mark a PR ready**). Output: `patch.diff`, the test, `build-notes.md`. Pushing and draft-PR-open are allowed because they let CI exercise the artifact during the cycle without bypassing the sign-off gate.

**The ready-mark mechanism — designed, not yet implemented.** The intended enforcement is subcommand-level Bash allowlists in the builder subagent's config (`.claude/agents/builder.md` or equivalent): allow `Bash(gh pr create:*)` and `Bash(git push:*)`, deny `Bash(gh pr ready:*)` and `Bash(gh pr merge:*)`. Subcommand-level allowlists *are* supported by Claude Code's permission system (verified against the testbed's current `settings.json`), so the mechanism is feasible. The `.claude/agents/` files that would instantiate it for this project **have not been built yet** (see F1-style maturity tagging — the builder subagent is *planned*, not *built*). Until those files exist, the ready-mark constraint relies on the builder respecting the brief's STOP discipline, not on a mechanical block. The pipeline-mode L2/L3 ladder ([[#Maturity ladder]]) treats this honestly: until the subagent config is in place, the "mechanical enforcement" claim is downgraded to "asked of the builder via the brief; verified by sign-off."

### Check — mixed (gates full, reviewer full, sign-off instrumented)

Check is one beat with three components, each automating at a different level. Components run in order; the blocking logic across all three is **100% deterministic** — no LLM in the gating path.

**1. Deterministic gates → `check-gates.json` (full).** The same checks that run in CI, run locally: the correctness re-runs (repro red / verify green / regression suite) + conformance Tiers 1–4 (structural validator, semgrep, find_spec/runtime, commit-msg + branch-target + version-bump). Each emits pass/fail + rule ID + oracle + path:line. A FAIL with auto-fixable cause (lint/format/genuinely-red) is auto-fixed and re-run; a FAIL needing a decision goes to NEEDS-HUMAN.

**2. Cross-vendor reviewer → `check-review.md` (full).** Different-vendor model (e.g. `codex`) headless, fed `{patch, test, brief, check-gates}` — **not** `build-notes.md`. **Implements** the judgment cells C5 / T5 / validation act: re-runs the asserted evidence (stash→red, unstash→green), re-checks cited path:lines ground, emits per-item `PASS/FAIL/NEEDS-HUMAN`. Emits `NEEDS-HUMAN` *by design* on the structurally-undecidable items enumerated in [[04 - Validation Tooling]] §Inside the judgment cell (validation fitness-to-purpose, contested symptom-vs-root-cause, semantic upstream-isn't-ahead, scope-creep / Plan re-entry, visual / manual-repro, project-defined human-only items) — those are the "what the human must look at because the model can't decide" list. Advisory in effect (never blocks accept); not opining (does the work).

**3. Human sign-off (instrumented — the second human touch point).** The driver assembles `SUMMARY.md` (the ten sections from [[02 - Cycle Artifacts]]) from `brief.md` + `check-gates.json` + `check-review.md`, routes unresolved items into §6, leaves §9 (sign-off) and §10 (Act candidates) empty for the human, and marks the issue AWAITING_SIGNOFF. Then the driver presents a **sign-off queue**: an index of all AWAITING_SIGNOFF bundles, sorted so the cheap ones come first — empty §6 + disposition ∈ {already-fixed, wontfix, by-design, external} are near-instant confirms (typically the most common outcome); non-empty §6 (real adjudication) flagged and ordered last. The human opens each `SUMMARY.md`, clears §6, fills §9 via a one-command capture, completing Check:

- **accept** → driver performs the sign-off-gated transitions: marks the draft PR ready, posts the §8 tracker comment, and (where the project's per-repo spec allows it) merges. The push and draft-PR-open may already have happened during Do or Check assembly — accept only performs the steps that *required* sign-off. Cycle closes; bundle frozen.
- **iterate-to-Do** → driver removes `patch.diff` and the test from the bundle (preserving the brief), state returns to PLANNED, driver re-invokes the builder. Same cycle.
- **iterate-to-Plan** → driver opens `brief.md` for human edit; on save, state returns to PLANNED, driver re-invokes the builder. Same cycle.

Optionally, the human jots §10 Act candidates while at the bundle — these are hints for the next Act review, not gates for this sign-off.

### Act — instrumented, cross-cycle, batched

Act does not run inside the per-issue state machine. It is a **separate pass**, on a separate cadence (every N completed cycles, weekly, when a pattern surfaces). Its instrumentation:

- **Bundle index.** A read-only generator that lists frozen bundles since the last Act review, surfaces §6/§7/§9/§10 contents, and highlights recurring patterns (same NEEDS-HUMAN class across cycles, same brief-template field flagged in §10).
- **Process-baseline diff tools.** Edit-with-history for the spec template, the conformance ruleset, the gate set, the agent skill files (`SKILL.md` / `AGENTS.md`), with diff/preview against current.
- **Act log writer.** Appends a dated entry to `process/act-log.md` ([[02 - Cycle Artifacts]] §ACT) recording: which bundles were considered, the patterns found, the concrete deltas applied, and a watch-for-recurrence note used by the next Act review.

What is *not* instrumented: the judgment of which rule to add, which template field to clarify, which skill to refine. That is Act's irreducible work.

## Independence is enforced by the orchestrator, mechanically

The decorrelation that makes the reviewer worth running is enforced by the driver, not by prompt text:

- **File withholding** — the driver constructs the reviewer's input set and omits `build-notes.md`. The builder's framing cannot anchor the reviewer because the reviewer never receives it.
- **Tool scope** — reviewer gets execute (run tests/validator, git stash/unstash) and **no write to the fix**. It cannot patch what it judges.
- **Vendor split** — reviewer is a different model family from the builder. Different family = decorrelated blind spots.

These three are orchestrator responsibilities. An LLM told "don't look at the rationale" that still has the file is not independent; the driver simply does not pass the file.

**What this enforcement does and does not buy.** The three mechanisms above decorrelate **evidence-integrity** — the reviewer can't be anchored by the builder's narrative, can't edit the artifact it judges, and brings a different model family's blind spots. They do *not* decorrelate **fix-correctness**: the reviewer's input set still includes `brief.md` and the shipped test, so a framing blind spot the brief carries reaches the reviewer too, and stash → red / unstash → green confirms the test's own narrow oracle, not that the test exercises the real defect. The reviewer attempts causal adequacy advisory (correctness step 5) and may flag NEEDS-HUMAN; the actual check on causal adequacy is the **human at sign-off** ([[06 - Quality Cycle Guidelines]] C6). The orchestrator's job is to make the reviewer's evidence trustworthy, not to make sign-off optional.

## Where it runs: local driver + CI re-confirmation

Two substrates, used for what each is good at:

- **Local/container driver** **[planned]** runs the **contribution body** — Do + Check + assemble — co-located, full control. This is the fast inner loop. Not implemented yet; the role is filled today by hand-invoking Claude Code on a per-issue brief.
- **CI** **[partial]** runs the **same deterministic gates** again as the merge-gate, triggered when sign-off accepts and the draft PR is pushed. The CI workflows exist and run (see the testbed's `.github/workflows/`); they currently cover the gates that have been written (T3 most mature, T1 partly upstream, T2/T4 not yet). The belt-and-suspenders model is the design; the second belt is in place where its rules exist.

The two agree because the gates are **single-sourced** — the validator(s), semgrep rules, and the runtime/suite checks are one implementation, invoked by both the local driver and CI. CI is not a second opinion; it is the same check re-run at the merge boundary so nothing merges that the body did not clear.

Act has no CI counterpart — process improvement is human work that edits the rules CI enforces, not work CI enforces back.

## Batch fan-out

The contribution-batch case is the per-issue driver under an existing fan-out:

1. `run-batch.sh <name> <ids>` → scrape + handoff generator → N draft `brief.md` (Plan scaffolding). **Human fills verdicts** (Plan judgment, the one human step before the body runs).
2. Driver loops every issue through Do → Check → assemble, unattended, producing N `results/issue_<id>/` bundles. Resumable via the state machine.
3. Driver emits the **sign-off queue** (burn-down index, cheap-first). Human works the queue; confirm-and-close items are one keystroke each.

So a contribution-batch is: one human pass at the **Plan** beat to author specs, an unattended run of the **Do** beat and the mechanical portion of the **Check** beat (gates + reviewer) over N issues, then one human pass to complete the **Check** beat (sign-off). Four beats, two human touches inside them.

**An Act batch is separate and slower.** Every K contribution-batches (or on a calendar), the Act tooling presents a cross-cycle bundle index and the human runs one Act review pass covering all bundles since the last review. Cadence is yours; the model only requires that Act fire *eventually* over the records, not that it fire per-cycle.

## Maturity ladder

Build the automation in order. **The three human touch points — Plan authoring, Check sign-off, and Act — stay human at every level.** (Those are three touch points across three beats: Plan and Act are fully human beats; Check is a mixed beat whose sign-off step is its human portion. Do is the fourth beat and has no human touch.)

- **L1 — scripted handoff.** **[built — current rung as of today]** Beats run by hand; the driver only assembles bundles. The agent-work scaffolding (`agent-work/run-batch.sh`, `agent-work/scripts/make_handoff.py`, templates under `agent-work/templates/`) emits draft briefs and bundle directories; everything beat-side from there is hand-invoked Claude Code with manual sign-off.
- **L2 — unattended per-issue body.** **[planned]** One command runs Do→Check→assemble→STOP for a single issue. The state machine + the two headless agent calls + the gate single-sourcing. Blocked on the gates first ([[#Build order]]).
- **L3 — unattended contribution-batch + sign-off queue.** **[planned]** `run-batch.sh` extended to produce N bundles + the burn-down sign-off queue. Plan scaffolding + L2 per issue + the queue generator.
- **L4 — Act review tooling.** **[planned]** Bundle index across frozen cycles, process-baseline diff tools, act-log writer. L4 is independent of L1–L3 — you can run Act manually against L3 bundles before L4 is built. Build L4 when manual Act becomes the bottleneck.

The deterministic gates are the prerequisite for L2/L3 — until Tiers 1–4 are single-sourced and scriptable, "Check" is not automatable and the body cannot run unattended. So the build order is: **gates first**, then the driver, then the contribution-batch queue, then Act tooling.

## What stays human (the honest boundary)

Judgment is irreducible at parts of three beats — Plan, Check, and Act. The fourth beat, **Do**, is fully delegable to the builder: it is production work without an embedded human judgment step.

- **Plan** — the entire beat is human, including any re-entry into Plan triggered by iterate-to-Plan from Check sign-off (the brief revision is Plan work). The agent-work scaffolding drafts; the human decides what to fix and what "fixed" means.
- **Check, at the sign-off step** — the gates and the cross-vendor reviewer model run unattended (full automation); the **sign-off step** that completes Check is the human one. The reviewer **implements** the judgment cells (C5, T5, validation act), attempting PASS/FAIL on items it can decide from `{patch, test, brief, check-gates}` and emitting `NEEDS-HUMAN` *by design* on the items it structurally cannot — fitness-to-purpose, contested symptom-vs-root-cause, semantic upstream-isn't-ahead matches, scope-creep / Plan re-entry calls, visual or manual-repro outcomes, and the project's enumerated human-only items (full list in [[04 - Validation Tooling]] §Inside the judgment cell). The human clears every NEEDS-HUMAN row in `SUMMARY.md` §6 and records the per-contribution disposition in §9.
- **Act** — the entire beat is human. What rule to add, which template field to revise, whether to retire a check. The bundle index surfaces patterns; the human decides.

Automating any of these would be automating judgment, which the model says is irreducible at those three points. The pipeline does not remove the human; it removes everything around the human so the human only does the parts no oracle can.

## Implementation substrate (what is built from what)

"Maximally scripted" has a precise meaning: **minimise model-in-the-loop at run time.** Every beat that *can* be code *is* code; a model is invoked only at the two leaves where the sole available oracle is a model. A skill does not reduce the number of model decisions — it makes the two unavoidable ones repeatable. So skills are one row in the table below, not the backbone.

| Beat(s) served | Concern | Vehicle | Rationale |
|---|---|---|---|
| all four (cross-beat) | Orchestration, state machine, `SUMMARY.md` assembly, sign-off queue | **deterministic driver** (e.g. Python; extends an existing batch runner) | control flow must be code, not a model — a model in the control path can skip a gate or reorder steps |
| Check (gates component) | Check gates (correctness re-runs + conformance T1–4) | **plain code, single-sourced** (validator, semgrep, suite, commit-hooks) | this is the *scripting* of Check; the same impl CI invokes |
| Do | Do — build consistency | **Claude Code Skill** (`SKILL.md`) | pins how a brief becomes patch+test+build-notes; committed, versioned |
| Check (reviewer component) | Reviewer — review consistency | **Codex `AGENTS.md`** | Codex's instruction vehicle; different vendor by design |
| Do + Check (reviewer) | Independence / tool scope | **Claude Code subagents** (`.claude/agents/`) | builder=write, reviewer=execute-no-write, enforced mechanically |
| Plan (cycle entry) | Human single-issue trigger | **slash command** | thin invocation only |
| Check (gates re-run on the actual PR) | Merge re-gate | **CI** (e.g. GitHub Actions) | re-runs the same single-sourced gates on the real PR |
| Plan + Check (read), Act (maintains) | Persistent rules | **CLAUDE.md / AGENTS.md** | already in place |
| Act | Act tooling (L4) | **separate scripts + the act-log** | runs against frozen bundles; never touches in-flight ones |

**The anti-pattern to avoid:** a single agentic skill/loop that "runs the PDCA cycle." It feels like more automation and is less — it re-inserts a model into the control path the design works to keep deterministic (no LLM in the gating path). The cycle is *run by* a script; the model is *invoked by* the script at two leaves. Hold that inversion and the rest follows.

The two model leaves use different instruction vehicles because they are different tools: the builder's consistency lives in a **Claude `SKILL.md`**, the reviewer's in **Codex `AGENTS.md`**. Do not share one file across both.

## Driver skeleton

> **Maturity: [planned].** This is the design for the L2 driver. None of the code below runs as-is today; it is the reference shape an implementation should match. Each function corresponds to a piece in the [[#Build order]] below.

The driver is a thin loop: read each issue's file-state, run the next beat's command, write its artifact, advance, STOP at AWAITING_SIGNOFF. Gates and agents are called through narrow interfaces so they are swappable and individually testable.

```python
# states are derived from files present in results/issue_<id>/ — no DB
def state(d):
    if not (d/"brief.md").exists():        return "UNPLANNED"
    if not (d/"patch.diff").exists():      return "PLANNED"        # ready for Do
    if not (d/"check-gates.json").exists():return "BUILT"          # ready for Check
    if not (d/"SUMMARY.md").exists():      return "CHECKED"        # ready to assemble
    if not signoff_set(d/"SUMMARY.md"):    return "AWAITING_SIGNOFF" # STOP — human
    return iterate_or_complete(d/"SUMMARY.md")  # ITERATE_DO | ITERATE_PLAN | COMPLETE

def advance(d):
    s = state(d)
    if s == "PLANNED":
        do_build(d)                 # Claude Code headless — leaf 1
    elif s == "BUILT":
        run_gates(d)                # deterministic; writes check-gates.json
        run_review(d)               # Codex headless — leaf 2 (advisory)
    elif s == "CHECKED":
        assemble_summary(d)         # pure code: brief+gates+review -> SUMMARY.md §1-8
    elif s == "ITERATE_DO":
        clear_downstream_of_brief(d)   # clear EVERY Do+Check artifact —
                                       # see implementation below
        # state now == "PLANNED" on next call; do_build re-runs
    elif s == "ITERATE_PLAN":
        version_brief_and_clear(d)     # rename brief.md → brief.vN.md,
                                       # then clear everything downstream
        # state now == "UNPLANNED"; human authors a new brief.md, then
        # do_build re-runs
    # AWAITING_SIGNOFF and COMPLETE: driver does nothing (human work or done)

def run_issue(d):
    while state(d) not in ("UNPLANNED", "AWAITING_SIGNOFF", "COMPLETE"):
        advance(d)                  # idempotent; resumable; no-clobber
                                    # (iterate transitions clear deliberately —
                                    # see clear_downstream_of_brief below)

# ---- iterate transitions: clear EVERY downstream artifact, by explicit name ----
# Files downstream of brief.md (everything Do and Check write):
DOWNSTREAM_OF_BRIEF = [
    "patch.diff",
    "build-notes.md",
    "check-gates.json",
    "check-review.md",
    "SUMMARY.md",
]

def clear_downstream_of_brief(d):
    """Iterate-to-Do: clear every artifact produced after brief.md so
    state() returns PLANNED (not the stale CHECKED it would otherwise
    return because check-gates.json was left on disk)."""
    for name in DOWNSTREAM_OF_BRIEF:
        (d/name).unlink(missing_ok=True)
    # the shipped test file's path was named in brief.md — unlink it too
    for tf in test_files_from_brief(d/"brief.md"):
        tf.unlink(missing_ok=True)

def version_brief_and_clear(d):
    """Iterate-to-Plan: version the current brief (brief.md →
    brief.vN.md, preserving history per case-study practice — see
    [[07 - Case Study - CI Hardening]] CLAUDE_CODE_BRIEF v1/v2/v3), then clear every
    downstream artifact so state() returns UNPLANNED."""
    n = next_brief_version(d)        # 1 for first iterate; counts existing brief.vN.md files
    (d/"brief.md").rename(d/f"brief.v{n}.md")
    clear_downstream_of_brief(d)

# ---- leaf 1: Do (builder) — full write + push + draft-PR (no ready-mark) ----
def do_build(d):
    run(["claude","-p","--agent","builder","--input", d/"brief.md",
         "--cwd", target_repo(d)])  # writes patch.diff, the test, build-notes.md

# ---- leaf 2: Check-review (reviewer) — INDEPENDENCE ENFORCED HERE ----
def run_review(d):
    inputs = [d/"patch.diff", d/"test", d/"brief.md", d/"check-gates.json"]
    # build-notes.md is DELIBERATELY ABSENT from inputs — the driver withholds it
    run(["codex","exec","--config","review.AGENTS.md",
         "--read-only-fix", *inputs])   # execute (stash/run), no write to the fix
                                        # writes check-review.md

# ---- the gate runner: one interface, every check single-sourced ----
def run_gates(d):
    results = []
    results += correctness_reruns(d)      # repro red / verify green / regression
    results += conformance_tier(d, 1)     # structural validator (rule IDs)
    results += conformance_tier(d, 2)     # semgrep             (rule IDs)
    results += conformance_tier(d, 3)     # find_spec / runtime suite
    results += conformance_tier(d, 4)     # commit-msg / branch-target / version-bump
    write_json(d/"check-gates.json", results)   # each row: {check, result, oracle, rule_id, path_line}
    # NOTE: blocking logic reads ONLY this file — the reviewer never gates

# ---- Act review (L4) — SEPARATE process, NOT in run_issue ----
def act_review(since: date):
    bundles = list_frozen_bundles_since(since)            # COMPLETE state only
    patterns = scan_for_recurring_signals(bundles)        # §6, §7, §10 across bundles
    # human reviews patterns, decides concrete deltas, applies them via the
    # process-baseline tools; act_log.append() records the decision and the
    # watch-for-recurrence note used by the next act_review.
```

Four invariants the skeleton encodes, each a design rule from [[01 - The Quality Cycle]] / [[02 - Cycle Artifacts]]:

1. **No model in control flow.** `run_issue`/`advance`/`state` are pure code; `claude` and `codex` are called only inside the two leaf functions.
2. **Independence is a missing list element.** `run_review`'s `inputs` omit `build-notes.md`. Independence is enforced by what the driver *does not pass*, not by instruction.
3. **Gating is deterministic.** Blocking reads `check-gates.json` only; `check-review.md` is consumed by `assemble_summary` into §5/§6 as advisory annotation, never as a gate.
4. **Act is out-of-band.** `act_review` is not called from `run_issue`. Per-contribution control flow finishes at AWAITING_SIGNOFF / COMPLETE; Act runs separately, across frozen bundles, on a cadence the human picks.

The gate runner is the long pole: `conformance_tier(d, n)` must resolve to single-sourced implementations (the structural validator, the semgrep rules, the runtime/suite checks, the Tier-4 hooks) that **CI calls too**. Until those exist, `run_gates` has nothing to call and the body cannot run unattended — which is why the build order is gates → driver → contribution-batch queue → Act tooling. See [[04 - Validation Tooling]] for the tier × home decomposition that drives where each gate is built.

## Build order (restated as concrete deliverables)

Status against each step is shown in brackets. The pipeline as a whole sits at L1 today; everything below L1 is **[planned]** until the gates ship.

1. **Gates, single-sourced** **[partial]** — the structural validator (Tier-1 exec-shim + Tier-2 semgrep, per [[04 - Validation Tooling]]), the Tier-3 runtime checks, the Tier-4 commit-msg + branch-target + version-bump hooks. Each callable identically by the driver and by CI. Status today (per [[04 - Validation Tooling]]): T3 most mature; T1 partly upstream; T2 not yet written for addons; T4 greenfield.
2. **The driver** **[planned]** — the skeleton above: state machine including iteration paths, the two leaf invocations with file-withholding, the gate runner, `assemble_summary`.
3. **The contribution-batch queue** **[planned]** — extension that fans the driver over N issues and emits the cheap-first sign-off burn-down index.
4. **The two leaf instruction files** **[planned]** — builder `SKILL.md`, reviewer Codex `AGENTS.md`, plus the `.claude/agents/` subagent scopes (including the ready-mark allowlist constraint, see [[#Do — full]]) — built alongside 2, refined as the body runs on real issues.
5. **Act tooling (L4)** **[planned]** — bundle index across frozen cycles, process-baseline diff helpers, act-log writer. Build when manual Act becomes the bottleneck, not before — Act can run on hand-read bundles indefinitely.
