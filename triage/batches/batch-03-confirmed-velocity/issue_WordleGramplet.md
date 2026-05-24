# WordleGramplet — ImportError: cannot import name 'imap' from 'itertools' (Python 2 leftover)

| field | value |
|---|---|
| Source | detector (c)-bucket, NOT a Mantis confirmed scrape |
| Addon | WordleGramplet — verify in-tree addons-source |
| Failure | `ImportError: cannot import name 'imap' from 'itertools'` |

## What the detector found
WordleGramplet fails isolated load importing `imap` from `itertools`. `itertools.imap`
was removed in Python 3 (it existed only in Py2; in Py3 the builtin `map` is lazy and
replaces it). This is unported Python-2 code — the addon has never worked on Py3.

## ===== TRIAGE VERDICT =====
- **Actionable?** yes — near-certain fast fix, classic Py2→Py3 port.
- **Where:** addons-source (in-tree). Confirm dir, branch maintenance/gramps61.
- **Root cause:** `from itertools import imap` (and likely usages of `imap(...)`).
  In Py3, `imap` → builtin `map` (already lazy). Remove the import; replace `imap(` calls
  with `map(`.
- **Fix sketch:** drop the `imap` import; replace `imap(` → `map(` at call sites. CHECK for
  other Py2 leftovers in the same file while there (`izip`, `ifilter`, `xrange`, `print`
  statements, `dict.iteritems`) — a module with `imap` often has siblings. But fix only
  what blocks loading + obvious Py2 idioms; do NOT rewrite logic. One logical fix:
  "port WordleGramplet to Python 3 imports."
- **Repro:** import the module — fails pre-fix, succeeds post-fix.
- **Test:** detector is the regression guard. Optional import test in `WordleGramplet/tests/`.
- **Check upstream isn't ahead:** grep history/open PRs for WordleGramplet; overlaps the
  PR #820 lint/compile spin-off series — check there first.
