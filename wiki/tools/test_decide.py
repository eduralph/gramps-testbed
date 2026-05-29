#!/usr/bin/env python3
"""Offline tests for the publisher's decision matrix -- no browser, no network.
This is the safety-critical logic (drift detection), so it gets pinned."""

import unittest

import publish as P


class DecideMatrix(unittest.TestCase):
    SC = {"pushed_revid": 100, "generated_hash": "AAA"}

    def test_create_when_unknown_and_absent(self):
        a, _ = P.decide(
            sidecar=None, live_exists=False, live_revid=None, generated_hash="X"
        )
        self.assertEqual(a, P.CREATE)

    def test_adopt_conflict_when_unknown_but_present(self):
        # never published by us, yet it exists on the wiki -> do NOT clobber
        a, _ = P.decide(
            sidecar=None, live_exists=True, live_revid=55, generated_hash="X"
        )
        self.assertEqual(a, P.ADOPT_CONFLICT)

    def test_skip_when_source_unchanged(self):
        a, _ = P.decide(
            sidecar=self.SC, live_exists=True, live_revid=100, generated_hash="AAA"
        )
        self.assertEqual(a, P.SKIP)

    def test_update_when_source_changed_and_no_drift(self):
        a, _ = P.decide(
            sidecar=self.SC, live_exists=True, live_revid=100, generated_hash="BBB"
        )
        self.assertEqual(a, P.UPDATE)

    def test_drift_when_wiki_revid_moved(self):
        # human edited the wiki since our push -> never silently overwrite
        a, _ = P.decide(
            sidecar=self.SC, live_exists=True, live_revid=101, generated_hash="BBB"
        )
        self.assertEqual(a, P.DRIFT)

    def test_drift_takes_priority_over_unchanged_source(self):
        # even if our source is unchanged, a moved revid is still drift
        a, _ = P.decide(
            sidecar=self.SC, live_exists=True, live_revid=101, generated_hash="AAA"
        )
        self.assertEqual(a, P.DRIFT)

    def test_deleted_on_wiki(self):
        a, _ = P.decide(
            sidecar=self.SC, live_exists=False, live_revid=None, generated_hash="AAA"
        )
        self.assertEqual(a, P.DELETED_ON_WIKI)


if __name__ == "__main__":
    unittest.main(verbosity=2)
