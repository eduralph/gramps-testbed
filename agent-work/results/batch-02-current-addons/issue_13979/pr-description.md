## Root cause
`PluginStatus.__info` iterates `Requirements().info(addon)` output as
`[label, table]` pairs and joins the first row with
`txt = " ".join(req_lst[0])`. gramps core's `Requirements.info` still
emits a label + empty table when the addon listing carries a
present-but-empty requires key — e.g. PostgreSQL Enhanced declares
`requires_exe=[]` in its `.gpr.py`, which lands in `addons-en.json`
as `"re": []`. Indexing `req_lst[0]` on the empty table raises
`IndexError: list index out of range`, crashing the row click.

A scan of the live `addons/gramps61/listings/addons-en.json` confirms
PostgreSQL Enhanced is the only addon currently shipping with a
present-but-empty requires key — which exactly matches the reported
"only the PostgreSQL Enhanced row crashes" symptom.

## Fix
Skip the iteration when `req_lst` is empty. Indexing it would fail,
and there is nothing meaningful to render for an empty requires
list.

## Verified against
- `PluginManager/PluginManager.py:650-660` — the
  installed-plugins branch where the bug lives. The traceback line
  numbers in the report (580 → 655) match this site.
- `gramps/gen/utils/requirements.py:146-172` (`maintenance/gramps61`)
  — the upstream `Requirements.info` that emits the label + empty
  table for any `"rm"`/`"rg"`/`"re"` key present in the addon dict,
  even when the value is `[]`. A cleaner contract would be "only
  emit pairs with at least one entry"; that is a separate gramps-core
  cleanup, not bundled here per the one-PR-per-bug rule.
- `addons-source/PostgreSQLEnhanced/postgresqlenhanced.gpr.py:47`
  — `requires_exe=[],  # No external executables required`. Source
  of the `"re": []` field in the listing.
- `addons/gramps61/listings/addons-en.json` — confirmed PostgreSQL
  Enhanced is the only addon with a present-but-empty requires key,
  matching the reported "only this row" symptom.

## Test
`PluginManager/tests/test_info_empty_requires.py` builds a
`PluginStatus` via `__new__`-bypass (no Gtk-heavy `__init__`), stubs
the Gtk-text-buffer / plugin-manager / plugin-registry attributes,
then calls the name-mangled `_PluginStatus__info("postgresqlenhanced")`
against an addon dict matching the live listing entry
(`"rm": ["psycopg"]`, `"re": []`). Two assertions:

1. No `IndexError` is raised.
2. The non-empty Python modules entry is still rendered while the
   empty Executables entry is skipped — verifies the `continue` only
   skips empty tables, not all requirements.

Pre-fix the test fails with the reported traceback (`txt = " ".join(
req_lst[0]) / IndexError: list index out of range`); post-fix it
passes.

The test class is gated on `_has_gtk_display()` — `PluginManager.py`
imports Gtk at module load, so the test skips cleanly in
display-less CI environments. Under `xvfb-run` (e.g. the testbed's
addon-unit runner with a display, or a developer's desktop) both
assertions run.

```
xvfb-run -a python3 -m unittest PluginManager.tests.test_info_empty_requires -v
```

Resolves #13979
