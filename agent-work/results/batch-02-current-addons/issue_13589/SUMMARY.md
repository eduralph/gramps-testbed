# Issue 13589 — Family Sheet PDF trailing blank page

## Outcome
**Cannot reproduce on Ubuntu 24.04** (testbed's docker image). No code
change made. The verdict explicitly called this out as a valid
terminal outcome:

> "could not reproduce" is a VALID terminal outcome … the most likely
> honest outcomes here are "could not reproduce" or "renderer/upstream,
> not the addon".

## Environment tested
- Host: `gramps-testbed:ubuntu-6.1.0` Docker image (`FROM ubuntu:24.04`).
- Gramps: `maintenance/gramps61` HEAD at the time of test
  (`gramps -C TestTree -i example.gramps`).
- Family Sheet addon: addons-source `maintenance/gramps61` HEAD,
  installed into `USER_PLUGINS`.
- Rendering stack:
  - `libpango-1.0-0:amd64    1.52.1+ds-1build1`
  - `libpoppler134:amd64     24.02.0-1ubuntu9.8`
  - `libcairo2`, `libcairo-gobject2  1.18.0-3build1`
- PDF page counts measured with `pdfinfo`; per-page content sampled
  with `pdftotext -f N -l N`.

## Reporter's environment
- favdb (reporter): Linux Mint 21.3 / Ubuntu 22.04 base + Gramps
  6.0.5 + PDF.
- snoiraud (confirmer): Ubuntu 22.04.5 + PDF, running from git, no
  snap/flatpak/deb.
- codefarmer: could not reproduce on Windows 10 (WSL) or Windows 11.

The Ubuntu 22.04 ⇄ 24.04 jump replaces Pango/Cairo with newer
versions, which is the most plausible explanation: a trailing blank
page that the 22.04 stack appended at a content/page boundary no
longer appears on 24.04.

## What I ran

Generated the Family Sheet report as PDF for five
person/recurse combinations against `example.gramps`, then counted
pages and inspected the last page's non-whitespace character count:

| pid    | recurse        | pages | last-page non-ws chars |
|--------|----------------|-------|------------------------|
| I00552 | NONE (0)       |     1 | 472                    |
| I00552 | 1              |     1 | 472                    |
| I00552 | ALL (2)        |    52 | 337                    |
| I01776 | NONE (0)       |     1 | 231                    |
| I01776 | ALL (2)        |     1 | 231                    |

In every case the last page contained real content (not whitespace).
A trailing blank page would have shown zero non-whitespace chars.

`pdftotext -f 52 -l 52 fs.pdf` on the 52-page recurse=ALL run prints
"Moreno, Solon" / "Perkins, Lydia" sheet content — a normal Family
Sheet, not an empty page.

## Doc-model side of the diagnostic
The verdict's "model-vs-rendered" split came out cleanly even before
running the report:

> If the model has a trailing page-break / trailing empty page →
> addon bug. If the model looks correct but the rendered PDF has an
> extra page → renderer bug.

`FamilySheet.py` calls `self.doc.page_break()` at exactly one site,
[FamilySheet.py:306](../../../../addons-source/FamilySheet/FamilySheet.py#L306):

```python
for (child, child_rank, child_at, child_key) in more_sheets:
    self.doc.page_break()
    self.__process_person(child, child_rank, child_at, child_key)
```

The break fires *before* each child's sheet, never *after*. The last
child's sheet ends with `self.doc.end_table()` and the report
returns. So the document model emitted by the addon has no trailing
page-break and no trailing empty content. **If a Linux+PDF user sees
a trailing blank page, the addon model is not the source** — by the
verdict's own diagnostic, the bug is downstream (cairo PDF docgen, or
upstream cairo/Pango behavior on certain content-height / page-
boundary conditions).

## What this means for the tracker

- Add a "could not reproduce on Ubuntu 24.04" data point.
- Note that the addon's doc model is verified clean (no trailing
  page-break in the source).
- Suggest the next move is **environmental**: a reporter still on
  Ubuntu 22.04 needs to retry on a 24.04 system (LiveCD or fresh
  install) to confirm whether updating the rendering stack resolves
  it. If it does, the bug is closed as fixed-upstream-in-cairo/Pango.

## Repo and branch
No code change. No PR. Result artifact only.
