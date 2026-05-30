---
title: Gramps 6.0 Wiki Manual - Command Line
categories:
- Documentation
managed: false
source: wiki-scrape
wiki_revid: 130276
wiki_fetched_at: '2026-05-30T11:10:03Z'
---

{{#vardefine:chapter\|C}} {{#vardefine:figure\|0}} This appendix provides the reference to the command line capabilities available when launching **Gramps (for desktops)** from the command line.

## Start Gramps through the Command Line

Normally Gramps is started through the graphical user interface (GUI) on [your platform](wiki:Gramps_6.0_Wiki_Manual_-_Getting_started#Start_Gramps).

It is also possible to start Gramps using a command line interface (CLI). CLI use can

- produce reports that are not available via the GUI,
- create reports, do conversions etc. without opening a window and
- can provide [extra information](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window#Seeing_all_the_error_messages) in the event of problems.

This section of the user manual describes how to start Gramps through the CLI, and the features that are available.

The way you start Gramps through the CLI depends on the operating system you are using.

For simplicity of description, the examples of use below are written from the point of view of running Gramps on Linux. The examples would need to be changed for other platforms.

### Linux

Linux platform is the main *officially* supported platform. (Other platforms are *community supported*.) This is because Gramps developers design, code, use and test the source code on that platform. So diagnosing and fixing any problems that arise (whether due to upgrades or other causes) is done using Linux tools.

Assuming you have used the standard Package Manager (either through a CLI or a GUI) for your Linux distribution, you start Gramps through the CLI by typing:

`gramps`

If you have done a "[build from source](wiki:Linux:Build_from_source)", navigate to where you installed the application. (That folder will include the `Gramps.py` file.) Type:

`python3 Gramps.py`

### MS Windows

MS Windows is an [officially supported](wiki:Download) platform. If you install the [Windows AIO bundle](wiki:All_In_One_Gramps_Software_Bundle_for_Windows), then this will place an icon on the desktop as well as a menu item in the 'Start' menu. However, the Gramps installation directory is not added to the system path and to run gramps via CLI, we need to know the path to that directory.

To find the installation folder, refer to  

- [AIO bundle's installation folder section](wiki:All_In_One_Gramps_Software_Bundle_for_Windows#Installation_folder).

To find the path using a shortcut icon instead  

- Right-click on the `GrampsAIO64 ``-console` application, or the corresponding item in the Start menu.
- Note down the file location (its "Start in' directory).
- Select the full path and copy () it.

To run Gramps from the command line, you'll need to start a console window  

- From the Start menu, start cmd.exe.
- Change directory to the installation directory you located.
- Type in or paste the path, surrounding it in quotes if there are spaces.
- Press .

For example, this might be:

`cd "C:\Program Files\GrampsAIO64-``"`  
`gramps`

You may use any of the command-line options along with this. For example, to get a detailed listing of all of the Family Tree databases in your default Family Tree folder, you would append `-L`

`cd "C:\Program Files\GrampsAIO64-``"`  
`gramps -L`

See also:

- Example usage <https://github.com/gramps-project/addons-source/pull/121>

### macOS

macOS is a [community supported](wiki:Download) platform. If you download the macOS disk image (.dmg), then you simply drag the application to your application folder (or anywhere else you want to store it) and start Gramps by double clicking on the application in the normal way. The [Homebrew package manager](https://github.com/Homebrew) also allows for installation of the application in the usual Applications folder.

To run from the command line, you'll need to start Terminal, found in the Utilities folder of the main Applications folder (/Applications/Utilities). Once you have a terminal window open, at the prompt type

` /path/to/Gramps.app/Contents/MacOS/Gramps`

If you installed Gramps in Applications along with most of your other apps, as suggested above, that would be

` /Applications/Gramps.app/Contents/MacOS/Gramps`

You may use any of the command-line options along with this. For example, to get a detailed listing of all of the Family Tree databases in your default Family Tree folder, you would use

` /Applications/Gramps.app/Contents/MacOS/Gramps -L`

There are other ways to install Gramps for macOS, but these are much more complicated and are not covered here.

## Python options

In the examples of different platforms above, and also in commands in various files you may see some options after the 'python' command, for example '-EO' in

`"python3 -EO ..\share\gramps\gramps.py -L`

It is important to distinguish between the **python options** in this case:

`-EO`

and the **Gramps options**, in this case

`-L`

The **python options** that you may come across are:

- `-E` Ignore all PYTHON\* environment variables, e.g. `PYTHONPATH` and `PYTHONHOME`, that might be set.
- `-O` Turn on basic optimizations. This changes the filename extension for compiled (bytecode) files from `.pyc` to `.pyo`. See also PYTHONOPTIMIZE.

The `-O` optimise flag has a number of effects in Gramps:

- If it is not turned on, an additional entry appears in the menu.
- If it is not turned on, [info logging messages are output](wiki:Logging_system#So_how_logging_works_in_Gramps_after_all.3F).
- If it is not turned on, [debug statements](wiki:Debugging_Gramps#Add_debug_statements) may be activated.
- If it is not turned on, additional features are available in the [Plugin Manager](wiki:Gramps_6.0_Wiki_Manual_-_Plugin_Manager).

The **Gramps options** are described below.

## Available Gramps options

This section provides the reference list of all command line options available in Gramps. If you want to know more than just a list of options, see next sections: [Operation](#Operation) and [Examples](#Examples).

### Help options

The summary below is printed by

`gramps --help`

or

`gramps -h`

`Usage: gramps [OPTION...]`  
`  --load-modules=MODULE1,MODULE2,...     Dynamic modules to load`  
  
` Help options`  
`  `[<code>-?, --help</code>](#Help_options)`                             Show this help message`  
`  `[<code>--usage</code>](#Usage_message)`                                Display brief usage message`  
  
` Application options`  
`  `[<code>-O, --open=FAMILY_TREE</code>](#Opening_options)`                 Open Family Tree`  
`  -U, --username=USERNAME                Database username`  
`  -P, --password=PASSWORD                Database password`  
`  -C, --create=FAMILY_TREE               Create on open if new Family Tree`  
`  `[<code>-i, --import=FILENAME</code>](#Import_options)`                  Import file`  
`  `[<code>-e, --export=FILENAME</code>](#Export_options)`                  Export file`  
`  -r, --remove=FAMILY_TREE_PATTERN       Remove matching Family Tree(s) (use regular expressions)`  
`  `[<code>-f, --format=FORMAT</code>](#Format_options)`                    Specify Family Tree format`  
`  `[<code>-a, --action=ACTION</code>](#Action_options)`                    Specify action`  
`  -p, --options=OPTIONS_STRING           Specify options`  
`  -d, --debug=LOGGER_NAME                Enable debug logs`  
`  `[<code>-l [FAMILY_TREE_PATTERN...</code>](#List_options)`]            List Family Trees`  
`  `[<code>-L [FAMILY_TREE_PATTERN...</code>](#List_options)`]            List Family Trees in Detail`  
`  -t [FAMILY_TREE_PATTERN...]            List Family Trees, tab delimited`  
`  `[<code>-u, --force-unlock</code>](#Force_unlock_option)`                     Force unlock of Family Tree`  
`  `[<code>-s, --show</code>](#Configuration_(config)_option)`                             Show config settings`  
`  `[<code>-c, --config=[config.setting[:value</code>](#Configuration_(config)_option)`]]  Set config setting(s) and start Gramps`  
`  -y, --yes                              Don't ask to confirm dangerous actions (non-GUI mode only)`  
`  -q, --quiet                            Suppress progress indication output (non-GUI mode only)`  
`  `[<code>-v, --version</code>](#Version_options)`                          Show versions`  
`  `[<code>-S, --safe</code>](#Safe_mode)`                             Start Gramps in 'Safe mode'`  
`                                         (temporarily use default settings)`  
`  `[<code>-D, --default=[APXFE</code>](#Defaults)`]                  Reset settings to default;`  
`                 A - addons are cleared`  
`                 P - Preferences to default`  
`                 X - Books are cleared, reports and tool settings to default`  
`                 F - filters are cleared`  
`                 E - Everything is set to default or cleared`

### Usage message

The usage message is as follows:

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

Tab delimited  

`-t, List Family Trees tab delimited`

`gramps -t`

    gramps -t "Example6_0"
    Gramps Family Trees:
    Family Tree Database    Database module location    Database version    Last accessed   Locked? Number of citations Number of events    Number of families  Number of media Number of notes Number of people    Number of places    Number of repositories  Number of sources   Number of tags  Path    Schema version
    "Example6_0"    "SQLite"    "/Applications/Gramps-6.0.4-Intel/Gramps.app/Contents/Resources/lib/python3.13/sqlite3/__init__.py" "3.49.1"    "06/04/2026 21:47:31"   "False" "2854"  "3432"  "762"   "7" "19"    "2157"  "1296"  "3" "4" "2" "/Users/name/Library/Application Support/gramps/grampsdb/69d13149"  "21.0.0"

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

### Safe mode

`gramps -S` or `gramps --safe`

This CLI command starts Gramps as if it had never been installed before. In this mode, any previous family trees can still be loaded, as long as they were stored in the default folder. All other settings, filters, books, addons etc. are either cleared or returned to their default values. Other CLI commands can be used, or, if none, Gramps will start the GUI. Nothing except the actual family tree data is saved.

Note that this is typically used to see if Gramps behaves better when it is running as if with a totally 'clean' install. It is NOT permanent (if you want that see [Defaults](#Defaults) below), if you start Gramps normally after using this command all of your previous settings etc. are still there.

This actually works by setting the folder that Gramps uses to store its user data (except for family trees) to a temporary directory, which is deleted when Gramps closes.

### Defaults

`gramps -D E` or `gramps --default=E`

This CLI command causes Gramps to clear out or return to defaults the desired settings. The family tree databases are NOT cleared out or removed. The sub-commands (replace the 'E' from the example command line above with one or more of the subcommand characters) are:

- `A` Addons are cleared. Any installed addons are removed, along with their settings.
- `F` Filters are cleared. Any custom filters are removed.
- `P` Preferences are returned to their default values.
- `X` Books are cleared, Reports and Tools settings are returned to their default values.
- `Z` Old '.zip' files from family tree version upgrades are deleted.
- `E` Everything except the actual family tree data is returned to default settings. This does all of the above as well as a few more items; deletes thumbnails, maps, and the user CSS (used in web reports).

For example:

`gramps -D AP`

will cause Gramps to remove all the Addons and to reset Preferences to their default values.

## Operation

If the first argument on the command line does not start with a dash (i.e. no flag), Gramps will attempt to open the file with the name given by the first argument and start an interactive session, ignoring the rest of the command line arguments.

If the `-O` flag is given, then Gramps will try opening the supplied file name and then work with that data, as instructed by the further command line parameters.

With or without the `-O` flag, there could be multiple imports, exports, and actions specified further on the command line by using `-i` , `-e` , and `-a` flags.

The order of `-i` , `-e` , or `-a` options with respect to each does not matter. The actual execution order always is: all imports (if any) -\> all exports (if any) -\> all actions (if any).

If no `-O` or `-i` option is given, Gramps will launch its main window and start the usual interactive session with the empty database, since there is no data to process, anyway. (Unless you have already expressed a "preference" that it start with the last database it used.)

If no `-e` or `-a` options are given, Gramps will launch its main window and start the usual interactive session with the database resulted from opening and all imports (if any). This database resides in a directory under the *`~/.gramps/grampsdb/`* directory.

Any errors encountered during import, export, or action, will be either dumped to stdout (if these are exceptions handled by Gramps) or to stderr (if these are not handled). Use usual shell redirections of stdout and stderr to save messages and errors in files.

## Examples

- To import four databases (whose formats can be determined from their names) and then check the resulting database for errors, one may type:

  
`gramps -i file1.ged -i file2.gpkg -i ~/db3.gramps -i file4.wft -a check`

- To explicitly specify the formats in the above example, append filenames with appropriate -f options:

  
`gramps -i file1.ged -f gedcom -i file2.gpkg -f gramps-pkg -i ~/db3.gramps -f gramps-xml -i file4.wft -f wft -a check`

- To record the database resulting from all imports, supply -e flag (use -f if the filename does not allow Gramps to guess the format):

  
`gramps -i file1.ged -i file2.gpkg -e ~/new-package -f gramps-pkg`

- To save any error messages of the above example into files outfile and errfile, run:

  
`gramps -i file1.ged -i file2.dpkg -e ~/new-package -f gramps-pkg >outfile 2>errfile`

- To import three databases and start interactive Gramps session with the result:

  
`gramps -i file1.ged -i file2.gpkg -i ~/db3.gramps`

- To open a database and, based on that data, generate timeline report in PDF format putting the output into the my_timeline.pdf file:

  
`gramps -O 'Family Tree 1' -a report -p name=timeline,off=pdf,of=my_timeline.pdf`

- To convert the bsddb database on the fly to a .gramps xml file:

  
`gramps -O 'Family Tree 1' -e output.gramps -f gramps-xml`

- To generate a web site into an other locale (in German):

  
`LANGUAGE=de_DE; LANG=de_DE.UTF-8 gramps -O 'Family Tree 1' -a report -p name=navwebpage,target=/../de`

- Finally, to start normal interactive session type:

  
`gramps`

## Environment variables

### GRAMPSHOME

- **GRAMPSHOME** - if set, [override default path](wiki:Gramps_and_Windows#Setting_the_configuration_path) to profile allowing user to use an external network drive to store data and all settings. For technically advanced users who run multiple versions of Gramps, setting a different \$GRAMPSHOME is a way to avoid interference between the different versions in the Gramps [User Directory](wiki:Gramps_Glossary#user_directory). It can also be used to configure Gramps to [run from a portable drive](wiki:Run_Gramps_from_a_portable_drive) or to prepare for a [manual installation](wiki:Installation). The path can also be used to configure the path to a [separate test Tree](wiki:Gramps_for_Windows_with_MSYS2#Keep_your_GRAMPSHOME_separate) or [development Tree](wiki:Getting_started_with_Gramps_development).

For example

    GRAMPSHOME=$HOME/familytrees/paternal

### LANG, LANGUAGE, LC_MESSAGES, LC_TIME

- **LANG**, **LANGUAGE**, **LC_MESSAGES**, and **LC_TIME** - are used by Gramps to determine which language file(s) should be loaded. See [locale](https://pubs.opengroup.org/onlinepubs/9799919799/basedefs/V1_chap07.html) for a general discussion of **LANG**, **LC_MESSAGES**, and **LC_TIME**. Note that in addition to setting date formats (which are overridden in Gramps with Preferences settings) **LC_TIME** also sets the language used for words in dates like month and day names and *in the context of dates* words like *about*, *between*, and *before*. **LANGUAGE** is a comma-separated list of language codes (*not locales*, though certain languages like pt_BR or cn_TW are regional variants) that sets a preference-ordered list of desired translations. It will override **LANG** but not **LC_MESSAGES** or **LC_TIME**.

### GRAMPSI18N

- [$GRAMPSI18N (for your locale)](wiki:Translating_Gramps#.24GRAMPSI18N_.28for_your_locale.29) - The LANG assumes the Gramps translations are installed globally. If this is not the case, you need to [give Gramps the directory](wiki:Translating_Gramps#.24GRAMPSI18N_.28for_your_locale.29) where the translations will be found. This can be used to temporarily [change the language for Reports](wiki:Howto:Change_the_language_of_reports) being generated.

A translation is called `gramps.mo`, you can find it in Linux with the locate command. For example, if you have Swedish in directory `/home/me/gramps/mo/sv/gramps.mo`, you can direct Gramps there using:

`GRAMPSI18N=/home/me/gramps/mo LC_ALL=C.UTF-8 LANG="sv" python3 gramps`

### GRAMPSDIR

- The environment variable GRAMPSDIR is the path to your [Gramps directory](wiki:Translating_Gramps#gramps.sh).

### GRAMPS_RESOURCES

- The environment variable GRAMPS_RESOURCES is the path to Gramps built-in resources files. You should only change this if you are using Gramps from source code or a custom environment. An indicator that you need to set this variable is if you receive one of the following errors:
  - *Encoding error while parsing resource path*
  - *Failed to open resource file*
  - *Resource Path {invalid/path/to/resources} is invalid*
  - *Unable to determine resource path*

Example [usage](wiki:Linux:Build_from_source#Running_from_a_tarball_release):

`GRAMPS_RESOURCES=/home/username/gramps/branches/maintenance/gramps60/build/t PYTHONPATH=$GRAMPS_RESOURCES:$PYTHONPATH ./gramps`

{{-}}

[Category:Documentation](wiki:Category:Documentation)
