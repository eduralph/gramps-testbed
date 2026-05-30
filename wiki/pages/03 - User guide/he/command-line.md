---
title: Gramps 6.0 Wiki Manual - Command Line/he
categories:
- He:מסננים
- He:מתקעים
- He:תגים
- He:תיעוד
managed: false
source: wiki-scrape
wiki_revid: 130330
wiki_fetched_at: '2026-05-30T19:22:17Z'
lang: he
---

<div dir="rtl" lang="he" class="mw-content-rtl">

{{#vardefine:chapter\|C}} {{#vardefine:figure\|0}} נספח זה עוסק בהפעלת גרמפס משורת הפקודה ומפרט יכולות מיוחדות שזמינות בעת הפעלת גרמפס באופן זה ממסוף.

## אתחול גרמפס משורת הפקודה

בדרך כלל, גרמפס מופעל דרך ממשק המשתמש הגרפי (GUI) ב[מסדת](wiki:Gramps_6.0_Wiki_Manual_-_Getting_started/he#אתחול_גרמפס) שמותקנת על המחשב.

אך ניתן ואפשר להפעיל את גרמפס גם באמצעות ממשק שורת פקודה (CLI). שימוש ב־CLI מספק גם את היכולות הבאות:

- הפקת דוחות שאינם זמינים דרך ממשק המשתמש הגרפי,
- יצירת דוחות, ביצוע המרות וכדומה, זאת מבלי לפתוח חלון כלל
- לספק [מידע נוסף](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window/he#Seeing_all_the_error_messages) במקרה של בעיות בהרצת התוכנה.

הדרך בה מפעילים את גרמפס דרך שורת הפקודה (CLI) תלויה במערכת ההפעלה עליה מותקנת תוכנת גרמפס.

למען פשטות התיאור, דוגמאות השימוש שלהלן נכתבות מנקודת המבט של הפעלת גרמפס בסביבת מערכת הפעלה לינוקס. הפקודות במערכות הפעלה אחרות יהיו שונות זו מזו.

### לינוקס

באופן רשמי רק סביבת עבודה לינוקס נתמכת, כיוון שמפתחי גרמפס משתמשים ובודקים את קוד המקור במערכות הפעלה מבוססי לינוקס, ומתקנים בעיות שמתעוררות בעקבות שדרוגים.

בהנחה שחבילת גרמפס הותקנה באמצעות מנהל החבילות התקני (בין אם דרך CLI או GUI) עבור הפצת הלינוקס שמותקנת במחשב, אתחול גרמפס מתבצע ממסוף, משורת הפקודה על ידי הקלדת:

<div dir="ltr">

`gramps`

</div>

אם בוצעה "[בנייה מקוד המקור](https://gramps-project.org/wiki/index.php/Linux:Build_from_source)", נא לנווט למחיצה שבה התקנן היישום. (תיקיה זו תכלול את הקובץ `Gramps.py`.) ולהקליד:

<div dir="ltr">

`python3 Gramps.py`

</div>

### MS וינדוס

חבילת גרמפס למסדת מיקרוסופט וינדוס היא [בתמיכת הקהילה](wiki:Download/he#MS_וינדוס). בעת התקנת [חבילת וינדוס AIO](wiki:All_In_One_Gramps_Software_Bundle_for_Windows), סמל יוצב על גבי שולחן העבודה ופריט תפריט יתווסף לתפריט 'התחל'. עם זאת, חיצת התקנת גרמפס לא מתווספת לנתיב המערכת בעת ההתקנה באופו אוטומטי וכדי להפעיל את גרמפס משורת הפקודה (CLI), נדרש לדעת את הנתיב אל אותה מחיצה. לדרכי מציאת תיקיית ההתקנה, נא לעיין ב[מקטע תיקיית ההתקנה של חבילת AIO](wiki:All_In_One_Gramps_Software_Bundle_for_Windows#Installation_folder).

למציאת הנתיב באמצעות סמל קיצור־דרך נא לבצע את הצעדים הבאים:

- לחיצה ימנית על היישום `GrampsAIO64 ``-console`, או על הפריט המתאים בתפריט 'התחל'.
- רישום מיקום הקובץ (המחיצה תופיע בשורה "מתחיל ב" ).
- בחירה וסימון הנתיב המלא והעתקתו באמצעות ).

כדי להפעיל את גרמפס משורת הפקודה, נדרש להפעיל חלון מסוף:

- מתפריט התחל, יש להפעיל את `cmd.exe`.
- לשנות את המחיצה למחיצת ההתקנה שאותרה בשלב הקודם.
- להקליד או להדביק את הנתיב שהועתק קודם לכן, ולהקיף אותו במרכאות אם קיימים בו רווחים.
- להקיש על .

לדוגמה, זה עשוי להראות כך:

<div dir="ltr">

`cd "C:\Program Files\GrampsAOI64-``"`  
`gramps`

</div>

ניתן להשתמש בכל אחת מאפשרויות שורת הפקודה יחד עם זה. לדוגמה, כדי לקבל רשימה מפורטת של כל מסדי הנתונים של אילנות היוחסין בתיקיית ברירת המחדל של אילן היוחסין, יש להוסיף את המשתנה `L-`

<div dir="ltr">

`cd "C:\Program Files\GrampsAOI64-``"`  
`gramps -L`

</div>

דוגמאות שימושיות ניתן למצוא בקישור [הזה](https://github.com/gramps-project/addons-source/pull/121)

### OS X מק

חבילת גרמפס למסדת מק OS X היא [בתמיכת הקהילה|מק_OS](wiki:Download/he).לאחר הורדת תמונת תקליטור מק OS (.dmg), ניתן פשוט לגרור את היישום לתיקיית היישום (או לכל מקום אחר שם הוא יאוחסן) ולהפעיל את גרמפס על ידי הקשה כפולה על היישום באותה הדרך בה מפעילים כל יישום בסביבת עבודה של מק OS. [מנהל החבילות Homebrew](https://github.com/Homebrew) מאפשר גם התקנה של היישום בתיקיית היישומים הרגילה.

להפעלה משורת הפקודה, נדרש להפעיל את המסוף, שנמצאה בתיקיית עזרים, בתוך תיקיית היישומים הראשית (/Applications/Utilities). לאחר שחלון המסוף נפתח, ניתן להקליד את ההנחיה

<div dir="ltr">

` /path/to/Gramps.app/Contents/MacOS/Gramps`

</div>

אם גרמפס הותקן בספריית היישומים יחד עם רוב היישומים האחרים, כפי שהוצע לעיל, זה יהיה בנתיב:

<div dir="ltr">

` /Applications/Gramps.app/Contents/MacOS/Gramps`

</div>

ניתן להשתמש בכל אחת מאפשרויות שורת הפקודה ביחד עם זה. לדוגמה, כדי לקבל רשימה מפורטת של כל מסדי הנתונים של אילן היוחסין בתיקיית ברירת המחדל שלך אילן היוחסין, יש להשתמש בפקודה:

<div dir="ltr">

` /Applications/Gramps.app/Contents/MacOS/Gramps -L`

</div>

קיימות כמובן דרכים נוספות להתקנת גרמפס בסביבת מק osx אבל הן מסובכות הרבה יותר ולא מוסברות במדריך זה.

## אפשרויות פיתון

בדוגמאות למסדות השונות לעיל, וגם בפקודות שמופיעות בקבצים שונים, עשויות להופיע מספר אפשרויות אחרי הפקודה 'python', כגון `'EO-'` כמו בשורה הבאה:

<div dir="ltr">

`"python3 -EO ..\share\gramps\gramps.py -L`

</div>

חשוב להבחין בין **אפשרויות פיתון** כמו בשורה הבאה:

<div dir="ltr">

`-EO`

</div>

ל**אפשרויות גרמפס**, כמו:

<div dir="ltr">

`-L`

</div>

**אפשרויות פיתון** נפוצות בהו יש סבירות גבוהה להתקל הן:

- <div dir="ltr">

  `-E`

  </div>

  להתעלם מכל משתני סביבת פיתון, כלומר `PYTHONPATH` ו־`PYTHONHOME`, שייתכן והוגדרו.

- <div dir="ltr">

  `-O`

  </div>

  הפעלת מיטוב בסיסי. שישנה את סיומת שם הקובץ לקבצים מהודרים (bytecode) מ־`.pyc` ל־`.pyo`.</br>

לקריאה נוספת PYTHONOPTIMIZE.

משתנה המיטוב `O-` משפיע במספר אופנים בגרמפס:

- אם הוא לא מופעל, ערך נוסף של יופיע בתפריט .
- אם הוא לא מופעל, [info logging messages are output](wiki:Logging_system/he#So_how_logging_works_in_Gramps_after_all.3F).
- אם הוא לא מופעל, [דוחות ניפוי תקלים](wiki:Debugging_Gramps/he#Add_debug_statements) ישופעל.
- אם הוא לא מופעל, תכונות נוספות יהיו זמינו ב[מנהל מתקעים](wiki:Gramps_6.0_Wiki_Manual_-_Plugin_Manager/he).

## אפשרויות גרמפס זמינות

This section provides the reference list of all command line options available in Gramps. If you want to know more than just a list of options, see next sections: [Operation](#Operation) and [Examples](#Examples). The summary below is printed by

<div dir="ltr">

`gramps -h`

</div>

או

<div dir="ltr">

`gramps --help`

</div>

אופן שימוש:

<div dir="ltr">

     gramps.py [OPTION...]
      --load-modules=MODULE1,MODULE2,...     פרקנים הידודיים לטעינה

</div>

אפשרויות עזרה:

<div dir="ltr">

` -?, --help                             הצגת הודעת עזרה זו`  
` --usage                                הצגת הודעת אופן שימוש קצר`

</div>

אפשרויות יישום:

<div dir="ltr">

     
      -O, --open=FAMILY_TREE                 Open Family Tree
      -U, --username=USERNAME                Database username
      -P, --password=PASSWORD                Database password
      -C, --create=FAMILY_TREE               Create on open if new Family Tree
      -i, --import=FILENAME                  Import file
      -e, --export=FILENAME                  Export file
      -r, --remove=FAMILY_TREE_PATTERN       Remove matching Family Tree(s) (use regular expressions)
      -f, --format=FORMAT                    Specify Family Tree format
      -a, --action=ACTION                    Specify action
      -p, --options=OPTIONS_STRING           Specify options
      -d, --debug=LOGGER_NAME                Enable debug logs
      -l [FAMILY_TREE_PATTERN...]            List Family Trees
      -L [FAMILY_TREE_PATTERN...]            List Family Trees in Detail
      -t [FAMILY_TREE_PATTERN...]            List Family Trees, tab delimited
      -u, --force-unlock                     Force unlock of Family Tree
      -s, --show                             Show config settings
      -c, --config=[config.setting[:value]]  Set config setting(s) and start Gramps
      -y, --yes                              Don't ask to confirm dangerous actions (non-GUI mode only)
      -q, --quiet                            Suppress progress indication output (non-GUI mode only)
      -v, --version                          Show versions

</div>

The usage message is as follows:

<div dir="ltr">

`gramps --usage`

</div>

Example of usage of Gramps command line interface

1\. To import four databases (whose formats can be determined from their names) and then check the resulting database for errors, one may type:

<div dir="ltr">

`gramps -i file1.ged -i file2.gpkg -i ~/db3.gramps -i file4.wft -a tool -p name=check.`

</div>

2\. To explicitly specify the formats in the above example, append filenames with appropriate -f options:

<div dir="ltr">

`gramps -i file1.ged -f gedcom -i file2.gpkg -f gramps-pkg -i ~/db3.gramps -f gramps-xml -i file4.wft -f wft -a tool -p name=check.`

</div>

3\. To record the database resulting from all imports, supply -e flag (use -f if the filename does not allow Gramps to guess the format):

<div dir="ltr">

`gramps -i file1.ged -i file2.gpkg -e ~/new-package -f gramps-pkg`

</div>

4\. To save any error messages of the above example into files outfile and errfile, run:

<div dir="ltr">

`gramps -i file1.ged -i file2.dpkg -e ~/new-package -f gramps-pkg >outfile 2>errfile`

</div>

5\. To import three databases and start interactive Gramps session with the result:

<div dir="ltr">

`gramps -i file1.ged -i file2.gpkg -i ~/db3.gramps`

</div>

6\. To open a database and, based on that data, generate timeline report in PDF format putting the output into the my_timeline.pdf file:

<div dir="ltr">

`gramps -O 'Family Tree 1' -a report -p name=timeline,off=pdf,of=my_timeline.pdf`

</div>

7\. To generate a summary of a database:

<div dir="ltr">

`gramps -O 'Family Tree 1' -a report -p name=summary`

</div>

8\. Listing report options Use the name=timeline,show=all to find out about all available options for the timeline report. To find out details of a particular option, use show=option_name , e.g. name=timeline,show=off string. To learn about available report names, use name=show string.

9\. To convert a Family Tree on the fly to a .gramps xml file:

<div dir="ltr">

`gramps -O 'Family Tree 1' -e output.gramps -f gramps-xml`

</div>

10\. To generate a web site into an other locale (in german):

<div dir="ltr">

`LANGUAGE=de_DE; LANG=de_DE.UTF-8 gramps -O 'Family Tree 1' -a report -p name=navwebpage,target=/../de`

</div>

11\. Finally, to start normal interactive session type:

<div dir="ltr">

`gramps`

</div>

Note: These examples are for bash shell. Syntax may be different for other shells and for Windows.

### אפשרויות רשימה

הדפסת רשימת אילונות־היוחסין הידועים:

בלווית המשתנה  

<div dir="ltr">

`-l, רשימת אילנות יוחסין`

</div>

<div dir="ltr">

`gramps -l`

</div>

הדפסת רשימת אילונות־היוחסין הידועים בנתיב מסד הנתונים:

<div dir="ltr">

`/home/<~username>/.gramps/grampsdb/5a46c1c3 בשם "Example Family Tree"`

</div>

{{-}}

לרשימה מפורטת  

<div dir="ltr">

`-L, רשימת אילנות יוחסין מפורטת`

</div>

<div dir="ltr">

`gramps -L`

</div>

דוגמת פלט שיוצג במסוף:

<div dir="ltr">

<code> Gramps Family Trees: Family Tree "Example Family Tree":

`  Database: SQLite`  
`  Database module location: /usr/lib/python3.5/sqlite3/__init__.py`  
`  Database module version: 2.6.0`  
`  Database version: 3.11.0`  
`  Last accessed: 30/12/17 09:29:37`  
`  Locked?: False`  
`  Number of citations: 2854`  
`  Number of events: 3432`  
`  Number of families: 762`  
`  Number of media: 7`  
`  Number of notes: 19`  
`  Number of people: 2157`  
`  Number of places: 1294`  
`  Number of repositories: 3`  
`  Number of sources: 4`  
`  Number of tags: 2`  
`  Path: /home/<~username>/.gramps/grampsdb/5a46c1c3`  
`  Schema version: 18.0.0`

</code>

</div>

{{-}}

### Version options

`-v or --version prints version of Gramps and dependencies,`  
`     information about environment settings and python and system paths`

`gramps -v`

    Gramps Settings:
    ----------------
     python    : 3.6.0
     gramps    : 5.0.0
     gtk++     : 3.18.9
     pygobject : 3.20.0
     pango     : 1.38.1
     cairo     : 1.14.6
     pycairo   : 1.10.0
     osmgpsmap : 1.0
     GExiv2    : 0.10
     ICU       : 55.1
     PyICU     : 1.9.5
     o.s.      : linux
     kernel    : 4.4.0-104-generic

    Environment settings:
    ---------------------
     LANG      : en_GB.UTF-8
     LANGUAGE  : en_GB:en_GB:en
     GRAMPSI18N: not set
     GRAMPSHOME: not set
     GRAMPSDIR : not set
     GRAMPS_RESOURCES : /gramps
     PYTHONPATH:
        /usr/lib/python3.5
        /usr/lib/python3.5/plat-x86_64-linux-gnu
        /usr/local/lib/python3.5/dist-packages
        /usr/lib/python3/dist-packages

    Non-python dependencies:
    ------------------------
     Graphviz  : 2.38
     Ghostscr. : 9.18

    System PATH env variable:
    -------------------------
         /usr/local/sbin
         /usr/local/bin
         /usr/sbin
         /usr/bin
         /sbin
         /bin
         /usr/games
         /usr/local/games
         /snap/bin

    Databases:
    -------------------------
     bsddb     :
         version     : 6.1.0
         db version  : 5.3.28
         location    : /usr/lib/python3/dist-packages/bsddb3/__init__.py
     sqlite3   :
         version     : 3.11.0
         py version  : 2.6.0
         location    : /usr/lib/python3.5/sqlite3/__init__.py

{{-}}

### Format options

The format of any file destined for opening, importing, or exporting can be specified with the

    -f format

option. The acceptable *`format`* values are listed below.

#### Full family tree support

These formats contain all your data that is present in a family tree.

- **gramps** - Gramps XML format: This format is available for import, and export. When not specified, it can be guessed if the filename ends with .gramps
- **gpkg** - Gramps package XML format: This format is available for import and export. When not specified, it can be guessed if the filename ends with .gpkg. This creates a zip package with your data as xml, and all your media files included
- **grdb** - pre Gramps 3.x database: This format is available for import to support the old file format of Gramps. Everything in the grdb file is imported. When not specified, it can be guessed if the filename ends with .grdb
- **burn** - GNOME iso burning: export, only available on GNOME where burn protocol exists

#### Reduced family tree support

These formats contain most, but not all data that can be created in Gramps

- **ged** - GEDCOM format: This format is available for import, and export. When not specified, it can be guessed if the filename ends with .ged
- **gw** - GeneWeb file: This format is available for import and export. When not specified, it can be guessed if the filename ends with .gw

#### Subset of your data

These formats contain a specific subset of your data

- **csv** - Comma Separated Value: This format is available for import and export. Be careful however, import must be as values created by the export function. Only a part of your data is contained in the output.
- **vcf** - VCard format: import and export
- **vcs** - VCalandar format: export
- **def** - old Pro-Gen format: import
- **wft** - Web Family Tree: This format is available for export only. When not specified, it can be guessed if the filename ends with .wft

### אפשרויות פתיחה

ניתן לפתוח אילן־יוחסין קיים, או לחלופין "לפתוח" קובץ באמצעות ייבואו לאילן־יוחסין ריק.

כדי לאפשר לגרמפס לטפל בכך באופן אוטומטי, יש פשוט לציין את שם אילן־היוחסין או את שם הקובץ אותו מעונינים לפתוח, לדוגמה:

<div dir="ltr">

`python gramps.py 'אילן משפחתי שלי'`  
`python gramps.py JohnDoe.ged`

</div>

השורה הראשונה פותחת אילן־יוחסין קיים, והשנייה מייבאת קובץ GEDCOM לאילן־יוחסין ריק.

בנוסף, ניתן לציין לגרמפס את שם אילן־היוחסין שיש לפתוח באמצעות המתגים הבאים:

<div dir="ltr">

`-O famtree`

</div>

או

<div dir="ltr">

`--open=famtree`

</div>

המתג

<div dir="ltr">

`-O`

</div>

מציין פתיחה של אילן־יוחסין. ניתן גם פשוט לציין את שמו (כשם בלבד או כנתיב למחיצה מסד הנתונים).

דוגמאות:

<div dir="ltr">

`python gramps.py 'אילן יוחסין 1'`  
`python gramps.py /home/cristina/.gramps/grampsdb/47320f3d`  
`python gramps.py -O 'אילן יוחסין 1'`  
`python gramps.py -O /home/cristina/.gramps/grampsdb/47320f3d`

</div>

**לתשומת לב**: אם לא צוין כל מתג, אלא שם בלבד, גרמפס יתעלם משאר הארגומנטים בשורת הפקודה. לכן כדי להשתמש ב־<span dir="ltr">`-O`</span>לפתיחה, וב־<span dir="ltr">`-i`</span> ליבוא, והוסף אחריהם בהמשך את שאר ההוראות לעיבוד הנתונים כגון שם אילן־יוחסין, או שם כובץ וכן הלאה.

{{-}}

### Import options

The files destined for import can be specified with the `-i filename` or `--import=filename` option. The format can be specified with the `-f format` or `--format=format` option, immediately following the *filename* . If not specified, the guess will be attempted based on the *filename*.

Example:

`  python gramps.py -i 'Family Tree 1' -i 'Family Tree 2'`  
`  python gramps.py -i test.grdb -i data.gramps`

When more than one input file is given, each has to be preceded by `-i` flag. The files are imported in the specified order, i.e. `-i file1 -i file2` and `-i file2 -i file1` might produce different Gramps IDs in the resulting database.

### Export options

The files destined for export can be specified with the `-e filename` or `--export=filename` option. The format can be specified with the `-f` option immediately following the *filename* . If not specified, the guess will be attempted based on the *filename* . For iso format, the *filename* is actually the name of directory the Gramps database will be written into. For gramps-xml, gpkg, gedcom, wft, geneweb, and gramps-pkg, the *filename* is the name of the resulting file.

-e, export a family tree in required format. It is not possible to export to a family tree.

Example:

` python gramps.py -i 'Family Tree 1' -i test.grdb -f grdb -e mergedDB.gramps`

Note that above does not change 'Family Tree 1' as everything happens via a temporary database, whereas:

` python gramps.py -O 'Family Tree 1' -i test.grdb -f grdb -e mergedDB.gramps`

will import test.grdb into Family Tree 1, and then export to a file !

When more than one output file is given, each has to be preceded by `-e` flag. The files are written one by one, in the specified order.

### Action options

The action to perform on the imported data can be specified with the `-a action` or `--action=action` option. This is done after all imports are successfully completed.

The following actions remain the same:

- *report*: This action allows producing reports from the command line.

<!-- -->

- *tool*: This action allows to run a tool from the command line.

Reports and tools generally have many options of their own, so these actions should be followed by the report/tool option string. The string is given using the `-p option_string` or `--options=option_string` option.

The actions available in older versions of Gramps which were relocated in Gramps 3.3 are:

- *summary*: This action was the same as . In Gramps 3.3 it was replaced by (or renamed to) **-a report -p name=summary**.

<!-- -->

- *check*: This action was the same as . In Gramps 3.3 it was replaced by (or renamed to) **-a tool -p name=check**.

#### report action option

You can generate most reports from the command line using the report action.

An example:

`gramps -O "Family Tree 1" -a report -p "name=family_group,style=default,off=html,of=test.html"`

You can provide the css style to use here with the css option:

`gramps -O "Family Tree 1" -a report -p "name=family_group,style=default,off=html,of=test.html,css=Web_Nebraska.css"`

or without css in the html output:

`gramps -O "Family Tree 1" -a report -p "name=family_group,style=default,off=html,of=test.html,css="`

Most of the report options are specific for every report. However, there are some common options.

- `name=report_name`: This mandatory option determines which report will be generated.

- `of=`: output filename and optional destination folder/directory eg: `of="C:\Users\`<username>`\Desktop\FamilyTree.odt"`
- `off=`: output format. These are the extension an output format makes available, eg, pdf, html, doc, ...
- `style=`: for text reports, the stylesheet to use. Defaults to 'default'.
- `show=all`: This will produce the list of names for all options available for a given report.
- `show=option_name`: This will print the description of the functionality supplied by the option_name, as well as what are the acceptable types and values for this option.

So, to learn to use a report, do for example:

`gramps -O "Family Tree 1" -a report -p "name=family_group,show=all"`

When more than one output action is given, each has to be preceded by `-a` flag. The actions are performed one by one, in the specified order.

On the command line such lists must always start with a left square bracket `[` and must always end with a right square bracket `]` but since such square brackets are usually "special" to the "shell" (they mean something to the command interpreter you are typing the command to), you must "escape" them so that they are ignored by your shell.

The details vary with each shell but (in linux/UNIX) usually you can precede such a square bracket with a backslash `\` or put quotation marks around the square bracket, usually either "single" or "double" ones.

The Hourglass Graph report allows you to put a "note" at the top of the report and such a "note" is an example of a "list" option. Here is an example:

`gramps -O "Family Tree 1" -a report -p name=hourglass_graph,note='[line one,line two]'`

which shows that inside such a list different lines are separated by commas, and that spaces are acceptable since the quotation marks are already there for the square brackets.

But if you want to have a comma inside your report you have to somehow tell Gramps that comma is not one which separates lines. You do that by enclosing the line with the comma in quotation marks (either single or double).

But if you are already using a set of quotation marks (to enclose your square brackets) you have to use the other type to enclose the line with your comma. Here is an example:

`gramps -O "Family Tree 1" -a report -p name=hourglass_graph,note="['line one, also line one','line two, also line two']"`

It is possible to include any character in a list but the details are beyond the scope of this command-line introduction to Gramps.

You will need to know the precise methods available in your particular command shell interpreter to include a character which is "special" to your shell or "special" to Gramps (like the comma in the example above) but in general you will have to "escape" it twice, once to your shell and once again to Gramps, since you don't want your shell to think it is some instruction it should pay attention to and you don't want Gramps to think that either.

#### tool action option

You can run most tools from the command line using the 'tool' action. To see which ones, say:

`gramps -O "Family Tree 1" -a tool -p show=all`

To see a tool's available options, for instance the "verify" tool:

`gramps -O "Family Tree 1" -a tool -p name=verify,show=all`

To run a tool, for instance the "verify" tool:

`gramps -O "Family Tree 1" -a tool -p name=verify`

#### book action option

You can run books from the command line using the 'book' action. To see which ones, say:

`gramps -O "Family Tree 1" -a book`

To see a book's available options, for instance a book called "mybook":

`gramps -O "Family Tree 1" -a book -p name=mybook,show=all`

To run a book, for instance a book called "mybook":

`gramps -O "Family Tree 1" -a book -p name=mybook`

### אפשרות אילוץ שחרור נעילה

- `-u`: you can extend the `-O` flag with `-u` to force a locked family to be unlocked. This allows you to recover from a crash that leaves the family tree (database) locked, from the command line.

An example (to unlock the "Family Tree 1" database):

<div dir="ltr">

  
`gramps -O "Family Tree 1" -a report -u > /dev/null`

</div>

לקריאה נוספת:

- [Manage Family Trees:Unlocking a Family Tree](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees/he#Unlocking_a_Family_Tree)

### אפשרויות תצור ‎(config)

כאשר כל משתני התצורה מוגדרים, גרמפס יאתחל עם הערכים החדשים הללו.

אפשרויות אלה יכולות ללבוש שלוש צורות:

1\) הצגת כל ערכי התצורה  
`-s` or `--show`

  
לדוגמה:

<div dir="ltr">

`gramps --show`

</div>

    Gramps config settings from /home/<~username>/.gramps/gramps50/gramps.ini:
    export.proxy-order=[['privacy', 0], ['living', 0], ['person', 0], ['note', 0], ['reference', 0]]

    database.compress-backup=True
    database.backend='bsddb'
    database.backup-path='/home/<~username>'
    database.port=''
    database.autobackup=0
    database.path='/home/<~username>/.gramps/grampsdb'
    database.host=''
    database.backup-on-exit=True

    geography.lock=False
    ....

{{-}}

2\) See a single config value  
`--config=database.path` or `-c database.path`

  
לדוגמה:

<div dir="ltr">

`gramps --config=database.path`

</div>

    Current Gramps config setting: database.path:'/home/<~username>/.gramps/grampsdb'

3\) Set a value: `--config=behavior.database-path:'/media/mydb'` or `-c behavior.database-path:'/media/mydb'`  
For example:

3.1) Set a value to its default: `--config=behavior.database-path:DEFAULT` or `-c behavior.database-path:DEFAULT`  
For example:

3.2) Set more than one value: `--config=behavior.use-tips:False --config=behavior.autoload:True` or `-c behavior.use-tips:False -c behavior.autoload:True`  
For example:

## Operation

If the first argument on the command line does not start with a dash (i.e. no flag), Gramps will attempt to open the file with the name given by the first argument and start an interactive session, ignoring the rest of the command line arguments.

If the `-O` flag is given, then Gramps will try opening the supplied file name and then work with that data, as instructed by the further command line parameters.

With or without the `-O` flag, there could be multiple imports, exports, and actions specified further on the command line by using `-i` , `-e` , and `-a` flags.

The order of `-i` , `-e` , or `-a` options with respect to each does not matter. The actual execution order always is: all imports (if any) -\> all exports (if any) -\> all actions (if any).

If no `-O` or `-i` option is given, Gramps will launch its main window and start the usual interactive session with the empty database, since there is no data to process, anyway. (Unless you have already expressed a "preference" that it start with the last database it used.)

If no `-e` or `-a` options are given, Gramps will launch its main window and start the usual interactive session with the database resulted from opening and all imports (if any). This database resides in a directory under the *`~/.gramps/grampsdb/`* directory.

Any errors encountered during import, export, or action, will be either dumped to stdout (if these are exceptions handled by Gramps) or to stderr (if these are not handled). Use usual shell redirections of stdout and stderr to save messages and errors in files.

## דוגמאות

- To import four databases (whose formats can be determined from their names) and then check the resulting database for errors, one may type:

<div dir="ltr">

  
`gramps -i file1.ged -i file2.gpkg -i ~/db3.gramps -i file4.wft -a check`

</div>

- To explicitly specify the formats in the above example, append filenames with appropriate -f options:

<div dir="ltr">

  
`gramps -i file1.ged -f gedcom -i file2.gpkg -f gramps-pkg -i ~/db3.gramps -f gramps-xml -i file4.wft -f wft -a check`

</div>

- To record the database resulting from all imports, supply -e flag (use -f if the filename does not allow Gramps to guess the format):

<div dir="ltr">

  
`gramps -i file1.ged -i file2.gpkg -e ~/new-package -f gramps-pkg`

</div>

- To save any error messages of the above example into files outfile and errfile, run:

<div dir="ltr">

  
`gramps -i file1.ged -i file2.dpkg -e ~/new-package -f gramps-pkg >outfile 2>errfile`

</div>

- To import three databases and start interactive Gramps session with the result:

<div dir="ltr">

  
`gramps -i file1.ged -i file2.gpkg -i ~/db3.gramps`

</div>

- To open a database and, based on that data, generate timeline report in PDF format putting the output into the my_timeline.pdf file:

<div dir="ltr">

  
`gramps -O 'Family Tree 1' -a report -p name=timeline,off=pdf,of=my_timeline.pdf`

</div>

- To convert the bsddb database on the fly to a .gramps xml file:

  
`gramps -O 'Family Tree 1' -e output.gramps -f gramps-xml`

- To generate a web site into an other locale (in german):

  
`LANGUAGE=de_DE; LANG=de_DE.UTF-8 gramps -O 'Family Tree 1' -a report -p name=navwebpage,target=/../de`

- Finally, to start normal interactive session type:

  
`gramps`

## Environment variables

### GRAMPSHOME

- **GRAMPSHOME** - if set, override default path to profile allowing user to use an external network drive to store data and all settings. For technically advanced users who run multiple versions of Gramps, setting a different \$GRAMPSHOME is a way to avoid interference between the different versions in the Gramps user directory.

For example

    GRAMPSHOME=$HOME/familytrees/paternal

### LANG, LANGUAGE, LC_MESSAGE, LC_TIME

- **LANG**, **LANGUAGE**, **LC_MESSAGES**, and **LC_TIME** - are used by Gramps to determine which language file(s) should be loaded. See locale(1) for a general discussion of **LANG**, **LC_MESSAGES**, and **LC_TIME**. Note that in addition to setting date formats (which are overridden in Gramps with Preferences settings) **LC_TIME** also sets the language used for words in dates like month and day names and *in the context of dates* words like *about*, *between*, and *before*. **LANGUAGE** is a comma-separated list of language codes (*not locales*, though certain languages like pt_BR or cn_TW are regional variants) that sets a preference-ordered list of desired translations. It will override **LANG** but not **LC_MESSAGES** or **LC_TIME**.

### GRAMPSI18N

- [$GRAMPSI18N (for your locale)](wiki:Translating_Gramps#.24GRAMPSI18N_.28for_your_locale.29) - The LANG assumes the Gramps translations are installed globally. If this is not the case, you need to give Gramps the directory where the translations will be found. A translation is called `gramps.mo`, you can find it in linux with the locate command. For example, if you have Swedish in directory `/home/me/gramps/mo/sv/gramps.mo`, you can direct Gramps there using:

`GRAMPSI18N=/home/me/gramps/mo LC_ALL=C.UTF-8 LANG="sv" python3 gramps`

### GRAMPSDIR

- The environment variable GRAMPSDIR is the path to your [Gramps directory](wiki:Translating_Gramps#gramps.sh).

### GRAMPS_RESOURCES

- The environment variable GRAMPS_RESOURCES is the path to Gramps builtin resources files. You should only change this if you are using Gramps from source code or a custom environment. An indicator that you need to set this variable is if you receive one of the following errors:
  - *Encoding error while parsing resource path*
  - *Failed to open resource file*
  - *Resource Path {invalid/path/to/resources} is invalid*
  - *Unable to determine resource path*

Example [usage](wiki:Linux:Build_from_source#Running_from_a_tarball_release):

`GRAMPS_RESOURCES=/home/benny/gramps/branches/maintenance/gramps52/build/lib.linux-x86_64-2.7/ PYTHONPATH=$GRAMPS_RESOURCES:$PYTHONPATH ./gramps`

{{-}}

[Category:He:תיעוד](wiki:Category:He:תיעוד) [Category:He:מסננים](wiki:Category:He:מסננים) [Category:He:מתקעים](wiki:Category:He:מתקעים) [Category:He:תגים](wiki:Category:He:תגים)
