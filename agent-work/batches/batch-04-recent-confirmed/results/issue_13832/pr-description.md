## Root cause
The GraphView DOT generator wrote Gramps handles as **unquoted** Graphviz node
ids: `add_node` emitted ` _<handle> [...]`, `add_link` emitted
` _<id1> -> _<id2>`, and `start_subgraph` emitted ` subgraph cluster_<handle>`.
Handles are arbitrary schema-valid strings (≤50 chars), and Gramps-Web creates
UUIDv4 handles containing hyphens (e.g. `22e6b2a0-269e-4c58-8e27-0c38b2ef5a10`).
Graphviz splits an unquoted id at the hyphen, so the node/edge/cluster name is
mangled, the DOT is malformed, and the Graph View renders blank (bug 13832).

## Fix
Quote the handle at the three DOT-id write sites (the leading `_`, needed
because Graphviz dislikes ids starting with a digit, stays inside the quotes):

```python
self.write('  "_%s" -> "_%s"' % (id1, id2))        # add_link
self.write(' "_%s" %s;\n' % (node_id, text))        # add_node
self.write('\n subgraph "cluster_%s"\n' % graph_id) # start_subgraph
```

A quoted subgraph name still beginning with `cluster` is recognised by Graphviz
as a cluster, so clustering is unaffected. This matches what core's own
`graphdoc.py` already does (it quotes and escapes node ids).

## Verified against
- `GraphView/graphview.py` — the three id-write sites (`add_link`, `add_node`,
  `start_subgraph`), and `start_subgraph(person_handle)` confirming the cluster
  name is handle-derived.
- `gramps/gen/plug/docgen/graphdoc.py:642,650` — core's quoted node-id writes,
  the pattern this aligns the addon with.

## Test
`GraphView/tests/test_graphview_dot_handles.py` asserts that a hyphenated
UUIDv4 handle, a plain handle, an edge's endpoints, and a cluster name are all
emitted quoted. Run in the Ubuntu CI image with graphviz/GooCanvas present, the
tests fail before this change (unquoted ids) and pass after. The import is
guarded so the suite skips cleanly where Gtk/GooCanvas/dot are unavailable.
