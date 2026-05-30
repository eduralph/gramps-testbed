---
title: De:Gramps 6.0 Wiki Handbuch - Filter
categories:
- De:Dokumentation
- Filters
- Stub
managed: false
source: wiki-scrape
wiki_revid: 131258
wiki_fetched_at: '2026-05-30T17:47:01Z'
lang: de
---

{{#vardefine:chapter\|16}} {{#vardefine:figure\|0}} ![[_media/DefineFilter-dialog-default-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}}  - Dialog - Standardeinstellungen]] Mit Hilfe von Filtern kann Gramps Operationen auf einen kleineren Teil eines Stammbaums beschränken. Der gefilterte Teil des Stammbaums hat ein bestimmtes Merkmal gemeinsam. (z.B. Frauen, die zwischen 1550 und 1575 in Frankreich geboren wurden.) Der Filter gibt an, welche Merkmale wichtig sind und erlaubt die Auswahl von Werten, nach denen gesucht werden soll. (Im Beispiel sucht der Filter nach Personen eines bestimmten Geschlechts, die an einem bestimmten Ort während eines kleinen Zeitraums ein Ereignis haben).

Die Erstellung von Datenbankabfragen ohne Fehler in der Syntax kann eine Herausforderung sein. Daher bieten Filter strukturierte und vorab getestete Datenbankabfragen, die einen Großteil der komplexen Syntax verbergen und gleichzeitig einige Sicherheitsnetze zur Vermeidung von Routinefehlern bieten. Gemeinsame Merkmale, die für die Filterung verwendet werden, werden normalerweise als "Parameter"-Felder in einem Formular dargestellt. Dann stellt das Formular eine ordnungsgemäß geschriebene Abfrage um den Parameter herum zusammen. Formulare mit mehreren Parameterfeldern führen zu komplexen Abfragen.

Listen aller derzeit in Gramps definierten Regeln für Filterabfragen. Jede dieser Regeln kann bei der Erstellung benutzerdefinierter Filter verwendet werden.

Die Regeln sind nach [Kategorien](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Filter#Welche_Filter_in_welcher_Kategorie.3F) geordnet.

## Filter vs. Suche

Es gibt zwei Hauptmethoden, um Daten in Gramps zu finden: Suchen und Filtern.

- Die Suche verwendet die [Suchleiste](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Hauptfenster#Suchleiste) oberhalb einer Ansicht (z. B. Personen, Familien usw.).  
  Die [Suchleiste](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Hauptfenster#Suchleiste) wird nur angezeigt, wenn die gesamte Seitenleiste geschlossen ist. Du kannst die Gramplet-Leisten ein- oder ausblenden, indem du die Auswahl in den Menüs oder änderst.
- Benutzerdefinierte Filter werden über Aufklappmenüs im Filter-Gramplet, in der Exportoption und in einigen Berichten ausgewählt. Sie können in Kombination mit der Suche oder eigenständig in den Gramplets der Seitenleiste/Fußleiste verwendet werden. Benutzerdefinierte Filter werden über das Filter-Gramplet oder das Menü erstellt oder bearbeitet.

(Es gibt auch ein einfaches *beim-Tippen-suchen* [Suchfeld](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Navigation#Datens.C3.A4tze_finden) zum Navigieren im aktiven Datensatzfokus innerhalb der Listenansicht und der Objektauswahllisten.)

Suche und Filter arbeiten komplett unterschiedlich und es ist sinnvoll diese Unterschiede zu verstehen:

- *Suche* - Die [Suchleiste](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Hauptfenster#Suchleiste) durchsucht die Datenbank, wie sie in den Zeilen und Spalten auf dem Bildschirm erscheint. Die Suchfunktion ist wahrscheinlich diejenige, die du am häufigsten verwenden möchtest, da sie schnell und unkompliziert ist. Aber Geschwindigkeit und Einfachheit bringen einige Einschränkungen mit sich (siehe unten).

  
Zum Beispiel, wenn du das Anzeigeformat für Namen in den Einstellungen auf "Nachname, Vorname" gesetzt hast, kannst du Namen wie "Müller, H" finden und alle passenden Zeilen werden angezeigt. Wenn du das Anzeigeformat änderst (in den Einstellungen), kannst du in diesem Format suchen (z.B. "Hans Müller").

![[_media/wiki:De:Gramps_6.0_Wiki_Handbuch_-_Hauptfenster#Suchleiste|[_media/MainWindow-SearchBar-sidebar-hidden-example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Gramps Hauptfenster mit [Suchleiste]]]]

- *Filter* - Filter verwenden ein komplexeres System. Es beschränkt sich nicht auf das, was du auf dem Bildschirm siehst, sondern prüft die tatsächlichen Daten in allen Namensfeldern und nicht nur das, was in der Ansicht angezeigt wird. Die Eingabe mehrerer Wörter führt für die meisten Textfelder einen Ausdrucksabgleich durch. Die Filterzeile Name ist jedoch weitaus leistungsfähiger. Jedes Wort in der Namenssuche wird separat behandelt, als wäre es eine Untersuche der mit dem vorherigen Suchwort gefundenen Datensätze. Und es werden gleichzeitig ***alle*** Namensfelder durchsucht.

  
z.B. eine Namenssuche nach "geo r." in der [Beispiel-Baumdatenbank](wiki:Example.gramps) findet 5 Personen: mit einer Variante 'Jr.' & 'Sr.' als Suffix und 'George's' als Vor- und Mittelnamen. Oder die Suche nach "garn ski ph" findet Phoebe Emily, die den Geburtsnamen Zieliński und den alternativen Ehenachnamen Garner hat.

![[_media/wiki:De:Gramps_Glossar#Etikett|[_media/Sidebar-PeopleTreeView-Filter-TagDropDownList-example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Gramps Filter-Seitenleiste für die Personenansicht - Beispiel für ein [Etikett]]-Aufklappmenü]]

Filter können über das Menü oder über ein spezielles Gramplet in der Seitenleiste/Bodenleiste erstellt und gesteuert werden. Die Filter-Gramplets ermöglichen einige Schnellfilter, die der [Suchleiste](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Hauptfenster#Suchleiste) ähnlich sind, aber alle Filter folgen der hier beschriebenen Unterscheidung.

Einige zusätzliche Punkte:

- Der Filter sucht auch nach alternativen und mehreren Namen; die [Suchleiste](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Hauptfenster#Suchleiste) sucht nur nach dem primären Namen, also dem, der in der Personenansicht angezeigt wird. Aus diesem Grund kann ein Filter auf "Smith" Personen auflisten, die oberflächlich betrachtet nicht übereinstimmen. Wenn du aber die Details dieser Person mit dem [Namenseditor](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Daten_eingeben_und_bearbeiten:_Ausführlich_-_Teil_3#Namenseditor) genauer untersuchst, siehst du vielleicht, dass sie einen alternativen Namen hat, der "smith" enthält.
- Der Filter erlaubt "Reguläre Ausdrücke". So kannst du alle Namen finden, die mit einem "B" beginnen und mit "er" enden: "B.\*er". Mit der [Suchleiste](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Hauptfenster#Suchleiste) ist dies nicht möglich.
- Die Suche findet nur was sichtbar ist. Wenn ein Name oder Text zu lang ist, um ihn in der Liste unter der [Suchleiste](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Hauptfenster#Suchleiste) zu sehen, dann findest du ihn nicht. Dies solltest du beachten, wenn du Notizen durchsuchst. Verwende am besten Filter für Notizen und andere lange Textfelder.
- Alle Filter arbeiten unabhängig von der Großkleinschreibung; "Schiff" passt auf "schiff", "SCHIFF", oder "ScHiFf". Wie weiter unten unter Reguläre Ausdrücke erläutert, gibt es bei der Verwendung regulärer Ausdrücke derzeit keine Möglichkeit, von der Standardeinstellung abzuweichen.

### Siehe auch

- [Datensatz finden](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Navigation#Datensatz_finden) - (auch bekannt als „interaktive Suche mit vorausgehender Eingabe“ oder „Suchen während du tippst“.)
- [Filter](wiki:De:Gramps_Glossar#Filter) - eine Definition
- [Einführung von Filtern](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Filter) im Gramps Handbuch (diese Seite)
- [Welche Filter in welcher Kategorie?](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Filter#Welche_Filter_in_welcher_Kategorie.3F)
- [Filter](wiki:De:Filter)
- [Beispielfilter](wiki:Example_filters) - Mehrstufige Filter
- [Regeln](wiki:De:Gramps_Glossar#Regel) - eine Definition
- [Zusatzmodule Liste - Regeln](wiki:6.0_Addons#Addon_List)
- [Erweitern des Filter-Regelwerks](wiki:Addon:Rule_expansions) mit Zusatzmodulen
- [Kategorie: Filter](wiki::Category:Filters)
- [Migration benutzerdefinierter Filter](wiki:Template:Backup_Omissions/de) - das Sichern eines Gramps Baums beinhaltet keine Filteranpassungen

{{-}}

## Reguläre Ausdrücke

[Reguläre Ausdrücke](https://de.wikipedia.org/wiki/Regul%C3%A4rer_Ausdruck) (auch bekannt als *regex*, *regexp* oder manchmal *rationaler Ausdruck*) sind eine komprimierte, präzise und leistungsfähige Methode zur Beschreibung von Text, der einem Muster entspricht.

Das Entwerfen eines effektiven Suchmusters kann formelhaft sein. Wie mathematische Formeln kann ein Suchmuster, das eine Teilmenge von Datensätzen findet, schnell zusammengesetzt werden, aber es ist sehr grob und langsam. Elegante und effiziente RegEx-Phrasen werden von Optimierungsexperten für Datenmanipulationen gesammelt. Es gibt viele Ressourcen (Bücher, Websites, professionelle Schulungen) für RegEx-Design und -Strategie.

Gramps verwendet reguläre Ausdrücke als Anpassungsoption, die für benutzerdefinierte Filter und in den Filter-Gramplets jeder Kategorieansicht aktiviert werden kann.

Der RegEx-Musterabgleich ist eine fortgeschrittene Funktion, weshalb das Kontrollkästchen standardmäßig nicht aktiviert ist. Bei benutzerdefinierten Filtern verfügt jede einzelne Regel über ein Kontrollkästchen in ihrem Dialogfeld Regel bearbeiten. Die Filter-Gramplets verfügen ebenfalls über Kontrollkästchen für die Option , damit reguläre Ausdrücke direkt für den Abgleich von Zeichenfolgen in ihren Textfeldern verwendet werden können.

Zum Beispiel, wenn du nach einem Nachnamen suchst, der mit einem "B" beginnt und auf "fels" endet, kannst du Reguläre Ausdrücke verwenden, um dieses Muster zu beschreiben. Er wäre **`^B.*fels`**:

- Das **`^B`** zeigt an, dass der Text mit B beginnt
- Der **`.`** steht für ein beliebiges einzelnes Zeichen (Buchstabe, Nummer oder jedes andere Zeichen)
- Der **`*`** steht für Null oder mehr beliebige vorangehende Elemente (in diesem Fall Buchstabe, Nummer oder jedes andere Zeichen)
- Das **`fels`** passt genau auf die Buchstaben f, e, l, s in der Reihenfolge.

Reguläre Ausdrücke sind sehr mächtig und es gibt viele Optionen. Wir verwenden das [Python Reguläre Ausdrücke](https://docs.python.org/3/library/re.html) System und beschreiben es hier. Zusätzlich kannst du jede Python Reguläre Ausdrücke Ressource verwenden.

Gramps ist derzeit so implementiert, dass beim Abgleich von Zeichenketten die Groß- und Kleinschreibung nicht beachtet wird (was das Gegenteil der üblichen Standardeinstellung in Python ist). Es gibt derzeit keine einfache Möglichkeit, dieses Verhalten für den relativ seltenen Zweck des Abgleichs von Zeichenketten, die in einem bestimmten Groß-/Kleinschreibungsformat in die Datenbank eingegeben wurden, außer Kraft zu setzen. Reguläre Ausdrücke in Gramps liefern derzeit identische Ergebnisse, unabhängig davon, ob die Zielzeichenkette in Großbuchstaben, Titel, Kleinbuchstaben oder einer Mischung davon eingegeben wurde.

Übersetzt mit www.DeepL.com/Translator (kostenlose Version)

*Leerraum* - Der Begriff "Leerraum" wird unten verwendet für einen oder mehrere Zeichen, die du nicht siehst. Zum Beispiel enthält Leerraum Tabulatoren, Leerzeichen und Zeilenvorschübe.

Es gibt einige Zeichen, die in Regulären Ausdrücken eine besondere Bedeutung besitzen. Diese sind:

- **`. ^ $ * + ? { } [ ] \ | ( )`**  
  Dezimalpunkt (Punkt), Caret, Dollarzeichen, Sternchen, Pluszeichen, Fragezeichen, geschweifte Klammern links und rechts, eckige Klammern links und rechts, Backslash, senkrechter Strich (Pipe), Klammern links und rechts

Sie können wie folgt verwendet werden:

- '`.`' entspricht einem beliebigen einzelnen Zeichen (Buchstabe, Nummer oder jedes andere Zeichen)
- '`^`' entspricht dem Textanfang
- '`$`' entspricht dem Textende
- '`*`' entspricht Null oder mehr der vorangehenden Elemente
- '`+`' entspricht einem oder mehr der vorangehenden Elemente
- '`?`' entspricht Null oder einem der vorangehenden Elemente (macht es optional)
- '`{`' - Definiert eine Reihe von Treffern
- '`}`' - Ende der reihe von Treffern
- '`[`' - Beginn einer Menge
- '`]`' - Ende einer Menge
- '`\`' - das nächste Zeichen ist eine spezielle Sequenz
- '`|`' - oder
- '`(`' - Beginn einer Gruppe
- '`)`' - Ende einer Gruppe

Einige der speziellen Sequenzen beginnend mit'`\`' repräsentieren eine vordefinierte Menge von Zeichen, die häufig sehr hilfreich sind, wie die menge der Ziffern, die Menge der Buchstaben oder die Menge von allem was kein Leerraumzeichen ist. Die folgenden vordefinierten spezial Sequenzen sind eine Untermenge derer, die zur Verfügung stehen.

- `\d` Entspricht einer dezimal Ziffer; dies ist gleichbedeutend mit der Gruppe `[0-9]`.
- `\D` Entspricht einem Zeichen, das keine Ziffer ist; dies ist gleichbedeutend mit der Gruppe `[^0-9]`.
- `\s` Entspricht jedem Leerraumzeichen; dies ist gleichbedeutend mit der Gruppe `[ \t\n\r\f\v]`.
- `\S` Entspricht einem Zeichen, das kein Leerraumzeichen ist; dies ist gleichbedeutend mit der Gruppe `[^ \t\n\r\f\v]`.
- `\w` Entspricht einem Buchstabe, eine Ziffer oder der Unterstrich; dies ist gleichbedeutend mit der Gruppe `[a-zA-Z0-9_]`.
- `\W` Entspricht einem Zeichen, das weder Buchstabe noch Zahl noch Unterstrich ist; dies ist gleichbedeutend mit der Gruppe `[^a-zA-Z0-9_]`.

Der komplexeste Wiederholungsfaktor ist `{m,n}` wobei `m` und `n` dezimale Ganzzahlen sind. This qualifier means there must be at least `m` repetitions, and at most `n`.

### Finde alle definierten Werte oder Leerzeichen

<span id="regex_all">Um alle Werte zu finden, passt `(.|\s)*` auf: jedes Zeichen oder jedes Leerzeichen sowie null oder mehr Wiederholungen davon.</span>

<span id="regex_null">Um leere (leere oder ungültige) Zeichenfolgen zu finden, sucht `^.{0}$` ab dem Beginn der Übereinstimmung `^` nach jedem Zeichen (außer dem Zeilenumbruch) `.` , das genau nullmal `{0}` vor dem Ende der Übereinstimmung `$` vorkommt.</span>

### Gruppen und Mengen

Gruppen werden durch die Metazeichen '`('` und '`)`' gekennzeichnet. '`('` und '`)`' haben nahezu die selbe Bedeutung wie in mathematischen Ausdrücken; sie fassen die Ausdrücke, die in ihnen enthalten sind zusammen und du kannst den Inhalt von Gruppen durch Wiederholungsfaktoren wie `*, +, ?, oder {m,n}` wiederholen. Zum Beispiel, `(ab)*` entspricht Null oder mehr Wiederholungen von `ab`.

Mengen werden durch die '`[`' und '`]`' Metazeichen gekennzeichnet.

Du kannst dir Gruppen als eine Liste von Alternativen getrennt durch das '`|`' Metazeichen vorstellen, wobei jede Alternative aus einem, mehreren oder gar keinem Zeichen und Gruppen als eine Liste von Alternativen wobei jede Alternative ein einzelnes Zeichen ist besteht.

### Beispiele

- **`^B.*ship$`** - passt auf alle Texte die mit einem 'B' beginnen, gefolgt von irgendetwas, und auf 'ship' enden.
  - passt auf: **`Blankenship`**, **`Blueship`**, **`Beeship`**
  - passt nicht auf: **`Blankenships`**
- **`^B.*ship`** - passt auf alle Texte die mit einem '`B`' beginnen, gefolgt von irgendetwas, gefolgt von '`ship`' (es kann noch mehr folgen).
  - passt auf: **`Blankenship`**, **`Blankenships`**, **`Blueship`**, **`Blueshipman`**, **`Beeship`**, **`Beeshipness`**
  - passt nicht auf: **`Blankenschips`**

#### Gebräuchliche Abweichungen eines Nachnamen

Beispiel 1  
Mit Hilfe des Ausdrucks **`Eri(ch|ck|k|c)(ss|s)on`** werden die folgenden Treffer erzielt:

<!-- -->

    Erikson
    Eriksson
    Ericson
    Ericsson
    Erickson
    Ericksson
    Erichson
    Erichsson

**Erklärung:**: Aus folgenden Gründen

- **`Eri`** = Eri
- **`(ch|ck|k|c)`** = Gruppe passt **`ch`**, **`ck`**, **`k`** oder **`c`**. Es wird zuerst bei dem längsten Teil geschaut ob es passt
- **`(ss|s)`** = Gruppe passt **`ss`** oder **`s`**. Es wird zuerst bei dem längsten Teil geschaut ob es passt
- **`on`** = on

<hr>

Beispiel 2  
Mit Hilfe des Ausdrucks **`Ba(in|yn|m|n)bri(dge|cke|g(g|e|))`** werden die folgenden Treffer erzielt:

<!-- -->

    Bainbricke
    Bainbridge
    Bainbrig
    Bainbrigg
    Bambridge
    Banbrig
    Banbrige
    Baynbrige

**Erklärung:** Aus folgenden Gründen

- **`Ba`** = Ba
- **`(in|yn|m|n)`** = Gruppe passt **in**, **yn**, **m** oder **n**. Es wird zuerst bei dem längsten Teil geschaut ob es passt.
- **`bri`** = bri
- **`(dge|cke|g(g|e|))`** = Gruppe passt **dge**, **cke** oder (**g** mit **g**, **g** mit **e** oder **g** mit nichts)

<hr>

Beispiel 3  
Mit Hilfe des Ausdrucks **`n(es|oua|oai|o[iya]|a[iy])r(r|)(on|((e|)au(x|t|d|lt|)))`** werden die folgenden Treffer erzielt:

<!-- -->

    nairaud
    nairault
    naireaud
    nayrault
    nesrau                
    nesrault
    nesreau
    nesreaud
    noirau
    noiraud
    noirauld
    noirault
    noiraut
    noiraux
    noireau
    noireaud
    noireault
    noireaut
    noirraux
    noirreau
    noirreaud
    nouarault
    noyraud
    noyrault 

**Erklärung:** Aus folgenden Gründen

- **`n`** = n
- **`(es|oua|oai|Menge1|Menge2)`** = Gruppe passt **es**, **oua**, **oai**, **Menge1** oder **Menge2**
- **`Menge1`** ist **`o[iya]`** = Gruppe passt **o** UND **i**, **y** oder **a**. In anderen Worten **oi**, **oy** oder **oa**
- **`Menge2`** ist **`a[iy]`** = Gruppe passt **a** UND **i** oder **y**. In anderen Worten **ai** oder **ay**
- **`r`** = r
- **`(r|)`** = Gruppe passt **r** oder nichts
- **`(on|(Untergruppe1)`** = Gruppe passt **on** oder **Untergruppe1**.
- **subgroup1** entspricht der Gruppe (**Untergruppe2 au Untergruppe3**)
- **Untergruppe2** ist **(e\|)** = Gruppe passt **e** oder nichts
- **`au`** = au
- **Untergruppe3** ist **(x\|t\|d\|lt)** = Gruppe passt **x**, **t**, **d** oder **lt**

#### Reguläre Ausdrücke testen

Tester für Reguläre Ausdrücke können online über Google gefunden werden. <https://regexr.com/> ist einfach und praktisch.

### Siehe auch

Reguläre Ausdrücke sind in der Computerindustrie seit den 1950er Jahren weit verbreitet. Sie sind jedoch "Expertenwerkzeuge", die eher auf Leistung und Effizienz als auf Intuitivität ausgelegt sind. Infolgedessen wurden viele Hilfen im Internet veröffentlicht.

Einige dieser Ressourcen bieten hervorragende Anleitungen. Einige haben Spickzettel. Einige haben "Sandkästen", in denen reguläre Ausdrücke in Echtzeit ausprobiert werden können.

Eine Auswahl an englischen Referenz-Websites für reguläre Ausdrücke:

- [rexegg.com](http://rexegg.com/) (Anleitungen)
- [RegexBuddy](https://www.regular-expressions.info/)
- [regex101.com](https://regex101.com/) (Sandkasten mit Rückmeldung)

## Benutzerdefinierte Filter

Du kannst eine beträchtliche Auswahl von Personen, Ereignissen, Orten usw. treffen, indem du einfach die Filter-Seitenleiste in den Ansichten Person, Ereignis, Ort usw. benutzt. Beachte jedoch, dass die Option "Reguläre Ausdrücke verwenden" **nur mit bestimmten Feldern in jeder Ansicht funktioniert**.

Wenn die Filter-Seitenleiste für deine Zwecke unzureichend ist, musst du eigene Filter erstellen. <span id="KategorieNamefilter Dialog"></span>

### <Kategorie> Filtereditor Dialog

Für jede Kategorie gibt es im Menü die . (d. h. „<Kategorie>“ ist ein Platzhalter. Wir meinen, es steht für die Person, das Ereignis, die Quellen oder andere Kategorien, die derzeit aktiv sind.) In diesem Dialogfeld werden alle benutzerdefinierten Filter aufgelistet, die für die aktuelle Kategorie spezifisch sind um diese benutzerdefinierten Filter zu verwalten. (Ähnlich wie das Dialogfeld [Etiketten organisieren](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Filter#Etiketten_organisieren_Fenster) die Verwaltung von Etiketten ermöglicht.) Es gibt keine Option zum gleichzeitigen Organisieren der benutzerdefinierten Filter in allen Kategorien.

![[_media/PersonFilters-dialog-example-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Personenfilter - Dialog - Beispiel]]

Um neue benutzerdefinierte Filter zu erstellen oder zuvor erstellte Filter anzuzeigen, verwende die Dialogliste , in der sich der *Kategoriename* je nach der Kategorie, in der du sich befindest, ändert:

-  Personenfilter

-  Familienfilter

-  Ereignisfilter

-  Ortsfilter

-  Quellenfilter

-  Fundstellenfilter

-  Aufbewahrungsortfilter

-  Medienfilter

-  Notizfilter

Im Dialogfeld hast du über die Symbole auf der rechten Seite die folgenden Optionen:

-  

  
zeigt das Dialogfeld an und fügt ein neues (noch unbenanntes) benutzerdefiniertes Filtergerüst hinzu.

-  

  
öffnet das Dialogfeld und lädt deinen vorhandenen benutzerdefinierten Filter zur Bearbeitung.

-  

  
erstellt eine exakte Kopie des ausgewählten Filters

-  

  
öffnet das Dialogfeld Ergebnisse mit einer Liste der Treffer nach einem erfolgreichen Test. Wenn der Filtertest ungültig ist, kann stattdessen ein Fehler angezeigt werden.

-  :

  
entfernt den ausgewählten Filter aus der Sammlung der benutzerdefinierten Filter von Gramps.

{{-}}

#### Filtertest Dialog

![[_media/FilterTest-results-for-TestTheSelectedFilter-button-example-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Filtertest - Beispiel einer Ergebnisliste von Personenfiltern]]

Die Ergebnisliste eines erfolgreichen Dialogs kann leer sein, ein gültiger benutzerdefinierter Filter passt möglicherweise zu keinem Datensatz. {{-}}

### Filter definieren Dialog

![[_media/DefineFilter-dialog-default-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Filter definieren - Dialog - Standardeinstellungen]]

Mit dem Dialogfeld lassen sich benutzerdefinierte Filter erstellen, die zur Auswahl von Personen in Berichten, Exporten und anderen Werkzeugen und Dienstprogrammen verwendet werden können. Dies ist in der Tat ein sehr leistungsfähiges Werkzeug für die genealogische Analyse.

Um alle zuvor von dir definierten Filter (falls vorhanden) aufzulisten, rufe das Dialogfeld auf über:

- Die Seitenleisten-/Fußleistenfilter
- In den meisten Kategorien gelangt man über das Menü zum Dialog , in dem man die Schaltfläche oder die Schaltfläche wählen kann.

Im Abschnitt **Definition** gibst du den für deinen neuen Filter ein und fügst einen hinzu, der dir helfen soll, diesen Filter in Zukunft zu identifizieren. Fügen Sie mit der Schaltfläche so viele Regeln in die ein, wie du deinem Filter hinzufügen möchtest.

<span ID="multiple_rule_options">Wenn der Filter mehr als eine Regel enthält, wähle eine der aus der Auswahlliste, mit der du festlegen kannst, ob

- **Alle Regeln müssen passen** (Standard)
- Mindestens eine Regel muss passen
- Genau eine Regel muss passen

erforderlich, damit der Filter eine Übereinstimmung erzeugt. Wenn dein Filter nur eine Regel hat, hat diese Auswahl keine Auswirkung.

- Wähle , um die Filterregel zu invertieren. Wenn du zum Beispiel die Regel **"hat einen gemeinsamen Vorfahren mit I1"** umkehrst, werden alle Personen gefunden, die keinen gemeinsamen Vorfahren mit dieser Person haben. (Standardmäßig ist das Kontrollkästchen deaktiviert)</span>

{{-}}

### Regel hinzufügen Dialog

![[_media/AddRule-selector-dialog-PersonFilters-example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Regel hinzufügen" - Auswahldialog - verfügbar für Personenfilter - Beispiel]]

Um einen neuen Filter zu definieren, klicken Sie im Dialogfeld auf die Schaltfläche , wodurch das Dialogfeld aufgerufen wird.

Der Bereich auf der linken Seite zeigt die verfügbaren Filterregeln nach Kategorien geordnet in einem erweiterbaren Baum an.

Wenn du eine ausführliche Referenz zu einer Filterregel suchst, kannst du entweder das Suchfeld benutzen, um die Regel zu finden, oder:

- Klicke auf die Pfeile, um die entsprechende Kategorie ein- oder auszuklappen.
- Wähle die Regel in der Baumstruktur aus, indem du auf ihren Namen klickst. Auf der rechten Seite werden der Name, die Beschreibung und die Werte für die aktuell ausgewählte Regel angezeigt.

Wenn du mit deiner Regelauswahl und ihren Werten zufrieden bist, klicke auf , um diese Regel zur Regelliste des aktuell bearbeiteten Filters hinzuzufügen. Wenn du auf klickst, wird das Hinzufügen der Regel zu dem Filter abgebrochen.

Siehe auch [Welche Filter in welcher Kategorie?](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Filter#Welche_Filter_in_welcher_Kategorie.3F) {{-}}

<span id="Which filters in which Category?">

## Welche Filter in welcher Kategorie?

Je nach verwendeter [Kategorie](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Kategorien) erhältst du einen anderen Satz von [Filterregeln](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Gramplets#Filter). Siehe auch [Übersicht der Gramplets](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Gramplets#.C3.9Cbersicht_der_Gramplets).

\*; Werkzeugbankkategorie: keine Filter verfügbar

\*; Personenkategorie und Beziehungenkategorie: Regeln für [Ahnenfilter](#Ahnenfilter), [Fundstellen/Quellenfilter](#Fundstellen/Quellenfilter), [Nachkommenfilter](#Nachkommenfilter), [Ereignisfilter](#Ereignisfilter), [Familienfilter](#Familienfilter), [Allgemeine Filter](#Allgemeine_Filter) und [Verwandtschaftsfilterfilter](#Verwandtschaftsfilter).

\*; Familienkategorie: Regeln für [Filter nach Kind](#Filter_nach_Kind), [Fundstellen/Quellenfilter](#Fundstellen/Quellenfilter), [Ereignisfilter](#Ereignisfilter), [Filter nach Vater](#Filter_nach_Vater), [Allgemeine Filter](#Allgemeine_Filter) und [Filter nach Mutter](#Filter_nach_Mutter),

\*; Schaubikderkategorie: Regeln für [Ahnenfilter](#Ahnenfilter), [Fundstellen/Quellenfilter](#Fundstellen.2FQuellenfilter), [Nachkommenfilter](#Nachkommenfilter), [Ereignisfilter](#Ereignisfilter), [Familienfilter](#Familienfilter), [Allgemeine Filter](#Allgemeine_Filter), und [Verwandtschaftsfilter](#Verwandtschaftsfilter)

\*; Ereignissekategorie und Medienkategorie: Regeln für [Fundstellen/Quellenfilter](#Fundstellen/Quellenfilter) und [Allgemeine Filter](#Allgemeine_Filter)

\*; Ortekategorie: Regeln für [Fundstellen/Quellenfilter](#Fundstellen/Quellenfilter), [Allgemeine Filter](#Allgemeine_Filter) und [Positionsfilter](#Positionsfilter).

\*; Geografiekategiorie: Regeln für [Ahnenfilter](#Ahnenfilter), [Fundstellen/Quellenfilter](#Fundstellen/Quellenfilter), [Nachkommenfilter](#Nachkommenfilter), [Ereignisfilter](#Ereignisfilter), [Familienfilter](#Familienfilter), [Allgemeine Filter](#Allgemeine_Filter), und [Verwandtschaftsfilterfilter](#Verwandtschaftsfilter).

\*; Quellenkategorie, Aufbewahrungsortekategorie und Notizenkategorie: nur Regeln für [Allgemeine Filter](#Allgemeine_Filter) vorhanden

\*; Fundstellenkategorie: Regeln für [Allgemeine Filter](#Allgemeine_Filter) und [Quellenfilter](#Quellenfilter)

## Ahnenfilter

Diese Kategorie umfasst die folgenden Regeln, die Personen nach ihren Ahnenbeziehungen zu anderen Personen entsprechen:

### Ist ein Vorfahre eines <Filter>Treffers

Diese Regel entspricht Personen, die Vorfahren von jemandem sind, der/die dem angegeben Filter entspricht. Der angegebene Filtername sollte aus dem Menü ausgewählt werden.

### Vorfahren von <Person>

Diese Regel entspricht Personen, die Vorfahren der angegebenen Person sind. Die Einschließlich-Option entscheidet, ob die angegebene Person als sein/ihr eigener Vorfahre betrachtet wird (nützlich beim Erstellen von Berichten). Du kannst entweder die ID in das Textfeld eingeben oder eine Person aus der Liste auswählen, indem du auf den ...-Knopf klickst. Im zweiten Fall erscheint die ID nach deiner Auswahl im Textfeld.

### Vorfahren einer <Person>, wenigstens <N> Generationen entfernt

Diese Regel entspricht Personen, die Vorfahren der angegebenen Person sind und wenigstens N Generationen von dieser Person in der Linie entfernt sind. Zum Beispiel würde diese Regel mit dem Wert 2 als Anzahl der Generationen den Großeltern, Urgroßeltern usw. entsprechen, aber nicht den Eltern der angegebenen Person.

### Vorfahren einer <Person>, nicht mehr als <N> Generationen entfernt

Diese Regel entspricht Personen, die Vorfahren der angegebenen Person sind und weniger als N Generationen von dieser Person in der Linie entfernt sind. Zum Beispiel würde diese Regel mit dem Wert 2 als Anzahl der Generationen den Eltern und Großeltern entsprechen, aber nicht den Urgroßeltern usw. angegebenen Person.

### Vorfahre einer Person aus dem Lesezeichen, nicht mehr als <N> Generationen entfernt

Entspricht beliebig vielen Generationen Vorfahren (definiert durch <n>) für jede Person in der Lesezeichenliste.

### Vorfahren der Hauptperson, weniger als <N> Generationen entfernt

Entspricht Personen, die Vorfahren der Hauptperson sind, die aber höchstens <N> Generationen entfernt sind.

### Mehrfach Vorfahren von <Person>

Entspricht Personen, die doppelt oder mehrfach Vorfahren von einer festgelegten Person sind

### Hat gemeinsame Vorfahren mit einem <Filter>Treffer

Diese Regel entspricht Personen, die gemeinsame Vorfahren mit jemand haben, der/die dem angegebenen Filter entspricht. Der angegebene Filtername sollte aus dem Menü ausgewählt werden.

### Personen mit gemeinsamen Vorfahren mit <Person>

Diese Regel entspricht Personen, die gemeinsame Vorfahren mit der angegebenen Person haben.

## Filter nach Kind

Diese Regelkategorie findet Familien mit Kindern, die der Regel entsprechen:

### Liefert Familien mit Kind dessen ID den <Text> enthält

Liefert Familien mit dem Kind mit der Gramps-ID

### Familien mit Kind mit dem <Namen>

Liefert Familien, deren Kinder den Namen oder Namensteil hat

### Familien mit Zwillingen

Liefert Familien mit Zwillingen

## Fundstellen/Quellenfilter

Diese Filter sind Ansichten spezifisch.

- [Personen- und Beziehungenkategorie](#Personen-_und_Beziehungenkategorie)
- [Familienkategorie](#Familienkategorie)
- [Ereignissekategorie](#Ereignissekategorie)
- [Ortekategorie](#Ortekategorie)
- [Medienkategorie](#Medienkategorie)

### Personen- und Beziehungenkategorie

Diese Kategorie enthält die folgenden Fundstellen und Quellen Regeln:

#### Personen mit <Anzahl> Quellen

Entspricht Personen mit einer bestimmten Anzahl von Elementen unter Quellen. Werte: Anzahl der Instanzen -- Anzahl muss größer als/kleiner als/gleich mit sein.

#### Personen mit der <Fundstelle>

Passt auf Personen mit einer Fundstelle mit einem bestimmten Wert

#### Personen mit der <Quelle>

Entspricht Personen mit einen bestimmten Quellenangabe. Werte: Quellen ID

====Personen mit mindestens einer direkten Quelle \>= <Vertrauensgrad>==== Passt zu Personen, die eine Fundstelle direkt mit dem Objekt Person verknüpft haben. Fundstellen zur Familie oder zu sekundären Objekten wie Ereignissen werden ignoriert.

Die minimal akzeptable Vertrauensschwelle ist wählbar:

Sehr niedrig, niedrig, normal, hoch, sehr hoch

### Familienkategorie

Diese Kategorie enthält die folgenden Fundstellen und Quellen Regeln:

#### Familien mit <Anzahl> Quellen

Entspricht Familien mit einer bestimmten Anzahl von Elementen unter Quellen. Werte: Anzahl der Instanzen -- Anzahl muss größer als/kleiner als/gleich mit sein.

====Familien mit mindestens einer direkten Quelle \>= <Vertrauensgrad>==== Findet Familien, die eine Fundstelle direkt mit dem Objekt Familie verknüpft haben. Fundstellen zur Person oder zu sekundären Objekten wie Ereignissen werden ignoriert.

Die minimal akzeptable Vertrauensschwelle ist wählbar:

Sehr niedrig, niedrig, normal, hoch, sehr hoch

#### Familien mit der <Fundstelle>

Passt auf Familien mit einer Fundstelle mit einem bestimmten Wert

#### Familien mit der <Quelle>

Entspricht Familien mit einen bestimmten Quellenangabe. Werte: Quellen ID

### Ereignissekategorie

Diese Kategorie enthält die folgenden Fundstellen und Quellen Regeln:

#### Ereignisse mit <Anzahl> Quellen

Entspricht Ereignissen mit einer bestimmten Anzahl von Elementen unter Quellen. Werte: Anzahl der Instanzen -- Anzahl muss größer als/kleiner als/gleich mit sein.

====Ereignisse mit mindestens einer direkten Quelle \>= <Vertrauensgrad>==== Passt zu Ereignissen, bei denen eine Quellenangabe direkt mit dem Ereignisobjekt verknüpft ist. Fundstellen zur Familie oder sekundäre Objekte wie Notizen werden ignoriert.

Die minimal akzeptable Vertrauensschwelle ist wählbar:

Sehr niedrig, niedrig, normal, hoch, sehr hoch

#### Ereignisse mit Quellen, die dem <Quellenfilter> entsprechen

Passt zu Ereignissen mit einer beliebigen Quelle (oder einer Fundstelle unter einer Quelle), die mit einem angegebenen Quellenfilter übereinstimmt und direkt mit dem Ereignisobjekt verknüpft ist. Quellen, die mit Medien oder Attributen des Ereignisses verknüpft sind, werden ignoriert.

#### Ereignisse mit der <Fundstelle>

Passt auf Ereignisse mit einer Fundstelle mit einem bestimmten Wert

### Ortekategorie

Diese Kategorie enthält die folgenden Fundstellen und Quellen Regeln:

#### Orte mit <Anzahl> Quellen

Entspricht Orten mit einer bestimmten Anzahl von Elementen unter Quellen. Werte: Anzahl der Instanzen -- Anzahl muss größer als/kleiner als/gleich mit sein.

====Orte mit einer direkten Quelle \>=<Vertrauensgrad>==== Entspricht Orten, die eine Fundstelle haben, die direkt mit dem Objekt Ort verknüpft ist. Fundstellen zu sekundären Objekten wie Notizen werden ignoriert.

Die minimal akzeptable Vertrauensschwelle ist wählbar:

Sehr niedrig, niedrig, normal, hoch, sehr hoch

#### Orte mit der <Fundstelle>

Passt auf Orte mit einer Fundstelle mit einem bestimmten Wert

#### Orte mit der <Quelle>

Entspricht Orten mit einen bestimmten Quellenangabe. Werte: Quellen ID

### Medienkategorie

Diese Kategorie enthält die folgenden Fundstellen und Quellen Regeln:

#### Medien mit <Anzahl> Quellen

Entspricht Medien mit einer bestimmten Anzahl von Elementen unter Quellen. Werte: Anzahl der Instanzen -- Anzahl muss größer als/kleiner als/gleich mit sein.

====Medien mit mindestens einer direkten Quelle \>= <Vertrauensgrad>==== Entspricht Medien, bei denen ein Quellenangabe direkt mit dem Medienobjekt verknüpft ist. Quellenangaben zu sekundären Objekten, wie z. B. Ereignissen, werden ignoriert.

Die minimal akzeptable Vertrauensschwelle ist wählbar:

Sehr niedrig, niedrig, normal, hoch, sehr hoch

#### Medien mit der <Fundstelle>

Passt auf Medien mit einer Fundstelle mit einem bestimmten Wert

#### Medien mit der <Quelle>

Entspricht Medien mit einen bestimmten Quellenangabe. Werte: Quellen ID

## Nachkommenfilter

Diese Nachkommenfilterkategorie umfasst die folgenden Regeln, die Personen nach ihren Nachkommenbeziehungen zu anderen Personen entsprechen:

### Ist Familienmitglied eines Nachkommen von <Filter>Treffer

Entspricht Personen, die Nachkommen oder Partner von jemanden sind, der dem Filter entspricht.

### Ist ein Familienmitglied eines Nachkommen von <Person>

Diese Regel entspricht nicht nur Personen, die Nachkommen der angegebenen Person, sondern auch deren (Ehe-)Partnern.

### Ist ein Nachkomme eines <Filter>Treffers

Diese Regel entspricht Personen, die Nachkommen von jemand sind, der/die dem angegebenen Filter entspricht. Der angegebene Filtername sollte aus dem Menü gewählt werden.

### Nachkommen von <Person>

Diese Regel entspricht Personen, die Nachkommen der angegebenen Person sind. Die Einschließlich-Option entscheidet, ob die angegebene Person als sein/ihr eigener Nachkomme betrachtet wird (nützlich beim Erstellen von Berichten). Du kannst entweder die ID in das Textfeld eingeben oder eine Person aus der Liste auswählen, indem du auf den ...-Knopf klickst. Im zweiten Fall erscheint die ID nach deiner Auswahl im Textfeld.

### Ist ein Nachkomme von <Person> wenigstens <N> Generationen entfernt

Diese Regel entspricht Personen, die Nachkomme der angegebenen Person sind und wenigstens N Generationen von dieser Person in der Linie entfernt sind. Zum Beispiel würde diese Regel mit dem Wert 2 als Anzahl der Generationen den Enkeln, Urenkeln usw. entsprechen, aber nicht den Kindern der angegebenen Person.

### Ist ein Nachkomme von <Person> und weniger als <N> Generationen entfernt

Diese Regel entspricht Personen, die Nachkomme der angegebenen Person sind und weniger als N Generationen von dieser Person in der Linie entfernt sind. Zum Beispiel würde diese Regel mit dem Wert 2 als Anzahl der Generationen den Kinder und Enkeln entsprechen, aber nicht den Urenkeln usw. angegebenen Person.

## Ereignisfilter

### Ereignisse, die den Parametern entsprechen

Allgemeine Filterregel, die Ereignisse mit bestimmten Parametern findet:

- 

- 

- 

- 

- 

Bietet auch die Option an.

### Diese Filter sind Ansichten spezifisch

- [Personen- und Beziehungenkategorie](#Personen-_und_Beziehungenkategorie_2)
- [Familienkategorie](#Familienkategorie_2)

### Personen- und Beziehungenkategorie

Diese Kategorie enthält die folgenden Regeln, die Personen aufgrund ihrer aufgezeichneten Ereignisse filtern:

#### Familien mit unvollständigen Ereignissen

Diese Regel passt auf Personen bei denen Datum oder Ort in den Familien Ereignissen fehlt.

#### Personen mit unvollständigen Ereignissen

Diese Regel passt auf Personen bei denen Datum oder Ort in den Persönlichen Ereignissen fehlt.

#### Personen mit <Geburtsdaten>

Diese Regel entspricht Personen, dessen Geburtsereignis angegebenen Werten für Daten, Ort und Beschreibung entspricht. Diese Regel liefert auch dann einen Treffer, wenn das Geburtsereignis nur teilweise mit den Werten Übereinstimmt. Die Regel ignoriert Groß- und Kleinschreibung. Zum Beispiel, wenn jemand in Schweden geboren wurde, entspricht er der Regel mit "schw" als Ort. Die Regel liefert einen Treffer, nur wenn alle nicht-leeren Felder (teilweise) der Geburt der Person entsprechen. Lass die anderen Felder leer, wenn du nur einen Wert verwenden willst.

#### Personen mit <Sterbedaten>

Diese Regel entspricht Personen, dessen Todesereignis angegebenen Werten für Daten, Ort und Beschreibung entspricht. Diese Regel liefert auch dann einen Treffer, wenn das Todesereignis nur teilweise mit den Werten Übereinstimmt. Die Regel ignoriert Groß- und Kleinschreibung. Zum Beispiel, wenn jemand in Schweden gestorben ist, entspricht er der Regel mit "schw" als Ort. Die Regel liefert einen Treffer, nur wenn alle nicht-leeren Felder (teilweise) dem Tod der Person entsprechen. Lass die anderen Felder leer, wenn du nur einen Wert verwenden willst.

#### Hat das familiäre <Ereignis>

Diese Regel entspricht Personen, die ein familiäres Ereignis, entsprechend den angegebenen Werten für die Art, das Datum, den Ort und die Beschreibung des Ereignisses, haben. Diese Regel liefert auch dann einen Treffer, wenn das Ereignis der Person nur teilweise mit den Werten übereinstimmt. Die Regel ignoriert Groß- und Kleinschreibung. Zum Beispiel, wenn jemand in Schweden geheiratet hat, entspricht er der Regel mit dem Hochzeitsereignis und "schw" als Ort. Die familiären Ereignisse sollten aus dem Menü ausgewählt werden. Die Regel liefert einen Treffer, nur wenn alle nicht-leeren Felder (teilweise) dem familiären Ereignis entsprechen. Lass die anderen Felder leer, wenn du nur einen Wert verwenden willst.

#### Hat das persönliche <Ereignis>

Diese Regel entspricht Personen, die ein persönliches Ereignis entsprechend den angegebenen Werten für Art des Ereignisses, Datum, Ort und Beschreibung entspricht. Diese Regel liefert auch dann einen Treffer, wenn das Ereignis der Person nur teilweise mit den Werten übereinstimmt. Die Regel ignoriert Groß- und Kleinschreibung. Zum Beispiel, wenn jemand in Schweden eine Abschluss gemacht hat, entspricht er der Regel mit dem Bildungsabschluss-Ereignis und "schw" als Ort. Die persönlichen Ereignisse sollten aus dem Menü ausgewählt werden. Die Regel liefert einen Treffer, nur wenn alle nicht-leeren Felder (teilweise) dem persönlichen Ereignis entsprechen. Lass die anderen Felder leer, wenn du nur einen Wert verwenden willst.

#### Personen mit Ereignis entsprechend dem <Ereignisfilter>

Entspricht Personen, die ein Ereignis besitzen, welches zu einem bestimmten Ereignisfilterergebnis passt.

#### Zeugen

Diese Regel sucht nach Personen, die sich in einer [Ereignisrolle](wiki:Gramps_Glossary#event_role) "Zeuge" befinden. Wenn die Ereignisart (persönlich oder familiär) angegeben ist, werden nur die Ereignisse dieser Art durchsucht.

##### Siehe auch

[FilterRegeln](wiki:Addon:Rule_expansions#FilterRules_:_Plugin_Manager_Rulebook_Collection) : Plugin Manager Rulebook Collection enthält Regeln für die Suche nach Personen oder Familien mit Ereignissen mit bestimmten Rollen:

- [Personen mit Ereignissen mit einer ausgewählten Rolle](wiki:Addon:Rule_expansions#People_with_events_with_a_selected_role) : Filterregel Personen
- [Familien mit Ereignissen mit einer ausgewählten Rolle](wiki:Addon:Rule_expansions#Families_with_Events_with_a_selected_role) : Filterregel Familie

### Familienkategorie

Diese Kategorie enthält die folgenden Regeln, die Familien aufgrund ihrer aufgezeichneten Ereignisse filtern:

#### Familien mit <Ereignis>

Diese Regel entspricht Familien, die ein Ereignis, entsprechend den angegebenen Werten für die Art, das Datum, den Ort und die Beschreibung des Ereignisses, haben. Diese Regel liefert auch dann einen Treffer, wenn das Ereignis der Familie nur teilweise mit den Werten übereinstimmt. Die Regel ignoriert Groß- und Kleinschreibung. Zum Beispiel, wenn eine Familie in Schweden geheiratet hat, entspricht sie der Regel mit dem Hochzeitsereignis und "schw" als Ort. Die Ereignisse sollten aus dem Menü ausgewählt werden. Die Regel liefert einen Treffer, nur wenn alle nicht-leeren Felder (teilweise) dem Ereignis entsprechen. Lass die anderen Felder leer, wenn du nur einen Wert verwenden willst.

## Familienfilter

Diese Kategorie umfasst die folgenden Regeln, die Personen auf Grund ihrer Familienbeziehungen filtern:

### Adoptierte Personen

Diese Regel entspricht Personen, die adoptiert wurden.

### Kinder von einem <Filter>Treffer

Diese Regel entspricht Personen, von denen wenigstens ein Elternteil dem angegebenen Filter entspricht. Der angegebene Filtername sollte aus dem Menü gewählt werden.

### Eltern eines <Filter>Treffers

Diese Regel entspricht Personen, dessen Kind dem angegebenen Filter entspricht. Der angegebene Filtername sollte aus dem Menü gewählt werden.

### Personen mit fehlenden Eltern

Passt zu Personen, die Kinder in einer Familie mit weniger als zwei Elternteilen sind oder die keine Kinder in einer Familie sind.

### Personen mit Kindern

Diese Regel entspricht Personen mit Kindern.

### Personen mit mehreren Ehen

Diese Regel entspricht Personen mit mehr als einem Partner(in).

### Personen ohne Ehen

Diese Regel entspricht Personen ohne Partner(in).

### Personen mit der <Beziehung>

Diese Regel entspricht Personen mit einer bestimmten Beziehung. Die Beziehung muss der aus dem Menü gewählten entsprechen. Zusätzlich kann auch die Anzahl der Beziehungen und die Anzahl der Kinder angegeben werden. Die Regel liefert einen Treffer, nur wenn alle nicht-leeren Felder (teilweise) der Beziehung der Person entsprechen. Lassen Sie die anderen Felder leer, wenn Sie nur einen Wert verwenden wollen.

### Geschwister eines <Filter>Treffers

Diese Regel entspricht Personen deren Geschwister auf den angegeben Filter passen. Der entsprechende Filter sollte aus dem Menü gewählt werden.

### Ist ein (Ehe-)Partner eines <Filter>Treffers

Diese Regel entspricht Personen, die mit jemand verheiratet sind, der/die dem angegebenen Filter entspricht. Der angegebene Filtername sollte aus dem Menü gewählt werden.

## Filter nach Vater

Diese Regelkategorie findet Familien mit Vätern, die der Regel entsprechen:

### Liefert Familien deren Vater den <Text> in der ID enthält

Entspricht Familien, deren Vater eine vorgegebene Gramps-ID hat.

### Familien mit Vater mit dem <Namen>

Entspricht Familien, deren Vater den vorgegebenen Namen oder Namensteil hat.

## Allgemeine Filter

Diese Filter sind Ansichten spezifisch

- [Personen- und Beziehungenkategorie](#Personen-_und_Beziehungenkategorie_3)
- [Familienkategorie](#Familienkategorie_3)
- [Ereignissekategorie](#Ereignissekategorie_2)
- [Ortekategorie](#Ortekategorie_2)
- [Quellenkategorie](#Quellenkategorie)
- [Fundstellenkategorie](#Fundstellenkategorie)
- [Aufbewahrungsortekategorie](#Aufbewahrungsortekategorie)
- [Medienkategoriekategorie](#Medienkategoriekategorie)
- [Notizenkategoriekategorie](#Notizenkategoriekategorie)

### Personen- und Beziehungenkategorie

Diese Kategorie enthält die folgenden allgemeinen Regeln:

#### Personen aus Lesezeichenliste

Entspricht allen Personen, die sich auf der Lesezeichenliste befinden.

<span id="Default person">

#### Hauptperson

</span> Entspricht der Hauptperson.

#### Einzeln stehende Personen

Entspricht Personen die keine Familiärebeziehung zu irgendeiner anderen Person in der Datenbank besitzen.

#### Jeden

Entspricht jedem in der Datenbank.

#### Frauen

Entspricht allen weiblichen Personen.

#### Männer

Entspricht allen männlichen Personen.

#### Personen mit <Anzahl> Notizen

Entspricht Personen mit einer bestimmten Anzahl von Notizen: Werte: Anzahl der Instanzen -- Anzahl muss größer als/kleiner als/gleich mit sein.

#### Personen, deren Notizen, den <Text> enthalten

Entspricht Personen deren Notizen Text enthalten.

#### Als vertraulich markierte Personen

Entspricht Personen deren Datensätze als vertraulich markiert sind.

#### Personen, die dem <Filter> entsprechen

Entspricht Personen, die auf den Filter mit dem Filternamen passen. Werte: Filtername. Der entsprechende Filtername sollte aus dem Menü gewählt werden.

#### Nicht als vertraulich markierte Personen

Findet Personen, die nicht als vertraulich gekennzeichnet sind

#### Personen, die wahrscheinlich leben

Entspricht Personen ohne Hinweise auf den Tod bis zu einem bestimmten Datum. Wenn der angegebene "Am-Datum"-Wert leer ist, wird mit "heute()" verglichen. Der Wert "wahrscheinlich lebend" berücksichtigt die in den Einstellungen festgelegten Datumsannäherungen und Lebensspannen.

Genauere Informationen zu dieser Berechnung findest du im Abschnitt "[Vermutlich lebend](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Vermutlich_lebend)".

- [Vermutlich lebend Filter](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Vermutlich_lebend#Vermutlich_lebend_Filter)

#### Personen mit <Anzahl> HLT Ereignissen

Entspricht Personen mit einer bestimmten Anzahl von HLT Ereignissen. Werte: Anzahl der Instanzen -- Anzahl muss größer als/kleiner als/gleich mit sein.

#### Personen mit <Anzahl> Adressen

Entspricht Personen mit einer bestimmten Anzahl von persönlichen Adressen. Werte: Anzahl der Instanzen -- Anzahl muss größer als/kleiner als/gleich mit sein.

#### Personen mit <Anzahl> Verbindungen

Entspricht Personen mit einer bestimmten Anzahl von Verbindungen. Werte: Anzahl der Instanzen -- Anzahl muss größer als/kleiner als/gleich mit sein.

#### Personen mit <Anzahl> Medien

Entspricht Personen mit einer bestimmten Anzahl von Elementen in der Galerie. Werte: Anzahl der Instanzen -- Anzahl muss größer als/kleiner als/gleich mit sein.

#### Personen, deren ID den <Text> enthält

Entspricht Personen, deren Gramps ID dem 'regulären Ausdruck' entspricht

#### Personen mit einem Namen, der <Text> entspricht

Findet Namen von Personen, die eine Teilzeichenkette enthalten oder einem [regulären Ausdruck](wiki:De:Gramps_Glossar#regex) entsprechen

#### Personen mit einem Spitznamen

Entspricht Personen mit einem Spitznamen

#### Personen mit alternativen Namen

Entspricht Personen mit alternativen Namen

#### Personen mit unvollständigem Namen

Entspricht allen Personen denen entweder der Vor- oder Familienname fehlt.

#### Personen, deren Aufzeichnungen die <Zeichenfolge> enthalten

Entspricht Personen deren Datensatz die angegebene Zeichenkette enthält. Werte: Teilzeichenkette

*Der Filter sucht nicht in Notizen.*

#### Personen mit der <Namensart>

Entspricht Personen mit einem Namenstyp

#### Personen mit der <Nachnamensherkunftsart>

Entspricht Personen mit einer Nachnamenherkunft

#### Personen mit dem <Namen>

Passt auf Personen mit einem bestimmten (Teil-)Namen

Werte:

- Vornamen
- Vollständiger Familienname : sucht Präfix, Nachname und Verbindungen mit mehreren Nachnamen
- Titel
- Suffix
- Rufname
- Spitzname
- Präfix
- Einzelner Nachname : sucht nur den [Bevorzugten Namen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Daten_eingeben_und_bearbeiten:_Ausführlich_-_Teil_1#Bevorzugter_Name_Bereich)
- Verbinder : Suche in Konnektoren für [Mehrere Nachnamen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Daten_eingeben_und_bearbeiten:_Ausführlich_-_Teil_1#Mehrere_Nachnamen)
- Patronymisch
- Familienspitzname

Optionen:

- \- wähle diese Option und gib die regulären Ausdrücke in eines der Eingabefelder ein.

  - Wenn du zum Beispiel den regulären Ausdruck `(.|\s)*\S(.|\s)*` in das Feld eingibst und diese Option auswählst, kannst du nicht leere Präfixe finden.

- 

{{-}}

##### Siehe auch

- [Personen mit einem Namen, der &lt;Text&gt; entspricht](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Filter#Personen_mit_einem_Namen.2C_der_.3CText.3E_entspricht)
- [Personen mit einem Spitznamen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Filter#Personen_mit_einem_Spitznamen)
- [Personen mit alternativen Namen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Filter#Personen_mit_alternativen_Namen)
- [Personen mit unvollständigem Namen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Filter#Personen_mit_unvollst.C3.A4ndigem_Namen)
- [Personen mit der &lt;Namensart&gt;](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Filter#Personen_mit_der_.3CNamensart.3E)
- [Personen mit der &lt;Nachnamensherkunftsart&gt;](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Filter#Personen_mit_der_.3CNachnamensherkunftsart.3E)
- [Personen mit dem &lt;Namen&gt;](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Filter#Personen_mit_dem_.3CNamen.3E)
- [Soundex passt auf Personen mit dem &lt;Namen&gt;](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Filter#Soundex_passt_auf_Personen_mit_dem_.3CNamen.3E)
- [Familien mit Kind mit dem &lt;Namen&gt;](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Filter#Familien_mit_Kind_mit_dem_.3CNamen.3E)
- [Familien mit Vater mit dem &lt;Namen&gt;](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Filter#Familien_mit_Vater_mit_dem_.3CNamen.3E)
- [Familien mit Mutter mit dem &lt;Namen&gt;](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Filter#Familien_mit_Mutter_mit_dem_.3CNamen.3E)
- [Suchleiste](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Hauptfenster#Suchleiste) (Namen enthält, Name enthält nicht)
- [Personenfilter](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Gramplets#Personenfilter) Gramplet (Name)
- Isotammi [Personenfilter+](wiki:Addon:Isotammi_addons#Filter.2B) Zusatzmodulgramplet (Name)
- Isotammi [SuperTool](wiki:Addon:Isotammi_addons#SuperTool) Abfragewerkzeug (Kategorie Personen)

{{-}}

#### Personen mit dem <Etikett>

Entspricht Personen mit einem Etikett mit dem entsprechenden Wert. Werte: Etikett.

#### Personen mit dem familiären <Attribut>

Entspricht Personen mit dem Familien Attribut mit einem bestimmten Wert. Verwende reguläre Ausdrücke für den Mustervergleich, um nach [allen Werten](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Filter#regex_all) oder Attributen zu suchen, die [leer gelassen wurden](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Filter#regex_null). Werte: Familien-Attribut: Identifikationsnummer -- Alter ...

#### Personen mit dem persönlichen <Attribut>

Entspricht Personen mit dem persönlichen Attribut mit einem bestimmten Wert. Verwende reguläre Ausdrücke für den Mustervergleich, um nach [allen Werten](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Filter#regex_all) oder Attributen zu suchen, die [leer gelassen wurden](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Filter#regex_null). Werte: Personen-Attribut: Identifikationsnummer -- Alter ...

#### Personen mit unbekanntem Geschlecht

Entspricht allen Personen mit unbekanntem Geschlecht.

#### Personen ohne bekanntes Geburtsdatum

Dieser allgemeine Filter in der Kategorie Personen passt zu Personen ohne bekanntes Geburtsdatum.

Diese Regel gilt sowohl für Personen ohne geburtsartiges Ereignis als auch für Personen mit undatierten geburtsartigen Ereignissen.

#### Personen ohne bekanntes Todesdatum

Entspricht Personen ohne bekanntes Todesdatum

#### Person mit <ID>

Entspricht Personen mit Gramps ID. Die Regel liefert nur dann einen Treffer, wenn die ID exakt übereinstimmt. Du kannst entweder die ID in ein Texteingabefeld eingeben oder ein Objekt aus der Liste auswählen, indem du auf die Schaltfläche klickst. Im letzteren Fall erscheint die ID im Textfeld, nachdem die Auswahl getroffen wurde.

#### Personen geändert nach <Datum Zeit>

Entspricht Personendatensätzen, die während eines bestimmten Zeitraums geändert wurden. Wird verwendet, um Datensätze zu identifizieren, die während bestimmter Arbeitssitzungen importiert oder geändert wurden.

Filterung auf der Grundlage des angegebenen Datums und Zeitstempels nach einem bestimmten Zeitstempel im Format `JJJJ-MM-TT HH:MM:SS`. Diese Filterregeln suchen nach Datensätzen, die innerhalb eines Datumsbereichs geändert wurden, wenn eine zweite Datumszeit angegeben wird.

Werte:

` Geändert nach: `  
` aber vor: `

Werte müssen nach dem 1. Januar 1970 (UTC) liegen. Zukünftige Daten bis `3001-01-01 01:59:59` sind gültig.

Die Filterregeln sind im Abschnitt für benutzerdefinierte Regeln in den Ansichten Personen, Beziehungen, Schaubilder und Geografie verfügbar.

Entsprechende Regeln gibt es für Datensätze des entsprechenden Kategorietyps in den Kategorieansichten Personen, Familien, Ereignisse, Orte, Quellen, Zitate, Aufbewahrungsorte, Medien und Notizen.

#### Soundex passt auf Personen mit dem <Namen>

Soundex-Abgleich von Personen mit einem bestimmten Namen. Vornamen, Nachnamen, Rufnamen und Spitznamen werden in Haupt- und Alternativnamen gesucht.

Diese Regel vergleicht die Namen von Personen mit einem phonetischen Muster. Sie verwendet den phonetischen [Soundex](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Gramplets#SoundEx_was_ist_das.3F)-Algorithmus zur Indizierung von Namen nach Lauten, wie sie im Englischen ausgesprochen werden.

Das Übereinstimmungskriterium kann ein Soundex-Code sein (der mit dem Soundex Gramplet gefunden werden kann), der aus einem Buchstaben gefolgt von drei numerischen Ziffern besteht: Der Buchstabe ist der erste Buchstabe des Namens, und die Ziffern kodieren die restlichen Konsonanten. Wenn das Übereinstimmungskriterium jedoch kein gültiger Soundex-Code ist, erzeugt der Filter einfach einen Soundex-Code für das eingegebene Wort.

Alle Namensfelder (und die einzelnen Wörter innerhalb dieser Felder) werden einzeln mit dem Soundex-Code abgeglichen.

### Familienkategorie

Diese Kategorie enthält die folgenden allgemeinen Regeln:

#### Vorfahrenfamilien von <Familie>

Entspricht Familien, die Vorfahren der Partner in einer bestimmten Familie sind. Es besteht die Möglichkeit, die angegebene Familie in die Ergebnisse einzuschließen. Einschließlich gemischter Familien und Familien, die nicht durch Geburt entstanden sind.

#### Familien aus Lesezeichenliste

Entspricht allen Familien, die sich auf der Lesezeichenliste befinden.

#### Nachkommenfamilien von <Familie>

Entspricht dem Familienobjekt, das von einer bestimmten Familie abstammt. (Es werden keine Personenobjekte einbezogen.)

Siehe auch:

- Nachkommendes Familienmitglied von <Filter> Übereinstimmung
- Nachkommendes Familienmitglied von <Person>

#### Jede Familie

Entspricht jeder Familie in der Datenbank.

#### Familien geändert nach <Datum Zeit>

Entspricht Familiendatensätzen, die nach einer bestimmten Zeitpunkt geändert wurden (JJJJ-MM-TT HH:MM:SS) oder in einem bestimmten Zeitfenster, wenn ein zweiter Zeitpunkt angegeben wird: Werte: Geändert nach: -- aber vor:.

#### Familien mit <Anzahl> Notizen

Entspricht Familien mit einer bestimmten Anzahl von Notizen: Werte: Anzahl der Instanzen -- Anzahl muss größer als/kleiner als/gleich mit sein.

#### Familien, deren Notizen, den <Text> enthalten

Entspricht Familien deren Notizen Text enthalten.

#### Als vertraulich markierte Familien

Entspricht Familien deren Datensätze als vertraulich markiert sind.

#### Familien die dem <Filter> entsprechen

Entspricht Familien, die auf den Filter mit dem Filternamen passen. Werte: Filtername. Der entsprechende Filtername sollte aus dem Menü gewählt werden.

#### Familien mit <Anzahl> HLT Ereignisse

Entspricht Familien mit einer bestimmten Anzahl von HLT Ereignissen. Werte: Anzahl der Instanzen -- Anzahl muss größer als/kleiner als/gleich mit sein.

#### Familien mit <Anzahl> Medien

Entspricht Familien mit einer bestimmten Anzahl von Elementen in der Galerie. Werte: Anzahl der Instanzen -- Anzahl muss größer als/kleiner als/gleich mit sein.

#### Familien mit ID, die den <Text> enthält

Entspricht Familien, deren Gramps ID dem 'regulären Ausdruck' entspricht

#### Familien mit einer Referenzenanzahl von <Anzahl>

Entspricht Familien mit einer bestimmten Anzahl von Referenzen. Werte: Anzahl der Instanzen -- Anzahl muss größer als/kleiner als/gleich mit sein.

#### Familien mit dem <Etikett>

Entspricht Familien mit einem Etikett mit dem entsprechenden Wert. Werte: Etikett.

#### Familien mit dem <Attribut>

Entspricht Familien mit dem Attribut mit einem bestimmten Wert. Werte: Familien Attribute: Identifikationsnummer -- Alter ...

#### Familien mit der Beziehungsart

Diese Regel entspricht Familien mit einer bestimmten Beziehungsart. Die Beziehungsart muss der aus dem Menü gewählten entsprechen.

#### Familien mit <ID>

Entspricht Familien mit Gramps ID. Die Regel liefert nur Treffer, wenn die ID genau übereinstimmt. Du kannst entweder die ID in ein Texteingabefeld eingeben oder ein Objekt durch klicken auf die Schaltfläche auswählen. Im letzteren Fall erscheint die ID im Textfeld, nachdem die Auswahl getroffen wurde.

### Ereignissekategorie

Diese Kategorie enthält die folgenden allgemeinen Regeln:

#### Ereignis mit <ID>

Entspricht Ereignissen mit Gramps ID. Die Regel liefert nur Treffer, wenn die ID genau übereinstimmt. Du kannst entweder die ID in ein Texteingabefeld eingeben oder ein Objekt durch klicken auf die Schaltfläche auswählen. Im letzteren Fall erscheint die ID im Textfeld, nachdem die Auswahl getroffen wurde.

#### Ereignisse geändert nach <Datum Zeit>

Entspricht Ereignissen, die nach einer bestimmten Zeitpunkt geändert wurden (JJJJ-MM-TT HH:MM:SS) oder in einem bestimmten Zeitfenster, wenn ein zweiter Zeitpunkt angegeben wird: Werte: Geändert nach: -- aber vor:.

#### Ereignisse mit <Anzahl> Notizen

Entspricht Ereignissen mit einer bestimmten Anzahl von Notizen: Werte: Anzahl der Instanzen -- Anzahl muss größer als/kleiner als/gleich mit sein.

#### Ereignisse, deren Notizen, den <Text> enthalten

Entspricht Ereignisse deren Notizen Text enthalten.

#### Als vertraulich markierte Ereignisse

Entspricht Ereignissen die als vertraulich markiert sind.

#### Ereignisse entsprechend <Filter>

Entspricht Ereignissen, die auf den Filter mit dem Filternamen passen. Werte: Filtername. Der entsprechende Filtername sollte aus dem Menü gewählt werden.

#### Ereignisse an einem bestimmten Wochentag stattfanden

Passt auf Ereignisse, die an einem bestimmten Wochentag stattfanden

#### Ereignisse von Personen, die dem <Personenfilter> entsprechen

Passt auf Ereignisse von Personen, die dem gegebenen Personenfilter entsprechen.

#### Ereignisse mit Orten, die dem <Ortsfilter> entsprechen

Passt auf Ereignisse die an Orten stattfanden, die einem bestimmten Ortsfilter entsprechen.

#### Ereignisse mit <Anzahl> Medien

Entspricht Ereignissen mit einer bestimmten Anzahl von Elementen in der Galerie. Werte: Anzahl der Instanzen -- Anzahl muss größer als/kleiner als/gleich mit sein.

#### Ereignisse mit \<Daten\>

Passt auf Ereignisse mit Daten mit einem bestimmten Wert

#### Ereignisse, deren ID den <Text> enthält

Entspricht Ereignissen, deren Gramps ID dem 'regulären Ausdruck' entspricht

#### Ereignisse mit einer Referenzenanzahl von <Anzahl>

Entspricht Ereignissen mit einer bestimmten Anzahl von Referenzen. Werte: Anzahl der Instanzen -- Anzahl muss größer als/kleiner als/gleich mit sein.

#### Ereignisse mit dem <Etikett>

Entspricht Ereignissen mit einem Etikett mit dem entsprechenden Wert. Werte: Etikett.

#### Ereignisse mit dem Attribut <Attribut>

Entspricht Ereignissen mit dem Attribut mit einem bestimmten Wert. Werte: Familien Attribute: Identifikationsnummer -- Alter ...

#### Ereignisse der gegebenen Art

Liefert Ereignisse der gegebenen Art

#### Jedes Ereignis

Entspricht jedem Ereignis in der Datenbank.

### Ortekategorie

Diese Kategorie enthält die folgenden allgemeinen Regeln:

#### Jeder Ort

Entspricht jedem Ort in der Datenbank.

#### Orte mit <ID>

Entspricht Orten mit Gramps ID. Die Regel liefert nur Treffer, wenn die ID genau übereinstimmt. Du kannst entweder die ID in ein Texteingabefeld eingeben oder ein Objekt durch klicken auf die Schaltfläche auswählen. Im letzteren Fall erscheint die ID im Textfeld, nachdem die Auswahl getroffen wurde.

#### Orte geändert nach <Datum Zeit>

Entspricht Orten, die nach einer bestimmten Zeitpunkt geändert wurden (JJJJ-MM-TT HH:MM:SS) oder in einem bestimmten Zeitfenster, wenn ein zweiter Zeitpunkt angegeben wird: Werte: Geändert nach: -- aber vor:.

#### Orte die in anderen Orten enthalten sind

Entspricht Orten unterhalb der hierarchischen Struktur eines angegebenen Ortes. Schließt den Umschließenden Ort nicht ein und ignoriert Datumsangaben.

#### Orte mit <Anzahl> Notizen

Entspricht Orten mit einer bestimmten Anzahl von Notizen: Werte: Anzahl der Instanzen -- Anzahl muss größer als/kleiner als/gleich mit sein.

#### Orte, deren Notizen, den <Text> enthalten

Entspricht Orte deren Notizen Text enthalten.

#### Als vertraulich markierte Orte

Entspricht Orten die als vertraulich markiert sind.

#### Orte mit Titel

Liefert Orte mit einem bestimmten Titel

#### Orte mit gegebenen Parametern

Allgemeine Filterregel, die Orte mit bestimmten Parametern findet:

- 

- 

- 

Bietet auch die Option an.

#### Orte entsprechend <Filter>

Entspricht Orten, die auf den Filter mit dem Filternamen passen. Werte: Filtername. Der entsprechende Filtername sollte aus dem Menü gewählt werden.

#### Orte von Ereignissen entsprechend dem <Ereignisfilter>

Entspricht Orten, wo Ereignisse stattfanden, die auf den angegebenen Ereignisfilter passen.

#### Orte mit <Anzahl> Medien

Entspricht Orten mit einer bestimmten Anzahl von Elementen in der Galerie. Werte: Anzahl der Instanzen -- Anzahl muss größer als/kleiner als/gleich mit sein.

#### Orte, deren ID den <Text> enthält

Entspricht Orten, deren Gramps ID dem 'regulären Ausdruck' entspricht

#### Orte mit gegebener Anzahl Referenzen von <Anzahl>

Entspricht Orten mit einer bestimmten Anzahl von Referenzen. Werte: Anzahl der Instanzen -- Anzahl muss größer als/kleiner als/gleich mit sein.

#### Orte mit dem <Etikett>

Entspricht Orten mit einem Etikett mit dem entsprechenden Wert. Werte: Etikett.

### Quellenkategorie

Diese Kategorie enthält die folgenden allgemeinen Regeln:

#### Jede Quelle

Entspricht jeder Quelle in der Datenbank.

#### Quellen mit <ID>

Entspricht Quellen mit Gramps ID. Die Regel liefert nur Treffer, wenn die ID genau übereinstimmt. Du kannst entweder die ID in ein Texteingabefeld eingeben oder ein Objekt durch klicken auf die Schaltfläche auswählen. Im letzteren Fall erscheint die ID im Textfeld, nachdem die Auswahl getroffen wurde.

#### Quellen geändert nach <Datum Zeit>

Entspricht Quellen, die nach einer bestimmten Zeitpunkt geändert wurden (JJJJ-MM-TT HH:MM:SS) oder in einem bestimmten Zeitfenster, wenn ein zweiter Zeitpunkt angegeben wird: Werte: Geändert nach: -- aber vor:.

#### Quellen mit <Anzahl> Notizen

Entspricht Quellen mit einer bestimmten Anzahl von Notizen: Werte: Anzahl der Instanzen -- Anzahl muss größer als/kleiner als/gleich mit sein.

#### Quellen, deren Notizen, den <Text> enthalten

Entspricht Quellen deren Notizen Text enthalten.

#### Als vertraulich markierte Quellen

Entspricht Quellen die als vertraulich markiert sind.

#### Quellen entsprechend <Filter>

Entspricht Quellen, die auf den Filter mit dem Filternamen passen. Werte: Filtername. Der entsprechende Filtername sollte aus dem Menü gewählt werden.

#### Quellen mit <Anzahl> Aufbewahrungsorte Referenzen

Entspricht Quellen mit einer bestimmten Anzahl von Aufbewahrungsorterefrenzen. Werte: Anzahl der Instanzen -- Anzahl muss größer als/kleiner als/gleich mit sein.

#### Quellen mit <Anzahl> Medien

Entspricht Quellen mit einer bestimmten Anzahl von Elementen in der Galerie. Werte: Anzahl der Instanzen -- Anzahl muss größer als/kleiner als/gleich mit sein.

#### Quellen, deren ID den <Text> enthält

Entspricht Quellen, deren Gramps ID dem 'regulären Ausdruck' entspricht

#### Quellen mit einer Anzahl von Referenzen von <Anzahl>

Entspricht Quellen mit einer bestimmten Anzahl von Referenzen. Werte: Anzahl der Instanzen -- Anzahl muss größer als/kleiner als/gleich mit sein.

#### Quellen, deren Aufbewahrungsortereferenz den <Text> in der "Signatur" enthalten

Entspricht Quellen, deren Aufbewahrungsortereferenz eine Zeichenfolge in der 'Signatur' enthält.

#### Quellen mit Aufbewahrungsortreferenzen, die dem <Aufbewahrungsortfilter> entsprechen

Entspricht Quellen mit einer Aufbewahrungsortereferenz, die einem bestimmten Aufbewahrungsortfilter entspricht.

#### Quellen mit dem <Etikett>

Entspricht Quellen mit einem Etikett mit dem entsprechenden Wert. Werte: Etikett.

#### Quellentitel enthält <Text>

Entspricht Quellen, deren Titel eine bestimmte Zeichenfolge enthält.

### Fundstellenkategorie

Diese Kategorie enthält die folgenden allgemeinen Regeln:

#### Fundstelle mit <ID>

Entspricht Fundstellen mit Gramps ID. Die Regel liefert nur Treffer, wenn die ID genau übereinstimmt. Du kannst entweder die ID in ein Texteingabefeld eingeben oder ein Objekt durch klicken auf die Schaltfläche auswählen. Im letzteren Fall erscheint die ID im Textfeld, nachdem die Auswahl getroffen wurde.

#### Fundstellen geändert nach <Datum Zeit>

Entspricht Fundstellen, die nach einer bestimmten Zeitpunkt geändert wurden (JJJJ-MM-TT HH:MM:SS) oder in einem bestimmten Zeitfenster, wenn ein zweiter Zeitpunkt angegeben wird: Werte: Geändert nach: -- aber vor:.

#### Fundstellen mit <Anzahl> Notizen

Entspricht Fundstellen mit einer bestimmten Anzahl von Notizen: Werte: Anzahl der Instanzen -- Anzahl muss größer als/kleiner als/gleich mit sein.

#### Fundstellen, deren Notizen, den <Text> enthalten

Entspricht Fundstellen deren Notizen Text enthalten.

#### Als vertraulich markierte Fundstellen

Entspricht Fundstellen die als vertraulich markiert sind.

#### Fundstellen entsprechend Parametern

Allgemeine Filterregel, die Fundstellen mit bestimmten Parametern findet:

- 

- 

- 

Bietet auch die Option an.

#### Fundstellen entsprechend <Filter>

Liefert Fundstellen, die dem angegebenen Filter entsprechen

#### Fundstellen mit <Anzahl> Medien

Entspricht Fundstellen mit einer bestimmten Anzahl von Elementen in der Galerie. Werte: Anzahl der Instanzen -- Anzahl muss größer als/kleiner als/gleich mit sein.

#### Fundstellen, deren ID den <Text> enthalten

Entspricht Fundstellen, deren Gramps ID dem 'regulären Ausdruck' entspricht

#### Fundstelle Band/Seite enthält <Text>

Liefert Fundstellen, deren Band/Seite eine bestimmte Zeichenfolge enthalten.

#### Fundstellen mit einer Anzahl von Referenzen von <Anzahl>

Entspricht Fundstellen mit einer bestimmten Anzahl von Referenzen. Werte: Anzahl der Instanzen -- Anzahl muss größer als/kleiner als/gleich mit sein.

#### Fundstellen mit Quellen mit einer Aufbewahrungsortreferenz, die dem <Aufbewahrungsortfilter> entsprechen

Passt auf Fundstellen mit Quellen mit einer Aufbewahrungsortreferenz, die einem bestimmten Aufbewahrungsortfilter entspricht.

#### Fundstellen mit Quellen, die dem <Quellenfilter> entsprechen

Entspricht Fundstellen mit Quellen, die dem vorgegebenen Quellenfilternamen entsprechen.

#### Fundstellen mit dem <Etikett>

Entspricht Fundstellen mit einem Etikett mit dem entsprechenden Wert. Werte: Etikett.

#### Jede Fundstellen

Entspricht jeder Fundstelle in der Datenbank.

### Aufbewahrungsortekategorie

Diese Kategorie enthält die folgenden allgemeinen Regeln:

#### Jeder Aufbewahrungsort

Entspricht jedem Aufbewahrungsort in der Datenbank.

#### Aufbewahrungsorte geändert nach <Datum Zeit>

Entspricht Aufbewahrungsorten, die nach einer bestimmten Zeitpunkt geändert wurden (JJJJ-MM-TT HH:MM:SS) oder in einem bestimmten Zeitfenster, wenn ein zweiter Zeitpunkt angegeben wird: Werte: Geändert nach: -- aber vor:.

#### Aufbewahrungsorte, deren Notizen, den <Text> enthalten

Entspricht Aufbewahrungsorten deren Notizen Text enthalten.

#### Als vertraulich markierte Aufbewahrungsorte

Entspricht Aufbewahrungsorten die als vertraulich markiert sind.

#### Aufbewahrungsorte entsprechend Parametern

Allgemeine Filterregel, die mit Aufbewahrungsorten mit bestimmten Parametern übereinstimmt:

- 

- 

-   
  durchsucht alle Textfelder in allen Postadressen

-   
  durchsucht alle Textfelder in allen URLs (siehe Fehler )

Bietet auch die Option an.

#### Aufbewahrungsorte entsprechend <Filter>

Entspricht Aufbewahrungsorten, die dem vorgegebenen Filter entsprechen.

#### Aufbewahrungsorte, deren ID den <Text> enthält

Entspricht Aufbewahrungsorten, deren Gramps ID dem 'regulären Ausdruck' entspricht

#### Aufbewahrungsorte mit einer Anzahl von Referenzen von <Anzahl>

Entspricht Aufbewahrungsorten mit einer bestimmten Anzahl von Referenzen. Werte: Anzahl der Instanzen -- Anzahl muss größer als/kleiner als/gleich mit sein.

#### Aufbewahrungsortname enthält <Text>

Entspricht Aufbewahrungsorten, deren Name eine bestimmte Zeichenfolge enthält.

#### Aufbewahrungsorte mit dem <Etikett>

Entspricht Aufbewahrungsorten mit einem Etikett mit dem entsprechenden Wert. Werte: Etikett.

#### Aufbewahrungsort mit <ID>

Entspricht Aufbewahrungsorten mit Gramps ID. Die Regel liefert nur Treffer, wenn die ID genau übereinstimmt. Du kannst entweder die ID in ein Texteingabefeld eingeben oder ein Objekt durch klicken auf die Schaltfläche auswählen. Im letzteren Fall erscheint die ID im Textfeld, nachdem die Auswahl getroffen wurde.

### Medienkategorie

Diese Kategorie enthält die folgenden allgemeinen Regeln:

#### Jedes Medienobjekt

Entspricht jedem Medienobjekt in der Datenbank.

#### Medienobjekte mit <ID>

Entspricht Medienobjekte mit Gramps ID. Die Regel liefert nur Treffer, wenn die ID genau übereinstimmt. Du kannst entweder die ID in ein Texteingabefeld eingeben oder ein Objekt durch klicken auf die Schaltfläche auswählen. Im letzteren Fall erscheint die ID im Textfeld, nachdem die Auswahl getroffen wurde.

#### Medienobjekte geändert nach <Datum Zeit>

Entspricht Medienobjekten, die nach einer bestimmten Zeitpunkt geändert wurden (JJJJ-MM-TT HH:MM:SS) oder in einem bestimmten Zeitfenster, wenn ein zweiter Zeitpunkt angegeben wird: Werte: Geändert nach: -- aber vor:.

#### Medienobjekte, deren Notizen, den <Text> enthalten

Entspricht Medienobjekten deren Notizen Text enthalten.

#### Als vertraulich markierte Medienobjekte

Entspricht Medienobjekten die als vertraulich markiert sind.

#### Medienobjekte, die den Parametern entsprechen

Allgemeine Filterregel, die auf Medienobjekte mit bestimmten Parametern passt:

- 

- 

Bietet auch die Option an.

#### Medienobjekte entsprechend <Filter>

Liefert Medienobjekte, die dem gegebenen Filter entsprechen

#### Medienobjekte, deren ID den <Text> enthält

Entspricht Medienobjekten, deren Gramps ID dem 'regulären Ausdruck' entspricht

#### Medienobjekte mit einer Anzahl von Referenzen von <Anzahl>

Entspricht Medienobjekte mit einer bestimmten Anzahl von Referenzen. Werte: Anzahl der Instanzen -- Anzahl muss größer als/kleiner als/gleich mit sein.

#### Medienobjekt mit dem <Etikett>

Entspricht Medienobjekten mit einem Etikett mit dem entsprechenden Wert. Werte: Etikett.

#### Medienobjekte mit dem Attribut <Attribut>

Liefert Medienobjekte mit dem Attribut mit einem bestimmten Wert

### Notizenkategorie

Diese Kategorie enthält die folgenden allgemeinen Regeln:

#### Jede Notiz

Entspricht jeder Notiz in der Datenbank.

#### Notizen mit <ID>

Entspricht Notizen mit Gramps ID. Die Regel liefert nur Treffer, wenn die ID genau übereinstimmt. Du kannst entweder die ID in ein Texteingabefeld eingeben oder ein Objekt durch klicken auf die Schaltfläche auswählen. Im letzteren Fall erscheint die ID im Textfeld, nachdem die Auswahl getroffen wurde.

#### Notizen geändert nach <Datum Zeit>

Entspricht Notizen, die nach einer bestimmten Zeitpunkt geändert wurden (JJJJ-MM-TT HH:MM:SS) oder in einem bestimmten Zeitfenster, wenn ein zweiter Zeitpunkt angegeben wird: Werte: Geändert nach: -- aber vor:.

#### Notizen die den <Text> enthalten

Entspricht Notizen die den Text enthalten.

#### Als vertraulich markierte Notizen

Entspricht Notizen die als vertraulich markiert sind.

#### Notizen mit entsprechenden Parametern

Passt auf Notizen mit bestimmten Parametern

- 

- 

Bietet auch die Option an.

#### Notizen entsprechend <Filter>

Passt auf Notizen, die dem gegebenen Filter entsprechen

#### Notizen, deren ID den <Text> enthält

Entspricht Notizen, deren Gramps ID dem 'regulären Ausdruck' entspricht

#### Notizen mit einer Anzahl von Referenzen von <Anzahl>

Entspricht Notizen mit einer bestimmten Anzahl von Referenzen. Werte: Anzahl der Instanzen -- Anzahl muss größer als/kleiner als/gleich mit sein.

#### Notizen mit dem <Etikett>

Entspricht Notizen mit einem Etikett mit dem entsprechenden Wert. Werte: Etikett.

#### Notizen der gegebenen Art

Liefert Notizen der gegebenen Art

## Filter nach Mutter

Diese Regelkategorie findet Familien mit Müttern, die der Regel entsprechen:

### Liefert Familien mit Mutter deren ID den <Text> enthält

Entspricht Familien, deren Mutter eine vorgegebene Gramps-ID hat.

### Familien mit Mutter mit dem <Namen>

Entspricht Familien, deren Mutter einen bestimmten Namen oder Namensteil enthält

## Positionsfilter

Diese Regelkategorie findet Orte anhand der Nähe ihrer Global Positioning System-Koordinaten (GPS):

### Orte in der Umgebung der gegebenen Position

Entspricht Orten mit Breiten- oder Längengrad, positioniert in einem Rechteck von gegebener Höhe und Breite (in Grad) und als Mittelpunkt den gegebenen Längen- und Breitengrad.

### Orte ohne angegeben Längen- oder Breitengrad

Entspricht Orten mit leeren Längen- oder Breitengrad.

### Orte innerhalb eines Gebiets

Entspricht Orten innerhalb einer bestimmten Entfernung von einem bestimmten Ort.

Nach der Auswahl eines Ortes (der einen gültigen Koordinatensatz haben muss) wird jeder Ort gesucht, dessen Koordinaten innerhalb eines Kreises auf dem Globus (einer Ellipse auf einer flachen Karte) liegen, der auf diesen Koordinaten mit einem bestimmten Radius zentriert ist.

Die Entfernungseinheiten können ausgewählt werden: Kilometer (lineares Maß), Grad (Winkelmaß) und Meilen (lineares Maß).

## Quellenfilter

Diese Regelkategorie findet Fundstellen, die der Regel entsprechen:

### Fundstelle mit Quellen <ID>

Liefert Fundstellen mit einer Quelle mit einer bestimmten Gramps-ID. Werte: Quellen ID:

### Fundstellen, deren Quellen Notizen den <Text> enthalten

Liefert Fundstellen, deren Quellennotizen einen Text entsprechend eines regulären Ausdrucks enthalten.

### Fundstellen mit einer Quelle deren ID den <Text> enthält

Liefert Fundstellen, deren Quelle eine Gramps-ID haben, die dem regulären Ausdruck entspricht.

### Quellen entsprechend Parameter

Allgemeine Filterregel, die Quellen mit einer Quelle mit einem bestimmten Wert abgleicht:

- 

- 

- 

- 

Bietet auch die Option an.

## Verwandtschaftsfilter

Diese Kategorie umfasst die folgenden Regeln, die Personen nach ihrer gegenseitigen Verwandtschaft entsprechen:

### Personen verwandt mit <Person>

Entspricht Personen, die mit einer festgelegten Person verwandt sind

### Verwandschaftspfad zwischen <Person> und Personen entsprechend <Filter>

Startet die Datenbanksuchen bei einer bestimmten Person und liefert jede Person, die zwischen dieser und einer Reihe von Zielpersonen steht, die in einem Filter festgelegt sind. Dies erzeugt Reihen von Beziehungspfaden zwischen der festgelegten Person und den Zielpersonen. Da auch die Angeheirateten herangezogen werden, sind die einzelnen Pfade nicht unbedingt die kürzesten. ;-)

### Verwandtschaftspfad zwischen <Personen>

Diese Regel entspricht allen Vorfahren beider Personen zurück bis zu ihrem gemeinsamen Vorfahren (falls er existiert). Dies liefert den "Verwandtschaftspfad" zwischen diesen zwei Personen durch ihre gemeinsamen Vorfahren. Du kannst entweder die ID's beider Personen in die entsprechenden Textfelder eingeben oder Personen aus der Liste auswählen durch dein Klicken der Schaltfläche. Im zweiten Fall erscheint die ID danach im Textfeld.

### Verwandschaftspfad zwischen Personen aus dem Lesezeichen

Entspricht den Vorfahren zweier Personen aus den Lesezeichen, zurückgehend bis zu einem gemeinsamen Vorfahren, so dass man den Verwandtschaftspfad zwischen zwei Personen erhält.

## Etikettierung

![[_media/gramps-tag.png]]Ein [Etikett](wiki:De:Gramps_Glossar#Etikett) ist ein benutzerdefiniertes und farbcodiertes Kennzeichen, das mit dem Dialogfeld erstellt und an ausgewählte [Fundstelle](#Fundstellen), [Ereignisse](#Ereigniss), [Familien](#Familie), [Medien](#Medium), [Notizen](#Notiz), [Personen](#Person), [Orte](#Ort), [Aufbewahrungsorte](#Aufbewahrungsort) oder [Quellenobjekte](#Quelle) angehängt werden kann, um eine einfache Identifizierung und Filterung zu ermöglichen.

Ein benutzerdefiniertes Schlüsselwort oder eine Phrase kann verwendet werden, um die Sammlung zu gruppieren und einen Bericht zu erstellen. Mehrere Etiketten können verwendet werden, um Objekte zu beschriften und in mehrere Gruppen zu kategorisieren, wenn eine Filterung nach anderen Attributen nicht möglich ist.

Wenn du zum Beispiel einen großen Familienstammbaum hast, möchtest du vielleicht Teilmengen des Stammbaums erstellen, und diese Teilmengen können sich überschneiden. Zum Beispiel die Teilmengen der Familie deines Vaters und der Familie deiner Mutter, eine Teilmenge deiner Familie, die nach Australien ausgewandert ist. Die Idee wäre, jeder Untergruppe ein anderes Etikett zuzuweisen: „Väterlicherseits“, „Mütterlicherseits“, „Australien“ und „Zu erledigen“, um jede Gruppe zu identifizieren.

Technisch: Denjenigen von euch, die die E-Mail-Programme Gmail oder Thunderbird verwenden, wird die [Etikettierungsfunktion](wiki:De:Gramps_Glossar#tag) ziemlich vertraut vorkommen. Anstatt E-Mails in Ordnern wie in Outlook (Windows) oder Evolution (Linux) zu klassifizieren, werden E-Mails durch die Zuweisung von Etiketten klassifiziert. Anstelle einer disjunkten N:1-Klassifizierung (eine E-Mail kann sich nur in einem einzigen Ordner befinden, und ein Ordner kann viele E-Mails enthalten), gibt es in Gmail oder Thunderbird eine N:M-Klassifizierung (eine E-Mail kann mehrere Etiketten haben, und ein Etikett kann auf mehrere E-Mails angewendet werden) {{-}}

### Etikett-Menü

![[_media/Menu-Edit-Tag-Options-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Etikett-Aktionen aus dem Menü Bearbeiten]]

Im Menü kannst du aus den folgenden Optionen wählen:

- Dialogfeld

- Fenster

- Eine Liste zuvor erstellter Etiketten, die du für die folgende Aktion auswählen kannst:
  - 

  - 

{{-}}

### Werkzeugleistensymbol Ausgewählte Zeilen etikettieren

![[_media/Toolbar-TagSelectedRows-Icon-DropDownMenu-overview-example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Verfügbare Ettiketierungsaktionen über das Symbol " Ausgewählte Zeilen markieren" in der Werkzeugleiste - Übersicht über das Aufklappmenü - Beispiel]]

Oder klicke auf die Werkzeugleistenschaltfläche ![[_media/16x16-gramps-tag.png]], um auf dieselben Optionen wie im Menü zuzugreifen. {{-}} Siehe auch:

- [Etikettenbericht](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte_-_Teil_6#Etikettenbericht) das listet primäre Objekte (Person, Familie, Notizen), die mit dem ausgewählten Etikett übereinstimmen.

{{-}}

### Neues Etikett Dialog

![[_media/NewTag-dialog-default-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Neues Etikett" Dialog - Standard]]

![[_media/NewTag-dialog-ShowingMultipleListSelection-example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Anhängen eines "Neuen Etiketts" an die Auswahl mehrerer Listeneinträge - Beispiel mit "Neues Etikett"-Dialog]]

Du kannst eine neues Etikett entweder zu einem einzelnen Listeneintrag oder zu mehreren Listeneinträgen aus einer der Kategorielistenansichten hinzufügen, indem du die Auswahl triffst und dann das Dialogfeld verwendest, um den Namen des Etiketts einzugeben und, falls gewünscht, für das Etikett mit dem Farbwähler. Beachte, dass die Reihenfolge der Etiketten in der Liste Etiketten organisieren die Priorität für die Einfärbung der Zeilen in den Kategorielistenansichten bestimmt.

Etiketten können mit allen [primären Objekten](wiki:De:Gramps_Glossar#primary_object) verwendet werden. {{-}}

##### Etikettierung einer Auswahl von Objekten

Aufgrund der statischen Natur von Etiketten kann es nützlich sein, ein Etikett zu einer Auswahl von Objekten hinzuzufügen. So sollte es beispielsweise möglich sein, in der [Personen(listen)ansicht](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Kategorien#Personenkategorie) eine Reihe von Personen auszuwählen und ihnen ein neues oder ein bestehendes Etikett hinzuzufügen. {{-}}

### Etiketten organisieren Fenster

![[_media/MenuEditTag-OrganizeTags-dialog-example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Etiketten organisieren - Dialog - Beispiel]]

Im Dialogfeld werden Etiketten in einer Liste angezeigt, die den `Namen` und die `Farbe` enthält, wobei die Reihenfolge der Etiketten in der Liste die Priorität für die Einfärbung der Zeilen in den Kategorieansichten festlegt. Du kannst die Etiketten auch neu anordnen, indem du eines auswählst und die Schaltflächen oder verwendest. Mit wird das Dialogfeld angezeigt, und mit der Schaltfläche wird das Dialogfeld angezeigt. Über die Schaltfläche gelangst du zu dieser Seite. Sobald du fertig bist, kannst du den Dialog mit schließen.

{{-}}

#### Etikett entfernen <Etikettname> Dialog

![[_media/Remove-tag-dialog-example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Etikett entfernen <Etikettname> Dialog - Beispiel]]

### Etikettenauswahldialog

![[_media/TagSelection-dialog-example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Etikettenauswahl" Dialog - Beispiel]]

Wenn du die Schaltfläche ![[_media/16x16-gramps-tag.png]] in einem der Editor-Dialoge wie z.B. verwendest, wird die Dialogliste zur angezeigt, mit der du vorhandene benutzerdefinierte Etiketten entfernen oder zuweisen kannst. Die Etiketten werden in alphabetischer Reihenfolge angezeigt und nicht die im Fenster Etiketten organisieren angezeigte Reihenfolge. {{-}}

### Verwendung von Etiketten

Hier sind einige Ideen für Operationen, die mit Etiketten durchgeführt werden können

#### Filtern

![[_media/Sidebar-PeopleTreeView-Filter-TagDropDownList-example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Gramps Filter Seitenleiste - Etikettenliste Beispiel]]

Die offensichtlichste ist filtern.

- Etiketten und Filter erstellen beide Untermengen des Baums. Doch es gibt faktische Unterschiede in der Anwendung.

Die Familie deines Vaters mit Hilfe von Filtern zu bestimmen ist einfach; es existieren bereits Filter mit bestimmter Logik, die dies erledigen. Auf der anderen Seite Personen zu bestimmen, die in die USA ausgewandert sind, ist erheblich schwieriger, während es für berühmte Personen in deiner Familie schlicht unmöglich ist, da keine schlüssige Regel existiert. Etiketten sind hier erheblich besser geeignet.

Dennoch haben Filter den Vorteil, das sie **dynamisch** sind. Wenn du einen Vorfahren deines Vaters dem Stammbaum hinzufügst, wird er automatisch dem Filter hinzugefügt.

Auf der anderen Seite sind Etiketten **statisch**. Wenn eine berühmte Person der Datenbank hinzugefügt wird, musst du sie explizit als **BERÜHMT** etikettieren.

- Das unmittelbarste Objekt, das einem in den Sinn kommt, sind die Personen, und das ist auch das nützlichste. Es könnten aber auch andere Objekte etikettiert werden:
  - Orte: Zum Beispiel "Orte die besucht werden sollten",
  - Quellen: Zum Beispiel "Quellen in englisch",
  - Notizen: Zum Beispiel "Notizen in Arbeit", oder "Notizen in englisch",
  - Medien: Zum Beispiel "Bilder, die zu Onkel Alfred gehören".

Etiketten können mit **allen primären Objekten** verwendet werden. {{-}}

#### Etikettenspalte

![[_media/PeopleListView-ExampleTagColoredRows-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Personen (Liste) Ansicht - Anzeige der Spalte " Etikett " und farbige Etikett Zeilen - Beispiel]]

Verwende den , um die `Etiketten`-Spalte zu den Listenansichten der Objekte hinzuzufügen, damit du deine Etiketten leicht sehen kannst. Der Inhalt der `Etiketten`-Spalte wird dann als kommagetrennte Liste der mit den Objekten verbundenen Etiketten angezeigt. Beachte, dass die Reihenfolge der Etiketten in der Liste des Dialogs die Priorität für die Färbung der Zeilen in den Listenansichten der Kategorien bestimmt.

#### Verwendungsbericht für Etiketten

Der [Bericht über die Verwendung von Etiketten](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte_-_Teil_6#Etikettenbericht) listet die [primären Objekte](wiki:De:Gramps_Glossar#primäres_Objekt) (Person, Familie, Notizen) auf, die das ausgewählte Etikett haben.

### Siehe auch

- [Etiketten in Gramps](wiki:Tags_in_Gramps) - eine Einführung
- Automatische [Import Zeitstempel Etiketten](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Einstellungen#Import)
- gefiltertes [Hinzufügen/Entfernen Markierungswerkzeug](wiki:Addon:AddRemoveTagTool) (Zusatzmodul eines Drittanbieters für Gramps)

{{-}}

[F](wiki:Category:De:Dokumentation) [H](wiki:Category:Filters)
