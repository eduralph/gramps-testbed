# Mantis 12544 — DynamicWeb OsmPointStyle reads OL feature internal state

## Verdict
**FIX SHIPPED** — replace `feature.values_.name` (a reference to the
private OpenLayers feature-property store) with the documented
`feature.get('name')`. Same value, supported API, won't break on the
next OL upgrade. Aligns with the existing `feature.get('name')` usage
already present in the OsmClick handler in the same file.

## Branch + PR
- **fork branch:** `eduralph/addons-source:fix/bug-12544-dwr-osmpointstyle-feature-get`
- **target:** `gramps-project/addons-source:maintenance/gramps60`
- **status:** PR **addons-source#925** opened, marked ready, and **verified** (browser sign-off 2026-05-29 — see MANUAL-VERIFICATION.md "Result"). Awaiting upstream merge.

## Files
- `DynamicWeb/templates/dwr_default/data/dwr.js` — single-line change
  at the OsmPointStyle name-lookup site, plus a short comment block
  pointing at the OL public-API contract.

## Test
No automated test ships with the patch — the affected code is browser-
rendered JavaScript, not Python; the testbed has no headless-browser
runner. **See MANUAL-VERIFICATION.md** for the exact repro steps.

## Manual work
**YES.** This is a JS / OpenLayers map-view change; correctness has to
be confirmed in an actual browser session against a generated
DynamicWeb site. Steps and acceptance criteria are in
`MANUAL-VERIFICATION.md` in this directory.
