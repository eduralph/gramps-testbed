---
title: De:Gramps 6.0 Wiki Handbuch - Fehler und Warnung Referenz
categories:
- De:Dokumentation
- Pages with broken file links
- Stub
- Troubleshooting
managed: false
source: wiki-scrape
wiki_revid: 131299
wiki_fetched_at: '2026-05-30T17:46:06Z'
lang: de
---

{{#vardefine:chapter\|E}} {{#vardefine:figure\|0}}

Diesr Abschnitt erklärt was zu tun ist wenn etwas unerwartetes passiert.

## Wenn etwas schief läuft

Manchmal geht etwas schief, entweder weil du darum gebeten hast, etwas zu tun, von dem Gramps nicht weiß, wie es zu tun ist, oder weil etwas passiert ist, das die Entwickler von Gramps nicht erwartet haben, oder weil ein Fehler in der Kodierung von Gramps vorliegt.

## Alarme

Eine Warnung ist ein Dialogfeld, das angezeigt wird, wenn Gramps dir eine wichtige Meldung über einen Fehlerzustand geben oder Sie vor potenziell gefährlichen Situationen oder Konsequenzen warnen muss.

Die meisten Warnungen sind selbsterklärend und dieselbe Art von Warnungen, die du möglicherweise mit jeder Anwendung erhältst. Diese werden hier nicht weiter besprochen.

Einige Warnungen erfordern jedoch kompliziertere Aktionen, sodass sie im Folgenden beschrieben werden. {{-}}

### Änderungen verwerfen?

![[_media/Abort-changes-dialog-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Änderungen verwerfen?" Dialog]]

Das Dialogfeld wird angezeigt, wenn du im Menü \]\] auswählst. Mit der Schaltfläche kannst du deine Bearbeitung fortsetzen, mit der Schaltfläche kannst du den Stammbaum in den Zustand zurückversetzen, in dem er sich vor Beginn der Bearbeitung befand.

{{-}}

### Möchtest du diesen Stammbaum wirklich aktualisieren?

![[_media/AreYouSureYouWantToUpgradeThisFamilyTree-dialog-DbUpgradeRequiredError-example-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Bist du sicher, dass du diesen Stammbaum aktualisieren möchtest?" Dialog - Datenbank-Aktualisierung erforderlich - Beispiel]]

![[_media/AreYouSureYouWantToUpgradeThisFamilyTree-dialog-BsddbUnsupported-example-52-de.png||thumb|right|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Bist du sicher, dass du diesen Stammbaum aktualisieren möchtest?" Dialog - BSDDB-Konvertierung - Beispiel]]

![[_media/AreYouSureYouWantToUpgradeThisFamilyTree-dialog-BsddbUpgradeRequiredError-example-50.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Möchtest du diesen Stammbaum wirklich aktualisieren?" Dialog - BSDDB Aktualisierung erforderlich Fehler - Beispiel]]

![[_media/AreYouSureYouWantToDowngradeThisFamilyTree-dialog-BsddbDowngradeRequiredError-example-50.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Bist du sicher, dass du diesen Stammbaum herabstufen möchtest?" Dialog - BSDDB Downgrade erforderliche Fehler - Beispiel]]

![[_media/AreYouSureYouWantToUpgradeThisFamilyTree-dialog-PythonUpgradeRequiredError-example-50.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Bist du sicher, dass du diesen Stammbaum aktualisieren möchtest?" Dialog - Python Aktualisierung erforderliche Fehler - Beispiel]]

Diese Dialoge werden aus den folgenden Gründen angezeigt:

- „BSDDB Aktualisierung erforderlich Fehler" - die veraltete [BSDDB](wiki:De:Gramps_Glossar#bsddb)-Datenbankfamilie muss für Gramps in eine aktuelle Datenbank-Engine (normalerweise SQLite) konvertiert werden.
- "BSDDB-Upgrade erforderlich Fehler" - Wenn du versuchst, einen BSDDB-Stammbaum mit einer neueren Version von Gramps zu öffnen, der mit einer früheren älteren Version von Gramps erstellt wurde.
- "BSDDB Downgrade Erforderliche Fehler" - Wenn du versuchst, einen BSDDB-Stammbaum mit einer neueren Version von BSDDB zu öffnen, der mit einer mit einer neueren Version von BSDDB erstellt wurde.
- "Fehler Python-Aktualisierung erforderlich" - Wenn du versuchst, einen BSDDB-Stammbaum mit einer neueren Version von Gramps mit Python 3 zu öffnen, der mit einer früheren älteren Version von Gramps mit Python 2 erstellt wurde.

Aus jedem dieser Gründe kannst du demselben allgemeinen Rat befolgen. Wenn du noch die ältere Version von Gramps zur Verfügung hast, solltest du:

- Diesen Dialog abbrechen und Gramps beenden
- Öffne den Stammbaum mit der vorherigen Version von Gramps (Installiere die alte Version von Gramps neu).
- Exportiere deinen Stammbaum im Exportformat [Gramps XML (Stammbaum)](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Stammbäume_Verwalten#Gramps_XML_.28Stammbaum.29_Export) oder im Format [Gramps XML Package (Stammbaum und Medien)](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Stammbäume_Verwalten#Gramps_XML_Paket_.28Stammbaum_und_Medien.29_Export).
- Beende die alte Version von Gramps und starte die neue Version von Gramps.
- Öffne den Stammbaum in der neuen Version von Gramps und klicke auf die Schaltfläche in diesem Dialog

{{-}}

### Fehler beim Analysieren von Argumenten

![[_media/ErrorParsingArguments-dialog-DatabaseIsLocked-example-51-de.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}}Fehler beim Analysieren von Argumenten - Dialog - Beispiel: Datenbank ist gesperrt]] Die Familienstammbaum-Datenbank ist gesperrt, während sie von einem anderen Benutzer verwendet wird oder weil Gramps während der vorherigen Verwendung abnormal beendet wurde.

Siehe [Einen Stammbaum entsperren](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Stammbäume_Verwalten#Einen_Stammbaum_entsperren) {{-}}

### Die Datenbank ist gesperrt. Ich kann sie nicht öffnen!

Die Familienstammbaum-Datenbank ist gesperrt, während sie von einem anderen Benutzer verwendet wird oder weil Gramps während der vorherigen Verwendung abnormal beendet wurde.

Siehe [Einen Stammbaum entsperren](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Stammbäume_Verwalten#Einen_Stammbaum_entsperren) {{-}}

### Datenbank kann nicht geöffnet werden

![[_media/Cannot_open_database-40.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Dialog mit DB-Umgebungsfehler]]

![[_media/DbVersionError-40.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Dialog mit DB-Versionsfehler]]

Wie im Dialog erläutert, wurde der Stammbaum wahrscheinlich mit einer alten Version des Berkeley-Datenbankprogramms erstellt. Dies ist nicht ganz dasselbe wie eine alte Version des Gramps-Programms, da die Version des Gramps-Programms und die Version der Berkeley-Datenbank unabhängig voneinander sind. Der Effekt ist jedoch in etwa gleich. Wenn du die alte Version von Gramps und die Support-Software hast, solltest du wie im Dialog vorgeschlagen:

- diesen Dialog abbrechen,
- den Stammbaum mit der vorherigen Gramps-Version öffnen,
- Deinen Stammbaum im Exportformat der Gramps XML-Datenbank oder im Exportformat des Gramps-Pakets exportieren (siehe [Daten exportieren](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Stammbäume_Verwalten#Daten_exportieren)),
- die neue Gramps-Version starten,
- öffne den 'Stammbäume verwalten' Dialog,
- klicke auf und erstelle einen neuen Stammbaum,
- lade den neuen Stammbaum
- Die Gramps XML oder das Gramps-Paket importieren.

Alternativ können möglicherweise die Wiederherstellungswerkzeuge verwendet werden. Siehe 'Beziehen der bsddb-Wiederherstellungswerkzeuge' unter [Beschädigten Stammbaum wiederherstellen](wiki:De:Defekten_Stammbaum_wiederherstellen) {{-}}

## Datenbankbeschädigung auf niedriger Ebene erkannt

![[_media/LowLevelDatabaseCorruptionDetected-dialog-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Dialogfeld "Datenbankbeschädigung auf niedriger Ebene erkannt" - Beispiel]]

Dieser Dialog wird angezeigt, wenn ein Problem mit der zugrunde liegenden Datenbank festgestellt wird, die Stammbäume unterstützt.

- schließe den Dialog,
- klicke auf die Stammbaumverwaltung,
- wähle den Stammbaum, den du versuchst zu öffnen,
- die Schaltfläche sollte verfügbar sein; klicke auf sie,
- Sobald der Stammbaum repariert wurde, sollte es möglich sein, ihn auf normale Weise zu öffnen.

Wenn dies nicht funktioniert, versuche die 'bsddb-Wiederherstellungswerkzeuge zu besorgen' unter [Beschädigten Stammbaum wiederherstellen](wiki:De:Defekten_Stammbaum_wiederherstellen) {{-}}

### Fehler in der Datenbank erkannt

![[_media/RunDatabaseRepair-40.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Dialogfeld "Datenbankreparatur ausführen"]]

Vorgeschlagene Maßnahme ausführen. {{-}}

## Warnungen

Wenn Gramps einen geringfügigen Fehler feststellt oder dich über ein Vorkommen im Programm informieren möchte, zeigt Gramps möglicherweise eine Schaltfläche in der Statusleiste an, wie unten gezeigt. Diese Schaltfläche wird nur 180 Sekunden lang angezeigt. Wenn du sie siehst, solltest du sofort darauf klicken, wenn du die Nachrichten sehen möchtest.

### Warnknopf

![[_media/Status-bar-warning-button-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Gramps-Hauptfenster mit Warnungsschaltfläche in der Statusleiste]] Der (Glühbirnen-Symbol) {{-}}

### Gramps Warnungen Dialog

![[_media/Gramps-warnings-dialog-example-60.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Gramps-Hauptfenster mit Warnmeldung und Kontextmenü]] Wenn du auf die Schaltfläche klickst, wird ein Dialogfeld mit Gramps-Warnungen angezeigt, in dem die letzten 20 empfangenen Nachrichten angezeigt werden.

Du kannst das Kontextmenü verwenden, um die Details in eine Textdatei zu kopieren.

Siehe [Weitere Details zum Logging-System](wiki:Logging_system) (englisch) {{-}}

Einige der möglicherweise auftretenden Warnungen werden nachfolgend beschrieben:

### Gebietsschema-Warnungen

Manchmal gibt es ein Problem mit der von dir gewählten Sprache.

Wenn du Gramps mit der Standardinstallationsmethode deiner Plattform (Paketmanager / AIO-Installationsprogramm / Anwendungspaket) installiert hast und den integrierten Mechanismus deiner Plattform (Systemeinstellungen / Systemsteuerung / Systemeinstellungen) verwendest, um die Sprache / Sortierreihenfolge / Formate auszuwählen, die du verwendest, sollten diese Fehler nicht auftreten und können bedeuten, dass ein Problem in Gramps vorliegt.

Wenn du jedoch die Sprache / Sortierreihenfolge / Formate manuell festgelegt hast, indem du die 'Umgebung' festlegst, siehe [Sprachen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Einstellungen#Sprache), insbesondere wenn du Gramps über die Befehlszeile ausführst, liegt möglicherweise ein Problem mit der Eingabe vor. Die Nachricht (Nur ein Teil davon ist unten dargestellt.) soll dir helfen, zu verstehen, wo der Fehler liegt.

- "Datumsparser für '% s' nicht verfügbar, verwende Standardeinstellung"
- "Datumsanzeige für '% s' nicht verfügbar, verwende Standardeinstellung"
- "Die Übersetzung für Familienbeziehungen ist für die Sprache '% s' nicht verfügbar. Verwende stattdessen 'Englisch'."
- 'Dein Gebietsschema kann nicht ermittelt werden, verwende Englisch'
- "Lokalisierungsbibliothek libintl nicht im %PATH%, Lokalisierung wird unvollständig sein"
- "Es wurden keine Übersetzungen für %s gefunden, wodurch die Lokalisierung auf US-Englisch eingestellt wurde."
- "Collator kann nicht erstellt werden: %s"
- "Keine Sprache angegeben, verwende US-Englisch"
- "Keine verwendbaren Sprachen in der Liste gefunden, verwende US-Englisch"
- "Keine der angeforderten Sprachen (%s) war verfügbar, stattdessen wurde %s verwendet."

### Modul nicht geladen Warnungen

Die Gramps-Anwendung enthält viele verschiedene 'Module'. Einige dieser Module sind erforderlich, damit Gramps überhaupt ausgeführt werden kann. Einige werden 'dringend empfohlen', andere sind optional.

Wenn du Gramps mit der Standardinstallationsmethode deiner Plattform (Paketmanager / AIO-Installationsprogramm / Anwendungspaket) installiert hast, hat der Ersteller dieses Pakets entschieden, welche Module vorhanden sind. Er muss alle erforderlichen Module aufnehmen, da Gramps sonst nicht ausgeführt wird. Er kann jedoch auswählen, welches der empfohlenen und optionalen Pakete er aufnimmt. Konsultiere die Dokumentation deines Pakets, um festzustellen, welche Module enthalten sind.

Wenn du versuchst, etwas zu tun, für das ein Modul erforderlich ist, das nicht enthalten ist, erhälts du eine Warnung wie die folgenden (nur der erste Teil der Nachricht ist enthalten). Was du dagegen tun kannst, hängt von deiner Plattform ab:

**Linux** Du solltest in der Lage sein, das Paket mit dem Standard-Paketmanager Deiner Distribution oder der GUI-Schnittstelle zum Paketmanager zu installieren. In einigen Fällen musst du das Modul jedoch aus dem Quellcode erstellen.

**MS Windows und macOS** Das MS Windows AIO-Installationsprogramm und das macOS-Anwendungspaket enthalten bestimmte Module. Der normale Benutzer kann keine weiteren Module hinzufügen. Wenn du also ein Modul findest, das deiner Meinung nach enthalten sein sollte, solltest du es auf der Gramps-[Forum](wiki:De:Kontakt#Offiziell) (wahrscheinlich der Bereich Entwicklung) veröffentlichen und erklären, warum du der Meinung bist, dass das Auslassen ein Fehler ist.

- "WARNUNG: PIL-Modul nicht geladen. "
- "ICU nicht geladen, da %s. Die Lokalisierung wird beeinträchtigt. "
- "OsmGpsMap Modul nicht geladen.. "
- "GExiv2 Modul nicht geladen. "
- "Webkit Modul nicht geladen. "
- "PIL (Python Imaging Library) nicht geladen. "
- "GtkSpell nicht geladen. "

#### Zeige Zusatzmodulstatusdialog bei Zusatzmodulladefehler

Ermöglicht die Anzeige eines Dialogs nach der [Plugin](wiki:De:Gramps_Glossar#plugin)-Registrierung beim Start von Gramps. Der Dialog meldet Plugins, die bei der Registrierung einen Fehler verursachen. Dies ermöglicht es Benutzern, Plugin-Probleme zu finden und zu beheben.

Der Dialog kann über die Option unterdrückt werden. im Register des Dialogs .

Die Fehlerbedingungen, die den Plugin-Fehlerstatusdialog auslösen würden, werden hauptsächlich in der Funktion \`load_plugin\` der Klasse \`PluginManager\` behandelt. Hier sind die wichtigsten Fehlerbedingungen:

1\. Fehler in der Plugin-Registrierungsdatei:

- Fehlende oder ungültige gramps_target_version ([gen/plug/\_manager](https://github.com/gramps-project/gramps/blob/maintenance/gramps52/gramps/gen/plug/_manager.py#L1050-L1056))
- Falsches Plugin-Versionsformat ([gen/plug/\_manager](https://github.com/gramps-project/gramps/blob/maintenance/gramps52/gramps/gen/plug/_manager.py#L1058-L1062))
- Fehlende erforderliche Attribute für den spezifischen Plugin-Typ ([gen/plug/\_manager](https://github.com/gramps-project/gramps/blob/maintenance/gramps52/gramps/gen/plug/_manager.py#L1064-L1068))

2\. Modul-Import-Fehler:

- Die Haupt-Python-Datei des Plugins kann nicht importiert werden ([gen/plug/\_manager](https://github.com/gramps-project/gramps/blob/maintenance/gramps52/gramps/gen/plug/_manager.py#L1070-L1074))

3\. Plugin-Initialisierungsfehler:

- Ausnahmen, die während des Initialisierungsprozesses des Plugins auftreten ([gen/plug/\_manager.py](https://github.com/gramps-project/gramps/blob/maintenance/gramps52/gramps/gen/plug/_manager.py#L1076-L1080))

4\. Versions-Inkompatibilität:

- Die gramps_target_version des Plugins stimmt nicht mit der laufenden Gramps-Version überein ([gen/plug/\_manager](https://github.com/gramps-project/gramps/blob/maintenance/gramps52/gramps/gen/plug/_manager.py#L1082-L1086))

5\. Doppelte Plugin-IDs:

- Es wurden mehrere Plugins mit der gleichen ID entdeckt ([gen/plug/\_manager](https://github.com/gramps-project/gramps/blob/maintenance/gramps52/gramps/gen/plug/_manager.py#L1088-L1092))

6\. Ungültiger Plugin-Typ:

- Der angegebene [PTYPE](wiki:Addons_development#Create_a_Gramps_Plugin_Registration_file) wird nicht erkannt ([gen/plug/\_manager](https://github.com/gramps-project/gramps/blob/maintenance/gramps52/gramps/gen/plug/_manager.py#L1094-L1098) und [gui/viewmanager](https://github.com/gramps-project/gramps/blob/maintenance/gramps52/gramps/gui/viewmanager.py#L615-L618))

### Konfigurationswarnungen

Manchmal lohnt es sich, einfach die alten Konfigurationsdateien zu löschen.

- "Importiere alte Schlüsseldatei 'keys.ini'..." (The `.gramps/keys.ini` Datei wurde in Gramps 3.2 abgeschafft, jetzt `.gramps/gramps``/gramps.ini` )
- "Der Import der alten Schlüsseldatei ist abgeschlossen 'keys.ini'"
- "Filter %s kann in den definierten benutzerdefinierten Filtern nicht gefunden werden"
- "Die Anzahl der Argumente stimmt nicht überein mit der Anzahl von " +
- "Wert '%(val)s' nicht gefunden für Option '%(opt)s'"
- "Letzte Datei%s kann nicht geöffnet werden weil %s",
- "WARNUNG: ignoriere alten Schlüssel '%s'"
- "WARNUNG: ignoriere Schlüssel mit falschem Typ "
- "Fehler beim Analysieren der Dokumentoptionen"
- "Eine Zeile in der addon Liste übersprungen: "
- "Fehler beim Laden von Gramplets von %s weil %s"

### Andere Warnungen

{{-}}

#### Ort Schleife gefunden Dialog

![[_media/PlaceCycleDetected-warning-dialog-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Ort Schleife gefunden" Warndialog]]

"Ort Schleife gefunden" Der Warnhinweis zeigte an, dass "Der Ort, den du hinzufügst, ist bereits Bestandteil " "dieses Ortes"

Siehe auch:

- [Teil von](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Daten_eingeben_und_bearbeiten:_Ausführlich_-_Teil_2#Teil_von)

{{-}}

#### Fehlendes Medium Dialog

Wenn eine Mediendatei beim Exportieren nicht gefunden wird, wird derselbe Dialog „“Fehlendes Medium“ angezeigt.

#### Datei konnte nicht geöffnet werden: <Dateipfad und Dateiname>

![[_media/Could-not-open-file-file-path-and-file-name-warning-dialog-example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} „Datei konnte nicht geöffnet werden: “ – (Warnfenster)]] Im [Dialogfeld „Stammbaum importieren“](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Stammbäume_Verwalten#Dialogfeld_Stammbaum_importieren) wird die Warnmeldung „Datei konnte nicht geöffnet werden: <Dateipfad und Dateiname>“ angezeigt, wenn du die Option „Alle Dateien“ auswählst und dann einen nicht unterstützten Dateiimporttyp auswählst.

Die Meldung lautet:

<hr>

Der Dateityp „xxx“ ist Gramps unbekannt.

Gültige Typen sind: Gramps-Datenbank, Gramps XML, Gramps-Paket, GEDCOM und andere.

{{-}}

#### Kann Person nicht speichern

![[_media/CannotSavePerson-dialog-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Kann Person nicht speichern (Warnfenster)]] Beim Versuch, eine Person ohne Daten aus dem Personeneditor zu speichern, wird dieses Warnfenster angezeigt. Du benötigst mindestens einen Buchstaben für den Vornamen. **Kann Person nicht speichern**  
Für diese Person existieren keine Daten. Bitte gib Daten ein oder brich die Bearbeitung ab.  
Schließen {{-}}

#### Kann <Objekt> nicht zusammenführen

![[_media/CannotMerge-object-warning-dialog-example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Person kann nicht zusammengeführt werden (Warndialog) - Beispiel]] Wenn du versuchst, etwas anderes als zwei (2) Datensätze eines Typs zusammenzuführen, wird dieses Warn-Popup-Dialogfeld angezeigt.

Zum Beispiel:

**Personen können nicht zusammengeführt werden**  
Es müssen genau zwei Personen ausgewählt werden, um eine Zusammenführung durchzuführen. Eine zweite Person kann ausgewählt werden, indem du die Steuerungstaste gedrückt hältst, während du auf die gewünschte Person klickst.

Schließen

{{-}}

Siehe:

- [Datensätze zusammenführen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Daten_eingeben_und_bearbeiten:_Ausführlich_-_Teil_3#Datens.C3.A4tze_zusammenf.C3.BChren)

#### Doppelte Familie Warnung Dialog

![[_media/DuplicateFamily-warning-dialog-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Doppelte Familie - Warnung Dialog]]

{{-}}

#### Warnung unterdrücken wenn zu einem Kind Eltern hinzugefügt werden

Kann aktiviert werden mit Option in dem [Einstellungen&gt; Warnungen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Einstellungen#Warnungen) Dialog.

{{-}}

##### Eltern zu einer Person hinzufügen Dialog

![[_media/AddingParetsToA-Person-warning-dialog-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Eltern zu einer Person hinzufügen" Warnung Dialog]]

{{-}}

#### Warnung unterdrücken wenn mit geänderten Daten abgebrochen wird

Kann deaktiviert werden durch die Option in dem Dialog.

Wird vom verwendet.

#### Änderungen speichern? Dialog

![[_media/SaveChanges-alert-dialog-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Änderungen speichern?" - Alarmdialog]]

Wenn Daten in einem der Registerkarten im Dialogfeld „Person bearbeiten“ geändert wurden, wird das Warnfenster angezeigt, in dem du zwischen folgenden Optionen wählen kannst:

- – Änderungen.

- (Standard) – die ursprüngliche Abbrechanforderung.

- – die Änderungen.

sowie ein Kontrollkästchen zum Aktivieren von , das über die Option im Dialogfeld deaktiviert werden kann.

{{-}}

#### Warnungen unterdrücken bei fehlendem Forscher beim Export nach GEDCOM

![[_media/xxx.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} xxx]]

Kann deaktiviert werden mit Option in dem [Einstellungen&gt; Warnungen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Einstellungen#Warnungen) Dialog.

{{-}}

#### Löschbestätigungsdialog

![[_media/Delete-confirmation-dialog-Undo-History-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Löschbestätigungsdialog für den Dialog „Rückgängig-Verlauf“]] Willst du den [Verlauf](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Navigation#Dialogfeld_R.C3.BCckg.C3.A4ngig-Verlauf) wirklich löschen? Wähl , um zu bestätigen, oder , um den Vorgang abzubrechen. {{-}}

#### Verlauf zurücksetzen Warnung

![[_media/UndoHistoryWarning-Tool-dialog-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Verlauf zurücksetzen Warnung" Dialog - Voreinstellung]]

Der Dialog wird angezeigt und du kannst entweder en oder . Es wird empfohlen, anzuhalten und die Datenbank zu sichern. Damit kannst du den Vorgang zum Ausführen des Werkzeug (oder Import) bei Bedarf zurücksetzen. {{-}} ![[_media/UndoHistoryWarning-Import-dialog-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Import &quot;Undo history warning&quot; dialog - default]] {{-}}

#### Kein ausgewähltes Buchelement

![[_media/No-selected-book-item-warning-60-de.png|Kein ausgewähltes Buchelement - Warnung]] Wenn du im Dialogfeld **Bücher verwalten** im Abschnitt **Aktuelles Buch** keinen Eintrag ausgewählt hast, wird im Dialogfeld [Buchbericht](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte_-_Teil_3#B.C3.BCcher) die Warnmeldung angezeigt. {{-}}

#### Person \<\_\_\_\_\> befindet sich nicht in der Datenbank

![[_media/xxx-52.png|Person &lt;____&gt; ist nicht in der Datenbank Warnungsdialog]]

Die Warnung wird angezeigt, wenn es sich bei der zentralen Person um eine Privatperson oder eine lebende Person handelt und die Filteroptionen auf der Registerkarte „Berichtsoptionen (2)“ die Einstellungen für Vertrauliche oder lebende Personen nicht zulassen verwenden.

{{-}}

#### Automatische Sicherung...

![[_media/Autobackup.notification.on.exit-52.png|&quot;Automatische Sicherung...&quot; -Benachrichtigung beim Beenden Warndialog]] Die **Bitte warte, bis die Sicherung abgeschlossen ist**. wird beim Beenden von Gramps angezeigt, um darauf hinzuweisen, dass eine automatische Sicherung im Gange ist.

Siehe auch:

- Registerkarte , Abschnitt [Verwaltung der Datensicherung](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Einstellungen#Verwaltung_der_Datensicherung) für die Optionen und .

<!-- -->

- [Sichern: Popup zur Anzeige des Gramps-Status hinzufügen \#1416](https://github.com/gramps-project/gramps/pull/1416)

#### Lesezeichen konnte nicht gesetzt werden

![[_media/Could-Not-Set-a-Bookmark-warning-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;Lesezeichen konnte nicht gesetzt werden&quot; Warnung Dialog]] Es konnte kein [Lesezeichen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Navigation#Lesezeichen_Navigation) gesetzt werden, da nichts ausgewählt war. {{-}}

#### Öffnen der Datenbank „<xxxxxxx>“

![[_media/Opening-the-xxxxxxx-database-warning-60.png|&quot;Öffnen der Datenbank &#39;&#39;“ Warnung Dialog]] Beim Versuch, den *Datenbanktyp* von BSDDB zu SQLite zu [konvertieren](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Stammbäume_Verwalten#Stammb.C3.A4ume.28verwaltungs.29fenster), wird möglicherweise der Warnhinweis „Öffnen der Datenbank ‚<xxxxxxx>‘“ angezeigt.

Der Versuch, die Datenbank zu konvertieren, ist fehlgeschlagen. Möglicherweise muss sie aktualisiert werden. {{-}}

## Fehler

Bei schwerwiegenderen Problemen wird ein Dialogfeld angezeigt, in dem die Maßnahmen beschrieben werden, die du ergreifen solltest.

{{-}}

### Fehlerbericht

![[_media/ErrorReport-dialog-collapsed-ErrorDetail-default-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Fehlerbericht-Assistent - Dialog - reduziert "Fehlerdetails" - Standard]]

Das Dialogfeld wird angezeigt, wenn in der Gramps-Anwendung etwas passiert ist, das die Programmierer nicht erwartet haben.

Lies den Artikel [Wie man einen guten Fehlerbericht erstellt](wiki:How_to_create_a_good_bug_report) (englisch). Wenn du glaubst, dass du weißt, wie die Gramps-Entwickler den Fehler reproduzieren könnten oder nicht, wähle die Schaltfläche , um das Dialogfeld zu starten, und folge den Anweisungen. {{-}} ![[_media/ErrorReport-dialog-expanded-ErrorDetail-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Fehlerbericht-Assistent - Dialog - erweitert &quot;Fehlerdetails&quot; - Standard]] {{-}}

### Dialogfeld Fehlerberichtsassistent

Ermöglicht es dir, einen Bericht über einen Fehler zu erstellen und ihn dann manuell an das Gramps-Fehlermeldesystem zu senden (Dazu musst du ein registriertes Konto im Gramps-Fehlerberichterstattungssystem haben und dich dann in dein Fehlerverfolgungskonto einloggen.)

- [Verwenden des Fehlermeldesystem](wiki:Using_the_bug_tracker) (englisch)

{{-}}

#### Einen Fehler berichten Seite

![[_media/ErrorReportingAssistant-ReportABug-page-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Fehler melden (Seite) - Assistent zur Fehlerberichterstattung]]

Dies ist der Fehlerberichtsassistent. Er ist hilfreich, den Gramps-Entwicklern einen Fehlerbericht zu erstellen, der so detailliert wie möglich ist.

Der Assistent stellt einige Fragen und sammelt Informationen über den gerade aufgetretenen Fehler und die Betriebsumgebung.

Am Ende des Assistentenprozesses wirst du aufgefordert, einen Fehlerbericht über das Gramps-Fehlerverfolgungssystem [Gramps bug tracking](https://gramps-project.org/bugs/my_view_page.php) einzureichen.

Der Assistent kopiert den Fehlerbericht in die Zwischenablage des Betriebssystems. Auf diese Weise kannst du ihn in das Formular der [Gramps-Fehlerverfolgung](https://gramps-project.org/bugs/my_view_page.php)\] einfügen und genau überprüfen, welche Informationen du einschließen möchtest. {{-}}

#### Fehler Details Seite

![[_media/ErrorReportingAssistant-ErrorDetails-page-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Fehlerdetails (Seite) - Fehlerberichterstattungsassistent (zeigt Beispielfehler)]]

Wenn du feststellst, dass der Fehler persönliche Informationen enthält, entferne diese bitte.

Dies sind die detaillierten Gramps-Fehlerinformationen. Mach dir keine Sorgen, wenn du sie nicht verstehst. Auf den folgenden Seiten des Assistenten hast du die Möglichkeit, weitere Details zum Fehler hinzuzufügen. {{-}}

#### Systeminformationsseite

![[_media/ErrorReportingAssistant-SystemInformation-page-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Systeminformationen (Seite) - Fehlerbericht-Assistent]]

Dies sind die Informationen zu deinem System, die den Entwicklern helfen, den Fehler zu beheben. {{-}}

#### Weitere Informationen Seite

![[_media/ErrorReportingAssistant-FurtherInformation-page-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Weitere Informationen (Seite) - Fehlerberichterstattungsassistent]]

Bitte gib so viele Informationen wie möglich darüber an, was du getan hast, als der Fehler aufgetreten ist.

Dies ist deine Gelegenheit, um zu beschreiben, was du getan hast, als der Fehler aufgetreten ist. {{-}}

#### Seite mit der Zusammenfassung des Fehlerberichts

![[_media/ErrorReportingAssistant-BugReportSummary-page-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Zusammenfassung des Fehlerberichts (Seite) - Assistent zur Fehlerberichterstattung]]

Dies ist der vollständige Fehlerbericht. Auf der nächsten Seite des Assistenten kannst du einen Fehler auf der Website des Gramps-Fehlerverfolgungssystems melden. {{-}}

#### Fehlerbericht senden Seite

![[_media/ErrorReportingAssistant-SendBugReport-page-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Fehlerbericht senden (Seite) - Assistent zur Fehlerberichterstattung]]

Verwende die beiden folgenden Schaltflächen, um zuerst den Fehlerbericht in die Zwischenablage zu kopieren und dann einen Webbrowser zu öffnen, in dem du einen Fehlerbericht ablegen kannst unter <https://gramps-project.org/bugs/login_select_proj_page.php?ref=bug_report_page.php>

- \- Dies ist der letzte Schritt. Verwende die Schaltflächen auf dieser Seite, um einen Webbrowser zu starten und einen Fehlerbericht über das Gramps-Fehlerverfolgungssystem einzureichen. (Dazu musst du ein registriertes Konto im Gramps-Fehlerberichterstattungssystem haben und dich dann in dein Fehlerverfolgungskonto einloggen.)

  - \- Verwende diese Schaltfläche, um einen Webbrowser zu starten und einen Fehlerbericht auf dem Gramps-Fehlerverfolgungssystem einzureichen.

  - \- Verwende diese Schaltfläche, um den Fehlerbericht in die Zwischenablage zu kopieren. Gehe dann über die Schaltfläche unten zur Website zur Fehlerverfolgung, füge den Bericht ein und klicke auf Bericht senden

{{-}}

#### Abschließen Seite

![[_media/ErrorReportingAssistant-Complete-page-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Vollständig (Seite) - Fehlerberichterstattungsassistent]]

Gramps ist ein Open Source-Projekt. Der Erfolg hängt von den Nutzern ab. Benutzerfeedback ist wichtig. Vielen Dank, dass du dir die Zeit genommen hast, einen Fehlerbericht einzureichen. {{-}}

### Andere Fehler

#### Bericht konnte nicht erstellt werden

![[_media/xxxx.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Bericht konnte nicht erstellt werden Dialog]]

Das Dialogfeld kann aus verschiedenen Gründen auftreten, z. B.: Ein Grund ist, dass das benutzerdefinierte Papierformat, das du für den Bericht ausgewählt hast, für das verwendete PDF-Format zu groß ist.

## Alle Fehlermeldungen anzeigen

Manchmal werden nicht alle Informationen auf dem Bildschirm angezeigt, die erforderlich sind, um zu verstehen, was schief gelaufen ist. Wenn du beispielsweise Gramps mit einer ungültigen Spracheinstellung (und einigen fehlenden Komponenten) startest, wird im Dialogfeld folgende Meldung angezeigt:

![[_media/Warning_message_GExiv2-40.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Dialog zeigt eingeschränkte Warnungen]] {{-}} Der vollständige Satz der Warnmeldungen lautet jedoch:

`(process:10929): Gtk-WARNING **: Locale not supported by C library.`  
`   Using the fallback 'C' locale.`  
`2013-03-13 18:49:04.376: WARNING: __init__.py: line 69: Date parser for 'xx_XX.UTF-8' not available, using default`  
`2013-03-13 18:49:04.547: WARNING: __init__.py: line 85: Date displayer for 'xx_XX.UTF-8' not available, using default`  
`2013-03-13 18:49:05.949: WARNING: spell.py: line 74: Spelling checker is not installed`  
`2013-03-13 18:49:16.023: WARNING: gramplet.gpr.py: line 400: WARNING: GExiv2 module not loaded.  Image metadata functionality will not be available.`

Manchmal startet Gramps einfach nicht und es wird nichts auf dem Bildschirm angezeigt, oder Gramps wird plötzlich beendet, sodass du nichts auf dem Bildschirm siehst. In all diesen Fällen musst du möglicherweise etwas Besonderes tun, um alle Fehler anzuzeigen.

### Linux

Du kannst Gramps über die Befehlszeile starten, wie im Hinweis [hier](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Erste_Schritte#Linux) beschrieben. Du siehst dann alle Diagnoseinformationen auf dem Terminal.

### MS Windows

Du kannst Gramps über die Befehlszeile starten, wie im Hinweis [hier](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Erste_Schritte#MS_Windows) beschrieben. Du siehst dann alle Diagnoseinformationen auf dem Terminal.

### macOS

Das Starten von Gramps über die CLI auf macOS wird [hier](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Kommandozeilen_Referenz#macOS) behandelt.

#### Konsolenanwendung

Du kannst auch Protokollnachrichten von Gramps mithilfe der Apple anzeigen. Die Konsolenanwendung befindet sich im Ordner "Dienstprogramme" deines Mac, der sich im Ordner "Anwendungen" befindet. (Eine Kurzform auf neueren Versionen von macOS besteht darin, Befehl und die Leertaste zu drücken, um eine Spotlight-Suche zu starten. Gib im daraufhin angezeigten Popup-Fenster die ersten Zeichen des Wortes "Konsole" ein und wählen dann die Konsolenanwendung aus.)

Zum Beispiel würde eine der frühen Alpha-Versionen von Gramps einfach nicht gestartet und nichts auf dem Bildschirm angezeigt. Durch Öffnen der Konsolenanwendung und Eingeben von Gramps in den Filter in der oberen rechten Ecke wurden jedoch einige Diagnoseinformationen angezeigt. (Eigentlich haben wir "gramps\[" eingegeben, weil es einige andere Nachrichten gab, die nicht relevant waren, aber es wäre egal, ob sie auch enthalten waren). ![[_media/Console_output-40.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Konsolenausgabe]] {{-}} Wenn du bei gedrückter Umschalttaste alle relevanten Nachrichten auswählst und kopierst, erhältst du:

`01/03/2013 00:08:02 [0x0-0x88088].org.gramps-project.gramps[1867] 2939: ERROR: importer.py: line 51: Could not find any typelib for Gtk `  
`01/03/2013 00:08:05 [0x0-0x88088].org.gramps-project.gramps[1867] Gtk typelib not installed. Install Gnome  Introspection, and pygobject version 3.3.2 or later. `  
`01/03/2013 00:08:05 [0x0-0x88088].org.gramps-project.gramps[1867] Gramps will terminate now. `

In diesem speziellen Fall war dies ausreichend, um dem Entwickler zu helfen, das Problem zu erkennen.

{{-}}

[F](wiki:Category:De:Dokumentation) [F](wiki:Category:Troubleshooting)
