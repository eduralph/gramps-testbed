---
title: "Repository Integration — what each repo provides to plug into the cycle"
categories: []
managed: false
status: active
---

> The generic PDCA quality cycle (docs 01–04, 06) is project-agnostic by design. To **run** it against a specific repository, that repository MUST provide a small set of concretizations — a **repository-integration specification** that slots into the generic cycle and supplies the project-specific details the cycle's beats need at runtime. This doc enumerates **only what is strictly repo-specific**. Anything the generic cycle docs already cover — the model, the artifact shape, the orchestration, the per-beat rules — is *not* in the integration. The integration is the project's answer to a small set of "which / where / how" questions the generic docs deliberately leave open. Living document.

## What the integration is, and what it is not

**The integration IS** the project's answer to questions of the form:

- *Which* tracker / branches / fixtures / rules / templates apply to this repo?
- *Where* do the cycle's gates and artifacts live in this project?
- *How* are the project's specific scripts and runners invoked?

**The integration IS NOT** a restatement of the generic cycle. It does not redefine Plan/Do/Check/Act, does not re-document the artifact shape ([[02 - Cycle Artifacts]]), does not re-state the per-beat rules ([[06 - Quality Cycle Guidelines]]), does not re-describe the tier × home decomposition ([[04 - Validation Tooling]]). When the integration needs to refer to those, it cites them.

The integration's relationship to the generic docs is **read by**, not **replace**:

- Plan reads it for repo-specific inputs (P11 instantiation).
- Check reads it for the active conformance ruleset and gate homes (C11 instantiation).
- Act maintains it as part of the process baseline (A6 append-only, per [[06 - Quality Cycle Guidelines]] §Precondition).

Conflict resolution between the integration and the generic docs follows [[06 - Quality Cycle Guidelines]] §Precondition R3: **generic wins on shape; integration wins on instantiation.**

## What the integration MUST cover

Each item below is strictly repo-specific — the generic cycle docs cannot answer it without becoming useless for other projects. Each item names the rule(s) it instantiates so the integration with the rest of the doc set is explicit.

### 1. Tracker integration

Instantiates the project's tracker mechanics. Read by Plan during triage and by the writer of `tracker-comment.md` (always required per [[02 - Cycle Artifacts]] §SUMMARY.md §8). Integration MUST declare:

- **Tracker system and URL** (e.g. MantisBT at `gramps-project.org/bugs`; GitHub Issues at `org/repo`; Jira project key).
- **Issue-ID format** as it appears in briefs, commits, and PRs (e.g. `13418`, `#13418`, `MANT-13418`, `gh-12345`).
- **Cross-link form into the tracker from a commit or PR** — the project's actual citation pattern (e.g. `p:gramps:nnnn:` for Gramps' Mantis instance; `Fixes #nnnn` for GitHub Issues).
- **Status field names and the per-disposition mapping** — which tracker statuses correspond to which cycle dispositions (acknowledged / confirmed / feedback / assigned / resolved → cycle Plan-time and Check-time states).
- **Per-release field** (e.g. "Fixed in version") the cycle updates on a fix.
- **The project's tracker-comment voice and template path** — the template `agent-work/templates/tracker-comment.md.tpl` for the testbed; one per project. Cite the specific path.

### 2. Branch-target rules

Instantiates [[06 - Quality Cycle Guidelines]] P4. Integration MUST declare:

- **The per-area branch map** (e.g. core fixes → `maintenance/gramps61`; addon fixes → `maintenance/gramps60` + forward cherry-pick; testbed → `main`).
- **Override convention** — where reviewer-specific override instructions are recorded when they exist (typically the PR review thread).
- **Cross-version cherry-pick rules** if the project has them (direction, label, who picks).
- **The master-vs-maintenance rule** for this project's release model (cite the project's own statement of it).

### 3. Reproduction fixtures and runners

Instantiates [[06 - Quality Cycle Guidelines]] P1 (the canonical reproduction). Integration MUST declare:

- **The canonical fixture path** (e.g. `example.gramps` for Gramps).
- **The project-specific runner script(s) and their commands** — the actual scripts the cycle invokes, **with paths**:
  - Reproduction: e.g. `agent-work/scripts/ubuntu/run-interface.sh`, `agent-work/scripts/windows/run-unit.sh` (testbed Linux/Windows splits).
  - Verification: the project's test runner (`make test`, `pytest`, `cargo test`, `./make.py test`, etc.).
- **Platform variants** if the project supports multiple platforms (Linux containerized vs Windows MSYS2; macOS notes if any).
- **What counts as "successful repro"** in this project — exit code, log marker, screenshot, UI assertion.

### 4. Conformance ruleset — bound to 04 and 06

This section is the most load-bearing integration point with the rest of the doc set. The integration does NOT re-document the tier × home decomposition (that is [[04 - Validation Tooling]]). The integration's job is to **answer 04's matrix** for this repo and **bind it to** [[06 - Quality Cycle Guidelines]] C11 (Check applies the per-repo conformance ruleset at the homes the integration designates).

For each Tier 1–5 ([[04 - Validation Tooling]] §5/5/1 × tooling-shape matrix), integration MUST declare:

- **The project's written ruleset** that Tier consumes — point at the project's own contributor guidelines, addon-dev doc, PEP, RFC, code-of-conduct, etc. The integration does not RESTATE the rules; it cites the document that owns them.
- **The home** for that Tier in this repo ([[04 - Validation Tooling]] §Homes — where each gate lives): upstream CI, local dev-tooling mirror or staging, fork-local hooks, fork PR CI, or Check's reviewer / sign-off.
- **The single-sourced invocation command** the driver runs and CI runs (the same impl, per [[04 - Validation Tooling]] §Single-sourcing). Cite the *script or module path* explicitly.
- **Any project-specific extension rules** prefixed per the integration's repo prefix (e.g. `gramps-T1-gpr-fields`). These tighten or add to the generic Tier rules without weakening any.

For Tier 5 (judgment), the integration names the project's reviewer contract: which **cross-vendor model family** runs the reviewer (different from the builder's family, by the [[02 - Cycle Artifacts]] §Independence contract), the `AGENTS.md` / `SKILL.md` path, the `.claude/agents/` subagent scopes if they exist (or "[planned]" if they do not yet — see [[03 - Cycle Automation]] §Do for the maturity-tag convention). The integration MUST also enumerate the **project-defined human-only items** ([[04 - Validation Tooling]] §Inside the judgment cell) — the T5 (and C5, validation-act) items the reviewer must emit `NEEDS-HUMAN` on by design rather than attempt a PASS/FAIL. This is the "what the human must look at because the model can't decide" list for this project; without it the reviewer has no project-specific list to defer on and the human has no project-specific list to expect.

**The conformance ruleset entry is the integration's "this is what 04's matrix means in this project" answer.** A reader of [[04 - Validation Tooling]] should be able to come here and find, for each cell of 04's matrix, the concrete file path and command this project uses.

### 5. Upstream-isn't-ahead routine

Instantiates [[06 - Quality Cycle Guidelines]] P8. Integration MUST declare:

- **What "upstream" is** for this project — canonical URL, relevant branches, fork relationship.
- **The project-specific search routine** — which trackers to consult, which PR search patterns work, tokenization gotchas. Gramps' is recorded in `CLAUDE.md` as the search-by-affected-file-path rule; cite the equivalent for this project.
- **The merged-history check command** — the actual `git log` or `gh search` invocation the cycle uses.

### 6. Brief and design-proposal templates

Instantiates [[02 - Cycle Artifacts]] §PLAN (the brief shape) and [[01 - The Quality Cycle]] §Solution-approach design (the design-proposal shape) for this project. Integration MUST declare:

- **The brief template path(s)** the project's scaffolder reads from (e.g. `agent-work/templates/SUMMARY.md.tpl`, `agent-work/templates/exit-brief.md.tpl`, `agent-work/templates/increment-brief.md.tpl` in the testbed).
- **The design-proposal template path** if the project supports design-shaped Plans (a GEPS template, an RFC template, etc.). "[planned]" if none yet.
- **Any required project-specific frontmatter or sections** the brief MUST include beyond the generic spec.

### 7. Bundle and act-log paths

Instantiates [[02 - Cycle Artifacts]] §Bundle layout. Integration MUST declare:

- **Bundle root and ID format** (e.g. `agent-work/results/<batch>/issue_<mantis-id>/` in the testbed).
- **The Act log path** (e.g. `process/act-log.md`) — or "[planned]" with a recommended path if not yet established.
- **Where versioned briefs live on iterate-to-Plan** (default: `brief.vN.md` in the bundle root; the integration can override).

### 8. Committing and PR conventions

Instantiates Tier 4 ([[04 - Validation Tooling]]). Integration MUST declare:

- **Commit-message format** — subject length, wrap column, trailer format, required references.
- **PR description format** — the project's expected sections (the testbed's `CLAUDE.md` has "Root cause / Fix / Verified against / Test").
- **Enforcement mechanism** — which checks fire via commit-msg hook (fork-local), which via fork PR CI, which catch at human review.

### 9. Repo-specific scripts and tooling

The integration MUST list **the project-specific code the cycle invokes**. These scripts are themselves repo-specific (a different project will have different scripts implementing the same cycle roles), so they belong in the integration rather than the generic docs. Integration MUST declare each as **role → script path + invocation + status**:

- **Tracker scrape / handoff generator** — e.g. in the testbed, `agent-work/scripts/make_handoff.py` scrapes MantisBT and emits draft briefs. A project with a different tracker (Jira, GitHub Issues) needs its own scraper at the same role.
- **Tracker-comment template** — `agent-work/templates/tracker-comment.md.tpl` is the testbed's; per-tracker conventions differ in voice and required fields.
- **Per-platform repro runners** — already listed under item 3; cross-reference there.
- **Conformance gate runners** — the actual scripts that 04's matrix points at (validator, semgrep, suite runner, hooks). Already listed under item 4; cross-reference there.
- **Corpus / extraction tools** — e.g. `agent-work/dev-tooling/claude-commands/extract_corpus.py` for the testbed, which reads frozen bundles. Optional per-project.
- **Any other cycle-specific code** the project maintains — layout linters, addon validators, build helpers used by Check, etc.

**This list IS the integration's accountability for cycle code.** Items not on the list are either (a) generic cycle code that lives in the quality-cycle docs / driver (out of scope for the integration), or (b) missing — i.e. **[planned]**, which the integration should mark honestly so the next Act review can see the gap.

### 10. Maintainer and governance specifics

Integration MUST declare:

- **Who reviews** — solo / team / per-area reviewer assignment.
- **The project's ready-mark gate** — who marks PRs ready and what convention precedes the mark (e.g. the testbed's "Eduard re-reads with fresh eyes" rule).
- **External-contribution flow differences** — fork PR vs same-owner branch PR if they materially differ.
- **The MAINTAINERS file** or equivalent.

### 11. Per-repo P- / D- / C- / A- extensions (if any)

Integration MAY add repo-prefixed rules that tighten or add to a generic rule for this project (e.g. `gramps-P1`, `testbed-C7`). If the integration adds any:

- **Declare the prefix convention** for this project.
- **List the rules**, one per section per beat (P-, D-, C-, A-).
- **Acknowledge non-weakening** — the rules tighten or add only; none deletes or weakens a generic rule ([[06 - Quality Cycle Guidelines]] §Precondition).

If no extensions, the section says so.

## Optional items the integration SHOULD cover

Brief list — these aid the cycle's usability without being load-bearing:

- **Integration maturity status per item** (which items are fully specified vs partial vs not yet — so Act can see the gaps).
- **Project-specific dispositions** beyond the generic set.
- **Testing platform matrix** (which platforms a fix is "verified" against — used by `SUMMARY.md` §7 to be honest about coverage).
- **Skills / agent files** — pointers to `SKILL.md` (builder), `AGENTS.md` (reviewer), `.claude/agents/*`.

## Discovery — where the integration lives

The cycle's scaffolder MUST be pointed at a **single entry point** that either contains the integration or links to its parts. Common choices: `AGENTS.md`, `CLAUDE.md`, `docs/quality-cycle.md`. A structured `integration/` directory works as long as one entry point delegates to the others.

The format (Markdown, JSON, YAML, structured directory) is the project's choice; consistency within one project matters more than the format choice.

## Maintenance

Per [[06 - Quality Cycle Guidelines]] §Precondition: the integration is process-baseline material maintained by Act. Updates land as act-log entries (A6 append-only). A1 (no Act mid-cycle) applies — a "quick fix to the rules" mid-Do is iterate-to-Plan plus a §10 Act candidate, not an in-place integration edit.

## Worked example — the Gramps testbed integration

The testbed's integration lives across `CLAUDE.md`, `agent-work/`, and `agent-work/dev-tooling/`. Concrete answers, item by item:

| Item | Where this integration's answer lives |
|---|---|
| **1. Tracker integration** | `CLAUDE.md` §"Bug tracker (MantisBT)" — URL, `p:gramps:nnnn:` link form, status meanings, "Fixed in version" rule. Comment voice and template: `agent-work/templates/tracker-comment.md.tpl`. |
| **2. Branch-target rules** | `CLAUDE.md` §"Upstream fix workflow" — core → `maintenance/gramps61`; addon → `maintenance/gramps60` + forward cherry-pick; testbed → `main`. Override via PR review thread. |
| **3. Reproduction fixtures and runners** | Fixture: `example.gramps`. Runners: `agent-work/scripts/ubuntu/run-interface.sh`, `agent-work/scripts/ubuntu/run-unit.sh`, `agent-work/scripts/ubuntu/run-addon-unit.sh`, `agent-work/scripts/windows/run-unit.sh`, `agent-work/scripts/windows/run-addon-unit.sh`. Documented in `CLAUDE.md` §"Reproduce against `example.gramps` first" + §Local runs. |
| **4. Conformance ruleset** | The tier × home matrix is filled in [[04 - Validation Tooling]] §"Worked example — Gramps testbed `agent-work/dev-tooling/`". Project ruleset cited: doc-16 (addon-dev guidelines) for the in-scope conformance tooling on `addons-source`; gramps core has no equivalent written ruleset yet ([[01 - The Quality Cycle]] §Per repo notes this) — when one exists, it gates `gramps`-core PRs, with the testbed's `core-analysis/` tree continuing as the dependency-analysis source feeding handoffs from addon cycles ([[04 - Validation Tooling]] §Subject item dependencies). |
| **5. Upstream-isn't-ahead routine** | `CLAUDE.md` §"Pre-flight: check upstream isn't ahead" — search-by-affected-file-path rule, GitHub tokenization caveat ("`latex in:title` does NOT match 'Latexdoc'"), `git log upstream/maintenance/gramps60 -- <Addon>/` for addons. |
| **6. Brief / design-proposal templates** | `agent-work/templates/SUMMARY.md.tpl`; `agent-work/templates/exit-brief.md.tpl`; `agent-work/templates/increment-brief.md.tpl`. Design-proposal template: **[planned]** (GEPS 049 was authored upstream, not via this cycle — see [[07 - Case Study - CI Hardening]] §Parallel example). |
| **7. Bundle and act-log paths** | Triage bundles: `agent-work/results/<batch>/issue_<mantis-id>/` (current convention; some historical batches under `agent-work/batches/<batch>/results/`). CI-hardening bundles (testbed self-improvement cycle): `agent-work/results/ci-hardening/ci-<slug>/` (consolidated from former root `/results/`). Act log: **[planned]** as `agent-work/act-log.md` or `process/act-log.md`; current practice is to log Act outcomes in batch exit briefs. Versioned briefs: `brief.vN.md` per [[03 - Cycle Automation]] §Driver skeleton. |
| **8. Committing and PR conventions** | `CLAUDE.md` §"PR description format" — Root cause / Fix / Verified against / Test. Enforcement: human review today; commit-msg hook **[planned]** (Tier 4 greenfield per [[04 - Validation Tooling]]). |
| **9. Repo-specific scripts and tooling** | See expanded table below. |
| **10. Maintainer and governance** | `CLAUDE.md` §"Eduard's review gate" — Eduard opens fork PRs as draft and re-reads with fresh eyes before marking ready; Claude commits and stops there. Solo author; no team review. |
| **11. P-/D-/C-/A- extensions** | None today. **[planned]** when running cycles surface project-specific tightenings. |

### Repo-specific scripts (item 9 expanded)

| Role | Script path | Invocation | Status |
|---|---|---|---|
| Tracker scrape | `agent-work/scripts/make_handoff.py` | Run during batch start; scrapes MantisBT and emits draft briefs into `agent-work/results/<batch>/`. **Mantis-specific** — a project on Jira / GitHub Issues needs its own scraper at this role. | **[built]** |
| Tracker-comment template | `agent-work/templates/tracker-comment.md.tpl` | Filled per disposition; written to `tracker-comment.md` in each bundle. | **[built]** |
| Brief / exit-brief / increment-brief templates | `agent-work/templates/*.md.tpl` | Filled by the scaffolder and (for exits) by the closing step of a batch. | **[built]** |
| Linux repro runners | `agent-work/scripts/ubuntu/run-*.sh` | Driver-invoked for reproduction and verification (T3 runtime + correctness steps 2 and 4). | **[built]** |
| Windows repro runners | `agent-work/scripts/windows/run-*.sh` | Same role, Windows MSYS2 UCRT64. | **[built]** |
| Family-B analyzers (core defect analysis) | `agent-work/dev-tooling/{pyright,semgrep,codeql}/` | Run on gramps core source; findings become *upstream* core PRs. **Not addon conformance** ([[04 - Validation Tooling]] §Two rule families). | **[partial]** (pyright + semgrep run; codeql reserved) |
| Family-A addon-conformance gates | `agent-work/dev-tooling/addon-conformance/` (proposed layout) | The Tier 1–3 mirror of upstream `addons-source` CI. | **[planned]** layout; tooling partly built (PR #820 upstream) |
| Corpus extractor | `agent-work/dev-tooling/claude-commands/extract_corpus.py` | Reads frozen bundles for cross-cycle analysis. Accepts both `tracker-comment.md` (current) and `mantis-comment.md` (historical). | **[built]** |
| Batch runner | `agent-work/run-batch.sh` | Entry point for a triage batch — scrape + handoff. | **[built]** |
| Pre-commit hooks (testbed itself) | `.pre-commit-config.yaml` | Static checks on testbed code; black, ruff E9/F63/F7/F82, ast.parse. | **[built]** |
| Pre-commit hooks (forks) | `agent-work/dev-tooling/pre-commit/` | Installed via `install.sh` into the forks; per-repo configs. | **[built]** |
| Driver (state machine + leaf invocations) | (none yet) | The [[03 - Cycle Automation]] §Driver skeleton design. | **[planned]** |
| Reviewer subagent config | `.claude/agents/reviewer.md` (planned path) | Codex AGENTS.md + scope. | **[planned]** |
| Builder subagent config | `.claude/agents/builder.md` (planned path) | Claude SKILL.md + ready-mark scope ([[03 - Cycle Automation]] §Do). | **[planned]** |

The honest read of this table: the integration's Family-B analyzer plumbing is mature, the Family-A addon-conformance mirror is partial, the driver and subagent configs are entirely planned. That gap is what Act has to chip away at over time.

## What this doc is not

1. **Not a restatement of the cycle.** Plan/Do/Check/Act, the 5/5/1 inside Check, the artifact bundle, the per-beat guidelines — those live in 01–04 and 06. The integration cites them.
2. **Not the project's conformance rules.** The integration says *which* rules apply and *where* their gates run; the rules themselves live in the project's contributor docs (doc 16 for Gramps addons; PEPs / RFCs / code-of-conduct for other projects).
3. **Not the Act log.** The integration is the *current baseline*; the Act log is the *history of changes to it*. Both are process-baseline material, distinct roles.
4. **Not a place for generic guidance.** If an item belongs in every project, it belongs in one of the generic docs, not here. The integration's discipline is "if every project answers this the same way, the answer doesn't live in the integration."
