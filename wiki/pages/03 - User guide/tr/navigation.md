---
title: Gramps 6.0 Wiki Manual - Navigation/tr
categories:
- Documentation
- Stub
managed: false
source: wiki-scrape
wiki_revid: 122699
wiki_fetched_at: '2026-05-30T20:58:50Z'
lang: tr
---

{{#vardefine:chapter\|10}} {{#vardefine:figure\|0}} As long as any [Family Tree](wiki:Gramps_Glossary#family_tree) database is open, Gramps is focused on a single person usually referred to as an [Active Person](wiki:Gramps_Glossary#active_person). This allows you to view or modify the data concerning this person, his or her immediate family, etc. [Navigating in the Family Tree](wiki:Gramps_6.0_Wiki_Manual_-_Navigation#Setting_the_Active_Person) database (i.e. moving from person to person) is in fact nothing else but changing the Active Person.

This section describes many alternative ways to navigate through the database using both the complex and the convenient interfaces Gramps provides. All these ways fundamentally accomplish the same result, but some methods of navigating will be more convenient than others... depending on what you are doing in Gramps at the moment.

## Using the People Category

The most intuitive way to select an Active Person is to use the [People Category](wiki:Gramps_6.0_Wiki_Manual_-_Categories#People_Category). When in the People Category, just select the name of the desired person from the list by clicking that list entry. The person you have selected becomes active. The statusbar updates to reflect the change of the active person.

See also

- [Editing information about people](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1#Editing_information_about_people)

## Using the Relationships Category

When in the [Relationships Category](wiki:Gramps_6.0_Wiki_Manual_-_Categories#Relationships_Category), you can easily navigate between the members of the displayed family as follows:

Click on the underlined name of the person you want to go to and this person will be the new active person of the Relationships Category.

The name of the currently active person is not underlined.

In addition to this, Gramps provides an extensive set of keyboard navigation options. The detailed reference to the key bindings is found in the [Appendix B: Keybindings reference](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings).

## Using the Families Category

When in the [Families Category](wiki:Gramps_6.0_Wiki_Manual_-_Categories#Families_Category), you can easily navigate between the displayed families.

## Using the Charts ![[_media/22x22-gramps-pedigree.png]] Category

![[_media/TimelinePedigreeView-Addon-Existing-Person-ContextMenu-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Timeline Pedigree View - 3rd Party Addon for Charts Category - context menu example]] Gramps relies heavily on form-based layouts of linked list items. These imply relationships between records in your family Tree. The **Charts Category** provides an alternative, more visual, way of representing those relationships. The positions, shapes, and colors of containers along with their connecting lines & arrows can show an extra depth of interrelation with different factors. Containers can be simple color filled boxes, arcs, ribbons, or many other shapes.

But the [Charts Category](wiki:Gramps_6.0_Wiki_Manual_-_Categories#Charts_Category) also provides an alternative way to navigate through the family tree. The benefit of this method is that you can see more than one generation of the family tree. So you can jump directly from a great-grandson to a great-grandfather without going through the intermediate generations.

Note that after changing the [Active Person](wiki:Gramps_Glossary#active_person) in the Charts Category, the Chart View is re-adjusted to the newly selected Active Person focus. When in the Charts Category, you can easily navigate between the members of the displayed family tree as follows:

To make any displayed person the Active Person focus, left-click their corresponding container. Right-clicking the container will invoke a context menu with options appropriate to contents.

The a context menu for a Person container may contain ▶sub-menus listing all spouses, siblings, children, and parents of the corresponding Person. The first entry in the context menu will usually be the name of the Person in that container. (It could alternately be an Edit option.) Selecting the Person name will shift focus in the same way as left-clicking the container. You can also change the Active Person focus to any of the spouses, siblings, children, or parents of any displayed person.

Some charts views have an obvious navigational correlation. Moving through generations intuitively matches moving to the left, right, upwards or downwards in the chart. These may have custom directional navigation buttons to allow navigation by clicking rather than dragging.

As an example, to change the focus of the [Pedigree View](wiki:Gramps_6.0_Wiki_Manual_-_Categories#Pedigree_View) to a child (if any exists) of the current Active Person, click the (*Left Arrowhead*) button to the left of the Active Person’s chart box. If there is only one child, the focus changes immediately. If the Active Person has more than one child, the (*Left Arrowhead*) button expands with a pop-up menu with a selectable list of the children. (For this particular (*Left Arrowhead*) button, the pop-up menu list of Children is sorted by that Parent‘s Marriage order, sub-sorted by Birth order. These [orders can be changed](wiki:Gramps_6.0_Wiki_Manual_-_FAQ#How_do_I_change_the_order_of_children.3F) globally in the Relationships category.)

Like containers, buttons may have alternate features accessed by right-clicking and choosing from a contexual pop-up menu.

Other buttons are less obvious aids to navigating to not People but features of Gramps. Using the [Pedigree View](wiki:Gramps_6.0_Wiki_Manual_-_Categories#Pedigree_View) example again, rolling over the lines between boxes shows a hint with any known basic details about the relationship and double-clicking those lines opens the editor for that Family. And double-clicking the Active Person box opens the editor for that Person. It is well worth reading the detailed documentation on each Chart View to discover these hidden shortcuts to favorite features.

The built-in Views of the [Chart Category](wiki:Gramps_6.0_Wiki_Manual_-_Categories#Charts_Category) are introduced in the [Categories](wiki:Gramps_6.0_Wiki_Manual_-_Categories) reference section. Some are described in greater depth in articles listed at the bottom of the View’s introductory section.

The collection of Views in the Charts Category can be expanded with 3rd Party Addons using the [Plug-in Manager](wiki:Gramps_6.0_Wiki_Manual_-_Plugin_Manager) feature of Gramps. The available 3rd Party Addon plug-ins can be found under the **View** column of the [list of Addons](wiki:6.0_Addons#Addon_List) table. The maintenance of a few 3rd Party Addon Views has been adopted by the Gramps volunteer team over the years. These became 'built-in' after being vetted and then included in the main Gramps distributions. Articles about using each Addon View are linked to the label **Plugin/Documentation** column. The quality of documentation varies dramatically for these articles.

## Using Gramplets

![[_media/DashboardCategory-DashboardView-default-gramplets-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Dashboard Category view - with example Gramplets shown]]

On the [Sidebar and bottombar](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#The_split-screen_Sidebar_.26_Bottombar), you can add Gramplets to expand your navigation options beyond a single generation's distance. Some examples are:

- [Relatives](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Relatives)
- [Descendants](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Descendants)
- [Pedigree](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Pedigree)
- [Fan Chart](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Fan_Chart)

These examples provide the ability to navigate the Active Person focus with using the perspective of familial relationship... to nearby relatives, descendants or ancestors. Future Gramplets might allow navigating by geographical proximity, [DNA matching](wiki:Addon:DNASegmentMapGramplet) or some other connection we haven't yet considered.

The text based Gramplets tend to have names [hotlinked for navigation](#Hotlink_Navigation) while the graphical ones may use [contextual menus](#Contextual_Menu_Navigation). {{-}}

## Setting the Home Person

One (and only one) person in the Family Tree database can be designated as the [Home Person](wiki:Gramps_Glossary#home_person). Once the Home Person is designated, returning the [Active Person](wiki:Gramps_Glossary#active_person) focus to that person becomes a matter of a single click, regardless of which Category is being used at the moment.

To set the Home Person, first [navigate](wiki:Gramps_6.0_Wiki_Manual_-_Navigation#Setting_the_Active_Person) to that person using any method you like. Then choose the People category and select the menu . Once this is done, you can move to the Home Person from anywhere in the database by simply clicking the Toolbar icon. You can also choose the menu or select item from any context menu available on the right click or use the keyboard shortcut .

- [Settings#Setting Home Person](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Setting_Home_person)
- On the [Edit Person dialog](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1#Edit_Person_dialog) you can select "Make Home Person" from the context menu.

## Setting the Active Person

The [Active Person](wiki:Gramps_Glossary#active_person) is expected to be the contextual focus of actions, reports and edits.

There is a selection highlight as a visual cue of the Active Person in the People View. In the Relationship View, the Active Person is shown in a separate section at the top. All other persons shown below have an immediate (parent, sibling, spouse, child) relationship with the Active Person.

### Hotlink Navigation

Normally, simply clicking on the hotlinked name of a Person will select that person and shift this Active Person contextual focus.

![[_media/Relationships-category-view-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Relationships Category view]]Each Person's name in the Person and Relationship category views is a hotlink. Changing the Active Person focus in Person view appears to merely change which record is highlighted. But this also causes Gramplets contents to be updated and the Relationship, Charts & Geography views to be re-focused on the new Active Person.

Selecting a different hotlinked name in the Relationship category view causes a less subtle change. The perspective of how the family data is represented changes towards that focus. Their details move to the top section and their immediate family are re-arranged below.

{{-}}

### Contextual Menu Navigation

However, hotlinked names in the References tab and Notes (and in some Gramplets) will merely open the Person Editor window *without* navigating the Active Person focus to that Person. (These links behave as though you had clicked an button instead of a hotlinked name.) This facilitates quickly editing Persons around the Active Person without the disorientation of a shifting focus.

![[_media/QuickViewReport-EditPerson-context-menu-popup-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Context menu on the Person editor]] The Active Person focus can be set while in the [Edit Person dialog](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1#Edit_Person_dialog) by using the context menu (right-clicking) in the empty space of the header area. The option in that context menu changes the Active Person focus to the Person being edited.

{{-}}

### Using history-based Navigation

![[_media/History-based-navigation-tools-Go-menu-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Example of the history based navigation tools]]

Gramps also features a powerful set of history-based navigation tools. These tools are similar to those commonly used in web browsers.

They include and items available from the menu, context menus (available in People, Family, and Pedigree Categories), and the toolbar buttons. They also include the list of the recent selections available under the menu that allows you to jump directly to any of the recent selections. Finally, right-clicking on the and toolbar buttons invokes the popup menu with corresponding portion of the history. Select any item from the menu to jump directly to it. {{-}}

### Bookmark Navigation

![[_media/Gramps_Go-Home48x48_win.png]] The Home button on the toolbar is a special case bookmark. It shifts the Active Person focus to the Person currently designated as the [Home Person](wiki:Gramps_Glossary#Home_Person). This is so frequently useful that this feature also has a [keybinding](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings#Common_keybindings).

Similar to setting the Home Person, you can bookmark other people from the database to simplify further navigation. To bookmark a person, first navigate to that person, then choose the menu . To move to that person elsewhere in the database, choose the menu from the list of bookmarked names shown. The other categories have their own list of Bookmarks.

![[_media/OrganizeBookmarks-dialog-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Organize Bookmarks]]

You can manage your bookmarks by choosing the menu or [keybinding](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings) . This opens the dialog with the list of bookmarks and the controls to modify this list.

Use the and buttons to change the list sequence. Use the button to remove a Bookmark. The will bring you to this page, and you close the window with the button.

The list of Bookmarked People can be selected through the People Category, as explained above, but is also shared with the Relationships and Charts Categories.

On a similar basis, separate lists of Bookmarks are maintained in each of the following Categories: Families, Events, Places, Sources, Citations, Repositories, Media, and Notes.

{{-}}

### Notes as Navigational Shortcuts

![[_media/Note-showing-tooltip-for-link-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Notes Editor - Linking text]] There are separate Bookmarks lists in several categories. But they are still just simple lists. Long lists of bookmarks quickly become unwieldy.

Persistent Links can be created in [Notes](wiki:Gramps_Glossary#note). Use the [Link Editor](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_2#Link_Editor) in Notes to organize navigation links to different types of Gramps records following to your own organization methods. Once a Note has linked text, that linked record can be used like a Bookmark. Navigate to that record by holding the key and clicking on the Linked Text. One note be used as a Linked Index to other Notes with different sets of Links.

An example of a linked note might include an obituary where all the Persons, Places or even the Events are Linked. This makes it easier to navigate to the indirectly related (or even unrelated) pallbearers, funeral [officiators](wiki:Gramps_Glossary#officiator), or attendees.

Another note might be the transcribed bibliography for the published original research of another genealogist. As you collect digital copies of those originally cited references, the linked bibliography can be used as a Source acquisition checklist. When completely Linked, the Bibliography can be use to navigate through Sources for each citation while searching for unsupported conclusions, inaccuracies or omissions.

{{-}}

## Finding records

![[_media/Find-type-ahead-search-PeopleTreeView-list-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Find people list view using Interactive search type ahead - example]]

To find a record in one of the category list views, first switch to the appropriate category that provides the list of the desired records: People, Sources, Places, or Media. Select a line in the list to gain focus and then start typing the name of a person or the title of a Source, Place, or Media object that you are looking for, respectively.

Alternatively, select a line in the list to gain focus and then you may press to turn on the search mode textbox. However, simply starting to type is also enough to both open the box and start entering the search term.

As you type, the first matching record in the sort column of the list will scroll to the center of the list and be selected. As you type more characters, the match will be refined. As long as the search mode text box is visible, pressing the down arrow cursor key will move to the next match while pressing the up arrow cursor control key will move to the previous match. The box disappears after it is idle. (When there have been no keystrokes for between 5 and 15 seconds.) Without the Find box active, the cursor control keys revert to moving the records selection up and down the list.

Changing the sort column (by clicking on the header) also changes the column being matched. {{-}}

## Using the Clipboard

![[_media/Clipboard-dialog-example-context-menu-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Clipboard - dialog - Showing Context menu (right click) example]]

For an application like Gramps the is very important as it will help reduce repetitive data entry.

The tool provides a temporary notepad to store database records for easy reuse during a single Gramps session eg: until you exit Gramps. In short, this is a sort of the copy-and-paste functionality extended from textual objects to other types of records used in Gramps. Clipboard makes extensive use of the [*drag and drop*](http://en.wikipedia.org/wiki/Drag-and-drop) technique

To invoke the , either choose the menu or click the Toolbar button or use the [Keyboard shortcut (accelerator key)](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings#8) .

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

## Ana Menü

![[_media/Menubar-MainMenuOverview-NoFamilyTree-Loaded-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menubar - Main Menu Overview - No Family Tree Loaded]] ![[_media/Menubar-MainMenuOverview-FamilyTree-Loaded-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menubar - Main Menu Overview - Family Tree Loaded]] ![[_media/Menubar-MainMenuOverview-FamilyTree-Loaded-Active-Go-Windows-menus-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menubar - Main Menu Overview - Family Tree Loaded showing &quot;Active&quot; and &quot;Windows&quot; menu entries in use]]

The MenuBar shows the available Gramps Menus that change and appear depending on the Category used eg: Edit / View.

{{-}}

### 

![[_media/Menubar-FamilyTrees-overview-FamilyTree-Loaded-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menubar - "Family Trees" - overview example]]

- \- open the [Family Tree Manager Window](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees#Family_Trees_manager_window)

- \- a shortcut to opening a recently worked on Family Tree

- \- backup and close the current Tree

<hr>

- \- Bring in data from other [formats](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees#Importing_data).  
  *Make a Backup before importing! There are [import Preferences](wiki:Gramps_6.0_Wiki_Manual_-_Settings#General_Gramps_settings) to mark imported data with timestamped [Tag](wiki:Gramps_Glossary#tag) and/or [Source](wiki:Gramps_Glossary#source) attributes. These options dramatically slow the Import process but are helpful for the ensuing data cleanup.*

- \- [Exporting data](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees#Exporting_data) allows you to share any portion of your Gramps Family Tree with other researchers as well as to enable you to transfer your data to another computer.

<hr>

- \- Menu only appears on most Views, if the displayed data can be exported. Gramps will export data on screen according your choice: **CSV** or **Open Document** spreadsheet format.

<hr>

- \- Allows you to make a [Full Gramps XML backup](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees#Backing_up_a_Family_Tree) of your currently opened Family Tree. Note [some configuration and Media items are omitted](wiki:Template:Backup_Omissions) from XML backups.

<hr>

- \-

- \-

{{-}}

### 

![[_media/Menubar-Add-a-new-object-overview-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menubar - Add Overview]]

- \- a new [object](wiki:Gramps_Glossary#primary_object)  
  also see [keybindings](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings).

<hr>

- \- adds a [Person](wiki:Gramps_Glossary#person) *([prim. obj.](wiki:Gramps_Glossary#primary_object))*

- \- adds a [Family](wiki:Gramps_Glossary#family) *([prim. obj.](wiki:Gramps_Glossary#primary_object))* - Brings up the

- \- adds an [Event](wiki:Gramps_Glossary#event) *([prim. obj.](wiki:Gramps_Glossary#primary_object))*

- \- adds a [Place](wiki:Gramps_Glossary#place) *([prim. obj.](wiki:Gramps_Glossary#primary_object))*

- \- adds a [Source](wiki:Gramps_Glossary#source) *([prim. obj.](wiki:Gramps_Glossary#primary_object))*

- \- adds a [Citation](wiki:Gramps_Glossary#citation) *([prim. obj.](wiki:Gramps_Glossary#primary_object))*

- \- adds a [Repository](wiki:Gramps_Glossary#repository) *([prim. obj.](wiki:Gramps_Glossary#primary_object))*

- \- adds a [Media](wiki:Gramps_Glossary#media) *([prim. obj.](wiki:Gramps_Glossary#primary_object))*

- \- adds a [Note](wiki:Gramps_Glossary#note) *([prim. obj.](wiki:Gramps_Glossary#primary_object))*

<hr>

{{-}}

### 

![[_media/Menubar-Edit-defaults-family-tree-loaded-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menubar - Edit Overview]]

- \-

- \-

- \- Open the dialog

<hr>

Additional menu options dependent on Category view will appear here.

- \- See [Tagging](wiki:Gramps_6.0_Wiki_Manual_-_Filters#Tagging)

<hr>

- \- The Clipboard tool provides a temporary notepad to store database records for easy reuse.

<hr>

- \- Shows the dialog. That allows you to change most settings in Gramps.

- Additional menu options dependent on Category view will appear here.

{{-}}

### 

![[_media/Menubar-View-overview-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menubar - "View" - overview example]]

- \- Etkin görünümü yapılandırmanıza izin verir. Öğeleri gizleme, ortaya çıkarma ve yeniden düzenleme seçenekleri sunar.

- \- Gezgin, Gezgin Kategorisi simgeleri için bir kenar çubuğu kabıdır. Seçildiğinde (varsayılan), kenar çubuğu etkin Görünümün solunda gösterilir. Seçimin kaldırılması Gezgin kenar çubuğunu gizler. Tüm Kategori simgeleri mevcut dikey alana sığamazsa, kenar çubuğunun sağ tarafında gizli bir kaydırma çubuğu oluşturulur ve üzerine gelindiğinde (fareyle üzerine gelindiğinde) ortaya çıkar.  
  Simgeler için metin etiketleri, Tercihler'in [Görüntüle](wiki:Gramps_6.0_Wiki_Manual_-_Settings/tr#Görüntüle) sekmesindeki bir seçenek aracılığıyla gizlenebilir. Gezgin kenar çubuğunun altındaki açılır menüden [Görüntüleme modları](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window/tr#Gezgin_modları_arasında_geçiş_yapma) seçilebilir.

- \- Kategori Görünümünün üzerinde (sık kullanılan) eylem simgeleri için bölünmüş ekran kapsayıcısını gösterin (veya gizleyin). Eylem simgelerinin seçimi, Kategori görünümüne göre değişir.  
  Tercihler'i, her Araç Çubuğu düğmesi için Metin etiketlerini gösterme seçeneği sunan bir [Tema](wiki:Addon:ThemePreferences/tr) sekmesi ile desteklemek üzere bir [Üçüncü taraf Eklenti](wiki:Third-party_Addons/tr) yüklenebilir.

<!-- -->

- \- Show (or hide) a split screen container for Gramplets to the right of the Category View.

- \- Show (or hide) a split screen container for Gramplets at the bottom of the window, just above the Status Bar.

- \- Expand window to use all available screen space while disabling the window dragging & resizing controls. Deselecting restores to previous size while re-enabling the window dragging & resizing controls.

<hr width=25%>

- Dependent on which view is active, other option menu items will appear here that can modify how the View organizes data.

{{-}}

### 

![[_media/Menubar-GoOverview-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menubar - Go Overview]]

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

- \- Opens the [Organize Bookmarks](wiki:Gramps_6.0_Wiki_Manual_-_Navigation#Bookmark_Navigation) window.

<hr>

- Dynamic section where the bookmarks appear

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

- \-

  - 

  - 

  - 

  - 

  - \-

  - \-

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

![[_media/Menubar-Windows-menu-overview-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menubar - "Windows" - overview example]]

- \- This menu provides quick access to opened windows you are working on.

{{-}}

### 

![[_media/Menubar-Help-overview-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menubar - "Help" - overview example]]

- \- Direct link to the online Gramps User manual you are viewing right now. Yes, you need an internet connection to consult the Gramps User Manual.

- \- A link to the [Frequently Asked Questions](wiki:Gramps_6.0_Wiki_Manual_-_FAQ) about Gramps.

- \- A link to the [Keybindings reference](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings) for Gramps. Also known as Keyboard shortcuts.

- \- Displays the "Tip of the day" dialog.

- \- From this menu you can manage the built in plugins as well as any [Third-Party Addons](wiki:6.0_Addons) you may have installed.

- \- This item opens your web browser and connects to the Gramps project web site.

- \- This item opens your web browser to the Gramps mailing list page. On this page, you can browse the mailing list archives and join the gramps-users mailing list so you can share your experiences with other Gramps user's.

- \- Choose this item to file a [bug report](wiki:Using_the_bug_tracker) in the Gramps bug tracking system. (This requires you to have a registered account on the Gramps bug reporting system) (Remember, Gramps is a living project. We want to know about any problems you encounter so we can work to solve them for you and everyone elses benefit.)

- \- A link to [Installing Third-Party Addons in Gramps](wiki:6.0_Addons).

<!-- -->

- \- This item displays a dialog with general information about the Gramps version you are running.

## Araç çubuğu

- Toolbar: The [Toolbar](wiki:Gramps_Glossary#toolbar) is located right below the menubar. It gives you access to the most frequently used functions of Gramps.
- The assortment of Tool buttons shown depends on which Category [view](wiki:Gramps_Glossary#view) is active
- ⚙ Configurable Options: most Category views have a ![[_media/Gramps-config.png]] button as an alternative to choosing the from the View menu, or pressing the *Configure active view* [keyboard keybinding](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings#Common_keybindings). This option opens a dialog with choices for displaying records in the View. (The dialog will also have tabs for any added [Gramplets which have configurable options](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#.E2.9A.99_Configurable_Options_2).)
- Hovering over a toolbar icon shows a tip of its function

![[_media/ToolbarIcon-OpenTheToolsDialog-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Tip for the Tools button of the Dashboard category toolbar]] The Toolbar can be hidden or revealed by the option in menu .

.{{#vardefineecho:figure\|{{#expr:{{#var:figure}}+1}}}} Added Theme tab options for the Preferences dialog.\]\]}}

{{-}} ![[_media/FamilyTrees-ManageDatabases-icon-toolbar-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure\|{{#expr:{{#var:figure}}+1}}}} Manage databases - icon on toolbar (Same as using menu )]] {{-}} ![[_media/ConnectToARecentDatabase-icon-toolbar-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure\|{{#expr:{{#var:figure}}+1}}}} Connect to a recent database - icon drop down on toolbar menu]] {{-}}

{{-}}

[Category:Documentation](wiki:Category:Documentation)
