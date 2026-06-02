# Manual verification — issue {{ID}}

> Run this on {{PLATFORM}}. Follow the numbered steps; the decision tree at
> the bottom picks which Mantis comment to paste. Both comments are pre-
> written below — paste whichever the outcome matches.
>
> If this file exists, the SUMMARY.md for issue {{ID}} flags
> "MANUAL VERIFICATION REQUIRED" at the top. The triage chain treats this
> item as not-yet-closed until the manual step runs.

## What manual step is required and why
{{MANUAL_STEP_DESCRIPTION}}

Why it can't be automated:
{{CANNOT_AUTOMATE_REASON}}

## Platform(s) to test
{{PLATFORMS_LIST}}

## Environment
- **Gramps build:** {{GRAMPS_BUILD}}
- **Branch / version under test:** {{BRANCH_OR_VERSION}}
- **Addon (if relevant) and version:** {{ADDON_AND_VERSION}}
- **Theme / locale / config that matter:** {{ENV_KNOBS}}

## Numbered repro steps

1. {{STEP_1}}
2. {{STEP_2}}
3. {{STEP_3}}
4. {{STEP_4}}
5. {{STEP_5}}

(Add or remove as needed. Each step should be concrete enough that someone
who hasn't read the tracker thread can follow it.)

## Expected vs defect behaviour

| | What you should see | What the bug shows |
|---|---|---|
| {{ASPECT_1}} | {{EXPECTED_1}} | {{DEFECT_1}} |
| {{ASPECT_2}} | {{EXPECTED_2}} | {{DEFECT_2}} |

## What to capture
- {{CAPTURE_1}} (e.g. screenshot of the dialog)
- {{CAPTURE_2}} (e.g. terminal output of `gramps -d` or AIO console)
- {{CAPTURE_3}} (e.g. error report text from Help → Report a bug)

Attach to the Mantis ticket alongside the comment paste.

## Decision tree

```
Did the defect reproduce per the expected-vs-defect table?
├── YES → paste "Comment A: reproduced" below
│         outcome: {{NEXT_STEP_IF_REPRODUCED}}
│         (e.g. file a follow-up fix issue scoped to {{PLATFORM}};
│         or escalate to {{COMPONENT}} maintainer)
│
└── NO  → paste "Comment B: could not reproduce" below
          outcome: close as cant-repro on {{PLATFORMS_LIST}}
```

## Comment A: reproduced (paste verbatim if defect reproduced)

```
Reproduced on {{PLATFORM}} ({{ENVIRONMENT_RECAP}}).

Steps that triggered it:
{{STEP_RECAP}}

Observed: {{OBSERVED_DEFECT}}.
Expected: {{EXPECTED_BEHAVIOUR}}.

Captured: {{CAPTURED_ARTIFACTS_LIST}}.

Marking this confirmed and proceeding with {{NEXT_STEP_IF_REPRODUCED}}.
```

## Comment B: could not reproduce (paste verbatim if defect did NOT reproduce)

```
Could not reproduce on {{PLATFORM}} ({{ENVIRONMENT_RECAP}}) following the
steps in the original report.

What was tried:
{{STEP_RECAP}}

Observed: {{OBSERVED_NON_DEFECT}}.

If you can still reproduce on a current build, please reopen with:
- exact Gramps version (Help → About);
- the data or tree that triggers it;
- a fresh debug log (Help → Show debug log).

Closing as cannot-reproduce on {{PLATFORMS_LIST}}.
```

## Notes for Eduard
{{NOTES_FOR_EDUARD_OR_NONE}}
