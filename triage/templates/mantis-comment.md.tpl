# Mantis comment template

> One of the cases below applies. Claude Code picks the right one based on
> `disposition` in the SUMMARY frontmatter, fills the placeholders, and
> deletes the unused cases. Final output: `mantis-comment.md` is the
> single-case text, ready for Eduard to paste verbatim.
>
> Voice: first-person Eduard. Direct, technical, factual. No emoji. No "I
> hope this helps". State the resolution, cite the evidence, stop.

## USE IF disposition == fix

Fixed in commit {{FIXING_COMMIT}} (PR {{FIXING_PR_NUMBER}}) on `{{TARGET_REPO}}` branch `{{TARGET_BRANCH}}`.

Root cause: {{ROOT_CAUSE_ONE_LINE}}

Fix: {{FIX_ONE_LINE}}

Test: {{TEST_ONE_LINE}}

Fixed in version: {{FIXED_IN_VERSION}}

## USE IF disposition == confirm-and-close

Already addressed by commit {{FIXING_COMMIT}} (PR {{FIXING_PR_NUMBER}}) on `{{TARGET_REPO}}` branch `{{TARGET_BRANCH}}`, merged {{MERGE_DATE}}.

Verified against {{TARGET_BRANCH}} at SHA `{{HEAD_SHA}}`: {{VERIFICATION_EVIDENCE_ONE_LINE}}.

Fixed in version: {{FIXED_IN_VERSION}}

Closing as already-fixed.

## USE IF disposition == cant-repro

Could not reproduce on `{{TARGET_REPO}}` branch `{{TARGET_BRANCH}}` (SHA `{{HEAD_SHA}}`).

What was tried:
- {{REPRO_STEP_1}}
- {{REPRO_STEP_2}}
- {{REPRO_STEP_3}}

Observed behaviour: {{OBSERVED_BEHAVIOUR}}.

If you can reproduce on a current build, please reopen with a fresh debug log
(Help → Show debug log) and the exact tree/data that triggers it. Without a
reproducer the defect cannot be diagnosed further.

Closing as cannot-reproduce.

## USE IF disposition == invalid-input

The input that triggered this is malformed: {{INVALID_INPUT_EXPLANATION}}.

A conformant counter-example: {{COUNTER_EXAMPLE_OR_OMIT}}.

If Gramps should accept this input gracefully rather than error, that's a
separate feature request (a more permissive parser / better error message).
Please open a new tracker item for that if you'd like to pursue it.

Closing as invalid-input.

## USE IF disposition == wontfix

This is by-design: {{BY_DESIGN_RATIONALE}}.

Reference: {{DESIGN_DOC_OR_MAINTAINER_DECISION_LINK}}.

Closing as wontfix.

## USE IF disposition == external

The root cause is not in Gramps or addons-source: {{EXTERNAL_EXPLANATION_ONE_LINE}}.

Upstream location: {{EXTERNAL_REPO_URL}}.

Recommended action: please file an issue with the upstream maintainer at the
link above; this tracker cannot drive a fix in their repo.

Closing as external.

## USE IF disposition == manual-verification

Reproducing on Linux did not trigger this defect (Linux being the platform
the triage harness can confirm against). Given it is filed against
{{PLATFORM}}, the next step is a manual verification on that platform.

Detailed repro instructions and expected vs defect behaviour have been
prepared and will be run on {{PLATFORM}} shortly. This tracker entry will be
updated with the outcome (reproduced / could-not-reproduce) once the manual
run completes.

Leaving open pending manual verification on {{PLATFORM}}.

## USE IF disposition == deferred-decision

Diagnosed: {{DIAGNOSIS_ONE_LINE}}.

Fix direction requires a UX/policy decision before code can be written:
{{DECISION_QUESTION}}.

Leaving open pending decision; the diagnosis is captured and the fix can be
written in a follow-up once direction is set.
