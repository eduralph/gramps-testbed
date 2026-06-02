# pre-commit hooks

Three pre-commit configs live under `agent-work/dev-tooling/pre-commit/`; one is
the testbed root config installed via the standard `pre-commit install`,
the other two are out-of-tree configs wired into the gramps and
addons-source forks. Out-of-tree avoids committing dev-tooling onto
fork maintenance branches that get used as the base for upstream PRs.

## What each config runs

| Repo | black | mypy | ruff | ast.parse |
|---|---|---|---|---|
| gramps-testbed (`.pre-commit-config.yaml` at root) | yes | – | E9 F63 F7 F82 | yes |
| eduralph/gramps (`gramps.yaml`) | yes | yes | – | yes |
| eduralph/addons-source (`addons-source.yaml`) | – | – | E9 F63 F7 F82 | yes |

`black` matches the `psf/black@stable --check --diff` job in gramps CI.
`mypy` matches the "Run mypy static type checker" job. `ruff` flags
match the lint job in addons-source CI (post PR 820).

## Install

```sh
./agent-work/dev-tooling/pre-commit/install.sh
```

Installs hooks into all three repos. Re-run if `pre-commit` updates the
hook template, or if a fork repo is freshly cloned. Hooks run on the
next `git commit`.

To uninstall (e.g. to bisect whether a hook is blocking something):

```sh
./agent-work/dev-tooling/pre-commit/install.sh --uninstall
```

To skip a single commit (only if you know why):

```sh
git commit --no-verify
```

## What it catches, what it doesn't

**Catches** — class of failures that have actually broken PRs:

- `[method-assign]` lint errors (PR 2334 — mypy in `gramps.yaml`)
- Black-formatting drift (CI's lint gate)
- Bare-numeric `SyntaxError` / undefined name (ruff E9/F82)

**Does NOT catch** — needs an actual test run:

- Test-fixture attribute-bypass bugs (PR 2335 — `__new__`-built
  `AddonManager` missing `dbstate`/`uistate`)
- Behavioural regressions

For the latter, run the testbed Docker test runner as a manual pre-push
step:

- `agent-work/scripts/ubuntu/run-unit.sh` for gramps changes
- `agent-work/scripts/ubuntu/run-addon-unit.sh <Addon>` for addon changes

And after pushing a PR, verify CI is green with
`agent-work/scripts/verify-pr.sh <repo> <PR#> --watch`.
