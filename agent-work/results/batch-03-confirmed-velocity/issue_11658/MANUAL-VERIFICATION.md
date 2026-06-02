# 11658 — Windows validation (REQUIRED before close)

**Why this needs Windows verification:** the original 2020 report was
Windows AIO 5.1.2 (`libgoocanvas` DLL in the program folder — a strong
packaging hint). Linux can't reproduce by construction (current Linux
distros ship complete GdkPixbuf loader sets). But code-level inspection
on `upstream/maintenance/gramps60` flagged a residual concern in
[`GraphView/graphview.py:2258`](../../../../../../addons-source/GraphView/graphview.py#L2258)
— `GdkPixbuf.Pixbuf.new_from_file()` is called without an exception
guard in the SVG `<image>` element path. If GdkPixbuf can't load an
image (incomplete format loaders, broken DLL), the SVG parse aborts
silently. Whether that's still possible on the **current** GrampsAIO
build is what your manual check answers.

**Per the testbed convention** (memory:
`feedback_windows_only_eduard_verifies`): Linux can't repro + Windows-only
signal → Eduard verifies; the mantis-comment says "needs Windows
confirmation", not a clean cannot-reproduce close, until you've run
this.

---

## Setup

1. Install current GrampsAIO Windows build (latest 6.x).
2. Family Trees → Manage Family Trees → New → name it `TestTree` →
   Load → Import the bundled `example.gramps` (it lives at
   `share/gramps/example/gramps/example.gramps` inside the AIO
   install directory).
3. Install the **Graph View** addon: Addons (or Addon Manager) → search
   "Graph View" → install → restart Gramps.

## Repro

4. Pick a person who has a photo in `example.gramps`. Several do —
   e.g. Garner von Zieliński or Hanson; you can spot them in the
   People view by the thumbnail in the row.
5. Switch to the **Charts** category → **Graph View** subview.
6. Look at the person nodes in the graph: **does the photo render as
   a small thumbnail on/next to the node?**

## Outcomes

- ✅ **Photos render** → 11658 is environmental to 5.1.2, resolved by
  6.x AIO packaging. Paste `mantis-comment.md` (this folder), close as
  cannot-reproduce-on-current.
- ❌ **Photos do NOT render** → 11658 is still live on current Windows.
  Capture evidence and reopen:
  - Open the GrampsAIO console (launch `GrampsAIO-*.exe` from cmd.exe
    so stdout/stderr are visible, or watch
    `%APPDATA%\gramps\error.log`).
  - Look for a traceback originating in
    `gramps/plugins/addons/GraphView/graphview.py` around line
    **2258** (`start_image`, `GdkPixbuf.Pixbuf.new_from_file()`).
  - If found → the SVG `<image>` element path is the culprit; the
    targeted hardening is to wrap that call in try/except and
    skip-on-load-failure rather than letting the SVG parse abort.
    Reopen 11658 with the traceback and the GrampsAIO version,
    and update the SUMMARY.
  - If NOT found → something else is failing silently. Capture the
    AT-SPI tree of GraphView startup if possible and reopen 11658
    with that.
