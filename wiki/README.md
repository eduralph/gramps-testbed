# wiki/ — docs-as-code for the Gramps wiki

Markdown in `pages/` is the source of truth. `tools/` converts it to wikitext
and publishes it to the Gramps MediaWiki. **One-way: repo → wiki.**

```
wiki/
├── pages/
│   ├── 00 - meta/                    # repo-side notes (managed: false by convention)
│   ├── 01 - preliminary notes/       # drafts / scratch
│   ├── 02 - templates/               # Obsidian "Templates" plugin source (NEVER published)
│   ├── 03 - User guide/              # end-user documentation
│   ├── 04 - Technical Documentation/ # internals, architecture, contributor reference
│   └── 05 - Addon development/       # addon authors' manual
├── tools/                            # converter + publisher + browser transport — STAYS here
└── .wikisync/                        # publish state (committed): one sidecar per page, mirrors pages/
```

The folder names use Obsidian's "NN - " sort prefix so they order visibly in
the file explorer; rename, renumber, add, or remove content folders freely.
`publish.py` walks all of `pages/`, strips the `NN - ` prefix only when
matching the special `templates` segment, and is otherwise structure-agnostic
— the `managed: true` flag in front-matter is the publish allowlist for
everything that isn't a template.

The `pages/` ↔ `tools/` split is deliberate: when/if upstream maintains addon
docs in-repo, the relevant content folder (today `05 - Addon development/`)
moves with a `git mv` and the tooling stays behind. Keep the content trees
transport-agnostic — no tool cruft inside them — so whoever renders them next
(this rig, or upstream CI) just points at clean markdown.

The templates folder holds the seed file(s) for Obsidian's core Templates
plugin (point its template folder there). `publish.py` skips any
`templates`-named segment (`templates/`, `02 - templates/`, etc.)
unconditionally, so templates can carry `managed: true` — making a
freshly-copied page push-ready — without the template itself ever being
pushable.

## Authoring a page

Each `.md` starts with YAML front-matter. The wiki page identity lives here, not
in the file path, so the tree can be relocated without breaking the mapping.

```markdown
---
title: "Gramps 6.0 Wiki Manual - Addon Development"   # required: the wiki title
categories: ["Addons", "Developers", "Gramps 6.0"]    # appended as [[Category:…]]
managed: true                                          # ONLY managed pages are pushed
---

## Start at H2 — the title is the implicit H1 (from front-matter)
```

`managed: true` is the allowlist. A page without it is converted on demand but
never pushed — you don't unilaterally own canonical wiki pages.

### Two markup conveniences (so the same .md renders on GitHub *and* the wiki)

- **Templates** — author as an HTML comment: `<!--wiki:{{man index|6.0}}-->`.
  GitHub hides it; the converter emits raw `{{man index|6.0}}`. Works inline or
  as a block. This is what keeps GitHub rendering clean while still producing
  wiki templates.
- **Internal links** — author as `[label](wiki:Page_Name)`. GitHub shows a link;
  the converter emits `[[Page_Name|label]]` (or `[[Page_Name]]` if identical).

Everything else is plain GitHub-Flavored Markdown.

## Convert (no wiki, no browser)

```
python3 tools/md2wiki.py "pages/05 - Addon development/addon-development.md"          # prints wikitext
python3 tools/md2wiki.py "pages/05 - Addon development/addon-development.md" --json    # title+cats+text
```

## Publish

Dry-run is the default and pushes nothing — it prints what *would* happen:

```
python3 tools/publish.py                       # plan over all managed pages
python3 tools/publish.py --filter addon        # only sources matching 'addon'
python3 tools/publish.py --apply               # actually push
python3 tools/publish.py --apply --force       # push over drift / adopt / deleted
```

`--apply` launches (or reattaches to) your cleared Chrome via the same attached-
browser rig as `wiki_write_probe.py`, pauses once for the Cloudflare-clear +
login, then issues every API call as a same-origin XHR through that session.
**This runs on your workstation, not CI** — a GitHub runner has no cleared
session. Trigger it as a `make publish-wiki` after merging doc changes.

Without `--apply` there is no browser at all: the dry-run reasons from the
sidecars only (it reports CREATE / SKIP / UPDATE but cannot check live drift).
Run a dry-run to sanity-check the plan, then `--apply` to get the live picture
and push.

## The safety model

- **Managed allowlist** — only `managed: true` pages are ever written.
- **Dry-run default** — `--apply` is the explicit opt-in to editing a live
  community wiki.
- **Drift detection (keyed on revid)** — each push records the resulting revid
  in `.wikisync/<path>.json`. Before re-pushing, the live revid is compared to
  the recorded one; a mismatch means a human edited the page since our push, so
  we STOP on that page rather than clobber (override with `--force`). Keying on
  revid, not content, means MediaWiki's save-time normalisation never reads as
  false drift.
- **Change detection (keyed on content hash)** — unchanged sources are SKIPped,
  so re-runs don't flood Recent Changes with null edits.
- **Conflict-safe writes** — every edit carries `basetimestamp`/`starttimestamp`,
  so a concurrent human edit between read and write fails with `editconflict`
  instead of overwriting.
- **Provenance** — edit summaries carry `Synced from repo@<sha>` (set `GIT_SHA`
  or run inside the repo) so every wiki revision points back at its commit.

## Future: when this can become CI

The only thing tying publishing to your workstation is the Cloudflare wall on
write XHRs. If Gramps infra ever allowlists a bot token at the WAF, swap
`tools/wikitransport.py` for a plain `requests` session doing `action=login`
with a `Special:BotPasswords` credential. The publisher, converter, drift model,
and sidecars are unchanged — only the transport swaps, and then it can run in
GitHub Actions. That's also the moment to mark edits with the `bot` flag for
real (it needs the bot user-right; harmless-but-ignored without it today).

## Tests

```
cd tools && python3 test_decide.py     # pins the drift decision matrix, offline
```

## Dependencies

- `pandoc` (system package)
- `pip install pyyaml playwright` — no `playwright install` needed; the transport
  attaches to *your* Chrome, not the bundled chromium.
