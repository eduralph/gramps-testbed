---
title: 'Gramps 6.0 Wiki Manual - Entering and editing data: detailed - part 2'
categories:
- Documentation
- Stub
managed: false
source: wiki-scrape
wiki_revid: 131187
wiki_fetched_at: '2026-05-30T11:12:20Z'
---

{{#vardefine:chapter\|9.2}} {{#vardefine:figure\|0}} **<span style="font-size:120%">Entering and editing data: detailed Events, Media, Places, Source Citations, Notes</span>**  
The previous section offered you a detailed overview of how to enter and edit data for people, relationships and dates. This section continues with other objects you encounter in Gramps.

## Editing information about events

![[_media/EventsCategory-EventsListView-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Events Category - Events (List) View - example]]

Adding an Event to a person allows you to record information you have found.

When adding an event to the , the dialog appears.

To add or edit event data, switch to the Category View and select the desired entry in the list of events. Double-click on that entry or click on the toolbar to invoke the following dialog. {{-}}

### New Event dialog

![[_media/EditEvent-dialog-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Edit Event - dialog - example]] When Events are edited through the dialog. This dialog can be accessed by: double-clicking a row in the Event category view. Events can also be edited in the [tab](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1#Events) of the dialog, or the [tab](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1#Events_2) of the dialog. When editing events via the Person Editor or the Family Editor the [Event Reference Editor dialog](#Event_Reference_Editor_dialog) is used.

The top part lets you view and edit basic information about the event:

- The can be selected from the available types listed in the Event type drop-down menu. e.g., **Birth** (*default*), Baptism, Death, Burial, etc. Gramps  
  You can enter you own Event [Custom Types](wiki:Gramps_Glossary#custom) by typing directly into the textbox portion of the [selector combo box](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window#Selector_Combo_Boxes).
- The of the event can be an exact date, a range (*from ... to ..., between ...*), or an inexact date (*about ...*).
  - ![[_media/22x22-gramps-date.png]] button starts the dialog.
- The field gives you the opportunity to give a longer description what this event is.
  - \- Toggle the Privacy lock to mark the event record as private which allows it to be omitted from reports.
- The can be selected from a list of previously entered place using the button or entered anew using the button. Additionally, you can drag and drop a place entry into this field.
- The is a unique identifier for the event. Leave this field blank to allow Gramps to generate this value automatically for new events.
- The allow you to select an existing tag using the button.

At the bottom of the window are the and buttons. Clicking will apply all the changes made in all tabs and close the dialog window, unless you have not entered data then you will be shown the warning. Clicking the button will close the window without applying any changes. Selecting will bring you here.

#### New Event tab pages

The central part of the window displays tabs containing different categories of information. Click on a tab to view or edit its contents. The tabs provide the following information categories of the event data:

##### Source Citations

  
The tab lets you view and edit sources relevant to an event. The central part of the window lists all such source references stored in the database. The buttons , , and let you add, modify, and remove a source reference associated with an event. Note that the and buttons become available only when a source reference is selected from the list.

##### Notes

  
The tab provides a place to record notes or comments about the event. To add a note or modify existing notes simply edit the text in the text entry field.

##### Gallery

  
The tab

##### Attributes

  
The tab

##### References

  
The tab

{{-}}

#### Cannot save event warning dialog

![[_media/Cannot-save-event-warning-dialog-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Cannot save event - warning dialog]]

warning dialog. No data exist for this event. Please enter data or cancel the edit. Press to return to the . {{-}}

## Editing event references

Event references connect a Event to a person and allow you to provide additional information about the event.

When adding event references to a tab, the dialog appears.

{{-}}

### Event Reference Editor dialog

Accessing the [reference object editor](wiki:Gramps_Glossary#reference_object_editor) .

![[_media/EventReferenceEditor-dialog-default-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Event Reference Editor - dialog]]

The dialog includes two sections, and .

- The section indicates the details associated with the particular reference to this Event: , , , .
- The displays : , , , , , .

{{-}}

#### Reference Information

##### Reference Information tab pages

###### General

For the of the person in this event, use the Role [selector combo box](wiki:Gramps_Glossary#selector_combo_box). Select **[Primary](wiki:Gramps_Glossary#primary)** (which is the *default* during an Add Event) option for the main beneficiary. Select a descriptive Event Role (e.g., [Aide](wiki:Gramps_Glossary#aide), [Bride](wiki:Gramps_Glossary#bride), [Celebrant](wiki:Gramps_Glossary#celebrant), [Clergy](wiki:Gramps_Glossary#clergy), [Family](wiki:Gramps_Glossary#family_role), [Godparent](wiki:Gramps_Glossary#godparent), [Groom](wiki:Gramps_Glossary#groom), [Informant](wiki:Gramps_Glossary#informant), [Witness](wiki:Gramps_Glossary#witness)) for a Events where the Person is not the Primary participant.

Events added to a Person via the Share or by drag'n'drop will be assigned the **[Unknown](wiki:Gramps_Glossary#unknown)** Event Role by default. If the Person holds an equal Role, set their Role to Primary as well.

If none of the pre-defined Roles are appropriate, add a Role *[Custom Types](wiki:Gramps_Glossary#custom)* in text box portion of the [selector combo box](wiki:Gramps_Glossary#selector_combo_box). Keyboarding in the new, unique Role name (rather than selecting one from the pull-down menu) creates a new Role custom type. New Role custom types will be added to the pull-down menu list. It remains there until the Tree is exported & re-imported or cleaned via a [Third party addon](wiki:Third-party_Addons) Utility like [Type Cleanup](wiki:Addon:Types_Cleanup_Tool).

Some example Custom Types for Event Roles are suggested in the [Roles, Relationships and Associations](wiki:Roles,_Relationships_%26_Associations) article. {{-}}

###### Source Citations

{{-}}

###### Attributes

###### Notes

{{-}}{{-}}

#### Shared Information

{{-}}

###### General

{{-}}

###### Source Citations

{{-}}

###### Attributes

{{-}}

###### Notes

{{-}}

###### Gallery

{{-}}

###### References

{{-}}

## Editing information about media objects

To add or edit media data objects, switch to the Category View and for existing media object select the desired entry in the media list. Double-click on that entry or click on the toolbar to open the editor dialog to edit existing information. Or select the button on the toolbar to see both the editor dialog and the dialog to select and then modify the media objects details before adding it.

### New Media dialog

![[_media/NewMediaEditor-dialog-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} New Media Editor - dialog - example showing Media properties]]

The top section presents a thumbnail of the media object if available, along with a summary of its properties (ID, Date, Path and *object type*) that you can view and edit. You can type this information directly into the corresponding fields.

- A descriptive for this media object. Either generated based on the media objects filename automatically or entered manually.

- The is an unique record to identify the media object, leave blank to have it generated by Gramps.
  - Privacy toggle for this media object (default) or

- type a date associated with the media object (eg: for a picture it could be the date it was taken.) You can also use the:

  - ![[_media/22x22-gramps-date.png]] button to invoke the dialog.

- of the media object on your computer. Gramps does not store the media internally, it only stores the path! Set the in the 's entry to avoid retyping the common base directory where all your media is stored. The tool can help managing paths of a collection of media objects.

  - button.

- button button brings up the dialog list that lets you remove or assign existing custom tags.

The bottom section of the window displays four notebook tabs containing different categories of information. Click on a tab to view or edit its contents. The bottom part of the window has the button to bring you here, the button will close the window without applying any changes and the button will apply all the changes made in all tabs and close the dialog window.

Double clicking on the thumbnail will open the media object in an external viewer if available.

#### Cannot save media object warning dialog

![[_media/Cannot-save-media-object-warning-dialog-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Cannot save media object - warning dialog]]

The warning dialog is shown when you have not entered enough information about the new media object. Please enter data or cancel the edit. {{-}}

### New Media tab pages

The tabs represent the following categories of media data:

- 

- 

- 

- 

#### Source Citations

The tab lets you....

#### Attributes

The tab lets you view and edit particular information about the media object that can be expressed as Attributes. The bottom part displays the list of all such attributes stored in the database. The top part shows the details of the currently selected attribute in the list (if any). The buttons , , and let you add, modify, or remove an attribute. Note that the and buttons become available only when an attribute is selected from the list.

#### Notes

The tab provides a place to record various information about the source that does not fit neatly into other categories. This area is particularly useful for recording information that does not naturally fit into the "Parameter/Value" pairs available to Attributes. To add a note or modify existing notes simply edit the text in the text entry field.

#### References

The tab indicates any database records that refer to a given media object. The list can be ordered according to any of its column headings: `Type`, `ID`, or `Name`. Double-clicking an entry allows you to view and edit the corresponding record.

{{-}}

## Editing media object references

When Media Object references connect a Media Object to another object on a tab, the button will bring up the file chooser and once you select a Media Object the dialog appears.

{{-}}

### Select a media object file chooser

![[_media/SelectAMediaObject-file-selector-dialog-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Select a media object - (File) chooser Dialog - example]]

The [file chooser](wiki:Gramps_6.0_Wiki_Manual_-_Settings#File_Chooser) allow you to preview and select a media file you want to attach, and at the same time you may edit the shown (Defaults to the filename without the file extension).

- (checkbox unchecked by default until checked for the first time and remembered for each subsequent image selection.)

See also:

- [Select Media Object selector](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1#Select_Media_Object_selector)
- [Family Tree's Media path &gt; Base media path:](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Family_Tree.27s_Media_path)

<!-- -->

- [](wiki:Gramps_6.0_Wiki_Manual_-_Tools#Media_Manager) a group of four separate tools two of which allow you to:
  - 

  - 

{{-}}

### Media Reference Editor dialog

![[_media/MediaReferenceEditor-dialog-collapsed-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Media Reference Editor - dialog - collapsed default example]]

The dialog.

See also [How to create image reference regions](wiki:How_to_create_image_reference_regions) {{-}} ![[_media/MediaReferenceEditor-dialog-expanded-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Media Reference Editor - dialog - &quot;Shared Information&quot; section expanded example]]

You may also expand the **Shared Information** section.

{{-}}

#### Top section

##### Top section tab pages

###### General

- Region corners : x1, x2, y1, y2.

The part allows to select a specific region on the Media Object. You can use the mouse cursor on the picture to select a region, or use these spinbuttons to set the top left, and bottom right corner of the referenced region. Point (0,0) is the top left corner of the picture, and (100,100) the bottom right corner.

- Privacy

The button lets you mark whether or not the record is considered private. Check the record box to mark this .

See also the [Narrated Web Site](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_7#Page_Generation) Gallery tab supports output of these referenced regions.

{{-}}

###### Source Citations

{{-}}

###### Attributes

{{-}}

###### Notes

{{-}}

#### Shared Information

##### Shared Information tab pages

###### General

{{-}}

###### References

{{-}}

###### Source Citations

{{-}}

###### Attributes

{{-}}

###### Notes

{{-}}

## Editing information about places

To edit information about places, switch to the and select the desired entry from the list of places. Double-click that entry or click the button on the toolbar to bring up the dialog:

{{-}}

### Place Editor dialog

![[_media/PlaceEditor-dialog-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Place editor - dialog - existing place example]]

To add a new place or edit information about existing places, switch to the Places Category and select the desired entry from the list of places. Double-click that entry or click the button on the toolbar to bring up the following dialog:

The following fields are available:

- Title area at top displays the description of this place to be used in reports. Gramps will construct this for you. See section \> generation option.

- 

  - button opens the dialog where you can add/edit additional information.

- . All **[Custom Types](wiki:Gramps_Glossary#custom)** are shown at the bottom of the list. Choose from the following default available place **Types**:

  - *Building*
  - *Borough*
  - *Country*
  - *County*
  - *City*
  - *Department*
  - *District*
  - *Farm*
  - *Hamlet*
  - *Locality*
  - *Municipality*
  - *Neighborhood*
  - *Number* - See the option for the
  - *Parish*
  - *Province*
  - *Region*
  - *State*
  - *Street*
  - *Town*
  - **Unknown** (*default*)
  - *Village*

<hr>

#### Coordinates Parser

- the position above equation of the place in decimal or degree notation. Eg, valid values are 12.0154, 50°52'21.92\\N, N50º52'21.92\\ or 50:52:21.92. You can set these values via the Geography View by searching the place, or via a map service in the Place view. See: [Supported longitude/latitude formats](#Supported_longitude.2Flatitude_formats) See: [Coordinates format:](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Display_Options) in preferences Display as this option controls the display of Coordinates.

<!-- -->

- the position relative to the Prime, or Greenwich, Meridian of the place in decimal or degree notation. Eg, valid values are -124.3647, 124°52'21.92\\E, E124º52'21.92\\ or 124:52:21.92. You can set these values via the Geography View by searching the place, or via a map service in the Place view. See: [Supported longitude/latitude formats](#Supported_longitude.2Flatitude_formats) See: [Coordinates format:](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Display_Options) in preferences Display as this option controls the display of Coordinates.

-  See: [Coordinates format:](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Display_Options) in preferences Display as this option controls the display of Coordinates.

<hr>

- \- public is the default

- an unique record to identify the place. Leave generated by Gramps.

- a code for this place. For example, an area code or postal code.

- - 

{{-}}

### Place editor tab pages

The tabs represent the following categories of place data:

- 

- 

- 

- 

- 

- 

- 

#### Enclosed By

![[_media/PlaceEditor-EnclosedBy-tab-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Enclosed By" tab from "Place Editor" - dialog - example]]

Places in Gramps are stored in a hierarchy. The tab allows you to link this place to other places, higher in the hierarchy, which enclose it. Each link consists of a place and an optional date range.

To enclose with an existing place, use the use the button to choose a Place from the [Place Selector](#Select_Place_selector). Alternately, drag a place (from the Clipboard, Places Category view, or an Event Editor) into bottom of the tab.

The buttons , , and let you add a new Place as an enclosing hierarchical level, modify the selected enclosing Place, and remove a selected link to an enclosing Place.

Note that the , and re-ordering (up, down) buttons become available only when a link exists and is selected from the list. In general, a country will be a top level place, and will not be linked to any other place.

**See also:**

- [Enclosed By](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Enclosed_By) Gramplet
- [Using the clipboard](wiki:Gramps_6.0_Wiki_Manual_-_Navigation#Using_the_Clipboard)

##### Select Place selector

![[_media/SelectPlace-SelectorDialog-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Select Place - Selector Dialog - example]]

The selector dialog allows you to link to an already existing place and once selected it will be opened in the

You may use the button to filter the list based on one of the options from the drop down list:

- **Name contains** (default)
- **Name does not contain**
- **ID contains**
- **ID does not contain**
- **Type contains**
- **Type does not contain**
- **Title contains**
- **Title does not contain**
- **Last Change contains**
- **Last Change does not contain**

The button will reset the filter.

If no record was selected, clearing will reset the scrolling to the top of the list. However, if a row was selected from the 'Find' results, clearing the filter will re-center on the selected item instead scrolling to top.

{{-}} See also:

- [Selector dialogs](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Selector_dialogs)

##### Place Reference Editor

![[_media/PlaceReferenceEditor-dialog-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Place Reference Editor - Dialog - example]]

The second part of the window displays seven notebook tabs containing different categories of information. Click a tab to view or edit its contents. The bottom part of the window has and buttons. Clicking will apply all the changes made in all tabs and close the dialog window. Clicking the button will close the window without applying any changes.

{{-}}

#### Alternative Names

  
The tab lets you view and edit other names by which the place might be known. The tab lists all other names of the place stored in the database. The buttons , , and let you add, modify, and remove a name record. Note that the and buttons become available only when a name is selected from the list.

#### Source Citations

  
The tab lets you view and edit sources relevant to a place. The central part of the window lists all such source references stored in the database. The buttons , , and let you add, modify, and remove a source reference associated with a place. Note that the and buttons become available only when a source reference is selected from the list.

#### Notes

  
The tab displays any comments or notes concerning the place. To add a note or modify existing notes simply edit the text in the text entry field.

#### Gallery

  
The tab lets you store and display photos and other media objects associated with a given place. The central part of the window lists all such media objects and gives you a thumbnail preview of image files. Other objects such as audio files, movie files, etc., are represented by a generic Gramps icon. The buttons , , , and let you add a new image, add a reference to an existing image, modify an existing image, and remove a media object's link to the place. Note that the and buttons become available only when a media object is selected from the list.

#### Internet

  
The tab contains Internet addresses relevant to the place. (This tab exhibits identical behavior to the [Internet Tab](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1#Internet) for the Person editor and its [Internet Address Editor](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1#Internet_Address_Editor) is the same also.)

<!-- -->

  
The bottom part of the window lists all such Internet addresses stored in the database. The top part shows the details of the currently selected address in the list (if any). The buttons , , and let you add, modify, and remove an Internet address. The button (represented by an icon with a green arrow and yellow circle) opens your browser and takes you to the web page corresponding to the highlighted Internet address. Note that the , , and buttons become available only when an address is selected from the list.

#### References

  
The tab indicates any database records (events or LDS ordinances) that refer to a place. This information cannot be modified from the dialog. Instead, the corresponding event record (e.g., a birth event) has to be brought up and its place reference edited.

{{-}}

### Place Name Editor dialog

![[_media/PlaceNameEditor-dialog-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Place Name Editor" dialog - default]]

The dialog is accessed from the dialogs button.

The dialog allows you to add/edit the following information:

- the name of the place

- Date range in which the place is valid

  - ![[_media/22x22-gramps-date.png]] button

- Language in which the name is written. Valid values are two character ISO codes for example: en,fr, de, nl. See Wikipedia for the full list of valid [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) codes.

{{-}}

### Supported longitude/latitude formats

When you create/modify a place, the possible formats used for longitude/latitude coordinates are :

<table>
<thead>
<tr>
<th colspan="2"><p>Longitude &amp; Latitude Formats</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p>D.D4</p></td>
<td><p>degree notation, 4 decimals</p>
<dl>
<dt></dt>
<dd>
eg +12.0154 , -124.3647
</dd>
<dd>
4 <a href="https://wikipedia.org/wiki/Decimal_degrees#Precision">decimals of longitude precision</a> allows an 11.132 meter (36.5223097 foot) approximation at the equator.
</dd>
</dl></td>
</tr>
<tr>
<td><p>D.D8</p></td>
<td><p>degree notation, 8 decimals (<a href="https://wikipedia.org/wiki/Decimal_degrees#Precision">precision</a> like ISO-DMS)</p>
<dl>
<dt></dt>
<dd>
eg +12.01543265 , -124.36473268
</dd>
</dl></td>
</tr>
<tr>
<td><p>DEG</p></td>
<td><p>degree, minutes, seconds notation</p>
<dl>
<dt></dt>
<dd>
eg 50°52'21.92"N , 124°52'21.92"E (° symbol has UTF-8 code c2b00a)
</dd>
<dd>
or N50º52'21.92" , E124º52'21.92" (º symbol has UTF-8 code c2ba0a)
</dd>
<dd>
The character for seconds can be either one double quote "
</dd>
<dd>
or two single quote '
</dd>
<dd>
The letters N/S/W/E can be placed before or after the digits.
</dd>
</dl></td>
</tr>
<tr>
<td><p>DEG-</p></td>
<td><p>degree, minutes, seconds notation with :</p>
<dl>
<dt></dt>
<dd>
eg -50:52:21.92 , 124:52:21.92
</dd>
</dl></td>
</tr>
<tr>
<td><p>ISO-D</p></td>
<td><p>ISO 6709 degree notation</p>
<dl>
<dt></dt>
<dd>
i.e. ±DD.DDDD±DDD.DDDD
</dd>
</dl></td>
</tr>
<tr>
<td><p>ISO-DM</p></td>
<td><p>ISO 6709 degree, minutes notation</p>
<dl>
<dt></dt>
<dd>
i.e. ±DDMM.MMM±DDDMM.MMM
</dd>
</dl></td>
</tr>
<tr>
<td><p>ISO-DMS</p></td>
<td><p>ISO 6709 degree, minutes, seconds notation</p>
<dl>
<dt></dt>
<dd>
i.e. ±DDMMSS.SS±DDDMMSS.SS
</dd>
</dl></td>
</tr>
</tbody>
</table>

{{-}}

See: [Coordinates format:](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Display_Options) in preferences Display as this option controls the display of Coordinates.

## Editing information about sources

From either of the category views you can select or create a new source, or if you had chosen the or buttons, then the editor dialog appears.

### New Source dialog

![[_media/NewSource-editor-dialog-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} New Source - editor dialog - example]]

For the editor dialog the general information in the top section of the window lets you define basic information about the source: its , , , and . You can type this information directly into the adjacent fields.

- Title of the source.

- Authors of the source.

- Publication Information, such as city and year of publication, name of publisher, ...

- Provide a short title used for sorting, filing, and retrieving source records.

  - Lock icon toggle.

- an unique record to identify the source. Leave generated by Gramps.

- - 

{{-}}

### New Source tab pages

The tabs provide the following information categories of source data:

#### Notes

  
The tab provides a place to record notes or comments about the source. To add a note or modify existing notes simply edit the text in the text entry field. Only primary objects can be shown in the tab: Person, Family, Event, Place, or Media object. Secondary objects such as Names and Attributes can only be accessed through the primary objects to which they belong.

#### Gallery

  
The tab lets you store and display photos and other media objects associated with a given source (for example, a photo of a birth certificate). The central part of the window lists all such objects and gives you a thumbnail preview of image files. Other objects such as audio files, movie files, etc., are represented by a generic Gramps icon. The buttons , , , and let you add a new image, add a reference to an existing image, modify an existing image, and remove a media object's link to the relationship. Note that the and buttons become available only when a media object is selected from the list.

#### Attributes

  
The tab displays "Key/Value" pairs that may be associated with the source. These are similar to the "Attributes" used for other types of Gramps records. The difference between these Key/Value pairs and Attributes is that Attributes may have source references and notes, while Key/Value data may not.

<!-- -->

  
The central part of the window lists all existing Key/Value pairs. The buttons and let you add and remove pairs. To modify the text of Key or Value, first select the desired entry. Then click in either the Key or Value cell of that entry and type your text. When you are done, click outside the cell to exit editing mode.

#### Repositories

![[_media/NewSource-Repositories-tab-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Repositories" tab from "New Source" - dialog - example]]

  
The tab displays the references to the repositories in which the source is contained. The list can be ordered by any of its column headings: , , ,and . Double-clicking an entry allows you to view and edit the record in the . You may also edit the reference. The buttons on the side of the tab allow you add a new repository, link to (or share) an existing repository, edit the reference to the repository, or remove the reference.

##### Repository Reference Editor

![[_media/Repository-Reference-Editor-example-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Repository Reference Editor - Dialog - example]] The **Repository Reference Editor** dialog is opened by double-clicking a record in the tab of the [Source Editor](#Editing_information_about_sources) dialog.

It provides the ability to log the Type and Call Numbers for a Source in a particular Repository. Since a source might exist in multiple repositories. (I might have a photocopy in my personal library. A copy of the original book might be in the holdings of the <abbr title="Allen County Public Library">ACPL</abbr> Genealogy Center in Ft. Wayne, Indiana. The microfilm might being in the FamilySearch Library in Salt Lake City, Utah. Each can be located using different Call Numbers.)

###### Reference information

The Reference Information section has and tabs. The General tab has a text entry field for the and a [drop-down list combo box](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window#Combo_Boxes).

Media Type choices: Audio, **Book** *(default)*, Card, Electronic, Fiche, Film, Magazine, Manuscript, Map, Newspaper, Photo, Tombstone, Unknown, Video, [custom types](wiki:Gramps_Glossary#custom).

###### Shared information

The section offers all the options of the [Repository Editor](#New_Repository_dialog) dialogs with General, Addresses, Internet, Notes and References tabs. {{-}}

##### Select Repository selector

![[_media/SelectRepository-SelectorDialog-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Select Repository - Selector Dialog - example]]

The selector dialog allows you to link to an already existing repositories and once selected it will be opened in the <span id="Repository_Reference_Editor"></span>

You may use the button to filter the list based on one of the options from the drop down list:

- **Title contains** (default)
- *Title not contain*
- *ID contains*
- *ID does not contain*
- *Last Change contains*
- *Last Change does not contain*

{{-}}

#### References

  
The tab lists all the database records that refer to this source, if any. The list can be ordered by any of its column headings: , , or . Double-clicking an entry allows you to view and edit the record.

{{-}}

## Editing source citations

Citations connect a Source to another object and allow you to provide additional information about the source. Citations can be attached to a large number of objects,

- [People and various information about people](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1#Editing_information_about_people) (such as their name, address etc),
- [Relationships (Families) and various information about relationships](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1#Editing_information_about_relationships),
- [Events and various information about events](#Editing_information_about_events),
- [Media objects and attributes of media objects](#Editing_information_about_media_objects),
- [Places and various information about places](#Editing_information_about_places),
- [Addresses of repositories](#Editing_information_about_repositories).

For each object, a common set of buttons are provided:

-  (Create and add a new citation and a new source). This brings up an empty Citation dialog.

-  (Add an existing citation or source). This brings up the Source or Citation selection dialog box.

-  (Edit the selected citation). This brings up the Citation dialog pre-populated with the Citation and source information.

-  (Remove the existing citation). This removes the citation from the object. It does not delete the citation itself, which could then be connected to another object.

Note that the and buttons become available only when a citation has been selected.

{{-}}

### Select Source or Citation selector

![[_media/SelectSourceOrCitation-SelectorDialog-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Select Source or Citation - Selector Dialog - example]]

When adding an existing citation or source, the [selector](wiki:Gramps_Glossary#selector) dialog appears.

This allows either an existing source or an existing citation (along with its associated source) to be selected. Click on the disclosure triangle alongside a source to see the citations associated with that source. For example, if one of your sources were a book, then the citations would normally refer to a page (or pages) within the book. If you already have a citation that refer to the particular page of the book, then you could select that citation which would then be shared. On the other hand, if this object needs to refer to a new page, then you would select the source and in the subsequent dialog enter the new page.

You may use the button to filter the list based on one of the options from the drop down list:

- **Source: Title or Citation: Volume/Page contains**(default)
- *Source: Title or Citation: Volume/Page does not contain*
- *ID contains*
- *ID does not contain*
- *Last Change contains*
- *Last Change does not contain*

{{-}}

### New Citation dialog

![[_media/NewCitation-editor-dialog-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} New Citation - editor Dialog - example]]

Once you have selected a citation or a source, or if you had chosen the or buttons, then the dialog appears.

The dialog includes one section called . {{-}}

#### Citation information

The section indicates the details associated with the particular reference to this Source: , , , and . You can choose the Confidence level from the drop-down menu. The remaining details can be typed in the corresponding text entry fields.

- Date associated with this source reference. Typically used to store the date that the data was entered into the original source document (not the date when the event occurred).

  - ![[_media/22x22-gramps-date.png]] button starts the dialog.

-   
  Specific location with in the information referenced. For a published work, this could include the volume of a multi-volume work and the page number(s). For a periodical, it could include volume, issue, and page numbers. For a newspaper, it could include a column number and page number. For an unpublished source, this could be a sheet number, page number, frame number, etc. A census record might have a line number or dwelling and family numbers in addition to the page number.

-   
  Level conveys the submitter's qualitative evaluation of the credibility of a piece of information, based upon its supporting evidence. It is not intended to eliminate the receiver's need to evaluate the evidence for themselves. (Shown in the as the column)

  - *Very Low* = Unreliable evidence or estimated data.
  - *Low* = Questionable reliability of evidence (interviews, census, oral genealogies, or potential for bias for example, an autobiography).
  - **Normal** - (default) Evidence possibly has no issue or has not been assessed. Not yet validated
  - *High* = Secondary evidence, data officially recorded sometime after event.
  - *Very High* = Direct and primary evidence used, or by dominance of the evidence.

- 

- 

A warning icon  is displayed if the citation is shared.  

{{-}}

##### Select Source selector

![[_media/SelectSource-selector-dialog-example-50.PNG|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Select Source - Selector Dialog - example]]

The selector dialog allows you to link to an already existing source.

You may use the button to filter the list based on one of the options from the drop down list:

- **Title contains** (default)
- *Title not contain*
- *Author contains*
- *Author does not contain*
- *ID contains*
- *ID does not contain*
- *Last Change contains*
- *Last Change does not contain*

{{-}}

##### Citation information section tab pages

The tabs provide the following information categories of citation data:

###### Notes

The tab provides a place to record notes or comments about the citation. The central part of the window lists all notes for this citation, and gives you a preview of the beginning of the note. The buttons , , , , and let you add a new note, share the selected note, edit the selected note, remove the selected note and move the selected note up or down the list of notes. Note that the , , , and buttons become available only when a media object is selected from the list. Removing a note only removes the note from this citation, it does not delete the note itself. Please refer to [details on editing notes](#Editing_information_about_notes).

###### Gallery

The tab lets you store and display photos and other media objects associated with a given citation (for example, a photo of a page of a book or a page of a census). The central part of the window lists all such objects and gives you a thumbnail preview of image files. Other objects such as audio files, movie files, etc., are represented by a generic Gramps icon. The buttons , , and let you add a new image, add a reference to an existing image, modify an existing image, and remove a media object's link to the citation. Note that the and buttons become available only when a media object is selected from the list. Please refer to [details on editing media references](#Editing_media_object_references).

###### Attributes

The tab displays "Key/Value" pairs that may be associated with the citation. These are similar to the "Attributes" used for other types of Gramps records. The difference between these Key/Value pairs and Attributes is that Attributes may have source citations and notes, while Key/Value data may not.

The central part of the window lists all existing Key/Value pairs. The buttons and let you add and remove pairs. To modify the text of Key or Value, first select the desired entry. Then press the button to select the Key, or click in either the Key or Value cell of that entry and type your text. When you are done, click outside the cell to exit editing mode.

###### References

The tab lists all the database records that refer to this source, if any. The list can be ordered by any of its column headings: , , or . Double-clicking an entry allows you to view and edit the record.

{{-}}

## Editing information about repositories

Once you have selected a source, or if you had chosen the or buttons, then the dialog appears.

### New Repository dialog

![[_media/NewRepository-editor-dialog-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} New Repository - editor dialog - example]]

The following fields are shown:

- of the repository (where sources are stored).

- of repository can be physical or virtual structures where genealogical and family history sources are stored:

  - *Album*
  - *Archive*
  - *Bookstore*
  - *Cemetery*
  - *Church*
  - *Collection*
  - **Library** (default)
  - *Safe*
  - *Unknown*
  - *Web site*

-   
  an unique record to identify the repository. Leave empty to be generated by Gramps.

- Lock icon toggle.

- - 

{{-}}

### New Repository tab pages

The tabs represent the following categories of repository data:

- 

- 

- 

- 

#### Addresses

The tab lets you view and record the various addresses of the repository.

The bottom part of the window lists all addresses stored in the database. The top part shows the details of the currently selected address in the list (if any). The buttons , , and allow you to correspondingly add, modify, and remove an address record from the database. Note that the and buttons become available only when an address is selected from the list.

#### Internet

The tab displays Internet addresses relevant to the repository. (This tab exhibits identical behavior to the [Internet Tab](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1#Internet) for the Person editor and its [Internet Address Editor](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1#Internet_Address_Editor) is the same also.)

The bottom part lists all such Internet addresses and accompanying descriptions. The top part shows the details of the currently selected addresses in the list (if any). The buttons , , and let you add, modify, and remove an Internet address. The "Go" button (represented by an icon having a green arrow and yellow circle) opens your web browser and takes you directly to the highlighted page. Note that the , and buttons become available only when an address is selected from the list.

#### Notes

  
The tab provides a place to record notes or comments about the repository. To add a note or modify existing notes simply edit the text in the text entry field.

#### References

  
The tab indicates any database records that refer to a given repository. The list can be ordered according to any of its column headings: , , or . Double-clicking an entry allows you to view and edit the corresponding record.

{{-}}

## Editing information about notes

See also:

- [Notes Category](wiki:Gramps_6.0_Wiki_Manual_-_Categories#Notes_Category)

### Note editor dialog

![[_media/NewNote-editor-dialog-example-with-context-menu-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} New Note - editor dialog - example with context menu]] When creating a new note, or when editing an existing note, the dialog appears. There are two tabs, the **** tab, and the **** tab.

#### Note tab

The tab is the space where text is added. The text can be formatted using many standard text editing tools.

##### Note Toolbar

:\* A toolbar to apply styles (or Font Decorations) to text in your notes. You can select and apply one of the toolbuttons, or set the values as you want and start typing.

::\* : Slants text for emphasis, common in most text editors

::\* : Darkens text for emphasis, common in most text editors

::\* : Draws a line under text, common in most text editors

::\* : draws a line through, commonly used to indicate text to be deleted

::\* : Raises text slightly, commonly used for footnotes (e.g., Wikipedia<sup>2</sup>)

::\* : Lowers text slightly, commonly used in formulas (e.g., H<sub>2</sub>O)

::\* : selection drop down list, a basic font selector showing all fonts installed on your operating system.

::\* : selection drop down list, select the size of the font to use for your text.

::\* : Undoes last action.

::\* : Re-applies last "Undone" action.

::\* : Select the color of your font.

::\* : Adds a background color to the text you enter.

::\* : Opens the allowing you to create an internal link to an item in Gramps, such as a Person, Family, Event, Note, etc. External URL links can also be created.

::\* : Return selected text to plain text. Removes any links made.

##### Textview context menu

:\* Right click on the textview to show the context menu:

<hr>

::\*  - selected or alternatively you can press and right-click the mouse button - *Only shown when a link is selected in the textview*

::\*  - and you can paste the content elsewhere - *Only shown when a link is selected in the textview*

::\*  - Opens the allowing you to create an modify the selected link. - *Only shown when a link is selected in the textview*

::\*  - The most important entry in this context menu is the spell selection. You are offered a selection of installed languages on your system with spell checking enabled. A [spelling checker](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Environment_Settings) is available for *English* and your installed local language (Note in the section enable the option for global English by default or the language your Gramps is run in and the note context menu is per note in the selected Language of your choice)

:::\*

:::\*  - (default)

::\*  - the selected text.

::\*  - the selected text.

::\*  - the previously cut or copied text.

::\*  - the selected text.

<hr>

::\*  - the text in the textview.

::\* -

::\* -

<hr>

##### Note properties

:\* Some properties of your note

::\* checkbox: Notes in Gramps are considered reflowable to allow the content to conform to the report's page size and formatting for the most harmonious presentation. In the default setting, newlines (linefeeds & carriage returns) and white spaces will be automatically ignored so as to form complete paragraphs, which are defined by an empty line between two textblocks.  
When is checked, Gramps will assume the whitespace and newlines you keyed into the notes are important. Use *Preformatted* for tables, literal transcripts, and so forth. Using a monospace font will help keep preformatting column widths & margins predictable.  
Try not to use preformatted unless absolutely necessary, the reports created will flow more naturally.

::\* Privacy is the same as on the other objects. With one easy click, you can indicate a note should be considered private so Gramps can remove this note from all output created.

::\* a unique ID for the note. If left blank, an automatic ID will be generated according to the settings in the preferences.

<div id="note_type">

::\* (`General` default) The note type. You can add your own [custom Type](wiki:Gramps_Glossary#custom) by keyboarding it in directly. Adding a Note will automatically set the Type to match the object to which it is being added. (e.g. A note added to the Notes tab of the Person Editor will default to *Person Note* Type.)

  
  
{\|class="wikitable"

! style="text-align:left;"\| Type ! Recognized for features in \|- \|*[<primary object>](wiki:Gramps_Glossary#primary_object)* Note \| \|- \|*[<secondary object>](wiki:Gramps_Glossary#secondary_object)* Note \| \|- \|Citation \| \|- \|General \|*(default)* \|- \|Html code \|[Narrated Web Site](wiki:Gramps_6.0_Wiki_Manual_-_Reports#Narrated_Web_Site) report inclusions; export to GEDCOM \|- \|Link \| \|- \|Report \| \|- \|Research \| \|- \|Source text \| \|- \|To Do \|[To Do](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#To_Do) Gramplet, [ToDo Notes Gramplet](wiki:Addon:ToDoNotesGramplet) Addon. *Not to be confused with ToDo tag-based reports.* \|- \|Transcript \| \|- \|Unknown \| \|}

</div>

::\* Select a Tag for the note: Complete, Todo etc... You can add your own Tags by typing it. Reports based on tags include: [Tag Report](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_6#Tag_Report), [Todo report](wiki:Addon:ToDoReport)

:::\* The button brings up the dialog list that lets you remove or assign existing custom tags. {{-}}

#### References tab

The tab indicates any objects that refer to a given note. The list can be ordered according to any of its column headings: `Type`, `ID`, or `Name`. Double-clicking on an entry or selecting an entry and using the button allows you to view and edit the corresponding record.

### Link Editor

![[_media/Note-LinkEditor-dialog-default-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Note "Link Editor" - dialog - defaults to active person - example]]

To create a note link, **a block of Note text must first be highlighted for the Link Editor to be active** and when the [Note Toolbar's](#Note_Toolbar) button icon is selected you will be shown the . There is no visual indicator when the Note Toolbar's button icon is inactive.

The Links created in the note will turn blue and show an underline when you hover your mouse over the Linked text. While working within the Gramps Note, you can either press  + the left-click mouse button or from the right-click [Textview context menu](#Textview_context_menu) select allowing either the edit window for the selected object to open or to open the HTML URL link in your default internet browser.

The true power of Links are shown when a [Narrated Web Site](wiki:Gramps_6.0_Wiki_Manual_-_Reports#Narrated_Web_Site) or [Dynamic Web](wiki:Addon:DynamicWeb_report) site report is created. The created Links become true navigation links to other pages within the web report.

#### Note Link Editor dialog

![[_media/Note-LinkEditor-dialog-InternetAddress-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Note "Link Editor" - dialog - showing the Link Type: Internet Address - example]]

The Note dialog shows the Active *Person* by default and when selected for each of the other objects the relevant active object. Or you can select the link type of *Internet Address*.

The following options are shown:

- specify the type of link for either one of the active nine Gramps item/objects by default the active *Person* or an *Internet Address* you manually enter.

  - *Internet Address* - ([<abbr title="Uniform Resource Locator, also known as a web address">URL</abbr>](https://en.m.wikipedia.org/wiki/URL)) - if selected the field becomes available for data entry.
  - *[Event](wiki:Events)*
  - *Family*
  - *Media*
  - *Note*
  - **Person** (default)
  - *[Place](wiki:Places)*
  - *Repository*
  - *[Source](wiki:Sources)*
  - *[Citation](wiki:Citations)*
    -  button : opens the relevant [selector dialog](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Selector_dialogs) for existing items in the category specified in the Link Type. **Not applicable for Internet Address selection.**

    - button : opens a window to create a new item of the specified Gramps item. Successful creation of a new item will autofill the Gramps item box and the Internet Address box with the appropriate data.

- shows the selected item eg: If Person is selected and then the active persons name is shown see the screenshot. **Not applicable for Internet Address selection.**

  - This box is Auto generated by the selection of the button/ button/ button.

- button : opens the editor dialog for the specified Gramps item. The selected item will autofill the Gramps item box and the Internet Address box with the appropriate data.

- - for the = Gramps type will autofill this box but the contents will be greyed out
  - for the = *Internet Address* (defaults to: [`https://`](https://) ) you delete the default provide by Gramps and enter the full Internet Address either manually or via copy and paste.

![[_media/Note-showing-tooltip-for-link-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Notes Editor - Linked text with tooltip - example]]

See also:

- [Internet Address Editor](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1#Internet_Address_Editor)
- [Note Link Report](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_6#Note_Link_Report)

{{-}}

### Note markup and preformat in reports

Markup like **bold**, color, <u>underline</u>, ... can be added to notes. A note can be preformatted or not. It depends on the output type how this markup will appear. Here an overview is given of what you can expect.

- **PDF** and **direct print** (to printer or to file) fully support the markup and the preformatted setting
- **ascii** print removes all markup from the notes for obvious reasons

<!-- -->

- **LaTeX** supports the preformatted setting and partially supports font emphasis stylings and size markup;  
  output does not support font family or colors markup.
- **Narrative Web**. Many people use the Narrative Web report as an easy way to work with their data. This report is trying to respect markup in the notes. This is an interpreted translation, it is not one-to-one.
- **ODF** output does not support markup.
- **RTF** output does not support markup.
- **html** output does not support markup.

{{-}}

[Category:Documentation](wiki:Category:Documentation)
