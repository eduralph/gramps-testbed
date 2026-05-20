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

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.SCREENSHOT_DIR.mkdir(parents=True, exist_ok=True)

        # ``-c behavior.use-tips:False`` suppresses the Tip of the Day
        # frame, which otherwise appears asynchronously a few seconds
        # after the main window paints and grabs input focus. With it up,
        # raw X clicks delivered at AT-SPI label coordinates are
        # intercepted by the tip dialog rather than reaching the
        # widgets we're trying to drive. The setting also persists in
        # the gramps config so subsequent launches stay clean.
        config_args: list[str] = []
        for setting in ("behavior.use-tips:False", *cls.LAUNCH_CONFIG):
            config_args += ["-c", setting]

        launch_env = None
        if cls.LAUNCH_ENV:
            launch_env = {**os.environ, **cls.LAUNCH_ENV}

        cls._proc = subprocess.Popen(
            ["gramps", *config_args, "-O", cls.TREE_NAME],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            env=launch_env,
        )

        deadline = time.monotonic() + cls.LAUNCH_TIMEOUT_SEC
        last_err: Exception | None = None
        while time.monotonic() < deadline:
            try:
                app = root.application("gramps")
                cls._dismiss_startup_dialogs(app)
                if app.findChildren(
                    lambda n: n.roleName == "frame"
                    and cls.TREE_NAME in (n.name or "")
                ):
                    cls.app = app
                    return
            except Exception as exc:
                last_err = exc
            time.sleep(1)

        cls._capture_screenshot("launch-failure")
        cls._dump_tree_on_timeout()
        cls._terminate_process()
        raise RuntimeError(
            f"Gramps main window with tree {cls.TREE_NAME!r} did not appear "
            f"within {cls.LAUNCH_TIMEOUT_SEC}s (last error: {last_err!r})"
        )

    @classmethod
    def _dump_tree_on_timeout(cls) -> None:
        """Best-effort dump of the Gramps AT-SPI tree for diagnostics."""
        try:
            app = root.application("gramps")
        except Exception:
            print("TIMEOUT-DUMP: gramps application not visible in AT-SPI")
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
        """
        for modal in app.findChildren(
            lambda n: n.roleName in ("dialog", "alert")
        ):
            clicked = False
            for btn in modal.findChildren(
                lambda n: n.roleName == "push button"
                and n.name in ("Close", "OK", "Cancel")
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
            # screenshots are best-effort; don't mask the original failure
            pass

    def run(self, result=None):  # type: ignore[override]
        outcome = super().run(result)
        if result is not None and (result.failures or result.errors):
            type(self)._capture_screenshot(self._testMethodName)
        return outcome
