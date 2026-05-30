---
title: Gramps 6.0 Wiki Manual - Error and Warning Reference/he
categories:
- He:מסננים
- He:מתקעים
- He:תגים
- He:תיעוד
- Pages with broken file links
- Stub
managed: false
source: wiki-scrape
wiki_revid: 126037
wiki_fetched_at: '2026-05-30T19:16:11Z'
lang: he
---

{{#vardefine:chapter\|E}} {{#vardefine:figure\|0}} עמוד זה מסביר מה ניתן לעשות כשמשהו לא צפוי קורה.

## כשמשהו משתבש

לפעמים דברים משתבשים, בגלל שגרמפס נתבקש לבצע דבר שהוא לא בנוי לעשות, בגלל שקרה משהו בקוד התוכנה שמפתחי גרמפס לא צפו, או בגלל טעות בקידוד גרמפס שלא צפה במהך הבדיקות.

## התראות

התראה היא דו־שיח שמופיע כאשר גרמפס צריך לתקשר הודעה חשובה לגבי מצב שגיאה או להזהיר לגבי מצבים או השלכות שעלולים לסכן את שלמות מסד־הנתונים.

רוב ההתראות הן מובנות מאליהן, מסוג ההתראות שעשויות להתקבל מיישומים שונים. התראות אלו לא יידונו כאן.

אך התראות מסוימות דורשות פעולות מורכבות יותר, לכן הן מתוארות להלן. {{-}}

### האם לשדרג אילן־יוחסין זה??

![[_media/AreYouSureYouWantToUpgradeThisFamilyTree-dialog-DbUpgradeRequiredError-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Are you sure you want to upgrade this Family Tree?" dialog - Db Upgrade Required - example]]

![[_media/AreYouSureYouWantToUpgradeThisFamilyTree-dialog-BsddbUpgradeRequiredError-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Are you sure you want to upgrade this Family Tree?" dialog - Bsddb Upgrade Required Error - example]]

![[_media/AreYouSureYouWantToDowngradeThisFamilyTree-dialog-BsddbDowngradeRequiredError-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Are you sure you want to downgrade this Family Tree?" dialog - Bsddb Downgrade Required Error - example]]

![[_media/AreYouSureYouWantToUpgradeThisFamilyTree-dialog-PythonUpgradeRequiredError-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Are you sure you want to upgrade this Family Tree?" dialog - Python Upgrade Required Error - example]]

These dialogs appear for the listed reasons:

- "Db Upgrade Required" - If you try to open a Db(Sqlite3) Family Tree created with a previous older version of Gramps with a newer version of Gramps.
- "Bsddb Upgrade Required Error" - If you try to open a Bsddb Family Tree created with a previous older version of Gramps with a newer version of Gramps.
- "Bsddb Downgrade Required Error" - If you try to open a Bsddb Family Tree created with a previous older version of Bsddb with a newer version of Bsddb.
- "Python Upgrade Required Error" - If you try to open a Bsddb Family Tree created with a previous older version of Gramps using Python 2 with a newer version of Gramps that uses Python 3.

For each of these reasons you may follow the same general advice; if you still have the older version of Gramps available, then you should:

- Cancel this dialogue, and exit Gramps
- Open the Family Tree with the previous version of Gramps (Reinstall the old version of Gramps),
- Export your family tree in [Gramps XML (family tree) export](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees#Gramps_XML_.28family_tree.29_export) format or [Gramps XML Package (family tree and media)](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees#Gramps_XML_Package_.28family_tree_and_media.29_export) format,
- Exit the old version of Gramps and Start the new version of Gramps,
- Open the Family Tree in the new version of Gramps and click in this dialogue

{{-}}

### Error parsing arguments

![[_media/ErrorParsingArguments-dialog-DatabaseIsLocked-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}}Error parsing arguments - dialog - Database is locked example]] The Family Tree database is locked while in use by another user or because Gramps exited abnormally during previous use.

See [Unlocking a Family Tree](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees#Unlocking_a_Family_Tree)

### מסד נתונים נעול. לא ניתן לטעון אותו!

The Family Tree database is locked while in use by another user or because Gramps exited abnormally during previous use.

See [Unlocking a Family Tree](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees#Unlocking_a_Family_Tree) {{-}}

### לא ניתן לפתוח מסד נתונים

![[_media/Cannot_open_database.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Dialogue showing DB Environment Error]]

![[_media/DbVersionError.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Dialogue showing DB Version Error]]

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

### שגיאות שנתגלו במסד הנתונים

![[_media/RunDatabaseRepair.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Dialogue showing Run Database Repair]]

Carry out suggested action. {{-}}

## אזהרות

If Gramps detects a minor error, or wishes to notify you about an occurrence within the program, then Gramps may display a button on the status bar, as shown below. This button is only displayed for 180 seconds, so if you see it you should immediately click on it if you want to see the messages.

![[_media/Status-bar-warning-button-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Gramps Main Window showing Warning button on the Status bar]]

{{-}}

### דו־שיח אזהרות גרמפס

If you click the button, then a dialog box appears showing the last 20 messages received. [More details](wiki:Logging_system) ![[_media/Gramps-warnings-dialog-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Gramps Main Window showing Warning messages]] {{-}}

Some of the warnings that may appear are described below:

### מזהרוצ מקם

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

#### Show plugin status dialog on plugin load error.

Can be disabled from option in the [Preferences &gt; Warnings](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Warnings) dialog.

### אזהרות תצור

Sometimes it is worth just deleting the old configuration files.

- "Importing old key file 'keys.ini'..."
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

### אזהרות אחרות

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

Close {{-}}

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

Can be disabled from option in the [Preferences &gt; Warnings](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Warnings) dialog.

Used by the [Edit Person dialog](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1#Edit_Person_dialog).

#### דו־שיח "שמירת שינויים?"

![[_media/SaveChanges-alert-dialog-60-he.png|איור {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "שמירת שינויים?" – חלונית דו־שיח התראת]]

אם בוצעו שינויים בנתונים בכל אחת מהלשוניות שבחלונית , תופיע חלונית דו־שיח התראה שתבקש לבחור אחת מהאפשרויות הבאות:

- – ביטול השינויים.

- (ברירת מחדל) – ביטול הבקשה הראשונית.

- – שמירת השינויים.

בנוסף מופיעה תיבת סימון שניתן לבטל את הסתרתה דרך האפשרות **דיכוי אזהרה בעת ביטול עם נתונים ששונו** שבחלונית .

{{-}}

#### Suppress warning about missing researcher when exporting to GEDCOM

![[_media/xxx.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} xxx]]

Can be disabled from option in the [Preferences &gt; Warnings](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Warnings) dialog.

{{-}}

#### אזהרת היסטוריית הסגה

![[_media/UndoHistoryWarning-Tool-dialog-60_he.png|איור {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} — תיבת דו־שיח "אזהרת הסגת היסטוריה" לפעולות כלים — ברירת מחדל]]

תוצג תיבת הדו־שיח , ובה ניתן לבחור את אחת משתי האפשרויות או .

עם קבלת התראה מסוג זה, מומלץ לעצור [<strong>לגבות</strong>](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees/he#גיבוי_אילן־יוחסין) את אילן־היוחסין, כדי שיהיה ניתן לחזור אחורנית ככול יידרש.

{{-}}

![[_media/UndoHistoryWarning-Import-dialog-52.png|איור {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} — תיבת דו־שיח "אזהרת הסגת היסטוריה" לפעולות ייבוא — ברירת מחדל]]

{{-}}

## Errors

More serious problems cause an dialog to be shown which will describe the actions you should take.

{{-}}

### Error Report

![[_media/ErrorReport-dialog-collapsed-ErrorDetail-default-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Error Report Assistant - dialog - collapsed "Error Detail" - default]]

The dialogue appears whenever something has happened in the Gramps application that the programmers did not expect.

Have a read of the [How to create a good bug report](wiki:How_to_create_a_good_bug_report) article. If you believe you know how the Gramps developers might reproduce the bug or not, then select the button to start the dialog, and you can then follow the instructions. {{-}} ![[_media/ErrorReport-dialog-expanded-ErrorDetail-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Error Report Assistant - dialog - expanded &quot;Error Detail&quot; - default]] {{-}}

### Error Reporting Assistant dialog

Allows you an opportunity to compile a report about an error and then submit it manually to the Gramps bug reporting system (This requires you to have a registered account on the Gramps bug reporting system)

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

- \- This is the final step. Use the buttons on this page to start a web browser and file a bug report on the Gramps bug tracking system (This assumes you already have an user account on the bug tracker, if not signup for one first.)

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

## הצגת כל הודעות השגיאה

לפעמים, לא כל המידע הדרוש להבנת את מה שהשתבש יופיע על המסך. לדוגמה, אתחול גרמפס עם הגדרת שפה לא תקינות (או שכמה רכיבים בהגדרה חסרים), תופיע הודעת האזהרה הבאה בתיבת דו־השיח :

![[_media/Warning_message_GExiv2.png|איור {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} תיבת זו־שיח שמציגה הודעת אזהרה מוגבלת]] {{-}} עם זאת, ערכת הודעת האזהרה המלאה היא:

<div dir='ltr'>

`(process:10929): Gtk-WARNING **: Locale not supported by C library.`  
`   Using the fallback 'C' locale.`  
`2013-03-13 18:49:04.376: WARNING: __init__.py: line 69: Date parser for 'xx_XX.UTF-8' not available, using default`  
`2013-03-13 18:49:04.547: WARNING: __init__.py: line 85: Date displayer for 'xx_XX.UTF-8' not available, using default`  
`2013-03-13 18:49:05.949: WARNING: spell.py: line 74: Spelling checker is not installed`  
`2013-03-13 18:49:16.023: WARNING: gramplet.gpr.py: line 400: WARNING: GExiv2 module not loaded.  Image metadata functionality will not be available.`

</div>

במקרים מסויימים גרמפס פשוט מסרב לאתחל ושום דבר לא מופיע על המרקע, או שגרמפס עוצר ונעלפ מהמרקע כך שלא נתן לראות כלום על המרקע. בכל המקרים האלה ייתכן שיידרש לייזום פעולהו מיוחדת כדי להציג את כל הודעות השגיאה.

### לינוקס

You can start Gramps from the Command Line, as described in the note [here](wiki:Gramps_6.0_Wiki_Manual_-_Getting_started#Linux). You will then see all the diagnostic information on the terminal.

### MS Windows

You can start Gramps from the Command Line, as described in the note [here](wiki:Gramps_6.0_Wiki_Manual_-_Getting_started#MS_Windows). You will then see all the diagnostic information on the terminal.

### macOS

Starting Gramps through the CLI on macOS is covered [here](wiki:Gramps_6.0_Wiki_Manual_-_Command_Line#macOS).

#### Console application

You can also look at log messages from Gramps using Apples . The Console application is located in your Mac's Utilities folder, which is found in the Applications folder. (A shortcut on recent versions of macOS is to press Command and the space bar to start a Spotlight search. In the resulting pop up window, enter the first few characters of the word "Console" and then select the Console application.)

For example, one of the early alpha releases of Gramps just would not start and displayed nothing on the screen. However by opening the Console application, and typing Gramps in the filter at the top right hand corner some diagnostic information appeared. (Actually we typed "gramps\[" because there were some other messages that were not relevant, but it wouldn't matter if they were included as well). ![[_media/Console_output.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Console output]] {{-}} By shift clicking to select all the relevant messages and copying them we get:

`01/03/2013 00:08:02 [0x0-0x88088].org.gramps-project.gramps[1867] 2939: ERROR: importer.py: line 51: Could not find any typelib for Gtk `  
`01/03/2013 00:08:05 [0x0-0x88088].org.gramps-project.gramps[1867] Gtk typelib not installed. Install Gnome  Introspection, and pygobject version 3.3.2 or later. `  
`01/03/2013 00:08:05 [0x0-0x88088].org.gramps-project.gramps[1867] Gramps will terminate now. `

In this particular case, this was enough to help the developer discover the problem.

{{-}}

[Category:He:תיעוד](wiki:Category:He:תיעוד) [Category:He:מסננים](wiki:Category:He:מסננים) [Category:He:מתקעים](wiki:Category:He:מתקעים) [Category:He:תגים](wiki:Category:He:תגים)
