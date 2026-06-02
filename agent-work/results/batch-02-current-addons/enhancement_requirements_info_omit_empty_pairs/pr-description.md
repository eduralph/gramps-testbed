## What this changes
`Requirements.info` previously appended a label whenever an addon
dict carried a `"rm"` / `"rg"` / `"re"` key, regardless of whether
the value was a non-empty list. A present-but-empty key — e.g. an
addon listing with `"re": []` because its `.gpr.py` declares
`requires_exe=[]` — produced a labelled section paired with an
empty table.

The live user-visible effect is in gramps core's own AddonManager:
the "Requirements" InfoDialog
([`_windows.py:349`](gramps/gui/plug/_windows.py#L349)) renders an
empty labelled section for every present-but-empty requires key.
The PostgreSQL Enhanced listing surfaces this today — clicking
Requires shows an empty "Executables" section after the real
"Python modules" section.

## Verified behaviour change

| input addon dict                                                  | before                                                                                                    | after                                              |
|-------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|----------------------------------------------------|
| `{}`                                                              | `[]`                                                                                                      | `[]` (unchanged)                                   |
| `{"re": []}`                                                      | `["Executables", []]`                                                                                     | `[]`                                               |
| `{"rm": []}`                                                      | `["Python modules", []]`                                                                                  | `[]`                                               |
| `{"rg": []}`                                                      | `["GObject introspection modules", []]`                                                                   | `[]`                                               |
| `{"rm": ["psycopg"], "re": []}` (live PostgreSQL Enhanced shape)  | `["Python modules", [["psycopg", "❌"]], "Executables", []]`                                              | `["Python modules", [["psycopg", "❌"]]]`         |
| `{"rm": [], "rg": [], "re": []}`                                  | `["Python modules", [], "GObject introspection modules", [], "Executables", []]`                          | `[]`                                               |
| `{"rm": ["psycopg", "Pillow"]}`                                   | `["Python modules", [["psycopg", "❌"], ["Pillow", "❌"]]]`                                               | identical — populated sections unchanged           |
| `{"rm": ["psycopg"], "re": ["dot"]}`                              | `["Python modules", [["psycopg", "❌"]], "Executables", [["dot", "❌"]]]`                                 | identical — rm / rg / re order preserved           |

The change is uniform across all three sections (`rm` / `rg` /
`re`): build the section's table first, then append BOTH label and
table only if the table has entries. Behaviour for any non-empty
key is preserved exactly.

## Context — Mantis 13979 (already fixed elsewhere)
The same empty-pair shape was also the trigger for the IndexError
crash reported in Mantis 13979 against the Plugin Manager Enhanced
addon: its row-click handler does `txt = " ".join(req_lst[0])` and
indexes an empty list. That crash is resolved in addons-source PR
916 with a defensive guard at the consumer.

This core-side change is **complementary, not a substitute**: the
two fixes ship on independent release cadences (the addon update
reaches users separately from a gramps point release), and the
upstream contract hardening protects any future caller of
`Requirements.info`. 13979 is not being closed here — it is closed
by PR 916 once that merges and ships.

## Blast radius
`Requirements.info` is a public-ish API; tightening it is a
contract change. Reviewers should confirm no unlisted consumer
relies on receiving a label-without-rows pair. Known consumers,
both surveyed:

1. **gramps core** —
   [`EnhancedAddonStatus.__on_requires_clicked`](gramps/gui/plug/_windows.py#L345)
   passes the list straight to `InfoDialog`. The empty labelled
   section no longer renders — this is the visible improvement.
2. **addons-source — `PluginManager` Enhanced addon** —
   `PluginStatus.__info` iterates the list. With the addon-side
   PR 916 fix, the addon already guards empty tables; this change
   also fixes the producer so the guard becomes defence-in-depth
   rather than load-bearing.

`gramps/gen/plug/_pluginreg.py:1373` instantiates `Requirements()`
but only calls `check_plugin`, never `info`, so it is unaffected.

## Test
[`gramps/gen/utils/test/requirements_test.py`](gramps/gen/utils/test/requirements_test.py)
ships in this PR. 8 `unittest.TestCase` methods cover:

- All six pre-change shapes from the verified-behaviour table —
  asserts none of them now emits an empty pair.
- A positive case for non-empty `rm` (populated label + table
  preserved).
- A positive case for non-empty `rm` + non-empty `re` (order
  preserved as well).

The 5 empty-section tests fail on the pre-change file; the 3
positive tests continue to pass. With the change, all 8 pass.

Headless — runs under plain `python3 -m unittest`, no display,
matching the AGENTS.md command:

```
GRAMPS_RESOURCES=. python3 -m unittest gramps.gen.utils.test.requirements_test
```
