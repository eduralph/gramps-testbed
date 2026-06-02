This is fixed. The diagnosis in the report (and in note 1) was correct: in the
Family Editor save transaction the child-reference lists were diffed with set
operations on the ChildRef objects, which Python compares by identity. The two
lists held different instances of the same children, so the difference marked
every child as both removed and re-added, and the resulting
remove/add-parent-family cycle dropped the parent-family ordering.

The fix compares the lists by handle instead of object identity, so an edit that
leaves the child set unchanged produces no remove/add cycle and the order is
preserved.

Fixed in PR p:gramps:2266: (commit f7c6444a34273f421b11cab3bbe635de612649be) on
the maintenance/gramps61 branch.

Fixed in version: 6.1.0.
