---
description: Mine the triage batch results for recurring fix shapes and propose new analyzer rules
allowed-tools: Bash(python3 agent-work/dev-tooling/claude-commands/extract_corpus.py:*), Read, Grep
---

Analyze the fixed-bug corpus and produce feedback for the analyzer ruleset.

## Steps

1. Extract structured facts from all batches:
   `python3 agent-work/dev-tooling/claude-commands/extract_corpus.py $ARGUMENTS`
   (No argument = all batches under `agent-work/batches/`. An argument scopes to one
   batch dir, e.g. `/corpus-feedback agent-work/batches/batch-03-confirmed-velocity`.)

2. Read `agent-work/dev-tooling/findings/corpus.json`. Each issue record has: status,
   repo/branch, whether a patch exists, the `Fixes #` trailer, the diffstat, the
   actual added/removed hunk lines, and new test files. The `analyzer_reachable`
   and `edit_shape` fields are UNSET — you assign them.

3. **Partition first.** Split issues into: fixed-with-code (has_patch), and
   non-fix (already-fixed / cant-repro / wontfix / invalid / duplicate). Report
   the partition counts. The non-fix set is NOT a rule source — but report what
   fraction of the corpus it is, because it tells Eduard how much of the real bug
   population is even analyzer-shaped.

4. **For the fixed-with-code set, classify each by edit shape** from the hunk
   lines. Don't use a fixed taxonomy — derive shapes from what you see. Examples
   of shapes that have appeared or are expected: None-guard-added, disconnect-
   added-in-cleanup, attribute-reorder/init-order-fix, uncomment-stale-block,
   loop-invariant-hoist, signature/API-rename, import-path-fix, logic-rewrite.
   For each fix, tag:
   - **edit_shape** — a short label for what the patch structurally did.
   - **analyzer_reachable** — which tool COULD catch this shape at authoring time:
     `semgrep` (a structural/shape idiom), `pyright` (a type/None-flow fact),
     `codeql` (path-sensitive flow), or `none` (logic/behavioral — no static
     analyzer catches "this feature silently does nothing"; 13955 is `none`).

5. **Cluster and rank.** Group the fixed set by edit_shape. Output a ranked table:
   shape | count | analyzer | example issue IDs | existing-rule? | rule-worth-writing?
   Rank by recurrence among the *analyzer-reachable* shapes — that ranking IS the
   rule backlog, ordered by payoff.

6. **Cross-check the existing rule.** The one shipped rule is
   `gramps-connect-without-disconnect` (A2 disposal, foreign-lifetime connects).
   How many corpus fixes match its shape? If many, it earns its keep; if one, it
   was a teaching example, not a recurring pattern. Note this explicitly.

## Output

A) Partition summary (fixed-with-code vs non-fix, with the analyzer-shaped fraction).
B) The ranked edit-shape table.
C) For the top 1-3 analyzer-reachable shapes with NO existing rule: a concrete
   proposal — which tool, the rough pattern/idiom to match, and which corpus issues
   would serve as positive controls (and any post-fix state as negative controls).
   Do NOT write the rule here; this command produces the BACKLOG, not the rules.
   Writing a rule is a separate, deliberate step against its labeled controls.

Honor the README's bar: a shape worth a rule recurs AND is reachable AND can hit
zero false positives. A one-off, or a logic bug no analyzer can see, is not a rule —
say so plainly rather than inventing a rule for it.
