---
schema_version: 1
id: {{ID}}
title: "{{TITLE}}"
batch: {{BATCH}}
increment: null
disposition: null               # one of: fix | confirm-and-close | cant-repro | invalid-input | wontfix | external | manual-verification | deferred-decision
target_repo: null               # one of: addons-source | gramps | external | none
target_branch: null             # one of: maintenance/gramps60 | maintenance/gramps61 | master | null
addon: null                     # null for core; "<AddonName>" for addons-source
external_repo_url: null
file_paths_suspected: []
cluster_with: []
existing_pr:
  number: null
  repo: null
  state: null
flags: {{AUTO_FLAGS}}            # populated by make_handoff from heuristics
needs_fixture: false
mantis_severity: {{SEVERITY}}
mantis_version_reported: {{VERSION}}
---

# Issue {{ID}}: {{TITLE}}

## Tracker report (from CSV)

- **Project:** {{PROJECT}}
- **Reporter:** {{REPORTER}}
- **Severity:** {{SEVERITY}}
- **Reproducibility:** {{REPRODUCIBILITY}}
- **Product version:** {{VERSION}}
- **Category:** {{CATEGORY}}
- **Date submitted:** {{DATE_SUBMITTED}}
- **OS / Platform:** {{OS}} / {{PLATFORM}}
- **Status:** {{STATUS}}
- **Updated:** {{UPDATED}}

### Description
{{DESCRIPTION}}

### Steps to reproduce
{{STEPS_TO_REPRODUCE}}

### Additional information
{{ADDITIONAL_INFORMATION}}

## Scraped comment thread ({{NOTE_COUNT}} notes)

{{SCRAPED_NOTES}}

## TRIAGE VERDICT

> Fill the frontmatter above, then write free-prose notes here covering:
> root cause hypothesis, pre-flight requirements (merged + closed PRs to
> check), scope warnings (DO NOT BUNDLE ...), test strategy and location,
> repro requirements (does example.gramps trigger it, or is a fixture needed),
> any cluster relationship to other IDs in this batch.
>
> The frontmatter is the structured slice for scripts to read. The prose
> below is what Claude Code reads when executing this item.

{{VERDICT_NOTES}}
