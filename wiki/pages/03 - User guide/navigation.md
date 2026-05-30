---
title: Gramps 6.0 Wiki Manual - Navigation
categories:
- Documentation
- Stub
managed: false
source: wiki-scrape
wiki_revid: 129610
wiki_fetched_at: '2026-05-30T11:35:35Z'
---

{{#vardefine:chapter\|10}} {{#vardefine:figure\|0}} As long as any [Family Tree](wiki:Genealogy_Glossary#family_tree) database is open, Gramps is focused on a single person usually referred to as an [Active Person](wiki:Gramps_Glossary#active_person). This allows you to view or modify the data concerning this person, his or her immediate family, etc. [Navigating in the Family Tree](wiki:Gramps_6.0_Wiki_Manual_-_Navigation#Setting_the_Active_Person) database (i.e. moving from person to person) is in fact nothing else but changing the Active Person.

This section describes many alternative ways to navigate through the database using both the complex and the convenient interfaces Gramps provides. All these ways fundamentally accomplish the same result, but some methods of navigating will be more convenient than others... depending on what you are doing in Gramps at the moment.

## Using the People Category

The most intuitive way to select an Active Person is to use the ![[_media/gramps-person.png]] [People Category](wiki:Gramps_6.0_Wiki_Manual_-_Categories#People_Category). When in the People Category, just select the name of the desired person from the list by clicking that list entry. The person you have selected becomes active. The statusbar updates to reflect the change of the active person.

See also

- [Editing information about people](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1#Editing_information_about_people)

## Using the Relationships Category

When in the ![[_media/gramps-relation.png]] [Relationships Category](wiki:Gramps_6.0_Wiki_Manual_-_Categories#Relationships_Category), you can easily navigate between the members of the displayed family as follows:

Click on the <u>underlined</u> name of the person you want to go to and this person will be the new active person of the Relationships Category.

The name of the currently active person is not underlined.

In addition to this, Gramps provides an extensive set of keyboard navigation options. The detailed reference to the key bindings is found in the [Appendix B: Keybindings reference](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings).

## Using the Families Category

When in the ![[_media/gramps-family.png]] [Families Category](wiki:Gramps_6.0_Wiki_Manual_-_Categories#Families_Category), you can easily navigate between the displayed families.

The Families can be used to visually compare a series of families for possible duplicates and missing data. Sorting on the different columns allows putting similarly named Partners in close proximity allowing Spouses to be compared. You can match by Given name or Nickname by temporarily changing the option in the section of dialogs tab. As an example, a name format of **Given Surname Suffix** would makes the column sort on the nickname name.

Merging two families will not only combine the Family secondary objects, but also simultaneously merge the two fathers and two mothers.

The Family view's Filter Gramplet allows searching for Persons in different family roles. So you might look for Families with a father named "John", a mother named "Mary" and a child named "Thomas".

## Using the ![[_media/22x22-gramps-pedigree.png]] Charts Category

![[_media/TimelinePedigreeView-Addon-Existing-Person-ContextMenu-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Timeline Pedigree View - Third Party Addon for Charts Category - context menu example]] Gramps relies heavily on form-based layouts of linked list items. These imply relationships between records in your family Tree. The **[Charts Category](wiki:Gramps_6.0_Wiki_Manual_-_Categories#Charts_Category)** provides an alternative, more visual, way of representing those relationships. The positions, shapes, and colors of containers along with their connecting lines & arrows can show an extra depth of interrelation with different factors. Containers can be simple color filled boxes, arcs, ribbons, or many other shapes.

But the [Charts Category](wiki:Gramps_6.0_Wiki_Manual_-_Categories#Charts_Category) also provides an alternative way to navigate through the family tree. The benefit of this method is that you can see more than one generation of the family tree. So you can jump directly from a great-grandson to a great-grandfather without going through the intermediate generations.

Note that after changing the [Active Person](wiki:Gramps_Glossary#active_person) in the Charts Category, the Chart View is re-adjusted to the newly selected Active Person focus. When in the Charts Category, you can easily navigate between the members of the displayed family tree as follows:

To make any displayed person the Active Person focus, left-click their corresponding container. Right-clicking the container will invoke a context menu with options appropriate to contents.

The context menu for a Person container may contain ▶sub-menus listing all spouses, siblings, children, and parents of the corresponding Person. The first entry in the context menu will usually be the name of the Person in that container. (It could alternately be an Edit option.) Selecting the Person name will shift focus in the same way as left-clicking the container. You can also change the Active Person focus to any of the spouses, siblings, children, or parents of any displayed person.

Some charts views have an obvious navigational correlation. Moving through generations intuitively matches moving to the left, right, upwards or downwards in the chart. These may have custom directional navigation buttons to allow navigation by clicking rather than dragging.

As an example, to change the focus of the [Pedigree View](wiki:Gramps_6.0_Wiki_Manual_-_Categories#Pedigree_View) to a child (if any exists) of the current Active Person, click the (*Left Arrowhead*) button to the left of the Active Person’s chart box. If there is only one child, the focus changes immediately. If the Active Person has more than one child, the (*Left Arrowhead*) button expands with a pop-up menu with a selectable list of the children. (For this particular (*Left Arrowhead*) button, the pop-up menu list of Children is sorted by that Parent‘s Marriage order, sub-sorted by Birth order. These [orders can be changed](wiki:Gramps_6.0_Wiki_Manual_-_FAQ#How_do_I_change_the_order_of_children.3F) globally in the Relationships category.)

Like containers, buttons may have alternate features accessed by right-clicking and choosing from a contexual pop-up menu.

Other buttons are less obvious aids to navigating to not People but features of Gramps. Using the [Pedigree View](wiki:Gramps_6.0_Wiki_Manual_-_Categories#Pedigree_View) example again, rolling over the lines between boxes shows a hint with any known basic details about the relationship and double-clicking those lines opens the editor for that Family. And double-clicking the Active Person box opens the editor for that Person. It is well worth reading the detailed documentation on each Chart View to discover these hidden shortcuts to favorite features.

The builtin Views of the [Chart Category](wiki:Gramps_6.0_Wiki_Manual_-_Categories#Charts_Category) are introduced in the [Categories](wiki:Gramps_6.0_Wiki_Manual_-_Categories) reference section. Some are described in greater depth in articles listed at the bottom of the View’s introductory section.

The collection of Views in the Charts Category can be expanded with Third-Party Addons using the [Plugin Manager](wiki:Gramps_6.0_Wiki_Manual_-_Plugin_Manager) feature of Gramps. The available Third-Party Addon plugins can be found under the **View** column of the [list of Addons](wiki:6.0_Addons#Addon_List) table. The maintenance of a few Third-Party Addon Views has been adopted by the Gramps volunteer team over the years. These became 'builtin' after being vetted and then included in the main Gramps distributions. Articles about using each Addon View are linked to the label **Plugin/Documentation** column. The quality of documentation varies dramatically for these articles.

## Using Gramplets

![[_media/DashboardCategory-DashboardView-default-gramplets-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Dashboard Category view - with default Gramplets shown]]

On the [Sidebar and bottombar](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#The_split-screen_Sidebar_.26_Bottombar), you can add Gramplets to expand your navigation options beyond a single generation's distance. Some examples are:

- [Relatives](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Relatives)
- [Descendants](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Descendants)
- [Pedigree](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Pedigree)
- [Fan Chart](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Fan_Chart)

These examples provide the ability to navigate the Active Person focus with using the perspective of familial relationship... to nearby relatives, descendants or ancestors. Future Gramplets might allow navigating by geographical proximity, [DNA matching](wiki:Addon:DNASegmentMapGramplet) or some other connection we haven't yet considered.

The text based Gramplets tend to have names [hotlinked for navigation](#Hotlink_Navigation) while the graphical ones may use [contextual menus](#Contextual_Menu_Navigation). {{-}}

## Setting the Home Person

One (and only one) person in the Family Tree database can be designated as the [Home Person](wiki:Gramps_Glossary#home_person). Once the Home Person is designated, returning the [Active Person](wiki:Gramps_Glossary#active_person) focus to that person becomes a matter of a single click, regardless of which Category is being used at the moment.

To set the Home Person, first [navigate](wiki:Gramps_6.0_Wiki_Manual_-_Navigation#Setting_the_Active_Person) to that person using any method you like. Then choose the People category and select the menu . Once this is done, you can move to the Home Person from anywhere in the database by simply clicking the Toolbar ![[_media/Gramps_Go-Home48x48_win.png]] icon. You can also choose the menu or select item from any context menu available on the right click or use the keyboard shortcut .

- [Settings#Setting Home Person](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Setting_Home_person)
- On the [Edit Person dialog](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1#Edit_Person_dialog) you can select from the context menu.

## Setting the Active Person

The [Active Person](wiki:Gramps_Glossary#active_person) is expected to be the contextual focus of actions, reports and edits. They are the selected item in the Person view or at top of the Relationship view.

The Active Person focus may be selected directly or "navigated" to indirectly. Methods include:

- clicking on a person's listing in the Person view
- selecting the person from the [Bookmarks](#Bookmark_Navigation) menu
- [Using history-based Navigation](#Using_history-based_Navigation) ( and toolbar buttons and the menu)
- [hotlink navigation](#Hotlink_Navigation)
- [Context menus](#Contextual_Menu_Navigation)
- [Notes as Navigational Shortcuts](#Notes_as_Navigational_Shortcuts)

There is a selection highlight as a visual cue of the Active Person in the People View. In the Relationship View, the Active Person is shown in a separate section at the top. All other persons shown below have an immediate (parent, sibling, spouse, child) relationship with the Active Person. Optionally, the [Status Bar may set](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Display) to list the focus Object for the View Category. (The Active Person is the focus for several View Categories.)

### Hotlink Navigation

Normally, simply clicking on the hotlinked name of a Person will select that person and shift this Active Person contextual focus.

![[_media/Relationships-category-view-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Relationships Category view]]Each Person's name in the Person and Relationship category views is a hotlink. Changing the Active Person focus in Person view appears to merely change which record is highlighted. But this also causes Gramplets contents to be updated and the Relationship, Charts and Geography views to be re-focused on the new Active Person.

Selecting a different hotlinked name in the Relationship category view causes a less subtle change. The perspective of how the family data is represented changes towards that focus. Their details move to the top section and their immediate family are re-arranged below.

{{-}}

### Contextual Menu Navigation

However, hotlinked names in the References tab and Notes (and in some Gramplets) will merely open the Person Editor window *without* navigating the Active Person focus to that Person. (These links behave as though you had clicked an button instead of a hotlinked name.) This facilitates quickly editing Persons around the Active Person without the disorientation of a shifting focus.

![[_media/QuickViewReport-EditPerson-context-menu-popup-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Context menu on the Person editor]] The Active Person focus can be set while in the by using the context menu (right-clicking) in the empty space of the header area. The option in that context menu changes the Active Person focus to the Person being edited. {{-}}

### Using history-based Navigation

![[_media/History-based-navigation-tools-Go-menu-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Example of the history based navigation tools ("Go" menu)]]

Gramps also features a powerful set of history-based navigation tools. These tools are similar to those commonly used in web browsers.

They include and items available from the menu, context menus and keybindings (available in People, Family, and Pedigree Categories), and the and toolbar buttons. They also include the list of the recent selections available under the menu that allows you to jump directly to any of the recent selections. Finally, clicking on the and toolbar buttons goes to previous or next object in the history. {{-}}

- [Gramps_6.0_Wiki_Manual_-_Navigation#Navigation_History](wiki:Gramps_6.0_Wiki_Manual_-_Navigation#Navigation_History)

### Bookmark Navigation

![[_media/Gramps_Go-Home48x48_win.png]] The on the toolbar is a special case bookmark. It shifts the Active Person focus to the Person currently designated as the [Home Person](wiki:Gramps_Glossary#home_person). This is so frequently useful that this feature has the [keybinding](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings#Common_keybindings) . {{-}} Similar to setting the Home Person, you can bookmark other people from the database to simplify further navigation. To bookmark a person, first navigate to that person, then choose the menu or use the [keybinding](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings#Common_keybindings) , if no person is selected you will get the warning. To move to that person elsewhere in the database, choose the menu from the list of bookmarked names shown. The other categories have their own list of Bookmarks.

#### Organize Bookmarks dialog

![[_media/OrganizeBookmarks-dialog-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Organize Bookmarks" dialog - example]]

You can manage your bookmarks by choosing the menu or [keybinding](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings) . This opens the dialog with the list of bookmarks and the controls to modify this list.

Use the and buttons to change the list sequence. Use the button to remove a Bookmark. The will bring you to this page, and you close the window with the button.

The list of Bookmarked People can be selected through the People Category, as explained above, but is also shared with the Relationships and Charts Categories.

On a similar basis, separate lists of Bookmarks are maintained in each of the following Categories: Families, Events, Places, Sources, Citations, Repositories, Media, and Notes.

{{-}}

### Notes as Navigational Shortcuts

![[_media/Note-showing-tooltip-for-link-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Notes Editor - Linking text]] There are separate Bookmarks lists in several categories. But they are still just simple lists. Long lists of bookmarks quickly become unwieldy.

Persistent Links can be created in [Notes](wiki:Gramps_Glossary#note). Use the [Link Editor](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_2#Link_Editor) in Notes to organize navigation links to different types of Gramps records following to your own organization methods. Once a Note has linked text, that linked record can be used like a Bookmark. In Note Gramplets where editing is not active, clicking on the Link open the Object Editor for that link. (It requires an extra modifier in the Noted Editor: navigate to that record by holding the key and clicking on the Linked Text.) One note be used as a Linked Index to other Notes with different sets of Links.

An example of a linked note might include an obituary where all the Persons, Places or even the Events are Linked. This makes it easier to navigate to the indirectly related (or even unrelated) pallbearers, funeral [officiators](wiki:Gramps_Glossary#officiator), or attendees.

Another note might be the transcribed bibliography for the published original research of another genealogist. As you collect digital copies of those originally cited references, the linked bibliography can be used as a Source acquisition checklist. When completely Linked, the Bibliography can be use to navigate through Sources for each citation while searching for unsupported conclusions, inaccuracies or omissions. {{-}}

## Finding records

### Browse to a record

To find a record in one of the category list views, first switch to the appropriate category that provides the list of the desired records: People, Sources, Places, or Media. Then scroll to the desired record. The focus of the active record for the category is changed by selecting a record. Simply scrolling the view does not change the active record focus.

By default, the list will be sorted on the first column of the tabular data. The for grouped (People) or hierarchical tree (Places) records, the first column is required to be the "Name" column. In the People, the grouping is based on the Preferred Surname. In the Places, the Grouping is based on the order of Enclosing Places.

The order and display (or hiding) of columns change be Configured. A dialog appears after selecting the menu item; or, clicking the Configure button on the Toolbar; or using the configure active view [common keybinding](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings#Common_keybindings).

The list of records in the view can be reduced by filtering with the [Search Bar](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window#Search_Bar) or the [Filter gramplet](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Filter). {{-}}

### Find a Record

![[_media/Find-type-ahead-search-PeopleTreeView-list-example-detail-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Interactive search box at bottom of list view - example]] ![[_media/Find-type-ahead-search-PeopleTreeView-list-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Find type ahead search on the &quot;People Tree View&quot; list example]]

Also known as an "interactive type-ahead search".

Select a line in the list to gain focus and then start typing information (contained in the data of the current Sort column) of a person or the title of a Source, Place, or Media object that you are attempt to find, respectively. The focus will shift to the first record that matches the text in the search mode textbox.

Alternatively, after clicking anywhere in the main view area to gain focus, press ( on macOS) [keybinding](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings#All_List_Views_bindings) to turn on the search mode textbox. This keybinding is often overlooked since simply starting to type is also enough to both open the box and start entering the search term.

As you type, the first matching record in the sort column of the list will scroll to the center of the list and be selected. As you type more characters, the match will be refined. As long as the search mode text box is visible, pressing the down arrow cursor key will move to the next match while pressing the up arrow cursor control key will move to the previous match. The box disappears after it is idle. (When there have been no keystrokes for between 5 and 15 seconds.) Without the Find box active, the cursor control keys revert to moving the records selection up and down the list.

Changing the sort column (by clicking on the header) also changes the column being matched. Finding in a different sort column works best in Flat List view modes.

People or Place category view modes with hierarchical grouped are a bit less responsive than Flat List view that are already sorted alphabetically. The Grouped Person is the most complex functionality. By default, it is sorted on the Grouping name then sub-sorted on the 'Name' column in the 'Display As' [Name format](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Display_Name_Editor) from the Data menu of Preferences. That will be the Preferred/Primary name in "Surname, Given Suffix" format and the "Surname" includes the Prefix and Connectors. However, the 'Group as', 'Sort as', and 'Display as' settings can be used to override the order using the '[Name Editor](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data%3A_detailed_-_part_3#Name_Editor).' {{-}}

### Jump to by Gramps ID

![[_media/Jump-to-by-Gramps-ID-dialog-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Jump to by Gramps ID - dialog - example]]

If you know the ID for the target record in the currently active category, The **Jump to** feature can be the most efficient way to navigate to that target.

Pressing the [keybinding](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings#Common_keybindings) will show the dialog allowing you enter the particular [Gramps ID](wiki:Gramps_6.0_Wiki_Manual_-_Settings#ID_Formats) in the current View to which you want to make active.

only searches for an exact text match. The Gramps ID can either be generated automatically when the ID field is left blank when adding a record or [manually entered](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1#ID) as an override.

It is similar to Find, except that it is not interactive and ONLY works on the Gramps ID field rather than the column that currently selected for sorting. And can change the focus for the active record in every view category except the Geography and Dashboard categories.

#### See also

- [The “Jump to” Gramps ID feature](https://gramps.discourse.group/t/the-ctrl-j-jump-to-gramps-id-feature/3756) discussion

<!-- -->

- GEPS: [Selector design proposals](wiki:GEPS_041:_New_Selector)

{{-}}

### Navigation History

A history of the recently active records for the focus the active category is tracked. The last ten are made accessible through the menu and its [keybindings](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings#Common_keybindings). Or you can scroll through the focus history with the left and right cursor keys.

## Using the Clipboard

![[_media/Clipboard-dialog-example-context-menu-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Clipboard - dialog - Showing Context menu (right click) example]]

For an application like Gramps the is very important as it will help reduce repetitive data entry.

The tool provides a temporary notepad to store database records for easy reuse during a single Gramps session eg: until you exit Gramps. In short, this is a sort of the copy-and-paste functionality extended from textual objects to other types of records used in Gramps. Clipboard makes extensive use of the [*drag and drop*](http://en.wikipedia.org/wiki/Drag-and-drop) technique

To invoke the , either choose the menu or click the Toolbar ![[_media/Gramps_Clipboard48x48_win.png]] button or use the [Keyboard shortcut (accelerator key)](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings#8) .

{{-}}

supports addresses, attributes (both personal and family), events (both personal and family), names, media objects references, citations, URLs, and of course textual information of notes and comments. To store any type of these records, simply drag the existing record on to the Pad from the corresponding editor dialog. To reuse the record, drag it from the Clipboard on to the corresponding place in the editor, e.g. Address tab, Attribute tab, etc.

### Clipboard context menu

Selecting a record using the context menu (right click) will show the following three options for each record type:

- 

- 

- 

{{-}}

One example  
You find a birth certificate of a person. In this certificate also the witnesses are mentioned. And the birth certificate also determines a source where the information was stored. The best way is to open the clipboard and drag the source you want to work with there. Then use drag and drop to use it in new items you use.

Now you can finalize the information on the person editor screen. Drag that info also to the Clipboard.

Now you add two new persons for the witnesses (assuming you do not have them already in your database). Simply drag and drop the birth info to the witness event screen. You are then presented with the screen where you can change the role of the witness to witness for this birth event. You do the same with the other witness.

This saves you a lot of typing and possible errors.

<span id="Using the Addon Manager..."></span>

## Using the Addon Manager

![[_media/AddonManager-addons-listing-60.png|Right\|thumb\|550px\|Fig. {{#var:chapter}}.{{#vardefineecho:figure\|{{#expr:{{#var:figure}}+1}}}} **Addon Manager** dialog showing the tab]] You can access the from the menu or select the icon on the toolbar to show the 's tab window that will list the Third-party addon plugins available based the currently selected projects on the tab.

Gramps utilizes builtin and addon (aka "add-on") plugin (aka "[plug-in](https://wikipedia.org/wiki/Plug-in_(computing))") modules to extend the capabilities of the core application. One of the primary benefits of a plugin framework is that it allows evolution of a specific feature without needing to update the entire program. Addons should not be mistaken for being of lesser utility to basic users than core features or builtin plugin. Nor does "Third-Party" mean an addon is of lesser quality. However, the addons published to the Gramps-Project GitHub repository have been vetted and will not covertly change your Tree data.

The [Addon Manager](wiki:Gramps_6.0_Wiki_Manual_-_Navigation#Addon_Manager) provides a way to explore which Addons will enhance your personal workflows. And the [Plugin Manager](wiki:Gramps_6.0_Wiki_Manual_-_Plugin_Manager) (or the [Plugin Manager Enhanced](wiki:Addon:Plugin_Manager) addon) builtin plugins provide a way to customize Gramps to remove the clutter of features that you do not use.

{{-}}

<span ID="Addon Manager..."></span>

### Addon Manager

The shows the following three tabs:

- The tab shown by default displays the list of available Addons.
- The tab where options can be changed
- The tab where external or local addon repository links can be added.

{{-}}

#### Addons

![[_media/AddonManager-addons-tab-default-60.png|Right|thumb|550px|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} <strong>Addons</strong> tab for <em>Addon Manager</em> dialog showing default filters while loading the lists of available addons]]

![[_media/AddonManager-addons-tab-default-no-internet-60.png|Right|thumb|550px|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} <strong>Addons</strong> tab for <em>Addon Manager</em> dialog showing result of no internet connection]]

The dialog's tab will show a list of available Addons after loading the lists from the [Gramps Project Default server](wiki:Gramps_6.0_Wiki_Manual_-_Navigation#Projects) that requires access to the internet; the list can be reloaded by pressing the button. The Addon Manager is available without a Family Tree loaded. The button will show this section.

The top of window shows a filter field where you can type any part of the addons name and the results below will be restricted/filtered to those addons that match.

Below the search field you have five addon (see: [Addon list legend](wiki:Addon_list_legend)) and a button to show all results again:

- Installation status:
  - \- *default*

  - Not installed

  - Installed

  - Updates
- Project:  - *default*
- Type:  - *default*
- Audience:  - *default*
- Status:  - *default*

To install the addon you are interested in use the various search filters and then select the [Addon listing](#Addon_listing) entries button and once installed the addons version number will be shown on the right hand side of the entry if all prerequisite requirements if any are met.

You can change the first filter (Installation status) from to to manually check for new versions of your installed addons. Or you can have Gramps automatically check for addons by using the setting shown on the [Third-party Addons: Installing Addons in Gramps](wiki:6.0_Addons#Installing_Addons_in_Gramps).

The Addon manager does not support removal, for that you can use the [Plugin Manager](wiki:Gramps_6.0_Wiki_Manual_-_Plugin_Manager) to hide the addon.

##### Addon listing

![[_media/AddonManager-addons-listing-60.png|Right|thumb|550px|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} <strong>Addon Manager</strong> dialog showing the  tab with addons installed]]

Each addon listing shows the following information:

- Addon name
- Second line shows multiple colored boxes with details:
  - Left side: *Project*, *Type*, *Audience*, *Status*, *Version*
  - Right side: *Installed Version*, of the addon only shown if installed.
- Description
- Botton line may show multiple buttons depending on installation status:
  - Left side: button that provides a link to the addons support page, only shown if available.
  - Right side: button.

see: [Addon list legend](wiki:Addon_list_legend) {{-}}

#### Settings

![[_media/AddonManager-Settings-tab-default-60.png|Right|thumb|550px|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} <strong>Addon Manager</strong> dialog showing default  tab]]

The Addon Manager dialog's Settings tab has the following two sections:

- General
- Scheduled update checks

##### General

-   
  Checkbox un-selected by default

##### Scheduled update checks

The following setting only applies to the window.

- Select the frequency that Gramps checks for updates to [Addons](wiki:6.0_Addons#Installing_Addons_in_Gramps).

  - *Never* - never checks for updates when you start Gramps (*Default*)
  - *Once a month* - checks for updates when you start Gramps once a month
  - **Once a week** - checks for updates when you start Gramps once a week
  - *Once a day* - checks for updates when you start Gramps once a day
  - *Always* - checks for updates whenever you start Gramps

- so when you check for updates, it checks for:

  - *Updated addons only* - does not check for new addons
  - *New addons only* - does not check for updated addons (*Default*)
  - **New and updated addons** - checks for all new and updated addons

-   

  - Checked: Means that new/updated addons are only asked about once; afterwards it does not show them to you (*Checkbox selected by default*)

  - Unchecked: Means that new/updated addons are always shown to you.

-   
  Button assumes you have an **Internet** connection and if pressed will force a check for Addons based on the above settings, if Addons are available you will then be presented the window where you choose and install them from.

{{-}}

##### Available Gramps Updates for Addons

![[_media/AvailableGrampsUpdatesforAddons-example-listing-60.png|Right|thumb|550px|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} <strong>Available Gramps Updates for Addons</strong> dialog after checking for updated addons in the  tab]]

The window you will show a list broken down by **[Type](wiki:Addon_list_legend#Type)** that you can view by selecting the `Select` column to expand out each of the top level arrows to show the listings under those `Type` that will show the `Name` and `Description` of the Addons.

- You can then select the check box of those Addons you want to install.
  - Alternatively but not recommended you can use the button.
  - The will un-select all choices.
- Then select the button to download those Addons from the *Internet*.
- While downloading you will be shown the window.
- Once downloads are completed from the dialog select the button
- From the dialog select button.
- To use the Addons you need to restart Gramps, menu .

{{-}}

###### Progress Information window

![[_media/ProgressInformation-window-60.png|Addon Progress Information window - example]] The Addon window is shown while *Downloading and installing selected addons...*

If required you may the download. {{-}}

###### Done downloading and installing addons dialog

![[_media/DoneDownloadingAndInstallingAddons-dialog-example-60.png|&quot;Done downloading and installing addons&quot; dialog - example]] The dialog is shown once the download is completed and reports how many addons have been installed, along with a reminder that if you have installed a 'View' addon you will need to restart Gramps. Select the button to continue. {{-}}

#### Projects

![[_media/AddonManager-Projects-tab-default-60.png|Right|thumb|550px|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} <strong>Addon Manager</strong> dialog showing default  tab]]

Where to check for Addons either the main Gramps Project *Default* server:

- **Gramps**:

:;https://raw.githubusercontent.com/gramps-project/addons/master/gramps60

Or any Gramps compatible Addon servers that you have added, the [Other projects](wiki:Gramps_6.0_Wiki_Manual_-_Navigation#Other_Projects) section shows a list of know external projects.

Near the bottom left of the Projects tab you have the following options

- \- opens the dialog for you to add the project name and URL.

- \- deletes the selected project lines. (The **Gramps** default project cannot be deleted, but it can be unselected so nothing is checked on that server.)

- \-

- \-

- \- opens the dialog where selecting removes all other projects.

{{-}}

##### New Project dialog

![[_media/NewProject-default-dialog-60.png|Right|thumb|450px|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} <strong>New Project</strong> dialog - default]]

The dialog allows you to enter the and of the external projects and can also be used for local projects. {{-}}

##### Other Projects

![[_media/AddonManager-Projects-tab-with-default-and-known-external-other-projects-60.png|Right\|thumb\|550px\|Fig. {{#var:chapter}}.{{#vardefineecho:figure\|{{#expr:{{#var:figure}}+1}}}} **Addon Manager** dialog showing optional projects tab]] List of known external other projects (copy and paste the **Project name** and **URL** as required to the :

<hr>

- **Project name:** `Isotammi project addons`

:;URL:

:;https://raw.githubusercontent.com/Taapeli/isotammi-addons/master/addons/gramps60

  
Summary: [Addon:Isotammi project](wiki:Addon:Isotammi_addons)

<hr>

- **Project name:** `Jean Michault tools for FamilySearch`

:;URL:

:;https://raw.githubusercontent.com/jmichault/gramps-kromprogramoj/gramps60

  
Summary: <https://github.com/jmichault/gramps-kromprogramoj> & [PersonFS](https://github.com/jmichault/PersonFS) gramplet (FamilySearch) / <https://github.com/jmichault/gramps-kromprogramoj/blob/gramps60/ReadMe.en.md>

<hr>

- **Project name:** `GlopGlop’s collection for France`

:;URL:

:;https://raw.githubusercontent.com/grocanar/glopglop-addons/main/gramps60

  
Summary: GedcomforGeneanet & ImportGenewebPlus

<hr>

- **Project name:** `ztlxltl experimental FamilyTreeView (FTV) chart view`

:;URL:

:;https://raw.githubusercontent.com/ztlxltl/FamilyTreeView/dist/gramps60

  
Summary: <https://github.com/ztlxltl/FamilyTreeView> [Addon:FamilyTreeView](wiki:Addon:FamilyTreeView)

<hr>

- **Project name:** `ChatWithTree - by MelleKoning (Hace)`

:;URL:

:;https://raw.githubusercontent.com/MelleKoning/addons/refs/heads/myaddon60/gramps60

  
Summary: [ChatWithTree](wiki:Addon:ChatWithTree) is a Chatbot to interact and query a Gramps genealogy Family tree.

<hr>

- **Project name:** `WebSearch - by Urchello (Hace)`

:;URL:

:;https://raw.githubusercontent.com/jurchello/WebSearch/dist/gramps60

  
Summary: [WebSearch](wiki:Addon:WebSearch) is a gramplet web lookup by parameters based on the current record or an ID stored as an Attribute.

<hr>

There is a Discourse community support thread where other ["Project"](https://gramps.discourse.group/t/curated-addon-collections/7170) (or curated collections of Gramps addons) are listed.

<hr>

You can also add local projects see example screenshot.

Local example for Microsoft Windows  
Path to your local project, useful to developers creating addons. The string **<file:///>** refers to internal storage to access a Windows PC's internal storage.

- **Project name:** `Local Example`

:;URL:

:;file:///c/Users/User/Desktop/gramps60

{{-}}

##### Restore project defaults

![[_media/Restore-project-defaults-dialog-60.png|Right|thumb|550px|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} <strong>Restore projects defaults</strong> dialog]]

If needed you can verify that in the option has the correct URL. To locate the [list of addons](https://raw.githubusercontent.com/gramps-project/addons/master/gramps60/listings/addons-en.json) for your current language and version, it should be set to:

:;https://raw.githubusercontent.com/gramps-project/addons/master/gramps60 if not select the button on the *Projects* tab, that removes all entries except the default.

{{-}}

## Using Undo History

![[_media/Menubar-Edit-defaults-family-tree-loaded-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menubar - Edit Overview]] A work session has an Undo history to reverse transactions.

Three related menu options:

- \- Shows the last change made that can be reverted.

- \- Shows the last change made that can be reverted.

- \- shows the dialog.

see [keybindings](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings).

Various actions will reset the sessions change history and show the :

- Some Tools and Import are batch transactions so the user is warned before the undo history is lost/cleared.
- The menu option undoes the Undo History.
- Exiting Gramps and restarting.

See also:

- Gramplet - Keeps track of activity in this session. It lists selected and edited objects.

- undo history can be invoked, even though it is not possible to undo anything.

-   
  Remove "Abandon Changes and Quit"

-   
  Harmonize History/logging features

- History: 2006 Gramps version 2.1.2. added [New Undo History dialog. You can view all the changes that have been made, and can select the point to which you would like to undo (or redo) - Alex](https://sourceforge.net/p/gramps/mailman/message/11952810/)[1](https://github.com/gramps-project/gramps/blob/master/gramps/gui/undohistory.py)

### Undo History dialog

![[_media/UndoHistory-dialog-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;Undo history&quot; dialog - example]] Shows a list of changes made so far in the Undo History list that allows you to / / a single transaction.

If you select button the dialog is shown "Are you sure you want to clear the Undo history?"

The list shows the "Original time" and "Action" made in each transaction.

Undo History dialog list spans all objects modifications.

The UndoHistory provides a list view with all the editing steps available for undo/redo. Selecting a line in the list will revert/advance to the appropriate step in editing history.

{{-}}

## Main Menus

![[_media/Menubar-MainMenuOverview-NoFamilyTree-Loaded-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menubar - Main Menu Overview - No Family Tree Loaded]]

The MenuBar shows the available Gramps Menu options.

Very abbreviated menus will be available before a Family Tree is loaded. They allow managing Family Trees; quitting Gramps; editing application-wide Preferences; enabling and disabling sections of the Graphical User Interface (GUI); and Help options.

{{-}} ![[_media/Menubar-MainMenuOverview-FamilyTree-Loaded-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menubar - Main Menu Overview - Family Tree Loaded]] After a Family Tree is loaded, the , , and menus will always have consistent options. But the availability of options of the other menus is context aware. Options in the , and menus change depending on the active Category and some menu items appear 'dimmed' when the selection objects in the view do not permit the action. {{-}} ![[_media/Menubar-MainMenuOverview-FamilyTree-Loaded-Active-Go-Windows-menus-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menubar - Main Menu Overview - Family Tree Loaded showing active &quot;&quot;, &quot;&quot; and &quot;&quot; menu entries in use]]

The and menus are specifically built of navigation links within each view.

A menu appears when there are any spawned windows or dialogs to be listed. {{-}} If available [keybindings](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings) are shown in the menubar menus next to the name of the function.

You can also select each of main menus using the [access key shortcuts](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings#Access_Key_Shortcuts) of key, plus the first left of each menu option eg: Pressing  + keys together will show the menu.

### 

![[_media/Menubar-FamilyTrees-overview-FamilyTree-Loaded-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menubar - "Family Trees" - overview example]]

- \- open the [Family Tree Manager Window](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees#Family_Trees_manager_window)

- \- a shortcut to opening a recently worked on Family Tree (Toolbar: [<big>▼ </big>Connect to a recent database](wiki:Gramps_6.0_Wiki_Manual_-_Navigation#.E2.96.BC_Connect_to_a_recent_database))

- \- backup and close the current Tree

<hr>

- \- Bring in data from other [formats](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees#Importing_data).  
  *Make a Backup before importing! There are [import Preferences](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Import) to mark imported data with timestamped [Tag](wiki:Gramps_Glossary#tag) and/or [Source](wiki:Gramps_Glossary#source) attributes. These options significantly slow down the Import process but are helpful for the ensuing data cleanup.*

- \- [Exporting data](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees#Exporting_data) allows you to share any portion of your Gramps Family Tree with other researchers as well as to enable you to transfer your data to another computer.

<hr>

- \- Menu only appears on most Views, if the displayed data can be exported. Gramps will export data on screen according your choice: **CSV** or **Open Document** spreadsheet format.

<hr>

- \- Allows you to make a [Full Gramps XML backup](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees#Backing_up_a_Family_Tree) of your currently opened Family Tree. Note [some configuration and Media items are omitted](wiki:Template:Backup_Omissions) from XML backups.

<hr>

- \- If you want to return your Family Tree to the way it was when you opened at the start of that session. (This is just like quitting without saving in other programs.) You will be shown the alert dialog.

- \- Exits your Gramps session and may start your [Autobackup](wiki:Gramps_6.0_Wiki_Manual_-_Error_and_Warning_Reference#Autobackup...) if setup.

{{-}}

### 

![[_media/Menubar-Add-a-new-object-overview-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menubar - "Add" (a new object) overview]]

- \- a new [object](wiki:Gramps_Glossary#primary_object)  
  also see [keybindings](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings).

<hr>

- \- adds a [Person](wiki:Gramps_Glossary#person) *([prim. obj.](wiki:Gramps_Glossary#primary_object))*

<hr>

- \- adds a [Family](wiki:Gramps_Glossary#family) *([prim. obj.](wiki:Gramps_Glossary#primary_object))* - Brings up the

<hr>

- \- adds an [Event](wiki:Gramps_Glossary#event) *([prim. obj.](wiki:Gramps_Glossary#primary_object))*

<hr>

- \- adds a [Place](wiki:Gramps_Glossary#place) *([prim. obj.](wiki:Gramps_Glossary#primary_object))*

- \- adds a [Source](wiki:Gramps_Glossary#source) *([prim. obj.](wiki:Gramps_Glossary#primary_object))*

- \- adds a [Citation](wiki:Gramps_Glossary#citation) *([prim. obj.](wiki:Gramps_Glossary#primary_object))*

- \- adds a [Repository](wiki:Gramps_Glossary#repository) *([prim. obj.](wiki:Gramps_Glossary#primary_object))*

- \- adds a [Media](wiki:Gramps_Glossary#media) *([prim. obj.](wiki:Gramps_Glossary#primary_object))*

- \- adds a [Note](wiki:Gramps_Glossary#note) *([prim. obj.](wiki:Gramps_Glossary#primary_object))*

<hr>

{{-}}

### 

If no family tree is loaded only the **Addon Manager...** and **Preferences...** entries are shown. ![[_media/Menubar-Edit-defaults-family-tree-loaded-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menubar - Edit Overview - default]] ![[_media/MenuEdit-SetHomePerson-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menubar - Edit - with family tree loaded]]

- \- The last edit you made. See [Using Undo History](wiki:Gramps_6.0_Wiki_Manual_-_Navigation#Using_Undo_History)

- \- Revert the last undo you did. See [Using Undo History](wiki:Gramps_6.0_Wiki_Manual_-_Navigation#Using_Undo_History)

- \- Open the dialog

<hr>

Additional menu options dependent on Category view will appear here.

- \- See [Tagging](wiki:Gramps_6.0_Wiki_Manual_-_Filters#Tagging)

<hr>

- \- The Clipboard tool provides a temporary notepad to store database records for easy reuse.

<hr>

- \- Third-party addons management

- \- Shows the dialog. That allows you to change most settings in Gramps.

- Additional menu options dependent on Category view will appear here.

{{-}}

### 

![[_media/Menubar-View-overview-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menubar - "View" - overview example]]

- \- Allows you to configure the active view. Provides options to hide, reveal and re-arrange elements. The same as clicking the ![[_media/Gramps-config.png]] button in the [Toolbar](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window#Toolbar).

- \- The Navigator is a sidebar container for the Navigator Category icons. When selected (default), the sidebar is shown on the left of the active View. Deselecting hides the Navigator sidebar. If all the Category icons cannot fit in the available vertical space, a hidden scrollbar will be created on the right of the sidebar and be revealed when rolled (hovered) over.  
  Text labels for the icons can be hidden via an option in the [Display](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Display) tab of Preferences. [Display modes](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window#Switching_Navigator_modes) can be selected from the pop-up menu at the bottom of the Navigator sidebar.

- \- show (or hide) a split screen container for (frequently used) action icons above the Category View. The selection of action icons varies to suit the Category view.  
  A [Third party Addon](wiki:Third-party_Addons) can be installed to supplement the Preferences with a [Theme](wiki:Addon:ThemePreferences) tab providing an option to show Text labels for each Toolbar button.

- \- Show (or hide) a split screen container for Gramplets to the right of the Category View.

- \- Show (or hide) a split screen container for Gramplets at the bottom of the window, just above the Status Bar.

- \- Expand window to use all available screen space while disabling the window dragging and resizing controls. Deselecting restores to previous size while re-enabling the window dragging and resizing controls.

<hr>

- Dependent on which view is active, other option menu items will appear here that can modify how the View organizes data.

{{-}}

### 

![[_media/Menubar-GoOverview-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menubar - "Go" Overview]]

- \- navigates the selection of the current View backwards to the *previous* item in your [Navigation history](wiki:Gramps_6.0_Wiki_Manual_-_Navigation#Using_history-based_Navigation)

- \- navigates the selection of the current View forward to the *next* item in your [Navigation history](wiki:Gramps_6.0_Wiki_Manual_-_Navigation#Using_history-based_Navigation)

<hr>

- \- navigates the [Active Person](wiki:Gramps_Glossary#active_person) focus to the individual [set](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Setting_Home_person) as the [Home Person](wiki:Gramps_Glossary#home_person)

<hr>

- Dynamic list of the most recent 10 records (People, Families, et cetera) selected, the List is dependent on the Category view being viewed.

{{-}}

### 

![[_media/Menubar-BookmarksOverview-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menubar - Bookmarks Overview]]

- \- Create a bookmark from the currently selected item eg: Person, Family etc..

- \- Opens the dialog.

<hr>

- ... - *Dynamic section where the bookmarks appear.*

{{-}}

### 

![[_media/Menubar-ReportsOverview-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menubar - Reports Overview]]

- \- The [Books Report](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_3#Books) allows you to create a custom genealogy book containing a collection of Gramps textual and graphical reports in a single document (i.e. a Book)

<hr>

- \-

  - 

  - 

  - 

- \-

  - 

  - 

  - 

  - 

  - 

  - 

  - 

- \-

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

  - 

- \-

  - 

  - 

{{-}}

### 

![[_media/MenuOverview-Tools-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "" Menubar - Tools Overview]]

- \-

  - 

  - \-

<hr>

- \- Menu only shown in developer mode. See [Debug](wiki:Gramps_6.0_Wiki_Manual_-_Tools#Debug) section.

  - 

  - 

  - 

  - 

  - \- moved to [Gramplets](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Python_Evaluation)

  - \- moved to [Gramplets](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Uncollected_Objects)

<hr>

- \-

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

- \-

  - 

  - 

  - 

  - 

  - 

- - 

  - 

  - 

  - 

{{-}}

### 

![[_media/Menubar-Windows-menu-overview-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menubar - "Windows" menu - overview example]]

- \- This menu provides quick access to opened windows you are working on.

{{-}}

### 

![[_media/Menubar-Help-overview-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menubar - "Help" - overview example]]

- \- Direct link to the online Gramps User manual you are viewing right now. Yes, you need an internet connection to consult the Gramps User Manual.

- \- A link to the [Frequently Asked Questions](wiki:Gramps_6.0_Wiki_Manual_-_FAQ) about Gramps.

- \- A link to the [Keybindings reference](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings) for Gramps. Also known as Keyboard shortcuts.

- \- Displays a dialog with a random hint about using the Gramps software.

- \- From this menu you can manage the built in plugins as well as any [Third-Party Addons](wiki:6.0_Addons) you may have installed.

<hr>

- \- This item opens your web browser and connects to the Gramps project web site.

- \- This item opens your web browser to the Gramps mailing list page. On this page, you can browse the mailing list archives and join the gramps-users mailing list so you can share your experiences with other Gramps user's.

- \- Choose this item to file a [bug report](wiki:Using_the_bug_tracker) in the Gramps bug tracking system. (This requires you to have a registered account on the Gramps bug reporting system) (Remember, Gramps is a living project. We want to know about any problems you encounter so we can work to solve them for you and everyone elses benefit.)

- \- A link to [Installing Third-Party Addons in Gramps](wiki:6.0_Addons).

<hr>

- \- This item displays a dialog with general information about the Gramps version you are running.

{{-}}

## Toolbar

![[_media/ToolbarIcon-OpenTheToolsDialog-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Tip for the Tools button of the Dashboard category toolbar]] The [Toolbar](wiki:Gramps_Glossary#toolbar) is a horizontal set of button controls located right below the menubar. It gives you access to the most frequently used functions of Gramps.

- The assortment of Toolbar buttons is "contextual" -- the icons shown depends on which Category [view](wiki:Gramps_Glossary#view) and [view mode](wiki:Gramps_Glossary#view_mode) is active
- Text labels are shown under the toolbar buttons.
- Hovering over a toolbar button shows a tip of its function.
- The Toolbar can be hidden or revealed by the option in menu .

{{-}}

### Common Toolbar buttons

#### ![[_media/Gramps.png]] Manage databases

![[_media/FamilyTrees-ManageDatabases-icon-toolbar-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure\|{{#expr:{{#var:figure}}+1}}}} Family Trees (Manage databases) - icon and tooltip on toolbar]] The ![[_media/16x16-gramps-pedigree.png]] button is the same as the menu option. The resulting dialog allow switching between Trees (genealogical databases), {{-}}

#### <big>▼ </big>Connect to a recent database

![Fig. {{#var:chapter}}.{{#vardefineecho:figure\|{{#expr:{{#var:figure}}+1}}}} "Connect to a recent database" toolbar button ](ConnectToARecentDatabase-icon-toolbar-60.png "Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Connect to a recent database" toolbar button ") This <big>▼ </big>button opens drop-down list from the toolbar.

See: [<big>▼ </big> Connect to a recent database](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees#.E2.96.BC_Connect_to_a_recent_database) section. {{-}}

#### ![[_media/Gramps_Go-Previous48x48_win.png]] Go to the previous object in the history

The ![[_media/Gramps_Go-Previous48x48_win.png]] toolbar button is an alternative to the menu option, or pressing the *Back* [keyboard keybinding](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings#Common_keybindings). It uses the [history based Navigation](#Using_history-based_Navigation) to shift the active object focus to the previously selected object in this category.

#### ![[_media/Go-next48x48_win.png]] Go to the next object in the history

The ![[_media/Go-next48x48_win.png]] toolbar button is an alternative to the menu option, or pressing the *Forward* [keyboard keybinding](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings#Common_keybindings). It uses the [history based Navigation](#Using_history-based_Navigation) to restore the active object focus shifted with the feature.

This button is only available after using the feature.

#### ![[_media/Gramps_Go-Home48x48_win.png]] Go to the home person

The ![[_media/Gramps_Go-Home48x48_win.png]] toolbar button is an alternative to the menu option, or pressing the *Home* [keyboard keybinding](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings#Common_keybindings). It shifts the [Active Person](wiki:Gramps_Glossary#active_person) focus to match the [Home Person](wiki:Gramps_Glossary#home_person).

This button is only functional if the Home Person has been set.

#### ![[_media/Gramps_Add48x48_win.png]] Add a new...

The toolbar button is an alternative to the menu option, or pressing the *Add* [keyboard keybinding](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings#Common_keybindings). It opens a blank Object Editor matching the object category of the current view.

####  Edit the selected...

The button is an alternative to the menu option, or pressing the *Edit* [keyboard keybinding](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings#Common_keybindings). It opens an Object Editor for each selected object in the category view.

#### ![[_media/Gramps_Remove48x48_win.png]] Delete the selected...

The toolbar button is an alternative to the menu option, or pressing the *Delete* [keyboard keybinding](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings#Common_keybindings). It opens a Delete confirmation dialog.

The item that is about to be deleted is identified. If multiple items were selected, a dialog appears for each. A checkbox option offers to "Use this answer for the rest of the items".

#### ![[_media/Gramps_Merge48x48_win.png]] Merge the selected...

This toolbar button is an alternative to the menu option. It opens the [Merge dialog](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data%3A_detailed_-_part_3#Merging_records) for that particular category of records.

Successful use of the Merge button is only possible if two (and only 2) records are selected in the view.

#### ![[_media/gramps-tag.png]] Tag the selected rows

This toolbar button is an alternative to the submenu.

The ![[_media/16x16-gramps-tag.png]] button reveals a pop-up menu with the following [Tag](wiki:Gramps_Glossary#tag) options:

- [New tag...](wiki:Gramps_6.0_Wiki_Manual_-_Filters#New_Tag_dialog)
- [Organize tags...](wiki:Gramps_6.0_Wiki_Manual_-_Filters#Organize_Tags_Window)

Followed by a list of currently available tags that can be applied to the selected objects in the view.

[Tags are used for](wiki:Gramps_6.0_Wiki_Manual_-_Filters#Usage_of_tags) color coding rows in list views, marker swatches on some charts, and persistent markers for filtering and organization.

#### ![[_media/Gramps_Clipboard48x48_win.png]] Open the Clipboard dialog

![[_media/Clipboard-dialog-example-context-menu-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Clipboard - dialog - showing (right click) Context menu]] This toolbar button is an alternative to the menu option, or pressing the *Clipboard* [keyboard keybinding](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings#Common_keybindings). It opens the [Clipboard](wiki:Gramps_6.0_Wiki_Manual_-_Navigation#Using_the_Clipboard) dialog without adding the selected object to its collection. {{-}}

#### ![[_media/Gramps-config.png]] Configure the active view

This toolbar button is an alternative to choosing the menu option, or pressing the *Configure active view* [keyboard keybinding](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings#Common_keybindings).

Most Category views have a ⚙ Configurable Options. Clicking this button opens the dialog with the controls for adjusting those options.

This option opens a dialog with choices for displaying records in the View. (The dialog will also have tabs for any [Gramplets which have configurable options](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#.E2.9A.99_Configurable_Options_2) that are active in the view.)

#### ![[_media/Gramps-reports.png]] Open the reports dialog

![[_media/ReportSelection-dialog-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Report Selection - dialog]] This is a persistent alternative to using the submenus.

By presenting the available Reports in a floating dialog, room is available for describing each Report, its status and contributing developer information. The dialog also allows exploration of Reports to be more structured. {{-}}

#### ![[_media/Gramps-tools.png]] Open the tools dialog

![[_media/ToolSelection-dialog-example-with-debug-menu-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Tool Selection - dialog]] This is a persistent alternative to using the submenus.

By presenting the available Tools in a floating dialog, room is available for describing each Tool, its status and contributing developer information. The dialog also allows exploration of Tools to be more structured.

{{-}}

#### ![[_media/Gramps-addon.png]] Open Addon Manager

![[_media/AddonManager-addons-listing-60.png|Right|thumb|550px|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} <strong>Addon Manager</strong> dialog example]]

- \- The Addon Manager provides a way to explore which Addons will enhance your personal workflows.

{{-}}

#### ![[_media/Gramps-preferences.png]] Open Preferences

![[_media/EditPreferences-Data-tab-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menu: "Edit -&gt; Preferences..." example]]

- \- Most of the settings affecting the entire Gramps program are configured in the Preferences dialog.

{{-}}

[Category:Documentation](wiki:Category:Documentation)
