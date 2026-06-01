---
title: Gramps 6.0 Wiki Manual - Addon Development - Testing
categories:
  - Addons
  - Developers
  - Gramps 6.0
managed: true
---

<!--
  Sources:
    - per-OS filename prefixes from addons-source ci.yml
    - dotted-path loading from upstream ci.yml
    - example.gramps vs mocks
    - requires_mod no-deps rule (Gary Griffin, 2026-05-16)
    - tests/__init__.py convention (Gary Griffin's PR 930)
  Cross-link to 09-debug for repro scripts, 10-troubleshoot for what
  these tests catch.
-->

## Overview

How to test an addon without launching the GUI on every iteration — the test framework, the layout conventions, the fixtures that work, and the platform-aware rules that keep tests portable across Linux, Windows, and Mac.

A working test suite is what makes an addon **maintainable across Gramps releases**. The matrix of (Gramps version × OS) makes manual testing impossible at scale; the per-OS prefix conventions below let a single CI matrix verify your addon against every supported combination automatically.

## Framework: stdlib `unittest`

Use stdlib `unittest`. Don't use pytest.

Gramps itself standardises on `unittest` (subclasses of `unittest.TestCase`), which keeps addon tests contributable upstream without a framework-conversion step. Mixing pytest features (fixtures, parametrise, plugins) breaks contribution upstream where pytest isn't installed.

```python
import unittest


class MyAddonTests(unittest.TestCase):
    def test_handles_empty_input(self):
        # ...
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
```

### Class header convention

The "class header navigation comment" rule from gramps' AGENTS.md is unconditional — it applies to `unittest.TestCase` subclasses too. PR 2326 round 2 caught the omission:

```python
# ------------------------------------------------------------
#
# MyAddonTests
#
# ------------------------------------------------------------
class MyAddonTests(unittest.TestCase):
    ...
```

## Layout

Each addon ships its tests in a `tests/` subpackage:

```
MyAddon/
├── MyAddon.gpr.py
├── MyAddon.py
└── tests/
    ├── __init__.py            # marker — see below
    └── test_myaddon.py
```

### Why `tests/__init__.py` exists

The marker is **hygiene, not a bug fix**. Python 3.3+'s implicit namespace packages (PEP 420) mean a directory without `__init__.py` is still importable; dotted-path loading (`python3 -m unittest MyAddon.tests.test_myaddon`) works either way. But:

1. **Explicit beats implicit.** "It works" is currently true by accident of invocation. The same code breaks the moment something uses `discover` or assumes regular packages.
2. **It's the prerequisite for centralisation.** Shared per-addon test setup — fixtures, the GTK-pin contract, presence meta-tests — has no home until `tests/__init__.py` exists. Empty marker now, contract-bearing later.

The convention crystallises as: every addon's `tests/` **should** have an `__init__.py`; the addon directory itself **should not**.

The asymmetry matters. The addon directory must remain a plain namespace dir — Gramps' plugin loader puts the addon dir on `sys.path` and imports `<Addon>.py` by name. Making the addon dir a regular package can disturb plugin loading (and the [Mantis 12691](https://gramps-project.org/bugs/view.php?id=12691) namespace trap lives in exactly this area). The `tests/` subfolder has no such constraint, so making it an explicit package is free.

This is what [addons-source PR 930](https://github.com/gramps-project/addons-source/pull/930) (Gary Griffin) is moving toward.

## Filename conventions (addons-source CI)

addons-source's CI workflow filters tests by **filename prefix** to scope them per platform:

| Prefix                  | Where it runs                                  |
|-------------------------|------------------------------------------------|
| `test_*.py`             | All platforms (Linux + Windows)                |
| `test_linux_*.py`       | Linux only                                     |
| `test_windows_*.py`     | Windows only                                   |
| `test_integration_*.py` | Linux only — full-pipeline / DB-backed         |

The Ubuntu runner skips `test_windows_*`; the Windows runner skips both `test_linux_*` and `test_integration_*`. Both runners include the platform-neutral `test_*.py` files.

**Pick the prefix that matches the test's portability**, not the platform you happen to be developing on. A test that exercises POSIX file paths goes under `test_linux_*`; a test that exercises win32 locale handling goes under `test_windows_*`; everything else, the plain `test_*.py` prefix.

CI's workflow file is authoritative: [addons-source/.github/workflows/ci.yml](https://github.com/gramps-project/addons-source/blob/maintenance/gramps60/.github/workflows/ci.yml).

## Loading: dotted path, not `discover`

Upstream CI loads tests by **dotted path**:

```bash
python3 -m unittest MyAddon.tests.test_myaddon
```

Not by `discover` from a `tests/` directory. The reason: dotted-path loading surfaces the namespace-package trap. Bug 12691 — `from <Addon> import <Addon>` binding the submodule instead of the class — only shows up under dotted-path loading. `discover`-based loading walks files by *filename*, hiding the import-resolution issue. Mirroring CI's invocation locally catches what CI catches.

Locally, from the `addons-source` root, the same invocation works:

```bash
# Run one test module
python3 -m unittest MyAddon.tests.test_myaddon

# Run every test in the addon's tests/ package
python3 -m unittest discover -s MyAddon/tests -t .
```

The discover form here works because the addon directory is the import root — the namespace-package trap shows up only when an *individual addon module* mis-imports itself.

## Mocked vs `example.gramps`-backed tests

Two complementary strategies. They're not alternatives.

### Mocked unit tests

Fast, no DB on disk, suitable for tight branch-coverage of pure logic. Substitute the database with a stub that returns fixed objects:

```python
import unittest
from unittest.mock import MagicMock


class HappyPathTests(unittest.TestCase):
    def test_skips_people_without_birth(self):
        person = MagicMock()
        person.get_birth_ref.return_value = None

        result = pure_logic(person)

        self.assertEqual(result, expected)
```

The MagicMock approach has a built-in failure mode: it returns something for *every* method call, so a typo'd method name appears to work. Real DB code that fails on the next call will pass the mocked test. This is the bug the next strategy catches.

### `example.gramps`-backed tests

`example.gramps` ships with the Gramps source under `example/gramps/example.gramps`. It's the canonical fixture triage and developers reproduce against; loading it produces a real populated database with the cross-typed backlinks, ID normalisations, and absent optional fields that real users hit.

```python
import os
import unittest
from gramps.gen.db.utils import open_database


class IntegrationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.db = open_database(
            os.path.expanduser("~/path/to/gramps/example/gramps/example.gramps")
        )

    def test_handles_real_data(self):
        result = code_under_test(self.db)
        self.assertGreater(len(result), 0)
```

Name these `test_integration_*.py` so CI scopes them to Linux only (loading a real DB is heavier, and Windows CI's Gramps setup is separately constrained — see [13-compatibility → Windows toolchain migrated to UCRT64L-compatibility.md#windows-toolchain-migrated-to-ucrt64)).

### Choosing between them

| Use the mock when                                 | Use `example.gramps` when                                 |
|---------------------------------------------------|-----------------------------------------------------------|
| The function under test takes pure inputs         | The function traverses the DB                             |
| You're covering many input shapes (loop / branch) | You're verifying *one* real-world scenario                |
| You need sub-millisecond turnaround               | You need real-data shape (backlinks, IDs, optional refs)  |

The lesson, learned the hard way: mocked tests can pass while real-DB tests fail, because the mock doesn't model what production data looks like.

## Tests must run without `requires_mod` deps

A hard constraint, set by Gary Griffin (2026-05-16): addon tests must run cleanly without the addon's `requires_mod` dependencies installed in the Python that runs them. Mac contributors can't easily install addon deps into the Gramps Python on macOS, and there's no Gramps debug-mode equivalent on Mac to work around it.

Two ways to honour this:

### Mock at the import boundary

```python
import sys
from unittest.mock import MagicMock

# Stand in for an optional dep before importing the addon.
sys.modules.setdefault("PIL", MagicMock())
sys.modules.setdefault("PIL.Image", MagicMock())

from MyAddon.MyAddon import code_under_test
```

Cleaner than try/except, and the test asserts the addon's behaviour **with the dep present** — what almost every real user sees.

### Skip cleanly

When mocking is impractical (e.g. the dep is core to the function under test), skip without erroring:

```python
import unittest
from importlib.util import find_spec


@unittest.skipUnless(find_spec("PIL"), "Pillow not installed")
class PhotoTaggingTests(unittest.TestCase):
    def test_loads_jpeg(self):
        ...
```

A failed import at module load — instead of a `skipUnless` — turns into a test error on the Mac runner, blocking the CI suite.

## What to test

Mandatory:

- **The bug a fix closes.** Every bug fix ships with a test that fails pre-fix and passes post-fix. This is a [16-guidelines MUSTN-guidelines.md#testing). Doc-only PRs are the only exception.

Strongly recommended:

- **One happy-path call** through the addon's main entry point. The smoke test that catches the next breakage.
- **One real-data scenario** against `example.gramps` for any DB-traversal code.

Optional but valuable:

- **Edge cases** the function explicitly handles: empty DB, missing optional fields, IDs at the boundaries of normalisation.

What *not* to test:

- The Gramps API itself. If `db.get_person_from_handle(h)` returns `None` for a missing handle, that's Gramps' contract; your test exercises that **your code handles `None`**, not that Gramps returns it.

## What the test catches that the GUI doesn't

A test surfaces failure modes the GUI cycle hides:

- **The namespace-package trap** (bug 12691) — surfaces under dotted-path loading.
- **`requires_mod` typos** — `from <pypi-name> import …` would fail import; surfaces immediately at test load.
- **DB-shape assumptions** — the cross-typed-backlinks / ID-norm issues that mocked tests miss.
- **Per-OS regressions** — running on both runners.

See [10-troubleshoot](10-troubleshoot.md) for the symptoms-to-cause mapping for these classes of failure.

## Running tests locally

From the `addons-source` checkout root:

```bash
# Run one addon's tests
python3 -m unittest discover -s MyAddon/tests -t .

# Or invoke a single test module by dotted path (mirrors CI's invocation)
python3 -m unittest MyAddon.tests.test_myaddon
```

The Python that runs the tests needs `gramps` importable. The simplest setup is `PYTHONPATH=/path/to/gramps python3 -m unittest …`; if Gramps is installed system-wide, the import resolves without `PYTHONPATH`.

On Windows, run from the MSYS2 UCRT64 shell against a UCRT64-installed Gramps — the AIO build for Gramps 6.1+ targets UCRT64; Gramps 6.0 isn't Windows-tested upstream. See [13-compatibility → Windows toolchain migrated to UCRT64L-compatibility.md#windows-toolchain-migrated-to-ucrt64).

## See also

- [05-fundamentals → Logging](05-fundamentals.md#logging) — `LOG` setup that tests assert against.
- [06-data-access → Testing data access](06-data-access.md#testing-data-access) — DB-API patterns to exercise.
- [09-debug](09-debug.md) — turning a repro script into a test.
- [10-troubleshoot](10-troubleshoot.md) — the symptoms these tests catch in CI rather than production.
- [11-code-analysis](11-code-analysis.md) — what the static checkers verify before tests run.
- [16-guidelines → TestingN-guidelines.md#testing) — normative rules.
- [Mantis 12691](https://gramps-project.org/bugs/view.php?id=12691) — the canonical namespace-package trap that motivates dotted-path loading.
- [addons-source PR 930](https://github.com/gramps-project/addons-source/pull/930) — `tests/__init__.py` convention.

<!--wiki:{{stub}}-->
