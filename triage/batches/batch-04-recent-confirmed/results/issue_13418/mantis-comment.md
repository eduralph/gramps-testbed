Confirmed and fixed. The traceback in the description is the real one for this
report: str_incr in latexdoc.py, which generates the column ids for LaTeX table
multicolumns, looped with "for i in reversed(lili)". That iterates the
characters of the counter rather than their positions, so lili[i] indexes the
list with a string and raises "TypeError: list indices must be integers or
slices, not str". The first value is yielded before the loop runs, so the crash
only appears once a table needs a second multicolumn id, which a note with
subscript/strikeout triggers.

The familygroup.py / "KeyError: 9" stack in note 1 is the separate report 13417
(styled-note markup), not this one; that was a different code path and is
already handled. This str_incr defect is independent of it.

The fix iterates the indices instead of the elements
(for i in reversed(range(len(lili)))), preserving the existing carry behaviour.
A headless unit test was added under gramps/plugins/docgen/test/ that exercises
str_incr and reproduces the crash on the unfixed code.

Fixed in PR p:gramps:2341: on the maintenance/gramps61 branch.

Fixed in version: 6.1.0.
