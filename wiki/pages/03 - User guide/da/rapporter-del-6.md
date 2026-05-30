---
title: Da:Gramps 6.0 brugsanvisning - Rapporter - del 6
categories:
- Documentation
- Plugins
managed: false
source: wiki-scrape
wiki_revid: 129292
wiki_fetched_at: '2026-05-30T17:32:39Z'
lang: da
---

{{#vardefine:chapter\|13.1}} {{#vardefine:figure\|0}} Tilbage [Indeks over Rapporter](wiki:Da:Gramps_6.0_brugsanvisning_-_Rapporter). {{-}}

<hr>

{{-}}

![[_media/MenuOverview-Reports-TextReports-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}}  Menu overview]] This sections describes the different available in Gramps.

## Text Reports

Text reports represent the desired information as formatted text. Most of the options are common among text reports, therefore they will be described in the [Common options](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_6#Common_options) section.

The following *Text reports* are available in Gramps:

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

- 

- 

- 

- 

- 

### Common options

Common options for text reports are the filename of the output, the format of the output, selected style, page size and orientation. For HTML reports, there is no page information. Instead, HTML options include the choice of the HTML template, either available in Gramps or a custom template defined by you. Optionally, the reports can be immediately opened with the default application.

The options which are specific to a given report will be described directly in that report's entry and on [Command line references](wiki:Gramps_6.0_Wiki_Manual_-_Command_Line#Action_options).

For each report there is a screen with on the top part tabs (like Paper Options...) and on the bottom part the **Document Options**. The number of tabs varies with the report.

#### Paper Options

![[_media/TextReports-PaperOptions-tab-defaults-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Paper Options" - tab for Text Reports]]

With the tab you can change:

- - **Letter**(default)

  - (`8.50` in. default)

  - (`11.00` in. default)

  - **Portrait**(default)

- - (`1.00` in. default)

  - (`1.00` in. default)

  - (`1.00` in. default)

  - (`1.00` in. default)

-  : whether to use metric values or not (in. or cm.). (checkbox unchecked by default)

{{-}}

#### Document Options

![[_media/TextReports-DocumentOptions-section-PlainText-output-settings-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Document Options - tab defaults for Text Reports (Plain Text - output selected)]] Options below will change slightly depending on the output format selected.

- choose the output format:

  - Print...
  - PDF document
  - HTML
  - Open Document Text
  - PostScript
  - RTF document
  - LaTex
  - Plain Text

- : you can indicate to open the made document your default viewer. (checkbox unchecked by default)

- default value is *`/home/`<username>`/`<Family Tree Name><Report Name>`.txt`*.

- (default is *default*). With the button you can add Document Styles.

- (`72` default)

{{-}}

<hr>

### <u>Ahnentafel Report</u>

![[_media/TextReports-AhnentafelReport-example-overview-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Ahnentafel Report - Text Reports - example output overview]]

The lists the Active Person and his or her ancestors along with their vital data.

You can choose the with

The people are numbered in a special way which is an established standard [Genealogical Numbering System](wiki:Genealogical_Numbering_Systems) called [Ahnentafel](wiki:Genealogical_Numbering_Systems#ahnentafel). This report has some [Ahnentafel specific Style options](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Style_editor_dialog) in the Style Editor accessible via the button.

The Active Person is given number 1. His or her father and mother have numbers 2 and 3, respectively.

This rule holds for every person while going back in generations: father's parents are numbered 4 and 5, and mother's parents are numbered 6 and 7, fathers always numbered with even and mothers with odd numbers.

Therefore, for any person having number N in this tree, the numbers of father and mother are 2N and 2N+1, respectively.

`   person = n`  
`   father = 2n`  
`   mother = 2n+1`

Each entry will consist of a single paragraph, and should contain the following contents:

- Person number.
- Person's name.
- Birth Information, if available.
- Death Information, if available.
- Burial Information, if available

See also [common options](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_6#Common_options) {{-}}

#### Report Options

![[_media/AhnentafelReport-TextReports-ReportOptions-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Ahnentafel Report - Text Reports - Report Options - tab default options]]

- the center person for the report, defaults to the current active person.

  - button to change the center person it will opens the selector allowing you to change the center person, by selecting the check box.

- (`10` default) The number of generations to include in the report.

- whether to include Gramps IDs.

  - **Do not include** (default)
  - *Include*

-  Whether to start a new page after each generation.(checkbox unchecked by default)

-  Indicates if a line break should follow the name.(checkbox unchecked by default)

{{-}}

#### Report Options (2)

![[_media/AhnentafelReport-TextReports-ReportOptions2-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Ahnentafel Report - Text Reports - Report Options (2) - tab default options]]

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
  - Full names, but data removed
  - Given names replaced, and data removed
  - Complete names replaced, and data removed
  - Not included

- `0`(default) - Whether to restrict data on recently dead people.

- The translation to be used for the report. Language selector showing all languages supported by Gramps. Defaults to the language you are using Gramps in.

- The format and language for dates, with examples

  - Default - Choose this option to use the default set in [Edit &gt; Display](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Display) tab for option.
  - **YYYY-MM-DD(ISO)(2018-03-14)** (default for report)
  - Numerical(14/3/2018)
  - Month Day, Year(March 14, 2018)
  - MON DAY, YEAR(Mar 14, 2018)
  - Day Month Year(14 March 2018)
  - DAY MON YEAR(14 Mar 2018)

{{-}}

### <u>Birthday and Anniversary Report</u>

![[_media/TextReports-BirthdayAndAnniversaryReport-example-overview-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Birthday and Anniversary Report - Text Reports - example output overview]]

This report produces a list of birthdays and anniversaries on a page by month. It produces the same information as a [Calendar report](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_4#Calendar) but in text format instead of a calendar table.

You can choose the Birthday and Anniversary Report with {{-}} See also [common options](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_6#Common_options) {{-}}

#### Report Options

![[_media/BirthdayAndAnniversaryReport-TextReports-ReportOptions-tab-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Birthday and Anniversary Report - Text Reports - Report Options - tab default options]]

- \- Select the filter to be applied to the report. Choose from:

  - **Entire Database** (Default)
  - Descendants of **Filter Person**
  - Descendant families of **Filter Person**
  - Ancestors of **Filter Person**
  - People with common ancestor with **Filter Person**
  - *or select from the **Person** category's **[Custom Filters](wiki:Gramps_6.0_Wiki_Manual_-_Filters#Custom_Filters)***

-   
  The center person for the report. (Default to the [Active Person](wiki:Gramps_Glossary#active_person))

  - button to change the filter person it will opens the selector allowing you to change the filter person from the [Bookmarked people](wiki:Gramps_6.0_Wiki_Manual_-_Navigation#Bookmarks). Select the check box to choose from the entire Tree.

- `Birthday an Anniversary Report` (default) - Title of report

- `My Birthday Report` (default) - First line of text at bottom of report

- `Produced with Gramps` (default) - Second line of text at bottom of report

- [`http://gramps-project.org/`](http://gramps-project.org/) (default) - Third line of text at bottom of report

{{-}}

#### Report Options (2)

![[_media/BirthdayAndAnniversaryReport-TextReports-ReportOptions2-tab-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Birthday and Anniversary Report - Text Reports - Report Options (2) - tab default options]]

- \- Select the format to display the names. This choice in normally taken from the default setting in [Edit &gt; Display](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Display) tab for . Or to override that setting for the report choose from:

  - **Default** - (in a new Family Tree this is normally *Surname, Given Suffix* )
  - Surname, Given Suffix
  - Given Surname Suffix
  - Given
  - Main Surnames, Given Patronymic Suffix
  - SURNAME, Given (Common)

-  (checkbox checked by default) - Whether to include private data.

-  (checkbox checked by default) Include only living people in the report.

- The translation to be used for the report. Language selector showing all languages supported by Gramps. Defaults to the language you are using Gramps in.

{{-}}

#### Content

![[_media/BirthdayAndAnniversaryReport-TextReports-Content-tab-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Birthday and Anniversary Report - Text Reports - Content - tab default options]]

- fill in the year. Defaults to current Year.

- Select the country to see associated holidays. None are shown by default.

- Select married women's displayed surname.

  - **Wives use their own surname** (Default)
  - Wives use husband's surname (from first family listed)
  - Wives use husband's surname (from last family listed)

-  Whether to include birthdays in the calendar (checkbox checked by default)

-  Whether to include anniversaries in the calendar (checkbox checked by default)

-  Whether to include relationships to the filter person (Note: Slower to create report) (checkbox unchecked by default)

{{-}}

### <u>Complete Individual Report</u>

![[_media/TextReports-CompleteIndividualReport-example-overview-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Complete Individual Report - Text Reports - example output overview]]

This report provides individual summaries.

You can choose the Complete Individual Report with

See also [common options](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_6#Common_options) {{-}}

#### Report Options

![[_media/CompleteIndividualReport-TextReports-ReportOptions-tab-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Complete Individual Report - Text Reports - Report Options - tab default options]]

The advantage of this report is the specific filter option. Depending on the filter choice (Active Person only, his or her descendants, his or her ancestors, or entire database), the report may contain from one to many individual summaries. Another option for this report is the inclusion of source information when listing events.

-   
  choose between

  - **Entire Database** (Default)
  - Descendants of **Filter Person**
  - Descendant families of **Filter Person**
  - Ancestors of **Filter Person**
  - People with common ancestor with **Filter Person**
  - or select from the **Person** category's **[Custom Filters](wiki:Gramps_6.0_Wiki_Manual_-_Filters#Custom_Filters)**

-   
  The center person for the report. (Default to the [Active Person](wiki:Gramps_Glossary#active_person))

  - button to change the filter person it will opens the selector allowing you to change the filter person from the [Bookmarked people](wiki:Gramps_6.0_Wiki_Manual_-_Navigation#Bookmarks). Select the check box to choose from the entire Tree.

-  (checkbox checked by default)

-  (checkbox unchecked by default)

{{-}}

#### Report Options (2)

![[_media/CompleteIndividualReport-TextReports-ReportOptions2-tab-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Complete Individual Report - Text Reports - Report Options (2) - tab default options]]

-   
  Select the format to display the names. Choose from **Surname, Given Suffix**(default) / Given Surname Suffix / Given / Main Surnames, Given Patronymic Suffix / SURNAME, Given (Common)

-  (checkbox checked by default)

- \- How to handle (information about) living people

  - **Included, and all data** (default)
  - Full names, but data removed
  - Given names replaced, and data removed
  - Complete names replaced, and data removed
  - Not included

- `0`(default) - Whether to restrict data on recently dead people.

- The translation to be used for the report. Language selector showing all languages supported by Gramps. Defaults to the language you are using Gramps in.

- The format and language for dates, with examples

  - Default - Choose this option to use the default set in [Edit &gt; Display](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Display) tab for option.
  - **YYYY-MM-DD(ISO)(2018-03-14)** (default for report)
  - Numerical(14/3/2018)
  - Month Day, Year(March 14, 2018)
  - MON DAY, YEAR(Mar 14, 2018)
  - Day Month Year(14 March 2018)
  - DAY MON YEAR(14 Mar 2018)

{{-}}

#### Include

![[_media/CompleteIndividualReport-TextReports-Include-tab-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Complete Individual Report - Text Reports - Include - tab default options]]

-  (checkbox checked by default)

-  (checkbox checked by default)

-  (checkbox unchecked by default)

-  (checkbox checked by default)

{{-}}

#### Include (2)

![[_media/CompleteIndividualReport-TextReports-Include2-tab-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Complete Individual Report - Text Reports - Include (2) - tab default options]]

- whether to include Gramps IDs.

  - **Do not include** default
  - include

-  (checkbox checked by default)

-  (checkbox checked by default)

-  (checkbox checked by default)

-  Whether to include relationships to the filter person (Note: Slower to create report) (checkbox unchecked by default)

{{-}}

#### Sections

![[_media/CompleteIndividualReport-TextReports-Sections-tab-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Complete Individual Report - Text Reports - Sections - tab default options]]

Used if separate section is required.

- -  (Checkbox checked by default)

  -  (Checkbox checked by default)

  -  (Checkbox checked by default)

  -  (Checkbox checked by default)

  -  (Checkbox checked by default)

  -  (Checkbox checked by default)

  -  (Checkbox checked by default)

  -  (Checkbox checked by default)

  -  (Checkbox checked by default)

{{-}}

### <u>Database Summary Report</u>

![[_media/TextReports-DatabaseSummaryReport-example-overview-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Database Summary Report - Text Reports - example output overview]]

This report displays the overall statistics concerning number of individuals of each gender, various incomplete entries statistics, as well as family and media statistics.

You can choose the Database Summary Report with

The report shows a break down of the following information for the open Family tree

The numbers in the different categories are shown

- **<b>Individuals</b>**:
  - Number of individuals:
  - Males:
  - Females:
  - Individuals with unknown gender:
  - Incomplete names:
  - Individuals missing birth dates:
  - Disconnected individuals:
  - Unique surnames:
  - Individuals with media objects:

<!-- -->

- **<b>Family information</b>**:
  - Number of families:

<!-- -->

- **<b>Media Objects</b>**:
  - Number of unique media objects:
  - Total size of media objects: in MB(megabytes)

<!-- -->

- Missing Media Objects: this will show the file names of any missing media object.

The information given in this report is the same as in the [Statistics Gramplet](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Statistics) and similar to the result from the dialog.

See also [common options](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_6#Common_options) {{-}}

#### Report Options

![[_media/DatabaseSummaryReport-TextReports-ReportOptions-tab-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Database Summary Report - Text Reports - Report Options - tab default options]]

-  (checkbox checked by default)

- \- How to handle (information about) living people

  - **Included, and all data** (default)
  - Full names, but data removed
  - Given names replaced, and data removed
  - Complete names replaced, and data removed
  - Not included

- `0`(default) - Whether to restrict data on recently dead people.

- The translation to be used for the report. Language selector showing all languages supported by Gramps. Defaults to the language you are using Gramps in.

{{-}}

### <u>Descendant Report</u>

![[_media/TextReports-DescendantReport-example-overview-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Descendant Report - Text Reports - example output overview]]

This report presents the descendants of the Active Person with a brief description in indented style.

You can choose the Descendant Report with {{-}} See also [common options](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_6#Common_options) {{-}}

#### Report Options

![[_media/DescendantReport-TextReports-ReportOptions-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Descendant Report - Text Reports - Report Options - tab default options]]

The only specific option concerns the number of forward generations to consider.

- the center person for the report, defaults to the current active person.

  - button to change the center person it will opens the selector allowing you to change the center person, by selecting the check box.

- The [numbering system](wiki:Genealogical_Numbering_Systems) to be used.

  - **[Simple numbering](wiki:Genealogical_Numbering_Systems#Simple_numbering)** (default)
  - [d'Aboville](wiki:Genealogical_Numbering_Systems#d.27Aboville) numbering
  - [Henry](wiki:Genealogical_Numbering_Systems#Henry) numbering
  - [Modified Henry](wiki:Genealogical_Numbering_Systems#modified_henry) numbering
  - [de Villiers/Pama](wiki:Genealogical_Numbering_Systems#de_villiers) numbering
  - [Meurgey de Tupigny](wiki:Genealogical_Numbering_Systems#meurgey_de_tupigny) numbering

- (`10` default) The number of generations to include in the report.

-  Whether to show marriage information in the report. (checkbox unchecked by default)

-  Whether to show divorce information in the report. (checkbox unchecked by default)

-  Whether to show birth and death information in the report. (checkbox checked by default)

-  Whether to show duplicate Family Trees information in the report. (checkbox checked by default)

{{-}}

#### Report Options (2)

![[_media/DescendantReport-TextReports-ReportOptions2-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Descendant Report - Text Reports - Report Options (2) - tab default options]]

- \- Select the format to display the names. This choice in normally taken from the default setting in tab's **Display Options** section for . Or to override that setting for the report choose from:

  - **Default** - (in a new Family Tree this is normally *Surname, Given Suffix* )
  - Surname, Given Suffix
  - Given Surname Suffix
  - Given
  - Main Surnames, Given Patronymic Suffix
  - SURNAME, Given (Common)

- \- Select the format to display places. This choice in normally taken from the default setting in [Edit &gt; Display](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Display) tab for . Or to override that setting for the report choose from:

  - Default
  - Full

-  (checkbox checked by default) - Whether to include private data.

- \- How to handle (information about) living people

  - **Included, and all data** (default)
  - Full names, but data removed
  - Given names replaced, and data removed
  - Complete names replaced, and data removed
  - Not included

- `0`(default) - Whether to restrict data on recently dead people.

- The translation to be used for the report. Language selector showing all languages supported by Gramps. Defaults to the language you are using Gramps in.

- The format and language for dates, with examples

  - Default - Choose this option to use the default set in [Edit &gt; Display](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Display) tab for option.
  - **YYYY-MM-DD(ISO)(2018-03-14)** (default for report)
  - Numerical(14/3/2018)
  - Month Day, Year(March 14, 2018)
  - MON DAY, YEAR(Mar 14, 2018)
  - Day Month Year(14 March 2018)
  - DAY MON YEAR(14 Mar 2018)

{{-}}

### <u>Detailed Ancestral Report</u>

![[_media/TextReports-DetailedAncestralReport-example-overview-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Detailed Ancestral Report - Text Reports - example output overview]]

This report covers in detail the ancestors of the active person, including a range of vital data as well as marriages, following [Sosa-Stradonitz](wiki:Genealogical_Numbering_Systems#sosa-stradonitz)/[Ahnentafel](wiki:Genealogical_Numbering_Systems#ahnentafel) numbering. It shares many of its properties with the Detailed Descendant Report (see below).

You can choose the Detailed Ancestral Report with {{-}} See also [common options](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_6#Common_options) {{-}}

#### Report Options

![[_media/DetailedAncestralReport-TextReports-ReportOptions-tab-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Detailed Ancestral Report - Text Reports - Report Options - tab default options]]

The report is structured with the [Ahnentafel](wiki:Genealogical_Numbering_Systems#ahnentafel) standard numbering.

- the center person for the report, defaults to the current active person.

  - button to change the center person it will opens the selector allowing you to change the center person, by selecting the check box.

- (`1` default) The [Sosa-Stradonitz](wiki:Genealogical_Numbering_Systems#sosa-stradonitz) number of the central person.

- (`10` default) The number of generations to include in the report.

- whether to include Gramps IDs.

  - **Do not include** default
  - include

- : Whether to start a new page after each generation. (checkbox unchecked by default)

- : whether to start a new page before end notes (checkbox unchecked by default)

{{-}}

#### Report Options (2)

![[_media/DetailedAncestralReport-TextReports-ReportOptions2-tab-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Detailed Ancestral Report - Text Reports - Report Options (2) - tab default options]]

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
  - Full names, but data removed
  - Given names replaced, and data removed
  - Complete names replaced, and data removed
  - Not included

- `0`(default) - Whether to restrict data on recently dead people.

- The translation to be used for the report. Language selector showing all languages supported by Gramps. Defaults to the language you are using Gramps in.

- The format and language for dates, with examples

  - Default - Choose this option to use the default set in [Edit &gt; Display](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Display) tab for option.
  - **YYYY-MM-DD(ISO)(2018-03-14)** (default for report)
  - Numerical(14/3/2018)
  - Month Day, Year(March 14, 2018)
  - MON DAY, YEAR(Mar 14, 2018)
  - Day Month Year(14 March 2018)
  - DAY MON YEAR(14 Mar 2018)

{{-}}

#### Content

![[_media/DetailedAncestralReport-TextReports-Content-tab-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Detailed Ancestral Report - Text Reports - Content - tab default options]]

- : whether to use complete sentences or succinct language.(checkbox checked by default)

- : whether to use full dates instead of year.(checkbox checked by default)

- : whether to compute a person's age at death.(checkbox checked by default)

- : whether to omit duplicate ancestors.(checkbox checked by default)

- : whether to use the call name as the first name. (checkbox unchecked by default)

{{-}}

#### Include

![[_media/DetailedAncestralReport-TextReports-Include-tab-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Detailed Ancestral Report - Text Reports - Include - tab default options]]

- : whether to list children.(checkbox checked by default)

- : whether to list the spouses of the children.(checkbox checked by default)

- : Whether to include events. (checkbox unchecked by default)

- : Whether to include other events people participated in.(checkbox unchecked by default)

- : whether to add descendant references in child list.(checkbox checked by default)

-  (checkbox unchecked by default)

{{-}}

#### Include (2)

![[_media/DetailedAncestralReport-TextReports-Include2-tab-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Detailed Ancestral Report - Text Reports - Include (2) - tab default options]]

-  (checkbox checked by default)

-  (checkbox unchecked by default)

-  (checkbox unchecked by default)

-  (checkbox unchecked by default)

-  (checkbox unchecked by default)

-  (checkbox unchecked by default)

{{-}}

#### Missing information

![[_media/DetailedAncestralReport-TextReports-MissingInformation-tab-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Detailed Ancestral Report - Text Reports - Missing Information - tab default options]]

-   
  Whether to replace missing Places with blank spaces.(checkbox unchecked by default)

-   
  Whether to replace missing Dates with blank spaces.(checkbox unchecked by default)

{{-}}

### <u>Detailed Descendant Report</u>

![[_media/TextReports-DetailedDescendantReport-example-overview-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Detailed Descendant Report - Text Reports - example output overview]]

This report covers in detail the descendants of the active person by generation, following the genealogical tradition of textual descendant reports by generation. It aims to provide all important features expected to be found in these classic descendency formats and has received influence from various sources. The Gramps team considers as one of its objectives the viability of this report's adoption by professional genealogical institutions worldwide. As a consequence this is a highly customizable report.

The report includes a range of vital information, marriages and (optionally) notes and spouses' information. Among the numerous options are the number of forward generations to consider, whether to compute ages, the text-style between complete-sentenced and succinct, and whether to include images. The report utilizes [Henry-style numbering](wiki:Genealogical_Numbering_Systems#henry) by default, and offers [d'Aboville-style numbering](wiki:Genealogical_Numbering_Systems#d&#39;aboville) and [Register-style numbering](wiki:Genealogical_Numbering_Systems#register) as options.

You can choose the Detailed Descendant Report with {{-}} See also [common options](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_6#Common_options) {{-}}

#### Report Options

![[_media/DetailedDescendantReport-TextReports-ReportOptions-tab-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Detailed Descendant Report - Text Reports - Report Options - tab default options]]

- the center person for the report, defaults to the current active person.

  - button to change the center person it will opens the selector allowing you to change the center person, by selecting the check box.

- the [numbering system](http://en.wikipedia.org/wiki/Genealogical_numbering_systems#Register_System) to be used.

  - **Henry numbering** (default)
  - d'Aboville numbering
  - Record (Modified Register) numbering

- How people are organized in the report

  - **show people by generations** (default)
  - show people by lineage

- (`10` default) The number of generations to include in the report.

- whether to include Gramps IDs.

  - **Do not include** default
  - include

-   
  Whether to start a new page after each generation. (checkbox unchecked by default)

-   
  whether to start a new page before end notes (checkbox unchecked by default)

{{-}}

#### Report Options (2)

![[_media/DetailedDescendantReport-TextReports-ReportOptions2-tab-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Detailed Descendant Report - Text Reports - Report Options (2) - tab default options]]

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
  - Full names, but data removed
  - Given names replaced, and data removed
  - Complete names replaced, and data removed
  - Not included

- `0`(default) - Whether to restrict data on recently dead people.

- The translation to be used for the report. Language selector showing all languages supported by Gramps. Defaults to the language you are using Gramps in.

- The format and language for dates, with examples

  - Default - Choose this option to use the default set in [Edit &gt; Display](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Display) tab for option.
  - **YYYY-MM-DD(ISO)(2018-03-14)** (default for report)
  - Numerical(14/3/2018)
  - Month Day, Year(March 14, 2018)
  - MON DAY, YEAR(Mar 14, 2018)
  - Day Month Year(14 March 2018)
  - DAY MON YEAR(14 Mar 2018)

{{-}}

#### Content

![[_media/DetailedDescendantReport-TextReports-Content-tab-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Detailed Descendant Report - Text Reports - Content - tab default options]]

-   
  whether to use complete sentences or succinct language.(checkbox checked by default)

-   
  whether to use full dates instead of year.(checkbox checked by default)

-   
  whether to compute a person's age at death.(checkbox checked by default)

-   
  whether to use the call name as the first name. (checkbox unchecked by default)

{{-}}

#### Include

![[_media/DetailedDescendantReport-TextReports-Include-tab-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Detailed Descendant Report - Text Reports - Include - tab default options]]

-   
  whether to list children.(checkbox checked by default)

-   
  whether to list spouses of children.(checkbox unchecked by default)

-  (checkbox unchecked by default)

-  (checkbox unchecked by default)

-  (checkbox unchecked by default)

- : whether to include descendant references in child list.(checkbox checked by default)

-  (checkbox unchecked by default)

{{-}}

#### Include (2)

![[_media/DetailedDescendantReport-TextReports-Include2-tab-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Detailed Descendant Report - Text Reports - Include (2) - tab default options]]

-  (checkbox checked by default)

-  (checkbox unchecked by default)

-  (checkbox unchecked by default)

-  (checkbox unchecked by default)

-  (checkbox unchecked by default)

-  (checkbox unchecked by default)

-  (checkbox checked by default)

-  (checkbox unchecked by default)

{{-}}

#### Missing Information

![[_media/DetailedDescendantReport-TextReports-MissingInformation-tab-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Detailed Descendant Report - Text Reports - Missing Information - tab default options]]

-   
  Whether to replace missing Places with blank spaces.(checkbox unchecked by default)

-   
  Whether to replace missing Dates with blank spaces.(checkbox unchecked by default)

{{-}}

### <u>End of Line Report</u>

![[_media/TextReports-EndOfLineReport-example-overview-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} End of Line Report - Text Reports - example output overview]]

This provides a list of a person's last known ancestors with the pedigree line, ordered by generations.

You can choose the End of Line Report with {{-}} See also [common options](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_6#Common_options) {{-}}

#### Report Options

![[_media/EndOfLineReport-TextReports-ReportOptions-tab-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} End of Line Report - Text Reports - Report Options - tab default options]]

- the center person for the report, defaults to the current active person.

  - button to change the center person it will opens the selector allowing you to change the center person, by selecting the check box.

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
  - Full names, but data removed
  - Given names replaced, and data removed
  - Complete names replaced, and data removed
  - Not included

- `0`(default) - Whether to restrict data on recently dead people.

- The translation to be used for the report. Language selector showing all languages supported by Gramps. Defaults to the language you are using Gramps in.

- The format and language for dates, with examples

  - Default - Choose this option to use the default set in [Edit &gt; Display](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Display) tab for option.
  - **YYYY-MM-DD(ISO)(2018-03-14)** (default for report)
  - Numerical(14/3/2018)
  - Month Day, Year(March 14, 2018)
  - MON DAY, YEAR(Mar 14, 2018)
  - Day Month Year(14 March 2018)
  - DAY MON YEAR(14 Mar 2018)

{{-}}

### <u>Family Group Report</u>

![[_media/TextReports-FamilyGroupReport-example-overview-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Family Group Report - Text Reports - example output overview]]

This creates a family group report, showing information on a set of parents and their children.

You can choose the Family Group Report with {{-}} See also

- [common options](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_6#Common_options)
- [Family Sheet](wiki:Addon:Family_Sheet) addon - includes output of sources.

{{-}}

#### Report Options

![[_media/FamilyGroupReport-TextReports-ReportOptions-tab-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Family Group Report - Text Reports - Report Options - tab default options]]

- \- Select the filter to be applied to the report. Choose from:

  - **Default** - Defaults to the Active family for the current active Person.
  - Every family
  - Descendant families - of the active family
  - Ancestors families - of active family

- The center family for the filter. Defaults to the Active family for the current active Person.

  - button that opens the selector allowing you to change the filter family, by selecting the check box.

- : Create reports for all descendants of this family.(checkbox unchecked by default)

{{-}}

#### Report Options (2)

![[_media/FamilyGroupReport-TextReports-ReportOptions2-tab-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Family Group Report - Text Reports - Report Options (2) - tab default options]]

- \- Select the format to display the names. This choice in normally taken from the default setting in [Edit &gt; Data](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Display_Options) tab in the Display Options section for . Or to override that setting for the report choose from:

  - **Default** - (in a new Family Tree this is normally *Surname, Given Suffix* )
  - Surname, Given Suffix
  - Given Surname Suffix
  - Given
  - Main Surnames, Given Patronymic Suffix
  - SURNAME, Given (Common)

- Select the format to display places

  - **Default**
  - Full

-  (checkbox checked by default) - Whether to include private data.

- \- How to handle (information about) living people

  - **Included, and all data** (default)
  - Full names, but data removed
  - Given names replaced, and data removed
  - Complete names replaced, and data removed
  - Not included

- `0`(default) - Whether to restrict data on recently dead people.

- The translation to be used for the report. Language selector showing all languages supported by Gramps. Defaults to the language you are using Gramps in.

- The format and language for dates, with examples

  - Default - Choose this option to use the default set in [Edit &gt; Display](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Display) tab for option.
  - **YYYY-MM-DD(ISO)(2018-03-14)** (default for report)
  - Numerical(14/3/2018)
  - Month Day, Year(March 14, 2018)
  - MON DAY, YEAR(Mar 14, 2018)
  - Day Month Year(14 March 2018)
  - DAY MON YEAR(14 Mar 2018)

{{-}}

#### Include

![[_media/FamilyGroupReport-TextReports-Include-tab-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Family Group Report - Text Reports - Include - tab default options]]

- : Whether to include marriage information for parent. (checkbox checked by default)

- : Whether to include events for parents. (checkbox unchecked by default)

- : Whether to include addresses for parents. (checkbox unchecked by default)

- : Whether to include notes for parents. (checkbox unchecked by default)

- : Whether to include attributes. (checkbox unchecked by default)

- : Whether to include alternate name. (checkbox unchecked by default)

{{-}}

#### Include (2)

![[_media/FamilyGroupReport-TextReports-Include2-tab-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Family Group Report - Text Reports - Include (2) - tab default options]]

- whether to include Gramps IDs.

  - **Do not include** (default)
  - Include

- : Whether to include notes for families. (checkbox unchecked by default)

- : Whether to include dates for relatives. (checkbox unchecked by default)

- : Whether to include marriage information for children.(checkbox checked by default)

- : Whether to include the generation on each.(checkbox unchecked by default)

- : Whether to include fields for missing information. (checkbox checked by default)

{{-}}

### <u>Kinship Report</u>

![[_media/TextReports-KinshipReport-example-overview-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Kinship Report - Text Reports - example output overview]]

This provides the kinship of selected person according to level search (height, down generations) set by user.

You can choose the Kinship Report with {{-}} See also:

- [common options](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_6#Common_options)
- [Relationship Calculator Localization](wiki:Specification:Relationship_Calculator) - create meaningful relation descriptions in your region.

{{-}}

#### Report Options

![[_media/KinshipReport-TextReports-ReportOptions-tab-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Kinship Report - Text Reports - Report Options - tab default options]]

- the center person for the report, defaults to the current active person.

  - button to change the center person it will opens the selector allowing you to change the center person, by selecting the check box.

- (`2`default) The maximum number of descendant generations. If needed you can type a larger number.

- (`2`default) The maximum number of ancestor generations. If needed you can type a larger number.

- : Whether to include spouses. (checkbox checked by default)

- : Whether to include cousins. (checkbox checked by default)

- : Whether to include aunts/uncles/nephews/nieces. (checkbox checked by default)

{{-}}

#### Report Options (2)

![[_media/KinshipReport-TextReports-ReportOptions2-tab-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Kinship Report - Text Reports - Report Options (2) - tab default options]]

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
  - Full names, but data removed
  - Given names replaced, and data removed
  - Complete names replaced, and data removed
  - Not included

- `0`(default) - Whether to restrict data on recently dead people.

- The translation to be used for the report. Language selector showing all languages supported by Gramps. Defaults to the language you are using Gramps in.

- The format and language for dates, with examples

  - Default - Choose this option to use the default set in [Edit &gt; Display](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Display) tab for option.
  - **YYYY-MM-DD(ISO)(2018-03-14)** (default for report)
  - Numerical(14/3/2018)
  - Month Day, Year(March 14, 2018)
  - MON DAY, YEAR(Mar 14, 2018)
  - Day Month Year(14 March 2018)
  - DAY MON YEAR(14 Mar 2018)

{{-}}

### <u>Note Link Report</u>

![[_media/TextReports-NoteLinkReport-example-overview-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Note Link Report - Text Reports - example output overview]]

The allows you to check Links in Notes are valid.

This report displays and checks the status of the *internal link* consistency in Gramps notes created with the [Link Editor](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_2#Link_Editor) and only list external internet addresses created using the [Internet Address Editor](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1#Internet_Address_Editor) without checking them.

You can choose the Note Link Report with

No options are available for this report.[1](https://web.archive.org/web/20210123144928/http://gramps.1791082.n4.nabble.com/Privacy-td4671118.html#a4671131)

See also:

- [common options](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_6#Common_options)
- [Link Editor](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_2#Link_Editor)
- [Internet Address Editor](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1#Internet_Address_Editor).

{{-}}

### <u>Number of Ancestors Report</u>

![[_media/TextReports-NumberOfAncestorsReport-example-overview-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Number Of Ancestors Report - Text Reports - example output overview]]

This report displays the number of ancestors of the active person.

You can choose the Number of Ancestors Report with

The report shows the following details:

  
generation 1 has 1 individual : 100% : this is the person you started with

generation 2 has 2 individuals : 100% : both parents are known

.....

generation 8 has 35 individuals : 27.34 % **this means from the (2\*\*7) 128 possible ancestors in generation 8 - 27% are known.**

Total ancestors in generation 2 to .. is also given in numbers and percentages. {{-}} See also [common options](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_6#Common_options) {{-}}

#### Report Options

![[_media/NumberOfAncestorsReport-TextReports-ReportOptions-tab-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Number of Ancestors Report - Text Reports - Report Options - tab default options]]

- the center person for the report, defaults to the current active person.

  - button to change the center person it will opens the selector allowing you to change the center person, by selecting the check box.

<!-- -->

- \- Select the format to display the names. This choice in normally taken from the default setting in [Edit &gt; Display](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Display) tab for . Or to override that setting for the report choose from:

  - **Default** - (in a new Family Tree this is normally *Surname, Given Suffix* )
  - Surname, Given Suffix
  - Given Surname Suffix
  - Given
  - Main Surnames, Given Patronymic Suffix
  - SURNAME, Given (Common)

-  (checkbox checked by default) - Whether to include private data.

- The translation to be used for the report. Language selector showing all languages supported by Gramps. Defaults to the language you are using Gramps in.

{{-}}

### <u>Place Report</u>

![[_media/TextReports-PlaceReport-example-overview-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Place Report - Text Reports - example output overview]]

Produces a report according to places selected by the user.

It will list related person and event to the selected place.

You can choose the Place Report with

See also [common options](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_6#Common_options) {{-}}

#### Report Options

![[_media/PlaceReport-TextReports-ReportOptions-tab-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Place Report - Text Reports - Report Options - tab default options]]

- Select places using a custom filter you created earlier.

- List of places to report on.

  - button - Brings up the selector dialog so you can choose a place.

  - button - Select place in list then press this to remove place.

- \- If report is event or person centered.

  - **Event** (default)
  - Person

{{-}}

#### Report Options (2)

![[_media/PlaceReport-TextReports-ReportOptions2-tab-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Place Report - Text Reports - Report Options (2) - tab default options]]

- \- Select the format to display the names. This choice in normally taken from the default setting in [Edit &gt; Display](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Display) tab for . Or to override that setting for the report choose from:

  - **Default** - (in a new Family Tree this is normally *Surname, Given Suffix* )
  - Surname, Given Suffix
  - Given Surname Suffix
  - Given
  - Main Surnames, Given Patronymic Suffix
  - SURNAME, Given (Common)

- \- Select the format to display places. This choice in normally taken from the default setting in [Edit &gt; Display](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Display) tab for . Or to override that setting for the report choose from:

  - Default
  - Full

-  (checkbox checked by default) - Whether to include private data.

- \- How to handle (information about) living people

  - **Included, and all data** (default)
  - Full names, but data removed
  - Given names replaced, and data removed
  - Complete names replaced, and data removed
  - Not included

- `0`(default) - Whether to restrict data on recently dead people.

- The translation to be used for the report. Language selector showing all languages supported by Gramps. Defaults to the language you are using Gramps in.

- The format and language for dates, with examples

  - Default - Choose this option to use the default set in [Edit &gt; Display](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Display) tab for option.
  - **YYYY-MM-DD(ISO)(2018-03-14)** (default for report)
  - Numerical(14/3/2018)
  - Month Day, Year(March 14, 2018)
  - MON DAY, YEAR(Mar 14, 2018)
  - Day Month Year(14 March 2018)
  - DAY MON YEAR(14 Mar 2018)

{{-}}

### <u>Records Report</u>

![[_media/TextReports-RecordsReport-example-overview-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Records Report - Text Reports - example output overview]]

The Records report shows a number of interesting records (mostly age related) in your database, like oldest living person, youngest mother, etc.

You can choose the Records Report with

An identical [Records Gramplet](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Records) is also available.

See also [common options](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_6#Common_options) {{-}}

#### Report Options

![[_media/RecordsReport-TextReports-ReportOptions-tab-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Records Report - Text Reports - Report Options - tab default options]]

Selection of the records to print is possible, and a reasonable list of "positive records" is preselected (most people would regard, for example, a long marriage as a positive record, while an early divorce would rather be seen as a negative record).

- \- Select the filter to be applied to the report. Choose from:

  - **Entire Database** (Default)
  - Descendants of active person
  - Descendant families of active person
  - Ancestors of active person
  - People with common ancestor with active person
  - *Any custom made filter you have created will be listed below the other choices.*

- The center person for the filter. Defaults to the Active Person.

  - button to change the filter person it will opens the selector allowing you to change the filter person from the [Bookmarked people](wiki:Gramps_6.0_Wiki_Manual_-_Navigation#Bookmarks). Select the check box to choose from the entire Tree.

- `3` (default)

- - **Don't use call name**(default)
  - Replace first names with call name - (See Caveats)
  - underline call name in first names / add call name to first name

- default = empty field

{{-}}

#### Report Options (2)

![[_media/RecordsReport-TextReports-ReportOptions2-tab-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Records Report - Text Reports - Report Options (2) - tab default options]]

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
  - Full names, but data removed
  - Given names replaced, and data removed
  - Complete names replaced, and data removed
  - Not included

- `0`(default) - Whether to restrict data on recently dead people.

- The translation to be used for the report. Language selector showing all languages supported by Gramps. Defaults to the language you are using Gramps in.

{{-}}

#### Person 1

![[_media/RecordsReport-TextReports-Person1-tab-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Records Report - Text Reports - Person 1 - tab default options]]

-  (checkbox checked by default)

-  (checkbox checked by default)

-  (checkbox unchecked by default)

-  (checkbox checked by default)

-  (checkbox checked by default)

-  (checkbox checked by default)

-  (checkbox unchecked by default)

-  (checkbox unchecked by default)

{{-}}

#### Person 2

![[_media/RecordsReport-TextReports-Person2-tab-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Records Report - Text Reports - Person 2 - tab default options]]

-  (checkbox checked by default)

-  (checkbox checked by default)

-  (checkbox checked by default)

-  (checkbox checked by default)

-  (checkbox unchecked by default)

-  (checkbox unchecked by default)

-  (checkbox unchecked by default)

-  (checkbox unchecked by default)

{{-}}

#### Family

![[_media/RecordsReport-TextReports-Family-tab-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Records Report - Text Reports - Family - tab default options]]

-  (checkbox checked by default)

-  (checkbox checked by default)

-  (checkbox checked by default)

-  (checkbox unchecked by default)

-  (checkbox checked by default)

-  (checkbox checked by default)

-  (checkbox checked by default)

{{-}}

### <u>Tag Report</u>

![[_media/TextReports-TagReport-example-overview-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Tag Report - Text Reports - example output overview]]

This lists Tag Usage for primary objects (person, family, notes) who match the selected [Tag](wiki:Gramps_6.0_Wiki_Manual_-_Filters#Tagging).

You can choose the Tag Report with

See also [common options](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_6#Common_options) {{-}}

#### Report Options

![[_media/TagReport-TextReports-ReportOptions-tab-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Tag Report - Text Reports - Report Options - tab default options]]

-   
  Select the [Tag](wiki:Gramps_6.0_Wiki_Manual_-_Filters#Tagging) to use for the report.

- \- Select the format to display the names. This choice in normally taken from the default setting in tab for . Or to override that setting for the report choose from:

  - **Default** - (in a new Family Tree this is normally *Surname, Given Suffix* )
  - Surname, Given Suffix
  - Given Surname Suffix
  - Given
  - Main Surnames, Given Patronymic Suffix
  - SURNAME, Given (Common)

- \- Select the format to display places. This choice in normally taken from the default setting in tab for . Or to override that setting for the report choose from:

  - Default
  - Full

-  (checkbox checked by default) - Whether to include private data.

- \- How to handle (information about) living people

  - **Included, and all data** (default)
  - Full names, but data removed
  - Given names replaced, and data removed
  - Complete names replaced, and data removed
  - Not included

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

<hr>

Tilbage til [Indeks over Rapporter](wiki:Da:Gramps_6.0_brugsanvisning_-_Rapporter). {{-}}

[Category:Documentation](wiki:Category:Documentation) [Category:Plugins](wiki:Category:Plugins)
