# Item 2a — Disambiguate addon vs core branch targeting in `CLAUDE.md`

**Branch:** `ci-claude-md-branch-targets` (off `main`) · **Patch:** `patch.diff`
**This is the root-cause fix; it must land before Item 2b.**

## Root cause
`CLAUDE.md`'s "Branch targeting" bullet led with the **core** rule — "the
latest `maintenance/gramps*` (today `maintenance/gramps61`)", cited to jralls
on gramps#2298 — phrased as if it applied to everything, then tacked on a
vague sentence ("An addon change must sit on the branch matching the Gramps
version it targets"). A reader infers addons→gramps61 by omission. Meanwhile
the Pre-flight check a few lines up reads `maintenance/gramps60` for addons.
That internal contradiction is the upstream source of the addon-unit CI jobs
defaulting `addons_ref` to gramps61 (Item 2b fixes the workflows).

## The fix is **disambiguate, not flip**
The `gramps61` reference is *correct for core* and is pinned to jralls#2298.
The defect is conflation, not a wrong branch number. So:
- Core sub-point keeps `maintenance/gramps61` verbatim, citation intact.
- A new Addons sub-point states `maintenance/gramps60` + maintainer
  cherry-picks forward, cited to Gary Griffin on addons-source PR 915
  (2026-05-24), and explicitly ties it to the Pre-flight check and the
  corrected CI defaults so the three can't drift apart again.

## Verified against
- `wiki/pages/05 - Addon development/16-guidelines.md:111-114` — the ratified
  rule: addons → `maintenance/gramps60`, maintainer cherry-picks forward
  (Gary Griffin, addons-source PR 915, 2026-05-24); core → `gramps61`
  (jralls#2298).
- `../addons-source` working copy — `HEAD -> origin/maintenance/gramps60`,
  current branch `maintenance/gramps60`. Confirms addon work really sits on
  gramps60, not gramps61.
- `CLAUDE.md:94` (Pre-flight) — `git log upstream/maintenance/gramps60 --
  <Addon>/`; now consistent with the Addons sub-point.

## Files
- `CLAUDE.md` (Branch-targeting bullet only).

## What this proves / leaves unproven
- **Proves:** the two halves of `CLAUDE.md` now agree, and both cite a
  source; the core rule was preserved exactly (no inadvertent gramps61→60
  flip on the jralls#2298 line).
- **Leaves unproven:** nothing mechanical — this is documentation. The
  *policy* itself is ratified upstream (doc 16 + the addons-source default
  branch), not invented here.
