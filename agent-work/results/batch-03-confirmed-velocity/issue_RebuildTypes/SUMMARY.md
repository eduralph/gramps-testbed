# RebuildTypes — delete the addon (per Nick Hall's request on closed PR 877)

## Original triage verdict
The increment-1 addendum directed a Py3-namespace import fix
(`from gui.plug import tool` → `from gramps.gui.plug import tool`,
`from QuestionDialog import OkDialog` → `from gramps.gui.dialog import OkDialog`).
Source state on `upstream/maintenance/gramps60` was confirmed
broken: `ModuleNotFoundError: No module named 'gui'` at plugin
registration, exactly as the detector flagged.

## What changed during execution
Mid-batch the maintainers' prior decision on the same addon
surfaced. **upstream PR
[#877](https://github.com/gramps-project/addons-source/pull/877)**
(CLOSED 2026-05-15, branch `fix/rebuildtypes-py3-namespace-imports`)
was the previous port attempt with the same fix shape. The thread
there closed it in favour of deletion:

- **GaryGriffin**: `RebuildTypes.gpr.py` declares
  `include_in_listing=False`, `status=UNSTABLE`,
  `category=TOOL_DBFIX` — "Seeing TOOL_DBFIX and UNSTABLE together
  is scary for a released addon."
- **Nick-Hall** (addon author + core maintainer): *"The
  RebuildTypes addon was either just an example or written for a
  particular person to fix a bug. An export followed by an import
  will achieve the same result. The Type Cleanup tool may also be
  a better option. **I am happy for this addon to be deleted.**"*

Eduard closed #877 on the basis of that exchange. The detector
re-flagged the same addon in this batch without visibility into
that history.

## Action taken
Two iterations on the same PR (#918) — they are visible in the
PR's force-push history but only the second one is shipping:

1. **First commit (`93dbe4bc6`, then force-replaced):** the port
   fix from the addendum's task list — `RebuildTypes/RebuildTypes.py`
   imports migrated, regression test added at
   `RebuildTypes/tests/test_rebuildtypes_imports.py`. Test failed
   pre-fix with the exact `ModuleNotFoundError: No module named
   'gui'` and passed post-fix via the testbed's
   `run-addon-unit.sh RebuildTypes`. This commit was discarded
   when PR 877's history surfaced.
2. **Final commit (`faa1a1058`, shipping):** delete `RebuildTypes/`
   entirely (16 files, -525 lines). No replacement; users with the
   same need have two supported alternatives Nick named —
   export/re-import or the _Type Cleanup_ tool. Verified `grep -rn
   'RebuildTypes'` on `maintenance/gramps60` outside the directory
   itself: no hits in any `.py` / `.json` / `.txt` / `.md` /
   `.yml`. Listings in `gramps-project/addons` did not reference it
   either (already `include_in_listing=False`).

## Repo and branch
- Repo: `addons-source` (in-tree addon `RebuildTypes/`, now deleted)
- Branch: `fix/rebuildtypes-py3-imports` based on
  `upstream/maintenance/gramps60` (vestigial name — the commit on
  it is a deletion, not a port)
- Commit: `faa1a1058 Delete RebuildTypes addon per author's request`
- Upstream PR:
  [#918](https://github.com/gramps-project/addons-source/pull/918)
  — base `maintenance/gramps60`, status: ready for review (Eduard
  authorised ready-mark before the deletion repurpose; the
  ready-mark carried over after the force-push)

## Mantis link
None — detector-sourced (c)-bucket; no Mantis issue.

## Process lesson
"Check upstream isn't ahead" was applied to merged PRs only on
the first pass — closed PRs carry equally important signal about
what maintainers have rejected. Adding closed-PR checks to the
per-addon pre-flight would have caught this before any commit
landed. Captured separately in user memory for future batches.
