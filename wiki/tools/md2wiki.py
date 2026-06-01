#!/usr/bin/env python3
"""md2wiki -- convert a managed Markdown source file into MediaWiki wikitext.

Source of truth is the .md file; this produces what gets pushed to the wiki.
One-way: repo -> wiki.

Front-matter (YAML) drives the mapping; the file path never does (so the page
identity survives the docs tree being relocated later):

    ---
    title: "Gramps 6.0 Wiki Manual - Addons"   # the wiki page title (required)
    categories: ["Addons", "Gramps 6.0"]        # appended as [[Category:...]]
    managed: true                               # only managed pages are pushed
    ---

Two markup conveniences that keep the SAME .md rendering correctly on GitHub
while still producing wiki-isms on the wiki:

  * Template shim -- GitHub hides HTML comments, so wiki templates are authored
    as `<!--wiki:{{man index}}-->`. On GitHub: invisible. Converted: emitted as
    raw `{{man index}}` wikitext. Works inline or as a block.

  * Internal links -- authored as `[label](wiki:Page_Name)`. On GitHub this is a
    normal link; converted it becomes `[[Page_Name|label]]`. (If label == page,
    collapses to `[[Page_Name]]`.)

Everything else is plain GitHub-Flavored Markdown handed to pandoc
(`-f gfm -t mediawiki`). Author bodies starting at H2 -- the page title is the
implicit H1 and lives in front-matter, not the body.

CLI:  python3 md2wiki.py pages/addon-development.md      # prints wikitext
      python3 md2wiki.py pages/addon-development.md --json  # title+categories+text
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path

# yaml is imported lazily inside split_frontmatter -- the only function here
# that needs it. Keeping it lazy lets tests that don't touch frontmatter
# (or that mock split_frontmatter) run in environments without pyyaml.
import mdcommon

FM_RE = re.compile(r"^---\n(.*?)\n---\n?(.*)$", re.DOTALL)
SHIM_RE = re.compile(r"<!--\s*wiki:(.*?)-->", re.DOTALL)
WIKILINK_RE = re.compile(r"\[([^\]]+)\]\(wiki:([^)]+)\)")
# pandoc leaves a bare alphanumeric word untouched; we use that as a placeholder.
PLACEHOLDER = "xWIKITOKEN{:04d}x"
PLACEHOLDER_SCAN = re.compile(r"xWIKITOKEN(\d{4})x")
# pandoc emits an empty anchor span before each heading; MediaWiki makes its own.
HEADING_ANCHOR_RE = re.compile(r'^<span id="[^"]*"></span>\n', re.MULTILINE)


@dataclass
class ConvertedPage:
    title: str
    managed: bool
    categories: list[str]
    wikitext: str
    source: str
    frontmatter: dict = field(default_factory=dict)


def split_frontmatter(text: str) -> tuple[dict, str]:
    import yaml  # noqa: PLC0415 -- lazy so tests without pyyaml can import the module

    m = FM_RE.match(text)
    if not m:
        raise ValueError("no YAML front-matter found (file must start with '---')")
    meta = yaml.safe_load(m.group(1)) or {}
    if not isinstance(meta, dict):
        raise ValueError("front-matter did not parse to a mapping")
    return meta, m.group(2)


def _stash(body: str) -> tuple[str, dict[str, str]]:
    """Replace template shims and wiki: links with opaque placeholders BEFORE
    pandoc, so pandoc can't mangle them. Returns (body, token->wikitext)."""
    tokens: dict[str, str] = {}
    counter = [0]

    def make(repl: str) -> str:
        key = PLACEHOLDER.format(counter[0])
        counter[0] += 1
        tokens[key] = repl
        return key

    # template shims -> raw wikitext verbatim
    body = SHIM_RE.sub(lambda m: make(m.group(1).strip()), body)

    # [label](wiki:Page) -> [[Page|label]]  (or [[Page]] if identical)
    def link(m: re.Match) -> str:
        label, page = m.group(1).strip(), m.group(2).strip()
        wt = f"[[{page}]]" if label == page else f"[[{page}|{label}]]"
        return make(wt)

    body = WIKILINK_RE.sub(link, body)
    return body, tokens


def _unstash(wikitext: str, tokens: dict[str, str]) -> str:
    def restore(m: re.Match) -> str:
        key = m.group(0)
        if key not in tokens:
            return key  # not one of ours; leave it
        return tokens[key]

    return PLACEHOLDER_SCAN.sub(restore, wikitext)


def _pandoc(markdown: str) -> str:
    proc = subprocess.run(
        ["pandoc", "-f", "gfm", "-t", "mediawiki", "--wrap=none"],
        input=markdown,
        capture_output=True,
        text=True,
    )
    if proc.returncode != 0:
        raise RuntimeError(f"pandoc failed: {proc.stderr.strip()}")
    return proc.stdout


def convert_text(
    text: str,
    source: str = "<string>",
    *,
    title_map: dict[str, str] | None = None,
    title_prefix: str = "",
    inbatch_canonical_titles: set[str] | None = None,
    strip_categories: bool = False,
) -> ConvertedPage:
    """Convert one page's Markdown to MediaWiki wikitext.

    ``title_map`` resolves Obsidian-internal ``[[Page]]`` references AND
    relative ``[label](XX.md)`` links; when omitted, either flavour raises
    ``ValueError`` so a silently-broken link can't slip through. Build the
    map with ``mdcommon.build_title_map`` (or via ``convert_file`` /
    ``convert_dir`` which build it automatically).

    ``title_prefix`` (e.g. ``"User:Eduralph/Sandbox/"``) is prepended to the
    returned page title AND to any ``wiki:`` link target whose page is in
    ``inbatch_canonical_titles`` -- typically the set of canonical titles
    being published in the same run. Out-of-batch ``wiki:`` links are left
    alone so genuine cross-wiki references keep resolving correctly.

    ``strip_categories`` drops the ``[[Category:X]]`` trailers; useful for
    sandbox / User-namespace pushes that otherwise would add the User page
    to those public categories.
    """
    meta, body = split_frontmatter(text)
    title = meta.get("title")
    if not title:
        raise ValueError("front-matter missing required 'title'")

    # Normalise Obsidian-native conventions BEFORE handing to pandoc. Code
    # spans and HTML comments are stashed first so the preprocessors can't
    # reach into them (an author documenting [[Page]] syntax in a comment
    # or showing `[['list', 'literal']]` in a code block must not get their
    # documentation silently rewritten).
    body, code_tokens = mdcommon.stash_code(body)
    body, comment_tokens = mdcommon.stash_html_comments(body)
    body = mdcommon.convert_obsidian_embeds(body)
    if mdcommon.OBSIDIAN_INTERNAL_LINK_RE.search(body):
        if title_map is None:
            raise ValueError(
                f"{source}: contains Obsidian-internal [[Page]] links but no "
                f"title_map was provided -- pass title_map=mdcommon.build_title_map(...)"
            )
        body = mdcommon.convert_obsidian_internal_links(body, title_map)
    if mdcommon.RELATIVE_MD_LINK_RE.search(body):
        if title_map is None:
            raise ValueError(
                f"{source}: contains relative .md links but no title_map "
                f"was provided -- pass title_map=mdcommon.build_title_map(...)"
            )
        body = mdcommon.convert_relative_md_links(body, title_map)
    # Apply the sandbox prefix to in-batch wiki: targets. Operates on the
    # uniform `wiki:` form, so it covers all three sources of wiki: links:
    # the Obsidian [[Page]] conversion above, the relative .md conversion
    # above, and the [label](wiki:Foo) form authored directly in the source.
    if title_prefix and inbatch_canonical_titles:
        body = mdcommon.prefix_inbatch_wiki_links(
            body, inbatch_canonical_titles, title_prefix
        )
    body = mdcommon.unstash_html_comments(body, comment_tokens)
    body = mdcommon.unstash_code(body, code_tokens)

    stashed, tokens = _stash(body)
    raw = HEADING_ANCHOR_RE.sub("", _pandoc(stashed))
    wikitext = _unstash(raw, tokens).strip()
    # Pandoc emits [[File:_media/foo.svg|cap]] from a markdown image with a
    # subdir path, but MediaWiki's File: namespace is flat. Basenameify so
    # the resulting wikitext links to a valid File: title.
    wikitext = mdcommon.basenameify_file_refs(wikitext)

    cats = meta.get("categories") or []
    if isinstance(cats, str):
        cats = [cats]
    if cats and not strip_categories:
        wikitext += "\n\n" + "\n".join(f"[[Category:{c}]]" for c in cats)

    return ConvertedPage(
        title=(title_prefix + title) if title_prefix else title,
        managed=bool(meta.get("managed", False)),
        categories=([] if strip_categories else list(cats)),
        wikitext=normalize(wikitext),
        source=source,
        frontmatter=meta,
    )


def convert_file(
    path: str,
    *,
    title_map: dict[str, str] | None = None,
    title_prefix: str = "",
    inbatch_canonical_titles: set[str] | None = None,
    strip_categories: bool = False,
) -> ConvertedPage:
    """Convert a single .md file.

    If ``title_map`` is omitted, one is built from the source file's parent
    directory -- enough to resolve sibling-page ``[[Page]]`` references in
    the common single-page case. For multi-folder vaults, build the map at
    the docs-root and pass it explicitly.

    See :func:`convert_text` for the meaning of ``title_prefix``,
    ``inbatch_canonical_titles``, and ``strip_categories``.
    """
    src = Path(path)
    if title_map is None:
        title_map = mdcommon.build_title_map(src.parent)
    with open(path, encoding="utf-8") as f:
        return convert_text(
            f.read(),
            source=path,
            title_map=title_map,
            title_prefix=title_prefix,
            inbatch_canonical_titles=inbatch_canonical_titles,
            strip_categories=strip_categories,
        )


def normalize(wikitext: str) -> str:
    """Canonical form for hashing: strip per-line trailing ws, single trailing
    newline. Keeps cosmetic churn out of the change/drift comparison."""
    lines = [ln.rstrip() for ln in wikitext.splitlines()]
    return "\n".join(lines).strip() + "\n"


def main() -> None:
    ap = argparse.ArgumentParser(description="Convert managed Markdown to wikitext.")
    ap.add_argument("path")
    ap.add_argument(
        "--json",
        action="store_true",
        help="emit title/categories/managed/wikitext as JSON",
    )
    ap.add_argument(
        "--title-prefix",
        default="",
        help=(
            'prepend to the page title and to in-batch wiki: link targets, '
            'e.g. "User:Eduralph/Sandbox/". When set, the in-batch set is '
            "built by scanning --inbatch-from (defaults to the source file's "
            "parent directory)."
        ),
    )
    ap.add_argument(
        "--inbatch-from",
        default=None,
        help=(
            "directory to scan for managed: true pages, whose canonical titles "
            "become the 'in-batch' set for --title-prefix rewriting. Defaults "
            "to the source file's parent directory. Ignored when "
            "--title-prefix is empty."
        ),
    )
    ap.add_argument(
        "--strip-categories",
        action="store_true",
        help=(
            "drop [[Category:X]] trailers. Mirrors publish.py behaviour: "
            "auto-on when --title-prefix starts with 'User:'; this flag "
            "forces it on otherwise."
        ),
    )
    ap.add_argument(
        "--keep-categories",
        action="store_true",
        help="keep [[Category:X]] trailers even under a User: title prefix",
    )
    args = ap.parse_args()

    if args.strip_categories and args.keep_categories:
        sys.exit("md2wiki: --strip-categories and --keep-categories are mutually exclusive")

    # Mirror publish.py: auto-strip categories for User-namespace prefixes
    # unless overridden by --keep-categories. Explicit --strip-categories
    # forces it on regardless of prefix.
    strip_categories = args.strip_categories or (
        args.title_prefix.startswith("User:") and not args.keep_categories
    )

    inbatch: set[str] | None = None
    title_map = None
    if args.title_prefix or args.inbatch_from:
        # One knob: --inbatch-from (default: source's parent) drives BOTH
        # the title_map (so cross-folder [[Page]] / .md links resolve) and
        # the in-batch set (canonical titles of managed pages in scope, for
        # the wiki: prefix rewrite). Mirrors publish.build_plan's logic so
        # the spot-check output matches what the full publish would produce.
        scan_dir = Path(args.inbatch_from) if args.inbatch_from else Path(args.path).parent
        title_map = mdcommon.build_title_map(scan_dir)
        inbatch = set()
        for md in sorted(scan_dir.rglob("*.md")):
            try:
                with open(md, encoding="utf-8") as f:
                    head = f.read()
                meta, _ = split_frontmatter(head)
            except (OSError, ValueError):
                continue
            if meta.get("managed", False) and meta.get("title"):
                inbatch.add(str(meta["title"]))

    try:
        page = convert_file(
            args.path,
            title_map=title_map,
            title_prefix=args.title_prefix,
            inbatch_canonical_titles=inbatch,
            strip_categories=strip_categories,
        )
    except Exception as e:
        sys.exit(f"md2wiki: {args.path}: {e}")
    if args.json:
        print(
            json.dumps(
                {
                    "title": page.title,
                    "managed": page.managed,
                    "categories": page.categories,
                    "wikitext": page.wikitext,
                },
                indent=2,
                ensure_ascii=False,
            )
        )
    else:
        sys.stdout.write(page.wikitext)


if __name__ == "__main__":
    main()
