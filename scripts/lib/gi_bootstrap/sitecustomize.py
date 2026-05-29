"""Pin the GObject-introspection versions for addon test runs.

This directory is prepended to ``PYTHONPATH`` only for the per-addon test
invocation in ``scripts/ubuntu/run-addon-unit.sh`` (and the mirrored CI step),
so the interpreter imports this ``sitecustomize`` at startup — before any test
imports a ``gramps.gui`` module.

Why: gramps pins its GI versions in the **GUI launcher**
(``gramps/gui/grampsgui.py`` calls ``gi.require_version`` for
``Pango``/``PangoCairo``/``Gtk`` at module import). A unit test that imports a
``gramps.gui.*`` submodule directly never runs that launcher, so ``Gtk``/``Pango``
get imported with no version pinned first — which emits a ``PyGIWarning`` and, on
a host where GTK 4 is the default resolution, risks loading the wrong stack and
the addon test silently skipping. This shim performs the same ``require_version``
bootstrap the launcher does, so addon tests import ``gramps.gui`` modules under
the supported GTK 3 stack, exactly as a real Gramps session would.

(An earlier version promoted ``PyGIWarning`` to an error instead. That was wrong:
the warning is emitted by gramps core's own unversioned import — not the addon's
code — so it fired for essentially every addon test that imports ``gramps.gui``.
Pinning the version, like the launcher, is the correct fix.)

Mirrors ``gramps/gui/grampsgui.py``; keep the namespace/version set in sync if
the launcher's set changes. Silent-skip detection
(``scripts/lib/junit_coverage.py``) remains the backstop that turns a skipped
run into a failure.
"""

try:
    import gi

    # Same set and order as gramps/gui/grampsgui.py. require_version alone (no
    # import) is enough to pin the version for later imports; bringing in
    # Gtk 3.0 also pins its Gdk/GdkPixbuf dependencies transitively.
    gi.require_version("Pango", "1.0")
    gi.require_version("PangoCairo", "1.0")
    gi.require_version("Gtk", "3.0")
except Exception:
    # No PyGObject here, or a namespace/version is unavailable: leave the
    # environment untouched. The skip-detection gate still guards the run.
    pass
