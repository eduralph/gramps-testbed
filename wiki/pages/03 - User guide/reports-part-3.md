---
title: Gramps 6.0 Wiki Manual - Reports - part 3
categories:
- Documentation
- Plugins
- Stub
managed: false
source: wiki-scrape
wiki_revid: 128712
wiki_fetched_at: '2026-05-30T11:37:41Z'
---

{{#vardefine:chapter\|13.3}} {{#vardefine:figure\|0}} Back to [Index of Reports](wiki:Gramps_6.0_Wiki_Manual_-_Reports).

<hr>

{{-}} ![[_media/Menubar-ReportsOverview-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menu entry for]] This section describes the Book report available in Gramps.

## Books

The Books Report allows you to create a custom **genealogy book** containing a collection of Gramps textual and graphical reports in a single document (i.e. a Book)

The only report available under this report is the Books Report.

When you select from the menu, the main dialog appears. {{-}}

### Manage Books dialog

![[_media/ManageBooks-dialog-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Manage Books - dialog]]

The main dialog has three sections , and

To start the creation of your custom genealogy book click the button once all selections of the reports to be included have been made, and possibly configured (or reconfigured) or to just accept the defaults; this will present the dialog.

#### Book name

The (`New Book`default) text entry field shows the name of the current book. Change it and save your custom book (a set of configured selections) for future use, in which case you may first alter the field to contain whatever name you want. If you load a saved-away book (see below) it will show that book's name -- which may then be changed if you want to save a slightly-different configuration.

##### Book name toolbar

The top horizontal set of set of toolbar icons near the field operate on the whole book and allow the following functions:

- The icon button clears all previously selected items from the section.
- The icon button to save the current book (under the name previously typed in the text entry field) for future use, if the book name already exists you will be asked if you wanted to to save over it or you can and provide another name.

{{-}} ![[_media/OpenPreviouslyCreatedBook-AvailableBooks-dialog-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;Open previously created book&quot; icon and resulting &quot;Available Books&quot; - dialog]]

- Select the icon button to open the window which shows all your previously-saved books. In that box either double-click on a particular book name or first select it and then hit to then load the book.

{{-}} ![[_media/ManagePreviouslyCreatedBooks-AvailableBooks-dialog-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;Manage previously created books&quot; icon and resulting &quot;Available Books&quot; - dialog]]

- You can also select the icon button to open a slightly different window which shows your list of available books, and by using the button you can removed the selected book.

{{-}}

##### Available Books window

###### Available Books window (1)

![[_media/OpenPreviouslyCreatedBook-AvailableBooks-dialog-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Open previously created book" icon and resulting "Available Books" - dialog]]

window

"Open previously created book" icon and resulting "Available Books" - dialog {{-}}

###### Available Books window (2)

![[_media/ManagePreviouslyCreatedBooks-AvailableBooks-dialog-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Manage previously created books" icon and resulting "Available Books" - dialog]]

window with Delete button !

"Manage previously created books" icon and resulting "Available Books" - dialog {{-}}

#### Available items

![[_media/ManageBooks-dialog-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Available items (section list) from the &quot;Manage Books&quot; - dialog - with context menu]] The middle section lists the book items available for inclusion in the book.

The list shows the `Name` and `Type` of available reports that you can either double click-on a selection to add the report or right click on a selection and use the context menu.

##### Available items context menu

- \- selected entry to book.

#### Available items selections

Almost all 26 book items available for inclusion in the book are textual or graphical reports, and are therefore available in the form of standalone reports (see [Index of Reports](wiki:Gramps_6.0_Wiki_Manual_-_Reports) for their individual documentation). The exceptions are the following 4 items which are only available as book items, in a book report:

- [Alphabetical Index](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_3#Alphabetical_Index)
- [Custom Text](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_3#Custom_Text)
- [Table Of Contents](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_3#Table_Of_Contents)
- [Title Page](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_3#Title_Page)

The other 22 book items do not have the tab that is available only to the standalone reports. Note the book item version of the report may be named slightly differently to the standalone version.

- Ancestor Chart - same as the [Ancestor Tree](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_4#Ancestor_Tree) report.
- Calendar
- Descendant Chart - same as the [Descendant Tree](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_4#Descendant_Tree) report.

{{-}}

##### Alphabetical Index

![[_media/AlphabeticalIndex-book-item-BooksReport-options-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Alphabetical Index - item]]

The book item produces page(s) with an alphabetical index of people noted into selected textual reports.

On the tab you may choose the language from the drop down list.

{{-}}

##### Custom Text

![[_media/CustomText-book-item-BooksReport-options-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Custom Text - item]]

The book item produces a page with three paragraphs, each containing custom text.

The tab shows:

- 

- 

- 

The text input fields are expandable so you can really put all the text you want in there.

The lower window part shows some : here you can choose the . You can choose the default style or click on the button. This brings up a window where you can add and remove Styles. For more details see also [style editor](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Style_editor_dialog). This item is typically meant to be used for epigraphs, dedications, explanations, notes, and so forth.

{{-}}

##### Table Of Contents

![[_media/TableOfContents-book-item-BooksReport-options-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Table Of Contents - item]]

A (TOC) is generated for the book as a list of the parts of a book or document organized in the order in which the parts appear.

On the tab you may choose the language from the drop down list.

{{-}}

##### Title Page

![[_media/TitlePage-book-item-BooksReport-options-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Title Page - item]]

If you selected the book item and clicked the button to put this item in your book and you click button (Configure currently selected item) you will get a window.

On the tab you have three text input fields available where you can change the example text provided.

- (`Title of the Book` default)

- (`Subtitle of the Book` default)

- (`Copyright 2024 Alex Roitman...` default) (FYI Alex was an early Gramps project contributor)

<!-- -->

- allows an image to be placed optionally between the subtitle and the footer, by selecting the

  - button which will show the selector dialog where you can select the existing image you want.

- You can also change the default (`0.0`) size.

The lower window part shows some **Document Options**: here you can choose the **Style**. You can choose the default style or click on the button. This brings up a window where you can add and remove Styles. For more details see also [Style Editor](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Style_editor_dialog).

Because you can configure the various elements, this item can be used to create title pages for the whole book, its chapter, or even a single item.

{{-}}

#### Current book

The bottom section lists the currently selected items in the order they will appear in the book.

The list shows the `Item name`, `Type` and `Subject` of your current book selections that you can double click-on a selection to setup/configure that report or use the [Current book context menu](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_3#Current_book_context_menu) to make further modifications to the book.

{{-}}

##### Current book toolbar

![[_media/ManageBooks-dialog-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Manage Books - dialog]]

The bottom right vertical set of toolbar icons beside the section table operate on the sections and allow the following functions:

- Use the icon button to add the selected item from the top section list to the section list below. Using the shortcut or double-clicking the (top list's) selected item will also add it.
- Use the icon button to remove an item from the bottom section list.
- Use the icon button to change the order of the selected item in the .
- Use the icon button to change the order of the selected item in the .
- With the icon button you can configure the options of the selected **item** of the -- but you must select the item first otherwise the warning will be shown. Double-clicking an item will also start a configuration dialog. The configuration dialog invoked by icon button are item-specific. If you choose not to configure the item, some defaults will be used for all needed options. The common option for almost all book items is the center person: the person on whom the item is centered. Thanks to this option, you can create a book with items centered on different people (e.g. your mom's and dad's ancestors as separate chapters). By default, the center person is set to the .

![[_media/No-selected-book-item-warning-52.png|No selected book item - warning]] {{-}}

##### Current book context menu

- 

- 

- 

- 

---

- 

- 

- 

- 

{{-}}

### Generate Book dialog

![[_media/GenerateBook-dialog-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Generate Book - dialog]]

You will see the dialog once you have selected the dialogs button to accept the defaults and start the creation of your custom genealogy book.

There are two sections and :

#### Paper Options

where you can change the Size and Orientation for the Paper Format, and all Margins. A Checkbox is available to use metric values instead.

See also:

- Same as the
  - Graphical Reports - [Paper Options](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_4#Paper_Options) tab
  - Text Reports - [Paper Options](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_6#Paper_Options) tab

#### Document Options

The section allows you to change the:

- use the drop down menu to change output format:

  - **PDF document** (default)
  - *PostScript*
  - *OpenDocument Text*
  - *Print...*

-  if checked allow you to open in the default viewer eg: [LibreOffice](https://www.libreoffice.org/download/) Writer Word Processor. (checkbox unchecked by default)

- enter your filename, note the filename extension changes depending on the output format. eg: For *PDF document*s the default value is `/yourhomedir/`<Family Tree name>`_book.pdf` and *OpenDocument Text* the default value is `/yourhomedir/`<Family Tree name>`_book.odt`, et cetera.

#### See also

- [Add a table contents or an index to a Book of Reports](wiki:Add_Table_of_Contents_or_Index_to_reports)

{{-}}

<hr>

Back to [Index of Reports](wiki:Gramps_6.0_Wiki_Manual_-_Reports).

[Category:Documentation](wiki:Category:Documentation) [Category:Plugins](wiki:Category:Plugins)
