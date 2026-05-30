---
title: De:Gramps 6.0 Wiki Handbuch - FAQ
categories:
- De:Dokumentation
managed: false
source: wiki-scrape
wiki_revid: 128620
wiki_fetched_at: '2026-05-30T17:46:00Z'
lang: de
---

{{#vardefine:chapter\|A}} {{#vardefine:figure\|0}} Dieser Abschnitt enthält eine Liste von **Häufig gestellten Fragen** (englisch kurz FAQ), die in Diskussionen, Foren und Mailinglisten häufig auftauchen.

Wenn du Fragen/Antworten zu dieser Liste hinzufügen möchtest, melde dich bitte unter [Kontakt](wiki:De:Kontakt#Forum) an und füge deine Vorschläge im Hilfebereich des Forums hinzu.

Schaue bitte auch hier (in englisch):

- [Wie mache ich...](wiki::Category:How_do_I...)
- [Gramps Lernprogramme](wiki::Category:Tutorials)

Möglicherweise ist es hilfreich, dies zu überprüfen

- [Glossar](wiki::De:Gramps_Glossar) - gibt einen Überblick über Begriffe, die in Gramps erscheinen
- [Genealogie Glossar](wiki::De:Glossar) - genealogische Begriffe und Bedeutungen.

## Allgemein

### Was ist Gramps?

Gramps ist eine Sammlung von persönlichen Ahnenforschungswerkzeugen, mit denen du genealogische Daten speichern, bearbeiten und recherchieren kannst. Es hilft dir, die komplexen Beziehungen zwischen verschiedenen Personen, Orten und Ereignissen zu ordnen. Gramps bietet dir viele verschiedene Möglichkeiten, die vielen Details aus dem Leben einer Person zu erfassen, und alle deine Recherchen werden organisiert und durchsuchbar gehalten. Siehe [Über](wiki:GRAMPS:About/de).

### Wo bekomme ich es und wie viel kostet es?

Gramps kann ohne Gebühr [installiert](wiki:De:Installation) werden. Gramps ist ein Open Source Projekt unter der GNU General Public License. Du hast vollen Zugriff auf den Quellcode und kannst das Programm und den Quellcode frei weitergeben.

### Muss ich mich als Benutzer registrieren, um Gramps verwenden zu können? Ich bin kein Programmierer.

Nein, eine Registrierung ist nur erforderlich, wenn du einen Fehlerbericht (oder eine Funktionsanforderung) einreichen oder eine Wiki-Seite bearbeiten / schreiben möchtest.

Dafür sind keine Programmierkenntnisse erforderlich.

### Gibt es Gramps in anderen Sprachen?

Ja, mit der Veröffentlichung von Gramps 6.0 ist es in 28 Sprachen übersetzt, siehe [Gramps Übersetzungen (englisch)](wiki:Gramps_translations).

### Wie bewahre ich Sicherungen?

Die automatische Sicherung ist eine Standardfunktion, die deine genealogischen Daten in Gramps schützt. (Mit der Veröffentlichung der Version 6.0 wurde es 2018 automatisiert.) Die Einstellungen für das Intervall, den Sicherungsdateipfad und die Option, ob beim Beenden von Gramps eine Sicherung durchgeführt werden soll, befinden sich auf der Registerkarte des Menüs Darüber hinaus kann eine Sicherung manuell im Fenster ausgewählt werden.

Es ist sehr wichtig Sicherungen deiner Daten zu erstellen und diese an einem sicheren Ort aufzubewahren. Gramps besitzt ein eigenes portables Dateiformat welches von Menschen gelesen werden kann und wenig Platz beansprucht. Es wird gekennzeichnet durch: `.gramps`. Siehe "[Einen Stammbaum sichern](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Stammbäume_Verwalten#Einen_Stammbaum_sichern)" Abschnitt des Handbuchs. Es ist auch wichtig zu wissen, [was in einem Gramps-Backup nicht enthalten ist](wiki:Template:Backup_Omissions/de).

Du kannst diese Sicherung von Zeit zu Zeit an einen sicheren Ort kopieren (z.B. einen USB-Stick). \[Beachte: Die `.gramps` Dateien sind standardmäßig komprimiert. Wenn sie angeklickt werden wird Gramps geöffnet. Um das XML zu sehen, wähle die `.gramps` Datei und öffne sie mit einem dekomprimierungs Werkzeug (wie ark, gunzip, 7-zip), anschließend kannst du die XML-Text Datei entpacken welche von Menschen gelesen werden kann siehe [Details](wiki:Generate_XML#How_do_I_uncompress_the_file?) (englisch).

Gramps erstellt eine schnelle versteckte binäre Sicherung zur Wiederherstellung falls ein Fehler festgestellt wird. Wenn das richtige Paket installiert ist, kannst du ein Versionierungssystem verwenden.

Eine andere Methode ist, das versteckte Verzeichnis *`./gramps`* zu sichern. Dieses Unterverzeichnis befindet sich bei Linux Systemen in deinem [home Verzeichnis](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Anwenderverzeichnis). Die Sicherung dieses Verzeichnisses sichert deine Datenbank und Änderungen. (Unter Windows 10 ist es *`/Benutzer/`<dein Name>`/AppData/Roaming/gramps`*)

**Verwende für Sicherungen kein GEDCOM Format**. Nicht alle Informationen, die Gramps speichert können in GEDCOM geschrieben werden. Daher bedeutet ein Export/Import von Gramps nach GEDCOM und ein Re-Import nach Gramps, dass du [Daten](wiki:Gramps_and_GEDCOM) *verlierst*. Verwende für Sicherungen das `.gramps` Dateiformat!

**Verwende das GRDB Format nicht für Sicherungen**. GRDB ist eine Datenbank, welche rechnerabhängig sein kann (lesen auf anderen Rechnern nicht möglich). Kleine Schäden an der Datei können auch nicht repariert werden. Verwende für Sicherungen das `.gramps` Dateiformat!

### Unterstützt Gramps Unicode Zeichensätze?

Unterstützt es insbesondere nicht-lateinische Unicode-Schriftarten? Ja. Gramps arbeitet intern mit Unicode (UTF-8), so dass alle Alphabete für alle Eingabefelder verwendet werden können.

Für die Eingabe von Unicode-Symbolen (Glyphen), die nicht direkt auf Ihrer Tastatur beschriftet sind, gibt es keine spezielle Hilfe. Suchhilfen für [vorkomponierte Zeichen](https://wikipedia.org/wiki/Precomposed_character) (auch zusammengesetzte Zeichen oder dekomponierbare Zeichen genannt) mit diakritischen Zeichen sind außerhalb des Programms verfügbar. Vielleicht findest du die verschiedenen sprachspezifischen [multilingualen virtuellen Tastaturen auf der Lexilogos-Website](https://www.lexilogos.com/keyboard/latin_alphabet.htm) nützlich.

Alle Berichte unterstützen Unicode, [auch wenn du für PDF/PS](#Warum_werden_nicht_lateinische_Zeichen_in_PDF.2FPS_Berichten_als_M.C3.BCll_dargestellt.3F) mit gnome-print oder [LibreOffice](https://de.libreoffice.org/download/download/) arbeiten musst.

## Installation

### Was wird benötigt um Gramps unter Linux, Solaris, oder FreeBSD zu installieren?

Gramps ist eine [GTK](http://de.wikipedia.org/wiki/GTK%2B) Anwendung. Gramps benötigt die [PyGObject](http://de.wikipedia.org/wiki/PyGObject) Bibliotheken auf dem System. Solange diese Bibliotheken installiert sind, sollte Gramps funktionieren. Es läuft unter dem GNOME Desktop, dem KDE Desktop oder jedem anderen Desktop. Wenn die GNOME Anbindungen für Python auf dem System installiert sind, enthält Gramps zusätzliche Funktionalitäten. Bitte prüfe, ob es den Empfehlungen des Gramps-Projekts bezüglich der zu verwendenden GTK-Version entspricht.

### Funktioniert Gramps unter Windows?

Ja, Windows ist eine von der Community unterstützte Plattform für Gramps.

Du kannst das [All In One Gramps-Softwarepaket für Windows](wiki:All_In_One_Gramps_Software_Bundle_for_Windows) (GrampsAIO) [herunterladen](wiki:De:Download#MS_Windows).

Wir werden unser Bestes tun, um alle gemeldeten Windows-Probleme zu lösen. Siehe [hier](wiki:De:Kontakt).

### Funktioniert Gramps auf dem Mac?

Ja, Mac ist eine von Gramps unterstützte Plattform.

Du kannst die macOS Version [herunterladen](wiki:De:Download#macOS).

Wir werden unser Bestes tun, um alle gemeldeten Apple macOS-Probleme zu lösen. Siehe [hier](wiki:De:Kontakt).

Siehe [hier](wiki:Mac_OS_X:Application_package) (englisch).

### Funktioniert Gramps auf meinem Mobilgerät?

Die kurze Antwort lautet "Nein". Gramps kann nicht auf deinem Mobiltelefon oder Tablet installiert werden( [Google Android](https://de.wikipedia.org/wiki/Android_(Betriebssystem)) oder [Apple iOS](https://de.wikipedia.org/wiki/IOS_(Betriebssystem)) )

Die technischere Antwort ist "ja", aber ***nicht**'' als***native**'' Anwendung. Die Verwendung von Gramps würde entweder erfordern:

:# eine Version des Linux-Betriebssystems zusammen mit allen Unterstützungspaketen auf dem mobilen Gerät installieren, oder

:# einen lokalen oder Online-Server mit einer [für die Zusammenarbeit konzipierten Gramps-Variante](wiki:Web_Solutions_for_Gramps#Interactive_web_apps) (z. B. [Gramps Web](wiki:Web_Solutions_for_Gramps#GrampsWeb)) einrichten und dann mit Gramps über das Internet arbeiten

### Funktioniert Gramps auf meinem Google Chromebook?

Du kannst Gramps mit ein paar Einschränkungen auf deinem [Chromebook](https://de.wikipedia.org/wiki/Chromebook)(\[hhttps://de.wikipedia.org/wiki/ChromeOS ChromeOS\]) installieren.

Siehe:

- Drag and Drop funktioniert nicht in Crostini\[Linux\] auf einem Pixelbook

### Was sind die Mindestanforderungen um Gramps laufen zu lassen?

Wir empfehlen eine Bildschirmauflösung von mindestens 1920x1080 Punkten. Für Gramps 3.0 wurden die Speicheranforderungen reduziert und Gramps kann leistungsfähig auf einem 256MB System laufen und erheblich mehr Personen fassen. Ein System mit 512MB sollte ungefähr 200.000 Personen fassen können. Festplattenspeicherplatzanforderungen sind jedoch erheblich höher, für eine typische Datenbank mit einer Größe von etlichen Megabyte. Für 120.000 Personen musst du bereits mit 530MB für die Datenbank rechnen. Bilder werden getrennt auf der Festplatte gespeichert, es wird also eine größere Festplatte benötigt.

<span id="How do I upgrade GRAMPS?">

### Wie aktualisiere ich Gramps?

</span> Aktualisierungen beginnen damit, dass du [Sicherungen](wiki:De:Wie_erstelle_ich_eine_Sicherung) von ALLEN deinen Bäumen machst. Schau dir außerdem die Liste [Backup-Auslassung](wiki:Template:Backup_Omissions/de) an, um festzustellen, welche zusätzlichen Elemente du archivieren möchtest. (Die wichtigsten Punkte sind der Datenbankpfad, der Sicherungspfad und der relative Medienpfad in den Voreinstellungen. Wenn du deine Daten nach einer Aktualisierung nicht mehr finden kannst, wirst du sehr unglücklich sein).

Sobald die Sicherungen sicher gespeichert sind, ist die sicherste Vorgehensweise für eine Aktualisierung: Herunterladen des neuesten Installationsprogramms, Deinstallation des vorhandenen Gramps und Neuinstallation mit dem Installationsprogramm.

Starte Gramps (das erste Laden wird langsam sein, da es die Python-Quellcode-Dateien neu kompiliert und zwischenspeichert). In den " Bearbeiten -\> Einstellungen..." gib deinen Medienpfad auf der Registerkarte "Allgemein", den Datenbankpfad auf der Registerkarte "Stammbaum" und das Backup auf der Registerkarte "Stammbaum" ein. Versuche, deinen Stammbaum über das Menü Stammbäume zu laden.

Wenn es sich um eine "kleinere" Aktualisierung handelt (die nur Fehlerbehebungen enthält), sollte die Aktualisierung deine Konfiguration und Zusatzmodule ohne weiteren Aufwand finden. Wenn es sich um ein Upgrade handelt, musst du alle deine Konfigurationsanpassungen zurücksetzen und die kompatiblen Zusatzmodule herunterladen.

## Einstellungen

### Kann ich die Daten in Berichten in 'Tag Monat Jahr' ändern?

Ja, ändere in den Präferenzen ( im Reiter ) das von Gramps in das gewünschte Format (z.B. JJJ-MM-TT oder Tag Monat Jahr) und erstelle den Bericht. Deine globalen Datums Einstellungen werden verwendet.

### Gibt es einen dunklen Modus?

Nur durch die Installation der Erweiterung [Themes](wiki:Addon:ThemePreferences), die eine Registerkarte zu hinzufügt. Diese Erweiterung ist hilfreich, wenn du Probleme mit der Lichtempfindlichkeit hast oder wenn du einen dunklen Modus für die Nacht oder ganz allgemein bevorzugst. Auf der Registerkarte Thema kannst du die Option "" aktivieren, die für die meisten Themen verfügbar ist. Du kannst auch die Schriftgröße erhöhen, um die Ermüdung beim Lesen zu verringern.

## Zusammenarbeit-Übertragbarkeit

### Ist Gramps mit anderen Ahnenforschungsprogrammen kompatibel?

Gramps versucht kompatibel mit [GEDCOM](http://wiki-de.genealogy.net/GEDCOM), dem allgemeinen Standard beim speichern genealogischer Informationen, zu sein. Es gibt Import- und Exportfilter, die es Gramps ermöglichen GEDCOM-Dateien zu lesen und zu schreiben.

Es ist wichtig zu verstehen, dass der GEDCOM-Standard nur schwach implementiert ist -- praktisch jede genealogische Software hat einen eigenen "Dialekt" von GEDCOM. Sobald wir von einem neuen Dialekt hören, können die Import- und Exportfilter sehr schnell erstellt werden. Aber um unbekannte Dialekte zu finden benötigen wir [Rückmeldungen vom Anwender](wiki:De:Kontakt). Bitte informiere uns über GEDCOM-Dialekte, die nicht von Gramps unterstützt werden, und wir werden unser Bestes tun, um sie zu unterstützen!

Es gibt einen eigenen Artikel dieses Wikis, der sich mit [Gramps und GEDCOM](wiki:Gramps_and_GEDCOM) beschäftigt. Es gibt auch einen Artikel über die bekannten Eigenheiten von [GEDCOM-Dialekte beim Import aus einem anderen Programm](wiki:De:Import_aus_einem_anderen_Genealogieprogramm).

### Kann Gramps von anderen Genealogieprogrammen erstellte Dateien lesen?

Ja Gramps kann GEDCOM-Dateien lesen, die von anderen Genealogie-Programmen erstellt wurden.

- [Siehe oben.](wiki:De:Gramps_6.0_Wiki_Handbuch_-_FAQ#Ist_Gramps_mit_anderen_Ahnenforschungsprogrammen_kompatibel.3F)

### Kann Gramps Dateien schreiben die andere Genealogierogrammen lesen können?

Ja kann GEDCOM-Dateien schreiben, die von anderen Genealogie-Programmen gelesen werden können.

- [Siehe.](wiki:De:Gramps_6.0_Wiki_Handbuch_-_FAQ#Ist_Gramps_mit_anderen_Ahnenforschungsprogrammen_kompatibel.3F)

### Welche Standards unterstützt Gramps?

Eine nette Tatsache über Standards ist, dass es nie zu wenige davon gibt :-). Gramps wurde getestet, um die folgenden Dialekte von GEDCOM zu unterstützen: GEDCOM5.5, Brother's Keeper, Family Origins, Familty Tree Maker, Ftree, GeneWeb, Legacy, Personal Ancestral File, Pro-Gen, Reunion und Visual Genealogie.

### Wie importiere ich Daten aus einem anderen Genealogieprogramm nach Gramps?

Der beste Weg ist, einen neuen Stammbaum zu erstellen und die Import Option im Dateimenü zu wählen. Hier wählst du die GEDCOM-Datei, die du mit dem anderen Programm erstellt hast, und importierst sie.

### Kann ich Gramps auf einen Linux Webserver installieren und es über einen Webbrowser verwenden?

Dies würde meinen Verwandten weltweit den Zugriff und das aktualisieren ermöglichen.

Während Gramps Webseiten erstellen kann, bietet es keine Webschnittstelle, die das Bearbeiten ermöglicht. Wenn dies eine Anforderung ist, dann sind [GeneWeb](http://geneweb.org) oder [webtrees](http://webtrees.net) Programme, die mehr deinen Anforderungen entsprechen. Schau dir außerdem das experimentelle [gramps-connect](wiki:GEPS_013:_Gramps_Webapp) an. Dennoch solltest du dir folgende Fragen stellen:

1.  Will ich wirklich, das Verwandte oder andere Personen meine genealogische Datenbank direkt bearbeiten?
2.  Vertraue ich bedingungslos ohne Überprüfung allen Daten die Personen eingeben könnten?
3.  Habe diese Personen das selbe Verständnis von gutem genealogischen fachlichen Vorgehen wie ich?

Ein besserer Ansatz kann das Bereitstellen einer Webformularschnittstelle sein, die es anderen ermöglicht, Daten einzugeben, die dann für deine Überprüfung bereitgestellt werden. Du kannst dann entscheiden, ob die Informationen in deine Datenbank aufgenommen werden.

Es empfiehlt sich außerdem zu bedenken, welche Auswirkungen ein möglicher Ausfall deiner Seite hat, wenn du dir hochwertigen Webhosting Service leisten kannst.

### Wie kann man zwei Versionen von Gramps gleichzeitig auf einem Rechner ausführen?

Dies kann mit Virtualisierungssoftware wie Virtualbox durchgeführt werden.

Siehe:

- [Verschiedene Gramps-Versionen parallel ausführen](wiki:Run_different_Gramps_versions_parallel)

## Berichte

### Kann Gramps einen Stammbaum meiner Familie drucken?

Ja. Verschiedene Leute haben verschiedene Ansichten, was ein Stammbaum ist. Manche denken an eine Tafel, ausgehend von dem am weitesten entfernten Ahnen, die alle seine/ihre Nachkommen und deren Familien auflistet. Anderen denken an eine Tafel, die von der Person aus zurück in der Zeit geht und alle Ahnen und deren Familien auflistet. Noch andere Leute denken an eine Tabelle, einen Textbericht usw.

Gramps kann alle oben genannten und viele weitere Tafeln und Berichte produzieren. Darüber hinaus ermöglicht die Zusatzmodularchitektur es dem Anwender (dir) eigene Zusatzmodule zu erstellen, welche neue Berichte, Tafeln oder Forschungswerkzeuge sein können.

### Wie kann die Beziehung zwischen Menschen am Baum bestimmt werden?

Einige Benutzer sind daran interessiert, nur direkte genetische Beziehungen zwischen Vorfahren oder Nachkommen anzuzeigen. Andere Benutzer sind ebenfalls an seitlichen Linien (Cousins!) oder unmittelbaren Schwiegereltern interessiert. Und noch andere Benutzer sind daran interessiert, wie die indirektsten Verbindungen eine Gemeinschaft beeinflussen.

Daher bietet Gramps eine ständig wachsende Auswahl an Werkzeugen, Berichten und Methoden, um festzustellen, wie Personen in der Datenbank eines Baums verbunden sind. Nach einer Diskussion über den Gramps-User [Maillist](wiki:Contact#Mailing_lists) wurden die veröffentlichten Vorschläge im Artikel "[Wie finde ich die Beziehung zwischen Menschen?](wiki:How_to_find_the_relationship_between_people)" (englisch) In der Wiki-Kategorie "[Wie mache ich ...](wiki::Category:How_do_I...)" (englisch) zusammengefasst und erläutert.

### In welchen Formaten kann Gramps seine Berichte ausgeben?

Textberichte sind verfügbar in den Formaten HTML, PDF, ODT, LaTex und RTF. Grafische Berichte (Tafeln und Diagramme) sind verfügbar in den Formaten Postscript, PDF, SVG, ODS und [GraphViz](wiki:Output_formats#Graphviz).

### Wie kann ich die Standardsprache in Berichten ändern?

Die Berichte sind in der Sprache deiner Linux Installation. In den meisten Berichten kannst du die auszugebende Sprache auswählen, um nach der Option zu suchen und die für den Bericht zu verwendende Übersetzung auszuwählen. Du kannst sie ändern, indem du zusätzliche Sprachpakete installierst. Weitere Informationen findest du unter [Gewusst wie: Ändern der Sprache von Berichten](wiki:Howto:Change_the_language_of_reports) (englisch).

### Ist Gramps mit dem Internet kompatibel?

Ja, auf verschiedene Weise. Es gibt Funktionen zum Verweisen auf direkt verlinkte externe Daten, Archivierungstools, um sie im internen Speicher zu sammeln, und obwohl Gramps als lokale Anwendung konzipiert ist, wurden zahlreiche Werkzeuge entwickelt, um einige oder alle deine Recherchen im Internet zu veröffentlichen.

Gramps kann Internetadressen speichern und sie im Browser aufrufen. Es kann Daten importieren, die du aus dem Internet herunter geladen hast. Es kann Daten exportieren, die du über das Internet versenden kannst. Gramps ist mit den Standard-Dateiformaten, die häufig im Internet verwendet werden vertraut (z.B. JPEG-, PNG- und GIF-Bilder, MP3-, OGG- und WAV-Audiodateien, Quicktime-, MPEG- und AVI-Videodateien usw.) Wenn dein Browser für den Zugriff auf andere Dateitypen konfiguriert ist, erbt Gramps diese Fähigkeit.

Es gibt Zusatzmodule zur Findung von Hilfsmitteln , die die Suche nach Datensätzen in Online-Quellen unterstützen. Es gibt eine zunehmende Vielfalt anderer [Weblösungen für Gramps](wiki:Web_Solutions_for_Gramps).

Die Berichte können optional Inhalte in Formaten generieren, die für die Veröffentlichung als Webseiten oder sogar als ganze Websites geeignet sind. Und es gibt Entwicklungszweige, die Gramps zu online genealogischen Content-Management-Systemen erweitern. Einige sind dynamische Präsentationssysteme für die Veröffentlichung von Forschungsergebnissen, andere bieten eine begrenzte kollaborative Bearbeitung.

#### Siehe auch

- [Web Solutions for Gramps](wiki:Web_Solutions_for_Gramps)

### Kann ich benutzerdefinierte Berichte/Filter/ was auch immer erstellen?

Ja. Es gibt verschiedene Ebenen der Anpassung. Eine ist die Erstellung oder das Verändern der Vorlagen, die für die Berichte verwendet werden. Dies gibt dir etwas Kontrolle über die Schriftarten, Farben und das Layout der Berichte. Du kannst die Gramps Steuerung in den Berichtdialogen verwenden um festzulegen, welcher Inhalt in einem bestimmten Bericht verwendet werden soll. Zusätzlich hast du die Möglichkeit eigene Filter zu erstellen -- dies ist nützlich beim Auswählen von Personen basierend auf deinen Vorgaben. Du kannst diese Filter kombinieren um neue, komplexere Filter zu erstellen. Schließlich hast du die Möglichkeit eigene Zusatzmodule zu erstellen. Diese können neue Berichte, Forschungswerkzeuge, Import-/Exportfilter usw. sein. Dies setzt aber einige Kenntnisse in der Python-Programmierung voraus.

### Warum werden nicht lateinische Zeichen in PDF/PS Berichten als Müll dargestellt?

Dies ist eine Einschränkung der in den PS und PDF Formaten enthaltenen Zeichensätzen. Um nicht lateinische Texte zu drucken, verwende drucken.. im Formatauswahlmenü des Berichtdialogs. Diese verwendet das `gnome-print` Backend, welches PS und PDF Erstellung genau so wie direktes Drucken unterstützt. (Beachte: Es kann sein, dass du gnome-print separat installieren musst, da es von Gramps nicht benötigt wird).

Wenn du nur lateinischen Text hast, erstellt die PDF Option eine kleine PDF-Datei im Vergleich zu gnome-print, einfach weil keine Zeichensatzinformationen enthalten sind.

### Ich möchte mich an Gramps durch schreiben meines Lieblingsberichts beteiligen. Wie mache ich das?

Der einfachste Weg um sich an Berichten, Filtern, Werkzeugen usw. zu beteiligen, ist es ein bestehenden Gramps Bericht, Filter oder Werkzeug zu kopieren. Wenn du was du möchtest durch modifizieren von bestehenden Code erreichen kannst -- Super! Wenn deine Idee nicht in die Logik irgend eines bestehenden Gramps Werkzeugs passt, musst du dein eigenes Zusatzmodul von Grund auf neu schreiben. Hilfe gibt es im [Entwickler Portal](wiki:Portal:Developers), oder auf der [Entwickler Mailingliste](wiki:De:Kontakt): gramps-devel@lists.sourceforge.net (beides in englisch).

Um deine Arbeit während der Entwicklung zu überprüfen, kannst du dein Zusatzmodul in das Verzeichnis \$HOME/.gramps/plugins speichern und es sollte beim Start gefunden und importiert werden. Ein korrekt geschriebenes Zusatzmodul registriert sich selbst bei Gramps, erzeugt einen Menüeintrag usw.

Wenn du mit deinem Zusatzmodul zufrieden bist und deinen Quellcode zum Gramps-Projekt beitragen möchtest, bist du eingeladen es zu tun, indem du uns unter gramps-devel@lists.sourceforge.net kontaktierst.

## Datenbank - Gramps Dateiformate

Das Standarddateiformat ist [Gramps XML](wiki:Gramps_XML) (englisch). Es wird für Exporte, Sicherungen und Importe verwendet und bewahrt Ihre eingegebenen genealogischen Daten ohne Datenverlust im Vergleich zum GEDCOM-Format.

### Was ist die maximale Datenbankgröße (Bytes) mit der Gramps arbeiten kann?

Gramps hat keine festen Begrenzungen für die Größe einer Datenbank die es handhaben kann. Seit Version 2.0.0 lädt Gramps die Daten nicht mehr komplett in den Arbeitsspeicher, was es ermöglicht mit einer erheblich größeren Datenbank als vorher zu arbeiten. In der Realität gibt es aber faktische Begrenzungen. Den größten Einfluss haben der verfügbare Speicher auf dem System und die Cachegröße die für den BSDDB Datenbankzugriff verwendet wird. Mit üblichen Speichergrößen dieser Tage sollte Gramps keine Probleme mit Datenbanken mit [Millionen von Personen](wiki:Gramps_Performance#JohnBoyTheGreat_2019-12.2C_version_6.0.1) (englisch) haben.

### Wie viele Personen kann die Gramps Datenbank handhaben?

Siehe oben. Nochmal, das hängt davon ab wie viel Speicher du hast, siehe [Gramps Leistungsfähigkeit](wiki:Gramps_Performance) (englisch).

### Meine Datenbank ist wirklich groß. Gibt es einen Weg nicht alle Daten in den Arbeitsspeicher zu laden?

Seit Version 2.0.0 lädt Gramps die Daten nicht mehr komplett in den Arbeitsspeicher was es ermöglicht mit einer erheblich größeren Datenbank als vorher zu arbeiten. Das Dateiformat welches verwendet wird ist `.grdb` es bedeutet Gramps Datenbank.

### Kann ich Gramps mit einer Datenbank auf einem NFS-Share ausführen?

Ja, du kannst eine Gramps-Datenbank von einer [NFS-Freigabe (NetworkFile System)](https://de.wikipedia.org/wiki/Network_File_System) ausführen.

### Was bedeutet "portabel"?

Eine Gramps 3 Datenbank (und jede .grdb Datei) ist sehr von der Programmversion, mit der sie erstellt wurde, abhängig. Zum Beispiel kannst du deine Gramps Daten in diesem Format nicht einfach auf ein anderes Betriebssystem übertragen (oder eine andere Version eines Betriebssystems) und erwarten, das du deine Daten lesen kannst. Die Daten sind nicht "portabel". Daher kannst du nicht einfach auf Sicherungen in diesem Format vertrauen, du solltest gleichzeitig deine Daten in ein portables Format exportieren. Es gibt zwei mögliche portable Formate: GEDCOM und Gramps XML (.gramps oder .gpkg). Aber nur Gramps XML wird empfohlen, da es originalgetreu all deinen Daten speichert.

### Warum ist das Datenbankformat (GRDB) nicht portabel?

Das größte Problem mit der Portabilität von Gramps liegt bei den "Transaktionen". Mit Gramps 2.2 haben wir um die Daten zu schützen die Unterstützung von "atomaren Transaktionen" (atomic transactions) eingeführt. Mit "atomaren Transaktionen" werden mehrere Änderungen als eine Einheit übergeben. Entweder alle Änderungen schaffen es oder keine der Änderungen schafft es. Du gelangst nie in eine Situation in der nur ein Teil der Änderungen durchgeführt wurde. Ein weiterer Vorteil von der Verwendung von Transaktionen ist, dass der Datenbankzugriff (lesen und schreiben) schneller ist.

Das Problem mit Transaktionen (zumindest bei der Verwendung von BSDDB) das es nicht möglich ist, alle Daten in einer Datei zu speichern. Es werden Protokolldateien benötigt, um Dinge nachverfolgen zu können. Diese Protokolldateien werden in einem Verzeichnis der DB Umgebung aufbewahrt. Wir benötigen ein extra Verzeichnis für jede Datei, sonst könnten sich die Protokolldateien gegenseitig stören.

In 2.2 haben wir die Protokolldateien unter ~/.gramps/<Pfad>Verzeichnis gespeichert, für jede Datenbank wurde ein extra Verzeichnis angelegt. Das Problem ist, das deine GRDB Datei die Protokolldateien benötigt, die sich in einem anderen Verzeichnis befinden.

Kopieren der GRD Dateien kopiert nur einen Teil der Datenbank.

### Hat Gramps einen Beispielbaum?

Ja tut es. Mehrere Beispiel-Stammbaumdatenbanken sind [in den meisten Installationen von Gramps enthalten und können zum Durcharbeiten von Tutorials und zum sicheren Erkunden von Tools oder Funktionen importiert werden](wiki:Example.gramps#Load_example.gramps).

Die beispielhafte Stammbaumdatenbank (**`example.gramps`**-Datei) versucht das Ideal, zumindest ein Beispiel für sogar die obskuren Dinge zu haben, die Gramps macht. Du kannst das Beispiel in einen leeren Baum importieren und dann sicher destruktive Erkundungsfehler in einer Wegwerf-Arbeitsdatenbank machen. Und wenn du vermutest, dass du ein Problem (auch bekannt als 'Bug') in Gramps entdeckt hast, kannst du die gleiche Operation zuerst mit dem Beispiel-Stammbaum versuchen und dann [einen Fehlerbericht einreichen](wiki:How_to_create_a_good_bug_report).

- Der [<code>Example.gramps</code> Wiki-Artikel](wiki:Example.gramps) beschreibt, wo du die Beispiel-Stammbaum-Archivdatei findest, wie man sie verwendet und schlägt einige alternative Dateien vor.

## Fehler und Anforderungen

### Was mache ich wenn ich einen Fehler gefunden habe?

Das Beste was du tun kannst ist den Fehler zu beheben und den Patch an gramps-devel@lists.sourceforge.net zu schicken :-)

Wenn das nicht möglich ist, solltest du einen [Fehlerbericht erstellen](wiki:Using_the_bug_tracker)

Ein guter Fehlerbericht sollte enthalten:

1.  Die Version von Gramps, die du verwendet hast, als du auf den Fehler gestoßen bist (verfügbar durch den Hilfe - Info-Menüeintrag).
2.  Die Sprache, unter der Gramps ausgeführt wurde (verfügbar durch das Ausführen von `echo $LANG` in deinem Terminal).
3.  Die Symptome, die zeigen, dass es sich um einen Fehler handelt.
4.  Zurückverfolgungsnachrichten, Fehlermeldungen, Warnungen usw., die in deinem Terminal auftreten oder in einem separaten Zurückverfolgungsfenster.

Die meisten Probleme können sehr schnell gelöst werden, vorausgesetzt es gibt genügend Informationen. Um dies sicher zu stellen verfolge deine Fehlerberichte. Dann haben wir eine Möglichkeit, dich zu kontaktieren falls wir weitere fragen haben.

### Anforderungen

- Gramps sollte eine .... Anwendung sein

Es ist offensichtlich, dass Gramps unbedingt eine (client-server/web-based/PHP/weblog/Javascript/C++/verteilte/KDE/Motif/Tcl/Win32/C#/was auch immer) Anwendung werden muss. Wann wird das passieren?

Der sicherste Weg, es wahr werden zu lassen ist, dass du es selber machst. Weil Gramps Open Source ist, wird niemand dich daran hindern den Quellcode zu nehmen und seine Entwicklung in die Richtung, die du möchtest weiterzuführen. Wenn du das machst, solltest du deinem Projekt einen neuen Namen geben, um Verwirrung mit der weitergehenden Gramps-Entwicklung zu verhindern. Wenn du dem GRAMPS-Projekt Ratschläge, Filter usw. geben willst, werden wir mit deinem Projekt zusammenarbeiten, um Kompatibilität und Import/Export-Möglichkeiten zu deinem neuen Projekt zu bewahren.

Wenn du aber möchtest, dass das Gramps-Projekt deine Strategie übernimmt, solltest du die Gramps-Entwickler überzeugen, dass deine Strategie für Gramps gut und der aktuellen Entwicklungsstrategie überlegen ist.

## Meine Datenbank erweitern und bearbeiten

### Was ist der Unterschied zwischen einem Wohnort und einer Adresse?

Ein Wohnort ist ein Ort, wo jemand für eine bestimmte Zeit gelebt hat. Eine Adresse ist der Name eines Wohnorts in dem Format wie es von der Post erwartet wird. Dafür kann jeder Wohnort eine Adresse haben, wenn dies sinnvoll ist. Siehe auch: [Warum Wohnort-Ereignis und nicht Adresse?](wiki:De:Warum_Wohnort-Ereignis_und_nicht_Adresse?)

### Wie ändere ich die Reihenfolge von Kindern?

Kinder können verschoben werden im [Familieneditor](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Daten_eingeben_und_bearbeiten:_Ausführlich_-_Teil_1#Informationen_.C3.BCber_Beziehungen_bearbeiten) durch [Drag & Drop](http://de.wikipedia.org/wiki/Drag_and_Drop) oder verwenden der und Schaltflächen.

Alternativ installiere

- die Erweiterung von Drittanbietern, das Werkzeug, das Massenaktualisierungen der Reihenfolge der Kinder ermöglicht.

### Wie ändere ich die Reihenfolge von Partnern?

Ehepartner (die in verschiedenen Teilen des Wikis auch als Beziehung oder Familie aufgeführt sind) können in der Ansicht der [Beziehungenkategorie](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Kategorien#Beziehungenkategorie) neu geordnet werden, indem du die Schaltfläche in der Symbolleiste oder den Menüpunkt wählst. Alternativ dazu listet die Registerkarte Ereignisse beim Bearbeiten einer Person für jeden Ehepartner eine ausklappbare Familie auf. Wenn es mehrere Familien gibt, kannst du eine Familie auswählen und auf die Schaltfläche Aufwärts oder Abwärts unter den Registerkartenüberschriften klicken, um die ausgewählte Familie neu anzuordnen.

### Wie füge ich einen zusätzlichen Ehepartner hinzu?

Siehe [Einen Partner hinzufügen](wiki:De:Einen_Partner_hinzufügen)

### Wie entferne ich einen Ehepartner?

Um einen Ehepartner zu entfernen (ohne das Personenprofil aus dem Baum zu löschen), genügt ein einziger Klick im Dialogfeld [Familie bearbeiten](wiki:De:Gramps_Glossar#Familie). Klicke einfach auf die Schaltfläche "Person als Mutter/Vater entfernen" (-) direkt über dem Namen des Ehepartners.

Die Felder "Name", "Geburt" und "Tod" werden gelöscht und die Schaltflächen "Eine neue Person als Mutter/Vater hinzufügen" (+) und "Gemeinsame Personenauswahl" ersetzen die Schaltflächen (-) und "Bearbeiten".

Um den Ehepartner vollständig aus dem Stammbaum zu entfernen, wähle die Person in der Personenansicht aus und klicke auf die Schaltfläche "Ausgewählte Person löschen" (-) in der Werkzeugleiste. Ein Bestätigungsdialog wird angezeigt. Bestätige, indem du auf die Schaltfläche "Person löschen" klickst.

Die Person wird aus allen Familien entfernt, in denen sie ein Ehepartner oder ein Kind ist. Die zugehörigen Ereignisse, Zitate, Notizen und Medien werden verwaist. Die anderen sekundären Objekte werden zusammen mit der Person gelöscht.''

### Wie fügt man einem Element Fotos hinzu?

Siehe [Fotos und andere Medien Objekte hinzufügen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Daten_eingeben_und_bearbeiten:_Kurz#Fotos_und_andere_Medien_Objekte_hinzuf.C3.BCgen).

### Wie findest du nicht verwendete Medien?

Medien, die keinem Objekt zugeordnet wurden, können durch Erstellen eines [benutzerdefinierten Filters](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Filter#Benutzerdefinierte_Filter) in der Ansicht Medienkategorie gefunden werden. Verwende die [Medienobjekte mit einer Anzahl von Referenzen von <Anzahl>](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Filter#Medienobjekte_mit_einer_Anzahl_von_Referenzen_von_.3CAnzahl.3E), um Medien mit weniger als einer Referenz zu suchen.

### Wie kann ich eine Genealogie-Website mit Gramps veröffentlichen?

<span id="How can I publish web sites generated by GRAMPS?"> Gramps bietet im Menü "Berichte" mehrere Optionen zum Erstellen von Webseiten basierend auf Ihren Baumdaten.

Das Tutorial: [Erstellen einer Genealogie-Website mit dem Gramps](wiki:Howto:_Make_a_genealogy_website_with_Gramps)-Lernprogramm (englisch) beschreibt die Verwendung des Berichts [Erzählende Website](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte_-_Teil_7#Erz.C3.A4hlende_Website) (aka NarrativeWeb). Darin lernen Sie, eine Website für eine Reihe von Personen in Ihrem Stammbaum zu erstellen.

Nach der Generierung kannst du die Webdateien auf einen Hosting-Service hochladen. Du kannstz sie auch auf einem tragbaren USB-Stick oder einem anderen Medium verteilen.

#### Siehe auch

- [Web Solutions for Gramps](wiki:Web_Solutions_for_Gramps)

</span>

- Du kannst auch Zusatzmodule-Berichte von Drittanbietern installieren, um andere Arten von Webinhalten zu erstellen. Siehe die [Addons-Liste](wiki:6.0_Addons#Addon_List).

{{-}}

## Die FAQ lösen mein Problem nicht.

Bitte zögere nicht, uns über eine der auf der Seite "[Kontakt](wiki:De:Kontakt)" aufgeführten offiziellen Methoden zu kontaktieren. {{-}}

[F](wiki:Category:De:Dokumentation)
