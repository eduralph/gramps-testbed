# Item 1 — Fix the hardcoded fork owner in `upstream-sync.yml`

**Branch:** `ci-fork-owner` (off `main`) · **Patch:** `patch.diff`

## Root cause
`upstream-sync.yml` was never parameterised the way the test workflows are:
the fork owner was hardcoded as `eduralph` in the `matrix.repo` entries, and
the header comment + `FORK_SYNC_TOKEN` scope note named `eduralph/*` directly.
After an owner rename this targets a stale handle.

## Change
- `.github/workflows/upstream-sync.yml:33,35` — `owner: eduralph` →
  `owner: ${{ github.repository_owner }}` (both matrix rows).
- `.github/workflows/upstream-sync.yml:16-22` (header) — token-requirement
  comment reworded to name the owner via `github.repository_owner` and to
  flag that the PAT scope is configured out-of-band and must be re-pointed on
  an owner rename.
- `.github/workflows/upstream-sync.yml:~57` — token-scope error message
  reworded from `eduralph/gramps + eduralph/addons-source` to
  "this owner's gramps + addons-source forks".

Sync logic, the PRFirst-via-PR approach, and the branch matrix are unchanged.

## Files
- `.github/workflows/upstream-sync.yml`

## Verification
- `actionlint .github/workflows/upstream-sync.yml` → exit 0 (with shellcheck
  0.10.0 on PATH, so the `run:` shell blocks were linted too). This confirms
  `${{ github.repository_owner }}` is a valid expression in the matrix context
  — actionlint resolves the `github` context there.
- `grep -n eduralph .github/workflows/upstream-sync.yml` → no matches.

## What this proves / leaves unproven
- **Proves:** the file is syntactically valid, the expression is legal in
  matrix position, and no literal `eduralph` remains.
- **Leaves unproven (caveat A):** that the swap is *behaviourally* correct
  end-to-end. `${{ github.repository_owner }}` is the **testbed's** owner;
  the workflow pushes to the **fork** repos authenticated by
  `FORK_SYNC_TOKEN`. The swap is only correct if (a) the forks live under the
  same owner as the testbed and (b) the PAT scope covers that owner's fork
  repos. If the break was an account rename, GitHub redirects repo identity
  and fine-grained PATs follow it, so it likely resolves clean — but this can
  only be confirmed by a `workflow_dispatch` run with a correctly-scoped
  token. **Eduard's step; do not trigger.** Confirm the fork remotes' owner
  and the PAT scope before running.
