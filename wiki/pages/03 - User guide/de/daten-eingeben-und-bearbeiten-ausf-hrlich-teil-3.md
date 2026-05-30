---
title: 'De:Gramps 6.0 Wiki Handbuch - Daten eingeben und bearbeiten: Ausführlich -
  Teil 3'
categories:
- De:Dokumentation
- Stub
managed: false
source: wiki-scrape
wiki_revid: 130762
wiki_fetched_at: '2026-05-30T17:42:26Z'
lang: de
---

{{#vardefine:chapter\|9.3}} {{#vardefine:figure\|0}} **<span style="font-size:120%">Daten eingeben und bearbeiten: Ausführlich Namen, Attribute, Adressen, Zusammenführen</span>**  
Der vorhergehende Abschnitt bot dir eine detaillierte Übersicht wie man die Hauptobjekte in Gramps erstellt und bearbeitet. Dieser Abschnitt wird mit anderen Objekten fortgesetzt, denen du in Gramps begegnest.

## Namenseditor

Namen werden über das Dialogfeld bearbeitet, das auf der Registerkarte des Dialogfelds verfügbar ist. Neben der Bearbeitung des Namens ermöglicht der Namenseditor: die Definition mehrerer Nachnamen, Aliasnamen, die Auswahl des bevorzugten Namens (nach Epoche) und das Überschreiben von Anzeigeformat, Gruppen und Sortierung.

Die Namen in Gramps werden in dem Format angezeigt, das im Abschnitt „Anzeigeoptionen“ der [Registerkarte](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Einstellungen#Anzeigeoptionen) im Dialogfeld ausgewählt wurde. Andere vordefinierte Anzeigeformate können aus dem Einblendmenü ausgewählt werden. Neue Namensformate können mit dem erstellt werden, indem du auf die Schaltfläche klickst. {{-}}

### Namenseditor Dialog

![[_media/NameEditor-dialog-example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;Namenseditor&quot; - Dialog - Beispiel]] Der obere Bereich des Dialog Fensters ermöglicht die Eingabe der Namensart (z.B. Geburtsname, Name nach Hochzeit, usw.) aus einer Aufklappliste wählen. Als nächstes kommen die Elemente des persönlichen Namens in den meisten Fällen als Teile des Vornamen zusammengefasst. Nach dem Vornamenbereich folgt der Nachnamenbereich. Unten befinden sich Elemente die das Anpassen der Namenssortierung ermöglichen, Daten für Namen, Namensquellen und Notizen für die Namen. {{-}}

#### Art

- (`Geburtsname` Standardeinstellung) In der Dropdown-Liste Namenstyp kannst du die eingegebene Namensart auswählen. Du kannst auch direkt eine [benutzerdefinierte](wiki:De:Gramps_Glossar#benutzerdefiniert) Art in dieses Feld eingeben.

- schalte das Symbol in der oberen rechten Ecke um, um diesen Namensdatensatz als vertraulich zu markieren. Auf diese Weise kannst du diesen Namen nicht in Berichte aufnehmen, wenn du dies unter den Optionen für die Berichterstellung auswählst.

{{-}}

#### Vorname(n) Bereich

Der **Vorname(n)** Bereich enthält alle Teile des persönlichen Namens die du in Gramps speichern kannst:

- , Die Vornamen der Person sollte alle hier eingegeben werden.

- , Der offizielle juristische Vorname der normalerweise von der Person verwendet wurde, sollte hier eingegeben werden. Zum Beispiel jemand heißt Johann Heinrich Schmidt und verwendet den Namen Johann sollte *Johann* hier eingegeben werden. Wenn die Person *Hans* verwendet, sollte dieser unter Spitzname eingetragen werden da Hans kein offizieller Vorname der Person ist (siehe weiter unten). In Deutschland und an einigen anderen Orten war es üblich den Rufnamen zwischen den anderen Vornamen zu unterstreichen (siehe auch [hier](wiki:Namen_in_Gramps)).

- , Der Titel einer Person wie Doktor kann hier eingegeben werden.

- , Der Suffix des persönlichen Namens wie zum Beispiel Junior (Jun). oder III. sollte hier eingegeben werden.

- , Der Spitzname einer Person sollte hier eingegeben werden. Spitznamen beinhalten auch Kurzformen des korrekten Namens wie Hans für Johann (vergleiche Rufname oben).

{{-}}

#### Nachnamen Bereich

Der **Nachnamen** Bereich enthält die Elemente des Nachnamens der Person. Gramps erlaubt sowohl mehrfach Nachnamen als auch mehrere Arten von Nachnamen.

- Werkzeugleiste - / / / /

Die folgenden Spalten werden angezeigt:

- Ein für den Nachnamen wird nicht für die Sortierung verwendet (wie "von" oder "de").

- für den Hauptteil des Nachnamen.

- oft in matronymischen oder patronymischen Namensschemen verwendet wie *dotter*.

- zeigt den Typ des Familiennamen wie er ist und dessen Herkunft.

Das folgende Feld wird angezeigt:

- für Familien die üblicherweise mit einem örtlichen Spitznamen bezeichnet werden.

Siehe auch: [Namen Wiki Eintrag](wiki:De:Namen_in_Gramps) {{-}}

### Namenseditor Registerkarten

Die folgenden Registerkarten sind verfügbar:

- 

- 

- 

#### Allgemein

Optionen ermöglichen dir gezielte Gruppierung, Sortierung und Anzeige Eigenschaften für den Namen fest zu legen genauso wie ein zu dem Namen gehörendes Datum anzugeben.

- Das Feld bietet eine alternative Gruppierung in der Personenansicht, welche die Standardgruppierung die auf dem Nachnamen basiert überschreibt. Dies kann nötig sein bei ähnlichen Familiennamen, die zusammen Gruppiert werden sollten -- zum Beispiel russische Namen Ivanov und Ivanova sind identisch werden aber je nach Geschlecht unterschiedlich geschrieben. Siehe [Nachnamen gruppieren](wiki:De:Nachnamen_gruppieren)
  -  Aktiviere dieses Kontrollkästchen, um die Eingabe in dieses Feld zu aktivieren. (Kontrollkästchen standardmäßig deaktiviert)

  
Personen werden entsprechend dem Namensformat in den Präferenzen angezeigt (die Standardeinstellung).

Hier kannst du festlegen, das diese Person entsprechend einem benutzerdefinierten Namensformat angezeigt wird. *(Weitere Namensformate können auf der Registerkarte ausgewählt oder mit dem [Anzeigename-Editor](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Einstellungen#Anzeigename-Editor) angepasst werden.)*

- und legen fest, wie die Namen in der Personenansicht und den Berichten erscheinen. Sortieren als ermöglicht dir das Namensmuster welches in den Präferenzen zur Sortierung der Namen eingestellt ist, zu überschreiben. Zum Beispiel, du hast plötzlich einen Zweig mit Schwedischen Namen mit Vornamen und Patronymikon aber der Rest deiner Datenbank sortiert die Namen nach Familienname, Vorname. Du kannst hier angeben, diesen Namen immer als Patronymikon, Vorname zu sortieren.

  
Hier kannst du festlegen, das diese Person entsprechend einem benutzerdefinierten Namensformat sortiert wird. *(Weitere Namensformate können auf der Registerkarte ausgewählt oder mit dem [Anzeigename-Editor](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Einstellungen#Anzeigename-Editor) angepasst werden.)*

ermöglicht dir fest zu legen, wie der Name angezeigt wird. Möglicherweise möchtest du beispielsweise einen Namen anhand des Vor- oder Nachnamens einer Person sortieren, die Anzeige zeigt jedoch weiterhin einen Ehrentitel vor diesem Namen an. *(Weitere Namensformate können auf der Registerkarte ausgewählt oder mit dem [Anzeigename-Editor](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Einstellungen#Anzeigename-Editor) angepasst werden.)*

Die Personenbaumansicht gruppiert Personen nach ihrem primären Nachnamen. Du kannst dies mit einem hier gesetzten Gruppierungswert überschreiben. Du wirst gefragt, ob du nur diese Person anders gruppieren willst oder alle Personen mit diesem primären Nachnamen.

- Das kann Informationen über die Gültigkeit des Namen liefern -- verwende wenn nötig Zeiträume. Die Datum bearbeiten Schaltfläche öffnet den [Datumseditor](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Daten_eingeben_und_bearbeiten:_Ausführlich_-_Teil_1#Daten_bearbeiten). Z.B. bei einem Namen nach Heirat das Datum an dem der Name das erste mal verwendet wurde oder das Hochzeitsdatum.

#### Quellenangaben

Der Reiter zeigt Informationen über für diesen Namen relevante Quellen und Fundstellen und Bedienelemente die deren Änderung ermöglichen. Der zentrale Bereich zeigt eine Liste all dieser Fundstellen und Quellen aus der Datenbank. Die Schaltflächen , und ermöglichen dir entsprechend das Hinzufügen, Ändern und Entfernen einer Fundstelle zu diesem Namen. Beachte das die und Schaltflächen nur verfügbar sind wenn eine Quellenreferenz aus der Liste gewählt ist.

Mehr Informationen: [Fundstelleneditor](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Daten_eingeben_und_bearbeiten:_Ausführlich_-_Teil_2#Quellenfundstellen_bearbeiten)

#### Notizen

Der Reiter zeigt jede Notiz, die den Namen betrifft. Um eine Notiz hinzuzufügen oder eine bestehende Notiz zu bearbeiten, bearbeite einfach den Text im Texteingabefeld.

Mehr Informationen: [Notizeditor](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Daten_eingeben_und_bearbeiten:_Ausführlich_-_Teil_2#Informationen_über_Notizen_bearbeiten)

## Attribute

Wenn du [Attribute](wiki:Attributes_in_Gramps) über die Dialog Registerkarte hinzufügst oder bearbeitest, wird das Dialogfeld angezeigt. {{-}}

### Attributeditor Dialog

![[_media/AttributeEditor-dialog-default-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;Attributeditor&quot; - Dialog - Standard]] Der obere Bereich des Dialog Fensters zeigt den Namen des Dialog mit dem Namen der Person deren Attribute bearbeitet werden. Der Zentrale Bereich des Fensters enthält drei Reiter die verschiedene Kategorien von verfügbaren Informationen enthalten. Du kannst jeden Reiter zu Ansicht oder zum bearbeiten durch klicken auf die entsprechende Reiterbeschriftung in den Vordergrund holen. Der untere Bereich enthält und Schaltflächen. Klicken der Schaltfläche übernimmt jederzeit alle Änderungen die in allen Reitern gemacht wurden und schließt das Dialogfenster. Klicken der Schaltfläche schließt jederzeit das Dialogfenster und verwirft alle Änderungen.

Der obere Bereich ermöglicht das Bearbeiten der Hauptinformationen des Attributs:

- (`Identifikationsnummer` Vorgabe) Der Name eines Attributs, das du verwenden möchtest. Beispiel: *Größe* (für eine Person), *Wetter an diesem Tag* (für ein Ereignis), ... Verwende diese Option, um Ausschnitte von Informationen zu speichern, die du sammeln und die du korrekt mit Quellen verknüpfen möchtest. Attribute können für Personen, Familien, Ereignisse und Medien verwendet werden. Die Informationen können in die entsprechenden Texteingabefelder eingegeben werden. Der Attributname kann auch aus den verfügbaren Optionen (falls vorhanden) ausgewählt werden, die im Dropdown-Menü aufgeführt sind.

  - Schalte diese Option um, um diesen Attributdatensatz als vertraulich oder öffentlich zu markieren. Auf diese Weise kannst du dieses Attribut nicht in die Berichte aufnehmen, wenn du dies unter den Optionen für die Berichterstellung auswählst.

- Der des Attribut. Z.B. *1,8m, sonnig oder blaue Augen*.

{{-}}

#### Attribut-Editor-Kontextmenü

{{-}}

### Attributeditor Registerkarten

Die folgenden Registerkarten sind verfügbar:

- [Quellenangaben](##Quellenangaben_2)
- [Notizen](##Notizen_2)

#### Quellenangaben

  
Der Reiter zeigt Informationen über für dieses Attribut relevante Fundstellen und Quellen und Bedienelemente die deren Änderung ermöglichen. Der zentrale Bereich zeigt eine Liste all dieser Quellen und Fundstellen aus der Datenbank. Die Schaltflächen , und ermöglichen dir entsprechend das Hinzufügen, Ändern und Entfernen einer Quellenreferenz zu diesem Attribut. Beachte, das die und Schaltflächen nur verfügbar sind wenn eine Fundstelle/Quelle aus der Liste gewählt ist.

#### Notizen

Der Reiter zeigt alle das Attribut betreffende Notizen an. Zum Hinzufügen oder Ändern einer Notiz bearbeite einfach den Text im Texteingabefeld.

## Adressen

Wenn du eine Adresse auf der Registerkarte des Dialog hinzufügst oder bearbeitest, wird das Dialogfeld angezeigt. {{-}}

### Adresseditor Dialog

![[_media/AddressEditor-dialog-default-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;Adresseditor&quot; - Dialog - Standard]] Im Dialogfeld kannst du eine aktuelle Adresse aufzeichnen, indem du die Informationen in die entsprechenden Texteingabefelder einträgst.

Im oberen Bereich des Dialogfelds können Informationen zur Adresse bearbeitet und eingegeben werden:

-   
  Datum an dem die Adresse gültig ist.

  - ![[_media/22x22-gramps-date.png]] Schaltfläche startet den Dialog.

-   
  Die Straße der Adresse.

- Schaltfläche. Schalte diese Schaltfläche um, um diesen Adressdatensatz als veertraulich oder öffentlich zu markieren. Auf diese Weise kannst du dieses Attribut nicht in die Berichte aufnehmen, wenn du dies unter den Optionen für die Berichterstellung auswählst.

-   
  Der Name der Lokalität der Adresse.

-   
  Der Staat oder Landkreis der Adresse, wenn eine Postadresse dies enthalten muss.

-   
  Der Ort oder die Stadt der Adresse.

-   
  Das Land der Adresse.

-   
  Die Postleitzahl.

-   
  Die Telefonnummer die zu der Adresse gehört.

Im unteren Bereich des Dialogfelds befinden sich die Schaltflächen , und . Wenn du jederzeit auf die Schaltfläche klickst, werden alle auf allen Registerkarten vorgenommenen Änderungen übernommen und das Dialogfenster geschlossen. Wenn du jederzeit auf die Schaltfläche klickst, wird das Fenster geschlossen, ohne dass Änderungen vorgenommen werden. {{-}}

### Adresseditor Registerkarten

Die folgenden Registerkarten enthalten verschiedene Kategorien verfügbarer Informationen. Du kannst jede Registerkarte zum Anzeigen oder Bearbeiten nach oben bringen, indem du auf die entsprechende Registerkarte klickst.

#### Quellenangaben

  
Der Reiter zeigt Informationen über für diese Adresse relevante Quellen und Bedienelemente die deren Änderung ermöglichen. Der zentrale Bereich zeigt eine Liste all dieser Quellen und Fundstellen aus der Datenbank. Die Schaltflächen , und ermöglichen dir entsprechend das Hinzufügen, Ändern und Entfernen einer Fundstelle/Quelle zu dieser Adresse. Beachte, dass die und Schaltflächen nur verfügbar sind wenn eine Quellenreferenz aus der Liste gewählt ist.

#### Notizen

  
Der Reiter zeigt jede die Adresse betreffende Notiz. Um eine Notiz hinzuzufügen oder eine bestehende zu ändern bearbeite einfach den Text im Texteingabefeld.

{{-}}

## Datensätze zusammenführen

![[_media/PeopleCategory-Toolbar-MergeTheSelectedPersons-icon-example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;Gewählte Personen zusammengfassen&quot; - &quot;Zusammenfasen...&quot; Werkzeugleistensymbol - Beispiel]] Manchmal stellt sich heraus, das mehrere Datensätze in der Datenbank das selbe Objekt beschreiben: selbe Person, selber Ort, oder selbe Fundstelle/Quelle. Das kann auch passieren wenn die Daten aus versehen zweimal eingegeben wurden oder wenn neue Informationen zeigen, das zwei Einträge zu der selben Person gehören. Es kann auch passieren nach dem Import einer GEDCOM Datei die du von einem Verwandten erhalten hast, dessen Datenbank sich mit deinen Daten überschneiden.

Immer wenn du doppelte Datensätze entdeckst ist das Zusammenfassen ein nützlicher Weg die Situation zu bereinigen.

General usage  
Merging of two records is accomplished by selecting one entry and then selecting another entry while holding down the key and selecting either the or toolbar icon or context menu option.

The following merge options are available:

- [Personen zusammenführen](#Personen_zusammenf.C3.BChren)
- [Familien zusammenführen](#Familien_zusammenf.C3.BChren)
- [Ereignisse zusammenführen](#Ereignisse_zusammenf.C3.BChren)
- [Orte zusammenführen](#Orte_zusammenf.C3.BChren)
- [Quellen zusammenführen](#Quellen_zusammenf.C3.BChren)
- [Fundstellen zusammenführen](#Fundstellen_zusammenf.C3.BChren)
- [Aufbewahrungsorte zusammenführen](#Aufbewahrungsorte_zusammenf.C3.BChren)
- [Medienobjekte zusammenführen](#Medienobjekte_zusammenführen)
- [Notizen zusammenführen](#Notizen_zusammenf.C3.BChren)

{{-}}

### Personen zusammenführen

![[_media/MergePeople-dialog-default-example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Dialogfeld „Personen zusammenführen“ – mit standardmäßig erweitertem Abschnitt „Kontextinformationen“ – Beispiel]]

Wenn genau zwei Personen markiert sind, wähle um den Dialog zu öffnen.

Der Dialog erlaubt zu entscheiden ob die gewählten Datensätze zusammengefasst werden sollen oder nicht. Wenn du entscheidest die Datensätze sollten nicht zusammen gefasst werden, trotz gleichen Namens, klicke um den Dialog ohne jede Änderung zu schließen.

Du kannst die Felder unten links erweitern, um weitere Informationen anzuzeigen, anhand derer du entscheiden kannst, welche Auswahl als primäre Information für die Zusammenführung beibehalten werden soll.

Das Feld unten links zeigt weitere Informationen zu den Personen, die zusammengeführt werden sollen.

Wenn du dich für die Zusammenführung entscheidest, wähle das entsprechende Auswahlfeld ![[_media/RadioButton_Selected.png]] aus, um den Datensatz anzugeben

- Name
- Geschlecht
- Gramps-ID,

`der als Quelle für die primären Daten verwendet werden soll, und klicke dann auf ``. Die Daten aus dem anderen Datensatz werden als alternative Daten beibehalten.`

Spezifisch werden alle Namen von dem anderen Datensatz Zweitnamen des vermischten Datensatz. Ähnlich werden Eltern, Gatten und Kinder des anderen Datensatz zweit Eltern, Gatten und Kinder des vermischten Datensatz und so weiter.

Siehe auch:

- [Finde mögliche doppelte Personen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Werkzeuge#Finde_m.C3.B6gliche_doppelte_Personen)
- [Personen zusammenführen](wiki:Merging_people) (englisch)

{{-}} ![[_media/MergePeople-dialog-sections-expanded-example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Dialogfeld „Personen zusammenführen“ – mit erweiterten Abschnitten „Detaillierte Auswahl“ und „Kontextinformationen“ – Beispiel]] {{-}}

### Familien zusammenführen

![[_media/MergeFamilies-dialog-default-example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Familien zusammenfassen - Dialog - Vorgabe Beispiel]]

Wenn genau zwei Familien markiert sind, wähle um den Dialog zu öffnen.

Der Dialog ermöglicht dir zu entscheiden, ob gewählten Datensätze zusammen gefasst werden sollen oder nicht. Wenn du entscheidest, dass die Datensätze trotz ähnlicher Eigenschaften nicht zusammengeführt werden sollen, kannst du auf klicken, um das Dialogfeld zu schließen, ohne Änderungen vorzunehmen.

Du kannst entweder eine der beiden Familien als Quelle für die primären Daten für die neue Familie wählen oder du kannst durch erweitern des Feld wählen welcher Vater die Quelle für die primären Daten ist, welche Mutter die Quelle für die primären Daten ist und welche Familie (Auswahl über Gramps-ID) die Quelle für die restlichen primären Daten ist.

Wenn du dich für die Zusammenführung entscheidest, wählst du die entsprechenden Familien ![[_media/RadioButton_Selected.png]] Auswahlfelder aus, um die Quelle(n) der Primärdaten anzugeben

- Vater
- Mutter
- Beziehung
- Gramps-ID,

die für den zusammengeführten Familieneintrag verwendet werden sollen, und klickst dann auf .

Die Kinder aus beiden Ehen werden in die neue Familie zusammengeführt. Die beiden Väter werden zusammengeführt und die Ereignisse des sekundären Vaters werden dem primären Vater zugeordnet. Die Namen des sekundären Vaters werden zu alternativen Namen für den primären Vater. Das Gleiche gilt für die beiden Mütter. Die Ereignisse, die sich auf die sekundäre Familie beziehen (z. B. Heirat und Scheidung), werden auf die primäre Familie übertragen. Die sekundäre Familie und die Personendatensätze für den sekundären Vater und die sekundäre Mutter werden aus der Datenbank gelöscht.

![[_media/MergeFamilies-dialog-DetailedSelection-section-expanded-example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} „Familien zusammenführen“ – Dialogfeld – mit erweitertem Abschnitt „Detaillierte Auswahl“ – Beispiel]] {{-}}

### Ereignisse zusammenführen

![[_media/MergeEvents-dialog-example-default-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;Ereignisse zusammenfassen&quot; - Dialog - Vorgabe Beispielexample]] Wenn genau zwei Ereignisse markiert sind, wähle um den Dialog zu öffnen.

Der Dialog ermöglicht dir zu entscheiden, ob gewählten Datensätze zusammen gefasst werden sollen oder nicht.

Durch Erweitern des Felds kannst du zusätzliche Informationen zur Zusammenführung anzeigen.

Wenn du beschließt, das die Datensätze trotz ähnlichen Titel nicht zusammen gefasst werden sollen, kannst du auf klicken um den Dialog zu schließen ohne irgendwelche Änderungen vor zu nehmen.

Wenn du beschließt, das Zusammenfassen fortzusetzen, wähle die entsprechenden ![[_media/RadioButton_Selected.png]] Optionsfelder:

- Art
- Datum
- Ort
- Beschreibung
- Gramps-ID

die für den zusammengefassten Datensatz verwendet werden sollen, dann klicke . {{-}} ![[_media/MergeEvents-dialog-DetailedSelection-section-expanded-example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;Ereignisse zusammenfassen&quot; - mit &quot;Detailauswahl&quot; Abschnitt wurde erweitert - Beispiel]] {{-}}

### Orte zusammenführen

![[_media/MergePlaces-dialog-example-default-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;Orte zusammenfassen&quot; - Dialog - Vorgabe Beispiel]] Wenn genau zwei Orte markiert sind, wähle um den Dialog zu öffnen.

Im Dialogfeld kannst du entscheiden, ob die ausgewählten Datensätze zusammengeführt werden sollen oder nicht.

Durch Erweitern des Felds kannst du zusätzliche Informationen zur Zusammenführung anzeigen.

Wenn du entscheidest die Datensätze sollten nicht zusammen gefasst werden, trotz gleichen Titels, klicke um den Dialog ohne jede Änderung zu schließen.

Wenn du beschließt, das Zusammenfassen fortzusetzen, wähle die entsprechenden ![[_media/RadioButton_Selected.png]] Optionsfelder:

- Ortsname
- Art
- Kennung
- Breitengrad
- Längengrad
- Gramps-ID

die für den zusammengefassten Datensatz verwendet werden sollen, dann klicke . {{-}} ![[_media/MergePlaces-dialog-DetailedSelection-section-expanded-example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;Orte zusammenfassen&quot; Dialog - mit &quot;Detailauswahl&quot; Abschnitt wurde erweitert - Beispiel]] {{-}}

#### Orte können nicht zusammengeführt werden – Schleife in der Ortshierarchie – Warnungsdialogfeld

Wenn du versuchst, zwei (2) Orte zusammenzuführen, was zu einer Schleife in der Ortshierarchie führen würde, wird dir der Warnhinweis mit der Meldung *Das Zusammenführen dieser Orte würde zu einer Schleife in der Ortshierarchie führen.* angezeigt. Zum Beispiel würde der Versuch, ein Land der obersten Ebene mit einer der zugehörigen Städte zusammenzuführen, Folgendes anzeigen: ![[_media/Cannot-merge-places-cycle-in-place-hierarchy-example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} {man label|Orte können nicht zusammengeführt werden.}} Warndialog mit der Meldung Das Zusammenführen dieser Orte würde zu einer Schleife in der Ortshierarchie führen. Beispiel]] {{-}}

### Quellen zusammenführen

![[_media/MergeSources-dialog-example-default-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;Quellen zusammenfassen&quot; - Dialog - Vorgabe Beispiel]] Wenn genau zwei Quellen markiert sind, wähle um den Dialog zu öffnen.

Durch Erweitern des Felds kannst du zusätzliche Informationen zur Zusammenführung anzeigen.

Der Dialog erlaubt zu entscheiden ob die gewählten Datensätze zusammengefasst werden sollen oder nicht.

Wenn du entscheidest, die Datensätze sollten nicht zusammen gefasst werden, trotz gleichen Titels, klicke um den Dialog ohne jede Änderung zu schließen.

Wenn du beschließt, das Zusammenfassen fortzusetzen, wähle die entsprechenden ![[_media/RadioButton_Selected.png]] Optionsfelder:

- Titel
- Autor
- Verkürzter Titel
- Veröffentlichung
- Gramps-ID

die für den zusammengefassten Datensatz verwendet werden sollen, dann klicke . {{-}} ![[_media/MergeSources-dialog-DetailedSelection-section-expanded-example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;Quellen zusammenfassen&quot; - mit &quot;Detailauswahl&quot; Abschnitt wurde erweitert - Dialog - Beispiel]] {{-}}

### Fundstellen zusammenführen

![[_media/MergeCitations-dialog-example-default-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;Fundstellen zusammenfassen&quot; - Dialog - Vorgabe Beispiel]] Wenn genau zwei Fundstellen markiert sind [mit identischen Quellen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Daten_eingeben_und_bearbeiten:_Ausführlich_-_Teil_3#Fundstellen_mit_unterschiedlichen_Quellen_können_nicht_zusammengeführt_werden._Warnungsdialogfeld), wähle um den Dialog zu öffnen.

Durch Erweitern des Felds kannst du zusätzliche Informationen zur Zusammenführung anzeigen.

Der Dialog ermöglicht dir zu entscheiden, ob gewählten Datensätze zusammen gefasst werden sollen oder nicht.

Wenn du entscheidest, die Datensätze sollten nicht zusammen gefasst werden, trotz gleichen Titels, klicke um den Dialog ohne jede Änderung zu schließen.

Wenn du beschließt, das Zusammenfassen fortzusetzen, wähle die entsprechenden ![[_media/RadioButton_Selected.png]]Optionsfelder:

- Band/Seite
- Datum
- Vertrauensgrad
- Gramps-ID

die für den zusammengefassten Datensatz verwendet werden sollen, dann klicke .

{{-}} ![[_media/MergeCitations-dialog-DetailedSelection-section-expanded-example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} „Fundstellen zusammenführen“ – mit erweitertem Abschnitt „Detaillierte Auswahl“ – Dialogfeld – Beispiel]] {{-}} Siehe auch

- [Fundstellen zusammenfassen...](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Werkzeuge#Fundstellen_zusammenfassen) Werkzeug.

#### Fundstellen mit unterschiedlichen Quellen können nicht zusammengeführt werden. Warnungsdialogfeld

`   +   `

![[_media/Cannot-merge-citations-with-different-sources-warning-dialog-example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}}  -Mit-verschiedenen-Quellen-Warndialog - Beispiel]]

Beachte, dass die beiden ausgewählten Fundstellen entweder dieselben Quellen haben müssen oder nur eine oder keine der Fundstellen eine Quelle hat, sonst wird dir bei der Auswahl zum Zusammenführen der Warnhinweis mit dem Hinweis *Wenn du diese beiden Fundstellen zusammenführen möchtest, musst du zuerst die Quellen zusammenführen.* angezeigt. {{-}}

### Aufbewahrungsorte zusammenführen

![[_media/MergeRepositories-dialog-example-default-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;Aufbewahrungsorte zusammenfassen&quot; - Dialog - Vorgabe Beispiel]] Wenn genau zwei Aufbewahrungsorte markiert sind, wähle um den Dialog zu öffnen.

Durch Erweitern des Felds kannst du zusätzliche Informationen zur Zusammenführung anzeigen.

Der Dialog ermöglicht dir zu entscheiden, ob gewählten Datensätze zusammen gefasst werden sollen oder nicht.

Wenn du beschließt, das die Datensätze trotz ähnlichen Titel nicht zusammen gefasst werden sollen, kannst du auf klicken um den Dialog zu schließen ohne irgendwelche Änderungen vor zu nehmen.

Wenn du beschließt, das Zusammenfassen fortzusetzen, wähle die entsprechenden ![[_media/RadioButton_Selected.png]] Optionsfelder:

- Name
- Art
- Gramps-ID

die für den zusammengefassten Datensatz verwendet werden sollen, dann klicke . {{-}} ![[_media/MergeRepositories-dialog-DetailedSelection-section-expanded-example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;Aufbewahrungsorte zusammenfassen&quot; - mit &quot;Detailauswahl&quot; Abschnitt wurde erweitert - Dialog - Beispiel]] {{-}}

### Medienobjekte zusammenführen

![[_media/MergeMediaObjects-dialog-example-default-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;Medienobjekte zusammenfassen&quot; - Dialog - Vorgabe Beispiel]] Wenn genau zwei Medienobjekte markiert sind, wähle um den Dialog zu öffnen.

Durch Erweitern des Felds kannst du zusätzliche Informationen zur Zusammenführung anzeigen.

Der Dialog ermöglicht dir zu entscheiden, ob gewählten Datensätze zusammen gefasst werden sollen oder nicht.

Wenn du beschließt, das die Datensätze trotz ähnlichen Titel nicht zusammen gefasst werden sollen, kannst du auf klicken um den Dialog zu schließen ohne irgendwelche Änderungen vor zu nehmen.

Wenn du beschließt, das Zusammenfassen fortzusetzen, wähle die entsprechenden ![[_media/RadioButton_Selected.png]] Optionsfelder:

- Titel
- Pfad
- Datum
- Gramps-ID

die für den zusammengefassten Datensatz verwendet werden sollen, dann klicke . {{-}} ![[_media/MergeMediaObjects-dialog-DetailedSelection-section-expanded-example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;Medienobjekte zusammenfassen&quot; - mit &quot;Detailauswahl&quot; Abschnitt wurde erweitert - Dialog - Beispiel]] {{-}}

### Notizen zusammenführen

![[_media/MergeNotes-dialog-example-default-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Notizen zusammenfassen - Dialog - Vorgabe Beispiel]] Wenn genau zwei Notizen markiert sind, wähle zum öffnen des Dialog.

Durch Erweitern des Felds kannst du zusätzliche Informationen zur Zusammenführung anzeigen.

Der Dialog ermöglicht dir zu entscheiden, ob gewählten Datensätze zusammen gefasst werden sollen oder nicht.

Wenn du beschließt, das die Datensätze trotz ähnlichen Titel nicht zusammen gefasst werden sollen, kannst du auf klicken um den Dialog zu schließen ohne irgendwelche Änderungen vor zu nehmen.

Wenn du beschließt, das Zusammenfassen fortzusetzen, wähle die entsprechenden ![[_media/RadioButton_Selected.png]] Optionsfelder:

- Text
- Art
- Format
- Gramps-ID

die für den zusammengefassten Datensatz verwendet werden sollen, dann klicke . {{-}} ![[_media/MergeNotes-dialog-DetailedSelection-section-expanded-example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;Notizen zusammenfassen&quot; Dialog - mit &quot;Detailauswahl&quot; Abschnitt wurde erweitert - Dialog - Beispiel]]

{{-}}

[D](wiki:Category:De:Dokumentation)
