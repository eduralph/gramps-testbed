# Mantis 13736 — Addon Registration Failed dialog gives no diagnosis

## Verdict
**FIX SHIPPED** — improved `OkDialog` message in `AddonManager.install_addon`
to name the failing addon, the running Gramps major.minor, and point the
user at `Edit → Preferences → Addon Manager → Projects` (the canonical fix
location when the dialog fires because a stale 5.x project URL targets a
catalogue with a different `gramps_target_version`).

## Branch + PR
- **fork branch:** `eduralph/gramps:fix/bug-13736-addon-registration-failed-msg`
- **target:** `gramps-project/gramps:maintenance/gramps61`
- **status:** committed and pushed; **draft PR not yet opened** (Eduard opens upstream PRs)

## Files
- `gramps/gui/plug/_windows.py` — message text + `major_version` import
- `gramps/gui/plug/test/windows_test.py` — new headless regression test
  using `__new__`-bypass on `AddonManager` and `patch.object` on `OkDialog`

## Test
Test passes locally via the testbed `scripts/ubuntu/run-unit.sh`. The
test asserts the dialog text contains the failing `addon_id`, the running
`major_version`, and "Projects". A sanity case asserts the dialog is
**not** raised on the happy path.

## Manual work
None — fully automated regression test ships with the PR.
