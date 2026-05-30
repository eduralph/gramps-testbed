---
title: De:Gramps 6.0 Wiki Handbuch - Berichte - Teil 5
categories:
- De:Dokumentation
- Plugins
- Stub
managed: false
source: wiki-scrape
wiki_revid: 131041
wiki_fetched_at: '2026-05-30T17:36:59Z'
lang: de
---

{{#vardefine:chapter\|13.5}} {{#vardefine:figure\|0}} Zurück zur [Übersicht der Berichte](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte).

<hr>

{{-}} ![[_media/MenuOverview-Reports-Graphs-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}}  Menüübersicht]] Dieser Abschnitt beschreibt die verschieden (auch bekannt als grafische Berichte), die in Gramps verfügbar sind.

## Grafiken

Alle drei Diagrammberichte: [Familienlinien](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte_-_Teil_5#Familienliniengrafik), [Stundenglas](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte_-_Teil_5#Stundenglasdiagramm) und [Beziehungsdiagramme](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte_-_Teil_5#Beziehungengrafik) haben gemeinsame Optionen: , und .

Sie haben auch gemeinsame Optionen mit den [gemeinsamen Optionen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte_-_Teil_4#Gemeinsame_Optionen) der anderen Berichte: und .

### Voraussetzungen für Diagrammberichte

Erfordert die Installation des [GraphViz](wiki:Output_formats#Graphviz)-Programms und des Ghostscript-Programms, das von Graphviz-Berichten verwendet wird, um PDF-Dateien zu erstellen.

- Unter Linux verwende deinen Paketmanager.
- Unter Microsoft Windows verwende das Gramps AIO, da diese bereits Teil des Installationsprogramms sind.
- Unter Apple macOS verwende die Gramps .dmg, da diese bereits Teil des Installationsprogramms sind.

### Gemeinsame Optionen

Es sind hier diverse [GraphViz](wiki:Output_formats#Graphviz)-spezifische Optionen vorhanden in Zusammenhang mit Seiteneinstellungen, Farbe und Details zu den Graphen.

Dieses Zusatzmodul verwendet die GraphViz visualisierungs und Ghostscript Programme. GraphViz nimmt die erstellten [<code>.gv</code>](wiki:Output_formats#Graphviz) Dateien und erstellt die endgültigen Dateien wie zum Beispiel `.gif`, `.png`, `.ps`, (Ghostscript erstellt `.pdf`), etc.

#### GraphViz Layout

![[_media/FamilyLinesGraph-Graphs-GraphvizLayout-tab-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Familienliniengrafik - Grafiken - Graphviz Layout - Registerkarte Standardoptionen]]

-   
  Wähle die Schriftfamilie. Wenn keine internationalen Zeichen angezeigt werden, verwende **FreeSans** Schrift. FreeSans ist verfügbar auf [die NonGNU Organisation](http://www.nongnu.org/freefont/).

  - **Standard**
  - PostScript/ Groteskschrift
  - True Type/ FreeSans

- (`14` Standardeinstellung) Die Schriftgröße in [Punkten](https://de.wikipedia.org/wiki/Punkt_(Einheit))

-   
  Ob die Grafik von oben nach unten oder von links nach rechts geht

  - **Vertikal (Oben nach unten)** (Standardeinstellung)
  - Vertikal (Unten nach oben)
  - Horizontal (links nach rechts)
  - Horizontal (rechts nach links)

- (`1` Standardeinstellung) GraphViz kann sehr große Grafiken durch verteilen der Grafik über eine rechteckige Anordnung von Seiten erstellen. Dies bestimmt die horizontale Seitenanzahl in der Anordnung. **Nur gültig für dot und PDF über Ghostscript**.

- (`1` Standardeinstellung) GraphViz kann sehr große Grafiken durch verteilen der Grafik über eine rechteckige Anordnung von Seiten erstellen. Dies bestimmt die vertikale Seitenanzahl in der Anordnung. **Nur gültig für dot und PDF über Ghostscript**.

- (*Unten, links* Standardeinstellung) Die Reihenfolge in der die Grafikseiten ausgegeben werden. Diese Option erscheint nur, wenn die horizontale oder vertikale Seitenanzahl größer ist als 1.

- \- Wie die Linien zwischen Objekten gezeichnet werden. Wähle aus:

  - *Gerade*
  - **Gebogen** (Standardeinstellung)
  - *Rechtwinklig*

{{-}}

#### Optionen für GraphViz

![[_media/FamilyLinesGraph-Graphs-GraphvizOptions-tab-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Familienliniengrafik - Grafiken - Optionen für Graphviz - Registerkarte Standardoptionen]]

Dieser erste Reiter erlaubt es verschiedene GraphViz Einstellungen zu setzen:

- Bestimmt hauptsächlich, wie das Diagramm auf der Seite angeordnet ist.

Insbesondere Knotenabstand und Skalierung des Graphen( siehe *Hinweis 1:*).

- - *Auf minimale Größe komprimieren*
  - **Gegebenen Bereich füllen** (Standardeinstellung)
  - *Gleichmäßig ausdehnen*

<hr>

**Hinweis 1:**

Wenn die Grafik kleiner als der Druckbereich ist:

- *Auf minimale Größe komprimieren* ändert den Knotenabstand nicht.
- *Gegebenen Bereich füllen* erhöht den Knotenabstand, um in Breite und Höhe den Druckbereich zu füllen.
- *Gleichmäßig ausdehnen* erhöht den Knotenabstand gleichmäßig, um das Seitenverhältnis beizubehalten.

Wenn die Grafik größer als der Druckbereich ist:

- *Auf minimale Größe komprimieren* schrumpft den Graphen, um eine dichte Packung auf Kosten der Symmetrie zu erreichen.
- *Gegebenen Bereich füllen* schrumpft das Diagramm, damit es in den Druckbereich passt, nachdem zuerst der Knotenabstand erhöht wurde.
- *Gleichmäßig ausdehnen* schrumpft das Diagramm gleichmäßig, damit es in den Druckbereich passt.

<hr>

- (`72` Standardeinstellung) dots-per-inch (Punkte pro Zoll). Verwende beim Erstellen von PostScript oder PDF 72 DPI. Normalerweise zwischen 75 und 120 beim Generieren von .png- oder .gif-Dateien, aber 300 oder 600 beim Generieren von zu druckenden Dateien. Wenn du Bilder wie .gif- oder .png-Dateien für das Web erstellst, versuche es mit Zahlen wie 100 oder 300 DPI.

- (`0.20` Standardeinstellung) Der minimale Abstand, in Zoll zwischen den einzelnen Knoten. Für vertikale Grafiken entspricht dies dem Spaltenabstand. Für horizontale Grafiken entspricht dies dem Zeilenabstand.

- (`0.20` Standardeinstellung) Der minimale Abstand, in Zoll zwischen den einzelnen Ebenen. Für vertikale Grafiken entspricht dies dem Zeilenabstand. Für horizontale Grafiken entspricht dies dem Spaltenabstand.

#### Notiz

![[_media/FamilyLinesGraph-Graphs-Note-tab-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Familienliniengrafik - Grafiken - Notiz - Registerkarte Standardoptionen]]

- (Standardmäßig leer) Dieser Text wird der Grafik hinzugefügt

- \- Ob die Notiz oben oder unten auf der Seite erscheint

  - **Oben** (Vorgabe)
  - *Unten*

- (`32` Standardeinstellung) Die Größe des Notiztext in [Punkten](https://de.wikipedia.org/wiki/Punkt_(Einheit)).

{{-}}

### <u>Familienliniengrafik</u>

![[_media/Graphs-FamilyLinesGraph-example-overview-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Familienliniengrafik - Grafiken - Beispielausgabe Übersicht]]

Die beginnt mit einer Liste von „Personen von Interesse“. Diese anfängliche Liste von Personen wird dann verwendet, um sowohl Vorfahren als auch Nachkommen zu finden und mit Hilfe des [GraphViz-Generator](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte_-_Teil_5#Voraussetzungen_für_Diagrammberichte) die zu erstellen.

Eine typische Anwendung dieser Erweiterung ist die Erstellung vereinfachter Schaubilder, um sie als große Poster auszudrucken.

Du kannst die Familienliniengrafik über wählen.

Um eine zu erstellen, wähle im Menü klicke auf die Schaltfläche (Hinzufügen) und wähle dann auf der Registerkarte mindestens eine Person aus dem Auswahldialog und der Bericht schlägt, wenn möglich, eine zweite verbundene Person vor über den Warndialog wähle oder , je nachdem, was du entscheidest, und wähle dann , um den Bericht zu erstellen. {{-}} Siehe auch:

- [Gemeinsame Optionen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte_-_Teil_5#Gemeinsame_Optionen) - (GraphViz-spezifisch in Bezug auf Seitennummerierung, Farbe und Details des Diagramms.)

{{-}}

#### Berichtsoptionen

![[_media/FamilyLinesGraph-Graphs-ReportOptions-tab-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Familienliniengrafik - Grafiken - Berichtsoptionen - Registerkarte Standardoptionen]]

-  Eltern und ihre Vorfahren werden bei der Bestimmung von "Familienlinien" berücksichtigt(Kontrollkästchen standardmäßig aktiviert)

-  Children will be considered when determining "family lines". (Kontrollkästchen standardmäßig aktiviert)

-  Personen und Familien, die nicht direkt mit Personen von Interesse verwandt sind, werden bei der Bestimmung von "Familienlinien" entfernt.(Kontrollkästchen standardmäßig aktiviert)

- Wähle die Richtung, in die die Pfeile zeigen:

  - **Nachkommen \<- Vorfahren**(Standardeinstellung) - Pfeile zeigen auf die Nachkommen.
  - *Nachkommen -\> Vorfahren* - Pfeile zeigen auf die Vorfahren.
  - *Nachkommen \<-\> Vorfahren* - Pfeile zeigen auf beide.
  - *Nachkommen - Vorfahren* - Keine (es werden keine Pfeile angezeigt)

- \- Männer werden mit Blau, Frauen mit Rot dargestellt, sofern oben nicht anders für gefüllt angegeben. Wenn das Geschlecht einer Person unbekannt ist, wird sie grau dargestellt.

  - *Schwarz-Weiß umrandet*
  - *Farbig umrandet*
  - **Farbig gefüllt** (Standardeinstellung)

- um zwischen Frauen und Männern zu unterscheiden

  - **Ohne** (Standardeinstellung)
  - *Weiblich*
  - *Männlich*
  - *Beide*

- Ob (und wo) Gramps-IDs eingeschlossen werden sollen.

  - **Nicht aufnehmen** (Standardeinstellung)
  - *Eine bestehende Linie teilen*
  - *In einer eigenen Linie*

{{-}}

#### Berichtsoptionen (2)

![[_media/FamilyLinesGraph-Graphs-ReportOptions2-tab-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Familienliniengrafik - Grafiken - Berichtsoptionen (2) - Registerkarte Standardoptionen]]

- Wähle das Format aus, um die Namen anzuzeigen. Diese Auswahl wird normalerweise von der Standardeinstellung in für Namensformat übernommen:. Oder wähle eine der folgenden Optionen, um diese Einstellung für den Bericht zu überschreiben:

  - Vorgbe - (in einem neuen Stammbaum ist dies normalerweise *Nachname, Vorname Suffix*)

  - **Nachname, Vorname Suffix** (Standardeinstellung)

  - *Vorname Nachname Suffix*

  - *Vorname*

  - *Haupt Nachnamen, Vorname Patronymikon Suffix*

  - *NACHNAME, Vorname (Üblich)*

  -  (Kontrollkästchen standardmäßig aktiviert)

- Umgang mit (Informationen über) lebende Personen

  - **Aufnehmen und alle Daten** (Standardeinstellung)
  - *Vollständige Namen, aber Daten entfernt*
  - *Vornamen ersetzt und Daten entfernt*
  - *Kompletter Name ersetzt und Daten entfernt*
  - *Nicht enthalten*

- `0` (Standardeinstellung) Wähle die Anzahl der Jahre seit dem Tod aus, um Personen für den Bericht zu berücksichtigen. Ermöglicht die Aufnahme oder den Ausschluss kürzlich verstorbener Personen in den Bericht. Der Standardwert ist 0 Jahre.

- Die Übersetzung, die für den Bericht verwendet wird. Standardmäßig die Sprache, in der du Gramps verwendest

  - Sprachauswahl

- Format und Sprache für Datumsangaben mit Beispielen

  - Vorgabe - Wähle diese Option, um den Standardsatz in für die Option zu verwenden.
  - **JJJJ-MM-TT (ISO) (2024-11-15)** (Standardeinstellung)
  - *Numerisch (15.11.2024)*
  - *Monat Tag, Jahr (November 15. 2024)*
  - *MONAT Tag, Jahr (Nov 15. 2024)*
  - *Tag Monat Jahr (15. November 2024)*
  - *Tag MONAT Jahr (5. Nov 2024)*

-  (Kontrollkästchen standardmäßig aktiviert) - Untergraphen können Grapviz helfen, Ehepartner zusammen zu positionieren, aber bei nicht-trivalen Graphen führen sie zu längeren Linien und größeren Graphen.

{{-}}

#### Personen von Interesse

![[_media/FamilyLinesGraph-Graphs-PeopleOfInterest-tab-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Familienliniengrafik - Grafiken - Personen von Interesse - Registerkarte Standardoptionen]]

Die Grafik funktioniert indem sie mit einer Liste mit "Personen von Interesse" beginnt. Diese initiale Liste von Personen wird dann verwendet um beides zu finden Vorfahren und Nachkommen.

- klicke auf und , um Personen von Interesse hinzuzufügen/entfernen. Wenn du dir unsicher bist, versuche deine Großeltern als Startpersonen hinzuzufügen.

-  (Kontrollkästchen standardmäßig deaktiviert) Ob die Anzahl der Vorfahren begrenzt wird.

  - `50` Vorgabe. Die maximale Anzahl der einzuschließenden Vorfahren. Das Maximum gilt für die Gesamtzahl der Personen, nicht für Generationen, die auf dem Diagramm angezeigt werden sollen.

-  (Kontrollkästchen standardmäßig deaktiviert) Ob die Anzahl der Nachfahrenbegrenzt wird.

  - `50` Vorgabe. Die maximale Anzahl der einzuschließenden Nachkommen. Das Maximum gilt für die Gesamtzahl der Personen, nicht für Generationen, die auf dem Diagramm angezeigt werden sollen.

{{-}}

##### Person auswählen - Enthält auch den Warndialog <Personenname>

Person auswählen - Enthält auch den Warndialog <Personenname> {{-}}

#### Einbeziehen

![[_media/FamilyLinesGraph-Graphs-Include-tab-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Familienliniengrafik - Grafiken - Einbeziehen - Registerkarte Standardoptionen]]

- : Geburtsdatum, Sterbedatum und Heiratsdatum werden in die Grafik aufgenommen, wenn dies ausgewählt wird. (Kontrollkästchen standardmäßig aktiviert)

- : von oben zeige nur die Jahre.(Kontrollkästchen standardmäßig deaktiviert)

- : Geburtsort, Sterbeort und Ort der Eheschließung werden in die Grafik aufgenommen, wenn dies ausgewählt wird.(Kontrollkästchen standardmäßig aktiviert)

- : Der Heiratstext enthält die Gesamtzahl der Kinder, wenn dies ausgewählt ist.(Kontrollkästchen standardmäßig deaktiviert)

-  (Kontrollkästchen standardmäßig aktiviert)

- - **Über dem Namen** (Standardeinstellung)
  - *Neben dem Namen*

- - **Normal** (Standardeinstellung)
  - *Groß*

{{-}}

#### Familienfarben

![[_media/FamilyLinesGraph-Graphs-FamilyColours-tab-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Familienliniengrafik - Grafiken - Familienfarben - Registerkarte Standardoptionen]]

- Wähle die Farbe aus, die für Personen mit einem bestimmten Nachnamen verwendet werden soll. Es stehen zwei Spalten zur Verfügung: **Nachname** und **Farbe**. Klicke auf oder , um einen Nachnamen aus dem Fenster hinzuzufügen, wähle einen Nachnamen aus und drücke . Um die Farbe des Nachnamens zu bearbeiten, doppelklicke auf einen Nachnamen und wähle im Fenster eine der angezeigten Farben aus und wähle dann .

{{-}}

#### Personen

![[_media/FamilyLinesGraph-Graphs-Individuals-tab-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Familienliniengrafik - Grafiken - Personen - Registerkarte Standardoptionen]]

Du kannst im Fenster für jede der folgenden Farben eine Farbe auswählen und dann die Schaltfläche auswählen.

- die Farbe, die verwendet wird, um Männer anzuzeigen.

- die Farbe, die verwendet wird, um Frauen anzuzeigen.

- die Farbe, die verwendet wird, um Personen anzuzeigen, die weder Mann noch Frau sind. (Bis einschließlich 6.0.3 steht hier noch )

- die zu verwendende Farbe, wenn das Geschlecht unbekannt ist (und für Personen, deren Nachname mit keinem der Namen auf der Registerkarte "Familienfarben" übereinstimmt.)

- die Farbe, die verwendet wird, um Familien anzuzeigen. (Hochzeiten)

{{-}}

### <u>Stundenglasdiagramm</u>

![[_media/Graphs-HourglassGraph-example-overview-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Stundenglasdiagramm - Grafiken - Beispielausgabe Übersicht]]

Generiere ein Siehe auch:

- [Gemeinsame Optionen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte_-_Teil_5#Gemeinsame_Optionen) - (GraphViz-spezifisch in Bezug auf Seitennummerierung, Farbe und Details des Diagramms.)

{{-}}

#### Berichtsoptionen

![[_media/HourglassGraph-Graphs-ReportOptions-tab-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Stundenglasdiagramm - Grafiken - Berichtsoptionen - Registerkarte Standardoptionen]]

- die zentrale Person für den Bericht, standardmäßig wird die aktuelle aktive Person verwendet.

  - Schaltfläche. - Ändert die Hauptperson

- Standardeinstellung `10`

- Standardeinstellung `10`

- Wähle die Richtung, in die die Pfeile zeigen:

  - **Zentrum -\> Andere** (Vorgabe) - Pfeile zeigen auf die Anderen.
  - *Zentrum \<- Andere* - Pfeile zeigen auf das Zentrum.
  - *Zentrum \<-\> Andere* - Pfeile zeigen auf beide.
  - *Zentrum - Andere* - Keine (es werden keine Pfeile angezeigt)

- \- Männer werden mit Blau, Frauen mit Rot dargestellt, sofern oben nicht anders für gefüllt angegeben. Wenn das Geschlecht einer Person unbekannt ist, wird sie grau dargestellt.

  - *Schwarz-Weiß umrandet*
  - *Farbig umrandet*
  - **Farbig gefüllt** (Standardeinstellung)

-  um zwischen Frauen und Männern zu unterscheiden(Kontrollkästchen standardmäßig deaktiviert)

- ob Gramps-IDs eingeschlossen werden sollen.

  - **Nicht aufnehmen** (Standardeinstellung)
  - *Eine bestehende Linie teilen*
  - *In einer eigenen Linie*

{{-}}

#### Berichtsoptionen (2)

![[_media/HourglassGraph-Graphs-ReportOptions2-tab-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Stundenglasdiagramm - Grafiken - Berichtsoptionen (2) - Registerkarte Standardoptionen]]

- Wähle das Format aus, um die Namen anzuzeigen. Diese Auswahl wird normalerweise von der Standardeinstellung in [Bearbeiten &gt; Registerkarte Anzeige](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Einstellungen#Anzeige) für Namensformat übernommen:. Oder wähle eine der folgenden Optionen, um diese Einstellung für den Bericht zu überschreiben:

  - Vorgabe - (in einem neuen Stammbaum ist dies normalerweise *Nachname, Vorname Suffix*)

  - **Nachname, Vorname Suffix** (Standardeinstellung)

  - ''Vorname Nachname Suffix

  - *Vorname*

  - *Haupt Nachnamen, Vorname Patronymikon Suffix*

  - *NACHNAME, Vorname (Üblich)*

  -  (Kontrollkästchen standardmäßig aktiviert)

- Umgang mit (Informationen über) lebende Personen

  - **Aufnehmen und alle Daten** (Standardeinstellung)
  - *Vollständige Namen, aber Daten entfernt*
  - *Vornamen ersetzt und Daten entfernt*
  - *Kompletter Name ersetzt und Daten entfernt*
  - *Nicht enthalten*

- `0`(Vorgabe) Wähle die Anzahl der Jahre seit dem Tod aus, um Personen für den Bericht zu berücksichtigen. Ermöglicht die Aufnahme oder den Ausschluss kürzlich verstorbener Personen in den Bericht. Der Standardwert ist 0 Jahre.

- Die Übersetzung, die für den Bericht verwendet wird. Standardmäßig die Sprache, in der du Gramps verwendest

  - Sprachauswahl

- Format und Sprache für Datumsangaben mit Beispielen

  - Vorgabe - Wähle diese Option, um den Standardsatz in für die Option zu verwenden.
  - **JJJJ-MM-TT (ISO) (2018-04-08)** (Standardeinstellung)
  - Numerisch (8.4.2018)
  - Monat Tag, Jahr (April 8. 2018)
  - MONAT Tag, Jahr (Apr 8. 2018)
  - Tag Monat Jahr (8. April 2018)
  - Tag MONAT Jahr (8. Apr 2018)

{{-}}

#### Diagrammstil

![[_media/HourglassGraph-Graphs-GraphStyle-tab-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Stundenglasdiagramm - Grafiken - Diagrammstil - Registerkarte Standardoptionen]]

Du kannst im Fenster für jede der folgenden Farben eine Farbe auswählen und dann die Schaltfläche auswählen.

- die Farbe für Männer zu verwenden.

- die Farbe für Frauen zu verwenden.

- die Farbe, die verwendet wird, um Personen anzuzeigen, die weder Mann noch Frau sind. (Bis einschließlich 6.0.3 steht hier noch )

- die zu verwendende Farbe, wenn das Geschlecht unbekannt ist (und für Personen, deren Nachname mit keinem der Namen auf der Registerkarte "Familienfarben" übereinstimmt.)

- die Farbe für Familien (Hochzeiten).

(Kontrollkästchen standardmäßig deaktiviert) - Erzwingen Sie die Reihenfolge des Sosa / Sosa-Stradonitz / Ahnentafel-Layouts für alle Vorfahren, so dass die Väter immer auf dem linken Zweig und die Mütter auf dem rechten Zweig stehen. (Kontrollkästchen standardmäßig deaktiviert) - Sosa / Sosa-Stradonitz / Ahnentafel-Nummer anzeigen.  - Zeige genealogische Symbole für Geburts-, Heirats- und Todesfälle an. {{-}}

### <u>Beziehungengrafik</u>

![[_media/Graphs-RelationshipGraph-example-overview-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Beziehungengrafik - Grafiken - Beispielausgabe Übersicht]]

Die erstellt eine komplexe Beziehungengrafik unter Verwendung des [GraphViz-Generator](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte_-_Teil_5#Voraussetzungen_für_Diagrammberichte). Über das Menü: Erhälts du ein Fenster, in dem du alle Einstellungen ändern kannst. {{-}} Siehe auch:

- [Gemeinsame Optionen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte_-_Teil_5#Gemeinsame_Optionen) - (GraphViz-spezifisch in Bezug auf Seitennummerierung, Farbe und Details des Diagramms.)

{{-}}

#### Berichtsoptionen

![[_media/RelationshipGraph-Graphs-ReportOptions-tab-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Beziehungengrafik - Grafiken - Berichtsoptionen - Registerkarte Standardoptionen]]

- \- Wähle den Filter aus, der auf den Bericht angewendet werden soll. Wähle aus:

  - **Gesamte Datenbank** (Standardeinstellung) ()
  - *Nachkommen von aktive Person*
  - *Nachkommen Familien von aktive Person*
  - *Vorfahren von aktive Person*
  - *Personen mit gemeinsamen Vorfahren mit aktive Person*
  - *Alle benutzerdefinierten Filter, die du erstellt hast, werden unter den anderen Auswahlmöglichkeiten aufgeführt.*

- Die zentrale Person für den Filter. Standardmäßig ist die aktive Person. Wenn du einen benutzerdefinierten Filter verwendest, kann keine Person ausgewählt werden.

  - Schaltfläche. - Wechselt die Hauptperson

-   
  Wähle die Richtung, in die die Pfeile zeigen:

  - **Nachkommen \<- Vorfahren**(Standardeinstellung) - Pfeile zeigen auf die Nachkommen.
  - *Nachkommen -\> Vorfahren* - Pfeile zeigen auf die Vorfahren.
  - *Nachkommen \<-\> Vorfahren* - Pfeile zeigen auf beide.
  - *Nachkommen - Vorfahren* - Keine (es werden keine Pfeile angezeigt)

- \- Männer werden mit Blau, Frauen mit Rot dargestellt, sofern oben nicht anders für gefüllt angegeben. Wenn das Geschlecht einer Person unbekannt ist, wird sie grau dargestellt.

  - *Schwarz-Weiß umrandet*
  - *Farbig umrandet*
  - **Farbig gefüllt** (Standardeinstellung)

-  um zwischen Frauen und Männern zu unterscheiden (Kontrollkästchen standardmäßig deaktiviert)

-  (Kontrollkästchen standardmäßig deaktiviert)

- ob Gramps-IDs eingeschlossen werden sollen.

  - **Nicht aufnehmen** (Standardeinstellung)
  - *Eine bestehende Linie teilen*
  - *In einer eigenen Linie*

{{-}}

#### Berichtsoptionen (2)

![[_media/RelationshipGraph-Graphs-ReportOptions2-tab-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Beziehungengrafik - Grafiken - Berichtsoptionen (2) - Registerkarte Standardoptionen]]

- Wähle das Format aus, um die Namen anzuzeigen. Diese Auswahl wird normalerweise von der Standardeinstellung in für Namensformat übernommen:. Oder wähle eine der folgenden Optionen, um diese Einstellung für den Bericht zu überschreiben:

  - Vorgbe - (in einem neuen Stammbaum ist dies normalerweise *Nachname, Vorname Suffix*)

  - **Nachname, Vorname Suffix** (Standardeinstellung)

  - *Vorname Nachname Suffix*

  - *Vorname*

  - *Haupt Nachnamen, Vorname Patronymikon Suffix*

  - *NACHNAME, Vorname (Üblich)*

  -  (Kontrollkästchen standardmäßig aktiviert)

- Umgang mit (Informationen über) lebende Personen

  - **Aufnehmen und alle Daten** (Standardeinstellung)
  - *Vollständige Namen, aber Daten entfernt*
  - *Vornamen ersetzt und Daten entfernt*
  - *Kompletter Name ersetzt und Daten entfernt*
  - *Nicht enthalten*

- `0`(Vorgabe) Wähle die Anzahl der Jahre seit dem Tod aus, um Personen für den Bericht zu berücksichtigen. Ermöglicht die Aufnahme oder den Ausschluss kürzlich verstorbener Personen in den Bericht. Der Standardwert ist 0 Jahre.

- Die Übersetzung, die für den Bericht verwendet wird. Standardmäßig die Sprache, in der du Gramps verwendest

  - Sprachauswahl

- Format und Sprache für Datumsangaben mit Beispielen

  - Vorgabe - Wähle diese Option, um den Standardsatz in [Bearbeiten &gt; Registerkarte Anzeige](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Einstellungen#Anzeige) für die Option zu verwenden.
  - **JJJJ-MM-TT (ISO) (2024-11-15)** (Standardeinstellung)
  - *Numerisch (15.11.2024)*
  - *Monat Tag, Jahr (November 15. 2024)*
  - *MONAT Tag, Jahr (Nov 15. 2024)*
  - *Tag Monat Jahr (15. November 2024)*
  - *Tag MONAT Jahr (15. Nov 2024)*

{{-}}

#### Einbeziehen

![[_media/RelationshipGraph-Graphs-Include-tab-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Beziehungengrafik - Grafiken - Einbeziehen - Registerkarte Standardoptionen]]

- \- Ob Daten und/oder Orte aufgenommen werden sollen

  - **Keine Daten oder Orte aufnehmen** (Standardeinstellung)
  - *Geburts-, Hochzeits- und Sterbedaten aufnehmen aber keine Orte*
  - *Geburts-, Hochzeits- und Sterbedaten und Orte aufnehmen*
  - *Geburts-, Hochzeits- und Sterbedaten aufnehmen und Orte wenn kein Datum vorhanden*
  - *Geburts-, Hochzeits- und Sterbejahre aufnehmen aber keine Orte*
  - *Geburts-, Hochzeits- und Sterbejahre und Orte aufnehmen*
  - *Geburts-, Hochzeits- und Sterbeorte aber keine Daten aufnehmen*
  - *Geburts-, Hochzeits- und Sterbedaten und Orte in der selben Zeile aufnehmen*

-  Familienknoten anzeigen, auch wenn die Ausgabe nur ein Mitglied der Familie enthält. (Kontrollkästchen standardmäßig aktiviert)

-  (Kontrollkästchen standardmäßig deaktiviert)

-  (Kontrollkästchen standardmäßig deaktiviert)

-  (Kontrollkästchen standardmäßig deaktiviert)

- Wo das Miniaturbild relativ zum Namen erscheinen soll

  - **Über dem Namen** (Vorgabe)
  - *Neben dem Namen*

- Ob die letzte Beschäftigung aufgenommen werden soll

  - **Keinen Beruf aufnehmen** (Standardeinstellung)
  - *Beschreibung des aktuellsten Berufs aufnehmen*
  - *Datum, Beschreibung und Ortaller Berufe aufnehmen*

-  Whether to include 'Ga' and 'Gb' also, to debug the relationship calculator (Kontrollkästchen standardmäßig deaktiviert)

{{-}}

#### Diagrammstil

![[_media/RelationshipGraph-Graphs-GraphStyle-tab-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Beziehungengrafik - Grafiken - Diagrammstil - Registerkarte Standardoptionen]]

Du kannst im Fenster für jede der folgenden Farben eine Farbe auswählen und dann die Schaltfläche auswählen.

- die Farbe für Männer zu verwenden.

- die Farbe für Frauen zu verwenden.

- die Farbe, die verwendet wird, um Personen anzuzeigen, die weder Mann noch Frau sind. (Bis einschließlich 6.0.3 steht hier noch )

- die zu verwendende Farbe, wenn das Geschlecht unbekannt ist (und für Personen, deren Nachname mit keinem der Namen auf der Registerkarte "Familienfarben" übereinstimmt.)

- die Farbe für Familien (Hochzeiten).

-  (Kontrollkästchen standardmäßig aktiviert) - Zeigt adoptierte Beziehungen

-  (Kontrollkästchen standardmäßig aktiviert)

- Legt die Position der Eltern im Diagramm fest.

  - **Normal** (Vorgabe)
  - *Eltern zusammen*
  - *Eltern versetzt*

{{-}}

#### Beispiel Beziehungengrafik

![[_media/Graphs-RelationshipGraph-example-overview-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Beziehungengrafik - Grafiken - Beispielausgabe Übersicht]]

Ein einfaches Beispiel. Wir wollen eine Beziehungengrafik mit den Nachkommenfamilien einer bestimmten Person.

1.  Überprüfe als erstes ob diese Person die **aktive Person** ist. (Du änderst das später aber dies ist praktischer)

2.  Gehe über das Menü

3.  Papiergröße: A1 metrisch Querformat: wir wissen, dass der Bericht nicht viele Personen enthält also ist dies ok.

4.   Nachkommenfamilien von..., ,

5.  

6.    
      
    15 FreeSans :

7.    
    : 133

8.    
    wir fügen oben einen Titel hinzu in der Größe 18

9.    
    wir wollen eine JPEG Datei und .

Die Ergebnisse ähneln der Abbildung in Abb. {{#var:chapter}}.{{#var:figure}}.. {{-}} Siehe auch:

- Ein detailliertes Tutorial [Wie man ein Beziehungsdiagramm erstellt](wiki:Howto:_Make_a_relationship_chart)

{{-}}

<hr>

Zurück zur [Übersicht der Berichte](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte)

[B](wiki:Category:De:Dokumentation) [Category:Plugins](wiki:Category:Plugins)
