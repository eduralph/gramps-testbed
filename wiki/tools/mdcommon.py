#!/usr/bin/env python3
"""Preprocessing helpers shared by md2wiki and md2pdf.

These convert Obsidian-native conventions into plain markdown / wikitext forms
that pandoc and MediaWiki understand. Authors write in the Obsidian-friendly
form (renders live in Obsidian); the publishing tools run these helpers before
handing off to pandoc.

Pure functions, no I/O except for ``build_title_map`` which scans source files
to build the stem-to-wiki-title map needed to resolve ``[[Page]]`` references.
"""

from __future__ import annotations

import re
from pathlib import Path

# yaml is imported lazily inside build_title_map -- it's the only function in
# this module that needs it, and keeping it lazy lets the pure-function tests
# (link conversion, code stash, etc.) run in environments without pyyaml.

# ------------------------
# Obsidian source-side patterns
# ------------------------

# ![[target]] or ![[target|caption]]. Target is a path (no nested brackets,
# no pipe). Caption is free text up to ]].
OBSIDIAN_EMBED_RE = re.compile(r"!\[\[([^\[\]|]+?)(?:\|([^\]]*))?\]\]")

# [[Page]] or [[Page|label]]. Negative lookbehind excludes ![[...]] embeds.
OBSIDIAN_INTERNAL_LINK_RE = re.compile(r"(?<!!)\[\[([^\[\]|]+?)(?:\|([^\]]*))?\]\]")

# Standard markdown image: ![alt](src). Used by md2pdf for path absolutising
# and SVG pre-conversion AFTER Obsidian embeds have been normalised.
MARKDOWN_IMAGE_RE = re.compile(r"!\[([^\]]*)\]\(([^)]+)\)")

# Standard markdown link with a relative .md target: [label](path/to/file.md)
# or [label](file.md#anchor). The href must end with .md or .md#... .
# Negative lookbehind on `!` keeps this from matching ![alt](img.md)-shaped
# images. The path part allows everything except `)` and `#` (so folder
# names with spaces like "05 - Addon development/foo.md" work). External
# URLs are filtered inside the substitution by checking for "://".
RELATIVE_MD_LINK_RE = re.compile(
    r"(?<!!)\[([^\]]+)\]\(([^)#]+\.md)(#[^)]*)?\)"
)

# A [label](wiki:Target) link, post-conversion of all sources. Used by the
# in-batch prefix rewriter to apply a sandbox prefix to in-batch targets only.
WIKI_LINK_RE = re.compile(r"\[([^\]]+)\]\(wiki:([^)]+)\)")

# ------------------------
# MediaWiki-side patterns (post-pandoc)
# ------------------------

# [[File:<path>|<caption>]] or [[File:<path>]]. Pandoc emits these from
# markdown images; we need to basenameify the path because MediaWiki's
# File: namespace is flat.
FILE_REF_RE = re.compile(r"\[\[File:([^|\]]+?)(\|[^\]]*)?\]\]")

# ------------------------
# Front-matter splitter (mirrors md2wiki / md2pdf local copies)
# ------------------------

_FM_RE = re.compile(r"^---\n(.*?)\n---\n?(.*)$", re.DOTALL)

# HTML comments. Text-pattern preprocessors below must NOT reach into
# comments -- an author writing `<!-- see [[15-rules]] -->` is documenting
# the syntax, not asking for a link.
_HTML_COMMENT_RE = re.compile(r"<!--.*?-->", re.DOTALL)

# Fenced code blocks (```lang ... ``` or ~~~lang ... ~~~) and inline code
# spans (`...`). Markdown semantics: anything inside is verbatim and must
# not be reached by preprocessors. We stash both to prevent things like
# `[['Gramps', 'https://...']]` (a Python list literal in a code block)
# from being parsed as an Obsidian wiki-link.
#
# The fenced-code pattern is non-greedy and matches the matching number of
# backticks/tildes (3+); the inline pattern matches a single ``` ` ``` run
# bounded by the same length. Order matters: stash fenced FIRST so an
# inline backtick inside a fence doesn't get matched standalone.
_FENCED_CODE_RE = re.compile(r"(?m)^(```+|~~~+)[^\n]*\n.*?^\1\s*$", re.DOTALL)
_INLINE_CODE_RE = re.compile(r"(`+)(?:(?!\1).)+\1")

# Placeholder pattern for stashed regions. Uses ASCII control chars so it
# can't collide with user text or with pandoc's own placeholder mangling.
# The numeric suffix is wide enough for any plausible per-page count.
_COMMENT_PLACEHOLDER = "\x00MDCOMMENT{:04d}\x00"
_COMMENT_PLACEHOLDER_RE = re.compile(r"\x00MDCOMMENT(\d{4})\x00")
_CODE_PLACEHOLDER = "\x00MDCODE{:04d}\x00"
_CODE_PLACEHOLDER_RE = re.compile(r"\x00MDCODE(\d{4})\x00")


# ------------------------------------------------------------
# HTML-comment stash/unstash (run around Obsidian preprocessors so the
# preprocessors don't reach into commented-out content)
# ------------------------------------------------------------


def stash_html_comments(body: str) -> tuple[str, list[str]]:
    """Replace each HTML comment with an opaque placeholder; return the
    rewritten body and a list of the original comments (indexed by the
    placeholder's numeric suffix).

    Pair with ``unstash_html_comments`` to restore. Run before any
    text-pattern preprocessor that should not see commented-out content.
    """
    tokens: list[str] = []

    def repl(m: re.Match) -> str:
        key = _COMMENT_PLACEHOLDER.format(len(tokens))
        tokens.append(m.group(0))
        return key

    return _HTML_COMMENT_RE.sub(repl, body), tokens


def unstash_html_comments(text: str, tokens: list[str]) -> str:
    """Inverse of ``stash_html_comments`` -- restore comments in place."""

    def repl(m: re.Match) -> str:
        idx = int(m.group(1))
        if idx >= len(tokens):
            return m.group(0)  # not one of ours; leave it
        return tokens[idx]

    return _COMMENT_PLACEHOLDER_RE.sub(repl, text)


def stash_code(body: str) -> tuple[str, list[str]]:
    """Stash fenced and inline code spans so preprocessors don't reach them.

    Markdown semantics: ``code`` and ```` ```fenced``` ```` blocks are
    verbatim. Without this, an inline code span like `` `[[Page]]` `` (an
    author DOCUMENTING the syntax) gets rewritten as a real link, and a
    fenced code block containing `[['list', 'literal']]` blows up the
    Obsidian-link resolver entirely.

    Fenced blocks are stashed BEFORE inline so the inline-backtick pattern
    can't reach into the fence.
    """
    tokens: list[str] = []

    def repl(m: re.Match) -> str:
        key = _CODE_PLACEHOLDER.format(len(tokens))
        tokens.append(m.group(0))
        return key

    body = _FENCED_CODE_RE.sub(repl, body)
    body = _INLINE_CODE_RE.sub(repl, body)
    return body, tokens


def unstash_code(text: str, tokens: list[str]) -> str:
    """Inverse of ``stash_code`` -- restore code spans in place."""

    def repl(m: re.Match) -> str:
        idx = int(m.group(1))
        if idx >= len(tokens):
            return m.group(0)
        return tokens[idx]

    return _CODE_PLACEHOLDER_RE.sub(repl, text)


# ------------------------------------------------------------
# Obsidian source-side preprocessors
# ------------------------------------------------------------


def convert_obsidian_embeds(body: str) -> str:
    """Convert ``![[path|cap]]`` -> ``![cap](path)`` and ``![[path]]`` -> ``![](path)``.

    Pandoc's GFM reader doesn't understand Obsidian embed syntax; this turns
    each embed into a standard markdown image so the downstream renderer can
    pick it up. Idempotent on bodies that have no Obsidian embeds.
    """

    def repl(m: re.Match) -> str:
        target = m.group(1).strip()
        caption = (m.group(2) or "").strip()
        return f"![{caption}]({target})"

    return OBSIDIAN_EMBED_RE.sub(repl, body)


def convert_obsidian_internal_links(
    body: str, title_map: dict[str, list[tuple[str, str]]]
) -> str:
    """Convert ``[[Page]]`` / ``[[Page|label]]`` -> ``[label](wiki:Wiki_Title)``.

    ``title_map`` is the multi-candidate map returned by ``build_title_map``:
    each filename stem maps to a list of ``(wiki_title, source_path)`` pairs.
    Most stems have exactly one candidate, but a vault with multi-language
    copies of the same page (``getting-started.md`` in root and ``bg/`` and
    ``da/``) will have several.

    Targets may use any of:
      * ``[[Stem]]`` -- resolves if exactly one file with that stem
      * ``[[folder/Stem]]`` -- path-suffix match disambiguates collisions
      * ``[[Stem#anchor]]`` (anchor is dropped; wiki may have no match)
      * ``[[Stem|label]]`` (or any combination of the above)

    Raises ``ValueError`` for unresolved (no candidate) or ambiguous
    (multiple candidates and the target didn't disambiguate) references --
    the error names the candidates so an author can switch to the
    folder-prefixed form.
    """

    def repl(m: re.Match) -> str:
        target_raw = m.group(1).strip()
        label = (m.group(2) or "").strip()
        # Strip anchor (#section) -- wiki pages may not have matching anchors.
        target = target_raw.split("#", 1)[0].rstrip()
        # Stem is the last path segment. The full target (with any folder
        # prefix) is used to filter candidates if there are several.
        stem = target.rsplit("/", 1)[-1]
        candidates = title_map.get(stem, [])
        if not candidates:
            known = sorted(title_map)
            preview = ", ".join(known[:10]) + (
                f", ... ({len(known) - 10} more)" if len(known) > 10 else ""
            )
            raise ValueError(
                f"unresolved Obsidian internal link [[{target_raw}]]: "
                f"no page with stem {stem!r} in title map (known: {preview})"
            )
        if "/" in target:
            # Folder-prefixed form: keep only candidates whose source path
            # ends with the user-specified ``folder/stem.md`` suffix. ALWAYS
            # filter -- not just on multi-candidate stems -- so a typo'd
            # prefix doesn't silently resolve to the wrong page.
            suffix = target + ".md"
            candidates = [
                c for c in candidates if c[1].replace("\\", "/").endswith(suffix)
            ]
        if not candidates:
            raise ValueError(
                f"unresolved Obsidian internal link [[{target_raw}]]: "
                f"no source path matched folder/stem form {target!r}"
            )
        if len(candidates) > 1:
            paths = ", ".join(c[1] for c in candidates)
            raise ValueError(
                f"ambiguous Obsidian internal link [[{target_raw}]]: "
                f"stem {stem!r} matches multiple pages -- disambiguate with "
                f"[[folder/{stem}]] form. Candidates: {paths}"
            )
        wiki_title = candidates[0][0]
        if not label:
            # Human-readable label = title without underscores.
            label = wiki_title.replace("_", " ")
        return f"[{label}](wiki:{wiki_title})"

    return OBSIDIAN_INTERNAL_LINK_RE.sub(repl, body)


def convert_relative_md_links(
    body: str, title_map: dict[str, list[tuple[str, str]]]
) -> str:
    """Convert ``[label](XX-name.md[#anchor])`` -> ``[label](wiki:Wiki_Title[#anchor])``.

    Resolves the .md target via the same ``title_map`` shape used by
    :func:`convert_obsidian_internal_links` (``{stem: [(title, path), ...]}``).
    Bare-stem and ``folder/stem.md`` forms both work; folder form filters by
    path suffix to disambiguate collisions.

    External URLs (anything with ``://`` in the href) and images are skipped.
    An anchor (``#section``) is preserved verbatim on the wiki: target so the
    wikilink can target a section heading on the resolved page.

    Raises ``ValueError`` for unresolved or ambiguous ``.md`` targets, with
    the same error shape as :func:`convert_obsidian_internal_links` so authors
    get consistent diagnostics regardless of which link style they used.
    """

    def repl(m: re.Match) -> str:
        label = m.group(1)
        href = m.group(2)
        anchor = m.group(3) or ""
        # Skip external URLs (e.g. https://example.com/x.md). The regex
        # already excludes ! but not "://", so guard here.
        if "://" in href:
            return m.group(0)
        # Stem is the last path segment without the .md suffix.
        path_no_ext = href[: -len(".md")]
        stem = path_no_ext.rsplit("/", 1)[-1]
        candidates = title_map.get(stem, [])
        if not candidates:
            known = sorted(title_map)
            preview = ", ".join(known[:10]) + (
                f", ... ({len(known) - 10} more)" if len(known) > 10 else ""
            )
            raise ValueError(
                f"unresolved relative .md link [{label}]({href}{anchor}): "
                f"no page with stem {stem!r} in title map (known: {preview})"
            )
        if "/" in path_no_ext:
            suffix = path_no_ext + ".md"
            candidates = [
                c for c in candidates if c[1].replace("\\", "/").endswith(suffix)
            ]
        if not candidates:
            raise ValueError(
                f"unresolved relative .md link [{label}]({href}{anchor}): "
                f"no source path matched folder/stem form {path_no_ext!r}"
            )
        if len(candidates) > 1:
            paths = ", ".join(c[1] for c in candidates)
            raise ValueError(
                f"ambiguous relative .md link [{label}]({href}{anchor}): "
                f"stem {stem!r} matches multiple pages -- disambiguate by using "
                f"the folder/stem.md form. Candidates: {paths}"
            )
        wiki_title = candidates[0][0]
        return f"[{label}](wiki:{wiki_title}{anchor})"

    return RELATIVE_MD_LINK_RE.sub(repl, body)


def prefix_inbatch_wiki_links(
    body: str, inbatch_titles: set[str], title_prefix: str
) -> str:
    """Prepend ``title_prefix`` to any ``[label](wiki:Target)`` whose Target
    matches an entry in ``inbatch_titles``. Out-of-batch wiki: links are
    left alone (so external references like ``wiki:Coding_for_translation``
    keep pointing at the genuine community page).

    ``inbatch_titles`` is compared with both space-form and underscore-form
    normalisation, since MediaWiki treats ``Foo Bar`` and ``Foo_Bar`` as the
    same page name and authors may write either.
    """
    if not title_prefix or not inbatch_titles:
        return body
    # Normalise once: store both underscore and space forms in a set we can
    # check the raw target against (which is whatever the author wrote).
    normalised: set[str] = set()
    for t in inbatch_titles:
        normalised.add(t)
        normalised.add(t.replace(" ", "_"))
        normalised.add(t.replace("_", " "))

    def repl(m: re.Match) -> str:
        label = m.group(1)
        target = m.group(2)
        # Split off any #anchor before comparing.
        bare, sep, anchor = target.partition("#")
        if bare not in normalised:
            return m.group(0)
        return f"[{label}](wiki:{title_prefix}{bare}{sep}{anchor})"

    return WIKI_LINK_RE.sub(repl, body)


def absolutize_image_paths(body: str, source_dir: Path) -> str:
    """Rewrite relative image ``src`` paths in ``![alt](src)`` to absolute
    paths anchored at ``source_dir``.

    Pandoc resolves relative image paths against its working directory, which
    for our usage (markdown via stdin) is the caller's CWD -- usually wrong.
    Rewriting to absolute paths sidesteps the ambiguity. External URLs
    (``http://``, ``https://``, ``data:``) and already-absolute paths
    (``/...``) are left alone.
    """

    def repl(m: re.Match) -> str:
        alt = m.group(1)
        src = m.group(2).strip()
        if "://" in src or src.startswith("/") or src.startswith("data:"):
            return m.group(0)
        abs_path = (source_dir / src).resolve()
        return f"![{alt}]({abs_path})"

    return MARKDOWN_IMAGE_RE.sub(repl, body)


# ------------------------------------------------------------
# Title-map scanner
# ------------------------------------------------------------


def build_title_map(docs_root: Path) -> dict[str, list[tuple[str, str]]]:
    """Scan every .md file under ``docs_root``, read front-matter ``title``,
    build a ``{stem: [(wiki_title, source_path), ...]}`` map.

    Pages with ``managed: false`` ARE included -- a link to a draft is still a
    valid reference; ``managed`` controls publishability, not resolvability.

    Stem collisions (e.g. ``getting-started.md`` in multiple language
    subfolders) are NOT errors at build time -- they only matter if some
    page actually references the colliding stem with ``[[stem]]``, at which
    point ``convert_obsidian_internal_links`` raises ``ValueError`` and the
    author can disambiguate with ``[[folder/stem]]``. Building eagerly here
    would break tree mode on vaults where colliding stems exist but nobody
    links across the collision.
    """
    import yaml  # noqa: PLC0415 -- lazy so callers without pyyaml can use rest of module

    out: dict[str, list[tuple[str, str]]] = {}
    for p in sorted(docs_root.rglob("*.md")):
        try:
            text = p.read_text(encoding="utf-8")
        except OSError:
            continue
        m = _FM_RE.match(text)
        if not m:
            continue  # no front-matter -> not a page we track
        try:
            meta = yaml.safe_load(m.group(1)) or {}
        except yaml.YAMLError:
            continue
        if not isinstance(meta, dict):
            continue
        title = meta.get("title")
        if not title:
            continue
        out.setdefault(p.stem, []).append((str(title).replace(" ", "_"), str(p)))
    return out


# ------------------------------------------------------------
# MediaWiki post-pandoc helpers
# ------------------------------------------------------------


def basenameify_file_refs(wikitext: str) -> str:
    """In ``[[File:<path>|...]]`` refs emitted by pandoc, replace ``<path>``
    with its basename. MediaWiki's File: namespace is flat (no subdirs).

    Example: ``[[File:_media/foo.svg|cap]]`` -> ``[[File:foo.svg|cap]]``.
    """

    def repl(m: re.Match) -> str:
        path = m.group(1).strip()
        suffix = m.group(2) or ""
        return f"[[File:{Path(path).name}{suffix}]]"

    return FILE_REF_RE.sub(repl, wikitext)


def extract_file_basenames(wikitext: str) -> list[str]:
    """Return the basenames of every ``[[File:...]]`` reference in wikitext.

    Used by the publisher to know which media files to upload alongside a
    page. Order preserved; duplicates preserved (caller can dedup).
    """
    return [Path(m.group(1).strip()).name for m in FILE_REF_RE.finditer(wikitext)]
