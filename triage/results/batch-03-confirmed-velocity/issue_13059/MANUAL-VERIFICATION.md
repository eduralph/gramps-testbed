# 13059 — Windows validation (post-merge confirmation)

**Why this needs a Windows check:** the bug is REAL (the headless unit
test in `gramps/gui/widgets/test/selectionwidget_test.py` reproduces
and confirms the fix on Linux), and the original tracker report was on
Windows (5.1.6 / 5.2.2). Mihle's reproducer is GUI-only via the Photo
Tagging addon. The Windows check is the GUI confirmation that the
Linux-verified fix lands correctly under the AIO bundled GTK.

**This is NOT a Linux-can't-repro case.** The fix was verified
headlessly on Linux. The Windows step is post-merge confirmation,
mostly to give the Mantis ticket a "Fixed in version" anchored to a
specific AIO release.

**Run after [gramps#2334](https://github.com/gramps-project/gramps/pull/2334) merges and a GrampsAIO build picks it up.**

---

## Setup

1. Install the GrampsAIO Windows build that contains the merged
   gramps#2334 (it'll be the next AIO drop from
   `maintenance/gramps61`).
2. Load example.gramps (as for 11658).
3. Install the **Photo Tagging** addon. Restart Gramps.

## Repro mihle's exact sequence

4. Open a Media entry that has a photo of a person (Media tab → any
   image).
5. Use Photo Tagging to draw a region box on the photo and link it to
   a person — save.
6. Close and re-open the same media entry so the saved box is loaded
   and visible.
7. Hover the cursor over a box EDGE so the resize cursor appears.
8. Press-and-drag that edge a few pixels (resizing the box).
9. Release the mouse button.
10. Move the cursor to the MIDDLE of the same box (not on an edge).
11. Single CLICK (press-release, no drag).

## Outcomes

- ✅ **No error dialog, no traceback.** Box stays where it is.
  → fix is correct on Windows. Paste `mantis-comment.md`, set
  Fixed in version to the AIO release that carries the fix, close.
  The same comment closes 0012659 (the 2022 duplicate) — paste it
  there too.
- ❌ **`TypeError: set_coords() argument after * must be an iterable,
  not NoneType`** (in an error dialog or "Error Report" window) →
  fix did not land in this build, or regressed. Reopen with:
  - the actual GrampsAIO version (Help → About)
  - the traceback (Copy from the Error Report dialog)
  - confirmation of which gramps PR is shipping in that build
    (check the build's commit / git log against gramps#2334's merge SHA).
