---
title: Addon Testing Guidelines
categories:
  - Addons
  - Developers
managed: false
status: draft
---

## Goal

In order to improve overall code quality and ensure that the addons continue to function as gramps evolves, unit testing and quality control guidelines should help the fledgling addon developer build good unit tests.

## Context

Issues in existing addon unit tests triggered the discovery that they have a dependency on Gtk 3.0 and Gdk 3.0 which the Addon Manager in Gramps automatically pins and covers for them at runtime. Unfortunately unit tests do not have the full Gramps environment available, and we need to satisfy this dependency in a different fashion. This and other aspects mean that we need to define a baseline for testing if we want to declare an addon as "Stable". These notes serve as a repository for those baseline items, which we will use later.

## Notes

### `<addon>/tests/__init__.py` must exist

Because **Python 3.3+ has implicit namespace packages (PEP 420)**: a directory with no `__init__.py` is _still_ importable as a package. And both upstream CI and our testbed runner load tests by **dotted path** — `python3 -m unittest <Addon>.tests.<module>` — which is exactly the case namespace packages handle fine. I just demonstrated it: `MyAddon.tests.test_demo` ran green with **zero** `__init__.py` anywhere, and even two addons with an identically-named `test_integration` module loaded fine (their fully-qualified names — `AddonA.tests.test_integration` vs `AddonB.tests.test_integration` — are distinct, so no clash). <!-- TODO: capture the demo as a runnable snippet (or repo path) before this graduates to CONTRIBUTING — the "I just demonstrated it" claim needs to be reproducible. -->

So nothing was broken. The dotted-path happy path works on namespace-package behavior. The `__init__.py` only starts to matter when you leave that path:

- **`discover`-based loading** (loads by _filename_, which can collide across folders),
- tooling that assumes regular packages,
- certain `sys.path` / name-collision setups.

The testbed deliberately uses dotted-path, _not_ `discover` — and note CLAUDE.md's point is about the **opposite** trap: dotted-path loading _surfaces_ the addon-**module**-level namespace trap ([Mantis 12691](https://gramps-project.org/bugs/view.php?id=12691): `from <Addon> import <Addon>` binding the submodule). That's a different thing from the `tests/` marker, and it's why dotted-path is preferred. The missing `tests/__init__.py` simply never bit because namespace packages covered it.

#### The asymmetry worth noticing

[Gary's PR](https://github.com/gramps-project/addons-source/pull/930) (addons-source#930) adds `<Addon>/tests/__init__.py` but **not** `<Addon>/__init__.py`. That's deliberate and correct:

- The **addon directory must stay a plain namespace dir** — gramps' plugin loader puts the addon dir on `sys.path` and imports `<Addon>.py` by name. Making the addon dir a regular package could disturb plugin loading. (It's also where the [Mantis 12691](https://gramps-project.org/bugs/view.php?id=12691) trap lives.)
- The **`tests/` subfolder has no such constraint**, so making it an explicit package is free and beneficial. PEP 420 happily lets a _regular_ `tests` subpackage live under a _namespace_ addon dir.

#### What it means as convention

The honest framing: **adding `tests/__init__.py` is hygiene, not a bug fix.** Nothing is failing today. But:

1. **Explicit beats implicit.** "It works" is currently true _by accident of invocation_ — same smell as the silent-skip and the mocked-DB-passing-by-luck we hit earlier today. The thing works until someone runs `discover`, or a tool assumes regular packages, or GTK 4 becomes default. A convention that _requires_ `tests/__init__.py` makes the guarantee deterministic across invocation methods, instead of leaning on namespace-package luck.

2. **It's the prerequisite for centralization.** You can't put a shared per-addon thing in `tests/__init__.py` — the GI contract (#43 <!-- TODO: disambiguate — addons-source issue? gramps-project/gramps PR? include full owner/repo#NN -->), common fixtures, a presence meta-test — if the file doesn't exist. Gary's PR is the _foundation_; #43 is what would _fill_ it. That's why the two are connected: empty markers now, contract-bearing later.

3. **So the convention crystallizes as:** every addon `tests/` **should** have an `__init__.py`; the addon dir itself should **not**. Empty is fine when it's just a marker; non-empty when it hosts shared setup.

The clean way to state it in `addons-source` docs (CONTRIBUTING/ci.yml comment): _"Each addon's `tests/` is a package — include an `__init__.py`. Tests are loaded by dotted path; the marker keeps loading deterministic and gives a home for shared test setup. Do not add `__init__.py` to the addon directory itself — the plugin loader requires it to remain a plain directory."_

That's the takeaway: Gary's PR isn't fixing a live break — it's converting an implicit, works-by-luck arrangement into an explicit convention, which is also what makes the GTK-pin centralization (#43) possible and enforceable later.

## Open questions

- [ ]

## References

<!-- Links worth keeping. Mix wikilinks to other notes, GitHub URLs, Mantis
     bug URLs, file paths. Whatever you want to find again. -->

- [Mantis 12691 — `from <Addon> import <Addon>` submodule binding trap](https://gramps-project.org/bugs/view.php?id=12691)
- PEP 420 — Implicit namespace packages: <https://peps.python.org/pep-0420/>
- [addons-source#930](https://github.com/gramps-project/addons-source/pull/930) — Gary's `tests/__init__.py` PR
- "#43" — <!-- TODO: resolve to <owner>/<repo>#NN; the GI contract / GTK-pin centralization issue -->

## Next step

<!-- The single concrete action that moves this forward, or the reason it's
     parked. If neither exists, the note is done — archive or delete. -->
