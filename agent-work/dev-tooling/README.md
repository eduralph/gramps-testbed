# Gramps dev-tooling experiment — shape+flow analyzer stack

Goal: catch the recurring bug classes from the fault-line analysis AT AUTHORING TIME,
not after they're filed. Three tools, layered by shape-vs-flow and editor→commit→CI.
This is a LOCAL EXPERIMENT — tune each to high precision in your environment before
proposing any to upstream. "Ready" is measured against the labeled corpus below.

## The stack (bring up in THIS order — each quiet & trusted before the next)
1. **Pylance/pyright** — flow (types), in-editor, instant. Already installed; TUNE it.
   Owns: generic None / Optional-flow (fault-line classes 1 & 3, the type-level subset).
2. **Semgrep** — shape, pre-commit + editor + CI, fast. The custom Gramps patterns.
   Owns: connect-without-disconnect, None-sentinel preallocation (shape-recognizable).
3. **CodeQL** — flow (deep dataflow), CI only, heavy. Add LAST, only for the residual.
   Owns: path-sensitive flow neither other tool reaches (mid-init access, deep None-flow).

## Division of labor (avoid double-reporting)
- Generic None-deref → Pylance owns it (earliest, in-editor). Don't also CodeQL it.
- Shape/convention patterns → Semgrep (Pylance can't express them; not type errors).
- Path-sensitive flow Pylance misses → CodeQL (the residual only).

## Labeled corpus — "ready" is measured against THIS
Positive controls (rule/check SHOULD flag the pre-fix code):
- A2 disposal pattern: 13326 (GalleryTab, pre-fix), 13966 (PrerequisitesChecker, pre-fix),
  13091 (callman=None), 12031 (_save_position None)
- A1 sentinel pattern: fanchart.py pre-fix (the [(None,)*4]*2**i preallocation)
- A3 boundary-null: 13987 (anonymous tag name None → startswith)
Negative controls (check should NOT flag — post-fix / correct code):
- 13326 post-fix (PR 2330), 13966 post-fix (addons#913), fanchart post-fix (PR 2315),
  ce0229fb6f (A3 trio fix — method deleted)
Out-of-scope (NONE of these tools' shape/type layers catch; CodeQL-or-structural only):
- 14177 mid-init (attribute read before __init__ completes — flow, no connect to match)

## "Ready" criteria (define before tuning, or it never converges)
- Flags ALL positive controls in its class.
- Flags ZERO negative controls.
- Zero false positives on a clean pass of gramps/gui/ (precision > recall — this is an
  authoring-time tool; a false positive trains developers to ignore it).
- If a check can't hit zero false positives, NARROW it until it can, even at the cost of
  missing some true positives. Silence-when-unsure.

---

## Layout & setup (this repo)

This stack lives in `gramps-testbed/agent-work/dev-tooling/` and analyzes the **sibling**
`../gramps` fork — same cross-repo convention as the testbed's `additionalDirectories`.
All paths assume invocation from the `gramps-testbed/` repo root.

```
agent-work/dev-tooling/
├── README.md
├── .pre-commit-config.experiment.yaml   # local gate (pyright + semgrep)
├── pyright/
│   ├── pyrightconfig.experiment.json    # include paths are ../gramps-relative
│   └── NOTES_pylance.md
├── semgrep/
│   ├── rules/gramps-connect-without-disconnect.yml
│   ├── tests/gramps-connect-without-disconnect.py   # basename matches rule (--test pairing)
│   └── NOTES_semgrep.md
└── codeql/NOTES_codeql.md               # docs only until the residual flow class is reached

# CI workflow lives at the testbed root, not here:
.github/workflows/gramps-dev-tooling.yml
```

### Run locally

```bash
pip install --break-system-packages pyright semgrep   # Ubuntu workstation

# pyright (scoped None-flow on hot files):
pyright --project agent-work/dev-tooling/pyright/pyrightconfig.experiment.json

# semgrep against real source:
semgrep --config agent-work/dev-tooling/semgrep/rules/ --error ../gramps/gramps/gui/

# semgrep rule self-test (validates positive/negative controls):
cd agent-work/dev-tooling/semgrep && semgrep --test --config rules/ tests/

# pre-commit (both, on commit):
pre-commit run --all-files --config agent-work/dev-tooling/.pre-commit-config.experiment.yaml
```

### Status of the one shipped rule
`gramps-connect-without-disconnect` passes its labeled corpus: flags the `EditCitationLike`
positive (13091/12031 shape), stays silent on the `GalleryTabFixed` negative (13326 post-fix)
and the `EditPrimaryLike` out-of-scope class (14177, no connect). The `pattern-not-inside`
was tightened with a `metavariable-regex` on cleanup-method names; it does **not** yet verify
the disconnected handler id equals the connected one — that's the next refinement (fine for
the one-connect/one-disconnect-per-class corpus).
