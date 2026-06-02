# Mantis 13830 — draft note (Eduard to paste, then mark Fixed in version 6.0.4)

(Bare bug numbers per the no-`#`-prefix convention; PR linked with `p:gramps:` for gramps core.)

---

Triage finding: this is already fixed upstream — no code change is needed beyond the maintainer setting Fixed in version.

Root cause is in gramps core, not in the GraphView addon. `gramps/gen/filters/rules/person/_relationshippathbetween.py` — `init_list` had

```
for person_handle in firstList and secondList:
    new_rank = firstMap[person_handle]
```

Python evaluates `firstList and secondList` as `secondList` via short-circuit `and`, so the loop iterated over the second root's ancestors and read `firstMap[person_handle]` — which only contains the first root's ancestors. KeyError fires on the first handle reachable from the second root but not the first. Graph View's "Show path to home person" hits this every time the active person and the home person do not share an entire ancestor set, which is almost always.

Regression introduced by commit 1280aa45a5f47581badfb655021ce1d430f8a581 ("Refactor, fix, and optimize filters/rules", 2025-02-03). Fixed by commit 48a6cbfb0541d429a3e3fba778c611f6e1843a6a ("Fix regression in relationship path between people filter", landed 2025-08-09) on master and forward-merged to maintenance/gramps60 and maintenance/gramps61. Shipped in releases 6.0.4, 6.0.5, 6.0.6, 6.0.7, 6.0.8, and 6.1.0-beta1.

The reporter's workaround (deleting GraphView ini settings that held uppercase `interface.graphview-show-id` keys, blamed on commit 6357efb) was a red herring — current `maintenance/gramps61` uses the lowercase key throughout `GraphView/graphview.py` (lines 155, 193, 674, 754, 2383), and the traceback terminates inside core, not in addon code.

The fix shipped without a direct test for `RelationshipPathBetween` (only the `RelationshipPathBetweenBookmarks` wrapper had coverage). Filed p:gramps:2329: to add a regression test that fails on the pre-fix file with KeyError at `_relationshippathbetween.py:130` (same line and exception class as the original traceback above) and passes on current `maintenance/gramps61`.

Suggested tracker action: set Fixed in version to 6.0.4 on the Gramps 6.0 project and resolve.
