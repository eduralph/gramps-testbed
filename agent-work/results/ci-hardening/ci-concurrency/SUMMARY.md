# Item 5 — Add `concurrency` control to all workflows

**Branch:** `ci-concurrency` (off `main`) · **Patch:** `patch.diff`

## Root cause
No workflow declared a `concurrency` group, so rapid pushes spawned
overlapping full matrices (including the 30-min Windows and interface jobs)
with no auto-cancel.

## Change
Added the same top-level block to **seven** CI workflows
(`addon-unit-tests`, `dev-tooling`, `docker-build`, `interface-tests`,
`unit-tests`, `windows-addon-unit-tests`, `windows-unit-tests`):

```yaml
concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: ${{ github.ref != 'refs/heads/main' }}
```

Placed between `permissions:`/`on:` and `jobs:` in each.

**`upstream-sync.yml` is deliberately excluded** — it is schedule/dispatch-only
and must never cancel a half-finished fork sync (a cancelled merge/push to a
fork could leave a sync branch in a partial state).

**Conditional `cancel-in-progress`** (vs blanket `true`): cancels superseded
PR-branch runs — the actual goal — while letting post-merge `main` runs always
complete, so a fast second merge doesn't cancel the first merge's CI.

This is one PR for all seven because it is a single logical change applied
uniformly.

## Verified against
- `grep -L cancel-in-progress .github/workflows/*.yml` → only
  `upstream-sync.yml` (confirms 7-in / 1-out).
- `unit-tests.yml:25-32` (sample) — block sits cleanly between `permissions:`
  and `jobs:` with blank-line separation.

## Verification
- `actionlint .github/workflows/*.yml` → the only finding is a **pre-existing**
  SC2115 in `interface-tests.yml:163` (a `run:` block, untouched by this
  top-level insertion). No new warnings from any of the seven edits.

## What this proves / leaves unproven
- **Proves:** the block is valid YAML/expression in all seven, placed
  identically, and `upstream-sync` is untouched.
- **Leaves unproven:** the cancel-on-superseded-push behaviour actually firing
  — that needs two overlapping pushes on a real branch (`workflow_dispatch` /
  observation, Eduard's step). The local check proves wiring, not runtime
  cancellation semantics.
