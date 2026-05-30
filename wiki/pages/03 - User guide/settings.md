---
title: Gramps 6.0 Wiki Manual - Settings
categories:
- Documentation
- Stub
- Tips
managed: false
source: wiki-scrape
wiki_revid: 129849
wiki_fetched_at: '2026-05-30T11:42:25Z'
---

{{#vardefine:chapter\|15}} {{#vardefine:figure\|0}} This section deals with settings you can manage within Gramps either in the dialog or [other various settings](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Other_settings). As well as various ways of [customizing](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Customizing) Gramps.

## Preferences

![[_media/EditPreferencesTabsOnly-overview-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Overview of all default Preferences tabs]]

Most of the settings affecting the entire Gramps program are configured in the dialog. To invoke it, select the menu or select the icon on the toolbar.

There are overrides that can be set *before* running Gramps (such setting the Language shown in the interfaces or for reports) that can be set temporarily or permanently from the [command line interface](wiki:Gramps_6.0_Wiki_Manual_-_Command_Line).

For configuration options that are limited to the current view or Gramplet set, choose via the menu , click on ![[_media/Gramps-config.png]] toolbar button or press the *Configure active view* [keyboard keybinding](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings#Common_keybindings).

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

- 

Also *other* additional tabs maybe shown from any [addons](wiki:6.0_Addons#Addon_List) you may have installed. {{-}}

### Data

![[_media/EditPreferences-Data-tab-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menu: &quot;Edit -&gt; Preferences...&quot; &quot;Data&quot; tab defaults]] The tab contains preferences relevant to the following two sections:

- 

- 

{{-}}

#### Display Options

![[_media/EditPreferences-Data-tab-DisplayOptions-section-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menu: &quot;Edit -&gt; Preferences...&quot; &quot;Data&quot; tab &quot;Display Options&quot; section defaults]] The section contains the following options:

- This option controls the display of places. This feature was labeled as "Enable automatic place title generation" in the 5.0 revision and as "Place format(auto place title)" in the 5.1 revision. The [hierarchy of Places](wiki:Gramps_4.1_Wiki_Manual_-_What%27s_new%3F#Place_hierarchies) was new in the [4.1.0](wiki:Template:Releases/4.1.0) revision and the [Places tab](wiki:Gramps_4.2_Wiki_Manual_-_Settings#Places) of Preferences only existed in the 4.2 version. Major revisions are expected for Place hierarchies so this interfaces is likely to relocated and renamed again.

  - **Full** (default)
    - Selecting the button will show the

- This option controls the display of Coordinates. (See [Supported longitude/latitude formats](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_2#Supported_longitude.2Flatitude_formats))

  - **DEG Degree,minutes,seconds notation** (default)
  - DEG-: degree, minutes, seconds notation with :
  - D.D4 degree notation, 4 decimals
  - D.D8 degree notation, 8 decimals (precision like ISO-DMS)
  - RT90 Output format for the [Swedish coordinate system RT90](https://en.wikipedia.org/wiki/Swedish_grid)

- This option controls the display of names in the current database (the setting is saved in the database and is not system wide). In Gramps there are two type of name display formats: the predefined formats, and the user defined custom formats. Several different predefined name formats are available: **"Surname, Given Suffix"** (default), *"Given Surname Suffix"*, *"Given"*, *"Primary\[sur\] Primary\[con\] NotPatronymic, Given Patronymic\[sur\] Suffix Primary\[pre\]"*

  - Clicking on the right hand side button will bring up a window where the available list of options is shown. The format is given as well as an example. When predefined formats are not suitable one can define one's own format. You can use the button to add a Name format to the list. Clicking once will give you a **SURNAME,Given Suffix(call)** format and as example : **SMITH, Edwin Jose Sr (Ed)**. If you added new name formats to the list the and buttons become available to change the name format list.
    -   
      Checkbox unselected by default. If selected enables Gramps to consider patronymic and matronymic names as surnames.

- This option controls the display of dates. It is a global setting, requiring a restart of Gramps to take effect, and applies to the display of dates in all databases loaded within Gramps until such time as the date display format is changed again. Several different formats are available, which may be dependent on your locale.

  - **YYYY-MM-DD (ISO)** (default) - Example 2020-09-30 - Displays the date using the international standard [ISO 8601 Data elements and interchange formats – Information interchange](https://wikipedia.org/wiki/ISO_8601) particularly useful when sharing data between countries with different conventions for writing numeric dates and times.
  - Numerical
  - Month Day, Year
  - MON DAY, YEAR
  - Day Month Year
  - DAY MON YEAR

<!-- -->

- 

  - **Years** (default)
  - Years, Months
  - Years, Months, Days

- 

- 

<!-- -->

- **Gregorian** (default). This option controls the display of calendar on reports, tools, gramplets, views. Several different calendars are available (see [Date Edition](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_Editing_Data:_Detailed_-_part_1#Editing_dates)). Two dates with two different calendars will not properly display timeline or period, (e.g. Using the Gregorian calendar as the default displayed calendar, users will have a better coherency for displaying dates on period).

- **Gregorian** (default).

- **On the previous day** (default).

<!-- -->

- This option controls the information displayed in the status bar. This can be either the **[Active Person](wiki:Gramps_Glossary#active_person)'s name and ID** (default) or **Relationship to [home person](wiki:Gramps_Glossary#home_person)**.

<!-- -->

- **Legacy** (default). Select from the available plugins for composing and display of Citation data. The built-in "Legacy" [CITE plugin](wiki:Addon_list_legend#cite) is compatible with versions 5.1.6 and earlier.

##### Place Format Editor

![[_media/EditPreferences-Data-tab-DisplayOptions-section-PlaceFormatEditor-dialog-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Place Format Editor - dialog (default) from Menu: "Edit &gt; Preferences..." - "Data" tab "Display Options" section]]

The dialog contains preferences relevant to how Places should be shown.

The dialog can be accessed from the  - "Data" tab in the [Display Options](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Display_Options) section via the button on the option.

The dialog allows you to create custom Place formats by using the button in the left column and choosing how each part of the Place shown should be displayed based on the following settings:

- `New` (by default) - A name for the place format strongly suggest you change this to be unique.

- `:` (default colon ":" meaning display all of the place name ) - Select the hierarchy levels of the place names to be displayed.

  - Each level in the hierarchy is represented by a positive integer, starting with 0 for the selected place and increasing by 1 for each level up the hierarchy. The levels can also be represented by negative integers, starting with -1 for the top level (usually a country) and decreasing by 1 for each level lower in the hierarchy. In addition, the populated place (city, town, village or hamlet) is represented by the letter p; this can be used with an offset (e.g. p+1 or p-2).
  - The names to be displayed are defined as a comma-separated list of ranges. A range can either be a single level, or a start level and an end level separated by a colon. The start level must be less than the end level in a range. The start and end levels default to 0 and -1 if missing.

- \- Optionally concatenate the number and street in order to suppress the comma.

  - **None** (default) - Display as is.
  - *Number Street* - For these options to work, the street must have the [<strong>Type</strong>](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_2#Place_Editor_dialog) *Street* and house number must have the **Type** *Number*.
  - *Street Number* - as per *Number Street*

- (Empty by Default) A [two-digit language code](https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes).

-  (checkbox unchecked by default)

You can remove a custom place format using the button.

The has one pre-defined format named **Full** by default.

See also:

- [Implement place formats \#368](https://github.com/gramps-project/gramps/pull/368)
- [Hierarchical Place Structure](wiki:Hierarchical_Place_Structure)
- <https://gramps-project.org/wiki/index.php/GEPS_045:_Place_Model_Enhancements_-_Place_Changes_Screenshots#Enhanced_Place_Format_Editor>
- [(Gramps-users) Proposed place formatting dialogs](https://sourceforge.net/p/gramps/mailman/message/36637553/) From: Nick Hall. - 2019-04-11
- <https://sourceforge.net/p/gramps/mailman/message/36422019/>
- <https://sourceforge.net/p/gramps/mailman/message/36363239/>
- <https://sourceforge.net/p/gramps/mailman/message/35694337/>
- [Place Editor dialog](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_2#Place_Editor_dialog)
- [Place Name Editor dialog](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_2#Place_Name_Editor_dialog)

{{-}}

###### Example Place Formats

The editor has a new field called "levels". It allows users to select hierarchy levels in the place loosely based on the python string slicing syntax. A number of colon ranges can be specified in a comma-separated list. "0" represents the lowest level - typically a building or street. "-1" represents the highest level - typically a country. The populated place is represented as "p".

For example: "p:" = Populated place upwards. "p,-1" = Populated place and country.

Valid options:

- `0 - 9` - Hierarchy Level
- `-` - Negative
- `:` - ??
- `p` - Populated Place
- `,` - comma

Place Format examples

- \["p:" = Populated place upwards\]
- \["p,-1" = Populated place and country.\]
- \[1,p House and city\],\[p,1 City and house\]

It lets you restrict long place descriptions in reports and views. [1](https://github.com/gramps-project/gramps/pull/368#issuecomment-290886087)

{{-}}

##### Display Name Editor

![[_media/EditPreferences-Data-tab-DisplayOptions-section-DisplayNameEditor-dialog-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;Display Name Editor&quot; - dialog (default) from Menu: &quot;Edit&gt;Preferences...&quot; - &quot;Data&quot; tab &gt; &quot;Display Options&quot; section]] The allows you to define custom name formats, that can be shown on reports and charts at a global level or a per person level.

The has two section:

- section shown at the top

- table section

The can be accessed from the menu:  - tab \> sections button. {{-}}

###### Help Reference

Display Name Help Reference:

<hr>

The following keywords are replaced with the appropriate name parts:

- **Given** - given name (first name)
- **Title** - title (Dr., Mrs.)
- **Call** - call name
- **Initials** - first letters of Given
- **Prefix** - all prefixes (von, de)
- **Surname** - surnames (with prefix and connectors)
- **Suffix** - suffix (Jr., Sr.)
- **Nickname** - nick name
- **Common** - nick name as first option if it exists, Call as second option, otherwise first of Given

<hr>

  
Surname:

- **Rest** - non primary surnames
- **Familynick** - family nick name
- **Primary, Primary\[pre\] or \[sur\] or \[con\]**- full primary surname, prefix, surname only, connector
- **Patronymic, or \[pre\] or \[sur\] or \[con\]** - full pa/matronymic surname, prefix, surname only, connector
- **Notpatronymic**- all surnames, except pa/matronymic & primary
- **Rawsurnames**- surnames (no prefixes and connectors)

<hr>

Extra parentheses, commas are removed. Other text appears literally.

<hr>

  
**Example:** Dr. Edwin Jose von der Smith and Weston Wilson Sr (“Ed”) - Underhills  

*Edwin Jose*: **Given**, *von der*: **Prefix**, *Smith* and *Weston*: **Primary**, *and*: <abbr title="a connector">**\[con\]**</abbr>, *Wilson*: **Patronymic**,  

*Dr.*: **Title**, *Sr*: **Suffix**, *Ed*: **Nickname**, *Underhills* <abbr title="family nick name">**Familynick**</abbr>, Jose <abbr title="called (preferred given name)">**Call**</abbr>.

<hr>

{{-}}

###### Help Reference Example person

![[_media/wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_3#Name_Editor|[_media/NameEditor-format_reference_example-51.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Display Name Editor's - reference person shown in the [Name Editor]] dialog]]

All the fields for the Help Reference **Example** person except the Family Nickname can be added in the standard Person Editor dialog. Double-click the Preferred name in Names tab of the Person Editor to access additional fields including: the Family Nick Name, Grouping controls, exception Sorting and Display controls, Date range controls for using a particular name. {{-}}

###### Display Name list

In this section you can add, remove or edit existing name formats as well as see an example of the formatted name.

Table shows two headings and

- \- Based on the name parts shown

- \- Displays the name format applied to a ? [builtin reference person](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Help_Reference_Example_person) ?

The List shows four default display name formats they are:

- *Surname, Given Suffix* - displays the name as:
- *Given Surname Suffix* - displays the name as:
- *Given* - displays the name as: *Edwin Jose*
- *xxx*' - displays the name as:

<!-- -->

- \- a new name format, type the required keywords as needed and press the key to see the resulting

- \- an existing name format (except for the four default name formats )

- \- an existing name format (except for the four default name formats )

{{-}}

#### Input Options

![[_media/EditPreferences-Data-tab-InputOptions-section-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menu: "Edit -&gt; Preferences..." "Data" tab "Input Options" section defaults]]

- <span id="surname guessing"><span> This option affects the initial family name of a child when they are added to the family tree.
  - **Father's surname** (default) - will use the family name of the father.
  - *None* - means that no surname guessing will be attempted.
  - *Combination of mother's and father's surname* - will use the father's name followed by the mother's name.
  - *[Icelandic style](https://wikipedia.org/wiki/Icelandic_name)* - will use the father's given name followed by the "sson" suffix (e.g. the son of Edwin will be guessed as Edwin*sson*).

- \- used by the dialog.

  - **Unknown** (default)
  - *Married*
  - *Unmarried*
  - *Civil Union*

<!-- -->

-   
  Latter Days Saints

{{-}}

### General

![[_media/EditPreferences-General-tab-EnviromentSettings-section-default-60.png|Right|thumb|450px|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menu: "Edit -&gt; Preferences..." "General" tab "Environment Settings" section defaults]]

This tab contains one section containing preferences relevant to the general operation of the program.

#### Environment Settings

-   
  This checkbox option controls the enabling and disabling of the dialog at startup.

-   
  Selecting this checkbox option causes the last used database to load upon start. It bypasses the **Manage Family Trees** dialog.

-   
  This checkbox option controls the enabling and disabling of the display of the last [View](wiki:Gramps_Glossary#view). Enabling will bring you to the view where you stopped the program the last time.

-   
  This checkbox option controls the enabling and disabling of the global spelling checker for notes. The **[gspell](https://gitlab.gnome.org/GNOME/gspell)** package must be loaded for this to have an effect.[2](https://github.com/gramps-project/gramps/pull/1450) ( See: [Troubleshoot Spellcheck](wiki:Troubleshoot_Spellcheck) ) (Note the Edit\>preferences option enables global English or the language your Gramps is run in and the note context menu is per note in the selected Language of your choice)

<!-- -->

- *checked* (default) This checkbox controls whether or not a text description is displayed next to the icon in the [Navigator](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window#Navigator) in the [Main Window](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window#Main_Window). This option takes effect after the program has been restarted.

<!-- -->

- 

- 

- 

- 

- 

- 

  - **Both text and icons** (default)
  - *Text only*
  - *Icons only*

- *checked*(default)

<!-- -->

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

<!-- -->

- Default: `150` Pixels

#### Tip of the Day dialog

![[_media/TipOfTheDay-dialog--example-PrivacyInGramps-60.png|Right|thumb|400px|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Tip of the Day dialog - example]]

When enabled in tab the dialog shows helpful hints.

The following options are available:

-  (check box checked by default - once enabled) - uncheck to stop further tips appearing.

- \- Advance to the next tip.

- \- exit for this session until the Gramps program is restarted.

{{-}}

### Family Tree

![[_media/EditPreferences-FamilyTree-tab-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menu:  - &quot;Family Tree&quot; - tab - defaults]] The tab contains the following four sections:

- 

- 

- 

- 

See also:

- [Backing up a family tree](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees#Backing_up_a_Family_Tree) - more information on backups
- [Backup omissions](wiki:Template:Backup_Omissions) - what is not included during a backup

{{-}}

#### Database Settings

![[_media/EditPreferences-FamilyTree-tab-DatabaseSetting-section-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menu:  - "Family Tree" - tab - "Database Settings" section defaults]]

- \-

  - **[SQLite](wiki:Gramps_Glossary#sqlite)** (*default*) - the [DB-API Database Backend](wiki:DB-API_Database_Backend)
  - ... If other database backends addons are installed, they will be added to the list <abbr title="exempli gratia - Latin phrase meaning 'for example'">e.g.</abbr>: [PostgreSQL](wiki:Addon:PostgreSQL) backend

See also:

- Addon [PostgreSQL](wiki:Addon:PostgreSQL) - this adds experimental support for PostgreSQL databases. Recommended for Experts only!

{{-}}

#### Database Location

![[_media/EditPreferences-FamilyTree-tab-DatabaseLocation-section-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menu:  - "Family Tree" - tab - "Database Location" section defaults]]

- \- Server address or other computer IP address for the location of the database.

- \- Port number to access the Host database

- Unless you have a definite reason to change this, stay with the default path. The default path where databases are stored is `grampsdb` within the [User Directory](wiki:Gramps_6.0_Wiki_Manual_-_User_Directory).

{{-}}

#### Backup Management

![[_media/EditPreferences-FamilyTree-tab-BackupManagement-section-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menu:  - "Family Tree" - tab - "Backup Management" section defaults]]

- \- Location in which to save your Gramps backup archive files.

- \- Selecting this option will Backup Your family tree upon choosing to exit Gramps. The file be saved to the Backup path specified above. The filename of the backup will match the Family Tree appended with a date and time.

- timer interval for triggering full backups during Gramps editing sessions.

  - **Never** (*default*)
  - Every 15 minutes
  - Every 30 minutes
  - Every hour
  - Every 12 hours
  - Every day

{{-}}

#### Family Tree's Media path

![[_media/EditPreferences-FamilyTree-tab-FamilyTreesMediaPath-section-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menu:  - "Family Tree" - tab - "Family Tree's Media path" section defaults]]

- Here you can fill in a base path for the media objects.

  - Selecting the button gives you a dialog where you can fill in the required path.

See also:

- [](wiki:Gramps_6.0_Wiki_Manual_-_Tools#Media_Manager) a group of four separate tools two of which allow you to:
  - 

  - 

{{-}}

##### Select media directory dialog

See [Gramps_6.0_Wiki_Manual_-_Settings#File_Chooser](wiki:Gramps_6.0_Wiki_Manual_-_Settings#File_Chooser) {{-}}

##### Missing Media Objects 'broken link' icon of a box with a red 'x'

![[_media/BrokenMediaPath-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Media object with a broken filepath]]

If the Preview thumbnails displays 'broken link' icon of a box with a red 'x' you will need to correct for your family tree in the section.

See also:

- Example.gramps - [Connecting to the example Media Objects](wiki:Example.gramps#Connecting_to_the_example_Media_Objects)
- [Media Verify Tool](wiki:Addon:Media_Verify_Tool) addon tool for revalidating media paths

{{-}}

### Import

![[_media/EditPreferences-Import-tab-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menu: &quot;Edit&gt;Preferences...&quot; - &quot;Import&quot; - tab - defaults]] The tab has two sections as follows:

- 

- 

#### Tag Records

-   
  Checkbox (Default: `Imported %Y/%m/%d %H:%M:%S` ) **Note - Adding a timestamped [Tag](wiki:Gramps_Glossary#tag) on import can significantly slow down the importing of your data, but are helpful for the ensuing data cleanup.**

#### Source GEDCOM import

-   
  This checkbox option affects the importing of [GEDCOM data](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees#GEDCOM_import). If this is set, each item that is imported will contain a [Source](wiki:Gramps_Glossary#source) reference to the imported file. **Note - Adding a default source can significantly slow down the importing of your GEDCOM data, but are helpful for the ensuing data cleanup.**

{{-}}

### Limits

![[_media/EditPreferences-Limits-tab-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menu: "Edit&gt;Preferences..." - "Limits" - tab - defaults]]

Settings used for calculation operations of dates, ages and generations.

See also:

- [Gramps 6.0 Wiki Manual - Probably Alive](wiki:Gramps_6.0_Wiki_Manual_-_Probably_Alive)
- [Editing dates](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1#Editing_dates)
- Setting the [date approximation .ini](wiki:Match_dates#Changing_after.2Fbefore.2Fabout_range) manually

#### Calculation limits

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

- You can enter the number of generations used to determine relationships. The default value is **`15`**. Limits the scope of features based on the [Relationship Calculator](wiki:Gramps_6.0_Wiki_Manual_-_Tools#Relationship_Calculator).

{{-}}

### Colors

![[_media/EditPreferences-Colors-tab-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menu: "Edit&gt;Preferences..." - "Colors" - tab - defaults]]

This tab has seven section related to allowing you to set the **colors used for boxes in the graphical views**.

Each of the colors can be customized using the .

#### Colors used for boxes in the graphical views

You can select the

- - **Light colors** (default)
  - *Dark colors*
    - \- restores themes default colors.

#### Colors for Male persons

- \[ \] \#b8cee6

- \[ \] \#1f4986

- \[ \] \#b8cee6

- \[ \] \#000000

#### Colors for Female persons

- \[ \] \#feccf0

- \[ \] \#861f69

- \[ \] \#feccf0

- \[ \] \#000000

#### Colors for people who are neither male nor female

- \[ \] \#94ef9e

- \[ \] \#2a5d16

- \[ \] \#94ef9e

- \[ \] \#000000

#### Colors for Unknown persons

- \[ \] \#f3dbb6

- \[ \] \#8e5801

- \[ \] \#f3dbb6

- \[ \] \#000000

#### Colors for Family nodes

- \[ \] \#eeeeee

- \[ \] \#cccccc

- \[ \] \#eeeeee

- \[ \] \#eeeeee

- \[ \] \#eeeeee

- \[ \] \#eeeeee

- \[ \] \#eeeeee

- \[ \] \#ff7373

#### Other colors

- \[ \] \#bbe68a

{{-}}

### Genealogical Symbols

![[_media/EditPreferences-GenealogicalSymbols-tab-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menu: "Edit&gt;Preferences..." - "Genealogical Symbols" - tab - defaults]]

Allows you to use Genealogical symbols instead of text abbreviations in reports, charts and the Gramps interface.

This tab gives you the possibility to use one font which is able to show all genealogical symbols. (Once configured see: [Prerequisite to use Genealogical Symbols](#Prerequisite_to_use_Genealogical_Symbols))

If you select the "" checkbox, Gramps will use the selected font if it exists.

This can be useful if you want to add phonetic in a note to show how to pronounce a name or if you mix multiple languages like Greek and Russian.

You can only configure the death symbol from this tab.

  
List of Genealogical Symbols shown (listed in order shown at bottom of screenshot):

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
| hermaphrodite | ⚥ | U+26A5 | Interlocked Male and Female Sign |
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

### ID Formats

![[_media/EditPreferences-IDFormats-tab-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menu: "Edit&gt;Preferences..." - "ID Formats" - tab - defaults]]

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

### Text

![[_media/EditPreferences-Text-tab-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menu: "Edit&gt;Preferences..." - "Text" - tab - defaults]]

This tab contains one section with preferences relevant to how missing and private names and records should be shown.

#### Conditional Text Replacements

- in the input field you can determine how a missing surname should be displayed. Default value is **`[Missing Surname]`**. You can change this to \[--\] or whatever is most convenient for you.

- in the input field you can determine how a missing given name should be displayed. Default value is **`[Missing Given Name]`**. You can change this to whatever you want.

- Default: `[Missing Record]`

- Default: `[Living]`

- Default: `[Living]`

- Default: `[Private Record]`

{{-}}

### Warnings

![[_media/EditPreferences-Warnings-tab-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menu: "Edit&gt;Preferences..." - "Warnings" - tab - defaults]]

This tab has one section that controls the display of warning dialogs, allowing the re-enabling of dialogs that have been disabled.

See the [Error and Warning Reference](wiki:Gramps_6.0_Wiki_Manual_-_Error_and_Warning_Reference) page for examples.

#### Warnings and Error dialogs

- Checkbox unchecked by Default (See [Dialog](wiki:Gramps_6.0_Wiki_Manual_-_Error_and_Warning_Reference#Suppress_warning_when_adding_parents_to_a_child))

- Checkbox unchecked by Default (See [Dialog](wiki:Gramps_6.0_Wiki_Manual_-_Error_and_Warning_Reference#Suppress_warning_when_cancelling_with_changed_data))

- Checkbox unchecked by Default (See [Dialog](wiki:Gramps_6.0_Wiki_Manual_-_Error_and_Warning_Reference#Suppress_warning_about_missing_researcher_when_exporting_to_GEDCOM))

- Checkbox unchecked by Default

- Checkbox unchecked by Default (See [Dialog](wiki:Gramps_6.0_Wiki_Manual_-_Error_and_Warning_Reference#Module_not_loaded_warnings))

{{-}}

### Researcher

![[_media/EditPreferences-Researcher-tab-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menu: "Edit&gt;Preferences..." - "Researcher" - tab - defaults]]

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

The information entered under this preference acts as default value for family tree specific values that can be adjusted with the . {{-}}

## Other settings

Besides dialog, there are other settings available in Gramps. For various reasons they have been made more readily accessible, as listed below. {{-}}

### Columns editor

![[_media/ColumnsEditorTab-dialog-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} <strong>Columns</strong> editor tab - dialog - People Tree View default columns]]

The columns of the list views may be added, removed, or reordered in a editor dialog.

To use the editor dialog for the current view, choose via the menu , click on ![[_media/Gramps-config.png]] toolbar button or press the *Configure active view* [keyboard keybinding](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings#Common_keybindings).

Only columns with a selected checkbox will be shown in the view. You can also change the position of a column in the View by clicking and dragging it to a new position in the Editor ([*drag and drop*](https://wikipedia.org/wiki/Drag-and-drop)). Once you have made the changes you want click , then click to exit the Editor and see your changes in the View.

By default, the View List, displays several columns of information about the respective category. You can add or remove columns to and from the display

The default sort key for the view \[always ascending\] is the left-most field \[i.e. at the top in the Columns Editor\], so changing which field is in that position affects default sorting. For some views the first field cannot be changed and the reason will be mentioned at the top of the Columns editor.

The dialog will have a different selection of columns for each category of View that displays a simple table.

Changes will only be enacted when the button is clicked.

Once the View columns changes have been applied, clicking once on the column header sorts in ascending order, clicking again sorts in descending order.

The subset of columns and the current [filters](wiki:Gramps_6.0_Wiki_Manual_-_Filters) will also constrain the data exported via the operation. Hidden columns and records will not be exported. {{-}}

### Sorting columns

![[_media/PersonView-PeopleListView-example-with-context-menu-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} <strong>Before</strong> - default sort by "Name" column "People" Category - "Person" (List) View]]

![[_media/PeopleCategory-PeopleListView-SortedByBirthDateColumn-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} <strong>After</strong> - Sorted by "Birth Date" column in the list mode of the People Category View - example]]

By default, each Category View presenting data in a columnated table layout will sort the rows in ascending order based on the data in the first (left-most) column. If the table has grouped rows, the grouped data will be sub-sorted. *(Tables in tabbed subsets of data, Editors and Selectors will work similarly.)*

Click once on a different column header to sort on the data of that column in ascending order. Click the header again to sort in reverse order.

The dialog can be used to add, remove and rearrange the displayed columns. Choosing a different first column will make that the new default sorting column of the view \[though always ascending\]. {{-}}

### Setting Home person

![[_media/MenuEdit-SetHomePerson-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menu showing <em>Set Home Person</em>]]

To set (designate) the [Home person](wiki:Gramps_Glossary#home_person), select the People Category and select the desired person to make them into the [Active Person](wiki:Gramps_Glossary#active_person) and then choose via the menus.

Alternately, when editing any Person, right-clicking on inactive areas (areas without a text-entry box) of the top section displays a pop-up menu which includes an option to of that profile.

The Home person is the persistently designated person who becomes the [Active Person](wiki:Gramps_Glossary#active_person) when one of the following occurs:

- By default, when the Family tree database is opened  
  *(The [General](wiki:Gramps_6.0_Wiki_Manual_-_Settings#General_Gramps_settings) setting in [Preferences](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Preferences) can modify this default behavior. The "Remember last view displayed" will return to the last [Active Person](wiki:Gramps_Glossary#active_person) of the previous session.)*
- As the toolbar button is clicked
- When the Home menu item is selected from either the menu or the right-click context menu in selected views
- As the [keybinding](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings#15) is pressed to return to the **Home Person**.

The toolbar button is available in the People Category, Relationships Category, and Charts Category. ![[_media/Gramps_Go-Home48x48_win.png]]

#### See also

- [Setting the Home Person](wiki:Gramps_6.0_Wiki_Manual_-_Navigation#Setting_the_Home_Person)

{{-}}

### Adjusting viewing controls

Whether the toolbar, the sidebar, or the filter (not available on Charts and Relationships Views) are displayed in the main window is adjusted through the View menu.

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

All other Views: the [Columns editor](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Columns_editor).

### Export View

![[_media/Menubar-FamilyTrees-overview-FamilyTree-Loaded-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menubar - "Family Trees" - overview example showing "Export View" menu entry]]

On most [Category List Views](wiki:Gramps_6.0_Wiki_Manual_-_Categories#Categories_of_the_Navigator), displayed data maybe be exported, choose via the [menu](wiki:Gramps_6.0_Wiki_Manual_-_Navigation#Main_Menus) command.

This Menu command only appears if the displayed data can be exported. Gramps will export data on screen according your choice: **CSV** or **Open Document** spreadsheet format.

Note that the current configuration of the View's columns will control what data will be exported. The export will contain only the displayed column data (in the same order) and be limited to records matching any [filters](wiki:Gramps_6.0_Wiki_Manual_-_Filters) you have applied.

Use the Views [CSV Dialect](wiki:Gramps_6.0_Wiki_Manual_-_Settings#CSV_Dialect) tab control the type of CSV to be created. {{-}}

#### Export View as Spreadsheet dialog

![[_media/ExportViewAsSpreadsheet-CSV-file-dialog-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Export View as Spreadsheet" CSV(default) filetype - dialog - example]]

Gramps will then display the dialog where after choosing a file location to save to and a name for your file; export data on from the Category List View in one of two spreadsheet formats:

- - **CSV** (default)
  - **OpenDocument Spreadsheet** - ODS format.

{{-}} ![[_media/ExportViewAsSpreadsheet-ODS-Displayed-in-LibreOfficeCalc-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Example ODS Spreadsheet - Displayed in LibreOffice Calc]]

The example screenshot shows an export to the **OpenDocument Spreadsheet** (ODS format) displayed as a Spreadsheet in LibreOffice Calc.

{{-}}

#### CSV Dialect

![[_media/CSV-Dialect-Tab-dialog-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "CSV Dialect" tab - dialog - example]]

All list table views have a tab in the dialog for the menu. You can choose the CSV format's delimiter to be used when exporting and importing data in Gramps.

*Choose your dialect* from:

- 

- 

- 

- - - ',' *comma* (default)
    - ';' *semicolon*
    - ':' *colon*
    - '\|' *bar*
    - 'tab'

CSV stands for **[comma-separated values](https://wikipedia.org/wiki/Comma-separated_values)**. It is a plain text file format that separate data into columns and rows for simple way to exchange data. Originally, data was limited by being separated into columns by fixed positions in `.txt` text files. When more flexibility was needed, the comma was chosen as a delimiter to mark the boundaries of the columns and the `.csv` format of a text file was established. To complicate matters, different Operating System marked their end-of-line and end-of-file with different terminating codes.

When comma was needed too frequently in the data itself, a `.tsv` (tab-separated-values) file format became popular. When other delimiters began being adopted, rather than use up more file extensions, CSV became synonymous with any text format with delimiter marked columns. They were just different 'dialects' of "CSV".

[Python's `csv` module](https://docs.python.org/3/library/csv.html) provides several pre-defined dialects to simplify reading and writing CSV files. These dialects specify rules for parsing and formatting data. The standard dialects include , , and . The following sections outline each dialect's characteristics, including its separator, line terminator, and quoting behavior.

##### Excel Dialect

The dialect is designed to be compatible with CSV files generated by Microsoft Excel. It is suitable for data that has been saved from Excel as comma-separated values.

- Separator:\*\* Comma (`,`\`)
- Line Terminator: Carriage return and line feed (`\r\n`)
- Quoting:
  - Double quotes (`"`\`) are used to enclose fields containing the separator or other special characters.
  - To include a double quote within a quoted field, it is escaped by doubling it (e.g., `""example""`).

##### Excel-tab Dialect

The dialect is similar to the \`excel\` dialect but uses tabs instead of commas as the separator. This format is often encountered when copying cell data from Excel to the OS clipboard. Pasting tab separated data into the [Import Text](wiki:Addon:Import_Text_Gramplet) addon gramplet is one of the quickest way to populate parts of your tree.

- Separator: Tab (`\t`)
- Line Terminator: Carriage return and line feed (`\r\n`)
- Quoting:
  - Double quotes (`"`) are used to enclose fields containing the separator or other special characters.
  - To include a double quote within a quoted field, it is escaped by doubling it (e.g., `""example""`).

##### Unix Dialect

The dialect is designed for use in Unix-like environments. It uses a line feed character as the line terminator and always quotes all fields.

- Separator: Comma (`,`)
- Line Terminator: Line feed (`\n`)
- Quoting:
  - All fields are enclosed in double quotes (`"`).
  - To include a double quote within a quoted field, it is escaped by doubling it (e.g., `""example""`).

##### See also:

- [CSV: possibility to select the dialect. \#1314](https://github.com/gramps-project/gramps/pull/1314)

{{-}}

### Modularity and plugins

Gramps has been designed for expansion. The Plugin (a.k.a. Plug-in, addon, extension) framework provides a path for third party development outside the normal Gramps release distributions.

The documentation for each addon is maintained outside the flow of these main wiki chapters. The interface and functionality of the software and documentation may not conform with the styles seen throughout the rest of Gramps... although we encourage Developers to try to make their additions as seamless as possible.

A brief description and screenshot of each addon can be found in the [Addon List](wiki:6.0_Addons#Addon_List) section of the wiki manual. The separately maintained documentation page for the addon is linked from the 1st column of that list.

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

![[_media/StyleEditor-dialog-Description-tab-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Description options tab - Document Styles - dialog - default styles for Ahnentafel Report]]

The dialog allow you to customize the document style specific to each report.

Change the `New Style` (default) field to a unique name as it will appear in drop down list.

Once changes for your custom style have been finalized select the button to save the changes or to exit.

##### Style editor dialog tabs

On the left hand side you will see the column that list the paragraph options specific to that report that you may modify. For example the shows the style options for `AHN-Entry`, `AHN-Generation` and `AHN-Title`.

On the right hand side are three tabs associated with each style listed in the left hand column:

- [Description](#Description)
- [Font options](#Font_options)
- [Paragraph options](#Paragraph_options)

{{-}}

###### Description

![[_media/StyleEditor-dialog-Description-tab-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Description options tab - Document Styles - dialog - default styles for Ahnentafel Report]]

- tab describes what each paragraph is all about. For example shown here is the style used for the Ahnentafel Report ( `AHN-Entry` ) with the description: *The basic style used for the text display.*

{{-}}

###### Font options

![[_media/StyleEditor-dialog-FontOptions-tab-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Font options" tab - "Style Editor" dialog for "Document Styles" (default styles for Ahnentafel Report)]]

- tab allows you to set the *Roman* or *Swiss*, the of the font in pt.(point), the of the font and some like *Bold*, *Italic* or *Underline*.

{{-}}

###### Paragraph options

![[_media/StyleEditor-dialog-ParagraphOptions-tab-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Paragraph options" tab - "Style Editor" dialog for "Document Styles" (default styles for Ahnentafel Report)]]

- tab allows you to set the , the , , and of your style.

{{-}}

### Context menu

![[_media/Clipboard-dialog-example-context-menu-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Clipboard - with example contextual pop-up menu from right-clicking a Family]] [Pop-up menus](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window#Pop-up_menus) are used in various places in Gramps; how you access the context menu is dependent on your operating systems:

- On Microsoft windows, you generally use the right button of your mouse to show the context menu or use the keyboard shortcut +. see [Using Context Menus - Microsoft Docs](https://docs.microsoft.com/en-us/previous-versions/windows/desktop/mpc/using-context-menus)
- On Apple macOS, you generally press while clicking the button of your mouse to show the context menu. see: [Contextual Menus - Menus - macOS - Human Interface Guidelines - Apple Developer](https://developer.apple.com/design/human-interface-guidelines/macos/menus/contextual-menus/)

List of known Context menus in Gramps:

- Pedigree View Context menus
- Clipboard context menu
- File Chooser - Context Menu options
- <Category view> context menus
- Manage Books dialog
- ... and many more

See also:

- [Keybindings](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings)

### Selector dialogs

![[_media/wiki:Gramps_6.0_Wiki_Manual_-_Categories#Select_Family_selector|[_media/SelectFamily-SelectorDialog-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} [Select Family selector]] - showing Search Bar]]

Selector dialogs are a combo interface box and you generally use then to select an object (Person/Family/Events etc). Also various also have search bars:

- [Select Family selector](wiki:Gramps_6.0_Wiki_Manual_-_Categories#Select_Family_selector)
- [Select Event selector](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1#Select_Event_selector)
- [Select Note selector](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1#Select_Note_selector)
- [Select Person selector](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1#Select_Person_selector)
- [Select a person for the report selector](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_4#Select_a_person_for_the_report_selector)
- [Select Father selector](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1#Select_Father_selector) (filtered to Father)
- [Select Mother selector](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1#Select_Mother_selector) (filtered to Mother)
- [Select Child selector](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1#Select_Child_selector)
- [Select Media Object selector](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1#Select_Media_Object_selector)
- [Select Place selector](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_2#Select_Place_selector)
- [Select Repository selector](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_2#Select_Repository_selector)
- [Select Source or Citation selector](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_2#Select_Source_or_Citation_selector)
- [Select Source selector](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_2#Select_Source_selector)

{{-}} See also

- [GEPS_041:\_New_Selector](https://gramps-project.org/wiki/index.php/GEPS_041:_New_Selector)
- [Pick a Color selector](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Pick_a_Color_selector)

## Customizing

Here are some ways that you can customize Gramps.

### Preferences

In the "Display Options" section of the Edit\>Preferences tab you can select the Name format used by default throughout Gramps. The Edit button for the opens the , allowing the creation of user-defined (custom) stylings beyond the pre-defined (built-in) name format choices.

See [Preferences](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Preferences)

The Edit button for a person's preferred and alternative names opens the , allowing the selection of a name format exceptions that will override the format chosen in the Display tab of Preferences for the entire Tree.

The name format, grouping and sorting can be overridden for selected individuals and surnames. The Edit Person dialogs have two Edit buttons to access this feature. The button for Preferred name is to the right of the Suffix field. However, for any selected Name (Preferred or Alternative) in the Names tab which opens the Name Editor. The built-in and custom Display Name formats can be selected exceptions to "Group as:" and "Sort as:" options that default to the Name format selected in Preferences.

### Pick a Color selector

The [Colors](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Colors) tab of the Preferences allows customizing of the color of various elements of diagrams in the Charts category's graphical views.

#### Color Palette

![[_media/PickAColor-selector-dialog-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;Pick a Color&quot; - palette selector dialog]] Select a color from the 45 [swatches](wiki:Gramps_Glossary#swatch) in predefined color palette area. Or select from the recently used color swatches. Or click the button to create your own custom color. Right-click on any swatch to add another custom color and open the gradient selector.

You can drag any color swatch to any swatch in the preference (or configure) dialog.

{{-}}

#### Color Gradient

![[_media/PickAColor-gradient-dialog-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;Pick a Color&quot; - gradient selector dialog]] The gradient selector dialog is for adjust the [color swatch](wiki:Gramps_Glossary#swatch) at the top of the dialog. Once changed, either click the button to apply the color. Drag the single gradient dialog swatch to any swatch in the preference (or configure) dialog.

Specific colors of the swatch can be changed in several ways:

- via direct entry 'color Hex color code'
- the hue slider (with a numeric fine control
- mouse left-click in the 1-dimensional (hue) rainbow gradient or the 2-dimensional (brightness and saturation) hue gradient.
- mouse right-click in either gradient to show the numeric control for the dimension(s) of the gradient
- mouse left-click on the eyedropper color picker to choose from any pixel shown on the monitor(s)

{{-}}

### File Chooser

![[_media/FileChooser_Bookmarks_Breadcrumbs.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Linux GTK File Chooser: highlighting breadcrumbs and bookmarking]] ![[_media/FileChooser_Bookmarks_Breadcrumbs_mac.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} macOS GTK File Chooser: highlighting breadcrumbs and bookmarking]] ![[_media/FileChooser_Bookmarks_Breadcrumbs_win.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Windows GTK File Chooser: highlighting breadcrumbs and bookmarking]] The Open and Save dialogs (File Chooser) for Gramps are based on the [GTK File Chooser](https://docs.gtk.org/gtk3/iface.FileChooser.html). Each operating system has expected behaviors for clicks, double-clicks, sorting, [keybindings](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings#Handy_Shortcuts), environmental variables, and standard file locations that are characteristic of File Chooser dialogs native to the operating system. A few of these can be customized via the user interface to feel more similar to the OS native File Choosers. However, the idiosyncrasies of various OSes mean shared network folders and URI support may not be as readily browsed as when using the OS native File Choosers.

The [GtkFileChooser](https://developer-old.gnome.org/gtk4/stable/GtkFileChooser.html) allows for adding quick navigation hotlinks to commonly used places of the filesystem. In the default implementation, these are displayed in the left sidebar navigation pane. It may be a bit unclear at first that these shortcuts come from various sources and in various flavors, so let's explain the terminology here:

- **[Bookmarks](#Bookmarking_file_folders)**: are created by the user, by dragging folders from the right pane to the left pane, or by using the “Add”. Bookmarks can be renamed and deleted by the user.
- **Shortcuts**: can be provided by the Gramps application. For example, program may want to add a shortcut for a Downloads or Documents folder. Shortcuts *cannot* be added or removed by the user. The 'Rename...' context menu option allows them to be relabeled.
- **Volumes**: are provided by the underlying filesystem abstraction. They are the “roots” of the filesystem. The Home and Downloads hotlinks are common "roots". Volumes cannot be modified by the user.

#### File Chooser context menus

Right-click on any file or folder in the current directory to open context pop-up menu with the following options:

<hr>

- 

<hr>

- 

- 

<hr>

- 

- 

- 

- 

- 

<hr>

Right-click in the navigation sidebar to open context pop-up menu with the following options:

<hr>

- 

- 

- 

<hr>

#### Breadcrumbs and text-entry address bar

By default, the file folder navigation in the File Chooser is by browsing. There are also some shortcuts on the left and breadcrumbs (highlighted in green in the dialog illustration) for quick navigation up and down the path.

Optionally, a text-entry address bar can be used to directly key-in or paste a path. Toggle between displaying breadcrumbs and the text-entry address bar with the [keybinding](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings).

#### Bookmarking file folders

File folder bookmarks can be user defined to make finding standard locations easier. These bookmarks are remembered between sessions and regardless of which Family Tree has been loaded.

With any Open or Save dialog open, navigate to the file location containing the folder to be bookmarked. Create the bookmark by either: dragging the folder icon to the navigation column on the left; or, right-clicking that folder to use the context menu option.

Right-clicking an existing Bookmark allows renaming that bookmark or removing it.

#### File Formats

Support for several file formats are built into the standard distribution of Gramps. Import plugin and Export Plugin Addons can be installed via the Plugin Manager or Preferences to expand the options.

See the [Output Format](wiki:Output_formats) article for list of file formats.

#### See also

- [How to Show Text-Entry Address Bar or “Breadcrumbs” (Navigation Buttons)](https://ubuntugenius.wordpress.com/2010/05/14/how-to-show-text-entry-address-bar-or-breadcrumbs-navigation-buttons-in-nautilus-after-ubuntu-10-04-upgrade/) in Nautilus After Ubuntu 10.04 Upgrade

<!-- -->

- Discourse discussions about the GTK File Chooser:
  - [Documenting the File Chooser in the wiki](https://gramps.discourse.group/t/need-suggestions-for-documenting-the-gtk-file-chooser/1820/8)
  - [Illustrating the File Chooser in the Wiki](https://gramps.discourse.group/t/macos-and-windows-gtk-file-chooser-dialog-capture-request/3364)
  - [File Chooser: Sorting files and folders](https://gramps.discourse.group/t/can-i-cause-folders-to-sort-to-the-top-of-the-list-when-presented-with-the-folder-contents/1708/14)
- [Where is the FileChooser feature list?](https://discourse.gnome.org/t/where-is-the-filechooser-feature-list/9101/1)

### Language

Gramps has been translated into a number of [languages](wiki:Portal:Translators). Usually Gramps automatically starts in your local language, as chosen for other applications, but sometimes this may not be right for you. And in other cases, a module or addon will not yet have been translated and a warning dialog will appear saying something like “Warning: plugin XYZ has no translation for any of your configured languages, using US English instead”. (Note that the US dialect of English is the default rather than British.) This can become annoying or intrusive.

The most idealistic situation is that you are as fluent in US English as the language selected for the operating system GUI on your computer. And that you would take the opportunity to translate that Gramps feature for users who are non-English speakers.

If your system is configured to show a language other then English, you can override this for Gramps.

As an example, assume that a computer in the Netherlands is configured to default to Unicode 8 Dutch: "LANG: nl_NL.UTF-8". You could either reset the OS language

In Windows, use the SET command to change the LANG environment variable to "en_GB.UTF-8" for British English. You can do this from the command line interface or [create a startup shortcut with the following Target](https://gramps-project.org/bugs/view.php?id=11009): `C:\Windows\System32\cmd.exe /c "SET LANG=en_GB.UTF-8 && START /D ^"C:\Program Files\GrampsAIO64-6.0.5^" gramps.exe"`

'''

#### Linux

If you want to choose a locale 'variant' for sorting that is not the default variant, then you can start Gramps from the terminal (or console) with a different LC_COLLATE environment. For example, the default sorting (collation) variant for Swedish is "reformed", but you can instead choose "standard" by typing:

`export LC_COLLATE="sv_SE.UTF-8@collation=standard"`  
`python Gramps.py`

#### macOS

For macOS see [Advanced setup](wiki:Mac_OS_X:Application_package#Advanced_setup) for details on how the language is normally chosen, and how to choose a special, non-default setting for the language, the sorting order or the format of such things as day and month names and number separators.

#### MS Windows

![[_media/MicrosoftWindowGrampsAIO-Installer-ChooseComponents-Selection-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Gramps 6.0.3 AIO 64 bit for Microsoft Windows installer - &quot;Choose Components&quot; page showing selection of the &quot;de&quot;( German) Translation]] If you want to run Gramps in another language other than English using the Gramps AIO installer, then you must select it during installation process.

Otherwise it will not be available.

More information can be found at [Installing_Gramps_for_Windows_computers#Missing_other_languages](wiki:Installing_Gramps_for_Windows_computers#Missing_other_languages) page.

{{-}}

### Add Windows OS Menu Item

![[_media/Edit-Target-GrampsAIO64-Properties-Danish-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Edit-Target-GrampsAIO64-Properties for Danish shortcut example.]]

To make Gramps work in your selected language (See table below for your [language code](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Language_codes)), complete the following:

- Using your mouse right button click on the "" icon on Desktop and from menu choose: .
- Right click anywhere on Desktop and from menu choose:
- New icon will be created with name: ""
- Right click on that and from menu choose:
- A new window will open, click on first tab called and change text from "" to something more descriptive like: ""
  - Click on second tab called , change text in first entry called from (note path will vary depending on Gramps version used):
    - `"C:\Program Files\GrampsAIO64-6.x.x\grampsw.exe"` to:
    - `%comspec% /c set LANG=da_DK.UTF-8 && start grampsw.exe"`
- Click

Now when you click on that icon Gramps will start in Danish.

{{-}} {{-}}

### Change the windows LANG variables

Another option if you want Gramps to always load in say: French Canadian language, you can go to Windows \> System Properties, and add the LANG variable in the user section of the environment variables dialog with the appropriate Value.

The value to add is:

    Name: LANG
    Value: fr_CA.UTF-8

- [How to Set Environment Variables in Windows 10](https://www.redswitches.com/blog/environment-variables/#method-1-set-environment-variables-through-the-gui)

### Language codes

Select from the following table of [languages Gramps](wiki:Portal:Translators) has been translated into:

| Language | ISO code | Example | Notes |
|----|----|----|----|
| English-USA (Default) | en_US.UTF-8 | %comspec% /c set LANG=en_US.UTF-8 && start grampsw.exe" |  |
| English (British) | en_GB.UTF-8 | %comspec% /c set LANG=en_GB.UTF-8 && start grampsw.exe" |  |
| Finnish | fi.UTF-8 | %comspec% /c set LANG=fi.UTF-8 && start grampsw.exe" |  |
| Russian | ru_RU.UTF-8 | %comspec% /c set LANG=ru_RU.UTF-8 && start grampsw.exe" |  |
| Albanian | sq_AL.UTF-8 | %comspec% /c set LANG=sq_AL.UTF-8 && start grampsw.exe" |  |
| German | de_DE.UTF-8 | %comspec% /c set LANG=de_DE.UTF-8 && start grampsw.exe" |  |
| French | fr_FR.UTF-8 | %comspec% /c set LANG=fr_FR.UTF-8 && start grampsw.exe" |  |
| French Canadian | fr_CA.UTF-8 | %comspec% /c set LANG=fr_CA.UTF-8 && start grampsw.exe" |  |
| Macedonian | mk_MK.UTF-8 ??? |  |  |
| Nederlands (Dutch) | nl_NL.UTF-8 | %comspec% /c set LANG=nl_NL.UTF-8 && start grampsw.exe" |  |
| Dutch | nl_BE.UTF-8 | %comspec% /c set LANG=nl_BE.UTF-8 && start grampsw.exe" |  |
| Slovak | sk_SK.UTF-8 | %comspec% /c set LANG=sk_SK.UTF-8 && start grampsw.exe" |  |
| Hebrew | he_IL.UTF-8 | %comspec% /c set LANG=he_IL.UTF-8 && start grampsw.exe" |  |
| Danish | da_DK.UTF-8 | %comspec% /c set LANG=da_DK.UTF-8 && start grampsw.exe" |  |
| Greek | el_GR.UTF-8 | %comspec% /c set LANG=el_GR.UTF-8 && start grampsw.exe" |  |
| Italian | it_IT.UTF-8 | %comspec% /c set LANG=it_IT.UTF-8 && start grampsw.exe" |  |
| Esperanto | eo.UTF-8 ??? |  |  |
| Chinese (Simplified) | zh_CN.UTF-8 | %comspec% /c set LANG=zh_CN.UTF-8 && start grampsw.exe" |  |
| Chinese (Hong Kong) | zh_HK.UTF-8 ??? |  |  |
| Chinese (Traditional) | zh_TW.UTF-8 | %comspec% /c set LANG=zh_TW.UTF-8 && start grampsw.exe" |  |
| Ukrainian | uk_UA.UTF-8 |  |  |
| Portuguese | pt_PT.UTF-8 | %comspec% /c set LANG=pt_PT.UTF-8 && start grampsw.exe" |  |
| Portuguese (Brazil) | pt_BR.UTF-8 | %comspec% /c set LANG=pt_BR.UTF-8 && start grampsw.exe" |  |
| Afrikaans | af_ZA.UTF-8 |  |  |
| Norwegian Bokmål | nb_NO.UTF-8 | %comspec% /c set LANG=nb_NO.UTF-8 && start grampsw.exe" |  |
| Norwegian Nynorsk | nn_NO.UTF-8 | %comspec% /c set LANG=nn_NO.UTF-8 && start grampsw.exe" |  |
| Turkish | tr_TR.UTF-8 | %comspec% /c set LANG=tr_TR.UTF-8 && start grampsw.exe" |  |
| Spanish | es_ES.UTF-8 | %comspec% /c set LANG=es_ES.UTF-8 && start grampsw.exe" |  |
| Polish | pl_PL.UTF-8 | %comspec% /c set LANG=pl_PL.UTF-8 && start grampsw.exe" |  |
| Slovenian | sl_SI.UTF-8 | %comspec% /c set LANG=sl_SI.UTF-8 && start grampsw.exe" |  |
| Japanese | ja_JP.UTF-8 | %comspec% /c set LANG=ja_JP.UTF-8 && start grampsw.exe" |  |
| Arabic (Saudi Arabia) | ar_SA.UTF-8 | %comspec% /c set LANG=ar_SA.UTF-8 && start grampsw.exe" |  |
|  |  |  |  |
|  |  |  |  |

- The language codes are two-letter lowercase ISO language codes (such as "da") as defined by [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes).
- The country codes are two-letter uppercase ISO country codes (such as "BE") as defined by [ISO 3166-1](https://en.wikipedia.org/wiki/ISO_3166-1).

### Advanced manipulation of settings

Besides the settings available in Preferences, you may also wish to explore the advanced settings.

Gramps uses **[INI keys](https://en.wikipedia.org/wiki/INI_file#Keys_(properties))** and [INI sections](https://en.wikipedia.org/wiki/INI_file#Sections) for managing user preferences and program settings these are stored in the text file `gramps.ini` under the `.gramps/gramps[XX]` folder in your home or user directory.

The `gramps.ini` file has following sections:

- \[behavior\] : typical Key names are: [betawarn](https://github.com/gramps-project/gramps/blob/master/gramps/gui/grampsgui.py#L502), enable-autobackup, use-tips...
- \[colors\] :
- \[csv\] :
- \[database\] : related to database settings for the Family Tree.
- \[export\] : export and import folders/directories
- \[geography\] :
- \[interface\] : a lot of keys regarding height and width of the different Views: e.g. event-height: 450, event-ref-height: 585, event-ref-width: 728, event-width: 712...
- \[paths\] : keys related to recent imported files and folders/directories
- \[plugin\] :
- \[preferences\] : keys related to preferences: all the common prefixes , todo -colors..
- \[researcher\] : all information regarding the researcher
- \[spacing\] :
- \[test\] :
- \[utf8\] :

#### Example `gramps.ini` file

Example contents of the `gramps.ini` file:

    ;; Gramps key file
    ;; Automatically created at 2025/05/24 08:49:41

    [behavior]
    ;;addmedia-image-dir=''
    ;;addmedia-relative-path=0
    ;;addons-allow-install=0
    ;;addons-projects=[['Gramps', 'https://raw.githubusercontent.com/gramps-project/addons/master/gramps60', True]]
    ;;addons-url='https://raw.githubusercontent.com/gramps-project/addons/master/gramps60'
    ;;autoload=0
    ;;avg-generation-gap=20
    ;;check-for-addon-update-types=['new']
    ;;check-for-addon-updates=0
    ;;date-about-range=50
    ;;date-after-range=50
    ;;date-before-range=50
    ;;do-not-show-previously-seen-addon-updates=1
    ;;generation-depth=15
    ;;immediate-warn=0
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
    ;;use-tips=1
    ;;web-search-url='https://google.com/search?q=%(text)s'
    ;;welcome=100

    [colors]
    ;;border-family=['#cccccc', '#252525']
    ;;border-family-divorced=['#ff7373', '#720b0b']
    ;;border-female-alive=['#861f69', '#261111']
    ;;border-female-dead=['#000000', '#000000']
    ;;border-male-alive=['#1f4986', '#171d26']
    ;;border-male-dead=['#000000', '#000000']
    ;;border-other-alive=['#2a5f16', '#26a269']
    ;;border-other-dead=['#000000', '#000000']
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
    ;;other-alive=['#94ef9e', '#285b27']
    ;;other-dead=['#94ef9e', '#062304']
    ;;scheme=0
    ;;unknown-alive=['#f3dbb6', '#75507B']
    ;;unknown-dead=['#f3dbb6', '#35103b']

    [csv]
    ;;delimiter=','
    ;;dialect='excel'

    [database]
    ;;autobackup=0
    ;;backend='sqlite'
    ;;backup-on-exit=1
    ;;backup-path='C:\\Users\\[username]'
    ;;compress-backup=1
    ;;host=''
    ;;path='C:\\Users\\[username]\\AppData\\Roaming\\gramps\\grampsdb'
    ;;port=''

    [export]
    ;;proxy-order=[['privacy', 0], ['living', 0], ['person', 0], ['note', 0], ['reference', 0]]

    [geography]
    ;;center-lat=0.0
    ;;center-lon=0.0
    ;;lock=0
    ;;map_service=1
    ;;path=''
    ;;personal-map=''
    ;;show_cross=0
    ;;use-keypad=1
    ;;zoom=0
    ;;zoom_when_center=12

    [interface]
    dbmanager-height=370
    ;;dbmanager-horiz-position=12
    ;;dbmanager-vert-position=85
    ;;dbmanager-width=780
    ;;dont-ask=0
    ;;filter=0
    ;;fullscreen=0
    ;;grampletbar-close=1
    ;;hide-lds=0
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
    ;;tipofday-height=350
    tipofday-horiz-position=-49
    tipofday-vert-position=84
    ;;tipofday-width=550
    ;;toolbar-addons=1
    ;;toolbar-clipboard=1
    ;;toolbar-on=1
    ;;toolbar-preference=1
    ;;toolbar-reports=1
    ;;toolbar-style=0
    ;;toolbar-tools=1
    ;;treemodel-cache-size=1000
    ;;view=1
    ;;view-categories=['Dashboard', 'People', 'Relationships', 'Families', 'Ancestry', 'Events', 'Places', 'Geography', 'Sources', 'Citations', 'Repositories', 'Media', 'Notes']

    [paths]
    ;;quick-backup-directory='C:\\Users\\[username]'
    ;;quick-backup-filename='%(filename)s_%(year)d-%(month)02d-%(day)02d.%(extension)s'
    ;;recent-export-dir='C:\\Users\\[username]'
    ;;recent-file=''
    ;;recent-import-dir='C:\\Users\\[username]'
    ;;report-directory='C:\\Users\\[username]'
    ;;website-cal-uri=''
    ;;website-cms-uri=''
    ;;website-directory='C:\\Users\\[username]'
    ;;website-extra-page-name=''
    ;;website-extra-page-uri=''

    [plugin]
    ;;addonplugins=[]
    ;;hiddenplugins=[]

    [preferences]
    ;;age-after-death=1
    ;;age-display-precision=1
    ;;age-rounded-year=1
    ;;calendar-format-input=0
    ;;calendar-format-report=0
    ;;cite-plugin='cite-legacy'
    ;;coord-format=0
    ;;cprefix='C%04d'
    ;;date-format=0
    ;;default-source=0
    ;;eprefix='E%04d'
    ;;family-relation-type=3
    ;;family-warn=0
    ;;february-29=0
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

    [spacing]
    dbman=[22.605613425925927, 5.877459490740741, 9.856047453703704]

    [test]
    ;;january='January'

    [utf8]
    ;;baptism-symbol='~'
    ;;birth-symbol='*'
    ;;buried-symbol='[]'
    ;;cremated-symbol='⚱'
    ;;dead-symbol='✝'
    ;;death-symbol=2
    ;;divorce-symbol='o|o'
    ;;engaged-symbol='o'
    ;;in-use=0
    ;;killed-symbol='x'
    ;;marriage-symbol='oo'
    ;;partner-symbol='o-o'
    ;;selected-font=''

#### Advanced backup filename setting

You can also define the naming pattern for the backup filename by setting the *`paths.quick-backup-filename`* in the `~/.gramps/gramps60/gramps.ini` key file like the following: {{-}}

`[paths]`  
`;;quick-backup-filename='%(filename)s_%(year)d-%(month)02d-%(day)02d.%(extension)s'`

by removing the two semicolons(`;;`) from the front of INI key line and using use any of the following keywords for the filename pattern:

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

`~/.gramps/gramps60/gramps.ini`

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

[Category:Tips](wiki:Category:Tips) [Category:Documentation](wiki:Category:Documentation)
