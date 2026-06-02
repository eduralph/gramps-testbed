# 14143 — Windows validation (post-merge visual sign-off)

**Why this needs a Windows check:** the verdict in `issue_14143.md`
explicitly calls for HUMAN visual sign-off — contrast is a visual
property and an automated regex-on-CSS-string test was rejected as
low-value busywork. The fastest sign-off is on Linux with a dark GTK
theme (Adwaita Dark / Yaru Dark), where GTK honours the system theme
directly. Windows is a secondary check — useful insofar as the bundled
GTK in your AIO build actually picks up Windows' system dark mode.

**This is NOT a Linux-can't-repro case.** Dark-mode contrast does
reproduce on Linux. The Windows step is a secondary visual confirmation
under the AIO's GTK bundle.

**Run after [addons-source#924](https://github.com/gramps-project/addons-source/pull/924) merges and a Linux dark-theme sign-off is in.**

---

## Linux primary (do this first)

### Setup
1. Apply addons-source#924 to your local `addons-source/` checkout
   (the testbed's auto-sync installs the addon into the live plugin
   dir).
2. Force Gramps to render dark. Gramps 6.x is a **GTK3** app
   (`grampsapp.py` pins `Gtk 3.0`) with no internal dark-mode handling —
   it follows `GtkSettings` only. Use whichever is convenient:
   - **Per-launch, no session change (most reliable — use this):**
     `GTK_THEME=Adwaita:dark gramps`
     forces the dark variant for that one process. Best for a clean
     test because it touches nothing else in your session.
   - Session-wide:
     `gsettings set org.gnome.desktop.interface gtk-theme 'Adwaita-dark'`
     (a dark *gtk-theme*; remember to set it back afterwards).
   - NOTE: `gsettings set … color-scheme 'prefer-dark'` does **not**
     flip a GTK3 app on its own — `color-scheme` is the GNOME 42+ /
     libadwaita (GTK4) signal. Setting only that and seeing Gramps stay
     light is a false "can't reproduce", not a fixed bug. Use one of the
     two methods above.
3. Launch Gramps (with the env var above, if using it). Open the Chat
   With Tree gramplet (Gramplets bar).

### Verify
4. Type a query → confirm **USER** bubble (green) text is readable.
5. Wait for reply → confirm **REPLY** bubble (blue) text is readable.
6. If you can trigger a tool call (depends on LLM config), confirm
   **TOOL-CALL** bubble (yellow) text is readable.
7. If you can trigger an error (e.g. an obviously invalid query),
   confirm **ERROR** bubble (light red) text is readable.
8. Switch back to a light theme briefly — confirm the bubbles still
   render correctly in light mode (no regression).

### Outcomes
- ✅ **All bubble text readable in both themes, colour coding
  preserved** → primary sign-off done. Proceed to Windows secondary
  below (or skip if you don't have a current AIO build with the fix).
- ❌ **Any bubble unreadable** → reopen with a screenshot showing
  the unreadable state + the GTK theme name in use.

---

## Windows secondary (AIO-specific, optional but informative)

### Setup
1. Install the GrampsAIO Windows build that contains the merged
   addons-source#924.
2. Enable Windows dark mode: Settings → Personalization → Colors →
   Choose your mode → Dark.

### Verify
3. Launch Gramps. **The bundled GTK either does or doesn't pick up the
   Windows dark mode** — observe whether the main Gramps window itself
   renders dark.
   - If the main window stays light despite Windows dark mode → the
     bundled GTK isn't honouring the OS theme on this AIO build. You
     can still exercise the fix: relaunch with the dark variant forced
     for the process — in the MSYS2/AIO shell, `set
     GTK_THEME=Adwaita:dark` (cmd) or `$env:GTK_THEME='Adwaita:dark'`
     (PowerShell) before launching Gramps, then continue from step 4.
     If forcing dark isn't possible on this build, the 14143 fix is
     still correct (it locks the foreground regardless of theme) but
     the dark-mode regression can't be reproduced on this AIO — note
     that and close.
   - If the main window goes dark → continue.
4. Open Chat With Tree, exercise the bubble types as for Linux above.
5. Confirm all bubble text remains readable (the `color: black;` lock
   keeps it dark regardless of theme).

### Outcomes
- ✅ Readable → secondary sign-off confirms cross-platform.
  Paste `mantis-comment.md`, set Fixed in version, close.
- ❌ Unreadable on Windows AIO dark mode → reopen with screenshot +
  AIO version. This would indicate the bundled GTK on Windows is
  overriding inline CSS `color:` properties, which is a much weirder
  upstream issue.
