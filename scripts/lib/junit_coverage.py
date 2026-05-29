#!/usr/bin/env python3
"""Print ``<total tests> <skipped>`` summed across the JUnit XML in a dir.

Used by the addon-unit runners (local + CI) to tell a run where every test
actually executed from one where every test SKIPPED: both exit 0 from
unittest/xmlrunner, so the exit code alone would mark an all-skipped addon
PASS. Reading the ``tests`` / ``skipped`` attributes off the emitted testsuite
elements is robust and avoids parsing stderr.

Usage: junit_coverage.py <results-dir>   ->   prints e.g. "8 8"
"""

import glob
import os
import sys
import xml.etree.ElementTree as ET


def coverage(results_dir: str) -> tuple[int, int]:
    tests = skipped = 0
    for path in glob.glob(os.path.join(results_dir, "*.xml")):
        try:
            root = ET.parse(path).getroot()
        except ET.ParseError:
            continue
        for suite in root.iter("testsuite"):
            tests += int(suite.get("tests", 0))
            skipped += int(suite.get("skipped", 0))
    return tests, skipped


if __name__ == "__main__":
    total, skip = coverage(sys.argv[1] if len(sys.argv) > 1 else ".")
    print(total, skip)
