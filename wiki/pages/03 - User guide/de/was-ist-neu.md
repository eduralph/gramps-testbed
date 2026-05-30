---
title: De:Gramps 6.0 Wiki Handbuch - Was ist neu?
categories:
- De:Dokumentation
managed: false
source: wiki-scrape
wiki_revid: 127804
wiki_fetched_at: '2026-05-30T18:12:29Z'
lang: de
---

{{#vardefine:chapter\|1}} {{#vardefine:figure\|0}}

Dieser Abschnitt gibt einen Überblick über die Änderungen seit der Version 5.2 von Gramps. Dies ist eine "Verbesserungs"-Version. Die Änderungen umfassen also sowohl neue Funktionen als auch Fehlerbehebungen. Diese Änderungen sind auch detailliert weiter hinten hier im Handbuch enthalten. Anwendern die von von früheren Gramps Versionen aktualisieren, wird empfohlen, diesen Abschnitt in älteren [Handbüchern](wiki:De:Handbuch) durchzusehen, um keine neuen Möglichkeiten zu übersehen, wenn sie beginnen mit Gramps 6.0 zu arbeiten. Suche nach dem Blitz der "" markierten Abschnitte.

### vorläufige Changeliste

**Die Gramps-Dokumentation wird von Freiwilligen erstellt, daher wird die Benutzerdokumentation schrittweise ‘'nach'‚ der Veröffentlichung der Version veröffentlicht.** (Ausgewählte wichtige Elemente werden in der Dokumentation mit "''</small>" gekennzeichnet, um die Suche zu erleichtern.) Die Wiki-Mitwirkenden schreiben nicht nur aus ihrer Erfahrung mit den Funktionen, sondern auch unter Berücksichtigung der Entwicklungsziele, Funktionsanfragen, Statusberichte und Pull-Request-Notizen. Wenn du ebenfalls ein Forscher bist, findest du in den folgenden Ankündigungen teilweise Links zu diesen Referenzdokumenten. Erkunde die Funktionen nach Belieben und teile deine Erfahrungen, um anderen zu helfen.

#### Aus den Ankündigungen

Aus dem Bereich **[Ankündigungen](https://gramps.discourse.group/c/gramps-announce/5)** des englisch sprachigen **[Gramps Community Support Discourse Forums](https://gramps.discourse.group/t/welcome-to-the-gramps-discourse-forum/7)**:

- [6.0.5](https://github.com/gramps-project/gramps/releases/tag/v6.0.5) - eine neue Wartungsversion, veröffentlicht am 2025-09-06.
- [6.0.4](https://github.com/gramps-project/gramps/releases/tag/v6.0.4) - eine neue Wartungsversion, veröffentlicht am 2025-08-10.
- [6.0.3](https://github.com/gramps-project/gramps/releases/tag/v6.0.3) - eine neue Wartungsversion, veröffentlicht am 2025-06-18.
- [6.0.2](https://github.com/gramps-project/gramps/releases/tag/v6.0.2) - eine neue Wartungsversion, veröffentlicht am 2025-06-15.
- [6.0.1](https://github.com/gramps-project/gramps/releases/tag/v6.0.1) - eine neue Wartungsversion, veröffentlicht am 2025-04-18.
- [6.0.0](https://github.com/gramps-project/gramps/releases/tag/v6.0.0) - eine neue Hauptversion, veröffentlicht am 2025-03-19.
- [v6.0.0-rc1](https://github.com/gramps-project/gramps/releases/tag/v6.0.0-rc1) - eine experimentelle Vorabversion, veröffentlicht am 2025-03-16
- [v6.0.0-beta2](https://github.com/gramps-project/gramps/releases/tag/v6.0.0-beta2) - eine experimentelle Vorabversion, veröffentlicht am 2025-03-03
- [v6.0.0-beta2](https://github.com/gramps-project/gramps/releases/tag/v6.0.0-beta2) - eine experimentelle Vorabversion, veröffentlicht am 2025-02-13
- [v6.0.0-beta1](https://github.com/gramps-project/gramps/releases/tag/v6.0.0-beta1) - eine experimentelle Vorabversion, veröffentlicht am 2025-02-05

Diskussionen mit den Entwicklern über die zukünftige Version 6.0:

- [6.0 verstehen](https://gramps.discourse.group/t/understanding-gramps-6-0/6652Gramps) Von Doug Blank - Entwicklung - Roadmap

<!-- -->

- Verbesserung der Benutzerfreundlichkeit der Symbolleiste zeigt standardmäßig Text unter den Symbolen an [1](https://gramps.discourse.group/t/gramps-6-0-defaults/6990/3)

## Bevor du aktualisierst

***Bevor*** du aktualisierst, stelle sicher, dass du eine Sicherung deiner Stammbaumdaten besitzt. Die beste Möglichkeit dies zu tun ist folgende:

1.  Starte deine vorhandene Version von Gramps (Gramps 4.2/5.0/5.1/5.2)
2.  öffne deinen Stammbaum
3.  sichere den Stammbaum in das *gramps xml* Format oder das *gramps xml Paket* Format (das *gramps xml Paket* enthält deine Mediendateien). Dies geht über das Menü , stelle sicher, dass du **alle Daten sicherst**, schränke die Datensicherung in keiner Weise ein.
4.  Schließe den Stammbaum und wiederhole die obigen Schritte mit all deinen Stammbäumen
5.  Bewahre die resultierende(en) Datei(en) an einem sicheren Ort auf

Für mehr Informationen siehe [Einen Stammbaum sichern](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Stammb%C3%A4ume_Verwalten#Einen_Stammbaum_sichern). Beachte [was in einer Sicherung nicht enthalten ist](wiki:Template:Backup_Omissions/de).

Nachdem du deine Daten gesichert hast, installiere Gramps 6.0. Die Verwendung des hierfür für dein Betriebssystem vorgesehenen Prozess stellt in den meisten Fällen sicher, das Gramps 6.0 nicht mit deiner älteren Installation kollidiert. Es ist trotzdem sicherer, Gramps 3.4 vor der Installation von Gramps 6.0 zu deinstallieren oder stelle sicher, dass du Gramps 6.0 in einem anderen Verzeichnis installierst. Dies ist immer notwendig, wenn du aus den Quellcode installierst. Für mehr Informationen zur Installation von Gramps 6.0 schau bitte auf [Neueste Gramps Version herunterladen](wiki:De:Download)

Nachdem du Gramps 6.0 installiert hast, kannst du direkt deine alten Stammbäume öffnen und mit der Arbeit fortfahren. Im Falle von Problemen (z.B. nach einer kompletten Systemaktualisierung), importiere die Sicherungsdatei, die du weiter oben erstellt hast um deinen Stammbaum wieder herzustellen.

## Sichtbare Änderungen am Kern

Sichtbare Änderungen nach der Migration: Interface, Daten.

### Datenmodell

Details zu Änderungen am [Datenmodell](wiki:Gramps_Data_Model) (sofern vorhanden):

1.  Keine Änderungen

<hr>

- Ein Stammbaum **kann nicht in** in Gramps 3.4/4.0/4.1/4.2 und Gramps 6.0 ohne Aktualisierung bzw. Herabstufung geöffnet werden.

<!-- -->

- Ein Downgrade kann nur durch Exportieren von XML und Importieren in die vorherige Version erreicht werden.

<!-- -->

- Eine Gramps XML erstellt mit Gramps 3.4/4.0/4.1 ist **nicht identisch** mit einer in Gramps 6.0 erstellten.

<!-- -->

- Gramps 6.0 ist jetzt nur noch **Python3**

Siehe [detaillierte Änderungen](wiki:Database_Formats#Detailed_Changes) (englisch) für mehr Details über die interne Datenbank.

### Primäre Änderungen

- SQLite ist jetzt das Standard-Datenbank-Backend und nicht mehr BSDDB. Sie können weiterhin [alternative Datenbank](wiki:Relational_database_comparison) Backends verwenden. BSDDB bleibt als Standardalternative verfügbar. Für Power-User stehen PostgreSQL und MongoDB als experimentelle Addons von Drittanbietern zur Verfügung.

Die Entwickler glauben, dass SQLite möglicherweise weniger Datenbankbeschädigungen aufweist, die eine einfache Wiederherstellung verhindern.

- 

### GUI

- 

### Orte

- Möglichkeit, bei der Auswahl des Ortes nach alternativen Ortsnamen zu suchen

### Berichte, Werkzeuge, Gramplets

- 

### Import/Export

- 

### Neue Erweiterungen

- 

## Änderungen unter der Haube

Technischer Änderungen

- Zahlreiche Änderungen in Bezug auf die Unterstützung anderer Datenbank-Backends (SQLite, PostgreSQL, MongoDB usw.).

### Abhängigkeiten

## Weitere Informationen

### Verschiedenes

### Lokalisierung

- Aktualisierte Übersetzungen:

#### Erweiterungen von Drittanbietern

- [Weblate für Erweiterungen von Drittanbietern Übersetzung](https://gramps.discourse.group/t/weblate-translation-for-addons-experiment-needs-testers/6964)

### Fahrplan

- Lies die Versionshinweise für [frühere Versionen von Gramps](wiki:Previous_releases_of_Gramps) (englisch)
- Siehe projizierte Elemente im Zusammenhang mit Gramps [nächster Version.](https://gramps-project.org/bugs/roadmap_page.php)
- [Vorschläge zur Verbesserung von Gramps (GEPS)](wiki::Category:GEPS) (englisch) - In der Spalte **Released** findest du neue Elemente, die in Gramps 6.0 implementiert wurden
- [6.0 Roadmap](wiki:6.0_Roadmap) - wiki

### Änderungsprotokoll

- Weitere Informationen zu Gramps 6.0 findest du [6.0](https://gramps-project.org/bugs/changelog_page.php) (englisch) im Gramps Issue Tracker.

<!-- -->

- Weitere Informationen findest du in den Änderungsprotokollen für die Wartungsversionen von Gramps:
  - Gramps [6.0.5](https://github.com/gramps-project/gramps/releases/tag/v6.0.4) (englisch)
  - Gramps [6.0.4](https://github.com/gramps-project/gramps/releases/tag/v6.0.4) (englisch)
  - Gramps [6.0.3](https://github.com/gramps-project/gramps/releases/tag/v6.0.3) (englisch)
  - Gramps [6.0.2](https://github.com/gramps-project/gramps/releases/tag/v6.0.2) (englisch)
  - Gramps [6.0.1](https://github.com/gramps-project/gramps/releases/tag/v6.0.1) (englisch)
  - Gramps [6.0.0](https://github.com/gramps-project/gramps/releases/tag/v6.0.0) (englisch)
  - Gramps [6.0.0-rc2](https://github.com/gramps-project/gramps/releases/tag/v6.0.0-rc2)
  - Gramps [6.0.0-rc1](https://github.com/gramps-project/gramps/releases/tag/v6.0.0-rc1)
  - Gramps [6.0.0-beta2](https://github.com/gramps-project/gramps/releases/tag/v6.0.0-beta2)
  - Gramps [6.0.0-beta1](https://github.com/gramps-project/gramps/releases/tag/v6.0.0-beta1)

Verleich der GitHub Commits von \[<https://github.com/gramps-project/gramps/compare/v5.2.4>...v6.0.1 Gramps 5.2.4 zu 6.0.1\] {{-}}

### Was war *einmal* neu

Die Seite [Vorherige Version](wiki:Previous_releases_of_Gramps) (englisch) enthält Links zu Aufzählungslisten mit Änderungen in Hauptversionen und Wartungsversionen im Laufe der Jahre.

Allerdings, die **Was ist neu?** Seiten in der ersetzten Version des Wiki-Handbuchs für jede Hauptversion können detailliertere Informationen enthalten:

- [Version 5.2](wiki:De:Gramps_5.2_Wiki_Handbuch_-_Was_ist_neu%3F)
- [Version 5.1](wiki:De:Gramps_5.1_Wiki_Handbuch_-_Was_ist_neu%3F)
- [Version 5.0](wiki:De:Gramps_5.0_Wiki_Handbuch_-_Was_ist_neu%3F)
- [Version 4.2](wiki:De:Gramps_4.2_Wiki_Handbuch_-_Was_ist_neu%3F)
- [Version 4.1](wiki:De:Gramps_4.1_Wiki_Handbuch_-_Was_ist_neu%3F)
- [Version 4.0](wiki:De:Gramps_4.0_Wiki_Handbuch_-_Was_ist_neu%3F)
- [Version 3.4](wiki:De:Gramps_3.4_Wiki_Handbuch_-_Was_ist_neu%3F)
- [Version 3.3](wiki:De:Gramps_3.3_Wiki_Handbuch_-_Was_ist_neu%3F)
- [Version 3.2](wiki:De:Gramps_3.2_Wiki_Handbuch_-_Was_ist_neu%3F)

Eine kompakte Übersicht der Verbesserungen wurde erstmals 2010 in das Handbuch aufgenommen. In den ersten drei Jahren des Wikis musste das gesamte Handbuch überprüft werden.

### Handbuch zum Herunterladen

Version 6.0 – Handbuch zum Herunterladen

- [Deutsch PDF](wiki::File:Gramps6.0UserManual_de.pdf)
- [English PDF](wiki::File:Gramps6.0UserManual.pdf)

Wir führen auf dieser Seite nicht jede einzelne Fehlerbehebung oder kleinere Verbesserung auf. Um eine vollständige Liste der Änderungen zu erhalten, solltest du dir die [Commit-Historie](https://github.com/gramps-project/gramps/commits/maintenance/gramps60) für jede Version ansehen. {{-}}

[W](wiki:Category:De:Dokumentation)
