## Root cause
`make.py <ver> listing <Addon>` builds a per-language `listings`
buffer and then either merges it with the existing
`addons-<lang>.json` or writes a fresh file. When the targeted addon
yields no eligible plugin — `include_in_listing=False`, or the
`.addon.tgz` isn't built yet — `listings` is empty, the merge loop
doesn't iterate, `output` stays `[]`, and the next statement
overwrites the file with `[]`. Every previously listed addon for
that language is wiped.

## Fix
In the per-language loop, after `listings` is built, gate the write:
when `cmd_arg != "all"` and `listings` is empty and the listings
file already exists, skip the write and print a clear pointer to
`unlist` for the user. The existing entries are preserved.

The same path string —
`f"../addons/{gramps_version}/listings/" + ("addons-%s.json" % lang)`
— was duplicated at three sites: the existence check in the merge
branch, the `open(..., "r")` that reads the existing file inside the
merge loop, and the final `open(..., "w")` that writes the output.
Adding a fourth use for the new guard would have made it four
copies in a 50-line block, and the bug is precisely the kind that
hides when one of those copies drifts (the guard checking one path
while the writer overwrites another). Hoisting into a single
`listings_path` local at the top of the loop makes the invariant
"all references read and write the same file" syntactically
enforced and keeps the new guard, the existence check, the read,
and the write trivially aligned.

## Verified against
- `make.py:947-977` — the `for p in plugins` block that filters by
  `include_in_listing` and prints `"   ignoring '%s'"` without
  contributing to `listings`. This is where `listings` ends up
  empty for an excluded addon.
- `make.py:978-1033` (pre-fix) — the write path that consumed an
  empty `output` and produced `[]` on disk. The `else:` branch
  (`# just update the lines from these addons:`) is where the
  `for plugin in sorted(listings, …)` loop fails to iterate.
- prculley's note 1 on the tracker — `listing` is not the unlist
  command, so silently corrupting the file is doubly wrong; the
  user message in the guard tells them which command to use.

## Test
`tests/test_make_listing.py` builds a temp addons-source/addons
pair, creates a synthetic addon with `include_in_listing=False`, a
placeholder `.addon.tgz`, and a seeded `addons-en.json` containing
one entry; then runs `python3 make.py <ver> listing ExcludedAddon`
as a subprocess and asserts the seed survives. Pre-fix the
assertion fails (`[] != [seed]`); post-fix it passes.

```
python3 -m unittest tests.test_make_listing -v
```

Resolves #13694
