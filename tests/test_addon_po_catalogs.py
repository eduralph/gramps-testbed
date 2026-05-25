"""Every addon translation catalog must compile with msgfmt.

``make.py build <addon>`` runs ``msgfmt`` on each ``<addon>/po/*.po`` to
produce the ``.mo`` files bundled into the addon tarball. A catalog that
msgfmt rejects aborts the build — exactly what happened in Mantis bug
14234, where four lxml ``ngettext()`` calls left the singular and plural
forms disagreeing on a trailing newline (gettext requires a ``msgid`` and
its ``msgid_plural`` to both end with ``\\n`` or neither), so ``msgfmt``
failed fatally on every translated lxml catalog.

addons-source has no unit-test CI of its own, so this testbed check is
the only automated guard against a ``.po`` regression that breaks
``make.py build``. msgfmt is invoked plain — no ``--check`` — so the test
mirrors what the build actually does and stays green on the format-string
nits that ``--check`` would flag in third-party translations.
"""

from __future__ import annotations

import os
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path


def _find_addons_source() -> Path | None:
    """Locate the addons-source checkout.

    Honours ``$ADDONS_SOURCE`` / ``$ADDONS_SOURCE_DIR``; otherwise falls
    back to the sibling-of-the-testbed layout this repo's scripts assume
    (``../addons-source`` next to ``gramps-testbed/``).
    """
    for var in ("ADDONS_SOURCE", "ADDONS_SOURCE_DIR"):
        val = os.environ.get(var)
        if val and Path(val).is_dir():
            return Path(val).resolve()
    sibling = Path(__file__).resolve().parents[2] / "addons-source"
    return sibling if sibling.is_dir() else None


ADDONS_SOURCE = _find_addons_source()
MSGFMT = shutil.which("msgfmt")


@unittest.skipUnless(MSGFMT, "msgfmt (gettext) is not installed")
@unittest.skipUnless(ADDONS_SOURCE, "addons-source checkout not found")
class AddonPoCatalogTest(unittest.TestCase):
    """msgfmt must accept every ``<addon>/po/*.po`` catalog."""

    def test_all_addon_catalogs_compile(self) -> None:
        catalogs = sorted(ADDONS_SOURCE.glob("*/po/*.po"))
        self.assertTrue(
            catalogs, f"no addon .po catalogs found under {ADDONS_SOURCE}"
        )
        with tempfile.TemporaryDirectory() as tmp:
            mo = os.path.join(tmp, "addon.mo")
            for po in catalogs:
                rel = po.relative_to(ADDONS_SOURCE)
                with self.subTest(catalog=str(rel)):
                    result = subprocess.run(
                        [MSGFMT, str(po), "-o", mo],
                        capture_output=True,
                        text=True,
                    )
                    self.assertEqual(
                        result.returncode,
                        0,
                        f"msgfmt rejected {rel}:\n{result.stderr.strip()}",
                    )


if __name__ == "__main__":
    unittest.main()
