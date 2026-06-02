## Root cause
`RepositoryReportAlt.__write_repository` (RepositoriesReportAlt.py:198-200
pre-fix) carried the URL-writing block commented out, and the variable
the commented code referenced (`internet`) was never defined anywhere — a
naive uncomment would raise `NameError: name 'internet' is not defined`.
With the include-URLs option selected, the report opened an Internet
paragraph but emitted nothing into it. codefarmer captured this on
Mantis 13955 note 7 (commented since 2010).

## Fix
Replace the stub with the URL section it should always have been. Compute
URLs from `repository.get_url_list()` (the same attribute
`gramps/plugins/textreport/tagreport.py:712` uses) and write them in a
dedicated paragraph guarded by `inc_intern`. Hoist out of the per-address
loop so a repository with zero addresses still gets its URLs and one with
multiple addresses doesn't duplicate the URL list per iteration. Drop the
now-stale outer `inc_intern or inc_addres` combined guard; each block has
its own gate. Honour the report's empty-field convention (no paragraph
unless URLs OR `incl_empty`), mirroring the `inc_addres` / `incl_empty`
pattern.

## Verified against
- `gramps/gen/lib/urlbase.py:67` — `UrlBase.get_url_list()` returns the addressable URL list on Repository (via the `UrlBase` mixin at `gramps/gen/lib/repo.py:49`).
- `gramps/gen/lib/url.py:141` — `Url.get_path()` returns the URL string.
- `gramps/plugins/textreport/tagreport.py:712` — same `for url in repo.get_url_list()` pattern used elsewhere in core for repository URLs.

## Test
`RepositoriesReport/tests/test_repositoriesreport_internet.py` (new; stdlib
`unittest`, plus `tests/__init__.py` — the addon had no `tests/` package
yet). Three cases built via `__new__`-bypass with `self.doc` mocked: URLs
written when `inc_intern` is on; no Internet paragraph when off; no
Internet paragraph when there are no URLs and `incl_empty` is off. Pure
unit test — no doc backend, no Gramps DB. Gated on
`gi.require_version("Gtk", "3.0")` because the addon's import chain pulls
`gramps.gen.plug.docgen`.

  Before fix: FAILED (failures=1) — `test_urls_written_when_inc_intern_on`
              fails with `AssertionError: 'Internet: ' not found in
              ['Test Library (Library)']`
  After fix:  3 tests, OK

Fixes #13955
