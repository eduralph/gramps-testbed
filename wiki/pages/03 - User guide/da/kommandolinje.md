---
title: Da:Gramps 6.0 brugsanvisning - Kommandolinje
categories:
- Documentation
managed: false
source: wiki-scrape
wiki_revid: 128127
wiki_fetched_at: '2026-05-30T17:03:55Z'
lang: da
---

{{#vardefine:kapitel\|C}} {{#vardefine:figure\|0}}

Appendiks C: Kommandolinje

Dette appendiks indeholder en reference til de kommandolinjefunktioner, der er tilgængelige, når **Gramps (til desktops)** startes fra kommandolinjen.

## Start Gramps via kommandolinjen

Normalt startes Gramps via den grafiske brugergrænseflade (GUI) på [din platform](wiki:Gramps_6.0_Wiki_Manual_-_Getting_started#Start_Gramps).

Det er også muligt at starte Gramps ved hjælp af en kommandolinjegrænseflade (CLI). CLI-brug kan

- producere rapporter, der ikke er tilgængelige via GUI'en,
- oprette rapporter, udføre konverteringer osv. uden at åbne et vindue og
- give [ekstra information](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window#Seeing_all_the_error_messages) i tilfælde af problemer.

Dette afsnit af brugermanualen beskriver, hvordan man starter Gramps via CLI'en, og de tilgængelige funktioner.

Måden, du starter Gramps via CLI'en, afhænger af det operativsystem, du bruger.

For at forenkle beskrivelsen er eksemplerne på brug nedenfor skrevet ud fra et synspunkt om at køre Gramps på Linux. Eksemplerne skal ændres til andre platforme.

### Linux

Linux-platformen er den primære *officielt* understøttede platform. (Andre platforme er *fællesskabsstøttede*.) Dette skyldes, at Gramps-udviklere designer, koder, bruger og tester kildekoden på den platform. Så diagnosticering og løsning af eventuelle problemer, der opstår (uanset om det skyldes opgraderinger eller andre årsager), udføres ved hjælp af Linux-værktøjer.

Forudsat at du har brugt standardpakkehåndteringen (enten via en CLI eller en GUI) til din Linux-distribution, starter du Gramps via CLI ved at skrive: gramps

Hvis du har lavet en "[build from source](wiki:Linux:Build_from_source)", skal du navigere til det sted, hvor du installerede applikationen. (Denne mappe vil indeholde filen `Gramps.py`.) Skriv: python3 Gramps.py

### MS Windows

MS Windows er en [officielt understøttet](wiki:Download) platform. Hvis du installerer [Windows AIO-pakken](wiki:All_In_One_Gramps_Software_Bundle_for_Windows), vil dette placere et ikon på skrivebordet samt et menupunkt i 'Start'-menuen. Gramps-installationsmappen tilføjes dog ikke til systemstien, og for at køre gramps via CLI skal vi kende stien til den mappe.

For at finde installationsmappen, se  

- [AIO-bundlens installationsmappeafsnit](wiki:All_In_One_Gramps_Software_Bundle_for_Windows#Installation_folder).

For at finde stien ved hjælp af et genvejsikon i stedet  

- Højreklik på `GrampsAIO64 ``-console`-applikationen eller det tilsvarende element i Start-menuen.

<!-- -->

- Notér filplaceringen (dens "Start i"-mappe).
- Vælg den fulde sti og kopier () den.

For at køre Gramps fra kommandolinjen skal du starte et konsolvindue  

- Start cmd.exe fra Start-menuen.
- Skift mappe til den installationsmappe, du fandt.
- Indtast eller indsæt stien, og sæt den i anførselstegn, hvis der er mellemrum.
- Tryk på .

For eksempel kan dette være:

`cd "C:\Program Files\GrampsAIO64-``"`  
`gramps`

Du kan bruge en hvilken som helst af kommandolinjeindstillingerne sammen med dette. For eksempel, for at få en detaljeret liste over alle Slægtsbog-databaserne i din standard Slægtsbog-mappe, skal du tilføje `-L`

`cd "C:\Program Files\GrampsAIO64-``"`  
`gramps -L`  

Se også:

- Eksempel på brug <https://github.com/gramps-project/addons-source/pull/121>

### macOS

macOS er en platform, der [community-understøttet](wiki:Download). Hvis du downloader macOS-diskbilledet (.dmg), skal du blot trække programmet til din programmappe (eller et andet sted, hvor du vil gemme det) og starte Gramps ved at dobbeltklikke på programmet på normal vis. [Homebrew-pakkehåndteringen](https://github.com/Homebrew) tillader også installation af programmet i den sædvanlige Programmer-mappe.

For at køre fra kommandolinjen skal du starte Terminal, som findes i mappen Hjælpeprogrammer i hovedmappen Programmer (/Programmer/Hjælpeprogrammer). Når du har et terminalvindue åbent, skal du skrive følgende ved prompten:

`/sti/til/Gramps.app/Contents/MacOS/Gramps`

Hvis du installerede Gramps i Programmer sammen med de fleste af dine andre apps, som foreslået ovenfor, ville det være

`/Applications/Gramps.app/Contents/MacOS/Gramps`

Du kan bruge en hvilken som helst af kommandolinjeindstillingerne sammen med dette. For eksempel, for at få en detaljeret liste over alle Slægtsbog-databaserne i din standard Slægtsbog-mappe, skal du bruge

`/Applications/Gramps.app/Contents/MacOS/Gramps -L`

Der er andre måder at installere Gramps til macOS på, men disse er meget mere komplicerede og er ikke dækket her.

## Python-indstillinger

I eksemplerne på forskellige platforme ovenfor, og også i kommandoer i forskellige filer, kan du se nogle indstillinger efter 'python'-kommandoen, for eksempel '-EO' i

`"python3 -EO ..\share\gramps\gramps.py -L`

Det er vigtigt at skelne mellem **python-indstillingerne** i dette tilfælde:

`-EO`

og **Gramps-indstillingerne**, i dette tilfælde

`-L`

De **python-indstillinger**, som du kan støde på, er:

- `-E` Ignorer alle PYTHON\*-miljøvariabler, f.eks. `PYTHONPATH` og `PYTHONHOME`, der kan være indstillet.
- `-O` Aktiver grundlæggende optimeringer. Dette ændrer filnavnetypen for kompilerede (bytecode) filer fra `.pyc` til `.pyo`. Se også PYTHONOPTIMIZE.

`-O` optimizer-flaget har en række effekter i Gramps:

- Hvis det ikke er aktiveret, vises en yderligere -post i -menuen.
- Hvis det ikke er aktiveret, vises [info-logmeddelelser](wiki:Logging_system#So_how_logging_works_in_Gramps_after_all.3F).
- Hvis det ikke er aktiveret, kan [debug statements](wiki:Debugging_Gramps#Add_debug_statements) blive aktiveret.
- Hvis det ikke er aktiveret, er yderligere funktioner tilgængelige i [Plugin Manager](wiki:Gramps_6.0_Wiki_Manual_-_Plugin_Manager).

**Gramps-indstillingerne** er beskrevet nedenfor.

## Tilgængelige Gramps-indstillinger

Dette afsnit indeholder en referenceliste over alle kommandolinjeindstillinger, der er tilgængelige i Gramps. Hvis du vil vide mere end blot en liste over indstillinger, kan du se de næste afsnit: [Operation](#Operation) og [Examples](#Examples).

### Hjælpeindstillinger

Resuméet nedenfor udskrives ved

`gramps --help`

eller

`gramps -h`

    Usage: gramps [OPTION...]
      --load-modules=MODULE1,MODULE2,...     Dynamic modules to load

    Help options
      -?, --help                             Show this help message
      --usage                                Display brief usage message

    Application options
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
      -S, --safe                             Start Gramps in 'Safe mode'
                                              (temporarily use default settings)
      -D, --default=[APXFE]                  Reset settings to default;
                     A - addons are cleared
                     P - Preferences to default
                     X - Books are cleared, reports and tool settings to default
                     F - filters are cleared
                     E - Everything is set to default or cleared

{{-}}

### Usage meddelelse

"usage" meddelelse er som følger:

`gramps --usage`

    Example of usage of Gramps command line interface

    1. To import four databases (whose formats can be determined from their names)
    and then check the resulting database for errors, one may type:
    gramps -i file1.ged -i file2.gpkg -i ~/db3.gramps -i file4.wft -a tool -p name=check.

    2. To explicitly specify the formats in the above example, append filenames with appropriate -f options:
    gramps -i file1.ged -f gedcom -i file2.gpkg -f gramps-pkg -i ~/db3.gramps -f gramps -i file4.wft -f wft -a tool -p name=check.

    3. To record the database resulting from all imports, supply -e flag
    (use -f if the filename does not allow Gramps to guess the format):
    gramps -i file1.ged -i file2.gpkg -e ~/new-package -f gramps-pkg

    4. To save any error messages of the above example into files outfile and errfile, run:
    gramps -i file1.ged -i file2.dpkg -e ~/new-package -f gramps-pkg >outfile 2>errfile

    5. To import three databases and start interactive Gramps session with the result:
    gramps -i file1.ged -i file2.gpkg -i ~/db3.gramps

    6. To open a database and, based on that data, generate timeline report in PDF format
    putting the output into the my_timeline.pdf file:
    gramps -O 'Family Tree 1' -a report -p name=timeline,off=pdf,of=my_timeline.pdf

    7. To generate a summary of a database:
    gramps -O 'Family Tree 1' -a report -p name=summary

    8. Listing report options
    Use the name=timeline,show=all to find out about all available options for the timeline report.
    To find out details of a particular option, use show=option_name , e.g. name=timeline,show=off string.
    To learn about available report names, use name=show string.

    9. To convert a Family Tree on the fly to a .gramps xml file:
    gramps -O 'Family Tree 1' -e output.gramps -f gramps

    10. To generate a web site into an other locale (in german):
    LANGUAGE=de_DE; LANG=de_DE.UTF-8 gramps -O 'Family Tree 1' -a report -p name=navwebpage,target=/../de

    11. Finally, to start normal interactive session type:
    gramps

    Note: These examples are for bash shell.
    Syntax may be different for other shells and for Windows.

{{-}}

### List options

Print a list of known family trees:

Sparse  

`-l, List Family Trees`

`gramps -l`

    List of known Family Trees in your database path

    /home/<~username>/.gramps/grampsdb/5a46c1c3 with name "Example Family Tree"

{{-}}

Detailed  

`-L, List Family Trees in Detail`

`gramps -L`

    Gramps Family Trees:
    Family Tree "Example Family Tree":
       Database: SQLite
       Database module location: C:\Program Files\GrampsAIO64-6.0.3\lib\library.zip\sqlite3\__init__.pyc
       Database version: 3.50.1
       Last accessed: 03/08/2025 15:42:22
       Locked?: False
       Number of citations: 2854
       Number of events: 3436
       Number of families: 766
       Number of media: 7
       Number of notes: 19
       Number of people: 2165
       Number of places: 1296
       Number of repositories: 3
       Number of sources: 4
       Number of tags: 2
       Path: C:\Users\<~username>\AppData\Roaming\gramps\grampsdb\687d8278
       Schema version: 21.0.0

{{-}}

### Version options

`-v or --version prints version of Gramps and dependencies,`  
`     information about environment settings and python and system paths`

`gramps -v`

    Gramps Settings:
    ----------------
     gramps    : AIO64-6.0.3--1
     o.s.      : Windows

    Required:
    ---------
     Python    : 3.12.11
     Gtk++     : 3.24.49
     pygobject : 3.52.3
     Cairo     : 1.18.4
     pycairo   : 1.28.0
     Pango     : 1.56.3
     PangoCairo: 1.0
     orjson    : 3.10.18

    Recommended:
    ------------
     osmgpsmap : 1.0
     Graphviz  : 12.2
     Ghostscr. : 10.05.1
     ICU       : 3.12.10
     PyICU     : not found

    Optional:
    ---------
     Gspell     : 1
     RCS        : not found
     PILLOW     : 11.2.1
     GExiv2     : 0.10
     Exiv2 lib. : not found because exiv2 is not installed
     geocodeglib: 1.0

    Environment settings:
    ---------------------
     LANG      : en_GB.UTF-8
     LANGUAGE  : en_GB
     GRAMPSI18N: not set
     GRAMPSHOME: not set
     GRAMPSDIR : not set
     GRAMPS_RESOURCES : C:\Program Files\GrampsAIO64-6.0.3\share
     PYTHONPATH:
        C:\Program Files\GrampsAIO64-6.0.3\gramps
        C:\Program Files\GrampsAIO64-6.0.3\lib\library.zip
        C:\Users\<~username>\.local/lib/python3.12-mingw_x86_64_msvcrt_gnu/site-packages
        C:\Program Files\GrampsAIO64-6.0.3\lib
        C:\Program Files\GrampsAIO64-6.0.3
        C:\Users\<~username>\AppData\Roaming\gramps\gramps60\plugins\lib

    System PATH env variable:
    -------------------------
         C:\Program Files\GrampsAIO64-6.0.3
         C:\Program Files\GrampsAIO64-6.0.3\lib
         C:\Windows\system32
         C:\Windows
         C:\Users\admin\AppData\Local\Microsoft\WindowsApps

    Databases:
    -------------------------
     bsddb     :
         version     : 6.2.9
         db version  : 6.0.30
         location    : C:\Program Files\GrampsAIO64-6.0.3\lib\library.zip\bsddb3\__init__.pyc
     sqlite3   :
         version     : 3.50.1
         location    : C:\Program Files\GrampsAIO64-6.0.3\lib\library.zip\sqlite3\__init__.pyc

{{-}}

### Format options

The format of any file destined for opening, importing, or exporting can be specified with the

    --format=FORMAT

or

    -f FORMAT

option. The acceptable *`FORMAT`* values are listed below.

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
- **vcf** - VCard 3.0 format: import and export
- **vcs** - VCalendar format: export
- **def** - old Pro-Gen format: import
- **wft** - Web Family Tree: This format is available for export only. When not specified, it can be guessed if the filename ends with .wft

### Opening options

You can open a family tree, or you can *open* a file by importing it in an empty family tree.

To let Gramps handle this automatically, just supply the family tree or filename you want to open:

`python gramps.py 'My Fam Tree'`  
`python gramps.py JohnDoe.ged`

The first opens a family tree, the second imports a GEDCOM into an empty family tree.

Additionally, you can pass Gramps the name of the family tree to be opened:

- use this option : `-O famtree` or `--open=famtree`

`-O`, Open of a family tree. This can be done also by just typing the name (name or database dir)

Examples:

`python gramps.py 'Family Tree 1'`  
`python gramps.py /home/cristina/.gramps/grampsdb/47320f3d`  
`python gramps.py -O 'Family Tree 1'`  
`python gramps.py -O /home/cristina/.gramps/grampsdb/47320f3d`

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

You can run books from the command line using the 'book' action.

To see which ones, say:

`gramps -O "Family Tree 1" -a book`

To see a book's available options, for instance a book called "mybook":

`gramps -O "Family Tree 1" -a book -p name=mybook,show=all`

To run a book, for instance a book called "mybook":

`gramps -O "Family Tree 1" -a book -p name=mybook`

### Force unlock option

- `-u`: you can extend the `-O` flag with `-u` to force a locked family to be unlocked. This allows you to recover from a crash that leaves the family tree (database) locked, from the command line.

An example (to unlock the "Family Tree 1" database):

  
`gramps -O "Family Tree 1" -a report -u > /dev/null`

See also:

- [Manage Family Trees:Unlocking a Family Tree](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees#Unlocking_a_Family_Tree)

### Configuration (config) option

When all configuration variable(s) are set Gramps will start with these new values.

These options can takes three forms:

1\) See all config values  
`-s` or `--show`

  
For example:

`gramps --show`

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

  
For example:

`gramps --config=database.path`

    Current Gramps config setting: database.path:'/home/<~username>/.gramps/grampsdb'

3\) Set a value  
`--config=behavior.database-path:'/media/mydb'` or `-c behavior.database-path:'/media/mydb'`

  
For example:

3.1) Set a value to its default  
`--config=behavior.database-path:DEFAULT` or `-c behavior.database-path:DEFAULT`

  
For example:

3.2) Set more than one value  
`--config=behavior.use-tips:False --config=behavior.autoload:True` or `-c behavior.use-tips:False -c behavior.autoload:True`

  
For example:

### Sikker tilstand

`gramps -S` eller `gramps --safe`

Denne CLI-kommando starter Gramps, som om den aldrig havde været installeret før. I denne tilstand kan alle tidligere slægtsbøger stadig indlæses, så længe de blev gemt i standardmappen. Alle andre indstillinger, filtre, bøger, tilføjelser osv. ryddes eller sættes tilbage til deres standardværdier. Andre CLI-kommandoer kan bruges, eller hvis ingen er tilgængelige, starter Gramps den grafiske brugergrænseflade. Intet andet end de faktiske slægtstræsdata gemmes.

Bemærk, at dette typisk bruges til at se, om Gramps opfører sig bedre, når den kører, som om den havde en helt 'ren' installation. Det er IKKE permanent (hvis du ønsker det, se [Standarder](#Standarder) nedenfor). Hvis du starter Gramps normalt efter at have brugt denne kommando, er alle dine tidligere indstillinger osv. stadig der.

Dette fungerer faktisk ved at indstille den mappe, som Gramps bruger til at gemme sine brugerdata (undtagen slægtsbøger), til en midlertidig mappe, som slettes, når Gramps lukker.

### Standardindstillinger

`gramps -D E` eller `gramps --default=E`

Denne CLI-kommando får Gramps til at rydde eller vende tilbage til standardindstillingerne for de ønskede indstillinger.

Slægtsbogsdatabaserne ryddes eller fjernes IKKE.

Underkommandoerne (erstat 'E' fra eksempelkommandolinjen ovenfor med et eller flere af underkommandotegnene) er:

- `A` Tilføjelser ryddes. Alle installerede tilføjelser fjernes sammen med deres indstillinger.

<!-- -->

- `F` Filtre ryddes. Alle brugerdefinerede filtre fjernes.

<!-- -->

- `P` Præferencer vender tilbage til deres standardværdier.
- `X` Bøger ryddes, og indstillinger for rapporter og værktøjer vender tilbage til deres standardværdier.
- `Z` Gamle '.zip'-filer fra opgraderinger af slægtsbogsversioner slettes.
- `E` Alt undtagen de faktiske slægtstræsdata vender tilbage til standardindstillingerne. Dette gør alt ovenstående samt et par flere ting; sletter miniaturebilleder, kort og bruger-CSS (bruges i webrapporter).

For eksempel: gramps -D AP vil få Gramps til at fjerne alle tilføjelser og nulstille indstillinger til deres standardværdier. {{-}}

## Operation

Hvis det første argument på kommandolinjen ikke starter med en bindestreg (dvs. intet flag), vil Gramps forsøge at åbne filen med det navn, der er angivet af det første argument, og starte en interaktiv session, hvor resten af ​​kommandolinjeargumenterne ignoreres.

Hvis flaget `-O` er angivet, vil Gramps forsøge at åbne det angivne filnavn og derefter arbejde med disse data, som anvist af de yderligere kommandolinjeparametre.

Med eller uden flaget `-O` kan der være flere importer, eksporter og handlinger specificeret yderligere på kommandolinjen ved hjælp af flaget `-i`, `-e` og `-a`.

Rækkefølgen af ​​`-i`, `-e` eller `-a`-indstillingerne i forhold til hver enkelt er ligegyldig. Den faktiske udførelsesrækkefølge er altid: alle importer (hvis nogen) -\> alle eksporter (hvis nogen) -\> alle handlinger (hvis nogen).

Hvis der ikke er angivet nogen `-O` eller `-i`-indstilling, vil Gramps åbne sit hovedvindue og starte den sædvanlige interaktive session med den tomme database, da der alligevel ikke er data at behandle. (Medmindre du allerede har udtrykt en "præference" om, at den starter med den sidst brugte database.)

Hvis der ikke er angivet nogen `-e` eller `-a`-indstillinger, vil Gramps åbne sit hovedvindue og starte den sædvanlige interaktive session med databasen, der er resultatet af åbningen, og alle importer (hvis nogen). Denne database findes i en mappe under mappen *`~/.gramps/grampsdb/`*.

Eventuelle fejl, der opstår under import, eksport eller handling, vil enten blive sendt til stdout (hvis disse er undtagelser, der håndteres af Gramps) eller til stderr (hvis disse ikke håndteres). Brug sædvanlige shell-omdirigeringer af stdout og stderr til at gemme beskeder og fejl i filer. {{-}}

## Eksempler

- For at importere fire databaser (hvis formater kan bestemmes ud fra deres navne) og derefter kontrollere den resulterende database for fejl, kan man skrive:

  
`gramps -i file1.ged -i file2.gpkg -i ~/db3.gramps -i file4.wft -a check`

- For eksplicit at angive formaterne i ovenstående eksempel, tilføj filnavne med passende -f-indstillinger:

  
`gramps -i file1.ged -f gedcom -i file2.gpkg -f gramps-pkg -i ~/db3.gramps -f gramps-xml -i file4.wft -f wft -a check`

- For at registrere databasen, der er resultatet af alle importer, skal du angive -e flag (brug -f hvis filnavnet ikke tillader Gramps at gætte formatet):

  
`gramps -i file1.ged -i file2.gpkg -e ~/new-package -f gramps-pkg`

- For at gemme eventuelle fejlmeddelelser fra ovenstående eksempel i filerne outfile og errfile, kør:

  
`gramps -i file1.ged -i file2.dpkg -e ~/new-package -f gramps-pkg >outfile 2>errfile`

- For at importere tre databaser og starte en interaktiv Gramps-session med resultatet:

  
`gramps -i file1.ged -i file2.gpkg -i ~/db3.gramps`

- For at åbne en database og, baseret på disse data, generere en tidslinjerapport i PDF-format ved at placere outputtet i filen my_timeline.pdf:

  
`gramps -O 'Family Tree 1' -a report -p name=timeline,off=pdf,of=my_timeline.pdf`

- Sådan konverterer du bsddb-databasen til en .gramps xml-fil på farten:

  
`gramps -O 'Family Tree 1' -e output.gramps -f gramps-xml`

- Sådan genererer du et websted til en anden sprogindstilling (på tysk):

  
`LANGUAGE=de_DE; LANG=de_DE.UTF-8 gramps -O 'Family Tree 1' -a report -p name=navwebpage,target=/../de`

- Endelig, for at starte en normal interaktiv session, skriv:

  
`gramps`

{{-}}

## Miljøvariabler

### GRAMPSHOME

- **GRAMPSHOME** - hvis angivet, [tilsidesætter standardstien](wiki:Gramps_and_Windows#Setting_the_configuration_path) en profil, der tillader brugeren at anvende et eksternt netværksdrev til at gemme data og alle indstillinger. For teknisk avancerede brugere, der kører flere versioner af Gramps, er det at indstille \$GRAMPSHOME en måde at undgå sammenblanding mellem de forskellige versioner i Gramps [brugermappen](wiki:Gramps_Glossary/da#user_directory). Det kan også bruges til at konfigurere Gramps til at [køre fra et bærbart drev](wiki:Run_Gramps_from_a_portable_drive) eller til at forberede en [manuel installation](wiki:Installation). Stien kan også bruges til at konfigurere stien til et [separate testtræ](wiki:Gramps_for_Windows_with_MSYS2#Keep_your_GRAMPSHOME_separate) eller [udviklingstræ](wiki:Getting_started_with_Gramps_development).

For eksempel

    GRAMPSHOME=$HOME/familytrees/paternal

### LANG, LANGUAGE, LC_MESSAGES, LC_TIME

- **LANG**, **LANGUAGE**, **LC_MESSAGES** og **LC_TIME** - bruges af Gramps til at bestemme, hvilke sprogfiler der skal indlæses. Se [locale](https://pubs.opengroup.org/onlinepubs/9799919799/basedefs/V1_chap07.html) for en generel diskussion af **LANG**, **LC_MESSAGES** og **LC_TIME**. Bemærk, at udover at indstille datoformater (som tilsidesættes i Gramps med præferencer) indstiller **LC_TIME** også det sprog, der bruges til ord i datoer som måneds- og dagsnavne og *i konteksten af ​​datoer* ord som *omkring*, *mellem* og *før*. **LANGUAGE** er en kommasepareret liste over sprogkoder (*ikke lokaliteter*, selvom visse sprog som pt_BR eller cn_TW er regionale varianter), der angiver en præferenceordnet liste over ønskede oversættelser. Den vil tilsidesætte **LANG**, men ikke **LC_MESSAGES** eller **LC_TIME**.

### GRAMPSI18N

- [$GRAMPSI18N (for your locale)](wiki:Translating_Gramps#.24GRAMPSI18N_.28for_your_locale.29) - The LANG assumes the Gramps translations are installed globally. If this is not the case, you need to [give Gramps the directory](wiki:Translating_Gramps#.24GRAMPSI18N_.28for_your_locale.29) where the translations will be found. This can be used to temporarily [change the language for Reports](wiki:Howto:Change_the_language_of_reports) being generated.

A translation is called `gramps.mo`, you can find it in Linux with the locate command. For example, if you have Swedish in directory `/home/me/gramps/mo/sv/gramps.mo`, you can direct Gramps there using:

`GRAMPSI18N=/home/me/gramps/mo LC_ALL=C.UTF-8 LANG="sv" python3 gramps`

### GRAMPSDIR

- Miljøvariablen GRAMPSDIR er stien til din [Gramps-mappe](wiki:Translating_Gramps#gramps.sh).

### GRAMPS_RESOURCES

- Miljøvariablen GRAMPS_RESOURCES er stien til Gramps' indbyggede ressourcefiler. Du bør kun ændre dette, hvis du bruger Gramps fra kildekode eller et brugerdefineret miljø. En indikator for, at du skal indstille denne variabel, er, hvis du modtager en af ​​følgende fejl:
  - *Encoding error while parsing resource path*
  - *Failed to open resource file*
  - *Resource Path {invalid/path/to/resources} is invalid*
  - *Unable to determine resource path*

Example [usage](wiki:Linux:Build_from_source#Running_from_a_tarball_release):

`GRAMPS_RESOURCES=/home/username/gramps/branches/maintenance/gramps60/build/t PYTHONPATH=$GRAMPS_RESOURCES:$PYTHONPATH ./gramps`

{{-}}

[Category:Documentation](wiki:Category:Documentation)
