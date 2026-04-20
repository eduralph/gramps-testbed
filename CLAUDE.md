# gramps-testbed

CI/CD harness for GUI-testing Gramps and its addons via AT-SPI/dogtail.

## Workspace layout
Expects three sibling directories:
- `../gramps` — fork of gramps-project/gramps (branch: maintenance/gramps60)
- `../addons-source` — fork of gramps-project/addons-source (branch: maintenance/gramps60)
- `../addons` — upstream gramps-project/addons, used as make.py output target

## Upstream agent guidance
The gramps repository ships its own agent instructions. Always treat these as
authoritative for anything you do inside `../gramps/`:

@../gramps/AGENTS.md

If `../addons-source/AGENTS.md` exists, it applies inside that repo:

@../addons-source/AGENTS.md

## Conventions
- All tests use stdlib unittest.TestCase (contributable upstream; gramps
  itself uses unittest, so pytest is not introduced anywhere in the testbed)
- Local runs (Ubuntu/Linux), containerised, mirrors CI:
  - ./scripts/ubuntu/run-interface.sh — dogtail/AT-SPI GUI tests
  - ./scripts/ubuntu/run-unit.sh — gramps' own *_test.py suite (no GUI)
  - ./scripts/ubuntu/run-addon-unit.sh [addon ...] — per-addon tests/test_*.py (no GUI)
- Before pushing an addon-source change that touches tests or the addon
  module itself, run `./scripts/ubuntu/run-addon-unit.sh <AddonName>` on
  the PR branch. The runner loads each test via its dotted path
  (`<Addon>.tests.<module>`) — the same form upstream's ci.yml uses —
  which is what surfaces Python namespace-package traps that
  `discover`-from-tests/ hides. Bug 0012691 was exactly this class of
  bug: `from <Addon> import <Addon>` bound the submodule instead of the
  class under dotted-path loading.
- Platform-specific scripts live under ./scripts/<platform>/; today only
  scripts/ubuntu/ exists (Fedora/Arch/macOS/Windows equivalents are planned)
- Addon test filename convention (mirrors addons-source/.github/workflows/ci.yml):
  - `test_*.py` — general, runs on every platform
  - `test_linux_*.py` — Linux-only
  - `test_windows_*.py` — Windows-only
  - `test_integration_*.py` — Linux-only, full-pipeline/DB-backed
  Each platform's `run-addon-unit.sh` (and the corresponding CI job) filters
  out the prefixes that don't match its OS. The Ubuntu runner skips
  `test_windows_*` and runs everything else; a future `scripts/windows/`
  runner would do the inverse. Until a Windows image/runner exists in the
  testbed, `test_windows_*.py` runs nowhere here — Windows coverage lives
  in addons-source's own Windows CI job.
- Docker image: gramps-testbed:ubuntu-<gramps-version> (e.g. gramps-testbed:ubuntu-6.0.8),
  built from docker/Dockerfile.ubuntu; version is auto-read from gramps/version.py
  by the wrapper scripts so different Gramps versions get different tags
- Do not edit files in ../gramps or ../addons-source without explicit instruction

## Status
Interface smoke suite (tests/interface/test_smoke.py) passes locally and in CI
— the previous "smoke before all else" priority is cleared. Addon-unit suite
is now scheduled (push/PR/nightly) and invokes tests via dotted path, so
namespace-package bugs surface in the testbed. No singular next focus yet;
natural candidates are expanding interface coverage or porting scripts to
other platforms.

## CI gates and branch protection
- `main` is protected by ruleset "main branch protection" (id 15262402):
  PR required (0 approvals), no force-push, no deletion, conversation
  resolution required. Admin can bypass on PR merges only — direct pushes
  to main are never allowed.
- Gate policy: PR-blocking checks should only fire on issues the PR's own
  diff can cause. Every test workflow here runs gramps or addon code
  against upstream, so **none are listed as required checks**. Unit Tests
  and Docker Image Build additionally set `continue-on-error: true` at
  job level so their workflow conclusion stays green even when the job
  check-run is red. Interface Tests runs visibly but doesn't block.
- Python env in CI: install `python3-gi`/`python3-pyatspi` via apt and
  create a `--system-site-packages` venv. **Do not switch to
  `actions/setup-python@v5`** — the toolcache interpreter can't see
  apt-installed PyGObject and everything that imports `gi` dies on load.
- Adding a new Gramps minor: append to `matrix.gramps_ref` in
  unit-tests.yml and interface-tests.yml (keep them in sync).
- Nightly drift crons fire 1-2.5h after upstream-sync (04:00 UTC): unit
  tests 05:00, interface tests 05:30, docker build 06:00, addon unit
  tests 06:30.
- `eduralph/gramps` and `eduralph/addons-source` carry a parallel
  "PRFirst" ruleset on `master` + `maintenance/gramps60` (no bypass).