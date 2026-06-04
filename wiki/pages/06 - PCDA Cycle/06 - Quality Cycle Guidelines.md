---
title: "Quality Cycle Guidelines (per-beat MUST / SHOULD / MAY rules)"
categories: []
managed: false
status: active
---

> Prescriptive guidelines for executing each PDCA beat. Sits beside the descriptive model in [[01 - The Quality Cycle]] and the operational spec in [[02 - Cycle Artifacts]]: 01 says *what each beat is*, 02 says *what each beat produces*, this doc says *how to do each beat well*. Designed for a practitioner to open side-by-side with the beat they are currently running. Living document.

## Conventions

The keywords **MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT**, and **MAY** are used in the sense of [RFC 2119](https://www.rfc-editor.org/rfc/rfc2119):

- **MUST / MUST NOT** — an absolute requirement or prohibition. A cycle that violates a MUST is broken; the violation MUST be corrected before the beat can be considered complete.
- **SHOULD / SHOULD NOT** — strongly recommended; deviations exist but the practitioner must understand the cost. Deviating without recording why in `build-notes.md` / `SUMMARY.md` §7 is itself a violation.
- **MAY** — optional; the practitioner chooses based on context.

Guidelines are numbered per beat (**P-**, **D-**, **C-**, **A-**) so a review note or PR comment can cite e.g. "P3" or "C6" without ambiguity.

## Precondition — the per-repo specification

The PDCA cycle has four beats. But the cycle as documented here cannot run against a particular repository without knowing that repository's specifics: which branch a fix targets, which fixture is ground truth, which conformance ruleset applies, where the brief template lives. Those specifics are not part of the generic cycle — they are a **per-repo specification** that the Plan and Check beats *read* when they run in a given repo.

**Every repository that adopts this cycle MUST maintain its own per-repo specification document** (e.g. `docs/quality-cycle.md`, `AGENTS.md`, `CLAUDE.md`, or wherever the project keeps agent instructions). [[05 - Repository Integration]] is the full specification of what the integration must cover and how it slots in; the summary below is the minimum view for the per-beat rules in this doc. Required items at minimum:

- **Branch-target resolution.** Which logical change targets which branch (e.g. core fixes → `maintenance/gramps61`; addon fixes → `maintenance/gramps60` with forward cherry-pick; testbed changes → `main`). Read by Plan (P4 instantiation).
- **Canonical reproduction fixtures.** Which fixture is the cycle's ground truth (the file, the dataset, the test command). Read by Plan (P1) and re-run by Check (correctness chain step 2).
- **Conformance ruleset and gate homes.** The active rules at each Tier (1–4), where they are implemented, and which gate them. The repo's instantiation of [[04 - Validation Tooling]]'s tier × home decomposition. Read by Check (gates path). **For Tier 5, the spec MUST also enumerate the project-defined human-only items** ([[04 - Validation Tooling]] §Inside the judgment cell; [[05 - Repository Integration]] §4) — the C5/T5/validation-act items the cross-vendor reviewer must emit `NEEDS-HUMAN` on *by design* rather than attempt a PASS/FAIL. This is the "what the human must look at because the model can't decide" list for this project; the reviewer reads it as input and §6 NEEDS-HUMAN is populated from it.
- **Upstream-isn't-ahead verification routine.** The specific search/grep/PR-check the human runs on triage cycles — search-by-affected-file-path conventions, which trackers to consult, which keywords don't tokenize. Read by Plan (P8 instantiation).
- **Brief and design-proposal template locations.** Paths to the `brief.md` template Plan uses for one-fix cycles, and to the design-proposal template if design-shaped Plans are written here. Read by Plan.
- **Result-bundle path convention.** Where `results/issue_<id>/` bundles live in this repo, and where `process/act-log.md` lives. Read by Plan (bundle creation) and Check (bundle writes).
- **Repo-specific cycle conventions.** Anything the cycle's generic shape doesn't determine but the repo needs: commit-message format, PR-review gates, disposition-language conventions, reviewer-permission boundaries layered on the generic Check/Act seam.

The per-repo specification MAY add repo-prefixed P- / D- / C- / A- rules of its own (e.g. `gramps-P1`, `testbed-C7`) to tighten or specify a generic rule for local needs. It MUST NOT delete or weaken a generic rule below.

**Conflict resolution.** When a per-repo rule and a generic rule appear to conflict:

- If the conflict is about **cycle shape** (what Plan/Do/Check/Act are, what the artifacts are, what the seam between beats means) — the **generic rule wins**. A per-repo spec MUST NOT redefine the cycle.
- If the conflict is about **instantiation** (which branch, which fixture, which rule ID, which path, which tracker convention) — the **per-repo rule wins**. The generic doc has no opinion on specifics.

A real shape-layer conflict is an A2-shaped Act candidate against this generic doc — log it for the next review of this file.

The per-repo specification is itself part of the **process baseline** Act maintains ([[01 - The Quality Cycle]] §Act); updates land as act-log entries per A6 (append-only). A repo that runs the cycle without writing its per-repo specification is running on tribal knowledge — the failure mode the cycle exists to eliminate ([[01 - The Quality Cycle]] §What Plan inherits from Act). The per-repo spec *is* the project's accumulated Act output made writable; without it, Act has nowhere to land.

---

## Plan guidelines (P-)

### P1. MUST reproduce before authoring the spec

Reproduce the reported defect against the canonical fixture on the target branch before writing the spec. If the report does not reproduce, close the cycle here with a confirm-and-close disposition.

*Rationale.* A spec authored without a reproduction is unfounded — Do will build against a guess and Check has nothing to verify. Plan asking "is there a defect at all" and answering "no" is a successful PDCA outcome ([[01 - The Quality Cycle]] §Plan), not a failure.

### P2. MUST write a mechanically testable success criterion

The "what 'fixed' means" sentence MUST be specific enough that you could draft the test that would pass it before Do starts. If you cannot draft that test from the criterion alone, the criterion is too vague.

*Rationale.* The success criterion is the load-bearing field of the spec. Check measures against it; ambiguity here propagates into every downstream beat. The mechanical-test reductio is the cheapest test of spec specificity available at Plan time.

### P3. MUST state what is out of scope

The brief MUST explicitly list what the contribution is *not* attempting, alongside what it is. Out-of-scope statements are not optional; they are how Check flags scope creep against a written boundary ([[02 - Cycle Artifacts]] §PLAN).

*Rationale.* Without an out-of-scope clause, scope creep at Do time becomes ambiguous — the builder may legitimately expand because no boundary was written. The cost of writing the boundary is one sentence; the cost of relitigating scope at Check is the whole cycle.

### P4. MUST resolve the branch target in the brief

The repo + branch target MUST be decided at Plan time and named in the brief, not deferred to Do. For cross-repo ambiguity (e.g. core vs addon), use a reproduction to disambiguate.

*Rationale.* Branch-target resolution is a Plan-side judgment (which project policy applies, what the maintenance vs master rule is here) and decoupling it from Do prevents builders from making it mechanically wrong. See [[07 - Case Study - CI Hardening]] Item 2 for the failure mode when the branch-target rule itself is self-contradictory and the resolution gets delegated downward.

### P5. MUST author one logical contribution per brief

A brief MUST cover exactly one logical fix. If the work spans coordinated multi-part scope (architectural change, phased migration, proposal-shaped piece), the brief MUST be promoted to a design proposal ([[01 - The Quality Cycle]] §Solution-approach design) that spawns N child briefs.

*Rationale.* "One logical fix per PR" enforced at Do/Check is a brief-level discipline; bundling at the brief level just pushes the bundling problem one beat upstream. The promotion-to-design rule is what keeps the brief shape honest at small scale.

### P6. SHOULD give a disposition hint; MUST NOT make it binding

The brief SHOULD include the Plan-time triage guess (likely-fix, likely-close, POSSIBLY-FIXED → verify first). The hint MUST NOT bind Do or Check; either may override it on evidence.

*Rationale.* Hints save cycle time on the common cases (the cheap confirm-and-close burns one keystroke at Check) without short-circuiting evidence on the uncommon ones. A hint that binds becomes a verdict-by-Plan, which Plan does not have the information to make.

### P7. MUST enforce STOP discipline (no ready-mark before sign-off)

The brief MUST instruct Do that pushing to feature/draft branches and opening draft PRs are permitted, and that the **ready-mark** (the explicit "this is ready to merge" transition) MUST NOT happen before Check sign-off accepts. Operationally this is enforced by builder subagent tool scope ([[03 - Cycle Automation]] §Independence), but the brief MUST also state the constraint so the contract with the human is explicit at Plan time.

*Rationale.* Sign-off is the human's, irreducibly. STOP discipline is what makes Check sign-off the only path from draft to merged. Pushing and draft-PR-open during the cycle are useful — they let CI gates run against the actual artifact and surface work-in-progress for review — without bypassing the sign-off gate, because neither transitions the PR out of draft state. The ready-mark is the one action only the human (or the driver's accept transition) may perform.

### P8. SHOULD verify upstream isn't ahead

For triage cycles (bug reports against an upstream project), the brief SHOULD include a check that the defect isn't already fixed on the target branch or addressed by an open PR. Search by affected file path, not just the bug number or keyword substring.

The check has two layers, with different decidability ([[04 - Validation Tooling]] §Inside the judgment cell):

- **Mechanical search** — open PRs touching the same files, merged history on the target branch. Automatable; the cross-vendor reviewer may re-run this at Check time on the artifact alone.
- **Semantic match** — *does* an open rewrite PR supersede this fix; is the closed PR a maintainer "no" rather than an unrelated dead end. Human-only by design (the reviewer emits `NEEDS-HUMAN`); needs project-direction context the model lacks. Plan owns this layer.

*Rationale.* A third of recent-pool triage items turn out already-fixed, by-design, duplicate, or external. The default action on POSSIBLY-FIXED is verification, not implementation. Mechanical-only verification misses superseded-by-rewrite PRs; semantic verification is Plan-time human work. See the project's bug-tracker conventions ([[00 - Overview]] / project CLAUDE.md) for the specific verification routine.

### P9. (Design-shaped Plans) MUST include Non-goals and Open questions

A design-proposal-shaped Plan ([[01 - The Quality Cycle]] §Solution-approach design) MUST include explicit Non-goals (what the design refuses to attempt) and Open questions (items Plan could not resolve, flagged for the review cycle on the proposal itself).

*Rationale.* Non-goals do the same boundary-maintenance work for designs that P3's out-of-scope clause does for briefs. Open questions are Plan's ex-ante analogue of `SUMMARY.md` §6 NEEDS-HUMAN — hidden opens become surprise rework at child-brief Check time.

### P10. SHOULD cite Plan-internal grounding investigations like evidence

When Plan runs a scoped Do-shape sub-investigation to ground a recommendation (a measurement, an audit, an analysis), the investigation's output SHOULD be cited as evidence (path or URL, run date, scope of inputs) — not narrated as belief.

*Rationale.* Plan honest about its evidence sources keeps Plan-to-Do expectations grounded. See GEPS 049's griffe analysis ([[07 - Case Study - CI Hardening]] §Parallel example) for the model: the empirical breakage table is what makes the maintenance-release claim defensible rather than asserted.

### P11. MUST consult the per-repo specification for repo-specific inputs

Plan MUST read the active repo's per-repo specification (see §Precondition above) for branch-target resolution (concretizes P4), canonical reproduction fixtures (P1), brief and design-proposal template paths, upstream-isn't-ahead verification routine (P8), and the result-bundle path convention. Improvising these values when the spec answers them is a P11 violation even if the resulting brief happens to be correct.

*Rationale.* Plan's per-cycle judgment is "what to fix and what 'fixed' means"; the repo-specific facts surrounding that judgment (which branch, which fixture, which template) are baseline questions already answered by the per-repo spec. Re-deriving them per cycle invites drift between cycles in the same repo and dissolves the spec's role as the project's accumulated Act output. If a per-repo spec answer feels wrong, the action is a §10 Act candidate against that spec — not an in-brief override.

---

## Do guidelines (D-)

### D1. MUST read `brief.md` only

The builder MUST read the brief and the cited source files. The builder MUST NOT read prior cycles' bundles, the conformance ruleset (which Check applies), or unrelated project context not cited by the brief.

*Rationale.* Narrow input keeps Do focused on this contribution; Check later evaluates whether the build matches *this brief*, not whether it matches some broader interpretation Do imported. Wider input ranges expand the surface for misalignment without improving the build.

### D2. MUST produce three outputs in lockstep

Do MUST produce `patch.diff`, the test (at the location the brief named), and `build-notes.md` — together, in the same cycle turn. Missing any one means the brief's requirements are unmet ([[02 - Cycle Artifacts]] §DO).

*Rationale.* The test ships with the patch because Check's verification step needs both; build-notes ships with the patch because the human signing off Check sees claim and verdict side by side. Each file serves a distinct downstream consumer; skipping one breaks that consumer.

### D3. MUST verify the test fails pre-fix and passes post-fix

The builder MUST run the shipped test against the pre-fix code (it MUST fail) and the post-fix code (it MUST pass), and cite both runs in `build-notes.md`. A test that does not fail pre-fix proves nothing about the fix.

*Rationale.* The most common silent failure of D2 is a green test that never exercised the bug. The pre-fix red is the only oracle that the test actually covers the defect the brief named.

### D4. MUST cite path:line on the target branch for every claim

Every claim in `build-notes.md` and every change-related statement MUST cite `path:line` on the target branch. Citations that do not resolve at Check time are dropped by the reviewer (a Check-side rule); unresolved citations in the build are functionally absent.

*Rationale.* Recollection is a hypothesis, not a verification. Path:line citations make every claim falsifiable, which is the only way Check can verify them at all.

### D5. SHOULD write `build-notes.md` for the human, not the reviewer

`build-notes.md` is for the human signing off Check. It SHOULD record the builder's rationale plainly: why this change, what was tried, what was ruled out. It SHOULD NOT anticipate or address the reviewer's grading (the reviewer never sees the file — file-withholding, [[03 - Cycle Automation]] §Independence).

*Rationale.* Build-notes written *as if* the reviewer will read them distort toward defense rather than explanation. The independence contract works mechanically; the builder writing as if it didn't makes the human's sign-off harder, not easier.

### D6. MUST keep the patch to one logical change; out-of-scope findings need proof, not narration

The patch MUST implement exactly the brief's scope. Defects the builder discovers mid-build that are *outside* the brief's scope MUST NOT be folded into this patch — they must be **proven** and **handed off** per [[04 - Validation Tooling]] §Subject item dependencies, by the relationship to the dependency:

- **Sister-project dependency** (a repo with contribution rights — e.g., `gramps` core relative to `addons-source`): triage to handoff readiness — either a minimal proven reproduction (repro script + evidence + path:line) or a `brief.md`-shape draft ready to enter the sister project's own PDCA cycle. Record as a `handoff-<repo>.md` attachment in the bundle and a `§10` Act candidate noting the handoff exists.
- **Pre-build dependency** (third-party, no control — Gtk, glibc, PyPI): same proof rigor (repro + evidence), but flagged in `build-notes.md` for the cross-vendor reviewer to surface as `NEEDS-HUMAN` at Check, where the human at sign-off decides disposition (file upstream, defensive workaround → likely iterate-to-Plan, pin, document-and-ship, wait).

"Noticed and abandoned" is not a valid disposition for out-of-scope findings. A finding without a repro is dropped, not deferred — the cycle MUST NOT leak unproven dependency observations into the next cycle's archaeology layer.

*Rationale.* Bundling hides mistakes ([[07 - Case Study - CI Hardening]] convention). Drive-by fixes in this patch shift Check's unit of evaluation away from the brief and toward whatever the builder felt was worth fixing — which is not what Check is set up to adjudicate. The proof-required clause is what stops D6's "surface for a future Plan" from degrading into a TODO graveyard: a sister-project handoff or pre-build NEEDS-HUMAN both require evidence Check can verify, so the discipline is honest at the seam.

### D7. MUST NOT mark a PR ready before Check sign-off

Do MAY commit, push to feature/draft branches, and open draft PRs — all useful for letting CI gates exercise the artifact and surfacing work-in-progress. Do MUST NOT mark a PR ready, transition a PR out of draft state, or merge.

**On enforcement.** The intended mechanism is subcommand-level Bash allowlists in the builder subagent's config: allow `Bash(gh pr create:*)` and `Bash(git push:*)`, deny `Bash(gh pr ready:*)` and `Bash(gh pr merge:*)`. Claude Code's permission system supports that granularity; the testbed's current top-level `settings.json` already uses the same pattern (`gh pr create:*` allowed, `gh pr ready:*` absent). The `.claude/agents/` files that would apply the pattern to the builder subagent **are planned but not yet built** in this project (see [[03 - Cycle Automation]] §Do for the maturity-tag context). Until those files exist, the builder MUST respect this rule because the brief states it — not because the tool scope blocks it. Any action that would transition the PR out of draft state is a D7 violation regardless of whether enforcement is currently mechanical or discipline-based.

*Rationale.* STOP discipline (P7's downstream half) is the only thing that makes Check sign-off load-bearing. A PR that escapes draft state before sign-off has bypassed the cycle's only validation point. Push and draft-PR-open do *not* bypass that gate — they enable CI feedback and visibility without changing the PR's reviewability state. The ready-mark is the line because it is the explicit "this is ready to merge" signal that downstream consumers (CI required-checks, human reviewers, auto-merge bots) act on.

### D8. MUST stop and request iterate-to-Plan if the brief is ambiguous

If a brief field is ambiguous in a way that affects the build, Do MUST stop and surface the ambiguity for iterate-to-Plan ([[02 - Cycle Artifacts]] §9) — not guess. Recording the ambiguity in `build-notes.md` and proceeding is a violation of D8.

*Rationale.* Guessing produces a build that might match the brief, or might not, with no way for Check to tell which. Iterate-to-Plan is cheap (revise the brief, re-run Do); a guess that later fails Check costs the full Do+Check turn plus rework.

### D9. MUST stop and surface if the brief is wrong

If, during build, Do discovers evidence that the brief itself is incorrect (e.g. the assumed root cause is wrong, the cited file no longer exists, the proposed mechanism is empirically invalid), Do MUST stop and surface — do not implement against a brief you believe is broken.

*Rationale.* A patch built against a known-wrong brief produces a known-wrong fix that Check may nonetheless accept on its narrow criteria. The honest move is iterate-to-Plan with the evidence attached. See [[07 - Case Study - CI Hardening]] Item C for the canonical case (brief demanded an exec-shim; 14/14 empirical audit showed it was unnecessary).

### D10. SHOULD NOT consume the conformance ruleset directly

Do SHOULD NOT read or apply the conformance ruleset (Tiers 1–4) during the build. The ruleset is Check's input; Do follows the brief.

*Rationale.* Pre-conforming during Do anchors the build toward ruleset-conformance over brief-conformance and trains the builder to optimize for "passes Check" instead of "matches brief." The deterministic gates can correct conformance defects auto-fix-style at Check time without Do attempting it.

---

## Check guidelines (C-)

### C1. MUST run deterministic gates before the cross-vendor reviewer

The gate suite (correctness re-runs + conformance Tiers 1–4) MUST complete before the cross-vendor reviewer model is invoked. The reviewer reads `check-gates.json` as input ([[02 - Cycle Artifacts]] §CHECK), so gates-first is mechanical, not just preferred.

*Rationale.* The reviewer's value is decorrelation; reading gate output sharpens the reviewer's grounding step (re-run cited evidence, re-verify path:lines). Reversing the order would have the reviewer opine on un-verified claims. "Advisory" describes the reviewer's effect (never gates accept), not its role — the reviewer *implements* the judgment cells ([[04 - Validation Tooling]] §Inside the judgment cell); it is not a courtesy second opinion.

### C2. MUST name an oracle and cite path:line for every gating claim

Every **gating** row in `check-gates.{md,json}` (C2 reproduction, C4 verification + regression, T1–T4) and every finding in `check-review.md` MUST carry: the oracle that decided it, the rule ID (where applicable), and a path:line citation on the target branch. Findings without an oracle are dropped.

The check-gates table also includes **non-gating rows** for structural alignment with the 5/5/1 ([[02 - Cycle Artifacts]] §check-gates table) — C1 spec, C3 change (inputs from Plan/Do); C5 causal adequacy, T5 judgment, validation act (judgment-path, decided in `check-review.md` and §9 sign-off). These rows carry `none` for output, oracle, and evidence *by design* — they are listed so the reader can see they were not silently dropped, not gated here. Treating `none` on a non-gating row as a C2 violation is itself a C2 misreading.

*Rationale.* Oracle accounting is what lets the human signing off Check weigh evidence honestly ([[01 - The Quality Cycle]] §The oracle principle). A claim with no oracle is rhetoric. The non-gating-row exception is what stops "every row needs an oracle" from forcing fake oracles onto cells decided elsewhere; the 5/5/1 alignment matters more than table uniformity.

### C3. MUST state scope of green and what is unproven

`SUMMARY.md` §7 (Proven / not proven) MUST name what specific path the green checks exercised and what is left unproven (a platform not run, a fixture not exercised, a behavioral edge not tested). An empty §7 is a violation of C3 — "everything is proven" is almost never true.

*Rationale.* "A green check is evidence of that narrow check, not of correctness." Honest oracle limits at §7 prevent over-trusting greens at sign-off. The discipline of writing §7 also surfaces gaps that can become P10-style grounding investigations in the next Plan.

### C4. MUST withhold `build-notes.md` from the reviewer

The reviewer's input set MUST be `{patch.diff, test, brief.md, check-gates.json}` only. `build-notes.md` is excluded by the driver's file-input list ([[03 - Cycle Automation]] §Independence). Any configuration that passes build-notes is an independence-contract violation.

*Rationale.* Independence is enforced by file access, not prompt wording. The reviewer told "ignore the rationale" that still receives it is not independent. The driver's input list is the contract.

**What C4 does and does not buy** ([[02 - Cycle Artifacts]] §Independence contract): file-withholding decorrelates evidence-integrity — the builder's framing of *why* the change is correct cannot anchor the reviewer's reading of the patch. It does *not* fully defend against framing blind spots in the brief and test (both of which the reviewer sees), nor against causal-adequacy errors that survive a passing test. C6 (§6 must be empty before accept) and the human at sign-off are the real check on those failure modes; C4 is a necessary discipline, not a substitute.

### C5. MUST auto-fix only mechanical FAILs; route decisions to NEEDS-HUMAN

A deterministic FAIL with auto-fixable cause (lint, format, genuinely-red test that's a known-fixable shape) MAY be auto-fixed and re-run. A FAIL that requires a decision (which fixture? which branch? is this scope creep?) MUST be routed to `SUMMARY.md` §6 NEEDS-HUMAN.

*Rationale.* Auto-fixing decisions is a model in the gating path, which the design works to keep deterministic ([[03 - Cycle Automation]] §Implementation substrate). The rule "auto-fix only mechanical FAILs" is what preserves the no-LLM-in-gates invariant.

### C6. §6 NEEDS-HUMAN MUST be empty before sign-off can accept

Check sign-off (§9) MUST NOT record an *accept* outcome while §6 contains unresolved items. Each NEEDS-HUMAN item is cleared by the human or routed to iterate-to-Plan / iterate-to-Do before accept is available.

*Rationale.* §6 is literally the within-Check seam between mechanical (gates + reviewer) and human (sign-off) on the page — it lists the items the gates and reviewer could not resolve, which the human at sign-off must. Accepting with §6 items still open means the human signed off something the cycle explicitly flagged as undecidable without human input. The accept/iterate fork exists precisely so this doesn't happen.

### C7. MUST distinguish iterate-to-Do from iterate-to-Plan

When sign-off chooses iteration, the §9 outcome MUST be either *iterate-to-Do* (the build was wrong; the spec was right) or *iterate-to-Plan* (the spec was wrong). The two paths trigger different driver actions ([[03 - Cycle Automation]] §Driver skeleton: `unlink_build_outputs` vs `unlink_brief_and_build`) and conflating them produces wrong control flow.

*Rationale.* Iterate-to-Do re-runs the builder against the same brief. Iterate-to-Plan invites the human to revise the brief and *then* re-runs Do. Defaulting to one when the other is right wastes a turn and may produce the same failed build twice.

### C8. §10 Act candidates MUST NOT gate sign-off

Items recorded in `SUMMARY.md` §10 (process observations for the next Act review) MUST NOT block sign-off, regardless of count or severity. §10 is a hint feeder, not a gate.

*Rationale.* Act fires across cycles; a single cycle's §10 item is data for a future Act review, not a Check requirement. Gating sign-off on §10 would conflate per-contribution adjudication (Check) with process improvement (Act), the seam [[01 - The Quality Cycle]] §The seam is built to preserve.

### C9. The cross-vendor reviewer MUST NOT write the fix

The cross-vendor reviewer's tool scope MUST grant execute access (run tests, validator, `git stash`/`unstash`) and MUST deny write access to the fix or to `SUMMARY.md` §9. The reviewer implements the judgment cells with PASS/FAIL/NEEDS-HUMAN; the human and the deterministic gates decide accept.

*Rationale.* A reviewer that can patch the artifact it is judging becomes a builder with extra steps, breaking the role partition [[01 - The Quality Cycle]] §The four beats names. The tool-scope constraint is mechanical, not stylistic. C9 is the partner to C4 in the independence contract: C4 withholds the builder's narrative, C9 withholds the reviewer's ability to become a builder.

### C10. SHOULD apply the collapse rule

For conformance-defect fixes (a missing `tests/__init__.py`, a banned import), the conformance check itself SHOULD be treated as the correctness oracle — "correct" reduces to "the check now passes." For behavioral-defect fixes, correctness needs its own independent evidence chain ([[01 - The Quality Cycle]] §Where the stages touch and collapse).

*Rationale.* Forcing a full behavioral-correctness chain for a conformance-defect fix wastes a cycle turn on evidence that doesn't inform the decision. Forcing only the conformance check for a behavioral defect leaves the actual behavior unverified.

### C11. MUST apply the per-repo conformance ruleset at the homes the spec designates

Check MUST run the active repo's conformance ruleset — Tiers 1–4 at the homes the per-repo specification designates ([[04 - Validation Tooling]] tier × home decomposition, instantiated per-repo in the spec). Running a partial or substituted ruleset is a C11 violation even if every check that *did* run passes.

*Rationale.* The per-repo specification is what makes "did Check apply the right rules" answerable in any specific repo. The generic doc has no opinion on which rules are active; the per-repo spec does. Skipping or substituting a rule because the gate was inconvenient to run shifts the cycle off the project's actual ruleset — which is the failure mode A2 (concrete, located deltas) protects against on the Act side, applied here on the Check side. If a rule is genuinely wrong or its home is genuinely misplaced, that is a §10 Act candidate against the per-repo spec — not a Check-time skip.

### C12. MUST flag the project's enumerated human-only items as NEEDS-HUMAN by design

The per-repo specification MUST enumerate the project's human-only items for the judgment cells C5 / T5 / validation act (per §Precondition; per [[04 - Validation Tooling]] §Inside the judgment cell and [[05 - Repository Integration]] §4). The cross-vendor reviewer MUST emit `NEEDS-HUMAN` on those items *by design* — it MUST NOT attempt a PASS/FAIL on them from the artifacts alone. Generic always-human items the spec MUST include (it MAY add project-specific ones):

- Validation fitness-to-purpose ("is this the right thing at all").
- Symptom-vs-root-cause when the bug's mechanism is contested.
- Upstream-isn't-ahead, *semantic* match (does an open rewrite PR supersede this fix; cf. P8).
- Scope-creep / Plan re-entry calls.
- Visual sign-off and manual-repro outcomes (also flagged in `MANUAL-VERIFICATION.md`).

A reviewer that returns PASS/FAIL on an enumerated human-only item is a C12 violation regardless of whether the verdict happens to be correct. A per-repo spec that omits the enumeration is a §Precondition violation that surfaces here.

*Rationale.* The judgment cell is implemented by the reviewer, but its implementation is *not* "decide everything." `NEEDS-HUMAN` is a structural verdict — the explicit list of "what the human must look at because the model can't decide." Without the enumeration, the model and the human are both improvising the boundary at run time, which is the failure mode the cycle exists to eliminate. C12 closes the loop between [[04 - Validation Tooling]]'s judgment-cell design and the per-repo integration's enumeration duty.

---

## Act guidelines (A-)

### A1. MUST NOT fire mid-cycle

Act MUST run only on completed (frozen) cycles. If you are tempted to Act before sign-off has closed the cycle, that work is iterate-to-Plan or NEEDS-HUMAN, not Act.

*Rationale.* Act operates on *the process*; Check operates on *the contribution* ([[01 - The Quality Cycle]] §Contribution work vs process work). Acting mid-cycle dissolves the seam. The frozen-bundle constraint is what keeps Act's inputs stable enough to reason across.

### A2. MUST make every delta concrete and located

Every Act-log entry MUST name a specific delta: a file path edited, a rule ID added/retired, a template field changed, a SKILL.md / AGENTS.md passage adjusted. "We should be more careful" is not a delta; "rule R-042 added to Tier 2 covering the `_("f-string")` shape, with fixture at `path/to/fixture`" is.

*Rationale.* Act's effectiveness is judged against future cycles ([[01 - The Quality Cycle]] §When effectiveness is judged). Without a concrete delta, there is nothing to judge — and nothing for the next Act review to verify against either.

### A3. MUST state how effectiveness will be judged

Every Act-log entry MUST include a watch-for-recurrence note: which next K cycles to watch, what failure of the delta would look like, what would prove the delta is working. This is the entry's own contract with future Act reviews.

*Rationale.* Without a stated effectiveness test, the delta becomes a permanent commitment with no exit. The watch-K-cycles clause forces an honest "we'll know by date X whether this worked," which the next Act review reads as input.

### A4. MUST NOT re-decide contribution dispositions

Act MUST NOT revisit individual cycles' sign-off outcomes. Check decided merge/close/iterate at sign-off; Act takes those as input, not as questions to reopen.

*Rationale.* Re-deciding dispositions retroactively breaks the finality of sign-off and dissolves the Check/Act seam from the Act side. Process-level deltas may *change the rules that would govern the next cycle*, but they do not retroactively change what was right under the prior rules.

### A5. SHOULD read across multiple bundles, not the most recent only

An Act review SHOULD consider §6/§7/§9/§10 of more than one completed bundle when more than one exists since the last Act review. Reviewing only the most recent cycle produces noisy, reactive process changes.

*Rationale.* Patterns surface across N — "three cycles in a row hit the same NEEDS-HUMAN class" is the kind of signal a single cycle can't produce. The cross-cycle read is Act's actual value-add over per-cycle sign-off.

**On cadence.** A5 is SHOULD, not MUST, deliberately. Earlier drafts required N ≥ ~5 bundles before Act could fire, which fits enterprise maturity but is wrong for a solo project. The honest rule: Act *should* span more than one bundle when more than one is available; *may* span only one when that's all there is and a process observation genuinely warrants action. Skipping Act because "we don't have five bundles yet" is a worse failure mode than running it with two. Pick a cadence that matches the project's actual flow (a single contributor batching weekly looks different from a team batching quarterly); the rule is "more than one bundle when possible," not a fixed N.

### A6. Act log MUST be append-only

Entries in `process/act-log.md` MUST NOT be edited or removed. Corrections to a prior Act take the form of a new entry that cites and supersedes the prior one. (Solo projects: A6 stays MUST. Append-only is cheap, useful at any scale, and it is what makes A8's recurrence test possible.)

*Rationale.* The log is the audit trail for *why* the current process baseline reads as it does. Overwriting prior entries loses the history that the next Act review needs to evaluate effectiveness. Editorial cleanup is the wrong reflex; new-entry-citing-old is the right one.

### A7. MUST escalate architectural-scale deltas to design-shaped Plans

If an Act review concludes that a delta would constitute a multi-part architectural change (a new gate stack, a registration-schema extension, a re-homing of conformance tiers), the work MUST be escalated to a design-shaped Plan ([[01 - The Quality Cycle]] §Solution-approach design) — not landed as an Act delta directly.

*Rationale.* Act is for incremental process improvement; coordinated multi-part work needs the design-proposal sections (goals/non-goals, phased migration, objections-and-responses, open questions) to land safely. The escalation rule is what keeps Act from accidentally shipping unreviewed architecture.

### A8. SHOULD watch for recurrence in subsequent cycles

The next Act review SHOULD verify the predicted recurrence test from the prior Act (per A3). If the issue recurred, the next Act records that the prior Act was not effective and proposes a sharper delta.

*Rationale.* "Did the next Do recreate the issue this Act tried to eliminate?" is the only honest measure of an Act's effectiveness. The feedback loop closes through SHOULD-A8, not through introspection.

**On K.** The recurrence-watch window is the number of cycles between this Act and the next Act review that will check effectiveness — it is whatever the project's cadence makes natural, not a fixed number. For a solo project running cycles every few days, K = 5 to 10 cycles is a reasonable window. For a team batching quarterly, K might be one batch. The point of A8 is *that the next Act remembers to check*, not that K equals any specific value.

---

## On using these guidelines

These are the rules a practitioner consults *while in a beat*. They are not a substitute for the model ([[01 - The Quality Cycle]]) or the artifact spec ([[02 - Cycle Artifacts]]) — read those once, refer to this doc often. A review comment or PR thread citing e.g. "P3, P8" or "C6 violated — §6 has open items" is the intended interaction shape.

When a guideline appears to conflict with another (P5 vs the brief in hand, C5 vs an auto-fix that "feels" decision-level, A2 vs a soft-shaped pattern), the higher-numbered model documents are the tiebreaker: the guideline is a derived rule; the model is the source. A real conflict between two guidelines is itself an A2-shaped Act candidate — log it.
