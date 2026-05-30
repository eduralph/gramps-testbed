---
title: De:Gramps 6.0 Wiki Handbuch - Werkzeuge
categories:
- De:Dokumentation
- Plugins
- Stub
- Tools
managed: false
source: wiki-scrape
wiki_revid: 131158
wiki_fetched_at: '2026-05-30T18:12:34Z'
lang: de
---

{{#vardefine:chapter\|14}} {{#vardefine:figure\|0}} ![[_media/MenuOverview-Tools-default-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;&quot; Menüleiste - Werkzeuge Übersicht - Standard]] Dieses Kapitel beschreibt die verschiedenen , die in Gramps verfügbar sind.

Gramps ermöglichen dir verschiedene Arten der Analyse deiner Genealogiedaten durchzuführen. Typischerweise erzeugen Werkzeuge keine Ausgaben in der Form von Ausdrucken oder Dateien. Stattdessen erzeugen sie Bildschirmausgaben die dem Forscher sofort zur Verfügung stehen. Allerdings kannst du, wenn es dienlich ist, die Ergebnisse eines laufenden Werkzeugs in einer Datei speichern.

## Werkzeuge

![[_media/ToolbarIcon-OpenTheToolsDialog-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Werkzeugleistensymbol für "Öffnet den Werkzeugdialog"]]

Auf die Werkzeuge kann über das Menü zugegriffen werden.

Alternativ kannst du die komplette Liste der verfügbaren Werkzeuge mit einer kurzen Beschreibung im , der über die Schaltfläche in der Werkzeugleiste aufgerufen wird, durchsuchen. {{-}}

### Werkzeugauswahl Dialog

![[_media/ToolSelection-dialog-with-debug-menu-60.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Werkzeugauswahl – Dialogfeld – Standardinformationen (und Auswahl der „Fehleranalyse“-Werkzeuge)]]

![[_media/ToolSelection-dialog-example-with-debug-menu-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Werkzeugauswahl – Dialogfeld – Beispiel mit Informationen zu „Datenbank überprüfen und reparieren“ (und Auswahl der „Fehleranalyse“-Werkzeuge)]]

Im Dialog kannst du die vollständige Auswahl der verfügbaren Werkzeuge zusammen mit ihren kurzen Beschreibungen durchsuchen, wenn sie aufgerufen werden, indem du in einer der Kategorien auf das Symbol ![[_media/Gramps-tools.png]] in der Symbolleiste klickst und die Listen mit den Pfeilen erweiterst. **Wähle ein Werkzeug aus den links verfügbaren Optionen aus**. Verwende die Pfeile, um die oberste Ebene der Liste zu erweitern:

- [Analyse und Untersuchung](#Analyse_und_Untersuchung)
- [Fehlersuche](#Fehlersuche)
- [StammbaumverarbeitungStammbaumverarbeitung](#Stammbaumverarbeitung)
- [Stammbaumverarbeitung](#Stammbaumreparatur)
- [Dienstprogramme](#Dienstprogramme)

Wähle dann das Werkzeug aus, das dich interessiert, damit auf der rechten Seite Folgendes angezeigt wird:

- Name des Werkzeugs
- Beschreibung des Werkzeugs
- Status:
- Autor:
- E-Mail-Adresse des Autors:

Über die Schaltflächen unten kannst du dann entweder weitere Informationen zum Werkzeug abrufen oder dein Werkzeug öffnen und ausführen.

- öffnet die Hilfeseite, sofern verfügbar – erfordert eine Internetverbindung —

- schließt diesen Dialog.

- – Ausgewähltes Werkzeug ausführen – öffnet die Werkzeugkonfigurationsseite.

{{-}} Siehe auch: [Berichtauswahldialog](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte#Berichtauswahldialog)

### Analyse und Untersuchung

Dieser Abschnitt enthält Werkzeuge, die die Datenbank analysieren und untersuchen, sie aber nicht verändern. Die folgenden Analyse- und Untersuchungswerkzeuge stehen aktuell in Gramps zur Verfügung:

#### <u>Einzelne Ereignisse vergleichen</u>

![[_media/CompareIndividualEvents-EventComparisonFilterSelection-dialog-default-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Einzelne Ereignisse vergleichen" - "Filterauswahl für Ereignisvergleich" - Dialog]]

Dieses Werkzeug sammelt alle Ereignisarten, die in einer Gruppe von Personen entdeckt wurden. Man könnte es wohl eher als Bericht denn als Werkzeug bezeichnen. Es erstellt eine zusammenfassende Vergleichstabelle, die mit dem Namen und der ID jeder Person beginnt und dann Spalten für die Ereignisarten und -daten hinzufügt. Wenn es mehrere Ereignisse derselben Art gibt, werden zusätzliche Zeilen erstellt. Die Zusammenstellung ignoriert die Rollen, berücksichtigt jedoch benutzerdefinierte Ereignisarten.

Die daraus resultierende Tabelle ist nützlich, um mutmaßliche Duplikate zu vergleichen und Unstimmigkeiten aufzudecken. Die Tabelle kann sehr breit werden, daher ermöglicht die Funktion „Speichern unter“ (im Format .ods) die Analyse in einer Tabellenkalkulationsanwendung.

Du kannst dieses Werkzeug über das Menü aufrufen, wodurch sich das Dialogfeld öffnet.

##### Dialogfeld zur Auswahl des Ereignisvergleichsfilters

Die Personen für diesen Vergleich können aus zuvor erstellten benutzerdefinierten Filtern ausgewählt werden, indem du die Dropdown-Liste auswählst, die standardmäßig die *Gesamte Datenbank* enthält. Oder indem du die Schaltfläche auswählst, um benutzerdefinierte Filter im Editor für zu erstellen. Um den Bericht auszuführen, wähle und die Ergebnisse werden im Dialogfeld angezeigt.

{{-}}

##### Dialogfeld Ergebnisse des Ereignisvergleichs

Im Dialogfeld kannst du die Ergebnisse anzeigen oder als Ergebnistabelle als Tabellenkalkulation (ODS-Format) . Wähle , um den Bericht zu beenden. {{-}} ![[_media/CompareIndividualEvents-EventComparisonResults-dialog-expanded-example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;Einzelne Ereignisse vergleichen&quot; - &quot;Ereignisvergleichs-Resultate&quot; - Dialog - erweitertes Beispiel]]

Die Tabelle (ODS-Format) enthält die folgenden Ausgabefelder:

- `Person, ID, Geburtsdatum, Geburtsort, Sterbedatum, Sterbeort, LVG-Datum, LVG-Ort, Beerdigungsdatum, Beerdigungsort, Heiratsdatum, Heiratsort`

{{-}}

### Stammbaumverarbeitung

Dieser Abschnitt enthält Werkzeuge die deine Daten ändern können. Die Werkzeuge aus diesem Abschnitt werden Hauptsächlich dazu verwendet Fehler in den Daten zu finden und zu beheben. Die folgenden Stammbaumverarbeitungswerkzeuge stehen aktuell in Gramps zur Verfügung:

- [Datenbankeigner Informationen bearbeiten](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Werkzeuge#Datenbankeigner_Informationen_bearbeiten)
- [Ereignisbeschreibung extrahieren](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Werkzeuge#Ereignisbeschreibung_extrahieren)
- [Informationen aus Namen extrahieren](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Werkzeuge#Informationen_aus_Namen_extrahieren)
- [Ortsdaten aus einem Ortstitel extrahieren](wiki:Addon:Extract_Place_Data_from_a_Place_Title) - **Dieses Werkzeug wurde zu [Erweiterungen von Drittanbietern](wiki:Third-party_Addons) verschoben.**
- [Finde mögliche doppelte Personen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Werkzeuge#Finde_mögliche_doppelte_Personen)
- [Großschreibung von Nachnamen korrigieren](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Werkzeuge#Großschreibung_von_Nachnamen_korrigieren)
- [Fundstellen zusammenfassen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Werkzeuge#Fundstellen_zusammenfassen)
- [Ereignisarten umbenennen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Werkzeuge#Ereignisarten_umbenennen)
- [Gramps-IDs neu ordnen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Werkzeuge#Gramps-IDs_neu_ordnen)
- [Sortiert Ereignisse](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Werkzeuge#Sortiert_Ereignisse)

#### <u>Datenbankeigner Informationen bearbeiten</u>

![[_media/DatabaseOwnerEditor-dialog-default-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Datenbankeignereditor" - Dialog - Standard]]

Das Werkzeug ändert alle vorhandenen [Forscherinformationen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Einstellungen#Informationen_zum_Forscher).

Wähle das Menü . Daraufhin wird das Fenster angezeigt, in dem du die erforderlichen Informationen eingeben oder über eine der Schaltflächen vorhandene Informationen abrufen kannst.

- 

- 

- 

- 

- 

- 

- 

- 

- 

Diese Informationen sind stammbaumspezifisch und werden beim Export deiner Daten in das GEDCOM-Format verwendet.

Zwei Schaltflächen stehen zur Auswahl:

- \- zum Abschnitt **Forscher**.

- \- aus dem Abschnitt **Forscher**.

{{-}}

#### <u>Ereignisbeschreibung extrahieren</u>

Extrahiert Ereignisbeschreibungen aus Ereignisdaten nach folgendem Schema:

`{Ereignistyp} von {Familienname}, {Vorname}`

Wenn eine Ereignisbeschreibung fehlt, füllt dieses Werkzeug das Feld nach oben genanntem Schema.

Du erreichst dieses Werkzeug über das Menü

Die **Warnung zum Rückgängigmachen** wird angezeigt und du kannst entweder oder wählen.

Wenn du wählst, scannt dieses Werkzeug deinen Stammbaum und nimmt Änderungen vor. Wenn keine Änderungen vorgenommen wurden, wird die Meldung angezeigt, andernfalls wird Folgendes angezeigt:

##### Ergebnisfenster für vorgenommene Änderungen

![[_media/ExtractEventDescription-ModificationsMade-window-example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Auszug aus der Ereignisbeschreibung – Fenster „Vorgenommene Änderungen“ – Beispielergebnis]]

werden im Ergebnisfenster aufgeführt, in dem die Gesamtzahl der hinzugefügten Ereignisbeschreibungen angegeben ist. {{-}}

#### <u>Informationen aus Namen extrahieren</u>

Dieses Werkzeug durchsucht die gesamte Datenbank und versucht Titel und Spitznamen die in dem einer Person enthalten sein können zu extrahieren. Wenn irgendeine Information extrahiert werden konnte, werden die Kandidaten für eine Korrektur in einer Tabelle dargestellt. Du kannst dann entscheiden welche wie vorgeschlagen korrigiert werden und welche nicht.

Du kannst auf dieses Werkzeug über das Menü zugreifen.

Der Dialog wird gezeigt und du kannst entweder oder wählen.

Das Dialogfeld wird angezeigt. Du kannst jede der Optionen nach Bedarf ändern und nach Abschluss der Änderungen auf klicken, um das Tool zu starten. {{-}}

Sobald das Werkzeug fertig ist, wird entweder das Dialogfeld mit der Meldung „Es wurden keine Titel, Spitznamen oder Präfixe gefunden“ angezeigt oder das Fenster mit den Suchergebnissen. {{-}}

##### Dialogfeld für Standardpräfix- und Konnektoreinstellungen

![[_media/ExtractInformationFromNames-DefaultPrefixAndConnectorSettings-dialog-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Standard Präfix und Verbinder einstellen" - Dialog für das Werkzeug "Informationen aus Namen extrahieren"]]

Der Dialog wird gezeigt und du kannst jede Option wie benötigt ändern:

- `de, van, von, di, le, du, dela, della, des, vande, ten, da, af, den, das, dello, del, en, ein, elet, les, lo, los, un, um, una, uno, der, ter, te, die` (Vorgabe)

- `e, y` (Standardeinstellung)

- `de, van` (Standardeinstellung)

{{-}}

##### Keine Änderungen vorgenommen-Dialogfeld

![[_media/ExtractInformationFromNames-NoModificationsMade-dialog-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Keine Änderungen vorgenommen" - Dialog für das "Informationen aus Namen extrahieren" Werzeug]]

Wird angezeigt, wenn im ausgewählten Stammbaum *Keine Titel, Spitznamen oder Präfixe gefunden wurden*.

Wähle , um das Dialogfeld zu schließen. {{-}}

##### Fenster für die Extraktion von Namen und Titeln

Der obere Abschnitt enthält Informationen zum Werkzeug.

![[_media/ExtractInformationFromNames-NameAndTitleExtractionTool-dialog-example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Werkzeug zur Extraktion von Namen und Titeln" - Dialogfenster mit den Ergebnissen für das "Informationen aus Namen extrahieren" Werkzeug]]

Beispielsweise wird der Name „de Mascarenhas da Silva e Lencastre” mit den Standardeinstellungen wie folgt angezeigt:

Der untere Bereich zeigt die Ergebnisliste in einer Tabelle mit den folgenden Spalten an: `Auswählen`, `ID`, `Art`, `Wert`, `Aktueller Name`.

Du kannst die gewünschten Ergebnisse `Auswählen` und dann auf klicken, um diese Ergebnisse auf deinen Stammbaum anzuwenden, oder auf , um nichts zu tun. Über die Schaltfläche gelangst du zum Hilfebereich dieses Werkzeugs.

{{-}}

#### <u>Extrahiere Ortsdaten aus Ortstitel</u>

#### <u>Mögliche doppelte Personen finden</u>

![[_media/FindPossibleDuplicatePeople-dialog-default-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Mögliche doppelte Personen finden - Dialog - Vorgabe]]

Das Werkzeug **Mögliche doppelte Personen finden** durchsucht die gesamte Baumdatenbank nach Einträgen, die möglicherweise dieselbe Person repräsentieren.

Du erreichst dieses Werkzeug über das Menü .

Das Dialogfeld wird angezeigt und du kannst die folgenden Optionen anpassen:

- : wähle zwischen **Niedrig**(Standard) *Mittel* und *Hoch* aus dem Aufklappmenü.

-  für mögliche übereinstimmende Personen. (Kontrollkästchen standardmäßig aktiviert)

Die folgenden Schaltflächen sind vorhanden: bringt dich auf diese Seite, zum Beenden der Verarbeitung und zum Start der Verarbeitung der Daten. Klicke auf die Schaltfläche um das Werkzeug zu starten und die Daten werden in zwei Durchgängen verarbeitet.

- Durchgang 1: vorläufige Listen erstellen
- Durchgang 2: mögliche Übereinstimmungen berechnen.

Es wird ein Fortschrittsbalken angezeigt und abhängig von der Geschwindigkeit deines Rechners und der Anzahl der Personen in deiner Datenbank kann dies eine Weile dauern.

{{-}}

##### <u>Mögliche Zusammenführungen</u>

![[_media/FindPossibleDuplicatePeople-PotentialMerges-result-dialog-example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Mögliche Zusammenführungen" Ergebnisdialogfenster für "Finde mögliche doppelte Personen" - Dialog - Beispiel]]

Zum Schluss wird ein Fenster angezeigt. Dieses Fenster enthält eine Liste mit drei Spalten:

- `Bewertung` : dies gibt dir eine Vorstellung von der Ähnlichkeit der beiden Personen. Je höher die Bewertung desto größer ist die Wahrscheinlichkeit, das diese Personen identisch sind.
- `Erste Person`
- `Zweite Person`

Wenn du eine Zeile auswählst, kannst du die Details mit der Schaltfläche überprüfen oder du kannst die gewählte Zeile doppelklicken.

Das Fenster besitzt drei Schaltflächen: bringt dich auf diese Seite, um das Fenster zuschließen, was dich zurück zu dem **Mögliche doppelte Personen finden** Fenster bringt und eine Schaltfläche die ein Fenster öffnet, welches in im Detail beschrieben wurde. Hier kannst du mit den Optionsschaltflächen eine der Personen wählen und eventuell die Schaltfläche verwenden um die Daten zusammenzufassen wenn du herausgefunden hast, das diese Personen identisch sind.

Wenn du auf die Schaltfläche klickst, gelangst du zurück zum Ergebnislistenfenster . {{-}}

#### <u>Großschreibung von Nachnamen korrigieren</u>

Dieses Werkzeug durchsucht die gesamte Datenbank und versucht die Großschreibung von Familiennamen zu korrigieren.

Das Ziel ist es, eine übliche Groß/Kleinschreibung zu erreichen: erste Buchstabe groß und die restlichen Buchstaben des Familiennamens klein. Wenn Abweichungen von dieser Regel festgestellt werden, werden die Kandidaten für die Korrektur in der Tabelle angezeigt.

Du kannst dann entscheiden, welche wie vorgeschlagen korrigiert werden sollen und welche nicht.

Du erreichst dieses Werkzeug über das Menü .

Der Dialog wird gezeigt und du kannst entweder oder wählen.

{{-}} ![[_media/FixCapitalizationofFamilyNames-CapitalizationChanges-dialog-results-example-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;Capitalization changes&quot; - Dialog - Ergebnis Beispiel für &quot;Großschreibung von Nachnamen korrigieren&quot; Werkzeug]]

Wenn es Änderungen in der Großschreibung von Namen gab, wird das Fenster geöffnet. Das Fenster zeigt eine Liste der Familiennamen, die Gramps in die (laut Gramps) korrekte Großschreibung umwandeln kann (bitte überprüfe, ob es für dich richtig ist.). In der Ergebnisliste der stehen die folgenden Spalten zur Verfügung:

-  - Aktiviere oder deaktiviere diese "nach Namen", wenn du die Empfehlung nicht akzeptierst (Kontrollkästchen standardmäßig aktiviert)

\- Der Name wie aktuell aufgezeichnet.  - Der Name mit Änderung, falls angewendet.

Wähle die Namen, die du ändern möchtest dann klicke auf die Schaltfläche. Oder verwende die Schaltfläche um die Änderungen zu verwerfen. {{-}}

Du kannst auch das "[Großschreibung von Vornamen korrigieren](wiki:Addon:Fix_Capitalization_of_Given_Names)" Werkzeugzusatzmodul installieren es arbeitet nahezu identisch wie dieses Werkzeug aber für "Vornamen". {{-}}

#### <u>Fundstellen zusammenfassen</u>

Du erreichst dieses Werkzeug über das Menü

Der Dialog wird gezeigt und du kannst entweder oder wählen.

{{-}} ![[_media/MergeCitations-dialog-default-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;Fundstellen zusammenfassen&quot; - Dialog - Voreinstellung]]

Dann wird der Dialog (Titel des Dialogs zeigt: *Notizen, Medienobjekte und Datenelemente passender Zitate werden kombiniert*.) angezeigt

Folgende Optionen stehen zur Verfügung:

- Aufklappliste:

  - Liefert Seite/Band, Datum und Vertrauensgrad
  - **Datum ignorieren** (Vorgabe)
  - Vertrauensgrad ignorieren
  - Datum und Vertrauensgrad ignorieren

- -  (Kontrollkästchen standardmäßig deaktiviert)

{{-}} ![[_media/NumberOfMergesDone-dialog-result-example-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;Anzahl erfolgter Zusammenfassungen&quot; Ergebnisdialog für &quot;Fundstellen zusammenfassen&quot; - Dialog - Werkzeug - Beispiel]]

Wähle , um das Werkzeug auszuführen, und nach Abschluss wird die Gesamtsumme mit dem Ergebnisdialogfeld zurückgemeldet. {{-}} Siehe auch die Option [Fundstellen zusammenführen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Daten_eingeben_und_bearbeiten:_Ausführlich_-_Teil_3#Fundstellen_zusammenf.C3.BChren), die in der Listenansicht der Fundstellenkategorie verfügbar ist {{-}}

#### <u>Ereignisarten umbenennen</u>

Dieses Werkzeug benennt alle Ereignisse einer Art in eine andere Art um.

Du erreichst dieses Werkzeug über das Menü

Der Dialog wird gezeigt und du kannst entweder oder wählen.

{{-}} ![[_media/RenameEventTypes-Tool-ChangeEventTypes-dialog-example-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;Ereignisarten ändern&quot; - Dialog - Beispiel für &quot;Ereignisarten umbenennen&quot; Werkzeug]]

Der Dialog wird angezeigt.

-   
  schreibe in das Textfeld oder verwende das Aufklappmenü, um eine originale Ereignisart zu wählen.

-   
  Schreibe in das Textfeld (du kannst hier eine völlig neue Art erstellen) oder verwende das Aufklappmenü, um eine neue Art zu wählen.

Das Beispiel zeigt eine Umbenennung des Ereignisses **Geburt** in ein Ereignis **Taufe**.

{{-}} ![[_media/RenameEventTypes-Tool-ChangeTypes-result-dialog-example-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;Arten ändern&quot; - Ergebnisdialog - Beispiel für &quot;Ereignisarten umbenennen&quot; Werkzeug]]

Verwende abschließend , um das Werkzeug zu beenden, oder wähle , um das Werkzeug auszuführen, und sobald es abgeschlossen ist, werden die gesamten geänderten Ereignisse mit dem Ergebnisdialogfeld zurückgemeldet. {{-}}

Siehe auch:

- [Informationen über Ereignisse bearbeiten](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Daten_eingeben_und_bearbeiten:_Ausführlich_-_Teil_2#Informationen_.C3.BCber_Ereignisse_bearbeiten)

<span ID="Reorder Gramps ID">

#### <u> Gramps-IDs neu ordnen </u>

</span>

Dieses Werkzeug kann verwendet werden, um deine Gramps-Objekt-IDs neu zu ordnen.

![[_media/ReorderGrampsIDs-dialog-example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Gramps-IDs neu ordnen" Werkzeugfenster – Beispiel]]

Du kannst dieses Werkzeug über das Menü verwenden.

Zunächst wird die Meldung **** angezeigt, und du kannst entweder auf oder klicken.

Dann wird das Werkzeugfenster angezeigt, in dem du die [Spaltenoptionen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Werkzeuge#Gramps-IDs_neu_ordnen_Werkzeugfenster) nach Bedarf ändern und dann auswählen kannst, um den Vorgang zu starten.

Das Werkzeug zeigt dann während der verschiedenen Fortschrittsphasen verschiedene Fortschrittsdialoge an, während die folgenden Objekt-IDs neu zugeordnet werden: „ „Personen-IDs neu ordnen”, „Familien-IDs neu ordnen”, „Ereignis-IDs neu ordnen”, „Orts-IDs neu ordnen”, „Quellen-IDs neu ordnen”, „Fundstellen-IDs neu ordnen”, „Aufbewahrungsorte-IDs neu ordnen”, „Medienobjekt-IDs neu ordnen” und schließlich „Notiz-IDs neu ordnen”.

Im letzten Schritt werden „unbenutzte IDs” gesucht und zugewiesen.

Während dieses Vorgangs überprüft das Werkzeug jede ID, um festzustellen, ob sie „angepasst” wurde, d. h. ob sie nicht dem vorherigen Objekt-ID-Format oder dem Standard-Objekt-ID-Format entspricht. Dies kann der Fall sein, wenn der Benutzer bei der Bearbeitung des Objekts manuell eigenen Text in das ID-Feld eingegeben hat. Es kann auch vorkommen, wenn das Add-on [GeoName](wiki:Addon:GeoName) oder das Add-on [GetGOV](wiki:Addon:GetGOV) verwendet wurde, das die **GOV ID** im Feld „Orts-ID” speichert. Wenn eine *angepasste* ID gefunden wird, zeigt das Werkzeug den Dialog an, in dem der Benutzer gefragt wird, ob er die ID wirklich ersetzen möchte, und der ihm optional erlaubt, die gleiche Antwort für alle gefundenen angepassten Objekt-IDs zu verwenden.

##### Gramps-IDs neu ordnen Werkzeugfenster

![[_media/ReorderGrampsIDs-dialog-default-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Gramps-IDs neu ordnen" Werkzeugfenster - Standardwert für neuen leeren Stammbaum]]

Das Werkzeug zeigt jedes Gramps-Objekt (Person, Familie, Ereignis, Ort, Quelle, Zitat, Archiv, Medien, Notiz) und die folgenden Optionsspalten (`Objekt`, „`Aktuell`“, `Anzahl`, `Format`, `Ändern`, `Start`, `Stopp`, `Beibehalten`), die zum Ändern der Objekt-IDs verwendet werden können.

Die Schaltfläche zeigt diesen Abschnitt an. Die Schaltfläche beendet das Werkzeug. Die Schaltfläche startet das Werkzeug.

Die meisten Spaltenbeschriftungen dienen gleichzeitig als versteckte Umschaltknöpfe und führen verschiedene Aktionen aus, wie unten beschrieben.

`Objekt`  
In dieser Spalte wird der Typ der Gramps-ID aufgeführt. Unmittelbar links neben dieser Spalte befinden sich Kontrollkästchen, mit denen Änderungen an einzelnen Objekttypen aktiviert werden können. Wenn diese Kontrollkästchen aktiviert sind, kann der Typ neu angeordnet werden. Die Beschriftung ist eigentlich eine versteckte Schaltfläche, mit der alle Kontrollkästchen auf einmal aktiviert oder deaktiviert werden können.

<!-- -->

`Aktuell`  
Diese Spalte zeigt ein Beispiel für die aktuelle Objekt-ID.

<!-- -->

`Anzahl`  
Diese Spalte zeigt die aktuelle Anzahl der Objekte im Stammbaum an.

<!-- -->

`Format`  
In dieser Spalte kann das ID-Format für jeden Objekttyp geändert werden. Beachte, dass das Standard-ID-Format aus einem einstelligen Präfix (I, F, E, P, S, C, R, O, N) für jedes Objekt und dem Suffix „`%04d`“ besteht. Es **MUSS** mindestens ein Präfix oder ein Suffix vorhanden sein, beide sind zulässig. Es wird empfohlen, diese relativ kurz zu halten. „`%04d`“ definiert die Länge des numerischen Teils der ID, wobei „`4`“ geändert werden kann und Werte zwischen „`3`“ (für Zahlen von 000 bis 999) und „`9`“ (000000000-999999999) sind zulässig (*Wenn dein Stammbaum mehr als „neunhundertneunundneunzig Millionen, neunhundertneunundneunzig Tausend, neunhundertneunundneunzig“ benötigt, reiche bitte eine Funktionsanfrage ein!*). Die hier vorgenommenen Änderungen entsprechen denen, die im Menü und dann auf der Registerkarte **** vorgenommen werden. Die Bezeichnung „“ ist eigentlich eine versteckte Schaltfläche, mit der alle Formate auf den zuletzt verwendeten Wert *zurückgesetzt* werden können.

<!-- -->

`Ändern`  
Diese Spalte enthält Kontrollkästchen für jeden Objekttyp. Wenn diese aktiviert sind, werden die IDs für dieses Objekt durch neue IDs im `Format`stil ersetzt, es sei denn, „Beibehalten“ ist ebenfalls aktiviert. Wenn kein Häkchen gesetzt ist, werden die ID-Formate *NICHT* aktualisiert, aber das Zahlenfeld innerhalb des Formats wird neu nummeriert. Die Bezeichnung ist eigentlich eine versteckte Schaltfläche, mit der alle Kontrollkästchen auf einmal umgeschaltet werden können.

<!-- -->

`Start`  
Dieses Feld gibt die Startnummer an, die bei der Umnummerierung verwendet wird. Die Beschriftung ist eigentlich eine versteckte Schaltfläche, mit der zwischen dem Start bei `0` und dem Start nach der letzten aktuellen Nummer umgeschaltet werden kann.

<!-- -->

`Schritt;`  
Dieses Feld gibt das Intervall zwischen den Nummern während der Umnummerierung an. `1` ist eine einfache Erhöhung, `2` erhöht um 2 usw. Die Bezeichnung ist eigentlich eine versteckte Schaltfläche, mit der zwischen `1`, `2`, `5`, und `10` umgeschaltet werden kann.

<!-- -->

`Beibehalten`  
Diese Spalte enthält Kontrollkästchen für jeden Objekttyp. Wenn sowohl das Kontrollkästchen `Beibehalten` als auch das Kontrollkästchen `Ändern` aktiviert sind, werden die ID-Formate für dieses Objekt beibehalten und das Zahlenfeld innerhalb des Formats neu nummeriert. Die Bezeichnung ist eigentlich eine versteckte Schaltfläche, mit der alle Kontrollkästchen auf einmal aktiviert werden können.

##### Gramps-IDs neu ordnen ersetzen Dialog

![[_media/ReorderGrampsIDs-replace-dialog-example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Gramps-IDs neu ordnen" ersetzen Dialog - Beispiel]]

Der Dialog fragt den Benutzer, ob er die ID wirklich ersetzen möchte, und bietet ihm optional die Möglichkeit, dieselbe Antwort für alle gefundenen benutzerdefinierten Objekt-IDs zu verwenden.

- 

Wähle oder . {{-}}

#### <u>Sortiert Ereignisse</u>

Ereignisse im Ereignisreiter vom *Personen* oder *Familieneditor* erscheinen in keiner bestimmten Reihenfolge außer in der Reihenfolge in der sie hinzugefügt wurden. Der Grund warum die Ereignisse nicht auf eine bestimmte Art wie zum Beispiel nach Datum sortiert werden, ist das ein Ereignis eingeordnet werden kann auch wenn kein genaues Datum oder Reihenfolge bekannt sind. Der Import oder das Zusammenfassen von Daten aus einer externen Quelle kann auch zu zusätzlich hinzugefügten Ereignissen, die außerhalb der Reihenfolge bestehender Ereignisse einer Person oder Familie liegen führen.

Ereignisse können manuell via [*Drag & Drop*](http://de.wikipedia.org/wiki/Drag_and_Drop) oder durch Verwendung der neu-ordnen Schaltflächen im Reiter neu angeordnet werden. So oder so kann ein Ereignis in der Ereignisliste hoch oder runter bewegt werden und Gramps merkt sich die neue Anordnung, wenn die Änderungen gespeichert werden. Die neue Reihenfolge wird überall dort verwendet, wo Ereignisse in Gramps angezeigt werden zum Beispiel in einem Bericht.

Die Reihenfolge von allen Ereignissen in einem Reiter kann auch durch klicken auf den Spaltentitel geändert werden. Zum Beispiel klicken auf den `Datum` Spaltentitel sortiert alle Ereignisse nach Datum. Jedoch ist diese Art der Sortierung nicht von Dauer beim Schließen des Fensters werden diese Änderungen rückgängig gemacht.

Die [*Drag & Drop*](http://de.wikipedia.org/wiki/Drag_and_Drop) Methode zum Sortieren von Ereignissen ist gut wenn eine kleine Anzahl sortiert wird aber für große Mengen ungeeignet. Das wurde speziell für diesen Zweck entwickelt, alle Ereignisse in der Datenbank neu sortieren oder nur jene die mit über einen Filter ausgewählten Personen zusammenhängen.

##### Ereignisse sortieren Werkzeug

Du erreichst dieses Werkzeug über das Menü .

Der Dialog wird gezeigt und du kannst entweder oder wählen.

{{-}}

###### Werkzeugoptionen-Registerkarte

![[_media/SortEvents-dialog-ToolOptions-tab-default-example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Sortiert Ereignisse" Werkzeug - Dialog - zeigt "Werkzeugoptionen" Registerkarte]]

Auf der Registerkarte des Dialogfensters wird mit der ersten Option der Bereich der Personen definiert, deren Ereignisse sortiert werden sollen. Die erste Auswahlmöglichkeit in der Liste ist, die Sortierung auf alle Personen in der Datenbank anzuwenden. Alternative Auswahlmöglichkeiten sind, die Sortierung auf Vorfahren und Nachkommen einer ausgewählten Person oder auf einen Bereich von Personen anzuwenden, die mit einem benutzerdefinierten Personenfilter ausgewählt wurden. Nachdem du ausgewählt hast, für wen die Sortierung gelten soll, musst du als Nächstes überlegen, wie die Ereignisse sortiert werden sollen. Die erste Option ist die Sortierung nach Datum. Dies ist wahrscheinlich die wahrscheinlichste Wahl, aber es können auch andere Ereignisattribute ausgewählt werden. Die letzten Auswahlmöglichkeiten sind, ob die Ereignisse aufsteigend oder absteigend sortiert werden sollen und ob die Sortierung auch auf Familienereignisse angewendet werden soll, zu denen die ausgewählten Personen gehören.

{{-}}

### Stammbaumreparatur

Die folgenden Werkzeuge zur Reparatur von Stammbäumen sind verfügbar:

- [Datenbank prüfen und reparieren](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Werkzeuge#Datenbank_prüfen_und_reparieren)
- [Geschlechtsstatistik neu erstellen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Werkzeuge#Geschlechtsstatistik_neu_erstellen)
- [Interne Referenzen neu erstellen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Werkzeuge#Interne_Referenzen_neu_erstellen)
- [Neuaufbau sekundäre Indexe](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Werkzeuge#Neuaufbau_sekundäre_Indexe)
- [Unbenutzte Objekte entfernen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Werkzeuge#Unbenutzte_Objekte_entfernen)

#### <u>Datenbank prüfen und reparieren</u>

Das Werkzeug überprüft die Datenbank auf Integritätsprobleme und behebt sie wenn es ihm möglich ist. Im Besonderen sucht es nach:

- Kaputten Familienverknüpfungen. Dies sind die Fälle in denen ein Personendatensatz auf eine Familie verweist, der Familiendatensatz aber nicht auf die Person verweist und umgekehrt.

<!-- -->

- Fehlende Medienobjekte. Das fehlende Medienobjekt ist das Objekt dessen Datei in der Datenbank verknüpft ist aber nicht existiert. Dies kann passieren wenn eine Datei versehentlich gelöscht, umbenannt oder an einen anderen Ort verschoben wird.

<!-- -->

- Leere Familien. Dies sind die Familieneinträge die keine Verknüpfungen zu Personen als ihre Angehörige besitzt.

<!-- -->

- Elternbeziehung. Dies überprüft alle Familien um sicherzustellen, das Vater und Mutter nicht verwechselt wurden. Der Test überprüft auch ob die Eltern ein unterschiedliches Geschlecht haben. Wenn sie das gleiche Geschlecht haben, wird die Beziehung in "Partner" umbenannt.

Du erreichst dieses Werkzeug über das Menü .

Der Dialog wird gezeigt und du kannst entweder oder wählen.

{{-}}

##### Dialogfeld Ergebnisse der Integritätsprüfung

![[_media/IntegrityCheckResults-dialog-CheckAndRepairDatabase-example-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Ergebnisse der Integritätsprüfung" - Beispiel Ergebnisdialog - für das "Datenbank prüfen und reparieren" Werkzeug]]

Alle gefundenen Probleme werden automatisch behoben und das Dialogfeld wird mit einer Zusammenfassung der durchgeführten Aktionen angezeigt. {{-}}

##### Dialogfeld Keine Fehler gefunden

Andernfalls siehst du den Dialog mit der Meldung *Die interne Prüfungen der Datenbank wurden erfolgreich durchgeführt*. {{-}}

##### Gramps hatte ein Problem, als es zum letzten Mal ausgeführt wurde - Dialog

![[_media/GrampsHadAProblemTheLastTimeItWasRun-dialog-51.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Gramps hatte ein Problem, als es zum letzten Mal ausgeführt wurde - Dialog]]

Nach einem Gramps Absturz [bietet Gramps beim Neustart an, das Werkzeug Prüfen & Reparieren zu starten](https://github.com/gramps-project/gramps/pull/778). (Eingeführt in Gramps 5.1.x)

{{-}}

#### <u>Geschlechtsstatistik neu erstellen</u>

![[_media/GenderStatisticsRebuilt-dialog-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Geschlechtsstatistik neu erstellen" - Ergebnisdialog für "Geschlechtsstatistik neu erstellen" Werkzeug]]

Die Statistik kann auch mit dem Werkzeug [Geschlechtsstatistik verwerfen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Werkzeuge#Geschlechtsstatistik_verwerfen) gelöscht werden (wenn das Menü aktiviert wurde).

Du erreichst dieses Werkzeug über das Menü .

Sobald dies abgeschlossen ist, wird der Ergebnisdialog angezeigt.

Siehe [Geschlecht](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Daten_eingeben_und_bearbeiten:_Ausführlich_-_Teil_1#Geschlecht) Eintrag.

{{-}}

#### <u>Interne Referenzen neu erstellen</u>

![[_media/ReferenceMapsRebuilt-dialog-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Interne Referenzen neu erstellen" - Ergebnisdialog für "Interne Referenzen neu erstellen" Werkzeug]]

Dieses Werkzeug erstellt Referenzkartentabellen neu. Dies steuert die Liste der *Referenzen*-Elemente in Editoren.

Du erreichst dieses Werkzeug über das Menü .

Sobald dies abgeschlossen ist, wird der Ergebnisdialog angezeigt.

##### Siehe auch

- Dieser Neuaufbau wird auch als Teil des Werkzeugs durchgeführt

{{-}}

#### <u>Neuaufbau sekundäre Indexe</u>

![[_media/SecondaryIndexesRebuilt-dialog-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Neuaufbau sekundäre Indexe" - Ergebnisdialog für "Neuaufbau sekundäre Indexe" Werkzeug]]

Dieses Werkzeug erstellt Sekundärindizes neu.

Du erreichst dieses Werkzeug über das Menü .

Nach Abschluss wird der Ergebnisdialog angezeigt.

Das rekonstruiert die sekundären Tabellen in der Baum-DB. Diese Tabellen enthalten Dinge wie Geschlechtsstatistiken (Vorname versus Geschlecht), um das Geschlecht von Namen bei der Eingabe erraten zu können, Nachnamen (für eine schnellere Suche nach möglichen Nachnamen und damit die Personenbaumansicht funktioniert), die verschiedenen IDs für Objekte (zum erleichtern der Suche nach ID), Platzieren von Beilagentabellen, damit die Ortsbaumansicht funktioniert, und einige andere.

Theoretisch werden diese Tabellen ständig aktualisiert, wenn sich etwas ändert. Ein Neuaufbau der Referenzkarten und Sekundärindizes sollte daher nicht erforderlich sein. Aber besonders zu Beginn der Gramps-Geschichte haben Fehler manchmal die korrekte Ausführung von Updates beeinträchtigt. Die Werkzeuge bleiben also verfügbar... ‘nur für alle Fälle’.

##### Siehe auch

- Dieser Neuaufbau wird auch als Teil des Werkzeugs durchgeführt

{{-}}

#### <u>Nicht verwendete Objekte entfernen</u>

Dieses Werkzeug durchsucht deine Datenbank nach nicht verwendeten Informationen und ermöglicht dir diese anschließend zu bearbeiten, zu verknüpfen oder zu entfernen.

Du erreichst dieses Werkzeug über das Menü .

{{-}} ![[_media/UnusedObjects-dialog-example-results-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;Unused Objects&quot; - Beispiel Ergebnisdialog für &quot;Unbenutzte Objekte entfernen&quot; Werkzeug]]

Der Dialog wird angezeigt.

Du kannst im oberen Abschnitt des Dialogfelds aus der Suchoption auswählen, die du verwenden möchtest:

-  (Kontrollkästchen standardmäßig aktiviert)

-  (Kontrollkästchen standardmäßig aktiviert)

-  (Kontrollkästchen standardmäßig aktiviert)

-  (Kontrollkästchen standardmäßig aktiviert)

-  (Kontrollkästchen standardmäßig aktiviert)

-  (Kontrollkästchen standardmäßig aktiviert)

-  (Kontrollkästchen standardmäßig aktiviert)

Wähle die Schaltfläche , um den Bericht auszuführen. Sobald abgeschlossen, werden die Ergebnisse wenn vorhanden im unteren Abschnitt des Dialogfelds mit den folgenden angezeigten Spalten angezeigt:

- Wähle die Zeile aus, wenn du das Objekt löschen möchtest (standardmäßig deaktiviert)

- \- Symbol für den Objekttyp.

- \- Gramps interner Name für das Objekt.

- \- des Objekts.

Um das Objekt zu untersuchen, musst du auf die Zeile doppelklicken und es wird der entsprechende Editor für das Objekt angezeigt, in dem du es bei Bedarf bearbeiten kannst.

die Objekte, die du löschen möchtest, entweder über die einzelnen Kontrollkästchen oder über die zugehörigen Schaltflächen:

- 

- 

- 

Nachdem du deine Löschentscheidungen getroffen hast, wähle die Schaltfläche , um die Objekte zu löschen.

Wenn du fertig bist, kannst du das Werkzeug mit der Schaltfläche beenden. {{-}}

### Dienstprogramme

Dieser Abschnitt enthält Werkzeuge, mit denen du einen einfachen Vorgang an einem Teil der Daten ausführen kannst. Die Ergebnisse können in deiner Datenbank gespeichert werden, ändern jedoch nicht deine vorhandenen Daten. Die folgenden Dienstprogramme sind derzeit in Gramps verfügbar:

- [Eingabedaten bereinigen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Werkzeuge#Eingabedaten_bereinigen)
- [Finde Datenbankschleife](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Werkzeuge#Finde_Datenbankschleife) -
- [Medienverwaltung](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Werkzeuge#Medienverwaltung) -
- [Nicht verwandt](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Werkzeuge#Nicht_verwandt) -
- [Verwandtschaftsrechner](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Werkzeuge#Verwandtschaftsrechner) -
- [Die Daten überprüfen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Werkzeuge#Die_Daten_.C3.BCberpr.C3.BCfen) -

#### <u>Eingabedaten bereinigen</u>

#### <u>Führende und nachgestellte Leerzeichen entfernen</u>

![[_media/CleanInputData-dialog-tool-example-dialog-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Eingabedaten bereinigen]]

Werkzeug zum Entfernen von führenden und nachfolgenden Leerzeichen aus importierten oder alten Daten. Das Werkzeug sucht nach Ortsnamen mit führenden und/oder nachfolgenden Leerzeichen. Es sucht auch im Vornamen und Nachnamen.

Leerzeichen am Anfang und Ende werden automatisch entfernt, wenn die Namensdaten in den Baum übernommen werden.

Das Werkzeug kann über das Menü oder den Werkzeugauswahldialog aufgerufen werden

Siehe auch:

- Ungültige Zeichen und führende oder nachfolgende Leerzeichen im Eingabefeld vermeiden - (hinzugefügt in Gramps [5.0.2](wiki:Template:Releases/5.0.2) mit [PR811](https://github.com/gramps-project/gramps/pull/811))
- [Neues Werkzeug zum Unterdrücken von führenden und nachgestellten Leerzeichen.](https://github.com/gramps-project/gramps/pull/783) - (hinzugefügt in Gramps [5.1.0](wiki:Template:Releases/5.1.0))
- Funktionsanforderung : Bitte Leerzeichen am Ende von Einträgen bei der Eingabe entfernen (2016)
- Funktionsanforderung : Nachfolgende Leerzeichen werden aus Abfragen in den voreingestellten Filtern entfernt (2011)

{{-}}

#### <u>Datenbankschleife finden</u>

![[_media/FindDatabaseLoop-example-PedigreeChartView-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Stammbaumdiagramm mit Schleife - Beispiel]]

Mit dem Dienstprogramm kannst du überprüfen, ob deine Datenbank Vorfahren-Schleifen enthält. Schleifen in deinem Stammbaum können beispielsweise dazu führen, dass eine Person sowohl als Kind als auch als Vorfahre einer anderen Person im Stammbaum angezeigt wird. Schleifen können versehentlich bei der Dateneingabe entstehen, beispielsweise wenn ein Sohn als sein eigener Großvater in den Stammbaum eingefügt wird!

Andere gültige Schleifen kommen ebenfalls vor und sollten nach Überprüfung im Stammbaum beibehalten werden:

- Eine Inzucht-Schleife, weil die Eltern miteinander verwandt sind.
- Eine Paarungsschleife, verursacht durch einen Mann, der Kinder mit genetisch verwandten Frauen hat.
- Eine Inzucht-Paarungsschleife, verursacht durch Vollgeschwister.

{{-}} ![[_media/FindDatabaseLoop-dialog-example-results-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Datenbankschleife finden – Dialogfeld – Ergebnisse aus dem Beispielfall „Stammbaum“]]

Verwende das Menü und du erhältst ein Fenster , das die Ergebnisse in einer Liste mit sechs Spalten anzeigt: *Schleifengruppe ohne Bezeichnung* (`Gramps ID`, `Elternteil`), (`Gramps ID`, `Kind`), `Familien-ID`.

- Die erste `Gramps ID` ist ein Verweis auf den Elternteil.
- Der `Elternteil` (Vorfahre auf dem Bild) ist die Person, nach der wir suchen.
- Die zweite `Gramps ID` ist ein Verweis auf das Kind.
- Das `Kind` (Nachkomme) ist der Ursprung der Schleife.
- Die `Familien-ID` ist ein Verweis auf die zugehörige Familie.

Durch Doppelklicken auf eine Auswahl wird der zugehörige [Familieneintrag](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Daten_eingeben_und_bearbeiten:_Ausführlich_-_Teil_1#Familieneditordialog) geöffnet.

So behebst du eine Stammbaumschleife in deinem Stammbaum.

- Suche die Personenseite der Person, deren Verwandtschaftsverhältnis angepasst werden muss.
- Überprüfe zunächst, ob ein Name oder ein Datum eines wichtigen Ereignisses nicht versehentlich falsch eingegeben wurde.
- Wenn du sicher bist, dass das Löschen der falschen Eltern-Kind-Beziehung die Schleife behebt, fahre mit den Schritten fort.

Sobald du alle Schleifen aufgelöst hast, wähle zum Beenden.

{{-}} Weitere Informationen zu Ahnenschleifen findest du unter:

- [Ahnenschleifen finden: Moderne Software-Erfahrung](https://www.tamurajones.net/FindingAncestralLoops.xhtml) (englisch)
- [Ahnenschleifen: Louis Kesslers Behold-Blog](http://www.beholdgenealogy.com/blog/?p=1309)

Siehe auch:

- [Endogamie](https://de.wikipedia.org/wiki/Endogamie) - Aus Wikipedia, der freien Enzyklopädie
- [Verwandtenheirat](https://de.wikipedia.org/wiki/Verwandtenheirat) - Aus Wikipedia, der freien Enzyklopädie

##### Beispiel für Ahnen-Schleifen

![[_media/FindDatabaseLoop-dialog-complex-example-results-60.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Finde mögliche Schleifen in einem komplexen Beispiel]] ![[_media/FindDatabaseLoop-dialog-example2-50.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Diagramm mit einem komplexen Beispiel]]

Im folgenden komplexen Beispiel haben wir mehrere Vorfahren-Schleifen, die durch die Zahl in der ersten unbeschrifteten Spalte „Schleifengruppe” gekennzeichnet sind:

Wenn wir uns die zweite Zeile ansehen, haben wir :

1.  Erste Gramps-ID : I0002
2.  Elter ist : Vater, Kind2
3.  Zweite Gramps-ID : I0001
4.  Kind ist : Vater, Vater
5.  Familie-ID ist : F0000

{{-}} ![[_media/FindDatabaseLoop-dialog-example2-50.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Mögliche Schleife in einem komplexen Beispiel finden]]

Um zu verstehen was passiert :

1.  Wir beginnen bei \[I0002\] Vater, Kind2.
2.  Weiter geht es mit seinem Sohn \[I0003\] Vater, Kind3.
3.  Weiter geht es mit seinem Sohn: \[I0000\] Kind, Kind.
4.  Weiter geht es mit seinem Sohn: \[I0001\] Vater, Vater.
5.  Weiter geht es mit seinem Sohn: \[I0002\] Vater, Kind2 ==\> **HIER haben wir eine Ahnenschleife**.

{{-}}

#### <u>Medienverwaltung</u>

Die besteht aus vier separaten Werkzeugen, auf die du über einen assistentenähnlichen Dialog zugreifen kannst, den du über das Menü aufrufen kannst. Daraufhin wird die erste Dialogseite **[Einführung](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Werkzeuge#Einf.C3.BChrung)** angezeigt.

##### Einführung

![[_media/Introduction-page-MediaManager-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Einleitung - Seite für "Gramps Medienverwaltung" - Werkzeug-Assistent]]

Es werden kurze Informationen zu den Funktionen der Werkzeuge angezeigt.

Wenn du auf der Seite **Einführung** auf die Schaltfläche klickst (oder die Tastenkombination benutzt), wird dir das Fenster **[Auswahl](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Werkzeuge#Auswahl)** angezeigt.

{{-}}

##### Auswahl

![[_media/Selection-page-MediaManager-default-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Auswahl - Seite für "Medienverwaltung" - Werkzeugassistent - Standard]]

Wähle im **Auswahl** Seite Fenster aus einer der vier Optionen die Aktionen aus, die du ausführen möchtest, und wähle dann die Schaltfläche :

- (Standardeinstellung)

- 

- 

- 

{{-}}

##### Ersetze die Zeichenfolge in dem Pfad

![[_media/ReplaceSubstringSettings-page-MediaManager-default-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Ersetze Zeichenfolge Einstellungen - Seite für "Medienverwaltung" - Werkzeugassistent - Standard]]

Dieses Werkzeug ermöglicht das Ersetzen einer angegebenen Teilzeichenfolge im Pfad von Medienobjekten durch eine andere Teilzeichenfolge. Dies kann nützlich sein, wenn du deine Mediendateien von einem Verzeichnis in ein anderes verschiebst.

Wenn du dieses Optionsfeld auswählst, wird ein -Fenster geöffnet, in dem du eine beliebige Zeichenfolge in das Textfeld und das Textfeld eingeben kannst . Du kannst jederzeit auf die Schaltfläche oder auf die Schaltfläche klicken. Wenn du auf die Schaltfläche klickst, wird das Fenster angezeigt.

{{-}}

##### Ändere Pfade von relativ zu absolut

![[_media/ConvertPathsFromRelativeToAbsolute-FinalConfirmation-page-MediaManager-example-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} 'Ändere Pfade von relativ zu absolut':"Endgültige Bestätigung" Seite für "Medienverwaltung" - Werkzeugassistent - Beispiel]]

Dieses Werkzeug ermöglicht die Konvertierung relativer Medienpfade in absolute. Dies geschieht, indem den wie in der Registerkarte von in dem Abschnitt angegeben voranstellst,, oder wenn dies nicht festgelegt ist, stellt es das vorgegebene [Benutzerverzeichnis](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Anwenderverzeichnis) voran.

- [Absolute und relative Pfadnamen](https://de.wikipedia.org/wiki/Pfadname#Absolute_and_relative_paths), Aus Wikipedia.
- [Absolute Pfade, relative Pfade, UNC-Pfade und URL-Pfade](https://desktop.arcgis.com/de/arcmap/latest/tools/supplement/pathnames-explained-absolute-relative-unc-and-url.htm) ArcMap Hilfe.

{{-}}

##### Ändere Pfade von absolut zu relativ

![[_media/ConvertPathsFromAbsoluteToRelative-FinalConfirmation-page-MediaManager-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} 'Ändere Pfade von absolut zu relativ':"Endgültige Bestätigung" Seite für "Medienverwaltung" - Werkzeugassistent - Beispiel]]

Dieses Werkzeug ermöglicht die Konvertierung absoluter Medienpfade in einen relativen Pfad. Der relative Pfad ist relativ zum angegebenen Basispfad in der Einstellung der Registerkarte von in dem Abschnitt oder Wenn dies nicht festgelegt ist, wird das Verzeichnis des Benutzers verwendet. Ein relativer Pfad verbindet den Dateispeicherort mit dem Basis-Medienpfad, der je nach Bedarf geändert werden kann.

- [Absolute und relative Pfadnamen](https://de.wikipedia.org/wiki/Pfadname#Absolute_and_relative_paths), Aus Wikipedia.
- [Absolute Pfade, relative Pfade, UNC-Pfade und URL-Pfade](https://desktop.arcgis.com/de/arcmap/latest/tools/supplement/pathnames-explained-absolute-relative-unc-and-url.htm) ArcMap Hilfe.

{{-}}

##### Bilder, die nicht in der Datenbank enthalten sind, hinzufügen

![[_media/AddImagesNotIncludedInDatabase-FinalConfirmation-page-MediaManager-example-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} 'Bilder, die nicht in der Datenbank enthalten sind, hinzufügen':"Endgültige Bestätigung" Seite für "Medienverwaltung" - Werkzeugassistent - Beispiel]]

Verzeichnisse auf Bilder überprüfen, die nicht in der Datenbank enthalten sind. Dieses Werkzeug fügt Bilder in Verzeichnissen hinzu, auf die von vorhandenen Bildern in der Datenbank verwiesen wird. Du musst ein Medienelement aus jedem Unterverzeichnis manuell importieren. Medienverwaltung schließt Unterverzeichnisse nicht automatisch ein. Alle im Werkzeug angezeigten Verzeichnispfade werden durchsucht. {{-}}

#### <u>Nicht verwandt</u>

![[_media/NotRelatedTo-dialog-NotRelated-Tool-example-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}}. "Nicht verwandt mit '...'" - Dialog - zeigt Ergebnisse für "Nicht verwandt" Werkzeug]]

Dieses Werkzeug listet Personen auf, die nicht mit der ausgewählten aktiven Person verbunden sind. Verbindungen können verknüpft in einer Kette von [Referenzen](wiki:Referenzen) oder in Verknüpfungen, die mit dem [Verknüpfungseditor in Notizen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Daten_eingeben_und_bearbeiten:_Ausführlich_-_Teil_2#Verkn.C3.BCpfungeditor) erstellten wurden enthalten sein.

Du erreichst dieses Werkzeug über das Menü .

Es öffnet sich ein Fenster, welches eine Liste aller **NICHT** mit der gewählten Person verwandten Personen enthält.

Diese Liste enthält:

- *Name*
- *ID*
- *Eltern*
- *Etiketten*

In der Spalte *Name* kannst du die Schaltflächen und verwenden, um die gruppierte *Name*-Liste zu reduzieren oder zu erweitern. Wenn du auf eine Person doppelklickst, wird das Dialogfeld oder angezeigt.

Wenn du eine Person wählst, kannst du das Feld verwenden: Es gibt 3 Möglichkeiten: leer (du kannst reinschreiben was du willst), Zu erledigen, Nicht verwandt. Mit der Schaltfläche kannst du die gewählte Marke der Person zuordnen. Diese Marke wird dann in der rechten Spalte angezeigt. {{-}}

#### <u>Beziehungsrechner</u>

![[_media/RelationshipTo-dialog-RelationshipCalculator-Tool-example-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;Beziehung zu&#39;...&#39; &quot; - Dialog - zeigt Ergebnisse für &quot;Beziehungsrechner&quot; Werkzeug]] Du erreichst dieses Werkzeug über das Menü .

Wenn du das Beziehungsrechner-Werkzeug auswählst, wird eine Liste geöffnet, die nach allen Personen gefiltert ist, die mit der [Aktive Person](wiki:De:Gramps_Glossar#aktive_Person) verbunden sind, **aber nicht unbedingt verwandt** sind. Um die Beziehung zu einer anderen Person zu berechnen, schließe das Fenster, aktiviere diese Person und wählen Das Werkzeug erneut aus dem Menü aus.

Wähle die Person aus der gefilterten Liste aus, um festzustellen, ob eine Beziehung besteht. Die genaue Verwandtschaft wird im unteren Feld angezeigt... zusammen mit den gemeinsamen Vorfahren in dieser Beziehung. Es werden nur Blutsverwandtschaften angezeigt (mit Ausnahme von Ehemann-Ehefrau- und Stiefverwandtschaften). Beachte, dass "verschwägerte" Beziehungen nicht angezeigt werden.

Die gefilterte Liste wird gruppiert und alphabetisch nach Nachnamen sortiert. (Unabhängig davon, ob die Menüeinstellung Ansicht der Kategorie Person auf **Gruppiert** gesetzt wurde.) Die Listenspalten können nicht umsortiert werden.

Der Grad der Trennung (Generationsabstand), der erkannt wird, wird durch den Wert auf der Registerkarte [Grenzwerte](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Einstellungen#Grenzwerte) im Menü gesteuert. Verschoben von der Registerkarte [5.1 Allgemeines](wiki:De:Gramps_5.1_Wiki_Handbuch_-_Einstellungen#Allgemeines) (Der Standardwert von 15 Generationen meldet eine Beziehung zwischen 12 Urgroßeltern, aber nicht die 13 Urgroßeltern. Die aktive Person wird als eine der Generationen gezählt. Eigene Generation plus Eltern plus Großeltern sind also die anderen 3 Generationen).

Im Wesentlichen sind zwei Personen direkt blutsverwandt, wenn sie einen gemeinsamen Vorfahren haben. Eine dieser Personen kann tatsächlich ein Vorfahre der anderen sein – beispielsweise ein Urgroßelternteil. Auch bei Tanten und Onkeln kannst du die Verwandtschaft durch die Suche nach dem gemeinsamen Vorfahren berechnen. In diesem Fall werden der Vater oder die Mutter der Tante oder des Onkels Großeltern des Neffen oder der Nichte.

Die grundlegendste Blutsverwandtschaft durch gemeinsame Vorfahren ist die der Geschwister (Brüder und Schwestern), die nur eine Generation unter dem gemeinsamen Vorfahren stehen. Eine weitere besondere Beziehung ist die eines dieser Geschwister zu den Nachkommen der anderen Geschwister. Wenn die aktive Person ein Enkel des gemeinsamen Vorfahren ist, wäre das Geschwister eine Tante oder ein Onkel. Abgesehen von dieser Generation von Nachkommen gibt es zwei gleichwertige Arten, die Beziehung zu beschreiben. Die Tochter von Urgroßeltern kann entweder Großtante oder Großtante genannt werden. (Der Beziehungsrechner verwendet die 'große' Variante.) Diese Person ist eine Urgroßtante der zweiten Urenkel, die vier Generationen vom gemeinsamen Vorfahren entfernt sind. (Sie kann auch eine zweite Großtante genannt werden.) Die umgekehrte Beziehung einer Tante oder eines Onkels ist ein Neffe oder eine Nichte.

Cousins (auch Cousins ersten Grades) sind zwei Generationen nach dem gemeinsamen Vorfahren durch verschiedene Geschwister. Cousins zweiten Grades sind also drei Generationen vom gemeinsamen Vorfahren entfernt - und so weiter.

Danach gilt jeder als "Cousin", aber um anzuzeigen, dass sie nicht zur gleichen Generation gehören, verwenden wir das Wort "entfernt", um die Anzahl der Generationen anzugeben, die sich zwischen den beiden unterscheiden. Zum Beispiel ist der Cousin "ersten" meines Vaters auch mein Cousin "ersten" aber "einmal entfernt" (ein Generationenunterschied zwischen uns). Der Cousin ersten Grades meines Vaters ist der "zweimal entfernte Cousin ersten Grades" meines eigenen Kindes - zwei Generationen unterschiedlich.

Wenn mehrere Blutsverwandte aufgrund eines Zusammenbruchs des Stammbaums bestehen, werden alle gemeldet.

Eine Volltextliste aller Blutsverwandten und ihrer Ehepartner kann in der [Verwandtschaftsliste](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte_-_Teil_6#Verwandtschaftsliste) eingesehen werden.

##### Siehe auch:

- Die **Beziehung zur Hauptperson** [Anzeigeeinstellungen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Einstellungen#Anzeige) Optionen für die Statusleiste
- **Beziehung zur Hauptperson** [Schnellansicht](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte_-_Teil_8#Schnellansichten).
- Das Gramplet **[Tiefe Verbindungen](wiki:Addon:Deep_Connections_Gramplet)**: Wenn dieses Zusatzmodul von Drittanbietern installiert ist, listet es die dazwischenliegenden Generationen durch die Geschwister eines gemeinsamen Vorfahren auf. (Aber es listet nicht den gemeinsamen Vorfahren auf oder wenn beide Personen durch denselben Ehepartner verbunden sind.) Das Gramplet beschreibt auch die indirekten Beziehungen.
- [Lokalisierung des Beziehungsrechners](wiki:Specification:Relationship_Calculator) - Erstelle aussagekräftige Beziehungsbeschreibungen in deiner Region.

{{-}}

#### <u>Die Daten überprüfen</u>

![[_media/VerifyTheData-DataVerifyTool-dialog-General-tab-defaults-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Die Daten überprüfen..." - "Die Daten überprüfen" Werkzeug Dialog - "Allgemeines" Registerkarte - Vorgaben]]

Dieses Werkzeug ermöglicht dir die Überprüfung der Datenbank auf der Grundlage einer Reihe von dir festgelegter Kriterien.

Zum Beispiel, du willst sicherstellen, das keiner in deiner Datenbank im Alter von 98 Kinder bekam. Nach gesundem Menschenverstand würde ein solcher Datensatz auf einen Fehler hinweisen. Jedoch ist dies kein Konsistenzfehler in der Datenbank. Außerdem könnte jemand im alter von 98 ein Kind bekommen haben (das ist wirklich passiert). Das überprüfen Werkzeug zeigt alles, was deine Kriterien verletzt, so das du überprüfen kannst, ob der Datensatz fehlerhaft ist oder nicht. Du triffst die endgültige Entscheidung.

Über das Menü erhältst du das Fenster. Das Fenster enthält vier Reiter; , , und . Diese Reiter enthalten eine Liste von Kriterien und Eingabefelder in denen du die Werte für die Kriterien ändern kannst. In den Listen unten stehen einige *brauchbare* Werte.

##### Die Daten überprüfen Registerkarten

Wähle auf den folgenden Registerkarten die Kriterien aus, mit denen du das Werkzeug ausführen möchtest. Wenn du mit den Kriterien einverstanden st, klicke auf die Schaltfläche (oder drücke die Tastenkombination) und du erhältst ein Fenster.

###### Allgemeines

-   
  (Standardeinstellung: `90`)

-   
  (Standardeinstellung: `17`)

-   
  (Standardeinstellung: `50`)

-   
  (Standardeinstellung: `3`)

-   
  (Standardeinstellung: `30`)

-   
  (Standardeinstellung: `99`)

Es gibt zwei Kontrollkästchen:

-  (Kontrollkästchen standardmäßig deaktiviert) : bewirkt, dass das Werkzeug ein Taufdatum akzeptiert, wenn ein Geburtsdatum nicht bekannt ist, und ein Bestattungsdatum akzeptiert, wenn ein Sterbedatum nicht bekannt ist. Es bewirkt auch, dass das Werkzeug "ungenaue" Daten akzeptiert (d. h. jedes "legale" Gramps-Datum, das nicht vollständig spezifiziert ist (mit einem expliziten Tag, Monat und Jahr)).

-  : überprüft, ob die Daten ungültig sind. (Kontrollkästchen standardmäßig aktiviert)

###### Frauen

-   
  (Standardeinstellung: `17`)

-   
  (Standardeinstellung: `48`)

-   
  (Standardeinstellung: `12`)

###### Männer

-   
  (Standardeinstellung: `18`)

-   
  (Standardeinstellung: `65`)

-   
  (Standardeinstellung: `15`)

###### Familien

-   
  (Standardeinstellung: `30`)

-   
  (Standardeinstellung: `8`)

-   
  (Standardeinstellung: `25`)

{{-}}

##### Ergebnisse der Datenüberprüfung Fenster

![[_media/DataVerificationResults-window-example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Datenüberprüfung Ergebnisfenster.]]

Nachdem du das Werkzeug ausgeführt hast, wird das Fenster angezeigt.

Abhängig von deinen Kriterien und deinen Daten wird eine Liste angezeigt. Die möglichen Befunde sind unten aufgeführt. (Es können jedoch weitere hinzugefügt werden.) Jeder Treffer wird mit ähnlichen Ergebnissen gruppiert.

- Taufe vor der Geburt
- **Taufe zu spät nach Familientradition**

  
Diese Regel ermittelt den Median der Tage zwischen Geburt und Taufe über alle Kinder einer Familie. Sie vergleicht dann die Tage zwischen der Geburt und der Taufe der betreffenden Person, wobei auch eine gewisse Frist für die Abweichung eingeräumt wird. Derzeit ist dieser Zeitraum mit 120 Tagen fest kodiert.

- Geburt ist gleich Tod
- Geburt gleich Heirat
- Beerdigung vor der Taufe
- Beerdigung vor der Geburt
- Beerdigung vor dem Tod
- **Beerdigung zu spät**

  
Eine Beerdigung gilt als "zu spät", wenn sie mehr als 14 Tage nach dem Todestag stattfindet. Sollte dies ein Parameter sein oder könnte dies den Benutzer verwirren?

- **Kinder sind nicht in chronologischer Reihenfolge**

  
Die Geburtsdaten (wenn kein Datum vorhanden ist und die Schätzung eingeschaltet ist, werden die Taufdaten verwendet) werden für jedes Kind einer Familie überprüft. Es wird überprüft, ob die Daten in der Liste der Kinder aufsteigen. Kinder ohne eines dieser Daten werden ignoriert

- Toter Vater
- Tote Mutter
- Tod vor der Taufe
- Tod vor der Geburt
- Tod gleich Heirat
- Getrennte Person

  
Personen ohne Elternteil, Ehepartner, Kind oder Geschwister

- Frühe Heirat

  
( Registerkarte Allgemein, Voreinstellung = 17 )

- **Familien sind nicht in chronologischer Reihenfolge**

  
Diese Regel verwendet das Heiratsdatum und wertet aus, dass die Familien für eine Person chronologisch geordnet sind. Wenn kein Heiratsdatum vorhanden ist, wird ein Scheidungsdatum oder sogar das Geburtsdatum des ältesten Kindes jeder Familie verwendet. Das Geburtsdatum als letzter möglicher Fallback wird verwendet, um nicht verheiratete Familien mit unehelichen Kindern zu berücksichtigen.

- **Familienereignisse nicht in chronologischer Reihenfolge**
- **Familie hat Ereignisse mit Rolle Unbekannt**
- Weiblicher Ehemann
- Ehemann und Ehefrau mit demselben Nachnamen
- Ungültiges Geburtsdatum

  
( Registerkarte Allgemein, Voreinstellung = Wahr )

- Ungültiges Sterbedatum

  
( Registerkarte Allgemein, Voreinstellung = Wahr )

- Großer Altersunterschied zwischen den Ehegatten

  
(Registerkarte "Familien", Voreinstellung = 30)

- Großer Altersunterschied zwischen Kindern

  
( Registerkarte "Familien", Standardwert = 8 )

- **Große Jahresspanne für alle Kinder**

  
( Registerkarte Familien, Voreinstellung = 25 )

- Späte Heirat

  
( Registerkarte Allgemein, Voreinstellung = 50 )

- Männliche Ehefrau
- Heirat nach dem Tod
- Heirat vor der Geburt
- Heiratsdatum, aber nicht verheiratet
- Oft verheiratet

  
( Registerkarte Allgemein, Standardwert = 3 )

- Mehrere Eltern
- Alter bei Tod
- Alter, aber kein Tod

  
( Registerkarte Allgemein, Standardwert = 90 )

- Alt und unverheiratet

  
( Registerkarte Allgemein, Standardwert = 50 )

- Alter Vater

  
( Registerkarte Männer, Voreinstellung = 65 )

- Alte Mutter

  
( Registerkarte Frauen, Standardwert = 48 )

- **Ereignisse der Person nicht in chronologischer Reihenfolge**
- **Person hat Ereignisse mit Rolle Unbekannt**
- Gleichgeschlechtliche Ehe
- Zu viele Kinder

  
( Reiter Männer, Standard = 15; Reiter Frauen, Standard = 12 )

- Ungeborener Vater
- Ungeborene Mutter
- Unbekanntes Geschlecht
- Junger Vater

  
( Registerkarte Männer, Standardwert = 18 )

- Junge Mutter

  
( Registerkarte Frauen, Standardwert = 17 )

Am unteren Rand des Fensters stehen vier Schaltflächen zur Verfügung, um die Auswahl zu erleichtern. Dies sind , , und .

Durch Doppelklicken auf eine Zeile hast du die Möglichkeit, die Daten anzuzeigen und/oder zu bearbeiten.

Mit der Schaltfläche (oder der Tastenkombination ) schließt du das Fenster . {{-}}

##### Beispiele

Zwei Beispiele für die Verwendung von Echtdaten mit diesem Werkzeug:

  
Die Warnung zeigt 'weiblicher Ehemann': Beim Überprüfen der Daten fand ich eine Familie mit dem Vater: Anna Roelants. Glücklicherweise las ich in der : *Die Hochzeit von Adam Roelants und Cornelia Crabbe*. Es war also klar ein Tippfehler: Anna anstatt Adam. Ohne dieses **Werkzeug** wäre dies schwer zu finden.

<!-- -->

  
Die Warnung zeigt 'späte Heirat': Überprüfung der Daten: männliche Person °1738 weibliche Person °1756 : Heirat X 1804 \[Gregorian Calender\|Gregorianischer Kalender\] : Alles scheint OK. zu sein: Sie heirateten im alter von 66 und 48 Jahren! Die Warnung wurde gezeigt, weil die **Allgemeinen Kriterien** auf **60** gesetzt waren.

##### Siehe auch

- Entwicklungsdiskussion im Gramps Community Support Discourse Forum:

  
[Interest in enhancing verify.py](https://gramps.discourse.group/t/interest-in-enhancing-verify-py/4075/23)

{{-}}

### Fehlersuche

![[_media/MenuOverview-Tools-Debug-menu-example-60.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "" Menüleiste - Werkzeuge - Fehlersuche Menüübersicht]]

Befehlszeile: Python-Option`-O` „Optimierungsflagge“ nicht aktiviert ist, erscheint ein zusätzlicher -Eintrag im Menü und die folgenden Werkzeuge stehen zur Verfügung:

- [Check Localized Date Displayer and Parser](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Werkzeuge#Check_Localized_Date_Displayer_and_Parser)
- [Dump Gender Statistics](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Werkzeuge#Dump_Gender_Statistics)
- [Generate Testcases for Persons and Families](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Werkzeuge#Generate_Testcases_for_Persons_and_Families)
- [Populate Sources and Citations](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Werkzeuge#Populate_Sources_and_Citations)

Siehe auch:

- [Kommandozeile: Python Optionen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Kommandozeilen_Referenz#Python_Optionen)
- [Uncollected Objects](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Gramplets#Uncollected_Objects) Gramplet
- [Python-Auswertung](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Gramplets#Python-Auswertung) Gramplet

{{-}}

#### Check Localized Date Displayer and Parser

![[_media/StartDateTest-dialog-CheckLocalizedDateDisplayerAndParser-Tool-60.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Start date test?" Dialog - für "Check Localized Date Displayer and Parser" - Werkzeug]]

Dieses Testwerkzeug erstellt viele Personen, die alle verschiedenen Datumsvarianten als Geburt anzeigen. Das Sterbedatum wird erstellt, indem das Ergebnis der Datumsanzeige für das Geburtsdatum analysiert wird. Auf diese Weise kannst du sicherstellen, dass gedruckte Datumsangaben korrekt wieder eingelesen werden können.

Es wird das Dialogfeld angezeigt, in dem du entweder zum Beenden oder zum Starten des Werkzeugs auswählen kannst. {{-}}

#### Geschlechtsstatistik verwerfen

![[_media/GenderStatisticsTool-dialog-DumpGenderStatistics-Tool-example-60.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Gender Statistics tool" Dialog Ergebnisbeispiel - für "Geschlechtsstatistik verwerfen" - Werkzeug]]

Das Dialogfeld „Geschlechterstatistik-Werkzeug“ zeigt die Ergebnisse in einer Liste mit Statistiken zur Geschlechtsermittlung anhand des Vornamens der Person an.

Siehe [Geschlecht](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Daten_eingeben_und_bearbeiten:_Ausführlich_-_Teil_1#Geschlecht) Eintrag. {{-}}

#### Generate Testcases for Persons and Families

![[_media/GenerateTestcases-dialog-GenerateTestcasesForPersonsAndFamilies-Tool-60.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Generate testcases" Dialog - für "Generate Testcases for Persons and Families" - Werkzeug - Vorgabe]]

Der Testfallgenerator generiert einige Personen und Familien, die fehlerhafte Links in der Datenbank haben oder Daten, die in Konflikt mit einer Beziehung stehen.

Die wird angezeigt und du kannst entweder oder .

Du kannst Testfälle erstellen, die Folgendes verursachen:

- 

- 

- 

- 

- 

- 

- 

<!-- -->

- `2000`(default)

Select to exit or to start the tool.

will bring you here.

- Command line usage see: [Plugins_Command_Line#Generate_Testcases_for_Persons_and_Families](wiki:Plugins_Command_Line#Generate_Testcases_for_Persons_and_Families)

{{-}}

#### Populate Sources and Citations

![[_media/PopulateSourcesAndCitationsTool-dialog-default-60.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Populate sources and citations tool" Dialog - Vorgabe]]

Dieses Werkzeug generiert Quellen und Fundstellen für jede Quelle, um die Datenbank zum Testen mit einer beträchtlichen Anzahl von Quellen und Fundstellen zu füllen.

Enter the required number and then select to run the tool:

- `2` (default)

- `2` (default)

Sobald das Werkzeug fertiggestellt ist, wird dir der Warnungsdialog angezeigt.

{{-}}

[W](wiki:Category:De:Dokumentation) [Category:Tools](wiki:Category:Tools) [Category:Plugins](wiki:Category:Plugins)
