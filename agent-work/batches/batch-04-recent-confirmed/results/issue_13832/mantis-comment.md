Confirmed, and it is the Graph View addon, not Gramps core or Gramps Web. The
addon writes each handle into the Graphviz/DOT graph as an unquoted node id
(add_node, add_link and the subgraph/cluster name). Handles are allowed to be
any string up to 50 characters, and the handles Gramps Web creates are UUIDv4s
containing hyphens, e.g. 22e6b2a0-269e-4c58-8e27-0c38b2ef5a10. Graphviz splits an
unquoted id at the first hyphen, so the id becomes "_22e6b2a0" plus leftover
tokens, the DOT is malformed, and the view goes blank. That matches what was
seen here: the node showed as "_22e6b2a0" (note 16), and removing the hyphens
made it render (note 6). The core Graphviz reports already quote their node ids,
which is why they are unaffected; this is exactly the same quoting fix
@DavidMStraub mentioned in note 19.

Fix: quote the handle at the three places the addon emits it as a DOT id, so a
hyphenated handle is treated as a single id. A quoted subgraph name beginning
with "cluster" is still treated as a cluster by Graphviz, so the grouping is
unchanged. A regression test was added under GraphView/tests/ that checks a
hyphenated handle is quoted in the node, edge and cluster output.

This is separate from the "show path to home person" problem in 0013830, which
is a different code path.

The fix targets the addons-source maintenance/gramps60 branch (cherry-picked to
gramps61):

https://github.com/gramps-project/addons-source/pull/928
