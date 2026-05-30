---
title: De:Gramps 6.0 Wiki Handbuch - Berichte - Teil 8
categories:
- De:Dokumentation
- Plugins
- Stub
managed: false
source: wiki-scrape
wiki_revid: 131119
wiki_fetched_at: '2026-05-30T17:39:51Z'
lang: de
---

{{#vardefine:chapter\|13.8}} {{#vardefine:figure\|0}} Zurück zur [Übersicht der Berichte](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte).

<hr>

{{-}} ![[_media/QuickViewReport-EditPerson-context-menu-popup-default-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Kontextmenü Schnellansicht auf Person bearbeiten]] Dieser Abschnitt beschreibt die [Schnellansichten](wiki:Quick_Views) als Teil der verschiedenen in Gramps verfügbaren Berichte.

## Schnellansichten

![[_media/QuickViewReport-SameSurname-PeopleView-example-popup-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Schnellansicht-Bericht – Personenansicht –  – Beispiel-Popup-Fenster, das das Kontextmenü der rechten Maustaste für die Ergebnistabelle anzeigt]]

**Schnellansicht**(en) sind Berichtsfenster, die über das [Kontextmenü](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Hauptfenster#Pop-up_Men.C3.BCs) der meisten Kategorieansichten und *einiger* der Bearbeitungsdialoge verfügbar sind.

Diese **Schnellansicht**(en) sind Berichte, die auf dem ersten ausgewählten Datensatz basieren und keine Optionen enthalten, die den Prozess verkomplizieren könnten. Wie bei den Hauptansichten werden jedoch auch in diesen Berichten die in den Einstellungen auf der Registerkarte „Anzeige“ ausgewählten benutzerdefinierten Formate übernommen.

**Schnellansichtsberichte** sind statisch. Der Inhalt dieser schwebenden Fenster wird nicht aktualisiert, wenn sich der Objektfokus ändert oder wenn die Datensatzdaten bearbeitet werden. Wenn du eine dynamischere Version des Berichts wünschst, kann ein zur Seitenleiste oder zur unteren Leiste hinzugefügt werden. Der Bericht wird neu generiert, wenn sich der Objektfokus verschiebt. Das Werkzeug "Konfigurieren" in der Symbolleiste (oder die Option "Konfigurieren..." im Menü "Ansicht") verfügt über eine Registerkarte "Schnellansicht", auf der du den Objekttyp und den angezeigten Bericht auswählen kannst.

### Zwischenablage von Schnellansichtsdaten

Verwende das Schnellansichtstabelle Kontextmenü (Rechtsklick) für , um den Inhalt der Schnellansicht zu markieren, der *nicht* in einer formatierten Tabelle enthalten ist. Verwende dann erneut das Kontextmenü, um den markierten Inhalt in die OS-Zwischenablage zu .

Bei Schnellansichten, die Listen von Datensätzen im Tabellenformat enthalten, kann man die Zeilendaten der Schnellansichtstabelle in die OS-Zwischenablage kopieren, indem man das Kontextmenü (Rechtsklick) innerhalb einer Tabellenzeile verwendet und die Menüoption wählt. Wenn die Schnellansicht mehrere Tabellen enthält, müssen diese einzeln kopiert werden.

#### Schnellansichtstabelle Kontextmenü

- }

- 

{{-}}

### Zugriff auf Schnellansichten

![[_media/PersonView-PeopleListView-example-with-context-menu-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Kontextmenü „Schnellansicht“ in der Kategorie „Personen“ – Personen(listen)ansicht]]

Die Schnellansichten können schwer auffindbar sein. Der direkte Zugriff auf die Schnittstelle erfolgt über Kontextmenüs und nicht über Symbole, Menüeinträge oder eine explizite Auflistung in Dialogen. Und der indirekte Zugriff ist sogar noch transparenter: Er erfolgt über Verknüpfungen oder Kontextmenüs in Gramplets oder Dialogen.

Die folgenden integrierten Schnellansichten sind über Kontextmenüs pro Kategorie verfügbar:

- *[Werkzeugbankansicht](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Kategorien#Werkzeugbankkategorie)* - **Nicht verfügbar**

  - Beachte, dass du das verwenden kannst

<!-- -->

- *[Personenansicht](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Kategorien#Personenkategorie)* und *Dialog*

  - [Alle Ereignisse](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte_-_Teil_8#Alle_Ereignisse) : Anzeige der persönlichen und familiären Ereignisse einer Person
  - [Beziehung zur Hauptperson](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte_-_Teil_8#Beziehung_zur_Hauptperson)
  - [Derselbe Nachname](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte_-_Teil_8#Derselbe_Nachname) : Personen mit dem gleichen Nachnamen wie eine Person anzeigen
  - [Derselbe Vorname](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte_-_Teil_8#Derselbe_Vorname) : Personen mit dem gleichen Vornamen wie eine Person anzeigen
  - [Geschwister](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte_-_Teil_8#Geschwister) : Anzeige der Geschwister einer Person
  - [Mütterliche Abstammungslinie](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte_-_Teil_8#Mütterliche_Abstammungslinie) : : Mutterlinie anzeigen
  - [Person Referenzen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte_-_Teil_8#Person_Referenzen) : Referenzen für einen *\<Objekttyp\>* anzeigen
  - [Väterliche Abstammungslinie](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte_-_Teil_8#Väterliche_Abstammungslinie) : Vaterlinie anzeigen

<!-- -->

- *[Beziehungenansicht](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Kategorien#Beziehungenkategorie)* - **Nicht verfügbar**

<!-- -->

- *[Familienansicht](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Kategorien#Familienkategorie)* und *Dialog*

  - [Alle Familienereignisse](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte_-_Teil_8#Alle_Familienereignisse) : Anzeige der Ereignisse der Familie und der Familienmitglieder
  - [Familie Referenzen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte_-_Teil_8#Familie_Referenzen) : Referenzen für einen *\<Objekttyp\>* anzeigen

<!-- -->

- *[Schaubilderansicht](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Kategorien#Schaubilderkategorie)* - **Nicht verfügbar**

<!-- -->

- *[Ereignisansicht](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Kategorien#Ereignissekategorie)*

  - [An diesem Tag](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte_-_Teil_8#An_diesem_Tag) : Ereignisse an einem bestimmten Tag anzeigen
  - [Ereignis Referenzen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte_-_Teil_8#Ereignis_Referenzen) : Referenzen für einen *\<Objekttyp\>* anzeigen

<!-- -->

- *[Orteansicht](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Kategorien#Ortekategorie)*

  - [Ort Referenzen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte_-_Teil_8#Ort_Referenzen) : Referenzen für einen *\<Objekttyp\>* anzeigen

<!-- -->

- *[Geografieansicht](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Kategorien#Geografiekategorie)* - **Nicht verfügbar**

<!-- -->

- *[Quellenansicht](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Kategorien#Quellenkategorie)*

  - [Quelle Referenzen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte_-_Teil_8#Quelle_Referenzen) : Referenzen für einen *\<Objekttyp\>* anzeigen

<!-- -->

- *[Fundstellenansicht](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Kategorien#Fundstellenkategorie)*

  - [Fundstelle Referenzen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte_-_Teil_8#Fundstelle_Referenzen) : Referenzen für einen *\<Objekttyp\>* anzeigen

<!-- -->

- *[Aufbewahrungsorteansicht](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Kategorien#Aufbewahrungsortekategorie)*

  - [Aufbewahrungsort Referenzen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte_-_Teil_8#Aufbewahrungsort_Referenzen) : Referenzen für einen *\<Objekttyp\>* anzeigen

<!-- -->

- *[Medienansicht](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Kategorien#Medienkategorie)*

  - [Medien Referenzen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte_-_Teil_8#Medien_Referenzen) : Referenzen für einen *\<Objekttyp\>* anzeigen

<!-- -->

- *[Notizenansicht](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Kategorien#Notizenkategorie)*

  - [Notiz Referenzen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte_-_Teil_8#Notiz_Referenzen) : Referenzen für einen *\<Objekttyp\>* anzeigen
  - [Verknüpfung Referenzen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte_-_Teil_8#Verknüpfung_Referenzen) : Link-Referenzen innerhalb einer Notiz anzeigen

Die folgenden eingebauten "Verschiedenen" Schnellansichten sind indirekt verfügbar: über Kontextmenüs in Gramplets und Dialogen:

- Alter am Datum : Anzeige der wahrscheinlich lebenden Personen und ihres Alters an einem bestimmten Datum eines Ereignisses
  - Zugriff über das [Kalender Gramplet](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Gramplets#Kalender). Ein Doppelklick auf einen Kalendertag öffnet die Schnellansicht [An diesem Tag](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte_-_Teil_8#An_diesem_Tag)
- Attributübereinstimmung : Anzeige von Personen mit einem Attribut, das einem Bezeichner entspricht
  - Zugriff über das [Attribute Gramplet](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Attributes)
- Filter nach \[benutzerdefinierter Filter\] Name :
  - Alle
  - Alle Personen
  - Alle Familien
  - Alle Ereignisse
  - Alle Orte
  - Alle Quellen
  - Alle Repositorien
  - Alle Medien
  - Alle Notizen
  - Gegenteilige Person
  - Gegenteilige Familie
  - Gegenteiliges Ereignis
  - Gegenteiliger Ort
  - Gegenteilige Quelle
  - Gegenteiliger Aufbewahrungsort
  - Gegenteilige Medien
  - Gegenteilige Anmerkung
  - männlich
  - weiblich
  - Personen mit anderem Geschlecht
  - Personen mit unbekanntem Geschlecht
  - Personen mit fehlendem Geburtsdatum
  - Personen mit Medien
  - Medien nach Größe
  - unvollständige Namen
  - nicht verbundene Personen
  - eindeutige Nachnamen
  - Liste der Personen
    - Zugriff über das [Ahnentafel Gramplet](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Gramplets#Ahnentafel) und [Altersstatistiken](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Gramplets#Altersstatistiken) Gramplet

{{-}}

### Eingebaute Schnellansichten

#### Alle Ereignisse

Beispielbericht "Alle Ereignisse" in der Schnellansicht der Personenansicht:

<center>

**Sortierte Ereignisse von Big Louie (Big Louie) Garner von Zieliński Sr**

| Ereignisart             | Ereignisdatum     | Ereignisort                     |
|-------------------------|-------------------|---------------------------------|
| Geburt \[E0001656\]     | Jun 21, 1855      | Great Falls, MT, USA            |
| Heirat \[E0002815\]     | Apr 1, 1875       | Paragould, Greene, AR, USA      |
| Tot \[E0001657\]        | Jun 28, 1911      | Twin Falls, Twin Falls, ID, USA |
| Beerdigung \[E0001658\] | Jul 1, 1911       | Twin Falls, Twin Falls, ID, USA |

</center>

#### Alle Familienereignisse

Beispielbericht "Alle Familienereignisse" in der Schnellansicht der Ansicht "Familien":

<center>

**Sortierte Ereignisse der Familie  
 Big Louie (Big Louie) Garner von Zieliński Sr - Luella Martel**

| Familienmitglieder     | Ereignisart     | Ereignisdatum     | Ereignisort     |
|----|----|----|----|
| Luella Martel \[I0000045\] | Geburt | Jan 23, 1852 | Eureka, Humboldt, CA, USA |
| Big Louie (Big Louie) Garner von Zieliński Sr \[I0000044\] | Geburt | Jun 21, 1855 | Great Falls, MT, USA, 2398756 |
| Familie | Heirat | Apr 1, 1875 | Paragould, Greene, AR, USA |
| Big Louie (Big Louie) Garner von Zieliński Sr \[I0000044\]   | Tot | Jun 28, 1911 | Twin Falls, Twin Falls, ID, USA |
| Big Louie (Big Louie) Garner von Zieliński Sr \[I0000044\] | Beerdigung | Jul 1, 1911 | Twin Falls, Twin Falls, ID, USA |
| Luella Martel \[I0000045\] | Tot | Apr 28, 1921 | Myrtle Beach, SC, USA |
| Luella Martel \[I0000045\] | Beerdigung | Apr 30, 1921 | Myrtle Beach, SC, USA |

**Persönliche Ereignisse der Kinder**

| Familienmitglieder     | Ereignisart     | Ereignisdatum     | Ereignisort     |
|----|----|----|----|
| Jesse Garner \[I0000623\] | Geburt | Jun 18, 1876 | Paragould, Greene, AR |
| Raymond Garner \[I0000624\] | Geburt | Sep 16, 1878 | Paragould, Greene, AR |
| Jennie Garner \[I0000625\] | Geburt | Sep 11, 1880 | Paragould, Greene, AR |
| Walter Garner \[I0000626\] | Geburt | Feb 17, 1882 | Paragould, Greene, AR |
| Elizabeth Garner \[I0000629\] | Geburt | 1883 |  |
| Daniel Garner \[I0000627\] | Geburt | Sep 30, 1883 | Hood River, OR, USA |
| Bertha Garner \[I0000628\] | Geburt | Mar 13, 1888 | Hagerstown, MD, USA |
| Eugene Garner \[I0000046\] | Geburt | Dez 1, 1895 | Portsmouth, OH |
| Raymond Garner \[I0000624\]   | Geburt | Jul 12, 1911 |  |
| Bertha Garner \[I0000628\] | Beerdigung | Apr 1918 | Sterling, Whiteside, IL, USA |
| Jesse Garner \[I0000623\] | Beerdigung | 1929 | Sterling, Whiteside, IL, USA |
| Daniel Garner \[I0000627\] | Beerdigung | Mrz 4, 1936 | Sterling, Whiteside, IL, USA |
| Walter Garner \[I0000626\] | Beerdigung | Okt 1946 | Sterling, Whiteside, IL, USA |
| Jennie Garner \[I0000625\] | Beerdigung | Jun 1964 | Sterling, Whiteside, IL, USA |
| Eugene Garner \[I0000046\] | Beerdigung | Mrz 3, 1984 | Twin Falls, Twin Falls, ID, USA |
| Bertha Garner \[I0000628\] | Tot | Apr 5, 1918 | Columbus, Bartholomew, IN, USA |
| Raymond Garner \[I0000624\] | Tot | Mai 2, 1921 | Astoria, OR, USA |
| Jesse Garner \[I0000623\] | Tot | Jan 21, 1929 | Cedar City, UT, USA |
| Daniel Garner \[I0000627\] | Tot | Mrz 2, 1936 | Gary, Lake, IN, USA |
| Walter Garner \[I0000626\] | Tot | Okt 23, 1946 | Battle Creek, MI, USA |
| Jennie Garner \[I0000625\] | Tot | Jun 20, 1964 | Columbus, Bartholomew, IN, USA |
| Eugene Garner \[I0000046\] | Tot | Mrz 1, 1984 | Twin Falls, Twin Falls, ID, USA |

</center>

#### An diesem Tag

![[_media/QuickViewReport-OnThisDay-example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} „An diesem Tag“ – Schnellansicht Beispiel]]

Klicke mit der rechten Maustaste auf einen ausgewählten Datensatz in der Ereignisansicht, um ihn aus dem Kontextmenü auszuwählen, oder doppelklicke auf einen Tag im [Kalender Gramplet](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Gramplets#Kalender), um die Schnellansicht zu starten. Das Schnellansichtsfenster zeigt die *Ereignisse* des ausgewählten Tages: *Ereignisse an diesem genauen Datum* und *Sonstige Ereignisse an diesem Monat/Tag in der Historie* sowie *Sonstige Ereignisse in diesem Jahr*.

Die Informationen werden in einer Tabelle dargestellt, die Folgendes zeigt:

- Datum
- Art
- Ort
- Referenz

Wähle einen Schnellansichtseintrag aus und bearbeite ihn über das Kontextmenü. Du kannst auch einen Verweis in die Zwischenablage ziehen. {{-}}

#### Väterliche Abstammungslinie

Beispielbericht "väterliche Abstammungslinie" in der Schnellansicht der Personenansicht:

<center>

<big>**Abstammung väterlicherseits für Big Louie (Big Louie) Garner von Zieliński Sr**</big>

Dieser Bericht zeigt die väterliche Abstammungslinie, auch patrilineare Abstammungslinie oder Y-Linie genannt. Die Personen in dieser Linie haben alle die gleichen Y-Chromosomen.

| Name Vater     | Geburtsdatum     | Todesdatum     | Anmerkungen     |
|----|----|----|----|
| Big Louie (Big Louie) Garner von Zieliński Sr \[I0000044\] | Jun 21, 1855 | Jun 28, 1911 |  |
| Robert Garner \[I0000106\] | Apr 24, 1826/7 (Julian) | Feb 3, 1916 | Keine Geburtsbeziehung zum Kind |
| Joseph Garner \[I0000104\] | 1792 |  |  |

<table>
<tbody>
<tr>
<td><p><strong>Männliche Nachkommen in direkter Linie</strong><br />
Big Louie (Big Louie) Garner von Zieliński Sr (Jun 21, 1855 - Jun 28, 1911)<br />
  |-Eugene Garner (Dec 1, 1895 - Mar 1, 1984)<br />
  |  |-Howard Garner (Jul 9, 1928 - )<br />
  |  |  |-Barry Garner (Dec 14, 1948 - )<br />
  |  |  |  |-Andrew Garner (Apr 11, 1999 - )<br />
  |  |  |-Gerard Garner (Jul 31, 1955 - )<br />
  |  |  |  |-Stephen Garner (Oct 5, 1983 - )<br />
  |  |  |  |-Daniel Garner (Feb 11, 1985 - )<br />
  |  |  |-David Garner (Dec 21, 1956 - )<br />
  |  |  |-Thomas Garner (Dec 10, 1965 - )<br />
  |  |-Eugene Garner ( - )<br />
  |  |  |-Francis Garner (Jan 3, 1945 - )<br />
  |  |  |-Richard Garner (Feb 28, 1947 - )<br />
  |  |  |  |-Jason Garner (Okt 20, 1975 - )<br />
  |  |  |-Michael Garner (Jun 12, 1948 - )<br />
  |  |  |  |-Michael Garner (Jun 1, 1975 - )<br />
  |  |  |-Peter Garner (Aug 5, 1954 - )<br />
  |  |  |-Mark Garner (Okt 16, 1962 - )<br />
  |  |  |-John Garner (Aug 15, 1961 - )<br />
  |  |-John Garner (Okt 29, 1925 - )<br />
  |-Jesse Garner (Jun 18, 1876 - Jan 21, 1929)<br />
  |  |-Victor Garner ( - )<br />
  |-Raymond Garner (Sep 16, 1878 - May 2, 1921)<br />
  |-Walter Garner (Feb 17, 1882 - Oct 23, 1946)<br />
  |-Daniel Garner (Sep 30, 1883 - Mar 2, 1936)</p></td>
</tr>
</tbody>
</table>

</center>

#### Mütterliche Abstammungslinie

Ähnlich wie bei der Schnellansicht der Abstammung des Vaters in der Personenansicht, wie oben beschrieben.

#### Geschwister

![[_media/QuickViewReport-Siblings-example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Schnellansicht Bericht für Geschwister]] Geschwister der aktuellen Person mit Name, Geschlecht, Geburtsdatum und Art der Beziehung (relativ zur aktuellen Person). {{-}}

#### Beziehung zur Hauptperson

![[_media/RelationToHomePerson-Quickview-example-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Beziehung zur Hauptperson Schnellansicht]] Beispielbericht "Beziehung zur Heimatperson" in der Schnellansicht der Personenansicht: {{-}}

#### Gleicher Vorname

**Derselbe Vornamen** Schnellansicht-Bericht aus der Personenansicht zeigt ein Dialogfeld mit den Informationen im folgenden Format:

        People with the given name *\<Given Name\>*

nbsp;       There are *\<count\>* people with a matching name, or alternate name.

</center>

| Person     | Geburtsdatum     | Namensart     |
|----|----|----|
| Webb, Lewis I. \[I0193\] | March 31, 1903 | Geburtsname |
| Warner, Lewis \[I1253\] | Geburtsname |  |
| Garner von Zieliński, Lewis Anderson Sr \[I0044\]   | June 21, 1855 | Geburtsname |
| Garner, Lewis \[I1105\] | November 18, 1823 | Geburtsname |

</center>

Das Kontextmenü "Alles kopieren" enthält die Tabellendaten ohne Überschriften und 2 zusätzliche Spalten zum Sortieren der Daten:  
ursprüngliche Zeilennummer, Name (im Format der Voreinstellungen) \[*\<Gramps ID\>*\], Geburtsdatum (im Format der Voreinstellungen), Namenstyp, Julianische Tageszahl (fortlaufende Zählung der Tage seit dem 1. Januar 4713 v. Chr. im proleptischen Julianischen Kalender)

    1, Webb, Lewis I. [I0193], March 31, 1903, Birth Name, 2416205
    0, Warner, Lewis [I1253], , Birth Name, 0
    2, Garner von Zieliński, Lewis Anderson Sr [I0044], June 21, 1855, Birth Name, 2398756
    3, Garner, Lewis [I1105], November 18, 1823, Birth Name, 2387218

{{-}}

#### Gleiche Nachnamen

![[_media/QuickViewReport-SameSurname-PeopleView-example-popup-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Schnellansicht-Bericht – Personenansicht –  – Beispiel-Popup-Fenster, das das Kontextmenü der rechten Maustaste für die Ergebnistabelle anzeigt]]

Der Bericht **Gleiche Nachnamen** Schnellansicht aus der Personenansicht zeigt einen Dialog mit einer Liste der Personen mit dem Nachnamen. Verwendet das gleiche Format wie die Schnellansicht der Personenkategorie [Gleicher Vorname](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte_-_Teil_8#Gleicher_Vorname).

Siehe: [Häufigste Nachnamen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Gramplets#H.C3.A4ufigste_Nachnamen) und [Nachnamen-Wolke](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Gramplets#Nachnamen-Wolke) Gramplets {{-}}

#### Kategorie Referenzen

##### Person Referenzen

- Personenreferenzen eingebaute Schnellansicht: Anzeige mit den Backlinkreferenzen für die aktive Person

##### Familie Referenzen

- Integrierte Schnellansicht für Familienreferenzen: Anzeige mit den Backlink-Referenzen für eine Familie

##### Ereignis Referenzen

- Ereignisreferenzen integrierte Schnellansicht: Anzeige mit den Backlink-Referenzen für ein Ereignis

##### Ort Referenzen

- Integrierte Schnellansicht für Ortsreferenzen: Anzeige der Backlink-Referenzen für einen Ort

##### Quelle Referenzen

- Integrierte Schnellansicht für Quellenreferenzen: Backlink-Referenzen für eine Quelle anzeigen
- Integrierte Quellen- oder Fundstellenreferenzen : Backlink-Referenzen für eine Quelle oder einer Fundstelle anzeigen

##### Fundstelle Referenzen

- Fundstellenreferenzen integrierter Schnellbericht : Backlink-Referenzen für eine Quelle oder eine Fundstelle anzeigen

##### Aufbewahrungsort Referenzen

![[_media/RepositoryReferencesQuickView-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Aufbewahrungsort-Referenzen Schnellansicht]]

Aufbewahrungsort-Referenzen integrierte Schnellansicht: Zeigt die Aufbewahrungsort-Backlink-Referenzen für Quellen an, die sich auf den aktiven Aufbewahrungsort beziehen

- Siehe [Aufbewahrungsorte Bericht](wiki:Addon:RepositoriesReport) Zusatzmodul

##### Medien Referenzen

- Integrierte Schnellansicht für Medienreferenzen: Anzeige mit den Backlink-Referenzen für ein Medienobjekt

##### Notiz Referenzen

- Integrierte Schnellansicht für Notizenreferenzen: Anzeige der Backlink-Referenzen für eine Notiz

#### Verknüpfung Referenzen

Der **Link-Referenz**-Schnellansichtsbericht aus der Personenansicht zeigt einen Dialog mit den Informationen im folgenden Format:

        Link Referenzen für diese Notiz

</center>

| Art     | Referenz     | Link-Prüfung     |
|----|----|----|
| Familie | Garner, Rita Marie/Warner, Allen Carl \[F0001\] | Ok |
| Medien | Media, 1897_expeditionsmannschaft_rio_a \[O0010\]     | Ok |
| Internet     | relative://relative.archive.tgz |  |
| Internet | relative://relative.archive.zip |  |

</center>

Das Kontextmenü variiert je nach der Art der Verknüpfung in der angegebenen Zeile.

Links, die auf einen Gramps-Objektdatensatz verweisen, bieten "Details zum *\<Objekttyp\>* anzeigen". Dies öffnet den Objekteditor. Zeilen mit Person-Objekttypen bieten eine Option zum **Aktivieren der Person.** an. Internet-Objekttypen haben keine Kontextmenü-Optionen.

Das Kontextmenü enthält die Tabellendaten ohne Überschriften und eine zusätzliche Spalte zum Sortieren der Daten:

**ursprüngliche Zeilennummer**, **Objekttyp**, **Referenz** (Linkziel), **Linkprüfung**

    0, Family, Garner, Rita Marie/Warner, Allen Carl [F0001], Ok
    1, Media, 1897_expeditionsmannschaft_rio_a [O0010], Ok
    ⋮
    8, Internet, relative://relative.archive.tgz, 
    9, Internet, relative://relative.archive.zip, 

{{-}}

### Schnellansicht-Gramplet

Konfigurierbar, um den gewünschten Schnellansichtbericht anzuzeigen.

Verfügbar für die Verwendung über und jede der Seitenleisten und unteren Leisten der Kategorieansicht.

Siehe:

- Gramplet

{{-}}

<hr />

### Schnellansichten Zusatzmodule

Sortiere die Tabelle [Zusatzmodule-Liste](wiki:6.0_Addons#Addon_List) nach der Spalte **Art** und scrolle zur Gruppierung **Schnellansicht**.

Verfügbare Erweiterungen für Schnellansichten (in der Kategorieansicht „Personen“) umfassen:

- [Alle Namen aller Personen](wiki:Addon:All_Names_Quickview)
- [Biographie](wiki:Addon:Biography_Quickview)
- [Anzahl der Nachkommen](wiki:Addon:Number_of_Descendants_Quickview) (Gesamtbeträge aufgeschlüsselt nach Generationen und zeitlichen Überschneidungen) \[\<abbr title="sic erat scriptum, recte \_\_\_\_ - lateinische Redewendung mit der Bedeutung "so wurde es geschrieben, genau \_\_\_\_"\>[recte](wiki:De:Genealogie-Glossar#recte)</abbr>: nicht das [Anzahl der Nachkommen](wiki:Addon:Descendant_Count_Gramplet) Gramplet\]
- [Anzahl der Nachkommen](wiki:Addon:Descendant_Count_Gramplet) (einfache Zählungen)
- [Anzahl der Vorfahren](wiki:Addon:NumberOfAncestorsQuickView) (nach Generation)
- [Anzahl der Nachkommen](wiki:Addon:Number_of_Descendants_Quickview) (nach Generation)
- [Zeitleiste](wiki:Addon:Timeline_Quickview) (Ereignisse im engsten Familienkreis)

### Deine eigene Schnellansicht erstellen

Du kannst deine eigenen Schnellansichten erstellen, auch wenn du nur über begrenzte Programmier-/Codierungskenntnisse verfügst.

Viele Anwender wollen schnell einen Bericht nach ihren speziellen Bedürfnissen erstellen, sind aber durch die Tatsache behindert, das sie weder Python komplett noch die Feinheiten eines so komplexen Programms wie Gramps lernen wollen.

Diese Berichte sind kurze Textberichte die der Anwender mit Gramps registrieren kann, so das sie automatisch in den Kontextmenüs erscheinen.

Dazu wurde ein [einfacher Datenbankzugriff](wiki:Simple_Access_API) und eine einfache Dokumentenschnittstelle entwickelt, um das erstellen so einfach wie möglich zu gestalten.

Um deine eigene Schnellansicht zu erstellen, besuche die [Schnellansicht programmieren Seite](wiki:Quick_Views) (englisch) {{-}}

<hr>

Zurück zur [Übersicht der Berichte](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte).

[B](wiki:Category:De:Dokumentation) [Category:Plugins](wiki:Category:Plugins)
