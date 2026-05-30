---
title: "REPLACE ME — Gramps 6.0 Wiki Manual - <Topic> (e.g. Gramps 6.0 Wiki Manual - Importing a GEDCOM file)"
categories:
  - Documentation
managed: true
---

<!--
  USER GUIDE TEMPLATE — for end-user documentation: how-tos, feature
  walkthroughs, troubleshooting recipes aimed at people USING Gramps in the
  app. Lives under 03 - User guide/ by convention.

  How this template differs from its siblings:
    technical-documentation.md — contributor audience: architecture, internals.
    addon-development.md       — addon-author audience: registration, code.
    user-guide.md (this)       — end-user audience: action-oriented steps,
                                 screenshots over code, troubleshooting.

  All three are managed: true and flow to BOTH outputs: MediaWiki (via
  md2wiki.py / publish.py) AND the bound PDF manual (via md2pdf.py --tree).
  They differ only in the default section skeleton and the category set.

  IMPORTANT — cohabitation with wiki-scraped pages:
  The 03 - User guide/ folder also holds read-only MIRRORS of the live wiki
  manual, marked with:
      managed: false
      source: wiki-scrape
      wiki_revid: <NNNNNN>
      wiki_fetched_at: '<ISO timestamp>'
  Those pages are managed: false on purpose — the source-of-truth is the
  live wiki, not the repo. publish.py and md2pdf.py --tree both skip them.
  This template is for the OTHER case: a NEW user-guide page authored
  locally, where the repo IS the source-of-truth and `managed: true` will
  push it upstream. Do NOT mimic the scraped pages' front-matter (no
  `source:`, no `wiki_revid:`, no `wiki_fetched_at:` on authored pages).

  In Obsidian: Settings -> core "Templates" plugin -> template folder
  location = pages/02 - templates. Then "Insert template" into a new note
  in pages/03 - User guide/.

  Front-matter keys:
    title:      the wiki page title, NOT the filename. Convention on this
                tree is `Gramps 6.0 Wiki Manual - <Topic>`; follow it.
                Identity lives here, so the file can be renamed/moved
                without breaking the wiki mapping or the PDF anchor.
    categories: appended as [[Category:...]] at the foot of the wiki page.
                `Documentation` is the established single category for
                user-guide pages on this wiki (verified against every
                scraped page in this folder). Optionally extend with
                feature-area categories where they exist on the live wiki
                (e.g. `Reports`, `GEDCOM`); do NOT add a version-scoped
                category like `Gramps 6.0` — the wiki convention doesn't
                use one here.
    managed:    true -> publish.py + md2pdf.py --tree WILL include this
                page. false -> draft only (treated as preliminary-notes).
  Start the body at H2 (##); the title above is the implicit H1.
-->

## Overview

<!-- 2-3 sentences: what task does this page help the user accomplish, and
     what's the rough outcome? Link the broader area page if there is one. -->

## Prerequisites

<!-- What the user needs to have set up BEFORE starting. Keep short and
     concrete; a table reads well when there are several items. -->

| Requirement | Notes |
|-------------|-------|
| Gramps 6.0 installed | |
| ... | |

## Steps

<!-- Numbered steps from start to finish. Each step short and verb-led;
     menu paths in italics (*Edit → Preferences*) read well in both
     MediaWiki and PDF. Screenshots via wiki shim (see below) for the
     wiki; for PDF output the shim is dropped, so if a screenshot is
     load-bearing for print readers, also embed the source asset with
     ![[image.png]] referencing a vault media file. -->

1. Open *Edit → Preferences*.
2. ...
3. ...

<!--wiki:[[File:example-step.png|thumb|right|400px|Caption goes here.]]-->

## Common problems

<!-- Things that go wrong in practice and how to recover. One subheading
     per problem keeps each findable in both the wiki ToC and the PDF
     ToC (which goes H1 + H2 by default). -->

### Problem one

<!-- Symptom, cause, fix. -->

### Problem two

<!-- ... -->

## See also

<!-- Related user-guide pages, upstream references. wiki: links targeting
     other on-tree pages become internal anchors in the bound PDF; off-tree
     targets fall back to the live wiki URL. -->

- [Adjacent task](wiki:Gramps_6.0_Wiki_Manual_-_Some_Adjacent_Task)
- [Upstream wiki area](https://gramps-project.org/wiki/Manual)

<!--wiki:{{stub}}-->
