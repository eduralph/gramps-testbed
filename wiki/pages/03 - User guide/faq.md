---
title: Gramps 6.0 Wiki Manual - FAQ
categories:
- Documentation
managed: false
source: wiki-scrape
wiki_revid: 128623
wiki_fetched_at: '2026-05-30T11:14:47Z'
---

{{#vardefine:chapter\|A}} {{#vardefine:figure\|0}} This appendix contains the list of **Frequently Asked Questions** (FAQ) that repeatedly come up in discussion forums and mailing lists.

This list is by no means complete. If you would like to add questions/answers to this list, please [join](wiki:Contact#Forum) and add your suggestions to the help section of the forum.

Also consider having a look at the following Categories on the Gramps wiki:

- [How do I...](wiki::Category:How_do_I...)
- [Gramps Tutorials](wiki::Category:Tutorials)

You may find it useful to review

- [:Gramps Glossary](wiki::Gramps_Glossary) - gives an overview of terms that appear in Gramps
- [:Genealogy Glossary](wiki::Genealogy_Glossary) - genealogical terms and meanings.

## General

### What is Gramps?

Gramps is a suite of personal genealogy tools that let you store, edit, and research genealogical data. It helps you sort out the complex relationships between various people, places and events. Gramps gives you many different ways to record the many details of an individual’s life and all of your research is kept organized, searchable. See [About](wiki:Gramps:About).

### Where do I get it and how much does it cost?

Gramps can be [installed](wiki:Installation) at no charge. Gramps is an Open Source project covered by the GNU General Public License. You have full access to the source code and are allowed to distribute the program and source code freely.

### Do I need to register as a user to use Gramps, I am not a programmer?

No, registering is only needed if you want to file a bug (or feature request) report or edit/write a wiki page.

No programming skill needed for that.

### Does Gramps exist in other languages?

Yes, at the release of Gramps 6.0 it has been translated into 28 languages, see [Gramps translations](wiki:Gramps_translations).

### How do I keep backups?

Automatic backup is a default feature that protects your genealogical data in Gramps. (It became automated in 2018 with the release of the 6.0 version.) The interval, backup file path and option to backup when exiting Gramps settings are in the tab of the menu. Additionally, a backup can be manually selected from the window.

It is extremely important to keep backups of your data, and keep them in a safe place. Gramps has a specific portable file format which is small, and human readable, denoted by `.gramps`. See the "[backup up a Family Tree](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees#Backing_up_a_Family_Tree)" section of the manual. It is also important to be aware of [what is omitted from a Gramps backup](wiki:Template:Backup_Omissions).

You can copy this backup file from time to time to a safe location (<abbr title="exempli gratia - Latin phrase meaning 'for example'">e.g.</abbr>, a USB stick). \[Note: The `.gramps` files are compressed by default. Clicking them will open Gramps. To see the XML, select the `.gramps` file and open it with a decompressing utility (like ark, gunzip, 7-zip), after which you can extract the XML text file which is human readable, see [details](wiki:Generate_XML#How_do_I_uncompress_the_file?).

Gramps does a quick hidden binary backup to allow restore if an error is noted. If the correct package is installed, you can use a revision system.

Another method is to backup the *`/.gramps`* hidden directory. This subdirectory is situated in your [User Directory](wiki:Gramps_6.0_Wiki_Manual_-_User_Directory). Backing up this directory will backup your databases and revisions. (On Windows 10 it is *`/Users/`<your username>`/AppData/Roaming/gramps`*)

**Do not keep backups in GEDCOM format**. Not all information Gramps stores can be written in the GEDCOM. Hence, an export/import operation from Gramps exported into GEDCOM and re-imported into Gramps, will mean you **lose** [data](wiki:Gramps_and_GEDCOM). Use the `.gramps` file format for backups!

**Do not keep backups in GRDB format**. GRDB is a database, which might be computer dependent (read, not working on a different PC). Small damage to a GRDB file can also not be repaired. Use the `.gramps` file format for backups!

### Does Gramps support Unicode fonts?

In particular, does it support non-Roman Unicode fonts? Yes. Gramps works internally with Unicode (UTF-8), so all alphabets can be used on all entry fields.

There is no special assistance for entering Unicode symbols (glyphs) that are not directly labeled on your keyboard. Finding aids for [precomposed characters](https://wikipedia.org/wiki/Precomposed_character) (aka composite characters or decomposable characters) with diacritical marks are available outside the program. You may find the various language-specific [multilingual virtual keyboards on the Lexilogos website](https://www.lexilogos.com/keyboard/latin_alphabet.htm) useful.

All reports fully support Unicode, [although for PDF/PS](#Why_are_non-Latin_characters_displayed_as_garbage_in_PDF.2FPS_reports.3F) you need to work with gnome-print or [LibreOffice](http://www.documentfoundation.org/download/).

## Installation

### What is needed to install Gramps under Linux, Solaris, or FreeBSD?

Gramps is a [GTK](http://en.wikipedia.org/wiki/Gtk) application. Gramps needs to have the [PyGObject](http://en.wikipedia.org/wiki/PyGObject) libraries installed on the system. As long as these libraries are installed, Gramps should function. It will operate under the GNOME desktop, KDE desktop, or any other desktop. If the GNOME bindings for Python are installed on the system, Gramps will have additional functionality. Please check that it meets the Gramps project recommendations regarding the GTK version to use.

### Does Gramps work on Windows?

Yes, Windows is a community supported platform for Gramps.

You can [download](wiki:Download#MS_Windows) the [All In One Gramps Software Bundle for Windows](wiki:All_In_One_Gramps_Software_Bundle_for_Windows)(GrampsAIO).

We will do our best to solve any reported Windows-related problems. See [here](wiki:Contact).

### Does Gramps work on the Mac?

Yes, macOS is a community supported platform for Gramps.

You can [download](wiki:Download#macOS) the macOS version.

We will do our best to solve any reported Apple macOS related problems. See [here](wiki:Contact).

See [here](wiki:Mac_OS_X:Application_package).

### Does Gramps work on my mobile device?

Short answer is no, Gramps cannot be installed on your Mobile Phone or tablet( [Google Android](https://en.wikipedia.org/wiki/Android_(operating_system)) or [Apple iOS](https://wikipedia.org/wiki/IOS) )

More technical answer is 'yes' but ***not**'' as a***native**'' application. Using Gramps would require either:

:# install a version of Linux Operating systems on the mobile device along with all the support packages, or

:# set up a local or online server with a fork of [Gramps designed for collaboration](wiki:Web_Solutions_for_Gramps#Interactive_web_apps) (such as [Gramps Web](wiki:Web_Solutions_for_Gramps#GrampsWeb)) and then work with Gramps via browsing

### Does Gramps work on my Google Chromebook?

You can but with a few issues install Gramps on your [Chromebook](https://en.wikipedia.org/wiki/Chromebook) ([ChromeOS](https://en.wikipedia.org/wiki/ChromeOS)).

See:

- Drag and Drop Not Working in Crostini\[Linux\] on a Pixelbook

### What are the Minimum Specs to run Gramps?

We would recommend at least an 1920x1080 video display. The early memory requirements for Gramps, have been reduced, and Gramps were quite high. Beginning with Gramps 3.0, the software could run quite efficiently on a 256MB system, holding considerably more people. A system with 512MB should be able to hold around 200,000 people. However, disk disk space requirements for databases are however considerably larger, with a typical database being several megabytes in size. For 120.000 people you must consider already 530MB for the database. Pictures are stored on disk separately, so a large harddisk is necessary.

<span id="How do I upgrade GRAMPS?">

### How do I upgrade Gramps?

</span> Upgrades begin with making [backups](wiki:How_to_make_a_backup) of ALL your Trees. But in addition to that, look at the list [Backup Omission](wiki:Template:Backup_Omissions) to determine additions items you may want to archive. (The most important items are noting the database path, backup path, and relative media path in Preferences. If you can't find your data after an upgrade, you will be very unhappy.)

Once backups are safely stored, the most safest approach to upgrading is: downloading the newest installer, un-installing the existing Gramps and re-installing from the installer.

Start Gramps (the first load will be slow as it re-compiles and caches the Python source code files) In the "Edit -\> Preferences...", enter your Media path on the General tab, database path on the Family Tree tab, backup on the Family Tree tab. Try loading your Tree via the Family Trees menu.

If this was a 'minor' update (containing only bug fixes), the update should find your configuration and add-ons with no further effort. If it was an upgrade, you wil need to reset all your configuration customizations and download the compatible add-ons.

## Preferences

### Can I change the dates in reports to 'day month year'?

Yes, in the preferences ( tab) change the setting for Gramps to the required format (eg YYYY-MM-DD or day month year), and make the report. Your global date preferences will be used.

### Is there a Dark Mode?

Only by installing the [Themes addon](wiki:Addon:ThemePreferences), that adds a tab to . This addon is helpful if you have issues with light sensitivity and or if you prefer a dark mode for night use or just in general. In the Theme tab you can activate the "" option that are available for most Themes. You can also increase the fontsize for less fatigue when reading.

## Collaboration-Portability

### Is Gramps compatible with other genealogical software?

Gramps makes every effort to maintain compatibility with [GEDCOM](wiki:GEDCOM), the general standard of recording genealogical information. We have import and export filters that enable Gramps to read and write GEDCOM files.

It is important to understand that the GEDCOM standard is poorly implemented -- virtually every genealogical software has its own "flavor" of GEDCOM. As we learn about new flavor, the import/export filters can be created very quickly. However, finding out about the unknown flavors requires [user feedback](wiki:Contact). Please feel free to inform us about any GEDCOM flavor not supported by Gramps, and we will do our best to support it!

There is a specific article of this wiki which discusses [Gramps and GEDCOM](wiki:Gramps_and_GEDCOM). There is also an article about the know idiosyncracies of [GEDCOM dialects when importing from another program](wiki:Import_from_another_genealogy_program).

### Can Gramps read files created by other genealogy programs?

Yes can read GEDCOM files created by other genealogy programs.

- [See above.](wiki:Gramps_6.0_Wiki_Manual_-_FAQ#Is_Gramps_compatible_with_other_genealogical_software.3F)

### Can Gramps write files readable by other genealogy programs?

Yes can write GEDCOM files to be read by other genealogy programs.

- [See above.](wiki:Gramps_6.0_Wiki_Manual_-_FAQ#Is_Gramps_compatible_with_other_genealogical_software.3F)

### What standards does Gramps support?

The nice thing about standards is that there never is a shortage of them. Gramps is tested to support the following flavors of GEDCOM 5.6.0, Brother's Keeper, Family Origins, Family Tree Maker, Ftree, GeneWeb, Legacy, Personal Ancestral File, Pro-Gen, Reunion, and Visual Genealogie.

### How do I import data from another genealogy program into Gramps?

The best way is to create a new family tree, and select the import option in the file menu. Here you select the GEDCOM you generated with the other program, and import it.

### Can I install Gramps on a Linux Web Server and use it via a web browser?

This would enable my relations worldwide to access and update it.

While Gramps can generate web sites, it does not provide a web interface that allows for editing. If this is a requirement, then [GeneWeb](http://geneweb.org) or [webtrees](http://www.webtrees.net/) are programs more likely to meet your needs. Also have a look at experimental [gramps-online](https://github.com/gramps-project/gramps-online). However, you may wish to ask yourself the following questions:

1.  Do I really want relatives or other people to directly edit my genealogy database?
2.  Do I implicitly trust, without verification, any data that people may enter?
3.  Do these people have the same understanding of good genealogy practice that I have?

A better approach may be to provide a web form interface that allows others to enter data that is then held for your examination. You can then decide if the information should be entered into your database.

You may also want to consider the effects of possible downtime of your site if you cannot afford yourself a premium webhosting service.

### How to run two versions of Gramps together on one machine?

This can be done using virtualization software like Virtualbox.

See:

- [Run different Gramps versions parallel](wiki:Run_different_Gramps_versions_parallel)

## Reports

### Can Gramps print a genealogical tree for my family?

Yes. Different people have different ideas of what a genealogical tree is. Some think of it as a chart going from the distant ancestor and listing all his/her descendants and their families. Others think it should be a chart going from the person back in time, listing the ancestors and their families. Yet other people think of a table, text report, etc.

Gramps can produce any of the above, and many more different charts and reports. Moreover, the plugin architecture enables users (you) to create their own plugins which could be new reports, charts, or research tools.

### How can the relationship between people on the tree be determined?

Some users are interested in only showing direct ancestor or descendant genetic relationships. Other users are also interested in collateral (cousins!) lines or immediate in-laws. And yet other users are interested in how the most indirect connections influence a community.

So Gramps offers a continually expanding variety of tools, reports and methods to determine how people are connected within a Tree's database. Following a discussion on the Gramps-User [Maillist](wiki:Contact#Mailing_lists), the posted suggestions have been collated and expounded upon in the "[How to find the relationship between people](wiki:How_to_find_the_relationship_between_people)" article in the "[How do I...](wiki::Category:How_do_I...)" wiki category.

### In what formats can Gramps output its reports?

Text reports are available in HTML, PDF, ODT, LaTeX, and RTF formats. Graphical reports (charts and diagrams) are available in PostScript, PDF, SVG, ODS, and [GraphViz](wiki:Output_formats#Graphviz) formats.

### How can I change the default language in reports?

The reports are in the language of your installation. Most reports allow you to select the Language to output to look for the option to select the translation to be used for the report. You can change it by installing extra language packs, see [Howto:Change the language of reports](wiki:Howto:Change_the_language_of_reports).

### Is Gramps compatible with the Internet?

Yes, in a variety of ways. There are features for referencing hot-linked external data, archiving tools to collecting them to internal storage, and while Gramps is designed to be a local application, a rich set of tools have been created for publishing some or all of your research to the web.

Gramps can store web addresses and direct your browser to them. It can import data that you download from the Internet. It can export data that you could send over the Internet. Gramps is familiar with the standard file formats widely used on the Internet (<abbr title="exempli gratia - Latin phrase meaning 'for example'">e.g.</abbr> JPEG, PNG, and GIF images, MP3, OGG, and WAV sound files, QuickTime, MPEG, and AVI movie files, etc). If your browser is configured to access other file types, Gramps will inherit that ability.

There are addon Finding Aid tools to assist searching for records in online sources. The is an increasing variety of other [Web Solutions for Gramps](wiki:Web_Solutions_for_Gramps).

The Reports can optionally generate content in formats suitable for publication as webpages or even as entire websites. And there are development forks that extend Gramps into online genealogical content management systems. Some are dynamic presentation systems for publishing research, others offer limited collaborative editing.

#### See Also

- [Web Solutions for Gramps](wiki:Web_Solutions_for_Gramps)

### Can I create custom reports/filters/whatever?

Yes. There are many levels of customization. One is creating or modifying the templates used for the reports. This gives you some control over the fonts, colors, and some layout of the reports. You can also use Gramps controls in the report dialogs to tell what contents should be used for a particular report. In addition to this, you have an ability to create your own filters -- this is useful in selecting people based on criteria set by you. You can combine these filters to create new, more complex filters. Finally, you have an option to create your own plugins. These may be new reports, research tools, import/export filters, etc. This assumes some knowledge of programming in Python.

### Why are non-Latin characters displayed as garbage in PDF/PS reports?

This is a limitation of the built-in fonts of PS and PDF formats. To print non-Latin text, use the Print... in the format selection menu of the report dialog. This will use the `gnome-print` backend, which supports PS and PDF creation, as well as direct printing. (Note: you might need to install gnome-print separately as it is not required for Gramps).

If you only have Latin text, the PDF option will produce a smaller PDF compared to that created by gnome-print, simply because no font information will be embedded.

### I would like to contribute to Gramps by writing my favorite report. How do I do that?

The easiest way to contribute to reports, filters, tools, etc. is to copy an existing Gramps report, filter, or tool. If you can create what you want by modifying existing code -- great! If your idea does not fit into the logic of any existing Gramps tool, you will need to write your own plugin from scratch. Help is available on the [Developers Portal](wiki:Portal:Developers), or on the [Developers mailing list](wiki:Contact): gramps-devel@lists.sourceforge.net.

To test your work in progress, you may save your plugin under `$HOME/.gramps/plugins` directory and it should be found and imported on startup. The correctly written addon/plugin will register itself with Gramps, create menu item, and so on.

If you are happy with your addon/plugin and would like to contribute your code back to the Gramps project, you are very welcome to do so by joining and contacting us at gramps-devel@lists.sourceforge.net mailing list.

## Database - Gramps file formats

The default file format is [Gramps XML](wiki:Gramps_XML) it is used for exports, backups, and imports and preserves your entered genealogical data with no data loss as compared to the GEDCOM format.

### What is the maximum database size (bytes) Gramps can handle?

Gramps has no hard limits on the size of a database that it can handle. Starting with 2.0.0 release, Gramps no longer loads all data into memory, which allows it to work with a much larger database than before. In reality, however, there are practical limits. The main limiting factors are the available memory on the system and the cache size used for BSDDB database access. With common memory sizes these days, Gramps should have no problem using databases with [Millions of people](wiki:Gramps_Performance#JohnBoyTheGreat_2019-12.2C_version_6.0.1).

### How many people can Gramps database handle?

See above. Again, this is dependent on how much memory and storage space your computer has, see [Gramps Performance](wiki:Gramps_Performance).

### My database is really big. Is there a way around loading all the data into memory?

Starting with 2.0.0 release, Gramps no longer loads all data into memory, which allows it to work with a much larger database than before. The fileformat used is `.grdb` which means Gramps database.

### Can I run Gramps from a database on a NFS share?

Yes you can run a Gramps database from a [NFS(NetworkFile System)](https://en.wikipedia.org/wiki/Network_File_System) share.

### What does "portable" mean?

A Gramps 3 database (and any .grdb file) is very dependent on the software versions that created it. For example, you can't just move your Gramps data in these formats to a different operating system (or even a different version of an operating system) and expect that you will be able to read your data. The data is not "portable". Therefore, you can't just rely on backups of these formats, but you should also occasionally export into a format that is portable. There are two possible portable formats: GEDCOM and Gramps XML (.gramps or .gpkg). But only Gramps XML is recommended, as it faithfully saves all of your data.

### Why is the database format (GRDB) not portable?

The biggest issue with Gramps portability lies with 'transactions'. With Gramps 2.2, we added support for atomic transactions to protect data. With atomic transactions, multiple changes are committed as a single unit. Either all the changes make it, or none of the changes make it. You are never left in a situation with a partial set of changes. A side benefit of using transactions is that database access (reads and writes) are faster.

The problem with transactions (at least using BSDDB) is that it does not allow all the data to be stored in a single file. Logging files are needed to keep track of things. These logging files are kept in a DB Environment directory. We need a separate directory for each file, otherwise the log files can interfere with each other.

In 2.2, we keep the log files under the `~/.gramps/` directory, creating a unique directory for each database. The problem is that your GRDB file needs the log files, which are in a different directory.

Copying the GRDB file is only copying a portion of the database.

### Does Gramps have an Example Tree?

Yes, it does. Several example family tree databases are [included with most installations of Gramps and can be imported](wiki:Example.gramps#Load_example.gramps) for working through tutorials and for safely exploring tools or features.

The example family tree database (**`example.gramps`** file) attempts the ideal of having at least one example of even the obscure things that Gramps does. You can import the example into a blank Tree then safely make destructive exploratory mistakes on a disposable working database. And when you suspect that you have discovered an issue (aka 'bug') in Gramps, you can first try the same operation with the example family tree then [file a bug report](wiki:How_to_create_a_good_bug_report).

- The [<code>Example.gramps</code> wiki article](wiki:Example.gramps) describes where to find the example Family Tree archival file, how to use it and suggests some alternative files.

## Bugs and requests

### What do I do if I have found a bug?

You can [submit a bug report.](wiki:Using_the_bug_tracker)

A good bug report would include:

1.  Version of Gramps you were using when you encountered the bug (available through Help → About menu item).
2.  Language under which Gramps was run (available by executing `echo $LANG` in your terminal).
3.  Symptoms indicating that this is indeed a bug.
4.  Any Traceback messages, error messages, warnings, etc, that showed up in your terminal or a in separate traceback window.

Most problems can be fixed quickly provided there is enough information. To ensure this, please follow up on your bug reports. Then we will have a way of contacting you should we need more information.

### Requests

- Gramps should be a .... type of application

It is obvious that Gramps absolutely needs to become a (client-server/web-based/PHP/weblog/Javascript/C++/distributed/KDE/Motif/Tcl/Win32/C#/You-name-it) application. When is this going to happen?

The surest way to see it happen is to get it done by yourself. Since Gramps is free/open source, nobody prevents you from taking all of the code and continuing its development in whatever direction you see fit. In doing so, you may consider giving your new project another name to avoid confusion with the continuing Gramps development. If you would like the Gramps project to provide advice, expertise, filters, etc., we will gladly cooperate with your new project, to ensure compatibility or import/export options to your new format of a project.

If, however, you would like the Gramps project to adopt your strategy, you would need to convince Gramps developers that your strategy is good for Gramps and superior to the present development strategy.

## Adding to and editing my database

### What is the difference between a residence and an address?

A residence is a place where someone lived for a period of time. An address is the name of a residence formatted in the way expected by the postal system. Therefore each residence can also have an address if that is useful. See also: [Why residence event and not Address?](wiki:Why_residence_event_and_not_Address%3F)

### How do I change the order of children?

Children can be moved in the [Family Editor](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1#Editing_information_about_relationships)'s [Children](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1#Children) tab by [dragging and dropping](http://en.wikipedia.org/wiki/Drag-and-drop) or using the and buttons.

Alternatively install and

- Use the third-party addon tool which allows bulk updates of the children order.

### How do I change the order of spouses?

Spouses (also listed as their Relationship or as a Family in different parts of the wiki) can be reordered from the [Relationships Category](wiki:Gramps_6.0_Wiki_Manual_-_Categories#Reorder_Relationships_dialog) view by selecting the button in the toolbar or selecting menu item. Alternately, the Events tab lists a collapsible Family for each spouse when Editing a Person. When there are multiple Families, selecting a Family and clicking the Upwards or Downwards button below the Tab headers will reorder the Selected Family.

### How do I add an additional spouse?

See [Add a spouse](wiki:Add_a_spouse)

### How do I remove a spouse?

Removing a Spouse (without deleting the Person profile from the tree) requires just a single click in the [Edit Family](wiki:Gramps_Glossary#family) dialog. Simply click the "Remove person as the mother/father" (-) button just above the name of the Spouse.

*The Name, Birth & Death will be cleared and the "Add a new person as the mother/father" (+) and "Shared person selection" buttons will replace the (-) and "Edit" buttons.*

To remove the Spouse from the Tree entirely, select the Person in the Person view and click the "Delete the selected person" (-) toolbar button. A confirmation dialog will appear. Confirm by clicking the "Delete Person" button.

*The Person will be removed from all families where they are a Spouse or a Child. The attached Events, Citations, Notes and Media will be orphaned. The other secondary objects will be deleted along with their Person.*

### How do you add photos to an item?

See [Adding photos and other media objects](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_brief#Adding_photos_and_other_media_objects).

### How do you find unused media?

Media that have not been associated with any objects may be found by creating a [Custom Filter](wiki:Gramps_6.0_Wiki_Manual_-_Filters#Custom_Filters) in the Media Category view. Use the [Media objects with a reference count of &lt;count&gt;](wiki:Gramps_6.0_Wiki_Manual_-_Filters#Media_objects_with_a_reference_count_of_.3Ccount.3E) rule to find media with fewer than 1 reference.

### How can I publish a genealogy web site with Gramps?

<span id="How can I publish web sites generated by GRAMPS?"> Gramps has multiple options in the Reports menu for creating Web Pages based on your Tree data.

The [Howto: Make a genealogy website with Gramps](wiki:Howto:_Make_a_genealogy_website_with_Gramps) tutorial describes using the [Narrated Web Site](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_7#Narrated_Web_Site) (a.k.a. NarrativeWeb) report. In it, you will learn to generate a website around a set of people in your Family Tree.

Once generated, you can upload the web files to a hosting service. You can also distribute them on a portable thumbdrive or other media.

#### See Also

- [Web Solutions for Gramps](wiki:Web_Solutions_for_Gramps)

</span>

- You can also install third party addon reports to create other styles of web content. See the [Addons List](wiki:6.0_Addons#Addon_List).

{{-}}

## The FAQ does not solve my problem.

Please feel free to contact us through any of the official methods listed on the “[Contact](wiki:Contact)” page. {{-}}

[Category:Documentation](wiki:Category:Documentation)
