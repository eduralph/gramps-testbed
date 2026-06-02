---
schema_version: 1
id: {{ID}}
batch: {{BATCH}}
increment: {{INCREMENT}}
disposition: {{DISPOSITION}}
target_repo: {{TARGET_REPO}}
target_branch: {{TARGET_BRANCH}}
addon: {{ADDON_OR_NULL}}
files_touched: {{FILES_TOUCHED}}
test_added: {{TEST_ADDED}}
test_paths: {{TEST_PATHS}}
fixing_commit: null
fixing_pr:
  number: null
  repo: null
fixed_in_version: null
verified_against_branch: {{TARGET_BRANCH}}
verified_against_sha: {{HEAD_SHA}}
mantis_comment_written: true
manual_verification: {{MANUAL_VERIFICATION_FILE_OR_NULL}}
needs_eduard_decision: {{NEEDS_EDUARD_DECISION}}
eduard_decision_question: {{EDUARD_DECISION_QUESTION_OR_NULL}}
---

# Issue {{ID}} — {{TITLE_SHORT}}

## Outcome
{{ONE_LINE_OUTCOME}}

## Root cause
{{ROOT_CAUSE_NARRATIVE}}

## Fix
{{FIX_NARRATIVE}}

## Test
{{TEST_NARRATIVE}}

## Verification
- Target branch: `{{TARGET_BRANCH}}` at SHA `{{HEAD_SHA}}`
- Path:line citations:
  - `{{PATH_1}}:{{LINE_1}}` — {{CONTEXT_1}}
  - `{{PATH_2}}:{{LINE_2}}` — {{CONTEXT_2}}
- Test invocation: `{{TEST_INVOCATION}}`
- Result: {{TEST_RESULT}}

## Pre-flight
- Merged history checked: `{{PREFLIGHT_MERGED_CMD}}` — {{PREFLIGHT_MERGED_RESULT}}
- Open PRs checked: {{PREFLIGHT_OPEN_PRS}}
- Closed/rejected PRs checked: {{PREFLIGHT_CLOSED_PRS}}

## Artefacts in this directory
- `SUMMARY.md` (this file)
- `patch.diff` ({{PATCH_PRESENT_OR_ABSENT}})
- `pr-description.md` ({{PR_DESC_PRESENT_OR_ABSENT}})
- `tracker-comment.md` (ready to paste verbatim)
- `MANUAL-VERIFICATION.md` ({{MV_PRESENT_OR_ABSENT}})

## Decisions for Eduard
{{EDUARD_DECISIONS_OR_NONE}}

---

## Section guide for Claude Code
- `disposition: fix` → all sections above filled; patch.diff + pr-description.md exist.
- `disposition: confirm-and-close` → Fix/Test/Verification describe what was verified, not patched; patch.diff absent; pr-description.md absent.
- `disposition: cant-repro` → Root cause section says "could not reproduce"; Verification documents what was tried; patch.diff absent.
- `disposition: manual-verification` → MANUAL-VERIFICATION.md exists and is referenced at top; the human step is flagged in Outcome.
- `disposition: deferred-decision` → Eduard Decisions section is filled with the question; no patch.
- `disposition: external` → Outcome cites the upstream repo/URL; tracker-comment.md points reporter there.
- `disposition: invalid-input` / `wontfix` → Outcome explains why; counter-example included if useful.
