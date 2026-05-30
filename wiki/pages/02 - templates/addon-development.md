---
title: "REPLACE ME — exact wiki page title (e.g. Gramps 6.0 Wiki Manual - Addon Development - Quick Views)"
categories:
  - Addons
  - Developers
  - Gramps 6.0
managed: true
---

<!--
  ADDON DEVELOPMENT TEMPLATE — for pages aimed at addon authors writing or
  maintaining a specific addon kind, feature, or pattern. Lives under
  05 - Addon development/ by convention.

  How this template differs from its siblings:
    technical-documentation.md — Gramps INTERNALS audience: architecture
                                 of the core, what contributors modify.
    user-guide.md              — end-user audience: in-app workflows.
    addon-development.md (this) — addon AUTHOR audience: registration
                                 fields, the .gpr.py + impl pair, testing.

  All three are managed: true and flow to BOTH outputs: MediaWiki (via
  md2wiki.py / publish.py) AND the bound PDF manual (via md2pdf.py --tree).
  They differ only in the default section skeleton and the category set.

  Note: this template's filename matches the existing content page
  pages/05 - Addon development/addon-development.md by intent (folder-name
  parallelism). Obsidian's template picker disambiguates by folder.

  In Obsidian: Settings -> core "Templates" plugin -> template folder
  location = pages/02 - templates. Then "Insert template" into a new note
  in pages/05 - Addon development/.

  Front-matter keys (same as the other publishable templates):
    title:      the wiki page title, NOT the filename.
    categories: "Addons" + "Developers" + version-scoped category is the
                established pairing on this tree's existing addon pages.
    managed:    true -> publish.py + md2pdf.py --tree WILL include this
                page. false -> draft only.
  Start the body at H2 (##); the title above is the implicit H1.
-->

## Overview

<!-- 2-3 sentences: what addon kind / feature does this page document, and
     what does an author come away knowing? Link the addon development
     overview page for context. -->

See [the addon development overview](wiki:Gramps_6.0_Wiki_Manual_-_Addon_Development)
for where this fits.

## Prerequisites

| Requirement | Why |
|-------------|-----|
| Gramps 6.0 installed and runnable | The target you're developing against |
| Python 3.10+ | Matches Gramps 6.0's minimum |
| Familiarity with addon registration | See [Getting Started](wiki:Gramps_6.0_Wiki_Manual_-_Addon_Development_-_Getting_Started) |

## Worked example

<!-- The .gpr.py + implementation pair an author can copy and adapt. The
     two-file pair is the central artifact for any addon page; even a
     minimal example is more useful than prose alone. -->

### Registration

```python
register(
    KIND,                       # e.g. GRAMPLET, VIEW, REPORT, GENERAL
    id="ExampleAddon",
    name=_("Example Addon"),
    description=_("..."),
    version="1.0.0",
    gramps_target_version="6.0",
    status=STABLE,
    fname="exampleaddon.py",
    # ... kind-specific fields ...
)
```

### Implementation

```python
from gramps.gen.plug import ...


class ExampleAddon(...):
    def init(self):
        ...
```

## Registration fields

<!-- The .gpr.py fields used above plus any kind-specific ones, with
     their meaning. Keep the table grounded in the worked example. -->

| Field | Meaning |
|-------|---------|
| `id` | Stable identifier; MUST match the addon's folder name |
| `fname` | Implementation module filename |
| `version` | Addon version (semver-ish) |
| `gramps_target_version` | Major.minor Gramps version the addon targets |
| `status` | `STABLE` / `BETA` / `EXPERIMENTAL` / `UNSTABLE` |

## Implementation notes

<!-- The non-obvious bits of writing this addon kind: lifecycle hooks,
     threading rules, data-access conventions, common gotchas. One bullet
     per point reads better than long prose. -->

- ...
- ...

## Testing

<!-- How to verify the addon works. Mention both the manual reload/restart
     loop (covered in Getting Started) and `unittest`-based tests for
     non-GUI logic — the conventions are in the Addon Testing page. -->

See [Addon Testing](wiki:Gramps_6.0_Wiki_Manual_-_Addon_Testing) for the
unit-test conventions and the `tests/` package layout.

## See also

<!-- wiki: links to other on-tree pages become internal anchors in the
     bound PDF (cross-linked manual); off-tree targets fall back to the
     live wiki URL. -->

- [Addon Development overview](wiki:Gramps_6.0_Wiki_Manual_-_Addon_Development)
- [Getting Started](wiki:Gramps_6.0_Wiki_Manual_-_Addon_Development_-_Getting_Started)
- [Addons development](wiki:Addons_development) — cross-version porting notes.

<!--wiki:{{stub}}-->
