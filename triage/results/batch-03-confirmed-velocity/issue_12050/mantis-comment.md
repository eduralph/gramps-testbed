Per the investigation in this thread (notes ~0061351 from lordemannd and
~0061365 from prculley), the SQLite import is not hung. It completes — just
far slower than the XML import path (~8 hours for ~95k people versus minutes
for the same data via XML). This is a known design tradeoff in the SQLite
addon: the import iterates one normalized table row at a time, where the core
database uses a single blob per object specifically to avoid the per-object
overhead this produces.

Closing as no-change-required (working as intended).

The one actionable follow-up raised in the thread — an Abort button so users
need not force-kill Gramps mid-import — is a UI enhancement to the addon,
separate from this defect report. If pursued, please file it as a new feature
request and reference it from here.
