# Item 7 (Item D) — remaining composite extractions: decisions

Disposition of the two Item 7 extractions deferred in the v2 results.

## setup-gramps-venv — IMPLEMENTED (PR #65)
The `--system-site-packages` venv step is byte-identical across the 3 Ubuntu
workflows → extracted to `.github/actions/setup-gramps-venv` (bash composite),
migrated unit/interface/addon-unit. Same shell-split as compile-gramps-mo: the
2 Windows jobs use `/ucrt64/bin/python` + `cygpath` under `shell: msys2 {0}`
and stay inline. Validated by a unit-tests dispatch.

## repo-resolution composite — DECLINED (do not extract)
**Decision: do not extract.** Grounded in the actual shapes:

- The `repository:` expression is identical across the 5 test workflows:
  `${{ github.event.inputs.gramps_repo || vars.GRAMPS_REPO ||
  format('{0}/gramps', github.repository_owner) }}`.
- But the `ref:` resolution has **three structurally different shapes**:
  1. **matrix** (`unit-tests`, `interface-tests`, `windows-unit-tests`):
     `${{ github.event.inputs.gramps_ref || matrix.gramps_ref }}`
  2. **variable+default** (`addon-unit-tests`, `windows-addon-unit-tests`):
     `${{ github.event.inputs.gramps_ref || vars.GRAMPS_REF ||
     'maintenance/gramps61' }}`
  3. **computed run-step** (`dev-tooling`): a `Resolve gramps source` bash step
     → `${{ steps.src.outputs.ref }}`.

**Why a composite action doesn't help here:**
- `matrix.gramps_ref` is **not accessible inside a composite action** (no matrix
  context), so the ref must be computed in each caller and passed as an input —
  the resolution logic stays in the callers, defeating the purpose.
- The only genuinely-shared element is the one-line `repository:` expression. A
  composite action can't DRY a single `with:` expression without the caller
  re-writing it to pass it in (circular) — no real reduction, added indirection.
- Forcing one shape (e.g., matrix→vars) would be a **behavior change**: the
  per-matrix-cell job fan-out (gramps61 + master on Windows) is load-bearing.

This matches the brief's own flag ("forcing one shape would be a behavior
change, not a refactor"). The duplication here is a shared *expression*, not a
shared *step body*; GitHub Actions has no clean cross-file mechanism to DRY it
(workflow-level `env` can't reliably hold `github.event.inputs` across all
triggers, and is per-file anyway). Net: the cost (indirection + an input the
caller computes) exceeds the benefit (one shared line). Leave as-is.

## Windows composite variants (venv / compile-mo) — DEFERRED, low priority
The 2 Windows venv steps and 2 Windows compile-mo steps are each internally
identical and *could* become msys2 composite actions. Not done because:
- A composite step's `shell:` is a literal; whether `shell: msys2 {0}` (the
  custom shell setup-msys2 registers at job level) works inside a composite
  action is **unproven** and would need its own dispatch to confirm.
- Each de-dups only 2 steps; the Windows jobs are advisory
  (`continue-on-error`), so the upside is marginal.
Consistent with how compile-gramps-mo (PR #60) left Windows inline. Revisit only
if a future change makes the msys2-in-composite question worth a probe.

## Net Item 7 outcome
- compile-gramps-mo (Ubuntu) — merged (#60), validated.
- setup-gramps-venv (Ubuntu) — PR #65, validated.
- repo-resolution — declined, rationale above.
- Windows composite variants — deferred, low priority.
The un-DRY'd surface that remains is exactly the parts where DRYing would
change behavior or rests on an unproven composite-shell assumption.
