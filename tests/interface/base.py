"""Base class for Gramps GUI tests driven via AT-SPI / dogtail.

Written as a ``unittest.TestCase`` subclass so tests can be proposed upstream
(gramps-project/gramps) without a framework rewrite.

Environment prerequisites (handled by CI / scripts/ubuntu/run-interface.sh):
  * Xvfb running on $DISPLAY
  * A D-Bus session bus (dbus-run-session)
  * at-spi-bus-launcher active
  * gsettings: org.gnome.desktop.interface toolkit-accessibility = true
"""

from __future__ import annotations

import os
import subprocess
import tempfile
import time
import unittest
from pathlib import Path

from dogtail.config import config
from dogtail.rawinput import keyCombo
from dogtail.tree import root
from dogtail.utils import screenshot

config.searchShowingOnly = False
config.actionDelay = 0.3
config.logDebugToStdOut = True


class GrampsInterfaceTestCase(unittest.TestCase):
    """One Gramps process per TestCase class, opened on a named tree.

    Subclasses get ``cls.app`` — the dogtail Application root for Gramps.
    A screenshot is captured automatically on any test failure or error.
    """

    TREE_NAME: str = "TestTree"
    LAUNCH_TIMEOUT_SEC: int = 60
    SCREENSHOT_DIR: Path = Path(os.environ.get("ARTIFACTS_DIR", "artifacts")) / "screenshots"

    # Subclasses may launch Gramps under a specific UI language or with
    # extra ``-c key:value`` config settings. The defaults preserve the
    # plain English launch used by every test that does not set them.
    LAUNCH_ENV: dict[str, str] | None = None
    LAUNCH_CONFIG: tuple[str, ...] = ()

    # When True (default), setUpClass insists that ``gramps -O TREE_NAME``
    # actually opens the tree -- it loops until a frame titled with
    # TREE_NAME appears, and a timeout is a class-level ERROR. Set False
    # in a subclass whose test exercises a bug that crashes the tree-open
    # path itself (e.g. bug 14100, where a Finnish about-date raises
    # KeyError during render at tree-open and the launch lands on "No
    # Family Tree loaded" instead). In that mode setUpClass records
    # ``cls.tree_opened = False`` and returns, so the test method can
    # fail cleanly with a clear bug-pointer message.
    TREE_REQUIRED: bool = True

    # Set by setUpClass: whether ``gramps -O TREE_NAME`` actually opened
    # the tree. Always True under the default required-tree launch; only
    # ever False under ``TREE_REQUIRED = False``.
    tree_opened: bool = True

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.SCREENSHOT_DIR.mkdir(parents=True, exist_ok=True)

        # The defaults below are PERSISTED writes to ~/.gramps/grampsrc.
        # Every test launch starts by resetting these, which guards against
        # state leaking from a previous test class. Subclasses can still
        # override individual settings via LAUNCH_CONFIG; the per-subclass
        # entries appear AFTER the defaults below, so they win.
        #
        # - behavior.use-tips:False suppresses the Tip of the Day frame,
        #   which otherwise appears asynchronously a few seconds after
        #   the main window paints and grabs input focus, intercepting
        #   raw X clicks aimed at AT-SPI label coordinates.
        # - preferences.date-format:0 resets to the safe ISO-like default.
        #   Without this, Bug14100RelviewInflectionKeyErrorTest's
        #   LAUNCH_CONFIG=("preferences.date-format:2",) — the Finnish
        #   long-month format — persists into subsequent tests. When those
        #   tests reopen TestTree (whose example.gramps data contains
        #   "about January 1652"-style dates), gramps hits the
        #   KeyError: 'noin' inflection bug (Mantis 14100, fix gramps#2322
        #   not yet merged) while rendering the tree, and hangs in
        #   startup before reaching AT-SPI registration — manifesting as
        #   SearchError("Application 'gramps' was not found in desktop")
        #   in SmokeTest / CombinedViewStaleCloseTest setUpClass.
        defaults = (
            "behavior.use-tips:False",
            "preferences.date-format:0",
        )
        config_args: list[str] = []
        for setting in (*defaults, *cls.LAUNCH_CONFIG):
            config_args += ["-c", setting]

        launch_env = None
        if cls.LAUNCH_ENV:
            launch_env = {**os.environ, **cls.LAUNCH_ENV}

        # Tempfiles instead of PIPE: the wait loop below doesn't drain
        # the captured streams, so the 64KB pipe buffer would block
        # gramps mid-startup if it wrote that much (verbose logging,
        # warnings, etc). Tempfiles have no buffer limit and we still
        # get full output at timeout via _dump_subprocess_output_on_timeout.
        cls._stdout_file = tempfile.NamedTemporaryFile(
            mode="w+b", prefix="gramps-stdout-", suffix=".log", delete=False
        )
        cls._stderr_file = tempfile.NamedTemporaryFile(
            mode="w+b", prefix="gramps-stderr-", suffix=".log", delete=False
        )
        cls._launched_at = time.monotonic()
        # ``-u`` / ``--force-unlock`` breaks any stale lock file on
        # ``TREE_NAME`` from a previous test class's gramps that was
        # SIGKILL'd by ``_terminate_process`` (the tear-down sends SIGTERM
        # with a 10s grace period, then SIGKILL; SIGKILL doesn't let
        # gramps release the BSD lock file under
        # ``~/.gramps/grampsdb/<TREE>/``). Without this flag, the next
        # gramps starts up, hits ``check_db`` in
        # ``gramps/cli/arghandler.py``, sees a locked tree, calls
        # ``self.__error("Database is locked, cannot open it!")``, which
        # under GUI mode (DISPLAY set under Xvfb) routes to the GUI
        # errorfunc and shows an invisible dialog instead of printing to
        # stderr, then ``sys.exit(1)``. Manifests as gramps exiting
        # silently with rc=1 about 3-4s into the launch (post-argparse,
        # mid-DB-open), which is exactly what we see for the failing
        # SmokeTest and CombinedViewStaleCloseTest setUpClasses.
        cls._proc = subprocess.Popen(
            ["gramps", "-u", *config_args, "-O", cls.TREE_NAME],
            stdout=cls._stdout_file,
            stderr=cls._stderr_file,
            env=launch_env,
        )

        deadline = time.monotonic() + cls.LAUNCH_TIMEOUT_SEC
        last_err: Exception | None = None
        app = None
        while time.monotonic() < deadline:
            # Early-exit: if gramps already died, no point waiting for
            # AT-SPI to show it. Break out so we dump the captured output
            # immediately instead of blocking until LAUNCH_TIMEOUT_SEC.
            rc = cls._proc.poll()
            if rc is not None:
                last_err = RuntimeError(
                    f"gramps exited prematurely with rc={rc} after "
                    f"{time.monotonic() - cls._launched_at:.1f}s"
                )
                break
            try:
                app = root.application("gramps")
                cls._dismiss_startup_dialogs(app)
                if app.findChildren(
                    lambda n: n.roleName == "frame"
                    and cls.TREE_NAME in (n.name or "")
                ):
                    cls.app = app
                    cls.tree_opened = True
                    return
            except Exception as exc:
                last_err = exc
            time.sleep(1)

        # Timeout. Either gramps never reached AT-SPI (app is None), or
        # gramps came up but never opened a frame titled TREE_NAME --
        # i.e. ``gramps -O TREE_NAME`` failed to open the tree (e.g. it
        # crashed while rendering the tree's content on the way in).
        # Tests opt in to the second case by setting TREE_REQUIRED = False,
        # which lets setUpClass return so the test method can assert
        # about the failed tree-open instead of dying here.
        if app is not None and not cls.TREE_REQUIRED:
            cls.app = app
            cls.tree_opened = False
            return

        cls._capture_screenshot("launch-failure")
        # poll() BEFORE terminate distinguishes "gramps already exited
        # on its own" (returncode is an int) from "still running"
        # (returncode is None — we are about to send SIGTERM). A
        # silent crash with no traceback otherwise looks identical to
        # a slow startup.
        pre_kill_rc = cls._proc.poll() if getattr(cls, "_proc", None) else None
        if pre_kill_rc is not None:
            print(f"GRAMPS-EXIT: process exited on its own with rc={pre_kill_rc}")
        else:
            print("GRAMPS-EXIT: process still running at timeout (will SIGTERM)")
        cls._dump_tree_on_timeout()
        cls._terminate_process()
        # After terminate, drain the captured stdout/stderr. Gramps was
        # launched with stdout=PIPE, stderr=PIPE but nothing read them
        # during the wait loop — without this dump the only diagnostic
        # on timeout is "gramps not in AT-SPI", which doesn't say why
        # (crash on startup? slow startup? missing dep? lock conflict?).
        cls._dump_subprocess_output_on_timeout()
        raise RuntimeError(
            f"Gramps main window with tree {cls.TREE_NAME!r} did not appear "
            f"within {cls.LAUNCH_TIMEOUT_SEC}s (last error: {last_err!r})"
        )

    def setUp(self) -> None:
        """Dismiss any modal dialog that appeared since setUpClass exited.

        setUpClass returns as soon as a frame titled with ``TREE_NAME``
        is visible in AT-SPI, but Gramps still does asynchronous startup
        work after that — emitting deferred warnings, the Tip of the Day
        frame, and (under ``-u``) the "Gramps had a problem the last
        time it was run" recovery prompt. Without dismissing those at
        the start of every test, the dialog stays up and intercepts
        clicks aimed at the main UI (sidebar toggles, etc.), so calls
        like ``self.app.child(roleName="tree table")`` fail with
        SearchError on what looks like an unresponsive view.
        """
        super().setUp()
        app = getattr(type(self), "app", None)
        if app is not None:
            try:
                type(self)._dismiss_startup_dialogs(app)
            except Exception:
                # Best-effort — failure here shouldn't mask the test's
                # own assertion. We've still got the AT-SPI tree dump
                # on test failure to debug.
                pass

    @classmethod
    def _dump_subprocess_output_on_timeout(cls) -> None:
        """Print everything gramps wrote to stdout/stderr.

        Called after ``_terminate_process`` from the setUpClass failure
        path. Reads the tempfiles backing stdout/stderr (no 64KB pipe
        buffer limit — gramps could write megabytes of warnings during
        a slow startup without blocking). Prefixes each line with
        ``GRAMPS-<stream>:`` so the dump is greppable.
        """
        for stream_name, tmp_attr in (("stdout", "_stdout_file"), ("stderr", "_stderr_file")):
            tmp = getattr(cls, tmp_attr, None)
            if tmp is None:
                continue
            try:
                tmp.flush()
                tmp.seek(0)
                data = tmp.read()
            except Exception as exc:
                print(f"GRAMPS-{stream_name}: <failed to read tempfile: {exc!r}>")
                continue
            if not data:
                print(f"GRAMPS-{stream_name}: <empty>")
                continue
            text = data.decode("utf-8", errors="replace")
            for line in text.splitlines():
                print(f"GRAMPS-{stream_name}: {line}")
        # Clean up the tempfiles (delete=False meant the OS didn't).
        for tmp_attr in ("_stdout_file", "_stderr_file"):
            tmp = getattr(cls, tmp_attr, None)
            if tmp is None:
                continue
            try:
                tmp.close()
                os.unlink(tmp.name)
            except Exception:
                pass

    @classmethod
    def _dump_tree_on_timeout(cls) -> None:
        """Best-effort dump of the Gramps AT-SPI tree for diagnostics."""
        try:
            app = root.application("gramps")
        except Exception:
            print("TIMEOUT-DUMP: gramps application not visible in AT-SPI")
            # When gramps isn't visible under that exact name, the next
            # most useful question is "what IS visible". A misnamed
            # process (e.g. registered as 'python3' instead of 'gramps')
            # would show up here, as would an empty registry indicating
            # the AT-SPI bridge itself died.
            try:
                visible = []
                for child in root.children:
                    try:
                        visible.append(getattr(child, "name", "") or "?")
                    except Exception:
                        visible.append("?")
                print(f"TIMEOUT-DUMP: AT-SPI registry has {len(visible)} apps: {visible!r}")
            except Exception as exc:
                print(f"TIMEOUT-DUMP: failed to enumerate AT-SPI registry: {exc!r}")
            return

        def _walk(node, depth: int = 0, max_depth: int = 6) -> None:
            try:
                name = getattr(node, "name", "") or ""
                role = getattr(node, "roleName", "") or ""
                print(f"TIMEOUT-DUMP {'  ' * depth}[{role}] {name!r}")
            except Exception:
                return
            if depth >= max_depth:
                return
            try:
                children = list(node.children)
            except Exception:
                return
            for child in children:
                _walk(child, depth + 1, max_depth)

        print("TIMEOUT-DUMP >>> begin")
        _walk(app)
        print("TIMEOUT-DUMP <<< end")

    @classmethod
    def _dismiss_startup_dialogs(cls, app) -> None:
        """Close modal dialogs/alerts blocking the main frame.

        Gramps emits startup warnings (GExiv2 missing, GTK translations missing,
        etc.) as GtkMessageDialog instances, which surface with ``roleName``
        ``dialog`` or ``alert`` in AT-SPI. Leaving them up blocks the main loop,
        so ``gramps -O <tree>`` never actually opens the tree.

        Two button-set categories are handled:
          * generic dismissal — ``Close`` / ``OK`` / ``Cancel`` — for
            informational warnings (e.g. "GExiv2 not available").
          * "decline this offered tool" — ``No`` — for the
            "Gramps had a problem the last time it was run.  Would you
            like to run the Check and Repair tool?" dialog. This appears
            on every launch under ``-u``/``--force-unlock`` because the
            previous test class's tearDown sent SIGTERM/SIGKILL to
            gramps; that looks like an unclean exit to the next launch,
            triggering the recovery prompt.

        Buttons must be ``showing=True`` — gramps puts non-visible
        ``Cancel`` buttons on the recovery dialog (the visible buttons
        are ``Yes`` / ``No``). Without the visibility filter, a "click"
        on the invisible Cancel was a no-op but set ``clicked = True``,
        so the Escape fallback was suppressed and the dialog stayed up.
        """
        for modal in app.findChildren(
            lambda n: n.roleName in ("dialog", "alert")
        ):
            clicked = False
            for btn in modal.findChildren(
                lambda n: n.roleName == "push button"
                and (n.name or "") in ("Close", "OK", "Cancel", "No")
                and getattr(n, "showing", False)
            ):
                try:
                    btn.click()
                    clicked = True
                except Exception:
                    pass
            # Button names are localized (e.g. Finnish "Sulje"), so a
            # named-button match can miss when Gramps runs in another
            # language. Escape dismisses a standard GtkMessageDialog
            # regardless of UI language.
            if not clicked:
                try:
                    if modal.showing:
                        keyCombo("Escape")
                except Exception:
                    pass

    @classmethod
    def tearDownClass(cls) -> None:
        cls._terminate_process()
        # Clean up the stdout/stderr tempfiles created in setUpClass.
        # On the failure path these are already unlinked by
        # _dump_subprocess_output_on_timeout; this is the success path.
        for tmp_attr in ("_stdout_file", "_stderr_file"):
            tmp = getattr(cls, tmp_attr, None)
            if tmp is None:
                continue
            try:
                tmp.close()
                os.unlink(tmp.name)
            except Exception:
                pass
        super().tearDownClass()

    # ---- helpers -----------------------------------------------------------

    @classmethod
    def _terminate_process(cls) -> None:
        proc = getattr(cls, "_proc", None)
        if proc is None:
            return
        proc.terminate()
        try:
            proc.wait(timeout=10)
        except subprocess.TimeoutExpired:
            proc.kill()
            proc.wait(timeout=5)

    @classmethod
    def _capture_screenshot(cls, label: str) -> None:
        path = cls.SCREENSHOT_DIR / f"{label}-{int(time.time())}.png"
        try:
            screenshot(str(path))
        except Exception:
            # screenshots are best-effort; don't mask the original failure.
            # dogtail's screenshot helper requires the ``dasbus`` Python
            # package which isn't installed in CI, so this typically silently
            # no-ops there (see test_bug_0002092_geography_focused for a
            # Gdk-pixbuf-based screenshot helper that works in the same env).
            pass

    @classmethod
    def _dump_app_tree_on_failure(cls, label: str) -> None:
        """Walk and print the AT-SPI tree of the gramps app at failure time.

        dogtail's screenshot is broken in this environment (missing dasbus
        package — see ``_capture_screenshot``), so visual evidence isn't
        available. The AT-SPI tree dump is the next-best diagnostic: it
        tells you what widgets exist (and which don't) when a test like
        ``self.app.child(roleName="tree table")`` raises SearchError, so
        you can tell whether the test was timing-racing against an
        in-progress view switch, looking for the wrong role/name, or the
        addon's view never registered at all. Prefixes each line with
        ``FAILDUMP-<label>:`` so the per-test output is greppable.
        """
        app = getattr(cls, "app", None)
        if app is None:
            print(f"FAILDUMP-{label}: cls.app is None — no AT-SPI tree to dump")
            return

        def _walk(node, depth: int = 0, max_depth: int = 8) -> None:
            try:
                name = (getattr(node, "name", "") or "").strip()
                role = getattr(node, "roleName", "") or ""
                showing = getattr(node, "showing", "?")
                print(
                    f"FAILDUMP-{label}: {'  ' * depth}[{role}] {name!r} "
                    f"(showing={showing})"
                )
            except Exception as exc:
                print(f"FAILDUMP-{label}: {'  ' * depth}<failed node read: {exc!r}>")
                return
            if depth >= max_depth:
                return
            try:
                children = list(node.children)
            except Exception:
                return
            for child in children:
                _walk(child, depth + 1, max_depth)

        print(f"FAILDUMP-{label} >>> begin")
        try:
            _walk(app)
        except Exception as exc:
            print(f"FAILDUMP-{label}: walk aborted: {exc!r}")
        print(f"FAILDUMP-{label} <<< end")

    def run(self, result=None):  # type: ignore[override]
        outcome = super().run(result)
        if result is not None and (result.failures or result.errors):
            type(self)._capture_screenshot(self._testMethodName)
            # AT-SPI tree dump on failure: tells us what was visible at
            # the moment of the assertion. See _dump_app_tree_on_failure
            # for rationale (dogtail screenshot is broken in CI).
            type(self)._dump_app_tree_on_failure(self._testMethodName)
        return outcome
