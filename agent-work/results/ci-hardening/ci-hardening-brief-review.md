# Review — CI hardening brief (gramps-testbed)

**Reviewer:** Claude Code (in-repo)
**Date:** 2026-06-01
**Subject:** `CLAUDE_CODE_BRIEF-ci-hardening.md` (produced by Claude in Projects)
**Method:** Spot-checked every load-bearing factual claim against the
workflows on `main` before assessing. Claims cited `path:line` below.

---

## Verdict

Green-light with two pre-implementation caveats (Item 1 owner check, Item 2
must also reconcile `CLAUDE.md`). The brief is accurate, well-scoped, and
respects the repo's conventions (one-PR-per-item, draft-only, cite
`path:line`, honest "proves X / leaves Y unproven" framing). It correctly
isolates Item 2 as DECISION-REQUIRED rather than guessing a policy — which is
the right call, since a wrong default is what caused the drift in the first
place.

It is *not* built on a stale premise — the usual failure mode for an audit
hand-off. All five factual claims I checked hold.

---

## Verification log

| Item | Claim | Status | Evidence |
|------|-------|--------|----------|
| 1 | `eduralph` hardcoded in upstream-sync | ✓ confirmed | `upstream-sync.yml:33`, `:35` (matrix `owner:`), plus comments `:17–18`, `:53`. All other workflows use `github.repository_owner`. |
| 2 | `addons_ref` defaults to gramps61; dev-tooling defaults to gramps60 | ✓ confirmed | `addon-unit-tests.yml:30` + `:71`, `windows-addon-unit-tests.yml:24`, `interface-tests.yml:81` → `maintenance/gramps61`; `dev-tooling.yml:61` → `maintenance/gramps60`. |
| 3 | `requires_mod` logic duplicated in both addon workflows | ✓ confirmed | Present in `addon-unit-tests.yml` and `windows-addon-unit-tests.yml`. `scripts/lib/addon_system_deps.py` exists as the sibling precedent the brief names. |
| 4 | Coverage guard only on Linux addon job | ✓ confirmed | `junit_coverage` referenced only in `addon-unit-tests.yml`; zero hits in `windows-addon-unit-tests.yml`. |
| 5 / 6 | No `concurrency` anywhere; `dev-tooling.yml` has bare `push:` | ✓ confirmed | No `concurrency:` in any workflow. `dev-tooling.yml` `on: push:` has no `branches:` filter; all seven others use `push: branches: [main]`. |

---

## Why the current state exists (intentional vs. drift)

The single most useful thing for review is knowing whether each "divergence"
is **deliberate design** (don't touch it) or **accidental drift** (the brief's
fix is correct). I read the rationale embedded in the workflow comments and
`CLAUDE.md` to classify each. This is where the brief is slightly too uniform —
it treats everything as drift, and at least one item isn't.

### Item 1 — hardcoded `eduralph`: **drift, but with a load-bearing reason it was missed**
The hardcoding isn't arbitrary. `upstream-sync.yml:6–18` documents that this
workflow exists *because* the forks carry a no-bypass "PRFirst" ruleset, so it
must open a PR rather than fast-forward, and the `FORK_SYNC_TOKEN` is
explicitly "scoped to `eduralph/gramps` + `eduralph/addons-source`"
(`:17–18`, `:51–53`). So the whole file — matrix owner, header, token-scope
note, and the *actual PAT scope in GitHub settings* — was written as a matched
set assuming owner = `eduralph`. That's why it didn't track the rename: it was
never parameterised in the first place, unlike the test workflows.
→ **Consequence for the fix:** swapping to `github.repository_owner` only works
if the PAT's scope was *also* updated to the new owner's fork repos. The YAML
edit and the secret are coupled. This is the mechanism behind caveat A — it's
not a hypothetical.

### Item 2 — branch-target defaults: **partly intentional, partly drift — do NOT flatten to "make them all agree"**
This is the item where uniform treatment is actively misleading:
- `unit-tests.yml` / `interface-tests.yml` / `windows-*` run **gramps core**
  to verify the testbed harness against current *production* core →
  `maintenance/gramps61` is correct and deliberate (the Windows comment at
  `windows-unit-tests.yml:46–50` even explains gramps60 is excluded because
  the BSDDB-skip landed on gramps61 only).
- `dev-tooling.yml:61` defaults its target to `maintenance/gramps60` — but this
  job is **not a test job**. Its header (`dev-tooling.yml:6–12`) says it runs
  the pyright+semgrep shape/flow analyzers against the gramps **source** to
  feed *agent-work/addon* work. Triage and addon fixes historically target
  gramps60. So this default may be **correct-by-purpose**, not drift — it
  analyses the branch where those fixes land, which is legitimately different
  from where the harness tests run.
- The genuine drift is narrower: `addons_ref` defaulting to `gramps61` in the
  addon-unit jobs, when addon code is authored against a different branch; plus
  the stale "Linux still tests gramps60" comment vs. a gramps61-only matrix.
→ **Consequence:** Item 2's decision shouldn't be "pick one branch for
everything." It's "core-test jobs = newest production (gramps61); addon-test
jobs = whatever branch addons target; analyzer job = whatever triage targets —
then make every comment state which and why." That's three reasoned defaults,
not one. And per caveat B, the addon-target ambiguity has to be resolved in
`CLAUDE.md` first or the defaults have nothing authoritative to point at.

### Item 4 — coverage guard missing on Windows: **drift, by sequence not intent**
Nothing documents a reason Windows should skip the all-skipped guard. The
likeliest history: the Linux `junit_coverage.py` guard was added after the
Windows addon job was first written, and the port was never backfilled. The
brief's "wire it identically" is the right shape — there's no design rationale
to preserve.

### Items 5 / 6 — no `concurrency`, bare `push:`: **drift / omission, not design**
`dev-tooling.yml:14–16` has `on: push:` with no `branches:` filter while every
sibling uses `push: branches: [main]`, and the file's own comment claims its
"repo/ref resolution matches the other test workflows" — i.e. it was *meant* to
match the suite, so the missing filter is an oversight, not a deliberate
broaden. No workflow documents a reason to omit `concurrency`. Both are safe to
treat as drift.

### Item 7 — copy-pasted step bodies: **drift the repo's own philosophy predicts**
This is the un-DRY'd surface most at odds with the testbed's stated anti-drift
stance (the same stance that motivates Item 3's single-sourcing). It's
accumulated rather than intended. The brief's caution (split per action, do the
identical-body one first, flag repo-resolution as DECISION-REQUIRED) is right
precisely *because* the three blocks aren't equally identical — the
repo-resolution block legitimately differs between matrix callers and
repo-variable callers (compare `dev-tooling.yml:54–61`'s input→var→default
chain against the matrix form in `unit-tests.yml:66`), so forcing one shape
there *would* be a behavior change, not a refactor.

---

## Caveats to settle BEFORE any code is written

### A. Item 1 — confirm the fork owner tracks the testbed owner
`upstream-sync` pushes to the **fork** repos (`eduralph/gramps`,
`eduralph/addons-source`), not to the testbed. `github.repository_owner` is
the *testbed's* owner. The substitution is only correct if the forks live
under the same owner as the testbed after the rename. Almost certainly true,
but this is the one spot where a wrong assumption silently breaks the sync.
Confirm the fork remotes' owner before editing, not after.

### B. Item 2 — the decision must patch `CLAUDE.md`, not just the YAML
`CLAUDE.md` is itself internally split on the addon target branch: the
"Branch targeting" section says fixes target "the latest `maintenance/gramps*`
(today `maintenance/gramps61`)", while the pre-flight check instructs
`git log upstream/maintenance/gramps60 -- <Addon>/`. That tension *is* the
root cause of the workflow drift. If the Item 2 follow-up only fixes the
workflow defaults and leaves `CLAUDE.md` ambiguous, the drift regenerates.
The decision output must update both.

---

## Per-item notes (refinements, not blockers)

**Item 3 — exec-shim is the right model, but don't oversell the regex weakness.**
Reading each `.gpr.py` through a `register` shim mirrors how Gramps' own plugin
loader reads these files, so it is genuinely more correct than regex. But the
justification leans on "regex misses computed/concatenated declarations,"
which may be theoretical — I'd want one real example from
`addons-source/*/*.gpr.py` before claiming a live bug is fixed. The **drift**
(copy-paste across two workflows) justifies the change on its own. Also state
the trade-off plainly: exec runs arbitrary code (fine for trusted
addons-source, but it should be named).

**Item 5 — blanket `cancel-in-progress: true` will cancel in-flight runs on `main`.**
For PR branches that is exactly the goal; on `main` (post-merge) a fast second
merge cancels the first merge's CI. Usually acceptable for a CI repo, but the
cleaner idiom is:
```yaml
cancel-in-progress: ${{ github.ref != 'refs/heads/main' }}
```
so `main` runs always complete. At minimum, name the choice rather than
defaulting silently.

**Item 7 — correctly flagged as the risky one, correctly split and deferred.**
No objection to the plan. Note that composite actions don't get the same
actionlint depth and add an indirection layer when debugging a red — so the
"diff effective steps before/after" verification is doing real work there, not
ceremony. Keep the repo-resolution extraction last / DECISION-REQUIRED as
proposed.

---

## Gaps the brief doesn't cover

It's a closed list bounded by what the original review found — fair. But two
adjacent hardening gaps are conspicuously absent and belong at least in the
"record, do not fix" appendix:

- **Third-party action pinning.** Are `dorny/test-reporter`,
  `msys2/setup-msys2`, et al. pinned by SHA or floating on a tag?
  Supply-chain-relevant, cheap to check.
- **`timeout-minutes` per job.** Item 5 worries about 30-min Windows/interface
  jobs piling up, but nothing caps a single hung job. A runaway job is the
  other half of that same concern.

Neither needs to be in this batch.

---

## Suggested sequencing

The "work in order, don't bundle" instruction is right; the real dependency
graph:

1. **Item 2 decision first** — it's blocking and it's Eduard's to make.
   Everything reads cleaner once the gramps60/61 policy is settled.
2. **Items 1, 4, 5, 6 in parallel** — independent quick wins (with caveat A
   on Item 1).
3. **Item 3** — self-contained, has a real pass/fail test.
4. **Item 7** — last regardless; one PR per extracted action.

---

## Bottom line

Approve the brief as the work plan. Two things to nail down before code:
the Item 1 owner check (caveat A) and Item 2-also-reconciles-`CLAUDE.md`
(caveat B). The Item 5 `main`-cancellation refinement and the
pinning/timeout appendix are nice-to-haves, not blockers.

---
---

# IMPLEMENTATION RESULTS (v2 brief, 2026-06-01)

The v2 brief was implemented. Each item is on its own branch off `main`
(one logical change = one PR), nothing pushed, nothing merged, drafts not
opened — the review gate is preserved. Per-item `results/ci-<slug>/{SUMMARY.md,
patch.diff}` written. Verification used `actionlint` 1.7.12 **with** shellcheck
0.10.0 on PATH (both installed locally; the brief assumed actionlint only).

## Status table

| Item | Branch | Status | One-line |
|------|--------|--------|----------|
| 1 — fork owner | `ci-fork-owner` | ✅ done | `owner: eduralph` → `github.repository_owner`; actionlint clean; **caveat A unverified** (PAT scope). |
| 2a — CLAUDE.md | `ci-claude-md-branch-targets` | ✅ done | Split Branch-targeting into Core(61)/Addons(60); core rule preserved, **not flipped** (the trap I flagged). |
| 2b — addon `addons_ref`→60 | `ci-windows-matrix-comment` (comment only) | ⚠️ **NOT flipped — DECISION** | Flipping only `addons_ref` makes an **incoherent gramps61-core/gramps60-addon** pair. Stale comment fixed separately. See `results/ci-addon-ref-gramps60/`. |
| 2 #3 — analyzer branch | — | ⚠️ decision | Recommend gramps61; not implemented. `results/ci-analyzer-branch/`. |
| 3 — requires_mod extractor | `ci-requires-mod-extractor` | ✅ done | **Deviation:** regex+`literal_eval` (sibling-consistent), **not** exec-shim. 6 unit tests pass; output byte-identical to old heredoc. |
| 4 — Windows coverage guard | `ci-windows-coverage-guard` | ✅ done | Same `junit_coverage.py` guard as Linux, `cygpath -w` wrapped. |
| 5 — concurrency ×7 | `ci-concurrency` | ✅ done | Conditional `cancel-in-progress` (main protected); upstream-sync excluded. |
| 6 — dev-tooling push | `ci-dev-tooling-push-scope` | ✅ done | `push: branches: [main]`. |
| 7 — compile-gramps-mo | `ci-compile-gramps-mo-action` | ⚠️ partial | **3 Ubuntu callers only** (shell split discovery); venv + repo-resolution **deferred**. |
| 8 — timeout-minutes | `ci-timeout-minutes` | ✅ done | `15` on dev-tooling + upstream-sync; all 8 workflows now capped. |

## The four findings that changed the plan during implementation

1. **Item 2b is not the settled flip the brief (and my v1/v2 review) claimed.**
   doc 16 governs where addon *fork PRs are based* (gramps60) — but the
   testbed's addon-unit CI checks out **both** core (`gramps_ref`) and addons
   (`addons_ref`), and pairs them. Today it's gramps61+gramps61 (coherent).
   Flipping *only* `addons_ref`→60 yields gramps61-core + gramps60-addon, a
   pair that ships nowhere and that addons-source's own CI never tests. The
   job's own header ("import/ABI regressions against fresh upstream… while
   addons-source's own CI stays green") suggests gramps61 may be deliberate.
   → **Not implemented.** Decision doc presents 3 coherent options (status-quo
   61/61; both→60; or a 60/60+61/61 matrix) and a recommendation. I conflated
   "fork-PR base" with "CI pairing" in my earlier review — this corrects it.

2. **Item 3 — used regex, not the exec-shim the brief specified.** Every real
   `requires_mod` in addons-source (14 of them) is a flat literal, the sibling
   `addon_system_deps.py` and the old heredoc both use regex+`literal_eval`,
   and an exec-shim would add an arbitrary-code surface + a second scanning
   paradigm. Documented as a deliberate, reversible deviation.

3. **Item 7 — the msgfmt loop is NOT "identical everywhere" in the way that
   matters.** Its 5 callers span two shells (3 bash, 2 `msys2 {0}`), and a
   composite step's `shell:` is a literal that can't be the caller's msys2
   default. So one action can't serve all five; I extracted the 3 Ubuntu
   callers and left Windows inline. `setup-gramps-venv` (bigger Ubuntu/MSYS2
   body divergence) and repo-resolution are deferred as decision-required.

4. **New sub-question raised (not in the brief):** even option (b) for Item 2b
   would need `gramps_ref` *and* `addons_ref` to move together — the brief only
   considered `addons_ref`. Captured in the decision doc.

## What is verified vs. what needs Eduard

- **Verified locally:** all `actionlint` clean (no new warnings vs `main`);
  Item 3's 6 unit tests pass and its output matches the old heredoc byte-for-
  byte; guard/shell parity confirmed by inspection.
- **Needs a `workflow_dispatch` run (Eduard — I did not trigger any):**
  Item 1 end-to-end sync (PAT scope), Item 4 all-skipped path on a real
  Windows runner, Item 5 cancellation semantics, and **Item 7's
  `./gramps-testbed/.github/actions/…` local-action path** — actionlint
  neither validates nor rejects it, so a dispatch run is the only proof it
  resolves.
- **Needs a decision (Eduard):** Item 2b pairing, Item 2 #3 analyzer branch,
  and whether to revert Item 3 to the brief's exec-shim.

## Git state
9 local branches (`ci-*`), all off `41d611f`. Nothing pushed; no PRs opened;
working tree on `main` is unchanged apart from the untracked `results/` tree
and this file. The pre-existing uncommitted `wiki/` WIP was never touched. A
repo-local git identity (`eduard@ralphovi.net`) was set so the per-item commits
could be made.

---
---

# V3 DECISIONS — IMPLEMENTED (2026-06-01)

The three v2 items that stopped at a DECISION/deviation were adjudicated and
implemented. Branches off `main`; nothing pushed.

| Item | Branch | Result |
|------|--------|--------|
| A — addon pairing (was 2b) | `ci-addon-ref-gramps60` | ✅ `addons_ref`→gramps60, **`gramps_ref` kept gramps61**; self-documenting comments. |
| B — analyzer branch (was 2 #3) | `ci-analyzer-branch-gramps61` | ✅ dev-tooling default gramps60→gramps61 (active + disabled CodeQL example). |
| C — regex extractor (was 3) | `ci-requires-mod-extractor` | ✅ deviation **ratified** in SUMMARY; no code change. |

Consolidated Eduard queue (dispatch runs + deferred items): see
`results/ci-decisions-v3/SUMMARY.md`.

## On Item A — I reversed my own v2 decline, on purpose
v2 I declined "flip only `addons_ref`" as an incoherent 61-core/60-addon pair.
The v3 brief supplied the rationale v2 lacked, and I re-verified it before
editing (the brief's STOP-if-still-wrong gate did not trigger):
- `maintenance/gramps61` is a real addons-source branch (`c2799bc`), so the
  pairing isn't a phantom-branch case;
- the job's purpose (header) is forward-compat early-warning, and the
  gramps60-addon/gramps61-core pairing is the **one config neither
  addons-source CI runs** — "ships nowhere yet" is exactly what a forward-compat
  test exercises. My v2 objection was answered, not overruled.

**Honest nuance I recorded (not a blocker):** status-quo 61/61 wasn't a *pure*
duplicate of addons-source's gramps61 CI (that tests *released* core; the
testbed tests *fresh* source), so the flip trades a fresh-core-regression
signal for the forward-compat signal. A coherent `{60/61, 61/61}` matrix keeps
both — flagged for later, out of scope for a one-change PR.

## Where my earlier review was wrong, and why it matters
My v1/v2 review endorsed "Item 2 is settled (addons→gramps60)" by reading doc 16
— but I conflated **where addon fork PRs are based** (gramps60, doc 16, true)
with **what the testbed CI should pair** (a separate coverage question doc 16
doesn't govern). v2-implementation caught the conflation and stopped; v3
resolved it with the missing forward-compat rationale. The end state is correct
*and* now self-documented in the workflow comments, so the next audit reads the
cross-version pairing as intent.

## Full branch inventory (11 branches, one logical change each)
`ci-fork-owner`, `ci-claude-md-branch-targets`, `ci-windows-matrix-comment`,
`ci-requires-mod-extractor`, `ci-windows-coverage-guard`, `ci-concurrency`,
`ci-dev-tooling-push-scope`, `ci-timeout-minutes`, `ci-compile-gramps-mo-action`
(v2) + `ci-addon-ref-gramps60`, `ci-analyzer-branch-gramps61` (v3). All off
`41d611f`; nothing pushed; no PRs opened.
