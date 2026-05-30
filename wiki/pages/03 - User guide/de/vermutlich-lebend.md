---
title: De:Gramps 6.0 Wiki Handbuch - Vermutlich lebend
categories:
- De:Dokumentation
managed: false
source: wiki-scrape
wiki_revid: 130616
wiki_fetched_at: '2026-05-30T18:12:25Z'
lang: de
---

{{#vardefine:chapter\|7}} {{#vardefine:figure\|0}} Der lebt Status der Personen in einer Gramps Datenbank ist wichtig, wenn du deine Daten mit anderen teilen willst aber die Daten jener, die leben schützen willst. Er kommt auch in einigen Berichten zum Einsatz. Aus diesem Grund besitzt Gramps einige Werkzeuge um zu bestimmen ob jemand lebt. Diese Seite erklärt die Details dieser Werkzeuge.

## Woher weiß Gramps, ob jemand lebt?

![[_media/EditPreferences-Limits-tab-default-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menü: "Bearbeiten&gt; Einstellungen..." - "Grenzwerte" - Registerkarte - Standardeinstellungen]]

Ein einfacher Weg festzustellen ob eine Person lebt ist nachzusehen ob sie ein Todesereignis oder ein mit dem Tod zusammenhängendes Ereignis besitzt (wie z.B. eine Beerdigung). Jedoch ist es wahrscheinlich, dass viele Personen in deiner Datenbank keine solchen Ereignisse haben, da du keine Details über ihren Tot kennst. Wenn du weißt, dass jemand tot ist, kann es eine gute Idee sein, ein Todesereignis anzulegen. Du kannst auch später nützliche Details hinzufügen (wie ein Todesort oder Platz), wenn sie bekannt sind. Ereignisse für Personen hinzuzufügen, von denen man weiß, das sie tot sind, auch wenn man keine genauen Daten hat, ist einigermaßen sinnvoll. Jedoch kann Gramps auch geschätzte Daten (oder auch nicht) für dich hinzufügen (siehe weiter unten).

Von einem Anwender zu verlangen ein Todesereignis manuell einer Person hinzuzufügen, so dass nicht angenommen wird, dass sie lebt, wäre ziemlich mühsam ---man müsste Details zu vielen Personen hinzufügen. Erinnere dich, wenn jemand als lebend gilt, soll verhindert werden, dass seine Daten exportiert werden. Deshalb besitzt Gramps eine Funktion, die auf der Basis ihrer Ereignisdaten oder ihrer Beziehung zu anderen Personen, die eventuell Ereignisdaten besitzen, berechnen kann ob eine Person wahrscheinlich lebt. Zum Beispiel: wenn eine Person keine Belege dafür hat, tot zu sein (wie ein Todes- oder Beerdigungsereignis), dann überprüft Gramps die Eltern, Kinder, Geschwister, und so weiter bis ein Beleg gefunden wird---oder keine Verbindungen mehr findet, die es überprüfen kann. Unter Verwendung von typischen Lebensaltern und Ereigniszeitspannen (wie übliche Altersunterschiede zwischen Geschwistern, übliche Lebensalter von Müttern bei der Geburt, usw.) kann Gramps vermuten ob eine Person lebt oder nicht. Wie du dir vorstellen kannst, kann dies eine bei der Ausführung zeitaufwändige Funktion sein, sie kann aber sehr nützlich sein. Die Werte für das typische Alter bei Geburt, zwischen Generationen, usw. können in der Registerkarte eingestellt werden.

Die vermutlich lebend Funktion kann überprüfen, ob eine Person zu einer bestimmten Zeit oder Zeitraum vermutlich am leben war. Dies wird im [Alter am Datum](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Gramplets#Alter_am_Datum) Gramplet verwendet, Beschreibung weiter unten. Normalerweise schätzt das System Geburts- und Todesdatum und schaut ob das Datum zwischen beiden liegt.

Jedoch gibt es einen Sonderfall: wenn du nach Personen suchst, die wahrscheinlich *Heute* am leben sind und sie ein Todesereignis haben, gelten sie als tot (auch wenn das Ereignis kein Datum enthält). Deshalb erhältst du unterschiedliche Ergebnisse wenn du schaust, wer gestern (oder letztes Jahr) vermutlich am leben war, im Vergleich dazu wer heute vermutlich am leben ist. Der Grund dafür ist, wenn du ein Todesereignis hast, weißt du, dass die Person in der Vergangenheit starb aber du weißt nicht wann. Wenn du in der Vergangenheit schaust (gestern oder davor), ob eine Person am leben war, kannst du ohne das Todesdatum zu wissen, nicht sicher sagen ob sie zu diesem Zeitpunkt schon tot war.

Wenn du Details wissen willst, warum Gramps annimmt, dass eine Person lebt oder gestorben ist, kannst du das Werkzeugerweiterung verwenden um eine Erklärung zu erhalten. Dies zeigt die geschätzten Geburts- und Todesdaten und die Beziehung zu jemanden, der ein Ereignisdatum besitzt auf dem diese basieren.

## Vermutlich lebend Proxy

Das erste Werkzeug ist der "vermutlich am leben" Proxy. Dieser wird immer automatisch verwendet, wenn du die Daten in ein Format exportierst, das die Möglichkeit Informationen für lebende Personen zu begrenzen unterstützt. Der Proxy hüllt die Datenbank in eine Schicht, die den Zugriff auf sensible Daten von lebenden Personen wie ihren Vornamen und ihre Ereignisse verhindert.

## Vermutlich lebend Filter

Das heutige Datum wird in den Fällen von Ereignissen ohne Datum und beim Überprüfen ob jemand in der Vergangenheit lebte gesondert behandelt. Zum Beispiel: wenn eine Person ein Todesereignis ohne Datum besitzt, dann wissen wir, dass diese Person heute und in der Zukunft tot ist. Jedoch für die Funktionen mit denen du überprüfen kannst, ob eine Person an einem bestimmten Datum in der Vergangenheit gelebt hat, können wir nicht sagen ob sie an diesem Datum gelebt hat oder nicht. Also wenn du ein Todesereignis ohne Datum hast, und überprüfst ob die Person gestern gelebt hat, kann Gramps unmöglich den lebt/tot Status feststellen.

Siehe:

- [Personen, die wahrscheinlich leben Filter filter](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Filter#Personen,_die_wahrscheinlich_leben)

## Kalender Gramplet

Siehe [Kalender Gramplet](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Gramplets#Kalender_Gramplet).

## Daten bearbeiten

Siehe [Daten bearbeiten](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Daten_eingeben_und_bearbeiten:_Ausführlich_-_Teil_1#Daten_bearbeiten).

[V](wiki:Category:De:Dokumentation)
