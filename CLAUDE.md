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
- Local runs, mirrors CI:
  - Ubuntu (containerised, Docker):
    - ./scripts/ubuntu/run-interface.sh — dogtail/AT-SPI GUI tests
    - ./scripts/ubuntu/run-unit.sh — gramps' own *_test.py suite (no GUI)
    - ./scripts/ubuntu/run-addon-unit.sh [addon ...] — per-addon tests/test_*.py (no GUI)
  - Windows (host, MSYS2 MINGW64 shell — no Docker; same toolchain as aio/build.sh):
    - ./scripts/windows/run-unit.sh — gramps' own *_test.py suite
    - ./scripts/windows/run-addon-unit.sh [addon ...] — per-addon tests/test_*.py
    - Interface tests (AT-SPI/dogtail) do not port to Windows — Windows
      accessibility is UI Automation, requires a different driver stack
- Before pushing an addon-source change that touches tests or the addon
  module itself, run `./scripts/ubuntu/run-addon-unit.sh <AddonName>` on
  the PR branch. The runner loads each test via its dotted path
  (`<Addon>.tests.<module>`) — the same form upstream's ci.yml uses —
  which is what surfaces Python namespace-package traps that
  `discover`-from-tests/ hides. Bug 0012691 was exactly this class of
  bug: `from <Addon> import <Addon>` bound the submodule instead of the
  class under dotted-path loading.
- Platform-specific scripts live under ./scripts/<platform>/; today
  scripts/ubuntu/ and scripts/windows/ exist (Fedora/Arch/macOS
  equivalents are planned)
- Addon test filename convention (mirrors addons-source/.github/workflows/ci.yml):
  - `test_*.py` — general, runs on every platform
  - `test_linux_*.py` — Linux-only
  - `test_windows_*.py` — Windows-only
  - `test_integration_*.py` — Linux-only, full-pipeline/DB-backed
  Each platform's `run-addon-unit.sh` (and the corresponding CI job)
  filters out the prefixes that don't match its OS. The Ubuntu runner
  skips `test_windows_*`; the Windows runner skips both `test_linux_*`
  and `test_integration_*`. Both runners include the platform-neutral
  `test_*.py` files.
- Docker image: gramps-testbed:ubuntu-<gramps-version> (e.g. gramps-testbed:ubuntu-6.0.8),
  built from docker/Dockerfile.ubuntu; version is auto-read from gramps/version.py
  by the wrapper scripts so different Gramps versions get different tags
- Do not edit files in ../gramps or ../addons-source without explicit instruction

## Upstream fix workflow (gramps / addons-source forks)
Fixes to Gramps and its addons are developed in the `../gramps` and
`../addons-source` forks and submitted as PRs to `gramps-project/*`.
The editing ban above still holds — work in either fork only on explicit
instruction. This section complements the global engineering rules in
`~/.claude/CLAUDE.md`; it does not repeat them.

- **Branch targeting.** Bug fixes *and* code-cleanup PRs are based on
  the current production branch — the latest `maintenance/gramps*`
  (today `maintenance/gramps60`, the default working branch for both
  forks), not `master`. Per jralls on gramps-project/gramps#2298:
  `master` is for new features and doesn't reach users until the next
  major release, so anything users should get sooner — fixes and
  cleanups alike — goes on the maintenance branch and is forward-merged
  from there. Only genuinely new-feature work targets `master`. An addon
  change must sit on the branch matching the Gramps version it targets.
- **Reviewer instruction beats default targeting.** When a maintainer
  on a specific PR has explicitly asked for a particular base branch,
  honour that — the targeting default above is the rule, an explicit
  request from a reviewer is the override. Before retargeting any PR,
  read its review thread for instructions of this kind. Example:
  gramps-project/gramps#2299, where Nick-Hall asked for `master` on a
  bug-fix PR ("Please rebase this on the *master* branch."); the
  master targeting stands until he says otherwise.
- **Cherry-picking across gramps60 / gramps61 / master is a correctness
  check, not a `git cherry-pick` check.** The branches' implementation
  code diverges (e.g. addons-source PR 829 rewrote GExiv2 version
  handling on gramps61 only). A patch that applies with no conflict can
  still be wrong on the target branch — a `requires_gi` / version pin /
  declaration is only correct relative to the code it describes. Verify
  against the target branch's *related* code, including files the patch
  doesn't touch. "Applies cleanly" is not "remains correct."
- **Cite the upstream reference.** State the exact upstream file and
  line(s) the fix was checked against — open `gramps-project/gramps` or
  `gramps-project/addons-source` and cite `path:lines` (plus a SHA when
  it matters). Recollection is a hypothesis, not a verification.
- **Check upstream isn't already ahead.** Before calling a bug unfixed,
  grep recent upstream commits and open PRs for the same symptom — a
  fix may have landed on `master` but not yet on `maintenance/gramps60`.
- **One logical fix per PR.** The lint/compile backlog is deliberately
  one PR per addon per issue; keep it that way. Bundling hides mistakes.
- **Ship the means to verify.** Prefer a regression test in the same PR
  — an interface test for testbed-supported code, a `unittest.TestCase`
  for unit-testable code like libtmg. When a test is genuinely
  impractical (GUI-only paths, dead-code deletion), say so explicitly in
  the PR body with a short rationale or manual repro.
- **Edit the source, never the live plugin dir.** Addon changes go in
  `../addons-source/`. The auto-sync runs source → installed plugin
  (`~/.local/share/gramps/gramps60/plugins/…`) one way only; edits made
  directly in the plugin dir are silently lost on the next source save.
- **PR description format:**

  ```
  ## Root cause
  <two sentences>

  ## Fix
  <what the diff does>

  ## Verified against
  - gramps-project/<repo>@<sha>:<path>:<lines>

  ## Test
  <link to the test, or rationale for why none applies + manual repro>
  ```

- **Eduard's review gate (not Claude's to perform).** Eduard opens fork
  PRs as draft and re-reads with fresh eyes before marking ready — solo
  forks have no second reviewer. Claude commits and stops there; pushing,
  opening PRs, and marking them ready happen only on Eduard's explicit
  instruction.

## Status
Interface smoke suite (tests/interface/test_smoke.py) passes locally and in CI
— the previous "smoke before all else" priority is cleared. Addon-unit suite
is now scheduled (push/PR/nightly) and invokes tests via dotted path, so
namespace-package bugs surface in the testbed. Windows unit + addon-unit
runners (MSYS2 MINGW64) are in place — interface coverage on Windows is
still open (AT-SPI/dogtail doesn't port; would need a UIA-based driver).
No singular next focus yet; natural candidates are expanding interface
coverage or adding Fedora/Arch/macOS runners.

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
- Python env in CI:
  - Linux jobs: install `python3-gi`/`python3-pyatspi` via apt and
    create a `--system-site-packages` venv. **Do not switch to
    `actions/setup-python@v5`** — the toolcache interpreter can't see
    apt-installed PyGObject and everything that imports `gi` dies on
    load.
  - Windows jobs: install `mingw-w64-x86_64-python-gobject` (and the
    matching gir typelibs) via `msys2/setup-msys2@v2`, then create a
    `--system-site-packages` venv on `/mingw64/bin/python`. Pacman
    package list is the trimmed runtime subset of `aio/build.sh` —
    that script is authoritative; keep the two in sync when AIO's
    list changes.
- Adding a new Gramps minor: append to `matrix.gramps_ref` in
  unit-tests.yml, interface-tests.yml, and windows-unit-tests.yml
  (keep them in sync).
- Nightly drift crons fire 1-2.75h after upstream-sync (04:00 UTC):
  unit tests 05:00, windows unit tests 05:15, interface tests 05:30,
  docker build 06:00, addon unit tests 06:30, windows addon unit
  tests 06:45.
- `eduralph/gramps` and `eduralph/addons-source` carry a parallel
  "PRFirst" ruleset on `master` + `maintenance/gramps60` (no bypass).