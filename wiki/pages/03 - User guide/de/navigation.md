---
title: De:Gramps 6.0 Wiki Handbuch - Navigation
categories:
- De:Dokumentation
- Stub
managed: false
source: wiki-scrape
wiki_revid: 130845
wiki_fetched_at: '2026-05-30T18:06:38Z'
lang: de
---

{{#vardefine:chapter\|10}} {{#vardefine:figure\|0}} Solange ein [Stammbnaum](wiki:De:Genealogie-Glossar#Stammbaum) geöffnet ist, konzentriert sich Gramps auf eine Person gewöhnlich bezieht sich das auf eine [aktive Person](wiki:De:Gramps_Glossar#aktive_Person). Dies ermöglicht dir Daten diese Person betreffend anzuschauen und zu bearbeiten, seine oder ihre direkte Familie, usw. [Navigation in der Stammbaumdatenbank](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Navigation#Einstellen_der_aktiven_Person) (z.B. wechseln von einer Person zu einer anderen Person) ist tatsächlich nichts anderes als die aktive Person zu ändern.

Dieser Abschnitt beschreibt viele verschiedene Wege durch die Datenbank zu navigieren unter Verwendung beider, der komplexen und der praktischen Schnittstellen, die Gramps bietet. All diese Wege erreichen eventuell das Selbe, aber einige sind praktischer als andere, basierend darauf was du in Gramps in diesen Moment machst.

## Die Personenkategorie verwenden

Der intuitive Weg zur Auswahl einer aktiven Person, ist die Verwendung der ![[_media/gramps-person.png]] [Personenkategorie](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Kategorien#Personenkategorie). Wenn du dich in der Personenansicht befindest, wähle einfach den Namen der gewünschten Person durch klicken auf den Listeneintrag aus der Liste. Die Person die du gewählt hast wird die aktive Person. Die Statusleiste wird aktualisiert um die Änderung der aktiven Person widerzuspiegeln.

Siehe auch

- [Informationen über Personen bearbeiten](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Daten_eingeben_und_bearbeiten:_Ausführlich_-_Teil_1#Informationen_.C3.BCber_Personen_bearbeiten)

## Die Beziehungenkategorie verwenden

Wenn du dich in der ![[_media/gramps-relation.png]] [Beziehungenkategorie](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Kategorien#Beziehungenkategorie) befindest, kannst wie folgt ganz einfach zwischen den Mitgliedern der angezeigten Familie wechseln:

Klicke auf den <u>unterstrichenen</u> Namen der gewünschten Person und diese wird zur Hauptperson der Beziehungenansicht.

Der Name der zur Zeit aktiven Person ist nicht unterstrichen.

Zusätzlich dazu bietet Gramps eine reichhaltige Möglichkeit mit Hilfe der Tastatur zu navigieren. Die detaillierte über die Tastenkürzel findet sich in dem [Anhang B: Tastenkürzel Referenz](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Tastenkürzel_Referenz).

## Die Familienkategorie verwenden

Wenn du dich in der ![[_media/gramps-family.png]] [Familienkategorie](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Kategorien#Familienkategorie) befindest, kannst du ganz einfach zwischen den angezeigten Familien navigieren.

Die Familien können verwendet werden, um eine Reihe von Familien visuell auf mögliche Duplikate und fehlende Daten zu vergleichen. Durch Sortieren nach den verschiedenen Spalten können Partner mit ähnlichen Namen nahe beieinander platziert werden, sodass Ehepartner verglichen werden können. Du kannst nach Vornamen oder Spitznamen suchen, indem du vorübergehend die Option im Abschnitt des Dialogfelds auf der Registerkarte änderst. Ein Beispiel: Mit dem Namensformat „Vorname Nachname Suffix“ wird die Spalte nach dem Spitznamen sortiert.

Bei der Zusammenführung zweier Familien werden nicht nur die sekundären Objekte der Familie, sondern auch die beiden Väter und die beiden Mütter zusammengeführt.

Das Filter Gramplet in der Familienansicht ermöglicht die Suche nach Personen in verschiedenen Familienrollen. Du könntest also nach Familien mit einem Vater namens "John", einer Mutter namens "Mary" und einem Kind namens "Thomas" suchen.

## Die ![[_media/22x22-gramps-pedigree.png]] Schaubilderkategorie verwenden

![[_media/TimelinePedigreeView-Addon-Existing-Person-ContextMenu-example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Zeitleistestammbaum Ansicht- Zusatzmodul von Drittanbieter für Schaubilderkategorie - Kontextmenü Beispiel]] Gramps stützt sich stark auf formularbasierte Layouts verknüpfter Listenelemente. Diese implizieren Beziehungen zwischen Datensätzen in deinem Stammbaum. Die **Schaubildkategorie** bietet eine alternative, visuellere Möglichkeit, diese Beziehungen darzustellen. Die Positionen, Formen und Farben von Behältern sowie ihre Verbindungslinien & Pfeile können eine zusätzliche Beziehungstiefe mit verschiedenen Faktoren aufweisen. Behälter können einfache farbgefüllte Kästchen, Bögen, Bänder oder viele andere Formen sein.

Aber die [Schaubilderkategorie](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Kategorien#Schaubilderkategorie) bietet jedoch auch eine alternative Möglichkeit, durch den Stammbaum zu navigieren. Der Vorteil dieser Methode besteht darin, dass du mehr als eine Generation des Stammbaums sehen kannst. So kannst du direkt von einem Urenkel zu einem Urgroßvater springen, ohne die Zwischengenerationen zu durchlaufen.

Beachte das nach dem wechseln der aktiven Person in der Schaubilderkategorie die Ansicht neu aufgebaut wird, um die eingestellte Anzahl von Generationen beginnend mit der neuen Hauptperson anzuzeigen. Wenn du dich in der Schaubilderkategorie befindest, kannst du wie folgt durch die Mitglieder des angezeigten Stammbaum navigieren:

Um eine angezeigte Person zum Fokus der aktiven Person zu machen, klicke mit der linken Maustaste auf den entsprechenden Behälter. Wenn du mit der rechten Maustaste auf den Behälter klickst, wird ein Kontextmenü mit Optionen aufgerufen, die dem Inhalt entsprechen.

Das Kontextmenü für einen Personenbehälter kann ▶Untermenüs enthalten, in denen alle Ehepartner, Geschwister, Kinder und Eltern der entsprechenden Person aufgelistet sind. Der erste Eintrag im Kontextmenü ist normalerweise der Name der Person in diesem Behälter. (Alternativ kann es sich auch um eine Bearbeitungsoption handeln.) Durch Auswahl des Personennamens wird der Fokus auf die gleiche Weise verschoben wie durch Klicken mit der linken Maustaste auf den Behälter. Du kannst den Fokus der aktiven Person auch auf einen der Ehepartner, Geschwister, Kinder oder Eltern einer angezeigten Person ändern.

Einige Schaubildansichten weisen eine offensichtliche Navigationskorrelation auf. Wenn du dich intuitiv durch Generationen bewegst, entspricht dies der Bewegung nach links, rechts, oben oder unten im Diagramm. Diese verfügen möglicherweise über benutzerdefinierte Richtungsnavigationsschaltflächen, um die Navigation durch Klicken und nicht durch Ziehen zu ermöglichen.

Um beispielsweise den Fokus der [Stammbaumansich](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Kategorien#Ahnentafelansicht)t auf ein Kind (falls vorhanden) der aktuellen aktiven Person zu ändern, klicke auf die Schaltfläche (*Linke Pfeilspitze*) links neben dem Diagrammfeld der aktiven Person. Wenn es nur ein Kind gibt, ändert sich der Fokus sofort. Wenn die aktive Person mehr als ein Kind hat, wird die Schaltfläche (*Linke Pfeilspitze*) um ein Popup-Menü mit einer auswählbaren Liste der Kinder erweitert. (Für diese bestimmte Schaltfläche (*Linke Pfeilspitze*) wird die Popup-Menüliste der Kinder nach der Reihenfolge der Eheschließung der Eltern sortiert, sortiert nach der Reihenfolge der Geburt. Diese [Reihenfolge kann global in der Kategorie Beziehungen geändert werden](wiki:De:Gramps_6.0_Wiki_Handbuch_-_FAQ#Wie_.C3.A4ndere_ich_die_Reihenfolge_von_Kindern.3F).)

Wie Behälter können Schaltflächen über alternative Funktionen verfügen, auf die du zugreifen kannst, indem du mit der rechten Maustaste klickst und aus einem Kontext-Popup-Menü auswählst.

Andere Schaltflächen sind weniger offensichtliche Hilfsmittel, um nicht zu Personen, sondern zu Funktionen von Gramps zu navigieren. Wenn du das Beispiel der [Stammbaumansicht](wiki:Gramps_6.0_Wiki_Manual_-_Categories) erneut verwendest, wird beim Überfahren der Zeilen zwischen den Feldern ein Hinweis mit allen bekannten grundlegenden Details zur Beziehung angezeigt. Wenn du auf diese Zeilen doppelklickst, wird der Editor für diese Familie geöffnet. Durch Doppelklicken auf das Feld Aktive Person wird der Editor für diese Person geöffnet. Es lohnt sich, die ausführliche Dokumentation in jeder Diagrammansicht zu lesen, um diese versteckten Verknüpfungen zu bevorzugten Funktionen zu entdecken.

Die integrierten Ansichten der [Schaubildkategorie](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Kategorien#Schaubilderkategorie) werden im Referenzabschnitt [Kategorien](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Kategorien) vorgestellt. Einige werden ausführlicher in Artikeln beschrieben, die am Ende des Einführungsabschnitts der Ansicht aufgeführt sind.

Die Sammlung von Ansichten in der Schaubilderkategorie kann mithilfe der [Zusatzmodulverwaltung](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Zusatzmodulverwaltung) Funktion von Gramps um Zusatzmodule von Drittanbietern erweitert werden. Die verfügbaren Zusatzmodule von Drittanbietern findest du in der Spalte **Ansicht** der [Liste der Zusatzmodule](wiki:6.0_Addons#Addon_List). Die Pflege einiger Zusatzmodul-Ansichten von Drittanbietern wurde im Laufe der Jahre vom Gramps-Freiwilligenteam übernommen. Diese wurden nach der Überprüfung eingebaut und dann in die Hauptverteilungen von Gramps aufgenommen. Artikel zur Verwendung der einzelnen Zusatzmodul-Ansichten sind mit der Spalte **Zusatzmodul/Dokumentation** verknüpft. Die Qualität der Dokumentation variiert für diese Artikel erheblich.

## Gramplets verwenden

![[_media/DashboardCategory-DashboardView-default-gramplets-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Werkzeugbankkategorieansicht - mit Beispiel Gramplets gezeigt]]

In der [Seitenleiste und Fußleiste](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Gramplets#Die_Bildschirmunterteilung_Seitenleiste_.26_Fu.C3.9Fleiste) kannst du einige Gramplets wie diese aktivieren:

- [Angehörige](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Gramplets#Angeh.C3.B6rige)
- [Nachkommen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Gramplets#Nachkommen)
- [Ahnentafel](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Gramplets#Ahnentafel)
- [Fächergrafik](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Gramplets#F.C3.A4chergrafik)

Diese Beispiele bieten die Möglichkeit, den Fokus der aktiven Person unter Verwendung der Perspektive einer familiären Beziehung... zu nahen Verwandten, Nachkommen oder Vorfahren zu navigieren. Zukünftige Gramplets ermöglichen möglicherweise die Navigation nach geografischer Nähe, [DNA-Vergleich](wiki:Addon:DNASegmentMapGramplet) oder einer anderen Verbindung, die wir noch nicht berücksichtigt haben.

Die textbasierten Gramplets enthalten in der Regel Namen, die für die Navigation mit einem Hotlink verknüpft sind, während die grafischen Gramplets möglicherweise [Kontextmenüs](#Kontextmen.C3.BC-Navigation) verwenden. {{-}}

## Die Hauptperson setzen

Eine (und nur eine Person) kann in der Datenbank als die [Hauptperson](wiki:De:Gramps_Glossar#Hauptperson) gewählt werden. Sobald die Hauptperson festgelegt wurde, wird das Zurücksetzen des Fokus der [aktiven Person](wiki:De:Gramps_Glossar#aktive_Person) auf diese Person mit einem einzigen Klick erledigt, unabhängig davon, welche Kategorie gerade verwendet wird.

Um die Hauptperson zu setzen, [navigiere](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Navigation#Einstellen_der_aktiven_Person) zuerst zu der Person wie ist egal. Dann gehe zur Personenkategorie und wähle . Wenn die Startperson gesetzt ist, kannst du jederzeit von überall in der Datenbank durch einfaches klicken auf die ![[_media/Gramps_Go-Home48x48_win.png]] Schaltfläche in der Werkzeugleiste zu der Startperson navigieren. Du kannst auch aus dem Menü, den Eintrag aus jedem Kontextmenü welches mit rechts-Klick geöffnet wird oder das Tastenkürzel verwenden.

- [Einstellungen#Hauptperson setzen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Einstellungen#Hauptperson_setzen)
- Im Dialogfeld [Person bearbeiten](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Daten_eingeben_und_bearbeiten:_Ausführlich_-_Teil_1#Person_bearbeiten_Dialog) kannst du im Kontextmenü auswählen.

## Einstellen der aktiven Person

Es wird erwartet, dass die [aktive Person](wiki:De:Gramps_Glossar#aktive_Person) im Kontext von Aktionen, Berichten und Änderungen steht. Sie sind das ausgewählte Element in der Personenansicht oder oben in der Beziehungsansicht.

Der Fokus Aktive Person kann direkt ausgewählt oder indirekt "angesteuert" werden. Die Methoden umfassen:

- Klicken auf den Eintrag einer Person in der Personenansicht
- Auswahl der Person aus dem Menü [Lesezeichen](#Lesezeichen_Navigation)
- [Verwendung verlaufbasierender Navigation](#Verwendung_verlaufbasierender_Navigation) ( und Werkzeugleisteschaltflächen und das Menü)
- [Hotlink Navigation](#Hotlink_Navigation)
- [Kontextmenüs](#Kontextmen.C3.BC-Navigation)
- [Notizen als Navigationsverknüpfungen](#Notizen_als_Navigationsverkn.C3.BCpfungen)

In der Personenansicht gibt es ein Auswahlhervorhebung als visuellen Hinweis auf die aktive Person. In der Beziehungsansicht wird die aktive Person in einem separaten Abschnitt oben angezeigt. Alle anderen unten aufgeführten Personen haben eine unmittelbare Beziehung (Eltern, Geschwister, Ehepartner, Kind) zur aktiven Person. Optional kann die [Statusleiste](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Einstellungen#Anzeige) so eingestellt werden, dass das Fokusobjekt für die Ansichtskategorie aufgelistet wird. (Die Aktive Person ist der Fokus für mehrere Ansichtskategorien.)

### Hotlink Navigation

Normalerweise wird durch einfaches Klicken auf den Hotlink-Namen einer Person diese Person ausgewählt und der Kontextfokus auf diese als aktiven Person verschoben.

![[_media/Relationships-category-view-default-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Beziehungenkategorieansicht]]Der Name jeder Person in den Kategorienansichten Personen und Beziehungen ist ein Hotlink. Durch Ändern des Fokus der aktiven Person in der Personenansicht wird lediglich geändert, welcher Datensatz hervorgehoben ist. Dies führt jedoch auch dazu, dass der Inhalt von Gramplets aktualisiert wird und die Ansichten Beziehungen, Schaubilder und Geografie neu auf die neue aktive Person ausgerichtet werden.

Die Auswahl eines anderen Hotlink-Namens in der Ansicht Beziehungenkategorie führt zu einer weniger subtilen Änderung. Die Perspektive, wie die Familiendaten dargestellt werden, ändert sich in Richtung dieses Fokus. Ihre Details werden in den oberen Bereich verschoben und ihre unmittelbare Familie wird unten neu angeordnet.

{{-}}

### Kontextmenü-Navigation

Hotlink-Namen auf der Registerkarte Referenzen und in den Notizen (und in einigen Gramplets) öffnen jedoch lediglich das Fenster Personeneditor, *ohne* im Fokus der aktiven Person zu dieser Person zu navigieren. (Diese Links verhalten sich so, als hättest du auf eine Schaltfläche anstelle eines Hotlink-Namens geklickt.) Dies erleichtert das schnelle Bearbeiten von Personen um die aktive Person herum, ohne die Desorientierung eines Fokuswechsel.

![[_media/QuickViewReport-EditPerson-context-menu-popup-default-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Kontextmenü im Personeditor]] Der Fokus der aktiven Person kann im Dialogfeld mithilfe des Kontextmenüs (Rechtsklick) im leeren Bereich des Kopfbereichs festgelegt werden. Die Option in diesem Kontextmenü ändert den Fokus der aktiven Person auf die Person, die bearbeitet wird. {{-}}

### Verwendung verlaufbasierender Navigation

![[_media/History-based-navigation-tools-Go-menu-example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Beispiel für die verlaufsbasierten Navigationswerkzeuge ("Gehe" Menü)]]

Gramps bietet auch eine Reihe leistungsstarker verlauf basierender Navigationswerkzeuge. Diese Werkzeuge ähneln denen , die normalerweise in in Webbrowsern verwendet werden.

Dazu gehören die Optionen und im Menü , Kontextmenüs und Tastenkombinationen (verfügbar in den Kategorien Personen, Familie und Stammbaum) sowie die Symbolleisten-Schaltflächen und in Gramps. Außerdem enthalten sie die Liste der zuletzt ausgewählten Elemente im Menü , über die du direkt zu einem der zuletzt ausgewählten Elemente springen kannst. Wenn du auf die Symbolleisten-Schaltflächen und klickst, gelangst du zum vorherigen oder nächsten Objekt im Verlauf. {{-}}

- [Navigation Verlauf](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Navigation#Navigation_Verlauf)

### Lesezeichen Navigation

![[_media/Gramps_Go-Home48x48_win.png]] Die in der Symbolleiste ist ein Lesezeichen für Sonderfälle. Dadurch wird der Fokus der aktiven Person auf die Person verschoben, die derzeit als [Hauptperson](wiki:De:Gramps_Glossar#home_person) festgelegt ist. Dies ist so häufig nützlich, dass diese Funktion auch eine [Tastenkombination](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Tastenkürzel_Referenz#Allgemeine_K.C3.BCrzel) aufweist. {{-}} Ähnlich wie beim festlegen der Startperson, kannst du andere Personen aus der Datenbank mit einem Lesezeichen versehen, um die spätere Navigation zu dieser Person zu vereinfachen. Um ein Lesezeichen zu einer Person hinzuzufügen, navigiere zu der Person und wähle dann oder verwende die [Tastenkombination](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Tastenkürzel_Referenz#Allgemeine_K.C3.BCrzel) . Wenn keine Person ausgewählt ist, erhältst du die Warnung [Lesezeichen konnte nicht gesetzt werden](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Fehler_und_Warnung_Referenz#Lesezeichen_konnte_nicht_gesetzt_werden)}}. Um zu dieser Person von überall in der Datenbank zu gelangen, wähle .

#### Dialogfeld Lesezeichen organisieren

![[_media/OrganizeBookmarks-dialog-example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Lesezeichen verwalten" - Dialog - Beispiel]]

Du kannst über oder [Tastenkürzel](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Tastenkürzel_Referenz) deine Lesezeichen verwalten. Dies öffnet den folgenden Dialog mit einer Liste der Lesezeichen und Bedienelemente diese zu modifizieren.

Verwende die und Schaltflächen um die Reihenfolge in der Liste zu ändern. Verwende die Schaltfläche um ein Lesezeichen zu löschen. Die Schaltfläche bringt dich auf diese Seite und du schließt das Fenster schließt du mit der Schaltfläche.

Die mit einem Lesezeichen versehene Person kann in der Personenkategorie, wie oben beschrieben, aber auch in der Beziehungenkategorie, Familienkategorie, und der Schaubilderkategorie ausgewählt werden.

Auf ähnliche Weise kannst du auch für folgendes Lesezeichen erstellen: Ereignisse, Quellen, Fundstellen, Orte, Medien, Aufbewahrungsorte und Notizen

{{-}}

### Notizen als Navigationsverknüpfungen

![[_media/Note-showing-tooltip-for-link-example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Notiz-Editor - Verknüpfen von Text]] Es gibt separate Lesezeichenlisten in mehreren Kategorien. Aber es sind immer noch einfache Listen. Lange Listen von Lesezeichen werden schnell unhandlich.

Permanente Links können in [Notizen](wiki:De:Gramps_Glossar#Notiz) erstellt werden. Verwende den [Verknüpfungeditor](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Daten_eingeben_und_bearbeiten:_Ausführlich_-_Teil_2#Verkn.C3.BCpfungeditor) in Notizen, um Navigationslinks zu verschiedenen Arten von Gramps-Datensätzen gemäß Ihren eigenen Organisationsmethoden zu organisieren. Sobald eine Notiz Text verknüpft hat, kann dieser verknüpfte Datensatz wie ein Lesezeichen verwendet werden. In Notiz-Gramplets, in denen die Bearbeitung nicht aktiv ist, öffnet ein Klick auf den Link den Objekteditor für diesen Link. (Es erfordert einen zusätzlichen Modifikator im Notizeditor: Navigiere zu diesem Datensatz, indem du die Taste gedrückt hältst und auf den verknüpften Text klickst.) Eine Notiz kann als verknüpfter Index für andere Notizen mit unterschiedlichen Verknüpfungssätzen verwendet werden.

Ein Beispiel für eine verknüpfte Notiz könnte einen Nachruf enthalten, in dem alle Personen, Orte oder sogar die Ereignisse verknüpft sind. Dies erleichtert die Navigation zu den indirekt verwandten (oder sogar nicht verwandten) Sargträgern, Bestattungsunternehmen oder Teilnehmern.

Ein weiterer Hinweis könnte die transkribierte Bibliographie für die veröffentlichte Originalforschung eines anderen Genealogen sein. Wenn du digitale Kopien dieser ursprünglich zitierten Referenzen sammelst, kann die verknüpfte Bibliographie als Checkliste für die Quellenerfassung verwendet werden. Wenn die Bibliographie vollständig verknüpft ist, kann sie verwendet werden, um für jedes Zitat durch die Quellen zu navigieren und nach nicht unterstützten Schlussfolgerungen, Ungenauigkeiten oder Auslassungen zu suchen. {{-}}

## Datensätze finden

### Zu einem Datensatz navigieren

Um einen Datensatz in einer der Kategorielistenansichten zu suchen, wechsle zunächst zu der entsprechenden Kategorie, die die Liste der gewünschten Datensätze enthält: Personen, Quellen, Orte oder Medien. Blättere dann zu dem gewünschten Datensatz. Der Fokus des aktiven Datensatzes für die Kategorie wird durch die Auswahl eines Datensatzes geändert. Durch einfaches Blättern in der Ansicht wird der Fokus des aktiven Datensatzes nicht geändert.

Standardmäßig wird die Liste nach der ersten Spalte der tabellarischen Daten sortiert. Bei gruppierten Datensätzen (Personen) oder hierarchischen Baumstrukturen (Orte) muss die erste Spalte die Spalte "Name" sein. Bei den Personen basiert die Gruppierung auf dem bevorzugten Nachnamen. Bei den Orten basiert die Gruppierung auf der Reihenfolge der umgebenden Orte.

Die Reihenfolge und die Anzeige (oder das Ausblenden) von Spalten kann konfiguriert werden. Ein Dialog erscheint nach Auswahl des Menüpunkts oder nach Klicken auf die Schaltfläche Konfigurieren in der Symbolleiste oder nach Verwendung der [allgemeine Tastenkombination](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Tastenkürzel_Referenz#Allgemeine_K.C3.BCrzel) Aktive Ansicht konfigurieren.

Die Liste der Datensätze in der Ansicht kann durch Filtern mit der [Suchleiste](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Hauptfenster#Suchleiste) oder dem [Filter Gramplet](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Gramplets#Filter) reduziert werden. {{-}}

### Datensatz finden

![[_media/Find-type-ahead-search-PeopleTreeView-list-example-detail-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Interaktives Suchfeld am Ende der Listenansicht – Beispiel]] ![[_media/Find-type-ahead-search-PeopleTreeView-list-example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Beispiel für die Suche nach einer Vorabsuche im Listenbeispiel „Personenstrukturansicht“]]

Auch bekannt als "interaktive Suche mit Vorauswahl".

Wähle eine Zeile in der Liste aus, um den Fokus zu erhalten, und beginne dann mit der Eingabe von Informationen (die in den Daten der aktuellen Sortierspalte enthalten sind) zu einer Person oder dem Titel eines Quellen-, Orts- oder Medienobjekts, das du zu finden versuchst. Der Fokus wird auf den ersten Datensatz verschoben, der mit dem Text im Suchmodus-Textfeld übereinstimmt.

Alternativ kannst du, nachdem du auf eine beliebige Stelle in der Hauptansicht geklickt hast, um den Fokus zu setzen, die [Tastenkombination](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Tastenkürzel_Referenz#Alle_Listenansicht_K.C3.BCrzel) ( unter macOS) drücken, um das Suchmodus-Textfeld zu aktivieren. Diese Tastenkombination wird oft übersehen, da es ausreicht, einfach mit der Eingabe zu beginnen, um das Feld zu öffnen und den Suchbegriff einzugeben.

Während der Eingabe wird der erste übereinstimmende Datensatz in der Sortierspalte der Liste in die Mitte der Liste gescrollt und ausgewählt. Wenn du mehr Zeichen eingibst, wird die Übereinstimmung verfeinert. Solange das Textfeld für den Suchmodus sichtbar ist, wird durch Drücken der Cursortaste mit dem Abwärtspfeil zur nächsten Übereinstimmung gewechselt, während durch Drücken der Cursortaste mit dem Aufwärtspfeil zur vorherigen Übereinstimmung gewechselt wird. Die Box verschwindet, nachdem sie im Leerlauf ist. (Wenn zwischen 5 und 15 Sekunden lang keine Tastenanschläge aufgetreten sind.) Wenn das Feld Suchen nicht aktiviert ist, verschieben die Cursorsteuertasten die Datensatzauswahl in der Liste nach oben und unten.

Wenn du die Sortierspalte änderst (indem du auf die Kopfzeile klickst), wird auch die Spalte geändert, die abgeglichen wird. Die Suche in einer anderen Sortierspalte funktioniert am besten in flachen Listenansichten.

Personen- oder Ortskategorie-Ansichtsmodi mit hierarchischer Gruppierung sind etwas weniger reaktionsschnell als die flache Listenansicht, die bereits alphabetisch sortiert ist. Die gruppierte Person ist die komplexeste Funktionalität. Standardmäßig wird sie nach dem Gruppierungsnamen sortiert und dann nach der Spalte "Name" im "Anzeigen als"-[Namensformat](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Einstellungen#Anzeigename-Editor) aus dem Menü „Daten“ der Einstellungen untersortiert. Dabei handelt es sich um den bevorzugten/vorrangigen Namen im Format "Nachname, Vorname, Suffix", wobei der „Nachname“ das Präfix und die Konnektoren enthält. Die Einstellungen "Gruppieren als", "Sortieren als" und "Anzeigen als können jedoch verwendet werden, um die Reihenfolge mit Hilfe des "[Namenseditors](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Daten_eingeben_und_bearbeiten:_Ausführlich_-_Teil_3#Namenseditor)" außer Kraft zu setzen. {{-}}

### Springe zu mit Gramps ID

![[_media/Jump-to-by-Gramps-ID-dialog-example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Gehe zu Gramps ID - Dialog - Beispiel]]

Wenn du die ID des Zieldatensatzes in der gerade aktiven Kategorie kennst, kann die Funktion **Springen zu** der effizienteste Weg sein, um zu diesem Ziel zu navigieren.

Wenn du die [Tastenkombination](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Tastenkürzel_Referenz#Allgemeine_K.C3.BCrzel) drückst, wird das Dialogfeld Springe zu nach Gramps-ID angezeigt, in das du die \[De:Gramps_6.0_Wiki_Handbuch\_-\_Einstellungen#ID-Formate\|Gramps-ID\]\] in der aktuellen Ansicht eingeben kannst, die du aktivieren möchtest.

sucht nur nach einer exakten Textübereinstimmung. Die Gramps-ID kann entweder automatisch generiert werden, wenn das ID-Feld beim Hinzufügen eines Datensatzes leer gelassen wird, oder [manuell als Überschreibung eingegeben](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Daten_eingeben_und_bearbeiten:_Ausführlich_-_Teil_1#ID) werden.

Es ähnelt „Suchen“, außer dass es nicht interaktiv ist und NUR auf das Gramps-ID-Feld und nicht auf die aktuell zum Sortieren ausgewählte Spalte funktioniert. Und kann den Fokus für den aktiven Datensatz in jeder Ansichtskategorie außer den Kategorien „Geografie“ und „Werkzeugbank“ ändern.

#### Siehe auch

- [Die Diskussion über die Funktion "Springe zu" Gramps ID](https://gramps.discourse.group/t/the-ctrl-j-jump-to-gramps-id-feature/3756)

<!-- -->

- GEPS: [Selektor-Designvorschläge](wiki:GEPS_041:_New_Selector)

{{-}}

### Navigation Verlauf

Es wird eine Historie der zuletzt aktiven Datensätze für den Fokus der aktiven Kategorie geführt. Die letzten zehn Datensätze sind über das Menü und seine [Tastenkombinationen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Tastenkürzel_Referenz#Allgemeine_K.C3.BCrzel) zugänglich. Du kannst auch mit den Cursortasten links und rechts durch den Fokusverlauf blättern.

## Die Zwischenablage verwenden

![[_media/Clipboard-dialog-example-context-menu-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Zwischenablage - Dialog - Zeigt Kontextmenü (Rechtsklick) Beispiel]]

Für eine Anwendung wie Gramps ist die sehr wichtig, da sie dazu beiträgt, die wiederholte Dateneingabe zu reduzieren.

Das Werkzeug bietet einen temporären Notizblock zum Speichern von Datenbankeinträgen zur einfachen Wiederverwendung während einer einzelnen Gramps-Sitzung, z.B.: Bis du Gramps beendest. Kurz gesagt, dies ist eine Art Kopier- und Einfügefunktion, die von Textobjekten auf andere Arten von Datensätzen erweitert wird, die in Gramps verwendet werden. In der Zwischenablage wird die [*Drag & Drop*](https://de.wikipedia.org/wiki/Drag_and_Drop) Technik in großem Umfang verwendet.

Um die aufzurufen, wähle entweder das Menü oder klicke auf die Schaltfläche ![[_media/Gramps_Clipboard48x48_win.png]] in der Symbolleiste oder verwende die [Tastenkombination](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Tastenkürzel_Referenz#8) .

{{-}}

Die unterstützt Adressen, Attribute (beide persönlich und familiär), Ereignisse (beide persönliche und familiäre), Namen, Medienobjektreferenzen, Fundstellen, URLs und natürlich Textinformationen von Notizen und Kommentaren. Zum speichern jeglicher Art dieser Datensätze, ziehe den entsprechenden Datensatz aus dem entsprechenden Bearbeiten Dialog in die Zwischenablage. Zur Wiederverwendung des Datensatz ziehe ihn von der Zwischenablage an die entsprechende Stelle im Editor z.B. Adressenreiter, Attributereiter, usw..

### Zwischenablage Kontextmenü

Wenn du einen Datensatz über das Kontextmenü auswählst (Rechtsklick), werden die folgenden drei Optionen für jeden Datensatztyp angezeigt:

- 

- 

- 

{{-}}

Ein Beispiel  
Du findest die Geburtsurkunde einer Person. In dieser Urkunde werden auch die Zeugen genannt. Und die Geburtsurkunde bestimmt wo diese Information aufbewahrt wird. Der beste Weg ist, die Zwischenablage zu öffnen, und die Quelle, mit der du arbeiten möchtest, dorthin zu ziehen. Dann verwende ziehen und ablegen um sie in neuen Objekten, die du verwendest, zu verwenden.

Jetzt kannst du die Informationen in dem Personeneditor vervollständigen. Ziehe diese Information auch in die Zwischenablage.

Nun fügst du zwei Personen für die Zeugen hinzu (wenn sie noch nicht in deiner Datenbank existieren). Ziehe die Geburtsinformation einfach in die Ereignisansicht der Zeugen und lege sie dort ab. Du siehst dann die Ansicht in der du die Rolle des Zeugen auf Zeuge für dieses Geburtsereignis ändern kannst. Wiederhole diesen Vorgang mit dem anderen Zeugen.

Dies erspart dir eine Menge Schreibarbeit und mögliche Fehler.

<span id="Using the Addon Manager..."></span>

## Verwendung der Erweitungsverwaltung

![[_media/AddonManager-addons-listing-60-de.png|Right|thumb|550px|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Der "Erweiterungsverwaltung" Dialog zeigt den  Reiter]]

Du kannst die über das Menü aufrufen oder wähle das Symbol in der Symbolleiste, um das Fenster der anzuzeigen, in dem die verfügbaren Addon-Plugins von Drittanbietern basierend auf den aktuell ausgewählten Projekten auf der Registerkarte aufgelistet werden.

Gramps nutzt integrierte und Addon-Plugins (auch "[Plug-in](https://de.wikipedia.org/wiki/Plug-in)" genannt), um die Funktionen der Kernanwendung zu erweitern. Einer der Hauptvorteile eines Plugin-Frameworks besteht darin, dass es die Weiterentwicklung einer bestimmten Funktion ermöglicht, ohne dass das gesamte Programm aktualisiert werden muss. Erweiterungen sollten nicht als weniger nützlich für Basisbenutzer angesehen werden als Kernfunktionen oder integrierte Plugins. Auch bedeutet „Drittanbieter” nicht, dass eine Erweiterung von geringerer Qualität ist. Die im GitHub-Repository des Gramps-Projekts veröffentlichten Erweiterungen wurden jedoch geprüft und verändern deine Stammbaumdaten nicht heimlich.

Die [Erweiterungsverwaltung](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Navigation#Erweiterungsverwaltung) bietet dir die Möglichkeit, zu erkunden, welche Erweiterungen deine persönlichen Arbeitsabläufe verbessern können. Und die [Zusatzmodulverwaltung](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Zusatzmodulverwaltung) (oder die Erweiterung [Plugin-Verwaltung erweitert](wiki:Addon:Plugin_Manager)) bietet dir die Möglichkeit, Gramps so anzupassen, dass nicht benötigte Funktionen entfernt werden.

{{-}}

<span ID="Addon Manager..."></span>

### Zusatzmodulverwaltung

Die zeigt die folgenden drei Registerkarten an:

- Auf der Registerkarte {man label\|[Erweiterungen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Navigation#Erweiterungen)}} wird standardmäßig die Liste der verfügbaren Erweiterungen angezeigt.
- Die Registerkarte {man label\|[Einstellungen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Navigation#Einstellungen)}}, auf der Optionen geändert werden können
- Die Registerkarte , auf der Verknüpfungen zu externen oder lokalen Erweiterungen-Repositories hinzugefügt werden können.

{{-}}

#### Erweiterungen

![[_media/AddonManager-addons-tab-default-60-de.png|Right|thumb|550px|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Registerkarte <strong>Erweiterungen</strong> für die <strong>Erweiterungsverwaltung</strong> Dialog mit Standardfiltern beim Laden der Liste der verfügbaren Erweiterungen]]

![[_media/AddonManager-addons-tab-default-no-internet-60-de.png|Right|thumb|550px|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Registerkarte <strong>Erweiterungen</strong> für die <strong>Erweiterungsverwaltung</strong> Dialog zeigt das Ergebnis Keine Internetverbindung an]]

Die Registerkarte der zeigt eine Liste der verfügbaren Erweiterungen an, nachdem die Listen von der [Gramps-Projekt Standardserver](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Navigation#Projekte) geladen wurden, wofür eine Internetverbindung erforderlich ist. Die Liste kann durch Klicken auf die Schaltfläche neu geladen werden. Die Erweiterungsverwaltung ist auch ohne geladenen Stammbaum verfügbar. Die Schaltfläche zeigt diesen Abschnitt an.

Im oberen Bereich des Fensters befindet sich ein , in das du einen beliebigen Teil des Erweiterungsnamens eingeben kannst. Die Ergebnisse darunter werden dann auf die passenden Erweiterungen beschränkt/gefiltert.

Unterhalb des Suchfeldes befinden sich fünf Erweiterungen (siehe: [Legende zur Erweiterungenliste](wiki:Addon_list_legend)) und eine Schaltfläche , um wieder alle Ergebnisse anzuzeigen:

- Installationsstatus:
  - – *Standard*

  - Nicht installiert

  - Installiert

  - Aktualisierungen
- Projekt: – *Standard*
- Art: – *Standard*
- Zielgruppe: – *Standard*
- Status: – *Standard*

Um die gewünschte Erweiterung zu installieren, verwende die verschiedenen Suchfilter und wähle dann die Schaltfläche in der [Erweiterungsliste](#Erweiterungsliste) aus. Nach der Installation wird die Versionsnummer der Erweiterung auf der rechten Seite des Eintrags angezeigt, sofern alle erforderlichen Voraussetzungen erfüllt sind.

Du kannst den ersten Filter (Installationsstatus) von auf ändern, um manuell nach neuen Versionen deiner installierten Erweiterungen zu suchen. Oder du kannst Gramps automatisch nach Erweiterungen suchen lassen, indem du die unter [Erweiterungen von Drittanbietern: Installieren von Erweiterungen](wiki:6.0_Addons#Installing_Addons_in_Gramps) in Gramps gezeigten Einstellungen verwendest.

Der Erweiterungsmanager unterstützt das Entfernen nicht. Dazu kannst du die [Zusatzmodulverwaltung](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Zusatzmodulverwaltung) verwenden, um die Erweiterung auszublenden.

##### Erweiterungsliste

![[_media/AddonManager-addons-listing-60-de.png|Right|thumb|550px|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} <strong>Erweiterungsverwaltung</strong> Dialog zeigt die  Registerkarte mit installierten Erweiterungen]]

Jede Erweiterungsliste enthält die folgenden Informationen:

- Erweiterungsname
- Die zweite Zeile zeigt mehrere farbige Kästchen mit Details:
  - Linke Seite: *Projekt*, *Art*, *Zielgruppe*, *Status*, *Version*
  - Rechte Seite: *Installierte Version* der Erweiterung, wird nur angezeigt, wenn sie installiert ist.
- Beschreibung
- Die untere Leiste kann je nach Installationsstatus mehrere Schaltflächen anzeigen:
  - Linke Seite: -Schaltfläche mit einem Link zur Support-Seite für Erweiterungen, wird nur angezeigt, wenn verfügbar.
  - Rechte Seite: Schaltfläche .

siehe: [Legende zur Erweiterungsliste](wiki:Addon_list_legend) {{-}}

#### Einstellungen

![[_media/AddonManager-Settings-tab-default-60-de.png|Right|thumb|550px|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} <strong>Erweiterungsverwaltung</strong> Dialog mit Standard  Registerkarte]]

##### Allgemein

-   
  Standardmäßig nicht ausgewähltes Kontrollkästchen

Die Registerkarte „Einstellungen“ des Erweitungsverwaltungdialogfelds enthält die folgenden zwei Abschnitte:

- Alllgemein
- Zeitgesteuerte Aktualisierungsprüfungen

##### Zeitgesteuerte Aktualisierungsprüfungen

Die folgenden Einstellungen gelten nur für das Fenster

- Wähle die Häufigkeit, mit der Gramps nach [Aktualisierungen](wiki:6.0_Addons#Installing_Addons_in_Gramps) für Erweiterungen sucht. Standard:

  - *Nie* - prüft nie auf Aktualisierungen, wenn du Gramps startest (*Standard*)
  - *Einmal im Monat* - prüft einmal im Monat beim Start von Gramps auf Aktualisierungen
  - **Einmal pro Woche** - prüft einmal pro Woche beim Start von Gramps auf Aktualisierungen
  - *Einmal am Tag* - prüft einmal täglich beim Start von Gramps auf Aktualisierungen
  - *Immer* - prüft auf Aktualisierungen, wenn du Gramps startest

- Standard: Wenn du also nach Updates suchst, prüft es nach:

1.  1.  *Nur aktualisierte Erweiterungen* - prüft nicht auf neue Erweiterungen
    2.  *Nur neue Erweiterungen* - prüft nicht auf aktualisierte Erweiterungen (*Standard*)
    3.  **Neue und aktualisierte Erweiterungen** - prüft auf alle neuen und aktualisierten Erweiterungen

-   
  Standardmäßig ausgewähltes Kontrollkästchen

  - Markiert: Bedeutet, dass neue/aktualisierte Erweiterungen nur einmal abgefragt werden; danach werden sie dir nicht mehr angezeigt (**Kontrollkästchen standardmäßig aktiviert**).

  - Nicht angekreuzt: Bedeutet, dass dir neue/aktualisierte Erweiterungen immer angezeigt werden.

-   
  Schaltfläche geht davon aus, dass du eine **Internet**-Verbindung hast, und wenn du sie drückst, wird eine Prüfung auf Erweiterungen basierend auf den obigen Einstellungen erzwungen. Wenn Erweiterungen verfügbar sind, wird das Fenster ) angezeigt, aus dem du sie auswählen und installieren kannst.

{{-}}

##### Verfügbare Gramps-Aktualisierungen für Erweiterungen

![[_media/AvailableGrampsUpdatesforAddons-example-listing-60-de.png|Right|thumb|550px|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} <strong>Verfügbare Gramps-Aktualisierungen für Erweiterungen</strong> Dialog nach der Überprüfung auf aktualisierte Erweiterungen auf der Registerkarte]]

Im Fenster wird eine nach **[Art](wiki:Addon_list_legend#Type)** gegliederte Liste angezeigt, die du durch Auswahl der Spalte `Auswählen` anzeigen kannst, um die Pfeile der obersten Ebene zu erweitern und die Einträge unter dieser `Art` anzuzeigen, die den `Namen` und die `Beschreibung` der Erweiterungen anzeigen.

- Du kannst dann das Kontrollkästchen der Erweiterung aktivieren, die du installieren möchtest.
  - Alternativ, aber nicht empfohlen, kannst du die Schaltfläche verwenden.
  - Mit

###### Fortschrittsinformationsfenster

![[_media/ProgressInformation-window-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Erweiterung Fortschrittsinformationen Fenster - Beispiel]] Das Fenster wird während des *Herunterladen und Installieren ausgewählter Erweiterungen...* angezeigt.

Bei Bedarf kannst du das Herunterladen . {{-}}

###### Fertig mit dem Herunterladen und Installieren von Erweiterungen Dialog

![[_media/DoneDownloadingAndInstallingAddons-dialog-example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Dialogfeld Erweiterungen heruntergeladen und installiert – Beispiel]] Der Dialog wird nach Abschluss des Downloads angezeigt und gibt Auskunft darüber, wie viele Erweiterungen installiert wurden, sowie einen Hinweis, dass du Gramps neu starten musst, wenn du eine „Ansicht“-Erweiterung installiert hast. Wähle die Schaltfläche , um fortzufahren. {{-}}

#### Projekte

![[_media/AddonManager-Projects-tab-default-60-de.png|Right|thumb|550px|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} <strong>Erweiterungsverwaltung</strong> Dialog mit Standard-Registerkarte]]

Wo kann man nach Erweiterungen suchen? Entweder auf dem *Standard* Hauptserver vom Gramps Projekt *Standard*:

- **Gramps**:

:;https://raw.githubusercontent.com/gramps-project/addons/master/gramps60

Oder alle Gramps-kompatiblen Erweiterungsserver, die du hinzugefügt hast. Der [Andere Projekte](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Navigation#Andere_Projekte) Abschnitt zeigt eine Liste der bekannten externen Projekte.

Unten links auf der Registerkarte Projekte hast du die folgenden Optionen

- \- öffnet das Dialogfeld {man label\|[Neues Projekt](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Navigation#Neues_Projekt_Dialog)}}, in dem du den Projektnamen und die URL hinzufügen kannst.

- \- löscht die ausgewählten Projektzeilen. (Das Gramps-Standardprojekt kann nicht gelöscht werden, aber es kann abgewählt werden, so dass auf diesem Server nichts markiert ist).

- \-

- \-

- \- öffnet das Dialogfeld , in dem bei Auswahl von alle anderen Projekte entfernt werden.

{{-}}

##### Neues Projekt Dialog

![[_media/NewProject-default-dialog-60-de.png|Right|thumb|450px|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} <strong>Neues Projekt</strong> Dialog - Standard]]

Der Dialog ermöglicht die Eingabe von und der externen Projekte und kann auch für lokale Projekte verwendet werden. {{-}}

##### Andere Projekte

![[_media/AddonManager-Projects-tab-with-default-and-known-external-other-projects-60-de.png|Right\|thumb\|550px\|Abb. {{#var:chapter}}.{{#vardefineecho:figure\|{{#expr:{{#var:figure}}+1}}}} **Zusatzmodulverwaltung** Dialog mit optionalen Projekten Registerkarte]] Liste bekannter externer Projekte (kopiere den **Projektnamen** und die **URL** nach Bedarf in das Dialogfeld )

<hr>

- **Projektname:** `Isotammi project addons`

:;URL:

:;https://raw.githubusercontent.com/Taapeli/isotammi-addons/master/addons/gramps60

  
Zusammenfassung: [Addon:Isotammi project](wiki:Addon:Isotammi_addons)

<hr>

- **Projektname:** `Jean Michault tools for FamilySearch`

:;URL:

:;https://raw.githubusercontent.com/jmichault/gramps-kromprogramoj/gramps60

  
Zusammenfassung: <https://github.com/jmichault/gramps-kromprogramoj> & [PersonFS](https://github.com/jmichault/PersonFS) gramplet (FamilySearch) / <https://github.com/jmichault/gramps-kromprogramoj/blob/gramps60/ReadMe.en.md>

<hr>

- **Projektname:** `GlopGlop’s collection for France`

:;URL:

:;https://raw.githubusercontent.com/grocanar/glopglop-addons/main/gramps60

  
Zusammenfassung: GedcomforGeneanet & ImportGenewebPlus

<hr>

- **Projektname:** `ztlxltl experimental FamilyTreeView (FTV) chart view`

:;URL:

:;https://raw.githubusercontent.com/ztlxltl/FamilyTreeView/dist/gramps60

  
Zusammenfassung:<https://github.com/ztlxltl/FamilyTreeView> [Erweiterung Stammbaumansicht](wiki:Addon:FamilyTreeView)

<hr>

- **Projektname:** `ChatWithTree - Von MelleKoning (Hace)`

:;URL:

:;https://raw.githubusercontent.com/MelleKoning/addons/refs/heads/myaddon60/gramps60

  
Zusammenfassung: [ChatWithTree](wiki:Addon:ChatWithTree) ist ein Chatbot zur Interaktion und Abfrage eines Gramps- Genealogie-Stammbaums.

<hr>

- **Projektname:** `WebSearch - von Urchello (Hace)`

:;URL:

:;https://raw.githubusercontent.com/jurchello/WebSearch/dist/gramps60

  
Zusammenfassung: [WebSearch](wiki:Addon:WebSearch) ist ein Gramplet zur Websuche anhand von Parametern, die auf dem aktuellen Datensatz oder einer als Attribut gespeicherten ID basieren.

<hr>

Es gibt einen Discouse Community-Support-Thread, in dem andere [„Projekte“](https://gramps.discourse.group/t/curated-addon-collections/7170) (oder kuratierte Sammlungen von Gramps-Erweiterungen) aufgeführt sind.

<hr>

Du kannst auch lokale Projekte hinzufügen, siehe Beispiel-Screenshot.

Lokales Beispiel für Microsoft Windows  
Pfad zu deinem lokalen Projekt, nützlich für Entwickler, die Erweiterungen erstellen. Die Zeichenfolge **<file:///>** bezieht sich auf den internen Speicher, um auf den internen Speicher eines Windows-PCs zuzugreifen.

- **Projektname:** `Lokales Beispiel`

:;URL:

:;file:///c/Users/User/Desktop/gramps60

{{-}}

##### Projektvorgaben wiederherstellen

![[_media/Restore-project-defaults-dialog-60-de.png|Right|thumb|550px|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} <strong>Projektvorgaben wiederherstellen</strong> Dialog]]

Bei Bedarf kannst du überprüfen, ob in der Registerkarte die richtige URL angegeben ist. Um die [Liste der Erweiterungen](https://raw.githubusercontent.com/gramps-project/addons/master/gramps60/listings/addons-en.json) für deine aktuelle Sprache und Version zu finden, sollte sie eingestellt sein auf:

:;https://raw.githubusercontent.com/gramps-project/addons/master/gramps60 wenn nicht, wähle die Schaltfläche auf der Registerkarte „Projekte“, die alle Einträge außer dem Standardeintrag entfernt.

{{-}}

## Verwendung des Rückgängig-Verlaufs

![[_media/Menubar-Edit-defaults-family-tree-loaded-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menüleiste – Bearbeiten Übersicht]] Eine Arbeitssitzung verfügt über einen Rückgängig-Verlauf, um Transaktionen rückgängig zu machen.

Drei zugehörige Menüoptionen:

- – Zeigt die letzte Änderung an, die rückgängig gemacht werden kann.

- – Zeigt die letzte Änderung an, die rückgängig gemacht werden kann.

- – Zeigt das Dialogfeld [Rückgängig-Verlauf](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Navigation#Undo_History_dialog)}} an.

Siehe [Tastenkombinationen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Tastenkürzel_Referenz).

Verschiedene Aktionen setzen den Änderungsverlauf der Sitzung zurück und zeigen die an:

- Einige Werkzeuge und Importvorgänge sind Stapelverarbeitungen, sodass der Benutzer gewarnt wird, bevor der Rückgängig-Verlauf verloren geht/gelöscht wird.
- Die Menüoption macht den Rückgängig-Verlauf rückgängig.
- Gramps beenden und neu starten.

Siehe auch:

- -Gramplet – Verfolgt die Aktivitäten in dieser Sitzung. Es listet ausgewählte und bearbeitete Objekte auf.

- Der Rückgängig-Verlauf kann aufgerufen werden, auch wenn nichts rückgängig gemacht werden kann.

-   
  „Änderungen verwerfen und beenden“ entfernen

-   
  Verlaufs-/Protokollierungsfunktionen harmonisieren

- Geschichte: 2006 Gramps Version 2.1.2. [Neues Dialogfeld „Rückgängig-Verlauf“ hinzugefügt. Sie können alle vorgenommenen Änderungen anzeigen und den Punkt auswählen, bis zu dem Sie rückgängig machen (oder wiederherstellen) möchten – Alex](https://sourceforge.net/p/gramps/mailman/message/11952810/)[1](https://github.com/gramps-project/gramps/blob/master/gramps/gui/undohistory.py)

### Dialogfeld Rückgängig-Verlauf

![[_media/UndoHistory-dialog-example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Dialogfeld „Rückgängig-Verlauf“ – Beispiel]] Zeigt eine Liste der bisher vorgenommenen Änderungen in der Liste „Rückgängig-Verlauf“ an, in der du einzelne Vorgänge machen, oder kannst.

Wenn du auf die Schaltfläche klickst, wird das „Möchtest du den Rückgängig-Verlauf wirklich löschen?“ angezeigt.

Die Liste zeigt die „ursprüngliche Zeit“ und die „Aktion“ jedes Vorgangs an.

Die Liste im Dialogfeld „Rückgängig-Verlauf“ umfasst alle Objektänderungen.

Der Rückgängig-Verlauf bietet eine Listenansicht mit allen Bearbeitungsschritten, die rückgängig gemacht oder wiederhergestellt werden können. Durch Auswahl einer Zeile in der Liste wird der entsprechende Schritt im Bearbeitungsverlauf rückgängig gemacht oder wiederhergestellt.

## Hauptmenüs

![[_media/Menubar-MainMenuOverview-NoFamilyTree-Loaded-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menüleiste - Hauptmenü Übersicht - Kein Stammbaum geladen]]

Die Menüleiste zeigt die verfügbaren Gramps-Menüoptionen an.

Bevor ein Stammbaum geladen wird, sind stark verkürzte Menüs verfügbar. Sie ermöglichen die Verwaltung von Stammbäumen, das Beenden von Gramps, das Bearbeiten von anwendungsweiten Einstellungen, das Aktivieren und Deaktivieren von Abschnitten der grafischen Benutzeroberfläche (GUI) sowie Hilfeoptionen.

{{-}} ![[_media/Menubar-MainMenuOverview-FamilyTree-Loaded-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menüleiste - Hauptmenü Übersicht - Stammbaum geladen]] Nachdem ein Stammbaum geladen wurde, haben die Menüs , , und immer die gleichen Optionen. Die Verfügbarkeit von Optionen in den anderen Menüs ist jedoch kontextabhängig. Die Optionen in den Menüs , und ändern sich in Abhängigkeit von der aktiven Kategorie, und einige Menüpunkte erscheinen 'abgeblendet', wenn die Auswahlobjekte in der Ansicht die Aktion nicht zulassen. {{-}} ![[_media/Menubar-MainMenuOverview-FamilyTree-Loaded-Active-Go-Windows-menus-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menüleiste - Hauptmenü Übersicht - Stammbaum geladen mit den verwendeten Menüeinträgen &quot;Gehe zu&quot; und &quot;Fenster&quot;]]

Die Menüs und sind speziell für die Navigation in jeder Ansicht konzipiert.

Ein -Menü erscheint, wenn es irgendwelche hervorgebrachte Fenster oder Dialoge gibt, die aufgelistet werden sollen. {{-}} Verfügbare [Tastenkombinationen](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings) werden in den Menüs der Menüleiste neben dem Namen der Funktion angezeigt.

Du kannst auch jedes der Hauptmenüs über die [Zugriffstastenkombinationen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Tastenkürzel_Referenz#Zugriff_auf_Tastenkombinationen) der -Taste und der ersten Taste links neben jeder Menüoption auswählen, z. B.: Durch gleichzeitiges Drücken der Tasten  + wird das Menü angezeigt.

### 

![[_media/Menubar-FamilyTrees-overview-FamilyTree-Loaded-example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menüleiste - "Stammbäume" - Übersicht Beispiel]]

- \- Öffnet das [Stammbaumverwaltungsfenster](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Stammbäume_Verwalten#Stammbaumverwaltungsfenster)

- \- eine Verknüpfung zum Öffnen eines kürzlich bearbeiteten Stammbaums (Werkzeugleiste: [<big>▼ </big>Verbinden mit einer bestehenden Datenbank](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Navigation#.E2.96.BC_Verbinden_mit_einer_bestehenden_Datenbank))

- \- den aktuellen Baum sichern und schließen

<hr>

- \- Bringt Daten aus anderen [Formaten](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Stammbäume_Verwalten#Daten_importieren) ein.  
  *Erstelle vor dem Import eine Sicherung! Es gibt [Importeinstellungen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Einstellungen#Import), um importierte Daten mit zeitgestempelter [Markierung](wiki:De:Gramps_Glossar#Markierung) und/oder [Quellattributen](wiki:De:Gramps_Glossar#Quelle) zu markieren. Diese Optionen verlangsamen den Importvorgang erheblich, sind aber für die anschließende Datenbereinigung hilfreich.*

- \- [Daten exportieren](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Stammbäume_Verwalten#Daten_exportieren) ermöglicht dir einen beliebigen Teil deines Gramps-Stammbaums mit anderen Forschern zu teilen und deine Daten auf einen anderen Computer zu übertragen.

<hr>

- \- Das Menü wird in den meisten Ansichten nur angezeigt, wenn die angezeigten Daten exportiert werden können. Gramps exportiert Daten auf dem Bildschirm nach deiner Wahl: **CSV** oder **Open Document** Tabellenformat.

<hr>

- \- Ermöglicht das Erstellen einer [vollständigen Gramps-XML-Sicherung](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Stammbäume_Verwalten#Einen_Stammbaum_sichern) Deines aktuell geöffneten Stammbaums. Beachte, [dass einige Konfigurations- und Medienelemente in XML-Sicherungen weggelassen werden](wiki:Template:Backup_Omissions/de).

<hr>

- \- Wenn du deinen Stammbaum wieder so haben willst, wie er war, als du ihn zu Beginn der Sitzung geöffnet hast. (Das ist wie in anderen Programmen, wenn du ohne zu speichern beendest.) Du bekommst dann die Warnmeldung

- \- Beendet deine Gramps-Sitzung und startet möglicherweise deine [automatische Sicherung](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Fehler_und_Warnung_Referenz#Automatische_Sicherung...), falls diese eingerichtet ist.

{{-}}

### 

![[_media/Menubar-Add-a-new-object-overview-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menüleiste - "Hinzufügen" (ein neues Objekt) Übersicht]]

- \- ein neues [Objekt](wiki:De:Gramps_Glossar#primäres_Objekt)  
  siehe auch [Tastenkürzel](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Tastenkürzel_Referenz).

<hr>

- \- fügt eine [Person](wiki:De:Gramps_Glossar#Person) hinzu *([prim. Obj.](wiki:De:Gramps_Glossar#primäres_Objekt))*

<hr>

- \- fügt eine [Familie](wiki:De:Gramps_Glossar#Familie) hinzu *([prim. Obj.](wiki:De:Gramps_Glossar#primäres_Objekt))* - Öffnet den

<hr>

- \- fügt ein [Ereignis](wiki:De:Gramps_Glossar#Ereignis) hinzu *([prim. Obj.](wiki:De:Gramps_Glossar#primäres_Objekt))*

<hr>

- \- fügt einen [Ort](wiki:De:Gramps_Glossar#Ort) hinzu *([prim. Obj.](wiki:De:Gramps_Glossar#primäres_Objekt))*

- \- fügt eine [Quelle](wiki:De:Gramps_Glossar#Quelle) hinzu *([prim. Obj.](wiki:De:Gramps_Glossar#primäres_Objekt))*

- \- fügt eine [Fundstelle](wiki:De:Gramps_Glossar#Fundstelle) hinzu *([prim. Obj.](wiki:De:Gramps_Glossar#primäres_Objekt))*

- \- fügt einen [Aufbewahrungsort](wiki:De:Gramps_Glossar#Aufbewahrungsort) hinzu *([prim. Obj.](wiki:De:Gramps_Glossar#primäres_Objekt))*

- \- fügt ein [Medium](wiki:De:Gramps_Glossar#Medien) hinzu *([prim. Obj.](wiki:De:Gramps_Glossar#primäres_Objekt))*

- \- fügt eine [Notiz](wiki:De:Gramps_Glossar#Notiz) hinzu *([prim. Obj.](wiki:De:Gramps_Glossar#primäres_Objekt))*

<hr>

{{-}}

### 

Wenn kein Stammbaum geladen ist, werden nur die Einträge **Erweiterungsverwaltung...** und „Einstellungen...“ angezeigt. ![[_media/Menubar-Edit-defaults-family-tree-loaded-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menüleiste - Bearbeiten Übersicht - Standart]] ![[_media/MenuEdit-SetHomePerson-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menüleiste – Bearbeiten – mit geladenem Stammbaum]]

- \- Die letzte Änderung, die du vorgenommen hast. Siehe [Using Undo History](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Navigation#Verwendung_des_R.C3.BCckg.C3.A4ngig-Verlaufs)

- \- Die letzte Rückgängig-Aktion rückgängig machen. Siehe [Verwendung des Verlaufs zum Rückgängigmachen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Navigation#Verwendung_des_R.C3.BCckg.C3.A4ngig-Verlaufs)

- \- Öffne das Dialogfeld

<hr>

Hier werden zusätzliche Menüoptionen angezeigt, die von der Kategorieansicht abhängen.

- \- Siehe [Markieren](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Filter#Markieren)

<hr>

- \- Das Zwischenablagewerkzeug bietet einen temporären Notizblock zum Speichern von Datenbankeinträgen zur einfachen Wiederverwendung.

<hr>

- \- Verwaltung von Erweiterungen von Drittanbietern

- \- Zeigt das Dialogfeld an. Dies ermöglicht dir die meisten Einstellungen in Gramps zu ändern.

- Hier werden zusätzliche Menüoptionen angezeigt, die von der Kategorieansicht abhängen.

{{-}}

### 

![[_media/Menubar-View-overview-example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menüleiste - "Ansicht" - Übersicht Beispiel]]

- \- Ermöglicht das Konfigurieren der aktiven Ansicht. Bietet Optionen zum Ausblenden, Anzeigen und Neuanordnen von Elementen. Dies entspricht einem Klick auf die Schaltfläche ![[_media/Gramps-config.png]] in der [Werkzeugleiste](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Hauptfenster#Werkzeugleiste).

- \- Der Navigator ist ein Seitenleistencontainer für die Symbole der Navigatorkategorie. Bei Auswahl (Standard) wird die Seitenleiste links von der aktiven Ansicht angezeigt. Durch Deaktivieren wird die Navigator-Seitenleiste ausgeblendet. Wenn nicht alle Kategoriesymbole in den verfügbaren vertikalen Bereich passen, wird rechts neben der Seitenleiste eine ausgeblendete Bildlaufleiste erstellt, die beim Überrollen (Bewegen) angezeigt wird.  
  Textbeschriftungen für die Symbole können über eine Option auf der Registerkarte [Anzeige](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Einstellungen#Anzeige) der Einstellungen ausgeblendet werden. [Anzeigemodi](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Hauptfenster#Navigationsmodus_.C3.A4ndern) können aus dem Einblendmenü unten in der Navigator-Seitenleiste ausgewählt werden.

- \- Anzeigen (oder Ausblenden) eines Containers mit geteiltem Bildschirm für (häufig verwendete) Aktionssymbole über der Kategorieansicht. Die Auswahl der Aktionssymbole variiert je nach Kategorieansicht.  
  Ein [Zusatzmodul eines Drittanbieters](wiki:Third-party_Addons) kann installiert werden, um die Einstellungen durch eine Registerkarte [Thema](wiki:Addon:ThemePreferences) zu ergänzen, die eine Option zum Anzeigen von Textbeschriftungen für jede Symbolleistenschaltfläche bietet.

- \- Ein- (oder Ausblenden) eines geteilten Bildschirmcontainers für Gramplets rechts neben der Kategorieansicht.

- \- Ein- (oder Ausblenden) eines geteilten Bildschirmcontainers für Gramplets am unteren Rand des Fensters direkt über der Statusleiste.

- \- Erweitert das Fenster, um den gesamten verfügbaren Bildschirmbereich zu nutzen, während die Steuerelemente zum Ziehen und Ändern der Größe des Fensters deaktiviert werden. Durch Deaktivieren wird die vorherige Größe wiederhergestellt, während die Steuerelemente zum Ziehen und Ändern der Größe des Fensters wieder aktiviert werden.

<hr width=25%>

- Abhängig davon, welche Ansicht aktiv ist, werden hier andere Optionsmenüelemente angezeigt, mit denen du ändern kannst, wie die Ansicht Daten organisiert.

{{-}}

### 

![[_media/Menubar-GoOverview-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menüleiste - Gehe zu Übersicht]]

- \- Navigiert durch die Auswahl der aktuellen Ansicht rückwärts zum *vorherigen* Element in deinem [Navigationsverlauf](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Navigation#Verwendung_verlaufbasierender_Navigation)

- \- Navigiert durch die Auswahl der aktuellen Ansicht vorwärts zum nächsten Element in deinem [Navigationsverlauf](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Navigation#Verwendung_verlaufbasierender_Navigation)

<hr>

- \- Navigiert im Fokus der [aktiven Person](wiki:De:Gramps_Glossar#aktive_Person) zu der Person, die als [Hauptperson](wiki:De:Gramps_Glossar#Hauptperson) [festgelegt](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Einstellungen#Hauptperson_setzen) wurde

<hr>

- Dynamische Liste der letzten 10 ausgewählten Datensätze (Personen, Familien usw.). Die Liste hängt von der angezeigten Kategorieansicht ab.

{{-}}

### 

![[_media/Menubar-BookmarksOverview-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menüleiste - Lesezeichen Übersicht]]

- \- Erstellt ein Lesezeichen aus dem aktuell ausgewählten Element, z.B.: Person, Familie usw..

- \- Öffnet das Fenster .

<hr>

- ... - *Dynamischer Abschnitt, in dem die Lesezeichen angezeigt werden.*

{{-}}

### 

![[_media/Menubar-ReportsOverview-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menüleiste - Berichte Übersicht]]

- \- Mit dem [Buchbericht](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte_-_Teil_3#B.C3.BCcher) kannst du ein benutzerdefiniertes Genealogiebuch erstellen, das eine Sammlung von Gramps-Text- und Grafikberichten in einem einzigen Dokument (z.B. Einem Buch) enthält.

<hr>

- \-

  - 

  - 

  - 

- \-

  - 

  - 

  - 

  - 

  - 

  - 

  - 

- \-

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

<!-- -->

- \-

  - 

  - 

{{-}}

### 

![[_media/MenuOverview-Tools-default-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "" Menüleiste - Werkzeuge Übersicht]]

- \-

  - 

  - \-

<hr>

- \- Das Menü wird nur im Entwicklermodus angezeigt. Siehe Abschnitt [Fehlersuche](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Werkzeuge#Fehlersuche).

  - 

  - 

  - 

  - 

  - \- verschoben nach [Gramplets](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Gramplets#Python-Auswertung)

  - \- verschoben nach [Gramplets](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Gramplets#Uncollected_Objects)

<hr>

- \-

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

- \-

  - 

  - 

  - 

  - 

  - 

- - 

  - 

  - 

  - 

  - 

  - 

{{-}}

### 

![[_media/Menubar-Windows-menu-overview-example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menüleiste - "Fenster" Menü - Übersicht Beispiel]]

- \- Dieses Menü bietet schnellen Zugriff auf geöffnete Fenster, an denen du arbeitest.

{{-}}

### 

![[_media/Menubar-Help-overview-example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menüleiste - "Hilfe" - Übersicht Beispiel]]

- \- Direkter Link zum Online-Gramps-Benutzerhandbuch, das du gerade anschaust. Ja, du benötigst eine Internetverbindung, um das Gramps-Benutzerhandbuch zu lesen.

- \- Ein Link zu den [häufig gestellten Fragen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_FAQ) zu Gramps.

- \- Ein Link zur [Tastenkürzel Referenz](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Tastenkürzel_Referenz) für Gramps.

- \- Zeigt einen Dialog mit einem zufälligen Hinweis zur Verwendung der Gramps-Software an.

- \- In diesem Menü kannst du die integrierten Module sowie alle von dir installierten [Zusatzmodule von Drittanbietern](wiki:6.0_Addons) verwalten.

<hr>

- \- Dieses Element öffnet deinen Webbrowser und stellt eine Verbindung zur Gramps-Projektwebsite her.

- \- Dieser Eintrag öffnet deinen Webbrowser für die Seite der Gramps-Mailingliste. Auf dieser Seite kannst du die Mailinglistenarchive durchsuchen und dich der Mailingliste der Gramps-Benutzer anschließen, um deine Erfahrungen mit anderen Gramps-Benutzern zu teilen.

- \- Wähle dieses Element aus, um einen [Fehlerbericht](wiki:Using_the_bug_tracker) im Gramps-Fehlerverfolgungssystem einzureichen. (Dazu musst du über ein registriertes Konto im Gramps-Fehlerberichterstattungssystem verfügen.) (Denke daran, dass Gramps ein lebendiges Projekt ist. Wir möchten alle auftretenden Probleme kennen, damit wir daran arbeiten können, sie für dich zu lösen, und alle anderen profitieren davon.)

- \- Ein Link zum [Installieren von Zusatzmodulen von Drittanbietern in Gramps.](wiki:6.0_Addons)

<hr>

- \- Dieses Element zeigt einen Dialog mit allgemeinen Informationen zur von dir ausgeführten Gramps-Version an.

{{-}}

## Werkzeugleiste

![[_media/ToolbarIcon-OpenTheToolsDialog-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Tipp für die Schaltfläche Werkzeuge in der Symbolleiste der Kategorie Dashboard]] Die [Werkzeugleiste](wiki:De:Gramps_Glossar#Werkzeugleiste) ist ein horizontaler Satz von Schaltflächen, die sich direkt unter der Menüleiste befinden. Sie ermöglicht dir den Zugriff auf die am häufigsten verwendeten Funktionen von Gramps.

- Die Auswahl der Werkzeugleisteschaltflächen ist "kontextabhängig" - die angezeigten Symbole hängen davon ab, welche Kategorie [Ansicht](wiki:De:Gramps_Glossar#Ansicht) und welcher [Ansichtsmodus](wiki:De:Gramps_Glossar#Ansichtsmodus) aktiv ist
- Textbeschriftungen werden unter den Schaltflächen der Werkzeugleiste angezeigt.
- Wenn du den Mauszeiger über eine Schaltfläche in der Werkzeugleiste bewegst, wird ein Hinweis auf ihre Funktion angezeigt.
- Die Symbolleiste kann über die Option im Menü ein- oder ausgeblendet werden.

{{-}}

### Gemeinsame Schaltflächen in der Werkzeugleiste

#### ![[_media/Gramps.png]] Datenbanken verwalten

![[_media/FamilyTrees-ManageDatabases-icon-toolbar-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure\|{{#expr:{{#var:figure}}+1}}}} Stammbäume (Datenbanken verwalten) - Symbol und Funktionshinweis in der Symbolleiste]] Die ![[_media/16x16-gramps-pedigree.png]] Schaltfläche ist die gleiche wie die Menüoption Der daraus resultierende Dialog ermöglicht das Umschalten zwischen den Bäumen (genealogischen Datenbanken), {{-}}

#### <big>▼ </big>Verbinden mit einer bestehenden Datenbank

![Abb. {{#var:chapter}}.{{#vardefineecho:figure\|{{#expr:{{#var:figure}}+1}}}} Schaltfläche "Mit einer bestehenden Datenbank verbinden" in der Werkzeugleiste ](ConnectToARecentDatabase-icon-toolbar-60-de.png "Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Schaltfläche "Mit einer bestehenden Datenbank verbinden" in der Werkzeugleiste ") Diese <big>▼ </big>Schaltfläche öffnet das Auswahlliste in der Werkzeugleiste.

Siehe: Abschnitt [<big>▼ </big> Mit einer aktuellen Datenbank verbinden](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Stammbäume_Verwalten#Mit_einer_aktuellen_Datenbank_verbinden). {{-}}

#### ![[_media/Gramps_Go-Previous48x48_win.png]] Zum vorherigen Objekt in der Historie wechseln

Die ![[_media/Gramps_Go-Previous48x48_win.png]] Schaltfläche in der Werkzeugleiste ist eine Alternative zur Menüoption oder zum Drücken der [Tastenkürzel](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Tastenkürzel_Referenz#Allgemeine_K.C3.BCrzel) *Zurück*. Sie nutzt die [historienbasierte Navigation](#Verwendung_verlaufbasierender_Navigation), um den Fokus des aktiven Objekts auf das zuvor ausgewählte Objekt in dieser Kategorie zu verschieben.

#### ![[_media/Go-next48x48_win.png]] Zum nächsten Objekt in der Historie wechseln

Die Schaltfläche ![[_media/Go-next48x48_win.png]] in der Werkzeugleiste ist eine Alternative zur Menüoption oder zum Drücken des Vor-[Tastenkürzel](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Tastenkürzel_Referenz#Allgemeine_K.C3.BCrzel). Sie verwendet die [historienbasierte Navigation](#Verwendung_verlaufbasierender_Navigation), um den Fokus des aktiven Objekts wiederherzustellen, der mit der Funktion verschoben wurde.

Diese Schaltfläche ist nur nach Verwendung der Funktion verfügbar.

#### ![[_media/Gramps_Go-Home48x48_win.png]] Springe zur Hauptperson

Die Gramps ![[_media/Gramps_Go-Home48x48_win.png]] Schaltfläche in der Werkzeugleiste ist eine Alternative zum Menüpunkt oder zum Drücken des Home-[Tastenkürzel](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Tastenkürzel_Referenz#Allgemeine_K.C3.BCrzel). Sie verschiebt den Fokus der [Aktiven Person](wiki:De:Gramps_Glossar#aktive_Person) auf die [Hauptperson](wiki:De:Gramps_Glossar#Hauptperson).

Diese Schaltfläche ist nur funktionsfähig, wenn die Hauptperson eingestellt wurde.

#### ![[_media/Gramps_Add48x48_win.png]] Neues ... hinzufügen

Die Schaltfläche in der Werkzeugleiste ist eine Alternative zum Menüpunkt oder des [Tastenkürzel](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Tastenkürzel_Referenz#Allgemeine_K.C3.BCrzel) *Hinzufügen*. Sie öffnet einen leeren Objekteditor, der der Objektkategorie der aktuellen Ansicht entspricht.

####  Das ausgewählte ... bearbeiten

Die Schaltfläche ist eine Alternative zum Menüpunkt oder zum Drücken des [Tastenkürzel](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Tastenkürzel_Referenz#Allgemeine_K.C3.BCrzel) Bearbeiten. Sie öffnet einen Objekteditor für jedes ausgewählte Objekt in der Kategorieansicht.

#### ![[_media/Gramps_Remove48x48_win.png]] Gewählte ... löschen

Die Schaltfläche in der Werkzeugleiste ist eine Alternative zur Menüoption oder zum Drücken der [Tastenkürzel](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Tastenkürzel_Referenz#Allgemeine_K.C3.BCrzel) *Löschen*. Sie öffnet einen Bestätigungsdialog zum Löschen.

Das Element, das gelöscht werden soll, wird identifiziert. Wenn mehrere Elemente ausgewählt wurden, erscheint für jedes ein Dialogfeld. Ein Kontrollkästchen bietet die Option "Diese Antwort für den Rest der Einträge verwenden".

#### ![[_media/Gramps_Merge48x48_win.png]] Gewählte ... zusammenfassen

Diese Schaltfläche in der Symbolleiste ist eine Alternative zum Menüpunkt Sie öffnet den [Zusammenführen-Dialog](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Daten_eingeben_und_bearbeiten:_Ausführlich_-_Teil_3#Datens.C3.A4tze_zusammenf.C3.BChren) für diese bestimmte Kategorie von Datensätzen.

Die Schaltfläche Zusammenführen kann nur dann erfolgreich verwendet werden, wenn zwei (und nur 2) Datensätze in der Ansicht ausgewählt sind.

#### ![[_media/gramps-tag.png]] Ausgewählte Zeilen markieren

Diese Schaltfläche in der Werkzeugleiste ist eine Alternative zum Untermenü .

Die ![[_media/16x16-gramps-tag.png]] Schaltfläche öffnet ein Aufklappmenü mit den folgenden [Markierungsoptionen](wiki:De:Gramps_Glossar#Markierung):

- [Neue Markierung...](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Filter#Neuer_Markierungsdialog)
- [Markierungen organisieren...](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Filter#Markierungen_organisieren_Fenster)

Es folgt eine Liste der aktuell verfügbaren Markierungen, die auf die ausgewählten Objekte in der Ansicht angewendet werden können.

[Markierungen werden verwendet](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Filter#Verwendung_von_Markierungen), um Zeilen in Listenansichten farblich zu kodieren, Markierungsfelder in einigen Diagrammen und dauerhafte Markierungen zum Filtern und Organisieren.

#### ![[_media/Gramps_Clipboard48x48_win.png]] Öffnet den Zwischenablagedialog

![[_media/Clipboard-dialog-example-context-menu-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Zwischenablage - Dialog - Anzeigen (Rechtsklick) Kontextmenü]] Diese Schaltfläche in der Werkzeugleiste ist eine Alternative zum Menüpunkt oder zum Drücken der [Tastenkürzel](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Tastenkürzel_Referenz#Allgemeine_K.C3.BCrzel) *Zwischenablage*. Sie öffnet den [Zwischenablage](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Navigation#Die_Zwischenablage_verwenden)-Dialog, ohne das ausgewählte Objekt zu seiner Sammlung hinzuzufügen. {{-}}

#### ![[_media/Gramps-config.png]] Die aktive Ansicht konfigurieren

Diese Schaltfläche in der Werkzeugleiste ist eine Alternative zur Auswahl des Menüpunkts oder zum Drücken der [Tastenkürzel](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Tastenkürzel_Referenz#Allgemeine_K.C3.BCrzel) Aktive Ansicht konfigurieren.

Die meisten Kategorieansichten haben ein ⚙ Konfigurierbare Optionen. Wenn Sie auf diese Schaltfläche klicken, öffnet sich der Dialog mit den Steuerelementen für die Anpassung dieser Optionen.

Diese Option öffnet ein Dialogfeld mit Auswahlmöglichkeiten für die Anzeige von Datensätzen in der Ansicht. (Das Dialogfeld enthält auch Registerkarten für alle [Gramplets, die konfigurierbare Optionen haben](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Gramplets#.E2.9A.99_Konfigurierbare_Optionen_2), die in der Ansicht aktiv sind).

#### ![[_media/Gramps-reports.png]] Öffnet den Berichtsdialog

![[_media/ReportSelection-dialog-default-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Berichtsauswahl - Dialog]] Dies ist eine dauerhafte Alternative zur Verwendung der Untermenüs .

Durch die Darstellung der verfügbaren Berichte in einem schwebenden Dialogfeld wird Raum für die Beschreibung der einzelnen Berichte, ihres Status und der Informationen für die Entwickler geschaffen. Der Dialog ermöglicht auch eine strukturiertere Erkundung der Berichte. {{-}}

#### ![[_media/Gramps-tools.png]] Öffnet den Werkzeugdialog

![[_media/ToolSelection-dialog-example-with-debug-menu-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Werkzeugauswahl - Dialog]] Dies ist eine dauerhafte Alternative zur Verwendung der Untermenüs .

Indem die verfügbaren Werkzeuge in einem schwebenden Dialogfeld angezeigt werden, steht mehr Raum für die Beschreibung der einzelnen Werkzeuge, ihren Status und die Informationen für die Entwickler zur Verfügung. Der Dialog ermöglicht auch eine strukturiertere Erkundung der Werkzeuge.

{{-}}

#### ![[_media/Gramps-addon.png]] Erweiterungsverwaltung öffnen

![[_media/AddonManager-addons-listing-60-de.png|Right|thumb|550px|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} <strong>Erweiterungsverwaltung</strong> Dialog Beispiel]]

- \- Die \[\[man label\|Erweiterungsverwaltung}} bietet dir die Möglichkeit, herauszufinden, welche Erweiterung deinepersönlichen Arbeitsabläufe verbessern können.

{{-}}

#### ![[_media/Gramps-preferences.png]] Einstellungen öffnen

![[_media/EditPreferences-Data-tab-default-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menü: "Bearbeiten -&gt; Einstellungen..." Beispiel]]

- \- Die meisten Einstellungen, die sich auf das gesamte Gramps-Programm auswirken, werden im Dialogfeld konfiguriert.

{{-}}

[N](wiki:Category:De:Dokumentation)
