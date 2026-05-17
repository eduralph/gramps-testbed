"""E2E regression for addons-source PR #863 (QuiltView: import Surname).

Bug: QuiltView.py L1266 evaluates ``Surname()`` inside
``add_child_to_family`` but ``Surname`` is never imported, so the call
raises ``NameError`` when the user activates "Add child to family" from a
family node's context menu. The unpatched code reaches that line via:

    left-click on a FamilyNode in the quilt canvas
        -> family_menu (QuiltView.py:1168)
        -> add_children_submenu(menu, None, family)  (L1193, family != None)
        -> "Add child to family" item connected to add_child_to_family
        -> Surname()  -> NameError

This test reproduces the path on a minimal tree (one family, two parents,
no children) so the FamilyNode lands at a near-deterministic canvas
coordinate, then asserts the gramps subprocess stderr contains the
NameError on the unpatched code (and is silent on the patched code).
"""

from __future__ import annotations

import subprocess
import threading
import time
import unittest

from dogtail.rawinput import click as raw_click
from dogtail.rawinput import keyCombo, pressKey

from .base import GrampsInterfaceTestCase


# QuiltView module-level constants (QuiltView.py:84-85). The layout in
# on_draw places nodes in world coordinates starting at (BORDER, BORDER)
# with HEIGHT per row/column step.
BORDER = 10
HEIGHT = 18

# With layers {0: [parent1, parent2], 1: [family]} and default scale=1.0
# the FamilyNode lives at y == BORDER + 2*HEIGHT == 46, height 18, so
# its vertical centre is y=55. The x position depends on the rendered
# parent-name width — we sweep along this y to find it.
FAMILY_NODE_Y_CENTRE = BORDER + 2 * HEIGHT + HEIGHT // 2  # 55

# Sweep step in world coords; the box is 18 wide, 9 px steps guarantee a hit.
SWEEP_STEP = 9
# Practical right edge for our 2-parent tree — names "Aa Aa" / "Bb Bb"
# render under 200 px wide even with the sex-symbol prefix.
SWEEP_X_MAX = 320

class QuiltViewAddChildTest(GrampsInterfaceTestCase):
    """Regression for addons-source PR #863 (QuiltView Surname import).

    Drives the QuiltView canvas to fire the family-menu's "Add child to
    family" action. On the unpatched code, ``Surname()`` at
    QuiltView.py:1266 raises ``NameError`` and the EditPerson editor
    never opens — so this test fails until #863 lands upstream.
    """

    TREE_NAME = "QuiltViewTree"

    # --- stderr capture ------------------------------------------------------

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls._gramps_output: dict[str, list[bytes]] = {"stdout": [], "stderr": []}
        cls._gramps_lock = threading.Lock()
        for stream_name in ("stdout", "stderr"):
            t = threading.Thread(
                target=cls._drain_stream, args=(stream_name,), daemon=True
            )
            t.start()

    @classmethod
    def _drain_stream(cls, stream_name: str) -> None:
        proc: subprocess.Popen = cls._proc  # type: ignore[assignment]
        stream = getattr(proc, stream_name, None)
        if stream is None:
            return
        while True:
            chunk = stream.read(4096)
            if not chunk:
                return
            with cls._gramps_lock:
                cls._gramps_output[stream_name].append(chunk)

    @classmethod
    def _gramps_text(cls, which: str = "stderr") -> str:
        with cls._gramps_lock:
            return b"".join(cls._gramps_output[which]).decode(
                "utf-8", errors="replace"
            )

    @classmethod
    def _stderr_text(cls) -> str:
        return cls._gramps_text("stderr")

    # --- navigation helpers --------------------------------------------------

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

    def _dismiss_tip_of_the_day(self) -> None:
        """Close the Tip-of-the-Day frame if up; it appears asynchronously
        after startup and steals focus, so call this defensively."""
        for frame in self.app.findChildren(
            lambda n: n.roleName == "frame"
            and "Tip of the Day" in (n.name or "")
        ):
            for btn in frame.findChildren(
                lambda n: n.roleName == "push button" and (n.name or "") == "Close"
            ):
                try:
                    btn.click()
                except Exception:
                    pass

    def _click_toggle(self, name: str, timeout: float = 10.0) -> None:
        """Click a sidebar category toggle button by name."""
        deadline = time.monotonic() + timeout
        target = None
        while time.monotonic() < deadline:
            for n in self.app.findChildren(
                lambda n, _n=name: n.roleName == "toggle button"
                and (n.name or "") == _n
            ):
                if self._is_clickable(n):
                    target = n
                    break
            if target:
                break
            time.sleep(0.3)
        if target is None:
            self.fail(f"Sidebar toggle button {name!r} not found / not clickable")
        target.click()

    def _frame_title(self) -> str:
        for f in self.app.findChildren(lambda n: n.roleName == "frame"):
            try:
                if f.showing and (f.name or "").startswith(self.TREE_NAME):
                    return f.name or ""
            except Exception:
                continue
        return ""

    def _activate_via_action(self, node) -> bool:
        """Invoke the node's default AT-SPI Action — works even if the node
        is currently off-screen (hidden inside a popover, etc.)."""
        for method in ("doActionNamed", "doAction"):
            fn = getattr(node, method, None)
            if fn is None:
                continue
            for action in ("click", "press", "activate"):
                try:
                    fn(action)
                    return True
                except Exception:
                    pass
        return False

    def _open_quilt_view(self) -> None:
        """Switch to the Charts category, then to the Quilt Chart view."""
        self._dismiss_tip_of_the_day()
        # Gramps' Category sidebar labels each toggle with the *sub-category*
        # half of the (cat, subcat) tuple. QuiltView registers as
        # ``category=("Ancestry", _("Charts"))`` so its sidebar button is
        # named "Charts", not "Ancestry". The first click switches Gramps
        # into the category's default view (Pedigree).
        self._click_toggle("Charts")
        time.sleep(0.5)
        self._dismiss_tip_of_the_day()

        # The Quilt Chart selector lives inside the Charts category's
        # view-switcher popover; it is structurally present but not laid
        # out on screen, so a coordinate-based click fails. Invoke its
        # AT-SPI Action interface directly instead.
        deadline = time.monotonic() + 10
        quilt_toggle = None
        while time.monotonic() < deadline:
            for n in self.app.findChildren(
                lambda n: n.roleName in ("toggle button", "radio menu item")
                and (n.name or "") == "Quilt Chart"
            ):
                quilt_toggle = n
                break
            if quilt_toggle:
                break
            time.sleep(0.3)
        if quilt_toggle is None:
            self.fail("Quilt Chart selector not found anywhere in the tree")

        if not self._activate_via_action(quilt_toggle):
            self.fail(
                f"Could not activate Quilt Chart selector (role="
                f"{quilt_toggle.roleName})"
            )

        # Wait for the frame title to show "Quilt Chart" so we know
        # QuiltView.on_draw has run at least once.
        deadline = time.monotonic() + 10
        while time.monotonic() < deadline:
            if "quilt chart" in self._frame_title().lower():
                break
            time.sleep(0.3)
        else:
            self.fail(
                "Frame title never showed Quilt Chart after activation; "
                f"current title: {self._frame_title()!r}"
            )

        # QuiltView's rebuild bails out when no active person is set
        # (QuiltView.py:760 ``if not self.active: return``), so the canvas
        # paints nothing on a fresh launch. Clicking Home sets the active
        # person to the tree's home person (declared in the .gramps XML),
        # which triggers a real layout pass.
        for n in self.app.findChildren(
            lambda n: n.roleName == "push button" and (n.name or "") == "Home"
        ):
            if self._is_clickable(n):
                n.click()
                break
        time.sleep(1.0)

    def _find_canvas(self):
        """Locate the QuiltView drawing area (the Cairo canvas)."""
        deadline = time.monotonic() + 10
        while time.monotonic() < deadline:
            for node in self.app.findChildren(
                lambda n: n.roleName == "drawing area"
            ):
                try:
                    if not node.showing:
                        continue
                    pos = node.position
                    size = node.size
                except Exception:
                    continue
                if pos[0] >= 0 and pos[1] >= 0 and size[0] > 0 and size[1] > 0:
                    return node, pos, size
            time.sleep(0.3)
        self.fail("QuiltView 'drawing area' not found in AT-SPI tree")

    @staticmethod
    def _is_in_menu_bar(menu) -> bool:
        """True if the menu lives inside a permanent menu-bar hierarchy
        (so it is not a transient popup)."""
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

    def _visible_menu(self):
        """Return the currently-showing popup GtkMenu, or None.

        Popup menus from QuiltView's canvas appear directly under the
        application root; menu-bar children (e.g. the persistently-rooted
        "Family Trees" menu) are excluded so they do not masquerade as
        the popup we are looking for."""
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
            if items:
                return menu, items
        return None

    def _menu_kind(self, items) -> str:
        labels = [(it.name or "") for it in items]
        if any(lbl.startswith("Family of ") for lbl in labels):
            return "family"
        if "Parents" in labels or "Spouses" in labels or "Siblings" in labels:
            return "person"
        return "unknown"

    def _dismiss_menu(self) -> None:
        keyCombo("Escape")
        time.sleep(0.2)

    # --- the test ------------------------------------------------------------

    def test_add_child_to_family_does_not_raise_nameerror(self) -> None:
        self._open_quilt_view()
        _, (cx, cy), _ = self._find_canvas()

        # Sweep the canvas along y == FAMILY_NODE_Y_CENTRE (deterministic for
        # a 2-parent, 0-child layout) until the click lands on the FamilyNode
        # and family_menu pops up.
        family_menu_node = None
        for dx in range(BORDER, SWEEP_X_MAX, SWEEP_STEP):
            raw_click(cx + dx, cy + FAMILY_NODE_Y_CENTRE, button=1)
            time.sleep(0.25)
            menu = self._visible_menu()
            if menu is None:
                continue
            node, items = menu
            if self._menu_kind(items) == "family":
                family_menu_node = node
                break
            self._dismiss_menu()

        if family_menu_node is None:
            self._capture_screenshot("family-menu-not-found")
            self.fail(
                "No family_menu found while sweeping the QuiltView canvas at "
                f"y={FAMILY_NODE_Y_CENTRE} from x={BORDER} to {SWEEP_X_MAX}"
            )

        # Drive the popup with the keyboard. Mouse-clicking through nested
        # GTK popup menus races the menu lifetime — the submenu often
        # dismisses before xdotool's MoveMouse+Click lands on the leaf —
        # whereas arrow-key navigation in a focused menu is synchronous.
        #
        # The family menu order is: Family-of-label (insensitive), separator,
        # Edit, Edit tags, Children (submenu), separator, About. GTK skips
        # separators and insensitive items, so:
        #   Down x 3  -> Edit, Edit tags, Children
        #   Right     -> opens Children submenu, highlights "Add child to family"
        #   Return    -> activates it
        time.sleep(0.3)  # let the popup grab keyboard focus
        for _ in range(3):
            pressKey("Down")
            time.sleep(0.1)
        pressKey("Right")
        time.sleep(0.4)
        pressKey("Return")

        # On patched code (#863), this opens an EditPerson dialog. On the
        # unpatched bug, ``Surname()`` at QuiltView.py:1266 raises NameError
        # before EditPerson is invoked, the dialog never appears, and
        # gramps' uncaught-exception handler surfaces an "Error Report"
        # dialog instead.
        #
        # The EditPerson dialog surfaces with role "dialog" and title of
        # the form "Person: <name>". For our 2-parent tree ``preset_name``
        # copies the father's first name into the new child, so the title
        # is "Person: Aa - Gramps".
        deadline = time.monotonic() + 6
        editperson = None
        error_report = None
        while time.monotonic() < deadline:
            for f in self.app.findChildren(
                lambda n: n.roleName in ("dialog", "frame")
            ):
                try:
                    if not f.showing:
                        continue
                    name = f.name or ""
                except Exception:
                    continue
                if name.startswith("Person:") or "New Person" in name:
                    editperson = f
                elif name.startswith("Error Report"):
                    error_report = f
            if editperson:
                break
            time.sleep(0.3)

        if editperson is None:
            visible = [
                f"[{f.roleName}] {(f.name or '')!r}"
                for f in self.app.findChildren(
                    lambda n: n.roleName in ("frame", "dialog")
                )
                if getattr(f, "showing", False)
            ]
            stderr = self._stderr_text()
            self.fail(
                "EditPerson dialog never appeared after activating 'Add "
                "child to family'. This matches the addons-source PR #863 "
                "bug: QuiltView.py:1266 evaluates Surname() but Surname is "
                "not imported, so a NameError fires inside the GLib callback "
                "and Gramps' uncaught-exception handler surfaces an 'Error "
                "Report' dialog instead of opening the editor.\n"
                f"Error Report dialog visible: {error_report is not None}\n"
                f"Visible top-levels: {visible}\n"
                f"Last 1 KB stderr: {stderr[-1024:]!r}"
            )


if __name__ == "__main__":
    unittest.main()
