#!/usr/bin/env python3
"""
agent-work/dev-tooling/claude-commands/extract_corpus.py

Walks the triage batch results and emits ONE structured JSON record per issue —
mechanical facts only, no judgment. Claude Code (via /corpus-feedback) reads the
JSON and does the pattern-recognition: which fixes share an edit shape, which
shapes are analyzer-reachable, what new rules the recurrence justifies.

Why split this way: the diff format and outcome vocabulary in the corpus are not
fully known, so this script does NOT hardcode signature regexes it can't validate.
It extracts robustly-available facts (status line, repo/branch, Fixes-trailer,
diffstat, per-hunk added/removed lines, new test files) and leaves classification
to the model, which can read the actual hunks.

Usage (from the gramps-testbed repo root):
    python3 agent-work/dev-tooling/claude-commands/extract_corpus.py                 # all batches under agent-work/batches/
    python3 agent-work/dev-tooling/claude-commands/extract_corpus.py agent-work/batches/batch-03-confirmed-velocity
    python3 agent-work/dev-tooling/claude-commands/extract_corpus.py --out agent-work/dev-tooling/findings/corpus.json

Output: agent-work/dev-tooling/findings/corpus.json  (gitignored; regenerable)
"""
import sys, os, json, re, glob, argparse

# ---- robust-but-shallow extractors. Each tolerates absence; never raises on a
# ---- missing field. Returns None / [] when something isn't present.

STATUS_PATTERNS = [
    # ordered: first match wins. Tuned to the SUMMARY.md vocabulary seen so far,
    # plus the obvious siblings. Extend as new status phrasings surface.
    (r"already[- ]fixed", "already-fixed"),
    (r"can'?t[- ]repro|cannot reproduce|not reproducible|unable to reproduce", "cant-repro"),
    (r"\bwont[- ]?fix\b|will not fix", "wontfix"),
    (r"\binvalid\b|invalid input|not a bug", "invalid"),
    (r"\bduplicate\b", "duplicate"),
    (r"addon deleted|delete the addon|deleted;|not ported|removed per", "deletion"),
    (r"\bmerged\b|merged via|merged to", "merged"),
    (r"verification only|verified\b", "verified"),
    (r"\bfixed\b", "fixed"),   # generic 'fixed' last so the specific ones win
]

def read(path):
    try:
        with open(path, encoding="utf-8", errors="replace") as f:
            return f.read()
    except Exception:
        return ""

def parse_status(summary_text):
    """Normalized status from SUMMARY.md. Resolution order:
      1. explicit '## Status' section, matched against STATUS_PATTERNS
      2. structural inference when there's no '## Status' (batch-02 schema: the
         summary records the fix via '## Fix' / '## Test' sections, not a status word)
      3. whole-doc prose scan against STATUS_PATTERNS
      4. 'unknown' (has a summary, but no recognizable status by any means)
    Returns (status, raw_status_line)."""
    if not summary_text:
        return None, None

    def first_line(text):
        return next((l.strip() for l in text.splitlines() if l.strip()), None)

    # 1. explicit '## Status' section
    m = re.search(r"##\s*Status\s*\n(.+?)(?:\n##|\Z)", summary_text, re.S | re.I)
    if m:
        scope = m.group(1)
        low = scope.lower()
        for pat, label in STATUS_PATTERNS:
            if re.search(pat, low):
                return label, first_line(scope)
        # explicit Status section but unrecognized phrasing → fall through to prose scan

    # 2. structural inference (no '## Status' — the batch-02 case). A '## Fix' section is
    #    the schema's way of saying "a fix was written"; '## Root cause' + '## Test' confirm
    #    a worked fix. This is what batch-02 summaries use instead of a status word.
    if not m:
        headers = set(h.strip().lower() for h in re.findall(r"^##\s*(.+?)\s*$", summary_text, re.M))
        if "fix" in headers:
            return "fixed", "inferred from '## Fix' section (no '## Status' — batch-02 schema)"
        # 'already fixed upstream' / verification batches sometimes title that way
        if any("already" in h or "verif" in h for h in headers):
            return "verified", "inferred from section headers (no '## Status')"

    # 3. whole-doc prose scan
    low = summary_text.lower()
    for pat, label in STATUS_PATTERNS:
        if re.search(pat, low):
            return label, first_line(summary_text)

    # 4. genuinely unrecognized
    return "unknown", first_line(summary_text)

def parse_repo_branch(summary_text):
    repo = branch = None
    if summary_text:
        rm = re.search(r"-?\s*Repo:\s*`?([A-Za-z0-9_./-]+)`?", summary_text)
        bm = re.search(r"-?\s*Branch:\s*`?([A-Za-z0-9_./-]+)`?", summary_text)
        if rm: repo = rm.group(1)
        if bm: branch = bm.group(1)
    return repo, branch

def parse_diff(diff_text):
    """Extract structured facts from a git format-patch / unified diff.
    Returns a dict; all keys present even if empty."""
    out = {
        "present": bool(diff_text.strip()),
        "fixes_issue": None,           # from 'Fixes #NNNN' trailer
        "subject": None,               # commit subject
        "files_changed": [],           # [{path, added, removed, new_file}]
        "new_test_files": [],          # paths under tests/ that are new
        "total_added": 0,
        "total_removed": 0,
        "hunk_added_lines": [],        # all '+' code lines (no +++ headers), capped
        "hunk_removed_lines": [],      # all '-' code lines (no --- headers), capped
    }
    if not out["present"]:
        return out

    fm = re.search(r"^Fixes #(\d+)", diff_text, re.M)
    if fm: out["fixes_issue"] = fm.group(1)
    sm = re.search(r"^Subject:\s*(?:\[PATCH[^\]]*\]\s*)?(.+)", diff_text, re.M)
    if sm: out["subject"] = sm.group(1).strip()

    # per-file diff blocks
    for block in re.split(r"(?=^diff --git )", diff_text, flags=re.M):
        if not block.startswith("diff --git"):
            continue
        pm = re.search(r"^diff --git a/(.+?) b/(.+?)\s*$", block, re.M)
        path = pm.group(2) if pm else "?"
        new_file = bool(re.search(r"^new file mode", block, re.M))
        added = len(re.findall(r"^\+(?!\+\+)", block, re.M))
        removed = len(re.findall(r"^-(?!--)", block, re.M))
        out["files_changed"].append(
            {"path": path, "added": added, "removed": removed, "new_file": new_file}
        )
        if new_file and ("/tests/" in path or path.startswith("tests/") or "test_" in os.path.basename(path)):
            out["new_test_files"].append(path)
        out["total_added"] += added
        out["total_removed"] += removed

    # collect actual code lines from hunks (skip file headers), cap to keep JSON sane
    for line in diff_text.splitlines():
        if line.startswith("+++") or line.startswith("---"):
            continue
        if line.startswith("+"):
            out["hunk_added_lines"].append(line[1:])
        elif line.startswith("-"):
            out["hunk_removed_lines"].append(line[1:])
    CAP = 120
    out["hunk_added_lines"] = out["hunk_added_lines"][:CAP]
    out["hunk_removed_lines"] = out["hunk_removed_lines"][:CAP]
    return out

def issue_id_from_dir(dirname):
    base = os.path.basename(dirname.rstrip("/"))
    m = re.match(r"issue[_-](.+)", base)
    return m.group(1) if m else base   # non-issue_ dirs (enhancement_*) keep their full name

def batch_from_dir(issue_dir):
    # .../agent-work/batches/<BATCH>/results/<issue> → grab <BATCH>
    parts = os.path.normpath(issue_dir).split(os.sep)
    try:
        return parts[parts.index("results") - 1]
    except (ValueError, IndexError):
        return None

def extract_issue(issue_dir):
    summary_path = os.path.join(issue_dir, "SUMMARY.md")
    summary = read(summary_path)
    diff = read(os.path.join(issue_dir, "patch.diff"))
    has_summary = os.path.exists(summary_path)
    status, status_line = parse_status(summary)
    diff_facts = parse_diff(diff)
    # Honest handling when there's no SUMMARY: don't emit null. Infer what we can,
    # and flag for the BATCH_INDEX fallback (wired in main()).
    # TODO(batch-index-fallback): ~11 result dirs across batches have no SUMMARY.md.
    #   They're labeled fixed-no-summary (patch present) or no-result (empty) here, which
    #   is honest but coarse. Each batch has a BATCH_INDEX.md that likely records the real
    #   per-issue outcome (cant-repro/wontfix/etc). To upgrade: parse <batch>/BATCH_INDEX.md
    #   once in main(), build {issue_id: status}, and override here when status == no-result.
    #   Deferred: rule-mining keys off PATCHED issues, which nearly all HAVE summaries, so the
    #   no-summary set rarely affects the backlog. Wire only if per-issue precision is needed.
    if not has_summary:
        if diff_facts["present"]:
            status, status_line = "fixed-no-summary", "patch present, no SUMMARY.md"
        else:
            status, status_line = "no-result", "empty result dir (no SUMMARY, no patch)"
    repo, branch = parse_repo_branch(summary)
    # Accept either name: tracker-comment.md (current) or mantis-comment.md
    # (historical bundles from before the rename). Frozen historical bundles
    # are not retroactively renamed.
    has_mantis = (
        os.path.exists(os.path.join(issue_dir, "tracker-comment.md"))
        or os.path.exists(os.path.join(issue_dir, "mantis-comment.md"))
    )
    has_pr = os.path.exists(os.path.join(issue_dir, "pr-description.md"))
    return {
        "issue": issue_id_from_dir(issue_dir),
        "batch": batch_from_dir(issue_dir),
        "dir": issue_dir,
        "has_summary": has_summary,
        "status": status,
        "status_line": status_line,
        "repo": repo,
        "branch": branch,
        "has_patch": diff_facts["present"],
        "has_mantis_comment": has_mantis,
        "has_pr_description": has_pr,
        "diff": diff_facts,
        # reachability is left UNSET — Claude assigns it from the hunks.
        "analyzer_reachable": None,
        "edit_shape": None,
    }

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("roots", nargs="*", default=None,
                    help="batch dirs or a parent; default agent-work/batches/")
    ap.add_argument("--out", default="agent-work/dev-tooling/findings/corpus.json")
    args = ap.parse_args()

    roots = args.roots or ["agent-work/batches"]
    issue_dirs = []
    for root in roots:
        # every per-issue result dir, any depth. Match ALL result subdirs (issue_*, issue-*,
        # and non-issue names like enhancement_*), then exclude the stray top-level
        # results/SUMMARY.md and any non-dir. Keyed on full path so the same issue worked in
        # two batches (e.g. 13736 in batch-02 AND batch-03) yields TWO records, not one.
        for d in glob.glob(os.path.join(root, "**", "results", "*"), recursive=True):
            if os.path.isdir(d):
                issue_dirs.append(d)
    issue_dirs = sorted(set(issue_dirs))   # full-path dedup; cross-batch dupes preserved

    records = [extract_issue(d) for d in issue_dirs]

    # roll-up counts for the human/Claude header
    from collections import Counter
    by_status = Counter(r["status"] for r in records)
    with_patch = sum(1 for r in records if r["has_patch"])
    rollup = {
        "total_issues": len(records),
        "with_patch": with_patch,
        "without_patch": len(records) - with_patch,
        "by_status": dict(by_status),
        "batches_scanned": roots,
    }

    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    with open(args.out, "w") as f:
        json.dump({"rollup": rollup, "issues": records}, f, indent=2)

    # console summary
    print(f"== corpus extract ==")
    print(f"  issues: {rollup['total_issues']}  with-patch: {with_patch}  without: {rollup['without_patch']}")
    print(f"  by status: {dict(by_status)}")
    print(f"  wrote: {args.out}")
    if not records:
        print("  (no issue_* dirs found — check the root path / batch layout)")

if __name__ == "__main__":
    main()
