# Batch: batch-03-confirmed-velocity — TRIAGED

Two parallel tracks next session:
- **Claude Code:** works the FIX / INVESTIGATE / REPRO-OR-CLOSE items below.
- **Eduard (Mantis, in parallel):** the close-on-tracker items — see MANTIS_ACTIONS.md.

## Disposition table

| ID | Disposition | Track | Note |
|---|---|---|---|
| 13065 | **CLOSE: already fixed** (5.2.0, PR #1530) | Mantis | comment ready |
| 12050 | **CLOSE: by design** (slow not hung) | Mantis | comment ready; opt. abort-button enh. |
| QueryQuickview | FIX: SyntaxError | Claude Code | verdict done; detector-sourced |
| WordleGramplet | FIX: Py2 imap | Claude Code | verdict done; detector-sourced |
| RebuildTypes | FIX: bare `gui` import | Claude Code | verdict done; detector-sourced |
| 14143 | FIX: dark-mode CSS | Claude Code | easy, current, best fast win |
| 13955 | FIX: commented-out URL code + NameError | Claude Code | exact line known (L200) |
| 13059 | FIX: **CORE** selectionwidget set_coords(*None) | Claude Code | exact repro; core-vs-addon |
| 14145 | FIX: stale Geneanet URL (1-line) | Claude Code | EOL question flagged |
| 13420 | INVESTIGATE: repro w/ clean XML → fix or close | Claude Code | clean-XML test is the decision |
| 11658 | REPRO-OR-CLOSE (likely environmental) | Claude Code | NO-NOTES; 5.1.2 Win packaging |
| 12453 | REPRO-OR-CLOSE (likely environmental TLS) | Claude Code | NO-NOTES; NOT a 13065 cluster |
| 12544 | FIX: **JavaScript** (dwr.js OSMPointStyle) | Claude Code | JS not Python; manual verify |
| 11054 | FIX (narrow guard) or DEFER | Claude Code | slowest/riskiest; nick_h's scope only |
| 13736 | FIX low-priority (CORE msg) — REUSE batch-02 | Claude Code | do after fast wins or defer |

## Suggested increment order (fast wins first)
1. **Detector trio** (QueryQuickview, WordleGramplet, RebuildTypes) — import-hygiene sweep,
   surest fixes, no repro risk. BUT first check the PR #820 lint/compile spin-off series —
   some may already be fixed there.
2. **14143 + 13955** — clean located fixes (CSS; commented-out code).
3. **13059** — the real core bug with exact repro (resolve addon-vs-core by reproducing).
4. **14145** — one-line URL (decide EOL question).
5. **Repro-or-close batch: 11658, 12453, 13420** — likely closes; confirm-or-fix.
6. **12544** — JS fix (manual verify).
7. **11054, 13736** — slowest/lowest-priority; defer if velocity matters.

## Cluster note
- The Place Coordinates "cluster" DISSOLVED: 13065 is fixed-and-closing; 12453 is a
  separate (environmental TLS) issue. Do NOT treat as one root cause.
- Detector trio is the one real cluster: same import-hygiene fix shape, one increment.

## Honest expectation
Confirmed: 2 immediate Mantis closes (13065, 12050). Likely: 11658/12453 close as
environmental, 13420 may close as invalid-input. Real fixes: detector trio + 14143 +
13955 + 13059 (+ 14145, 12544). 11054/13736 are defer-candidates. This is a backlog-
shrinking batch as much as a fix batch — expected and fine.

## Checklist
- [ ] Eduard: paste 13065 + 12050 Mantis closes (MANTIS_ACTIONS.md)
- [ ] Claude Code: detector trio (check #820 spin-offs first)
- [ ] Claude Code: 14143, 13955, 13059 fixes
- [ ] Claude Code: repro-or-close 11658, 12453, 13420 (Mantis comments pre-written)
- [ ] Decide 11054 fix-vs-defer; 13736 after fast wins
- [ ] 14145 EOL decision; 12544 JS manual-verify
