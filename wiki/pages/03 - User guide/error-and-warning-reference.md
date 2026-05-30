---
title: Gramps 6.0 Wiki Manual - Error and Warning Reference
categories:
- Documentation
- Pages with broken file links
- Stub
- Troubleshooting
managed: false
source: wiki-scrape
wiki_revid: 127929
wiki_fetched_at: '2026-05-30T11:13:49Z'
---

{{#vardefine:chapter\|E}} {{#vardefine:figure\|0}} This section explains what to do when something unexpected happens.

## When something goes wrong

Sometimes something goes wrong, either because you have asked to do something that Gramps doesn't know how to do, or because something has happened that the developers of Gramps did not anticipate, or because there is a mistake in the coding of Gramps.

## Alerts

An alert is a dialog that appears when Gramps needs to give you an important message about an error condition or warn you about potentially hazardous situations or consequences.

Most alerts are self explanatory, and the same type of alerts that you might get with any application. These are not discussed further here.

However, some alerts require more complicated actions, so they are described below. {{-}}

### Abort changes?

![[_media/Abort-changes-dialog-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Abort changes?" dialog]]

The dialog is shown when you select menu you can use the button to continue your editing session or button to return the family tree to the state it was before you started the editing session.

{{-}}

### Are you sure you want to upgrade this Family Tree?

![[_media/AreYouSureYouWantToUpgradeThisFamilyTree-dialog-DbUpgradeRequiredError-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Are you sure you want to upgrade this Family Tree?" dialog - Db Upgrade Required - example]]

![[_media/AreYouSureYouWantToUpgradeThisFamilyTree-dialog-BsddbUnsupported-example-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Are you sure you want to upgrade this Family Tree?" dialog - BSDDB conversion - example]]

![[_media/AreYouSureYouWantToUpgradeThisFamilyTree-dialog-BsddbUpgradeRequiredError-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Are you sure you want to upgrade this Family Tree?" dialog - BSDDB Upgrade Required Error - example]]

![[_media/AreYouSureYouWantToDowngradeThisFamilyTree-dialog-BsddbDowngradeRequiredError-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Are you sure you want to downgrade this Family Tree?" dialog - BSDDB Downgrade Required Error - example]]

![[_media/AreYouSureYouWantToUpgradeThisFamilyTree-dialog-PythonUpgradeRequiredError-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Are you sure you want to upgrade this Family Tree?" dialog - Python Upgrade Required Error - example]]

These dialogs appear for the listed reasons:

- "Db Upgrade Required" - If you try to open a Db(Sqlite3) Family Tree created with a previous older version of Gramps with a newer version of Gramps.
- "BSDDB Upgrade Required Error" - superseded [BSDDB](wiki:Gramps_Glossary#bsddb) database Family must be converted to a current Database engine (typically SQLite) for Gramps.
- "BSDDB Upgrade Required Error" - If you try to open a BSDDB Family Tree created with a previous older version of Gramps with a newer version of Gramps.
- "BSDDB Downgrade Required Error" - If you try to open a BSDDB Family Tree created with a previous older version of BSDDB with a newer version of BSDDB.
- "Python Upgrade Required Error" - If you try to open a BSDDB Family Tree created with a previous older version of Gramps using Python 2 with a newer version of Gramps that uses Python 3.

For each of these reasons you may follow the same general advice; if you still have the older version of Gramps available, then you should:

- this dialog, and exit Gramps

- Open the Family Tree with the previous version of Gramps (Reinstall the old version of Gramps),

- Export your family tree in [Gramps XML (family tree) export](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees#Gramps_XML_.28family_tree.29_export) format or [Gramps XML Package (family tree and media)](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees#Gramps_XML_Package_.28family_tree_and_media.29_export) format,

- Exit the old version of Gramps and Start the new version of Gramps,

- Open the Family Tree in the new version of Gramps and click the  
  button in this dialog

{{-}}

### Error parsing arguments

![[_media/ErrorParsingArguments-dialog-DatabaseIsLocked-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}}Error parsing arguments - dialog - Database is locked example]] The Family Tree database is locked while in use by another user or because Gramps exited abnormally during previous use.

See [Unlocking a Family Tree](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees#Unlocking_a_Family_Tree) {{-}}

### Database is locked. cannot open it!

The Family Tree database is locked while in use by another user or because Gramps exited abnormally during previous use.

See [Unlocking a Family Tree](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees#Unlocking_a_Family_Tree) {{-}}

### Cannot open database

![[_media/Cannot_open_database-40.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Dialogue showing DB Environment Error]]

![[_media/DbVersionError-40.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Dialogue showing DB Version Error]]

As explained in the dialogue, the Family Tree was probably created with an old version of the Berkeley database program. This is not quite the same thing as an old version of the Gramps program, because the version of the Gramps program and the version of the Berkeley database are independent. However, the effect is somewhat the same. As suggested in the dialogue, if you have the old version of Gramps and its support software, then you should:

- cancel this dialogue,
- open the Family Tree with the previous version of Gramps,
- export your family tree in Gramps XML database export format or Gramps package export format (see [Export into Gramps formats](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees#Export_into_Gramps_formats)),
- start the new version of Gramps,
- open the 'Manage Family Tree' dialogue,
- click on and create a new Family Tree,
- load the new Family Tree
- Import the Gramps XML or Gramps package.

Alternatively, it may be possible to use the recovery tools. See 'obtain the bsddb recovery tools' under [Recover corrupted family tree](wiki:Recover_corrupted_family_tree) {{-}}

## Low level database corruption detected

![[_media/LowLevelDatabaseCorruptionDetected-dialog-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Low level database corruption detected" dialog - example]]

This dialogue appears when a problem is detected with the underlying database that supports Family Trees.

- close the dialogue,
- click on the Family Tree Manager,
- select the Family Tree you were trying to open,
- the button should be available; click on it,
- once the Family Tree has been repaired it should be possible to open it in the normal way.

If this does not work, try 'obtain the bsddb recovery tools' under [Recover corrupted family tree](wiki:Recover_corrupted_family_tree) {{-}}

### Error detected in database

![[_media/RunDatabaseRepair-40.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Dialogue showing Run Database Repair]]

Carry out suggested action. {{-}}

## Warnings

If Gramps detects a minor error, or wishes to notify you about an occurrence within the program, then Gramps may display a button on the status bar, as shown below. This button is only displayed for 180 seconds, so if you see it you should immediately click on it if you want to see the messages.

### Warning button

![[_media/Status-bar-warning-button-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Gramps Main Window showing Warning button on the Status bar]] The button (light bulb icon) {{-}}

### Gramps Warnings dialog

![[_media/Gramps-warnings-dialog-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Gramps Main Window showing Warning message and context menu]]

If you click the button, then a dialog box appears showing the last 20 messages received.

You may use the context menu to copy the details to a text file.

See [More details about the Logging system](wiki:Logging_system) {{-}}

Some of the warnings that may appear are described below:

### Locale warnings

Sometimes there is a problem with the language you have chosen.

If you have installed Gramps using your platform's standard installation method (Package manager/AIO installer/Application package) and are using your platform's built-in mechanism (System Setting/Control Panel/System Preferences) to choose the language/sort order/formats you are running in, then these errors should not occur, and may mean there is a problem in Gramps.

However, if you have set the language/sort order/formats manually by setting the 'environment' see [languages](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Language), particularly if you are running Gramps from the command line, then there may be a problem with what you have typed in. The message (only part of which is shown below) should help you to understand where the error is.

- "Date parser for '%s' not available, using default"
- "Date displayer for '%s' not available, using default"
- "Family relationship translator not available for language '%s'. Using 'english' instead."
- 'Unable to determine your Locale, using English'
- "Localization library libintl not on %PATH%, localization will be incomplete"
- "No translations for %s were found, setting localization to U.S. English"
- "Unable to create collator: %s"
- "No language provided, using US English"
- "No usable languages found in list, using US English"
- "None of the requested languages (%s) were available, using %s instead"

### Module not loaded warnings

The Gramps application contains many different 'modules'. Some of these modules are required for Gramps to run at all; some are 'strongly recommend', and some are optional.

If you have installed Gramps using your platform's standard installation method (Package manager/AIO installer/Application package) then the builder of that package will have decided which modules are present. He must include all the required modules, because otherwise Gramps will not run, but he can choose which of the recommended and optional packages he includes. Consult the documentation for your package to determine which modules are included.

If you try to do something that needs a module that is not included, then you will get a warning like the ones below (only the first part of the message is included). What you can do about it depends on your platform:

**Linux** You should be able to install the package using your distribution's standard Package Manager or the GUI interface to the Package Manager. However, in some cases you will need to build the module from source.

**MS Windows and macOS** The MS Windows AIO installer and the macOS Application bundle come with certain modules built in. It is not possible for the normal user to add further modules. Therefore, if you find a module that you particularly feel should be included you should post on the Gramps [Forum](wiki:Contact#Official) (probably the Development section) explaining why you feel its omission is a mistake.

- "WARNING: PIL module not loaded. "
- "ICU not loaded because %s. Localization will be impaired. "
- "OsmGpsMap module not loaded. "
- "GExiv2 module not loaded. "
- "Webkit module not loaded. "
- "PIL (Python Imaging Library) not loaded. "
- "GtkSpell not loaded. "

#### Show plugin status dialog on plugin load error

Allows showing dialog following the [Plugin](wiki:Gramps_Glossary#plugin) Registration process as Gramps starts. The dialog reports plugins that cause an error during registration. This allows users to find and resolve plugin problems.

The dialog can be suppressed from option in the tab of the dialog.

The error conditions that would trigger the plugin error status dialog are primarily handled in the \`load_plugin\` function of the \`PluginManager\` class. Here are the main error conditions:

1\. Plugin Registration File Errors:

- Missing or invalid gramps_target_version ([gen/plug/\_manager](https://github.com/gramps-project/gramps/blob/maintenance/gramps52/gramps/gen/plug/_manager.py#L1050-L1056))
- Incorrect plugin version format ([gen/plug/\_manager](https://github.com/gramps-project/gramps/blob/maintenance/gramps52/gramps/gen/plug/_manager.py#L1058-L1062))
- Missing required attributes for the specific plugin type ([gen/plug/\_manager](https://github.com/gramps-project/gramps/blob/maintenance/gramps52/gramps/gen/plug/_manager.py#L1064-L1068))

2\. Module Import Errors:

- The plugin's main Python file cannot be imported ([gen/plug/\_manager](https://github.com/gramps-project/gramps/blob/maintenance/gramps52/gramps/gen/plug/_manager.py#L1070-L1074))

3\. Plugin Initialization Errors:

- Exceptions raised during the plugin's initialization process ([gen/plug/\_manager.py](https://github.com/gramps-project/gramps/blob/maintenance/gramps52/gramps/gen/plug/_manager.py#L1076-L1080))

4\. Version Incompatibility:

- The plugin's gramps_target_version does not match the running Gramps version ([gen/plug/\_manager](https://github.com/gramps-project/gramps/blob/maintenance/gramps52/gramps/gen/plug/_manager.py#L1082-L1086))

5\. Duplicate Plugin IDs:

- Multiple plugins with the same ID are detected ([gen/plug/\_manager](https://github.com/gramps-project/gramps/blob/maintenance/gramps52/gramps/gen/plug/_manager.py#L1088-L1092))

6\. Invalid Plugin Type:

- [PTYPE](wiki:Addons_development#Create_a_Gramps_Plugin_Registration_file) specified is not recognized ([gen/plug/\_manager](https://github.com/gramps-project/gramps/blob/maintenance/gramps52/gramps/gen/plug/_manager.py#L1094-L1098) and [gui/viewmanager](https://github.com/gramps-project/gramps/blob/maintenance/gramps52/gramps/gui/viewmanager.py#L615-L618))

### Configuration warnings

Sometimes it is worth just deleting the old configuration files.

- "Importing old key file 'keys.ini'..." (The `.gramps/keys.ini` file was deprecated in Gramps 3.2, now `.gramps/gramps``/gramps.ini` )
- "Done importing old key file 'keys.ini'"
- "Can't find filter %s in the defined custom filters"
- "Number of arguments does not match number of " +
- "Value '%(val)s' not found for option '%(opt)s'"
- "Unable to open recent file %s because %s",
- "WARNING: ignoring old key '%s'"
- "WARNING: ignoring key with wrong type "
- "Failed to parse doc options"
- "Skipped a line in the addon listing: "
- "Failed to load gramplets from %s because %s"

### Other warnings

{{-}}

#### Place cycle detected dialog

![[_media/PlaceCycleDetected-warning-dialog-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Place cycle detected" warning dialog]]

"Place cycle detected" warning dialog indicated that "The place you are adding is already enclosed by " "this place"

See also:

- [Enclosed By](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_2#Enclosed_By)

{{-}}

#### Missing Media dialog

If a media file is not found during export, you will see the same Missing Media dialog.

#### Could not open file: <file path and file name>

![[_media/Could-not-open-file-file-path-and-file-name-warning-dialog-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Could not open file: <file path and file name>" - (Warning window)]]

In the [Import_Family_Tree_dialog](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees#Import_Family_Tree_dialog) if you select the **All files** option and then select an unsupported file import type you will be shown the **Could not open file: <file path and file name>** warning dialog.

The message show mentions:

<hr>

File type "xxx" is unknown by Gramps.

Valid types are: Gramps database, Gramps XML, Gramps package, GEDCOM, and others.

{{-}}

#### Cannot save person

![[_media/CannotSavePerson-dialog-51.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Cannot save person (Warning window)]] Attempting to save a person without any data from the Person editor displays this warning popup. You need at least one letter for the first name.

**Cannot save person**  
No data exist for this person. Please enter data or cancel the edit.  
Close {{-}}

#### Cannot merge <object>

![[_media/CannotMerge-object-warning-dialog-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Cannot merge person (Warning dialog) - example]] Attempting to merge anything other than two(2) of one type of record displays this warning popup dialog.

For example:

**Cannot merge people**  
Exactly two people must be selected to perform a merge. A second person can be selected by holding down the control key while clicking on the desired person.

Close

{{-}}

See:

- [Merging records](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_3#Merging_records)

#### Duplicate Family warning dialog

![[_media/DuplicateFamily-warning-dialog-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Duplicate Family - warning dialog]]

{{-}}

#### Suppress warning when adding parents to a child

Can be enabled from option in the [Preferences &gt; Warnings](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Warnings) dialog.

{{-}}

##### Adding parents to a person dialog

![[_media/AddingParetsToA-Person-warning-dialog-51.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Adding parents to a person" warning dialog]]

{{-}}

#### Suppress warning when cancelling with changed data

Can be disabled from option in the dialog.

Used by the dialog.

#### Save Changes? dialog

![[_media/SaveChanges-alert-dialog-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Save Changes?" - alert dialog]]

If any data in any tabs in the Edit Person dialog were modified, an alert window will appear, prompting you to choose from the following options:

- \- changes.

- (default) - the initial cancel request.

- \- the changes.

as well as a checkbox to indicate that can be disabled from the option in the dialog.

{{-}}

#### Suppress warning about missing researcher when exporting to GEDCOM

![[_media/xxx.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} xxx]]

Can be disabled from option in the [Preferences &gt; Warnings](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Warnings) dialog.

{{-}}

#### Delete confirmation dialog

![[_media/Delete-confirmation-dialog-Undo-History-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Delete confirmation dialog for the &quot;Undo History&quot; dialog]] Are you sure you want to clear the [Undo history](wiki:Gramps_6.0_Wiki_Manual_-_Navigation#Undo_History_dialog)? Select to confirm or to exit. {{-}}

#### Undo history warning

![[_media/UndoHistoryWarning-Tool-dialog-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Tool "Undo history warning" dialog - default]]

The dialog will be shown and you can either or . It is recommended that you stop and backup your database; so that you can revert the process of running the tool (or import) if required. {{-}} ![[_media/UndoHistoryWarning-Import-dialog-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Import &quot;Undo history warning&quot; dialog - default]] {{-}}

#### No selected book item

![[_media/No-selected-book-item-warning-52.png|<em>No selected book item</em> - warning]]

You will see warning dialog when the [Books](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_3#Books) Report when you have not selected the item first in the **Current book** section of the **Manage Books** dialog. {{-}}

#### Person \<\_\_\_\_\> is not in the Database

![[_media/xxx-52.png|Person &lt;____&gt; is not in the Database}} warning dialog]]

warning dialog will be shown if the Center Person is Private or Living when the filtering options on the Report Options (2) tab settings for do not allow Private or Living Persons are used.

{{-}}

#### Autobackup...

![[_media/Autobackup.notification.on.exit-52.png|&quot;Autobackup...&quot; notification on exit warning dialog]] The **Please wait for backup to complete.** notification on exit dialog is shown when exiting Gramps to indicate an Automatic Backup is in progress.

See also:

-  tab's [Backup Management](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Backup_Management) section for the and options.

<!-- -->

- [Backup: Add a popup to show the gramps state \#1416](https://github.com/gramps-project/gramps/pull/1416)

{{-}}

#### Could Not Set a Bookmark

![[_media/Could-Not-Set-a-Bookmark-warning-60.png|&quot;Could Not Set a Bookmark&quot; warning dialog]] A [bookmark](wiki:Gramps_6.0_Wiki_Manual_-_Navigation#Bookmark_Navigation) could not be set because nothing was selected. {{-}}

#### Opening the '<xxxxxxx>' database

![[_media/Opening-the-xxxxxxx-database-warning-60.png|&quot;Opening the &#39;&#39; database&quot; warning dialog]] You may see the "Opening the '<xxxxxxx>' database" warning dialog when attempting to [convert](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees#Family_Trees_.28manager.29_window) the *Database Type* from BSDDB to SQLite .

An attempt to convert the database failed. Perhaps it needs updating. {{-}}

## Errors

More serious problems cause an dialog to be shown which will describe the actions you should take.

{{-}}

### Error Report

![[_media/ErrorReport-dialog-collapsed-ErrorDetail-default-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Error Report Assistant - dialog - collapsed "Error Detail" - default]]

The dialog appears whenever something has happened in the Gramps application that the programmers did not expect.

Have a read of the [How to create a good bug report](wiki:How_to_create_a_good_bug_report) article. If you believe you know how the Gramps developers might reproduce the bug or not, then select the button to start the dialog, and you can then follow the instructions. {{-}} ![[_media/ErrorReport-dialog-expanded-ErrorDetail-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Error Report Assistant - dialog - expanded &quot;Error Detail&quot; - default]] {{-}}

### Error Reporting Assistant dialog

Allows you an opportunity to compile a report about an error and then submit it manually to the Gramps bug reporting system (This requires you to have a registered account on the Gramps bug reporting system and then login into your bug tracker account.)

- [Using the bug tracker](wiki:Using_the_bug_tracker)

The Error Reporting Assistant is also known as the Bug Reporting Assistant. {{-}}

#### Report a bug page

![[_media/ErrorReportingAssistant-ReportABug-page-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Report a bug (page) - Error Reporting Assistant]]

This is the Bug Reporting Assistant. It helps to make a bug report to the Gramps developers that will be as detailed as possible.

The assistant asks a few questions and gathers some information about the error that just occurred and the operating environment.

At the end of the assistant process, you will be asked to file a bug report through the [Gramps bug tracking](https://gramps-project.org/bugs/my_view_page.php) system.

The assistant will copy the bug report to the Operating System clipboard. This allows you to paste it into the form on the [Gramps bug tracking](https://gramps-project.org/bugs/my_view_page.php) and review exactly what information you want to include. {{-}}

#### Error Details page

![[_media/ErrorReportingAssistant-ErrorDetails-page-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Error Details (page) - Error Reporting Assistant (Showing example error)]]

If you can see that there is any personal information included in the error please remove it.

This is the detailed Gramps error information, don't worry if you do not understand it. You will have the opportunity to add further detail about the error in the following pages of the assistant. {{-}}

#### System Information page

![[_media/ErrorReportingAssistant-SystemInformation-page-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} System Information (page) - Error Report Assistant]]

This is the information about your system that will help the developers to fix the bug. {{-}}

#### Further Information page

![[_media/ErrorReportingAssistant-FurtherInformation-page-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Further Information (page) - Error Reporting Assistant]]

Please provide as much information as you can about what you were doing when the error occurred.

This is your opportunity to describe what you were doing when the error occurred. {{-}}

#### Bug Report Summary page

![[_media/ErrorReportingAssistant-BugReportSummary-page-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Bug Report Summary (page) - Error Reporting Assistant]]

This is the completed bug report. The next page of the assistant will help you to file a bug on the Gramps bug tracking system website. {{-}}

#### Send Bug Report page

![[_media/ErrorReportingAssistant-SendBugReport-page-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Send Bug Report (page) - Error Reporting Assistant]]

Use the two buttons below to first copy the bug report to the clipboard and then open a webbrowser to file a bug report at <https://gramps-project.org/bugs/login_select_proj_page.php?ref=bug_report_page.php>

- \- This is the final step. Use the buttons on this page to start a web browser and file a bug report on the Gramps bug tracking system (This assumes you already have an user account on the bug tracker, if not signup for one first and then login into your bug tracker account.)

  - \- Use this button to start a web browser and file a bug report on the Gramps bug tracking system.

  - \- Use this button to copy the bug report onto the clipboard. Then go to the bug tracking website by using the button below, paste the report and click submit report

{{-}}

#### Complete page

![[_media/ErrorReportingAssistant-Complete-page-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Complete (page) - Error Reporting Assistant]]

Gramps is an Open Source project. Its success depends on its users. User feedback is important. Thank you for taking the time to submit a bug report. {{-}}

### Other Errors

#### Report could not be created

![[_media/xxxx.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Report could not be created dialog]]

The dialog can occur for various reasons, eg: one reason is that the custom paper size you have chosen for the report is too large for PDF format that is being used.

## Seeing all the error messages

Sometimes, not all the information needed to understand what has gone wrong will appear on the screen. For example, if you start Gramps with an invalid language setting (and some missing components) then the message that appears in the dialog is:

![[_media/Warning_message_GExiv2-40.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Dialogue showing limited warnings]] {{-}} However, the full set of warning messages is:

`(process:10929): Gtk-WARNING **: Locale not supported by C library.`  
`   Using the fallback 'C' locale.`  
`2013-03-13 18:49:04.376: WARNING: __init__.py: line 69: Date parser for 'xx_XX.UTF-8' not available, using default`  
`2013-03-13 18:49:04.547: WARNING: __init__.py: line 85: Date displayer for 'xx_XX.UTF-8' not available, using default`  
`2013-03-13 18:49:05.949: WARNING: spell.py: line 74: Spelling checker is not installed`  
`2013-03-13 18:49:16.023: WARNING: gramplet.gpr.py: line 400: WARNING: GExiv2 module not loaded.  Image metadata functionality will not be available.`

Sometimes Gramps just doesn't start and nothing appears on the screen, or Gramps suddenly quits so you don't see anything on the screen. In all these cases you may need to do something special to see all the errors.

### Linux

You can start Gramps from the Command Line, as described in the note [here](wiki:Gramps_6.0_Wiki_Manual_-_Getting_started#Linux). You will then see all the diagnostic information on the terminal.

### MS Windows

You can start Gramps from the Command Line, as described in the note [here](wiki:Gramps_6.0_Wiki_Manual_-_Getting_started#MS_Windows). You will then see all the diagnostic information on the terminal.

### macOS

Starting Gramps through the CLI on macOS is covered [here](wiki:Gramps_6.0_Wiki_Manual_-_Command_Line#macOS).

#### Console application

You can also look at log messages from Gramps using Apples . The Console application is located in your Mac's Utilities folder, which is found in the Applications folder. (A shortcut on recent versions of macOS is to press Command and the space bar to start a Spotlight search. In the resulting pop up window, enter the first few characters of the word "Console" and then select the Console application.)

For example, one of the early alpha releases of Gramps just would not start and displayed nothing on the screen. However by opening the Console application, and typing Gramps in the filter at the top right hand corner some diagnostic information appeared. (Actually we typed "gramps\[" because there were some other messages that were not relevant, but it wouldn't matter if they were included as well). ![[_media/Console_output-40.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Console output]] {{-}} By shift clicking to select all the relevant messages and copying them we get:

`01/03/2013 00:08:02 [0x0-0x88088].org.gramps-project.gramps[1867] 2939: ERROR: importer.py: line 51: Could not find any typelib for Gtk `  
`01/03/2013 00:08:05 [0x0-0x88088].org.gramps-project.gramps[1867] Gtk typelib not installed. Install Gnome  Introspection, and pygobject version 3.3.2 or later. `  
`01/03/2013 00:08:05 [0x0-0x88088].org.gramps-project.gramps[1867] Gramps will terminate now. `

In this particular case, this was enough to help the developer discover the problem.

{{-}}

[Category:Documentation](wiki:Category:Documentation) [Category:Troubleshooting](wiki:Category:Troubleshooting)
