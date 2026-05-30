---
title: De:Gramps 6.0 Wiki Handbuch - Berichte - Teil 7
categories:
- De:Dokumentation
- Plugins
- Stub
managed: false
source: wiki-scrape
wiki_revid: 131112
wiki_fetched_at: '2026-05-30T17:38:58Z'
lang: de
---

{{#vardefine:chapter\|13.7}} {{#vardefine:figure\|0}} Zurück zur [Übersicht der Berichte](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte).

<hr>

{{-}} ![[_media/MenuOverview-Reports-WebPages-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}}  Menüübersicht]] Dieser Abschnitt beschreibt die Berichte [Erzählende Website](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte_-_Teil_7#Erz.C3.A4hlende_Website) und [Webkalender](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte_-_Teil_7#Webkalender) als Teil der verschiedenen in Gramps verfügbaren Berichte.

## Webseiten

### <u>Erzählende Website</u>

![[_media/NarratedWebSite-WebPages-Individuals-index-page-example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Erzählende Website - Webseiten - Personen(index)seite - Standard-HTML-Ausgabe - Beispiel]]

Der Bericht generiert eine Website (d.h. eine Reihe verknüpfter Webseiten) für eine Reihe ausgewählter Personen und bietet dem Benutzer Optionen, die eine breite Palette von Anpassungen ermöglichen. Du kannst diesen Bericht über das Menü aufrufen.

Der Bericht Erzählende Website erstellt Seiten, die den Empfehlungen des World Wide Web Consortiums für XHTML 1.0 Strict und CSS 1 genau folgen. Diese Empfehlungen beinhalten eine Trennung von Inhalt und Präsentation. Aufgrund dieser Vorgehensweise können Stil und Aussehen der neuen Webseiten vollständig von einem CSS-Stylesheet aus gesteuert werden, ohne einzelne Seiten zu ändern.

Einführungsseiten können hinzugefügt werden, um zusätzliche Informationen bereitzustellen, z.B. eine Familiengeschichte.

Genealogie-Datensätze können viele Dateien generieren. Viele Webserver haben Schwierigkeiten mit einer großen Anzahl von Dateien in einem einzigen Verzeichnis. Der Bericht Erzählende Website versucht die Anzahl der Dateien pro Verzeichnis auf einem überschaubaren Niveau zu halten. Dazu wird eine Verzeichnishierarchie erstellt. Die generierten Dateinamen sind nicht intuitiv, sondern für jede Person eindeutig. Nachfolgende Läufe generieren identische Dateinamen, was das Aktualisieren bestimmter Dateien erleichtert.

{{-}}

#### Dialog-Registerkarten

Das Dialogfeld für den Bericht über die hat die folgenden Registerkarten, die im Folgenden erläutert werden.

- [Berichtsoptionen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte_-_Teil_7#Berichtsoptionen)
- [HTML Optionen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte_-_Teil_7#HTML_Optionen)
- [Anzeige](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte_-_Teil_7#Anzeige)
- [Seitengenerierung](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte_-_Teil_7#Seitengenerierung)
- [Extraseiten](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte_-_Teil_7#Extraseiten)
- [Bilder Erstellung](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte_-_Teil_7#Bilder_Erstellung)
- [Download](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte_-_Teil_7#Download)
- [Erweiterte Optionen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte_-_Teil_7#Erweiterte_Optionen)
- [Einbeziehen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte_-_Teil_7#Einbeziehen)
- [Ortekarteoptionen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte_-_Teil_7#Ortekarteoptionen)
- [Andere Einbindungen (CMS, Webkalender, PHP)](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte_-_Teil_7#Andere_Einbindungen_.28CMS.2C_Webkalender.2C_PHP.29)
- [Übersetzungen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte_-_Teil_7#.C3.9Cbersetzungen)
- [Kalender Optionen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte_-_Teil_7#Kalender_Optionen)

{{-}}

##### Berichtsoptionen

![[_media/NarratedWebSite-WebPages-ReportOptions-tab-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Erzählende Website - Webseiten - Berichtsoptionen - Registerkarte Standardoptionen]]

-  (Kontrollkästchen standardmäßig deaktiviert) Wenn du Probleme hast, die Dateien an einen externen Webhost zu übertragen, kannst du eine einzelne gzip-Datei erstellen, um die Daten einfacher hochzuladen. Die große Anzahl von Dateien und Verzeichnissen in dieser Webausgabe kann die Übertragung der Dateien an einen externen Webhost erschweren. Gramps hat die Möglichkeit, alle deine Erzählende Website-Dateien in einem komprimierten Archiv mit den Formaten gzip und tar (auch bekannt als ‘Tarball’) zu speichern. Diese einzelne Datei kann schnell auf deinen Server übertragen und auf dem Website-Host entpackt werden. ****

- (`~/DeinHeimatVerzeichnis/`<Stammbaumname>`+NAVWEB` Vorgabe) Das Zielverzeichnis für die Webdateien.

- (`Mein Stammbaum` Vorgabe) Der Titel der Website. Du kannst in dieser Option einen benutzerdefinierten Site-Titel eingeben.

- (Jede Person, die diesem Filter entspricht und nicht aufgrund der Datenschutzregeln ausgeschlossen ist, wird in die Ausgabe aufgenommen.) wähle zwischen

  - **Gesamte Datenbank** (Standardeinstellung)
  - Nachkommen von aktive Person
  - Nachkommenfamilien von aktive Person
  - Vorfahren von aktive Person
  - Personen mit gemeinsamen Vorfahren mit aktive Person

- Die zentrale Person für den Bericht. (standardmäßig Aktive Person)

  -  (Kontrollkästchen standardmäßig deaktiviert) - Für jede Personenseite.

- Wie lebenden Personen behandelt werden. Du kannst die Anzeige vertraulicher Informationen basierend darauf steuern, ob eine Person derzeit lebt oder nicht. Da Gramps jedoch ein Recherchetool ist, ist es wahrscheinlich, dass es Personen ohne bekanntes Sterbedatum in deiner Datenbank gibt. Um abzuleiten, ob eine Person *möglicherweise noch lebt*, verwendet Gramps einen Algorithmus, der Sterbedaten, Geburtsdaten, Taufdaten, Sterbedaten von Vorfahren und Geburtsdaten von Vorfahren vergleicht. Der Algorithmus geht davon aus, dass jede Person *möglicherweise noch am Leben ist*, es sei denn, die Daten mit Querverweisen machen die Möglichkeit der Person, *am Leben zu sein*, unwahrscheinlich.

  - **Nicht enthalten** – (Vorgabe) Schließt alle Informationen aller *[möglicherweise noch lebenden](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Vermutlich_lebend)* Personen aus
  - **Nur Nachnamen aufnehmen**
  - **Nur Vollständige Namen aufnehmen**
  - **Aufnehmen und alle Daten** – Alle Informationen aller Personen aufnehmen, auch wenn diese *möglicherweise noch am Leben* sind

- (`30` Vorgabe) Diese Option ist inaktiv, wenn die Option "Lebende Personen" auf **Aufnehmen** gesetzt ist.

- : Ob vertrauliche Objekte eingeschlossen werden sollen. Wenn du beabsichtigst, eine vollständige Aufzeichnung deiner Recherchen bereitzustellen, werden durch Aktivieren dieses Kontrollkästchens alle als **vertraulich** gekennzeichneten Einträge zusammen mit dem Rest deiner Datenbank eingeschlossen. (Kontrollkästchen standardmäßig deaktiviert)

{{-}}

##### HTML-Optionen

![[_media/NarratedWebSite-WebPages-HTMLOptions-tab-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Erzählende Website - Webseiten - HTML-Optionen - Registerkarte Standardoptionen]]

- Die für die Webdateien zu verwendende Erweiterung.

  - **.html** (Standardeinstellung)
  - .htm
  - .shtml
  - .php
  - .php3
  - .cgi

- \- Wenn du eine öffentliche Website erstellst, ist es wichtig, die Urheberrechtsbedingungen anzugeben, unter denen du deine Daten veröffentlichst. Nach dem internationalen Urheberrecht liegen alle Rechte an deinen Daten in deinem Ermessen. Du bist der Eigentümer der Daten, und Personen müssen deine Erlaubnis haben, wenn sie diese Daten weiterverwenden wollen. In der genealogischen Forschung ist es üblich, Daten mit anderen Forschern zu teilen.

  - **Standard Copyright** (Standardeinstellung)
  - *Creative Commons - Namensnennung* - Eine Reihe von sechs Creative-Commons-Lizenzen, die verschiedene oder gar keine Nutzungsbeschränkungen vorsehen. Mehr über die Creative Commons erfährst du unter <https://creativecommons.org/>
  - *Creative Commons - Namensnennung, keine Bearbeitung*
  - *Creative Commons - Namensnennung, Weitergabe unter gleichen Bedingungen*
  - *Creative Commons - Namensnennung, Nicht kommerziell*
  - *Creative Commons - Namensnennung, Nicht kommerziell, keine Bearbeitung*
  - *Creative Commons - Namensnennung, Nicht kommerziell, Weitergabe unter gleichen Bedingungen*
  - *Keine Copyright Notiz*

{{-}} ![[_media/NarratedWebSite-Stylesheet-examples-52.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Registerkarte &quot;HTML-Optionen&quot; - &quot;StyleSheet&quot; acht Beispiele (in der Liste von oben nach unten aufgeführt.)]]

- Gramps bietet neun eingebaute Formatvorlagen, aus denen du wählen kannst, um das Aussehen deiner Webseiten zu bestimmen. Wähle zwischen diesen Formatvorlagen:

  - **Einfach-Asche** (ein 'Basis'-Farbschema)(Standardeinstellung)
  - *Einfach-Blau* (ein 'Basis'-Farbschema)
  - *Einfach-Zypresse*(ein 'Basis'-Farbschema)
  - *Einfach-Lila* (ein 'Basis'-Farbschema)
  - *Einfach-Pfirsich* (ein 'Basis'-Farbschema)
  - *Einfach-Tannengrün* (ein 'Basis'-Farbschema)
  - *Mainz*
  - *Nebraska*
  - *Keine Formartvorlage* (bestehende Stylesheets nicht überschreiben)
  - *Sehbehindert*

  
Unabhängig von dem von dir gewählten Stil ist die Formatvorlage in *`css/narrative-screen.css`* zu finden. Du kannst diese Datei bearbeiten, um das Erscheinungsbild deiner Webseiten weiter anzupassen.  
Wenn du Änderungen an deiner Formatvorlage vornimmst, sei dir bewusst, dass eine erneute Generierung deiner Seiten mit demselben Ausgabeziel deine benutzerdefinierte Formatvorlage überschreibt.

Die Option, keine Formatvorlage einzubinden (Keine Formatvorlage), ist für Benutzer gedacht, die bereits eine benutzerdefinierte Formatvorlage erstellt haben, als sie einen früheren Bericht über eine erzählte Website erstellten. Um dein benutzerdefiniertes Stylesheet bei späteren Aktualisierungen der Webseite beizubehalten, wähle .

Wenn du dein eigenes Stylesheet haben willst, kannst du eins von den vorhandenen Stylesheets in *`$HOME/.gramps/css/`* kopieren. Wenn dieses Verzeichnis nicht da ist, musst du es erst anlegen, bevor du dein zukünftiges Stylesheet kopierst. Ändere seinen Namen. Wenn du einen neuen Bericht anforderst, wird dieses neue Stylesheet zur Liste der schon vorhandenen Stylesheets hinzugefügt.

- Wähle das Layout für die Navigationsmenüs. (Nur für ausgewählte Formatvorlage verfügbar)

  - **Horizontal -- Vorgabe**
  - Vertikal -- Linke Seite
  - Überblenden -- nur [Webkit](https://de.wikipedia.org/wiki/WebKit) Browser
  - Drop-Down -- nur Webkit Browser

- Bestimme das Standardlayout für den Abschnitt Fundstellenreferenz der Quellseite

  - **Normaler Umrandungsstil** (Standardeinstellung)
  - Drop-Down -- nur Webkit Browser

- : Wenn du dieses Kästchen ankreuzt, wird eine Ahnengrafik auf der Detailseite jeder Person eingefügt, wenn sie definierte Vorfahren in deiner Datenbank hat. (das Kästchen ist standardmäßig aktiviert) (Hinweis: [In Erzählte Website Vorfahren-Baum-Design-Hinweise](wiki:Narrated_Website_Ancestry_Tree_Design_Notes) (englisch) wird die Erstellung eines kompakten Abstammungsbaums unter Verwendung des [Buchheim](wiki:Narrated_Website_Ancestry_Tree_Design_Notes#buchheim)/[Walker](wiki:Narrated_Website_Ancestry_Tree_Design_Notes#walker)-Algorithmus besprochen).

  - Du kannst die Anzahl der angezeigten Generationen auf den Registerkarten *[Diagrammgenerationen:](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte_-_Teil_7#Anzeige)* Option ändern.

-  (Kontrollkästchen standardmäßig deaktiviert) - fügt Links zur Navigationsleiste hinzu.

-  (Kontrollkästchen standardmäßig deaktiviert)

-  (Kontrollkästchen standardmäßig deaktiviert) - Aktiviere das Kontrollkästchen, wenn du einen Abschnitt öffnen/schließen möchtest.

{{-}}

##### Anzeige

![[_media/NarratedWebSite-WebPages-Display-tab-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Erzählende Website - Webseiten - Anzeige - Registerkarte Standardoptionen]]

- Wähle das Format aus, um die Namen anzuzeigen. Diese Auswahl wird normalerweise von der Standardeinstellung in [Bearbeiten &gt; Registerkarte Anzeige](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Einstellungen#Anzeige) für Namensformat übernommen:. Oder wähle eine der folgenden Optionen, um diese Einstellung für den Bericht zu überschreiben:

  - Vorgabe - (in einem neuen Stammbaum ist dies normalerweise *Nachname, Vorname Suffix*)
  - **Nachname, Vorname Suffix** (Standardeinstellung)
  - Vorname Nachname Suffix
  - Vorname
  - Haupt Nachnamen, Vorname Patronymikon Suffix
  - NACHNAME, Vorname (Üblich)

-  ( Kontrollkästchen standardmäßig nicht aktiviert) - Ob das erzählende Web in mehreren Sprachen angezeigt werden soll. Auf der Registerkarte kannst du eine neue Sprache zu der im nächsten Feld definierten Standardsprache hinzufügen.

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

- \- Die Option bestimmt, ob die Gramps-ID von Objekten in deiner Webseitenausgabe ausgeblendet oder angezeigt wird.

  - **Nicht aufnehmen** (Standardeinstellung)
  - Einbeziehen

- \- Whether to include tags

  - **Nicht aufnehmen** (Standardeinstellung)
  - Einbeziehen

- (Kontrollkästchen standardmäßig deaktiviert) - Ob Kinder in Geburtsreihenfolge oder in Eingabereihenfolge angezeigt werden sollen?

- (Kontrollkästchen standardmäßig deaktiviert) - Ob Breite/Länge in der Ortsliste angezeigt werden soll?

- (Kontrollkästchen standardmäßig deaktiviert) - Sortiert die Ortsreferenzen nach Datum oder Name. Nicht aktiviert bedeutet nach Datum.

- Diese Option ist inaktiv, wenn die Option *[Mit Ahnentafel](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte_-_Teil_7#HTML-Optionen)* auf der Registerkarte *HTML-Optionen* nicht aktiviert ist. Die Standardanzahl der in den Ahnendiagrammen angezeigten Generationen ist `4` mit den Optionen 2, 3, 4 oder 5. Die in den Ahnendiagrammen dargestellten Personen sind dieselben Personen, deren Informationen an anderer Stelle auf Ihren Webseiten bereitgestellt werden.

- (Kontrollkästchen standardmäßig aktiviert) - Wenn diese Option deaktiviert ist, werden sie direkt vor den Attributen angezeigt.

{{-}}

##### Seitengenerierung

![[_media/NarratedWebSite-WebPages-PageGeneration-tab-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Erzählende Website - Webseiten - Seiten Generation - Registerkarte Standardoptionen]]

Die Registerkarte *Seitengenerierung* bietet Optionen für die Erstellung von allgemein erwarteten ergänzenden Webseiten und Anmerkungen, die allen Webseiten auf der gesamten generierten Website gemeinsam sind.

Die ersten Optionen werden verwendet, um die Generierung von drei zusätzlichen Seiten zu steuern: **Startseite** ([Home-Webseite](https://de.wikipedia.org/wiki/Homepage)), **Einführung** ([FAQ](https://de.wikipedia.org/wiki/Frequently_Asked_Questions)- oder [Über uns](https://www.searchenginejournal.com/about-us-page-examples/250967/amp/)-Webseite) und **Herausgeberkontakt** ([Kontakt](https://wikipedia.org/wiki/Contact_page)-Webseite).

Jede der ergänzenden Seiten kann ein bestimmtes [Medien](wiki:De:Gramps_Glossar#Medien)- oder [Notizelement](wiki:De:Gramps_Glossar#Notiz) zugewiesen werden. Standardmäßig ist diesen Seiten kein Inhalt (weder Medien noch Text aus einer Notiz) zugewiesen.

Der Inhalt dieser Seiten ***muss*** aus Medien- oder Notizelementen stammen, die vor dem Ausführen des Berichts erstellt wurden. Nachdem die gewünschten Elemente zu deinem Baum hinzugefügt wurden, kannst du sie aus einer Liste von Notizen oder Medienobjekten auswählen.

- Zeigt eine individuelle Notiz deiner Wahl an.

- Zeigt ein individuelles Medienobjekt deiner Wahl an.

- Zeigt eine individuelle Notiz deiner Wahl an.

- Zeigt ein individuelles Medienobjekt deiner Wahl an.

- Zeigt eine individuelle Notiz deiner Wahl an.

- Zeigt ein individuelles Medienobjekt deiner Wahl an.

- Zeigt eine individuelle Notiz deiner Wahl an. Dieser Anmerkungstext wird auf jeder Webseite direkt unter dem Site-Titel angezeigt.

- Zeigt eine individuelle Notiz deiner Wahl an. Dieser Anmerkungstext erscheint in der Fußzeile über der Copyright-Erklärung auf jeder Webseite.

- Ein Hinweis, der zum Starten der PHP-Sitzung verwendet wird. Diese Option ist nur verfügbar, wenn die Dateierweiterung .php gewählt wurde.

{{-}}

##### Extraseiten

![[_media/:NarratedWebSite-WebPages-ExtraPages-tab-52.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Erzählende Website - Webseiten - Extraseiten - Registerkarte Standardoptionen]]

- (Standardeinstellung: leer) - Dein zusätzlicher Seitenname wird in der Menüleiste angezeigt.

- (Standardeinstellung: leer) - Dein zusätzlicher Seitenpfad ohne Erweiterung.

  - Schaltfläche

{{-}}

##### Bilder Erstellung

![[_media/NarratedWebSite-WebPages-ImageGeneration-tab-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Erzählende Website - Webseiten - Bilder Erstellung - Registerkarte Standardoptionen]]

-  Diese Option legt fest, ob eine Galerie von Medienobjekten auf deiner Website eingeschlossen/ausgeschlossen werden soll. (Kontrollkästchen standardmäßig aktiviert)

-  Mit dieser Option kannst du den Bildindex erstellen. (Standardmäßig ist das Kontrollkästchen deaktiviert)

-  Diese Option legt fest, ob eine Galerie nicht verwendeter Medienobjekte auf deiner Website eingeschlossen/ausgeschlossen werden soll. (Kontrollkästchen standardmäßig aktiviert)

-  : Mit dieser Option kannst du nur Miniaturbilder anstelle von Bildern in voller Größe auf der Medienseite erstellen. Auf diese Weise kannst du eine viel geringere Gesamtgröße für den Upload auf deine Webhosting-Site haben. (Kontrollkästchen standardmäßig deaktiviert)

- (`800` Standardeinstellung) Auf diese Weise kannst du die maximale Breite des auf der Medienseite angezeigten Bildes (in Pixel) festlegen.

- 

{{-}}

![[_media/wiki:How_to_create_image_reference_regions|[_media/NarrativeWeb-Media-tab-ImageReferenceRegions-example-50.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Beispiel für [Bildreferenzbereiche]] - Registerkarte Medien der HTML-Ausgabe für den Bericht "Erzählende Website"]]

Beachte, dass [Bildreferenzbereiche](wiki:How_to_create_image_reference_regions) auch in den mit Gramps erstellten Erzählende Website HTML-Seiten angezeigt werden. Für diese Funktion sind keine besonderen Optionen erforderlich, außer der Existenz von Referenzbereichen für 1 oder mehrere Bilder. Erzählende Website zeigt nur Referenzregionen für Personen und Ortsobjekte an. {{-}}

##### Download

![[_media/NarratedWebSite-WebPages-Download-tab-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Erzählende Website - Webseiten - Download - Registerkarte Standardoptionen]]

- : Ob eine Datenbank-Download-Option eingeschlossen werden soll. (Kontrollkästchen standardmäßig deaktiviert)

- (2 Standardwerte) Die Anzahl der Download-Dateien, die auf der Download-Seite erscheinen sollen.

- Wähle die Datei aus, die für das Herunterladen der Datenbank verwendet werden soll.

- (Stammbaum \#1 Standard) Gib eine Beschreibung für diese Datei an.

- Wähle die Datei aus, die zum Herunterladen der Datenbank verwendet werden soll.

- (`Stammbaum` Standardeinstellung) Gib eine Beschreibung für diese Datei an.

- Wähle die Datei aus, die zum Herunterladen der Datenbank verwendet werden soll.

- (`Stammbaum` Standardeinstellung) Gib eine Beschreibung für diese Datei an.

{{-}}

##### Erweiterte Optionen

![[_media/NarratedWebSite-WebPages-AdvancedOptions-tab-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Erzählende Website - Webseiten - Erweiterte Optionen - Registerkarte Standardoptionen]]

Diese Einstellungen beziehen sich auf die Informationsmenge, die auf den Webseiten Nachnamedetail und Individueller Index angezeigt wird.

- Die für die Webdateien zu verwendende Codierung.

  - **Unicode UTF-8 (empfohlen)** (Standardeinstellung)
  - ISO-8859-1 *- [ISO/IEC-Zeichensatzstandard:](https://de.wikipedia.org/wiki/ISO_8859) Teil 1 (Latein 1: Westeuropäisch)*
  - ISO-8859-2
  - ISO-8859-3
  - ISO-8859-4
  - ISO-8859-5
  - ISO-8859-6
  - ISO-8859-7
  - ISO-8859-8
  - ISO-8859-9
  - ISO-8859-10
  - ISO-8859-13
  - ISO-8859-14
  - ISO-8859-15
  - koi8_r ''- [Kod Obmena Informazijei, 8 bit ("Code für Informationsaustausch, 8 Bit")''](https://de.wikipedia.org/wiki/KOI8-R)

- : (Wenn sie eine Webseite haben) (Kontrollkästchen standardmäßig deaktiviert)

- (Kontrollkästchen standardmäßig aktiviert)

- (Kontrollkästchen standardmäßig deaktiviert)

- (Kontrollkästchen standardmäßig deaktiviert)

- (Kontrollkästchen standardmäßig deaktiviert)

- (Kontrollkästchen standardmäßig deaktiviert)

{{-}}

##### Einbeziehen

![[_media/NarratedWebSite-WebPages-Include-tab-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Erzählende Website - Webseiten - Einbeziehen - Registerkarte Standardoptionen]]

- (Kontrollkästchen standardmäßig deaktiviert)

- (Kontrollkästchen standardmäßig deaktiviert)

- (Kontrollkästchen standardmäßig deaktiviert)

-  (Kontrollkästchen standardmäßig deaktiviert)

- (Kontrollkästchen standardmäßig deaktiviert)

- (Kontrollkästchen standardmäßig deaktiviert)

- . Diese Option erstellt eine GENDEX-Datei, die oben auf der Website platziert wird. Du kannst Websites sehen, die dieses Format unterstützen, und mehr darüber im [GENDEX Wikipedia Artikel](https://de.wikipedia.org/wiki/GENDEX) lesen.)(Kontrollkästchen standardmäßig deaktiviert)

- (Kontrollkästchen standardmäßig deaktiviert)

- (Kontrollkästchen standardmäßig deaktiviert)

{{-}}

##### Ortekarteoptionen

![[_media/NarratedWebSite-WebPages-PlaceMapOptions-tab-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Erzählende Website - Webseiten - Ortekarteoptionen - Registerkarte Standardoptionen]]

- Wähle den Kartendienst deiner Wahl zum Erstellen der Ortskartenseiten

  - **OpenStreetMap** (Standardeinstellung)
  - Stamen Map
  - Google : Damit diese Option funktioniert, muss ein eingegeben werden. Um einen zu beantragen, gehe zur Google Maps-Plattform ( <https://cloud.google.com/maps-platform/> ) und wähle "Get Started" (obere rechte Ecke) und folge den Anweisungen (kann eine Kreditkarte beinhalten) und wähle dann die Option "Credentials" im Menü "API Manager" . Klicke dann im Fenster "Credentials" auf die Schaltfläche "create Credentials". Klicke im nächsten aufklappendes Fenster auf "API Key". Kopiere den generierten API-Schlüssel in deine Zwischenablage und füge ihn in das Gramps-Feld "Google Maps API Schlüssel:" ein. Ich schlage dringend vor, dass du nach der Erstellung und Online-Stellung deines Berichts zur Google Maps-Plattform zurückkehrst und im Fenster mit dem erstellten API-Schlüssel auf die Schaltfläche "Restrict key" klickst und deine Domain hinzufügst (dies verhindert, dass andere Websites deinen API-Schlüssel kapern und dich zahlen lassen! Diese neuen Änderungen an der Google Maps-API traten am 11. Juni 2018 in Kraft. Siehe die Preistabelle <https://cloud.google.com/maps-platform/pricing/sheet/> "Du erhältst außerdem eine wiederkehrende Gutschrift von 200 \$ monatlich auf dein Rechnungskonto, um deine Nutzungskosten auszugleichen, und du kannst Nutzungslimits festlegen, um dich vor unerwarteten Kostensteigerungen zu schützen."

- : Ob eine Ortskarte auf den Ortsseiten eingefügt werden soll, wenn Breitengrad/Längengrad verfügbar sind. (Kontrollkästchen standardmäßig deaktiviert)

- : Ob eine einzelne Seitenkarte mit allen Orten auf dieser Seite hinzugefügt werden soll oder nicht. Auf diese Weise kannst du sehen, wie deine Familie durch das Land gereist ist. (Kontrollkästchen standardmäßig deaktiviert)

- Wähle aus, welche Option du für die Google Maps Familie Kartenseiten haben möchtest...

  - **Familienverknüpfungen** (Standardeinstellung)
  - Drop
  - Markierungen

- Der für Google Maps verwendete API-Schlüssel. Dieser Schlüssel ist obligatorisch und muss gültig sein

- <https://developers.google.com/maps/documentation/javascript/get-api-key>

- 

- 

- 

- 

- 

{{-}}

##### Andere Einbindungen (CMS, Webkalender, PHP)

![[_media/NarratedWebSite-WebPages-OtherInclusionCMSWebCalendarPHP-tab-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Erzählende Website - Webseiten - Andere Einbindungen (CMS, Webkalender, PHP) - Registerkarte Standardoptionen]]

-  (Kontrollkästchen standardmäßig deaktiviert)

  - `/NAVWEB` (Standardeinstellung) - Wo platzierst du deine Website ?

-  (Kontrollkästchen standardmäßig aktiviert) Ob eine Seite mit den letzten Aktualisierungen eingefügt werden soll

- `1` (Standard) - Du willst die letzten Aktualisierungen seit wie vielen Tagen sehen?

- `1` (Standard) - Wie viele Aktualisierungen möchtest du maximal sehen?

{{-}} Siehe auch:

- [Integration von ErzählendeWebsite in ein CMS oder MVS](wiki:Howto:_Make_a_genealogy_website_with_Gramps#Integration_of_NarrativeWeb_in_a_CMS_or_MVS)
- Feature Request Integration von ErzählendeWebsite in ein CMS oder MVS

{{-}}

##### Übersetzungen

![[_media/NarratedWebSite-WebPages-Translations-tab-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Erzählende Website - Webseiten - Übersetzungen - Registerkarte Standardoptionen]]

Auf der Registerkarte „Übersetzung“ kannst du auswählen, in welchen Sprachen der Bericht angezeigt werden soll.

Um diesen Bereich zu nutzen, aktiviere die Option auf der Registerkarte und du kannst auch die Sprache wählen, in der der Webbericht angezeigt werden soll, wenn sie von der Standardsprache abweicht.

- *`Standard`* - Standardsprache, die Gramps verwendet.

<!-- -->

- *`Titel dieser Website`* - Ändere ihn so, dass er der Sprache für diese Übersetzung entspricht, oder verwende den Standard-Seitentitel für die Standardsprache, die Gramps verwendet.

- *`Standard`* - Standardsprache, die Gramps verwendet.

- *`Titel dieser Website`* - Ändere ihn so, dass er der Sprache für diese Übersetzung entspricht, oder verwende den Standard-Seitentitel für die Standardsprache, die Gramps verwendet.

- *`Standard`* - Standardsprache, die Gramps verwendet.

- *`Titel dieser Website`* - Ändere ihn so, dass er der Sprache für diese Übersetzung entspricht, oder verwende den Standard-Seitentitel für die Standardsprache, die Gramps verwendet

- *`Standard`* - Standardsprache, die Gramps verwendet.

- *`Titel dieser Website`* - Ändere ihn so, dass er der Sprache für diese Übersetzung entspricht, oder verwende den Standard-Seitentitel für die Standardsprache, die Gramps verwendet

- *`Standard`* - Standardsprache, die Gramps verwendet.

- *`Titel dieser Website`* - Ändere ihn so, dass er der Sprache dieser Übersetzung entspricht, oder verwende den Standard-Seitentitel für die Standardsprache, die Gramps verwendet.

Siehe auch:

- [Mehrere Sprachen für das erzählende Web und optionale andere Ergänzungen \#1051](https://github.com/gramps-project/gramps/pull/1051) hinzugefügt 9. November 2020

{{-}}

##### Kalender Optionen

![[_media/NarratedWebSite-WebPages-CalendarOptions-tab-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Erzählende Website - Webseiten - Kalenderoptionen - Registerkarte Standardoptionen]]

-  (Kontrollkästchen ist standardmäßig deaktiviert)

- `Sonntag`

- `Ehefrauen verwenden ihren eigenen Nachnamen`

-  (Kontrollkästchen ist standardmäßig deaktiviert)

-  (Kontrollkästchen ist standardmäßig aktiviert)

-  (Kontrollkästchen ist standardmäßig aktiviert)

-  (Kontrollkästchen ist standardmäßig deaktiviert)

-  (Kontrollkästchen ist standardmäßig aktiviert)

- `1914`

<!-- -->

- [Mehrere Sprachen für das narrative Web und optionale andere Ergänzungen \#1051](https://github.com/gramps-project/gramps/pull/1051) hinzugefügt 9. November 2020 "Der Webkalender funktioniert nicht, wenn mehrere Sprachen verwendet werden und wir Personen mit dem narrativen Web verbinden. Für jede Sprache verwende ich den entsprechenden Feiertagskalender. (#07151)"

{{-}}

#### Beispiel einer Website-Ausgabe

Die folgenden Abschnitte zeigen das Standardaussehen von Webseiten im Bericht „“Erzählende Website““ mit aktivierten optionalen Seiten. (Unter Verwendung des Stammbaums [example.gramps](wiki:example.gramps).)

{{-}}

##### Home

(optionale Seite) {{-}}

##### Einleitung

(optionale Seite) {{-}}

##### Personen

Personen (Index) (Standardseite) Dateiname: `individuals.html` ![[_media/NarratedWebSite-WebPages-Individuals-index-page-example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Erzählende Website - Webseiten - Personen (Index)-Seite - Standard-HTML-Ausgabe - Beispiel]]

{{-}}

##### <b>Nachnamen</b>

Nachnamen (Index) (Standardseite) Dateiname: `index.html`

###### Anzahl Nachnamen

Nachnamen (Zählindex - sortiert nach der Spalte „Anzahl der Personen“.) (Standardseite) Dateiname: `surnames_count.html` {{-}}

##### Familien

(optionale Seite) {{-}}

##### Ereignisse

(optionale Seite) {{-}}

##### Orte

Orte (Index) (Standardseite) Dateiname: `places.html` {{-}}

##### Quellen

Quellen (Index) (Standardseite) Dateiname: `sources.html` {{-}}

##### Aufbewahrungsorte

(optionale Seite) {{-}}

##### Medien

(Standardseite) {{-}}

##### Miniaturbilder

(Standardseite) {{-}}

##### Download

(optionale Seite) {{-}}

##### Adressbuch

(optionale Seite) {{-}}

##### Kontakt

(optionale Seite) {{-}}

##### Aktualisierungen

Aktualisierungen (Standardseite) Dateiname: `updates.html` {{-}}

#### <span id="HTML Code">**HTML-Code-Typ Hinweise**</span>

Gramps [<strong>Notizen</strong>](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Daten_eingeben_und_bearbeiten:_Ausführlich_-_Teil_2#Informationen_.C3.BCber_Notizen_bearbeiten), die auf die [Art](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Daten_eingeben_und_bearbeiten:_Ausführlich_-_Teil_2#note_type) **HTML-Code** eingestellt sind, werden unter dem Objekt eingefügt, an das sie angehängt sind. Auf diese Weise können spezielle *HTML-Bausteine* in den Bericht aufgenommen werden.

Die HTML-Blöcke müssen ordnungsgemäß formatiert sein, d. h. alle Tags müssen korrekt geschlossen sein, um Konflikte mit dem Rest der vom Bericht erzeugten Webseite zu vermeiden. Füge nur Tags in einen Hinweis vom Typ **HTML-Code** ein, die normalerweise im Textkörper eines HTML-Dokuments enthalten wären.

Die folgenden Tags werden immer ignoriert: `html`, `meta`, `doctype`, `head`, `meta`, `title`, `link`, `script`, `body`

Alle anderen Tags sind verfügbar: {{-}}

#### Voraussetzungen für die erzählte Website

Für Gramps 6.0.x musst du Pyicu und die zugehörigen Pakete installieren.

Siehe auch:

- Navweb wird nicht geladen ( Name localAlphabeticindex ist nicht definiert ) \[Wenn die optionale Voraussetzung PyICU nicht installiert ist \]

##### Mögliche Probleme

- Wenn der Bericht <b>"Fehlgeschlagenes Laden des Plugins“ anzeigt, ist der Name 'localAlphabeticIndex' nicht definiert: hast du die Voraussetzung `pyicu` installiert?</b>
  - Führe*`gramps -v`* auf der Kommandozeile aus, um zu sehen, ob zusätzliche Informationen angezeigt werden, die dir helfen könnten.
- Sonstige Fehler: [Fehler melden](wiki:Using_the_bug_tracker)

### <u>Webkalender</u>

![[_media/WebCalendar-WebPages-example-DecemberCalendar2018-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Webkalender Bericht - Webseiten - Standardkalender für Dezember 2018 - HTML Ausgabe]]

Der zeigt Ereignisse für die ausgewählten Personen in einem Satz monatlicher Kalender an. Du kannst diesen Bericht über das Menü erstellen.

Es gibt Optionen zum Filtern der Personen, um auszuwählen, welche Jahre eingeschlossen werden sollen (standardmäßig wird nur das aktuelle Jahr berücksichtigt); ob nur lebende Personen und Geburtstage oder Jubiläen oder beides berücksichtigt werden sollen; Notizen können auf Monatsseiten und gekürzte Seiten eingefügt werden.

Der Bericht ist so konzipiert, dass er mit dem [Erzählende Websitebebericht](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte_-_Teil_7#Erz.C3.A4hlende_Website) funktioniert. Wenn ausgewählt befindet sich auf jeder Seite ein "Heimat" Link zur Homepage des Erzählende Websitebeberichts. Es besteht auch die Möglichkeit, Links von den Personen im Kalender zu derselben Person auf der erzählten Website einzufügen.

Die Zusammenarbeit mit dem Erzählende Websitebebericht erfordert, dass die beiden Berichte vom Benutzer auf kompatible Weise erstellt wurden. Es gibt keine automatische Überprüfung, ob die beiden kompatibel sind. Wenn die Seiten nicht kompatibel sind, wird dem Benutzer wahrscheinlich die Fehlermeldung "[Seite nicht gefunden](https://de.wikipedia.org/wiki/HTTP_404)" angezeigt.

Die Kompatibilität hängt ab von:

1.  Die Einbeziehung derselben Personen in die beiden Berichte,
2.  Speichern der Seiten in kompatiblen Verzeichnissen.

Um dieselben Personen in die beiden Berichte einzubeziehen, sollten dieselben Filter verwendet werden und ähnliche Optionen in Bezug auf lebende Personen (der Webkalender bietet keine Option zum Entfernen "vertraulicher" Informationen).

Standardmäßig wird der Erzählende Websitebebericht im Verzeichnis "`~/`<Stammbaumname>`+NAVWEB`" gespeichert und der Webkalender wird standardmäßig im Verzeichnis "`~/`<Stammbaumname>`+WEBCAL`" gespeichert. Wenn diese Voreinstellungen beibehalten werden, sollten die verschiedenen Links ordnungsgemäß funktionieren. Wenn die Verzeichnisse geändert wurden, müssen der "Home-Link" unter den "Inhaltsoptionen" und das "Link-Präfix" unter den "Erweiterten Optionen" entsprechend geändert werden.

Wenn der Webkalender ohne eine zugehörige erzählende Website verwendet werden soll, deaktiviere auf der Registerkarte die Option , um sicherzustellen, dass kein „Home“-Link erzeugt wird.

#### Dialog-Registerkarten

Das Webkalender-Berichtsdialogfenster hat folgenden Registerkarten, von denen jede unten beschrieben wird.

- [Berichtsoptionen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte_-_Teil_7#Berichtsoptionen_2)
- [Berichtsoptionen (2)](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte_-_Teil_7#Berichtsoptionen_.282.29)
- [Inhaltsoptionen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte_-_Teil_7#Inhaltsoptionen)
- [Erweiterte Optionen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte_-_Teil_7#Erweiterte_Optionen_2)
- [Jan - Jun Notizen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte_-_Teil_7#Jan_-_Jun_Notizen)
- [Jul - Dez Notizen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte_-_Teil_7#Jul_-_Dez_Notizen)

{{-}}

##### Berichtsoptionen

![[_media/WebCalendar-WebPages-ReportOptions-tab-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Webkalender - Webseiten - Berichtsoptionen - Registerkarte Standardoptionen]]

- `~/DeinHomeVerzeichnis/`<Stammbaumname>`+WEBCAL` Das Zielverzeichnis für die Webdateien.

  - Schaltfläche

- (`Mein Familienkalender` Standardeinstellung) Der Titel des Kalenders.

- (Jede Person, die diesem Filter entspricht und nicht aufgrund der Datenschutzregeln ausgeschlossen ist, wird in die Ausgabe aufgenommen.) wähle zwischen

  - **Gesamte Datenbank** (Standardeinstellung)
  - Nachkommen von aktive Person
  - Nachkommenfamilien von aktive Person
  - Vorfahren von aktive Person
  - Personen mit gemeinsamen Vorfahren mit aktive Person

- Die zentrale Person für den Bericht. (standardmäßig Aktive Person)

- Die für die Webdateien zu verwendende Erweiterung.

  - **.html** (Standardeinstellung)
  - .htm
  - .shtml
  - .php
  - .php3
  - .cgi

-   
  Das Copyright, welches für die Webdateien verwendet wird.

  - **Standard Copyright** (Standardeinstellung)
  - *Creative Commons - Namensnennung* - Eine Reihe von sechs Creative-Commons-Lizenzen, die verschiedene oder gar keine Nutzungsbeschränkungen vorsehen. Mehr über die Creative Commons erfährst du unter <https://creativecommons.org/>
  - *Creative Commons - Namensnennung, keine Bearbeitung*
  - *Creative Commons - Namensnennung, Weitergabe unter gleichen Bedingungen*
  - *Creative Commons - Namensnennung, Nicht kommerziell*
  - *Creative Commons - Namensnennung, Nicht kommerziell, keine Bearbeitung*
  - *Creative Commons - Namensnennung, Nicht kommerziell, Weitergabe unter gleichen Bedingungen*
  - *Keine Copyright Notiz*

-   
  Die Formartvorlage, welche für die Webdateien verwendet wird.

  - **Einfach-Asche** (ein 'Basis'-Farbschema)(Standardeinstellung)
  - *Einfach-Blau* (ein 'Basis'-Farbschema)
  - *Einfach-Zypresse*(ein 'Basis'-Farbschema)
  - *Einfach-Lila* (ein 'Basis'-Farbschema)
  - *Einfach-Pfirsich* (ein 'Basis'-Farbschema)
  - *Einfach-Tannengrün* (ein 'Basis'-Farbschema)
  - *Mainz*
  - *Nebraska*
  - *Keine Formartvorlage* (bestehende Stylesheets nicht überschreiben)
  - *Sehbehindert*

{{-}}

##### Berichtsoptionen (2)

![[_media/WebCalendar-WebPages-ReportOptions2-tab-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Webkalender - Webseiten - Berichtsoptionen (2) - Registerkarte Standardoptionen]]

- Wähle das Format aus, um die Namen anzuzeigen. Diese Auswahl wird normalerweise von der Standardeinstellung in [](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Einstellungen#Anzeigeoptionen) für Namensformat übernommen:. Oder wähle eine der folgenden Optionen, um diese Einstellung für den Bericht zu überschreiben:

  - *Nachname, Vorname Suffix* (Standard in einem neuen Stammbaum)
  - Vorname Nachname Suffix
  - Vorname
  - Haupt Nachnamen, Vorname Patronymikon Suffix
  - NACHNAME, Vorname (Üblich)

- : Ob vertrauliche Objekte eingeschlossen werden sollen. Wenn du beabsichtigst, eine vollständige Aufzeichnung deiner Recherchen bereitzustellen, werden durch Aktivieren dieses Kontrollkästchens alle als **vertraulich** gekennzeichneten Einträge zusammen mit dem Rest deiner Datenbank eingeschlossen. (Kontrollkästchen standardmäßig deaktiviert)

-  (Kontrollkästchen standardmäßig aktiviert) - beseitigt die Vorfahren von Webkalendern, die als Gedächtnisstütze und nicht als historisches Instrument verwendet werden.

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

##### Inhaltsoptionen

![[_media/WebCalendar-WebPages-ContentOptions-tab-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Webkalender - Webseiten - Inhaltsoptionen - Registerkarte Standardoptionen]]

-  (Kontrollkästchen standardmäßig deaktiviert)

  - (Standardmäßig das aktuelle Jahr)

  - (Standardmäßig das aktuelle Jahr)

- Wähle das Land aus, um die zugehörigen Feiertage anzuzeigen. (Standardmäßig leer)

- Wähle den ersten Tag der Woche für den Kalender aus. (Vorgabe: **Sonntag**)

- Wähle den angezeigten Nachnamen der verheirateten Frauen aus.

  - **Frauen benutzen ihren Mädchennamen** (Standardeinstellung)
  - Frauen benutzen den Nachnamen vom Mann (von der ersten gelisteten Familie)
  - Frauen benutzen den Nachnamen vom Mann (von der letzten gelisteten Familie)

![[_media/WebCalendar-WebPages-example-JanuaryCalendar2021-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Webkalender – Webseiten – Feiertage in den USA im Januar 2021: Neujahr, 1.; MLK-Tag, 3. Montag; Amtseinführungstag, alle vier Jahre am 20.]] {{-}}

##### Erweiterte Optionen

![[_media/WebCalendar-WebPages-AdvancedOptions-tab-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Webkalender - Webseiten - Erweiterte Optionen - Registerkarte Standardoptionen]]

- Die für die Webdateien zu verwendende Codierung.

  - **Unicode UTF-8 (empfohlen)** (Standardeinstellung)
  - ISO-8859-1 *- [ISO/IEC-Zeichensatzstandard:](https://de.wikipedia.org/wiki/ISO_8859) Teil 1 (Latein 1: Westeuropäisch)*
  - ISO-8859-2
  - ISO-8859-3
  - ISO-8859-4
  - ISO-8859-5
  - ISO-8859-6
  - ISO-8859-7
  - ISO-8859-8
  - ISO-8859-9
  - ISO-8859-10
  - ISO-8859-13
  - ISO-8859-14
  - ISO-8859-15
  - koi8_r ''- [Kod Obmena Informazijei, 8 bit ("Code für Informationsaustausch, 8 Bit")''](https://de.wikipedia.org/wiki/KOI8-R)

-  (Kontrollkästchen standardmäßig deaktiviert)

-  (Kontrollkästchen standardmäßig aktiviert)

-  (Kontrollkästchen standardmäßig aktiviert)

-  (Kontrollkästchen standardmäßig deaktiviert)

-  (Kontrollkästchen standardmäßig deaktiviert)

- (`1914` Standard) Daten nur nach diesem Jahr anzeigen. Standardwert ist das aktuelle Jahr - "Höchstalter wahrscheinlich lebend", das in den Datumseinstellungen definiert ist.

- **`../../StammbaumName_NAVWEB/`** Ein Präfix auf die Links, die dich zum kommentierten Webbericht führen.

{{-}}

##### Jan - Jun Notizen

![[_media/WebCalendar-WebPages-Jan-JunNotes-tab-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Webkalender - Webseiten - Jan - Jun Notizen - Registerkarte Standardoptionen]]

Verwende die Schaltflächen , um bei Bedarf für jeden Monat eine Notiz aus der Auswahlbox auszuwählen:

- 

- 

- 

- 

- 

- 

{{-}}

##### Jul - Dez Notizen

![[_media/WebCalendar-WebPages-Jul-DecNotes-tab-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Webkalender - Webseiten - Jul - Dez Notizen - Registerkarte Standardoptionen]]

Verwende die Schaltflächen , um bei Bedarf für jeden Monat eine Notiz aus der Auswahlbox auszuwählen:

- 

- 

- 

- 

- 

- 

{{-}}

#### Beispiel einer Website-Ausgabe

![[_media/WebCalendar-WebPages-example-DecemberCalendar2018-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Webkalenderbericht - Webseiten - Standardkalender für Dezember 2018 - HTML-Ausgabe]]

{{-}}

### Siehe auch

- [Web-Lösungen für Gramps](wiki:Web_Solutions_for_Gramps)

<hr>

Zurück zur [Übersicht der Berichte](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte).

[B](wiki:Category:De:Dokumentation) [Category:Plugins](wiki:Category:Plugins)
