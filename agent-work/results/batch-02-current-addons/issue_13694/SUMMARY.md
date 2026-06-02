# Issue 13694 — make.py `listing` wipes addons-<lang>.json for excluded addon

## Root cause
`make.py <ver> listing <Addon>` builds a per-language `listings`
buffer, then writes it out. The single-addon update path (cmd_arg !=
"all") merges entries from the existing `addons-<lang>.json` with
the freshly built ones. When the targeted addon yields no eligible
plugin — `include_in_listing=False`, or `.addon.tgz` not built yet —
`listings` is empty, the merge loop doesn't iterate, `output` stays
`[]`, and the next-but-one statement overwrites the file with `[]`.
Every previously listed addon for that language is wiped.

This is the reframing the triage verdict called for: prculley is
right that `listing` isn't the way to unlist an addon (use `unlist`
/ `as-needed`), but the tool corrupting its output on an
unsupported input is a real defect independent of intent.

## Fix
In the per-language listings loop, after `listings` is built but
before the merge/write:

- If `cmd_arg != "all"` and `listings` is empty and the listings
  file already exists, skip the write and print a clear pointer to
  `unlist` for the user. The file is left untouched; previously
  listed addons survive.
- Hoist the path string into a local `listings_path` so the three
  references that used `f"../addons/{gramps_version}/listings/" +
  ("addons-%s.json" % lang)` stay in sync (build/merge/write).

No behaviour change in `listing all` (which intentionally
rebuilds), and no change in the normal single-addon path (the
preserved entry just gets re-merged with the new one — current
behaviour).

## Test
`tests/test_make_listing.py` (new; stdlib `unittest`). Builds a
synthetic addon tree in a temp dir: a `.gpr.py` declaring
`include_in_listing=False`, a placeholder `.addon.tgz`, and a
seeded `addons-en.json` containing one "ExistingAddon" entry. Runs
`make.py <ver> listing ExcludedAddon` as a subprocess (so glob,
file I/O, and the CLI dispatch are exercised end-to-end), then
asserts the seeded entry is still there.

Pre-fix: `[] != [seed]` — seed wiped.
Post-fix: equal — seed preserved.

```
python3 -m unittest tests.test_make_listing -v
```
→ PASS (1 test). The full `tests/` suite (incl. the existing #820
plugin-registration tests on the fork) also still passes.

The test is self-contained — no dependency on the in-flight #820
test harness — so it loads under upstream's CI as soon as a runner
is added, and meanwhile stands as the verifiable reproducer.

## Repo and branch
- Repo: `addons-source` (in-tree `make.py`)
- Branch: `fix/bug-13694-make-listing-preserves-listings` based on
  `upstream/maintenance/gramps61`
- Commit: `f431b2e5e Fix make.py listing wiping addons-<lang>.json
  for excluded addon.`

## Notes for review
- The `listings_path` hoist is mechanical (3 identical strings →
  1 local); kept inside the same commit because it's load-bearing
  for the early-return guard.
- No change to `make.py`'s "listing all" semantics — only the
  single-addon update path is gated.
- The fix message (`'CheckPlaceTitles' produced no listing entry;
  leaving addons-en.json untouched. Use 'make.py gramps61 unlist
  CheckPlaceTitles' to remove an existing entry.`) doubles as the
  user-facing docs nudge prculley's note recommended.
