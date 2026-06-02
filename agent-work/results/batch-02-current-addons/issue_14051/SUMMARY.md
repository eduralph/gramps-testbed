# Issue 14051 — DetailedDescendantBookReport: index crash when omit-duplicates is off

## Root cause
`write_report()` only fills `self.report_app_ref` (the table
`append_event` reads via `report_app_ref[self.phandle][0]`) inside the
pre-pass guarded by `if self.dubperson:`. With "Omit duplicate
ancestors" UNSELECTED but Index of Dates / Places / Names enabled, the
pre-pass is skipped, yet `append_event` is still invoked for every
event from `write_person_info` / `__write_family_events`. The table is
either empty (current source, since the partial 12857/12859 fix at
3c79b8a6f added an unconditional init) or absent (older addon versions
the bug 14051 reporter is running) — KeyError or AttributeError.

This is an incomplete fix for prior bug 12857; the earlier patch
unconditionally initialised the three dicts but left the writing path's
unguarded read intact.

## Fix
Inside `append_event`, populate `report_app_ref[self.phandle]` on the
first encounter with `(report_count, generation+1, dnumber[phandle],
False, name)`, then read `[0]` exactly as the omit-duplicates path
does. Subsequent encounters of the same handle reuse the existing
entry, so the surviving index Ref pins to the FIRST encounter — the
same `[0]` semantic the omit-duplicates path emits. When the
omit-duplicates pre-pass DID populate the table, this populate-on-
miss branch is skipped, so that path is unchanged.

## Verified
**Semantic parity (empirical on example.gramps, center I00016).**
- Both modes produce identical date counts (429 / 429).
- omit-duplicates ON yields 656 indexed places; OFF yields 658
  (slightly higher because OFF doesn't early-return duplicates, so
  events on duplicated people are indexed too).
- 1365 / 1372 common `(place, date)` entries have **identical**
  `(repno, gen, per)` Ref tuples between the two modes.
- 7 mismatches all carry `date="0000-00-00"` — a pre-existing
  key-collision in `index_of_places[place][date]` where unrelated
  empty-date events overwrite each other. Independent of this fix.
- Drove via `/tmp/ddb_compare.py` (bootstraps config + custom
  filters + import_as_dict, runs `write_report` twice with a
  null doc, diffs `index_of_*` Ref tuples).

**Unit tests (`DescendantBooks/tests/test_append_event_index_without_omit_duplicates.py`).**

Two classes, four cases — all run via the testbed addon runner
(`./scripts/ubuntu/run-addon-unit.sh DescendantBooks` → PASS, 4
tests):

1. `test_append_event_does_not_crash_without_prepopulated_table` —
   empty `report_app_ref` + valid phandle → must not raise; the
   index Ref uses first-encounter coords.
2. `test_append_event_for_mate_without_dnumber` — phandle is a mate
   not in `dnumber` (the `__write_mate` Branch A path) → must not
   raise; `per` falls back to "?".
3. `test_dubperson_on_baseline_ref_is_first_encounter` — baseline
   that locks the existing omit-duplicates path's `[0]` semantic.
4. `test_dubperson_off_multi_encounter_matches_first_encounter` —
   simulates the same person/event encountered in reports 1 and 2;
   asserts the surviving index Ref is the first encounter's tuple,
   not the second's. **Fails on the original "use current state"
   fallback** (got `Ref: 2 4 5`, expected `Ref: 1 2 3`); passes on
   the populate-on-first revision.

## Note on the verdict's secondary symptom
Note 12 in the tracker reports "Index of Places page comes out blank"
with the omit-duplicates-ON workaround. In the empirical run that
symptom did NOT reproduce on example.gramps: omit-duplicates ON
yielded 656 indexed places, omit-duplicates OFF (with this fix)
yielded 658. The fix does not depend on or worsen the symptom — if
anything, OFF now produces a more comprehensive index. The blank-
places symptom remains a separate ticket per CLAUDE.md "one issue per
ticket".

## Repo and branch
- Repo: `addons-source` (in-tree addon `DescendantBooks/`)
- Branch: `fix/bug-14051-detaileddescendantbook-report-app-ref` based
  on `upstream/maintenance/gramps61`
- Commits:
  - `aeeca4470 DetailedDescendantBookReport: fix index crash when
    omit-duplicates is off` (initial fallback)
  - `9318da90a DetailedDescendantBookReport: pin Ref to first
    encounter, not current` (semantic refinement after empirical
    comparison)

## Notes for review
- Addon version not bumped per
  [[feedback_addons_source_no_version_bump]].
- Two commits on the branch; Eduard can squash on merge if preferred.
