# Item 4 — Port the degraded-coverage guard to the Windows addon job

**Branch:** `ci-windows-coverage-guard` (off `main`) · **Patch:** `patch.diff`

## Root cause
`addon-unit-tests.yml:265-270` reads `scripts/lib/junit_coverage.py` after each
addon's xmlrunner run and fails the addon when **every** test skipped (a
wholly-skipped module exits 0, so exit-code-only would call it PASS).
`windows-addon-unit-tests.yml` checked only the xmlrunner exit code
(`) || fail=1`), so a Windows addon whose `requires_mod` failed to install and
whose tests all `skipUnless`-skip reported **green** — a false pass. Drift by
sequence: the guard was added to Linux after the Windows job was written and
never backfilled.

## Change
In the Windows "Run addon unit tests" per-addon loop:
- capture the xmlrunner result into `rc` (`) || rc=$?`) instead of
  `) || fail=1`, so the coverage read happens regardless of exit code;
- `read -r t s < <(python <junit_coverage.py> <out_dir>)` and apply the
  identical `rc != 0 → fail` / `t>0 && s==t → fail` logic the Linux job uses;
- wrap both the script path and `out_dir` in `cygpath -w` — the MSYS2-native
  Python reads Windows paths, the same reason the existing `xmlrunner -o` does.

The inverted filename filter (`test_linux_*`/`test_integration_*` skipped) and
all other `cygpath` handling are untouched.

## Verified against
- `addon-unit-tests.yml:248-271` — the Linux pattern (`rc=0; (...) || rc=$?;
  read t s; if rc!=0 fail; elif t>0 && s==t → ::error + fail`). The Windows
  guard now uses the **same script** and the **same threshold**
  (`[ "${s:-0}" -eq "${t:-0}" ]`).
- `scripts/lib/junit_coverage.py` — prints `<total> <skipped>` summed over
  `*.xml` in the dir; unchanged, now consumed by both jobs.
- `windows-addon-unit-tests.yml:263` — the pre-existing `cygpath -w "$out_dir"`
  on the xmlrunner `-o`, confirming MSYS2 Python needs Windows paths here.

## Verification
- `actionlint .github/workflows/windows-addon-unit-tests.yml` → exit 0 (no
  warnings; the file has none, before or after).
- Side-by-side grep confirms identical guard text (`all ${t} tests skipped
  (degraded coverage)`, `-eq "${t:-0}"`) in both jobs.

## What this proves / leaves unproven
- **Proves:** the guard is wired identically to the working Linux one (same
  script, same threshold), and the YAML is valid.
- **Leaves unproven:** the all-skipped path actually firing on Windows — that
  needs a Windows runner (`workflow_dispatch`, Eduard's step), including that
  MSYS2 Python resolves the `cygpath -w` script path and that process
  substitution `< <(...)` behaves under `shell: msys2 {0}`. The local check
  proves wiring parity, not a live Windows run.
