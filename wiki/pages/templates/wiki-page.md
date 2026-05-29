---
title: "REPLACE ME — exact wiki page title (e.g. Gramps 6.0 Wiki Manual - Foo)"
categories:
  - Addons
  - Gramps 6.0
managed: true
---

<!--
  WIKI PAGE TEMPLATE — copy into pages/content/ to start a new page.
  Front-matter MUST be the very first thing in the file (Obsidian and the
  converter both require it). All guidance below is in HTML comments: Obsidian
  and GitHub hide them, and the converter strips them, so they never reach the
  wiki. Only wiki shims (see below) survive.

  In Obsidian: Settings -> core "Templates" plugin -> template folder location
  = pages/templates. Then "Insert template" into a new note in pages/content.

  Front-matter keys:
    title:      the wiki page title, NOT the filename. Identity lives here, so
                you can rename/move the file freely without breaking the mapping.
    categories: appended as [[Category:...]] at the foot of the page.
    managed:    true -> publish.py WILL push this page. false -> draft only.
  Start the body at H2 (##); the title above is the implicit H1.
-->

## Overview

Write in normal Markdown. **Bold**, *italic*, `inline code`, lists, and tables
all convert to wikitext.

See [[6.0_Addons]] for the current list, or [[Addons_development|the porting
notes]] for cross-version concerns.

<!--
  INTERNAL LINKS: use Obsidian-native [[wikilinks]] above — same syntax as
  MediaWiki, so they round-trip for free. Alternative if you want the link
  clickable when browsing the repo on GitHub: [the addon list](wiki:6.0_Addons),
  which the converter also turns into [[6.0_Addons|the addon list]]. Native
  [[...]] shows as literal brackets on GitHub; choose per how much GitHub
  rendering matters for this page.
-->

## Using a wiki template

<!--wiki:{{man index|6.0}}-->

<!--
  WIKI TEMPLATES / TRANSCLUSIONS have no Markdown equivalent — author them in a
  wiki shim comment (hidden in Obsidian + GitHub, emitted raw to the wiki).
  Works as a block (own line, above) or inline within a sentence.
-->

Explanatory prose for this section.

## Code

```python
register(
    GRAMPLET,
    id="Example",
    name=_("Example"),
    version="1.0.0",
    gramps_target_version="6.0",
    fname="example.py",
    gramplet="Example",
)
```

## Tables

| File | Purpose |
|------|---------|
| `<Addon>.gpr.py` | Registration |
| `<Addon>.py` | Implementation |

<!--
  AVOID in published pages: Obsidian embeds (image transclusions), callouts
  (> [!note]), Dataview — Obsidian-only, won't convert. For a wiki image use a
  shim with File: syntax inside a wiki comment instead.
-->

<!--wiki:{{stub}}-->
