"""Regression test: docker-build.yml must watch the Dockerfile's COPY sources.

``docker/Dockerfile.ubuntu`` builds the image from repo-context sources it
``COPY``s in (e.g. ``agent-work/scripts/lib/addon_system_deps.py``, which
drives the image's apt package set). But ``.github/workflows/docker-build.yml``
path-filters its ``push`` and ``pull_request`` triggers, so unless every such
source is listed in those filters, a change that breaks the build does **not**
run the build-validation workflow on the PR that makes it -- the break first
surfaces in the nightly ``schedule`` run, post-merge.

This happened once already: the ``agent-work/`` move repointed the ``COPY``
into ``agent-work/`` but left the path filter watching only the Dockerfile, so
the two silently drifted apart. This test ties them back together: every
repo-relative ``COPY``/``ADD`` source in the Dockerfile must appear in **both**
the ``push.paths`` and ``pull_request.paths`` lists, so they cannot drift again.

Out of scope by design: sources that are not repo-relative build context
(``--from=`` stage copies, absolute container paths, URLs) -- those are not
files in this repo and cannot be path-filtered on.
"""

# ------------------------
# Python modules
# ------------------------
import re
import unittest
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover - exercised only where PyYAML is absent
    yaml = None

REPO_ROOT = Path(__file__).resolve().parent.parent
DOCKERFILE = REPO_ROOT / "docker" / "Dockerfile.ubuntu"
WORKFLOW = REPO_ROOT / ".github" / "workflows" / "docker-build.yml"


def _copy_add_sources(dockerfile: Path) -> list[str]:
    """Return the repo-relative ``COPY``/``ADD`` source paths in the Dockerfile.

    Skips sources that cannot be path-filtered: ``--from=`` build-stage copies,
    absolute container paths, and URLs. Honours line continuations.
    """
    text = dockerfile.read_text()
    text = re.sub(r"\\\n", " ", text)  # join continued lines
    sources: list[str] = []
    for line in text.splitlines():
        m = re.match(r"\s*(COPY|ADD)\s+(.*)", line)
        if not m:
            continue
        args = m.group(2).split()
        # Drop flags (--from=..., --chown=..., --chmod=...); the last token is
        # the destination, everything before it is a source.
        args = [a for a in args if not a.startswith("--")]
        if "--from" in m.group(2):
            continue  # copies from another build stage, not repo context
        for src in args[:-1]:
            if src.startswith(("/", "http://", "https://")):
                continue
            sources.append(src)
    return sources


def _trigger_paths(workflow: Path, event: str) -> list[str]:
    """Return the ``paths:`` list for ``on.<event>`` in the workflow."""
    data = yaml.safe_load(workflow.read_text())
    # PyYAML parses the bare ``on:`` key as the boolean True (YAML 1.1).
    on = data.get("on", data.get(True))
    return list((on or {}).get(event, {}).get("paths", []))


# ------------------------------------------------------------
#
# DockerBuildPathFilterTest
#
# ------------------------------------------------------------
@unittest.skipUnless(yaml is not None, "PyYAML is required to parse the workflow")
class DockerBuildPathFilterTest(unittest.TestCase):
    """The build workflow must trigger on every Dockerfile COPY source."""

    def test_dockerfile_has_repo_context_sources(self) -> None:
        """Sanity: the Dockerfile COPYs at least one repo-relative source.

        Guards the guard -- if parsing silently found nothing, the coverage
        assertions below would pass vacuously.
        """
        self.assertTrue(
            _copy_add_sources(DOCKERFILE),
            "no repo-relative COPY/ADD source parsed from the Dockerfile",
        )

    def test_copy_sources_covered_by_push_and_pr_filters(self) -> None:
        """Every COPY source is in both the push and pull_request path filters."""
        sources = set(_copy_add_sources(DOCKERFILE))
        for event in ("push", "pull_request"):
            paths = set(_trigger_paths(WORKFLOW, event))
            with self.subTest(event=event):
                missing = sources - paths
                self.assertFalse(
                    missing,
                    f"docker-build.yml `on.{event}.paths` does not watch Dockerfile "
                    f"COPY source(s) {sorted(missing)} -- a change to them would not "
                    f"trigger build validation on its PR. Add them to the filter.",
                )

    def test_dockerfile_itself_still_watched(self) -> None:
        """The Dockerfile path stays in both filters (don't regress the baseline)."""
        rel = "docker/Dockerfile.ubuntu"
        for event in ("push", "pull_request"):
            with self.subTest(event=event):
                self.assertIn(rel, _trigger_paths(WORKFLOW, event))


if __name__ == "__main__":
    unittest.main()
