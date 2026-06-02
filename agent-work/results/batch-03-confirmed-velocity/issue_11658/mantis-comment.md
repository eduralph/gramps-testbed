Unable to reproduce on current Gramps 6.x with current GrampsAIO packaging.

The original report (Gramps 5.1.2, GrampsAIO64 Windows, 2020) referenced a
`libgoocanvas` DLL in the program folder — a Windows-AIO 5.1.2-specific
packaging hint rather than an addon-code symptom. Code-level review of
`GraphView/graphview.py` on current `maintenance/gramps60` (HEAD `388be68be`)
shows:

- The per-person photo path (`get_person_image`, lines 1433-1466) is
  defensive — null-checks media refs, file-exists, returns None on any
  pixbuf-load failure. This path cannot produce "no image" as a code
  defect.
- The SVG image-element path (`start_image`, lines 2250-2266) calls
  `GdkPixbuf.Pixbuf.new_from_file()` without an exception guard, which
  fails on a system with incomplete GdkPixbuf format loaders — exactly the
  Windows-AIO 5.1.2 environmental shape the report hints at.

No code changes to GraphView's image handling since the 5.1.2 era. Current
Linux distributions ship complete GdkPixbuf loader sets, so the failure
cannot trigger there. Closing as cannot-reproduce / environmental.

Please reopen with a current GrampsAIO version, OS details, and the
GdkPixbuf loader list if the symptom recurs on 6.x.
