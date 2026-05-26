# Semgrep — bring-up notes

## Install & run
    pip install semgrep
    cd dev-tooling/semgrep
    semgrep --config gramps-connect-without-disconnect.yml ../../../gramps/gramps/gui/
    semgrep --test tests/           # validate against the labeled fixtures

## The iteration loop (this is the experiment)
1. Run --test tests/ — does the rule flag the POSITIVE fixtures and not the NEGATIVE/ok?
2. Run against real gramps/gui/ — count false positives. Authoring-time tool ⇒ target ZERO.
3. Refine: constrain $CLEANUP to real cleanup-method names (metavariable-regex on
   _cleanup_callbacks|close|_do_close|disconnect_all|destroy), tighten connect idioms to
   Gramps's actual ones (GObject .connect, dbstate.connect, callman.register_*). Track the
   specific handler id, not "any disconnect".
4. Repeat until: all positive controls flag, all negative controls clean, zero FP on gui/.

## Honest scope (put this in any upstream proposal)
- Catches the DISPOSAL half of A2 (connect present, no disconnect). 
- Does NOT catch the INIT half (14177 — no connect to match). That's CodeQL/structural.
- Name the rule's coverage precisely: "post-disposal callback dispatch", not "A2 bugs".

## Why Semgrep here and not pyright/CodeQL
This pattern is a SHAPE (connect without disconnect), not a type error (pyright can't see
it) and doesn't need full dataflow (CodeQL is overkill). Shape ⇒ Semgrep. And being
shape-based, it's QUIET on untyped GTK code — sidesteps the noise that made pyright hard.
