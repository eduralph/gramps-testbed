#!/usr/bin/env python3
"""publish -- push managed Markdown pages to the Gramps wiki.

Repo is the source of truth; the wiki is a render target. One-way.

Safety model (the load-bearing part):
  * Only pages with `managed: true` front-matter are ever touched.
  * DRY-RUN IS THE DEFAULT. It prints a plan and pushes nothing. `--apply` opts
    in to actually editing the live community wiki.
  * Drift detection: each push records the resulting revid in a sidecar under
    the state dir. Before re-pushing, the live revid is compared to the recorded
    one. If they differ, a HUMAN edited the page since our last push -- we STOP
    on that page (warn, skip) rather than clobber, unless `--force`.
  * Drift is keyed on REVID, not content hash, so MediaWiki's save-time
    normalisation never reads as false drift.
  * Change detection (whether to push at all) is keyed on a content hash of the
    generated wikitext, so unchanged sources are SKIPped -- no null edits
    flooding Recent Changes.
  * Pushes pass basetimestamp/starttimestamp so a concurrent human edit between
    our read and our write fails with editconflict instead of overwriting.

Usage:
  python3 publish.py                      # dry-run plan over all managed pages
  python3 publish.py --apply              # actually push
  python3 publish.py --apply --force      # push even over drift / adopt
  python3 publish.py --docs-root pages --state-dir .wikisync
  python3 publish.py --filter addon       # only sources whose path contains 'addon'
  python3 publish.py --no-login           # skip the interactive-login pause
"""

from __future__ import annotations

import argparse
import glob
import hashlib
import json
import os
import re
import sys
import time
from dataclasses import dataclass
from pathlib import Path

import md2wiki
import mdcommon

# Strip an Obsidian-style "NN - " sort prefix from a folder name before
# comparing it, so "templates", "02 - templates", "10-Templates" all collapse
# to "templates". Pattern: leading digits, optional whitespace, dash, optional
# whitespace.
_PREFIX_RE = re.compile(r"^\d+\s*-\s*")


def _segment_name(seg: str) -> str:
    return _PREFIX_RE.sub("", seg).lower()


# Actions
CREATE = "CREATE"
UPDATE = "UPDATE"
SKIP = "SKIP"
DRIFT = "DRIFT"
ADOPT_CONFLICT = "ADOPT-CONFLICT"
DELETED_ON_WIKI = "DELETED-ON-WIKI"


def sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def decide(
    *,
    sidecar: dict | None,
    live_exists: bool,
    live_revid: int | None,
    generated_hash: str,
) -> tuple[str, str]:
    """Pure decision: what should happen to this page? Returns (action, reason).
    --force handling lives in the caller; this reports the true state."""
    if sidecar is None:
        if not live_exists:
            return CREATE, "no local record, not on wiki -> create"
        return ADOPT_CONFLICT, (
            "no local record but page EXISTS on wiki -- "
            "created/owned elsewhere; refusing to adopt"
        )
    # we have published this page before
    if not live_exists:
        return DELETED_ON_WIKI, "we published it, but it's gone from the wiki now"
    if live_revid != sidecar.get("pushed_revid"):
        return DRIFT, (
            f"wiki revid {live_revid} != our recorded "
            f"{sidecar.get('pushed_revid')} -- edited since our push"
        )
    if generated_hash == sidecar.get("generated_hash"):
        return SKIP, "source unchanged since last push"
    return UPDATE, "source changed, wiki untouched since our push -> update"


# ---- sidecar state ----------------------------------------------------------


def _prefix_slug(title_prefix: str) -> str:
    """Slugify a ``--title-prefix`` for use as a sidecar-directory segment.
    Empty prefix -> empty slug (default flat layout). Non-empty -> a leading
    underscore + ascii-safe slug so canonical pushes and prefixed pushes
    don't share sidecars (which would make a fresh sandbox publish look
    like 'we published this before to the canonical page').
    """
    if not title_prefix:
        return ""
    safe = re.sub(r"[^A-Za-z0-9._-]+", "_", title_prefix.strip("/")).strip("_")
    return f"_prefix-{safe}" if safe else ""


def sidecar_path(
    state_dir: str, docs_root: str, source: str, title_prefix: str = ""
) -> str:
    rel = os.path.relpath(source, docs_root)
    slug = _prefix_slug(title_prefix)
    if slug:
        return os.path.join(state_dir, slug, rel + ".json")
    return os.path.join(state_dir, rel + ".json")


def load_sidecar(path: str) -> dict | None:
    if not os.path.exists(path):
        return None
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def save_sidecar(path: str, data: dict) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")


# ---- planning ---------------------------------------------------------------


@dataclass
class PlanItem:
    source: str
    title: str
    action: str
    reason: str
    page: md2wiki.ConvertedPage
    generated_hash: str
    live: object = None  # LivePage when a transport was used


def discover(docs_root: str, filt: str | None) -> list[str]:
    paths = sorted(glob.glob(os.path.join(docs_root, "**", "*.md"), recursive=True))

    # Never publish anything under a templates/ subtree. Templates ship with
    # `managed: true` so a freshly-copied page is push-ready; without this
    # filter the template itself would also be pushable. The segment match is
    # robust to Obsidian "NN - " sort prefixes so "templates", "02 - templates",
    # etc. all collapse to the same thing.
    def _under_templates(path: str) -> bool:
        rel = os.path.relpath(path, docs_root)
        return any(_segment_name(seg) == "templates" for seg in rel.split(os.sep))

    paths = [p for p in paths if not _under_templates(p)]
    if filt:
        paths = [p for p in paths if filt in p]
    return paths


def provenance_summary() -> str:
    sha = os.environ.get("GIT_SHA")
    if not sha:
        sha = _git_short_sha()
    return f"Synced from repo{('@' + sha) if sha else ''} via publish.py"


def _git_short_sha() -> str | None:
    try:
        import subprocess

        out = subprocess.run(
            ["git", "rev-parse", "--short", "HEAD"], capture_output=True, text=True
        )
        return out.stdout.strip() or None
    except Exception:
        return None


def build_plan(
    transport,
    docs_root: str,
    state_dir: str,
    filt: str | None,
    *,
    title_prefix: str = "",
    strip_categories: bool = False,
) -> list[PlanItem]:
    plan: list[PlanItem] = []
    # Build the title map ONCE across the whole docs tree -- a page in any
    # folder can reference any other via [[Stem]]. md2wiki.convert_file
    # defaults to scanning the source file's parent, which is too narrow
    # for cross-folder references.
    title_map = mdcommon.build_title_map(Path(docs_root))

    # Two-pass over the discovered sources: pass 1 collects the canonical
    # titles of the pages that are actually in this publish batch (managed
    # AND matched by --filter), so pass 2 can pass that set to md2wiki for
    # the in-batch wiki:-link prefix rewriting. Without this, the converter
    # can't tell "in-batch (rewrite)" from "out-of-batch (leave alone)".
    sources = discover(docs_root, filt)
    inbatch_titles: set[str] = set()
    src_meta: list[tuple[str, dict]] = []
    for src in sources:
        try:
            with open(src, encoding="utf-8") as f:
                head_text = f.read()
        except OSError:
            continue
        try:
            meta, _ = md2wiki.split_frontmatter(head_text)
        except ValueError:
            continue
        src_meta.append((src, meta))
        if meta.get("managed", False) and meta.get("title"):
            inbatch_titles.add(str(meta["title"]))

    for src, meta in src_meta:
        # Cheap front-matter peek: we only want to RUN md2wiki on pages we
        # intend to publish. Unmanaged drafts may contain content that
        # md2wiki rejects (rare but real -- e.g. a scraped page with
        # [[...]]-looking content in an indented code block); failing the
        # whole plan because of an unrelated draft is unhelpful.
        if not meta.get("managed", False):
            continue
        page = md2wiki.convert_file(
            src,
            title_map=title_map,
            title_prefix=title_prefix,
            inbatch_canonical_titles=inbatch_titles,
            strip_categories=strip_categories,
        )
        if not page.managed:
            continue
        ghash = sha256(page.wikitext)
        sc = load_sidecar(sidecar_path(state_dir, docs_root, src, title_prefix))
        if transport is not None:
            live = transport.get_page(page.title)
            action, reason = decide(
                sidecar=sc,
                live_exists=live.exists,
                live_revid=live.revid,
                generated_hash=ghash,
            )
        else:  # offline plan -- can only reason from the sidecar
            live = None
            if sc is None:
                action, reason = CREATE, "no local record (offline; wiki not checked)"
            elif ghash == sc.get("generated_hash"):
                action, reason = SKIP, "source unchanged (offline)"
            else:
                action, reason = UPDATE, "source changed (offline; drift unchecked)"
        plan.append(PlanItem(src, page.title, action, reason, page, ghash, live))
    return plan


def print_plan(plan: list[PlanItem]) -> None:
    width = max((len(p.action) for p in plan), default=6)
    for p in plan:
        print(f"  {p.action:<{width}}  {p.title}")
        print(f"  {'':<{width}}  ({p.source}) {p.reason}")
    counts: dict[str, int] = {}
    for p in plan:
        counts[p.action] = counts.get(p.action, 0) + 1
    print("\nsummary:", ", ".join(f"{k}={v}" for k, v in sorted(counts.items())))


# ---- apply ------------------------------------------------------------------

PUSHABLE = {CREATE, UPDATE}
FORCEABLE = {DRIFT, ADOPT_CONFLICT, DELETED_ON_WIKI}

# Default location of media files referenced from a page, relative to the
# page's own folder. Matches the scrape_wiki / Obsidian convention.
MEDIA_SUBDIR = "_media"


def upload_media_for(transport, item: PlanItem, summary: str) -> int:
    """Upload every File: reference in ``item.page.wikitext`` from the
    sibling ``_media/`` folder. SHA-1 skip-if-unchanged.

    Returns the number of failures. Prints one line per file action
    (CREATE / UPDATE / SKIP / WARN / FAIL).
    """
    media_dir = Path(item.source).parent / MEDIA_SUBDIR
    failures = 0
    seen: set[str] = set()
    for basename in mdcommon.extract_file_basenames(item.page.wikitext):
        if basename in seen:
            continue  # already handled this file for this page
        seen.add(basename)
        local = media_dir / basename
        if not local.exists():
            print(f"  WARN  media {basename}: not found at {local}")
            failures += 1
            continue
        try:
            token = transport.csrf_token()
            action, _resp = transport.upload_if_changed(
                filename=basename,
                path=local,
                token=token,
                comment=summary,
            )
            print(f"  {action:<6}  media {basename}")
        except Exception as e:  # noqa: BLE001 -- network/wiki errors vary
            print(f"  FAIL  media {basename}: {e}")
            failures += 1
    return failures


def apply_plan(
    transport,
    plan: list[PlanItem],
    state_dir: str,
    docs_root: str,
    force: bool,
    bot: bool,
    *,
    title_prefix: str = "",
) -> int:
    summary = provenance_summary()
    failures = 0
    for p in plan:
        do_push = p.action in PUSHABLE or (force and p.action in FORCEABLE)
        if not do_push:
            print(f"  skip  {p.title} [{p.action}]")
            continue
        # Upload referenced media FIRST so the edited page never references
        # a missing file (even briefly between edit and uploads).
        media_failures = upload_media_for(transport, p, summary)
        if media_failures:
            print(
                f"  abort {p.title}: {media_failures} media upload(s) failed; "
                f"skipping page edit so the wiki doesn't show red File: refs"
            )
            failures += media_failures
            continue
        token = transport.csrf_token()
        create_only = (p.action == CREATE) and not force
        base_ts = p.live.timestamp if (p.live and p.live.exists) else None
        start_ts = p.live.curtimestamp if p.live else None
        result = transport.edit(
            title=p.title,
            text=p.page.wikitext,
            summary=summary,
            token=token,
            base_timestamp=base_ts,
            start_timestamp=start_ts,
            create_only=create_only,
            bot=bot,
        )
        if "error" in result:
            failures += 1
            print(
                f"  FAIL  {p.title}: {result['error'].get('code')} -> "
                f"{result['error'].get('info')}"
            )
            continue
        edit = result.get("edit", {})
        if edit.get("result") != "Success":
            failures += 1
            print(f"  FAIL  {p.title}: unexpected response {result}")
            continue
        new_revid = edit.get("newrevid") or edit.get("oldrevid")
        save_sidecar(
            sidecar_path(state_dir, docs_root, p.source, title_prefix),
            {
                "title": p.title,
                "source": os.path.relpath(p.source, docs_root),
                "pushed_revid": new_revid,
                "generated_hash": p.generated_hash,
                "last_pushed": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            },
        )
        print(f"  OK    {p.title} [{p.action}] -> revid {new_revid}")
    return failures


def main() -> None:
    ap = argparse.ArgumentParser(description="Publish managed Markdown to the wiki.")
    ap.add_argument("--docs-root", default="pages")
    ap.add_argument("--state-dir", default=".wikisync")
    ap.add_argument("--filter", dest="filt", default=None)
    ap.add_argument(
        "--apply", action="store_true", help="actually push (default: dry-run)"
    )
    ap.add_argument(
        "--force", action="store_true", help="push over drift/adopt/deleted"
    )
    ap.add_argument("--no-bot", action="store_true", help="don't flag edits as bot")
    ap.add_argument(
        "--no-login", action="store_true", help="skip interactive login pause"
    )
    ap.add_argument(
        "--title-prefix",
        default="",
        help=(
            'prepend to every published title and to in-batch wiki: link '
            'targets, e.g. "User:Eduralph/Sandbox/". Sidecars are kept '
            "under a separate subdirectory per prefix so canonical and "
            "sandbox publishes don't share state."
        ),
    )
    ap.add_argument(
        "--keep-categories",
        action="store_true",
        help=(
            "keep [[Category:X]] trailers even when --title-prefix starts "
            "with 'User:' (default: auto-strip for User-namespace pushes so "
            "the sandbox page doesn't show up in public category indexes)"
        ),
    )
    args = ap.parse_args()

    # Auto-strip categories for User-namespace prefixes unless overridden.
    strip_categories = (
        args.title_prefix.startswith("User:") and not args.keep_categories
    )

    if not os.path.isdir(args.docs_root):
        sys.exit(f"docs-root not found: {args.docs_root}")

    transport = None
    pw = browser = None
    if args.apply:
        import wikitransport

        pw, browser, transport = wikitransport.connect(
            interactive_login=not args.no_login
        )
        who = transport.userinfo()
        if who.get("id", 0) == 0 or "anon" in who:
            pw.stop()
            sys.exit(f"Not logged in (userinfo={who}). Log into the wiki first.")
        print(f"Authenticated as {who.get('name')} (id {who.get('id')})\n")

    try:
        plan = build_plan(
            transport,
            args.docs_root,
            args.state_dir,
            args.filt,
            title_prefix=args.title_prefix,
            strip_categories=strip_categories,
        )
        if not plan:
            print("No managed pages found.")
            return
        print_plan(plan)
        if not args.apply:
            print("\n(dry-run -- nothing pushed. Re-run with --apply to push.)")
            return
        print("\napplying:")
        failures = apply_plan(
            transport,
            plan,
            args.state_dir,
            args.docs_root,
            force=args.force,
            bot=not args.no_bot,
            title_prefix=args.title_prefix,
        )
        if failures:
            sys.exit(f"\n{failures} page(s) failed.")
    finally:
        if pw is not None:
            pw.stop()


if __name__ == "__main__":
    main()
