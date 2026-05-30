---
title: 'De:Gramps 6.0 Wiki Handbuch - Daten eingeben und bearbeiten: Ausführlich -
  Teil 2'
categories:
- De:Dokumentation
- Stub
managed: false
source: wiki-scrape
wiki_revid: 131305
wiki_fetched_at: '2026-05-30T17:41:36Z'
lang: de
---

{{#vardefine:chapter\|9.2}} {{#vardefine:figure\|0}} **<span style="font-size:120%">Daten eingeben und bearbeiten: Ausführlich Ereignisse, Medien, Orte, Quellenangaben, Notizen</span>**  
Der vorherige Abschnitt bot dir einen detaillierten Überblick über die Eingabe und Bearbeitung von Daten für Personen, Beziehungen und Daten. Dieser Abschnitt wird mit anderen Objekten fortgesetzt, denen du in Gramps begegnest.

## Informationen über Ereignisse bearbeiten

![[_media/EventsCategory-EventsListView-example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Ereigniskategorie - Ereignis (Liste) Ansicht - Beispiel]]

Durch Hinzufügen eines Ereignisses zu einer Person kannst du gefundene Informationen aufzeichnen.

Wenn du der ein Ereignis hinzufügst, wird das Dialogfeld angezeigt.

Um Ereignisdaten hinzuzufügen oder zu bearbeiten, wechsle zur und wähle den gewünschten Eintrag in der Liste der Ereignisse aus. Doppelklicke auf diesen Eintrag oder klicke in der Symbolleiste auf , um das folgende Dialogfeld aufzurufen. {{-}}

### Neues Ereignis Dialog

![[_media/EditEvent-dialog-example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Ereignis bearbeiten - Dialog - Beispiel]] Wenn Ereignisse über den Dialog bearbeitet werden. Dieser Dialog kann aufgerufen werden durch: Doppelklick auf eine Zeile in der Ereignis-Kategorienansicht. Ereignisse können auch in der Registerkarte [-Registerkarte](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Daten_eingeben_und_bearbeiten:_Ausführlich_-_Teil_1#Ereignisse) des -Dialogfensters oder über die Registerkarte [-Registerkarte](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Daten_eingeben_und_bearbeiten:_Ausführlich_-_Teil_1#Ereignisse_2) des Dialogfelds Dialogs. Bei der Bearbeitung von Ereignissen über den Personeneditor oder den Familieneditor wird der [Ereignisreferenzeditordialog](#Ereignisreferenzeditordialog) verwendet.

Im oberen Teil kannst du Grundinformationen über das Ereignis ansehen und bearbeiten:

- Die kann aus den verfügbaren Typen ausgewählt werden, die im Dropdown-Menü Ereignisart aufgeführt sind. Zum Beispiel **Geburt** (*Standard*), Taufe, Tod, Beerdigung usw. Gramps  
  Du kannst deine eigene [benutzerdefinierte Ereignisart](wiki:De:Gramps_Glossar#benutzerdefiniert) eingeben, indem du direkt in das [Textfeld des Kombinationsfeldes](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Hauptfenster#Auswahl-Kombinationsfelder) der Auswahl eintippst.
- Das des Ereignisses kann ein exaktes Datum, ein Zeitraum (*von ... bis ..., zwischen ...*) oder ein ungenaues Datum (*um ...*) sein.
  - ![[_media/22x22-gramps-date.png]] Schaltfläche öffnet den Dialog.
- Das Feld gibt dir die Möglichkeit eine längere Beschreibung für dieses Ereignis einzugeben.
  - \- Schaltet die Datenschutzsperre um, um den Ereignisdatensatz als privat zu markieren, sodass er in Berichten weggelassen werden kann.
- Der kann aus einer Liste bereits eingegebener Orte mit der Schaltfläche ausgewählt oder mit der Schaltfläche neu eingegeben werden. Zusätzlich kannst du einen Ortseintrag durch drag und drop in dieses Feld ziehen.
- Die ist eine eindeutige Identifikation des Ereignisses. Lasse das Feld leer, um Gramps das automatische Erstellen einer ID zu erlauben
- Mit den kannst du eine vorhandene Markierung über die Schaltfläche auswählen.

Am unteren Rand des Fensters befinden sich die Schaltflächen und . Wenn du auf klickst, werden alle in den Registerkarten vorgenommenen Änderungen übernommen und das Dialogfenster geschlossen, es sei denn, du hast keine Daten eingegeben. In diesem Fall wird die Warnmeldung angezeigt. Wenn du auf die Schaltfläche klickst, wird das Fenster geschlossen, ohne dass Änderungen übernommen werden. Wenn du auswählst, gelangst du hierher.

#### Neues Ereignis Registerkarten

Der zentrale Bereich des Fensters zeigt Notizbuchreiter mit verschiedenen Kategorien von Informationen. Klicke auf einen Reiter, um seinen Inhalt anzusehen oder zu bearbeiten. Die Reiter bieten die folgenden Informationskategorien der Ereignisdaten:

##### Quellenangaben

  
Der Reiter lässt sie Quellen zu diesem Ereignis ansehen und bearbeiten. Der zentrale Bereich des Fensters listet all solche Quellenreferenzen, die in der Datenbank gespeichert sind. Die Schaltflächen , und ermöglicht dir das Hinzufügen, ändern und entfernen einer Quellenreferenz die mit einem Ereignis verknüpft ist. Beachte, dass die und Schaltflächen nur verfügbar sind, wenn eine Quellenreferenz aus der Liste gewählt ist.

##### Notizen

  
Der Reiter bietet die Möglichkeit Notizen oder Kommentare zu einen Ereignis aufzuzeichnen. Um eine Notiz hinzuzufügen oder eine bestehende Notiz zu ändern, bearbeite einfach den Text im Texteingabefeld.

##### Galerie

  
Der Reiter

##### Attribute

  
Der Reiter

##### Referenzen

  
Der Reiter

{{-}}

#### Ereignis kann nicht gespeichert werden – Warnung Dialog

![[_media/Cannot-save-event-warning-dialog-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Ereignis kann nicht gespeichert werden – Warnung Dialog]]

-Warnung. Für dieses Ereignis sind keine Daten vorhanden. Bitte gib Daten ein oder brich die Bearbeitung ab. Klicke auf , um zum zurückzukehren. {{-}}

## Ereignisreferenzen bearbeiten

Ereignisreferenzen verbinden ein Ereignis mit einer Person und ermöglichen es dir zusätzliche Informationen über das Ereignis zu liefern.

Wenn du Ereignisreferenzen zu Reiter hinzufügst, öffnet sich der Dialog.

{{-}}

### Ereignisreferenzeditordialog

Zugriff auf den [Referenzobjekteditor](wiki:De:Gramps_Glossar#reference_object_editor).

![[_media/EventReferenceEditor-dialog-default-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Ereignisreferenzeditor - Dialog]]

Der Dialog enthält zwei Hauptrubriken, und .

- Der Bereich zeigt die Details, die mit dieser Ereignisreferenz verbunden sind: , , , .
- Die enthält : , , , , , .

{{-}}

#### Referenzinformation

##### Informationen zu Referenz Registerkarten

###### Allgemeines

Verwende für die der Person in diesem Ereignis das \[De:Gramps_Glossar#selector_combo_box\|Kombinationsfeld\]\] Rollenauswahl. Wähle für den Hauptbegünstigten die Option [Primär](wiki:De:Gramps_Glossar#primär) (dies ist die Standardeinstellung beim Hinzufügen einer Veranstaltung). Wähle eine beschreibende Ereignisrolle (z.B. [Adjutant](wiki:De:Gramps_Glossar#aide), [Braut](wiki:De:Gramps_Glossar#Braut), [Zelebrant](wiki:De:Gramps_Glossar#Zelebrant), Geistlicher, [Familie](wiki:De:Gramps_Glossar#Familie), [Taufpate](wiki:De:Gramps_Glossar#Taufpate), [Bräutigam](wiki:De:Gramps_Glossar#Bräutigam), [Informant](wiki:De:Gramps_Glossar#Informant), [Zeuge](wiki:De:Gramps_Glossar#Zeuge)) für Ereignisse, bei denen die Person nicht der Hauptbeteiligte ist.

Ereignissen, die einer Person über die Freigabe oder per Drag'n'Drop hinzugefügt wurden, wird standardmäßig die Rolle **[Unbekannt](wiki:De:Gramps_Glossar#unbekannt)** zugewiesen. Wenn die Person eine gleiche Rolle innehat, setze ihre Rolle ebenfalls auf Primär.

Wenn keine der vordefinierten Rollen geeignet ist, füge eine *[benutzerdefinierten](wiki:De:Gramps_Glossar#benutzerdefiniert)*' Rolle in das Textfeld des \[De:Gramps_Glossar#selector_combo_box\|Kombinationsfeldes\]\] ein. Durch Eingabe des neuen, eindeutigen Rollennamens (anstatt einer Auswahl aus dem Pulldown-Menü) wird eine neue benutzerdefinierte Rolle erstellt. Neue benutzerdefinierte Rollen werden der Liste des Pulldown-Menüs hinzugefügt. Sie bleiben dort, bis die Struktur exportiert und wieder importiert oder mit einem [Zusatzmodul eines Drittanbieters](wiki:Third-party_Addons) wie [Typbereinigung](wiki:Addon:Types_Cleanup_Tool) bereinigt wird.

Einige Beispiele für benutzerdefinierte Arten für Ereignisrollen werden im Artikel [Rollen, Beziehungen und Assoziationen](wiki:Roles,_Relationships_%26_Associations) vorgeschlagen. {{-}}

###### Quellenangaben

{{-}}

###### Attribute

###### Notizen

{{-}}{{-}}

#### Geteilte Information

{{-}}

###### Allgemeines

{{-}}

###### Quellenangaben

{{-}}

###### Attribute

{{-}}

###### Notizen

{{-}}

###### Galerie

{{-}}

###### Referenzen

{{-}}

## Informationen über Medienobjekte bearbeiten

Um Medienobjekte hinzuzufügen oder zu bearbeiten, wechsle zur kategorieansicht und wähle für vorhandene Medienobjekte den gewünschten Eintrag in der Medienliste aus. Doppelklicke auf diesen Eintrag oder klicke in der Symbolleiste auf , um das Dialogfeld zu öffnen und die vorhandenen Informationen zu bearbeiten. Oder wähle in der Symbolleiste die Schaltfläche , um sowohl das Dialogfeld als auch das Dialogfeld anzuzeigen, in dem du die Details des Medienobjekts auswählen und ändern kannst, bevor du es hinzufügst.

### Neues Medium Dialog

![[_media/NewMediaEditor-dialog-example-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Neues Medium Editor - Dialog - Beispiel zeigt Medieneigenschaften]]

Im oberen Bereich wird eine Miniaturansicht des Medienobjekts angezeigt, sofern verfügbar, sowie eine Zusammenfassung seiner Eigenschaften (ID, Datum, Pfad und "Objekttyp"), die du anzeigen und bearbeiten kannst. Du kannst diese Informationen direkt in die entsprechenden Felder eingeben.

- Ein beschreibender für dieses Medienobjekt. Entweder automatisch basierend auf dem Dateinamen des Medienobjekts generiert oder manuell eingegeben.

- Die ist ein eindeutiger Wert zum identifizieren des Medienobjekts, lass sie Gramps erstellen.
  - Datenschutz für dieses Medienobjekt umschalten (Vorgabe) oder

- Gib ein Datum ein, das mit dem Medienobjekt verbunden ist (z. B. könnte es bei einem Bild das Aufnahmedatum sein). Du kannst auch Folgendes verwenden:

  - ![[_media/22x22-gramps-date.png]] Schaltfläche um das Dialogfeld **** aufzurufen.

- des Medienobjekts auf deinem Computer. Gramps speichert die Medien nicht intern, sondern nur den Pfad! Leg den in den fest, damit du das gemeinsame Basisverzeichnis, in dem alle deine Medien gespeichert sind, nicht immer wieder neu eingeben musst. Das kann dir dabei helfen, die Pfade einer Sammlung von Medienobjekten zu verwalten.

  - Schaltfläche.

- Die Schaltfläche öffnet das Dialogfeld , in dem du vorhandene benutzerdefinierte Etiketten entfernen oder zuweisen kannst.

Im unteren Bereich des Fensters werden vier Notizbuchregisterkarten mit verschiedenen Informationskategorien angezeigt. Klicke auf eine Registerkarte, um deren Inhalt anzuzeigen oder zu bearbeiten. Im unteren Bereich des Fensters befindet sich die Schaltfläche , über die du hierher gelangst, die Schaltfläche , mit der du das Fenster ohne Übernehmen der Änderungen schließt, und die Schaltfläche , mit der du alle in allen Registerkarten vorgenommenen Änderungen übernimmst und das Dialogfeld schließt.

Durch Doppelklicken auf die -Miniaturansicht wird das Medienobjekt in einem externen Viewer geöffnet, sofern verfügbar.

#### Medienobjekt kann nicht gespeichert werden Warnung Dialog

![[_media/Cannot-save-media-object-warning-dialog-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Medienobjekt kann nicht gespeichert werden - Warnung Dialog]]

Der Warnung Dialog wird angezeigt, wenn du nicht genug Infos über das neue Medienobjekt eingegeben hast. Bitte gib die Daten ein oder brich die Bearbeitung ab. {{-}}

### Neues Medium Registerkarten

Die Reiter stehen für folgende Gruppen von Mediendaten:

- 

- \+

- 

- 

#### Quellenangaben

Auf der Registerkarte kannst du ...

#### Attribute

Der Reiter ermöglicht das Ansehen und Bearbeiten bestimmter Informationen über das Medienobjekt, die als Attribute formuliert werden können. Der untere Teil zeigt eine Liste all solcher Attribute, die in der Datenbank gespeichert sind. Der obere Teil zeigt die Details des zur Zeit aus der Liste gewählten Attributs (wenn vorhanden). Die Schaltflächen , , und ermöglichen ihnen das Hinzufügen, Modifizieren und Entfernen eines Attributs. Beachte das die und Schaltflächen nur verfügbar sind wenn ein Attribut aus der Liste gewählt ist.

#### Notizen

Der Reiter bietet einen Platz um Informationen zu speichern, die nicht ordentlich in eine andere Kategorie passen. Dieser Bereich ist besonders nützlich zum aufzeichnen von Informationen, die normalerweise nicht in die "Parameter-Wert" Paare der Attribute passen. Zum hinzufügen einer Notiz oder ändern einer bestehenden Notiz einfach den Text im Texteingabefeld bearbeiten.

#### Referenzen

Der Reiter zeigt jeden Datensatz an, der sich auf das gegebene Medienobjekt bezieht. Die Liste kann nach jeder ihrer Spaltenüberschriften sortiert werden: `Typ` , `ID` oder `Name`. Doppel-klicken auf einen Eintrag ermöglicht ihnen das Ansehen und Bearbeiten des entsprechenden Datensatzes.

{{-}}

## Medienobjektreferenzen bearbeiten

Wenn Medienobjektreferenzen ein Medienobjekt mit einem anderen Objekt auf der Registerkarte verbinden, wird über die Schaltfläche die aufgerufen. Sobald du ein Medienobjekt ausgewählt hast, wird das Dialogfeld angezeigt.

{{-}}

### Medienobjekt-Dateiauswahl auswählen

![[_media/SelectAMediaObject-file-selector-dialog-example-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Medienobjekt auswählen – (Datei-)Auswahldialog – Beispiel]]

Mit der [Dateiauswahl](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Einstellungen#Dateiauswahl) kannst du eine Vorschau anzeigen und eine Mediendatei auswählen, die du anhängen möchtest. Gleichzeitig kannst du den angezeigten bearbeiten: (Standardmäßig wird der Dateiname ohne Dateierweiterung verwendet.)

- (das Kontrollkästchen ist standardmäßig deaktiviert, bis es zum ersten Mal aktiviert und für jede nachfolgende Bildauswahl gemerkt wird.)

Siehe auch:

- [Medienobjekt wählen Auswahl](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Daten_eingeben_und_bearbeiten:_Ausführlich_-_Teil_1#Medien_Objekt_w.C3.A4hlen_Auswahl)
- [Medienpfad des Stammbaums &gt; Basismedienpfad:](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Einstellungen#Medienpfad_des_Stammbaums)

<!-- -->

- [](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Werkzeuge#Medienverwaltung) eine Gruppe von vier einzelnen Werkzeugen, von denen zwei es dir ermöglichen:
  - 

  - 

{{-}}

### Medienreferenzeditor Dialog

![[_media/MediaReferenceEditor-dialog-collapsed-example-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Medienreferenzeditor - Dialog - eingeklappt Vorgabe Beispiel]]

Der Dialog.

Siehe auch [Wie man Bildreferenzregionen erstellt](wiki:How_to_create_image_reference_regions) {{-}} ![[_media/MediaReferenceEditor-dialog-expanded-example-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Medienreferenzeditor - Dialog - &quot;Geteilte Information&quot; Bereich aufgeklappt Beispiel]]

Du darfst auch den **Geteilte Information** Bereich aufklappen.

{{-}}

#### Oberer Bereich

##### Oberer Bereich Registerkarten

###### Allgemeines

- Bereich (Ecken x1, x2, y1, y2)

Der Abschnitt ermöglicht das Auswählen eines bestimmten Bereich des Medienobjekts. Du kannst den Mauscursor zur Auswahl eines Bereichs aus dem Bild verwenden, oder diese "Spin" Schaltflächen zum setzen der oberen linken und untere rechte Ecke des referenzierten Bereichs zu setzen. Punkt (0,0) ist die obere linke Ecke und Punkt (100,100) die untere Rechte Ecke des Bildes.

- Privat

Die Schaltfläche ermöglicht dir zu markieren, ob dieser Datensatz als privat zu betrachten ist oder nicht. Aktiviere das Datensatz Kästchen um diesen zu markieren.

Siehe auch der [Erzählende Website](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte_-_Teil_7#Seitengenerierung) Galerie Reiter unterstützt die Ausgabe dieser referenzierten Regionen.

{{-}}

###### Quellenangaben

{{-}}

###### Attribute

{{-}}

###### Notizen

{{-}}

#### Geteilte Information

##### Geteilte Information Registerkarten

###### Allgemeines

{{-}}

###### Referenzen

{{-}}

###### Quelle Fundstellen

{{-}}

###### Attribute

{{-}}

###### Notizen

{{-}}

## Informationen über Orte bearbeiten

Um Informationen über Orte zu bearbeiten, wechsle in die und wähle den gewünschten Eintrag aus der Liste der Orte. Klicke den Eintrag doppelt oder klicke auf die Schaltfläche in der Werkzeugleiste um den Dialog zu öffnen:

{{-}}

### Orteditor Dialog

![[_media/PlaceEditor-dialog-example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Orteditor - Dialog - Beispiel für einen bestehenden Ort]]

Um einen neuen Ort hinzuzufügen oder Informationen zu bestehenden Orten zu bearbeiten, wechsle zur Kategorie „Orte“ und wähle den gewünschten Eintrag aus der Liste der Orte aus. Doppelklicke auf diesen Eintrag oder klicke in der Symbolleiste auf die Schaltfläche , um das folgende Dialogfeld aufzurufen:

Folgende Felder stehen zur Verfügung:

- Der Titelbereich oben zeigt die Beschreibung dieses Ortes an, der in Berichten verwendet werden soll. Gramps wird diese für dich konstruieren. Siehe Abschnitt \> generieren Option.

- 

  - Die Schaltfläche öffnet das Dialogfeld , in dem du zusätzliche Informationen hinzufügen/bearbeiten kannst.

- 

### Orteditor Registerkarten

Die Registerkarten stehen für die folgenden Kategorien von Ortsdaten:

- 

- 

- 

- 

- 

- 

- 

#### Teil von

![[_media/PlaceEditor-EnclosedBy-tab-example-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Teil von" Reiter vom "Ort Editor" - Dialog - Beispiel]]

Orte in Gramps werden in einer Hierarchie gespeichert. Der Reiter ermöglicht es dir diesen Ort mit anderen, in der Hierarchie höheren, Orten zu verknüpfen, welche ihn beinhalten. Jeder Link besteht aus einem Ort und optional aus einem Zeitraum.

Um einen bestehenden Ort mit einzuschließen, verwende die Schaltfläche , um einen Ort aus dem [Ort auswählen](#Ort_auswählen) auszuwählen. Alternativ dazu kannst du einen Ort (aus der Zwischenablage, der Ortskategorie-Ansicht oder einem Ereigniseditor) in den unteren Bereich der Registerkarte ziehen.

Mit den Schaltflächen , und kannst du einen neuen Ort als einschließende Hierarchieebene hinzufügen, den ausgewählten einschließenden Ort ändern und eine ausgewählte Verknüpfung zu einem einschließenden Ort entfernen.

Beachte, dass die Schaltflächen , und Neuordnung (nach oben, nach unten) nur verfügbar sind, wenn ein Link existiert und in der Liste ausgewählt wurde. Im Allgemeinen ist ein Land ein übergeordneter Ort, der mit keinem anderen Ort verknüpft ist.

**Siehe auch**

- [Teil von](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Gramplets#Teil_von) Gramplet
- [Die Zwischenablage verwenden](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Navigation#Die_Zwischenablage_verwenden)

{{-}}

##### Ort wählen Auswahl

![[_media/SelectPlace-SelectorDialog-example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Ort wählen - Auswahl Dialog - Beispiel]]

Im Dialogfeld kannst du eine Verknüpfung zu einem bereits vorhandenen Ort herstellen. Nach der Auswahl wird dieser im geöffnet

Du kannst die Schaltfläche verwenden, um die Liste basierend auf einer der Optionen aus der Dropdown-Liste zu filtern:

- **Name enthält** (Standardeinstellung)
- *Name enthält nicht*
- *ID enthält*
- *ID enthält nicht*
- *Art enthält*
- *Art enthält nicht*
- *Titel enthält*
- *Titel enthält nicht*
- *Letzte Änderung enthält*
- *Letzte Änderung enthält nicht*

Die Schaltfläche setzt den Filter zurück.

Wenn kein Datensatz ausgewählt wurde, springt der Bildlauf nach dem Leeren an den Anfang der Liste. Wenn jedoch eine Zeile aus den „Finden“-Ergebnissen ausgewählt wurde, wird der Bildschirm nach dem Löschen des Filters auf das ausgewählte Element zentriert, anstatt an den Anfang zu springen.

{{-}} Siehe auch:

- [Auswahldialoge](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Einstellungen#Auswahldialoge)

##### Ort Referenzeditor

![[_media/PlaceReferenceEditor-dialog-example-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Ortsreferenzeditor - Dialog - Beispiel]]

Im zweiten Teil des Fensters werden sieben Notizbuchregisterkarten mit verschiedenen Informationskategorien angezeigt. Klicke auf eine Registerkarte, um deren Inhalt anzuzeigen oder zu bearbeiten. Im unteren Teil des Fensters befinden sich die Schaltflächen und . Wenn du auf klickst, werden alle auf allen Registerkarten vorgenommenen Änderungen übernommen und das Dialogfenster geschlossen. Durch Klicken auf die Schaltfläche wird das Fenster geschlossen, ohne dass Änderungen vorgenommen werden.

{{-}}

#### Alternative Namen

  
Der Reiter ermöglicht dir die Ansicht und das Bearbeiten von sonstigen Namen unter denen der Ort bekannt sein könnte. Der Reiter listet alle sonstigen Namen des Ortes aus der Datenbank. Die Schaltflächen , , und ermöglichen dir das Hinzufügen, Bearbeiten und Entfernen eines Namendatensatzes. Beachte, das die und Schaltflächen nur verfügbar sind, wenn ein Name aus der Liste gewählt ist.

#### Quellenangaben

  
Der Reiter ermöglicht dir das Ansehen und Bearbeiten von Quellen, die für den Ort relevant sind. Der zentrale Bereich des Fensters listet all diese Quellenreferenzen, die in der Datenbank gespeichert sind. Die Schaltflächen , , und ermöglichen dir das Hinzufügen, Bearbeiten und Entfernen einer Quellenreferenz, die mit dem Ort verbunden ist. Beachte das die und Schaltflächen nur verfügbar sind wenn ein Quellen Referenz aus der Liste gewählt ist.

#### Notizen

  
Der Reiter zeigt jeden Kommentar oder Notiz die mit dem Ort in Verbindung stehen. Zum hinzufügen einer Notiz oder ändern einer bestehenden Notiz einfach den Text im Texteingabefeld bearbeiten.

#### Galerie

  
Der Reiter ermöglicht dir das Speichern und Anzeigen von Fotos und anderen Medienobjekten, die mit dem Ort in Verbindung stehen. Der zentrale Bereich des Fensters listet all diese Medienobjekte und gibt dir eine Miniaturvorschau von Bilddateien. Andere Objekte wie Audiodateien, Videodateien usw. werden durch Gramps typische Symbole dargestellt. Die Schaltflächen , , und ermöglichen dir das hinzufügen neuer Bilder, das Hinzufügen einer Referenz zu einem bestehenden Bild und das Entfernen von Medienverknüpfungen zu dem Ort. Beachte das die und Schaltflächen nur verfügbar sind wenn ein Medienobjekt aus der Liste gewählt ist.

#### Internet

  
Der Reiter enthält für den Ort relevante Internetadressen. (Diese Registerkarte verhält sich genauso wie die Registerkarte [Internet](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Daten_eingeben_und_bearbeiten:_Ausführlich_-_Teil_1#Internet) für den Personen-Editor und auch der \[\[De:Gramps_6.0_Wiki_Handbuch\_-\_Daten_eingeben_und_bearbeiten:\_Ausführlich\_-\_Teil_1#Internetadresseneditor\|Internet-Adress-Editor\] ist derselbe).

<!-- -->

  
Der untere Teil des Fensters listet all diese Adressen aus der Datenbank. Der obere Teil zeigt die Details der aktuell gewählten Adresse (wenn vorhanden). Die Schaltflächen , und ermöglichen dir das Hinzufügen, Bearbeiten und Entfernen von Internetadressen. Die Schaltfläche (dargestellt durch ein Symbol mit einem grünen Pfeil und einem gelben Kreis) öffnet deinen Browser und bringt dich zu der Webseite die zu der markierten Internetadresse gehört. Beachte das die , und Schaltflächen nur verfügbar sind wenn eine Adresse aus der Liste gewählt ist.

#### Referenzen

  
Der Reiter zeigt alle Datensätze (Ereignisse oder LDS Riten), die sich auf diesen Ort beziehen. Diese Information kann nicht im Dialog geändert werden. Stattdessen muss der entsprechende Ereignis (z.B., ein Geburt Ereignis) geöffnet werden und seine Ortsreferenz bearbeitet werden.

{{-}}

### Ortsnamenseditor Dialog

![[_media/PlaceNameEditor-dialog-default-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Ortsnamenseditor Dialog - Standard]]

Das Dialogfeld wird aus dem Dialog über die Schaltflächen aufgerufen.

Im Dialogfeld kannst du die folgenden Informationen hinzufügen/bearbeiten:

- der Name des Ortes

- Datumsbereich, in dem der Ort gültig ist

  - ![[_media/22x22-gramps-date.png]] Schaltfläche

- Sprache, in der der Name geschrieben ist. Gültige Werte sind beispielsweise zweistellige ISO-Codes: en, fr, de, nl. Die vollständige Liste der gültigen [ISO 639-1-Codes](https://de.wikipedia.org/wiki/Liste_der_ISO-639-1-Codes) findest du in Wikipedia.

{{-}}

### Unterstützte Längen/Breiten Formate

Wenn du einen Ort erstellst/bearbeitest, das sind die möglichen Formate für Koordinaten:

<table>
<thead>
<tr>
<th colspan="2"><p>Längen- und Breitengradformate</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p>D.D4</p></td>
<td><p>Gradnotation, 4 Nachkommastellen</p>
<dl>
<dt></dt>
<dd>
z.B. +12.0154 , -124.3647
</dd>
<dd>
4 <a href="https://wikipedia.org/wiki/Decimal_degrees#Precision">Dezimalstellen Längengenauigkeit</a> ermöglichen eine Annäherung von 11,132 Metern am Äquator.
</dd>
</dl></td>
</tr>
<tr>
<td><p>D.D8</p></td>
<td><p>Gradnotation, 8 Nachkommastellen (<a href="https://wikipedia.org/wiki/Decimal_degrees#Precision">Genauigkeit</a> entsprechend ISO-DMS)</p>
<dl>
<dt></dt>
<dd>
z.B. +12.01543265 , -124.36473268
</dd>
</dl></td>
</tr>
<tr>
<td><p>Grad</p></td>
<td><p>Grad, Minuten, Sekunden Notation</p>
<dl>
<dt></dt>
<dd>
z.B. 50°52'21.92"N , 124°52'21.92"O (° Symbol hat UTF-8 Code c2b00a)
</dd>
<dd>
oder N50º52'21.92" , O124º52'21.92" (º Symbol hat UTF-8 Code c2ba0a)
</dd>
<dd>
Das Zeichen für Sekunden kann entweder ein doppeltes Anführungszeichen sein "
</dd>
<dd>
oder zwei einfache Anführungszeichen '
</dd>
<dd>
Die Buchstaben N/S/W/O können vor oder nach den Ziffern stehen. Für Ost geht auch E(ast).
</dd>
</dl></td>
</tr>
<tr>
<td><p>Grad-</p></td>
<td><p>Grad, Minuten, Sekunden Notation mit :</p>
<dl>
<dt></dt>
<dd>
z.B. -50:52:21.92 , 124:52:21.92
</dd>
</dl></td>
</tr>
<tr>
<td><p>ISO-D</p></td>
<td><p>ISO 6709 Gradnotation</p>
<dl>
<dt></dt>
<dd>
z.B. ±GG.GGGG±GGG.GGGG
</dd>
</dl></td>
</tr>
<tr>
<td><p>ISO-DM</p></td>
<td><p>ISO 6709 Grad, Minutennotation</p>
<dl>
<dt></dt>
<dd>
z.B. ±GGMM.MMM±GGGMM.MMM
</dd>
</dl></td>
</tr>
<tr>
<td><p>ISO-DMS</p></td>
<td><p>ISO 6709 Grad, Minuten, Sekunden Notation</p>
<dl>
<dt></dt>
<dd>
z.B. ±GGMMSS.SS±GGGMMSS.SS
</dd>
</dl></td>
</tr>
</tbody>
</table>

{{-}}

Siehe: [Koordinatenformat](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Einstellungen#Anzeigeoptionen): in den Einstellungen Anzeige, da diese Option die Anzeige der Koordinaten steuert.

## Informationen zu Quellen bearbeiten

In einer der Kategorienansichten für kannst du eine neue Quelle auswählen oder erstellen. Wenn du die Schaltflächen oder ausgewählt hast, wird das Dialogfeld Editor angezeigt.

### Neue Quelle Dialog

![[_media/NewSource-editor-dialog-example-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Neue Quelle - Editordialog - Beispiel]]

Für das Dialogfeld kannst du in den allgemeinen Informationen im oberen Bereich des Fensters grundlegende Informationen zur Quelle definieren: , , und . Du kannst diese Informationen direkt in die angrenzenden Felder eingeben.

- Titel der Quelle.

- Autoren der Quelle.

- Veröffentlichungsinformationen wie Stadt und Erscheinungsjahr, Name des Herausgebers, ...

- Gib einen kurzen Titel zum Sortieren, Ablegen und Abrufen von Quelldatensätzen an.

  - Schlosssymbol umschalten.

- Eine eindeutige Datensatzkennung zur Identifizierung der Quelle. Wenn leer wird sie von Gramps erzeugt.

- - 

{{-}}

### Neue Quelle Registerkarten

Die Registerkarten enthalten die folgenden Informationskategorien von Quelldaten:

#### Notizen

  
Der Reiter liefert einen Ort zum speichern von Notizen oder Kommentaren zu der Quelle. Um eine Notiz hinzuzufügen oder eine bestehende Notiz zu bearbeiten bearbeite einfach den Text im Texteingabefeld. Nur Hauptobjekte können in dem Reiter gezeigt werden: Personen, Familie, Ereignis, Ort oder Medienobjekt. Auf sekundäre Objekte wie Namen und Attribute kann nur über das Hauptobjekt zu dem sie gehören zugegriffen werden.

#### Galerie

  
Der Reiter ermöglicht dir das Speichern und Anzeigen von Fotos und anderen Medienobjekten, die mit der Quelle in Verbindung stehen (z.B. ein Bild der Geburtsurkunde). Der zentrale Bereich des Fensters listet all diese Medienobjekte und gibt dir eine Miniaturvorschau von Bilddateien. Andere Objekte wie Audiodateien, Videodateien usw. werden durch Gramps typische Symbole dargestellt. Die Schaltflächen , , , und ermöglichen dir das hinzufügen neuer Bilder, das Hinzufügen einer Referenz zu einem bestehenden Bild und das Entfernen von Medienverknüpfungen zu der Quelle. Beachte das die und Schaltflächen nur verfügbar sind wenn ein Medienobjekt aus der Liste gewählt ist.

#### Attribute

  
Der Reiter zeigt dir "Schlüssel/Wert" Paare die mit der Quelle in Verbindung stehen können. Sie sind ähnlich den "Attributen", die für andere Arten von Gramps Datensätzen verwendet werden. Der Unterschied zwischen den Schlüssel/Wert Paaren und Attributen ist, das Attribute Quellen und Notiz Referenzen enthalten können, Schlüssel/Wert Paare aber nicht.

<!-- -->

  
Der zentrale Bereich des Fensters listet alle vorhandenen Schlüssel/Wert Paare. Die Schaltflächen und ermöglichen dir das Hinzufügen und Entfernen von Paaren. Zum ändern des Text eines Schlüssel oder Werts wähle erst den gewünschten Eintrag klicke dann in die Schlüssel oder Wert Zelle und gebe deinen Text ein. Wenn du fertig bist, klicke außerhalb der Zelle um den Bearbeitungsmodus zu verlassen.

#### Aufbewahrungsorte

![[_media/NewSource-Repositories-tab-example-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Aufbewahrungsorte" Reiter vom "Neue Quelle" - Dialog - Beispiel]]

  
Der Reiter zeigt die Verknüpfungen zu den Aufbewahrungsorten in denen die Quellen aufbewahrt werden. Die Liste kann nach jeder ihrer Spaltenüberschriften sortiert werden: , , und . Doppel klicken eines Eintrags ermöglicht dir das Ansehen und Bearbeiten des Eintrags in dem .. Du kannst auch die Verknüpfungen bearbeiten. Die Schaltflächen an der Seite des Reiters ermöglichen dir das Hinzufügen eines neuen Aufbewahrungsort, Verknüpfen mit oder Teilhaben an einem bestehenden Aufbewahrungsort, bearbeiten der Beziehung zu einem Aufbewahrungsort oder das Entfernen der Verknüpfung.

##### Aufbewahrungsortreferenzeditor

![[_media/Repository-Reference-Editor-example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Aufbewahrungsortreferenzeditor - Dialog - Beispiel]] Der **Aufbewahrungsortreferenzeditor** wird durch einen Doppelklick auf einen Datensatz auf der Registerkarte im [Quelleneditor](#Informationen_zu_Quellen_bearbeiten)-Dialog geöffnet.

Er bietet die Möglichkeit, die Art und die Signatur für eine Quelle in einem bestimmten Aufbewahrungsort zu protokollieren. Da eine Quelle in mehreren Aufbewahrungsorten vorhanden sein kann. (Ich könnte eine Fotokopie in meiner persönlichen Bibliothek haben. Eine Kopie des Originalbuchs könnte sich in den Beständen des ACPL Genealogy Center in Ft. Wayne, Indiana befinden. Der Mikrofilm könnte sich in der FamilySearch Library in Salt Lake City, Utah, befinden. Beide können über verschiedene Signaturnummern gefunden werden).

###### Referenzinformationen

Der Abschnitt Referenzinformationen besteht aus den Registerkarten und . Die Registerkarte Allgemein enthält ein Texteingabefeld für die und ein [Dropdown-Liste Kombinationsfeld](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Hauptfenster#Kombinationsfelder) zur Auswahl der .

Zur Auswahl stehen folgende Medienarten: Audio, **Buch** *(Standard)*, Karte, Elektronisch, Fiche, Film, Magazin, Manuskript, Karte, Zeitung, Foto, Grabstein, Unbekannt, Video, [eigene Typen](wiki:De:Gramps_Glossar#custom).

###### Gemeinsame Informationen

Der Abschnitt bietet alle Optionen der [Aufbewahrungsorteditordialoge](#Neuer_Aufbewahrungsort_Dialog) mit den Registerkarten Allgemein, Adressen, Internet, Notizen und Referenzen. {{-}}

##### Aufbewahrungsort wählen Auswahl

![[_media/SelectRepository-SelectorDialog-example-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Aufbewahrungsort wählen - Auswahldialog - Beispiel]]

Im Dialogfeld Auswahl kannst du eine Verknüpfung zu bereits vorhandenen Aufbewahrungsorten herstellen. Nach der Auswahl wird dieser im <span id="Aufbewahrungsortreferenzeditor"> geöffnet.</span>

Du kannst die Schaltfläche verwenden, um die Liste basierend auf einer der Optionen aus der Dropdown-Liste zu filtern:

- **Titel enthält** (Standardeinstellung)
- *Titel enthält nicht*
- *ID enthält*
- *ID enthält nicht*
- *Letzte Änderung enthält*
- *Letzte Änderung enthält nicht*

{{-}}

#### Referenzen

  
Der Reiter zeigt alle Datensätze, die sich auf diese Quelle beziehen. Die Liste kann nach jeder ihrer Spaltenüberschriften sortiert werden: , , oder . Doppel klicken eines Eintrags ermöglicht dir das Ansehen und Bearbeiten des Eintrags.

{{-}}

## Quellenfundstellen bearbeiten

Fundstellen verbinden eine Quelle mit einem anderen Objekt und ermöglichen dir die Quelle mit zusätzlichen Informationen zu versehen. Fundstellen können an eine große Anzahl von Objekten angehängt werden,

- [Personen und diverse Informationen über Personen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Daten_eingeben_und_bearbeiten:_Ausführlich_-_Teil_1#Informationen_.C3.BCber_Personen_bearbeiten) (wie ihr Name, Adresse usw.),
- [Beziehungen (Familien) und diverse Informationen über Beziehungen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Daten_eingeben_und_bearbeiten:_Ausführlich_-_Teil_1#Informationen_.C3.BCber_Beziehungen_bearbeiten),
- [Ereignisse und diverse Informationen über Ereignisse](#Informationen_.C3.BCber_Ereignisse_bearbeiten),
- [Medienobjekte und Attribute von Medienobjekten](#Informationen_.C3.BCber_Medienobjekte_bearbeiten),
- [Orte und diverse Informationen über Orte](#Informationen_.C3.BCber_Orte_bearbeiten),
- [Adressen von Aufbewahrungsorten](#Informationen_.C3.BCber_Aufbewahrungsorte_bearbeiten).

Für jedes Objekt wird eine Gruppe von üblichen Schaltflächen bereitgestellt:

-  (Erstellen und hinzufügen einer neuen Fundstelle und Quelle). Dies öffnet einen leeren Fundstellendialog.

- (Fügt eine bestehende Fundstelle oder Quelle hinzu). Dies öffnet den Fundstellen oder Quellenauswahldialog.

- (Die gewählte Fundstelle bearbeiten). Dies öffnet den mit den Fundstellen und Quelleninformationen vor ausgefüllten Fundstellendialog.

-  (Die bestehende Fundstelle entfernen). Dies entfernt die Fundstelle von dem Objekt. Es löscht nicht die Fundstelle selbst, sie kann dann mit einem anderen Objekt verbunden werden.

Beachte, das die Schaltflächen und nur verfügbar sind, wenn eine Fundstelle ausgewählt wurde.

{{-}}

### Quelle oder Fundstelle wählen Auswahl

![[_media/SelectSourceOrCitation-SelectorDialog-example-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Quelle oder Fundstelle wählen - Auswahl Dialog - Beispiel]]

Wenn du eine bestehende Quelle oder Fundstelle , erscheint das [Dialogfeld](wiki:De:Gramps_Glossar#selector) .

Dies ermöglicht entweder eine bestehende Quelle oder Fundstelle (zusammen mit der zugehörigen Quelle) auszuwählen. Klick auf das Dreieck neben einer Quelle um die mit dieser Quelle verbundenen Zitate zusehen. Zum Beispiel, wenn eine deiner Quellen ein Buch ist, dann verweisen die Fundstellen normalerweise auf eine Seite (oder Seiten) in diesem Buch. Wenn du bereits eine Fundstelle hast, die auf die bestimmte Seite aus dem Buch verweist, kannst du diese Fundstelle auswählen welche dann mitbenutzt wird. Andererseits wenn das Objekt auf eine neu Seite verweisen muss, dann wähle die Quelle und gib in dem nachfolgenden Dialog die neue Seite ein.

Du kannst die Schaltfläche verwenden, um die Liste basierend auf einer der Optionen aus der Dropdown-Liste zu filtern:

- **Quelle: Titel oder Fundstelle: Band/Seite enthält** (Standardeinstellung)
- *Quelle: Titel oder Fundstelle: Band/Seite enthält nicht*
- *ID enthält*
- *ID enthält nicht*
- *Letzte Änderung enthält*
- *Letzte Änderung enthält nicht*

{{-}}

### Neue Fundstelle Dialog

![[_media/NewCitation-editor-dialog-example-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Neue Fundstelle - Editor Dialog - Beispiel]]

Sobald du eine Fundstelle oder Quelle gewählt hast oder auf eine der oder Schaltflächen geklickt hast, erscheint der folgende Dialog:

Der Dialog enthält zwei Bereiche und . {{-}}

#### Fundstelle Information

Der Bereich zeigt die Details zu der aktuellen Referenz zu dieser Quelle: , , und . Du kannst die Zuverlässigkeit in dem Aufklappmenü wählen. Die restlichen Details können in die entsprechenden Texteingabefelder eingegeben werden.

-   
  Datum das mit dieser Quellenreferenz verbunden ist. Typischerweise verwendet, um das Datum zu speichern, an dem die Daten in das original Quelldokument eingetragen wurden (nicht das Datum an dem das Ereignis stattgefunden hat).

  - ![[_media/22x22-gramps-date.png]] Schaltfläche öffnet das Dialogfeld .

-   
  Konkrete Stelle an der die referenzierte Information zu finden ist. Für eine veröffentlichte Arbeit kann dies den Band eines mehr bändigen Werks und die Seitennummer(n) enthalten. Für eine periodisch erscheinende Quelle kann es den Band, die Ausgabe und die Seitennummern enthalten. Für eine Zeitung kann es die Spalten und Seitennummer(n) enthalten. Für eine unveröffentlichte Quelle kann dies sein eine Blattnummer, Seitennummer, Bildnummer, usw. Ein Zensusdatensatz kann eine Zeilen, Wohnungsnummer oder Familiennummern zusätzlich zur Seitennummer enthalten.

-   
  Die Stufe gibt die quantitative Bewertung der Glaubwürdigkeit einer Information durch den Einsender auf der Grundlage der entsprechenden Belege wieder. Es ist nicht beabsichtigt, den Empfänger davon abzuhalten, die Beweise selbst zu bewerten. (Wird in der der Fundstellen als Spalte angezeigt)

  - *sehr niedrig* = unsicherer Beleg oder geschätzte Daten.
  - *niedrig* = Fragliche Glaubwürdigkeit des Beleg (Interviews, Zensus, mündliche Genealogie oder mögliche Einseitigkeit z.B. eine Autobiografie).
  - *Normal* - (Vorgabe) Der Nachweis ist möglicherweise nicht relevant oder wurde nicht bewertet. Noch nicht validiert
  - *hoch* = Sekundärer Beleg, Daten wurden offiziell irgendwann nach dem Ereignis aufgezeichnet.
  - *sehr hoch* = Direkter und primärer Beleg wurde verwendet oder die Dominanz des Beleg.

- 

- 

Ein Warnungsymbol  wird angezeigt, wenn die Fundstelle mehrfach verwendet wird.  

{{-}}

##### Quelle wählen Auswahl

![[_media/SelectSource-selector-dialog-example-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Quelle wählen - Auswahl Dialog - Beispiel]]

Im Dialogfeld kannst du eine Verknüpfung zu einer bereits vorhandenen Quelle herstellen.

Du kannst die Schaltfläche verwenden, um die Liste basierend auf einer der Optionen aus der Dropdown-Liste zu filtern:

- **Titel enthält** (Standardeinstellung)
- *Titel enthält nicht*
- *Autor enthält*
- *Autor enthält nicht*
- *ID enthält*
- *ID enthält nicht*
- *Letzte Änderung enthält*
- *Letzte Änderung enthält nicht*

{{-}}

##### Fundstelle Information Bereich Registerkarten

Die Reiter liefern die folgenden Informationskategorien der Fundstellendaten:

###### Notizen

Der Reiter bietet einen Platz um Notizen und Bemerkungen zu der Fundstelle zu speichern. Der zentrale Bereich des Fensters listet alle Notizen und gibt dir eine Vorschau auf den Anfang der Notizen. Die Schaltflächen , , , , und ermöglichen dir eine neu Notiz hinzuzufügen, eine gewählte Notiz gemeinsam zu verwenden, die gewählte Notiz zu bearbeiten, die gewählte Notiz zu entfernen und die gewählte Notiz in der Liste der Notizen hoch oder runter zu bewegen. Beachte das die , , , und Schaltflächen nur verfügbar sind, wenn ein Notizobjekt aus der Liste gewählt ist. Entfernen einer Notiz entfernt diese nur von der Fundstelle, es löscht nicht die Notiz selbst. Bitte siehe auch in [Details über das Bearbeiten von Notizen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Daten_eingeben_und_bearbeiten:_Ausführlich_-_Teil_2#Informationen_über_Notizen_bearbeiten).

###### Galerie

Der Reiter ermöglicht dir das Speichern und Anzeigen von Fotos und anderen Medienobjekten die mit der Fundstelle in Verbindung stehen (zum Beispiel ein Foto von der Seite eines Buches oder einer Seite eines Zensus). Der zentrale Bereich des Fensters listet all diese Objekte und gibt dir eine Miniaturvorschau von Bilddateien. Andere Objekte wie Audiodateien, Filmdateien usw. werden durch ein typisches Grampssymbol dargestellt. Die Schaltflächen , , und ermöglichen dir ein neues Medienobjekt hinzuzufügen, eine Referenz zu einem bestehenden Medienobjekt zu erstellen, ein bestehendes Medienobjekt zu ändern und die Verknüpfung eines Medienobjekts zu dieser Fundstelle zu entfernen. Beachte das die und Schaltflächen nur verfügbar sind, wenn ein Medienobjekt aus der Liste gewählt ist. Bitte siehe auch [Details über das Bearbeiten von Medienobjekten](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Daten_eingeben_und_bearbeiten:_Ausführlich_-_Teil_2#Medienobjektreferenzen_bearbeiten).

###### Attribute

Der Reiter zeigt "Schlüssel/Wert" Paare die mit der Fundstelle in Verbindung stehen können. Diese sind ähnlich den "Attributen" die für andere Arten von Gramps Datensätzen verwendet werden. Der Unterschied zwischen diesen Schlüssel/Wert Paaren und Attributen ist, das Attribute Quellenfundstellen und Notizen haben können und Schlüssel/Wert Daten nicht.

Der zentrale Bereich des Fensters listet alle vorhandenen Schlüssel/Wert Paare. Die Schaltflächen und ermöglichen dir Paare hinzuzufügen und zu entfernen. Um den Text des Schlüssel oder des Werts zu ändern, wähle zuerst den gewünschten Eintrag. Dann drücke die Schaltfläche um den Schlüssel zu wählen oder klicke in die Schlüssel oder Wert Zelle des Eintrags und gib deinen Text ein. Wenn du fertig bist, klicke außerhalb der Zelle um den Bearbeiten Modus zu beenden.

###### Referenzen

Der Reiter zeigt alle Datensätze, die sich auf diese Referenz beziehen. Die Liste kann nach jeder ihrer Spaltenüberschriften sortiert werden: , , oder . Doppel klicken eines Eintrags ermöglicht dir das Ansehen und Bearbeiten des entsprechenden Eintrags.

{{-}}

## Informationen über Aufbewahrungsorte bearbeiten

Wenn du eine Quelle ausgewählt hast, oder wenn du die Schaltflächen oder gewählt hast, erscheint das Dialogfeld Dialog.

### Neuer Aufbewahrungsort Dialog

![[_media/NewRepository-editor-dialog-example-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Neuer Aufbewahrungsort - Editor Dialog - Beispiel]]

Die folgenden Felder werden angezeigt:

- Der des Aufbewahrungsort (wo die Quelle aufbewahrt wird).

- des Aufbewahrungsort können physische oder virtuelle Strukturen sein, in denen genealogische und familiengeschichtliche Quellen gespeichert sind:

  - *Album*
  - *Archive*
  - **Bibliothek** (Vorgabe)
  - *Buchladen*
  - *Friedhof*
  - *Internetseite*
  - *Kirche*
  - *Safe*
  - *Sammlung*
  - *Unbekannt*

-   
  ein eindeutiger Wert zum identifizieren des Aufbewahrungsort. Wenn er leer ist wird er von Gramps erstellt.

- Schlosssymbol umschalten..

- - 

{{-}}

### Neuer Aufbewahrungsort Registerkarten

Die Reiter repräsentieren die folgenden Kategorien der Aufbewahrungsort Daten:

- 

- 

- 

- 

#### Adressen

Der Reiter ermöglicht dir das Ansehen und Speichern der verschiedenen Adressen des Aufbewahrungsort.

Der untere Bereich des Fensters listet alle Adressen, die in der Datenbank gespeichert sind. Der obere Bereich zeigt die Details der aktuell aus der Liste ausgewählten Adresse (wenn vorhanden). Die Schaltflächen , und ermöglichen dir das Hinzufügen, ändern und entfernen einer mit dem Aufbewahrungsort verknüpften Adresse. Beachte das die und Schaltflächen nur verfügbar sind wenn eine Adresse aus der Liste gewählt ist.

#### Internet

Der Reiter enthält für den Aufbewahrungsort relevante Internetadressen. (Diese Registerkarte verhält sich genauso wie die Registerkarte [Internet](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Daten_eingeben_und_bearbeiten:_Ausführlich_-_Teil_1#Internet) für den Personen-Editor und auch der \[\[De:Gramps_6.0_Wiki_Handbuch\_-\_Daten_eingeben_und_bearbeiten:\_Ausführlich\_-\_Teil_1#Internetadresseneditor\|Internet-Adress-Editor\] ist derselbe).

Der untere Teil des Fensters listet all diese Adressen aus der Datenbank. Der obere Teil zeigt die Details der aktuell gewählten Adresse (wenn vorhanden). Die Schaltflächen , und ermöglichen dir das Hinzufügen, Bearbeiten und Entfernen von Internetadressen. Die Schaltfläche (dargestellt durch ein Symbol mit einem grünen Pfeil und einem gelben Kreis) öffnet deinen Browser und bringt dich zu der Webseite die zu der markierten Internetadresse gehört. Beachte das die , und Schaltflächen nur verfügbar sind wenn eine Adresse aus der Liste gewählt ist.

#### Notizen

  
Der Reiter liefert einen Ort zum speichern von Notizen oder Kommentaren zu dem Aufbewahrungsort. Zum hinzufügen einer Notiz oder ändern einer bestehenden Notiz einfach den Text im Texteingabefeld bearbeiten.

#### Referenzen

  
Der Reiter zeigt alle Datensätze, die sich auf diesen Aufbewahrungsort beziehen. Die Liste kann nach jeder ihrer Spaltenüberschriften sortiert werden: , , oder . Doppel klicken eines Eintrags ermöglicht dir das Ansehen und Bearbeiten des entsprechenden Eintrags.

{{-}}

## Informationen über Notizen bearbeiten

Siehe auch:

- [Notizenkategorie](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Kategorien#Notizenkategorie)

### Notiz Editor Dialog

![[_media/NewNote-editor-dialog-example-with-context-menu-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Neue Notiz - Editor Dialog - Beispiel mit Kontextmenü]]

Beim erstellen einer neuen Notiz oder beim bearbeiten einer existierenden Notiz, wird der geöffnet. Dort gibt es zwei Reiter den **und den** ''' Reiter.

#### Notizenreiter

Die Registerkarte ist der Bereich, in dem Text hinzugefügt wird. Der Text kann mit vielen Standard-Textbearbeitungswerkzeugen formatiert werden.

##### Notizenwerkzeugleiste

:\* Eine Werkzeugleiste zur Anwendung von Stilen (oder Schriftdekorationen) auf den Text in deinen Notizen. Du kannst eine der Schaltflächen auswählen und anwenden oder die Werte nach Belieben einstellen und mit der Eingabe beginnen.

::\* : Schrägstellen von Text zur Hervorhebung, wie in den meisten Texteditoren üblich

::\* : Dunkelt Text zur Hervorhebung ab, wie in den meisten Texteditoren üblich

::\* : Zeichnet eine Linie unter den Text, wie in den meisten Texteditoren üblich

::\* : zieht eine Linie durch, die üblicherweise verwendet wird, um zu löschenden Text anzuzeigen

::\* : Hebt den Text leicht an, wird häufig für Fußnoten verwendet (z. B. Wikipedia <sup>2</sup>)

::\* : Senkt den Text leicht ab, wird häufig in Formeln verwendet (z. B., H<sub>2</sub>O)

::\* :Dropdown-Liste zur Auswahl von Schriftarten: Eine grundlegende Auswahl für Schriftarten, in der alle auf Ihrem Betriebssystem installierten Schriftarten angezeigt werden.

::\* : die Größe der Schrift die du eingibst.

::\* : Macht die letzte Aktion rückgängig.

::\* : Wendet die letzte "Rückgängig"-Aktion erneut an.

::\* Wähle die Farbe deiner Schrift.

::\* Fügt dem von dir eingegebenen Text eine Hintergrundfarbe hinzu.

::\* Öffnet den , mit dem du eine interne Verknüpfung zu einem Element in Gramps erstellen kannst, z. B. zu einer Person, einer Familie, einem Ereignis, einer Notiz usw. Es können auch externe URL-Links erstellt werden.

::\* Verwandelt den markierten Text in reinen Text zurück. Entfernt alle erstellten Verknüpfungen.

##### Textansicht-Kontextmenü

:\* Rechtsklick auf die Textansicht, um das Kontextmenü anzuzeigen:

<hr>

::\* – ausgewählt oder alternativ kannst du drücken und mit der rechten Maustaste klicken – Wird nur angezeigt, wenn ein Link in der Textansicht ausgewählt ist

::\* – Du kannst den Inhalt an anderer Stelle einfügen – Wird nur angezeigt, wenn ein Link in der Textansicht ausgewählt ist

::\* – Öffnet den , in dem du den ausgewählten Link erstellen und bearbeiten kannst. – Wird nur angezeigt, wenn ein Link in der Textansicht ausgewählt ist

::\* – Der wichtigste Eintrag in diesem Kontextmenü ist die Rechtschreibauswahl. Dir wird eine Auswahl der auf deinem System installierten Sprachen mit aktivierter [Rechtschreibprüfung](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Einstellungen#Umgebungseinstellungen) angeboten. Eine Rechtschreibprüfung ist für Englisch und deine installierte Landessprache verfügbar (Hinweis: Aktiviere im Abschnitt die Option für globales Englisch als Standard oder die Sprache, in der Gramps ausgeführt wird, und das Notiz-Kontextmenü ist pro Notiz in der ausgewählten Sprache deiner Wahl).

:::\*

:::\* – (Standard)

::\* – den ausgewählten Text.

::\* – den ausgewählten Text.

::\* – den zuvor ausgeschnittenen oder kopierten Text.

::\*

#### Referenzen Reiter

Die Registerkarte zeigt alle Objekte an, die auf eine bestimmte Notiz verweisen. Die Liste kann nach jeder deiner Spaltenüberschriften sortiert werden: `Art`, `ID` oder `Name`. Durch Doppelklicken auf einen Eintrag oder durch Auswählen eines Eintrags und Klicken auf die Schaltfläche kannst du den entsprechenden Datensatz anzeigen und bearbeiten.

### Verknüpfungeditor

![[_media/Note-LinkEditor-dialog-default-example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Notiz „Link-Editor“ – Dialogfeld – standardmäßig auf aktive Person eingestellt – Beispiel]]

Um einen Notizlink zu erstellen, **muss zunächst ein Block mit Notiztext markiert werden**, damit der Link-Editor aktiv wird. Wenn du dann auf das Symbol in der [Notizenwerkzeugleiste](#Notizenwerkzeugleiste) klickst, wird der angezeigt. Es gibt keine visuelle Anzeige, wenn das Symbol in der Notiz-Symbolleiste inaktiv ist.

Die in der Notiz erstellten Links werden blau und unterstrichen, wenn du mit der Maus über den verlinkten Text fährst. Während du in der Gramps-Notiz arbeitest, kannst du entweder  + die linke Maustaste drücken oder im [Kontextmenü der Textansicht](#Textansicht-Kontextmen.C3.BC) mit der rechten Maustaste auswählen, wodurch entweder das Bearbeitungsfenster für das ausgewählte Objekt oder der HTML-URL-Link in deinem Standard-Internetbrowser geöffnet wird.

Die wahre Stärke von Links zeigt sich, wenn ein Bericht mit [Erzählende Website](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte#Erz.C3.A4hlende_Website) oder [dynamischer Website](wiki:Addon:DynamicWeb_report) erstellt wird. Die erstellten Links werden zu echten Navigationslinks zu anderen Seiten innerhalb des Webberichts.

#### Dialogfeld Notizlinkeditor

![[_media/Note-LinkEditor-dialog-InternetAddress-example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Dialogfeld „Notizlinkeditor” – Anzeige des Linktyps: Internetadresse – Beispiel]]

Das Dialogfeld zeigt standardmäßig die aktive Person an und bei Auswahl für jedes der anderen Objekte das entsprechende aktive Objekt. Du kannst auch den Linktyp „Internetadresse” auswählen.

Es werden die folgenden Optionen angezeigt:

- Gibt die Link-Art für eines der neun aktiven Gramps-Elemente/Objekte an, standardmäßig die aktive *Person* oder eine von dir manuell eingegebene Internetadresse.

  - *Internetadresse* – (https://de.wikipedia.org/wiki/Uniform_Resource_Locator <abbr title="Uniform Resource Locator, also known as a web address">URL</abbr>\]) – Wenn diese Option ausgewählt ist, wird das Feld für die Dateneingabe verfügbar.
  - *[Ereignis](wiki:Events)*
  - *Familie*
  - *Medien*
  - *Notiz*
  - *Person* (Standard)
  - *[Ort](wiki:De:Orte_in_Gramps)*
  - *Aufbewahrungsort*
  - *[Quelle](wiki:De:Quellen)*
  - *[Fundstelle](wiki:Citations)*
    -  Schaltfläche: Öffnet den entsprechenden [Auswahldialog](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Einstellungen#Auswahldialoge) für vorhandene Elemente in der im Link-Typ angegebenen Kategorie. **Gilt nicht für die Auswahl Internetadresse**.

    - Schaltfläche: Öffnet ein Fenster zum Erstellen eines neuen Elements des angegebenen Gramps-Elements. Nach erfolgreicher Erstellung eines neuen Elements werden das Feld „Gramps-Element“ und das Feld „Internetadresse“ automatisch mit den entsprechenden Daten ausgefüllt.

- Zeigt das ausgewählte Element an, z. B.: Wenn „Person” ausgewählt ist, wird der Name der aktiven Person angezeigt (siehe Screenshot). Nicht anwendbar für die Auswahl von Internetadressen.

  - Dieses Feld wird automatisch durch die Auswahl der Schaltfläche // generiert.

- Schaltfläche: Öffnet den Editor-Dialog für das angegebene Gramps-Element. Das ausgewählte Element füllt automatisch das Feld Gramps-Element und das Feld Internetadresse mit den entsprechenden Daten.

- - Für die = Gramps-Typ wird dieses Feld automatisch ausgefüllt, aber der Inhalt wird ausgegraut.
  - Für die = *Internetadresse* (Standard: [`https://`](https://) ) löschen Sie die von Gramps vorgegebene Standardeinstellung und geben Sie die vollständige Internetadresse entweder manuell oder per Kopieren und Einfügen ein.

![[_media/Note-showing-tooltip-for-link-example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Notizen-Editor – Verknüpfter Text mit Tooltip – Beispiel]]

Siehe auch:

- [Internetadresseneditor](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Daten_eingeben_und_bearbeiten:_Ausführlich_-_Teil_1#Internetadresseneditor)
- [Notiz Verknüpfung Bericht](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte_-_Teil_6#Notiz_Verkn.C3.BCpfung-Bericht)

{{-}}

### Notizhervorhebungen und Vorformatierungen in Berichten

Hervorhebungen wie **fett**, Farbe, <u>unterstrichen</u>, ... können zu Notizen hinzugefügt werden. Eine Notiz kann vorformatiert werden oder nicht. Es hängt von der Ausgabeart ab, wie diese Hervorhebungen erscheinen. Hier eine Übersicht was du erwarten kannst.

- **PDF** und **direkter Druck** (zum Drucker oder in eine Datei) volle Unterstützung der Hervorhebungen und der Vorformatierung.
- **ASCII**-Druck entfernt alle Hervorhebungen von der Notiz aus offensichtlichem Grund.

<!-- -->

- **LaTeX** unterstützt die vorformatierte Einstellung und teilweise die Hervorhebung von Schriftarten und die Größenmarkierung;  
  die Ausgabe unterstützt keine Markierung von Schriftfamilien oder Farben.
- **Erzählendes Web**. Viele Menschen verwenden die Erzählenden Web Berichte als einfache Möglichkeit um mit ihren Daten zu arbeiten. Dieser Bericht versucht Hervorhebungen in den Notizen zu beachten. Dies ist eine interpretierte Übertragung - sie ist nicht Eins zu Eins.
- **ODF**-Ausgabe unterstützt keine Hervorhebungen. Dies wird in der Zukunft hinzugefügt.
- **RTF**-Ausgabe unterstützt keine Hervorhebungen.
- **HTML**-Ausgabe unterstützt keine Hervorhebungen.

{{-}}

[D](wiki:Category:De:Dokumentation)
