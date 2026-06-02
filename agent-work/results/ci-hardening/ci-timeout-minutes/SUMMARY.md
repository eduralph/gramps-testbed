# Item 8 — Add the two missing `timeout-minutes`

**Branch:** `ci-timeout-minutes` (off `main`) · **Patch:** `patch.diff`

## Root cause
Most jobs cap runtime (unit/addon-unit `20`; interface/windows/docker `30`),
but `dev-tooling.yml`'s `shape-and-flow` job and `upstream-sync.yml`'s `sync`
job had no `timeout-minutes`, so a hung analyzer or a wedged git/network
operation could run to the runner's hard cap. This is the single-runaway-job
half of Item 5's concern (Item 5 stops jobs *piling up*; this stops one job
*running away*).

## Change
- `dev-tooling.yml` `shape-and-flow` → `timeout-minutes: 15`.
- `upstream-sync.yml` `sync` → `timeout-minutes: 15`.

Both matched to the existing magnitudes (the analyzers and the per-cell
git+gh sync each normally finish in a few minutes). No job that already had a
value was touched.

## Verified against
- `unit-tests.yml`, `addon-unit-tests.yml` (`timeout-minutes: 20`),
  `interface-tests.yml`, `windows-*`, `docker-build.yml`
  (`timeout-minutes: 30`) — the existing magnitudes 15 sits below.

## Verification
- `actionlint` on both files → exit 0.
- Inventory: every workflow now has exactly one `timeout-minutes` (8/8); only
  the two previously-uncapped jobs gained a value.

## What this proves / leaves unproven
- **Proves:** both jobs are now capped; YAML valid; no other job changed.
- **Leaves unproven:** that 15 min is the right ceiling under worst-case load —
  it is a generous bound on observed runtimes, adjustable if a legitimate run
  ever approaches it.
