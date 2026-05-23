#!/usr/bin/env bash
#
# run-batch.sh — one-command batch cycle: scrape Mantis notes, then generate
# the Claude Code handoff briefs. Run from gramps-testbed/triage/.
#
# This automates steps 1–2 of the triage cycle. The judgment steps either side
# stay manual ON PURPOSE:
#   - selecting which IDs go in the batch (a planning decision)
#   - filling each issue's TRIAGE VERDICT (the human/planning-chat judgment)
#   - handing the batch to Claude Code and reviewing its output
#
# Usage:
#   ./run-batch.sh <batch-name> <id1,id2,...>
#
# Example:
#   ./run-batch.sh batch-02-current-addons 14230,14051,13979,13774,13966
#
# Options (env vars):
#   CSV=...        path to the dated Mantis export   (default: newest data/*.csv)
#   CDP=...        Chrome remote-debugging URL        (default: http://127.0.0.1:9222)
#   NOTES_DIR=...  where scraped notes land           (default: notes)
#   SKIP_SCRAPE=1  skip the scrape step (notes already pulled), just regenerate
#
# Prerequisite for scraping (attach mode — rides your own Cloudflare clearance):
#   Start Chrome yourself in another terminal and pass Cloudflare by hand once:
#     google-chrome --remote-debugging-port=9222 --user-data-dir=/tmp/cfprofile \
#       "https://gramps-project.org/bugs/view.php?id=<first-id>"
#   The script reminds you and waits for confirmation before scraping.

set -euo pipefail

# ---- args ----------------------------------------------------------------
if [ $# -lt 2 ]; then
  echo "usage: $0 <batch-name> <id1,id2,...>" >&2
  echo "example: $0 batch-02-current-addons 14230,14051,13979" >&2
  exit 2
fi
BATCH="$1"
IDS="$2"

# ---- config (overridable via env) ---------------------------------------
CDP="${CDP:-http://127.0.0.1:9222}"
NOTES_DIR="${NOTES_DIR:-notes}"
SKIP_SCRAPE="${SKIP_SCRAPE:-}"

# Default CSV = newest file in data/ (so you don't retype the dated name).
if [ -z "${CSV:-}" ]; then
  CSV="$(ls -t data/*.csv 2>/dev/null | head -1 || true)"
fi
if [ -z "${CSV:-}" ] || [ ! -f "$CSV" ]; then
  echo "ERROR: no CSV found. Put a Mantis export in data/ or set CSV=<path>." >&2
  exit 1
fi

# ---- sanity: are we in triage/ with the scripts? ------------------------
if [ ! -f scripts/mantis_notes.py ] || [ ! -f scripts/make_handoff.py ]; then
  echo "ERROR: run this from gramps-testbed/triage/ (scripts/ not found here)." >&2
  exit 1
fi

echo "════════════════════════════════════════════════════════════════"
echo " batch:   $BATCH"
echo " ids:     $IDS"
echo " csv:     $CSV"
echo " notes:   $NOTES_DIR/"
echo "════════════════════════════════════════════════════════════════"

# ---- step 1: scrape notes (attach mode) ---------------------------------
if [ -n "$SKIP_SCRAPE" ]; then
  echo "[1/2] SKIP_SCRAPE set — using existing notes in $NOTES_DIR/"
else
  echo "[1/2] Scrape Mantis notes via attached Chrome."
  echo
  echo "  Before continuing, in ANOTHER terminal start Chrome and pass"
  echo "  Cloudflare by hand once:"
  echo
  first_id="${IDS%%,*}"
  echo "    google-chrome --remote-debugging-port=9222 --user-data-dir=/tmp/cfprofile \\"
  echo "      \"https://gramps-project.org/bugs/view.php?id=${first_id}\""
  echo
  read -r -p "  Chrome is up and past Cloudflare? [y/N] " ok
  case "$ok" in
    y|Y) ;;
    *) echo "  Aborting before scrape. Re-run when Chrome is ready, or set SKIP_SCRAPE=1." >&2
       exit 1 ;;
  esac

  python3 scripts/mantis_notes.py --attach "$CDP" --ids "$IDS" --out "$NOTES_DIR"
  echo "[1/2] done — notes in $NOTES_DIR/"
fi

# ---- step 2: generate handoff briefs ------------------------------------
echo "[2/2] Generate handoff briefs (no-clobber: existing verdicts preserved)."
python3 scripts/make_handoff.py \
  --csv "$CSV" \
  --notes-dir "$NOTES_DIR" \
  --ids "$IDS" \
  --batch "$BATCH"

BATCH_PATH="batches/$BATCH"
echo
echo "════════════════════════════════════════════════════════════════"
echo " Batch ready: $BATCH_PATH/"
echo "════════════════════════════════════════════════════════════════"
echo " NEXT (manual — these are the judgment steps):"
echo "   1. Fill the TRIAGE VERDICT in each $BATCH_PATH/issue_*.md"
echo "      (or paste the briefs to the planning chat to draft verdicts)."
echo "   2. Prune EXTERNAL-REPO / UPSTREAM issues — not fixable in the forks."
echo "   3. Launch Claude Code from the gramps-testbed root and point it at"
echo "      $BATCH_PATH/CLAUDE_CODE_BRIEF.md"
echo "   4. Review its results/issue_<id>/ output before any push/PR/tracker edit."
echo
echo " Check the index + auto-flags:"
echo "   cat $BATCH_PATH/BATCH_INDEX.md"
