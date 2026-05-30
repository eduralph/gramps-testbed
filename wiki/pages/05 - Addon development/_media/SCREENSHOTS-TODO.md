---
title: Screenshot capture brief — Addon Development manual
managed: false
status: todo
---

<!--
  Eduard runs Gramps; Claude can't. This file lists every screenshot
  the section wants, with enough setup detail that any of them can be
  captured in isolation.

  Capture conventions (apply to all):
    - Gramps 6.0 from maintenance/gramps60. Note the version in the
      filename suffix if 6.1 captures land later.
    - Open example.gramps (~/path/to/gramps/example/gramps/example.gramps).
      No PII, reproducible by any reviewer.
    - Default GTK theme (Adwaita) — keeps captures consistent with what
      a new user sees out of the box. If you've themed, switch back for
      capture only.
    - PNG, lossless, at the smallest resolution that's readable at the
      embed width Obsidian renders. ~1200 px wide is usually enough.
    - Crop tight to the relevant UI region. Full-window shots only when
      the chapter is showing UI placement, not content.
    - Save under _media/ with the filename listed below.

  Embed pattern in the chapter (matches existing plugin-discovery.svg):
    ![[_media/<filename>|Fig. N — <caption that doubles as alt text>]]
-->

# Captures needed

## For [[02-get-started]] — first Gramplet

Each tutorial in 03 has a "Try it" closer. The Hello Gramplet in 02 is the simplest case and deserves one capture:

### `hellogramplet-in-sidebar.png`

**Setup.**

1. Drop `HelloGramplet/` (the two files from [02-get-started → 2. Add the registration file](../02-get-started.md)) into your user plugin directory.
2. Restart Gramps.
3. Open example.gramps.
4. Add the "Hello Gramplet" from the sidebar gramplet menu.

**Capture.** Crop to the right sidebar showing the gramplet docked. Include the tab title bar so the gramplet's title chip ("Hello") is visible. ~400×300 px is plenty.

**Insertion point.** After the *4. Restart Gramps* step, before *Reload / test cycle*. Caption: "Fig. 1 — The Hello Gramplet docked in the sidebar after restart. The title bar shows the `gramplet_title` from the registration; the body shows the text set in `init()`."

---

## For [[03-tutorials]] — one per walkthrough

### `tut-personevents-gramplet.png`

**Setup.**

1. Build `PersonEvents/` from [03-tutorials → A live Gramplet](../03-tutorials.md#a-live-gramplet).
2. Drop into user plugin dir, restart Gramps, open example.gramps.
3. Select a person with several events recorded — Garner family (I0044 *Lewis Anderson Garner*) is a good choice in example.gramps; he has ~7 events.
4. Add the "Person Events" gramplet to the sidebar.

**Capture.** Right sidebar only, ~400×400 px. The gramplet body should show I0044's gramps_id in bold followed by the event list. Bonus demonstration: capture twice (one for I0044, one for I0046 his daughter) to show the gramplet refreshing on selection change — but one is enough if you're keeping it minimal.

**Insertion point.** End of *A live Gramplet → Try it*. Caption: "Fig. 2 — Person Events gramplet showing direct events for the active person. The list refreshes when the user selects a different person or when the database changes."

### `tut-missingbirthdates-dialog.png`

**Setup.**

1. Build `MissingBirthDates/` from [03-tutorials → A simple Tool](../03-tutorials.md#a-simple-tool).
2. Drop into user plugin dir, restart Gramps, open example.gramps.
3. Tools → Analysis and Exploration → Missing Birth Dates.

**Capture.** The full dialog modal (`OkDialog`) at its default size. Should show the heading line ("N people with no recorded birth date:") and the first ~10 person entries.

**Insertion point.** End of *A simple Tool → Try it*. Caption: "Fig. 3 — Missing Birth Dates tool dialog listing affected people, run against example.gramps."

### `tut-dbsummary-pdf.png`

**Setup.**

1. Build `DbSummary/` from [03-tutorials → A text Report](../03-tutorials.md#a-text-report).
2. Drop into user plugin dir, restart Gramps, open example.gramps.
3. Reports → Text Reports → Database Summary.
4. Output format: PDF (or HTML — pick whichever renders cleanly in your viewer for the screenshot).

**Capture two.** (a) The Reports menu showing the new entry highlighted; (b) the rendered output PDF/HTML page. The point of capturing both is to show "the addon is in the menu" and "the addon produces output" — the two questions every tutorial reader has.

- `tut-dbsummary-menu.png` — menu screenshot, ~400×200 px.
- `tut-dbsummary-output.png` — PDF/HTML render, ~600×400 px.

**Insertion point.** Two figures at *A text Report → Try it*. Captions: "Fig. 4a — Database Summary appears under Reports → Text Reports after restart." and "Fig. 4b — Rendered Database Summary output for example.gramps in PDF format."

### `tut-siblings-quickview.png`

**Setup.**

1. Build `Siblings/` from [03-tutorials → A Quick View](../03-tutorials.md#a-quick-view).
2. Drop into user plugin dir, restart Gramps, open example.gramps.
3. People view, right-click any person who has siblings — I0001 *Eugene Stanley Garner* (multiple siblings) works.
4. Quick View → Siblings.

**Capture two.** (a) The context menu showing "Quick View ▸ Siblings" highlighted, (b) the Quick View result window.

- `tut-siblings-contextmenu.png` — ~400×400 px, partial main window with the right-click menu open and the entry highlighted.
- `tut-siblings-result.png` — ~500×400 px, the result window showing the title, columns header, and ~5 sibling rows.

**Insertion point.** Two figures at *A Quick View → Try it*.

### `tut-hasnchildren-rule.png`

**Setup.**

1. Build `HasNChildren/` from [03-tutorials → A custom filter Rule](../03-tutorials.md#a-custom-filter-rule).
2. Drop into user plugin dir, restart Gramps, open example.gramps.
3. Edit → Person Filter Editor → Add → Add Rule.
4. Scroll to "Family filters" section.
5. Highlight "People with at least N children".

**Capture.** The Add Rule dialog with "Family filters" expanded and the new rule highlighted. Don't accept the dialog — the capture is "the rule registered and shows up in the dialog catalogue."

**Insertion point.** End of *A custom filter Rule → Try it*. Caption: "Fig. 6 — The custom rule appears under Family filters in the Add Rule dialog after restart. Typing a number in the Minimum count field activates it."

---

## For [[01-overview]] (optional, lower leverage)

### `overview-pluginmanager.png`

The Plugin Manager (Help → Plugin Manager) gives a literal view of "what an addon is" — a list of registered plugins with their kind, version, target Gramps version, and status. A capture here would anchor the overview's abstract prose to something concrete.

**Setup.** No special addons needed — built-in plugins fill the list.

**Capture.** The Plugin Manager window at default size, default tab (Loaded plugins). Crop to remove window decoration if your WM produces heavy chrome.

**Insertion point.** Mid-page in 01-overview, anchoring the "addons are discovered and catalogued" description. Optional — overview is already short.

---

## Conventions reminder

- **Filenames** use lowercase + hyphens (`tut-personevents-gramplet.png`), matching existing media: `Dashboard-category-view-first-open-no-family-tree-loaded-60.png`.
- **Embed** as `![[_media/<filename>|Fig. N — <caption>]]`. The caption doubles as alt text and is what shows up in published output.
- **Re-capture rule.** A screenshot stays valid as long as the captured UI element hasn't changed. GTK theme changes don't require re-capture unless the theme makes content unreadable. Gramps minor releases (6.0 → 6.1 → 6.2) may shift layouts; check the figure on upgrade.

## After capture

1. Drop each PNG into `05 - Addon development/_media/`.
2. Delete the corresponding **Insertion point** stub from this file (or strike-through the section heading).
3. When all are done, this file can be deleted entirely.
