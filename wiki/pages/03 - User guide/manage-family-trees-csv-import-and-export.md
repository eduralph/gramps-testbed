---
title: 'Gramps 6.0 Wiki Manual - Manage Family Trees: CSV Import and Export'
categories:
- Documentation
- Gramps Examples
managed: false
source: wiki-scrape
wiki_revid: 129959
wiki_fetched_at: '2026-05-30T11:35:21Z'
---

{{#vardefine:chapter\|6}} {{#vardefine:figure\|0}} This section relates to using Gramps with the **Comma Separated Values Spreadsheet(CSV)** format.

- [Gramps CSV import](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees#Gramps_CSV_import)
- [Comma Separated Values Spreadsheet(CSV) export](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees#Comma_Separated_Values_Spreadsheet.28CSV.29_export)

You can also [Export](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Export_View) the current list view to a Spreadsheet(\*.ODT) or CSV file.

## Gramps Spreadsheet Import/Export

This format allows you to import/export a spreadsheet of data all at once. By default, the spreadsheet must be in the Comma Separated Value (CSV) format. (Although alternative Delimiters can be specified for the [CSV Dialect](wiki:Gramps_6.0_Wiki_Manual_-_Settings#CSV_Dialect) in the in list views.) Most spreadsheet programs can read and write this format. It is also easy to write by hand. This is the only Gramps import format which allows for merging with existing data.

There are three main uses for this format:

1.  You can export your core Gramps data into a spreadsheet format, edit it with a text or spreadsheet program, and import the changes and additions back into Gramps. This is handy for sending to others to fill in, or for taking on the road when you don't have your full Gramps application.
2.  You can import new data into your Gramps family tree (database). For example, if you have a set of new people to add to your family tree, but don't want to hunt and peck your way to finding where they go, you might find it easier to type them into a spreadsheet, and then quickly bring all of them in at once. This is handy if you have a large amount of data that you are cutting and pasting from another application or the web. An example of this is [restoring your Gramps family tree](wiki:Narrative_Website_Import) by loading the Narrative Website into a spreadsheet.
3.  You can also import a set of corrections and additions. Say that you have printed out a report, and you are going through it marking corrections. If you make each correction a section of a spreadsheet, you can "script the edits" and then execute them all at once.

## Export

### Exporting a Family Tree

![[_media/ExportAssistant-ExportOptions-CSV-defaults-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Export Assistant - Export Options - wizard dialog (showing defaults for "Comma Separated Values Spreadsheet(CSV)") with Bottom section for File format specific options]]

To export your family tree:

1.  Start Gramps
2.  Load the Family Tree to be exported
3.  Select from the menu
4.  Select on the window.
5.  Select **Comma Separated Values Spreadsheet (CSV)** on the window
6.  On the window:
    1.  In the top section, select which filters to apply to your family tree
    2.  From the checkboxes, select which items to include in the export (people, marriages, children, places) and whether to Translate headers into the language currently being used.
7.  On the window, select the destination filename and path
8.  On the window, verify the setting and click the button to begin the actual export.

{{-}}

A subset of fields containing your genealogy data will be saved to a .csv file in the format described below. The people and families are annotated in such a way that allows the data to be edited and overwrite the outdated information as they are Imported back in. The annotations allow updating the Tree database via Import.

There are some columns that will be blank, specifically note and source columns. These are listed in the spreadsheet so that you can make notes for the import, but notes are never exported with this tool.

Your data is broken up into four sections representing places, individuals, marriages, and children. The exported fields and column names are:

Places  
Place, Title, Name, Type, Latitude, Longitude, Code, Enclosed_by, Date

<!-- -->

Individuals  
Person, Lastname, Firstname, Callname, Suffix, Prefix, Title, Gender, Birthdate, Birthplace (or Birthplaceid), Birthsource, Baptismdate, Baptismplace (or Baptismplaceid), Baptismsource, Deathdate, Deathplace (or Deathplaceid), Deathsource, Burialdate, Burialplace (or Burialplaceid), Burialsource, Note

<!-- -->

Marriages  
Marriage, Husband, Wife, Date, Place (or Placeid), Source, Note

<!-- -->

Families  
Family, Child

The first column in each area is the Gramps ID. That is what will connect your edits back to the appropriate data, so do not alter those IDs. Load this file into your favorite spreadsheet using comma separated, double-quote text delimited, and Text format (any encoding for now). Then you can add or correct data, and save it back out, keeping the same format. You can then import the data back on top of your old data and it will be corrected.

. . {{-}}

### Exporting a single category

You can export all the data of a single category - e.g. Places - by selecting the category view and then using

![[_media/CategoryView-CSV-Export-Options-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Category View Configure CSV export options]] Before exporting the data, you can select CSV format, that fits best for your environment or purpose.

Click the ![[_media/Gramps-config.png]] icon on the to open the Configure View CSV Dialect dialog

Using the Custom option makes it possible to choose a specific column separation character, e.g. tab or '\|'. {{-}}

## Import

To import your CSV data:

1.  Use the file from above, or create a spreadsheet (described [below](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees:_CSV_Import_and_Export#Example_CSV_with_multiple_areas)) with genealogical data
2.  Start Gramps
3.  Create a new Family Tree
4.  Select from the menu
5.  Select the **Comma Separated Values Spreadsheet (CSV)** file and then select the button

The merge part of this code will only add or update information to your family tree, and it always assume that the spreadsheet data is the correct version.

If you load this spreadsheet into LibreOffice Calc, make sure you select each column as type **Text** rather than **Standard**. Standard will reformat your dates and numbers. Also, if you use Excel, you will probably want to select all cells once opened, and change the format of the cells to **Text**.

The spreadsheet is data made up of columns. Each column should have at the top of it the name of what type of data is in the column. The first column in each area is the Gramps ID reference. You must use special names for the columns. They are:

### Place

    place - a reference to this place
    title - title of place
    name - name of place
    type - type of place (eg, City, County, State, etc.)
    latitude - latitude of place (in decimal format)
    longitude - longitude of place (in decimal format)
    code - postal code, etc.
    enclosed_by - the reference to another place that encloses this one
    date - date that the enclosed_by place was in effect

### People

    person -  a reference to be used for families (marriages, and children) 
    grampsid - to assign a Gramps id to the person
    firstname/first_name/given_name/given - a person's first name
    surname/lastname/last_name - a person's last name
    callname/call_name/call - a common name (nickname) for the person
    prefix - surname prefix (von, de, etc)
    suffix - a suffix of a person's name (Jr., Sr.)
    title - a person's title (Dr., Mr.)
    gender - male or female (you should use the translation for your language)
    source - source title for person
    note - a note for the person's record

    birthdate - date of birth
    birthplace - place of birth (only use if Place ID column is blank)
    birthplaceid/birthplace_id/birth_place_id - place id of birth (only use if Place name column is blank)
    birthsource - source title for birth

    baptismdate - date of baptism
    baptismplace - place of baptism (only use if Place ID column is blank)
    baptismplaceid - place id of baptism (only use if Place name column is blank)
    baptismsource - source title of baptism

    deathdate - date of death
    deathplace - place of death (only use if Place ID column is blank)
    deathplaceid - place id of death (only use if Place name column is blank)
    deathsource - source title for death
    deathcause - cause of death

    burialdate - date of burial
    burialplace - place of burial (only use if Place ID column is blank)
    burialplaceid - place id of burial (only use if Place name column is blank)
    burialsource - source title of burial

    occupationdate - date of occupation
    occupationplace - place of occupation (only use if Place ID column is blank)
    occupationplace_id - place id of occupation (only use if Place name column is blank)
    occupationsource - source title of occupation
    occupationdescr - description of occupation

    residencedate - date of residence
    residenceplace - place of residence (only use if Place ID column is blank)
    residenceplace_id - place id of residence (only use if Place name column is blank)
    residencesource - source title of residence

    attributetype - type of attribute
    attributevalue - value of attribute
    attributesource - source title of attribute

### Marriage

    marriage - if you want to reference this from a family, you'll need a matching name here
    husband/father/parent1 - the reference of the person above who is the husband 
                             (for female parent1, you'll need to put gender in the person area, 
                             or edit it later in gramps)
    wife/mother/parent2 - the reference of the person above who is the wife 
                             (for male parent2, you'll need to put gender in the person area, 
                             or edit it later in gramps)
    date - the date of the marriage
    place - the place of the marriage (only use if Place id column is blank)
    placeid - the place id of the marriage (only use if Place name column is blank)
    source - source title of the marriage
    note - a note about the marriage/wedding

### Family

    family - a reference to tie this to a marriage above (required)
    child - the reference of the person above who is a child
    source - source title of the marriage
    note - a note about the family
    gender - male or female (you should use the translation for your language) 
             [You can put gender here, or in person above]

## Details

Column names are not case-sensitive. You may use any combination of the columns, in any order. (**Actually, you have to at least have a surname and a given name when defining a person, you have to have a marriage and child columns when defining children, and places need a place reference, but that is it.**) The column names are the English names given (for now) but the data should be in your language (including the words "male" and "female").

Top-to-bottom order is important in that if you want to reference something in one area to another, the definition MUST come first. For example, if you want to define families of people, the individuals must be defined before the families. The same applies to places. So it is usually best to put the Places data first, people next, then marriages and families.

Each of these can go in its own area in a spreadsheet. There is no limit to the number of areas in a sheet, and each area can have any number of rows. Leave a blank row between "areas". Just make sure that areas are not next to each other; they must be above and below one another.

You can have multiple areas of each kind on a spreadsheet. The only limitation is that if you refer to a person, you must do that in a row lower than where that person is described. Likewise, if you refer to a marriage, you must do that in a row lower than where the marriage is described. References to enclosed_by places must already exist in the database, or be defined in rows above in the spreadsheet.

If you use the 'grampsid' as a way to assign specific ids, be *very* careful when importing to a current database. Any data you enter will **overwrite** the data assigned to that grampsid. If you use ids in the place, person, marriage, or family columns that are surrounded by square brackets (for example '\[I0001\]'), the values you use will be interpreted as grampsids as well. If you are adding **new** items, you are encouraged to avoid use of the bracket format or grampsid columns, so as to avoid accidentally overwriting your data. If you are mixing the bracket (or grampsid) methods with plain references (no square brackets), put the plain referenced data after the bracket referenced data.

If you are entering the data in a text file, and if you wish to have a comma inside one of the values, like "Clinton, Co., MO" then you need place the entire value in double-quotes and put the first double-quote right after the preceding comma. For example:

    marriage, parent1, parent2, place
    m1, p1, p2,"Clinton, Co., MO"
    m2, p3, p4,"Havertown, PA"

A spreadsheet program will do this automatically for you.

### Example CSV

Here is an example spreadsheet in LibreOffice Calc, but any spreadsheet program should work.

![[_media/Gramps-csv-example1.csv-LibreOffice-Calc--example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Example gramps-csv-example1.csv file shown as a &quot;LibreOffice Calc&quot; spreadsheet]] {{-}}

<hr>

Filename: `gramps-csv-example1.csv`

File content:

    ,,,,,,,,,
    ,"Firstname","Surname","Callname","Gender","Prefix","Suffix","Title","Note","Grampsid"
    ,"Douglas","Test","Doug","male","Von","Sr.","Dr.","This is not related","I0007"
    ,"Laura","Test",,"female",,,,,

<hr>

{{-}} Notice that the CSV data need not begin in the first column, nor in the first row.

Once [imported](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees:_CSV_Import_and_Export#Import) into Gramps the resulting data is displayed as follows:

![[_media/FamilyTree-example-imported-gramps-csv-example1.csv-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Example imported CSV file result (Gramps 6.0.3; Microsoft Windows 10)(data from gramps-csv-example1.csv file)]] {{-}}

### Example CSV with multiple areas

Here is an example of a CSV text spreadsheet with multiple areas:

If you create and cut and paste the following into a file, you can import it directly.

<hr>

Filename: `gramps-csv-example2.csv`

File content:

    Place, Title, Name, Type
    [P0001], Michigan, Michigan, State
    L1, Canada, Canada, Country
    L2, USA, USA, Country

    Firstname, Surname, Birthdate, Birth place id
    John,      Tester,  11/11/1965, L1
    Sally,     Tester,  01/26/1973, L1

    Person, Firstname, Surname, Birthdate,    Birth place id
    p1,     Tom,       Smith,   22 Jan 1970, [P0001]
    p2,     Mary,      Jones
    p3,     Jonnie,    Smith
    p5,     James,     Loucher
    p6,     Penny,     Armbruster
    [P0002],Tim,       Sparklet

    Marriage, Husband, Wife
    m1,       p1,      p2
    m2,       p5,      p6

    Family, Child
    m1,     p3
    m1,     p6
    m2,     [P0002]

<hr>

The CSV file shows that a date can be any valid Gramps date, including dates formats like "26 JAN 1973" or "26.1.1973".

If you make your references be Gramps IDs inside square brackets, then you can refer to people already in the family tree, like this:

    Person,    Firstname, Lastname
    joe's boy, Harry,     Smith

    Family,  Child
    [F1524], joe's boy

    Husband, Wife
    [I0123], [I0562]

    firstname, surname
    Timothy, Jones

    place, enclosed_by
    [P0001], [P0002]

This example would create and add Harry Smith to the previously existing family in Gramps, family F1524.

Also, this example would marry two previously existing people, I0123, and I0562.

This also creates a person named Timothy Jones who is not related to anyone.

Finally, this also make place P0001 be enclosed by place P0002.

### Example CSV from Spreadsheet

![[_media/Gramps-csv-example3.ods-LibreOffice-Calc-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Manually entered data in a spreadsheet: <code>gramps-csv-example3.ods</code>]]

Using Gramps [Example.gramps](wiki:Example.gramps) for this example. The children already exist in the Family Tree. So you can enter an entire generation (8 names with marriage dates) into an spreadsheet in LibreOffice Calc.

Notice that you can use numbers or strings as the reference names between areas. In the person area, I used the numbers 1 through 8. That made it easy to refer to them in the second area of marriages. The marriages are labeled with the letters A through D.

Also note that in the spreadsheet the children in the third area are existing people in Gramps as indicated by the square brackets around the Gramps IDs.

Saving as a CSV file using LibreOffice Calc

<hr>

Filename: `gramps-csv-example3.csv`

File content:

    ,,,
    ,,,
    "Person","Firstname","Lastname",
    1,"Peter","Blank",
    2,"Anna Maria","Kiefer",
    3,"Georg","Schmidt",
    4,"Barbara","Goering",
    5,"Johann","Kiefer",
    6,"Fides","Federer",
    7,"Sebastian","Schelli",
    8,"Magdelena","Schlegel",
    ,,,
    ,,,
    "Marriage","Husband","Wife","Date"
    "A",1,2,"28 jan 1712"
    "B",3,4,"4 may 1732"
    "C",5,6,02/07/1930
    "D",7,8,17/08/1927
    ,,,
    "Family","Child",,
    "A","[I0104]",,
    "B","[I0105]",,
    "C","[I0972]",,
    "D","[I0973]",,

<hr>

{{-}} And importing from the CSV file into the existing Gramps *Example.gramps* family tree produces the far right-hand column shown on the **After:** Pedigree chart tree screenshot. ![[_media/ChartsCategory-Pedigree-view1-horizontal-right-standard-5gen-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Before: Pedigree view tree]]

![[_media/FamilyTree-example-imported-gramps-csv-example3.csv-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} After: Saving as CSV and importing into Gramps produces the far right-hand column in the Pedigree view tree.]] {{-}}

### See also

- [CSV Dialect](wiki:Gramps_6.0_Wiki_Manual_-_Settings#CSV_Dialect) settings for delimiters
- Gramps forum discussion:
  - [CSV template for Text Import](https://gramps.discourse.group/t/csv-template-for-text-import/5277/5)

<!-- -->

- [Addon:Import (text) Gramplet](wiki:Addon:ImportGramplet) Third party addon by Doug Blank - an interactive version of the [CSV Import](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees:_CSV_Import_and_Export)
- Python CSV library docs - [dialects and formatting parameters](https://docs.python.org/3/library/csv.html#dialects-and-formatting-parameters)

Examples of customizing the CSV import code to support additional records:

- Feature request : \[CSV\] Importing complex Excel tables into Gramps (such as witnesses information)
- [PR \#139](https://github.com/gramps-project/gramps/pull/139) : Add CSV Import support for AFN and REFN attributes
- [PR \#810](https://github.com/gramps-project/gramps/pull/810) : Add occupation & residence events + attributes in the CSV persons importer

[C](wiki:Category:Documentation) [CSV import/Export](wiki:Category:Gramps_Examples)
