# Mantis 13589 — draft note (Eduard to paste)

(Bare bug numbers per the no-`#`-prefix convention.)

---

Adding another no-repro data point and a doc-model finding.

**Cannot reproduce on Ubuntu 24.04** with the current
`maintenance/gramps61` Family Sheet addon and `example.gramps`.
Tested five PID + recurse combinations as PDF (via the CLI report
runner). In every case the PDF's last page contained real Family
Sheet content; no trailing blank page appeared:

| pid    | recurse  | pages | last-page non-ws chars |
|--------|----------|-------|------------------------|
| I00552 | NONE     |     1 | 472                    |
| I00552 | 1        |     1 | 472                    |
| I00552 | ALL      |    52 | 337                    |
| I01776 | NONE     |     1 | 231                    |
| I01776 | ALL      |     1 | 231                    |

Rendering stack on the host that did not reproduce:
`libpango-1.0-0 1.52.1`, `libcairo2 1.18.0`, `libpoppler134 24.02`.

favdb (reporter) and snoiraud (confirmer) were both on Ubuntu 22.04.
codefarmer could not reproduce on Windows. The 22.04 ⇄ 24.04 jump is
the most plausible discriminator: a trailing blank page emitted at a
content/page boundary on the 22.04 cairo/Pango stack apparently no
longer fires on 24.04. That makes this a candidate "fixed upstream
in cairo/Pango" rather than a Gramps defect.

**Doc-model check (the verdict's diagnostic, run by reading source):**
`FamilySheet.py:306` calls `self.doc.page_break()` at exactly one
site — *before* each child sheet inside the descendant loop, never
*after* the last sheet. The report ends with `end_table()` and
returns. So the document model the addon emits has no trailing
page-break and no trailing empty content. By the model-vs-rendered
split, **if a Linux+PDF user still sees the trailing blank page, the
defect is downstream of the addon** — cairo PDF docgen in gramps
core, or upstream cairo/Pango behavior on certain content-height /
page-boundary combinations.

Suggested next step: ask the original reporter (still on Ubuntu
22.04?) to retest on a 24.04 system or LiveCD. If it goes away with
the newer cairo/Pango, this resolves as fixed-upstream and the
ticket can be closed.
