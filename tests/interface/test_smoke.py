"""Smoke test: Gramps launches, opens the seeded tree, People view has rows.

If this test fails, nothing else in the interface suite will work. Fix it
before adding more tests.
"""

from __future__ import annotations

import unittest

from .base import GrampsInterfaceTestCase


class SmokeTest(GrampsInterfaceTestCase):
    def test_main_window_present(self) -> None:
        frames = self.app.findChildren(lambda n: n.roleName == "frame")
        self.assertTrue(frames, "No top-level Gramps frame in AT-SPI tree")

    def test_people_view_has_rows(self) -> None:
        tab = self.app.child(name="People", roleName="page tab")
        tab.click()
        tree = self.app.child(roleName="tree table")
        self.assertGreater(
            len(tree.children), 0,
            "People view is empty; example tree failed to load",
        )


if __name__ == "__main__":
    unittest.main()
