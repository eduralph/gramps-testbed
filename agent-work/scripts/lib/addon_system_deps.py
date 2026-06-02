#!/usr/bin/env python3
"""
Single source of truth for addon *system* dependencies.

Gramps addons declare three kinds of dependency in their ``.gpr.py``:

* ``requires_mod`` — importable Python modules. These are pip-installable and
  are auto-derived from the ``.gpr.py`` files at container/run start (see
  ``agent-work/scripts/<platform>/run-addon-unit.sh``); they need nothing here.
* ``requires_gi`` — GObject-introspection typelibs (e.g. ``GooCanvas``).
* ``requires_exe`` — system executables (e.g. ``dot`` from graphviz).

The latter two are *system* packages: they are NOT pip-installable, their
package names differ per platform, and Gramps' own ``Requirements`` only
*checks* them, never installs them. They therefore have to be provided by the
environment (baked into the Docker image, installed via apt in CI, or via
pacman on MSYS2). Historically each platform hand-maintained its own list,
which drifted (the Ubuntu image lacked ``graphviz`` while Windows had it; both
lacked the GeocodeGlib typelib).

This module is the one place that:

1. maps each declared GI namespace / executable to its per-platform package
   (``GI_PACKAGES`` / ``EXE_PACKAGES`` below), and
2. scans the addons for what they actually declare,

so every consumer (the Ubuntu Dockerfile, the apt step in CI, the MSYS2 pacman
lists, and the drift-guard test) derives from the same data instead of a
hand-copied list. Adding a new system dep means adding one row here.

Pure stdlib so it can run at image-build time before Gramps is installed.

CLI::

    # packages to install for a platform (space-separated, by-name only)
    addon_system_deps.py --platform ubuntu
    addon_system_deps.py --platform windows            # pacman -S names
    addon_system_deps.py --platform windows --urls     # pacman -U pinned URLs

    # drift-guard helpers
    addon_system_deps.py --unmapped   <addons-source-dir>   # declared but not mapped
"""

# ------------------------
# Python modules
# ------------------------
from __future__ import annotations

import argparse
import ast
import glob
import os
import re
import sys

# ---------------------------------------------------------------------------
# The map. Keys are the names addons declare; values give the package that
# provides that dependency on each platform.
#
#   "install": False  -> recognised for completeness but not auto-installed
#                        (e.g. no satisfying package exists on the platform).
#   "windows" value of the form "url:<URL>" -> installed with `pacman -U`
#                        (a version-pinned package), not `pacman -S <name>`.
# ---------------------------------------------------------------------------

# requires_gi namespace -> per-platform package providing the typelib.
GI_PACKAGES: dict[str, dict] = {
    "GExiv2": {
        "ubuntu": "gir1.2-gexiv2-0.10",
        "windows": "mingw-w64-ucrt-x86_64-gexiv2",
    },
    "GooCanvas": {
        "ubuntu": "gir1.2-goocanvas-2.0",
        "windows": "mingw-w64-ucrt-x86_64-goocanvas",
    },
    "OsmGpsMap": {
        "ubuntu": "gir1.2-osmgpsmap-1.0",
        "windows": "mingw-w64-ucrt-x86_64-osm-gps-map",
    },
    # PlaceCoordinateGramplet declares GeocodeGlib 1.0, but modern distros ship
    # only the 2.0 typelib (no package provides namespace version 1.0), so it
    # cannot be satisfied. The addon also ships no test suite, so the presence
    # guard skips it and nothing is auto-installed. The entry exists only so
    # the completeness guard recognises the namespace rather than flagging it
    # as unmapped drift.
    "GeocodeGlib": {
        "ubuntu": None,
        "windows": None,
        "install": False,
        "note": "addon declares 1.0; distros ship only 2.0; addon has no tests",
    },
}

# requires_exe executable -> per-platform install token.
EXE_PACKAGES: dict[str, dict] = {
    # MSYS2 graphviz is version-pinned via URL (matches agent-work/scripts/windows/
    # run-unit.sh; newer pacman builds broke pygraphviz/rendering).
    "dot": {
        "ubuntu": "graphviz",
        "windows": (
            "url:https://repo.msys2.org/mingw/ucrt64/"
            "mingw-w64-ucrt-x86_64-graphviz-12.2.1-4-any.pkg.tar.zst"
        ),
    },
}

PLATFORMS = ("ubuntu", "windows")


# ------------------------------------------------------------
#
# scanning helpers
#
# ------------------------------------------------------------
_GI_RE = re.compile(r"requires_gi\s*=\s*(\[[^\]]*\])")
_EXE_RE = re.compile(r"requires_exe\s*=\s*(\[[^\]]*\])")


def _gpr_files(addons_dir: str) -> list[str]:
    return sorted(glob.glob(os.path.join(addons_dir, "*", "*.gpr.py")))


def _literal(list_src: str):
    try:
        return ast.literal_eval(list_src)
    except (ValueError, SyntaxError):
        return []


def scan_gi_namespaces(addons_dir: str) -> set[str]:
    """Return the set of GI namespaces declared by any addon."""
    names: set[str] = set()
    for path in _gpr_files(addons_dir):
        try:
            text = open(path, encoding="utf-8").read()
        except OSError:
            continue
        for m in _GI_RE.finditer(text):
            for entry in _literal(m.group(1)):
                # entry is (namespace, version) or just namespace
                ns = entry[0] if isinstance(entry, (tuple, list)) else entry
                if ns:
                    names.add(ns)
    return names


def scan_executables(addons_dir: str) -> set[str]:
    """Return the set of executables declared by any addon."""
    exes: set[str] = set()
    for path in _gpr_files(addons_dir):
        try:
            text = open(path, encoding="utf-8").read()
        except OSError:
            continue
        for m in _EXE_RE.finditer(text):
            for entry in _literal(m.group(1)):
                if entry:
                    exes.add(entry)
    return exes


def scan_addon_requirements(addon_dir: str) -> tuple[set[str], set[str]]:
    """
    Return (gi_namespaces, executables) declared by a single addon directory.
    """
    gi: set[str] = set()
    exe: set[str] = set()
    for path in sorted(glob.glob(os.path.join(addon_dir, "*.gpr.py"))):
        try:
            text = open(path, encoding="utf-8").read()
        except OSError:
            continue
        for m in _GI_RE.finditer(text):
            for entry in _literal(m.group(1)):
                ns = entry[0] if isinstance(entry, (tuple, list)) else entry
                if ns:
                    gi.add(ns)
        for m in _EXE_RE.finditer(text):
            for entry in _literal(m.group(1)):
                if entry:
                    exe.add(entry)
    return gi, exe


def scan_addon_gi_specs(addon_dir: str) -> list[tuple[str, str]]:
    """
    Return the (namespace, version) GI specs declared by an addon directory.

    The version string may be comma-separated alternatives, e.g.
    ``("GooCanvas", "2.0,3.0")``; the empty string means no version given.
    """
    specs: list[tuple[str, str]] = []
    for path in sorted(glob.glob(os.path.join(addon_dir, "*.gpr.py"))):
        try:
            text = open(path, encoding="utf-8").read()
        except OSError:
            continue
        for m in _GI_RE.finditer(text):
            for entry in _literal(m.group(1)):
                if isinstance(entry, (tuple, list)) and entry:
                    ns = entry[0]
                    ver = entry[1] if len(entry) > 1 else ""
                    if ns:
                        specs.append((ns, ver))
                elif entry:
                    specs.append((entry, ""))
    return specs


# ------------------------------------------------------------
#
# package-list derivation
#
# ------------------------------------------------------------
def _installable(entry: dict, platform: str):
    if entry.get("install", True) is False:
        return None
    return entry.get(platform)


def packages_by_name(platform: str) -> list[str]:
    """
    All install-by-name packages for a platform (the full mapped set).

    Used by the image build / pacman -S list: a generic image installs every
    mapped dependency so any addon that reuses one works without a rebuild.
    """
    pkgs: list[str] = []
    for table in (GI_PACKAGES, EXE_PACKAGES):
        for entry in table.values():
            pkg = _installable(entry, platform)
            if pkg and not str(pkg).startswith("url:"):
                pkgs.append(pkg)
    return sorted(set(pkgs))


def packages_by_url(platform: str) -> list[str]:
    """Pinned-URL packages for a platform (pacman -U), e.g. MSYS2 graphviz."""
    urls: list[str] = []
    for table in (GI_PACKAGES, EXE_PACKAGES):
        for entry in table.values():
            pkg = _installable(entry, platform)
            if pkg and str(pkg).startswith("url:"):
                urls.append(str(pkg)[len("url:") :])
    return sorted(set(urls))


def unmapped(addons_dir: str) -> tuple[set[str], set[str]]:
    """
    Declared deps that have no entry in the maps (drift-guard input).

    Returns (unmapped_gi_namespaces, unmapped_executables).
    """
    gi = scan_gi_namespaces(addons_dir)
    exe = scan_executables(addons_dir)
    return (gi - set(GI_PACKAGES), exe - set(EXE_PACKAGES))


# ------------------------------------------------------------
#
# CLI
#
# ------------------------------------------------------------
def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--platform", choices=PLATFORMS)
    parser.add_argument(
        "--urls",
        action="store_true",
        help="with --platform: print pinned-URL packages (pacman -U) instead "
        "of by-name packages",
    )
    parser.add_argument(
        "--unmapped",
        metavar="ADDONS_DIR",
        help="print declared GI/exe deps that have no map entry, then exit "
        "non-zero if any",
    )
    args = parser.parse_args(argv)

    if args.unmapped:
        gi, exe = unmapped(args.unmapped)
        for ns in sorted(gi):
            print(f"gi:{ns}")
        for e in sorted(exe):
            print(f"exe:{e}")
        return 1 if (gi or exe) else 0

    if args.platform:
        items = (
            packages_by_url(args.platform)
            if args.urls
            else packages_by_name(args.platform)
        )
        print(" ".join(items))
        return 0

    parser.error("nothing to do: pass --platform or --unmapped")
    return 2


if __name__ == "__main__":
    sys.exit(main())
