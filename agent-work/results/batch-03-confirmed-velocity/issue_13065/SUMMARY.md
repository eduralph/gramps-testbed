# Issue 13065 — Place Coordinates wrong URL (Nominatim 404) — already fixed upstream

## Status
**Closed as already-fixed in 5.2 via gramps core PR #1530.** No new
fix written. Verification only.

## Verification (per the verdict's task list)

1. **Fix commit is on the target branch.**
   `git merge-base --is-ancestor 44629e36517f4f639e961ec762e17230451b0c14 upstream/maintenance/gramps61`
   → exit 0. Commit
   [44629e3](https://github.com/gramps-project/gramps/commit/44629e36517f4f639e961ec762e17230451b0c14)
   ("Fix error 404 with openstreetmap map service", SNoiraud,
   2023-08-20) is an ancestor of `upstream/maintenance/gramps61`.

2. **Current Map Service URL builder uses the `/search?q=` form.**
   [gramps/plugins/mapservices/openstreetmap.py:64](../../../../../../gramps/gramps/plugins/mapservices/openstreetmap.py#L64) on `maintenance/gramps61`:

   ```python
   self.url = "https://nominatim.openstreetmap.org/" "search?q=%s" % "+".join(
       titledescr.split()
   )
   ```

   No `.php`, no trailing slash — matches what daleathan (tracker
   note 3) named as the only form Nominatim still accepts. The HTTPS
   upgrade (was `http://`) is a bonus that arrived alongside.

3. **Reporter confirmed in the thread.** bishnu (note 5):
   *"I confirm that this issue is solved with GRAMPS 5.2.0."*

Loop closed: core fix is in tree on both maintenance branches
(merged for 5.2 → forward-merged to gramps60 → forward-merged to
gramps61), the URL form on the live branch is the correct one, and
the reporter signed off. No regression possible from the testbed's
gramps60/gramps61 baselines.

## Repo and branch
- Repo: `gramps` (core) — addon `PlaceCoordinatesGramplet` only
  *surfaced* the symptom; the Nominatim URL is built by the core
  Map Service. Pattern matches the verdict's note (same shape as
  bug 13059: addon named in title, defect/fix in core).
- Branch: `maintenance/gramps61` — but no change is being made.
- This batch: no commit; no patch.diff; no pr-description.md.

## Mantis link
[bug 13065](https://gramps-project.org/bugs/view.php?id=13065).
Eduard's side: paste the close-as-already-fixed comment from
`MANTIS_ACTIONS.md`. Tracker fields to update per the
gramps-testbed CLAUDE.md "Resolving a bug (dev side)" section:
note the fixing commit `44629e3`, set "Fixed in version" to 5.2.0.
