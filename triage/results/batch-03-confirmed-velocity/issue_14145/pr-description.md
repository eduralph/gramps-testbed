## Root cause
`FRWebConnectPack/FRWebPack.py:45` stored the Geneanet search URL as
`https://search.geneanet.org/result.php?lang=fr&name=%(surname)s`. Geneanet
deprecated that URL — searches no longer return useful results — and the
template only carried the surname, so Geneanet's current `fonds/individus`
search couldn't filter by given name.

## Fix
Replace the stale URL template with the corrected one the reporter supplied
on tracker note 3:
`https://www.geneanet.org/fonds/individus/?go=1&nom=%(surname)s&prenom=%(given)s`.
Both `%(...)s` placeholders match the file's existing convention and are
populated by libwebconnect's `make_person_dict`.

## Verified against
- `libwebconnect/libwebconnect.py:88-128` — `make_person_dict` populates both `surname` and `given` keys.
- `libwebconnect/libwebconnect.py:182` — `display_url(self.pattern % results, …)` is the call site that consumes the template.
- `FRWebConnectPack/FRWebPack.py:41,46,48` — adjacent entries use the same `%(surname)s` / `%(given)s` convention.

callmedave (Mantis note 4) recommends the WebSearch Gramplet as a longer-term
replacement for the Web Connect Pack family, but note 5 on the same thread
confirms the bug for FrWebConnectPack — so the live addon is still in scope.

## Test
`FRWebConnectPack/tests/test_geneanet_url.py` (new; stdlib `unittest`, plus
`tests/__init__.py` — the addon had no `tests/` package yet). Two cases, both
pure string assertion (no network, no display, no Gtk): asserts that the
built URL contains both name parts AND that it targets the corrected host /
path / `nom=` / `prenom=` query keys, while the deprecated `result.php` /
`search.geneanet.org` form is absent.

  Before fix: FAILED (failures=2) — `'Marie' not found in 'https://search.geneanet.org/result.php?lang=fr&name=Dupont'`
  After fix:  2 tests, OK

Fixes #14145
