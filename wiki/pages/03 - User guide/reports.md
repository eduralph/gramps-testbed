---
title: Gramps 6.0 Wiki Manual - Reports
categories:
- Documentation
- Plugins
- Stub
managed: false
source: wiki-scrape
wiki_revid: 126315
wiki_fetched_at: '2026-05-30T11:37:27Z'
---

{{#vardefine:chapter\|13}} {{#vardefine:figure\|0}} ![[_media/Menubar-ReportsOverview-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menubar - Reports Overview]] This section provide a brief description of all the different reports available in Gramps.

Gramps comes with a large number of available reports. The different subsections describe the various possibilities and options:

## Introduction

[Generating Reports](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_1): This first subsection gives you some general remarks.

## Reports

![[_media/ToolbarIcon-Reports-OpenTheReportsDialog-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Reports" toolbar icon for "Open the reports dialog"]]

The reports can be accessed by choosing the menu .

Alternatively, you can browse the complete selection of available reports along with their brief descriptions in a dialog invoked by clicking the ![[_media/Gramps-reports.png]] icon on the toolbar from any of the categories. {{-}}

### Report Selection dialog

![[_media/ReportSelection-dialog-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Report Selection - dialog - default information]]

![[_media/ReportSelection-dialog-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Report Selection - dialog - example showing "Timeline Chart" information]]

The dialog allows you to browse the complete selection of available reports along with their brief descriptions when invoked by clicking the ![[_media/Gramps-reports.png]] icon on the toolbar from any of the categories.

**Select a report from those available on the left**. Use the arrows to expand the top level listings:

- [Graphs](#Graphs)
- [Graphical Reports](#Graphical_Reports)
- [Text Reports](#Text_Reports)
- [Web Pages](#Web_Pages)

Then select the report you are interested in to be shown on the right hand side the following:

- Report name
- Report description
- Status:
- Author:
- Author's email:

You can can then use the buttons below to either find out more about the report or open and create your report.

- opens the help page if available - needs an internet connection

- exits this dialog

- \-  - opens the reports configuration page.

{{-}} See also: [Tool Selection dialog](wiki:Gramps_6.0_Wiki_Manual_-_Tools#Tool_Selection_dialog)

## Substitution Values

[Substitution Values](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_2): you can use some handy values in your reports. (Selected reports only)

## Books

[The Books Report](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_3#Books) allows you to create a custom **genealogy book** containing a collection of Gramps textual and graphical reports in a single document (i.e. a Book)

### Available items selections

#### Alphabetical Index

[Alphabetical Index](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_3#Alphabetical_Index) - This item produces page(s) with an alphabetical index of people noted into selected textual reports.

#### Custom Text

[Custom Text](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_3#Custom_Text) - This item produces a page with three paragraphs, each containing custom text: Initial Text, Middle Text and Final Text. The text input fields are expandable so you can really put all the text you want in there.

#### Table Of Contents

[Table Of Contents](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_3#Table_of_contents) - A Table of contents (TOC) is generated for book as a list of the parts of a book or document organized in the order in which the parts appear.

#### Title Page

[Title Page](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_3#Title_Page) - A title page for your book.

## Summary of Reports

Summary of all default built-in Reports that can be used.

{{-}}

### Reports List

Click a list header to sort the list and show available builtin Report choices. (The actual Report menu will also include installed [Third-party addon](wiki:6.0_Addons#Addon_List) Reports.)

## Graphs

[Graphs](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_5#Graphs) reports are created in Graphviz format and then converted into graphical output running it through the [Graphviz dot tool](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_5#Prerequisites_for_Graph_Reports) behind the scene.

### <u>Family Lines Graph</u>

The [Family Lines Graph](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_5#Family_Lines_Graph) creates an easy-to-follow graph.

### <u>Hourglass Graph</u>

The [Hourglass Graph](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_5#Hourglass_Graph) generate an hourglass graph.

### <u>Relationship Graph</u>

The [Relationship Graph](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_5#Relationship_Graph) creates a complex relationship graph.

## Graphical Reports

[Graphical reports](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_4#Graphical_Reports) represent information in forms of charts and graphs.

### <u>Ancestor Tree</u>

<span ID="Ancestor Chart"></span> The [Ancestor Tree report](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_4#Ancestor_Tree) generates the chart of people who are ancestors of the Active Person.

### <u>Calendar</u>

The [Calendar report](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_4#Calendar) produces a calendar with birthdays and anniversaries on a page by month.

### <u>Descendant Tree</u>

<span ID="Descendant Chart"></span> The [Descendant Tree report](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_4#Descendant_Tree) generates a graph of people who are descendants of the Active Person.

### <u>Descendants Lines</u>

[Addon:DescendantsLines](wiki:Addon:DescendantsLines) - Third Party Addon.

### <u>Family Descendant Tree</u>

The [Family Descendant Tree](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_4#Family_Descendant_Tree) generates a graph of people who are descendants of the Active Family.

### <u>Family Tree</u>

[Addon:Family Tree](wiki:Addon:Family_Tree) - Third Party Addon.

### <u>Fan Chart</u>

The [Fan Chart report](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_4#Fan_Chart) produces a chart resembling a fan, with Active Person in the center, parents the semicircle next to it, and so on, for a total of five generations.

#### See also

### <u>Pedigree Chart</u>

[Addon:PedigreeChart](wiki:Addon:PedigreeChart) - Third Party Addon.

### <u>Statistics Charts</u>

The [Statistics Charts report](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_4#Statistics_Charts) can collect and display a wealth of statistical data about your database.

### <u>Timeline Chart</u>

The [Timeline Chart report](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_4#Timeline_Chart) outputs the list of people with their lifetimes represented by intervals on a common chronological scale.

## Text Reports

[Text reports](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_6#Text_Reports) output information as formatted text.

### <u>Ahnentafel Report</u>

The [Ahnentafel Report](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_6#Ahnentafel_Report) lists the Active Person and his or her ancestors along with their vital data. The people are numbered in an establish standard called 'Ahnentafel'. <span id="AncestorFill">

### <u>Ancestorfill Report</u>

[Addon:Ancestor Fill Report](wiki:Addon:Ancestor_Fill_Report) - Third Party Addon. </span>

### <u>Birthday and Anniversary Report</u>

The [Birthday and Anniversary Report](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_6#Birthday_and_Anniversary_Report) gives the same information as a calendar but in text format.

### <u>Complete Individual Report</u>

The [Complete Individual Report](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_6#Complete_Individual_Report) provides individual summaries similar to that of the Individual Summary Report.

### <u>Database Differences Report</u>

[Addon:Database Differences Report](wiki:Addon:Database_Differences_Report) - Third Party Addon.

### <u>Database Summary Report</u>

The [Database Summary Report](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_6#Database_Summary_Report) displays the overall statistics concerning number of individuals of each gender, various incomplete entries statistics, as well as family and media statistics.

### <u>Descendant Book</u>

[Addon:Descendant and Detailed Descendant Book](wiki:Addon:Descendant_and_Detailed_Descendant_Book_Reports#Differences_to_Descendant_Reports) Reports - Third Party Addon.

### <u>Descendant Report</u>

The [Descendant Report](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_6#Descendant_Report) presents the descendants of the Active Person with a brief description in intended style.

### <u>Detailed Ancestral Report</u>

The [Detailed Ancestral Report](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_6#Detailed_Ancestral_Report) covers in detail the ancestors of the Active Person, including a range of vital data as well as marriages.

### <u>Detailed Descendant Book</u>

[Addon:Descendant and Detailed Descendant Book](wiki:Addon:Descendant_and_Detailed_Descendant_Book_Reports#Differences_to_Descendant_Reports) Reports - Third Party Addon.

### <u>Detailed Descendant Report</u>

The [Detailed Descendant Report](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_6#Detailed_Descendant_Report) covers in detail the descendants of the Active Person by generation, following the genealogical tradition of textual descendant reports by generation. It aims to provide all important features expected to be found in these classic descendency formats and has received influence from various sources.

### <u>Detailed Descendant Report with all Images</u>

[Addon:Detailed Descendant Report With All Images](wiki:Addon:Detailed_Descendant_Report_With_All_Images) - Third Party Addon.

### <u>Double Cousins</u>

[Addon:DoubleCousinReport](wiki:Addon:DoubleCousinReport) - Third Party Addon.

### <u>End of Line Report</u>

The [End of Line Report](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_6#End_of_Line_Report) provides a list of of the person's last known ancestors with the pedigree line, ordered by generations.

### <u>Family Group Report</u>

The [Family Group Report](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_6#Family_Group_Report) creates a family group report, showing information on a set of parents and their children.

### <u>Family Sheet Report</u>

[Addon:Family Sheet](wiki:Addon:Family_Sheet) - Third Party Addon.

### <u>Kinship Report</u>

[Kinship Report](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_6#Kinship_Report) provides the kinship of selected person according to level search( height, down generations) set by the user.

### <u>Last Change Report</u>

[Addon:LastChange](wiki:Addon:LastChange) - Third-Party Addon.

### <u>Lines of Descendancy Report</u>

[Addon:Lines of Descendency Report](wiki:Addon:Lines_of_Descendency_Report) - Third-Party Addon.

### <u>Media Report</u>

[Addon:MediaReport](wiki:Addon:MediaReport) - Third-Party Addon.

### <u>Note Link Report</u>

The [Note Link Report](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_6#Note_Link_Report) checks the status of internal Gramps links in notes.

### <u>Note Report</u>

[Addon:Note_Report](wiki:Addon:Note_Report) - Third-Party Addon.

### <u>Number of Ancestors Report</u>

The [Number of Ancestors Report](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_6#Number_of_Ancestors_Report) displays the number of ancestors of the Active Person. The form is - generation x has y individuals (z %).

### <u>PersonEverything Report</u>

[Addon:PersonEverything Report](wiki:Addon:PersonEverything_Report) - Third-Party Addon.

### <u>Place Report</u>

The [Place Report](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_6#Place_Report) produces a report according to places selected by the user. It will list related person and event to the selected place.

### <u>Records Report</u>

[Records Report](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_6#Records_Report) shows a number of interesting records(mostly age related) in your database, like oldest living person, youngest mother,etc.

### <u>Repositories Report</u>

[Addon:Repositories Report](wiki:Addon:RepositoriesReport) - Third-Party Addon.

### <u>Repositories Options Report</u>

[Addon:Repositories Options Report](wiki:Addon:RepositoriesReport#Repositories_Report_Options) Third Party Addon.

### <u><span title="Sandclock_Tree">Sandclock Tree Report</span></u>

[Addon:GenealogyTree (Sandclock tree subsection) Report](wiki:Addon:GenealogyTree#Sandclock_tree) - Third-Party Addon.

### <u>Sources and Citations Report</u>

[Addon:Sources Citations Report](wiki:Addon:SourcesCitationsReport) - Third-Party Addon.

### <u>Tag Report</u>

The [Tag Report](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_6#Tag_Report) lists primary objects - persons, families, and notes - who match the selected tag.

### <u>TinyTafel Report</u>

[Addon:TinyTafel](wiki:Addon:TinyTafel) - Third-Party Addon.

### <u>ToDo Report</u>

[Addon:ToDo Report](wiki:Addon:ToDoReport) - Third-Party Addon.

## Web Pages

[Web Pages](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_7#Web_Pages) for use on your personal website or to give away as a standalone report.

### <u>Narrated Web Site</u>

The [article about the <strong>Narrated Web Site report</strong>](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_7#Narrated_Web_Site) describes the report with extensive options for generating a web site (i.e., a set of linked web pages), for a subset of selected individuals.

### <u>Web Calendar</u>

The [Web Calendar](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_7#Web_Calendar) is a Report that creates webpages showing events for the selected individuals as a set of monthly calendars.

### Network_Chart

- [Network Chart](wiki:Addon:NetworkChart) Third-party addon.

### See Also

- [Web Solutions for Gramps](wiki:Web_Solutions_for_Gramps)

## Quick Views

[Quick Views](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_8#Quick_Views) are reports that are available in the context menus of person, family, ... They maybe created by users, even with limited programming knowledge. {{-}}

[Category:Documentation](wiki:Category:Documentation) [Category:Plugins](wiki:Category:Plugins)
