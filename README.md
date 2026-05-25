# gramps-testbed

CI/CD harness for interface-testing [Gramps](https://github.com/gramps-project/gramps)
and third-party addons via AT-SPI / dogtail.

Designed to be forked: by default both the bootstrap script and the CI
workflow target same-owner forks of `gramps` and `addons-source`. Fork
this repo to `you/gramps-testbed`, fork Gramps to `you/gramps`, fork
addons-source to `you/addons-source`, and everything picks up your
names automatically. See [Configuration](#configuration) to point at
forks living elsewhere.

## Layout

The testbed expects this workspace layout (all four as siblings):

```
workspace/
├── gramps/              # fork of gramps-project/gramps
├── addons-source/       # fork of gramps-project/addons-source
├── addons/              # upstream gramps-project/addons (publish target)
└── gramps-testbed/      # this repo
```

Run `./scripts/bootstrap-forks.sh` to produce that layout.

## Philosophy

- **Interface tests are written as `unittest.TestCase` subclasses** so they
  can be contributed upstream without rewriting.
- **CI machinery lives in this repo, not in the forks.** Where the
  forks must carry CI cherry-picks upstream hasn't adopted, the nightly
  `upstream-sync.yml` workflow reconciles them with a merge PR rather
  than fast-forwarding — the fork maintenance branches are
  PR-protected and direct push is rejected.
- **The `gramps` unit suite runs upstream-style** (`python -m unittest
  discover -p '*_test.py'`, matching gramps' own `regrtest.py`
  conventions). Interface tests use the same discovery mechanism under
  `xmlrunner` so GitHub Actions can render JUnit XML reports.
- **Triage feeds the tests, not the other way round.** Bug selection is
  scripted and reviewable (see [Triage pipeline](#triage-pipeline)); the
  intent is that every fix that lands carries a regression test back into
  this harness, so the backlog shrinks without re-growing.

## Workflows

| Workflow | Purpose | Triggers |
| --- | --- | --- |
| `unit-tests.yml` | Run gramps' own `*_test.py` unit suite | push, PR, cron, manual |
| `interface-tests.yml` | Run dogtail interface tests against gramps | push, PR, cron, manual (with parameterised refs) |
| `addon-unit-tests.yml` | Run per-addon `tests/test_*.py` suites | push, PR, cron, manual |
| `docker-build.yml` | Build the Ubuntu Docker test image | push (Dockerfile paths), PR (Dockerfile paths), cron, manual |
| `upstream-sync.yml` | Open fork-sync PRs from upstream | cron, manual |

All three test workflows accept `workflow_dispatch` inputs to override
which repos/refs to pull — useful for isolating a regression against a
specific branch or commit. `addon-unit-tests.yml` additionally accepts
a space-separated `addons` input; empty means "every addon with
`tests/test_*.py`".

## Triage pipeline

`triage/` turns the Gramps [MantisBT bug tracker](https://gramps-project.org/bugs)
into reviewable, fix-ready work items. It exists because the highest-value
input to the test suite is *the right bug to fix next*, and that decision
benefits from the tracker's full comment history — which the bulk CSV export
omits and the web UI gates behind Cloudflare.

The cycle, scripted where it's mechanical and manual where it's judgment:

1. **Export** (manual, periodic): a logged-in Mantis CSV export — with the
   `description`, `steps_to_reproduce`, and `additional_information` columns
   enabled under *My Account → Manage Columns* — lands dated in `triage/data/`.
   The export cannot include comment threads; step 2 handles those.
2. **Scrape notes** (`triage/scripts/mantis_notes.py`): pulls each issue's
   comment thread by driving a real browser that has already cleared
   Cloudflare, writing `triage/notes/issue_<id>.json`. (This rides your own
   browser session; it does not bypass the challenge.)
3. **Generate briefs** (`triage/scripts/make_handoff.py`): merges the CSV
   fields and scraped notes into one Markdown brief per issue under
   `triage/batches/<batch>/`, each carrying an empty triage verdict and an
   auto-flag pass (external-repo / upstream / core-traceback / already-fixed).
   `run-batch.sh` chains steps 2–3.
4. **Triage** (manual judgment): each brief's verdict records whether the
   issue is actionable, which repo the fix targets (addon vs gramps core vs
   an external repo — different PR destinations), whether the reporter's
   workaround masks the real defect, and where the regression test goes.
   This is the step that catches mislabelled bugs before any code is written.
5. **Fix** ([Claude Code](https://docs.claude.com/en/docs/claude-code),
   or by hand): a brief is handed to Claude Code, which works the issue per
   its verdict — reproduce against `example.gramps` first, write the failing
   test, fix until green, and emit a result (summary + patch + PR description)
   under the batch's `results/`. The verdict's conventions (branch target,
   "edit source not the plugin dir", the PR format) are enforced via the
   testbed's `CLAUDE.md`. Fixes are committed only after human review;
   nothing is pushed or PR'd automatically.

The dependency-light scripts (`mantis_notes.py` needs a browser driver;
`make_handoff.py` is pure stdlib) and the full per-step workflow — including
the Cloudflare attach-mode setup, the Claude Code handoff conventions, and
the per-issue verdict format — are documented in
[`triage/README.md`](triage/README.md).

`triage/data/` and `triage/notes/` are gitignored: they are regenerable
exports of third-party tracker content. The verdicts and scripts are tracked,
since the verdict is the curated judgment the pipeline produces.

## Configuration

Defaults resolve to same-owner forks, so most users only need to fork
the three repos under the same GitHub account and run the bootstrap.
For forks that live under a different owner, override as follows.

**Locally (`scripts/bootstrap-forks.sh`):**

```bash
FORK_OWNER=alice ./scripts/bootstrap-forks.sh           # alice/gramps, alice/addons-source
GRAMPS_FORK_URL=https://gitlab.com/… ./scripts/…        # full URL override
BRANCH=feature/xyz ./scripts/bootstrap-forks.sh         # non-default branch
./scripts/bootstrap-forks.sh --ssh                      # SSH remotes
```

**CI (`.github/workflows/interface-tests.yml`, `unit-tests.yml`, `addon-unit-tests.yml`):**

Resolved in this order: `workflow_dispatch` input → repository variable
→ same-owner default.

| Knob | Per-run input | Persistent variable |
| --- | --- | --- |
| gramps repo | `gramps_repo` | `vars.GRAMPS_REPO` |
| gramps ref | `gramps_ref` | `vars.GRAMPS_REF` |
| addons-source repo | `addons_source_repo` | `vars.ADDONS_SOURCE_REPO` |
| addons-source ref | `addons_ref` | `vars.ADDONS_SOURCE_REF` |

Set persistent values under *Settings → Secrets and variables → Actions
→ Variables*.

## Running locally

Per-platform scripts live under `scripts/<platform>/`. Today that's
`scripts/ubuntu/` (Docker on Linux). Fedora, Arch, macOS, and Windows
entry points will land alongside as those testbeds are added.

Mirror CI exactly via Docker on an Ubuntu/Linux host:

```bash
./scripts/bootstrap-forks.sh          # once, to clone the forks
./scripts/ubuntu/run-interface.sh     # dogtail/AT-SPI GUI tests (mirrors CI)
./scripts/ubuntu/run-unit.sh          # gramps' own *_test.py unit suite
./scripts/ubuntu/run-addon-unit.sh    # per-addon tests/test_*.py (args = addon names, empty = all)
./scripts/ubuntu/run-manual.sh        # launches Gramps visibly for manual QA
./scripts/ubuntu/rebuild-image.sh     # force-rebuild after Dockerfile edits
```

The container installs gramps in editable mode against your checkout, so
code edits in `../gramps/` are reflected on the next run without rebuilding
the image.

## Adding a test

1. Drop a `test_*.py` under `tests/interface/`.
2. Subclass `tests.interface.base.GrampsInterfaceTestCase`.
3. Use `self.app` (the dogtail `Application` root) to find widgets.
4. Screenshots on failure land in `artifacts/screenshots/` automatically.

For a bug-specific regression test, name it `test_bug_<id>_<slug>.py` and
cite the Mantis issue in the module docstring — the convention the triage
pipeline's verdicts point fixes at.

## Current state

- **Smoke** (`tests/interface/test_smoke.py`) launches Gramps, opens
  the seeded example tree, and asserts the People view is populated.
- **Per-bug interface regression tests** under `tests/interface/`
  each reproduce a specific upstream issue (CombinedView stale-view
  crash, QuiltView Surname import, the Finnish about-date inflection
  KeyError, …) and go green once the upstream fix lands and syncs to
  the fork branches CI checks out. That "fails until the fix lands"
  pattern is the testbed's main purpose — interface tests stay
  non-blocking so the red is informative without gating merges.
- **Addon `.po` catalog gate** (`tests/test_addon_po_catalogs.py`)
  runs `msgfmt` over every addon's translations the same way
  `make.py build` does, catching `.po` regressions before they reach
  users.
- **Triage pipeline** (`triage/`) selects and prepares tracker bugs for
  fixing, with each fix expected to return a regression test to one of
  the suites above. See [Triage pipeline](#triage-pipeline).

See CLAUDE.md "CI gates and branch protection" for which workflows
block merges (none of the test workflows do; all advisory).

## Known constraints

- Gramps is GTK3; the harness relies on AT-SPI2. A future GTK4 migration
  upstream would require migrating off dogtail.
- Upstream maintainers have not (yet) adopted GUI testing. Float interface
  test contributions on `gramps-devel` before investing heavily in
  upstream-targeted tests.