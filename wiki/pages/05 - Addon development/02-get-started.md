---
title: "Gramps 6.0 Wiki Manual - Addon Development - Getting Started"
categories:
  - Addons
  - Developers
  - Gramps 6.0
managed: true
---

<!--wiki:{{man index|6.0}}-->

## Overview

This page walks a first-time addon author from "Gramps is installed" to "my addon shows up in the menu". For the conceptual picture and the file roles, see [the addon development overview](wiki:Gramps_6.0_Wiki_Manual_-_Addon_Development); for the catalogue of what already exists, see [the addon list](wiki:6.0_Addons).

## Prerequisites

| Requirement | Why |
|-------------|-----|
| Gramps 6.0 installed and runnable | The target you're developing against |
| Python 3.10+ | Matches Gramps 6.0's minimum |
| A text editor or IDE | Any will do; Gramps doesn't impose one |
| Familiarity with Python imports and packages | Addons are Python modules |

You do **not** need to build Gramps from source for addon work. Addons load from the user plugin directory and are picked up at next start.

## Where addons live

Each addon is a folder under Gramps' user plugin directory, one folder per addon. The exact path is platform-specific; see [the Addons page](wiki:6.0_Addons) for the canonical locations. The folder name is the addon name and must match the `id` used in registration.

On Gramps 6.0, plugin discovery does **not** follow symlinks — the addon must be physically present under the plugin path, so the development loop is copying (or `rsync`ing) from your working tree on save.

**Changed in 6.1**: plugin discovery follows symlinks (with realpath-based dedup against symlink loops), so you can `ln -s <working-tree>/<Addon>` into the user plugin directory and edit in place. Windows users: the 6.1 symlink test is skipped on Windows because the platform's symlink behavior is inconsistent without elevated privileges; the `rsync`/copy loop remains the safe default there. (gramps commit `9443dcbb30` on `maintenance/gramps61`.)

## Your first addon: a minimal Gramplet

A *Gramplet* is the lightest-weight addon kind — a sidebar widget. Two files are enough.

### 1. Create the addon folder

Make a folder named `HelloGramplet` under the user plugin directory.

### 2. Add the registration file

Save this as `HelloGramplet/HelloGramplet.gpr.py`:

```python
register(
    GRAMPLET,
    id="HelloGramplet",
    name=_("Hello Gramplet"),
    description=_("A minimal example Gramplet"),
    version="1.0.0",
    gramps_target_version="6.0",
    status=STABLE,
    fname="hellogramplet.py",
    gramplet="HelloGramplet",
    gramplet_title=_("Hello"),
)
```

The `id` is the addon's stable identifier. `fname` is the implementation module. `gramplet` is the class inside it that Gramps will instantiate.

### 3. Add the implementation

Save this as `HelloGramplet/hellogramplet.py`:

```python
from gramps.gen.plug import Gramplet


class HelloGramplet(Gramplet):
    def init(self):
        self.set_text(_("Hello from your first Gramplet!"))
```

`init()` is the construction hook — Gramps calls it once when the Gramplet is first shown.

### 4. Restart Gramps

Plugin discovery happens at startup. After the restart, the new Gramplet appears under *View → Sidebar* (or the Dashboard, depending on view).

## Reload / test cycle

There is no hot-reload for addons. The development loop is:

1. Edit the source.
2. Sync the change into the plugin directory (or work directly there).
3. Restart Gramps.
4. Observe.

For faster iteration on non-GUI logic, write a `unittest`-based test alongside the addon and run it without launching Gramps — see [Addon Testing](wiki:Gramps_6.0_Wiki_Manual_-_Addon_Testing) for the conventions.

## Translation

Wrap every user-visible string in `_()` so it can be translated:

```python
self.set_text(_("Hello from your first Gramplet!"))
```

`_` is injected into the addon's namespace by Gramps' plugin loader; you do not need to import it. Translation catalogues live in a per-addon `po/` directory — optional for a first experiment, required for an addon you intend to share.

## Next steps

- [Addon Development overview](wiki:Gramps_6.0_Wiki_Manual_-_Addon_Development) — file roles, registration fields, addon kinds beyond Gramplets.
- [Addon Testing](wiki:Gramps_6.0_Wiki_Manual_-_Addon_Testing) — unit-test conventions and the `tests/` package layout.
- [Addons development](wiki:Addons_development) — cross-version porting notes and the wider development reference.
- [6.0 Addons](wiki:6.0_Addons) — what already exists; read a similar addon's source as your second tutorial.

<!--wiki:{{stub}}-->
