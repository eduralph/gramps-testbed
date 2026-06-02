# Mantis 13065 — ready-to-paste comment (Eduard)

(Bare bug numbers per the no-`#`-prefix convention; gramps core PR
linked with `p:gramps:` shorthand per CLAUDE.md "Linking a GitHub
PR from a MantisBT note".)

---

Confirmed already fixed in 5.2. The fix is in gramps core, not in
PlaceCoordinatesGramplet — the Nominatim URL is built by the core
Map Service, which is why the symptom only appears via this addon
but the patch landed core-side.

Commit 44629e3 ("Fix error 404 with openstreetmap map service",
SNoiraud, 2023-08-20), merged via p:gramps:1530:. The Map Service
URL builder at gramps/plugins/mapservices/openstreetmap.py:64 now
uses the `/search?q=` form (no `.php`, no trailing slash) — which
is the only form Nominatim still accepts per daleathan's note 3
and the upstream Nominatim issue osm-search/Nominatim#3134. The
commit also upgraded the protocol from `http://` to `https://`.

Bishnu already signed off in note 5 ("I confirm that this issue
is solved with GRAMPS 5.2.0"); closing.

Resolution: fixed
Fixed in version: 5.2.0
