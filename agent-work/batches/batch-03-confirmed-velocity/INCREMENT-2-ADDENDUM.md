# Increment 2 (CSV items) — handoff addendum

> Append to / read alongside CLAUDE_CODE_BRIEF.md. Scope: FOUR issues selected
> because each can be driven to a STOP-for-review WITHOUT a human watching a
> screen — headless-verifiable fixes or verification-only closes. The other
> eight batch-03 items are held for manual/Eduard-in-the-loop work (visual
> verify, mouse-sequence repro, or a design decision) and are NOT in this
> increment.
>
> Standing rules from increment 1 still apply: repro-or-close before fixing;
> check BOTH merged AND closed/rejected PRs (closed PRs reveal maintainer
> deletion/decline decisions); fix only what the verdict scopes; one logical
> change per issue; STOP after writing results — no push, no PR, no ready-mark.

## Branch targets — READ THIS, it is not uniform
The addons-source → gramps60 / gramps core → gramps61 rule applies PER ITEM,
and two of these four are CORE despite being filed under "3rd Party Addons":

| Issue | Real repo | Branch | Why |
|---|---|---|---|
| 13955 | addons-source | maintenance/gramps60 | RepositoriesReport addon Python |
| 14145 | addons-source | maintenance/gramps60 | FrWebConnectpack addon Python |
| 13420 | addons-source | maintenance/gramps60 | ImportGramplet addon (IF it reproduces) |
| 13065 | gramps core | maintenance/gramps61 | fix is core PR #1530; addon only shows symptom |

The "resolve addon-vs-core by reproducing" step in the brief is mandatory for
13065 (it's a verification-only close, already core-fixed) and was the deciding
factor for putting it on the core branch.

## The four — what each is, and the expected outcome

### 13955 — RepositoriesReport omits URLs — REAL FIX (strongest of the four)
Root cause is located in the verdict: the URL-writing block in
`RepositoriesReportAlt.py` is commented out (since 2010), and naively
uncommenting it throws `NameError: name 'internet' is not defined` at ~line 200.
- The fix is "uncomment the write block AND restore the assignment of `internet`"
  (build it from the repository's URL list — see `repo.get_url_list()` /
  `url.get_path()` usage in sibling report addons). NOT just uncomment.
- Test: addon unit test — repository with a URL, run report with include-URLs
  option, assert the URL text appears in output. Gate on display if the doc
  layer needs one.
- Expected outcome: a real patch + test. addons-source/gramps60.

### 14145 — FrWebConnectpack stale Geneanet URL — REAL FIX (one-liner)
See issue_14145.md (verdict now filled). Stale Geneanet search-URL template at
`FRWebPack.py` ~line 45; reporter supplied the corrected URL (adds given name).
- Fix: replace the URL template, keeping the file's existing `%(...)s`
  placeholder convention (grep a working entry to confirm key names first).
- Maintainer caveat: callmedave pushes the WebSearch Gramplet as a "replacement"
  but explicitly CONFIRMED this issue for FrWebConnectpack — so it's a real fix,
  NOT wontfix. Only stop if a CLOSED PR shows the addon is being retired.
- Test: pure string assertion that the constructed URL has both name parts and
  the corrected host/path/params. No network, no display.
- Expected outcome: a real patch + test. addons-source/gramps60.

### 13420 — Text Import death-fallback — INVESTIGATE-FIRST (fix OR clean close)
The whole decision is the repro, and it's scriptable headless:
- Build a CONFORMANT minimal Gramps XML (one person, Birth + Death events both
  role Primary, STANDARD Gramps handles — NOT the reporter's UUID handles),
  import via the Import Text gramplet path on gramps60, assert whether the Death
  event resolves as the person's death fallback WITHOUT a manual editor re-save.
- If fallback is missing with clean XML → REAL addon bug (gramplet skips the
  post-import fallback recompute the normal path does) → fix + test.
- If fallback resolves with clean XML → NOT our bug; reporter's malformed
  UUID-handle XML was the cause → close as cannot-reproduce / invalid input.
- Do NOT use the reporter's XML as the fixture. Build a clean one.
- Expected outcome: EITHER a patch+test OR a documented can't-repro close. Both
  are success. addons-source/gramps60.

### 13065 — Place Coords wrong URL — VERIFICATION-ONLY CLOSE (no fix)
See issue_13065.md (verdict now filled). Already fixed in gramps CORE, 5.2, via
PR #1530 / commit 44629e3; reporter confirmed on 5.2.0.
- Task is verification only: confirm 44629e3 is an ancestor of the target branch
  and the current Map Service URL builder uses `/search?q=` (no `.php`, no
  trailing slash). Cite path:line.
- Close as already-fixed. No patch.diff, no pr-description.md.
- ONLY escalate (do not fix) if the bad URL is somehow still present — that
  contradicts the thread and needs a human look.
- Expected outcome: a confirm-and-close SUMMARY.md. gramps core / gramps61.

## Net expected result of increment 2
Two real fixes (13955, 14145), one investigate-then-fix-or-close (13420), one
verification-only close (13065). Each reaches a STOP point Claude Code can hit
unattended; none requires Eduard to watch a GUI or make a design call mid-stream.
