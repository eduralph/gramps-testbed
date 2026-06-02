# Verdict schema (v1)

> Source of truth for all YAML frontmatter in the triage pipeline.
> Files: `issue_<id>.md` (VERDICT), `results/issue_<id>/SUMMARY.md`,
> `INCREMENT-N-<batch>.md` (manifest), `BATCH_INDEX.md` (batch header).
>
> Schema version: 1. Additive changes are allowed; breaking changes require
> a version bump and a parallel parser branch.

## Common enums (used across documents)

### disposition
| Value | Meaning |
|---|---|
| `fix` | Write a patch + test; PR to target_repo/target_branch. |
| `confirm-and-close` | Already fixed upstream; cite commit/PR, mantis-close. |
| `cant-repro` | Repro failed on target branch with evidenced steps. |
| `invalid-input` | Reporter's input was the cause; counter-example may help. |
| `wontfix` | By-design / maintainer-declined. |
| `external` | Not a gramps/addons-source defect (upstream lib, OS, etc). |
| `manual-verification` | Pending Eduard's macOS/Windows run; pre-written comments shipped. |
| `deferred-decision` | Pending Eduard's UX/policy call; diagnosis only. |

`manual-verification` and `deferred-decision` are PENDING states — they resolve
to one of the other 6 once the manual step runs or the call is made. SUMMARY.md
keeps the pending value; the eventual resolution is captured in the mantis
comment that gets posted.

### target_repo
| Value | Notes |
|---|---|
| `addons-source` | gramps-project/addons-source. Default branch maintenance/gramps60. |
| `gramps` | gramps-project/gramps. Default branch maintenance/gramps61. |
| `external` | An external repo; record-and-stop. Use `external_repo_url` to point. |
| `none` | No repo (e.g. cant-repro with no target). |

### target_branch
| Value | When |
|---|---|
| `maintenance/gramps60` | target_repo=addons-source default |
| `maintenance/gramps61` | target_repo=gramps default |
| `master` | Forward-port work only; explicit Eduard call required |
| `null` | target_repo=external or none |

### flags (list, may be empty)
| Value | Meaning |
|---|---|
| `EXTERNAL-REPO` | Source code lives in a non-gramps-project repo |
| `UPSTREAM` | Root cause is upstream of Gramps (GTK, Pango, reportlab, ...) |
| `CORE-TRACE` | Symptom in addon, traceback through gramps/... |
| `POSSIBLY-FIXED` | Comment thread suggests a release may have addressed it |
| `NO-NOTES` | Mantis thread empty; only the description signal |
| `NEEDS-FIXTURE` | example.gramps doesn't trigger; synthetic fixture required |
| `NEEDS-EDUARD-DECISION` | UX/policy/risk-acceptance call before any code |

## Document: `issue_<id>.md` (VERDICT)

Top of file:

```yaml
---
schema_version: 1
id: 13819
title: "Family Edit window changes the order of parent families"
batch: batch-04-recent-confirmed
increment: 1
disposition: fix
target_repo: gramps
target_branch: maintenance/gramps61
addon: null                          # null for core; "GraphView" etc for addon
external_repo_url: null              # set only when target_repo=external
file_paths_suspected:                # best-effort, root-cause source files
  - gramps/gen/lib/familyref.py
  - gramps/gen/lib/childref.py
cluster_with: []                     # IDs sharing root cause
existing_pr:                         # null if none
  number: null
  repo: null
  state: null                        # open | merged | closed | null
flags: []
needs_fixture: false
mantis_severity: major
mantis_version_reported: 6.0.1
---
```

Below the frontmatter: the tracker report (CSV-derived), scraped thread, and
free-prose root-cause / pre-flight / scope notes the human wrote during the
verdict pass. The frontmatter is the structured slice; the prose is the
narrative.

## Document: `results/issue_<id>/SUMMARY.md`

Top of file:

```yaml
---
schema_version: 1
id: 13819
batch: batch-04-recent-confirmed
increment: 1
disposition: fix                     # final disposition for this run
target_repo: gramps
target_branch: maintenance/gramps61
addon: null
files_touched:                       # files actually changed by the patch
  - gramps/gen/lib/childref.py
  - gramps/gen/lib/test/childref_test.py
test_added: true
test_paths:
  - gramps/gen/lib/test/childref_test.py
fixing_commit: null                  # filled after Eduard pushes
fixing_pr:                           # filled after Eduard opens
  number: null
  repo: null
fixed_in_version: null               # filled when version is known
verified_against_branch: maintenance/gramps61
verified_against_sha: a1b2c3d        # git rev-parse HEAD at fix time
mantis_comment_written: true
manual_verification: null            # filename if MANUAL-VERIFICATION.md exists
needs_eduard_decision: false
eduard_decision_question: null       # the question if needs_eduard_decision=true
---
```

Below the frontmatter: root cause, fix description, test description,
verification (path:line citations), outcome. Same fields as today's hand-
written SUMMARYs.

## Document: `INCREMENT-N-<batch>.md`

Top of file:

```yaml
---
schema_version: 1
batch: batch-04-recent-confirmed
increment: 1
ids: [13819, 13747, 13716, 13832, 13418, 13326]
target_repo_dominant: gramps         # for branch-coherence checks
target_branch_dominant: maintenance/gramps61
posture_notes_carryover_from: null   # increment N where the POSTURE first appeared, or null
launched_at: null                    # ISO timestamp, filled at launch
closed_at: null                      # ISO timestamp, filled at exit brief
---
```

The rest of the file is the existing prose increment brief (POSTURE, per-item,
expected shape, decision points). Unchanged in structure; just gains the
manifest header.

## Document: `BATCH_INDEX.md`

Top of file:

```yaml
---
schema_version: 1
batch: batch-04-recent-confirmed
character: fix-oriented              # fix-oriented | hygiene | blended
source_csv: 20260523-Mantis_Export.csv
source_csv_rows: 253
selected_ids_count: 38
non_defects_dropped: [12757, 13354, 13404, 13470, 13839]
buckets:
  A: 12                              # core defects, Linux-confirmable
  B: 10                              # addon defects, Linux-confirmable
  C: 2                               # clusters
  D: 7                               # repro-or-close
  E: 7                               # platform-specific
increments_planned: 4
increments_launched: 1               # bumped as increments fire
created_at: 2026-05-23T12:00:00Z
---
```

Below the frontmatter: the existing markdown table layout. The frontmatter
gives reconcile_batches.py what it needs to do set ops; the table stays
human-readable.

## Document field-level rules

- All `id` fields are integers (Mantis IDs), no quotes.
- All `*_paths` and `file_paths_suspected` are POSIX-style relative paths from
  the relevant repo root (e.g. `gramps/gen/lib/childref.py`, not absolute).
- All ISO timestamps use `Z` UTC. No timezone offsets.
- Empty lists are `[]`, not omitted. Empty strings are `""` (rare). Null is
  `null`, not absent — explicit null is parseable, absent is ambiguous.
- Unknown fields are ignored by parsers (forward-compatibility). Parsers warn
  but do not fail.
- Required vs optional: see the per-document tables below. All other fields
  are optional with sensible defaults.

### `issue_<id>.md` required fields
schema_version, id, title, batch, disposition, target_repo, target_branch.

### `results/issue_<id>/SUMMARY.md` required fields
schema_version, id, batch, increment, disposition, target_repo,
target_branch, files_touched, test_added, verified_against_branch,
verified_against_sha, mantis_comment_written.

### `INCREMENT-N-<batch>.md` required fields
schema_version, batch, increment, ids.

### `BATCH_INDEX.md` required fields
schema_version, batch, character, source_csv, selected_ids_count.

## Validation

A `validate_schema.py` script (out of v2 scope, suggested for v3) can be added
later. For v1, parsers in `reconcile_batches.py` and `exit_brief.py` validate
their inputs at read time and emit warnings; they tolerate missing optional
fields and warn on missing required ones.
