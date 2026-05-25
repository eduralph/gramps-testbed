"""Regression for Mantis #14100 ("[detancestralreport] Fail to make text
report [ KeyError: 'noin' ]").

Reported in 2026 against Gramps 6.0.6 AIO on Windows, Finnish locale.

Root cause
----------
``DateDisplay.format_long_month_year`` and its short/month-only siblings
looked up the modifier-derived ``inflect`` key in ``FORMATS_long_month_year``
/ ``FORMATS_short_month_year`` with a bare subscript. ``display_formatted``
derives that key from a translatable string (``_("", "about-date")`` and
friends), which the source comments ask translators to leave untranslated
or render as the English keyword the dicts are keyed by ("about"). The
Finnish ``fi.po`` instead translates "about-date" to the native word
"noin", so displaying an "about <Month> <Year>" date under a long-month
format raised ``KeyError: 'noin'``.

The ticket's traceback is the Detailed Ancestral Report, but the same
unguarded ``get_date()`` / ``displayer.display()`` call is reached by
``gramps/plugins/view/relview.py`` when it paints a person's birth date,
so simply viewing such a person in the Relationship View crashes too.
Fixed upstream by the gramps-project/gramps commit "Fall back to
uninflected date format on an unknown inflection".

Reproduction (mirrors the reporter's confirmed Windows steps)
-------------------------------------------------------------
  * ``Bug14100Tree`` -- a one-person tree whose home person's Birth event
    is dated "about January 1652" (data/bug_0014100_minimal.gramps).
  * Gramps launched with ``LANGUAGE=fi`` and ``preferences.date-format=2``
    (the Finnish long-month format, "Päivä Kuukausi Vuosi").
  * Navigate to the Relationship View -- it paints the home person.

Assertion: the birth year "1652" becomes visible in the view. With the
fix the date degrades to the uninflected form ("noin tammikuu 1652") and
renders; without it ``displayer.display()`` raises and the date never
paints.

The test *skips* (rather than false-passing) if Gramps did not actually
come up in Finnish -- in English the inflection key is valid and the bug
cannot occur.

On a pre-fix Gramps the bug actually fires earlier than the navigate-to-
relview step originally targeted: rendering the about-1652 person on the
tree-open path itself raises, so ``gramps -O Bug14100Tree`` lands on the
"Ei sukupuuta ladattuna" / "No Family Tree loaded" main window and the
test cannot navigate at all. The class opts out of the required-tree
launch (``TREE_REQUIRED = False`` in ``GrampsInterfaceTestCase``) and
reports that case as a clean test failure naming the upstream fix
(gramps-project/gramps#2322) instead of letting setUpClass time out.
"""

from __future__ import annotations

import time
import unittest

from .base import GrampsInterfaceTestCase

# Finnish display name of the "Relationships" category (po/fi.po:
# msgid "Relationships" -> msgstr "Suhteet"). Seeing this as a sidebar
# toggle is also our proof that the fi locale actually loaded.
RELATIONSHIPS_FI = "Suhteet"
RELATIONSHIPS_EN = "Relationships"

# The home person's Birth event in Bug14100Tree is "about January 1652".
# The year is locale-invariant, so it is a safe content probe.
BIRTH_YEAR = "1652"


class Bug14100RelviewInflectionKeyErrorTest(GrampsInterfaceTestCase):
    """Viewing an "about <Month> <Year>" date in the Relationship View
    under the Finnish long-month format must not raise KeyError."""

    TREE_NAME = "Bug14100Tree"
    # Finnish UI so the date displayer is DateDisplayFI and the modifier
    # maps through the (mis)translated "about-date" inflection context.
    LAUNCH_ENV = {"LANGUAGE": "fi"}
    # Date format index 2 == "Päivä Kuukausi Vuosi" (long month name);
    # the default ISO format never reaches the inflection code path.
    LAUNCH_CONFIG = ("preferences.date-format:2",)
    # Pre-fix Gramps crashes during ``gramps -O Bug14100Tree`` itself --
    # rendering the home person's "about January 1652" birth on the
    # tree-open path raises ``KeyError: 'noin'`` from
    # ``DateDisplay.format_long_month_year``, and the launch lands on
    # "No Family Tree loaded" instead. Opt out of the required-tree
    # launch so ``base.setUpClass`` returns with ``tree_opened = False``
    # and the test method can fail cleanly with a pointer to PR 2322.
    TREE_REQUIRED = False

    def _find_category_toggle(self, name: str, timeout: float = 10.0):
        """Return a showing sidebar ``toggle button`` with the given name,
        or None if none appears within ``timeout`` seconds."""
        deadline = time.monotonic() + timeout
        while time.monotonic() < deadline:
            for n in self.app.findChildren(
                lambda n, _n=name: n.roleName == "toggle button"
                and (n.name or "") == _n
            ):
                try:
                    if n.showing:
                        return n
                except Exception:
                    pass
            time.sleep(0.3)
        return None

    def _showing_text_contains(self, needle: str) -> bool:
        """True if any showing label/text node embeds ``needle``."""
        for n in self.app.findChildren(
            lambda n: n.roleName in ("label", "text")
        ):
            try:
                if not n.showing:
                    continue
                blob = (n.name or "") + " " + (n.text or "")
            except Exception:
                continue
            if needle in blob:
                return True
        return False

    def test_relationship_view_renders_about_date_without_crash(self) -> None:
        # Pre-fix Gramps crashes inside ``gramps -O Bug14100Tree`` itself
        # (rendering the "about January 1652" home person at tree-open
        # raises KeyError: 'noin' from format_long_month_year), so the
        # launch lands on "Ei sukupuuta ladattuna" / "No Family Tree
        # loaded" and never opens the tree. base.setUpClass tolerates
        # this when TREE_REQUIRED = False, records cls.tree_opened and
        # returns -- report the bug cleanly here with a pointer to the
        # upstream fix instead of letting setUpClass time out.
        if not self.tree_opened:
            self._capture_screenshot("bug-14100-tree-did-not-open")
            self.fail(
                "Mantis bug 14100 reproduced: gramps could not open "
                f"{self.TREE_NAME!r} -- the launch finished at the "
                '"No Family Tree loaded" main window. With LANGUAGE=fi + '
                "preferences.date-format=2, rendering the home person's "
                '"about January 1652" birth raises KeyError: \'noin\' from '
                "DateDisplay.format_long_month_year, which kills the "
                "tree-open path. Fixed upstream by gramps-project/gramps"
                '#2322 (the .get(inflect, FORMATS[""]) fallback in '
                "_datedisplay.py)."
            )

        # The category is "Suhteet" only if the fi locale loaded. In
        # English the inflection key is valid and the bug cannot occur,
        # so a non-Finnish run must skip rather than pass vacuously.
        toggle = self._find_category_toggle(RELATIONSHIPS_FI)
        if toggle is None:
            if self._find_category_toggle(RELATIONSHIPS_EN, timeout=2.0):
                self.skipTest(
                    "Gramps did not start in Finnish (the Relationships "
                    "category is shown in English). The 'noin' inflection "
                    "key only arises under the fi locale, so bug 14100 "
                    "cannot be exercised. Check that the fi translation is "
                    "compiled and LANGUAGE=fi reached the gramps process."
                )
            self._capture_screenshot("no-relationships-toggle")
            self.fail(
                "Neither the Finnish ('Suhteet') nor the English "
                "('Relationships') category toggle appeared in the sidebar "
                "within 10s -- cannot drive the Relationship View."
            )

        # Switching to the Relationship View paints the active (home)
        # person, whose "about January 1652" birth event is formatted via
        # displayer.display() -- the unguarded call bug 14100 crashes in.
        toggle.click()
        time.sleep(1.0)

        deadline = time.monotonic() + 12.0
        while time.monotonic() < deadline:
            if self._showing_text_contains(BIRTH_YEAR):
                return  # date painted -> displayer.display() did not raise
            time.sleep(0.4)

        self._capture_screenshot("relview-about-date-not-rendered")
        self.fail(
            "The Relationship View never displayed the home person's birth "
            f"year {BIRTH_YEAR!r}. Under the Finnish long-month date format "
            "an 'about January 1652' date reaches displayer.display(); "
            "bug 14100 makes that raise KeyError: 'noin', so the birth date "
            "never paints. Fixed upstream by the _datedisplay.py inflection "
            "fallback (commit 'Fall back to uninflected date format on an "
            "unknown inflection')."
        )


if __name__ == "__main__":
    unittest.main()
