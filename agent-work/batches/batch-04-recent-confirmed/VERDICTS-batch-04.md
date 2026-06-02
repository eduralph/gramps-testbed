# batch-04-recent-confirmed — VERDICTS (apply with apply_verdicts.py)
#
# Run from gramps-testbed/agent-work/:
#   python3 scripts/apply_verdicts.py \
#     --verdicts batches/batch-04-recent-confirmed/VERDICTS-batch-04.md \
#     --batch-dir batches/batch-04-recent-confirmed
# Each "## VERDICT <id>" block replaces the empty TRIAGE VERDICT section in the
# matching issue_<id>.md; notes/report above the marker are preserved.

## VERDICT 13819  Family Edit reorders parent families (MAJOR)
- **Actionable?** yes — lead item, root cause + fix in thread (note 1)
- **Where does the fix go?** gramps core (../gramps)
- **Branch target:** gramps core → maintenance/gramps61
- **Root cause (one line):** child-ref lists compared by Python IDENTITY not handle; orig_set and new_set hold different instances of the same children, so set.difference() marks every child both removed and re-added → reorder.
- **Does the reporter's workaround match the real root cause?** Reporter's own diagnosis (note 1) is correct and is the fix.
- **Fix sketch:** compare child refs by handle, not object identity, when diffing.
- **Repro on example.gramps?** yes — open a family with ≥2 parent families, edit + OK, observe reorder.
- **Test location & type:** core unittest on the child-ref diff with equal-handle/different-instance objects; assert no spurious add/remove.
- **Related issues / commits / upstream PRs to read first:** note 1 says author "plan to work on this today" — CHECK for an already-landed fix/PR (merged AND closed).
- **Check upstream isn't already ahead:** git log gramps61 on the family editor child-ref diff; check closed PRs.

## VERDICT 13747  Saving unmodified DB changes it on disk
- **Actionable?** yes — root cause + fix in thread (notes 3-4)
- **Where does the fix go?** gramps core (../gramps)
- **Branch target:** gramps core → maintenance/gramps61
- **Root cause (one line):** metadata (name-types etc.) stored as Python sets (unordered); every db-close re-serializes them in a different order → on-disk change with no user edit.
- **Does the reporter's workaround match the real root cause?** Yes; note 3 (maintainer) confirms metadata is always saved on close.
- **Fix sketch:** deterministic ordering — sort the set before storing (or use an ordered structure) so serialization is stable. SCOPE: ordering only; do NOT bundle the read-only-export-mode split (separate ticket 13748, note 2).
- **Repro on example.gramps?** yes — open, close without editing, diff the on-disk file.
- **Test location & type:** core unittest — serialize metadata twice, assert byte-stable output.
- **Related issues / commits / upstream PRs to read first:** 13748 (the split-off read/write-mode issue — do not fix here). 13744 (sibling serialization issue).
- **Check upstream isn't already ahead:** git log gramps61 on metadata serialization; check closed PRs.

## VERDICT 13716  Sidebar Filter gramplet Type popup not updated
- **Actionable?** yes — root cause + reference impl in thread (note 3)
- **Where does the fix go?** gramps core (../gramps)
- **Branch target:** gramps core → maintenance/gramps61
- **Root cause (one line):** sidebar filter Types selector is built once when the view first opens and never refreshed; custom types read at db-open don't propagate (maintainer, note 3). Other dialogs rebuild their type selector each time so they show updates.
- **Does the reporter's workaround match the real root cause?** Yes — note 3 is the maintainer's precise explanation.
- **Fix sketch:** generalize the place-sidebar-filter refresh the maintainer already built in PR #809 (enhanced places) to the other sidebar filters. READ PR #809 first.
- **Repro on example.gramps?** yes — add a custom type (or import the John Cardinal GEDCOM, notes 1-2, which creates custom GEDCOM-import note types), check the sidebar filter Type popup doesn't list it until restart.
- **Test location & type:** core unittest on the sidebar filter type-list refresh path.
- **Related issues / commits / upstream PRs to read first:** PR #809 (the reference fix for place sidebar filters).
- **Check upstream isn't already ahead:** check whether #809's approach was already generalized; check closed PRs.

## VERDICT 13744  Empty dates saved in non-round-tripping format
- **Actionable?** yes
- **Where does the fix go?** gramps core (../gramps) — date serialization
- **Branch target:** gramps core → maintenance/gramps61
- **Root cause (one line):** an empty date is serialized in a form that doesn't round-trip (re-import/validate fails); needs CSV + the attached simpson.gramps fixture (note 1) to pin the exact format.
- **Does the reporter's workaround match the real root cause?** Thread is thin (just the fixture); triage from CSV + fixture.
- **Fix sketch:** ensure empty/partial dates serialize to a round-trip-stable representation. Confirm the exact failing format from simpson.gramps first.
- **Repro on example.gramps?** use the attached fixture, or construct an empty date, save, reload.
- **Test location & type:** core unittest round-tripping an empty date.
- **Related issues / commits / upstream PRs to read first:** 13747 (sibling serialization-stability issue; distinct cause).
- **Check upstream isn't already ahead:** git log gramps61 on date serialization; check closed PRs.

## VERDICT 13864  Dashboard crashes & locks family tree
- **Actionable?** yes (CSV repro; thread only "Confirmed on 6.0.1!")
- **Where does the fix go?** gramps core (../gramps) — Dashboard / gramplet loading
- **Branch target:** gramps core → maintenance/gramps61
- **Root cause (one line):** not diagnosed in-thread; a Gramplet-loading path crashes and locks the tree. Derive from CSV Steps on repro.
- **Does the reporter's workaround match the real root cause?** No workaround; confirm on repro.
- **Fix sketch:** determine on repro; likely an unguarded gramplet-load/teardown path. LIKELY CLUSTER with 13865 (both Dashboard, both 6.0.1, same reporter) — verify shared cause before two fixes.
- **Repro on example.gramps?** follow CSV Steps.
- **Test location & type:** interface test if GUI-only; core unittest if the gramplet-load path is reachable headless.
- **Related issues / commits / upstream PRs to read first:** 13865 (probable cluster).
- **Check upstream isn't already ahead:** git log gramps61 on Dashboard/gramplet load; check closed PRs.

## VERDICT 13865  Dashboard Number of Columns 20 / added gramplet
- **Actionable?** yes (CSV repro + screenshots; thread "Confirmed on 6.0.1!")
- **Where does the fix go?** gramps core (../gramps) — Dashboard column handling
- **Branch target:** gramps core → maintenance/gramps61
- **Root cause (one line):** not diagnosed in-thread; setting columns to 20 + adding a gramplet misbehaves. Derive on repro.
- **Does the reporter's workaround match the real root cause?** No workaround.
- **Fix sketch:** determine on repro. CLUSTER with 13864 — verify whether one root cause covers both before separate fixes.
- **Repro on example.gramps?** set columns to 20, add a gramplet, per CSV Steps.
- **Test location & type:** interface test (GUI), or core unittest on the column-config path if reachable.
- **Related issues / commits / upstream PRs to read first:** 13864 (probable cluster).
- **Check upstream isn't already ahead:** git log gramps61 on Dashboard columns; check closed PRs.

## VERDICT 13876  Citation Tree view fails to delete citations
- **Actionable?** yes — genuine NO-NOTES (empty thread, not restricted); CSV repro
- **Where does the fix go?** gramps core (../gramps) — Citation Tree view delete
- **Branch target:** gramps core → maintenance/gramps61
- **Root cause (one line):** not diagnosed (no thread); deleting a citation in Citation Tree view mode fails. Derive on repro.
- **Does the reporter's workaround match the real root cause?** No thread; CSV Steps only.
- **Fix sketch:** determine on repro; likely the tree-vs-flat view delete path differs.
- **Repro on example.gramps?** yes — Citations → Tree view mode → delete a citation, per CSV Steps.
- **Test location & type:** interface test if GUI-only; core unittest if the delete path is reachable headless.
- **Related issues / commits / upstream PRs to read first:** none.
- **Check upstream isn't already ahead:** git log gramps61 on citation tree view; check closed PRs.

## VERDICT 13418  LaTeX report exception (str_incr index)
- **Actionable?** yes
- **Where does the fix go?** gramps core (../gramps) — plugins/docgen/latexdoc.py
- **Branch target:** gramps core → maintenance/gramps61
- **Root cause (one line):** latexdoc.py str_incr (~line 512) does `if lili[i] < "z"` with `i` a STRING not int → TypeError: list indices must be integers; hit via the multicol width path (calc_latex_widths → handle_table → end_table) when a styled note forces it.
- **CORRECTION:** note 1's familygroup.py traceback is daleathan's *13417* call stack (KeyError: 9), NOT this bug. The real traceback is in the DESCRIPTION (latexdoc.py:512). codefarmer (notes 3-4) confirms 13418 reproduces on 5.2.2 without the 13417 changes.
- **Does the reporter's workaround match the real root cause?** Description traceback is correct; note 1 is a different (related) bug.
- **Fix sketch:** fix the indexing in str_incr — iterate by integer index, not the string element.
- **Repro on example.gramps?** yes (Steps): person Garner von Zieliński Lewis Anderson Sr, Reports → Text → Complete Individual Report, output LaTeX, include notes, note with subscript+strikethrough.
- **Test location & type:** core unittest → gramps/plugins/docgen/test/ exercising str_incr / the multicol width path; assert no TypeError. Headless, preferred.
- **Related issues / commits / upstream PRs to read first:** bug 13417 / PR 1762 — confirm state on gramps61 and that str_incr is independent (it is, note 3).
- **Check upstream isn't already ahead:** git log gramps61 -- plugins/docgen/latexdoc.py; check closed PRs touching str_incr/calc_latex_widths.

## VERDICT 13413  Fan Chart font size — DUPLICATE of 12028
- **Actionable?** no — duplicate
- **Where does the fix go?** N/A (track under canonical 12028)
- **Branch target:** N/A
- **Root cause (one line):** fan-chart report font size varies across generations and per-gen custom styles aren't honored; daleathan (notes 4-6) marks it a duplicate of 0012028, already confirmed there.
- **Does the reporter's workaround match the real root cause?** N/A.
- **Fix sketch:** none here; if fixed, fix in the 12028 context.
- **Repro on example.gramps?** redundant with 12028.
- **Test location & type:** N/A.
- **Related issues / commits / upstream PRs to read first:** 0012028 (canonical).
- **Check upstream isn't already ahead:** check 12028 status / any fan-chart font PR.
- **DISPOSITION:** close as duplicate of 12028; mantis dup pointer.

## VERDICT 13268  Notes editor Undo scrolls to top
- **Actionable?** yes
- **Where does the fix go?** gramps core (../gramps) — Notes (StyledText) editor
- **Branch target:** gramps core → maintenance/gramps61
- **Root cause (one line):** undo in the Notes editor resets scroll to the top instead of preserving position; the undo handler doesn't restore the TextView scroll/cursor after applying.
- **Does the reporter's workaround match the real root cause?** No workaround; symptom is clear.
- **Fix sketch:** preserve and restore scroll (and cursor) position across undo in the notes editor.
- **Repro on example.gramps?** yes — open a long note, scroll to bottom, undo → jumps to top.
- **Test location & type:** GUI-only → gramps-testbed/tests/interface/test_bug_13268_notes_undo_scroll.py on a seeded long-note fixture (scroll position is hard to assert headlessly; otherwise an interface test that exercises undo without exception + manual visual confirm).
- **Related issues / commits / upstream PRs to read first:** **13267** — note 2: the same GIF shows BOTH 13268 and 13267. Check 13267's relationship (possible shared undo-handler cause) before fixing.
- **Check upstream isn't already ahead:** git log gramps61 on the notes/styledtext editor; check closed PRs.

## VERDICT 13830  Graph View path-to-home — ALREADY FIXED (core)
- **Actionable?** no — already fixed upstream (core); confirm-and-close
- **Where does the fix go?** gramps core (../gramps) — already fixed
- **Branch target:** gramps core → maintenance/gramps61 (verify fix is on branch)
- **Root cause (one line):** core bug in gramps/gen/filters/rules/person/_relationshippathbetween.py — `for x in firstList and secondList` short-circuits to secondList, iterating the wrong list → KeyError on firstMap[handle] (note 4 triage). Also a config-key-casing change (commit 6357efb) left stale uppercase ini keys (note 3).
- **Does the reporter's workaround match the real root cause?** The GraphView symptom masked a core filter bug; note 4 confirms it's core, not the addon.
- **Fix sketch:** none new — confirm the core fix is an ancestor of gramps61, cite the commit. (Stale-ini-keys is a user-side cleanup, note 3.)
- **Repro on example.gramps?** confirm-only.
- **Test location & type:** none (confirm-and-close).
- **Related issues / commits / upstream PRs to read first:** the _relationshippathbetween.py fix commit; commit 6357efb (config key casing).
- **Check upstream isn't already ahead:** YES — verify the fix commit is on gramps61.
- **DISPOSITION:** confirm-and-close; mantis cites the fixing commit + Fixed in version.

## VERDICT 13707  Lib WebConnect depends_on — ALREADY FIXED
- **Actionable?** no — already fixed (PR 640) before the report; confirm-and-close
- **Where does the fix go?** addons-source — already fixed
- **Branch target:** addons-source → maintenance/gramps60 (verify)
- **Root cause (one line):** WebConnect packs needed depends_on=["libwebconnect"]; note 4 triage: every pack has declared it since commit 7c3002157 (PR 640, merged 2025-02-06), which pre-dates the 2025-03-16 report. Reporter saw a pre-rc2 / local state.
- **Does the reporter's workaround match the real root cause?** N/A — already resolved.
- **Fix sketch:** none.
- **Repro on example.gramps?** confirm-only — verify depends_on present on gramps60.
- **Test location & type:** none.
- **Related issues / commits / upstream PRs to read first:** PR 640 / commit 7c3002157.
- **Check upstream isn't already ahead:** YES — already ahead; cite PR 640.
- **DISPOSITION:** confirm-and-close; mantis cites PR 640 + Fixed in version.

## VERDICT 13920  FTV Pango TypeError — EXTERNAL + already fixed
- **Actionable?** no — external repo + already fixed; close
- **Where does the fix go?** external repo (ztlxltl/FamilyTreeView) — NOT addons-source
- **Branch target:** N/A (external)
- **Root cause (one line):** upstream GTK/Pango bug (gitlab.gnome.org/GNOME/gtk#7651) surfacing in FamilyTreeView, an EXTERNAL experimental addon; ztlxltl released FTV v0.1.164 with a fallback (note 4); resolved, no user feedback (note 5).
- **Does the reporter's workaround match the real root cause?** The Pango downgrade (notes 2-3) is a stopgap; the real fix is FTV's v0.1.164 fallback + the upstream GTK fix.
- **Fix sketch:** none here.
- **Repro on example.gramps?** N/A.
- **Test location & type:** none.
- **Related issues / commits / upstream PRs to read first:** GTK issue #7651; FTV issues #60/#61; FTV v0.1.164.
- **Check upstream isn't already ahead:** external — FTV v0.1.164 already addresses it.
- **DISPOSITION:** close as external (FTV) + already-fixed; mantis points to FTV v0.1.164 and the upstream GTK issue. NOT an addons-source target.

## VERDICT 13326  Forms gallery AttributeError — CORE teardown race (PR 2330)
- **Actionable?** yes — already diagnosed by Eduard (note 5); verify PR 2330 state
- **Where does the fix go?** gramps core (../gramps) — NOT the Forms addon
- **Branch target:** gramps core → maintenance/gramps61
- **Root cause (one line):** teardown race — GalleryTab.clean_up() removes self.iconlist via track_ref_for_deletion but doesn't disconnect the 'selection-changed' handler on the still-live Gtk.IconView; on Cancel the widget fires a final selection-changed → get_selected() → self.iconlist → AttributeError. Regression: original disconnect (svn r20849 / 51a53ccebd, 2012) removed by 37395da262 (2023) to silence a GTK warning.
- **Does the reporter's workaround match the real root cause?** Title blames Forms; traceback is entirely core display-tab code. Forms only hosts a GalleryTab and calls clean_up() correctly. Fix is core.
- **Fix sketch:** restore the disconnect — capture the handler id at connect, disconnect at head of clean_up(), guarded by GObject.signal_handler_is_connected so the already-disposed case stays warning-free. (= gramps PR 2330.)
- **Repro on example.gramps?** yes (note 4): install Forms, configure a Source as form, new form, gallery tab, add image, select it, Cancel.
- **Test location & type:** core → gramps/gui/editors/displaytabs/test/gallerytab_test.py. Case 1: capture signal id on live iconlist, clean_up(), assert via signal_handler_find no handler remains. Case 2: destroy iconlist before clean_up(), assert via warnings.catch_warnings no "no handler with id" warning.
- **Related issues / commits / upstream PRs to read first:** svn r20849/51a53ccebd, 37395da262, gramps PR 2330. Bug 13059 (selectionwidget) is the same teardown-race family.
- **Check upstream isn't already ahead:** VERIFY PR 2330 state first — if merged, confirm-and-close.

## VERDICT 13979  PostgreSQL Enhanced row click crash — ADDON fix
- **Actionable?** yes — root cause in thread (note 3)
- **Where does the fix go?** addons-source — Plugin Manager Enhanced addon
- **Branch target:** addons-source → maintenance/gramps60
- **Root cause (one line):** PluginStatus.__info (PluginManager.py:655) does `" ".join(req_lst[0])` where req_lst is a [label, table] pair; core Requirements.info emits label + EMPTY table when an addon listing has a present-but-empty requires key (rm/rg/re: []) → index error on req_lst[0] (note 3 triage).
- **Does the reporter's workaround match the real root cause?** Reporter framed it as PostgreSQL Enhanced; the defect is in the Enhanced Plugin Manager addon's handling of empty requires.
- **Fix sketch:** guard the empty-table case in the Enhanced Plugin Manager addon before joining req_lst[0].
- **Repro on example.gramps?** config-level: load Plugin Manager Enhanced, click a row (e.g. PostgreSQL Enhanced) whose listing has an empty requires key.
- **Test location & type:** addon unit test → addons-source/PluginManager*/tests/, feeding a present-but-empty requires key.
- **Related issues / commits / upstream PRs to read first:** core Requirements.info API (to confirm the empty-table emission is intended).
- **Check upstream isn't already ahead:** git log gramps60 on the Enhanced Plugin Manager; check closed PRs.

## VERDICT 13966  Closing tree → Prerequisites Checker AttributeError — PR 913 open
- **Actionable?** yes — PR already opened (note 1); review-and-confirm
- **Where does the fix go?** addons-source — PrerequisitesChecker gramplet
- **Branch target:** addons-source → maintenance/gramps60 (NB PR 913 was opened vs gramps61 — verify intended branch)
- **Root cause (one line):** PrerequisitesCheckerGramplet.main() is a generator the framework keeps stepping after tree close; active_page is None, unguarded .bottombar read → AttributeError (note 1).
- **Does the reporter's workaround match the real root cause?** Yes — note 1 (PR author) gives root cause + fix.
- **Fix sketch:** read active_page into a local, return early if None; the existing short-circuit chain runs unchanged. Regression test in same change.
- **Repro on example.gramps?** open then close a tree with the gramplet active.
- **Test location & type:** addon unit test (note 1 says a regression test ships in PR 913).
- **Related issues / commits / upstream PRs to read first:** **addons-source PR #913** — verify state + branch target.
- **Check upstream isn't already ahead:** YES — PR 913 exists; if merged, confirm-and-close; resolve the gramps60-vs-61 branch question.

## VERDICT 13888  GenealogyTree LaTeX thumbnails — BY-DESIGN / option
- **Actionable?** deferred — not a defect; option request (Eduard decision)
- **Where does the fix go?** addons-source — GenealogyTree addon (only if option taken)
- **Branch target:** addons-source → maintenance/gramps60
- **Root cause (one line):** intentional change in PR 1620 (azrdev, note 5) to embed thumbnails not originals (smaller PDFs, avoids latex-parser filename issues); reporter + others want full images back (notes 3-4). Maintainer acknowledges the workflow break.
- **Does the reporter's workaround match the real root cause?** It's not a bug; it's a deliberate behavior change.
- **Fix sketch:** make full-image-vs-thumbnail a USER OPTION (notes 4 ask exactly this). Otherwise close as by-design with the PR 1620 rationale.
- **Repro on example.gramps?** generate a GenealogyTree LaTeX report; observe thumbnails referenced.
- **Test location & type:** if option implemented — addon unit test on the option toggle.
- **Related issues / commits / upstream PRs to read first:** PR 1620 (the intentional change).
- **Check upstream isn't already ahead:** check whether an option was already added.
- **DISPOSITION:** Eduard decides: implement the option (enhancement) or close by-design. Mantis explains the intentional change + the option offer/decline.

## VERDICT 13694  make.py corrupts listing on unsupported input — ADDON tooling fix
- **Actionable?** yes — reframed robustness bug (note 2 triage)
- **Where does the fix go?** addons-source — make.py tooling
- **Branch target:** addons-source → maintenance/gramps60 (verify which branch's make.py; reproduced on gramps61 + master too)
- **Root cause (one line):** `make.py <ver> listing <addon>` against an addon whose .gpr.py has include_in_listing=False corrupts the listings output; prculley (note 1) is right that `listing` isn't the unlist command, but the tool corrupting its output on unsupported input is a real robustness bug (note 2).
- **Does the reporter's workaround match the real root cause?** The user used the wrong command; the actionable defect is the tool not handling it gracefully.
- **Fix sketch:** make.py should reject/no-op gracefully on an include_in_listing=False addon passed to `listing`, not corrupt the listings file.
- **Repro on example.gramps?** N/A — tooling: `python3 make.py gramps61 listing <False-addon>` corrupts output (note 2, confirmed gramps61 + master).
- **Test location & type:** tooling test invoking the listing path on a False addon; assert listings unchanged.
- **Related issues / commits / upstream PRs to read first:** make.py listing/unlist/as-needed commands.
- **Check upstream isn't already ahead:** git log on make.py; check closed PRs.

## VERDICT 13906  Addon manager locale fallback — already works; mostly close
- **Actionable?** deferred / close — reported defect doesn't exist (fallback works)
- **Where does the fix go?** gramps core (../gramps) only if message enhancement taken
- **Branch target:** gramps core → maintenance/gramps61 (only if enhancing)
- **Root cause (one line):** reporter claims no English fallback for unsupported locales, but Nick_H (note 8) shows it already exists (gramps/gen/plug/utils.py:218/226); the residual "couldn't update isotammi without restarting in English" (note 11) is unreproduced.
- **Does the reporter's workaround match the real root cause?** No — the premise is incorrect per the maintainer.
- **Fix sketch:** none for the stated bug. Optional: append "Using 'English' instead." to the fallback warning + capitalize English (note 9); better not-found messaging.
- **Repro on example.gramps?** N/A — locale/config; maintainers couldn't reproduce (note 12 suggests closing).
- **Test location & type:** none unless message enhancement taken.
- **Related issues / commits / upstream PRs to read first:** 13174 (cluster — same warning, different cause). utils.py:226 (existing fallback).
- **Check upstream isn't already ahead:** fallback already exists — cite utils.py:226.
- **DISPOSITION:** close as "fallback already exists"; offer to split the unexplained update-failure into a new issue. CLUSTER with 13174 — do NOT bundle (different causes).

## VERDICT 13174  Addon manager isotammi crash — CORE crash fix (cluster w/ 13906)
- **Actionable?** yes — as a core crash fix (not the locale ask)
- **Where does the fix go?** gramps core (../gramps)
- **Branch target:** gramps core → maintenance/gramps61
- **Root cause (one line):** hard crash = dangling window pointer passed to the Gtk draw cycle when Addon Manager refreshes against a listings URL whose .json is missing (jralls note 6: "not a Mac-specific problem"); the 404 itself is expected.
- **Does the reporter's workaround match the real root cause?** No — reporter framed it as "wrong URL"; real defect is unguarded teardown/redraw on failed refresh.
- **Fix sketch:** guard the refresh path so a not-found listing can't leave a dangling window pointer; add actionable feedback on bad/empty Project URL (note 8 items 1-3).
- **Repro on example.gramps?** config-level: Addon Manager → add a Project URL pointing at a 5.1/nonexistent listings dir → Refresh. Crash was first-time-only on Win10 5.2.0-rc1 (note 3). VERIFY still reproduces on gramps61; if not, can't-repro close.
- **Test location & type:** core unittest on refresh-with-missing-listing (assert graceful, no exception); GUI crash may need an interface test if reachable.
- **Related issues / commits / upstream PRs to read first:** 13906 (cluster).
- **Check upstream isn't already ahead:** grep gramps61 addon-manager refresh for not-found guards; check closed PRs.
- **CLUSTER NOTE:** shares the 404 SYMPTOM with 13906 but the CAUSE differs (crash vs working-fallback). Do NOT treat as one fix.

## VERDICT 14014  Gramps-Web empty range-date import — PARTIAL UPSTREAM
- **Actionable?** yes — core import hardening (the gramps-web side is upstream)
- **Where does the fix go?** gramps core (../gramps) for hardening; gramps-web emission is upstream
- **Branch target:** gramps core → maintenance/gramps61
- **Root cause (one line):** reporter's data had <daterange start="1911-09-01" stop=""/> (empty stop) created via Gramps-Web; an uncaught exception on empty stop was introduced by commit 634e5ccc (note 4). Gramps "never allowed ranges with a single date" (note 9).
- **Does the reporter's workaround match the real root cause?** Not example.gramps-reproducible; it's malformed data from Gramps-Web (notes 7-11).
- **Fix sketch:** (a) core import should not raise an UNCAUGHT exception on malformed stop — wrap defensively; add a Verify-the-Data check (note 9). (b) Gramps-Web shouldn't emit stop="" (gramps-web #780 — external).
- **Repro on example.gramps?** reproducible by deliberately corrupting a date (note 6 gives the exact snippet); not via normal desktop entry.
- **Test location & type:** core unittest importing XML with stop="" ; assert handled error not uncaught exception.
- **Related issues / commits / upstream PRs to read first:** commit 634e5ccc; gramps-web #780.
- **Check upstream isn't already ahead:** check gramps61 import/date handling around 634e5ccc; check closed PRs.
- **DISPOSITION:** core defensive-import + verify-check fix (gramps61); note the gramps-web emission is upstream in the mantis comment.

## VERDICT 13832  Gramps-Web UUID hyphen handles break Graph View — CORE handle handling
- **Actionable?** yes — root cause in thread (notes 5-10)
- **Where does the fix go?** gramps core (../gramps) — handle handling
- **Branch target:** gramps core → maintenance/gramps61
- **Root cause (one line):** Gramps-Web creates handles as UUIDv4 WITH hyphens; some core/GraphView paths fail on hyphenated handles. dstraub (note 10): schema allows any ≤50-char string, so "not handling arbitrary schema-valid handle strings is a bug."
- **Does the reporter's workaround match the real root cause?** Editing out the hyphens (note 6) confirms the cause but isn't the fix; core should accept hyphenated handles.
- **Fix sketch:** make the affected path handle arbitrary schema-valid handle strings (hyphens/UUID), not assume a charset. Distinct from 13830 (path-to-home short-circuit) — this is handle-format.
- **Repro on example.gramps?** yes — import the reporter's example.gramps (note 1) with hyphenated handles; Graph View blanks.
- **Test location & type:** core unittest exercising the affected path with a hyphenated/UUID handle.
- **Related issues / commits / upstream PRs to read first:** 13830 (different GraphView cause). gramps-web util.js handle generation (note 10).
- **Check upstream isn't already ahead:** check gramps61 handling of hyphenated handles; check closed PRs.

## VERDICT 13984  Dashboard label wrong language after install — repro-or-close
- **Actionable?** yes — repro-or-close
- **Where does the fix go?** gramps core (../gramps) — localization / install state
- **Branch target:** gramps core → maintenance/gramps61
- **Root cause (one line):** Dashboard label shows the wrong language after install — likely a locale/translation-load timing or cached-state issue; thin thread (3 notes), derive on repro.
- **Does the reporter's workaround match the real root cause?** Undetermined; may be environment/install-state specific.
- **Fix sketch:** determine on repro; if environment-specific (stale locale cache) → external/close.
- **Repro on example.gramps?** attempt: install/switch locale, observe Dashboard label language.
- **Test location & type:** core unittest if a translation-load path is implicated; else repro-or-close.
- **Related issues / commits / upstream PRs to read first:** none.
- **Check upstream isn't already ahead:** check gramps61 locale init; check closed PRs.

## VERDICT 13518  RCS Archive Tree Manager can't rename — repro-or-close
- **Actionable?** yes — repro-or-close
- **Where does the fix go?** gramps core (../gramps) — Tree Manager / RCS archive
- **Branch target:** gramps core → maintenance/gramps61
- **Root cause (one line):** renaming an RCS-archived backup in Tree Manager fails; thin thread, derive on repro.
- **Does the reporter's workaround match the real root cause?** Undetermined.
- **Fix sketch:** determine on repro.
- **Repro on example.gramps?** attempt: create an RCS archive of a tree, try to rename it in Tree Manager.
- **Test location & type:** core unittest if reachable; else interface/repro-or-close.
- **Related issues / commits / upstream PRs to read first:** RCS archive code.
- **Check upstream isn't already ahead:** check gramps61 Tree Manager / RCS; check closed PRs.

## VERDICT 13406  Top Surnames quick view + name prefix — repro-or-close (likely real)
- **Actionable?** yes
- **Where does the fix go?** gramps core (../gramps) — Top Surnames quick view / surname filter
- **Branch target:** gramps core → maintenance/gramps61
- **Root cause (one line):** the quick-view click builds its search from the full surname including prefix (e.g. "de Boer") while the surname is stored as prefix="de" + surname="Boer", so the lookup finds nobody though the gramplet counted them (reporter, note 5: only fails with a prefix; prefix-less works).
- **Does the reporter's workaround match the real root cause?** Reporter's prefix hypothesis is well-supported.
- **Fix sketch:** make the quick-view surname lookup use the same prefix-aware surname representation the gramplet count uses.
- **Repro on example.gramps?** example.gramps lacks prefixed surnames (note 5) — build a tiny fixture with one "de Boer"-style name (reporter's allefriezen.gramps, note 3, is such a file).
- **Test location & type:** core unittest on the surname quick-view query with a prefixed surname; assert found.
- **Related issues / commits / upstream PRs to read first:** Top Surnames gramplet + the samesurnames quick view it invokes.
- **Check upstream isn't already ahead:** git log gramps61 on surnames quick view; check closed PRs.

## VERDICT 13387  Age Calculator estimated-date contamination — repro-or-close (likely real)
- **Actionable?** yes
- **Where does the fix go?** gramps core (../gramps) — date/age estimation
- **Branch target:** gramps core → maintenance/gramps61
- **Root cause (one line):** an explicit "estimated between Y1 and Y2" still has the global 'about' ± limit applied on top, re-widening a tight explicit range (e.g. between 1968 and 1978 → age 19–94); explicit range should override the 'about' preference.
- **Does the reporter's workaround match the real root cause?** Reporter's analysis is correct.
- **Fix sketch:** when a date carries an explicit range, use those bounds directly rather than expanding each endpoint by the 'about' year range.
- **Repro on example.gramps?** yes — add an event "estimated between 1968 and 1978" to a person; observe inflated age range.
- **Test location & type:** core unittest on the date-span/age computation for an explicit-range estimated date vs 'about'; assert explicit bounds win.
- **Related issues / commits / upstream PRs to read first:** date span / probably-alive computation (gen/lib/date.py, datehandler).
- **Check upstream isn't already ahead:** git log gramps61 on date span calc; check closed PRs.

## VERDICT 13270  Chart tooltip dagger for living person — repro-or-close (likely real)
- **Actionable?** yes
- **Where does the fix go?** gramps core (../gramps) — chart/view tooltip
- **Branch target:** gramps core → maintenance/gramps61
- **Root cause (one line):** the chart mouseover tooltip shows the deceased dagger whenever death date is missing, without consulting the "max age to be considered living" probably-alive logic.
- **Does the reporter's workaround match the real root cause?** Reporter's diagnosis (description) is correct.
- **Fix sketch:** gate the dagger on the same probably-alive / max-age determination used elsewhere, not merely "death date present?".
- **Repro on example.gramps?** yes — living person with no death date, hover their box in a chart view → dagger shown.
- **Test location & type:** core unittest on the tooltip alive/deceased decision given missing death date + living window; assert no dagger for probably-alive.
- **Related issues / commits / upstream PRs to read first:** resolve which chart view's tooltip by reproducing.
- **Check upstream isn't already ahead:** git log gramps61 on chart tooltip; check closed PRs.

## VERDICT 13205  Merge Citations MergeError — RESTRICTED (CSV-only)
- **Actionable?** yes — repro-or-close from CSV (thread is permission-restricted)
- **Where does the fix go?** gramps core (../gramps) — likely
- **Branch target:** gramps core → maintenance/gramps61
- **Root cause (one line):** Merge Citations tool raises MergeError "Encountered an object of type Note that has a citation reference" (mergecitations.py:205) — merge logic rejects a Note carrying a citation reference, killing the run instead of handling it.
- **Does the reporter's workaround match the real root cause?** N/A — thread access-restricted; triage from CSV traceback.
- **Fix sketch:** in plugins/tool/mergecitations.py handle the note-with-citation-reference case instead of an unrecoverable MergeError. Confirm current gramps61 behavior first.
- **Repro on example.gramps?** attempt: two citations, a note carrying a citation reference, Tools → Family Tree Processing → Merge Citations (default options). If not reproducible → can't-repro close.
- **Test location & type:** core unittest on the merge path with a note-bearing-citation-reference fixture.
- **Related issues / commits / upstream PRs to read first:** closed/merged PRs touching mergecitations.py since 5.2.0.
- **Check upstream isn't already ahead:** git log gramps61 -- plugins/tool/mergecitations.py.
- **ACCESS NOTE:** issue is permission-restricted; mantis-comment notes triage was from the public CSV + repro, not the thread.

## VERDICT 14033  Place cycle detected — macOS, MANUAL-VERIFICATION (reclassified)
- **Actionable?** no on Linux — macOS-specific, possibly by-design; MANUAL-VERIFICATION
- **Where does the fix go?** gramps core macOS port (if anything) — undetermined
- **Branch target:** gramps core → maintenance/gramps61 (only if a fix emerges)
- **Root cause (one line):** "Place cycle detected" dialog fires on opening a place; reproducible ONLY on macOS (Apple Silicon, Tahoe), NOT on Windows 10/11 (notes 5,15,18); sporadic; one maintainer calls it "more a usage issue than Gramps issue — the dialog only reports an attempted loop" (note 5). Memory-leak angle split to issue 14044 (notes 13,17).
- **Does the reporter's workaround match the real root cause?** Unclear — sporadic and macOS-only; may be a Mac-port rendering/event quirk.
- **Fix sketch:** none confirmable on Linux. Needs jralls or Eduard's macOS VM.
- **Repro on example.gramps?** macOS only — open places, the dialog fires sporadically (notes 14,18 repro on example file on macOS).
- **Test location & type:** none automatable on Linux.
- **Related issues / commits / upstream PRs to read first:** 14044 (split-off memory issue).
- **Check upstream isn't already ahead:** check placerefembedlist.py handle_extra_type on gramps61.
- **DISPOSITION:** MANUAL-VERIFICATION.md (macOS). Do NOT treat as a Linux core fix; possibly by-design (dialog correctly warns of an attempted cycle).

## VERDICT 14230  macOS S3/boto3 media hosting — MANUAL-VERIFICATION (macOS)
- **Actionable?** no on Linux — MANUAL-VERIFICATION (macOS); check POSSIBLY-FIXED
- **Where does the fix go?** addons-source (the S3 media addon) — verify on macOS
- **Branch target:** addons-source → maintenance/gramps60
- **Root cause (one line):** boto3 problems hosting media on S3 on macOS; POSSIBLY-FIXED flag — check for a release fix first. Can't confirm on Linux without the S3/boto3 setup.
- **Does the reporter's workaround match the real root cause?** Undetermined.
- **Fix sketch:** determine on macOS repro; may already be fixed.
- **Repro on example.gramps?** macOS + an S3 bucket + boto3 — not Linux-confirmable.
- **Test location & type:** none automatable here.
- **Related issues / commits / upstream PRs to read first:** the S3 media addon history (POSSIBLY-FIXED).
- **Check upstream isn't already ahead:** check the addon for a fix release first.
- **DISPOSITION:** MANUAL-VERIFICATION.md (macOS); first confirm it isn't already fixed.

## VERDICT 13983  macOS no further editing after load — MANUAL-VERIFICATION (macOS)
- **Actionable?** no on Linux — MANUAL-VERIFICATION (macOS)
- **Where does the fix go?** gramps core macOS port — verify on macOS
- **Branch target:** gramps core → maintenance/gramps61
- **Root cause (one line):** after loading a family tree on macOS, no further editing is possible (12 notes); macOS-port event/focus issue, not Linux-confirmable.
- **Does the reporter's workaround match the real root cause?** Undetermined — read the 12-note thread on macOS verification.
- **Fix sketch:** determine on macOS repro.
- **Repro on example.gramps?** macOS only.
- **Test location & type:** none automatable here.
- **Related issues / commits / upstream PRs to read first:** the thread (12 notes) for any maintainer diagnosis.
- **Check upstream isn't already ahead:** check gramps61 macOS port commits.
- **DISPOSITION:** MANUAL-VERIFICATION.md (macOS).

## VERDICT 13774  macOS Life Line Ancestor Chart install crash — MANUAL-VERIFICATION (macOS)
- **Actionable?** no on Linux — MANUAL-VERIFICATION (macOS); likely same as 13223
- **Where does the fix go?** macOS packaging (pip-absent) — likely by-design like 13223
- **Branch target:** N/A (likely by-design) or gramps61 if graceful-error hardening taken
- **Root cause (one line):** installing the Life Line Ancestor Chart addon crashes on macOS — almost certainly the same pip-absent prerequisite failure as 13223 (macOS .app ships without pip).
- **Does the reporter's workaround match the real root cause?** Likely the 13223 root cause.
- **Fix sketch:** none as a defect; the only code action is the graceful pip-absent error message (see 13223).
- **Repro on example.gramps?** macOS only — install an addon with a pip prerequisite.
- **Test location & type:** as 13223 (graceful-error unittest) if taken.
- **Related issues / commits / upstream PRs to read first:** **13223** (same pip-absent cause).
- **Check upstream isn't already ahead:** as 13223.
- **DISPOSITION:** MANUAL-VERIFICATION.md (macOS); cross-reference 13223; likely by-design + graceful-error hardening.

## VERDICT 13223  macOS addon install pip-absent — MANUAL-VERIFICATION (by-design)
- **Actionable?** no (by-design) — MANUAL-VERIFICATION + close
- **Where does the fix go?** none (macOS packaging) / core graceful-error hardening only
- **Branch target:** gramps core → maintenance/gramps61 (only for the graceful-error fix)
- **Root cause (one line):** macOS .dmg/.app intentionally ships without pip (jralls, notes 2/4), so the addon-prerequisite installer (FileNotFoundError: 'pip') can't run — a deliberate packaging choice, not a code defect.
- **Does the reporter's workaround match the real root cause?** Maintainer position: don't want pip on macOS; use MacPorts/Homebrew.
- **Fix sketch:** none as a defect. Optional real hardening: core (_windows.py:289 subprocess) should catch missing-pip and show an actionable message instead of an unhandled FileNotFoundError.
- **Repro on example.gramps?** macOS only — install an addon with a pip prerequisite on the .app build.
- **Test location & type:** if hardening taken — core unittest asserting a caught, clear error when pip is absent.
- **Related issues / commits / upstream PRs to read first:** the discourse threads (notes 2/4); 13774 (same cause).
- **Check upstream isn't already ahead:** check _windows.py on gramps61 for a pip-missing guard.
- **DISPOSITION:** MANUAL-VERIFICATION.md (macOS) documenting by-design; recommend the graceful-error hardening as the only worthwhile code action. Mantis explains the by-design macOS choice.

## VERDICT 13409  Windows installer UAC elevation — MANUAL-VERIFICATION (Windows)
- **Actionable?** yes — NSIS installer change, manually verified on Windows
- **Where does the fix go?** gramps core Windows AIO installer (NSIS script), not Python
- **Branch target:** gramps core → maintenance/gramps61 (installer/packaging)
- **Root cause (one line):** after an elevated "install for all users" on Win11, the installer's "run Gramps now" launches with the ADMIN token, so trees land in the admin's %LOCALAPPDATA% and vanish for the normal user next launch (codefarmer note 10 confirms on Win10 too — not Win11-specific).
- **Does the reporter's workaround match the real root cause?** Yes — "don't offer to run immediately, or drop elevation first" is correct.
- **Fix sketch:** in the NSIS installer, drop elevation before the post-install launch (run de-elevated as the invoking user), or remove the run-immediately option when installed elevated for-all-users.
- **Repro on example.gramps?** N/A — Windows installer behavior; Linux can't confirm.
- **Test location & type:** none automatable on Linux; manual Windows verification.
- **Related issues / commits / upstream PRs to read first:** the AIO NSIS installer script; the Install Mode dialog (note 8).
- **Check upstream isn't already ahead:** check whether the gramps61 installer already de-elevates the post-install launch.
- **DISPOSITION:** MANUAL-VERIFICATION.md (Windows) with the install-elevated repro + both mantis comments. Fix is an installer-script change Eduard verifies on Windows.

## VERDICT 13667  Windows AIO beta2 Addon Manager module install — MANUAL-VERIFICATION (Windows)
- **Actionable?** maybe — confirm it still applies to a 6.0.x RELEASE first (beta2 is old)
- **Where does the fix go?** gramps core Windows AIO / Addon Manager — verify on Windows
- **Branch target:** gramps core → maintenance/gramps61
- **Root cause (one line):** Addon Manager module install issue reported on Windows AIO 6.0.0-beta2 — a stale pre-release; likely already fixed in the 6.0.x release line.
- **Does the reporter's workaround match the real root cause?** Undetermined — version is pre-release.
- **Fix sketch:** FIRST confirm it reproduces on a current 6.0.x Windows AIO; if not → already-fixed close. If it does → determine fix on Windows repro.
- **Repro on example.gramps?** Windows AIO only — not Linux-confirmable.
- **Test location & type:** none automatable here.
- **Related issues / commits / upstream PRs to read first:** Addon Manager changes since 6.0.0-beta2.
- **Check upstream isn't already ahead:** very likely — beta2 → release. Check first.
- **DISPOSITION:** MANUAL-VERIFICATION.md (Windows), but lead with the already-fixed check given the stale beta2 version.

## VERDICT 13260  Linux Mint can't load bsddb backend — repro-or-close (BSDDB drop)
- **Actionable?** yes — but almost certainly already-addressed / environmental
- **Where does the fix go?** gramps core (../gramps) for graceful-error; user's case is environmental
- **Branch target:** gramps core → maintenance/gramps61
- **Root cause (one line):** Gramps can't load the 'bsddb' backend because bsddb3 isn't available for the Python running Gramps (Flatpak dropped BSDDB as of 5.2 — Nick_H note 21); compounded by the user's tangled 4.2.8 + 5.2.2 / two-Python install (notes 13-19). Actionable core ask (note 22): don't raise a raw Exception when BSDDB is absent.
- **Does the reporter's workaround match the real root cause?** User self-resolved by converting to SQLite (note 23). Remaining item is the unhelpful hard exception.
- **Fix sketch:** core should degrade gracefully when the bsddb backend is unavailable (clear message + steer to SQLite), not raise "can't load database backend: 'bsddb'". Intersects the BSDDB-removal work (gramps PR #2198/#2202) — verify current gramps61 behavior first.
- **Repro on example.gramps?** partial — on a gramps61 build without bsddb3, attempt to open a bsddb-backed tree. The multi-install tangle isn't reproducible/isn't a Gramps bug.
- **Test location & type:** core unittest asserting a clean handled error (not raw Exception) when the bsddb backend plugin is missing.
- **Related issues / commits / upstream PRs to read first:** gramps PR #2198/#2202 (BSDDB drop); flatpak BSDDB discourse (note 21).
- **Check upstream isn't already ahead:** very likely — check gramps61 gen/db/utils.py make_database for current no-BSDDB behavior.
- **DISPOSITION:** read the full 23-note thread, then most likely confirm-and-close as already-addressed by the BSDDB drop (or environmental), OR a small graceful-message fix if gramps61 still raises the raw Exception.

## VERDICT 14051  DetailedDescendantBook AttributeError — repro-or-close (option-conditional)
- **Actionable?** yes — repro-or-close; tied to "omit duplicate ancestors" option
- **Where does the fix go?** addons-source (DetailedDescendantBook) — likely; verify vs core
- **Branch target:** addons-source → maintenance/gramps60
- **Root cause (one line):** AttributeError generating DetailedDescendantBook on a specific tree; reporter narrows it (notes 5-6, confused then corrected) to the "omit duplicate ancestors" option; works on example.gramps (note 3). Likely related to 0012857 (incomplete fix, note 4). Reporter on v1.1.34 still hit it (note 8).
- **Does the reporter's workaround match the real root cause?** Reporter's option-toggle finding is muddled (notes 5 then 6 reverse it) — trust the option as the trigger, verify direction on repro.
- **Fix sketch:** reproduce with "omit duplicate ancestors" enabled + "Include Index of Names" (note 4 settings) on a tree with duplicate ancestors; fix the AttributeError in the dedup/index path. Build a synthetic fixture with a pedigree collapse (duplicate ancestor) since example.gramps doesn't trigger it.
- **Repro on example.gramps?** No (note 3) — needs a tree with duplicate ancestors. Build a minimal fixture.
- **Test location & type:** addon unit test → addons-source/DetailedDescendantBook/tests/ with a duplicate-ancestor fixture + omit-duplicates option.
- **Related issues / commits / upstream PRs to read first:** **0012857** (note 4 — possibly incomplete prior fix); DetailedDescendantBook/DescendantBook v1.1.34.
- **Check upstream isn't already ahead:** check the addon's history re 12857; closed PRs.

## VERDICT 13589  Family Sheet extra page — repro-or-close (Linux render stack)
- **Actionable?** yes — repro-or-close; appears render-stack-specific
- **Where does the fix go?** addons-source (Family Sheet report) or core docgen — resolve by repro
- **Branch target:** addons-source → maintenance/gramps60 (verify; may be core docgen)
- **Root cause (one line):** a blank page is appended to the Family Sheet report PDF; reproduced by reporter + SNoiraud on Ubuntu 22.04 (notes 6-7) but NOT on Windows, NOT on Ubuntu 24.04 with current maintenance/gramps61 + example.gramps (note 11, five PID/recurse combos all clean). Strongly suggests an older Pango/cairo/poppler render-stack interaction, not a report-logic bug.
- **Does the reporter's workaround match the real root cause?** The "extra page" is real for them but tied to their rendering stack (Ubuntu 22.04 libs), not reproducible on current.
- **Fix sketch:** likely NOT a code fix — note 11's clean repro on 24.04/gramps61 points to already-resolved-by-newer-libs or environment. Confirm on current; if clean → can't-repro/already-resolved close.
- **Repro on example.gramps?** NOT on Ubuntu 24.04 + gramps61 (note 11). Only on the reporters' Ubuntu 22.04 stacks.
- **Test location & type:** if a real logic bug surfaces — report-level test; otherwise close.
- **Related issues / commits / upstream PRs to read first:** note 11's render-stack versions (libpango 1.52 vs reporters' older).
- **Check upstream isn't already ahead:** note 11 already shows current gramps61 doesn't reproduce.
- **DISPOSITION:** most likely can't-reproduce-on-current / environment (old render stack) close, citing note 11's clean test matrix; mantis documents the version split.
