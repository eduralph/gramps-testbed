---
title: "REPLACE ME — working title (free-form, not a wiki title yet)"
categories: []
managed: false
status: draft
---

<!--
  PRELIMINARY NOTES TEMPLATE — for in-flight thinking that isn't ready (and may
  never be ready) to ship to the wiki. Insert via Obsidian's core "Templates"
  plugin (folder set to pages/templates) into any note you're working on.

  Where this file lives is up to you. publish.py only pushes pages with
  `managed: true`, and these notes ship with `managed: false`, so they're
  safe to keep alongside content/ without leaking to the wiki. Suggested
  homes:
    pages/content/<slug>.md  -- if you expect this to grow into a wiki page;
                                flip `managed: true` and switch to the
                                matching per-folder template's structure
                                when ready (user-guide.md /
                                technical-documentation.md /
                                addon-development.md).
    elsewhere in the vault    -- if it's pure scratch / research / triage.

  Front-matter keys:
    title:      working title — rename freely; identity does NOT round-trip
                to a wiki page until you promote this note.
    categories: leave empty until promotion; wiki categories don't apply to
                drafts.
    managed:    KEEP false. Flipping to true makes publish.py push the page;
                only do that once the body is in proper publishable shape
                — see the matching per-folder template under
                pages/02 - templates/.
    status:     free-form. Useful values: draft, blocked, parked, ready.

  Obsidian-only conveniences (callouts, [[wikilinks]], dataview, embeds) are
  fine here — these notes are never converted by md2wiki.py. If you promote
  to a wiki page later, strip Obsidian-only constructs at that point.
-->

## Goal

<!-- One or two sentences: what is this note trying to figure out / capture?
     If you can't write it, the note isn't ready to exist yet. -->

## Context

<!-- Background: what triggered this? Link the bug / PR / thread / commit.
     Mantis bugs as plain numbers (no `#` — that auto-links in MantisBT but
     not here; spelling out "Mantis 12345" or [12345](https://gramps-project.org/bugs/view.php?id=12345)
     is unambiguous). -->

- Trigger:
- Related:

## Notes

<!-- The body of the thinking. Use whatever shape helps: prose, bullets,
     sub-headings, tables. Obsidian features welcome — callouts, embeds,
     dataview blocks. -->

> [!note]
> Obsidian callouts work here; they DO NOT survive promotion to a wiki page.

## Open questions

- [ ]

## References

<!-- Links worth keeping. Mix wikilinks to other notes, GitHub URLs, Mantis
     bug URLs, file paths. Whatever you want to find again. -->

- [[some-other-note]]
-

## Next step

<!-- The single concrete action that moves this forward, or the reason it's
     parked. If neither exists, the note is done — archive or delete. -->
