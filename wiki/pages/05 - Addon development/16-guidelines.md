---
title: Gramps 6.0 Wiki Manual - Addon Development - Rules
categories:
  - Addons
  - Developers
  - Gramps 6.0
managed: true
---

<!--wiki:{{man index|6.0}}-->

## Overview

Normative reference for addon authors. Conceptual / how-to material lives in the other section pages; this page enumerates the guidelines and is the one to cite in code review.

## Conventions

RFC 2119 keywords, with our short forms:

| Keyword | Meaning |
|---------|---------|
| **MUST** / **MUST NOT** | Required; a violation is a defect |
| **SHOULD** / **SHOULD NOT** | Strongly recommended; deviate only with a stated reason |
| **MAY** | Allowed |

Where a rule has a known origin — an upstream PR, a maintainer ruling, a Mantis bug — it's cited inline so the rule is auditable.

## Structure

- **MUST**: the addon's folder name matches the `id` in `.gpr.py`.
- **MUST**: `.gpr.py` declares `gramps_target_version` matching the Gramps minor the addon targets.
- **MUST**: `fname` points to an implementation module shipped in the same folder.
- **MUST** (Gramps 6.0): the addon is physically present under the plugin path. 6.0 plugin discovery does not follow symlinks. **MAY** (Gramps 6.1+): the addon folder is reached via a symlink. 6.1 plugin discovery follows symlinks, with realpath-based dedup so symlink loops terminate. The symlink test is skipped on Windows because the platform's symlink behavior is inconsistent without elevated privileges; on Windows a physical copy remains the recommended approach even on 6.1+.
- **MUST NOT**: import `register`, `GRAMPLET`, `STABLE`, `_`, or any other name Gramps injects into the `.gpr.py` namespace.
- **MUST NOT**: add `__init__.py` to the addon directory itself. The plugin loader puts the addon dir on `sys.path` and imports `<Addon>.py` by name; making the addon dir a regular package disturbs that resolution and can trigger the [Mantis 12691](https://gramps-project.org/bugs/view.php?id=12691) submodule-binding trap. (See [08-testing → Why `tests/__init__.py` exists](08-testing.md#why-tests__init__py-exists).)
- **MUST** (`TOOL` kind): register an `optionclass` even when the tool takes no options. Gramps refuses to load a `TOOL` without one; an empty `tool.ToolOptions` subclass is sufficient.
- **SHOULD**: ship a `po/` directory with at least `template.pot` if any user-visible string exists.
- **SHOULD**: ship a `tests/` package with an `__init__.py` marker and at least one test. The marker keeps dotted-path loading deterministic and is the prerequisite for shared test setup.
- **MAY**: ship multiple plugin kinds from a single addon (multiple `register(...)` calls in one `.gpr.py`).

## Source location

- **MUST**: edit addon source in `addons-source/`, never in the live plugin directory. The auto-sync runs source → installed plugin one-way; edits in the live dir are silently overwritten on the next source save.

## Translation

The full how-to (registration setup, `make.py` lifecycle, Glade runtime-override pattern, function reference) lives in [12-internationalization](12-internationalization.md). The rules below are what code review enforces.

- **MUST**: wrap every user-visible string with `_()`.
- **MUST NOT**: `import _` in `.gpr.py` — Gramps' plugin loader injects it. Implementation modules **MUST** bind it explicitly via `_ = glocale.get_addon_translator(__file__).gettext`.
- **MUST NOT**: wrap an f-string or `.format()` result in a translation function. `xgettext` cannot extract dynamically built strings.
  - **Bad:** `_(f"User {name}")`, `_("User {}".format(name))`
  - **Good:** `_("User %s") % name`
- **MUST** (Glade): translatable strings in `.glade` / `.ui` files are **not** picked up by the addon translation tooling — the extractor only sees Python. For each translatable Glade string, give the widget a meaningful `id`, mark the string with `translatable="yes"` (optionally with a `"context|"` prefix), and override the label at runtime in Python: `self.get_widget("place_name_label").set_label(_("place|Name:"))`.
- **SHOULD**: use `ngettext(singular, plural, n)` for plural forms.
- **SHOULD**: use the pipe-prefix form `_("Context|String")` whenever a word could carry multiple senses (e.g. `_("book|Title")` vs `_("person|Title")`). This is the convention used throughout `addons-source` and is what translators see in the `.po` file. The two-arg form `_(msg, context)` works equivalently. **MUST NOT** call `pgettext` or `sgettext` directly — go through `_`.
- **SHOULD**: use `N_("…")` to mark a string for extraction without translating it at call time (e.g. for module-level constants that are translated later when displayed).

## Runtime

- **MUST**: perform every database write inside a `DbTxn`:
  ```python
  with DbTxn(_("Adding example"), db) as trans:
      db.add_person(person, trans)
  ```
- **MUST**: declare runtime imports in `requires_mod` using the *importable* module name (`PIL`), not the PyPI distribution name (`Pillow`).
- **MUST**: verify each `requires_mod` entry with `importlib.util.find_spec("<name>")` on a system with the package installed before publishing.
- **MUST**: use `requires_gi` for GObject-Introspection bindings, with version strings. The version pin **must match what the code actually imports** at runtime — pins can drift between Gramps minors (e.g. GExiv2 handling was rewritten on `maintenance/gramps61` per addons-source PR 829), so verify the pin against the target branch's related code, not just the previous branch's working declaration.
- **SHOULD**: use handles (`PersonHandle`, etc.) for internal traversal; reserve Gramps IDs (`I0001`, …) for user-facing display. Handles are internal and stable; Gramps IDs are user-editable and rewritten in bulk by the Reorder Gramps IDs tool.
- **SHOULD**: import only from `gramps.gen.*`. `gramps.gui.*` and `gramps.plugins.*` are internal to the shipped distribution and break across Gramps versions.
- **SHOULD**: use a module-level logger (`LOG = logging.getLogger(__name__)`); **MUST NOT** use `print()` for diagnostic output.
- **SHOULD**: raise existing exceptions from `gramps.gen.errors` and `gramps.gen.db.exceptions` before inventing a new class.
- **SHOULD**: raise `HandleError` for invalid or missing handles.
- **SHOULD**: compare backlink class names by string. `db.find_backlink_handles(handle)` yields `(class_name, handle)` tuples where `class_name` is `"Person"` / `"Family"` / … as a `str`, not the Python class — `if cls is Person:` always evaluates `False`.
- **MAY**: introduce a new exception class only when none of the existing ones accurately represent the error condition.

## Testing

- **MUST**: use stdlib `unittest` — never `pytest`. Gramps itself standardises on `unittest`, which keeps addon tests contributable upstream.
- **MUST**: name test files `test_*.py` and place them in a `tests/` package alongside the addon module.
- **MUST**: scope platform-specific tests with the correct prefix:

  | Prefix | Where it runs |
  |--------|---------------|
  | `test_*.py`             | All platforms |
  | `test_linux_*.py`       | Linux only |
  | `test_windows_*.py`     | Windows only |
  | `test_integration_*.py` | Linux only — full-pipeline / DB-backed |

- **MUST**: tests run cleanly without the addon's `requires_mod` dependencies installed in the Python that runs them — mock at the import boundary, or skip cleanly with `@unittest.skipUnless(...)`. Mac contributors can't easily install addon deps into the Gramps Python, and there's no Gramps debug-mode on Mac. (Gary Griffin, 2026-05-16.)
- **SHOULD**: ship a regression test with every bug fix that **fails pre-fix and passes post-fix**. Doc-only PRs are the only exception.
- **SHOULD**: prefer `example.gramps`-backed tests over mocked DBs for DB-traversal logic — real data has cross-typed backlinks and ID-normalisation shapes that mocks don't reproduce.
- **MAY**: ship mocked unit tests alongside real-DB tests as complementary coverage.

## Coding style

The full Python coding standard — Black, Python 3.10+ type hints (`X | None`, `list[X]`), Sphinx docstrings, import grouping with comment headers, class-header navigation comments, `cb_` callback prefix — is specified in `../gramps/AGENTS.md` and applies to all Gramps-related Python.

- **MUST**: every new `.py` file carries a GPL-2.0-or-later license header with copyright.
- **MUST**: any code in `gramps.gen.*` does not import from any other Gramps submodule (`gen` stays self-contained). Addon code SHOULD uphold the same discipline against itself: factor pure logic into modules that don't import `gramps.gui.*` so it stays unit-testable without a display.
- **SHOULD**: type-hint all public functions and methods, using Python 3.10+ syntax (`X | None` over `Optional[X]`, `list[X]` over `typing.List[X]`).
- **SHOULD**: use handle / ID types from `gramps.gen.types` (`PersonHandle`, `PersonGrampsID`, ...) rather than bare `str`.
- **SHOULD**: docstring all functions and methods in Sphinx format.
- **SHOULD**: prefix callbacks `cb_*`.
- **SHOULD**: prepend a class-header navigation comment to each class, including `unittest.TestCase` subclasses. (PR 2326 round 2.)
- **SHOULD**: run `black --check` before pushing to repos that enforce it. Gramps core does (pre-commit + CI); addons-source today does NOT.

## Contributor workflow

- **MUST**: one logical fix per PR. Bundling hides mistakes.
- **MUST**: target the right branch:
  - Addon changes (`addons-source`) → `maintenance/gramps60`. The maintainer cherry-picks forward to `gramps61`. (Gary Griffin on addons-source PR 915, 2026-05-24.)
  - Core changes (`gramps`) → `maintenance/gramps61`. Fixes and cleanups go on the current production branch and forward-merge to `master`. (jralls on gramps#2298.)
  - Reviewer instruction on a specific PR wins over the default targeting. (e.g. Nick-Hall on gramps#2299.)
- **MUST**: branch from `upstream/<base>`, not the fork's tracking copy — fork bases drift (e.g. PRs 2315/2316 carried a stray `AGENTS.md` from the fork).
- **MUST NOT**: bump the addon's `version` field in an addons-source PR. The maintainer manages versions centrally. (Caught on PR 911, bug 12572.)
- **MUST**: a bug-fix PR includes a regression test, or an explicit "no test because X" rationale plus a manual repro. "Add the test later" is not an option.
- **MUST**: structure the PR body as **Root cause / Fix / Verified against / Test**, citing `path:lines` on the branch the PR targets.
- **MUST**: reference the Mantis bug — gramps core PRs end the body *and* the commit message with `Fixes #NNNN` (no URL, no padding; PR 2322 is the canonical example). addons-source PRs reference the bug in the body.
- **MUST NOT**: merge across branches. Rebase rather than merge — PRs with merge commits are rejected upstream.
- **MUST NOT**: cosmetically update in-flight upstream PRs. Parity, "rebase is clean," and "branch is behind" are not reasons to force-push. Push only when a specific correctness issue needs fixing.
- **SHOULD**: before writing any fix, check upstream isn't ahead — merged history on the target branch AND `master`, *plus* closed and rejected PRs on the *affected file* (not just the bug number). Closed PRs are signal: a closed-unmerged PR with the same fix shape is the maintainer's "no."
- **SHOULD**: if a PR already exists for the bug, verify it instead of duplicating. Merged → confirm-and-close; open → review and defer to the maintainer; closed → treat as the maintainer's "no."
- **SHOULD**: reproduce against `example.gramps` first — it's the canonical fixture and "couldn't reproduce" is the most common reason a fix stalls in triage.
- **MAY**: open as a draft PR for early review or to publish work-in-progress; mark ready when the change is complete and the author has re-read the diff with fresh eyes.

## Verification before commit

- **MUST**: find a test procedure before committing — local run, dry-run, snippet check. Never commit untested changes.
- **MUST**: treat a green mechanical check (lint, `git cherry-pick` applies, build green, `py_compile` exits 0) as evidence of *that narrow check*, not of correctness. Name what the check verified and what it left unverified.
- **MUST**: after pushing a PR branch, watch the PR's CI checks until they finish (e.g. `gh pr checks <PR#> --watch`). Local pre-commit catches static checks only; test failures surface in CI's actual unit-test run.

## Commit messages

Commit messages are parsed by scripts that update Mantis BT and generate the ChangeLog / News files for releases. Formatting must be followed precisely.

- **MUST**: the first line is a short summary, **≤ 70 characters**.
- **MUST**: the description is separated from the summary by a single blank line, and wrapped at **80 characters**.
- **MUST**: describe the change from the user's perspective. Don't recap the diff — `git diff` exists.
- **SHOULD**: use complete sentences in the description.
- **MUST**: reference another commit by its **full hash**, not a short hash. GitHub auto-hyperlinks full hashes; short hashes in brackets do not link.
- **MUST**: the Mantis trailer is on the **last** line of the commit message, separated from the description by a single blank line.

### Mantis trailer keywords

To **resolve** a bug (closes it on commit):

```
Fixes #12345
Fixed #12345
Resolves #12345
Resolved #12345
Fixes #12345, #67890
```

To **link** to a bug (cross-reference without closing):

```
Bug #12345
Issue #12345
Report #12345
Bugs #12345, #67890
```

Bare numbers (no `#`) and URLs both miss the auto-link — use the `#NNNN` form. Note this is the opposite of the convention *inside* MantisBT itself, where `#NNNN` auto-links to another Mantis issue and bare numbers are preferred; here, inside Git commit messages and GitHub PR bodies, `#NNNN` is what hooks the MantisBT scripts.

For the trailer to wire up on Mantis, the Git **author** or **committer** has to be a developer on the Mantis bug tracker. The Git name must match the Mantis username or real name, or the Git email must match the Mantis email.

### gramps core: trailer at the END

For gramps core PRs both the **PR body** and the **commit message** end with `Fixes #NNNN` (no URL, no padding; PR 2322 is the canonical example). The older URL-at-top form on PR 2317 is the outdated pattern.

### addons-source: bug reference in PR body

addons-source PRs don't use `Fixes #NNNN` in the commit message; reference the Mantis bug in the PR body instead.

## Adding and removing Python files (gramps core only)

When a gramps core PR adds or removes a `.py` file with translatable strings:

- **MUST**: update `po/POTFILES.in` (translatable strings) or `po/POTFILES.skip` (no translatable strings; deliberately excluded).
- **MUST**: remove references from both `po/POTFILES.in` and `po/POTFILES.skip` when a file is deleted.

Local check:

```bash
PYTHONPATH=../../gramps python po/test/po_test.py
```

For addons, the per-addon `po/template.pot` is regenerated by `make.py init <Addon>` (see [12-packagingK-packaging.md)); there is no equivalent of `POTFILES.in` to maintain by hand.

## See also

- [Overview](wiki:Gramps_6.0_Wiki_Manual_-_Addon_Development)
- [Fundamentals](wiki:Gramps_6.0_Wiki_Manual_-_Addon_Development_-_Fundamentals)
- [Testing](wiki:Gramps_6.0_Wiki_Manual_-_Addon_Testing)
- [Code analysis](wiki:Gramps_6.0_Wiki_Manual_-_Addon_Development_-_Code_Analysis)
- [Packaging](wiki:Gramps_6.0_Wiki_Manual_-_Addon_Development_-_Packaging)
- `../gramps/AGENTS.md` — the full Python coding standard inherited here.
- [addons-source CONTRIBUTING.md](https://github.com/gramps-project/addons-source/blob/maintenance/gramps60/CONTRIBUTING.md)
- [Committing policies](https://www.gramps-project.org/wiki/index.php/Committing_policies) — upstream's commit-message + Mantis-trailer rules.

<!--wiki:{{stub}}-->
