#!/usr/bin/env python3
"""
mantis_notes_playwright.py — pull Gramps Mantis issue notes/comments using a REAL
browser (Playwright), riding the Cloudflare clearance your own session earned.

Why this exists: the bug tracker sits behind Cloudflare, which challenges plain
HTTP clients (curl/requests) but lets real browsers through. This drives a real
browser, so there is no challenge to "defeat" — the browser passes it the normal way.

KEY IDEA: a *persistent* browser profile. You log in + clear Cloudflare ONCE by
hand in the launched window; the script reuses that cleared, authenticated session
for every subsequent issue. No credential handling in code, no fingerprint spoofing.

SETUP (one time):
  pip install --break-system-packages playwright
  # Do NOT run `playwright install chromium` on Ubuntu 26.04 — it fails
  # ("Playwright does not support chromium on ubuntu26.04-x64").
  # Instead use a system-installed Google Chrome (.deb, not snap):
  #   wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
  #   sudo apt install ./google-chrome-stable_current_amd64.deb

USAGE:
  # First run: a Chrome window opens. Log into the tracker and, if Cloudflare
  # shows a challenge, click it. Then press Enter in the terminal. The script
  # reuses this profile (./pw-profile) on every later run — usually no re-login.
  python3 mantis_notes_playwright.py --channel chrome --ids 13830,14051,13920
  python3 mantis_notes_playwright.py --channel chrome --csv Gramps__1_.csv --category "3rd Party Addons"
  # If --channel chrome can't find it, point explicitly:
  python3 mantis_notes_playwright.py --browser-path /usr/bin/google-chrome-stable --ids 13830

OUTPUT:
  notes_json/issue_<id>.json   one file per issue: fields + every note (author/date/text)
  notes_json/all_notes.json    combined

NOTES:
  - Run HEADED (default). Headless is far more likely to trip an interactive challenge.
  - Be polite: --delay defaults to 1.5s between issues. This is a volunteer project.
  - This reads pages you can already see as a logged-in user. It does not bypass
    any access control — it automates your own authenticated browsing.
"""

import argparse
import json
import re
import sys
import time
from pathlib import Path

BASE = "https://gramps-project.org/bugs"
VIEW = f"{BASE}/view.php?id="
PROFILE_DIR = Path("./pw-profile")  # persistent: keeps login + cf_clearance


def norm_id(raw: str) -> str:
    n = str(raw).strip().lstrip("0") or "0"
    return n


def load_ids(args) -> list[str]:
    if args.ids:
        return [norm_id(x) for x in args.ids.split(",") if x.strip()]
    # stdlib csv (no pandas) — keeps the scraper dependency-light (playwright only).
    import csv

    ids = []
    with open(args.csv, newline="", encoding="utf-8-sig") as fh:
        reader = csv.DictReader(fh)
        for raw in reader:
            row = {(k.strip() if k else k): (v or "") for k, v in raw.items()}
            if args.category and not args.all and row.get("Category") != args.category:
                continue
            ids.append(norm_id(row.get("Id", "")))
    return ids


def extract_issue(page, issue_id: str) -> dict:
    """Parse a Mantis view.php page that's already loaded in `page`."""
    # Mantis bugnotes live in elements with id like 'bugnote-<n>' or rows class 'bugnote'.
    # We grab author, timestamp, and text defensively across Mantis skins.
    data = page.evaluate(r"""
    () => {
      const txt = el => (el ? el.innerText.trim() : "");

      // --- summary ---
      let summary = "";
      const sumEl = document.querySelector(".bug-summary, td.bug-summary, span.bug-summary")
                 || document.querySelector("h1, .page-title");
      if (sumEl) summary = sumEl.innerText.trim();

      // --- top fields: Mantis renders <td class="category">Label</td><td>value</td> ---
      const fields = {};
      document.querySelectorAll("td.category").forEach(td => {
        const label = td.innerText.replace(/:$/,"").trim().toLowerCase();
        const val = td.nextElementSibling ? td.nextElementSibling.innerText.trim() : "";
        if (label) fields[label] = val;
      });

      // --- notes ---
      const notes = [];
      // Modern Mantis: each note is a table row group; ids like 'bugnote-12345'
      const noteNodes = document.querySelectorAll("[id^='bugnote-'], tr.bugnote, .bugnote");
      const seen = new Set();
      noteNodes.forEach(n => {
        const idm = (n.id || "").match(/bugnote-(\d+)/);
        const key = idm ? idm[1] : n.innerText.slice(0,40);
        if (seen.has(key)) return; seen.add(key);
        // author + date often in a header cell; text in a body cell
        const author = txt(n.querySelector(".bugnote-author, .username, a.user"))
                    || "";
        const date   = txt(n.querySelector(".bugnote-date, .date, .timestamp")) || "";
        // note body: prefer a dedicated text container, else whole node minus header
        let body = txt(n.querySelector(".bugnote-note, .bugnote-text, td.bugnote-public, td.bugnote-private"));
        if (!body) body = n.innerText.trim();
        notes.push({author, date, text: body});
      });

      return {summary, fields, notes};
    }
    """)
    data["id"] = issue_id
    data["url"] = VIEW + issue_id
    return data


def detect_block(page) -> str | None:
    """Return a string naming a non-issue page we landed on, or None if the page
    looks legitimate. Three distinct cases, handled differently by the caller:
      - 'cloudflare'    : interstitial challenge — retryable after you clear it
      - 'login'         : session expired / not logged in — retryable after login
      - 'access-denied' : Mantis says this issue is permission-restricted —
                          TERMINAL. Logging in won't help if your account lacks
                          view rights on this issue (private/developer-only bug).
    This is the fix for the silent-empty failure: each of these parses to 0 notes
    and was previously indistinguishable from a genuinely empty issue."""
    title = (page.title() or "").lower()
    try:
        body = (page.inner_text("body") or "").strip().lower()
    except Exception:
        body = ""

    if "just a moment" in title or "attention required" in title:
        return "cloudflare"

    # Mantis renders a permission failure as a tiny page: "Access Denied." with
    # Login / Proceed links. The issue EXISTS but this account can't view it.
    # Detect it by the short body text, not the title (title may be generic).
    if body.startswith("access denied") or (
        "access denied" in body and "login" in body and len(body) < 200
    ):
        return "access-denied"

    if "login" in title or "log in" in title or "sign in" in title:
        return "login"
    try:
        if page.query_selector(
            "input[name='username'], input[name='password'], form[action*='login']"
        ):
            return "login"
    except Exception:
        pass
    return None


def looks_like_issue_page(page, issue_id: str) -> bool:
    """Positive confirmation we're actually on the issue's view.php page BEFORE
    trusting any parse. A login/error/challenge page won't have the bug
    container. We require a positive signal rather than only checking for known
    bad titles — defends against future redirect shapes too."""
    try:
        if page.query_selector(
            "#view_all_bug_page, .bug-summary, td.bug-summary, td.category, [id^='bugnote-']"
        ):
            return True
        # fallback: the issue id is embedded in a hidden field on the view page
        if page.query_selector(f"input[value='{issue_id}']"):
            return True
    except Exception:
        pass
    return False


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ids")
    ap.add_argument("--csv")
    ap.add_argument("--category", default="3rd Party Addons")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--out", default="notes_json")
    ap.add_argument("--delay", type=float, default=1.5)
    ap.add_argument(
        "--headless",
        action="store_true",
        help="NOT recommended — Cloudflare interactive challenge needs a visible window",
    )
    ap.add_argument(
        "--channel",
        default="chrome",
        help="Playwright browser channel: 'chrome' (system Google Chrome .deb), "
        "'chromium', or 'msedge'. Use this to avoid Playwright's bundled-browser "
        "download, which fails on too-new distros like Ubuntu 26.04.",
    )
    ap.add_argument(
        "--browser-path",
        default=None,
        help="Explicit path to a browser binary, e.g. /usr/bin/google-chrome-stable. "
        "Overrides --channel. Use `which google-chrome-stable` to find it. "
        "Avoid snap-installed chromium — Playwright can't drive it reliably.",
    )
    ap.add_argument(
        "--attach",
        default=None,
        metavar="CDP_URL",
        help="Attach to a Chrome YOU started yourself, instead of launching one. "
        "Fixes the Cloudflare verification LOOP (Playwright's automation flags "
        "re-trigger the challenge). Start Chrome with:\n"
        "  google-chrome --remote-debugging-port=9222 --user-data-dir=/tmp/cfprofile <url>\n"
        "pass Cloudflare + log in by hand in that window, then run this with "
        "--attach http://127.0.0.1:9222",
    )
    args = ap.parse_args()

    ids = load_ids(args)
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)

    from playwright.sync_api import sync_playwright

    with sync_playwright() as p:
        launch_kwargs = dict(
            user_data_dir=str(PROFILE_DIR),
            headless=args.headless,
            viewport={"width": 1280, "height": 900},
        )
        owns_browser = True  # whether we launched it (and must close it)

        if args.attach:
            # ATTACH MODE: connect to a Chrome YOU started yourself with
            #   google-chrome --remote-debugging-port=9222 --user-data-dir=/tmp/cfprofile
            # You pass Cloudflare by hand in that normal Chrome (no automation flags
            # for Cloudflare to detect), then we attach over CDP and reuse the session.
            # This is the reliable fix for the Cloudflare verification LOOP, which is
            # caused by Playwright's own --enable-automation / navigator.webdriver
            # signals re-triggering the challenge after each pass.
            try:
                browser = p.chromium.connect_over_cdp(args.attach)
            except Exception as e:
                print(
                    f"\nCould not attach to Chrome at {args.attach}: {e}\n",
                    file=sys.stderr,
                )
                print(
                    "Start Chrome yourself first, in its own terminal:", file=sys.stderr
                )
                print(
                    "  google-chrome --remote-debugging-port=9222 \\", file=sys.stderr
                )
                print("    --user-data-dir=/tmp/cfprofile \\", file=sys.stderr)
                print(f"    '{VIEW}{ids[0]}'", file=sys.stderr)
                print(
                    "Pass Cloudflare + log in in THAT window, then run this with --attach http://127.0.0.1:9222",
                    file=sys.stderr,
                )
                sys.exit(1)
            ctx = browser.contexts[0] if browser.contexts else browser.new_context()
            owns_browser = False
            page = ctx.pages[0] if ctx.pages else ctx.new_page()
            print(
                "\nAttached to your Chrome. Make sure you've already passed Cloudflare"
            )
            print("and logged in in that window, with an issue page visible.")
            input("Press Enter to begin pulling issues... ")
        else:
            # LAUNCH MODE: Playwright starts the browser. Simpler, but Cloudflare may
            # loop on the challenge because of automation flags. If you hit that loop,
            # switch to --attach (see --help).
            if args.browser_path:
                launch_kwargs["executable_path"] = args.browser_path
            elif args.channel:
                launch_kwargs["channel"] = args.channel
            try:
                ctx = p.chromium.launch_persistent_context(**launch_kwargs)
            except Exception as e:
                print(f"\nFailed to launch browser: {e}\n", file=sys.stderr)
                print("Hints:", file=sys.stderr)
                print("  - Install Google Chrome (.deb, NOT snap):", file=sys.stderr)
                print(
                    "      wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb",
                    file=sys.stderr,
                )
                print(
                    "      sudo apt install ./google-chrome-stable_current_amd64.deb",
                    file=sys.stderr,
                )
                print("  - Then retry with:  --channel chrome", file=sys.stderr)
                print(
                    "  - Or point explicitly:  --browser-path /usr/bin/google-chrome-stable",
                    file=sys.stderr,
                )
                print(
                    "  - If Cloudflare LOOPS on the challenge, use --attach (see --help).",
                    file=sys.stderr,
                )
                sys.exit(1)
            page = ctx.pages[0] if ctx.pages else ctx.new_page()

            # Prime: load one issue so you can log in / clear Cloudflare by hand once.
            first = VIEW + ids[0]
            page.goto(first, wait_until="domcontentloaded")
            print("\n" + "=" * 70)
            print("A browser window is open. If you see a Cloudflare challenge or a")
            print("login page, handle it now in that window (log in, click the check).")
            print(
                "If the challenge keeps LOOPING, quit and re-run with --attach (see --help)."
            )
            print(
                "When the issue page is fully visible, come back here and press Enter."
            )
            print("=" * 70)
            input("Press Enter once the issue page is showing... ")

        records = []
        suspect = []  # blocked/empty/failed — retryable after fixing session
        restricted = []  # access-denied — TERMINAL, account lacks view rights
        for n, iid in enumerate(ids, 1):
            url = VIEW + iid
            try:
                page.goto(url, wait_until="domcontentloaded", timeout=30000)

                # Detect a non-issue page. Three cases, handled differently:
                blocked = detect_block(page)

                # TERMINAL: access-denied means this account can't view the issue
                # (private / developer-only / reporter-restricted). Logging in
                # won't help. Record and move on — do NOT pause, do NOT retry.
                if blocked == "access-denied":
                    print(
                        f"[{n}/{len(ids)}] #{iid}: ACCESS DENIED — issue is "
                        f"permission-restricted for your account. Not scrapeable; "
                        f"recording as restricted. (Needs tracker-admin view rights.)"
                    )
                    records.append(
                        {
                            "id": iid,
                            "url": url,
                            "summary": "",
                            "fields": {},
                            "notes": [],
                            "error": "access-denied-restricted",
                        }
                    )
                    restricted.append(iid)
                    time.sleep(args.delay)
                    continue

                # RETRYABLE: Cloudflare challenge or a login wall (session expired).
                # The login case is the bug that produced a false "0 notes" for
                # #13205-style pages: the script parsed the page and recorded no
                # notes as if the issue genuinely had none.
                if blocked:
                    print(
                        f"[{n}/{len(ids)}] #{iid}: hit a {blocked} page, not the issue "
                        f"— resolve it in the window (log in / clear challenge), then Enter"
                    )
                    input("  ...press Enter when the ISSUE page is showing... ")
                    page.goto(url, wait_until="domcontentloaded", timeout=30000)
                    blocked = detect_block(page)
                    if blocked == "access-denied":
                        print(
                            f"[{n}/{len(ids)}] #{iid}: ACCESS DENIED after login — "
                            f"account lacks view rights on this issue. Recording as restricted."
                        )
                        records.append(
                            {
                                "id": iid,
                                "url": url,
                                "summary": "",
                                "fields": {},
                                "notes": [],
                                "error": "access-denied-restricted",
                            }
                        )
                        restricted.append(iid)
                        time.sleep(args.delay)
                        continue
                    if blocked:
                        print(
                            f"[{n}/{len(ids)}] #{iid}: STILL on a {blocked} page — "
                            f"recording as ERROR (not 0-notes). Re-scrape after fixing session."
                        )
                        records.append(
                            {
                                "id": iid,
                                "url": url,
                                "summary": "",
                                "fields": {},
                                "notes": [],
                                "error": f"blocked:{blocked}",
                            }
                        )
                        suspect.append(iid)
                        time.sleep(args.delay)
                        continue

                # Positive confirmation we're on the real issue before trusting the parse.
                if not looks_like_issue_page(page, iid):
                    print(
                        f"[{n}/{len(ids)}] #{iid}: WARNING — page does not look like the "
                        f"issue (login redirect / session expiry?). Recording as ERROR, "
                        f"not 0-notes."
                    )
                    records.append(
                        {
                            "id": iid,
                            "url": url,
                            "summary": "",
                            "fields": {},
                            "notes": [],
                            "error": "not-an-issue-page",
                        }
                    )
                    suspect.append(iid)
                    time.sleep(args.delay)
                    continue

                rec = extract_issue(page, iid)
                nnotes = len(rec.get("notes", []))

                # An issue page with literally zero notes is possible but rare. If
                # we got 0 notes AND no summary AND no fields, it's almost certainly
                # a bad page that slipped past the guards — flag it suspect rather
                # than silently burying it as a legitimate NO-NOTES.
                if (
                    not rec.get("notes")
                    and not rec.get("summary")
                    and not rec.get("fields")
                ):
                    rec["suspect_empty"] = True
                    suspect.append(iid)
                    print(
                        f"[{n}/{len(ids)}] #{iid}: WARNING — empty parse (0 notes, no "
                        f"summary, no fields). Likely a blocked page; flagged suspect_empty."
                    )
                else:
                    print(f"[{n}/{len(ids)}] #{iid}: {nnotes} notes")

                records.append(rec)
                (out / f"issue_{iid}.json").write_text(
                    json.dumps(rec, indent=2, ensure_ascii=False), encoding="utf-8"
                )
            except Exception as e:
                print(f"[{n}/{len(ids)}] #{iid}: FAILED ({e})")
                suspect.append(iid)
            time.sleep(args.delay)

        (out / "all_notes.json").write_text(
            json.dumps(records, indent=2, ensure_ascii=False), encoding="utf-8"
        )
        if suspect:
            print(
                f"\n*** {len(suspect)} issue(s) blocked/empty/failed and need a re-scrape: "
                f"{','.join(suspect)}"
            )
            print(
                f"    After fixing the session, re-run with:  --ids {','.join(suspect)}"
            )
        if restricted:
            print(
                f"\n*** {len(restricted)} issue(s) are ACCESS-RESTRICTED (Access Denied) — "
                f"NOT scrapeable by this account: {','.join(restricted)}"
            )
            print(
                f"    These are private/developer-only tracker issues. Re-scraping won't "
                f"help without tracker view permissions. Handle their verdicts from the "
                f"CSV summary + tracker-admin access, or note them as restricted."
            )
        if owns_browser:
            ctx.close()
        print(f"\nDone. {len(records)} issues -> {out}/")


if __name__ == "__main__":
    main()
