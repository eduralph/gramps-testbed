# DynamicWeb — ol.css loaded as JavaScript (console SyntaxError, missing OL control styling)

**Status:** NEW find — no Mantis ID yet. Discovered 2026-05-29 while doing the
manual browser verification for Mantis 12544 (same addon, different bug). Needs
a decision: file on Mantis + fix, or fix directly with a Mantis filing in the
PR. NOT bundled into 12544 (one issue per ticket).

## Symptom
Every DynamicWeb place/family map page logs, in the browser console:

```
Uncaught SyntaxError: Unexpected token ':'   ol.css:1
```

The OpenStreetMap map tiles and markers still render, but OpenLayers' own
control styling (zoom buttons, attribution, popups) is unstyled because its
stylesheet never actually applies as CSS.

## Root cause
`DynamicWeb/templates/dwr_default/data/dwr_start.js` has two loader helpers:

- `LoadJsFile(f)` → `document.write('<script src="'+f+'">')` (loads as JS;
  uses `document.write` deliberately so it works under `file://`).
- `LoadCssFile(f)` → creates a `<link rel="stylesheet" href=f>` (loads as CSS).

At lines 127–130 the OpenLayers assets are pulled in:

```js
//	LoadJsFile('http://openlayers.org/en/latest/build/ol.js');
LoadJsFile(scriptFolder + 'ol.js');     // line 128 — correct (ol.js IS JS)
//	LoadCssFile('http://openlayers.org/en/latest/css/ol.css');
LoadJsFile(scriptFolder + 'ol.css');    // line 130 — WRONG: ol.css is CSS
```

Line 130 loads the bundled `ol.css` with `LoadJsFile`, so the browser injects
`<script src="…/ol.css">` and tries to parse the CSS as JavaScript → the
`Unexpected token ':'` SyntaxError (the first `selector:value` is invalid JS).
Note line 129's commented-out original correctly used `LoadCssFile` against the
remote CDN; whoever switched to the local bundle (line 130) copied the
`LoadJsFile` idiom from the adjacent `ol.js` line and missed that ol.css needs
the CSS loader.

## Fix (one line)
`maintenance/gramps60` and `maintenance/gramps61`, line 130:

```diff
-LoadJsFile(scriptFolder + 'ol.css');
+LoadCssFile(scriptFolder + 'ol.css');
```

## Check upstream isn't ahead — DONE 2026-05-29
The two maintenance branches are live-buggy; **master is not affected** because
it took a different route (remote CDN + correct loader):

| branch | dwr_start.js ol.css line | affected? |
|---|---|---|
| `maintenance/gramps60` | `LoadJsFile(scriptFolder + 'ol.css')` | YES |
| `maintenance/gramps61` | `LoadJsFile(scriptFolder + 'ol.css')` | YES |
| `master` | `LoadCssFile('https://openlayers.org/en/latest/css/ol.css')` | no |

So master can't be the cherry-pick source — it uses the CDN, not the bundled
file. The maintenance-branch fix is the local-bundle variant above. No existing
open/closed PR addresses this (`gh pr list --search "DynamicWeb ol.css"` →
only unrelated #520). Branch target per the addons-source rule:
`maintenance/gramps60` (Gary forward-cherry-picks to gramps61).

## Repro
1. Generate a DynamicWeb report with Map Service = OpenStreetMap and
   "Include Place map on Place Pages" enabled (see
   `../issue_12544/MANUAL-VERIFICATION.md` for the full harness).
2. Serve over HTTP, open a geocoded place page, open DevTools console.
3. Observe `Uncaught SyntaxError: Unexpected token ':'  ol.css:1`. Zoom/
   attribution controls are unstyled.

## Test / verification approach
No automated test (browser JS, no headless-browser runner). Manual:
pre-fix the console shows the SyntaxError and OL controls are unstyled;
post-fix the console is clean and the zoom/attribution controls pick up
OpenLayers' stylesheet. Manual repro above; same harness as 12544.

## Why not bundled with 12544
Different defect (asset-loader mistake vs. private-API marker read), different
file (`dwr_start.js` vs `dwr.js`), and the one-issue-per-ticket rule. 12544
ships on its own; this gets its own Mantis filing + PR.
