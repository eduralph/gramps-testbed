---
title: "REPLACE ME — free-form working title (e.g. Publisher drift model)"
categories: []
managed: false
status: active
---

<!--
  META PAGE TEMPLATE — for repo-side notes ABOUT the wiki workflow itself:
  publisher mechanics, converter conventions, drift model, decisions and
  their rationale, "how this rig works" reference. Lives under 00 - meta/
  by convention; the leading "00 - " prefix keeps it at the top of the
  Obsidian file explorer where setup/reference material belongs.

  How this template differs from the others:
    user-guide.md /
    technical-documentation.md /
    addon-development.md  — publishable content (managed: true); ship to
                            the wiki AND the bound PDF.
    preliminary-notes.md  — in-flight thinking; may or may not ship.
    meta-page.md (this)   — settled reference ABOUT the system; NEVER ships
                            to the wiki or PDF, lives only in the repo.

  Front-matter keys:
    title:      free-form. Not a wiki page title; pick what reads well in
                the file explorer and in cross-references.
    categories: leave empty. Wiki categories don't apply to repo-only notes.
    managed:    MUST stay false. publish.py honours this absolutely — a
                meta page with managed: true would push to the wiki, which
                is exactly what this folder exists NOT to do.
    status:     free-form. Suggested values: active, superseded, archived.
                "superseded" notes stay in the repo as history; add a link
                to the replacement at the top.

  Obsidian-only conveniences (callouts, [[wikilinks]], dataview, embeds)
  are fine here — these notes are never converted by md2wiki.py or
  md2pdf.py. Write for repo readers, not wiki readers.
-->

## Purpose

<!-- One or two sentences: what does this note document and who is it for?
     If you can't write it, the note isn't ready to exist yet. -->

## Context

<!-- Why this exists. What problem prompted writing it down, what prior
     state is being replaced or clarified. Link the commit / PR / issue
     that motivated it. -->

- Trigger:
- Related:

## Notes

<!-- The settled content. Architecture sketch, decision + rationale,
     workflow steps, gotcha catalogue — whatever shape fits.

     Obsidian features welcome:
       > [!note] callouts for asides
       ```dataview``` blocks for live cross-references
       ![[image.png]] embeds for diagrams / screenshots
     None of these need to round-trip anywhere. -->

> [!note]
> Obsidian callouts work here; they do not survive promotion to a wiki
> page, which is fine because this template never promotes.

## See also

<!-- Other meta notes, the relevant source files in tools/, upstream
     references. -->

- [[some-other-meta-note]]
- `tools/publish.py`
-

## Changelog

<!-- Optional but recommended for notes that document a decision or a
     subsystem: when the documented thing changes, append a dated entry
     here rather than silently editing the body. Repo readers can then
     diff intent against current state. -->

- YYYY-MM-DD — initial note.
