"""Diagnostic test for Mantis #2092 ("Problems when no database is open").

This is *not* a regression test in the assertion sense — it runs the
reproduction protocol from ``work/2092-reproduction-protocol.md`` and emits
a structured per-gramplet baseline-vs-post-close comparison as test
output. The expected workflow is:

  1. Run this test once on ``maintenance/gramps60`` head.
  2. Capture the printed comparison block.
  3. Paste into the "Observed" column of the protocol file.
  4. File a focused Mantis split per surviving symptom; close #2092 as
     superseded.
  5. Once the splits are filed and each split has its own focused
     regression test in this same suite, retire this diagnostic test.

The test deliberately asserts nothing about gramplet behaviour — it
will pass whether the symptoms are present or not. The point is to
record the current state so we know which kulath-2020 items are still
alive in 6.0.

References:
  - Mantis #2092 itself (umbrella)
  - kulath's note ~0060977 (the enumeration this protocol verifies)
  - work/2092-reproduction-protocol.md (the static-read companion)

Status: skeleton. Each component on kulath's list is documented below
as a separate ``_capture_*`` helper; the helpers that aren't yet
implemented just record "not implemented" so the diagnostic output is
self-describing about its own coverage.
"""

from __future__ import annotations

import time
import unittest
from typing import Callable

from .base import GrampsInterfaceTestCase


# kulath's 2020-09-23 list. Order preserved; each entry maps the
# reporter's display name to (a) the sidebar category we have to land
# on to make the gramplet populate, and (b) a capture helper name.
# Helpers that aren't yet written record a "skip: helper not implemented"
# observation so the protocol output is complete.
KULATH_COMPONENTS: list[tuple[str, str, str]] = [
    # (kulath name, category to navigate to, capture helper name)
    ("Top Surnames (Dashboard)", "Dashboard", "_capture_text_gramplet"),
    ("Statistics", "Dashboard", "_capture_text_gramplet"),
    ("Given Name Cloud", "Dashboard", "_capture_text_gramplet"),
    ("Details (People)", "People", "_capture_details_gramplet"),
    ("Details (Relationships)", "Relationships", "_capture_details_gramplet"),
    ("Children (Family)", "Families", "_capture_tree_gramplet"),
    ("Details (Charts)", "Charts", "_capture_details_gramplet"),
    ("References (Events)", "Events", "_capture_backlinks_gramplet"),
    ("Details (Places)", "Places", "_capture_details_gramplet"),
    ("Geography", "Geography", "_capture_geography_view"),
    ("References (Sources)", "Sources", "_capture_backlinks_gramplet"),
    ("References (Citations)", "Citations", "_capture_backlinks_gramplet"),
    ("Details (Repositories)", "Repositories", "_capture_details_gramplet"),
    ("Media Preview (Media)", "Media", "_capture_media_preview"),
]


class Bug2092NoDbStateDiagnostic(GrampsInterfaceTestCase):
    """One-shot diagnostic: walk kulath's list, close the tree, walk again."""

    TREE_NAME = "TestTree"
    # Same window-size override as the #8594 test — gramps defaults to
    # 775×500, which under Xvfb (no window manager) leaves bottombar
    # gramplets clipped. 1800×1000 gives every gramplet space to paint.
    LAUNCH_CONFIG = (
        "interface.main-window-width:1800",
        "interface.main-window-height:1000",
    )

    # ------------------------------------------------------------------
    # Capture helpers — one per gramplet class. Each takes the category
    # name (to be navigated to first) and returns a string snapshot of
    # the gramplet's user-visible state, or None if the gramplet is not
    # found / not implemented.
    # ------------------------------------------------------------------

    def _navigate_to_category(self, name: str) -> bool:
        """Click the sidebar toggle for the named category. Returns True
        on success, False if the category isn't found within 5s."""
        deadline = time.monotonic() + 5
        while time.monotonic() < deadline:
            for n in self.app.findChildren(
                lambda n, _n=name: n.roleName == "toggle button"
                and (n.name or "") == _n
            ):
                try:
                    if n.showing:
                        n.click()
                        time.sleep(0.5)  # let the view paint
                        return True
                except Exception:
                    pass
            time.sleep(0.3)
        return False

    # Phase label set by the test method ("before"/"after"); used to
    # name screenshots so baseline and post-close grabs of the same
    # category land in different files.
    _phase: str = "before"

    def _screenshot_category(self, category: str) -> None:
        """X-screen screenshot of the current view, saved to
        artifacts/screenshots/2092-<phase>-<category>.png. Best effort
        — never blocks the test if Gdk pixbuf save fails."""
        try:
            import gi
            gi.require_version("Gdk", "3.0")
            from gi.repository import Gdk
            import os
            # ARTIFACTS_DIR is set by both CI and the local Docker runner;
            # falling back to "artifacts" mirrors base.py:SCREENSHOT_DIR.
            # A previous hard-coded "/workspace/..." path worked only
            # inside the Docker container and failed in CI with
            # PermissionError(13).
            outdir = os.path.join(
                os.environ.get("ARTIFACTS_DIR", "artifacts"),
                "screenshots",
            )
            os.makedirs(outdir, exist_ok=True)
            root = Gdk.get_default_root_window()
            w, h = root.get_width(), root.get_height()
            pb = Gdk.pixbuf_get_from_window(root, 0, 0, w, h)
            safe_cat = category.replace(" ", "-").replace("/", "_")
            path = f"{outdir}/2092-{self._phase}-{safe_cat}.png"
            pb.savev(path, "png", [], [])
        except Exception as exc:
            print(f"  screenshot for {category!r} failed: {exc!r}")

    def _capture_text_gramplet(self, category: str) -> str | None:
        """Generic capture for TextView-based gramplets (Top Surnames,
        Statistics, Given Name Cloud). Returns the text content or a
        short marker."""
        if not self._navigate_to_category(category):
            return f"NAV_FAILED:{category}"
        self._screenshot_category(category)
        # Look for a text widget showing non-trivial content. This is
        # intentionally broad — multiple gramplets on the same page will
        # each match; the per-gramplet refinement is a follow-up.
        for n in self.app.findChildren(
            lambda n: n.roleName in ("text", "label") and n.showing
        ):
            try:
                text = n.text or ""
            except Exception:
                continue
            if len(text) > 20:
                return text[:200]
        return "NO_TEXT_FOUND"

    def _capture_details_gramplet(self, category: str) -> str | None:
        if not self._navigate_to_category(category):
            return f"NAV_FAILED:{category}"
        self._screenshot_category(category)
        # Person/Place/Repository Details and Children all show a
        # composite label + grid; the exact AT-SPI shape depends on
        # whether the bottombar has the gramplet docked. Mark as
        # unimplemented for now so the diagnostic output is honest.
        return "SKIP:helper not implemented (per-gramplet refinement needed)"

    def _capture_tree_gramplet(self, category: str) -> str | None:
        if not self._navigate_to_category(category):
            return f"NAV_FAILED:{category}"
        self._screenshot_category(category)
        # Children gramplet is a GtkTreeView; capture row count.
        for tv in self.app.findChildren(
            lambda n: n.roleName == "tree table" and n.showing
        ):
            try:
                row_count = len(tv.children)
            except Exception:
                continue
            return f"tree:{row_count} rows"
        return "NO_TREE_FOUND"

    def _capture_backlinks_gramplet(self, category: str) -> str | None:
        """References gramplet — also a tree table, but with a known
        interaction-crash hazard. Capture row count first; the
        double-click probe is a separate helper invoked only in
        post-close."""
        return self._capture_tree_gramplet(category)

    def _capture_media_preview(self, category: str) -> str | None:
        if not self._navigate_to_category(category):
            return f"NAV_FAILED:{category}"
        self._screenshot_category(category)
        # Media Preview shows a Gtk.Image; AT-SPI surfaces it as an
        # "image" role with a description. Pre/post comparison of the
        # image description is enough for diagnostic purposes.
        for n in self.app.findChildren(
            lambda n: n.roleName == "image" and n.showing
        ):
            try:
                desc = n.description or ""
            except Exception:
                continue
            if desc:
                return f"image:{desc[:80]}"
        return "NO_IMAGE_FOUND"

    def _capture_geography_view(self, category: str) -> str | None:
        if not self._navigate_to_category(category):
            return f"NAV_FAILED:{category}"
        return "SKIP:helper not implemented (Geography view audit pending)"

    # ------------------------------------------------------------------
    # Close-tree action.
    # ------------------------------------------------------------------

    def _close_tree(self) -> bool:
        """Find Family Trees menu → Close, invoke it, return True on
        success."""
        # Surface the Family Trees menu in the menu bar. AT-SPI strips
        # the leading underscore accel marker so the actual name is
        # "Family Trees", not "_Family Trees" — accept both for safety.
        for menu in self.app.findChildren(
            lambda n: n.roleName == "menu"
            and (n.name or "") in ("Family Trees", "_Family Trees")
        ):
            try:
                menu.click()
                time.sleep(0.3)
            except Exception:
                continue
            # The "Close" item lives under Family Trees on a tree being open.
            for item in self.app.findChildren(
                lambda n: n.roleName == "menu item" and (n.name or "") in ("_Close", "Close")
            ):
                try:
                    if item.showing:
                        item.click()
                        time.sleep(1.0)  # let the close propagate
                        return True
                except Exception:
                    continue
        return False

    # ------------------------------------------------------------------
    # The diagnostic.
    # ------------------------------------------------------------------

    def test_record_pre_and_post_close_state(self) -> None:
        """Walk each kulath component, close the tree, walk again. Emit
        the comparison as test output for the protocol file."""
        baseline: dict[str, str | None] = {}
        type(self)._phase = "before"
        for name, category, helper_name in KULATH_COMPONENTS:
            helper: Callable[[str], str | None] = getattr(self, helper_name)
            baseline[name] = helper(category)

        closed = self._close_tree()
        if not closed:
            self.skipTest(
                "Could not invoke Family Trees → Close from the menu bar. "
                "Either the AT-SPI labels have changed or no tree is open. "
                "Fill in the protocol manually."
            )

        post: dict[str, str | None] = {}
        type(self)._phase = "after"
        for name, category, helper_name in KULATH_COMPONENTS:
            helper = getattr(self, helper_name)
            post[name] = helper(category)

        # Emit the comparison block. The intent is for whoever runs this
        # diagnostic (locally or in CI) to copy these lines into the
        # "Observed" column of work/2092-reproduction-protocol.md.
        print("\n" + "=" * 72)
        print("BUG 2092 DIAGNOSTIC — per-component baseline vs post-close")
        print("=" * 72)
        print(f"{'Component':35} | {'Baseline':30} | Post-close")
        print("-" * 100)
        for name, _category, _ in KULATH_COMPONENTS:
            b = (baseline[name] or "<None>")[:30]
            p = (post[name] or "<None>")[:30]
            verdict = "cleared" if (b != p and "NO_" not in p) else "?"
            if b == p and b not in ("<None>", "NAV_FAILED:", "NO_TREE_FOUND"):
                verdict = "stale-display"
            print(f"{name:35} | {b:30} | {p:30} -> {verdict}")
        print("=" * 72)


if __name__ == "__main__":
    unittest.main()
