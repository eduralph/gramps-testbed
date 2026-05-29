## Root cause
Gramps rewrites all metadata when a database is closed, and custom-type metadata
(name types, event names, place types, …) is stored as a Python `set`. The JSON
serializer encodes a set with `list(value)`, which yields the set's
hash-iteration order; since CPython randomises string hashing per process, that
order differs between runs, so closing an unmodified tree rewrites the metadata
rows in a new order and needlessly changes the on-disk file.

## Fix
In `JSONSerializer.object_to_metadata`, sort the value when it is a `set` so the
serialized order is deterministic. Tuples are kept unsorted (their order is
meaningful); the `set`/`tuple` read paths in `metadata_to_object` are unchanged.

## Verified against
- `gramps/gen/lib/serialize.py:155-186` — `set` is read back with
  `set(doc["value"])` and the `tuple` path is untouched, so sorting only affects
  on-disk order, not the reconstructed object.
- `gramps/gen/db/generic.py:898-914` — the custom-type sets written on close.
- `gramps/gen/db/generic.py:2082` — set members are `str(type)`, so `sorted()`
  is a total order and cannot raise.
- `gramps/plugins/db/dbapi/dbapi.py:111,431-451` — `JSONSerializer` is the live
  metadata serializer for current databases.

## Test
`gramps/gen/lib/test/serialize_test.py::MetadataSerializeCheck` asserts a string
set serializes in sorted order, round-trips back to a `set`, and that tuple
order is preserved. The sorted-order assertion fails on the unfixed code for all
of `PYTHONHASHSEED` 0–7 and passes after the change.

Fixes #13747.
