# Increment 1 (detector items) — handoff addendum

> Append to / read alongside CLAUDE_CODE_BRIEF.md. This OVERRIDES the
> "three clean fixes" framing. Triage on 2026-05-25 changed the picture:
> the three items are NOT three identical fixes. Treat each per its finding
> below. All three target **maintenance/gramps60** in **addons-source**
> (addons-source → gramps60; gramps core → gramps61).

## Standing rules (apply to all three)
- **Repro-or-close first.** Confirm the defect still exists on the current
  gramps60 tree BEFORE writing any fix. An already-fixed item closes as
  confirm-and-done — that is a success, not a failure.
- **Check upstream isn't ahead.** All three overlap the PR #820 lint/compile
  spin-off series. Before committing any fix, check open PRs + branch history
  for that addon name. If already fixed in a spin-off PR, close as duplicate.
- **Fix only what blocks loading.** These are import-hygiene / syntax fixes.
  Do NOT refactor logic. One logical change per addon.
- **One issue per ticket.** Keep the three as separate commits/PRs even though
  they share a fix shape.

## Item 1 — WordleGramplet — LIKELY ALREADY FIXED (confirm-and-close)
Detector verdict was: `ImportError: cannot import name 'imap' from 'itertools'`.
**But triage found no `imap` in the addon source — only in the test file**
`WordleGramplet/tests/test_wordlegramplet_imports.py`, which references
"this PR's earlier revision" and the exact ImportError. That test reads like a
regression guard written FOR this fix, implying the port already happened.

Tasks:
1. `grep -rn 'imap' WordleGramplet/*.py` — expected EMPTY if already ported.
2. `git log --oneline maintenance/gramps60 -- WordleGramplet/` and
   `git log --all --oneline -- WordleGramplet/tests/test_wordlegramplet_imports.py`
   — find where the port + test landed. May be an OPEN PR (#820 spin-off) not
   yet merged to gramps60, not in the merged history.
3. If source is clean and the import test passes → **confirm-and-close**, link
   the PR/commit that already fixed it. Do NOT write a duplicate fix.
4. Only if source still has `imap` → port: drop the import, `imap(`→`map(`.

## Item 2 — QueryQuickview — DIRECTORY NOT FOUND (resolve name first)
Detector verdict was: `SyntaxError: '(' was never closed`.
**But `grep` reported `QueryQuickview: No such file or directory`** — no addon
dir by that name in the gramps60 addons-source tree.

Tasks:
1. Find the real name / location:
   `ls -d */ | grep -i query` ; `find . -iname '*query*' -maxdepth 2`.
2. If it exists under another name/case → run `python3 -m py_compile` on the
   module to get the exact unclosed-paren line, balance it, confirm import.
   Keep the fix to the syntax error ONLY.
3. If it genuinely does not exist on gramps60 → the detector flagged something
   not in this tree. Record that and close as not-applicable / wrong-tree;
   do NOT fabricate a fix.

## Item 3 — RebuildTypes — VERIFY THE BARE IMPORT (grep was inconclusive)
Detector verdict was: `ModuleNotFoundError: No module named 'gui'` — a bare
`import gui` that should be `gramps.gui`. The combined sibling-sweep grep did
NOT hit RebuildTypes (its `import (gen|gui|cli)$` pattern misses `from gui
import X` and trailing-whitespace cases), so the bare import is unconfirmed,
not absent.

Tasks:
1. `grep -rn 'gui' RebuildTypes/*.py` — locate the actual bare `gui` reference
   (`import gui` or `from gui import ...`).
2. Qualify to `gramps.gui` (`from gramps import gui` or
   `from gramps.gui... import ...` matching usage). Fix import path(s) only.
3. Repro note: the module pulls Gtk via gramps.gui, so the import test needs a
   display — gate on display like the batch-02 PluginManager test, or run under
   xvfb. Don't let a missing-display failure read as the bug.

## Generator bug (separate, do not block this increment)
The CSV-scaffold generator (make_handoff.py or equivalent) hardcoded a
`gramps61` branch default; it contaminated every CSV item this batch
(12544, 13955, 14143, 13059, 13420, 11054) and was fixed by hand with sed.
**Fix the generator to derive branch from repo target** (addons-source →
gramps60, gramps → gramps61) before batch-04, or it recurs. Out of scope for
increment 1 — noted here so it isn't lost.
