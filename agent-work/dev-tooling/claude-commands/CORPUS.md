# agent-work/dev-tooling/claude-commands — corpus mining: fixed bugs → rule feedback fixed bugs for rule feedback

Turns the triage batch results into an empirically-ranked rule backlog: which new
analyzer rules to write, ordered by how often that fix-shape actually recurred.

## Why

The fault-line corpus (13091, 13326, fanchart…) is a hand-picked teaching set for
the A1/A2/A3 classes. The batch results are the *actual fixed-bug population*. The
difference matters: many real fixes are logic/behavioral bugs no static analyzer
can catch (e.g. 13955 — a feature silently did nothing because a block was
commented out since 2010). Mining the real corpus tells you what fraction is even
analyzer-shaped, and which shapes recur enough to justify a rule — instead of
guessing from the teaching set.

## Two pieces

- `extract_corpus.py` — mechanical extractor. Walks `agent-work/batches/**/results/
  issue_*/`, emits one structured JSON record per issue: status, repo/branch,
  patch presence, `Fixes #` trailer, diffstat, the actual hunk lines, new test
  files. No judgment — it does NOT hardcode signature regexes. Output:
  `agent-work/dev-tooling/findings/corpus.json` (gitignore it; regenerable).
- `corpus-feedback.md` — Claude Code slash command. Runs the extractor, reads the
  JSON, classifies each fix by edit-shape and analyzer-reachability, clusters and
  ranks, cross-checks the existing rule, and proposes the top new rules with their
  positive/negative controls. Produces the BACKLOG, not the rules.

The split is deliberate: mechanical extraction in Python (testable, deterministic),
pattern-recognition in the model (reads the hunks, assigns shape + reachability).

## Install

```bash
cp agent-work/dev-tooling/claude-commands/corpus-feedback.md .claude/commands/
echo "agent-work/dev-tooling/findings/" >> .gitignore
```

## Use

```
/corpus-feedback                                          # all batches
/corpus-feedback agent-work/batches/batch-03-confirmed-velocity   # one batch
```

Output: partition summary (analyzer-shaped fraction of the corpus), a ranked
edit-shape table, and concrete rule proposals for the top reachable shapes that
have no rule yet — each with the corpus issues that would serve as controls.

## The loop this closes

```
triage → fix (with regression test) → batch results
                                            │
                              /corpus-feedback mines them
                                            │
                       ranked backlog of analyzer-reachable shapes
                                            │
                  write the top rule against its corpus controls
                                            │
                     /analyze runs it → catches the NEXT one at authoring time
```

A fix-shape that recurs becomes a rule; the rule catches the next instance before
it's filed. That's the testbed's "backlog shrinks without re-growing" thesis,
applied to the analyzer ruleset.

## Honest limits

- The extractor was validated against the one real `format-patch` diff available
  (13955) and one `SUMMARY.md` (13065). The status vocabulary and diff format may
  vary across batches; `STATUS_PATTERNS` in the script is the place to extend when
  a new status phrasing or `unknown` shows up in the rollup.
- It reads `Fixes #NNNN` trailers and diffstats; if a batch stored patches in a
  non-`format-patch` shape, the per-file/hunk extraction degrades gracefully
  (counts may be off) but the hunk-line capture still feeds the model the code.
