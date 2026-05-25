"""Regression for Mantis #8594 ("right-click on a sibling in Relationship
View doesn't open the edit menu").

Reported in 2015 against Gramps 4.1.3 AIO on Windows XP SP3. Josip's
2015-06-12 diagnosis: right-click broke on the gramps41 branch
specifically, but worked on gramps42 and master. gramps60 inherits from
the working lineage, so this test exists both to verify the assertion and
to guard against future regression.

Path under test:
  gramps/plugins/view/relview.py:1502 ``_button_press`` —
  on _RIGHT_BUTTON, builds a one-item Gtk.Menu containing
  ``Edit Person (<name>)`` and pops it up at pointer.

  The handler is wired through ``widgets.LinkLabel`` for every clickable
  person in the Relationship View (parents, spouses, siblings, children).
  We exercise the siblings path specifically to mirror the bug report.

Window-size fix
---------------
gramps defaults ``interface.main-window-width=775``/``main-window-height=500``
(gen/config.py:252,255). Under xvfb with no window manager to maximize,
the Gtk.Window.fullscreen() call (viewmanager.py:389) is ignored, so the
window stays at that default. The relview's siblings section then renders
in clipped/empty viewport space — AT-SPI still reports each sibling
LinkLabel's extents, but the widget is not drawn at the reported pixels,
and raw_click delivered there hits nothing. ``LAUNCH_CONFIG`` (below)
overrides the saved geometry to 1800×1000 so the Siblings section
actually paints inside the viewport before we click.

Test design — three gated probes:
  1. **Menubar probe**: raw_click on the "Edit" menubar item must open
     the menu. This verifies rawinput.click delivers events at all.
  2. **Left-click probe**: raw_click on the sibling LinkLabel must change
     the active person (relview.py:1503 calls change_active(handle) on
     left-click). With the window-size override above this passes; the
     probe stays as a defensive guard so the right-click test never
     reports a false-positive bug from a click-delivery failure.
  3. **Right-click assertion**: raw_click button=3 on the sibling
     LinkLabel must produce a popup menu with an ``Edit Person (...)``
     item. Passing this confirms #8594 is fixed at runtime — not just by
     code-reading.

If probe 1 or 2 fails, the test skips with a clear "test infra cannot
drive this widget class" marker rather than reporting a false-positive
bug. Only a failure at step 3 — clicks delivered, left-click works,
right-click doesn't — confirms the original Mantis #8594 symptom.
"""

from __future__ import annotations

import time
import unittest

from dogtail.rawinput import click as raw_click
from dogtail.rawinput import keyCombo

from .base import GrampsInterfaceTestCase


# In example.gramps the home person Lewis Anderson Garner (handle
# _GNUJQCL9MD64AM56OH, id I0044) is the first child in family F0018,
# whose 11 other children appear in his Relationship View's Siblings
# section. We target Phebe — her given name is uncommon enough that a
# substring match against AT-SPI label nodes is unambiguous.
SIBLING_GIVEN_NAME = "Phebe"


class Bug8594RelviewSiblingRightClickTest(GrampsInterfaceTestCase):
    """Right-clicking a sibling's name in the Relationship View pops up
    a menu containing an ``Edit Person (<name>)`` item."""

    TREE_NAME = "TestTree"
    # gramps defaults interface.main-window-height to 500 (gen/config.py:252),
    # which under xvfb (no window manager to maximize) leaves the
    # Relationship View siblings region rendered but visually clipped
    # — the LinkLabels are in the GTK tree (AT-SPI reports their
    # extents) yet not actually drawn at the reported pixels, so raw
    # clicks land on empty space. Maximizing gramps makes the rendered
    # geometry match what AT-SPI advertises.
    # In xvfb there is no window manager to honour Gtk.Window.fullscreen(),
    # so we set the saved main-window geometry instead — gramps reads it
    # at startup via set_default_size (viewmanager.py:303). 1800×1000
    # fits inside the 1920×1080 xvfb screen and gives the relview viewport
    # enough vertical space to render the Siblings section visibly.
    LAUNCH_CONFIG = (
        "interface.main-window-width:1800",
        "interface.main-window-height:1000",
    )

    @staticmethod
    def _is_clickable(node) -> bool:
        try:
            if not node.showing:
                return False
            pos = node.position
            size = node.size
        except Exception:
            return False
        return pos[0] >= 0 and pos[1] >= 0 and size[0] > 0 and size[1] > 0

    def _click_toggle(self, name: str, timeout: float = 10.0) -> None:
        deadline = time.monotonic() + timeout
        while time.monotonic() < deadline:
            for n in self.app.findChildren(
                lambda n, _n=name: n.roleName == "toggle button"
                and (n.name or "") == _n
            ):
                if self._is_clickable(n):
                    n.click()
                    return
            time.sleep(0.3)
        self.fail(f"Sidebar toggle button {name!r} not found / not clickable")

    def _click_home_button(self) -> None:
        for n in self.app.findChildren(
            lambda n: n.roleName == "push button" and (n.name or "") == "Home"
        ):
            if self._is_clickable(n):
                n.click()
                time.sleep(0.5)
                return
        self.fail("Toolbar Home button not found")

    def _find_showing_label(self, substring: str, timeout: float = 10.0):
        deadline = time.monotonic() + timeout
        while time.monotonic() < deadline:
            for n in self.app.findChildren(
                lambda n: n.roleName == "label" and substring in (n.name or "")
            ):
                if self._is_clickable(n):
                    return n
            time.sleep(0.3)
        return None

    @staticmethod
    def _is_in_menu_bar(menu) -> bool:
        node = menu
        for _ in range(8):
            try:
                node = node.parent
            except Exception:
                return False
            if node is None:
                return False
            try:
                if node.roleName == "menu bar":
                    return True
                if node.roleName in ("frame", "application"):
                    return False
            except Exception:
                return False
        return False

    def _menubar_click_probe(self) -> bool:
        """Open the Edit menu by raw_click on its menubar header. Return
        True if at least one popup menu item becomes showing below the
        menubar (y > 30) within a short window. Dismiss the menu with
        Escape regardless."""
        edit_menu = None
        for n in self.app.findChildren(
            lambda n: n.roleName == "menu" and (n.name or "") == "Edit"
        ):
            try:
                if not n.showing:
                    continue
                pos, size = n.position, n.size
            except Exception:
                continue
            if pos[1] < 0 or pos[1] > 60 or size[0] <= 0:
                continue
            edit_menu = n
            break
        if edit_menu is None:
            return False
        pos, size = edit_menu.position, edit_menu.size
        raw_click(pos[0] + size[0] // 2, pos[1] + size[1] // 2, button=1)
        time.sleep(0.6)
        opened = False
        for child in self.app.findChildren(
            lambda n: n.roleName == "menu item"
        ):
            try:
                if child.showing and child.position[1] > 30:
                    opened = True
                    break
            except Exception:
                continue
        keyCombo("Escape")
        time.sleep(0.3)
        return opened

    def _frame_titles(self) -> list[str]:
        out: list[str] = []
        for f in self.app.findChildren(lambda n: n.roleName == "frame"):
            try:
                if f.showing:
                    out.append(f.name or "")
            except Exception:
                continue
        return out

    def _find_popup_with_edit_person_item(self, timeout: float = 3.0):
        deadline = time.monotonic() + timeout
        while time.monotonic() < deadline:
            for menu in self.app.findChildren(lambda n: n.roleName == "menu"):
                try:
                    if not menu.showing:
                        continue
                    pos = menu.position
                except Exception:
                    continue
                if pos[0] < 0 or pos[1] < 0:
                    continue
                if self._is_in_menu_bar(menu):
                    continue
                try:
                    items = [c for c in menu.children if c.roleName == "menu item"]
                except Exception:
                    continue
                for it in items:
                    try:
                        label = it.name or ""
                    except Exception:
                        continue
                    if label.startswith("Edit Person ("):
                        return menu, items, it
            time.sleep(0.2)
        return None

    def test_right_click_on_sibling_opens_edit_menu(self) -> None:
        self._click_toggle("Relationships")
        time.sleep(0.5)
        self._click_home_button()
        time.sleep(0.8)

        sibling = self._find_showing_label(SIBLING_GIVEN_NAME)
        if sibling is None:
            self._capture_screenshot("sibling-label-not-found")
            self.fail(
                f"Could not find a showing label containing "
                f"{SIBLING_GIVEN_NAME!r} in the Relationships view. "
                "The view may not have rendered the siblings section."
            )
        pos = sibling.position
        size = sibling.size
        cx = pos[0] + size[0] // 2
        cy = pos[1] + size[1] // 2

        # Probe 1: rawinput.click must reach gramps at all.
        if not self._menubar_click_probe():
            self.skipTest(
                "rawinput.click() does not deliver events to the menubar "
                "in this xvfb session — cannot exercise the right-click "
                "path either. Test infra issue, not a #8594 reproduction."
            )

        # Probe 2: rawinput.click must reach a LinkLabel inside the
        # relview's GtkScrolledWindow. Left-click on a sibling triggers
        # change_active(handle); we detect "active changed" by checking
        # the relview's main person-header label (at the top of the
        # view, y < 150), which repaints with the new active person's
        # name. The frame title — used previously — does not embed the
        # active person on gramps60.
        def _header_text() -> str:
            for n in self.app.findChildren(
                lambda n: n.roleName == "label"
            ):
                try:
                    if not n.showing:
                        continue
                    if n.position[1] >= 150:
                        continue
                    text = (n.name or "").strip()
                except Exception:
                    continue
                # Header has a person name (contains a comma) and length > 8.
                if "," in text and len(text) > 8:
                    return text
            return ""
        header_before = _header_text()
        raw_click(cx, cy, button=1)
        time.sleep(1.0)
        header_after = _header_text()
        left_click_worked = (
            SIBLING_GIVEN_NAME in header_after
            and SIBLING_GIVEN_NAME not in header_before
        )
        if not left_click_worked:
            # Defensive guard. With LAUNCH_CONFIG sizing the window to
            # 1800x1000 this should not fire — siblings render inside
            # the viewport and raw_click reaches the LinkLabel. If we
            # land here, the window-size override stopped working or
            # the relview layout changed in a way that pushes Phebe out
            # of the viewport again; skip rather than report a
            # false-positive bug.
            self._click_home_button()
            self.skipTest(
                f"rawinput.click button=1 on the sibling LinkLabel did "
                f"not change the active person (header was "
                f"{header_before!r}, still {header_after!r} after click). "
                "Click is not reaching the LinkLabel — most likely the "
                "Siblings section is not rendered in the visible viewport. "
                "Cannot exercise the right-click path."
            )

        # The left-click probe just changed the active person to the
        # sibling. To exercise the same right-click on the *original*
        # active person's siblings, navigate back and re-find Phebe.
        self._click_home_button()
        time.sleep(0.8)
        sibling = self._find_showing_label(SIBLING_GIVEN_NAME)
        self.assertIsNotNone(
            sibling, "Phebe label disappeared after returning to home"
        )
        pos = sibling.position
        size = sibling.size
        cx = pos[0] + size[0] // 2
        cy = pos[1] + size[1] // 2

        # Real test: right-click → Edit Person popup.
        raw_click(cx, cy, button=3)
        found = self._find_popup_with_edit_person_item()
        if found is None:
            self._capture_screenshot("no-edit-person-popup")
            self.fail(
                "Both probes passed (rawinput.click reaches the menubar "
                "AND a left-click on this LinkLabel switches the active "
                "person), so click delivery works — yet a right-click at "
                "the same coordinates did NOT produce a popup with an "
                "'Edit Person (...)' item within 3s. This is the "
                "original Mantis #8594 symptom on gramps60."
            )

        _menu, _items, edit_item = found
        self.assertIn(
            SIBLING_GIVEN_NAME, edit_item.name or "",
            f"Edit Person item label {edit_item.name!r} does not embed "
            f"the target sibling's given name",
        )
        keyCombo("Escape")
        time.sleep(0.2)


if __name__ == "__main__":
    unittest.main()
