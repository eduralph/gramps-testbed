## Root cause
`str_incr` in `latexdoc.py` generates the column identifiers used for LaTeX
table multicolumns. Its increment loop, `for i in reversed(lili)`, iterates the
character list's *elements* rather than its indices, so `lili[i]` indexes the
list with a string and raises `TypeError: list indices must be integers or
slices, not str`. The first `next()` returns at the `yield` before the loop, so
the crash appears on the second value — reached whenever a table has two or more
multicolumns, such as a styled note containing subscript/strikeout (bug 13418).

## Fix
Iterate the indices instead of the elements:

```python
-        for i in reversed(lili):
+        for i in reversed(range(len(lili))):
```

The carry behaviour is unchanged: `aaa, aab, … aaz, aba, …`.

## Verified against
- `gramps/plugins/docgen/latexdoc.py:496-517` — the `str_incr` generator and its
  carry/`else` branch.
- This is independent of bug 13417 (styled-note markup): that fix is commit
  8b935f1551 and does not touch `str_incr`.

## Test
`gramps/plugins/docgen/test/latexdoc_test.py` adds a headless `StrIncrTest`
asserting `str_incr` yields successive ids (including a carry) without raising.
The second yielded value reproduces the `TypeError` on the unfixed code; both
tests pass after the change.

Fixes #13418.
