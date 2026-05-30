---
title: De:Gramps 6.0 Wiki Handbuch - Berichte - Teil 4
categories:
- De:Dokumentation
- Plugins
- Stub
managed: false
source: wiki-scrape
wiki_revid: 131007
wiki_fetched_at: '2026-05-30T17:35:55Z'
lang: de
---

{{#vardefine:chapter\|13.4}} {{#vardefine:figure\|0}} Zurück zur [Übersicht der Berichte](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte).

<hr>

{{-}} ![[_media/MenuOverview-Reports-GraphicalReports-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}}  Menüübersicht]] Dieser Abschnitt beschreibt die verschiedenen von Gramps.

## Grafische Berichte

*Grafische Berichte* stellen Informationen in Form von Diagrammen und Grafiken dar. Die meisten Optionen sind bei grafischen Berichten gleich, daher werden sie im Abschnitt [Gemeinsame Optionen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte_-_Teil_4#Gemeinsame_Optionen) beschrieben. Alle Optionen, die für einen bestimmten Bericht spezifisch sind, werden direkt im Eintrag dieses Berichts beschrieben. Siehe auch [Werte ersetzen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte_-_Teil_2#Werte_ersetzen).

Die folgenden „grafischen Berichte” sind in Gramps verfügbar:

- 

- 

- 

- 

- 

- 

- 

### Gemeinsame Optionen

Allgemeine Optionen für Textberichte sind der Dateiname der Ausgabe, das Format der Ausgabe, der gewählte Stil, die Seitengröße und die Ausrichtung. Für HTML-Berichte gibt es keine Seiteninformationen. Stattdessen beinhalten die HTML-Optionen die Wahl der HTML-Vorlage, die entweder in Gramps verfügbar ist oder eine von dir definierte benutzerdefinierte Vorlage. Optional können die Berichte sofort mit der Standardanwendung geöffnet werden.

Die für einen bestimmten Bericht spezifischen Optionen werden direkt im Eintrag dieses Berichts und in den [Befehlszeilenreferenzen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Kommandozeilen_Referenz#Aktionsoptionen) beschrieben.

Für jeden Bericht gibt es einen Bildschirm mit im oberen Teil Registerkarten (wie **Papieroptionen**...) und im unteren Teil die **Dokumentoptionen**. Die Anzahl der Registerkarten variiert je nach Bericht.

#### Papieroptionen

![[_media/TextReports-PaperOptions-tab-defaults-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Papieroptionen - Reiter für Grafische Berichte]]

Mit den kannst du folgendes ändern:

- - **Letter**(Vorgabe)

  - (`8.50` in. Standardeinstellung)

  - (`11.00` in. Standardeinstellung)

  - **Portrait**(Standardeinstellung)

- - (`1.00` in. Standardeinstellung)

  - (`1.00` in. Standardeinstellung)

  - (`1.00` in. Standardeinstellung)

  - (`1.00` in. Standardeinstellung)

-  : ob metrische Werte verwendet werden sollen oder nicht (Zoll oder cm). (Kontrollkästchen standardmäßig deaktiviert) (Siehe *Eine systemweite Einstellung für metrische Einheiten hinzufügen, die in einzelnen Berichten bis zum Neustart von Gramps überschrieben werden kann.* )

Siehe auch [Bericht konnte nicht erstellt werden](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Fehler_und_Warnung_Referenz#Bericht_konnte_nicht_erstellt_werden) Dialog, der auftreten kann, wenn deine benutzerdefinierte Seitengröße zu groß ist. {{-}}

#### Dokumentoptionen

Die folgenden Optionen ändern sich je nach ausgewähltem Ausgabeformat geringfügig. ![[_media/GraphicalReports-DocumentOptions-section-SVG-document-output-settings-example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Dokumentoptionen - SVG-Dokument - Ausgabe ausgewählt - Beispiel]]

- wähle das Ausgabeformat:

  - *PostScript*
  - *Open Dokument Text* (wenn du den Bericht mit OpenOffice oder LibreOffice bearbeiten willst)
  - *PDF Dokument*
  - *Drucken...*

-  du kannst angeben, dass das erstellte Dokument als Standardbetrachter geöffnet werden soll. öffnet den erstellten Bericht mit dem Programm, das auf deinem System für die Verarbeitung des ausgewählten Formats definiert ist. (Kontrollkästchen standardmäßig deaktiviert)

- Vorgabewert ist *`/home/`<Benutzername>`/`<Stammbaumname><Berichtsname>`.`<Ausgabeformaterweiterung>*. Standardmäßig entspricht der Dateiname dem Berichtstyp und wird in deinem Home-Verzeichnis abgelegt. (In Windows ist es standardmäßig eine Ebene höher als "Dokumente".)

- (Vorgabe ist *Standardwert*). Mit der Schaltfläche kannst du Dokumentstile hinzufügen.

- (**Transparenter Hintergrund** Standardeinstellung)

{{-}}

#### Eine Person für den Bericht wählen Auswahl

![[_media/SelectAPersonForTheReport-SelectorDialog-example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Eine Person für den Bericht wählen" - Auswahl Dialog - Beispiel]]

Mit der Auswahl kannst du eine bereits existierende Person für den Bericht auswählen und diese nach der Auswahl als zentrale Person in den platzieren.

Standardmäßig wird die aktuell aktive Person verwendet.

{{-}} Siehe auch:

- [Person wählen Auswahl](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Daten_eingeben_und_bearbeiten:_Ausführlich_-_Teil_1#Person_w.C3.A4hlen_Auswahl)

#### Optionen zum Skalieren und Größe Ändern

Der Baum wird erst auf einer Arbeitsfläche die jede Baumgröße aufnehmen kann erstellt. Von dieser Arbeitsfläche können die folgenden Optionen ändern wie er endgültig auf einer Seite angezeigt wird. {{-}}

##### 

Diese Option ändert die Größe größer/kleiner des Berichts auf der Arbeitsfläche so das er auf die Seitengröße (gesetzt in den Papieroptionen) auf der du drucken möchtest passt. Aktuell kannst du:

- (Standardeinstellung)

- 

- (Breite und Höhe)

Ohne die aktivierte Option geschieht folgendes:

- gibt dir einen Bericht ausgeben, der sich sowohl horizontal als auch vertikal über mehrere Seiten erstrecken kann.

- gibt einen Bericht aus, der sich immer noch vertikal über mehrere Seiten erstrecken kann. Keine Seiten nebeneinander. Nur eine Seite über der Anderen.

- gibt den Bericht auf nur einer Seite aus. Der Bericht wird auf einer Seite mit dem Format aus den Papieroptionen ausgegeben.

##### 

Diese Option legt fest, wie groß/klein die Seite wird auf der wir drucken. **Wenn diese Option nicht aktiviert ist**, ist es die Seitengröße aus den Papieroptionen. Wenn diese Option aktiviert ist, passiert folgendes basierend auf den drei Auswahlmöglichkeiten in .

Dies sagt (fast) alles zu ignorieren, was in den Papieroptionen festgelegt ist, und auf einer Seite zu drucken, die die selben Ausmaße hat wie der Baum auf der Arbeitsfläche. Also hat das Verwenden der Optionen unter wenn du die Option aktivierst folgende Auswirkungen:

- Mit Diese Option ignoriert die Einstellungen unter Papieroptionen komplett und druckt auf einer Seite, die groß genug ist, um den gesamten Baum abzubilden.
- Mit Diese Option ignoriert nur die Seitenhöhe aus den Papieroptionen. Der Baum wurde bereits auf die Seitenbreite die gesetzt wurde skaliert. Nur die Seitenhöhe wird an den zu druckenden Baum angepasst.
- Mit Der Baum wurde bereits auf Seitengröße skaliert. Aber wie weiter oben schon erwähnt, wird die Ausgabe entweder in der Breite oder Höhe (größer als üblich) eine Lücke besitzen (weiße Fläche). Die Option reduziert diese Lücke auf der Seite um sie zu entfernen.

##### Faktor für den Y-Kästchenabstand

  
Vergrößere oder verkleinere den Y-Abstand zwischen den Boxen

##### Skalierungsfaktor für Kästchenschatten

  
Vergrößere oder verkleinere den Kästchenschatten

##### Wissen auf was du drucken willst

Das skalieren eines Baumes ist eine Funktion für fortgeschrittene. Die → legt die Größe des Text den du drucken kannst fest. Verkleinern ist nicht sehr wünschenswert da der Text schwerer zu lesen ist. Vergrößern ist besser kann aber den selben Effekt haben. Hier einige Punkte um schön gedruckte Dokumente zu erhalten.

Das Wichtigste zuerst. Auf welchen Papiergrößen KANNST du drucken? Schau dich um und stell fest, auf welcher Papiergröße du einfach drucken kannst. Bloß zu wissen, auf welcher Papiergröße du drucken KANNST, hilft schon sehr viel. Es gibt Copy-Shops die Ausdrucke auf A0 Endlospapier (auf einer Rolle) anbieten. Für den Fall können wir die Optionen und 'Einseitenbericht' verwenden.

Es ist auch erwähnenswert, den Bericht mit den Optionen und mit dem Wert zu erstellen, um festzustellen was die reale Größe (Breite und Höhe) des Berichts ist. Dies hilft dir festzustellen wie du den Bericht auf Seiten, auf die du drucken kannst, verteilen kannst. Hier noch schnell einige andere Dinge auf die du achten solltest.

- Ein Bericht, der sehr hoch aber nicht besonders breit ist, kann eventuell besser gedruckt werden, wenn nur die Option gesetzt ist.
- Mit der normalen Breite des Berichts, was lässt sich besser drucken? Querformat oder Hochformat?
- Da die Breite jeder Box durch die Breite der breitesten Box festgelegt wird, kannst du die Nachkommen Berichte → Ersetzen Option für Abkürzungen verwenden oder sehr lange Bereiche, die nicht benötigt werden entfernen?
- Die Größe des Titel. Wenn der Platz vorhanden ist, kannst du den Titel größer machen. Und wenn er zu groß ist, legt er die Breite des Bericht fest.

{{-}}

<hr>

### <u>Ahnentafel</u>

![[_media/GraphicalReports-AncestorTree-example-landscape-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Ahnentafel - Grafische Berichte - Beispielausgabe Übersicht]]

Der Bericht erstellt ein Diagramm von Personen, die Vorfahren der aktiven Person sind.

Wähle aus dem Menü . {{-}} Siehe auch [gemeinsame Optionen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte_-_Teil_4#Gemeinsame_Optionen) {{-}}

#### Baumoptionen

![[_media/AncestorTree-GraphicalReports-TreeOptions-tab-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Ahnentafel - Grafische Berichte - Baumoptionen - Registerkarte Standardoptionen]]

- Die zentrale Person des Baums. Standardmäßig ist dies die aktive Person.

  - Schaltfläche. - Ändere die zentrale Person.

-  Ob nur die zentrale Person oder auch alle ihre Geschwister angezeigt werden sollen (das Kontrollkästchen ist standardmäßig nicht markiert)

- (`10` Vorgabe) Die Anzahl der Generationen, die in den Baum aufgenommen werden sollen

- Die Anzahl der Generationen der leeren Kästchen, die angezeigt werden sollen (wenn der Baum nicht vollständig gefüllt ist).

  - **Keine Generierung von leeren Feldern für unbekannte Vorfahren** (Voreinstellung)

- *\# Generation(en) von leeren Boxen für unbekannte Vorfahren* (bis zu 9 Generationen von leeren Boxen anzeigen)

-  Ob zusätzliche leere Felder für unbekannte Personen entfernt werden sollen (standardmäßig ist das Kontrollkästchen aktiviert)

-  Index jeder Person anzeigen (Kontrollkästchen standardmäßig deaktiviert)

- (`1` Vorgabe) Der Startindex

{{-}}

#### Berichtsoptionen

![[_media/AncestorTree-GraphicalReports-ReportOptions-tab-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Ahnentafel - Grafische Berichte - Berichtsoptionen - Registerkarte Standardoptionen]]

Auf dieser Registerkarte hast du die Möglichkeit, andere Elemente in den Bericht aufzunehmen.

- wähle einen Titels für den Bericht.

  - **Ohne Titel** (Vorgabe)
  - **Berichttitel aufnehmen**

-  (Kontrollkästchen ist standardmäßig deaktiviert)

-  (Kontrollkästchen ist standardmäßig aktiviert)

- Baum passend skalieren vergrößert oder verkleinert den Baum, damit er wie gewünscht auf die Seite passt. Die Optionen sind:

  - **Baum nicht skalieren** (Vorgabe)
  - **Baum nur auf Seitenbreite skalieren**
  - **Baum auf Seitengröße skalieren**

-  (standardmäßig deaktiviert) macht die Seite größer oder kleiner, damit sie zum Baum passt.

-  (Kontrollkästchen ist standardmäßig deaktiviert)

Wenn sowohl als auch ausgewählt sind, werden die Optionen in dieser Reihenfolge ausgeführt; zuerst wird der Baum skaliert, dann die Seite.

Diese beiden Optionen und werden in [gemeinsame Optionen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte_-_Teil_4#Gemeinsame_Optionen) mit Tipps zum Erstellen schönerer Berichte besser beschrieben. {{-}}

#### Berichtsoptionen (2)

![[_media/AncestorTree-GraphicalReports-ReportOptions2-tab-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Ahnentafel - Grafische Berichte - Berichtsoptionen (2) - Registerkarte Standardoptionen]]

- Wähle das Format aus, um die Namen anzuzeigen. Diese Auswahl wird normalerweise von der Standardeinstellung in [Bearbeiten &gt; Registerkarte Anzeige](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Einstellungen#Anzeige) für Namensformat übernommen:. Oder wähle eine der folgenden Optionen, um diese Einstellung für den Bericht zu überschreiben:

  - Vorgabe - (in einem neuen Stammbaum ist dies normalerweise *Nachname, Vorname Suffix*)
  - **Nachname, Vorname Suffix** (Vorgabe)
  - *Vorname Nachname Suffix*
  - *Vorname*
  - *Haupt Nachnamen, Vorname Patronymikon Suffix*
  - *NACHNAME, Vorname (Üblich)*

- Wie lebende Personen behandelt werden. Wähle aus:

  - **Aufnehmen und alle Daten** (Vorgabe)
  - *Vollständige Namen, aber Daten entfernt*
  - *Vornamen ersetzt und Daten entfernt*
  - *Kompletter Name ersetzt und Daten entfernt*
  - *Nicht enthalten*

- Whether to restrict data on recently-dead people. Wähle die Anzahl der Jahre seit dem Tod aus, um Personen für den Bericht zu berücksichtigen. Ermöglicht die Aufnahme oder den Ausschluss kürzlich verstorbener Personen in den Bericht. Der (Standardwert ist `0` Jahre.)

  -  (Kontrollkästchen standardmäßig aktiviert)

- Die Übersetzung, die für den Bericht verwendet wird. Standardmäßig die Sprache, in der du Gramps verwendest

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

#### Anzeige

![[_media/AncestorTree-GraphicalReports-Display-tab-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Ahnentafel - Grafische Berichte - Anzeige - Registerkarte Standardoptionen]]

In diesem Reiter kannst du das für diesen Bericht festlegen. Alle Väter, Großväter und so weiter verwenden dieses Format.

Das wird für alle Mütter, Großmütter und so weiter verwendet.

Die `{}` um die Zeile mit den Todesinformationen zeigt an, das der Text '†' NUR angezeigt wird, wenn es Todesinformationen gibt. Für mehr Informationen inklusive wie Orte und Attribute aufgenommen werden oder Namen, Daten und Orte formatiert werden siehe [Werte ersetzen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte_-_Teil_2).

ermöglicht dir festzulegen, ob die zentrale Person das Anzeigeformat des Vaters oder das Anzeigeformat der Mutter auf der Registerkarte Anzeige verwendet.

legt fest, das ein extra Kästchen zwischen Vater und Mutter mit den Heiratsinformationen ausgegeben wird. Das (siehe [Werte ersetzen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte_-_Teil_2)) legt fest, was in diesem Kästchen ausgegeben wird.

{{-}}

#### Erweitert

![[_media/AncestorTree-GraphicalReports-Advanced-tab-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Ahnentafel - Grafische Berichte - Erweitert - Registerkarte Standardoptionen]]

- Auf diese Weise kannst du durch '`/`' getrennte Zeichenfolgenpaare einfügen, die den Text angeben, den du durch anderen Text ersetzen möchtest. Beispiel: `Vereinigte Staaten von Amerika/USA` ersetzt die Vereinigten Staaten von Amerika durch USA. Die Breite jeder Spalte wird durch das breiteste Feld im Bericht bestimmt. Wenn also ein Feld viel breiter ist als die anderen, wird viel Platz verschwendet. Mit der Option „Zeichenfolge ersetzen“ kannst du Teile der Zeichenfolge entfernen oder abkürzen, die nicht benötigt werden oder gekürzt werden können, so dass nur wenig Platz verschwendet wird.

  -  Du kannst das Kontrollkästchen Notiz einschließen aktivieren, um eine Notiz hinzuzufügen (das Kontrollkästchen ist standardmäßig deaktiviert).

- gibt den Text an, den die Notiz enthalten wird. Wenn du den Ersetzungswert “`$T`” in die Notiz einfügst, wird der Tag angezeigt, an dem der Bericht erstellt wurde. Es gilt die normale Datumsformatierung (siehe [Ersetzungswerte](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte_-_Teil_2)).

- Gib an, wo auf der Seite die Notiz platziert werden soll. Derzeit wird an einer Ecke eine Notiz angebracht. Wenn eine Personenbox darüber schreibt, bewegt sich die Notizbox nicht. Wähle eine andere Option für die Positionierung der Notiz, wenn dies der Fall ist.

  - **Oben links** (Vorgabe)
  - *Unten links*
  - *Unten rechts*

Die folgenden zwei Optionen werden unter [Größenoptionen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte_-_Teil_4#Optionen_zum_Skalieren_und_Gr.C3.B6.C3.9Fe_.C3.84ndern) mit Tipps zum Erstellen schönerer Berichte besser beschrieben.

- Macht den Kästchenabstand größer oder kleiner (Standardeinstellung ist `1.00` in.).

- Macht den Kästchenschatten größer oder kleiner (Standardeinstellung ist `1.00` in.).

{{-}}

### <u>Kalender</u>

![[_media/GraphicalReports-Calendar-example-landscape-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Kalender - Grafische Berichte - Beispielausgabe Übersicht]]

Dieser Bericht erstellt einen Kalender mit Geburtstagen und Jubiläen mit einer Seite pro Monat.

Du kannst den Kalenderbericht über auswählen.

Du kannst dieselben Informationen drucken, jedoch im Textformat, indem du den [Geburtstags- und Jahrestagebericht](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte_-_Teil_6#Geburtstags-_und_Jahrestage-Bericht) verwendest.

Siehe [Kalenderwerkzeug Feiertage](wiki:Calendar_tools_holidays) (englisch) wie die Feiertage, die in der Kalenderzusatzmodulausgabe erscheinen hinzugefügt oder geändert werden. {{-}} Siehe auch [gemeinsame Optionen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte_-_Teil_4#Gemeinsame_Optionen) {{-}}

#### Berichtsoptionen

![[_media/Calendar-GraphicalReports-ReportOptions-tab-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Kalender - Grafische Berichte - Berichtsoptionen - Registerkarte Standardoptionen]]

- wähle zwischen

  - **Gesamte Datenbank** (Standardeinstellung)
  - 'Nachkommen von <Aktive Person>'
  - 'Nachkommenfamilien von <Aktive Person>'
  - 'Vorfahren von <Aktive Person>'
  - 'Personen mit gemeinsamen Vorfahren mit <Aktive Person>'

- Die zentrale Person für den Bericht ist normalerweise die aktive Person, es sei denn, du verwendest die :

  - Schaltfläche zur Verwendung des Auswahldialogfeld.

- (`Mein Kalender` Standardeinstellung) Erste Textzeile unten im Kalender.

- (`Erstellt mit Gramps` Standardeinstellung) Zweite Textzeile unten im Kalender.

- ([`http://gramps-project.org/`](http://gramps-project.org/) Standardeinstellung) Dritte Textzeile unten im Kalender.

{{-}}

#### Berichtsoptionen (2)

![[_media/Calendar-GraphicalReports-ReportOptions2-tab-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Kalender - Grafische Berichte - Berichtsoptionen (2) - Registerkarte Standardoptionen]]

- Wähle das Format für die Anzeige der Namen: wähle zwischen

  - **Nachname, Vorname Suffix** (Standardeinstellung)
  - *Vorname Nachname Suffix*
  - *Vorname*
  - *Haupt Nachnamen, Vorname Patronymikon Suffix*
  - *NACHNAME, Vorname (Üblich)*

-  (Kontrollkästchen standardmäßig aktiviert)

-  (Kontrollkästchen standardmäßig aktiviert)

- Die Übersetzung, die für den Bericht verwendet wird. Zeigt die Sprachauswahl

{{-}}

#### Inhalt

![[_media/Calendar-GraphicalReports-Content-tab-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Kalender - Grafische Berichte - Inhalt - Registerkarte Standardoptionen]]

- Gib das Jahr ein. Standardmäßig das aktuelle Jahr.

- Wähle das Land aus, um die zugehörigen Feiertage anzuzeigen. Vorgabe ist keins. Siehe Beispiel: [Calendar tools holidays](wiki:Calendar_tools_holidays)

- (Standardeinstellung: **Montag**) Wähle den ersten Tag der Woche für den Bericht aus.

- Wähle den angezeigten Nachnamen der verheirateten Frauen aus.

  - **Frauen benutzen ihren Mädchennamen** (Standardeinstellung)
  - *Frauen benutzen den Nachnamen vom Mann (von der ersten gelisteten Familie)*
  - *Frauen benutzen den Nachnamen vom Mann (von der letzten gelisteten Familie)*

-  Geburtstage in den Kalender aufnehmen oder nicht (Kontrollkästchen standardmäßig aktiviert)

-  Jahrestage in den Kalender aufnehmen oder nicht (Kontrollkästchen standardmäßig aktiviert)

-  Todestage in den Kalender aufnehmen oder nicht (Kontrollkästchen standardmäßig deaktiviert)

{{-}}

### <u>Nachkommenbaum</u>

![[_media/GraphicalReports-DescendantTree-example-portrait-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Nachkommenbaum - Grafische Berichte - Beispielausgabe Übersicht]]

Der Bericht erstellt ein Diagramm mit Personen, die Nachkommen der aktiven Person sind. Alternativ kann es ein Diagramm der Nachkommen der Eltern der aktiven Person erstellen.

Du kannst den -Bericht über auswählen. {{-}} Siehe auch [gemeinsame Optionen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte_-_Teil_4#Gemeinsame_Optionen) {{-}}

#### Baumoptionen

![[_media/DescendantTree-GraphicalReports-TreeOptions-tab-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Nachkommenbaum - Grafische Berichte - Baumoptionen - Registerkarte Standardoptionen]]

- Die Hauptperson für den Bericht. Standardmäßig ist dies die aktive Person.

  - Schaltfläche. - Ändert die Hauptperson.

- (`10` standardmäßig). Die Anzahl der Generationen, die in den Stammbaum aufgenommen werden sollen (einschließlich der Hauptperson). Hinweis: Das Diagramm enthält eine weitere Generation, wenn ausgewählt ist.

gibt an, wie tief die Partner angezeigt werden sollen. (`1` Voreinstellung)

-  Zeigt die Eltern, Brüder und Schwestern der ausgewählten Person an. (Standardmäßig ist das Kontrollkästchen deaktiviert)

-  Ob Personen nach Möglichkeit nach oben verschoben werden sollen, was zu einem kleineren Baum führt (standardmäßig nicht aktiviert)

-  Legt fest, ob Personen, die direkte Nachkommen (keine Stief- oder Halbnachkommen) sind, fett markiert werden sollen. (Kontrollkästchen standardmäßig aktiviert)

-  Ob die Ehegatten im Stammbaum eingerückt werden sollen (Kontrollkästchen standardmäßig aktiviert).

{{-}}

#### Berichtsoptionen

![[_media/DescendantTree-GraphicalReports-ReportOptions-tab-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Nachkommenbaum - Grafische Berichte - Berichtsoptionen - Registerkarte Standardoptionen]]

- wähle einen Titels für den Bericht. Optionen sind:

  - **Keinen Titel einfügen** (Vorgabe)
  - *Nachfahrentafel für \[ausgewählte Person(en)\]* (Hinweis: Wenn auf der Registerkarte das Kontrollkästchen aktiviert ist, werden beide Eltern der ausgewählten Person angezeigt. Im Titel werden dann nur zwei Personen aufgeführt. Wenn zwei oder mehr ist, werden die Nachkommen der „Partner der Partner“ in das Diagramm aufgenommen, aber nicht im Titel aufgeführt.)

- Ob ein Rahmen um den Bericht gezogen werden soll. (Kontrollkästchen ist standardmäßig deaktiviert)

- Ob die Seitenzahlen auf jeder Seite angegeben werden sollen. (Kontrollkästchen ist standardmäßig deaktiviert)

- Skalierung des Baums (Vergrößerung oder Verkleinerung des Baums) zur Anpassung an eine bestimmte Papiergröße. Die Optionen sind:

  - **Baum nicht skalieren** (Vorgabe)
  - *Baum nur auf Seitenbreite skalieren*
  - *Baum auf Seitengröße anpassen*

-  (standardmäßig deaktiviert) macht die Seite größer oder kleiner, damit sie zum Baum passt. Bei Auswahl mit werden die Optionen in dieser Reihenfolge ausgeführt; zuerst den Baum skalieren, dann die Seite. Es gibt einen kombinierten Effekt mit jeder Option:

1.  Mit "Baum nicht skalieren" wird sowohl die Seitenbreite als auch die Seitenhöhe an den Baum angepasst.
2.  Mit "Baum nur auf Seitenbreite skalieren" wird die Seitenhöhe an die Baumhöhe angepasst.
3.  Mit "Baum auf Seitengröße skalieren" wird die Seitengröße angepasst, um Lücken in Höhe und Breite zu entfernen.

-  Ob leere Seiten einbezogen werden sollen. (Kontrollkästchen standardmäßig aktiviert)

Die Optionen und (Hinweis: Übersteuert die Optionen auf der Registerkarte Papieroptionen) werden besser unter \[De:Gramps_6.0_Wiki_Handbuch\_-\_Berichte\_-\_Teil_4#Gemeinsame_Optionen\|Gemeinsame Optionen\]\] mit Tipps zur Erstellung schöner Berichte beschrieben. {{-}}

#### Berichtsoptionen (2)

![[_media/DescendantTree-GraphicalReports-ReportOptions2-tab-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Nachkommenbaum - Grafische Berichte - Berichtsoptionen (2) - Registerkarte Standardoptionen]]

- Wähle das Format aus, um die Namen anzuzeigen. Wähle aus:

  - Vorgabe - (in einem neuen Stammbaum ist dies normalerweise *Nachname, Vorname Suffix*)
  - **Nachname, Vorname Suffix** (Standardeinstellung)
  - *Vorname Nachname Suffix*
  - *Vorname*
  - *Haupt Nachnamen, Vorname Patronymikon Suffix*
  - *NACHNAME, Vorname (Üblich)*

-  Ob ein vertrauliche Daten aufgenommen werden sollen (Kontrollkästchen standardmäßig aktiviert)

- Wie lebende Personen behandelt werden. Wähle aus:

  - **Aufnehmen und alle Daten** (Vorgabe)
  - *Vollständige Namen, aber Daten entfernt*
  - *Vornamen ersetzt und Daten entfernt*
  - *Kompletter Name ersetzt und Daten entfernt*
  - *Nicht enthalten*

- Ob Daten über kürzlich verstorbene Personen eingeschränkt werden sollen. Wähle die Anzahl der Jahre seit dem Tod aus, um Personen für den Bericht zu berücksichtigen. Ermöglicht die Aufnahme oder den Ausschluss kürzlich verstorbener Personen in den Bericht. Der (Standardwert ist `0` Jahre.)

- Die Übersetzung, die für den Bericht verwendet wird. Standardmäßig die Sprache, in der du Gramps verwendest

- Format und Sprache für Datumsangaben mit Beispielen

  - Vorgabe - Wähle diese Option, um den Standardsatz in [Bearbeiten &gt; Registerkarte Anzeige](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Einstellungen#Anzeige) für die Option zu verwenden.
  - **JJJJ-MM-TT (ISO) (2018-04-08)** (Vorgabe)
  - *Numerisch (8.4.2018)*
  - *Monat Tag, Jahr (April 8. 2018)*
  - *MONAT Tag, Jahr (Apr 8. 2018)*
  - *Tag Monat Jahr (8. April 2018)*
  - *Tag MONAT Jahr (8. Apr 2018)*

{{-}}

#### Anzeige

![[_media/DescendantTree-GraphicalReports-Display-tab-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Nachkommenbaum - Grafische Berichte - Anzeige - Registerkarte Standardoptionen]]

- setzt das Anzeigeformat für alle Nachkommen in dem Baum. Der Standard ist:

<!-- -->

    $n
    * $b
    -{† $d}

welcher den Namen, Geburtsdatum und Todesdatum in aufeinander folgenden Zeilen im Format aus dem Anzeigenreiter der Gramps Einstellungen ausgibt. Die {} in der dritten Zeile bewirken, das der Text '†' NUR ausgegeben wird, wenn \$d einen Wert enthält z.B. es steht etwas im Todesdatumsfeld in der Datenbank. Siehe [Werte ersetzen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte_-_Teil_2) für mehr Informationen inklusive die Aufnahme von Orten und Attributen und verschiedene Formatierungen von Namen, Daten und Orten.

Das Kontrollkästchen bewirkt die Namen und andere Informationen über direkte Nachkommen in fetter Schrift aus dem Stileditor ausgegeben werden.

- bestimmt was für jeden Partner angezeigt wird. Der Standard ist der selbe wie für die Nachkommen. Wenn du keine eigene Box für die Hochzeitsinformationen haben möchtest, können sie in der Partnerbox angegeben werden, zum Beispiel durch Hinzufügen einer Zeile mit

<!-- -->

    m. $m

was das Datum der Hochzeit anzeigt

rückt die Partner- und Hochzeitsboxen gegenüber den Nachkommenboxen ein. Es hat keine Auswirkung auf die Startfamilie oder die Eltern der Startfamilie aber auf alle anderen Partner dieser drei Paare im Nachkommendiagram.

- (Kontrollkästchen standardmäßig aktiviert) zeigt ein extra Kästchen im Baum für jede Hochzeit. Das Anzeigeformat für dieses Kästchen wird im eingestellt. Der Standardwert ist

<!-- -->

    m. $m

was das Datum der Hochzeit anzeigt. Wenn dieses Kästchen nicht aktiviert ist, werden Hochzeitsinformationen nicht angezeigt bis du sie du sie im wie oben beschrieben angibst.

{{-}}

#### Erweitert

![[_media/DescendantTree-GraphicalReports-Advanced-tab-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Nachkommenbaum - Grafische Berichte - Erweitert - Registerkarte Standardoptionen]]

- Auf diese Weise kannst du durch '`/`' getrennte Zeichenfolgenpaare einfügen, die den Text angeben, den du durch anderen Text ersetzen möchtest. Beispiel: `Vereinigte Staaten von Amerika/USA` ersetzt die Vereinigten Staaten von Amerika durch USA. Die Breite jeder Spalte wird durch das breiteste Feld im Bericht bestimmt. Wenn also ein Feld viel breiter ist als die anderen, wird viel Platz verschwendet. Mit der Option „Zeichenfolge ersetzen“ kannst du Teile der Zeichenfolge entfernen oder abkürzen, die nicht benötigt werden oder gekürzt werden können, so dass nur wenig Platz verschwendet wird.

  -  Du kannst das Kontrollkästchen Notiz einschließen aktivieren, um eine Notiz hinzuzufügen (das Kontrollkästchen ist standardmäßig deaktiviert).

- gibt den Text an, den die Notiz enthalten wird. Wenn du den Ersetzungswert “`$T`” in die Notiz einfügst, wird der Tag angezeigt, an dem der Bericht erstellt wurde. Es gilt die normale Datumsformatierung (siehe [Ersetzungswerte](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte_-_Teil_2)).

- Gib an, wo auf der Seite die Notiz platziert werden soll. Derzeit wird an einer Ecke eine Notiz angebracht. Wenn eine Personenbox darüber schreibt, bewegt sich die Notizbox nicht. Wähle eine andere Option für die Positionierung der Notiz, wenn dies der Fall ist.

  - **Oben links** ( Vorgabe)
  - *Unten links*
  - *Unten rechts*

Die folgenden zwei Optionen werden unter [Größenoptionen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte_-_Teil_4#Optionen_zum_Skalieren_und_Gr.C3.B6.C3.9Fe_.C3.84ndern) mit Tipps zum Erstellen schönerer Berichte besser beschrieben.

- Macht den Kästchenabstand größer oder kleiner (Standardeinstellung ist `1.00` in.).

- Macht den Kästchenschatten größer oder kleiner (Standardeinstellung ist `1.00` in.).

{{-}}

#### Beispiele

![[_media/Descendant_tree_example1.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Nachkommenbaumbericht, Beispiel 1. Allan Davies hatte drei Ehefrauen.]]

![[_media/Descendant_tree_example2.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Nachkommenbaumbericht, Beispiel 2.]]

{{-}} Das folgende Beispiel basiert auf der gleichen Familie wie das erste Beispiel und zeigt das Ergebnis, wenn man mit „Kind 2 Davies“ beginnt und dieses Kästchen ankreuzt.

{{-}} Beispiel 1 wurde durch Auswahl von Allan Davies als Ausgangsperson und anschließende Ausführung des Berichts ohne Ankreuzen dieses Kästchens erhalten, wobei alle anderen Optionen mit Ausnahme der unverändert blieben. Die Unterschiede zwischen den beiden Beispielen sind:

- Das Format der ersten Generation ist geändert. Da die Eltern der Ausgangsperson nebeneinander liegen müssen, werden die Ehegatten in der ersten Generation möglicherweise nicht in der richtigen Reihenfolge angezeigt.
- Für die Einstellung der werden beide Eltern als direkte Nachkommen und nicht als Ehegatten betrachtet. (Obwohl die Mutter das auf der Registerkarte Anzeige verwendet).

Das bedeutet, dass andere Ehegatten (falls vorhanden) der beiden auf der durch festgelegten Anzahl von Ebenen angezeigt werden. In Beispiel 2 wird Mike Morris angezeigt, obwohl die auf 1 eingestellt ist.

- Der Titel des Berichts (falls auf der Registerkarte Einschließen ausgewählt) wird so geändert, dass beide Elternteile der Ausgangsperson enthalten sind. Es werden nur zwei Personen im Titel angezeigt. In Beispiel 2 wird Mike Morris nicht im Titel aufgeführt, obwohl seine Nachkommen angezeigt werden.

Die Anzahl der Generationen, die in dem Bericht angezeigt werden sollen (einschließlich der Ausgangsperson). Wenn ausgewählt ist, enthält das Diagramm eine Generation. (Beispiel 1 wurde mit =3 ausgeführt, Beispiel 2 mit =2.)

gibt an, wie tief die Ehegatten angezeigt werden sollen.

Für das Beispiel:

- Abe ist ein direkter Nachkomme
  - Abe hat/hatte Barbra geheiratet und hatte zwei Kinder
  - Abe heiratete auch Bridget und hatte ein Kind
    - Bridget hat/hatte Carl geheiratet.
      - Carl und Denise hatten ein Kind.

Im obigen Beispiel wird für die ersten drei Optionen Folgendes angezeigt.

- 0 bedeutet, dass nur direkte Nachkommen angezeigt werden. Auf der Registerkarte „Sekundär“ wird nichts angezeigt (Informationen zum Ehepartner oder Informationen zur Ehe). Im obigen Beispiel wird nur Abe mit drei Kindern direkt unter ihm angezeigt.
- 1 bedeutet, dass nur die Ehepartner der direkten Nachkommen angezeigt werden. Für das obige Beispiel wird Abe mit zwei Heiratsinformationen angezeigt. Unter der ersten werden zwei Kinder und unter der zweiten ein Kind angezeigt.
- 2 bedeutet, dass die Ehegatten der Ehegatten angezeigt werden. Dasselbe wie bei 1, aber bei Bridget wird auch ihre andere Ehe angezeigt. Wenn sie Kinder hatten, werden diese ebenfalls angezeigt.
- 3 bedeutet, dass alle Personen aus dem obigen Beispiel angezeigt werden.

Jede Option über 1 ist im Bericht ohne die Option auf der Registerkarte Anzeige sehr schwer zu lesen.

Zu guter Letzt gibt es noch die Option , mit der versucht wird, jeden so weit wie möglich nach oben zu verschieben (komprimieren) und trotzdem einen lesbaren Bericht zu erhalten. Wenn angekreuzt ist, hat keine Auswirkungen auf die erste Generation. {{-}}

#### Beispiele 1 oder 2

....

(`10` Vorgabe). Die Anzahl der Generationen, die im Diagramm angezeigt werden sollen (einschließlich der Ausgangsperson). Wenn ausgewählt wird, enthält das Diagramm eine weitere Generation. (Beispiel 1 wurde mit =3 ausgeführt, Beispiel 2 mit =2).

gibt an, wie tief die Ehegatten angezeigt werden sollen.

, um ein Abstammungsdiagramm von den Eltern der Ausgangsperson zu erstellen, sofern diese in der Datenbank vorhanden sind. Das [Beispiel](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte_-_Teil_4#Beispiele) basiert auf derselben Familie wie das erste Beispiel und zeigt das Ergebnis, wenn man mit „Kind 2 Davies“ beginnt und dieses Kästchen ankreuzt.

{{-}} Beispiel 1 wurde durch Auswahl von Allan Davies als Ausgangsperson und anschließende Ausführung des Berichts ohne Ankreuzen dieses Kästchens erzielt, wobei alle anderen Optionen mit Ausnahme der gleich geblieben sind. Die Unterschiede zwischen den beiden Beispielen sind:

- Das Format der ersten Generation ist geändert. Da die Eltern der Ausgangsperson nebeneinander liegen müssen, werden die Ehegatten in der ersten Generation möglicherweise nicht in der richtigen Reihenfolge angezeigt.
- Für die Einstellung der werden beide Eltern als direkte Nachkommen und nicht als Ehegatten betrachtet. (Obwohl die Mutter das auf der Registerkarte Anzeige verwendet).

Das bedeutet, dass andere Ehegatten (falls vorhanden) der beiden angezeigt werden durch die Anzahl der Ebenen festgelegt durch . In Beispiel 2 wird Mike Morris angezeigt, obwohl die auf 1 eingestellt ist.

- Der Titel des Berichts (falls auf der Registerkarte Einschließen ausgewählt) wird so geändert, dass er beide Elternteile der Ausgangsperson enthält. Es werden nur zwei Personen im Titel angezeigt. In Beispiel 2 wird Mike Morris nicht im Titel aufgeführt, obwohl seine Nachkommen angezeigt werden.

Für das Beispiel:

- Abe ist ein direkter Nachkomme
  - Abe hat/hatte Barbra geheiratet und hatte zwei Kinder
  - Abe heiratete auch Bridget und hatte ein Kind
    - Bridget hat/hatte Carl geheiratet.
      - Carl und Denise hatten ein Kind.

Im obigen Beispiel wird für die ersten drei Optionen Folgendes angezeigt.

- 0 bedeutet, dass nur direkte Nachkommen angezeigt werden. Auf der Registerkarte „Sekundär“ wird nichts angezeigt (Informationen zum Ehepartner oder Informationen zur Ehe). Im obigen Beispiel wird nur Abe mit drei Kindern direkt unter ihm angezeigt.
- 1 bedeutet, dass nur die Ehepartner der direkten Nachkommen angezeigt werden. Für das obige Beispiel wird Abe mit zwei Heiratsinformationen angezeigt. Unter der ersten werden zwei Kinder und unter der zweiten ein Kind angezeigt.
- 2 bedeutet, dass die Ehegatten der Ehegatten angezeigt werden. Dasselbe wie bei 1, aber bei Bridget wird auch ihre andere Ehe angezeigt. Wenn sie Kinder hatten, werden diese ebenfalls angezeigt.
- 3 bedeutet, dass alle Personen aus dem obigen Beispiel angezeigt werden.

Jede Option über 1 ist im Bericht ohne die Option auf der Registerkarte Anzeige sehr schwer zu lesen.

Zu guter Letzt gibt es noch die Option , mit der versucht wird, jeden so weit wie möglich nach oben zu verschieben (komprimieren) und trotzdem einen lesbaren Bericht zu erhalten. Wenn angekreuzt ist, hat keine Auswirkungen auf die erste Generation. {{-}}

### <u>Familienachkommenbaum</u>

![[_media/GraphicalReports-FamilyDescendantTree-example-portrait-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Familienachkommenbaum - Grafische Berichte - Beispielausgabe Übersicht]]

Der Bericht erstellt ein Diagramm der Personen, die Nachkommen der aktiven Familie sind.

Du kannst den Bericht zum Stammbaum der Familie über auswählen. {{-}} Siehe auch [gemeinsame Optionen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte_-_Teil_4#Gemeinsame_Optionen) {{-}}

#### Baumoptionen

![[_media/FamilyDescendantTree-GraphicalReports-TreeOptions-tab-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Familienachkommenbaum - Grafische Berichte - Baumoptionen - Registerkarte Standardoptionen]]

- Die Hauptperson für den Bericht. Standardmäßig ist dies die aktive Person.

  - Schaltfläche. - Ändert die Hauptperson.

(`10` Vorgabe). gibt an, wie tief Ehepartner angezeigt werden sollen. (`1` Vorgabe)

-  Zeigt die Eltern, Brüder und Schwestern der ausgewählten Person an. (Standardmäßig ist das Kontrollkästchen deaktiviert)

-  Ob Personen nach Möglichkeit nach oben verschoben werden sollen, was zu einem kleineren Baum führt (standardmäßig nicht aktiviert)

-  Legt fest, ob Personen, die direkte Nachkommen (keine Stief- oder Halbnachkommen) sind, fett markiert werden sollen. (Kontrollkästchen standardmäßig aktiviert)

-  Ob die Ehegatten im Stammbaum eingerückt werden sollen (Kontrollkästchen standardmäßig aktiviert).

{{-}} Wenn das Kontrollkästchen aktiviert ist, zeigt der Bericht beide Elternteile des Startvaters und der Startmutter (sofern sie in der Datenbank vorhanden sind) sowie alle Nachkommen beider Elternpaare für die ausgewählte Anzahl von Generationen. Die Gesamtzahl der Generationen im Diagramm ist also um 1 höher als die im Feld Generationen ausgewählte Anzahl. (Das obige Beispieldiagramm wurde mit Generationen=2 erstellt).

Der Startvater und die Startmutter müssen sich in der Mitte des Diagramms befinden.

Sie werden daher nicht in der Reihenfolge der Geburt mit ihren Geschwistern angezeigt, sondern als letztes bzw. erstes Kind ihrer Eltern. Dies wird in dem Dies wird in dem [Beispieldiagramm](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte_-_Teil_4#Beispiele) gezeigt, in dem die Kinder in beiden Familien gezeigt, in dem die Kinder in beiden Familien

in ihrer Geburtsreihenfolge als Kind 1,2,3 bezeichnet wurden. Wenn der Startvater oder die Startmutter noch andere Ehepartner haben, werden sie doppelt aufgeführt. Dies gilt auch für die Eltern des Startvaters oder der Startmutter.

Wenn dieses Kästchen nicht angekreuzt ist, ist der Bericht derselbe wie der Nachkommenschaftsbericht, außer dass die Anzahl der Generationen um eine erhöht wird, das Format der ersten Generation anders ist und du zusätzliche Optionen für den Titel der Tabelle erhältst. {{-}}

#### Berichtsoptionen

![[_media/FamilyDescendantTree-GraphicalReports-ReportOptions-tab-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Familienachkommenbaum - Grafische Berichte - Berichtsoptionen - Registerkarte Standardoptionen]]

- wähle einen Titels für den Bericht. Optionen sind:

  - **Ohne Titel** (Vorgabe)
  - *Nachfahrentafel für \[gewählte Person(en)\]* (Hinweis: Wenn auf der Registerkarte das Kontrollkästchen aktiviert ist, werden beide Eltern der ausgewählten Person angezeigt. Im Titel werden dann nur zwei Personen aufgeführt. Wenn zwei oder mehr ist, werden die Nachkommen der „ Partner der Partner“ im Diagramm angezeigt, aber nicht im Titel aufgeführt.)

- Ob ein Rahmen um den Bericht gezogen werden soll. (Kontrollkästchen ist standardmäßig deaktiviert)

- Ob die Seitenzahlen auf jeder Seite angegeben werden sollen. (Kontrollkästchen ist standardmäßig deaktiviert)

- Skalierung des Baums (Vergrößerung oder Verkleinerung des Baums) zur Anpassung an eine bestimmte Papiergröße. Die Optionen sind:

  - **Baum nicht skalieren** (Vorgabe)
  - *Baum nur auf Seitenbreite skalieren*
  - *Baum auf Seitengröße anpassen*

-  (standardmäßig deaktiviert) macht die Seite größer oder kleiner, damit sie zum Baum passt. Bei Auswahl mit werden die Optionen in dieser Reihenfolge ausgeführt; zuerst den Baum skalieren, dann die Seite. Es gibt einen kombinierten Effekt mit jeder Option:

1.  Mit "Baum nicht skalieren" wird sowohl die Seitenbreite als auch die Seitenhöhe an den Baum angepasst.
2.  Mit "Baum nur auf Seitenbreite skalieren" wird die Seitenhöhe an die Baumhöhe angepasst.
3.  Mit "Baum auf Seitengröße skalieren" wird die Seitengröße angepasst, um Lücken in Höhe und Breite zu entfernen.

-  Ob leere Seiten einbezogen werden sollen. (Kontrollkästchen standardmäßig aktiviert)

Die Optionen und (Hinweis: Übersteuert die Optionen auf der Registerkarte Papieroptionen) werden besser unter [Gemeinsame Optionen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte_-_Teil_4#Gemeinsame_Optionen) mit Tipps zur Erstellung schöner Berichte beschrieben. {{-}}

#### Berichtsoptionen (2)

![[_media/FamilyDescendantTree-GraphicalReports-ReportOptions2-tab-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Familienachkommenbaum - Grafische Berichte - Berichtsoptionen (2) - Registerkarte Standardoptionen]]

- Wähle das Format aus, um die Namen anzuzeigen. Diese Auswahl wird normalerweise von der Standardeinstellung in [Bearbeiten &gt; Registerkarte Anzeige](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Einstellungen#Anzeige) für Namensformat übernommen:. Oder wähle eine der folgenden Optionen, um diese Einstellung für den Bericht zu überschreiben:

  - Vorgabe - (in einem neuen Stammbaum ist dies normalerweise *Nachname, Vorname Suffix*)
  - **Nachname, Vorname Suffix** (Vorgabe)
  - *Vorname Nachname Suffix*
  - *Vorname*
  - *Haupt Nachnamen, Vorname Patronymikon Suffix*
  - *NACHNAME, Vorname (Üblich)*

-  Ob ein vertrauliche Daten aufgenommen werden sollen (Kontrollkästchen standardmäßig aktiviert)

- Wie lebende Personen behandelt werden. Wähle aus:

  - **Aufnehmen und alle Daten** (Vorgabe)
  - *Vollständige Namen, aber Daten entfernt*
  - *Vornamen ersetzt und Daten entfernt*
  - *Kompletter Name ersetzt und Daten entfernt*
  - *Nicht enthalten*

- Ob Daten über kürzlich verstorbene Personen eingeschränkt werden sollen. Wähle die Anzahl der Jahre seit dem Tod aus, um Personen für den Bericht zu berücksichtigen. Ermöglicht die Aufnahme oder den Ausschluss kürzlich verstorbener Personen in den Bericht. Der (Standardwert ist `0` Jahre.)

- Die Übersetzung, die für den Bericht verwendet wird.

  - Sprachauswahl

- Format und Sprache für Datumsangaben mit Beispielen

  - Vorgabe - Wähle diese Option, um den Standardsatz in [Bearbeiten &gt; Registerkarte Anzeige](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Einstellungen#Anzeige) für die Option zu verwenden.
  - **JJJJ-MM-TT (ISO) (2018-04-08)** (Vorgabe)
  - *Numerisch (8.4.2018)*
  - *Monat Tag, Jahr (April 8. 2018)*
  - *MONAT Tag, Jahr (Apr 8. 2018)*
  - *Tag Monat Jahr (8. April 2018)*
  - *Tag MONAT Jahr (8. Apr 2018)*

{{-}}

#### Anzeige

![[_media/FamilyDescendantTree-GraphicalReports-Display-tab-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Familienachkommenbaum - Grafische Berichte - Anzeige - Registerkarte Standardoptionen]]

setzt das Anzeigeformat für alle Nachkommen in dem Baum. Der Standard ist:

    $n
    * $b
    -{† $d}

welcher den Namen, Geburtsdatum und Todesdatum in aufeinander folgenden Zeilen im Format aus dem Anzeigenreiter der Gramps Einstellungen ausgibt. Die {} in der dritten Zeile bewirken, das der Text '†' NUR ausgegeben wird, wenn \$d einen Wert enthält z.B. es steht etwas im Todesdatumsfeld in der Datenbank. Siehe [Werte ersetzen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte_-_Teil_2) für mehr Informationen inklusive die Aufnahme von Orten und Attributen und verschiedene Formatierungen von Namen, Daten und Orten.

Das Kontrollkästchen bewirkt die Namen und andere Informationen über direkte Nachkommen in fetter Schrift aus dem Stileditor ausgegeben werden.

bestimmt was für jeden Partner angezeigt wird. Der Standard ist der selbe wie für die Nachkommen. Wenn du keine eigene Box für die Hochzeitsinformationen haben möchtest, können sie in der Partnerbox angegeben werden, zum Beispiel durch Hinzufügen einer Zeile mit

    m. $m

was das Datum der Hochzeit anzeigt

rückt die Partner- und Hochzeitsboxen gegenüber den Nachkommenboxen ein. Es hat keine Auswirkung auf die Startfamilie oder die Eltern der Startfamilie aber auf alle anderen Partner dieser drei Paare im Nachkommendiagram.

zeigt ein extra Kästchen im Baum für jede Hochzeit. Das Anzeigeformat für dieses Kästchen wird im eingestellt. Der Standardwert ist

    m. $m

was das Datum der Hochzeit anzeigt. Wenn dieses Kästchen nicht aktiviert ist, werden Hochzeitsinformationen nicht angezeigt bis du sie du sie im wie oben beschrieben angibst.

{{-}}

#### Erweitert

![[_media/FamilyDescendantTree-GraphicalReports-Advanced-tab-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Familienachkommenbaum - Grafische Berichte - Erweitert - Registerkarte Standardoptionen]]

- Auf diese Weise kannst du durch '`/`' getrennte Zeichenfolgenpaare einfügen, die den Text angeben, den du durch anderen Text ersetzen möchtest. Beispiel: `Vereinigte Staaten von Amerika/USA` ersetzt die Vereinigten Staaten von Amerika durch USA. Die Breite jeder Spalte wird durch das breiteste Feld im Bericht bestimmt. Wenn also ein Feld viel breiter ist als die anderen, wird viel Platz verschwendet. Mit der Option „Zeichenfolge ersetzen“ kannst du Teile der Zeichenfolge entfernen oder abkürzen, die nicht benötigt werden oder gekürzt werden können, so dass nur wenig Platz verschwendet wird.

  -  Du kannst das Kontrollkästchen Notiz einschließen aktivieren, um eine Notiz hinzuzufügen (das Kontrollkästchen ist standardmäßig deaktiviert).

- gibt den Text an, den die Notiz enthalten wird. Wenn du den Ersetzungswert “`$T`” in die Notiz einfügst, wird der Tag angezeigt, an dem der Bericht erstellt wurde. Es gilt die normale Datumsformatierung (siehe [Ersetzungswerte](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte_-_Teil_2)).

- Gib an, wo auf der Seite die Notiz platziert werden soll. Derzeit wird an einer Ecke eine Notiz angebracht. Wenn eine Personenbox darüber schreibt, bewegt sich die Notizbox nicht. Wähle eine andere Option für die Positionierung der Notiz, wenn dies der Fall ist.

  - **Oben links** (Vorgabe)
  - *Unten links*
  - *Unten rechts*

Die folgenden zwei Optionen werden unter [Größenoptionen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte_-_Teil_4#Optionen_zum_Skalieren_und_Gr.C3.B6.C3.9Fe_.C3.84ndern) mit Tipps zum Erstellen schönerer Berichte besser beschrieben.

- Macht den Kästchenabstand größer oder kleiner (Standardeinstellung ist `1.00` in.).

- Macht den Kästchenschatten größer oder kleiner (Standardeinstellung ist `1.00` in.).

{{-}}

### <u>Fächerdiagramm</u>

![[_media/GraphicalReports-FanChart-example-landscape-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Fächergrafik - Grafische Berichte - Beispielausgabe Übersicht]]

Die zeigt kompakt die Vorfahren väterlicherseits und mütterlicherseits. Der Bericht erstellt ein Diagramm, das die familiären Beziehungen in einer Baumstruktur darstellt, die einem Fächer (Halbkreis) und wahlweise einem Viertel- oder Vollkreis ähnelt, mit der Aktiven Person im inneren Kreis (Zentrum), den Eltern im zweiten konzentrischen Kreis, der in zwei geteilt ist (jede Seite ist ein Elternteil), dem dritten Kreis, der in vier geteilt ist und die Großeltern darstellt, und so weiter, für maximal elf Generationen.

Dieses Diagramm wird auch als *Stammbaum-Fächerdiagramm* bezeichnet.

Du kannst den Fächergrafik über auswählen. {{-}} Siehe auch [gemeinsame Optionen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte_-_Teil_4#Gemeinsame_Optionen) {{-}}

#### Berichtsoptionen

![[_media/FanChart-GraphicalReports-ReportOptions-tab-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Fächergrafik - Grafische Berichte - Berichtsoptionen - Registerkarte Standardoptionen]]

- Die zentrale Person für den Bericht. Standardmäßig ist dies die aktive Person.

  - Schaltfläche. - Ändert die Hauptperson.

- (`5` Standardeinstellung) Die Anzahl der im Bericht enthaltenen Generationen. (Bis maximal `11` Generationenenerations)

- Die Gestalt der Grafik.

  - *Vollkreis*
  - **Halbkreis**(Vorgabe)
  - *Überhang* (Halbkreis mit Überhang)
  - *Viertelkreis*

- wähle aus:

  - *Weiß*
  - **von der Generation abhängig**(Vorgabe).

- wähle aus:

  - **aufrecht**(Vorgabe)
  - *umlaufend*

-  Zeichne den Hintergrund obwohl keine Informationen vorliegen (Kontrollkästchen standardmäßig aktiviert)

-  Du kannst die Schrift und Farbe für jede Generation im Stileditor anpassen

-  : Namen umdrehen für die Generationen 2, 3 und 4, d.h. die in den Kreisen gefundenen (Kontrollkästchen standardmäßig aktiviert)

-  : um mehr Platz für das Diagramm zu schaffen (Kontrollkästchen standardmäßig deaktiviert)

{{-}}

#### Berichtsoptionen (2)

![[_media/FanChart-GraphicalReports-ReportOptions2-tab-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Fächergrafik - Grafische Berichte - Berichtsoptionen (2) - Registerkarte Standardoptionen]]

-  (Kontrollkästchen standardmäßig aktiviert)

- Wie lebende Personen behandelt werden. Wähle aus:

  - **Aufnehmen und alle Daten** (Vorgabe)
  - *Vollständige Namen, aber Daten entfernt*
  - *Vornamen ersetzt und Daten entfernt*
  - *Kompletter Name ersetzt und Daten entfernt*
  - *Nicht enthalten*

- Ob Daten über kürzlich verstorbene Personen eingeschränkt werden sollen. Wähle die Anzahl der Jahre seit dem Tod aus, um Personen für den Bericht zu berücksichtigen. Ermöglicht die Aufnahme oder den Ausschluss kürzlich verstorbener Personen in den Bericht. Der (Standardwert ist `0` Jahre.)

- Die Übersetzung, die für den Bericht verwendet wird. Standardmäßig die Sprache, in der du Gramps verwendest

  - Sprachauswahl

{{-}}

### <u>Statistikdiagramme</u>

Der Bericht zeigt statistische Daten über deinen Stammbaum in Form von drei Diagrammen für *Geburtsmonat*, *Anzahl der Kinder* und *Geschlechts*-statistiken.

Du kannst den Statistikdiagrammbericht mit auswählen.

Zu den spezifischen Optionen gehören Filter, Sortiermethoden und zusätzliche geburts- und geschlechtsspezifische Grenzen für die Aufnahme in die Statistik. Du kannst auch die Mindestanzahl von Elementen festlegen, um sich für das Balkendiagramm zu qualifizieren, sodass die Diagramme mit weniger Elementen stattdessen ein Kreisdiagramm generieren. Auf den Registerkarten , und kannst du auswählen, welche zusätzlichen Informationen in jedes einzelne Diagramm deines Berichts aufgenommen werden sollen.

<div>

- ![[_media/GraphicalReports-StatisticsCharts-Chart1-example-portrait-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Diagramm 1 (Geburtsmonat)]]

- ![[_media/GraphicalReports-StatisticsCharts-Chart3-example-portrait-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Chart 2 (Number of children) -]]

- ![[_media/GraphicalReports-StatisticsCharts-Chart3-Gender-example-portrait-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Chart 3 (Gender)]]

</div>

{{-}} Siehe auch [gemeinsame Optionen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte_-_Teil_4#Gemeinsame_Optionen) {{-}}

#### Berichtsoptionen

![[_media/StatisticsCharts-GraphicalReports-ReportOptions-tab-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Statistikdiagramme - Grafische Berichte - Berichtsoptionen - Registerkarte Standardoptionen]]

- wähle zwischen

  - **Gesamte Datenbank** (Vorgabe)
  - *Nachkommen der aktiven Person*
  - *Nachkommen der aktiven Person und deren Partner*
  - *Vorfahren der aktiven Person*
  - *Personen mit gemeinsamen Vorfahren wie aktive Person*

- die zentrale Person für den Filter. Standardmäßig ist dies die aktive Person.

  - Schaltfläche. - Ändert die Hauptperson.

- Wähle wie die Statistikdaten sortiert werden:

  - **Artikelanzahl** (Standardeinstellung)
  - *Artikelname*

-  (Kontrollkästchen standardmäßig deaktiviert)

- (`1700` Standardeinstellung) Geburtsjahr ab dem Personen aufgenommen werden: gib das Anfangsjahr ein

- (`aktuelles Jahr` Standardeinstellung) Geburtsjahr bis zu dem Personen aufgenommen werden: gib das Endjahr ein

-  (Kontrollkästchen standardmäßig deaktiviert)

- Wähle welche Geschlechter in die Statistik aufgenommen werden:

  - **Alle** (Vorgabe)
  - Männer
  - Frauen
  - Divers

- (`8` Standardeinstellung) Bei weniger Elementen wird ein Tortendigramm mit Legende anstatt ein Balkendigramm verwendet.

-  Angabe, ob die Anzahl der Personen, denen die angegebenen Informationen fehlen, erfasst werden soll. (Kontrollkästchen standardmäßig deaktiviert)

{{-}}

#### Berichtsoptionen (2)

![[_media/StatisticsCharts-GraphicalReports-ReportOptions2-tab-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Statistikdiagramme - Grafische Berichte - Berichtsoptionen (2) - Registerkarte Standardoptionen]]

- Wähle das Format aus, um die Namen anzuzeigen.

  - Vorgabe - (in einem neuen Stammbaum ist dies normalerweise *Nachname, Vorname Suffix*)

  - **Nachname, Vorname Suffix** (Vorgabe)

  - *Vorname Nachname Suffix*

  - *Vorname*

  - *Haupt Nachnamen, Vorname Patronymikon Suffix*

  - *NACHNAME, Vorname (Üblich)*

  -  Ob ein vertrauliche Daten aufgenommen werden sollen (Kontrollkästchen standardmäßig aktiviert)

- Wie lebende Personen behandelt werden. Wähle aus:

  - **Aufnehmen und alle Daten** (Vorgabe)
  - *Vollständige Namen, aber Daten entfernt*
  - *Vornamen ersetzt und Daten entfernt*
  - *Kompletter Name ersetzt und Daten entfernt*
  - *Nicht enthalten*

- Ob Daten über kürzlich verstorbene Personen eingeschränkt werden sollen. Wähle die Anzahl der Jahre seit dem Tod aus, um Personen für den Bericht zu berücksichtigen. Ermöglicht die Aufnahme oder den Ausschluss kürzlich verstorbener Personen in den Bericht. Der (Standardwert ist `0` Jahre.)

- Die Übersetzung, die für den Bericht verwendet wird.

  - Sprachauswahl

{{-}}

#### Grafiken 1

![[_media/StatisticsCharts-GraphicalReports-Charts1-tab-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Statistikdiagramme - Grafische Berichte - Grafiken 1 - Registerkarte Standardoptionen]]

Du kannst beliebige der folgenden angegebenen Daten in ein Diagramm aufnehmen:

-  (Kontrollkästchen standardmäßig deaktiviert)

-  (Kontrollkästchen standardmäßig deaktiviert)

-  (Kontrollkästchen standardmäßig deaktiviert)

-  (Kontrollkästchen standardmäßig deaktiviert)

-  (Kontrollkästchen standardmäßig deaktiviert)

-  (Kontrollkästchen standardmäßig deaktiviert)

{{-}}

#### Grafiken 2

![[_media/StatisticsCharts-GraphicalReports-Charts2-tab-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Statistikdiagramme - Grafische Berichte - Grafiken 2 - Registerkarte Standardoptionen]]

Zeigt standardmäßig und Statistiken an und du kannst beliebige der folgenden angegebenen Daten in ein Diagramm aufnehmen:

-  (Kontrollkästchen standardmäßig aktiviert)

-  (Kontrollkästchen standardmäßig deaktiviert)

-  (Kontrollkästchen standardmäßig deaktiviert)

-  (Kontrollkästchen standardmäßig aktiviert)

-  (Kontrollkästchen standardmäßig deaktiviert)

-  (Kontrollkästchen standardmäßig aktiviert)

{{-}}

#### Grafiken 3

![[_media/StatisticsCharts-GraphicalReports-Charts3-tab-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Statistikdiagramme - Grafische Berichte - Grafiken 3 - Registerkarte Standardoptionen]]

Zeigt standardmäßig -Statistiken an und du kannst beliebige der folgenden angegebenen Daten in ein Diagramm aufnehmen:

-  (Kontrollkästchen standardmäßig deaktiviert)

-  (Kontrollkästchen standardmäßig deaktiviert)

-  (Kontrollkästchen standardmäßig deaktiviert)

-  (Kontrollkästchen standardmäßig deaktiviert)

-  (Kontrollkästchen standardmäßig deaktiviert)

-  (Kontrollkästchen standardmäßig deaktiviert)

-  (Kontrollkästchen standardmäßig deaktiviert)

{{-}}

### <u>Zeitleistendiagramm</u>

![[_media/GraphicalReports-TimelineChart-example-landscape-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Zeitliniengrafik - Grafische Berichte - Beispielausgabe Übersicht]]

Der Bericht gibt die Liste der Personen aus, deren Lebenszeit durch Intervalle auf einer gemeinsamen chronologischen Skala dargestellt wird.

Du kannst den -Bericht über auswählen. {{-}} Siehe auch [gemeinsame Optionen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte_-_Teil_4#Gemeinsame_Optionen) {{-}}

#### Berichtsoptionen

![[_media/TimelineChart-GraphicalReports-ReportOptions-tab-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Zeitliniengrafik - Grafische Berichte - Berichtsoptionen - Registerkarte Standardoptionen]]

- wähle zwischen

  - **Gesamte Datenbank** (Vorgabe)
  - *Nachkommen der aktiven Person*
  - *Nachkommen Familien der aktiven Person*
  - *Vorfahren der aktiven Person*
  - *Personen mit gemeinsamen Vorfahren wie aktive Person*

- die zentrale Person für diesen Filter. Standardmäßig ist dies die aktive Person.

  - Schaltfläche. - Ändert die Hauptperson.

- Zu verwendende Sortiermethode.

  - **Geburtsdatum** (Standardeinstellung)
  - *Name*

{{-}}

#### Berichtsoptionen (2)

![[_media/TimelineChart-GraphicalReports-ReportOptions2-tab-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Zeitliniengrafik - Grafische Berichte - Berichtsoptionen (2) - Registerkarte Standardoptionen]]

- Wähle das Format aus, um die Namen anzuzeigen. Diese Auswahl wird normalerweise von der Standardeinstellung in [Bearbeiten &gt; Registerkarte Anzeige](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Einstellungen#Anzeige) für Namensformat übernommen:. Oder wähle eine der folgenden Optionen, um diese Einstellung für den Bericht zu überschreiben:

  - Vorgabe - (in einem neuen Stammbaum ist dies normalerweise *Nachname, Vorname Suffix*)
  - **Nachname, Vorname Suffix** (Standardeinstellung)
  - *Vorname Nachname Suffix*
  - *Vorname*
  - *Haupt Nachnamen, Vorname Patronymikon Suffix*
  - *NACHNAME, Vorname (Üblich)*

- Wie lebende Personen behandelt werden. Wähle aus:

  - **Aufnehmen und alle Daten** (Vorgabe)
  - *Vollständige Namen, aber Daten entfernt*
  - *Vornamen ersetzt und Daten entfernt*
  - *Kompletter Name ersetzt und Daten entfernt*
  - *Nicht enthalten*

- Ob Daten über kürzlich verstorbene Personen eingeschränkt werden sollen. Wähle die Anzahl der Jahre seit dem Tod aus, um Personen für den Bericht zu berücksichtigen. Ermöglicht die Aufnahme oder den Ausschluss kürzlich verstorbener Personen in den Bericht. Der (Standardwert ist `0` Jahre.)

- Die Übersetzung, die für den Bericht verwendet wird. Standardmäßig die Sprache, in der du Gramps verwendest

  - Sprachauswahl

{{-}}

<hr>

Zurück zur [Übersicht der Berichte](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte). {{-}}

[B](wiki:Category:De:Dokumentation) [Category:Plugins](wiki:Category:Plugins)
