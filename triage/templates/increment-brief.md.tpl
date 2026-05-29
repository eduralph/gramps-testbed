---
schema_version: 1
batch: {{BATCH}}
increment: {{INCREMENT_NUMBER}}
ids: {{IDS_LIST}}
target_repo_dominant: {{TARGET_REPO_DOMINANT}}
target_branch_dominant: {{TARGET_BRANCH_DOMINANT}}
posture_notes_carryover_from: {{CARRYOVER_INCREMENT_OR_NULL}}
launched_at: null
closed_at: null
---

# Claude Code increment — {{BATCH}}, INCREMENT {{INCREMENT_NUMBER}}

> Read alongside CLAUDE_CODE_BRIEF.md (binding) and each issue_<id>.md verdict.
> Standing rules apply: trust the verdict over the title; resolve addon-vs-core
> by reproducing; repro-or-close before fixing; check merged AND closed PRs;
> one logical fix per issue with a test in the same change; STOP after writing
> results (no push/PR/ready-mark — Eduard's review gate).

## Batch POSTURE
{{POSTURE_NOTES}}

## Items in this increment ({{ITEM_COUNT}}, dominant target {{TARGET_REPO_DOMINANT}}/{{TARGET_BRANCH_DOMINANT}})
Worked in this order.

{{PER_ITEM_SECTIONS}}

(Each per-item section follows the pattern:
### {{ID}} — {{TITLE_SHORT}}{{LEAD_MARKER_IF_LEAD}}
{{ROOT_CAUSE_HINT_FROM_VERDICT}}
{{PRE_FLIGHT_REQUIREMENTS}}
{{SCOPE_AND_FIX_GUIDANCE}}
{{TEST_LOCATION_AND_STRATEGY}}
{{CLUSTER_OR_DEFERRAL_NOTES}}
)

## Per-item: write results/issue_<id>/ then STOP
Each item: SUMMARY.md (root cause, fix/close, test, repo+branch, outcome),
patch.diff (if a fix), pr-description.md (if a PR is warranted),
mantis-comment.md (ALWAYS), MANUAL-VERIFICATION.md (REQUIRED for any manual-
work outcome). STOP for review; no push/PR/ready-mark.

## Expected shape
{{EXPECTED_OUTCOMES_NARRATIVE}}

## Decision points worth flagging back to Eduard
{{DECISION_POINTS}}

## Increment closure
This is increment {{INCREMENT_NUMBER}} of {{TOTAL_INCREMENTS}} in {{BATCH}}.
After this increment closes, run `exit_brief.py {{BATCH}} inc-{{INCREMENT_NUMBER}}`
to produce the exit brief; review and finalise; then{{NEXT_INCREMENT_OR_BATCH_CLOSURE}}.
