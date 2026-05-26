# dev-tooling in Claude Code

Turns the two-analyzer run into one slash command: `/analyze`.

## Install (one-time, per testbed checkout)

```bash
# from the gramps-testbed repo root
mkdir -p .claude/commands
cp dev-tooling/claude-commands/analyze.md .claude/commands/analyze.md
```

`.claude/commands/analyze.md` is project-scoped: committed, shared, and only
available when Claude Code runs in this repo. (Claude Code's newer format is
`.claude/skills/<name>/SKILL.md`, which also supports autonomous invocation —
but `/analyze` is something you trigger deliberately, so the commands/ form is
the right fit. The CLI supports both.)

Add the regenerable output to gitignore (same discipline as `triage/data/`):

```bash
echo "dev-tooling/findings/" >> .gitignore
```

## Use

In a Claude Code session at the testbed root:

```
/analyze                                          # full ../gramps/gramps/gui/ scope
/analyze ../gramps/gramps/gui/widgets/fanchart.py # narrow to one file
```

`/analyze` runs `dev-tooling/claude-commands/analyze.sh`, which writes:

- `dev-tooling/findings/pyright.json`  — full pyright diagnostics (`--outputjson`)
- `dev-tooling/findings/semgrep.json`  — full semgrep results (`--json`)
- `dev-tooling/findings/summary.txt`   — counts, per-rule breakdown, one line per finding

Then Claude Code reads those and produces a triage table classifying each finding
as **real bug** / **GTK-typing noise** / **rule needs narrowing**, per the scope
notes in `NOTES_pylance.md` and `NOTES_semgrep.md`. Triage only — it does not edit
source or write fixes; that stays in the review-gated flow.

## Without the slash command

The script stands alone. Run it directly and point any Claude Code session at the
output file:

```bash
./dev-tooling/claude-commands/analyze.sh
# then in Claude Code:  "read dev-tooling/findings/summary.txt and triage"
```

## Why structured output, not terminal text

The analyzers' pretty terminal output is unparseable (boxes, wrapped lines, line
numbers split from paths) and overflows scrollback. The JSON gives Claude Code
file/line/rule/message as fields; `summary.txt` is the skimmable human view. The
script also flags if NON-Optional pyright rules leak into results — an early
warning that the config's GTK-silencing or `include` scope has regressed, which
`NOTES_pylance.md` calls out as the main noise risk.

## Relationship to the other tiers

| Tier | Trigger | Output |
| --- | --- | --- |
| Claude Code | `/analyze` | structured findings + triage table |
| VS Code | tasks / `Ctrl+Alt+A` | Problems panel |
| pre-commit | `git commit` | blocking, `--error` |
| CI | push / PR | advisory job summary |

All four invoke the same configs (`pyrightconfig.experiment.json`,
`semgrep/rules/`), so editor, command, commit, and CI agree on what fires.
