# Mantis 13979 — draft note (Eduard to paste once the PR is opened)

(Bare bug numbers per the no-`#`-prefix convention; addons-source
PRs linked with the full GitHub URL — `p:gramps:` shorthand applies
only to the gramps core repo.)

---

Triage finding: this is in the addons-source Plugin Manager Enhanced
addon, not the core Addon Manager nor an external repo.

Root cause: `PluginStatus.__info` (PluginManager.py:655) does
`txt = " ".join(req_lst[0])`, where `req_lst` is the second element
of each `[label, table]` pair returned by gramps core's
`Requirements.info`. That core API emits a label + empty table
whenever the addon listing has a present-but-empty requires key —
i.e. `"rm": []`, `"rg": []`, or `"re": []`. Indexing `req_lst[0]`
then raises `IndexError: list index out of range`.

PostgreSQL Enhanced declares `requires_exe=[]` in its `.gpr.py`,
which lands in `addons-en.json` as `"re": []`. A scan of the current
`addons/gramps61/listings/addons-en.json` confirms it is the only
addon shipping with a present-but-empty requires key — which is why
only its row trips the crash.

Fix (PR https://github.com/gramps-project/addons-source/pull/916):
skip empty tables in the iteration — indexing fails on them and
there is nothing meaningful to render anyway. Three-line guard at the
top of the iteration body. Targets `maintenance/gramps61`. Ships a
regression test (`PluginManager/tests/test_info_empty_requires.py`)
that uses `__new__`-bypass to drive `__info` directly against an
addon dict shaped like the live PostgreSQL Enhanced listing entry;
pre-fix the test fails with the reported traceback, post-fix it
passes. The test class skips cleanly on hosts without a Gtk display
(addon imports Gtk at module load); under `xvfb-run` or a real
desktop it runs.

Related items not bundled (per the one-issue-per-ticket rule):

- gramps core's `Requirements.info` could be hardened so it never
  emits a label + empty table pair. That is a cleaner contract
  (matches what every existing consumer assumes) but is a separate
  cleanup. The user-visible crash is fully resolved by the addon
  fix.
- lordemannd's note 2 reports a second symptom — the core Addon
  Manager claims "install succeeded" but the addon is not actually
  installed and can be "installed" again. That is a different
  defect, possibly in core, possibly the same addon, and is not
  addressed here. Worth filing as its own Mantis if it still
  reproduces against current `maintenance/gramps61`.

Suggested tracker action: leave as confirmed until the PR merges;
no version bump needed (addons-source maintainer manages addon
versions centrally).
