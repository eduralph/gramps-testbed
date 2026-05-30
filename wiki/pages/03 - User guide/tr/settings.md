---
title: Gramps 6.0 Wiki Manual - Settings/tr
categories:
- Stub
- Tr:Documentation
managed: false
source: wiki-scrape
wiki_revid: 125636
wiki_fetched_at: '2026-05-30T20:59:27Z'
lang: tr
---

{{#vardefine:chapter\|15}} {{#vardefine:figure\|0}} Bu bölüm, Gramps içinde yönetebileceğiniz çeşitli ayarlarla ilgilidir.

## Tercihler

![[_media/EditPreferencesTabsOnly-overview-51.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Overview of all Preferences tabs]]

Most of the settings in Gramps are configured in the dialog. To invoke it, select the menu .

The tabs on the top display the available option categories as follows:

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

Also *other* additional tabs maybe shown from any [addons](wiki:6.0_Addons#Addon_List) you may have installed. {{-}}

### General

![[_media/EditPreferences-General-tab-example-51.png|Right|thumb|450px|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} General Preferences (Linux)]]

This tab contains two sections containing preferences relevant to the general operation of the program. Sections and options are:

#### General Gramps settings

- \[ \]: This checkbox option affects the importing of [GEDCOM data](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees#GEDCOM_import). If this is set, each item that is imported will contain a [Source](wiki:Gramps_Glossary#source) reference to the imported file. **Note - Adding a default source can significantly slow down the importing of your GEDCOM data.**

- \[ \]: Checkbox (Default: `Imported %Y/%m/%d %H:%M:%S` ) **Note - Adding a [Tag](wiki:Gramps_Glossary#tag) on import can significantly slow down the importing of your data.**

- \[ \]: This checkbox option controls the enabling and disabling of the spelling checker for notes. The **gtkspell** package must be loaded for this to have an effect.

-   
  This checkbox option controls the enabling and disabling of the dialog at startup.

-   
  This checkbox option controls the enabling and disabling of the display of the last [View](wiki:Gramps_Glossary#view). Enabling will bring you to the view where you stopped the program the last time.

- You can enter the number of generations used to determine relationships. The default value is **`15`**.

- Here you can fill in a base path for the media objects. Selecting the button gives you a editor where you can fill in the required path.

#### Third party addons management

- Select the frequency that Gramps checks for updates to [Addons](wiki:6.0_Addons#Installing_Addons_in_Gramps). Default: *Never*

- Default: *New addons only*

- Default: [`https://raw.githubusercontent.com/gramps-project/addons/master/gramps51`](https://raw.githubusercontent.com/gramps-project/addons/master/gramps51)

-   
  Checkbox selected by default

-   
  Button to force a check for Addons, if Addons are available you will then be presented the window where you choose and install them from.

{{-}}

###### Available Gramps Updates for Addons

![[_media/AvailableGrampsUpdatesforAddons-example-listing-60.png|Right|thumb|550px|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Available Gramps Updates for Addons" window showing example listing output for Gramps 6.0]]

The window you will be shown a list broken down by **Type** that you can view by selecting the "Select" column expand out each "Type".

- You can then select the check box of those Addons you want to install.
- Then select the button to download those Addons from the *Internet*.
- Once downloaded from the dialog select the button
- From the dialog select button.
- To use the Addons you need to and restart Gramps.

{{-}}

#### Tip of the Day dialog

![[_media/TipOfTheDay-dialog--example-keeping-good-records-50.png|Right|thumb|400px|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Tip of the Day dialog]]

When enabled in tab the dialog shows helpful hints.

The following options are available:

-  (check box checked by default - once enabled) - uncheck to stop further tips appearing.

- \- Advance to the next tip.

- \- exit for this session until the Gramps program is restarted.

{{-}}

### Family Tree

![[_media/EditPreferences-FamilyTree-tab-example-51.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menu:  - "Family Tree" - tab - example - Ubuntu defaults]]

This tab contains preferences relevant to the **Family Tree Database settings and Backup management**.

- \-

  - *[BSDDB](wiki:Gramps_Glossary#bsddb)* - Legacy Database backend. Superseded in the Gramps 6.0 version.
  - **[SQLite](wiki:Gramps_Glossary#sqlite)** (*default*) - the [DB-API Database Backend](wiki:DB-API_Database_Backend)
  - ... If other database backends addons are installed, they will be added to the list <abbr title="exempli gratia - Latin phrase meaning 'for example'">e.g.</abbr>: [Addon:PostgreSQL}PostgreSQL](wiki:Addon:PostgreSQL}PostgreSQL) backend

- \- Server address or other computer IP address for the location of the database.

- \- Port number to access the Host database

- Unless you have a definite reason to change this, stay with the default path. This path will be within the [User Directory](wiki:Gramps_6.0_Wiki_Manual_-_User_Directory) of the local machine's Operating Systems.  
  The default path where the Databases are stored is:

  
  
`/home/`<small>***<username>***</small>`/.gramps/grampsdb`''' <small>(Linux and macOS)</small>

`C:\Users\`<small>***\<~username\>***</small>`\AppData\Roaming\gramps\grampsdb`''' <small>(Windows)</small>

-   
  Selecting this checkbox option causes the last used database to load upon start. It bypasses the **Manage Family Trees** dialog.

- \- Location in which to save your Gramps backup archive files.

- \- Selecting this option will Backup Your family tree upon choosing to exit Gramps. The file be saved to the Backup path specified above. The filename of the backup will match the Family Tree appended with a date and time.

- timer interval for triggering full backups during Gramps editing sessions.

  - **Never** (*default*)
  - Every 15 minutes
  - Every 30 minutes
  - Every hour

{{-}}

See also:

- [Backing up a family tree](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees#Backing_up_a_Family_Tree) - more information on backups
- [Backup omissions](wiki:Template:Backup_Omissions) - what is not included during a backup
- Addon [PostgreSQL](wiki:Addon:PostgreSQL) - this adds support for PostgreSQL databases.

### Görüntüle

![[_media/EditPreferences-Display-tab-default-51.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menu: "Edit&gt;Preferences..." - "Display" - tab - defaults]]

The tab contains preferences relevant to the display of data and names, **Appearance and format settings**. Options are:

- This option controls the display of names in the current database (the setting is saved in the database and is not system wide). In Gramps there are two type of name display formats: the predefined formats, and the user defined custom formats. Several different predefined name formats are available: Given - Prefix Patronymic, Suffix Given - Prefix Surname, Given Patronymic Suffix etc.

  - Clicking on the right hand side button will bring up a window where the available list of options is shown. The format is given as well as an example. When predefined formats are not suitable one can define one's own format. You can use the button to add a Name format to the list. Clicking once will give you a **SURNAME,Given Suffix(call)** format and as example : **SMITH, Edwin Jose Sr (Ed)**. If you added new name formats to the list the and buttons become available to change the name format list.
    -   
      Checkbox unselected by default. If selected enables Gramps to consider patronymic and matronymic names as surnames.

- This option controls the display of dates. It is a global setting, requiring a restart of Gramps to take effect, and applies to the display of dates in all databases loaded within Gramps until such time as the date display format is changed again. Several different formats are available, which may be dependent on your locale.

  - **YYYY-MM-DD (ISO)** (Default) - Example 2020-09-30 - Displays the date using the international standard [ISO 8601 Data elements and interchange formats – Information interchange](https://wikipedia.org/wiki/ISO_8601) particularly useful when sharing data between countries with different conventions for writing numeric dates and times.
  - Numerical
  - Month Day, Year
  - MON DAY, YEAR
  - Day Month Year
  - DAY MON YEAR

<!-- -->

- This option controls the display of places.

  - **Full** (Default)
    - Selecting the button will show the

<!-- -->

- - **Years**(default)
  - Years, Months
  - Years, Months, Days

- **Gregorian**(default). This option controls the display of calendar on reports, tools, gramplets, views. Several different calendars are available (see [Date Edition](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_Editing_Data:_Detailed_-_part_1#Editing_dates)). Two dates with two different calendars will not properly display timeline or period, (e.g. Using the Gregorian calendar as the default displayed calendar, users will have a better coherency for displaying dates on period).

<!-- -->

- <span id="surname guessing"><span> This option affects the initial family name of a child when he/she is added to the database. The default will use the family name of the father. Selecting means that no surname guessing will be attempted. Selecting will use the father's name followed by the mother's name. Finally, will use the father's given name followed by the "sson" suffix (e.g. the son of Edwin will be guessed as Edwin*sson*).

- - **Unknown**(default)
  - Married
  - Unmarried
  - Civil Union

<!-- -->

- Default:**150**

<!-- -->

- This option controls the information displayed in the status bar. This can be either the **Active person's name and ID**(default) or **Relationship to home person**.

<!-- -->

- *checked* (default) This checkbox controls whether or not a text description is displayed next to the icon in the [Navigator](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window#Navigator) in the [Main Window](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window#Main_Window). This option takes effect after the program has been restarted.

<!-- -->

- *unchecked*(default)

#### Display Name Editor

![[_media/EditPreferences-Display-tab-DisplayNameEditor-dialog-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Display Name Editor - dialog (example) from Menu: &quot;Edit&gt;Preferences...&quot; - &quot;Display&quot; - tab]] The following keywords are replaced with the appropriate name parts:

- <b>Given</b> - given name (first name)
- <b>Title</b> - title (Dr., Mrs.)
- <b>Call</b> - call name
- <b>Initials</b> - first letters of Given
- <b>Primary, Primary\[pre\] or \[sur\] or \[con\]</b>- full primary surname, prefix, surname only, connector
- <b>Patronymic, or \[pre\] or \[sur\] or \[con\]</b> - full pa/matronymic surname, prefix, surname only, connector
- <b>Familynick</b> - family nick name
- <b>Rest</b> - non primary surnames
- <b>Rawsurnames</b>- surnames (no prefixes and connectors)
- <b>Surname</b> - surnames (with prefix and connectors)
- <b>Suffix</b> - suffix (Jr., Sr.)
- <b>Nickname</b> - nick name
- <b>Common</b> - nick name, otherwise first of Given
- <b>Prefix</b> - all prefixes (von, de)
- <b>Notpatronymic</b>- all surnames, except pa/matronymic & primary

Extra parentheses, commas are removed. Other text appears literally.

![[_media/NameEditor-format_reference_example-51.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Display Name Editor - reference person]]

**Example:** Dr. Edwin Jose von der Smith and Weston Wilson Sr (“Ed”) - Underhills *Edwin Jose*: Given, *von der*: Prefix, *Smith* and *Weston*: Primary, *and*: <abbr title="a connector">\[con\]</abbr>, *Wilson*: Patronymic, *Dr.*: Title, *Sr*: Suffix, *Ed*: Nickname, *Underhills* <abbr title="family nick name">Familynick</abbr>, Jose <abbr title="called (preferred given name)">call</abbr>.

All the fields in the Example except the Family Nickname can be added in the standard Person Editor dialog. Double-click the Preferred name in Names tab of the Person Editor to access additional fields including: the Family Nick Name, Grouping controls, exception Sorting & Display controls, Date range controls for using a particular name. {{-}}

#### Place Format Editor

![[_media/EditPreferences-Display-tab-PlaceFormatEditor-dialog-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Place Format Editor - dialog (example) from Menu: "Edit&gt;Preferences..." - "Display" - tab]]

Accessed from the [Display](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Display) tabs Place Format option.

This tab contains preferences relevant to how Places should be shown.

- A unique name for the place format.

- The place names to be displayed.

Each level in the hierarchy is represented by a positive integer, starting with 0 for the selected place and increasing by 1 for each level up the hierarchy. The levels can also be represented by negative integers, starting with -1 for the top level (usually a country) and decreasing by 1 for each level lower in the hierarchy. In addition, the populated place (city, town, village or hamlet) is represented by the letter p; this can be used with an offset (e.g. p+1 or p-2).

The names to be displayed are defined as a comma-separated list of ranges. A range can either be a single level, or a start level and an end level separated by a colon. The start level must be less than the end level in a range. The start and end levels default to 0 and -1 if missing.

- "None" (Default), "Number Street" or "Street Number". Option to concatenate the number and street in order to suppress the comma. For this option to work, the street must have the [<strong>Type</strong>](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_2#Place_Editor_dialog) *Street* and house number must have the **Type** *Number*.

- (Empty by Default) A two-digit language code.

-  (checkbox unchecked by default)

See also:

- [Place Editor dialog](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_2#Place_Editor_dialog)
- [Place Name Editor dialog](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_2#Place_Name_Editor_dialog)

{{-}}

### Text

![[_media/EditPreferences-Text-tab-default-51.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menu: "Edit&gt;Preferences..." - "Text" - tab - defaults]]

This tab contains preferences relevant to how missing and private names and records should be shown.

- in the input field you can determine how a missing surname should be displayed. Default value is **`[Missing Surname]`**. You can change this to \[--\] or whatever is most convenient for you.

- in the input field you can determine how a missing given name should be displayed. Default value is **`[Missing Given Name]`**. You can change this to whatever you want.

- Default: `[Missing Record]`

- Default: `[Living]`

- Default: `[Living]`

- Default: `[Private Record]`

{{-}}

### KNo (Kimlik Numarası) Biçimleri

![[_media/EditPreferences-IDFormats-tab-default-51.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menu: "Edit&gt;Preferences..." - "ID Formats" - tab - defaults]]

This tab contains preferences relevant to the automatic generation of Gramps IDs.

- Provides the template for generating IDs for a Person. Default value: `I%04d`

- Provides the template for generating IDs for a Family. Default value: `F%04d`

- Provides the template for generating IDs for a Place. Default value: `P%04d`

- Provides the template for generating IDs for a Source. Default value: `S%04d`

- Provides the template for generating IDs for a Citation. Default value: `C%04d`

- Provides the template for generating IDs for a Media Object. Default value: `O%04d`

- Provides the template for generating IDs for an Event. Default value: `E%04d`

- Provides the template for generating IDs for a Repository. Default value: `R%04d`

- Provides the template for generating IDs for a Note. Default value: `N%04d`

You can use the [Reorder Gramps ID](wiki:Gramps_6.0_Wiki_Manual_-_Tools#Reorder_Gramps_ID) tool to change the format. {{-}}

### Tarihler

![[_media/EditPreferences-Dates-tab-default-51.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menu: "Edit&gt;Preferences..." - "Dates" - tab - defaults]]

Date settings used for calculation operations.

- Default: `<b>%s</b>`

  - Convenience markups are:
    - <b>\<b\>Bold\</b\></b> (Default)
    - <big>\<big\>Makes font relatively larger\</big\></big>
    - <i>\<i\>Italic\</i\></i>
    - <s>\<s\>Strikethrough\</s\></s>
    - <sub>\<sub\>Subscript\</sub\></sub>
    - <sup>\<sup\>Superscript\</sup\></sup>
    - <small>\<small\>Makes font relatively smaller\</small\></small>
    - `<tt>Monospace font</tt>`
    - <u>\<u\>Underline\</u\></u>
      - For example: \<u\>\<b\>%s\</b\>\</u\> will display <u><b>Underlined bold date</b></u>.

- Default: `50`

  - Defines the number of years +/- of the event date "`about `<date>" that the event will return as valid for a filter.
  - Used in the calculation of the person's age.

- Default: `50`

  - Defines the number of years after the event date "`after `<date>" that the event will return as valid for a filter.
  - Used in the calculation of the person's age.

- Default: `50`

  - Defines the number of years before the event date "`before `<date>" that the event will return as valid for a filter.
  - Used in the calculation of the person's age.

- Default: `110`

  - Absent a Death event, the age by which Gramps will consider the person is no longer alive.

- Default: `20`

- Default: `13`

- Default: `20`

{{-}} See also:

- [Gramps 6.0 Wiki Manual - Probably Alive](wiki:Gramps_6.0_Wiki_Manual_-_Probably_Alive)
- [Editing dates](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1#Editing_dates)
- Setting the [date approximation .ini](wiki:Match_dates#Changing_after.2Fbefore.2Fabout_range) manually

{{-}}

### Researcher

![[_media/EditPreferences-Researcher-tab-default-51.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menu: "Edit&gt;Preferences..." - "Researcher" - tab - defaults]]

Allows you to in the corresponding text entry fields. Although Gramps requests information about you, this information is used only so that Gramps can create valid GEDCOM output files. A valid GEDCOM file requires information about the file's creator. If you choose, you may leave the information empty, however none of your exported GEDCOM files will be valid.

The available text entry fields are (all blank by default):

- 

- 

- 

- 

- 

- 

- 

- 

- 

The information entered under this preference acts as default value for family tree specific values that can be adjusted with the [Edit Database Owner Information](wiki:Gramps_6.0_Wiki_Manual_-_Tools#Edit_Database_Owner_Information) tool. {{-}}

### Warnings

![[_media/EditPreferences-Warnings-tab-default-51.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menu: "Edit&gt;Preferences..." - "Warnings" - tab - defaults]]

This tab controls the display of warning dialogs, allowing the re-enabling of dialogs that have been disabled.

- Checkbox checked by Default (See [Dialog](wiki:Gramps_6.0_Wiki_Manual_-_Error_and_Warning_Reference#Suppress_warning_when_adding_parents_to_a_child))

- Checkbox unchecked by Default (See [Dialog](wiki:Gramps_6.0_Wiki_Manual_-_Error_and_Warning_Reference#Suppress_warning_when_cancelling_with_changed_data))

- Checkbox unchecked by Default (See [Dialog](wiki:Gramps_6.0_Wiki_Manual_-_Error_and_Warning_Reference#Suppress_warning_about_missing_researcher_when_exporting_to_GEDCOM))

- Checkbox unchecked by Default (See [Dialog](wiki:Gramps_6.0_Wiki_Manual_-_Error_and_Warning_Reference#Module_not_loaded_warnings))

See the [Error and Warning Reference](wiki:Gramps_6.0_Wiki_Manual_-_Error_and_Warning_Reference) page for examples. {{-}}

### Colors

![[_media/EditPreferences-Colors-tab-default-51.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menu: "Edit&gt;Preferences..." - "Colors" - tab - defaults]]

This tab allows you to set the **colors used for boxes in the graphical views**.

You can select the

- *Light colours*(default) or *Dark colours*

  - \- restores themes default colors.

- Colors for Male persons

- Colors for Female persons

- Colors for Unknown persons

- Colors for Family nodes

- Other colors

{{-}}

#### Pick a Color selector

![[_media/PickAColor-selector-dialog-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Pick a Color" - selector dialog]]

Select a color from the color pallet area, or select the button to create your own color either via direct 'color Hex color code'; the slider or mouse click. {{-}}

### Genealogical Symbols

![[_media/EditPreferences-GenealogicalSymbols-tab-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Genealogical Symbols" - Preferences tab - activated defaults]]

Allows you to use Genealogical symbols instead of text abbreviations in reports, charts and the Gramps interface.

This tab gives you the possibility to use one font which is able to show all genealogical symbols. (Once configured see: [Prerequisite to use Genealogical Symbols](#Prerequisite_to_use_Genealogical_Symbols))

If you select the "use symbols" checkbox, Gramps will use the selected font if it exists.

This can be useful if you want to add phonetic in a note to show how to pronounce a name or if you mix multiple languages like Greek and Russian.

You can only configure the death symbol from this tab.

  
List of Genealogical Symbols shown (listed in order shown at bottom screenshot):

- Female
- Male
- Asexuality, sexless, genderless
- Lesbianism
- Male homosexuality
- Heterosexuality
- Transgender, hermaphrodite (in entomology)
- Transgender
- Neuter

<!-- -->

- Illegitimate
- Birth
- Baptism/Christening
- Engaged
- Marriage
- Divorce
- Unmarried partnership
- Buried
- Cremated/Funeral urn
- Killed in action
- Extinct

<!-- -->

- Death

{{-}}

| meaning | symbol | Unicode code point(s) | name |
|----|----|----|----|
| male | ♂ | U+2642 | Male Sign |
| female | ♀ | U+2640 | Female Sign |
| unknown | ⚪︎ | U+26AA | Medium White Circle |
| hermaphrodite | ⚥ | U+26A4 | Interlocked Male and Female Sign |
| neuter | ⚲ | U+26B2 | Neuter |
| birth | \* | U+002A | Asterisk |
| baptisation, christening | ~ | U+007E | Tilde |
| death | ✝︎ | U+271D | Latin Cross |
| burial | ⚰︎ | U+26B0 | Coffin |
| cremation | ⚱︎ | U+26B1 | Funeral Urn |
| stillborn | ✝︎\* | U+0086 U+002A | Latin Cross, Asterisk |
| born illegitimately | \*⃝ | U+002A U+20DD | Circled Asterisk |
| born illegitimately | ⊛ | U+229B | Circled Asterisk Operator |
| killed in action | ⚔︎ | U+2694 | Crossed Swords |
| this line extinct | ‡ | U+2021 | Double Dagger |
| approximate(ly) | ± | U+00B1 | Plus-Minus |
| before | \< | U+003C | Less-Than Symbol |
| after | \> | U+003E | Greater-Than Symbol |
| engaged | ⚬ | U+26AC | Medium Small White Circle |
| married | ⚭ | U+26AD | Marriage Symbol |
| divorced | ⚮ | U+26AE | Divorce Symbol |
| unmarried | ⚯ | U+26AF | Unmarried Partnership Symbol |

{{-}}

#### Prerequisite to use Genealogical Symbols

![[_media/EditPreferences-GenealogicalSymbols-tab-default-51.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Genealogical Symbols" - Preferences tab - defaults]]

##### Initial setup

If the fontconfig [prerequisite has been installed](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Prerequisite), then on the tab select the button, Gramps will attempt to detect any suitable unicode text fonts that can be used.

![[_media/EditPreferences-GenealogicalSymbols-FindFont-51.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Genealogical Symbols" - Finding fonts]]

When the search has completed select one of the fonts from the list and then select the checkbox:

##### Prerequisite

Prerequisite : **python-fontconfig** : Python bindings of fontconfig and its dependencies are required for displaying genealogical symbols

See also:

- Tamura Jones expounds on [Genealogical Symbols](https://www.tamurajones.net/GenealogySymbols.xhtml) *(the 'Unicode' section is particularly relevant)*
- [GEPS 039: Genealogical symbols in gramps](wiki:GEPS_039:_Genealogical_symbols_in_gramps)
- Feature request: Gramps should be able to use genealogy symbols everywhere.
- [Customize the Genealogical Symbols lookup table](wiki:Customize_the_Genealogical_Symbols_lookup_table) located in the [Gramps user directory](wiki:Gramps_6.0_Wiki_Manual_-_User_Directory#MS_Windows) at: [gramps\gen\utils\symbols.py](https://github.com/gramps-project/gramps/blob/maintenance/gramps51/gramps/gen/utils/symbols.py)

{{-}}

## Other settings

Besides dialog, there are other settings available in Gramps. For various reasons they have been made more readily accessible, as listed below. {{-}}

### Column Editor

![[_media/ConfigureTheActiveView-icon-on-toolbar-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Selecting the  button]]

![[_media/ColumnsEditorTab-dialog-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Column Editor - Dialog - People example]]

The columns of the list views may be added, removed, or reordered in a dialog.

To use the dialog for the current view, choose via the menu , click on ![[_media/Gramps-config.png]] toolbar button or press the *Configure active view* [keyboard keybinding](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings#Common_keybindings).

Only columns with a selected checkbox will be shown in the view. You can also change the position of a column in the View by clicking and dragging it to a new position in the Editor ([*drag and drop*](https://wikipedia.org/wiki/Drag-and-drop)). Once you have made the changes you want click , then click to exit the Editor and see your changes in the View.

By default, the View List, displays several columns of information about the respective category. You can add or remove columns to and from the display

The default sort key for the view \[always ascending\] is the left-most field \[i.e. at the top in the Column Editor\], so changing which field is in that position affects default sorting.

![[_media/ConfigurePersonView-51.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Column Editor - Dialog - Places example]]The dialog will have a different selection of columns for each category of View that displays a simple table.

Changes will only be enacted when the button is clicked.

Once the View columns changes have been applied, clicking once on the column header sorts in ascending order, clicking again sorts in descending order.

The subset of columns and the current [filters](wiki:Gramps_6.0_Wiki_Manual_-_Filters) will also constrain the data exported via the operation. Hidden columns and records will not be exported. {{-}}

### Sorting columns

![[_media/PeopleCategory-PeopleListView-SortedByBirthDateColumn-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Sorted by "Birth Date" column in the list mode of the People Category View - example]]

By default, each Category View presenting data in a columnated table layout will sort the rows in ascending order based on the data in the first (left-most) column. If the table has grouped rows, the grouped data will be sub-sorted. *(Tables in tabbed subsets of data, Editors and Selectors will work similarly.)*

Click once on a different column header to sort on the data of that column in ascending order. Click the header again to sort in reverse order.

The dialog can be used to add, remove and rearrange the displayed columns. Choosing a different first column will make that the new default sorting column of the view \[though always ascending\]. {{-}}

### Ana kişiyi ayarlama

![[_media/MenuEdit-SetHomePerson-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menu showing <em>Set Home Person</em>]]

To set (designate) the [Home person](wiki:Gramps_Glossary#home_person), select the People Category and select the desired person to make them into the [Active Person](wiki:Gramps_Glossary#active_person) and then choose via the menus.

Alternately, when editing any Person, right-clicking on inactive areas (areas without a text-entry box) of the top section displays a pop-up menu which includes an option to of that profile.

The Home person is the persistently designated person who becomes the [Active Person](wiki:Gramps_Glossary#active_person) when one of the following occurs:

- By default, when the Family tree database is opened  
  *(The [General](wiki:Gramps_6.0_Wiki_Manual_-_Settings#General_Gramps_settings) setting in [Preferences](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Preferences) can modify this default behavior. The "Remember last view displayed" will return to the last [Active Person](wiki:Gramps_Glossary#active_person) of the previous session.)*
- As the toolbar button is clicked
- When the Home menu item is selected from either the menu or the right-click context menu in selected views
- As the [keybinding](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings#15) is pressed to return to the **Home Person**.

The toolbar button is available in the People Category, Relationships Category, and Pedigree Category. ![[_media/Gramps_Go-Home48x48_win.png]]

#### Ayrıca bakınız

- [Setting the Home Person](wiki:Gramps_6.0_Wiki_Manual_-_Navigation#Setting_the_Home_Person)

{{-}}

### Adjusting viewing controls

Whether the toolbar, the sidebar, or the filter (not available on Pedigree and Relationships Views) are displayed in the main window is adjusted through the View menu.

In the different views clicking the menu will shows for boxes you can click:

- Navigator
- Toolbar
- Sidebar
- Bottombar
- Full Screen

Additionally, depending on the view you are in, other options will be available on .

- Gramplets:
  - Set Columns to 1
  - Set Columns to 2
  - Set Columns to 3
- Relationships:
  - Show Siblings
  - Show Details
- Geography:
  - Time period
  - Layout

All other Views: the [column editor](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Column_Editor).

### Dışa Aktar Görünümü

![[_media/Menubar-FamilyTrees-overview-FamilyTree-Loaded-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menubar - "Family Trees" - overview example showing "Export View" menu entry]]

On most [Category List Views](wiki:Gramps_6.0_Wiki_Manual_-_Categories#Categories_of_the_Navigator), displayed data maybe be exported, choose via the [menu](wiki:Gramps_6.0_Wiki_Manual_-_Navigation#Main_Menus) command.

This Menu command only appears if the displayed data can be exported. Gramps will export data on screen according your choice: **CSV** or **Open Document** spreadsheet format.

Note that the current configuration of the View's columns will control what data will be exported. The export will contain only the displayed column data (in the same order) and be limited to records matching any [filters](wiki:Gramps_6.0_Wiki_Manual_-_Filters) you have applied. {{-}}

#### Export View as Spreadsheet dialog

![[_media/ExportViewAsSpreadsheet-CSV-file-dialog-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Export View as Spreadsheet" CSV(default) file-dialog - example]]

Gramps will then display the dialog where after choosing a file location to save to and a name for your file; export data on from the Category List View in one of two spreadsheet formats:

- **CSV** (default)
- **OpenDocument Spreadsheet** - ODS format.

{{-}} ![[_media/ExportViewAsSpreadsheet-ODS-Displayed-in-LibreOfficeCalc-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Example ODS Spreadsheet - Displayed in LibreOffice Calc]]

The example screenshot shows an export to the **OpenDocument Spreadsheet** (ODS format) displayed as a Spreadsheet in Libreoffice Calc.

{{-}}

### Modularity and plugins

Gramps has been designed for expansion. The Plugin (a.k.a. Plug-in, Addon, extension) framework provides a path for 3rd party development outside the normal Gramps release distributions.

The documentation for each addon is maintained outside the flow of these main wiki chapters. The interface & functionality of the software & documentation may not conform with the styles seen throughout the rest of Gramps... although we encourage Developers to try to make their additions as seamless as possible.

A brief description & screenshot of each addon can be found in the [Addon List](wiki:6.0_Addons#Addon_List) section of the wiki manual. The separately maintained documentation page for the addon is linked from the 1st column of that list.

See [Plugin Manager](wiki:Gramps_6.0_Wiki_Manual_-_Plugin_Manager) and [Third-Party Addons](wiki:6.0_Addons). {{-}}

### Customize report output formats

![[_media/TextReports-DocumentOptions-section-PlainText-output-settings-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Document Options - tab defaults for Text Reports (Plain Text - output selected) example]]

What kind of output customization is available? This dialog allows you to change the fonts, font sizes, font color, background color of the text and alignment of paragraphs on the report.

For most report dialogs, in the top part are option tabs specifically related that particular report. The lower part will have more broadly reusable features and is called the section.

From the drop down list you can choose an existing custom style. Or to make your own select the button to show the dialog and then select the button to show the dialog.

{{-}}

#### Document Styles dialog

![[_media/DocumentStyles-dialog-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Document Styles - dialog - default]]

The dialog, list the *default* style and any custom styles for that report and allows you to edit or delete any custom styles you have created. Select the button to show the dialog. {{-}}

#### Style editor dialog

The dialog allow you to customize the document style specific to each report.

Change the (`New Style`default) field to a unique name as it will appear in drop down list.

Once changes for your custom style have been finalized select the button to save the changes or to exit.

{{-}}

##### Style editor dialog tabs

On the left hand side you will see the column that list the paragraph options specific to that report that you may modify. For example the shows the style options for AHN-Entry, AHN-Generation and AHN-Title.

On the right hand side are three tabs associated with each style listed in the left hand column: {{-}}

###### Description

![[_media/StyleEditor-dialog-Description-tab-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Description options tab - Document Styles - dialog (default styles for Ahnentafel Report) (Gramps 4.2.0 Windows 7)]]

- : The description describes what each paragraph is all about. For example shown here is the style used for the Ahnentafel Report ( AHN-Entry ).

{{-}}

###### Font options

![[_media/StyleEditor-dialog-FontOptions-tab-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Font options" tab - "Style Editor" dialog for "Document Styles" (default styles for Ahnentafel Report)]]

- : Here you can set the Roman or Swiss, the of the font in pt., the of the font and some like Bold, Italic or Underline.

{{-}}

###### Paragraph options

![[_media/StyleEditor-dialog-ParagraphOptions-tab-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Paragraph options" tab - "Style Editor" dialog for "Document Styles" (default styles for Ahnentafel Report)]]

- : Here you set the , the , , and of your style.

{{-}}

### Context menu

Used in various places in Gramps; how you access the context menu is dependent on your operating systems:

- On Microsoft windows, you generally use the right button of your mouse to show the context menu or use the keyboard shortcut +. see [Using Context Menus - Microsoft Docs](https://docs.microsoft.com/en-us/previous-versions/windows/desktop/mpc/using-context-menus)
- On Apple macOS, you generally press while clicking the button of your mouse to show the context menu. see: [Contextual Menus - Menus - macOS - Human Interface Guidelines - Apple Developer](https://developer.apple.com/design/human-interface-guidelines/macos/menus/contextual-menus/)

See also:

- [Keybindings](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings)

## Customizing

Here are some ways that you can customize Gramps.

### Preferences

See [Preferences](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Preferences)

### Language

Gramps has been translated into a number of [languages](wiki:Portal:Translators). Usually Gramps automatically starts in your local language, as chosen for other applications, but sometimes this may not be right for you. And in other cases, a module or addon will not yet have been translated and a warning dialog will appear saying something like “Warning: plugin XYZ has no translation for any of your configured languages, using US English instead”. (Note that the US dialect of English is the default rather than British.) This can become annoying or intrusive.

The most idealistic situation is that you are as facile in US English as the language selected for the operating system GUI on your computer. And that you would take the opportunity to translate that Gramps feature for users who are non-English speakers.

If your system is configured to show a language other then English, you can override this for Gramps.

As an example, assume that a computer in the Netherlands is configured to default to Unicode 8 Dutch: "LANG: nl_NL.UTF-8". You could either reset the OS language

In Windows, use the SET command to rest the LAN env variable to "en_GB.UTF-8" for British English. You can do this from the command line interface or [create a startup shortcut with the following Target](https://gramps-project.org/bugs/view.php?id=11009): `C:\Windows\System32\cmd.exe /c "SET LANG=en_GB.UTF-8 && START /D ^"C:\Program Files\GrampsAIO64-6.0.3^" gramps.exe"`

'''

#### Linux

If you want to choose a locale 'variant' for sorting that is not the default variant, then you can start Gramps from the terminal (or console) with a different LC_COLLATE environment. For example, the default sorting (collation) variant for Swedish is "reformed", but you can instead choose "standard" by typing:

`export LC_COLLATE="sv_SE.UTF-8@collation=standard"`  
`python Gramps.py`

#### Mac OS X

For Mac OS X see [Advanced setup](wiki:Mac_OS_X:Application_package#Advanced_setup) for details on how the language is normally chosen, and how to choose a special, non-default setting for the language, the sorting order or the format of such things as day and month names and number separators.

#### MS Windows

![[_media/MicrosoftWindowGrampsAIO-Installer-ChooseComponents-Selection-example-60.png|Microsoft Window Gramps AIO Installer Choose Components-Selection window.]] If you want to run Gramps in another language other than English using the Gramps AIO installer, then you must select it during installation process.

Otherwise it will not be available.

More information can be found at [Download#MS_Windows](wiki:Download#MS_Windows) page.

{{-}}

### Add Windows OS Menu Item

To make Gramps work in your selected language (See table below for your language code), complete the following:

- Using your mouse right button click on the "GrampsAIOxx 5.x.x" icon on Desktop and from menu choose: Copy.
- Right click anywhere on Desktop and from menu choose: Paste shortcut
- New icon will be created with name: "GrampsAIOxx 5.x.x (2)"
- Right click on that and from menu choose: Properties
- A new window will open, click on first tab called General and change text from "GrampsAIOxx 5.x.x (2)" to something more descriptive like: "GrampsAIO Danish"
  - Click on second tab called Shortcut, change text in first entry called Target from (note path will vary depending on Gramps version used):
    - `"C:\Program Files(xxx)\GrampsAIOxx-5.x.x\grampsw.exe"` to:
    - `%comspec% /c set LANG=da_DK.UTF-8 && start grampsw.exe"`
- Click OK and now when you click on that icon Gramps will start in Danish.

### Change the windows LANG variables

Another option if you want Gramps to always load in say:French Canadian language, you can go to Windows \> System Properties, and add the LANG variable in the user section of the environment variables dialog with the appropriate Value.

The value to add is:

    Name: LANG
    Value: fr_CA.UTF-8

### Language codes

Select from the following table of [languages Gramps](wiki:Portal:Translators) has been translated into:

| Language          | ISO code    | Example | Notes |
|-------------------|-------------|---------|-------|
| Dutch             | nl_BE.UTF-8 |         |       |
| English (British) | en_GB.UTF-8 |         |       |
| Finnish           | fi-UTF-8    |         |       |
| French Canadian   | fr_CA.UTF-8 |         |       |
| Russian           | ru_RU.UTF-8 |         |       |
|                   |             |         |       |

- The language codes are two-letter lowercase ISO language codes (such as "da") as defined by [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes).
- The country codes are two-letter uppercase ISO country codes (such as "BE") as defined by [ISO 3166-1](https://en.wikipedia.org/wiki/ISO_3166-1).

### Advanced manipulation of settings

Besides the settings available in Preferences, you may also wish to explore the advanced settings.

Gramps uses **[INI keys](https://en.wikipedia.org/wiki/INI_file#Keys_(properties))** and [INI sections](https://en.wikipedia.org/wiki/INI_file#Sections) for managing user preferences and program settings these are stored in the text file `gramps.ini` under the `.gramps/gramps[XX]` folder in your home or user directory.

The `gramps.ini` file has following sections:

- \[behavior\] : typical Key names are: [betawarn](https://github.com/gramps-project/gramps/blob/master/gramps/gui/grampsgui.py#L502), enable-autobackup, use-tips...
- \[colors\] :
- \[database\] : related to database settings for the Family Tree.
- \[export\] : export and import folders/directories
- \[geography\] :
- \[interface\] : a lot of keys regarding height and width of the different Views: e.g. event-height: 450, event-ref-height: 585, event-ref-width: 728, event-width: 712...
- \[paths\] : keys related to recent imported files and folders/directories
- \[plugin\] :
- \[preferences\] : keys related to preferences: all the common prefixes , todo -colors..
- \[researcher\] : all information regarding the researcher
- \[utf8\] :

#### Example `gramps.ini` file

Example contents of the `gramps.ini` file:

    ;; Gramps key file
    ;; Automatically created at 2020/05/17 15:15:34

    [behavior]
    ;;addmedia-image-dir=''
    ;;addmedia-relative-path=0
    ;;addons-url='https://raw.githubusercontent.com/gramps-project/addons/master/gramps51'
    ;;autoload=0
    ;;avg-generation-gap=20
    ;;betawarn=0
    ;;check-for-addon-update-types=['new']
    ;;check-for-addon-updates=0
    ;;date-about-range=50
    ;;date-after-range=50
    ;;date-before-range=50
    ;;do-not-show-previously-seen-addon-updates=1
    ;;generation-depth=15
    ;;last-check-for-addon-updates='1970/01/01'
    ;;max-age-prob-alive=110
    ;;max-sib-age-diff=20
    ;;min-generation-years=13
    ;;owner-warn=0
    ;;pop-plugin-status=0
    ;;previously-seen-addon-updates=[]
    ;;recent-export-type=3
    ;;runcheck=0
    ;;spellcheck=0
    ;;startup=0
    ;;surname-guessing=0
    translator-needed=0
    ;;use-tips=0
    ;;web-search-url='http://google.com/#&q=%(text)s'
    ;;welcome=100

    [colors]
    ;;border-family=['#cccccc', '#252525']
    ;;border-family-divorced=['#ff7373', '#720b0b']
    ;;border-female-alive=['#861f69', '#261111']
    ;;border-female-dead=['#000000', '#000000']
    ;;border-male-alive=['#1f4986', '#171d26']
    ;;border-male-dead=['#000000', '#000000']
    ;;border-unknown-alive=['#8e5801', '#8e5801']
    ;;border-unknown-dead=['#000000', '#000000']
    ;;family=['#eeeeee', '#454545']
    ;;family-civil-union=['#eeeeee', '#454545']
    ;;family-divorced=['#ffdede', '#5c3636']
    ;;family-married=['#eeeeee', '#454545']
    ;;family-unknown=['#eeeeee', '#454545']
    ;;family-unmarried=['#eeeeee', '#454545']
    ;;female-alive=['#feccf0', '#62242D']
    ;;female-dead=['#feccf0', '#3a292b']
    ;;home-person=['#bbe68a', '#304918']
    ;;male-alive=['#b8cee6', '#1f344a']
    ;;male-dead=['#b8cee6', '#2d3039']
    ;;scheme=0
    ;;unknown-alive=['#f3dbb6', '#75507B']
    ;;unknown-dead=['#f3dbb6', '#35103b']

    [database]
    ;;autobackup=0
    ;;backend='sqlite'
    ;;backup-on-exit=1
    ;;backup-path='C:\\Users\\[username]\\Documents\\GrampsBackup'
    ;;compress-backup=1
    ;;host=''
    ;;path='C:\\Users\\[username]\\Documents\\gramps\\grampsdb'
    ;;port=''

    [export]
    ;;proxy-order=[['privacy', 0], ['living', 0], ['person', 0], ['note', 0], ['reference', 0]]

    [geography]
    ;;center-lat=0.0
    ;;center-lon=0.0
    ;;lock=0
    ;;map='person'
    ;;map_service=1
    ;;path=''
    ;;show_cross=0
    ;;use-keypad=1
    ;;zoom=0
    ;;zoom_when_center=12

    [interface]
    ;;dbmanager-height=350
    ;;dbmanager-horiz-position=12
    ;;dbmanager-vert-position=85
    ;;dbmanager-width=780
    ;;dont-ask=0
    ;;filter=0
    ;;fullscreen=0
    ;;grampletbar-close=0
    ;;ignore-gexiv2=0
    ;;ignore-osmgpsmap=0
    ;;ignore-pil=0
    ;;main-window-height=500
    ;;main-window-horiz-position=15
    ;;main-window-vert-position=10
    ;;main-window-width=775
    ;;mapservice='OpenStreetMap'
    ;;open-with-default-viewer=0
    ;;pedview-layout=0
    ;;pedview-show-images=1
    ;;pedview-show-marriage=0
    ;;pedview-show-unknown-people=0
    ;;pedview-tree-direction=2
    ;;pedview-tree-size=5
    ;;place-name-height=100
    ;;place-name-width=450
    ;;sidebar-text=1
    ;;size-checked=0
    ;;statusbar=1
    ;;surname-box-height=150
    ;;toolbar-on=1
    ;;toolbar-text=0
    ;;treemodel-cache-size=1000
    ;;view=1
    ;;view-categories=['Dashboard', 'People', 'Relationships', 'Families', 'Ancestry', 'Events', 'Places', 'Geography', 'Sources', 'Citations', 'Repositories', 'Media', 'Notes']

    [paths]
    ;;quick-backup-directory='C:\\Users\\[username]\\Documents\\gramps'
    ;;quick-backup-filename='%(filename)s_%(year)d-%(month)02d-%(day)02d.%(extension)s'
    ;;recent-export-dir='C:\\Users\\[username]\\Documents\\gramps'
    ;;recent-file=''
    ;;recent-import-dir='C:\\Users\\[username]\\Documents\\gramps'
    ;;report-directory='C:\\Users\\[username]\\Documents\\gramps'
    ;;website-cal-uri=''
    ;;website-cms-uri=''
    ;;website-directory='C:\\Users\\[username]\\Documents\\gramps'
    ;;website-extra-page-name=''
    ;;website-extra-page-uri=''

    [plugin]
    ;;addonplugins=[]
    ;;hiddenplugins=[]

    [preferences]
    ;;age-display-precision=1
    ;;calendar-format-report=0
    ;;cprefix='C%04d'
    ;;date-format=0
    ;;default-source=0
    ;;eprefix='E%04d'
    ;;family-relation-type=3
    ;;family-warn=1
    ;;fprefix='F%04d'
    ;;hide-ep-msg=0
    ;;invalid-date-format='<b>%s</b>'
    ;;iprefix='I%04d'
    last-view='dashboardview'
    last-views=['dashboardview', '', '', '', '', '', '', '', '', '', '', '', '']
    ;;name-format=1
    ;;no-given-text='[Missing Given Name]'
    ;;no-record-text='[Missing Record]'
    ;;no-surname-text='[Missing Surname]'
    ;;nprefix='N%04d'
    ;;online-maps=0
    ;;oprefix='O%04d'
    ;;paper-metric=0
    ;;paper-preference='Letter'
    ;;patronimic-surname=0
    ;;place-auto=1
    ;;place-format=0
    ;;pprefix='P%04d'
    ;;private-given-text='[Living]'
    ;;private-record-text='[Private Record]'
    ;;private-surname-text='[Living]'
    ;;quick-backup-include-mode=0
    ;;rprefix='R%04d'
    ;;sprefix='S%04d'
    ;;tag-on-import=0
    ;;tag-on-import-format='Imported %Y/%m/%d %H:%M:%S'
    ;;use-last-view=0

    [researcher]
    ;;researcher-addr=''
    ;;researcher-city=''
    ;;researcher-country=''
    ;;researcher-email=''
    ;;researcher-locality=''
    ;;researcher-name=''
    ;;researcher-phone=''
    ;;researcher-postal=''
    ;;researcher-state=''

    [utf8]
    ;;available-fonts=[]
    ;;death-symbol=13
    ;;in-use=0
    ;;selected-font=''

#### Advanced backup filename setting

You can also define the naming pattern for the backup filename by setting the *`paths.quick-backup-filename`* in the `~/.gramps/gramps51/gramps.ini` key file like the following: {{-}}

`[paths]`  
`;;quick-backup-filename='%(filename)s_%(year)d-%(month)02d-%(day)02d.%(extension)s'`

by removing the two semicolons(`;;`) from the front of INI key line and using use any of the following keywords for the filenam pattern:

- filename
- year
- month
- day
- hour
- minutes
- seconds
- extension :
  - **.gpkg**(default) if you include media.
  - *.gramps* if you exclude media.

Use the appropriate ~/.gramps/gramps{XX}/gramps.ini key file.

- Gramps version 6.0 :

`~/.gramps/gramps51/gramps.ini`

See also:

- [Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees#Backup_dialog](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees#Backup_dialog)
- [Gramps_6.0_Wiki_Manual_-_Command_Line#Configuration_.28config.29_option](wiki:Gramps_6.0_Wiki_Manual_-_Command_Line#Configuration_.28config.29_option)
- [Install_latest_BSDDB#Make_Gramps_use_bsddb3](wiki:Install_latest_BSDDB#Make_Gramps_use_bsddb3)
- [Customize_the_Genealogical_Symbols_lookup_table#Genealogy_symbols_preferences](wiki:Customize_the_Genealogical_Symbols_lookup_table#Genealogy_symbols_preferences)

### Theme

The look of Gramps can be changed.

- [Addon:Theme Preferences](wiki:Addon:ThemePreferences)
- [Windows_AIO_themes](wiki:Windows_AIO_themes)
- [GTK 3 theme - GEPS 029: GTK3-GObject introspection Conversion](wiki:GEPS_029:_GTK3-GObject_introspection_Conversion#GTK_3_theme)
- [Overrule_Gramps_Icons](wiki:Overrule_Gramps_Icons) - for older Gramps versions.
- [UI style](wiki:UI_style)

Some reports can also be changed:

- [Website report Themes](wiki:Website_report_Themes)

{{-}}

[Category:Tr:Documentation](wiki:Category:Tr:Documentation)
