# Issue 13418 — LaTeX report TypeError in str_incr (styled note: subscript + strikeout)

**Outcome: core fix written (gramps `maintenance/gramps61`) + headless unittest.**
Not pushed — Eduard's review gate.

## Root cause
`gramps/plugins/docgen/latexdoc.py:str_incr` generates the column identifiers
(`aaa`, `aab`, …) used when a LaTeX table contains spanning multicolumns. Its
increment loop is

```python
for i in reversed(lili):      # lili is list("aaa") == ['a','a','a']
    if lili[i] < "z":
```

`reversed(lili)` yields the list's **elements** (`'a'`, `'a'`, …), not its
indices, so `lili[i]` indexes a list with a string and raises
`TypeError: list indices must be integers or slices, not str`.

The first `next()` only `yield`s the base value and returns *before* reaching
the loop, so the failure surfaces on the **second** `next()` — i.e. as soon as a
table needs a second multicolumn id. A Complete Individual Report rendered to
LaTeX with a note that has subscript+strikeout produces exactly such a table
(traceback: `calc_latex_widths → next(self.multcol_alph_counter) → str_incr`,
`latexdoc.py:512` in the report).

## Verdict caveat handled
The verdict's CORRECTION is confirmed: note 1's `familygroup.py` /
`KeyError: 9` traceback is the *separate* bug 13417 (styled-note markup mapping),
not this one. The 13417 work landed on gramps61 as commit `8b935f1551`; I
verified that commit does **not** touch `str_incr`, so 13418 is independent and
still live. The description's `str_incr` traceback is the real one (codefarmer
notes 3-4: reproduces on 5.2.2 with no 13417 changes).

## Fix
One line — iterate indices instead of elements:

```python
-        for i in reversed(lili):
+        for i in reversed(range(len(lili))):
```

Carry semantics are preserved (last column first; on `z` reset to `a` and carry
left). Sequence is now `aaa, aab, … aaz, aba, abb, …`.

## Existing PR — verified, not duplicated
`gramps-project/gramps#2208` (OPEN, by dsblank) is a **major LaTeX rewrite
targeting `master`**. Its rewritten `str_incr` already iterates by index
(`for i in range(len(lili) - 1, -1, -1)`), which corroborates this fix's
direction. It is *not* a substitute here:
- It targets `master`; bug fixes for users go on `maintenance/gramps61` (project
  policy), and 2208 is a large feature-scope rewrite that will not reach gramps61
  users soon.
- It is unmerged. The bug is live on both gramps61 **and** master today.
This minimal one-line fix on gramps61 does not compete with 2208 (different
branch, different scope) and forward-merges cleanly; if/when 2208 lands on
master it supersedes the whole file. Flagged for Eduard's call.

## Verified against
- `maintenance/gramps61` `gramps/plugins/docgen/latexdoc.py:496-517` — the
  `str_incr` generator; the buggy `reversed(lili)` and the carry/`else` branch.
- commit `8b935f1551` (13417 fix on gramps61) — does not touch `str_incr`.
- `dsblank/gramps@258887e` `latexdoc.py:514,530` (PR 2208 head) — independent
  index-based rewrite of the same loop.

## Test
New headless unittest (no Gtk / no display):
`gramps/plugins/docgen/test/latexdoc_test.py::StrIncrTest`
(+ empty `test/__init__.py`, matching the `importer/test`, `export/test`
convention so CI's `*_test.py` discovery picks it up).
- `test_yields_successive_ids_without_typeerror` — pulls 28 values, asserting
  `aaa, aab, … aaz, aba, abb`; the 2nd value alone reproduces the crash pre-fix.
- `test_carry_with_short_base` — `az → ba`, exercising a full carry.

Pre-fix the unfixed generator raises the exact
`TypeError: list indices must be integers or slices, not str` on the 2nd
`next()` (verified inline); post-fix both tests pass. `black --check` clean;
`mypy gramps/plugins/docgen/latexdoc.py` clean.

## Branch / status
- Target: gramps core → `maintenance/gramps61` (per verdict).
- **Draft PR opened:** gramps-project/gramps#2341 (base `maintenance/gramps61`,
  head `eduralph:fix/bug-13418-latex-str-incr`). Left as DRAFT for Eduard's
  ready-mark. Verified on the gramps61 branch: test passes, black + mypy clean.

## Files
- `patch.diff` — fix + test against gramps working tree
- `pr-description.md` — PR body in project format
- `mantis-comment.md` — tracker comment, Eduard's voice (cites `p:gramps:NNNN:`
  — fill in the PR number when the draft is opened)
