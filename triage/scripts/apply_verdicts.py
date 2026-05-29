#!/usr/bin/env python3
"""
apply_verdicts.py — merge one batch verdicts file into the per-issue issue_<id>.md
scaffolds, replacing the empty "TRIAGE VERDICT" section with the filled verdict.

Deterministic text surgery — no LLM. Everything ABOVE the verdict marker in each
issue_<id>.md (tracker report + scraped notes that make_handoff.py wrote) is left
byte-for-byte untouched; only the verdict section below the marker is replaced.

VERDICTS FILE FORMAT
--------------------
One file, blocks delimited by a line starting with '## VERDICT <id>' (anything
after the id on that line is ignored — e.g. a title). The block runs until the
next '## VERDICT' line or EOF. Example:

    ## VERDICT 13819  Family Edit reorders parents
    - **Actionable?** yes
    - **Where does the fix go?** gramps core
    ... rest of the filled verdict ...

    ## VERDICT 13747
    - **Actionable?** yes
    ...

The marker matched in each issue_<id>.md is the scaffold's verdict header line
(default: a line containing 'TRIAGE VERDICT'); everything from that line to EOF
is replaced by a fresh header + the block body.

USAGE (from gramps-testbed/triage/):
    python3 scripts/apply_verdicts.py \
        --verdicts batches/batch-04-recent-confirmed/VERDICTS.md \
        --batch-dir batches/batch-04-recent-confirmed

    # preview without writing:
    python3 scripts/apply_verdicts.py --verdicts ... --batch-dir ... --dry-run

    # overwrite verdicts already filled (default SKIPS issues whose verdict
    # section already has content, to protect hand-edits):
    python3 scripts/apply_verdicts.py --verdicts ... --batch-dir ... --clobber
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

VERDICT_HEADER = "## ===== TRIAGE VERDICT (filled) ====="
# The scaffold's empty marker contains this substring; we split on the line
# that has it. (make_handoff.py writes "## ===== TRIAGE VERDICT (fill before
# handoff) =====".)
MARKER_SUBSTR = "TRIAGE VERDICT"

# A verdict section is considered "already filled" (and thus skipped without
# --clobber) if its Actionable field has a real decision rather than the empty
# scaffold's "yes / no / deferred —" placeholder. We detect the PLACEHOLDER and
# treat its presence as "empty"; anything else on that field means hand-filled.
PLACEHOLDER_ACTIONABLE = re.compile(
    r"\*\*\s*Actionable\?\s*\*\*\s*yes\s*/\s*no\s*/\s*deferred", re.I
)


def verdict_already_filled(section: str) -> bool:
    # If the section still contains the unedited placeholder, it's NOT filled.
    if PLACEHOLDER_ACTIONABLE.search(section):
        return False
    # Otherwise, if there's an Actionable field at all with some content, it's filled.
    return bool(re.search(r"\*\*\s*Actionable\?\s*\*\*\s*\S", section))


def parse_verdicts(text: str) -> dict[str, str]:
    """Split the verdicts file into {id: block_body}. Block starts at a line
    beginning with '## VERDICT <id>' and runs to the next such line / EOF."""
    blocks: dict[str, str] = {}
    cur_id = None
    cur_lines: list[str] = []
    header_re = re.compile(r"^##\s+VERDICT\s+0*(\d+)\b", re.I)
    for line in text.splitlines():
        m = header_re.match(line)
        if m:
            if cur_id is not None:
                blocks[cur_id] = "\n".join(cur_lines).strip("\n")
            cur_id = m.group(1)
            cur_lines = []
        elif cur_id is not None:
            cur_lines.append(line)
    if cur_id is not None:
        blocks[cur_id] = "\n".join(cur_lines).strip("\n")
    return blocks


def split_scaffold(md: str) -> tuple[str, str | None]:
    """Return (head, verdict_section). head is everything up to and excluding the
    marker line; verdict_section is the marker line + below (or None if absent)."""
    lines = md.splitlines(keepends=True)
    for i, line in enumerate(lines):
        if MARKER_SUBSTR in line and line.lstrip().startswith("#"):
            return "".join(lines[:i]), "".join(lines[i:])
    return md, None


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--verdicts", required=True, help="path to the single VERDICTS.md")
    ap.add_argument(
        "--batch-dir", required=True, help="batch folder with issue_<id>.md files"
    )
    ap.add_argument(
        "--dry-run", action="store_true", help="report actions, write nothing"
    )
    ap.add_argument(
        "--clobber",
        action="store_true",
        help="overwrite verdict sections that already look filled "
        "(default: skip them to protect hand-edits)",
    )
    args = ap.parse_args()

    vfile = Path(args.verdicts)
    bdir = Path(args.batch_dir)
    if not vfile.is_file():
        print(f"ERROR: verdicts file not found: {vfile}", file=sys.stderr)
        return 1
    if not bdir.is_dir():
        print(f"ERROR: batch dir not found: {bdir}", file=sys.stderr)
        return 1

    blocks = parse_verdicts(vfile.read_text(encoding="utf-8"))
    if not blocks:
        print(
            "ERROR: no '## VERDICT <id>' blocks found in the verdicts file.",
            file=sys.stderr,
        )
        return 1
    print(f"Parsed {len(blocks)} verdict block(s): {', '.join(sorted(blocks))}")

    applied, skipped, missing, no_marker = [], [], [], []
    for iid, body in blocks.items():
        target = bdir / f"issue_{iid}.md"
        if not target.exists():
            missing.append(iid)
            print(f"  #{iid}: NO issue_{iid}.md in batch dir — skipping")
            continue
        md = target.read_text(encoding="utf-8")
        head, section = split_scaffold(md)
        if section is None:
            no_marker.append(iid)
            print(f"  #{iid}: no TRIAGE VERDICT marker found — skipping (manual check)")
            continue
        if verdict_already_filled(section) and not args.clobber:
            skipped.append(iid)
            print(
                f"  #{iid}: verdict already filled — SKIPPING (use --clobber to overwrite)"
            )
            continue
        new_md = (
            head.rstrip("\n") + "\n\n" + VERDICT_HEADER + "\n\n" + body.strip() + "\n"
        )
        if args.dry_run:
            print(f"  #{iid}: would write ({len(body)} chars of verdict)")
        else:
            target.write_text(new_md, encoding="utf-8")
            print(f"  #{iid}: verdict applied")
        applied.append(iid)

    print(
        f"\nSummary: {len(applied)} applied, {len(skipped)} skipped (already filled), "
        f"{len(missing)} missing file, {len(no_marker)} no-marker."
    )
    # IDs present in the batch dir but with NO verdict block — flag them.
    present = {p.name[6:-3] for p in bdir.glob("issue_*.md")}
    have_block = set(blocks)
    unverdicted = sorted(present - have_block)
    if unverdicted:
        print(
            f"WARNING: {len(unverdicted)} issue file(s) have NO verdict block in "
            f"the verdicts file: {', '.join(unverdicted)}"
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
