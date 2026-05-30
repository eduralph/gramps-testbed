---
title: De:Gramps 6.0 Wiki Handbuch - Berichte - Teil 6
categories:
- De:Dokumentation
- Plugins
managed: false
source: wiki-scrape
wiki_revid: 131065
wiki_fetched_at: '2026-05-30T17:37:33Z'
lang: de
---

{{#vardefine:chapter\|13.6}} {{#vardefine:figure\|0}} Zurück zur [Übersicht der Berichte](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte).

<hr>

{{-}} ![[_media/MenuOverview-Reports-TextReports-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}}  Menüübersicht]] Dieser Abschnitt beschreibt die verschiedenen in Gramps.

## Textberichte

Textberichte stellen die gewünschten Informationen als formatierten Text dar. Die meisten Optionen sind bei Textberichten gleich, daher werden sie im Abschnitt [Gemeinsame Optionen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte_-_Teil_6#Gemeinsame_Optionen) beschrieben.

Die folgenden *Textberichte* sind in Gramps verfügbar:

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

### Gemeinsame Optionen

Die gemeinsamen Optionen für die Textberichte sind: der Dateiname für die Ausgabe, das Ausgabeformat, gewählter Stil, Seitengröße und Ausrichtung. Für HTML Berichte gibt es keine Seitenangaben. Stattdessen beinhalten die HTML Optionen die Auswahl der HTML Vorlage entweder aus Gramps oder eine von dir selbst erstellte. Optional können die Berichte direkt mit der Standardanwendung geöffnet werden.

Die Optionen die spezifisch für einen bestimmten Bericht sind, werden direkt in dem Eintrag für den Bericht und auf der [Kommandozeilenreferenz](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Kommandozeilen_Referenz#Aktionsoptionen) beschrieben.

Für jeden Bericht gibt es ein Fenster mit Reitern im oberen Bereich (wie Papieroptionen..) und im unteren Bereich die . Die Anzahl der Reiter variiert je nach Bericht.

#### Papieroptionen

![[_media/TextReports-PaperOptions-tab-defaults-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Papieroptionen" - Reiter für Textberichte]]

Mit den kannst du folgendes ändern:

- - **Letter**(Vorgabe)

  - (`8.50` in. Standardeinstellung)

  - (`11.00` in. Standardeinstellung)

  - **Portrait** (Standardeinstellung)

- - (`1.00` in. Standardeinstellung)

  - (`1.00` in. Standardeinstellung)

  - (`1.00` in. Standardeinstellung)

  - (`1.00` in. Standardeinstellung)

-  : ob metrische Werte verwendet werden sollen oder nicht (Zoll oder cm). (Kontrollkästchen standardmäßig deaktiviert)

{{-}}

#### Dokumentoptionen

![[_media/TextReports-DocumentOptions-section-PlainText-output-settings-example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Dokumentoptionen - Registerkarten-Standardeinstellungen für Textberichte (Nur Text - Ausgabe ausgewählt)]] Die folgenden Optionen ändern sich je nach ausgewähltem Ausgabeformat geringfügig.

- wähle das Ausgabeformat:

  - *Drucken...*
  - *PDF Dokument*
  - *HTML*
  - *Open Dokument Text* (wenn du den Bericht mit OpenOffice oder LibreOffice bearbeiten willst)
  - *PostScript*
  - *RTF-Dokument*
  - ''LaTex'
  - *Einfacher Text*

-  du kannst angeben, dass das erstellte Dokument als Standardbetrachter geöffnet werden soll. öffnet den erstellten Bericht mit dem Programm, das auf deinem System für die Verarbeitung des ausgewählten Formats definiert ist. (Kontrollkästchen standardmäßig deaktiviert)

- Vorgabewert ist *`/home/`<Benutzername>`/`<Stammbaumname><Berichtsname>`.`<Ausgabeformaterweiterung>*. Standardmäßig entspricht der Dateiname dem Berichtstyp und wird in deinem Home-Verzeichnis abgelegt. (In Windows ist es standardmäßig eine Ebene höher als "Dokumente".)

- (Standardeinstellung ist *Standardwert*). Mit der Schaltfläche kannst du Dokumentstile hinzufügen.

- (`72` Standardeinstellung)

{{-}}

<hr>

### <u>Ahnentafel-Bericht</u>

![[_media/TextReports-AhnentafelReport-example-overview-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Ahnentafel-Bericht - Textberichte - Beispielausgabe Übersicht]]

Der listet die aktive Person und ihre Vorfahren zusammen mit ihren Lebensdaten.

Du kannst den über auswählen.

Die Personen werden auf eine besondere Weise nummeriert, die ein etabliertes standardisiertes [genealogisches Nummerierungssystem](wiki:Genealogical_Numbering_Systems) namens [Ahnentafel](wiki:Genealogical_Numbering_Systems#ahnentafel) ist. Dieser Bericht enthält einige [Ahnentafel-spezifische Stiloptionen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Einstellungen#Stileditor_Dialog) im Stileditor, auf die über die Schaltfläche zugegriffen werden kann.

Die aktive Person ist Nummer 1. Ihr Vater und Mutter haben die Nummer 2 beziehungsweise 3.

Diese Regel gilt für jede Person während man in den Generationen zurück geht: die Eltern des Vaters sind Nummer 4 und 5 und die Eltern der Mutter sind 6 und 7, Väter haben immer eine gerade und Mütter eine ungerade Nummer.

Es gilt daher für jeder Person mit der Nummer N in dem Baum, die Nummer Von Vater und Mutter sind 2N beziehungsweise 2N+1.

`   Person = n`  
`   Vater = 2n`  
`   Mutter = 2n+1`

Jeder Eintrag besteht aus einem einzigen Absatz und sollte die folgenden Informationen beinhalten:

- Personennummer.
- Name der Person.
- Geburtsinformationen, wenn vorhanden.
- Todesinformationen, wenn vorhanden.
- Beisetzungsinformationen, wenn vorhanden.

Siehe auch [Gemeinsame Optionen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte_-_Teil_6#Gemeinsame_Optionen) {{-}}

#### Berichtsoptionen

![[_media/AhnentafelReport-TextReports-ReportOptions-tab-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Ahnentafel-Bericht - Textberichte - Berichtsoptionen - Registerkarte Standardoptionen]]

-   
  die zentrale Person für den Bericht, es wird standardmäßig die aktuelle aktive Person verwendet.

  - Schaltfläche, um die zentrale Person zu ändern, öffnet die , mit der du die zentrale Person ändern kannst, indem du das Kontrollkästchen aktivierst.

- (`10` Standardeinstellung) Die Anzahl der Generationen, die in den Bericht aufgenommen werden.

- ob Gramps-IDs eingeschlossen werden sollen.

  - **Nicht aufnehmen** (Vorgabe)
  - *Einbeziehen*

-  Ob nach jeder Generation eine neue Seite angefangen wird.(Kontrollkästchen standardmäßig deaktiviert)

-  Legt fest, ob nach dem Namen ein Zeilenumbruch erfolgt.(Kontrollkästchen standardmäßig deaktiviert)

{{-}}

#### Berichtsoptionen (2)

![[_media/AhnentafelReport-TextReports-ReportOptions2-tab-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Ahnentafel-Bericht - Textberichte - Berichtsoptionen (2) - Registerkarte Standardoptionen]]

- Wähle das Format aus, um die Namen anzuzeigen. Diese Auswahl wird normalerweise von der Standardeinstellung in [Bearbeiten &gt; Registerkarte Anzeige](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Einstellungen#Anzeige) für Namensformat übernommen:. Oder wähle eine der folgenden Optionen, um diese Einstellung für den Bericht zu überschreiben:

  - Vorgabe - (in einem neuen Stammbaum ist dies normalerweise *Nachname, Vorname Suffix*)

  - **Nachname, Vorname Suffix** (Standardeinstellung)

  - Vorname Nachname Suffix

  - Vorname

  - Haupt Nachnamen, Vorname Patronymikon Suffix

  - NACHNAME, Vorname (Üblich)

  -  (Kontrollkästchen standardmäßig aktiviert) - Ob vertrauliche Daten eingeschlossen werden sollen.

- Umgang mit (Informationen über) lebende Personen

  - **Aufnehmen und alle Daten** (Standardeinstellung)
  - Vollständige Namen, aber Daten entfernt
  - Vornamen ersetzt und Daten entfernt
  - Kompletter Name ersetzt und Daten entfernt
  - Nicht enthalten

- `0` (Standardeinstellung) Wähle die Anzahl der Jahre seit dem Tod aus, um Personen für den Bericht zu berücksichtigen. Ermöglicht die Aufnahme oder den Ausschluss kürzlich verstorbener Personen in den Bericht. Der Standardwert ist 0 Jahre.

- Die für den Bericht zu verwendende Übersetzung. Sprachauswahl mit allen von Gramps unterstützten Sprachen. Standardmäßig die Sprache, in der du Gramps verwendest.

  - Sprachauswahl

- Format und Sprache für Datumsangaben mit Beispielen

  - Vorgabe - Wähle diese Option, um den Standardsatz in [Bearbeiten &gt; Registerkarte Anzeige](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Einstellungen#Anzeige) für die Option zu verwenden.
  - **JJJJ-MM-TT (ISO) (2018-04-08)** (Standardeinstellung)
  - Numerisch (8.4.2018)
  - Monat Tag, Jahr (April 8. 2018)
  - MONAT Tag, Jahr (Apr 8. 2018)
  - Tag Monat Jahr (8. April 2018)
  - Tag MONAT Jahr (8. Apr 2018)

{{-}}

### <u>Geburtstags- und Jahrestage-Bericht</u>

![[_media/TextReports-BirthdayAndAnniversaryReport-example-overview-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Geburtstags- und Jahrestage-Bericht - Textberichte - Beispielausgabe Übersicht]]

Dieser Bericht erstellt eine Liste der Geburtstage und Jahrestage auf einer Seite nach Monat. Er enthält dieselben Informationen wie ein [Kalenderbericht](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte_-_Teil_4#Kalender), jedoch im Textformat anstelle einer Kalendertabelle.

Du kannst den Geburtstags- und Jubiläumsbericht mit auswählen. {{-}} Siehe auch [Gemeinsame Optionen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte_-_Teil_6#Gemeinsame_Optionen) {{-}}

#### Berichtsoptionen

![[_media/BirthdayAndAnniversaryReport-TextReports-ReportOptions-tab-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Geburtstags- und Jahrestage-Bericht - Textberichte - Berichtsoptionen - Registerkarte Standardoptionen]]

- \- Wähle den Filter aus, der auf den Bericht angewendet werden soll. Wähle aus:

  - **Gesamte Datenbank** (Standardeinstellung)
  - Nachkommen von **Filter Person**
  - Nachkommen Familien von **Filter Person**
  - Vorfahren von **Filter Person**
  - Personen mit gemeinsamen Vorfahren mit **Filter Person**
  - *oder wähle aus den **[benutzerdefinierten Filtern](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Filter#Benutzerdefinierte_Filter)** der Kategorie **Person***

-   
  Die zentrale Person für den Bericht. (Standardmäßig die [aktive Person](wiki:De:Gramps_Glossar#active_person))

  - , um die Filterperson zu ändern, öffne die , mit der du die Filterperson aus den mit [Lesezeichen versehenen Personen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Navigation#Lesezeichen) ändern kannst. Wähle das Kontrollkästchen , um aus dem gesamten Baum auszuwählen.

- `Geburtstags- und Jahrestage-Bericht` (Standardeinstellung) - Titel des Berichts

- `Mein Geburtstage.Bericht` (Standardeinstellung) - Erste Textzeile am Ende des Berichts

- `Erstellt mit Gramps` (Standardeinstellung) - Zweite Textzeile am Ende des Berichts

- [`http://gramps-project.org/`](http://gramps-project.org/) (Standardeinstellung) - Dritte Textzeile am Ende des Berichts

{{-}}

#### Berichtsoptionen (2)

![[_media/BirthdayAndAnniversaryReport-TextReports-ReportOptions2-tab-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Geburtstags- und Jahrestage-Bericht - Textberichte - Berichtsoptionen (2) - Registerkarte Standardoptionen]]

- Wähle das Format aus, um die Namen anzuzeigen. Diese Auswahl wird normalerweise von der Standardeinstellung in [Bearbeiten &gt; Registerkarte Anzeige](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Einstellungen#Anzeige) für Namensformat übernommen:. Oder wähle eine der folgenden Optionen, um diese Einstellung für den Bericht zu überschreiben:

  - Vorgabe - (in einem neuen Stammbaum ist dies normalerweise *Nachname, Vorname Suffix*)

  - **Nachname, Vorname Suffix** (Standardeinstellung)

  - Vorname Nachname Suffix

  - Vorname

  - Haupt Nachnamen, Vorname Patronymikon Suffix

  - NACHNAME, Vorname (Üblich)

  -  (Kontrollkästchen standardmäßig aktiviert) Ob vertrauliche Daten eingeschlossen werden sollen.

  -  (Kontrollkästchen standardmäßig aktiviert) Nur lebende Personen in den Bericht aufnehmen.

- 

- Die für den Bericht zu verwendende Übersetzung. Sprachauswahl mit allen von Gramps unterstützten Sprachen. Standardmäßig die Sprache, in der du Gramps verwendest.

  - Sprachauswahl

  -  (Kontrollkästchen standardmäßig aktiviert)

{{-}}

#### Inhalt

![[_media/BirthdayAndAnniversaryReport-TextReports-Content-tab-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Geburtstags- und Jahrestage-Bericht - Textberichte - Inhalt - Registerkarte Standardoptionen]]

- das Jahr ausfüllen. Standardmäßig das aktuelle Jahr.

- Wähle das Land aus, um die zugehörigen Feiertage anzuzeigen. Standardmäßig werden keine angezeigt.

- Wähle den angezeigten Nachnamen der verheirateten Frau aus.

  - **Frauen benutzen ihren Mädchennamen** (Standardeinstellung)
  - Frauen benutzen den Nachnamen vom Mann (von der ersten gelisteten Familie)
  - Frauen benutzen den Nachnamen vom Mann (von der letzten gelisteten Familie)

-  Ob Geburtstage in den Kalender aufgenommen werden sollen (Kontrollkästchen standardmäßig aktiviert)

-  Ob Jubiläen in den Kalender aufgenommen werden sollen (Kontrollkästchen standardmäßig aktiviert)

-  (Kontrollkästchen standardmäßig aktiviert)

-  Ob Beziehungen zur Filterperson eingeschlossen werden sollen (Hinweis: Langsamere Berichterstellung) (Kontrollkästchen standardmäßig deaktiviert)

{{-}}

### <u>PersonAlles Bericht</u>

![[_media/TextReports-CompleteIndividualReport-example-overview-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} PersonAlles Bericht - Textberichte - Beispielausgabe Übersicht]]

Dieser Bericht liefert persönliche Zusammenfassungen.

Du kannst den PersonAlles Bericht über auswählen.

Siehe auch [Gemeinsame Optionen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte_-_Teil_6#Gemeinsame_Optionen) {{-}}

#### Berichtsoptionen

![[_media/CompleteIndividualReport-TextReports-ReportOptions-tab-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} PersonAlles Bericht - Textberichte - Berichtsoptionen - Registerkarte Standardoptionen]]

Der Vorteil dieses Berichts ist die spezifische Filteroption. Abhängig von der Filterwahl (Nur aktive Person, ihre Nachkommen, ihre Vorfahren oder gesamte Datenbank), kann der Bericht eine bis viele persönliche Zusammenfassungen enthalten. Eine andere Option für diesen Bericht ist die Aufnahme von Quellenangaben beim Auflisten der Ereignisse.

-   
  wähle einen Filter um die Personen, die im Kalender erscheinen einzugrenzen.

  - **Gesamte Datenbank** (Standardeinstellung)
  - Nachkommen von **Filter Person**
  - Nachkommen Familien von **Filter Person**
  - Vorfahren von **Filter Person**
  - Personen mit gemeinsamen Vorfahren mit **Filter Person**
  - *oder wähle aus den **[benutzerdefinierten Filtern](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Filter#Benutzerdefinierte_Filter)** der Kategorie **Person***

-   
  Die zentrale Person für den Bericht. (Standardmäßig die [aktive Person](wiki:De:Gramps_Glossar#active_person))

  - , um die Filterperson zu ändern, öffne die , mit der du die Filterperson aus den mit [Lesezeichen versehenen Personen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Navigation#Lesezeichen) ändern kannst. Wähle das Kontrollkästchen , um aus dem gesamten Baum auszuwählen.

-  (Kontrollkästchen standardmäßig aktiviert)

-  (Kontrollkästchen standardmäßig deaktiviert)

{{-}}

#### Berichtsoptionen (2)

![[_media/CompleteIndividualReport-TextReports-ReportOptions2-tab-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} PersonAlles Bericht - Textberichte - Berichtsoptionen (2) - Registerkarte Standardoptionen]]

- Wähle das Format aus, um die Namen anzuzeigen. Diese Auswahl wird normalerweise von der Standardeinstellung in [Bearbeiten &gt; Registerkarte Anzeige](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Einstellungen#Anzeige) für Namensformat übernommen:. Oder wähle eine der folgenden Optionen, um diese Einstellung für den Bericht zu überschreiben:

  - Vorgabe - (in einem neuen Stammbaum ist dies normalerweise *Nachname, Vorname Suffix*)

  - **Nachname, Vorname Suffix** (Standardeinstellung)

  - Vorname Nachname Suffix

  - Vorname

  - Haupt Nachnamen, Vorname Patronymikon Suffix

  - NACHNAME, Vorname (Üblich)

  -  (Kontrollkästchen standardmäßig aktiviert) Ob vertrauliche Daten eingeschlossen werden sollen.

- Umgang mit (Informationen über) lebende Personen

  - **Aufnehmen und alle Daten** (Standardeinstellung)
  - Vollständige Namen, aber Daten entfernt
  - Vornamen ersetzt und Daten entfernt
  - Kompletter Name ersetzt und Daten entfernt
  - Nicht enthalten

- `0`(Vorgabe) Wähle die Anzahl der Jahre seit dem Tod aus, um Personen für den Bericht zu berücksichtigen. Ermöglicht die Aufnahme oder den Ausschluss kürzlich verstorbener Personen in den Bericht. Der Standardwert ist 0 Jahre.

- Die für den Bericht zu verwendende Übersetzung. Sprachauswahl mit allen von Gramps unterstützten Sprachen. Standardmäßig die Sprache, in der du Gramps verwendest.

  - Sprachauswahl

- Format und Sprache für Datumsangaben mit Beispielen

  - Vorgabe - Wähle diese Option, um den Standardsatz in [Bearbeiten &gt; Registerkarte Anzeige](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Einstellungen#Anzeige) für die Option zu verwenden.
  - **JJJJ-MM-TT (ISO) (2018-04-08)** (Standardeinstellung)
  - Numerisch (8.4.2018)
  - Monat Tag, Jahr (April 8. 2018)
  - MONAT Tag, Jahr (Apr 8. 2018)
  - Tag Monat Jahr (8. April 2018)
  - Tag MONAT Jahr (8. Apr 2018)

{{-}}

#### Einbeziehen

![[_media/CompleteIndividualReport-TextReports-Include-tab-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} PersonAlles Bericht - Textberichte - Einbeziehen - Registerkarte Standardoptionen]]

-  (Kontrollkästchen standardmäßig deaktiviert)

-  (Kontrollkästchen standardmäßig aktiviert)

-  (Kontrollkästchen standardmäßig deaktiviert)

-  (Kontrollkästchen standardmäßig aktiviert)

{{-}}

#### Einbeziehen (2)

![[_media/CompleteIndividualReport-TextReports-Include2-tab-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} PersonAlles Bericht - Textberichte - Einbeziehen (2) - Registerkarte Standardoptionen]]

- ob Gramps-IDs hinzugefügt werden sollen.

  - **Nicht aufnehmen** (Standardeinstellung)
  - Einbeziehen

-  (Kontrollkästchen standardmäßig aktiviert)

-  (Kontrollkästchen standardmäßig aktiviert)

-  (Kontrollkästchen standardmäßig aktiviert)

-  Ob Beziehungen zur Filterperson eingeschlossen werden sollen (Hinweis: Langsamere Berichterstellung) (Kontrollkästchen standardmäßig deaktiviert)

{{-}}

#### Abschnitte

![[_media/CompleteIndividualReport-TextReports-Sections-tab-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} PersonAlles Bericht - Textberichte - Abschnitte - Registerkarte Standardoptionen]]

Wird verwendet, wenn ein separater Abschnitt erforderlich ist.

- -  (Kontrollkästchen standardmäßig aktiviert)

  -  (Kontrollkästchen standardmäßig aktiviert)

  -  (Kontrollkästchen standardmäßig aktiviert)

  -  (Kontrollkästchen standardmäßig aktiviert)

  -  (Kontrollkästchen standardmäßig aktiviert)

  -  (Kontrollkästchen standardmäßig aktiviert)

  -  (Kontrollkästchen standardmäßig aktiviert)

  -  (Kontrollkästchen standardmäßig aktiviert)

  -  (Kontrollkästchen standardmäßig aktiviert)

{{-}}

### <u>Datenbankzusammenfassungsbericht</u>

![[_media/TextReports-DatabaseSummaryReport-example-overview-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Datenbankzusammenfassungsbericht - Textberichte - Beispielausgabe Übersicht]]

Dieser Bericht zeigt eine Gesamtstatistik hinsichtlich Anzahl der Personen jedes Geschlechts, verschiedene unvollständige Einträge Statistiken, genauso wie Familien und Medien Statistiken.

Du kannst diesen Bericht über das Menü aufrufen.

Der Bericht zeigt eine Aufschlüsselung folgender Informationen für den geöffneten Stammbaum

Die Anzahl wird in den verschiedenen Kategorien angezeigt

- **<b>Personen</b>**:
  - Anzahl der Personen:
  - Männer:
  - Frauen:
  - Personen mit unbekanntem Geschlecht:
  - Unvollständige Namen:
  - Personen ohne Geburtsdatum:
  - Einzelstehende Personen:
  - Einmalige Nachnamen:
  - Personen mit Medienobjekten

<!-- -->

- **<b>Familieninformationen</b>**:
  - Anzahl der Familien:

<!-- -->

- **<b>Medienobjekte</b>**:
  - Anzahl von einzelnen Medienobjekten:
  - Gesamtgröße der Medienobjekte: in MB (MegaByte)

<!-- -->

- Fehlende Medienobjekte: dies zeigt den Dateinamen von jedem fehlenden Medienobjekt.

Die in diesem Bericht enthaltenen Informationen entsprechen denen im [Statistik-Gramplet](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Gramplets#Statistik) und ähneln den Ergebnissen aus dem Dialogfeld .

Siehe auch [Gemeinsame Optionen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte_-_Teil_6#Gemeinsame_Optionen) {{-}}

#### Berichtsoptionen

![[_media/DatabaseSummaryReport-TextReports-ReportOptions-tab-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Datenbankzusammenfassungsbericht - Textberichte - Berichtsoptionen - Registerkarte Standardoptionen]]

-  (Kontrollkästchen standardmäßig aktiviert) Ob vertrauliche Daten eingeschlossen werden sollen.

- Umgang mit (Informationen über) lebende Personen

  - **Aufnehmen und alle Daten** (Standardeinstellung)
  - Nicht enthalten

- `0` (Standardeinstellung) Wähle die Anzahl der Jahre seit dem Tod aus, um Personen für den Bericht zu berücksichtigen. Ermöglicht die Aufnahme oder den Ausschluss kürzlich verstorbener Personen in den Bericht. Der Standardwert ist 0 Jahre.

- Die für den Bericht zu verwendende Übersetzung. Sprachauswahl mit allen von Gramps unterstützten Sprachen. Standardmäßig die Sprache, in der du Gramps verwendest.

  - Sprachauswahl

{{-}}

### <u>Nachkommenbericht</u>

![[_media/TextReports-DescendantReport-example-overview-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Nachkommenbericht - Textberichte - Beispielausgabe Übersicht]]

Dieser Bericht zeigt die Nachkommen der aktiven Person mit einer kurzen Beschreibung mit Einrückungen.

Du kannst den Nachkommenbericht über auswählen. {{-}} Siehe auch [Gemeinsame Optionen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte_-_Teil_6#Gemeinsame_Optionen) {{-}}

#### Berichtsoptionen

![[_media/DescendantReport-TextReports-ReportOptions-tab-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Nachkommenbericht - Textberichte - Berichtsoptionen - Registerkarte Standardoptionen]]

Die einzige spezifische Option ist die Anzahl der zu berücksichtigen Nachkommengenerationen.

- die zentrale Person für den Bericht, standardmäßig wird die aktuelle aktive Person verwendet.

  - Schaltfläche, um die zentrale Person zu ändern, öffnet die , mit der du die Hauptperson ändern kannst, indem du das Kontrollkästchen aktivierst.

- Das zu verwendende [Nummerierungssystem](wiki:Genealogical_Numbering_Systems).

  - **[Einfache Nummerierung](wiki:Genealogical_Numbering_Systems#Simple_numbering)** (Standardeinstellung)
  - [d'Aboville](wiki:Genealogical_Numbering_Systems#d.27Aboville) Nummerierung
  - [Henry](wiki:Genealogical_Numbering_Systems#Henry) Nummerierung
  - [Modifiezierte Henry](wiki:Genealogical_Numbering_Systems#modified_henry)-Nummerierung
  - [de Villiers/Pama](wiki:Genealogical_Numbering_Systems#de_villiers) Nummerierung
  - [Meurgey de Tupigny](wiki:Genealogical_Numbering_Systems#meurgey_de_tupigny) Nummerierung

- (`10` Standardeinstellung) Die Anzahl der Generationen, die in den Bericht aufgenommen werden sollen.

-  Ob Heiratsinformationen im Bericht angezeigt werden sollen. (Kontrollkästchen standardmäßig deaktiviert)

-  Ob Scheidungsinformationen im Bericht angezeigt werden sollen. (Kontrollkästchen standardmäßig deaktiviert)

-  Ob Geburts- und Todesinformationen im Bericht angezeigt werden sollen. (Kontrollkästchen standardmäßig aktiviert)

-  Ob doppelte Stammbauminformationen im Bericht angezeigt werden sollen. (Kontrollkästchen standardmäßig deaktiviert)

{{-}}

#### Berichtsoptionen (2)

![[_media/DescendantReport-TextReports-ReportOptions2-tab-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Nachkommenbericht - Textberichte - Berichtsoptionen (2) - Registerkarte Standardoptionen]]

- Wähle das Format aus, um die Namen anzuzeigen. Diese Auswahl wird normalerweise von der Standardeinstellung im

### <u>Detailierter Ahnenbericht</u>

![[_media/TextReports-DetailedAncestralReport-example-overview-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Detailierter Ahnenbericht - Textberichte - Beispielausgabe Übersicht]]

Dieser Bericht behandelt detailliert die Vorfahren der aktiven Person mit einer Reihe von Lebensdaten genauso wie Hochzeiten und Sosa-Stradonitz/Ahnentafelnummerierung. Er teilt viele seiner Eigenschaften mit dem ausführlichen Nachkommenbericht (siehe unten).

Du kannst den ausführlichen Nachkommenbericht mit auswählen. {{-}} Siehe auch [Gemeinsame Optionen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte_-_Teil_6#Gemeinsame_Optionen) {{-}}

#### Berichtsoptionen

![[_media/DetailedAncestralReport-TextReports-ReportOptions-tab-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Detailierter Ahnenbericht - Textberichte - Berichtsoptionen - Registerkarte Standardoptionen]]

Der Bericht ist nach der [Ahnentafelstandardnummerierung](wiki:Genealogical_Numbering_Systems#ahnentafel) gegliedert.

- die zentrale Person für den Bericht, standardmäßig wird die aktuelle aktive Person verwendet.

  - Schaltfläche, um die zentrale Person zu ändern, öffnet die , mit der du die zentrale Person ändern kannst, indem du das Kontrollkästchen aktivierst.

- (`1` Standardeinstellung) Die [Kekule](wiki:Genealogical_Numbering_Systems#sosa-stradonitz)-Nummer der zentralen Person.

- (`10` Standardeinstellung) Die Anzahl der Generationen, die in den Bericht aufgenommen werden sollen.

- ob Gramps-IDs aufgenommen werden sollen.

  - **Nicht aufnehmen** Vorgabe
  - Einbeziehen

- : Ob nach jeder Generation eine neue Seite gestartet werden soll. (Kontrollkästchen standardmäßig deaktiviert)

- : ob eine neue Seite vor den Endnotizen begonnen werden soll (Kontrollkästchen standardmäßig deaktiviert)

{{-}}

#### Berichtsoptionen (2)

![[_media/DetailedAncestralReport-TextReports-ReportOptions2-tab-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Detailierter Ahnenbericht - Textberichte - Berichtsoptionen (2) - Registerkarte Standardoptionen]]

- Wähle das Format aus, um die Namen anzuzeigen. Diese Auswahl wird normalerweise von der Standardeinstellung in [Bearbeiten &gt; Registerkarte Anzeige](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Einstellungen#Anzeige) für Namensformat übernommen:. Oder wähle eine der folgenden Optionen, um diese Einstellung für den Bericht zu überschreiben:

  - Vorgabe - (in einem neuen Stammbaum ist dies normalerweise *Nachname, Vorname Suffix*)
  - **Nachname, Vorname Suffix** (Standardeinstellung)
  - Vorname Nachname Suffix
  - Vorname
  - Haupt Nachnamen, Vorname Patronymikon Suffix
  - NACHNAME, Vorname (Üblich)

-  (Kontrollkästchen standardmäßig aktiviert) Ob vertrauliche Daten eingeschlossen werden sollen.

- Umgang mit (Informationen über) lebende Personen

  - **Aufnehmen und alle Daten** (Standardeinstellung)
  - Vollständige Namen, aber Daten entfernt
  - Vornamen ersetzt und Daten entfernt
  - Kompletter Name ersetzt und Daten entfernt
  - Nicht enthalten

- `0`(Vorgabe) Wähle die Anzahl der Jahre seit dem Tod aus, um Personen für den Bericht zu berücksichtigen. Ermöglicht die Aufnahme oder den Ausschluss kürzlich verstorbener Personen in den Bericht. Der Standardwert ist 0 Jahre.

- Die für den Bericht zu verwendende Übersetzung. Sprachauswahl mit allen von Gramps unterstützten Sprachen. Standardmäßig die Sprache, in der du Gramps verwendest.

  - Sprachauswahl

- Format und Sprache für Datumsangaben mit Beispielen

  - Vorgabe - Wähle diese Option, um den Standardsatz in [Bearbeiten &gt; Registerkarte Anzeige](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Einstellungen#Anzeige) für die Option zu verwenden.
  - **JJJJ-MM-TT (ISO) (2018-04-08)** (Standardeinstellung)
  - Numerisch (8.4.2018)
  - Monat Tag, Jahr (April 8. 2018)
  - MONAT Tag, Jahr (Apr 8. 2018)
  - Tag Monat Jahr (8. April 2018)
  - Tag MONAT Jahr (8. Apr 2018)

{{-}}

#### Inhalt

![[_media/DetailedAncestralReport-TextReports-Content-tab-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Detailierter Ahnenbericht - Textberichte - Inhalt - Registerkarte Standardoptionen]]

- : ob ganze Sätze oder eine prägnante Sprache verwendet wird.(Kontrollkästchen standardmäßig aktiviert)

- : ob vollständige Datumsangaben statt Jahreszahlen verwendet werden sollen.(Kontrollkästchen standardmäßig aktiviert)

- : ob das Sterbealter einer Person berechnet werden soll.(Kontrollkästchen standardmäßig aktiviert)

- : ob doppelte Vorfahren weggelassen werden sollen.(Kontrollkästchen standardmäßig aktiviert)

- : ob der Rufname als Vorname verwendet werden soll. (Kontrollkästchen standardmäßig deaktiviert)

{{-}}

#### Einbeziehen

![[_media/DetailedAncestralReport-TextReports-Include-tab-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Detailierter Ahnenbericht - Textberichte - Einbeziehen - Registerkarte Standardoptionen]]

- : Gibt an, ob das Geschlechtssymbol vorangestellt werden soll (Kontrollkästchen standardmäßig deaktiviert). Hinweis: Diese Option funktioniert nicht für die PDF-Ausgabe auf Mac. Verwende eine andere Ausgabe, wenn du Geschlechtssymbole wünschst.

- : ob Kinder aufgelistet werden sollen. (Kontrollkästchen standardmäßig aktiviert)

- : ob die Ehegatten der Kinder aufgeführt werden sollen. (Kontrollkästchen standardmäßig aktiviert)

- : ob Ereignisse eingeschlossen werden sollen. (Kontrollkästchen standardmäßig aktiviert)

- : ob andere Ereignisse einbezogen werden sollen, an denen Personen teilgenommen haben. (Kontrollkästchen standardmäßig deaktiviert)

- : ob Verweise auf Nachkommen in die Liste der Kinder aufgenommen werden sollen. (Kontrollkästchen standardmäßig deaktiviert)

-  (Kontrollkästchen standardmäßig deaktiviert)

{{-}}

#### Einbeziehen (2)

![[_media/DetailedAncestralReport-TextReports-Include2-tab-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Detailierter Ahnenbericht - Textberichte - Einbeziehen (2) - Registerkarte Standardoptionen]]

-  (Kontrollkästchen standardmäßig aktiviert)

-  (Kontrollkästchen standardmäßig deaktiviert)

-  (Kontrollkästchen standardmäßig deaktiviert)

-  (Kontrollkästchen standardmäßig deaktiviert)

-  (Kontrollkästchen standardmäßig deaktiviert)

-  (Kontrollkästchen standardmäßig deaktiviert)

{{-}}

#### Fehlende Information

![[_media/DetailedAncestralReport-TextReports-MissingInformation-tab-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Detailierter Ahnenbericht - Textberichte - Fehlende Information - Registerkarte Standardoptionen]]

-   
  Ob fehlende Orte durch Leerzeichen ersetzt werden sollen.(Kontrollkästchen standardmäßig deaktiviert)

-   
  Ob fehlende Daten durch Leerzeichen ersetzt werden sollen.(Kontrollkästchen standardmäßig deaktiviert)

{{-}}

### <u>Detailierter Nachkommenbericht</u>

![[_media/TextReports-DetailedDescendantReport-example-overview-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Detailierter Nachkommenbericht - Textberichte - Beispielausgabe Übersicht]]

Dieser Bericht behandelt detailliert die Nachkommen der aktiven Person nach Generationen der genealogischen Tradition von Nachkommenberichten in Textform nach Generationen folgend. Er beabsichtigt alle wichtigen Eigenschaften, die in diesem klassischen Nachkommenberichtformat erwartet werden zu liefern und wurde von verschiedenen Quellen beeinflusst. Das Gramps Team betrachtet es als eines seiner Ziele die Realisierbarkeit der Übernahme dieses Berichts für professionelle Ahnenforschungseinrichtungen Weltweit. Als Konsequenz ist diese ein sehr stark anpassbarer Bericht.

Der Bericht enthält eine Reihe von Lebensdaten, Hochzeiten und (optional) Notizen und Partnerinformationen. Unter den vielen Optionen ist die Anzahl der Nachkommengenerationen, ob Alter berechnet werden, der Textstil von kompletten Sätzen und Kurzformen und ob Bilder aufgenommen werden zu bedenken. Der Bericht verwendet standardmäßig [Henry-System Nummerierung](http://wiki-de.genealogy.net/Henry-System) und bietet [d'Aboville-System Nummerierung](http://wiki-de.genealogy.net/D%27Aboville-System) und [Register-System Nummerierung](http://en.wikipedia.org/wiki/Genealogical_numbering_systems#Register_System) als Optionen.

Du kannst den Detailierter Nachkommenbericht mit auswählen. {{-}} Siehe auch

- [Gemeinsame Optionen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte_-_Teil_6#Gemeinsame_Optionen)

{{-}}

#### Berichtsoptionen

![[_media/DetailedDescendantReport-TextReports-ReportOptions-tab-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Detailierter Nachkommenbericht - Textberichte - Berichtsoptionen - Registerkarte Standardoptionen]]

- die zentrale Person für den Bericht, standardmäßig wird die aktuelle aktive Person verwendet.

  - Schaltfläche, um die zentrale Person zu ändern, öffnet die , mit der du die zentrale Person ändern kannst, indem du das Kontrollkästchen aktivierst.

- das zu verwendende [Nummerierungssystem](http://en.wikipedia.org/wiki/Genealogical_numbering_systems#Register_System).

  - **Henry-Nummerierung** (Standardeinstellung)
  - d'Aboville Nummerierung
  - Datensatz (Modifizierte Register) Nummerierung

- Wie die Personen im Bericht organisiert sind

  - **zeige Personen nach Generationen** (Standardeinstellung)
  - zeige Personen nach Abstammungslinie

- (`10` Standardeinstellung) Die Anzahl der Generationen, die in den Bericht aufgenommen werden sollen.

- ob Gramps-IDs eingeschlossen werden sollen.

  - **Nicht aufnehmen** Vorgabe
  - Einbeziehen

-   
  Ob nach jeder Generation eine neue Seite angefangen wird. (Kontrollkästchen standardmäßig deaktiviert)

-   
  ob eine neue Seite vor den Endnotizen begonnen werden soll (Kontrollkästchen standardmäßig deaktiviert)

{{-}}

#### Berichtsoptionen (2)

![[_media/DetailedDescendantReport-TextReports-ReportOptions2-tab-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Detailierter Nachkommenbericht - Textberichte - Berichtsoptionen (2) - Registerkarte Standardoptionen]]

- Wähle das Format aus, um die Namen anzuzeigen. Diese Auswahl wird normalerweise von der Standardeinstellung in [Bearbeiten &gt; Registerkarte Anzeige](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Einstellungen#Anzeige) für Namensformat übernommen:. Oder wähle eine der folgenden Optionen, um diese Einstellung für den Bericht zu überschreiben:

  - Vorgabe - (in einem neuen Stammbaum ist dies normalerweise *Nachname, Vorname Suffix*)
  - **Nachname, Vorname Suffix** (Standardeinstellung)
  - Vorname Nachname Suffix
  - Vorname
  - Haupt Nachnamen, Vorname Patronymikon Suffix
  - NACHNAME, Vorname (Üblich)

-  (Kontrollkästchen standardmäßig aktiviert) Ob vertrauliche Daten eingeschlossen werden sollen.

- Umgang mit (Informationen über) lebende Personen

  - **Aufnehmen und alle Daten** (Standardeinstellung)
  - Vollständige Namen, aber Daten entfernt
  - Vornamen ersetzt und Daten entfernt
  - Kompletter Name ersetzt und Daten entfernt
  - Nicht enthalten

- `0`(Vorgabe) Wähle die Anzahl der Jahre seit dem Tod aus, um Personen für den Bericht zu berücksichtigen. Ermöglicht die Aufnahme oder den Ausschluss kürzlich verstorbener Personen in den Bericht. Der Standardwert ist 0 Jahre.

- Die für den Bericht zu verwendende Übersetzung. Sprachauswahl mit allen von Gramps unterstützten Sprachen. Standardmäßig die Sprache, in der du Gramps verwendest.

  - Sprachauswahl

- Format und Sprache für Datumsangaben mit Beispielen

  - Vorgabe - Wähle diese Option, um den Standardsatz in \[\[De:Gramps_6.0_Wiki_Handbuch\_-\_Einstellungen#Anzeige\|Bearbeiten \> Registerkarte Anzeige}} für die Option zu verwenden.
  - **JJJJ-MM-TT (ISO) (2018-04-08)** (Standardeinstellung)
  - Numerisch (8.4.2018)
  - Monat Tag, Jahr (April 8. 2018)
  - MONAT Tag, Jahr (Apr 8. 2018)
  - Tag Monat Jahr (8. April 2018)
  - Tag MONAT Jahr (8. Apr 2018)

{{-}}

#### Inhalt

![[_media/DetailedDescendantReport-TextReports-Content-tab-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Detailierter Nachkommenberichtt - Textberichte - Content - Registerkarte Standardoptionen]]

- : ob ganze Sätze oder eine prägnante Sprache verwendet wird.(Kontrollkästchen standardmäßig aktiviert)

- : ob vollständige Datumsangaben statt Jahreszahlen verwendet werden sollen.(Kontrollkästchen standardmäßig aktiviert)

- : ob das Sterbealter einer Person berechnet werden soll.(Kontrollkästchen standardmäßig aktiviert)

- : ob der Rufname als Vorname verwendet werden soll. (Kontrollkästchen standardmäßig deaktiviert)

{{-}}

#### Einbeziehen

![[_media/DetailedDescendantReport-TextReports-Include-tab-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Detailierter Nachkommenbericht - Textberichte - Einbeziehen - Registerkarte Standardoptionen]]

- : ob Kinder aufgelistet werden sollen.(Kontrollkästchen standardmäßig aktiviert)

- : ob die Ehegatten der Kinder aufgeführt werden sollen.(Kontrollkästchen standardmäßig deaktiviert)

-  (Kontrollkästchen standardmäßig deaktiviert)

-  (Kontrollkästchen standardmäßig deaktiviert)

- : ob Ereignisse eingeschlossen werden sollen. (Kontrollkästchen standardmäßig deaktiviert)

- : ob Verweise auf Nachkommen in die Liste der Kinder aufgenommen werden sollen. (Kontrollkästchen standardmäßig aktiviert)

-  (Kontrollkästchen standardmäßig deaktiviert)

{{-}}

#### Einbeziehen (2)

![[_media/DetailedDescendantReport-TextReports-Include2-tab-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Detailierter Nachkommenbericht - Textberichte - Include (2) - Registerkarte Standardoptionen]]

-  (Kontrollkästchen standardmäßig aktiviert)

-  (Kontrollkästchen standardmäßig deaktiviert)

-  (Kontrollkästchen standardmäßig deaktiviert)

-  (Kontrollkästchen standardmäßig deaktiviert)

-  (Kontrollkästchen standardmäßig deaktiviert)

-  (Kontrollkästchen standardmäßig deaktiviert)

-  (Kontrollkästchen standardmäßig aktiviert)

-  (Kontrollkästchen standardmäßig deaktiviert)

{{-}}

#### Fehlende Information

![[_media/DetailedDescendantReport-TextReports-MissingInformation-tab-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Detailierter Nachkommenbericht - Textberichte - Fehlende Information - Registerkarte Standardoptionen]]

-   
  Ob fehlende Orte durch Leerzeichen ersetzt werden sollen.(Kontrollkästchen standardmäßig deaktiviert)

-   
  Ob fehlende Daten durch Leerzeichen ersetzt werden sollen.(Kontrollkästchen standardmäßig deaktiviert)

{{-}}

### <u>Linienendebericht</u>

![[_media/TextReports-EndOfLineReport-example-overview-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Linienendebericht - Textberichte - Beispielausgabe Übersicht]]

Liefert eine Liste der letzten bekannten Vorfahren einer Person mit der Ahnenreihe sortiert nach Generationen.

Du kannst den Linienendebericht mit auswählen. {{-}} Siehe auch [Gemeinsame Optionen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte_-_Teil_6#Gemeinsame_Optionen) {{-}}

#### Berichtsoptionen

![[_media/EndOfLineReport-TextReports-ReportOptions-tab-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Linienendebericht - Textberichte - Berichtsoptionen - Registerkarte Standardoptionen]]

- die zentrale Person für den Bericht, standardmäßig wird die aktuelle aktive Person verwendet.

  - Schaltfläche. - Ändert die Hauptperson.

- Wähle das Format aus, um die Namen anzuzeigen. Diese Auswahl wird normalerweise von der Standardeinstellung in [Bearbeiten &gt; Registerkarte Anzeige](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Einstellungen#Anzeige) für Namensformat übernommen:. Oder wähle eine der folgenden Optionen, um diese Einstellung für den Bericht zu überschreiben:

  - Vorgabe - (in einem neuen Stammbaum ist dies normalerweise *Nachname, Vorname Suffix*)
  - **Nachname, Vorname Suffix** (Standardeinstellung)
  - Vorname Nachname Suffix
  - Vorname
  - Haupt Nachnamen, Vorname Patronymikon Suffix
  - NACHNAME, Vorname (Üblich)

-  (Kontrollkästchen standardmäßig aktiviert) Ob vertrauliche Daten eingeschlossen werden sollen.

- Umgang mit (Informationen über) lebende Personen

  - **Aufnehmen und alle Daten** (Standardeinstellung)
  - Vollständige Namen, aber Daten entfernt
  - Vornamen ersetzt und Daten entfernt
  - Kompletter Name ersetzt und Daten entfernt
  - Nicht enthalten

- `0`(Vorgabe) Wähle die Anzahl der Jahre seit dem Tod aus, um Personen für den Bericht zu berücksichtigen. Ermöglicht die Aufnahme oder den Ausschluss kürzlich verstorbener Personen in den Bericht. Der Standardwert ist 0 Jahre.

- Die für den Bericht zu verwendende Übersetzung. Sprachauswahl mit allen von Gramps unterstützten Sprachen. Standardmäßig die Sprache, in der du Gramps verwendest.

  - Sprachauswahl

- Format und Sprache für Datumsangaben mit Beispielen

  - Vorgabe - Wähle diese Option, um den Standardsatz in \[\[De:Gramps_6.0_Wiki_Handbuch\_-\_Einstellungen#Anzeige\|Bearbeiten \> Registerkarte Anzeige}} für die Option zu verwenden.
  - **JJJJ-MM-TT (ISO) (2018-04-08)** (Standardeinstellung)
  - Numerisch (8.4.2018)
  - Monat Tag, Jahr (April 8. 2018)
  - MONAT Tag, Jahr (Apr 8. 2018)
  - Tag Monat Jahr (8. April 2018)
  - Tag MONAT Jahr (8. Apr 2018)

{{-}}

### <u>Familiengruppenbericht</u>

![[_media/TextReports-FamilyGroupReport-example-overview-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Familiengruppenbericht - Textberichte - Beispielausgabe Übersicht]]

Er erstellt einen Familiengruppenbericht der Informationen zu einem Elternpaar und seinen Kindern zeigt.

Du kannst den Familiengruppenbericht mit auswählen. {{-}} Siehe auch

- [Gemeinsame Optionen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte_-_Teil_6#Gemeinsame_Optionen)
- [Familienblatt](wiki:Addon:Family_Sheet) Erweiterung - beinhaltet die Ausgabe von Quellen.

{{-}}

#### Berichtsoptionen

![[_media/FamilyGroupReport-TextReports-ReportOptions-tab-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Familiengruppenbericht - Textberichte - Berichtsoptionen - Registerkarte Standardoptionen]]

- \- Wählen den Filter aus, der auf den Bericht angewendet werden soll. Wähle aus:

  - **Vorgabe** - Standardmäßig wird die aktive Familie für die aktuelle aktive Person verwendet.
  - Jede Familie
  - Nachkommenfamilien - von der aktiven Familie
  - Vorfahrenfamilien - von der aktiven Familie

- Die zentrale Familie für den Filter. Standardmäßig wird die aktive Familie für die aktuelle aktive Person verwendet.

  - Schaltfläche, die die Auswahlbox öffnet, mit der du die Filterfamilie ändern kannst, indem du das Kontrollkästchen aktivierst.

- : Erstellt Berichte für alle Nachkommen dieser Familie.(Kontrollkästchen standardmäßig deaktiviert)

{{-}}

#### Berichtsoptionen (2)

![[_media/FamilyGroupReport-TextReports-ReportOptions2-tab-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Familiengruppenbericht - Textberichte - Berichtsoptionen (2) - Registerkarte Standardoptionen]]

- Wähle das Format aus, um die Namen anzuzeigen. Diese Auswahl wird normalerweise von der Standardeinstellung in [Bearbeiten &gt; Registerkarte Daten](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Einstellungen#Anzeigeoptionen) im Anzeigeoptionen Abschnitt für Namensformat übernommen:. Oder wähle eine der folgenden Optionen, um diese Einstellung für den Bericht zu überschreiben:

  - Vorgabe - (in einem neuen Stammbaum ist dies normalerweise *Nachname, Vorname Suffix*)
  - **Nachname, Vorname Suffix** (Standardeinstellung)
  - Vorname Nachname Suffix
  - Vorname
  - Haupt Nachnamen, Vorname Patronymikon Suffix

- Wählt das Format für die Anzeige der Orte

  - **Standard**
  - Voll
  - NACHNAME, Vorname (Üblich)

-  (Kontrollkästchen standardmäßig aktiviert) Ob vertrauliche Daten eingeschlossen werden sollen.

- Umgang mit (Informationen über) lebende Personen

  - **Aufnehmen und alle Daten** (Standardeinstellung)
  - Vollständige Namen, aber Daten entfernt
  - Vornamen ersetzt und Daten entfernt
  - Kompletter Name ersetzt und Daten entfernt
  - Nicht enthalten

- `0`(Vorgabe) Wähle die Anzahl der Jahre seit dem Tod aus, um Personen für den Bericht zu berücksichtigen. Ermöglicht die Aufnahme oder den Ausschluss kürzlich verstorbener Personen in den Bericht. Der Standardwert ist 0 Jahre.

- Die für den Bericht zu verwendende Übersetzung. Sprachauswahl mit allen von Gramps unterstützten Sprachen. Standardmäßig die Sprache, in der du Gramps verwendest.

  - Sprachauswahl

- Format und Sprache für Datumsangaben mit Beispielen

  - Vorgabe - Wähle diese Option, um den Standardsatz in [Bearbeiten &gt; Registerkarte Anzeige](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Einstellungen#Anzeige) für die Option zu verwenden.
  - **JJJJ-MM-TT (ISO) (2018-04-08)** (Standardeinstellung)
  - Numerisch (8.4.2018)
  - Monat Tag, Jahr (April 8. 2018)
  - MONAT Tag, Jahr (Apr 8. 2018)
  - Tag Monat Jahr (8. April 2018)
  - Tag MONAT Jahr (8. Apr 2018)

{{-}}

#### Einbeziehen

![[_media/FamilyGroupReport-TextReports-Include-tab-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Familiengruppenbericht - Textberichte - Einbeziehen - Registerkarte Standardoptionen]]

- : Ob Heiratsinformationen für Eltern aufgenommen werden sollen. (Kontrollkästchen standardmäßig aktiviert)

- : Ob Ereignisse der Eltern aufgenommen werden sollen. (Kontrollkästchen standardmäßig deaktiviert)

- : Ob Adressen für Eltern aufgenommen werden sollen. (Kontrollkästchen standardmäßig deaktiviert)

- : Ob Notizen für Eltern hinzugefügt werden sollen. (Kontrollkästchen standardmäßig deaktiviert)

- : Ob Attribute der Eltern eingeschlossen werden sollen. (Kontrollkästchen standardmäßig deaktiviert)

- : Ob alternative Namen der Eltern eingeschlossen werden soll. (Kontrollkästchen standardmäßig deaktiviert)

{{-}}

#### Einbeziehen (2)

![[_media/FamilyGroupReport-TextReports-Include2-tab-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Familiengruppenbericht - Textberichte - Einbeziehen (2) - Registerkarte Standardoptionen]]

- ob Gramps-IDs eingeschlossen werden sollen.

  - **Nicht aufnehmen** (Vorgabe)
  - Einbeziehen

- : Ob Notizen für Familien hinzugefügt werden sollen. (Kontrollkästchen standardmäßig deaktiviert)

- : Ob Daten für Verwandte aufgenommen werden sollen. (Kontrollkästchen standardmäßig deaktiviert)

- : Ob Heiratsinformationen für Kinder aufgenommen werden sollen.(Kontrollkästchen standardmäßig aktiviert)

- : Ob die Generation für jedem aufgenommen werden soll.(Kontrollkästchen standardmäßig deaktiviert)

- : Ob Felder für fehlende Informationen eingefügt werden sollen. (Kontrollkästchen standardmäßig aktiviert)

{{-}}

### <u>Verwandtschaftsbericht</u>

![[_media/TextReports-KinshipReport-example-overview-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Verwandtschaftsbericht - Textberichte - Beispielausgabe Übersicht]]

Er liefert die Verwandtschaft der gewählten Person entsprechend der vom Anwender gesetzten Suchtiefe (Generationen hoch runter).

Du kanndst die Verwandtschaftsbericht über auswählen. {{-}} Siehe auch:

- [Gemeinsame Optionen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte_-_Teil_6#Gemeinsame_Optionen)
- [Lokalisierung des Beziehungsrechners](wiki:Specification:Relationship_Calculator) - Erstelle aussagekräftige Beziehungsbeschreibungen in deiner Region.

{{-}}

#### Berichtsoptionen

![[_media/KinshipReport-TextReports-ReportOptions-tab-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Verwandtschaftsbericht - Textberichte - Berichtsoptionen - Registerkarte Standardoptionen]]

- die zentrale Person für den Bericht, standardmäßig wird die aktuelle aktive Person verwendet.

  - Schaltfläche, um die zentrale Person zu ändern, öffnet die , mit der du die zentrale Person ändern kannst, indem du das Kontrollkästchen aktivierst.

- (`2` Standardeinstellung) Die maximale Anzahl von Nachkommengenerationen. Bei Bedarf kannst du eine größere Zahl eingeben.

- (`2` Standardeinstellung) Die maximale Anzahl von Vorfahrengenerationen. Bei Bedarf kannst du eine größere Zahl eingeben.

- : Ob Ehepartner einbezogen werden sollen. (Kontrollkästchen standardmäßig aktiviert)

- : Ob Cousins oder Cousinen einbezogen werden sollen. (Kontrollkästchen standardmäßig aktiviert)

- : Ob Tanten/Onkel/Neffen/Nichten einbezogen werden sollen. (Kontrollkästchen standardmäßig aktiviert)

{{-}}

#### Berichtsoptionen (2)

![[_media/KinshipReport-TextReports-ReportOptions2-tab-51.de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Verwandtschaftsbericht - Textberichte - Berichtsoptionen (2) - Registerkarte Standardoptionen]]

- Wähle das Format aus, um die Namen anzuzeigen. Diese Auswahl wird normalerweise von der Standardeinstellung in [Bearbeiten &gt; Registerkarte Anzeige](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Einstellungen#Anzeige) für Namensformat übernommen:. Oder wähle eine der folgenden Optionen, um diese Einstellung für den Bericht zu überschreiben:

  - Vorgabe - (in einem neuen Stammbaum ist dies normalerweise *Nachname, Vorname Suffix*)
  - **Nachname, Vorname Suffix** (Standardeinstellung)
  - Vorname Nachname Suffix
  - Vorname
  - Haupt Nachnamen, Vorname Patronymikon Suffix
  - NACHNAME, Vorname (Üblich)

-  (Kontrollkästchen standardmäßig aktiviert) Ob vertrauliche Daten eingeschlossen werden sollen.

- Umgang mit (Informationen über) lebende Personen

  - **Aufnehmen und alle Daten** (Standardeinstellung)
  - Vollständige Namen, aber Daten entfernt
  - Vornamen ersetzt und Daten entfernt
  - Kompletter Name ersetzt und Daten entfernt
  - Nicht enthalten

- `0`(Vorgabe) Wähle die Anzahl der Jahre seit dem Tod aus, um Personen für den Bericht zu berücksichtigen. Ermöglicht die Aufnahme oder den Ausschluss kürzlich verstorbener Personen in den Bericht. Der Standardwert ist 0 Jahre.

- Die für den Bericht zu verwendende Übersetzung. Sprachauswahl mit allen von Gramps unterstützten Sprachen. Standardmäßig die Sprache, in der du Gramps verwendest.

  - Sprachauswahl

- Format und Sprache für Datumsangaben mit Beispielen

  - Vorgabe - Wähle diese Option, um den Standardsatz in [Bearbeiten &gt; Registerkarte Anzeige](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Einstellungen#Anzeige) für die Option zu verwenden.
  - **JJJJ-MM-TT (ISO) (2018-04-08)** (Standardeinstellung)
  - Numerisch (8.4.2018)
  - Monat Tag, Jahr (April 8. 2018)
  - MONAT Tag, Jahr (Apr 8. 2018)
  - Tag Monat Jahr (8. April 2018)
  - Tag MONAT Jahr (8. Apr 2018)

{{-}}

### <u>Notiz Verknüpfung Bericht</u>

![[_media/TextReports-NoteLinkReport-example-overview-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Notiz Verknüpfung Bericht - Textberichte - Beispielausgabe Übersicht]]

Mit dem kannst du überprüfen, ob Links in Notizen gültig sind.

Dieser Bericht zeigt und überprüft den Status der *internen Linkkonsistenz* in Gramps-Notizen, die mit dem [Verknüpfungeditor](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Daten_eingeben_und_bearbeiten:_Ausführlich_-_Teil_2#Verkn.C3.BCpfungeditor) erstellt wurden, und listet nur externe Internetadressen auf, die mit dem [Internetadresseneditor](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Daten_eingeben_und_bearbeiten:_Ausführlich_-_Teil_1#Internetadresseneditor) erstellt wurden, ohne sie zu überprüfen.

Du kannst den Notiz Verknüpfung Bericht über auswählen.

Für diesen Bericht sind keine Optionen verfügbar.[1](https://web.archive.org/web/20210123144928/http://gramps.1791082.n4.nabble.com/Privacy-td4671118.html#a4671131)

Siehe auch:

- [Gemeinsame Optionen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte_-_Teil_6#Gemeinsame_Optionen)
- [Verknüpfungeditor](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Daten_eingeben_und_bearbeiten:_Ausführlich_-_Teil_2#Verkn.C3.BCpfungeditor)
- [Internetadresseneditor](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Daten_eingeben_und_bearbeiten:_Ausführlich_-_Teil_1#Internetadresseneditor).

{{-}}

### <u>Anzahl der Vorfahren Bericht</u>

![[_media/TextReports-NumberOfAncestorsReport-example-overview-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Anzahl der Vorfahren Bericht - Textberichte - Beispielausgabe Übersicht]]

Dieser Bericht zeigt die Anzahl der Vorfahren der aktiven Person.

Wähle einfach eine Person und klicke im Menü .

Der Bericht zeigt die folgenden Details:

  
Generation 1 hat 1 Person : 100% : Dies ist die Person, mit der du gestartet hast.

Generation 2 hat 2 Personen : 100% : Beide Eltern sind bekannt

.....

Generation 8 hat 35 Personen : 27.34 % dies bedeutet von den (2^7) 128 möglichen Vorfahren in Generation 8 sind 27% bekannt.

Die gesamt Vorfahren in Generation 2 bis .. werden in Gesamtzahl und prozentual angegeben. {{-}} Siehe auch [Gemeinsame Optionen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte_-_Teil_6#Gemeinsame_Optionen) {{-}}

#### Berichtsoptionen

![[_media/NumberOfAncestorsReport-TextReports-ReportOptions-tab-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Anzahl der Vorfahren Bericht - Textberichte - Berichtsoptionen - Registerkarte Standardoptionen]]

- die zentrale Person für den Bericht, standardmäßig wird die aktuelle aktive Person verwendet.

  - Schaltfläche, um die zentrale Person zu ändern, öffnet die , mit der du die zentrale Person ändern kannst, indem du das Kontrollkästchen aktivierst.

- Wähle das Format aus, um die Namen anzuzeigen. Diese Auswahl wird normalerweise von der Standardeinstellung in [Bearbeiten &gt; Registerkarte Anzeige](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Einstellungen#Anzeige) für Namensformat übernommen:. Oder wähle eine der folgenden Optionen, um diese Einstellung für den Bericht zu überschreiben:

  - Vorgabe - (in einem neuen Stammbaum ist dies normalerweise *Nachname, Vorname Suffix*)
  - **Nachname, Vorname Suffix** (Standardeinstellung)
  - Vorname Nachname Suffix
  - Vorname
  - Haupt Nachnamen, Vorname Patronymikon Suffix
  - NACHNAME, Vorname (Üblich)

-  (Kontrollkästchen standardmäßig aktiviert) - Ob vertrauliche Daten eingeschlossen werden sollen.

- Die für den Bericht zu verwendende Übersetzung. Sprachauswahl mit allen von Gramps unterstützten Sprachen. Standardmäßig die Sprache, in der du Gramps verwendest.

  - Sprachauswahl

{{-}}

### <u>Ortsbericht</u>

![[_media/TextReports-PlaceReport-example-overview-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Ortsbericht - Textberichte - Beispielausgabe Übersicht]]

Erstellt einen Bericht entsprechend der vom Anwender ausgewählten Orte.

Er listet auf die Orte bezogene Personen und Ereignisse.

Du kannst den Ortsbericht über auswählen.

Siehe auch [Gemeinsame Optionen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte_-_Teil_6#Gemeinsame_Optionen) {{-}}

#### Berichtsoptionen

![[_media/PlaceReport-TextReports-ReportOptions-tab-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Ortsbericht - Textberichte - Berichtsoptionen - Registerkarte Standardoptionen]]

- Wähle Orte mit einem benutzerdefinierten Filter aus, den du zuvor erstellt hast.

- Liste der Orte, über die berichtet werden soll.

  - Schaltfläche - Ruft das Auswahldialogfeld auf, damit du einen Ort auswählen kannst.

  - Schaltfläche - Wähle einen Ort in der Liste aus und drücken dann diese Taste, um den Ort zu entfernen.

- \- Ob der Bericht ereignis- oder personenzentriert ist.

  - **Ereignis** (Standardeinstellung)
  - Person

{{-}}

#### Berichtsoptionen (2)

![[_media/PlaceReport-TextReports-ReportOptions2-tab-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Ortsbericht - Textberichte - Berichtsoptionen (2) - Registerkarte Standardoptionen]]

- Wähle das Format aus, um die Namen anzuzeigen. Diese Auswahl wird normalerweise von der Standardeinstellung in [Bearbeiten &gt; Registerkarte Anzeige](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Einstellungen#Anzeige) für Namensformat übernommen:. Oder wähle eine der folgenden Optionen, um diese Einstellung für den Bericht zu überschreiben:

  - Vorgabe - (in einem neuen Stammbaum ist dies normalerweise *Nachname, Vorname Suffix*)
  - **Nachname, Vorname Suffix** (Standardeinstellung)
  - Vorname Nachname Suffix
  - Vorname
  - Haupt Nachnamen, Vorname Patronymikon Suffix
  - NACHNAME, Vorname (Üblich)

- \- Wähle das Format aus, um Orte anzuzeigen. Diese Auswahl wird normalerweise von der Standardeinstellung in [Bearbeiten &gt; Anzeige](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Einstellungen#Anzeige) Registerkarte für übernommen. Oder wähle eine der folgenden Optionen, um diese Einstellung für den Bericht zu überschreiben:

  - Vorgabe

  - Vollständig

  -  (Kontrollkästchen standardmäßig aktiviert) Ob vertrauliche Daten eingeschlossen werden sollen.

- Umgang mit (Informationen über) lebende Personen

  - **Aufnehmen und alle Daten** (Standardeinstellung)
  - Vollständige Namen, aber Daten entfernt
  - Vornamen ersetzt und Daten entfernt
  - Kompletter Name ersetzt und Daten entfernt
  - Nicht enthalten

- `0`(Vorgabe) Wähle die Anzahl der Jahre seit dem Tod aus, um Personen für den Bericht zu berücksichtigen. Ermöglicht die Aufnahme oder den Ausschluss kürzlich verstorbener Personen in den Bericht. Der Standardwert ist 0 Jahre.

- Die für den Bericht zu verwendende Übersetzung. Sprachauswahl mit allen von Gramps unterstützten Sprachen. Standardmäßig die Sprache, in der du Gramps verwendest.

  - Sprachauswahl

- Format und Sprache für Datumsangaben mit Beispielen

  - Vorgabe - Wähle diese Option, um den Standardsatz in [Bearbeiten &gt; Registerkarte Anzeige](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Einstellungen#Anzeige) für die Option zu verwenden.
  - **JJJJ-MM-TT (ISO) (2018-04-08)** (Standardeinstellung)
  - Numerisch (8.4.2018)
  - Monat Tag, Jahr (April 8. 2018)
  - MONAT Tag, Jahr (Apr 8. 2018)
  - Tag Monat Jahr (8. April 2018)
  - Tag MONAT Jahr (8. Apr 2018)

{{-}}

### <u>Rekordebericht</u>

![[_media/TextReports-RecordsReport-example-overview-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Rekordebericht - Textberichte - Beispielausgabe Übersicht]]

Der Rekordebericht zeigt eine Reihe interessanter Rekorde (meistens altersbezogen) aus deiner Datenbank, wie älteste lebende Person, jüngste Mutter usw..

Du kannst den Rekordebericht mit aufrufen.

Ein identisches [Rekorde Gramplet](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Gramplets#Rekorde) ist ebenfalls erhältlich.

Siehe auch [Gemeinsame Optionen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte_-_Teil_6#Gemeinsame_Optionen) {{-}}

#### Berichtsoptionen

![[_media/RecordsReport-TextReports-ReportOptions-tab-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Rekordebericht - Textberichte - Berichtsoptionen - Registerkarte Standardoptionen]]

Eine Auswahl der zu druckenden Datensätze ist möglich und eine akzeptable liste "positiver Rekorde" ist vorausgewählt (die meisten Menschen betrachten z.B. eine lange Ehe als ein positiven Rekord, wobei eine frühe Scheidung eher ein negativer gesehen Rekord wird).

- \- Select the filter to be applied to the report. Choose from:

  - **Gesammte Datenbank** (Standardeinstellung)
  - Nachkommen von aktiven Person
  - Nachkommenfamilien von aktiven Person
  - Vorfahren von aktive Person
  - Personen mit gemeinsamen Vorfahren mit aktive Person
  - *Jeder von dir erstellte benutzerdefinierte Filter wird unter den anderen Auswahlmöglichkeiten aufgeführt.*

- Die zentrale Person für den Filter. Standardmäßig ist die aktive Person.

  - , um die Filterperson zu ändern, öffne die , mit der du die Filterperson aus den mit [Lesezeichen versehenen Personen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Navigation#Lesezeichen) ändern kannst. Wähle das Kontrollkästchen , um aus dem gesamten Baum auszuwählen.

- `3` (Vorgabe)

- - **Rufnamen nicht verwenden**(Standardeinstellung)
  - Vornamen durch Rufnamen ersetzen - (Siehe Vorbehalte)
  - Rufname in Vornamen unterstreichen / Rufname zum Vornamen hinzufügen

- Vorgabe = leeres Feld

{{-}}

#### Berichtsoptionen (2)

![[_media/RecordsReport-TextReports-ReportOptions2-tab-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Rekordebericht - Textberichte - Berichtsoptionen (2) - Registerkarte Standardoptionen]]

- Wähle das Format aus, um die Namen anzuzeigen. Diese Auswahl wird normalerweise von der Standardeinstellung in [Bearbeiten &gt; Registerkarte Anzeige](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Einstellungen#Anzeige) für Namensformat übernommen:. Oder wähle eine der folgenden Optionen, um diese Einstellung für den Bericht zu überschreiben:

  - Vorgabe - (in einem neuen Stammbaum ist dies normalerweise *Nachname, Vorname Suffix*)
  - **Nachname, Vorname Suffix** (Standardeinstellung)
  - Vorname Nachname Suffix
  - Vorname
  - Haupt Nachnamen, Vorname Patronymikon Suffix
  - NACHNAME, Vorname (Üblich)

-  (Kontrollkästchen standardmäßig aktiviert) Ob vertrauliche Daten eingeschlossen werden sollen.

- Umgang mit (Informationen über) lebende Personen

  - **Aufnehmen und alle Daten** (Standardeinstellung)
  - Vollständige Namen, aber Daten entfernt
  - Vornamen ersetzt und Daten entfernt
  - Kompletter Name ersetzt und Daten entfernt
  - Nicht enthalten

- `0`(Vorgabe) Wähle die Anzahl der Jahre seit dem Tod aus, um Personen für den Bericht zu berücksichtigen. Ermöglicht die Aufnahme oder den Ausschluss kürzlich verstorbener Personen in den Bericht. Der Standardwert ist 0 Jahre.

- Die für den Bericht zu verwendende Übersetzung. Sprachauswahl mit allen von Gramps unterstützten Sprachen. Standardmäßig die Sprache, in der du Gramps verwendest.

  - Sprachauswahl

{{-}}

#### Person 1

![[_media/RecordsReport-TextReports-Person1-tab-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Rekordebericht - Textberichte - Person 1 - Registerkarte Standardoptionen]]

-  (Kontrollkästchen standardmäßig aktiviert)

-  (Kontrollkästchen standardmäßig aktiviert)

-  (Kontrollkästchen standardmäßig deaktiviert)

-  (Kontrollkästchen standardmäßig aktiviert)

-  (Kontrollkästchen standardmäßig aktiviert)

-  (Kontrollkästchen standardmäßig aktiviert)

-  (Kontrollkästchen standardmäßig deaktiviert)

-  (Kontrollkästchen standardmäßig deaktiviert)

{{-}}

#### Person 2

![[_media/RecordsReport-TextReports-Person2-tab-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Rekordebericht - Textberichte - Person 2 - Registerkarte Standardoptionen]]

-  (Kontrollkästchen standardmäßig aktiviert)

-  (Kontrollkästchen standardmäßig aktiviert)

-  (Kontrollkästchen standardmäßig aktiviert)

-  (Kontrollkästchen standardmäßig aktiviert)

-  (Kontrollkästchen standardmäßig deaktiviert)

-  (Kontrollkästchen standardmäßig deaktiviert)

-  (Kontrollkästchen standardmäßig deaktiviert)

-  (Kontrollkästchen standardmäßig deaktiviert)

{{-}}

#### Familie

![[_media/RecordsReport-TextReports-Family-tab-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Rekordebericht - Textberichte - Familie - Registerkarte Standardoptionen]]

-  (Kontrollkästchen standardmäßig aktiviert)

-  (Kontrollkästchen standardmäßig aktiviert)

-  (Kontrollkästchen standardmäßig aktiviert)

-  (Kontrollkästchen standardmäßig deaktiviert)

-  (Kontrollkästchen standardmäßig aktiviert)

-  (Kontrollkästchen standardmäßig aktiviert)

-  (Kontrollkästchen standardmäßig aktiviert)

{{-}}

### <u>Etikettenbericht</u>

![[_media/TextReports-TagReport-example-overview-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Etikettenbericht - Textberichte - Beispielausgabe Übersicht]]

Hier wird die Etikettenverwendung für primäre Objekte (Person, Familie, Notizen) aufgelistet, die dem ausgewählten [Etikett](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Filter#Etikettierung) entsprechen.

Du kannst den Etikettenbericht über auswählen.

Siehe auch [Gemeinsame Optionen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte_-_Teil_6#Gemeinsame_Optionen) {{-}}

#### Berichtsoptionen

![[_media/TagReport-TextReports-ReportOptions-tab-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Markierungenbericht - Textberichte - Berichtsoptionen - Registerkarte Standardoptionen]]

- Wähle die [Markierung](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Filter#Markieren), die für den Bericht verwendet werden soll.

- Wähle das Format aus, um die Namen anzuzeigen. Diese Auswahl wird normalerweise von der Standardeinstellung in für Namensformat übernommen:. Oder wähle eine der folgenden Optionen, um diese Einstellung für den Bericht zu überschreiben:

  - Vorgabe - (in einem neuen Stammbaum ist dies normalerweise *Nachname, Vorname Suffix*)
  - **Nachname, Vorname Suffix** (Standardeinstellung)
  - Vorname Nachname Suffix
  - Vorname
  - Haupt Nachnamen, Vorname Patronymikon Suffix
  - NACHNAME, Vorname (Üblich)

- \- Wähle das Format aus, um Orte anzuzeigen. Diese Auswahl wird normalerweise von der Standardeinstellung in Registerkarte für übernommen. Oder wähle eine der folgenden Optionen, um diese Einstellung für den Bericht zu überschreiben:

  - Vorgabe
  - Vollständig

-  (Kontrollkästchen standardmäßig aktiviert) Ob vertrauliche Daten eingeschlossen werden sollen.

- Umgang mit (Informationen über) lebende Personen

  - **Aufnehmen und alle Daten** (Standardeinstellung)
  - Vollständige Namen, aber Daten entfernt
  - Vornamen ersetzt und Daten entfernt
  - Kompletter Name ersetzt und Daten entfernt
  - Nicht enthalten

- `0` (Standardeinstellung) Wähle die Anzahl der Jahre seit dem Tod aus, um Personen für den Bericht zu berücksichtigen. Ermöglicht die Aufnahme oder den Ausschluss kürzlich verstorbener Personen in den Bericht. Der Standardwert ist 0 Jahre.

- Die für den Bericht zu verwendende Übersetzung. Sprachauswahl mit allen von Gramps unterstützten Sprachen. Standardmäßig die Sprache, in der du Gramps verwendest.

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

<hr>

Zurück zur [Übersicht der Berichte](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte).

[B](wiki:Category:De:Dokumentation) [Category:Plugins](wiki:Category:Plugins)
