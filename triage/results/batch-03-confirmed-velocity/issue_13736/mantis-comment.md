PR open against `maintenance/gramps61`: p:gramps:NNNN: — improves the
"Addon Registration Failed" dialog so it names the failing addon, the
running Gramps major.minor, and points at
Edit → Preferences → Addon Manager → Projects (the canonical fix
location when the dialog fires because a project URL indexes a
catalogue whose gramps_target_version no longer matches the running
Gramps — the scenario bamaustin traces in the original report and the
Discourse threads).

Includes a headless regression test under
gramps/gui/plug/test/windows_test.py asserting the dialog text contains
the addon id, the running major_version, and "Projects".
