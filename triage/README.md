# triage/ — automated Mantis bug triage → Claude Code handoff

Replaces the manual `work/`-folder flow (hand-downloaded tracker PDFs) with a
scripted pipeline: pull a batch of Mantis bugs, attach their comment threads,
triage them into per-issue briefs with a verdict, and hand the in-tree ones to
Claude Code for fix-with-test.

This lives in `gramps-testbed` on purpose: the testbed is the neutral hub that
reads its sibling forks (`../gramps`, `../addons-source`) without polluting them,
and it already owns the test harness a fix's regression test plugs into.

## Layout

```
triage/
├── data/        Gramps_<date>.csv         dated raw Mantis exports (never edited)
├── notes/       issue_<id>.json           scraped Mantis comment threads
├── batches/
│   └── batch-NN-<theme>/
│       ├── CLAUDE_CODE_BRIEF.md           entry instructions (defers to ../../CLAUDE.md)
│       ├── BATCH_INDEX.md                 TOC + auto-flags + triage checklist
│       ├── issue_<id>.md                  report + scraped notes + TRIAGE VERDICT
│       └── results/issue_<id>/            Claude Code writes here (SUMMARY/patch/PR)
└── scripts/
    ├── mantis_notes.py                    Playwright scraper for Mantis comment threads
    └── make_handoff.py                    CSV + notes -> per-issue briefs
```

## The CSV export (manual, one-time per refresh)

The scripted scrape can't get past Cloudflare for bulk reads, but Mantis's own
authenticated **CSV export** goes through fine (it's a logged-in action, not an
anonymous page fetch). To get bug *bodies* in the export, configure the columns
first — they're not on by default:

  My Account → Manage Columns → add `description`, `steps_to_reproduce`,
  `additional_information` to the **CSV Columns** list → save.

Then View Issues → filter → CSV Export. Drop the file in `data/` with a date.
(The export cannot include comment threads — that's what `mantis_notes.py` is for.)

## Pulling comment threads (mantis_notes.py)

The bug tracker sits behind Cloudflare, which challenges plain HTTP clients but
lets a real browser through. `mantis_notes.py` drives a real Chrome and rides the
Cloudflare clearance your own session earns — it does NOT defeat the challenge,
it passes it the normal way. Two modes:

**Launch mode** (simpler, but Cloudflare may loop on the automation flags):
```
python3 scripts/mantis_notes.py --channel chrome --ids 13830,14051
```

**Attach mode** (reliable — fixes the Cloudflare verification loop):
```
# Terminal 1: start YOUR Chrome, pass Cloudflare + log in by hand once
google-chrome --remote-debugging-port=9222 --user-data-dir=/tmp/cfprofile \
  "https://gramps-project.org/bugs/view.php?id=13830"

# Terminal 2: attach to it
python3 scripts/mantis_notes.py --attach http://127.0.0.1:9222 --ids 13830,14051 --out notes
```

Writes `notes/issue_<id>.json`. The note-parsing selectors are calibrated against
the current Mantis skin; if a future skin change empties the `notes` array, inspect
one comment's DOM in Chrome devtools and adjust `extract_issue()`.

Note: this is for **Mantis bug** comments. The repo's separate `fetch_comments.py`
pulls **GitHub PR** comments via `gh` — different source, different stage.

## Generating a batch (make_handoff.py)

```
python3 scripts/make_handoff.py \
    --csv data/Gramps_2026-05-23.csv \
    --notes-dir notes \
    --ids 13830,14051 \
    --batch batch-01-graphview \
    --batches-dir batches
```

Produces one `issue_<id>.md` per ID (report + scraped notes + an empty VERDICT
scaffold), plus `BATCH_INDEX.md` and `CLAUDE_CODE_BRIEF.md`. Auto-flags warn when
notes mention an external repo, an upstream root cause, a core-code traceback, or
a possible existing fix — cheap signals the human verdict confirms or overrides.

## Filling verdicts (human / planning chat)

The scaffold is empty by design — the verdict is judgment, not extraction. For
each issue decide: actionable? which repo (addon vs core vs external — this picks
the PR target)? does the reporter's workaround match the real defect, or mask it?
repro on example.gramps? where does the test go? See `issue_13830.md` for a worked
example — note it explicitly flags that the reporter's config-key workaround is
NOT the live gramps61 defect, and that the addon-vs-core question must be resolved
by reproducing before any code is written.

## Handing off to Claude Code

1. Prune EXTERNAL-REPO / UPSTREAM issues from the batch (not fixable in the forks).
2. Confirm every surviving issue has a filled verdict (BATCH_INDEX checklist).
3. Launch Claude Code **from the gramps-testbed root** (so `../addons-source` and
   `../gramps` are reachable and session history stays in one CWD).
4. Point it at the batch: have it read
   `triage/batches/<batch>/CLAUDE_CODE_BRIEF.md` and work the issues per their
   verdicts.
5. It writes fix + test in the sibling repo and a summary to
   `results/issue_<id>/`, then STOPS at Eduard's review gate (no push/PR).

## Conventions this pipeline honours

- Branch target for fixes: `maintenance/gramps61` (per CLAUDE.md; master is
  feature-only).
- Tests are stdlib `unittest.TestCase`. Unit-testable addon fixes go in
  `addons-source/<Addon>/tests/test_*.py` (loaded dotted-path `<Addon>.tests.<module>`;
  create `tests/__init__.py` if the addon lacks one). GUI-only fixes go in
  `tests/interface/test_bug_<id>_<slug>.py` here.
- Edit addon SOURCE only, never the installed plugin dir.
- Reproduce on example.gramps; never use real family data.
- Eduard's review gate: Claude Code commits and stops; pushing/PRs are manual.
```
