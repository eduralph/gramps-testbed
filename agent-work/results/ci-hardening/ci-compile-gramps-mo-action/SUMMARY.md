# Item 7 — DRY the duplicated step bodies (compile-gramps-mo)

**Branch:** `ci-compile-gramps-mo-action` (off `main`) · **Patch:** `patch.diff`

This is the first (cleanest) of the brief's three proposed extractions. Two of
the three are **not** implemented here — see "Deferred" below. One PR per
action, as the brief requires.

## Root cause
The msgfmt `po/*.po → build/mo/<lang>/LC_MESSAGES/gramps.mo` loop is copy-pasted
across **5** workflows.

## Change
- New `.github/actions/compile-gramps-mo/action.yml` — composite action,
  `shell: bash`, `working-directory` from a `gramps-path` input (default
  `gramps`). Loop body byte-identical to the originals.
- Migrated the **3 Ubuntu callers** — `unit-tests.yml`, `interface-tests.yml`,
  `addon-unit-tests.yml` — to
  `uses: ./gramps-testbed/.github/actions/compile-gramps-mo`.

## Discovery that narrowed the scope — the callers span TWO shells
The brief's premise was "identical body everywhere → cleanest extraction."
The body is identical, but the **execution context is not**: 3 callers run
under `bash` (Ubuntu), 2 under `shell: msys2 {0}` (Windows). A composite
action step's `shell:` is a literal and does **not** inherit the caller job's
`defaults.run.shell`, and `msgfmt` on Windows comes from the UCRT64 pacman
gettext, which is **not** on Git Bash's PATH. So:
- one action cannot serve both families without a behavior change;
- the Windows callers (`windows-unit-tests.yml`,
  `windows-addon-unit-tests.yml`) keep the loop **inline** and unchanged.

Net: 5 inline copies → 1 action + 2 (Windows) inline. A real but partial DRY
win, with zero behavior change to any migrated caller.

## Verified against
- `unit-tests.yml:119-126`, `interface-tests.yml:141-148`,
  `addon-unit-tests.yml:168-174` (pre-edit) — all three: `working-directory:
  gramps`, identical loop. Testbed checked out at `path: gramps-testbed`,
  gramps at `path: gramps` in all three (so the `uses:` path and `gramps-path`
  default are uniform).
- Effective-body diff: the action's `run:` block is byte-identical (modulo
  leading indentation, which bash ignores) to each original loop.
- Windows callers: `grep -c msgfmt` still 1 each, untouched.

## Verification
- `actionlint` on the 3 migrated workflows → no new findings. SC-warning sets
  on `main` vs this branch are identical (same 5 warnings, line numbers shifted
  by the 5 removed lines); the edit introduced none.
- **actionlint does not lint composite `action.yml` files** (it validates
  workflows; passing the action file makes it complain about a missing `on`/
  `jobs` — expected, not a real error). And it neither validates nor rejects
  the `./gramps-testbed/.github/actions/...` local-action path (tested both a
  correct and a wrong path — exit 0 for both).

## What this leaves UNPROVEN — important
- The **runtime local-action reference**. At runtime the testbed lives at
  `gramps-testbed/`, so the action is referenced as
  `./gramps-testbed/.github/actions/compile-gramps-mo`. actionlint can't
  confirm this resolves (see above), and the action sits at `.github/actions/`
  in the repo's static layout. **A `workflow_dispatch` smoke run on each of the
  3 migrated workflows is the only real confirmation that the `uses:` path
  resolves and the catalogs still compile** — Eduard's step. This is exactly
  the "dispatch run is the real confirmation" the brief anticipated; treat the
  local checks as wiring-only.

## Deferred (NOT implemented) — flagged for decision
- **`setup-gramps-venv`** — same Ubuntu/Windows shell split, *plus* the bodies
  genuinely differ: Ubuntu `python3 -m venv …; echo "$GITHUB_WORKSPACE/.venv/
  bin" >> $GITHUB_PATH` vs Windows `/ucrt64/bin/python -m venv …; echo
  "$(cygpath -u "$GITHUB_WORKSPACE")/.venv/bin" >> $GITHUB_PATH` (different
  interpreter, cygpath translation, msys2 shell). Parameterizing the
  interpreter path alone does **not** make these one shape — it's a
  behavior-change risk, so it is **DECISION-REQUIRED**, not done.
- **repo-resolution block** — the brief already flagged this DECISION-REQUIRED
  (matrix callers vs input→repo-variable→default callers differ). Unchanged.

Recommendation: validate this compile-gramps-mo PR with a dispatch run first;
if the `./gramps-testbed/...` local-action path resolves cleanly, the pattern
is proven and `setup-gramps-venv` can be attempted as a **two-action** split
(one bash, one msys2) rather than one parameterized action. Until a dispatch
run confirms the path, hold the other two.
