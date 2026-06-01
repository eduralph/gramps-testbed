---
title: Addon Development — Sidebar
managed: true
---

<!--
  Vault-internal map for the Addon Development section. NOT a published
  page (managed: false) — Obsidian users navigate by this; publish.py /
  md2pdf.py skip it.

  Ordering rationale: author journey. A reader new to Gramps addon work
  goes Overview -> Get started -> a tutorial -> picks the kind of addon
  they're building -> reads fundamentals when something doesn't behave
  the way they expected -> reaches for data access / API as the addon
  gets non-trivial -> testing / debug / troubleshoot when stuck ->
  code analysis / packaging when ready to ship -> compatibility /
  what's new when porting across Gramps versions.
-->

## Sidebar

1. [[01-overview]] — what an addon is, file roles, registration shape.
2. [[02-get-started]] — first Gramplet, restart loop, where addons live.
3. [[03-tutorials]] — end-to-end walkthroughs per addon kind.
4. [[04-addon-kinds]] — Gramplets, Views, Reports, Tools, Importers, Exporters, Docgens, Quick reports, Sidebars, Map services, Relationship calculators, Rules.
5. [[05-fundamentals]] — `.gpr.py` registration fields, plugin discovery, `_()` / `ngettext`, module-level loggers, lifecycle hooks.
6. [[06-data-access]] — `DbReadBase` / `DbWriteBase`, handles vs `gramps_id`, backlinks, transactions, what `gen/` exposes.
7. [[07-api-reference]] — curated `gramps.gen.*` surface addons are allowed to import; what's stable vs. what isn't.
8. [[08-testing]] — `unittest`-only, `test_*` filename conventions, mock-vs-`example.gramps` guidance, addon-unit runners.
9. [[09-debug]] — Gramps debug mode, log levels, repro scripts that bypass the GUI, `PrerequisitesCheckerGramplet`.
10. [[10-troubleshoot]] — common failure modes: silent reload, no-symlinks rule, namespace-package binding traps, `requires_mod` vs PyPI name.
11. [[11-code-analysis]] — Black, ruff E9/F63/F7/F82, `ast.parse`, mypy (for core); what the per-repo pre-commits enforce.
12. [[12-internationalization]] — i18n, translations, gettext, _() / N_() handling, .po/.pot generation for addons.
13. [[13-packaging]] — `make.py`, `addons-source` -> `addons` flow, version-field rules, submitting to upstream.
14. [[14-compatibility]] — porting across Gramps versions; `gramps_target_version`; deprecated API surface; gramps60 vs gramps61 deltas.
15. [[15-whats-new]] — per-Gramps-version API changes that affect addons.
16. [[16-guidelines]] — normative MUST / SHOULD / MAY reference for addons and the contributor workflow. The page to cite in code review.
17. [[17-roadmap]] — forward-looking: in-flight changes, deprecations, open questions, and the documentation roadmap itself. Prospective counterpart to *What's new*.


## Status

Section is being built out. Stubs (`managed: false`) won't appear in published output until promoted to `managed: true`.

<!-- This file is intentionally not a {{stub}} for the wiki — it lives
     vault-side only. -->
