"""Base class for Gramps GUI tests driven via AT-SPI / dogtail.

Written as a ``unittest.TestCase`` subclass so tests can be proposed upstream
(gramps-project/gramps) without a framework rewrite.

Environment prerequisites (handled by CI / scripts/run-local.sh):
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
    LAUNCH_TIMEOUT_SEC: int = 30
    SCREENSHOT_DIR: Path = Path(os.environ.get("ARTIFACTS_DIR", "artifacts")) / "screenshots"

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.SCREENSHOT_DIR.mkdir(parents=True, exist_ok=True)

        cls._proc = subprocess.Popen(
            ["gramps", "-O", cls.TREE_NAME],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )

        deadline = time.monotonic() + cls.LAUNCH_TIMEOUT_SEC
        last_err: Exception | None = None
        while time.monotonic() < deadline:
            try:
                app = root.application("gramps")
                if app.findChildren(lambda n: n.roleName == "frame"):
                    cls.app = app
                    return
            except Exception as exc:
                last_err = exc
            time.sleep(1)

        cls._capture_screenshot("launch-failure")
        cls._terminate_process()
        raise RuntimeError(
            f"Gramps main window did not appear within "
            f"{cls.LAUNCH_TIMEOUT_SEC}s (last error: {last_err!r})"
        )

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
