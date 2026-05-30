---
title: 'Gramps 6.0 Wiki Manual - Entering and editing data: detailed - part 3'
categories:
- Documentation
- Stub
managed: false
source: wiki-scrape
wiki_revid: 125026
wiki_fetched_at: '2026-05-30T11:13:10Z'
---

{{#vardefine:chapter\|9.3}} {{#vardefine:figure\|0}} **<span style="font-size:120%">Entering and editing data: detailed Names, Attributes, Addresses, Merging</span>**  
The previous section offered you a detailed overview of how to enter and edit the main objects you see in Gramps. This section continues with other objects you encounter in Gramps.

## Name Editor

Names are edited through the dialog, available from the of the dialog. Besides editing the name, the Name Editor allows: the definition of multiple surnames, aliases, selection of preferred name (by era) and the override of display format, groups and sorting.

Names throughout Gramps are displayed in the format selected in the *Display Options* section of the [tab](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Display_Options) of the dialog. Other predefined display formats can be selected from the pop-up menu. New name formats may be created with the by clicking the button. {{-}}

### Name Editor dialog

![[_media/NameEditor-dialog-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;Name Editor&quot; - dialog - example]] The top of the dialog window allows entry of the type of name (e.g., Birth Name, Married Name, etc) from a dropdown list. Next are elements of the personal name most commonly grouped as Given Name elements. Following the Given Name section is the Family Names section. At the bottom are elements allowing for customization of name sorting, dates for names, name sources, and notes for names. {{-}}

#### Type

- (`Birth Name`default) The Name type dropdown list allows you to select the type of name being entered. You may also directly key in a [Custom Type](wiki:Gramps_Glossary#custom) into this field.

- toggle the icon in the top right corner to mark this name record as private. This will give you a chance to omit this name from being included in reports if you choose so among the report generation options.

{{-}}

#### Given Name(s) Section

The **Given Name(s)** Section contains all parts of a personal name you can store with Gramps:

- The person's given names should all be entered here.

- The person's proper legal name that was used most commonly by the person should be entered here. For example, someone named John Raymond Smith who uses the name Raymond should have *Raymond* entered here. If this person uses *Ray* commonly, this should be entered as a nickname since Ray is not the proper legal name (see following). In Germany and some other places, it was customary to underline the call name among the different given names (see also [here](wiki:Names_in_Gramps#Call_Name)).

- The person's title, such as Doctor (or Dr.) can be entered here.

- The person's name suffix, such as Junior (Jr.) or III, should be entered here.

- The person's nickname should be entered here. Nicknames include shortenings of proper legal names such as Greg for Gregory (cf. Call Name above).

{{-}}

#### Family Names Section

The **Family Names** Section contains the person's family name elements. Gramps allows for multiple family names as well as multiple kinds of family names.

- Toolbar - / / / /

The following columns are shown:

- A prefix for the family name that is not used in sorting (such as "de" or "van").

- for the main portion of one's family name.

- often used in matronymic or patronymic naming schemes, such as *dotter*.

- indicating the type of family name this is and its derivation.

- Radiobox indicating if the family name is the primary one.

The following field is shown:

- for families commonly referred to using a more vernacular nickname.

See also: [Names in Gramps](wiki:Names_in_Gramps) - wiki article. {{-}}

### Name Editor tab pages

The following tabs are available:

- 

- 

- 

#### General

Options allowing you to adjust specific grouping, sorting, and displaying properties of this name, as well as to provide the date corresponding to the name:

- The field provides an alternative grouping node for a name in the person view, overriding the default grouping based on the family name. This may be necessary with similar family names that need to be grouped -- for example Russian names Ivanov and Ivanova are considered the same, but the difference in gender is reflected in different spelling. See [Grouping Surnames](wiki:Grouping_Surnames).
  -  Check this checkbox to enable typing into this field. (checkbox unchecked by default)

  
People are displayed according to the name format given in the Preferences (the default).

Here you can make sure this person is displayed according to a custom name format. *(More name formats can be selected in the tab or customized using the [Display_Name_Editor](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Display_Name_Editor).)*

- The and determine how the name appears in the People View and the reports. The sort allows you to override the name pattern set in the Gramps preferences in the sorting of the name. For example, you suddenly have a branch of Swedish names with given and patronymic, but the rest of your database sorts names on Family name, Given. You can indicate here to sort this name always as Patronymic, Given.

  
Here you can make sure this person is sorted according to a custom name format. *(More name formats can be selected in the tab or customized using the [Display_Name_Editor](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Display_Name_Editor).)*.

The allows you to say how the name is listed. You might, for example, want to sort a name in based on a person's given or surname, but still have the display show an honorific title before that name. *(More name formats can be selected in the tab or customized using the [Display_Name_Editor](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Display_Name_Editor).)*

The Person Tree view groups people under the primary surname. You can override this by setting here a group value. You will be asked if you want to group this person only or all people with this specific primary surname.

- The can provide information on the validity of this name -- use date spans as necessary. The edit date icon opens the [Date Editor](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_Editing_Data:_Detailed_-_part_1#Editing_dates). Eg. for a Married Name, enter the date that the name is first used or the marriage date.

#### Source Citations

The tab displays information about sources and citations relevant to this name and controls allowing its modification. The central part displays the list of all such citations and sources stored in the database. The buttons , , and allow you to correspondingly add, modify, and remove a citation to this name. Note that the and buttons become available only when a source reference is selected from the list.

More info: [Citations editor](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_2#Editing_source_citations)

#### Notes

The tab displays any notes concerning the name. To add a note or modify existing notes simply edit the text in the text entry field.

More info: [Note Editor](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_2#Editing_information_about_notes)

## Attributes

When you add or edit an [Attributes](wiki:Attributes_in_Gramps) from the dialogs tab the dialog will be shown. {{-}}

### Attribute Editor dialog

![[_media/AttributeEditor-dialog-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;Attribute Editor&quot; - dialog - default]] The top of the dialog window shows the dialog title including the name of the person whose attribute is being edited. The central part of the window displays three notebook tabs containing different categories of available information. You can bring any tab to the top for viewing or editing by clicking on the appropriate tab heading. The bottom part has and buttons. Clicking the button at any time will apply all the changes made in all tabs and close the dialog window. Clicking the button at any time will close the window without applying any changes.

The top section allows editing of the most general information about the attribute:

- (`Identification Number`default) The name of an attribute you want to use. For example: *Height* (for a person), *Weather on this Day* (for an event), ... Use this to store snippets of information you collect and want to correctly link to sources. Attributes can be used for people, families, events, and media. The information can be typed in the appropriate text entry fields. The attribute name can also be selected from available choices (if any) listed in the drop-down menu.

  - Toggle this to mark this attribute record as private or public. This will give you a chance to omit this attribute from being included in the reports if you choose so among the report generation options.

- Plain text description entry of the attribute. Eg. *1.8m, Sunny, or Blue eyes*.

{{-}}

#### Attribute Editor context menu

{{-}}

### Attribute Editor tab pages

The following tabs are available:

- [Notes](#Notes_2)
- [Source Citations](#Source_Citations_2)

#### Source Citations

  
The tab displays information about citations and sources relevant to this attribute and controls allowing its modification. The central part displays the list of all such sources and citations references stored in the database. The buttons , , and allow you to correspondingly add, modify, and remove a source reference to this attribute. Note that the and buttons become available only when a citation/source reference is selected from the list.

#### Notes

  
The tab displays any notes concerning the attribute. To add a note or modify existing notes simply edit the text in the text entry field.

{{-}}

## Addresses

When you add or edit an address from the dialogs tab the dialog will be shown. {{-}}

### Address Editor dialog

![[_media/AddressEditor-dialog-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;Address Editor: - dialog - default]] The dialog allows you to record a current address by recording the information in the appropriate text entry fields.

The top section of the dialog allows editing and entry of information about the address:

- Date at which the address is valid.

  - ![[_media/22x22-gramps-date.png]] button starts the dialog.

- The street of the address.

- button. Toggle this button to mark this address record as private or public. This will give you a chance to omit this address from being included in reports if you choose so among the report generation options.

- The locality name of the address.

- The state or county of the address in case a mail address must contain this.

- The village or city of the address.

- Country of the address.

- Postal code.

- Phone number linked to the address.

The bottom of the dialog has , and buttons. Clicking the button at any time will apply all the changes made in all tabs and close the dialog window. Clicking the button at any time will close the window without applying any changes. {{-}}

### Address Editor tab pages

The following tabs contain different categories of available information. You can bring any tab to the top for viewing or editing by clicking on the appropriate tab heading.

#### Source Citations

  
The tab displays information about sources relevant to this address and controls allowing its modification. The central part displays the list of all such sources and citations references stored in the database. The buttons , , and allow you to correspondingly add, modify, and remove a citation/source reference to this address. Note that the and buttons become available only when a source reference is selected from the list.

#### Notes

  
The tab displays any notes concerning the address. To add a note or modify existing notes simply edit the text in the text entry field.

{{-}}

## Merging records

![[_media/PeopleCategory-Toolbar-MergeTheSelectedPersons-icon-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;Merge the Selected Persons&quot; - Toolbar &quot;Merge...&quot; icon - example]] Sometimes several records in your family tree turn out to be describing the same object: same person, same place, or same citation/source. It could happen either when the data is entered twice by mistake, or when new information reveals that the two entries refer to the same person. It can also happen after importing a GEDCOM obtained from a relative, whose database overlaps with your existing data.

Whenever you detect duplicate records, merging them is a useful way of correcting the situation.

General usage  
Merging of two records is accomplished by selecting one entry and then selecting another entry while holding down the key and selecting either the or toolbar icon or context menu option.

The following merge options are available:

- [Merge People](#Merge_People)
- [Merge Families](#Merge_Families)
- [Merge Events](#Merge_Events)
- [Merge Places](#Merge_Places)
- [Merge Sources](#Merge_Sources)
- [Merge Citations](#Merge_Citations)
- [Merge Repositories](#Merge_Repositories)
- [Merge Media Objects](#Merge_Media_Objects)
- [Merge Notes](#Merge_Notes)

{{-}}

### Merge People

![[_media/MergePeople-dialog-default-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Merge People" dialog - with "Context Information" section expanded by default - example]]

When exactly two people are selected, choose to invoke the dialog.

The dialog allows you to decide on whether or not the selected records should be merged. If you decide that the records should not be merged, despite similar names, you may click button to close the dialog without making any changes.

You can expand the fields on the bottom left to show more information on which you can further decide which selection should be the primary piece of information to keep in the merge.

The field on the bottom left shows more information about the people to be merged.

If you decide to proceed with merging, select the appropriate persons ![[_media/RadioButton_Selected.png]] radio button to specify the record

- Name
- Gender
- Gramps ID

to be used as the source of primary data, then click . The data from the other record will be kept as alternate data.

Specifically, all names from the other record will become alternate names of the merged record. Similarly, parents, spouses, and children of the other record will become alternate parents, spouses, and children of the merged record, and so on.

See also:

- [Find Possible Duplicate People](wiki:Gramps_6.0_Wiki_Manual_-_Tools#Find_Possible_Duplicate_People)
- [Merging people](wiki:Merging_people)

{{-}} ![[_media/MergePeople-dialog-sections-expanded-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;Merge People&quot; dialog - with &quot;Detailed Selection&quot; &amp; &quot;Context Information&quot; sections expanded - example]] {{-}}

### Merge Families

![[_media/MergeFamilies-dialog-default-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Merge Families" - dialog - default example]]

When exactly two families are selected, choose to invoke dialog.

The dialog allows you to decide on whether or not the selected records should be merged. If you decide that the records should not be merged, despite being similar, you may click to close the dialog without making any changes.

You can either choose one of the two families to be the source of the primary data for the new family, or by expanding the field you can individually choose which father is the source of the primary data, which mother is the source of the primary data, and which family (selected by Gramps ID) is the source of the other primary data.

If you decide to proceed with merging, choose the appropriate families ![[_media/RadioButton_Selected.png]] radio button(s) to specify the source(s) of the primary data

- Father
- Mother
- Relationship
- Gramps ID

to be used for the merged family record, and then click .

The children from both marriages are merged into the new family. The two fathers are merged and the events from the secondary father are attached to the primary father. The names from the secondary father become alternate names for the primary father. The same occurs with the two mothers. The events related to the secondary family (e.g. marriage and any divorce) are transferred to the primary family. The secondary family and the person record for the secondary father and mother are deleted from the database.

![[_media/MergeFamilies-dialog-DetailedSelection-section-expanded-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;Merge Families&quot; - dialog - with &quot;Detailed Selection&quot; section expanded - example]] {{-}}

### Merge Events

![[_media/MergeEvents-dialog-example-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;Merge Events&quot; - dialog - default example]] When exactly two events are selected, choose to invoke dialog.

The dialog allows you to decide on whether or not the selected records should be merged.

By expanding the field you can see additional information about the merge.

If you decide that the records should not be merged, despite similar titles, you may click to close the dialog without making any changes.

If you decide to proceed with merging, choose the appropriate ![[_media/RadioButton_Selected.png]] radio button to specify:

- Type
- Date
- Place
- Description
- Gramps ID

to be used for the merged record, then click {{-}} ![[_media/MergeEvents-dialog-DetailedSelection-section-expanded-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;Merge Events&quot; dialog - with &quot;Detailed Selection&quot; section expanded - example]] {{-}}

### Merge Places

![[_media/MergePlaces-dialog-example-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;Merge Places&quot; - dialog - default example]] When exactly two places are selected, choose to invoke dialog.

The dialog allows you to decide on whether or not the selected records should be merged.

By expanding the field you can see additional information about the merge.

If you decide that the records should not be merged, despite similar titles, you may click to close the dialog without making any changes.

If you decide to proceed with merging, choose the appropriate ![[_media/RadioButton_Selected.png]] radio button to specify:

- Name
- Type
- Code
- Latitude
- Longitude
- Gramps ID

to be used for the merged record, then click . {{-}} ![[_media/MergePlaces-dialog-DetailedSelection-section-expanded-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;Merge Places&quot; dialog - with &quot;Detailed Selection&quot; section expanded - example]] {{-}}

#### Cannot merge places - cycle in place hierarchy - warning dialog

If you attempt to merge two(2) places that would result in a loop in the place hierarchy, you will be shown the warning dialog with the message *Merging these places would create a cycle in the place hierarchy.* For example attempting to merge a top level country with one of the associated cities would show: ![[_media/Cannot-merge-places-cycle-in-place-hierarchy-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}}  warning dialog with the message Merging these places would create a cycle in the place hierarchy. example]] {{-}}

### Merge Sources

![[_media/MergeSources-dialog-example-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;Merge Sources&quot; - dialog - default example]] When exactly two sources are selected, choose to invoke dialog.

By expanding the field you can see additional information about the merge.

The dialog allows you to decide on whether or not the selected records should be merged.

If you decide that the records should not be merged, despite similar titles, you may click to close the dialog without making any changes.

If you decide to proceed with merging, choose the appropriate ![[_media/RadioButton_Selected.png]] radio button to specify:

- Title
- Author
- Abbreviated - title
- Publication - information
- Gramps ID

to be used for the merged record, then click . {{-}} ![[_media/MergeSources-dialog-DetailedSelection-section-expanded-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;Merge Sources&quot; - with &quot;Detailed Selection&quot; section expanded - dialog - example]] {{-}}

### Merge Citations

![[_media/MergeCitations-dialog-example-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;Merge Citations&quot; - dialog - default example]] When exactly two citations are selected [with identical sources](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_3#Cannot_merge_citations._with_different_sources_warning_dialog), choose to invoke dialog.

By expanding the field you can see additional information about the merge.

The dialog allows you to decide on whether or not the selected records should be merged.

If you decide that the records should not be merged, despite similar titles, you may click to close the dialog without making any changes.

If you decide to proceed with merging, choose the appropriate ![[_media/RadioButton_Selected.png]] radio button to specify:

- Volume/Page
- Date
- Confidence
- Gramps ID

to be used for the merged record, then click . {{-}} ![[_media/MergeCitations-dialog-DetailedSelection-section-expanded-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;Merge Citations&quot; - with &quot;Detailed Selection&quot; section expanded - dialog - example]] {{-}} See also:

- [Merge Citations...](wiki:Gramps_6.0_Wiki_Manual_-_Tools#Merge_citations) Tool.

#### Cannot merge citations. with different sources warning dialog

![[_media/Cannot-merge-citations-with-different-sources-warning-dialog-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}}  -with-different-sources- warning dialog - example]]

Note the two selected citations must also either share the same sources or only one or none of the citations have a source attached, otherwise on selection to merge you will be shown the warning dialog with the advice *If you want to merge these two citations, then you must merge the sources first.*. {{-}}

### Merge Repositories

![[_media/MergeRepositories-dialog-example-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;Merge Repositories&quot; - dialog - default example]] When exactly two repositories are selected, choose to invoke dialog.

By expanding the field you can see additional information about the merge.

The dialog allows you to decide on whether or not the selected records should be merged.

If you decide that the records should not be merged, despite similar titles, you may click to close the dialog without making any changes.

If you decide to proceed with merging, choose the appropriate ![[_media/RadioButton_Selected.png]] radio button to specify:

- Name
- Type
- Gramps ID

to be used for the merged record, then click {{-}} ![[_media/MergeRepositories-dialog-DetailedSelection-section-expanded-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;Merge Repositories&quot; - with &quot;Detailed Selection&quot; section expanded - dialog - example]] {{-}}

### Merge Media Objects

![[_media/MergeMediaObjects-dialog-example-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;Merge Media Objects&quot; - dialog - default example]] When exactly two Media Objects are selected, choose to invoke dialog.

By expanding the field you can see additional information about the merge.

The dialog allows you to decide on whether or not the selected records should be merged.

If you decide that the records should not be merged, despite similar titles, you may click to close the dialog without making any changes.

If you decide to proceed with merging, choose the appropriate ![[_media/RadioButton_Selected.png]] radio button to specify:

- Title
- Path
- Date
- Gramps ID

to be used for the merged record, then click {{-}} ![[_media/MergeMediaObjects-dialog-DetailedSelection-section-expanded-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;Merge Media Objects&quot; - with &quot;Detailed Selection&quot; section expanded - dialog - example]] {{-}}

### Merge Notes

![[_media/MergeNotes-dialog-example-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;Merge Notes&quot; - dialog - default example]] When exactly two notes are selected, choose to invoke dialog.

By expanding the field you can see additional information about the merge.

The dialog allows you to decide on whether or not the selected records should be merged.

If you decide that the records should not be merged, despite similar titles, you may click to close the dialog without making any changes.

If you decide to proceed with merging, choose the appropriate ![[_media/RadioButton_Selected.png]] radio button to specify:

- Text
- Type
- Format
- Gramps ID

to be used for the merged record, then click {{-}} ![[_media/MergeNotes-dialog-DetailedSelection-section-expanded-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;Merge Notes&quot; dialog - with &quot;Detailed Selection&quot; section expanded - example]]

{{-}}

[Category:Documentation](wiki:Category:Documentation)
