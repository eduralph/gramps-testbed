---
title: 'De:Gramps 6.0 Wiki Handbuch - Stammbäume Verwalten: CSV Import und Export'
categories:
- De:Dokumentation
managed: false
source: wiki-scrape
wiki_revid: 130614
wiki_fetched_at: '2026-05-30T18:11:37Z'
lang: de
---

{{#vardefine:chapter\|6}} {{#vardefine:figure\|0}} Dieser Abschnitt bezieht sich auf die Verwendung von Gramps im **CSV-Format (Comma Separated Values Tabelle)**.

- [Gramps CSV Import](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Stammbäume_Verwalten#Gramps_CSV_Import)
- [CSV-Export (Tabelle mit durch Kommas getrennten Werten)](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Stammbäume_Verwalten#CSV-Export_.28Tabelle_mit_durch_Kommas_getrennten_Werten.29)

Du kannst die aktuelle Listenansicht auch in eine Tabellenkalkulations- (\*. ODT) oder CSV-Datei [exportieren](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Einstellungen#Ansicht_exportieren).

## Gramps Tabellen Import/Export

Dieses Format ermöglicht dir eine Datentabelle am Stück zu Importieren/Exportieren. Standardmäßig muss die Kalkulationstabelle im Format Comma Separated Value (CSV) vorliegen. (Alternative Trennzeichen können jedoch für den [CSV Dialekt](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Einstellungen#CSV_Dialekt) in den Optionen in Listenansichten angegeben werden). Die meisten Tabellenkalkulationsprogramme können dieses Format lesen und schreiben. Es kann auch einfach manuell geschrieben werden. Dies ist das einzige Gramps Importformat welches eine Zusammenführung mit bestehenden Daten ermöglicht.

Es gibt drei Hauptanwendungen für dieses Format:

1.  Du kannst deine Gramps Kerndaten in ein Tabellenformat exportieren, sie mit einer Tabellenkalkulation oder Textverarbeitung bearbeiten und die Änderungen und Zusätze zurück nach Gramps importieren. Dies ist praktisch um es an andere zum Ausfüllen zu senden oder für Unterwegs, wenn du nicht deine komplette Gramps Anwendung zur Verfügung hast.
2.  Du kannst neue Daten in deinen Gramps Stammbaum importieren. Zum Beispiel, wenn du eine Reihe von neuen Personen zum hinzuzufügen deinem Stammbaum hast, aber nicht mühsam schauen und suchen willst, wo sie hingehören, kann es sein, das du es einfacher findest sie alle in eine Tabelle zu schreiben, und sie dann schnell auf einmal einzulesen. Dies ist praktisch wenn du eine große Menge von Daten aus einer anderen Anwendung oder dem Netz kopiert hast. Ein Beispiel dafür ist [wiederherstellen deinem Gramps Stammbaum](wiki:Narrative_Website_Import) durch laden der Erzählenden Website in eine Tabelle.
3.  Du kannst auch eine Reihe von Korrekturen und Ergänzungen importieren. Nehmen wir an, du hast einen Bericht ausgedruckt und gehst ihn durch und markierst Korrekturen. Wenn du aus jeder Korrektur einen Abschnitt einer Tabelle erstellst, kannst du "die Änderungen Skripten" und sie dann alle auf einmal durchführen.

## Export

### Exportieren eines Stammbaums

![[_media/ExportAssistant-ExportOptions-CSV-defaults-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Exportassistent – Exportoptionen – Assistentendialogfeld (mit Standardeinstellungen für „Komma-getrennte Werte-Tabelle (CSV)“) mit unterem Bereich für dateiformatspezifische Optionen]]

Um deinen Stammbaum zu exportieren:

1.  Starte Gramps
2.  Lade den zu exportierenden Stammbaum
3.  Wähle aus dem Menü
4.  Wähle im Fenster.
5.  Wähle **Durch Komma getrennte Werte Tabelle (CSV)** im Fenster
6.  Im Fenster:
    1.  Wähle im oberen Bereich aus, welche Filter auf deinen Stammbaum angewendet werden sollen
    2.  Wähle in den Kontrollkästchen aus, welche Elemente in den Export aufgenommen werden sollen (Personen, Ehen, Kinder, Orte) und ob die Überschriften in die aktuell verwendete Sprache übersetzt werden sollen.
7.  Wähle im Fenster den Zieldateinamen und den Pfad
8.  Überprüfe im Fenster die Einstellung und klicke auf die Schaltfläche , um den eigentlichen Export zu starten.

{{-}}

Eine Teilmenge der Felder, die deine Genealogiedaten enthalten, wird in einer .csv-Datei in dem unten beschriebenen Format gespeichert. Die Personen und Familien sind so beschriftet, dass die Daten bearbeitet werden können und die veralteten Informationen überschrieben werden können, wenn sie wieder importiert werden. Die Anmerkungen ermöglichen es, die Baumdatenbank über den Import zu aktualisieren.

Es gibt einige leere Spalten besonders Notiz und Quellen Spalten. Sie werden in der Tabelle aufgeführt, so das du Notizen für den Import machen kannst, aber Notizen werden nie mit diesem Werkzeug exportiert.

Deine Daten werden in vier Bereiche aufgeteilt Personen, Heiraten, Kinder und Orte. Die exportierten Felder und Spaltennamen sind:

Orte  
Ort, Titel, Name, Art, Breitengrad, Längengrad, Kennung, Teil_von, Datum

<!-- -->

Personen  
Person, Nachname, Vorname, Rufname, Suffix, Präfix, Titel, Geschlecht, Geburtsdatum, Geburtsort, Geburt Quellenangabe, Taufdatum, Taufort, Taufe Quellenangabe, Sterbedatum, Sterbeort, Sterbequelle, Beerdigungsdatum, Beerdigungsort, Beerdigungsquelle, Notiz

<!-- -->

Heiraten  
Hochzeit, Ehemann, Ehefrau, Datum, Ort, Quelle, Notiz

<!-- -->

Familien  
Familie, Kind

Die erste Spalte in jedem Bereich ist die Gramps-ID. Damit werden deine Bearbeitungen mit den entsprechenden Daten verknüpft, also ändere diese IDs nicht. Lade diese Datei in deine bevorzugte Tabellenkalkulation und verwende dabei Komma-getrennte, durch doppelte Anführungszeichen getrennte Texte und das Textformat (vorerst in beliebiger Kodierung). Dann kannst du Daten hinzufügen oder korrigieren und sie unter Beibehaltung des gleichen Formats wieder speichern. Du kannst die Daten dann wieder über deine alten Daten importieren und sie werden korrigiert.

. {{-}}

### Exportieren einer einzelnen Kategorie

Du kannst alle Daten einer einzelnen Kategorie – z. B. Orte – exportieren, indem du die Kategorieansicht auswählst und dann verwendest.

![[_media/CategoryView-CSV-Export-Options-60-de.png|rechts\|thumb\|450px\|Abb. {{#var:chapter}}.{{#vardefineecho:figure\|{{#expr:{{#var:figure}}+1}}}} Kategorieansicht CSV-Exportoptionen konfigurieren]] Vor dem Exportieren der Daten kannst du das CSV-Format auswählen, das für deine Umgebung oder deinen Zweck am besten geeignet ist.

Klicke auf das Symbol ![[_media/Gramps-config.png]] in der , um das Dialogfeld „Ansicht CSV-Dialekt konfigurieren” zu öffnen.

Mit der Option „Benutzerdefiniert” kannst du ein bestimmtes Trennzeichen für Spalten auswählen, z. B. Tabulator oder „\|”.

Übersetzt mit DeepL.com (kostenlose Version) {{-}}

## Import

Um deine CSV Daten zu importieren:

1.  verwende die Datei von Oben oder erstelle eine Tabelle (wie [unten](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Stammbäume_Verwalten:_CSV_Import_und_Export#Beispiel_CSV_mit_mehreren_Bereichen) beschrieben) mit genealogischen Daten
2.  starte Gramps
3.  Erstelle einen neuen Stammbaum
4.  Wähle aus dem Menü
5.  Wähle die **CSV-Datei (Comma Separated Values Tabelle)** aus und klicke dann auf die Schaltfläche

Der zusammenführen Teil diese Funktion fügt deinem Stammbaum nur Informationen hinzu oder aktualisiert sie und nimmt an, dass die Tabelleninformationen immer die korrekten sind.

Wenn du diese Tabelle mit LibreOffice Calc öffnest, stelle sicher, das jede Spalte den Typ **Text** besitzt und nicht **Standard**. Standard formatiert deine Daten und Nummern um. Auch wenn du Excel verwendest, wirst du sicherlich nach dem Öffnen alle Zellen auswählen und das Format auf **Text** ändern.

Die Tabelle besteht aus Daten, die in Spalten aufgeteilt sind. Jede Spalte sollte als Kopf den Namen der Art der Daten, die sie enthält haben. Du musst spezielle Namen für die Spalten verwenden. Zur Zeit sind dies:

### Ort

    Ort - eine Referenz auf diesen Ort
    Titel - Titel des Ortes
    Name - Name des Ortes
    Art - Art des Platzes (z.B. Stadt, Kreis, Staat, etc.)
    Breitengrad - Breitengrad des Ortes (im Dezimalformat)
    Längengrad - Längengrad des Ortes (im Dezimalformat)
    Kennung - PLZ, GOV, etc.
    Teil_von - die Referenz auf einen anderen Ort der diesen enthält
    Datum - Datumsangabe für das Teil_von galt

### Personen

    Person -  eine Referenz, die für Familien (Heiraten und Kinder) verwendet wird 
    grampsid - gibt eine bestimmte Gramps-ID
    Vorname - der Vorname einer Person
    Nachname - der Nachname einer Person
    Rufname - der Rufname einer Person
    Präfix - Nachnamenpräfix (von, de, etc)
    Suffix - ein Suffix für den Namen der Person (Jr., Sr.)
    Titel - der Titel einer Person (Dr., Dipl. Ing.)
    Geschlecht - männlich, weiblich oder unbekannt
    Quelle - Quellentitel für Person
    Notiz - eine Notiz für den Personendatensatz

    Geburtsdatum - Geburtsdatum
    Geburtsort - Geburtsort (nur verwenden, wenn die Spalte Ort-ID leer ist)
    Geburtsort-ID - ID des Geburtsorts (nur verwenden, wenn die Spalte „Ortsname“ leer ist)
    Geburt Quelle - Quellentitel für die Geburt

    Taufdatum - Taufdatum
    Taufort - Taufort (nur verwenden, wenn die Spalte Ort-ID leer ist)
    Taufort-ID - ID des Tauforts (nur verwenden, wenn die Spalte „Ortsname“ leer ist)
    Tauf Quelle - Quellentitel für die Taufe

    Sterbedatum - Sterbedatum
    Sterbeort - Sterbeort (nur verwenden, wenn die Spalte Ort-ID leer ist)
    Sterbeort-ID - ID des Sterbeorts (nur verwenden, wenn die Spalte „Ortsname“ leer ist)
    Sterbequelle - Quellentitel für den Tod
    Todesursache - Todesursache

    Beerdigungsdatum - Beerdigungsdatum
    Beerdigungsort - Beerdigungsort (nur verwenden, wenn die Spalte Ort-ID leer ist)
    Beerdigungsort-ID - ID des Beerdigungsorts (nur verwenden, wenn die Spalte „Ortsname“ leer ist)
    Beerdigungsquelle - Quellentitel für die Beerdigung
    Beruf Datum - Datum für Beruf
    Beruf Ort - Ort für Beruf (nur verwenden, wenn die Spalte Ort-ID leer ist)
    Beruf Ort ID - ID Ort für Beruf (nur verwenden, wenn die Spalte „Ortsname“ leer ist)
    Beruf Quelle - Quellentitel für den Beruf
    Berufsbeschreibung - Beschreibung für Beruf

    Wohnort Datum - Datum des Wohnsitzes
    Wohnort Ort - Wohnort (nur verwenden, wenn die Spalte Ort-ID leer ist)
    Wohnort Ort ID - ID des Wohnorts (nur verwenden, wenn die Spalte „Ortsname“ leer ist)
    Wohnort Quelle - Quellentitel für den Wohnort

    Attribut Art - Art des Attributs
    Attribut Wert - Wert des Attributs
    Attribut Quelle - Quellentitel des Attributs

### Hochzeiten

    Hochzeit - wenn du dies von einer Familie referenzieren willst, benötigst du hier einen passenden Namen
    Ehemann/Vater/Elter1 - die Referenz auf die Person oben, welche der Mann ist 
             (für weiblichen Partner 1, musst du das Geschlecht im Personenabschnitt
              setzen oder später in Gramps bearbeiten)
    Ehefrau/Mutter/Elter2 - die Referenz auf die Person oben, welche die Frau ist 
              (für männlichen Partner 2, musst du das Geschlecht im Personenabschnitt
              setzen oder später in Gramps bearbeiten)
    Datum - Datum der Hochzeit
    Ort - Ort der Heirat (nur verwenden, wenn die Spalte Ort-ID leer ist)
    Orts-ID - Die Orts-ID für die Hochzeit (nur verwenden, wenn die Spalte „Ortsname“ leer ist)
    Quelle - Quellenmaterial zu der Heirat
    Notiz - eine Notiz zu der Heirat

### Familie

    Familie- eine Referenz um dies mit einen Hochzeit oben zu verbinden (erforderlich)
    Kind - die Referenz der Person oben, die ein Kind ist
    Quelle - Quellenmaterial über die Familie
    Notiz - eine Notiz zu der Familie
    Geschlecht - männlich oder weiblich (du solltest die Übersetzung für deine Sprache verwenden) 
             [Du kannst das Geschlecht hier oder oben bei Person eintragen]

## Details

Großkleinschreibung spielt keine Rolle. Beachte, dass in den Namen keine Unterstriche enthalten sind. Du kannst jede Kombination in beliebiger Reihenfolge verwenden. (Aktuell musst du einen Vor und Nachnamen angeben, wenn du eine Person definierst und wenn du Kinder definierst benötigst du eine Heirat und eine Kinder Spalte aber das war es.) Die Spaltennamen und Daten sind in deiner aktiven Sprache anzugeben.

Jedes davon kann sich in seinem eigenen Bereich in der Tabelle befinden. Es gibt keine Begrenzung für die Anzahl von Bereichen in einer Tabelle und jeder Bereich kann eine beliebige Anzahl von Zeilen besitzen. Lasse eine "Leerzeile" zwischen den Bereichen. Beachte nur, dass Bereiche nicht nebeneinander liegen; sie müssen sich untereinander befinden.

Du kannst mehrere Bereichen von jeder Art in einer Tabelle haben. Die einzige Beschränkung ist, wenn du auf eine Person verweist, musst du dies in einer Zeile unterhalb der Definition der Person tun. Genauso wenn du dich auf eine Heirat beziehst, musst du die in einer Zeile unterhalb der Definition der Heirat tun.

Wenn du „grampsid” als Methode zum Zuweisen spezifischer IDs verwendest, sei beim Importieren in eine aktuelle Datenbank **sehr** vorsichtig. Alle Daten, die du eingibst, werden die diesem Grampsid zugewiesenen Daten *überschreiben*. Wenn du IDs in den Spalten „Ort”, „Person”, „Ehe” oder „Familie” verwendest, die von eckigen Klammern umgeben sind (z. B. „\[I0001\]”), werden die von dir verwendeten Werte ebenfalls als Grampsids interpretiert. Wenn du **neue** Elemente hinzufügst, solltest du die Verwendung des Klammerformats oder der Grampsid-Spalten vermeiden, um ein versehentliches Überschreiben deiner Daten zu verhindern. Wenn du die Klammer- (oder Grampsid-)Methode mit einfachen Verweisen (ohne eckige Klammern) kombinierst, füge die einfach referenzierten Daten nach den mit Klammern referenzierten Daten ein.

Wenn du die Daten in eine Textdatei eingibst, und ein Komma innerhalb einem der Werte haben möchtest, wie zum Beispiel "Clinton, Co., MO", dann musst du den kompletten Wert in doppelte Anführungszeichen setzen und das erste Anführungszeichen direkt hinter das vorangehende Komma. Zum Beispiel:

    Hochzeit, Ehemann, Ehefrau, Ort
    m1, p1, p2,"Clinton, Co., MO"
    m2, p3, p4,"Havertown, PA"

Eine Tabellenverwaltung erledigt dies automatisch für dich.

### Beispiel CSV

Hier ist eine Beispiel Tabelle in LibreOffice Calc, es sollte aber jede Tabellenverwaltung funktionieren.

![[_media/Gramps-csv-example1.csv-LibreOffice-Calc--example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Beispiel gramps-csv-example1.csv-Datei, dargestellt als „LibreOffice Calc“-Tabelle]] {{-}}

<hr>

Dateiname: `gramps-csv-example1.csv`

Dateiinhalt:

    ,,,,,,,,,
    ,"Vorname","Nachname","Rufname","Geschlecht","Präfix","Suffix","Titel","Notiz","Grampsid"
    ,"Douglas","Test","Doug","mänlich","Von","Sr.","Dr.","Dies ist nicht verwandt","I0007"
    ,"Laura","Test",,"weiblich",,,,,

<hr>

{{-}} Beachte die CSV Daten müssen weder in der ersten Spalte noch Zeile beginnen.

Nach dem [Import](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Stammbäume_Verwalten:_CSV_Import_und_Export#Import) in Gramps werden die resultierenden Daten wie folgt angezeigt:

![[_media/FamilyTree-example-imported-gramps-csv-example1.csv-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Beispiel für das Ergebnis einer importierten CSV-Datei (Gramps 6.0.3; Microsoft Windows 10) (Daten aus der Datei gramps-csv-example1.csv)]] {{-}}

### Beispiel CSV mit mehreren Bereichen

Hier ist ein Beispiel für ein CSV Text Tabellenblatt mit mehreren Bereichen:

Wenn du das Folgende erstellst, ausschneidest und in eine Datei einfügst, kannst Du es direkt importieren.

<hr>

Dateiname: `gramps-csv-example2.csv`

Dateiinhalt:


    Ort, Titel, Name, Art
    [P0001], Michigan, Michigan, State
    L1, Canada, Canada, Land
    L2, USA, USA, Land

    Vorname, Nachname, Geburtsdatum, Geburtsort-ID
    John,      Tester,  11/11/1965, L1
    Sally,     Tester,  01/26/1973, L2

    Person, Vorname, Nachname, Geburtsdatum,    Geburtsort-ID
    p1,     Tom,       Smith,   22 Jan 1970, [P0001]
    p2,     Mary,      Jones
    p3,     Jonnie,    Smith
    p5,     James,     Loucher
    p6,     Penny,     Armbruster
    [P0002],     Tim,       Sparklet

    Hochzeit, Ehemann, Ehefrau
    m1,       p1,      p2
    m2,       p5,      p6

    Familie, Kind
    m1,      p3
    m1,      p6
    m2,      [P0002]

<hr>

Die CSV-Datei zeigt, dass ein Datum jedes gültige Gramps-Datum sein kann, einschließlich Datumsformaten wie „26 JAN 1973“ oder „26.1.1973“.

Wenn du als Referenzen Gramps-IDs in eckigen Klammern verwendest, kannst du auf Personen, die sich bereits in dem Stammbaum befinden verweisen, etwa so:

    Person,    Vorname, Nachname
    joe's boy, Harry,     Smith

    Familie, Kind
    [F1524], joe's boy

    Ehemann, Ehefrau
    [I0123], [I0562]

    Vorname, Nachname
    Timothy, Jones

    Ort, Teil_von
    [P0001], [P0002]

Dieses Beispiel würde Harry Smith erstellen und zu einer bereits vorher in Gramps bestehenden Familie F1524 hinzufügen.

Außerdem würde dieses Beispiel zwei vorher vorhandene Personen verheiraten, I0123, und I0562.

Zum Schluss erstellt es auch eine Person mit dem Namen Timothy Jones, die mit niemanden verknüpft ist.

Und schließlich erstellt es auch den Ort P0001 als Teil von Ort P0002.

### Beispiel CSV aus der Tabelle

![[_media/Gramps-csv-example3.ods-LibreOffice-Calc-example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Manuell in eine Tabellenkalkulation eingegebene Daten: <code>gramps-csv-example3.ods</code>]]

In diesem Beispiel musste ich eine ganze Generation eingeben, 16 Namen mit Hochzeitsdaten. Die Kinder hatte ich bereits in der Datenbank. Ich erstellte sie in einem Rechenblatt in Open/Libre Office:

Beachte, das du Nummern und Text als Referenznamen zwischen den Bereichen verwenden kannst. Im Personen Bereich habe ich die Nummern 1 bis 16 verwendet. Dies macht es einfacher auf sie im zweiten Abschnitt, den Hochzeiten, zu verweisen. Die Hochzeiten sind mit den Buchstaben A bis H markiert.

Beachte auch, das die Kinder im dritten Abschnitt existierende Personen sind, was durch die eckigen Klammern um die Gramps-IDs anzeigen.

Als CSV-Datei mit LibreOffice Calc speichern

<hr>

Dateiname: `gramps-csv-example3.csv`

Dateiinhalt

    ,,,
    ,,,
    "Person","Vorname","Nachname",
    1,"Peter","Blank",
    2,"Anna Maria","Kiefer",
    3,"Georg","Schmidt",
    4,"Barbara","Goering",
    5,"Johann","Kiefer",
    6,"Fides","Federer",
    7,"Sebastian","Schelli",
    8,"Magdelena","Schlegel",
    ,,,
    ,,,
    "Hochzeit","Ehemann","Ehefrau","Datum"
    "A",1,2,"28 jan 1712"
    "B",3,4,"4 may 1732"
    "C",5,6,02/07/1930
    "D",7,8,17/08/1927
    ,,,
    "Familie","Kind",,
    "A","[I0104]",,
    "B","[I0105]",,
    "C","[I0972]",,
    "D","[I0973]",,

<hr>

{{-}} Und der Import aus der CSV-Datei in den bestehenden Gramps-Stammbaum „Example.gramps” erzeugt die Spalte ganz rechts, die auf dem Screenshot „Nachher: Stammbaumdiagramm” zu sehen ist. ![[_media/ChartsCategory-Pedigree-view1-horizontal-right-standard-5gen-default-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Vorher: Stammbaum-Ansichtsbaum]]

![[_media/FamilyTree-example-imported-gramps-csv-example3.csv-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Nacher: Das Speichern als CSV-Datei und das Importieren in Gramps erzeugt die Spalte ganz rechts im Stammbaum-Ansichtsbaum.]] {{-}}

### Siehe auch

- [CSV Dialekt](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Einstellungen#CSV_Dialekt) Einstellungen für Trennzeichen
- Diskussion im Gramps-Forum:
  - [CSV-Vorlage für Textimport](https://gramps.discourse.group/t/csv-template-for-text-import/5277/5)

<!-- -->

- [Import (Text) Gramplet](wiki:Addon:ImportGramplet) Drittanbieter-Zusatzmodul von Doug Blank - eine interaktive Version des [CSV-Imports](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Stammbäume_Verwalten:_CSV_Import_und_Export)

<!-- -->

- Python CSV library docs - [Dialekte und Formatierungsparameter](https://docs.python.org/3/library/csv.html#dialects-and-formatting-parameters)

Beispiele für die Anpassung des CSV-Importcodes zur Unterstützung zusätzlicher Datensätze:

- Funktionsanfrage : \[CSV\] Importieren von komplexen Excel-Tabellen in Gramps (z.B. Zeugeninformationen)
- [PR \#139](https://github.com/gramps-project/gramps/pull/139) : CSV-Import Unterstützung für AFN und REFN Attribute hinzufügen
- [PR \#810](https://github.com/gramps-project/gramps/pull/810) : Hinzufügen von Berufs- und Wohnort-Ereignissen + Attributen im CSV-Personen-Importer

[C](wiki:Category:De:Dokumentation)
