---
title: "Validation Tooling — what implements Check, and where it lives"
categories: []
managed: false
status: active
---

> The Check beat ([[01 - The Quality Cycle]] §Check) has internal structure — the **5 / 5 / 1** (correctness chain, conformance stack, validation act) — and runs through three **components** (gates, reviewer, sign-off — see [[03 - Cycle Automation]] §Check). This doc documents the code and process that *implements* those components: which tool covers which 5/5/1 element, where that tool lives, and how single-sourcing keeps the driver and CI invoking the same implementation. Worked example uses the Gramps testbed at the end; the structure is project-agnostic. Living document.

## What "validation tooling" means here

"Validation tooling" is shorthand for **the implementation of Check's deterministic gates and advisory reviewer.** Check has three components:

- **Gates** (deterministic, full automation) — the validators, rule scanners, suite runners, and hooks that produce `check-gates.json`.
- **Reviewer** (advisory, full automation) — the cross-vendor model that grounds the gate evidence, re-runs the asserted red/green, and emits per-item `PASS / FAIL / NEEDS-HUMAN` into `check-review.md`.
- **Sign-off** (instrumented, human) — the human completes Check by reading the assembled `SUMMARY.md` and recording §9.

This doc is about the **gates** and **reviewer**. Sign-off is human work whose tooling is the result-document presentation in [[02 - Cycle Artifacts]] / [[03 - Cycle Automation]] §Check sign-off, not the subject here.

## Two axes — what and where

Validation tooling decomposes along two orthogonal axes:

1. **What it evaluates** — which element of Check's 5/5/1 it covers. The 5/5/1 is the *what*:
   - Correctness chain (5 steps): spec → reproduction → change → verification → causal adequacy.
   - Conformance stack (5 tiers): structure → shape → runtime → contribution → judgment.
   - Validation (1 act): fitness-to-purpose.
2. **Where it lives** — which **home** runs the tool. The home is the *where*:
   - Upstream project CI (the project that owns the contribution ruleset gates each PR there).
   - Local driver / dev-tooling (the same gates run pre-merge on the contributor's machine, single-sourced with upstream CI).
   - Fork-local hooks (`commit-msg`, pre-push) plus fork PR CI.
   - Check's reviewer component (advisory model + tool scope).
   - Check's sign-off step (human at the result-document review).

**What and where are independent.** A given conformance tier may be implemented as code (covering "what") and live in upstream CI (covering "where") — but the same tier's implementation can *also* mirror locally, so "where" can be multiple homes for one "what". The two-axis framing makes the locations explicit instead of letting tooling drift to "wherever it was first written."

## The 5/5/1 × tooling-shape matrix

Each element of the 5/5/1 maps to a tooling shape, and each tool lands in one of Check's three components.

| 5/5/1 element | Tooling shape | Check component | Artifact written |
|---|---|---|---|
| **Correctness 1 — Spec** | the brief (no code) | (Plan output, Check input) | `brief.md` |
| **Correctness 2 — Reproduction** | fixture loader + repro runner; pre-fix red proof | Gates | row in `check-gates.json` |
| **Correctness 3 — Change** | the patch (no code) | (Do output, Check input) | `patch.diff` |
| **Correctness 4 — Verification** | the shipped test + regression suite | Gates | rows in `check-gates.json` |
| **Correctness 5 — Causal adequacy** | judgment (symptom vs. root cause) | Reviewer (advisory), human at sign-off | row in `check-review.md`; §6 NEEDS-HUMAN if unresolvable |
| **Conformance T1 — Structure** | structural validator (stdlib + filesystem + spec-format exec-shim) | Gates | rows in `check-gates.json` |
| **Conformance T2 — Shape** | shape scanner (semgrep, AST) | Gates | rows in `check-gates.json` |
| **Conformance T3 — Runtime** | dependency resolution (`find_spec`, install-and-import) + clean-env suite | Gates | rows in `check-gates.json` |
| **Conformance T4 — Contribution** | `commit-msg` hook, branch-target check, version-bump check | Gates (mostly fork-local + fork PR CI) | rows in `check-gates.json` |
| **Conformance T5 — Judgment** | scope, one-logical-fix, message-from-user-perspective | Reviewer (advisory), human at sign-off | row in `check-review.md`; §6 NEEDS-HUMAN if unresolvable |
| **Validation (1 act) — fitness-to-purpose** | "is this the right thing at all" | Reviewer (advisory), human at sign-off | row in `check-review.md`; §6 NEEDS-HUMAN; §9 sign-off |

Three observations the matrix makes explicit:

1. **Correctness 1 and 3 carry no tooling row** — they are *inputs* to Check (the brief from Plan, the patch from Do), not work Check performs. They appear in the matrix to keep the chain complete.
2. **Tiers 1–4 of conformance plus correctness steps 2 and 4** are the **gates path** — fully mechanical, fully automated, the only thing that blocks accept.
3. **Correctness step 5, Conformance Tier 5, and the validation act** are the **judgment path** — implemented by the cross-vendor reviewer model, finalised by the human at sign-off. The reviewer never gates; the human never edits the fix at Check time ([[01 - The Quality Cycle]] §Where the stages touch). The model/human split inside the cell is spelled out in [[#Inside the judgment cell — what the cross-vendor model decides and what only the human can]] below.

## Inside the judgment cell — what the cross-vendor model decides and what only the human can

C5, T5, and the validation act share a cell because they share a tool: a **cross-vendor reviewer model** (different family from the builder — e.g. Codex when the builder is Claude — see [[02 - Cycle Artifacts]] §Independence contract) that reads `{patch.diff, test, brief.md, check-gates}` and emits `PASS / FAIL / NEEDS-HUMAN` per item. The model **implements** the judgment cell — it does the work, it is not a courtesy second opinion — but it is advisory in effect because it never gates accept.

Inside the cell, items split into two structural categories:

- **Model-decidable items** — the reviewer attempts a `PASS / FAIL` from the artifacts alone. The criterion: a competent reader of `{patch, test, brief, check-gates}` could reach a defensible verdict without external context. Examples (project-specific list lives in the integration — see [[05 - Repository Integration]] §4): does the commit message describe behavior from the user's perspective; does the diff stay within one logical fix; does the shipped test exercise the changed code path; are any user-visible strings unwrapped that the T2 scanner did not catch.
- **Human-only items — the model emits `NEEDS-HUMAN` by design.** The criterion: the verdict requires context the reviewer structurally does not have, or judgment the project's ruleset deliberately reserves for the human. Generic always-human items:
  - **Validation fitness-to-purpose** — "is this the right thing at all" — depends on the bug report, project direction, and user impact, not on the artifacts. The validation act is human-only by definition.
  - **Symptom-vs-root-cause when the bug's mechanism is contested** — the reviewer can attempt causal adequacy, but when the patch could plausibly be either (a deeper fix or a top-layer mask), the model has no privileged way to choose and must flag.
  - **Upstream-isn't-ahead, semantic match** — the mechanical search (open PRs touching the same files) is automatable; deciding whether an open rewrite PR *supersedes* this fix needs project-direction context the reviewer lacks.
  - **Scope-creep / Plan re-entry calls** — when the diff exceeds the brief's stated scope but the excess looks plausible, only the human (who owns Plan) can decide whether to accept or iterate-to-Plan.
  - **Visual sign-off / manual repro outcomes** — anything that requires a human to look at a screen or run an OS-specific reproduction the gates cannot. Pre-flagged in `MANUAL-VERIFICATION.md` per `[[02 - Cycle Artifacts]]` §8.
  - **Project-defined human-only items** — items the per-repo integration (§Conformance ruleset) explicitly carves out as reviewer-cannot-decide. The integration MUST enumerate these so the model knows when to flag and the human knows what to look at.

Each `NEEDS-HUMAN` becomes a `[ ]` row in `SUMMARY.md` §6 with the reason the model could not decide. The human signing off Check clears each row before recording §9. An empty §6 means every judgment-cell item the model attempted came back `PASS` and no always-human item applied; a non-empty §6 is the explicit list of "what the human must look at because the model can't decide."

The split is not "model attempts and might fail" vs. "human reviews everything." It is "model decides what it can, structurally yields what it can't" — the items it yields are pre-known to the project (from the integration) so neither the model nor the human is left improvising the boundary at run time.

## Single-sourcing — one implementation, multiple invocations

The connection to [[03 - Cycle Automation]] §Where it runs is load-bearing: the gates that run locally during the cycle MUST be the same gates that re-run in CI as the merge-gate. This is enforced not by policy but by **single-sourcing the implementation**:

- One repository / module owns each tool (the structural validator, the shape scanner's rule file, the runtime checker, the contribution hooks, the correctness re-runners).
- The local driver invokes it with one command.
- CI invokes the *same* command (against the actual PR).
- No regex copy-pasted across YAML files, no parallel implementation in dev-tooling and CI both, no hand-maintained dependency lists in more than one place.

The anti-pattern this prevents: tooling drift between local and CI, where a contribution passes locally and fails in CI (or vice versa) because the two invocations are different code. Both invocations must read the same single source, so "passes locally" and "passes CI" collapse into the same fact.

## Homes — where each gate lives

Conformance Tier-by-tier home assignments differ by project, but the generic rationale follows a small set of rules:

| Home | Lives there because | Tools that fit |
|---|---|---|
| **Upstream project CI** | Gates every contribution PR; zero-config for contributors; canonical | T1 Structure, T3 Runtime — when the upstream project will host them |
| **Local driver / dev-tooling (mirror)** | Pre-merge feedback; runs the same gates the upstream CI runs; cycle's inner loop | Any gate that needs to run *before* a PR is opened — typically a mirror of T1/T3 + the project's correctness re-runners |
| **Local driver / dev-tooling (staging)** | Gates the project's CI doesn't host yet — staged until upstream accepts | T2 Shape (often semgrep, which an upstream may not yet depend on) |
| **Fork-local hooks** | Fire pre-commit / pre-push, before the artifact reaches a PR | T4 Contribution: `commit-msg` format, signing |
| **Fork PR CI** | Runs on PR open; gates branch-target, version-bump, etc. | T4 Contribution: branch-target, version-bump |
| **Check's reviewer component** | Judgment cells that can't be mechanized | C5 causal adequacy, T5 judgment, validation act (advisory) |
| **Check's sign-off step** | Final human call on judgment + clearing NEEDS-HUMAN | All of the reviewer's path, finalized |

**The home that does NOT exist:** there is no "Act home" for gates. Act improves the *rules* that gates enforce ([[01 - The Quality Cycle]] §Act); the gates themselves run in Check. A new rule lands as an addition to one of the homes above, recorded in `process/act-log.md`.

## Subject item dependencies

A contribution under cycle has a **subject** — the artifact being built or fixed in this PDCA pass (a patch, an addon, a plugin). The cycle's gates and reviewer evaluate that subject. They do *not* evaluate code the subject depends on — sister projects in the same workspace, third-party libraries the project ships against, the system toolchain. But during Plan, Do, or Check, dependency issues *will* surface: a repro implicates an upstream Gtk bug, the reviewer notices a sister project's API contract is broken, static analysis pointed at a dependency tree flags a real defect. This section is the **guideline for what the cycle does with those findings.**

The constant across both cases below: **the current cycle does not fix the dependency** — out-of-scope by definition — but it also does not silently drop the finding. "Noticed and abandoned" is not a valid disposition. The finding gets *proven first*, then handled differently depending on the relationship to the dependency.

### (1) Sister-project dependency — triage to a handoff

A repo you have contribution rights to and standing visibility into. Canonical pair: the testbed's addon work depending on `gramps` core; both are forks under the same owner.

The current cycle triages to the point of **handoff readiness**, in one of two shapes:

- **(a) Bug identified and proven.** A minimal reproduction with evidence — repro script, log, screenshot, pointer to the offending source path:line. Same evidence rigor Check applies to in-scope work; "looks suspicious" is not enough.
- **(b) A full spec is authored** — a `brief.md`-shape draft ready to enter the sister project's *own* PDCA cycle at a later point: defect, success criterion, branch target, scope, repro instruction, test requirement. The sister project's next Plan picks it up unchanged.

The cycle's output for the dependency is the handoff artifact (the proven repro or the draft brief), not a fix. **It is a hand-off point into the other project's cycle**, not work for the current cycle. The actual repair happens later in the sister project's own Plan/Do/Check/Act. Mechanically: a `handoff-<sister-repo>.md` attachment in the current bundle and a §10 Act candidate noting the handoff exists.

### (2) Pre-build dependency — proven, but the human decides

A library or system component the project ships against but does not contribute to. Canonical case: Gtk for Gramps, glibc, the Python runtime, a third-party PyPI package outside the project's control.

The evidence rigor is identical to case (1) — the bug or spec-gap MUST be proven with a repro before any disposition. What changes is the **next step**: there's no sister cycle to hand off to, so the **human at sign-off must decide what to do with the proven finding**. Common dispositions:

- File an issue upstream and ship the contribution without a workaround.
- Patch a defensive workaround into the contribution (scope question — usually → iterate-to-Plan because the brief didn't envision it).
- Pin or version-constrain the dependency.
- Document, accept, ship anyway.
- Wait.

The reviewer flags this as `NEEDS-HUMAN` per [[#Inside the judgment cell — what the cross-vendor model decides and what only the human can]]. The proven evidence lives in §6; the human's disposition lands in §9 (if it bears on accept) or §10 (if it's a process observation for the next Act).

### What the two cases share

- **Neither gates the current cycle's accept.** Out-of-scope means out-of-scope.
- **Proof is mandatory in both.** The whole point of the guideline is to keep the cycle from leaking "we noticed something" into archaeology layer for the next cycle; a finding without a repro is dropped, not deferred.
- **Findings surface anywhere in the cycle.** Plan (the triage already named a dependency cause), Do (the builder hit a dependency issue while implementing), Check (the reviewer flags it, the gates' suite implicates a dependency). The handling guideline is the same regardless of where it surfaced.

### Implication for the directory layout

Tooling that hunts for dependency findings lives separately from tooling that gates the current cycle. Sharing a directory (e.g., one `semgrep/` tree holding both contribution-conformance rules and dependency-bug-hunting rules) invites a dependency finding to be mis-promoted into a gate of the cycle — exactly the failure mode this guideline prevents. The worked example below shows the testbed's split.

## Worked example — Gramps testbed `agent-work/dev-tooling/`

The Gramps testbed instantiates the generic structure with two distinct kinds of tooling living next to each other:

- **In-scope conformance tooling** — gates and reviewer for the `addons-source` contribution under cycle. Ruleset: addon-dev guidelines / "doc 16". This is what the 5/5/1 above and the rest of this doc describes; it gates the addon PRs the testbed produces.
- **Dependency analysis tooling** — surfaces sister-project handoff candidates per [[#Subject item dependencies]] case (1). `gramps` core is a sister-project dependency of the addons under cycle (both forks under the same owner). Bug-hunting analyzers (None-flow, init-order, missing-disconnect) reproduce findings, which the cycle then hands off to a future `gramps`-core PDCA cycle — either as a proven repro or as a draft `brief.md`. Never gates the current addon cycle's accept. Pre-build dependencies (Gtk, glibc, etc. — case (2)) currently have no standing analyzers in the testbed; findings surface ad-hoc during Plan/Do/Check.

### Tier × home assignment (testbed slice of the in-scope conformance tooling)

| Tier | Representative rules | Mechanism | Home in this project | Status today |
|---|---|---|---|---|
| **1 — Structure** | folder==`id`; `gramps_target_version` present; `fname` resolves; no `__init__.py` in addon dir; `tests/__init__.py` exists; `po/template.pot` present; `TOOL` has `optionclass`; GPL header | stdlib + `.gpr.py` exec-shim + filesystem checks | **Upstream `addons-source` CI** (gates every addon PR); testbed mirror for pre-merge | Partly built upstream (PR #820's `test_plugin_registration.py`, `test_addon_dependencies.py`, the `po/template.pot` job) |
| **2 — Shape** | `_(f"...")`; `print()` diagnostics; `gramps.gui` / `plugins` imports from addons; `if cls is Person`; direct `pgettext`; `Optional[X]`; missing `DbTxn`; no `import register` in `.gpr.py` | **semgrep** (rule file + fixtures) | Testbed `agent-work/dev-tooling/` (staging; propose upstream once zero-FP-tuned) | Harness exists (used by the dependency-analysis tooling on `gramps` core); addon-conformance rules not yet written |
| **3 — Runtime** | `requires_mod` importable via `find_spec` (Pillow/PIL); `requires_gi` / `requires_exe` mapped; tests pass with deps absent (skip cleanly); GI pins match imports | Install + run in a clean env | **Upstream `addons-source` CI**; testbed mirror | Most mature: PR #820's `find_spec` gate, `run_addon_tests.py` degraded-skip, `addon_system_deps.py --unmapped` |
| **4 — Contribution** | commit summary ≤70 / wrap 80; trailer on last line; `#NNNN` issue refs; full-hash refs; branch target (addon→60 / core→61); no addon `version` bump in maintenance PR; no merge commits; `POTFILES.in` sync (core) | `commit-msg` hook (local) + PR CI (fork) | **The `gramps` and `addons-source` forks** — commits land there, not the testbed | Greenfield |
| **5 — Judgment** | **Model-decidable (Codex attempts PASS/FAIL):** user-perspective commit; one-logical-fix scope when the brief's scope is unambiguous; test actually exercises the fix; "wrap *every* user-visible string" beyond what T2 catches; upstream-isn't-ahead *mechanical* search (open PRs touching the same files). **Human-only (Codex emits NEEDS-HUMAN by design):** symptom-vs-root-cause when the bug's mechanism is contested; upstream-isn't-ahead *semantic* match (does an open rewrite PR supersede this fix); scope-creep judgment when the diff exceeds the brief's stated scope but the excess looks plausible (Plan re-entry call); visual sign-off / Windows-only manual repro outcomes (`MANUAL-VERIFICATION.md`); validation fitness-to-purpose ("is this the right thing at all"). | cross-vendor reviewer (Codex) implements the cell; human at sign-off finalises NEEDS-HUMAN and the disposition | **Check's reviewer + sign-off components** ([[03 - Cycle Automation]]; see §Inside the judgment cell above) | The reviewer-contract thread (cross-vendor, decorrelated, implementing — not opining) |

### Correctness chain (testbed slice)

| Step | Implementation | Home |
|---|---|---|
| 2 — Reproduction | `tests/interface/*` (dogtail), `example.gramps` fixture | Local driver + CI (`interface-tests.yml`) |
| 4 — Verification | the shipped test (per cycle) + existing suite (`tests/`, `gramps/*_test.py`) | Local driver + CI (`unit-tests.yml`, `addon-unit-tests.yml`) |
| 5 — Causal adequacy | reviewer (Codex) implements (PASS when the patch's mechanism plausibly explains the observed defect from the artifacts alone; NEEDS-HUMAN when the bug's mechanism is contested or the fix could be either root-cause or symptom-mask) + human sign-off | Check's reviewer + sign-off |

### Directory layout — dependency analysis sits next to conformance tooling, not within it

`agent-work/dev-tooling/` is organised so the in-scope conformance tooling and the dependency-analysis tooling stay clearly separate, per [[#Implication for the directory layout]]:

```
agent-work/dev-tooling/
  core-analysis/             # DEPENDENCY ANALYSIS — out-of-scope: gramps core, a
                             #   sister-project dependency of addons under cycle.
                             #   Findings hand off to a future gramps-core PDCA
                             #   cycle (proven repro or draft brief); NEVER gate
                             #   the current addon cycle.
    pyright/                 #   None-flow            (existing)
    semgrep/                 #   core bug-hunting rules incl. connect-without-disconnect
    codeql/                  #   reserved flow        (existing NOTES)
    README.md                #   "subject = core (out-of-scope sister-project dep); NOT addon-dev conformance"
  addon-conformance/         # IN-SCOPE CONFORMANCE — gates and reviewer for
                             #   addons-source contributions under cycle.
    lib/                     #   shared .gpr.py exec-shim + requires_mod extractor (single-sourced)
    tier1-structure/         #   stdlib + exec-shim + fs    (TESTBED MIRROR of upstream)
    tier2-shape/             #   semgrep addon rules + fixtures (staging pre-upstream)
    README.md                #   "canonical home = addons-source CI; this mirrors it"
  pre-commit/                # hooks (existing) — Tier-4 local + analyzer pre-commits
  ide/                       # vscode/ + claude-commands/ (existing)
  README.md                  # this matrix; what is NOT here (T1/3 upstream, T4 forks, T5 process)
```

Names are a proposal, not the point. The point: dependency analysis stays whole and clearly labelled as out-of-scope (handoff source, not a gate); in-scope conformance is tiered and explicitly labeled a *mirror* of its upstream home; the shared exec-shim library has one location so single-sourcing has a place to point.

## Build order (concrete deliverables, per [[03 - Cycle Automation]])

1. **The gates, single-sourced** — structural validator (T1 exec-shim + T2 semgrep), runtime gate (T3 `find_spec` + clean-env suite), correctness re-runners (repro, verification, regression), T4 commit-msg + branch-target + version-bump hooks. Each callable identically by the local driver and by CI.
2. **The driver** (in 03) — calls the gates, withholds `build-notes.md` from the reviewer, assembles `SUMMARY.md`.
3. **The contribution-batch fan-out** (in 03) — uses the gates over N issues.
4. **The reviewer's `AGENTS.md`** (in 03) — fixes the judgment-path shape for C5, T5, validation.

The gates are the long pole because both the local driver and the CI re-gate depend on them existing as single-sourced code. Until they exist, Check cannot run unattended and the body cannot fan out.

## What this doc is not

This doc does not specify the project's *conformance rules* (those are the per-repo specification — [[06 - Quality Cycle Guidelines]] §Precondition; in the Gramps worked example, the "doc 16" addon-dev guidelines). It documents the **tooling axis** — what implements Check, where each piece lives, how single-sourcing connects local and CI — so a project adopting the cycle can plan its build order without ambiguity about which gate goes where.

The rules themselves are subject to Act ([[01 - The Quality Cycle]] §Act): when a rule needs adding, retiring, relaxing, or tightening, that change lands as an Act delta in `process/act-log.md` and modifies the per-repo specification. The tooling that *applies* the rules — this doc's subject — is downstream of the rules themselves and changes only when a rule's home moves, its mechanism changes, or single-sourcing introduces a new shared component.
