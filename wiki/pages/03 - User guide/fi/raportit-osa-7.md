---
title: Fi:Gramps 6.0 Wiki-käyttöohje - Raportit Osa 7
categories:
- Fi:Dokumentaatio
- Plugins
- Stub
managed: false
source: wiki-scrape
wiki_revid: 117785
wiki_fetched_at: '2026-05-30T18:28:26Z'
lang: fi
---

{{#vardefine:chapter\|11.7}} {{#vardefine:figure\|0}} Takaisin [Raportit](wiki:Fi:Gramps_6.0_Wiki-käyttöohje_-_Raportit) -osion alkuun.

<hr>

{{-}} ![[_media/MenuOverview-Reports-WebPages-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}}  Menu overview]] This section describes the reports, Narrated Web Site and Web Calendar as part of the different reports available in Gramps.

## Web Pages

### <u>Narrated Web Site</u>

![[_media/NarratedWebSite-WebPages-Individuals-index-page-example-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Narrated Web Site - Web Pages - Individuals page - default HTML output - example]]

The Narrated Web Site report generates a web site (that is, a set of linked web pages), for a set of selected individuals and provides the user with options that allow a wide range of customization. You can run this report via the menu .

The Narrated Web Site report creates pages that closely follow the World Wide Web Consortium’s Recommendations for XHTML 1.0 Strict and CSS 1. These recommendations include a separation of content from presentation. Due to this practice, the style and appearance of the new web pages can be completely controlled from one CSS stylesheet without altering individual pages.

Introduction pages can be added to provide additional information, such as a family history.

Genealogy records can generate a lot of files. Many web servers have a difficult time with a large number of files in a single directory. The Narrated Web report strives to keep the number of files per directory to a manageable level. To do this, a hierarchy of directories is created. The generated file names are not intuitive, but are unique for each person. Subsequent runs will generate identical file names, making it easy to update specific files.

{{-}}

#### Dialog tabs

The report dialog has the following tabs: {{-}}

##### Report Options

![[_media/NarratedWebSite-WebPages-ReportOptions-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Narrated Web Site - Web Pages - Report Options - tab default options]]

-  (Checkbox unchecked by default) If you have trouble transferring the files to an external web host, you can create a single gzip'd tar file to more easily upload the data. The large number of files and directories in this web output may make it difficult to transfer the files to an external web host. Gramps has the capability of saving all of your Narrative Web files in one compressed archive using the gzip and tar formats (casually known as a ‘tarball’). This single file can quickly be transferred to your server and uncompressed on the website host. ****

- (`~/yourhomedirectory/`<Family Tree Name>`+NAVWEB` default) The destination directory for the web files.

- (`My Family Tree` default) The title of the web site. You can enter a custom site title in this option.

- (Any person matching this filter who is not excluded due to the privacy rules, will be included in the output.) choose between

  - **Entire Database** (Default)
  - Descendants of active person
  - Descendant families of active person
  - Ancestors of active person
  - People with common ancestor with active person

- The center person for the report. (defaults to Active person)

- How to handle living people. You can control the display of sensitive information based on whether or not an individual is currently alive. However, since Gramps is a research tool, it is likely that there are individuals with no known date of death in your database. To deduce if an individual is *possibly still alive* Gramps employs an algorithm that compares death dates, birth dates, baptism/christening dates, death dates of ancestors and birth dates of ancestors. The algorithm assumes that each individual is *possibly still alive* unless the cross-referenced dates make the individual’s *possibility of being alive* unlikely.

  - **Exclude** – (Default) Excludes all information of all individuals who are *[possibly still alive](wiki:Gramps_6.0_Wiki_Manual_-_Probably_Alive)*
  - **Include Last Name Only**
  - **Include Full Name Only**
  - **Include** – Include all information of all individuals even if they are *possibly still alive*

- (`30` default) This option is inactive if the "Living People" option is set to **Include**.

- : Whether to include private objects. If your intention is to provide a complete record of your research, checking this box will include all entries marked **private** along with the rest of your database. (checkbox unchecked by default)

{{-}}

##### HTML Options

![[_media/NarratedWebSite-WebPages-HTMLOptions-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Narrated Web Site - Web Pages - Html options - tab default options]]

- The file extension to be used for the web files. Choose between **.html**(default)/.htm/.shtml/.php/.php3/.cgi

- (**Standard copyright** default) When creating a public a web site it is important to specify the copyright conditions under which you are publishing your data. International copyright law reserves all rights of your data to your discretion. You own the data and individuals must have your permission if they wish to reuse that data. In genealogical research sharing data with other researchers is a common practice. Other options include the Creative Commons licenses, offering a wide range of use restrictions or none at all. Learn more about the Creative Commons at <http://creativecommons.org/>

- Gramps provides seven built in style sheets for you to choose from to determine the appearance or your web pages. Choose between **Basic** (Ash, Blue, Cypress, Lilac, Peach or Spruce color schemes), **Mainz**, or **Nebraska** styles. There is also the option of not including a stylesheet (**No style sheet**). Regardless of the style you choose, the style sheet can be found in *`css/narrative-screen.css`*. You may edit this file to further customize the appearance of your web pages. If you make modifications to your style sheet be aware that regenerating your pages with the same output destination will overwrite your custom style sheet. To preserve your custom style sheet through subsequent web page updates select . If you want your own stylesheet, you can copy one of the existing stylesheet in *\$HOME/.gramps/css/*. This directory doesn't exist. You must create it before copying your future stylesheet. Change its name. If you ask for a new report, this new stylesheet will be added to the list of preexisting stylesheets.

- Choose which layout for the Navigation Menus. (Only available for selected Stylesheets)

  - **Horizontal -- Default**
  - Vertical -- Left Side
  - Fade -- [Webkit](https://en.wikipedia.org/wiki/WebKit) Browsers Only
  - Drop-Down -- Webkit Browsers Only

- Determine the default layout for the Source Page's Citation Referents section

  - **Normal Outline Style** (Default)
  - Drop-Down -- Webkit Browsers Only

- : Checking this box will include an ancestor graph on each individual’s detail page if they have defined ancestors in your database. (checkbox checked by default)

- :This option is inactive if the "Include ancestor graph" option is not checked. The default number of generations shown in the ancestor graphs is `4` with options of 2, 3, 4 or 5. The individuals represented in the ancestor graphs are the same individuals whose information is provided elsewhere in your web pages.

- This is a secure site (https) (checkbox unchecked by default)

{{-}}

##### Display

![[_media/NarratedWebSite-WebPages-Display-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Narrated Web Site - Web Pages - Display - tab default options]]

- Select the format to display the names. Choose from **Surname, Given Suffix** / Given Surname Suffix / Given / Main Surnames, Given Patronymic Suffix / SURNAME, Given (Common)

- : This option determines whether to include the Gramps ID of objects in your web page output. (checkbox unchecked by default)

- (checkbox unchecked by default)

{{-}}

##### Page Generation

![[_media/NarratedWebSite-WebPages-PageGeneration-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Narrated Web Site - Web Pages - Page Generation - tab default options]]

The following options can be set to generate three supplemental pages: **Home**, **Introduction** and **Contact**(Publisher Contact). From this tab you can also assign Media or Notes items to each page. By default no content (media or text) is assigned to these pages. Content for these pages must originate as Media or Notes items that you have previously created. If the desired items have already been added to your database you will be able to choose them from a list of Notes or Image Objects.

- Display an individual Note of your choice.

- Display an individual Media Object of your choice.

- Display an individual Note of your choice.

- Display an individual Media Object of your choice.

- Display an individual Note of your choice. ****

- Display an individual Media Object of your choice.****

- Display an individual Note of your choice. This text will appear directly below the site title on every web page.

- Display an individual Note of your choice. This text will appear within the footer, above the copyright statement on every web page.

{{-}}

##### Image Generation

![[_media/NarratedWebSite-WebPages-ImageGeneration-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Narrated Web Site - Web Pages - Image Generation - tab default options]]

-  This option determines whether to include/exclude a gallery of media objects on your website. (checkbox checked by default)

-  This option determines whether to include/exclude a gallery of unused media objects on your website. (checkbox checked by default)

-  : This option allows you to create only thumbnail images instead of full-sized images on the Media Page. This will allow you to have a much smaller total upload size to your web hosting site. (checkbox unchecked by default)

- (`800` default) This allows you to set the maximum width of the image (in pixels) shown on the media page. Set to 0 for no limit.

- (`600` default) This allows you to set the maximum height of the image (in pixels) shown on the media page. Set to 0 for no limit.

{{-}}

![[_media/wiki:How_to_create_image_reference_regions|[_media/NarrativeWeb-Media-tab-ImageReferenceRegions-example-50.png|Example of [image reference regions]] - Media tab of HTML output for "Narrative Web" Report]]

Note that [image reference regions](wiki:How_to_create_image_reference_regions) are also displayed in the Narrative Web HTML pages created with Gramps. There are no special options necessary for this feature, other than the existence of reference regions for 1 or more images. Narrative Web displays reference regions for people and place objects only. {{-}}

##### Download

![[_media/NarratedWebSite-WebPages-Download-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Narrated Web Site - Web Pages - Download - tab default options]]

- : Whether to include a database download option. (checkbox unchecked by default)

- Select the file to be used for downloading of database.

- (`Smith Family Tree` default) Give a description for this file.

- Select the file to be used for downloading of database.

- (`Johnson Family Tree` default) Give a description for this file.

{{-}}

##### Advanced Options

![[_media/NarratedWebSite-WebPages-AdvancedOptions-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Narrated Web Site - Web Pages - Advanced Options - tab default options]]

These settings address the amount of information displayed on the Surname detail and Individual index web pages.

- The encoding to be used for the web files.

  - **Unicode UTF-8 (recommended)** (Default)
  - ISO-8859-1
  - ISO-8859-2
  - ISO-8859-3
  - ISO-8859-4
  - ISO-8859-5
  - ISO-8859-6
  - ISO-8859-7
  - ISO-8859-8
  - ISO-8859-9
  - ISO-8859-10
  - ISO-8859-13
  - ISO-8859-14
  - ISO-8859-15
  - koi8_r

- : (If they have a webpage) (checkbox unchecked by default)

- (checkbox checked by default)

- (checkbox unchecked by default)

- (checkbox unchecked by default)

- (checkbox unchecked by default)

- (checkbox unchecked by default)

{{-}}

##### Include

![[_media/NarratedWebSite-WebPages-Include-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Narrated Web Site - Web Pages - Include - tab default options]]

- (checkbox unchecked by default)

- (checkbox unchecked by default)

- (checkbox unchecked by default)

- . This option creates a GENDEX file placed at the top of the website. You can see sites which support this format and read more about it at the [GENDEX Wikipedia article](http://en.wikipedia.org/wiki/GENDEX).)(checkbox unchecked by default)

- (checkbox unchecked by default)

- (checkbox unchecked by default)

{{-}}

##### Place Map Options

![[_media/NarratedWebSite-WebPages-PlaceMapOptions-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Narrated Web Site - Web Pages - Place Map Options - tab default options]]

- Choose your choice of map service for creating the Place Map Pages

  - **OpenStreetMap** (default)
  - Google

- : Whether to include a place map on the Place Pages, where Latitude/ Longitude are available. (checkbox unchecked by default)

- : Whether or not to add an individual page map showing all the places on this page. This will allow you to see how your family traveled around the country. (checkbox unchecked by default)

- Select which option that you would like to have for the Google Maps Family map pages...

  - **Family Links** (default)
  - Drop
  - Markers

- 

{{-}}

##### Other inclusion (CMS, Web Calendar, Php)

![[_media/NarratedWebSite-WebPages-OtherInclusionCMSWebCalendarPHP-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Narrated Web Site - Web Pages - Other inclusion (CMS, Web Calendar, Php) - tab default options]]

See also:

- [Howto:_Make_a_genealogy_website_with_Gramps#Integration_of_NarrativeWeb_in_a_CMS_or_MVS](wiki:Howto:_Make_a_genealogy_website_with_Gramps#Integration_of_NarrativeWeb_in_a_CMS_or_MVS)
- Feature request Integration of the Narrative Web Site into a CMS or MVC

{{-}}

#### Example Web Site output

The following sections show the default appearance of web pages the Narrative Website web page report. {{-}}

##### Home

(optional page) {{-}}

##### Introduction

(optional page) {{-}}

##### Individuals

(default page) {{-}}

##### Surnames

(default page) {{-}}

##### Families

(optional page) {{-}}

##### Events

(optional page) {{-}}

##### Places

(default page) {{-}}

##### Sources

(default page) {{-}}

##### Repositories

(optional page) {{-}}

##### Media

(default page) {{-}}

##### Thumbnails

(default page) {{-}}

##### Download

(optional page) {{-}}

##### Address Book

(optional page) {{-}}

##### Contact

(optional page) {{-}}

### <u>Web Calendar</u>

![[_media/WebCalendar-WebPages-example-DecemberCalendar2018-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Web Calendar Report - Web Pages - default Calendar for December 2018 - HTML output]]

The Web Calendar shows events for the selected individuals on a set of monthly calendars. You can run this report via the menu .

There are options to filter the individuals, to choose which years to include (by default, only the current year is included); whether to include only living people and whether to include birthdays or anniversaries or both; notes can be included on monthly pages and abbreviated pages can be included.

The report is designed to work with the [Narrative Web Site Report](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_7#Narrated_Web_Site). There is a 'Home' link on each page to the home page of the Narrative Web Site Report. There is also an option to include links from the individuals on the calendar to the same individual on the Narrated Web Site.

Working with the Narrated Web Site Report requires that the two reports have been constructed in a compatible way by the user. There is no automated check that the two are compatible. If the pages are not compatible, then the user will likely get a 'Page not found' error.

Compatibility depends on:

1.  Including the same individuals in the two reports,
2.  Storing the pages in compatible directories.

In order to include the same individuals in the two reports, the same filters should be used, and similar options with regard to including living individuals (the Web Calendar does not have an option to remove 'private' information).

By default, the Narrated Web Site Report is stored in the directory "`~/`<Family Tree Name>`+NAVWEB`", and by default the Web Calendar is stored in the directory "`~/`<Family Tree Name>`+WEBCAL`". If these defaults are retained, then the various links should work properly. If the directories have been changed, then the 'Home link' under the 'Content Options' and the 'Link prefix' under the 'Advanced Options' will need to be changed accordingly.

If the Web Calendar is to be used without an associated Narrative Web Site, then the text in the 'Home link' under the 'Content Options' should be deleted to ensure that no 'Home' link is generated.

#### Dialog tabs

The Web Calendar report dialog window has five tabs each are reviewed below. {{-}}

##### Report Options

![[_media/WebCalendar-WebPages-ReportOptions-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Web Calendar - Web Pages - Report Options - tab default options]]

- `~/yourhomedirectory/`<Family Tree Name>`+WEBCAL` The destination directory for the web files.

- (`My Family Calendar` default) The title of the calendar.

- choose between

  - **Entire Database** (Default)
  - Descendants of active person
  - Descendant families of active person
  - Ancestors of active person
  - People with common ancestor with active person

- The center person for the filter. (Default: Active person)

- The extension to be used for the web files.

  - **.html** (Default)
  - .htm
  - .shtml
  - .php
  - .php3
  - .cgi

- The copyright to be used for the web files.

  - **Standard copyright** (Default)
  - Creative Commons - By attribution
  - Creative Commons - By attribution, No derivations
  - Creative Commons - By attribution, Share-alike
  - Creative Commons - By attribution, Non-Commercial
  - Creative Commons - By attribution, Non-Commercial, No derivations
  - Creative Commons - By attribution, Non-Commercial, Share-alike
  - No copyright notice

- The stylesheet to be used for the web pages.

  - **Basic-Ash** (Default)
  - Basic-Blue
  - Basic-Cypress
  - Basic-Lilac
  - Basic-Peach
  - Basic-Spruce
  - Mainz
  - Nebraska
  - No style sheet
  - Visually Impaired

{{-}}

##### Report Options (2)

![[_media/WebCalendar-WebPages-ReportOptions2-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Web Calendar - Web Pages - Report Options (2) - tab default options]]

- Select the format to display the names. Choose from **Surname, Given Suffix**(default) / Given Surname Suffix / Given / Main Surnames, Given Patronymic Suffix / SURNAME, Given (Common)

{{-}}

##### Content Options

![[_media/WebCalendar-WebPages-ContentOptions-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Web Calendar - Web Pages - Content Options - tab default options]]

-  (checkbox unchecked by default)

  - (Defaults to current year)

  - (Defaults to current year)

- Select the country to see associated holidays. (Defaults to blank)

- Select the first day of the week for the calendar. (Default: **Sunday**)

- Select married women's displayed surname.

  - **Wives use their own surname** (Default)
  - Wives use husband's surname (from first family listed)
  - Wives use husband's surname (from last family listed)

- (**`../../Family Tree 1_NAVWEB/index.html`** default) The link to be included to direct the user to main page of the web site.

-  (checkbox checked by default)

-  (checkbox checked by default)

{{-}}

##### Jan - Jun Notes

![[_media/WebCalendar-WebPages-Jan-JunNotes-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Web Calendar - Web Pages - Jan-Jun Notes - tab default options]]

Select an existing note for the month.

- 

- 

- 

- 

- 

- 

{{-}}

##### Jul - Dec Notes

![[_media/WebCalendar-WebPages-Jul-DecNotes-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Web Calendar - Web Pages - Jul-Dec Notes - tab default options]]

Select an existing note for the month:

- 

- 

- 

- 

- 

- 

{{-}}

##### Advanced Options

![[_media/WebCalendar-WebPages-AdvancedOptions-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Web Calendar - Web Pages - Advanced Options - tab default options]]

- The encoding to be used for the web files

  - **Unicode UTF-8 (recommended)** (Default)
  - ISO-8859-1
  - ISO-8859-2
  - ISO-8859-3
  - ISO-8859-4
  - ISO-8859-5
  - ISO-8859-6
  - ISO-8859-7
  - ISO-8859-8
  - ISO-8859-9
  - ISO-8859-10
  - ISO-8859-13
  - ISO-8859-14
  - ISO-8859-15
  - koi8_r

-  (checkbox unchecked by default)

-  (checkbox unchecked by default)

-  (checkbox unchecked by default)

  - **`../../Family Tree 1_NAVWEB/`** A Prefix on the links to take you to Narrated Web Report.

{{-}}

#### Example Web Site output

{{-}}

<hr>

Back to [Index of Reports](wiki:Gramps_6.0_Wiki_Manual_-_Reports).

[Category:Fi:Dokumentaatio](wiki:Category:Fi:Dokumentaatio) [Category:Plugins](wiki:Category:Plugins)
