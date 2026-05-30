---
title: Da:Gramps 6.0 brugsanvisning - Rapporter - del 3
categories:
- Documentation
- Plugins
- Stub
managed: false
source: wiki-scrape
wiki_revid: 129340
wiki_fetched_at: '2026-05-30T17:30:47Z'
lang: da
---

{{#vardefine:chapter\|13.3}} {{#vardefine:figure\|0}} Tilbage [Indeks over Rapporter](wiki:Da:Gramps_6.0_brugsanvisning_-_Rapporter). {{-}}

<hr>

{{-}}

![[_media/Menubar-ReportsOverview-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menu-indgang for]] Dette afsnit beskriver rapporten **Bøger**, som er tilgængelig i Gramps.

## Bøger <span id="Books"></span>

Rapporten **Bøger** giver mulighed for at oprette en brugerdefineret **slægtsbog**, der indeholder en samling af tekst- og grafiske rapporter fra Gramps i et enkelt dokument (dvs. en bog).

Den eneste rapport, der er tilgængelig under denne rapport, er bograpporten.

Når du vælger fra menuen, vises hoveddialogen . {{-}}

### Administrer bøger <span id="Manage Books dialog"></span>

![[_media/ManageBooks-dialog-default-60-da.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Administrer bøger - dialog]]

Hoveddialogboksen har tre sektioner: , og

For at starte oprettelsen af ​​din brugerdefinerede slægtsbogsrapport skal du klikke på knappen , når alle valg af rapporter, der skal inkluderes, er foretaget og muligvis konfigureret (eller omkonfigureret) eller blot accepteret standardindstillingerne. Dette vil vise dialogboksen .

#### Bog navn <span id="Book name"></span>

Tekstindtastningsfeltet (`Ny bog`standard) viser navnet på den aktuelle bog. Rediger det, og gem din brugerdefinerede bog (et sæt konfigurerede valg) til senere brug. I så fald kan du først ændre feltet, så det indeholder det navn, du ønsker. Hvis du indlæser en gemt bog (se nedenfor), vil den vise bogens navn -- som derefter kan ændres, hvis du vil gemme en lidt anderledes konfiguration.

##### Værktøjslinje til bognavn <span id="Book name toolbar"></span>

Det øverste vandrette sæt af værktøjslinjeikoner nær feltet fungerer på hele bogen og tillader følgende funktioner:

- Ikonknappen rydder alle tidligere valgte elementer fra sektionen .

<!-- -->

- Ikonet bruges til at gemme den aktuelle bog (under det navn, der tidligere blev indtastet i tekstfeltet ) til senere brug. Hvis bognavnet allerede findes, vil du blive spurgt, om du vil for at gemme oveni, eller om du kan og angive et andet navn.

{{-}} ![[_media/OpenPreviouslyCreatedBook-AvailableBooks-dialog-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Ikonet &quot;Åbn tidligere oprettet bog&quot; og den resulterende dialogboks &quot;Bøger til rådighed&quot;]]

- Vælg ikonet for at åbne vinduet , som viser alle dine tidligere gemte bøger. I den boks skal du enten dobbeltklikke på et bestemt bognavn eller først vælge det og derefter trykke på for at indlæse bogen.

{{-}} ![[_media/ManagePreviouslyCreatedBooks-AvailableBooks-dialog-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Ikonet &quot;Administrer tidligere oprettede bøger&quot; og den resulterende dialogboks &quot;Bøger til rådighed&quot;]]

- Du kan også vælge ikonet for at åbne et lidt anderledes vindue, der viser din liste over tilgængelige bøger, og ved at bruge knappen kan du fjerne den valgte bog.

{{-}}

##### Bøger til rådighed <span id="Available Books window"></span>

###### Bøger til rådighed (1) <span id="Available Books window (1)"></span>

![[_media/OpenPreviouslyCreatedBook-AvailableBooks-dialog-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Ikonet "Åbn tidligere oprettet bog" og den resulterende dialogboks "Bøger til rådighed"]]

vindue

"Åbn tidligere oprettet bog" og den resulterende dialogboks "Bøger til rådighed" - dialog {{-}}

###### Bøger til rådighed (2) <span id="Available Books window (2)"></span>

![[_media/ManagePreviouslyCreatedBooks-AvailableBooks-dialog-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Håndtér tidligere oprettet bøger" ikon og "Bøger til rådighed" - dialog]]

vindue med **Slet** knap !

"Håndtér tidligere oprettet bøger" icon and resulting "Bøger til rådighed" - dialog {{-}}

#### Elementer til rådighed <span id="Available items"></span>

![[_media/ManageBooks-dialog-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Tilgængelige elementer (sektionsliste) fra dialogboksen &quot;Administrer bøger&quot; - med kontekstmenu]] Den midterste sektion viser de bogelementer, der er tilgængelige til inkludering i bogen.

Listen viser `Navn` og `Type` af tilgængelige rapporter, som du enten kan dobbeltklikke på for at tilføje rapporten eller højreklikke på et valg og bruge kontekstmenuen .

##### Kontekstmenu for Elementer til rådighed <span id="Available items context menu"></span>

- \- valgt indgang til bogen.

#### Valg af tilgængelige elementer <span id="Available items selections"></span>

Næsten alle 26 bogelementer, der er tilgængelige til inkludering i bogen, er tekstbaserede eller grafiske rapporter og er derfor tilgængelige i form af separate rapporter (se [Indeks over rapporter](wiki:Gramps_6.0_Wiki_Manual_-_Reports) for deres individuelle dokumentation). Undtagelserne er følgende 4 elementer, som kun er tilgængelige som bogelementer i en bograpport:

- [Alfabetisk indeks](#Alphabetical_Index)
- [Brugerdefineret tekst](#Custom_Text)
- [Indholdsfortegnelse](#Table_Of_Contents)
- [Titelside](#Title_Page)

De andre 22 bogelementer har ikke fanen , som kun er tilgængelig for de separate rapporter. Bemærk, at bogelementversionen af ​​rapporten kan have et lidt anderledes navn end den separate version.

- Stamtræ - samme som rapporten [Stamtræ](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_4#Ancestor_Tree).

<!-- -->

- Kalender
- Efterkommertavle - samme som rapporten [Efterkommertræ](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_4#Descendant_Tree).

{{-}}

##### Alfabetisk indeks <span id="Title Page"></span>

![[_media/AlphabeticalIndex-book-item-BooksReport-options-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Alfabetisk indeks - element]]

Bogelementet producerer side(r) med et alfabetisk indeks over personer, der er noteret i udvalgte tekstrapporter.

På fanen kan du vælge sproget fra rullelisten.

{{-}}

##### Brugerdefineret tekst <span id="Custom Text"></span>

![[_media/CustomText-book-item-BooksReport-options-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Brugerdefineret tekst - element]]

Bogelementet producerer en side med tre afsnit, der hver indeholder brugerdefineret tekst.

Fanen viser:

- 

- 

- 

Tekstinputfelterne kan udvides, så du virkelig kan indsætte al den tekst, du ønsker.

Den nederste vinduesdel viser nogle : her kan du vælge . Du kan vælge standardstilen eller klikke på knappen . Dette åbner et -vindue, hvor du kan tilføje og fjerne stilarter. For flere detaljer, se også [stileditor](wiki:Gramps_6.0_Wiki_Manual_-_Settings/da#Style_editor_dialog). Dette element er typisk beregnet til at blive brugt til epigrafer, dedikationer, forklaringer, noter osv.

{{-}}

##### Indholdsfortegnelse <span id="Table Of Contents"></span>

![[_media/TableOfContents-book-item-BooksReport-options-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Indholdsfortegnelse - element]]

En (TOC) genereres for bogen som en liste over delene af en bog eller et dokument organiseret i den rækkefølge, som delene vises i.

På fanen kan du vælge sproget fra rullelisten.

{{-}}

##### Titelside <span id="Title Page"></span>

![[_media/TitlePage-book-item-BooksReport-options-52.png|Fig. {{#var:kapitel}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Titelside - element]]

Hvis du valgte bogelementet og klikkede på knappen for at tilføje dette element til din bog, og du klikker på knappen (Konfigurer det aktuelt valgte element), får du vist et -vindue.

På fanen har du tre tekstfelter tilgængelige, hvor du kan ændre den viste eksempeltekst. \* (`Bogens titel` standard)

- (`Bogens undertitel` standard)

- (`Copyright 2024 Alex Roitman...` standard) (FYI Alex var en tidlig bidragyder til Gramps-projektet)

<!-- -->

- tillader valgfri placering af et billede mellem undertitlen og sidefoden ved at vælge knappen

  - , som viser vælgerdialogboksen , hvor du kan vælge det eksisterende billede, du ønsker.

- Du kan også ændre standardindstillingen (`0.0`) størrelse.

Den nederste del af vinduet viser nogle **Dokumentindstillinger**: her kan du vælge **Stil**. Du kan vælge standardstilen eller klikke på knappen . Dette åbner et -vindue, hvor du kan tilføje og fjerne stilarter. For flere detaljer, se også [Stilredigering](wiki:Gramps_6.0_Wiki_Manual_-_Settings/da#Style_editor_dialog).

Fordi du kan konfigurere de forskellige elementer, kan dette element bruges til at oprette titelsider for hele bogen, dens kapitel eller endda et enkelt element.

{{-}}

#### Aktuel bog <span id="Current book"></span>

Den nederste sektion viser de aktuelt valgte elementer i den rækkefølge, de vises i bogen.

Listen viser `Elementnavn`, `Type` og `Emne` for dine aktuelle bogvalg, som du kan dobbeltklikke på for at opsætte/konfigurere rapporten eller bruge [Kontekstmenuen for aktuel bog](#Current_book_context_menu) til at foretage yderligere ændringer i bogen.

{{-}}

##### Værktøjslinje for aktuel bog <span id="Current book tool bar"></span>

![[_media/ManageBooks-dialog-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Administrer bøger - dialog]]

Det nederste højre sæt af lodrette værktøjslinjeikoner ved siden af ​​sektionstabellen fungerer på sektionerne og tillader følgende funktioner:

- Brug ikonknappen for at tilføje det valgte element fra den øverste sektionsliste til sektionslisten nedenfor. Brug af genvejen eller dobbeltklik på det valgte element (øverste liste) vil også tilføje det.
- Brug ikonknappen for at fjerne et element fra den nederste sektionsliste.
- Brug ikonknappen for at ændre rækkefølgen af ​​det valgte element i .
- Brug ikonknappen for at ændre rækkefølgen af ​​det valgte element i .
- Med ikonknappen kan du konfigurere indstillingerne for det valgte **element** i -- men du skal først vælge elementet, ellers vises advarslen . Dobbeltklik på et element vil også starte en konfigurationsdialog. Konfigurationsdialogen, der åbnes af ikonknappen , er elementspecifik. Hvis du vælger ikke at konfigurere elementet, vil nogle standardindstillinger blive brugt til alle nødvendige indstillinger. Den fælles indstilling for næsten alle bogelementer er den midterste person: den person, som elementet er centreret om. Takket være denne indstilling kan du oprette en bog med elementer centreret om forskellige personer (f.eks. din mors og fars forfædre som separate kapitler). Som standard er den midterste person indstillet til . ![[_media/No-selected-book-item-warning-52.png|højre|tommelfinger|Intet valgt bogelement - advarsel]]

{{-}}

##### Aktuel bog kontekstmenu

- 

- 

- 

- 

---

- 

- 

- 

- 

{{-}}

### Dan bog-dialogboksen <span id="Generate Book dialog"></span>

![[_media/GenerateBook-dialog-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Dan bog - dialogboks]]

Du vil se dialogboksen , når du har valgt dialogboksen for at acceptere standardindstillingerne og starte oprettelsen af ​​din brugerdefinerede slægtsbog.

Der er to sektioner og :

#### Papirindstillinger <span id="Paper Options"></span>

, hvor du kan ændre størrelse og retning for papirformatet og alle margener. Der er et afkrydsningsfelt til at bruge metriske værdier i stedet.

Se også:

- Samme som
  - Grafiske rapporter - fanen [Papirindstillinger](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_4/da#Paper_Options)
  - Tekstrapporter - fanen [Papirindstillinger](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_6/da#Paper_Options)

#### Dokument-tilvalg <span id="Document Options"></span>

Afsnittet giver mulighed for at ændre:

- brug rullemenuen til at ændre uddataformat:

  - **PDF-dokument** (standard)
  - *PostScript*
  - *OpenDocument tekst*
  - *Udskriv...*

-  hvis markeret, tillader det dig at åbne i standardfremviseren, f.eks.: [LibreOffice](https://www.libreoffice.org/download/) Writer tekstbehandlingsprogram. (afkrydsningsfeltet er som standard ikke markeret)

- Indtast dit filnavn. Bemærk, at filnavnetypen ændres afhængigt af uddataformatet. F.eks.: For *PDF-dokumenter* er standardværdien `/yourhomedir/`<Familietræsnavn>`_bog.pdf` og *OpenDocument Text* er standardværdien `/yourhomedir/`<Familietræsnavn>`_bog.odt` osv.

#### Se også

- [Tilføj en indholdsfortegnelse eller et indeks til en rapportbog](wiki:Add_Table_of_Contents_or_Index_to_reports)

{{-}}

<hr>

Tilbage til [Indeks over Rapporter](wiki:Da:Gramps_6.0_brugsanvisning_-_Rapporter). {{-}}

[Category:Documentation](wiki:Category:Documentation) [Category:Plugins](wiki:Category:Plugins)
