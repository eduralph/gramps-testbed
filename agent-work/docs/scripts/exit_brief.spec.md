# `exit_brief.py` — script spec

> Suggestion 5 from the streamlining plan. Aggregates `results/issue_*/
> SUMMARY.md` frontmatter for an increment or whole batch and emits a draft
> exit brief using `templates/exit-brief.md.tpl`. Removes the manual
> aggregation step at every increment boundary.

## Purpose
Replace the hand-written exit brief with an auto-populated draft that has
all the structured slices filled (disposition breakdown, patches list,
manual-verification list, deferred decisions, cluster candidates) and only
narrative sections left for the planning chat.

## CLI
```
exit_brief.py <batch> [<scope>]
              [--triage-root <dir>]
              [--out <path>]
              [--dry-run]
```

Required: `<batch>`. Optional `<scope>`:
- `inc-N` for a specific increment
- `all` (default) for the whole batch

| Flag | Default | Meaning |
|---|---|---|
| `--triage-root` | `.` | Root of triage tooling |
| `--out` | `batches/<batch>/EXIT-BRIEF-<scope>.md` | Output path |
| `--dry-run` | off | Emit to stdout instead of writing to file |

Examples:
```
exit_brief.py batch-04-recent-confirmed inc-1
  → batches/batch-04-recent-confirmed/EXIT-BRIEF-inc-1.md

exit_brief.py batch-04-recent-confirmed
  → batches/batch-04-recent-confirmed/EXIT-BRIEF-all.md

exit_brief.py batch-04-recent-confirmed inc-2 --dry-run
  → stdout
```

## Inputs
- `batches/<batch>/INCREMENT-N-<batch>.md` for the IDs in scope (reads YAML
  manifest `ids:`). For scope=all: union of all increment manifests in the
  batch, or fallback to BATCH_INDEX.md selected IDs if no increments yet.
- `results/<batch>/<id>/SUMMARY.md` for each ID in scope. Reads frontmatter.
  Misses (no SUMMARY for a listed ID) become "not yet worked" rows in the
  brief, NOT an error — exit brief is meaningful even when an increment is
  partially done.

## Output structure
Follows `templates/exit-brief.md.tpl` exactly. Sections filled programmatically:
- Header (batch, scope, item count, timestamp, sources)
- Disposition breakdown table (counts + ID lists per disposition)
- Repo/branch split table
- Patches awaiting review (rows from SUMMARYs with `disposition=fix` and `patch.diff` present)
- PRs to open (same set, plus pr-description.md presence check)
- Manual-verification items (rows from SUMMARYs with `manual_verification != null`)
- Deferred decisions (rows from SUMMARYs with `needs_eduard_decision=true`)
- Cluster candidates (computed: IDs sharing any path in `files_touched` or `file_paths_suspected`)
- Cross-cutting notes (any SUMMARY mentioning `results/cross-issue/` reference is collected)
- Open Mantis comments to post (every SUMMARY where `mantis_comment_written=true`)

Sections left as stubs (NARRATIVE markers preserved):
- What went well
- What surprised us
- Posture adjustments for next increment
- Schema / tooling friction surfaced

## Implementation notes
- Stdlib only: same constraints as `reconcile_batches.py`. Shared
  frontmatter parser between the two — extract to a tiny `triage_lib.py`
  with `parse_frontmatter(path) -> dict` to avoid duplication.
- Template substitution: `str.replace` with `{{PLACEHOLDER}}` markers as
  written in the .tpl files. No Jinja, no string.Template — markers are
  unambiguous and the templates are small.
- For sections that take a "list" placeholder (e.g. `{{PATCHES_LIST}}`):
  generate the rows as a markdown table fragment. If the list is empty,
  emit "_(none)_" so the brief reads cleanly.
- Cluster detection: build an inverted index `path -> [ids]` from all
  SUMMARYs in scope; any path with `len(ids) >= 2` produces a cluster row.
  Cap at 10 clusters to avoid overwhelming the brief; "and N more" line if
  truncated.
- Cross-cutting notes: grep SUMMARYs for the string `results/cross-issue/`
  in the prose body; if found, collect the line.

## Use sites
- **End of each increment:** Eduard runs `exit_brief.py <batch> inc-N`,
  reviews draft, fills the NARRATIVE sections in this chat (or directly).
  Output is the increment exit brief.
- **End of batch:** `exit_brief.py <batch>` produces the batch-level brief.
  Same template, broader scope.

## Acceptance
- Returns within 5 seconds for a 38-item batch.
- Handles partially-worked increments (some IDs have SUMMARY, some don't).
- Idempotent: re-running before NARRATIVE edits produces a byte-identical
  draft. After NARRATIVE edits, re-running with `--out` to a fresh path
  produces a fresh draft (does NOT overwrite the edited one without
  explicit `--force`, to be added in v2 if needed; v1 hard-errors on
  output-path-exists unless `--dry-run`).
- Output reads correctly without filling NARRATIVE — every section
  generated is self-contained markdown.
