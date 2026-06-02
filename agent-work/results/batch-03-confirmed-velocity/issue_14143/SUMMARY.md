# Issue 14143 — ChatWithTree dark-mode contrast (addons-source)

## Status
**Real fix shipped** — draft PR [addons-source#924](https://github.com/gramps-project/addons-source/pull/924) on `maintenance/gramps60`. Pure CSS change locking `color: black;` on each chat-bubble class so the foreground contrasts against the intentional pastel backgrounds regardless of the active GTK theme.

**Manual work — see `MANUAL-VERIFICATION.md` in this folder.**
Verdict explicitly calls for HUMAN visual sign-off on the contrast
under a dark theme (an automated regex-on-CSS-string test was rejected
as low-value busywork). The MANUAL-VERIFICATION.md covers:
- Linux primary sign-off under Adwaita Dark / Yaru Dark (fastest;
  GTK on Linux honours the system theme directly)
- Windows secondary check on the GrampsAIO bundled GTK (depends on
  whether that build honours Windows dark mode)

Outcome gates the Mantis close: bubbles readable in both themes →
paste `mantis-comment.md` and set Fixed in version; any bubble
unreadable → reopen with a screenshot.

## Root cause
`ChatWithTreeClass._apply_css_styles` in
[`ChatWithTree/ChatWithTree.py:169-198`](../../../../../../addons-source/ChatWithTree/ChatWithTree.py#L169-L198)
sets hardcoded LIGHT background colours on each message-bubble CSS class
(`.message-box` `#f0f0f0`, `.user-message-box` `#dcf8c6`, `.tree-reply-box`
`#d1e2f4`, `.error-reply-box` `#f4e2d1`, `.tree-toolcall-box` `#fce8b2`)
plus `#chat-listbox { background-color: white; }`. NO foreground colour is
set — the foreground is inherited from the active GTK theme.

Under a light GTK theme the inherited fg is black/dark → fine. Under a
dark GTK theme the inherited fg is white/light → the text becomes
light-on-light on the hardcoded pastel backgrounds. Unreadable.

The pastel backgrounds are intentional — they colour-code message type
(green = user, blue = reply, yellow = tool-call, red = error) and were
chosen against a white parent. The fix is not to make the backgrounds
theme-aware (that'd lose the colour-coding) but to also lock the
foreground so it contrasts against those specific pastels in any theme.

## Fix
Add `color: black;` to each message-bubble CSS class (plus `#chat-listbox`).
Five additions in `_apply_css_styles`'s CSS string; no Python logic change.
Inline comment explains why the foreground is locked.

## Verified against
- `ChatWithTree/ChatWithTree.py:169-198` (`upstream/maintenance/gramps60`)
  — the only place this addon sets visual styling. Confirmed no other CSS
  provider is loaded, and there's no `style_context.add_class("...")` call
  that depends on theme-derived colours.
- `git log upstream/maintenance/gramps60 -- ChatWithTree/`:
  - HEAD `388be68be` (Merge local.po from PR827)
  - No fg/contrast-related changes since the addon was added
    (`706a78fa3 Merge ChatWithTree gramplet addition #762`).
  - Upstream is not ahead.
- No open or closed addons-source PRs in flight for ChatWithTree contrast
  / dark-mode (checked with `gh pr list --repo gramps-project/addons-source --state all --search "ChatWithTree"`).

## Test
None — the verdict in `issue_14143.md` explicitly calls this:
> Test caveat: contrast is a VISUAL property — do NOT force a brittle
> automated contrast test. Acceptable to ship a pure styling fix with a
> light assertion that the addon no longer hardcodes a foreground colour,
> OR no test with a note. **Eduard verifies the actual rendering manually**
> — flag clearly in the SUMMARY that this needs human visual sign-off (the
> one item here that is not fully self-verifying).

**Needs Eduard's visual sign-off** under a dark GTK theme (e.g. Adwaita
Dark) before merging — confirm the chat bubbles now render readable text
on the pastel backgrounds, and that the colour-coding (green/blue/red/yellow
bubble differentiation) is preserved.

A light assertion-style test (grep the CSS string for `color:`) was
considered and rejected as low-value busywork — it'd test the diff of the
PR rather than the behaviour, and would lock the addon into an
implementation choice that future theme-aware refactoring would need to
unwind. The PR description carries the visual-sign-off flag instead.

## Repo and branch
- Repo: `addons-source` (upstream `gramps-project/addons-source`)
- Branch: `maintenance/gramps60` (per CLAUDE.md: addons-source fixes go to
  gramps60; Gary cherry-picks to gramps61. Memory:
  `feedback_branch_targeting_addons_vs_core`.)
- Local branch in `../addons-source`: `fix/bug-14143-chatwithtree-dark-contrast`
  (off `upstream/maintenance/gramps60`; uncommitted working-tree diff —
  patch.diff captures the change).
- Per `feedback_addons_source_no_version_bump`: do NOT bump the addon's
  `version = '…'` line in `ChatWithTree.gpr.py`. Maintainer manages
  versions centrally.

## Mantis link
- Tracker: https://gramps-project.org/bugs/view.php?id=14143
- Status to set on close: resolved / fixed (after visual sign-off + merge)
- Fixed in version: next addons-source release on maintenance/gramps60
- Comment: see `mantis-comment.md`

## Notes for next reviewer
- The fix DOES lock `color: black` rather than pulling fg from the theme.
  That's deliberate — the backgrounds are intentionally hardcoded pastels
  for message-type colour-coding, and theme-fg-on-hardcoded-bg is exactly
  the failure mode the bug describes. Locking fg guarantees contrast
  against those specific pastels regardless of theme.
- A future refactor could rebuild the colour-coding via theme-aware
  CSS classes (e.g. `@define-color user-bubble-bg ...`) and let GTK
  pick the right fg per theme. That's a styling redesign, out of scope
  for a targeted contrast-fix backport — file separately if pursued.
