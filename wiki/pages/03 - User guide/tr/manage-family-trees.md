---
title: Gramps 6.0 Wiki Manual - Manage Family Trees/tr
categories:
- Documentation
- Stub
managed: false
source: wiki-scrape
wiki_revid: 127180
wiki_fetched_at: '2026-05-30T20:57:48Z'
lang: tr
---

{{#vardefine:chapter\|5}} {{#vardefine:figure\|0}} Gramps'in günlük kullanımının ayrıntılı keşfi. Bu Bölümde, soy ağaçlarınızı nasıl yönetebileceğinize ve verilerinizi diğer soy araştırmacılarıyla nasıl paylaşabileceğinize ilişkin ayrıntılı bir genel bakış sunuyoruz.

## Yeni bir Soyağacı başlatmak

![[_media/Menubar-FamilyTrees-overview-FamilyTree-Loaded-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menubar - "Family Trees" - overview example]]

To start a new Family Tree, choose the menu or select the toolbar button or use the [keybinding](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings) . This will open the manager window.

Select the button and to add a new Family Tree entry to the list of Family Trees. To change its name from the default *`Family Tree 1`*, select the name and press the button then type in a new name.

To open the new, empty Family Tree select the Family Tree and either double click or press the button to load. {{-}} ![[_media/FamilyTrees-ManageDatabases-icon-toolbar-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure\|{{#expr:{{#var:figure}}+1}}}} Manage databases - icon on toolbar (Same as using menu )]] {{-}} ![[_media/ConnectToARecentDatabase-icon-toolbar-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure\|{{#expr:{{#var:figure}}+1}}}} Connect to a recent database - icon drop down on toolbar menu]] {{-}}

### Soyağaçları yönetici penceresi

Family Trees are what Gramps calls the database structure used to store and organize genealogical data. You need to create a Family Tree before any genealogical data can be entered, [restored from a backup achive](wiki:How_to_restore_a_backup) or [imported from other software](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees#Importing_data).

Family Trees can be renamed, converted to other database backends, repaired or deleted. A 'mistake' here won't be unrecoverable. (The biggest potential mistake, an accidental Deletion, requires a confirmation.)

![[_media/FamilyTreesManager-window-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Family Trees" manager window]]

Clicking the button brings up the manager windows this allows you to work with and manage the Family Trees found within the specific Gramps [Family Tree Database path](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Family_Tree) directory.

The Family Tree Manager window allows the you to create a new Family tree, rename an existing Family tree, delete a Family tree, or load a Family tree or check information) about the Family tree. All the names of your Family trees appear in the list. If a Family tree is open, an icon will appear next to the name in the status column. The Database Type as well an indication of the date and time your family tree was *Last accessed*' is shown.

- yeni bir soyağacı oluşturur.

- seçilen soyağacıyla ilgili bilgileri gösterir.

- seçtiğiniz Soyağacını silmeniz için son bir uyarıya onay vermenizi isteyecektir.

- seçilen mevcut Soyağacının adını değiştirir.

- seçilen mevcut Soyağacını kapatır.

- seçilen soyağacını dönüştürür. Bu seçenek, yalnızca soyağacı bu veri tabanında olduğunda geçerlidir. Bakınız: [BSDDB](wiki:Gramps_Glossary/tr#bsddb) [eski Soyağacını](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees/tr#BSDDB_Soyağacını_SQLite&#39;a_Dönüştürme) [SQlite](wiki:Gramps_Glossary/tr#sqlite)'a dönüştürme

- seçilen mevcut Soyağacı için yalnızca Gramps bir sorun tespit ederse kullanılabilir.

- seçeneği yalnızca [GNU Revizyon Kontrol Sistemi](http://www.gnu.org/software/rcs/) (RCS) kuruluysa görünür olur.

- sadece düğmesiyle birlikte kullanılır ve seçenek yalnızca [GNU Revizyon Kontrol Sistemi](http://www.gnu.org/software/rcs/) (RCS) kuruluysa görünür olur.

- \- çevrimiçi kılavuzun bu bölümünü gösteren sayfayı varsayılan tarayıcıda açar.

- \- yöneticisi pencerelerini kapatır.

- seçili mevcut Soyağacını çalışan belleğe açar ve diğer kullanıcıların çakışan düzenlemeler yapamaması için veri tabanı dosyasını kilitler.

{{-}}

## Opening a Family Tree

To open a Family Tree, either choose the menu or click the Toolbar button. The will appear and you will see a list of all the Family Trees known to Gramps. In the column an icon (looks like an open folder) will display beside any Family Tree that is currently open. Select the tree you want to open, and open it by selecting the button. Alternatively you can double-click on the desired Family Tree.

To open a recently accessed Family Tree, choose either the menu or the down arrow next to the Toolbar button and select the Family Tree from the list.

### Read Only Mode

The Tools menu will not be available.

## Saving changes to your Family Tree

Gramps saves your changes as soon as you apply them. This means, for example, that any time you click when using Gramps, your changes are immediately recorded and saved. There is no separate "save" command.

You can undo changes you have made by selecting the menu . If you select this command repeatedly, your most recent changes will be undone one at a time. To roll back multiple commands at a time, you can use the menu dialog.

If you want to return your Family Tree to the way it was when you opened it, select the menu . (This is just like quitting without saving in other programs.)

If you would like to save a copy of your Family Tree under a different name, you will need to export it and then import it into a new Family Tree. The *Gramps XML* database format is recommended for this purpose.

## Opening a GEDCOM or XML database

Gramps allows you to open certain databases that have not been saved in Gramps own file format from the command line, see [Command line references](wiki:Gramps_6.0_Wiki_Manual_-_Command_Line#Opening_options). These include XML and GEDCOM databases. But you should be aware that if the XML or GEDCOM database is relatively large, you will encounter performance problems, and in the event of a crash your data can be corrupted. Hence, it is normally better to create a new Gramps family tree (database) and import your XML/GEDCOM data into it.

## Deleting a Family Tree

Select the family tree you want removed, and click the button.

This will **completely** remove the tree, with no possibility to retrieve the data. Consider taking a backup of your data by exporting to the GRAMPS XML format, and storing that file.

## Renaming a Family Tree

You can rename a Family Tree (or an archive of it) by selecting the tree you want to rename and clicking . You can also click on the name in the list of trees.

In either case, you just type in the new name to have it take effect.

## Soyağacını Yedekle

The safest way to backup your Gramps Family Tree is to export without privacy options and filters to **Gramps XML** format (or **Gramps XML Package** to include items from your Gallery) and copy the resultant file to a safe place, preferably in a different building.

### Yedekleme iletişim kutusu

![[_media/MakeBackup-GrampsXML-Backup-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Making a backup]]

From the menu select

The window will appear.

You can enter the where the backup should be stored manually or using the button to bring up the dialog.

You can enter a name manually or use the automatically generated file name.

You can either choose to *Include* or **Exclude**(default) the .

{{-}}

- You can use the Archive feature (see next section) to store snapshots of your Family Tree. These snapshots can be used as simple backups, very useful if you want to try something that you might later want to undo. However this method should not be used for standard backups, as it will not survive a hard disk crash or most of the other disasters that can befall a computer.

<!-- -->

- *For advanced users:* each database is stored in its own subdirectory under ~/.gramps. Although a manual backup can be made by backing up this directory, it is not recommended. It is strongly recommended that you please use a Gramps XML backup instead.

### Backup on exit

In preferences tab, Gramps can be set to create a backup when Gramps exits. Note that this only creates a backup for the open family tree. If the tree is closed before exiting Gramps, no backup is created.

- [Settings Family Tree](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Family_Tree)

### Automatic backup

In preferences tab, Gramps can be set to create a backup every 15, 30 or 60 minutes.

See also:

- [Settings Family Tree](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Family_Tree)
- [Advanced backup filename setting](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Advanced_backup_filename_setting) - Where you can also define the naming pattern for the backup filename.
- [Backup omissions](wiki:Template:Backup_Omissions) - what is not included during a backup

## Archiving a Family Tree

You can your family trees with Gramps to retain a copy before any major changes and be able to return to a known version.

To make an archive :

![[_media/ManageFamilyTrees-Archive-RevisionComment-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Archive a Family Tree example]]

1.  load your Family Tree.
2.  click on the Toolbar button (it displays when you hover over it).
3.  click on the family tree you have just loaded: the button should appear.
4.  click on and you will be able to enter in the dialog a *Version description* for your archive.

After archiving, the list of family trees will now show your original family tree with a right-pointing triangle on its left.

- Click on the triangle to display the archive name.(Click again to collapse the archive list).

Archives can be , and .

{{-}}

## Extracting a Family Tree Archive

![[_media/ManageFamilyTrees-Archive-Selected-to-Extract-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} (Manage)"Family Trees" dialog - Archive selected ready to "Extract" - example]]

To retrieve a version of a previously archived family tree in the "Family Tree" manager highlight the archive you want to restore, and select the button.

{{-}} ![[_media/ManageFamilyTrees-Archive-Extracted-version-selected-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} (Manage)&quot;Family Trees&quot; dialog - Archived version extracted and selected - example]]

The archive will then be restored into a new Family Tree and be listed in the family tree manager.

The Family Tree name is based on the original name and the archive name eg: *<name of original tree>`:`<name of archive>*.(see also [Archiving a Family Tree](#Archiving_a_Family_Tree))

This can be a useful way of preserving an archive, because archives disappear if the originating tree is deleted; and *'they are not incorporated into a Gramps XML export of the family tree*. {{-}}

## Unlocking a Family Tree

![[_media/FamilyTreesManager-Dialog-ShowingLocked-Sample-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Family Trees (Manager) - Dialog - Showing Locked &quot;Sample&quot; Family Tree]] Gramps is a single-user database application and identifies Tree database files as busy with a ![[_media/22x22-gramps-lock.png]]'lock' when in use. As Gramps opens a tree, it drops a `lock` file (which lists the username and domain) in the tree's subfolder in the `grampsdb` folder of the [User Directory](wiki:Gramps_6.0_Wiki_Manual_-_User_Directory). Gramps refuses to let you (or anyone else) open that Tree at the same time. A second instance of Gramps will be able to open another family tree, but any tree that is already open will appear with the lock icon in the Status column of the Manage Family Trees dialog. Closing the tree in the first copy of Gramps deletes the lock file and will make the tree available to be opened in the second instance.

If you *could* open the same Family Tree in two instances of Gramps at once, it is likely your data would be damaged as the two overwrite each other's work.

#### See also:

- [Command Line:Force unlock option](wiki:Gramps_6.0_Wiki_Manual_-_Command_Line#Force_unlock_option)

### Break the lock on the "Family Tree name" database? dialog

![[_media/ErrorParsingArguments-dialog-DatabaseIsLocked-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}}Error parsing arguments - dialog - Database is locked example]] In the unlikely event that Gramps crashes, the family tree will be left in a locked state (indicated by a ![[_media/22x22-gramps-lock.png]]lock icon in the column next to the Family Tree name)

To unlock the Family Tree during startup

- If the [Family Tree Preferences](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Family_Tree) have been set to open a tree automatically on startup, then you will see the **Error parsing arguments** dialog which remarks that the **Database is locked**. Click on the button then choose from the menu.
- Otherwise, the will appear automatically as Gramps starts.

{{-}} ![[_media/Break-the-lock-on-the-database-Dialog-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Break the lock on the &quot;Sample&quot; database? - Dialog - example]]Choose the locked family tree and then click the button. The **Break the lock on the '\[Family Tree name\]' database?** dialog will be shown.

Click the button and the window should show that the lock icon has gone.

Choose the previously locked family tree and then click the button to continue your work. {{-}}

## Repairing a damaged Family Tree

![[_media/FamilyTreesManager-Dialog-ShowingRedErrorStatusIcon-Sample-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Family Trees (Manager) - Dialog - Showing Red Error Status Icon for "Sample" Family Tree]]

Should your Family Tree become damaged or corrupted in some way, Gramps Family Tree Manager will display a red Error icon in the column.

To have Gramps attempt to repair the damage, select the Family Tree and then click the button.

This will attempt to rebuild your Family Tree from the backup files that are automatically created on exit.

See also:

- [Recover corrupted family tree](wiki:Recover_corrupted_family_tree)

{{-}}

## BSDDB Soyağacını SQLite'a Dönüştürme

![[_media/ManageFamilyTrees-Convert-the-database-dialog-example-51.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} <strong>Convert the 'Family Tree Name' database?</strong> dialog with <em>Family Trees (Manager)</em> - Dialog shown in background]]

If you have an older legacy [BSDDB](wiki:Gramps_Glossary#bsddb) format **Database Type** shown for any of your family tree's in the *Family Trees (Manager)* - Dialog, then selecting a family tree in the *Family Trees (Manager)* - Dialog will show the button as available.

When ready select the button and the dialog will be shown with the message **Do you wish to convert this family tree into a SQLite database?** you can select to stop or to start the process, once completed the *Family Trees (Manager)* - Dialog will show a new entry for the converted copy of your Family tree but with the *Database Type* of SQLite, you should then open and backup the converted family tree.

You may then rename the original BSDDB family tree with the word **OLD** or you can Delete it to avoid confusion, then you can rename the new SQLite database.

{{-}}

## Verileri içe aktarma

Importing allows you to transfer data from other genealogy programs into a Gramps Family Tree. Gramps can import data from the following formats:

- [Gramps XML](#Gramps_XML_and_XML_Package_import) (`.gramps` file extension) Gramps native data exchange format in uncompressed text and [gzip](https://wikipedia.org/wiki/Gzip) compressed
- [Gramps XML Package](#Gramps_XML_and_XML_Package_import) (`.gpkg` file extension) Gramps [.tar.gz](https://wikipedia.org/wiki/.tar.gz) archive compressed backup format
- [GRAMPS V2.x database](#GRAMPS_V2.x_database_import) (`.grdb` file extension)
- [CSV Spreadsheet](#Gramps_CSV_import) - comma separated values (`.csv` file extension)
- [GEDCOM](#GEDCOM_import) (`.ged` file extension) de facto standard file format for data interchange between genealogy programs
- GeneWeb (`.gw` file extension) - [GeneWeb](https://en.wikipedia.org/wiki/GeneWeb) is genealogy software with a web interface.
- Pro-Gen (`.def` file extension) - [Pro-Gen](https://www.pro-gen.nl/gbhome.htm) has been very popular in the Netherlands and North-West Germany. It is often used by people who started collecting and storing data as early as 1989. This was a DOS based program which has been patched to work with Win 10.
- vCard (`.vcf` file extension) - [Virtual Contact File](https://wikipedia.org/wiki/VCard) is a file format standard for electronic business cards.
- JSON Import (`.json` file extension) - [JavaScript Object Notation](https://www.json.org/) is a lightweight data-interchange format.
- SQLite Import (`.sql` file extension) - [SQLite database format](https://www.sqlite.org/fileformat.html)

### Import Family Tree dialog

![[_media/Importfamilytree-dialog-51.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Import Family Tree - dialog example]]

First create a [new and empty Family Tree](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees#Starting_a_new_Family_Tree). Then select the menu or use the [keybinding](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings#2) to import data or restore a previously saved Gramps Family Tree (from an older version of Gramps or the current version) the **** dialog will open, asking you to specify the file you wish to import.

![[_media/UndoHistoryWarning-Import-dialog-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Import warning dialog]]As you attempt to import into a Family Tree that is ***not empty***, the dialog will open. This reminds you make a backup before importing. Create a new Family Tree instead, unless you are knowingly attempting to merge data.

Gramps uses a [GTK File Chooser](https://developer.gnome.org/gtk3/stable/GtkFileChooser.html) for selecting the data file to be exported. The basic options for navigating to a file are familiar and obvious.

The default display option for the filepath is to show each folder level as clickable [breadcrumb navigation](https://en.wikipedia.org/wiki/Breadcrumb_navigation). The path can be typed in an editable text box by pressing the keybinding.

The file type extension will normally allow the option to expect a particular pattern of data to be converted to the native database format. You can override this by choosing a different **** options. The list of files may be filtered by changing from the option.

When planning to use the import repeatedly (for ongoing updates or including genealogy research), you can [customize the dialog](https://gramps.discourse.group/t/need-help-doing-a-cross-os-linux-mac-verification/1068/5) by adding buttons for bookmarked folder paths. Right-click on a folder name and choose from the pop-up menu.

### GRAMPS V2.x database import

GRAMPS V2.x database (.grdb): Prior to Gramps Version 3.0, this native Gramps database format was a specific form of the Berkeley database (BSDDB) with a special structure of data tables. This format was binary and architecture-dependent. It was very quick and efficient, but not generally portable across computers with different binary architecture (e.g. i386 vs. alpha).

Import from the GRAMPS V2.x database format is only supported by Gramps version 3.0.x. Import of V2.x into Gramps V3.0.x will not loose any data.

#### Moving a Gramps 2.2 databases to Gramps 3.x

To move your Gramps data from version 2.x to version 6.0.x you must import the v2.x database into an earlier Gramps v3.0.x program and then either save the database and import it into Gramps 6.0.x, or export the database in [XML](wiki:XML) format from the earlier Gramps version and import it into Gramps 6.0.x.

Please refer to the [User Manual](wiki:User_manual_translations) for earlier versions of Gramps for instructions on the import of v2.x databases into Gramps v3.x.

{{-}}

### Gramps XML and XML Package import

The Gramps [XML](wiki:XML) and Gramps [XML](wiki:XML) Package database are the native Gramps formats. There is no risk of information loss when importing (restore) from or exporting to these formats.

- Gramps [XML](wiki:XML) (.gramps): The Gramps [XML](wiki:XML) file is the standard Gramps data-exchange and backups format, and was also the default working-database format for older (pre 2.x) versions of Gramps. Unlike the GRAMPS V2.x grdb format, it is architecture independent and human-readable. The database may also have references to non-local (external) media objects, therefore it is not guaranteed to be completely portable (for full portability including media objects in the Gramps [XML](wiki:XML) package (.gpkg) should be used). The Gramps [XML](wiki:XML) database is created by exporting (Menu ) to that format.

<!-- -->

- Gramps [XML](wiki:XML) package (.gpkg): The Gramps [XML](wiki:XML) package is a **compressed** archive containing the Gramps [XML](wiki:XML) file and all [media](wiki:Gramps_Glossary#media) objects (images, sound files, etc.) to which the database refers. Because it contains all the media objects, this format is completely portable. The Gramps [XML](wiki:XML) package is created by exporting ( Menu ) data in that format.

If you import information from another Gramps database or Gramps [XML](wiki:XML) database, you will see the progress of the operation in the progress bar of Gramps main window. When the import finishes, a feedback window shows the number of imported objects. If the imported data originates from the very family tree in which you import the data, the import feedback gives suggestions about what could be merged; the merge is **not** done automatically for you. If you want to merge basic genealogy data automatically, consider CSV Spreadsheet Export/Import.

### Gramps CSV içe aktarma

- Gramps CSV E-tablo biçimi, Gramps verilerinizin bir alt kümesinin basit bir elektronik tablo biçiminde içe ve dışa aktarılmasına olanak tanır. Daha fazla bilgi için [CSV İçe ve Dışa Aktarma](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees:_CSV_Import_and_Export/tr) bölümüne bakın.

### GEDCOM import

First create a [new empty Family Tree](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees#Starting_a_new_Family_Tree). Then select the menu or the [keybinding](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings#2) then use the dialog to select the GEDCOM file you want to import, depending on the type of GEDCOM you may then see the dialog.

When you import information from GEDCOM, Gramps main window will show you a [progress bar](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window#Status_Bar_and_Progress_Bar). When the GEDCOM import finishes, the window and the **** windows show any results or warnings.

{{-}}

#### GEDCOM Encoding dialog

![[_media/GEDCOM-Encoding-dialog-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} GEDCOM Encoding - dialog]]

The dialog will be shown when the GEDCOM file you are importing has identified itself as using the ANSEL encoding format. Sometimes, this is in error. If after the GEDCOM is imported you notice that your data contains unusual characters, undo the import, and override the character set by selecting a different encoding from the available list.

- **default**
- ANSEL
- ANSI (iso-8859-1)
- ASCII
- UTF8

{{-}}

#### Import Statistics dialog

![[_media/ImportStatistics-dialog-example-GrampXML-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Import Statistics - dialog]] Shows details of the import statistics. {{-}}

#### GEDCOM import report dialog

![[_media/GEDCOM-import-report-result-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} GEDCOM import report - example results.]]

The **** details most of the GEDCOM lines that were either ignored or could not be understood. These are most likely because they are not part of the GEDCOM 5.6.0 standard. (See [Addon:GEDCOM Extensions](wiki:Addon:GEDCOM_Extensions).) The contents of the GEDCOM line (or lines where there are continuation lines) are also shown. In some cases, the lines may not be exactly what is contained in the input GEDCOM file, because the line is reconstructed following some processing. {{-}}

##### Reading the report

![[_media/Source-Note-GEDCOMImportNote-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} GEDCOM import note indicating omitted data attached to "Source&gt;Note"(data from "GEDitCOM" - "GEDCOM 5.5 Torture Test Files")]]

Gramps uses a more advanced 'data model' than GEDCOM, therefore some data in GEDCOM cannot be imported into Gramps. (See [Gramps and GEDCOM](wiki:Gramps_and_GEDCOM).) The main exceptions are:

- Some GEDCOM attribute structures are treated as Gramps and therefore many of the GEDCOM Primitive Elements cannot be stored.
- The DATA elements of a SOURCE_RECORD (indicating the events recorded and responsible agency) are ignored.
- Any source citations on notes are ignored.
- Many GEDCOM Primitive Elements do not have exactly corresponding data elements in Gramps, and they are therefore stored as with appropriate names, normally the GEDCOM tag. This applies particularly to the header, submitter and submission GEDCOM records and particular fields like REFN, RFN, RIN and AFN.

Where data is listed as 'ignored', its omission is reported in the feedback at the end of import, and it is included in a attached to a relevant object with a custom type of . See, for example, the Source object in the example screenshot.

Where data is listed as 'silently ignored', it is not reported and not included in a note. At present this may be regarded as something that has been missed by Gramps and should be raised as an issue . {{-}}

#### GEDCOM import limitations

This section describes any GEDCOM data that cannot be directly represented in Gramps, and how it is handled. For additional information on the limits of GEDCOM imports (and exports), please read the section on [Gramps and GEDCOM](wiki:Gramps_and_GEDCOM).

##### HEADer, SUBMitter and SUBmissioN

Gramps has no direct representation of this data, and hence all information there has to be stored in other objects. Depending on a [General preferences](wiki:Gramps_6.0_Wiki_Manual_-_Settings#General) setting, a 'default source' object may be created. If this is created, then much of the data is stored in that , or in attached to that source.

###### HEADer

`   HEADER:=`  
`        n HEAD                                          {1:1}`  
`          +1 SOUR `<APPROVED_SYSTEM_ID>`                  {1:1}  (Data item of the 'default source')`  
`            +2 VERS `<VERSION_NUMBER>`                    {0:1}  (Data item of the 'default source')`  
`            +2 NAME `<NAME_OF_PRODUCT>`                   {0:1}  (Data item of the 'default source')`  
`            +2 CORP `<NAME_OF_BUSINESS>`                  {0:1}  (Repository of the 'default source')`  
`              +3 <`<ADDRESS_STRUCTURE>`>                  {0:1}  (Repository of the 'default source')`  
`            +2 DATA `<NAME_OF_SOURCE_DATA>`               {0:1}  (Data item of the 'default source')`  
`              +3 DATE `<PUBLICATION_DATE>`                {0:1}  (Data item of the 'default source')`  
`              +3 COPR `<COPYRIGHT_SOURCE_DATA>`           {0:1}  (Data item of the 'default source')`  
`          +1 DEST `<RECEIVING_SYSTEM_NAME>`               {0:1*} (Data item of the 'default source')`  
`          +1 DATE `<TRANSMISSION_DATE>`                   {0:1}  (Data item of the 'default source')`  
`            +2 TIME `<TIME_VALUE>`                        {0:1}  (Data item of the 'default source')`  
`          +1 SUBM @`<XREF:SUBM>`@                         {1:1}  (Data item of the 'default source')`  
`                                                               (Also used to determine the SUBMITTER_RECORD)`  
`                                                               (that should be stored as the database owner)`  
`          +1 SUBN @`<XREF:SUBN>`@                         {0:1}  (ignored)`  
`          +1 FILE `<FILE_NAME>`                           {0:1}  (Data item of the 'default source')`  
`          +1 COPR `<COPYRIGHT_GEDCOM_FILE>`               {0:1}  (stored as the Publication information of the 'default source')`  
`          +1 GEDC                                       {1:1}`  
`            +2 VERS `<VERSION_NUMBER>`                    {1:1}  (Data item of the 'default source')`  
`            +2 FORM `<GEDCOM_FORM>`                       {1:1}  (Data item of the 'default source')`  
`          +1 CHAR `<CHARACTER_SET>`                       {1:1}  (Data item of the 'default source')`  
`            +2 VERS `<VERSION_NUMBER>`                    {0:1}  (Data item of the 'default source')`  
`          +1 LANG `<LANGUAGE_OF_TEXT>`                    {0:1}  (Data item of the 'default source')`  
`          +1 PLAC                                       {0:1}`  
`            +2 FORM `<PLACE_HIERARCHY>`                   {1:1}  (see below)`  
`          +1 NOTE `<GEDCOM_CONTENT_DESCRIPTION>`          {0:1}  (note attached to the 'default source')`  
`            +2 [CONT|CONC] `<GEDCOM_CONTENT_DESCRIPTION>` {0:M}`  
`            `  
`   * NOTE: Submissions to the Family History Department for Ancestral`  
`     File submission or for clearing temple ordinances must use a`  
`     DESTination of ANSTFILE or TempleReady.`

The PLAC FORM is stored internally and used to govern the interpretation of places (in accordance with the GEDCOM specification).

###### SUBmissioN

The SUBMISSION_RECORD (there should be only one, but this is not checked) is stored as a item of the 'default source'

`    SUBMISSION_RECORD:=`  
`        n @`<XREF:SUBN>`@ SUBN                            {1:1]`  
`          +1 SUBM @`<XREF:SUBM>`@                         {0:1}`  
`          +1 FAMF `<NAME_OF_FAMILY_FILE>`                 {0:1}`  
`          +1 TEMP `<TEMPLE_CODE>`                         {0:1}`  
`          +1 ANCE `<GENERATIONS_OF_ANCESTORS>`            {0:1}`  
`          +1 DESC `<GENERATIONS_OF_DESCENDANTS>`          {0:1}`  
`          +1 ORDI `<ORDINANCE_PROCESS_FLAG>`              {0:1}`  
`          +1 RIN `<AUTOMATED_RECORD_ID>`                  {0:1}`

###### SUBMitter

SUBMITTER_RECORDs (there may be more than one) are stored as records attached to the 'default source' except as indicated in bold below. The SUBMITTER_RECORD that corresponds with the SUBM record in the HEADER is used to set the [database owner](wiki:Gramps_6.0_Wiki_Manual_-_Tools#Edit_Database_Owner_Information) and can be copied to the [Researcher Information](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Researcher) tab if required.

`   SUBMITTER_RECORD:=`  
`        n @`<XREF:SUBM>`@   SUBM                          {1:1}`  
`          +1 NAME `<SUBMITTER_NAME>`                      {1:1}`  
`          +1 <`<ADDRESS_STRUCTURE>`>                      {0:1}`  
`          `**`+1 <`<MULTIMEDIA_LINK>`> {0:M}`**  
`          `**`+1 LANG `<LANGUAGE_PREFERENCE>` {0:3}`**  
`          `**`+1 RFN `<SUBMITTER_REGISTERED_RFN>` {0:1}`**  
`          `**`+1 RIN `<AUTOMATED_RECORD_ID>` {0:1}`**  
`          +1 <`<CHANGE_DATE>`>                            {0:1}`

- Mutimedia link is ignored
- LANG is ignored
- RFN and RIN are ignored

##### INDIvidual

The INDIVIDUAL_RECORD is stored as a Gramps record, except as indicated in bold below.

`   INDIVIDUAL_RECORD: =`  
`        n @`<XREF:INDI>`@  INDI                           {1:1}`  
`          +1 RESN `<RESTRICTION_NOTICE>`                  {0:1}`  
`          +1 <`<PERSONAL_NAME_STRUCTURE>`>                {0:M}`  
`          +1 SEX `<SEX_VALUE>`                            {0:1}`  
`          +1 <`<INDIVIDUAL_EVENT_STRUCTURE>`>             {0:M}`  
`          `**`+1 <`<INDIVIDUAL_ATTRIBUTE_STRUCTURE>`> {0:M}`**  
`          +1 <`<LDS_INDIVIDUAL_ORDINANCE>`>               {0:M}`  
`          +1 <`<CHILD_TO_FAMILY_LINK>`>                   {0:M}`  
`          +1 <`<SPOUSE_TO_FAMILY_LINK>`>                  {0:M}`  
`          `**`+1 SUBM @`<XREF:SUBM>`@ {0:M}`**  
`          +1 <`<ASSOCIATION_STRUCTURE>`>                  {0:M}`  
`          +1 ALIA @`<XREF:INDI>`@                         {0:M}`  
`          `**`+1 ANCI @`<XREF:SUBM>`@ {0:M}`**  
`          `**`+1 DESI @`<XREF:SUBM>`@ {0:M}`**  
`          +1 <`<SOURCE_CITATION>`>                        {0:M}`  
`          +1 <`<MULTIMEDIA_LINK>`>                        {0:M}`  
`          +1 <`<NOTE_STRUCTURE>`>                         {0:M}`  
`          +1 RFN `<PERMANENT_RECORD_FILE_NUMBER>`         {0:1}`  
`          +1 AFN `<ANCESTRAL_FILE_NUMBER>`                {0:1}`  
`          +1 REFN `<USER_REFERENCE_NUMBER>`               {0:M}`  
`            `**`+2 TYPE `<USER_REFERENCE_TYPE>` {0:1}`**  
`          +1 RIN `<AUTOMATED_RECORD_ID>`                  {0:1}`  
`          +1 <`<CHANGE_DATE>`>                            {0:1}`  
`   `

- Link to submitter, ancestor interest and descendent interest indicators are silently ignored.
- The alias indicator ("An indicator to link different record descriptions of a person who may be the same person") is stored as an called 'Alias'.
- The REFN and REFN:TYPE are stored as of the , but if there is more than one REFN, it may not be clear which TYPE is associated with which REFN.

Handling of the INDIVIDUAL_ATTRIBUTE_STRUCTURE is rather complicated. The following tags:

- EDUC (Scholastic achievement),
- NMR (Count of marriages),
- OCCU (Occupation),
- PROP (Possessions),
- RELI (Religious affiliation),
- RESI and
- TITL (Nobility title)

are all treated as Gramps s and the associated information is stored in the event structure. The details following the main tag (shown in brackets in the list above) are stored as the of the . The <EVENT_DESCRIPTOR> following the TYPE tag will overwrite the if the <EVENT_DESCRIPTOR> is not the attribute name.

The following tags:

- CAST (Caste name),
- DSCR (Physical description),
- INDO (National ID Number),
- NATI (National or tribal origin),
- NCHI (Count of Children) and
- SSN (Social Security Number)

are all treated as Gramps s and most of the fields except the details following the main tag (shown in brackets in the list above), the source citation and the note structure are ignored, as indicated in bold below.

`   INDIVIDUAL_ATTRIBUTE_STRUCTURE: =`  
`        n  CAST `<CASTE_NAME>`                            {1:1}`  
`          +1 <`<EVENT_DETAIL>`>                           {0:1}`  
`             etc.`  
`   `  
`   EVENT_DETAIL: =`  
`        `**`n TYPE `<EVENT_DESCRIPTOR>` {0:1}`**  
`        `**`n DATE `<DATE_VALUE>` {0:1}`**  
`        `**`n <`<PLACE_STRUCTURE>`> {0:1}`**  
`        `**`n <`<ADDRESS_STRUCTURE>`> {0:1}`**  
`        `**`n AGE `<AGE_AT_EVENT>` {0:1}`**  
`        `**`n AGNC `<RESPONSIBLE_AGENCY>` {0:1}`**  
`        `**`n CAUS `<CAUSE_OF_EVENT>` {0:1}`**  
`        n  <`<SOURCE_CITATION>`>                          {0:M}`  
`          +1 <`<NOTE_STRUCTURE>`>                         {0:M}`  
`          +1 <`<MULTIMEDIA_LINK>`>                        {0:M}`  
`        `**`n <`<MULTIMEDIA_LINK>`> {0:M}`**  
`        n  <`<NOTE_STRUCTURE>`>                           {0:M}`  
`        `  
`        `

- Individual attribute structure, type, date, place structure, address structure, age, agency, cause and multimedia link are all ignored.

##### FAM_RECORD

The FAM_RECORD is stored as a Gramps record.

`   FAM_RECORD:=`  
`        n @`<XREF:FAM>`@   FAM                            {1:1}`  
`          +1 <`<FAMILY_EVENT_STRUCTURE>`>                 {0:M}`  
`          +1 HUSB @`<XREF:INDI>`@                         {0:1}`  
`          +1 WIFE @`<XREF:INDI>`@                         {0:1}`  
`          +1 CHIL @`<XREF:INDI>`@                         {0:M}`  
`          +1 NCHI `<COUNT_OF_CHILDREN>`                   {0:1}`  
`          +1 SUBM @`<XREF:SUBM>`@                         {0:M}`  
`          +1 <`<LDS_SPOUSE_SEALING>`>                     {0:M}`  
`          +1 <`<SOURCE_CITATION>`>                        {0:M}`  
`          +1 <`<MULTIMEDIA_LINK>`>                        {0:M}`  
`          +1 <`<NOTE_STRUCTURE>`>                         {0:M}`  
`          +1 REFN `<USER_REFERENCE_NUMBER>`               {0:M}`  
`            +2 TYPE `<USER_REFERENCE_TYPE>`               {0:1}`  
`          +1 RIN `<AUTOMATED_RECORD_ID>`                  {0:1}`  
`          +1 <`<CHANGE_DATE>`>                            {0:1}`

- The link to submitter is silently ignored.
- The REFN and REFN:TYPE are stored as of the , but if there is more than one REFN, it may not be clear which TYPE is associated with which REFN.

##### SOURCE_RECORD

The SOURCE_RECORD is stored as a Gramps record, except as indicated in bold below.

`   SOURCE_RECORD:=`  
`        n @`<XREF:SOUR>`@ SOUR                            {1:1}`  
`          `**`+1 DATA {0:1}`**  
`            `**`+2 EVEN `<EVENTS_RECORDED>` {0:M}`**  
`              `**`+3 DATE `<DATE_PERIOD>` {0:1}`**  
`              `**`+3 PLAC `<SOURCE_JURISDICTION_PLACE>` {0:1}`**  
`            `**`+2 AGNC `<RESPONSIBLE_AGENCY>` {0:1}`**  
`            `**`+2 <`<NOTE_STRUCTURE>`> {0:M}`**  
`          +1 AUTH `<SOURCE_ORIGINATOR>`                   {0:1}`  
`            +2 [CONT|CONC] `<SOURCE_ORIGINATOR>`          {0:M}`  
`          +1 TITL `<SOURCE_DESCRIPTIVE_TITLE>`            {0:1}`  
`            +2 [CONT|CONC] `<SOURCE_DESCRIPTIVE_TITLE>`   {0:M}`  
`          +1 ABBR `<SOURCE_FILED_BY_ENTRY>`               {0:1}`  
`          +1 PUBL `<SOURCE_PUBLICATION_FACTS>`            {0:1}`  
`            +2 [CONT|CONC] `<SOURCE_PUBLICATION_FACTS>`   {0:M}`  
`          +1 TEXT `<TEXT_FROM_SOURCE>`                    {0:1}`  
`            +2 [CONT|CONC] `<TEXT_FROM_SOURCE>`           {0:M}`  
`          +1 <`<SOURCE_REPOSITORY_CITATION>`>             {0:1}`  
`          +1 <`<MULTIMEDIA_LINK>`>                        {0:M}`  
`          +1 <`<NOTE_STRUCTURE>`>                         {0:M}`  
`          +1 REFN `<USER_REFERENCE_NUMBER>`               {0:M}`  
`            +2 TYPE `<USER_REFERENCE_TYPE>`               {0:1}`  
`          +1 RIN `<AUTOMATED_RECORD_ID>`                  {0:1}`  
`          +1 <`<CHANGE_DATE>`>                            {0:1}`

- DATA and its subsidiary records are ignored

##### REPOSITORY_RECORD

The REPOSITORY_RECORD is stored as a Gramps record, except as indicated in bold below.

`   REPOSITORY_RECORD: =`  
`        n @`<XREF:REPO>`@ REPO                            {1:1}`  
`          +1 NAME `<NAME_OF_REPOSITORY>`                  {0:1}`  
`          +1 <`<ADDRESS_STRUCTURE>`>                      {0:1}`  
`          +1 <`<NOTE_STRUCTURE>`>                         {0:M}`  
`          `**`+1 REFN `<USER_REFERENCE_NUMBER>` {0:M}`**  
`            `**`+2 TYPE `<USER_REFERENCE_TYPE>` {0:1}`**  
`          `**`+1 RIN `<AUTOMATED_RECORD_ID>` {0:1}`**  
`          +1 <`<CHANGE_DATE>`>                            {0:1}`

- REFN, REFN:TYPE and RIN are ignored

##### MULTIMEDIA_RECORD

The MULTIMEDIA_RECORD is stored as a Gramps record, except as indicated in bold below.

`   MULTIMEDIA_RECORD:=`  
`        n @`<XREF:OBJE>`@ OBJE                            {1:1}`  
`          +1 FORM `<MULTIMEDIA_FORMAT>`                   {1:1}`  
`          +1 TITL `<DESCRIPTIVE_TITLE>`                   {0:1}`  
`          +1 <`<NOTE_STRUCTURE>`>                         {0:M}`  
`          +1 <`<SOURCE_CITATION>`>                        {0:M}`  
`          `**`+1 BLOB {1:1}`**  
`            `**`+2 CONT `<ENCODED_MULTIMEDIA_LINE>` {1:M}`**  
`          +1 OBJE @`<XREF:OBJE>`@     /* chain to continued object */  {0:1}`  
`          `**`+1 REFN `<USER_REFERENCE_NUMBER>` {0:M}`**  
`            `**`+2 TYPE `<USER_REFERENCE_TYPE>` {0:1}`**  
`          `**`+1 RIN `<AUTOMATED_RECORD_ID>` {0:1}`**

- It is expected that there will be a 'FILE' tag to indicate the file holding the multimedia object. This usage is taken from GEDCOM 5.6.0, but the ability in GEDCOM 5.6.0 to have more than one <MUTIMEDIA_FILE_REFN> and having the FORM, TYPE and TITL subsidiary to the FILE gedcom_line is not supported (a later FILE may overwrite an earlier one - there is no error checking).
- BLOB is ignored
- REFN, REFN:TYPE and RIN are ignored

##### NOTE_RECORD

The NOTE_RECORD is stored as a Gramps record, except as indicated in bold below.

`   NOTE_RECORD:=`  
`        n @`<XREF:NOTE>`@ NOTE `<SUBMITTER_TEXT>`           {1:1}`  
`          +1 [ CONC | CONT] `<SUBMITTER_TEXT>`            {0:M}`  
`          `**`+1 <`<SOURCE_CITATION>`> {0:M}`**  
`          `**`+1 REFN `<USER_REFERENCE_NUMBER>` {0:M}`**  
`            `**`+2 TYPE `<USER_REFERENCE_TYPE>` {0:1}`**  
`          `**`+1 RIN `<AUTOMATED_RECORD_ID>` {0:1}`**  
`          +1 <`<CHANGE_DATE>`>                            {0:1}`

- source citation ignored
- REFN, REFN:TYPE and RIN are ignored

## Verileri dışa aktarma

To export data, choose Menu or the [keybinding](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings#) or on Apple Mac's. This will bring up the dialog.

Exporting allows you to share any portion of your Gramps Family Tree(database) with other researchers as well as to enable you to transfer your data to another computer.

Gramps can export data to the following file formats:

- [Comma Separated Values Spreadsheet (CSV)](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees#Comma_Separated_Values_Spreadsheet.28CSV.29_export)
- [GEDCOM](#GEDCOM_export)
- GeneWeb
- Gramps [XML](wiki:Gramps_XML) (family tree)
- Gramps [XML](wiki:Gramps_XML) Package (family tree and media)
- Web Family Tree
- vCalendar
- vCard

{{-}}

### Export Assistant dialog

![[_media/ExportAssistant-SavingYourData-wizard-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Export Assistant: Saving your data - wizard start page]]The pages will guide you through the [output file format selection](#Choose_the_output_format), and then the export options specific to that file format. After the page, the export will be performed according to the choices you have made. At any time, you can click the button and revise any selection, and then go forward to redo the export. {{-}}

#### Saving your data

General information about exporting from Gramps.

Select the button to continue. {{-}}

#### Choose the output format

![[_media/ExportAssistant-ChooseTheOutputFormat-wizard-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Export Assistant - Choose the output format - wizard dialog]]Select the file format to export your data to:

- [Comma Separated Values Spreadsheet (CSV)](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees#Comma_Separated_Values_Spreadsheet.28CSV.29_export)
- [GEDCOM](#GEDCOM_export)
- GeneWeb
- **Gramps [XML](wiki:Gramps_XML) (family tree)**(default)
- Gramps [XML](wiki:Gramps_XML) Package (family tree and media)
- Web Family Tree
- vCalendar
- vCard

Then select the button to continue. {{-}}

#### Export options

![[_media/ExportAssistant-ExportOptions-CSV-defaults-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Export Assistant - Export Options - wizard dialog (showing defaults for "Comma Separated Values Spreadsheet(CSV)") with highlight Bottom section for File format specific options]]

After you have adjusted your options in the two sections.

- Top unlabeled section: [Filters and privacy](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees#Filters_and_privacy)
- Bottom unlabeled section: [File format specific options](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees#File_format_specific_export_options)

Select the button to continue. {{-}}

##### Filters and privacy

Gramps allows you to export your selected Family tree into common file formats.

The following filters provide options that allow you to fine tune your export.

Filters allow you to export a limited amount of data, based on the criteria you select.

###### Privacy Filter:

  
Check this box to prevent private records from being included in the exported file. (Checkbox checked by default)

###### Living Filter:

These option restrict data and help limit the information exported for living people. This means that all information concerning their birth, death, addresses, significant events, etc., will be omitted in the exported file. For example, you can choose to substitute the word **Living** for the first name (see your [settings](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Text)); you can exclude notes; and you can exclude sources for [living people](wiki:Gramps_6.0_Wiki_Manual_-_Probably_Alive).

Sometimes, it is not always obvious from the data if someone is actually alive. Gramps uses an advanced algorithm to try to determine [if a person could still be alive](wiki:Gramps_6.0_Wiki_Manual_-_Probably_Alive). Remember, Gramps is making its best guess, and it may not always be able to guess correctly all the time. Please double check your data.

Select from the following options:

- (default)

- 

- 

- 

###### Person Filter:

Select from the following options:

- (default)

- 

- 

- 

- 

- Create a custom filter by selecting the *Edit icon* to show the dialog.

###### Note Filter:

Select from the following options:

- (default)

- Create a custom filter by selecting the *Edit icon* to show the dialog.

###### Reference Filter:

Select from the following options:

- (default)

- 

##### Dosya biçimine özel dışa aktarma seçenekleri

Depending on the file format chosen, you may find a number of file format specific export options to choose from listed underneath the "Filters and privacy" section.

See the relevant section for each of file formats listed that have specific export options:

- [Comma Separated Values Spreadsheet (CSV)](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees#Comma_Separated_Values_Spreadsheet.28CSV.29_export)
- [Gramps XML (family tree)](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees#Gramps_XML_.28family_tree.29_export)

#### Select save file

![[_media/ExportAssistant-SelectSaveFile-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Export Assistant - Select save file - wizard dialog - example]]

Enter a export file `Untitled_1.`<file format extension>(default) and choose the folder location to save the export file to (normally your **Documents** folder.

Then select the button to continue.

If you don't have permission to save the file to that location you will see the warning dialog and then the Export Assistants wizard dialog, select the button and start the export again this time choosing a suitable folder. {{-}}

#### Final confirmation

![[_media/ExportAssistant-FinalConfirmation-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Export Assistant - Final confirmation - wizard dialog - example]]

The Export Assistants wizard dialog allows you to check the summarized details (Format/Name/Folder) of the export file to be created.

At this point you can press to revisit your options or to abort.

Or select the button to continue. {{-}}

#### Summary

![[_media/ExportAssistant-YourDataHasBeenSaved-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Export Assistant - Summary - wizard dialog - example]]

The Export Assistants wizard dialog shows the *Filename:* and confirms that you export data has been saved successfully.

Select the button to exit the Export Assistant. {{-}}

### Virgülle Ayrılmış Değerler E-tablosu (CSV) dışa aktarma

![[_media/ExportAssistant-ExportOptions-CSV-defaults-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Export Assistant - Export Options - wizard dialog (showing defaults for "Comma Separated Values Spreadsheet(CSV)") with highlight Bottom section for File format specific options]]

Virgülle Ayrılmış Değerler E-tablosu (CSV): Gramps verilerinizin bir alt kümesini basit bir e-tablo biçiminde dışa aktarmaya (ve içe aktarmaya) izin verir.

Ek bilgi ve örnekler için [CSV İçe ve Dışa Aktarma](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees:_CSV_Import_and_Export/tr) bölümüne bakın.

Virgülle Ayrılmış Değerler E-tablosu(CSV), aşağıdaki [dosya biçimine özel dışa aktarma seçeneklerine sahiptir](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees/tr#Dosya_biçimine_özel_dışa_aktarma_seçenekleri):

- Kişileri dahil et -
- Evlilikleri dahil et -
- Çocukları dahil et -
- Yerleri dahil et -
- Başlıkları çevir -

{{-}} Ayrıca, E-tablo Olarak [Dışa Aktar (Liste) Görünümü](wiki:Gramps_6.0_Wiki_Manual_-_Settings/tr#Dışa_Aktar_Görünümü) konusuna bakın.

### GEDCOM export

Gramps allows you to export a database into the common legacy format.

export has no [file format specific export options](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees#File_format_specific_export_options) but you can change the following:

- Make sure you add your information to create a valid GEDCOM file, this can be also be done with the tool.

<!-- -->

- In the [General Gramps settings](wiki:Gramps_6.0_Wiki_Manual_-_Settings#General) section of the General tab in preferences you can also choose to and also both can significantly slow down the importing of your data.

For more information on the GEDCOM format see: :

- <https://en.wikipedia.org/wiki/GEDCOM>
- <https://www.familysearch.org/developers/docs/guides/gedcom>
- <https://www.familysearch.org/developers/docs/gedcom/>

See [Gramps and GEDCOM](wiki:Gramps_and_GEDCOM) for details of data which is not exported when exporting to GEDCOM (). {{-}}

### GeneWeb export

export will save a copy of your data to the GeneWeb genealogy format.

To find out more about GeneWeb and its format, visit:

- <http://www.geneweb.org>

has no [file format specific export options](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees#File_format_specific_export_options) {{-}}

### Gramps XML (family tree) export

![[_media/ExportAssistant-ExportOptions-GrampsXMLFamilyTree-defaults-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Export Assistant - Export Options - wizard (showing defaults for "Gramps XML (family tree)") with highlight Bottom section for File format specific options]]

export (.gramps): This format is the standard format for data-exchange and backups (see the related .gpkg format below for full portability including media objects). Exporting into Gramps [XML](wiki:XML) format will produce a portable database. As XML is a text-based human-readable format, you may also use it to take a look at your data. Gramps guarantees you can open XML output of older versions of Gramps in newer version of Gramps (not the other way around though!).

If a media file is not found during export, you will see the same dialog you encounter with GEDCOM export.

has the following [file format specific export options](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees#File_format_specific_export_options):

- Use Compression -

{{-}}

#### What's not included:

### Gramps XML Package (family tree and media) export

export (.gpkg): Exporting to the Gramps package format will create a compressed file that contains the Gramps XML database and copies of all associated media files. This is useful if you want to move your database to another computer or to share it with someone.

If a media file is not found during export, you will see the same dialog you encounter with GEDCOM export.

has no [file format specific export options](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees#File_format_specific_export_options)

#### What's not included:

### Web Family Tree export

export creates a text file that can be used by the **Web Family Tree** program.

To find out more about Web Family Tree and its format, visit

- [`http://www.simonward.com/cgi-bin/page.pl?family/tree`](http://www.simonward.com/cgi-bin/page.pl?family/tree) - [linkrot](https://wikipedia.org/wiki/Link_rot). *see* [2016 **Internet Archive** snapshot](https://web.archive.org/web/20160316080343/http://www.simonward.com/cgi-bin/page.pl?family/tree)

has no [file format specific export options](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees#File_format_specific_export_options) {{-}}

### vCalendar export

export saves information in the format used in many calendaring applications, sometimes called PIM for Personal Information Manager.

For more information on the vCalendar format see:

- <https://en.wikipedia.org/wiki/ICalendar#vCalendar_1.0>

has no [file format specific export options](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees#File_format_specific_export_options) {{-}}

### vCard export

export saves information in a format used in many addressbook applications, sometimes called PIM for Personal Information Manager.

For more information on the vCard format see:

- <https://en.wikipedia.org/wiki/VCard>

has no [file format specific export options](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees#File_format_specific_export_options) {{-}}

[Category:Documentation](wiki:Category:Documentation)
