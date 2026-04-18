# gramps-testbed

CI/CD harness for interface-testing [Gramps](https://github.com/gramps-project/gramps)
and third-party addons via AT-SPI / dogtail.

Companion to the forks at:
- https://github.com/eduralph/gramps
- https://github.com/eduralph/addons-source

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
- **The `gramps` unit suite runs upstream-style** (`python -m unittest discover`).
  Interface tests run through `xmlrunner` so GitHub Actions can render
  JUnit XML reports.

## Workflows

| Workflow | Purpose | Triggers |
| --- | --- | --- |
| `unit-tests.yml` | Run `gramps`' own unit suite | push, PR |
| `gui-tests.yml` | Run dogtail interface tests against gramps + built addons | push, PR, manual (with parameterised refs) |
| `upstream-sync.yml` | Nightly rebase of forks onto upstream | cron, manual |

`gui-tests.yml` accepts `workflow_dispatch` inputs to pin specific refs of
either fork and to narrow the addon build to a single addon — useful for
isolating a regression.

## Running locally

Mirror CI exactly via Docker:

```bash
./scripts/bootstrap-forks.sh          # once, to clone the forks
./scripts/run-local.sh                # runs the full suite the same way CI does
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
