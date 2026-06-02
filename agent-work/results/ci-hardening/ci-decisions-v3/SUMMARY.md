# v3 decisions brief — batch summary (2026-06-01)

Implements the three open decisions from the v2 IMPLEMENTATION RESULTS.
Nothing pushed; no PRs opened; STOP after results.

## EDUARD QUEUE (record-only — Claude did not and does not act on these)

### Awaiting `workflow_dispatch` (Eduard runs)
- **Item 1** — end-to-end fork sync; depends on the `FORK_SYNC_TOKEN` PAT
  scope covering the **current owner's** fork repos (caveat A — the silent
  breaker). `results/ci-fork-owner/`.
- **Item 4** — the all-skipped degraded-coverage guard firing on a real
  Windows runner. `results/ci-windows-coverage-guard/`.
- **Item 5** — `cancel-in-progress` semantics: superseded PR-branch run
  cancelled, `main` run completes. `results/ci-concurrency/`.
- **Item 7** — the `./gramps-testbed/.github/actions/compile-gramps-mo`
  local-action path resolves (actionlint neither validates nor rejects it).
  `results/ci-compile-gramps-mo-action/`.
- **Item A (this brief)** — the gramps60-addon / gramps61-core pairing
  actually checks out and builds; expect advisory reds where real
  forward-compat gaps exist (the jobs are `continue-on-error`).
  `results/ci-addon-ref-gramps60/`.

### Deferred (decision-required, NOT in this brief)
- **Item 7 `setup-gramps-venv`** — Ubuntu/MSYS2 body divergence (different
  interpreter, cygpath, `$GITHUB_PATH`); a two-action split (bash + msys2),
  not one parameterized action, is the likely shape. Hold until Item 7's
  local-action path is dispatch-proven.
- **Item 7 repo-resolution composite** — matrix-caller vs
  input→repo-variable→default-caller shapes differ; forcing one shape is a
  behavior change.

## This brief's changes (each its own PR branch off `main`)

| Item | Branch | Result |
|------|--------|--------|
| A — addon pairing | `ci-addon-ref-gramps60` | ✅ `addons_ref`→gramps60, `gramps_ref` kept gramps61; self-documenting comments. Re-verified the basis (overrode my v2 decline). |
| B — analyzer branch | `ci-analyzer-branch-gramps61` | ✅ dev-tooling default gramps60→gramps61 (active + disabled CodeQL example). |
| C — regex extractor | `ci-requires-mod-extractor` (no new commit) | ✅ deviation **ratified** in its SUMMARY; no code change. |

## Decisions ledger (carried from the v3 brief, for the record)
- **2b** → flip `addons_ref`→gramps60, keep `gramps_ref`→gramps61 (forward-
  compat pairing). Implemented as Item A after independent re-verification.
- **2 #3** → analyzer branch gramps61 (core-defect analysis). Item B.
- **3** → accept the regex deviation; do not revert. Item C.
- **1, 4, 5, 6, 7, 8** → accepted from v2; dispatch/deferred items above.

## One honest nuance recorded under Item A
Status-quo 61/61 was not a *pure* duplicate of addons-source's gramps61 CI
(that CI tests *released* core; the testbed tests *fresh* source), so the flip
trades a fresh-core-regression signal for the forward-compat signal. A coherent
`{60/61, 61/61}` matrix would keep both — out of scope here, flagged for later.
See `results/ci-addon-ref-gramps60/SUMMARY.md`.
