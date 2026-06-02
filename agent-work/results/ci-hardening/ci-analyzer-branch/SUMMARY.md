# Item 2 #3 — `dev-tooling.yml` analyzer branch default — DECISION REQUIRED (recommendation only)

**No patch.** Per the brief, this sub-question is Eduard's call; this doc
presents both readings and recommends one. Not implemented.

## Current state
`dev-tooling.yml:61` resolves the analyzer target as
`input -> vars.GRAMPS_REF -> maintenance/gramps60` (the same input→var→default
chain the test workflows use, but with a gramps60 tail). The job runs
pyright + semgrep shape/flow analyzers against the gramps **source** checked
out at that ref (`dev-tooling.yml:6-12` header; `:54-61` resolve step).

## The two readings
- **(a) Current gramps60 is correct.** The analyzer feeds agent-work/addon work,
  which historically centred on gramps60; analysing that branch matches where
  those fixes land.
- **(b) gramps60 is drift; should be gramps61.** The analyzers scan **core**
  source (`gramps/gui/**` disposal/None-flow classes), and their findings
  become **core** PRs. Per the ratified targeting rule (Item 2a; jralls#2298)
  core fixes target `maintenance/gramps61`. Two corroborating facts:
  - The local workspace fork `../gramps` is on `maintenance/gramps61`
    (`CLAUDE.md:7`), and the `analyze` skill runs against that — so CI's
    gramps60 default already diverges from where the analyzer is run locally.
  - A finding produced against gramps60 source would be fixed on gramps61,
    where the surrounding code can differ — the same cross-branch-correctness
    trap `CLAUDE.md` warns about elsewhere.

## Recommendation: **(b) — change the default to `maintenance/gramps61`.**
The analyzer's output is core PRs, core targets gramps61, and the local
analyzer already runs on gramps61; keeping CI on gramps60 means analysing a
branch nobody will land the fixes on. The only thing that makes (a) tempting
is history, and the gramps61 production cutover superseded it.

**Caveat / left to Eduard:** if there's a deliberate reason the CI analyzer
tracks the addon/triage branch rather than the core-fix branch (e.g. a triage
workflow that specifically wants gramps60 line numbers), that overrides this.
Confirm before changing. If approved, it is a one-line change to
`dev-tooling.yml:61` (`maintenance/gramps60` → `maintenance/gramps61`),
**its own small PR**, not folded into any other item.
