# `preflight_prs.py` — script spec

> Suggestion 3 from the streamlining plan. Mandates the closed-PR pre-flight
> step from doc 04 as a cheap CLI invocation instead of manual GitHub UI
> clicks per item.

## Purpose
Given a repo + (path or keyword), report:
- Merged commits touching the path in the last N days (default 365).
- Open PRs touching the path.
- Closed/rejected (not merged) PRs touching the path.

So Claude Code can satisfy the playbook step "Pre-flight: check upstream isn't
ahead — merged AND closed PRs" in one tool call instead of three browser tabs.

## CLI
```
preflight_prs.py --repo <owner/name> [--path <path>] [--keyword <text>]
                 [--branch <branch>] [--days N] [--json] [--limit N]
```

Required: `--repo`, plus at least one of `--path` or `--keyword`.

| Flag | Default | Meaning |
|---|---|---|
| `--repo` | (required) | e.g. `gramps-project/addons-source` |
| `--path` | none | Repo-relative path; can be a directory (`GraphView/`) or a file |
| `--keyword` | none | Free text; matched against PR titles/bodies and commit messages |
| `--branch` | `maintenance/gramps60` for addons-source, `maintenance/gramps61` for gramps, else default branch | Base branch for the merged history check |
| `--days` | 365 | Lookback window for merged commits |
| `--json` | off | Emit JSON instead of human-readable text |
| `--limit` | 20 | Cap on results per section |

## Auth
`GITHUB_TOKEN` env var. Required for non-trivial usage (rate-limit otherwise
hits in two or three invocations). PAT scope: `public_repo` for public repos
only is sufficient.

## Output (human-readable, default)
```
=== preflight_prs.py results ===
Repo:     gramps-project/addons-source
Branch:   maintenance/gramps60
Path:     GraphView/
Keyword:  (none)
Window:   last 365 days
Generated: 2026-05-29T13:45:00Z

--- Merged history (last 365 days, base=maintenance/gramps60) ---
[3 commits]
- a1b2c3d 2026-04-18  GraphView: fix layout regression in compact mode (PR #874)
- e4f5g6h 2026-02-02  GraphView: handle UUID handles from Gramps-Web (PR #831)
- ...

--- Open PRs ---
[1 PR]
- #913 (open, head: dsblank/graphview-prereq-fix)
       "GraphView: skip prereq check during teardown"
       opened 2026-05-10, last activity 2026-05-26
       targets: maintenance/gramps60

--- Closed/rejected PRs (not merged) ---
[2 PRs]
- #877 (closed) "RebuildTypes: addon removal per author request"
       closed 2025-12-04, reason: author requested deletion
       targets: maintenance/gramps60
- #802 (closed) "GraphView: incompatible animation rewrite"
       closed 2025-09-15, reason: maintainer declined approach
       targets: maintenance/gramps60

--- Summary ---
Merged: 3   Open: 1   Closed/rejected: 2

Suggested action: an open PR (#913) addresses related code. VERIFY before
writing a fix; do not duplicate.
```

The "Suggested action" line is heuristic, not authoritative — emit when there
is an open PR matching, or when closed PR count > 0 (the "maintainer
declined" signal).

## Output (`--json`)
```json
{
  "repo": "gramps-project/addons-source",
  "branch": "maintenance/gramps60",
  "path": "GraphView/",
  "keyword": null,
  "window_days": 365,
  "generated_at": "2026-05-29T13:45:00Z",
  "merged": [{"sha": "...", "date": "...", "subject": "...", "pr": 874}, ...],
  "open_prs": [{"number": 913, "title": "...", "head": "...", "base": "...", "opened": "...", "updated": "..."}, ...],
  "closed_prs": [{"number": 877, "title": "...", "closed": "...", "merged": false, "base": "..."}, ...]
}
```

Stable schema (additive changes only).

## Implementation notes
- Stdlib only: `urllib.request`, `json`, `argparse`, `os`, `datetime`,
  `dataclasses`. No `requests`, no `PyGithub`.
- GitHub REST endpoints used:
  - `/repos/{owner}/{repo}/commits?path={path}&sha={branch}&since={iso}` for merged history
  - `/repos/{owner}/{repo}/pulls?state=open&base={branch}` then filter by path
  - `/repos/{owner}/{repo}/pulls?state=closed&base={branch}` then filter by path (closed includes merged; subtract merged set)
- Path-filter on PRs uses `/repos/{owner}/{repo}/pulls/{n}/files`; cache the
  file lists per PR-number to avoid repeated calls within one invocation.
- Pagination: follow `Link: ...; rel="next"` headers. Cap at `--limit`.
- Rate limiting: respect `X-RateLimit-Remaining`; if it drops below 10, sleep
  until `X-RateLimit-Reset` if the user passed `--wait`, otherwise abort
  cleanly with a message.
- Keyword search uses `/search/issues?q=...+repo:owner/name+type:pr` for the
  PR side, and `/search/commits?q=...` for the commit side (note: commits
  search requires the `Accept: application/vnd.github.cloak-preview` header,
  or use `/repos/.../commits` with title grep instead — pick one and document).

## Use sites
- **Verdict pass (planning chat):** `preflight_prs.py --repo gramps-project/addons-source --path GraphView/`. Runs at verdict-fill time; influences the VERDICT frontmatter (`existing_pr`).
- **Per-item in Claude Code:** `preflight_prs.py --repo {target_repo} --path {file_paths_suspected[0]}`. Output captured into SUMMARY.md `Pre-flight` section.

## Acceptance
- Returns within 10 seconds for typical queries (3-5 API calls, 1-2 page each).
- Exit code 0 on clean run; non-zero on auth failure / repo not found / rate-limit-hit-without-wait.
- JSON output passes `python -m json.tool` without error.
- Tested against gramps-project/addons-source and gramps-project/gramps for
  paths that have known merged commits, an open PR, and a closed PR (use the
  RebuildTypes case for the closed-PR axis).
