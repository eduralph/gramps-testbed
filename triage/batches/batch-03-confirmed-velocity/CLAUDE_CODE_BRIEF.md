# Claude Code working brief — Mantis bug batch: batch-03-confirmed-velocity

You are running from the **gramps-testbed** repo. Three sibling repos are reachable
via additionalDirectories: `../gramps`, `../addons-source`, `../addons`.

## Authoritative conventions — read these, do not re-derive
- **`../gramps-testbed/CLAUDE.md`** — the Upstream fix workflow section is binding:
  branch targeting (maintenance/gramps60, not master, for fixes), "edit source never the
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
6. **Check upstream isn't already ahead** before declaring a bug unfixed.

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
6. STOP. Eduard reviews, then decides on commit/push/PR.

## Reminders from project conventions
- Run Gramps from an EXTERNAL terminal, not the VS Code integrated one (GLIBC/Snap).
- Gramps does not follow symlinks for plugin discovery; the auto-sync task copies
  source -> installed plugin one way. Edit source only.
- All tests are stdlib `unittest.TestCase` — pytest is never introduced.

See `BATCH_INDEX.md` for the issue list and triage status.
