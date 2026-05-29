# Claude Code increment — batch-04-recent-confirmed, INCREMENT 4

> Read alongside CLAUDE_CODE_BRIEF.md (binding) and each issue_<id>.md verdict.
> Standing rules apply: trust the verdict over the title; resolve addon-vs-core
> by reproducing; repro-or-close before fixing; check merged AND closed PRs;
> one logical fix per issue with a test in the same change; STOP after writing
> results (no push/PR/ready-mark — Eduard's review gate).

## Batch-04 POSTURE (carried from increment 1 — still applies)
1. **Repro-or-close is the default for D-bucket items.** These were
   lower-confidence at selection time; if they don't reproduce on
   example.gramps on the target branch (gramps61), the outcome is
   evidenced can't-reproduce with a Mantis comment documenting what was
   tried — NOT an attempt to chase ambiguous signals into a speculative fix.
2. **MANUAL-VERIFICATION.md is REQUIRED for every platform-specific item.**
   The six macOS/Windows items in this increment cannot be confirmed on
   Linux. They do NOT get closed as can't-repro — they get a
   `results/issue_<id>/MANUAL-VERIFICATION.md` per the playbook template
   (numbered repro steps + decision tree + BOTH pre-written Mantis comments).
   Flag the manual-step requirement at the top of each SUMMARY.md.
3. **Some bugs need a built fixture.** 13406 (Top Surnames) needs a
   prefixed-surname fixture (e.g. "von Trapp", "de la Vega") — example.gramps
   does not trigger it. Build at the addon test location or the testbed
   fixture path. Never use Eduard's real data.
4. **Items DEFERRED from increment 3** (any 13830 / 13888 / 14051 that
   resolved to core) join this increment as gramps61 core fixes. Check
   inc 3's SUMMARY.md outputs before starting — the deferral notes there
   are the working set for any add-ins.

## Increment-4 items (13 items)
Mixed: 7 D-bucket repro-or-close core items + 6 platform-specific manual-
verification items. Work in this order: D-bucket first (Linux work, real
fix path), then the manual-verification batch (template work, no Linux
repro required).

### D-bucket — core/gramps61 repro-or-close (7 items)

#### 13260 — [Linux Mint] can't load database backend 'b...' — LEAD
23 notes, CORE-TRACE. This is FILED in the E bucket of BATCH_INDEX but the
disposition note correctly identifies it as Linux, not manual. Linux-
confirmable. Likely root cause from the volume of notes: bsddb backend
import path or distro-packaging dependency. Read the thread before
reproducing — 23 notes typically means a diagnosis was reached or narrowed
collaboratively. Repro on Ubuntu 24.04 (your workstation env, not Mint
specifically) by attempting to load a tree with the bsddb backend. Fix in
core (gramps/plugins/db/bsddb/ or the backend selection layer). Test:
headless unittest on the backend selection path with bsddb available /
unavailable.

If the thread concludes the bsddb backend should be REMOVED on Linux (the
Windows AIO already dropped it per the gramps PR #2198 era), then the
outcome is core/gramps61 fix that gracefully fails-and-explains instead
of throwing — flag this disposition decision back to Eduard before coding.

#### 14014 — [Gramps web] ranges-date Error while importing
11 notes, CORE-TRACE. Gramps-Web interaction; the traceback is in core's
date import path. Repro: import a Gramps-Web-exported tree with a date
range value (e.g. "between 1850 and 1860") on example.gramps target. Fix
in `gramps/gen/lib/date.py` or the XML date parser. Test: headless date-
parse unittest with the failing range syntax.

Note: this is the third Gramps-Web interaction item in the batch (after
13832 in inc 1 and possibly 13979). If a cross-cutting Gramps-Web
incompatibility theme emerges across these, flag back to Eduard — it may
warrant a coordinated note in the Gramps-Web project's compatibility
docs rather than per-issue fixes.

#### 13984 — Dashboard Label wrong language after install
3 notes. Locale/install-state issue. Repro: install Gramps fresh with a
non-en locale (e.g. LANG=de_DE.UTF-8), launch, observe Dashboard. The
label is failing to pick up translation — likely a gettext init missed,
or a string marked for translation that isn't being looked up at display
time. Fix in core (gramps/plugins/gramplet/welcomegramplet.py or
dashboard view). Test: locale-parametrized unit test asserting the
translated string is loaded for a non-en locale.

#### 13518 — [RCS Archive] Tree Manager can't rename archived backup
4 notes. RCS Archive feature is core. Repro: archive a tree via Tree
Manager, attempt rename, observe failure. Fix likely in
`gramps/cli/clidbman.py` or `gramps/gen/recentfiles.py` rename handler
for archived state. Test: headless unittest on the rename operation
with a synthetic archived-state tree.

#### 13406 — [Top Surnames Gramplet] quick view prefix issue
5 notes. FIXTURE NEEDED: build a synthetic tree containing surnames with
prefixes (per POSTURE note 3). Repro: open Top Surnames Gramplet, click a
prefixed surname's quick view, observe behaviour. Top Surnames is a core
gramplet (gramps/plugins/gramplet/topsurnamesgramplet.py); fix there. Test:
headless test on the surname-collection / display logic with a prefixed
surname.

#### 13387 — 'Estimated' in Age Calculator contaminated by 'about'
1 note. The "about" qualifier on a date is bleeding into the "estimated"
flag in age calculations. Fix in the age calculator core (likely
gramps/gen/datehandler/ or wherever AgeCalculator surfaces). Test:
headless unittest passing dates with each modifier (about, estimated,
calculated, etc) and asserting the estimated flag is computed from the
correct source.

#### 13270 — Tooltip on chart for living person shows
1 note. Tooltip on charts (Pedigree / Ancestry / Descendants chart views)
exposes data for living persons that should be hidden. Living-person
privacy is a core concept; the tooltip rendering is bypassing it. Fix in
the chart view tooltip handler. Test: GUI interface test in
gramps-testbed asserting tooltip content is redacted for a person marked
private/living.

### E-bucket — platform-specific MANUAL-VERIFICATION items (6 items)
These do NOT get a code fix from this increment. They get a
`results/issue_<id>/MANUAL-VERIFICATION.md` per the playbook template +
a flag at the top of SUMMARY.md. Each manual-verification doc contains:
- What manual step + why it can't be automated (Linux can't repro / GTK3
  on Windows exposes no UIA tree)
- Platform(s): macOS or Windows
- Exact environment: Gramps version/build (AIO64 macOS/Windows), branch,
  any theme/locale/config the repro needs
- Numbered repro steps (concrete, current-version, not just the tracker's
  original)
- Expected vs defect behaviour (unambiguous)
- What to capture (screenshot / console / error-report)
- Decision tree (reproduced → fix path / not reproduced → close as
  can't-repro)
- BOTH pre-written Mantis comments (confirmed and could-not-confirm)

#### 14230 — [macOS] Hosting Media on S3 — boto3 problems
POSSIBLY-FIXED + macOS. Pre-flight: check whether boto3 versioning in
recent macOS AIO releases addresses this; if so, the manual-verification
becomes "confirm the bundled boto3 version on AIO and verify against
14230's symptom". Otherwise full manual-verification doc.

#### 13983 — [macOS] No further editing after loading
12 notes. macOS-specific freeze/lock after tree load. Manual-verification
needs to be precise on which tree size / which load path triggers it —
read the notes for the narrowing.

#### 13774 — [macOS] Installing Life Line Ancestor Chart crashes
3 notes. macOS install-time crash. Manual-verification: install the
addon on macOS AIO, observe crash, capture console.

#### 13223 — [macOS] Cannot install addon — failing prerequisite
5 notes. macOS prerequisite check failing on addon install. Read the
notes for WHICH prerequisite; that determines whether this is the same
class of bug as 13774 or distinct.

#### 13409 — [Windows 11] AIO installer does not drop ...
10 notes. Win11 installer behaviour. Manual-verification: install
Gramps AIO 5.2.3 (or current 6.0.x AIO — check note thread for which
version still reproduces) on Win11, observe installer step that fails.

#### 13667 — [Windows AIO 6.0 beta2] Addon Manager Module Install
9 notes. Filed against 6.0.0-beta2 which is OLD. PRE-FLIGHT (per
BATCH_INDEX disposition note): confirm this still applies to the current
6.0.x release before writing the full manual-verification doc. If it
doesn't reproduce on current 6.0.x AIO, the outcome is a Mantis comment
"could not reproduce on Gramps 6.0.x AIO; closing as
fixed-or-already-resolved between beta2 and 6.0.x release" — not a full
manual-verification doc.

## Per-item: write results/issue_<id>/ then STOP
Each item: SUMMARY.md (root cause OR repro-status, fix/close/manual,
test if any, repo+branch, outcome), patch.diff (if a fix),
pr-description.md (if a PR is warranted), mantis-comment.md (ALWAYS),
MANUAL-VERIFICATION.md (REQUIRED for all 6 E-bucket items + any D-bucket
item that resolves as needing manual confirmation). STOP for review; no
push/PR/ready-mark.

## Expected increment-4 shape
Mixed and lighter per-item than inc 2 because manual-verification docs
are template-driven, not fix-driven. Likely:
- D-bucket (7 items): 3-5 real core fixes (gramps61); 2-4 evidenced
  can't-reproduce closes if the description signal was too thin to
  reproduce.
- E-bucket (6 items): 5 full MANUAL-VERIFICATION.md docs + 1 likely
  close on 13667 (the old beta2 one).

So roughly 3-5 real fixes + 2-4 closes + 5 manual-verification docs.
A successful outcome looks like every item having either a paste-ready
Mantis comment or a paste-ready manual-verification doc — the batch ends
with no item left without a tracker disposition.

## Decision points worth flagging back to Eduard
- 13260 (bsddb on Linux): if the thread suggests REMOVING the bsddb
  backend rather than fixing the import path, that's a deprecation
  decision — STOP after diagnosis, do not write the removal patch
  without explicit go-ahead.
- 14014 / cross-cutting Gramps-Web compatibility: if a pattern emerges
  across 13832 (inc 1), 14014 (inc 4), and any others, write it up
  separately in `results/cross-issue/gramps-web-compat-notes.md` rather
  than scattering it across per-issue SUMMARYs.
- 13270 (tooltip privacy): privacy/living-person rules in Gramps have
  history of UX debate. If the fix touches the privacy filter logic
  (not just the tooltip renderer), flag back before broadening.
- 13667 (Win AIO beta2): if it doesn't reproduce on current 6.0.x AIO,
  the close is "already fixed between beta2 and release" — Eduard's
  voice in the Mantis comment should make that explicit so the reporter
  isn't left wondering why their bug closed without a fix commit cited.

## Increment closure (batch-04 end)
This is the final batch-04 increment. After it completes:
- All 38 items have results/ folders with at minimum SUMMARY.md +
  mantis-comment.md.
- Manual-verification items have MANUAL-VERIFICATION.md ready for Eduard
  to run on macOS/Windows.
- batch-04 EXIT BRIEF is written separately by Eduard (or in a follow-up
  Claude Code session per his direction) — NOT in this increment.
