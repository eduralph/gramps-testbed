# Mantis 13955 — ready-to-paste comment (Eduard)

(Bare bug numbers per the no-`#`-prefix convention; addons-source
PRs need the full GitHub URL — no shorthand.)

---

Fixed. codefarmer's diagnosis in note 7 was on the money: the
URL-writing block in `RepositoriesReport/RepositoriesReportAlt.py`
(line 198-200 pre-fix) had been commented out since 2010, and a
naive uncomment threw `NameError: name 'internet' is not defined`
— which is exactly why it stayed commented all that time.

The variable `internet` is now built from
`repository.get_url_list()` (the same attribute
`gramps/plugins/textreport/tagreport.py:712` uses for the same
purpose) and the Internet paragraph is written once per repository
rather than once per address. Side effect: repositories with no
addresses now also get their URLs printed (the old in-loop
placement missed that case), and repositories with multiple
addresses no longer duplicate the URL list per iteration.

With "include repositories urls" selected the report now contains
the URLs the user asked for; with it off, the Internet paragraph
is suppressed entirely.

PR: https://github.com/gramps-project/addons-source/pull/920
Commit: 944b6309e on maintenance/gramps60

A regression test in `RepositoriesReport/tests/` exercises the
fixed `__write_repository` path against a stubbed repository with
two URLs and asserts they reach the doc; two more cases pin the
off-switch and the empty-URL-list behaviour. Pre-fix the URL test
fails with `'Internet: ' not found`; post-fix all three pass.

Resolution: fixed
Fixed in version: next addons release (Gary manages addon version
bumps centrally; the addon's `.gpr.py` version is not bumped per
PR).
