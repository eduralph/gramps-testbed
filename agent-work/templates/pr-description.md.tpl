# PR description template

> Two shapes below. Claude Code picks based on `target_repo` and deletes the
> other. Both follow the pattern from gramps-testbed/CLAUDE.md but specialise
> for the per-repo conventions observed in recent merges.

## USE IF target_repo == addons-source

### Title format
`{{ADDON}}: {{ONE_LINE_SUMMARY}} (bug {{ID}})`

### Body

#### Summary
Fixes https://gramps-project.org/bugs/view.php?id={{ID}}

{{TWO_OR_THREE_LINE_PROBLEM_STATEMENT}}

#### Root cause
{{ROOT_CAUSE_PARAGRAPH}}

#### Fix
{{FIX_PARAGRAPH}}

Files touched:
{{FILES_TOUCHED_BULLETS}}

#### Test
{{TEST_PARAGRAPH}}

Run with:
```
{{TEST_INVOCATION}}
```

#### Pre-flight
- Merged history on `{{TARGET_BRANCH}}`: {{PREFLIGHT_MERGED_RESULT}}
- Open PRs touching the same code: {{PREFLIGHT_OPEN_PRS}}
- Closed/rejected PRs: {{PREFLIGHT_CLOSED_PRS}}

🤖 Generated with Claude Code

## USE IF target_repo == gramps

### Title format
`{{COMPONENT}}: {{ONE_LINE_SUMMARY}} (bug {{ID}})`

(where `{{COMPONENT}}` is the affected gramps/ subdirectory — e.g.
`gen/lib`, `gui/editors`, `plugins/docgen` — matching upstream convention.)

### Body

#### Summary
Fixes https://gramps-project.org/bugs/view.php?id={{ID}}

{{TWO_OR_THREE_LINE_PROBLEM_STATEMENT}}

#### Root cause
{{ROOT_CAUSE_PARAGRAPH}}

The proximate failure is in `{{PATH_1}}:{{LINE_1}}` — {{ROOT_CAUSE_CITATION}}.

#### Fix
{{FIX_PARAGRAPH}}

Files touched:
{{FILES_TOUCHED_BULLETS}}

#### Test
{{TEST_PARAGRAPH}}

Test location matches the existing `gramps/.../test/` layout convention.

Run with:
```
{{TEST_INVOCATION}}
```

#### Pre-flight
- Merged history on `{{TARGET_BRANCH}}`: {{PREFLIGHT_MERGED_RESULT}}
- Open PRs touching the same code: {{PREFLIGHT_OPEN_PRS}}
- Closed/rejected PRs: {{PREFLIGHT_CLOSED_PRS}}

#### Compatibility
- Does this change public API? {{YES_OR_NO}}
- Affects database schema? {{YES_OR_NO}}
- Forward-port to `master` needed? {{YES_OR_NO_WITH_RATIONALE}}

🤖 Generated with Claude Code
