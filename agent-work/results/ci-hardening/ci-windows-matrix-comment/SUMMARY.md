# Item 2 (comment half) — Correct the stale gramps60 matrix comment

**Branch:** `ci-windows-matrix-comment` (off `main`) · **Patch:** `patch.diff`

This is the unambiguous, addon-independent half of the brief's Item 2b
("delete the stale comment"). Split out from the `addons_ref` change because
that change is now decision-required (see `results/ci-addon-ref-gramps60/`)
and this correction shouldn't be blocked by it.

## Root cause
`windows-unit-tests.yml:47-48` justified the Windows core matrix excluding
gramps60 by claiming "this matrix diverges from unit-tests.yml (Linux still
tests gramps60)". `unit-tests.yml:50` has a gramps61-only matrix — the
gramps60 cell was removed at some point and this comment was never updated.
The parenthetical is simply false.

## Change
Reword the comment to state gramps60 is not Windows-eligible (UCRT64 + the
BSDDB-on-Windows skip landed on gramps61/master only) and note that Linux is
gramps61-only now too. **Comment-only — the matrix itself is unchanged.**

## Files
- `.github/workflows/windows-unit-tests.yml` (comment lines only).

## Verified against
- `unit-tests.yml:49-50` — `gramps_ref` matrix is `maintenance/gramps61` only
  (no gramps60 cell), contradicting the old comment.
- `windows-unit-tests.yml:50-52` — matrix is `gramps61 + master`, untouched.

## Verification
- `actionlint .github/workflows/windows-unit-tests.yml` → exit 0.

## What this proves / leaves unproven
- **Proves:** YAML still valid; the matrix is byte-identical (diff is
  comment-only).
- **Leaves unproven:** nothing of substance — this is a comment fix.
