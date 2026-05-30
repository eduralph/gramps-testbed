---
title: Fr:Manuel wiki pour Gramps 6.0 - Les lignes de commande
categories:
- Fr:Documentation
- Stub
managed: false
source: wiki-scrape
wiki_revid: 111327
wiki_fetched_at: '2026-05-30T18:42:23Z'
lang: fr
---

{{#vardefine:chapter\|C}} {{#vardefine:figure\|0}}

Cette annexe décrit les possibilités offertes par Gramps en ligne de commande, depuis un terminal.

Normally Gramps is started through the graphical user interface (GUI) on [your platform](wiki:Gramps_6.0_Wiki_Manual_-_Getting_Started/fr).

It is also possible to start Gramps using a command line interface (CLI). CLI use can

- produce reports that are not available via the GUI,

<!-- -->

- create reports, do conversions etc. without opening a window and

<!-- -->

- can provide [extra information](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window#Seeing_all_the_error_messages) in the event of problems.

This section of the user manual describes how to start Gramps through the CLI, and the features that are available.

The way you start Gramps through the CLI depends on the operating system you are using.

For simplicity of description, the examples of use below are written from the point of view of running Gramps on Linux. The examples would need to be changed for other platforms.

### Linux

Only the Linux platform is officially supported as Gramps developers use and test the source code on that platform, fixing any problems that arise due to upgrades.

Assuming you have used the standard Package Manager (either through a CLI or a GUI) for your Linux distribution, you start Gramps through the CLI by typing

`gramps`

### MS Windows

MS Windows is a [community supported](wiki:Download#Comunity_supported) platform. If you install the [Windows AIO](wiki:All_In_One_Gramps_Software_Bundle_for_Windows) GrampsAIO32 or GrampsAIO64 executable, then this will place an icon on the desktop as well as a menu iten in the 'Start' menu.

What is the best way of knowing what command to type?

Starting Gramps from the command line (cmd.exe) depends on where you have chosen to install Gramps.

- Right click on the ??terminal Gramps application, or the corresponding item in the Start menu.

<!-- -->

- Note down the starting directory.

<!-- -->

- Select the whole of the command and copy (ctrl-C) it.

<!-- -->

- From the Start menu, start cmd.exe.

<!-- -->

- Change directory to the starting directory you noted down.

<!-- -->

- Right click and select Paste.

<!-- -->

- Press .

For example, this might be:

`cd "\Program Files\GrampsAIO64\bin`  
`   `  
`"C:\Program Files\GrampsAIO64\bin\pythonw.exe" -EO ..\share\gramps\gramps.py`  
`   `

When the instructions below tell you to type something after the start command, you just type this after the last line, for example:

`cd "\Program Files\GrampsAIO64\bin`  
`   `  
`"C:\Program Files\GrampsAIO64\bin\pythonw.exe" -EO ..\share\gramps\gramps.py -L`  
`   `

There are other ways to install Gramps for MS Windows, but these are much more complicated and are not covered here.

### Mac OS X

Mac OS X is a [community supported](wiki:Download#Comunity_supported) platform. If you download the Mac OS X disk image (.dmg), then you simply drag the application to your application folder (or anywhere else you want to store it) and start Gramps by double clicking on the application in the normal way.

To run from the command line, you'll need to start Terminal, found in Applications:Utilities.

Once you have a terminal window open, at the prompt type

` /path/to/Gramps.app/Contents/MacOS/Gramps`  
`   `

If you installed Gramps in Applications along with most of your other apps, that would be

` /Applications/Gramps.app/Contents/MacOS/Gramps`  
`   `

You may use any of the command-line options along with this. For example, to get a detailed listing of all of the Family Tree databases in your default Family Tree folder, you would use

` /Applications/Gramps.app/Content/MacOS/Gramps -L`  
`   `

There are other ways to install Gramps for Mac OS X, but these are much more complicated and are not covered here.

## Python options

In the examples of different platforms above, and also in commands in various files you may see some options after the 'python' command, for example '-EO' in

`"C:\Program Files\GrampsAIO64\bin\pythonw.exe" -EO ..\share\gramps\gramps.py -L`  
`   `

It is important to distinguish between the **python options** in this case:

`-EO`  
`   `

and the **Gramps options**, in this case

`-L`  

The **python options** that you may come across are:

- -E Ignore all PYTHON\* environment variables, e.g. PYTHONPATH and PYTHONHOME, that might be set.

<!-- -->

- -O Turn on basic optimizations. This changes the filename extension for compiled (bytecode) files from .pyc to .pyo. See also PYTHONOPTIMIZE.

The -O optimise flag has a number of effects in Gramps:

- If it is not turned on, an additional **Debug** entry appears in the **Tools** menu.

<!-- -->

- If it is not turned on, [info logging messages are output](wiki:Logging_system#So_how_logging_works_in_Gramps_after_all.3F).

<!-- -->

- If it is not turned on, [debug statements](wiki:Debugging_Gramps#Add_debug_statements) may be activated.

<!-- -->

- If it is not turned on, additional features are available in the [Plugin Manager](wiki:Gramps_6.0_Wiki_Manual_-_Plugin_Manager).

The **Gramps options** are described below.

## Options disponibles

Voici la liste des options de lancement de Gramps. Si vous voulez connaître plus d'options, voir [Opération](#Opération) et [Exemples](#Exemples). Une liste est également disponible sur [cette page](wiki:Plugins_Command_Line). Le résumé suivant est obtenu par la commande *gramps -h* et *gramps --usage*.

`Utilisation : gramps.py [OPTION...]`  
` --load-modules=MODULE1,MODULE2,...     Modules dynamiques à charger`

`Options d'aide`  
` -?, --help                             Affiche ce message d'aide`  
` --usage                                Affiche une aide à l'utilisation`

`Options de l'application`  
` -O, --open=ARBRE_FAMILIAL              Ouvre l'arbre familial`  
` -C, --create=ARBRE_FAMILIAL            Créé à l'ouverture si arbre familial`  
` -i, --import=FICHIER                   Importe un fichier`  
` -e, --export=FICHIER                   Exporte un fichier`  
` -f, --format=FORMAT                    Spécifie le format de l'arbre`  
` -a, --action=ACTION                    Spécifie l'action`  
` -p, --options=OPTIONS                  Spécifie les options`  
` -d, --debug=NOM_DE_LOGGER              Active les logs de déboguage`  
` -l                                     Liste les arbres familiaux`  
` -L                                     Liste les arbres familiaux en détail`  
` -t                                     Liste les arbres familiaux dans un format tabulaire (tab)`  
` -u, --force-unlock                     Force le déverrouillage de l'arbre`  
`                                        familial`  
` -s, --show                             Affiche les paramètres de configuration`  
` -c, --config=[config.setting[:value]]  Définit les paramètre(s) de`  
`                                        configuration et lance Gramps`  
` -v, --version                          Affiche les versions des bibliothèques`

`Exemples d'utilisation de l'interface en ligne de commande Gramps`

`1. Importer quatre bases de données (dont les formats sont déterminés depuis leurs noms) puis `  
`vérifier les bases résultantes, on peut faire :`  
`gramps -i file1.ged -i file2.gpkg -i ~/db3.gramps -i file4.wft -a tool -p name=check`

`2. Spécifier explicitement les formats dans l'exemple précédent, ajouter l'option -f après les `  
`noms de fichier :`  
`gramps -i file1.ged -f gedcom -i file2.gpkg -f gramps-pkg -i ~/db3.gramps -f gramps-xml -i `  
`file4.wft -f wft -a tool -p name=check`

`3. Enregistrer les bases de données résultantes des importations, utilisez l'option -e (préférez `  
`-f si le nom du fichier ne permet pas à Gramps de deviner le format) :`  
`gramps -i file1.ged -i file2.gpkg -e ~/nouveau-paquet -f gramps-pkg`

`4. Sauver tout message d'erreur de l'exemple précédent dans fichier_sortie et fichier_erreurs, lancez :`  
`gramps -i file1.ged -i file2.dpkg -e ~/nouveau-paquet -f gramps-pkg >fichier_sortie 2>fichier_erreurs`

`5. Importer trois bases de données et débuter une session interactive de Gramps avec le résultat :`  
`gramps -i file1.ged -i file2.gpkg -i ~/db3.gramps`

`6. Ouvrir une base de données et, basé sur ces données, générer le rapport graphique temporel `  
`au format PDF dont le fichier de sortie sera fil_du_temps.pdf :`  
`gramps -O 'Family Tree 1' -a report -p name=timeline,off=pdf,of=fil_du_temps.pdf`

`7. Générer un résumé de la base de données « Arbre de famille 1 » :`  
`gramps -O 'Arbre de famille 1' -a report -p name=summary`

`8. Lister les options d'un rapport :`  
`- Utiliser name=timeline,show=all pour trouver toutes les options disponibles du rapport graphique `  
`temporel.`  
`- Pour obtenir les détails d'une option particulière, utiliser show=option_name, par exemple : `  
`name=timeline,show=off.`  
`- Pour en savoir plus sur les noms de rapport disponibles, utilisez la chaîne name=show.`

`9. Convertir un arbre familial vers un fichier XML .gramps :`  
`gramps -O 'Family Tree 1' -e output.gramps -f gramps-xml`

`10. Générer un site internet dans une autre langue (par exemple en allemand) :`  
`LANGUAGE=de_DE; LANG=de_DE.UTF-8 gramps -O 'Arbre de famille 1' -a report -p `  
`name=navwebpage,target=/../de`

`11. Enfin, pour démarrer une session interactive normale, saisissez:`  
`gramps`

`Note : ces exemples sont pour le shell bash.`  
`La syntaxe peut être différente pour les autres shells ou sous Windows.`

### Options de liste

`-l, imprime une liste des arbres familiaux connus.`

![[_media/CommandLineExampleOutput-l-40.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Command Exemple de sortie en ligne de commande pour <em>python gramps.py -l</em>]]

  

`-L, imprime une liste détaillée des arbres familiaux connus.`

![[_media/CommandLineExampleOutput_L-40.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Command Exemple de sortie en ligne de commande pour <em>python gramps.py -L</em>]]

  
Note that dates are shown in the default LOCALE format. You change that at the system level. For example, on POSIX-based systems you could:

`LC_TIME=fr_CA.UTF-8 gramps -L`

{{-}}

### Options de version

`-v ou --version imprime la version de Gramps et ses dependances,`  
`     l'information sur l'environment, sur python et les chemins système.`

![[_media/CommandLineExampleOutput-v-40.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Command Exemple de sortie en ligne de commande pour python gramps.py -v]] {{-}}

### Options de format

Le format de chaque fichier destiné à être ouvert, importé, ou exploré peut être spécifié avec l'option

    -f format

. Les valeurs de *`format`* acceptables sont listées ci-dessous.

#### Support complet de l'arbre familial

Ces formats contiennent toutes les données présentes dans votre arbre familial.

- **gramps** - le format Gramps XML : ce format est prêt à l'importation et à l'exportation. Une fois indiqué, il peut deviner si le fichier représente un nom de fichier .gramps
- **gpkg** - le paquet Gramps XML format : ce format est prêt à l'importation et à l'exportation. Une fois indiqué, il peut deviner si le fichier représente un nom de fichier .gpkg. Il s'agit d'une archive avec vos données au format xml, et tous vos fichiers media.
- **grdb** - la base antérieurs à Gramps 3.x : ce format est prêt et à l'importation de cette ancienne version de la base de données. Une fois indiqué, il peut deviner si le fichier porte l'extension .grdb.
- **burn** - la gravure de GNOME : exportation, seulement disponible si le protocole de gravure GNOME est disponible.

#### Support réduit de l'arbre familial

Ces formats contiennent la plupart, mais pas la totalité des données pouvant être gérées dans Gramps.

- **ged** - le format GEDCOM : ce format est disponible pour l'importation et l'exportation. Si le format n'est pas spécifié, il peut être deviné si l'extension est .ged.
- **gw** - le fichier GeneWeb : ce format est disponible pour l'importation et l'exportation. Si le format n'est pas spécifié, il peut être deviné si l'extension est .gw

#### Partie de vos données

Ces formats contiennent une partie de vos données

- **csv** - valeurs séparées par des virgules : ce format est disponible pour l'importation et l'exportation. Soyez prudent, l'importation doit correspondre aux données créées par la fonction d'exportation. Seul une partie de vos données est présente.
- **vcf** - le format VCard: importation et exportation
- **vcs** - le format VCalander format: exportation
- **def** - ancien format Pro-Gen : importation
- **wft** - Web Family Tree: ce format est seulement disponible pour l'exportation. Si il n'est pas spécifié, il peut être deviné si l'extension est .wft

### Options d'ouverture

Vous pouvez ouvrir un arbre familial, ou vous pouvez *ouvrir* un fichier et l'importer dans un arbre familial vide. Pour laisser Gramps gérer ceci automatiquement, ajouter l'arbre familial ou le nom du fichier que vous désirez ouvrir :

`python gramps.py 'My Fam Tree'`  
`python gramps.py JohnDoe.ged`

Le premier ouvre un arbre familial, le second importe un gedcom dans un arbre familial vide.

Par ailleurs, vous pouvez donner à Gramps le nom ou le chemin du fichier à ouvrir :

- utilisez l'option :
      -O nom_du_fichier

  ou

      --open=nom_du_fichier

-O, ouvre un arbre familial. Ceci est également possible en saisissant le nom (nom ou répertoire de la base de données)

Exemples :

`python gramps.py 'Arbre familial 1'`  
`python gramps.py /home/cristina/.gramps/grampsdb/47320f3d`  
`python gramps.py -O 'Arbre familial 1'`  
`python gramps.py -O /home/cristina/.gramps/grampsdb/47320f3d`

### Options d'importation

Les dossiers destinés à l'importation peuvent être indiqués avec

    -i ''nom du fichier''

ou

    --import=''nom du fichier''

Le format peut être indiqué avec l'option

    -f format

ou

    --format=format

juste après *nom de fichier*.

Exemple:

`  python gramps.py -i 'Arbre familial 1' -i 'Arbre familial 2'`  
`  python gramps.py -i test.grdb -i données.gramps`

Quand plus d'un dossier d'entrée est donné, chacun doit être par précédé de

    -i

Les dossiers sont importés dans l'ordre indiqué, c.-à-d..

     -i ''fichier1'' -i ''fichier2''

et

     -i ''fichier2'' -i ''fichier1''

pourraient produire différentes versions dans la base de données résultant.

### Options d'exportation

Les dossiers destinés à l'exportation peuvent être indiqués avec

    -e ''nom du fichier''

ou

    --export=''nom du fichier''

Le format peut être indiqué avec l'option

    -f

juste après *le nom du fichier*. Pour gramps-xml et les formats iso, *nom du fichier* est réellement le nom du répertoire la base de données de gramps. Pour gedcom, wft, geneweb, et gramps-pkg,*le nom du fichier* est le nom du dossier résultant.

-e, exporte l'arbre familial dans le format requis. Il n'est pas possible d'exporter vers un arbre familial.

Exemple:

` python gramps.py -i 'Arbre familial 1' -i test.grdb -f grdb -e mergdeDB.gramps`

Notez qu'on ne modifie pas 'Arbre familial 1' puisque l'on utilise une base temporaire, et:

` python gramps.py -O 'Arbre familial 1' -i test.grdb -f grdb -e mergdeDB.gramps`

qui importera test.grdb dans Arbre familial 1, puis l'exporte dans un fichier !

Quand plus d'un fichier est donné, chacun doit être par précédé par

    -e

. Les dossiers sont écrits dans l'ordre indiqué.

### Options d'action

L'action à exécuter sur les données importées peut être indiquée avec

    -a action

ou

    --action=action

Ceci est fait après que toutes les importations soient accomplies avec succès.

Les actions actuellement disponibles sont :

- *summary* : cette action est identique à

<!-- -->

- *check* : cette action est identique à .

<!-- -->

- *tool* : cette annexe décrit les possibilités offertes par Gramps en ligne de commande, depuis un terminal.

<!-- -->

- *rapport* : cette action permet de produire des rapports à partir de la ligne de commande. Comme les rapports ont généralement beaucoup d'options propres, cette action doit être suivie de la chaîne d'options du rapport. La chaîne est donnée en utilisant
      -p option_string

  ou

      --options=option_string

  .

La plupart des options de rapport sont spécifiques pour chaque rapport. Cependant, il y a quelques options communes.

- name=report_name : Cette option obligatoire détermine quel rapport sera produit. Si le report_name ne correspond à aucun rapport disponible, le message d'erreur sera affiché à la suite de la liste de rapports disponibles.

<!-- -->

- of : nom du fichier créé par le rapport.

<!-- -->

- off: format du fichier créé. Par exemple pdf, html, odt, ...

<!-- -->

- style: pour les rapports textuels, la feuille de style à utiliser. Par défaut, la valeur est 'default'.

<!-- -->

- show=all : ceci affichera la liste de noms pour toutes les options disponibles pour un rapport présenté.

<!-- -->

- show=option_name : ceci affichera la description de la fonctionnalité assurée par l'option_name, pour les types et les valeurs acceptables pour cette option.

Employez les options ci-dessus pour découvrir tout au sujet d'un rapport présenté.

Quand plus d'une action à produire est donnée, chacunes doivent être précédée par

    -a

. Les actions sont effectuées dans l'ordre indiqué.

### Option pour forcer le déblocage

-u, vous pouvez étendre l'argument -O avec -u pour forcer une base de données à être débloquée. Ceci permet d'accéder depuis la ligne de commande à l'arbre familial bloqué après un crash.

Notez, il est impossible d'ouvrir un arbre familial depuis la ligne de commande alors qu'il a besoin d'être réparé.

### Option de configuration (config)

The option takes three forms: (the following examples, except 3.2, use behavior.database-path as the configuration variable to change.)

1\) See all config values

`-s or --show`

![[_media/CommandLineExampleOutput-s-40.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Command Line Example Output for python gramps.py -s]] {{-}}

2\) See a value:

`--config=behavior.database-path`  
`or`  
`-c behavior.database-path`

3\) Set a value:

`--config=behavior.database-path:'/media/mydb'`  
`or`  
`-c behavior.database-path:'/media/mydb'`

3.1) Set a value to its default:

`--config=behavior.database-path:DEFAULT`  
`or`  
`-c behavior.database-path:DEFAULT`

3.2) Set more than one value:

`--config=behavior.use-tips:False --config=behavior.autoload:True`  
`or`  
`-c behavior.use-tips:False -c behavior.autoload:True`

When all configuration variable(s) are set Gramps will start with these new values.

## Opération

Si le premier argument sur la ligne de commande ne commence pas par le tiret, Gramps essayera d'ouvrir le dossier avec le nom donné par le premier argument et de commencer la session interactive, ignorant le reste des arguments de ligne de commande.

Si

    -O

est donné, alors Gramps essayera d'ouvrir le nom de fichier fourni et fonctionnera alors avec ces données.

Avec ou sans l'argument

    -O

, il peut y avoir de multiples importations , exportations, et actions spécifiées par la ligne de commande par les arguments

    -i

,

    -e

, et

    -a

.

L'ordre des options

    -i

,

    -e

, ou

    -a

entre elles n'a pas de signification. L'ordre réel d'exécution est toujours : les lectures (s'il y en a) puis les écritures (s'il y en a) et enfin les actions (s'il y en a).

'

Si aucune option

    -O

ou

    -i

n'est donnée, gramps ouvrira sa fenêtre principale et commencera une session interactive avec un ensemble vide de données puisqu'il n'y a pas de données à traiter.

Si aucune option

    -e

ou

    -a

n'est donnée, gramps ouvrira sa fenêtre principale et commencera une session interactive avec les données lues. *import_db.grdb* se situera dans le répertoire *~/.gramps/import/*.

Les erreurs trouvées pendant les phases de lecture, d'écriture et d'action sont rapportées soit sur la sortie standard quand elles sont gérées par gramps, soit sur la sortie d'erreur dans le cas contraire. Utilisez les redirections du shell pour les conserver dans des fichiers.

## Exemples

- Lecture de quatre bases de données dont les formats peuvent être devinés d'après les noms, puis vérification des données :

  
    gramps -i fichier1.ged -i fichier2.gpkg -i ~/db3.gramps -i fichier4.wft -a check

- Si vous voulez préciser les formats de fichiers dans l'exemple ci-dessus, complétez les noms de fichiers par les options
      -f

  appropriées :

  
    gramps -i fichier1.ged -f gedcom -i fichier2.gpkg -f gramps-pkg -i ~/db3.gramps -f gramps-xml -i fichier4.wft -f wft -a check

- Pour enregistrer le résultat des lectures, donnez l'option
      -o

  (utiliser

      -f

  si le nom de fichier ne permet pas à gramps de deviner le format) :

  
    gramps -i fichier1.ged -i fichier2.gpkg -e ~/nouveau-paquet -f gramps-pkg

- Pour sauver les erreurs de l'exemple précédent dans les fichiers outfile et errfile, lancez :

  
    gramps -i fichier1.ged -i fichier2.dpkg -e ~/nouveau-paquet -f gramps-pkg >outfile 2>errfile 

- Pour lire trois ensembles de données puis lancer une session interactive de gramps sur le tout:

  
    gramps -i fichier1.ged -i fichier2.gpkg -i ~/db3.gramps 

- Pour ouvrir une base de données, produisant un rapport temporel dans le format pdf et l'enregistrant sous le fichier *my_timeline.pdf* :

  
    gramps -O 'Arbre Familial 1' -a report -p name=timeline,off=pdf,of=my_timeline.pdf 

- Pour convertir une base de données vers un fichier gramps xml :

  
    gramps -O 'Arbre Familial 1' -e sortie.gramps -f gramps-xml

- Pour générer un site web dans une autre langue (par exemple en allemand)

<!-- -->

    LANGUAGE=de_DE; LANG=de_DE.UTF-8 gramps -O 'Arbre familial 1' -a report -p name=navwebpage,target=/../de 

- Enfin, pour lancer une session interactive normale, entrez :

  
    gramps 

## Variables d'environnement

Gramps peut tenir compte de ces variables d'environnement (mais ne les changez pas si vous ne savez pas pourquoi):

- **GRAMPSHOME** - si défini, écrase le chemin par défaut du profil permettant d'utiliser un disque réseau pour sauvegarder ses données et préférences.
- **LANG** - est utilisé par Gramps pour déterminer quelle langue doit être chargée.

{{-}}

[M](wiki:Category:Fr:Documentation)
