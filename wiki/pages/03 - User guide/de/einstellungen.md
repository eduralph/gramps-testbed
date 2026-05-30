---
title: De:Gramps 6.0 Wiki Handbuch - Einstellungen
categories:
- De:Dokumentation
- Stub
- Tips
managed: false
source: wiki-scrape
wiki_revid: 131228
wiki_fetched_at: '2026-05-30T17:43:46Z'
lang: de
---

{{#vardefine:chapter\|15}} {{#vardefine:figure\|0}} Dieser Abschnitt befasst sich mit den Einstellungen, die du in Gramps entweder im Dialogfeld oder in [verschiedenen anderen Einstellungen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Einstellungen#Andere_Einstellungen) verwalten kannst. Außerdem geht es um verschiedene Möglichkeiten, Gramps [anzupassen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Einstellungen#Anpassen).

## Einstellungen

![[_media/EditPreferencesTabsOnly-overview-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Übersicht über alle Standard Einstellungen-Registerkarten]]

Die meisten Einstellungen, die sich auf das gesamte Gramps-Programm auswirken, werden im Dialogfeld konfiguriert. Um es aufzurufen, wähle das Menü oder klicke auf das Symbol in der Symbolleiste.

Es gibt Überschreibungen, die vor dem Start von Gramps eingestellt werden können (z. B. die Einstellung der Sprache, die in den Schnittstellen oder für Berichte angezeigt wird), die vorübergehend oder dauerhaft über die [Befehlszeilenschnittstelle](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Kommandozeilen_Referenz) gesetzt werden können.

Für Konfigurationsoptionen, die auf die aktuelle Ansicht oder das Gramplet-Set beschränkt sind, wähle über das Menü , klicke auf die Schaltfläche ![[_media/Gramps-config.png]] in der Symbolleiste oder drücke die [Tastenkombination](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Tastenkürzel_Referenz#Allgemeine_K.C3.BCrzel) *Aktive Ansicht konfigurieren*.

Die Registerkarten oben zeigen die verfügbaren Optionskategorien wie folgt an:

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

Es können auch *andere* zusätzliche Registerkarten von allen [Zusatzmodule](wiki:6.0_Addons#Addon_List) angezeigt werden, die du möglicherweise installiert hast. {{-}}

### Daten

![[_media/EditPreferences-Data-tab-default-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menü: &quot;Bearbeiten -&gt; Voreinstellungen...&quot; Registerkarte &quot;Daten&quot; Standardeinstellungen]] Die Registerkarte enthält Einstellungen, die für die folgenden beiden Abschnitte relevant sind:

- 

- 

{{-}}

#### Anzeigeoptionen

![[_media/EditPreferences-Data-tab-DisplayOptions-section-default-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menü: &quot;Bearbeiten -&gt; Einstellungen...&quot; Registerkarte &quot;Daten&quot; Abschnitt &quot;Anzeigeoptionen&quot; Standardwerte]] Der Abschnitt enthält die folgenden Optionen:

- Diese Option steuert die Anzeige von Orten. Diese Funktion wurde in der 5.0-Revision als " Automatische Ortsbezeichnung aktivieren" und in der 5.1-Revision als "Ortsformat (automatische Ortsbezeichnung)" bezeichnet. Die [Hierarchie der Orte](wiki:De:Gramps_4.1_Wiki_Handbuch_-_Was_ist_neu%3F#Orte_Hierarchien) war in der Version [4.1.0](wiki:Template:Releases/4.1.0) neu, und die [Registerkarte "Orte"](wiki:De:Gramps_4.2_Wiki_Handbuch_-_Einstellungen#Orte) in den Voreinstellungen gab es erst in der Version 4.2. Es werden größere Überarbeitungen für die Ortshierarchien erwartet, so dass diese Schnittstelle wahrscheinlich wieder verlegt und umbenannt werden wird.

  - **Vollständig** (Standardeinstellung)
    - Die Auswahl der Schaltfläche zeigt den

- Diese Option steuert die Anzeige der Koordinaten. (Siehe [Unterstützte Längen/Breiten Formate](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Daten_eingeben_und_bearbeiten:_Ausführlich_-_Teil_2#Unterst.C3.BCtzte_L.C3.A4ngen.2FBreiten_Formate))

  - **DEG Notation von Grad, Minuten und Sekunden** (Standardeinstellung)
  - DEG-: Grad-, Minuten-, Sekunden-Notation mit :
  - D.D4 Grad-Notation, 4 Dezimalstellen
  - D.D8 Grad-Notation, 8 Dezimalstellen (Genauigkeit wie ISO-DMS)
  - RT90 Ausgabeformat für das [schwedische Koordinatensystem RT90](https://en.wikipedia.org/wiki/Swedish_grid)

-   
  Diese Option steuert die Anzeige von Namen. In Gramps gibt es zwei Möglichkeiten, um Namen anzuzeigen: die vordefinierten Formate und die benutzerdefinierten Formate . Mehrere verschiedene vordefinierte Namensformate sind verfügbar: **"Nachname, Vorname Suffix"** (Standard), **"Vorname Nachname Suffix"**, **"Vorname"**, **"Primär\[Nach\] Primär\[Verb\] Kein Patronymikon, Vorname Patronymikon\[Nach\] Suffix Primär\[Prä\]"**

  - Das Anklicken des Buttons auf der rechten Seite öffnet das Fenster , in dem die verfügbaren Optionen angezeigt werden. Es wird das Format und ein Beispiel dazu angezeigt. Wenn die vordefinierten Formate nicht passen, kann man auch eigene Formate erstellen. Du kannst die Schaltfläche verwenden, um ein Namensformat der Liste hinzuzufügen. Einmal klicken gibt dir ein **NACHNAME,Vorname Suffix(Rufname)** Format und als Beispiel : **SMITH, Edwin Jose Sr (Ed)**. Wenn du ein neues Namensformat der Liste hinzufügst, werden die Schaltflächen und verfügbar um die Namensformatliste zu ändern.
    -   
      Kontrollkästchen standardmäßig deaktiviert. Wenn ausgewählt, erlaubt es Gramps, patronymische und matronymische Namen als Nachnamen zu betrachten.

-   
  Diese Option kontrolliert die Anzeige von Daten. Es ist eine globale Einstellung, die einen Neustart von Gramps erfordert, um wirksam zu werden, und gilt für die Anzeige von Datumsangaben in allen in Gramps geladenen Datenbanken, bis das Datumsanzeigeformat erneut geändert wird. Es sind mehrere unterschiedliche Formate verfügbar, die möglicherweise von deinem Gebietsschema abhängen.

  - **JJJJ-MM-TT (ISO)** (Standardeinstellung) - Beispiel 2020-09-30 – Zeigt das Datum unter Verwendung des internationalen Standards [ISO 8601 Datenelemente und Austauschformate – Informationsaustausch](https://de.wikipedia.org/wiki/ISO_8601) an, was besonders nützlich ist, wenn Daten zwischen Ländern mit unterschiedlichen Konventionen zum Schreiben von Zahlen, Daten und Zeiten ausgetauscht werden.
  - Numerisch
  - Monat Tag Jahr
  - MONAT Tag Jahr
  - Tag. Monat Jahr
  - Tag. MONAT Jahr

<!-- -->

- 

  - **Jahre**(Standard)
  - Jahre, Monate
  - Jahre, Monate, Tage

- 

- 

<!-- -->

- **Gregorianisch** (Standardeinstellung).

Diese Option kontrolliert die Anzeige der Zeitrechnung in Berichten, Werkzeugen, Gramplets und Ansichten. Es stehen mehrere verschiedene Kalender zur Verfügung (siehe [Daten bearbeiten](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Daten_eingeben_und_bearbeiten:_Ausführlich_-_Teil_1#Daten_bearbeiten)). Zwei Daten mit zwei unterschiedlichen Kalendern zeigen Zeitlinien und Zeiträume nicht korrekt an, (z.B. beim setzen des gregorianischen Kalender als Standardanzeigekalender, haben Anwender eine bessere Kohärenz zum Anzeigen von Daten bei Zeiträumen).

- **Gregorianisch**(Standardeinstellung).

- **Am Vortag**(Standardeinstellung).

<!-- -->

-   
  Diese Option kontrolliert die Informationen, die in der Statusleiste angezeigt werden. Dies kann entweder der **Name und die ID der [aktuellen Person](wiki:Gramps_Glossary#active_person)**(Standard) sein oder **die Verwandtschaftsbeziehung zu der [Hauptperson](wiki:De:Gramps_Glossar#home_person)**.

- **Alt** (Voreinstellung). Wähle aus den verfügbaren Zusatzmodulen für die Zusammenstellung und Anzeige von Fundstellendaten. Das integrierte [CITE-Plugin](wiki:Addon_list_legend#cite) "Alt" ist mit den Versionen 5.1.6 und früher kompatibel.

##### Ortsformateditor

![[_media/EditPreferences-Data-tab-DisplayOptions-section-PlaceFormatEditor-dialog-default-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Ortsformateditor - Dialog (Standard) von Menü: "Bearbeiten&gt;Einstellungen..." - Registerkarte "Daten" Abschnitt "Anzeige"]]

Das Dialogfeld enthält Einstellungen, die für die Darstellung von Orten relevant sind.

Das Dialogfeld kann über – Registerkarte „Daten“ im Abschnitt [Anzeigeoptionen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Einstellungen#Anzeigeoptionen) über die Schaltfläche bei der Option aufgerufen werden.

Im Dialogfeld kannst du benutzerdefinierte Ortsformate erstellen, indem du auf die Schaltfläche {man button\|Hinzufügen}} in der linken Spalte klickst und anhand der folgenden Einstellungen auswählst, wie die einzelnen Teile des angezeigten Ortes dargestellt werden sollen:

- `Neu` (Standard) – Ein Name für das Ortsformat. Es wird dringend empfohlen, diesen Namen so zu ändern, dass er eindeutig ist.

- `:` (Standard-Doppelpunkt „:“ bedeutet, dass der gesamte Ortsname angezeigt wird) – Wählen Sie die Hierarchieebenen der anzuzeigenden Ortsnamen aus.

  - Jede Ebene in der Hierarchie wird durch eine positive ganze Zahl dargestellt, beginnend mit 0 für den ausgewählten Ort und um 1 erhöht für jede Ebene höher in der Hierarchie. Die Ebenen können auch durch negative ganze Zahlen dargestellt werden, beginnend mit -1 für die oberste Ebene (in der Regel ein Land) und um jeweils 1 verringert für jede niedrigere Ebene in der Hierarchie. Darüber hinaus wird der besiedelte Ort (Stadt, Gemeinde, Dorf oder Weiler) durch den Buchstaben p dargestellt; dieser kann mit einem Offset verwendet werden (z. B. p+1 oder p-2).
  - Die anzuzeigenden Namen werden als kommaseparierte Liste von Bereichen definiert. Ein Bereich kann entweder eine einzelne Ebene oder eine Startebene und eine Endebene sein, die durch einen Doppelpunkt getrennt sind. Die Startebene muss in einem Bereich kleiner als die Endebene sein. Die Start- und Endebenen sind standardmäßig 0 und -1, falls sie fehlen.

- \- Optional kannst du die Nummer und die Straße zusammenfügen, um das Komma zu unterdrücken.

  - **Keine** (Standard) - Anzeige wie vorhanden.
  - *Nummer Straße* - Damit diese Optionen funktionieren, muss die Straße den [<strong>Type</strong>](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_2#Place_Editor_dialog) *Straße* und die Hausnummer den **Type** *Nummer* haben.

- *Straßennummer* - wie bei *Nummer Straße*

- (Standardmäßig leer) Ein [zweistelliger Sprachcode](https://de.wikipedia.org/wiki/Liste_der_ISO-639-Sprachcodes).

-  (Kontrollkästchen standardmäßig deaktiviert)

Du kannst ein benutzerdefiniertes Ortsformat mit der Schaltfläche löschen.

Der verfügt standardmäßig über ein vordefiniertes Format namens **Vollständig**.

Siehe auch:

- [Implement place formats \#368](https://github.com/gramps-project/gramps/pull/368)
- [Hierarchische Ortsstruktur](wiki:Hierarchical_Place_Structure)
- <https://gramps-project.org/wiki/index.php/GEPS_045:_Place_Model_Enhancements_-_Place_Changes_Screenshots#Enhanced_Place_Format_Editor>
- [(Gramps-users) Proposed place formatting dialogs](https://sourceforge.net/p/gramps/mailman/message/36637553/) From: Nick Hall. - 2019-04-11
- <https://sourceforge.net/p/gramps/mailman/message/36422019/>
- <https://sourceforge.net/p/gramps/mailman/message/36363239/>
- <https://sourceforge.net/p/gramps/mailman/message/35694337/>
- [Orteeditor Dialog](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Daten_eingeben_und_bearbeiten:_Ausführlich_-_Teil_2#Orteditor_Dialog)
- [Ortsnameeditor Dialog](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Daten_eingeben_und_bearbeiten:_Ausführlich_-_Teil_2#Ortsnamenseditor_Dialog)

{{-}}

###### Beispiel für Ortsformate

Der Editor verfügt über ein neues Feld namens „Ebenen“. Damit können Benutzer Hierarchieebenen an Orten auswählen, die lose auf der Python-String-Slicing-Syntax basieren. Eine Reihe von Doppelpunktbereichen kann in einer durch Kommas getrennten Liste angegeben werden. „0“ steht für die unterste Ebene – in der Regel ein Gebäude oder eine Straße. „-1“ steht für die höchste Ebene – in der Regel ein Land. Der besiedelte Ort wird als „p“ dargestellt.

Zum Beispiel: "p:" = Besiedelter Ort nach oben. "p,-1" = Besiedelter Ort und Land.

Gültige Optionen:

- `0 - 9` - Hierarchieebene
- `-` - Negativ
- `:` - ??
- `p` - Besiedelter Ort
- `,` - Komma

Beispiele für Ortsformate

- \["p:" = Besiedelter Ort nach oben\]
- \["p,-1" = Besiedelter Ort und Land.\]
- \[1,p Haus und Stadt\],\[p,1 Stadt und Haus\]

Damit kannst du lange Ortsbeschreibungen in Berichten und Ansichten einschränken.[1](https://github.com/gramps-project/gramps/pull/368#issuecomment-290886087)

{{-}}

##### Anzeigename-Editor

![[_media/EditPreferences-Data-tab-DisplayOptions-section-DisplayNameEditor-dialog-default-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} „Anzeigenamen-Editor“ – Dialogfeld (Standard) aus dem Menü: „Bearbeiten &gt; Einstellungen...“ – Registerkarte „Daten“ &gt; Abschnitt „Anzeigeoptionen“]] Mit dem kannst du benutzerdefinierte Namensformate festlegen, die in Berichten und Diagrammen auf globaler Ebene oder auf individueller Ebene angezeigt werden können.

Der besteht aus zwei Bereichen:

- -Bereich oben

- Tabellenabschnitt

Der kann über das Menü aufgerufen werden: – Registerkarte \> Abschnitt – Schaltfläche . {{-}}

###### Hilfe-Referenz

Anzeigename Hilfe-Referenz:

<hr>

Die folgenden Schlüsselwörter werden durch die entsprechenden Namensteile ersetzt:

- **Vorname** - Vorname/Taufname
- **Titel** - Titel (Dr., Frau)
- **Rufname** - Rufname
- **Initialen** - Anfangs Buchstaben des/der Vornamen
- **Präfix** - alle Präfixe (von, de)
- **Nachname** - Nachname (mit Präfixe und Konnektoren)
- **Suffix** - Suffix (Jr., Sr.)
- **Spitzname** - Spitzname
- **Üblich** - Spitzname als erste Option, wenn er existiert, Rufname als zweite Option, sonst erster Vorname

<hr>

  
Surname:

- **Rest** - nicht primäre Nachnamen
- **Familiensspitzname** - Spitzname der Familie
- **Primär, Primär\[Prä\] oder \[Nach\] oder \[Verb\]**- vollständiger primärer Nachname, Präfix, nur Nachname, Konnektor
- **Patronymikon, oder \[Prä\] oder \[Nach\] oder \[Verb\]** - vollständiger pa/matronymischer Nachname, Präfix, nur Nachname, Konnektor
- **Nichtpatronymisch**- alle Nachnamen, außer pa/matronymische & primär
- **OriginalNachnamen**- Nachnamen (keine Präfixe und Konnektoren)

<hr>

Zusätzliche Klammern, Kommas werden entfernt. Anderer Text erscheint wörtlich.

<hr>

  
**Beispiel:** Dr. Edwin Jose von der Smith and Weston Wilson Sr (“Ed”) - Underhills  

*Edwin Jose*: **Given**, *von der*: **Prefix**, *Smith* und *Weston*: **Primary**, *and*: <abbr title="ein Verbinder">**\[verb\]**</abbr>, *Wilson*: **Patronym**,  

*Dr.*: **Titel**, *Sr*: **Suffix**, *Ed*: **Spitzname**, *Underhills* <abbr title="Familiensspitzname">**Familynick**</abbr>, Jose <abbr title="genannt (bevorzugter Vorname)">**Call**</abbr>.

<hr>

{{-}}

###### Hilfe Referenz Beispielperson

![[_media/wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_3#Name_Editor|[_media/NameEditor-format_reference_example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Display Name Editor's - reference person shown in the [Name Editor]] dialog]]

Alle Felder für die Hilfe-Referenz **Beispielperson** mit Ausnahme des Familienkürzels können im Standarddialogfeld „Personeneditor“ hinzugefügt werden. Doppelklicke im Register Namen des Personeneditors auf den bevorzugten Namen, um auf zusätzliche Felder zuzugreifen, darunter: Familienkürzel, Gruppierungssteuerelemente, Ausnahmesteuerelemente für Sortierung und Anzeige sowie Datumsbereichssteuerelemente für die Verwendung eines bestimmten Namens. {{-}}

###### Anzeigenamensliste

In diesem Abschnitt kannst du vorhandene Namensformate hinzufügen, entfernen oder bearbeiten und dir ein Beispiel für den formatierten Namen ansehen.

Die Tabelle enthält zwei Überschriften: und

- – Basierend auf den angezeigten Namensbestandteilen

- – Zeigt das Namensformat an, das auf eine [integrierte Referenzperson](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Einstellungen#Hilfe_Referenz_Beispielperson) angewendet wird

Die Liste enthält vier Standardformate für Anzeigenamen:

- *Nachname, Vorname Suffix* - zeigt den Namen als:
- *Vorname Nachname Suffix* - zeigt den Namen als:
- *Vornme* - zeigt den Namen als: *Edwin Jose*
- *xxx*' - zeigt den Namen als:

<!-- -->

- – ein neues Namensformat, gib die erforderlichen Schlüsselwörter nach Bedarf ein und drücke die , um das Ergebnis anzuzeigen

- – ein vorhandenes Namensformat (mit Ausnahme der vier Standard-Namensformate )

- – ein vorhandenes Namensformat (mit Ausnahme der vier Standard-Namensformate )

{{-}}

#### Eingabeoptionen

![[_media/EditPreferences-Data-tab-InputOptions-section-default-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menü: "Bearbeiten -&gt; Einstellungen..." Registerkarte "Daten" Abschnitt "Eingabeoptionen" Standardwerte]]

- <span id="surname guessing"><span> Diese Option wirkt sich auf den anfänglichen Familiennamen eines Kindes aus, wenn es dem Familienstammbaum hinzugefügt wird.
  - **Nachname des Vaters** (Vorgabe) - verwendet den Familiennamen des Vaters.
  - *keine* - wird keine Nachnamenvermutung versucht.
  - *Kombination der Nachnamen von Vater und Mutter* - verwendet den Familiennamen des Vater gefolgt von dem der Mutter.
  - *[Isländischer Stil](https://de.wikipedia.org/wiki/Isl%C3%A4ndischer_Personenname)* - verwendet den Vornamen des Vaters gefolgt von dem Suffix "sson" (z.B. der Sohn von Edwin wird als Edwin*sson* vermutet).

- \- Verwendet vom Dialogfeld .

  - **Unbekannt**(Vorgabe) - die vom Dialogfeld verwendet wird.
  - *Verheiratet*
  - *Unverheiratet*
  - *Gesetzliche Partnerschaft*

<!-- -->

-   
  Heilige der letzten Tage

{{-}}

### Allgemein

![[_media/EditPreferences-General-tab-EnviromentSettings-section-default-60-de.png|Right|thumb|450px|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menü: „Bearbeiten -&gt; Einstellungen...“ Registerkarte „Allgemein“ Abschnitt „Umgebungseinstellungen“ Standardeinstellungen]]

Diese Registerkarte enthält einen Abschnitt mit Einstellungen, die für den allgemeinen Betrieb des Programms relevant sind.

#### Umgebungseinstellungen

-   
  Diese Option schaltet den [Tipp des Tages Dialog](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Einstellungen#Tipp_des_Tages_Dialog) beim Programmstart ein oder aus.

-   
  Das Aktivieren dieser Kontrollkästchen-Option bewirkt, dass die zuletzt verwendete Datenbank beim Start geladen wird. Es umgeht den Dialog **Stammbäume verwalten**.

-   
  Diese Option kontrolliert das Aktivieren und Deaktivieren des Anzeigen der letzten [Ansicht](wiki:De:Gramps_Glossar#Ansicht). Das Aktivieren wird dich beim nächsten Programmstart zu der Ansicht bringen, mit der du das Programm beendet hast.

-   
  Diese Option ermöglicht das Aktivieren und Deaktivieren der globalen Rechtschreibprüfung für Notizen. Das **'[gspell](https://gitlab.gnome.org/GNOME/gspell)** Paket muss geladen sein, damit dies funktioniert. [2](https://github.com/gramps-project/gramps/pull/1450) ( Siehe: [Fehlerbehebung bei der Rechtschreibprüfung](wiki:Troubleshoot_Spellcheck) ) ( Beachte, dass die Option „Bearbeiten\>Voreinstellungen“ global Englisch oder die Sprache, in der Gramps ausgeführt wird, aktiviert und dass das Kontextmenü für Notizen in der von dir gewählten Sprache angezeigt wird)

<!-- -->

- *aktiviert* (Standardeinstellung) Dieses Kontrollkästchen steuert, ob neben dem Symbol im [Navigator](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Hauptfenster#Navigation) im [Hauptfenster](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Hauptfenster#Hauptfenster) eine Textbeschreibung angezeigt wird oder nicht. Diese Option wird erst nach einem Neustart des Programms wirksam.

<!-- -->

- 

- 

- 

- 

- 

- .

  - **Sowohl Text als auch Symbole (Standard)**
  - *Nur Text*
  - *Nur Symbole*

- *aktiviert*(Vorgabe)

<!-- -->

- Standardeinstellung: `<b>%s</b>`

  - Praktische Auszeichnungen sind:
    - <b>\<b\>Bold\</b\></b> (Standardeinstellung)
    - <big>\<big\>Macht die Schrift relativ größer\</big\></big>
    - <i>\<i\>Kursiv\</i\></i>
    - <s>\<s\>Durchgestrichen\</s\></s>
    - <sub>\<sub\>Tiefgestellt\</sub\></sub>
    - <sup>\<sup\>Hochgestellt\</sup\></sup>
    - <small>\<small\>Macht die Schrift relativ kleiner\</small\></small>
    - `<tt>Konstantschrift</tt>`
    - <u>\<u\>Unterstreichen\</u\></u>
      - Zum Beispiel: \<u\>\<b\>%s\</b\>\</u\> wird **<u>Fett unterstrichenes</u>** Datum angezeigt.

<!-- -->

- Standardwert: `150` Pixels

#### Tipp des Tages Dialog

![[_media/TipOfTheDay-dialog--example-PrivacyInGramps-60-de.png|Right|thumb|400px|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Tipp des Tages Dialog - Beispiel]]

Wenn im Reiter aktiviert, zeigt der Dialog hilfreiche Hinweise.

Folgende Optionen stehen zur Verfügung:

-  (Kontrollkästchen standardmäßig aktiviert - wenn einmal aktiviert) - deaktivieren, um zu verhindern, dass weitere Tipps angezeigt werden.

- \- Fahren Sie mit dem nächsten Tipp fort.

- \- für diese Sitzung beenden, bis das Gramps-Programm neu gestartet wird.

{{-}}

### Stammbaum

![[_media/EditPreferences-FamilyTree-tab-default-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menü:  - "Stammbaum" - Registerkarte - Standardeinstellungen]]

Der Reiter enthält die folgenden vier Abschnitte:

- 

- 

- 

- 

Siehe auch:

- [Einen Stammbaum sichern](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Stammbäume_Verwalten#Einen_Stammbaum_sichern) - weitere Informationen zu Sicherungen
- [Sicherung-Auslassungen](wiki:Template:Backup_Omissions/de) - was bei einer Sicherung nicht

{{-}}

#### Datenbankeinstellung

![[_media/EditPreferences-FamilyTree-tab-DatabaseSetting-section-default-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menu:  - „Stammbaum“ – Registerkarte – Abschnitt „Datenbankeinstellungen“ – Standardeinstellungen]]

- \-

  - **[SQLite](wiki:De:Gramps_Glossar#SQLite)** (*Standard*) - das [DB-API-Datenbank-Backend](wiki:DB-API_Database_Backend)
  - ... Wenn andere Datenbank-Backend-Zusatzmodule installiert sind, werden sie der Liste hinzugefügt <abbr title="exempli gratia - Lateinische Phrase, die 'zum Beispiel' bedeutet">e.g.</abbr>: [PostgreSQL](wiki:Addon:PostgreSQL) backend

Siehe auch:

- Erweiterung [PostgreSQL](wiki:Addon:PostgreSQL) - Dies fügt experimentelle Unterstützung für PostgreSQL-Datenbanken hinzu. Nur für Experten empfohlen!

{{-}}

#### Datenbankspeicherort

![[_media/EditPreferences-FamilyTree-tab-DatabaseLocation-section-default-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menü:  - Registerkarte „Stammbaum“ - Abschnitt „Speicherort der Datenbank“ - Standardeinstellungen]]

- \- Serveradresse oder andere Computer-IP-Adresse für den Speicherort der Datenbank.

- \- Portnummer für den Zugriff auf die Host-Datenbank

-   
  Sofern du keinen konkreten Grund hast, dies zu ändern, solltest du den Standardpfad beibehalten. Der Standardpfad, in dem Datenbanken gespeichert werden, ist `grampsdb` im [Anwenderverzeichnis](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Anwenderverzeichnis).

{{-}}

#### Verwaltung der Datensicherung

![[_media/EditPreferences-FamilyTree-tab-BackupManagement-section-default-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menü:  - Registerkarte „Stammbaum“ - Abschnitt „Sicherungsverwaltung“ - Standardeinstellungen]]

- \- Speicherort, an dem deine Gramps-Sicherung-Archivdateien gespeichert werden.

- \- Wenn du diese Option wählst, wird dein Stammbaum gesichert, wenn Gramps beendet wird. Die Datei wird im oben angegebenen Sicherungspfad gespeichert. Der Dateiname der Sicherung entspricht dem Familienstammbaum, an den ein Datum und eine Uhrzeit angehängt sind.

- Timer-Intervall zum Auslösen vollständiger Sicherungen während Gramps-Bearbeitungssitzungen.

  - **Nie** (*Standard*)
  - Alle 15 Minuten
  - Alle 30 Minuten
  - Jede Stunde
  - Alle 12 Stunden
  - Jeden Tag

{{-}}

#### Medienpfad des Stammbaums

![[_media/EditPreferences-FamilyTree-tab-FamilyTreesMediaPath-section-default-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menü:  - Registerkarte „Stammbaum“ - Abschnitt „Medienpfad des Stammbaums“ - Standardeinstellungen]]

-   
  Hier kannst du das Basisverzeichnis für die Medienobjekte eintragen.

  - Das Anklicken der Schaltfläche aktiviert den Dialog, wo Du den erforderlichen Pfad auswählen kannst.

Siehe auch:

- [](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Werkzeuge#Medienverwaltung) eine Gruppe von vier einzelnen Werkzeugen, von denen zwei es dir ermöglichen:
  - 

  - 

{{-}}

##### Medienverzeichnis auswählen-Dialog

Siehe [Dateiauswahl](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Einstellungen#Dateiauswahl) {{-}}

##### Fehlendes Medienobjekt-Symbol für einen "defekten Link" in Form eines Kästchens mit einem roten "x

![[_media/BrokenMediaPath-example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Medienobjekt mit fehlerhaftem Dateipfad]]

Wenn in der Vorschau der Miniaturansichten das Symbol für einen "defekten Link" in Form eines Kästchens mit einem roten "x" angezeigt wird, musst du den für deinen Stammbaum im Abschnitt {man label\|[Medienpfad des Stammbaums](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Einstellungen#Medienpfad_des_Stammbaums)}} korrigieren.

Siehe auch:

- Example.gramps - [Verbindung zu den Beispiel-Medienobjekten herstellen](wiki:Example.gramps#Connecting_to_the_example_Media_Objects)
- [Medien Überprüfen-Wekzeug](wiki:Addon:Media_Verify_Tool) Erweiterungswerkzeug zur erneuten Überprüfung von Medienpfaden

{{-}}

### Importieren

![[_media/EditPreferences-Import-tab-default-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menü: &quot;Bearbeiten&gt;Einstellungen...&quot; - &quot;Importieren&quot; - Registerkarte - Standardeinstellungen]] Die Registerkarte besteht aus den folgenden zwei Abschnitten:

- 

- 

#### Etikett Datensätze

-   
  Kontrollkästchen (Standard: `Imported %Y/%m/%d %H:%M:%S` ) Kontrollkästchen (Standard: `Importiert %Y/%m/%d %H:%M:%S` ) **Hinweis - Das Hinzufügen eines mit einem Zeitstempel versehenen [Etiketts](wiki:De:Gramps_Glossar#tag) beim Import kann das Importieren deiner Daten erheblich verlangsamen, ist aber für die anschließende Datenbereinigung hilfreich.**

#### Quelle GEDCOM-Import

-   
  Dieses Kontrollkästchen wirkt sich auf den Import von [GEDCOM-Daten](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Stammbäume_Verwalten#GEDCOM_Import) aus. Wenn diese Option aktiviert ist, enthält jedes importierte Element einen [Quellenverweis](wiki:De:Gramps_Glossar#Quelle) auf die importierte Datei. **Hinweis - Das Hinzufügen einer Standardquelle kann das Importieren der GEDCOM-Daten erheblich verlangsamen, ist aber für die anschließende Datenbereinigung hilfreich.3**

{{-}}

### Grenzwerte

![[_media/EditPreferences-Limits-tab-default-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menü: "Bearbeiten&gt;Einstellungen..." - "Grenzen" - Registerkarte - Standardeinstellungen]]

Einstellungen für Berechnungen von Daten, Alter und Generationen.

Siehe auch:

- [Gramps 6.0 Wiki Handbuch - Vermutlich lebend](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Vermutlich_lebend)
- [Daten bearbeiten](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Daten_eingeben_und_bearbeiten:_Ausführlich_-_Teil_1#Daten_bearbeiten)
- Manuelle Einstellung der [Datumsannäherung .ini](wiki:Match_dates#Changing_after.2Fbefore.2Fabout_range) (englisch)

#### Berechnungsgrenzen

- Standardeinstellung: `50`

  - Legt die Anzahl der Jahre +/- ab dem Ereignisdatum "`um `<Datum>" fest, die das Ereignis als gültig für einen Filter zurückgibt.
  - Wird für die Berechnung des Alters der Person verwendet.

- Standardeinstellung: `50`

  - Legt die Anzahl der Jahre nach dem Ereignisdatum "`nach `<Datum>" fest, die das Ereignis als gültig für einen Filter zurückgibt.
  - Wird für die Berechnung des Alters der Person verwendet.

- Standardeinstellung: `50`

  - Legt die Anzahl der Jahre vor dem Ereignisdatum "`vor `<Datum>" fest, die das Ereignis als gültig für einen Filter zurückgibt.
  - Wird für die Berechnung des Alters der Person verwendet.

- Standardeinstellung: `110`

  - In Ermangelung eines Todesereignisses ist dies das Alter, in dem Gramps die Person als nicht mehr lebend betrachtet.

- Standardeinstellung: `20`

- Standardeinstellung: `13`

- Standardeinstellung: `20`

- Du kannst die Anzahl der Generationen eingeben, die zur Bestimmung der Beziehungen verwendet werden. Der Standardwert ist **`15`**. Schränkt den Umfang der Funktionen auf der Grundlage des [Verwandtschaftsrechner](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Werkzeuge#Verwandtschaftsrechner) ein.

{{-}}

### Farben

![[_media/EditPreferences-Colors-tab-default-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menü: "Bearbeiten &gt; Einstellungen..." - "Farben" - Registerkarte - Standardeinstellungen]]

Diese Registerkarte enthält sieben Abschnitte, in denen du die **Farben, die für die Felder in den grafischen Ansichten verwendet werden** einstellen kannst.

Jede der Farben kann mit dem angepasst werden.

#### Farben für Felder in den grafischen Ansichten

Du kannst wählen die

- - **Helle Farben** (Standardeinstellung)
  - *Dunkle Farben*
    - \- stellt die Standardfarben des Themas wieder her.

#### Farben für männliche Personen

- \[ \] \#b8cee6

- \[ \] \#1f4986

- \[ \] \#b8cee6

- \[ \] \#000000

#### Farben für weibliche Personen

- \[ \] \#feccf0

- \[ \] \#861f69

- \[ \] \#feccf0

- \[ \] \#000000

#### Farben für Personen, die weder männlich noch weiblich sind

- \[ \] \#94ef9e

- \[ \] \#2a5d16

- \[ \] \#94ef9e

- \[ \] \#000000

#### Farben für unbekannte Personen

- \[ \] \#f3dbb6

- \[ \] \#8e5801

- \[ \] \#f3dbb6

- \[ \] \#000000

#### Farben für Familienknoten

- \[ \] \#eeeeee

- \[ \] \#cccccc

- \[ \] \#eeeeee

- \[ \] \#eeeeee

- \[ \] \#eeeeee

- \[ \] \#eeeeee

- \[ \] \#eeeeee

- \[ \] \#ff7373

#### Andere Farben

- \[ \] \#bbe68a

{{-}}

### Genealogische Symbole

![[_media/EditPreferences-GenealogicalSymbols-tab-default-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menü: „Bearbeiten &gt; Einstellungen...“ – „Genealogische Symbole“ – Registerkarte – Standardeinstellungen]]

Ermöglicht dir die Verwendung von genealogischen Symbolen anstelle von Textabkürzungen in Berichten, Diagrammen und der Gramps-Schnittstelle.

Diese Registerkarte gibt dir die Möglichkeit, eine Schriftart zu verwenden, die alle genealogischen Symbole darstellen kann. (Nach der Konfiguration siehe: [Voraussetzung für die Verwendung von genealogischen Symbolen](#Voraussetzung_f.C3.BCr_die_Verwendung_von_genealogischen_Symbolen))

Wenn du das Kontrollkästchen "" aktivierst, verwendet Gramps die ausgewählte Schriftart, sofern sie vorhanden ist.

Dies kann nützlich sein, wenn du in einer Notiz die Lautschrift hinzufügen möchtest, um zu zeigen, wie man einen Namen ausspricht, oder wenn du mehrere Sprachen mischst, wie z. B. Griechisch und Russisch. Du kannst das Todessymbol nur auf dieser Registerkarte konfigurieren.

  
Liste der angezeigten genealogischen Symbole (aufgelistet in der Reihenfolge, wie sie unten im Screenshot zu sehen ist):

- Weiblich
- Männlich
- Asexualität, geschlechtslos
- Lesbisch
- Männliche Homosexualität
- Heterosexuell
- Intergeschlechtlichkeit, Zwitter in der Insektenkunde
- Transgender
- Neutrois

<!-- -->

- Illegitim
- Geboren
- Getauft
- Verlobt
- Verheiratet
- Geschieden
- Uneheliche/freie Verbindung
- Begraben
- Eingeäschert/Bestattungsurne
- Gefallen
- Ausgestorben

<!-- -->

- Gestorben

{{-}}

| Bedeutung | Symbol | Unicode-Codepunkt(e) | Name |
|----|----|----|----|
| männlich | ♂ | U+2642 | Marssymbol |
| weiblich | ♀ | U+2640 | Venussymbol |
| unbekannt | ⚪︎ | U+26AA | Kern der anderen Gendersymbole |
| Intergeschlechtlichkeit | ⚥ | U+26A5 | Eine Kombination aus Venus- und Marssymbol |
| Neutrois | ⚲ | U+26B2 | Ein Kreis und ein Strich |
| geboren | \* | U+002A | Asterisk |
| getauft | ~ | U+007E | Tilde |
| gestorben | ✝︎ | U+271D | Lateinisches Kreuz |
| begraben | ⚰︎ | U+26B0 | Sarg |
| eingeäschert | ⚱︎ | U+26B1 | Bestattungsurne |
| tot geboren | ✝︎\* | U+271d U+002A | Lateinisches Kreuz, Asterisk |
| außereheliche Geburt | (\*) | U+0028 U+20DD U+0029 | Asterisk in runden Klammern |
| außereheliche Geburt | ⊛ | U+229B | Eingekreister Stern-Operator |
| gefallen | ⚔︎ | U+2694 | Gekreuzte Schwerter |
| diese Linie ausgestorben | ‡ | U+2021 | Doppelter Dolch |
| Ungefähr(1J) | ± | U+00B1 | Plus-Minus |
| vor | \< | U+003C | Kleiner-als-Zeichen |
| nach | \> | U+003E | Größer-als-Zeichen |
| verlobt | ⚬ | U+26AC | Mittlerer kleiner weißer Kreis |
| verheiratet | ⚭ | U+26AD | Symbol der Ehe |
| geschieden | ⚮ | U+26AE | Scheidung-Symbol |
| uneheliche/freie Verbindung | ⚯ | U+26AF | Symbol für unverheiratete Partnerschaft |

{{-}}

#### Voraussetzung für die Verwendung von genealogischen Symbolen

![[_media/EditPreferences-GenealogicalSymbols-tab-default-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Genealogische Symbole" - Registerkarte Einstellungen - Standardeinstellungen]]

##### Ersteinrichtung

Wenn die fontconfig-[Voraussetzung installiert wurde](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Einstellungen#Voraussetzung), wähle auf der Registerkarte die Schaltfläche , Gramps wird versuchen, alle geeigneten Unicode-Textschriften zu finden, die verwendet werden können.

![[_media/EditPreferences-GenealogicalSymbols-FindFont-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Genealogische Symbole" - Schriftarten finden]]

Wenn die Suche abgeschlossen ist, wähle eine der Schriftarten aus der Liste und aktiviere das Kontrollkästchen:

##### Voraussetzung

Voraussetzung : **python-fontconfig** : Python-Bindungen von fontconfig und seinen Abhängigkeiten sind für die Anzeige genealogischer Symbole erforderlich

Siehe auch:

- Tamura Jones führt aus [Genealogical Symbols](https://www.tamurajones.net/GenealogySymbols.xhtml) *(der Abschnitt "Unicode" ist besonders wichtig)*
- [GEPS 039: Genealogische Symbole in Gramps](wiki:GEPS_039:_Genealogical_symbols_in_gramps)
- Anfrage für eine Funktion: Gramps sollte die Genealogie-Symbole überall verwenden können.
- [Passe die Nachschlagetabelle für genealogische Symbole an](wiki:Customize_the_Genealogical_Symbols_lookup_table), die sich im [Benutzerverzeichnis von Gramps](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Anwenderverzeichnis#MS_Windows) befindet: [gramps\gen\utils\symbols.py](https://github.com/gramps-project/gramps/blob/maintenance/gramps51/gramps/gen/utils/symbols.py)

{{-}}

### ID-Formate

![[_media/EditPreferences-IDFormats-tab-default-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menü: "Bearbeiten &gt; Einstellungen..." - "ID-Formate" - Registerkarte - Standardeinstellungen]]

Diese Registerkarte enthält Einstellungen, die für die automatische Generierung von Gramps-IDs relevant sind.

-   
  Stellt die Vorlage zum Generieren von IDs für eine Person bereit. Standardwert: `I%04d`

-   
  Stellt die Vorlage zum Generieren von IDs für eine Familie bereit. Standardwert: `F%04d`

-   
  Stellt die Vorlage zum Generieren von IDs für einen Ort bereit. Standardwert: `P%04d`

-   
  Stellt die Vorlage zum Generieren von IDs für eine Quelle bereit. Standardwert: `S%04d`

-   
  Stellt die Vorlage zum Generieren von IDs für eine Fundstelle bereit. Standardwert: `C%04d`

-   
  Stellt die Vorlage zum Generieren von IDs für ein Medienobjekt bereit. Standardwert: `O%04d`

-   
  Stellt die Vorlage zum Generieren von IDs für ein Ereignis bereit. Standardwert: `E%04d`

-   
  Stellt die Vorlage zum Generieren von IDs für einen Aufbewahrungsort bereit. Standardwert: `R%04d`

-   
  Stellt die Vorlage zum Generieren von IDs für eine Notiz bereit. Standardwert: `N%04d`

Du kannst das [Gramps-IDs neu ordnen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Werkzeuge#Gramps-IDs_neu_ordnen)-Werkzeug verwenden, um das Format zu ändern. {{-}}

### Text

![[_media/EditPreferences-Text-tab-default-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menü: "Bearbeiten &gt; Einstellungen..." - "Text" - Registerkarte - Standardeinstellungen]]

Diese Registerkarte enthält einen Abschnitt mit Einstellungen, die sich darauf beziehen, wie fehlende und vertrauliche Namen und Datensätze angezeigt werden sollen.

#### Bedingte Textersetzungen

- In diesem Eingabefeld kannst du bestimmen, wie ein fehlender Familienname angezeigt werden soll. Der Standardwert ist **`[Fehlender Nachname]`**. Du kannst hier \[--\] eingeben oder was immer du als passend erachten.

- In diesem Eingabefeld kannst du bestimmen, wie ein fehlender Vorname angezeigt werden soll. Der Standardwert ist **`[Fehlender Vorname]`**. Du kannst diesen Wert beliebig verändern.

- Standardwert: `[Fehlender Datensatz]`

- Standardwert: `[Lebt]`

- Standardwert: `[Lebt]`

- Standardwert: `[Vertraulicher Datensatz]`

{{-}}

### Warnungen

![[_media/EditPreferences-Warnings-tab-default-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menu: "Bearbeiten &gt; Einstellungen..." - "Warnungen" - Registerkarte - Standardeinstellungen]]

Diese Registerkarte enthält einen Abschnitt , der die Anzeige von Warnungsdialogen steuert und die erneute Aktivierung von deaktivierten Dialogen ermöglicht.

Siehe die [Referenz für Fehler und Warnungen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Fehler_und_Warnung_Referenz) Seite für Beispiele.

#### Warnungen und Fehlermeldungen

- Kontrollkästchen standardmäßig deaktiviert (Siehe [Dialog](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Fehler_und_Warnung_Referenz#Warnung_unterdr.C3.BCcken_wenn_zu_einem_Kind_Eltern_hinzugef.C3.BCgt_werden))

- Kontrollkästchen standardmäßig deaktiviert (Siehe [Dialog](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Fehler_und_Warnung_Referenz#Warnung_unterdr.C3.BCcken_wenn_mit_ge.C3.A4nderten_Daten_abgebrochen_wird))

- Kontrollkästchen standardmäßig deaktiviert (Siehe [Dialog](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Fehler_und_Warnung_Referenz#Warnungen_unterdr.C3.BCcken_bei_fehlendem_Forscher_beim_Export_nach_GEDCOM))

- Kontrollkästchen standardmäßig deaktiviert

- Kontrollkästchen standardmäßig deaktiviert (Siehe [Dialog](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Fehler_und_Warnung_Referenz#Modul_nicht_geladen_Warnungen))

{{-}}

### Forscher

![[_media/EditPreferences-Researcher-tab-default-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menü: "Bearbeiten &gt; Einstellungen..." - "Informationen zum Forscher" - Registerkarte - Standardeinstellungen]]

Ermöglicht es dir, , in die entsprechenden Texteingabefelder einzutragen. Obwohl Gramps Informationen über dich abfragt, verwendet Gramps diese Informationen nur um gültige GEDCOM Dateien zu erstellen. Eine gültige GEDCOM Datei erfordert Informationen über den Ersteller. Wenn du willst, kannst du diese Felder leer lassen, allerdings ist dann keine exportierte GEDCOM Datei gültig.

Die verfügbaren Texteingabefelder sind (standardmäßig sind alle Felder leer):

-   

-   

-   

-   

-   

-   

-   

-   

-   

Die Informationen, die unter dieser Präferenz eingegeben werden dienen als Standardwerte für stammbaumspezifische Werte die mit dem Werkzeug angepasst werden können. {{-}}

## Andere Einstellungen

Neben dem Dialog gibt es noch andere Einstellungsmöglichkeiten in Gramps. Aus mehreren Gründen wurden sie leichter zugänglich gemacht, wie unten aufgeführt. {{-}}

### Spalteneditor

![[_media/ColumnsEditorTab-dialog-example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} <strong>Spalten</strong> Editor-Registerkarte – Dialogfeld – Personenbaumansicht – Standardspalten]]

Die Spalten der Listenansichten können in einem -Editor Dialog hinzugefügt, entfernt oder umsortiert werden.

Um den -Editor Dialog für die aktuelle Ansicht zu verwenden, wähle über das Menü , klicke auf die Schaltfläche ![[_media/Gramps-config.png]] in der Symbolleiste oder drücke die [Tastenkombination](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Tastenkürzel_Referenz#Allgemeine_K.C3.BCrzel) *Aktive Ansicht konfigurieren*.

Nur aktivierte Spalten werden in der Ansicht angezeigt. Um ihre Reihenfolge zu ändern, ziehe die Spalten an die gewünscht Position innerhalb des Editors ([*Drag and Drop*](https://de.wikipedia.org/wiki/Drag_and_Drop)). Wenn du die gewünschten Änderungen durchgeführt hast, klicke auf und dann um den Editor zu beenden und die Änderungen in der Ansicht zu sehen.

Standardmäßig zeigt die Ansicht Liste mehrere Spalten mit Informationen über die jeweilige Kategorie an. Du kannst der Anzeige Spalten hinzufügen oder entfernen

Der Standardsortierschlüssel für die Ansicht \[immer aufsteigend\] ist das Feld ganz links \[d. h. oben im Spalteneditor\], so dass eine Änderung des Feldes an dieser Position die Standardsortierung beeinflusst. Bei einigen Ansichten kann das erste Feld nicht geändert werden. Der Grund dafür wird oben im Spalteneditor angegeben.

Der Dialog enthält für jede Kategorie der Ansicht, die eine einfache Tabelle anzeigt, eine andere Auswahl an Spalten.

Die Änderungen werden erst wirksam, wenn du auf die Schaltfläche klickst.

Nach der Änderung der Ansichtsspalten wird durch einmaliges Klicken auf die Spaltenüberschrift in aufsteigender Reihenfolge sortiert, durch erneutes Klicken in absteigender Reihenfolge sortiert.

Die Untergruppe der Spalten und die aktuellen [Filter](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Filter) schränken auch die Daten ein, die über die Operation exportiert werden. Ausgeblendete Spalten und Datensätze werden nicht exportiert. {{-}}

### Spalten sortieren

![[_media/PersonView-PeopleListView-example-with-context-menu-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} <strong>Vor</strong> - Standardsortierung nach Spalte „Name“ „Personen“ Kategorie – „Personen“ Ansicht (Liste)]]

![[_media/PeopleCategory-PeopleListView-SortedByBirthDateColumn-example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} <strong>Nach</strong> - Sortierung nach der Spalte "Geburtsdatum" im Listenmodus der Personenkategorieansicht - Beispiel]]

Standardmäßig werden in jeder Kategorieansicht, die Daten in einem spaltenförmigen Tabellenlayout darstellt, die Zeilen in aufsteigender Reihenfolge auf der Grundlage der Daten in der ersten (ganz linken) Spalte sortiert. Wenn die Tabelle gruppierte Zeilen hat, werden die gruppierten Daten untersortiert. *(Tabellen in Untergruppen von Daten mit Registerkarten, Editoren und Selektoren funktionieren ähnlich.)*

Klicke einmal auf eine andere Spaltenüberschrift, um nach den Daten dieser Spalte in aufsteigender Reihenfolge zu sortieren. Klicke erneut auf die Überschrift, um in umgekehrter Reihenfolge zu sortieren.

Mit dem Dialogfeld kannst du die angezeigten Spalten hinzufügen, entfernen und neu anordnen. Wenn du eine andere erste Spalte auswählst, wird diese zur neuen Standardsortierspalte der Ansicht \[allerdings immer aufsteigend\]. {{-}}

### Hauptperson setzen

![[_media/MenuEdit-SetHomePerson-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menü zeigt <em>Hauptperson setzen</em>]]

Um die [Haupttperson](wiki:De:Gramps_Glossar#Haupttperson) festzulegen, wähle die Personenkategorie und die gewünschte Person aus, um sie zur [aktiven Person](wiki:De:Gramps_Glossar#aktiven_Person) zu machen, und wähle dann über die Menüs .

Alternativ kannst du bei der Bearbeitung einer Person mit der rechten Maustaste auf inaktive Bereiche (Bereiche ohne Texteingabefeld) des oberen Abschnitts klicken, um ein Kontextmenü aufzurufen, das die Option für dieses Profil enthält.

Die Hauptperson ist die ständig benannte Person, die zur [aktiven Person](wiki:De:Gramps_Glossar#aktive_Person) wird, wenn einer der folgenden Fälle eintritt:

- Wenn die Stammbaum-Datenbank geöffnet wird, ist standardmäßig  
  *(Die Einstellung [Allgemeines](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Einstellungen#Allgemeine_Gramps_Einstellungen) in den [Einstellungen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Einstellungen#Einstellungen) kann dieses Standardverhalten ändern. Die Einstellung "Zuletzt angezeigte Ansicht merken" führt zur letzten [aktiven Person](wiki:De:Gramps_Glossar#aktive_Person) der vorherigen Sitzung zurück.)*
- Wenn die Schaltfläche in der Symbolleiste angeklickt wird
- Wenn der Menüpunkt Anfang entweder im Menü oder im Kontextmenü der rechten Maustaste in ausgewählten Ansichten ausgewählt wird
- Das [Tastenkürzel](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Tastenkürzel_Referenz) verwendet wird um zu der **Hauptperson** zurückzukehren.

Die Schaltfläche der Werkzeugleiste ist in den Kategorien „Personen“, „Beziehungen“ und „Diagramme“ verfügbar. ![[_media/Gramps_Go-Home48x48_win.png]]

#### Siehe auch

- [Die Hauptperson setzen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Navigation#Die_Hauptperson_setzen)

{{-}}

### Ansicht Bedienelemente festlegen

Ob die Werkzeugleiste, die Seitenleiste oder der Filter (nicht verfügbar in den Diagramm- und Beziehungsansichten) im Hauptfenster angezeigt werden, wird über das Menü Ansicht eingestellt.

In den verschiedenen Ansichten zeigt klicken auf das Menü vier Kontrollkästchen die du anklicken kannst:

- 

- 

- 

- 

- 

Zusätzlich, abhängig von der Ansicht, in der du dich befindest, sind andere Optionen unter verfügbar.

- Gramplets:
  - Spalten auf 1 setzen
  - Spalten auf 2 setzen
  - Spalten auf 3 setzen
- Beziehungen:
  - Zeige Geschwister
  - Zeige Details
- Geographie:
  - Zeitraum
  - Layout

Alle anderen Ansichten: der [Spalteneditor](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Einstellungen#Spalteneditor).

### Ansicht exportieren

![[_media/Menubar-FamilyTrees-overview-FamilyTree-Loaded-example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menüleiste - "Stammbäume" - Übersichtsbeispiel mit dem Menüeintrag "Exportansicht".]]

Bei den meisten [Kategorie-Listen-Ansichten](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Kategorien#Kategorien_des_Navigator) können die angezeigten Daten exportiert werden, wähle dazu den [Menübefehl](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Navigation#Hauptmen.C3.BCs) .

Dieser Menübefehl erscheint nur, wenn die angezeigten Daten exportiert werden können. Gramps exportiert die Daten auf dem Bildschirm nach Ihrer Wahl: **CSV** oder **Open Document** Tabellenkalkulationsformat.

Beachte, dass die aktuelle Konfiguration der Spalten in der Ansicht bestimmt, welche Daten exportiert werden. Der Export enthält nur die angezeigten Spaltendaten (in derselben Reihenfolge) und beschränkt sich auf Datensätze, die den von dir angewandten [Filtern](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Filter) entsprechen.

Verwende die Ansichten Registerkarte [CSV-Dialekt](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Einstellungen#CSV_Dialekt), um den Typ der zu erstellenden CSV-Datei festzulegen. {{-}}

#### Ansicht als Tabelle exportieren Dialog

![[_media/ExportViewAsSpreadsheet-CSV-file-dialog-example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Ansicht als Tabelle exportieren" CSV(Standardeinstellung)-Dateiart - Dialog - Beispiel]]

Gramps zeigt dann das Dialogfeld an, in dem du einen Speicherort und einen Dateinamen für deine Datei auswählen und die Daten aus der Kategorielistenansicht in einem von zwei Tabellenformaten exportieren kannst:

- - **CSV** (Standardeinstellung)
  - **OpenDocument Tabelle** - ODS Format.

{{-}} ![[_media/ExportViewAsSpreadsheet-ODS-Displayed-in-LibreOfficeCalc-example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Beispiel einer ODS-Tabelle - angezeigt in LibreOffice Calc]]

Der Beispiel-Screenshot zeigt einen Export in das **OpenDocument Tabellenblatt** (ODS-Format), das als Tabellenblatt in LibreOffice Calc angezeigt wird.

{{-}}

#### CSV Dialekt

![[_media/CSV-Dialect-Tab-dialog-example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "CSV Dialekt" Registerkarte – Dialogfeld – Beispiel]]

Alle Ansichten von Listentabellen haben eine Registerkarte CSV-Dialekt im Dialog des Menüs Du kannst das Trennzeichen des CSV-Formats auswählen, das beim Exportieren und Importieren von Daten in Gramps verwendet werden soll.

„Wähle deinen Dialekt“ aus:

- 

- 

- 

- - Begrenzungszeichen:
    - ',' *Komma* (Standard)
    - ';' *Semikolon*
    - ':' *Doppelpunkt*
    - '\|' *Senkrechter Strich (Pipe)*
    - 'Tab'

CSV steht für **[Komma-getrennte Werte](https://de.wikipedia.org/wiki/CSV_(Dateiformat))**. Es ist ein einfaches Textdateiformat, das Daten in Spalten und Zeilen aufteilt, um den Datenaustausch zu vereinfachen. Ursprünglich waren die Daten durch die Trennung in Spalten durch feste Positionen in `.txt`-Textdateien begrenzt. Als mehr Flexibilität benötigt wurde, wählte man das Komma als Trennzeichen, um die Grenzen der Spalten zu markieren, und das `.csv`-Format einer Textdatei wurde eingeführt. Erschwerend kam hinzu, dass die verschiedenen Betriebssysteme das Ende einer Zeile und das Ende einer Datei mit unterschiedlichen Begrenzungscodes markierten.

Als das Komma in den Daten selbst zu häufig benötigt wurde, setzte sich das `.tsv`-Dateiformat (tab-separated-values) durch. Als man begann, andere Begrenzungszeichen zu verwenden, um nicht noch mehr Dateierweiterungen zu verbrauchen, wurde CSV zum Synonym für jedes Textformat mit durch Begrenzungszeichen markierten Spalten. Es handelte sich lediglich um verschiedene „Dialekte“ von „CSV“.

Das [`csv`-Modul von Python](https://docs.python.org/3/library/csv.html) bietet mehrere vordefinierte Dialekte, um das Lesen und Schreiben von CSV-Dateien zu vereinfachen. Diese Dialekte legen Regeln für das Analysieren und Formatieren von Daten fest. Zu den Standarddialekten gehören , und . Die folgenden Abschnitte beschreiben die Merkmale der einzelnen Dialekte, einschließlich ihrer Trennzeichen, Zeilenendezeichen und Anführungszeichen.

##### Excel-Dialekt

Der -Dialekt wurde entwickelt, um mit CSV-Dateien kompatibel zu sein, die von Microsoft Excel erzeugt wurden. Er ist für Daten geeignet, die von Excel als kommagetrennte Werte gespeichert wurden.

- Trennzeichen:\*\* Komma (`,`\`)
- Zeilenabschlußzeichen: Wagenrücklauf und Zeilenvorschub (`\r\n`)
- Anführungszeichen:
  - Doppelte Anführungszeichen (`"`) werden verwendet, um Felder einzuschließen, die das Trennzeichen oder andere Sonderzeichen enthalten.
  - Um ein doppeltes Anführungszeichen in ein in Anführungszeichen gesetztes Feld einzuschließen, wird es durch Verdoppelung maskiert (z. B. `""Beispiel""`).

##### Excel-Tabellen-Dialekt

Der -Dialekt ähnelt dem \`excel\`-Dialekt, verwendet jedoch Tabulatoren anstelle von Kommas als Trennzeichen. Dieses Format wird häufig verwendet, wenn Zelldaten aus Excel in die Zwischenablage des Betriebssystems kopiert werden. Das Einfügen von Tabulator-getrennten Daten in das [Textimport](wiki:Addon:Import_Text_Gramplet)-Zusatzmodul-Gramplet ist eine der schnellsten Methoden, um Teile des Baums zu füllen.

- Trennzeichen: Tabulator (`\t`)
- Zeilenabschlußzeichen: Wagenrücklauf und Zeilenvorschub (`\r\n`)
- Anführungszeichen:
  - Doppelte Anführungszeichen (`"`) werden verwendet, um Felder einzuschließen, die das Trennzeichen oder andere Sonderzeichen enthalten.
  - Um ein doppeltes Anführungszeichen in ein in Anführungszeichen gesetztes Feld einzuschließen, wird es durch Verdoppelung maskiert (z. B. `""Beispiel""`).

##### Unix-Dialekt

Der -Dialekt ist für die Verwendung in Unix-ähnlichen Umgebungen konzipiert. Er verwendet ein Zeilenvorschubzeichen als Zeilenende und setzt alle Felder immer in Anführungszeichen.

- Trennzeichen: Komma (`,`)
- Zeilenabschlußzeichen: Zeilenvorschub (`\n`)
- Anführungszeichen:
  - Alle Felder werden in doppelte Anführungszeichen (`"`) gesetzt.
  - Um ein doppeltes Anführungszeichen in ein in Anführungszeichen gesetztes Feld einzuschließen, wird es durch Verdoppelung maskiert (z. B. `""Beispiel""`).

##### Siehe auch:

- [CSV: Möglichkeit zur Auswahl des Dialekts. \#1314](https://github.com/gramps-project/gramps/pull/1314)

{{-}}

### Modularität und Zusatzmodule

Gramps wurde für Erweiterungen konzipiert. Das Zusatzmodul-Framework (auch bekannt als Plugin, Addon, Extension) bietet einen Pfad für die Entwicklung von Drittanbietern außerhalb der normalen Gramps-Veröffentlichungen.

Die Dokumentation für jedes Zusatzmodul wird außerhalb des Rahmens dieser Haupt-Wikikapitel gepflegt. Die Benutzeroberfläche und die Funktionalität der Software und der Dokumentation entsprechen möglicherweise nicht dem Stil, der im Rest von Gramps zu sehen ist... obwohl wir die Entwickler ermutigen, zu versuchen, ihre Ergänzungen so nahtlos wie möglich zu gestalten.

Eine kurze Beschreibung und ein Bildschirmfoto zu jedem Zusatzmodul findest du im Abschnitt [Zusatzmodul-Liste](wiki:6.0_Addons#Addon_List) im Wiki-Handbuch. Die separat gepflegte Dokumentationsseite für das Zusatzmodul ist mit der ersten Spalte dieser Liste verlinkt.

Siehe [Zusatzmodulverwaltung](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Zusatzmodulverwaltung) und [Zusatzmodule von Drittanbietern](wiki:6.0_Addons). {{-}}

### Berichtausgabeformate anpassen

![[_media/TextReports-DocumentOptions-section-PlainText-output-settings-example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Dokumentoptionen - Registerkarte Vorgaben für Textberichte (Einfacher Text - Ausgabe ausgewählt) Beispiel]]

Welche Art der Anpassung der Ausgabe ist möglich? In diesem Dialogfeld kannst du die Schriftarten, Schriftgrößen, Schriftfarbe, Hintergrundfarbe des Textes und die Ausrichtung der Absätze im Bericht ändern.

Bei den meisten Berichtsdialogfeldern befinden sich im oberen Teil Optionsregisterkarten, die sich speziell auf den jeweiligen Bericht beziehen. Der untere Teil enthält allgemeiner wiederverwendbare Funktionen und wird als Abschnitt bezeichnet.

Aus der Dropdown-Liste kannst du einen vorhandenen benutzerdefinierten auswählen. Oder du erstellst deine eigene Formatvorlage: Wähle die Schaltfläche , um das Dialogfeld anzuzeigen, und wähle dann die Schaltfläche , um das Dialogfeld anzuzeigen.

{{-}}

#### Dokumentenstile Editor Dialog

![[_media/DocumentStyles-dialog-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Dokumentstile - Dialog - Standardeinstellung]]

Das Dialogfeld listet die *Standardvorlage* und alle benutzerdefinierten Vorlagen für diesen Bericht auf und ermöglicht es dir, benutzerdefinierte Vorlagen, die du erstellt hast, zu bearbeiten oder zu löschen. Wähle die Schaltfläche , um das Dialogfeld anzuzeigen. {{-}}

#### Stileditor Dialog

![[_media/StyleEditor-dialog-Description-tab-example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Registerkarte „Beschreibungsoptionen“ – Dokumentstile – Dialogfeld – Standardstile für Ahnentafelbericht]]

Im Dialogfeld kannst du den Dokumentstil für jeden Bericht individuell anpassen.

Ändere das Feld `Neues Format` (Voreinstellung) in einen eindeutigen Namen, wie er in der Dropdown-Liste der erscheinen wird.

Sobald die Änderungen für deinen benutzerdefinierten Stil abgeschlossen sind, wähle die Schaltfläche , um die Änderungen zu speichern, oder , um den Vorgang zu beenden.

##### Stileditor Dialog Registerkarten

Auf der linken Seite befindet sich die Spalte , in der die für den jeweiligen Bericht spezifischen Absatzoptionen aufgeführt sind, die du ändern kannst. Zum Beispiel zeigt der die Stiloptionen für `AHN-Entry`, `AHN-Generation` und `AHN-Title`.

Auf der rechten Seite befinden sich drei Registerkarten, die mit jedem in der linken Spalte aufgeführten Stil verbunden sind:

- [Beschreibung](#Beschreibung)
- [Schriftoptionen](#Schriftoptionen)
- [Absatzoptionen](#Absatzoptionen)

{{-}}

###### Beschreibung

![[_media/StyleEditor-dialog-Description-tab-example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Registerkarte Beschreibungsoptionen - Dokumentstil - Dialog - Standardstile für Ahnentafel-Bericht]]

- Die Registerkarte „Beschreibung“ beschreibt, worum es in den einzelnen Abschnitten geht. Hier wird beispielsweise der Stil gezeigt, der für den Ahnentafelbericht ( `AHN-Entry` ) verwendet wird, mit der Beschreibung: „Der für die Textanzeige verwendete Grundstil.“

{{-}}

###### Schriftoptionen

![[_media/StyleEditor-dialog-FontOptions-tab-example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Schriftoptionen" Registerkarte - "Stileditor" Dialog für "Dokumentenstile" (Standardstile für Ahnentafel-Bericht)]]

- Auf der Registerkarte kannst du die , die , , und deines Stils festlegen.

{{-}}

###### Absatzoptionen

![[_media/StyleEditor-dialog-ParagraphOptions-tab-example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Absatzoptionen" Registerkarte - "Stileditor" Dialog für "Dokumentenstile" (Standardstile für Ahnentafel-Bericht)]]

- : Hier kannst du die , die , das , und deines Stil festlegen.

{{-}}

### Kontextmenü

![[_media/Clipboard-dialog-example-context-menu-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Zwischenablage – mit Beispiel für ein kontextabhängiges Popup-Menü, das durch einen Rechtsklick auf eine Familie angezeigt wird]] [Pop-up Menüs](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Hauptfenster#Pop-up_Men.C3.BCs) werden an verschiedenen Stellen in Gramps verwendet; wie du auf das Kontextmenü zugreifst, hängt von deinem Betriebssystem ab:

- In Microsoft Windows verwendet man in der Regel die rechte Maustaste, um das Kontextmenü einzublenden, oder die Tastenkombination +. siehe [Kontextmenüs verwenden - Microsoft Docs](https://docs.microsoft.com/en-us/previous-versions/windows/desktop/mpc/using-context-menus)
- Unter Apple macOS drückt man in der Regel die -Taste, während man mit der Maus auf die Schaltfläche klickt, um das Kontextmenü anzuzeigen. siehe: [Kontextbezogene Menüs - Menüs - macOS - Human Interface Guidelines - Apple Developer](https://developer.apple.com/design/human-interface-guidelines/macos/menus/contextual-menus/)

Liste der bekannten Kontextmenüs in Gramps:

- Kontextmenüs der Stammbaumansicht
- Kontextmenü der Zwischenablage
- Dateiauswahl – Kontextmenüoptionen
- Kontextmenüs der <Kategorieansicht>
- Buchverwaltungsdialog
- ... und viele mehr

Siehe auch:

- [Tastenkürzel Referenz](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Tastenkürzel_Referenz)

### Auswahldialoge

![[_media/wiki:De:Gramps_6.0_Wiki_Handbuch_-_Kategorien#Familie_w.C3.A4hlen_Auswahl|[_media/SelectFamily-SelectorDialog-example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} [Familienauswahl]] - mit Suchleiste]]

Auswahldialoge sind eine Kombination aus Kombinationsfeld und Dialogfeld, die in der Regel zur Auswahl eines Objekts (Person/Familie/Ereignisse usw.) verwendet werden. Verschiedene verfügen außerdem über Suchleisten:

- [Familienauswahl](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Kategorien#Familie_w.C3.A4hlen_Auswahl)
- [Ereignis wählen Auswahl](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Daten_eingeben_und_bearbeiten:_Ausführlich_-_Teil_1#Ereignis_w.C3.A4hlen_Auswahl)
- [Notiz wählen Auswahl](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Daten_eingeben_und_bearbeiten:_Ausführlich_-_Teil_1#Notiz_w.C3.A4hlen_Auswahl)
- [Person wählen Auswahl](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Daten_eingeben_und_bearbeiten:_Ausführlich_-_Teil_1#Person_w.C3.A4hlen_Auswahl)
- [Select a person for the report selector](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte_-_Teil_4#Eine_Person_f.C3.BCr_den_Bericht_w.C3.A4hlen_Auswahl)
- [Vater wählen Auswahl](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Daten_eingeben_und_bearbeiten:_Ausführlich_-_Teil_1#Vater_w.C3.A4hlen_Auswahl) (Sonderfall, gefiltert nach Vater?)
- [Mutter wählen Auswahl](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Daten_eingeben_und_bearbeiten:_Ausführlich_-_Teil_1#Mutter_w.C3.A4hlen_Auswahl) (Sonderfall, gefiltert nach Mutter?)
- [Kind wählen Auswahl](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Daten_eingeben_und_bearbeiten:_Ausführlich_-_Teil_1#Kind_w.C3.A4hlen_Auswahl)
- [Medien Objekt wählen Auswahl](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Daten_eingeben_und_bearbeiten:_Ausführlich_-_Teil_1#Medien_Objekt_w.C3.A4hlen_Auswahl)
- [Ort wählen Auswahl](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Daten_eingeben_und_bearbeiten:_Ausführlich_-_Teil_2#Ort_w.C3.A4hlen_Auswahl)
- [Aufbewahrungsort wählen Auswahl](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Daten_eingeben_und_bearbeiten:_Ausführlich_-_Teil_2#Aufbewahrungsort_w.C3.A4hlen_Auswahl)
- [Quelle oder Fundstelle wählen Auswahl](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Daten_eingeben_und_bearbeiten:_Ausführlich_-_Teil_2#Quelle_oder_Fundstelle_w.C3.A4hlen_Auswahl)
- [Quelle wählen Auswahl](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Daten_eingeben_und_bearbeiten:_Ausführlich_-_Teil_2#Quelle_w.C3.A4hlen_Auswahl)

{{-}} Siehe auch

- [GEPS_041: Neue Auswahl](https://gramps-project.org/wiki/index.php/GEPS_041:_New_Selector)
- [Farbe-Auswahl](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Einstellungen#Farbw.C3.A4hler)

## Anpassen

Hier sind einige Möglichkeiten, wie du Gramps anpassen kannst.

### Einstellungen

Im Abschnitt „Anzeigeoptionen“ der Registerkarte „Bearbeiten \> Einstellungen \> kannst du das auswählen, das standardmäßig in Gramps verwendet wird. Die Schaltfläche öffnet den Editor für Anzeigenamen, in dem du benutzerdefinierte (individuelle) Stile erstellen kannst, die über die vordefinierten (integrierten) Namensformatoptionen hinausgehen.

Siehe [Einstellungen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Einstellungen#Einstellungen)

Die Schaltfläche Bearbeiten für die bevorzugten und alternativen Namen einer Person öffnet den und ermöglicht die Auswahl eines Namensformats, das das auf der Registerkarte Anzeige der Einstellungen für den gesamten Baum gewählte Format überschreibt.

Das Namensformat, die Gruppierung und die Sortierung können für ausgewählte Personen und Nachnamen außer Kraft gesetzt werden. Der Dialog "Person bearbeiten" verfügt über zwei Schaltflächen für den Zugriff auf diese Funktion. Die Schaltfläche für den bevorzugten Namen befindet sich rechts neben dem Feld Suffix. Für jeden ausgewählten Namen (bevorzugter oder alternativer Name) auf der Registerkarte Namen, die den Namenseditor öffnet. Die integrierten und benutzerdefinierten Anzeigeformate für Namen können ausgewählt werden, mit Ausnahme der Optionen "Gruppieren als:" und "Sortieren als:", die standardmäßig das in den Einstellungen ausgewählte Namensformat verwenden.

### Farbwähler

Auf der Registerkarte [Farben](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Einstellungen#Farben) der Voreinstellungen kannst du die Farbe der verschiedenen Diagrammelemente in den grafischen Ansichten der Kategorie Diagramme anpassen.

#### Farbpalette

![[_media/PickAColor-selector-dialog-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;Farbe auswählen&quot; - Palettenauswahldialog]] Wähle eine Farbe aus den 45 [Musterfeldern](wiki:De:Gramps_Glossar#swatch) der vordefinierten Farbpalette aus. Oder wähle aus den kürzlich verwendeten Farbmusterfeldern. Oder klicke auf die Schaltfläche , um deine eigene benutzerdefinierte Farbe zu erstellen. Klicke mit der rechten Maustaste auf ein beliebiges Musterfeld, um eine weitere benutzerdefinierte Farbe hinzuzufügen und die Farbverlaufsauswahl zu öffnen.

Du kannst jedes Farbfeld auf ein beliebiges Musterfeld im Einstellungsdialog (oder Konfigurationsdialog) ziehen.

{{-}}

#### Farbverlauf

![[_media/PickAColor-gradient-dialog-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;Farbe auswählen&quot; - Farbverlaufsauswahldialog]] Im Dialogfeld für die Farbverlaufsauswahl kannst du das [Farbmusterfeld](wiki:De:Gramps_Glossar#swatch) im oberen Bereich des Dialogfelds anpassen. Klicke nach der Änderung entweder auf die Schaltfläche , um die Farbe anzuwenden. Ziehe das einzelne Farbverlaufsdialogfeld auf ein beliebiges Musterfeld im Einstellungsdialog (oder im Konfigurationsdialog).

Bestimmte Farben des Musterfelds können auf verschiedene Weise geändert werden:

- über die direkte Eingabe 'Farbe Hex-Farbcode'
- über den Farbtonregler (mit numerischer Feineinstellung)
- Maus-Linksklick in den 1-dimensionalen (Farbton) Regenbogen-Farbverlauf oder den 2-dimensionalen (Helligkeit und Sättigung) Farbton-Farbverlauf.
- Klicke mit der rechten Maustaste in einen der beiden Farbverläufe, um die numerische Steuerung für die Dimension(en) des Farbverlaufs anzuzeigen
- Klicke mit der linken Maustaste auf die Farbauswahl mit der Pipette, um ein beliebiges auf dem Bildschirm angezeigtes Pixel auszuwählen.

{{-}}

### Dateiauswahl

![[_media/FileChooser_Bookmarks_Breadcrumbs.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Linux GTK Dateiauswahl: Hervorhebung von Breadcrumbs und Lesezeichen]] ![[_media/FileChooser_Bookmarks_Breadcrumbs_mac.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} macOS GTK Dateiauswahl: Hervorhebung von Breadcrumbs und Lesezeichen]] ![[_media/FileChooser_Bookmarks_Breadcrumbs_win.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Windows GTK Dateiauswahl: Hervorhebung von Breadcrumbs und Lesezeichen]] Die Dialogfelder Öffnen und Speichern (Dateiauswahl) für Gramps basieren auf der [GTK-Dateiauswahl](https://docs.gtk.org/gtk3/iface.FileChooser.html). Jedes Betriebssystem hat erwartete Verhaltensweisen für Klicks, Doppelklicks, Sortierung, [Tastenkombinationen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Tastenkürzel_Referenz#Praktische_Tastenk.C3.BCrzel), Umgebungsvariablen und Standard-Dateispeicherorte, die für die betriebssystemeigenen Dateiauswahldialoge charakteristisch sind. Einige davon können über die Benutzeroberfläche so angepasst werden, dass sie den systemeigenen Dateiauswahlen ähnlicher sind. Die Eigenheiten der verschiedenen Betriebssysteme bedeuten jedoch, dass freigegebene Netzwerkordner und URI-Unterstützung möglicherweise nicht so einfach durchsucht werden können wie bei der Verwendung der systemeigenen Dateiauswahlen.

Die [GtkDateiauswahl](https://developer-old.gnome.org/gtk4/stable/GtkFileChooser.html) ermöglicht das Hinzufügen von schnellen Navigations-Hotlinks zu häufig verwendeten Stellen im Dateisystem. In der Standardimplementierung werden diese im Navigationsbereich der linken Seitenleiste angezeigt. Es mag zunächst etwas unklar sein, dass diese Verknüpfungen aus verschiedenen Quellen und in verschiedenen Varianten kommen, daher wollen wir die Terminologie hier erklären:

- **[Lesezeichen](#Lesezeichen_f.C3.BCr_Dateiordner)**: werden vom Benutzer durch Ziehen von Ordnern aus dem rechten Fenster in das linke Fenster oder über die Schaltfläche "Hinzufügen" erstellt. Lesezeichen können vom Benutzer umbenannt und gelöscht werden.
- **Verknüpfungen**: können von der Gramps-Anwendung bereitgestellt werden. Zum Beispiel kann das Programm eine Verknüpfung für einen Ordner "Downloads" oder "Dokumente" hinzufügen. Verknüpfungen können nicht vom Benutzer hinzugefügt oder entfernt werden. Mit der Option "Umbenennen..." im Kontextmenü können sie umbenannt werden.
- **Laufwerke**: werden von der zugrunde liegenden Dateisystemabstraktion bereitgestellt. Sie sind die "Wurzeln" des Dateisystems. Die Hotlinks Home und Downloads sind gemeinsame "Wurzeln". Laufwerke können vom Benutzer nicht geändert werden.

#### Dateiauswahl-Kontextmenüs

Klicke mit der rechten Maustaste auf eine beliebige Datei oder einen beliebigen Ordner im aktuellen Verzeichnis, um ein Kontextmenü mit den folgenden Optionen zu öffnen:

<hr>

- 

<hr>

- 

- 

<hr>

- 

- 

- 

- 

- 

<hr>

Klicke mit der rechten Maustaste in die Navigations-Seitenleiste, um ein Kontextmenü mit den folgenden Optionen zu öffnen:

<hr>

- 

- 

- 

<hr>

#### Breadcrumbs und Adressleiste für Texteingabe

Standardmäßig erfolgt die Navigation in den Dateiordnern in der Dateiauswahl durch Blättern. Es gibt auch einige Verknüpfungen auf der linken Seite und Breadcrumbs (in der Dialogabbildung grün hervorgehoben) für die schnelle Navigation nach oben und unten im Pfad.

Optional kann eine Adressleiste für die Texteingabe verwendet werden, um einen Pfad direkt einzugeben oder einzufügen. Mit der [Tastenkombination](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Tastenkürzel_Referenz) kannst du zwischen der Anzeige von Breadcrumbs und der Texteingabe-Adressleiste umschalten.

#### Lesezeichen für Dateiordner

Dateiordner-Lesezeichen können benutzerdefiniert werden, um das Auffinden von Standardspeicherorten zu erleichtern. Diese Lesezeichen werden zwischen den Sitzungen und unabhängig davon, welcher Stammbaum geladen wurde, gespeichert.

Navigiere bei geöffnetem Dialogfeld "Öffnen" oder "Speichern" zu der Datei, die den Ordner enthält, der mit einem Lesezeichen versehen werden soll. Erstelle das Lesezeichen, indem du entweder das Ordnersymbol in die linke Navigationsspalte ziehst oder mit der rechten Maustaste auf den Ordner klickst, um die Kontextmenüoption zu verwenden.

Wenn du mit der rechten Maustaste auf ein vorhandenes Lesezeichen klickst, kannst du dieses Lesezeichen umbenennen oder es entfernen.

#### Dateiformate

In der Standarddistribution von Gramps ist die Unterstützung für mehrere Dateiformate integriert. Import Zusatzmodul und Export Zusatzmodul können über die Zusatzmodulverwaltung oder die Voreinstellungen installiert werden, um die Optionen zu erweitern.

Eine Liste der Dateiformate findest du im Artikel [Ausgabeformat](wiki:Output_formats) (englisch).

#### Siehe auch

- [Wie zeigt man die Texteingabe-Adressleiste oder "Brotkrümel" (Navigationsschaltflächen)](https://ubuntugenius.wordpress.com/2010/05/14/how-to-show-text-entry-address-bar-or-breadcrumbs-navigation-buttons-in-nautilus-after-ubuntu-10-04-upgrade/) in Nautilus nach dem Ubuntu 10.04 Upgrade an?

<!-- -->

- Diskurs-Diskussionen über die GTK-Dateiauswahl:

<!-- -->

- - [Dokumentieren der Dateiauswahl im Wiki](https://gramps.discourse.group/t/need-suggestions-for-documenting-the-gtk-file-chooser/1820/8)
  - [Veranschaulichung der Dateiauswahl im Wiki](https://gramps.discourse.group/t/macos-and-windows-gtk-file-chooser-dialog-capture-request/3364)
  - [Dateiauswahl: Sortieren von Dateien und Ordnern](https://gramps.discourse.group/t/can-i-cause-folders-to-sort-to-the-top-of-the-list-when-presented-with-the-folder-contents/1708/14)
- [Wo finde ich die Liste der Funktionen von FileChooser?](https://discourse.gnome.org/t/where-is-the-filechooser-feature-list/9101/1) (englisch)

### Sprache

Gramps wurde in eine Reihe von [Sprachen](wiki:Portal:Translators) übersetzt. Normalerweise startet Gramps automatisch in deiner lokalen Sprache, so wie du es für andere Anwendungen gewählt hast, aber manchmal ist das vielleicht nicht das Richtige für dich. In anderen Fällen ist ein Modul oder Zusatzmodul noch nicht übersetzt und es erscheint eine Warnung wie “Warnung: Zusatzmodul XYZ hat keine Übersetzung für eine deiner konfigurierten Sprachen, verwende stattdessen US-Englisch”. (Beachte, dass der US-Dialekt des Englischen die Standardeinstellung ist und nicht das Britische). Das kann lästig oder aufdringlich werden.

Im Idealfall beherrschst du das US-Englisch so gut wie die Sprache, die du für die Benutzeroberfläche deines Computers gewählt hast. Und dass du die Gelegenheit nutzen würdest, die Gramps-Funktion für Benutzer, die kein Englisch sprechen, zu übersetzen.

Wenn dein System so konfiguriert ist, dass eine andere Sprache als Englisch angezeigt wird, kannst du dies für Gramps außer Kraft setzen.

Angenommen, ein Computer in den Niederlanden ist standardmäßig auf Unicode 8 Niederländisch eingestellt: "LANG: nl_NL.UTF-8". Du könntest entweder die Betriebssystemsprache zurücksetzen

Verwende unter Windows den Befehl SET, um die Umgebungsvariable LANG in "en_GB.UTF-8" für britisches Englisch zu ändern. Du kannst dies über die Befehlszeilenschnittstelle tun oder [eine Startverknüpfung mit dem folgenden Ziel erstellen](https://gramps-project.org/bugs/view.php?id=11009): `C:\Windows\System32\cmd.exe /c "SET LANG=en_GB.UTF-8 && START /D ^"C:\Program Files\GrampsAIO64-6.0.5^" gramps.exe"`

'''

#### Linux

Wenn du eine lokale "Variante" für die Sortierung wählen willst, die nicht die Standardvariante ist, dann kannst du Gramps vom Terminal (oder der Konsole) mit einer anderen LC_COLLATE-Umgebung starten. Zum Beispiel ist die Standardsortiervariante für Schwedisch "reformed", aber du kannst stattdessen "standard" wählen, indem du tippst:

`export LC_COLLATE="sv_SE.UTF-8@collation=standard"`  
`python Gramps.py`

#### mac OS X

Unter mac OS X findest du unter [Erweiterte Einstellungen](wiki:Mac_OS_X:Application_package#Advanced_setup) Details darüber, wie die Sprache normalerweise ausgewählt wird und wie du eine spezielle, nicht standardmäßige Einstellung für die Sprache, die Sortierreihenfolge oder das Format von Dingen wie Tages- und Monatsnamen und Zahlentrennzeichen wählen kannst.

#### MS Windows

![[_media/MicrosoftWindowGrampsAIO-Installer-ChooseComponents-Selection-example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Gramps 6.0.3 AIO 64 Bit für Microsoft Windows Installer – Seite „Komponenten auswählen” mit Auswahl der Übersetzung „de” (Deutsch)]] Wenn du Gramps mit dem Gramps AIO-Installationsprogramm in einer anderen Sprache als Englisch ausführen möchtest, musst du diese während des Installationsprozesses auswählen.

Andernfalls wird sie nicht verfügbar sein.

Weitere Informationen befinden sich auf der Seite [Installation von Gramps für Windows-Computer#Fehlende andere Sprachen](wiki:De:Installation_von_Gramps_für_Windows-Computer#Fehlende_andere_Sprachen).

{{-}}

### Menüelement des Windows-Betriebssystems hinzufügen

![[_media/Edit-Target-GrampsAIO64-Properties-Danish-example-60-de.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Bearbeiten-Ziel-GrampsAIO64-Eigenschaften für das dänische Verknüpfungsbeispiel.]] Damit Gramps in der von dir gewählten Sprache funktioniert (den [Sprachcode](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Einstellungen#Sprachcodes) findest du in der Tabelle unten), musst du folgende Schritte ausführen:

- Mit der rechten Maustaste auf das Symbol "" auf dem Desktop klicken und aus dem Menü wählen: .
- Mit rechter Maustaste auf eine beliebige Stelle des Desktops klicken und aus dem Menü wählen:
- Es wird ein neues Symbol erstellt mit dem Namen: ""
- Rechtsklick darauf und aus dem Menü wählen:
- Es öffnet sich ein neues Fenster. Auf die erste Registerkarte klicken und den Text von "" in etwas Beschreibenderes ändern wie: ""
  - Auf die zweite Registerkarte klicken und den Text im ersten Eintrag ändern (der Pfad hängt von der verwendeten Gramps-Version ab):
    - `"C:\Program File\GrampsAIO64-6.x.x\grampsw.exe"` in:
    - `%comspec% /c set LANG=da_DK.UTF-8 && start grampsw.exe"`
- Klicke

Wenn du jetzt auf das Symbol klickst, startet Gramps auf Dänisch.

{{-}} {{-}}

### Ändern der Windows-LANG-Variablen

Eine weitere Option, wenn du willst, dass Gramps immer in der kanadischen Sprache geladen wird, kannst du unter Windows \> Systemeigenschaften die LANG-Variable im Benutzerabschnitt des Umgebungsvariablendialogs mit dem entsprechenden Wert hinzufügen.

Der hinzuzufügende Wert ist:

    Name: LANG
    Wert: fr_CA.UTF-8

- [Einstellen von Umgebungsvariablen in Windows 10](https://www.redswitches.com/blog/environment-variables/#method-1-set-environment-variables-through-the-gui) (englisch)

### Sprachcodes

Wähle aus der folgenden Tabelle aus, in welche [Sprachen Gramps](wiki:Portal:Translators) übersetzt wurde:

| Sprache | ISO-Code | Beispiel | Notizen |
|----|----|----|----|
| Englisch (Britisch) | en_GB.UTF-8 | %comspec% /c set LANG=en_GB.UTF-8 && start grampsw.exe" |  |
| Finnisch | fi.UTF-8 | %comspec% /c set LANG=fi.UTF-8 && start grampsw.exe" |  |
| Russisch | ru_RU.UTF-8 | %comspec% /c set LANG=ru_RU.UTF-8 && start grampsw.exe" |  |
| Albanisch | sq_AL.UTF-8 | %comspec% /c set LANG=sq_AL.UTF-8 && start grampsw.exe" |  |
| Deutsch | de_DE.UTF-8 | %comspec% /c set LANG=de_DE.UTF-8 && start grampsw.exe" |  |
| Französisch | fr_FR.UTF-8 | %comspec% /c set LANG=fr_FR.UTF-8 && start grampsw.exe" |  |
| Französisch-kanadisch | fr_CA.UTF-8 | %comspec% /c set LANG=fr_CA.UTF-8 && start grampsw.exe" |  |
| Mazedonisch | mk_MK.UTF-8 ??? |  |  |
| Niederländisch | nl_NL.UTF-8 | %comspec% /c set LANG=nl_NL.UTF-8 && start grampsw.exe" |  |
| Niederländisch (Belgien) | nl_BE.UTF-8 | %comspec% /c set LANG=nl_BE.UTF-8 && start grampsw.exe" |  |
| Slowakisch | sk_SK.UTF-8 | %comspec% /c set LANG=sk_SK.UTF-8 && start grampsw.exe" |  |
| Hebräisch | he_IL.UTF-8 | %comspec% /c set LANG=he_IL.UTF-8 && start grampsw.exe" |  |
| Dänisch | da_DK.UTF-8 | %comspec% /c set LANG=da_DK.UTF-8 && start grampsw.exe" |  |
| Griechisch | el_GR.UTF-8 | %comspec% /c set LANG=el_GR.UTF-8 && start grampsw.exe" |  |
| Italienisch | it_IT.UTF-8 | %comspec% /c set LANG=it_IT.UTF-8 && start grampsw.exe" |  |
| Esperanto | eo.UTF-8 ??? |  |  |
| Chinesisch (vereinfacht) | zh_CN.UTF-8 | %comspec% /c set LANG=zh_CN.UTF-8 && start grampsw.exe" |  |
| Chinesisch (Hong Kong) | zh_HK.UTF-8 ??? |  |  |
| Chinesisch (traditionell) | zh_TW.UTF-8 | %comspec% /c set LANG=zh_TW.UTF-8 && start grampsw.exe" |  |
| Ukrainisch | uk_UA.UTF-8 |  |  |
| Portugiesisch | pt_PT.UTF-8 | %comspec% /c set LANG=pt_PT.UTF-8 && start grampsw.exe" |  |
| Portugiesisch (Brasilien) | pt_BR.UTF-8 | %comspec% /c set LANG=pt_BR.UTF-8 && start grampsw.exe" |  |
| Afrikaans | af_ZA.UTF-8 |  |  |
| Norwegisch Bokmål | nb_NO.UTF-8 | %comspec% /c set LANG=nb_NO.UTF-8 && start grampsw.exe" |  |
| Norwegisch Nynorsk | nn_NO.UTF-8 | %comspec% /c set LANG=nn_NO.UTF-8 && start grampsw.exe" |  |
| Türkisch | tr_TR.UTF-8 | %comspec% /c set LANG=tr_TR.UTF-8 && start grampsw.exe" |  |
| Spanisch | es_ES.UTF-8 | %comspec% /c set LANG=es_ES.UTF-8 && start grampsw.exe" |  |
| Polnisch | pl_PL.UTF-8 | %comspec% /c set LANG=pl_PL.UTF-8 && start grampsw.exe" |  |
| Slowenisch | sl_SI.UTF-8 | %comspec% /c set LANG=sl_SI.UTF-8 && start grampsw.exe" |  |
| Japanisch | ja_JP.UTF-8 | %comspec% /c set LANG=ja_JP.UTF-8 && start grampsw.exe" |  |
| Arabisch (Saudi-Arabien) | ar_SA.UTF-8 | %comspec% /c set LANG=ar_SA.UTF-8 && start grampsw.exe" |  |
|  |  |  |  |
|  |  |  |  |

- Bei den Sprachcodes handelt es sich um zweibuchstabige ISO-Sprachcodes in Kleinbuchstaben (z. B. "da") gemäß der Definition in [ISO 639-1](https://de.wikipedia.org/wiki/Liste_der_ISO-639-1-Codes).
- Bei den Ländercodes handelt es sich um zweistellige ISO-Ländercodes in Großbuchstaben (z. B. "BE") gemäß der Definition in [ISO 3166-1](https://de.wikipedia.org/wiki/ISO-3166-1-Kodierliste).

### Fortgeschrittene Manipulation von Einstellungen

Neben den Einstellungen, die in den Voreinstellungen verfügbar sind, sind möglicherweise auch die erweiterten Einstellungen von Interesse.

Gramps verwendet **[INI-Schlüssel](https://en.wikipedia.org/wiki/INI_file#Keys_(properties))** und [INI-Abschnitte](https://en.wikipedia.org/wiki/INI_file#Sections) für die Verwaltung von Benutzerpräferenzen und Programmeinstellungen. Diese werden in der Textdatei `gramps.ini` im Ordner `.gramps/gramps[XX]` in deinem Heimat- oder Benutzerverzeichnis gespeichert.

Die Datei `gramps.ini` hat folgende Abschnitte:

- \[behavior\] : Typische Schlüsselnamen sind: [betawarn](https://github.com/gramps-project/gramps/blob/master/gramps/gui/grampsgui.py#L502), enable-autobackup, use-tips...
- \[colors\] :
- \[csv\] :
- \[database\] : im Zusammenhang mit den Datenbankeinstellungen für den Stammbaum.
- \[export\] : Export und Import von Ordner/Verzeichnisse
- \[geography\] :
- \[interface\] : viele Schlüssel für Höhe und Breite der verschiedenen Ansichten: z.B. event-height: 450, event-ref-height: 585, event-ref-width: 728, event-width: 712...
- \[paths\] : Schlüssel zu den zuletzt importierten Dateien und Ordnern/Verzeichnissen
- \[plugin\] :
- \[preferences\] : Schlüssel, die sich auf die Voreinstellungen beziehen: alle gängigen Präfixe, ToDo-Farben..
- \[researcher\] : alle Informationen über den Forscher
- \[spacing\] :
- \[test\] :
- \[utf8\] :

#### Beispiel `gramps.ini` Datei

Beispiel für den Inhalt der Datei `gramps.ini`:

    ;; Gramps key file
    ;; Automatically created at 2025/05/24 08:49:41

    [behavior]
    ;;addmedia-image-dir=''
    ;;addmedia-relative-path=0
    ;;addons-allow-install=0
    ;;addons-projects=[['Gramps', 'https://raw.githubusercontent.com/gramps-project/addons/master/gramps60', True]]
    ;;addons-url='https://raw.githubusercontent.com/gramps-project/addons/master/gramps60'
    ;;autoload=0
    ;;avg-generation-gap=20
    ;;check-for-addon-update-types=['new']
    ;;check-for-addon-updates=0
    ;;date-about-range=50
    ;;date-after-range=50
    ;;date-before-range=50
    ;;do-not-show-previously-seen-addon-updates=1
    ;;generation-depth=15
    ;;immediate-warn=0
    ;;last-check-for-addon-updates='1970/01/01'
    ;;max-age-prob-alive=110
    ;;max-sib-age-diff=20
    ;;min-generation-years=13
    ;;owner-warn=0
    ;;pop-plugin-status=0
    ;;previously-seen-addon-updates=[]
    ;;recent-export-type=3
    ;;runcheck=0
    ;;spellcheck=0
    ;;startup=0
    ;;surname-guessing=0
    translator-needed=0
    ;;use-tips=1
    ;;web-search-url='https://google.com/search?q=%(text)s'
    ;;welcome=100

    [colors]
    ;;border-family=['#cccccc', '#252525']
    ;;border-family-divorced=['#ff7373', '#720b0b']
    ;;border-female-alive=['#861f69', '#261111']
    ;;border-female-dead=['#000000', '#000000']
    ;;border-male-alive=['#1f4986', '#171d26']
    ;;border-male-dead=['#000000', '#000000']
    ;;border-other-alive=['#2a5f16', '#26a269']
    ;;border-other-dead=['#000000', '#000000']
    ;;border-unknown-alive=['#8e5801', '#8e5801']
    ;;border-unknown-dead=['#000000', '#000000']
    ;;family=['#eeeeee', '#454545']
    ;;family-civil-union=['#eeeeee', '#454545']
    ;;family-divorced=['#ffdede', '#5c3636']
    ;;family-married=['#eeeeee', '#454545']
    ;;family-unknown=['#eeeeee', '#454545']
    ;;family-unmarried=['#eeeeee', '#454545']
    ;;female-alive=['#feccf0', '#62242D']
    ;;female-dead=['#feccf0', '#3a292b']
    ;;home-person=['#bbe68a', '#304918']
    ;;male-alive=['#b8cee6', '#1f344a']
    ;;male-dead=['#b8cee6', '#2d3039']
    ;;other-alive=['#94ef9e', '#285b27']
    ;;other-dead=['#94ef9e', '#062304']
    ;;scheme=0
    ;;unknown-alive=['#f3dbb6', '#75507B']
    ;;unknown-dead=['#f3dbb6', '#35103b']

    [csv]
    ;;delimiter=','
    ;;dialect='excel'

    [database]
    ;;autobackup=0
    ;;backend='sqlite'
    ;;backup-on-exit=1
    ;;backup-path='C:\\Users\\[username]'
    ;;compress-backup=1
    ;;host=''
    ;;path='C:\\Users\\[username]\\AppData\\Roaming\\gramps\\grampsdb'
    ;;port=''

    [export]
    ;;proxy-order=[['privacy', 0], ['living', 0], ['person', 0], ['note', 0], ['reference', 0]]

    [geography]
    ;;center-lat=0.0
    ;;center-lon=0.0
    ;;lock=0
    ;;map_service=1
    ;;path=''
    ;;personal-map=''
    ;;show_cross=0
    ;;use-keypad=1
    ;;zoom=0
    ;;zoom_when_center=12

    [interface]
    dbmanager-height=370
    ;;dbmanager-horiz-position=12
    ;;dbmanager-vert-position=85
    ;;dbmanager-width=780
    ;;dont-ask=0
    ;;filter=0
    ;;fullscreen=0
    ;;grampletbar-close=0
    ;;hide-lds=0
    ;;ignore-gexiv2=0
    ;;ignore-osmgpsmap=0
    ;;ignore-pil=0
    ;;main-window-height=500
    ;;main-window-horiz-position=15
    ;;main-window-vert-position=10
    ;;main-window-width=775
    ;;mapservice='OpenStreetMap'
    ;;open-with-default-viewer=0
    ;;pedview-layout=0
    ;;pedview-show-images=1
    ;;pedview-show-marriage=0
    ;;pedview-show-unknown-people=0
    ;;pedview-tree-direction=2
    ;;pedview-tree-size=5
    ;;place-name-height=100
    ;;place-name-width=450
    ;;sidebar-text=1
    ;;size-checked=0
    ;;statusbar=1
    ;;surname-box-height=150
    ;;tipofday-height=350
    tipofday-horiz-position=-49
    tipofday-vert-position=84
    ;;tipofday-width=550
    ;;toolbar-addons=1
    ;;toolbar-clipboard=1
    ;;toolbar-on=1
    ;;toolbar-preference=1
    ;;toolbar-reports=1
    ;;toolbar-style=0
    ;;toolbar-tools=1
    ;;treemodel-cache-size=1000
    ;;view=1
    ;;view-categories=['Dashboard', 'People', 'Relationships', 'Families', 'Ancestry', 'Events', 'Places', 'Geography', 'Sources', 'Citations', 'Repositories', 'Media', 'Notes']

    [paths]
    ;;quick-backup-directory='C:\\Users\\[username]'
    ;;quick-backup-filename='%(filename)s_%(year)d-%(month)02d-%(day)02d.%(extension)s'
    ;;recent-export-dir='C:\\Users\\[username]'
    ;;recent-file=''
    ;;recent-import-dir='C:\\Users\\[username]'
    ;;report-directory='C:\\Users\\[username]'
    ;;website-cal-uri=''
    ;;website-cms-uri=''
    ;;website-directory='C:\\Users\\[username]'
    ;;website-extra-page-name=''
    ;;website-extra-page-uri=''

    [plugin]
    ;;addonplugins=[]
    ;;hiddenplugins=[]

    [preferences]
    ;;age-after-death=1
    ;;age-display-precision=1
    ;;age-rounded-year=1
    ;;calendar-format-input=0
    ;;calendar-format-report=0
    ;;cite-plugin='cite-legacy'
    ;;coord-format=0
    ;;cprefix='C%04d'
    ;;date-format=0
    ;;default-source=0
    ;;eprefix='E%04d'
    ;;family-relation-type=3
    ;;family-warn=0
    ;;february-29=0
    ;;fprefix='F%04d'
    ;;hide-ep-msg=0
    ;;invalid-date-format='<b>%s</b>'
    ;;iprefix='I%04d'
    last-view='dashboardview'
    last-views=['dashboardview', '', '', '', '', '', '', '', '', '', '', '', '']
    ;;name-format=1
    ;;no-given-text='[Missing Given Name]'
    ;;no-record-text='[Missing Record]'
    ;;no-surname-text='[Missing Surname]'
    ;;nprefix='N%04d'
    ;;online-maps=0
    ;;oprefix='O%04d'
    ;;paper-metric=0
    ;;paper-preference='Letter'
    ;;patronimic-surname=0
    ;;place-auto=1
    ;;place-format=0
    ;;pprefix='P%04d'
    ;;private-given-text='[Living]'
    ;;private-record-text='[Private Record]'
    ;;private-surname-text='[Living]'
    ;;quick-backup-include-mode=0
    ;;rprefix='R%04d'
    ;;sprefix='S%04d'
    ;;tag-on-import=0
    ;;tag-on-import-format='Imported %Y/%m/%d %H:%M:%S'
    ;;use-last-view=0

    [researcher]
    ;;researcher-addr=''
    ;;researcher-city=''
    ;;researcher-country=''
    ;;researcher-email=''
    ;;researcher-locality=''
    ;;researcher-name=''
    ;;researcher-phone=''
    ;;researcher-postal=''
    ;;researcher-state=''

    [spacing]
    dbman=[22.605613425925927, 5.877459490740741, 9.856047453703704]

    [test]
    ;;january='January'

    [utf8]
    ;;baptism-symbol='~'
    ;;birth-symbol='*'
    ;;buried-symbol='[]'
    ;;cremated-symbol='⚱'
    ;;dead-symbol='✝'
    ;;death-symbol=2
    ;;divorce-symbol='o|o'
    ;;engaged-symbol='o'
    ;;in-use=0
    ;;killed-symbol='x'
    ;;marriage-symbol='oo'
    ;;partner-symbol='o-o'
    ;;selected-font=''

#### Erweiterte Einstellung des Sicherungsdateinamens

Du kannst auch das Benennungsmuster für den Sicherungsdateinamen definieren, indem du den *`paths.quick-backup-filename`* in der `~/.gramps/gramps60/gramps.ini` Schlüsseldatei wie folgt einstellst: {{-}}

`[paths]`  
`;;quick-backup-filename='%(filename)s_%(year)d-%(month)02d-%(day)02d.%(extension)s'`

indem du die beiden Semikolons (`;;`) vor der INI-Schlüsselzeile entfernst und die folgenden Schlüsselwörter für das Dateinamensmuster verwendest:

- `filename` \# Dateiname
- `year` \# Jahr
- `month` \# Monat
- `day` \# Tag
- `hour` \# Stunde
- `minutes` \# Minuten
- `seconds` \# Sekunden
- `extension` : \# Dateierweiterung
  - **.gpkg**(Standardeinstellung) wenn du Medien einbeziehst.
  - *.gramps* wenn du die Medien ausschließt.

Verwende die entsprechende ~/.gramps/gramps{XX}/gramps.ini Schlüsseldatei.

- Gramps version 6.0 :

`~/.gramps/gramps60/gramps.ini`

Siehe auch:

- [De:Gramps_6.0_Wiki_Handbuch_-_Stammbäume_Verwalten#Sicherungsdialog](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Stammbäume_Verwalten#Sicherungsdialog)
- [De:Gramps_6.0_Wiki_Handbuch_-_Kommandozeilen_Referenz#Konfiguration_.28config.29_Option](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Kommandozeilen_Referenz#Konfiguration_.28config.29_Option)
- [Install_latest_BSDDB#Make_Gramps_use_bsddb3](wiki:Install_latest_BSDDB#Make_Gramps_use_bsddb3) (englisch)
- [Customize_the_Genealogical_Symbols_lookup_table#Genealogy_symbols_preferences](wiki:Customize_the_Genealogical_Symbols_lookup_table#Genealogy_symbols_preferences) (englisch)

### Thema

Das Aussehen von Gramps kann verändert werden.

- [Addon:Theme Preferences](wiki:Addon:ThemePreferences)
- [Windows_AIO_themes](wiki:Windows_AIO_themes)
- [GTK 3 theme - GEPS 029: GTK3-GObject introspection Conversion](wiki:GEPS_029:_GTK3-GObject_introspection_Conversion#GTK_3_theme)
- [Overrule_Gramps_Icons](wiki:Overrule_Gramps_Icons) - für ältere Gramps-Versionen.
- [UI style](wiki:UI_style)

Einige Berichte können auch geändert werden:

- [Website report Themes](wiki:Website_report_Themes)

{{-}}

[Category:Tips](wiki:Category:Tips) [E](wiki:Category:De:Dokumentation)
