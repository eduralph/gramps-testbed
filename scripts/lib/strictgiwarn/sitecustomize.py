"""Promote PyGObject's ``PyGIWarning`` to an error for addon test runs.

This directory is prepended to ``PYTHONPATH`` only for the per-addon test
invocation in ``scripts/ubuntu/run-addon-unit.sh`` (and the mirrored CI step),
so the interpreter imports this ``sitecustomize`` at startup — after site
initialisation, when ``gi`` is importable.

Why: a ``PyGIWarning`` ("X was imported without specifying a version first")
means an addon imported a GI module without pinning its version. That is the
early symptom of the GTK/Gdk-version fragility that otherwise only shows up as
a silent, all-skipped test run on a host whose default Gdk differs — which the
runner would still report as PASS. Turning the warning into an error makes it
fail loudly, on any host, even when the tests would otherwise run.

It is scoped to ``PyGIWarning`` specifically: ``PyGIDeprecationWarning`` is a
separate class (not a subclass), so unrelated GLib/Gtk deprecation noise stays
non-fatal.

This cannot be done with ``-W error::gi.PyGIWarning`` / ``PYTHONWARNINGS``: that
category is resolved by importing ``gi`` at warnings-setup time, which is too
early in interpreter startup and is silently discarded
(``Invalid -W option ignored: invalid module name: 'gi'``).

NOTE: the test runner must still pass *some* ``-W`` flag (a harmless
``-W ignore::ImportWarning`` will do). ``python -m unittest`` / ``xmlrunner``
call ``warnings.simplefilter("default")`` — which wipes the filter set here —
unless ``sys.warnoptions`` is non-empty. The dummy ``-W`` keeps it non-empty so
this filter survives the run; see scripts/ubuntu/run-addon-unit.sh.
"""

import warnings

try:
    import gi

    warnings.filterwarnings("error", category=gi.PyGIWarning)
except Exception:
    # No PyGObject here (or it changed shape): nothing to promote. The test's
    # own import guard / the skip-detection gate still cover the run.
    pass
