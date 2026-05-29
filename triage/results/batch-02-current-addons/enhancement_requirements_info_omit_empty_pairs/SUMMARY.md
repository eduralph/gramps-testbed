# Enhancement — `Requirements.info` omits empty `(label, table)` pairs

## Frame
**Enhancement / contract-hardening PR**, not a bug-fix PR. Drives off
`BRIEF_requirements_info_enhancement.md` in this batch directory.

The user-visible crash (Mantis 13979 IndexError in Plugin Manager
Enhanced) is already resolved addon-side in addons-source PR 916.
This PR is the complementary producer-side cleanup: tighten the
`Requirements.info` contract so no consumer ever sees
`(label, empty-table)` again. The remaining live improvement is
that gramps core's own Addon Manager Requirements dialog stops
rendering empty labelled sections.

**Not filing a separate Mantis** per the brief — the PR is the
report and the fix in one. Reference 13979 in the PR description
as origin context only; don't auto-close it (that's PR 916's job).

## Behaviour table (re-confirmed on `upstream/maintenance/gramps61` HEAD)

| input addon dict                                                  | before                                                                                                    | after                                              |
|-------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|----------------------------------------------------|
| `{}`                                                              | `[]`                                                                                                      | `[]` (unchanged)                                   |
| `{"re": []}`                                                      | `["Executables", []]`                                                                                     | `[]`                                               |
| `{"rm": []}`                                                      | `["Python modules", []]`                                                                                  | `[]`                                               |
| `{"rg": []}`                                                      | `["GObject introspection modules", []]`                                                                   | `[]`                                               |
| `{"rm": ["psycopg"], "re": []}` (live PostgreSQL Enhanced shape)  | `["Python modules", [["psycopg", "❌"]], "Executables", []]`                                              | `["Python modules", [["psycopg", "❌"]]]`         |
| `{"rm": [], "rg": [], "re": []}`                                  | `["Python modules", [], "GObject introspection modules", [], "Executables", []]`                          | `[]`                                               |
| `{"rm": ["psycopg", "Pillow"]}` (positive case)                   | `["Python modules", [["psycopg", "❌"], ["Pillow", "❌"]]]`                                               | identical — populated sections unchanged           |
| `{"rm": ["psycopg"], "re": ["dot"]}` (positive case)              | `["Python modules", [["psycopg", "❌"]], "Executables", [["dot", "❌"]]]`                                 | identical — rm/rg/re order preserved               |

## The change
[`gramps/gen/utils/requirements.py:146-172`](../../../../../gramps/gramps/gen/utils/requirements.py#L146):
build each section's `table` first, then append BOTH label and
table only when the table has entries. Same shape applied uniformly
to all three sections (`rm` / `rg` / `re`).

Behaviour for any non-empty key is preserved exactly: same labels,
same table contents, same `rm` → `rg` → `re` ordering.

## Blast radius — consumers grep result

Searched `gramps/` for `Requirements()` and `Requirements.info(`:

| call site                                                                             | call               | impact                                                                                                                                |
|---------------------------------------------------------------------------------------|--------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| [`gramps/gui/plug/_windows.py:349`](../../../../../gramps/gramps/gui/plug/_windows.py#L349) | `self.req.info(addon)` → `InfoDialog` | **Improved** — the live empty-section UX nit goes away. The "Executables" empty section after a populated "Python modules" no longer appears. |
| [`gramps/gen/plug/_pluginreg.py:1373`](../../../../../gramps/gramps/gen/plug/_pluginreg.py#L1373) | `Requirements()` instantiation only | Unchanged — only `check_plugin` is called here, not `info()`. |

Single out-of-tree consumer in the addons-source repo:

| call site                                                                                                                                                                       | call                          | impact                                                                                                                                                       |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `PluginManager/PluginManager.py:651` (addons-source)                                                                                                                            | `Requirements().info(addon)`  | **Belt-and-suspenders** — the addon already guards empty tables via PR 916; this change also fixes the upstream shape so any future consumer is protected.   |

No other consumer of `Requirements.info` exists in either repo. The
PR description names both consumers + asks reviewers to confirm no
unlisted caller relies on the empty-pair shape.

## Test
[`gramps/gen/utils/test/requirements_test.py`](../../../../../gramps/gramps/gen/utils/test/requirements_test.py)
(new). 8 `unittest.TestCase` methods:

1. `test_no_requires_keys` — `{}` → `[]`.
2. `test_present_but_empty_re_omits_pair`
3. `test_present_but_empty_rm_omits_pair`
4. `test_present_but_empty_rg_omits_pair`
5. `test_all_three_present_but_empty_omits_all_pairs`
6. `test_postgresql_enhanced_listing_shape` — the live trigger.
7. `test_non_empty_rm_still_renders` (positive — guards against over-suppression).
8. `test_non_empty_rm_and_re_both_render_in_order` (positive — locks ordering).

Mutation check (revert the fix) → 5 of 8 fail with `["Python
modules", []] != []` shape; the 3 positive cases continue to pass.
With the fix → all 8 pass.

Headless — runs under plain `GRAMPS_RESOURCES=. python3 -m unittest
gramps.gen.utils.test.requirements_test` (no display, no `xvfb-run`
needed — this is gen/ code).

## CI sanity
- `black --check` clean on both files.
- Targeted test path: `gramps.gen.utils.test.requirements_test` →
  PASS (8 tests in 0.000s).
- Sibling sweep `gramps.gen.utils.test.{alive,callback,file,grampslocale,keyword,place,requirements}_test` →
  PASS (90 tests cumulative).
- Full project unit suite `python3 -m unittest discover -p "*_test.py"`
  → 32578 tests in 216.6s, 7 failures, 56 skipped. The 7 failures
  are all in `gramps/plugins/test/imports_test.py` (5 cases) and
  `gramps/plugins/test/reports_test.py` (2 cases). Neither file
  references `Requirements`; the failures are pre-existing on
  `upstream/maintenance/gramps61` and unrelated to this change.

## Repo and branch
- Repo: `gramps` (gramps core)
- Branch: `enhancement/requirements-info-omit-empty-pairs` based on
  `upstream/maintenance/gramps61`
- Commit: `0daf9b22b7 Requirements.info: omit empty (label, table)
  pairs.`

## Notes for review
- Enhancement-framed, not bug-fix-framed. No `Fixes #` trailer.
  13979 referenced only as context.
- Two complementary fixes (this + addons-source PR 916) coexist by
  design: the addon defensive guard ships to users on the addon
  release cadence; this core hardening ships on the gramps release
  cadence.
- Per the brief, no separate Mantis filed for this — the PR is
  the report.
