---
title: Gramps 6.0 Wiki Manual - Reports/he
categories:
- He:דוחות
- He:מתקעים
- He:תיעוד
managed: false
source: wiki-scrape
wiki_revid: 119566
wiki_fetched_at: '2026-05-30T19:21:06Z'
lang: he
---

<div dir="rtl" lang="he" class="mw-content-rtl">

{{#vardefine:chapter\|13}} {{#vardefine:figure\|0}} ![[_media/Menubar-ReportsOverview-60.png|איור. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menubar - Reports Overview]] This section describes all the different reports available in Gramps.

Gramps comes with a large number of available reports. The different subsections describe the various possibilities and options:

## מבוא

[Generating Reports](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_1): This first subsection gives you some general remarks.

## דוחות

![[_media/ToolbarIcon-Reports-OpenTheReportsDialog-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Toolbar Icon for "Open the reports dialog"]]

The reports can be accessed by choosing the menu .

Alternatively, you can browse the complete selection of available reports along with their brief descriptions in a dialog invoked by clicking the icon on the toolbar from any of the categories. {{-}}

### חלונית בחירת דוחות

![[_media/ReportSelection-dialog-default-60.png|איור {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} — חלונית בחירת דוחות — תצוגת ברירת מחדל]]

![[_media/ReportSelection-dialog-example-60.png|איור {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} — חלונית בחירת דוחות — דוגמה המציגה מידע על הדוח "תרשים ציר־זמן"]]

חלונית מאפשרת לעיין בכלל הדוחות הזמינים בליווי תיאור קצר של כל דוח. ניתן לפתוח אותה על ידי לחיצה על הסמל ![[_media/Gramps-reports.png]] שבסרגל הכלים, מכל אחת מהתצוגות.

**יש לבחור דוח מתוך הרשימה שמשמאל**. יש להשתמש בלחצני כדי להרחיב את הרשימות הראשיות:

- [תרשימים](#Graphs)
- [דוחות חזותיים](#Graphical_Reports)
- [דוחות מלל](#Text_Reports)
- [דפי מרשתת](#Web_Pages)

לאחר בחירת דוח, יוצגו בצד ימין של החלונית הפרטים הבאים:

- שם הדוח
- תיאור הדוח
- מצב:
- מחבר:
- דוא"ל של המחבר:

לאחר מכן ניתן להשתמש בלחצנים הבאים כדי לצפות בפרטים נוספים או להפיק את הדוח:

- — פותח את דף העזרה של הדוח (אם קיים) — נדרש חיבור למרשתת

- — סגירת החלונית

- — — פותח את חלונית ההגדרות של הדוח

{{-}}

למידע נוסף: [חלונית בחירת כלים](wiki:Gramps_6.0_Wiki_Manual_-_Tools/he#דו־שיח_בחירת_כלים)

## Substitution Values

[Substitution Values](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_2): you can use some handy values in your reports. (Selected reports only)

## Books

[The Books Report](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_3#Books) allows you to create a custom **genealogy book** containing a collection of Gramps textual and graphical reports in a single document (i.e. a Book)

### Available items selections

#### Alphabetical Index

[Alphabetical Index](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_3#Alphabetical_Index) - This item produces page(s) with an alphabetical index of people noted into selected textual reports.

#### מלל מותאם אישית

[Custom Text](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_3#Custom_Text) - This item produces a page with three paragraphs, each containing custom text: Initial Text, Middle Text and Final Text. The text input fields are expandable so you can really put all the text you want in there.

#### תוכן ענינים

[Table Of Contents](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_3#Table_of_contents) - A Table of contents (TOC) is generated for book as a list of the parts of a book or document organized in the order in which the parts appear.

#### Title Page

[Title Page](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_3#Title_Page) - A title page for your book.

## תרשימים

[Graphs](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_5#Graphs) reports are created in the in Graphviz format and then converted into graphical output running it through the Graphviz dot tool behind the scene.

#### <u>Family Lines Graph</u>

![[_media/Graphs-FamilyLinesGraph-example-overview-50.png|Family Lines Graph]]The [Family Lines Graph](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_5#Family_Lines_Graph) creates an easy-to-follow graph.

#### <u>Hourglass Graph</u>

![[_media/Graphs-HourglassGraph-example-overview-50.png|Hourglass]]The [Hourglass Graph](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_5#Hourglass_Graph) generate an hourglass graph.

#### <u>Relationship Graph</u>

![[_media/Graphs-RelationshipGraph-example-overview-50.png|Relationship]]The [Relationship Graph](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_5#Relationship_Graph) creates a complex relationship graph.

## Graphical Reports

[Graphical reports](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_4#Graphical_Reports) represent information in forms of charts and graphs.

#### <u>Ancestor Tree</u>

The [Ancestor Tree report](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_4#Ancestor_Tree) generates the chart of people who are ancestors of the Active Person.

#### <u>Calendar</u>

The [Calendar report](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_4#Calendar) produces a calendar with birthdays and anniversaries on a page by month.

#### <u>Descendant Tree</u>

The [Descendant Tree report](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_4#Descendant_Tree) generates a graph of people who are descendants of the Active Person.

#### <u>Family Descendant Tree</u>

The [Family Descendant Tree](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_4#Family_Descendant_Tree) generates a graph of people who are descendants of the Active Family.

#### <u>Fan Chart</u>

The [Fan Chart report](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_4#Fan_Chart) produces a chart resembling a fan, with Active Person in the center, parents the semicircle next to it, ans so on, for a total of five generations.

##### See also

#### <u>Statistics Charts</u>

The [Statistics Charts report](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_4#Statistics_Charts) can collect and display a wealth of statistical data about your database.

#### <u>Timeline Chart</u>

The [Timeline Chart report](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_4#Timeline_Chart) outputs the list of people with their lifetimes represented by intervals on a common chronological scale.

## Text Reports

[Text reports](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_6#Text_Reports) output information as formatted text.

#### <u>Ahnentafel Report</u>

The [Ahnentafel Report](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_6#Ahnentafel_Report) lists the Active Person and his or her ancestors along with their vital data. The people are numbered in an establish standard called 'Ahnentafel'.

#### <u>Birthday and Anniversary Report</u>

The [Birthday and Anniversary Report](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_6#Birthday_and_Anniversary_Report) gives the same information as a calendar but in text format.

#### <u>Complete Individual Report</u>

The [Complete Individual Report](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_6#Complete_Individual_Report) provides individual summaries similar to that of the Individual Summary Report.

#### <u>Database Summary Report</u>

The [Database Summary Report](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_6#Database_Summary_Report) displays the overall statistics concerning number of individuals of each gender, various incomplete entries statistics, as well as family and media statistics.

#### <u>Descendant Report</u>

The [Descendant Report](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_6#Descendant_Report) presents the descendants of the Active Person with a brief description in intended style.

#### <u>Detailed Ancestral Report</u>

The [Detailed Ancestral Report](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_6#Detailed_Ancestral_Report) covers in detail the ancestors of the Active Person, including a range of vital data as well as marriages.

#### <u>Detailed Descendant Report</u>

The [Detailed Descendant Report](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_6#Detailed_Descendant_Report) covers in detail the descendants of the Active Person by generation, following the genealogical tradition of textual descendant reports by generation. It aims to provide all important features expected to be found in these classic descendency formats and has received influence from various sources.

#### <u>End of Line Report</u>

The [End of Line Report](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_6#End_of_Line_Report) provides a list of of the person's last known ancestors with the pedigree line, ordered by generations.

#### <u>Family Group Report</u>

The [Family Group Report](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_6#Family_Group_Report) creates a family group report, showing information on a set of parents and their children.

#### <u>Kinship Report</u>

[Kinship Report](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_6#Kinship_Report) provides the kinship of selected person according to level search( height, down generations) set by the user.

#### <u>Note Link Report</u>

The [Note Link Report](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_6#Note_Link_Report) checks the status of internal Gramps links in notes.

#### <u>Number of Ancestors Report</u>

The [Number of Ancestors Report](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_6#Number_of_Ancestors_Report) displays the number of ancestors of the Active Person. The form is - generation x has y individuals (z %).

#### <u>Place Report</u>

The [Place Report](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_6#Place_Report) produces a report according to places selected by the user. It will list related person and event to the selected place.

#### <u>Records Report</u>

[Records Report](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_6#Records_Report) shows a number of interesting records(mostly age related) in your database, like oldest living person, youngest mother,etc.

#### <u>Tag Report</u>

The [Tag Report](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_6#Tag_Report) lists primary objects - persons, families, and notes - who match the selected tag.

## Web Pages

[Web Pages](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_7#Web_Pages) for use on your personal website or to give away as a standalone report.

#### <u>Narrated Web Site</u>

One of the reports in this category is the [Narrated Web Site report](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_7#Narrated_Web_Site). It generates a web site (that is, a set of linked web pages), for a set of selected individuals.

#### <u>Web Calendar</u>

The [Web Calendar](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_7#Web_Calendar) is a Report that creates webpages showing events for the selected individuals as a set of monthly calendars.

#### <u>Dynamic Web Report</u>

The [Dynamic Web Report](wiki:Addon:DynamicWeb_report) Addon creates interactive web pages of the family tree database with options allowing a wide range of customization.

This addon is based on the [Narrative Web Report](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_7#Narrated_Web_Site) native Gramps report.

## מצגים מהירים

[מצג מהיר](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_8#Quick_Views/he) are reports that are available in the context menu's of person, family, ... They maybe created by users, even with limited programming knowledge. {{-}}

[Category:He:תיעוד](wiki:Category:He:תיעוד) [Category:He:מתקעים](wiki:Category:He:מתקעים) [Category:He:דוחות](wiki:Category:He:דוחות)
