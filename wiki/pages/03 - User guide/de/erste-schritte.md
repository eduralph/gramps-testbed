---
title: De:Gramps 6.0 Wiki Handbuch - Erste Schritte
categories:
- De:Dokumentation
managed: false
source: wiki-scrape
wiki_revid: 130335
wiki_fetched_at: '2026-05-30T17:45:35Z'
lang: de
---

{{#vardefine:chapter\|2}} {{#vardefine:figure\|0}}

In diesem Kapitel werden wir mit den Grundlagen beginnen. Erst beschreiben wir die Grundkonzepte in Gramps. Dann werden wir dir zeigen wie man Gramps startet und wie du Hilfe bekommst, wenn du sie benötigst. \_\_FORCETOC\_\_

## Übersicht über Gramps

Gramps ist ein kostenloses Open-Source-Programm, das als flexibles und leistungsstarkes Genealogie-Werkzeug entwickelt wurde. Es ist ein Rahmen für das Sammeln von genealogischen Daten, wobei festgestellt wird, wie jedes Datenelement miteinander in Beziehung steht, und diese Beziehungen darstellt.

Grundsätzlich kann man Gramps nach Belieben verwenden. Es gibt keine einzige, korrekte Methode, um mit deinen Daten zu arbeiten oder sie aufzuzeichnen. Wenn du jedoch mit anderen Forschern oder Programmen zusammenarbeiten möchtest, ist es hilfreich, einige gemeinsame Richtlinien einzuhalten. Auch wenn du mit gängigen genealogischen Forschungspraktiken vertraut bist, musst du dennoch verstehen, wie Gramps funktioniert. Dann kannst du in die Verwendung des Gramps-Programms einsteigen, um einen bestimmten genealogischen Forschungsstil zu ergänzen.

Gramps unterteilt alle genealogischen Informationen in 9 Hauptkategorien von Elementen:

- [Personen](wiki:De:Gramps_Glossar#Person)

- [Familien](wiki:De:Gramps_Glossar#Familie)

- [Ereignisse](wiki:De:Gramps_Glossar#Ereignis)

- [Orte](wiki:De:Gramps_Glossar#Ort)

- [Notizen](wiki:De:Gramps_Glossar#Notiz)

- [Medien](wiki:De:Gramps_Glossar#Medien)

- [Fundstellen](wiki:De:Gramps_Glossar#Fundstelle)

- [Quellen](wiki:De:Gramps_Glossar#Quelle)

- [Aufbewahrungsorte](wiki:De:Gramps_Glossar#Aufbewahrungsort)

Jedes davon besteht aus eigenständigen Elementen. Das bedeutet, dass du einen Eintrag nach dem anderen und in beliebiger Reihenfolge in deinen Stammbaum eintragen kannst. Du kannst die Elemente miteinander verbinden oder sie getrennt (oder sogar chaotisch desorganisiert) aber durchsuchbar lassen. Oder du kannst mit einem Baum-Design im Kopf beginnen und es nach außen füllen und dabei neue Elemente verbinden.

Du kannst beispielsweise zuerst jedes Personenelement eingeben und sie dann miteinander verbinden, indem du später Familienelemente erstellst. Oder du kannst mit einer Familie beginnen, die Familie verankern, indem du eine neue Person als Kind oder Elternteil hinzufügst, und dann Verwandte, Ereignisse und Quellmaterialien in den vorbereiteten Slots des Familien-Frameworks hinzufügst. Oder du beginnst mit Quellelementen und erstellst nur dann ein Personenelement, wenn deine Recherche eine Person erwähnt. Oder du kannst diese Arten der Dateneingabe mischen, indem du einige Notiz- und Quellenelemente hinzufügst, dann Familienelemente und später zu Notizen und Quellen zurückkehrst. Kurz gesagt, du machst deine genealogische Forschung, wie du möchtest.

Wenn du zusätzliche Fragen hast, besitzt Gramps eine lebende Gemeinschaft von Anwendern und Entwicklern. Es gibt eine [FAQ](wiki:De:Gramps_6.0_Wiki_Handbuch_-_FAQ) (häufig gestellte Fragen Liste); eine [Mailingliste](wiki:De:Kontakt#Mailingliste); [ein Fehler und Feature-Request Verfolgungswerkzeug](wiki:Using_the_bug_tracker); und du kannst über Online-[Chatrooms](wiki:De:Kontakt#Chatraum) oder [Community-Foren](wiki:De:Kontakt#Forum) interagieren.

### Verbindungen

Diese 9 Hauptelemente sind auf verschiedenste Weisen miteinander verknüpft. Einige dieser Verbindungen werden automatisch verwaltet. Zum Beispiel das Hinzufügen eines Personenelements zu einer Familie als Elternteil oder Kind erzeugt automatisch eine **Referenz** genannte Verbindung. Du kannst die Familien, mit denen eine Person verbunden ist, im Referenzenreiter des Personhauptfenster sehen. Es gibt viele andere Wege auf denen diese Verbindungen in Gramps noch dargestellt werden, unter anderem in der Beziehungenansicht.

Um das Wiederholen von Informationen zu vermeiden, ermöglicht es Gramps Elemente wiederzuverwenden oder zu teilen. Dies sind auch spezielle Verbindungen **Verknüpfung** genannt. Zum Beispiel kann ein Personenelement mit einer beliebigen Anzahl von Notizelementen verbunden sein. Wenn eine Notiz zwei getrennte Personen erwähnt, kann es Sinn machen, diese Notiz mit diesen beiden Personenelementen zuteilen.

Einige Verknüpfungen sind selbst Informationen. Zum Beispiel kannst du eine Person mit dem Hochzeitsereignis eines anderen Paares verknüpfen, sagen wir die Person war ein Trauzeuge bei der Hochzeit. Allerdings sind der Mann und die Frau mit einer **primär** Rolle mit dem Hochzeitsereignis verknüpft wohingegen ein Trauzeuge eine andere Rolle besitzt z.B. ein **Zeuge**. Diese Art von Information wird in der Verknüpfung selbst in der Rolle Eigenschaft gespeichert.

### Vertraulichkeit

Gramps unterstützt zwei Methoden um die Vertraulichkeit von sensiblen Daten in deinem Stammbaum sicherzustellen. Diese Methoden werden verwendet, wenn du deine Daten mit anderen teilst entweder durch das Erstellen eines Berichts, das Exportieren deiner Daten oder durch das Erstellen einer Website.

Die erste Methode schützt Informationen von Personen, von denen Gramps annimmt, dass sie leben. Wenn du nicht ausdrücklich angegeben hast, dass eine Person tot ist (durch Hinzufügen eines Todesereignis zu einem Personenelement), dann besitzt Gramps eine komplexe und automatische Funktion, um zu bestimmen, ob jemand tot ist. Die sensiblen Daten von lebenden Personen werden zensiert, wenn diese Methode verwendet wird. Zum Beispiel eine Person mit dem Namen "Smith, John" kann als "Smith, \[Lebt\]" erscheinen.

Die zweite Methode zum Schutz der Privatsphäre ist eine explizite ["vertraulich" Markierung](wiki:De:Gramps_Glossar#Vertraulich_Markierung), die als ![[_media/22x22-gramps-lock.png]]verschlossenes Vorhängeschloss angezeigt wird, wenn sie privat ist, und die du für jedes Element festlegen kannst. Beispielsweise könntest du sensible, persönliche Informationen in einer Notiz haben. Wenn du eine solche Notiz als privat markierst, wird sie nicht in Text- und Erzählungsberichten oder Exporten angezeigt. Beachte auch, dass einige Links selbst als vertraulich markiert werden können. Dies ist nützlich, wenn du beispielsweise die Verbindung zwischen einer Person und einem Ereignis als vertraulich markieren möchtest, die Person und das Ereignis aber dennoch im Bericht, Export oder auf der Website verfügbar sein sollen.

![[_media/Include-data-marked-private-checkbox-example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Datenschutzüberschreibungen für Berichte]]Um diese zwei Methoden zur Vertraulichkeit zu aktivieren, musst du ihre Verwendung bei der Erstellung von Berichten oder dem Export von Daten angeben. {{-}}

### GEDCOM

Gramps leitet seine Kernstruktur von Elementen aus einem Standard namens GEDCOM ab. Gramps erweitert diesen Standard jedoch, wenn dies als notwendig erachtet wurde. Wenn du vorhast, deine Familiendaten mit einem anderen System zu verwenden, das GEDCOM verwendet, solltest du wahrscheinlich versuchen, die Verwendung von Funktionen, die nur Gramps-Erweiterungen sind, einzuschränken. Wenn du jedoch nicht durch andere genealogische Software eingeschränkt bist, kannst du deine Daten auf eine für dich sinnvolle Weise eingeben.

Weitere Informationen zu diesem Problem findest du im Abschnitt über [Gramps und GEDCOM](wiki:Gramps_and_GEDCOM) (englisch).

## Gramps starten

Der beste Weg um Gramps kennen zu lernen, ist mit deinen Daten zu arbeiten. Lass uns anfangen!

Wie du Gramps startest, hängt davon ab, welches Betriebssystem du verwendest.

Ebenso wie es möglich ist, Gramps über die normale grafische Benutzeroberfläche (GUI), wie unten beschrieben zu starten, ist es auch möglich, Gramps unter Verwendung der Kommandozeilenschnittstelle (CLI) zu starten. Über die Verwendung der CLI können Berichte erstellt werde, die über die GUI nicht verfügbar sind, es können Berichte erstellt werden und Konvertierungen durchgeführt werden usw. ohne dass ein Fenster geöffnet wird und es können [zusätzliche Informationen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Fehler_und_Warnung_Referenz#Alle_Fehlermeldungen_anzeigen) im Falle von Problemen zur Verfügung gestellt werden. Für mehr Informationen siehe [der Kommandozeilenanhang](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Kommandozeilen_Referenz).

### Linux

Nur die Linux Plattform wird offiziell unterstützt, da die Gramps Entwickler den Quellcode auf dieser Plattform verwenden und testen, und jedes Problem das wegen einer Aktualisierung auftritt beheben.

Angenommen du hast die normale Paketverwaltung (entweder über die GUI oder CLI) für deine Linux Distribution verwendet, startest du Gramps auf die für deine Distribution übliche Art. Zum Beispiel in Ubuntu 18.04 ist ein Symbol in Start platziert. In anderen Distributionen kann ein Symbol im Anwendungsmenü (normalerweise im **Büro** Abschnitt)vorhanden sein.

Das Starten von Gramps mit dem CLI in Linux wird [hier](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Kommandozeilen_Referenz#Linux) behandelt.

### MS Windows

MS(Microsoft) Windows ist eine [von der Gemeinschaft unterstützte](wiki:De:Download#MS_Windows) Plattform. Wenn du das [Windows AIO](wiki:GrampsAIO_cx_freeze-based) GrampsAIO64 installierst, erstellt dies ein Symbol auf dem Desktop und einen Menüeintrag im Startmenü und du kannst auf diese klicken, um Gramps zu starten.

Das Starten von Gramps über die Befehlszeile (CLI) unter MS Windows wird [hier](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Kommandozeilen_Referenz#MS_Windows) behandelt.

Es gibt noch andere Möglichkeiten um Gramps in Windows zu installieren, diese sind aber viel komplizierter und werden hier nicht behandelt.

### macOS

Apple macOS (ürsprünglich Mac OS X kurz OS X) ist eine [von der Gemeinschaft unterstützte](wiki:De:Download) Plattform. Wenn du das macOS Plattenabbild (.dmg) herunter lädst, ziehst du die Anwendung einfach in dein Anwendungsverzeichnis (oder irgendwo sonst, wo du es speichern willst) und startest Gramps auf die übliche Art durch doppelklicken auf die Anwendung.

Das Starten von Gramps mit dem CLI in macOS wird [hier](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Kommandozeilen_Referenz#macOS) behandelt.

Es gibt noch andere Möglichkeiten um Gramps in mac OS X zu installieren, diese sind aber viel komplizierter und werden hier nicht behandelt.

## Einen Stammbaum wählen

![[_media/Dashboard-category-view-first-open-no-family-tree-loaded-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Dashboard Kategorieansicht - Erstes öffnen von Gramps mit keinem geladenen Stammbaum(Gramps 6.0 Linux KUbuntu)]]

Wenn Gramps ohne gewählten Stammbaum gestartet wird, hat der Startbildschirm nur wenige Funktionen. Die meisten Funktionen stehen nicht zur Verfügung. Um einen Stammbaum zu laden (auch als *Datenbank* bezeichnet), wähle im Menü , um die Stammbaumverwaltung zu öffnen oder klicke auf die Schaltfläche in der Werkzeugleiste. Gramps behält die Übersicht über deine kürzlich geöffneten Stammbäume und diese können durch Klicken auf den Pfeil neben der Schaltfläche und Auswahl aus dem Aufklappmenü gewählt werden.

Für mehr und genauere Informationen über die Stammbaumverwaltung und das Stammbaummenü, lies das entsprechende Kapitel: [Stammbäume verwalten](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Stammbäume_Verwalten).

{{-}}

## Sag mir wie ich jetzt sofort anfangen kann!

Wir empfehlen allen, das Handbuch zu lesen, um alles über die Verwendung von Gramps zu erfahren. Genealogie braucht Zeit, daher ist es gut investierte Zeit, sich mit den Werkzeugen vertraut zu machen.

Wie auch immer, wenn du wirklich nur das absolut Nötige zum Starten willst, dann lies:

- [Gramps 6.0 Wiki Handbuch - Daten eingeben und bearbeiten: Kurz](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Daten_eingeben_und_bearbeiten:_Kurz)
- [Wie starte ich mit der Genealogie unter der Verwendung von Gramps](wiki:De:Mit_Genealogie_beginnen).

## Hilfe bekommen

Gramps hat ein Menü, das du jederzeit befragen kannst.

- Siehe den Menü Abschnitt.

{{-}}

[E](wiki:Category:De:Dokumentation)
