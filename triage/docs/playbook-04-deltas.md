# Playbook deltas — `04-bug-batch-triage-playbook.md`

> Changes to fold into the playbook once Phase F (script implementation)
> completes. Doc 04 is the per-item-workflow source of truth; these deltas
> insert the v1 schema and the new scripts as first-class citizens.

## Delta 1 — preflight is now scripted

Today's playbook says:

> **Pre-flight: check upstream isn't ahead — merged AND closed PRs**
> Before writing a fix, check BOTH: merged history (`git log <branch> -- <path>`)
> ... and closed / rejected PRs ...

Replace with:

> **Pre-flight: check upstream isn't ahead — merged AND closed PRs.**
> Run `preflight_prs.py --repo <target_repo> --path <suspected_path>` and
> capture the output into SUMMARY.md's Pre-flight section. The script
> returns merged history + open PRs + closed/rejected PRs in one call.
> When `existing_pr` is non-null in the VERDICT frontmatter, also fetch
> that PR's current state — the verdict snapshot may be stale.
>
> A closed PR is signal, not noise. (RebuildTypes was deleted per the
> author's request, discovered via a closed PR — the lesson stands.) The
> script's "Suggested action" line surfaces this; do not ignore it.

## Delta 2 — verdict and SUMMARY are now structured

Insert under "Per-item workflow":

> **VERDICT and SUMMARY both carry v1 YAML frontmatter** (see
> `schema/verdict-schema.md`). Claude Code reads the VERDICT frontmatter as
> structured input (disposition, target_repo, target_branch, cluster_with,
> existing_pr, flags) and emits SUMMARY frontmatter as structured output
> (disposition, files_touched, test_added, verified_against_sha, etc).
>
> The frontmatter is the structured slice. The prose body below it is the
> narrative — root cause, fix, test, verification, decisions. Both matter;
> the scripts read the frontmatter, the human reads the prose, and both
> must stay in sync.

## Delta 3 — templates are first-class

Insert under "Disposition outcomes":

> Each disposition has a corresponding mantis-comment template case in
> `templates/mantis-comment.md.tpl`. Claude Code picks the case matching
> the SUMMARY's `disposition` value, fills the placeholders from the
> SUMMARY frontmatter + prose, and writes the result as
> `results/issue_<id>/mantis-comment.md`. The user pastes verbatim.
>
> Same pattern for `pr-description.md` (template per `target_repo`) and
> `MANUAL-VERIFICATION.md` (single template, all platforms).

## Delta 4 — exit brief is auto-populated

Replace today's loose "batch hygiene" notes near the end with:

> **Increment exit briefs are auto-populated.** At the end of each
> increment, run `exit_brief.py <batch> inc-N`. The script reads every
> SUMMARY.md frontmatter under `results/<batch>/<id>/`, aggregates the
> dispositions, lists patches awaiting review, manual-verifications
> pending, deferred decisions, and cluster candidates, then emits a
> draft `EXIT-BRIEF-inc-N.md`. The structured sections are filled; the
> NARRATIVE sections (what went well / what surprised us / posture
> adjustments) are stubs to fill in the planning chat before closing.
>
> Same script with no scope argument produces the batch-level exit brief
> at the end. Re-running before NARRATIVE edits produces a byte-identical
> draft.

## Delta 5 — new section: "Where scripts run"

Add a new sub-section near the end of the playbook:

> ## Where scripts run
>
> - **`mantis_notes.py`** — once per batch, in scrape step (run-batch.sh).
>   Scrapes Mantis comment threads via Playwright + attached Chrome.
> - **`make_handoff.py`** — once per batch, in generation step (run-batch.sh).
>   Emits BATCH_INDEX, per-issue verdicts, increment-1 stub.
> - **`preflight_prs.py`** — once per item in Claude Code; output captured
>   into SUMMARY.md Pre-flight section. Also run at verdict time to fill
>   `existing_pr` in the VERDICT frontmatter.
> - **`reconcile_batches.py`** — once per new-batch planning session, in
>   this chat. Output drives doc 05's step 1 (profile the pool) for free.
> - **`exit_brief.py`** — once per increment close + once per batch close.
>
> No scripts run during the v1→v2 migration except `migrate_v1_to_v2.py`
> (one-shot, archived after batch-04 closes).

## Delta 6 — manual-verification language tightens

Today's prose has variable wording for the MANUAL-VERIFICATION.md
requirement. Replace all variants with a single canonical paragraph:

> Any triage outcome requiring manual work — visual sign-off, post-merge
> GUI repro, or OS-specific verification (Windows/macOS, where Linux can't
> confirm) — must:
> 1. Flag "MANUAL VERIFICATION REQUIRED" at the top of SUMMARY.md.
> 2. Drop `results/issue_<id>/MANUAL-VERIFICATION.md` from
>    `templates/MANUAL-VERIFICATION.md.tpl`, fully filled.
> 3. Set `manual_verification: <filename>` in SUMMARY frontmatter.
> 4. Pre-write BOTH mantis comments (confirmed / could-not-confirm) in
>    MANUAL-VERIFICATION.md — the eventual paste is whichever the manual
>    run yields.
>
> Uniform filename across platforms. Uniform template. Uniform frontmatter
> field.

## Delta 7 — disposition vocabulary canonicalised

Today's playbook uses slightly different terms in different sections
("can't reproduce" / "cannot reproduce" / "cant-repro"; "by-design" /
"wontfix"; "external" / "upstream"). Canonicalise to the schema enum:

| Schema value | Replaces |
|---|---|
| `fix` | "Fixed" |
| `confirm-and-close` | "Already fixed upstream" |
| `cant-repro` | "Can't reproduce" / "Cannot reproduce" / "can't repro" |
| `invalid-input` | "Invalid input" |
| `wontfix` | "By-design" / "wontfix" / "By-design / wontfix" |
| `external` | "External" / "Not a Gramps/addon defect" |
| `manual-verification` | (new — was implicit "manual run required") |
| `deferred-decision` | (new — was implicit "needs UX call") |

Use the schema value in any structured reference; prose can still use the
phrase ("the fix path", "we confirmed and closed") for readability.
