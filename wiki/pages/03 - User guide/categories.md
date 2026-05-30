---
title: Gramps 6.0 Wiki Manual - Categories
categories:
- Documentation
- Pages using invalid self-closed HTML tags
- Stub
managed: false
source: wiki-scrape
wiki_revid: 129269
wiki_fetched_at: '2026-05-30T11:06:14Z'
---

{{#vardefine:chapter\|4}} {{#vardefine:figure\|0}} Genealogical information is very broad and can be extremely detailed. Displaying it poses a challenge that Gramps takes on by dividing and organizing the information into a series of Categories, each with their own Views. Each View displays a portion of the total information, selected according to a particular category. This will become clearer as we explore the different Categories.

- See the [Types of Genealogical information](https://wikipedia.org/wiki/Genealogy#Types_of_information) - entry on Wikipedia, the free encyclopedia

## Categories of the Navigator

The different Categories of the [Navigator](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window#Navigator): The navigator is located at the left of the window and allows selection of the different categories.

![[_media/Gramps-navigator-sidebar-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Navigator sidebar with Navigator mode "Category" selection Drop-Down list shown]]

-   
  Displays different general purpose Gramplets, small widgets that can help in your genealogical research.

<!-- -->

-   
  List of people in the family tree.

<!-- -->

-   
  Displays the relationships between the Active Person and other people in a textual way. This includes the parents, siblings, spouses, and children of that person.

<!-- -->

-   
  List of families in the family tree.

<!-- -->

-   
  Displays graphical trees for the selected person.

<!-- -->

-   
  List of events in the family tree.

<!-- -->

-   
  List of places in the family tree.

<!-- -->

-   
  Displays place data of your family tree on a map.

<!-- -->

-   
  List of sources in the family tree.

<!-- -->

-   
  List of citations in the family tree.

<!-- -->

-   
  List of repositories in the family tree.

<!-- -->

-   
  List of media objects in the family tree.

<!-- -->

-   
  List of notes in the family tree.

{{-}} ![[_media/Navigator-mode-selection-drop-down-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Drop-Down navigator mode showing Charts Category view modes]]

### View modes

The categories can contain several ways of presenting the data. Each specific way is called a View mode. For example:

- *view category*

  - **default view mode**

  - *alternate view mode*

  - *alternate view mode*

  - *alternate view mode*

{{-}} For each category you have a variety of ways to switch between View modes:

1.  By selecting the relevant icon from the toolbar
2.  From the menu
3.  Via the number-based [keybindings](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings#List_Views) (aka keyboard shortcuts) to *Change the view mode to correspond to number key ///../ in this view category*
4.  From the Navigator bar when the Drop-Down or Expander features are selected (See [Switching Navigator modes](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window#Switching_Navigator_modes))

{{-}} .{{#vardefineecho:figure\|{{#expr:{{#var:figure}}+1}}}} Navigator mode selection Drop-Down list. See [Switching Navigator modes](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window#Switching_Navigator_modes) \]\]

}}

{{-}} The following sections provide a brief description of each category and the view modes within.

## Dashboard Category

![[_media/gramps-gramplet.png]] ![[_media/DashboardCategory-DashboardView-default-gramplets-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Dashboard Category (Default View)]] This category contains the **Dashboard**, which shows a number of widgets, called [Gramplets](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#What_is_a_Gramplet), that can help you in your research.

Two Gramplets are shown by default on start-up (the [Top Surname](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Top_Surnames) and [Welcome to Gramps!](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Welcome) Gramplets) in a two column configuration; changeable in the [Gramplet layout](wiki:Gramps_6.0_Wiki_Manual_-_Categories#Gramplet_Layout_tab) tab. The Sidebar and Bottombar are not available on the Dashboard.

On the Dashboard you can:

- Click on a gramplets to rename it.

- \- and rearrange the Gramplets.

  - Closing a detached gramplet returns it to the Dashboard.

- \- the Gramplet.

- \- when attached.

See [Gramps_6.0_Wiki_Manual_-_Gramplets#The_Dashboard_Category_View](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#The_Dashboard_Category_View)

You can change the Gramplets on the Dashboard by using the context menu (right-clicking) on an empty area of the Dashboard View. This will show a pop-up menu to , populated with a list of the possible Gramplets you may add and use with this particular view. (Some Gramplets are only available in particular category views.) It is better to have a Family Tree open when changing out Gramplets. The added feedback of some tree data in the Gramplets will help make choices about configuring the layout.

- Gramplet - list the people alive and their ages on a particular date

- Gramplet - list age span statistics in a number of graphs

- Gramplet - see people's events on a particular date, or in a month in the past

- \- Frequently asked questions about Gramps.

- Gramplet - most popular given names

- \- run a Quick View on the current person

- \- see world's records of your data

- Gramplet - keep track of what you have done, and what records you have visited

- generates [SoundEx codes](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Soundex) for the names of people in the database.

- Gramplet - see stats on the database

- Gramplet - most popular surnames as a "text cloud"

- Gramplet - a notepad to keep tabs on your research

- Gramplet - top 10 most popular surnames *(default)*

- Gramplet - a Gramps welcome message *(default)*

- Gramplet - what needs to be done next

In addition, there are a number of Third-party Gramplets that you can easily install and use. These include:

- \- current, breaking news from Gramps

- \- edit active person's name, birth date and place, death date and place, and add people

- \- a Python shell

- \- see and edit active person's primary Person Note

and many others. See [Third-party Addons](wiki:Third-party_Addons) for more details.

For more detailed information on using the installed Gramplets, see [Gramplets](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets).

{{-}}

### Dashboard context menu

![[_media/DashboardCategory-context-menu-default-gramplets-list-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Dashboard Category View - Showing Dashboards context menu "Add a gramplet"s default gramplet list. With no gramplets on Dashboard]]

The Dashboard context menu shown when right-clicking on an empty area of the Dashboard View, allows you to add or restore gramplets.

Dashboard views drop-down menu shows the and options. A similar drop-down menu is also available from the [Gramplet Bar Menu](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window#Gramplet_Bar_Menu) available on the Bottombar and Sidebar of other Category views.

#### 

Shows a list of gramplets that can be installed on the Dashboard view.

#### 

Shows a list of gramplets that have been removed during that session of Gramps that can be restored. {{-}}

### ⚙ Dashboard Category Configuration Options

![[_media/ConfigureTheActiveView-icon-on-toolbar-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}}  button]] If any of the displayed Gramplets on the Dashboard have configuration options then those options will be shown on the related tabs, click the ![[_media/Gramps-config.png]] button. Alternatively, you can choose from the menu.

{{-}}

#### Gramplet Layout tab

![[_media/ConfigureDashboard-GrampletLayout-tab-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Configure Dashboard - Gramplet Layout - tab - default]] On the tab you can change the number of columns shown for Gramplets.

- `2` (default)

{{-}}

## People Category

![[_media/PeopleCategory-Toolbar-partial-overview-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} People Category - Toolbar People View Options.]]

![[_media/gramps-person.png]] ![[_media/Menubar-View-overview-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} View menu for the People category - People Tree view mode]] In the the *by surname* (default) or views display a list of all people in the family tree without their connections. From this view, you may add, edit, remove, export column data, or merge people. Each view (Grouped or List) display several columns of information about each person.

Additional options are available by selecting a person from the list and using the pop-up [context menu](wiki:Gramps_Glossary#context_menu) shown by right-clicking. {{-}}

### Tree View - Grouped People

![[_media/PeopleTreeView-GroupedPeople-example-with-context-menu-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "People Category" - "People Tree View" - "Grouped People" list showing context menu]]

People are grouped according to their family names (also known as a surname or last name). To the left of each collapsed family name is typically either an arrow or some other type of indicator (e.g., ). Clicking it once will reveal the entire list of people sharing that name. Clicking the indicator again will "roll up" the list and show only the family name.

Additional options are available by selecting a person from the grouped list and using the pop-up shown by right-clicking.

#### Grouped People context menu

Additional options are available by selecting a person from the grouped list and using the pop-up [context menu](wiki:Gramps_Glossary#context_menu) shown by right-clicking:

<hr>

- 

- 

- 

- 

<hr>

- 

- 

<hr>

- 

- 

- 

- 

- - 

  - 

  - 

  - 

  - 

  - 

  - 

  - 

<hr>

{{-}}

### People List View

<span id="Tree View - People List View"/>

![[_media/PersonView-PeopleListView-example-with-context-menu-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "People" Category - "Person" (List) View - showing context menu]]

List of all the people in the database, sorted by first column which by default is the column.

Additional options are available by selecting a person from the list and using the shown by right-clicking.

#### People List View context menu

Additional options are available by selecting a person from the list and using the context/pop-up menu shown by right-clicking:

<hr>

- 

- 

- 

- 

<hr>

- 

- 

- 

- 

- - 

  - 

  - 

  - 

  - 

  - 

  - 

  - 

<hr>

{{-}}

{{#vardefine:viewmode\|People category}} tab, tabs. The People view also defaults to showing the [Sidebar](#People_Category_Sidebar) tabs and [Bottombar](#People_Category_Bottombar_tabs). None of the default sidebar gramplets (see [Details](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Details), [Gallery](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Gallery), [Events](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Events), [Children](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Children), [Citations](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Citations), [Notes](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Notes), [Attributes](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Attributes), [References](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#References)) or sidebar gramplets (see [Filter](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#People_Filter)) have Configurable options.

##### {{#var:viewmode}} Columns

![[_media/ColumnsEditorTab-dialog-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} <strong>Columns</strong> editor tab - dialog - People Tree View default columns]]

By default, the tabular {{#var:viewmode}} view modes will display the columns selected in the Configuration Options with a row for each Person. Additional columns may be selected in the Configuration Options dialog. Configuration changes appear when the button is clicked.

The available columns for display are:

-  (**required** 1st column for the Grouped People view mode. So it is not shown as a configurable option)

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

- 

- 

- 

See also

- [Using the People Category](wiki:Gramps_6.0_Wiki_Manual_-_Navigation#Using_the_People_Category)
- [Editing information about people](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1#Editing_information_about_people)

{{-}}

### People Category Bottombar tabs

Both Tree Views (Grouped People/People List View) have the following [Bottombar](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window#Bottombar_and_Sidebar) tabs. The configuration is independent between modes. {{-}}

#### Details

See [Details](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Details) Gramplet {{-}}

#### Gallery

See [Gallery](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Gallery) Gramplet {{-}}

#### Events

See [Events](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Events) Gramplet {{-}}

#### Children

See [Children](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Children) Gramplet {{-}}

#### Citations

See [Citations](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Citations) Gramplet {{-}}

#### Notes

See [Notes](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Notes) Gramplet {{-}}

#### Attributes

See [Attributes](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Attributes) Gramplet {{-}}

#### References

See [References](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#References) Gramplet {{-}}

### People Category Sidebar tabs

Both Tree Views (Grouped People/People List View) have the following [Sidebar](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window#Bottombar_and_Sidebar) tab by default. The configuration is independent between modes. {{-}}

#### Filter

See [Filter](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Filter) Gramplet {{-}}

## Relationships Category

![[_media/gramps-relation.png]] ![[_media/Relationships-category-view-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Relationships Category view]]

The Relationships Category shows the default which displays all the relationships of the Active Person (the selected person). Specifically, it shows the parents, siblings, spouses, and children of that person.

The Relationships Category is designed to allow for quick navigation. You can quickly change the Active Person simply by clicking the name of any person listed on the page. Each name is actually a [hypertext link](http://en.wikipedia.org/wiki/Hyperlink), similar to a web page.

The name of the Active Person is in **bold** style and is not underlined. Other names are shown <u>underlined</u> either with or without ***bold and italic*** emphasis depending on whether certain relationships exist for the named person. For a person listed as a parent or spouse of the Active Person, the name is emphasized if that person has a parent family. For a person listed as a sibling or child of the Active Person, the name is emphasized if that person has children.

Dates are normally in regular style, and in *italic* style if the displayed event is a fallback event, i.e., a substitute event for another missing event. That may be christening event for birth event, burial event for death event, etc. {{-}}

### Relationships Category view

![[_media/Relationships-category-view-toolbar-detail-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Toolbar section - Relationships Category view]]

For the Relationships Category views via the menu or toolbar you may select:

- or the icon - opens the

- or the icon - to create a new family with the Active Person listed as a child.

- or the icon - which opens the allowing you to choose from a list of existing families, and then add the person as a child to that family.

- or the icon - to open a new dialog with the Active Person listed as one of the partners.

- or the icon - to open the dialog.

{{-}} ![[_media/Relationships-category-view-sections-collapsed-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Relationships Category View - example (all sections collapsed)]]

The following sections are available:

- Top section shows the [Active Person](wiki:Gramps_6.0_Wiki_Manual_-_Categories#Active_Person_section)
- [Parents](wiki:Gramps_6.0_Wiki_Manual_-_Categories#Parents)
  - [Siblings](wiki:Gramps_6.0_Wiki_Manual_-_Categories#Siblings)
- [Family](wiki:Gramps_6.0_Wiki_Manual_-_Categories#Family)
  - [Spouse](wiki:Gramps_6.0_Wiki_Manual_-_Categories#Spouse)
  - [Children](wiki:Gramps_6.0_Wiki_Manual_-_Categories#Children)

You can collapse or expand the sections by selecting the arrows. {{-}}

#### Active Person section

Starting at the top of this section:

- The *Active Person*'s name is displayed, along with a symbol indicating gender,
  - The button opens the dialog so you can edit all of the Active person's individual information. Pressing on the keyboard together also opens the dialog.

Below that you are shown information on active persons:

- Gramps

- 

- - 

You will also be shown the calculated age if and final age if deceased.

The and areas are text fields that can be highlight and copied.

On the right hand side of this area if available:

- A photo of the active person will be shown. This photo shows the first image available in the tab of this person (if any exist). You can click on the photo to open it in the default picture viewer. (See also [Missing Media Objects 'broken link' icon of a box with a red 'x'](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Missing_Media_Objects_.27broken_link.27_icon_of_a_box_with_a_red_.27x.27) )

See also:

- [Setting the Active Person](wiki:Gramps_6.0_Wiki_Manual_-_Navigation#Setting_the_Active_Person)
- [Using the Relationships Category](wiki:Gramps_6.0_Wiki_Manual_-_Navigation#Using_the_Relationships_Category)
- [Genealogical Symbols](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Genealogical_Symbols)

#### Parents

The Parents section, displays the families in which the person is a child. Since it is possible for a person to have multiple sets of parents ([biological and non-biological](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1#Child_Reference_Editor)), it is possible to have several Parents sections.

You may edit an existing parents by selecting the button next to the parents. If you select the button next to a set of parents, then the Active Person will be removed as a child from the parents. This button does not delete the parents' relationship.

When you collapse the sections by selecting the arrow only the parents names are shown along with a total count of the siblings.

See the section to configure what details to show or hide etc...

##### Select Family selector

![[_media/SelectFamily-SelectorDialog-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Select Family - selector dialog example]]

The selector dialog allows you to link to an already existing Family.

The following columns are shown: `ID` (default sort for list), `Father`, `Mother`, `Last Change`.

You may use the button to filter the list based on one of the options from the drop down list:

- **ID contains** (default)
- *ID does not contain*
- *Father contains*
- *Father does not contain*
- *Mother contains*
- *Mother does not contain*
- *Last Change contains*
- *Last Change does not contain*

Use the button to clear the search field.

Note on some reports the list is restricted until you select the check box. {{-}}

##### Siblings

The Sibling section shows brothers and sisters of the Active Person plus the Active Person themself. {{-}}

#### Family

Similar to the Parents section is the Family section, which displays families where the Active Person is a parent. Because it is possible for a Person to have been a partner in multiple families, Gramps allows multiple Family sections to describe that. Each family section displays the spouse and any children. Children who were biological offspring of both partners in one Family might be a stepchild or adopted child for one partner of a subsequently formed family.

You may add a family by selecting the button in the toolbar. This will create a new family with the Active Person listed as a father or mother.

Selecting the button next to the spouse will allow you to edit the displayed family.

Clicking the button will remove the person from the displayed family.

When you collapse the section by selecting the arrow only the spouses names are shown along with a total count of the children from that spouse.

{{-}}

{{-}}

###### Reorder Relationships dialog

![[_media/ReorderRelationships-dialog-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Reorder Relationships" - dialog - example]]

Select the button to display the dialog that will allow you to reorder the parents and families. The topmost entry in each of the sections is considered the primary entry and is used for charts, graphs and summaries.

When more than one set of parents or more than one set of spouses exists for the Active Person.

Select one of the following:

- the menu
- or the toolbar icon button
- or the icon near the label
- or the icon near the label

to display the dialog that will allow you to reorder:

Parent relationships  

- the parents order in the top section using the / arrow buttons.
  - The topmost set of parents are considered the Primary parents and are used for charts, graphs and summaries.

Family relationships  

- or families order in the bottom section using the / arrow buttons.
  - The topmost family is considered the Primary family and is the family used for charts, graphs and summaries.

{{-}}

##### Children

Shows the Active persons children. You are also able to add new or add existing children to the family. {{-}}

#### ⚙ Relationships Category Configuration Options

![[_media/Gramps-config.png]] button in the [Toolbar](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window#Toolbar) is clicked to customize options specific to the current view mode. (As opposed to [](wiki:Gramps_6.0_Wiki_Manual_-_Settings) options that customize all views.) Alternatively, use the menu or press the *Configure active view* [keyboard keybinding](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings#Common_keybindings).

The following options are available: {{-}}

##### Content

![[_media/ConfigureRelationshipsView-Content-tab-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Configure Relationships Category - Content (tab) defaults]]

- On the tab
  -  (checkbox checked by default) show or hide the birth and death information (All except the Active person)

  -  (checkbox checked by default) show or hide siblings.

{{-}}

##### Layout

![[_media/ConfigureRelationshipsView-Layout-tab-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Configure Relationships Category - Layout (tab) defaults]]

- On the tab
  -  (checkbox checked by default)

  -  (checkbox checked by default) - show or hide the button shown next to each person.

  -  (checkbox unchecked by default) - Non active peoples names are displayed as <span style="color:#0000ff">blue text</span> with no underline.

{{-}}

### Relationships Category Bottombar tabs

The by default displays no Gramplets in the [Bottombar](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window#Bottombar_and_Sidebar) tab. You may add them as required. {{-}}

### Relationships Category Sidebar tabs

The by default displays no Gramplets in the [Sidebar](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window#Bottombar_and_Sidebar) tab. You may add them as required. {{-}}

## Families Category

![[_media/gramps-family.png]] ![[_media/Families-category-list-view-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;Families&quot; Category - (List) View - showing context menu and &quot;Children&quot; tab in the bottombar]]

In the the displays a list of all families in the family tree (see Fig. {{#var:chapter}}.{{#var:figure}}).

From this view, you may use buttons on the toolbar to:

- 

- 

- 

- ![[_media/Gramps_Merge48x48_win.png]] from the list ( you can only select and merge two(2) families at a time. )

- ![[_media/16x16-gramps-tag.png]]

The default display lists the `ID, Father, Mother, Relationship and Marriage Date`. If you configure the active view you can, hide existing columns, show additional columns like `Private, Tags, Last Changed`, or rearrange the column order.

#### Families Category context menu

Additional options are available by selecting a family from the list and using the context/pop-up menu shown by right-clicking:

<hr>

- 

- 

<hr>

- 

- 

- 

- 

<hr>

- 

- 

<hr>

- - 

  - 

<hr>

See also

- [Using the Families Category](wiki:Gramps_6.0_Wiki_Manual_-_Navigation#Using_the_Families_Category)
- [Editing information about relationships](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1#Editing_information_about_relationships)

{{-}}

#### ⚙ Families Category Configuration Options

![[_media/Gramps-config.png]] button in the [Toolbar](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window#Toolbar) is clicked to customize options specific to the current view mode. (As opposed to [](wiki:Gramps_6.0_Wiki_Manual_-_Settings) options that customize all views.) Alternatively, use the menu or press the *Configure active view* [keyboard keybinding](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings#Common_keybindings).

The following two tabs are shown:

- Columns
- CSV Dialect

{{-}}

##### Columns

![[_media/FamiliesCategory-FamiliesView-Configure-dialog-Columns-defaults-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Families Category - Families View - Configure the active view - dialog - showing Defaults on Columns tab]]

As with most list style Views, the layout configuration tab allows customization of which columns will be displayed and their order of display.

The displayable columns include:

The available columns for display are:

- 

- 

- 

- 

- 

- 

- 

- 

{{-}}

##### CSV Dialect

On the [CSV Dialect tab](wiki:Gramps_6.0_Wiki_Manual_-_Settings#CSV_Dialect) you can choose the CSV format for the delimiter to be used when [exporting this list view](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Export_View).

{{-}}

### Families Category Bottombar tabs

The shows the following [Bottombar](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window#Bottombar_and_Sidebar) tabs as default. {{-}}

#### Gallery

See [Gallery](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Gallery) Gramplet {{-}}

#### Events

See [Events](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Events) Gramplet {{-}}

#### Children

See [Children](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Children) Gramplet {{-}}

#### Citations

See [Citations](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Citations) Gramplet {{-}}

#### Notes

See [Notes](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Notes) Gramplet {{-}}

#### Attributes

See [Attributes](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Attributes) Gramplet {{-}}

#### References

See [References](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#References) Gramplet {{-}}

### Families Category Sidebar tabs

The shows the following [Sidebar](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window#Bottombar_and_Sidebar) tabs as default. {{-}}

#### Filter

See [Filter](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Filter) Gramplet {{-}}

## Charts Category

![[_media/ChartsCategory-Toolbar-partial-overview-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Charts Category - Toolbar Chart View Options]]

![[_media/gramps.png]] The Category shows several graphical representations of the ancestry or descendants of the active person.

By default Gramps shows the View. With the View and chart View and chart view being selectable from the toolbar or menu via

### Pedigree View

![[_media/ChartsCategory-Pedigree-view1-horizontal-right-standard-5gen-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Pedigree" view (Default) Tree direction: Horizontal (→) (horizontal to right) with person tooltip shown]]

The View shows up to nine generations in the form of a chart, depending on the size of the window you may need to use the scroll bars to see parts of the chart.

Each person is indicated by a box labeled with his or her name, birth information (indicated by an asterisk `*` sign), death information (indicated by a plus `+` sign), a black stripe across the top left corner of the box is shown if the person is deceased (or determined by Gramps to be no longer alive) and optionally the primary image will be displayed if available.

If you hover the mouse cursor over any of person boxes or marriage nodes you will be shown a tooltip.

Two lines branch from each person box. The top line leads to the person's father and the bottom line leads to the mother. Solid lines represent the biological birth type relationship, while dashed lines represent non-birth relationships such as adoption, step-parenthood, guardianship, etc.

The left arrow button beside the Active Person is a only selectable if the Active Person has children, clicking this button expands to show a list of the Active Person's children. Selecting one of the children makes that child the Active Person for the chart.

The appearance of the children's names in the menu differentiates the dead ends of the tree from the continuing branches.

Children who have children themselves appear in the menu in the boldface and italic type, while children without children (dead ends) appear in a regular font. If the Active Person has only one child, no menu will be displayed (since there is only one choice) and the child will become the Active Person when the arrow button is clicked.

The right-hand side of the window shows two right arrow buttons. When the top button is clicked, the Father of the Active Person becomes the Active Person. When the bottom button is clicked, the Mother of the Active Person becomes the Active Person.

{{-}}

#### Pedigree View Context menus

##### Pedigree View Person Context menu

![[_media/ChartsCategory-PedigreeView-PersonContextMenu-showing-Children-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Pedigree View "Person context menu" showing Children]]

Right-clicking on any person's box in the Pedigree View will bring up the Person "context menu".

Among other useful items, the context menu has sub-menus listing , , and

In addition, there is a submenu for people to that person. These are people who share an Event with the Person.

"Greyed-out" sub-menus indicate the absence of the data in the appropriate category. Similar to the children menu above, Childrens' and Parents' menus distinguish continuing lines from dead ends.

The button will bring you to this page for help.

Context menu entries:

<hr>

- 

- 

- 

- \>

- \>

- \>

- \>

- \>

<hr>

- 

- 

- 

- 

<hr>

- \>

  - 

  - 

<hr>

- 

<hr>

##### Pedigree View Blank Context menu

![[_media/ChartsCategory-PedigreeView-BlankAreaContextMenu-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Pedigree View "Blank (area) context menu" overview]]

Right-clicking on an empty area of the Pedigree view will bring up the same Person "context menu" but with limited choices. {{-}} <span id="Configure the active view">

#### ⚙ Configuration Options

</span> ![[_media/ChartsCategory-PedigreeView-ConfigureCharts-dialog-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Charts Category - Pedigree View - Configure the active view - dialog - showing Defaults on Layout tab]] ![[_media/Gramps-config.png]] button in the [Toolbar](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window#Toolbar) is clicked to customize options specific to the current view mode. (As opposed to [](wiki:Gramps_6.0_Wiki_Manual_-_Settings) options that customize all views.) Alternatively, use the menu or press the *Configure active view* [keyboard keybinding](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings#Common_keybindings).

##### Layout

The View tab has the following option available:

-  (checked by default)

-  (checked by default)

-  (checked by default)

-  (unchecked by default)

- - **Standard**(default)
  - Compact
  - Expanded

- - Vertical (↑) ![[_media/ChartsCategory-pedigreeview2-vertical-up-standard-5gen-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Pedigree view 1 - Tree direction: Vertical (↑) (vertical and up)]] (See Fig. {{#var:chapter}}.{{#expr:{{#var:figure}}}})
  - Vertical (↓) ![[_media/ChartsCategory-pedigreeview2-vertical-down-standard-5gen-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Pedigree view 2 - Tree direction: Vertical (↓) (vertical and down)]] (See Fig. {{#var:chapter}}.{{#expr:{{#var:figure}}}})
  - **Horizontal (→)**(default) ![[_media/ChartsCategory-Pedigree-view1-horizontal-right-standard-5gen-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;Pedigree&quot; view (Default) Tree direction: Horizontal (→) (horizontal to right) with person tooltip shown]] (See Fig. {{#var:chapter}}.{{#expr:{{#var:figure}}}})
  - Horizontal (←) ![[_media/ChartsCategory-pedigreeview2-horizontal-left-standard-5gen-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Pedigree view 4 - Tree direction: Horizontal (←) (horizontal to left)]] (See Fig. {{#var:chapter}}.{{#expr:{{#var:figure}}}})

- slider range 2 to 9 generations. Set to `5`(by default)

{{-}}

### Fan Chart View

![[_media/ChartsCategory-fanchartview-halfcircle-7gen-Royals-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Fan Chart View - half circle (Royals92.ged)]]

The view shows the active persons ancestry as a pie chart. Clicking on a name in the chart will double the section of the pie allocated to that person by collapsing the spouse section. A second click brings the chart back to the original form. Right-click brings up a context menu like in the pedigree view, allowing to navigate to other people.

This view enables to see large ancestries in a more compact manner, and to see very quickly which parts of an ancestry need further research.

You can rotate the view by click and drag outside the fan chart. You can move the view by click and drag inside the inner (white) region.

- The view can be a circle, a halfcircle or a quadrant of a circle. The latter are always attached to the bottom or side of the view
- Children of the center person are shown within the ring at the center
- Drag and drop people to the center to change the active person
- Color options
  - Colors of the boxes based on the age of the people
  - Colors of the boxes depending on the time period the person lived in
  - White, classic, gender based, and user defined colors
- Filtering: use the person filter in the sidebar to quickly obtain insight in the people shown. For example: which people have birth events, who has the attribute *blue eyes*, ... . Filtered results have bold font, the ones that don’t satisfy the filter are shown transparent
- Show up to 11 generations in the view.
- Print the view from the toolbar. The view as you see it (after rotating, expanding, changing color) can via the button. The view can be printed or use the Print to File option to save in any of the following formats: SVG (which can be edit further in tools like Inkscape or viewed in browsers like Firefox), PostScript (.ps) or PDF.
- The font used can be selected and automatically adjust to fit within the boxes. On a darker background, the font is white, and vice versa.

{{-}}

##### Fan Chart View context menu

Context menu entries:

<hr>

- 

- 

- 

- \>

- \>

- \>

- \>

- \>

- \>

<hr>

{{-}} <span id="Configure the active view">

#### ⚙ Configuration Options

</span> ![[_media/ChartsCategory-FanChartView-ConfigureCharts-dialog-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Charts Category - Fan Chart View - Configure the active view - dialog - showing Defaults Defaults on Layout tab]] ![[_media/Gramps-config.png]] button in the [Toolbar](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window#Toolbar) is clicked to customize options specific to the current view mode. (As opposed to [](wiki:Gramps_6.0_Wiki_Manual_-_Settings) options that customize all views.) Alternatively, use the menu or press the *Configure active view* [keyboard keybinding](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings#Common_keybindings).

##### Layout

- *9* (default)

- *Sans* (default)

- - Gender colors
  - **Generation based gradient** (default)
  - Age (0-100) based gradient
  - Single main (filter) color
  - Time period based gradient
  - White
  - Color scheme classic report
  - Color scheme classic view

- *\#ef2929* (default)

- *\#3d37e9* (default)

- - **Full Circle** (default)
  - Half Circle
  - Quadrant

- 

- 

- 

- 

#### See also

{{-}}

### Descendant Fan View

![[_media/ChartsCategory-DescendantFanChart-fullcircle-9gen-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Descendant Fan Chart View - full circle - showing context menu]] The view interactively displays the active person's descendants in a pie chart format. The Descendant Fan provides a comprehensive and visually appealing way to explore and analyze an individual's descendants within your family tree.

Clicking on a name in the chart collapses the sibling sections of the pie chart, while a second click reverts the chart to its original form. Right-clicking brings up a context menu similar to the pedigree view, allowing navigation to other individuals. The center Active Person's parents are shown within the innermost ring

This view enables users to visualize large descendant trees more compactly and quickly identify areas that require further research.

Key Features:

- Tooltips appear (with the person's Name, birth and death information) after a slight delay when indicating a Fan segment
- Drag and drop individuals to the center to change the active person (or [Navigate the Active Person](wiki:Gramps_6.0_Wiki_Manual_-_Navigation#Setting_the_Active_Person) using the standard methods)
- Clicking on a descendant name in the chart collapses (or expands) the sibling sections
- Rotate the view by clicking and dragging outside the fan chart or inside the inner (white) region
- Drag the center black dot to move the center focus in the main view area
- Move the center focus horizontally by dragging the bottom scrollbar.
- Move the center focus vertically by dragging the right hand scrollbar or scrolling the mouse wheel.
- Surnames appear in bold font
- Display up to 16 generations
- Adjustable font selection with automatic sizing to fit within boxes

The Filter gramplet, configuration options and Dark Variants (of the [Themes addon](wiki:Addon:ThemePreferences) for Preferences) can be used to adjust the way data is rendered.

Use the person filter in the sidebar for quick insights (e.g., individuals with birth events, specific attributes). Filtered results are in full saturation color while the non-matching entry colors are semi-transparent.

#### Descendant Fan View context menu

Right-clicking brings up a context menu similar to the pedigree view, allowing navigation to other individuals.

#### Printing

Use the button on the views toolbar, output will include any rotations, expansions, or color changes. Use the Print to File option to save in various formats:

- SVG (editable in tools like Inkscape or viewable in browsers)
- PostScript (.ps)
- PDF

{{-}} <span id="Configure the active view">

#### ⚙ Configuration Options

</span> ![[_media/ChartsCategory-DescendantFanChartView-ConfigureCharts-dialog-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Charts Category - Descendant Fan Chart View - Configure the active view - dialog - showing Defaults on Layout tab]] ![[_media/Gramps-config.png]] button in the [Toolbar](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window#Toolbar) is clicked to customize options specific to the current view mode. (As opposed to [](wiki:Gramps_6.0_Wiki_Manual_-_Settings) options that customize all views.) Alternatively, use the menu or press the *Configure active view* [keyboard keybinding](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings#Common_keybindings).

##### Layout

- *9* (default)

- *Sans* (default)

- - Gender colors
  - **Generation based gradient** (default)
  - Age (0-100) based gradient
  - Single main (filter) color
  - Time period based gradient
  - White
  - Color scheme classic report
  - Color scheme classic view

- *\#ef2929* (default)

- *\#3d37e9* (default)

- - **Full Circle** (default)
  - Half Circle
  - Quadrant

- - Homogeneous children distribution
  - **Size proportional to number of descendants** (default)

- 

- 

- 

#### See also

- [Descendant Fan View](https://gramps-project.org/blog/2012/09/descendant-fanchart/) (blog announcement)

- 

{{-}}

### 2-Way Fan View

![[_media/ChartsCategory-2-WayFan-fullcircle-ances4gen-descen4gen-example-defaults-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} 2-Way Fan Chart View - 4 Generations of Ancestors (Top) / 4 Generations of Descendants (bottom) showing context menu]]

The View interactively displays the active person's ancestors and descendants in a pie chart format. The Descendant Fan provides a comprehensive and visually appealing way to explore and analyze an individual's descendants within your family tree.

Clicking on a ancestor name in the chart collapses their spouse section of the pie, while a second click reverts the chart to its original form. Clicking on a descendant name in the chart collapses that person's sibling sections, while a second click reverts the chart to its original form. Right-clicking brings up a context menu similar to the pedigree view, allowing navigation to other individuals. The center Active Person's parents are shown within the innermost ring

This view enables users to visualize large descendant trees more compactly and quickly identify areas that require further research.

Key Features:

- Tooltips appear (with the person's Name, birth and death information) after a slight delay when indicating a Fan segment
- Drag and drop individuals to the center to change the active person (or [Navigate the Active Person](wiki:Gramps_6.0_Wiki_Manual_-_Navigation#Setting_the_Active_Person) using the standard methods)
- Clicking on a descendant name in the chart collapses (or expands) the sibling sections
- Rotate the view by clicking and dragging outside the fan chart or inside the inner (white) region
- Drag the center black dot to move the center focus in the main view area
- Move the center focus horizontally by dragging the bottom scrollbar.
- Move the center focus vertically by dragging the right hand scrollbar or scrolling the mouse wheel.
- Surnames appear in bold font
- Configurable to display up to 11 generations of ancestors
- Configurable to display up to 11 generations of descendants
- Adjustable font selection with automatic sizing to fit within boxes

The Filter gramplet, configuration options and Dark Variants (of the Themes addon for Preferences) can be used to adjust the way data is rendered.

Use the person filter in the sidebar for quick insights (e.g., individuals with birth events, specific attributes). Filtered results are in full saturation color while the non-matching entry colors are semi-transparent.

#### Printing

Print the view from the toolbar, including any rotations, expansions, or color changes. Use the Print to File option to save in various formats:

- SVG (editable in tools like Inkscape or viewable in browsers)
- PostScript (.ps)
- PDF

{{-}}

##### 2-Way Fan View Person Context menu

{{-}} <span id="Configure the active view">

#### ⚙ Configuration Options

</span> ![[_media/ChartsCategory-2-WayFanChartView-ConfigureCharts-dialog-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Charts Category - 2-Way Fan Chart View - Configure the active view - dialog - showing Defaults on Layout tab]] ![[_media/Gramps-config.png]] button in the [Toolbar](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window#Toolbar) is clicked to customize options specific to the current view mode. (As opposed to [](wiki:Gramps_6.0_Wiki_Manual_-_Settings) options that customize all views.) Alternatively, use the menu or press the *Configure active view* [keyboard keybinding](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings#Common_keybindings).

##### Layout

- *4* (default)

- *4* (default)

- *Sans* (default)

- - Gender colors
  - **Generation based gradient** (default)
  - Age (0-100) based gradient
  - Single main (filter) color
  - Time period based gradient
  - White
  - Color scheme classic report
  - Color scheme classic view

- 

- *\#ef2929* (default)

- *\#3d37e9* (default)

- *\#888a85* (default)

- - Homogeneous children distribution
  - **Size proportional to number of descendants** (default)

- 

- 

- 

#### See also

- [Feature: Gep-030 FanChart2Way](https://github.com/gramps-project/gramps/pull/222)

{{-}}

### Charts Category Bottombar tabs

The by default displays no Gramplets in the [Bottombar](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window#Bottombar_and_Sidebar) tab. You may add them as required. {{-}}

### Charts Category Sidebar tabs

The shows the following [Sidebar](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window#Bottombar_and_Sidebar) tabs. {{-}}

#### Filter

The Filter is shown by default in all Chart views except *Pedigree View*

See [Filter](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Filter) Gramplet {{-}}

## Events Category

![[_media/gramps-event.png]] The shows the that lists the all the events recorded in the Family Tree.

When first created, an Event is expected to be about an incident (or fact) for a specific (Primary) Person or Family. The details of the Event record the categorization of the Event, the date (which can be exact date or a span of dates) and Place where it occurred, and often includes a brief description when the categorization is broad. (A "Birth" category is often specific enough to not require a description. But an Occupation "Event" is almost meaningless without a description containing the specific type of vocation.)

Events can be shared between multiple people and multiple families. Each person or family may have had a different Role in shared events.

See also:

- [Editing information about events](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_2#Editing_information_about_events)

{{-}}

### Events View

![[_media/EventsCategory-EventsListView-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Events Category - Events (List) View - example with context menu]]

Displays a list of Events, that from the toolbar you can add, edit, delete, merge and tag.

- \- using the

- \- in the

- \-

- \-

- \-

  - \-

  - \-

From the list the following default columns are shown: `Description` , `ID`, `Type` , `Date` and `Place` of the event. The dialog can be used to add, remove and rearrange the displayed columns. This can be accessed from the button on the toolbar.

The list of Events can be sorted in the usual manner, by clicking on the column heading. Clicking once sorts in ascending order, clicking again sorts in descending order.

You can [Export the view](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Export_View) to a **CSV** file (default) or **OpenDocument Spreadsheet** (ODS).

#### Events View Context menu

Additional options are available by selecting an event from the list and using the context/pop-up menu shown by right-clicking:

<hr>

- 

- 

<hr>

- 

- 

- 

- 

<hr>

- - 

  - 

<hr>

#### ⚙ Events Category Configuration Options

![[_media/EventsCategory-EventsView-Configure-dialog-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Events Category - Events list View - Configure the active view - dialog - showing Defaults on Column tab]] ![[_media/Gramps-config.png]] button in the [Toolbar](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window#Toolbar) is clicked to customize options specific to the current view mode. (As opposed to [](wiki:Gramps_6.0_Wiki_Manual_-_Settings) options that customize all views.) Alternatively, use the menu or press the *Configure active view* [keyboard keybinding](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings#Common_keybindings).

##### Columns

As with most list style Views, the layout configuration tab allows customization of which columns will be displayed and their order of display.

The displayable columns include:

- 

- 

- 

- 

- 

- 

- 

- 

- 

Drag and drop columns to change their order in the Event list. The view will not be changed unless the button is clicked. Clicking without first clicking will abandon the changes.

{{-}}

##### CSV Dialect

On the [CSV Dialect tab](wiki:Gramps_6.0_Wiki_Manual_-_Settings#CSV_Dialect) you can choose the CSV format for the delimiter to be used when [exporting this list view](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Export_View).

{{-}}

### Events Category Bottombar tabs

The shows the following [Bottombar](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window#Bottombar_and_Sidebar) tabs. {{-}}

#### Gallery

See [Gallery](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Gallery) Gramplet {{-}}

#### Citations

See [Citations](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Citations) Gramplet {{-}}

#### Notes

See [Notes](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Notes) Gramplet {{-}}

#### Attributes

See [Attributes](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Attributes) Gramplet {{-}}

#### References

See [References](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#References) Gramplet {{-}}

### Events Category Sidebar tabs

The shows the following [Sidebar](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window#Bottombar_and_Sidebar) tabs. {{-}}

#### Filter

See [Filter](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Filter) Gramplet {{-}}

## Places Category

![[_media/PlacesCategory-Toolbar-partial-overview-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Places Category - Toolbar Place View Options]]

![[_media/gramps-place.png]] The holds two views that show [places](wiki:Gramps_Glossary#place): either as grouped (hierarchically in a tree) or ungrouped (in a simple flat list). Each view lists the geographical places in which the events of the database took place. These could be places of birth, death, and marriages of people, as well as their home, employment, education addresses, or any other conceivable reference to the geographical location.

- View - places grouped (hierarchically in a tree)

- List View - places ungrouped (in a simple flat list)

The Places View lists the places' `Name`, `Title`, `ID`, `Type`, `Code`, `Latitude`, `Longitude`, `Private`, `Tags`, and `Last Changed`. All of these columns can be used for sorting by clicking on a column heading.

<span ID="Places Tree View"></span>

### Place Tree View

![[_media/PlacesCategory-PlaceTreeView-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Places Tree View - example with context menu]]

The Place Tree View groups the list of places in a hierarchy: country, county, ... etc

You can expand the listing using the arrows.

{{-}}

#### Place Tree View context menu

All the nodes of the tree view mode can be simultaneously collapsed or expanded from the context/pop-up menu shown by selecting a place and right-clicking:

<hr>

- 

- 

- 

- 

<hr>

- 

- 

- 

- 

<hr>

- - 

<hr>

- 

<hr>

{{-}}

#### ⚙ Configuration Options

![[_media/PlacesCategory-PlaceTreeView-Configure-dialog-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Configure Places Category View - Places Tree View - Columns tab]] ![[_media/Gramps-config.png]] button in the [Toolbar](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window#Toolbar) is clicked to customize options specific to the current view mode. (As opposed to [](wiki:Gramps_6.0_Wiki_Manual_-_Settings) options that customize all views.) Alternatively, use the menu or press the *Configure active view* [keyboard keybinding](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings#Common_keybindings).

##### Columns

As with most list style Views, the layout configuration tab allows customization of which columns will be displayed and their order of display.

The available columns for display are:

-  (must be first column in the **Place Tree** view)

- *Title*

- **ID** (default)

- **Type** (default)

- **Code** (default)

- *Latitude*

- *Longitude*

- *Private*

- *Tags*

- *Last Changed*

Once the View columns are shown, clicking once on the column header sorts in ascending order, clicking again sorts in descending order.

These Configuration options and the current [filters](wiki:Gramps_6.0_Wiki_Manual_-_Filters) also constrain the data exported via the {{-}}

##### CSV Dialect

On the [CSV Dialect tab](wiki:Gramps_6.0_Wiki_Manual_-_Settings#CSV_Dialect) you can choose the CSV format for the delimiter to be used when [exporting this list view](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Export_View). {{-}}

<span ID="Place View">

### Places List View

</span> ![[_media/PlacesCategory-PlaceView-list-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Places Category - Place View (List) - example with context menu]]

The Place(s) View (List) shows all the places in one long list.

The Places View lists the places' `Name`, `Title`, `ID`, `Type`, `Code`, `Latitude`, `Longitude`, `Private`, `Tags`, and `Last Changed`. All of these columns can be used for sorting by clicking on a column heading.

{{-}}

#### Places List View context menu

Additional options are available by selecting a place from the list and using the context/pop-up menu shown by right-clicking:

<hr>

- 

- 

<hr>

- 

- 

- 

- 

<hr>

- - 

<hr>

- 

{{-}}

### Places Category Bottombar tabs

The shows the following [Bottombar](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window#Bottombar_and_Sidebar) tabs. {{-}}

#### Details

See [Details](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Details) Gramplet {{-}}

#### Location

See [Locations](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Locations) Gramplet {{-}}

#### Gallery

See [Gallery](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Gallery) Gramplet {{-}}

#### Events

See [Events](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Events) Gramplet {{-}}

#### Citations

See [Citations](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Citations) Gramplet {{-}}

#### Notes

See [Notes](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Notes) Gramplet {{-}}

#### References

See [References](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#References) Gramplet {{-}}

### Places Category Sidebar tabs

The shows the following [Sidebar](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window#Bottombar_and_Sidebar) tabs. {{-}}

#### Filter

See [Filter](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Filter) Gramplet {{-}}

### Map Service

![[_media/PlacesCategory-AttemptToSeeSelectedLocation-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Places Category - "Attempt to see selected locations with a Map Service (OpenstreetMap, Google Maps, ..." button - example]]

If a place has been highlighted, you may display the place in a web browser by selecting the button or using the right-click context menu to .

Your default web browser should open, attempting to use either the recorded coordinates (longitude and latitude) or the place name to display the location using the Maps provider web site. Different map services might have different requirements for the location description.

{{-}} ![[_media/PlacesCategory-MapServices-list-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Places Category - &quot;Select a Map Service&quot; button - showing list of options with OpenStreeMap (default)]]

From the drop down list you can choose the map service you want to use from the following three options:

- ****(default) - Uses longitude and latitude coordinates if present, otherwise uses city and country, or uses description of the place.
- ** - Valid for places within Sweden and Denmark, only if longitude and latitude are available, otherwise uses city and country, or uses description of the place.
- ** - Uses longitude and latitude coordinates if present, otherwise uses city and country, or uses description of the place.

{{-}} See also:

- [Map Services - Google Earth](wiki:Addon:MapService-GoogleEarth) - addon allows you to use Google Earth.

## Geography Category

![[_media/GeographyCategory-GeoPerson-navigator-expander-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Geography Category - partial overview of navigator - expander entries for all GeoPerson View Options]]

![[_media/Gramps-geo.png]]The shows place event data visually on a map. It contains many Geographic Views, which allows you to see the people and their events placed on a map via an internet map provider (OpenStreetMap, Google maps ...).

The following core Geography Views are available:

- **GeoPerson** -  - Show all known places connected to the active person.
- **GeoFamily** -  - Show all places connected to the active family.
- **GeoMoves** -  - Show all residences, displacements or moves for one person and their descendants.
- **GeoFamClose** Show  - if two families have been able to meet?
- **GeoClose** -  - Show if two people have been able to meet?
- **GeoPlaces** -  - Show all known Places in your family tree
- **GeoEvents** -  - Show all places connected to a filtered selection of events with a option.

These views are accessible via the buttons on the toolbar, the view menu and if selected as Navigator(Expander) entries. To filter on places or events, activate the filter sidebar via the menu

See also:

- Additional [third-party addon](wiki:6.0_Addons#Addon_List) Geography views are available:
  - **GeoAncestor** [Ancestors map](wiki:Addon:AncestorsMap) view addon - A Geography category View Mode which maps Event Places related to the Ancestors of the Home Person.
  - **PlaceCoordinateGeoView** [Place Coordinate Gramplet view](wiki:Addon:PlaceCoordinatesGramplet#Additional_geography_view_with_a_context_menu) addon - additional Geography category View Mode packaged with the Place and Coordinates Gramplet simplifies setting coordinates interactively.

![[_media/GeographyCategory-GeoPlaces-view-AllKnownPlaces-openstreemap-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "All known Places" GeoPlaces View - Geography Category - example using Openstreetmap]]

### Prerequisites for usage

To have these Geographic views work correctly, you need:

- To have events related to places.
- These places must have coordinates : latitude and longitude.
- If a place has no coordinates, it will never appear on the map.
- If you have an active internet connection, for all moves on the map, all zoom ... all tile maps are saved.
  - When you are without an internet connection, all tile maps are cached from the previous session and can be used.
  - So, the map can be used without an internet connection and all already visited places can be shown again.
  - The only thing to do is for each place or area you want to use without an internet connection is to select them, zoom into these places. You'll be able to use them again without connection.

#### Possible problems

- No Geography category icon in the Navigator sidebar : do you have the prerequisite `osmgpsmap` installed ? (*`gramps -v`* from the command line may help you)
- No tiles : do you have an internet connection active ?
- No tiles for one provider : if other providers are OK, file a bug
- Missing tiles : you have no internet connection and it's the first time you try to show the current place.
- Missing tiles : this can be the same as no tiles for one provider if they modify the access rules (i.e user-agent)
- Other : [Report a bug](wiki:Using_the_bug_tracker)

### Prerequisites to see the geography view

For Gramps 6.x, you need to install [osmgpsmap](http://nzjrs.github.io/osm-gps-map/) version 1.0 and above and the associated gir (**G**Object **I**ntrospection **R**epository) package.

For example on ubuntu, you must have: `gir1.2-osmgpsmap-1.0` and `libosmgpsmap-1.0-0`

### The different views

![[_media/GeographyCategory-GeoPerson-navigator-expander-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Geography Category - partial overview of navigator - expander entries for all GeoPerson View Options]]

As listed above the following core [Geography Views](#Geography_Category) are available: {{-}}

#### All known places for one Person

![[_media/GeographyCategory-AllKnownPlacesForOnePerson-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "All known places for one Person" GeoPerson View - Geography Category - example using Openstreetmap - sidebar and bottombar hidden]]

This view show all places visited by one person during that persons life.

This view is not connected to filters. It only depend on the active person and the history.

If you want to use the animate functionality, click on the [right button](wiki:Gramps_6.0_Wiki_Manual_-_Categories#button_3_.28_right_button_.29) of the mouse. You'll get a context menu popup. From the context menu popup, you can select to see the life way of the current person:

If the active person has several related events, you can see a virtual move between those markers. The move is related to years or distance and can be modified in the person map preferences. If the distance between to markers is greater than a value in tenth of degree, we show moves depending on distance instead of years. In these case, the number of steps between these two markers can be modified. You can modify the animation speed between steps. The moves start at the first event year until the last event year. {{-}} ![[_media/GeographyCategory-AllKnownPlacesForOnePerson-Configure-tab-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;The animation parameters&quot; tab for the &quot;All known places for one Person&quot; GeoPerson View - Configure the active view]]

##### Configure the active view

###### The animation parameters tab

tab See the configuration menu tab for the following options you can change:

- A slider to set the (default: *100*)
- A slider to set the (default: *20*)
- A slider to set the (default: *5*)

{{-}}

#### All known places for one Family

![[_media/GeographyCategory-AllKnownPlacesForOneFamily-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "All known places for one Family" GeoFamily View - Geography Category - example using Openstreetmap - sidebar and bottombar hidden]]

This view show all places visited by all family members during their lives.

This view is not connected to filters. It only depend on the active family and the history. {{-}}

##### Configure the active view

The configuration menu tab shows the tab for this view has which has no additional options. {{-}}

#### Every residence or move for a person and any descendants

![[_media/GeographyCategory-EveryResidenceOrMoveForAPersonAndAnyDescendants-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Every residence or move for a person and any descendants" GeoMoves View - Geography Category - example using Openstreetmap - sidebar and bottombar hidden]]

This view is used to show all the places in a person and their descendant's lifetime.

They are displayed by generation. You can change the delay between the generation display in the view configuration.

This view is not connected to filters. It only depends on the [Active Person](wiki:Gramps_Glossary#active_person) and their history. {{-}} ![[_media/GeographyCategory-EveryResidenceOrMoveForAPersonAndAnyDescendants-Configure-tab-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;The parameters for moves&quot; tab for the &quot;Every residence or move for a person and any descendants&quot; GeoMoves View - Configure the active view]]

##### Configure the active view

###### The parameters for moves tab

tab See the configuration menu tab for the following options you can change:

- A slider to set to show. (default: *20*)
- A slider to set the (default: *500*)

{{-}}

#### Have these two families been able to meet?

![[_media/GeographyCategory-HaveTheseTwoFamiliesBeenAbleToMeet-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Have these two families been able to meet ?" GeoFamClose View - Geography Category - example using Openstreetmap - sidebar and bottombar hidden]]

This view is used to show if two families were able to meet during their life.

You must select one reference family :

- From the menu popup : Choose the reference family
- From the toolbar

When the reference family is active, you'll see all its member's life way. For each known place with coordinates, you'll see a circle or an oval depending on the longitude.

The circle radius can be tuned in the configuration view. This value is defined in tenth of degree. {{-}} ![[_media/GeographyCategory-HaveTheseTwoFamiliesBeenAbleToMeet-Configure-tab-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;The selection parameters&quot; tab for the &quot;Have these two families been able to meet ?&quot; GeoFamClose View - Configure the active view]]

##### Configure the active view

###### The selection parameters tab

tab See the configuration menu tab for additional options. {{-}}

#### Have they been able to meet?

![[_media/GeographyCategory-HaveTheyBeenAbleToMeet-default-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Have they been able to meet ?" GeoClose View - Geography Category - example using Openstreetmap - sidebar and bottombar hidden]]

This view is used to show if two persons were able to meet during their life.

You must select one reference person :

1.  From the menu popup : Choose the reference person
2.  From the toolbar

When the reference person is active, you'll see its life way. For each known place with coordinates, you'll see a circle or an oval depending on the longitude.

The circle radius can be tuned in the configuration view. This value is defined in tenth of degree.

{{-}} ![[_media/GeographyCategory-HaveTheyBeenAbleToMeet-Configure-tab-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;The selection parameters&quot; tab for the &quot;Have they been able to meet ?&quot; GeoClose View - Configure the active view]]

##### Configure the active view

###### The selection parameters tab

tab See the configuration menu tab for additional options. {{-}}

#### All known places

![[_media/GeographyCategory-GeoPlaces-view-AllKnownPlaces-openstreemap-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "All known Places" GeoPlaces View - Geography Category - example using Openstreetmap - showing context menu]]

This view show all places with coordinates in the database.

For performances reason, by default, the view show only the place related to the places history or the filtered places. One additional step is required to see all places, you need to select "" from the context menu [right button](wiki:Gramps_6.0_Wiki_Manual_-_Categories#button_3_.28_right_button_.29) {{-}} ![[_media/GeographyCategory-AllKnownPlaces-Configure-tab-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}}  tab for the &quot;All known Places&quot; GeoPlaces View - Configure the active view]]

##### Configure the active view

###### The places marker color tab

tab The configuration menu tab for has the following options:

The view is the only Geography view that allows you to change the color used for the place type markers.

The colors are green for the following map renders:

- OpenStreetMap
- Maps for free
- Opencyclemap
- Public transport.

All other marker renders are red.

Click on the button on the toolbar.

Then click on the tab. The default color for each Place Type is green "#008b00"

For each type of place, you can select and choose a color. Once the **Pick a Color** dialog appears, you can drag a color swatch from that dialog to the Configure's swatches. It is not necessary to click the button for each Type then reopen the dialog.

See also:

- [Pick a Color selector](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Pick_a_Color_selector)
- [Can we change the place marker's color?](wiki:Gramps_6.0_Wiki_Manual_-_Categories#Can_we_change_the_place_marker.27s_color_.3F)

{{-}}

#### All places related to Events

![[_media/GeographyCategory-AllPlacesRelatedToEvents-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "All places related to Events" GeoEvents View - Geography Category - example using Openstreetmap - sidebar and bottombar hidden]]

For performances reason, the default view initially shows only the places related to the events history or the filtered events.

This view can also be used to show all places related to events. However, it can take some time to show when the tree records many events and many places.

<span id="show all events"> If you really want to see all events, you need to select "show all events" from the [right button](wiki:Gramps_6.0_Wiki_Manual_-_Categories#button_3_.28_right_button_.29) contextual popup menu.</span> {{-}}

##### Configure the active view

tab The configuration menu tab shows the tab for this view has which has no additional options. {{-}}

##### All known places for one person with graphical information (KML files)

![[_media/gramps-person-kml.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} One person with 3 KML files]]

If KML files are added as Media objects in the Gallery tab for the various records, the **** Geography view will show one path or one surface for each KML file.

In the following example, you see 3 layered KML files rendered from different Gallery tabs referenced by this Person:

- a farm limits outline KML in the Birth Event.
- a path KML used to go to school in the Education Event.
- a parish (or municipality) limits outline KLM in the Place Gallery tab for the Baptism Event.

In the case of the Farm limits outline, the KLM was added to the Gallery tab of the Birth Event (rather than being applied to that of the re-useable ['Farm' type Place](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_2#Place_Editor_dialog)) because acreage was bought and sold over the years. This outline represented the Farm size at the date of birth.

See [Adding places from KML files](wiki:Gramps_6.0_Wiki_Manual_-_Categories#Adding_places_from_KML_files)

{{-}}

### Geography Category Bottombar tabs

The by default displays no Gramplets in the [Bottombar](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window#Bottombar_and_Sidebar) tab. You may add them as required.

{{-}}

### Geography Category Sidebar tabs

The shows the following [Sidebar](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window#Bottombar_and_Sidebar) tabs.

{{-}}

#### Filter

The filter type may change depending on the view selected.

See [Filter](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Filter) Gramplet {{-}}

### Usage

#### Print or save the Map

Printing or saving each of the [Geography Category](wiki:Gramps_6.0_Wiki_Manual_-_Categories#Geography_Category) views, can be done via the menu, toolbar or keyboard shortcut as follows:

- Menu
- Toolbar button
- Keyboard shortcut

#### ⚙ Configuration Options

You can control the layout by clicking the ![[_media/Gramps-config.png]] button, choosing from the View menu, or pressing the *Configure active view* [keyboard keybinding](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings#Common_keybindings).

##### All views

![[_media/ConfigureGeography-the-map-tab-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Configure Geography - "The map" tab]]

tab contains options common to all Geography views:

- (the default is `~/.cache/gramps/maps` on POSIX systems and `C:\Users\`*<username>*`\appdata\local\gramps\maps` on Windows). If required you can change the directory where map tile files are stored on your computer. .

  - button

- A slider for (default: *12*). The zoom level for when we center the map or when we select one marker. Every time the Geographic View redraws the map, this zoomlevel will be used.

- A slider for (default: *5000*). Reducing this number for faster map drawing but with less life ways.

- \[x\]  - checkbox selected by default.

{{-}}

##### Specific views

See the configuration specific options for each views section.

- [Geography Category](wiki:Gramps_6.0_Wiki_Manual_-_Categories#Geography_Category) - List of views.

#### The mouse actions on the map

The following mouse actions on the map are described for right handed people using the right hand mouse button otherwise use the left hand mouse button if you are a left handed person.

##### button 1 (left button)

You have two possible actions for the button 1 (left button) :

1.  The place marker selection.
2.  Validate the region selection

##### button 2 ( middle button )

![[_media/Geography_MiddleButton.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Zoom rectangle drawn with middle button]] The only usage for the center button is to draw a rectangular region on the map via click and drag.

1.  when pressed : start the region selection
2.  when released, end the region selection.

A left-click (button 1) will zoom-in the Geography view to fit the rectangle. {{-}}

##### button 3 ( right button )

Only one usage for this button.

- show the [context menu popup](wiki:Gramps_6.0_Wiki_Manual_-_Categories#The_context_menu_popup).

#### The context menu popup

![[_media/GeographyCategoryView-context-menu-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Geography Category View - context menu - example]]

From this context menu, you have the following functions available for views:

<hr>

- \- hide or show the cross hair. See: [How to show remove the crosshair ?](wiki:Gramps_6.0_Wiki_Manual_-_Categories#How_to_show.2Fremove_the_crosshair_.3F)

- \- lock or unlock the zoom. See [How to lock unlock the map ?](wiki:Gramps_6.0_Wiki_Manual_-_Categories#How_to_lock.2Funlock_the_map_.3F)

- \- add a place at the mouse position. See [Adding or Linking to a place](wiki:Gramps_6.0_Wiki_Manual_-_Categories#Adding_or_Linking_to_a_place)

- \- link a place at the mouse position. See [Adding or Linking to a place](wiki:Gramps_6.0_Wiki_Manual_-_Categories#Adding_or_Linking_to_a_place)

- \- add a place from KML (Keyhole Markup Language) file. See [Adding places from KML files](wiki:Gramps_6.0_Wiki_Manual_-_Categories#Adding_places_from_KML_files)

- \- center the map at the mouse position.

<hr>

Also when using the or views you will see additional context menu entries for respectively:

- 

or

- 

and for both views:

- \> - center the map depending on a place from sub menu.

<hr>

- \- ... / Not available for the or views

- \- change the default map (provider). See [How to change the map provider?](wiki:Gramps_6.0_Wiki_Manual_-_Categories#How_to_change_the_map_provider_.3F)

- \- remove only the visible tiles already download from the current map provider.

- \- remove all tiles already download from the current map provider.

<hr>

{{-}}

#### How to zoom and move around the map ?

Zoom in and out and moving around the map can be achieved via the following methods:

##### Zoom in and Zoom out the map

To zoom, you can use :

- The buttons shown at the top left of the map.
- The scroll button on the mouse.
- The or key on the keypad (default).

You can replace the numeric keypad by the alpha numeric keyboard in the configuration view.

##### Move around the map

To move around the map, you can :

- Click on the map, then drag it.
- Use the arrows.

#### The mouse cursor over a place marker

When the mouse cursor is positioned over one *place marker*, the place name is display in the status bar.

#### Click on a place marker

We have two cases :

1.  events : For each event, we can edit this event or center the map on this place marker.
2.  places : For each place, we can edit this place or center the map on this place marker.

When centering the map, the zoom level used is defined in the

We may have several place markers in the clicked area depending on the zoom.

In this case, We show for each marker all related events and/or places.

We obtain a mix between the two cases described above.

#### Can we change the place marker's color ?

Only the view supports changing the place type markers colors all the other views are hard coded in Gramps. {{-}}

#### Adding or Linking to a place

For this context menu, (click on the [right button](wiki:Gramps_6.0_Wiki_Manual_-_Categories#button_3_.28_right_button_.29) of the mouse), select either or options.

When you add a place or try to link a place to the position of the *mouse pointer*, you'll get a window dialog.

From the window dialog you'll see on the map a circle in which you may choose markers place names. You can adjust the circle size with the cursor. Depending on the diameter of this circle, a list is created. If the place has already some filled fields, you'll see these values in a green color row. If you agree, you double click on this row. if you don't agree, you can choose another row.

Another way to set latitude and longitude :

- Install the [Place Cleanup Gramplet](wiki:Addon:PlaceCleanupGramplet) addon via the [Addons manager](wiki:6.0_Addons#Installing_Addons_in_Gramps). If you install this gramplet you can add latitude-longitude to all your places.

#### Adding places from KML files

For this, click on the [right button](wiki:Gramps_6.0_Wiki_Manual_-_Categories#button_3_.28_right_button_.29) of the mouse, you'll get a context popup menu.

In this menu, you can select (**KML** - Keyhole Markup Language)

You will get the file chooser dialog. Select the file you want to add.

If you have several places in the same KML file, you will get one place editor for each place. Be careful.

#### How to change the map provider ?

<table>
<thead>
<tr>
<th colspan="3">![[_media/OpenStreetMap_5.15.10.png|Center|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} OpenStreetMap]]</th>
</tr>
</thead>
<tbody>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>![[_media/MapsForFree_5.15.10.jpg|Left|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Maps For Free]]</td>
<td>![[_media/OpenCycleMap_5.15.10.png|Center|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} OpenCycleMap]]</td>
<td>![[_media/PublicTransport_5.15.10.png|Right|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Public Transport]]</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>![[_media/GoogleStreet_5.15.10.png|Left|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Google street]]</td>
<td>![[_media/GoogleSat_5.15.10.jpg|Center|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Google sat]]</td>
<td>![[_media/GoogleHybrid_5.15.10.jpg|Right|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Google hybrid]]</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>![[_media/Virtualearthstreet_5.15.10.png|Left|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Virtualearth street]]</td>
<td>![[_media/VirtualearthSat_5.15.10.jpg|Center|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Virtualearth sat]]</td>
<td>![[_media/VirtualearthHybrid_5.15.10.jpg|Right|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Virtualearth hybrid]]</td>
</tr>
</tbody>
</table>

Several map providers are available in Gramps.

From the context menu (click on the [right button](wiki:Gramps_6.0_Wiki_Manual_-_Categories#button_3_.28_right_button_.29) of the mouse) near the bottom you will see the:

- 

menu that allows you to select a another map provider from the following:

- **OpenStreetMap** (default) : The advantage of [OpenStreetMap](http://www.openstreetmap.org/) is that it is a free project, so you can update the maps yourself with missing information via their website.
- [Maps For Free](https://maps-for-free.com)
- [OpenCycleMap](https://www.opencyclemap.org/)
- Public Transport
- [Google street](https://www.google.com/intl/en_ALL/help/terms_maps.html)
- [Google sat](https://www.google.com/intl/en_ALL/help/terms_maps.html)
- [Google hybrid](https://www.google.com/intl/en_ALL/help/terms_maps.html)
- Virtualearth street ([Bing maps](https://www.bing.com/maps) was Virtualearth) [1](http://www.microsoft.com/maps/product/terms.html)
- Virtualearth sat ([Bing maps](https://www.bing.com/maps) was Virtualearth) [2](http://www.microsoft.com/maps/product/terms.html)
- Virtualearth hybrid ([Bing maps](https://www.bing.com/maps) was Virtualearth) [3](http://www.microsoft.com/maps/product/terms.html)

![[_media/GeographyCategoryView-context-menu-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Geography Category View - context menu - example]]

{{-}} See also:

- [Map Service](wiki:Gramps_6.0_Wiki_Manual_-_Categories#Map_Service) - Place Category.

#### How to show/remove the crosshair ?

It can be useful to have the crosshair visible to see the center of the map.

This functionality is available with the [right button](wiki:Gramps_6.0_Wiki_Manual_-_Categories#button_3_.28_right_button_.29) of the mouse. you'll get a context menu popup.

Select .

This is useful to add or link places to the correct latitude-longitude coordinates

#### How to lock/unlock the map ?

When we change the map ( person to family, ... ), the zoom is recalculated.

It can be useful in some case to keep the same zoom and position when we [change the map provider](wiki:Gramps_6.0_Wiki_Manual_-_Categories#How_to_change_the_map_provider_.3F).

For this, click on the [right button](wiki:Gramps_6.0_Wiki_Manual_-_Categories#button_3_.28_right_button_.29) of the mouse, you'll get a context menu popup.

In this menu, you can select .

## Sources Category

![[_media/gramps-source.png]] The offers two view modes ( View and View (default)) that list the sources of certain information stored in the family tree. The record selection, column configuration and Gramplet selections are independent for each view mode.

Sources can include various documents: birth, death, and marriage certificates; books; films; journals; private diaries - nearly anything that can be described as genealogical evidence. Gramps gives you the option to provide citations of sources for each (Event, Person, Place, Media, Note, et cetera) object you create.

By default, the Sources View mode lists the `Title`, `ID`, and `Author` of the source, as well as any `Publication` information that may be associated with it. The list of Sources can be re-sorted by clicking on a different column heading. Clicking the header the first time sorts the rows in ascending order based on that column. Clicking again reverses to descending order.

The tab of the Configure Sources dialog can be used to add, remove and rearrange the displayed columns. Click the ![[_media/gramps-config.png]] toolbar button or select from the menu to open the dialog.

You can select the toolbar button to create a new source or button to edit the sources selected in the list. Either action will invoke the dialog.

- See [Editing information about sources](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_2#Editing_information_about_sources)

{{-}}

### Sources List View

![[_media/SourcesCategory-Sources-ListView-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Sources" Category - "Sources" - List View - with context menu]]

The default, mode only shows the Sources as a list and displays the , , and of the source, as well as any associated . The list of Sources can be re-sorted by clicking on a different column heading. Clicking the header the first time sorts the rows in ascending order based on that column. Clicking again reverses to descending order.

{{-}}

#### Sources List View context menu

Additional options are available by selecting a source from the list and using the context/pop-up menu shown by right-clicking:

<hr>

- 

- 

<hr>

- 

- 

- 

- 

<hr>

- - 

<hr>

{{-}}

#### ⚙ Configuration Options

##### Columns

##### CSV Dialect

On the [CSV Dialect tab](wiki:Gramps_6.0_Wiki_Manual_-_Settings#CSV_Dialect) you can choose the CSV format for the delimiter to be used when [exporting this list view](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Export_View).

{{-}}

### Sources Category Bottombar tabs

The shows the following [Bottombar](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window#Bottombar_and_Sidebar) tabs. {{-}}

#### Gallery

See [Gallery](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Gallery) Gramplet {{-}}

#### Notes

See [Notes](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Notes) Gramplet {{-}}

#### References

See [References](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#References) Gramplet {{-}}

### Sources Category Sidebar tabs

The shows the following [Sidebar](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window#Bottombar_and_Sidebar) tabs. {{-}}

#### Filter

See [Filter](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Filter) Gramplet {{-}}

### Citation Tree View

![[_media/SourcesCategory-CitationTree-View-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Sources" Category - "Citation Tree" - View - example with context menu shown]]

The View mode list will also show all the sources. In addition, it allows the user to see the [Citations](#Citations_Category) associated with each source by clicking on the [disclosure triangle](https://en.wikipedia.org/wiki/Disclosure_widget) node expand or collapse disclosure triangular widget.

{{-}}

#### Citation Tree View context menu

All the nodes of the tree view mode can be simultaneously collapsed or expanded from the context/pop-up menu shown by right-clicking:

<hr>

- 

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

- - 

<hr>

{{-}}

#### ⚙ Configuration Options

##### Columns

The Columns tab allows customization of which columns will be displayed and their order of display.

The available columns for display are:

- 

{{-}}

##### CSV Dialect

On the [CSV Dialect tab](wiki:Gramps_6.0_Wiki_Manual_-_Settings#CSV_Dialect) you can choose the CSV format for the delimiter to be used when [exporting this list view](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Export_View).

{{-}}

## Citations Category

![[_media/gramps-citation.png]] The shows the that show the citations for certain information stored in the family tree.

Citations specify which parts of a source are relevant to the information in the Family Tree. For example, a Source may be a book, and the citation may be a particular page in the book. Gramps gives you the option to provide a citation for each event you record (births, deaths, marriages, etc.).

{{-}}

### Citations List View

![[_media/CitationsCategory-CitationView-List-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Citations" Category - "Citation View" (List) - example with context menu]]

The Citations List View shows the `Volume/Page` , `ID`, and `Date` of the citation, as well as the citations [<code>Confidence</code>](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_2#Citation_information) level of the evidence.

The list of Citations can be sorted by clicking on a column heading.

Clicking once sorts in ascending order, clicking again sorts in descending order.

The editor tab dialog can be used to remove and rearrange the displayed columns.

For the view via the menu or toolbar you may select:

- \-

- \-

- \-

- \-

- \-

The view may be exported to the CSV or spreadsheet format. {{-}}

#### Citations List View context menu

Additional options are available by selecting a citation from the list and using the context/pop-up menu shown by right-clicking:

<hr>

- 

- 

<hr>

- 

- 

- 

- 

<hr>

- - 

{{-}}

#### ⚙ Configuration Options

##### Columns

The editor tab dialog can be used to remove and rearrange the displayed columns and add the follow columns:

- Private
- Tags
- Last Changed
- Source:Title
- Source:ID
- Source:Author
- Source:Abbreviation
- Source:Publication Information
- Source:Private
- Source:Last Changed

{{-}}

##### CSV Dialect

On the [CSV Dialect tab](wiki:Gramps_6.0_Wiki_Manual_-_Settings#CSV_Dialect) you can choose the CSV format for the delimiter to be used when [exporting this list view](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Export_View).

{{-}}

### Citations Category Bottombar tabs

The shows the following [Bottombar](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window#Bottombar_and_Sidebar) tabs. {{-}}

#### Gallery

See [Gallery](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Gallery) Gramplet {{-}}

#### Notes

See [Notes](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Notes) Gramplet {{-}}

#### References

See [References](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#References) Gramplet {{-}}

### Citations Category Sidebar tabs

The shows the following [Sidebar](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window#Bottombar_and_Sidebar) tabs. {{-}}

#### Filter

See [Filter](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Filter) Gramplet {{-}}

## Repositories Category

![[_media/gramps-repository.png]] The shows the Repository List View. A repository can be thought of as a collection of sources. Each source in the family tree may be a reference to a repository (such as a library) in which it belongs.

{{-}}

### Repository List View

![[_media/RepositoriesCategory-Repositories-ListView-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Repositories" (list) view - example with context menu]]

This view shows a list of all recorded repositories. {{-}}

#### Repository List View context menu

Additional options are available by selecting a repository from the list and using the context/pop-up menu shown by right-clicking:

<hr>

- 

- 

<hr>

- 

- 

- 

- 

<hr>

- - 

<hr>

{{-}}

#### ⚙ Configuration Options

##### Columns

The Columns tab allows customization of which columns will be displayed and their order of display.

The available columns for display are:

- 

{{-}}

##### CSV Dialect

On the [CSV Dialect tab](wiki:Gramps_6.0_Wiki_Manual_-_Settings#CSV_Dialect) you can choose the CSV format for the delimiter to be used when [exporting this list view](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Export_View).

{{-}}

### Repository Category Bottombar tabs

The shows the following [Bottombar](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window#Bottombar_and_Sidebar) tabs. {{-}}

#### Details

See [Details](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Details) Gramplet {{-}}

#### Notes

See [Notes](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Notes) Gramplet {{-}}

#### References

See [References](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#References) Gramplet {{-}}

### Repository Category Sidebar tabs

The shows the following [Sidebar](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window#Bottombar_and_Sidebar) tabs. {{-}}

#### Filter

See [Filter](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Filter) Gramplet {{-}}

## Media Category

![[_media/gramps-media.png]] The shows the Media List View, which list the Media Objects stored in the family tree.

Media Objects are technically any files that relate somehow to the stored genealogical data.

Most frequently, these are images, audio files, animation files, etc. {{-}}

### Media List View

![[_media/MediaCategory-Media-ListView-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Media" Category - "Media" (List) View - example with context menu]]

The Media List View shows the following columns for the list `Name` , `ID`, `Type`, `Path` and `Date` of the Media Object.

The editor tab dialog may be used to rearrange the displayed columns, which obey usual sorting rules. {{-}}

#### Media List View context menu

Selecting a media item from the list and using the context menu (right-clicking) offers the following options:

<hr>

- 

- 

<hr>

- \- show the media item using an external program.

- \- which opens to the folder containing the media item.

- 

- 

- 

- 

<hr>

- - 

<hr>

{{-}}

#### ⚙ Configuration Options

##### Columns

The Columns tab allows customization of which columns will be displayed and their order of display.

The available columns for display are:

- 

{{-}}

##### CSV Dialect

On the [CSV Dialect tab](wiki:Gramps_6.0_Wiki_Manual_-_Settings#CSV_Dialect) you can choose the CSV format for the delimiter to be used when [exporting this list view](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Export_View).

{{-}}

### Media Category Bottombar tabs

The shows the following [Bottombar](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window#Bottombar_and_Sidebar) tabs. {{-}}

#### Preview

In the "Preview" tab you can double click on the media/photo to open it in the default picture viewer.

See [Media Preview](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Media_Preview) Gramplet {{-}}

#### Citations

See [Citations](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Citations) Gramplet {{-}}

#### Notes

See [Notes](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Notes) Gramplet {{-}}

#### Attributes

See [Attributes](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Attributes) Gramplet {{-}}

#### Image Metadata

See [Image Metadata](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Image_Metadata) Gramplet {{-}}

#### References

See [References](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#References) Gramplet {{-}}

### Media Category Sidebar tabs

The shows the following [Sidebar](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window#Bottombar_and_Sidebar) tabs. {{-}}

#### Filter

See [Filter](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Filter) Gramplet {{-}}

## Notes Category

![[_media/gramps-notes.png]] The View shows a List mode, which inventories the text notes (either pure text or pre-formatted) that can be referenced by the other objects.

See also:

- Using the dialog to make new annotations or editing information about existing notes

{{-}}

### Notes List View

![[_media/NotesCategory-Notes-ListView-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Notes" Category - "Notes" (List) view - example with context menu]]

The List View shows a list of text notes.

The functionality of the notes View is similar to the other views. The view lists all stored in the Family Tree.

Use the menu to open the editor tab and change the displayed columns from the default: `Preview`, `ID` and `Type`.

The `Type` can be ([amongst others](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_2#note_type)): *Event Note*, *Address Note*, *Source text*, *Place Note*. (In version 6.0, the built-in `Type` list includes: *Citation*, *Custom*, *General*, *HTML code*, *Link*, *Report*, *Research*, *Source text*, *To Do*, *Transcript*, *Unknown*)

Double-clicking on a Note item in the list will bring up the window dialog where you can edit the Note. You can change fonts, font color and background color. If enabled via the option a [spelling checker](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Environment_Settings) is available for *English* and your local language. {{-}}

#### Notes List View context menu

Selecting a Note item from the list and using the context menu (right-clicking) offers the following options

<hr>

- 

- 

<hr>

- 

- 

- 

- 

<hr>

- - 

  - 

<hr>

{{-}}

#### ⚙ Configuration Options

![[_media/Gramps-config.png]] button in the [Toolbar](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window#Toolbar) is clicked to customize options specific to the current view mode. (As opposed to [](wiki:Gramps_6.0_Wiki_Manual_-_Settings) options that customize all views.) Alternatively, use the menu or press the *Configure active view* [keyboard keybinding](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings#Common_keybindings).

The following two tabs are shown:

- Columns
- CSV Dialect

{{-}}

##### Columns

The Columns tab allows customization of which columns will be displayed and their order of display.

The available columns for display are:

- 

- 

- 

- 

- 

- 

{{-}}

##### CSV Dialect

On the [CSV Dialect tab](wiki:Gramps_6.0_Wiki_Manual_-_Settings#CSV_Dialect) you can choose the CSV format for the delimiter to be used when [exporting this list view](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Export_View).

{{-}}

### Notes Category Bottombar tabs

The shows the following [Bottombar](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window#Bottombar_and_Sidebar) tabs. {{-}}

#### References

See [References](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#References) Gramplet {{-}}

### Notes Category Sidebar tabs

The shows the following [Sidebar](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window#Bottombar_and_Sidebar) tabs. {{-}}

#### Filter

See [Filter](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Filter) Gramplet

{{-}}

[Category:Documentation](wiki:Category:Documentation)
