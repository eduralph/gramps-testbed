# `reconcile_batches.py` — script spec

> Suggestion 4 from the streamlining plan. Given a Mantis CSV export, reports
> which IDs have already been worked in prior batches and what the outcomes
> were, so the new-batch candidate pool excludes already-disposed items.
> Eliminates the "MajorBugs.csv was a different cut than batch-03's source"
> failure mode.

## Purpose
Cross-reference a fresh Mantis CSV against `batches/*/BATCH_INDEX.md` and
`results/*/<id>/SUMMARY.md` (using their YAML frontmatter). Output: what's
been worked, what hasn't, and a fresh candidate pool ready for the next batch.

## CLI
```
reconcile_batches.py <mantis-csv-path>
                     [--triage-root <dir>]
                     [--json]
                     [--show-worked]
                     [--show-pending]
```

Required: `<mantis-csv-path>`.

| Flag | Default | Meaning |
|---|---|---|
| `--triage-root` | `.` | Root of triage tooling (contains `batches/`, `results/`) |
| `--json` | off | Emit JSON instead of human-readable text |
| `--show-worked` | off | List the worked IDs with their dispositions |
| `--show-pending` | off | List the still-pending items (manual-verif, deferred) |

## Output (human-readable, default)
```
=== reconcile_batches.py results ===
CSV:        20260530-Mantis_Export.csv
CSV rows:   250
Triage root: gramps-testbed/triage
Batches scanned: batch-01, batch-02, batch-03, batch-04
Generated:  2026-05-30T09:00:00Z

--- Worked in prior batches ---
[64 IDs total across 4 batches]

  batch-04-recent-confirmed: 38 IDs
    fix: 14   confirm-and-close: 10   cant-repro: 5
    invalid-input: 1   wontfix: 0   external: 3
    manual-verification: 4   deferred-decision: 1
  batch-03-...: 14 IDs
    fix: 9    confirm-and-close: 2    cant-repro: 3
  ...

--- Still pending (not yet fully resolved) ---
[5 IDs]
- 13983 (manual-verification, batch-04, platform=macOS)
- 13774 (manual-verification, batch-04, platform=macOS)
- 13864 (deferred-decision, batch-04, question="Dashboard column cap UX")
- ...

--- New candidate pool ---
[186 IDs not in any prior batch and not currently pending]
  by Product Version:
    6.0.5: 12   6.0.4: 8    6.0.3: 9    6.0.2: 4    6.0.1: 18
    6.0.0: 7    5.2.x: 38   5.1.x: 21   5.0.x: 18   <=4.x: 51
  by Severity:
    block: 0    major: 14   minor: 87   text: 22   feature: 0   trivial: 38
    tweak: 25
  by Category (top 5):
    GUI: 41    Database: 28   3rd Party Addons: 24
    File Formats: 18   Tools: 15

--- Summary ---
CSV total:        250
Worked (closed):  59
Still pending:     5
New candidates:  186
```

## Output (`--json`)
```json
{
  "csv_path": "20260530-Mantis_Export.csv",
  "csv_rows": 250,
  "generated_at": "2026-05-30T09:00:00Z",
  "worked": [
    {"id": 13819, "batch": "batch-04-recent-confirmed", "disposition": "fix", ...},
    ...
  ],
  "pending": [
    {"id": 13983, "batch": "batch-04-recent-confirmed", "disposition": "manual-verification", "platform": "macOS"},
    ...
  ],
  "new_candidates": {
    "ids": [...],
    "by_version": {...},
    "by_severity": {...},
    "by_category": {...}
  }
}
```

## Implementation notes
- Stdlib only: `csv`, `argparse`, `pathlib`, `re`, `json`, `datetime`,
  `collections`. YAML parsing: there is no stdlib YAML — implement a minimal
  frontmatter parser (split on first `---`, second `---`; parse the keys we
  care about). The frontmatter is small and the schema is fixed; full YAML
  isn't needed and avoids a `PyYAML` dependency.
- Scans:
  - `{triage_root}/batches/*/BATCH_INDEX.md` for batch-level metadata.
  - `{triage_root}/results/*/issue_*/SUMMARY.md` for per-item dispositions.
  - Fallback: if a BATCH_INDEX or SUMMARY lacks frontmatter (pre-migration),
    warn and skip — don't fail. List unmigrated files at the end.
- "Pending" = disposition is `manual-verification` or `deferred-decision` AND
  no superseding SUMMARY has resolved it. (For v1, simple semantics:
  most-recent SUMMARY per ID wins.)
- Profiling section: re-uses the bucket logic from doc 05 step 1 (Product
  Version, Severity, Category). The output supports the next-batch character
  decision directly.

## Use sites
- **Before any new batch:** run `reconcile_batches.py 20260530-Mantis_Export.csv`
  to see what's new vs. worked. The output's "New candidate pool" + profiling
  is the doc 05 step 1 output, free.
- **During a batch:** re-run with `--show-pending` to see what's still
  outstanding from prior batches.

## Acceptance
- Returns within 5 seconds for a 250-row CSV + 4 prior batches.
- Handles pre-migration files gracefully (warn-and-skip, don't fail).
- JSON output passes `python -m json.tool`.
- Idempotent: re-running on the same CSV without intervening changes produces
  byte-identical output.
