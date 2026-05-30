---
title: 'Gramps 6.0 Wiki Manual - Entering and editing data: brief'
categories:
- Documentation
managed: false
source: wiki-scrape
wiki_revid: 120905
wiki_fetched_at: '2026-05-30T11:10:43Z'
---

{{#vardefine:chapter\|8}} {{#vardefine:figure\|0}} This section is provides the basic knowledge necessary to start entering your genealogical information into Gramps. It will explain how to enter people into your family tree (also called a database) and how to specify their family relationships. (A more detailed explanation will follow in the next chapter: [Gramps 6.0 Wiki Manual - Entering and editing data: detailed](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed).)

First, let us identify the types of information you can enter into your family tree using Gramps. These include:

- Personal information about an individual (names, addresses, birth and death dates, etc.)
- Information about an individual's relationships (marriages, divorces, civil unions, etc.)
- Information about an individual's parents and children
- Sources that document your research

Now let us explore how you can enter and edit these various types of genealogical information.

## To add or edit a person

The [menu](wiki:Gramps_6.0_Wiki_Manual_-_Navigation#Add) for each [Category](wiki:Gramps_Glossary#category) [View](wiki:Gramps_Glossary#view) includes the option to add a [Person](wiki:Gramps_Glossary#person). A [keybinding](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings#Common_keybindings) for adding a Person is also supported in all categories views.

There are multiple ways to add a new person to your family tree. Many have an implied context which saves a step in grafting the Person into a Tree. (e.g., adding a Person from within the Family context of the Relationships or Charts views automatically inserts the new Person into the Family. You don't have to create the Person as a separate action, then subsequently find and drag the new Person into that Family.) We will cover some of the different workflows as we proceed. {{-}}

### Add a new person

![[_media/PeopleTreeView-GroupedPeople-example-with-context-menu-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} People Category - Tree View - Grouped People]]

The most obvious way to insert a person in your tree is to add them from the View. While you are in the View, click the Toolbar button.

{{-}} ![[_media/Edit-person-window-new-person-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Edit Person - window - New empty editor]]

The dialog will be shown and you can enter any data you know about this person then select to save the new person.

{{-}}

### Edit an existing person

![[_media/Edit-person-window-existing-person-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Edit Person - window - Existing person example]]

To edit information about a person already present in the family tree, select the person from the View and click the Toolbar button.

People can also be added to the family tree in the View, dialog, and other places where it makes sense.

{{-}}

## To specify a relationship

There are two primary ways to specify relationships between people:

\(1\) By family:

  
<li>

using the View. The View is usually used to build multiple relationships around a single person.

</li>

<li>

using the dialog from the View. The is usually used to build all the Relationships within a single family at a time.

</li>

</ol>

\(2\) By association:

  
<li>

using the tab of the dialog. Adding a Person and specifying the type of Association (godparent, coworker, pallbearer, childhood friend, etc.) identifies an interpersonal relationship.

</li>

<li>

using the feature of the dialog. Cross-referencing a person via a Person link in a Note will associate that linked person to the person where the note is attached.

</li>

<li>

Persons who share a reference (sources, notes, colocated in the same places, etc.) have an indirect or proximal relationship.

</li>

</ol>

{{-}}

### Specifying a relationship using the Relationships View

![[_media/Relationships-category-view-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Relationships View]]

To specify a new relationship to the [Active Person](wiki:Gramps_Glossary#active_person), switch to the View and you will see this individual indicated as the "Active Person". Next to the label is a button (typically represented by a sign).

{{-}}

![[_media/FamilyEditor-dialog-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Editing a family]]

Clicking the button will display the dialog with the Active Person set as either the father or the mother.

{{-}}

![[_media/SelectMother-selector-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Select Mother - dialog]]

Now a question ?  
Does the person who will form the relationship with the Active Person already exist in the family tree? If yes, click the button for the other person. You will then be able to browse through the list of people in the family tree to select the one you want. If not, click the button; this will allow you to add a new person to the family tree and to specify the relationship this person has to the Active Person.

To edit an existing relationship from the View, click on the button next to corresponding Family entry. If there is more than one relationship in the list, you can select the spouse or partner you want by clicking the corresponding button next to the relationship.

{{-}}

### Specifying a relationship using the Families List View

To specify a new relationship in the View, click on the button on the toolbar, and an empty dialog will open. At this point, you can add people to the family.

{{-}}

## To specify parents

You can specify the Active Person's parents in the View (See  - selector). A little care is required to prevent the creation of . If you wish to add the Active Person to an already existing family, you should click the button. If the family including the parents does not already exist, you should click the button.

{{-}} ![[_media/SelectFamily-SelectorDialog-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Select Family - selector dialog example]]

If you click on the button, you are presented with the dialog. This will allow you to select the existing family, and then the Active Person will be added as a child to the family.

If you click on the button, a new dialog is presented with the Active Person listed a child of the new family. You can add the parents to the family by either adding new people as the parents or selecting existing people as the parents.

{{-}} You can also specify the parents of a person in the View. If the family already exists, click on the Toolbar button and add the person as a child when the dialog is displayed. If the family does not already exist, click the button to create a new family, and add the appropriate parents and children.

{{-}}

## To specify children

Adding children to a relationship is done through a similar procedure. From the View or the View, select the existing family or create a new family. Children can be added by selecting the button or button to the right of the child list.

Clicking the button will display the dialog, allowing you to enter a new person. Clicking on the button, will allow you to select an existing person from a list. By default, the child is added with the relationship type of **birth** to both parents.

{{-}} ![[_media/ChildReferenceEditor-dialog-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;Child Reference Editor&quot;]]

If you wish to change the parent/child relationship from the default setting of **Birth**, from the dialog select the child and click on the . This will display the dialog.

{{-}} If you wish to change the order of the children in the family, use the arrows or the [*drag and drop*](http://en.wikipedia.org/wiki/Drag_and_drop) function on s tab. {{-}}

## Adding photos and other media objects

Various types of media objects (including photos, documents, audio files, and video files) can be attached as [secondary objects](wiki:Gramps_Glossary#secondary_object). You can also add images that might not be limited to a single person or event. (For example, group photos from a family reunion)

Gramps supports various types of media objects including photos, documents, audio files, and video files. The most common method for adding media is through the tab of a primary object's editor (such as People, Events, Families, Places, Citations, Sources, or Repositories).

Before adding any ***new*** Media Objects, you should be double-check the in the tab of Preferences. While checking, confirm that you have used context menu so that there is a button for that 'Base Media Path' in the [File Chooser](wiki:Gramps_6.0_Wiki_Manual_-_Settings#File_Chooser).

Adding optional information can help categorize your media for easier searching later. Dates, titles, and [Tags](wiki:Gramps_Glossary#tag) can be added a media object.

1.  Open the object editor for the primary object
2.  Select the Gallery tab.
3.  To add a new Media object, click the button
    - Navigate to the file in the File Chooser, decide whether to use the "Convert to a relative path" option
    - click the button.
4.  To [share](wiki:Gramps_Glossary#sharing) an existing media object, click the button
    - Select an existing Media object from the [Select Media Object](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1#Select_Media_Object_selector) dialog
    - double-click the object or click the button.
5.  Add optional information
    - if the Media object is an image, drag a rectangle in the Preview to refine the thumbnail contents
6.  expand the section, then add helpful details
    - user-friendly **Title**
    - **Date** : the Media object was created or that the media object represents
    - select Tags
7.  click the button.

When adding a few media objects, it may be more efficient to use the category View and add them. Then use the button to link to various primary objects as needed.

### Using the Clipboard

![[_media/Clipboard-dialog-example-context-menu-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Clipboard - dialog - Showing Context menu (right click) example]] If adding more than a few objects, consider using the feature in the [<strong>Media Manager</strong>](wiki:Gramps_6.0_Wiki_Manual_-_Tools#Media_Manager) from the menu. the category to show Last Changed, sort to the new items and copy them to the [Clipboard](wiki:Gramps_Glossary#clipboard).

The Clipboard allows quick drag'n'drop to Object Editor galleries. However, when adding a media object to multiple Galleries, sharing "Media ref" can be more efficient than rather than having a separate copy of the Media object reference. After dropping a Media Object in a Gallery, copy the Media object in the Gallery back to the clipboard. This creates a "Media ref" for that object. Then clear the original Media object from the clipboard.

Use consistent naming conventions for your media files and add detailed descriptions to make searching easier. Remember to regularly backup your media files along with your Gramps database.

{{-}} ![[_media/PersonView-PeopleListView-example-with-context-menu-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;People&quot; Category - &quot;Person View&quot; - &quot;People&quot; (List) View showing context menu]]

If you want to add an image to a single person, switch to the View (See Fig. {{#var:chapter}}.{{#expr:{{#var:figure}}}}), select a person, and then click the icon on the toolbar. {{-}}

![[_media/Edit-person-window-existing-person-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Edit Person]]

This will bring up the dialog (See Fig. {{#var:chapter}}.{{#expr:{{#var:figure}}}}). Next, select the tab, and click the button to call up the dialog. Type a filename or browse to find the image file you want and then provide a title for that image. Keep adding images until you are done.

{{-}} ![[_media/Families-category-list-view-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Families category view]]

To add images related to a relationship (for example, a marriage), switch to the View (See Fig. {{#var:chapter}}.{{#expr:{{#var:figure}}}}) and double-click on the Spouse box. This calls up the dialog. Select the tab and click the button to add an image. {{-}}

![[_media/SourcesCategory-Sources-ListView-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Source view]]

To add images related to a source or a place, first switch to the View (See Fig. {{#var:chapter}}.{{#expr:{{#var:figure}}}}) or View (See Fig. {{#var:chapter}}.{{#expr:{{#var:figure}}+1}}). Select the source or place you want and then either double-click on it or click the icon on the toolbar. Select the tab and click the button to add an image.

![[_media/PlacesCategory-PlaceView-list-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Place view]]

{{-}}

![[_media/MediaCategory-Media-ListView-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Media view]]

Finally, to add images that you want to include in the family tree, but hare are not limited to any particular person, relationship, source or place, switch to the View (See Fig. {{#var:chapter}}.{{#expr:{{#var:figure}}}}). Then click the icon on the toolbar to add an image. If you have already added any images to any individual galleries, you will also find them listed in the View.

In any gallery, you can also use the to edit image information and the button and to remove the image reference from that gallery.

## To edit events, citations/sources, places, and repositories

To edit information about events, sources, places, and repositories already present in the family tree, switch to the appropriate view, select an entry you would like to view/modify, and then click the icon on the toolbar. Alternatively, you may double-click on the entry to edit it.

![[_media/EventsCategory-EventsListView-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Events view]]

To add an event, a citation/source, a place, or a repository to the family tree, switch to the appropriate View (See Fig. {{#var:chapter}}.{{#expr:{{#var:figure}}}}), View, View , View , or View. Then click the icon on the toolbar to add the corresponding object. Enter the information into the corresponding ( , , , or ) dialog.

[Category:Documentation](wiki:Category:Documentation)
