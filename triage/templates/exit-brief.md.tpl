# Exit brief — {{BATCH}}{{SCOPE_SUFFIX}}

> Auto-populated by `exit_brief.py {{BATCH}} {{INCREMENT_OR_BLANK}}`.
> Narrative sections (marked NARRATIVE) are stubs; fill them in this chat
> before closing the increment / batch. Everything else is computed from
> the SUMMARY.md frontmatter under `results/`.

## Header
- **Batch:** {{BATCH}}
- **Scope:** {{SCOPE_DESCRIPTION}} (e.g. "increment 2" or "entire batch")
- **Generated:** {{TIMESTAMP}}
- **Items in scope:** {{ITEM_COUNT}}
- **Sources:** {{LIST_OF_RESULTS_DIRS}}

## Disposition breakdown

| Disposition | Count | IDs |
|---|---|---|
| fix | {{N_FIX}} | {{IDS_FIX}} |
| confirm-and-close | {{N_CONFIRM}} | {{IDS_CONFIRM}} |
| cant-repro | {{N_CANT_REPRO}} | {{IDS_CANT_REPRO}} |
| invalid-input | {{N_INVALID}} | {{IDS_INVALID}} |
| wontfix | {{N_WONTFIX}} | {{IDS_WONTFIX}} |
| external | {{N_EXTERNAL}} | {{IDS_EXTERNAL}} |
| manual-verification | {{N_MANUAL}} | {{IDS_MANUAL}} |
| deferred-decision | {{N_DEFERRED}} | {{IDS_DEFERRED}} |

Total: {{ITEM_COUNT}}

## Repo / branch split

| target_repo | target_branch | Count | IDs |
|---|---|---|---|
| addons-source | maintenance/gramps60 | {{N_ADDON60}} | {{IDS_ADDON60}} |
| gramps | maintenance/gramps61 | {{N_CORE61}} | {{IDS_CORE61}} |
| external | n/a | {{N_EXTERNAL_REPO}} | {{IDS_EXTERNAL_REPO}} |
| none | n/a | {{N_NONE}} | {{IDS_NONE}} |

## Patches awaiting your review (push gate)
{{PATCHES_LIST}}

Each row: ID, target_repo/target_branch, files_touched, path to patch.diff.

## PRs to open
{{PRS_TO_OPEN_LIST}}

Each row: ID, target_repo, suggested title, path to pr-description.md.

## Manual-verification items pending your run
{{MANUAL_VERIFICATION_LIST}}

Each row: ID, platform(s), path to MANUAL-VERIFICATION.md.

## Deferred decisions needing your call
{{DEFERRED_DECISIONS_LIST}}

Each row: ID, the question, path to SUMMARY.md (Decisions for Eduard section).

## Cluster candidates flagged
{{CLUSTER_CANDIDATES}}

Items where two or more SUMMARYs share `file_paths_suspected` or
`files_touched`. Worth confirming whether the fixes are independent or
should consolidate before pushing.

## Cross-cutting notes
{{CROSS_CUTTING_NOTES_LIST}}

Items where SUMMARY.md or VERDICT mentioned a cross-issue theme (e.g.
Gramps-Web compatibility, docgen-LaTeX class). Worth a separate write-up at
`results/cross-issue/<theme>.md`.

## NARRATIVE — increment retrospective

> Fill these in the planning chat before closing the increment.

### What went well
{{...}}

### What surprised us
{{...}}

### Posture adjustments for the next increment
{{...}}

### Schema / tooling friction surfaced
{{...}}

## Open Mantis comments to post
{{MANTIS_COMMENTS_TO_POST_LIST}}

Each row: ID, disposition, path to mantis-comment.md. Eduard pastes each
verbatim into the corresponding tracker entry; mark posted as you go.

## Next steps
- [ ] Review patches in `Patches awaiting your review`.
- [ ] Open PRs from `PRs to open`.
- [ ] Run manual-verification items on the listed platforms.
- [ ] Post Mantis comments for all items.
- [ ] Decide on deferred items; rerun increment with chosen direction if needed.
- [ ] Apply learnings to next increment brief (edit INCREMENT-(N+1) if needed).
- [ ] Launch next increment.
