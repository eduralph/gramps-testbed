#!/usr/bin/env python3
"""Unit tests for the media-upload path in wikitransport + publish.

No browser, no network -- the WikiSession's per-method API surface is
small enough to mock directly. We pin the decision logic (SKIP / CREATE
/ UPDATE) and the publish-side iteration (which files get tried, in
what order, how failures are surfaced).
"""

import hashlib
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import publish as P
import wikitransport as WT
import md2wiki


# ------------------------------------------------------------
# Sha1File
# ------------------------------------------------------------
class Sha1File(unittest.TestCase):
    def test_matches_hashlib_for_small_file(self):
        with tempfile.NamedTemporaryFile(delete=False) as f:
            f.write(b"hello world\n")
            path = Path(f.name)
        try:
            expected = hashlib.sha1(b"hello world\n").hexdigest()
            self.assertEqual(WT.sha1_file(path), expected)
        finally:
            path.unlink()

    def test_chunked_read_handles_large_file(self):
        # 200 KB -- larger than the 64 KB chunk so we exercise the loop.
        payload = b"x" * (200 * 1024)
        with tempfile.NamedTemporaryFile(delete=False) as f:
            f.write(payload)
            path = Path(f.name)
        try:
            self.assertEqual(WT.sha1_file(path), hashlib.sha1(payload).hexdigest())
        finally:
            path.unlink()


# ------------------------------------------------------------
# GuessMime
# ------------------------------------------------------------
class GuessMime(unittest.TestCase):
    def test_svg_is_image_svg_xml(self):
        # SVG isn't always in the system mimetypes DB; we hard-code it.
        self.assertEqual(WT._guess_mime(Path("foo.svg")), "image/svg+xml")

    def test_png(self):
        self.assertEqual(WT._guess_mime(Path("foo.png")), "image/png")

    def test_pdf(self):
        self.assertEqual(WT._guess_mime(Path("foo.pdf")), "application/pdf")

    def test_unknown_extension_falls_back(self):
        # Not asserting the exact fallback, just that we get a string and
        # never raise.
        result = WT._guess_mime(Path("foo.weirdo"))
        self.assertIsInstance(result, str)
        self.assertTrue(result)


# ------------------------------------------------------------
# UploadIfChangedDecisionMatrix
# ------------------------------------------------------------
class UploadIfChangedDecisionMatrix(unittest.TestCase):
    """Drive WikiSession.upload_if_changed with a mocked file_info + upload.

    The three branches (SKIP / CREATE / UPDATE) are pinned because misclassifying
    them silently overwrites or refuses to overwrite -- both wrong.
    """

    def setUp(self):
        # Real-ish bytes; the SHA-1 is computed from these so we can pretend
        # the wiki has them or doesn't.
        self.payload = b"<svg>...</svg>"
        self.sha1 = hashlib.sha1(self.payload).hexdigest()
        f = tempfile.NamedTemporaryFile(suffix=".svg", delete=False)
        f.write(self.payload)
        f.close()
        self.path = Path(f.name)

    def tearDown(self):
        self.path.unlink(missing_ok=True)

    def _session(self, *, file_info, upload):
        """Build a WikiSession-like object with the two methods we exercise."""

        class FakeSession:
            def __init__(self):
                self.upload_calls = []

            def file_info(self, filename):
                return file_info

            def upload(
                self,
                *,
                filename,
                path,
                token,
                comment,
                ignore_warnings=False,
            ):
                self.upload_calls.append(
                    {
                        "filename": filename,
                        "ignore_warnings": ignore_warnings,
                    }
                )
                return upload

            # Borrow the real upload_if_changed so we're testing IT, not
            # a re-implementation. Bind it as a method.
            upload_if_changed = WT.WikiSession.upload_if_changed

        return FakeSession()

    def test_skip_when_wiki_has_same_sha1(self):
        sess = self._session(
            file_info=WT.LiveFile(exists=True, sha1=self.sha1, size=len(self.payload)),
            upload={"upload": {"result": "Success"}},
        )
        action, resp = sess.upload_if_changed(
            filename="x.svg", path=self.path, token="t", comment="c"
        )
        self.assertEqual(action, "SKIP")
        self.assertIsNone(resp)
        self.assertEqual(sess.upload_calls, [])  # upload never invoked

    def test_create_when_wiki_missing(self):
        sess = self._session(
            file_info=WT.LiveFile(exists=False, sha1=None, size=None),
            upload={"upload": {"result": "Success"}},
        )
        action, resp = sess.upload_if_changed(
            filename="x.svg", path=self.path, token="t", comment="c"
        )
        self.assertEqual(action, "CREATE")
        self.assertIsNotNone(resp)
        # CREATE does NOT pass ignore_warnings -- a fresh upload shouldn't
        # need to bypass the "file exists" warning, and bypassing it would
        # mask genuine collisions.
        self.assertEqual(
            sess.upload_calls,
            [
                {"filename": "x.svg", "ignore_warnings": False},
            ],
        )

    def test_update_when_wiki_has_different_sha1(self):
        sess = self._session(
            file_info=WT.LiveFile(
                exists=True, sha1="0" * 40, size=99
            ),  # different bytes
            upload={"upload": {"result": "Success"}},
        )
        action, resp = sess.upload_if_changed(
            filename="x.svg", path=self.path, token="t", comment="c"
        )
        self.assertEqual(action, "UPDATE")
        self.assertIsNotNone(resp)
        # UPDATE MUST pass ignore_warnings=True -- MediaWiki returns
        # warnings.exists on same-filename re-upload otherwise.
        self.assertEqual(
            sess.upload_calls,
            [
                {"filename": "x.svg", "ignore_warnings": True},
            ],
        )


# ------------------------------------------------------------
# UploadMediaForPage
# ------------------------------------------------------------
class UploadMediaForPage(unittest.TestCase):
    """publish.upload_media_for: per-page iteration + failure handling."""

    def _make_page(self, wikitext: str, src_dir: Path) -> P.PlanItem:
        # Build a PlanItem with just enough fields populated for the
        # upload path to read. The src lives at src_dir/page.md so _media/
        # resolves correctly.
        src = src_dir / "page.md"
        src.write_text("---\ntitle: T\nmanaged: true\n---\nbody", encoding="utf-8")
        page = md2wiki.ConvertedPage(
            title="T",
            managed=True,
            categories=[],
            wikitext=wikitext,
            source=str(src),
        )
        return P.PlanItem(
            source=str(src),
            title="T",
            action=P.UPDATE,
            reason="test",
            page=page,
            generated_hash="x",
            live=None,
        )

    def _transport(self, action_per_file=None, error_per_file=None):
        """Mock transport with controllable upload_if_changed behaviour."""
        action_per_file = action_per_file or {}
        error_per_file = error_per_file or {}

        class FakeTransport:
            def __init__(self):
                self.calls = []
                self.tokens_issued = 0

            def csrf_token(self):
                self.tokens_issued += 1
                return "t"

            def upload_if_changed(self, *, filename, path, token, comment):
                self.calls.append(filename)
                if filename in error_per_file:
                    raise error_per_file[filename]
                return action_per_file.get(filename, "CREATE"), {
                    "upload": {"result": "Success"}
                }

        return FakeTransport()

    def test_uploads_each_referenced_file_once(self):
        with tempfile.TemporaryDirectory() as tmp:
            src_dir = Path(tmp)
            media = src_dir / P.MEDIA_SUBDIR
            media.mkdir()
            (media / "a.svg").write_bytes(b"a")
            (media / "b.png").write_bytes(b"b")
            item = self._make_page(
                "Body [[File:a.svg|cap]] and [[File:b.png]] and again [[File:a.svg]].",
                src_dir,
            )
            transport = self._transport()
            failures = P.upload_media_for(transport, item, summary="s")
            self.assertEqual(failures, 0)
            # a.svg referenced twice but uploaded once.
            self.assertEqual(transport.calls, ["a.svg", "b.png"])

    def test_missing_file_is_a_failure_warning(self):
        with tempfile.TemporaryDirectory() as tmp:
            src_dir = Path(tmp)
            (src_dir / P.MEDIA_SUBDIR).mkdir()
            # No file written -> reference is broken.
            item = self._make_page("[[File:missing.svg]]", src_dir)
            transport = self._transport()
            failures = P.upload_media_for(transport, item, summary="s")
            self.assertEqual(failures, 1)
            self.assertEqual(transport.calls, [])  # never attempted

    def test_upload_exception_counted_as_failure_others_continue(self):
        with tempfile.TemporaryDirectory() as tmp:
            src_dir = Path(tmp)
            media = src_dir / P.MEDIA_SUBDIR
            media.mkdir()
            (media / "broken.svg").write_bytes(b"x")
            (media / "ok.svg").write_bytes(b"y")
            item = self._make_page("[[File:broken.svg]] [[File:ok.svg]]", src_dir)
            transport = self._transport(
                error_per_file={"broken.svg": RuntimeError("simulated")},
            )
            failures = P.upload_media_for(transport, item, summary="s")
            self.assertEqual(failures, 1)
            # Failure on first file does NOT abort the loop -- the second
            # one is still attempted.
            self.assertEqual(transport.calls, ["broken.svg", "ok.svg"])

    def test_page_with_no_file_refs_does_nothing(self):
        with tempfile.TemporaryDirectory() as tmp:
            src_dir = Path(tmp)
            item = self._make_page("Plain wikitext, no files.", src_dir)
            transport = self._transport()
            failures = P.upload_media_for(transport, item, summary="s")
            self.assertEqual(failures, 0)
            self.assertEqual(transport.calls, [])
            self.assertEqual(transport.tokens_issued, 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
