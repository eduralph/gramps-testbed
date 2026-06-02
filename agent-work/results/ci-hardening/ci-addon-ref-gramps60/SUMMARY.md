# Item A (v3) — Pair gramps60 addons against gramps61 core (addon-unit jobs)

**Branch:** `ci-addon-ref-gramps60` (off `main`) · **Patch:** `patch.diff`
**Supersedes the v2 decision doc** that declined this flip. The v3 brief
supplied the rationale v2 lacked; I re-verified it and reversed my prior call.

## What changed my v2 decline
v2 I declined "flip only `addons_ref`" as an incoherent gramps61-core/
gramps60-addon pair that "ships nowhere." The v3 basis reframes that as the
*point*, and I re-verified both facts before editing:
1. **`maintenance/gramps61` exists on addons-source** —
   `git ls-remote ... addons-source` → `maintenance/gramps61` = `c2799bc`
   (alongside `maintenance/gramps60` = `771db58`). So 61-core/60-addon is a
   real-branch pairing, not a phantom.
2. **The job header states the purpose** — `addon-unit-tests.yml:10-12`:
   surfaces "addon-side import/ABI regressions against fresh upstream … while
   addons-source's own CI stays green."

The pairing addons-source's CIs do NOT run is exactly **as-authored gramps60
addon against fresh gramps61 core**: their gramps60 CI runs 60-addon/60-core,
their gramps61 CI runs the *already forward-ported* 61 addon. So this job is
the only place the pre-cherry-pick forward-compat break shows up. "Ships
nowhere yet" is what a forward-compat test is supposed to exercise. After this
re-check I judge the flip correct, so I implemented it (the brief's STOP-if-
still-wrong condition did not trigger).

## Change
- `addon-unit-tests.yml` + `windows-addon-unit-tests.yml`: `addons_ref` default
  (input default **and** the checkout `||`-fallback) `maintenance/gramps61` →
  `maintenance/gramps60`.
- **`gramps_ref` left at `maintenance/gramps61`** in both — the pairing is
  deliberately cross-version.
- Adjacent comments rewritten to make the pairing self-documenting ("Do NOT
  fix this to 61/61 …") so the next audit reads intent, not divergence.
- Core-test jobs (`unit-tests`, `interface-tests`, `windows-unit-tests`)
  untouched — gramps61 is correct there.

## Verified against
- `addons-source` `maintenance/gramps61` @ `c2799bc`, `maintenance/gramps60` @
  `771db58` — both addon branches real.
- `addon-unit-tests.yml:10-12` — the "fresh upstream / addons-source CI stays
  green" purpose statement.
- `16-guidelines.md:111-114` — addons authored on gramps60, maintainer
  cherry-picks forward (the reason gramps60 is the as-authored branch).
- Diff inspection: per file, only the two `addons_ref` lines moved; every
  `gramps_ref` line shows as unchanged context.

## Verification
- `actionlint` (+ shellcheck) on both workflows → no new findings (only the
  pre-existing SC2046/2206/2295 in unrelated blocks remain).
- `gramps_ref` confirmed unchanged (no `-` line touches it in the diff);
  both `addons_ref` checkout fallbacks now read `maintenance/gramps60`.

## Honest trade-off this records (not a blocker)
Status-quo 61/61 was **not a pure duplicate** of addons-source's gramps61 CI:
addons-source tests against a *released* gramps, the testbed against *fresh*
source, so 61/61 also caught fresh-core regressions against the *shipping* 61
addon. The flip trades that signal for the forward-compat signal. If both are
wanted later, a coherent matrix `{60-addon/61-core, 61-addon/61-core}` is the
path — out of scope for this one-logical-change PR, noted for the record.

## What this proves / leaves unproven
- **Proves:** YAML valid; only `addons_ref` moved; the pairing is now
  documented as intentional.
- **Leaves unproven:** that the gramps60-addon/gramps61-core combination
  actually checks out and builds (the gramps60 branch of addons-source is the
  one whose tests run). That needs a `workflow_dispatch` on both addon jobs —
  Eduard's step; not triggered. Expect some advisory reds if real
  forward-compat gaps exist — that is the signal, and the jobs are
  `continue-on-error` so they don't block merges.
