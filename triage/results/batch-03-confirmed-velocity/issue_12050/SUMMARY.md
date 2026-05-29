# Issue 12050 — SQLite import "hangs" — close as no-change-required (by design)

## Status
**Close as no-change-required.** No code change.

## Verification
The increment-3 task list called for this item: 12050's results dir was
missing the `mantis-comment.md` Mantis-rule requires (every tracker entry
gets a generated comment). The triage verdict in `MANTIS_ACTIONS.md` already
concluded by-design / wontfix; this artefact generates the actual comment
text from that conclusion.

The relevant evidence is in the tracker thread:
- lordemannd, note ~0061351 (2020): reproduced — the import COMPLETES after
  ~8 hours on ~95k people, not hung. The progress indicator's apparent
  stall is the per-row commit pattern slowing as the database grows.
- prculley, note ~0061365 (addon maintainer): "the [SQLite addon's]
  normalized table format is inherently slow by design — the core
  database uses blobs for exactly this reason." Importing back via
  the blob-backed core path is fast; the XML round-trip is the
  practical workflow.

## Repo and branch
- Repo: addons-source (`Sqlite/` addon)
- Branch: maintenance/gramps60 — no commit; close-only.
- This batch: no patch.diff, no pr-description.md.

## Mantis link
- Tracker: https://gramps-project.org/bugs/view.php?id=12050
- Status to set: resolved / no change required
- Fixed in version: N/A (close-only)
- Comment: see `mantis-comment.md` (ready-to-paste).

## Notes for next reviewer
- The thread also surfaces a legitimate small follow-up — an "Abort import"
  button — flagged in the comment as a separate feature request, not part
  of this close. Eduard's call whether to file it.
- This is the closure artefact the increment-2 scaffolding pass left
  unfilled (results/issue_12050/ existed but was empty).
