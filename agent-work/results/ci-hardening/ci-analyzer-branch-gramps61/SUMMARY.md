# Item B (v3) — Analyze gramps61 in dev-tooling

**Branch:** `ci-analyzer-branch-gramps61` (off `main`) · **Patch:** `patch.diff`
Ratifies the v2 recommendation (reading (b)). Separate PR from Item A.

## Decision
The dev-tooling shape/flow analyzers (pyright + semgrep) are **core-subject**:
they scan gramps **core** source (`dev-tooling.yml:6-12` header; semgrep runs
over `../gramps/gramps/gui/` at `:94`) and their findings become **core** PRs,
which target `maintenance/gramps61`. So the analyzer should run on the branch
those fixes land on.

## Change
- `dev-tooling.yml:61` — resolve-step default `maintenance/gramps60` →
  `maintenance/gramps61`, with a comment stating the core-analysis rationale
  and contrasting it with the addon-conformance jobs (which pair gramps60
  addons against gramps61 core — Item A).
- `dev-tooling.yml:138` — the **disabled** CodeQL example's `ref:` updated
  `gramps60` → `gramps61` for consistency, so enabling that job later doesn't
  reintroduce the gramps60 default. Commented-out block; no runtime effect.

The input→repository-variable→default resolution chain is otherwise unchanged;
a `workflow_dispatch` input or `GRAMPS_REF` repo variable still overrides.

## Verified against
- `dev-tooling.yml:94` — semgrep target `../gramps/gramps/gui/` (core source).
- `CLAUDE.md:7` — local `../gramps` fork is on `maintenance/gramps61`; the
  `analyze` skill runs there, so CI now matches where the analyzer runs
  locally (it previously diverged at gramps60).
- Item 2a / jralls#2298 — core fixes target gramps61.

## Verification
- `actionlint .github/workflows/dev-tooling.yml` → exit 0.
- `grep maintenance/gramps60 dev-tooling.yml` → no matches (active default and
  the disabled example both moved).

## What this proves / leaves unproven
- **Proves:** YAML valid; only the analyzer default (and its disabled-example
  twin) moved; override chain intact.
- **Leaves unproven:** nothing runtime-risky — it's a default ref. The first
  scheduled/dispatch run will analyze gramps61; findings counts may differ from
  the gramps60 baseline (expected, since the source differs).
