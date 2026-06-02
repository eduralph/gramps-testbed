# Item 3 — Single-source the `requires_mod` extractor

**Branch:** `ci-requires-mod-extractor` (off `main`) · **Patch:** `patch.diff`

## Root cause
`addon-unit-tests.yml` and `windows-addon-unit-tests.yml` each inlined the
**identical** heredoc deriving the union of `requires_mod` across
`addons-source/*/*.gpr.py` (regex `requires_mod\s*=\s*(\[[^\]]*\])` +
`ast.literal_eval`). Copy-pasted across two files → drift risk; the same
anti-drift motivation behind the existing `scripts/lib/addon_system_deps.py`.

## Change
- **New `scripts/lib/addon_python_deps.py`** — sibling to
  `addon_system_deps.py`, exposes `requires_mod_union(addons_dir)` + a CLI
  (`addon_python_deps.py <addons-source-dir>` → space-separated sorted union).
- Both workflows' heredocs replaced by
  `python3 gramps-testbed/scripts/lib/addon_python_deps.py addons-source`
  (Windows: `python` after `source .venv/bin/activate`). The downstream
  install-one-at-a-time-tolerant loop is unchanged in both.
- **New `tests/test_addon_python_deps.py`** — stdlib `unittest`, 6 cases.

## STATUS: deviation RATIFIED (v3 decisions brief, 2026-06-01)
Act adjudicated the regex-vs-exec-shim deviation and **accepted it — do NOT
revert.** Basis: all 14 real `requires_mod` declarations in addons-source are
flat literals (`grep -rh requires_mod addons-source/*/*.gpr.py`), so the
exec-shim's sole justification (computed/concatenated declarations) is
empirically moot, while its costs (arbitrary-code surface; a second scanning
paradigm inconsistent with the sibling `addon_system_deps.py`) are real. The
spec's exec-shim requirement was falsified by reality. The 6 unit tests + the
byte-identical-output check remain the regression guard. No code change.

## DELIBERATE DEVIATION FROM THE BRIEF — read this
The brief (v2, Item 3) specified an **exec-shim** (`register`/`GRAMPLET`/… inject,
execute each `.gpr.py`, capture the kwarg). I implemented **regex +
`ast.literal_eval`** instead. Reasons:
1. **No real case needs the shim.** Every `requires_mod` in addons-source is a
   flat string literal (`grep -rh requires_mod addons-source/*/*.gpr.py`: 14
   declarations, all literal). The brief itself (v2) said: if no computed case
   exists, justify on drift alone — it doesn't.
2. **Sibling consistency.** `addon_system_deps.py` *and the old inline heredoc*
   both use regex + `literal_eval`. An exec-shim would be a second, different
   scanning paradigm in the same directory scanning the same files — itself a
   form of drift.
3. **No arbitrary-code-exec surface.** The shim would `exec()` each `.gpr.py`;
   the regex reads source without running it (stays "pure stdlib, pre-Gramps",
   like the sibling).
The deviation is trivially reversible if you prefer the brief's letter — say so
and I'll swap the extractor body for the shim (the test would change shape).

## Verified against
- `scripts/lib/addon_system_deps.py:108-110,123-145` — the regex + `_literal`
  (`ast.literal_eval`) pattern this mirrors.
- `addon-unit-tests.yml:134-149` / `windows-addon-unit-tests.yml:153-168`
  (pre-edit) — the byte-identical heredocs being replaced.
- `addons-source/*/*.gpr.py` — all 14 `requires_mod` declarations are literals.

## Verification (real pass/fail evidence)
- `python3 -m unittest tests.test_addon_python_deps` → **6 tests OK**. Cases:
  literal lists unioned+sorted; duplicates collapse; a `.gpr.py` that raises at
  module top level is still parsed (regex doesn't exec — a robustness win over
  the shim); a non-literal `requires_mod=[NAME]` skipped without aborting; no
  `.gpr.py` → empty; `.gpr.py` without `requires_mod` ignored.
- **Equivalence:** `addon_python_deps.py ../addons-source` and the old inline
  heredoc both print exactly
  `PIL boto3 dbf life_line_chart litellm networkx psycopg psycopg2 pygraphviz
  pymongo svgwrite`.
- `actionlint` (with shellcheck 0.10.0) on both workflows → the 3 shellcheck
  warnings (SC2046/SC2206/SC2295) are **pre-existing in unrelated blocks**;
  diffed warning sets between `main` and this branch are identical, so the edit
  added none.
- `ast.parse` OK on both new files. (black/ruff not installed in this env — the
  files follow the sibling's formatting; flag for the pre-commit run.)

## What this proves / leaves unproven
- **Proves:** the extractor returns the same module set as the old heredoc on
  real data; tolerant paths behave; YAML still valid; no new lint.
- **Leaves unproven:** the end-to-end CI step (pip-installing the derived
  modules on a real runner) — that needs a `workflow_dispatch` run (Eduard).
  black/ruff were not run locally (absent); the pre-commit hooks will.
