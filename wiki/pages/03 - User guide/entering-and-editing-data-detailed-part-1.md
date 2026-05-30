---
title: 'Gramps 6.0 Wiki Manual - Entering and editing data: detailed - part 1'
categories:
- Documentation
- Stub
managed: false
source: wiki-scrape
wiki_revid: 125679
wiki_fetched_at: '2026-05-30T11:11:21Z'
---

{{#vardefine:chapter\|9.1}} {{#vardefine:figure\|0}} **<span style="font-size:120%">Entering and editing data: detailed People, Relationships, Dates</span>**  
Section expands on the [brief overview](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_brief) of how to enter and edit data in Gramps.

Gramps offers you a series of Views. Each of these Views gives you opportunities to enter and edit information. In fact, you can often get to the same information from different Views.

In Gramps, information is entered and edited through what we call dialogs. Since we use that term frequently, we should define what we mean by it:

A dialog is a pop-up window that provides one or more forms for entering and editing data that fits a certain category. Examples in Gramps include the dialog and the dialog, among many others.

A dialog often includes a series of "[notebook tabs](https://wikipedia.org/wiki/Tab_(interface))" that group the information into subcategories. For example, the dialog has notebook tabs for subcategories such as Events, Attributes, Addresses, and Notes, among others.

## Editing information about people

Information about people is entered and edited through the dialog. Also called the Person Editor dialog, this dialog can be shown from different Views in the following ways:

- From the [People Category](wiki:Gramps_6.0_Wiki_Manual_-_Navigation#Using_the_People_Category):

  
  
Double-click the name of the person whose data you would like to edit

Select the name by single click and then click the button on the toolbar.

Select the name and then press **Enter** .

Select Edit... from the Edit menu of Gramps

Select Edit from the context menu that appears upon right-click on the name.

- From the [Relationships Category](wiki:Gramps_6.0_Wiki_Manual_-_Navigation#Using_the_Relationships_Category): To edit the Active Person's data, click on the button next to the Active Person's name.

<!-- -->

- From the [Charts Category](wiki:Gramps_6.0_Wiki_Manual_-_Navigation#Using_the_Charts_Category): Double-click in the box having the name of the person whose data you want to edit.

Any of these methods will prompt you with the dialog. {{-}} <span id="Edit Person dialog">

### Person Editor dialog

</span> ![[_media/Edit-person-window-new-person-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Edit Person - window - Default New empty editor]]

![[_media/Edit-person-window-existing-person-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}}  dialog - showing example person]]

The dialog is where you either add a new persons information or edit an existing person.

The top of the window has two parts: The basic information about the of the person, and a section with the privacy button (to set the record as private), the gender selector, an ID you can give this record, and a tag you can assign to the person indicating the state of the record (complete, TODO, uncertain, ....) which will give this record a specific color in the person list view. {{-}}

Below this top section, there are several "[tabs](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1#Edit_Person_tab_pages)" containing different categories of available information. Click any tab to view and edit its contents.

Clicking the button at the bottom will apply all the changes made in all tabs and close the dialog window. Clicking the button will close the window without applying any changes.

{{-}} ![[_media/SaveChanges-alert-dialog-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;Save Changes?&quot; - alert dialog]]

If any data in any tabs were modified, an alert window will appear, prompting you to choose from the following options:

- \- changes.

- (default) - the initial cancel request.

- \- the changes.

as well as a checkbox to indicate that can be disabled from the option in the dialog.

#### Person Editor context menu

![[_media/QuickViewReport-EditPerson-context-menu-popup-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}}  dialog - showing the Quick View context submenu]] By using the context menu(right clicking) from a blank area in the top section of the window eg:near the "Preferred Name" field or below the "Preferred image"; you will be presented with a context menu for the following options:

<hr>

- \-

- \-

<hr>

- reports are available.

  - 

  - 

  - 

  - 

  - 

  - 

  - 

  - 

<hr>

{{-}}

### Preferred image

![[_media/EditPerson-top-sections-image-with-context-menu-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Example "Image" section with context menu for the "Edit Person" - dialog]]

If any images exist the person editor will show an additional area in the top left region (otherwise it is hidden). This area shows the first image available in the tab of this person.

See also

- [Missing Media Objects 'broken link' icon of a box with a red 'x'](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Missing_Media_Objects_.27broken_link.27_icon_of_a_box_with_a_red_.27x.27)

#### Person Editor image context menu

You can right click on the image to show the following image context menu options:

- \- opens the image in an externally associated image viewer.

- \- opens the dialog.

{{-}}

### Preferred Name section

![[_media/EditPerson-PreferredName-section-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Preferred Name" section of "Edit Person" - dialog - default]]

![[_media/Edit-person-window-existing-person-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Preferred Name" section (Next to image) of "Edit Person" - dialog - example]]

The preferred or default name is the name that will be used in Gramps for the '[name](wiki:Names_in_Gramps)' of the person. You can set in the [Gramps Preferences](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Display_Options) how a name is displayed, and generally you will only need to enter data in fields shown in the preferred name section.

Some detailed reports (textual and Narrative Web site generator) also show the alternate names. Note however that searching on a name will search in all names attached to a person, not only the preferred name.

The preferred name section contains the typical name information you will edit upon creation of a person. To reduce clutter, the less frequently needed fields (for [Multiple Surnames](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1#Multiple_Surnames) and [Alternate Names](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1#Names)) are hidden by default. To expand the section for Multiple Surnames, click the   button or use its [keybinding](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings#Editor_bindings). With Multiple names, a connector (such as a hyphen or [non-breaking space](https://en.wikipedia.org/wiki/Non-breaking_space)) can be specified to bridge between the surnames to create compound (aka "[double-barrelled](https://en.wikipedia.org/wiki/Double-barrelled_name)") surnames. To see the full range of data you can store about a name, click the   button in the lower right corner the section or use its [keybinding](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings#Editor_bindings). This will show the [Name Editor](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_3#Name_Editor).

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

The and fields provide an "[autocompletion](https://wikipedia.org/wiki/Autocomplete)" feature: as you type in these fields, a menu appears below the field containing database entries that match your partial input. This gives you a shortcut by letting you select an entry that already exists in the database rather than having to type it all out. You can select the entry using your mouse or using your arrow and keys.

Searching the multitude of name fields can be broadly or precisely targeted. Use the Name field in the People category [Filter](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#People_Filter) gramplet to search all the fields simultaneously. Or use the [People with the &lt;name&gt;](wiki:Gramps_6.0_Wiki_Manual_-_Filters#People_with_the_.3Cname.3E) rule to create a custom filter to search each element individually. {{-}}

### Multiple Surnames

![[_media/EditPerson-MultipleSurnames-entry-section-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Multiple Surnames" section of the "Edit Person" - dialog - default]]

![[_media/Edit-person-window-existing-person-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Multiple Surnames" section of the "Edit Person" - dialog - example]]

When the add (Use Multiple Surnames) button has been pressed at the far right of the row in the window, a new section entry box will be shown, allowing compound surnames to be entered. Alternately, the [Add button's Editor keybinding](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings#Editor_bindings) can be used.

You can customize the in the dialog. [](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Environment_Settings) tab's **Environment Settings** section.

The [Multiple Surnames feature](https://gramps-project.org/blog/2010/11/final-multiple-surnames/) might be used for patronymics or compound matrilineal-patrilinial names. Another variation would be a Scandinavian name like ‘Syver Ericksen Skotterud’ where the full name is composed of a forename (Syver), a reference to his father (Ericksen or son of Erick) together with a village or locality name. In such a case, you can add 'Ericksen' with an [Origin](wiki:Names_in_Gramps#Origin_Attributes) of "Patronymic" and expand to a Multiple Surnames by adding 'Skotterud' with an Origin of "Location".

If you do not add any information in this section then, on the next open of the Edit Person dialog, it will be hidden. Any empty rows will not be saved.

See also:

- [Multiple Surnames feature](https://gramps-project.org/blog/2010/11/final-multiple-surnames/) - Introduction Blog post on Gramps website.

{{-}}

#### Multiple Surnames section context menu

- \-

- \-

- \-

{{-}}

### General section

![[_media/EditPerson-General-section-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "General" section of the "Edit Person" - dialog - example]]

The General section has the following options you can change:

- [Privacy](#Privacy)
- [Gender](#Gender)
- [ID](#ID)
- [Tags](#Tags)

#### Privacy

- The Privacy Padlock icon toggle lets you mark whether or not the person's record is considered public or private.

Records are shown with  
![[_media/22x22-gramps-unlock.png]]unlocked padlock by default when public; and an ![[_media/22x22-gramps-lock.png]]locked padlock when private. Clicking the padlock icon toggles between Public and Private flags.

{{-}}

#### Gender

- The menu offers the choice of person's gender :
  - *female*
  - *male*
  - **unknown** (Default)
  - *other*

If the gender is left as then the dialog is shown.

See [Rebuild Gender Statistics](wiki:Gramps_6.0_Wiki_Manual_-_Tools#Rebuild_Gender_Statistics) tool and [Dump Gender Statistics](wiki:Gramps_6.0_Wiki_Manual_-_Tools#Dump_Gender_Statistics) debug.

##### Unknown gender specified dialog

![[_media/Unknown-gender-specified-dialog-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Unknown gender specified" dialog]]

The dialog will alert you that the gender of the person is currently unknown. Usually, this is a mistake. Please specify the gender by selecting from , , , to confirm. {{-}}

#### ID

- The field displays the [Gramps ID](wiki:Gramps_6.0_Wiki_Manual_-_Settings#ID_Formats) number which identifies the user in the Family tree uniquely. This value helps you distinguish between people who have the same name. You may enter any unique value you want. If you do not provide a value, Gramps will automatically select a value for you or the template for generating IDs can be changed to a format that suits.
  - Use to navigate.

#### Tags

- The area show the your custom assigned tags that specify some basic information on the status of your research.
  - The button brings up the dialog list that lets you remove or assign existing custom tags.

{{-}}

### Edit Person tab pages

The tabs reflect the following categories of personal data:

- (default)

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

#### Events

![[_media/EditPerson-Events-tab-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Events" tab from "Edit Person" - dialog - example]]

  
The tab lets you view and edit any events relevant to the person. The bottom part of the window lists all such events stored in the database and displays the following columns: `Type, Description, Date, Place, Main Participants, Private(lock icon), Role, ID, Age`. The top part shows the details of the currently selected event in the list (if any). The buttons , , and allow you to add, modify, and remove an event record from the database. Note that the and buttons become available only when an event is selected from the list. The Up "^" or Down "v" buttons allow you to "Move the selected event upwards/downwards or change family order" of the selected line, for Family relationships you can also use the dialog.

<!-- -->

  
When you use the button the selector dialog is shown allowing you to select an already existing event and edit it in the dialog.

<!-- -->

  
When you add a new event or edit an existing event, the dialog is shown.

{{-}}

##### Select Event selector

![[_media/SelectEvent-selector-dialog-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Select Event - selector - example]]

The selector dialog allows you to link to an already existing event and once selected it will be opened in the dialog.

The following columns are shown: `Type` (default sort for list), `Main Participants`, `Date`, `Place`, `Description`, `ID`, `Last Change`.

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

Use the button to reset the filter. {{-}}

#### Names

![[_media/EditPerson-Names-tab-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Names" tab from "Edit Person" - dialog - example]]

  
The tab lets you view and edit any alternative names the person may have. The name shown in the top of the [Edit Person](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1#Editing_information_about_people) dialog is the and is usually (but not necessarily) the Birth Name. might be other [Name Types](wiki:Names_in_Gramps#Name_Types) for aliases ('Also Known As' name type) for adopted names, pennames, stagenames or legal name changes. (Because it is so common, there is a separate alias Name type for "Married Name".) If alternative names exist, date ranges can be set for each. So a "Birth Name" may use one range (before the date of adoption) and a "Also known as" will have another range (after the date of adoption). Alternative names can also be spelling variants, including anglicized versions of the birth name and common misspellings.

<!-- -->

  
The bottom part of the window lists all alternate names for the person stored in the database. The top part shows the details of the currently selected name in the list (if any). The buttons (add), (edit), and (remove) allow the addition, modification, and removal of an alternate name from the database. Double-clicking a row is the same as selecting and clicking the (edit) button. Note that the and buttons become available only when an alternate name is selected from the list.

<!-- -->

  
Any row in the Alternative names may be set to the Preferred name from the context menu. Right-click the Alternative name and choose the menu choice. That Alternative names row will be swapped into the Preferred name section and the previous Preferred name will be demoted to the bottom of the Alternative names list.

<!-- -->

  
When adding a new name or editing an existing name, the dialog is invoked. This Names dialog is described in the [Name Editor section](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_3#Name_Editor)

{{-}}

#### Source Citations

![[_media/EditPerson-SourceCitations-tab-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Source Citations" tab from "Edit Person" - dialog - example]]

  
The tab allows you to view and document the source citations for the information you collect.

<!-- -->

  
These might be general sources that do not describe a specific event, but which nevertheless yield information about the person. For example, if Aunt Martha's memoirs mention her great-grandson Paul, the researcher may assume that this Paul actually existed and cite Aunt Martha's memoirs as the source that justifies this assumption.

  
The central part displays the list of all source references stored in the database in relation to the person. The buttons , , and allow you to correspondingly add, modify, and remove a source reference to this person. Note that the , and buttons become available only when a source reference is selected from the list.

<!-- -->

  
On edit you can change the data in the citation (unique to this person), as well as the shared source object, see [Editing Citations](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_2#Editing_source_citations).

{{-}}

#### Attributes

![[_media/EditPerson-Attributes-tab-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Attributes" tab from "Edit Person" - dialog - example]]

  
The tab lets you view and assign attributes to the person. You have complete freedom to define and use attributes. For example, attributes might be assigned to describe the person's physical characteristics or personality traits.

<!-- -->

  
Note that each attribute listed in the dialog consists of two parts: the Attribute itself and a Value associated with that Attribute. This so-called "Parameter-Value" pairing can help you organize and systematize your research. For example, if you define "Hair color" as an Attribute for a person, "Hair Color" will become a selectable Attribute for all other people. The Value of Hair Color for person A might be red, and brown for person B. In similar fashion, you might define an Attribute like "Generosity" and use the Value of "Enormous" to describe a particularly generous person.

<!-- -->

  
The bottom part of the dialog window displays the list of all Attributes stored in the database. The top part shows the details of the currently selected attribute in the list (if any). The buttons , , and let you add, modify, and remove an attribute record from the database. Note that the **Edit** and **-** buttons become available only when an attribute is selected from the list.

If you edit an attribute the opens.

{{-}}

#### Addresses

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

The following columns are shown: `Preview` (default sort for list), `ID`, `Type`, `Tags`, `Last Change`.

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

#### Gallery

![[_media/EditPerson-Gallery-tab-example-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Gallery" tab from "Edit Person" - dialog - example]]

  
The tab lets you view and store photos, videos, and other media objects that are associated with the person. The central part of the window lists all such media objects. Any object in the form of a valid image file will result in the display of a thumbnail view of the image. For other objects such as audio files, movie files, etc., a corresponding file type icon is displayed instead.

<!-- -->

  
The following options are available:

- \- allows you to add a new media object from the .

- \- brings up the selector dialog allowing you to link to an already existing media object.

- \- allows you to modify the select media object in the . This button only becomes available when a media object is selected from the list.

- \- remove the selected media object from the person's gallery. This button only becomes available when a media object is selected from the list.

- (Move left arrow) and (Move right arrow) buttons - allow you to rearrange the media items to select a particular one for main photo. You can change also change the order of the primary (active) image by selecting the image and dragging it to the first position.

{{-}}

###### Gallery context menu

![[_media/EditPerson-Gallery-tab-example-with-context-menu-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Gallery" tab from "Edit Person" - dialog - example with context menu]]

If you select a media object in the gallery a context menu (right-click) is available with the following options:

- 

- 

<hr>

- 

<hr>

- 

- 

- 

- 

##### Select Media Object selector

![[_media/SelectMediaObject-selector-dialog-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Select Media Object - selector - example with multiple selections]]

The selector dialog allows you to link to an already existing media object and once the image is selected it will be opened in the dialog.

Once you select an media object from the list a preview will be shown if possible in the top section.

The following columns are shown: `Title` (default sort for list), `ID`, `Type`, `Last Change`.

You may use the button to filter the list based on one of the options from the drop down list:

- **Title Contains**(default)
- *Title does not contain*
- *ID contains*
- *ID does not contain*
- *Type contains*
- *Type does not contain*
- *Last Change contains*
- *Last Change does not contains*

See also [Select a media object](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_2#Select_a_media_object_selector) file selector dialog.

{{-}}

#### Internet

![[_media/EditPerson-Internet-tab-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Internet" tab from "Edit Person" - dialog - example]]

  
The tab displays Internet addresses relevant to the [Person](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1#Internet), [Place](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_2#Internet), or [Repository](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_2#Internet_2). A descriptive caption of the Internet location you are storing. Type of internet address as needed to navigate to it, eg. <http://gramps-project.org>, E-mail, Web Page, ...

<!-- -->

  
The bottom part lists all such Internet addresses and accompanying descriptions. The top part shows the details of the currently selected addresses in the list (if any). The buttons , opens the dialog to add or edit and the removes the selected Internet address. The button opens your web browser and takes you directly to the highlighted page.

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
  - Any custom type you enter manually.

- toggle the privacy status of the record.

- The internet address as needed to navigate to it eg: <https://gramps-project.org>

  - open the web address in the default browser

- A descriptive caption of the Internet location you are storing.

See also

- [Link Editor](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_2#Link_Editor)
- [Note Link Report](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_6#Note_Link_Report)
- Search for a Person's Internet Address (Type, Web address, or Description) data with the [People with records containing <substring>](wiki:Gramps_6.0_Wiki_Manual_-_Filters#People_with_records_containing_.3Csubstring.3E) custom filter rule
- Search for a Repository's Internet Address (Type, Web address, or Description) data with the [Repositories matching parameters](wiki:Gramps_6.0_Wiki_Manual_-_Filters#Repositories_matching_parameters) custom filter rule

{{-}}

#### Associations

![[_media/EditPerson-Associations-tab-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Associations" tab from "Edit Person" - dialog - example]]

The tab lets you view and edit relationship role information about two persons explicitly associated in the database.

The associations tend to be roles that cannot be inferred from being connected in normal (or blended) family structure or through shared event roles. For instance, cousin or sibling relationships are apparent through how marriages connect the people. Relationships such as Godparents (a participant in a Christening), an organ donor (participant in a medical procedure), pall bearer (participant in a Burial), and Guardian (participant in a Probate or mentioned in a will) may be Roles created by sharing an event created for the Primary role person.

So Association roles are less obvious. They might be family friends, an eponym (the person honored by a namesake), a coworker, a penpal, or any other type of associations you may wish to record. If the closest relation is 'Godparent', then this would indicate that the Godparent of the person (being edited) is the person whose name is shown in the Associations tab.

The [*Associates* (ASSO) tag in the GEDCOM standard](http://wiki-en.genealogy.net/GEDCOM/ASSO-Tag) says that "a person's relation or association is the person being pointed to." You might choose to put a reciprocal Association in that other person's Associations tab.

In the association shown from [example.gramps](wiki:Example.gramps), Lewis Garner's Godfather is Anderson Garner. Use Events instead for relations connected to specific time frames or occasions. Events can be shared between people, each indicating their [role](wiki:Gramps_Glossary#role) in the event.

The button opens the dialog to add. The button allows you to edit and the removes the selected association. The other buttons or move the selected entry position in the list only.

See also:

- [Roles, Relationships &amp; Associations](wiki:Roles,_Relationships_&amp;_Associations)
- [Add a godfather-godmother](wiki:Add_a_godfather-godmother) ***Note:*** A "Godparent" role was added to the standard list of Event roles in the 5.2 Gramps version.

{{-}}

##### Person Reference Editor

![[_media/PersonReferenceEditor-dialog-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Person Reference Editor" - dialog - default]]

The lets you add and edit Association entries. You can access it from the s dialog tab.

- *To select a person, use drag-and-drop or use the buttons*

  - button brings up the selector dialog.

  - \- add a new person

- you can over type the default entry with anything you choose to be the association eg. *Friend*, *Neighbor* .

  - **Godfather** (Default)

- \- record is public (Default)

{{-}}

###### Source Citations tab

  
The tab allows you to view and document the source citations for the information you collect.

<!-- -->

  
These might be general sources that do not describe a specific event, but which nevertheless yield information about the person. For example, if Aunt Martha's memoirs mention her great-grandson Paul, the researcher may assume that this Paul actually existed and cite Aunt Martha's memoirs as the source that justifies this assumption.

  
The central part displays the list of all source references stored in the database in relation to the person. The buttons , , and allow you to correspondingly add, modify, and remove a source reference to this person. Note that the , and buttons become available only when a source reference is selected from the list.

<!-- -->

  
On edit you can change the data in the citation (unique to this person), as well as the shared source object, see [Editing Citations](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_2#Editing_source_citations).

{{-}}

###### Notes tab

  
The tab lets you view and edit any [Note](wiki:Gramps_Glossary#note) associated with the relationship. These could be any comments which do not naturally fit into the "Parameter-Value" pairs available to Attributes. To add a note or modify existing notes simply edit the text in the text entry field.

The option lets you set the way the note will appear in reports and web pages. If you select Flowed, the text generated will have single spaces put in place of all multiple spaces, tabs, and single end-of-line characters. A blank line inserted between two blocks of text will signal a new paragraph; additional inserted lines will be ignored.

If you select the Preformatted option, the text in reports and web pages will appear exactly as you enter it in the dialog.

{{-}}

###### Select Person selector

![[_media/SelectPerson-selector-dialog-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Select Person" - selector dialog - example]]

The selector dialog allows you to link to an already existing person.

You may select any surname to expand and find the person you want then select them and press . {{-}} See also:

- [Select a person for the report selector](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_4#Select_a_person_for_the_report_selector)

#### LDS

![[_media/EditPerson-LDS-tab-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "LDS" tab from "Edit Person" - dialog - example]]

The (Latter Days Saints) tab lets you view and edit information about LDS ordinances of the person. This information is inherited from the LDS's GEDCOM specification. The LDS tabs in the Family Editor and the Person Editor can be hidden via the : Latter Days Saints checkbox under the **** section of the tab in the .

At the top of the tab you can use the following buttons to or buttons to bring up the dialog; and or in the list.

The following columns for the list are shown: `Source` (icon), `Private` (lock icon), `Type`, `Date`, `Status`, `Temple`, `Place`.

See also:

- Person Editor dialog's tab
- Family Editor dialog's tab - only displays information about the LDS Sealed to Spouse Ordinance.
- You can hide these tabs by changing the associated option in tab's **** section.

{{-}}

##### LDS tab context menu

You can use the context menu on a selected entry to:

- 

- 

- 

{{-}}

##### LDS Ordinance Editor

![[_media/LDSOrdinanceEditor-dialog-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "LDS Ordinance Editor" - dialog - default]]

Use the dialog to add or edit existing LDS ordinances for the person.

These LDS are for:

- **Baptism** (default)
- *Endowment*
- *Confirmation*
- *Sealed to Parents*

Each ordinance is further described by its , , and as well as an additional entry for, that is shown only for the *Sealed to Parents* ordinance.

Each ordinance can be further described through the selections available in the drop-down options:

- **<No Status>** (default)
- *Born in Covenant*
- *Cleared*
- *Completed*
- *Do not seal*
- *Pre-1970*
- *Qualified*
- *Stillborn*
- *Submitted*
- *Uncleared*

In the bottom section tabs you can also include sources citations and notes:

- [Source Citations tab](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1#Source_Citations_tab_2)
- [Notes tab](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1#Notes_tab_2)

See also:

- [Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1#LDS_2](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1#LDS_2)
- [Ordinance (Latter Day Saints)](https://wikipedia.org/wiki/Ordinance_(Latter_Day_Saints)) on [Wikipedia](https://wiktionary.org/wiki/Wikipedia#Etymology).

{{-}}

###### Source Citations tab

{{-}}

###### Notes tab

{{-}}

#### References

![[_media/EditPerson-References-tab-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "References" tab from "Edit Person" - dialog - example]]

The tab lists other Objects that are explicitly backlinked to the Person: Families where the Person is a spouse or child, Persons who have an Association, and Notes where the Person has been linked.

It does not list secondary linked object: objects (like Events, Citations, Media, Places, Tags) that are linked under the Person

Double-clicking a row in references opens the Editor for that referring object. {{-}}

## Editing information about relationships

Information about relationships is entered and edited through the dialog.

This dialog may be invoked in a number of ways:

- From the menu: select or use its [Keybinding](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings#xx).

<!-- -->

- From [Relationships Category](wiki:Gramps_6.0_Wiki_Manual_-_Categories#Relationships_Category): click on an button in the family that you want to edit. Or from the select: , , or .

<!-- -->

- From [Families Category](wiki:Gramps_6.0_Wiki_Manual_-_Categories#Families_Category): select the family in the list and then click the button on the Toolbar, or double-click on the family. Or from the menu, select .

<!-- -->

- From [Charts Category](wiki:Gramps_6.0_Wiki_Manual_-_Categories#Charts_Category): point your mouse over the black line connecting the spouses, right-click and select from the context menu, or double-click on the black line.

Any of these methods will prompt you with the dialog:

{{-}}

### Family Editor dialog

![[_media/FamilyEditor-dialog-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}}  dialog - showing example family and &quot;Quick View&quot; context menu]] The allows you to add or edit all the aspects of a family: the people (children,parents), their relationships to one another, the roles they play in events. The Family structure provides the context that Gramps needs to occasionally guess likely surnames, genders, roles, and Relationship or Event types.

Children added to a family are guessed to be birth children of (biologically related to) the parents and to inherit a surname guessed from the parents. But that can be changed manually with the [Child Reference Editor](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data%3A_detailed_-_part_1#Child_Reference_Editor). That editor appears when a child is added to a family. And it can be called to edited afterwards by double-clicking a child in the [Family Editor](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data%3A_detailed_-_part_1#Family_Editor_dialog).

A parent added to a family will have a guessed gender from the role (Father/Partner1 or Mother/Partner2) and possibly a surname.

Family Events with (the default [event role](wiki:Gramps_Glossary#event_role) of Family) apply to both spouses/partners in a family. This eliminates the need to make duplicate Events (and keep those Events harmonized) or to share an Event between the Father/Mother (Partner1/partner2) of a Family.

Families have [default relationship types](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Input_Options) and implicit [event roles](wiki:Gramps_Glossary#event_role). When Events are added in the Family Editor, the Event Role will be of "Family" role by default. And the first event added will be of [Marriage](#Marriage) type and the second will be of [Divorce](#Divorce) type. If Events are shared, the Event will be of "Unknown" role and need to be set to the appropriate role.

The top section of the window shows the names of the people whose relationship are being edited, as well as their birth and death information.

- - button opens the

  - button opens the dialog.

- - button opens the

  - button opens the dialog.

The button lets you mark whether or not the family record is considered public or private.

[Quick View](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_8#Quick_Views) reports are available by using the context menu(right clicking) from a blank area in the top section of the window.

##### Family Editor context menu

The following [Quick View](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_8#Quick_Views) reports are available from the context menu:

- 

- 

#### Relationship Information

The section displays three fields have the basic description of the relationship.

- field displays the ID number which labels this relationship in the database, leave this field empty to have Gramps generate a unique ID number.

<!-- -->

- shows a drop-down list of the available types of family relationships such as `Civil Union`, `Married`, **`Unknown`**(default), `Unmarried`, etc.) or add a [Custom Type](wiki:Gramps_Glossary#custom).

  - You can also set the  - used by the Family Editor dialog in
  - [How do I represent a divorce?](wiki:Indicate_a_divorce)
  - You can use the [](wiki:Addon:FamilyRelationship) addon to change the family relationship type for a selected group of filtered families.

<!-- -->

- displays shows the [tags](wiki:Gramps_6.0_Wiki_Manual_-_Filters#Tagging) you have created to show some basic information on the status of your research. You can add additional tags by selecting the button.

Below them are a number of [notebook tabs](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1#Family_Editor_tab_pages) are shown representing different categories of information about the relationship. Click any tab to view or edit the information it contains.

In the bottom part of the window you can click the button at any time to apply all the changes made in all tabs and close the dialog window. Clicking the button at any time will close the window without applying any changes. If any of the data in any tab is modified, an alert window will appear that will prompt you choose between closing the dialog without saving changes, canceling the initial cancel request, or saving the changes.

#### Select Father selector

![[_media/SelectFather-selector-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Select Father - selector]] The selector dialog allows you to link to an already existing Person as the Father.

You can either browse to the person or use the

- : the selector is filtered to Person with a *Male* gender. Persons with Unknown, Other and Female genders will not be listed. Selecting button and then turns off this filtering.

{{-}}

#### Select Mother selector

![[_media/SelectMother-selector-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Select Mother - selector]] The selector dialog allows you to link to an already existing Person as the Mother.

- : the selector is filtered to Person with a *Female* gender. Persons with Unknown, Other and Male genders will not be listed. Selecting button and then turns off this filtering.

{{-}}

### Family Editor tab pages

The tabs provide the following information categories of relationship data:

#### Children

![[_media/FamilyEditor-dialog-Children-tab-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Children" tab from "Family Editor" - dialog - example]]

  
The tab lets you view and edit the list of children who are part of this relationship. The button allows entering a new person to the database and adding that person as a child in this relationship. The button lets you select an existing person to be a child in the relationship. The button opens the dialog that allows for editing the relations between the selected child and the parents. Finally, the lets you remove the selected child from the relationship. Note that the and buttons become available only when a child is selected from the list.

[How do I change the order of children?](wiki:Gramps_6.0_Wiki_Manual_-_FAQ#How_do_I_change_the_order_of_children.3F)

- Use this [Children](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1#Children) tab in the Family Editor to change the order of children in the active family.
- Use the third-party addon tool which allows bulk updates of the children order.

See also:

- The [Children](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Children) gramplet in the [People Category](wiki:Gramps_6.0_Wiki_Manual_-_Categories#People_Category) views displays all children from **all marriages** for the active person. Children are displayed as ordered in the family record(s).

{{-}}

##### Select Child selector

![[_media/SelectChild-selector-dialog-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Select Child - selector - example]]

The selector dialog allows you to link to an already existing child and once selected will be opened in the

The following columns are shown: `Name` (default sort for list), `ID`, `Gender`, `Birth Date`, `Birth Place`, `Death Date`, `Death Place`, `Spouse`, `Last Change`. {{-}}

##### Child Reference Editor

![[_media/ChildReferenceEditor-dialog-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;Child Reference Editor&quot; - example]] The dialog allows editing of the relationship between the selected child and the parents in a Family. The dialog appears when initially committing a Person as offspring in a Family. The final step of using the Share button, the (Create an new person) button or using "drag and drop" to add someone to the family is to confirm the Relationship.

The Relationships may also be edited for existing children of shown in the Edit Family dialog. Double-clicking on an existing child in a Family or selecting the context menu item will open the Child Reference Editor for the selected child. (Selecting the context menu item will open the Edit Person dialog instead.)

While a Person will only have a Birth relationship to both parents in a traditional Birth family, they might also be part of multiple blended families. In those families, a birth parent re-marries and the other spouse can have a more complex relationship withe children of a previous marriage. But it they are part of the household, those children should be added to the new Family with the appropriate relationship.

The following options are available:

- The name of the child

  -  button.

- Select from the drop down list of possible relationship types:

  - *Adopted*
  - **Birth** (default)
  - *Foster*
  - *None*
  - *Sponsored*
  - *Stepchild*
  - *Unknown*

- Select from the drop down list of possible relationship types:

  - *Adopted*
  - **Birth** (default)
  - *Foster*
  - *None*
  - *Sponsored*
  - *Stepchild*
  - *Unknown*

- privacy toggle for this relationship.

{{-}} Also the following tabs are available:

- Source Citations
- Notes

###### Source Citations tab

  
The tab allows you to view and document the source citations for the information you collect.

<!-- -->

  
These might be general sources that do not describe a specific event, but which nevertheless yield information about the person. For example, if Aunt Martha's memoirs mention her great-grandson Paul, the researcher may assume that this Paul actually existed and cite Aunt Martha's memoirs as the source that justifies this assumption.

  
The central part displays the list of all source references stored in the database in relation to the person. The buttons , , and allow you to correspondingly add, modify, and remove a source reference to this person. Note that the , and buttons become available only when a source reference is selected from the list.

<!-- -->

  
On edit you can change the data in the citation (unique to this person), as well as the shared source object, see [Editing Citations](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_2#Editing_source_citations).

{{-}}

###### Notes tab

  
The tab lets you view and edit any [Note](wiki:Gramps_Glossary#note) associated with the relationship. These could be any comments which do not naturally fit into the "Parameter-Value" pairs available to Attributes. To add a note or modify existing notes simply edit the text in the text entry field.

The option lets you set the way the note will appear in reports and web pages. If you select Flowed, the text generated will have single spaces put in place of all multiple spaces, tabs, and single end-of-line characters. A blank line inserted between two blocks of text will signal a new paragraph; additional inserted lines will be ignored.

If you select the Preformatted option, the text in reports and web pages will appear exactly as you enter it in the dialog.

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

![[_media/LDSOrdinanceEditor-dialog-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Sealed to Spouse ordinance editor of &quot;Edit Family&quot; - dialog - example]] The (Latter Days Saints) tab of the Family Editor only displays information about the LDS **Sealed to Spouse** . (The ordinances related to individuals can be recorded in [LDS tab of the <strong>Person</strong> Editor](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1#LDS).) The LDS tabs in the Family Editor and the Person Editor can be hidden via the "Hide LDS tab is person and family editors." checkbox under the **** section of the tab in the .

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

The main part of the Family Editor’s tab displays a table of the five different kids of data in a each record. Click a column header to row or double-click a row to edit its contents. The bottom part of the window has and buttons. Clicking will apply all the changes made in all tabs and close the dialog window. Clicking the button will close the window without applying any changes.

See also:

- Person Editor dialog's tab
- Family Editor dialog's tab - only displays information about the LDS Sealed to Spouse Ordinance.
- You can hide these tabs by changing the associated option in tab's **** section.

{{-}}

## Editing dates

This section describes how to enter and modify dates. Since dates are so important in genealogical research, Gramps takes special care to preserve and use any date information available.

Information can be entered into a date field by directly typing it or by invoking the dialog by clicking the ![[_media/22x22-gramps-date.png]] button next to any entry field.

See also:

- [Gramps 6.0 Wiki Manual - Probably Alive](wiki:Gramps_6.0_Wiki_Manual_-_Probably_Alive)

- in the **Calculation limits** section - To change the default values for the typical ages at birth, between generations, etc.

### Date selection dialog

![[_media/DateSelection-dialog-defaults-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}}  - dialog - default]]

While the below [parsing rules](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1#Date_formats_and_parsing_rules) provide a guide for you to type in most common dates, you can also use dialog. The dialog is particularly useful for building a complex date or for simply insuring that your information is entered in a way Gramps will understand.

The following fields are available:

- Choose alternate [calendar type](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1#Calendars).

  - [**Gregorian**](https://wikipedia.org/wiki/Gregorian_calendar) (default)
  - *[Julian](https://www.familysearch.org/wiki/en/Julian_and_Gregorian_Calendars) (including [Mixed](wiki:Dates#Dual_Dated)/[Dual](#Dual-dated_dates) dates)*
  - *[Hebrew](https://wikipedia.org/wiki/Hebrew_calendar)*
  - *[French Republican](https://www.familysearch.org/wiki/en/French_Republican_Calendar)*
  - *[Persian](https://wikipedia.org/wiki/Iranian_calendars#Old_Persian_calendar)*
  - *[Islamic](https://wikipedia.org/wiki/Islamic_calendar)*
  - *[Swedish](https://www.familysearch.org/wiki/en/Sweden_Feast_Day_Calendars)* - [Swedish calendar](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1#Swedish_calendar)

-  This field is select-able with the matching field if the alternate supports [dual dating](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1#Dual-dated_dates). (checkbox unchecked by default)

  - (Empty text field by default)

- Set the [date quality](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1#Date_Quality).

  - **Regular**(default)
  - *Estimated*
  - *Calculated*

- Set the interval precision or time frame [date type](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1#Date_Type).

  - **Regular**(default) - the interval spanning a specific day, month or year (without regard to time zone)
  - *Before*
  - *After*
  - *About*
  - *Range* - the field will be available to set a date.
  - *From*
  - *To*
  - *Span* - the field will be available to set a date.
  - *Text only*

- Select the , and the .

- If your date is *Range* or *Span*, this option will be available to set a date.

- text entry field allows storing an arbitrary text string along with the date.

Also at the bottom of the dialog you have the , and buttons; as well as a status line area just below the buttons that provides feed back about issues with the date entry if any.

{{-}}

### Date validity indicators

![[_media/DateSelection-dialog-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Date selection" dialog - example]]

Gramps uses a date validator.

While partial dates do not uniquely define the day, they allow at least for some type of comparisons between the dates.

The date field will highlight in red and display a red symbol (such as a stop sign or cross) to indicate the entered date is not recognized as a recognized and valid format for a date.

Examples of common date references that are not recognizable Gramps formats might be "Christmas week of '61", "Fall 1782", or "the summer when I had surgery". In such a case, the date will be stored as string and marked as *Text only* type. Any dates of this Type will not be compared to other dates. Wherever possible, it is preferable to avoid such *Text Only* date entries. It might be better, for example, to enter a date of "December 1961" and then to add the Description annotation "Christmas week of '61." It would be more precise to check a calendar for December 1961 then key in the actual date span... but still include the annotation. The annotation is needed because you cannot assume that 'Christmas week' means the same span of days to you as to your source. There could be culture bias to color the interpretation. It could mean the calendar row containing Christmas day. But American & European calendar rows start on different days of the week. Or, it could mean the 7 days starting with Christmas or even the 7 days leading up to Christmas. So the span allows searches and comparisons but the annotation shows that actual interval is subject to interpretation.

In the various views (such as the ), unrecognized dates will be displayed in **bold** by default. The text markup (formatting style) for unrecognized dates can be modified by changing the option in the section of the [tab](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Environment_Settings) of [Preferences](wiki:Gramps_6.0_Wiki_Manual_-_Settings).

When a Birth or Death date is missing for a Person, the dates of existing fallback Events in the same category may be shown (and indicated with italics with an abbreviated title) rather leaving the display blank. So, a Burial or Cremation date will be shown if a Death date has not yet been recorded.

{{-}}

### Date Quality

- *Regular*: A "regular" date is one with an explicit day, month, or year.

<!-- -->

- *Estimated*: An "estimated" date is one based on average interval assumptions offset from a known reference date. (Such as the average number of years between generations, maximum lifespan, or length of sea voyage.)

<!-- -->

- *Calculated*: A "calculated" date is one based on a known interval from a reference date but without a source explicitly mentioning the date. (Such as a gravestone engraved with both a date of death and a precise age at death.)

Census data is unusual in that it seems to a candidate for a Calculated date but is not. The census often explicitly defines the interval (age) and the reference date (census polling date) but that age is often estimated or rounded.

### Date Type

To the right of the should appear the pop-up menu.

Dates in Gramps are classified according to the following types of precision (scale) of interval or time frame:

- **Regular**: A "regular" date is one which includes an interval spanning a specific day, month, or year. It can be complete (or 'fully qualified' for a 24 hour interval like June 6, 1990) or partial (like omitting the day for a 1 month interval like July 1977 or omitting the day and month for a 1 year interval).

<!-- -->

- **Before**: A "before" date is one that can only be identified as occurring (in a [preferences-defined long interval](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Dates)) prior to a certain day, month, or year. *(By default, the interval is 50 years.)*

<!-- -->

- **To**: A "to" date is one that is an open-ended span as that occurs prior to a certain day, month, or year. Unlike a "before" Date type, the span is unlimited into the past.

<!-- -->

- **From**: A "from" date is one that is an open-ended span that following a certain day, month, or year. Unlike an "after" Date type, the span is unlimited into the future.

<!-- -->

- **After**: An "after" date is one that occurs (in a [2nd preferences-defined long interval](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Dates)) following a certain day, month, or year. *(By default, the interval is 50 years.)*

<!-- -->

- **About**: An "about" (circa) date is one that occurs (in [yet another preferences-defined ±years interval](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Dates)) before **or** after a certain day, month, or year. *(By default, the interval is ±50 years.)*

<!-- -->

- **Range**: A "range" describes a time period during in which the event occurred. It could be recurrent event during the interval or a single instance believed to have occurred between known boundary dates.

  
For example, "between January 1932 and March 1932."

- **Span**: A "span" describes an inclusive time period during which a condition continually existed.

  
For example, "from May 12, 2000 to February 2, 2002."

### Date formats and parsing rules

The dialog just helps layout a date in the standard format that Gramps knows how to parse. It is useful while you're unfamiliar with the options, need to use an alternative calendar or specify a New Year begins date.

Gramps recognizes dates entered in a variety of formats. The default numeric format is that which is conventional for the environment is which Gramps is operating; that is, *DD.MM.YYYY* for most European countries, *MM/DD/YYYY* for the U.S., and so on. A way to avoid this ambiguity is to always choose a *d mmm yyyy* or *mmmn d yyyy* format. It will parse month and month abbreviations entered in the currently active language.

It will also parse dates entered in Quarters and convert them into "between" spans. e.g., "q2 1820" becomes "between 1 Apr 1820 and 30 Jun 1820".

Besides exact dates, Gramps recognizes many date types that are not regular: before, to, from, after, about, ranges and (from/to or between) spans. It also understands the quality: estimated or calculated. Finally, it supports partial dates and many alternative calendars. Below is the list of date entry rules to allow precise date parsing.

**Regular single dates** can be entered just as you would write them. And typing a slash after the year followed by a value 1 year later creates a Julian dual-dated entry.

  
Examples: "May 24, 1961" ; "31 Dec 1858/9" or "January 1, 2004".

**Before the Common Era** (BCE, BC and B.C.E.) and are notations for the Gregorian or Julian calendars. "Common Era" and "Before the Common Era" are religiously neutral alternatives to the familiar Anno Domini (AD) and Before Christ (BC) notations used for the same calendar era. The notation will be harmonized to the "B.C.E." form.

  
Examples: "c. 25 Dec 32 BC Julian" becomes "about 25 Dec 32 B.C.E. (Julian)"

**Partial dates** are entered simply by omitting unknown information.

  
Examples: May 1961 and 2004.

Dates that are not Regular should start with the keywords of *Estimated* or *Calculated* , if applicable.

  
Example: est. 1961, or calc 2005. (Note that a does not need to be specified for regular dates.)

The menu options can also be set to *Before*, *To*, *From* *After*, or *About* by simply typing "before", "to", "from", "after" or "about" before a single date in the Event Editing dialog.

If the desired is a range, write "between DATE and DATE", and if the is a span, write "from DATE to DATE".

  
Examples: est from 2001 to 2003, before June 1975, est circa 2000, calc between May 1900 and January 1, 1990.

Here are a couple examples to try:

  
Captain John Smith has been stationed in the 1st Grenadier regiment between 1888-5-13 and 1902-10-24 according to his military record (words "between" and "and" intentionally used as this is the way we talk in day-to-day life); Then date should be coded "from … to …" because this is the duration of his duty.

<!-- -->

  
Captain John Smith's regiment was posted to the Escaut river at Valenciennes the week before the Armistice.  
*Then this can be recorded as a "Military Service" Event type with a date of "between Nov 4 1918 and 11 Nov 1918" (Gramps will convert to a standard date format despite 2 formats being used for entry) at River Escaut, Valenciennes, Noord department, France... because the actual date for this "instantaneous" event is not known in the source.*

### Calendars

Alternate calendars are calendars other than the Gregorian calendar. Currently, Gramps supports Hebrew, French Republican, Julian, Islamic, Persian, and Swedish alternate calendars. To specify the calendar other than the default Gregorian, append the name of the calendar to the date string, e.g. "January 9, 1905 (Julian)" or use the drop down menu.

#### Swedish calendar

The [Swedish king](wiki:Swedish_kings), Karl XII, decided that Sweden should start using the Gregorian calendar. However, it was planned to take place gradually by skipping 11 leap days starting 1700-02-29 and end by 1744. So 1700-02-28 was followed by 1700-03-01. This took place during the Great Nordic War and the leap days were kept 1704 and 1708. In January 1711 the same king decided that Sweden should return to the Julian Calendar by 1712-03-01. In order to be in phase, an extra day was inserted on 1712-02-30. And that was the end of the Swedish Calendar. Sweden converted to Gregorian in 1753-03-01, by skipping dates between 1752-02-18 and 1753-02-28.

In Gramps you can only enter valid dates for the Swedish Calendar from 1700-03-01 to 1712-02-30. All other dates are flagged as not valid and has to be corrected.

### Dual-dated dates

Dual-dated dates (also called "double dating", "slash dates", and sometimes "Old Style/New Style" dates) appear like "Jan 23, 1735/6". Often mistaken as a year uncertainty, this actually has a specific historic meaning. The dual dated date represents a time when an area was in a transition between moving to January 1 as the beginning of the new year. Thus Jan 23, 1735/6 is an indication to make it clear what date is being referred to. In this example, "Jan 23, 1736" might have occurred after "Jun 23, 1736".

England and the American colonies didn't officially accept the "Jan 1" as the new year date until 1752. Before 1752, the English government still officially observed March 25 as the first of the year, whereas most of the English population observed January 1 as the first of the year. Many people therefore wrote dates falling between January 1 and March 25 in the dual-dated format.

Sometimes, a dual date may appear as a fraction, as in this grave stone (170 and 3/4, which means 1703 and 1704) (See Fig. {{#var:chapter}}.{{#expr:{{#var:figure}}+1}}):

![[_media/Gravestone.jpg|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Gravestone showing dual date as a fraction (170 and 3/4, which means 1703 and 1704)]]

Marking a date as dual dated can be done by simply putting a slash `/` between the years. For example:

- 1721/2
- 1719/20
- 1799/800

These slash-years can appear anywhere in a date that a regular year can appear.

Dual-dated dates are currently represented in the Julian calendar so their month and day will be the same as that in the textual representation. {{-}}

#### Alternate new year day

With dual-dated dates (and other dates) you may know that the new year was celebrated on a day other than January 1. To indicate this in Gramps, put the month/day code in Parentheses or round brackets `()` , after the calendar (if one). For example:

- Jan 20, 1865 (`Mar25`)
- Jan 20, 1750 (`Julian`,`Mar1`)
- Feb 23, 1710/1 (`Mar25`)

To indicate the beginning of a year that is different from that of January 1, you use the following date codes :

- `Jan1`
- `Mar1`
- `Mar25`
- `Sep1`

You can put that as the only item in parenthesis, or right after a calendar name (comma, and no space).

Note that if new year's day is not Jan 1, then January will come after December that year. Dates with these new year day codes will be sorted appropriately.

{{-}}

[Category:Documentation](wiki:Category:Documentation)
