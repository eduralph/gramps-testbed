"""E2E regression for Mantis bug 12572 (CombinedView stale-view crash).

Mantis 12572: when a family tree is closed, the CombinedView addon's
``Relationships > Combined`` view does not refresh -- it keeps showing
people from the closed tree.  Each row's edit button still holds a handle
that no longer resolves, so clicking one calls ``db.get_person_from_handle``
with a dead handle and raises ``gramps.gen.errors.HandleError``.

Root cause (addons-source ``CombinedView/combinedview.py``)::

    def change_object(self, obj_tuple):
        if obj_tuple is None:
            return                  # <-- leaves the stale view on screen

Closing the tree makes ``dbstate`` emit ``database-changed`` (with a
``DummyDb``); ``change_db`` -> ``history.clear()`` -> ``redraw()`` ->
``change_object(None)`` -- and the early ``return`` above never clears
``self.header`` / ``self.stack``.  The stock RelationshipView does *not*
have this bug: its ``change_db`` clears ``vbox``/``header`` directly
(``gramps/plugins/view/relview.py``).

The bug is platform-independent.  The report was filed on Windows only
because that is what the reporter runs; the faulty code path is plain
Python control flow with no OS-specific component, so it reproduces on
this Linux AT-SPI harness.

The test opens the example tree, switches to the Combined view, populates
it with the home person (gramps_id I00044), closes the tree with Ctrl+W,
and clicks an edit button on the still-visible person.  On the unpatched
addon this raises ``HandleError``, which Gramps surfaces in an "Error
Report" window; the test fails until the ``change_object(None)`` path is
fixed to clear the display.
"""

from __future__ import annotations

import subprocess
import threading
import time
import unittest

from dogtail.rawinput import click as raw_click
from dogtail.rawinput import keyCombo

from .base import GrampsInterfaceTestCase

# Home person of example.gramps -- format-independent identifier (the
# Combined view title shows the gramps_id verbatim via BasicLabel).
HOME_GRAMPS_ID = "I00044"


class CombinedViewStaleCloseTest(GrampsInterfaceTestCase):
    """Regression for Mantis 12572 (and the non-refresh half, Mantis 14226).

    Drives the Combined view, closes the family tree, and edits a
    still-visible person.  On the unpatched addon ``change_object(None)``
    returns without clearing the view, so the stale edit button raises
    ``HandleError`` -- this test fails until that path clears the display.
    """

    TREE_NAME = "TestTree"

    # --- stderr capture (gramps is launched with PIPEs by base.py; an
    #     undrained pipe buffer would eventually block the process) --------

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
    def _stderr_text(cls) -> str:
        with cls._gramps_lock:
            return b"".join(cls._gramps_output["stderr"]).decode(
                "utf-8", errors="replace"
            )

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
        after startup and steals focus."""
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

    def _activate_via_action(self, node) -> bool:
        """Invoke the node's default AT-SPI Action -- works even when the
        node is not laid out on screen (inside a view-switcher popover)."""
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

    def _frame_title(self) -> str:
        """Title of the showing main Gramps frame, or ''."""
        for f in self.app.findChildren(lambda n: n.roleName == "frame"):
            try:
                if not f.showing:
                    continue
                name = f.name or ""
            except Exception:
                continue
            if "Gramps" in name and "Tip of the Day" not in name:
                return name
        return ""

    # --- Combined-view-specific helpers --------------------------------------

    def _open_combined_view(self) -> None:
        """Switch to the Relationships category, then to the Combined view."""
        self._dismiss_tip_of_the_day()
        # CombinedView registers category=("Relationships", _("Relationships"));
        # the category sidebar labels each toggle with the sub-category half,
        # so its button is named "Relationships".  This first click switches
        # Gramps into the category's default view (the stock Relationships
        # view) -- not yet the Combined view.
        self._click_toggle("Relationships")
        time.sleep(0.5)
        self._dismiss_tip_of_the_day()

        # The "Combined" view selector is a GtkToggleToolButton in the
        # category's view-switcher; it may be structurally present but not
        # laid out on screen, so invoke its AT-SPI Action directly (a
        # coordinate click would miss).
        deadline = time.monotonic() + 10
        selector = None
        while time.monotonic() < deadline:
            for n in self.app.findChildren(
                lambda n: n.roleName in ("toggle button", "radio menu item")
                and (n.name or "") == "Combined"
            ):
                selector = n
                break
            if selector:
                break
            time.sleep(0.3)
        if selector is None:
            self._capture_screenshot("combined-selector-not-found")
            self.fail("'Combined' view selector not found in the AT-SPI tree")

        if not self._activate_via_action(selector):
            self.fail(
                f"Could not activate 'Combined' view selector "
                f"(role={selector.roleName})"
            )

        deadline = time.monotonic() + 10
        while time.monotonic() < deadline:
            if "combined" in self._frame_title().lower():
                break
            time.sleep(0.3)
        else:
            self.fail(
                "Frame title never showed the Combined view after "
                f"activation; current title: {self._frame_title()!r}"
            )

    def _go_home(self) -> None:
        """Click the Home toolbar button so the view shows the tree's
        default person (example.gramps home person I00044)."""
        for n in self.app.findChildren(
            lambda n: n.roleName == "push button" and (n.name or "") == "Home"
        ):
            if self._is_clickable(n):
                n.click()
                break
        else:
            self.fail("Combined view 'Home' toolbar button not found")

    def _id_label_showing(self) -> bool:
        """True while a label carrying the home person's gramps_id is shown
        -- i.e. the Combined view title is populated with that person."""
        for n in self.app.findChildren(lambda n: n.roleName == "label"):
            try:
                if n.showing and HOME_GRAMPS_ID in (n.name or ""):
                    return True
            except Exception:
                continue
        return False

    def _content_buttons(self):
        """Showing, unnamed push buttons sorted (top, left).

        The Combined view's in-row controls are ``widgets.IconButton``
        (Gtk.Button + Gtk.Image, no label) -- they surface as push buttons
        with an empty accessible name.  Toolbar buttons all carry names and,
        once the tree is closed, are hidden by ``viewmanager.post_close_db``;
        the StackSwitcher buttons carry the stack-page names.  So an unnamed,
        showing push button is a CombinedView content control.  The topmost-
        leftmost one is the title's edit-person button (basepage.py
        ``edit_person_button``)."""
        found = []
        for b in self.app.findChildren(
            lambda n: n.roleName == "push button"
        ):
            try:
                if not b.showing or (b.name or "").strip():
                    continue
                pos = b.position
                size = b.size
            except Exception:
                continue
            if size[0] > 0 and size[1] > 0:
                found.append((pos[1], pos[0], b))
        found.sort(key=lambda t: (t[0], t[1]))
        return [t[2] for t in found]

    def _visible_toplevels(self) -> list[str]:
        """Sorted ``[role] name`` of every showing top-level window."""
        out = set()
        for f in self.app.findChildren(
            lambda n: n.roleName in ("frame", "dialog", "alert")
        ):
            try:
                if f.showing:
                    out.add(f"[{f.roleName}] {(f.name or '')!r}")
            except Exception:
                continue
        return sorted(out)

    @staticmethod
    def _raw_click_node(node) -> None:
        """Synthesise a real left mouse press at the node's centre.

        CombinedView's row controls are ``widgets.IconButton``, which bind
        their handler to ``button-press-event`` -- NOT ``clicked``.  dogtail's
        ``node.click()`` drives the AT-SPI action (the GTK ``clicked``
        signal), which IconButton ignores; a synthesised X button press is
        delivered by GTK as ``button-press-event`` and does fire the handler.
        """
        bx, by = node.position
        bw, bh = node.size
        raw_click(bx + bw // 2, by + bh // 2, button=1)

    def _error_report_dialog(self):
        """The Gramps 'Error Report' window if its uncaught-exception
        handler has surfaced one, else None."""
        for d in self.app.findChildren(
            lambda n: n.roleName in ("dialog", "frame")
        ):
            try:
                if d.showing and (d.name or "").startswith("Error Report"):
                    return d
            except Exception:
                continue
        return None

    @staticmethod
    def _collect_text(node) -> str:
        """Concatenate every 'text' descendant's content -- the Error
        Report assistant holds the traceback in a Gtk.TextView."""
        chunks = []
        for t in node.findChildren(lambda n: n.roleName == "text"):
            try:
                txt = t.text or ""
            except Exception:
                txt = ""
            if txt:
                chunks.append(txt)
        return "\n".join(chunks)

    # --- the test ------------------------------------------------------------

    def test_edit_in_stale_view_after_tree_close(self) -> None:
        self._open_combined_view()
        self._go_home()

        deadline = time.monotonic() + 10
        while time.monotonic() < deadline and not self._id_label_showing():
            time.sleep(0.3)
        self.assertTrue(
            self._id_label_showing(),
            f"Combined view never populated -- no label carrying "
            f"{HOME_GRAMPS_ID!r} appeared after clicking Home.",
        )
        before = self._content_buttons()
        self.assertTrue(before, "Combined view exposed no content buttons")

        # Control: confirm the input mechanism works while the tree is open.
        # Clicking the title edit button must open the EditPerson editor;
        # if it does not, raw_click is not reaching the button-press-event
        # handler and the reproduction below would be inconclusive.
        tops_before = self._visible_toplevels()
        self._raw_click_node(before[0])
        time.sleep(2.5)
        new_windows = [t for t in self._visible_toplevels() if t not in tops_before]
        keyCombo("Escape")  # dismiss whatever editor opened
        time.sleep(1.0)
        self.assertTrue(
            new_windows,
            "Control click failed: raw_click on the title IconButton opened "
            "no editor while the tree was open, so the input mechanism is "
            "not reaching the IconButton's button-press-event handler.",
        )

        stderr_mark = len(self._stderr_text())

        # Close the family tree: Ctrl+W -> viewmanager.close_database ->
        # dbstate.no_database() -> emits 'database-changed' with a DummyDb.
        keyCombo("<Control>w")

        deadline = time.monotonic() + 10
        while time.monotonic() < deadline:
            if "no family tree" in self._frame_title().lower():
                break
            time.sleep(0.3)
        else:
            self._capture_screenshot("tree-not-closed")
            self.fail(
                "Family tree did not close after Ctrl+W; frame title: "
                f"{self._frame_title()!r}"
            )
        time.sleep(1.5)  # let change_db -> redraw -> change_object(None) settle

        # On the fixed addon, change_object(None) has cleared header/stack:
        # the home person is gone and there is nothing dead to edit.
        if not self._id_label_showing():
            return

        # Stale view (the Mantis 14226 non-refresh half).  Editing a
        # still-visible person now reproduces the Mantis 12572 crash.
        after = self._content_buttons()
        self.assertTrue(
            after,
            "Combined view is stale (still shows the closed tree's home "
            "person) but no edit button was found to click.",
        )

        # Click the topmost stale buttons (title + family-row edit buttons)
        # until the crash surfaces.  A normal edit button opens an editor
        # window (the control above proved that); on the stale view it
        # instead raises HandleError, which Gramps' uncaught-exception
        # handler turns into an "Error Report" window.
        for btn in after[:6]:
            try:
                self._raw_click_node(btn)
            except Exception:
                continue
            time.sleep(1.5)
            if (
                self._error_report_dialog() is not None
                or "HandleError" in self._stderr_text()[stderr_mark:]
            ):
                break

        err_dialog = self._error_report_dialog()
        report_text = self._collect_text(err_dialog) if err_dialog else ""
        stderr_tail = self._stderr_text()[stderr_mark:]
        crashed = err_dialog is not None or "HandleError" in stderr_tail
        evidence = report_text or stderr_tail

        self.assertFalse(
            crashed,
            "Mantis 12572 reproduced: editing a person in the stale Combined "
            "view crashed -- Gramps surfaced an 'Error Report' for the "
            "uncaught exception.  change_object(None) returned without "
            "clearing header/stack, so the view still holds handles from the "
            "closed tree and get_person_from_handle() raised HandleError.\n"
            f"HandleError seen in report/stderr: {'HandleError' in evidence}\n"
            f"evidence tail:\n{evidence[-2000:]}",
        )


if __name__ == "__main__":
    unittest.main()
