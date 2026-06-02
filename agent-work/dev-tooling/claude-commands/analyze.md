---
description: Run the scoped pyright + semgrep analyzers against ../gramps and triage the findings
allowed-tools: Bash(./agent-work/dev-tooling/claude-commands/analyze.sh:*), Read, Grep
---

Run the dev-tooling analyzers and triage what they find.

## Steps

1. Run the analyzer wrapper from the repo root:
   `./agent-work/dev-tooling/claude-commands/analyze.sh $ARGUMENTS`
   (No argument = full `../gramps/gramps/gui/` scope. An argument narrows the
   semgrep target to a specific path, e.g. `/analyze ../gramps/gramps/gui/widgets/fanchart.py`.)

2. Read `agent-work/dev-tooling/findings/summary.txt` for the counts and per-rule breakdown,
   then `agent-work/dev-tooling/findings/pyright.json` and `agent-work/dev-tooling/findings/semgrep.json`
   for the full findings.

3. Triage against the fault-line corpus and the tools' documented scope (see
   `agent-work/dev-tooling/README.md`, `agent-work/dev-tooling/pyright/NOTES_pylance.md`,
   `agent-work/dev-tooling/semgrep/NOTES_semgrep.md`). For each finding classify it as:
   - **real bug** — a genuine None-flow / post-disposal defect. Cite the file:line,
     the likely fault-line class (A1 sentinel / A2 disposal / A3 boundary-null), and
     whether it resembles a known issue (13091, 13326, fanchart, etc.).
   - **GTK-typing noise** — pyright flagging a None on a GTK object (tag, child
     widget). `NOTES_pylance.md` predicts these for styledtexteditor; they are
     EXPECTED weak results, not action items. Do not propose fixes; note that the
     `include` may need narrowing instead.
   - **rule needs narrowing** — a semgrep finding on correct code (false positive).
     The bar is zero-FP; a FP means the rule needs tightening, not the code.

4. If `summary.txt` shows the leaked-rule warning (NON-Optional rules appearing),
   surface that FIRST — it means the pyright config's silencing or `include` scope
   regressed, which must be fixed before any finding is trustworthy.

## Output

A short triage table: file:line | classification | fault-line class | note.
Then, only for the **real bug** rows, a one-line suggested next step per the
testbed conventions (reproduce against example.gramps first, branch target per
`CLAUDE.md`, regression test destination). Do NOT edit any source or write any
fix in this command — triage only. Fixes follow the normal review-gated flow.
