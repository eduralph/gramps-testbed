# Mantis 14145 — ready-to-paste comment (Eduard)

(Bare bug numbers per the no-`#`-prefix convention; addons-source
PRs need the full GitHub URL — no shorthand exists for that repo
per CLAUDE.md "Linking a GitHub PR from a MantisBT note".)

---

Fixed in FrWebConnectPack. The Geneanet entry in
`FRWebConnectPack/FRWebPack.py` now uses the URL you supplied in
note 3:

  `https://www.geneanet.org/fonds/individus/?go=1&nom=%(surname)s&prenom=%(given)s`

Both the surname and the given name now reach Geneanet's current
`fonds/individus` search; the deprecated
`search.geneanet.org/result.php` form (which only carried the
surname) is gone.

PR: https://github.com/gramps-project/addons-source/pull/919
Commit: 26ab7f98d on maintenance/gramps60

Acknowledged callmedave's WebSearch Gramplet recommendation (notes
2, 4) but this is the live addon, and note 5 explicitly confirmed
the bug for FrWebConnectPack — so it's a real fix, not wontfix.
No migration to WebSearch attempted; scope kept to the single
Geneanet URL.

A regression test in `FRWebConnectPack/tests/` pulls the Geneanet
pattern from `WEBSITES` and applies the same `pattern % dict`
formatting libwebconnect uses; pure string assertion, no network.
It fails pre-fix (the old surname-only template), passes post.

Thanks for the corrected URL.

Resolution: fixed
Fixed in version: next addons release (Gary manages addon version
bumps centrally; the addon's `.gpr.py` version is not bumped per
PR).
