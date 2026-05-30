---
title: 'Gramps 6.0 Wiki Manual - Entering and editing data: detailed - part 1/tr'
categories:
- Stub
- Tr:Documentation
managed: false
source: wiki-scrape
wiki_revid: 120918
wiki_fetched_at: '2026-05-30T21:00:40Z'
lang: tr
---

{{#vardefine:chapter\|9.1}} {{#vardefine:figure\|0}} The section expands on the [brief overview](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_brief) of how to enter and edit data in Gramps.

Gramps offers you a series of Views. Each of these Views gives you opportunities to enter and edit information. In fact, you can often get to the same information from different Views.

In Gramps, information is entered and edited through what we call dialogs. Since we use that term frequently, we should define what we mean by it:

A dialog is a pop-up window that provides one or more forms for entering and editing data that fits a certain category. Examples in Gramps include the dialog and the dialog, among many others.

A dialog often includes a series of "notebook tabs" that group the information into subcategories. For example, the dialog has notebook tabs for subcategories such as Events, Attributes, Addresses, and Notes, among others.

## Kişiler hakkındaki bilgileri düzenleme

Information about people is entered and edited through the dialog. This dialog can be invoked from different Views in the following ways:

- From the [People Category](wiki:Gramps_6.0_Wiki_Manual_-_Navigation#Using_the_People_Category):

  
  
Double-click the name of the person whose data you would like to edit

Select the name by single click and then click the button on the toolbar.

Select the name and then press **Enter** .

Select Edit... from the Edit menu of Gramps

Select Edit from the context menu that appears upon right-click on the name.

- From the [Relationships Category](wiki:Gramps_6.0_Wiki_Manual_-_Navigation#Using_the_Relationships_Category): To edit the Active Person's data, click on the button next to the Active Person's name.

<!-- -->

- From the [Charts Category](wiki:Gramps_6.0_Wiki_Manual_-_Navigation#Using_the_Charts_Category): Double-click in the box having the name of the person whose data you want to edit.

Any of these methods will prompt you with the dialog. {{-}}

### Kişi Düzenle iletişim kutusu

![[_media/Edit-person-window-new-person-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Edit Person - window - Default New empty editor]]

![[_media/Edit-person-window-existing-person-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}}  dialog - showing example person]]

The dialog is where you either add a new persons information or edit an existing person.

The top of the window has two parts: The basic information about the of the person, and a section with the privacy button (to set the record as private), the gender selector, an ID you can give this record, and a marker you can assign to the person indicating the state of the record (complete, TODO, uncertain, ....) which will give this record a specific color in the person view.

By using the context menu(right clicking) from a blank area in the top section of the window eg:near the "Preferred Name" field, you will be present with a context menu for three options:

- \-

- \-

- reports are available.

Below this top section, there are several "[tabs](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1#Edit_Person_tab_pages)" containing different categories of available information. Click any tab to view and edit its contents.

Clicking the button at the bottom will apply all the changes made in all tabs and close the dialog window. Clicking the button will close the window without applying any changes.

{{-}} ![[_media/SaveChanges-alert-dialog-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;Save Changes?&quot; - alert dialog]]

If any data in any tabs were modified, an alert window will appear, prompting you to choose from the following options:

- *Close the without saving* - changes.
- **Cancel**(default) - the initial cancel request.
- *Save* - the changes.

as well as a checkbox to indicate *Do not ask again*. Also can be disabled from option in the [Preferences &gt; Warnings](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Warnings) dialog.

### Preferred name section

![[_media/EditPerson-PreferredName-section-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Preferred name" section (Highlighted in yellow) of "Edit Person" - dialog - example]]

The preferred or default name is the name that will be used in Gramps for the '[name](wiki:Names_in_Gramps)' of the person. You can set in the [Gramps Preferences](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Display) how a name is displayed, and generally you will only the need to put data in fields shown in the preferred name section.

Only detailed reports (textual and Narrative Web site generator) show also the alternate names. Note however that searching on a name will search in all names attached to a person, not only the preferred name.

The preferred name section contains the typical name information you will edit upon creation of a person. To reduce clutter, the less frequently needed fields (for Multiple Surnames and Alternate Names) are hidden by default. To expand the section for Multiple Surnames, click the   button or use its [keybinding](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings#Editor_bindings). To see the full range of data you can store about a name, click the   button in the lower right corner the section or use its [keybinding](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings#Editor_bindings). This will show the [Name Editor](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_3#Name_Editor).

The name fields of the preferred name in the are:

- of the name. Predefined types include: Also Known As, **Birth Name** *(default)*, Married Name, Unknown. You can also type over in this entry field to create your own [Custom Types](wiki:Gramps_Glossary#custom) (eg nick name, short name, etc.).

  
It is advisable that the preferred name be a registered birth name or other name with legal standing. Those are names that will be found most often on citable documents. You may choose to store other name types in the tab of the .

- , the person's given name(s)

- , an optional suffix to the name, such as *Jr.* or *III*

- , the part of a person's name indicating the family to which the person belongs.

  - Selecting the   button, will show the section entry box, allowing you to enter compound surnames (for example for patronymics, or compound matrilineal-patrilinial names)

- , an optional prefix for the family name that is not used in sorting, such as *de* or *van*

- , the [origin](wiki:Gramps_Glossary#name_origin) type of the name identifies the cultural naming system that specifies how a particular surname was elected. This is meta information about the surname which can be important in genealogical research.

- , which is a title (typically in abbreviated form) used to refer to the person such as *Dr.* or *Rev.*, selector,

- , is a descriptive name given in place of or in addition to the official given name. If a Nick name is a full name construct, use a specific name type *Also known as* instead of the Nick field.

- , officially this is the part of the given name that is the normally used name. Eg, a person can have 3 given names as in *Jean Baptiste Jules*, where in reality only *Baptiste* is used. In Germany and some other places, it was customary to underline the callname among the different given names, see also [here](wiki:Names_in_Gramps#Call_Name). Some people will try to use this field also for nickname, or changes to the Given name (like Cristy for Cristina), but this is not the intended use. A call name is a proper legal name. For nick names, or short name variants, you should create an alternative name with a different type.

On the [Name Editor](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_3#Name_Editor) an extra field is available: . This is a unofficial name given to a family splinter group to distinguish them from people with the same family surname. Often referred to as Farm name and typically references a location where the splinter group resides or originates. (aka sept, sect, camp)

The and fields provide an "autocompletion" feature: as you type in these fields, a menu appears below the field containing database entries that match your partial input. This gives you a shortcut by letting you select an entry that already exists in the database rather than having to type it all out. You can select the entry using your mouse or using your arrow and **Enter** keys.

{{-}}

### Çoklu Soyadlar

![[_media/EditPerson-top-sections-highlighted-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Multiple Surnames" section (Highlighted in Blue) of the "Edit Person" - dialog - example]]

When s add button has been pressed, a new section entry box will be shown, allowing compound surnames to be entered.

The Multiple Surnames feature might be used for patronymics or compound matrilineal-patrilinial names. Another variation would be a Scandinavian name like ‘Syver Ericksen Skotterud’ where the full name is composed of a forename (Syver), a reference to his father (Ericksen or son of Erick) together with a village or locality name. In such a case, you can add 'Ericksen' with an [Origin](wiki:Names_in_Gramps#Origin_Attributes) of "Patronymic" and expand to a Multiple Surnames by adding 'Skotterud' with an Origin of "Location".

If you do not add any information in this section then, on the next open of the Edit Person dialog, it will be hidden. Any empty rows will not be saved.

{{-}}

### Genel bölüm

![[_media/EditPerson-General-section-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "General" section of the "Edit Person" - dialog - example]]

- The menu offers the choice of person's gender :
  - 

  - 

  - (Default)

<!-- -->

- The field displays the Gramps ID number which identifies the user in the Family tree uniquely. This value helps you distinguish between people who have the same name. You may enter any unique value you want. If you do not provide a value, Gramps will automatically select a value for you.

<!-- -->

- The area show the your custom assigned tags that specify some basic information on the status of your research.
  - The button brings up the dialog list that lets you remove or assign existing custom tags.

<!-- -->

- The button lets you mark whether or not the person's record is considered private.

{{-}}

### Preferred image

![[_media/EditPerson-top-sections-image-with-context-menu-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Image" section (Highlighted in Red) of the "Edit Person" - dialog - example]]

If any images exist the person editor will show an additional area in the top left region (otherwise it is hidden). This area shows the first image available in the of this person. {{-}}

### Kişi sekme sayfasını düzenle

The tabs reflect the following categories of personal data:

#### Etkinlikler

![[_media/EditPerson-Events-tab-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Events" tab from "Edit Person" - dialog - example]]

  
The tab lets you view and edit any events relevant to the person. The bottom part of the window lists all such events stored in the database and displays the following columns: `Type, Description, Date, Place, Main Participants, Private(lock icon), Role, ID, Age`. The top part shows the details of the currently selected event in the list (if any). The buttons , , and allow you to add, modify, and remove an event record from the database. Note that the and buttons become available only when an event is selected from the list.

<!-- -->

  
When you use the button the selector dialog is shown allowing you to select an already existing event and edit it in the dialog.

<!-- -->

  
When you add a new event or edit an existing event, the dialog is invoked. The dialog is described in the [Event Reference section](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_2#Editing_event_references)

{{-}}

##### Select Event selector

![[_media/SelectEvent-selector-dialog-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Select Event - selector - example]]

The selector dialog allows you to link to an already existing event and once selected it will be opened in the dialog.

The following columns are shown: Type(default sort for list), Main Participants, Date, Place, Description, ID, Last Change.

You may use the button to filter the list based on one of the options from the drop down list:

- **Type contains** (default)
- *Type does not contain*
- *Main Participants contains*
- *Main Participants does not contain*
- *Date contains*
- *Date does not contain*
- *Place contains*
- *Place does not contain*
- *Description contains*
- *Description does not contain*
- *ID contains*
- *ID does not contain*
- *Last Change contains*
- *Last Change does not contain*

{{-}}

#### Adlar

![[_media/EditPerson-Names-tab-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Names" tab from "Edit Person" - dialog - example]]

  
The tab lets you view and edit any alternate names the person may have. The bottom part of the window lists all alternate names for the person stored in the database. The top part shows the details of the currently selected name in the list (if any). The buttons , , and allow the addition, modification, and removal of an alternate name from the database. Note that the Edit and - buttons become available only when an alternate name is selected from the list.

<!-- -->

  
When you add a new name or edit an existing name, the dialog is invoked. This Names dialog is described in the [Name Editor section](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_Editing_Data:_Detailed_-_part_3#Name_Editor)

{{-}}

#### Kaynak Alıntıları

![[_media/EditPerson-SourceCitations-tab-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Source Citations" tab from "Edit Person" - dialog - example]]

  
The tab allows you to view and document the source citations for the information you collect.

<!-- -->

  
These might be general sources that do not describe a specific event, but which nevertheless yield information about the person. For example, if Aunt Martha's memoirs mention her great-grandson Paul, the researcher may assume that this Paul actually existed and cite Aunt Martha's memoirs as the source that justifies this assumption.

  
The central part displays the list of all source references stored in the database in relation to the person. The buttons , , and allow you to correspondingly add, modify, and remove a source reference to this person. Note that the , and buttons become available only when a source reference is selected from the list.

<!-- -->

  
On edit you can change the data in the citation (unique to this person), as well as the shared source object, see [Editing Citations](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_2#Editing_source_citations).

{{-}}

#### Nitelikler

![[_media/EditPerson-Attributes-tab-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Attributes" tab from "Edit Person" - dialog - example]]

  
The tab lets you view and assign attributes to the person. You have complete freedom to define and use attributes. For example, attributes might be assigned to describe the person's physical characteristics or personality traits.

<!-- -->

  
Note that each attribute listed in the dialog consists of two parts: the Attribute itself and a Value associated with that Attribute. This so-called "Parameter-Value" pairing can help you organize and systematize your research. For example, if you define "Hair color" as an Attribute for a person, "Hair Color" will become a selectable Attribute for all other people. The Value of Hair Color for person A might be red, and brown for person B. In similar fashion, you might define an Attribute like "Generosity" and use the Value of "Enormous" to describe a particularly generous person.

<!-- -->

  
The bottom part of the dialog window displays the list of all Attributes stored in the database. The top part shows the details of the currently selected attribute in the list (if any). The buttons , , and let you add, modify, and remove an attribute record from the database. Note that the **Edit** and **-** buttons become available only when an attribute is selected from the list.

If you edit an attribute the opens.

{{-}}

#### Adresler

![[_media/EditPerson-Addresses-tab-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Addresses" tab from "Edit Person" - dialog - example]]

  
The tab lets you view and record the various mailing addresses of the person. You are advised to use a residence event to store information of residency of a person. The address tab is offered mainly for compatibility with the GEDCOM standard where the rationale of addresses is mailing only.

<!-- -->

  
The bottom part of the window lists addresses stored for that person in the database. The top part shows the details of the currently selected address in the list (if any). The buttons , , and allow you to correspondingly add, modify, and remove an address record from the database. Note that the and buttons become available only when an address is selected from the list.

  
If you edit an address the opens.

<!-- -->

  
Some reports allow you to restrict data on living people. In particular, that option will omit their addresses.

{{-}}

#### Notes

![[_media/EditPerson-Notes-tab-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Notes" tab from "Edit Person" - dialog - example]]

  
The tab provides a place to record various items about the person that do not fit neatly into other categories, as well as text excerpts you want to add to the family tree. You can share notes between different records in Gramps. The iconbar in this tabpage offers the usual buttons: , , , , and reorder buttons to change the order of the notes

<!-- -->

  
If you edit a note, you obtain the .

{{-}}

##### Select Note selector

![[_media/SelectNote-selector-dialog-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Select Note - selector - example]]

The selector dialog allows you to link to an already existing note.

The following columns are shown: Preview(default sort for list), ID, Type, Tags, Last Change.

You may use the button to filter the list based on one of the options from the drop down list:

- **Preview contains** (default)
- *Preview does not contain*
- *ID contains*
- *ID does not contain*
- *Type contains*
- *Type does not contain*
- *Tags contains*
- *Tags does not contain*
- *Last Change contains*
- *Last Change does not contain*

{{-}}

#### Galeri

![[_media/EditPerson-Gallery-tab-example-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Gallery" tab from "Edit Person" - dialog - example]]

  
The tab lets you view and store photos, videos, and other media objects that are associated with the person. The central part of the window lists all such media objects. Any object in the form of a valid image file will result in the display of a thumbnail view of the image. For other objects such as audio files, movie files, etc., a corresponding file type icon is displayed instead.

<!-- -->

  
The following options are available:

- \- allows you to add a new media object from the .

- \- brings up the selector dialog allowing you to link to an already existing media object.

- \- allows you to modify the select media object in the . This button only becomes available when a media object is selected from the list.

- \- remove the selected media object from the person's gallery. This button only becomes available when a media object is selected from the list.

You can change the order of the primary (active) image by selecting the image and dragging it to the first position.

If you select a media object a context menu (right-click) is available with the following options:

- View
- Open Containing_folder
- Make Active Media
- Add
- Share
- Edit
- Remove

##### Select Media Object selector

![[_media/SelectMediaObject-selector-dialog-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Select Media Object - selector - example]]

The selector dialog allows you to link to an already existing media object and once the image is selected it will be opened in the dialog.

Once you select an media object from the list a preview will be shown if possible in the top section.

The following columns are shown: Title(default sort for list), ID, Type, Last Change.

You may use the button to filter the list based on one of the options from the drop down list:

- **Title Contains**(default)
- *Title does not contain*
- *ID contains*
- *ID does not contain*
- *Type contains*
- *Type does not contain*
- *Last Change contains*
- *Last Change does not contains*

See also [Select a media object selector](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_2#Select_a_media_object_selector) {{-}}

#### Internet

![[_media/EditPerson-Internet-tab-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Internet" tab from "Edit Person" - dialog - example]]

  
The tab displays Internet addresses relevant to the person. A descriptive caption of the Internet location you are storing. Type of internet address as needed to navigate to it, eg. <http://gramps-project.org>, E-mail, Web Page, ...

<!-- -->

  
The bottom part lists all such Internet addresses and accompanying descriptions. The top part shows the details of the currently selected addresses in the list (if any). The buttons , opens the dialog to add or edit and the removes the selected Internet address. The "Jump to" button opens your web browser and takes you directly to the highlighted page.

Note that the , and buttons become available only when an web address is selected from the list. {{-}}

##### Internet Address Editor

![[_media/InternetAddressEditor-dialog-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Internet Address Editor" - dialog - default]]

The dialog allows you to add an new Internet address or modify selected Internet address.

- Type of internet address:

  - *E-mail*
  - **Unknown** <small>(default)</small>
  - *FTP*
  - *Web Home*
  - *Web Search*

- toggle the privacy status of the record.

- The internet address as needed to navigate to it eg: <https://gramps-project.org>

  - open the web address in the default browser

- A descriptive caption of the Internet location you are storing.

See also

- [Link Editor](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_2#Link_Editor)
- [Note Link Report](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_6#Note_Link_Report)

{{-}}

#### Associations

![[_media/EditPerson-Associations-tab-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Associations" tab from "Edit Person" - dialog - example]]

The tab lets you view and edit information about the associations between people in the database. The associations may include Godparents, family friends, pall bearer, coworker, or any other type of associations you may wish to record. If the closest relation is 'Godparent', then this would indicate that the Godparent of the person (being edited) is the person whose name is shown in the Associations tab.

The [*Associates* (ASSO) tag in the GEDCOM standard](http://wiki-en.genealogy.net/GEDCOM/ASSO-Tag) says that "a person's relation or association is the person being pointed to." You might choose to put a reciprocal Association in that other person's Associations tab.

In the association shown from [example.gramps](wiki:Example.gramps), Lewis Garner's Godfather is Anderson Garner. Use Events instead for relations connected to specific time frames or occasions. Events can be shared between people, each indicating their [role](wiki:Gramps_Glossary#role) in the event.

The button opens the dialog to add. The button allows you to edit and the removes the selected association. The other buttons or move the selected entry position in the list only.

See also:

- [Roles, Relationships &amp; Associations](wiki:Roles,_Relationships_&amp;_Associations)
- [Add a godfather-godmother](wiki:Add_a_godfather-godmother)

{{-}}

##### Person Reference Editor

![[_media/PersonReferenceEditor-dialog-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Person Reference Editor" - dialog - default]]

The lets you add and edit Association entries. You can access it from the s dialog tab.

- - button brings up the selector dialog.

- *Godfather* (Default) you can over type the default entry with anything you choose.

  - record is public (Default)

<!-- -->

- Source Citations tab

<!-- -->

- Notes tab

{{-}}

###### Select Person selector

![[_media/SelectPerson-selector-dialog-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Select Person" - selector dialog - example]]

{{-}}

#### LDS

![[_media/EditPerson-LDS-tab-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "LDS" tab from "Edit Person" - dialog - example]]

  
The (Latter Days Saints) tab lets you view and edit information about LDS ordinances of the person. This information is inherited from GEDCOM specification.

<!-- -->

  
These are LDS Baptism, Endowment, and Sealed to Parents ordinances, as labeled inside the tab. Each ordinance is described by its date, LDS temple, and Place where it happened.

<!-- -->

  
An additional pop-up menu, "Parents," is available for the Sealed to Parents ordinance. Each ordinance can be further described through the selections available in the Status pop-up menu. It can also be include notes and references to sources through the corresponding and buttons.

See: [Family Editor dialog&gt;Tab&gt;LDS](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1#LDS_2)

{{-}}

##### LDS Ordinance Editor

![[_media/LDSOrdinanceEditor-dialog-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "LDS Ordinance Editor" - dialog - default]]

Use the or buttons to bring up the dialog where you can add or edit existing LDS ordinances of the person.

- See [Ordinance (Latter Day Saints)](https://wikipedia.org/wiki/Ordinance_(Latter_Day_Saints)) on [Wikipedia](https://en.wiktionary.org/wiki/Wikipedia#Etymology).

{{-}}

#### References

![[_media/EditPerson-References-tab-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "References" tab from "Edit Person" - dialog - example]]

  
The tab

{{-}}

## Editing information about relationships

Information about relationships is entered and edited through the dialog.

This dialog may be invoked in a number of ways:

- From [Relationships Category](wiki:Gramps_6.0_Wiki_Manual_-_Categories#Relationships_Category): click on an button in the family that you want to edit.

<!-- -->

- From [Families Category](wiki:Gramps_6.0_Wiki_Manual_-_Categories#Families_Category): select the family in the list and then click the button on the Toolbar, or double-click on the family.

<!-- -->

- From [Charts Category](wiki:Gramps_6.0_Wiki_Manual_-_Categories#Charts_Category): point your mouse over the black line connecting the spouses, right-click and select from the context menu, or double-click on the black line.

Any of these methods will prompt you with the dialog:

{{-}}

### Family Editor dialog

![[_media/FamilyEditor-dialog-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}}  dialog]]

The top section of the window shows the names of the people whose relationship is being edited, as well as their birth and death information.

- 

- 

[Quick View](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_8#Quick_Views) reports are available by using the context menu(right clicking) from a blank area in the top section of the window.

The section displays three fields and a number of [notebook tabs](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1#Family_Editor_tab_pages) representing different categories of information about the relationship. Click any tab to view or edit the information it contains. The bottom part has and buttons. Clicking the button at any time will apply all the changes made in all tabs and close the dialog window. Clicking the button at any time will close the window without applying any changes. If any of the data in any tab is modified, an alert window will appear that will prompt you choose between closing the dialog without saving changes, canceling the initial cancel request, or saving the changes.

The section fields have the basic description of the relationship. The field displays the ID number which labels this relationship in the database, leave this field empty to have Gramps generate a unique ID number. You can choose from the drop-down list the available types of family relationships such as `Civil Union`, `Married`, **`Unknown`**(default), `Unmarried`, etc.)

See also:

- [How do I represent a divorce?](wiki:Indicate_a_divorce)

displays shows the [tags](wiki:Gramps_6.0_Wiki_Manual_-_Filters#Tagging) you have created to show some basic information on the status of your research. You can add additional tags by selecting the button.

##### Select Father selector

![[_media/SelectFather-selector-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Select Father - selector]]

The selector dialog allows you to link to an already existing Father. {{-}}

##### Select Mother selector

![[_media/SelectMother-selector-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Select Mother - selector]]

The selector dialog allows you to link to an already existing Mother. {{-}}

### Family Editor tab pages

The tabs provide the following information categories of relationship data:

#### Children

![[_media/FamilyEditor-dialog-Children-tab-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Children" tab from "Family Editor" - dialog - example]]

  
The tab lets you view and edit the list of children who are part of this relationship. The button allows entering a new person to the database and adding that person as a child in this relationship. The button lets you select an existing person to be a child in the relationship. The button opens the dialog that allows for editing the relations between the selected child and the parents. Finally, the lets you remove the selected child from the relationship. Note that the and buttons become available only when a child is selected from the list.

[How do I change the order of children?](wiki:Gramps_6.0_Wiki_Manual_-_FAQ#How_do_I_change_the_order_of_children.3F) Use:

- This [Children](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1#Children) tab in the Family Editor to change the order of children in the family.
- The third party addon [Birth Order Tool](wiki:Addon:BirthOrderTool) which allows bulk updates of the children order.

{{-}}

##### Select Child selector

![[_media/SelectChild-selector-dialog-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Select Child - selector - example]]

The selector dialog allows you to link to an already existing child and once selected will be opened in the

The following columns are shown: Name(default sort for list), ID, Gender, Birth Date, Birth Place, Death Date, Death Place, Spouse, Last Change. {{-}}

##### Child Reference Editor

![[_media/ChildReferenceEditor-dialog-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Child reference editor]]

The dialog allows editing of the relationship between the selected child and the parents.

The following options are available:

- The name of the child

  - button.

- Select from the drop down list of possible relationship types:

  - Adopted
  - **Birth**(default)
  - Foster
  - None
  - Sponsored
  - Stepchild
  - Unknown

- Select from the drop down list of possible relationship types:

  - Adopted
  - **Birth**(default)
  - Foster
  - None
  - Sponsored
  - Stepchild
  - Unknown

- privacy toggle for this relationship.

{{-}} Also the following tabs are available.

###### Source Citations tab

{{-}}

###### Notes tab

{{-}}

#### Events

  
The tab lets you view and edit the list of events relevant to the relationship. The buttons , , and let you add, modify, or remove an event record from the database. Note that the and buttons become available only when an event is selected from the list.

{{-}}

#### Source Citations

  
The tab lets you view and edit a list of references to the sources that provide evidence for the relationship. These might be documents that refer to the relationship, but which do not necessarily document it officially. For example, if Aunt Martha's memoirs mention that her great-grandson Paul was married, the researcher may take this as evidence of the relationship between Paul and his wife existed and cite the memoirs as the source for this assumption.

The buttons , , and allow let you add, modify, and remove a source reference to this relationship. Note that the and buttons become available only when a source reference is selected from the list.

{{-}}

#### Attributes

  
The tab lets you view and edit particular information about the relationship that can be expressed as attributes. The buttons , , and let you add, modify, or remove an attribute. Note that the and buttons become available only when an attribute is selected from the list.

{{-}}

#### Notes

  
The tab lets you view and edit any [Note](wiki:Gramps_Glossary#note) associated with the relationship. These could be any comments which do not naturally fit into the "Parameter-Value" pairs available to Attributes. To add a note or modify existing notes simply edit the text in the text entry field.

The option lets you set the way the note will appear in reports and web pages. If you select Flowed, the text generated will have single spaces put in place of all multiple spaces, tabs, and single end-of-line characters. A blank line inserted between two blocks of text will signal a new paragraph; additional inserted lines will be ignored.

If you select the Preformatted option, the text in reports and web pages will appear exactly as you enter it in the dialog.

{{-}}

#### Gallery

  
The tab lets you store and display photos and other media objects associated with the relationship. The central part of the window lists all such objects and gives you a thumbnail preview of image files. Other objects such as audio files, movie files, etc., are represented by a generic Gramps icon. The buttons , , , and let you add a new image, add a reference to an existing image, modify an existing image, and remove a media object's link to the relationship. Note that the and buttons become available only when a media object is selected from the list.

{{-}}

#### LDS

![[_media/EditFamily-LDS-tab-example-51.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Sealed to Spouse ordinance editor of &quot;Edit Family&quot; - dialog - example]] The (Latter Days Saints) tab of the Family Editor only displays information about the LDS **Sealed to Spouse** . (The ordinances related to individuals can be recorded in [LDS tab of the <strong>Person</strong> Editor](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1#LDS).)

The data can also include , , , and .

Each ordinance record can also be annotated in the corresponding and tabs. The status of the ordinance can be described through the options available in the pop-up menu.

  
The status states for the **Sealed to Spouse** ordinance are:

- **<No Status>** *(default)*
- Canceled
- Cleared
- Completed
- Do not seal
- Pre-1970
- Qualified
- Do not seal/Cancel
- Submitted
- Uncleared

To edit Source or Note annotation data, switch to the corresponding LDS Ordination Editor tab and select the desired entry in the list of records. Double-click that entry or click the icon on the toolbar to invoke the following

The main part of the Family Editor’s tab displays a table of the five different kids of data in a each record. Click a column header to row or double-click a row to edit its contents. The bottom part of the window has and buttons. Clicking will apply all the changes made in all tabs and close the dialog window. Clicking the button will close the window without applying any changes. {{-}}

## Editing dates

This section describes how to enter and modify dates. Since dates are so important in genealogical research, Gramps takes special care to preserve and use any date information available.

Information can be entered into a date field by directly typing it or by invoking the dialog by clicking the button next to any entry field.

See also:

- [Gramps 6.0 Wiki Manual - Probably Alive](wiki:Gramps_6.0_Wiki_Manual_-_Probably_Alive)

- \- To change the default values for the typical ages at birth, between generations, etc.

### Date selection dialog

![[_media/DateSelection-dialog-defaults-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}}  - dialog - default]]

While the above parsing rules provide a guide for you to type in most common dates, you can also use dialog. The dialog is particularly useful for building a complex date or for simply insuring that your information is entered in a way Gramps will understand.

- Choose alternate [calendar type](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1#Calendars).

  - [**Gregorian**](https://en.wikipedia.org/wiki/Gregorian_calendar)(default)
  - [Julian](https://www.familysearch.org/wiki/en/Julian_and_Gregorian_Calendars) (including [Mixed](wiki:Dates#Dual_Dated)/[Dual](#Dual-dated_dates) dates)
  - [Hebrew](https://en.wikipedia.org/wiki/Hebrew_calendar)
  - [French Republican](https://www.familysearch.org/wiki/en/French_Republican_Calendar)
  - [Persian](https://en.wikipedia.org/wiki/Iranian_calendars#Old_Persian_calendar)
  - [Islamic](https://en.wikipedia.org/wiki/Islamic_calendar)
  - [Swedish](https://www.familysearch.org/wiki/en/Sweden_Feast_Day_Calendars)

-  This field is select-able with the matching field if the alternate supports [dual dating](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1#Dual-dated_dates). (checkbox unchecked by default)

  - (Empty text field by default)

- Set the [date quality](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1#Date_Quality).

  - **Regular**(default)
  - Estimated
  - Calculated

- Set the interval precision or time frame [date type](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1#Date_formats_and_parsing_rules).

  - **Regular**(default) - the interval spanning a specific day, month or year (without regard to time zone)
  - Before
  - After
  - About
  - Range
  - Span
  - Text only

- Select the , and the .

- If your date is *Range* or *Span*, this option will be available to set a date.

- text entry field allows storing an arbitrary text string along with the date.

{{-}}

### Date validity indicators

![[_media/DateSelection-dialog-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Date selection dialog - example]]

Gramps uses a date validator.

While partial dates do not uniquely define the day, they allow at least for some type of comparisons between the dates.

The date field will highlight in red and display a red symbol (such as a stop sign or cross) to indicate the entered date is not recognized as a recognized and valid format for a date.

Examples of common date references that are not recognizable Gramps formats might be "Christmas week of '61", "Fall 1782", or "the summer when I had surgery". In such a case, the date will be stored as string and marked as *Text only* type. Any dates of this Type will not be compared to other dates. Wherever possible, it is preferable to avoid such *Text Only* date entries. It might be better, for example, to enter a date of "December 1961" and then to add the Description annotation "Christmas week of '61." It would be more precise to check a calendar for December 1961 then key in the actual date span... but still include the annotation. The annotation is needed because you cannot assume that 'Christmas week' means the same span of days to you as to your source. There could be culture bias to color the interpretation. It could mean the calendar row containing Christmas day. But American & European calendar rows start on different days of the week. Or, it could mean the 7 days starting with Christmas or even the 7 days leading up to Christmas. So the span allows searches and comparisons but the annotation shows that actual interval is subject to interpretation.

In the various views (such as the ), unrecognized dates will be displayed in **bold** by default. The text markup (formatting style) for unrecognized dates can be modified by changing the option in the [tab](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Dates) of [Preferences](wiki:Gramps_6.0_Wiki_Manual_-_Settings).

When a Birth or Death date is missing for a Person, the dates of existing fallback Events in the same category may be shown (and indicated with italics with an abbreviated title) rather leaving the display blank. So, a Burial or Cremation date will be shown if a Death date has not yet been recorded.

{{-}}

### Date Quality

- Regular: A "regular" date is one with an explicit day, month, or year.

<!-- -->

- Estimated: An "estimated" date is one based on average interval assumptions offset from a known reference date. (Such as the average number of years between generations, maximum lifespan, or length of sea voyage.)

<!-- -->

- Calculated: A "calculated" date is one based on a known interval from a reference date but without a source explicitly mentioning the date. (Such as a gravestone engraved with both a date of death and a precise age at death.)

Census data is unusual in that it seems to a candidate for a Calculated date but is not. The census often explicitly defines the interval (age) and the reference date (census polling date) but that age is often estimated or rounded.

### Date Type

To the right of the should appear the pop-up menu.

Dates in Gramps are classified according to the following types of precision (scale) of interval or time frame:

- Regular: A "regular" date is one which includes an interval spanning a specific day, month, or year. It can be complete (or 'fully qualified' for a 24 hour interval like June 6, 1990) or partial (like omitting the day for a 1 month interval like July 1977 or omitting the day and month for a 1 year interval).

<!-- -->

- Before: A "before" date is one that can only be identified as occurring (in a [preferences-defined long interval](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Dates)) prior to a certain day, month, or year. *(By default, the interval is 50 years.)*

<!-- -->

- After: An "after" date is one that occurs (in a [2nd preferences-defined long interval](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Dates)) following a certain day, month, or year. *(By default, the interval is 50 years.)*

<!-- -->

- About: An "about" (circa) date is one that occurs (in [yet another preferences-defined ±years interval](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Dates)) before **or** after a certain day, month, or year. *(By default, the interval is ±50 years.)*

<!-- -->

- Range: A "range" describes a time period during in which the event occurred. It could be recurrent event during the interval or a single instance believed to have occurred between known boundary dates.

  
For example, "between January 1932 and March 1932."

- Span: A "span" describes an inclusive time period during which a condition continually existed.

  
For example, "from May 12, 2000 to February 2, 2002."

### Date formats and parsing rules

The Date Selection dialog just helps layout a date in the standard format that Gramps knows how to parse. It is useful while you're unfamiliar with the options, need to use an alternative calendar or specify a New Year begins date.

Gramps recognizes dates entered in a variety of formats. The default numeric format is that which is conventional for the environment is which Gramps is operating; that is, DD.MM.YYYY for most European countries, MM/DD/YYYY for the U.S., and so on. A way to avoid this ambiguity is to always choose a d mmmnbsp;yyyy or mmmnbsp;d yyyy format.

Besides exact dates, Gramps recognizes many date types that are not regular: before, after, about, ranges and spans. It also understands the quality: estimated or calculated. Finally, it supports partial dates and many alternative calendars. Below is the list of date entry rules to allow precise date parsing.

Regular single dates can be entered just as you would write them. And typing a slash after the year followed by a value 1 year later creates a Julian dual dated entry.

  
Examples: May 24, 1961, 31 Dec 1858/9 or January 1, 2004.

Partial dates are entered simply by omitting unknown information.

  
Examples: May 1961 and 2004.

Dates that are not Regular should start with the keywords of *Estimated* or *Calculated* , if applicable.

  
Example: est. 1961, or calc 2005. (Note that a does not need to be specified for regular dates.)

The menu options can also be set to *Before*, *After*, or *About* by simply typing "before", "after" or "about" before a single date in the Event Editing dialog.

If the desired is a range, write "between DATE and DATE", and if the is a span, write "from DATE to DATE".

  
Examples: est from 2001 to 2003, before June 1975, est circa 2000, calc between May 1900 and January 1, 1990.

Here are a couple examples to try:

  
Captain John Smith has been stationed in the 1st Grenadier regiment between 1888-5-13 and 1902-10-24 according to his military record (words "between" and "and" intentionally used as this is the way we talk in day-to-day life); Then date should be coded "from … to …" because this is the duration of his duty.

<!-- -->

  
Captain John Smith's regiment was posted to the Escaut river at Valenciennes the week before the Armistice.  
*Then this can be recorded as a "Military Service" Event type with a date of "between Nov 4 1918 and 11 Nov 1918" (Gramps will convert to a standard date format despite 2 formats being used for entry) at River Escaut, Valenciennes, Noord department, France... because the actual date for this "instantaneous" event is not known in the source.*

### Calendars

Alternate calendars are calendars other than the Gregorian calendar. Currently, Gramps supports Hebrew, French Republican, Julian, Islamic, Persian, and Swedish alternate calendars. To specify the calendar other than the default Gregorian, append the name of the calendar to the date string, e.g. "January 9, 1905 (julian)" or use the drop down menu.

#### Swedish calendar

The [Swedish king](wiki:Swedish_kings), Karl XII, decided that Sweden should start using the Gregorian calendar. However, it was planned to take place gradually by skipping 11 leap days starting 1700-02-29 and end by 1744. So 1700-02-28 was followed by 1700-03-01. This took place during the Great Nordic War and the leap days were kept 1704 and 1708. In January 1711 the same king decided that Sweden should return to the Julian Calendar by 1712-03-01. In order to be in phase, an extra day was inserted on 1712-02-30. And that was the end of the Swedish Calendar. Sweden converted to Gregorian in 1753-03-01, by skipping dates between 1752-02-18 and 1753-02-28. In Gramps you can only enter valid dates for the Swedish Calendar from 1700-03-01 to 1712-02-30. All other dates are flagged as not valid and has to be corrected.

### Dual-dated dates

Dual-dated dates (also called "double dating", "slash dates", and sometimes "Old Style/New Style" dates) appear like "Jan 23, 1735/6". Often mistaken as a year uncertainty, this actually has a specific historic meaning. The dual dated date represents a time when an area was in a transition between moving to January 1 as the beginning of the new year. Thus Jan 23, 1735/6 is an indication to make it clear what date is being referred to. In this example, "Jan 23, 1736" might have occurred after "Jun 23, 1736".

England and the American colonies didn't officially accept the "Jan 1" as the new year date until 1752. Before 1752, the English government still officially observed March 25 as the first of the year, whereas most of the English population observed January 1 as the first of the year. Many people therefore wrote dates falling between January 1 and March 25 in the dual-dated format.

Sometimes, a dual date may appear as a fraction, as in this grave stone (170 and 3/4, which means 1703 and 1704):

![[_media/Gravestone.jpg|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Gravestone showing dual date as a fraction (170 and 3/4, which means 1703 and 1704)]]

{{-}}

Marking a date as dual dated can be done by simply putting a slash between the years. For example:

- 1721/2
- 1719/20
- 1799/800

These slash-years can appear anywhere in a date that a regular year can appear.

Dual-dated dates are currently represented in the Julian calendar so their month and day will be the same as that in the textual representation.

#### Alternate new year day

With dual-dated dates (and other dates) you may know that the new year was celebrated on a day other than January 1. To indicate this in Gramps, put the month/day code in parentheses, after the calendar (if one). For example:

- Jan 20, 1865 (Mar25)
- Jan 20, 1750 (Julian,Mar1)
- Feb 23, 1710/1 (Mar25)

To indicate the beginning of a year that is different from that of January 1, you use the following codes:

- Jan1
- Mar1
- Mar25
- Sep1

You can put that as the only item in parenthesis, or right after a calendar name (comma, and no space).

Note that if new year's day is not Jan 1, then January will come after December that year. Dates with new year day codes will be sorted appropriately.

{{-}}

[Category:Tr:Documentation](wiki:Category:Tr:Documentation)
