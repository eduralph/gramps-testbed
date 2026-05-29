# Issue 13832 — Gramps-Web UUIDv4 (hyphen) handles blank the Graph View

**Outcome: addon fix written (addons-source GraphView) + headless unittest,
verified fail-pre / pass-post in the Ubuntu Docker image.** Not pushed —
Eduard's review gate.

## Repo question RESOLVED — addon, not core (verdict was wrong)
The verdict said "gramps core — handle handling". Reproduction by code-reading
shows the defect is in the **GraphView addon**, not core:
- **Core is already correct.** `gramps/gen/plug/docgen/graphdoc.py:642,650`
  writes node ids as `"%s"` / `"%s" -> "%s"` with an `esc()` wrapper — quoted
  and escaped.
- **GraphView is the outlier.** `GraphView/graphview.py` emitted the handle as a
  **bare, unquoted** Graphviz id: `add_node` → `self.write(' _%s %s;\n' % …)`,
  `add_link` → `'  _%s -> _%s'`, `start_subgraph` → `'\n subgraph cluster_%s\n'`.

A Gramps-Web UUIDv4 handle (`22e6b2a0-269e-4c58-8e27-0c38b2ef5a10`) written
unquoted becomes `_22e6b2a0-269e-…`, which Graphviz parses as the id `_22e6b2a0`
followed by stray `-269e…` tokens — the DOT is malformed and the view blanks.
This is exactly note 16 (handle displayed as `_22e6b2a0`, truncated at the first
hyphen) and note 6 (deleting the hyphens made it render). dstraub note 19
prescribes the fix directly: "adding quotation marks around the handle fixed it"
(same issue solved in gramps-web's graphviz output). Note 10: the schema allows
any ≤50-char handle string, so the renderer must accept hyphens.

Distinct from bug 13830 (Graph View "path to home person" short-circuit) — that
is a different code path; this is purely handle-as-DOT-id quoting.

## Fix
Quote the handle at all three DOT-id write sites in
`GraphView/graphview.py` (the leading `_` — required because Graphviz dislikes
ids starting with a digit — is kept inside the quotes):

```python
add_link:       self.write('  "_%s" -> "_%s"' % (id1, id2))
add_node:       self.write(' "_%s" %s;\n' % (node_id, text))
start_subgraph: self.write('\n subgraph "cluster_%s"\n' % graph_id)
```

`start_subgraph` is called with a `person_handle` (`graphview.py:2941`); a quoted
name beginning with `cluster` is still recognised by Graphviz as a cluster
subgraph, so the clustering behaviour is unchanged. The `.gpr.py` version line is
deliberately **not** touched (maintainer manages versions centrally).

## Verified against
- `addons-source` `GraphView/graphview.py:3329,3399,3420` (post-fix) — the three
  id-write sites, now quoted.
- `GraphView/graphview.py:2941` — `start_subgraph(person_handle)` confirms the
  cluster name is handle-derived.
- `gramps/gen/plug/docgen/graphdoc.py:642,650` — core's quoted+escaped node-id
  writes, i.e. the correct pattern the addon was missing.
- Bug present identically on `upstream/maintenance/gramps60` and
  `maintenance/gramps61`.

## Test
New `GraphView/tests/test_graphview_dot_handles.py` (+ empty `tests/__init__.py`;
GraphView had no tests dir). Loaded as `GraphView.tests.…` (dotted path) by
`run-addon-unit.sh` / CI. It builds a `DotSvgGenerator` via `__new__` (bypassing
the GUI `__init__`; the DOT methods only need `self.dot`, plus
`self.current_list`/`self.colors` for `add_link`) and asserts the hyphenated and
plain handles, the edge endpoints, and the cluster name are all quoted. The
module import (Gtk/GooCanvas/`dot`) is guarded → `skipIf` on hosts without them.

**Verification (Ubuntu Docker image `gramps-testbed:ubuntu-6.1.0`, with
`graphviz` + GooCanvas-2.0 present, under `xvfb-run`):**
- Pre-fix: all 4 tests **FAIL** — e.g. `'"cluster_22e6b2a0-…"' not found in
  '\n subgraph cluster_22e6b2a0-269e-…'`, the exact malformed DOT.
- Post-fix: all 4 **pass**.
The default `run-addon-unit.sh` invocation currently aborts earlier on an
unrelated upstream `po/mn.po` msgfmt error (malformed catalog) and the stock
image lacks the `dot` binary; both are environment issues, not this change. The
test itself is correct and demonstrated failing-pre / passing-post above.

## Branch / status
- Target: addons-source → `maintenance/gramps60` (Gary cherry-picks to gramps61
  per PR 915). Code is identical on both branches.
- **Draft PR opened:** gramps-project/addons-source#928 (base
  `maintenance/gramps60`, head `eduralph:fix/bug-13832-graphview-handle-quote`).
  Left as DRAFT for Eduard's ready-mark. Patch applies cleanly on gramps60
  (byte-identical to the gramps61 code already verified fail-pre/pass-post in
  Docker). **Manual verify suggested:** load the reporter's example.gramps and
  confirm the Graph View renders the hyphenated-handle family (the stock CI
  image lacks the `dot` binary, so the addon test skips there).

## Files
- `patch.diff` — fix + test against the addons-source working tree
- `pr-description.md` — PR body in project format
- `mantis-comment.md` — tracker comment, Eduard's voice (cites the addons-source
  PR URL — fill in the PR number when the draft is opened)
