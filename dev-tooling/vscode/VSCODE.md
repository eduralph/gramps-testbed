# dev-tooling in VS Code

How to run the shape+flow analyzers (pyright + semgrep) from inside the editor.

**Assumed setup:** you open `gramps-testbed/` as the workspace folder and reach
into the sibling `../gramps` fork — the same layout the bootstrap produces and
that `additionalDirectories` already assumes. All tasks run from the testbed
root and target `../gramps`.

## Why this is task-based, not Pylance-config-based

The experiment config (`dev-tooling/pyright/pyrightconfig.experiment.json`) is
deliberately **not** the repo's pyright config. It is scoped to a hot-file
allowlist with GTK-typing rules silenced — correct for the experiment, wrong as
the editor-wide default for the testbed's own Python.

Two hard constraints drive the design:

1. **A `pyrightconfig.json` takes precedence over everything and applies to its
   whole folder.** Dropping one at the testbed root would force the entire
   testbed under the experiment's narrowed rules.
2. **When a `pyrightconfig.json` is present, Pylance rejects `python.analysis.*`
   overrides in `settings.json`** (by design — the config is meant to be the
   single source of truth for that folder).

So the experiment config stays a non-default `.experiment.json`, invoked
explicitly via `--project` from tasks. Pylance's normal in-editor analysis of
the testbed is left untouched; the scoped experiment runs on demand against
`../gramps`.

## Install the tools

```bash
# from the testbed root, on your Ubuntu workstation
pip install --break-system-packages pyright semgrep
```

Pyright's CLI needs Node (it ships its own via the pip wheel's bundled runtime
on most platforms; if `pyright --version` fails, install Node 18+).

## Installing the files

**Critical:** VS Code only reads files named *exactly* `tasks.json`, `settings.json`,
and `keybindings.json`. The `.snippet.json` files in `dev-tooling/vscode/` are
deliberately misnamed so they stay **inert** until you place them — they're
templates, because you may already have a `settings.json`, and keybindings live in
your *user* profile (not the workspace). A `settings.snippet.json` sitting in
`.vscode/` does nothing.

For each, the rule is: **rename if you have nothing prior, merge if you do.**

| Source (`dev-tooling/vscode/`) | Goes to | If you have nothing there yet | If you already have one |
| --- | --- | --- | --- |
| `tasks.json` | `.vscode/tasks.json` | copy as-is (already correctly named) | merge the `tasks` array |
| `settings.snippet.json` | `.vscode/settings.json` | `mv` it (rename) | merge its keys by hand |
| `keybindings.snippet.json` | **user** `keybindings.json` | paste the array in | merge the array in |

Concretely, from the testbed root:

```bash
# tasks: correctly named already — just copy
cp dev-tooling/vscode/tasks.json .vscode/tasks.json

# settings: rename if absent, else merge by hand
[ -f .vscode/settings.json ] \
  && echo "you have a settings.json — merge settings.snippet.json's keys into it by hand" \
  || cp dev-tooling/vscode/settings.snippet.json .vscode/settings.json

# keybindings: NOT a workspace file. Open the user keybindings and paste the array:
#   Ctrl+Shift+P -> "Preferences: Open Keyboard Shortcuts (JSON)"
# Do NOT leave a keybindings.snippet.json in .vscode/ — it's inert there.
```

Keybindings are optional — if you don't set them, use `Terminal -> Run Task` from
the palette instead. `.vscode/tasks.json` and `.vscode/settings.json` are committed
(shared) and travel with the testbed.

## Running

- **Command palette:** `Terminal -> Run Task ->` pick one of:
  - `dev-tooling: pyright (scoped None-flow)`
  - `dev-tooling: semgrep (gramps shape patterns)`
  - `dev-tooling: semgrep rule self-test`
  - `dev-tooling: all analyzers` (self-test, then pyright, then semgrep, in sequence)
- **Keybindings** (if merged): `Ctrl+Alt+A` all, `Ctrl+Alt+P` pyright, `Ctrl+Alt+S` semgrep.
- **Findings land in the Problems panel** via the task problem matchers, click to
  jump to the source line in `../gramps`.

## On-save and live scanning

- **Pyright-on-save in-editor is already Pylance** — you get live None/Optional
  squiggles as you type in `../gramps` files (subject to Pylance's own config for
  that folder). The *task* is for running the SCOPED experiment rule set on the
  hot-file allowlist, which Pylance's editor-wide pass does not replicate.
- **Semgrep live/on-save** needs the official Semgrep extension
  (`semgrep.semgrep`). If installed, the `semgrep.scan.configuration` and
  `semgrep.scan.onSave` keys in the settings snippet make its live scan use the
  same rules dir as the task and CI, so editor / pre-commit / CI agree. Without
  the extension, use the task.
- **Generic on-save task running** (firing the pyright task on every save) is not
  native; it needs `emeraldwalk.runonsave` or similar. Not recommended here — the
  scoped pyright run is a deliberate check, not something to fire on every
  keystroke. Bind it to a key instead.

## Relationship to pre-commit and CI

Same three invocations, three tiers, deliberately consistent:

| Tier | What runs | Gate |
| --- | --- | --- |
| Editor (this doc) | tasks + Pylance/Semgrep live | advisory, on demand |
| pre-commit (`.pre-commit-config.experiment.yaml`) | pyright + semgrep `--error` | **blocking** (local, your commits) |
| CI (`.github/workflows/dev-tooling.yml`) | pyright + semgrep + self-test | advisory (informative red) |

The rule self-test is the one check that fails hard at every tier: a rule that
no longer pairs with its labeled fixtures is a tooling regression, not a finding
about gramps.
