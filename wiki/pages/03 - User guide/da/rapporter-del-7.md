---
title: Da:Gramps 6.0 brugsanvisning - Rapporter - del 7
categories:
- Documentation
- Plugins
- Stub
managed: false
source: wiki-scrape
wiki_revid: 129293
wiki_fetched_at: '2026-05-30T17:33:58Z'
lang: da
---

{{#vardefine:chapter\|13.1}} {{#vardefine:figure\|0}} Tilbage [Indeks over Rapporter](wiki:Da:Gramps_6.0_brugsanvisning_-_Rapporter). {{-}}

<hr>

{{-}}

![[_media/MenuOverview-Reports-WebPages-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}}  Menu overview]] This section describes the reports, [Narrated Web Site](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_7#Narrated_Web_Site) and [Web Calendar](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_7#Web_Calendar) as part of the different reports available in Gramps.

## Web Pages

### <u>Narrated Web Site</u>

![[_media/NarratedWebSite-WebPages-Individuals-index-page-example-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Narrated Web Site - Web Pages - Individuals (index) page - default HTML output - example]]

The report generates a web site (that is, a set of linked web pages), for a set of selected individuals and provides the user with options that allow a wide range of customization. You can run this report via the menu .

The Narrated Web Site report creates pages that closely follow the World Wide Web Consortium’s Recommendations for XHTML 1.0 Strict and CSS 1. These recommendations include a separation of content from presentation. Due to this practice, the style and appearance of the new web pages can be completely controlled from one CSS stylesheet without altering individual pages.

Introduction pages can be added to provide additional information, such as a family history.

Genealogy records can generate a lot of files. Many web servers have a difficult time with a large number of files in a single directory. The Narrated Web report attempts to keep the number of files per directory to a manageable level. To do this, a hierarchy of directories is created. The generated file names are not intuitive, but are unique for each person. Subsequent runs will generate identical file names, making it easy to update specific files.

{{-}}

#### Dialog tabs

The report dialog has the following tabs each are reviewed below.

- [Report Options](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_7#Report_Options)
- [HTML Options](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_7#HTML_Options)
- [Display](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_7#Display)
- [Page Generation](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_7#Page_Generation)
- [Extra pages](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_7#Extra_pages)
- [Images Generation](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_7#Images_Generation)
- [Download](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_7#Download)
- [Advanced Options](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_7#Advanced_Options)
- [Include](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_7#Include)
- [Place Map Options](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_7#Place_Map_Options)
- [Other inclusion (CMS, web calendar, PHP)](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_7#Other_inclusion_.28CMS.2C_web_calendar.2C_PHP.29)
- [Translations](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_7#Translations)
- [Calendar Options](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_7#Calendar_Options)

{{-}}

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

  -  (Checkbox unchecked by default) - For each person page.

- How to handle living people. You can control the display of sensitive information based on whether or not an individual is currently alive. However, since Gramps is a research tool, it is likely that there are individuals with no known date of death in your database. To deduce if an individual is *possibly still alive* Gramps employs an algorithm that compares death dates, birth dates, baptism/christening dates, death dates of ancestors and birth dates of ancestors. The algorithm assumes that each individual is *possibly still alive* unless the cross-referenced dates make the individual’s *possibility of being alive* unlikely.

  - **Exclude** – (Default) Excludes all information of all individuals who are *[possibly still alive](wiki:Gramps_6.0_Wiki_Manual_-_Probably_Alive)*
  - **Include Last Name Only**
  - **Include Full Name Only**
  - **Include** – Include all information of all individuals even if they are *possibly still alive*

- (`30` default) This option is inactive if the "Living People" option is set to **Include**.

- : Whether to include private objects. If your intention is to provide a complete record of your research, checking this box will include all entries marked **private** along with the rest of your database. (checkbox unchecked by default)

{{-}}

##### HTML Options

![[_media/NarratedWebSite-WebPages-HTMLOptions-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Narrated Web Site - Web Pages - HTML Options - tab default options]]

- The extension to be used for the web files.

  - **.html** (Default)
  - .htm
  - .shtml
  - .php
  - .php3
  - .cgi

- \- When creating a public a web site it is important to specify the copyright conditions under which you are publishing your data. International copyright law reserves all rights of your data to your discretion. You own the data and individuals must have your permission if they wish to reuse that data. In genealogical research sharing data with other researchers is a common practice.

  - **Standard copyright** (default)
  - *Creative Commons - By attribution*- A range of six Creative Commons licenses, offering various use restrictions or none at all. Learn more about the Creative Commons at <https://creativecommons.org/>
  - *Creative Commons - By attribution, No derivations*
  - *Creative Commons - By attribution, Share-alike*
  - *Creative Commons - By attribution, Non-Commercial*
  - *Creative Commons - By attribution, Non-Commercial, No derivations*
  - *Creative Commons - By attribution, Non-Commercial, Share-alike*
  - *No copyright notice*

{{-}} ![[_media/NarratedWebSite-Stylesheet-examples-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;HTML Options&quot; tab - &quot;StyleSheet&quot; eight samples (shown top down order of list.)]]

- Gramps provides nine built in style sheets for you to choose from to determine the appearance or your web pages. Choose between these stylesheets:

  - **Basic-Ash** (a 'Basic' color scheme) ( default)
  - *Basic-Blue* (a 'Basic' color scheme)
  - *Basic-Cypress* (a 'Basic' color scheme)
  - *Basic-Lilac* (a 'Basic' color scheme)
  - *Basic-Peach* (a 'Basic' color scheme)
  - *Basic-Spruce* (a 'Basic' color scheme)
  - *Mainz* -
  - *Nebraska*
  - *No style sheet* (do not overwrite existing stylesheets)
  - *Visually Impaired*

  
Regardless of the style you choose, the style sheet can be found in *`css/narrative-screen.css`*. You may edit this file to further customize the appearance of your web pages.  
If you make modifications to your style sheet be aware that regenerating your pages with the same output destination will overwrite your custom style sheet.

The option of not including a stylesheet (**No style sheet**) it for users who have already created a custom style sheet when generating a previous Narrated Web Site report. To preserve your custom style sheet through subsequent web page updates select .

If you want your own stylesheet, you can copy one of the existing stylesheet in *`$HOME/.gramps/css/`*. If this directory doesn't exist. You must create it before copying your future stylesheet. Change its name. If you ask for a new report, this new stylesheet will be added to the list of pre-existing stylesheets.

- Choose which layout for the Navigation Menus. (Only available for selected Stylesheets)

  - **Horizontal -- Default**
  - Vertical -- Left Side
  - Fade -- [Webkit](https://en.wikipedia.org/wiki/WebKit) Browsers Only
  - Drop-Down -- Webkit Browsers Only

- Determine the default layout for the Source Page's Citation Referents section

  - **Normal Outline Style** (Default)
  - Drop-Down -- Webkit Browsers Only

- : Checking this box will include an ancestor graph on each individual’s detail page if they have defined ancestors in your database. (checkbox checked by default) ( Note: [Narrated Website Ancestry Tree Design Notes](wiki:Narrated_Website_Ancestry_Tree_Design_Notes) discusses creating a compact Ancestry trees using the [Buchheim](wiki:Narrated_Website_Ancestry_Tree_Design_Notes#buchheim)/[Walker](wiki:Narrated_Website_Ancestry_Tree_Design_Notes#walker) algorithm.)

  - You can change the number of generations shown from the tabs *[Graph generations:](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_7#Display)* option.

-  (checkbox unchecked by default) - adds links to the navigation bar.

-  (checkbox unchecked by default)

-  (checkbox unchecked by default) - Check if you want to open/close a section

{{-}}

##### Display

![[_media/NarratedWebSite-WebPages-Display-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Narrated Web Site - Web Pages - Display - tab default options]]

- Select the format to display the names. Choose from **Surname, Given Suffix** / Given Surname Suffix / Given / Main Surnames, Given Patronymic Suffix / SURNAME, Given (Common)

-  (checkbox unchecked by default) - Whether to display the narrative web in multiple languages. See the tab to add a new languages to the default one defined in the next field.

- \- The translation to be used for the report.

- \- The format and language for dates, with examples.

- \- Option determines whether to hide or show the Gramps ID of objects in your web page output.

  - **Do not include** (default)
  - Include

- \- Whether to include tags

  - **Do not include** (default)
  - Include

- (checkbox unchecked by default) - Whether to display children in birth order or in entry order?

- (checkbox unchecked by default) - Whether to display latitude/longitude in the places list?

- (checkbox unchecked by default) - Sort the places references by date or by name. Not set means by date.

- :This option is inactive if the *[Include ancestor's tree](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_7#HTML_Options)* option on the *HTML Options* tab is not checked. The default number of generations shown in the ancestor graphs is `4` with options of 2, 3, 4 or 5. The individuals represented in the ancestor graphs are the same individuals whose information is provided elsewhere in your web pages.

- (checkbox checked by default) - Unchecked will show them just before attributes.

{{-}}

##### Page Generation

![[_media/NarratedWebSite-WebPages-PageGeneration-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Narrated Web Site - Web Pages - Page Generation - tab default options]]

The *Page Generation* tab provides options for creation of commonly expected supplemental webpages and annotations common to all webpages throughout the generated website.

The first options are used to control generation of three supplemental pages: **Home** ([Home](https://en.wikipedia.org/wiki/Home_page) webpage), **Introduction** ([FAQ](https://wikipedia.org/wiki/FAQ#In_web_design) or [About Us](https://www.searchenginejournal.com/about-us-page-examples/250967/amp/) webpage) and **Publisher Contact** ([Contact Us](https://wikipedia.org/wiki/Contact_page) webpage).

Each of supplemental pages may be assigned a specific [Media](wiki:Gramps_Glossary#media) or [Note](wiki:Gramps_Glossary#note) item. By default, no content (neither media nor text from a Note) is assigned to these pages.

Content for these pages ***must*** originate as Media or Notes items that have been created before running the report. Once the desired items have been added to your Tree, you will be able to choose them from a list of Notes or Media Objects.

- Display an individual Note of your choice.

- Display an individual Media Object of your choice.

- Display an individual Note of your choice.

- Display an individual Media Object of your choice.

- Display an individual Note of your choice.

- Display an individual Media Object of your choice.

- Display an individual Note of your choice. This annotation text will appear directly below the site title on every web page.

- Display an individual Note of your choice. This annotation text will appear within the footer, above the copyright statement on every web page.

- A note to use for starting the php session. This option will be available only if the .php file extension is selected.

{{-}}

##### Extra Pages

![[_media/NarratedWebSite-WebPages-ExtraPages-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Narrated Web Site - Web Pages - Extra Pages - tab default options]]

- (blank) - Your extra page name like it is shown in the menubar.

- (blank) - Your extra page path without extension.

  - button

{{-}}

##### Images Generation

![[_media/NarratedWebSite-WebPages-ImageGeneration-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Narrated Web Site - Web Pages - Image Generation - tab default options]]

-  This option determines whether to include/exclude a gallery of media objects on your website. (checkbox checked by default)

-  This option allows you to create the images index. (checkbox unchecked by default)

-  This option determines whether to include/exclude a gallery of unused media objects on your website. (checkbox unchecked by default)

-  : This option allows you to create only thumbnail images instead of full-sized images on the Media Page. This will allow you to have a much smaller total upload size to your web hosting site. (checkbox unchecked by default)

-  : This option allows you to create the thumbnail index (checkbox unchecked by default)

- (`800` default) This allows you to set the maximum width of the image (in pixels) shown on the media page.

<!-- -->

- 

{{-}}

![[_media/wiki:How_to_create_image_reference_regions|[_media/NarrativeWeb-Media-tab-ImageReferenceRegions-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Example of [image reference regions]] - Media tab of HTML output for "Narrative Web" Report]]

Note that [image reference regions](wiki:How_to_create_image_reference_regions) are also displayed in the Narrative Web HTML pages created with Gramps. There are no special options necessary for this feature, other than the existence of reference regions for 1 or more images. Narrative Web displays reference regions for people and place objects only. {{-}}

##### Download

![[_media/NarratedWebSite-WebPages-Download-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Narrated Web Site - Web Pages - Download - tab default options]]

- : Whether to include a database download option. (checkbox unchecked by default)

- (`2` default) The number of download files to include in the download page

- Select the file to be used for downloading of database.

- (`Family Tree #1` default) Give a description for this file.

- Select the file to be used for downloading of database.

- (`Family Tree #2` default) Give a description for this file.

- Select the file to be used for downloading of database.

- (`Family Tree #3` default) Give a description for this file.

{{-}}

##### Advanced Options

![[_media/NarratedWebSite-WebPages-AdvancedOptions-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Narrated Web Site - Web Pages - Advanced Options - tab default options]]

These settings address the amount of information displayed on the Surname detail and Individual index web pages.

- The encoding to be used for the web files.

  - **Unicode UTF-8 (recommended)** (Default)
  - ISO-8859-1 *- [ISO/IEC character set standard:](https://wikipedia.org/wiki/ISO/IEC_8859) Part 1 (Latin 1: Western European)*
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
  - koi8_r ''- [Kod Obmena Informatsiey, 8 bit ("Code for Information Exchange - 8 bit")''](https://wikipedia.org/wiki/KOI8-R)

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

- (checkbox unchecked by default)

- (checkbox unchecked by default)

- (checkbox unchecked by default)

- . This option creates a GENDEX file placed at the top of the website. You can see sites which support this format and read more about it at the [GENDEX Wikipedia article](http://en.wikipedia.org/wiki/GENDEX).(checkbox unchecked by default)

- (checkbox unchecked by default)

- (checkbox unchecked by default)

{{-}}

##### Place Map Options

![[_media/NarratedWebSite-WebPages-PlaceMapOptions-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Narrated Web Site - Web Pages - Place Map Options - tab default options]]

- Choose your choice of map service for creating the Place Map Pages

  - **OpenStreetMap** (default)
  - Stamen Map
  - Google : For this option to work requires a to be entered. To apply for one goto the Google maps platform ( <https://cloud.google.com/maps-platform/> ) and select "Get Started" (top right corner) and follow the instructions (may involve a credit card) and then select the "Credentials" option on the "API Manager" menu . Then click on the "Create Credentials" button on the "Credentials" window. Click on "API Key "on the next pop-up window. Copy the generated API key to your clipboard and paste in to Gramps "Google maps API key:" field. I strongly suggest that after generating and placing your report online that you go back to the google maps platform and Click the "Restrict key" button on the API key created window and add your domain (this will stop other website hijacking your api key and making you pay! These new Google Maps API changes came into affect from the 11th of June 2018. see the pricing table <https://cloud.google.com/maps-platform/pricing/sheet/> "You also get a recurring \$200 credit on your billing account each month to offset your usage costs, and you can set usage limits to protect against unexpected cost increases"

- : Whether to include a place map on the Place Pages, where Latitude/ Longitude are available. (checkbox unchecked by default)

- : Whether or not to add an individual page map showing all the places on this page. This will allow you to see how your family traveled around the country. (checkbox unchecked by default)

- Select which option that you would like to have for the Google Maps Family map pages...

  - **Family Links** (default)
  - Drop
  - Markers

- The API key used for the Google maps. This key is mandatory and must be valid

- <https://developers.google.com/maps/documentation/javascript/get-api-key>

- 

- 

- 

- 

- 

{{-}}

##### Other inclusion (CMS, web calendar, PHP)

![[_media/NarratedWebSite-WebPages-OtherInclusionCMSWebCalendarPHP-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Narrated Web Site - Web Pages - Other inclusion (CMS, web calendar, PHP) - tab default options]]

-  (Checkbox unchecked by default)

  - `/NAVWEB` (default) - Where do you place your website ?

-  (Checkbox checked by default) Whether to include a page with the last updates

- `1` (default) - You want to see the last updates on how many days?

- `1` (default) - How many updates do you want to see max?

{{-}} See also:

- [Howto:_Make_a_genealogy_website_with_Gramps#Integration_of_NarrativeWeb_in_a_CMS_or_MVS](wiki:Howto:_Make_a_genealogy_website_with_Gramps#Integration_of_NarrativeWeb_in_a_CMS_or_MVS)
- Feature request Integration of the Narrative Web Site into a CMS or MVC

{{-}}

##### Translations

![[_media/NarratedWebSite-WebPages-Translations-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Narrated Web Site - Web Pages - Translations - tab default options]]

On the Translation tab you can choose which languages to display the report in.

To use this section enable the language option on the tab and you can also choose the language to display the narrative web report in if different from the default.

- *`Default`* - Default language Gramps is using.

- *`This site title`* - Change it to suit the language for this translation or use the default site title for the default language Gramps is using.

- *`Default`* - Default language Gramps is using.

- *`This site title`* - Change it to suit the language for this translation or use the default site title for the default language Gramps is using

- *`Default`* - Default language Gramps is using.

- *`This site title`* - Change it to suit the language for this translation or use the default site title for the default language Gramps is using

- *`Default`* - Default language Gramps is using.

- *`This site title`* - Change it to suit the language for this translation or use the default site title for the default language Gramps is using

- *`Default`* - Default language Gramps is using.

- *`This site title`* - Change it to suit the language for this translation or use the default site title for the default language Gramps is using

See also:

- [Multiple languages ​​for the narrative web and optional other additions \#1051](https://github.com/gramps-project/gramps/pull/1051) added Nov 9, 2020

{{-}}

##### Calendar Options

![[_media/NarratedWebSite-WebPages-CalendarOptions-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Narrated Web Site - Web Pages - Calendar Options - tab default options]]

-  (Checkbox unchecked by default)

- `Sunday`

- `Wives use their own surname`

-  (Checkbox unchecked by default)

-  (Checkbox checked by default)

-  (Checkbox checked by default)

-  (Checkbox unchecked by default)

-  (Checkbox checked by default)

- `1914`

<!-- -->

- [Multiple languages ​​for the narrative web and optional other additions \#1051](https://github.com/gramps-project/gramps/pull/1051) added Nov 9, 2020 "The web calendar doesn't work when multiple languages is in use and we link people to the narrative web. after multiple tries without succes, I integrate webcal in the narrative web. For each language, I use the related holidays calendar. (#07151)"

{{-}}

#### Example Web Site output

The following sections show the default appearance of web pages the Narrative Website web page report with optional pages enabled. (Using the [example.gramps](wiki:example.gramps) family tree.)

{{-}}

##### Home

(optional page) {{-}}

##### Introduction

(optional page) {{-}}

##### Individuals

Individuals (index) (default page) Filename: `individuals.html` ![[_media/NarratedWebSite-WebPages-Individuals-index-page-example-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Narrated Web Site - Web Pages - Individuals (index) page - default HTML output - example]]

{{-}}

##### <b>Surnames</b>

Surnames (index) (default page) Filename: `index.html`

###### Surnames count

Surnames (count index - sorted by "Number of People" column) (default page) Filename: `surnames_count.html` {{-}}

##### Families

(optional page) {{-}}

##### Events

(optional page) {{-}}

##### Places

Places (index) (default page) Filename: `places.html` {{-}}

##### Sources

Sources (index) (default page) Filename: `sources.html` {{-}}

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

##### Updates

Updates (default page) Filename: `updates.html` {{-}}

#### <span id="HTML Code">**HTML Code type Notes**</span>

Gramps [<strong>Notes</strong>](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_2#Editing_information_about_notes) set to the **HTML Code** [type](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_2#note_type) will be inserted under the object to which they are attached. This allows special *HTML chunks* to be included in the report.

The HTML chunks must be well-formed, with all tags properly closed, to avoid conflicts with the rest of the webpage generated by the report. Only insert tags in a **HTML Code**-type Note that would normally be contained within the body of a HTML document.

The following tags will always be ignored: `html`, `meta`, `doctype`, `head`, `meta`, `title`, `link`, `script`, `body`

All other tags will be available : `i`, `a`, `p`, `ol`, `ul`, `div`, `h1`-`h7`, `button`, `svg`, `table`, `tr`, `td`, … {{-}}

#### Prerequisites for Narrated Web Site

For Gramps 6.0.x, you need to install Pyicu and the associated packages.

See also:

- Navweb will not load ( Name localAlphabeticindex is not defined ) \[If optional prerequiste PyICU not installed \]

##### Possible problems

- If the report shows <b>"Failed Loading Plugin" name 'localAlphabeticIndex' is not defined : do you have the prerequisite `pyicu` installed ?</b>
  - Run *`gramps -v`* from the command line to see if any additional information that may help you is shown.
- Other errors: [Report a bug](wiki:Using_the_bug_tracker)

### <u>Web Calendar</u>

![[_media/WebCalendar-WebPages-example-DecemberCalendar2018-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Web Calendar Report - Web Pages - default Calendar for December 2018 - HTML output]]

The shows events for the selected individuals on a set of monthly calendars. You can run this report via the menu .

There are options to filter the individuals, to choose which years to include (by default, only the current year is included); whether to include only living people and whether to include birthdays or anniversaries or both; notes can be included on monthly pages and abbreviated pages can be included.

The report is designed to work with the [Narrative Web Site Report](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_7#Narrated_Web_Site). If selected there is a 'Home' link on each page to the home page of the Narrative Web Site Report. There is also an option to include links from the individuals on the calendar to the same individual on the Narrated Web Site.

Working with the Narrated Web Site Report requires that the two reports have been constructed in a compatible way by the user. There is no automated check that the two are compatible. If the pages are not compatible, then the user will likely get a '[Page not found](https://en.wikipedia.org/wiki/HTTP_404)' error.

Compatibility depends on:

1.  Including the same individuals in the two reports,
2.  Storing the pages in compatible directories.

In order to include the same individuals in the two reports, the same filters should be used, and similar options with regard to including living individuals (the Web Calendar does not have an option to remove 'private' information).

By default, the Narrated Web Site Report is stored in the directory "`~/`<Family Tree Name>`+NAVWEB`", and by default the Web Calendar is stored in the directory "`~/`<Family Tree Name>`+WEBCAL`". If these defaults are retained, then the various links should work properly. If the directories have been changed, then the 'Home link' under the 'Content Options' and the 'Link prefix' under the 'Advanced Options' will need to be changed accordingly.

If the Web Calendar is to be used without an associated Narrative Web Site, then uncheck the option on the tab this will ensure that no 'Home' link is generated.

#### Dialog tabs

The Web Calendar report dialog window has the following tabs each are reviewed below.

- [Report Options](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_7#Report_Options_2)
- [Report Options (2)](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_7#Report_Options_.282.29)
- [Content Options](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_7#Content_Options)
- [Advanced Options](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_7#Advanced_Options_2)
- [Jan - Jun Notes](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_7#Jan_-_Jun_Notes)
- [Jul - Dec Notes](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_7#Jul_-_Dec_Notes)

{{-}}

##### Report Options

![[_media/WebCalendar-WebPages-ReportOptions-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Web Calendar - Web Pages - Report Options - tab default options]]

- `~/yourhomedirectory/`<Family Tree Name>`+WEBCAL` The destination directory for the web files.

  - button

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
  - *Creative Commons - By attribution* - A range of six Creative Commons licenses, offering various use restrictions or none at all. Learn more about the Creative Commons at <https://creativecommons.org/>
  - *Creative Commons - By attribution, No derivations*
  - *Creative Commons - By attribution, Share-alike*
  - *Creative Commons - By attribution, Non-Commercial*
  - *Creative Commons - By attribution, Non-Commercial, No derivations*
  - *Creative Commons - By attribution, Non-Commercial, Share-alike*
  - *No copyright notice*

- The stylesheet to be used for the web pages.

  - **Basic-Ash** (a 'Basic' color scheme) ( default)
  - *Basic-Blue* (a 'Basic' color scheme)
  - *Basic-Cypress* (a 'Basic' color scheme)
  - *Basic-Lilac* (a 'Basic' color scheme)
  - *Basic-Peach* (a 'Basic' color scheme)
  - *Basic-Spruce* (a 'Basic' color scheme)
  - *Mainz* -
  - *Nebraska*
  - *No style sheet* (do not overwrite existing stylesheets)
  - *Visually Impaired*

{{-}}

##### Report Options (2)

![[_media/WebCalendar-WebPages-ReportOptions2-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Web Calendar - Web Pages - Report Options (2) - tab default options]]

- \- Select the format to display the names. This choice in normally taken from the default setting in [](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Display_Options) tab for . Or to override that setting for the report choose from:

  - *Surname, Given Suffix* (Default in a new Family Tree )
  - Given Surname Suffix
  - Given
  - Main Surnames, Given Patronymic Suffix
  - SURNAME, Given (Common)

-  (checkbox unchecked by default)

-  (checkbox checked by default) - eliminates ancestors for webcalendars being used as reminder tools instead of historical tools.

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

##### Content Options

![[_media/WebCalendar-WebPages-ContentOptions-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Web Calendar - Web Pages - Content Options - tab default options]]

-  (checkbox unchecked by default) Whether to create Multiple year calendars or not.

  - (Defaults to current year)

  - (Defaults to current year)

- Select the country to see associated holidays. (Defaults to blank)

- Select the first day of the week for the calendar. (Default: **Sunday**)

- Select married women's displayed surname.

  - **Wives use their own surname** (Default)
  - Wives use husband's surname (from first family listed)
  - Wives use husband's surname (from last family listed)

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

-  (checkbox checked by default)

-  (checkbox checked by default)

-  (checkbox unchecked by default)

-  (checkbox unchecked by default)

  - (`1914` default) Show data only after this year. Default is current year - 'maximum age probably alive' which is defined in the dates preferences tabs.

  - **`../../Family Tree 1_NAVWEB/`** A Prefix on the links to take you to Narrated Web Report.

{{-}}

##### Jan - Jun Notes

![[_media/WebCalendar-WebPages-Jan-JunNotes-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Web Calendar - Web Pages - Jan-Jun Notes - tab default options]]

Use the buttons to choose the note from the selector for each of the months if needed:

- 

- 

- 

- 

- 

- 

{{-}}

##### Jul - Dec Notes

![[_media/WebCalendar-WebPages-Jul-DecNotes-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Web Calendar - Web Pages - Jul-Dec Notes - tab default options]]

Use the buttons to choose the note from the selector for each of the months if needed:

- 

- 

- 

- 

- 

- 

{{-}}

#### Example Web Site output

![[_media/WebCalendar-WebPages-example-DecemberCalendar2018-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Web Calendar Report - Web Pages - default Calendar for December 2018 - HTML output]]

{{-}}

### See Also

- [Web Solutions for Gramps](wiki:Web_Solutions_for_Gramps)

<hr>

Tilbage til [Indeks over Rapporter](wiki:Da:Gramps_6.0_brugsanvisning_-_Rapporter). {{-}}

[Category:Documentation](wiki:Category:Documentation) [Category:Plugins](wiki:Category:Plugins)
