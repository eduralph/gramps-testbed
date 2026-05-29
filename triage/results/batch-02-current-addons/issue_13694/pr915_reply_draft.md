# Draft reply for PR 915 (Eduard to post)

Two threads on the PR — Gary's multi-gpr finding, and Gary's branch-
targeting question. Drafts for both follow; Eduard is the one who
posts these.

---

## Draft 1 — addressing the multi-gpr corruption

Thanks for catching the Form case — reproduced it cleanly. Pushed a
follow-up commit (`abbeb0433`) that extends the fix.

The root cause is in the same merge path but a separate symptom: the
outer `for plugin in sorted(listings, ...)` loop reopened and
re-read the existing listings file on each iteration while
accumulating into a shared `output`. With three new plugins for
Form (two .gpr.py files, three `register()` calls total), every
existing entry ended up appended three times — 170 → 510 entries
in `addons-en.json`, every other addon appearing thrice. Same shape
would corrupt for any addon with N>1 registers.

The follow-up commit replaces the per-plugin re-read with a single-
pass merge: read the existing file once, drop every row that
belongs to `cmd_arg` (matched by `.z`) or whose `(t, i)` collides
with one of the fresh plugins, then merge the kept rows with the new
plugins in sorted `(t, i)` order. Two side-effects worth flagging,
both intentional:

1. Stale entries for `cmd_arg` (e.g. a `register()` removed from a
   `.gpr.py` since the last build) are now dropped, not preserved.
   The old code couldn't distinguish "this entry's plugin still
   exists" from "this entry is stale" because it matched lines by
   `(z, t)` — multiple Form lines all matched `Form.addon.tgz` so
   "first match wins" was effectively undefined.
2. The "first match wins" ambiguity of the old `z + t` matcher is
   gone; replacement matches per-plugin by `(t, i)`. For Form the
   stale `formgramplet` entry gets replaced with the fresh
   `myform_gramplet` (in the test fixture) without touching the two
   quickreports.

Test extended in `tests/test_make_listing.py` — the multi-gpr case
fails on the pre-fix code with the exact "14 != 6" duplication
symptom, passes after. Verified end-to-end against the real
`../addons/gramps61/listings/addons-en.json`: `listing Form` keeps
the file at 170 entries with 3 Form rows; `listing CheckPlaceTitles`
(`include_in_listing=False`) and `listing QuiltView` (single-plugin)
still behave correctly.

---

## Draft 2 — branch targeting question

(Eduard, the gramps60-vs-gramps61 question is more your call than
mine — what's below is a starting point you can edit / discard.)

> Concerning the gramps60 branch, I'm a bit confused tbh. gramps
> core has switched over to gramps61 so I've been running my fixes
> against that despite there being a 6.0.9 in mantis. For
> addons-source we seem to be doing something slightly different.
> Is there a reference page or something that I can refer to?

If the addons-source convention is that fixes land on gramps60 first
and forward-merge to gramps61, I'm happy to rebase 915 onto gramps60
and you can cherry-pick. Just confirm and I'll do that.

(Background context for myself: my reading of jralls + Nick-Hall on
gramps#2275 was that the active maintenance branch for fixes is now
`maintenance/gramps61`; that's what I've been targeting for the
gramps-core PRs. For addons-source the branches are independent and
the convention may differ — if so, a one-liner on the wiki or in
addons-source README would be helpful.)
