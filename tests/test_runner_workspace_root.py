"""Regression test: runner wrappers must resolve the workspace root robustly.

The Option-C restructure (commit 5c7ba57) relocated the runner wrappers one
directory deeper (``scripts/`` -> ``agent-work/scripts/``) but the original
fixed-depth ``$0``-relative ancestor walk was not deepened, so every wrapper
resolved ``WORKSPACE`` one level too shallow -- the repo root instead of its
parent, where the sibling ``gramps/`` checkout lives. The fix resolves the
repo root via ``git rev-parse --show-toplevel``, which is independent of how
deeply the script is nested, so a future move cannot silently reintroduce the
off-by-one.

This guards both halves of "don't get the same fragility again":

* **behavioural** -- each script's actual ``TESTBED=``/``WORKSPACE=`` lines,
  evaluated from the script's real on-disk location and from an unrelated
  working directory, resolve to ``WORKSPACE == <repo>/..`` and (where the
  script defines it) ``TESTBED == <repo>``;
* **structural** -- no script reintroduces a fixed-depth ``../..`` ancestor
  walk (the brittle pattern that caused the bug); each obtains the repo root
  from the git top-level lookup.

The test is intentionally depth-agnostic: it asserts the resolved *result*,
not a particular number of ``..`` levels, so it stays correct (and keeps
guarding) no matter where the wrappers are moved next.
"""

# ------------------------
# Python modules
# ------------------------
import os
import re
import shutil
import subprocess
import unittest
from pathlib import Path

# tests/ sits at the repo root; its parent-of-parent holds the sibling clones.
REPO_ROOT = Path(__file__).resolve().parent.parent
WORKSPACE_ROOT = REPO_ROOT.parent

# Every runner wrapper under the two platform dirs. Kept explicit (rather than
# globbed) so a newly added runner that forgets the robust resolution shows up
# as a missing-file failure here, prompting the author to add it to the guard.
RUNNERS = (
    "agent-work/scripts/ubuntu/run-unit.sh",
    "agent-work/scripts/ubuntu/run-interface.sh",
    "agent-work/scripts/ubuntu/run-addon-unit.sh",
    "agent-work/scripts/ubuntu/clean-build.sh",
    "agent-work/scripts/ubuntu/rebuild-image.sh",
    "agent-work/scripts/ubuntu/run-manual.sh",
    "agent-work/scripts/windows/run-unit.sh",
    "agent-work/scripts/windows/run-addon-unit.sh",
)

# A TESTBED=/WORKSPACE= assignment at column 0 (the wrappers' shape).
_ASSIGN_RE = re.compile(r"^(TESTBED|WORKSPACE)=")
# Two or more chained parent hops -- the fixed-depth walk that broke. A single
# "$TESTBED/.." (repo-root -> its parent) is fine and must not trip this.
_FIXED_DEPTH_WALK_RE = re.compile(r"\.\./\.\.")


def _resolution_lines(script: Path) -> list[str]:
    """Return the script's ``TESTBED=``/``WORKSPACE=`` assignment lines."""
    return [ln for ln in script.read_text().splitlines() if _ASSIGN_RE.match(ln)]


# ------------------------------------------------------------
#
# RunnerWorkspaceRootTest
#
# ------------------------------------------------------------
class RunnerWorkspaceRootTest(unittest.TestCase):
    """Each runner resolves its roots correctly and depth-independently."""

    def test_all_runners_present(self) -> None:
        """Every listed wrapper exists (catches a renamed/removed runner)."""
        for rel in RUNNERS:
            with self.subTest(runner=rel):
                self.assertTrue(
                    (REPO_ROOT / rel).is_file(),
                    f"{rel} is missing -- update RUNNERS (and the guard) if it moved",
                )

    def test_resolution_is_git_based_not_fixed_depth(self) -> None:
        """Structural guard: git top-level lookup, never a chained ../.. walk."""
        for rel in RUNNERS:
            script = REPO_ROOT / rel
            lines = _resolution_lines(script)
            with self.subTest(runner=rel):
                self.assertTrue(
                    lines, f"{rel}: no TESTBED=/WORKSPACE= assignment found"
                )
                block = "\n".join(lines)
                self.assertIn(
                    "rev-parse --show-toplevel",
                    block,
                    f"{rel}: repo root must come from `git rev-parse --show-toplevel`",
                )
                self.assertIsNone(
                    _FIXED_DEPTH_WALK_RE.search(block),
                    f"{rel}: reintroduced a fixed-depth `../..` walk -- this is the "
                    f"exact fragility the fix removed; resolve via git top-level instead",
                )

    @unittest.skipUnless(
        shutil.which("bash") and shutil.which("git"),
        "bash and git are required to evaluate the resolution",
    )
    def test_resolution_yields_correct_roots(self) -> None:
        """Behavioural guard: evaluate the real lines, assert the resolved roots.

        Run from an unrelated working directory and feed the script's true path
        in for ``${BASH_SOURCE[0]}`` -- so this exercises the script's actual
        resolution logic (git top-level + parent), independent of both the
        caller's CWD and the script's nesting depth.
        """
        want_workspace = os.path.realpath(WORKSPACE_ROOT)
        want_testbed = os.path.realpath(REPO_ROOT)
        for rel in RUNNERS:
            script = REPO_ROOT / rel
            block = "\n".join(_resolution_lines(script)).replace(
                '"${BASH_SOURCE[0]}"', f'"{script}"'
            )
            program = (
                "set -euo pipefail\n"
                f"{block}\n"
                'printf "%s\\n%s\\n" "${TESTBED:-}" "${WORKSPACE:-}"'
            )
            with self.subTest(runner=rel):
                result = subprocess.run(
                    ["bash", "-c", program],
                    cwd=os.environ.get("TMPDIR", "/tmp"),
                    capture_output=True,
                    text=True,
                )
                self.assertEqual(
                    result.returncode,
                    0,
                    f"{rel}: resolution failed:\n{result.stderr}",
                )
                testbed, workspace = (result.stdout.splitlines() + ["", ""])[:2]
                self.assertEqual(
                    os.path.realpath(workspace),
                    want_workspace,
                    f"{rel}: WORKSPACE resolved to {workspace!r}, expected the repo "
                    f"parent (holding the sibling gramps/ checkout)",
                )
                if testbed:  # only the TESTBED-defining wrappers set it
                    self.assertEqual(
                        os.path.realpath(testbed),
                        want_testbed,
                        f"{rel}: TESTBED resolved to {testbed!r}, expected the repo root",
                    )


if __name__ == "__main__":
    unittest.main()
