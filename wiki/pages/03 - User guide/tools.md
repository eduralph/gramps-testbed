---
title: Gramps 6.0 Wiki Manual - Tools
categories:
- Documentation
- Plugins
- Stub
- Tools
managed: false
source: wiki-scrape
wiki_revid: 129627
wiki_fetched_at: '2026-05-30T11:43:27Z'
---

{{#vardefine:chapter\|14}} {{#vardefine:figure\|0}} ![[_media/MenuOverview-Tools-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;&quot; Menubar - Tools Overview - default]] This chapter describes the various available in Gramps.

Gramps allow you to perform various types of analysis of your genealogical data. Typically, the tools do not produce output in form of printouts or files. Instead, they produce screen output immediately available for the researcher. However, when appropriate, you can save the results of running a tool into a file.

## Tools

![[_media/ToolbarIcon-OpenTheToolsDialog-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Toolbar Icon for "Open the tools dialog"]]

The tools can be accessed by choosing the menu .

Alternatively, you can browse the complete selection of available tools along with their brief descriptions in a dialog invoked by clicking the icon on the toolbar from any of the categories. {{-}}

### Tool Selection dialog

![[_media/ToolSelection-dialog-with-debug-menu-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Tool Selection - dialog - default information (and "Debug" tools selection)]]

![[_media/ToolSelection-dialog-example-with-debug-menu-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Tool Selection - dialog - example showing "Check and Repair Database" information (and "Debug" tools selection)]]

The dialog allows you to browse the complete selection of available tools along with their brief descriptions when invoked by clicking the ![[_media/Gramps-tools.png]] icon on the toolbar from any of the categories and use the arrows to expand the listings.

**Select a tool from those available on the left**. Use the arrows to expand the top level listings:

- [Analysis and Exploration](#Analysis_and_Exploration)
- [Debug](#Debug)
- [Family Tree Processing](#Family_Tree_Processing)
- [Family Tree Repair](#Family_Tree_Repair)
- [Utilities](#Utilities)

Then select the tool you are interested in to be shown on the right hand side the following:

- Tool name
- Tool description
- Status:
- Author:
- Author's email:

You can can then use the buttons below to either find out more about the tool or open and run your tool.

- opens the help page if available - needs an internet connection

- exits this dialog

- \-  - opens the tools configuration page.

{{-}} See also: [Report Selection dialog](wiki:Gramps_6.0_Wiki_Manual_-_Reports#Report_Selection_dialog)

### Analysis and Exploration

This section contains tools which analyze and explore the database, but do not alter it. The following analysis and exploration tools are currently available in Gramps:

#### <u>Compare Individual Events</u>

![[_media/CompareIndividualEvents-EventComparisonFilterSelection-dialog-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Compare Individual Events" - "Event comparison filter selection" - dialog]]

This tool collates all the event types discovered in a group of people. Arguably, it could be considered to be more a Report than a Tool. It generates a summary comparison table that begins with the Name and ID of each person, then adds columns for the Event types and dates. If there are multiples of the same event type, additional rows are created. The collation ignores the Roles but includes custom Event types.

The resulting table is useful for comparing of suspected duplicates and revealing inconsistencies. The table can become quite wide so the Save As (in the .ods format) will allow analysis in a spreadsheet application.

You can use this tool via menu which will open the dialog

##### Event comparison filter selection dialog

The people for this comparison can be chosen from previously created custom filters by selecting the drop down list, which defaults to the *Entire Database*. Or by selecting the button, to create custom filters in the editor. To run the report select and the results will be displayed in the dialog.

{{-}}

##### Event Comparison Results dialog

From the dialog you can view the results or the resulting table as a spreadsheet (ODS format). Select to exit the report. {{-}} ![[_media/CompareIndividualEvents-EventComparisonResults-dialog-expanded-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;Compare Individual Events&quot; - &quot;Event Comparison Results&quot; - dialog - expanded example]]

The spreadsheet (ODS format) shows the following output fields:

- `Person, ID, Birth Date, Birth Place, Death Date, Death Place, LVG Date, LVG Place, Burial Date, Burial Place, Marriage Date, Marriage Place`

{{-}}

### Family Tree Processing

This section contains tools which may modify your database. The tools from this section are used mostly for finding and correcting errors in the data. The following Family Tree Processing tools are currently available in Gramps:

- [Edit Database Owner Information](wiki:Gramps_6.0_Wiki_Manual_-_Tools#Edit_Database_Owner_Information)
- [Extract Event Description](wiki:Gramps_6.0_Wiki_Manual_-_Tools#Extract_Event_Description)
- [Extract Information from Names](wiki:Gramps_6.0_Wiki_Manual_-_Tools#Extract_Information_from_Names)
- [Extract Place Data from a Place Title](wiki:Addon:Extract_Place_Data_from_a_Place_Title) - **This tool was moved to [Third-party addons](wiki:Third-party_Addons)**
- [Find Possible Duplicate People](wiki:Gramps_6.0_Wiki_Manual_-_Tools#Find_Possible_Duplicate_People)
- [Fix Capitalization of Family Names](wiki:Gramps_6.0_Wiki_Manual_-_Tools#Fix_Capitalization_of_Family_Names)
- [Merge citations](wiki:Gramps_6.0_Wiki_Manual_-_Tools#Merge_citations)
- [Rename Event Types](wiki:Gramps_6.0_Wiki_Manual_-_Tools#Rename_Event_Types)
- [Reorder Gramps ID](wiki:Gramps_6.0_Wiki_Manual_-_Tools#Reorder_Gramps_ID)
- [Sort Events](wiki:Gramps_6.0_Wiki_Manual_-_Tools#Sort_Events)

#### <u>Edit Database Owner Information</u>

![[_media/DatabaseOwnerEditor-dialog-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Database Owner Editor" - dialog - default]]

The tool modifies any existing [Researcher Information](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Researcher).

Select the menu . This brings up the window, where you can fill in the needed information or use one of the buttons to retrieve existing information.

- 

- 

- 

- 

- 

- 

- 

- 

- 

This information is family tree specific and will be used when exporting your data in GEDCOM format.

Two button choices are available:

- \- to the **Researcher** section.

- \- from the **Researcher** section.

{{-}}

#### <u>Extract Event Description</u>

Extracts event descriptions from the event data by using a model :

`{event type} of {Surname}, {Given name}`

If event description is missing, then tool will use this event description field model.

You can access this tool via the menu

The **Undo history warning** will be shown and you can either or .

Once you this tool will scan and modify your Family Tree and if not present show you the alert otherwise if present you with the:

##### Modifications made result window

![[_media/ExtractEventDescription-ModificationsMade-window-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Extract Event Description's - "Modifications Made" - window - example result]]

result window listing the total number of event descriptions that have been added. {{-}}

#### <u>Extract Information from Names</u>

This tool searches the entire database and attempts to extract titles and nicknames that may be embedded in a person's field. If any information could be extracted, the candidates for fixing will be presented in the table. You may then decide which to repair as suggested and which not to.

You can access this tool via the menu

The dialog will be shown and you can either or .

The dialog will be shown and you can modify each of the options as required and once you have finished select to start the tool. {{-}}

Once the tool finishes either the dialog will be shown as *No titles, nicknames or prefixes were found* or the window will be shown with results of the search. {{-}}

##### Default prefix and connector settings dialog

![[_media/ExtractInformationFromNames-DefaultPrefixAndConnectorSettings-dialog-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Default prefix and connector settings" - dialog for the "Extract Information from Names" Tool]]

The dialog you can modify each of the options as required:

- `de, van, von, di, le, du, dela, della, des, vande, ten, da, af, den, das, dello, del, en, ein, elet, les, lo, los, un, um, una, uno, der, ter, te, die` (default)

- `e, y` (default)

- `de, van` (default)

{{-}}

##### No modifications made dialog

![[_media/ExtractInformationFromNames-NoModificationsMade-dialog-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "No modifications made" - dialog for the "Extract Information from Names" Tool]]

Shown when *No titles, nicknames or prefixes were found* in the selected family tree.

Select to dismiss the dialog.

{{-}}

##### Name and title extraction tool window

The top section shows information about the tool.

![[_media/ExtractInformationFromNames-NameAndTitleExtractionTool-dialog-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Name and title extraction tool" - dialog results window for the "Extract Information from Names" Tool]]

The bottom section displays the results list in a table with the following columns: `Select`, `ID`, `Type`, `Value`, `Current Name`

You can un-`Select` the results you don't want and then to apply those results to your family tree or to do nothing. The button brings you to this tools help section. {{-}}

#### <u>Extract Place Data from a Place Title</u>

#### <u>Find Possible Duplicate People</u>

![[_media/FindPossibleDuplicatePeople-dialog-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Find Possible Duplicate People - dialog - default]]

The **Find Possible Duplicate People** tool searches the entire Tree database, looking for the entries that may represent the same person.

You can access this tool via the menu .

The dialog will be shown and you can adjust the following options:

- : choose between **Low** (default), *Medium* and *High* from the drop down menu.

-  for matching possible duplicate people. (checkbox checked by default)

The following buttons are present: brings you to this page, to stop processing and an button to start processing the data.

Select to start the tool and the data will be processed in two passes.

- Pass 1: Building preliminary lists
- Pass 2: Calculating potential matches.

A progress bar will be shown and depending the speed of your computer and the amount of people in the database this can take some time.

{{-}}

##### <u>Potential Merges</u>

![[_media/FindPossibleDuplicatePeople-PotentialMerges-result-dialog-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Potential Merges" result dialog window for "Find Possible Duplicate People" - dialog - example]]

Once the report finishes a result list window is presented with the following columns shown:

- `Rating` : this gives you an idea of the resemblance between the two people. The higher the ranking, the higher the chance that the people are duplicates.
- `First Person`
- `Second Person`

You can either double-click on the selected row or select the button to check the details.

Three buttons are present: brings you to this page, a to close the window which returns you to the window and a button to which brings up the window which was explained in detail in the dialog. Here you can select with the radio buttons one of the persons and eventually use the button to merge the data if you find the two persons are duplicates.

Selecting the button brings you back to the result list window. {{-}}

#### <u>Fix Capitalization of Family Names</u>

This tool searches the entire database and attempts to fix the capitalization of family names.

The aim is to have conventional capitalization: capital first letter and lower case for the rest of the family name. If deviations from this rule are detected, the candidates for fixing will be presented in the table.

You may then decide which to repair as suggested and which not to.

You can use this tool via menu .

The **Undo history warning** will be shown and you can either or .

{{-}} ![[_media/FixCapitalizationofFamilyNames-CapitalizationChanges-dialog-results-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;Capitalization changes&quot; - dialog - results example for &quot;Fix Capitalization of Family Names&quot; tool]]

If there where changes to the capitalization of any names you will be presented with the results window. The window shows a list of the family names that Gramps can convert to (according to Gramps) correct capitalization (please check that it is correct for you.). In the results window list the following columns are available:

-  - Check or uncheck these on a "by name" basis if you choose not to accept the recommendation (checkbox checked by default)

- \- The name as currently recorded.

- \- The name with change if applied.

Select the names you want to be changed, then select the button. Or use the button to abort changes. {{-}}

You can also install the "[Addon:Fix Capitalization of Given Names](wiki:Addon:Fix_Capitalization_of_Given_Names)" tool Addon that once installed works almost identically to this tool but works for "Given Names" {{-}}

#### <u>Merge citations</u>

You can select this via menu .

The **Undo history warning** will be shown and you can either or . {{-}} ![[_media/MergeCitations-dialog-default-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;Merge Citations&quot; - dialog - default]]

Then the dialog (Title of dialog shows:*Notes, media objects and data-items of matching citations will be combined.*)will be shown

The following options are available:

- drop down list:

  - Match on Page/Volume, Date and Confidence
  - **Ignore Date** (default)
  - Ignore Confidence
  - Ignore Date and Confidence

- -  (checkbox unchecked by default)

{{-}} ![[_media/NumberOfMergesDone-dialog-result-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;Number of merges done&quot; result dialog for &quot;Merge Citations&quot; - dialog - Tool - example]]

Select to run the tool and once complete it will report back the total with the result dialog. {{-}} See also the [Merge Citations](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_3#Merge_Citations) option available from the Citations Category list view {{-}}

#### <u>Rename Event Types</u>

This tool will rename all events of one type to a different type.

You can access this tool via the menu

The **Undo history warning** will be shown and you can either or .

{{-}} ![[_media/RenameEventTypes-Tool-ChangeEventTypes-dialog-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;Change Event Types&quot; - dialog - example for &quot;Rename Event Types&quot; Tool]]

The dialog is presented.

-   
  fill in the text field or use the drop down menu and select an original event type

-   
  fill in the text field (you can create a complete new type here) or use the drop down menu and select a new type

The example shows a renaming of the **Birth** event to a **Baptism** event.

{{-}} ![[_media/RenameEventTypes-Tool-ChangeTypes-result-dialog-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;Change types&quot; - result dialog - example for &quot;Rename Event Types&quot; Tool]]

Finally use the to exit or select to run the tool and once complete it will report back the total events modified with the result dialog. {{-}}

See also:

- [Editing information about events](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_2#Editing_information_about_events)

<span ID="Reorder Gramps ID">

#### <u>Reorder Gramps IDs</u>

</span> This tool can be used to reorder your Gramps object IDs.

![[_media/ReorderGrampsIDs-dialog-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Reorder Gramps IDs" tool window - example]]

You can use this tool via menu .

Initialy the **** will be shown and you can either or .

Then the tool window will be shown where you can modify the [column options](wiki:Gramps_6.0_Wiki_Manual_-_Tools#Reorder_Gramps_IDs_tool_window) as needed then select to start the process.

The tool will then show various progress dialogs during the different progress stages; as the following object IDs' are reordered: 'Reordering People IDs', 'Reordering Family IDs', 'Reordering Event IDs', 'Reordering Place IDs', 'Reordering Source IDs', 'Reordering Citation IDs', 'Reordering Repository IDs', 'Reordering Media Object IDs' and finally 'Reordering Note IDs'.

In the final step 'unused IDs' are searched for and assigned.

During this process the tool will examine each ID to see if it looks like it has been 'customized', if it doesn't look like the previous object ID format or the default object ID format. This might be the case if the user has manually entered their own text in the ID field for the object when editing it. It might also occur if the third-party [GeoName Addon](wiki:Addon:GeoName) has been used or the [GetGOV Addon](wiki:Addon:GetGOV) that stores the **GOV ID** in the Place ID field. If a *customized* ID is found, the tool will show the replace dialog that ask the user if they really wants to replace the ID and also optionally allows the user to use the same answer for same found customized object IDs.

##### Reorder Gramps IDs tool window

![[_media/ReorderGrampsIDs-dialog-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Reorder Gramps IDs" tool window - default on new empty family tree]]

The tool window shows each of Gramps objects (Person, Family, Event, Place, Source, Citation, Repository, Media, Note) and the following option columns (`Object`, '`Actual`, `Quantity`, `Format`, `Change`, `Start`, `Stop`, `Keep`) that can be applied to changing the object ID's.

The button will show this section. The button will exit the tool. The start the tool.

Most of the column labels also double as hidden toggles buttons and perform various actions as described below.

`Object`  
This column lists the type of Gramps ID. Immediately to the left of this column are checkboxes that allow the enabling of changes to individual object types. When checked, the type can be reordered. The label is actually a hidden button that can be used to toggle all of the checkboxes at once.

<!-- -->

`Actual`  
This column shows an example of the current objects ID.

<!-- -->

`Quantity`  
This column show the current number of objects in the family tree.

<!-- -->

`Format`  
This column can be used to change the ID format for each object type. Note that the default ID formats consists of a one letter prefix (I, F, E, P, S, C, R, O, N) representing each of the objects, and then a suffix '`%04d`'. There **MUST** be at least a prefix or a suffix, both are allowed. It is recommended to keep these relatively short. The '`%04d`' defines the length of the numeric portion of the ID, the '`4`' can be changed, anything from '`3`' (allowing numbers from 000-999) to '`9`' (000000000-999999999) is allowed (*If your family tree needs more than "nine hundred ninety-nine million, nine hundred ninety-nine thousand, nine hundred ninety-nine" please raise a feature request!*). Changes made here are the same as made in the menu and then select the **** tab. The '' label is actually a hidden button that can be used to *reset* all the formats to the last used value.

<!-- -->

`Change`  
This column contains checkboxes for each object type. When checked, the IDs for that object will be replaced with new IDs of the `Format` style, unless `Keep` is also checked. If there is no checkmark, the ID formats are *NOT* updated, but the number field within the format is renumbered. The label is actually a hidden button that can be used to toggle all of the check boxes at once.

<!-- -->

`Start`  
This field indicates the starting number used during the renumber operation. The label is actually a hidden button that can be used to toggle between start at `0`, and start after last current number.

<!-- -->

`Step`  
This field indicates the interval between numbers during the renumber, `1` is a simple increment, `2` will increment by 2 etc. The label is actually a hidden button that can be used to toggle between `1`, `2`, `5`, and `10`.

<!-- -->

`Keep`  
This column contains check boxes for each object type. If both the `Keep` and `Change` check boxes are checked, the ID formats for that object will be retained, and the number field within the format is renumbered. The label is actually a hidden button that can be used to toggle all of the check boxes at once.

##### Reorder Gramps IDs replace dialog

![[_media/ReorderGrampsIDs-replace-dialog-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Reorder Gramps IDs" replace dialog - example]]

The replace dialog that ask the user if they really wants to replace the ID and also optionally allows the user to use the same answer for same found customized object IDs.

- 

Select or . {{-}}

#### <u>Sort Events</u>

Events appearing on the Event tab on a *Person* or *Family Editor* are not sorted in any particular order other than the order that the events were added. The reason for not enforcing any particular ordering, particularly ordering by date, is to allow for the situation where an event was known to have happened but the exact chronology is not. Importing or merging data from an external source can lead to extra events being added to, but out of sequence with, the existing set of events of a person or family.

Events can be manually re-ordered by [*drag & drop*](http://en.wikipedia.org/wiki/Drag-and-drop) or by use of the re-order buttons on the tab. Either way, an event can be moved up or down in the list of events and Gramps will remember the new order when the changes are saved. The new ordering will be used wherever events are shown elsewhere in Gramps, such as on a report.

The order of all events on a tab can also be changed by clicking a column title. For example, clicking the `Date` column header will sort all the events in date order. However this way of sorting events is temporary and changes to the event order are not preserved when the window is closed.

The [*drag and drop*](http://en.wikipedia.org/wiki/Drag-and-drop) approach to sorting events is fine for moving a small number of events but is not practical for large scale changes. The has been designed specifically for this purpose, re-sorting all events in the database or just those associated with a targeted selection of people chosen by using a filter.

##### Sort Events tool

You can use this tool via menu .

The **Undo history warning** will be shown and you can either or .

{{-}}

###### Tool Options tab

![[_media/SortEvents-dialog-ToolOptions-tab-default-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Sort Events" Tool - dialog - showing "Tool Options" tab]]

On the tab for the dialog window the first option is used to define the range of people who's events are to be sorted. The first choice in the list is to apply the sorting to all people in the database. Alternative choices are to apply sorting to ancestors and descendants of a chosen person or to a range of people selected by a custom built person filter. After choosing who the sort should apply to, the next thing to consider is how the events should be sorted. The first option is to sort by date. This is probably the most likely choice, but other event attributes can be chosen too. The final choices are whether to make the events sorted ascending or descending and whether to apply the sort to family events that the selected people belong to as well.

{{-}}

### Family Tree Repair

The following Family Tree Repair tools are available:

- [Check and Repair Database](wiki:Gramps_6.0_Wiki_Manual_-_Tools#Check_and_Repair_Database)
- [Rebuild Gender Statistics](wiki:Gramps_6.0_Wiki_Manual_-_Tools#Rebuild_Gender_Statistics)
- [Rebuild Reference Maps](wiki:Gramps_6.0_Wiki_Manual_-_Tools#Rebuild_Reference_Maps)
- [Rebuild Secondary Indexes](wiki:Gramps_6.0_Wiki_Manual_-_Tools#Rebuild_Secondary_Indexes)
- [Remove Unused Objects](wiki:Gramps_6.0_Wiki_Manual_-_Tools#Remove_Unused_Objects)

#### <u>Check and Repair Database</u>

The tool checks the selected database/Family Tree for integrity problems, fixing the problems it can. Specifically, the tool is checking for:

- Broken family links. These are the cases when a person's record refers to a family while the family's record does not refer to that person, and vice versa.

<!-- -->

- Missing media objects. The missing media object is the object whose file is referenced in the database but does not exist. This can happen when the file is accidentally deleted, renamed, or moved to another location.

<!-- -->

- Empty families. These are the family entries which have no reference to any person as their member.

<!-- -->

- Parent relationship. This checks all families to ensure that father and mother are not mixed up. The check is also made that parents have different gender. If they have common gender then their relationship is renamed to "Partners".

You can use this tool via menu .

The **Undo history warning** will be shown and you can either or .

{{-}}

##### Integrity Check Results dialog

![[_media/IntegrityCheckResults-dialog-CheckAndRepairDatabase-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Integrity Check Results" - example result dialog - for the "Check and Repair Database" tool]]

Any issues found are automatically fixed and the dialog will be shown with a summary actions taken. {{-}}

##### No errors were found dialog

Otherwise you will see the dialog stating that *The database has passed internal checks*. {{-}}

##### Gramps had a problem the last time it was run - dialog

![[_media/GrampsHadAProblemTheLastTimeItWasRun-dialog-51.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Gramps had a problem the last time it was run - dialog]]

After Gramps crashes [on restart, Gramps will offer to run Check & Repair](https://github.com/gramps-project/gramps/pull/778) tool. (Introduced in Gramps 5.1.x)

{{-}}

#### <u>Rebuild Gender Statistics</u>

![[_media/GenderStatisticsRebuilt-dialog-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Gender statistics rebuilt" - result dialog for "Rebuild Gender Statistics" tool]]

Rebuilds gender statistics for name gender guessing based on the accumulated statistics of genders for given names within the tree. If a gender is common to more than half the in the Tree with a particular first word in their Given name, then Gramps will guess that Gender for that name will be the same.

The statistics can also be cleared (if the menu has been enabled) with the [Dump Gender Statistics](wiki:Gramps_6.0_Wiki_Manual_-_Tools#Dump_Gender_Statistics) Tool.

You can use this tool via menu .

Once completed the result dialog will be shown.

See [Gender](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1#Gender) entry.

{{-}}

#### <u>Rebuild Reference Maps</u>

![[_media/ReferenceMapsRebuilt-dialog-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Reference maps rebuilt" - result dialog for "Rebuild Reference Maps" tool]]

This tool rebuilds reference map tables. This drives the list of *References* items in editors.

You can use this tool via menu .

Once completed the result dialog will be shown.

##### See also

- This rebuild is also performed as part of the

{{-}}

#### <u>Rebuild Secondary Indexes</u>

![[_media/SecondaryIndexesRebuilt-dialog-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Secondary indexes rebuilt" - result dialog for "Rebuild Secondary Indexes" tool]]

This tool rebuilds secondary indices.

You can use this tool via menu .

Once completed the result dialog will be shown.

The re-constructs the secondary tables in the Tree db. These tables include things like gender statistics (Given Name versus gender) to allow guessing the gender of names as they are entered, surnames (for faster lookup of possible surname and to make the person tree view work), the various IDs for objects (to facilitate lookup by ID), place enclosure tables, to make the place tree view work, and a few others.

In theory, these tables are kept constantly up-to-date when anything changes. So rebuilding the Reference Maps and Secondary Indices should not be necessary. But, especially early on in the Gramps history, bugs sometimes interfered with updates completing correctly. So the tools remain available... ‘just in case’.

##### See also

- This rebuild is also performed as part of the

{{-}}

#### <u>Remove Unused Objects</u>

This tool will search your database for pieces of information which are not connected to anything else, and then allow you to edit and attach the information or remove them.

You can use this tool via menu .

{{-}} ![[_media/UnusedObjects-dialog-example-results-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;Unused Objects&quot; - dialog example results for &quot;Remove Unused Objects&quot; tool]]

The dialog is presented.

You can choose from the search option you want to use from the top section of the dialog:

-  (checkbox checked by default)

-  (checkbox checked by default)

-  (checkbox checked by default)

-  (checkbox checked by default)

-  (checkbox checked by default)

-  (checkbox checked by default)

-  (checkbox checked by default)

Select the button to run the tool, and once completed the results if any will show in the bottom section of the dialog with the following columns shown:

- Select the row if you want to delete the object (unchecked by default)

- \- Icon representing the type of object.

- \- Gramps internal name for the object.

- \- of the object.

To examine the object you must double-click on the row and it will show the appropriate editor for the object allowing you to edit if required.

the objects you want to delete either using the individual checkboxes or using the associated buttons:

- 

- 

- 

Once your deletion choices have been made select the button to delete the objects.

When finished you may then use the button to exit the tool. {{-}}

### Utilities

This section contains tools allowing you to perform a simple operation on a portion of data. The results can be saved in your database, but they will not modify your existing data. The following utilities are currently available in Gramps:

- [Clean input data](wiki:Gramps_6.0_Wiki_Manual_-_Tools#Clean_input_data)
- [Find database loop](wiki:Gramps_6.0_Wiki_Manual_-_Tools#Find_database_loop)
- [Media Manager](wiki:Gramps_6.0_Wiki_Manual_-_Tools#Media_Manager)
- [Not Related](wiki:Gramps_6.0_Wiki_Manual_-_Tools#Not_Related)
- [Relationship Calculator](wiki:Gramps_6.0_Wiki_Manual_-_Tools#Relationship_Calculator)
- [Verify the Data](wiki:Gramps_6.0_Wiki_Manual_-_Tools#Verify_the_Data)

#### <u>Clean input data</u>

#### <u>Remove leading and trailing spaces</u>

![[_media/CleanInputData-dialog-tool-example-dialog-51.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Clean input data]] Tool to clean leading and trailing spaces from imported or old data.  The tool searches for place names with leading or/and trailing spaces. It also looks in the first name and surname.

Leading and trailing spaces are automatically removed during name data being committed to the tree.

The tool can be triggered from the menu or Tools selector dialog

See also:

- Avoid invalid characters and leading or trailing spaces in the entry field - (added in Gramps [5.0.2](wiki:Template:Releases/5.0.2) with [PR811](https://github.com/gramps-project/gramps/pull/811))
- [New tool to suppress leading and trailing spaces.](https://github.com/gramps-project/gramps/pull/783) - (added in Gramps [5.1.0](wiki:Template:Releases/5.1.0))
- Feature request : Please remove trailing spaces on items on input (2016)
- Feature request : Trailing blanks are removed from queries in the preset filters (2011)

{{-}}

#### <u>Find database loop</u>

![[_media/FindDatabaseLoop-example-PedigreeChartView-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Pedigree chart showing loop - example]]

The utility allows you to verify if you have ancestral loops in the database. Loops in your family tree may for example show a person as both the child and ancestor of another person in Family Tree. Loops can happen accidentally during data entry, for example, when a son is linked into the family tree as his own grandfather!

Other valid loops also happen and should be kept in the family tree if verified:

- An inbreeding loop because the parents are related.
- A mating loop caused by a male who has children to genetically related females.
- An incest mating loop caused by full siblings.

{{-}} ![[_media/FindDatabaseLoop-dialog-example-results-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Find database loop - dialog - results from example family tree case]]

Use the menu and you will get a window that will display the results in a list with six columns: *Loop Group unlabeled* (`Gramps ID`, `Parent`), (`Gramps ID`, `Child`), `Family ID`.

- Loop Group unlabeled column - a number related to which loop the entries are about.
- First `Gramps ID` is a reference to the Parent.
- `Parent` (Ancestor on the image) is the person we are looking for a loop.
- Second `Gramps ID` is a reference to the Child.
- `Child` (Descendant) is the origin of the loop.
- `Family ID` is a reference to the associated family

Double clicking on a selection will open the related [Families entry](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1#Family_Editor_dialog).

To fix a pedigree loop in your family tree.

- Locate the person page of the individual whose relationship needs to be adjusted.
- First, verify that a name or vital event date was not accidentally entered incorrectly.
- If you are sure that deleting the incorrect parent-child relationship will fix the loop, proceed with the steps.

Once you have resolved any loops select to exit.

{{-}} To read more about ancestral loops see:

- [Finding Ancestral Loops : Modern Software Experience](https://www.tamurajones.net/FindingAncestralLoops.xhtml)
- [Ancestral Loops : Louis Kessler's Behold Blog](http://www.beholdgenealogy.com/blog/?p=1309)

Also see:

- [Endogamy](https://wikipedia.org/wiki/Endogamy) - From Wikipedia, the free encyclopedia
- [Cousin marriage](https://wikipedia.org/wiki/Cousin_marriage) - From Wikipedia, the free encyclopedia

##### Example ancestral loops

![[_media/FindDatabaseLoop-dialog-complex-example-results-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Find possible loop in a complex example]] ![[_media/FindDatabaseLoop-dialog-example2-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} chart showing complex example]]

In the following complex example, we have multiple ancestral loops indicated by the number in the first unlabeled column a "Loop Group" :

If we look at the second line, we have :

1.  First Gramps_ID : I0002
2.  Parent is : Father, Child2
3.  Second Gramps_ID : I0001
4.  Child is : Father, Father
5.  Family_ID is : F0000

{{-}} ![[_media/FindDatabaseLoop-dialog-example2-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Find possible loop in a complex example]]

To understand what happens :

1.  we start at \[I0002\] Father, Child2.
2.  We continue with his son \[I0003\] Father, Child3.
3.  We continue with his son : \[I0000\] Child, Child.
4.  We continue with his son : \[I0001\] Father, Father.
5.  We continue with his son : \[I0002\] Father, Child2 ==\> **HERE, we have a ancestral loop**.

{{-}}

#### <u>Media Manager</u>

The is a group of four separate tools accessed via a wizard like dialog that you can access via the menu which will show the first **[Introduction](wiki:Gramps_6.0_Wiki_Manual_-_Tools#)** dialog page.

##### Introduction

![[_media/Introduction-page-MediaManager-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Introduction - page for "Gramps Media Manager" - Tool wizard]]

A brief information on the tools abilities is shown.

From the **Introduction** page selecting the button (or using the keyboard shortcut ) you will be shown the **[Selection](wiki:Gramps_6.0_Wiki_Manual_-_Tools#Selection)** page window.

{{-}}

##### Selection

![[_media/Selection-page-MediaManager-default-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Selection - page for "Gramps Media Manager" - Tool wizard - default]]

From the **Selection** page window select from one the four options the actions you want to take and then select the button:

- (default)

- 

- 

- 

{{-}}

##### Replace substrings in the path

![[_media/ReplaceSubstringSettings-page-MediaManager-default-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Replace substring settings - page for "Gramps Media Manager" - Tool wizard - default]]

This tool allows replacing specified substring in the path of media objects with another substring. This can be useful when you move your media files from one directory to another.

Selecting this radio button will bring up a window where you can type in any string in the text field and the text field. At any time you can click on the button or the button. Clicking the button will bring up the window.

{{-}}

##### Convert paths from relative to absolute

![[_media/ConvertPathsFromRelativeToAbsolute-FinalConfirmation-page-MediaManager-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} 'Convert paths from relative to absolute':"Final Confirmation" page for "Gramps Media Manager" - Tool wizard - example]]

This tool allows converting relative media paths to the absolute ones. It does this by prepending the as given in the tab of in the section, or if that is not set, it prepends the default [User's Directory](wiki:Gramps_6.0_Wiki_Manual_-_User_Directory).

- [Absolute and relative paths](https://wikipedia.org/wiki/Path_(computing)#Absolute_and_relative_paths), From Wikipedia.
- [Absolute, relative, UNC, and URL paths](https://desktop.arcgis.com/en/arcmap/latest/tools/supplement/pathnames-explained-absolute-relative-unc-and-url.htm) ArcMap help.

{{-}}

##### Convert paths from absolute to relative

![[_media/ConvertPathsFromAbsoluteToRelative-FinalConfirmation-page-MediaManager-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} 'Convert paths from absolute to relative':"Final Confirmation" page for "Gramps Media Manager" - Tool wizard - example]]

This tool allows converting absolute media paths to a relative path. The relative path is relative to the given base path in the setting as given in the tab of in the section, or if that is not set, the user's directory is used. A relative path connects the file location to the base media path that can be changed according to your needs.

- [Absolute and relative paths](https://en.wikipedia.org/wiki/Path_(computing)#Absolute_and_relative_paths), From Wikipedia.
- [Absolute, relative, UNC, and URL paths](https://desktop.arcgis.com/en/arcmap/latest/tools/supplement/pathnames-explained-absolute-relative-unc-and-url.htm) ArcMap help.

{{-}}

##### Add images not included in database

![[_media/AddImagesNotIncludedInDatabase-FinalConfirmation-page-MediaManager-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} 'Add images not included in database':"Final Confirmation" page for "Gramps Media Manager" - Tool wizard - example]]

Check directories for images not included in database, this tool adds images in directories that are referenced by existing images in the database. You will have to import one media item from each sub directory manually. Media Manager does not include sub-directories automatically. All the directory paths shown in the tool will be searched through. {{-}}

#### <u>Not Related</u>

![[_media/NotRelatedTo-dialog-NotRelated-Tool-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}}. "Not related to '...'" - dialog - showing results for "Not Related" Tool]]

This tool will list people who are not connected to the selected active person. Connections may include linked in a chain of [references](wiki:References) or linkages created with the [link editor in Notes](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_2#Link_Editor).

You can use this tool via menu .

You will get a results dialog which shows a list of all the people that are **NOT** related to the selected person.

This list gives you:

- *Name*
- *ID*
- *Parents*
- *Tags*

From the *Name* column you can use the button and buttons to collapse or expand the grouped *Name* list. Double clicking on a person will bring up the dialog or dialog.

If you select a person, you can use the text field (you can fill in whatever custom tag name you want to use) or use the drop down list to choose an existing tag eg TODO, NotRelated. Use the to add the selected tag to the person(s). This tag will then show up in the *Tags* column. {{-}}

#### <u>Relationship Calculator</u>

![[_media/RelationshipTo-dialog-RelationshipCalculator-Tool-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;Relationship to &#39;...&#39; &quot; - dialog - showing results for &quot;Relationship Calculator&quot; Tool]] You can use this tool via menu .

Selecting the Relationship Calculator tool will open a list filtered to all people connected, **but not necessarily related**, to the [Active Person](wiki:Gramps_Glossary#active_person). To calculate relationship to different person, close the window, make that person Active and select the tool from the menu again.

Select the individual from the filtered list to report if a relationship exists. The exact relationship will be shown in the lower panel... along with the common ancestors in that relationship. Only blood relationships will display (except for husband-wife and step relationships). Note that "in-law" relationships are not displayed.

The filtered list will grouped and alphabetically sorted by surname. (Regardless of whether the View menu setting of the Person category has been set to **Grouped**.) The list columns cannot be re-sorted.

The degree of separation (generation distance) that will be recognized is controlled by the value in the [Limits](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Limits) tab under the menu. Moved from the [5.1 General](wiki:Gramps_5.1_Wiki_Manual_-_Settings#General) tab (The default of 15 generations will report a 12th great-grandparent relationship but not the 13th great-grandparents. The active person is counted as one of the generations. So, self generation plus parent plus grandparents are the other 3 generations.)

Essentially, any two people are directly related by blood if they have an ancestor in common. One of these individuals may actually be an ancestor of the other - such as a great grandparent. Even in the cases of aunts and uncles, you still can calculate the relationship by searching for the common ancestor. In this case, the father or mother of the aunt or uncle will be a grandparent to the nephew or niece.

The most basic blood relationship through common ancestors is that of siblings (brothers and sisters) who are only one generation down from the common ancestor. Another special relationship is that of one of those siblings to the descendants of the other siblings. If the Active Person is a grandchild of the common ancestor, the sibling would be an aunt or uncle. Beyond that generation of descendants, there are two equivalent ways of describing the relationship. The daughter of great grandparents might be called either a grandaunt or a great aunt. (The Relationship Calculator uses the 'grand' variant.) That person is a great grandaunt to the second great grandchildren, who are four generations distant from the common ancestor. (She may also be called a second great aunt.) The reverse relationship of an aunt or uncle is a nephew or niece.

Cousins (also called "first" cousins) are two generations down from the common ancestor through different siblings. "Second" cousins are thus, three generations down from the common ancestor - and so on.

After that, everyone is considered a "cousin", but to indicate that they are not in the same generation we use the word "removed" to indicate the number of generations different between the two. For example, my father's "first" cousin is also my "first" cousin but "once removed" (one generation difference between us). My fathers "first" cousin is my own child's "first cousin twice removed" - two generations different.

If multiple blood relationships exist due to pedigree Collapse, all will be reported.

A full text list of all blood relations and their spouses can be viewed using a [Kinship Report](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_6#Kinship_Report).

##### See also:

- The **Relationship to home person** [Display Preferences](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Display) option for the Status bar
- **Relation to Home Person** [quick view](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_8#Quick_Views).
- The **[Deep Connections](wiki:Addon:Deep_Connections_Gramplet)** gramplet: If this third party addon is installed, it will list the intervening generations through the sibling offspring of a common ancestor. (But it does not list the common ancestor or if both person a connected through the same spouse.) The Gramplet also details the indirect relationships.
- [Relationship Calculator Localization](wiki:Specification:Relationship_Calculator) - create meaningful relation descriptions in your region.

{{-}}

#### <u>Verify the Data</u>

![[_media/VerifyTheData-DataVerifyTool-dialog-General-tab-defaults-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Verify the Data..." - "Data Verify tool" dialog - "General" tab - defaults]]

This utility allows you to verify the database based on the set of criteria specified by you.

For example, you may want to make sure that nobody in your database had children at the age of 98. Based on common sense, such a record would indicate an error. However, it is not a consistency error in the database. Besides, someone might have a child at the age of 98 (although this rarely happens). The Verify tool will display everything that violates your criteria so that you can check whether the record is erroneous or not. The ultimate decision is yours.

Select this via the menu you will get a window. The window has four tabs; , , , . Those tabs show a list with criteria and a input field where you can alter the criteria value. In the lists below I show some *workable* values.

##### Verify the Data tab pages

Select the criteria you want to run the tool with from the following tabs. If you are OK with the criteria click the button (or hit the keybinding) and you will be presented with a window.

###### General

-   
  `90`

-   
  `17`

-   
  `50`

-   
  `3`

-   
  `30`

-   
  `99`

The first check box: causes the tool to accept a baptism date if a birth date is not known, and to accept a burial date if a death date is not known. It also causes the tool to accept "inexact" dates (i.e., any "legal" Gramps date which is not a fully-specified one (with an explicit day and month and year)).

The second check box: will check if the dates are invalid.

###### Women

-   
  `17`

-   
  `48`

-   
  `12`

###### Men

-   
  `18`

-   
  `65`

-   
  `15`

###### Families

-   
  `30`

-   
  `8`

-   
  `25`

{{-}}

##### Data Verification Results window

![[_media/DataVerificationResults-window-example-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Data Verification Results window.]]

After you run the tool you will be presented with the window.

Depending on your criteria and your data, a list will be shown. The possibilities of findings are listed below. (But others may be added.) Each match will be grouped with similar findings.

- Baptism before birth
- **Baptism too late according to family tradition**

  
This rule determines the median of days between birth and baptism over all children of a family. It then compares the days between the birth and the baptism of the person in question with also allowing some grace period of deviation. Currently, that grace period is hard-coded with 120 days.

- Birth equals death
- Birth equals marriage
- Burial before baptism
- Burial before birth
- Burial before death
- **Burial too late**

  
A Burial is considered “too late” when its more than 14 days after the date of death. Should this be a parameter or might this confuse the user?

- **Children are not in chronological order**

  
Birth dates (if no date exists and estimation is on, Baptism dates are used) are checked for each child of a family. Verifies that dates ascend through the list of children. Children without any of those dates are ignored

- Dead father
- Dead mother
- Death before baptism
- Death before birth
- Death equals marriage
- Disconnected individual

  
ones with no parent or spouse or child or sibling

- Early marriage

  
( General tab, default = 17 )

- **Families are not in chronological order**

  
This Rule uses the marriage date and evaluates that the families are ordered in a chronological order for a person. If no marriage date is available a divorce date or even the birth date of the oldes child of each family is used. The birth date as last possible fallback is used to account for non-married families with illegitimate children.

- **Family events not ordered in chronological order**
- **Family has events with role Unknown**
- Female husband
- Husband and wife with the same surname
- Invalid birth date

  
( General tab, default = True )

- Invalid death date

  
( General tab, default = True )

- Large age difference between spouses

  
( Families tab, default = 30 )

- Large age differences between children

  
( Families tab, default = 8 )

- **Large year span for all children**

  
( Families tab, default = 25 )

- Late marriage

  
( General tab, default = 50 )

- Male wife
- Marriage after death
- Marriage before birth
- Marriage date but not married
- Married often

  
( General tab, default = 3 )

- Multiple parents
- Old age at death
- Old age but no death

  
( General tab, default = 90 )

- Old and unmarried

  
( General tab, default = 50 )

- Old father

  
( Men tab, default = 65 )

- Old mother

  
( Women tab, default = 48 )

- **Person events not in chronological order**
- **Person has events with role Unknown**
- Same sex marriage
- Too many children

  
( Men tab, default = 15; Women tab, default = 12 )

- Unborn father
- Unborn mother
- Unknown gender
- Young father

  
( Men tab, default = 18 )

- Young mother

  
( Women tab, default = 17 )

On the bottom of the window four buttons are available to make a selection easier. Those are , , , and .

Double-clicking on a row will give you a possibility to view and or edit the data.

With the button (or select the keyboard shortcut ) you close the window. {{-}}

##### Examples

Two examples from using real data with this tool:

\*:The warning showed 'female husband': checking the data I found a family with father : Anna Roelants. Luckily in the I read: *The marriage of Adam Roelants and Cornelia Crabbe*. It was clearly a typo: Anna i.s.o. Adam. Without this **Tool** it would be very hard to find.

\*:The warning showed 'late marriage': checking the data: male person °1738 female person °1756 : marriage X 1804 \[Gregorian Calendar\] : Everything seemed to be OK: so they (re)married at the age of 66 and 48 years! The warning showed up because the **General criteria** was set to **60**.

##### See Also

- Development discussion on Gramps community support Discourse forum:

  
[Interest in enhancing verify.py](https://gramps.discourse.group/t/interest-in-enhancing-verify-py/4075/23)

{{-}}

### Debug

![[_media/MenuOverview-Tools-Debug-menu-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "" Menubar - Tools - Debug menu Overview]]

When the command line: Python option `-O` *optimise flag* is not turned on, an additional entry appears in the menu and the following tools are available:

- [Check Localized Date Displayer and Parser](wiki:Gramps_6.0_Wiki_Manual_-_Tools#Check_Localized_Date_Displayer_and_Parser)
- [Dump Gender Statistics](wiki:Gramps_6.0_Wiki_Manual_-_Tools#Dump_Gender_Statistics)
- [Generate Testcases for Persons and Families](wiki:Gramps_6.0_Wiki_Manual_-_Tools#Generate_Testcases_for_Persons_and_Families)
- [Populate Sources and Citations](wiki:Gramps_6.0_Wiki_Manual_-_Tools#Populate_Sources_and_Citations)

Also See:

- [Command Line: Python options](wiki:Gramps_6.0_Wiki_Manual_-_Command_Line#Python_options)
- [Uncollected Objects](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Uncollected_Objects) Gramplet
- [Python Evaluation](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Python_Evaluation) Gramplet

{{-}}

#### Check Localized Date Displayer and Parser

![[_media/StartDateTest-dialog-CheckLocalizedDateDisplayerAndParser-Tool-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Start date test?" dialog - for "Check Localized Date Displayer and Parser" - Tool]]

This test tool will create many people showing all different date variants as birth. The death date is created by parsing the result of the date displayer for the birth date. This way you can ensure that dates printed can be parsed back in correctly.

You will be shown the dialog to select either to exit or to start the tool. {{-}}

#### Dump Gender Statistics

![[_media/GenderStatisticsTool-dialog-DumpGenderStatistics-Tool-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Gender Statistics tool" dialog results example - for "Dump Gender Statistics" - Tool]]

The "Gender Statistics tool" dialog will show the results in list about the statistics for the gender guessing based on the persons first name.

See [Gender](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1#Gender) entry. {{-}}

#### Generate Testcases for Persons and Families

![[_media/GenerateTestcases-dialog-GenerateTestcasesForPersonsAndFamilies-Tool-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Generate testcases" dialog - for "Generate Testcases for Persons and Families" - Tool - default]]

The testcase generator will generate some persons and families that have broken links in the database or data that is in conflict to a relation.

The dialog will be shown and you can either or .

You can generate testcases that cause the following:

- 

- 

- 

- 

- 

- 

- 

<!-- -->

- `2000`(default)

Select to exit or to start the tool.

will bring you here.

- Command line usage see: [Plugins_Command_Line#Generate_Testcases_for_Persons_and_Families](wiki:Plugins_Command_Line#Generate_Testcases_for_Persons_and_Families)

{{-}}

#### Populate Sources and Citations

![[_media/PopulateSourcesAndCitationsTool-dialog-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Populate sources and citations tool" dialog - default]]

This tool generates sources and citations for each source in order to populate the database for testing with significant numbers of sources and citations.

Enter the required number and then select to run the tool:

- `2` (default)

- `2` (default)

Once the tool is complete you will be shown the alert dialog.

{{-}}

[Category:Documentation](wiki:Category:Documentation) [Category:Tools](wiki:Category:Tools) [Category:Plugins](wiki:Category:Plugins)
