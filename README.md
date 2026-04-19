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
- **Forks stay pure mirrors of upstream.** All CI machinery lives here,
  so `git pull upstream <branch>` in the forks is always a fast-forward.
- **The `gramps` unit suite runs upstream-style** (`python -m unittest
  discover -p '*_test.py'`, matching gramps' own `regrtest.py`
  conventions). Interface tests use the same discovery mechanism under
  `xmlrunner` so GitHub Actions can render JUnit XML reports.

## Workflows

| Workflow | Purpose | Triggers |
| --- | --- | --- |
| `unit-tests.yml` | Run gramps' own `*_test.py` unit suite | push, PR, manual |
| `interface-tests.yml` | Run dogtail interface tests against gramps | push, PR, manual (with parameterised refs) |
| `addon-unit-tests.yml` | Run per-addon `tests/test_*.py` suites | manual only |
| `upstream-sync.yml` | Nightly rebase of forks onto upstream | cron, manual |

All three test workflows accept `workflow_dispatch` inputs to override
which repos/refs to pull — useful for isolating a regression against a
specific branch or commit. `addon-unit-tests.yml` additionally accepts
a space-separated `addons` input; empty means "every addon with
`tests/test_*.py`".

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

**CI (`.github/workflows/interface-tests.yml`, `unit-tests.yml`):**

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

## Current state

- `test_smoke.py` — launches Gramps, opens the seeded example tree,
  asserts the People view is populated. Must pass before any other test
  is meaningful.

## Known constraints

- Gramps is GTK3; the harness relies on AT-SPI2. A future GTK4 migration
  upstream would require migrating off dogtail.
- Upstream maintainers have not (yet) adopted GUI testing. Float interface
  test contributions on `gramps-devel` before investing heavily in
  upstream-targeted tests.
