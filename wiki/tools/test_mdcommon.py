#!/usr/bin/env python3
"""Unit tests for mdcommon -- the preprocessing helpers shared by md2wiki
and md2pdf. Pure-function tests; no pandoc, no filesystem except for the
title-map scanner which uses a temp tree."""

import tempfile
import textwrap
import unittest
from pathlib import Path

import mdcommon as M


# ------------------------------------------------------------
# ObsidianEmbedConversion
# ------------------------------------------------------------
class ObsidianEmbedConversion(unittest.TestCase):
    def test_embed_with_caption(self):
        out = M.convert_obsidian_embeds("![[_media/foo.svg|A caption]]")
        self.assertEqual(out, "![A caption](_media/foo.svg)")

    def test_embed_without_caption(self):
        out = M.convert_obsidian_embeds("![[_media/foo.svg]]")
        self.assertEqual(out, "![](_media/foo.svg)")

    def test_multiple_embeds_in_paragraph(self):
        src = "Inline ![[a.png]] and ![[b.png|alt b]] together."
        out = M.convert_obsidian_embeds(src)
        self.assertEqual(out, "Inline ![](a.png) and ![alt b](b.png) together.")

    def test_embed_not_at_line_start(self):
        # Some authors indent embeds inside a list item.
        out = M.convert_obsidian_embeds("- See ![[diag.svg|fig]] here.")
        self.assertEqual(out, "- See ![fig](diag.svg) here.")

    def test_no_embeds_unchanged(self):
        src = "Plain text with [a normal link](http://x) and `code`."
        self.assertEqual(M.convert_obsidian_embeds(src), src)

    def test_caption_with_special_chars(self):
        # Captions can contain en dashes, parens, quotes -- anything but ]].
        src = "![[fig.svg|Fig. 1 — Setup (see note)]]"
        out = M.convert_obsidian_embeds(src)
        self.assertEqual(out, "![Fig. 1 — Setup (see note)](fig.svg)")

    def test_embed_does_not_match_internal_link(self):
        # ![[...]] is an embed; [[...]] is a link. They must not collide.
        out = M.convert_obsidian_embeds("![[a.png]] and [[Page]]")
        self.assertEqual(out, "![](a.png) and [[Page]]")


# ------------------------------------------------------------
# ObsidianInternalLinkConversion
# ------------------------------------------------------------
class ObsidianInternalLinkConversion(unittest.TestCase):
    # New shape: {stem: [(wiki_title, source_path), ...]}. Tests below
    # exercise both the single-candidate case (most pages) and the
    # multi-candidate collision case (language subfolders, etc.).
    TITLE_MAP = {
        "06-data-access": [
            (
                "Gramps_6.0_Wiki_Manual_-_Addon_Development_-_Data_Access",
                "05 - Addon development/06-data-access.md",
            )
        ],
        "02-get-started": [
            (
                "Gramps_6.0_Wiki_Manual_-_Addon_Development_-_Getting_Started",
                "05 - Addon development/02-get-started.md",
            )
        ],
        "15-rules": [
            (
                "Gramps_6.0_Wiki_Manual_-_Addon_Development_-_Rules",
                "05 - Addon development/15-rules.md",
            )
        ],
    }

    def test_bare_target(self):
        out = M.convert_obsidian_internal_links(
            "See [[06-data-access]] for details.", self.TITLE_MAP
        )
        # Label defaults to title with underscores stripped.
        self.assertEqual(
            out,
            "See [Gramps 6.0 Wiki Manual - Addon Development - Data Access]"
            "(wiki:Gramps_6.0_Wiki_Manual_-_Addon_Development_-_Data_Access) for details.",
        )

    def test_target_with_label(self):
        out = M.convert_obsidian_internal_links(
            "See [[06-data-access|the Data access page]] later.", self.TITLE_MAP
        )
        self.assertEqual(
            out,
            "See [the Data access page]"
            "(wiki:Gramps_6.0_Wiki_Manual_-_Addon_Development_-_Data_Access) later.",
        )

    def test_folder_prefixed_target(self):
        # [[folder/Stem]] -- folder is dropped, stem must still be unique.
        out = M.convert_obsidian_internal_links(
            "See [[05 - Addon development/06-data-access]].", self.TITLE_MAP
        )
        self.assertIn(
            "wiki:Gramps_6.0_Wiki_Manual_-_Addon_Development_-_Data_Access", out
        )

    def test_anchor_is_dropped(self):
        # Anchors (#section) are dropped -- wiki may not have a matching anchor.
        out = M.convert_obsidian_internal_links(
            "See [[15-rules#Testing|the Testing rule]].", self.TITLE_MAP
        )
        self.assertIn("[the Testing rule]", out)
        self.assertIn("wiki:Gramps_6.0_Wiki_Manual_-_Addon_Development_-_Rules", out)
        self.assertNotIn("#", out)

    def test_unresolved_raises(self):
        with self.assertRaises(ValueError) as cm:
            M.convert_obsidian_internal_links(
                "Broken [[no-such-page]] reference.", self.TITLE_MAP
            )
        msg = str(cm.exception)
        self.assertIn("no-such-page", msg)
        self.assertIn("title map", msg)

    def test_ambiguous_bare_target_raises(self):
        # Two pages share the same stem; bare [[stem]] is unresolvable
        # without a folder prefix. Error names BOTH candidates so the
        # author knows what to disambiguate against.
        tm = {
            "getting-started": [
                ("Gramps_Manual_-_Getting_Started", "user-guide/getting-started.md"),
                (
                    "Gramps_Manual_-_Getting_Started/bg",
                    "user-guide/bg/getting-started.md",
                ),
            ],
        }
        with self.assertRaises(ValueError) as cm:
            M.convert_obsidian_internal_links("See [[getting-started]].", tm)
        msg = str(cm.exception)
        self.assertIn("ambiguous", msg)
        self.assertIn("user-guide/getting-started.md", msg)
        self.assertIn("user-guide/bg/getting-started.md", msg)
        self.assertIn("[[folder/getting-started]]", msg)

    def test_folder_form_disambiguates_collision(self):
        # When a stem has multiple candidates, [[folder/stem]] picks one
        # by path suffix.
        tm = {
            "getting-started": [
                ("Manual_-_Getting_Started", "user-guide/getting-started.md"),
                ("Manual_-_Getting_Started_BG", "user-guide/bg/getting-started.md"),
            ],
        }
        out = M.convert_obsidian_internal_links("See [[bg/getting-started]].", tm)
        self.assertIn("(wiki:Manual_-_Getting_Started_BG)", out)
        self.assertNotIn("ambiguous", out)

    def test_folder_form_no_match_raises(self):
        # Folder-prefixed form that doesn't match any candidate path is an
        # error -- prevents silent fallback to the wrong page.
        tm = {
            "getting-started": [
                ("Manual_GS", "user-guide/getting-started.md"),
            ],
        }
        with self.assertRaises(ValueError) as cm:
            M.convert_obsidian_internal_links(
                "See [[nonexistent-folder/getting-started]].", tm
            )
        msg = str(cm.exception)
        self.assertIn("no source path matched", msg)
        self.assertIn("nonexistent-folder/getting-started", msg)

    def test_does_not_match_embed(self):
        # ![[...]] is an embed; this helper must skip it.
        src = "Embed ![[06-data-access.png]] should pass through unchanged here."
        out = M.convert_obsidian_internal_links(src, self.TITLE_MAP)
        self.assertEqual(out, src)

    def test_multiple_links_in_one_line(self):
        src = "See [[02-get-started]] then [[15-rules]]."
        out = M.convert_obsidian_internal_links(src, self.TITLE_MAP)
        # Both converted to wiki: form.
        self.assertEqual(out.count("(wiki:"), 2)
        self.assertNotIn("[[", out)

    def test_no_links_unchanged(self):
        src = "Plain paragraph with [a normal link](http://x)."
        self.assertEqual(M.convert_obsidian_internal_links(src, self.TITLE_MAP), src)


# ------------------------------------------------------------
# ImagePathAbsolutising
# ------------------------------------------------------------
class ImagePathAbsolutising(unittest.TestCase):
    def test_relative_path_resolved(self):
        # Use the actual cwd resolution to keep this OS-agnostic.
        with tempfile.TemporaryDirectory() as tmp:
            src_dir = Path(tmp)
            media = src_dir / "_media"
            media.mkdir()
            (media / "x.png").write_bytes(b"")
            out = M.absolutize_image_paths("![alt](_media/x.png)", src_dir)
            self.assertEqual(out, f"![alt]({media / 'x.png'})")

    def test_external_url_untouched(self):
        src = "![alt](https://example.com/x.png)"
        self.assertEqual(M.absolutize_image_paths(src, Path("/tmp")), src)

    def test_data_uri_untouched(self):
        src = "![alt](data:image/png;base64,iVBOR...)"
        self.assertEqual(M.absolutize_image_paths(src, Path("/tmp")), src)

    def test_absolute_path_untouched(self):
        src = "![alt](/abs/path/x.png)"
        self.assertEqual(M.absolutize_image_paths(src, Path("/tmp")), src)

    def test_obsidian_embed_left_alone(self):
        # Helper operates on standard markdown images only; Obsidian embeds
        # are a separate pass (run convert_obsidian_embeds first).
        src = "![[_media/x.png]]"
        with tempfile.TemporaryDirectory() as tmp:
            self.assertEqual(M.absolutize_image_paths(src, Path(tmp)), src)


# ------------------------------------------------------------
# TitleMapScanner
# ------------------------------------------------------------
class TitleMapScanner(unittest.TestCase):
    def _make_page(
        self, dir: Path, name: str, title: str, managed: bool = True
    ) -> None:
        body = textwrap.dedent(f"""\
            ---
            title: "{title}"
            managed: {str(managed).lower()}
            ---

            Body text.
            """)
        (dir / name).write_text(body, encoding="utf-8")

    def test_basic_scan(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self._make_page(root, "01-foo.md", "The Foo Page")
            self._make_page(root, "02-bar.md", "Bar Page")
            tm = M.build_title_map(root)
            # New shape: stem -> [(title, path), ...]; one candidate each here.
            self.assertEqual(len(tm["01-foo"]), 1)
            self.assertEqual(tm["01-foo"][0][0], "The_Foo_Page")
            self.assertEqual(len(tm["02-bar"]), 1)
            self.assertEqual(tm["02-bar"][0][0], "Bar_Page")

    def test_includes_unmanaged_drafts(self):
        # Drafts ARE resolvable -- managed only controls publishability.
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self._make_page(root, "draft.md", "Draft Page", managed=False)
            tm = M.build_title_map(root)
            self.assertIn("draft", tm)

    def test_skips_files_without_frontmatter(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "no-frontmatter.md").write_text("Just text.\n", encoding="utf-8")
            self._make_page(root, "real.md", "Real Page")
            tm = M.build_title_map(root)
            self.assertEqual(list(tm), ["real"])
            self.assertEqual(tm["real"][0][0], "Real_Page")

    def test_skips_pages_without_title(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "no-title.md").write_text(
                "---\nmanaged: true\n---\nBody.\n", encoding="utf-8"
            )
            self._make_page(root, "real.md", "Real Page")
            tm = M.build_title_map(root)
            self.assertEqual(list(tm), ["real"])

    def test_collisions_collected_not_raised(self):
        # New behaviour: collisions are kept as multi-candidate entries.
        # Build-time tolerates them; only resolution-time ambiguity errors.
        # (Pre-existing vaults like 03 - User guide/ have multi-language
        # copies of the same page that nobody actually [[link]]s across.)
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "a").mkdir()
            (root / "b").mkdir()
            self._make_page(root / "a", "shared.md", "From A")
            self._make_page(root / "b", "shared.md", "From B")
            tm = M.build_title_map(root)  # MUST NOT raise
            self.assertEqual(len(tm["shared"]), 2)
            titles = {entry[0] for entry in tm["shared"]}
            self.assertEqual(titles, {"From_A", "From_B"})
            paths = {entry[1] for entry in tm["shared"]}
            self.assertTrue(any(p.endswith("a/shared.md") for p in paths))
            self.assertTrue(any(p.endswith("b/shared.md") for p in paths))

    def test_recursive_walk(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "sub" / "deeper").mkdir(parents=True)
            self._make_page(root / "sub" / "deeper", "deep.md", "Deep Page")
            tm = M.build_title_map(root)
            self.assertEqual(list(tm), ["deep"])
            self.assertEqual(tm["deep"][0][0], "Deep_Page")


# ------------------------------------------------------------
# FileRefBasenameify
# ------------------------------------------------------------
class FileRefBasenameify(unittest.TestCase):
    def test_subdir_prefix_stripped(self):
        out = M.basenameify_file_refs("[[File:_media/foo.svg|cap]]")
        self.assertEqual(out, "[[File:foo.svg|cap]]")

    def test_no_caption(self):
        out = M.basenameify_file_refs("[[File:_media/foo.svg]]")
        self.assertEqual(out, "[[File:foo.svg]]")

    def test_no_subdir_untouched(self):
        out = M.basenameify_file_refs("[[File:foo.svg|cap]]")
        self.assertEqual(out, "[[File:foo.svg|cap]]")

    def test_deep_subdir(self):
        out = M.basenameify_file_refs("[[File:a/b/c/foo.png]]")
        self.assertEqual(out, "[[File:foo.png]]")

    def test_multiple_refs_in_one_text(self):
        src = "First [[File:a/x.svg|alpha]] and [[File:b/c/y.png]]."
        out = M.basenameify_file_refs(src)
        self.assertEqual(out, "First [[File:x.svg|alpha]] and [[File:y.png]].")


# ------------------------------------------------------------
# HtmlCommentStash
# ------------------------------------------------------------
class HtmlCommentStash(unittest.TestCase):
    def test_round_trip_preserves_content(self):
        src = "Before <!-- a note --> after."
        stashed, tokens = M.stash_html_comments(src)
        self.assertNotIn("<!--", stashed)
        self.assertIn("MDCOMMENT", stashed)
        restored = M.unstash_html_comments(stashed, tokens)
        self.assertEqual(restored, src)

    def test_multiple_comments(self):
        src = "<!-- one --> X <!-- two --> Y <!-- three -->"
        stashed, tokens = M.stash_html_comments(src)
        self.assertEqual(len(tokens), 3)
        restored = M.unstash_html_comments(stashed, tokens)
        self.assertEqual(restored, src)

    def test_multiline_comment(self):
        src = "Before\n<!-- line one\nline two\nline three -->\nAfter"
        stashed, tokens = M.stash_html_comments(src)
        self.assertNotIn("<!--", stashed)
        self.assertEqual(M.unstash_html_comments(stashed, tokens), src)

    def test_obsidian_link_inside_comment_is_protected(self):
        # The bug this guards against: an author documenting [[Page]] syntax
        # inside a comment had their documentation silently rewritten.
        src = "<!-- see [[15-rules]] for the rule -->"
        title_map = {"15-rules": [("Real_Rules_Page", "rules.md")]}
        stashed, tokens = M.stash_html_comments(src)
        # The preprocessor sees the placeholder, not the comment.
        converted = M.convert_obsidian_internal_links(stashed, title_map)
        restored = M.unstash_html_comments(converted, tokens)
        self.assertEqual(restored, src)  # original comment intact

    def test_embed_inside_comment_is_protected(self):
        src = "<!-- demo: ![[_media/foo.svg|cap]] -->"
        stashed, tokens = M.stash_html_comments(src)
        converted = M.convert_obsidian_embeds(stashed)
        restored = M.unstash_html_comments(converted, tokens)
        self.assertEqual(restored, src)

    def test_links_outside_comments_still_convert(self):
        # Comment-stash must NOT interfere with links in body text.
        src = "<!-- ignored: [[15-rules]] -->\nIn body: [[15-rules]]."
        title_map = {"15-rules": [("Real_Rules_Page", "rules.md")]}
        stashed, tokens = M.stash_html_comments(src)
        converted = M.convert_obsidian_internal_links(stashed, title_map)
        restored = M.unstash_html_comments(converted, tokens)
        # Body link converted, comment untouched.
        self.assertIn("<!-- ignored: [[15-rules]] -->", restored)
        self.assertIn("(wiki:Real_Rules_Page)", restored)

    def test_no_comments_is_identity(self):
        src = "No comments here, just text and [[Page]]."
        stashed, tokens = M.stash_html_comments(src)
        self.assertEqual(stashed, src)
        self.assertEqual(tokens, [])
        self.assertEqual(M.unstash_html_comments(stashed, tokens), src)

    def test_unknown_placeholder_passes_through(self):
        # If the unstash sees a placeholder not in its token list (e.g. token
        # list corrupted), leave it alone rather than blowing up.
        stray = "Some \x00MDCOMMENT0099\x00 stray."
        self.assertEqual(M.unstash_html_comments(stray, []), stray)


# ------------------------------------------------------------
# CodeStash
# ------------------------------------------------------------
class CodeStash(unittest.TestCase):
    def test_inline_code_round_trip(self):
        src = "Use `[[Page]]` to link."
        stashed, tokens = M.stash_code(src)
        self.assertNotIn("`", stashed)
        self.assertEqual(M.unstash_code(stashed, tokens), src)

    def test_fenced_code_round_trip(self):
        src = textwrap.dedent("""\
            Before.

            ```python
            data = [['Gramps', 'url', True]]
            ```

            After.
            """)
        stashed, tokens = M.stash_code(src)
        self.assertNotIn("```", stashed)
        self.assertNotIn("[[", stashed)  # the list-literal inside is gone too
        self.assertEqual(M.unstash_code(stashed, tokens), src)

    def test_obsidian_link_inside_inline_code_protected(self):
        # The bug this guards against: a code span like `[[Page]]` (typically
        # showing the SYNTAX of an Obsidian link) got rewritten as a real one.
        src = "Authors write `[[Page]]` for internal links."
        title_map = {"Page": [("Real_Page", "page.md")]}
        stashed, code_tokens = M.stash_code(src)
        converted = M.convert_obsidian_internal_links(stashed, title_map)
        restored = M.unstash_code(converted, code_tokens)
        self.assertEqual(restored, src)  # code span untouched

    def test_obsidian_link_inside_fenced_code_protected(self):
        # Regression from a scraped page that contained:
        #   [['Gramps', 'https://raw.githubusercontent.com/...', True]]
        # inside a fenced code block. The Obsidian-link regex matched the
        # outer [[...]] and tried to resolve a stem that wasn't a stem.
        src = textwrap.dedent("""\
            Example:

            ```
            [['Gramps', 'https://raw.githubusercontent.com/...', True]]
            ```

            End.
            """)
        title_map = {"unused": [("Unused", "u.md")]}
        stashed, code_tokens = M.stash_code(src)
        # MUST NOT raise -- the [[...]] is inside the fence, stashed away.
        converted = M.convert_obsidian_internal_links(stashed, title_map)
        restored = M.unstash_code(converted, code_tokens)
        self.assertEqual(restored, src)

    def test_links_outside_code_still_convert(self):
        src = "See `[[Page]]` syntax above; the actual link is [[Page]] here."
        title_map = {"Page": [("Real_Page", "page.md")]}
        stashed, code_tokens = M.stash_code(src)
        converted = M.convert_obsidian_internal_links(stashed, title_map)
        restored = M.unstash_code(converted, code_tokens)
        self.assertIn("`[[Page]]`", restored)  # code span intact
        self.assertIn("[Real Page](wiki:Real_Page)", restored)  # body converted

    def test_no_code_is_identity(self):
        src = "No code here, just text."
        stashed, tokens = M.stash_code(src)
        self.assertEqual(stashed, src)
        self.assertEqual(tokens, [])
        self.assertEqual(M.unstash_code(stashed, tokens), src)

    def test_unknown_placeholder_passes_through(self):
        stray = "Some \x00MDCODE0099\x00 stray."
        self.assertEqual(M.unstash_code(stray, []), stray)


# ------------------------------------------------------------
# FileRefExtraction
# ------------------------------------------------------------
class FileRefExtraction(unittest.TestCase):
    def test_extracts_basenames(self):
        wikitext = "Page body [[File:_media/foo.svg|cap]] and [[File:bar.png]]."
        self.assertEqual(M.extract_file_basenames(wikitext), ["foo.svg", "bar.png"])

    def test_no_refs(self):
        self.assertEqual(M.extract_file_basenames("Plain text."), [])

    def test_duplicates_preserved(self):
        # Caller deduplicates if it cares; this just reports what's there.
        wikitext = "[[File:a.svg]] twice: [[File:a.svg|second]]."
        self.assertEqual(M.extract_file_basenames(wikitext), ["a.svg", "a.svg"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
