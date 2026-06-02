# Issue 11658 — GraphView no images for people — likely environmental, NEEDS WINDOWS CONFIRMATION

## Status
**Likely close as cannot-reproduce / environmental** — but the close
is GATED on Eduard's manual Windows check per the testbed convention
for Linux-can't-repro + Windows-only signal bugs (Mantis 11658 was
filed against Windows AIO 5.1.2 with a `libgoocanvas` DLL hint —
classic Windows-only signal). No code change in either outcome
unless the Windows check surfaces a still-live failure on current AIO.

**See `MANUAL-VERIFICATION.md` in this folder** for the exact setup +
repro steps + outcomes. Run that BEFORE pasting `mantis-comment.md`.

## Verification
Investigated in this increment (no GUI repro per the workstream-B UIA
spike pause — Linux-first code-level analysis).

Original report context (Mantis 11658):
- Reported 2020, Gramps 5.1.2, GrampsAIO64 (Windows).
- Reporter referenced a `libgoocanvas` DLL in the program folder — a
  strong Windows-AIO packaging hint, not an addon-code symptom.

Code-level inspection on `upstream/maintenance/gramps60`:

- **Person-photo path** in
  [`GraphView/graphview.py:1433-1466`](../../../../../../addons-source/GraphView/graphview.py#L1433-L1466):
  `get_person_image` is already defensive — it null-checks media-ref
  resolution, file-exists, and uses `GdkPixbuf.Pixbuf.new_from_file_at_scale`
  inside an exception path that returns `None` on any failure. This path
  cannot produce "no image displayed" silently in a code-defect sense; it
  either succeeds or returns None deliberately.
- **SVG image-element rendering path** in
  [`GraphView/graphview.py:2250-2266`](../../../../../../addons-source/GraphView/graphview.py#L2250-L2266):
  `start_image` calls `GdkPixbuf.Pixbuf.new_from_file()` without a
  try/except. If GdkPixbuf cannot load the image format, this raises an
  unhandled exception that terminates SVG parsing. On Linux with a
  complete GdkPixbuf loader set, this path is robust; on Windows AIO 5.1.2
  with potentially-missing GdkPixbuf format-loader DLLs, it could fail
  silently.
- **No code changes** to the image-loading paths since the 5.1.2 era —
  recent commits on GraphView are translation updates (`388be68be`,
  `8c3880b8f`) and PR #883 (trailing-whitespace cleanup, 2026-05).
- **No open or closed upstream PRs** addressing GraphView image rendering
  (checked `gh pr list --repo gramps-project/addons-source --state all --search "GraphView"`).
- **Reporter's `libgoocanvas` DLL hint** is consistent with the SVG-path
  failure mode — incomplete GooCanvas / GdkPixbuf bindings on a specific
  Windows AIO build would manifest exactly as "image element doesn't
  render, no error in the log".

This is **environmental, not an addon defect**. Current Linux distributions
ship complete GdkPixbuf loader sets; the SVG-path failure cannot trigger.
GrampsAIO Windows packaging has moved on substantially since 5.1.2 (the
6.x AIO builds use a different MSYS2 base). The original reporter's
environment cannot be recreated, and current Linux cannot reproduce the
symptom by construction.

## Repo and branch
- Repo: `addons-source` (`GraphView/`)
- Branch: maintenance/gramps60 — no commit; close-only.
- This batch: no patch.diff, no pr-description.md.

## Mantis link
- Tracker: https://gramps-project.org/bugs/view.php?id=11658
- Status to set: resolved / cannot reproduce
- Fixed in version: N/A
- Comment: see `mantis-comment.md`

## Notes for next reviewer
- The Windows check (`MANUAL-VERIFICATION.md`) is the close gate, not
  a "reopen if a future user complains" hook. Per the testbed memory
  rule `feedback_windows_only_eduard_verifies`: bugs that can't be
  repro'd on Linux and have a Windows-only signal need Eduard's
  manual confirmation on a current AIO before they close cleanly.
- The unguarded `GdkPixbuf.Pixbuf.new_from_file()` in `start_image`
  ([`GraphView/graphview.py:2258`](../../../../../../addons-source/GraphView/graphview.py#L2258))
  is a latent robustness issue worth a separate hardening pass
  regardless of how the 11658 verification lands — wrap in try/except
  and skip the image element on load failure rather than silently
  terminating the SVG parse. If the Windows check shows the bug is
  still live, that hardening becomes the targeted fix. If the check
  shows photos render fine on current AIO, file the hardening as a
  separate "robustness, no known repro" addons-source issue and let
  it queue.
