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

import os
import shutil
import subprocess
import sys
import time
import urllib.request
from dataclasses import dataclass

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
  return { ok:true, exists:true, revid:rev.revid, timestamp:rev.timestamp,
           content:rev.slots.main.content, curtimestamp:j.curtimestamp };
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
