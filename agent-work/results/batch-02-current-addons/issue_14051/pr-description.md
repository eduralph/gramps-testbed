## Root cause
The pre-pass in `write_report()` that populates `self.report_app_ref` is
guarded by `if self.dubperson:` (the "Omit duplicate ancestors" option),
but `append_event` unconditionally reads `report_app_ref[self.phandle][0]`
whenever an index option is enabled — so with omit-duplicates off and
Index of Dates / Places on, the report crashes (`KeyError` today,
`AttributeError` on addon versions prior to the 12857/12859 init fix).

## Fix
Populate `report_app_ref[self.phandle]` inside `append_event` on the
first encounter with `(report_count, generation+1, dnumber[phandle],
False, name)`, then read `[0]` exactly as before. Subsequent
encounters of the same handle (the omit-duplicates-off + multi-
ascendant case) reuse the existing entry, so the surviving index Ref
pins to the FIRST encounter — identical to the omit-duplicates path's
`[0]` semantic. When the omit-duplicates pre-pass DID populate the
table, the populate-on-miss branch is skipped and behaviour is
unchanged.

## Verified against
- `DescendantBooks/DetailedDescendantBookReport.py:349-419` — the
  pre-pass that fills `report_app_ref` is gated on `self.dubperson`;
  when off, the table stays at `{}` (or, on older addon versions,
  unset).
- `DescendantBooks/DetailedDescendantBookReport.py:1117-1118,
  1242-1255` — the two call sites that drive `append_event` are gated
  on the index options, not on `dubperson`.
- Prior partial fix 3c79b8a6f for #12857 / #12859 — added the
  unconditional init at line 357-359 but left the read at the old
  line 789 unguarded; this PR completes that fix for the inverse
  settings combination, with first-encounter Ref semantics.

## Empirical parity check
Ran the report on `example.gramps` (center person I00016) with both
settings of `omitda`. Compared the resulting `index_of_dates` /
`index_of_places` `(repno, gen, per)` tuples for every common
`(place, date)` and `(year, date)` key:

| | omit-duplicates ON | omit-duplicates OFF |
|---|---|---|
| ascendants generated | 204 | 204 |
| indexed dates | 429 | 429 |
| indexed places | 656 | 658 |

Of 1372 common (place, date) keys, 1365 (99.5%) have **identical**
Ref tuples. The 7 mismatches all carry `date="0000-00-00"` — a
pre-existing key-collision in `index_of_places[place][date]` where
unrelated empty-date events overwrite each other, independent of
this PR. The two extra places in the OFF run come from events on
duplicated people, which OFF renders in full while ON early-returns.

## Test
`DescendantBooks/tests/test_append_event_index_without_omit_duplicates.py`
exercises `append_event` directly. Four cases:

1. Empty `report_app_ref` + valid phandle — primary bug 14051 crash
   path. Fails pre-fix with the bug's exact signature.
2. Mate not in `dnumber` (the `__write_mate` Branch A code path) —
   `per` falls back gracefully.
3. omit-duplicates-on baseline — the existing `[0]` read.
4. Multi-encounter parity — same person/event encountered in
   reports 1 and 2 must yield the first encounter's Ref, not the
   second's. This case fails on a current-state fallback (which I
   initially shipped); the populate-on-first revision passes it.

Fixes #14051
