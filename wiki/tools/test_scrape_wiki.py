#!/usr/bin/env python3
"""Offline tests for the pure helpers in scrape_wiki -- no browser, no network.

Run:
  cd tools && python3 test_scrape_wiki.py
"""

from __future__ import annotations

import unittest

import scrape_wiki as sw


# ---------------------------------------------------------------------------
#
# TitleToSlugTests
#
# ---------------------------------------------------------------------------
class TitleToSlugTests(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(sw.title_to_slug("Foo Bar"), "foo-bar")

    def test_strip_prefix_with_hyphen_joiner(self):
        self.assertEqual(
            sw.title_to_slug(
                "Gramps 6.0 Wiki Manual - Getting started",
                strip_prefix="Gramps 6.0 Wiki Manual",
            ),
            "getting-started",
        )

    def test_strip_prefix_with_slash_joiner(self):
        self.assertEqual(
            sw.title_to_slug("Manual/Sub Page", strip_prefix="Manual"),
            "sub-page",
        )

    def test_strip_prefix_equals_title(self):
        # The seed itself: stripping leaves nothing, so we keep the full title.
        self.assertEqual(
            sw.title_to_slug(
                "Gramps 6.0 Wiki Manual", strip_prefix="Gramps 6.0 Wiki Manual"
            ),
            "gramps-6.0-wiki-manual",
        )

    def test_special_chars_collapse(self):
        # Punctuation other than . _ - becomes a single hyphen.
        self.assertEqual(
            sw.title_to_slug("Why is it called 'Gramps'?"), "why-is-it-called-gramps"
        )

    def test_preserves_version_dots(self):
        self.assertEqual(sw.title_to_slug("Gramps 6.0 release"), "gramps-6.0-release")


# ---------------------------------------------------------------------------
#
# ImageTitleToFilenameTests
#
# ---------------------------------------------------------------------------
class ImageTitleToFilenameTests(unittest.TestCase):
    def test_strips_namespace_keeps_extension(self):
        self.assertEqual(sw.image_title_to_filename("File:Foo Bar.png"), "Foo_Bar.png")

    def test_already_bare(self):
        self.assertEqual(sw.image_title_to_filename("Foo_Bar.png"), "Foo_Bar.png")

    def test_multiple_spaces(self):
        self.assertEqual(
            sw.image_title_to_filename("File:Foo   Bar Baz.jpg"), "Foo_Bar_Baz.jpg"
        )

    def test_german_datei_namespace(self):
        self.assertEqual(sw.image_title_to_filename("Datei:Foo Bar.png"), "Foo_Bar.png")

    def test_french_fichier_namespace(self):
        self.assertEqual(
            sw.image_title_to_filename("Fichier:Capture.png"), "Capture.png"
        )

    def test_arbitrary_namespace_stripped(self):
        # Defensive: any single-colon prefix is treated as a namespace.
        self.assertEqual(sw.image_title_to_filename("Image:Photo.jpg"), "Photo.jpg")


# ---------------------------------------------------------------------------
#
# LangFromTitleTests
#
# ---------------------------------------------------------------------------
class LangFromTitleTests(unittest.TestCase):
    def test_german(self):
        self.assertEqual(sw.lang_from_title("De:Gramps 6.0 Wiki Handbuch"), "de")

    def test_french(self):
        self.assertEqual(sw.lang_from_title("Fr:Gramps 6.0 Wiki Manuel"), "fr")

    def test_english_no_prefix(self):
        self.assertIsNone(sw.lang_from_title("Gramps 6.0 Wiki Manual"))

    def test_namespace_not_a_lang_code(self):
        # 'Help:' is a real MediaWiki namespace, not a language code -- the
        # regex requires Uppercase+lowercase (two chars). Anything else
        # uppercase-then-not-lowercase won't match.
        self.assertIsNone(sw.lang_from_title("HELP:Foo"))

    def test_lowercase_prefix_rejected(self):
        # 'de:' (lowercase) is the interwiki form, not the local-title form;
        # the convention here is 'De:'.
        self.assertIsNone(sw.lang_from_title("de:Gramps 6.0 Wiki Handbuch"))


# ---------------------------------------------------------------------------
#
# NormaliseFileLinksTests
#
# ---------------------------------------------------------------------------
class NormaliseFileLinksTests(unittest.TestCase):
    def test_german_alias(self):
        wt = "Embed: [[Datei:Foo.png|thumb|Eine Bildunterschrift]]"
        out = sw.normalise_file_links(wt)
        self.assertEqual(out, "Embed: [[File:Foo.png|thumb|Eine Bildunterschrift]]")

    def test_canonical_file_unchanged(self):
        wt = "[[File:Foo.png]]"
        self.assertEqual(sw.normalise_file_links(wt), wt)

    def test_french_alias(self):
        wt = "[[Fichier:Capture.png]]"
        self.assertEqual(sw.normalise_file_links(wt), "[[File:Capture.png]]")

    def test_multiple_in_one_doc(self):
        wt = "[[Datei:A.png]] und [[Bild:B.jpg]] sind beide Bilder."
        out = sw.normalise_file_links(wt)
        self.assertEqual(out, "[[File:A.png]] und [[File:B.jpg]] sind beide Bilder.")

    def test_alias_inside_word_not_rewritten(self):
        # 'Datei' appearing in prose (not in '[[...]]') must NOT be touched.
        wt = "Das Wort Datei kommt hier vor, aber nicht als Link."
        self.assertEqual(sw.normalise_file_links(wt), wt)

    def test_whitespace_inside_brackets_handled(self):
        wt = "[[  Datei : Foo.png ]]"
        # We only normalise the namespace; whitespace inside the brackets
        # is preserved as MediaWiki itself ignores it on parse.
        self.assertEqual(sw.normalise_file_links(wt), "[[  File : Foo.png ]]")


# ---------------------------------------------------------------------------
#
# InScopeTests
#
# ---------------------------------------------------------------------------
class InScopeTests(unittest.TestCase):
    PREFIXES = ["Gramps 6.0 Wiki Manual"]

    def test_seed_itself(self):
        self.assertTrue(sw.in_scope("Gramps 6.0 Wiki Manual", self.PREFIXES))

    def test_hyphen_subpage(self):
        self.assertTrue(
            sw.in_scope("Gramps 6.0 Wiki Manual - Getting started", self.PREFIXES)
        )

    def test_slash_subpage(self):
        self.assertTrue(sw.in_scope("Gramps 6.0 Wiki Manual/FAQ", self.PREFIXES))

    def test_other_manual_version_not_in_scope(self):
        # A 5.2 manual page should NOT match the 6.0 prefix.
        self.assertFalse(
            sw.in_scope("Gramps 5.2 Wiki Manual - Getting started", self.PREFIXES)
        )

    def test_unrelated_page(self):
        self.assertFalse(sw.in_scope("Addons", self.PREFIXES))

    def test_prefix_substring_not_a_match(self):
        # "Gramps 6.0 Wiki Manual2" must NOT match (no ' - ' or '/' joiner).
        self.assertFalse(sw.in_scope("Gramps 6.0 Wiki Manual2", self.PREFIXES))

    def test_multiple_prefixes(self):
        prefixes = ["Gramps 6.0 Wiki Manual", "Addons development"]
        self.assertTrue(sw.in_scope("Addons development - GTK pins", prefixes))

    def test_german_prefix_in_scope(self):
        prefixes = ["De:Gramps 6.0 Wiki Handbuch"]
        self.assertTrue(
            sw.in_scope("De:Gramps 6.0 Wiki Handbuch - Erste Schritte", prefixes)
        )

    def test_german_excludes_english(self):
        # A German scrape must not chase English links.
        prefixes = ["De:Gramps 6.0 Wiki Handbuch"]
        self.assertFalse(
            sw.in_scope("Gramps 6.0 Wiki Manual - Getting started", prefixes)
        )


# ---------------------------------------------------------------------------
#
# RewriteImageRefsTests
#
# ---------------------------------------------------------------------------
class RewriteImageRefsTests(unittest.TestCase):
    def test_basic_file_ref(self):
        md = "Before ![alt text](File:Foo_Bar.png) after."
        out = sw.rewrite_image_refs(md, "_media")
        self.assertEqual(out, "Before ![[_media/Foo_Bar.png|alt text]] after.")

    def test_empty_alt(self):
        md = "![](File:Foo.png)"
        self.assertEqual(sw.rewrite_image_refs(md, "_media"), "![[_media/Foo.png]]")

    def test_lowercase_file_namespace(self):
        # pandoc sometimes emits lower-case file:
        md = "![pic](file:Diagram.svg)"
        self.assertEqual(
            sw.rewrite_image_refs(md, "_media"), "![[_media/Diagram.svg|pic]]"
        )

    def test_title_attribute_stripped(self):
        md = '![alt](File:Foo.png "tooltip text")'
        self.assertEqual(sw.rewrite_image_refs(md, "_media"), "![[_media/Foo.png|alt]]")

    def test_spaces_in_name_become_underscores(self):
        # If pandoc URL-decodes %20 into a literal space, we still normalise.
        md = "![](File:Foo%20Bar.png)"
        self.assertEqual(sw.rewrite_image_refs(md, "_media"), "![[_media/Foo_Bar.png]]")

    def test_custom_media_subdir(self):
        md = "![](File:Foo.png)"
        self.assertEqual(
            sw.rewrite_image_refs(md, "assets/img"), "![[assets/img/Foo.png]]"
        )

    def test_non_image_links_untouched(self):
        # An ordinary link to File: (not an embed) is left alone.
        md = "[Foo](File:Foo.png) is a link not an embed"
        self.assertEqual(sw.rewrite_image_refs(md, "_media"), md)

    def test_pandoc_actual_output_shape(self):
        # The shape pandoc -t gfm ACTUALLY emits for a wiki embed: the
        # 'File:' prefix is stripped and the alt text is duplicated in a
        # title attribute. Regression for the bug the end-to-end check
        # exposed -- the old regex only matched the wishful 'File:'-prefixed
        # form and would have left this untouched.
        md = '![Eine Bildunterschrift](Beispiel_Bild.png "Eine Bildunterschrift")'
        self.assertEqual(
            sw.rewrite_image_refs(md, "_media"),
            "![[_media/Beispiel_Bild.png|Eine Bildunterschrift]]",
        )

    def test_external_url_left_alone(self):
        # We must not ferry remote-hosted images into _media/.
        md = "![remote](https://example.com/foo.png)"
        self.assertEqual(sw.rewrite_image_refs(md, "_media"), md)

    def test_protocol_relative_url_left_alone(self):
        md = "![remote](//example.com/foo.png)"
        self.assertEqual(sw.rewrite_image_refs(md, "_media"), md)

    def test_basename_collapses_path(self):
        # Defensive: a path-shaped target lands at the bare basename.
        md = "![](sub/dir/Foo.png)"
        self.assertEqual(sw.rewrite_image_refs(md, "_media"), "![[_media/Foo.png]]")


# ---------------------------------------------------------------------------
#
# RenderMarkdownTests
#
# ---------------------------------------------------------------------------
class RenderMarkdownTests(unittest.TestCase):
    def test_round_trip_shape(self):
        fm = {
            "title": "Gramps 6.0 Wiki Manual",
            "categories": ["Manual", "Gramps 6.0"],
            "managed": False,
        }
        body = "## Overview\n\nHello."
        out = sw.render_markdown(fm, body)
        self.assertTrue(out.startswith("---\n"))
        # Key order must follow insertion order (we asserted not-sorted).
        title_pos = out.index("title:")
        cats_pos = out.index("categories:")
        managed_pos = out.index("managed:")
        self.assertLess(title_pos, cats_pos)
        self.assertLess(cats_pos, managed_pos)
        # Body separated from front-matter by a blank line, single trailing nl.
        self.assertIn("---\n\n## Overview", out)
        self.assertTrue(out.endswith("\n"))


# ---------------------------------------------------------------------------
#
# LangSubpathRejectionTests
#
# ---------------------------------------------------------------------------
class LangSubpathRejectionTests(unittest.TestCase):
    """The '/<lang>' suffix is the Gramps wiki's OTHER translation
    convention; an English scrape must not chase '/bg', '/ca', '/cs' etc."""

    EN = ["Gramps 6.0 Wiki Manual"]
    DE_SLASH = ["Gramps 6.0 Wiki Manual/de"]  # hypothetical seed in the
    # other-style translation namespace

    def test_bulgarian_slash_excluded_from_english(self):
        self.assertFalse(sw.in_scope("Gramps 6.0 Wiki Manual/bg", self.EN))

    def test_catalan_slash_excluded_from_english(self):
        self.assertFalse(sw.in_scope("Gramps 6.0 Wiki Manual/ca", self.EN))

    def test_three_letter_code_excluded(self):
        # Some MediaWiki sites use ISO 639-3 codes; same convention here.
        self.assertFalse(sw.in_scope("Gramps 6.0 Wiki Manual/deu", self.EN))

    def test_uppercase_subpage_still_in_scope(self):
        # 'FAQ', 'Glossary', etc. are real subpages, not language codes.
        self.assertTrue(sw.in_scope("Gramps 6.0 Wiki Manual/FAQ", self.EN))

    def test_long_subpage_name_still_in_scope(self):
        self.assertTrue(sw.in_scope("Gramps 6.0 Wiki Manual/Editing", self.EN))

    def test_lang_subpath_matches_when_seed_matches(self):
        # When the seed itself uses '/de', a '/de' child of it must remain in scope.
        self.assertTrue(sw.in_scope("Gramps 6.0 Wiki Manual/de", self.DE_SLASH))

    def test_bcp47_hyphen_form_excluded(self):
        # Regression for the first-run miss: '/pt-br' (Brazilian Portuguese)
        # slipped through the original 2-3-letter-only filter.
        self.assertFalse(sw.in_scope("Gramps 6.0 Wiki Manual/pt-br", self.EN))

    def test_zh_hans_excluded(self):
        self.assertFalse(sw.in_scope("Gramps 6.0 Wiki Manual/zh-hans", self.EN))

    def test_space_separated_locale_excluded(self):
        # Regression for the first-run miss: 'Gramps 6.0 Wiki Manual/pt PT'
        # wrote a junk pt-pt.md before this filter caught the space-separated
        # locale form.
        self.assertFalse(sw.in_scope("Gramps 6.0 Wiki Manual/pt PT", self.EN))

    def test_uppercase_region_with_hyphen_excluded(self):
        self.assertFalse(sw.in_scope("Gramps 6.0 Wiki Manual/zh-CN", self.EN))


# ---------------------------------------------------------------------------
#
# LangSubpathOfTests
#
# ---------------------------------------------------------------------------
class LangSubpathOfTests(unittest.TestCase):
    """Direct coverage of the underlying detector, separate from in_scope."""

    def test_simple_two_letter(self):
        self.assertEqual(sw.lang_subpath_of("Foo/bg"), "bg")

    def test_three_letter(self):
        self.assertEqual(sw.lang_subpath_of("Foo/eng"), "eng")

    def test_bcp47_hyphen(self):
        self.assertEqual(sw.lang_subpath_of("Foo/pt-br"), "pt-br")

    def test_space_separated(self):
        self.assertEqual(sw.lang_subpath_of("Foo/pt PT"), "pt PT")

    def test_uppercase_first_letter_rejected(self):
        self.assertIsNone(sw.lang_subpath_of("Foo/FAQ"))

    def test_no_subpath(self):
        self.assertIsNone(sw.lang_subpath_of("Foo"))

    def test_subpath_not_at_end(self):
        # '/bg' is not at the end of the title.
        self.assertIsNone(sw.lang_subpath_of("Foo/bg/details"))


# ---------------------------------------------------------------------------
#
# LangCodeOfTests
#
# ---------------------------------------------------------------------------
class LangCodeOfTests(unittest.TestCase):
    """The unified detector covers BOTH wiki translation conventions."""

    def test_prefix_form(self):
        self.assertEqual(sw.lang_code_of("De:Gramps 6.0 Wiki Handbuch"), "de")

    def test_suffix_form(self):
        self.assertEqual(sw.lang_code_of("Gramps 6.0 Wiki Manual/bg"), "bg")

    def test_english_untagged(self):
        self.assertIsNone(sw.lang_code_of("Gramps 6.0 Wiki Manual"))

    def test_suffix_chapter_form(self):
        self.assertEqual(sw.lang_code_of("Gramps 6.0 Wiki Manual - Preface/bg"), "bg")


# ---------------------------------------------------------------------------
#
# TitleRootTests
#
# ---------------------------------------------------------------------------
class TitleRootTests(unittest.TestCase):
    def test_strips_prefix_form(self):
        self.assertEqual(
            sw.title_root("De:Gramps 6.0 Wiki Handbuch"), "Gramps 6.0 Wiki Handbuch"
        )

    def test_strips_suffix_form(self):
        self.assertEqual(
            sw.title_root("Gramps 6.0 Wiki Manual/bg"), "Gramps 6.0 Wiki Manual"
        )

    def test_strips_suffix_on_chapter(self):
        self.assertEqual(
            sw.title_root("Gramps 6.0 Wiki Manual - Preface/bg"),
            "Gramps 6.0 Wiki Manual - Preface",
        )

    def test_untagged_passes_through(self):
        self.assertEqual(
            sw.title_root("Gramps 6.0 Wiki Manual - Preface"),
            "Gramps 6.0 Wiki Manual - Preface",
        )


# ---------------------------------------------------------------------------
#
# BulgarianSeedScopeTests
#
# ---------------------------------------------------------------------------
class BulgarianSeedScopeTests(unittest.TestCase):
    """Suffix-style seed must match its own root-equal index page AND its
    hyphenated chapters. This was the live bug -- old in_scope compared raw
    titles, so 'Foo - Preface/bg' didn't match prefix 'Foo/bg'."""

    BG = ["Gramps 6.0 Wiki Manual/bg"]

    def test_bulgarian_seed_in_scope(self):
        self.assertTrue(sw.in_scope("Gramps 6.0 Wiki Manual/bg", self.BG))

    def test_bulgarian_chapter_in_scope(self):
        # The bug: 'Foo - Preface/bg' doesn't startswith 'Foo/bg - '. Fixed
        # by comparing roots.
        self.assertTrue(sw.in_scope("Gramps 6.0 Wiki Manual - Preface/bg", self.BG))

    def test_bulgarian_excludes_english(self):
        self.assertFalse(sw.in_scope("Gramps 6.0 Wiki Manual - Preface", self.BG))

    def test_bulgarian_excludes_catalan(self):
        self.assertFalse(sw.in_scope("Gramps 6.0 Wiki Manual - Preface/ca", self.BG))

    def test_english_seed_still_excludes_bulgarian(self):
        # Regression for the original /lang-leak fix.
        en = ["Gramps 6.0 Wiki Manual"]
        self.assertFalse(sw.in_scope("Gramps 6.0 Wiki Manual - Preface/bg", en))

    def test_german_seed_matches_german_chapter(self):
        # Prefix-style translation continues to work via root comparison.
        de = ["De:Gramps 6.0 Wiki Handbuch"]
        self.assertTrue(sw.in_scope("De:Gramps 6.0 Wiki Handbuch - Vorwort", de))

    def test_german_excludes_english(self):
        de = ["De:Gramps 6.0 Wiki Handbuch"]
        self.assertFalse(sw.in_scope("Gramps 6.0 Wiki Manual - Preface", de))


# ---------------------------------------------------------------------------
#
# FindTranslationLinksInHtmlTests
#
# ---------------------------------------------------------------------------
class FindTranslationLinksInHtmlTests(unittest.TestCase):
    """The pure HTML-scanning helper that drives both --list-translations
    and --all-translations. Synthetic HTML covers the Gramps wiki's two
    translation conventions plus the noise we have to filter out."""

    SEED = "Gramps 6.0 Wiki Manual"

    def _languages_html(self) -> str:
        # Synthetic shape of what the {{Languages}} template renders to.
        return (
            '<div class="languages">Languages: '
            '<a href="/wiki/index.php/De:Gramps_6.0_Wiki_Handbuch" '
            'title="De:Gramps 6.0 Wiki Handbuch">Deutsch</a> &middot; '
            '<a href="/wiki/index.php/Gramps_6.0_Wiki_Manual/bg" '
            'title="Gramps 6.0 Wiki Manual/bg">Bulgarian</a> &middot; '
            '<a href="/wiki/index.php/Fr:Gramps_6.0_Wiki_Manuel" '
            'title="Fr:Gramps 6.0 Wiki Manuel">français</a>'
            "</div>"
        )

    def test_discovers_both_conventions(self):
        out = sw.find_translation_links_in_html(self._languages_html(), self.SEED)
        codes = [lang for lang, _ in out]
        titles = [title for _, title in out]
        self.assertIn("de", codes)
        self.assertIn("bg", codes)
        self.assertIn("fr", codes)
        self.assertIn("De:Gramps 6.0 Wiki Handbuch", titles)
        self.assertIn("Gramps 6.0 Wiki Manual/bg", titles)
        self.assertIn("Fr:Gramps 6.0 Wiki Manuel", titles)

    def test_sorted_by_lang_code(self):
        out = sw.find_translation_links_in_html(self._languages_html(), self.SEED)
        codes = [lang for lang, _ in out]
        self.assertEqual(codes, sorted(codes))

    def test_chapter_subpages_filtered_out(self):
        # A chapter-depth title (one " - " in the root) under an
        # index-depth seed (zero " - ") must be rejected.
        html = (
            '<a href="X" title="Gramps 6.0 Wiki Manual - Preface/bg">'
            "Preface (BG)</a>"
        )
        self.assertEqual(sw.find_translation_links_in_html(html, self.SEED), [])

    def test_non_translation_titles_ignored(self):
        # Body links to other English pages (no lang tag) must be ignored.
        html = (
            '<a href="X" title="Some Other Page">other</a>'
            '<a href="X" title="Gramps Glossary">glossary</a>'
        )
        self.assertEqual(sw.find_translation_links_in_html(html, self.SEED), [])

    def test_duplicate_titles_collapsed(self):
        # The Languages template might link the same translation twice
        # (top and bottom of page). We want one entry per unique title.
        html = (
            '<a href="X" title="De:Gramps 6.0 Wiki Handbuch">Deutsch</a>'
            '<a href="X" title="De:Gramps 6.0 Wiki Handbuch">Deutsch (bottom)</a>'
        )
        out = sw.find_translation_links_in_html(html, self.SEED)
        self.assertEqual(len(out), 1)
        self.assertEqual(out[0], ("de", "De:Gramps 6.0 Wiki Handbuch"))

    def test_empty_html(self):
        self.assertEqual(sw.find_translation_links_in_html("", self.SEED), [])

    def test_no_translations_present(self):
        # A page whose links are all chapter-style or non-translation.
        html = (
            '<a href="X" title="Gramps 6.0 Wiki Manual - Preface">Preface</a>'
            '<a href="X" title="Gramps 6.0 Wiki Manual - FAQ">FAQ</a>'
        )
        self.assertEqual(sw.find_translation_links_in_html(html, self.SEED), [])


# ---------------------------------------------------------------------------
#
# ResolveRedirectFallbackTests
#
# ---------------------------------------------------------------------------
class ResolveRedirectFallbackTests(unittest.TestCase):
    """The success path needs a live session; the failure path is testable
    via a tiny stub. Important: on ANY failure the helper must return the
    INPUT title, so the in-crawl is_redirect() detector still catches a
    redirect we couldn't resolve upfront."""

    def test_returns_input_on_session_exception(self):
        class FakeSession:
            api = "/wiki/api.php"

            class page:
                @staticmethod
                def evaluate(*a, **kw):
                    raise RuntimeError("simulated network failure")

        title = "Gramps 6.0 Wiki Manual/de"
        # silence the diagnostic print
        import io, contextlib

        with contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(sw.resolve_redirect(FakeSession(), title), title)


# ---------------------------------------------------------------------------
#
# FilterSeedsTests
#
# ---------------------------------------------------------------------------
class FilterSeedsTests(unittest.TestCase):
    """The --from / --only selection that drives mid-run resumes."""

    # Realistic seed shape: English (untagged), then alphabetical translations.
    SEEDS = [
        "Gramps 6.0 Wiki Manual",  # en
        "Gramps 6.0 Wiki Manual/bg",  # bg
        "Ca:Manual wiki per a Gramps 6.0",  # ca
        "Gramps 6.0 Wiki Manual/cs",  # cs
        "Gramps 6.0 Wiki Manual/da",  # da
        "De:Gramps 6.0 Wiki Handbuch",  # de
    ]

    def test_no_filter_passes_all_through(self):
        kept, skipped = sw.filter_seeds(self.SEEDS)
        self.assertEqual(kept, self.SEEDS)
        self.assertEqual(skipped, [])

    def test_resume_from_da(self):
        # The user's actual case: CF blew up mid-cs, resume at da.
        kept, skipped = sw.filter_seeds(self.SEEDS, resume_from="da")
        self.assertEqual([sw.lang_code_of(s) or "en" for s in kept], ["da", "de"])
        self.assertEqual(
            [sw.lang_code_of(s) or "en" for s in skipped], ["en", "bg", "ca", "cs"]
        )

    def test_resume_from_en_keeps_everything(self):
        kept, skipped = sw.filter_seeds(self.SEEDS, resume_from="en")
        self.assertEqual(kept, self.SEEDS)
        self.assertEqual(skipped, [])

    def test_resume_from_unknown_skips_everything(self):
        # If the resume code never matches, nothing is kept. The caller
        # (main) detects an empty kept list and prints a clear message.
        kept, skipped = sw.filter_seeds(self.SEEDS, resume_from="xx")
        self.assertEqual(kept, [])
        self.assertEqual(skipped, self.SEEDS)

    def test_only_single_code(self):
        kept, skipped = sw.filter_seeds(self.SEEDS, only={"de"})
        self.assertEqual([sw.lang_code_of(s) or "en" for s in kept], ["de"])
        self.assertEqual(len(skipped), 5)

    def test_only_multiple_codes(self):
        kept, _ = sw.filter_seeds(self.SEEDS, only={"de", "bg", "en"})
        self.assertEqual([sw.lang_code_of(s) or "en" for s in kept], ["en", "bg", "de"])

    def test_only_takes_precedence_over_resume_from(self):
        # When --only is set, --from is ignored (--only is the harder
        # whitelist).
        kept, _ = sw.filter_seeds(self.SEEDS, only={"bg"}, resume_from="da")
        self.assertEqual([sw.lang_code_of(s) or "en" for s in kept], ["bg"])

    def test_only_no_match_returns_empty(self):
        kept, skipped = sw.filter_seeds(self.SEEDS, only={"xx"})
        self.assertEqual(kept, [])
        self.assertEqual(skipped, self.SEEDS)


# ---------------------------------------------------------------------------
#
# IsEnqueueableTests
#
# ---------------------------------------------------------------------------
class IsEnqueueableTests(unittest.TestCase):
    """The pure scope-decision helper: prefix-based by default, depth-
    bounded when max_depth is set."""

    PREFIXES = ["Gramps 6.0 Wiki Manual"]

    # --- prefix mode (max_depth is None) -----------------------------------

    def test_prefix_mode_in_scope(self):
        self.assertTrue(
            sw.is_enqueueable(
                "Gramps 6.0 Wiki Manual - Preface",
                prefixes=self.PREFIXES,
                seed_lang=None,
                max_depth=None,
                depth=99,
            )
        )

    def test_prefix_mode_out_of_scope(self):
        self.assertFalse(
            sw.is_enqueueable(
                "Random Other Page",
                prefixes=self.PREFIXES,
                seed_lang=None,
                max_depth=None,
                depth=0,
            )
        )

    # --- depth mode (portal-style) ----------------------------------------

    def test_depth_mode_seed_at_depth_0_accepted(self):
        # A portal-style scrape: 'Portal:Developers' is the seed, depth=0.
        self.assertTrue(
            sw.is_enqueueable(
                "Portal:Developers",
                prefixes=["Portal:Developers"],
                seed_lang=None,
                max_depth=1,
                depth=0,
            )
        )

    def test_depth_mode_first_hop_accepted(self):
        # A page linked from the portal, disparate title. max_depth=1.
        self.assertTrue(
            sw.is_enqueueable(
                "Getting started with Gramps development",
                prefixes=["Portal:Developers"],
                seed_lang=None,
                max_depth=1,
                depth=1,
            )
        )

    def test_depth_mode_second_hop_rejected(self):
        # A page linked from a page linked from the portal -- exceeds budget.
        self.assertFalse(
            sw.is_enqueueable(
                "Some Subpage",
                prefixes=["Portal:Developers"],
                seed_lang=None,
                max_depth=1,
                depth=2,
            )
        )

    def test_depth_mode_cross_language_rejected(self):
        # Polish translation of the portal -- must not be followed even
        # though depth=1 is within budget.
        self.assertFalse(
            sw.is_enqueueable(
                "Pl:Portal:Developers",
                prefixes=["Portal:Developers"],
                seed_lang=None,
                max_depth=1,
                depth=1,
            )
        )

    def test_depth_mode_disparate_titles_accepted(self):
        # The whole point of depth mode: titles with NO common stem are in
        # scope as long as they're reachable within depth.
        for title in [
            "Debugging Gramps",
            "Using database API",
            "Programming guidelines",
            "Git tutorial",
        ]:
            self.assertTrue(
                sw.is_enqueueable(
                    title,
                    prefixes=["Portal:Developers"],
                    seed_lang=None,
                    max_depth=1,
                    depth=1,
                ),
                f"{title!r} should be enqueueable",
            )

    def test_depth_mode_seed_language_propagates(self):
        # If the seed itself is a translated portal ('Pl:Portal:Developers'),
        # the same-language scope applies in Polish: 'Pl:'-tagged pages
        # accepted, English ('Portal:Other') rejected.
        self.assertTrue(
            sw.is_enqueueable(
                "Pl:Foo",
                prefixes=["Pl:Portal:Developers"],
                seed_lang="pl",
                max_depth=1,
                depth=1,
            )
        )
        self.assertFalse(
            sw.is_enqueueable(
                "Portal:Other",
                prefixes=["Pl:Portal:Developers"],
                seed_lang="pl",
                max_depth=1,
                depth=1,
            )
        )


# ---------------------------------------------------------------------------
#
# IsRedirectTests
#
# ---------------------------------------------------------------------------
class IsRedirectTests(unittest.TestCase):
    def test_canonical_uppercase(self):
        self.assertTrue(sw.is_redirect("#REDIRECT [[Foo]]"))

    def test_lowercase(self):
        self.assertTrue(sw.is_redirect("#redirect [[Foo]]"))

    def test_mixed_case(self):
        self.assertTrue(sw.is_redirect("#Redirect [[Foo]]"))

    def test_leading_whitespace_tolerated(self):
        # MediaWiki itself doesn't tolerate this, but the API sometimes
        # returns content with a stray BOM or whitespace; be permissive.
        self.assertTrue(sw.is_redirect("  #REDIRECT [[Foo]]"))

    def test_redirect_word_in_body_is_not_a_redirect(self):
        self.assertFalse(sw.is_redirect("This page is not a #REDIRECT."))

    def test_real_content_not_a_redirect(self):
        self.assertFalse(sw.is_redirect("== Foo ==\n\nSome content."))

    def test_empty_string(self):
        self.assertFalse(sw.is_redirect(""))


# ---------------------------------------------------------------------------
#
# RewriteHtmlImgsTests
#
# ---------------------------------------------------------------------------
class RewriteHtmlImgsTests(unittest.TestCase):
    def test_basic_img(self):
        md = '<img src="Foo.png" alt="alt text" />'
        self.assertEqual(
            sw.rewrite_html_imgs(md, "_media"), "![[_media/Foo.png|alt text]]"
        )

    def test_img_without_alt(self):
        md = '<img src="Foo.png" />'
        self.assertEqual(sw.rewrite_html_imgs(md, "_media"), "![[_media/Foo.png]]")

    def test_img_with_filename_alt_suppressed(self):
        # Pandoc auto-fills alt with the filename when wikitext has no
        # caption; that's noise as a visible label.
        md = '<img src="Foo.png" alt="Foo.png" />'
        self.assertEqual(sw.rewrite_html_imgs(md, "_media"), "![[_media/Foo.png]]")

    def test_img_with_width_attr(self):
        md = '<img src="Foo.png" title="t" width="120" alt="Foo.png" />'
        # Width/title are dropped; alt matches filename so suppressed.
        self.assertEqual(sw.rewrite_html_imgs(md, "_media"), "![[_media/Foo.png]]")

    def test_external_img_left_alone(self):
        md = '<img src="https://example.com/foo.png" alt="x" />'
        self.assertEqual(sw.rewrite_html_imgs(md, "_media"), md)

    def test_attribute_order_independent(self):
        md = '<img alt="caption" src="Foo.png" />'
        self.assertEqual(
            sw.rewrite_html_imgs(md, "_media"), "![[_media/Foo.png|caption]]"
        )


# ---------------------------------------------------------------------------
#
# RewriteHtmlFiguresTests
#
# ---------------------------------------------------------------------------
class RewriteHtmlFiguresTests(unittest.TestCase):
    def test_figure_with_caption(self):
        md = (
            "<figure>\n"
            '<img src="Foo.png" title="t" width="120" />\n'
            "<figcaption>The Foo image</figcaption>\n"
            "</figure>"
        )
        self.assertEqual(
            sw.rewrite_html_figures(md, "_media"), "![[_media/Foo.png|The Foo image]]"
        )

    def test_figure_without_caption(self):
        md = "<figure>\n" '<img src="Foo.png" />\n' "</figure>"
        self.assertEqual(sw.rewrite_html_figures(md, "_media"), "![[_media/Foo.png]]")


# ---------------------------------------------------------------------------
#
# RewriteHtmlWikilinksTests
#
# ---------------------------------------------------------------------------
class RewriteHtmlWikilinksTests(unittest.TestCase):
    def test_basic_wikilink(self):
        md = '<a href="Gramps_Glossary" class="wikilink" title="Glossary">the glossary</a>'
        self.assertEqual(
            sw.rewrite_html_wikilinks(md), "[the glossary](wiki:Gramps_Glossary)"
        )

    def test_wikilink_with_anchor(self):
        md = '<a href="Gramps_Glossary#wiki" class="wikilink" title="Wiki">Wiki</a>'
        self.assertEqual(
            sw.rewrite_html_wikilinks(md), "[Wiki](wiki:Gramps_Glossary#wiki)"
        )

    def test_wikilink_to_media(self):
        # Media: prefix is preserved -- md2wiki re-emits it intact.
        md = '<a href=":Media:Foo.pdf" class="wikilink" title="t">Foo PDF</a>'
        self.assertEqual(
            sw.rewrite_html_wikilinks(md), "[Foo PDF](wiki::Media:Foo.pdf)"
        )

    def test_attribute_order_independent(self):
        md = '<a class="wikilink" href="X" title="Y">L</a>'
        self.assertEqual(sw.rewrite_html_wikilinks(md), "[L](wiki:X)")

    def test_anchor_only_link_stays_local(self):
        # In-page anchors don't go through 'wiki:'.
        md = '<a href="#section" class="wikilink">Section</a>'
        self.assertEqual(sw.rewrite_html_wikilinks(md), "[Section](#section)")

    def test_non_wikilink_anchor_untouched(self):
        # A plain external anchor without class="wikilink" stays as-is.
        md = '<a href="https://example.com">external</a>'
        self.assertEqual(sw.rewrite_html_wikilinks(md), md)


# ---------------------------------------------------------------------------
#
# CleanPandocHtmlPipelineTests
#
# ---------------------------------------------------------------------------
class CleanPandocHtmlPipelineTests(unittest.TestCase):
    def test_figure_then_img_then_wikilink(self):
        # End-to-end shape: a figure-wrapped image, a bare img, and a wikilink
        # all in one document, run through the same pipeline crawl() uses.
        md = (
            'Lead: <img src="Lead.jpg" width="120" alt="Lead.jpg" />\n\n'
            "<figure>\n"
            '<img src="Diagram.png" />\n'
            "<figcaption>An overview</figcaption>\n"
            "</figure>\n\n"
            'See <a href="Glossary" class="wikilink" title="Glossary">the glossary</a>.'
        )
        out = sw.clean_pandoc_html(md, "_media")
        self.assertIn("![[_media/Lead.jpg]]", out)
        self.assertIn("![[_media/Diagram.png|An overview]]", out)
        self.assertIn("[the glossary](wiki:Glossary)", out)
        # No raw HTML survives.
        self.assertNotIn("<img", out)
        self.assertNotIn("<figure", out)
        self.assertNotIn('class="wikilink"', out)


# ---------------------------------------------------------------------------
#
# TeeTests
#
# ---------------------------------------------------------------------------
class TeeTests(unittest.TestCase):
    def _make(self):
        import io

        a, b = io.StringIO(), io.StringIO()
        return a, b, sw._Tee(a, b)

    def test_writes_to_both_streams(self):
        a, b, tee = self._make()
        tee.write("hello\n")
        tee.write("world\n")
        self.assertEqual(a.getvalue(), "hello\nworld\n")
        self.assertEqual(b.getvalue(), "hello\nworld\n")

    def test_write_returns_length(self):
        # A file-like .write() returns the number of characters written;
        # builtins.print honours that contract on some Python builds.
        _, _, tee = self._make()
        self.assertEqual(tee.write("abc"), 3)

    def test_flush_propagates(self):
        # StringIO.flush() is a no-op but must not raise; just check that
        # the call goes through.
        _, _, tee = self._make()
        tee.flush()  # no exception is the assertion

    def test_isatty_follows_primary(self):
        import io

        class FakeTTY(io.StringIO):
            def isatty(self):
                return True

        primary = FakeTTY()
        secondary = io.StringIO()
        self.assertTrue(sw._Tee(primary, secondary).isatty())
        self.assertFalse(sw._Tee(secondary, primary).isatty())

    def test_isatty_empty(self):
        # Defensive: no streams shouldn't crash isatty().
        self.assertFalse(sw._Tee().isatty())


# ---------------------------------------------------------------------------
#
# RewriteMdWikiLinksTests
#
# ---------------------------------------------------------------------------
class RewriteMdWikiLinksTests(unittest.TestCase):
    """The HTML-fallback path emits internal links as `/wiki/index.php/Foo`;
    these need to become `wiki:Foo` to match md2wiki's round-trip form."""

    def test_index_php_form(self):
        md = "[Foo](/wiki/index.php/Foo)"
        self.assertEqual(sw.rewrite_md_wiki_links(md), "[Foo](wiki:Foo)")

    def test_short_form(self):
        # Some wikis omit '/index.php/' depending on rewrite rules.
        md = "[Foo](/wiki/Foo)"
        self.assertEqual(sw.rewrite_md_wiki_links(md), "[Foo](wiki:Foo)")

    def test_fragment_preserved(self):
        md = "[See section](/wiki/index.php/Foo#section)"
        self.assertEqual(
            sw.rewrite_md_wiki_links(md), "[See section](wiki:Foo#section)"
        )

    def test_query_string_stripped(self):
        # The 'edit this page' links carry a query; the round-trip form has
        # no place for them.
        md = "[edit](/wiki/index.php/Foo?action=edit)"
        self.assertEqual(sw.rewrite_md_wiki_links(md), "[edit](wiki:Foo)")

    def test_query_stripped_fragment_preserved(self):
        md = "[link](/wiki/index.php/Foo?action=edit#bar)"
        self.assertEqual(sw.rewrite_md_wiki_links(md), "[link](wiki:Foo#bar)")

    def test_external_link_untouched(self):
        md = "[external](https://example.com/foo)"
        self.assertEqual(sw.rewrite_md_wiki_links(md), md)


# ---------------------------------------------------------------------------
#
# CollapseLinkedImagesTests
#
# ---------------------------------------------------------------------------
class CollapseLinkedImagesTests(unittest.TestCase):
    """MW's HTML wraps inline images in a link to the file-description page;
    after pandoc that's `[![alt](src)](href)`. Obsidian renders the wrapping
    link rather than the embed."""

    def test_basic_linked_image(self):
        md = "[![alt](Foo.png)](/wiki/index.php/File:Foo.png)"
        self.assertEqual(sw.collapse_linked_images(md), "![alt](Foo.png)")

    def test_linked_image_with_title_attr(self):
        md = '[![alt](Foo.png "tooltip")](/wiki/index.php/File:Foo.png)'
        self.assertEqual(sw.collapse_linked_images(md), '![alt](Foo.png "tooltip")')

    def test_bare_image_untouched(self):
        md = "![alt](Foo.png)"
        self.assertEqual(sw.collapse_linked_images(md), md)

    def test_text_link_untouched(self):
        # A normal text-only link is not a linked image.
        md = "[label](/wiki/index.php/Foo)"
        self.assertEqual(sw.collapse_linked_images(md), md)


# ---------------------------------------------------------------------------
#
# ImageRefThumbnailTests
#
# ---------------------------------------------------------------------------
class ImageRefThumbnailTests(unittest.TestCase):
    """MW thumbnail filenames are '<size>px-<original>'; we always download
    the original via prop=images so the embed must point at the original
    name, not the thumbnail filename."""

    def test_thumb_in_url_resolves_to_original(self):
        md = "![alt](/wiki/images/thumb/4/4f/Foo.png/120px-Foo.png)"
        self.assertEqual(sw.rewrite_image_refs(md, "_media"), "![[_media/Foo.png|alt]]")

    def test_thumb_with_three_digit_size(self):
        md = "![](/wiki/images/thumb/a/b/Bar.jpg/240px-Bar.jpg)"
        self.assertEqual(sw.rewrite_image_refs(md, "_media"), "![[_media/Bar.jpg]]")

    def test_non_thumb_url_unchanged_basename(self):
        md = "![alt](/wiki/images/4/4f/Foo.png)"
        self.assertEqual(sw.rewrite_image_refs(md, "_media"), "![[_media/Foo.png|alt]]")

    def test_filename_starting_with_digits_not_treated_as_thumb(self):
        # '500px-Foo.png' = thumbnail. '500.png' = literal filename. The
        # regex requires '<digits>px-<rest>' specifically.
        md = "![](500.png)"
        self.assertEqual(sw.rewrite_image_refs(md, "_media"), "![[_media/500.png]]")


# ---------------------------------------------------------------------------
#
# PostProcessMdPipelineTests
#
# ---------------------------------------------------------------------------
class PostProcessMdPipelineTests(unittest.TestCase):
    """End-to-end shape covering HTML-fallback's output through the unified
    post-processor that BOTH paths use."""

    def test_html_fallback_shape(self):
        # Simulates what pandoc -f html -t gfm produces from MW HTML:
        # a linked image and an internal link side by side.
        md = (
            "See [![Diagram](/wiki/images/thumb/4/4f/Diagram.png/120px-Diagram.png)]"
            "(/wiki/index.php/File:Diagram.png) for the overview.\n\n"
            "Next: [the glossary](/wiki/index.php/Gramps_Glossary)."
        )
        out = sw.post_process_md(md, "_media")
        # Linked image -> bare embed pointing at the ORIGINAL (no thumb prefix)
        self.assertIn("![[_media/Diagram.png|Diagram]]", out)
        # /wiki/index.php/<page> -> wiki:<page>
        self.assertIn("[the glossary](wiki:Gramps_Glossary)", out)
        # No surviving wiki paths or thumb prefixes.
        self.assertNotIn("/wiki/", out)
        self.assertNotIn("120px-", out)


if __name__ == "__main__":
    unittest.main()
