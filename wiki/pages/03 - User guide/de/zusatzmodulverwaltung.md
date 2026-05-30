---
title: De:Gramps 6.0 Wiki Handbuch - Zusatzmodulverwaltung
categories:
- De:Dokumentation
- Plugins
managed: false
source: wiki-scrape
wiki_revid: 130851
wiki_fetched_at: '2026-05-30T18:13:47Z'
lang: de
---

{{#vardefine:chapter\|9}} {{#vardefine:figure\|0}} Über den Dialog kannst du steuern, wie Gramps Plugins und Add-ons von Drittanbietern verwaltet. Gramps besteht aus einem Kern und vielen Plugins. Beim Start von Gramps wird der Kern geladen und nur eine begrenzte Anzahl von Plugins. Das verkürzt die Startzeit und verringert den Speicherbedarf von Gramps. Anschließend werden viele Plugins bei Bedarf automatisch von Gramps geladen, sodass viele Benutzer sich der Existenz von Plugins oder deren verzögertem Laden nicht bewusst sein müssen.

Der -Dialog ist über das Menü +1}}}} "Registrierte Zusatzmodule" Registerkarte (Entwicklermodus)\]\]

Hier siehst du eine Liste aller Zusatzmodule, die Gramps gefunden hat. Dies sind Zusatzmodule, die Teil von Gramps sind genauso wie Zusatzmodule/Erweiterungen im Verzeichnis `gramps60/plugins` welches sich im [Gramps Anwenderverzeichnis](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Anwenderverzeichnis) befindet. Die Art der Zusatzmodule wird in der ersten Spalte angezeigt.

Du kannst ein Zusatzmodul ein- oder ausblenden, indem du eine Zeile auswählst und auf die Schaltfläche klickst. Dies ist nur für die Benutzer-Zusatzmodule sinnvoll.

Wenn du eine Zeile auswählst und darauf doppelklickst oder auf die Schaltfläche drückst, wird das Dialogfeld angezeigt.

Verwende die Schaltfläche , um das Programm zu beenden. Die Schaltfläche ... tut was?

Im [Entwicklermodus](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Zusatzmodulverwaltung#Benutzermodus_oder_Entwicklermodus) werden zwei zusätzliche Schaltflächen angezeigt:

- \- Dadurch wird die Quellcode-Datei der ausgewählten Zeilen in deinem zugehörigen Texteditor geladen.

- \- Erzwingt ein Neuladen des ausgewählten Zusatzmodul/Erweiterung.

{{-}}

### Geladene Zusatzmodule

![[_media/PluginManager-LoadedPlugins-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Geladene Zusatzmodule" Registerkarte (Entwicklermodus)]]

Hier siehst du eine Liste aller Zusatzmodule, die versucht wurden zu laden. Normalerweise werden alle Ansichten (wie Beziehungenkategorie) geladen und alle Gramplets/Berichte/Werkzeuge, die du verwendet hast, werden automatisch geladen.

Wenn eine Fehler während des Ladens des Zusatzmoduls aufgetreten ist, wird der **Status** hier angezeigt. Durch Doppelklicken auf eine Zeile mit einem Fehler wird das Dialogfeld geöffnet, in dem der Fehler im Detail angezeigt wird. Du kannst diese verwenden, um den Autor des Zusatzmoduls oder die Gramps-Fehlerliste zu kontaktieren.

Wenn du später feststellst, dass dir ein Zusatzmodul nicht gefällt, kannst du es als "Verdeckt" markieren und es wird nicht mehr angezeigt.

Du kannst ein Zusatzmodul ein- oder ausblenden, indem du eine Zeile auswählst und auf die Schaltfläche klickst. Dies ist nur für die Benutzer-Zusatzmodule sinnvoll.

Wenn du eine Zeile auswählst und auf die Schaltfläche drückst, wird das Dialogfeld angezeigt.

Verwende die Schaltfläche , um das Programm zu beenden.

Im [Entwicklermodus](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Zusatzmodulverwaltung#Benutzermodus_oder_Entwicklermodus) werden zwei zusätzliche Schaltflächen angezeigt:

- \- Dadurch wird die Quellcode-Datei der ausgewählten Zeilen in deinem zugehörigen Texteditor geladen.

- \- Erzwingt ein Neuladen des ausgewählten Zusatzmodul/Erweiterung.

{{-}}

## Aktionen

### Ausblenden/Aufdecken

Über den -Dialog können Zusatzmodule ein- oder ausgeblendet werden. Einige Menüs zeigen ausgeblendete Erweiterungen nicht an, sodass das Erweiterung nicht ausgewählt werden kann. Wenn beispielsweise ein Gramplet ausgeblendet ist, erscheint es nicht im Kontextmenü , das angezeigt wird, wenn du mit der rechten Maustaste auf den Hintergrund der Hauptregisterkarte Gramplets klickst. Das Ausblenden einiger Erweiterungen (wie Beziehungen oder Gramps-Ansichten) hat jedoch keine Auswirkungen und ist möglicherweise nicht einmal zulässig.

### Detaillierte Informationen Dialog

![[_media/Detailed-Info-dialog-plugin-example-with-context-menu-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Dialogfeld „Detaillierte Informationen“ – Beispiel mit Kontextmenü]]

Das Dialogfeld zeigt Informationen zum ausgewählten Zusatzmodul/Erweiterung an. Über ein Kontextmenü kannst du die Informationen nach Bedarf kopieren und einfügen. Du kannst damit den Zusatzmodul-Autor kontaktieren oder ein Problem an den [Gramps-Bugtracker](wiki:Using_the_bug_tracker) melden.

- *Zusatzmodulname:*
- *Beschreibung:*
- *Version:*
- *Autoren:*
- *E-Mail:*
- *Dateiname:*
- *Standort:*

{{-}}

## Zusatzmodularten

Es gibt zwei Hauptkategorien von Zusatzmodule in Gramps: **[Benutzer-Zusatzmodule](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Zusatzmodulverwaltung#Anwender_Zusatzmodulen)** und System-Zusatzmodule. **Benutzer-Zusatzmodule** sind solche, die du verwendest und steuerst, um dir verschiedene Funktionen zur Verfügung zu stellen. Die **[System-Zusatzmodule](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Zusatzmodulverwaltung#System_Zusatzmodule)** werden von Gramps verwendet.

Es gibt viele Zusatzmodule, die mit Gramps geliefert werden. Allerdings kann jeder auch ein Zusatzmodul schreiben und es teilen. Diese Zusatzmodule von Drittanbietern werden als „Erweiterungen” bezeichnet. Wir ermutigen Benutzer und Entwickler ausdrücklich, ihre Kreationen mit anderen Gramps-Benutzern zu teilen.

Siehe auch:

- [Addon_list_legend#Type](wiki:Addon_list_legend#Type)
- [Addons development](wiki:Addons_development)
  - [Addons_development#What_can_addons_extend.3F](wiki:Addons_development#What_can_addons_extend.3F)

### Anwender Zusatzmodulen

Die folgenden Arten von **Anwender Zusatzmodulen** existieren in Gramps:

1.    
    Unterbauten für die Gramps Berichte erstellen kann (PDF, ODF, ASCII Text, ...).

2.    
    Exportformate in die du deine Daten via exportieren kannst.

3.    
    kleine Programme die du in die Grampletansicht einbinden oder loslösen und als eigenes Fenster verwenden kannst.

4.    
    die Ansichten im Hauptfenster von Gramps.

5.    
    Importformate aus denen du via Daten importieren kannst.

6.    
    Ziele, die in der Orteansicht verwendet werden können um zu einem Internetkartendienst zu gelangen (*Gehe* Werkzeugleistenschaltfläche).

7.    
    kurze Berichte die über die Kontextmenüs in den Listenansichten oder über das Schnellbericht Gramplet verfügbar sind.

8.    
    Schriftliche oder grafische Berichte, die Gramps erstellen kann.

9.    
    Werkzeuge, die du über das Menü starten kannst.

### System Zusatzmodule

Die folgenden Arten von **System Zusatzmodulen** existieren in Gramps:

1.    
    Unterbauten, mit denen Gramps alternative [Datenbanktypen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Einstellungen#Stammbaum) unterstützen kann.

2.    
    Bibliotheken die vorliegen und zusätzliche Funktionalität bieten.

3.    
    Verwandtschaftsrechner für verschiedene Sprachen

4.    
    Regeln für benutzerdefinierte Filter

5.    
    Fundstellenformatierer

6.    
    Erzeugung von Miniaturansichten für die Vorschau von Medien

## Benutzermodus oder Entwicklermodus

Gramps erkennt anhand des [Python-Optionsflags](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Kommandozeilen_Referenz#Python_Optionen) „optimise“, ob es im Benutzermodus oder im Entwicklermodus ausgeführt wird:

- `python -O gramps.py`

Siehe [Debugging Gramps](wiki:Debugging_Gramps) (englisch). {{-}}

[Z](wiki:Category:De:Dokumentation) [Category:Plugins](wiki:Category:Plugins)
