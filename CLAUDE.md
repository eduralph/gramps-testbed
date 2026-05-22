# gramps-testbed

CI/CD harness for GUI-testing Gramps and its addons via AT-SPI/dogtail.

## Workspace layout
Expects three sibling directories:
- `../gramps` — fork of gramps-project/gramps (branch: maintenance/gramps61)
- `../addons-source` — fork of gramps-project/addons-source (branch: maintenance/gramps61)
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
- Docker image: gramps-testbed:ubuntu-<gramps-version> (e.g. gramps-testbed:ubuntu-6.1.0),
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
  (today `maintenance/gramps61`), not `master`. Per jralls on
  gramps-project/gramps#2298:
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
  fix may have landed on `master` but not yet on `maintenance/gramps61`.
- **One logical fix per PR.** The lint/compile backlog is deliberately
  one PR per addon per issue; keep it that way. Bundling hides mistakes.
- **Ship the means to verify.** Prefer a regression test in the same PR
  — an interface test for testbed-supported code, a `unittest.TestCase`
  for unit-testable code like libtmg. When a test is genuinely
  impractical (GUI-only paths, dead-code deletion), say so explicitly in
  the PR body with a short rationale or manual repro.
- **Edit the source, never the live plugin dir.** Addon changes go in
  `../addons-source/`. The auto-sync runs source → installed plugin
  (`~/.local/share/gramps/gramps61/plugins/…`) one way only; edits made
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

## Bug tracker (MantisBT)
Authoritative bug list for Gramps. When this CLAUDE.md and existing
memories cite a bug by Mantis ID (e.g. `0013214`, `bug 13395`), they
mean an issue here — not GitHub. Wiki references:
[Bug triage](https://gramps-project.org/wiki/index.php/Bug_triage) and
[Using the bug tracker](https://www.gramps-project.org/wiki/index.php/Using_the_bug_tracker).

- **Tracker:** https://gramps-project.org/bugs. MantisBT "projects" map
  to release branches:
  - "Gramps 6.0" project = `maintenance/gramps60` work
  - "Gramps 5.2" project = older maintenance branch
  - master-only bugs are filed against the next unreleased version
    (today 6.1.0; see the MantisBT Roadmap)
- **`#nnnn` in MantisBT is a MantisBT issue link, NOT a GitHub PR.**
  GitHub's `#nnnn` convention does not apply inside tracker notes — the
  hash references another Mantis ticket.
- **Linking a GitHub PR from a MantisBT note:**
  - gramps core: `p:gramps:nnnn:` — the syntax documented under the
    wiki's [Useful MantisBT bug tracker Syntax codes](https://www.gramps-project.org/wiki/index.php/Using_the_bug_tracker#Useful_MantisBT_bug_tracker_Syntax_codes)
    section (verified against oldid=125932, edited 2025-10-18).
    Applies only to the main `gramps` repository.
  - addons-source / other addon repos: paste the full GitHub URL —
    no shorthand exists for non-`gramps` repos.
- **The PR body must reference the MantisBT issue** using the special
  keywords from upstream's Committing policies, so the tracker
  cross-links automatically. A self-assigned bug whose PR doesn't
  reference it is a triage smell.
- **Status meanings worth knowing when reading a ticket:**
  - "acknowledged" — enough info to investigate, not spam
  - "confirmed" — independently reproduced (for feature requests:
    judged valid — not a commitment to ship)
  - "feedback" — waiting on the reporter
  - "assigned" — someone is actively working it (cleared when they
    stop)
- **Resolving a bug (dev side):**
  - Note the fixing commit SHA in a comment on the ticket.
  - On a maintenance-branch project, set the **"Fixed in version"**
    field to the next release on that branch — this is what drives the
    Change Log page for that release.
  - If you fix a bug ahead of its **Target Version**, update Target
    Version to the release you actually shipped it in before resolving
    — otherwise the [Roadmap](https://gramps-project.org/bugs/roadmap_page.php)
    display goes wrong. (`X.Y.99` phony releases mean "for X.Y
    eventually, no milestone yet".)
  - Don't mark "resolved" until the fix is committed to the maintenance
    branch AND forward-merged to master. Both are the developer's
    responsibility, not the triager's.
- **Reproduce against `example.gramps` first.** Triage and developers
  use it as the canonical fixture; "couldn't reproduce" is the most
  common reason a fix stalls in triage.
- **One issue per ticket.** Bundled reports are closed upstream with a
  request to file one ticket per issue (or renamed and split). Mirror
  this when filing or splitting.

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