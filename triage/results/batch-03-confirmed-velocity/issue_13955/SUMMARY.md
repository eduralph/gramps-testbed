# Issue 13955 — RepositoriesReport omits URLs when "include URLs" is selected

## Root cause
`RepositoryReportAlt.__write_repository`
([RepositoriesReportAlt.py:198-200](../../../../../../addons-source/RepositoriesReport/RepositoriesReportAlt.py#L198-L200) pre-fix) carried the URL-writing
block commented out:

```python
#if self.inc_intern:
    #self.doc.write_text(self._('Internet:'))
    #self.doc.write_text(internet)
```

The variable `internet` was never defined anywhere, so naively
uncommenting it would raise
`NameError: name 'internet' is not defined`. codefarmer on Mantis
13955 note 7 captured this: the block has been commented since
2010. With include-URLs ON the report opened an Internet paragraph
(via the outer `if self.inc_intern or self.inc_addres:` guard at
line 195) but emitted nothing into it; per-address iteration then
left empty paragraphs (one per address) — silently dropping the
URLs the user asked for.

The verdict explicitly required "uncomment the URL-writing block
AND restore the assignment of `internet` ... NOT just uncomment."

## Fix
Replace the stub block with the URL section it should have always
been. Compute URLs from `repository.get_url_list()` — the same
attribute `gramps/plugins/textreport/tagreport.py:712` and
`gramps/plugins/webreport/narrativeweb.py:1485` use to find a
repository's web addresses — and write them in their own paragraph
guarded by `inc_intern`. Lift the block OUT of the per-address
loop:

- A repository with **zero addresses** still gets its URLs printed
  (the old in-loop placement missed this case entirely).
- A repository with **multiple addresses** does not duplicate the
  URL list per iteration.

Drop the now-stale outer `if self.inc_intern or self.inc_addres:`
guard; each block has its own gate.

Honour the rest of the report's empty-field convention: with
`inc_intern` on and zero URLs the Internet paragraph is suppressed
unless `incl_empty` is also on (mirrors the
`inc_addres` / `incl_empty` pattern at the original line 201).

## Test
`RepositoriesReport/tests/test_repositoriesreport_internet.py`
(new; stdlib `unittest`, plus `tests/__init__.py`). Three cases:

1. `test_urls_written_when_inc_intern_on` — Stubbed repository
   with two URLs + `inc_intern=True` → both URLs (joined with
   `\n`) reach `doc.write_text` AND the `Internet: ` label
   appears. Fails pre-fix with
   `AssertionError: 'Internet: ' not found in ['Test Library (Library)']`.
2. `test_no_url_paragraph_when_inc_intern_off` — Same repo,
   `inc_intern=False` → no Internet label, no URL text.
   (Same pre-fix outcome; pins the gate against a later refactor
   that "always writes the section.")
3. `test_no_url_paragraph_when_no_urls_and_incl_empty_off` — Empty
   `get_url_list()`, `incl_empty=False` → no Internet paragraph.

Built via `__new__`-bypass so the test doesn't need an Options
object, a database, a User, or a real doc backend. `self.doc` is a
`MagicMock`; assertions read `write_text.call_args_list`. Pure
unit test — no display, no doc backend, no Gramps DB.

Gates on `gi.require_version("Gtk", "3.0")` because the addon's
import chain pulls `gramps.gen.plug.docgen`, which transitively
touches GTK-3-only enums.

Verified via `run-addon-unit.sh RepositoriesReport`:

  - Before fix: FAILED (failures=1) on `test_urls_written_when_inc_intern_on`
  - After fix:  3 tests, OK

## Check upstream isn't ahead
- `gh pr list -R gramps-project/addons-source --state all --search 'RepositoriesReport'`
  → only PR 423 (2020 Dutch translation update).
- Closed-PR pre-flight: clean.
- Per `feedback_check_closed_prs_too` — both queries returned nothing relevant.

## Repo and branch
- Repo: `addons-source` (in-tree `RepositoriesReport/`)
- Branch: `fix/bug-13955-repositoriesreport-urls` based on
  `upstream/maintenance/gramps60`
- Commit: `944b6309e RepositoriesReport: write repository URLs when "include URLs" is on`
- Status: committed locally on the fork worktree; not pushed, no
  PR opened — awaiting Eduard's review gate.

## Mantis link
[bug 13955](https://gramps-project.org/bugs/view.php?id=13955).
Commit trailer ends with `Fixes #13955`.
