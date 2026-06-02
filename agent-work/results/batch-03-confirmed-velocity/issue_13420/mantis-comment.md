# Mantis 13420 — ready-to-paste comment (Eduard)

(Bare bug numbers per the no-`#`-prefix convention; addons-source
PRs need the full GitHub URL — no shorthand.)

---

Could not reproduce on conformant Gramps XML.

I built a minimal test XML — one person, Birth + Death events
both `role="Primary"`, standard Gramps handles (no UUIDs), events
listed BEFORE people in the document order the core importer
requires — and ran it through the Text Import gramplet's
`AtomicGrampsParser`. The person's `get_death_ref()` resolved to
the Death event without any manual editor re-save. Same for
`get_birth_ref()`.

The fallback-setting logic lives in gramps core at
`gramps/plugins/importer/importxml.py:1434-1473` (`start_eventref`)
and the parser spells out its own precondition at line 1451-1452:

  "We count here on events being already parsed prior to parsing
  people or families. This code will fail if this is not true."

If the event handle doesn't resolve — because the events block is
listed AFTER people, or because the handle scheme doesn't match
between events and `eventref hlink` attributes (UUID handles, as
snoiraud noted in note 8) — `start_eventref` silently early-
returns and the death_ref never gets set. Re-saving via the editor
then sets it explicitly, which matches the workaround you
described.

So the cause is most likely the XML your Android tool produced
(UUID handles and/or events-after-people document order), not the
gramplet. Closing as cannot-reproduce / invalid input.

If you can reproduce with strictly-conformant Gramps XML
(events-block first, standard Gramps handles), please reopen and
attach that XML — that would point at a real defect.

A regression test in `ImportGramplet/tests/` now pins this
contract (clean XML → AtomicGrampsParser → death_ref set) so a
future refactor of the atomic parser can't silently break the
fallback wiring.

PR (test-only regression guard, not a fix):
https://github.com/gramps-project/addons-source/pull/921
Commit: 184220420 on maintenance/gramps60

Resolution: unable to reproduce
