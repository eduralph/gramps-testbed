# Playbook deltas — `05-batch-selection-process.md`

> Changes to fold into the playbook once Phase F completes. Doc 05 is the
> selection-and-preparation source of truth; these deltas insert
> `reconcile_batches.py` into Step 1 and update Steps 6-7 for the new
> generator behaviour.

## Delta 1 — Step 1 is now scripted

Today's Step 1:

> ## Step 1 — profile the pool before selecting
> Never select "the next N rows." Profile first ...

Replace with:

> ## Step 1 — profile the pool with `reconcile_batches.py`
>
> Run `reconcile_batches.py <new-csv-path>` from the triage root. The
> script's output is exactly what this step needed:
>
> - **Worked in prior batches** — which IDs are off the table because
>   they've been disposed (with disposition breakdown per batch).
> - **Still pending** — items left in `manual-verification` or
>   `deferred-decision` state; these are NOT new candidates, they're
>   carryover work.
> - **New candidate pool** — IDs not in any prior batch and not pending,
>   with the by-Version / by-Severity / by-Category profiling that this
>   step previously required by hand.
>
> The pool is the working set. The profiling decides character (Step 2).
>
> The "MajorBugs.csv was a different cut than batch-03's source" failure
> mode from batch-04 prep is impossible under this flow — the script
> reads the prior batches directly, so the CSV being a different cut
> shows up as the script reporting different "Worked in prior batches"
> counts than expected.

## Delta 2 — Step 6 simplifies

Today's Step 6 covers the run-batch.sh tooling. Amend the description of
what `make_handoff.py` produces:

> `scripts/make_handoff.py` — merges the dated CSV (`data/*.csv`) + scraped
> notes into `batches/<batch>/`:
> - one `issue_<id>.md` per issue, with v1 YAML frontmatter (empty
>   verdict-pass fields) + the existing prose scaffold;
> - `BATCH_INDEX.md` with v1 frontmatter (batch metadata, bucket counts
>   start at 0);
> - `CLAUDE_CODE_BRIEF.md` (unchanged);
> - `INCREMENT-1-<batch>.md` as a STUB with `ids: []` in the manifest —
>   to be filled during Step 7.
>
> No-clobber by default, so re-running to add IDs never destroys a
> filled-in verdict.

## Delta 3 — Step 7 makes the verdict structured

Today's Step 7:

> ## Step 7 — fill verdicts, then hand to triage (doc 04)
> The generated `issue_<id>.md` files carry an empty TRIAGE VERDICT. Fill
> each ...

Replace with:

> ## Step 7 — fill verdicts (structured slice + prose), then hand to triage
>
> Each `issue_<id>.md` has v1 YAML frontmatter (empty verdict-pass fields)
> followed by the tracker report, scraped thread, and a TRIAGE VERDICT
> prose section. The verdict pass fills BOTH:
>
> **Frontmatter (structured slice — for scripts):**
> - `disposition` — pick from the 8-value enum; can be `null` if still
>   undecided (Claude Code will defer the item back if so).
> - `target_repo` / `target_branch` — addon → addons-source / gramps60;
>   core → gramps / gramps61. Per item, not uniform.
> - `addon` — addon name if target_repo=addons-source; else null.
> - `cluster_with` — IDs of related items in this batch (NOT a fix-
>   bundling instruction; a hint that shared root cause is plausible and
>   should be verified before treating as one fix).
> - `existing_pr` — if `preflight_prs.py` surfaced one, capture
>   number/repo/state here. Claude Code will re-check at execution time
>   in case state changed.
> - `flags` — auto-populated by make_handoff; refine if needed.
> - `needs_fixture` — true if example.gramps doesn't trigger the bug.
>
> **Prose (narrative — for the human reading it):**
> - Root-cause hypothesis (what the thread + description + auto-flags
>   suggest is going on).
> - Pre-flight requirements (which paths to check; which closed PRs to
>   look at — if `preflight_prs.py` already covered this, cite the
>   output).
> - Scope warnings ("DO NOT BUNDLE this with X" if a related-looking
>   item is actually a different cause; "FIXTURE NEEDED" if a synthetic
>   tree is required).
> - Test strategy and location (per the doc 04 rules — addon unit, GUI
>   interface, or core unittest).
>
> Then fill the `INCREMENT-1-<batch>.md` manifest's `ids:` list with the
> first increment's IDs. Subsequent increments (2, 3, 4) get drafted in
> the planning chat after looking at the verdict outcomes — they are NOT
> auto-generated.

## Delta 4 — common-failure-modes section gets a new entry

Add to "Common failure modes" at the end of doc 05:

> - **Stale `existing_pr` in VERDICT.** The verdict pass captures a
>   snapshot of PR state; Claude Code may execute days later. Claude Code
>   must re-query `preflight_prs.py` at execution time on any item where
>   `existing_pr` is non-null, not trust the snapshot.
> - **Frontmatter drift from prose.** If the verdict pass updates the
>   prose ("on reflection this is core, not addon") but forgets to update
>   the frontmatter (`target_repo` still says `addons-source`), the
>   scripts and Claude Code disagree. Treat frontmatter as authoritative;
>   if Claude Code finds prose contradicting frontmatter, it MUST stop
>   and flag rather than guess.
> - **Bucket counts in BATCH_INDEX frontmatter going stale.** If items
>   move buckets during verdict filling (a D becomes an A on further
>   thought), update the `buckets:` counts in the frontmatter. The
>   `reconcile_batches.py` profiler reads these.

## Delta 5 — pipeline scripts list at the end of doc 05

Add a new sub-section near the end:

> ## Scripts used in this phase (Step 1 → Step 7)
>
> - `reconcile_batches.py` — Step 1, profile the pool from a fresh CSV.
> - `run-batch.sh` (wraps `mantis_notes.py` + `make_handoff.py`) — Step 6,
>   scrape + generate batch artefacts.
> - `preflight_prs.py` — Step 7, fill `existing_pr` in VERDICT frontmatter
>   for items where the thread links a PR.
>
> Per-increment / per-item scripts (`exit_brief.py`, in-loop
> `preflight_prs.py`) belong to doc 04, not here.
