# CLAUDE CODE BRIEF — CI hardening, decisions resolved (v3)

> Follow-up to the v2 brief's IMPLEMENTATION RESULTS. v2 implemented nine
> items; three reached a DECISION/deviation and stopped for Act. Act has
> adjudicated. This brief implements those decisions. Same conventions:
> testbed `main`, one logical change → one PR, draft-only, cite path:line,
> honest "proves X / leaves Y unproven", `results/ci-<slug>/{SUMMARY.md,
> patch.diff}`, STOP after each. Nothing pushed, no PRs opened.

## Decisions ledger (what Act settled, and why)

| Open item from v2 results | Act decision | This brief |
|---|---|---|
| 2b — addon `addons_ref` flip (you declined: "incoherent 61/60 pair") | **Flip `addons_ref`→gramps60, keep `gramps_ref`→gramps61** — for a reason the v2 brief did not give | Item A |
| 2 #3 — analyzer branch (you recommended gramps61, unimplemented) | **Ratify gramps61** | Item B |
| 3 — regex vs exec-shim deviation | **Accept the regex deviation; do NOT revert** | Item C |
| 1, 4, 5, 6, 8 (done) | Accept; await Eduard dispatch runs | Item D (record only) |
| 7 (partial) | Accept partial; local-action path needs a dispatch run | Item D (record only) |

---

## Item A — flip `addons_ref`→gramps60, keep `gramps_ref`→gramps61

**Verify the basis FIRST — this overrides your own v2 decline.** Two facts
were established that change the picture you decided against:

1. **`maintenance/gramps61` exists on `addons-source`** (`git ls-remote
   --heads https://github.com/gramps-project/addons-source.git` →
   `maintenance/gramps61` = c2799bc, alongside `maintenance/gramps60`). So a
   61-core/60-addon pairing is not a phantom-branch case; both addon
   branches are real.
2. **The job header states the purpose:** `addon-unit-tests.yml`'s schedule
   comment says it exists to surface "addon-side import/ABI regressions
   against fresh upstream … while addons-source's own CI stays green."

The reasoning Act drew from those facts (confirm it yourself before
editing): addons-source's gramps60 CI tests 60-addon/60-core, its gramps61
CI tests 61-addon/61-core — both green. The testbed's stated job is to catch
the gap *between* them: the as-authored **gramps60 addon against fresh
gramps61 core**, the pairing neither addons-source CI runs. Status-quo
61/61 duplicates addons-source's gramps61 CI and tests the *already
forward-ported* addon, so it cannot be an early warning. The "ships
nowhere" property of 61-core/60-addon is the point of a forward-compat test,
not a defect.

**If, after verifying both facts and re-reading the header, you still judge
the flip wrong — STOP and write why in SUMMARY.md instead of implementing.**
This is a genuine override of your prior call; it should survive your own
re-check, not just Eduard's say-so.

**Change (if the basis holds).**
- In `addon-unit-tests.yml` and `windows-addon-unit-tests.yml`, change the
  `addons_ref` default from `maintenance/gramps61` to `maintenance/gramps60`
  (v2 results cited `addon-unit-tests.yml:30` and `:71`,
  `windows-addon-unit-tests.yml:24` — confirm current lines).
- **Leave `gramps_ref` at `maintenance/gramps61`.** The flip is addon-only;
  the pairing is deliberately cross-version.
- Rewrite the adjacent comments so the pairing is **self-documenting**:
  state that this job pairs the as-authored gramps60 addon against fresh
  gramps61 core to catch pre-cherry-pick forward-compat breakage that
  addons-source's own CIs cannot. This is the anti-drift requirement — the
  next audit must read this as intent, not divergence.
- One PR. Do not touch the core-test jobs (`unit-tests`, `interface-tests`,
  `windows-unit-tests` stay gramps61 — correct as-is).

**Verify.** `actionlint` (+ shellcheck) clean. Confirm by inspection that
`gramps_ref` is unchanged and only `addons_ref` moved, in both addon jobs.
State plainly: actionlint proves the YAML; it does **not** prove the 60/61
pairing actually builds — that needs a `workflow_dispatch` (Eduard's step).
Note in SUMMARY.md that the gramps60 addon branch must be the one whose
tests run, i.e. the checkout resolves `maintenance/gramps60` of
addons-source.

---

## Item B — analyzer branch → gramps61 (dev-tooling)

**Decision ratified:** the analyzers are core-subject — they scan gramps
core source and their findings become *core* PRs, which target gramps61. So
the analyzer job should analyze the branch core fixes land on.

**Change.** In `dev-tooling.yml`, change the analyzer target default from
`maintenance/gramps60` to `maintenance/gramps61` (v2 results cited
`dev-tooling.yml:61` — confirm). Add a comment stating the reasoning: this
job is core-defect analysis (pyright/semgrep against gramps core), distinct
from the addon-conformance jobs; its findings are core PRs → gramps61.

This is a separate PR from Item A (different job, different rationale; one
logical change each).

**Verify.** `actionlint` clean. Inspection that only the analyzer default
moved and the addon/core-test jobs are untouched.

---

## Item C — ratify the regex extractor (no code change)

**Decision: the regex + `literal_eval` deviation on `ci-requires-mod-
extractor` is accepted. Do NOT revert to the exec-shim.** The basis: you
checked all 14 real `requires_mod` in addons-source and every one is a flat
literal, so the exec-shim's sole justification (computed/concatenated
declarations) is empirically moot, while its costs (arbitrary-code surface,
a second scanning paradigm inconsistent with the sibling
`addon_system_deps.py`) are real. The spec's exec-shim requirement was
wrong; reality falsified it.

**Action:** none on the code. Append one line to that item's `SUMMARY.md`
recording the deviation as **ratified** (not pending), citing the 14/14
literal finding as the falsifying evidence, so the decision is captured
where the next reader will look. Keep the 6 unit tests and the byte-identical
output check as the regression guard.

---

## Item D — record-only (no code this brief)

These need Eduard, not you. Consolidate them into the batch `SUMMARY.md`'s
top so the human queue is in one place; do not act on them:

- **Awaiting `workflow_dispatch` (Eduard runs; you did not and do not):**
  - Item 1 — end-to-end sync, which depends on the `FORK_SYNC_TOKEN` PAT
    scope covering the current owner's fork repos (caveat A — the silent
    breaker).
  - Item 4 — the all-skipped guard path on a real Windows runner.
  - Item 5 — cancellation semantics on a PR branch vs `main`.
  - Item 7 — the `./gramps-testbed/.github/actions/compile-gramps-mo` local-
    action path: actionlint neither validates nor rejects it, so a dispatch
    run is the only proof it resolves.
  - Item A (this brief) — the 60-addon/61-core pairing actually builds.
- **Deferred (decision-required, not this brief):** Item 7's
  `setup-gramps-venv` (Ubuntu/MSYS2 body divergence) and the repo-resolution
  composite (matrix-vs-variable caller shapes) remain unextracted.

---

## Branch / PR summary for this brief

- Item A → one PR (e.g. `ci-addon-ref-gramps60`, reusing or replacing the
  comment-only branch noted in v2 results).
- Item B → one PR (`ci-analyzer-branch-gramps61`).
- Item C → no PR; a one-line append to the existing extractor item's
  SUMMARY.md.
- Item D → no code; record in the batch SUMMARY.md.

STOP after writing results. No push, no PR open, no ready-mark.
