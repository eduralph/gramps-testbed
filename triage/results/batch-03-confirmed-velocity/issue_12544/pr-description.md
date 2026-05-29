## Root cause
`OsmPointStyle` reads the place-marker label as
`feature.values_.name`. `values_` is OpenLayers' **private**
property-store attribute on `ol.Feature`; the documented public-API
reader is `feature.get(<key>)`. The existing OsmClick handler in the
same file already uses `feature.get('name')` for the same property, so
the OsmPointStyle site is the lone outlier and a latent break the next
time OL renames or restructures the private store.

## Fix
Replace `feature.values_.name` with `feature.get('name')` in
`OsmPointStyle`. Behaviour is unchanged for the current OL version,
but the call now goes through the supported reader. Add a short
comment pointing at the public-API contract so the next person to
touch this block doesn't reintroduce the private-attribute access.

## Verified against
- `DynamicWeb/templates/dwr_default/data/dwr.js` (around the
  OsmPointStyle name-lookup line) — site of the change.
- `DynamicWeb/templates/dwr_default/data/dwr.js` (around the OsmClick
  handler) — pre-existing `feature.get('name')` call on the same
  property, used as the in-file precedent.

## Test
No regression test ships with this PR. The code path is browser-
rendered OpenLayers JavaScript; addons-source has no headless-browser
runner and the testbed's Linux-only AT-SPI suite does not cover web
output. Manual verification on a generated DynamicWeb site is the
practical check; the steps and acceptance criteria are captured in the
PR description below.

**Manual repro:**
1. Generate a DynamicWeb report (`Reports → DynamicWeb Report`) from
   `example.gramps` against a tree with placed people (so the map view
   has at least two markers with `name` properties).
2. Open the generated `index.html` in a browser; navigate to a page
   with the OpenLayers map (place index or person view).
3. Hover each marker — the tooltip label must show the place's name.
   Click the marker — the popup must show the same name. Both come
   from the OsmPointStyle code path the patch touches.
4. Browser console must be free of OL errors and undefined-property
   warnings around `values_` or `feature.get`.

Fixes #12544
