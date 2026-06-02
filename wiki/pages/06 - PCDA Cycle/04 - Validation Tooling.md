---
title: "Validation Tooling — what implements Check, and where it lives"
categories: []
managed: false
status: active
---

> The Check beat ([[01 - The Quality Cycle]] §Check) has internal
> structure — the **5 / 5 / 1** (correctness chain, conformance stack,
> validation act) — and runs through three **components** (gates,
> reviewer, sign-off — see [[03 - Cycle Automation]] §Check). This doc
> documents the code and process that *implements* those components:
> which tool covers which 5/5/1 element, where that tool lives, and
> how single-sourcing keeps the driver and CI invoking the same
> implementation. Worked example uses the Gramps testbed at the end;
> the structure is project-agnostic. Living document.

## What "validation tooling" means here

"Validation tooling" is shorthand for **the implementation of Check's
deterministic gates and advisory reviewer.** Check has three
components:

- **Gates** (deterministic, full automation) — the validators, rule
  scanners, suite runners, and hooks that produce `check-gates.json`.
- **Reviewer** (advisory, full automation) — the cross-vendor model
  that grounds the gate evidence, re-runs the asserted red/green, and
  emits per-item `PASS / FAIL / NEEDS-HUMAN` into `check-review.md`.
- **Sign-off** (instrumented, human) — the human completes Check by
  reading the assembled `SUMMARY.md` and recording §9.

This doc is about the **gates** and **reviewer**. Sign-off is human
work whose tooling is the result-document presentation in
[[02 - Cycle Artifacts]] / [[03 - Cycle Automation]] §Check sign-off,
not the subject here.

## Two axes — what and where

Validation tooling decomposes along two orthogonal axes:

1. **What it evaluates** — which element of Check's 5/5/1 it covers.
   The 5/5/1 is the *what*:
   - Correctness chain (5 steps): spec → reproduction → change →
     verification → causal adequacy.
   - Conformance stack (5 tiers): structure → shape → runtime →
     contribution → judgment.
   - Validation (1 act): fitness-to-purpose.
2. **Where it lives** — which **home** runs the tool. The home is the
   *where*:
   - Upstream project CI (the project that owns the contribution
     ruleset gates each PR there).
   - Local driver / dev-tooling (the same gates run pre-merge on the
     contributor's machine, single-sourced with upstream CI).
   - Fork-local hooks (`commit-msg`, pre-push) plus fork PR CI.
   - Check's reviewer component (advisory model + tool scope).
   - Check's sign-off step (human at the result-document review).

**What and where are independent.** A given conformance tier may be
implemented as code (covering "what") and live in upstream CI
(covering "where") — but the same tier's implementation can *also*
mirror locally, so "where" can be multiple homes for one "what". The
two-axis framing makes the locations explicit instead of letting
tooling drift to "wherever it was first written."

## The 5/5/1 × tooling-shape matrix

Each element of the 5/5/1 maps to a tooling shape, and each tool
lands in one of Check's three components.

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

1. **Correctness 1 and 3 carry no tooling row** — they are *inputs* to
   Check (the brief from Plan, the patch from Do), not work Check
   performs. They appear in the matrix to keep the chain complete.
2. **Tiers 1–4 of conformance plus correctness steps 2 and 4** are the
   **gates path** — fully mechanical, fully automated, the only thing
   that blocks accept.
3. **Correctness step 5, Conformance Tier 5, and the validation act**
   are the **judgment path** — the reviewer attempts each advisory,
   then the human signs off in §9. The reviewer never gates; the human
   never edits the fix at Check time
   ([[01 - The Quality Cycle]] §Where the stages touch).

## Single-sourcing — one implementation, multiple invocations

The connection to [[03 - Cycle Automation]] §Where it runs is
load-bearing: the gates that run locally during the cycle MUST be the
same gates that re-run in CI as the merge-gate. This is enforced not
by policy but by **single-sourcing the implementation**:

- One repository / module owns each tool (the structural validator,
  the shape scanner's rule file, the runtime checker, the
  contribution hooks, the correctness re-runners).
- The local driver invokes it with one command.
- CI invokes the *same* command (against the actual PR).
- No regex copy-pasted across YAML files, no parallel implementation
  in dev-tooling and CI both, no hand-maintained dependency lists in
  more than one place.

The anti-pattern this prevents: tooling drift between local and CI,
where a contribution passes locally and fails in CI (or vice versa)
because the two invocations are different code. Both invocations must
read the same single source, so "passes locally" and "passes CI"
collapse into the same fact.

## Homes — where each gate lives

Conformance Tier-by-tier home assignments differ by project, but the
generic rationale follows a small set of rules:

| Home | Lives there because | Tools that fit |
|---|---|---|
| **Upstream project CI** | Gates every contribution PR; zero-config for contributors; canonical | T1 Structure, T3 Runtime — when the upstream project will host them |
| **Local driver / dev-tooling (mirror)** | Pre-merge feedback; runs the same gates the upstream CI runs; cycle's inner loop | Any gate that needs to run *before* a PR is opened — typically a mirror of T1/T3 + the project's correctness re-runners |
| **Local driver / dev-tooling (staging)** | Gates the project's CI doesn't host yet — staged until upstream accepts | T2 Shape (often semgrep, which an upstream may not yet depend on) |
| **Fork-local hooks** | Fire pre-commit / pre-push, before the artifact reaches a PR | T4 Contribution: `commit-msg` format, signing |
| **Fork PR CI** | Runs on PR open; gates branch-target, version-bump, etc. | T4 Contribution: branch-target, version-bump |
| **Check's reviewer component** | Judgment cells that can't be mechanized | C5 causal adequacy, T5 judgment, validation act (advisory) |
| **Check's sign-off step** | Final human call on judgment + clearing NEEDS-HUMAN | All of the reviewer's path, finalized |

**The home that does NOT exist:** there is no "Act home" for gates.
Act improves the *rules* that gates enforce ([[01 - The Quality Cycle]]
§Act); the gates themselves run in Check. A new rule lands as an
addition to one of the homes above, recorded in `process/act-log.md`.

## Two rule families (project-agnostic)

Validation tooling typically splits into two families that share tools
but must not be merged in the layout:

- **Family A — project-guideline conformance.** The project's own
  written ruleset for contributions to itself. Subject: contribution
  artifacts (patches, packages, addons, plugins) against the project's
  written rules. The 5/5/1 above (especially the conformance stack) is
  Family A.
- **Family B — upstream-defect analysis.** Bug-hunting analyzers
  against the source the *project depends on*. Subject: upstream code;
  findings become *upstream* PRs, not contributions to this project.
  Family B uses the same tool families (semgrep, type-checkers, flow
  analysis) but its rules and rule-targets differ.

The split matters because Family B's analyzers ARE NOT conformance
checks. A semgrep rule that hunts for missing `disconnect()` in
upstream Gtk code is a bug-hunting rule, not a "Tier 2 shape" rule
under the project's own conformance stack. Sharing a layout collapses
the distinction; keeping them in separate directories preserves it.

## Worked example — Gramps testbed `agent-work/dev-tooling/`

The Gramps testbed instantiates this generic structure as follows.
References:
- Family A = `addons-source` conformance (the addon-dev guidelines /
  "doc 16" ruleset).
- Family B = `gramps` core defect analysis (None-flow, init-order,
  missing-disconnect).

### Tier × home assignment (testbed slice of Family A)

| Tier | Representative rules | Mechanism | Home in this project | Status today |
|---|---|---|---|---|
| **1 — Structure** | folder==`id`; `gramps_target_version` present; `fname` resolves; no `__init__.py` in addon dir; `tests/__init__.py` exists; `po/template.pot` present; `TOOL` has `optionclass`; GPL header | stdlib + `.gpr.py` exec-shim + filesystem checks | **Upstream `addons-source` CI** (gates every addon PR); testbed mirror for pre-merge | Partly built upstream (PR #820's `test_plugin_registration.py`, `test_addon_dependencies.py`, the `po/template.pot` job) |
| **2 — Shape** | `_(f"...")`; `print()` diagnostics; `gramps.gui` / `plugins` imports from addons; `if cls is Person`; direct `pgettext`; `Optional[X]`; missing `DbTxn`; no `import register` in `.gpr.py` | **semgrep** (rule file + fixtures) | Testbed `agent-work/dev-tooling/` (staging; propose upstream once zero-FP-tuned) | Harness exists (used by Family B); addon rules not yet written |
| **3 — Runtime** | `requires_mod` importable via `find_spec` (Pillow/PIL); `requires_gi` / `requires_exe` mapped; tests pass with deps absent (skip cleanly); GI pins match imports | Install + run in a clean env | **Upstream `addons-source` CI**; testbed mirror | Most mature: PR #820's `find_spec` gate, `run_addon_tests.py` degraded-skip, `addon_system_deps.py --unmapped` |
| **4 — Contribution** | commit summary ≤70 / wrap 80; trailer on last line; `#NNNN` issue refs; full-hash refs; branch target (addon→60 / core→61); no addon `version` bump in maintenance PR; no merge commits; `POTFILES.in` sync (core) | `commit-msg` hook (local) + PR CI (fork) | **The `gramps` and `addons-source` forks** — commits land there, not the testbed | Greenfield |
| **5 — Judgment** | user-perspective commit; one-logical-fix scope; symptom-vs-root-cause; test actually exercises the fix; "wrap *every* user-visible string"; upstream-isn't-ahead (semantic) | human + advisory cross-vendor reviewer (Codex) | **Check's reviewer + sign-off components** ([[03 - Cycle Automation]]) | The reviewer-contract thread (advisory, decorrelated) |

### Correctness chain (testbed slice)

| Step | Implementation | Home |
|---|---|---|
| 2 — Reproduction | `tests/interface/*` (dogtail), `example.gramps` fixture | Local driver + CI (`interface-tests.yml`) |
| 4 — Verification | the shipped test (per cycle) + existing suite (`tests/`, `gramps/*_test.py`) | Local driver + CI (`unit-tests.yml`, `addon-unit-tests.yml`) |
| 5 — Causal adequacy | reviewer (Codex) + human sign-off | Check's reviewer + sign-off |

### Two families in the layout

`agent-work/dev-tooling/` reorganized by *family* (instead of by tool) keeps the
two distinct:

```
agent-work/dev-tooling/
  core-analysis/             # FAMILY B — subject: gramps CORE; findings → core PRs
    pyright/                 #   None-flow            (existing)
    semgrep/                 #   core bug-hunting rules incl. connect-without-disconnect
    codeql/                  #   reserved flow        (existing NOTES)
    README.md                #   "subject = core; NOT addon-dev conformance"
  addon-conformance/         # FAMILY A — subject: addons-source; addon-dev tiers
    lib/                     #   shared .gpr.py exec-shim + requires_mod extractor (single-sourced)
    tier1-structure/         #   stdlib + exec-shim + fs    (TESTBED MIRROR of upstream)
    tier2-shape/             #   semgrep addon rules + fixtures (staging pre-upstream)
    README.md                #   "canonical home = addons-source CI; this mirrors it"
  pre-commit/                # hooks (existing) — Tier-4 local + analyzer pre-commits
  ide/                       # vscode/ + claude-commands/ (existing)
  README.md                  # this matrix; what is NOT here (T1/3 upstream, T4 forks, T5 process)
```

Names are a proposal, not the point. The point: Family B stays whole
and clearly upstream-source-subject; Family A is tiered and explicitly
labeled a *mirror* of its upstream home; the shared exec-shim library
has one location so single-sourcing has a place to point.

## Build order (concrete deliverables, per [[03 - Cycle Automation]])

1. **The gates, single-sourced** — structural validator (T1 exec-shim
   + T2 semgrep), runtime gate (T3 `find_spec` + clean-env suite),
   correctness re-runners (repro, verification, regression), T4
   commit-msg + branch-target + version-bump hooks. Each callable
   identically by the local driver and by CI.
2. **The driver** (in 03) — calls the gates, withholds `build-notes.md`
   from the reviewer, assembles `SUMMARY.md`.
3. **The contribution-batch fan-out** (in 03) — uses the gates over N
   issues.
4. **The reviewer's `AGENTS.md`** (in 03) — fixes the judgment-path
   shape for C5, T5, validation.

The gates are the long pole because both the local driver and the CI
re-gate depend on them existing as single-sourced code. Until they
exist, Check cannot run unattended and the body cannot fan out.

## What this doc is not

This doc does not specify the project's *conformance rules* (those are
the per-repo specification — [[06 - Quality Cycle Guidelines]]
§Precondition; in the Gramps worked example, the "doc 16" addon-dev
guidelines). It documents the **tooling axis** — what implements
Check, where each piece lives, how single-sourcing connects local and
CI — so a project adopting the cycle can plan its build order without
ambiguity about which gate goes where.

The rules themselves are subject to Act
([[01 - The Quality Cycle]] §Act): when a rule needs adding, retiring,
relaxing, or tightening, that change lands as an Act delta in
`process/act-log.md` and modifies the per-repo specification. The
tooling that *applies* the rules — this doc's subject — is downstream
of the rules themselves and changes only when a rule's home moves,
its mechanism changes, or single-sourcing introduces a new shared
component.
