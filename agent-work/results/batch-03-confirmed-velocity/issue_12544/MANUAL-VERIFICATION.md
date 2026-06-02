# Manual verification — Mantis 12544 (DynamicWeb OsmPointStyle)

## Why this is manual
The fix changes `dwr.js`, JavaScript that runs in the browser as part of a
generated DynamicWeb site. The testbed's Linux AT-SPI suite doesn't cover web
output and addons-source CI has no headless-browser job, so the marker behaviour
must be confirmed in a real browser.

**Critical:** the 12544 fix lives only in the **OpenStreetMap** code path
(`OsmPointStyle` / `OsmClick` in `dwr.js`). If the report is generated with the
default **Google** map service, the patched code never executes and the test is
meaningless. The report MUST be generated with Map Service = OpenStreetMap and
place maps enabled (see below). This was the single biggest trap during the
first verification attempt.

---

## 1. Make the addon load under the running Gramps

The addon branch is `maintenance/gramps60`, so its `.gpr.py` declares
`gramps_target_version="6.0"`. The testbed's gramps is currently **6.1.0**.
`valid_plugin_version` rejects a 6.0-targeted addon under 6.1
(`gramps/gen/plug/_pluginreg.py` — `(6,0) != (6,1)`), so it never appears in the
menu — this is bug 13736 in miniature. The fix is version-agnostic JS, so
testing under 6.1 is valid; just get the addon to register:

```bash
cd ../addons-source && git checkout fix/bug-12544-dwr-osmpointstyle-feature-get
# throwaway: let it register under 6.1 (DO NOT commit)
sed -i 's/gramps_target_version="6.0"/gramps_target_version="6.1"/' \
  DynamicWeb/dynamicweb.gpr.py
```

Launch the manual container shell:

```bash
cd ../gramps-testbed && ./scripts/ubuntu/run-manual.sh --shell
```

Install the addon into the plugin dir. **Use a copy, not a symlink** — stock
Gramps scans plugin dirs with `os.walk(followlinks=False)`
(`gramps/gen/plug/_manager.py`), so a symlinked addon dir is *not* descended
into and never registers (fixed by the unmerged gramps PR #2248). Inside the
container:

```bash
PLUGINS=$(python3 -c "from gramps.gen.const import USER_PLUGINS; print(USER_PLUGINS)")
rm -f "$PLUGINS/DynamicWeb"
cp -r /workspace/addons-source/DynamicWeb "$PLUGINS/DynamicWeb"
gramps -O TestTree
```

Revert the throwaway target-version edit when done:
`git -C ../addons-source checkout DynamicWeb/dynamicweb.gpr.py`.

---

## 2. Generate the report — the options that matter

**Reports → Web Pages → Dynamic Web Report → "Options" tab:**

1. ☑ **Include Place map on Place Pages** (default OFF — without it `printMap()`
   returns nothing and no map is drawn).
2. **Map Service → OpenStreetMap** (default "Google" — and only the
   OpenStreetMap path contains the patched `feature.get('name')` call).
3. *(optional)* ☑ Include a map in the individuals and family pages.

**Destination:** write to a path that is bind-mounted to the host so the output
is reachable from your host browser. The one mounted dir is the Gramps home:

```
/home/runner/gramps-home            (container)
→ gramps-testbed/.run/gramps-home   (host)
```

Do NOT use `/tmp` or `/home/runner/test` — those are container-only and vanish /
are invisible from the host.

Confirm the generated `dwr_conf.js` has:
`INC_PLACES=true; MAP_PLACE=true; MAP_SERVICE="OpenStreetMap"`.

---

## 3. Serve over HTTP (file:// will not work)

The site loads its data via dynamic `<script>` injection (`loadScript`), which
browsers block under `file://` — the page renders blank. Serve it over HTTP from
the **host** (use `/usr/bin/python3`; the snap-wrapped `python3` in a VS Code
terminal dies with a `GLIBC_PRIVATE` symbol error):

```bash
cd gramps-testbed/.run/gramps-home
/usr/bin/python3 -m http.server 8099 --bind 127.0.0.1
```

Open `http://localhost:8099/places.html` in the host browser (OpenLayers tiles
load from the network, so the host browser — not the container — is required).

---

## 4. Acceptance

1. Navigate to a place that has coordinates (e.g. Albany, Dougherty, GA — most
   `example.gramps` cities are geocoded). The OpenStreetMap map renders with a
   marker pin at the place's lat/long. **The pin rendering at all is the core
   proof**: `OsmPointStyle` ran and read the marker name via the patched
   `feature.get('name')`; had it returned `undefined`/thrown, the marker style
   would fail and no pin would draw.
2. **Click** the marker → popup shows the place name (exercises the `OsmClick`
   handler, which already used `feature.get('name')` — the precedent the fix
   aligns to). Both name-lookup paths now consistent.
3. DevTools console: no `values_` / `undefined` / `feature.get` errors.

### Known unrelated console error — do NOT fail the verification on it
`Uncaught SyntaxError: Unexpected token ':' at ol.css:1` is a **separate,
pre-existing DynamicWeb bug** (`dwr_start.js:130` loads `ol.css` via
`LoadJsFile` instead of `LoadCssFile`, so the browser parses CSS as JS). It only
costs OpenLayers control styling; tiles + markers still render. Tracked
separately — see `results/issue_dynamicweb_olcss_loader/`. It is not caused by
and does not affect the 12544 fix.

---

## Result (2026-05-29, gramps 6.1.0, OpenStreetMap, example.gramps)
PASS. Place "Albany, Dougherty, GA, USA" (31.5785, -84.1557) rendered the
OpenStreetMap map with a marker pin at the correct location; the patched
`OsmPointStyle` executed (3 `feature.get('name')` occurrences confirmed in the
generated `data/dwr.js`). Only console error was the unrelated `ol.css` loader
bug above.
