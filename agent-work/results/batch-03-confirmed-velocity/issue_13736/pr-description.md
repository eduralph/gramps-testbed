## Root cause
`AddonManager.install_addon` raises an `OkDialog` whose message says
only "The addon will be unavailable in your current configuration" —
it names neither the failing addon nor any of the common causes. The
canonical 13736 scenario (5.x `gramps.ini` carried into a 6.x install,
project URLs index catalogues whose `gramps_target_version` no longer
matches the running Gramps, `valid_plugin_version` rejects on
registration) leaves the user with no diagnosis path.

## Fix
Reword the failure dialog to name the addon, the running Gramps
`major_version`, and point the user at
`Edit → Preferences → Addon Manager → Projects` — where the project
URL is edited. Bring `major_version` into scope on the module via a
new import.

## Verified against
- `gramps/gui/plug/_windows.py:install_addon` — the path that raises
  the dialog when `self.__preg.get_plugin(addon_id)` returns `None`
  (i.e. `reg_plugins` rejected the addon, most often on the
  `valid_plugin_version` check).
- `gramps/version.py` — `major_version` is the existing, exported
  "MAJOR.MINOR" string compared by the registry against
  `gramps_target_version`.

## Test
`gramps/gui/plug/test/windows_test.py` — two cases under
`AddonManagerInstallAddonFailureDialogTest`:

* `test_failure_dialog_names_the_addon_and_points_at_projects` — drives
  `install_addon` with a forced `get_plugin → None`, captures the
  patched `OkDialog` call, asserts the message contains the addon id,
  the running `major_version`, and "Projects".
* `test_failure_dialog_not_shown_on_success` — sanity check that the
  dialog is **not** raised when `get_plugin` returns a non-`None` pdata,
  and that `load_plugin` + `plugins-reloaded` fire on the happy path.

Headless via `__new__`-bypass on `AddonManager` + `patch.object` on
`OkDialog` in the module, so the test does not require a live Gtk
display.

Fixes #13736
