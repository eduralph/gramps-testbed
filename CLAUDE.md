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
- Platform-specific scripts live under ./scripts/<platform>/; today only
  scripts/ubuntu/ exists (Fedora/Arch/macOS/Windows equivalents are planned)
- Docker image: gramps-testbed:ubuntu-<gramps-version> (e.g. gramps-testbed:ubuntu-6.0.8),
  built from docker/Dockerfile.ubuntu; version is auto-read from gramps/version.py
  by the wrapper scripts so different Gramps versions get different tags
- Do not edit files in ../gramps or ../addons-source without explicit instruction

## Current priority
Get tests/interface/test_smoke.py passing locally and in CI before adding any
other tests.