#!/usr/bin/env python3
"""wikitransport -- talk to the MediaWiki API through your already-cleared real
Chrome (attach mode over CDP), the rig proven by wiki_write_probe.py.

Every call is a same-origin fetch issued from inside a page on the wiki origin,
so it rides the interactive cf_clearance + login session. This is NOT a headless
client and cannot run in CI; it runs on your workstation against the browser you
logged into. (When/if Gramps infra allowlists a bot token at the WAF, swap this
module for a plain `requests` session doing action=login with a BotPasswords
credential -- the publisher above it stays identical.)
"""

from __future__ import annotations

import base64
import hashlib
import mimetypes
import os
import shutil
import subprocess
import sys
import time
import urllib.request
from dataclasses import dataclass
from pathlib import Path

from playwright.sync_api import sync_playwright

PORT = 9222
CDP_URL = f"http://localhost:{PORT}"
WIKI_ORIGIN = "https://www.gramps-project.org"
ANCHOR_URL = WIKI_ORIGIN + "/wiki/index.php/Main_Page"
API_PATH = "/wiki/api.php"

CHROME_BINARY = ""
CHROME_CANDIDATES = [
    "google-chrome",
    "google-chrome-stable",
    "chromium",
    "chromium-browser",
]
PROFILE_DIR = os.path.expanduser("~/.cache/wiki-probe-chrome")


# ---- browser lifecycle ------------------------------------------------------


def _cdp_up() -> bool:
    try:
        with urllib.request.urlopen(f"{CDP_URL}/json/version", timeout=1) as r:
            return r.status == 200
    except Exception:
        return False


def _resolve_chrome() -> str:
    if CHROME_BINARY:
        return CHROME_BINARY
    for name in CHROME_CANDIDATES:
        path = shutil.which(name)
        if path:
            return path
    sys.exit("No Chrome/Chromium binary found on PATH; set CHROME_BINARY.")


def _launch_chrome() -> subprocess.Popen:
    binary = _resolve_chrome()
    os.makedirs(PROFILE_DIR, exist_ok=True)
    args = [
        binary,
        f"--remote-debugging-port={PORT}",
        f"--user-data-dir={PROFILE_DIR}",
        "--no-first-run",
        "--no-default-browser-check",
        ANCHOR_URL,
    ]
    print(f"Launching {binary} (profile {PROFILE_DIR}, CDP {PORT})")
    return subprocess.Popen(args, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def _wait_for_cdp(timeout: int = 30) -> bool:
    deadline = time.time() + timeout
    while time.time() < deadline:
        if _cdp_up():
            return True
        time.sleep(0.5)
    return False


# ---- the JS that runs inside the cleared page -------------------------------

_JS_GET = r"""
async (cfg) => {
  const u = cfg.api
    + '?action=query&prop=revisions&rvprop=ids|content|timestamp'
    + '&rvslots=main&formatversion=2&curtimestamp=1&format=json'
    + '&titles=' + encodeURIComponent(cfg.title);
  const r = await fetch(u, { credentials: 'same-origin',
                             headers: { Accept: 'application/json' } });
  const t = await r.text();
  let j; try { j = JSON.parse(t); }
  catch { return { ok:false, challenge:/cloudflare|just a moment|cf-chl/i.test(t),
                   status:r.status, raw:t.slice(0,400) }; }
  const page = j.query.pages[0];
  if (page.missing) return { ok:true, exists:false, curtimestamp:j.curtimestamp };
  const rev = page.revisions[0];
  // MW 1.32+ with rvslots=main returns content under rev.slots.main.content;
  // older MW (or when rvslots is ignored) returns content at the top level
  // for backward compatibility. Accept either shape.
  const content = (rev.slots && rev.slots.main)
                    ? rev.slots.main.content
                    : rev.content;
  if (content === undefined) {
    return { ok:false, status:r.status,
             raw:'unexpected revision shape: ' + JSON.stringify(rev).slice(0,400) };
  }
  return { ok:true, exists:true, revid:rev.revid, timestamp:rev.timestamp,
           content:content, curtimestamp:j.curtimestamp };
}
"""

_JS_TOKEN = r"""
async (cfg) => {
  const r = await fetch(cfg.api + '?action=query&meta=tokens&type=csrf&format=json',
    { credentials:'same-origin', headers:{ Accept:'application/json' } });
  const t = await r.text();
  try { return { ok:true, token: JSON.parse(t).query.tokens.csrftoken }; }
  catch { return { ok:false, challenge:/cloudflare|just a moment|cf-chl/i.test(t),
                   raw:t.slice(0,400) }; }
}
"""

_JS_USERINFO = r"""
async (cfg) => {
  const r = await fetch(cfg.api + '?action=query&meta=userinfo&format=json',
    { credentials:'same-origin', headers:{ Accept:'application/json' } });
  const t = await r.text();
  try { return { ok:true, userinfo: JSON.parse(t).query.userinfo }; }
  catch { return { ok:false, challenge:/cloudflare|just a moment|cf-chl/i.test(t),
                   raw:t.slice(0,400) }; }
}
"""

_JS_FILE_INFO = r"""
async (cfg) => {
  const u = cfg.api
    + '?action=query&prop=imageinfo&iiprop=sha1|size'
    + '&format=json&formatversion=2'
    + '&titles=' + encodeURIComponent('File:' + cfg.filename);
  const r = await fetch(u, { credentials: 'same-origin',
                             headers: { Accept: 'application/json' } });
  const t = await r.text();
  let j; try { j = JSON.parse(t); }
  catch { return { ok:false, challenge:/cloudflare|just a moment|cf-chl/i.test(t),
                   status:r.status, raw:t.slice(0,400) }; }
  const page = j.query.pages[0];
  if (page.missing) return { ok:true, exists:false };
  const ii = (page.imageinfo && page.imageinfo[0]) || null;
  return { ok:true, exists:true,
           sha1: ii ? ii.sha1 : null,
           size: ii ? ii.size : null };
}
"""

_JS_UPLOAD = r"""
async (cfg) => {
  // Decode base64 file content to a Blob -- multipart/form-data needs the
  // raw bytes, and Playwright's evaluate() can only marshal JSON-safe args.
  const raw = atob(cfg.b64);
  const bytes = new Uint8Array(raw.length);
  for (let i = 0; i < raw.length; i++) bytes[i] = raw.charCodeAt(i);
  const blob = new Blob([bytes], { type: cfg.mime });
  const fd = new FormData();
  fd.set('action', 'upload');
  fd.set('format', 'json');
  fd.set('filename', cfg.filename);
  fd.set('comment', cfg.comment);
  fd.set('token', cfg.token);
  if (cfg.ignoreWarnings) fd.set('ignorewarnings', '1');
  fd.set('file', blob, cfg.filename);
  const r = await fetch(cfg.api, { method: 'POST', credentials: 'same-origin',
                                   body: fd });
  const t = await r.text();
  try { return { ok:true, status:r.status, json: JSON.parse(t) }; }
  catch { return { ok:false, status:r.status,
                   challenge:/cloudflare|just a moment|cf-chl/i.test(t),
                   raw:t.slice(0,600) }; }
}
"""

_JS_EDIT = r"""
async (cfg) => {
  const b = new URLSearchParams();
  b.set('action','edit'); b.set('format','json'); b.set('formatversion','2');
  b.set('title', cfg.title); b.set('text', cfg.text);
  b.set('summary', cfg.summary); b.set('token', cfg.token);
  if (cfg.bot)            b.set('bot','1');
  if (cfg.createOnly)     b.set('createonly','1');
  if (cfg.baseTimestamp)  b.set('basetimestamp', cfg.baseTimestamp);
  if (cfg.startTimestamp) b.set('starttimestamp', cfg.startTimestamp);
  const r = await fetch(cfg.api, { method:'POST', credentials:'same-origin',
    headers:{ 'Content-Type':'application/x-www-form-urlencoded',
              Accept:'application/json' }, body:b.toString() });
  const t = await r.text();
  try { return { ok:true, status:r.status, json: JSON.parse(t) }; }
  catch { return { ok:false, status:r.status,
                   challenge:/cloudflare|just a moment|cf-chl/i.test(t),
                   raw:t.slice(0,600) }; }
}
"""


@dataclass
class LivePage:
    exists: bool
    revid: int | None
    timestamp: str | None  # basetimestamp for conflict detection
    content: str | None
    curtimestamp: str  # starttimestamp for conflict detection


@dataclass
class LiveFile:
    """What the wiki currently has for a given File: title.

    ``sha1`` is MediaWiki's per-file SHA-1, computed over the actual upload
    bytes. Compare against ``sha1_file()`` locally to decide whether to skip
    or re-upload.
    """

    exists: bool
    sha1: str | None
    size: int | None


def sha1_file(path: Path) -> str:
    """Compute the SHA-1 of a file's bytes, matching MediaWiki's imageinfo
    ``sha1`` property so a local-vs-wiki equality check is meaningful."""
    h = hashlib.sha1()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def _guess_mime(path: Path) -> str:
    """Best-effort MIME type for upload. SVG isn't always in the system DB,
    so we hard-code the ones the docs pipeline cares about."""
    overrides = {
        ".svg": "image/svg+xml",
        ".png": "image/png",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".gif": "image/gif",
        ".pdf": "application/pdf",
    }
    ext = path.suffix.lower()
    if ext in overrides:
        return overrides[ext]
    return mimetypes.guess_type(str(path))[0] or "application/octet-stream"


class WikiSession:
    """Wraps a Playwright page sitting on the wiki origin."""

    def __init__(self, page, api_path: str = API_PATH):
        self.page = page
        self.api = api_path

    def _eval(self, js: str, **extra):
        cfg = {"api": self.api, **extra}
        res = self.page.evaluate(js, cfg)
        if not res.get("ok"):
            if res.get("challenge"):
                raise RuntimeError(
                    "Cloudflare challenged the XHR -- session not "
                    "cleared. Open the wiki in the Chrome window "
                    "and pass the challenge, then retry."
                )
            raise RuntimeError(f"API call failed: {res}")
        return res

    def userinfo(self) -> dict:
        return self._eval(_JS_USERINFO)["userinfo"]

    def csrf_token(self) -> str:
        return self._eval(_JS_TOKEN)["token"]

    def get_page(self, title: str) -> LivePage:
        r = self._eval(_JS_GET, title=title)
        return LivePage(
            exists=r["exists"],
            revid=r.get("revid"),
            timestamp=r.get("timestamp"),
            content=r.get("content"),
            curtimestamp=r["curtimestamp"],
        )

    def edit(
        self,
        *,
        title: str,
        text: str,
        summary: str,
        token: str,
        base_timestamp: str | None = None,
        start_timestamp: str | None = None,
        create_only: bool = False,
        bot: bool = True,
    ) -> dict:
        r = self._eval(
            _JS_EDIT,
            title=title,
            text=text,
            summary=summary,
            token=token,
            bot=bot,
            createOnly=create_only,
            baseTimestamp=base_timestamp or "",
            startTimestamp=start_timestamp or "",
        )
        return r["json"]

    def file_info(self, filename: str) -> LiveFile:
        """Query the wiki for an existing File:<filename>.

        Returns a ``LiveFile`` with ``exists=False`` when the wiki has no
        such file, or ``exists=True`` plus the wiki's recorded SHA-1 and
        size when it does. Use ``sha1_file(local_path)`` to compare locally.
        """
        r = self._eval(_JS_FILE_INFO, filename=filename)
        return LiveFile(
            exists=bool(r.get("exists")),
            sha1=r.get("sha1"),
            size=r.get("size"),
        )

    def upload(
        self,
        *,
        filename: str,
        path: Path,
        token: str,
        comment: str,
        ignore_warnings: bool = False,
    ) -> dict:
        """Upload a local file as ``File:<filename>``.

        ``ignore_warnings`` is needed when re-uploading the same filename
        with new bytes -- MediaWiki returns ``warnings.exists`` otherwise
        and refuses the upload. The publisher only opts in after confirming
        via ``file_info`` that this is a genuine re-upload, not an accidental
        clobber.
        """
        with path.open("rb") as f:
            payload = f.read()
        b64 = base64.b64encode(payload).decode("ascii")
        r = self._eval(
            _JS_UPLOAD,
            filename=filename,
            b64=b64,
            mime=_guess_mime(path),
            token=token,
            comment=comment,
            ignoreWarnings=ignore_warnings,
        )
        return r["json"]

    def upload_if_changed(
        self,
        *,
        filename: str,
        path: Path,
        token: str,
        comment: str,
    ) -> tuple[str, dict | None]:
        """Skip-if-unchanged wrapper around ``upload``.

        Returns ``(action, response)`` where ``action`` is one of:
          * ``"SKIP"`` -- wiki already has this file with the same SHA-1.
          * ``"CREATE"`` -- file didn't exist; we uploaded it.
          * ``"UPDATE"`` -- file existed with different bytes; we re-uploaded.

        ``response`` is the MediaWiki ``action=upload`` JSON for the two
        upload paths, or ``None`` for SKIP.
        """
        local_sha1 = sha1_file(path)
        live = self.file_info(filename)
        if live.exists and live.sha1 == local_sha1:
            return "SKIP", None
        if live.exists:
            return "UPDATE", self.upload(
                filename=filename,
                path=path,
                token=token,
                comment=comment,
                ignore_warnings=True,
            )
        return "CREATE", self.upload(
            filename=filename,
            path=path,
            token=token,
            comment=comment,
            ignore_warnings=False,
        )


def connect(interactive_login: bool = True):
    """Launch-or-reattach Chrome and return (playwright, browser, WikiSession).

    Caller is responsible for stopping playwright when done. On a fresh launch
    this pauses for the manual Cloudflare-clear + login on an idle browser.
    """
    launched = False
    if _cdp_up():
        print(f"Reusing Chrome on {CDP_URL} (warm session).")
    else:
        _launch_chrome()
        launched = True
        if interactive_login:
            input(
                "\n>>> Chrome opened on the wiki. Clear Cloudflare, log in with "
                "an\n    edit-capable account, then press Enter to continue... "
            )
        if not _wait_for_cdp():
            sys.exit("Chrome did not expose the CDP port in time.")

    p = sync_playwright().start()
    browser = p.chromium.connect_over_cdp(CDP_URL)
    if not browser.contexts:
        sys.exit("Attached, but Chrome has no context/window open.")
    ctx = browser.contexts[0]
    page = next(
        (
            pg
            for c in browser.contexts
            for pg in c.pages
            if WIKI_ORIGIN in (pg.url or "")
        ),
        None,
    )
    if page is None:
        page = ctx.pages[0] if ctx.pages else ctx.new_page()
    if WIKI_ORIGIN not in (page.url or ""):
        page.goto(ANCHOR_URL, wait_until="domcontentloaded")
    return p, browser, WikiSession(page)
