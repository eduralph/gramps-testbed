#!/usr/bin/env python3
"""md2pdf -- render Markdown sources from ``pages/`` to PDF.

Two modes:

  * **Single page** -- pass a .md path; produces one PDF for that page.
    ``wiki:`` links resolve to external URLs on the live wiki.

  * **Whole tree (``--tree``)** -- pass a directory (typically ``pages``);
    every ``managed: true`` page under it (templates excluded, matching
    publish.py) is assembled into one bound PDF in path order. ``wiki:``
    links targeting a page that IS in the tree are rewritten to internal
    anchors, so the PDF cross-links itself. Off-tree targets fall back to
    external URLs on the live wiki. A table of contents (H1 + H2) is
    generated automatically.

Reader is ``commonmark_x`` -- a near-superset of GFM that supports
``{#anchor}`` attribute syntax on headings (gfm itself does not), needed
to assign stable per-page anchors. Tables, fenced code with language tags,
autolinks, and strikethrough all behave the same as under gfm on the real
content tree.

The two markup conveniences match md2wiki.py:

  * ``<!--wiki:{{...}}-->`` template shims are DROPPED (no print analogue).
  * ``[label](wiki:Page_Name)`` becomes external URL (single-page) or
    internal anchor (tree mode, when Page_Name is on-tree).

Table styling: a small LaTeX preamble adds horizontal/vertical breathing
room to tables under xelatex/lualatex/pdflatex. Override with ``--preamble``
or skip with ``--no-preamble``; non-LaTeX engines (weasyprint, ...) ignore
the preamble entirely -- pass CSS via your own pandoc args instead.

CLI:
    python3 md2pdf.py "pages/.../getting-started.md"
    python3 md2pdf.py "pages/.../getting-started.md" -o out.pdf
    python3 md2pdf.py pages --tree -o manual.pdf
    python3 md2pdf.py pages --tree --doc-title "Gramps 6.0 Manual" -o manual.pdf
"""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
import tempfile
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable

import yaml

import mdcommon

WIKI_BASE = "https://gramps-project.org/wiki/"

FM_RE = re.compile(r"^---\n(.*?)\n---\n?(.*)$", re.DOTALL)
SHIM_RE = re.compile(r"<!--\s*wiki:.*?-->", re.DOTALL)
WIKILINK_RE = re.compile(r"\[([^\]]+)\]\(wiki:([^)]+)\)")
TEMPLATE_DIR_RE = re.compile(r"^(?:\d+\s*-\s*)?templates$", re.IGNORECASE)

LATEX_ENGINES = {"xelatex", "lualatex", "pdflatex"}

# Default LaTeX preamble. Pandoc's template already loads booktabs and
# longtable; this just adds breathing room so wider cells don't read as
# cramped. Override with --preamble for project-specific styling.
DEFAULT_LATEX_PREAMBLE = r"""
% --- md2pdf default table styling ---
\setlength{\tabcolsep}{8pt}
\renewcommand{\arraystretch}{1.25}
"""


LinkResolver = Callable[[str], str]


@dataclass
class RenderedPage:
    title: str
    categories: list[str]
    pdf_bytes: bytes
    source: str
    frontmatter: dict = field(default_factory=dict)


@dataclass
class TreePage:
    path: Path
    title: str
    anchor: str
    categories: list[str]


def split_frontmatter(text: str) -> tuple[dict, str]:
    m = FM_RE.match(text)
    if not m:
        raise ValueError("no YAML front-matter found (file must start with '---')")
    meta = yaml.safe_load(m.group(1)) or {}
    if not isinstance(meta, dict):
        raise ValueError("front-matter did not parse to a mapping")
    return meta, m.group(2)


def _slug(s: str) -> str:
    """Filesystem/anchor-safe slug: lowercase alnum, hyphen-separated."""
    s = s.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-")


def _external_resolver(page: str) -> str:
    return f"{WIKI_BASE}{page}"


def _tree_resolver(anchors: dict[str, str]) -> LinkResolver:
    """anchors maps wiki URL form (underscores) to in-doc anchor."""

    def resolve(page: str) -> str:
        if page in anchors:
            return f"#{anchors[page]}"
        return f"{WIKI_BASE}{page}"

    return resolve


def _rewrite_for_pdf(body: str, resolver: LinkResolver) -> str:
    """Drop template shims; rewrite ``wiki:`` links via ``resolver``."""
    body = SHIM_RE.sub("", body)

    def link(m: re.Match) -> str:
        label, page = m.group(1).strip(), m.group(2).strip()
        return f"[{label}]({resolver(page)})"

    return WIKILINK_RE.sub(link, body)


# ------------------------------------------------------------
# SVG-to-PDF pre-conversion (xelatex/lualatex/pdflatex cannot embed SVG)
# ------------------------------------------------------------


def _svg_to_pdf(svg: Path, out: Path) -> None:
    """Convert one SVG file to PDF.

    Prefers ``rsvg-convert`` (smallest dependency, ships with librsvg);
    falls back to ``inkscape`` (heavier but ubiquitous). If neither is on
    PATH, raises ``RuntimeError`` with the actionable install hint.
    """
    if shutil.which("rsvg-convert"):
        cmd = ["rsvg-convert", "-f", "pdf", str(svg), "-o", str(out)]
    elif shutil.which("inkscape"):
        cmd = [
            "inkscape",
            str(svg),
            "--export-type=pdf",
            f"--export-filename={out}",
        ]
    else:
        raise RuntimeError(
            "SVG-to-PDF conversion requires rsvg-convert (librsvg) or "
            "inkscape on PATH -- neither found. Install with e.g. "
            "`apt install librsvg2-bin` or `apt install inkscape`."
        )
    proc = subprocess.run(cmd, capture_output=True, text=True)
    if proc.returncode != 0:
        raise RuntimeError(
            f"SVG-to-PDF conversion failed ({cmd[0]}): {proc.stderr.strip()}"
        )


def _preconvert_svgs(body: str, tmpdir: Path) -> str:
    """For every ``![alt](src.svg)`` in the body, convert the SVG to PDF and
    rewrite the src to the temp PDF path.

    Expects image paths to already be absolute (run ``absolutize_image_paths``
    first). Non-SVG images are left untouched. SVG paths that don't exist
    error clearly rather than silently dropping the image.
    """

    def repl(m: re.Match) -> str:
        alt = m.group(1)
        src = m.group(2).strip()
        if not src.lower().endswith(".svg"):
            return m.group(0)
        svg_path = Path(src)
        if not svg_path.is_absolute():
            # Shouldn't happen if absolutize_image_paths ran first, but guard.
            raise RuntimeError(
                f"SVG path not absolute: {src!r} -- "
                f"call absolutize_image_paths before _preconvert_svgs"
            )
        if not svg_path.exists():
            raise RuntimeError(f"SVG not found: {svg_path}")
        # Stem-based PDF name; tmpdir is unique per render so collisions are
        # only possible if two SVGs share a stem within the same page.
        pdf_path = tmpdir / (svg_path.stem + ".pdf")
        if not pdf_path.exists():
            _svg_to_pdf(svg_path, pdf_path)
        return f"![{alt}]({pdf_path})"

    return mdcommon.MARKDOWN_IMAGE_RE.sub(repl, body)


def _pandoc_to_pdf(
    markdown: str,
    title: str,
    engine: str,
    *,
    toc: bool = False,
    preamble: str | None = None,
    resource_paths: list[Path] | None = None,
) -> bytes:
    args = [
        "pandoc",
        "-f",
        "commonmark_x",
        "-t",
        "pdf",
        f"--pdf-engine={engine}",
        "--metadata",
        f"title={title}",
        "--standalone",
    ]
    if resource_paths:
        # Pandoc resolves relative image / include paths against this list.
        # We piped markdown via stdin, so it has no source-file context;
        # without --resource-path, relative srcs would fall back to CWD.
        # Path separator: ':' on POSIX, ';' on Windows -- os.pathsep handles
        # both transparently.
        import os

        sep = os.pathsep
        args += [f"--resource-path={sep.join(str(p) for p in resource_paths)}"]
    if toc:
        args += ["--toc", "--toc-depth=2"]

    preamble_path: Path | None = None
    if preamble and engine in LATEX_ENGINES:
        f = tempfile.NamedTemporaryFile(
            mode="w", suffix=".tex", delete=False, encoding="utf-8"
        )
        f.write(preamble)
        f.close()
        preamble_path = Path(f.name)
        args += [f"--include-in-header={preamble_path}"]

    args += ["-o", "-"]

    try:
        proc = subprocess.run(
            args,
            input=markdown.encode("utf-8"),
            capture_output=True,
            text=False,
        )
    finally:
        if preamble_path is not None:
            preamble_path.unlink(missing_ok=True)

    if proc.returncode != 0:
        raise RuntimeError(
            f"pandoc failed (engine={engine}): "
            f"{proc.stderr.decode('utf-8', 'replace').strip()}"
        )
    return proc.stdout


def convert_text(
    text: str,
    source: str = "<string>",
    engine: str = "xelatex",
    preamble: str | None = DEFAULT_LATEX_PREAMBLE,
    *,
    source_dir: Path | None = None,
    title_map: dict[str, str] | None = None,
) -> RenderedPage:
    """Render one page's Markdown to PDF bytes.

    ``source_dir`` anchors relative image paths (``_media/foo.svg`` etc.)
    and is required when the body contains any image references. ``title_map``
    resolves Obsidian-internal ``[[Page]]`` references; when omitted,
    ``[[Page]]`` in the body raises rather than silently rendering as literal
    text. Both are filled in automatically by ``convert_file`` /
    ``convert_tree``; callers using ``convert_text`` directly must supply
    them when the body needs them.
    """
    meta, body = split_frontmatter(text)
    title = meta.get("title")
    if not title:
        raise ValueError("front-matter missing required 'title'")

    cats = meta.get("categories") or []
    if isinstance(cats, str):
        cats = [cats]

    # Normalise Obsidian-native conventions BEFORE other rewrites. Stash
    # code spans and HTML comments first so the preprocessors can't reach
    # inside them (an author documenting [[Page]] syntax in a comment or
    # showing `[['list', 'literal']]` in a code block must not get their
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
    body = mdcommon.unstash_html_comments(body, comment_tokens)
    body = mdcommon.unstash_code(body, code_tokens)

    body = _rewrite_for_pdf(body, _external_resolver)

    # Absolutise image paths and pre-convert SVGs. The SVG conversion writes
    # PDFs into a tempdir whose lifetime must outlast the pandoc call below
    # (pandoc reads the PDFs synchronously, so a context manager works).
    with tempfile.TemporaryDirectory(prefix="md2pdf-svg-") as tmp:
        tmpdir = Path(tmp)
        if source_dir is not None:
            body = mdcommon.absolutize_image_paths(body, source_dir)
        if mdcommon.MARKDOWN_IMAGE_RE.search(body):
            # Any image with a relative path at this point would not resolve.
            # Pre-convert SVGs (xelatex can't embed them); other formats are
            # left for pandoc / the engine to handle directly.
            body = _preconvert_svgs(body, tmpdir)
        if cats:
            body = body.rstrip() + "\n\n---\n\n*Categories: " + ", ".join(cats) + "*\n"

        resource_paths = [source_dir, tmpdir] if source_dir is not None else [tmpdir]
        pdf_bytes = _pandoc_to_pdf(
            body,
            title=title,
            engine=engine,
            preamble=preamble,
            resource_paths=resource_paths,
        )
    return RenderedPage(
        title=title,
        categories=list(cats),
        pdf_bytes=pdf_bytes,
        source=source,
        frontmatter=meta,
    )


def convert_file(
    path: str,
    engine: str = "xelatex",
    preamble: str | None = DEFAULT_LATEX_PREAMBLE,
    *,
    title_map: dict[str, str] | None = None,
) -> RenderedPage:
    """Render one .md file to PDF bytes.

    Image paths in the body resolve against the file's parent directory.
    ``[[Page]]`` references default to a title map built from the file's
    parent directory; pass ``title_map`` explicitly for wider scoping.
    """
    src = Path(path)
    if title_map is None:
        title_map = mdcommon.build_title_map(src.parent)
    with open(path, encoding="utf-8") as f:
        return convert_text(
            f.read(),
            source=path,
            engine=engine,
            preamble=preamble,
            source_dir=src.parent,
            title_map=title_map,
        )


def _is_template_part(part: str) -> bool:
    return bool(TEMPLATE_DIR_RE.match(part))


def _walk_pages(root: Path) -> list[Path]:
    out: list[Path] = []
    for p in sorted(root.rglob("*.md")):
        rel_parts = p.relative_to(root).parts[:-1]
        if any(_is_template_part(part) for part in rel_parts):
            continue
        out.append(p)
    return out


def convert_tree(
    root: Path,
    doc_title: str,
    *,
    engine: str = "xelatex",
    preamble: str | None = DEFAULT_LATEX_PREAMBLE,
) -> tuple[bytes, list[TreePage]]:
    """Assemble every ``managed: true`` page under ``root`` into one PDF.

    Returns (pdf_bytes, list of TreePage in tree order). ``managed: false``
    is honoured absolutely -- meta notes and preliminary drafts are
    excluded from the bound PDF the same way they're excluded from the
    wiki publisher; there is no override flag. Templates folders are
    excluded unconditionally on top of that.
    """
    files = _walk_pages(root)
    parsed: list[tuple[Path, dict, str]] = []
    for p in files:
        try:
            meta, body = split_frontmatter(p.read_text(encoding="utf-8"))
        except ValueError:
            continue  # not a page file (no front-matter)
        if not meta.get("managed", False):
            continue
        if not meta.get("title"):
            continue
        parsed.append((p, meta, body))

    if not parsed:
        raise ValueError(f"no managed pages found under {root}")

    # Pass 1: title -> anchor map keyed by wiki URL form (underscores).
    anchors: dict[str, str] = {}
    for _p, meta, _body in parsed:
        title = meta["title"]
        anchors[title.replace(" ", "_")] = _slug(title)

    # Pass 1b: filename-stem -> wiki title map for Obsidian-internal
    # ``[[Page]]`` resolution. Built across the whole tree so a page can
    # reference any other page in the manual.
    title_map = mdcommon.build_title_map(root)

    # Pass 2: rewrite each page's body using a tree-aware resolver, then
    # prepend an H1 carrying the explicit anchor. Image rewrites and SVG
    # pre-conversion happen per-page because each page's relative image
    # paths anchor against its OWN folder, not the tree root.
    resolver = _tree_resolver(anchors)
    chunks: list[str] = []
    pages: list[TreePage] = []
    # SVG-converted PDFs need to outlive the pandoc call; use one tempdir
    # for the whole tree-render rather than per-page so cleanup is centralised.
    with tempfile.TemporaryDirectory(prefix="md2pdf-tree-svg-") as tmp:
        tmpdir = Path(tmp)
        resource_paths: list[Path] = [tmpdir]
        for p, meta, body in parsed:
            title = meta["title"]
            anchor = anchors[title.replace(" ", "_")]
            # Obsidian-native conventions first; this matches single-page
            # mode. Code spans and comments are stashed around the
            # preprocessors so the [[Page]] / ![[...]] regexes can't reach
            # into commented-out or code-block content.
            page_body, code_tokens = mdcommon.stash_code(body)
            page_body, comment_tokens = mdcommon.stash_html_comments(page_body)
            page_body = mdcommon.convert_obsidian_embeds(page_body)
            if mdcommon.OBSIDIAN_INTERNAL_LINK_RE.search(page_body):
                page_body = mdcommon.convert_obsidian_internal_links(
                    page_body, title_map
                )
            page_body = mdcommon.unstash_html_comments(page_body, comment_tokens)
            page_body = mdcommon.unstash_code(page_body, code_tokens)
            page_body = _rewrite_for_pdf(page_body, resolver).strip()
            # Resolve image paths against THIS page's folder; pre-convert SVGs.
            page_body = mdcommon.absolutize_image_paths(page_body, p.parent)
            if mdcommon.MARKDOWN_IMAGE_RE.search(page_body):
                page_body = _preconvert_svgs(page_body, tmpdir)
            cats = meta.get("categories") or []
            if isinstance(cats, str):
                cats = [cats]
            chunks.append(f"# {title} {{#{anchor}}}\n\n{page_body}\n")
            pages.append(TreePage(p, title, anchor, list(cats)))
            # Also expose this page's folder to pandoc's resource search.
            if p.parent not in resource_paths:
                resource_paths.append(p.parent)

        assembled = "\n\n".join(chunks)
        pdf_bytes = _pandoc_to_pdf(
            assembled,
            title=doc_title,
            engine=engine,
            toc=True,
            preamble=preamble,
            resource_paths=resource_paths,
        )
    return pdf_bytes, pages


def _default_output(src: str) -> Path:
    return Path(Path(src).stem + ".pdf")


def main() -> None:
    ap = argparse.ArgumentParser(description="Render managed Markdown to PDF.")
    ap.add_argument(
        "path", help="a .md file (single-page) or a directory (with --tree)"
    )
    ap.add_argument("-o", "--output", help="output PDF path")
    ap.add_argument(
        "--engine",
        default="xelatex",
        help="pandoc --pdf-engine (xelatex, lualatex, weasyprint, ...). "
        "Default: xelatex.",
    )
    ap.add_argument(
        "--tree",
        action="store_true",
        help="render every managed:true page under path/ into one bound PDF "
        "(managed:false pages -- meta notes, drafts -- are excluded, no override)",
    )
    ap.add_argument(
        "--doc-title",
        default="Gramps Wiki Manual",
        help="(--tree only) PDF document title",
    )
    ap.add_argument(
        "--preamble",
        help="path to a LaTeX preamble file to --include-in-header "
        "(overrides the built-in default)",
    )
    ap.add_argument(
        "--no-preamble",
        action="store_true",
        help="suppress the default LaTeX preamble entirely",
    )
    args = ap.parse_args()

    if args.no_preamble:
        preamble: str | None = None
    elif args.preamble:
        preamble = Path(args.preamble).read_text(encoding="utf-8")
    else:
        preamble = DEFAULT_LATEX_PREAMBLE

    try:
        if args.tree:
            root = Path(args.path)
            if not root.is_dir():
                sys.exit(f"md2pdf: --tree requires a directory: {root}")
            pdf_bytes, pages = convert_tree(
                root,
                doc_title=args.doc_title,
                engine=args.engine,
                preamble=preamble,
            )
            out = Path(args.output) if args.output else Path("manual.pdf")
            out.write_bytes(pdf_bytes)
            print(
                f"wrote {out} ({len(pdf_bytes)} bytes, {len(pages)} pages, "
                f"title={args.doc_title!r})"
            )
        else:
            page = convert_file(args.path, engine=args.engine, preamble=preamble)
            out = Path(args.output) if args.output else _default_output(args.path)
            out.write_bytes(page.pdf_bytes)
            print(f"wrote {out} ({len(page.pdf_bytes)} bytes, title={page.title!r})")
    except Exception as e:
        sys.exit(f"md2pdf: {args.path}: {e}")


if __name__ == "__main__":
    main()
