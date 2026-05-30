---
title: 'De:Gramps 6.0 Wiki Handbuch - Daten eingeben und bearbeiten: Kurz'
categories:
- De:Dokumentation
managed: false
source: wiki-scrape
wiki_revid: 130639
wiki_fetched_at: '2026-05-30T17:43:07Z'
lang: de
---

{{#vardefine:chapter\|8}} {{#vardefine:figure\|0}} Dieser Abschnitt ist dafür gedacht dir das Basiswissen, welches benötigt wird um damit zu beginnen genealogische Informationen in Gramps einzugeben, zu vermitteln. Er erklärt wie man Personen in die Datenbank eingibt und wie man deren familiäre Beziehungen angibt. (Eine genauere Erklärung erfolgt im nächsten Kapitel: [Daten eingeben und bearbeiten: Ausführlich](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Daten_eingeben_und_bearbeiten:_Ausführlich).)

Zuerst lass uns die Arten von Informationen bestimmen, die du in Gramps eingeben kannst. Diese beinhalten:

- Persönliche Informationen einer Einzelperson (Namen, Adressen, Geburts- und Sterbedaten, usw.)
- Informationen über die Beziehungen einer Einzelperson (Heiraten, Scheidungen, Eingetragene Lebenspartnerschaften, usw.)
- Informationen über Eltern und Kinder einer Person
- Quellen die deine Forschung dokumentieren

Nun lass uns einen kurzen Blick darauf werfen wie man diese verschiedenen Informationen eingeben kann.

## Eine Person hinzufügen oder bearbeiten

Das [Menü](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Navigation#Hinzuf.C3.BCgen) für jede [Kategorie](wiki:De:Gramps_Glossar#Kategorie)-[Ansicht](wiki:De:Gramps_Glossar#Ansicht) enthält die Option, eine [Person](wiki:De:Gramps_Glossar#Person) hinzuzufügen. Eine [Tastenkombination](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Tastenkürzel_Referenz#Allgemeine_K.C3.BCrzel) zum Hinzufügen einer Person wird ebenfalls in allen Kategorieansichten unterstützt.

Es gibt mehrere Möglichkeiten eine Person zur Datenbank hinzuzufügen. Viele haben einen impliziten Kontext, der einen Schritt beim Einfügen der Person in einen Baum erspart. (z.B. das Hinzufügen einer Person aus dem Familienkontext der Ansichten Beziehungen oder Diagramme fügt die neue Person automatisch in die Familie ein. Die Person muss nicht als separate Aktion erstellt und anschließend gesucht und in die Familie gezogen werden). Im weiteren Verlauf werden wir einige der verschiedenen Arbeitsabläufe erläutern. {{-}}

### Eine neue Person hinzufügen

![[_media/PeopleTreeView-GroupedPeople-example-with-context-menu-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Personenkategorie - Baumansicht - Gruppierte Personen]]

Der naheliegendste Weg, eine Person in Ihren Stammbaum einzufügen, ist das Hinzufügen aus der . Während du dich in der befindest (siehe Keine Seitenleiste kein Filter Abb.), klicke in der Werkzeugleiste.

{{-}} ![[_media/Edit-person-window-new-person-example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Person bearbeiten - Fenster - Neuer leerer Editor]]

Das Dialogfeld wird angezeigt und du kannst alle Daten eingeben, die du über diese Person kennst und dann auswählen, um die neue Person zu speichern.

{{-}}

### Eine vorhandene Person bearbeiten

![[_media/Edit-person-window-existing-person-example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Person bearbeiten - Fenster - Beispiel für eine vorhandene Person]]

Um Informationen über eine Person, die schon in der Datenbank existiert, zu bearbeiten, wähle die Person aus der und wähle die Schaltfläche in der Werkzeugleiste.

Personen können auch zur Datenbank in der , dem und anderen Orte wo es Sinn macht hinzugefügt werden.

{{-}}

## Eine Beziehung angeben

Es gibt zwei primäre Möglichkeiten Beziehungen zwischen Personen festzulegen:

\(1\) Von der Familie:

  
<li>

verwenden der Die wird üblicherweise verwendet, , um mehrere Beziehungen um eine einzelne Person herum aufzubauen.

</li>

<li>

verwenden des Dialogs der . Die wird üblicherweise verwendet, um alle Beziehungen in einer Familie auf einmal zu erstellen.

</li>

</ol>

\(2\) Nach Verbindung

  
<li>

Verwendung der Registerkarte des Dialogfelds . Durch Hinzufügen einer Person und Angabe der Art der Vereinigung (Paten, Mitarbeiter, Sargträger, Freund aus Kindertagen usw.) wird eine zwischenmenschliche Beziehung identifiziert.

</li>

<li>

Verwendung des Funktion des Dialogfelds . Durch Querverweise auf eine Person über einen Personenlink in einer Notiz wird diese verknüpfte Person der Person zugeordnet, an die die Notiz angehängt ist.

</li>

<li>

Personen, die eine Referenz teilen (Quellen, Notizen, an denselben Stellen kolokalisiert usw.), haben eine indirekte oder nahe Beziehung.

</li>

</ol>

{{-}}

### Eine Beziehung mit Hilfe der Beziehungenansicht angeben

![[_media/Relationships-category-view-default-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Beziehungenansicht]]

Um eine neue Beziehung zur [aktiven Person](wiki:De:Gramps_Glossar#aktive_Person) anzugeben, wechsle in die und du siehst diese Person als die "aktive Person". Neben der Beschriftung ist eine Schaltfläche (üblicherweise durch ein Zeichen repräsentiert).

{{-}}

![[_media/FamilyEditor-dialog-example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Eine Familie bearbeiten]]

Durch klicken der Schaltfläche öffnet sich der Dialog mit der aktiven Person entweder als Vater oder Mutter.

{{-}}

![[_media/SelectMother-selector-example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Mutter wählen - Dialog]]

Jetzt eine Frage?  
Ist die Person, die die Beziehung zur aktiven Person eingehen wird, bereits im Stammbaum vorhanden? Wenn ja, klicke auf die Schaltfläche für die andere Person. Du kannst dann die Liste der Personen im Stammbaum durchsuchen, um die gewünschte Person auszuwählen. Wenn nicht, klicke auf die Schaltfläche . Dadurch kannst du eine neue Person zum Stammbaum hinzufügen und die Beziehung dieser Person zur aktiven Person angeben.

Um eine bestehende Beziehung in der zu bearbeiten, klicke auf die Schaltfläche neben dem dazugehörigen Familieneintrag. Wenn sich mehr als eine Beziehung in der Liste befindet, kannst du den Partner oder Eltern durch klicken der zugehörigen Schaltfläche neben der Beziehung wählen.

{{-}}

### Eine Beziehung mit Hilfe der Familienlistenansicht angeben

Um eine neue Beziehung in der anzulegen, klicke auf die Schaltfläche in der Werkzeugleiste und ein leerer Dialog wird geöffnet. An dieser Stelle kannst du Personen zur Familie hinzufügen.

{{-}}

## Eltern festlegen

Du kannst die Eltern der aktiven Person in der festlegen (siehe  - Auswahl). Etwas Sorgfalt ist nötig, um das Erstellen zu verhindern. Wenn du die aktive Person zu einer bereits bestehenden Familie hinzufügen willst, solltest du auf die Schaltfläche klicken. Wenn die Familie mit den Eltern nicht bereits existiert, klicke auf die Schaltfläche.

{{-}} ![[_media/SelectFamily-SelectorDialog-example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Familie wählen - Auswahl Dialog Beispiel]]

Wenn du auf die Schaltfläche klickst, befindest du dich im Dialog. Dies ermöglicht dir eine bestehende Familie zu wählen und die aktive Person wird als Kind dieser Familie hinzugefügt.

Wenn du auf die Schaltfläche klickst, wird ein neuer Dialog mit der aktiven Person als Kind geöffnet. Du kannst die Eltern dieser Familie entweder durch hinzufügen von neuen Personen oder wählen existierender Personen festlegen.

{{-}} Die Eltern einer Person können auch in der festgelegt werden. Wenn die Familie bereits existiert, klicke auf die Schaltfläche in der Werkzeugleiste und füge die Person als Kind hinzu, wenn der Dialog erscheint. Wenn die Familie noch nicht existiert, klicke die Schaltfläche, um eine neue Familie zu erstellen und die passenden Eltern und Kinder hinzuzufügen.

{{-}}

## Kinder angeben

Das Hinzufügen von Kindern zu einer Beziehung erfolgt auf eine ähnliche Weise. In der oder , wähle eine bestehende Familie oder erstelle eine neue. Kinder können durch klicken der oder Schaltfläche rechts neben der Kinderliste hinzugefügt werden.

Klicken der Schaltfläche öffnet den Dialog und erlaubt das Hinzufügen einer neuen Person. Klicken auf die Schaltfläche erlaubt eine bestehende Person aus einer Liste zu wählen. Standardmäßig wird ein Kind mit dem Beziehungsart Geburt zu beiden Eltern hinzugefügt.

{{-}} ![[_media/ChildReferenceEditor-dialog-example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;Kinder Referenzeditor&quot;]]

Wenn du die Eltern/Kind Beziehung von der Vorgabe **Geburt** ändern willst, wähle im Dialog das Kind und klicke auf die Schaltfläche. Dies zeigt den Dialog.

{{-}} Wenn du die Reihenfolge der Kinder in der Familie ändern willst, verwende die Pfeile oder die [*Drag and Drop*](http://de.wikipedia.org/wiki/Drag_and_Drop) Funktion im Reiter. {{-}}

## Fotos und andere Medien Objekte hinzufügen

Verschiedene Arten von Medienobjekten (einschließlich Fotos, Dokumente, Audio- und Videodateien) können als [sekundäre Objekte](wiki:De:Gramps_Glossar#secondary_object) angefügt werden. Du kannst auch Bilder hinzufügen, die nicht auf eine einzelne Person oder ein Ereignis beschränkt sind. (Zum Beispiel Gruppenfotos von einem Familientreffen)

Gramps unterstützt verschiedene Arten von Medienobjekten, darunter Fotos, Dokumente, Audio- und Videodateien. Die gebräuchlichste Methode zum Hinzufügen von Medien ist die Registerkarte des Editors eines primären Objekts (z. B. Personen, Ereignisse, Familien, Orte, Fundstellen, Quellen oder Aufbewahrungsorte).

Bevor du ***neue*** Medienobjekte hinzufügst, solltest du den auf der Registerkarte in den Voreinstellungen überprüfen. Vergewissere dich dabei, dass du das Kontextmenü verwendet hast, damit in der [Dateiauswahl](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Einstellungen#Dateiauswahl) eine Schaltfläche für den „Basismedienpfad“ vorhanden ist.

Das Hinzufügen optionaler Informationen kann dir helfen, deine Medien zu kategorisieren, um sie später leichter finden zu können. Datumsangaben, Titel und [Etiketten](wiki:De:Gramps_Glossar#tag) können zu einem Medienobjekt hinzugefügt werden.

1.  Öffne den Objekteditor für das Primärobjekt
2.  Wähle die Registerkarte Galerie.
3.  Um ein neues Medienobjekt hinzuzufügen, klicke auf die Schaltfläche
    - Navigiere zu der Datei in der Dateiauswahl, entscheide, ob du die Option "In einen relativen Pfad konvertieren" verwenden möchtest
    - Klicke auf die Schaltfläche .
4.  Um ein vorhandenes Medienobjekt zu [Teilen](wiki:De:Gramps_Glossar#sharing), klicke auf die Schaltfläche
    - Wähle ein vorhandenes Medienobjekt im Dialogfeld [Medienobjekt auswählen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Daten_eingeben_und_bearbeiten:_Ausführlich_-_Teil_1#Medien_Objekt_w.C3.A4hlen_Auswahl) aus
    - Doppelklicke auf das Objekt oder klicke auf die Schaltfläche .
5.  Füge optionale Informationen hinzu
    - Wenn es sich bei dem Medienobjekt um ein Bild handelt, ziehe ein Rechteck in der Vorschau, um den Inhalt der Miniaturansicht zu verfeinern.
6.  Erweitere den Abschnitt und füge dann hilfreiche Details hinzu
    - benutzerfreundlicher **Titel**
    - **Datum**: das Medienobjekt wurde erstellt oder stellt das Medienobjekt dar
    - Etiketten auswählen

Wenn du ein paar Medienobjekte hinzufügst, kann es effizienter sein, die Ansicht zu verwenden und sie hinzuzufügen. Verwende dann die Schaltfläche , um je nach Bedarf eine Verknüpfung zu verschiedenen primären Objekten herzustellen.

### Verwenden der Zwischenablage

![[_media/Clipboard-dialog-example-context-menu-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Zwischenablage - Dialog - Kontextmenü anzeigen (Rechtsklick) Beispiel]] Wenn du mehr als ein paar Objekte hinzufügst, solltest du die Funktion in der [<strong>Medienverwaltung</strong>](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Werkzeuge#Medienverwaltung) aus dem Menü verwenden. der , um Letzte Änderung anzuzeigen, die neuen Objekte zu sortieren und sie in die [Zwischenablage](wiki:De:Gramps_Glossar#clipboard) zu kopieren.

Die Zwischenablage ermöglicht ein schnelles Drag'n'Drop in Objekteditor-Galerien. Beim Hinzufügen eines Medienobjekts zu mehreren Galerien kann es jedoch effizienter sein, die „Medienreferenz“ zu teilen, als eine separate Kopie der Medienobjektreferenz zu haben. Nachdem du ein Medienobjekt in einer Galerie abgelegt hast, kopiere das Medienobjekt in der Galerie zurück in die Zwischenablage. Dadurch wird eine „Medienreferenz“ für dieses Objekt erstellt. Lösche dann das ursprüngliche Medienobjekt aus der Zwischenablage.

Verwende einheitliche Namenskonventionen für deine Mediendateien und füge detaillierte Beschreibungen hinzu, um die Suche zu erleichtern. Denke daran, deine Mediendateien zusammen mit deiner Gramps-Datenbank regelmäßig zu sichern.

{{-}} ![[_media/PersonView-PeopleListView-example-with-context-menu-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Kategorie „Personen“ – „Personenansicht“ – „Personen“ (Liste) Ansicht mit Kontextmenü]]

Um ein Bild einer einzelnen Person zuzuordnen, in die wechseln (Siehe Abb. {{#var:chapter}}.{{#expr:{{#var:figure}}}}), eine Person wählen und auf die Schaltfläche in der Werkzeugleiste klicken. {{-}}

![[_media/Edit-person-window-existing-person-example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Person bearbeiten]]

Das öffnet den Dialog (See Fig. {{#var:chapter}}.{{#expr:{{#var:figure}}}}). Als nächstes wähle den Reiter und klicke die Schaltfläche um den Dialog zu öffnen. Gib einen Dateinamen ein oder blättere um das gewünschte Bild zu finden und vergib dann einen Titel für dieses Bild. Füge Bilder hinzu bis du fertig bist.

{{-}} ![[_media/Families-category-list-view-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Familienkategorieansicht]]

Um ein Bild zu einer Beziehung hinzuzufügen (z.B. eine Hochzeit), wechsle in die (Siehe Abb. {{#var:chapter}}.{{#expr:{{#var:figure}}}}) und klicke doppelt auf den Familieneintrag. Dies öffnet den Dialog. Wähle den Reiter und klicke die Schaltfläche um ein Bild hinzuzufügen. {{-}}

![[_media/SourcesCategory-Sources-ListView-example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Quellenansicht]]

Um Bilder zu einer Quelle oder einem Ort hinzuzufügen, wechseln Sie zunächst in die Ansicht (Quellen-Abbildung) oder Ansicht (Siehe Abb. {{#var:chapter}}.{{#expr:{{#var:figure}}}. Wähle die gewünschte Quelle oder den gewünschten Ort und doppelklicke darauf oder klicke auf das Symbol in der Symbolleiste. Wähle die Registerkarte und klicke auf die Schaltfläche , um ein Bild hinzuzufügen.

![[_media/PlacesCategory-PlaceView-list-example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Ortensicht]]

{{-}}

![[_media/MediaCategory-Media-ListView-example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Medienansicht]]

Zum Schluss um Bilder hinzuzufügen, die du zur Datenbank hinzufügen willst, die aber nicht auf eine einzelne Person, Beziehung, Quelle oder Ort begrenzt sind, wechsele in die (Siehe Abb. {{#var:chapter}}.{{#expr:{{#var:figure}}}}). Dann klicke auf das Symbol in der Werkzeugleiste um ein Bild hinzuzufügen. Wenn du schon Bilder zu irgendeiner Galerie hinzugefügt hast, findest du auch diese aufgelistet in der .

In jeder Galerie kannst du die Schaltfläche zum bearbeiten der Bildinformationen und die Schaltfläche zum entfernen der Bildreferenz von der Galerie verwenden.

## Ereignisse, Fundstellen/Quellen, Orte und Aufbewahrungsorte bearbeiten

Um Informationen von Ereignissen, Quellen, Orten und Aufbewahrungsorten aus der Datenbank zu bearbeiten, wechsele in die entsprechende Ansicht, wähle den Eintrag den du ansehen/bearbeiten möchtest und klicke auf die Schaltfläche in der Werkzeugleiste. Alternativ kannst du auf den Eintrag doppelklicken, um ihn zu bearbeiten.

![[_media/EventsCategory-EventsListView-example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Ereignisseansicht]]

Um ein Ereignis, eine Fundstelle/Quelle, einen Ort oder einen Aufbewahrungsort zur Datenbank hinzuzufügen, wechsele zur entsprechenden (Siehe Abb. {{#var:chapter}}.{{#expr:{{#var:figure}}}}), , , oder . Dann die Schaltfläche in der Werkzeugleiste anklicken, um das entsprechende Objekt hinzuzufügen. Gib die Informationen im entsprechenden (, , oder ) Dialog ein.

[D](wiki:Category:De:Dokumentation)
