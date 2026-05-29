Unable to reproduce on current systems with an up-to-date TLS stack.

The `"Unacceptable TLS certificate"` error originates in the
`g-io-error-quark` domain — GLib's gio networking layer (GnuTLS, via
GeocodeGlib). The addon never touches the socket or the certificate chain;
it calls `GeocodeGlib.Forward.new_for_string(...).search()` and displays
the underlying error to the user verbatim. There is no TLS logic in the
addon source to fix.

Verified that Nominatim — the geocoding endpoint GeocodeGlib targets —
currently presents a valid TLS certificate (Let's Encrypt R13, 2026,
chain validates cleanly with current OpenSSL/GnuTLS). Code-level review
on `maintenance/gramps60` confirms the addon's HTTPS path is unchanged
since the 2020 switch from geopy to GeocodeGlib.

The original 2021 report (Gramps 5.1.4, empty tracker entry — no notes
or steps) most plausibly hit one of: outdated system CA bundle, corporate
proxy TLS interception, or end-of-lifed system GnuTLS / OpenSSL.

Closing as cannot-reproduce / environmental. Please reopen with OS
version, system OpenSSL/GnuTLS version, and the output of
`openssl s_client -connect nominatim.openstreetmap.org:443 -servername nominatim.openstreetmap.org`
if the symptom recurs on a current system.
