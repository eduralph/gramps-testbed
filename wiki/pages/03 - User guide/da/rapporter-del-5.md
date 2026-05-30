---
title: Da:Gramps 6.0 brugsanvisning - Rapporter - del 5
categories:
- Documentation
- Plugins
- Stub
managed: false
source: wiki-scrape
wiki_revid: 129291
wiki_fetched_at: '2026-05-30T17:32:09Z'
lang: da
---

{{#vardefine:chapter\|13.1}} {{#vardefine:figure\|0}} Tilbage [Indeks over Rapporter](wiki:Da:Gramps_6.0_brugsanvisning_-_Rapporter). {{-}}

<hr>

{{-}}

![[_media/MenuOverview-Reports-Graphs-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}}  Menu overview]] This section describes the different (aka Graph Reports) available in Gramps.

## Graphs

All three graph reports: [Family Lines](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_5#Family_Lines_Graph), [Hourglass](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_5#Hourglass_Graph), and [Relationship](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_5#Relationship_Graph) Graphs share common options: , , and .

Also they share common options with the other reports [common options](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_4#Common_options): and .

### Prerequisites for Graph Reports

Requires the installation of the [GraphViz](wiki:Output_formats#Graphviz) program and Ghostscript program that is used by Graphviz reports to help create PDF files.

- On Linux, use your package manager.
- On Microsoft Windows use the Gramps AIO as they are already part of the installer.
- On Apple macOS use the Gramps .dmg as they are already part of the installer.

### Common Options

There are also several [GraphViz](wiki:Output_formats#Graphviz) specific options related to pagination, color, and details of the graph.

This plugin uses the Graphviz graph visualization and Ghostscript programs. Graphviz takes the generated [<code>.gv</code>](wiki:Output_formats#Graphviz) files and creates the final files, such as `.gif`, `.png`, , `.ps`, (Ghostscript creates `.pdf`), etc.

#### Graphviz Layout

![[_media/FamilyLinesGraph-Graphs-GraphvizLayout-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Family Lines Graph - Graphs - Graphviz Layout - tab default options]]

- Choose the font family. If international characters don't show, use **FreeSans** font. FreeSans is available from [the NonGNU org](http://www.nongnu.org/freefont/).

  - **Default**
  - PostScript/ Helvetica
  - True Type/ FreeSans

- (`14` default) The font size, in [points](https://wikipedia.org/wiki/Point_(typography)).

- Whether the graph goes from top to bottom or left to right

  - **Vertical (top to bottom)** (Default)
  - Vertical (bottom to top)
  - Horizontal (left to right)
  - Horizontal (right to left)

- (`1` default) Graphviz can create very large graphs by spreading the graph across a rectangular array of pages. This controls the number of pages in the array horizontally. **Only valid for dot and pdf via Ghostscript**.

- (`1` default) Graphviz can create very large graphs by spreading the graph across a rectangular array of pages. This controls the number of pages in the array vertically. **Only valid for dot and pdf via Ghostscript**.

- (*Bottom, left* default) The order in which the graph pages are output. This option only applies if the horizontal pages or vertical pages are greater than 1.

- \- How the lines between objects will be drawn. Choose from:

  - *Straight*
  - **Curved** (Default)
  - *Orthogonal*

{{-}}

#### Graphviz Options

![[_media/FamilyLinesGraph-Graphs-GraphvizOptions-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Family Lines Graph - Graphs - Graphviz Options - tab default options]]

- Affects greatly how the graph is laid out on the page. Specifically node spacing and scaling of the graph( see *Advice 1:*).

  - *Compress to minimal minimal size*
  - **Fill the given area** (default)
  - *Expand uniformly*

<hr>

**Advice 1:**

If the graph is smaller than the print area:

- *Compress to minimal minimal size* will not change the node spacing.
- *Fill the given area* will increase the node spacing to fit the print area in both width and height.
- *Expand uniformly* will increase the node spacing uniformly to preserve the aspect ratio.

If the graph is larger than the print area:

- *Compress to minimal minimal size* will shrink the graph to achieve tight packing at the expense of symmetry.
- *Fill the given area* will shrink the graph to fit the print area after first increasing the node spacing.
- *Expand uniformly* will shrink the graph uniformly to fit the print area.

<hr>

- (`72` default) dots-per-inch. When creating PostScript or PDF, use 72 DPI. Typically between 75 and 120 if generating .png or .gif files, but 300 or 600 if generating files to be printed. When creating images such as .gif or .png files for the web, try numbers such as 100 or 300 DPI.

- (`0.20` default) The minimum amount of free space, in inches, between individual nodes. For vertical graphs, this corresponds to spacing between columns. For horizontal graphs, this corresponds to spacing between rows.

- (`0.20` default) The minimum amount of free space, in inches, between ranks. For vertical graphs, this corresponds to spacing between rows. For horizontal graphs, this corresponds to spacing between columns.

#### Note

![[_media/FamilyLinesGraph-Graphs-Note-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Family Lines Graph - Graphs - Note - tab default options]]

- (Empty by default) This text will be added to the graph

- \- Whether the note will appear on top or bottom of the page.

  - **Top** (default)
  - *Bottom*

- (`32` default) The size of note text, in [points](https://en.wikipedia.org/wiki/Point_(typography)).

{{-}}

### <u>Family Lines Graph</u>

![[_media/Graphs-FamilyLinesGraph-example-overview-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Family Lines Graph - Graphs - example output overview]]

The works by starting with a list of "people of interest". This initial list of people is then used to find both ancestors and descendants to generate the using the [GraphViz generator](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_5#Prerequisites_for_Graph_Reports).

A typical use of this report is to generate simplified graphs to be printed on *large format printing plotters*.

To create a from the menu select and then from the tab click on the (add) icon and select at least one person from the selector dialog and the report will suggest if possible a second related person via the warning dialog select or depending on what you decide and then select to generate the report. {{-}} See also:

- [common options](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_5#Common_Options) - (GraphViz specific related to pagination, color, and details of the graph.)

{{-}}

#### Report Options

![[_media/FamilyLinesGraph-Graphs-ReportOptions-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Family Lines Graph - Graphs - Report Options - tab default options]]

-  Parents and their ancestors will be considered when determining "family lines". (checkbox checked by default)

-  Children will be considered when determining "family lines". (checkbox checked by default)

-  People and families not directly related to people of interest will be removed when determining "family lines". (checkbox checked by default)

- Choose the direction that the arrows point:

  - **Descendants \<- Ancestors** (default) - arrows point to the Descendants.
  - *Descendants -\> Ancestors* - arrows point to the Ancestors.
  - *Descendants \<-\> Ancestors* - arrows point to both.
  - *Descendants - Ancestors* - None (no arrows are shown)

- \- Males will be shown with blue, females with red, unless otherwise set above for filled. If the sex of an individual is unknown it will be shown with gray.

  - *B&W outline* - Black and white outline
  - *Coloured outline*
  - **Colour fill** (default)

- to differentiate between women and men.

  - **None** (default)
  - *Female*
  - *Male*
  - *Both*

- Whether (and where) to include Gramps IDs

  - **Do not include** (default)
  - *Share an existing line*
  - *On a line of its own*

{{-}}

#### Report Options (2)

![[_media/FamilyLinesGraph-Graphs-ReportOptions2-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Family Lines Graph - Graphs - Report Options (2) - tab default options]]

- \- Select the format to display the names. This choice in normally taken from the default setting in tab for . Or to override that setting for the report choose from:

  - **Default** - (in a new Family Tree this is normally *Surname, Given Suffix* )
  - *Surname, Given Suffix*
  - *Given Surname Suffix*
  - *Given*
  - *Main Surnames, Given Patronymic Suffix*
  - *SURNAME, Given (Common)*

-  (checkbox checked by default) - Whether to include private data.

- \- How to handle (information about) living people

  - **Included, and all data** (default)
  - *Full names, but data removed*
  - *Given names replaced, and data removed*
  - *Complete names replaced, and data removed*
  - *Not included*

- `0`(default) - Whether to restrict data on recently dead people.

- The translation to be used for the report. Language selector showing all languages supported by Gramps. Defaults to the language you are using Gramps in.

- The format and language for dates, with examples

  - Default - Choose this option to use the default set in tab for option.
  - **YYYY-MM-DD (ISO) (2024-11-15)** (default for report)
  - *Numerical (15/11/2024)*
  - *Month Day, Year (March 14, 2018)*
  - *MON DAY, YEAR (Mar 14, 2018)*
  - *Day Month Year (14 March 2018)*
  - *DAY MON YEAR (14 Mar 2018)*

-  (checkbox checked by default) - Subgraphs can help Grapviz position spouses together, but with non-trival graphs will result in longer lines and larger graphs.

{{-}}

#### People of Interest

![[_media/FamilyLinesGraph-Graphs-PeopleOfInterest-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Family Lines Graph - Graphs - People of Interest - tab default options]]

The graph works by starting with a list of "people of interest". This initial list of people is then used to find both ancestors and descendants.

- click on and to add/remove people of interest. When in doubt, try adding your grandparents as a starting point.

-  (checkbox unchecked by default) Whether to limit the number of ancestors.

  - `50` default. The maximum number of ancestors to include. The maximum is for the total number of people, not generations to be displayed on the chart.

-  (checkbox unchecked by default) Whether to limit the number of descendants.

  - `50` default. The maximum number of descendants to include. The maximum is for the total number of people, not generations to be displayed on the chart.

{{-}}

##### Select Person - Also include <Person Name> warning dialog

Select Person - Also include <Person Name> warning dialog {{-}}

#### Include

![[_media/FamilyLinesGraph-Graphs-Include-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Family Lines Graph - Graphs - Include - tab default options]]

- : date of birth, date of death, and marriage dates will be included in the graph when this is selected. (checkbox checked by default)

- : from the above only show the years.(checkbox unchecked by default)

- : place of birth, place of death, and place of marriage will be included in the graph when this is selected.(checkbox checked by default)

- : marriage text will include the total number of children when this is selected.(checkbox unchecked by default)

-  (checkbox checked by default)

- - **Above the name** (Default)
  - *Beside the name*

- - **Normal** (default)
  - *Large*

{{-}}

#### Family Colours

![[_media/FamilyLinesGraph-Graphs-FamilyColours-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Family Lines Graph - Graphs - Family Colours - tab default options]]

- Select the color to use for people with a specific surname. Two columns are available: *Surname* and *Color*. Click on or to add a surname from the window, select a surname and press . To edit the surname color double-click on a surname and from the window choose from the shown colors and then select .

{{-}}

#### Individuals

![[_media/FamilyLinesGraph-Graphs-Individuals-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Family Lines Graph - Graphs - Individuals - tab default options]]

You can select a color for each of the following from the window and then select the button.

- the colour to use to display men.

- the colour to use to display women.

- the colour to use to display people who neither men nor women.

- the colour to used when gender is unknown (and for people whose surname doesn't match any of the names on the "Family Colours" tab.)

- the colour to use to display families. (marriages).

{{-}}

### <u>Hourglass Graph</u>

![[_media/Graphs-HourglassGraph-example-overview-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Hourglass Graph - Graphs - example output overview]]

Generate an using the [GraphViz generator](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_5#Prerequisites_for_Graph_Reports). Go to .

The hourglass graph chart shows the s ancestors above them and descendants below them. The hourglass graph does not show siblings of the ancestors but it does include all the descendants below them including any spouses. {{-}} See also:

- [common options](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_5#Common_Options) - (GraphViz specific related to pagination, color, and details of the graph.)

{{-}}

#### Report Options

![[_media/HourglassGraph-Graphs-ReportOptions-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Hourglass Graph - Graphs - Report Options - tab default options]]

- the center person for the report, defaults to the current active person.

  - button. - Change the center person.

- default `10`

- default `10`

- Choose the direction that the arrows point:

  - **Centre -\> Others** (default) - arrows point to the Other.
  - *Centre \<- Others* - arrows point to the Centre.
  - *Centre \<-\> Others* - arrows point to both.
  - *Centre - Others* - None (no arrows are shown)

- \- Males will be shown with blue, females with red, unless otherwise set above for filled. If the sex of an individual is unknown it will be shown with gray.

  - *B&W outline* - Black and white outline
  - *Coloured outline*
  - **Colour fill** (default)

-  to differentiate between women and men (checkbox unchecked by default)

- whether to include Gramps IDs.

  - **Do not include** (default)
  - *include*

{{-}}

#### Report Options (2)

![[_media/HourglassGraph-Graphs-ReportOptions2-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Hourglass Graph - Graphs - Report Options (2) - tab default options]]

- \- Select the format to display the names. This choice in normally taken from the default setting in [Edit &gt; Display](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Display) tab for . Or to override that setting for the report choose from:

  - **Default** - (in a new Family Tree this is normally *Surname, Given Suffix* )
  - Surname, Given Suffix
  - Given Surname Suffix
  - Given
  - Main Surnames, Given Patronymic Suffix
  - SURNAME, Given (Common)

-  (checkbox checked by default) - Whether to include private data.

- \- How to handle (information about) living people

  - **Included, and all data** (default)
  - *Full names, but data removed*
  - *Given names replaced, and data removed*
  - *Complete names replaced, and data removed*
  - *Not included*

- `0`(default) - Whether to restrict data on recently dead people.

- The translation to be used for the report. Language selector showing all languages supported by Gramps. Defaults to the language you are using Gramps in.

- The format and language for dates, with examples

  - Default - Choose this option to use the default set in tab for option.
  - **YYYY-MM-DD(ISO)(2018-03-14)** (default for report)
  - Numerical(14/3/2018)
  - Month Day, Year(March 14, 2018)
  - MON DAY, YEAR(Mar 14, 2018)
  - Day Month Year(14 March 2018)
  - DAY MON YEAR(14 Mar 2018)

{{-}}

#### Graph Style

![[_media/HourglassGraph-Graphs-GraphStyle-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Hourglass Graph - Graphs - Graph Style - tab default options]]

You can select a color for each of the following from the window and then select the button.

- the colour to use for males.

- the colour to use for females.

- the colour to use for Others.

- the colour to used when gender is unknown (and for people whose surname doesn't match any of the names on the "Family Colours" tab.)

- the colour to use for families (weddings).

 - Force Sosa / Sosa-Stradonitz / Ahnentafel layout order for all ancestors, so that fathers are always on the left branch and mothers are on the right branch.  - Show Sosa / Sosa-Stradonitz / Ahnentafel number.  - Show genealogical symbols for birth, marriage and death events. {{-}}

### <u>Relationship Graph</u>

![[_media/Graphs-RelationshipGraph-example-overview-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Relationship Graph - Graphs - example output overview]]

The creates a complex relationship graph using the [GraphViz generator](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_5#Prerequisites_for_Graph_Reports).

Via the menu: . You will be presented with a window where you can change all the settings. {{-}} See also:

- [common options](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_5#Common_Options) - (GraphViz specific related to pagination, color, and details of the graph.)

{{-}}

#### Report Options

![[_media/RelationshipGraph-Graphs-ReportOptions-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Relationship Graph - Graphs - Report Options - tab default options]]

- \- Select the filter to be applied to the report. Choose from:

  - **Entire Database** (Default) ()
  - *Descendants of active person*
  - *Descendant families of active person*
  - *Ancestors of active person*
  - *People with common ancestor with active person*
  - *Any custom made filter you have created will be listed below the other choices.*

- The center person for the filter. Defaults to the Active Person. If you use a custom filter, no Person can be chosen.

  - button. - Change the Centre person.

-   
  Choose the direction that the arrows point:

  - **Descendants \<- Ancestors**(default) - arrows point to the to the Descendants.
  - *Descendants -\> Ancestors* - arrows point to the to the Ancestors.
  - *Descendants \<-\> Ancestors* - arrows point to both.
  - *Descendants - Ancestors* - None (no arrows are shown)

- \- Males will be shown with blue, females with red, unless otherwise set above for filled. If the sex of an individual is unknown it will be shown with gray.

  - *B&W outline* - Black and white outline
  - *Coloured outline*
  - **Colour fill** (default)

-  Use rounded corners to differentiate between women and men (checkbox unchecked by default)

-  (checkbox unchecked by default)

- whether to include Gramps IDs.

  - **Do not include** default
  - *include*

{{-}}

#### Report Options (2)

![[_media/RelationshipGraph-Graphs-ReportOptions2-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Relationship Graph - Graphs - Report Options (2) - tab default options]]

- \- Select the format to display the names. This choice in normally taken from the default setting in tab for . Or to override that setting for the report choose from:

  - **Default** - (in a new Family Tree this is normally *Surname, Given Suffix* )
  - *Surname, Given Suffix*
  - *Given Surname Suffix*
  - *Given*
  - *Main Surnames, Given Patronymic Suffix*
  - *SURNAME, Given (Common)*

-  (checkbox checked by default) - Whether to include private data.

- \- How to handle (information about) living people

  - **Included, and all data** (default)
  - *Full names, but data removed*
  - *Given names replaced, and data removed*
  - *Complete names replaced, and data removed*
  - *Not included*

- `0` (default) - Whether to restrict data on recently dead people.

- The translation to be used for the report. Language selector showing all languages supported by Gramps. Defaults to the language you are using Gramps in.

- The format and language for dates, with examples

  - Default - Choose this option to use the default set in [Edit &gt; Display](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Display) tab for option.
  - **YYYY-MM-DD(ISO)(2024-11-15)** (default for report)
  - *Numerical(15/11/2014)*
  - *Month Day, Year(November 15, 2024)*
  - *MON DAY, YEAR(Nov 15, 2024)*
  - *Day Month Year(15 November 2024)*
  - *DAY MON YEAR(15 Nov 2024)*

{{-}}

#### Include

![[_media/RelationshipGraph-Graphs-Include-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Relationship Graph - Graphs - Include - tab default options]]

- \- Whether to include dates and/or places

  - **Do not include any dates or places** (default)
  - *Include (birth, marriage, death) dates, but no places*
  - *Include (birth, marriage, death) dates, and place*
  - *Include (birth, marriage, death) dates, and place if no dates*
  - *Include (birth, marriage, death) years, but no places*
  - *Include (birth, marriage, death) years, and places*
  - *Include (birth, marriage, death) places, but no date*s
  - *Include (birth, marriage, death) dates and places on same line*

-  Show family nodes even if the output contains only one member of the family. (checkbox checked by default)

-  (checkbox unchecked by default)

-  (checkbox unchecked by default)

-  (checkbox unchecked by default)

- Where the thumbnail image should appear relative to the name

  - **Above the name** (Default)
  - *Beside the name*

- Whether to include the last occupation

  - **Do not include any occupation** (default)
  - *Include description of most recent occupation*
  - *Include date, description and place of all occupations*

-  Whether to include 'Ga' and 'Gb' also, to debug the relationship calculator (checkbox unchecked by default)

{{-}}

#### Graph Style

![[_media/RelationshipGraph-Graphs-GraphStyle-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Relationship Graph - Graphs - Graph Style - tab default options]]

You can select a color for each of the following from the window and then select the button.

- the colour to use for males.

- the colour to use for females.

- the colour to use for others.

- the colour to used when gender is unknown (and for people whose surname doesn't match any of the names on the "Family Colours" tab.)

- the colour to use for families (weddings).

-  (checkbox checked by default) - Shows adopted relationships.

-  (checkbox checked by default)

- Decides the location of the parents in the graph.

  - **Normal** (default)
  - *Parents together*
  - *Parents offset*

{{-}}

#### Example relationship graph

![[_media/Graphs-RelationshipGraph-example-overview-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Relationship Graph - Graphs - example output overview]]

Let us make a simple example. We want a relationship graph with the Descendant Families of a certain person.

1.  First check that this person is the *active person*. (You change this later but this is handier)
2.  Go via the menu
3.  Papersize : A4 metric landscape: we know there will be not too many people on the graph, so this is ok
4.  Report Options: filter: Descendant Families of..., Color fill, Use rounded corners
5.  Graph Style : Show Family Nodes
6.  Graphviz Layout: Font size: 15 pts FreeSans Direction: top to bottom
7.  Graphviz Options: Fill given area dpi 133
8.  Note : we add title on the top size: 18 pts
9.  Output Format: we want a JPEG file.

The results are similar to the image shown in Fig. {{#var:chapter}}.{{#var:figure}}. {{-}} See also:

- A detailed tutorial [How to make a relationship chart](wiki:Howto:_Make_a_relationship_chart)

{{-}}

<hr>

Tilbage til [Indeks over Rapporter](wiki:Da:Gramps_6.0_brugsanvisning_-_Rapporter). {{-}}

[Category:Documentation](wiki:Category:Documentation) [Category:Plugins](wiki:Category:Plugins)
