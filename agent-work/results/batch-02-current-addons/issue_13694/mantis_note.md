# Mantis 13694 — draft note (Eduard to paste once the PR is opened)

(Bare bug numbers per the no-`#`-prefix convention; addons-source
PRs linked with the full GitHub URL — `p:gramps:` shorthand applies
only to the gramps core repo.)

---

Triage finding: the actionable defect is reframed. prculley's note 1
is correct that `listing` is not the unlist command (use `unlist` /
`as-needed` for that), but the tool corrupting its own output on an
unsupported input is a real robustness bug independent of the user's
intent.

Confirmed reproducible on `addons-source/maintenance/gramps61` (and
identical code path on master). Running

```
python3 make.py gramps61 listing CheckPlaceTitles
```

against an addon whose `.gpr.py` declares `include_in_listing=False`
shrank `addons/gramps61/listings/addons-en.json` from 170 entries to
`[]` — every previously listed addon was wiped for every language
the `listing` loop iterated over. CheckPlaceTitles is just a
convenient example; the same happens for any addon with
`include_in_listing=False`, and for any addon whose `.addon.tgz`
hasn't been built yet.

Root cause (`make.py:947-1033`): the single-addon `listing <Addon>`
path builds a per-language `listings` buffer, then either replaces
the file (`listing all`) or merges with the existing file. When the
targeted addon yields no eligible plugin, `listings` is empty, the
merge loop doesn't iterate, `output` stays `[]`, and the next
`json.dump(output, fp_out, …)` overwrites the file with `[]`.

Fix (PR https://github.com/gramps-project/addons-source/pull/915):
gate the write — when `cmd_arg != "all"` and `listings` is empty and
the listings file already exists, skip the write and tell the user
the addon is not eligible and how to remove an existing entry on
purpose (`make.py <ver> unlist <Addon>`). Targets
`maintenance/gramps61`. No behaviour change in `listing all`, no
change in the normal single-addon path. The path string is hoisted
to a local so the guard, merge, and write all reference the same
file.

Regression test ships in the same PR
(`tests/test_make_listing.py`): builds a synthetic addons-source /
addons pair in a temp dir, creates an addon with
`include_in_listing=False`, seeds `addons-en.json` with one entry,
runs `make.py listing <Addon>` as a subprocess, and asserts the
seed survives. Fails pre-fix (`[] != [seed]`), passes post-fix.

Suggested tracker action: leave as confirmed until the PR merges;
no version bump needed (addons-source maintainer manages addon
versions centrally).
