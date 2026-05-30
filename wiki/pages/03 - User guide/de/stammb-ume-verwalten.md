---
title: De:Gramps 6.0 Wiki Handbuch - Stammbäume Verwalten
categories:
- De:Dokumentation
- Stub
managed: false
source: wiki-scrape
wiki_revid: 130604
wiki_fetched_at: '2026-05-30T18:10:00Z'
lang: de
---

{{#vardefine:chapter\|5}} {{#vardefine:figure\|0}} Eine detaillierte Untersuchung der Wartung und des Verschiebens von Daten (in Massenoperationen) in Stambaumdatenbanken.

In diesem Kapitel wird die Verwaltung deiner Familienstammbäume (Datenbanken) sowie die Optionen für die gemeinsame Nutzung deiner Daten mit anderen Genealogen erläutert. Dazu gehören das Erstellen von leeren Stammbäumen, das Konvertieren alter Datenbankformate, das Erstellen von Sicherungsarchiven, das Umbenennen von Stammbäumen, das Löschen von Stammbäumen sowie das Importieren und Exportieren von Baumdaten.

## Neuen Stammbaum beginnen

![[_media/Menubar-FamilyTrees-overview-FamilyTree-Loaded-example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menüleiste - "Stammbäume" - Übersichtsbeispiel]]

Um einen neuen Stammbaum zu beginnen wähle verwalten oder wähle die Schaltfläche aus der Werkzeugleiste oder verwende die [Tastenkombination](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Tastenkürzel_Referenz) .. Dies öffnet das .

Wähle die Schaltfläche und Gramps fügt einen neuen Stammbaumeintrag zur Liste der Stammbäume hinzu. Um seinen Namen vom Standard *`Stammbaum 1`* zu ändern, wähle den Namen und drücke die Schaltfläche gib einen neuen Namen ein.

Um den neuen, leeren Stammbaum zu öffnen, wähle den Stammbaum aus und doppelklicke ihn oder klicke zum Laden auf die Schaltfläche . {{-}}

### Stammbäume verwalten...

![[_media/Menubar-FamilyTrees-overview-FamilyTree-Loaded-example-60-de.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menüleiste - „Stammbäume“ - Beispiel für eine Übersicht]] {{-}}

### Datenbanken verwalten

![[_media/FamilyTrees-ManageDatabases-icon-toolbar-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure\|{{#expr:{{#var:figure}}+1}}}} Datenbanken verwalten - Symbol in der Symbolleiste (wie im Menü )]] {{-}} <span ID="Stammbumverwaltungsfenster"></span>

### Stammbäume(verwaltungs)fenster

Stammbäume nennt Gramps die Datenbankstruktur, die verwendet wird, um genealogische Daten zu speichern und zu organisieren. Du musst einen Stammbaum erstellen, bevor genealogische Daten eingegeben, aus einem [Backup-Archiv wiederhergestellt](wiki:How_to_restore_a_backup) oder [aus einer anderen Software importiert werden](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Stammbäume_Verwalten#Daten_importieren) können.

Stammbäume können umbenannt, in andere Datenbank-Backends konvertiert, repariert oder gelöscht werden. Ein "Fehler" wird hier nicht unkorrigierbar sein. (Der größte potenzielle Fehler, ein versehentliches Löschen, erfordert eine Bestätigung.)

![[_media/:FamilyTreesManager-window-example-60.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Stammbäume" (Verwaltungs)fenster]]

Wenn du auf die Schaltfläche klickst, wird das (Verwaltung\] Fenster geöffnet, das es dir ermöglichen, mit den Stammbäumen zu arbeiten und sie zu verwalten, die sich im spezifischen [Pfadverzeichnis der Gramps Stammbaumdatenbank](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Einstellungen#Stammbaum) befinden.

Im Fenster Stammbäume(verwaltung) kannst du einen neuen Stammbaum erstellen, einen vorhandenen Stammbaum umbenennen, einen Stammbaum löschen oder einen Stammbaum laden oder Informationen über den Stammbaum überprüfen. Alle Namen deiner Stammbäume werden in der Liste angezeigt. Wenn ein Stammbaum geöffnet ist, wird neben dem Namen in der Statusspalte ein Symbol angezeigt. Der Datenbanktyp sowie eine Angabe des Datums und der Uhrzeit, zu der dein Stammbaum zuletzt aufgerufen wurde, werden angezeigt.

- erstellt einen neuen Stammbaum.

- }} zeigt zum ausgewählten Stammbaum an.

- den gewählten Stammbaum, daraufhin wird eine Warnung mit einer endgültigen Bestätigung angezeigt, für dich zum Bestätigen.

- den gewählten existierenden Stammbaum und gib den neuen Namen ein..

- den gewählten existierenden Stammbaum.

- den gewählten Stammbaum. Diese Option ist nur verfügbar, wenn die Datenbank des Baums vom Standard-**Datenbanktyp** *SQLite* abweicht.

- den ausgewählten bestehenden Stammbaum, nur verfügbar, wenn Gramps ein Problem erkennt.

- Option ist nur verfügbar wenn [GNU Revision Control System](http://www.gnu.org/software/rcs/) (RCS) installiert ist.

- verwendet mit Schaltfläche und die Option ist nur verfügbar wenn [GNU Revision Control System](http://www.gnu.org/software/rcs/) (RCS) installiert ist.

- \- öffnet das Standardbrowserfenster mit diesem Abschnitt des Online-Handbuchs.

- \- schließt das Verwaltung Fenster

- öffnet den ausgewählten bestehenden Stammbaum im Arbeitsspeicher und sperrt die Datenbankdatei, damit andere Benutzer keine widersprüchlichen Bearbeitungen vornehmen können.

{{-}}

#### Dialogfeld Datenbankinformationen

![[_media/Database-Information-dialog-example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Dialog "Datenbankinformationen", der beim Drücken der Schaltfläche "Info" im Fenster "Familienstammbäume" angezeigt wird und der Stammbaum ist nicht geladen/geschlossen.]]

Wird angezeigt, wenn du die -Taste im Fenster drückst und der Stammbaum nicht geladen/geschlossen ist.

Die folgenden Informationen werden in der Spalte `Einstellung` zusammen mit dem Ergebnis in der Spalte `Wert` angezeigt:

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

- – Die Art des Backends, das zum Erstellen des Stammbaums verwendet wurde.

- 

- – aktueller Status entweder „True“ oder „False“.

- – Datum und Uhrzeit.

- – Speicherort des Stammbaums.

- – Gramps-XML-Version.

- 

- – Name.

Siehe auch:

- Ähnlich wie der und das

{{-}}

## Einen Stammbaum öffnen

Um einen Stammbaum zu öffnen wähle entweder oder klicke die Schaltfläche in der Werkzeugleiste. Die öffnet sich und du siehst eine Liste aller Gramps bekannten Stammbäume. Ein Symbol wird in der Spalte (sieht aus wie ein geöffneter Ordner) neben jedem aktuell geöffneten Stammbaum angezeigt. Wähle den Baum den du öffnen willst und öffne ihn durch klicken der Schaltfläche. Alternativ kannst du den gewünschten Baum auch doppelt klicken.

### Schaltfläche Stammbaum laden

Wähle im Fenster (Manager) aus der Liste den Baum aus, den du öffnen möchtest, und öffne ihn, indem du auf die Schaltfläche klickst. {{-}}

### <big>▼ </big> Mit einer aktuellen Datenbank verbinden

![[_media/ConnectToARecentDatabase-icon-toolbar-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Mit einer aktuellen Datenbank verbinden - Dropdown-Symbol in der Symbolleiste]]

Um einen kürzlich geöffneten Stammbaum zu öffnen, wähle entweder das Menü oder die Schaltfläche <big>▼ </big> neben der Schaltfläche Symbolleisten Diagramme und wähle den Stammbaum aus der Liste aus. {{-}}

#### Ein aktueller Stammbaum konnte nicht geladen werden. Warnung

![[_media/Could-not-load-a-recent-Family-Tree-warning-60.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Ein aktueller Stammbaum konnte nicht geladen werden. Warnung]]

Wenn der ausgewählte Stammbaum in der Liste nicht verfügbar ist, wird die folgende Warnung angezeigt:

**Ein aktueller Stammbaum konnte nicht geladen werden.**

*Der Stammbaum existiert nicht, da er gelöscht wurde.* {{-}}

### Nur lesen Modus

## Änderungen im Stammbaum speichern

Gramps speichert deine Daten direkt nachdem du sie eingegeben hast. Dies bedeutet zum Beispiel, das jedes mal wenn du klickst während du Gramps verwendest werden deine Daten unverzüglich übernommen und gespeichert. Es gibt kein spezielles "speichern" Kommando.

Du kannst deine Änderungen durch aufrufen von rückgängig machen. Wenn du dieses Kommando wiederholt aufrufst, werden deine letzten Änderungen Stück für Stück rückgängig gemacht. Um mehrere Kommandos am Stück rückgängig zu machen, kannst du den Dialog verwenden, verfügbar über das Menü.

Wenn du deinen Stammbaum wieder so haben willst, wie er war, als du ihn geöffnet hast, wähl das Menü .{{#vardefineecho:figure\|{{#expr:{{#var:figure}}+1}}}} Den Stammbaum "<Stammbaumname>" entfernen? Dialog\]\]

Wähle den Stammbaum aus, der entfernt werden soll, und klicke im Fenster auf die Schaltfläche , und wähle dann im Dialog die Option oder .

{{-}}

## Einen Stammbaum umbenennen

Im Fenster kannst du einen Stammbaum (oder ein Archiv davon) umbenennen, indem du den Stammbaum, den du umbenennen möchtest, auswählst und auf klickst. Du kannst auch auf den Namen in der Liste der Stammbäume klicken.

In beiden Fällen gib einfach den neuen Namen ein damit er gültig wird.

## Einen Stammbaum sichern

Der sicherste Weg deinen Stammbaum zu sichern, ist der Export ohne Einschränkungen und Filter im **Gramps XML** Format (oder als **Gramps Paket**, um Elemente aus der Galerie mit zu sichern) und die resultierende Datei an einem sicheren Ort zu kopieren, bevorzugt in einem anderen Gebäude.

### Sicherungsdialog

![[_media/MakeBackup-GrampsXML-Backup-example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Eine Sicherung erstellen]]

Wähle einfach das Menü.

#### Gramps XML Sicherung Fenster

Das Fenster wird angezeigt.

Du kannst den eingeben in dem die Sicherung manuell gespeichert werden soll, oder über die Schaltfläche das Dialogfeld aufrufen.

Du kannst einen Namen manuell eingeben oder den automatisch generierten Dateinamen verwenden.

Du kannst auswählen, ob du die Medien **Einbeziehen**(Vorgabe) oder **Ausschließen** willst.

Wähle , um den Vorgang zu beenden, oder , um die Sicherung zu starten. Nach Abschluss des Vorgangs wird in der Statusleiste eine Bestätigung angezeigt, wo die Sicherung gespeichert wurde.

{{-}}

- Mit der [Archivierungsfunktion](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Stammbäume_Verwalten#Einen_Stammbaum_archivieren) (siehe nächster Abschnitt) kannst du Schnappschüsse deines Stammbaums speichern. Diese Schnappschüsse können als einfache Backups verwendet werden. Dies ist sehr nützlich, wenn du etwas ausprobieren möchtest, das du später möglicherweise rückgängig machen möchtest. Diese Methode sollte jedoch nicht für Standard-Backups verwendet werden, da sie einen Festplattenabsturz oder die meisten anderen Katastrophen, die einen Computer betreffen können, nicht überlebt.

<!-- -->

- *Für fortgeschrittene Benutzer:* Jede Datenbank wird in einem eigenen Unterverzeichnis unter deinen [Anwenderverzeichnis](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Anwenderverzeichnis) in `~/.gramps` gespeichert. Obwohl eine manuelle Sicherung durch Sichern dieses Verzeichnisses durchgeführt werden kann, wird dies nicht empfohlen. Es wird dringend empfohlen, stattdessen ein Gramps XML-Backup zu verwenden.

### Beim beenden sichern

In der Registerkarte der Voreinstellungen kann Gramps so eingestellt werden, dass eine Sicherung erstellt wird, wenn Gramps beendet wird. Beachte, dass dies nur eine Sicherung für den geöffneten Stammbaum erstellt. Wenn der Baum vor dem Beenden von Gramps geschlossen wird, wird kein Backup erstellt.

Siehe:

- [Einstellungen Stammbaum](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Einstellungen#Verwaltung_der_Datensicherung) im Abschnitt .

### Automatiche Sicherung

Auf der Registerkarte in den Einstellungen kann ein Intervall für die festgelegt werden, in dem geprüft wird, ob sich der Stammbaum in dieser Bearbeitungssitzung geändert hat, und eine Archivierungskopie erstellt wird. Der Countdown beginnt mit dem Start von Gramps oder mit der Änderung der Intervallauswahl. Dieser Auslöser wird verschoben, wenn der Computer angehalten wurde und während des Aufwachens verzögert wird.

Die Intervalle für die automatische Datensicherung können auf 15, 30, 60 Minuten, "alle 12 Stunden" und "jeden Tag" eingestellt werden.

Jede archivierte Sicherung (ohne Medien) wird in dem im angegebenen Ordner gespeichert. Der Dateiname ist nach dem Muster :

- <small>*\<Family Tree name\>*</small>`-yyyy-mm-dd-hh-mm-ss.gramps`

#### Siehe auch

- [Einstellungen Stammbaum](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Einstellungen#Stammbaum)
- [Erweiterte Einstellung des Sicherungsdateinamens](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Einstellungen#Erweiterte_Einstellung_des_Sicherungsdateinamens) - Hier kannst du auch das Namensmuster für den Sicherungsdateinamen definieren.
- [Backup Auslassungen](wiki:Template:Backup_Omissions/de) - Was ist während einer Sicherung nicht enthalten

## Archivieren

A quick and handy option that allows you to your family trees at a point in time to retain a copy before any major changes and be able to return to a known version.

- [Archiving a Family Tree](#Archiving_a_Family_Tree)
- [Extracting a Family Tree Archive](#Extracting_a_Family_Tree_Archive)
- [Removing a Family Tree Archive](#Removing_a_Family_Tree_Archive)

#### Archivierung Voraussetzung

Erfordert, dass [GNU Revision Control System](http://www.gnu.org/software/rcs) (RCS) installiert ist, damit Gramps die Archivierungsfunktion nutzen kann.

{{-}}

### Einen Stammbaum archivieren

![[_media/ManageFamilyTrees-Archive-RevisionComment-example-60.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Einen Stammbaum archivieren Beispiel]]

Du kannst mit der in Gramps verwendeten [GNU Revision Control System](http://www.gnu.org/software/rcs/) oder *RCS* wenn dieses installiert ist einfach Stammbäume archivieren oder mit einem Zeitstempel versehen. Um dies zu ermöglichen, muss das Programm auf deinem Computer installiert sein.

Um ein Archiv zu erstellen:

1.  lade den Stammbaum.
2.  klicke in der Werkzeugleiste auf die Schaltfläche (sie hat das Gramps-Logo und zeigt , wenn man über sie fährt).
3.  klicke auf den Stammbaum, den du gerade geladen hast: die Schaltfläche sollte erscheinen.
4.  klicke auf und du wirst nach einer "Revisionskommentar - Versionsbeschreibung" für dein Archiv gefragt.

Nach dem Archivieren zeigt die Liste der Stammbäume links neben dem originalen Stammbaum ein nach rechts zeigendes Dreieck.

- Klicke auf das Dreieck um, den Archivnamen zu zeigen. (Klicke erneut zum zuklappen der Archivliste).

Archive können , und werden.

### Ein Stammbaumarchiv extrahieren

![[_media/ManageFamilyTrees-Archive-Selected-to-Extract-example-60.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Stammbaum"(Verwaltung) Dialog - Archiv ausgewählt bereit zum "Extrahieren" - Beispiel]]

Um eine Version eines zuvor archivierten Stammbaums in der "Stammbaumverwaltung" abzurufen, markiere das Archiv, das du wiederherstellen möchtest, und klicke auf die Schaltfläche .

{{-}} ![[_media/ManageFamilyTrees-Archive-Extracted-version-selected-example-60.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;Stammbaum&quot; (Verwaltung) Dialog - Archivierte Version extrahiert und ausgewählt - Beispiel]]

Das Archiv wird dann in einem neuen Stammbaum wiederhergestellt und in der *Stammbaumverwaltung* aufgelistet.

Der Stammbaumname basiert auf dem ursprünglichen Namen und dem Archivnamen, z.B.:

*<Name des ursprünglichen Baums>`:`<Name des Archivs>*.

(siehe auch [Einen Stammbaum archivieren](#Einen_Stammbaum_archivieren))

Dies kann eine nützliche Methode zum Aufbewahren eines Archivs sein, da Archive verschwinden, wenn der Ursprungsbaum gelöscht wird. und **sie sind nicht in einen Gramps XML-Export des Stammbaums** integriert. {{-}}

### Ein Stammbaumarchiv entfernen

![[_media/ManageFamilyTrees-Archive-Remove-dialog-example-60.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Dialogfeld „Stammbäume“ (Verwaltung) – Archivierte Version entfernen – Beispiel]]

Um eine archivierte Version zu entfernen, wähle diese aus und klicke dann auf die Schaltfläche , um das Dialogfeld zu öffnen. Dort kannst du entweder auf klicken und das Dialogfeld schließen oder auf die Schaltfläche klicken.

{{-}}

#### Entfernen der <Name des Archivs>-Version von <Name des ursprünglichen Baums> Dialog

*Wenn du diese Version löschst, kannst du sie später nicht mehr extrahieren.*

{{-}}

## Einen Stammbaum entsperren

![[_media/FamilyTreesManager-Dialog-ShowingLocked-Sample-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} (Verwaltung)&quot;Stammbaum&quot; - Dialog - Zeigt gesperrten &quot;Beispiel&quot; Stammbaum]] Gramps ist eine Einzelbenutzer-Datenbankanwendung und identifiziert Baum-Datenbankdateien als beschäftigt mit einer ![[_media/22x22-gramps-lock.png]]'Sperre', wenn sie verwendet werden. Wenn Gramps einen Baum öffnet, wird eine `Sperrdatei` (die den Benutzernamen und die Domäne auflistet) im Unterordner des Baums im Ordner `grampsdb` des [Anwenderverzeichnisses](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Anwenderverzeichnis) abgelegt. Gramps weigert sich, dir (oder irgendjemanden anderen) diesen Baum gleichzeitig öffnen zu lassen. Eine zweite Instanz von Gramps kann einen anderen Stammbaum öffnen, aber jeder bereits geöffnete Baum wird mit dem Schlosssymbol in der Spalte Status des Dialogfelds Stammbäume verwalten angezeigt. Durch das Schließen des Baums in der ersten Kopie von Gramps wird die Sperrdatei gelöscht und der Baum kann in der zweiten Instanz geöffnet werden.

Wenn du denselben Stammbaum in zwei Fällen von Gramps gleichzeitig öffnen *könntest*, würden deine Daten wahrscheinlich beschädigt, wenn die beiden die Arbeit des anderen überschreiben.

### Die Sperre für die Datenbank "Stammbaumname" aufheben? Dialog

![[_media/ErrorParsingArguments-dialog-DatabaseIsLocked-example-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Fehler bei der Syntaxanalyse von Argumenten - Dialog - Datenbank ist gesperrt Beispiel]] In dem unwahrscheinlichen Fall, dass Gramps abstürzt, bleibt der Stammbaum gesperrt (angezeigt durch ein ![[_media/22x22-gramps-lock.png]]Schlosssymbol in der Spalte neben dem Namen des Stammbaums).

So entsperrst du den Stammbaum während des Startvorgangs

- Wenn in den [Stammbaumeinstellungen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Einstellungen#Stammbaum) festgelegt wurde, dass beim Start automatisch ein Baum geöffnet wird, wird das Dialogfeld **Fehler beim Analysieren von Argumenten** angezeigt, in dem darauf hingewiesen wird, dass die **Datenbank gesperrt** ist. Klicke auf die Schaltfläche und wähle im Menü die Option .
- Andernfalls wird die automatisch angezeigt, wenn Gramps gestartet wird.

{{-}} ![[_media/Break-the-lock-on-the-database-Dialog-example-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Die Sperre für die &quot;Beispiel&quot; -Datenbank aufheben? - Dialog - Beispiel]]Wähle den gesperrten Stammbaum und klicke dann auf die Schaltfläche . Die **Sperre für die Datenbank '\[Stammbaumname\]' aufheben?** Dialog wird angezeigt.

Klicke auf die Schaltfläche , und im Fenster sollte angezeigt werden, dass das Schlosssymbol nicht mehr vorhanden ist.

Wähle den zuvor gesperrten Stammbaum und klicke dann auf die Schaltfläche , um deine Arbeit fortzusetzen. {{-}}

### Die Datenbank ist gesperrt Dialog

![[_media/TheDatabaseIsLocked-dialog-example-52.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Die Datenbank ist gesperrt - Dialog - Verwende die Option --force unlock - Beispiel]]

Wenn du die Meldung erhältst, verwende die [Kommandozeilenoption --force unlock](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Stammbäume_Verwalten#Kommandozeile:Entsperren_erzwingen_Option), wenn du sicher bist, dass die Datenbank nicht benutzt wird.

#### Kommandozeile:Entsperren erzwingen Option

- [Kommandozeilenoption --force unlock](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Kommandozeilen_Referenz#Entsperren_erzwingen_Option) - Alternativ kannst du versuchen, einen Absturz, der den Stammbaum (die Datenbank) gesperrt lässt, über die Kommandozeile zu beheben.

{{-}}

## Einen beschädigten Stammbaum reparieren

![[_media/FamilyTreesManager-Dialog-ShowingRedErrorStatusIcon-Sample-50.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Stammbäume (Verwaltung) - Dialogfeld - Zeigt das rote Fehlerstatussymbol für den Stammbaum "Beispiel" an]]

Wenn dein Stammbaum in irgendeiner Weise beschädigt wurde, zeigt die Gramps-Stammbaumverwaltung ein rotes Fehlersymbol in der Spalte.

Um Gramps mitzuteilen, das es versuchen soll, den Schaden zu reparieren, wähle den Baum und klicke auf die Schaltfläche.

Gramps wird versuchen den Stammbaum aus den Sicherungsdateien, die automatisch beim Beenden erstellt werden, wieder herzustellen.

Siehe auch:

- [Defekten Stammbaum wiederherstellen](wiki:De:Defekten_Stammbaum_wiederherstellen) gilt für BSDDB nicht SQLite

{{-}}

## Konvertieren eines BSDDB-Stammbaums in SQLite

![[_media/ManageFamilyTrees-Convert-the-database-dialog-example-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} <strong>Die Datenbank 'Stammbaumname' konvertieren?</strong> Dialog mit <em>Stammbäumen (Verwaltung</em> - Dialog im Hintergrund]]

Wenn du einen älteren alten **Datenbanktyp** im [BSDDB](wiki:De:Gramps_Glossar#bsddb)-Format für einen deiner Stammbäume im Dialogfeld *Stammbäume (Verwaltung)* - angezeigt bekommst, wird bei Auswahl eines Stammbaums im Dialogfeld "Stammbäume (Verwaltung) -" die Schaltfläche als verfügbar angezeigt.

Wenn du fertig bist, klicke auf die Schaltfläche und dann wird das Dialogfeld mit der Meldung **Möchten Sie diesen Stammbaum in eine SQLite-Datenbank konvertieren?** angezeigt. Du kannst zum Beenden oder zum Starten des Vorgangs auswählen. Nach Abschluss wird im *Stammbäume (Verwalten)* - Dialog ein neuer Eintrag für die konvertierte Kopie deines Stammbaums aber mit dem *Datenbanktyp* SQLite angezeigt. Du solltest den konvertierten Stammbaum öffnen und sichern.

Du kannst dann den ursprünglichen BSDDB-Stammbaum mit dem Wort **ALT** umbenennen oder ihn löschen, um Verwirrung zu vermeiden. Anschließend kannst du die neue SQLite-Datenbank umbenennen.

{{-}}

## Dialogfeld Stammbaum importieren

![[_media/ImportFamilyTree-dialog-Select-file-type-default-list-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} IStammbaum importieren – Dialogfeld – mit Standard-Dropdown-Liste „Dateityp auswählen:“ angezeigt]]

Mit dem Importieren kannst du Daten aus anderen Genealogieprogrammen in einen Gramps-Stammbaum übertragen. Gramps enthält einen Kernsatz von Import-Plugins, die automatisch auf der Grundlage der entsprechenden Dateierweiterung ausgewählt werden. Du kannst auch zusätzliche „Importer“ [Erweiterungen von Drittanbietern](wiki:Third-party_Addons) installieren, und die Automatisierung erkennt dann die neuen Dateiendungen.

Im Dialogfeld kannst du über das Dropdown-Menü aus den folgenden unterstützten Importdateiformaten auswählen:

- **Automatisch erkannt** *(Standard)*- Diese Automatisierungsoption kann außer Kraft gesetzt werden. Dies ist nützlich, wenn Formate aktualisiert werden und die Kern-Plugins dadurch veraltet sind.
- [Tabellenkalkulation mit durch Kommata getrennten Werten (CSV)](#Gramps_CSV_Import) (`.csv` Dateierweiterung)
- [GEDCOM](#GEDCOM_Import) (Version 5.5.1 `.ged` Dateierweiterung) De-facto-Standarddateiformat für den Datenaustausch zwischen Genealogie-Programmen
- GeneWeb (`.gw` Dateierweiterung) - [GeneWeb](https://de.wikipedia.org/wiki/GeneWeb) ist ein Genealogie-Programm mit einem Webinterface.
- [Gramps XML](#Gramps_XML_und_XML_Paket_Import) (`.gramps` Dateierweiterung) Gramps natives Datenaustauschformat in unkomprimiertem Text und [gzip](https://de.wikipedia.org/wiki/Gzip) komprimiert
- [Gramps XML Package](#Gramps_XML_und_XML_Paket_Import) (`.gpkg` Dateierweiterung) Gramps [.tar.gz](https://de.wikipedia.org/wiki/Tar_(Packprogramm)) Archiv komprimiertes Backup-Format
- [GRAMPS V2.x Datenbank](#GRAMPS_V2.x_Datenbankimport) (`.grdb` Dateierweiterung)
- [Pro-Gen](wiki:De:Import_aus_einem_anderen_Genealogieprogramm#Pro-Gen) (`.def` Dateierweiterung) - [Pro-Gen](https://www.pro-gen.nl/gbhome.htm) war in den Niederlanden und im Nordwesten Deutschlands sehr beliebt. Es wird häufig von Personen verwendet, die bereits 1989 mit dem Sammeln und Speichern von Daten begonnen haben. Dies war ein DOS-basiertes Programm, das für die Verwendung mit Win 10 gepatcht wurde.
- vCard (`.vcf` Dateierweiterung) - [Virtual Contact File](https://de.wikipedia.org/wiki/VCard) ist ein Dateiformatstandard für elektronische Visitenkarten. Unterstützt nur das Format [Version 3.0](https://de.wikipedia.org/wiki/VCard#Spezifikation).

----

Zusätzliche Importer-Formate können über Zusatzmodule installiert werden und werden ebenfalls aufgelistet, zum Beispiel:

- [JSON Import](wiki:Addon:JSON_Export_Import) (`.json` Dateierweiterung) - [JavaScript Objekt Notation](https://www.json.org/json-de.html) ist ein Leichtgewicht Datenaustauschformat. ***Erweiterung***
- [SQLite Import](wiki:Addon:SQLite_Export_Import) (`.sql` Dateierweiterung) - [SQLite Datenbankformat](https://www.sqlite.org/fileformat.html) **Erweiterung**

### Import Stammbaumdialog

![[_media/Importfamilytree-dialog-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Stammbaum Import - Dialog Beispiel]]

Erstelle zunächst einen [neuen und leeren Stammbaum](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Stammbäume_Verwalten#Neuen_Stammbaum_beginnen). Wähle dann das Menü oder verwende die [Tastenkombination](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Tastenkürzel_Referenz#2) , um Daten zu importieren oder einen zuvor gespeicherten Gramps-Stammbaum (aus einer älteren Version von Gramps oder der aktuellen Version) wiederherzustellen. Das Dialogfeld **** wird geöffnet und du dazu aufgefordert, die Datei, die du importieren möchtest anzugeben.

Wenn du versuchst, in einen Stammbaum zu importieren, der ***nicht leer*** ist, wird das Dialogfeld geöffnet. Dies erinnert dich daran, vor dem Import ein Backup zu erstellen. Erstelle stattdessen einen neuen Stammbaum, es sei denn, du versuchst wissentlich, Daten zusammenzuführen.

Gramps verwendet eine [GTK-Dateiauswahl](https://developer.gnome.org/gtk3/stable/GtkFileChooser.html) zur Auswahl der zu exportierenden Datendatei. Die grundlegenden Optionen zum Navigieren zu einer Datei sind bekannt.

Die Standardanzeigeoption für den Dateipfad besteht darin, jede Ordnerebene als anklickbare [Brotkrümelnavigation](https://de.wikipedia.org/wiki/Brotkr%C3%BCmelnavigation) anzuzeigen. Der Pfad kann durch Drücken der Tastenkombination in ein bearbeitbares Textfeld eingegeben werden.

Mit der Dateityp-Erweiterung kann die Option normalerweise erwarten, dass ein bestimmtes Datenmuster in das native Datenbankformat konvertiert wird. Du kannst dies überschreiben, indem du eine andere **** Optionen auswählst. Die Liste der Dateien kann durch Ändern der Option gefiltert werden. Wenn du die Option wählst und dann einen nicht unterstützten Dateiimporttyp auswählst, wird dir der Warnungsdialog angezeigt.

Wenn du planst, den Import wiederholt zu verwenden (für laufende Updates oder einschließlich Ahnenforschung), kannst du [den Dialog anpassen](https://gramps.discourse.group/t/need-help-doing-a-cross-os-linux-mac-verification/1068/5), indem du Schaltflächen für Ordnerpfade mit Lesezeichen hinzufügst. Klicke mit der rechten Maustaste auf einen Ordnernamen und wähle im Popup-Menü .

### Unterstützte Importdateiformate

#### GRAMPS V2.x Datenbankimport

GRAMPS V2.x Datenbank (.grdb): Vor Version 3.0 war dies das Format in dem Gramps die Daten gespeichert hat, eine speziell angepasste Berkeley Datenbank (BSDDB) mit einer angepassten Datentabellenstruktur. Dieses Format war System und Architektur gebunden. Es war schnell und effizient, aber nicht sehr übertragbar auf Computer mit einer anderen Architektur (z.B. i386 nach Alpha).

Der Import im GRAMPS v2.x Datenbankformat wird nur von Gramps Version 3.0.x unterstützt. Der Import von V2.x in Gramps V3.0.x geschieht ohne Datenverlust.

##### Umziehen einer Gramps 2.2-Datenbank nach Gramps 3.x.

Um deine Gramps-Daten von Version 2.x auf Version 6.0.x umzuziehen, musst du die v2.x-Datenbank in ein früheres Gramps v3.0.x-Programm importieren und dann entweder die Datenbank speichern und in Gramps 6.0.x importieren oder exportiere die Datenbank im [XML](wiki:XML)-Format aus der früheren Gramps-Version und importiere sie in Gramps 6.0.x.

Anweisungen zum Importieren von v2.x-Datenbanken in Gramps v3.x findest du im [Benutzerhandbuch](wiki:Previous_releases_of_Gramps) für frühere Versionen von Gramps.

{{-}}

#### Gramps XML und XML Paket Import

Die Gramps [XML](wiki:XML)- und Gramps [XML](wiki:XML)-Paketdatenbank sind die nativen Archivformate von Gramps. Beim Importieren (Wiederherstellen) aus diesen Formaten oder beim Exportieren in diese Formate besteht keine Gefahr des Datenverlusts.

- Gramps [XML](wiki:XML) (.gramps): Die Gramps [XML](wiki:XML)-Datei ist das Standardformat für den Datenaustausch und die Datensicherung in Gramps und war auch das Standardformat für Arbeitsdatenbanken in älteren Versionen (vor 2.x) von Gramps. Im Gegensatz zum GRAMPS V2.x grdb-Format (oder nachfolgenden BSDDB- oder SQLite-Formatdateien) ist es architekturunabhängig und für Menschen lesbar. Die Datenbank kann auch Verweise auf nicht-lokale (externe) Medienobjekte enthalten, daher ist ihre vollständige Portabilität nicht garantiert (für vollständige Portabilität einschließlich Medienobjekten sollte das Gramps [XML](wiki:XML)-Paket (.gpkg) verwendet werden). Die Gramps [XML](wiki:XML)-Datenbank wird durch Exportieren (Menü ) in dieses Format erstellt.

<!-- -->

- Gramps [XMLPaket](wiki:XML) (.gpkg): Das Gramps [XML](wiki:XML) Paket ist eine **komprimiertes** Archiv welches die Gramps [XML](wiki:XML) Datei und alle Medienobjekte (Bilder, Klangdateien usw.) enthält, auf die der Stammbaum verweist. Weil es alle Medienobjekte enthält, ist dieses Format komplett übertragbar. Das Gramps [XMLPaket](wiki:XML) wird durch den Export (**Stammbäume -\>Export...**) der Daten in dieses Format erstellt.

Wenn du Informationen von einer anderen Gramps Datenbank oder Gramps [XML](wiki:XML) Datei importierst, wird dir der Fortschritt im Fortschrittsbalken im Gramps Hauptfenster angezeigt. Wenn der Import abgeschlossen ist, zeigt ein Statusfenster die Anzahl der importierten Objekte. Wenn die importierten Daten ursprünglich von dem Stammbaum stammen, in den du sie importierst, bekommst du Vorschläge, was zusammengefasst werden könnte; das Zusammenfassen wird **nicht** automatisch für dich erledigt. Wenn du genealogische Grunddaten automatisch zusammengefasst haben möchtest, denke über CSV Tabellen Export/Import nach.

#### Gramps CSV Import

Das Gramps CSV Tabellenformat erlaubt dir den Im- und Export einer Teilmenge deiner Gramps-Daten in einem einfachen Tabellenformat. Siehe [CSV Import und Export](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Stammbäume_Verwalten:_CSV_Import_und_Export) für mehr Informationen.

#### GEDCOM Import

Erstelle zunächst einen [neuen leeren Stammbaum](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Stammbäume_Verwalten#Neuen_Stammbaum_beginnen). Wähle dann das Menü oder die [Tastenkombination](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Tastenkürzel_Referenz#2) verwende dann das Dialogfeld , um die GEDCOM-Datei auszuwählen, die Sie importieren möchten. Abhängig vom GEDCOM-Typ wird dann möglicherweise das Dialogfeld angezeigt.

Wenn du Informationen aus GEDCOM importierst, wird im Hauptfenster von Gramps ein [Fortschrittsbalken](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Hauptfenster#Statusleiste_und_Fortschrittsbalken) angezeigt. Wenn der GEDCOM-Import abgeschlossen ist, werden im Fenster und im **** Fenster alle Ergebnisse oder Warnungen angezeigt.

- Im Abschnitt [Allgemeine Gramps Einstellungen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Einstellungen#Allgemeines) der Registerkarte Allgemeines in den Einstellungen kannst du einstellen und aktivieren. Beides kann den Import deiner Daten erheblich verlangsamen.

{{-}}

##### GEDCOM-Zeichenkodierungsdialog

![[_media/GEDCOM-Encoding-dialog-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} GEDCOM-Zeichenkodierung - Dialog]]

Das Dialogfeld wird angezeigt, wenn sich die von dir importierte GEDCOM-Datei als ANSEL-Zeichenkodierung identifiziert hat. Manchmal ist dies ein Fehler. Wenn du nach dem Import von GEDCOM feststellst, dass deine Daten ungewöhnliche Zeichen enthalten, mach den Import rückgängig und überschreibe den Zeichensatz, indem du eine andere Kodierung aus der verfügbaren Liste auswählst.

- **Standardwert**
- *ANSEL* (American National Standard Extended Latin)
- *ANSI* (American National Standards Institute; ähnlich wie ISO-8859-1)
- *ASCII* (American Standard Code for Information Interchange)
- *UTF8* (Unicode Transformation Format 8-Bit)

{{-}}

##### Import Statistik Dialog

![[_media/ImportStatistics-dialog-example-GrampXML-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Importstatistiken - Dialog - Zeigt Ergebnisse für &quot;Example.gramps&quot; die Gramps XML-Datei]] Zeigt Details der Importstatistiken in Abhängigkeit vom importierten Dateityp an.

- Gramps XML - Zeigt Importstatistiken und die Meldung an:
  - 
- GEDCOM - keine Importstatistiken ( meldet nur , wenn erfolgreich )

{{-}}

##### GEDCOM Import Bericht Dialog

![[_media/GEDCOM-import-report-result-example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} GEDCOM-Importbericht - Beispielergebnisse.]]

Der **** enthält Details zu den meisten GEDCOM-Zeilen, die entweder ignoriert wurden oder nicht verstanden werden konnten. Dies höchstwahrscheinlich, weil sie nicht Teil des GEDCOM 5.5.1-Standards sind. (Siehe [GEDCOM-Erweiterungen](wiki:Addon:GEDCOM_Extensions).) Der Inhalt der GEDCOM-Zeile (oder der Zeilen, in denen Fortsetzungszeilen vorhanden sind) wird ebenfalls angezeigt. In einigen Fällen entsprechen die Zeilen möglicherweise nicht genau dem, was in der eingegebenen GEDCOM-Datei enthalten ist, da die Zeile nach einer gewissen Verarbeitung rekonstruiert wurden. {{-}}

###### Den Bericht lesen

![[_media/Source-Note-GEDCOMImportNote-example-50.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} GEDCOM-Importnotiz mit ausgelassenen Daten, die an "Quelle&gt; Notiz" angehängt sind (Daten aus "GEDitCOM" - "GEDCOM 5.5-Stresstestdateien")]]

Gramps verwendet ein fortgeschritteneres 'Datenmodell' als GEDCOM, daher können einige Daten in GEDCOM nicht in Gramps importiert werden. (Siehe [Gramps und GEDCOM](wiki:Gramps_and_GEDCOM).) Die Hauptausnahmen sind:

- Einige GEDCOM-Attributstrukturen werden als Gramps- behandelt, und daher können viele der primitiven GEDCOM-Elemente nicht gespeichert werden.
- Die DATA-Elemente eines SOURCE RECORD (die die aufgezeichneten Ereignisse und die verantwortliche Agentur angeben) werden ignoriert.
- Alle Quellenangaben zu Notizen werden ignoriert.
- Viele primitive GEDCOM-Elemente haben nicht genau die entsprechenden Datenelemente in Gramps und werden daher als mit geeigneten Namen gespeichert, normalerweise das GEDCOM-Tag. Dies gilt insbesondere für die GEDCOM-Datensätze für Header, Übermittler und Einsendung sowie für bestimmte Felder wie REFN, RFN, RIN und AFN.

Wenn Daten als 'ignoriert' aufgeführt sind, wird ihre Auslassung im Feedback am Ende des Imports gemeldet und in einer enthalten, der an ein relevantes Objekt mit einem benutzerdefinierten Typ von angehängt ist. Siehe zum Beispiel das Quellobjekt im Beispiel-Screenshot.

Wenn Daten als 'stillschweigend ignoriert' aufgeführt sind, werden sie nicht gemeldet und nicht in eine Notiz aufgenommen. Gegenwärtig kann dies als etwas angesehen werden, das von Gramps übersehen wurde und als Problem angesprochen werden sollte. {{-}}

##### GEDCOM-Importbeschränkungen

In diesem Abschnitt werden alle GEDCOM-Daten beschrieben, die in Gramps nicht direkt dargestellt werden können, und wie sie behandelt werden. Weitere Informationen zu den Grenzwerten für GEDCOM-Importe (und -Exporte) findest du im Abschnitt über [Gramps und GEDCOM](wiki:Gramps_and_GEDCOM).

###### Kopf(HEAD), Einreichung(SUBM) und Einreicher(SUBN)

Gramps hat keine direkte Entsprechung für [Kopf](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Stammbäume_Verwalten#Kopf), [Einreichung](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Stammbäume_Verwalten#Einreichung), and [Einreicher](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Stammbäume_Verwalten#Einreicher) Daten, daher müssen diese Informationen in anderen Objekten gespeichert werden. Abhängig von den [Import Einstellungen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Einstellungen#Quelle_GEDCOM-Import) wird ein 'Standardquelle' Objekt erstellt. Wenn diese erstellt wird, werden die meisten Daten in der oder im der Quelle zugeordnet gespeichert.

###### Kopf

`   KOPF:=`  
`        n HEAD                                          {1:1}`  
`          +1 SOUR `<APPROVED_SYSTEM_ID>`                  {1:1}  (Datenelement der 'Standardquelle')`  
`            +2 VERS `<VERSION_NUMMER>`                    {0:1}  (Datenelement der 'Standardquelle')`  
`            +2 NAME `<NAME_DES PRODUKT>`                  {0:1}  (Datenelement der 'Standardquelle')`  
`            +2 CORP `<NAME_OF_BUSINESS>`                  {0:1}  (Aufbewahrungsort der 'Standardquelle')`  
`              +3 <`<ADRESSEN_STRUKTUR>`>                  {0:1}  (Aufbewahrungsort der 'Standardquelle')`  
`            +2 DATA `<NAME_OF_SOURCE_DATA>`               {0:1}  (Datenelement der 'Standardquelle')`  
`              +3 DATE `<VERÖFFENTLICHUNGSDATUM>`          {0:1}  (Datenelement der 'Standardquelle')`  
`              +3 COPR `<COPYRIGHT_SOURCE_DATA>`           {0:1}  (Datenelement der 'Standardquelle')`  
`          +1 DEST `<RECEIVING_SYSTEM_NAME>`               {0:1*} (Datenelement der 'Standardquelle')`  
`          +1 DATE `<ÜBERTRAGUNGSDATUM>`                   {0:1}  (Datenelement der 'Standardquelle')`  
`            +2 TIME `<ZEIT_WERT>`                         {0:1}  (Datenelement der 'Standardquelle')`  
`          +1 SUBM @`<XREF:SUBM>`@                         {1:1}  (Datenelement der 'Standardquelle')`

(Wird auch verwendet, um den Übermittlerdatensatz zu bestimmen)

`                                                               (dies sollte als Datenbankeignerinformation gespeichert werden)`  
`          +1 SUBN @`<XREF:SUBN>`@                         {0:1}  (ignoriert)`  
`          +1 FILE `<DATEINAME>`                           {0:1}  (Datenelement der 'Standardquelle')`  
`          +1 COPR `<COPYRIGHT_GEDCOM_DATEI>`              {0:1}  (als Veröffentlichungsinformation der 'Standardquelle' gespeichert)`  
`          +1 GEDC                                       {1:1}`  
`            +2 VERS `<VERSION_NUMMER>`                    {1:1}  (Datenelement der 'Standardquelle')`  
`            +2 FORM `<GEDCOM_FORM>`                       {1:1}  (Datenelement der 'Standardquelle')`  
`          +1 CHAR `<ZEICHENSATZ>`                         {1:1}  (Datenelement der 'Standardquelle')`  
`            +2 VERS `<VERSION_NUMMER>`                    {0:1}  (Datenelement der 'Standardquelle')`  
`          +1 LANG `<SPRACHE_VON_TEXT>`                    {0:1}  (Datenelement der 'Standardquelle')`  
`          +1 PLAC                                       {0:1}`  
`            +2 FORM `<ORTEHIERARCHIE>`                    {1:1}  (siehe unten)`  
`          +1 NOTE `<GEDCOM_CONTENT_DESCRIPTION>`          {0:1}  (Notiz der 'Standardquelle')`  
`            +2 [CONT|CONC] `<GEDCOM_CONTENT_DESCRIPTION>` {0:M}`  
`            `  
`   * Anmerkung: Einsendungen zu the Family History Department for Ancestral`  
`     File submission oder für clearing temple ordinances muss ein Ziel (DEST) aus `  
`     DESTination of ANSTFILE oder TempleReady verwenden.`

Das PLAC Formular wird intern gespeichert und verwendet die Interpretation von Orten zu steuern (in Übereinstimmung mit den GEDCOM Spezifikation).

###### Einreichung

Der SUBMISSION_Datensatz (es sollte nur einen geben, dies wird aber nicht überprüft) wird als Element der 'Standardquelle' gespeichert.

`    SUBMISSION_RECORD:=`  
`        n @`<XREF:SUBN>`@ SUBN                            {1:1]`  
`          +1 SUBM @`<XREF:SUBM>`@                         {0:1}`  
`          +1 FAMF `<NAME_OF_FAMILY_FILE>`                 {0:1}`  
`          +1 TEMP `<TEMPLE_CODE>`                         {0:1}`  
`          +1 ANCE `<GENERATIONS_OF_ANCESTORS>`            {0:1}`  
`          +1 DESC `<GENERATIONS_OF_DESCENDANTS>`          {0:1}`  
`          +1 ORDI `<ORDINANCE_PROCESS_FLAG>`              {0:1}`  
`          +1 RIN `<AUTOMATED_RECORD_ID>`                  {0:1}`

###### Einreicher

SUBMITTER_Datensätze (Es können mehr als einer vorkommen) werden als Datensätze verknüpft mit der 'Standardquelle' gespeichert. Ausnahmen sind unten **FETT** dargestellt. Der Übermittlerdatensatz entspricht dem SBM Datensatz im KOPF und wird verwendet den [Datenbankeigner](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Werkzeuge#Datenbankeigner_Informationen_bearbeiten...) zu setzen siehe dort.

`   SUBMITTER_RECORD:=`  
`        n @`<XREF:SUBM>`@   SUBM                          {1:1}`  
`          +1 NAME `<SUBMITTER_NAME>`                      {1:1}`  
`          +1 <`<ADRESSEN_STRUKTUR>`>                      {0:1}`  
`          `**`+1 <`<MULTIMEDIA_LINK>`> {0:M}`**  
`          `**`+1 LANG `<LANGUAGE_PREFERENCE>` {0:3}`**  
`          `**`+1 RFN `<SUBMITTER_REGISTERED_RFN>` {0:1}`**  
`          `**`+1 RIN `<AUTOMATED_RECORD_ID>` {0:1}`**  
`          +1 <`<ÄNDERUNGSDATUM>`>                         {0:1}`

- Multimedia Link wird ignoriert
- LANG wird ignoriert
- RFN und RIN werden ignoriert

###### Person_Datensatz

Der INDI_Datensatz wird in Gramps als Datensatz gespeichert. Ausnahmen sind unten **FETT** dargestellt.

`   PERSON_DATENSATZ: =`  
`        n @`<XREF:INDI>`@  INDI                           {1:1}`  
`          +1 RESN `<RESTRICTION_NOTICE>`                  {0:1}`  
`          +1 <`<PERSÖNLICHER_NAME_STRUKTUR>`>             {0:M}`  
`          +1 SEX `<SEX_Wert>`                             {0:1}`  
`          +1 <`<PERSÖNLICHE_EREIGNIS_STRUKTUR>`>          {0:M}`  
`          `**`+1 <`<PERSÖNLICHE_ATTRIBUTE_STRUKTUR>`> {0:M}`**  
`          +1 <`<LDS_INDIVIDUAL_ORDINANCE>`>               {0:M}`  
`          +1 <`<KIND_ZU_FAMILIE_LINK>`>                   {0:M}`  
`          +1 <`<PARTNER_ZU_FAMILIE_LINK>`>                {0:M}`  
`          `**`+1 SUBM @`<XREF:SUBM>`@ {0:M}`**  
`          +1 <`<ASSOCIATION_STRUCTURE>`>                  {0:M}`  
`          +1 ALIA @`<XREF:INDI>`@                         {0:M}`  
`          `**`+1 ANCI @`<XREF:SUBM>`@ {0:M}`**  
`          `**`+1 DESI @`<XREF:SUBM>`@ {0:M}`**  
`          +1 <`<SOURCE_CITATION>`>                        {0:M}`  
`          +1 <`<MULTIMEDIA_LINK>`>                        {0:M}`  
`          +1 <`<NOTIZ_STRUKTUR>`>                         {0:M}`  
`          +1 RFN `<PERMANENT_RECORD_FILE_NUMMER>`         {0:1}`  
`          +1 AFN `<ANCESTRAL_FILE_NUMMER>`                {0:1}`  
`          +1 REFN `<USER_REFERENZ_NUMMER>`                {0:M}`  
`            `**`+2 TYPE `<USER_REFERENZ_TYP>` {0:1}`**  
`          +1 RIN `<AUTOMATED_RECORD_ID>`                  {0:1}`  
`          +1 <`<ÄNDERUNGSDATUM>`>                         {0:1}`  
`   `

- Link zum Übermittler, Vorfahren und Nachkommen Interesse Anzeige werden stillschweigend ignoriert.
- Die Alias Kennzeichnung ("Eine Kennzeichnung um verschiedene Beschreibungsdatensätze einer Person, die die selbe Person sein könnten, zu verknüpfen") wird als mit dem Namen 'Alias' gespeichert.
- Die REFN und REFN:TYPE werden als der gespeichert. Wenn es aber mehr als eine REFN gibt ist nicht klar welcher TYP zu welcher REFN gehört.

Die Behandlung der PERSÖNLICHE_ATTRIBUTE_STRUKTUR ist komplizierter. Die folgenden Tags:

- EDUC (schulische Leistungen),
- NMR (Anzahl der Heiraten),
- OCCU (Beruf),
- PROP (Besitz),
- RELI (Religion),
- RESI und
- TITL (Adelstitel)

werden als Gramps behandelt und die zugehörigen Informationen werden in der Ereignisstruktur gespeichert. Die Details, die dem Haupttag folgen (dargestellt in den Klammern in der obigen Liste), werden als die des gespeichert. Der <EREIGNIS_DESKRIPTOR> der dem Typtag folgt, überschreibt die wenn der <EREIGNIS_DESKRIPTOR> nicht der Attributname ist.

Die folgenden Tags:

- CAST (Kastenname),
- DSCR (körperliche Beschreibung),
- INDO (National ID Nummer),
- NATI (Nationalität oder Stammeszugehörigkeit),
- NCHI (Anzahl der Kinder) und
- SSN (Sozialversicherungsnummer)

werden in Gramps als behandelt und die meisten Felder mit Ausnahme den Details die dem Haupttag folgen (in der Liste oben in Klammern dargestellt) der Quellenverweise und Notizstrukturen werden ignoriert wie unten in **FETT** angedeutet.

`   PERSON_ATTRIBUTE_STRUKTUR: =`  
`        n  CAST `<CASTE_NAME>`                            {1:1}`  
`          +1 <`<EREIGNIS_DETAIL>`>                        {0:1}`  
`             usw.`  
`   `  
`   EREIGNIS_DETAIL: =`  
`        `**`n TYPE `<EREIGNIS_DESKRIPTOR>` {0:1}`**  
`        `**`n DATE `<DATUMSWERT>` {0:1}`**  
`        `**`n <`<ORTSSTRUKTUR>`> {0:1}`**  
`        `**`n <`<ADRESSE_STRUKTUR>`> {0:1}`**  
`        `**`n AGE `<ALTER_AM_EREIGNIS>` {0:1}`**  
`        `**`n AGNC `<RESPONSIBLE_AGENCY>` {0:1}`**  
`        `**`n CAUS `<URSACHE_DES_EREIGNIS>` {0:1}`**  
`        n  <`<SOURCE_CITATION>`>                          {0:M}`  
`          +1 <`<NOTIZ_STRUKTUR>`>                         {0:M}`  
`          +1 <`<MULTIMEDIA_LINK>`>                        {0:M}`  
`        `**`n <`<MULTIMEDIA_LINK>`> {0:M}`**  
`        n  <`<NOTIZ_STRUKTUR>`>                           {0:M}`  
`        `  
`        `

- Person Attribute Struktur, Art, Datum, Ortsstruktur, Adresse Struktur, Alter, Agentur, Ursache und Multimedia Link werden alle ignoriert.

###### FAM_Datensatz

Der FAM Datensatz wird als Gramps Datensatz gespeichert.

`   FAM_Datensatz:=`  
`        n @`<XREF:FAM>`@   FAM                            {1:1}`  
`          +1 <`<FAMILIEN_EREIGNIS_STRUKTUR>`>             {0:M}`  
`          +1 HUSB @`<XREF:INDI>`@                         {0:1}`  
`          +1 WIFE @`<XREF:INDI>`@                         {0:1}`  
`          +1 CHIL @`<XREF:INDI>`@                         {0:M}`  
`          +1 NCHI `<ANZAHL_DER_KINDER>`                   {0:1}`  
`          +1 SUBM @`<XREF:SUBM>`@                         {0:M}`  
`          +1 <`<LDS_SPOUSE_SEALING>`>                     {0:M}`  
`          +1 <`<SOURCE_CITATION>`>                        {0:M}`  
`          +1 <`<MULTIMEDIA_LINK>`>                        {0:M}`  
`          +1 <`<NOTIZ_STRUKTUR>`>                         {0:M}`  
`          +1 REFN `<USER_REFERENZ_NUMMER>`                {0:M}`  
`            +2 TYPE `<USER_REFERENZ_TYPE>`                {0:1}`  
`          +1 RIN `<AUTOMATED_RECORD_ID>`                  {0:1}`  
`          +1 <`<ÄNDERUNGSDATUM>`>                         {0:1}`

- Die Verknüpfung zum Übermittler (SUBM) wird stillschweigend ignoriert.
- Die REFN und REFN:TYPE werden als der gespeichert. Wenn es aber mehr als eine REFN gibt ist nicht klar welcher TYP zu welcher REFN gehört.

###### Quellen_Datensatz

Der SOUR_Datensatz wird in Gramps als Datensatz gespeichert. Ausnahmen sind unten **FETT** dargestellt.

`   QUELLE_DATENSATZ:=`  
`        n @`<XREF:SOUR>`@ SOUR                            {1:1}`  
`          `**`+1 DATA {0:1}`**  
`            `**`+2 EVEN `<EVENTS_RECORDED>` {0:M}`**  
`              `**`+3 DATE `<DATE_PERIOD>` {0:1}`**  
`              `**`+3 PLAC `<SOURCE_JURISDICTION_PLACE>` {0:1}`**  
`            `**`+2 AGNC `<RESPONSIBLE_AGENCY>` {0:1}`**  
`            `**`+2 <`<NOTE_STRUKTUR>`> {0:M}`**  
`          +1 AUTH `<SOURCE_ORIGINATOR>`                   {0:1}`  
`            +2 [CONT|CONC] `<SOURCE_ORIGINATOR>`          {0:M}`  
`          +1 TITL `<SOURCE_DESCRIPTIVE_TITLE>`            {0:1}`  
`            +2 [CONT|CONC] `<SOURCE_DESCRIPTIVE_TITLE>`   {0:M}`  
`          +1 ABBR `<SOURCE_FILED_BY_ENTRY>`               {0:1}`  
`          +1 PUBL `<SOURCE_PUBLICATION_FACTS>`            {0:1}`  
`            +2 [CONT|CONC] `<SOURCE_PUBLICATION_FACTS>`   {0:M}`  
`          +1 TEXT `<TEXT_AUS_QUELLE>`                     {0:1}`  
`            +2 [CONT|CONC] `<TEXT_AUS_QUELLE>`            {0:M}`  
`          +1 <`<SOURCE_REPOSITORY_CITATION>`>             {0:1}`  
`          +1 <`<MULTIMEDIA_LINK>`>                        {0:M}`  
`          +1 <`<NOTIZ_STRUKTUR>`>                         {0:M}`  
`          +1 REFN `<USER_REFERENZ_NUMMER>`                {0:M}`  
`            +2 TYPE `<USER_REFERENZ_TYPE>`                {0:1}`  
`          +1 RIN `<AUTOMATED_RECORD_ID>`                  {0:1}`  
`          +1 <`<ÄNDERUNGSDATUM>`>                         {0:1}`

- DATA und seine untergeordneten Datensätze werden ignoriert

====== Aufbewahrungsort Datensatz =====

Der REPO_Datensatz wird als Gramps Datensatz gespeichert. Ausnahmen sind unten **FETT** dargestellt.

`   AUFBEWAHRUNGSORT_Datensatz: =`  
`        n @`<XREF:REPO>`@ REPO                            {1:1}`  
`          +1 NAME `<NAME_DES_AUFBEWAHRUNGSORT>`           {0:1}`  
`          +1 <`<ADRESSE_STRUKTUR>`>                       {0:1}`  
`          +1 <`<NOTIZ_STRUKTUR>`>                         {0:M}`  
`          `**`+1 REFN `<USER_REFERENZ_NUMMER>` {0:M}`**  
`            `**`+2 TYPE `<USER_REFERENZ_TYP>` {0:1}`**  
`          `**`+1 RIN `<AUTOMATED_RECORD_ID>` {0:1}`**  
`          +1 <`<ÄNDERUNGSDATUM>`>                         {0:1}`

- REFN, REFN:TYPE und RIN werden ignoriert

###### Multimedia Datensatz

Der MULTIMEDIA_Datensatz wird in Gramps als Datensatz gespeichert.Ausnahmen sind unten **FETT** dargestellt.

`   MULTIMEDIA_DATENSATZ:=`  
`        n @`<XREF:OBJE>`@ OBJE                            {1:1}`  
`          +1 FORM `<MULTIMEDIA_FORMAT>`                   {1:1}`  
`          +1 TITL `<Beschreibender_TITEL>`                {0:1}`  
`          +1 <`<NOTIZ_STRUKTUR>`>                         {0:M}`  
`          +1 <`<SOURCE_CITATION>`>                        {0:M}`  
`          `**`+1 BLOB {1:1}`**  
`            `**`+2 CONT `<ENCODED_MULTIMEDIA_LINE>` {1:M}`**  
`          +1 OBJE @`<XREF:OBJE>`@     /* chain to continued object */  {0:1}`  
`          `**`+1 REFN `<USER_REFERENZ_NUMMER>` {0:M}`**  
`            `**`+2 TYPE `<USER_REFERENZ_TYPE>` {0:1}`**  
`          `**`+1 RIN `<AUTOMATED_RECORD_ID>` {0:1}`**

- Es wird ein 'File' Tag erwartet das auf die Datei hinweist, die das Multimediaobjekt enthält. Diese Verwendung wurde aus GEDCOM 5.5.1 übernommen, aber die Möglichkeiten in GEDCOM 5.5.1 mehr als eine <Multimedia_Datei_REFN> und die zur FILE GEDCOM_Zeile untergeordneten FORM, TYPE und TITLE zu haben wird nicht unterstützt (ein späteres FILE kann ein früheres überschreiben - es gibt keine Fehlerprüfung).
- BLOB wird ignoriert
- REFN, REFN:TYPE und RIN werden ignoriert

###### Notiz Datensatz

Der NOTE_Datensatz wird als Gramps Datensatz gespeichert. Ausnahmen sind unten **FETT** dargestellt.

`   NOTIZ_DATENSATZ:=`  
`        n @`<XREF:NOTE>`@ NOTE `<SUBMITTER_TEXT>`           {1:1}`  
`          +1 [ CONC | CONT] `<SUBMITTER_TEXT>`            {0:M}`  
`          `**`+1 <`<QUELLEN_ZITAT>`> {0:M}`**  
`          `**`+1 REFN `<USER_REFERENZ_NUMMER>` {0:M}`**  
`            `**`+2 TYPE `<USER_REFERENZ_TYPE>` {0:1}`**  
`          `**`+1 RIN `<AUTOMATED_RECORD_ID>` {0:1}`**  
`          +1 <`<ÄNDERUNGSDATUM>`>                         {0:1}`

- Quellen Zitat wird ignoriert
- REFN, REFN:TYPE und RIN werden ignoriert

## Daten exportieren

Um Daten zu exportieren wähle oder die [Tastenkombination](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Tastenkürzel_Referenz#) oder auf Apple Mac's. Dies öffnet den .

Das Exportieren erlaubt dir jeden Teil deiner Gramps Datenbank mit anderen Forschern zu teilen, genauso wie das überspielen deiner Daten auf einen anderen Computer.

Gramps kann Daten in den folgenden Formaten exportieren:

- [CSV-Export (Tabelle mit durch Kommas getrennten Werten)](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Stammbäume_Verwalten#CSV-Export_.28Tabelle_mit_durch_Kommas_getrennten_Werten.29)
- [GEDCOM](#GEDCOM_Export)
- [GeneWeb](#GeneWeb_Export)
- Gramps [XML](wiki:Gramps_XML) (Stammbaum)
- Gramps [XML](wiki:Gramps_XML) Paket (Stammbaum und Medien)
- [Web Family Tree](#Web_Family_Tree_Export)
- [vCalendar](#vCalendar_Export)
- [vCard](#vCard_Export)

Zusätzliche Exportformate können über Erweiterungen installiert werden.

{{-}}

### Exportassistentdialog

Die Seiten des führen dich durch die [Auswahl des Ausgabeformats](#Ausgabeformat_w.C3.A4hlen) und anschließend durch die für dieses Format spezifischen Exportoptionen. Nach der Seite wird der Export gemäß den von dir getroffenen Auswahlen durchgeführt. Du kannst jederzeit auf die Schaltfläche klicken, deine Auswahl überarbeiten und dann den Export erneut durchführen.

- [Deine Daten speichern](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Stammbäume_Verwalten#Deine_Daten_speichern)
- [Ausgabeformat wählen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Stammbäume_Verwalten#Ausgabeformat_w.C3.A4hlen)
- [Exportoptionen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Stammbäume_Verwalten#Exportoptionen)
- [Wähle Speicherdatei](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Stammbäume_Verwalten#W.C3.A4hle_Speicherdatei)
- [Endgültige Bestätigung](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Stammbäume_Verwalten#Endg.C3.BCltige_Best.C3.A4tigung)
- [Zusammenfassung](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Stammbäume_Verwalten#Zusammenfassung)

#### Deine Daten speichern

![[_media/ExportAssistant-SavingYourData-wizard-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Exportassistent: "Speichern deiner Daten" - Startseite des Assistenten]]

Allgemeine Informationen zum Exportieren aus Gramps:

  
**Unter normalen Umständen musst du deine Änderungen in Gramps nicht direkt speichern. Alle Änderungen, die du vornimmst, werden sofort in der Datenbank gespeichert.**

<!-- -->

  
**Dieser Vorgang hilft dir dabei, eine Kopie deiner Daten in einem der verschiedenen von Gramps unterstützten Formate zu speichern. Dies kann verwendet werden, um eine Kopie deiner Daten zu erstellen, deine Daten zu sichern oder sie in ein Format zu konvertieren, das dir die Übertragung in ein anderes Programm ermöglicht.**

<!-- -->

  
**Wenn du während dieses Vorgangs deine Meinung änderst, kannst du jederzeit auf die Schaltfläche „Abbrechen“ klicken, ohne dass deine aktuelle Datenbank beeinträchtigt wird.**

Wähle die Schaltfläche , um fortzufahren.

{{-}}

#### Ausgabeformat wählen

![[_media/ExportAssistant-ChooseTheOutputFormat-wizard-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Exportassistent - Ausgabeformat wählen - Assistent Dialog]]

Ausgabeformat wählen:

- [GEDCOM](#GEDCOM_Export)

- [GeneWeb](#GeneWeb_Export)

- **Gramps [Gramps-XML](wiki:Gramps_XML) (Stammbaum)**(Vorgabe)

- Gramps [Gramps-XML](wiki:Gramps_XML) Paket (Stammbaum und Medien)

- [Tabellenkalkulation mit durch Komma getrennte Wertetabelle (CSV)](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Stammbäume_Verwalten#CSV-Export_.28Tabelle_mit_durch_Kommas_getrennten_Werten.29)

- [Web Family Tree](#Web_Family_Tree_Export)

- [vCalendar](#vCalendar_Export)

- [vCard](#vCard_Export)

Wähle dann die Schaltfläche , um fortzufahren. {{-}}

#### Exportoptionen

![[_media/ExportAssistant-ExportOptions-CSV-defaults-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Exportassistent - Exportoptionen - Dialogfeld des Assistenten (mit Standardeinstellungen für "Durch Komma getrennte Wertetabelle (CSV)") mit Hervorhebung des unteren Abschnitts für Dateiformat-spezifische Optionen]]

Nachdem du deine Optionen in den beiden Abschnitten angepasst hast.

- Oberer unbeschrifteter Abschnitt: [Filter und vertraulich](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Stammbäume_Verwalten#Filter_und_vertraulich)
- Unterer unbeschrifteter Abschnitt: [Dateiformatspezifische Exportoptionen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Stammbäume_Verwalten#Dateiformatspezifische_Exportoptionen)

Nimm die gewünschten Änderungen vor und klicke dann auf die Schaltfläche , um fortzufahren.

{{-}}

##### Filter und vertraulich

Im oberen, nicht beschrifteten Bereich kannst du mit Gramps deinen ausgewählten Stammbaum in gängige Dateiformate exportieren.

Es bietet Optionen, die es ermöglichen, deinen Export genau fest zu legen.

Filter ermöglichen es dir einen begrenzten Umfang deiner Daten, basierend auf deinen gewählten Kriterien, zu exportieren.

###### Vertraulichkeitsfilter:

Dieses aktivieren, um zu verhindern, das als ![[_media/22x22-gramps-lock.png]][vertraulich](wiki:De:Gramps_Glossar#vertraulich) markierte Datensätze im Export enthalten sind.

###### Lebendfilter:

Diese Option schränkt Daten ein und hilft, die für lebende Personen exportierten Informationen einzuschränken. Dies bedeutet, dass alle Informationen zu Geburt, Tod, Adressen, wichtigen Ereignissen usw. in der exportierten Datei weggelassen werden. Du kannst beispielsweise den Vornamen durch das Wort **Leben** ersetzen (siehe deine [Einstellungen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Einstellungen#Text)). Du kannst Notizen ausschließen und du kannst Quellen für [lebende Personen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Vermutlich_lebend) ausschließen.

Manchmal ist aus den Daten nicht immer ersichtlich, ob jemand tatsächlich lebt. Gramps verwendet einen erweiterten Algorithmus, um festzustellen, [ob eine Person noch am Leben sein könnte](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Vermutlich_lebend). Denke daran, dass Gramps seine besten Vermutungen anstellt und möglicherweise nicht immer in der Lage ist, immer richtig zu raten. Bitte überprüfe deine Daten genau.

Wähle aus den folgenden Optionen:

- (Standardeinstellung)

- 

- 

- 

###### Personenfilter:

Wähle aus den folgenden Optionen:

- (Standardeinstellung)

- 

- 

- 

- 

- Erstelle einen benutzerdefinierten Filter, indem du auf das *Bearbeiten Symbol* klickst, um den Dialog anzuzeigen.

###### Notizfilter:

Wähle aus den folgenden Optionen:

- (Standardeinstellung)

- Erstelle einen benutzerdefinierten Filter, indem du auf das Symbol Bearbeiten klickst, um den Dialog anzuzeigen.

###### Referenzfilter:

Wähle aus den folgenden Optionen:

- (Standardeinstellung)

- 

##### Dateiformatspezifische Exportoptionen

Der untere, nicht beschriftete Bereich wird nur in Abhängigkeit vom gewählten Dateiformat angezeigt. Unter dem Abschnitt *[Filter und Datenschutz](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Stammbäume_Verwalten#Filter_und_vertraulich)* findest du eine Reihe von dateiformatspezifischen Exportoptionen zur Auswahl.

Weitere Informationen zu den aufgelisteten Dateiformaten mit bestimmten Exportoptionen findest du im entsprechenden Abschnitt:

- [Durch Komma getrennte Wertetabelle (CSV)](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Stammbäume_Verwalten#CSV-Export_.28Tabelle_mit_durch_Kommas_getrennten_Werten.29)
- [Gramps-XML (Stammbaum)](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Stammbäume_Verwalten#Gramps_XML_.28Stammbaum.29_Export)

#### Wähle Speicherdatei

![[_media/ExportAssistant-SelectSaveFile-example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Exportassistent - "Wähle Speicherdatei" - Dialogfeld des Assistenten - Beispiel]]

Gib eine Exportdatei ein. `Untitled_1.`<Dateiformat-Erweiterung>(Standard) und wähle den Ordner aus, in dem die Exportdatei gespeichert werden soll (normalerweise dein **Dokumente** Ordner).

Wähle dann die Schaltfläche , um fortzufahren.

Wenn du nicht berechtigt bist, die Datei an diesem Speicherort zu speichern, wird das Warndialogfeld und anschließend der Exportassistent Assistentendialog angezeigt. Wähle die Schaltfläche und starte den Export erneut wähle Diesmal einen geeigneten Ordner. {{-}}

#### Endgültige Bestätigung

![[_media/ExportAssistant-FinalConfirmation-example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Exportassistent - Endgültige Bestätigung - Assistentendialog - Beispiel]]

Im Assistenten Dialogfeld für die des Exportassistenten kannst du die zusammengefassten Details (Format / Name / Ordner) der zu erstellenden Exportdatei überprüfen.

Zu diesem Zeitpunkt kannst du drücken, um Ihre Optionen erneut aufzurufen, oder , um den Vorgang abzubrechen.

Oder klicke auf die Schaltfläche , um fortzufahren. {{-}}

#### Zusammenfassung

![[_media/ExportAssistant-YourDataHasBeenSaved-example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Exportassistent - Zusammenfassung - Assistentendialog - Beispiel]]

Der Dialog der Export-Assistenten- zeigt den Dateinamen an und bestätigt, dass deine exportierten Daten erfolgreich gespeichert wurden, und zeigt eine Erinnerung an den Speicherort der Datei an.

Klicke auf die Schaltfläche , um den Exportassistenten zu beenden. {{-}}

### CSV-Export (Tabelle mit durch Kommas getrennten Werten)

![[_media/ExportAssistant-ExportOptions-CSV-defaults-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Exportassistent - Exportoptionen - Dialogfeld des Assistenten (mit Standardeinstellungen für "Tabelle mit durch Kommas getrennten Werten (CSV)") mit Hervorhebung des unteren Abschnitts für Dateiformat-spezifische Optionen]]

Durch Komma getrennte Wertetabelle(CSV): Ermöglicht das Exportieren (und Importieren) einer Teilmenge deiner Gramps-Daten in einem einfachen Tabellenformat.

Weitere Informationen und Beispiele findest du unter [CSV-Import und -Export](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Stammbäume_Verwalten:_CSV_Import_und_Export).

Tabelle mit durch Kommas getrennten Werten (CSV) bietet die folgenden [dateiformatspezifischen Exportoptionen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Stammbäume_Verwalten#Dateiformatspezifische_Exportoptionen):

- \-

- \-

- \-

- \-

- \-

{{-}} Siehe auch [Ansicht exportieren](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Einstellungen#Ansicht_exportieren).

### GEDCOM Export

Mit Gramps kannst du eine Datenbank in das gängige -Format exportieren.

Der -Export verfügt über keine [dateiformatspezifischen Exportoptionen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Stammbäume_Verwalten#Dateiformatspezifische_Exportoptionen). Du kannst jedoch Folgendes ändern:

- Stelle sicher, dass du deine -Informationen hinzufügst, um eine gültige GEDCOM-Datei zu erstellen. Dies kann auch mit dem Werkzeug zum durchgeführt werden.

Weitere Informationen zum GEDCOM-Format findest du unter:

- <https://de.wikipedia.org/wiki/GEDCOM>
- <https://www.familysearch.org/developers/docs/guides/gedcom>
- <https://www.familysearch.org/developers/docs/gedcom/>

Weitere Informationen zu Daten, die beim Export nach GEDCOM nicht exportiert werden, findest du unter [Gramps und GEDCOM](wiki:Gramps_and_GEDCOM) (). {{-}}

### GeneWeb Export

Export nach GeneWeb speichert deine Daten in einem gängigen Webgenealogieformat.

Um mehr Informationen zu GeneWeb und sein Format zu erhalten, besuche

- [GeneWeb](http://opensource.geneanet.org/projects/geneweb)

verfügt über keine [dateiformatspezifischen Exportoptionen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Stammbäume_Verwalten#Dateiformatspezifische_Exportoptionen) {{-}}

<span id="Export into Gramps formats"></span>

### Gramps XML (Stammbaum) Export

![[_media/ExportAssistant-ExportOptions-GrampsXMLFamilyTree-defaults-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Exportassistent - Exportoptionen - Assistent (zeigt die Standardeinstellungen für "Gramps XML (Stammbaum)" an) Der untere Abschnitt zeigt die dateiformatspezifische Option „[x]Komprimierung verwenden“.]]

Export (.gramps): Dies Format ist das Standardformat für Datenaustausch und Sicherungen (siehe das verwandte .gpkg Format weiter unten für volle Portabilität inklusive Medienobjekten). Der Export im Gramps [XML](wiki:XML) Format erzeugt eine portable Datenbank. Da XML ein textbasiertes von Menschen lesbares Format ist, kannst du es auch verwenden, um einen Blick auf deine Daten zu werfen. Gramps garantiert dir, das du XML Ausgaben älterer Gramps Versionen in neueren Gramps Versionen öffnen kannst (allerdings nicht andersherum!).

Wenn eine Mediendatei während des Exports nicht gefunden wird, siehst du den selben Dialog wie beim GEDCOM Export.

hat die folgenden [dateiformatspezifischen Exportoptionen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Stammbäume_Verwalten#Dateiformatspezifische_Exportoptionen):

- \- Option, die es Gramps ermöglicht, eine .gramps-Datei zu exportieren, ohne sie zu komprimieren. (Das Kontrollkästchen ist standardmäßig aktiviert)

{{-}}

#### Was ist nicht enthalten:

### Gramps XML Paket (Stammbaum und Medien) Export

Export (.gpkg): Der Export in das Gramps-Paketformat erstellt eine komprimierte Datei, welche die Gramps [XML](wiki:XML) Datei und Kopien aller zugehörigen Mediendateien enthält. Dies ist sinnvoll wenn du deine Daten auf einen anderen Computer kopieren oder mit jemanden teilen willst.

Wenn eine Mediendatei während des Exports nicht gefunden wird, siehst du den selben Dialog wie beim GEDCOM Export.

hat keine [dateiformatspezifischen Exportoptionen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Stammbäume_Verwalten#Dateiformatspezifische_Exportoptionen)

#### Was ist nicht enthalten:

### Web Family Tree Export

Der Export erstellt eine Textdatei, die vom **Web Family Tree** Programm verwendet werden kann.

Weitere Informationen zum Web Family Tree und seinem Format findest du unter

- [`http://www.simonward.com/cgi-bin/page.pl?family/tree`](http://www.simonward.com/cgi-bin/page.pl?family/tree) - [Toter Link](https://de.wikipedia.org/wiki/Toter_Link). *siehe* [2016 **Internet Archive** snapshot](https://web.archive.org/web/20160316080343/http://www.simonward.com/cgi-bin/page.pl?family/tree)

hat keine [dateiformatspezifischen Exportoptionen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Stammbäume_Verwalten#Dateiformatspezifische_Exportoptionen) {{-}}

### vCalendar Export

Export speichert die Informationen in einem Format welches in vielen Terminplanungs und Adressverwaltungsprogrammen verwendet wird, manchmal als PIM (Persönlicher Informationsmanager)bezeichnet.

Für mehr Informationen über das Format siehe:

- <https://en.wikipedia.org/wiki/ICalendar#vCalendar_1.0>

hat keine [dateiformatspezifischen Exportoptionen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Stammbäume_Verwalten#Dateiformatspezifische_Exportoptionen) {{-}}

### vCard Export

Export speichert die Informationen in einem Format welches in vielen Terminplanungs und Adressverwaltungsprogrammen verwendet wird, manchmal als PIM (Persönlicher Informationsmanager)bezeichnet.

Für mehr Informationen über das Format siehe:

- <https://de.wikipedia.org/wiki/VCard>

hat keine [dateiformatspezifischen Exportoptionen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Stammbäume_Verwalten#Dateiformatspezifische_Exportoptionen) {{-}}

[S](wiki:Category:De:Dokumentation)
