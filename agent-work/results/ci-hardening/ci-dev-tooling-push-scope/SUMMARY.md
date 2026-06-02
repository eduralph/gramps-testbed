# Item 6 — Scope `dev-tooling.yml`'s push trigger

**Branch:** `ci-dev-tooling-push-scope` (off `main`) · **Patch:** `patch.diff`

## Root cause
`dev-tooling.yml:14-16` had a bare `push:` (no `branches:` filter) while every
other workflow uses `push: branches: [main]`. The file's own header
(`dev-tooling.yml:13`) states its repo/ref resolution "matches the other test
workflows", so the missing filter is an oversight, not a deliberate broaden —
it fired the analyzer on every push to every branch.

## Change
Added `branches: [main]` to the `push:` trigger (the form recommended by the
brief for consistency with the suite). `pull_request`, `schedule`, and
`workflow_dispatch` are unchanged, so PR and nightly/manual coverage is
unaffected — only the per-branch push firing is removed.

## Verified against
- `unit-tests.yml:4-6`, `addon-unit-tests.yml:4-6`, `docker-build.yml:4-6`,
  etc. — all siblings use `push: branches: [main]`. `dev-tooling.yml` now
  matches.

## Verification
- `actionlint .github/workflows/dev-tooling.yml` → exit 0.

## What this proves / leaves unproven
- **Proves:** YAML valid; trigger block now consistent with the suite.
- **Leaves unproven:** nothing of substance — trigger-filter semantics are
  GitHub-native and well-defined; the behavioural effect (no run on non-main
  push) is observable but not worth a dispatch run.
