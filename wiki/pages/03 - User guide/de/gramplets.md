---
title: De:Gramps 6.0 Wiki Handbuch - Gramplets
categories:
- De:Dokumentation
- Stub
managed: false
source: wiki-scrape
wiki_revid: 130915
wiki_fetched_at: '2026-05-30T17:47:37Z'
lang: de
---

{{#vardefine:chapter\|12}} {{#vardefine:figure\|0}} Hier beschreiben wir die Funktionen der [Gramplets](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Gramplets#Was_ist_ein_Gramplet.3F), die mit Gramps geliefert werden.

## Was ist ein Gramplet?

<span id="definition"> ![[_media/DashboardCategory-DashboardView-default-gramplets-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Übersicht Kategorie Ansicht (Standard-Gramplets)]]

Ein [Gramplet](wiki:De:Gramps_Glossar#Gramplet) ist eine Erweiterung des Gramps-Programms, die im Idealfall so nahtlos funktioniert, als wäre sie eine Kernfunktion. Sie werden tatsächlich als Teil von Gramps eingebettet. Aber während die Kernfunktionen einer Ansicht fast ständig benötigt werden, erweitern die gebündelten Gramplets die Ansicht auf eine Weise, die nur gelegentlich benötigt wird. Gramplets bieten eine zusätzliche Perspektive auf die Daten des Stammbaums, die sich entweder dynamisch während der Navigation durch den Gramps-Baum ändert oder die Interaktivität mit Ihren genealogischen Daten ermöglicht.

Gramplets sind die Abteilung der Zusatzmodule (auch [Widgets](https://de.wikipedia.org/wiki/Widget#Widget-Engines), Plugins, Addons, Hilfskomponenten genannt), die in der **[Übersichtkategorie](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Kategorien#Übersichtkategorie)** ... oder den **[Seitenleisten](#Die_Bildschirmunterteilung_Seitenleiste_.26_Fu.C3.9Fleiste)** und **[Fußleisten](#Die_Bildschirmunterteilung_Seitenleiste_.26_Fu.C3.9Fleiste)** in anderen Navigator-[Ansichtskategorien](wiki:De:Gramps_Glossar#Ansichtskategorie) zu finden sind. Sie bieten alle möglichen Funktionen, die für den Forscher nützlich sein können.

Eine [Auswahl an eingebauten Zusatzmodulen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Gramplets#Gramplet-Liste) ist mit Gramps gebündelt und vorinstalliert. Das Gramps-Projekt beherbergt eine [Auswahl von zusätzlichen Zusatzmodulen](wiki:6.0_Addons#Addon_List), die möglicherweise nur für bestimmte Zielgruppen von Interesse sind.

Es gibt auch Drittanbieter, wie das Taapeli-Projekt in Finnland, die ihre eigene Auswahl an [Zusatz-Plug-ins der Isotammi-Gruppe](wiki:Addon:Isotammi_addons) bereitstellen, die entwickelt wurden, um Gramps auf ihre Bedürfnisse abzustimmen. Mitglieder der Gramps-Community stellen auch privat oder über GitHub-Repositories spezielle Erweiterungen zur Verfügung. Und natürlich sind die Nutzer [eingeladen, ihre eigenen Erweiterungen zu entwickeln](wiki:Addons_development#Develop_your_addon).</span>

zu deinstallieren.) Geschlossene Gramplets können bei Bedarf wieder zu einer *Grampletleiste* oder *Übersicht* hinzugefügt werden.}}

### Sind nicht alle Zusatzmodule auch Gramplets?

Was ist der Unterschied zwischen Gramplets, Berichten, Schnellansichten und Werkzeugen?

All dies sind **Zusatzmodul**arten. Gramplets sind jedoch Subtypen von Zusatzmodulen mit stärkerem Schwerpunkt auf der Benutzeroberfläche. Gramplets fügen der Ansicht eine **Funktion** oder eine **andere Perspektive** hinzu. Sie können verwendet werden, um den Arbeitsablauf einer Ansicht zu verbessern.

Die anderen Zusatzmodule neigen dazu, den normalen Arbeitsablauf zu unterbrechen, um eine andere Aufgabe auszuführen. Sie neigen auch dazu, zeitweise verwendet zu werden. Ein Zusatzmodul kann eine statischen (auch wenn aktiv verknüpft) Momentaufnahme der Daten erstellen, eine Möglichkeit zur Massenänderung darstellen oder ein alternatives Import-/Export-/Ausgabesystem bereitstellen.

Einige gängige [Zusatzmodularten](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Zusatzmodulverwaltung#Zusatzmodularten) sind:

- Berichte - bieten ein statisches Ausgabeformat deiner Daten, typischerweise für Präsentationen
- [Schnellansichten](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte_-_Teil_8#Schnellansichten) - bieten eine normalerweise kurze, interaktive Liste, die aus deinen Daten abgeleitet wird
- Werkzeuge - bieten eine Methode zur Verarbeitung deiner Daten
- Gramplets - bieten eine dynamische Ansicht und Schnittstelle zu deinen Daten.

Ein tieferes Verständnis der verschiedenen Arten von Zusatzmodulen erhältst du, indem du die [Zusatzmodulliste](wiki:6.0_Addons#Addon_List) nach **Art** sortierst und die gegensätzlichen **Beschreibungen** untersuchst.

Einige der eher statischen Arten von Zusatzmodulen können erweitert werden, um dynamisch als Gramplet zu arbeiten.

Mehrere Zusatzmodule haben sich zu mehreren Arten entwickelt. Einige Zusatzmodule sind Konsolen, die zusätzliche Funktionen um andere Zusatzmodule legen. Das **Schnellansicht** Gramplet ist keine [Art von Schnellansichtzusatzmodul](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte_-_Teil_8#Schnellansichten). Stattdessen handelt es sich um eine andockbare Konsole, die ein Zusatzmodul für die Schnellansicht anzeigt und das Zusatzmodul zur Aktualisierung drängt, wenn sich der Kontext ändert.

### Mit Gramplets beginnen

Wenn du die [Übersichtkategorie](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Kategorien#Übersichtkategorie) zum ersten Mal startest, sihst du zwei Standard-Gramplets; das **** Gramplet und das **** Gramplet.

Die Übersicht und die Gramplet Trennleisten der Navigator-Kategorien können **allgemeine** und **spezifische** Gramplets haben.

- Gemeinsame Gramplets sind auf jede Ansicht anwendbar ... und der Datenansichtspunkt bezieht sich auf den Kontext der aktiven Person und/oder der Hauptperson. Sie können an eine beliebige Navigator-Kategorieansicht angedockt werden, ohne dass diese Ansicht zweideutig erscheint.
- Spezielle Gramplets benötigen den Kontext bestimmter Ansichten, um ihrer Perspektive auf die Daten einen Kontext zu geben. Die Liste im Untermenü "Gramplet hinzufügen" des Dashboards und das Gramplet Bar Menü unterscheiden sich je nach aktiver Kategorieansicht und installierten Gramplets.

Diese Liste stammt aus einer früheren Überarbeitung des Wikis. Es ist unklar, wo die Punkte in diese Diskussion passen.

- Rückverweise Gramplets - bieten sofortige Sichtbarkeit von Daten, die gelegentlich angezeigt werden und in der Benutzeroberfläche vergraben sind ... wie die Registerkarte im Objekteditor.
- Filter Gramplet ist wie die vorherige Filter-Seitenleiste
- Gängige Modelle für Notizen, Galerie, Quellen, Zitate, Ereignisse
- Kinder Gramplet in Personenansichten (auch Schaubilderkategorie und Beziehungenkategorie), Familienansicht

### Allgemein Verwendung und Konfiguration

![[_media/WelcomeToGramps-Gramplet-docked-in-dashboard-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Beispiel für ein Gramplet, das an der Übersicht angedockt ist und oben die Steuerelemente anzeigt]] Die Container-Steuerelemente für Gramplets sind in der Übersichtkategorieansicht etwas anders angeordnet als in der Seitenleiste und Fußleiste. Wenn du dir bewusst bist, wie sich diese Gramplet-Container unterscheiden (und ähnlich sind), kannst du dich darauf konzentrieren, die Hochgeschwindigkeitsleistung zu erzielen, anstatt sich zu fragen, warum sie außer Kontrolle geraten sind.

Ursprünglich in Version 3 hinzugefügt, sind Gramplets in der Übersichtkategorieansicht in einer konfigurierbaren Anzahl von Spalten angeordnet. Die [geteilten Fenster](wiki:Split_Views) Seitenleiste und Fußleiste wurden aus späteren Innovationen von [GEPS 19](wiki:GEPS_019:_Improved_Sidebar_and_Split_Views) ausgewählt. Sie wurden auf der Filter Seitenleiste der Version 3.3 aufgebaut. Der Filter wurde in ein Gramplet umgewandelt ''und in der Seitenleiste vor angedockt.

![[_media/Welcome-to-Gramps-Gramplet-detached-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Freistehendes Seitenleisten Willkommen bei Gramps! Gramplet]]Die geteilten Fenster bieten einen begrenzten Bildschirmbereich zum Andocken von Gramplets in den anderen Navigator-Kategorien. Im Gegensatz zu den vielen Spalten der Übersichtansicht ist jedes neue geteilte Fenster eine einzelne Spalte, die mit einem einzelnen Gramplet gefüllt ist. (Der Bereich unterstützt immer noch das Bereithalten mehrerer Gramplets, er verwendet nur Tabulatoren, um sie einzeln anzuzeigen.)

Der Ansatz mit geteilten Fenstern reduziert die Notwendigkeit, zwischen Kategorieansichten zu wechseln... und das verringert die Anforderungen an die Datenbank.

![[_media/DashboardCategory-gramplet-detached-and-docked-example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Freistehendes Gramplet in in der Übersichtansicht (mit darunter angedocktem Gramplet)]] Gramplets können jedoch ausgedockt (abgetrennt, abgezogen) werden, um frei von den drei Containern zu schweben. Wenn sie abgetrennt sind, öffnet eine zusätzliche -Schaltfläche unten links die Gramplet-Seite auf dieser Website und eine -Schaltfläche unten rechts. Ein Klick auf die  Schaltfläche in der oberen rechten Ecke dockt ein abgetrenntes Gramplet wieder an. Durch Klicken auf die ähnliche  Schaltfläche eines angedockten Gramplets wird es aus dem Bereich entfernt.

#### Die Übersichtkategorieansicht

In der [Übersichtkategorie](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Kategorien#Übersichtkategorie) kannst du die  Schaltfläche (oben links) jedes Gramplets ziehen, um es im Übersichtansichtsbereich neu zu positionieren. Du kannst auf die  Schaltfläche klicken, um das Gramplet von der Übersicht-Ansicht zu trennen (oder *‘abkoppeln’*) und in einem eigenen Fenster zu platzieren. Das Fenster bleibt unabhängig von der Seite geöffnet (Beziehungen, Diagramme usw.). Wenn du die getrennte Ansicht schließt, wird sie wieder in die Übersicht-Ansicht verschoben. Wenn du Gramps mit einem geöffneten Gramplet beendest, öffnet es sich automatisch, wenn du Gramps erneut startest.

Wenn ein oder mehrere Gramplets von der Übersichtansicht abgedockt sind, bleiben sie sichtbar, wenn du zu einer anderen Ansicht wechselst (wie der Personen- oder Diagrammansicht). Auf diese Weise kannst du diese Gramplets verwenden, um eine bestimmte Ansicht mit zusätzlichen Details und Funktionen zu ergänzen, die das Gramplet bietet.

Du kannst neue Gramplets hinzufügen, indem du mit der rechten Maustaste auf einen freien Bereich in der Übersicht-Ansicht klickst. Klicke auf die  Schaltfläche über dem Gramplet, um es aus der Übersicht zu entfernen.

##### ⚙ Konfigurierbare Optionen

![[_media/Menubar-View-overview-example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Ansicht Menü]] Du kannst auch die Anzahl der Spalten ändern, indem du eine Einstellung der Registerkarte *Gramplets Layout* im Fenster *Übersicht konfigurieren* änderst. Um das Fenster zu öffnen, klicke auf die ![[_media/Gramps-config.png]] Schaltfläche, wähle aus dem Menü Ansicht oder drücke die *aktiven Ansicht konfigurieren* [Tastaturbelegung](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Tastenkürzel_Referenz#Allgemeine_K.C3.BCrzel). ![[_media/Whats-next-gramplet-configure-dashboard-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Registerkarten für die Gramplet-Konfiguration]] Jedem auf der Übersicht angedockten Gramplet wird auch eine Registerkarte "Konfiguration" hinzugefügt. (Aber dasselbe Gramplet hat möglicherweise keine Konfigurationsoptionen oder Registerkarte, wenn es in der Seitenleiste oder der Fußleiste angedockt ist.) Die Übersicht bietet zusätzliche Optionen für jedes Gramplet, um es umbenennen, auf eine feste vertikale Größe einstellen oder in seiner Spalte vertikal maximieren zu können . Die in der Übersicht angedockte Registerkarte Konfiguration für Gramplets spiegelt mindestens diese Mindestoptionen wider.

Durch Doppelklicken auf den Titel eines in der Übersicht-Kategorie angedockten Gramplets kannst du den Anzeigetitel ändern.

#### Die Bildschirmunterteilung Seitenleiste & Fußleiste

![[_media/Bottombar-sidebar-drop-down-menu-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Gramplet geteilte Bildschirme, die das Gramplet-Leistenmenü mit der unbeschrifteten Aufklappmenüschaltfläche mit dem Abwärtspfeil  zeigen]] Jeder dieser geteilten Bildschirme ist ein Behälter mit gestapelten Gramplet-Registerkarten. Wie bei Windows mit einem Abschnitt mit Registerkarten kann jeweils nur eine einzelne Registerkarte angezeigt werden. Registerkarten können jedoch ähnlich wie in der Übersicht hinzugefügt, neu angeordnet, abgedockt oder deaktiviert werden. Anstelle eines Kontextmenüs verfügt jedoch jedes mit geteilten Fenstern über eine Aufklappmenüschaltfläche mit dem *Abwärtspfeil* , um dieselbe Aufklappliste mit Optionen anzuzeigen.

Um ein Gramplet zu den gestapelten Registerkarten hinzuzufügen, wähle es aus dem Untermenü.

<span id="undock gramplet">Um eine Registerkarte zu lösen, greife den Titel der Registerkarte und ziehe sie aus dem geteilten Fenster auf die Symbolleiste oder die Menüleiste. Um eine Registerkarte wieder anzudocken, klicke auf die Schaltfläche „Schließen“ oder die Schaltfläche „X“.</span>

Um das Gramplet aus den Stapelregisterkarten zu entfernen, wähle es aus dem Untermenüs. (Alternativ ist die Schaltfläche Schließen verfügbar, wenn das Kontrollkästchen 'Schließen-Schaltfläche in Gramplet-Registerkarten anzeigen' auf der Registerkarte [Anzeige](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Einstellungen#Anzeige) der Einstellungen aktiviert ist.)

Seltsamerweise können dieselben Gramplets Registerkarten in den verschiedenen geteilten Bildschirmabschnitten einer Ansicht sein, aber so konfiguriert sein, dass sie Informationen unterschiedlich anzeigen. Es ist wichtig zu wissen, dass jedes Gramplet (ob gestapelt als Registerkarte oder schwebend abgedockt) die Leistung von Gramps beeinträchtigt. Verwende weniger Gramplets, um Gramps reaktionsschneller zu machen.

Die Listen von Gramplets, die dem Registerkartenstapel in einem geteilten Fenster hinzugefügt werden können, werden nach den für diese Kategorie geeigneten gefiltert.

##### ⚙ Konfigurierbare Optionen

![[_media/Menubar-View-overview-example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Ansicht Menü]]

Darüber hinaus gibt es eine Reihe von Gramplets von Drittanbietern, die du einfach installieren und verwenden kannst. Diese schließen ein:

- Schlagzeilen Gramplet - aktuelle Kurzmeldungen von Gramps
- Dateneingabe Gramplet - Bearbeiten des Namen, Geburtsdatum und Ort, Todesdatum und Ort der aktiven Person und Personen hinzufügen
- Python Gramplet - eine Python Shell
- FAQ Gramplet - häufig gestellte Fragen
- Notiz Gramplet - Anzeigen und Bearbeiten der Hauptnotiz der aktiven Person

und viele andere. Siehe [Zusatzmodule von Drittanbietern](wiki:Third-party_Addons) für mehr Details.

## Übersicht der Gramplets

Zusammenfassung aller standardmäßig eingebauten Gramplets und der Ansichtskategorien, in denen jedes Gramplet verwendet werden kann.

Unabhängig für jeden Kategorieansichtsmodus-Container können die Gramplets mit den folgenden Steuerelementen hinzugefügt oder entfernt werden:

- In der Kategorie Übersicht über das Kontextmenü mit der rechten Maustaste.
- In allen anderen Kategorien über die Dropdown-Menüs zur Gramplet-Auswahl (Pfeiltaste nach unten) entweder in der Fußleiste oder in der Seitenleiste.

*Es gibt keine Menüoptionen, um ein Gramplet hinzuzufügen. Dies liegt daran, dass es mehrdeutig wäre, ob das Gramplet der Seitenleiste oder der Fußleiste dieses Ansichtsmodus hinzugefügt werden soll.* {{-}}

### Gramplet-Liste

Klicke (zweimal) auf einen Kategorie-Header, um die Liste zu sortieren und das Menü dieser Kategorie mit verfügbaren integrierten Gramplet-Optionen anzuzeigen. (Das eigentliche Menü enthält auch installierte [Gramplets-Zusatzmodule](wiki:6.0_Addons#Addon_List) von Drittanbietern.)

| Gramplet | ![[_media/22x22-gramps-gramplet.png]] <small>Übersicht</small> | ![[_media/22x22-gramps-person.png]] <small>Personen</small> | ![[_media/22x22-gramps-relation.png]] <small>Beziehungen</small> | ![[_media/22x22-gramps-family.png]] <small>Familien</small> | ![[_media/22x22-gramps-pedigree.png]] <small>Schaubilder</small> | ![[_media/22x22-gramps-event.png]] <small>Ereignisse</small> | ![[_media/22x22-gramps-place.png]] <small>Orte</small> | ![[_media/22x22-gramps-geo.png]] <small>Geografie</small> | ![[_media/22x22-gramps-source.png]] <small>Quellen</small> | ![[_media/22x22-gramps-citation.png]] <small>Fundstellen</small> | ![[_media/22x22-gramps-repository.png]] <small>Aufbewahrungsorte</small> | ![[_media/22x22-gramps-media.png]] <small>Medien</small> | ![[_media/22x22-gramps-notes.png]] <small>Notizen</small> |
|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
| id="0" \| |  | ✔ | ✔ |  | ✔ |  |  | ✔ |  |  |  |  |  |
| id="20" \| |  | ✔ | ✔ |  | ✔ |  |  | ✔ |  |  |  |  |  |
| id="2" \| | <big>🗹</big> | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| id="1" \| | <big>🗹</big> | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| id="4" \| |  | <big>❖</big> | ✔ | <big>❖</big> | ✔ | <big>❖</big> |  | ✔ | <big>❖</big> | <big>❖</big> |  | <big>❖</big> |  |
| id="17" \| |  |  |  |  |  |  |  |  |  |  |  | ✔ |  |
| id="10" \| |  | <big>❖</big> | ✔ |  | ✔ |  | <big>❖</big> | ✔ |  |  | <big>❖</big> |  |  |
| id="18a" \| |  |  |  |  |  |  | ✔ |  |  |  |  |  |  |
| id="11" \| |  | <big>❖</big> | ✔ | <big>❖</big> | ✔ |  |  | ✔ |  |  |  |  |  |
| id="11a" \| |  | <big>❖</big> | ✔ | <big>❖</big> | ✔ |  |  | ✔ |  |  |  |  |  |
| id="13" \| |  | ✔ | ✔ |  | ✔ |  |  | ✔ |  |  |  |  |  |
| id="12" \| | <big>🗹</big> | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| id="14" \| |  | <big>♦</big> | <big>♦</big> | <big>♦</big> | <big>♦</big> | <big>♦</big> | <big>♦</big> | <big>♦</big> | <big>♦</big> | <big>♦</big> | <big>♦</big> | <big>♦</big> | <big>♦</big> |
| id="7" \| |  | <big>❖</big> | ✔ | <big>❖</big> | ✔ | <big>❖</big> | <big>❖</big> | ✔ |  |  |  | <big>❖</big> |  |
| id="15" \| |  | <big>❖</big> | ✔ | <big>❖</big> | ✔ | <big>❖</big> | <big>❖</big> | ✔ | <big>❖</big> | <big>❖</big> |  |  |  |
| id="32" \| | <big>🗹</big> | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| id="5" \| | <big>🗹</big> | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| id="6" \| |  | <big>❖</big> | ✔ | <big>❖</big> | ✔ |  |  | ✔ |  |  |  |  |  |
| id="21" \| |  |  |  |  |  |  |  |  |  |  |  | ✔ |  |
| id="8" \| |  | ✔ | ✔ |  | ✔ |  |  | ✔ |  |  |  |  |  |
| id="9" \| |  | ✔ | ✔ |  | ✔ |  |  | ✔ |  |  |  |  |  |
| id="30" \| | <big>🗹</big> | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| id="19" \| |  | <big>❖</big> | ✔ | <big>❖</big> | ✔ | <big>❖</big> | <big>❖</big> | ✔ | <big>❖</big> | <big>❖</big> | <big>❖</big> | <big>❖</big> | <big>❖</big> |
| id="24" \| |  | <big>❖</big> | ✔ | <big>❖</big> | ✔ | <big>❖</big> | <big>❖</big> | ✔ | <big>❖</big> | <big>❖</big> | <big>❖</big> | <big>❖</big> | <big>❖</big> |
| id="23" \| | <big>🗹</big> | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| id="22" \| | <big>🗹 ⚙</big> | <big>♦ ⚙</big> | <big>♦ ⚙</big> | <big>♦ ⚙</big> | <big>♦ ⚙</big> | <big>♦ ⚙</big> | <big>♦ ⚙</big> | <big>♦ ⚙</big> | <big>♦ ⚙</big> | <big>♦ ⚙</big> | <big>♦ ⚙</big> | <big>♦ ⚙</big> | <big>♦ ⚙</big> |
| id="27" \| | <big>🗹</big> | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| id="28" \| | <big>🗹</big> | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| id="29" \| | <big>🗹</big> | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| id="18b" \| |  |  |  |  |  |  | ✔ |  |  |  |  |  |  |
| id="25" \| |  | ✔ | ✔ |  | ✔ |  |  | ✔ |  |  |  |  |  |
| id="3" \| |  | ✔ | ✔ |  | ✔ |  |  | ✔ |  |  |  |  |  |
| id="16" \| | <big>🗹</big> | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| id="34" \| | <big>🗹</big> | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| id="33" \| | <big>🗹</big> | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| id="26" \| |  | ✔ | ✔ |  | ✔ |  |  | ✔ |  |  |  |  |  |
| id="31" \| | <big>🗹</big> | <big>❖</big> | <big>❖</big> | <big>❖</big> | <big>❖</big> | <big>❖</big> | <big>❖</big> | <big>❖</big> | <big>❖</big> | <big>❖</big> | <big>❖</big> | <big>❖</big> |  |
| id="37" \| | <big>🗹</big> ⚠ | ⚠ | ⚠ |  | ⚠ | ⚠ | ⚠ | ⚠ | ⚠ | ⚠ | ⚠ | ⚠ | ⚠ |
| id="35" \| | <big>🗹</big> ⚠ | ⚠ | ⚠ |  | ⚠ | ⚠ | ⚠ | ⚠ | ⚠ | ⚠ | ⚠ | ⚠ | ⚠ |
| id="xx" \| |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |

| Symbol         | Bedeutung                                             |
|----------------|-------------------------------------------------------|
| ⚠              | Gefährlich. Nur im Debug-Modus verfügbar              |
| ✔              | aufgelistet im Gramplet-Menü zur Ansicht              |
| <big>🗹</big>   | unterschiedliches Verhalten der Container             |
| <big>♦ ⚙</big> | Kategorie spezifische Konfigurationsoptionen          |
| <big>♦</big>   | Kategorie spezifische Schnittstelle                   |
| <big>❖</big>   | Inhalt basierend auf aktivem Datensatz oder Kategorie |

Ausführlichere Informationen zur Verwendung der installierten Gramplets findest du unter [Gramplets](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Gramplets#Gramplets).. {{-}}

## Gramplets

In den folgenden Abschnitten werden die einzelnen Gramplets und ihre Grundfunktionen beschrieben. {{-}}

### 2-Wege-Fächergrafik

![[_media/2-WayFanChart-detached-gramplet-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} 2-Wege-Fächergrafik Gramplet]] Diagramm, das sowohl aus Vorfahren als auch aus Nachkommen besteht. **Die 2-Wege-Fächeransicht** zeigt interaktiv die Vorfahren und Nachkommen der aktiven Person in einem Tortendiagrammformat an. Der Nachkommen-Fächer bietet eine umfassende und visuell ansprechende Möglichkeit, die Nachkommen einer Person in Ihrem Familienstammbaum zu untersuchen und zu analysieren.

Siehe auch: {{-}}

### Alter am Datum

![[_media/AgeOnDate-Gramplet-detached-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Alter am Datum Gramplet - freistehend Beispiel]]

Das Gramplet ermöglicht dir die Eingabe eines [Kalenderdatums](https://de.wikipedia.org/wiki/Kalenderdatum) in das Eingabefeld . Wenn du wählst, berechnet das Gramplet das Alter für alle Personen in deinem Stammbaum, die an diesem Datum leben, und zeigt die Ergebnisse in einem separaten Schnellansicht-Berichtsdialog an. Das Datum muss in einem von Gramps akzeptierten Kalenderformat eingegeben werden, zB: JJJJ-MM-TT.

- Für dieses Gramplet sind keine Konfigurationsoptionen verfügbar.

{{-}}

- Du kannst auch ein Datum aus [Kalender Gramplet](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Gramplets#Kalender) in das Eingabefeld des Gramplets ziehen, um dieses Datum einzugeben.
- Siehe auch das Gramplet [Datums Rechner](wiki:Addon:DateCalculator) der [Drittanbieter Zusatzmodule](wiki:Third-party_Addons), mit dem du Datumsberechnungen durchführen kannst.

{{-}}

#### Personen und ihr Alter am <Datum> Quick Schnellansicht-Berichtsdialog

![[_media/AgeOnDate-Gramplet-QuickView-example-result-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Alter am Datum Gramplet - Schnellansicht - Ergebnis Beispiel]]

Im resultierenden Schnellansicht-Berichtsdialog kannst du nach den Spalten Person, Alter oder Status sortieren. Ein Rechtsklick auf die Zeile öffnet ein Kontextmenü, mit dem du in die Zwischenablage *Alles kopieren* kannst; oder *Siehe die Personendetails* im Personeneditor oder *Aktiviere die Person* kannst. {{-}} Siehe auch:

- [Schnellansichten](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte_-_Teil_8#Schnellansichten)

### Altersstatistiken

![[_media/AgeStats-Gramplet-detached-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Altersstatistiken Gramplet - freistehend Beispiel]]

Das Gramplet zeigt Statistiken in Form von drei Textgrafiken an, die nach Altersspannen von 5 Jahren gruppiert sind (Verwende die vertikale Bildlaufleiste, um die beiden anderen Diagramme anzuzeigen, oder löse das Gramplet und maximiere es):

- **Lebensspanne Altersverteilung** - für alle Personen mit gültigen Geburts- und Sterbedaten.
- **Vater - *Kind Altersunterschiedsverteilung*** - zeigt den Altersunterschied zwischen Kind und Vater, wenn beide Personen gültige Geburtsdaten haben.
- **Mutter - *Kind Altersunterschiedsverteilung*** - zeigt den Altersunterschied zwischen Kind und Mutter, wenn beide Personen gültige Geburtsdaten haben.

Wenn du mit dem Mauszeiger über eine Zeile im Diagramm fährst, wird ein Hinweis mit der Anzahl der Nachkommen angezeigt, die dem Bereich der Zeile entsprechen.

Doppel klicken einer Zeile in den Statistiken öffnet einen Schnellansichtbericht mit allen Personen, die in der Zeile enthalten sind. Du kannst den Schnellansichtbericht nach den Spalten Namen, Geburtsdatum und Namensart sortieren.

Wenn du mit der rechten Maustaste auf die Berichtszeile der Schnellansicht klickst, wird ein Kontextmenü zum Kopieren der Liste, zum Öffnen des Personeneditors oder zum Aktivieren der Person angezeigt.

{{-}}

#### Altersstatistiken Schnellansicht

##### ⚙ Konfigurierbare Optionen

![[_media/AgeStats-Gramplet-configuration-tab-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;Altersstatistiken&quot; Gramplet - die Personenkategorie Standardeinstellungen aus der Registerkarte &quot;Schaubilder Konfiguration&quot;]] Einstellbare Schaubildskalierungsgrenzen

- (`110` Standardeinstellung)- Das Höchstalter liegt zwischen 1 und 150 Jahren.

- (`55` Standardeinstellung) - Das Höchstalter liegt zwischen 1 und 150 Jahren.

- (`70` Standardeinstellung) - Das Höchstalter liegt zwischen 1 und 70 Jahren.

Wähle die Schaltfläche , um deine Änderungen zu übernehmen.

In der Übersichtansicht kann das Gramplet durch Klicken auf die Schaltfläche losgelöst werden. {{-}}

### Vorfahren

![[_media/Ancestors-Gramplet-detached-example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Vorfahren Gramplet - freistehend Beispiele]]

Verwende das Gramplet , um die Vorfahren der aktiven Person anzuzeigen. Es ist als Navigationshilfe gedacht, als alternative Möglichkeit, sich in Gramps durch deinen Stammbaum zu bewegen. Wenn du das Gramplet löst und neben Gramps platzierst, kannst du damit den Inhalt der aktuellen „Personenansicht” leicht ändern.

Wenn du mit der Maus über eine Person fährst, wird ein Tooltip mit Details zu dieser Person angezeigt.

Verwende das Kontextmenü für:

- – die ausgewählte Person.

- – den Inhalt des Gramplets in die Zwischenablage des Betriebssystems.

{{-}} Siehe auch:

- Gramplet - Angehörige der aktiven Person Navigationshilfe.

### Attribute

![[_media/Attributes-Gramplet-detached-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Attribute Gramplet]]

Das Attribute Gramplet zeigt alle Attribute der aktuellen, aktiven Person. Doppelklicke auf den Namen des Attributs, und du führst eine Schnellansicht aus, die alle Personen mit diesem Attribut und die Werte dafür anzeigt. Du kannst die Schnellansicht nach dem Attributwert sortieren, indem du auf den Spaltennamen klickst. {{-}}

##### Attribute Schnellansicht

![[_media/Atttribute-Gramplet-QuickView-example-result-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Attribute Gramplet - Schnellansicht - Ergebnis Beispiel]]

Markiere in der Schnellansicht den Eintrag, um die aktive Person zu ändern (wodurch dann das Gramplet der Attribute geändert wird), und doppelklicke auf den Eintrag der Schnellansicht, um das Dialogfenster Person bearbeiten aufzurufen. {{-}}

#### Person Attribute

Siehe [Attribute](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Gramplets#Attribute) {{-}}

#### Familie Attribute

Siehe [Attribute](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Gramplets#Attribute) {{-}}

#### Ereignis Attribute

Siehe [Attribute](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Gramplets#Attribute) {{-}}

#### Quelle Attribute

Siehe [Attribute](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Gramplets#Attribute) {{-}}

#### Fundstelle Attribute

Siehe [Attribute](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Gramplets#Attribute) {{-}}

#### Medium Attribute

Siehe [Attribute](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Gramplets#Attribute) {{-}}

### Kalender

![[_media/CalendarGramplet-detached-example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Kalender Gramplet" - freistehend Beispiel]]

Das **Kalender Gramplet** zeigt einen Monatskalender.

Um die Bezeichnung in der oberen linken Ecke, die und -Schaltflächen können verwendet werden, um den Monat zu ändern.

Um die Bezeichnung in der oberen linken Ecke, die und -Schaltflächen können verwendet werden, um das Jahr zu ändern.

Doppelklicke auf einen **Tag**, um die -Schnellansicht auszuführen. Das Schnellansichtsfenster zeigt bis zu 3 Tabellenabschnitte, die Ereignisse (sofern vorhanden) von: dem genauen Datum, anderen Ereignissen im selben Monat/Tag im Verlauf und Ereignisse in diesem Jahr.

Du kannst auch einen Tag aus dem Kalender in die Datumsfelder ziehen (z.B. für das [Ereigniseditor](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Daten_eingeben_und_bearbeiten:_Ausführlich_-_Teil_2#Neues_Ereignis_Dialog) oder das [Alter am Datum Gramplet](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Gramplets#Alter_am_Datum)), um dieses Datum einzugeben. Auf ähnliche Weise kann ein Kalendertag auch in die [Zwischenablage](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Navigation#Die_Zwischenablage_verwenden) gezogen werden, wo er in einem Nur-Text-Format gespeichert wird.

{man tip\|Die Kalenderspalten sind lokalisiert\|Der übliche erste Tag der Woche, der in Kalendern angezeigt wird, variiert kulturell. Der Kalender passt sich dem Ort an. Wenn die erste Kalenderspalte für den falschen Wochentag steht, wende dich an den Übersetzer für deine Sprache und verweise ihn auf die [`gtk/gtkcalendar`-Übersetzungszeichenfolge](https://github.com/gramps-project/gramps/pull/1319#issuecomment-1002039348).}} {{-}}

### Kinder

![[_media/ChildrenGramplet-PeopleCategoryView-detached-example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Kinder Gramplet - freistehend Beispiel mit Werkzeughinweis]]

Gramplet, das die Kinder der aktiven Personen aus **allen Ehen** anzeigt. Die Kinder werden in der Reihenfolge angezeigt, in der sie in den Familiendatensätzen aufgeführt sind.

Doppelklicke auf eine Zeile, um das ausgewählte Kind zu bearbeiten.

Wähle einen Spaltenüberschrift aus, um die Daten vorübergehend zu sortieren, bis du Gramps beendest.

[Wie ändere ich die Reihenfolge von Kindern?](wiki:De:Gramps_6.0_Wiki_Handbuch_-_FAQ#Wie_.C3.A4ndere_ich_die_Reihenfolge_von_Kindern.3F)

Verwende:

- Verwende die Registerkarte [Kinder](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Daten_eingeben_und_bearbeiten:_Ausführlich_-_Teil_1#Kinder) im Familieneditor, um die Reihenfolge der Kinder in der aktiven Familie zu ändern.
- Verwende die Erweiterung von Drittanbietern, mit der du die Reihenfolge der Kinder in großen Mengen aktualisieren kannst.

Siehe auch:

- Dieses Gramplet [Kinder](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Gramplets#Kinder) in der [Personenkategorie](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Kategorien#Personenkategorie) zeigt alle Kinder aus allen Ehen der aktiven Person an. Die Kinder werden in der Reihenfolge angezeigt, in der sie in den Familiendatensätzen aufgeführt sind.

{{-}}

#### Person Kinder

Siehe [Kinder](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Gramplets#Kinder)

Außerdem zeigt die Spalte `Ehepartner` an, mit welchem anderen Elternteil die aktive Person das Kind hatte (und der nicht der Ehepartner des aufgeführten Kindes ist!). {{-}}

#### Familie Kinder

Siehe [Kinder](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Gramplets#Kinder) {{-}}

### Fundstellen

![[_media/Citation-Gramplet-detached-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Fundstelle Gramplet - freistehend Beispiel]]

Gramplet zeigt die Fundstellen der aktiven Person. {{-}}

#### Person Fundstellen

Siehe [Fundstellen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Gramplets#Fundstellen) {{-}}

#### Familie Fundstellen

Siehe [Fundstellen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Gramplets#Fundstellen) {{-}}

#### Ereignis Fundstellen

Siehe [Fundstellen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Gramplets#Fundstellen) {{-}}

#### Ort Fundstellen

Siehe [Fundstellen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Gramplets#Fundstellen) {{-}}

#### Medium Fundstellen

Siehe [Fundstellen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Gramplets#Fundstellen) {{-}}

### Nachfahrefächer

![[_media/DescendantFan-Gramplet-detached-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Nachfahrefächer (Schaubild) Gramplet - freistehend Beispiel]]

Gramplet zeigt die direkten Nachkommen der aktiven Person als Fächerdiagramm.

**Siehe auch:** {{-}}

### Nachkommen

![[_media/Descendants-Gramplet-detached-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Nachkommen Gramplet - freistehend Beispiel]]

Das Nachkommen Gramplet zeigt die direkten Nachkommen der aktiven Person.

Die Reihenfolge der Ehepartner und Kinder ist die im Gramps-Editor angegebene. Um die Reihenfolge der Ehepartner zu ändern, klicke in der Beziehungsansicht auf *Reihenfolge*. Um die Reihenfolge der Kinder zu ändern, [ziehe](https://de.wikipedia.org/wiki/Drag_and_Drop) sie im Familienbearbeitungsfenster in die richtige Reihenfolge.

Dieses Gramplet basiert auf dem [Nachkommenbericht](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte_-_Teil_6#Nachkommenbericht), der bei den Textberichten zu finden ist.

Das Nachkommen Gramplet wird aktualisiert, wenn du die aktive Person oder den Stammbaum änderst. Es wird bei Änderungen oder Ergänzungen nicht automatisch aktualisiert, da die Ausführung dieses Berichts zeitaufwändig ist.

Das Minimieren eines Gramplets verhindert, dass es aktualisiert wird.

Wenn du die Maus über eine Person bewegst, wird eine QuickInfo-Zusammenfassung mit dem Sterbedatum angezeigt. {{-}}

### Details

![[_media/Details-Gramplet-detached-example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Details Gramplet - freistehend Beispie mit Kontextmenül]]

Gramplet mit Details und Bild der aktiven Person.

Bietet eine kurze, nicht editierbare Zusammenfassung der ausgewählten Person, zum Beispiel:

- *Name*: der Person
- *Auch bekannt als:*
- *Other Name:*
- *Vater:*
- *Mutter:*
- *Geburt:*
- *Tod:*
- *Beerdigung:*

<!-- -->

- *Bild*: Wenn vorhanden, wird das Primärbild rechts neben den Details angezeigt, andernfalls weist ein Kreuz auf das Fehlen des Bildes hin. Du kannst auf das Bild doppelklicken, um es in einem externen Anzeigeprogramm zu öffnen. Um das primäre aktive Bild zu ändern, siehe: [Person-bearbeiten – Registerkarte Galerie](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Daten_eingeben_und_bearbeiten:_Ausführlich_-_Teil_1#Galerie)

Du kannst das Kontextmenü verwenden, indem du mit der rechten Maustaste klickst und auswählst.

Du kannst die einzelnen Textfelder markieren und kopieren.

- [Fehlendes Medienobjekt-Symbol für einen "defekten Link" in Form eines Kästchens mit einem roten 'x'](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Einstellungen#Fehlendes_Medienobjekt-Symbol_f.C3.BCr_einen_.22defekten_Link.22_in_Form_eines_K.C3.A4stchens_mit_einem_roten_.22x)

{{-}}

#### Person Details

Siehe [Details](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Gramplets#Details) {{-}}

#### Ort Details

Siehe [Details](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Gramplets#Details) {{-}}

#### Aufbewahrungsort Details

Siehe [Details](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Gramplets#Details) {{-}}

<span id="Place_Encloses">

### Enthalten

</span> ![[_media/Encloses-Gramplet-detached-example-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Enthalten Gramplet - freistehend Beispiel]]

Gramplet, das die hierarchische Lage eines Ortes zeigt, den es im Laufe der Zeit umschließt.

{{-}}

- Siehe auch [Teil von](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Daten_eingeben_und_bearbeiten:_Ausführlich_-_Teil_2#Teil_von) Registerkarte

<span id="Place_Enclosed_By">

#### Eingeschlossene Orte

</span> Siehe [Teil von](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Gramplets#Teil_von) {{-}}

### Teil von

![[_media/EnclosedBy-Gramplet-detached-example-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Teil von Gramplet - freistehend Beispiel]]

Gramplet, das die von einem Ort hierarchisch eingeschlossenen Orte im Laufe der Zeit zeigt.

- Siehe auch [Teil von](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Daten_eingeben_und_bearbeiten:_Ausführlich_-_Teil_2#Teil_von) Registerkarte

{{-}}

#### Eingeschlossen von Orten

Siehe [Enthalten](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Gramplets#Enthalten) {{-}}

### Ereignisse

![[_media/Events-Gramplet-detached-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Ereignisse Gramplet - freistehend Beispiel]] In erster Linie als Alternative zum Öffnen einer Layout-Registerkarte im Dialogfeld "Objekt bearbeiten" konzipiert..

Doppelklicke auf eine Zeile, um das Ereignis zu bearbeiten.

Siehe [Ereignisse](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Gramplets#Ereignisse)

#### Familie Ereignisse

Das in der Kategorie Person hinzugefügte Gramplet zeigt die Ereignisse für die aktive Familie an.

#### Person Ereignisse

Ein in der Kategorie Person hinzugefügtes Gramplet zeigt die Ereignisse für die aktive Person an.

{{-}}

### Ereigniskoordinaten

In erster Linie zur Überprüfung, ob die Schlüsseldaten für die Darstellung der Ereignisse in der Geografieansicht vorhanden sind. Neben den Koordinaten werden für einige der animierten Ansichten auch ein Datum und eine Ereignisart benötigt.

Klicke mit der rechten Maustaste auf eine Zeile, um ein Kontextmenü zum Bearbeiten des Ereignisses oder des Ortes zu öffnen. <span id="Geography coordinates for Family Events">

#### Audit Familienereignisse

</span>![[_media/EventsCoordinates-Gramplet-detached-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Ereigniskoordinaten Gramplet - freistehend Beispiel]]

Das in der Kategorie Familie hinzugefügte Gramplet zeigt die Ereignisse für die aktive Familie an.  
<span id="Geography_coordinates_for_Person_Events">

#### Person Ereignisse Audit

</span> Ein in der Kategorie Person hinzugefügtes Gramplet zeigt die Ereignisse für die aktive Person an. {{-}}

### Fächergrafik

![[_media/FanChart-detached-gramplet-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Fächergrafik Gramplet]]

Das Fächergrafik Gramplet zeigt die direkten Vorfahren der aktiven Person in einem kreisförmigen Format. Es ähnelt der Stammbaumansicht, wird jedoch um die zentrale/aktive Person herum gezeigt, und weitere Generationen wachsen heraus.

Klicke auf ein Elternteil im Diagramm und es wird über seinem Kind vergrößert oder verkleinert. Klicke mit der rechten Maustaste auf eine Person und du kannst:

- diese Person als aktive Person auswählen
- die Person, bearbeiten was es ermöglicht über den Personen-Editor Kinder zu den Familien der Person hinzuzufügen
- Kopieren von Name, Geburt und Tod der Person in die Zwischenablage
- aus den Verwandten der Person wählen um als aktive Person zu setzen
- Hinzufügen eines Partners (Familien) zu der Person

Wenn du in einen offenen Bereich (keine Person) klickst und die Maus ziehst, kannst du das Diagramm um die Mitte drehen. Du kannst auch mit der linken Maustaste klicken und in die Mitte ziehen, um das Fächerdiagramm neu zu positionieren.

Ein schwarzer Rand am äußeren Radius des Diagramms weist auf mehr Eltern für diese Person hin. Ein schwarzer Kreis in der Mitte zeigt an, dass die Person in der Mitte Kinder hat.

Das Fächergrafik Gramplet wird aktualisiert, wenn du die aktive Person oder den Stammbaum änderst.

Das Minimieren eines Gramplets verhindert, dass es aktualisiert wird.

**Siehe auch:** {{-}}

### FAQ

![[_media/FAQ-Gramplet-detached-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} FAQ Gramplet - freistehend Beispiel]]

Das (Häufig gestellte Fragen) zeigt eine Liste häufig gestellter Fragen und Links zu ihren Antworten aus dem Gramps-Wiki (erfordert eine Internetverbindung).

Dieses Gramplet zeigt eine manuell betreute Liste von **häufig gestellten Fragen** mit Hyperlinks zu Antworten in Artikeln des Gramps-Wikis. Die Liste wird aus Beiträgen neuer Benutzer in die [Gramps-Benutzer-Forum](wiki:De:Kontakt#Forum) zusammengestellt, die wiederholt beantwortet werden müssen.

Die Idee ist, die Antworten auf die am häufigsten gestellten Fragen leichter zu finden. Das Hauptziel besteht darin, dass neue Benutzer Gramps schneller verwenden können.

#### Siehe auch

- Fehlerbericht : wie man FAQs hinzufügt/aktualisiert

{{-}}

### Filter

Gramplet bietet einen für die Kategorie spezifischen Filter.

- 

- 

- \- *Interface is the same as the*

- 

- 

- \- *Interface is the same as the*

- 

- 

- 

- 

- 

###### Allgemeine Verwendung

Gib den Suchbegriff ein, passe die gewünschten Optionen an und klicke dann auf die Schaltfläche , um die Ergebnisse anzuzeigen, falls vorhanden.

###### Siehe auch

- [Welche Filter (Regeln) in welcher Kategorie?](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Filter#Welche_Filter_in_welcher_Kategorie.3F)
- Gramps Glossar Begriff: [Reguläre Ausdrücke](wiki:De:Gramps_Glossar#regex) für den Mustervergleich bei der Suche
- Drittanbieter *Isotammi* [Filter+ Gramplet Erweiterung](wiki:Addon:Isotammi_addons#Filter.2B)

{{-}} <span id="Person Filter"></span>

#### Personenfilter

![[_media/FilterGramplet-Person-detached-default-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Personen - &quot;Filter&quot; Gramplet - freistehend - Vorgabe]] Äquivalent zu den integrierten [eigenen Filterregeln](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Filter#toc):

- : [Personen mit Namen die dem &lt;Text&gt; entsprechen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Filter#Personen_mit_dem_.3CNamen.3E)

- : [Personen mit ID die den &lt;Text&gt; enthält](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Filter#Person_mit_.3CID.3E)

- : [Männer](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Filter#M.C3.A4nner) • [Frauen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Filter#Frauen) • [Personen mit unbekanntem Geschlecht](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Filter#Personen_mit_unbekanntem_Geschlecht)

- : [Personen mit dem &lt;Geburtsdatum&gt;](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Filter#Personen_mit_.3CGeburtsdaten.3E)

  - Datumsauswahl-Editor

- : [Personen mit dem &lt;Sterbedatum&gt;](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Filter#Personen_mit_.3CSterbedaten.3E)

  - Date selection editor

- : [Personen mit dem persönlichen &lt;Ereignis&gt;](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Filter#Hat_das_pers.C3.B6nliche_.3CEreignis.3E)

- : [Personen mit Notizen die den &lt;Text&gt; enthalten](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Filter#Personen.2C_deren_Notizen.2C_den_.3CText.3E_enthalten)

- : [Personen mit dem &lt;Etikett&gt;](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Filter#Personen_mit_dem_.3CEtikett.3E)

- : [Personen, die dem &lt;Filter&gt; entsprechen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Filter#Personen.2C_die_dem_.3CFilter.3E_entsprechen)

  - Filter definieren Editor

- :

- :

- :

- :

- Schaltfläche, die automatisch einen benutzerdefinierten Filter basierend auf den angegebenen Kriterien erstellt. Dies erleichtert die Erstellung einfacher benutzerdefinierter Filter.

##### Beispiel für Personenfilter

Einige einfache reguläre Ausdrücke zum Herausfiltern von Personen mit leicht abweichenden Nachnamen.

Mit diesem regulären Ausdruck im Seitenleistenfilter eingeben:

`eri[ck](s|ss)on`

oder

`eri[ck]ss?on`

oder

`eri[ck]s+on`

Du bekommst alle vier Versionen als Ergebnis:

`Ericson`  
`Ericsson`  
`Erikson `  
`Eriksson`

{{-}} <span id="Familie Filter"></span>

#### Familienfilter

![[_media/FilterGramplet-Family-detached-default-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Familien - &quot;Filter&quot; Gramplet - freistehend - Vorgabe]] Äquivalent zu den integrierten [eigenen Filterregeln](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Filter#toc):

- ID : [Familien mit ID, die den &lt;Text&gt; enthält](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Filter#Familien_mit_ID.2C_die_den_.3CText.3E_enth.C3.A4lt)
- Vater :[Familien mit Vater mit dem &lt;regex_Namen&gt;](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Filter#Familien_mit_Vater_mit_dem_.3CNamen.3E)
- Mutter : [Familien mit Mutter mit dem &lt;regex_Namen&gt;](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Filter#Familien_mit_Mutter_mit_dem_.3CNamen.3E)
- Kind : [Familien mit Kind mit dem &lt;regex_Namen&gt;](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Filter#Familien_mit_Kind_mit_dem_.3CNamen.3E)
- Beziehung : [Familien mit der Beziehungsart](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Filter#Familien_mit_der_Beziehungsart)
- Familiäres Ereignis : [Familien mit &lt;Ereignis&gt;](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Filter#Familien_mit_.3CEreignis.3E)
- Familiennotiz : [Familien, deren Notizen, den &lt;Text&gt; enthalten](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Filter#Familien.2C_deren_Notizen.2C_den_.3CText.3E_enthalten)
- Etikett : [Familien mit dem &lt;Etikett&gt;](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Filter#Familien_mit_dem_.3CEtikett.3E)
- Benutzerfilter : [Familien die dem &lt;Filter&gt; entsprechen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Filter#Familien_die_dem_.3CFilter.3E_entsprechen)

{{-}}

#### Schaubilder Filter

![[_media/FilterGramplet-Person-detached-default-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Schaubilder - Filter Gramplet - losgelöst - Standard (Gleich wie Personenfilter)]] Die Diagramme in Schaubildern benötigen den Kontext der verbundenen Datensätze, um die Verbindungen zwischen Blöcken zu definieren. Anstatt also "nur" die übereinstimmenden Datensätze in den Diagrammansichtsmodi anzuzeigen, zeigen die Filter für die Diagramme weiterhin alle Datensätze an, blenden aber die nicht übereinstimmenden Datensätze aus.

*Die Schnittstelle ist die gleiche wie die des* {{-}}

<span id="Ereignis Filter"></span>

#### Ereignisefilter

![[_media/FilterGramplet-Event-detached-default-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Ereignisefilter Gramplet - freistehend - Vorgabe]] Äquivalent zu den integrierten [eigenen Filterregeln](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Filter#toc):

- ID : [Ereignisse, deren ID den &lt;Text&gt; enthält](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Filter#Ereignisse.2C_deren_ID_den_.3CText.3E_enth.C3.A4lt)
- Beschreibung :[Ereignisse, die den Parametern entsprechen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Filter#Ereignisse.2C_die_den_Parametern_entsprechen)
- Art :<small>*Ereignisse, die den Parametern entsprechen*</small>
- Beteiligte :<small>*Ereignisse, die den Parametern entsprechen*</small>
- Datum :<small>*Ereignisse, die den Parametern entsprechen*</small>
- Ort :<small>*Ereignisse, die den Parametern entsprechen*</small>
- Notiz : [Ereignisse, deren Notizen, den &lt;Text&gt; enthalten](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Filter#Ereignisse.2C_deren_Notizen.2C_den_.3CText.3E_enthalten)
- Etikett : [Ereignisse mit dem &lt;Etikett&gt;](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Filter#Ereignisse_mit_dem_.3CEtikett.3E)
- Benutzerfilter : [Ereignisse entsprechend &lt;Filter&gt;](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Filter#Ereignisse_entsprechend_.3CFilter.3E)

{{-}} <span id="Ort Filter"></span>

#### Ortefilter

![[_media/FilterGramplet-Place-detached-default-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Ortefilter Gramplet - freistehend - Vorgabe]] Äquivalent zu den integrierten [eigenen Filterregeln](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Filter#toc):

- ID : [Orte, deren ID den &lt;Text&gt; enthält](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Filter#Orte.2C_deren_ID_den_.3CText.3E_enth.C3.A4lt)
- Name : [Orte mit gegebenen Parametern](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Filter#Orte_mit_gegebenen_Parametern)
- Art : <small>*Orte mit gegebenen Parametern*</small>
- Kennung : <small>*Orte mit gegebenen Parametern*</small>
- Teil von : [Orte die in anderen Orten enthalten sind](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Filter#Orte_die_in_anderen_Orten_enthalten_sind)
- Innerhalb : [Orte innerhalb eines Gebiets](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Filter#Orte_innerhalb_eines_Gebiets)
- Notiz : [Orte, deren Notizen, den &lt;Text&gt; enthalten](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Filter#Orte.2C_deren_Notizen.2C_den_.3CText.3E_enthalten)
- Etikett : [Orte mit dem &lt;Etikett&gt;](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Filter#Orte_mit_dem_.3CEtikett.3E)
- Benutzerfilter : [Orte entsprechend &lt;Filter&gt;](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Filter#Orte_entsprechend_.3CFilter.3E)

{{-}}

#### Geographie Filter

![[_media/FilterGramplet-Place-detached-default-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Geografie - Filter Gramplet - losgelöst - Standard (wie Filter Orte)]] *Die Schnittstelle ist die gleiche wie die des*

{{-}} <span id="Quelle Filter"></span>

#### Quellenfilter

![[_media/FilterGramplet-Source-detached-default-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Quellenfilter Gramplet - freistehend - Vorgabe]] Äquivalent zu den integrierten [eigenen Filterregeln](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Filter#toc):

- ID : [Quellen, deren ID den &lt;Text&gt; enthält](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Filter#Quellen.2C_deren_ID_den_.3CText.3E_enth.C3.A4lt)
- Titel :[Quellen entsprechend Parameter](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Filter#Quellen_entsprechend_Parameter)
- Autor :<small>*Quellen entsprechend Parameter*</small>
- Abkürzung :<small>*Quellen entsprechend Parameter*</small>
- Veröffentlichung :<small>*Quellen entsprechend Parameter*</small>
- Notiz : [Quellen, deren Notizen, den &lt;Text&gt; enthalten](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Filter#Quellen.2C_deren_Notizen.2C_den_.3CText.3E_enthalten)
- Etikett : [Quellen mit dem &lt;Etikett&gt;](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Filter#Quellen_mit_dem_.3CEtikett.3E)
- Benutzerfilter : [Quellen entsprechend &lt;Filter&gt;](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Filter#Quellen_entsprechend_.3CFilter.3E)

{{-}} <span id="Fundstelle Filter"></span>

#### Fundstellenfilter

![[_media/FilterGramplet-Citation-detached-default-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Fundstellenfilter Gramplet - freistehend - Vorgabe]] Äquivalent zu den integrierten [eigenen Filterregeln](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Filter#toc):

**Quelle:**

- ID : [Quellen, deren ID den &lt;Text&gt; enthält](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Filter#Quellen.2C_deren_ID_den_.3CText.3E_enth.C3.A4lt)
- Titel : [Quellen entsprechend Parametern](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Filter#Quellen_entsprechend_Parameter)
- Autor : <small>*Quellen entsprechend Parametern*</small>
- Abkürzung:<small>*Quellen entsprechend Parametern*</small>
- Veröffentlichung :<small>*Quellen entsprechend Parametern*</small>
- Notiz : [Fundstellen, deren Quellen Notizen den &lt;Text&gt; enthalten](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Filter#Fundstellen.2C_deren_Quellen_Notizen_den_.3CText.3E_enthalten)

**Fundstelle:**

- ID : [Fundstellen, deren ID den &lt;Text&gt; enthalten](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Filter#Fundstellen.2C_deren_ID_den_.3CText.3E_enthalten)
- Band/Seite: [Fundstellen entsprechend Parametern](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Filter#Fundstellen_entsprechend_Parametern)
- Datum :<small>*Fundstellen entsprechend Parametern*</small>
- Min. Vert. :<small>*Fundstellen entsprechend Parametern*</small>
- Notiz : [Fundstellen, deren Notizen, den &lt;Text&gt; enthalten](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Filter#Fundstellen.2C_deren_Notizen.2C_den_.3CText.3E_enthalten)
- Etikett : [Fundstellen mit dem &lt;Etikett&gt;](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Filter#Fundstellen_mit_dem_.3CEtikett.3E)
- Benutzerfilter : [Fundstellen entsprechend &lt;Filter&gt;](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Filter#Fundstellen_entsprechend_.3CFilter.3E)

{{-}} <span id="Aufbewahrungsort Filter"></span>

#### Aufbewahrungsortefilter

![[_media/FilterGramplet-Repository-detached-default-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Aufbewahrungsortefilter Gramplet - freistehend - Vorgabe]] Äquivalent zu den integrierten [eigenen Filterregeln](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Filter#toc):

- ID : [Aufbewahrungsorte, deren ID den &lt;Text&gt; enthält](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Filter#Aufbewahrungsorte.2C_deren_ID_den_.3CText.3E_enth.C3.A4lt)
- Name : [Aufbewahrungsorte entsprechend Parametern](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Filter#Aufbewahrungsorte_entsprechend_Parametern)
- Art :<small>*Aufbewahrungsorte entsprechend Parametern*</small>
- Adresse :<small>*Aufbewahrungsorte entsprechend Parametern*</small>
- URL :<small>*Aufbewahrungsorte entsprechend Parametern*</small>
- Notiz : [Aufbewahrungsorte, deren Notizen, den &lt;Text&gt; enthalten](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Filter#Aufbewahrungsorte.2C_deren_Notizen.2C_den_.3CText.3E_enthalten)
- Etikett : [Aufbewahrungsorte mit dem &lt;Etikett&gt;](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Filter#Aufbewahrungsorte_mit_dem_.3CEtikett.3E)
- Benutzerfilter : [Aufbewahrungsorte entsprechend &lt;Filter&gt;](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Filter#Aufbewahrungsorte_entsprechend_.3CFilter.3E)

{{-}}

#### Medium Filter

![[_media/FilterGramplet-Media-detached-default-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Medium - Filter Gramplet - freistehend - Vorgabe]] Äquivalent zu den integrierten [eigenen Filterregeln](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Filter#toc):

- ID : [Medienobjekte, deren ID den &lt;Text&gt; enthält](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Filter#Medienobjekte.2C_deren_ID_den_.3CText.3E_enth.C3.A4lt)
- Titel : [Medienobjekte, die den Parametern entsprechen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Filter#Medienobjekte.2C_die_den_Parametern_entsprechen)
- Art :<small>*Medienobjekte, die den Parametern entsprechen*</small>
- Pfad :<small>*Medienobjekte, die den Parametern entsprechen*</small>
- Datum :<small>*Medienobjekte, die den Parametern entsprechen*</small>
- Notiz : [Medienobjekte, deren Notizen, den &lt;Text&gt; enthalten](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Filter#Medienobjekte.2C_deren_Notizen.2C_den_.3CText.3E_enthalten)
- Etikett : [Medienobjekt mit dem &lt;Etikett&gt;](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Filter#Medienobjekt_mit_dem_.3CEtikett.3E)
- Benutzerfilter : [Medienobjekte entsprechend &lt;Filter&gt;](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Filter#Medienobjekte_entsprechend_.3CFilter.3E)

{{-}}

#### Notiz Filter

![[_media/FilterGramplet-Notes-detached-default-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Notiz - Filter Gramplet - freistehend - Vorgabe]] Äquivalent zu den integrierten [eigenen Filterregeln](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Filter#toc):

- ID : [Notizen, deren ID den &lt;Text&gt; enthält](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Filter#Notizen.2C_deren_ID_den_.3CText.3E_enth.C3.A4lt)
- Text : [Notizen mit entsprechenden Parametern](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Filter#Notizen_mit_entsprechenden_Parametern)
- Art :<small>*Notizen mit entsprechenden Parametern*</small>
- Etikett : [Notizen mit dem &lt;Etikett&gt;](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Filter#Notizen_mit_dem_.3CEtikett.3E)
- Benutzerfilter : [Notizen entsprechend &lt;Filter&gt;](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Filter#Notizen_entsprechend_.3CFilter.3E)

{{-}}

### Galerie

![[_media/Gallery-Gramplet-detached-example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Galerie Gramplet - freistehend Beispiel]]

Gramplet zeigt Medienobjekte. Das erste Bild ist das primäre aktive Medienobjekt, das in Berichten und im Dialogfeld verwendet wird.

Du kannst das Kontextmenü verwenden, um mit der rechten Maustaste zu klicken und es

Ein Doppelklick auf das Bild zeigt es in der Standard-Bildbetrachtungsanwendung an.

Siehe auch:

- Um das primäre Medienobjekt für Berichte usw. zu ändern, verwende die Registerkarte [Galerie](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Daten_eingeben_und_bearbeiten:_Ausführlich_-_Teil_1#Galerie) des Dialogs .

{{-}}

#### Person Galerie

Siehe [Galerie](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Gramplets#Galerie) {{-}}

#### Familie Galerie

Siehe [Galerie](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Gramplets#Galerie) {{-}}

#### Ereignis Galerie

Siehe [Galerie](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Gramplets#Galerie) {{-}}

#### Ort Galerie

Siehe [Galerie](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Gramplets#Galerie) {{-}}

#### Quelle Galerie

Siehe [Galerie](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Gramplets#Galerie) {{-}}

#### Fundstelle Galerie

Siehe [Galerie](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Gramplets#Galerie) {{-}}

### Vornamen-Wolke

![[_media/GivenNameCloud-Gramplet-detached-example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Vornamen-Wolke Gramplet - freistehend Beispiel]]

Das Gramplet zeigt das Vornamen-Wolke Gramplet die beliebtesten Vornamen in deinem Stammbaum. Die Schriftgröße des Namens zeigt, wie beliebt er ist. Bewege die Maus über den Namen, um die genaue Anzahl und den Prozentsatz der Personen im Stammbaum mit diesem Namen anzuzeigen.

Das Gramplet teilt [bevorzugte Vornamen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Daten_eingeben_und_bearbeiten:_Ausführlich_-_Teil_1#Bevorzugter_Name_Abschnitt) in Wörter auf (durch Leerzeichen getrennt), es sei denn, es wurde ein Verbindungselement (wie ein Bindestrich oder ein geschützter Leerzeichen) angegeben, um die Namen zu einem zusammengesetzten Namen zu verbinden. Beispielsweise würde „Sarah Elizabeth“ sowohl unter „Sarah“ als auch unter „Elizabeth“ erscheinen.

Doppelklicke auf den Vornamen, um eine Schnellansicht aller passenden Personen anzuzeigen. {{-}}

Siehe auch:

- [Nachnamen-Wolke Gramplet](#Nachnamen-Wolke)

#### Vornamen-Wolke Schnellansicht

### Bildmetadaten

![[_media/ImageMetadata-Gramplet-detached-example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Bildmetadaten" Gramplet - Beispiel]]

Das Gramplet bietet eine Schnittstelle zum Betrachten von [Bild-Exif-Metadaten](https://de.wikipedia.org/wiki/Exchangeable_Image_File_Format) aus deinen Bildern (\*.jpg, \*.png. \*.tiff, \*.exv, \*.nef, \*.psd, \*.pgf). {{-}} Siehe auch das Drittanbieter:

- [Bild Exif Metadaten bearbeiten](wiki:Addon:Edit_Image_Exif_Metadata) Zusatzmodul

#### Voraussetzungen

Sobald du gexiv2 installiert hast, findest du oben eine Anleitung zum Herunterladen und Installieren dieses Zusatzmoduls...

Pyexiv2 kann auch über die Befehlszeilenschnittstelle und innerhalb eines Python-Skripts verwendet werden:

1.  Importiere die pyexiv2-Bibliothek
      
    from pyexiv2 import ImageMetadata, ExifTag
2.  gib dein Bild an
      
    image = ImageMetadata("/home/user/image.jpg")
3.  lese das Bild
      
    image.read()

Exif-, IPTC- und XMP-Metadaten-Referenz-Tags findest du [hier](http://www.exiv2.org/metadata.html).

Beispiele:

  
image\["Exif.Image.Artist"\] \# Künstler

Smith and Johnson's Photography Studio

<!-- -->

  
image\["Exif.Image.DateTime"\] \# DatumZeit

1826 Apr 12 14:00:00

<!-- -->

  
image\["Exif.Image.DateTime"\] = datetime.datetime.now() \# DatumZeit hinzufügen

<!-- -->

  
image.write() \# schreibe die Metadaten

#### Nutzungsszenario

Der bevorzugte Weg, dieses Zusatzmodul zu verwenden, ist:

1.  pyexiv2 installieren
2.  Dieses Zusatzmodul installieren
3.  Restart Gramps
4.  Klicke in der Menüleiste auf Ansichten und wähle Medienansichten
5.  Öffne die Seitenleiste
6.  Schiebe die verfügbare leere rechte Ansicht auf etwa die Hälfte des Bildschirms.
7.  Klicke mit der rechten Maustaste auf den Text auf der Registerkarte Seitenleiste und wähle Gramplet hinzufügen
8.  Wähle Bildmetadaten Gramplet
9.  Wähle ein Bild aus der linken MedienAnsicht

{{-}}

### Medienvorschau

![[_media/MediaPreview-Gramplet-detached-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Medienvorschau Gramplet - freistehend Beispiel]]

Gramplet zeigt eine Vorschau des einzelnen primären Medienobjekts an, sofern vorhanden. {{-}} Siehe [Medienkategorie](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Kategorien#Medienkategorie)

### Notizen

![[_media/Notes-Gramplet-detached-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Notizen Gramplet - freistehend Beispiel]]

Gramplet zeigt die Notizen der aktiven Person.

Siehe auch:

- [Notizenkategorie](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Kategorien#Notizenkategorie)
- [Informationen über Notizen bearbeiten](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Daten_eingeben_und_bearbeiten:_Ausführlich_-_Teil_2#Informationen_.C3.BCber_Notizen_bearbeiten)
- [Notiz Gramplet](wiki:Addon:NoteGramplet) - Drittanbieter-Zusatzmodul

{{-}}

#### Person Notizen

Siehe [Notizen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Gramplets#Notizen) {{-}}

#### Familie Notizen

Siehe [Notizen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Gramplets#Notizen) {{-}}

#### Ereignis Notizen

Siehe [Notizen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Gramplets#Notizen) {{-}}

#### Ort Notizen

Siehe [Notizen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Gramplets#Notizen) {{-}}

#### Quelle Notizen

Siehe [Notizen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Gramplets#Notizen) {{-}}

#### Fundstelle Notizen

Siehe [Notizen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Gramplets#Notizen) {{-}}

#### Aufbewahrungsort Notizen

Siehe [Notizen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Gramplets#Notizen) {{-}}

#### Medium Notizen

Siehe [Notizen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Gramplets#Notizen) {{-}}

### Ahnentafel

![[_media/Pedigree-Gramplet-detached-example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Ahnentafel Gramplet - freistehend Beispiel]]

Das Gramplet zeigt eine komprimierte Ansicht der direkten Vorfahren der aktiven Person. Standardmäßig geht es 100 Generationen zurück. Die Namen können angeklickt werden, um die aktive Person zu ändern, Rechtsklick, um die Person zu bearbeiten. Am unteren Rand des Gramplets ist die Anzahl der Personen pro Generation aufgeführt. Geburts- und Sterbedatum werden neben dem Namen jeder Person angezeigt. Doppelklicke auf die Generationsnummer, um die übereinstimmenden Personen anzuzeigen.

Die Verwendung des Inhalts der Ahnentafel in einem anderen Programm erfordert ein wenig Aufwand. Öffne ein kontextbezogenes Aufklappmenü, indem du mit der rechten Maustaste auf eine beliebige Stelle im Gramplet außer einem Hotlink klickst. Oder du kannst eine Ziehauswahl aus denselben inaktiven Bereichen beginnen. Kopiere den markierten Text aus demselben Kontextmenü in die Zwischenablage des Betriebssystems. (Die Tastenbelegung für 'Kopieren' funktioniert nicht.) Wenn du den Text in ein anderes Textbearbeitungsprogramm einfügst, musst du möglicherweise die Schriftart in eine nicht proportionale Schriftart ändern, um die Einrückung beizubehalten. Einige Onlinedienste reduzieren führende Leerzeichen, wenn du einen Textblock versendest. Um den Einzug für solche Dienste beizubehalten, müssen möglicherweise doppelte Leerzeichen durch doppelte Platzhalterzeichen ersetzt werden... z.B. Punkte.

#### ⚙ Konfigurierbare Optionen

- 1 bis 100 Grenze; (Standardeinstellung: *100*) - Maximal anzuzeigende Generationen.

-  (Standardeinstellung: Kontrollkästchen ausgewählt)

- - <abbr title="Grafische Symbole im Unicode-Transformationsformat">**UTF**</abbr> (Standardeinstellung)
  - <abbr title="American Standard Code for Information Interchange Textsymbole">*ASCII*</abbr>;

### Python-Auswertung

![[_media/PythonEvaluationGramplet-detached-example-60.png|Abb.{{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Python Auswertung Gramplet - freistehendes Beispiel]] Das Gramplet Fensterwerkzeug ist dazu gedacht, Python-Skripte mit Gramps-Daten zu testen.

#### Anwendungsbeispiel

Beispielcode zum Auflisten der internen "[Konstanten](https://github.com/gramps-project/gramps/blob/master/gramps/gen/const.py)" von Gramps: "[Konstanten](https://github.com/gramps-project/gramps/blob/master/gramps/gen/const.py)":

    import os
    import sys
    from gramps.gen.const import *

    # Get all uppercase variables from the current namespace
    ENV = {
        name: value for name, value in locals().items()
        if name.isupper() and not name.startswith('_') and isinstance(value, str)
    }

    # Print each item in the dictionary, indicating if it's a hidden directory
    for key, value in ENV.items():
        try:
            if os.path.isdir(value):
                if sys.platform.startswith('win'):
                    import ctypes
                    attrs = ctypes.windll.kernel32.GetFileAttributesW(value)
                    hidden_status = "HIDDEN" if attrs != -1 and bool(attrs & 2) else "NOT HIDDEN"
                else:
                    hidden_status = "HIDDEN" if os.path.basename(value).startswith('.') else "NOT HIDDEN"
                print(f"({hidden_status})    {key}  :    {value}")
            else:
                print(f"{key}  :    {value}     (NOT A DIRECTORY)")
        except Exception as e:
            print(f"{key}  :    {value}     (ERROR :    {str(e)})")

#### Siehe auch

- [Python-Shell](wiki:Addon:Python_Shell_Gramplet) ZUsatzmodul Gramplet. Wenn möglich, verwende die **Python Shell** anstelle von **Python Eval**. Sie verfügt über zusätzliche Garbage-Collection-Funktionen
- Untermenü Fehlersuche im Menü [Werkzeuge](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Navigation#Werkzeuge) vor Version 4.0.2
- [Gramps-devel](wiki:De:Kontakt#Mailinglisten) Mailingliste: [Werkzeuge in Gramplets umwandeln](https://sourceforge.net/p/gramps/mailman/gramps-devel/thread/524D973D.9000604%40hotmail.com/#msg31477962) - Okt 2013
- Diskurs - Beispielskripte:
  - [Beispielskript zum Parsen von ausgewähltem JSON in CSV](https://gramps.discourse.group/t/need-some-json-parsing-tools/6855/7)
  - [Fehlerbehebung bei Gramps Pfaden und Umgebungsvariablen](https://gramps.discourse.group/t/troubleshooting-gramps-paths-and-environmental-variables/5692)
- [Kommandozeile: Python Optionen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Kommandozeilen_Referenz#Python_Optionen)
- [Uncollected Objects](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Gramplets#Uncollected_Objects) Gramplet

{{-}}

### Schnellansicht

![[_media/QuickView-Gramplet-detached-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Schnellansicht Gramplet - freistehend Beispiel]]

Das -Gramplet ermöglicht die dynamische Aktualisierung des ausgewählten [Schnellansichtsberichts](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte_-_Teil_8#Schnellansichten), wenn aktive Datensätze geändert werden. Anstelle eines Fensters mit einem statischen Bericht wird das Gramplet aktualisiert, wenn verschiedene aktive Datensätze innerhalb der Zielkategorie ausgewählt werden. (Als dieses Gramplet eingeführt wurde, bot es nur die Auswahl von Schnellansichtsberichten aus der Kategorie „Personen“ an. Seitdem wurde ein Popup-Menü zur Auswahl der Ansichtskategorien hinzugefügt.)

Du kannst jede der integrirten [Schnellansicht](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte_-_Teil_8#Schnellansichten) oder [zusätzliche](wiki:6.0_Addons#Addon_List) Schnellansichtsberichte ausführen. {{-}} ![[_media/QuickView-Gramplet-Configuration-tab-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Schnellansicht Gramplet - zeigt Registerkarte Konfiguration]]

Du kannst die Optionen ändern, indem du auf die Optionsschaltfläche (obere, linke Schaltfläche des Gramplets) klickst, wodurch das Gramplet freigestellt und in einem Fenster geöffnet wird. Wähle in der obersten Zeile und eine Liste mit Optionen wird angezeigt. Drücke , um die Änderungen auf die Schnellansicht zu übernehmen. Du kannst dann das Fenster schließen, um das Gramplet wieder einzubinden.

{{-}} Sieh dir die folgenden Entwicklerinformationen an, wenn du daran interessiert bist, deine eigenen zu erstellen:

- [Deine eigene Schnellansicht erstellen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte_-_Teil_8#Deine_eigene_Schnellansicht_erstellen).

{{-}}

### Rekorde

![[_media/Records-Gramplet-detached-51-de.png|Abb{{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Rekorde Gramplet - freistehend Beispiel]]

Das Rekorde Gramplet zeigt eine Reihe interessanter Rekorde (meistens altersbezogen) aus deiner Datenbank. Die Liste zeigt die Top 3 für jedes Element.

- Personen Rekorde:
  - Jüngste lebende Person
  - Älteste lebende Person
  - Jüngste gestorbene Person
  - Älteste gestorbene Person
  - Bei der Heirat jüngste Person
  - Bei der Heirat älteste Person
  - Bei der Scheidung jüngste Person
  - Bei der Scheidung älteste Person
  - Jüngster Vater
  - Jüngste Mutter
  - Ältester Vater
  - Älteste Mutter
- Familien Rekorde
  - Paar mit den meisten Kindern
  - Kürzeste noch andauernde Ehe
  - Längste noch andauernde Ehe
  - Kürzeste beendete Ehe
  - Längste beendete Ehe

{{-}} Die Liste ist nicht nur für sich interessant, sie ist auch eine gute Plausibilitätsüberprüfung der Daten. Für einige Elemente musst du einige zusätzliche Informationen eingeben.

Das folgende Beispiel zeigt das es hier ein Hochzeitsereignis (von welchem die Länge berechnet wurde) aber keine der Personen hat ein Todesereignis. Auch wenn das Datum unbekannt ist, füge den Partnern ein Tod Ereignis hinzu und die Liste wird korrigiert.

**Längste noch andauernde Ehe**

1.  van Dosselaere, Egidius und Rechters, Petronella (382 Jahre, 1 Monat)
2.  de Richter, Petrus und Asscericx, Catharina (379 Jahre, 9 Monate)

{{-}}

Ein identischer [Rekordebericht](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte_-_Teil_6#Rekordebericht) ist ebenfalls verfügbar.

### Referenzen

![[_media/References-Gramplet-detached-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Referenzen Gramplet - freistehend Beispiel]] Gramplet zeigt die Referenzen der aktiven Person

{{-}}

#### Person Referenzen

- Person Referenzen : Gramplet zeigt die Rückverweis Referenzen für eine Person

Siehe [Referenzen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Gramplets#Referenzen) {{-}}

#### Familie Referenzen

- Familie Referenzen : Gramplet zeigt die Rückverweis Referenzen für eine Familie

Siehe [Referenzen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Gramplets#Referenzen) {{-}}

#### Ereignis Referenzen

- Ereignis Referenzen : Gramplet zeigt die Rückverweis Referenzen für ein Ereignis

Siehe [Referenzen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Gramplets#Referenzen) {{-}}

#### Ort Referenzen

- Ort Referenzen : Gramplet zeigt die Rückverweis Referenzen für einen Ort

Siehe [Referenzen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Gramplets#Referenzen) {{-}}

#### Quelle Referenzen

- Quelle Referenzen : Gramplet zeigt die Rückverweis Referenzen für eine Quelle

Siehe [Referenzen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Gramplets#Referenzen) {{-}}

#### Fundstelle Referenzen

- Fundstelle Referenzen : Gramplet zeigt die Rückverweis Referenzen für eine Fundstelle

Siehe [Referenzen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Gramplets#Referenzen) {{-}}

#### Aufbewahrungsort Referenzen

- Aufbewahrungsort Referenzen : Gramplet zeigt die Rückverweis Referenzen für einen Aufbewahrungsort

Siehe [Referenzen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Gramplets#Referenzen) {{-}}

#### Medium Referenzen

- Medium Referenzen : Gramplet zeigt die Rückverweis Referenzen für ein Medienobjekt

Siehe [Referenzen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Gramplets#Referenzen) {{-}}

#### Notiz Referenzen

- Notiz Referenzen : Gramplet zeigt die Rückverweis Referenzen für eine Notiz

Siehe [Referenzen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Gramplets#Referenzen) {{-}}

### Verwandte

![[_media/Relatives-Gramplet-detached-example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Angehörige Gramplet - freistehend Beispiel]]

Verwende das Gramplet , um alle direkten Verwandten der aktiven Person anzuzeigen. Es ist als Navigationshilfe gedacht, als alternative Möglichkeit, sich in Gramps durch deinen Stammbaum zu bewegen. Wenn du das Gramplet löst und neben Gramps platzierst, kannst du damit ganz einfach den Inhalt der aktuellen „Personenansicht” ändern.

Wenn du in der Schaubilderkategorie Ahnentafelansicht arbeitest, ist die aktive Person die Person ganz links. Durch Klicken auf einen Namen im Verwandte-Gramplet kannst du die aktive Person einfach ändern, und alle Personenansichten im anderen Fenster werden aktualisiert. Da das Verwandte Gramplet alle Ehepartner, alle Kinder und alle Eltern anzeigt, bietet dies eine alternative Möglichkeit zur Navigation durch deine Daten.

Die Namen in diesem Gramplet ermöglichen es dir auch, den Personeneditor direkt aufzurufen, indem du mit der rechten Maustaste auf einen der Namen klickst.

Das Verwandte Gramplet kann den folgenden Kategorien hinzugefügt werden:

- Personen Kategorie
- Beziehungen Kategorie
- Schaubilder Kategorie
- Geografie Kategorie (Nur ausgewählte Ansichten)

{{-}} Siehe auch:

- Gramplet - Vorfahren der aktiven Person Navigationshilfe.

### Wohnort

![[_media/ResidenceGramplet-Person-detached-example-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Person - Wohnort Gramplet - freistehend Beispiel]]

Gramplet zeigt die Wohnort Ereignisse für die aktive Person {{-}}

#### Person Wohnort

Siehe [Wohnort](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Gramplets#Wohnort) {{-}}

### Sitzungsaufzeichnungen

![[_media/SessionLog-Gramplet-detached-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Sitzungsaufzeichnungen Gramplet - freistehend Beispiel]]

Die Sitzungsaufzeichnung verfolgt die Aktivitäten in dieser Sitzung. Sie listet ausgewählte und bearbeitete Objekte.

Klicke einmal auf einen Namen um diese Person zur aktiven Person zu machen. Doppelklick auf einen Namen oder eine Familie öffnet den Dialog für dieses Objekt. Außerdem, wenn du eine Person bearbeiten möchtest, aber die aktive Person nicht ändern möchtest, kannst du mit der rechten Maustaste auf den Namen der Person klicken.

Dieses Gramplet ist praktisch weil du schnell die aktive Person ändern oder ein Objekt aus der Sitzungsliste bearbeiten kannst.

`* `[<code>Verwendung des Rückgängig-Verlaufs</code>](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Navigation#Verwendung_des_R.C3.BCckg.C3.A4ngig-Verlaufs)`]`

{{-}}

### SoundEx

![[_media/SoundEx-Gramplet-detached-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} SoundEx Gramplet - freistehend Beispiel zeigt Kontextmenü an]]

Das generiert SoundEx-Codes für die Namen von Personen in dem Stambaum.

Im Fenster kannst du entweder einen aus dem Aufklappm, das durch Auswahl der Pfeilspitze nach unten (Dreieck) auswählen oder du kannst einen Namen in das Textfeld eingeben.

Der Name, den du eingibst, kann ein beliebiger Name sein... sogar ein Name, der nicht in deinem Stammbaum vorhanden ist.

Das Feld zeigt das Ergebnis automatisch an, z. B.: Der SoundEx-Code für *Simpson* lautet *S512*

Du kannst mit der rechten Maustaste auf das Feld klicken, um das Ergebnis zu kopieren.

Es steht eine Schaltfläche zur Verfügung, die dich zu dieser Seite führt. Mit der Schaltfläche (oder mit der Tastenkombination )) blendest du das SoundEx Gramplet-Fenster aus. {{-}}

#### SoundEx was ist das?

Soundex ist der bekannteste aller [phonetischen Algorithmen](https://de.wikipedia.org/wiki/Phonetische_Suche), die eine Indizierung von Wörtern nach ihrem Klang ermöglichen, wie sie im Englischen ausgesprochen werden. Soundex-Unterstützung ist bei der Suche über eine [Soundex passt auf Personen mit dem <Namen>](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Filter#Soundex_passt_auf_Personen_mit_dem_.3CNamen.3E) Filterregel, einem [Soundex-Gramplet](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Gramplets#SoundEx) und als Qualitätskontrolle für den Abgleich mit dem Werkzeug [Finde mögliche doppelte Personen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Werkzeuge#Finde_m.C3.B6gliche_doppelte_Personen) enthalten.

Der Soundex ist ein kodierter Nachnamenindex mehr darauf basierend wie ein Name ausgesprochen wird als darauf wie er buchstabiert wird. Nachnamen die gleich klingen aber unterschiedlich geschrieben werden wie MAYER und MEIER werden gleich kodiert und zusammen abgelegt. Das Soundex Code System wurde entwickelt so das man Nachnamen finden kann auch wenn sie in verschiedenen Schreibweisen aufgezeichnet wurden.

Zuerst beim US Zensus von 1880 eingesetzt ist Soundex ein "phonetischer Index" kein strikt alphabetischer. Sein Hauptmerkmal ist, dass er Nachnamen auf der Basis wie sie klingen und weniger wie sie geschrieben werden kodiert. Das phonetische Codierungssystem von Soundex ist älter als Computer und sollte Forschern helfen, einen Nachnamen schnell zu finden, auch wenn er möglicherweise in verschiedenen Schreibweisen vor kam.

Diejenigen, die Zensus Nachforschungen anstellen, müssen die selbe Methode zum kodieren von Nachnamen verwenden, wie die Volkszähler als sie die Datenbasis erstellt haben.

Um nach einem bestimmten Nachnamen zu suchen, müsst du zunächst dessen Codierungsäquivalent ermitteln.

- **Grundregeln zur Soundexkodierung:**

Jeder Soundex-Code besteht aus einem Buchstaben und drei Zahlen, beispielsweise W-252. Der Buchstabe ist immer der Anfangsbuchstabe des Nachnamens. Die Nummern werden den restlichen Buchstaben des Nachnamens gemäß der unten gezeigten Soundex-Anleitung zugewiesen. Am Ende werden bei Bedarf Nullen hinzugefügt, um einen vierstelligen Code zu erzeugen. Zusätzliche Buchstaben werden nicht berücksichtigt. Beispiele: Washington wird kodiert als W-252 (W, 2 für das S, 5 für das N, 2 für das G, die restlichen Buchstaben werden nicht beachtet). Lee wird L-000 kodiert (L, 000 hinzugefügt).

| Nummer | Repräsentiert die Buchstaben |
|--------|------------------------------|
| 1      | B, F, P, V                   |
| 2      | C, G, J, K, Q, S, X, Z       |
| 3      | D, T                         |
| 4      | L                            |
| 5      | M, N                         |
| 6      | R                            |

Ignoriere die Buchstaben A, E, I, O, U, H, W und Y.

- **Erweiterte Regeln zur Soundexkodierung:**
  - Namen mit doppelten Buchstaben: Wenn ein Nachname doppelte Buchstaben hat, werden sie wie ein Buchstabe behandelt. Zum Beispiel:
    - Gutierrez wird kodiert als G-362 (G, 3 für das T, 6 für das erste R, zweite R wird ignoriert, 2 für das Z).
  - Namen mit Buchstaben nebeneinander, die dieselbe Soundex-Codenummer haben: Wenn der Nachname im Soundex-Codierungsleitfaden verschiedene Buchstaben mit derselben Nummer hat, sollten sie als ein Buchstabe behandelt werden. Beispiele:
    - Pfister wird kodiert als P-236 (P, F ignoriert, 2 für das S, 3 für das T, 6 für das R).
    - Jackson wird kodiert als J-250 (J, 2 für das C, K ignoriert, S ignoriert, 5 für das N, 0 hinzugefügt).
    - Tymczak wird kodiert als T-522 (T, 5 für das M, 2 für das C, Z ignoriert, 2 für das K). Da der Vokal "A" das Z und das K trennt, wird das K kodiert.
  - Namen mit Präfixen: Wenn ein Nachname einen Präfix wie Van, Con, De, Di, La oder Le besitzt, kodiere beides mit und ohne den Präfix, weil der Nachname unter beiden Kodierungen gespeichert sein kann. Beachte jedoch das Mc und Mac nicht als Präfixe betrachtet werden. Zum Beispiel kann VanDeusen auf zwei Arten kodiert werden: V-532 (V, 5 für N, 3 für D, 2 für S) oder D-250 (D, 2 für das S, 5 für das N, 0 hinzugefügt).
  - Konsonanten Trennzeichen: Wenn ein Vokal (A, E, I, O, U) zwei Konsonanten mit dem selben Soundex-Code trennt, wird der Konsonant rechts neben dem Vokal kodiert. Beispiel:Tymczak wird kodiert als T-522 (T, 5 für das M, 2 für das C, Z ignoriert (siehe "nacheinander" Regel oben), 2 für das K). Da der Vokal "A" das z und das K trennt, wird das K kodiert. Wenn "H" oder "W" zwei Konsonanten mit dem selben SoundEx-Code trennen, wird der Konsonant rechts neben dem Vokal kodiert. Beispiel: Ashcraft wird kodiert A-261 (A, 2 für das S, C ignoriert, 6 für das R, 1 für das F). Es wird nicht kodiert als A-226.

Bitte besuche die [NARA Soundex Indexing-Seite](http://www.archives.gov/research/census/soundex.html), um mehr über das Soundex Indexing System zu erfahren. {{-}}

### Statistik

![[_media/Statistics-Gramplet-detached-example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Statistik Gramplet - freistehend Beispiel]]

Das Gramplet erstellt einen Statistikbericht. Doppelklicke auf die Ausdrücke, um die Schnellansichtsberichte der passenden Elemente anzuzeigen.

Folgende Informationen werden dir in diesem Gramplet zur Verfügung gestellt:

- **Personen**
  - Personenzahl
  - Männer
  - Frauen
  - Personen mit anderem Geschlecht
  - Personen mit unbekanntem Geschlecht
  - Unvollständige Namen
  - Personen ohne Geburtsdatum
  - Einzeln stehende Personen
- **Familieninformation**
  - Familienzahl
  - Eindeutige Nachnamen
- **Medienobjekte**
  - Personen mit Medienobjekten
  - Gesamtanzahl der Medienobjektreferenzen
  - Anzahl von einzelnen Medienobjekten
  - Gesamtgröße der Medienobjekte
  - Fehlende Medienobjekte

Wie bei allen Gramplets wenn du links auf die Schaltfläche klickst, löst du das Fenster und wenn du Personen deinem Stammbaum hinzufügst, siehst du, das sich die Anzahl der Personen dynamisch ändert.

Die in diesem Gramplet angegebenen Informationen entsprechen denen im [Datenbank-Zusammenfassungsbericht](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte_-_Teil_6#Datenbank.C3.BCbersichtbericht) und ähneln den Ergebnissen aus dem Dialogfeld [Datenbankinformationen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Stammbäume_Verwalten#Dialogfeld_Datenbankinformationen). {{-}}

#### Schnellansichten

### Nachnamen-Wolke

![[_media/SurnameCloud-Gramplet-detached-example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Nachnamen-Wolke Gramplet - freistehend Beispiel]]

Das Nachnamen-Wolke Gramplet zeigt (standardmäßig) die 150 am häufigsten vorkommenden Nachnamen. Die Schriftgröße der Namen ist proportional zur Anzahl der Personen mit demselben Namen.

Doppelklicke einen Nachnamen um die zu starten. Dies öffnet das Fenster, in dem alle Personen mit diesem oder alternativen Namen aufgeführt sind. Person, Geburtsdatum und Namensart werden angegeben.

Wenn du mit der Maus über einen Namen fährst, siehst du die genaue Anzahl und die prozentuale Häufigkeit.

Am unteren Rand des Gramplets wird Folgendes angezeigt:

- Gesamtzahl der eindeutigen Nachnamen:
- Gesamtzahl der angezeigten Nachnamen:
- Gesamtzahl der Personen:

Über das Kontextmenü kannst du den Text auswählen und an anderer Stelle kopieren. {{-}} ![[_media/SurnameCloud-Gramplet-Configuration-tab-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Nachnamen-Wolke Gramplet - zeigt Registerkarte Konfiguration]]

Du kannst die Anzahl der angezeigten Nachnamen sowie die minimale und maximale Schriftgröße ändern, indem du die Ansicht für dieses Gramplet konfigurierst. {{-}}

#### Schnellansicht

<span id="Person Zu erledigen"></span><span id="Familie Zu erledigen"></span><span id="Ereignis Zu erledigen"></span><span id="Ort Zu erledigen"></span><span id="Quelle Zu erledigen"></span><span id="Fundstelle Zu erledigen"></span><span id="Aufbewahrungsort Zu erledigen"></span><span id="Medium Zu erledigen"></span>

### Zu erledigen

![[_media/ToDo-Gramplet-detached-default-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Zu erledigen Gramplet - freistehend Beispiel]] Das **Gramplet** zeigt einen Freiform-Textbereich an, der den Inhalt von Notizobjekten des Typs "Zu erledigen" anzeigt. Die Art der Zu-erledigen-Notiz wird nach der aktuellen Kategorie gefiltert.

Du kannst diesen Bereich verwenden, um einige Notizen, Bemerkungen und Dinge zu notieren, die du benötigst, um deine Forschung in Gang zu bringen. Es gibt mehrere andere Zu erledigen Programme (z.B. [Tomboy](https://github.com/tomboy-notes/tomboy-ng) und andere), aber diese Gramplets sind nützlich, da die Informationen in der Gramps-Datenbank verbleiben.

Das Zu erledigen Gramplets ermöglichen es dir, Notizen zu erstellen und sie an Gramps-Objekte anzuhängen. Du kannst beispielsweise ein Person Zu erledigen Gramplet zur Seitenleiste der Personenansicht hinzufügen. Notizen, die mit diesem Gramplet hinzugefügt wurden, werden an die derzeit aktive Person angehängt. Es gibt ein Zu erledigen Gramplet für jeden primären Gramps Objekttyp. {{-}} Siehe auch das [Zusatzmodul von Drittanbietern](wiki:Third-party_Addons):

- [ToDo Notes Gramplet](wiki:Addon:ToDoNotesGramplet) für die Übersicht verfügbar, das alle Zu erledigen-Notizen in der Datenbank zusammen mit dem Objekt auflistet, an das sie angehängt sind.

{{-}}

### Häufigste Nachnamen

![[_media/TopSurnames-Gramplet-detached-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Häufigste Nachnamen Gramplet - freistehend Beispiel]]

Das Gramplet zeigt eine Liste der 10 häufigsten Nachnamen (Standard) an und ist standardmäßig in der Übersicht-Kategorie installiert.

Die Top 10 werden wie folgt präsentiert:

- Nachname
- prozentual
- Vorkommen

Die Liste zeigt dir auch die Anzahl verschiedener Nachnamen in der Datenbank wie die Anzahl der Personen in deiner Datenbank.

Klicke einen Nachnamen doppelt um die zu öffnen. Dies öffnet das Fenster mit den Personen mit dem von dir doppelt angeklickten Nachnamen.

Es wird eine Tabelle gezeigt, mit allen Personen mit einem passenden Nachnamen oder alternativen Namen. Namen der Person, ID, Geburtsdatum und Namensart wird angezeigt. {{-}}

{{-}}

### Uncollected Objects

![[_media/UncollectedObjects-Gramplet-detached-example-60.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Uncollected Objects Gramplet" - freistehend Beispiel]]

Das Gramplet soll die Low-Level-Python-Objekte auflisten, die im Speicher verbleiben und nicht (einfach) automatisch gelöscht werden können, wenn sie nicht mehr verwendet werden. Entwickler verwenden es, um zu versuchen, die Quelle von 'Speicherlecks' zu identifizieren, die dazu führen, dass Gramps immer mehr Speicher verwendet, je länger es verwendet wird.

Da das Werkzeug versucht, Objekte anzuzeigen, die möglicherweise noch gelöscht werden, treten manchmal Probleme auf.

Um diese Funktion zu nutzen, klicke auf die Schaltfläche . Wenn Ergebnisse vorhanden sind, werden diese in einer Liste mit den folgenden Spalten angezeigt: `Anzahl`, `Referrer`, `Uncollected object`.

Siehe auch:

- [Kommandozeile: Python Optionen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Kommandozeilen_Referenz#Python_Optionen)
- [Python-Auswertung](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Gramplets#Python-Auswertung) Gramplet

{{-}}

### Willkommen bei Gramps!

![[_media/Welcome-to-Gramps-Gramplet-detached-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Willkommen bei Gramps! Gramplet - freistehend Beispiel]]

Das Gramplet **Willkommen bei Gramps!** gibt neuen Benutzern eine Einführungsmeldung und einige grundlegende Anweisungen und ist standardmäßig in der Übersicht-Kategoriewentansicht installiert.

Die Willkommensnachricht beschreibt was Gramps ist, dass das Programm Open Source Software ist und wie man einen [Stammbaum](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Stammbäume_Verwalten) startet. {{-}}

### Was als nächstes?

![[_media/WhatsNext-Gramplet-detached-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Was als nächstes? Gramplet - freistehend Beispiel]]

Das **** Gramplet zeigt eine Liste der "dringlichsten" Informationslücken in deinem Stammbaum. Sie basiert auf folgenden Annahmen:

- Die [Hauptperson](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Navigation#Die_Hauptperson_setzen) definiert den Schwerpunkt
- Sucht nach Lücken. Die Suche beginnt mit den Nachkommen der Ausgangsperson und arbeitet sich im Stammbaum nach oben.
- Der Datensatz für jede Person soll Folgendes enthalten: Vorname, Nachname, Geburt (mit Datum und Ort) und Tod (mit Datum und Ort)
- Du willst die Eltern kennen, ihre Heirat (mit Datum und Ort) und - falls geschieden - Scheidungsdatum und -ort jeder Familie mit verheirateten Eltern
- Du willst zumindest die Mutter jeder Familie mit unverheirateten Eltern kennen
- Je enger die Beziehung zur Hauptperson ist, desto "dringlicher" ist die Informationslücke.
- Je näher der gemeinsame Vorfahre der Hauptperson ist, desto "dringender" ist die Information (z.B. Neffen gelten als "dringender" als Onkel, obwohl beide einen Abstand von 3 Generationen haben, denn bei Neffen ist der gemeinsame Vorfahr Vater/Mutter, während bei Onkeln der gemeinsame Vorfahre Großvater/Großmutter ist)
- Heiratsdaten und personenbezogene Daten des Ehepartners sind etwas weniger "dringend" als personenbezogene Daten der direkt verwandten Person
- Halbgeschwister sind weniger "dringend" als Geschwister

Du kannst den Text aus diesem Gramplet kopieren, indem du ihn auswählst und in ein leeres Dokument einfügst. {{-}}

#### ⚙ Konfigurierbare Optionen

![[_media/WhatsNext-Gramplet-Configuration-tab-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Was als nächstes? Gramplet - zeigt Registerkarte Konfiguration]]

Das Gramplet kann zuvor verifizierte Ereignisse ignorieren, indem es einige benutzerdefinierte Markierungen verwendet. Die Markierungen werden in der Gramplets-Konfiguration ausgewählt. Du kannst beispielsweise Folgendes markieren, damit es ignoriert wird:

- dass eine Person vollständig ist
- dass eine Familie vollständig ist
- dass eine Person oder Familie ausgeklammert werden soll

{{-}}

[G](wiki:Category:De:Dokumentation)
