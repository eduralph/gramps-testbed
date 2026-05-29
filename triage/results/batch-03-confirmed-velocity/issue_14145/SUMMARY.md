# Issue 14145 — FrWebConnectPack Geneanet link broken

## Root cause
`FRWebConnectPack/FRWebPack.py:45` stored the Geneanet search URL
as
`https://search.geneanet.org/result.php?lang=fr&name=%(surname)s`.
Geneanet deprecated the `search.geneanet.org/result.php` path, and
the template only carried the surname — Geneanet's current
`fonds/individus` search requires both `nom` and `prenom` to return
useful results.

## Fix
One-line URL-template replacement, using the corrected URL the
reporter supplied (tracker note 3) and matching the file's existing
`%(...)s` placeholder convention:

```diff
-["Person", "Geneanet", "Geneanet", "https://search.geneanet.org/result.php?lang=fr&name=%(surname)s"],
+["Person", "Geneanet", "Geneanet", "https://www.geneanet.org/fonds/individus/?go=1&nom=%(surname)s&prenom=%(given)s"],
```

Both placeholders are populated by libwebconnect's
`make_person_dict` (libwebconnect.py:88-128) and substituted via
`pattern % results` at `libwebconnect.Search.callback`
(libwebconnect.py:182). No other Web Connect Pack addons changed
(out of scope — one logical fix per issue).

## Maintainer caveat (already considered)
callmedave (notes 2, 4) pushes the **WebSearch Gramplet** as a
long-term replacement for the Web Connect Pack family, but note 5
on the same thread explicitly confirms the bug for FrWebConnectPack
— so the live addon is in scope and this is not wontfix. The fix
is conservative (one URL); no migration to WebSearch attempted.

## Test
`FRWebConnectPack/tests/test_geneanet_url.py` (new; stdlib
`unittest`, plus `tests/__init__.py` — the addon had no `tests/`
package yet). Two cases, both pure string assertion (no network,
no display, no Gtk):

1. `test_built_url_contains_both_name_parts` — apply the Geneanet
   pattern via `pattern % dict` (the same call libwebconnect itself
   uses) with a Dupont/Marie dummy; assert both names appear. Fails
   pre-fix because the old template discarded `given`.
2. `test_built_url_uses_current_geneanet_host_and_path` — assert
   the URL contains `www.geneanet.org/fonds/individus/` and the
   `nom=` / `prenom=` query keys, and does NOT contain
   `result.php` or `search.geneanet.org`.

Verified via the testbed's
`run-addon-unit.sh FRWebConnectPack`:

  - Before fix: FAILED (failures=2) — `'Marie' not found in 'https://search.geneanet.org/result.php?lang=fr&name=Dupont'`
  - After fix:  2 tests, OK

## Check upstream isn't ahead
- `gh pr list -R gramps-project/addons-source --state all --search 'FRWebPack'` → only PR 258 (2019 translation update).
- Closed-PR pre-flight: no closed PR mentions deprecation or retirement of the addon.
- Per `feedback_check_closed_prs_too` — both queries clean.

## Repo and branch
- Repo: `addons-source` (in-tree `FRWebConnectPack/`)
- Branch: `fix/bug-14145-frwebpack-geneanet-url` based on
  `upstream/maintenance/gramps60` (per
  `feedback_branch_targeting_addons_vs_core`)
- Commit: `26ab7f98d FRWebConnectPack: update Geneanet search URL to current individus form`
- Status: committed locally on the fork worktree; not pushed, no
  PR opened — awaiting Eduard's review gate.

## Mantis link
[bug 14145](https://gramps-project.org/bugs/view.php?id=14145).
Commit trailer ends with `Fixes #14145` per
`feedback_mantis_fixes_trailer`.
