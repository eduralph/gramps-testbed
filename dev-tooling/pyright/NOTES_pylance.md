# Pylance/pyright — tuning notes

You already have this via Pylance; the VSC noise is the GTK-typing rules, NOT the None
rules. The experiment is to isolate the None/Optional rules on the hot files.

## Run it scoped (CLI, to see ONLY None findings)
    pip install pyright            # or: npm i -g pyright
    pyright --project pyrightconfig.experiment.json
(Or in VSC: point python.analysis to this config / open only the hot files with this
config active, so the squiggles you see are ONLY the Optional-access ones.)

## What to expect per class
- A1 (fanchart None-sentinel): pyright SHOULD flag the .append on the possibly-None slot,
  because the None is in Gramps's OWN python container — pyright's strength. Good positive
  control. If it flags pre-fix and not post-fix (PR 2315), it's working.
- A3 (styledtexteditor get_child / startswith on None): MIXED — the None is on a GTK
  object (tag, child widget) which pyright models poorly. May miss or false-positive.
  Expect weaker results here; this is the boundary-nullability case where shape (Semgrep)
  or flow-on-typed-code is needed. Don't force it.
- A2 (teardown): pyright will NOT catch the lifecycle/ordering pattern — that's not a type
  error. Leave A2 to Semgrep (disposal half) / CodeQL (init half).

## "Ready" for pyright
Flags fanchart pre-fix .append (A1 positive), silent on fanchart post-fix (A1 negative),
zero false positives across the 5 hot files. If GTK-object false positives appear in
styledtexteditor, that's expected — narrow 'include' to where pyright is reliable (the
pure-python-state files) rather than fighting GTK typing.

## Honest scope
pyright owns the GENERIC type-level None-flow. It is the EARLIEST catch (in-editor) but
the NARROWEST (only what the type system sees). It is not the Gramps-pattern detector —
that's Semgrep. Tune it quiet, trust it for what it's good at, don't expand it into noise.
