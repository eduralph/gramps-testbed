# CodeQL — add LAST, only for the residual flow class

Do NOT start here. Bring up pyright (tuned) and Semgrep first. CodeQL earns its place
ONLY for the patterns the other two demonstrably can't catch — the flow-dependent
residual, chiefly the A2 INIT half (14177: attribute read before __init__ completes on
some path) and any deep None-flow pyright's type layer misses.

## Why it's last
- Heaviest: builds a code database (compile-like step), CI-tier not in-editor, and QL is
  a real query language with a learning curve.
- Its power (path-sensitive dataflow) is only NEEDED for flow bugs. If Semgrep+pyright
  retire enough of the classes, you may not need it — decide AFTER they're tuned.

## Setup (when you get here)
- Free for open-source on public GitHub: runs as a GitHub Action (github/codeql-action),
  results in the repo Security tab. For local: install the CodeQL CLI + VS Code CodeQL
  extension, build a db:  codeql database create gramps-db --language=python
- Start from the standard python query suite, then write ONE custom query for the
  init-order pattern: "is there a path where self.$ATTR is read but not assigned before
  that read in __init__/lifecycle". This is genuine dataflow — QL's wheelhouse, Semgrep's
  blind spot.

## The labeled case it must catch
- 14177: EditPrimary.__init__ raises before ManagedWindow.show() sets self.opened; later
  close_item reads self.opened. Positive control for the init-order query.

## "Ready" for CodeQL
Flags 14177's pre-fix read-before-set path; silent on the d83fff3b62-fixed close() path.
Zero FP on gramps/gui/. Same precision bar — but CI-tier, so a bit more FP tolerance than
the in-editor tools (it's reviewed in a PR, not blocking a keystroke).

## Division reminder
CodeQL owns ONLY the residual flow Pylance misses. Do not re-implement generic None-deref
in CodeQL — Pylance already catches those in-editor, earlier. Avoid double-reporting.
