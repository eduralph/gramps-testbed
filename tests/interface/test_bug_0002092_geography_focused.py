"""Focused #2092 verification — Geography view stale-marker check.

The umbrella Mantis #2092 diagnostic
(``test_bug_0002092_no_db_state.py``) was inconclusive for Geography
because (a) its ``_capture_geography_view`` is a SKIP-stub that doesn't
even screenshot, and (b) the sidebar-toggle navigation past the first
hop is unreliable in the AT-SPI ``.click()`` form. Code-reading
``gramps/plugins/lib/maps/geography.py:324-340`` shows ``change_db``
early-returns on ``DummyDb`` without calling ``build_tree()`` or
clearing the OSM widget's markers, which matches kulath's 2020
"stale display" pattern.

This test confirms the runtime symptom by raw_click-navigating to
Geography → Places, waiting for tiles + markers to render, screenshotting,
closing the tree via the menubar, screenshotting again. Whether the
post-close screenshot still shows markers is the verdict.

This is throwaway — once the bug is confirmed (or refuted) and a fix
PR is opened upstream, retire it.
"""

from __future__ import annotations

import time
import unittest

from dogtail.rawinput import click as raw_click

from .base import GrampsInterfaceTestCase


class Bug2092GeographyStaleMarkersTest(GrampsInterfaceTestCase):
    """Drive Geography → Places, close tree, screenshot before+after."""

    TREE_NAME = "TestTree"
    # Match the #8594 test's window-size override so the sidebar +
    # Geography subview list aren't clipped.
    LAUNCH_CONFIG = (
        "interface.main-window-width:1800",
        "interface.main-window-height:1000",
    )

    @staticmethod
    def _screenshot(label: str) -> None:
        try:
            import gi
            gi.require_version("Gdk", "3.0")
            from gi.repository import Gdk
            import os
            # ARTIFACTS_DIR is set by both CI (interface-tests.yml) and the
            # local Docker runner (agent-work/scripts/ubuntu/run-interface.sh). Falling
            # back to "artifacts" mirrors base.py:SCREENSHOT_DIR. A previous
            # hard-coded "/workspace/gramps-testbed/artifacts/screenshots"
            # path worked only inside the Docker container and failed in
            # CI with PermissionError(13).
            outdir = os.path.join(
                os.environ.get("ARTIFACTS_DIR", "artifacts"),
                "screenshots",
            )
            os.makedirs(outdir, exist_ok=True)
            root = Gdk.get_default_root_window()
            w, h = root.get_width(), root.get_height()
            pb = Gdk.pixbuf_get_from_window(root, 0, 0, w, h)
            pb.savev(f"{outdir}/2092-geo-{label}.png", "png", [], [])
            print(f"  screenshot saved: 2092-geo-{label}.png ({w}x{h})")
        except Exception as exc:
            print(f"  screenshot {label!r} FAILED: {exc!r}")

    def _click_by_coords(self, node) -> bool:
        """raw_click the centre of an AT-SPI node. Returns True on
        success (node visible and clicked); False otherwise."""
        try:
            if not node.showing:
                return False
            pos = node.position
            size = node.size
        except Exception:
            return False
        if pos[0] < 0 or size[0] <= 0:
            return False
        raw_click(pos[0] + size[0] // 2, pos[1] + size[1] // 2, button=1)
        return True

    def _click_sidebar_category(self, name: str) -> bool:
        for n in self.app.findChildren(
            lambda n, _n=name: n.roleName == "toggle button"
            and (n.name or "") == _n
        ):
            if self._click_by_coords(n):
                return True
        return False

    def _close_tree_via_menubar(self) -> bool:
        """Open Family Trees → Close from the menubar via raw_click.
        AT-SPI strips the underscore accel marker so the menu name is
        'Family Trees' / 'Close' (no underscore)."""
        for menu in self.app.findChildren(
            lambda n: n.roleName == "menu" and (n.name or "") == "Family Trees"
        ):
            if not self._click_by_coords(menu):
                continue
            time.sleep(0.4)
            for item in self.app.findChildren(
                lambda n: n.roleName == "menu item" and (n.name or "") == "Close"
            ):
                try:
                    if item.showing:
                        item.click()
                        time.sleep(1.5)
                        return True
                except Exception:
                    continue
        return False

    def test_geography_clears_on_close(self) -> None:
        # Click Home first so an active person is set — many Geography
        # subviews paint markers anchored on the active person's
        # events / places.
        for n in self.app.findChildren(
            lambda n: n.roleName == "push button" and (n.name or "") == "Home"
        ):
            if self._click_by_coords(n):
                time.sleep(0.4)
                break

        # Navigate to Geography. Use raw_click rather than AT-SPI
        # .click() — the latter sticks unreliably past the first hop.
        self.assertTrue(
            self._click_sidebar_category("Geography"),
            "Geography sidebar toggle not found / not clickable",
        )
        time.sleep(1.5)

        # Geography's default subview is "Geographic View" — that's
        # typically the Places map. Give the OSM widget time to fetch
        # tiles and paint markers.
        time.sleep(4.0)
        self._screenshot("before-close")

        # Close the tree via menubar.
        self.assertTrue(
            self._close_tree_via_menubar(),
            "Could not invoke Family Trees → Close from the menubar",
        )
        time.sleep(2.0)
        self._screenshot("after-close")

        # Concrete assertion. Pre-close, the Geography view's title
        # area carries a label of the form "Person places for <active
        # person's name>". If clear_view fires on the "no-database"
        # signal (lib/maps/geography.py:143), every label referencing
        # the previous active person should disappear post-close.
        def _person_labels_present() -> list[str]:
            out: list[str] = []
            for n in self.app.findChildren(
                lambda n: n.roleName == "label"
            ):
                try:
                    if not n.showing:
                        continue
                    text = (n.name or "")
                except Exception:
                    continue
                if "Garner von Zieliński" in text:
                    out.append(text)
            return out

        self.assertFalse(
            _person_labels_present(),
            "Geography view still shows the previous active person's "
            "name after tree close — `clear_view` (lib/maps/geography.py"
            ":299) likely did not fire on the `no-database` signal. "
            "Compare artifacts/screenshots/2092-geo-{before,after}-close.png.",
        )


if __name__ == "__main__":
    unittest.main()
