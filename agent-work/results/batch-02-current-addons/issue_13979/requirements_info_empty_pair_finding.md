# `Requirements.info` emits empty (label, table) pairs — verified

## Claim being checked
PR 916's SUMMARY and the verdict for 13979 both say the underlying
shape that triggers the IndexError is gramps core's
`Requirements.info` returning a label paired with an empty table
whenever the addon listing has a present-but-empty requires key —
e.g. `"re": []`. That claim was made from a code read; this note
verifies it empirically before the claim ships in the PR description
or moves into any follow-up Mantis filing.

## Source under test
[`gramps/gen/utils/requirements.py:146-172`](../../../../gramps/gramps/gen/utils/requirements.py#L146)
(`maintenance/gramps61`):

```python
def info(self, addon):
    info = []
    if "rm" in addon:
        info.append(_("Python modules"))
        table = []
        for module in addon.get("rm"):
            result = self.check_mod(module)
            table.append([module, tick_cross(result)])
        info.append(table)
    if "rg" in addon:
        ...
    if "re" in addon:
        ...
    return info
```

Two readings are possible:
1. The label and table are appended unconditionally if the key is
   present — even when the value is `[]` — and the empty table
   propagates downstream.
2. The loop body short-circuits empty values via some guard that an
   earlier read missed.

Whichever is right matters for the PR description's accuracy and for
deciding whether a separate gramps-core PR is needed.

## Method
Inside the testbed docker image (Ubuntu 24.04, gramps
`maintenance/gramps61` HEAD), construct synthetic addon dicts and
call `Requirements().info(addon)`. Six shapes covering: no requires
keys, each requires key present-but-empty individually, the live
PostgreSQL Enhanced listing shape, and all three keys present-but-
empty together.

## Results

| input addon dict                                                   | `Requirements.info` returned                                                                          | empty pair? |
|--------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|-------------|
| `{}` (no requires keys)                                            | `[]`                                                                                                  | no          |
| `{"re": []}`                                                       | `["Executables", []]`                                                                                 | **yes**     |
| `{"rm": []}`                                                       | `["Python modules", []]`                                                                              | **yes**     |
| `{"rg": []}`                                                       | `["GObject introspection modules", []]`                                                               | **yes**     |
| `{"rm": ["psycopg"], "re": []}` (live PostgreSQL Enhanced shape)   | `["Python modules", [["psycopg", "❌"]], "Executables", []]`                                          | **yes**     |
| `{"rm": [], "rg": [], "re": []}`                                   | `["Python modules", [], "GObject introspection modules", [], "Executables", []]`                      | **yes**     |

## Verdict
Reading (1) is correct. The guard at lines 151 / 158 / 165 is
`if "rm" in addon:` — key presence, not value truthiness. So `"re":
[]` is enough to produce `["Executables", []]`, and the PostgreSQL
Enhanced listing shape produces exactly the pair that crashes
`PluginStatus.__info` at `req_lst[0]`.

## Implications
- The PR 916 description and SUMMARY are accurate — leave them as-is.
- The "follow-up note" in PR 916 stands: a separate gramps-core PR
  could tighten `Requirements.info` so it never emits a pair without
  entries. The fix in core would mirror the addon-side fix: append
  the label only after confirming the table is non-empty:

  ```python
  if "rm" in addon:
      table = []
      for module in addon.get("rm"):
          result = self.check_mod(module)
          table.append([module, tick_cross(result)])
      if table:
          info.append(_("Python modules"))
          info.append(table)
  # ditto for rg, re
  ```

- That core fix would be a defensive improvement, NOT a substitute
  for PR 916. Two reasons to ship both:
  1. Users on 6.1.x get the addon fix as soon as the addon update
     ships, independent of the gramps release cadence.
  2. The addon defensive guard protects against any other producer
     of label + empty table pairs (today only `Requirements.info`,
     but future callers could trip the same).

- gramps core's own consumer of `Requirements.info` is
  `EnhancedAddonStatus.__on_requires_clicked` at
  [`_windows.py:345-349`](../../../../gramps/gramps/gui/plug/_windows.py#L345),
  which passes the list straight to `InfoDialog`. `InfoDialog`
  doesn't crash on the empty-table shape, but it does **render an
  empty section** with a label and no rows — also a UX nit that a
  core fix would resolve.

## Repo and branch
No code change in this artefact. The eventual gramps-core fix would
target `maintenance/gramps61`. File a separate Mantis if/when you
want to track it; for now, this is documentation only.
