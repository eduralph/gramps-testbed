---
title: "REPLACE ME — exact wiki page title (e.g. Gramps 6.0 Wiki Manual - Database Architecture)"
categories:
  - Developers
  - Gramps 6.0
managed: true
---

<!--
  TECHNICAL DOCUMENTATION TEMPLATE — for contributor-facing reference that
  ships to the wiki: architecture, internals, data models, interface
  contracts, conventions. Lives under 04 - Technical Documentation/ by
  convention.

  How this template differs from its siblings:
    user-guide.md              — end-user audience: in-app workflows.
    addon-development.md       — addon-author audience: registration, code.
    technical-documentation.md (this) — contributor / maintainer audience;
                                        defaults steer toward architecture
                                        and reference structure.

  All three are managed: true and flow to BOTH outputs: MediaWiki (via
  md2wiki.py / publish.py) AND the bound PDF manual (via md2pdf.py --tree).
  They differ only in the default section skeleton and the category set.

  In Obsidian: Settings -> core "Templates" plugin -> template folder
  location = pages/02 - templates. Then "Insert template" into a new note
  in pages/04 - Technical Documentation/.

  Front-matter keys (same as wiki-page.md):
    title:      the wiki page title, NOT the filename. Identity lives here,
                so the file can be renamed/moved without breaking the
                wiki mapping or the cross-link slug in tree-mode PDFs.
    categories: appended as [[Category:...]] at the foot of the wiki page.
                "Developers" + the version-scoped category is the usual
                pairing; add subsystem categories (e.g. "Database", "GUI")
                where they exist in the live wiki.
    managed:    true -> publish.py WILL push this page. false -> draft only.
  Start the body at H2 (##); the title above is the implicit H1.
-->

## Overview

<!-- 2–4 sentences: what subsystem / interface / convention does this page
     document, and what does a contributor walk away knowing? Link the
     overview page that this one sits beneath, if any. -->

See [the parent area overview](wiki:Gramps_6.0_Wiki_Manual_-_Developer_Reference)
for where this fits.

## Architecture

<!-- The structural picture. A short prose paragraph plus a table of the
     components is usually enough at this level — deep dives belong on
     their own pages, linked from "See also". -->

| Component | Role | Source |
|-----------|------|--------|
| `Foo` | what it does | `gramps/gen/foo.py` |
| `Bar` | what it does | `gramps/gen/bar.py` |

## Data flow

<!-- How a request / event / change moves through the components above.
     Numbered steps work well; a sequence diagram is even better if you
     have one (embed as an image via wiki shim, see below). -->

1. Caller invokes `Foo.frob(x)`.
2. …
3. Result returned as a `Bar` instance.

## Interface contract

<!-- The public surface a contributor needs to honour: function signatures,
     invariants, error conditions, threading rules. Code blocks with
     concrete signatures are more useful here than prose. -->

```python
def frob(x: FooHandle) -> Bar | None:
    """Return the Bar for x, or None if x is unknown.

    Raises HandleError if x is malformed.
    """
```

## Conventions

<!-- Per-subsystem rules that aren't enforced by the type system: naming,
     ordering, what NOT to do, common gotchas. Mirrors what an AGENTS.md
     would say at file granularity. -->

- Always do X before Y.
- Never call `Foo._internal()` from outside the module.

## Diagrams and images

<!--wiki:[[File:example-diagram.png|thumb|right|400px|Caption goes here.]]-->

<!--
  Wiki image syntax has no Markdown equivalent — use a wiki shim. Upload
  the asset to the live wiki first (Special:Upload) and reference it by
  its File: name. For PDF rendering via md2pdf.py the shim is dropped, so
  if the diagram is load-bearing for print readers, ALSO embed the source
  asset with ![[diagram.png]] in a sibling repo-side meta note.
-->

## See also

<!-- Related contributor docs, source files, upstream references. Prefer
     wiki: links to other pages in this tree (they cross-link in PDF mode
     too), external URLs to upstream gramps / gramps-project.org pages
     that aren't part of this tree. -->

- [Addons development](wiki:Addons_development) — cross-version notes.
- `gramps/gen/...` — source root for this subsystem.
- [Upstream wiki page](https://gramps-project.org/wiki/Some_Page).

<!--wiki:{{stub}}-->
