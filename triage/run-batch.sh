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
#   CSV=...         path to the dated Mantis export  (default: newest data/*.csv)
#   CDP=...         Chrome remote-debugging URL       (default: http://127.0.0.1:9222)
#   NOTES_DIR=...   where scraped notes land          (default: notes)
#   SKIP_SCRAPE=1   skip the scrape step (notes already pulled), just regenerate
#   CHROME_BIN=...  Chrome binary                     (default: autodetect)
#   CHROME_PROFILE= persistent profile dir            (default: ~/.cache/gramps-triage-chrome)
#   PORT=...        debug port                         (default: 9222)
#
# Scraping uses attach mode (rides your own Cloudflare clearance — does NOT bypass it).
# By default this script now LAUNCHES Chrome for you against a persistent profile, waits
# for the debug port, opens the first issue, and PAUSES for you to clear Cloudflare (if a
# challenge appears) and confirm. The persistent profile means later runs usually have no
# challenge at all, because the trust/cookies carry over.
#
#   --attach-only   do NOT launch Chrome; attach to one you started yourself (old behavior)
#
# Chrome is LEFT RUNNING after the scrape so the cleared session is reusable next run.
# It launches your REAL Chrome (not Playwright's bundled browser) so Cloudflare trusts it.

set -euo pipefail

# ---- args ----------------------------------------------------------------
ATTACH_ONLY=""
POSARGS=()
for a in "$@"; do
  case "$a" in
    --attach-only) ATTACH_ONLY=1 ;;
    *) POSARGS+=("$a") ;;
  esac
done
set -- "${POSARGS[@]}"

if [ $# -lt 2 ]; then
  echo "usage: $0 [--attach-only] <batch-name> <id1,id2,...>" >&2
  echo "example: $0 batch-02-current-addons 14230,14051,13979" >&2
  exit 2
fi
BATCH="$1"
IDS="$2"

# ---- config (overridable via env) ---------------------------------------
PORT="${PORT:-9222}"
CDP="${CDP:-http://127.0.0.1:${PORT}}"
NOTES_DIR="${NOTES_DIR:-notes}"
SKIP_SCRAPE="${SKIP_SCRAPE:-}"
CHROME_PROFILE="${CHROME_PROFILE:-$HOME/.cache/gramps-triage-chrome}"

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

# ---- step 1: scrape notes (attach mode, auto-launching Chrome) ----------
if [ -n "$SKIP_SCRAPE" ]; then
  echo "[1/2] SKIP_SCRAPE set — using existing notes in $NOTES_DIR/"
else
  first_id="${IDS%%,*}"
  first_url="https://gramps-project.org/bugs/view.php?id=${first_id}"

  # Is a debug-enabled Chrome already listening?
  port_up () { curl -fsS "http://127.0.0.1:${PORT}/json/version" >/dev/null 2>&1; }

  if port_up; then
    echo "[1/2] Chrome already listening on :${PORT} — attaching to it."
  elif [ -n "$ATTACH_ONLY" ]; then
    echo "ERROR: --attach-only set but nothing is listening on :${PORT}." >&2
    echo "  Start Chrome yourself with --remote-debugging-port=${PORT}, then re-run." >&2
    exit 1
  else
    # Autodetect a real Chrome/Chromium binary (NOT Playwright's bundled one).
    CHROME_BIN="${CHROME_BIN:-}"
    if [ -z "$CHROME_BIN" ]; then
      for c in google-chrome google-chrome-stable chromium chromium-browser \
               "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"; do
        if command -v "$c" >/dev/null 2>&1 || [ -x "$c" ]; then CHROME_BIN="$c"; break; fi
      done
    fi
    if [ -z "$CHROME_BIN" ]; then
      echo "ERROR: no Chrome/Chromium found. Set CHROME_BIN=/path/to/chrome, or" >&2
      echo "  start Chrome yourself and re-run with --attach-only." >&2
      exit 1
    fi

    echo "[1/2] Launching Chrome ($CHROME_BIN) on :${PORT}"
    echo "      profile: $CHROME_PROFILE (persistent — Cloudflare trust carries over)"
    mkdir -p "$CHROME_PROFILE"
    "$CHROME_BIN" \
      --remote-debugging-port="${PORT}" \
      --user-data-dir="$CHROME_PROFILE" \
      "$first_url" >/dev/null 2>&1 &
    CHROME_PID=$!

    # Poll until the debug port answers (Chrome needs a moment to open it).
    echo -n "      waiting for debug port"
    for _ in $(seq 1 30); do
      if port_up; then break; fi
      # If Chrome died immediately (e.g. already running on this profile), say so.
      if ! kill -0 "$CHROME_PID" 2>/dev/null; then
        echo
        echo "ERROR: Chrome exited before the debug port came up." >&2
        echo "  Most likely this profile is already open in another Chrome window." >&2
        echo "  Close it, or set CHROME_PROFILE=<a different dir>, or use --attach-only." >&2
        exit 1
      fi
      echo -n "."; sleep 1
    done
    echo
    if ! port_up; then
      echo "ERROR: debug port :${PORT} never came up after 30s." >&2
      exit 1
    fi
  fi

  # Human-in-the-loop: clear Cloudflare if challenged. This is the load-bearing
  # step — it cannot be automated and is why this is attach-mode, not launch-mode.
  echo
  echo "  Chrome should now be open at:"
  echo "    $first_url"
  echo "  If a Cloudflare challenge appears, solve it by hand now."
  echo "  (With the persistent profile, later runs usually show no challenge.)"
  echo
  read -r -p "  Past Cloudflare and ready to scrape? [y/N] " ok
  case "$ok" in
    y|Y) ;;
    *) echo "  Aborting before scrape. Chrome left running; re-run when ready." >&2
       echo "  (Or set SKIP_SCRAPE=1 if notes are already pulled.)" >&2
       exit 1 ;;
  esac

  python3 scripts/mantis_notes.py --attach "$CDP" --ids "$IDS" --out "$NOTES_DIR"
  echo "[1/2] done — notes in $NOTES_DIR/  (Chrome left running for reuse)"
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