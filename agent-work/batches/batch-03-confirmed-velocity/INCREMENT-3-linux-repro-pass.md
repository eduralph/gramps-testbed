# Claude Code increment — batch-03 Linux-repro pass (13059, 14143, 11658, 12453) + 12050 artifact gap

> Append to / read alongside CLAUDE_CODE_BRIEF.md. Standing rules still apply:
> repro-or-close BEFORE fixing; check merged AND closed/rejected PRs; fix only
> what the verdict scopes; one logical change per issue; STOP after writing
> results (no push/PR/ready-mark — Eduard's review gate).
>
> **Context for this increment:** the Windows GUI-automation effort is PAUSED
> (GTK3-on-Windows exposes no UIA tree; name-based desktop drivers can't drive
> it — spike verdict is RED, see work/workstream-b-uia-spike-findings). So these
> items are worked **Linux-first**: recreate on the Linux dogtail/AT-SPI e2e
> harness that already works, fix or close there. Do NOT attempt Windows
> verification for any of these. A bug that only reproduces on Windows becomes a
> documented "Linux-can't-repro, Windows-only" note for later manual handling —
> not a blocker.

## Per-item branch targets (NOT uniform — resolve addon-vs-core by reproducing)
| Issue | Likely repo | Branch | Note |
|---|---|---|---|
| 13059 | gramps CORE | maintenance/gramps61 | traceback in core selectionwidget.py; addon only hosts it |
| 14143 | addons-source | maintenance/gramps60 | ChatWithTree styling |
| 11658 | addons-source | maintenance/gramps60 | GraphView (if it even reproduces) |
| 12453 | addons-source / external | maintenance/gramps60 | PlaceCoordinatesGramplet (likely external) |

Mantis rule: every one of these has a tracker entry, so EACH produces a
`results/issue_<id>/mantis-comment.md` regardless of outcome (fix / can't-repro /
external / wontfix). That includes the closes.

## 13059 — Photo Tagging click-after-resize crash — REAL FIX CANDIDATE (the substantive one)
Verdict in issue_13059.md. Traceback is in gramps CORE
`gramps/gui/widgets/selectionwidget.py:742` — `self.current.set_coords(*self.selection)`
called with `self.selection is None` on the click-after-resize path.
1. **Resolve addon-vs-core by reproducing** (mandatory): the Photo Tagging addon
   hosts the SelectionWidget but the defect is in core. Confirm by reproducing —
   if the crash is in selectionwidget.py regardless, the fix targets `../gramps`
   (maintenance/gramps61), NOT addons-source.
2. **Repro on Linux** with mihle's exact sequence (issue_13059.md notes): existing
   box on a photo linked to a person → drag a box EDGE to resize → release →
   single CLICK (not drag) inside the middle of that same box → TypeError. Needs
   Photo Tagging addon + a photo with a person-linked box on example.gramps.
   Reported on 5.1.6/5.2.2 — confirm it still fires on gramps61.
3. **Fix:** guard the call — if `self.selection is None`, skip/return rather than
   splatting None into set_coords. Read the handler to determine correct
   no-selection behavior (the plain click likely should just select the box).
   Conservative guard like the 13966/13326 teardown family; do not restructure
   the widget.
4. **Test:** try the headless unit path FIRST (cheaper, upstreamable) — if the
   `set_coords`/release path can be exercised with `selection=None` in a
   `unittest.TestCase` in gramps' gui test layout asserting no TypeError, do that.
   Fall back to a `tests/interface/` dogtail test reproducing the drag-then-click
   only if headless can't reach the path.
5. Duplicate 0012659 (2022) closes with it — reference in the comment/PR.

## 14143 — ChatWithTree dark-mode contrast — VISUAL FIX (Eduard verifies)
Verdict in issue_14143.md. Current (6.0.7), will reproduce on Linux under a dark
GTK theme.
1. **Repro on Linux:** set a dark GTK theme, open Chat With Tree, confirm text is
   low-contrast/unreadable.
2. **Fix:** make text styling theme-aware — pull fg/bg from the GTK theme instead
   of hardcoded colours, OR `@media (prefers-color-scheme: dark)` if it's an
   embedded HTML/WebKit view. Inspect how the addon currently sets colours; pick
   the minimal correct fix.
3. **Test caveat:** contrast is a VISUAL property — do NOT force a brittle
   automated contrast test. Acceptable to ship a pure styling fix with a light
   assertion that the addon no longer hardcodes a foreground colour, OR no test
   with a note. **Eduard verifies the actual rendering manually** — flag clearly
   in the SUMMARY that this needs human visual sign-off (the one item here that
   is not fully self-verifying).

## 11658 — GraphView no images — REPRO-OR-CLOSE (expect close)
Verdict-scaffold in issue_11658.md (NO-NOTES, 2020, GrampsAIO64 5.1.2 Windows).
1. **Repro on Linux:** GraphView addon + a person with a photo on example.gramps;
   check whether the image renders in graph view. The original report is a
   Windows-AIO packaging context (libgoocanvas dll) — a strong hint this is
   environmental, not an addon-code bug.
2. If it reproduces on Linux current → real addon bug, diagnose/fix.
3. If it does NOT reproduce on Linux (likely) → close as can't-reproduce /
   likely-environmental (stale 5.1.2 Windows packaging). Write the
   mantis-comment.md documenting the Linux repro attempt and outcome.

## 12453 — PlaceCoordinatesGramplet TLS cert — REPRO-OR-CLOSE (expect external)
Empty tracker record (no notes/steps), 2021, 5.1.4. Symptom
`g-io-error-quark: Unacceptable TLS certificate`.
1. **Repro on Linux:** almost certainly an environment/system-cert/GnuTLS issue,
   NOT addon code — but confirm by attempting a place search via the gramplet on
   gramps60.
2. Expected outcome: cannot reproduce / external (system TLS trust store), close
   with mantis-comment.md explaining it's environmental, not an addon defect.
   NOTE: this is explicitly NOT part of any 13065 cluster (different root cause);
   do not conflate.

## 12050 — mantis-comment gap (admin, not a repro item)
12050 was already triaged to "close as by-design" (SQLite import is slow but
working-as-intended; the only 'fix' would be an abort-button feature — deferred).
Its results currently point at MANTIS_ACTIONS.md instead of having its own
comment. Per the Mantis rule (every tracker entry gets a generated comment),
**generate `results/issue_12050/mantis-comment.md`** — a ready-to-paste
by-design/wontfix close citing the thread's conclusion (blob storage design
tradeoff, import works but is ~100x slower than XML; abort-button is a separate
feature request). No code, no repro — just the artifact.

## Expected net result
- 13059: a core fix (gramps61) + test, OR a documented Linux-can't-repro note.
- 14143: a styling fix (gramps60) flagged for Eduard's visual sign-off.
- 11658: almost certainly a can't-repro-on-Linux close + comment.
- 12453: almost certainly an external/environmental close + comment.
- 12050: the missing mantis-comment.md generated.
Each item that touches code STOPs for review; closes produce comment artifacts.
```
