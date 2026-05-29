#!/usr/bin/env python3
"""
make_handoff.py — turn a triaged batch of Mantis issues into a Claude Code brief,
fitted to gramps-testbed conventions.

Pipeline (all inside gramps-testbed/triage/):
  1. (this chat) select candidate IDs, score for actionability
  2. scripts/mantis_notes.py --ids <batch>   -> triage/notes/issue_<id>.json
  3. THIS SCRIPT: merge triage/data/<csv> + triage/notes/ -> triage/batches/<batch>/
  4. (this chat / Eduard) fill the TRIAGE VERDICT in each issue_<id>.md
  5. launch Claude Code from gramps-testbed/, point it at the batch folder

Design choices specific to this testbed:
  - The per-batch CLAUDE_CODE_BRIEF.md DEFERS to ../CLAUDE.md for the upstream-fix
    workflow (branch targeting, PR format, review gate) instead of duplicating it.
  - Test-location guidance matches the real convention:
      * unit-testable addon fix -> addons-source/<Addon>/tests/test_*.py
        (loaded dotted-path as <Addon>.tests.<module>; create tests/ + __init__.py
        if absent — e.g. GraphView has none yet)
      * GUI-only fix -> gramps-testbed/tests/interface/test_bug_<id>_<slug>.py
        with a fixture at tests/interface/data/bug_<id>_minimal.gramps
      * core fix -> gramps/gen/.../test/ following gramps' own layout
  - Branch target default is maintenance/gramps61 (current production per CLAUDE.md).

Usage (from gramps-testbed/triage/):
  python3 scripts/make_handoff.py \
      --csv data/Gramps_2026-05-23.csv \
      --notes-dir notes \
      --ids 13830,14051 \
      --batch batch-01-graphview-config \
      --batches-dir batches
"""

import argparse
import json
import re
from pathlib import Path

TRACKER = "https://gramps-project.org/bugs/view.php?id="
# Branch target is NOT uniform across a batch — it is resolved PER ITEM by where
# the fix lands: addons-source -> maintenance/gramps60, gramps core ->
# maintenance/gramps61. There is therefore no single correct default; the verdict
# scaffold presents BOTH and forces the human to delete the wrong one. (A prior
# hardcoded gramps61 default silently contaminated every addon item in a batch and
# had to be sed'd out by hand — do not reintroduce a single default.)
BRANCH_ADDONS = "maintenance/gramps60"
BRANCH_CORE = "maintenance/gramps61"


def norm(raw):
    return str(raw).strip().lstrip("0") or "0"


def load_notes(notes_dir, iid):
    f = notes_dir / f"issue_{iid}.json"
    if not f.exists():
        return None
    try:
        return json.loads(f.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return None


def clean_note_blocks(rec):
    """The Mantis scraper stores 'author\\n\\n date\\n\\n role  ~noteid' in the
    field KEY and the note body as the value. Recover (author, date, text)."""
    out = []
    for k, v in (rec.get("fields", {}) or {}).items():
        parts = [p.strip() for p in re.split(r"\n+", k) if p.strip()]
        author = parts[0] if parts else ""
        date = ""
        for p in parts[1:]:
            m = re.search(r"\d{4}-\d{2}-\d{2}[\d :]*", p)
            if m:
                date = m.group(0).strip()
                break
        out.append({"author": author, "date": date, "text": v.strip()})
    if not out:
        for n in rec.get("notes", []) or []:
            out.append(
                {
                    "author": n.get("author", ""),
                    "date": n.get("date", ""),
                    "text": (n.get("text") or "").strip(),
                }
            )
    return out


# Auto-flags: cheap first-pass warnings the human verdict confirms/overrides.
EXT_REPO = re.compile(r"FamilyTreeView|github\.com/ztlxltl|CardView|/cdhorn/", re.I)
UPSTREAM = re.compile(r"gitlab\.gnome\.org|upstream bug|Pango|GTK issue", re.I)
FIXED = re.compile(
    r"released v|fixed in|now resolved|adds a fallback|just released", re.I
)
CORE = re.compile(r"gramps[/\\]gen[/\\]|gramps\.gen\.|/filters/|_genericfilter", re.I)


def auto_flags(row, notes):
    blob = " ".join(n["text"] for n in notes) + " " + row.get("Summary", "")
    flags = []
    if EXT_REPO.search(blob):
        flags.append(
            "EXTERNAL-REPO: fix may live outside addons-source — NOT a Claude Code target here"
        )
    if UPSTREAM.search(blob):
        flags.append(
            "UPSTREAM: root cause may be Gramps core / GTK / Pango, not the addon"
        )
    if CORE.search(blob):
        flags.append(
            "CORE-TRACE: traceback passes through gramps/gen — fix may belong in ../gramps, not the addon"
        )
    if FIXED.search(blob):
        flags.append(
            "POSSIBLY-FIXED: a comment mentions a release/fix — verify upstream isn't ahead before working"
        )
    if not notes:
        flags.append(
            "NO-NOTES: no tracker discussion scraped (may be unengaged / low signal)"
        )
    return flags


VERDICT_SCAFFOLD = f"""## ===== TRIAGE VERDICT (fill before handoff) =====

- **Actionable?** yes / no / deferred —
- **Where does the fix go?** addons-source (in-tree) / gramps core (../gramps) / external repo / upstream — (this decides the PR target repo; resolve before coding)
- **Branch target (resolve by where the FIX lands, not the symptom):** addons-source → {BRANCH_ADDONS} | gramps core → {BRANCH_CORE} — DELETE THE WRONG ONE
- **Root cause (one line):**
- **Does the reporter's workaround match the real root cause?** (verify — the symptom on their machine may differ from the defect in current source)
- **Fix sketch:**
- **Repro on example.gramps?** yes / no — (how:)
- **Test location & type:**
  - unit-testable addon -> `addons-source/<Addon>/tests/test_*.py` (create tests/ + __init__.py if absent; loaded as `<Addon>.tests.<module>`)
  - GUI-only -> `gramps-testbed/tests/interface/test_bug_<id>_<slug>.py` (+ fixture `tests/interface/data/bug_<id>_minimal.gramps`)
  - core -> `gramps/gen/.../test/` (gramps' own layout)
- **Related issues / commits / upstream PRs to read first:**
- **Check upstream isn't already ahead:** (grep result —)
"""


def issue_brief(row, notes):
    iid = norm(row["Id"])
    flags = auto_flags(row, notes)
    flag_md = (
        "\n".join(f"- [warn] {f}" for f in flags) if flags else "- (none auto-detected)"
    )

    notes_md = ""
    for i, n in enumerate(notes, 1):
        hdr = " - ".join(x for x in [n["author"], n["date"]] if x)
        notes_md += f"\n**Note {i}** ({hdr})\n\n{n['text']}\n\n---\n"
    if not notes_md:
        notes_md = "\n_(no notes scraped)_\n"

    return f"""# Issue #{iid} — {row.get('Summary','').strip()}

| field | value |
|---|---|
| Category | {row.get('Category','')} |
| Severity | {row.get('Severity','')} |
| Reproducibility | {row.get('Reproducibility','')} |
| Product Version | {row.get('Product Version','')} |
| Status | {row.get('Status','')} |
| Submitted | {row.get('Date Submitted','')} |
| Tracker | {TRACKER}{iid} |

## Auto-detected flags
{flag_md}

## Description
{row.get('Description','').strip() or '_(empty)_'}

## Steps to Reproduce
{row.get('Steps To Reproduce','').strip() or '_(empty)_'}

## Additional Information
{row.get('Additional Information','').strip() or '_(empty)_'}

## Tracker discussion (Mantis notes, scraped)
{notes_md}

{VERDICT_SCAFFOLD}"""


CLAUDE_CODE_BRIEF = f"""# Claude Code working brief — Mantis bug batch: {{batch}}

You are running from the **gramps-testbed** repo. Three sibling repos are reachable
via additionalDirectories: `../gramps`, `../addons-source`, `../addons`.

## Authoritative conventions — read these, do not re-derive
- **`../gramps-testbed/CLAUDE.md`** — the Upstream fix workflow section is binding:
  branch targeting (addons-source→{BRANCH_ADDONS}, gramps core→{BRANCH_CORE}, NOT
  master, NOT uniform — resolve per item by where the fix lands), "edit source never the
  plugin dir", reproduce against example.gramps first, the PR description format, the
  Mantis cross-link syntax, and **Eduard's review gate (you commit and STOP — no
  pushing, no opening PRs, no marking ready unless explicitly instructed)**.
- **`../gramps/AGENTS.md`** and **`../addons-source/AGENTS.md`** — authoritative
  inside those repos. The "do not edit ../gramps or ../addons-source without explicit
  instruction" rule in CLAUDE.md holds; working a batch issue IS that instruction,
  scoped to the specific addon/file named in the verdict.

## What this batch is
Triaged Mantis bugs, one `issue_<id>.md` per issue. Each has the tracker report,
the scraped comment thread, and a human-written TRIAGE VERDICT. **Trust the verdict
over the title and over the reporter's workaround** — several of these bugs are
mislabeled by their summary, and a reporter's workaround often masks a different
root cause than the live defect in current source.

## Hard rules for this batch
1. **Honour the verdict's "Where does the fix go?".** addons-source / gramps core /
   external / upstream are DIFFERENT PR targets. If external or upstream, do NOT
   attempt a fix — record the finding and stop. If the verdict is unsure between
   addon and core, RESOLVE THAT FIRST by reproducing; it changes the repo.
2. **Reproduce before fixing**, on example.gramps. Never request Eduard's real data.
3. **Ship the means to verify** (per CLAUDE.md): a test in the same change.
   - unit-testable addon fix -> `addons-source/<Addon>/tests/test_*.py`
     (create `tests/__init__.py` if the addon has none — e.g. GraphView). It will be
     loaded as `<Addon>.tests.<module>` (dotted path) by run-addon-unit.sh / CI.
   - GUI-only fix -> `tests/interface/test_bug_<id>_<slug>.py` here in the testbed,
     subclassing `GrampsInterfaceTestCase`, with a minimal fixture at
     `tests/interface/data/bug_<id>_minimal.gramps` if a seeded tree is needed.
   - core fix -> a `unittest.TestCase` in gramps' own `.../test/` layout.
4. **One logical fix per issue.** No bundling (CLAUDE.md: bundling hides mistakes).
5. **Verify against the target branch's code and cite path:lines** (CLAUDE.md).
   "Applies cleanly" is not "remains correct" across gramps60/61/master.
6. **Check upstream isn't already ahead — merged AND closed/rejected PRs.** A
   closed PR is signal, not noise: the maintainer may have decided to delete the
   addon or declined this fix shape (e.g. RebuildTypes was deleted per the
   author's request, discovered only via a closed PR). Check BOTH merged history
   and closed PRs before declaring a bug unfixed or writing a fix.

## Per-issue workflow
1. Read `issue_<id>.md`, especially the VERDICT and its root-cause caveat.
2. Resolve the repo question (addon vs core) by reproducing on example.gramps.
3. Write a failing test capturing the bug, in the location the verdict specifies.
4. Fix until it passes; run the relevant suite:
   - addon:    `../gramps-testbed/scripts/ubuntu/run-addon-unit.sh <Addon>`
   - interface:`../gramps-testbed/scripts/ubuntu/run-interface.sh`
5. Write results to `results/issue_<id>/`:
   - `SUMMARY.md` — root cause, fix, test, repo+branch targeted
   - `patch.diff` — the change (in the sibling repo; do not commit it for Eduard)
   - `pr-description.md` — following CLAUDE.md's PR format exactly
   - `mantis-comment.md` — ready-to-paste tracker comment, in Eduard's voice
     (he pastes it verbatim). REQUIRED for every item that has a Mantis tracker
     entry, regardless of outcome (fix, cannot-reproduce, already-fixed,
     wontfix, invalid-input). State the resolution, the fixing commit and/or PR
     if any, and "Fixed in version" where applicable. Do not just reference
     MANTIS_ACTIONS.md — generate the actual comment text (templates there are a
     starting point, not a substitute). Exempt only: items with NO Mantis entry
     (e.g. detector (c)-bucket items), which note "no Mantis issue" instead.
   - `MANUAL-VERIFICATION.md` — REQUIRED for ANY manual-work outcome: visual
     sign-off (e.g. dark-mode/contrast), post-merge GUI repro, or OS-specific
     verification (macOS/Windows, where Linux can't confirm — Windows GUI
     automation is paused, no UIA tree). Uniform filename across all such cases.
     Also flag the required human step PROMINENTLY at the top of SUMMARY.md.
     Contains: what manual step + why it can't be automated; platform(s);
     exact environment; numbered repro steps; expected-vs-defect; what to
     capture; a decision tree; and BOTH pre-written Mantis comments (confirmed
     / could-not-confirm) so whichever way it goes, the paste is ready.
6. STOP. Eduard reviews, then decides on commit/push/PR.

## Reminders from project conventions
- Run Gramps from an EXTERNAL terminal, not the VS Code integrated one (GLIBC/Snap).
- Gramps does not follow symlinks for plugin discovery; the auto-sync task copies
  source -> installed plugin one way. Edit source only.
- All tests are stdlib `unittest.TestCase` — pytest is never introduced.

See `BATCH_INDEX.md` for the issue list and triage status.
"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--csv", required=True)
    ap.add_argument("--notes-dir", default="notes")
    ap.add_argument("--ids", required=True, help="comma-separated issue IDs")
    ap.add_argument(
        "--batch", required=True, help="batch folder name, e.g. batch-01-graphview"
    )
    ap.add_argument("--batches-dir", default="batches")
    ap.add_argument(
        "--clobber",
        action="store_true",
        help="Overwrite existing issue_<id>.md briefs. Default is to SKIP "
        "issues whose brief already exists, so re-running to add IDs "
        "never destroys a filled-in TRIAGE VERDICT.",
    )
    args = ap.parse_args()

    # stdlib csv (no pandas) — keeps the triage scripts dependency-free,
    # matching the testbed's stdlib-only discipline. Index rows by normalized id.
    import csv

    by_id = {}
    with open(args.csv, newline="", encoding="utf-8-sig") as fh:
        reader = csv.DictReader(fh)
        for raw_row in reader:
            row = {(k.strip() if k else k): (v or "") for k, v in raw_row.items()}
            by_id[norm(row.get("Id", ""))] = row

    ids = [norm(x) for x in args.ids.split(",") if x.strip()]
    notes_dir = Path(args.notes_dir)
    batch_dir = Path(args.batches_dir) / args.batch
    (batch_dir / "results").mkdir(parents=True, exist_ok=True)

    index_rows = []
    for iid in ids:
        row = by_id.get(iid)
        if row is None:
            print(f"#{iid}: not in CSV, skipping")
            continue
        brief_path = batch_dir / f"issue_{iid}.md"
        if brief_path.exists() and not args.clobber:
            print(
                f"#{iid}: brief exists, SKIPPING (use --clobber to overwrite). "
                f"Verdict preserved."
            )
            (batch_dir / "results" / f"issue_{iid}").mkdir(parents=True, exist_ok=True)
            # still include it in the index
            rec = load_notes(notes_dir, iid)
            notes = clean_note_blocks(rec) if rec else []
            flags = auto_flags(row, notes)
            index_rows.append(
                (
                    iid,
                    row.get("Summary", "")[:55],
                    len(notes),
                    "; ".join(f.split(":")[0] for f in flags),
                )
            )
            continue
        rec = load_notes(notes_dir, iid)
        notes = clean_note_blocks(rec) if rec else []
        brief_path.write_text(issue_brief(row, notes), encoding="utf-8")
        (batch_dir / "results" / f"issue_{iid}").mkdir(parents=True, exist_ok=True)
        flags = auto_flags(row, notes)
        index_rows.append(
            (
                iid,
                row.get("Summary", "")[:55],
                len(notes),
                "; ".join(f.split(":")[0] for f in flags),
            )
        )
        print(f"#{iid}: brief written ({len(notes)} notes, {len(flags)} flags)")

    idx = f"# Batch: {args.batch}\n\n| ID | Summary | Notes | Auto-flags |\n|---|---|---|---|\n"
    for iid, summ, nn, fl in index_rows:
        idx += f"| [{iid}](issue_{iid}.md) | {summ} | {nn} | {fl} |\n"
    idx += "\n## Triage checklist (do before launching Claude Code)\n"
    idx += "- [ ] Every issue has a filled TRIAGE VERDICT\n"
    idx += "- [ ] EXTERNAL-REPO / UPSTREAM issues removed from the batch (not fixable here)\n"
    idx += "- [ ] Each issue's repo target (addon vs core) is resolved or flagged for repro\n"
    idx += "- [ ] Each surviving issue repros on example.gramps (no private data)\n"
    idx += "- [ ] Branch target confirmed PER ITEM (addons-source->gramps60, core->gramps61 — NOT uniform)\n"
    idx += "- [ ] Pre-flight checked merged AND closed/rejected PRs before any fix\n"
    idx += "- [ ] Platform-specific items (macOS/Windows) flagged for MANUAL-VERIFICATION.md\n"
    (batch_dir / "BATCH_INDEX.md").write_text(idx, encoding="utf-8")
    (batch_dir / "CLAUDE_CODE_BRIEF.md").write_text(
        CLAUDE_CODE_BRIEF.format(batch=args.batch), encoding="utf-8"
    )

    print(
        f"\nWrote {len(index_rows)} briefs + BATCH_INDEX.md + CLAUDE_CODE_BRIEF.md to {batch_dir}/"
    )
    print(
        "NEXT: fill TRIAGE VERDICT in each issue_*.md, prune non-in-tree, then point Claude Code at the batch."
    )


if __name__ == "__main__":
    main()
