---
title: Da:Gramps 6.0 brugsanvisning - Rapporter - del 4
categories:
- Documentation
- Plugins
- Stub
managed: false
source: wiki-scrape
wiki_revid: 129290
wiki_fetched_at: '2026-05-30T17:31:11Z'
lang: da
---

{{#vardefine:chapter\|13.1}} {{#vardefine:figure\|0}} Tilbage [Indeks over Rapporter](wiki:Da:Gramps_6.0_brugsanvisning_-_Rapporter). {{-}}

<hr>

{{-}}

![[_media/MenuOverview-Reports-GraphicalReports-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}}  Menu overview]] This section describes the different available in Gramps.

## Graphical Reports

*Graphical Reports* represent information in forms of charts and graphs. Most of the options are common among graphical reports, therefore they will be described in the [Common options](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_4#Common_options) section. Any options which are specific to a given report will be described directly in that report's entry. See also [substitution values](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_2#Substitution_Values).

The following *Graphical Reports* are available in Gramps:

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

For each report there is a screen with on the top part tabs (like **Paper Options** ...) and on the bottom part the **Document Options**. The number of tabs varies with the report.

#### Paper Options

![[_media/TextReports-PaperOptions-tab-defaults-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Paper Options" - tab for Graphical Reports]]

With the tab you can change:

- - **Letter** (default)

  - (`8.50` in. default)

  - (`11.00` in. default)

  - **Portrait** (default)

- - (`1.00` in. default)

  - (`1.00` in. default)

  - (`1.00` in. default)

  - (`1.00` in. default)

-  : whether to use metric values or not (in. or cm.). (checkbox unchecked by default) (See *Add system wide preference for metric, that can be overridden in single reports until you restart gramps* )

See also dialog which may occur if your custom page size is too large. {{-}}

#### Document Options

Options below will change slightly depending on the output format selected. ![[_media/GraphicalReports-DocumentOptions-section-SVG-document-output-settings-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Document Options - SVG document - output selected - example]]

- choose the output format:

  - *SVG document* : (Scalable Vector Graphics) for display with a web browser or editing with a suitable graphics editor.
  - *PostScript*
  - *OpenDocument Text* (if you want to edit the report with Libreoffice/Openoffice)
  - *PDF document*
  - *Print...*

- : you can indicate to open the made document your default viewer. will open the created report using whatever program is defined on your system for handling the format selected.(checkbox unchecked by default)

- default value is ''<code>/home/<username>/<Family Tree Name><Report Name>.

  <output format extension>

  </code>''. by default the filename is the same as the report type, and it will be placed in your home directory. (In Windows it defaults to one level up from "My documents".)

- (default is *default*). With the button you can add Document Styles.

- (**transparent background** default)

{{-}}

#### Select a person for the report selector

![[_media/SelectAPersonForTheReport-SelectorDialog-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Select a person for the report" - selector dialog - example]]

The selector allows you to select an already existing person for the report and once selected they will be placed in as the Centre Person.

It defaults to the current active person. {{-}} See also:

- [Select Person selector](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1#Select_Person_selector)

#### Scale and Resize options

The tree is first made on a canvas that can fit a tree of any size. From that canvas the following options can change how it is finally displayed on a page. {{-}}

##### :

This option will scale up/down the size of the report on the canvas to fit the size of the page (set in Paper Options) that you wish to print on. Currently you can:

- **Do not scale tree** (Default)
- *Scale tree to fit page width only*
- *Scale tree to fit the size of the page* (both width and height)

Without the Check box: option checked, the following occurs for the *Scale tree to fit* selections:

- *Do not scale the tree* may give you a report that spans multiple pages horizontally and/or vertically
- *Scale tree to fit page width only* may still give you a report that spans multiple pages vertically. No pages to the sides of others. Only one on top of another.
- *Scale tree to fit the size of the page* will give you a one page only report. The report will print on a page the size set in Paper Options.

##### 

This option tells how big/small to resize the page we will print on. **With this option unchecked**, the page size that is set in Paper Option. With this option checked the following happens based upon the three choices in .

This overrides/ignores what is set on Paper Options and print on a page the same dimensions that the tree uses on the canvas. So taking the three options above, in scale tree to fit, this is what will happen if you select the 'Resize Page to Fit Tree size' option:

- With *Do not scale the tree*, this option will completely ignore what is set in Paper Options and print on a page that is large enough to display the entire tree
- With *Scale tree to fit page width only*, this option will ignore Paper Height that is set in Paper Options only. The tree has already been scaled up/down to fit the page width, so it is set. Only the page Height is set upon the height of the tree we are printing.
- With *Scale tree to fit the size of the page*, the tree has already been scaled to the size of the page. But as noted above, either the width or height will (more than likely) have a gap (empty white space) in it. The will narrow down this gap on the page to remove that gap.

##### inter-box Y scale factor

  
Make the inter-box Y bigger or smaller

##### box shadow scale factor

  
Make the box shadow bigger or smaller

##### Know what you want to print on

Scaling a tree is an advanced function. The → sets the size of text that you can print. Scaling down is not very desirable as the text becomes more difficult to read. Scaling up is better but may have the some issues. So here are some pointers to make nice printed documents.

First thing first. What paper sizes can you print on? Ask around and see what page sizes you can print on easily. Just knowing what paper sizes you can print on helps a lot. At Kinkos (in the U.S.A) there is a 3 foot wide printer with paper that is on a roll (any length). So we could use 'Scale report to fit page width only' and 'One page report' for this.

It is also noteworthy to first make your report using s *Do not scale the report* option and to know what the reports full dimensions (width and height) are. This will help you know how to better put this report on the pages you can print on. Here are some other quick things to take into account.

- A report that is very high and not too wide may print better with only the *Scale report to fit page width only* option.
- With the reports normal width, which will print better? Landscape or Portrait?
- Since every boxes width is set by the widest box, can you use the Descendant reports → Replace option to abbreviate or remove very long parts that are not needed?
- The size of the title. If there is room, you may want to make the title larger. And if it is too large, it will set the width of the report.

{{-}}

<hr>

### <u>Ancestor Tree</u>

![[_media/GraphicalReports-AncestorTree-example-landscape-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Ancestor Tree - Graphical Reports - example output overview]]

The report generates the chart of people who are ancestors of the Active Person.

From the menu choose {{-}} See also [common options](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_4#Common_options) {{-}}

#### Tree Options

![[_media/AncestorTree-GraphicalReports-TreeOptions-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Ancestor Tree - Graphical Reports - Tree Options - tab default options]]

- The center person for the tree. Defaults to the Active Person.

  - button. - Change the Centre person.

-  Whether to only display the centre person or all of his/her siblings too (checkbox unchecked by default)

- (`10` default) The number of generations to include in the tree

- The number of generations of empty boxes that will be displayed ( when the tree is not completely full.)

  - **No generations of empty boxes for unknown ancestors** (default)
  - *\# Generation(s) of empty boxes for unknown ancestors* (display up to 8 generations of empty boxes)

-  Whether to remove any extra blank spaces set aside for people that are unknown (checkbox checked by default)

-  Display index of each person (checkbox unchecked by default)

- (`1` default) The start index

{{-}}

#### Report Options

![[_media/AncestorTree-GraphicalReports-ReportOptions-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Ancestor Tree - Graphical Reports - Report Options - tab default options]]

This tab gives you the option to include other items on the report.

- Choose a title for the report.

  - **Do not print a title** (default)
  - *Include Report Title*

-  (checkbox unchecked by default)

-  (checkbox unchecked by default)

- will make the tree larger or smaller to fit the page as desired. The options are:

  - **Do not Scale the tree** (default)
  - *Scale tree to fit page width only*
  - *Scale tree to fit the size of the page*

-  (checkbox unchecked by default) will make the page larger or smaller to fit the tree.

-  (checkbox checked by default)

If both and are selected, the options happen in that order; scale the tree first, then the page.

The two options and are better described in [common options](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_4#Common_options) with tips for making nicer reports. {{-}}

#### Report Options (2)

![[_media/AncestorTree-GraphicalReports-ReportOptions2-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Ancestor Tree - Graphical Reports - Report Options (2) - tab default options]]

- Select the format to display the names. Choose from

  - **Surname, Given Suffix** (default)
  - *Given Surname Suffix*
  - *Given*
  - *Main Surnames, Given Patronymic Suffix*
  - *SURNAME, Given (Common)*

- Select to include or not living persons in the report. Choose from

  - **Include, and all data** (default)
  - *Full names, but data removed*
  - *Given names replaced, and data removed*
  - *Complete names replaced, and data removed*
  - *Not included*

- Select the number of years since death to consider persons for the report. Allows for the inclusion or exclusion of recently-dead persons in the report. Default value is 0 years.

  -  (checkbox checked by default)

- The translation to be used for the report.

  - Language selector

- Select the format to display dates. Choose from

  - **YYYY-MM-DD (ISO)(2018-04-08)** (default)
  - Numerical (8/4/2018)
  - Month Day, Year (April 8, 2018)
  - Mon Day, Year (Apr 8, 2018)
  - Day Month Year (8 April 2018)
  - Day Mon Year (8 Apr 2018)

{{-}}

#### Display

![[_media/AncestorTree-GraphicalReports-Display-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Ancestor Tree - Graphical Reports - Display - tab default options]]

This tab allows you to determine the to be used for the report. All fathers, grandfathers, etc. will use this format.

The to be used for all mothers, grandmothers, etc. will use this format.

The `{}` around the death information line states that the text '`d.`' will display ONLY when there is death information. See [Substitution Values](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_2) for more information, including how to include places and attributes, and format names and dates and places.

allows you to specify if the center person uses the father display format or the mother display format found on the Display tab.

specifies to display an extra box between a father and mother that contains marriage information. (see [Substitution Values](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_2)) specifies what will print in this box.

{{-}}

#### Advanced

![[_media/AncestorTree-GraphicalReports-Advanced-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Ancestor Tree - Graphical Reports - Advanced - tab default options]]

- This allows you to put in pairs of strings separated by '`/`'(foward slash) that specify text you want to replace with other text. For example, `United States of America/USA` replaces the United States of America with USA. Each column width is defined by the widest box in the report. So if one box happens to be a lot wider than the rest, a lot of space will be wasted. The replace string option allows you to remove, or abbreviate, parts of the string that is not needed, or that can be cut down, so the amount of space wasted is minimal.

  -  You may check the Include a note box to add a note (checkbox unchecked by default).

- specifies text the note will contain. Adding the substitution value “`$T`” within the note will display the day that the report was made. Regular date formatting (see [Substitution Values](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_2)) applies.

- Specify where on the page to place the note. Currently a note will be attached to a corner. If a person box writes over it, the note box will not move. Select another Note location option to position the note if this happens.

  - **Top Left** (default)
  - *Bottom Left*
  - *Bottom Right*

These following two options are better described in [Size options](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_4#Scale_and_Resize_options) with tips for making nicer reports.

- \- Make the inter-box bigger or smaller (default is `1.00` in.).

- \- Make the box shadow bigger or smaller (default is `1.00` in.).

{{-}}

### <u>Calendar</u>

![[_media/GraphicalReports-Calendar-example-landscape-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Calendar - Graphical Reports - example output overview]]

This report produces a calendar with birthdays and anniversaries on a page by month.

You can choose the Calendar report with

You can print the same information but in text format by using the [Birthday and Anniversary Report](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_6#Birthday_and_Anniversary_Report).

See [Calendar tools holidays](wiki:Calendar_tools_holidays) for an explanation of how to add or change the holidays appearing on the output of this calendar. {{-}} See also [common options](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_4#Common_options) {{-}}

#### Report Options

![[_media/Calendar-GraphicalReports-ReportOptions-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Calendar - Graphical Reports - Report Options - tab default options]]

- choose between

  - **Entire Database** (Default)
  - *Descendants of <active person>*
  - *Descendant families of <active person>*
  - *Ancestors of <active person>*
  - *People with common ancestor with <active person>*

- The center person for the report usually the active person unless you use the :

  - button to use selector dialog.

- (`My Calendar` default) First line of text at bottom of calendar.

- (`Produced with Gramps` default) Second line of text at bottom of calendar.

- ([`http://gramps-project.org/`](http://gramps-project.org/) default) Third line of text at bottom of calendar.

{{-}}

#### Report Options (2)

![[_media/Calendar-GraphicalReports-ReportOptions2-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Calendar - Graphical Reports - Report Options (2) - tab default options]]

- Select the format to display the names. Choose from

  - **Surname, Given Suffix** (default)
  - *Given Surname Suffix*
  - *Given*
  - *Main Surnames, Given Patronymic Suffix*
  - *SURNAME, Given (Common)*

-  (checkbox checked by default)

-  (checkbox checked by default)

- The translation to be used for the report. Shows the Language selector

{{-}}

#### Content

![[_media/Calendar-GraphicalReports-Content-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Calendar - Graphical Reports - Content - tab default options]]

- fill in the year. Defaults to current Year.

- Select the country to see associated holidays. Defaults to none. See example: [Calendar tools holidays](wiki:Calendar_tools_holidays)

- (Default: **Monday**) Select the first day of the week for the report.

- Select married women's displayed surname.

  - **Wives use their own surname** (Default)
  - *Wives use husband's surname (from first family listed)*
  - *Wives use husband's surname (from last family listed)*

-  : include or not birthdays in the calendar (checkbox checked by default)

-  : include or not anniversaries in the calendar (checkbox checked by default)

-  : include or not death anniversaries in the calendar (checkbox unchecked by default)

{{-}}

### <u>Descendant Tree</u>

![[_media/GraphicalReports-DescendantTree-example-portrait-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Descendant Tree - Graphical Reports - example output overview]]

The report generates a chart of people who are descendants of the Active Person. Alternatively it may generate a chart of descendants of the parents of the Active Person.

You can choose the report with {{-}} See also [common options](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_4#Common_options) {{-}}

#### Tree Options

![[_media/DescendantTree-GraphicalReports-TreeOptions-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Descendant Tree - Graphical Reports - Tree Options - tab default options]]

- The main person for the report. Defaults to the Active Person.

  - button. - Change the main person.

- (`10` default ). The number of generations to include in the tree (including the main person). Note: The chart will include one more generation if is selected.

- specifies how deep to display spouses. (`1` default )

-  Will show the parents, brother and sisters of the selected person. (checkbox unchecked by default)

-  Whether to move people up, where possible, resulting in a smaller tree (checkbox unchecked by default)

-  Whether to bold those people that are direct (not step or half) descendants. (checkbox checked by default)

-  Whether to indent the spouses in the tree. (checkbox checked by default)

{{-}}

#### Report Options

![[_media/DescendantTree-GraphicalReports-ReportOptions-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Descendant Tree - Graphical Reports - Report Options - tab default options]]

- Choose a title for the report. Options are:

  - **Do not include a title** (default)
  - *Descendant Chart for \[selected person(s)\]* (Note: If is ticked on the tab, both parents of the selected person are shown. Only two people will be listed in the title. If is two or more, descendants of "spouses of spouses" are included on the chart, but are not listed in the title.)

-  Whether to make a border around the report. (checkbox unchecked by default)

-  Whether to include page numbers on each page. (checkbox unchecked by default)

- Whether to scale the tree (make the tree larger or smaller) to fit a specific paper size. The options are:

  - **Do not scale the tree** (Default)
  - *Scale tree to fit page width only*
  - *Scale tree to fit the size of the page*

-  (unchecked by default) Resize page to fit tree will make the page larger or smaller to fit the tree. If selected with the , the options happen in that order; scale the tree first, then the page. There is a combined effect with each option:

1.  With "Do not scale the tree", both the page width and height is resized to fit the tree.
2.  With "Scale tree to fit page width only", the page height is resized to fit the tree height.
3.  With "Scale tree to fit the size of the page", the page is resized to remove any gap in both height and width.

-  Whether to include pages that are blank. (checkbox unchecked by default)

The and options are better described in [common options](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_4#Common_options) with tips for making nicer reports. {{-}}

#### Report Options (2)

![[_media/DescendantTree-GraphicalReports-ReportOptions2-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Descendant Tree - Graphical Reports - Report Options (2) - tab default options]]

- Select the format to display names. Choose from

  - **Surname, Given Suffix**(default)
  - *Given Surname Suffix*
  - *Given*
  - *Main Surnames, Given Patronymic Suffix*
  - *SURNAME, Given (Common)*

-  Whether to include private date (checkbox checked by default)

- How to handle living people. Choose from:

  - **Include, and all data** (default)
  - *Full names, but data removed*
  - *Given names replaced, and data removed*
  - *Complete names replaced, and data removed*
  - *Not included*

- Whether to restrict data on recently-dead people. Select the number of years since death to consider persons for the report. Allows for the inclusion or exclusion of recently-dead persons in the report. (Default value is `0` years.)

- The translation to be used for the report.

-   
  The format and language for dates, with examples. Choose from:

  - **YYYY-MM-DD (ISO)(2018-04-08)** (default)
  - *Numerical (8/4/2018)*
  - *Month Day, Year (April 8, 2018)*
  - *Mon Day, Year (Apr 8, 2018)*
  - *Day Month Year (8 April 2018)*
  - *Day Mon Year (8 Apr 2018)*

{{-}}

#### Display

![[_media/DescendantTree-GraphicalReports-Display-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Descendant Tree - Graphical Reports - Display - tab default options]]

- sets the display for all descendants in the tree. The default is:

<!-- -->

    $n
    b. $b
    -{d. $d}

which displays the name, birth date and death date on consecutive lines in the formats set on the Display tab in Gramps preferences. The {} on the third line states that the text 'd. ' will display ONLY when \$d has a value, i.e. there is something in the death date field of the database for this person. See [Substitution Values](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_2) for more information, including how to include places and attributes, and select different formats for names and dates and places.

The check box causes the names and other information about direct descendants to be in the bold font selected in the style editor.

- specifies what is displayed for each spouse. The default is the same as for descendants. If you do not wish to have a separate box for marriage information, it can be displayed in the spouse box, for example by adding a line with

<!-- -->

    m. $m 

Which displays the date of the marriage.

will indent the spouse and marriage boxes from the descendant boxes. In the Family Descendant Chart, it does not affect the starting family or the parents of the starting family, but it does affect any other spouses of those three couples.

-  (checkbox checked by default) will display a separate box on the tree for each marriage. The display format is set in . The default is

<!-- -->

    m. $m

which displays the date of the marriage. If this box is not ticked, marriage information will not be displayed unless you specify it in the spousal display format as described above.

{{-}}

#### Advanced

![[_media/DescendantTree-GraphicalReports-Advanced-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Descendant Tree - Graphical Reports - Advanced - tab default options]]

- This allows you to put in pairs of strings separated by '`/`'(foward slash) that specify text you want to replace with other text. For example, `United States of America/USA` replaces the United States of America with USA. Each column width is defined by the widest box in the report. So if one box happens to be a lot wider than the rest, a lot of space will be wasted. The replace string option allows you to remove, or abbreviate, parts of the string that is not needed, or that can be cut down, so the amount of space wasted is minimal.

  -  You may check the Include a note box to add a note (checkbox unchecked by default).

- specifies text the note will contain. Adding the substitution value “`$T`” within the note will display the day that the report was made. Regular date formatting (see [Substitution Values](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_2)) applies.

- Specify where on the page to place the note. Currently a note will be attached to a corner. If a person box writes over it, the note box will not move. Select another Note location option to position the note if this happens.

  - **Top Left** (default)
  - *Bottom Left*
  - *Bottom Right*

These following two options are better described in [Size options](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_4#Scale_and_Resize_options) with tips for making nicer reports.

- \- Make the inter-box bigger or smaller (default is `1.00` in.).

- \- Make the box shadow bigger or smaller (default is `1.00` in.).

{{-}}

#### Examples

![[_media/Descendant_tree_example1.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Descendant Tree Report, Example 1. Allan Davies had three spouses.]]

![[_media/Descendant_tree_example2.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Descendant Tree Report, Example 2.]]

{{-}} The example below is based on the same family as the first example and shows the result of starting with "Child 2 Davies" and ticking this box.

{{-}} Example 1 was obtained by selecting Allan Davies as the starting person and then running the report without this box ticked, with all other options the same except . The differences between the two examples are:

- The format of the first generation is changed. Because the parents of the starting person must be adjacent, spouses in the first generation may be shown out of order.
- For the purpose of the setting, both parents are considered direct descendants, rather than spouses. (Although the mother uses the on the Display tab.)

This means that other spouses (if any) of both of them will be shown to the number of levels specified by . In example 2, Mike Morris is shown even though is set to 1.

- The title of the report (if selected on the Include tab) is changed to include both parents of the starting person. Only two people are shown in the title. In example 2, Mike Morris is not listed in the title even though his descendants are shown.

The number of generations to show on the report (including the starting person). If is selected, the chart will include one more generation. (Example 1 was run with =3, Example 2 with =2.)

specifies how deep to display spouses.

For the example:

- Abe is a direct descendant
  - Abe has/had married Barbra and had two children
  - Abe also married Bridget and had one child
    - Bridget has/had married Carl.
      - Carl and Denise had a child.

Given the above example, this is what will be displayed for the first three options.

- 0 means that only direct descendants will be shown. Nothing on the Secondary tab will be shown (Spousal information or Marriage information). For the example above, only Abe will be shown with three children directly under him
- 1 means that only spouses of the direct descendants will be shown. For the example above, Abe will be shown with two pieces of marriage information. Under the first will be two children and one child under the second.
- 2 means that spouses of spouses are shown. Same as 1 but Bridget will also show her other marriage. If they had any children, they would be shown too.
- 3 means that everyone in the example above will be displayed.

Any option above 1 is very hard to read on the report without the option on the Display tab.

And last but not least is the option which tries to move everyone up as far as they can go (compress) and still have a readable report. If is ticked, does not have any affect on the first generation. {{-}}

#### Examples 1 or 2

....

(`10` default ). The number of generations to show on the chart (including the starting person). If is selected, the chart will include one more generation. (Example 1 was run with =3, Example 2 with =2.)

specifies how deep to display spouses.

will draw a descendancy chart from the parents of the starting person, if they are in the database. The [Example](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_4#Examples) is based on the same family as the first example and shows the result of starting with "Child 2 Davies" and ticking this box.

{{-}} Example 1 was obtained by selecting Allan Davies as the starting person and then running the report without this box ticked, with all other options the same except . The differences between the two examples are:

- The format of the first generation is changed. Because the parents of the starting person must be adjacent, spouses in the first generation may be shown out of order.
- For the purpose of the setting, both parents are considered direct descendants, rather than spouses. (Although the mother uses the on the Display tab.)

This means that other spouses (if any) of both of them will be shown to the number of levels specified by . In example 2, Mike Morris is shown even though is set to 1.

- The title of the report (if selected on the Include tab) is changed to include both parents of the starting person. Only two people are shown in the title. In example 2, Mike Morris is not listed in the title even though his descendants are shown.

For the example:

- Abe is a direct descendant
  - Abe has/had married Barbra and had two children
  - Abe also married Bridget and had one child
    - Bridget has/had married Carl.
      - Carl and Denise had a child.

Given the above example, this is what will be displayed for the first three options.

- 0 means that only direct descendants will be shown. Nothing on the Secondary tab will be shown (Spousal information or Marriage information). For the example above, only Abe will be shown with three children directly under him
- 1 means that only spouses of the direct descendants will be shown. For the example above, Abe will be shown with two pieces of marriage information. Under the first will be two children and one child under the second.
- 2 means that spouses of spouses are shown. Same as 1 but Bridget will also show her other marriage. If they had any children, they would be shown too.
- 3 means that everyone in the example above will be displayed.

Any option above 1 is very hard to read on the report without the option on the Display tab.

And last but not least is the option which tries to move everyone up as far as they can go (compress) and still have a readable report. If is ticked, does not have any affect on the first generation. {{-}}

### <u>Family Descendant Tree</u>

![[_media/GraphicalReports-FamilyDescendantTree-example-portrait-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Family Descendant Tree - Graphical Reports - example output overview]]

The report generates a chart of people who are descendants of the Active Family.

You can choose the Family Descendant Tree report with {{-}} See also [common options](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_4#Common_options) {{-}}

#### Tree Options

![[_media/FamilyDescendantTree-GraphicalReports-TreeOptions-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Family Descendant Tree - Graphical Reports - Tree Options - tab default options]]

- The main person for the report. Defaults to the Active Person.

  - button. - Change the main person.

- (`10` default ). The number of generations to include in the tree (including the main person). Note: The chart will include one more generation if is selected.

- specifies how deep to display spouses. (`1` default )

-  Will show the parents, brother and sisters of the selected person. (checkbox unchecked by default)

-  Whether to move people up, where possible, resulting in a smaller tree (checkbox unchecked by default)

-  Whether to bold those people that are direct (not step or half) descendants. (checkbox checked by default)

-  Whether to indent the spouses in the tree. (checkbox checked by default)

{{-}}

If the is checked, the report shows both parents of the starting father and mother (if they are in the database), and all descendants of both sets of parents for the selected number of generations. The total number of generations in the chart is therefore 1 more than the number selected in the generations box. (The example chart above was made with generations=2.)

The starting father and mother have to be in the center of the chart.

They will therefore not be shown in birth order with their siblings - instead they will be shown as the last and first child of their parents respectively. This is shown in the [Examples](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_4#Examples) chart, where the children in both families have been named Child 1,2,3 in their birth order. Furthermore, if the starting father or mother have other spouses they will be shown twice. This also applies to the parents of the starting father or mother.

If this box is not ticked, the report is the same as the descendant tree report, except that the number of generations is increased by one, the format of the first generation is different, and you get extra options for the chart title. {{-}}

#### Report Options

![[_media/FamilyDescendantTree-GraphicalReports-ReportOptions-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Family Descendant Tree - Graphical Reports - Report Options - tab default options]]

- Choose a title for the report. Options are:

  - **Do not include a title** (default)
  - *Descendant Chart for \[selected person(s)\]* (Note: If is ticked on the tab, both parents of the selected person are shown. Only two people will be listed in the title. If is two or more, descendants of "spouses of spouses" are included on the chart, but are not listed in the title.)

-  Whether to make a border around the report. (checkbox unchecked by default)

-  Whether to include page numbers on each page. (checkbox unchecked by default)

- Whether to scale the tree (make the tree larger or smaller) to fit a specific paper size. The options are:

  - **Do not scale the tree** (Default)
  - *Scale tree to fit page width only*
  - *Scale tree to fit the size of the page*

-  (unchecked by default) Resize page to fit tree will make the page larger or smaller to fit the tree. If selected with the , the options happen in that order; scale the tree first, then the page. There is a combined effect with each option:

1.  With "Do not scale the tree", both the page width and height is resized to fit the tree.
2.  With "Scale tree to fit page width only", the page height is resized to fit the tree height.
3.  With "Scale tree to fit the size of the page", the page is resized to remove any gap in both height and width.

-  Whether to include pages that are blank. (checkbox unchecked by default)

The and options are better described in [common options](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_4#Common_options) with tips for making nicer reports. {{-}}

#### Report Options (2)

![[_media/FamilyDescendantTree-GraphicalReports-ReportOptions2-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Family Descendant Tree - Graphical Reports - Report Options (2) - tab default options]]

- Select the format to display names. Choose from

  - **Surname, Given Suffix**(default)
  - *Given Surname Suffix*
  - *Given*
  - *Main Surnames, Given Patronymic Suffix*
  - *SURNAME, Given (Common)*

-  Whether to include private date (checkbox checked by default)

- How to handle living people. Choose from:

  - **Include, and all data** (default)
  - *Full names, but data removed*
  - *Given names replaced, and data removed*
  - *Complete names replaced, and data removed*
  - *Not included*

- Whether to restrict data on recently-dead people. Select the number of years since death to consider persons for the report. Allows for the inclusion or exclusion of recently-dead persons in the report. (Default value is `0` years.)

- The translation to be used for the report.

-   
  The format and language for dates, with examples. Choose from:

  - **YYYY-MM-DD (ISO)(2018-04-08)** (default)
  - *Numerical (8/4/2018)*
  - *Month Day, Year (April 8, 2018)*
  - *Mon Day, Year (Apr 8, 2018)*
  - *Day Month Year (8 April 2018)*
  - *Day Mon Year (8 Apr 2018)*

{{-}}

#### Display

![[_media/FamilyDescendantTree-GraphicalReports-Display-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Family Descendant Tree - Graphical Reports - Display - tab default options]]

sets the display for all descendants in the tree. The default is:

    $n
    b. $b
    {d. $d}

which displays the name, birth date and death date on consecutive lines in the formats set on the Display tab in Gramps preferences. The {} on the third line states that the text 'd. ' will display ONLY when \$d has a value, i.e. there is something in the death date field of the database for this person. See [Substitution Values](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_2) for more information, including how to include places and attributes, and select different formats for names and dates and places.

specifies what is displayed for each spouse. The default is the same as for descendants. If you do not wish to have a separate box for marriage information, it can be displayed in the spouse box, for example by adding a line with

    m. $m 

Which displays the date of the marriage.

will indent the spouse and marriage boxes from the descendant boxes. In the Family Descendant Chart, it does not affect the starting family or the parents of the starting family, but it does affect any other spouses of those three couples.

will display a separate box on the tree for each marriage. The display format is set in . The default is

    m. $m

which displays the date of the marriage. If this box is not ticked, marriage information will not be displayed unless you specify it in the spousal display format as described above.

{{-}}

#### Advanced

![[_media/FamilyDescendantTree-GraphicalReports-Advanced-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Family Descendant Tree - Graphical Reports - Advanced - tab default options]]

- This allows you to put in pairs of strings separated by '`/`'(foward slash) that specify text you want to replace with other text. For example, `United States of America/USA` replaces the United States of America with USA. Each column width is defined by the widest box in the report. So if one box happens to be a lot wider than the rest, a lot of space will be wasted. The replace string option allows you to remove, or abbreviate, parts of the string that is not needed, or that can be cut down, so the amount of space wasted is minimal.

  -  You may check the Include a note box to add a note (checkbox unchecked by default).

- specifies text the note will contain. Adding the substitution value “`$T`” within the note will display the day that the report was made. Regular date formatting (see [Substitution Values](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_2)) applies.

- Specify where on the page to place the note. Currently a note will be attached to a corner. If a person box writes over it, the note box will not move. Select another Note location option to position the note if this happens.

  - **Top Left** (default)
  - *Bottom Left*
  - *Bottom Right*

These following two options are better described in [Size options](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_4#Scale_and_Resize_options) with tips for making nicer reports.

- \- Make the inter-box bigger or smaller (default is `1.00` in.).

- \- Make the box shadow bigger or smaller (default is `1.00` in.).

{{-}}

### <u>Fan Chart</u>

![[_media/GraphicalReports-FanChart-example-landscape-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Fan Chart - Graphical Reports - example output overview]]

The compactly shows paternal and maternal ancestors. The report produces a chart representing family relationships in a tree structure resembling a fan (half circle) and optionally as a quarter or full circle, with the Active person in the inner circle (center), parents are in the second concentric circle divided in two (each side is one parent), the third circle is divided in four representing grandparents and so on, for a maximum of eleven generations.

This chart is also know as a *Pedigree fan chart*.

You can choose the Fan Chart report with {{-}} See also [common options](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_4#Common_options) {{-}}

#### Report Options

![[_media/FanChart-GraphicalReports-ReportOptions-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Fan Chart - Graphical Reports - Report Options - tab default options]]

- The center person for the report. Defaults to the Active Person.

  - button. - Change the center person.

- (`5` default ) The number of generations to include in the report. (To a maximum of `11` generations)

- The form of the graph.

  - *full circle*
  - **half circle** (Default)
  - *overhang* (half circle with overhang)
  - *quarter circle*

- choose from:

  - *white*
  - **generation dependent** (Default)

- choose from:

  - **upright** (Default)
  - *roundabout*

- : Draw the background although there is no information (checkbox checked by default)

-  : You can customize font and color for each generation in the style editor (checkbox checked by default)

-  : Flip names for generations 2,3, and 4 i.e. those found in circles (checkbox checked by default)

-  : to make more room for the chart (checkbox unchecked by default)

{{-}}

#### Report Options (2)

![[_media/FanChart-GraphicalReports-ReportOptions2-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Fan Chart - Graphical Reports - Report Options (2) - tab default options]]

-  (checkbox checked by default)

-   
  Select to include or not living persons in the report. Choose from

  - **Include, and all data** (default)
  - *Full names, but data removed*
  - *Given names replaced, and data removed*
  - *Complete names replaced, and data removed*
  - *Not included*

-   
  Select the number of years since death to consider persons for the report. Allows for the inclusion or exclusion of recently-dead persons in the report. Default value is 0 years.

-   
  The translation to be used for the report.

  - Language selector

{{-}}

### <u>Statistics Charts</u>

The report displays statistical data about your Family Tree in the form of three charts for *Birth Month*, *Number of children* and *Gender* statistics.

You can choose the Statistics Charts report with

Specific options include filter, sorting methods, and additional birth- and gender-based limit for inclusion into statistics. You can also set the minimum number of items to qualify for the bar chart, so that the charts with fewer items will generate a pie chart instead. The , and tabs allows you to select which additional information to include on each individual chart in your report.

<div>

- ![[_media/GraphicalReports-StatisticsCharts-Chart1-example-portrait-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Chart 1 (Birth Month)]]

- ![[_media/GraphicalReports-StatisticsCharts-Chart3-example-portrait-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Chart 2 (Number of children) -]]

- ![[_media/GraphicalReports-StatisticsCharts-Chart3-Gender-example-portrait-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Chart 3 (Gender)]]

</div>

{{-}} See also [common options](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_4#Common_options) {{-}}

#### Report Options

![[_media/StatisticsCharts-GraphicalReports-ReportOptions-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Statistics Charts - Graphical Reports - Report Options - tab default options]]

- choose between

  - **Entire Database** (Default)
  - *Descendants of active person*
  - *Descendant families of active person*
  - *Ancestors of active person*
  - *People with common ancestor with active person*

- The center person for the filter. Defaults to the Active Person.

  - button. - Change the Center person.

- Select how the statistical data is sorted:

  - **Item count** (default)
  - *Item name*

-  (checkbox unchecked by default)

- (`1700` default) Birth year from which to include people: fill in a year to start from

- (`Current year` default) Birth year until which to include people: fill in a year

-  (checkbox unchecked by default)

- Select which genders are included into statistics.

  - **All** (Default)
  - Men
  - Women
  - Other

- (`8` default) With fewer items pie chart and legend will be used instead of a bar chart.

-  Whether to include counts of the number of people who lack the given information. (checkbox unchecked by default)

{{-}}

#### Report Options (2)

![[_media/StatisticsCharts-GraphicalReports-ReportOptions2-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Statistics Charts - Graphical Reports - Report Options (2) - tab default options]]

- Select the format to display the names. Choose from

  - **Surname, Given Suffix** (default)

  - *Given Surname Suffix*

  - *Given*

  - *Main Surnames, Given Patronymic Suffix*

  - *SURNAME, Given (Common)*

  -  (checkbox checked by default)

- Select to include or not living persons in the report. Choose from

  - **Include, and all data** (default)
  - *Full names, but data removed*
  - *Given names replaced, and data removed*
  - *Complete names replaced, and data removed*
  - *Not included*

- Select the number of years since death to consider persons for the report. Allows for the inclusion or exclusion of recently-dead persons in the report. Default value is 0 years.

- The translation to be used for the report.

  - Language selector

{{-}}

#### Charts 1

![[_media/StatisticsCharts-GraphicalReports-Charts1-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Statistics Charts - Graphical Reports - Charts 1 - tab default options]]

Displays statistics by default and you can include any of the following the indicated data on a chart:

-  (checkbox unchecked by default)

-  (checkbox unchecked by default)

-  (checkbox unchecked by default)

-  (checkbox unchecked by default)

-  (checkbox unchecked by default)

-  (checkbox checked by default)

{{-}}

#### Charts 2

![[_media/StatisticsCharts-GraphicalReports-Charts2-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Statistics Charts - Graphical Reports - Charts 2 - tab default options]]

Displays statistics by default and you can include any of the following the indicated data on a chart:

-  (checkbox unchecked by default)

-  (checkbox unchecked by default)

-  (checkbox unchecked by default)

-  (checkbox unchecked by default)

-  (checkbox unchecked by default)

-  (checkbox unchecked by default)

{{-}}

#### Charts 3

![[_media/StatisticsCharts-GraphicalReports-Charts3-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Statistics Charts - Graphical Reports - Charts 3 - tab default options]]

Displays statistics by default and you can include any of the following the indicated data on a chart:

-  (checkbox unchecked by default)

-  (checkbox checked by default)

-  (checkbox unchecked by default)

-  (checkbox checked by default)

-  (checkbox unchecked by default)

-  (checkbox unchecked by default)

-  (checkbox unchecked by default)

{{-}}

### <u>Timeline Chart</u>

![[_media/GraphicalReports-TimelineChart-example-landscape-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Timeline Chart - Graphical Reports - example output overview]]

The report outputs the list of people with their lifetimes represented by intervals on a common chronological scale.

You can choose the report with {{-}} See also [common options](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_4#Common_options) {{-}}

#### Report Options

![[_media/TimelineChart-GraphicalReports-ReportOptions-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Timeline Chart - Graphical Reports - Report Options - tab default options]]

- choose between

  - **Entire Database** (Default)
  - *Descendants of active person*
  - *Descendant families of active person*
  - *Ancestors of active person*
  - *People with common ancestor with active person*

- The center person for the filter. Defaults to the Active Person.

  - button. - Change the Center person.

- Sorting method to use.

  - **Birth Date** (Default)
  - *Name*

{{-}}

#### Report Options (2)

![[_media/TimelineChart-GraphicalReports-ReportOptions2-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Timeline Chart - Graphical Reports - Report Options (2) - tab default options]]

- Select the format to display the names. Choose from

  - **Surname, Given Suffix** (default)

  - *Given Surname Suffix*

  - *Given*

  - *Main Surnames, Given Patronymic Suffix*

  - *SURNAME, Given (Common)*

  -  (checkbox checked by default)

-   
  Select to include or not living persons in the report. Choose from

  - **Include, and all data** (default)
  - *Full names, but data removed*
  - *Given names replaced, and data removed*
  - *Complete names replaced, and data removed*
  - *Not included*

- Select the number of years since death to consider persons for the report. Allows for the inclusion or exclusion of recently-dead persons in the report. Default value is 0 years.

- The translation to be used for the report.

  - Language selector

{{-}}

<hr>

Tilbage til [Indeks over Rapporter](wiki:Da:Gramps_6.0_brugsanvisning_-_Rapporter). {{-}}

[Category:Documentation](wiki:Category:Documentation) [Category:Plugins](wiki:Category:Plugins)
