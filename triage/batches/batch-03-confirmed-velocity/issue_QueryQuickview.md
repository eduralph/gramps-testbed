# QueryQuickview — SyntaxError: '(' was never closed (addon fails to load)

| field | value |
|---|---|
| Source | detector (c)-bucket, NOT a Mantis confirmed scrape |
| Addon | QueryQuickview — verify in-tree addons-source |
| Failure | `SyntaxError: '(' was never closed` at module import |

## What the detector found
QueryQuickview fails isolated load with `SyntaxError: '(' was never closed`. A syntax
error means the module cannot be imported at all — the addon is dead on the current tree
under Gramps' own loader too, not just the detector. No environmental ambiguity: a
SyntaxError is unconditional.

## ===== TRIAGE VERDICT =====
- **Actionable?** yes — near-certain fast fix.
- **Where:** addons-source (in-tree). Confirm the addon dir, branch maintenance/gramps61.
- **Root cause:** an unclosed `(` — a literal Python syntax error in the source. Find the
  unbalanced parenthesis (the traceback line number from a `python3 -m py_compile` on the
  file points at it) and close it.
- **Reporter workaround vs root cause:** n/a — detector-sourced, no reporter.
- **Fix sketch:** `python3 -m py_compile QueryQuickview/<module>.py` to get the exact line,
  fix the paren balance. Verify the whole addon then imports. Keep the fix to the syntax
  error ONLY — do not refactor surrounding code (a SyntaxError often masks whether the
  rest of the module is sound; fix the syntax, confirm import, stop).
- **Repro:** `py_compile` the module — fails pre-fix, passes post-fix. The detector's
  isolated-load is the integration check.
- **Test:** the detector itself is the regression guard (addon now loads). Optionally a
  trivial import test in `QueryQuickview/tests/`. Given it's a syntax fix, the import
  succeeding IS the verification.
- **Check upstream isn't ahead:** a SyntaxError this blatant may already have a fix in
  flight — grep addons-source history / open PRs for QueryQuickview before committing.
  Note: this overlaps the lint/compile fixes split out of PR #820 — check that series.
