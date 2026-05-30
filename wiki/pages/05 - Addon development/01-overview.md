---
title: "Gramps 6.0 Wiki Manual - Addon Development"
categories: ["Addons", "Developers", "Gramps 6.0"]
managed: true
---

<!--wiki:{{man index|6.0}}-->

## Overview

A Gramps **addon** extends the application without modifying core. Addons are discovered from the plugin directory; see [the addon list](wiki:6.0_Addons) for what ships today.

**New with 6.1**: plugin discovery follows symlinks (with realpath-based dedup to prevent infinite recursion on symlink loops), so a symlinked addon folder loads correctly.

## Anatomy of an addon

Every addon ships at minimum a registration file and an implementation module.

| File | Purpose |
|------|---------|
| `<Addon>.gpr.py` | Registration: name, version, Gramps target, entry point |
| `<Addon>.py` | The plugin implementation |
| `po/` | Translation catalogs (optional) |

The registration file declares the Gramps version it targets. An addon on `maintenance/gramps60` expects the Gramps 6.0 API; see [the porting notes](wiki:Addons_development) for cross-version concerns.

## Minimal registration

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

<!--wiki:{{stub}}-->
