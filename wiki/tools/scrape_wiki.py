#!/usr/bin/env python3
"""scrape_wiki -- mirror a section of the Gramps wiki into pages/ as Markdown.

One-way, OTHER direction from publish.py: wiki -> repo. Reads through the same
attached-Chrome rig as wikitransport.py so it rides your cleared cf_clearance
session; runs on your workstation, not CI.

The BFS:
  * Start at --seed (default 'Gramps 6.0 Wiki Manual').
  * Follow main-namespace links via prop=links, restricted to titles matching
    one of the --prefix scopes (default: the seed itself).
  * For each in-scope page: fetch wikitext (revisions/main), categories, and
    image titles; normalise localised File-namespace aliases; pandoc
    -f mediawiki -t gfm; write to <target>/<slug>.md with YAML front-matter.
  * For each image referenced by an in-scope page: resolve via prop=imageinfo,
    fetch bytes (Playwright APIRequestContext shares the cleared cookies),
    save under <target>/<media-subdir>/.

Translations:
  The Gramps wiki names translated pages with a title prefix like 'De:' or
  'Fr:' (e.g. 'De:Gramps 6.0 Wiki Handbuch'). scrape_wiki auto-detects this
  prefix from --seed and routes output to <target>/<lang>/ so translations
  don't collide. To scrape German: --seed "De:Gramps 6.0 Wiki Handbuch".
  The same prefix scopes the crawl, so cross-language links are skipped.

  Image namespace aliases (Datei, Bild, Fichier, ...) are normalised to the
  canonical 'File:' BEFORE pandoc, because pandoc's mediawiki reader only
  recognises 'File' / 'Image' for embeds.

Round-trip-friendly image rewriting:
  pandoc emits image refs roughly as `![alt](File:Foo.png)` or with the file:
  URI form. We rewrite those to Obsidian-native embeds: `![[_media/Foo.png|alt]]`
  (or without `|alt` when alt is empty). A future md2wiki extension can
  translate `![[_media/Foo.png|alt]]` back to `[[File:Foo.png|alt]]` for the
  wikitext output, with the publisher uploading the bytes through the same
  session. For now the bytes live next to the markdown and Obsidian renders
  the embed natively.

Resume:
  Per-page sidecars in --state-dir record the upstream revid. A re-run with
  unchanged upstream revid SKIPs the rewrite but still walks links (so newly
  added subpages on an already-mirrored ToC get picked up). Per-image sidecars
  record sha1 from imageinfo; matching sha1 + existing file = skip.

Usage:
  python3 scrape_wiki.py                                          # English
  python3 scrape_wiki.py --seed "De:Gramps 6.0 Wiki Handbuch"     # German
  python3 scrape_wiki.py --seed "Gramps 6.0 Wiki Manual" --max-pages 100
  python3 scrape_wiki.py --prefix "Gramps 6.0 Wiki Manual" \\
                        --prefix "Addons development"             # broaden scope
  python3 scrape_wiki.py --no-login                                # warm session
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import time
from collections import deque
from dataclasses import dataclass, field
from typing import Iterable

import yaml

import wikitransport

# ---- defaults ---------------------------------------------------------------

SEED_TITLE = "Gramps 6.0 Wiki Manual"
DEFAULT_TARGET = "pages/03 - User guide"
DEFAULT_MEDIA_SUBDIR = "_media"
DEFAULT_STATE_DIR = ".wikiscrape"
DEFAULT_MAX_PAGES = 500
DEFAULT_DELAY_S = 0.2  # polite gap between API calls
MAX_PAGES_HARD_CAP = 2000

# ---- JS snippets ------------------------------------------------------------
# Same shape as wikitransport's: same-origin fetch from a page on the wiki
# origin, JSON in / JSON out, Cloudflare challenge detection in the failure
# path.

_JS_LINKS = r"""
async (cfg) => {
  let out = [];
  let cont = null;
  for (let i = 0; i < 100; i++) {
    let u = cfg.api
      + '?action=query&prop=links&plnamespace=0&pllimit=max'
      + '&format=json&formatversion=2'
      + '&titles=' + encodeURIComponent(cfg.title);
    if (cont) u += '&plcontinue=' + encodeURIComponent(cont);
    const r = await fetch(u, { credentials:'same-origin',
                               headers:{ Accept:'application/json' } });
    const t = await r.text();
    let j;
    try { j = JSON.parse(t); }
    catch { return { ok:false,
                     challenge:/cloudflare|just a moment|cf-chl/i.test(t),
                     raw:t.slice(0,400) }; }
    const page = (j.query && j.query.pages && j.query.pages[0]) || {};
    if (page.links) for (const l of page.links) out.push(l.title);
    if (j.continue && j.continue.plcontinue) cont = j.continue.plcontinue;
    else break;
  }
  return { ok:true, links: out };
}
"""

_JS_IMAGES = r"""
async (cfg) => {
  let out = [];
  let cont = null;
  for (let i = 0; i < 50; i++) {
    let u = cfg.api
      + '?action=query&prop=images&imlimit=max'
      + '&format=json&formatversion=2'
      + '&titles=' + encodeURIComponent(cfg.title);
    if (cont) u += '&imcontinue=' + encodeURIComponent(cont);
    const r = await fetch(u, { credentials:'same-origin',
                               headers:{ Accept:'application/json' } });
    const t = await r.text();
    let j;
    try { j = JSON.parse(t); }
    catch { return { ok:false,
                     challenge:/cloudflare|just a moment|cf-chl/i.test(t),
                     raw:t.slice(0,400) }; }
    const page = (j.query && j.query.pages && j.query.pages[0]) || {};
    if (page.images) for (const im of page.images) out.push(im.title);
    if (j.continue && j.continue.imcontinue) cont = j.continue.imcontinue;
    else break;
  }
  return { ok:true, images: out };
}
"""

_JS_CATEGORIES = r"""
async (cfg) => {
  let out = [];
  let cont = null;
  for (let i = 0; i < 20; i++) {
    let u = cfg.api
      + '?action=query&prop=categories&cllimit=max'
      + '&format=json&formatversion=2'
      + '&titles=' + encodeURIComponent(cfg.title);
    if (cont) u += '&clcontinue=' + encodeURIComponent(cont);
    const r = await fetch(u, { credentials:'same-origin',
                               headers:{ Accept:'application/json' } });
    const t = await r.text();
    let j;
    try { j = JSON.parse(t); }
    catch { return { ok:false,
                     challenge:/cloudflare|just a moment|cf-chl/i.test(t),
                     raw:t.slice(0,400) }; }
    const page = (j.query && j.query.pages && j.query.pages[0]) || {};
    if (page.categories) for (const c of page.categories)
      out.push(c.title.replace(/^Category:/,''));
    if (j.continue && j.continue.clcontinue) cont = j.continue.clcontinue;
    else break;
  }
  return { ok:true, categories: out };
}
"""

_JS_RESOLVE_REDIRECT = r"""
async (cfg) => {
  // action=query with redirects=1 transparently follows a redirect chain
  // and returns the FINAL title (after normalisation + redirect chasing) on
  // the page object. We don't need any prop -- the title alone is enough.
  const u = cfg.api
    + '?action=query&redirects=1&format=json&formatversion=2'
    + '&titles=' + encodeURIComponent(cfg.title);
  const r = await fetch(u, { credentials:'same-origin',
                             headers:{ Accept:'application/json' } });
  const t = await r.text();
  let j;
  try { j = JSON.parse(t); }
  catch { return { ok:false,
                   challenge:/cloudflare|just a moment|cf-chl/i.test(t),
                   raw:t.slice(0,400) }; }
  if (!j.query || !Array.isArray(j.query.pages) || j.query.pages.length === 0)
    return { ok:true, title: cfg.title, redirected: false };
  const page = j.query.pages[0];
  const followed = (j.query.redirects || []).length > 0;
  return { ok:true, title: page.title || cfg.title, redirected: followed };
}
"""

_JS_PARSE_HTML = r"""
async (cfg) => {
  // action=parse&prop=text returns the already-rendered HTML for a page,
  // which we use as a fallback when pandoc's mediawiki reader chokes on the
  // raw wikitext. The MW parser handles every malformed construct that
  // exists in the live wiki, by definition.
  const u = cfg.api
    + '?action=parse&prop=text&format=json&formatversion=2'
    + '&page=' + encodeURIComponent(cfg.title);
  const r = await fetch(u, { credentials:'same-origin',
                             headers:{ Accept:'application/json' } });
  const t = await r.text();
  let j;
  try { j = JSON.parse(t); }
  catch { return { ok:false,
                   challenge:/cloudflare|just a moment|cf-chl/i.test(t),
                   raw:t.slice(0,400) }; }
  if (j.error)
    return { ok:false, raw:'API error: ' + JSON.stringify(j.error) };
  if (!j.parse || j.parse.text === undefined)
    return { ok:false, raw:'unexpected parse response shape' };
  return { ok:true, text: j.parse.text };
}
"""

_JS_IMAGEINFO = r"""
async (cfg) => {
  const u = cfg.api
    + '?action=query&prop=imageinfo&iiprop=url|sha1|mime'
    + '&format=json&formatversion=2'
    + '&titles=' + encodeURIComponent(cfg.title);
  const r = await fetch(u, { credentials:'same-origin',
                             headers:{ Accept:'application/json' } });
  const t = await r.text();
  let j;
  try { j = JSON.parse(t); }
  catch { return { ok:false,
                   challenge:/cloudflare|just a moment|cf-chl/i.test(t),
                   raw:t.slice(0,400) }; }
  const page = (j.query && j.query.pages && j.query.pages[0]) || {};
  if (page.missing || !page.imageinfo) return { ok:true, exists:false };
  const ii = page.imageinfo[0];
  return { ok:true, exists:true, url: ii.url, sha1: ii.sha1, mime: ii.mime };
}
"""


def _eval(session, js: str, **extra):
    """Same shape as WikiSession._eval but takes arbitrary JS."""
    cfg = {"api": session.api, **extra}
    res = session.page.evaluate(js, cfg)
    if not res.get("ok"):
        if res.get("challenge"):
            raise RuntimeError(
                "Cloudflare challenged the XHR -- session not cleared. "
                "Open the wiki in the Chrome window, pass the challenge, retry."
            )
        raise RuntimeError(f"API call failed: {res}")
    return res


def list_links(session, title: str) -> list[str]:
    return _eval(session, _JS_LINKS, title=title)["links"]


def list_images(session, title: str) -> list[str]:
    return _eval(session, _JS_IMAGES, title=title)["images"]


def list_categories(session, title: str) -> list[str]:
    return _eval(session, _JS_CATEGORIES, title=title)["categories"]


def parse_html_text(session, title: str) -> str:
    """Fetch the page's already-rendered HTML via action=parse&prop=text.
    The HTML is what MediaWiki itself produced from the wikitext; using it as
    the conversion source bypasses pandoc's mediawiki reader entirely."""
    return _eval(session, _JS_PARSE_HTML, title=title)["text"]


def resolve_redirect(session, title: str) -> str:
    """Return the canonical title after following any redirect chain. Used at
    seed entry so that '/lang' seeds (which on the Gramps wiki redirect to
    'Xx:'-style canonical titles like 'De:Gramps 6.0 Wiki Handbuch') drive
    a meaningful crawl. On any API failure, fall back to the input title --
    the in-crawl is_redirect() check will still catch a redirect we couldn't
    resolve upfront, and the user gets a clean 'redirect; skipping' log line."""
    try:
        r = _eval(session, _JS_RESOLVE_REDIRECT, title=title)
        return r.get("title") or title
    except Exception as e:
        print(f"resolve_redirect({title!r}) failed: {e}")
        return title


# Discover translation seed titles by parsing the rendered HTML of the seed
# page. The Gramps wiki uses the {{Languages}} template at the top of each
# manual page, which expands into a row of anchors whose href / title point
# at SAME-wiki translation pages (NOT interwiki, so prop=langlinks returns
# nothing). The translation titles use either of the two conventions we
# already detect: 'De:Foo' prefix or 'Foo/bg' suffix.
_HTML_LINK_TITLE_RE = re.compile(
    r'<a[^>]*\btitle="(?P<title>[^"]+)"[^>]*>', re.IGNORECASE
)


def find_translation_links_in_html(html: str, seed: str) -> list[tuple[str, str]]:
    """Pure: scan HTML, return sorted [(lang_code, title), ...] for unique
    translation-tagged titles whose chapter depth matches the seed's. The
    depth filter is what separates index pages (the seed's siblings in other
    languages) from chapter sub-pages (e.g. 'Gramps 6.0 Wiki Manual - Preface/bg'
    has depth 1; the seed has depth 0 so it's filtered out)."""
    seed_depth = title_root(seed).count(" - ")
    seen: set[str] = set()
    found: list[tuple[str, str]] = []
    for m in _HTML_LINK_TITLE_RE.finditer(html):
        title = m.group("title").strip()
        if title in seen:
            continue
        seen.add(title)
        lang = lang_code_of(title)
        if not lang:
            continue
        if title_root(title).count(" - ") != seed_depth:
            continue
        found.append((lang, title))
    found.sort()
    return found


def filter_seeds(
    seeds: list[str],
    *,
    only: set[str] | None = None,
    resume_from: str | None = None,
) -> tuple[list[str], list[str]]:
    """Apply --only / --from selection to a seed list. Returns
    (kept_seeds, skipped_seeds_for_display).

    Rules:
      * `only` (when set) is a hard whitelist on lang codes; --from is ignored.
      * `resume_from` skips every seed before the first whose lang code
        matches, then keeps everything from that point on.
      * Both treat the no-tag English seed as code 'en'.
      * If neither is given, returns (seeds, []) unchanged.
    """
    if only is not None:
        kept, skipped = [], []
        for s in seeds:
            (kept if (lang_code_of(s) or "en") in only else skipped).append(s)
        return kept, skipped
    if resume_from:
        kept, skipped, hit = [], [], False
        for s in seeds:
            code = lang_code_of(s) or "en"
            if not hit:
                if code == resume_from:
                    hit = True
                    kept.append(s)
                else:
                    skipped.append(s)
            else:
                kept.append(s)
        return kept, skipped
    return list(seeds), []


def discover_translations(session, seed: str) -> list[tuple[str, str]]:
    """Live-session discovery: fetch the seed's rendered HTML, parse out
    translation-shaped links, follow any redirects to land on canonical
    titles. Returns sorted [(lang_code, canonical_title), ...].

    Redirect resolution at discovery time means the Gramps wiki's '/lang'
    redirects to 'Xx:'-style canonical titles are transparent: the user sees
    (and --all-translations drives) the canonical title, which has the
    right root for the scope filter."""
    try:
        html = parse_html_text(session, seed)
    except Exception as e:
        print(f"Translation discovery: failed to fetch HTML " f"for {seed!r}: {e}")
        return []
    raw = find_translation_links_in_html(html, seed)
    resolved: list[tuple[str, str]] = []
    seen_titles: set[str] = set()
    for lang, title in raw:
        canon = resolve_redirect(session, title)
        # Recompute lang code post-resolution -- a /de redirect resolving to
        # 'De:Gramps 6.0 Wiki Handbuch' still gives 'de' through the prefix
        # detector, so the routing stays consistent.
        canon_lang = lang_code_of(canon) or lang
        if canon in seen_titles:
            continue
        seen_titles.add(canon)
        resolved.append((canon_lang, canon))
    resolved.sort()
    return resolved


def image_url(session, title: str) -> dict | None:
    r = _eval(session, _JS_IMAGEINFO, title=title)
    return (
        {"url": r["url"], "sha1": r.get("sha1"), "mime": r.get("mime")}
        if r.get("exists")
        else None
    )


def fetch_binary(session, url: str) -> bytes:
    """Pull a binary URL through the same browser context's cookies."""
    resp = session.page.request.get(url)
    if not resp.ok:
        raise RuntimeError(f"GET {url} -> HTTP {resp.status}")
    return resp.body()


# ---- pure helpers (covered by test_scrape_wiki.py) --------------------------

_SLUG_RE = re.compile(r"[^A-Za-z0-9._-]+")

# A title prefix like "De:" / "Fr:" / "Es:" -- the Gramps wiki's convention for
# translated pages. Two-letter form is what's actually used today; if a wiki
# ever adopts a longer code (ISO 639-3) the regex would need widening.
_LANG_PREFIX_RE = re.compile(r"^(?P<code>[A-Z][a-z]):")

# Localised aliases for the File namespace. pandoc's mediawiki reader only
# recognises 'File' and 'Image'; everything else degrades from an embed to a
# plain link. Normalising in the wikitext BEFORE pandoc keeps embeds intact.
# List drawn from MediaWiki's defaultmessages for the File namespace across
# the languages the Gramps wiki currently translates into; extend as needed.
_FILE_ALIASES = [
    "File",
    "Image",
    "Datei",
    "Bild",  # German
    "Fichier",  # French
    "Imagen",
    "Archivo",  # Spanish
    "Tiedosto",
    "Kuva",  # Finnish
    "Plik",  # Polish
    "Bestand",
    "Afbeelding",  # Dutch
    "Fil",  # Danish / Swedish / Norwegian
    "Soubor",
    "Obrázek",  # Czech
    "Файл",  # Russian / Ukrainian / Belarusian / Bulgarian
    "Datoteka",
    "Slika",  # Croatian / Slovenian / Serbian
]
_FILE_ALIAS_LINK_RE = re.compile(
    r"(\[\[\s*)(?:" + "|".join(re.escape(a) for a in _FILE_ALIASES) + r")(\s*:)",
    re.IGNORECASE,
)


def lang_from_title(title: str) -> str | None:
    """'De:Gramps 6.0 Wiki Handbuch' -> 'de'. 'Gramps 6.0 Wiki Manual' -> None."""
    m = _LANG_PREFIX_RE.match(title)
    return m.group("code").lower() if m else None


# Trailing '/<lang-code>' on a title is the Gramps wiki's OTHER translation
# convention: 'Gramps 6.0 Wiki Manual/bg' (Bulgarian) versus the 'De:'-style
# prefix used by other languages. Without a guard this leaks translations
# into an English scrape via the '/' subpage joiner in in_scope.
#
# Locale forms observed on the live wiki:
#   /bg                    - simple ISO 639-1 (most common)
#   /pt-br /zh-hans        - BCP47 with hyphen-separated region
#   /pt PT  /zh CN         - a malformed-but-real space-separated variant
# The pattern is permissive on the region tail; the lowercase-first-letter
# requirement keeps real chapter names like /FAQ or /Editing safe.
_LANG_SUBPATH_RE = re.compile(r"/(?P<code>[a-z]{2,3}(?:[-_ ][a-zA-Z]{2,4})?)$")


def lang_subpath_of(title: str) -> str | None:
    """'Foo/bg' -> 'bg', 'Foo/pt-br' -> 'pt-br', 'Foo/pt PT' -> 'pt PT'.
    'Foo/FAQ' -> None (uppercase first letter)."""
    m = _LANG_SUBPATH_RE.search(title)
    return m.group("code") if m else None


def lang_code_of(title: str) -> str | None:
    """The language code on this title via EITHER convention used on the
    Gramps wiki:
      * 'De:Foo' (prefix namespace, used by e.g. German, French, Spanish)
        -> 'de'
      * 'Foo/bg' (suffix subpath, used by e.g. Bulgarian, Catalan, Czech)
        -> 'bg'
    Returns the lowercase code, or None for English / untagged titles."""
    return lang_from_title(title) or lang_subpath_of(title)


def title_root(title: str) -> str:
    """Strip the language tag from EITHER end so the remaining 'English root'
    can be compared across languages. 'De:Foo' -> 'Foo', 'Foo/bg' -> 'Foo'.

    Untagged titles pass through unchanged.
    """
    pref = lang_from_title(title)
    if pref:
        return title[len(pref) + 1 :]  # strip 'Xx:'
    suff = lang_subpath_of(title)
    if suff:
        return title[: -(len(suff) + 1)]  # strip '/xx'
    return title


# Pandoc lowercases the #REDIRECT magic word; MediaWiki itself is case-
# insensitive on the leading directive but is otherwise picky about syntax
# (must be the first non-whitespace token). Localised forms exist (e.g.
# Spanish '#REDIRECCIÓN', German '#WEITERLEITUNG') but the Gramps wiki uses
# the canonical English form for its redirect entries, so matching '#REDIRECT'
# covers what we actually see.
_REDIRECT_RE = re.compile(r"^\s*#REDIRECT\b", re.IGNORECASE)


def is_redirect(wikitext: str) -> bool:
    return bool(_REDIRECT_RE.match(wikitext or ""))


def normalise_file_links(wikitext: str) -> str:
    """Rewrite '[[Datei:Foo.png|...]]' (and other localised aliases) to
    '[[File:Foo.png|...]]' so pandoc recognises the embed."""
    return _FILE_ALIAS_LINK_RE.sub(lambda m: m.group(1) + "File" + m.group(2), wikitext)


def title_to_slug(title: str, *, strip_prefix: str | None = None) -> str:
    """Stable, human-readable filename derived from a wiki title.

    Optionally drops a leading prefix (and any ' - '/' '/'-' joiner) so
    'Gramps 6.0 Wiki Manual - Getting started' becomes 'getting-started'.
    """
    t = title
    if strip_prefix and t.startswith(strip_prefix):
        t = t[len(strip_prefix) :].lstrip(" -/")
    if not t.strip():
        t = title  # don't collapse to empty if the title IS the prefix
    t = re.sub(r"\s+", "-", t.strip())
    t = _SLUG_RE.sub("-", t)
    t = re.sub(r"-+", "-", t).strip("-").lower()
    return t or "index"


def image_title_to_filename(title: str) -> str:
    """'File:Foo Bar.png' or 'Datei:Foo Bar.png' -> 'Foo_Bar.png'.

    Strips ANY single-colon namespace prefix, not just 'File:', so localised
    aliases (Datei, Bild, Fichier, ...) all collapse to the bare filename.
    """
    _, _, name = title.partition(":") if ":" in title else ("", "", title)
    if not name:
        name = title
    return re.sub(r"\s+", "_", name.strip())


def in_scope(title: str, prefixes: Iterable[str]) -> bool:
    """A page is in scope if its title equals a prefix, or extends one with
    '/' (subpages) or ' - ' (the Gramps wiki's hyphenated chapter convention)
    -- AFTER stripping any language tag from both sides.

    Comparing roots (not raw titles) means:
      * Prefix-style translations ('De:Foo - Vorwort' under seed 'De:Foo')
        match through the strip.
      * Suffix-style translations ('Foo - Preface/bg' under seed 'Foo/bg')
        match too -- the language tag and the ' - ' joiner don't collide
        because the lang suffix sits outside the root before comparison.
      * Cross-language titles ('Foo/bg' under English seed 'Foo') are
        rejected because the lang codes don't match.
    """
    title_lang = lang_code_of(title)
    title_r = title_root(title)
    for p in prefixes:
        p_lang = lang_code_of(p)
        if title_lang != p_lang:
            continue  # different language than this prefix; not its concern
        p_r = title_root(p)
        if (
            title_r == p_r
            or title_r.startswith(p_r + " - ")
            or title_r.startswith(p_r + "/")
        ):
            return True
    return False


# Pandoc -t gfm on wiki image embeds normally produces:
#   ![alt](Basename.ext "alt")
# i.e. it strips the 'File:' prefix and normalises spaces to underscores. We
# also defensively handle the variants where the prefix survives, and exclude
# external URLs so remote-hosted images aren't ferried into _media/.
#   ![alt](Foo_Bar.png "tooltip")        <- the common pandoc output
#   ![alt](File:Foo_Bar.png)             <- defensive: surviving namespace
#   ![alt](File:Foo Bar.png)             <- defensive: surviving namespace+space
#   ![remote](https://...)               <- LEFT ALONE
_IMG_REF_RE = re.compile(
    r"!\[(?P<alt>[^\]]*)\]\("
    r'(?P<target>(?!https?:|//)[^)\s"]+)'  # not a URL
    r'(?:\s+"[^"]*")?'  # optional pandoc title attr
    r"\)"
)


def rewrite_image_refs(md: str, media_subdir: str) -> str:
    def sub(m: re.Match) -> str:
        alt = m.group("alt").strip()
        target = m.group("target").strip()
        # Strip a surviving 'File:'/'file:' namespace if present. Pandoc
        # usually drops it, but be tolerant.
        if ":" in target and target.split(":", 1)[0].lower() in ("file", "image"):
            target = target.split(":", 1)[1]
        # Defensive basename: a wiki image title never contains '/', but if
        # pandoc ever emits a path-shaped target we don't want it mounted at
        # an unexpected place under _media/. This also handles MW's full
        # image URLs from the HTML-fallback path (/wiki/images/x/y/Foo.png).
        name = os.path.basename(target.replace("%20", " "))
        name = _strip_thumb_prefix(name)
        name = re.sub(r"\s+", "_", name)
        body = f"{media_subdir}/{name}"
        return f"![[{body}|{alt}]]" if alt else f"![[{body}]]"

    return _IMG_REF_RE.sub(sub, md)


# HTML-fallback path: pandoc -f html emits internal links as
# `[label](/wiki/index.php/Foo)` or `[label](/wiki/Foo)`, with an optional
# `"title"` attribute when the source <a> carried a title. Convert to the
# md2wiki round-trip convention `[label](wiki:Foo)` and drop the title (it's
# redundant with the visible label and md2wiki has no place for it).
_MD_WIKI_PATH_LINK_RE = re.compile(
    r"\[(?P<label>[^\]]*)\]\("
    r'(?P<href>/wiki/(?:index\.php/)?(?P<page>[^)\s"]+))'
    r'(?:\s+"[^"]*")?'
    r"\)"
)


def rewrite_md_wiki_links(md: str) -> str:
    def sub(m: re.Match) -> str:
        page = m.group("page")
        # Strip an action query string ('?action=edit'); preserve a #fragment.
        page = re.sub(r"\?[^#]*", "", page)
        return f"[{m.group('label')}](wiki:{page})"

    return _MD_WIKI_PATH_LINK_RE.sub(sub, md)


# MW's HTML wraps every inline image in an <a> linking to the file-description
# page. After pandoc, that's `[![alt](src)](/wiki/.../File:Foo.png)` -- a link
# wrapping an embed. Obsidian renders the wrapping link rather than the embed,
# which isn't what we want. Drop the wrapper and keep the embed.
_LINKED_IMG_RE = re.compile(
    r'\[(?P<embed>!\[[^\]]*\]\([^)]+(?:\s+"[^"]*")?\))\]\([^)]+\)'
)


def collapse_linked_images(md: str) -> str:
    return _LINKED_IMG_RE.sub(lambda m: m.group("embed"), md)


# Pandoc -t gfm passes through raw HTML for several mediawiki constructs that
# have no clean markdown equivalent: sized image embeds ([[File:Foo|120px]]),
# captioned embeds, and internal links. The result is markdown littered with
# <img>, <figure>, and <a class="wikilink">. Rewrite each to an
# Obsidian-native or md2wiki-roundtrip-compatible form.

_ATTR_RE = re.compile(r'(\w+)\s*=\s*"([^"]*)"')

# MW thumbnail filenames are '<size>px-<original>' (e.g. '120px-Foo.png');
# the original is what we download via prop=images. Rewrite to the original
# name so the embed resolves. Lives at module scope because both the raw-
# HTML <img> rewriter and the markdown-image rewriter need it.
_THUMB_PREFIX_RE = re.compile(r"^\d+px-(.+)")


def _strip_thumb_prefix(name: str) -> str:
    m = _THUMB_PREFIX_RE.match(name)
    return m.group(1) if m else name


_HTML_FIGURE_RE = re.compile(
    r"<figure>\s*(?P<img><img\s[^>]+?/?>)\s*"
    r"(?:<figcaption>(?P<caption>.*?)</figcaption>)?\s*</figure>",
    re.DOTALL,
)
_HTML_IMG_RE = re.compile(r"<img\s+(?P<attrs>[^>]+?)/?>")
_HTML_WIKILINK_RE = re.compile(
    r'<a\s+(?P<attrs>[^>]*\bclass="wikilink"[^>]*)>' r"(?P<label>.*?)</a>",
    re.DOTALL,
)


def _img_attrs_to_embed(
    attrs_str: str, media_subdir: str, caption: str | None = None
) -> str | None:
    """Turn an <img> tag's attributes (and optional figure caption) into an
    Obsidian embed. Returns None if the src is external or missing -- in
    which case the caller should leave the raw HTML untouched."""
    attrs = dict(_ATTR_RE.findall(attrs_str))
    src = attrs.get("src", "")
    if not src or src.startswith(("http://", "https://", "//")):
        return None
    name = os.path.basename(src.replace("%20", " "))
    name = _strip_thumb_prefix(name)
    name = re.sub(r"\s+", "_", name)
    # Caption wins over alt (more descriptive); alt wins over title (title is
    # often the auto-derived filename which is noise as a visible label).
    label = (caption or attrs.get("alt") or "").strip()
    # Filter the noisy "Foo.png" auto-label pandoc generates when the wikitext
    # had no caption.
    if label.lower() == name.lower() or label == attrs.get("title", "") == name:
        label = ""
    body = f"{media_subdir}/{name}"
    return f"![[{body}|{label}]]" if label else f"![[{body}]]"


def rewrite_html_figures(md: str, media_subdir: str) -> str:
    def sub(m: re.Match) -> str:
        # Pull attrs off the inner <img> by re-matching, rather than fiddling
        # with the raw tag string -- attribute order isn't fixed and
        # string-slicing the tag fence is fragile.
        inner = _HTML_IMG_RE.search(m.group("img"))
        if inner is None:
            return m.group(0)
        replacement = _img_attrs_to_embed(
            inner.group("attrs"),
            media_subdir,
            caption=m.group("caption"),
        )
        return replacement if replacement is not None else m.group(0)

    return _HTML_FIGURE_RE.sub(sub, md)


def rewrite_html_imgs(md: str, media_subdir: str) -> str:
    def sub(m: re.Match) -> str:
        replacement = _img_attrs_to_embed(m.group("attrs"), media_subdir)
        return replacement if replacement is not None else m.group(0)

    return _HTML_IMG_RE.sub(sub, md)


def rewrite_html_wikilinks(md: str) -> str:
    """`<a href="X" class="wikilink" title="Y">L</a>` -> `[L](wiki:X)`.

    Matches md2wiki's authored form, so pushing back through publish.py
    produces a real `[[X|L]]` wikitext link. The title attribute is dropped
    -- it's redundant with the visible label and md2wiki doesn't use it.
    """

    def sub(m: re.Match) -> str:
        attrs = dict(_ATTR_RE.findall(m.group("attrs")))
        href = attrs.get("href", "").strip()
        label = m.group("label").strip()
        if not href:
            return m.group(0)
        # Anchor-only links (#section) stay as plain markdown anchors.
        if href.startswith("#"):
            return f"[{label}]({href})"
        return f"[{label}](wiki:{href})"

    return _HTML_WIKILINK_RE.sub(sub, md)


def clean_pandoc_html(md: str, media_subdir: str) -> str:
    """Run all post-pandoc HTML cleanups in the correct order: figures
    (which wrap <img>) before bare <img>, then wikilinks."""
    md = rewrite_html_figures(md, media_subdir)
    md = rewrite_html_imgs(md, media_subdir)
    md = rewrite_html_wikilinks(md)
    return md


def post_process_md(md: str, media_subdir: str) -> str:
    """The shared post-pandoc pipeline -- runs against output from EITHER the
    wikitext path or the HTML-fallback path. Order matters: collapse linked
    images BEFORE rewriting wiki links (else we'd rewrite the wrapping link
    and then collapse on a different shape); rewrite image refs LAST so the
    HTML-residue cleanups can't introduce new image refs that miss the pass."""
    md = collapse_linked_images(md)
    md = rewrite_md_wiki_links(md)
    md = clean_pandoc_html(md, media_subdir)
    md = rewrite_image_refs(md, media_subdir)
    return md


# Result of a successful convert: the markdown body + a marker for which path
# produced it. The marker rides through to the page's front-matter so a
# curator can see at a glance which pages came through the lossy fallback.
CONVERT_WIKITEXT = "wikitext"
CONVERT_HTML_FALLBACK = "html-fallback"


def try_convert_page(
    session, title: str, wikitext: str, media_subdir: str
) -> tuple[str, str]:
    """Convert a page's content to markdown, falling back from the wikitext
    reader to the HTML reader if pandoc rejects the wikitext.

    Returns (markdown_body, method) where method is one of CONVERT_WIKITEXT
    or CONVERT_HTML_FALLBACK. Raises RuntimeError only if BOTH paths fail --
    the caller treats that as a per-page conversion failure (wikitext is
    still captured under .wikiscrape/failed/ for offline diagnosis).
    """
    try:
        md = wikitext_to_md(wikitext)
        return post_process_md(md, media_subdir), CONVERT_WIKITEXT
    except Exception as wt_err:
        try:
            html = parse_html_text(session, title)
            md = html_to_md(html)
            return post_process_md(md, media_subdir), CONVERT_HTML_FALLBACK
        except Exception as html_err:
            raise RuntimeError(
                f"both conversion paths failed -- "
                f"mediawiki: {wt_err}; html: {html_err}"
            ) from html_err


def wikitext_to_md(wikitext: str) -> str:
    proc = subprocess.run(
        ["pandoc", "-f", "mediawiki", "-t", "gfm", "--wrap=none"],
        input=normalise_file_links(wikitext),
        capture_output=True,
        text=True,
    )
    if proc.returncode != 0:
        raise RuntimeError(f"pandoc failed: {proc.stderr.strip()}")
    return proc.stdout


# MW's rendered HTML carries chrome we don't want in the markdown body:
#   * [edit] section links pandoc passes through as literal "[edit]"
#   * the auto-generated table of contents (we'd rather let the reader's
#     navigation handle this; the markdown already shows the heading tree)
#   * <a class="image"> wrappers around inline images, which pandoc can't
#     convert and otherwise survive as raw HTML in the markdown output
#   * the outermost <div class="mw-parser-output"> wrapper -- pure noise
# Strip them before handing the HTML to pandoc -f html.
_MW_EDITSECTION_RE = re.compile(r'<span class="mw-editsection">.*?</span>', re.DOTALL)
_MW_TOC_RE = re.compile(
    r'<div[^>]*\bclass="[^"]*\btoc\b[^"]*"[^>]*>.*?</div>', re.DOTALL
)
_MW_IMAGE_LINK_RE = re.compile(
    r'<a[^>]*\bclass="image"[^>]*>(?P<content>.*?)</a>', re.DOTALL
)
_MW_PARSER_OPEN_RE = re.compile(r'<div[^>]*\bclass="mw-parser-output"[^>]*>')


def _strip_mw_chrome(html: str) -> str:
    html = _MW_EDITSECTION_RE.sub("", html)
    html = _MW_TOC_RE.sub("", html)
    # Unwrap the file-description anchor around inline images, keeping the
    # inner <img> so pandoc converts it to a markdown image.
    html = _MW_IMAGE_LINK_RE.sub(lambda m: m.group("content"), html)
    # Strip the mw-parser-output wrapper. Done as opening-tag-only-plus-last-
    # closing-div rather than a regex over nested content, because the
    # wrapper contains nested divs that a non-greedy regex would close
    # against. Works because mw-parser-output is always the outermost div.
    m = _MW_PARSER_OPEN_RE.search(html)
    if m:
        html = html[: m.start()] + html[m.end() :]
        rstripped = html.rstrip()
        if rstripped.endswith("</div>"):
            html = rstripped[: -len("</div>")] + "\n"
    return html


def html_to_md(html: str) -> str:
    """Convert MediaWiki-rendered HTML to gfm markdown. Fallback path for
    pages where pandoc's mediawiki reader fails on the raw wikitext."""
    proc = subprocess.run(
        ["pandoc", "-f", "html", "-t", "gfm", "--wrap=none"],
        input=_strip_mw_chrome(html),
        capture_output=True,
        text=True,
    )
    if proc.returncode != 0:
        raise RuntimeError(f"pandoc (html) failed: {proc.stderr.strip()}")
    return proc.stdout


def render_markdown(fm: dict, body: str) -> str:
    """Serialise front-matter + body. Stable key order (insertion order)."""
    fm_text = yaml.safe_dump(fm, sort_keys=False, allow_unicode=True).strip()
    return f"---\n{fm_text}\n---\n\n{body.strip()}\n"


# ---- sidecars ---------------------------------------------------------------


def _page_sidecar_path(state_dir: str, title: str) -> str:
    return os.path.join(state_dir, "pages", title_to_slug(title) + ".json")


def _image_sidecar_path(state_dir: str, title: str) -> str:
    return os.path.join(state_dir, "images", image_title_to_filename(title) + ".json")


def _load_json(path: str) -> dict | None:
    if not os.path.exists(path):
        return None
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def _save_json(path: str, data: dict) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")


def _write_text(path: str, text: str) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


# ---- crawl ------------------------------------------------------------------


@dataclass
class ScrapeStats:
    pages_seen: int = 0
    pages_written: int = 0
    pages_unchanged: int = 0
    pages_out_of_scope: int = 0
    pages_missing: int = 0
    pages_redirect: int = 0
    pages_failed: int = 0
    images_seen: int = 0
    images_downloaded: int = 0
    images_unchanged: int = 0
    images_failed: int = 0


@dataclass
class CrawlConfig:
    seed: str
    prefixes: list[str]
    target_dir: str
    state_dir: str
    media_subdir: str
    max_pages: int
    delay_s: float
    # When set, the scope filter switches from prefix-matching to
    # depth-bounded same-language traversal -- right for portal/index pages
    # whose linked content lives at disparate titles. See is_enqueueable.
    max_depth: int | None = None


def is_enqueueable(
    title: str,
    *,
    prefixes: Iterable[str],
    seed_lang: str | None,
    max_depth: int | None,
    depth: int,
) -> bool:
    """Pure decision: should we enqueue a discovered title?

    Two scope modes:
      * max_depth is None (default) -- prefix-based scope via in_scope().
        Right for content trees with a shared title stem (the user manual).
      * max_depth is set -- depth-bounded same-language traversal. Right for
        portal/index pages (Portal:Developers links to disparate titles like
        'Getting started with Gramps development', 'Debugging Gramps', etc.;
        no shared prefix would catch them). Still rejects cross-language
        links so a 'Pl:Portal:Developers' translation link is filtered out.
    """
    if max_depth is not None:
        if lang_code_of(title) != seed_lang:
            return False
        return depth <= max_depth
    return in_scope(title, prefixes)


def crawl(session, cfg: CrawlConfig, stats: ScrapeStats) -> None:
    visited: set[str] = set()
    # Queue entries are (title, depth-from-seed). Depth is only consulted in
    # --max-depth mode, but tracking it always keeps the data flow uniform.
    queue: deque[tuple[str, int]] = deque()
    media_dir = os.path.join(cfg.target_dir, cfg.media_subdir)
    os.makedirs(media_dir, exist_ok=True)
    # The prefix used to shorten filenames is the most specific (longest) match.
    sorted_prefixes = sorted(cfg.prefixes, key=len, reverse=True)
    seed_lang = lang_code_of(cfg.seed)

    def enqueue(t: str, depth: int) -> None:
        """Filter at insert time so out-of-scope titles never consume
        --max-pages budget. visited gets the title either way, so we don't
        re-check the same out-of-scope title that appears as a link on
        multiple in-scope pages."""
        if t in visited:
            return
        visited.add(t)
        if not is_enqueueable(
            t,
            prefixes=cfg.prefixes,
            seed_lang=seed_lang,
            max_depth=cfg.max_depth,
            depth=depth,
        ):
            stats.pages_out_of_scope += 1
            return
        queue.append((t, depth))

    enqueue(cfg.seed, 0)
    if not queue:
        print(
            f"Seed {cfg.seed!r} is not in scope (prefixes={cfg.prefixes!r}, "
            f"max_depth={cfg.max_depth}); nothing to do."
        )
        return

    while queue:
        if stats.pages_seen >= cfg.max_pages:
            print(f"\n(hit --max-pages={cfg.max_pages}; stopping early)")
            break
        title, depth = queue.popleft()
        stats.pages_seen += 1
        # in_scope was already checked at enqueue; guaranteed in scope here.

        print(f"[{stats.pages_seen:>3}] {title}")
        live = session.get_page(title)
        time.sleep(cfg.delay_s)
        if not live.exists:
            print("       (missing on wiki)")
            stats.pages_missing += 1
            continue

        # Skip redirects -- they have no useful body, and following them
        # tends to leak cross-language targets through the scope filter.
        if is_redirect(live.content or ""):
            stats.pages_redirect += 1
            print("       (redirect; skipping)")
            continue

        sc_path = _page_sidecar_path(cfg.state_dir, title)
        sc = _load_json(sc_path)
        is_unchanged = (
            sc
            and sc.get("revid") == live.revid
            and os.path.exists(sc.get("out_path", ""))
        )

        if is_unchanged:
            print(f"       up-to-date (revid {live.revid})")
            stats.pages_unchanged += 1
        else:
            categories = list_categories(session, title)
            time.sleep(cfg.delay_s)
            try:
                md_body, convert_method = try_convert_page(
                    session, title, live.content or "", cfg.media_subdir
                )
            except Exception as e:
                # Both wikitext AND HTML-fallback paths failed. Capture the
                # raw wikitext for offline diagnosis and continue the crawl.
                # No sidecar is saved -- a future re-run will retry without
                # manual cleanup. Link/image walking still happens below so
                # the BFS doesn't stall on a single broken page.
                slug = title_to_slug(title)
                failed_path = os.path.join(cfg.state_dir, "failed", slug + ".wikitext")
                _write_text(failed_path, live.content or "")
                stats.pages_failed += 1
                print(f"       CONVERT FAILED ({e})")
                print(f"       wikitext saved to {failed_path}")
            else:
                # Match against ROOTS so '/lang'-style chapter titles slug
                # cleanly (e.g. 'Foo - Preface/bg' with prefix 'Foo/bg'
                # strips to 'Preface' before slugifying, not 'Preface/bg').
                t_root = title_root(title)
                slug_prefix_root = next(
                    (
                        title_root(p)
                        for p in sorted_prefixes
                        if t_root == title_root(p)
                        or t_root.startswith(title_root(p) + " - ")
                        or t_root.startswith(title_root(p) + "/")
                    ),
                    None,
                )
                slug = title_to_slug(t_root, strip_prefix=slug_prefix_root)
                md_path = os.path.join(cfg.target_dir, slug + ".md")
                # Mark fallback-path pages in front-matter so a curator can
                # filter for them ("which pages should I re-check?").
                source = "wiki-scrape" + (
                    f" ({convert_method})" if convert_method != CONVERT_WIKITEXT else ""
                )
                fm = {
                    "title": title,
                    "categories": categories,
                    "managed": False,
                    "source": source,
                    "wiki_revid": live.revid,
                    "wiki_fetched_at": time.strftime(
                        "%Y-%m-%dT%H:%M:%SZ", time.gmtime()
                    ),
                }
                # Record the language tag on non-English pages so a
                # Dataview query / Obsidian filter can pick them out.
                lang_code = lang_code_of(title)
                if lang_code:
                    fm["lang"] = lang_code
                _write_text(md_path, render_markdown(fm, md_body))
                _save_json(
                    sc_path,
                    {
                        "title": title,
                        "revid": live.revid,
                        "fetched_at": fm["wiki_fetched_at"],
                        "out_path": md_path,
                        "convert_method": convert_method,
                    },
                )
                stats.pages_written += 1
                tag = (
                    f" [{convert_method}]" if convert_method != CONVERT_WIKITEXT else ""
                )
                print(f"       wrote {md_path} (revid {live.revid}){tag}")

        # Walk links (always -- so newly added subpages on a cached ToC are
        # found). enqueue() filters out-of-scope titles so they don't eat
        # max-pages budget. Children enqueue at depth+1.
        for link in list_links(session, title):
            enqueue(link, depth + 1)
        time.sleep(cfg.delay_s)

        # Walk images
        for img_title in list_images(session, title):
            stats.images_seen += 1
            _scrape_image(session, img_title, media_dir, cfg, stats)
            time.sleep(cfg.delay_s)


def _scrape_image(
    session, img_title: str, media_dir: str, cfg: CrawlConfig, stats: ScrapeStats
) -> None:
    info = image_url(session, img_title)
    if not info:
        stats.images_failed += 1
        print(f"       image not found: {img_title}")
        return
    sc_path = _image_sidecar_path(cfg.state_dir, img_title)
    sc = _load_json(sc_path)
    out_path = os.path.join(media_dir, image_title_to_filename(img_title))
    if (
        sc
        and sc.get("sha1")
        and sc["sha1"] == info.get("sha1")
        and os.path.exists(out_path)
    ):
        stats.images_unchanged += 1
        return
    # Retry with exponential backoff -- the empirical failure mode is a
    # Playwright APIRequestContext 30s timeout on a single fetch, which on
    # a re-attempt usually completes. Three tries covers transient network
    # blips and Cloudflare nudges without dragging out the crawl.
    data = None
    last_err: Exception | None = None
    for attempt in range(3):
        try:
            data = fetch_binary(session, info["url"])
            break
        except Exception as e:
            last_err = e
            if attempt < 2:
                time.sleep(2**attempt)  # 1s, 2s
    if data is None:
        stats.images_failed += 1
        print(f"       image fetch failed (after 3 tries): {img_title}: {last_err}")
        return
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "wb") as f:
        f.write(data)
    _save_json(
        sc_path,
        {
            "title": img_title,
            "url": info["url"],
            "sha1": info.get("sha1"),
            "mime": info.get("mime"),
            "out_path": out_path,
        },
    )
    stats.images_downloaded += 1
    print(f"       image -> {out_path}")


# ---- diagnostic logging -----------------------------------------------------


class _Tee:
    """Write to multiple text streams. Used in main() to mirror stdout and
    stderr to a per-run log file without rewiring every print() call -- the
    rest of the script is unaware the log exists.

    Flushes after every write so a crashed run still has a usable tail in
    the log file.
    """

    def __init__(self, *streams):
        self.streams = streams

    def write(self, data: str) -> int:
        for s in self.streams:
            s.write(data)
            s.flush()
        return len(data)

    def flush(self) -> None:
        for s in self.streams:
            s.flush()

    def isatty(self) -> bool:
        # Some libraries probe isatty() to decide on colour output etc.;
        # answer for the primary stream (the real terminal) if any.
        return bool(self.streams) and self.streams[0].isatty()


# ---- main -------------------------------------------------------------------


def _print_summary(stats: ScrapeStats) -> None:
    print()
    print("=== scrape summary ===")
    print(f"  pages seen:          {stats.pages_seen}")
    print(f"    written/updated:   {stats.pages_written}")
    print(f"    unchanged (skip):  {stats.pages_unchanged}")
    print(f"    out of scope:      {stats.pages_out_of_scope}")
    print(f"    redirects (skip):  {stats.pages_redirect}")
    print(f"    missing on wiki:   {stats.pages_missing}")
    print(
        f"    convert failed:    {stats.pages_failed}"
        f"{' (see .wikiscrape/failed/)' if stats.pages_failed else ''}"
    )
    print(f"  images seen:         {stats.images_seen}")
    print(f"    downloaded:        {stats.images_downloaded}")
    print(f"    unchanged (skip):  {stats.images_unchanged}")
    print(f"    failed:            {stats.images_failed}")


def main() -> None:
    ap = argparse.ArgumentParser(
        description="Mirror a section of the Gramps wiki into pages/ as Markdown."
    )
    ap.add_argument(
        "--seed", default=SEED_TITLE, help=f"Seed page title (default: {SEED_TITLE!r})"
    )
    ap.add_argument(
        "--prefix",
        action="append",
        default=None,
        help="Title prefix to follow (repeatable; default: --seed value)",
    )
    ap.add_argument(
        "--target-dir",
        default=DEFAULT_TARGET,
        help=f"Where to write markdown (default: {DEFAULT_TARGET!r})",
    )
    ap.add_argument(
        "--media-subdir",
        default=DEFAULT_MEDIA_SUBDIR,
        help=f"Sub-folder under --target-dir for images "
        f"(default: {DEFAULT_MEDIA_SUBDIR!r})",
    )
    ap.add_argument(
        "--state-dir",
        default=DEFAULT_STATE_DIR,
        help=f"Sidecar dir for resume (default: {DEFAULT_STATE_DIR!r})",
    )
    ap.add_argument(
        "--max-pages",
        type=int,
        default=DEFAULT_MAX_PAGES,
        help=f"Hard cap on pages visited (default: {DEFAULT_MAX_PAGES})",
    )
    ap.add_argument(
        "--max-depth",
        type=int,
        default=None,
        metavar="N",
        help="Switch to depth-bounded crawl: follow links only N "
        "hops from --seed, regardless of title shape. Use "
        "for portal/index pages whose linked content has "
        "disparate titles (e.g. 'Portal:Developers'). Cross-"
        "language links are still excluded. Default: unset "
        "(prefix-based scope via --seed/--prefix).",
    )
    ap.add_argument(
        "--delay",
        type=float,
        default=DEFAULT_DELAY_S,
        help=f"Seconds between API calls (default: {DEFAULT_DELAY_S})",
    )
    ap.add_argument(
        "--no-login",
        action="store_true",
        help="Skip the interactive Cloudflare/login pause "
        "(only when reattaching to a warm Chrome)",
    )
    ap.add_argument(
        "--list-translations",
        action="store_true",
        help="Discover translations of --seed and print their "
        "seed titles, then exit. Performs no crawl.",
    )
    ap.add_argument(
        "--all-translations",
        action="store_true",
        help="Scrape --seed first, then auto-discover translation "
        "seed titles and crawl each in turn. Each language "
        "routes to its own subdirectory under --target-dir.",
    )
    ap.add_argument(
        "--from",
        dest="resume_from",
        default=None,
        metavar="CODE",
        help="With --all-translations: skip languages until "
        "reaching this lang code, then continue. Use 'en' "
        "to start at the English seed. Example: '--from da' "
        "after a CF timeout that landed mid-cs.",
    )
    ap.add_argument(
        "--only",
        dest="only_langs",
        default=None,
        metavar="CODE[,CODE,...]",
        help="With --all-translations: scrape only these lang "
        "codes (comma-separated). 'en' for English. Takes "
        "precedence over --from.",
    )
    args = ap.parse_args()

    if args.max_pages > MAX_PAGES_HARD_CAP:
        sys.exit(
            f"--max-pages {args.max_pages} exceeds hard cap "
            f"{MAX_PAGES_HARD_CAP}; raise MAX_PAGES_HARD_CAP if intended."
        )

    # Factory for per-seed CrawlConfig. Each language gets its own routed
    # target_dir / state_dir so sidecars and output don't collide across
    # runs of the same script invocation (--all-translations) or across
    # separate invocations.
    def _cfg_for(seed_title: str) -> CrawlConfig:
        td = args.target_dir
        sd = args.state_dir
        ln = lang_code_of(seed_title)
        if ln and td == DEFAULT_TARGET:
            td = os.path.join(td, ln)
        if ln and sd == DEFAULT_STATE_DIR:
            sd = os.path.join(sd, ln)
        # Explicit --prefix only applies to the original --seed; auto-derived
        # seeds (via --all-translations) get [seed] as their single prefix.
        prefixes = (
            (args.prefix or [seed_title]) if seed_title == args.seed else [seed_title]
        )
        return CrawlConfig(
            seed=seed_title,
            prefixes=prefixes,
            target_dir=td,
            state_dir=sd,
            media_subdir=args.media_subdir,
            max_pages=args.max_pages,
            delay_s=args.delay,
            max_depth=args.max_depth,
        )

    cfg = _cfg_for(args.seed)
    state_dir = cfg.state_dir  # for the log file path below

    # Tee stdout+stderr to a per-run log under <state-dir>/logs/. Set up
    # BEFORE wikitransport.connect() so the Chrome-launch banner and any
    # early errors are captured. Old logs are never pruned -- they're small,
    # one per run, and exactly what you want to grep when a failure clusters
    # across runs.
    log_dir = os.path.join(state_dir, "logs")
    os.makedirs(log_dir, exist_ok=True)
    log_path = os.path.join(
        log_dir,
        time.strftime("scrape-%Y%m%dT%H%M%SZ.log", time.gmtime()),
    )
    log_file = open(log_path, "w", encoding="utf-8")
    orig_stdout, orig_stderr = sys.stdout, sys.stderr
    sys.stdout = _Tee(orig_stdout, log_file)
    sys.stderr = _Tee(orig_stderr, log_file)

    try:
        # Self-describing header so a log opened weeks later explains itself
        # without needing to cross-reference shell history.
        print(f"# scrape_wiki argv: {sys.argv[1:]}")
        print(f"# log:              {log_path}")
        print(
            f"# started:          "
            f"{time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}"
        )
        print(f"# seed:             {cfg.seed}")
        print(f"# prefixes:         {cfg.prefixes}")
        print(f"# target:           {cfg.target_dir}")
        print(f"# state:            {cfg.state_dir}")
        print()

        pw, browser, session = wikitransport.connect(
            interactive_login=not args.no_login
        )
        try:
            who = session.userinfo()
            print(
                f"Authenticated as {who.get('name', '?')} "
                f"(id {who.get('id', '?')})\n"
            )

            # --list-translations: discover and print; no crawl.
            if args.list_translations:
                trans = discover_translations(session, args.seed)
                if not trans:
                    print(f"No translations discovered for {args.seed!r}.")
                else:
                    print(
                        f"{len(trans)} translation(s) discovered for " f"{args.seed!r}:"
                    )
                    for ln, t in trans:
                        print(f'  {ln:8}  --seed "{t}"')
                return

            # Build the seed list. --all-translations prepends auto-discovered
            # siblings; otherwise it's just the explicit --seed.
            seeds: list[str] = [args.seed]
            if args.all_translations:
                trans = discover_translations(session, args.seed)
                print(
                    f"Auto-discovered {len(trans)} translation(s); "
                    f"will consider {len(seeds) + len(trans)} languages "
                    f"in sequence.\n"
                )
                for _ln, t in trans:
                    if t not in seeds:
                        seeds.append(t)

            # Apply --only / --from selection. Warn if either is set without
            # --all-translations (they'd have no effect on a single-seed run).
            if (args.only_langs or args.resume_from) and not args.all_translations:
                print(
                    "Warning: --only / --from only take effect with "
                    "--all-translations; ignoring.\n"
                )
            else:
                only_set = (
                    set(c.strip() for c in args.only_langs.split(","))
                    if args.only_langs
                    else None
                )
                seeds, skipped = filter_seeds(
                    seeds, only=only_set, resume_from=args.resume_from
                )
                if skipped:
                    print(
                        f"Skipping {len(skipped)} language(s) "
                        f"({'--only' if only_set else '--from'}):"
                    )
                    for s in skipped:
                        code = lang_code_of(s) or "en"
                        print(f"  skip [{code}] {s}")
                    print()
                if not seeds:
                    print("No languages match the selection; nothing to do.")
                    return

            for s in seeds:
                # Resolve at the entry point so a manually-passed seed (e.g.
                # 'Gramps 6.0 Wiki Manual/de' that redirects to its canonical
                # 'De:'-style title) drives the crawl from the right title.
                # Discovery already resolved its outputs, so an --all-
                # translations seed is a no-op here.
                resolved = resolve_redirect(session, s)
                if resolved != s:
                    print(f"\nseed {s!r} -> {resolved!r} (redirect followed)")
                per_cfg = _cfg_for(resolved)
                per_stats = ScrapeStats()
                heading_lang = lang_code_of(resolved) or "en"
                print(f"\n========== [{heading_lang}] {resolved} ==========")
                print(f"target: {per_cfg.target_dir}")
                print(f"state:  {per_cfg.state_dir}\n")
                try:
                    crawl(session, per_cfg, per_stats)
                finally:
                    _print_summary(per_stats)
        finally:
            pw.stop()
    finally:
        # Restore the real stdout/stderr before printing the path hint, so
        # it lands on the terminal not into a closed log file.
        sys.stdout = orig_stdout
        sys.stderr = orig_stderr
        log_file.close()
        print(f"log: {log_path}")


if __name__ == "__main__":
    main()
