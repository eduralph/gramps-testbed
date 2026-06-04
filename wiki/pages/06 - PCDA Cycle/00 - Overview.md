---
title: "Quality Cycle — Overview"
categories: []
managed: false
status: active
---

## Purpose

A working reference for the **PDCA quality cycle** used in this project, and portable to any project where one contribution turns one cycle. Written for the human who authors specs (Plan) and improves the process (Act), for future Claude instances running the contribution work (Do and most of Check), and for anyone wanting to adopt the same cycle elsewhere.

**Built vs. planned.** Docs 01–02 describe the *model* and the *artifacts*; doc 03 describes the *automation*. Most of the automation described in 03 is **planned**, not built — see the maturity legend at the top of [[03 - Cycle Automation]] and the status-today column in [[04 - Validation Tooling]]'s tier matrix. The pipeline as a whole sits at L1 today (scripted handoff: the agent-work scaffolding under `agent-work/scripts/` and `agent-work/templates/` produces bundle directories and brief drafts; everything beat-side runs by hand). The model holds; the orchestration is staged.

## The cycle in one paragraph

One contribution turns one PDCA cycle: **Plan** (author the spec) → **Do** (implement) → **Check** (verify the built artifact — correctness, conformance, *and* validation, all against the spec) → **Act** (process improvement: adjust the spec template, ruleset, gates, or agent skills so the issues this cycle exposed do not recur) → back to **Plan** with a better baseline. Plan + Do + Check operate on the **contribution** (this bug, this fix); Act operates on the **process** (the ruleset, the template, the workflow). The next Do should not recreate the issues the previous Act tried to eliminate — if it does, the Act was not effective.

## Three layers

The cycle is documented in three layers, increasing in concreteness. Read them in order if new, or jump to the layer matching the question you have:

1. [[01 - The Quality Cycle]] — **the model**. PDCA, the four beats as the four roles, the seam between contribution work and process work, the 5/5/1 anatomy inside Check (5-step correctness chain, 5-tier conformance stack, 1 indivisible validation act), and Plan's scale range — from a one-fix `brief.md` to a multi-part design proposal (GEPS-shape) that spawns N child cycles. Answers *what shape is this*.
2. [[02 - Cycle Artifacts]] — **the operational layer**. The concrete files each beat produces: `brief.md`, `patch.diff`, `build-notes.md`, `check-gates`, `check-review.md`, the nine-section `SUMMARY.md` ending in a Check sign-off; the separate `act-notes.md` for process deltas. The independence contract. Answers *what gets written, when, by whom*.
3. [[03 - Cycle Automation]] — **the orchestration layer**. The driver as a state machine over the bundle; deterministic gates as the only blocking path; the two model leaves (builder + advisory reviewer) invoked from inside scripted control flow. Two human-instrumented passes (Plan-author and Check-signoff per cycle; Act across a batch of cycles). Maturity ladder L1/L2/L3. Answers *how the body runs unattended without automating the human work away*.

## Where the validation tooling sits

The Check beat's conformance stack has five tiers, and they do **not** all live in one place — each tier has a *home* matched to where the check gates the most work. The matrix and the build order are in:

- [[04 - Validation Tooling]] — tier × home decomposition, two rule families (project-conformance vs. upstream-defect-analysis), proposed layout. Worked example uses the Gramps testbed's `agent-work/dev-tooling/` but the structure generalizes.

## How a specific repo integrates with the cycle

The generic cycle is project-agnostic. To **run** it against a specific repository, the repository MUST provide a small set of concretizations — a **repository-integration specification** that slots into the generic cycle and supplies the project-specific details the cycle's beats need at runtime.

- [[05 - Repository Integration]] — what each repo provides to integrate with the cycle: bug-tracking integration, branch-target rules, canonical reproduction fixtures, conformance ruleset and gate homes, upstream-isn't-ahead routine, brief/design-proposal templates, result-bundle path conventions, committing conventions, repo-specific scripts and tooling, per-repo P-/D-/C-/A- extensions, and maintainer/governance specifics. Includes a worked example mapping these required items to the testbed's `CLAUDE.md` and `agent-work/` tree (the consolidated home for all cycle artifacts).

A repo running the cycle without writing its integration spec is running on **tribal knowledge** — the exact failure mode the cycle exists to eliminate.

## Operational discipline (per-beat rules)

[[06 - Quality Cycle Guidelines]] holds the per-beat MUST / SHOULD / MAY rules (RFC 2119 style) that govern how each beat is run well. Numbered per beat (P-, D-, C-, A-) so review comments and PR threads can cite e.g. "P3" or "C6 violated — §6 has open items" unambiguously. Plan reads the [[05 - Repository Integration]] for its repo-specific inputs (P11); Check applies the per-repo conformance ruleset (C11). The conflict-resolution rule between generic and per-repo: generic wins on cycle shape; per-repo wins on instantiation ([[06 - Quality Cycle Guidelines]] §Precondition).

## The cycle in action

[[07 - Case Study - CI Hardening]] carries two parallel worked examples:

- **Brief-shaped Plan** — one PDCA cycle, three turns deep, on the testbed CI itself. Plan (v1 brief, seven items) → in-cycle spec revision after builder review (v2) → mixed Check completion / Act-class process delta (v3). Shows where contribution-iteration (re-Plan or re-Do within the same cycle) ends and process-improvement (Act) begins.
- **Design-shaped Plan** — GEPS 049 (*Versioned Addon API surface and 2 axis lifecycle model*) as a multi-part design proposal: one Plan artifact that specs four coupled changes across a four-phase migration and will spawn N child briefs at implementation time. Demonstrates the design-proposal sections (Goals/Non-goals, Objections and responses, Impact assessment, De-risking, Open questions, Future Work) and Plan-internal grounding investigations.

## Changelog

- 2026-06-02 — initial documentation set built from Folds2 source.
