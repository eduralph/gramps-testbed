Confirmed and fixed. The diagnosis here and in note 3 is correct: custom-type
metadata (name types, event names, etc.) is stored as a Python set, and the JSON
serializer wrote it out with list(value). That gives the set's hash-iteration
order, which CPython randomises per process, so every close re-wrote the
metadata rows in a different order even when nothing was edited. The .gramps
export is unaffected because it sorts these on the way out.

The fix sorts the set before serializing it (note 4's suggestion), so the
on-disk metadata is now byte-stable across saves. Tuple-valued metadata is left
untouched, since its order is meaningful.

This addresses only the non-reproducible serialization. The separate
read/write-vs-read-only export-mode point raised in note 2 is tracked under
0013748 and is not changed here.

A regression test was added in gramps/gen/lib/test/serialize_test.py asserting
that set metadata serializes in a stable, sorted order.

Fixed in PR p:gramps:2340: on the maintenance/gramps61 branch.

Fixed in version: 6.1.0.
