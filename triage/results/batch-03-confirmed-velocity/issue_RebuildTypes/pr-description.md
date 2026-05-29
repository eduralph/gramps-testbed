## Root cause
`RebuildTypes/RebuildTypes.gpr.py` declares `include_in_listing=False`,
`status=UNSTABLE`, `category=TOOL_DBFIX` and `authors=["Nick Hall"]`. The addon
was flagged by the testbed's plugin-registration detector for two stale
Gramps-3 era pre-namespace imports (`from gui.plug import tool`,
`from QuestionDialog import OkDialog`) that prevent it from loading on Python 3
/ Gramps 5+.

## Decision (re-applying PR 877's verdict)
PR #877 ([closed 2026-05-15](https://github.com/gramps-project/addons-source/pull/877))
was the previous port attempt with the same fix shape. The thread there closed
it in favour of deletion:

> **@Nick-Hall**: "The _RebuildTypes_ addon was either just an example or
> written for a particular person to fix a bug. An export followed by an
> import will achieve the same result. The _Type Cleanup_ tool may also be a
> better option. I am happy for this addon to be deleted."

> **@GaryGriffin**: "Seeing TOOL_DBFIX and UNSTABLE together is scary for a
> released addon."

I (eduralph) closed #877 on the basis of that exchange. The addon was then
re-flagged by a downstream triage pass that didn't have visibility into the
prior thread; this PR finishes the call the maintainers already made by
removing the addon outright.

## Fix
Delete `RebuildTypes/` entirely (16 files, -525 lines: gpr / py / po
catalogues / template.pot).

## Verified against
- `RebuildTypes/RebuildTypes.gpr.py:24-30` (current `maintenance/gramps60`) —
  confirms `include_in_listing=False`, `status=UNSTABLE`, `category=TOOL_DBFIX`,
  `authors=["Nick Hall"]`.
- `grep -rn 'RebuildTypes'` on `maintenance/gramps60` outside the
  `RebuildTypes/` directory: no hits in any `.py` / `.json` / `.txt` / `.md` /
  `.yml`. The listing JSONs in `gramps-project/addons` did not reference it
  either (the addon was already `include_in_listing=False`).

## Test
N/A — pure deletion of an unlisted, unstable addon the author has agreed to
drop. Users with a custom-event-type catalogue that needs rebuilding have two
named alternatives Nick called out: export/re-import, or the _Type Cleanup_
tool (published and maintained).

(Branch name `fix/rebuildtypes-py3-imports` is a vestige of the earlier port
direction; the commit on it is now a single deletion.)
