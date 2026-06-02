PR open against addons-source `maintenance/gramps60`:
https://github.com/gramps-project/addons-source/pull/NNN — replaces
`feature.values_.name` with the documented `feature.get('name')` in
the DynamicWeb OsmPointStyle marker code path. Aligns with the
existing `feature.get('name')` usage already present in the OsmClick
handler in the same file; no behaviour change for current OpenLayers
versions but removes the private-attribute reach that would break on
an OL upgrade.

No automated regression test — the code is browser-rendered JS that
addons-source CI does not exercise. The PR description includes a
manual repro against `example.gramps`.
