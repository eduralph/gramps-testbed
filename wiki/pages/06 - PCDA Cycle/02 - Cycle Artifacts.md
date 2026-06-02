---
title: "Cycle Artifacts (operational layer)"
categories: []
managed: false
status: active
---

> One level below [[01 - The Quality Cycle]]. Defines the concrete
> artifact each PDCA beat produces, who writes it, and the handoff
> contract between beats. The through-line: Do and Check assemble one
> **result document** that ends in a Check sign-off (the per-
> contribution verdict); Act runs *across* completed cycles' result
> documents to identify process deltas. Extends the
> `results/issue_<id>/` bundle pattern with the Check-layer artifacts
> (gate report, advisory verdict) and adds a separate process-level
> Act log. Living document.

## Artifact flow

```
PLAN  ── writes ──▶  brief.md                 (the contribution spec)
                         │
DO    ── reads brief, writes ──▶  patch.diff + test + build-notes.md
                         │
┌─ CHECK (one beat, three components) ──────────────────────────────┐
│  ① gates    ── writes ──▶  check-gates.{md,json}                  │
│  ② reviewer ── writes ──▶  check-review.md                        │
│  ↓                                                                 │
│  driver assembles SUMMARY.md from brief + gates + review           │
│  ↓                                                                 │
│  ③ sign-off completes the beat; verdict recorded in §9:           │
│       accept          ──▶ mark PR ready / merge → cycle complete  │
│       iterate-to-Do   ──▶ rebuild (back to DO with same brief)    │
│       iterate-to-Plan ──▶ revise brief (back to PLAN, same cycle) │
└────────────────────────────────────────────────────────────────────┘
                         │
                         ▼
         (cycle complete — bundle frozen, ready for Act review)
                         │
                         ▼
ACT   ── periodically, across N completed cycles, reads their
         bundles + each §10 Act-candidate hints, writes ──▶
         process/act-log.md  (process deltas: ruleset/template/
                              gates/skills adjusted)
                         │
                         ▼
              improved baseline → next PLAN
```

The per-contribution bundle ends at Check sign-off. Act is a separate,
cross-cycle pass; it does not block the contribution from shipping or
closing. The bundle is the durable record Act reads from later.

Each per-cycle file lives in `results/issue_<id>/`. The result document
is `SUMMARY.md`; everything else is either its input or a ready-to-ship
attachment it references. The Act log lives outside the per-issue
bundle, at a project-level path (e.g. `process/act-log.md`), and cites
the bundles it draws on.

---

## PLAN → `brief.md` (the contribution spec)

Authored by **you** (or a planning chat). It is the spec plus the
marching orders, drawn from the *current* process baseline (templates,
ruleset, branch-target rules) that Act maintains.

**The Plan artifact's shape scales with the work.** For a one-fix
contribution (the common case), Plan writes one `brief.md` against the
fields below. For a coordinated multi-part contribution — an
architectural change, a phased migration, a design-proposal-shaped
piece of work — Plan instead writes a **design proposal** (e.g.
`design.md`, `GEPS-NNN.md`, an RFC) that *itself spawns N child
briefs*. The design proposal has its own structure
([[01 - The Quality Cycle]] §Solution-approach design: Goals/Non-goals,
Decomposition into independently-landable parts, Phased migration with
safe stall points, Objections and responses, Impact assessment,
De-risking, Open questions, Future Work), and goes through its own
review cycle before any child brief is authored. Each spawned child
brief then follows the per-fix `brief.md` spec below.

Both shapes flow through the same downstream beats — Do, Check,
Act — without modification; only the Plan-side artifact differs.

**Required fields (one-fix `brief.md`):**

- **Spec — the defect and the success criterion.** What is wrong, and
  the observable condition that means it is fixed. This is the thing
  Check verifies against; if it is vague, Check cannot adjudicate.
- **Repo + branch target, resolved.** Decided here, not left to Do.
  (Resolve cross-repo ambiguity by reproducing if the traceback location
  is unclear.)
- **Scope — one logical fix.** State it, and state what is explicitly
  out of scope, so Check can flag scope creep against a written
  boundary.
- **Repro instruction.** Which fixture, exact steps, on the target
  branch. Repro-or-close is the first action.
- **Test requirement.** Where the test ships and that it must fail
  pre-fix, pass post-fix.
- **Citations expected.** Do must cite path:line on the target branch
  for every claim and change.
- **STOP discipline.** Draft only until Check sign-off. Push and
  draft-PR-open MAY happen during the cycle (useful for CI feedback);
  MUST NOT mark ready before sign-off accepts.
- **Disposition hint, not verdict.** The Plan-time triage guess
  (POSSIBLY-FIXED → verify first; likely-fix; likely-close). Do/Check
  may override it with evidence.

---

## DO → `patch.diff` + the test + `build-notes.md`

Authored by the **builder** (e.g. Claude Code), production only —
implement, nothing else.

- **`patch.diff`** — the change. MAY be committed and pushed to a
  feature/draft branch; MUST NOT be merged. A draft PR against the
  brief's branch target MAY be opened to let CI exercise the patch.
- **the test** — shipped in the same change, at the location the brief
  named.
- **`build-notes.md`** — the builder's rationale: why this change, what
  was tried, the reasoning. **This file is withheld from the Check
  reviewer** (see Independence contract). It exists for the human
  signing off Check, so the human can see the builder's account *beside*
  the independent verdict, never instead of it.

Do also drafts the spec restatement and disposition-claimed sections of
`SUMMARY.md` (it knows what it set out to do); Check appends the
evidence.

---

## CHECK (gates + reviewer) → `check-gates.{md,json}` + `check-review.md`

The CHECK beat has three components — **gates**, **reviewer**, and
**sign-off** — covered in the next three sub-sections of this doc. The
two artifacts gates and reviewer produce (this section), the
**SUMMARY.md** result document the driver assembles from those
artifacts plus the brief (next section), and the **sign-off** step
that completes the beat (the section after that) together describe
the full CHECK beat. All three components belong to *one* CHECK beat
— not three separate beats. The correctness chain, conformance stack,
and validation act ([[01 - The Quality Cycle]] §5/5/1) run across all
three components.

This first sub-section covers the gates and the reviewer — two
oracles of different trust.

### `check-gates.{md,json}` — deterministic gates

Machine-decided, every row carries its oracle and a path:line.
Correctness chain + conformance Tiers 1–4:

| Check | Result | Oracle | Evidence |
|---|---|---|---|
| repro (red pre-fix) | confirmed / not-repro | fixture on target branch | log / screenshot |
| verification (green post-fix) | pass / fail | the shipped test | log |
| regression | suite green / N broke | existing suite | junit |
| T1 structure | pass / fail | structure validator (rule IDs) | path:line |
| T2 shape | pass / fail | semgrep (rule IDs) | path:line |
| T3 runtime | pass / fail | find_spec / deps-absent run | log |
| T4 contribution | pass / fail | commit-msg hook / branch-target / version-bump | path:line |

A deterministic FAIL with auto-fixable cause (lint, format, genuinely-
red test) may be auto-fixed and re-run; a deterministic FAIL that needs
a decision stops and surfaces to NEEDS-HUMAN.

### `check-review.md` — advisory reviewer (decorrelated)

Produced by the **advisory reviewer** (different model family, e.g.
Codex), from `{patch.diff, test, brief.md, check-gates}` **only** —
never `build-notes.md`. Covers the judgment cells of Check: correctness
causal-adequacy (symptom vs. root cause), conformance Tier-5 scope, and
the validation act (is this the right thing). Its mandate is to
execute, not opine:

- Re-runs the asserted evidence (stash the fix → confirm red; unstash →
  confirm green; re-run the validator and semgrep itself).
- Re-checks that every path:line the builder cited resolves on the
  target branch; drops findings that do not ground.
- Per item emits `PASS / FAIL / NEEDS-HUMAN` with a one-line rationale
  and a path:line. No free-form prose verdict.

Advisory: it annotates, it does not gate. Deterministic gates block;
the reviewer recommends; the human signs off Check.

---

## CHECK (assembled result) → `SUMMARY.md` (what the human signs off)

Assembled across Do (spec + claim) and Check (evidence + verdict). Its
job: let the human complete Check — *clear NEEDS-HUMAN, weigh the
advisory verdict, sign off the disposition* — without re-investigating,
and capture any process-improvement hints for the next Act review.
Required sections:

```
# Result — issue <id> / <slug>

## 1. Spec (from brief.md)              ← Check verifies against THIS
- Defect:
- Success criterion:
- Repo + branch target:
- Scope (one logical fix) / out of scope:

## 2. Disposition claimed               ← sign-off confirms or overrides
- Outcome: Fixed | Already-fixed | Can't-repro | Wontfix | By-design | External
- Confidence: high | medium | low
- Recommendation: merge-wider | close-<reason> | iterate-to-<beat>

## 3. Correctness (Check — chain)
- reproduction / verification / regression / causal-adequacy,
  each: result + oracle + evidence path. Causal-adequacy states the
  root cause and WHY this is cause not symptom (or → NEEDS-HUMAN).

## 4. Conformance (Check — stack)
- T1–T4 deterministic: pass/fail + rule IDs + path:line (from check-gates).
- T5 judgment: → see §5.

## 5. Advisory review (artifact-only, decorrelated)
- Reviewer summary, any FAILs, and the reviewer's RE-RUN results
  (red/green confirmed independently). Produced without build-notes.

## 6. NEEDS-HUMAN — items the human must clear before sign-off
- [ ] <decision only the human can make, and why a gate/reviewer couldn't>
  (empty ⇒ sign-off is a confirm; non-empty ⇒ each item cleared first)

## 7. Proven / not proven                ← oracle limits, stated honestly
- Proven by which oracle:
- Unproven / needs manual run (e.g. specific platform, visual sign-off):

## 8. Ready-to-ship attachments
- patch.diff
- pr-description.md      (only if a PR is warranted)
- tracker-comment.md     (ALWAYS, every tracker item)
- MANUAL-VERIFICATION.md (ANY manual-work outcome; also flagged at top)
- build-notes.md         (builder rationale — for the human signing off,
                          not the reviewer)

## 9. Check sign-off                     ← human completes Check here
- Disposition confirmed / overridden:
- Outcome: merged-wider | closed-<reason> | iterated-to-Do | iterated-to-Plan
- Iteration delta (if iterating): <what the next Do or Plan must change
  for THIS cycle — distinct from process-level Act deltas, which go to §10>
- By / date:

## 10. Act candidates (hints for the next Act review)
- [ ] <process observation flagged for the next Act review>
      Examples:
      - "Spec-template field X was ambiguous — three Do attempts needed."
      - "No rule caught this defect class — candidate for a new Tier-2 check."
      - "The reviewer's grounding step took 3× longer than usual on this
        repo — agent-skill candidate."
  Empty is the common case. The next Act review collects these across
  cycles before deciding any concrete process change.
```

Why these sections, mapped to the question each serves: §1 is the
yardstick Check measures against; §2 is the claim sign-off ratifies or
overturns; §3–4 are the verification evidence (Check's deterministic
product); §5 is the decorrelated second opinion the human weighs beside
the builder's claim; §6 is the heart — the items Check explicitly could
not decide, requiring the human to clear them; §7 stops the human from
over-trusting a green (the oracle-limit honesty); §8 means once sign-off
says "merge wider" there is no rework; §9 records the per-contribution
verdict and, on iterate, the within-cycle delta; §10 is **separate** —
it captures *process* observations that belong to Act, not the
per-contribution disposition.

§9 vs §10 is the boundary the new model insists on. §9 closes the
contribution. §10 is a hint feeder to a downstream Act review that
operates on the *process*. Do not conflate them: a §10 entry is never
required to clear before sign-off; a §9 outcome never decides what
process change to make.

---

## CHECK (sign-off step) → cycle closes, bundle frozen

This is the human-instrumented step that **completes the CHECK
beat** — not a separate beat. The gates and reviewer ran unattended;
the SUMMARY.md was assembled; the human now completes Check by
reading the bundle and signing off §9.

The human completes Check by reading `SUMMARY.md`:

1. Read §1, then §2 — does the claimed disposition match the spec?
2. Clear §6 (NEEDS-HUMAN) — each is a decision the gates and reviewer
   could not resolve: right bug? right spec? root cause or symptom-patch
   dressed as fix? worth doing at all?
3. Weigh §5 (decorrelated review) against §2/§3 — does the independent
   re-run agree?
4. Note §7 — is anything unproven that the disposition depends on?
5. Fill §9:
   - **accept** → merge wider. The push and draft-PR-open may already
     have happened during the cycle; accept performs the steps that
     were gated on sign-off: mark the PR ready, post the §8 tracker
     comment, merge. Cycle closes; bundle is frozen.
   - **iterate-to-Do** → builder re-runs against the same brief, new
     patch. Same cycle, new attempt. Bundle stays open until next
     sign-off.
   - **iterate-to-Plan** → human revises `brief.md`, builder re-runs
     against the new brief. Same cycle, revised spec. Bundle stays open.
6. Optionally fill §10 — note any process observations for the next
   Act review. Empty is normal.

A frozen bundle (sign-off accept) becomes Act material. Act does not
run synchronously on cycle close; cycles close, accumulate, and a
periodic Act review reads across them.

---

## ACT → `process/act-log.md` (process-level, cross-cycle)

Act fires periodically — after N completed cycles, on a calendar, or
on-demand when a pattern surfaces. Its input is **the cycles' record**:
their `SUMMARY.md` files (especially §6, §7, §9, §10), `build-notes.md`,
`check-review.md`. Its output is **deltas to the process baseline**,
recorded in a project-level append-only log.

The log is one file (or one directory of dated entries) at a project-
level path, separate from the per-issue bundles. Suggested name:
`process/act-log.md`. Each entry has:

```
# Act review — <date> — cycles considered: <issue_ids>

## What the cycles' records exposed
- <pattern observed across one or more cycles, with §10/§7/§6 citations>

## Process deltas
- Spec template: <field added / clarified / removed>            (file path)
- Ruleset: <rule added / retired / relaxed / tightened>         (path:line)
- Gates: <check added / promoted to gating / moved to new home> (path:line)
- Agent skills: <SKILL.md / AGENTS.md adjustment>               (path:line)
- Orchestration: <driver / state / queue change>                (path:line)

## How effectiveness will be judged
- The next Do phases should not recreate <specific issue>.
- Watch for it in the next K cycles' records; if it recurs, this Act
  was not effective and the delta needs revisiting.
```

Each delta is **concrete and located** (a path, a rule ID, a template
field) so a future reader — including a future Act review checking its
predecessor's effectiveness — can verify both that the change was made
and that the next cycles did not recreate the issue.

What Act does **not** do:

- Re-decide any contribution's disposition. Check sign-off already
  closed those.
- Run the validator or the suite. Check did.
- Author the next contribution's spec. The *next* Plan does that, with
  Act's improved baseline as its starting point.

---

## Independence contract (operational restatement)

The reviewer's value is decorrelation, and it is enforced by **file
access, not prompt wording**:

- `check-review.md` is generated from `{patch.diff, test, brief.md,
  check-gates}` only. `build-notes.md` is **not** in its inputs — the
  builder's framing must not anchor the reviewer.
- The reviewer has execute access (run tests, run the validator, git
  stash/unstash) and **no write access to the fix** — it physically
  cannot patch what it is judging.
- `build-notes.md` joins the audit packet (§8) for the human only, after
  Check has run, so sign-off sees claim and independent verdict side by
  side.

**What this contract does and does not buy.** File-withholding
decorrelates **evidence-integrity**, not **fix-correctness**:

- *Defends against:* the builder's narrative ("I tried X, ruled out Y,
  this is therefore root cause") anchoring the reviewer's reading of
  the patch. Stash → red / unstash → green confirms the shipped test
  fails pre-fix and passes post-fix, which the reviewer verifies by
  re-running, not by trusting the builder's report.
- *Does NOT defend against:* a plausible test that never actually
  exercises the real bug (the green is true of the test's narrow
  oracle, not of the defect); a framing blind spot the brief and test
  *both* carry into the reviewer (`brief.md` IS in the reviewer's
  input set — your framing of the defect and the success criterion is
  shared between builder and reviewer); causal-adequacy errors
  (symptom vs. root cause) that survive a passing test.

The reviewer attempts causal adequacy (correctness step 5) advisory,
and may flag NEEDS-HUMAN when the evidence is insufficient. **The
human at sign-off is the only real check on causal adequacy** — see
[[06 - Quality Cycle Guidelines]] C6 (§6 must be empty before
sign-off accepts). File-withholding is a useful piece of the
mechanism but not the whole answer to "did this fix really work."

How this is enforced mechanically by the driver is the subject of
[[03 - Cycle Automation]] §Independence is enforced by the orchestrator.

---

## Bundle layout

Per-cycle (`results/issue_<id>/`):

```
results/issue_<id>/
  brief.md               # PLAN  — current contribution spec         (you)
  brief.v1.md            # PLAN  — prior brief version, preserved on
  brief.v2.md            #         iterate-to-Plan (see [[03 - Cycle
  ...                    #         Automation]] §Driver skeleton; only
                         #         present when iterate-to-Plan fired)
  patch.diff             # DO    — the change                        (builder)
  <test file>            # DO    — ships with the patch              (builder)
  build-notes.md         # DO    — rationale, withheld from reviewer (builder)
  check-gates.md|json    # CHECK — deterministic gate results        (gates)
  check-review.md        # CHECK — advisory verdict, artifact-only   (reviewer)
  SUMMARY.md             # DO+CHECK — RESULT DOC, ends in §9 sign-off (assembled)
  pr-description.md       # attachment, if PR warranted
  tracker-comment.md      # attachment, ALWAYS
  MANUAL-VERIFICATION.md  # attachment, any manual-work outcome
```

Versioned-brief discipline: iterate-to-Plan renames the current
`brief.md` to `brief.vN.md` (where N is the next available integer),
then clears every downstream artifact so the next Do re-runs against a
new brief. iterate-to-Do does *not* version the brief — it clears only
the downstream artifacts. The pattern matches the case study's
CLAUDE_CODE_BRIEF v1/v2/v3 sequence ([[07 - Case Study - CI Hardening]] §Turn 2).

Project-level (one location for all cycles' process-level work):

```
process/
  act-log.md             # ACT  — append-only log of process deltas (you)
  spec-template.md       # the current brief.md template Act maintains
  ruleset/               # the current conformance ruleset (Tiers 1–4)
  skills/                # SKILL.md (builder) and AGENTS.md (reviewer)
```

The minimal per-cycle bundle is `SUMMARY.md`, `patch.diff`,
`pr-description.md`, `tracker-comment.md`, `MANUAL-VERIFICATION.md`. The
operational layer above adds `brief.md` (names the Plan artifact
explicitly), `build-notes.md` (separates builder rationale for the
independence contract), and the two `check-*` artifacts (makes Check's
product auditable rather than implicit), and reframes `SUMMARY.md` as
ending in **Check sign-off** (§9), with §10 as a lightweight feeder to
the *project-level* Act log.
