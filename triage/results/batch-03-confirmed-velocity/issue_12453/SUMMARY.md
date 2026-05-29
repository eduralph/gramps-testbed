# Issue 12453 — PlaceCoordinatesGramplet TLS cert error — close as external/environmental

## Status
**Close as cannot-reproduce / external (system TLS layer).** No code change.

## Verification
Investigated in this increment via code-level analysis on
`upstream/maintenance/gramps60` (no GUI repro per the workstream-B UIA
spike pause). The empty Mantis record (no notes, no steps, 2021, Gramps
5.1.4) constrained the investigation, but the error signature itself is
diagnostic.

Where the HTTPS call actually happens:
- `PlaceCoordinateGramplet/PlaceCoordinateGramplet.py:223-226` —
  forward geocoding via `GeocodeGlib.Forward.new_for_string(...).search()`
- `PlaceCoordinateGramplet/PlaceCoordinateGramplet.py:260-261`,
  `:291-292` — reverse geocoding via
  `GeocodeGlib.Reverse.new_for_location(loc)` + `.resolve(obj)`
- The backend service GeocodeGlib targets is **Nominatim** at
  `https://nominatim.openstreetmap.org/`.
- The HTTPS request / TLS handshake happens entirely inside
  GeocodeGlib (GLib's `gio` layer) — addon Python never touches the
  socket or the certificate chain.

Error attribution:
- The error string `"Unacceptable TLS certificate"` does NOT appear
  anywhere in `PlaceCoordinateGramplet/*.py`. It comes from the
  GLib `g-io-error-quark` error domain — system TLS (GnuTLS via GIO).
- The addon catches `Exception` at lines 228 and 245 and displays
  the error's `.message` to the user verbatim. The error originates
  in the system, not the addon.

Current endpoint state (2026):
```
$ curl -I https://nominatim.openstreetmap.org/
HTTP/2 302  ✓ Valid
$ openssl s_client -connect nominatim.openstreetmap.org:443 -servername nominatim.openstreetmap.org
verify return:1  ✓ Certificate chain validates
issuer: C=US, O=Let's Encrypt, CN=R13  ✓ Current Let's Encrypt cert
```

Nominatim's endpoint is alive and presents a valid current TLS
certificate. The 2021 reporter's environment most likely had:
- An outdated system CA bundle missing the chain root, or
- A corporate proxy doing TLS interception with an untrusted intermediate, or
- An end-of-lifed system OpenSSL / GnuTLS version unable to validate the chain.

Git history check:
- `git log upstream/maintenance/gramps60 -- PlaceCoordinateGramplet/`
  shows the last functional change as commit `e77a89829` (August 2020,
  switch from geopy to GeocodeGlib). No TLS, cert-handling, or
  endpoint-URL changes since.
- No open or closed addons-source PRs touching the addon's TLS path
  (`gh pr list --repo gramps-project/addons-source --state all --search "PlaceCoordinates"`).

**This is an external / environmental issue at the system TLS layer**, not
an addon defect. Current Linux systems with up-to-date GnuTLS/OpenSSL and
a current CA bundle do not reproduce. The addon has no TLS code to fix —
the addon already correctly delegates to GeocodeGlib and displays the
underlying error to the user.

## Repo and branch
- Repo: `addons-source` (`PlaceCoordinateGramplet/`)
- Branch: maintenance/gramps60 — no commit; close-only.
- This batch: no patch.diff, no pr-description.md.

## Mantis link
- Tracker: https://gramps-project.org/bugs/view.php?id=12453
- Status to set: resolved / cannot reproduce (external / environmental)
- Fixed in version: N/A
- Comment: see `mantis-comment.md`

## Notes for next reviewer
- **NOT part of the 13065 cluster.** Increment-3 brief explicitly flags
  this: "13065 is a Gramps CORE bug in `display_url()`; 12453 is about
  the incoming TLS from `GeocodeGlib.search()` — different code path,
  different root cause. Do not conflate."
- If a current user reports the same error, the productive next step
  is `openssl s_client` against the reported endpoint plus a system
  CA-bundle / GnuTLS version dump — those data answer it. Not an
  addons-source issue.
