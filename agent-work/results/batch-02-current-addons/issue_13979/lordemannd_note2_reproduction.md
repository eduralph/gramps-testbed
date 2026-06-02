# lordemannd's note 2 on Mantis 13979 — separate defect, reproduced

> Also notes a SECOND symptom: installing via the core Addon Manager
> reports success but doesn't actually install (retrace and you can
> "install" again).

## Outcome
**Reproduced.** Different defect from the IndexError fixed in
PR 916 — this one is in **gramps core**, not in the PluginManager
Enhanced addon. Per CLAUDE.md "one issue per ticket" + the
13979 verdict's explicit "do NOT bundle" instruction, **not addressed
in PR 916**. Eduard's call whether to file a fresh Mantis or note
it on 13979 with a request to split.

## Root cause
`EnhancedAddonStatus.__on_install_clicked` in
[`gramps/gui/plug/_windows.py:287-334`](../../../../gramps/gramps/gui/plug/_windows.py#L287)
calls `load_addon_file(path)` **without a callback** and **discards
the return value**:

```python
# Install addon
path = addon["_u"] + "/download/" + addon["z"]
load_addon_file(path)                     # ← return value ignored
self.manager.install_addon(addon["i"])    # ← marks installed regardless

# Refresh this row
pmgr = GuiPluginManager.get_instance()
plugin = pmgr.get_plugin(addon["i"])
if plugin:
    self.addon["_v"] = plugin.version
self.__build_gui(self.vbox, self.addon, self.req)
```

`load_addon_file` returns `False` on every failure mode (network
error, version mismatch, extract OSError, no matching gpr.py),
emitting error text only through the `callback` parameter — which is
not passed here. The chain is therefore:

1. `load_addon_file` fails silently (returns `False`, error message
   suppressed).
2. `self.manager.install_addon(addon["i"])` runs anyway — the
   manager's state is updated even though the plugin was never
   actually loaded.
3. `pmgr.get_plugin(addon["i"])` returns `None` because the .gpr.py
   was never extracted / registered.
4. `self.addon["_v"]` therefore never gets set.
5. `__build_gui` rebuilds the row. Since `"_v" not in addon`, the
   `Install` button re-appears
   ([`_windows.py:263`](../../../../gramps/gramps/gui/plug/_windows.py#L263)).
6. User sees "no error dialog" (interprets as success) but the
   `Install` button is still active. Clicks again → same silent
   failure. Matches lordemannd's exact description.

The 4 OTHER call sites for `load_addon_file` in the same file *do*
pass a callback (`_windows.py:1387`, `1413`, `2237`); 326 and 356
(install + update) are the inconsistent pair.

## Reproduction (run inside the testbed docker image)

```python
from gramps.gen.plug.utils import load_addon_file

# Scenario A — bad URL (the failure lordemannd most likely hit)
result = load_addon_file("https://example.invalid/nope.addon.tgz")
# -> False; no message anywhere

# Scenario B — version mismatch (testbed is 6.1; tgz declares 6.0)
result = load_addon_file(
    "file:///workspace/addons/gramps60/download/PostgreSQLEnhanced.addon.tgz"
)
# -> False; no message anywhere

# Scenario B with a callback to see what __on_install_clicked is
# throwing away:
messages = []
load_addon_file(
    "file:///workspace/addons/gramps60/download/PostgreSQLEnhanced.addon.tgz",
    callback=lambda m: messages.append(m),
)
# messages contains:
#   "Examining 'PostgreSQLEnhanced/postgresqlenhanced.gpr.py'...\n"
#   "   '<built-in function id>' is NOT for this version of Gramps.\n"
#   '   It is for version 6.0\n'
```

The callback-equipped run proves the underlying machinery already
*produces* a clear diagnostic — `__on_install_clicked` is simply
throwing it away.

## Likely fix shape (NOT in PR 916)
At the install + update call sites in `_windows.py:326` and `:356`,
either:
1. Capture the return value and surface a failure dialog if False:
   ```python
   messages = []
   if not load_addon_file(path, callback=lambda m: messages.append(m)):
       ErrorDialog(
           _("Addon installation failed"),
           "".join(messages) or _("Unknown error"),
           parent=self.window,
       )
       return
   self.manager.install_addon(addon["i"])
   ...
   ```
2. Or — minimally — emit the diagnostic *somewhere* the user sees
   it. Even logging at WARNING via the existing LOG would be better
   than the current "silently advance the UI".

A regression test could mock `load_addon_file` to return False and
assert that (a) an error is surfaced and (b) `install_addon` is NOT
called.

## Why this is a separate Mantis ticket
- Different code path: gramps core (`gramps/gui/plug/_windows.py`),
  not the Plugin Manager Enhanced addon's `__info`.
- Different defect class: silent-failure UX, not a crash.
- Different reporter intent in the original ticket: lordemannd
  filed 13979 for the IndexError; the install symptom is mentioned
  as an aside in note 2.
- The 13979 verdict explicitly says **do not bundle**.

Suggested next move: file a Mantis ticket against gramps core titled
"Addon Manager: Install reports success even when load_addon_file
fails silently". Reference 13979 note 2 + this reproduction.

## Repo and branch
No code change, no PR — finding only. The eventual fix would target
**gramps core**, branch `maintenance/gramps61`.
