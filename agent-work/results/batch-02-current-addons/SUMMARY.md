# Addon-dependency detector — findings (Mantis 13707 class)

**Round:** detector + findings list only. No `depends_on` fixes applied — the
WebConnect remediation is a separate later round on `maintenance/gramps61`.

**Status of this round:** detector built, run, reported. No code committed
or pushed (Eduard's review gate).

**Branch under test:** `eduralph/addons-source` @
`feature/ci-cd-pipeline-upstream` (the PR 820 branch, off
`maintenance/gramps60`).

**Test file (uncommitted):**
`addons-source/tests/test_addon_dependencies.py`

**Detector environment for the canonical results below:** `gramps-ci-local:gramps60-test`
(PR 820's CI image, Gramps 6.0.8). A local Ubuntu run reproduces the same
(a) result — 0 — but its bucket (c) is noisier (host snap-glibc + Gtk-4/3
default ambiguity), which the CI image does not have.

---

## STEP 0 — feasibility result

PASS. The empirical assumption the detector rests on holds:

* **0a (no-deps addon imports cleanly in isolation):** ClockGramplet loads
  in a subprocess with `sys.path = [ClockGramplet/]` and nothing else
  scoped from the addons tree — `rc=0`, module imports.
* **0b (sibling-dep absence fails naming the dep):** USWebPack loaded with
  `sys.path = [USWebConnectPack/]` (libwebconnect NOT on path) fails with
  `ModuleNotFoundError: No module named 'libwebconnect'`.

The approach is viable — proceeded to build the full detector.

---

## How the detector works

1. **Index every `*.gpr.py`** via a private exec-shim (no
   `gramps.gen.plug._pluginreg` import, no `PluginRegister`, no
   `PluginManager`): a permissive globals dict whose `__missing__`
   returns a sentinel, plus a fake `register()` that captures every call's
   kwargs. Builds the addon-provided-module set across the tree and an
   `addon_id → {directory, modules, depends_on, requires_mod, gpr_files}`
   map.
2. **Isolated-load each plugin's registered module(s)** in a fresh
   subprocess (`python3 -I -c ...`, `cwd=/tmp`, `PYTHONPATH` stripped, `""`
   removed from `sys.path` defensively against PEP 420 implicit
   namespace-package leakage) with `sys.path` scoped to the target addon's
   directory plus the directories of its declared `depends_on` (resolved
   via the index). Gramps is reachable from system site-packages, as
   intended — the constraint is addon-from-addon isolation, not
   addon-from-Gramps. Before importing the addon, the subprocess pins the
   GI namespace versions Gramps itself pins (`Gtk` 3.0, `PangoCairo` 1.0,
   `OsmGpsMap` 1.0, `GExiv2` 0.10, `Gspell` 1, `GeocodeGlib` 1.0), matching
   the runtime conditions an addon is loaded under — not using Gramps'
   loader.
3. **Classify each failure.** A failure may name multiple missing modules;
   bucket (a) wins over (b) wins over (c) so the highest-signal finding is
   reported:
   - **(a) undeclared addon dependency** — a missing name is in the
     addon-provided-module set AND not in this addon's declared
     `depends_on`. The Mantis 13707 class. **Counts as a finding; fails
     the test.**
   - **(b) missing requires_mod** — the missing name is in this addon's
     declared `requires_mod`. Environment concern (PR 820's auto-derive
     owns it). **Ignored.**
   - **(c) other** — any other failure. **Reported separately, NOT a
     finding, NOT a test failure.**

### Independence verified end-to-end

A two-addon synthetic tree (`USWebConnectPack` + `libwebconnect`) was
constructed in `/tmp/detector_validation/`:

* With `depends_on=["libwebconnect"]` stripped from `USWebPack.gpr.py`,
  the detector reports bucket **(a) `libwebconnect`** for `US Web Connect
  Pack`.
* With `depends_on=["libwebconnect"]` left in, the detector reports
  `rc=0` (clean load).

The detector both fires when it should and stays quiet when it shouldn't.
(This validation lives under `/tmp/`; it is a one-off check, not a
checked-in test.)

---

## Counts (CI image, gramps60)

| bucket | count |
|---|---|
| indexed plugins | 187 |
| unique registered modules | 182 |
| `.gpr.py` files skipped during exec-shim | 0 |
| isolated-load **pass** | 159 |
| **(a) undeclared addon dependency** | **0** |
| (b) missing `requires_mod` (ignored) | 7 |
| (c) other isolated-load failure (reported, not a finding) | 21 |

---

## (a) Undeclared addon dependencies — the deliverable

**None.** Every WebConnect pack on this branch already declares
`depends_on=["libwebconnect"]`:

```
DEWebConnectPack/DEWebPack.gpr.py:    depends_on=["libwebconnect"],
FRWebConnectPack/FRWebPack.gpr.py:    depends_on=["libwebconnect"],
NLWebConnectPack/NLWebPack.gpr.py:    depends_on=["libwebconnect"],
RUWebConnectPack/RUWebPack.gpr.py:    depends_on=["libwebconnect"],
UAWebConnectPack/UAWebPack.gpr.py:    depends_on=["libwebconnect"],
UKWebConnectPack/UKWebPack.gpr.py:    depends_on=["libwebconnect"],
USWebConnectPack/USWebPack.gpr.py:    depends_on=["libwebconnect"],
```

Mantis 13707 was filed 2025-03-16 by garygriffin against Gramps 6.0.0-rc2.
On the current PR 820 branch (off `maintenance/gramps60`), every pack
already carries the declaration — `git log` shows the line present on
`USWebPack.gpr.py` since at least commit `7c3002157` (PR 640,
"Add help_urls", merged 2025-02-06, *before* the Mantis report). So
the upstream tree on gramps60 was already correct when the bug was
filed; the report likely covers a pre-rc2 snapshot or a state
specific to the reporter's installation.

The detector is the regression check that this stays that way, including
for any future addon that imports a sibling without declaring it. It
detects the **class**, not just the WebConnect packs.

**Implication for the planned remediation round on `maintenance/gramps61`:**
do not apply the presumed-six fix until the detector has been re-run on
the `maintenance/gramps61` tree — that, not the original Mantis enumeration,
is the source of truth for which packs (and possibly other addons) need
the declaration there. This brief's `gramps60` run already removes the
gramps60 packs from the candidate set.

---

## (c) Isolated-load failures for non-dependency reasons

These are **NOT findings** — they fail isolated load for reasons other
than an undeclared addon dependency. Reported here because the signal is
genuine but mixed: some are environmental (the CI image is headless and
does not install every optional native lib), some are real addon-side
defects that show up at module load.

### Environmental — headless CI image (8)

`from gi.repository import Gtk` works, but constructing a `GtkStyleContext`
at module import requires a display:

| addon_id | module |
|---|---|
| HtreePedigreeView | HtreePedigreeView |
| QuiltView | QuiltView |
| TimelinePedigreeView | TimelinePedigreeView |
| combinedview | combinedview |
| graphview | graphview |
| htmlview | htmlview |
| lifelinechartancestorview | lifelinechartview |
| lifelinechartdescendantview | lifelinechartview |

These would clear under Xvfb / a display server — they are not addon bugs.

### Environmental — missing optional GI typelibs (4)

The CI image does not install OsmGpsMap or GExiv2:

| addon_id | module | missing |
|---|---|---|
| Photo Tagging | PhotoTaggingGramplet | GExiv2 typelib |
| geoIDplaceCoordinateGramplet | PlaceCoordinateGeoView | OsmGpsMap typelib |
| geoancestor | GeoAncestor | OsmGpsMap typelib |
| geotimelines | GeoTimeLines | OsmGpsMap typelib |

`requires_gi` declarations would make Gramps' Addon Manager skip these on
install when the typelib is absent. Out of scope for this round.

### Undeclared pip dep — sibling defect, out of scope for this round (2)

Both addons import a pip-installable module at load time without
declaring it in `requires_mod`. Same shape as 13707 (declaration
missing), different axis (addon-from-pip rather than addon-from-addon).
The detector flags them as (c) rather than (a) because (a) is
explicitly scoped to addon-from-addon by the brief; treat these as a
candidate future round, not this one.

| addon_id | module | missing | declared `requires_mod` |
|---|---|---|---|
| Edit Image Exif Metadata | editexifmetadata | `PIL` | (none) |
| mongodb | mongodb | `pymongo` | (none) |

### Real addon-side defects surfaced incidentally (6)

The detector is the wrong tool for these (its bucket-(c) is not gated),
but they are worth flagging since they prevent isolated import altogether
and so block the addon from loading under Gramps' own loader too:

| addon_id | module | last line |
|---|---|---|
| Collections Clipboard Gramplet | ClipboardGramplet | `AttributeError: 'NoneType' object has no attribute 'load_icon'` |
| Query Quickview | QueryQuickview | `SyntaxError: '(' was never closed` |
| Source References | SourceReferences | `ModuleNotFoundError: No module named 'ListModel'` |
| TimePedigreeHTML | TimePedigreeHtml | `NameError: name 'localAlphabeticIndex' is not defined` |
| Wordle Gramplet | WordleGramplet | `ImportError: cannot import name 'imap' from 'itertools'` (Python 2 leftover) |
| lxml Gramplet | lxmlGramplet | `NameError: name 'self' is not defined` |
| rebuild_types | RebuildTypes | `ModuleNotFoundError: No module named 'gui'` (bare `gui` should be `gramps.gui`) |

Several of these have or had corresponding Mantis tickets / PRs in
flight; tracking and remediation is out of scope for this brief.

---

## (b) Missing `requires_mod` (ignored)

Reported for completeness — these are the runtime / pip-dep concerns PR
820's auto-derive owns, not declaration bugs:

| addon_id | module | missing |
|---|---|---|
| ChatWithTree | ChatWithTree | litellm |
| GrampsChat | GrampsChat | litellm |
| networkchart | NetworkChart | networkx |
| postgresql | postgresql | psycopg2 |
| postgresqlenhanced | postgresqlenhanced | psycopg |
| s3uploader | S3MediaUploader | boto3 |
| sharedpostgresql | sharedpostgresql | psycopg2 |

---

## Limitation (must accompany any use of this detector)

The detector catches undeclared addon dependencies that manifest at
**load** time (top-level imports during module exec). It **misses**
lazily-imported sibling addons — e.g. a `from libsibling import foo`
inside a function body that is not called at module load. No false
positives, but **not exhaustive** — do not let it be mistaken for one.

---

## No fixes applied this round

Per the brief: this round is detector + findings list only. **No
`depends_on` (or any other) changes have been made to the addons tree.**
The detector goes green on the current gramps60 tree because there are no
(a) findings; that does not mean nothing else in this report deserves
attention, only that the WebConnect remediation that originally motivated
the detector is already in effect on this branch.

The next steps belong to Eduard, not Claude:

1. Decide whether the gramps61 tree needs a remediation round (the
   detector should be re-run there to know which packs / addons actually
   lack the declaration on that branch).
2. Decide whether to triage any of the bucket-(c) defects above (most are
   already tracked).
3. Decide whether to wire the detector test into `ci.yml` (advisory via
   `continue-on-error: true` first, matching PR 820's flip-to-blocking
   pattern once the tree is clean). This brief does not change `ci.yml`.
