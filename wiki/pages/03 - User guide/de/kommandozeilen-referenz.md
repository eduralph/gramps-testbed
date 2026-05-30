---
title: De:Gramps 6.0 Wiki Handbuch - Kommandozeilen Referenz
categories:
- De:Dokumentation
managed: false
source: wiki-scrape
wiki_revid: 130897
wiki_fetched_at: '2026-05-30T18:06:33Z'
lang: de
---

{{#vardefine:chapter\|C}} {{#vardefine:figure\|0}} Dieser Anhang liefert eine Referenz über die Möglichkeiten **Gramps (für Desktops)** von der Kommandozeile starten.

## Gramps über die Kommandozeile starten

Normalerweise startest du Gramps über die Grafischebenutzerschnittstelle (GUI) auf [deiner Plattform](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Erste_Schritte#Gramps_starten).

Es ist auch möglich, Gramps über eine Kommandozeilenschnittstelle zu starten (CLI). Über die CLI kannst du

- Berichte erstellen, die nicht über die GUI verfügbar sind,
- Berichte erstellen, Konvertierungen usw. durchführen ohne ein Fenster zu öffnen und
- kann [zusätzliche Informationen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Hauptfenster#Alle_Fehlermeldungen_sehen) im Fall von Problemen liefern.

Dieser Abschnitt des Benutzerhandbuchs beschreibt, wie Gramps über das CLI gestartet wird, und die zur Verfügung stehenden Funktionen.

Die Art wie du Gramps über das CLI startest, hängt von dem Betriebssystem, das du verwendest ab.

Zur Vereinfachung der Beschreibung, sind die Beispiele unten aus der Sicht von der Verwendung von Gramps unter Linux geschrieben. Die Beispiele müssen bei Bedarf für andere Plattformen angepasst werden.

### Linux

Die Linux-Plattform ist die Haupt *offiziell* unterstützte Plattform. (Andere Plattformen werden von der Gemeinschaft unterstützt.) Das liegt daran, dass die Gramps-Entwickler den Quellcode auf dieser Plattform entwickeln, programmieren, verwenden und testen. Die Diagnose und Behebung von Problemen, die auftreten (sei es aufgrund von Upgrades oder anderen Ursachen), erfolgt also mit Linux-Werkzeugen.

Angenommen, du hast die Standardpaketverwaltung deiner Distribution (CLI oder GUI) verwendet, um Gramps zu installieren, startest du Gramps in der Kommandozeile (CLI) durch die Eingabe von:

`gramps`

Wenn du einen "[aus dem Quellcode erstellen](wiki:Linux:Build_from_source)" gemacht hast, navigiere zu dem Ordner, in dem du die Anwendung installiert hast. (Dieser Ordner enthält die Datei `Gramps.py`.) Gib ein:

`python3 Gramps.py`

### MS Windows

MS Windows ist eine [offiziell von der Gemeinschaft unterstützte](wiki:De:Download) Plattform. Wenn du die [Windows AIO](wiki:All_In_One_Gramps_Software_Bundle_for_Windows) GrampsAIO32 oder GrampsAIO64 installierst, wird ein Icon auf dem Desktop und ein Eintrag im Startmenü erstellt. Das Gramps-Installationsverzeichnis wird jedoch nicht zum Systempfad hinzugefügt und um Gramps über CLI auszuführen, müssen wir den Pfad zu diesem Verzeichnis kennen.

Um den Installationsordner zu finden, siehe  

- [Abschnitt Installationsordner des AIO-Pakets](wiki:All_In_One_Gramps_Software_Bundle_for_Windows#Installation_folder).

Um den Pfad stattdessen über ein Verknüpfungssymbol zu finden  

- Rechts klicke auf die `GrampsAIO64 ``-Terminal` Anwendung oder den entsprechenden Menüeintrag.
- Notiere dir den Speicherort der Datei (das Verzeichnis "Indem sie startet").
- Markiere den kompletten Pfad und kopiere () ihn.

Um Gramps von der Kommandozeile auszuführen, musst du ein Konsolenfenster starten  

- Starte im Startmenü cmd.exe.
- Wechsel in das Installationsverzeichnis, das Sie gefunden haben.
- Gib den Pfad ein oder füge ihn ein und setze ihn in Anführungszeichen, wenn Leerzeichen vorhanden sind.
- Drücke .

Zum Beispiel kann das sein:

`cd "C:\Program Files\GrampsAIO64-``"`  
`gramps`

Du kannst jede der Befehlszeilenoptionen zusammen mit diesem verwenden. Um beispielsweise eine detaillierte Liste aller Stammbaum-Datenbanken in deinem standardmäßigen Stammbaum-Ordner zu erhalten, würdest du `-L` anhängen

`cd "C:\Program Files\GrampsAIO64-``"`  
`gramps -L`

Siehe auch:

- Beispielverwendung <https://github.com/gramps-project/addons-source/pull/121>

### macOS

MacOS ist eine [von der Gemeinschaft unterstützte](wiki:De:Download) Plattform. Wenn du das macOS disk image (.dmg) herunter geladen hast, dann ziehst du die Anwendung einfach in dein Anwendungsverzeichnis (oder irgendwo anders wo du sie speichern willst) und startest Gramps wie üblich durch doppelt klicken auf die Anwendung.Der [Homebrew-Paketmanager](https://github.com/Homebrew) ermöglicht auch die Installation der Anwendung im üblichen Anwendungsordner.

Um Gramps von der Kommandozeile zu starten, musst du Terminal starten, zu finden in dem Ordner Dienstprogramme des Hauptordners Anwendungen (/Anwendungen/Utilities). Wenn du ein Terminalfenster geöffnet hast, gib an der Eingabeaufforderung folgendes ein

`/Pfad/zur/Gramps.app/Contents/macOS/Gramps`

Wenn du Gramps unter Applications neben den meisten anderen Anwendungen, wie oben vorgeschlagen, installiert hast, ist dies

` /Applications/Gramps.app/Contents/MacOS/Gramps`

Du kannst damit zusammen jede Kommandozeilenoption verwenden. Zum Beispiel, um eine detaillierte Liste aller Stammbaumdatenbankern in deinem Standardstammbaumverzeichnis zu erhalten, würdest du folgendes eingeben:

` /Applications/Gramps.app/Contents/macOS/Gramps -L`

Es gibt noch andere Möglichkeiten, Gramps unter macOS zu installieren, diese sind aber weit komplizierter und werden hier nicht behandelt.

## Python Optionen

In den Beispielen für verschiedene Plattformen oben und auch in Kommandos in verschiedenen Dateien, kann es sein, dass du einige Optionen nach dem 'python' Kommando siehst, zum Beispiel '-EO' in

`"python3 -EO ..\share\gramps\gramps.py -L`

Es ist wichtig, zu unterscheiden zwischen den **Python Optionen** in diesem Fall:

`-EO`

und der **Gramps Option**, in diesem Fall

`-L`

Die **Python Optionen** die dir begegnen können sind:

- `-E` Ignoriere alle PYTHON\* Umgebungsvariablen z.B. `PYTHONPATH` und `PYTHONHOME`, die gesetzt sein könnten.
- `-O` Grundoptimierung anschalten. Dies ändert die Dateierweiterung für Kompilierte (Bytecode) Dateien von `.pyc` in `.pyo`. Siehe auch PYTHONOPTIMIZE.

Der `-O` Optimierungsbitschalter hat eine Reihe von Auswirkungen in Gamps:

- Wenn er nicht aktiviert ist, erscheint ein zusätzlicher Eintrag im Menü.
- Wenn er nicht aktiviert ist, werden [info Lognachrichten ausgegeben](wiki:Logging_system#So_how_logging_works_in_Gramps_after_all.3F).
- Wenn er nicht aktiviert ist, [debug statements](wiki:Debugging_Gramps#Add_debug_statements) können aktiviert sein.
- Wenn er nicht aktiviert ist, sind zusätzliche Funktionen in der [Zusatzmodulverwaltung](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Zusatzmodulverwaltung) verfügbar.

Die **Gramps Optionen** werden unten beschrieben.

## Verfügbare Gramps Optionen

Dieser Abschnitt bietet eine Liste aller in Gramps verfügbaren Befehlszeilen Parameter. Wenn du mehr wissen willst als nur eine Liste von Parametern, schaue in die nächsten Abschnitte: [Bedienung](#Bedienung) und [Beispiele](#Beispiele).

### Hilfeoptionen

Die Zusammenfassung unten wird ausgegeben von:

` gramps --help`

oder

` gramps -h`

Verwendung: gramps \[OPTION...\]

` --load-modules=MODUL1,MODUL2,...       Dynamische Module laden`  
  

Hilfeoptionen

` `[<code>-?, --help</code>](#Hilfeoptionen)`                             Zeigt diese Hilfe Information`  
` `[<code>--usage</code>](#Verwendungsnachricht)`                                Zeigt eine kurze Anwendungsinformation`

  
Anwendungsoptionen

` `[<code>-O, --open=STAMMBAUM</code>](#Öffnen_Optionen)`                   Stammbaum öffnen`  
` -U, --username=BENUTZERNAME            Datenbank-Benutzername`  
` -P, --password=KENNWORT                Datenbankkennwort`  
` -C, --create=STAMMBAUM                 Stammbaum beim Öffnen neu erstellen wenn er nicht existiert`  
` `[<code>-i, --import=DATEINAME</code>](#Importoptionen)`                 Datei importieren`  
` `[<code>-e, --export=DATEINAME</code>](#Exportoptionen)`                 Datei exportieren`  
` -r, --remove=STAMMBAUMMUSTER           Übereinstimmende Stammbäume entfernen (verwende reguläre Ausdrücke).`  
` `[<code>-f, --format=FORMAT</code>](#Formatoptionen)`                    Stammbaumformat festlegen`  
` `[<code>-a, --action=AKTION</code>](#Aktionsoptionen)`                    Aktion festlegen`  
` -p, --options=OPTIONEN_ZEICHENKETTE    Optionen festlegen`  
` -d, --debug=LOGGER_NAME                Fehlerprotokollierung aktivieren`  
` `[<code>-l [FAMILY_TREE_PATTERN...</code>](#Listenoptionen)`]           Stammbäume auflisten`  
` `[<code>-L [FAMILY_TREE_PATTERN...</code>](#Listenoptionen)`]           Stammbäume mit Details auflisten`  
` -t  [FAMILY_TREE_PATTERN...]           Stammbäume durch Tab. getrennt auflisten`  
` `[<code>-u, --force-unlock</code>](#Entsperren_erzwingen_Option)`                     Entsperren des Stammbaum erzwingen`  
` `[<code>-s, --show</code>](#Konfiguration_(config)_Option)`                             Konfig. Einstellungen zeigen`  
` `[<code>-c, --config=[config.setting[:Wert</code>](#Konfiguration_(config)_Option)`]]   Konfig. Einstellung(en) setzen und Gramps starten`  
` -y, --yes                              Bei gefährlichen Aktionen nicht nachfragen (nur im nicht Grafikmodus)`  
` -q, --quiet                            Fortschrittsausgabe unterdrücken (nur im nicht Grafikmodus)`  
` `[<code>-v, --version</code>](#Versionsoptionen)`                          Versionen zeigen`  
` -S, --safe                             Start Gramps in 'Abgesicherten Modus'`  
`                                         (Vorübergehend die Standardeinstellungen verwenden)`  
` `[<code>-D, --default=[APXFE</code>](#Standardeinstellungen)`]                  Setzt die Einstellungen auf die Standardeinstellungen zurück;`  
`                A - Erweiterungen werden entfernt`  
`                P - Einstellungen auf Standard zurücksetzen`  
`                X - Bücher werden gelöscht, Berichte und Werkzeugeinstellungen auf Standard gesetzt`  
`                F - Filter werden entfernt`  
`                E - Alles wird auf Standard gesetzt oder gelöscht`

</pre>

### Verwendungsnachricht

Die Verwendungsnachricht lautet wie folgt:

`gramps --usage`

    Beispiel zur Verwendung der Gramps Kommandozeilenschnittstelle                                                   
                                                                                                                     
    1. Zum Import von vier Datenbanken (deren Format aus deren Namen erkennbar ist) und Fehlerprüfung der resultierenden Datenbank kann man folgendes eingeben:                                     
     gramps -i Datei1.ged -i Datei2.gpkg -i ~/db3.gramps -i Datei4.wft -a check                                       
     
    2. Um das Format im obigen Beispiel explizit anzugeben, erweitere die Dateinamen mit der passenden -f Option:
     gramps -i Datei1.ged -f gedcom -i Datei2.gpkg -f gramps-pkg -i ~/db3.gramps -f gramps -i Datei4.wft -f wft -a check
     
    3. Zum Aufzeichnen der Datenbank, die aus allen Importen resultiert, verwende das -e Flag
     (verwende -f wenn der Dateiname es Gramps nicht ermöglicht das Dateiformat zu erkennen):
     gramps -i Datei1.ged -i Datei2.gpkg -e ~/new-package -f gramps-pkg
     
    4. Zum Speichern aller Fehlermeldungen aus dem obigen Beispiel in die Dateien Ausgabedatei und Fehlerdatei, starte:
     gramps -i Datei1.ged -i Datei2.dpkg -e ~/new-package -f gramps-pkg >Ausgabedatei 2>Fehlerdatei
     
    5. Um drei Datenbanken zu importieren und eine interaktive Gramps Sitzung mit dem Ergebnis:
     gramps -i Datei1.ged -i Datei2.gpkg -i ~/db3.gramps
     
    6. Eine Datenbank öffnen und anhand ihrer Daten einen Zeitlinienbericht als PDF-Dokument der meine_zeitlinie.pdf Datei:
     gramps -O 'Stammbaum 1' -a report -p name=timeline,off=pdf,of=meine_zeitlinie.pdf
     
    7. Um eine Zusammenfassung der Datenbank zu erstellen, verwende:
     gramps -O 'Stammbaum 1' -a report -p name=summary
     
    8. Berichtsoptionen listen
     Verwende name=timeline,show=all um alle Optionen für den Zeitlinienbericht zu erhalten.
     Um Details zu einer bestimmten Option zu erhalten, verwende show=Optionsname , z.B.. name=timeline,show=off string.
     Um die verfügbaren Berichtsnamen zu sehen, verwende name=show string.
     
    9. Um einen Stammbaum schnell in eine Gramps XML Datei umzuwandeln, verwende:
     gramps -O 'Stammbaum 1' -e Ausgabe.gramps -f gramps
     
    10. Um einen Webauftritt in einer anderen Sprache zu erstellen (in deutsch), verwende:
     LANGUAGE=de_DE; LANG=de_DE.UTF-8 gramps -O 'Stammbaum 1' -a report -p name=navwebpage,target=/../de
     
    11. Um abschließend eine normale interaktive Sitzung zu starten, gib folgendes ein:
     gramps
     
    Bemerkung: Die Beispiele sind für die bash Shell.
    Die Syntax kann sich für andere Shells oder Windows ändern.

### Listenoptionen

Eine Liste bekannter Stammbäume ausgeben:

Kurz  

`-l, gibt eine Liste bekannter Stammbäume aus`

`gramps -l`

    Liste bekannter Stammbäume in deinem Datenbankpfad

    /home/<~username>/.gramps/grampsdb/5a46c1c3 mit Name "Beispielstammbaum"

{{-}}

Ausführlich  

`-L, gibt eine detaillierte Liste bekannter Stammbäume aus`

`gramps -L`

    Gramps-Stammbäume:
    Stammbaum "Beispielstammbaum":
       Anzahl der Aufbewahrungsorte: 3
       Anzahl der Ereignisse: 3432
       Anzahl der Etiketten: 2
       Anzahl der Familien: 762
       Anzahl der Fundstellen: 2854
       Anzahl der Medien: 7
       Anzahl der Notizen: 19
       Anzahl der Orte: 1296
       Anzahl der Personen: 2157
       Anzahl der Quellen: 4
       Datenbank: SQLite
       Datenbankversion: 3.50.4
       Gesperrt?: False
       Letzter Zugriff: 14.08.2025 02:27:48
       Pfad: C:\Users\<~Benutzername>\AppData\Roaming\gramps\grampsdb\689d2c5e
       Schemaversion: 21.0.0
       Speicherort des Datenbankmoduls: C:\Program Files\GrampsAIO64-6.0.4\lib\library.zip\sqlite3\__init__.pyc
       Stammbaum: Beispielstammbaum

{{-}}

Durch Tabulatoren getrennt  

`-t, Stammbäume als tabulatorgetrennte Datei auflisten`

`gramps -t`

    gramps -t "Example6_0"
    Gramps-Stammbäume
    Stammbaum    Datenbank    Speicherort des Datenbankmoduls    Datenbankversion    Letzter Zugriff    Gesperrt?    Anzahl der Quellenangaben    Anzahl der Ereignisse    Anzahl der Familien    Anzahl der Medien    Anzahl der Notizen    Anzahl der Personen    Anzahl der Orte    Anzahl der Aufbewahrungsorte    Anzahl der Quellen    Anzahl der Tags    Pfad    Schema-Version
    "Example6_0"    "SQLite"    "/Applications/Gramps-6.0.4-Intel/Gramps.app/Contents/Resources/lib/python3.13/sqlite3/__init__.py" "3.49.1"    "06/04/2026 21:47:31"   "False" "2854"  "3432"  "762"   "7" "19"    "2157"  "1296"  "3" "4" "2" "/Users/name/Library/Application Support/gramps/grampsdb/69d13149"  "21.0.0"

### Versionsoptionen

`-v oder --version zeigt die Version von Gramps und Abhängigkeiten, `  
`       Informationen über Umgebungseinstellungen, Python und Systempfade`

`gramps -v`

    Gramps Settings:
    ----------------
     gramps    : AIO64-6.0.4--1
     o.s.      : Windows

    Required:
    ---------
     Python    : 3.12.11
     Gtk++     : 3.24.50
     pygobject : 3.52.3
     Cairo     : 1.18.4
     pycairo   : 1.28.0
     Pango     : 1.56.4
     PangoCairo: 1.0
     orjson    : 3.11.2

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
     RCS        : installiert
     PILLOW     : 11.3.0
     GExiv2     : 0.10
     Exiv2 lib. : nicht gefunden, weil exiv2 nicht installiert ist
     geocodeglib: 1.0

    Environment settings:
    ---------------------
     LANG      : de_DE.UTF-8
     LANGUAGE  : de
     GRAMPSI18N: not set
     GRAMPSHOME: not set
     GRAMPSDIR : not set
     GRAMPS_RESOURCES : C:\Program Files\GrampsAIO64-6.0.4\share
     PYTHONPATH:
        C:\Program Files\GrampsAIO64-6.0.4\gramps
        C:\Program Files\GrampsAIO64-6.0.4\lib\library.zip
        C:\Users\<~Benutzername>\.local/lib/python3.12-mingw_x86_64_msvcrt_gnu/site-packages
        C:\Program Files\GrampsAIO64-6.0.4\lib
        C:\Program Files\GrampsAIO64-6.0.4
        C:\Program Files\GrampsAIO64-6.0.4\lib
        C:\Users\<~Benutzername>\AppData\Roaming\gramps\gramps60\plugins\lib

    System PATH env variable:
    -------------------------
         C:\Program Files\GrampsAIO64-6.0.4
         C:\Program Files\GrampsAIO64-6.0.4\lib
         C:\Program Files\GrampsAIO64-6.0.4\lib
         C:\Program Files\Python311\Scripts
         C:\Program Files\Python311
         C:\WINDOWS\system32
         C:\WINDOWS
         C:\WINDOWS\System32\Wbem
         C:\WINDOWS\System32\WindowsPowerShell\v1.0
         C:\WINDOWS\System32\OpenSSH
         C:\Program Files\GrampsAIO64-6.0.4
         C:\Users\<~Benutzername>\AppData\Local\Microsoft\WindowsApps
         .

    Databases:
    -------------------------
     bsddb     :
         version     : not found
         db version  : not found
         location    : not found
     sqlite3   :
         version     : 3.50.4
         location    : C:\Program Files\GrampsAIO64-6.0.4\lib\library.zip\sqlite3\__init__.pyc

{{-}}

### Formatoptionen

Das Format jeder Datei, die geöffnet, importiert oder exportiert werden soll, kann mit der

    -f format

Option festgelegt werden. Die zulässigen *`format`* Werte sind unten aufgelistet.

#### Volle Stammbaum Unterstützung

Diese Formate enthalten deine gesamten Daten die in einem Stammbaum enthalten sind.

- **gramps** - Gramps XML Format: Dieses Format ist für Öffnen, den Import und den Export verfügbar. Falls nicht angegeben wird es gesetzt, wenn der Dateiname mit .gramps endet.
- **gpkg** - Gramps Paket XML Format: Dieses Format ist für den Import und Export verfügbar. Falls nicht angegeben wird es gesetzt, wenn der Dateiname mit .gpkg endet.
- **grdb** - vor Gramps 3.x Datenbank: Dieses Format ist für den Import zur Unterstützung älterer Dateiformate von Gramps verfügbar. Alles in der grdb Datei wird importiert. Falls nicht angegeben wird es angenommen wenn die Dateiendung .grdb lautet.
- **burn** - GNOME ISO brennen: Export, nur unter GNOME verfügbar wenn das Brennprotokoll existiert.

#### Eingeschränkte Stammbaum Unterstützung

Diese Formate enthalten die meisten aber nicht alle Daten, die mit Gramps erstellt werden können

- **ged** - GEDCOM Format: Dieses Format ist für den Import und den Export verfügbar. Falls nicht angegeben wird es gesetzt, wenn der Dateiname mit .ged endet.
- **gw** - GeneWeb Datei: Dieses Format ist für den Import und Export verfügbar. Falls nicht angegeben wird es gesetzt, wenn der Dateiname mit .gw endet.

#### Teilmenge deiner Daten

Diese Formate enthalten einen bestimmten Teilbereich deiner Daten

- **csv** - Komma getrennte Werte: Dieses Format ist für Import und Export verfügbar. Sei jedoch vorsichtig, der Import muss mit Werten erfolgen wie sie vom Export erstellt werden. Nur ein Teil deiner Daten ist in dieser Ausgabe enthalten.
- **vcf** - VCard 3.0 Format: Import und Export
- **vcs** - VCalendar Format: Export
- **def** - altes Pro-Gen Format: Import
- **wft** - Web Family Tree: Dieses Format ist nur für den Export verfügbar. Falls nichts angegeben wird es gesetzt, wenn der Dateiname mit .wft endet.

### Öffnen Optionen

Du kannst einen Stammbaum öffnen, oder eine Datei durch Import in einen leeren Stammbaum **öffnen**.

Damit Gramps dies automatisch erledigt, übergebe einfach den Stammbaum oder die Datei, die du öffnen möchtest:

`python gramps.py 'Mein Stammbaum'`  
`python gramps.py Mustermann.ged`

Das erste öffnet einen Stammbaum, das zweite importiert eine GEDCOM Datei in einen leeren Stammbaum.

Zusätzlich kannst du Gramps den Namen des zu öffnenden Stammbaums mitgeben:

- verwende diese Option : `-O Stammbaum` oder `--open=Stammbaum`

`-O`, Öffnen eines Stammbaum. Dies kann auch durch die einfache Eingabe des namens geschehen (Name oder Datenbankverzeichnis)

Beispiele:

`python gramps.py 'Stammbaum 1'`  
`python gramps.py /home/cristina/.gramps/grampsdb/47320f3d`  
`python gramps.py -O 'Stammbaum 1'`  
`python gramps.py -O /home/cristina/.gramps/grampsdb/47320f3d`

### Importoptionen

Die für den Import vorgesehenen Dateien können mit dem `-i Dateiname` oder `--import=Dateiname` Parameter angegeben werden. Das Format kann mit dem `-f Format` oder `--format=Format` Parameter bestimmt werden, dem sofort der **Dateiname** folgt. Falls es nicht angegeben wird, wird versucht das Format aus dem **Dateiname** zu ermitteln.

Beispiele:

`  python gramps.py -i 'Stammbaum 1' -i 'Stammbaum 2'`  
`  python gramps.py -i test.grdb -i daten.gramps`

Wenn mehr als eine Eingabedatei angegeben ist, muss vor jeder das Flag `-i` stehen. Die Dateien werden in der angegebenen Reihenfolge importiert, z. B. `-i Datei1 -i Datei2` und `-i Datei2 -i Datei1` können unterschiedliche Gramps-IDs in der resultierenden Datenbank erzeugen.

### Exportoptionen

Die für den Export vorgesehenen Dateien können mit dem Parameter `-e Dateiname` oder `--export=Dateinamean` gegeben werden. Das Format kann mit dem `-f` Parameter bestimmt werden, dem sofort der **Dateinamen** folgt. Falls es nicht angegeben wird, wird versucht das Format aus dem *Dateinamen* zu ermitteln. Für ISO-Formate, ist der *Dateiname* der Name des Verzeichnisses, in das die Gramps-Datenbank geschrieben wird. Für gramps-xml, gpkg, gedcom, wft, geneweb und gramps-pkg ist der *Dateiname* der Name der resultierenden Datei.

-e, exportiert einen Stammbaum in das gewünschte Format. Es ist nicht möglich in einen Stammbaum zu exportieren.

Beispiele:

` python gramps.py -i 'Stammbaum 1' -i test.grdb -f grdb -e verschmolzeneDB.gramps`

Beachte das das obige Beispiel 'Stammbaum 1' nicht verändert, da alles über eine temporäre Datenbank geschieht, wohingegen:

` python gramps.py -O 'Stammbaum 1' -i test.grdb -f grdb -e verschmolzeneDB.gramps`

test.grdb nach 'Stammbaum 1' importiert und dann das Ergebnis in eine Datei exportiert !

Wenn mehr als eine Ausgabedatei angegeben ist, muss vor jeder das Flag `-e` stehen. Die Dateien werden einzeln in der angegebenen Reihenfolge geschrieben.

### Aktionsoptionen

Die Aktion, die mit den importierten Daten durchgeführt werden soll, kann über die `-a Aktion` oder `--action=Aktion` Option angegeben werden. Diese wird ausgeführt, nachdem alle Importe erfolgreich abgeschlossen sind.

Die folgenden Aktionen sind gleich geblieben:

- *report*: Diese Aktion erlaubt das erstellen von Berichten über die Kommandozeile.

<!-- -->

- *tool*: Diese Aktion ermöglicht ein Werkzeug von einer Kommandozeile zu starten.

Da Berichte und Werkzeuge eine Reihe eigener Optionen haben, sollten diese Aktionen die Berichts/Werkzeug Optionenzeichenkette folgen. Die Zeichenkette wird mit der `-p Optionszeichenkette` oder `--options=Optionszeichenkette` Option übergeben.

Die Aktionen aus älteren Gramps Versionen, die in Gramps 3.3 umgezogen sind:

- *summary*: Diese Aktion war dieselbe wie . In Gramps 3.3 wurde es ersetzt durch (oder umbenannt in) **-a report -p name=summary**.

<!-- -->

- *check*: Diese Aktion war dieselbe wie . In Gramps 3.3 wurde es ersetzt durch (oder umbenannt in) **-a tool -p name=check**.

#### Berichtaktionoption

Du kannst die meisten Berichte von der Kommandozeile aus mit Hilfe der report Aktion erstellen.

Ein Beispiel:

`gramps -O "Stammbaum 1" -a report -p "name=family_group,style=default,off=html,of=test.html"`

Du kannst den css Stil der verwendet werden soll mit der css Option angeben:

`gramps -O "Stammbaum 1" -a report -p "name=family_group,style=default,off=html,of=test.html,css=Web_Nebraska.css"`

oder ohne css in der HTMl Ausgabe:

`gramps -O "Stammbaum 1" -a report -p "name=family_group,style=default,off=html,of=test.html,css="`

Die meisten Berichtsoptionen sind berichtspezifisch. Jedoch gibt es einige übliche Optionen.

- `name=Berichtname`: Diese benötigte Option bestimmt welcher Bericht erzeugt wird.

- `of` : Ausgabe Dateinam und optional Zielordner/-verzeichnis z.B.: `of="C:\Users\`<username>`\Desktop\FamilyTree.odt"`
- `off`: Ausgabeformat. Dies sind die Dateierweiterungen die das Ausgabeformat bestimmen, z.B., pdf, html, doc, ...
- `style`: für Textberichte, die zu verwendende Formartvorlage. Vorgabe 'default'.
- `show=all`: Dies erstellt eine Liste der Namen aller verfügbaren Optionen für den angegebenen Bericht.
- `show=option_name`: Dies zeigt die Beschreibung der Funktionalität die durch Option_Name bereit gestellt wird, genauso wie die akzeptierten Arten und Werte für diese Option.

So, um die Verwendung von report zu lernen, führe folgendes als Beispiel aus:

`gramps -O "Stammbaum 1" -a report -p "name=family_group,show=all"`

Wenn mehr als eine Ausgabeaktion angegeben wird, muss jede auf einem `-a` Parameter folgen. Die Aktionen werden nacheinander in der entsprechenden Reihenfolge durchgeführt.

Auf der Kommandozeile müssen solche Listen immer mit einer linken eckigen Klammer beginnen `[` und müssen immer mit einer rechten eckigen Klammer enden `]` aber da solche eckigen Klammern im Normalfall etwas "spezielles" für die "Shell" sind (sie bedeuten etwas für den Kommandozeileninterpreter in den du das Kommando eingibst), musst du sie "maskieren" so das sie von deiner Shell ignoriert werden.

Die Details variieren mit jeder Shell, aber (unter Linux / UNIX) kannst du einer solchen eckigen Klammer normalerweise einen umgekehrten Schrägstrich `\` voranstellen oder Anführungszeichen um die eckige Klammer setzen, normalerweise entweder "einfache" oder "doppelte".

Der Stundenglasbericht erlaubt dir eine "Notiz" über den Bericht zu setzen und solch eine "Notiz" ist ein Beispiel für eine "Listen" Option. Hier ist ein Beispiel:

`gramps -O "Stammbaum 1" -a report -p name=hourglass_graph,note='[Zeile eins,Zeile zwei]' `

was zeigt, das innerhalb solch einer Liste Zeilen durch Komma getrennt werden und Leerzeichen erlaubt sind, solange die Anführungszeichen wegen den eckigen Klammer bereits vorhanden sind.

Wenn du jedoch ein Komma in deinem Bericht haben möchtest, musst du Gramps irgendwie mitteilen, dass das Komma kein Trennzeichen zwischen den Zeilen ist. Du tust dies, indem du die Zeile mit dem Komma in Anführungszeichen setzen (entweder einfach oder doppelt).

Wenn du aber bereits ein Paar Anführungszeichen verwendest (um deine eckigen Klammern einzuschließen) musst du die andere Art verwenden, um die Zeile mit dem Komma einzuschließen. Hier ist ein Beispiel:

`gramps -O "Stammbaum 1" -a report -p name=hourglass_graph,note="['Zeile 1, auch Zeile 1','Zeile 2, auch Zeile 2']"`

Es ist möglich, jedes Zeichen in einer Liste aufzunehmen aber die Details gehen über den Umfang einer Anleitung für die Kommandozeile von Gramps hinaus.

Du musst die genauen Methoden deines Kommandozeileninterpreters kennen, um ein Zeichen welches für deine Shell oder Gramps "speziell" ist (wie das Komma im obigen Beispiel) aufzunehmen aber generell musst du es zweifach "maskieren" einmal für deine Shell und zweiten für Gramps da du nicht willst, das deine Shell denkt es sei ein Kommando, auf das sie achten muss und du willst auch nicht das Gramps dies denkt.

#### Werkzeugaktionoption

Du kannst die meisten Werkzeuge durch Verwendung der 'tool' Aktion von der Kommandozeile ausführen. Anzeigen aller verfügbaren Werkzeuge:

`gramps -O "Stammbaum 1" -a tool -p show=all`

Die verfügbaren Optionen für ein Werkzeug anzeigen etwa für das "verify" Werkzeug:

`gramps -O "Stammbaum 1" -a tool -p name=verify,show=all`

Ein Werkzeug ausführen etwas das "verify" Werkzeug:

`gramps -O "Stammbaum 1" -a tool -p name=verify`

#### Buchaktionoption

Du kannst Bücher aus der Kommandozeile mit der 'book' Aktion erstellen.

Um zu sehen welche sage:

`gramps -O "Stammbaum 1" -a book`

Um alle für ein Buch, zum Beispiel "meinBuch", verfügbaren Optionen zu sehen:

`gramps -O "Stammbaum 1" -a book -p name=meinBuch,show=all`

Um ein Buch, zum Beispiel ein Buch "meinBuch" zu erstellen:

`gramps -O "Stammbaum 1" -a book -p name=meinBuch`

### Entsperren erzwingen Option

- `-u`: du kannst den `-O` Parameter mit `-u` erweitern, um das Entsperren eines Stammbaum zu erzwingen. Dies ermöglicht den Wiedereinstieg von der Kommandozeile nach einem Absturz der den Stammbaum (Datenbank) gesperrt hinterlassen hat.

Ein Beispiel (um die "Stammbaum 1" Datenbank zu entsperren):

  
`gramps -O "Stammbaum 1" -a report -u > /dev/null`

Siehe auch::

- [Stammbäume Verwalten:Einen Stammbaum entsperren](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Stammbäume_Verwalten#Einen_Stammbaum_entsperren)

### Konfiguration (config) Option

Wenn alle Konfigurationsvariable(n) festgelegt sind, beginnt Gramps mit diesen neuen Werten.

Die Option gibt es in drei Formen:

1\) Alle Konfigurationswerte anzeigen  
`-s` oder `--show`

  
Zum Beispiel:

`gramps --show`

    Gramps Konfigurationseinstellungen von /home/mirko/.gramps/gramps51/gramps.ini:
    export.proxy-order=[['privacy', 0], ['living', 0], ['person', 0], ['note', 0], ['reference', 0]]

    database.compress-backup=True
    database.backend='bsddb'
    database.backup-path='/home/<~Nutzername>'
    database.port=''
    database.autobackup=0
    database.path='/home/<~Nutzername>/.gramps/grampsdb'
    database.host=''
    database.backup-on-exit=True

    geography.lock=False
    ....

{{-}}

2\) Einen einzelnen Konfigurationswert einsehen  
`--config=database.path` oder `-c database.path`

  
Zum Beispiel:

`gramps --config=database.path`

    Aktuelle Gramps Konfigurationseinstellungen: database.path:'/home/<~Nutzername>/.gramps/grampsdb'

3\) Einen Wert setzen  
`--config=behavior.database-path:'/media/mydb'` oder `-c behavior.database-path:'/media/mydb'`

  
Zum Beispiel:

3.1) Einen Wert auf seinen Standard setzen  
`--config=behavior.database-path:DEFAULT` oder `-c behavior.database-path:DEFAULT`

  
Zum Beispiel:

3.2) Mehr als einen Wert setzen  
`--config=behavior.use-tips:False --config=behavior.autoload:True` oder `-c behavior.use-tips:False -c behavior.autoload:True`

  
Zum Beispiel:

### Abgesicherter Modus

`gramps -S` oder `gramps --safe`

Dieser CLI-Befehl startet Gramps so, als wäre es noch nie zuvor installiert worden. In diesem Modus können alle vorherigen Stammbäume noch geladen werden, solange sie im Standardordner gespeichert wurden. Alle anderen Einstellungen, Filter, Bücher, Addons usw. werden entweder gelöscht oder auf ihre Standardwerte zurückgesetzt. Andere CLI-Befehle können verwendet werden, oder wenn keine vorhanden sind, startet Gramps die GUI. Es werden nur die tatsächlichen Stammbaumdaten gespeichert.

Beachte, dass dies normalerweise verwendet wird, um festzustellen, ob sich Gramps besser verhält wenn es wie bei einer vollständig "sauberen" Installation ausgeführt wird. Es ist NICHT permanent (wenn du dies möchtest, siehe [Standardeinstellungen](#Standardeinstellungen) unten). Wenn du Gramps nach Verwendung dieses Befehls normal startest, sind alle deine vorherigen Einstellungen usw. noch vorhanden.

Dies funktioniert tatsächlich, indem der Ordner, in dem Gramps seine Benutzerdaten (mit Ausnahme von Stammbäumen) speichert, auf einem temporäres Verzeichnis festgelegt wird, das beim Schließen von Gramps gelöscht wird.

### Standardeinstellungen

`gramps -D E` oder `gramps --default=E`

Dieser CLI-Befehl bewirkt, dass Gramps die gewünschten Einstellungen löscht oder zu den Standardeinstellungen zurückkehrt. Die Stammbaumdatenbanken werden NICHT gelöscht oder entfernt. Die Unterbefehle (ersetze das 'E' in der obigen Beispielbefehlszeile durch eines oder mehrere der Unterbefehlszeichen) sind:

- `A` Erweiterungen werden gelöscht. Alle installierten Erweiterungen werden zusammen mit ihren Einstellungen entfernt.
- `F` Filter werden gelöscht. Alle benutzerdefinierten Filter werden entfernt.
- `P` Die Einstellungen werden auf ihre Standardwerte zurückgesetzt.
- `X` Bücher werden gelöscht, die Einstellungen für Berichte und Tools werden auf ihre Standardwerte zurückgesetzt.
- `Z` Alte '.zip'-Dateien aus Stammbaum-Versions-Upgrades werden gelöscht.
- `E` Alles außer den eigentlichen Stammbaumdaten wird auf die Standardeinstellungen zurückgesetzt. Dies führt alle oben genannten sowie einige weitere Elemente aus. löscht Miniaturansichten, Karten und das Benutzer-CSS (in Webberichten verwendet).

Beispielsweise:

`gramps -D AP`

bewirkt, dass Gramps alle Addons entfernt und die Einstellungen auf ihre Standardwerte zurücksetzt.

## Bedienung

Wenn das erste Argument auf der Kommandozeile nicht mit einem Strich beginnt (z.B. kein Parameter), versucht Gramps die Datei mit dem Namen des ersten Arguments zu öffnen und eine interaktive Sitzung zu starten. Der Rest der Kommandozeilenargumente wird ignoriert.

Wenn der `-O` Parameter gesetzt ist, versucht Gramps den gelieferten Dateinamen zu öffnen und dann mit den Daten wie in weiteren Parametern angegeben zu arbeiten.

Mit oder ohne den `-O` Parameter, können mehrere Importe, Exporte und Aktionen in der Kommandozeile weiter spezifiziert werden durch Verwendung der `-i`, `-e`, und `-a` Parameter.

Die Reihenfolge der `-i` , `-e` , oder `-a` Parameter spielt keine Rolle. Die tatsächliche Ausführungsreihenfolge ist immer: alle Importe (wenn vorhanden) -\> alle Exporte (wenn vorhanden) -\> alle Aktionen (wenn vorhanden).

Wenn kein `-O` oder `-i` Parameter angegeben wird, startet Gramps sein Hauptfenster und startet die gewöhnliche interaktive Sitzung mit der leeren Datenbank, denn es gibt keine Daten zu verarbeiten. (Außer du hast schon eine "Präferenz" gesetzt, das es mit der letzten verwendeten Datenbank starten soll.)

Wenn kein `-e` oder `-a` Parameter angegeben ist, startet Gramps sein Hauptfenster und startet die gewöhnliche interaktive Sitzung mit der, aus öffnen und allen Importen (wenn vorhanden) resultierenden Datenbank. Die Datenbank liegt dann in einem Verzeichnis unter dem *`~/.gramps/import/`* Verzeichnis.

Fehler, die während des Imports, Exports oder einer Aktion auftreten, werden entweder auf stdout (wenn es Fehler sind, die von Gramps behandelt werden) oder auf stderr (wenn sie nicht behandelt werden) geschrieben. Verwende die gewöhnlichen Shell-Umleitungen von stdout und stderr um diese Nachrichten und Fehler in Dateien zu speichern.

## Beispiele

- Um vier Datenbanken zu importieren (deren Format aus ihrem Namen erschlossen werden kann) und die sich ergebende Datenbank auf Fehler zu überprüfen, kann man folgendes eingeben:

  
`gramps -i Datei1.ged -i Datei2.gpkg -i ~/DB3.gramps -i Datei4.wft -a check`

- Um die Formate in dem obigen Beispiel explizit anzugeben, erweitere die Dateinamen mit den entsprechenden -f Optionen:

  
`gramps -i Datei1.ged -f gedcom -i Datei2.gpkg -f gramps-pkg -i ~/DB3.gramps -f gramps-xml -i Datei4.wft -f wft -a check`

- Um die Datenbank die sich aus den Importen ergibt aufzuzeichnen, verwende das -e Flag (verwende -f wenn der Dateiname es Gramps nicht erlaubt das Format zu vermuten):

  
`gramps -i Datei1.ged -i Datei2.gpkg -e ~/new-package -f gramps-pkg`

- Um jede Fehlermeldung aus dem obigen Beispiel in die Dateien ausgabedatei und fehlerdatei zu speichern, starte:

  
`gramps -i Datei1.ged -i file2.dpkg -e ~/new-package -f gramps-pkg >ausgabedatei 2>fehlerdatei`

- Um drei Datenbanken zu importieren und eine interaktive Gramps Sitzung mit dem Ergebnis zu starten:

  
`gramps -i Datei1.ged -i Datei2.gpkg -i ~/db3.gramps`

- Um eine Datenbank zu öffnen und basierend auf diesen Daten einen Zeitlinienbericht im PDF-Format zu erstellen und inder Datei meine_zeitlinie.pdf zu speichern:

  
`gramps -O 'Stammbaum 1' -a report -p name=timeline,off=pdf,of=meine_zeitlinie.pdf`

- Um eine grdb spontan in eine .gramps XML-Datei umzuwandeln:

  
`gramps -O 'Stammbaum 1' -e ausgabe.gramps -f gramps-xml`

- Um eine Webseite in einer anderen Sprache (Deutsch) zu erstellen:

`LANGUAGE=de_DE; LANG=de_DE.UTF-8 gramps -O 'Stammbaum 1' -a report -p name=navwebpage,target=/../de`

- Zum Abschluss um eine normale Interaktive Sitzung zu starten, tippe:

  
`gramps`

## Umgebungsvariablen

### GRAMPSHOME

- *'GRAMPSHOME* - wenn gesetzt, [überschreibt es den Standardpfad](wiki:Gramps_and_Windows#Setting_the_configuration_path) zum Profil, sodass der Benutzer ein externes Netzlaufwerk zum Speichern von Daten und allen Einstellungen verwenden kann. Für technisch fortgeschrittene Benutzer, die mehrere Versionen von Gramps ausführen, ist das Festlegen eines anderen \$GRAMPSHOME eine Möglichkeit, Interferenzen zwischen den verschiedenen Versionen im Gramps-[Anwenderverzeichnis](wiki:De:Gramps_Glossar#Anwenderverzeichnis) zu vermeiden. Es kann auch verwendet werden, um Gramps so zu konfigurieren, dass es [von einem tragbaren Laufwerk ausgeführt](wiki:Run_Gramps_from_a_portable_drive) wird, oder um eine [manuelle Installation](wiki:De:Installation) vorzubereiten. Der Pfad kann auch verwendet werden, um den Pfad zu einem [separaten Testbaum](wiki:Gramps_for_Windows_with_MSYS2#Keep_your_GRAMPSHOME_separate) oder [Entwicklungsbaum](wiki:Getting_started_with_Gramps_development) zu konfigurieren.

Zum Beispiel

    GRAMPSHOME=$HOME/familytrees/paternal

### LANG, LANGUAGE, LC_MESSAGES, LC_TIME

- **LANG**, **LANGUAGE**, **LC_MESSAGES**, und **LC_TIME** - werden von Gramps verwendet, um zu bestimmen, welche Sprachdatei(en) geladen werden sollen. Siehe [locale](https://pubs.opengroup.org/onlinepubs/9799919799/basedefs/V1_chap07.html) für eine allgemeine Diskussion von **LANG**, **LC_MESSAGES**, und **LC_TIME**. Beachte, dass zusätzlich zum Festlegen von Datumsformaten (die in den Einstellungen für Gramps mit Einstellungen überschrieben werden) **LC_TIME** legt auch die Sprache fest, die für Wörter in Datumsangaben wie Monats- und Tagesnamen und im Kontext von *Datumswörtern* wie *um*, *zwischen* und *vor* verwendet wird. **LANGUAGE** ist eine durch Kommas getrennte Liste von Sprachcodes (*keine Gebietsschemas*, obwohl bestimmte Sprachen wie pt_BR oder cn_TW regionale Varianten sind), die eine nach Präferenzen geordnete Liste der gewünschten Übersetzungen festlegt. Es überschreibt **LANG** aber nicht **LC_MESSAGES** oder **LC_TIME**.

### GRAMPSI18N

- [$GRAMPSI18N (für dein Gebietsschema)](wiki:Translating_Gramps#.24GRAMPSI18N_.28for_your_locale.29) - LANG geht davon aus, dass die Gramps-Übersetzungen global installiert sind. Ist dies nicht der Fall, musst du [Gramps das Verzeichnis angeben](wiki:Translating_Gramps#.24GRAMPSI18N_.28for_your_locale.29), in dem sich die Übersetzungen befinden. Dies kann verwendet werden, um [die Sprache für die generierten Berichte vorübergehend zu ändern](wiki:Howto:Change_the_language_of_reports).

Eine Übersetzung heißt `gramps.mo` und kann unter Linux mit dem locate Kommando gefunden werden. Wenn du beispielsweise Schwedisch im Verzeichnis `/home/me/gramps/mo/sv/gramps.mo` hast, kannst du Gramps mit folgenden Anweisungen dorthin leiten:

`GRAMPSI18N=/home/me/gramps/mo LC_ALL=C.UTF-8 LANG="sv" python3 gramps`

### GRAMPSDIR

- Die Umgebungsvariable GRAMPSDIR ist der Pfad zu deinem [Gramps Verzeichnis](wiki:Translating_Gramps#gramps.sh).

### GRAMPS_RESOURCES

- Die Umgebungsvariable GRAMPS_RESOURCES ist der Pfad zu den in Gramps integrierten Ressourcendateien. Du solltest diesen nur ändern, wenn du Gramps aus dem Quellcode oder einer benutzerdefinierten Umgebung verwendest. Ein Indikator, dass du diese Variable setzen musst, ist, wenn du einen der folgenden Fehler erhältst:
  - *Encoding error while parsing resource path/Codierungsfehler beim Parsen des Ressourcenpfads*
  - *Failed to open resource file/Ressourcendatei konnte nicht geöffnet werden*
  - *Resource Path {invalid/path/to/resources} is invalid/Der Ressourcenpfad {ungültig / Pfad / zu / Ressourcen} ist ungültig*
  - *Unable to determine resource path/Ressourcenpfad kann nicht ermittelt werden*

Beispiel [Anwendungsbeispiel](wiki:Linux:Build_from_source#Running_from_a_tarball_release):

`GRAMPS_RESOURCES=/home/username/gramps/branches/maintenance/gramps60/build/t PYTHONPATH=$GRAMPS_RESOURCES:$PYTHONPATH ./gramps`

{{-}}

[K](wiki:Category:De:Dokumentation)
