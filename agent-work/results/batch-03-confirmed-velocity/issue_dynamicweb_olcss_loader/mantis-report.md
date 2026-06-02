# Mantis bug report — DynamicWeb: ol.css loaded as JavaScript

Draft for Eduard to file at https://gramps-project.org/bugs (new issue).
Claude does not file tracker issues — this is the ready-to-paste text.

---

## Tracker fields

| field | value |
|---|---|
| Category | 3rd Party Addons |
| Severity | minor |
| Reproducibility | always |
| Product Version | 6.1.0 (also affects 6.0.x) |
| Summary | [DynamicWeb] OpenLayers stylesheet ol.css is loaded as a script, raising a console SyntaxError and leaving map controls unstyled |

(File against the project matching the branch you intend to fix first —
"Gramps 6.0" if targeting maintenance/gramps60. Note in the report that it
also affects 6.1. master is NOT affected — see below.)

## Description

On every DynamicWeb place/family map page (when the report is generated with
Map Service = OpenStreetMap), the browser console reports:

```
Uncaught SyntaxError: Unexpected token ':'   ol.css:1
```

The OpenStreetMap tiles and place markers still render, but OpenLayers' own
control styling — the zoom buttons, the attribution line, popup chrome — is
missing, because the OpenLayers stylesheet is never applied as CSS.

The cause is in the report's bundled loader. `dwr_start.js` defines two
helpers: `LoadJsFile()` injects a `<script src=…>` element, and
`LoadCssFile()` injects a `<link rel="stylesheet" href=…>` element. The
OpenLayers assets are loaded as:

```js
LoadJsFile(scriptFolder + 'ol.js');     // correct — ol.js is JavaScript
LoadJsFile(scriptFolder + 'ol.css');    // wrong  — ol.css is a stylesheet
```

The second line uses the JavaScript loader for a CSS file, so the browser tries
to parse `ol.css` as JavaScript and fails at the first `selector: value` rule
(the stray `:` in the SyntaxError). It should use `LoadCssFile`.

This affects the maintenance branches only. master loads ol.css from the
OpenLayers CDN via the correct `LoadCssFile`, so master does not have the bug;
it was introduced when the maintenance branches switched to bundling a local
copy of ol.css but reused the adjacent `LoadJsFile` idiom from the ol.js line.

## Steps to reproduce

1. Open example.gramps (places have coordinates).
2. Reports → Web Pages → Dynamic Web Report. On the Options tab, enable
   "Include Place map on Place Pages" and set Map Service to OpenStreetMap.
   Generate to any directory.
3. Serve the output over HTTP (the report's data loads via dynamically injected
   scripts, which browsers block under file://):
   `python3 -m http.server` in the output directory.
4. Open a geocoded place page (e.g. places.html → Albany) in a browser and open
   the developer console.

## Expected

ol.css is applied as a stylesheet; OpenLayers controls (zoom, attribution) are
styled; no console error.

## Actual

`Uncaught SyntaxError: Unexpected token ':'  ol.css:1`; OpenLayers controls are
unstyled. The map itself is otherwise functional.

## Suggested fix

In `DynamicWeb/templates/dwr_default/data/dwr_start.js`, change the ol.css load
from `LoadJsFile` to `LoadCssFile`:

```diff
-LoadJsFile(scriptFolder + 'ol.css');
+LoadCssFile(scriptFolder + 'ol.css');
```

## Notes

- One-character-class fix; no behaviour change beyond the controls picking up
  their stylesheet and the console error disappearing.
- Found while verifying an unrelated DynamicWeb fix (the OsmPointStyle
  `feature.get('name')` change); filed separately per one-issue-per-ticket.
