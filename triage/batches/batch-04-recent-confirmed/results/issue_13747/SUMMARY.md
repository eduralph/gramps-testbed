# Issue 13747 — saving an unmodified DB changes the DB on disk

**Outcome: core fix written (gramps `maintenance/gramps61`) + regression test.**
Not pushed — Eduard's review gate.

## Root cause
Gramps always rewrites its metadata when a database is closed. Custom-type
metadata (`name_types`, `event_names`, `place_types`, …) is held as a Python
`set`. The JSON serializer encodes a set with
`gramps/gen/lib/serialize.py:JSONSerializer.object_to_metadata` via
`value = list(value)`. `list(set)` yields the set's *hash-iteration* order,
and because CPython randomises string hashing per process (`PYTHONHASHSEED`),
that order changes between runs. So closing an otherwise-unmodified tree
rewrites the `name_types` (etc.) metadata rows in a different order — exactly
the `{"value":["Test","Test2"]}` ↔ `{"value":["Test2","Test"]}` flip in the
reporter's SQL dump.

The reporter's diagnosis (description) and maintainer prculley's note 3 ("sets
are unordered … metadata is always saved on close") are both correct. note 4
(umlaeute) proposed the fix: "just do an alphabetic sort of the set data before
storing it."

## Fix
`gramps/gen/lib/serialize.py` — in `JSONSerializer.object_to_metadata`, sort the
value when it is a `set` so the serialized order is deterministic:

```python
if type_name == "set":
    value = sorted(value)
elif type_name == "tuple":
    value = list(value)
```

Tuples are split out and **not** sorted — tuple order is meaningful (e.g.
`name_formats`), and `metadata_to_object` reconstructs `tuple(doc["value"])`.
The set round-trip is unchanged: `metadata_to_object` still does
`set(doc["value"])`.

The metadata sets in question contain only `str(...)` values (built from
`str(type)` of custom Gramps types — see `generic.py:2082` and siblings), so
`sorted()` is total and cannot raise.

### Scope — JSON path only (deliberate)
The active serializer for current 6.x databases is `JSONSerializer`
(`use_json_data()` returns True once the `json_data` column exists). The
reporter's dump confirms it: the **json_data** column flipped while the legacy
blob column held a constant empty-set pickle. `BlobSerializer.object_to_metadata`
(`pickle.dumps(value)`) has the same theoretical instability, but: (a) it is the
deprecated path being phased out, (b) it is not what the reporter hit, and (c) a
correct blob fix would have to pickle a sorted *list* and convert back to a set
on read — a format change with its own round-trip risk. Per the verdict ("SCOPE:
ordering only", one logical fix) the blob path is left out and noted here.

## Verified against
- `maintenance/gramps61` `gramps/gen/lib/serialize.py:155-186` — `set` →
  `set(doc["value"])` on read, sorted list on write; `tuple` path unchanged.
- `gramps/gen/db/generic.py:898-914` — the metadata sets serialized on close.
- `gramps/gen/db/generic.py:2082` etc. — set members are `str(type)`, so total
  ordering holds.
- `gramps/plugins/db/dbapi/dbapi.py:431-451` (`_set_metadata`) and `:111`
  (`use_json_data`) — the JSON serializer is the live metadata path.

## Test
`gramps/gen/lib/test/serialize_test.py` → new `MetadataSerializeCheck`:
- `test_set_is_serialized_in_sorted_order` — the regression guard: a 7-element
  string set serializes with `value == sorted(names)`.
- `test_set_round_trips_to_set` — `set` → JSON → `set` is preserved.
- `test_tuple_order_is_preserved` — guards against the sort leaking onto tuples.

Pre-fix the guard test fails on **8/8** `PYTHONHASHSEED` values 0–7 (the unfixed
`list(set)` order matched `sorted()` on none of them); post-fix it passes, and
`object_to_metadata` output is byte-identical across hash seeds 0–5. Full
`serialize_test` suite: 20995 tests OK. `black --check` clean; `mypy` clean.

## Branch / status
- Target: gramps core → `maintenance/gramps61` (per verdict).
- Not bundled with 13748 (read-only export mode) — separate ticket, per note 2
  and the verdict.
- **Draft PR opened:** gramps-project/gramps#2340 (base `maintenance/gramps61`,
  head `eduralph:fix/bug-13747-metadata-set-order`). Left as DRAFT for Eduard's
  ready-mark. Verified on the gramps61 branch: test passes, black + mypy clean.

## Files
- `patch.diff` — the change against gramps working tree
- `pr-description.md` — PR body in the project format
- `mantis-comment.md` — tracker comment, Eduard's voice (cites `p:gramps:NNNN:`
  — fill in the PR number when the draft is opened)
