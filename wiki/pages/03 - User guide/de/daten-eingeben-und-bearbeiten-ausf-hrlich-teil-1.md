---
title: 'De:Gramps 6.0 Wiki Handbuch - Daten eingeben und bearbeiten: Ausführlich -
  Teil 1'
categories:
- De:Dokumentation
- Stub
managed: false
source: wiki-scrape
wiki_revid: 130684
wiki_fetched_at: '2026-05-30T17:40:40Z'
lang: de
---

{{#vardefine:chapter\|9.1}} {{#vardefine:figure\|0}} **<span style="font-size:120%">Daten eingeben und bearbeiten: Ausführlich Menschen, Beziehungen, Daten</span>**  
Abschnitt erweitert die [kurze Übersicht](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Daten_eingeben_und_bearbeiten:_Kurz) über die Eingabe und Bearbeitung von Daten in Gramps.

Gramps bietet dir eine Reihe von Ansichten. Jede dieser Ansichten bietet dir die Möglichkeit, Informationen einzugeben und zu bearbeiten. Tatsächlich kannst du häufig aus verschiedenen Ansichten auf dieselben Informationen zugreifen. In Gramps werden Informationen über Dialoge eingegeben und bearbeitet. Da wir diesen Begriff häufig verwenden sollten wir definieren was wir damit meinen:

Ein Dialog ist ein auf-klapp Fenster das ein oder mehrere Formulare zum eingeben und bearbeiten bietet die einer bestimmten Kategorie entsprechen. Beispiele in Gramps sind der Dialog, der Dialog, und viele andere.

Ein Dialog enthält häufig eine Reihe von "\[<https://de.wikipedia.org/wiki/Registerkarte> Registerkarten" die die Informationen in Unterkategorien aufteilen. Z.B. der Dialog hat Reiter für Unterkategorien wie Ereignisse, Attribute, Adressen, Notizen und andere.

## Informationen über Personen bearbeiten

Informationen über Personen werden über den Dialog eingegeben und bearbeitet. Dieser Dialog, der auch als Personeneditor bezeichnet wird, kann auf die folgenden Arten aus verschiedenen Ansichten gezeigt werden:

- Aus der [Personenkategorie](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Kategorien#Personenkategorie)

  
  
Den Namen der Person deren Daten du bearbeiten willst doppelklicken.

Den Namen durch einmal klicken wählen und dann auf die Schaltfläche in der Werkzeugleiste klicken.

Den Namen wählen und dann drücken.

Wähle Bearbeiten... von dem Bearbeiten Menü von Gramps.

Wähle Bearbeiten von dem Kontextmenü, das nach einem Rechtsklick auf den Namen erscheint.

- Aus den [Beziehungen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Kategorien#Beziehungenkategorie): Um die Daten der aktiven Person zu bearbeiten, auf die Schaltfläche neben dem Namen der aktiven Person klicken.

<!-- -->

- Aus der [Diagrammekategorie](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Kategorien#Diagrammekategorie): Doppelklicke in das Feld mit dem Namen der Person, deren Daten du bearbeiten möchtest.

In jedem der obigen Fälle wird der Dialog eingeblendet. {{-}} <span id="Person bearbeiten Dialog">

### Personeneditor Dialog

</span> ![[_media/Edit-person-window-new-person-example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Person bearbeiten - Fenster - Standard Neuer leerer Editor]]

![[_media/Edit-person-window-existing-person-example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Dialogfeld  - zeigt eine Beispielperson]]

Im Dialogfeld kannst du entweder neue Personeninformationen hinzufügen oder eine vorhandene Person bearbeiten.

Der obere Bereich des Fensters besteht aus zwei Teilen: Die wesentlichen Informationen über den der Person und einen Bereich mit der Schaltfläche (um den Datensatz als vertraulich zu markieren), die Auswahl des Geschlechts, eine ID die du diesem Datensatz geben kannst und ein Etikett das du mit der Person verknüpfen kannst das den Status des Datensatzes anzeigt (komplett, unvollständig, unsicher,..) welcher diesem Datensatz eine bestimmte Farbe in der Personenlistenansicht zuweist. {{-}}

Unterhalb dieses oberen Bereichs befinden sich mehrere "[Registerkarten](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Daten_eingeben_und_bearbeiten:_Ausführlich_-_Teil_1#Registerkarten_Person_bearbeiten)" mit verschiedenen Kategorien verfügbarer Informationen. Klicke auf eine beliebige Registerkarte, um deren Inhalt anzuzeigen und zu bearbeiten.

Wenn du unten auf die Schaltfläche klickst, werden alle in allen Registerkarten vorgenommenen Änderungen übernommen und das Dialogfenster geschlossen. Wenn du auf die Schaltfläche klickst, wird das Fenster geschlossen, ohne dass Änderungen übernommen werden.

{{-}} ![[_media/SaveChanges-alert-dialog-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} „Änderungen speichern?“ – Warnungsdialog]]

Wenn Daten in einer der Registerkarten geändert wurden, erscheint ein Warnfenster , in dem du aus folgenden Optionen wählen kannst:

- – Änderungen werden nicht gespeichert.

- (Standard) – die ursprüngliche Abbrechaufforderung.

- – der Änderungen.

sowie ein Kontrollkästchen zum Aktivieren von , das über die Option im Dialogfeld deaktiviert werden kann.

#### Kontextmenü des Personen-Editors

![[_media/QuickViewReport-EditPerson-context-menu-popup-default-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}}  Dialog - Anzeige des Kontextuntermenüs der Schnellansicht]] Wenn du das Kontextmenü (Rechtsklick) in einem leeren Bereich im oberen Teil des Fensters öffnest, z. B. in der Nähe des Feldes „Bevorzugter Name“ oder unterhalb des Feldes „Bevorzugtes Bild“, werden dir folgende Optionen angezeigt:

<hr>

- \-

- \-

<hr>

- Berichte sind verfügbar.

  - 

  - 

  - 

  - 

  - 

  - 

  - 

### Bevorzugtes Bild

![[_media/EditPerson-top-sections-image-with-context-menu-example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Beispiel „Bild“-Abschnitt mit Kontextmenü für den Dialog „Person bearbeiten“]]

Wenn Bilder vorhanden sind, zeigt der Personen-Editor einen zusätzlichen Bereich oben links an (ansonsten ist er ausgeblendet). Dieser bereich zeigt das erste verfügbare Bild auf der Registerkarte dieser Person.

Siehe auch

- [Fehlende Medienobjekte „Defekter Link“-Symbol einer Box mit einem roten „x“](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Einstellungen#Fehlendes_Medienobjekt-Symbol_f.C3.BCr_einen_.22defekten_Link.22_in_Form_eines_K.C3.A4stchens_mit_einem_roten_.22x)

#### Personeneditor-Bildkontextmenü

Du kannst mit der rechten Maustaste auf das Bild klicken, um die folgenden Bildkontextmenüoptionen anzuzeigen:

- – öffnet das Bild in einem externen Bildbetrachter.

- – öffnet das Dialogfeld .

{{-}}

### Bevorzugter Name Abschnitt

![[_media/EditPerson-PreferredName-section-default-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Abschnitt „Bevorzugter Name“ im Dialogfeld „Person bearbeiten“ – Standard]]

![[_media/Edit-person-window-existing-person-example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Abschnitt „Bevorzugter Name“ (neben dem Bild) im Dialogfeld „Person bearbeiten“ – Beispiel]]

Der bevorzugte oder Standardname ist der Name, der in Gramps als '[Name](wiki:De:Namen_in_Gramps)' der Person verwendet wird. Du kannst in den [Gramps Einstellungen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Einstellungen#Anzeigeoptionen) einstellen, wie ein Name angezeigt wird, und im Allgemeinen musst du nur Daten in Felder eingeben, die im Abschnitt "Bevorzugter Name" angezeigt werden.

Einige ausführliche Berichte (Texte und erzählender Webseitengenerator) zeigen auch die alternativen Namen. Beachte die Suche nach einem Namen sucht trotzdem in allen Namen einer Person nicht nur in dem bevorzugten Namen.

Der Abschnitt mit den bevorzugten Namen enthält die typischen Namensinformationen, die du beim Erstellen einer Person bearbeitest. Um die Unordnung zu verringern, werden die weniger häufig benötigten Felder (für [mehrere Nachnamen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Daten_eingeben_und_bearbeiten:_Ausführlich_-_Teil_1#Mehrere_Nachnamen) und [alternative Namen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Daten_eingeben_und_bearbeiten:_Ausführlich_-_Teil_1#Namen)) standardmäßig ausgeblendet. Um den Abschnitt für mehrere Nachnamen zu erweitern, klicke auf die   Schaltfläche oder verwende die [Tastenkombination](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Tastenkürzel_Referenz#Editor_Einbindung). Bei Mehrfachnamen kann ein Verbindungselement (z. B. ein Bindestrich oder ein [Geschütztes Leerzeichen](https://de.wikipedia.org/wiki/Gesch%C3%BCtztes_Leerzeichen)) angegeben werden, um eine Brücke zwischen den Nachnamen zu schlagen und so zusammengesetzte (auch als "[Doppelnamen](https://de.wikipedia.org/wiki/Doppelname_(Nachname))" bezeichnete) Nachnamen zu erstellen. Um den gesamten Datenbereich anzuzeigen, den du zu einem Namen speichern kannst, klicke auf die   Schaltfläche in der unteren rechten Ecke des Abschnitts oder verwende dessen [Tastenkombination](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Tastenkürzel_Referenz#Editor_Einbindung). Dies öffnet den [Namenseditor](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Daten_eingeben_und_bearbeiten:_Ausführlich_-_Teil_3#Namenseditor).

Die Namensfelder des bevorzugten Namens im sind:

- des Namens. Zu den vordefinierten Typen gehören: Auch bekannt als, **Geburtsname** *(Vorgabe)*, Name nach der Hochzeit, Unbekannt. Du kannst auch in dieses Eingabefeld eingeben, um deinen eigenen [benutzerdefinierten Typen](wiki:De:Gramps_Glossar#benutzerdefiniert) zu erstellen (z. B. Spitzname, Kurzname usw.).

  
Es wird geraten als bevorzugten Namen einen rechtlich gültigen Namen zu verwenden, da dieser meistens in Dokumenten gefunden wird und speichere andere Namensformen im Reiter des .

- , der Vorname der Person

- , ein optionaler Suffix zu dem Namen wie z.B. *Sen.* oder *III.*

- , der Teil des Namens einer Person, der die Familie anzeigt, zu der sie gehört-

  - Wenn du auf die Schaltfläche   klickst, wird das Eingabefeld für den Abschnitt angezeigt, in dem du zusammengesetzte Nachnamen eingeben kannst (z.B. für Patronymie oder zusammengesetzte matrilineare-patriliniale Namen).

- , ein optionaler Präfix für den Familiennamen, der bei der Sortierung nicht verwendet wird wie z.B. *de*, *van* oder *von*

- , der [Ursprungstyp](wiki:De:Gramps_Glossar#Namensherkunft) des Namens gibt das kulturelle Benennungssystem an, das angibt, wie ein bestimmter Familienname gewählt wurde. Dies sind Metainformationen über den Nachnamen, die für die genealogische Forschung wichtig sein können.

- , ist ein Titel der verwendet wird, um sich auf die Person zu beziehen wie z.B. *Dr.* oder *Rev.*

- ist ein beschreibender Name der an Stelle oder Zusätzlich zum offiziellen Vornamen gegeben wurde. Wenn ein Spitzname ein vollständiges Namenskonstrukt ist, verwende anstelle des Spitznamen-Felds einen bestimmten Namenstyp **Auch bekannt als**.

- , offiziell ist dies der Teil des Vornamen, der normalerweise verwendet wird. Z.B. kann eine Person drei Namen haben wie bei *Johann Wilhelm Karl* wovon in Wirklichkeit nur *Karl* verwendet wird. In Deutschland und in einigen anderen Gegenden, war es üblich den Rufnamen zwischen den anderen Vornamen zu unterstreichen, siehe auch [hier](wiki:De:Namen_in_Gramps#Rufname). Einige Personen möchten dieses Feld auch für Spitznamen oder Änderungen des Vornamens (wie Bibi für Sabine) verwenden, dies ist aber nicht der offizielle Gebrauch. Ein Rufname ist ein rechtsgültiger Name. Für Spitznamen oder Kurznamenvarianten solltest du einen alternativen Namen mit einem anderen Typ erstellen.

In dem [Nameneditor](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Daten_eingeben_und_bearbeiten:_Ausführlich_-_Teil_3#Nameneditor) steht ein zusätzliches Feld zur Verfügung: . Dies ist ein nicht offizieller Name, der Familien gegeben wurde um sie von anderen Personen mit dem selben Familiennamen zu unterscheiden. Wird oft als Hofname bezeichnet und verweist normalerweise auf einen Ort, an dem sich die Splittergruppe befindet oder ihren Ursprung hat. (alias Sept, Sekte, Lager)

Die und Felder bieten "[Autovervollständigung](https://de.wikipedia.org/wiki/Autovervollst%C3%A4ndigung)" Funktion: wenn du etwas in diese Felder eingibst, erscheint ein Menü unter dem Feld es enthält Einträge aus der Datenbank die mit deiner Teileingabe übereinstimmen. Dies gibt dir die Möglichkeit als Abkürzung einen Namen aus der Datenbank zu wählen anstatt ihn komplett einzugeben. Du kannst den Eintrag durch Verwendung der Maus oder der Pfeil und Tasten wählen.

Die Suche in der Vielzahl der Namensfelder kann breit gefächert oder präzise ausgerichtet sein. Verwende das Feld Name im [Filter](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Gramplets#Personenfilter) Gramplet der Kategorie Personen, um alle Felder gleichzeitig zu durchsuchen. Oder verwende die Regel [Personen mit &lt;Name&gt;](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Filter#Personen_mit_dem_.3CNamen.3E), um einen benutzerdefinierten Filter zu erstellen, der jedes Element einzeln durchsucht.

{{-}}

### Mehrere Nachnamen

![[_media/EditPerson-MultipleSurnames-entry-section-default-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Abschnitt „Mehrere Nachnamen“ im Dialogfeld „Person bearbeiten“ – Standard]]

![[_media/Edit-person-window-existing-person-example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Abschnitt „Mehrere Nachnamen“ im Dialogfeld „Person bearbeiten“ - Beispiel]]

Wenn die Schaltfläche Hinzufügen (Mehrere Nachnamen verwenden) ganz rechts in der Zeile im Fenster gedrückt wird, wird ein neues Eingabefeld für den Abschnitt angezeigt, in das zusammengesetzte Nachnamen eingegeben werden können. Alternativ kann die [Tastenkombination Editor der Schaltfläche Hinzufügen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Tastenkürzel_Referenz#Editor_Einbindung) verwendet werden.

Du kannst die anpassen: im Dialogfeld . Registerkarte , Abschnitt „Umgebungseinstellungen“.

Die [Funktion Mehrere Nachnamen](https://gramps-project.org/blog/2010/11/final-multiple-surnames/) kann für Patronym- oder zusammengesetzte matrilineal-patriliniale Namen verwendet werden. Eine andere Variante wäre ein skandinavischer Name wie "Syver Ericksen Skotterud", bei dem der vollständige Name aus einem Vornamen (Syver), einem Verweis auf seinen Vater (Ericksen oder Sohn von Erick) zusammen mit einem Dorf- oder Ortsnamen besteht. In einem solchen Fall können Sie "Ericksen" mit einem [Ursprung](wiki:Names_in_Gramps#Origin_Attributes) von "Patronym" hinzufügen und zu mehreren Nachnamen erweitern, indem du "Skotterud" mit einem Ursprung von "Ort" hinzufügst.

Wenn du in diesem Abschnitt keine Informationen hinzufügst, werden diese beim nächsten Öffnen des Dialogfelds "Person bearbeiten" ausgeblendet. Leere Zeilen werden nicht gespeichert.

Siehe auch:

- [Funktion für mehrere Nachnamen](https://gramps-project.org/blog/2010/11/final-multiple-surnames/) - Einführung Blogbeitrag auf der Gramps-Website.

{{-}}

#### Multiple Surnames section context menu

- \-

- \-

- \-

{{-}}

### Allgemein Bereich

![[_media/EditPerson-General-section-example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Abschnitt "Allgemein" des "Person bearbeiten" - Dialog - Beispiel]]

Im Bereich Allgemein kannst du die folgenden Optionen ändern:

- [Datenschutz](#Datenschutz)
- [Geschlecht](#Geschlecht)
- [ID](#ID)
- [Etiketten](#Etiketten).

#### Datenschutz

- Der Datenschutz Mit dem Vorhängeschloss-Symbol kannst du festlegen, ob der Datensatz der Person als öffentlich oder vertraulich gilt.

Datensätze werden standardmäßig mit einem ![[_media/22x22-gramps-unlock.png]]offenen Vorhängeschloss angezeigt, wenn sie öffentlich sind, und mit einem ![[_media/22x22-gramps-lock.png]]geschlossenen Vorhängeschloss, wenn sie vertraulich sind. Durch Klicken auf das Vorhängeschloss-Symbol kannst du zwischen den Optionen „Öffentlich“ und „Vertraulich“ wechseln.

{{-}}

#### Geschlecht

- Das Menü bietet die Wahl des Geschlechts der Person :
  - *weiblich*
  - *männlich*
  - **unbekannt** (Standardeinstellung)
  - *andere*

Wenn das Geschlecht als angegeben wird, wird das Dialogfeld angezeigt.

Siehe[Geschlechtsstatistik neu erstellen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Werkzeuge#Geschlechtsstatistik_neu_erstellen) Werkzeug und [Geschlechtsstatistik verwerfen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Werkzeuge#Geschlechtsstatistik_verwerfen) Fehlersuche.

##### Unbekanntes Geschlecht angegeben Dialog

![[_media/Unknown-gender-specified-dialog-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Unbekanntes Geschlecht angegeben" Dialog]]

Der Dialog weist dich darauf hin, dass das Geschlecht der Person derzeit unbekannt ist. In der Regel handelt es sich hierbei um einen Fehler. Bitte gib das Geschlecht an, indem du , , oder auswählst, um zu bestätigen. {{-}}

#### ID

- Das Feld zeigt die [Gramps ID](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Einstellungen#ID-Formate) Nummer welche die Person in der Datenbank identifiziert. Dieser Wert hilft Personen mit dem selben Namen zu unterscheiden. Es kann jeder eindeutige Wert eingegeben werden. Wenn du keinen Wert angibst, wählt Gramps automatisch einen Wert für dich aus, oder die Vorlage für die Erstellung von IDs kann in ein geeignetes Format geändert werden.
  - Verwende um zu navigieren.

#### Etiketten

- Die liste ermöglicht dir eigene Markierungen und Grundinformationen über den Status deiner Erforschung festzulegen.
  - Über die Schaltfläche wird die Dialogfeldliste angezeigt, in der du vorhandene benutzerdefinierte Markierungen entfernen oder zuweisen kannst.

{{-}}

### Registerkarten Person bearbeiten

Die Registerkarten spiegeln die folgenden Kategorien personenbezogener Daten wider:

- (Standard)

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

#### Ereignisse

![[_media/EditPerson-Events-tab-example-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Registerkarte "Ereignisse" unter "Person bearbeiten" - Dialog - Beispiel]]

  
Der Reiter ermöglicht die Ereignisse für diese Person anzusehen und zu bearbeiten. Der untere Teil des Fensters listet alle Ereignisse dieser Person aus der Datenbank und zeigt die folgenden Spalten: `Art, Beschreibung, Datum, Ort, Hauptbeteiligte, Private(Schlosssymbol), Rolle, ID, Alter`. Der obere Teil zeigt die Details des aktuell ausgewählten Ereignisses in der Liste (falls vorhanden).. Die Schaltflächen , und erlauben das hinzufügen, bearbeiten und entfernen von Ereignisdatensätzen von der Datenbank. Beachte das die und Schaltflächen nur verfügbar sind, wenn ein Ereignis aus der Liste gewählt ist. Mit den Schaltflächen „^“ (nach oben) und „v“ (nach unten) kannst du das ausgewählte Ereignis nach oben/unten verschieben oder die Reihenfolge der Familie in der ausgewählten Zeile ändern; für Familienbeziehungen kannst du auch das Dialogfeld

##### Ereignis wählen Auswahl

![[_media/SelectEvent-selector-dialog-example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Ereignis wählen - Auswahl - Beispiel]]

Im Dialogfeld Auswahl kannst du eine Verknüpfung zu einem bereits vorhandenen Ereignis herstellen. Nach der Auswahl wird es im Dialogfeld geöffnet.

Die folgenden Spalten werden angezeigt: `Art` (Standardsortierung für Liste), `Hauptbeteiligte`, `Datum`, `Ort`, `Beschreibung`, `ID`, `Letzte Änderung`.

Du kannst die Schaltfläche verwenden, um die Liste basierend auf einer der Optionen aus der Drop-down-Liste zu filtern:

- **Art enthält** (Standardeinstellung)
- *Art enthält nicht*
- *Hauptbeteiligte enthält*
- *Hauptbeteiligte enthält nicht*
- *Datum enthält*
- *Datum enthält nicht*
- *Ort enthält*
- *Ort enthält nicht*
- *Beschreibung enthält*
- *Beschreibung enthält nicht*
- *ID enthält*
- *ID enthält nicht*
- *Letzte Änderung enthält*
- *Letzte Änderung enthält nicht*

Verwende die Schaltfläche , um den Filter zurückzusetzen. {{-}}

#### Namen

![[_media/EditPerson-Names-tab-example-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Registerkarte "Namen" aus dem Dialog "Person bearbeiten" - Dialog - Beispiel]]

  
Auf der Registerkarte kannst du alle alternativen Namen, die die Person hat, anzeigen und bearbeiten. Der oben im Dialogfeld [Person bearbeiten](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Daten_eingeben_und_bearbeiten:_Ausführlich_-_Teil_1#Informationen_.C3.BCber_Personen_bearbeiten) angezeigte Name ist der bevorzugte Name und in der Regel (aber nicht unbedingt) der Geburtsname. können andere [Namensarten](wiki:De:Namen_in_Gramps#Namensarten) für Aliasnamen ("Auch bekannt als"), Adoptivnamen, Pennamen, Künstlernamen oder rechtliche Namensänderungen sein. (Weil dies so häufig vorkommt, gibt es einen separaten Alias-Namenstyp für "Ehename"). Wenn alternative Namen existieren, können für jeden Namen Datumsbereiche festgelegt werden. So kann ein "Geburtsname" einen Bereich verwenden (vor dem Datum der Adoption) und ein "Auch bekannt als" einen anderen Bereich (nach dem Datum der Adoption). Alternative Namen können auch Schreibvarianten sein, einschließlich anglisierter Versionen des Geburtsnamens und gängiger Schreibfehler.

<!-- -->

  
Im unteren Teil des Fensters werden alle in der Datenbank gespeicherten alternativen Namen für die Person aufgelistet. Im oberen Teil werden die Details des aktuell in der Liste ausgewählten Namens angezeigt (falls vorhanden). Die Schaltflächen (Hinzufügen), (Bearbeiten) und (Entfernen) ermöglichen das Hinzufügen, Ändern und Entfernen eines alternativen Namens aus der Datenbank. Ein Doppelklick auf eine Zeile entspricht dem Auswählen und Klicken auf die Schaltfläche (Bearbeiten). Beachte, dass die Schaltflächen und nur verfügbar sind, wenn ein alternativer Name in der Liste ausgewählt ist.

<!-- -->

  
Jede Zeile in der Liste der alternativen Namen kann über das Kontextmenü auf den bevorzugten Namen gesetzt werden. Klicke mit der rechten Maustaste auf den alternativen Namen und wähle die Menüoption . Die Zeile mit dem alternativen Namen wird in den Abschnitt Bevorzugter Name verschoben, und der vorherige bevorzugte Name wird an das Ende der Liste der alternativen Namen verschoben.

<!-- -->

  
Wenn du einen neuen Namen hinzufügen oder einen existierenden Namen bearbeitest, wird der Dialog geöffnet. Dieser Dialog wird im [Nameneditorabschnitt](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Daten_eingeben_und_bearbeiten:_Ausführlich_-_Teil_3#Nameneditor) beschrieben.

{{-}}

#### Quellen Fundstellen

![[_media/EditPerson-SourceCitations-tab-example-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Registerkarte "Quellzitate" aus dem Dialog "Person bearbeiten" - Dialog - Beispiel]]

  
Der Reiter erlaubt das Ansehen und Dokumentieren der Quellen Fundstellen für die gesammelten Informationen.

<!-- -->

  
Das können allgemeine Quellen sein die kein spezielles Ereignis beschreiben aber trotzdem Informationen über die Person enthalten. Zum Beispiel Tante Martha erwähnt ihren Ur-Enkel Paul,der Forscher kann annehmen das dieser Paul existiert und zitiert Tante Martha als Quelle die diese Annahme begründet.

  
Der zentrale Bereich zeigt eine Liste aller Quellen aus der Datenbank für diese Person. Die Schaltflächen , , und erlauben entsprechend das Hinzufügen, Ändern und Entfernen einer Quellenreferenz zu dieser Person. Beachte das die und Schaltflächen nur verfügbar sind wen eine Quellen Referenz aus der Liste gewählt ist.

<!-- -->

  
Während des Bearbeitens kannst du die Daten in der Fundstelle ändern (nur für diese Person), genauso wie die gemeinsam verwendeten des Quellenobjekts, siehe [Fundstellen bearbeiten](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Daten_eingeben_und_bearbeiten:_Ausführlich_-_Teil_2#Quellenfundstellen_bearbeiten).

{{-}}

#### Attribute

![[_media/EditPerson-Attributes-tab-example-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Registerkarte "Attribute" aus dem Dialog "Person bearbeiten" - Dialog - Beispiel]]

  
Der Reiter erlaubt Attribute für die Person zu sehen oder hinzuzufügen. Es besteht völlige Freiheit in der Definition und Benutzung der Attribute. Z.B. können Attribute zugeordnet werden um persönliche körperliche und charakteristische Eigenschaften zu beschreiben.

<!-- -->

  
Beachte das jedes Attribut das Dialog gelistet ist besteht aus zwei Teilen: das Attribut selbst und ein Wert der mit diesem Attribut verknüpft ist. Dieses so genannte "Wertepaar" kann helfen deine Forschungen zu organisieren und zu systematisieren. Zum Beispiel, wenn du "Haarfarbe" als ein Attribut für eine Person definierst, wird "Haarfarbe" ein wählbares Attribut für alle anderen Personen. Der Wert von Haarfarbe für Person A könnte rot sein und für Person B braun. Auf die selbe Weise könntest du ein Attribut wie "Großzügigkeit" definieren und den Wert "sehr" verwenden um eine besonders großzügige Person zu beschreiben.

<!-- -->

  
Der untere Bereich des Dialogfensters zeigt eine Liste aller Attribute aus der Datenbank. Die Schaltflächen , , und ermöglichen das hinzufügen, ändern und modifizieren eines Attribute Datensatzes in der Datenbank. Beachte das die und Schaltflächen nur verfügbar sind wenn ein Attribut aus der Liste gewählt ist.

Wenn du ein Attribut bearbeitest, wird der geöffnet.

{{-}}

#### Adressen

![[_media/EditPerson-Addresses-tab-example-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Registerkarte "Adressen" aus dem "Person bearbeiten" - Dialog - Beispiel]]

  
Der Reiter erlaubt das ansehen und eingeben der verschiedenen Postadressen der Person. Es wird geraten Informationen über die Wohnorte einer Person in Wohnortsereignissen zu speichern. Der Adressreiter besteht hauptsächlich wegen Kompatibilitätsgründen zum GEDCOM-Standard dort werden Adressen ausschließlich für die Post verwendet.

<!-- -->

  
Im unteren Teil des Fensters werden Adressen aufgelistet, die für diese Person in der Datenbank gespeichert sind. Der obere Teil zeigt die Details der aktuell ausgewählten Adresse in der Liste (falls vorhanden). Die Schaltflächen , , und ermöglichen das hinzufügen, ändern und modifizieren eines Adressen Datensatzes in der Datenbank. Beachte das die und Schaltflächen nur verfügbar sind wen eine Adresse aus der Liste gewählt ist.

  
Wenn du eine Adresse bearbeitest, wird der geöffnet.

<!-- -->

  
Einige Berichte erlauben die Daten von lebenden Personen zu begrenzen. Im speziellen werden bei diese Option die Adressen nicht ausgegeben.

{{-}}

#### Notizen

![[_media/EditPerson-Notes-tab-example-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Registerkarte "Notizen" aus dem "Person bearbeiten" - Dialog - Beispiel]]

  
Der Reiter ist ein Platz um verschiedene Einzelheiten über eine Person aufzuzeichnen, die nicht wirklich in andere Kategorien passen, genauso wie Textauszüge, die du dem Stammbaum hinzufügen willst. Du kannst Notizen zwischen verschiedenen Datensätzen in Gramps teilen. Die Symbolleiste auf dieser Reiterseite bietet die üblichen Schaltflächen: , , , und Schaltflächen um die Reihenfolge der Notizen zu ändern.

<!-- -->

  
Wenn du eine Notiz bearbeitest, wird der geöffnet.

{{-}}

##### Notiz wählen Auswahl

![[_media/SelectNote-selector-dialog-example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Notiz wählen - Auswahl - Beispiel]]

Im Dialogfeld Auswahl kannst du eine Verknüpfung zu einer bereits vorhandenen Notiz herstellen.

Die folgenden Spalten werden angezeigt: `Vorschau` (Standardsortierung für Liste), `ID`, `Art`, `Etiketten`, `Letzte Änderung`.

Du kannst die Schaltfläche verwenden, um die Liste basierend auf einer der Optionen aus der Drop-down-Liste zu filtern:

- **Vorschau enthält** (Standardeinstellung)
- *Vorschau enthält nicht*
- *ID enthält*
- *ID enthält nicht*
- *Art enthält*
- *Art enthält nicht*
- *Markierung enthält*
- *Markierung enthält nicht*
- *Letzte Änderung enthält*
- *Letzte Änderung enthält nicht*

{{-}}

#### Galerie

![[_media/EditPerson-Gallery-tab-example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Registerkarte "Galerie" aus dem "Person bearbeiten" - Dialog - Beispiel]]

  
Der Reiter erlaubt das Ansehen und Speichern von Fotos, Videos und anderen Medienobjekten die mit dieser Person in Verbindung stehen. Der zentrale Bereich des Fensters listet all diese Medienobjekte. Für jedes Objekt in Form einer Bilddatei wird ein Vorschaubild angezeigt. Für andere Objekte wie Audiodateien, Filmdateien usw. wird stattdessen ein passendes Symbol für den Dateityp angezeigt.

<!-- -->

  
Folgende Optionen stehen zur Verfügung:

- \- ermöglicht dir im ein neues Medienobjekt hinzuzufügen.

- \- öffnet das Dialogfeld , in dem du eine Verknüpfung zu einem bereits vorhandenen Medienobjekt herstellen kannst.

- \- ermöglicht dir das ausgewählte Medienobjekt im zu ändern. Diese Schaltfläche wird nur verfügbar, wenn ein Medienobjekt aus der Liste ausgewählt wird.

- \- entfernt das ausgewählte Medienobjekt aus der Galerie der Person. Diese Schaltfläche wird nur verfügbar, wenn ein Medienobjekt aus der Liste ausgewählt wird.

- Mit den Schaltflächen (Pfeil nach links) und (Pfeil nach rechts) kannst du die Medienelemente neu anordnen, um ein bestimmtes Bild als Hauptbild auszuwählen. Du kannst auch die Reihenfolge des primären (aktiven) Bildes ändern, indem du das Bild auswählst und es an die erste Position ziehst.

{{-}}

###### Kontextmenü der Galerie

![[_media/EditPerson-Gallery-tab-example-with-context-menu-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Registerkarte „Galerie“ aus „Person bearbeiten“ – Dialogfeld – Beispiel mit Kontextmenü]] Wenn du in der Galerie ein Medienobjekt auswählst, steht ein Kontextmenü (Rechtsklick) mit folgenden Optionen zur Verfügung:

- 

- 

<hr>

- 

<hr>

- 

- 

- 

- 

##### Medien Objekt wählen Auswahl

![[_media/SelectMediaObject-selector-dialog-example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Medienobjekt auswählen – Auswahlfeld – Beispiel mit mehreren Auswahlen]]

Im Dialogfeld kannst du eine Verknüpfung zu einem bereits vorhandenen Medienobjekt herstellen. Sobald das Bild ausgewählt ist, wird es im Dialogfeld geöffnet.

Sobald du ein Medienobjekt aus der Liste ausgewählt hast, wird nach Möglichkeit im oberen Bereich eine Vorschau angezeigt.

Die folgenden Spalten werden angezeigt: `Titel` (Standardsortierung für Liste), `ID`, `Art`, `Letzte Änderung`.

Du kannst die Schaltfläche verwenden, um die Liste basierend auf einer der Optionen aus der Dropdown-Liste zu filtern:

- **Title enthält** (Standardeinstellung)
- *Title enthält nicht*
- *ID enthält*
- *ID enthält nicht*
- *Art enthält*
- *Art enthält nicht*
- *Letzte Änderung enthält*
- *Letzte Änderung enthält nicht*

Siehe auch [Wähle ein Medienobjekt](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Daten_eingeben_und_bearbeiten:_Ausführlich_-_Teil_2#Medienobjekt_w.C3.A4hlen_Auswahl) Dateiauswahldialog.

{{-}}

#### Internet

![[_media/EditPerson-Internet-tab-example-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Registerkarte "Internet" aus "Person bearbeiten" - Dialog - Beispiel]]

  
Der Reiter zeigt die für diese [Person](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Daten_eingeben_und_bearbeiten:_Ausführlich_-_Teil_1#Internet), [Ort](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Daten_eingeben_und_bearbeiten:_Ausführlich_-_Teil_2#Internet), oder [Aufbewahrungsort](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Daten_eingeben_und_bearbeiten:_Ausführlich_-_Teil_2#Internet_2) relevanten Internetadressen. Ein beschreibender Titel der Internetadresse die du speicherst. Art der Internetadresse wie sie zum navigieren benötigt wird, z.B.. <http://gramps-project.org>, E-Mail, Webseite, ...

<!-- -->

  
Im unteren Teil werden alle Internetadressen und die zugehörigen Beschreibungen aufgelistet. Der obere Teil zeigt die Details der aktuell ausgewählten Adressen in der Liste (falls vorhanden). Die Schaltflächen , öffnen den zum Hinzufügen oder Bearbeiten und die Schaltfläche entfernt die ausgewählte Internetadresse. Die Schaltfläche öffnet Ihren Webbrowser und führt Sie direkt zu der markierten Seite.

Beachte das die , und Schaltflächen nur verfügbar sind, wenn eine Adresse aus der Liste gewählt ist. {{-}}

##### Internetadresseneditor

![[_media/InternetAddressEditor-dialog-default-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Internetadresseneditor" - Dialog - Vorgabe]]

Im Dialogfeld kannst du eine neue Internetadresse hinzufügen oder die ausgewählte Internetadresse ändern.

- Art der Internetadresse:

  - *E-Mail*
  - **Unbekannt** <small>(Standardeinstellung)</small>
  - *FTP*
  - *Homepage*
  - *Websuche*
  - Jeder benutzerdefinierte Typ, den du manuell eingibst.

- schaltet den Datenschutzstatus des Datensatzes um.

- Die Internetadresse, die zum Navigieren benötigt wird, z.B.: <https://gramps-project.org>

  - Öffnet die Webadresse im Standardbrowser

- Eine beschreibende Beschriftung des Internet-Standorts, den du speicherst.

Siehe auch

- [Verknüpfungseditor](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Daten_eingeben_und_bearbeiten:_Ausführlich_-_Teil_2#Verkn.C3.BCpfungeditor)
- [Notizverknüpfungenbericht](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte_-_Teil_6#Notizverkn.C3.BCpfungenbericht)
- Suche nach der Internetadresse einer Person ( Art, Webadresse oder Beschreibung) mit der benutzerdefinierten Filterregel [Personen, deren Aufzeichnungen die <Zeichenfolge> enthalten](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Filter#Personen.2C_deren_Aufzeichnungen_die_.3CZeichenfolge.3E_enthalten)
- Suche nach der Internetadresse eines Aufbewahrungsorte( Art, Webadresse oder Beschreibung) mit der benutzerdefinierten Filterregel [Aufbewahrungsorte entsprechend Parametern](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Filter#Aufbewahrungsorte_entsprechend_Parametern)

{{-}}

#### Verknüpfungen

![[_media/EditPerson-Associations-tab-example-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Registerkarte "Verknüpfungen" aus dem "Person bearbeiten" - Dialog - Beispiel]]

Auf der Registerkarte kannst du Beziehungsrolleninformationen zu zwei Personen, die in der Datenbank explizit verknüpft sind, anzeigen und bearbeiten.

Bei den Verknüpfungen handelt es sich in der Regel um Rollen, die sich nicht aus der Verbindung in einer normalen (oder gemischten) Familienstruktur oder durch gemeinsame Ereignisrollen ableiten lassen. Cousin- oder Geschwisterbeziehungen werden beispielsweise durch die Art und Weise deutlich, wie Ehen die Personen miteinander verbinden. Beziehungen wie Paten (Teilnehmer an einer Taufe), Organspender (Teilnehmer an einem medizinischen Eingriff), Sargträger (Teilnehmer an einer Beerdigung) und Vormund (Teilnehmer an einem Nachlass oder in einem Testament erwähnt) können Rollen sein, die durch die Teilnahme an einem Ereignis entstehen, das für die Person mit der Hauptrolle geschaffen wurde.

Verknüpfungsrollen sind also weniger offensichtlich. Dabei kann es sich um Freunde der Familie, einen Namensgeber (die Person, die von einem Namensvetter geehrt wird), einen Kollegen, einen Brieffreund oder jede andere Art von Verbindung handeln, die du aufzeichnen möchtest. Wenn die engste Beziehung "Pate" ist, bedeutet dies, dass der Pate der (zu bearbeitenden) Person die Person ist, deren Name auf der Registerkarte "Verknüpfungen" angezeigt wird.

Das [ASSO-Tag (Associates) im GEDCOM-Standard](http://wiki-de.genealogy.net/GEDCOM/ASSO-Tag) besagt, dass "die Beziehung oder Verbindung einer Person die Person ist, auf die verwiesen wird". Du kannst eine wechselseitige Zuordnung auf der Registerkarte Verbindungen dieser anderen Person einfügen.

In der von [example.gramps](wiki:Example.gramps) gezeigten Verbindung ist Lewis Garners Pate Anderson Garner. Verwende stattdessen Ereignisse für Beziehungen, die mit bestimmten Zeitrahmen oder Anlässen verbunden sind. Ereignisse können zwischen Personen geteilt werden, wobei jede ihre [Rolle](wiki:De:Gramps_Glossar#Rolle) in dem Ereignis angibt.

Die Schaltfläche öffnet das Dialogfeld zum Hinzufügen. Mit der Schaltfläche kannst du bearbeiten und mit wird die ausgewählte Verbindung entfernt. Die anderen Schaltflächen oder . Verschiebst du nur die ausgewählte Eintragsposition in der Liste.

Siehe auch:

- [Rollen, Beziehungen und Verbindungen](wiki:Roles,_Relationships_&amp;_Associations) (englisch)
- [Taufpaten hinzufügen](wiki:De:Taufpaten_hinzufügen) ***Anmerkung:*** In der Version 5.2 von Gramps wurde die Standardliste der Ereignisrollen um die Rolle "Paten" erweitert.

{{-}}

##### Personenreferenzeditor

![[_media/PersonReferenceEditor-dialog-default-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Personenreferenzeditor" - Dialog - Standard]]

Mit dem kannst du Zuordnungseinträge hinzufügen und bearbeiten. Du kannst über die Registerkarte des Dialogfelds darauf zugreifen.

- *Um eine Person auszuwählen, verwende Drag-and-Drop oder die Schaltflächen.*

  - Schaltfläche öffnet das Dialogfeld Auswahl.

  - \- Eine neue Person hinzufügen

- Du kannst den Standardeintrag mit einem beliebigen Begriff deiner Wahl überschreiben, z. B. „Freund”, „Nachbar”.

  - **Pate** (Vorgabe)

  - \- Datensatz ist öffentlich (Vorgabe)

{{-}}

###### Registerkarte Quellenangaben

  
Der Reiter erlaubt das Ansehen und Dokumentieren der Quellen Fundstellen für die gesammelten Informationen.

<!-- -->

  
Das können allgemeine Quellen sein die kein spezielles Ereignis beschreiben aber trotzdem Informationen über die Person enthalten. Zum Beispiel Tante Martha erwähnt ihren Ur-Enkel Paul,der Forscher kann annehmen das dieser Paul existiert und zitiert Tante Martha als Quelle die diese Annahme begründet.

  
Der zentrale Bereich zeigt eine Liste aller Quellen aus der Datenbank für diese Person. Die Schaltflächen , , und erlauben entsprechend das Hinzufügen, Ändern und Entfernen einer Quellenreferenz zu dieser Person. Beachte das die und Schaltflächen nur verfügbar sind wen eine Quellen Referenz aus der Liste gewählt ist.

<!-- -->

  
Während des Bearbeitens kannst du die Daten in der Fundstelle ändern (nur für diese Person), genauso wie die gemeinsam verwendeten des Quellenobjekts, siehe [Fundstellen bearbeiten](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Daten_eingeben_und_bearbeiten:_Ausführlich_-_Teil_2#Quellenfundstellen_bearbeiten).

{{-}}

###### Registerkarte Notizen

  
Auf der Registerkarte kannst du alle [Notizen](wiki:De:Gramps_Glossar#note) anzeigen und bearbeiten, die mit der Beziehung verbunden sind. Das können alle Kommentare sein, die nicht in die für Attribute verfügbaren „Parameter-Wert“-Paare passen. Um eine Notiz hinzuzufügen oder vorhandene Notizen zu ändern, bearbeite einfach den Text im Texteingabefeld.

Mit der Option kannst du festlegen, wie die Notiz in Berichten und Webseiten angezeigt wird. Wenn du „Fließend“ auswählst, werden im generierten Text alle Mehrfach-Leerzeichen, Tabulatoren und einzelnen Zeilenendezeichen durch einfache Leerzeichen ersetzt. Eine zwischen zwei Textblöcken eingefügte Leerzeile signalisiert einen neuen Absatz; zusätzlich eingefügte Zeilen werden ignoriert.

Wenn du die Option „Vorformatiert“ auswählst, wird der Text in Berichten und Webseiten genau so angezeigt, wie du ihn im Dialogfeld eingegeben hast.

{{-}}

###### Person wählen Auswahl

![[_media/SelectPerson-selector-dialog-example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Person wählen" - Auswahldialog - Beispiel]]

Das Dialogfeld ermöglicht es dir, eine Verbindung zu einer bereits vorhandenen Person herzustellen.

Wähle einen beliebigen Nachnamen aus, um ihn zu erweitern und die gewünschte Person zu finden, wähle sie aus und drücke . {{-}} Siehe auch:

- [Wähle eine Person für den Berichtsauswahlfilter aus.](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte_-_Teil_4#Eine_Person_f.C3.BCr_den_Bericht_w.C3.A4hlen_Auswahl)

#### HLT

![[_media/EditPerson-LDS-tab-example-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "HLT" Reiter vom "Person bearbeiten" - Dialog - Beispiel]]

Über die Registerkarte (Heilige der Letzten Tage) kannst du Infos zu den HLT-Ritualen der Person anzeigen und bearbeiten. Diese Infos kommen aus der GEDCOM-Spezifikation der HLT. Die HLT-Registerkarten im Familien- und Personen-Editor kannst du über das Kontrollkästchen ausblenden: Heilige der Letzten Tage im Abschnitt **** der Registerkarte unter ausblenden.

Oben auf der Registerkarte kannst du die folgenden Schaltflächen verwenden, um oder , um das Dialogfeld aufzurufen: und oder .

Die folgenden Spalten werden für die Liste angezeigt: `Quelle` (Symbol), `Vertraulich` (Schloss-Symbol), `Art`, `Datum`, `Status`, `Tempel`, `Ort`.

Siehe auch:

- Personeneditor Dialog Registerkarte
- Familieneditor Dialog Registerkarte - Zeigt nur Informationen über die HLT-Verordnung „An den Ehepartner gesiegelt“ an.
- Du kannst diese -Registerkarte ausblenden, indem du die entsprechende Option im Abschnitt Registerkarte **** änderst.

{{-}}

##### Kontextmenü der Registerkarte „HLT“

Über das Kontextmenü eines ausgewählten Eintrags kannst du:

- 

- 

- 

{{-}}

##### HLT-Verordnungseditor

![[_media/LDSOrdinanceEditor-dialog-default-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "HLT-Verordnungseditor" - Dialog - Standard]]

Verwende das Dialogfeld , um vorhandene HLT-Verordnungen für die Person hinzuzufügen oder zu bearbeiten.

Diese HLT- gelten für:

- **Taufe** (Standard)
- *Begabung*
- *Konfirmation*
- *An die Eltern gesiegelt*

Jede Verordnung wird durch ihren , , und sowie einen zusätzlichen Eintrag für beschrieben, der nur für die Verordnung „An die Eltern gesiegelt“ angezeigt wird.

Jede Verordnung kann durch die Auswahlmöglichkeiten in den Dropdown-Optionen unter näher beschrieben werden:

- **<Kein Status>** (Standard)
- *Im Bund geboren*
- *Geklärt*
- *Abgeschlossen*
- *Nicht siegeln*
- *Vor 1970*
- *Qualifiziert*
- *Tot geboren*
- *Eingereicht*
- *Ungeklärt*

Im unteren Bereich kannst du auch Quellenangaben und Notizen einfügen:

- [Registerkarte Quellenangaben](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Daten_eingeben_und_bearbeiten:_Ausführlich_-_Teil_1#Registerkarte_Quellenangaben_2)
- [Registerkarte Notizen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Daten_eingeben_und_bearbeiten:_Ausführlich_-_Teil_1#Registerkarte_Notizen_2)

Siehe auch:

- [De:Gramps_6.0_Wiki_Handbuch_-_Daten_eingeben_und_bearbeiten:_Ausführlich_-_Teil_1#HLT_2](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Daten_eingeben_und_bearbeiten:_Ausführlich_-_Teil_1#HLT_2)
- [Ordinance (Latter Day Saints)](https://wikipedia.org/wiki/Ordinance_(Latter_Day_Saints)) auf [Wikipedia](https://de.wiktionary.org/wiki/Wikipedia)).

{{-}}

###### Registerkarte Quellenangaben

{{-}}

###### Registerkarte Notizen

{{-}}

#### Referenzen

![[_media/EditPerson-References-tab-example-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Referenzen" Reiter vom "Person bearbeiten" - Dialog - Beispiel]]

Die Registerkarte listet andere Objekte auf, die explizit mit der Person verknüpft sind: Familien, in denen die Person ein Ehepartner oder Kind ist, Personen, die eine Assoziation haben, und Notizen, mit denen die Person verknüpft wurde.

Es werden keine sekundären verknüpften Objekte aufgelistet: Objekte (wie Ereignisse, Fundstellen, Medien, Orte, Etiketten), die mit einer Person verknüpft sind.

Ein Doppelklick auf eine Zeile in den Referenzen öffnet den Editor für das betreffende Objekt. {{-}}

## Informationen über Beziehungen bearbeiten

Informationen über Beziehungen werden eingegeben und bearbeitet im Dialog.

Dieser Dialog kann auf verschiedenen Wegen aufgerufen werden:

- Aus dem Menü : wähle oder verwende die [Tastenkombination](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Tastenkürzel_Referenz#xx).
- Von der [Beziehungenkategorie](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Kategorien#Beziehungenkategorie): Klicke auf die Schaltfläche in der Familie die du bearbeiten willst., oder .

<!-- -->

- Von der [Familienkategorie](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Kategorien#Familienkategorie): Wähle die Familie in der Liste und klicke dann auf die Schaltfläche in der Werkzeugleiste oder doppelklicke die Familie. Oder wähle im Menü die Option ....

<!-- -->

- Von der [Schaubilderkategorie](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Kategorien#Schaubilderkategorie): Bewege den Mauszeiger über die schwarze Verbindungslinie der Partner, klicke rechts und wähle aus dem Kontextmenü oder doppelklicke die schwarze Linie.

Jede dieser Methoden öffnet den folgenden Dialog:

{{-}}

### Familieneditordialog

![[_media/FamilyEditor-dialog-example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}}  Dialog] - Zeigt Beispielfamilie und Kontextmenü „Schnellansicht“ an]] Mit dem kannst du alle Aspekte einer Familie hinzufügen oder bearbeiten: die Personen (Kinder, Eltern), ihre Beziehungen zueinander, die Rollen, die sie bei Ereignissen spielen. Die Familienstruktur bietet den Kontext, den Gramps benötigt, um gelegentlich wahrscheinliche Nachnamen, Geschlechter, Rollen und Beziehungs- oder Ereignisarten zu erraten.

Bei Kindern, die einer Familie hinzugefügt werden, wird davon ausgegangen, dass sie leibliche Kinder der Eltern sind (biologisch mit ihnen verwandt) und einen von den Eltern erratenen Nachnamen erben. Dies kann jedoch manuell mit dem [Kindreferenzeditor](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Daten_eingeben_und_bearbeiten:_Ausführlich_-_Teil_1#Kindreferenzeditor) geändert werden. Dieser Editor erscheint, wenn ein Kind zu einer Familie hinzugefügt wird. Und er kann nachträglich durch einen Doppelklick auf ein Kind im [Familieneditor](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Daten_eingeben_und_bearbeiten:_Ausführlich_-_Teil_1#Familieneditordialog) zur Bearbeitung aufgerufen werden.

Ein Elternteil, der zu einer Familie hinzugefügt wird, hat ein aus der Rolle erratenes Geschlecht (Vater/Partner1 oder Mutter/Partner2) und möglicherweise einen Nachnamen.

Familienereignisse mit (der Standard-[Ereignisrolle](wiki:De:Gramps_Glossar#event_role) Familie) gelten für beide Ehegatten/Partner in einer Familie. Dadurch entfällt die Notwendigkeit, doppelte Ereignisse zu erstellen (und diese harmonisiert zu halten) oder ein Ereignis zwischen dem Vater/der Mutter (Partner1/Partner2) einer Familie zu teilen.

Familien haben [Standard-Beziehungsarten](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Einstellungen#Eingabeoptionen) und implizite [Ereignisrollen](wiki:De:Gramps_Glossar#event_role). Wenn Ereignisse im Familieneditor hinzugefügt werden, ist die Ereignisrolle standardmäßig die Rolle „Familie“. Das erste hinzugefügte Ereignis ist von der Art [Heirat](#Heirat) und das zweite von der Art [Scheidung](#Scheidung). Wenn Ereignisse gemeinsam genutzt werden, hat das Ereignis die Rolle „Unbekannt“ und muss auf die entsprechende Rolle eingestellt werden.

Der obere Bereich des Fensters zeigt die Namen der Personen, deren Verwandtschaftsverhältnisse bearbeitet werden, sowie deren Geburts- und Sterbedaten.

- - Die Schaltfläche öffnet das .
  - Die Schaltfläche öffnet das Dialogfeld .

- - Die Schaltfläche öffnet das .
  - Die Schaltfläche öffnet das Dialogfeld .

Mit der Schaltfläche kannst du festlegen, ob der Familieneintrag als öffentlich oder vertraulich gilt.

[Schnellansicht](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte_-_Teil_8#Schnellansichten) Berichte sind über das Kontextmenü (Rechtsklick) in einem leeren Bereich im oberen Bereich des Fensters verfügbar.

##### Kontextmenü des Familieneditors

Die folgenden [Schnellansicht](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte_-_Teil_8#Schnellansichten) Berichte sind über das Kontextmenü verfügbar:

- 

- 

#### Informationen über Beziehungen

Der Abschnitt enthält drei Felder mit einer grundlegenden Beschreibung der Beziehung.

- Das Feld zeigt die ID-Nummer an, mit der diese Beziehung in der Datenbank gekennzeichnet ist. Lass dieses Feld leer, damit Gramps eine eindeutige ID-Nummer generiert.

<!-- -->

- Zeigt eine Auswahlliste der verfügbaren Arten von Familienbeziehungen an, z. B. `Lebenspartnerschaft`, `Verheiratet`, **`Unbekannt`** (Standard), `Unverheiratet` usw. Du kannst auch einen [benutzerdefinierten Arten](wiki:De:Gramps_Glossar#custom) hinzufügen.

  - Du kannst auch die festlegen: - wird vom Familieneditor-Dialogfeld in verwendet.
  - [Wie stelle ich eine Scheidung dar?](wiki:Indicate_a_divorce)
  - Mit der Erweiterung [](wiki:Addon:FamilyRelationship) kannst du die Art der Familienbeziehung für eine ausgewählte Gruppe gefilterter Familien ändern.

<!-- -->

- Zeigt die [Etiketten](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Filter#Etikettierung) an, die du erstellt hast, um einige grundlegende Informationen zum Status deiner Forschung anzuzeigen. Du kannst zusätzliche Etiketten hinzufügen, indem du auf die Schaltfläche klickst.

Darunter werden mehrere [Notizbuchregisterkarten](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Daten_eingeben_und_bearbeiten:_Ausführlich_-_Teil_1#Familieneditor_Reiterseiten) angezeigt, die verschiedene Kategorien von Informationen über die Beziehung darstellen. Klicke auf eine beliebige Registerkarte, um die darin enthaltenen Informationen anzuzeigen oder zu bearbeiten.

Im unteren Teil des Fensters kannst du jederzeit auf die Schaltfläche klicken, um alle in allen Registerkarten vorgenommenen Änderungen zu übernehmen und das Dialogfenster zu schließen. Wenn du auf die Schaltfläche klickst, wird das Fenster geschlossen, ohne dass Änderungen übernommen werden. Wenn Daten in einer Registerkarte geändert werden, erscheint ein Warnfenster, in dem du zwischen dem Schließen des Dialogfelds ohne Speichern der Änderungen, dem Abbrechen der ursprünglichen Abbrech-Anforderung oder dem Speichern der Änderungen wählen kannst.

#### Vater wählen Auswahl

![[_media/SelectFather-selector-example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Vater wählen - Auswahl]] Das Dialogfeld ermöglicht es dir, eine Verbindung zu einer bereits vorhandenen Person als Vater herzustellen.

Du kannst entweder zu der Person blättern oder verwende die Schaltfläche

- ist: Der Selektor ist auf Personen mit männlichem Geschlecht gefiltert. Personen mit unbekanntem, anderem oder weiblichem Geschlecht werden nicht aufgelistet. Durch Auswahl der Schaltfläche und anschließendes Klicken auf wird diese Filterung deaktiviert.

{{-}}

#### Mutter wählen Auswahl

![[_media/SelectMother-selector-example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Mutter wählen - Auswahl]] Der Auswahldialog ermöglicht es dir, eine Verbindung zu einer bereits existierenden Person als Mutter herzustellen.

- ist: Der Selektor ist auf Personen mit weiblichem Geschlecht gefiltert. Personen mit unbekanntem, anderem oder männlichem Geschlecht werden nicht aufgelistet. Durch Auswahl der Schaltfläche und anschließendes Klicken auf wird diese Filterung deaktiviert.

{{-}}

### Familieneditor Reiterseiten

Die Reiter bieten folgende Beziehungsdaten Kategorien:

#### Kinder

![[_media/FamilyEditor-dialog-Children-tab-example-51-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Kinder" Reiter vom "Familieneditor" - Dialog - Beispiel]]

  
Der Reiter erlaubt dir das Ansehen und Bearbeiten der Liste der Kinder aus dieser Beziehung. Die Schaltfläche ermöglicht das Erstellen einer neuen Person in der Datenbank und das hinzufügen dieser Person als Kind zu dieser Beziehung. Die Schaltfläche lässt dich eine existierende Person auswählen und als Kind dieser Beziehung hinzufügen. Die Schaltfläche erlaubt das Bearbeiten der Beziehungen des gewählten Kindes und den Eltern. Abschließend lässt dich der das gewählte Kind von der Beziehung entfernen. Beachte, dass die und Schaltflächen nur verfügbar sind, wenn ein Kind aus der Liste gewählt ist.

[Wie ändere ich die Reihenfolge von Kindern?](wiki:De:Gramps_6.0_Wiki_Handbuch_-_FAQ#Wie_.C3.A4ndere_ich_die_Reihenfolge_von_Kindern.3F)

- Verwende diese Registerkarte [Kinder](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Daten_eingeben_und_bearbeiten:_Ausführlich_-_Teil_1#Kinder) im Familieneditor, um die Reihenfolge der Kinder in der aktiven Familie zu ändern.
- Verwende die Erweiterung Werkzeug eines Drittanbieters, das Massenaktualisierungen der Kinderreihenfolge ermöglicht.

Siehe auch:

- Das Gramplet [Kinder](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Gramplets#Kinder) in der [Personenkategorie](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Kategorien#Personenkategorie) zeigt alle Kinder aus **allen Ehen** der aktiven Person an. Die Kinder werden in der Reihenfolge angezeigt, in der sie in den Familiendatensätzen aufgeführt sind.

{{-}}

##### Kind wählen Auswahl

![[_media/SelectChild-selector-dialog-example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Kind wählen - Auswahl - Beispiel]]

Im Auswahl Dialog kannst du eine Verknüpfung zu einem bereits vorhandenen Kind herstellen. Nach der Auswahl wird es im geöffnet.

Die folgenden Spalten werden angezeigt: `Name` (Standardsortierung für Liste), `ID`, `Geschlecht`, `Geburtsdatum`, `Geburtsort`, `Sterbedatum`, `Sterbeort`, `Partner(in)`, `Letzte Änderung`. {{-}}

##### Kindreferenzeditor

![[_media/ChildReferenceEditor-dialog-example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} „Kinderreferenz-Editor“ – Beispiel]]

Der Dialog ermöglicht die Bearbeitung der Beziehung zwischen dem ausgewählten Kind und den Eltern in einer Familie. Der Dialog erscheint, wenn du eine Person als Nachkomme in eine Familie aufnimmst. Der letzte Schritt bei der Verwendung der Schaltfläche (zum Teilen), der Schaltfläche (eine neue Person erstellen) oder beim Hinzufügen einer Person zur Familie mittels "Drag and Drop" ist die Bestätigung der Beziehung.

Die Beziehungen können auch für bestehende Kinder im Dialogfeld "Familie bearbeiten" bearbeitet werden. Ein Doppelklick auf ein bestehendes Kind in einer Familie oder die Auswahl des Kontextmenüpunkts öffnet den Kindreferenzeditor für das ausgewählte Kind. (Durch Auswahl des Kontextmenüeintrags wird stattdessen der Dialog Person bearbeiten geöffnet).

Während eine Person nur in einer traditionellen Geburtsfamilie eine Geburtsbeziehung zu beiden Elternteilen hat, kann sie auch Teil mehrerer gemischter Familien sein. In diesen Familien heiratet ein leiblicher Elternteil erneut und der andere Ehepartner kann eine komplexere Beziehung zu den Kindern aus einer früheren Ehe haben. Da sie jedoch zum Haushalt gehören, sollten diese Kinder der neuen Familie mit der entsprechenden Beziehung hinzugefügt werden.

Folgende Optionen stehen zur Verfügung:

- Der Name des Kindes

  - Schaltfläche.

- Wähle aus der Dropdown-Liste mögliche Beziehungsarten aus:

  - *Adoptiert*
  - **Geburt** (Vorgabe)
  - *Pflegekind*
  - *Ohne*
  - *Patenschaft*
  - *Stiefkind*
  - *Unbekannt*

- Wähle aus der Dropdown-Liste mögliche Beziehungsarten aus:

  - *Adoptiert*
  - **Geburt** (Vorgabe)
  - *Pflegekind*
  - *Ohne*
  - *Patenschaft*
  - *Stiefkind*
  - *Unbekannt*

- Datenschutz für diese Beziehung umschalten.

{{-}} Außerdem sind die folgenden Registerkarten verfügbar:

- Quellenangaben
- Notizen

###### Quellenangabenreiter

  
Auf der Registerkarte kannst du die Quellenangaben für die von dir gesammelten Informationen anzeigen und dokumentieren.

<!-- -->

  
Dabei kann es sich um allgemeine Quellen handeln, die zwar kein bestimmtes Ereignis beschreiben, aber dennoch Informationen über die Person liefern. Wenn beispielsweise in den Memoiren von Tante Martha ihr Urenkel Paul erwähnt wird, kann der Forscher davon ausgehen, dass dieser Paul tatsächlich existiert hat, und die Memoiren von Tante Martha als Quelle für diese Annahme angeben.

  
Der mittlere Teil zeigt die Liste aller in der Datenbank gespeicherten Quellenangaben in Bezug auf die Person an. Mit den Schaltflächen , und kannst du entsprechend eine Quellenangabe zu dieser Person hinzufügen, ändern oder entfernen. Beachte, dass die Schaltflächen und nur verfügbar sind, wenn eine Quellenangabe aus der Liste ausgewählt ist.

<!-- -->

  
Beim Bearbeiten kannst du die Daten in der Quellenangabe (die für diese Person einzigartig ist) sowie das gemeinsame Quellobjekt ändern, siehe [Quellenangaben bearbeiten](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Daten_eingeben_und_bearbeiten:_Ausführlich_-_Teil_2#Quellenfundstellen_bearbeiten).

{{-}}

###### Notizenreiter

  
Auf der Registerkarte kannst du alle mit der Beziehung verbundenen [Notizen](wiki:De:Gramps_Glossar#note) anzeigen und bearbeiten. Dabei kann es sich um beliebige Kommentare handeln, die nicht in die für Attribute verfügbaren „Parameter-Wert“-Paare passen. Um eine Notiz hinzuzufügen oder vorhandene Notizen zu ändern, bearbeite einfach den Text im Texteingabefeld.

Mit der Option kannst du festlegen, wie die Notiz in Berichten und auf Webseiten angezeigt wird. Wenn du Fließend auswählst, werden im generierten Text alle Mehrfach-Leerzeichen, Tabulatoren und einzelnen Zeilenendezeichen durch einfache Leerzeichen ersetzt. Eine zwischen zwei Textblöcken eingefügte Leerzeile signalisiert einen neuen Absatz; zusätzlich eingefügte Zeilen werden ignoriert.

Wenn du die Option „Vorformatiert“ auswählst, wird der Text in Berichten und Webseiten genau so angezeigt, wie du ihn im Dialogfeld eingegeben hast.

{{-}}

#### Ereignisse

Der Reiter erlaubt dir das Ansehen und Bearbeiten der Liste der Ereignisse, die für die Beziehung relevant sind. Die Schaltflächen , und ermöglicht dir das Hinzufügen, Ändern oder Entfernen eines Ereignisdatensatzes von der Datenbank. Beachte, dass die und Schaltflächen nur verfügbar sind, wenn ein Ereignis aus der Liste gewählt ist.

{{-}}

#### Quellen Fundstellen

  
Der Reiter erlaubt dir das Ansehen und Bearbeiten einer Liste der Verweise auf Quellen, die Hinweise zu dieser Beziehung liefern. Dies können Dokumente sein, die sich auf die Beziehung beziehen, diese aber nicht unbedingt offiziell dokumentieren. Zum Beispiel: Wenn Tante Martas Erinnerungen erwähnen, dass Urenkel Paul verheiratet war, kann der Forscher dies als Anhaltspunkt nehmen, dass die Beziehung zwischen Paul und seiner Frau existiert und diese als Quelle für die Annahme zitieren.

Die Schaltflächen , und ermöglichen das Hinzufügen, Ändern und Entfernen eines Quellenhinweises zu dieser Beziehung. Beachte, dass die und Schaltflächen nur verfügbar sind, wenn ein Quellenbezug aus der Liste gewählt ist.

{{-}}

#### Attribute

  
Der Reiter erlaubt es dir die Ansicht und das Bearbeiten spezieller Informationen über die Beziehung, die als Eigenschaft ausgedrückt werden können. Die Schaltflächen , und ermöglichen das Hinzufügen, Ändern und Entfernen eines Attributs. Beachte, dass die und Schaltflächen nur verfügbar sind, wenn ein Attribut aus der Liste gewählt ist.

{{-}}

#### Notizen

  
Der Reiter lässt dich Notizen betrachten und bearbeiten, die mit der Beziehung verbunden sind. Dies können alle Anmerkungen sein, die naturgemäß nicht in die "Parameter-Wert" Paare passen, die bei den Attributen zur Verfügung stehen. Zum Hinzufügen einer Notiz oder Ändern einer bestehenden Notiz bearbeite einfach den Text im Texteingabefeld.

Die Schaltfläche im Notiz Editor erlaubt es festzulegen, wie die Notiz in Berichten und auf Webseiten erscheint. Wenn du sie nicht aktivierst hat der erzeugte Text nur einfache Leerstellen anstelle von Tabulatoren, einfachen Zeilenenden und mehrfachen Leerzeichen. Eine Leerzeile zwischen zwei Blöcken signalisiert einen neuen Absatz; zusätzliche Leerzeilen werden ignoriert.

Wenn du die Vorformatiert Schaltfläche aktiviert hast, erscheint der Text in Berichten und auf Webseiten genau so wie du ihn im Dialog eingegeben hast.

{{-}}

#### Galerie

  
Der Reiter lässt dich Fotos und andere Medienobjekte, die mit der Beziehung in Verbindung stehen, anzeigen und speichern. Der zentrale Bereich des Fensters listet all diese Objekte und zeigt eine Vorschau der Bilddateien. Andere Objekte wie Audiodateien, Filmdateien usw. werden durch ein GRAMPS-Icon dargestellt. Die Schaltflächen , , und ermöglichen es dir ein neues Bild hinzuzufügen, eine Referenz zu einem existierenden Bild hinzuzufügen, ein bestehendes Bild zu ändern und eine Medienobjektreferenz zur Beziehung zu entfernen. Beachte, dass die und Schaltflächen nur verfügbar sind, wenn ein Medienobjekt aus der Liste gewählt ist.

{{-}}

#### HLT

![[_media/LDSOrdinanceEditor-dialog-default-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Sealed to Spouse Ordinationseditor vom &quot;Familie bearbeiten&quot; - Dialog - Beispiel]] Auf der Registerkarte (Heiligen der Letzten Tage) des Familieneditors werden nur Informationen zur HLT **Sealed to Spouse** angezeigt. (Die Ordination in Bezug auf Einzelpersonen können auf der [Registerkarte HLT des <strong>Personeneditors</strong>](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Daten_eingeben_und_bearbeiten:_Ausführlich_-_Teil_1#HLT) aufgezeichnet werden.) Die HLT-Registerkarten im Familien-Editor und im Personen-Editor können über das Kontrollkästchen "HLT-Registerkarte im Personen- und Familien-Editor ausblenden" unter dem **** Abschnitt der -Registerkarte im ausgeblendet werden.

Die Daten können auch , , und enthalten.

Jeder Ordnungsdatensatz kann auch auf den entsprechenden Registerkarten und mit Anmerkungen versehen werden. Der Status der Verordnung kann über die im Popup-Menü verfügbaren Optionen beschrieben werden.

  
Die Statuszustände für die **An den Ehepartner gesiegelt** Ordnung sind:

- **<Kein Status>** *(Standardeinstellung)*
- Abgebrochen
- Geklärt
- Abgeschlossen
- Nicht siegeln
- Vor-1970
- Qualifiziert
- Nicht siegeln/Abbrechen
- Eingereicht
- Nicht freigegeben

Um Quellendaten zu bearbeiten, wechsle in die Quellenansicht und wähle den gewünschten Eintrag aus der Quellenliste. Klicke den Eintrag doppelt oder die Schaltfläche in der Werkzeugleiste, um den folgenden Dialog zu öffnen.

Der Hauptteil des Fensters zeigt vier Reiter, die verschiedene Arten von Informationen enthalten. Klicke einen Reiter, um seinen Inhalt anzusehen oder zu bearbeiten. Der untere Teil enthält die und Schaltfläche. Klicken der Schaltfläche bestätigt zu jeder Zeit alle Änderungen, die in jedem Reiter getätigt wurden und schließt das Dialogfenster. Klicken der Schaltfläche schließt jederzeit das Fenster ohne die Änderungen zu übernehmen.

Siehe auch:

- Personeneditor Dialog Registerkarte
- Familieneditor Dialog

{{-}}

## Daten bearbeiten

Dieser Abschnitt beschreibt das Eingeben und Ändern von Daten (Plural von Datum). Da Daten in der Ahnenforschung so wichtig sind, gibt sich Gramps besondere Mühe bei der Aufbewahrung und Verwendung jeder verfügbaren Datumsinformation.

Informationen können in ein Datumsfeld eingegeben werden, indem du es direkt eingibst oder indem du das Dialogfeld aufrufst, indem du auf die Schaltfläche ![[_media/22x22-gramps-date.png]] neben einem beliebigen Eingabefeld für klickst.

Siehe auch:

- [Gramps 6.0 Wiki Handbuch - Vermutlich lebend](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Vermutlich_lebend)

- im Abschnitt **Berechnungsgrenzen** - Ändern der Standardwerte für das typische Alter bei der Geburt, zwischen den Generationen usw.

### Datumsauswahl Dialog

![[_media/DateSelection-dialog-defaults-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}}  - Dialog - Standard]]

While the below [parsing rules](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1#Date_formats_and_parsing_rules) provide a guide for you to type in most common dates, you can also use dialog. The dialog is particularly useful for building a complex date or for simply insuring that your information is entered in a way Gramps will understand.

Die folgenden Felder sind verfügbar:

- Wähle einen alternativen [Kalendertyp](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Daten_eingeben_und_bearbeiten:_Ausführlich_-_Teil_1#Kalender).

  - [**Gregorianisch**](https://de.wikipedia.org/wiki/Gregorianischer_Kalender) (Standardeinstellung)
  - *[Julianisch](https://de.wikipedia.org/wiki/Julianischer_Kalender) (einschließlich [gemischte](wiki:Dates#Dual_Dated)/[Dual-datierte](#Dual-datierte_Daten) Daten)*
  - *[Hebräisch](https://de.wikipedia.org/wiki/J%C3%BCdischer_Kalender)*
  - *[Französisch-Republikanisch](https://de.wikipedia.org/wiki/Franz%C3%B6sischer_Revolutionskalender)*
  - *[Persisch](https://en.wikipedia.org/wiki/Iranian_calendars#Old_Persian_calendar)*
  - *[Islamisch](https://de.wikipedia.org/wiki/Islamischer_Kalender)*
  - *[Schwedisch](https://de.wikipedia.org/wiki/Schwedischer_Kalender)* - [Schwedischer Kalender](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Daten_eingeben_und_bearbeiten:_Ausführlich_-_Teil_1#Schwedischer_Kalender)

-  Dieses Feld kann mit dem passenden ausgewählt werden: Feld, wenn der alternative [duales Datieren](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Daten_eingeben_und_bearbeiten:_Ausführlich_-_Teil_1#Dual-datierte_Daten) unterstützt. (Kontrollkästchen standardmäßig deaktiviert)

  - (Standardmäßig leeres Textfeld)

- Stellt die [Datumsqualität](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Daten_eingeben_und_bearbeiten:_Ausführlich_-_Teil_1#Datumsqualit.C3.A4t) ein.

  - **Regulär**(Vorgabe)
  - *Geschätzt*
  - *Berechnet*

- Stellt die Intervallgenauigkeit oder die [Datumsart](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Daten_eingeben_und_bearbeiten:_Ausführlich_-_Teil_1#Datumsart) des Zeitrahmens ein.

  - **Regulär**(Vorgabe) - das Intervall, das sich über einen bestimmten Tag, Monat oder Jahr erstreckt (unabhängig von der Zeitzone)
  - *Vor*
  - *Nach*
  - *Um*
  - *Zeitraum* - Das Feld steht zur Verfügung, um ein Datum festzulegen.
  - *Von*
  - *Bis*
  - *Zeitspanne* - Das Feld steht zur Verfügung, um ein Datum festzulegen.
  - *Nur Text*

- Wähle das , den und den .

- Wenn deine Datums *Zeitraum* oder *Spanne* ist, ist diese Option verfügbar, um ein Datum festzulegen.

- Das Texteingabefeld ermöglicht das Speichern einer beliebigen Textzeichenfolge zusammen mit dem Datum.

Am unteren Rand des Dialogfelds befinden sich außerdem die Schaltflächen , und sowie ein Statuszeilenbereich direkt unter den Schaltflächen, der Rückmeldung zu eventuellen Problemen bei der Dateneingabe gibt.

{{-}}

### Datum Gültigkeitsanzeigen

![[_media/DateSelection-dialog-example-60-de.png|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Datumsauswahl" Dialog - Beispiel]]

Gramps verwendet eine Gültigkeitsprüfung beim Datum.

Obwohl unvollständige Daten nicht den eindeutigen Tag bestimmen, erlauben sie immerhin einige Varianten beim Vergleich von Daten.

Das Datumsfeld wird rot hervorgehoben und ein rotes Symbol (z. B. ein Stoppschild oder ein Kreuz) angezeigt, um anzuzeigen, dass das eingegebene Datum nicht als bekanntes und gültiges Format für ein Datum erkannt wird.

Beispiele für häufig verwendete Datumsangaben, bei denen es sich nicht um erkennbare Gramps-Formate handelt, sind "Weihnachtswoche '61", "Herbst 1782" oder "Sommer, in dem ich operiert wurde". In diesem Fall wird das Datum als Zeichenfolge gespeichert und als Nur-Text-Typ markiert. Daten dieses Typs werden nicht mit anderen Daten verglichen. Wo immer möglich, ist es vorzuziehen, solche Nur-Text-Datumseinträge zu vermeiden. Es könnte beispielsweise besser sein, ein Datum von "Dezember 1961" einzugeben und dann die Beschreibungsanmerkung "Weihnachtswoche von '61" hinzuzufügen. Es wäre genauer, einen Kalender für Dezember 1961 zu überprüfen und dann die tatsächliche Datumsspanne einzugeben ... aber dennoch die Anmerkung einzuschließen. Die Anmerkung wird benötigt, da du nicht davon ausgehen kannst, dass "Weihnachtswoche" für dich dieselbe Zeitspanne von Tagen bedeutet wie für deine Quelle. Es könnte eine kulturelle Tendenz geben, die Interpretation zu färben. Dies könnte bedeuten, dass die Kalenderzeile den Weihnachtstag enthält. Amerikanische und europäische Kalenderzeilen beginnen jedoch an verschiedenen Wochentagen. Oder es könnte die 7 Tage bedeuten, die mit Weihnachten beginnen, oder sogar die 7 Tage, die mit Weihnachten enden. Die Spanne ermöglicht also Suchen und Vergleiche, aber die Anmerkung zeigt, dass das tatsächliche Intervall interpretiert werden muss.

In den verschiedenen Ansichten (z. B. der ) werden nicht erkannte Datumsangaben standardmäßig in **Fettschrift** angezeigt. Die Textmarkierung (Formatierungsstil) für nicht erkannte Datumsangaben kann durch Ändern der Option im Abschnitt der Registerkarte [-Registerkarte](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Einstellungen#Umgebungseinstellungen) von [Einstellungen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Einstellungen) geändert werden.

Wenn ein Geburts- oder Sterbedatum für eine Person fehlt, werden möglicherweise die Daten vorhandener Ersatz-Ereignisse in derselben Kategorie angezeigt (und kursiv mit einem abgekürzten Titel gekennzeichnet), anstatt die Anzeige leer zu lassen. So wird ein Begräbnis- oder Einäscherungsdatum angezeigt, wenn noch kein Todesdatum aufgezeichnet wurde.

{{-}}

### Datumsqualität

- *Regulär*: Ein "reguläres" Datum ist ein Datum mit einem expliziten Tag, Monat oder Jahr.

<!-- -->

- *Geschätzt*: Ein "geschätztes" Datum basiert auf durchschnittlichen Intervallannahmen, die von einem bekannten Referenzdatum versetzt sind. (Wie die durchschnittliche Anzahl der Jahre zwischen den Generationen, die maximale Lebensdauer oder die Länge der Seereise.)

<!-- -->

- *Berechnet*: Ein "berechnetes" Datum basiert auf einem bekannten Intervall ab einem Referenzdatum, ohne dass eine Quelle das Datum explizit erwähnt. (Zum Beispiel ein Grabstein, in den sowohl ein Todesdatum als auch ein genaues Todesalter eingraviert sind.)

Volkszählungsdaten sind insofern ungewöhnlich, als sie einem Kandidaten für ein berechnetes Datum erscheinen, dies jedoch nicht sind. Die Volkszählung definiert häufig explizit das Intervall (Alter) und das Referenzdatum (Datum der Volkszählungsabfrage), aber dieses Alter wird häufig geschätzt oder gerundet.

### Datumsart

Rechts neben der Option sollte das Einblendmenü angezeigt werden.

Daten in Gramps werden nach den folgenden Arten der Genauigkeit (Skala) des Intervalls oder Zeitrahmens klassifiziert:

- **Regulär**: Ein "reguläres" Datum ist ein Datum, das ein Intervall umfasst, das sich über einen bestimmten Tag, Monat oder Jahr erstreckt. Es kann vollständig (oder für ein 24-Stunden-Intervall wie den 6. Juni 1990 „voll qualifiziert“) oder teilweise (wie das Weglassen des Tages für ein 1-Monats-Intervall wie Juli 1977 oder das Weglassen von Tag und Monat für ein 1-Jahres-Intervall) sein.

<!-- -->

- **Vor**: Ein "Vor"-Datum kann nur als vor einem bestimmten Tag, Monat oder Jahr auftretend (in einem [von Einstellungen festgelegten langen Intervall](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Einstellungen#Daten)) identifiziert werden. *(Standardmäßig beträgt das Intervall 50 Jahre.)*

<!-- -->

- **Bis** Ein "bis"-Datum ist ein Datum, das eine unbestimmte Zeitspanne vor einem bestimmten Tag, Monat oder Jahr liegt. Im Gegensatz zu einem "vor"-Datumstyp ist die Spanne in die Vergangenheit unbegrenzt.

<!-- -->

- **Ab** Ein "von"-Datum ist ein Datum, das eine unbegrenzte Zeitspanne nach einem bestimmten Tag, Monat oder Jahr darstellt. Im Gegensatz zu einem "nach"-Datumstyp ist die Spanne in die Zukunft unbegrenzt.

<!-- -->

- **Nach**: Ein "Nach"-Datum tritt nach einem bestimmten Tag, Monat oder Jahr (in einem [von den zweiten Einstellungen festgelegten langen Intervall](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Einstellungen#Daten)) auf. *(Standardmäßig beträgt das Intervall 50 Jahre.)*

<!-- -->

- **Um**: Ein "Um" (circa) Datum ist ein Datum, das (in [einem weiteren von Einstellungen definierten ±Jahre Intervall](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Einstellungen#Daten)) vor oder nach einem bestimmten Tag, Monat oder Jahr auftritt. *(Standardmäßig beträgt das Intervall 50 Jahre.)*

<!-- -->

- **Zeitraum**: Ein "Zeitraum" beschreibt einen Zeitraum innerhalb dessen das Ereignis stattfand. Es kann sich um ein wiederkehrendes Ereignis während des Intervalls handeln oder um eine einzelne Instanz, von der angenommen wird, dass sie zwischen bekannten Grenzdaten aufgetreten ist.

  
Zum Beispiel "zwischen Januar 1932 und März 1932."

- **Zeitspanne**: Eine "Zeitspanne" beschreibt einen Zeitraum während der eine Bedingung erfüllt war.

  
Zum Beispiel "vom 12. Mai 2000 bis zum 2. Februar 2002."

### Datumsformate und Syntaxanalyseregeln

Das Dialogfeld hilft nur beim Layouten eines Datums im Standardformat, das Gramps analysieren kann. Dies ist nützlich, wenn du mit den Optionen nicht vertraut bist, einen alternativen Kalender verwenden oder ein Neujahrsbeginndatum angeben musst.

Gramps erkennt Daten, die in verschiedenen Formaten eingegeben wurden. Das standardmäßige numerische Format ist das für die Umgebung übliche Format, in dem Gramps arbeitet. das heißt, *TT.MM.JJJJ* für die meisten europäischen Länder, *MM/TT/JJJJ* für die USA und so weiter. Eine Möglichkeit, diese Mehrdeutigkeit zu vermeiden, besteht darin, immer das Format *d mmm jjjj* oder *mmmn d jjjj* zu wählen. Es analysiert den Monat und die Monatsabkürzungen, die in der gerade aktiven Sprache eingegeben wurden.

Es analysiert auch Daten, die in Quartalen eingegeben wurden, und wandelt sie in „zwischen“-Spannen um. z.B. „q2 1820“ wird zu „zwischen 1 Apr 1820 und 30 Jun 1820“.

Neben den genauen Daten erkennt Gramps viele Datentypen, die nicht regelgerecht sind: vor, bis, ab, nach, um, Zeitraum und (von/bis oder zwischen) Zeitspanne. Es versteht auch die Qualität: geschätzt oder berechnet. Schließlich werden Teildaten und viele alternative Kalender unterstützt. Unten findest du eine Liste der Datumseingaberegeln, um eine genaue Datumsanalyse zu ermöglichen.

Ein **reguläres einzelnes Datum** kann wie du es schreiben würdest eingegeben werden. Wenn du nach dem Jahr einen Schrägstrich gefolgt von einem Wert 1 Jahr später eingibst, wird ein julianischer dual datierter Eintrag erstellt

  
Beispiele: **24. Mai 1961**, **31. Dez 1858/9** oder **1.1.2004**.

**Before the Common Era** (BCE, BC und B.C.E.) und sind Bezeichnungen für den Gregorianischen oder Julianischen Kalender. "Common Era" und "Before the Common Era" sind religiös neutrale Alternativen zu den bekannten Bezeichnungen Anno Domini (AD) und Before Christ (BC), die für dieselbe Kalenderepoche verwendet werden. Die Schreibweise wird auf die Form "B.C.E." harmonisiert. Beispiele: "ca. 25 Dez 32 v. Chr. Julianisch" wird zu "um 25 Dez 32 B.C.E. (Julianisch)"

**Teildaten** werden einfach durch Weglassen unbekannter Informationen eingegeben.

  
Beispiele: Mai 1961 und 2004.

Daten, die nicht regulär sind, sollten mit den .{{#expr:{{#var:figure}}+1}}):

![[_media/Gravestone.jpg|Abb. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Grabstein zeigt Doppeldatum als Bruch (170 und 3/4, was 1703 und 1704 bedeutet)]]

Um ein Datum als doppelt datiert zu kennzeichnen, füge einfach einen Schrägstrich `/` zwischen die Jahreszahlen ein. Beispiel:

- 1721/2
- 1719/20
- 1799/800

Diese Schrägstrichjahre können an jeder Stelle in einem Datum verwendet werden, wo auch ein reguläres Jahr stehen könnte.

Dual-datierte-Daten sind zur Zeit im julianischen Kalender vertreten, daher sind ihr Monat und Tag identisch mit der textlichen Darstellung. {{-}}

#### Wechselnder Neujahrstag

Bei doppelt datierten Daten (und anderen Daten) weist du vielleicht, dass das neue Jahr an einem anderen Tag als dem 1. Januar gefeiert wurde. Um dies in Gramps anzugeben, setze den Monats-/Tag-Code in Klammern oder runde Klammern `()` , nach dem Kalender (falls vorhanden). Zum Beispiel:

- Jan 20, 1865 (`Mar25`)
- Jan 20, 1750 (`Julian`,`Mar1`)
- Feb 23, 1710/1 (`Mar25`)

Um den Beginn eines Jahres anzugeben, das nicht am 1. Januar beginnt, verwende die folgenden Datumsschlüssel :

- `Jan1`
- `Mar1`
- `Mar25`
- `Sep1`

Du kannst dies als einzigen Wert in Klammern setzen oder rechts neben dem Kalendernamen (Komma, und keinen Abstand).

Bitte beachte, dass, wenn der Neujahrstag nicht der 1. Januar ist, der Januar in diesem Jahr nach dem Dezember kommt. Daten mit diesen Neujahrstag-Codes werden entsprechend sortiert.

{{-}}

[D](wiki:Category:De:Dokumentation)
