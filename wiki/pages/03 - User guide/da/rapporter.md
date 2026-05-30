---
title: Da:Gramps 6.0 brugsanvisning - Rapporter
categories:
- Documentation
- Plugins
- Stub
managed: false
source: wiki-scrape
wiki_revid: 129337
wiki_fetched_at: '2026-05-30T17:04:52Z'
lang: da
---

{{#vardefine:chapter\|13}} {{#vardefine:figure\|0}}

![[_media/Menubar-ReportsOverview-60-da.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menulinje - Rapportoversigt]] Dette afsnit giver en kort beskrivelse af alle de forskellige rapporter, der er tilgængelige i Gramps.

Gramps leveres med et stort antal tilgængelige rapporter. De forskellige underafsnit beskriver de forskellige muligheder og valgmuligheder:

## Introduktion <span id="Introduction"></span>

[Generering af rapporter](wiki:Da:Gramps_6.0_brugsanvisning_-_Rapporter_-_del_1): Dette første underafsnit giver dig nogle generelle bemærkninger.

## Rapporter <span id="Reports "></span>

![[_media/ToolbarIcon-Reports-OpenTheReportsDialog-60-da.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Rapporter" værktøjslinjeikon for "Åbn rapportdialogboksen"]]

Rapporterne kan tilgås ved at vælge menuen .

Alternativt kan du gennemse det komplette udvalg af tilgængelige rapporter sammen med deres korte beskrivelser i en dialogboks, der åbnes ved at klikke på ikonet ![[_media/Gramps-reports.png]] på værktøjslinjen fra en hvilken som helst af kategorierne. {{-}}

### Dialogboksen Valg af rapport

![[_media/ReportSelection-dialog-default-60-da.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Rapportvalg - dialog - standardinformation]]

![[_media/ReportSelection-dialog-example-60-da.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Rapportvalg - dialog - eksempel der viser information om "Tidslinietavle"]]

Dialogboksen giver dig mulighed for at gennemse det komplette udvalg af tilgængelige rapporter sammen med deres korte beskrivelser, når den åbnes ved at klikke på ikonet ![[_media/Gramps-reports.png]] på værktøjslinjen fra en hvilken som helst af kategorierne.

**Vælg en rapport blandt de tilgængelige til venstre**. Brug pilene på til at udvide listeniveauet:

- [Tavler](#Tavler)
- [Grafiske rapporter](#Grafiske_rapporter)
- [Tekstrapporter](#Tekstrapporter)
- [Websider](#Websider)

Vælg derefter den rapport, du er interesseret i, for at få vist følgende i højre side:

- Rapportnavn
- Rapportbeskrivelse
- Status:
- Forfatter:
- Forfatterens e-mail:

Du kan derefter bruge knapperne nedenfor til enten at finde ud af mere om rapporten eller åbne og oprette din rapport.

- åbner hjælpesiden, hvis tilgængelig - kræver en internetforbindelse

- afslutter denne dialog

- \-  - åbner rapportkonfigurationssiden.

{{-}} Se også: [Dialog til værktøjsvalg](wiki:Gramps_6.0_Wiki_Manual_-_Tools#Tool_Selection_dialog) {{-}}

## Erstatningsværdier <span id="Substitution Values"></span>

[Erstatningsværdier](wiki:Gramps_6.0_Wiki_Manual_-_Rapporter_-_del_2): Du kan bruge nogle praktiske værdier i dine rapporter. (Kun udvalgte rapporter)

## Bøger <span id="Books"></span>

[Rapporten Bøger](wiki:Da:Gramps_6.0_brugsanvisning_-_Rapporter_-_del_3#Bøger) giver dig mulighed for at oprette en brugerdefineret **slægtsbog**, der indeholder en samling af Gramps tekstrapporter og grafiske rapporter i et enkelt dokument (dvs. en bog)

### Valg af tilgængelige elementer

#### Alfabetisk indeks

[Alfabetisk indeks](wiki:Da:Gramps_6.0_brugsanvisning_-_Rapporter_-_del_3#Alfabetisk_indeks) - Dette element producerer side(r) med et alfabetisk indeks over personer, der er noteret i udvalgte tekstuelle rapporter.

#### Brugerdefineret tekst

[Brugerdefineret tekst](wiki:Da:Gramps_6.0_brugsanvisning_-_Rapporter_-_del_3#Brugerdefineret_tekst) - Dette element producerer en side med tre afsnit, der hver indeholder brugerdefineret tekst: Starttekst, Mellemtekst og Sluttekst. Tekstinputfelterne kan udvides, så du virkelig kan indtaste al den tekst, du ønsker.

#### Indholdsfortegnelse

[Indholdsfortegnelse](wiki:Da:Gramps_6.0_brugsanvisning_-_Rapporter_-_del_3#Table_of_contents) - En indholdsfortegnelse (TOC) genereres for en bog som en liste over delene af en bog eller et dokument organiseret i den rækkefølge, som delene vises i.

#### Titelside

[Titelside](wiki:Da:Gramps_6.0_brugsanvisning_-_Rapporter_-_del_3#Title_Page) - En titelside til din bog. {{-}}

## Oversigt over rapporter

Oversigt over alle standard indbyggede rapporter, der kan bruges.

{{-}}

### Rapportliste

Klik på en listeoverskrift for at sortere listen og vise tilgængelige indbyggede rapportvalg. (Den faktiske rapportmenu vil også indeholde installerede [Tredjepartstilføjelse](wiki:6.0_Addons#Addon_List)-rapporter.)

{{-}}

## Tavler

[Tavler](wiki:Da:Gramps_6.0_brugsanvisning_-_Rapporter_-_del_5#Tavler) rapporter oprettes i Graphviz-format og konverteres derefter til grafisk output ved at køre dem gennem [Graphviz dot tool](wiki:Da:Gramps_6.0_brugsanvisning_-_Rapporter_-_del_5#Forudsætninger_for_Graph_Reports) bag kulisserne.

### <u>Tavle over slægtslinier</u>

[Tavle over slægtslinier](wiki:Da:Gramps_6.0_brugsanvisning_-_Rapporter_-_del_5#Tavle_over_slægtslinier) opretter en letforståelig graf.

### <u>Timeglastavle</u>

[Timeglastavle](wiki:Da:Gramps_6.0_brugsanvisning_-_Rapporter_-_del_5#Timeglastavle) genererer en timeglasgraf.

### <u>Slægtstavle</u>

[Slægtstavle](wiki:Da:Gramps_6.0_brugsanvisning_-_Rapporter_-_del_5#Slægtstavle) opretter en kompleks relationsgraf. {{-}}

## Grafiske rapporter

[Grafiske rapporter](wiki:Da:Gramps_6.0_brugsanvisning_-_Rapporter_-_del_4#Graphical_Reports) repræsenterer information i form af diagrammer og grafer.

### <u>Forfædretræ</u>

<span ID="Forfædrediagram"></span> [Forfædretræsrapport](wiki:Da:Gramps_6.0_brugsanvisning_-_Rapporter_-_del_4#Forfædretræ) genererer diagrammet over personer, der er forfædre til den aktive person.

### <u>Kalender</u>

[Kalenderrapport](wiki:Da:Gramps_6.0_brugsanvisning_-_Rapporter_-_del_4#Kalender) producerer en kalender med fødselsdage og jubilæer på en side efter måned.

### <u>Efterkommertræ</u>

<span ID="Efterkommertabel"></span> [Efterkommertrærapport](wiki:Da:Gramps_6.0_brugsanvisning_-_Rapporter_-_del_4#Efterkommertræ) genererer en graf over personer, der er efterkommere af den aktive person.

### <u>Efterkommerlinjer</u>

[Tilføjelse:Efterkommerlinjer](wiki:Tilføjelse:Efterkommerlinjer) - Tredjepartstilføjelse.

### <u>Familie efterkommertræ</u>

[Familie efterkommertræ](wiki:Da:Gramps_6.0_brugsanvisning_-_Rapporter_-_del_4#Familie_efterkommertræ) genererer en graf over personer, der er efterkommere af den aktive familie.

### <u>Slægtstræ</u>

[Tilføjelse:Familietræ](wiki:Tilføjelse:Familie_træ) - Tredjepartstilføjelse.

### <u>Viftediagram</u>

[Viftediagramrapport](wiki:Da:Gramps_6.0_brugsanvisning_-_Rapporter_-_del_4#Viftediagram) producerer et diagram, der ligner en vifte, med Aktiv Person i midten, forældre halvcirklen ved siden af, og så videre, i alt fem generationer.

#### Se også

### <u>Stamtavle</u>

[Tilføjelse:PedigreeChart](wiki:Tilføjelse:PedigreeChart) - Tredjepartstilføjelse.

### <u>Statistikdiagrammer</u>

[Statistikdiagramrapport](wiki:Da:Gramps_6.0_brugsanvisning_-_Rapporter_-_del_4#Statistikdiagrammer) kan indsamle og vise et væld af statistiske data om din database.

### <u>Tidslinjediagram</u>

[Tidslinjediagramrapport](wiki:Da:Gramps_6.0_brugsanvisning_-_Rapporter_-_del_4#Tidslinjediagram) viser en liste over personer, hvis levetider er repræsenteret af intervaller på en fælles kronologisk skala. {{-}}

## Tekstrapporter

[Tekstrapporter](wiki:Da:Gramps_6.0_brugsanvisning_-_Rapporter_-_del_6#Text_Reports) viser information som formateret tekst.

### <u>Ahnentafel-rapport</u>

[Ahnentafel-rapport](wiki:Da:Gramps_6.0_brugsanvisning_-_Rapporter_-_del_6#Ahnentafel-rapport) viser den aktive person og dennes forfædre sammen med deres vitale data. Personerne er nummereret i en etableret standard kaldet 'Ahnentafel'. <span id="AncestorFill">

### <u>Ancestorfill-rapport</u>

[Addon:Ancestor Fill Report](wiki:Addon:Ancestor_Fill_Report) - Tredjeparts-tilføjelse. </span>

### <u>Fødselsdags- og jubilæumsrapport</u>

[Fødselsdags- og jubilæumsrapport](wiki:Da:Gramps_6.0_brugsanvisning_-_Rapporter_-_del_6#Fødselsdags-_og_jubilæumsrapport) giver de samme oplysninger som en kalender, men i tekstformat.

### <u>Komplet individuel rapport</u>

[Komplet individuel rapport](wiki:Da:Gramps_6.0_brugsanvisning_-_Rapporter_-_del_6#Komplet_individuel_rapport) giver individuelle opsummeringer svarende til den individuelle opsummeringsrapport.

### <u>Databaseforskellerapport</u>

[Tilføjelse:Databaseforskellerapport](wiki:Tilføjelse:Databaseforskellerapport) - Tredjepartstilføjelse.

### <u>Databaseoversigtsrapport</u>

[Databaseoversigtsrapport](wiki:Da:Gramps_6.0_brugsanvisning_-_Rapporter_-_del_6#Database_Summary_Report) viser den samlede statistik vedrørende antallet af individer af hvert køn, forskellige statistikker over ufuldstændige indtastninger samt familie- og mediestatistikker.

### <u>Efterkommerbog</u>

[Addon:Descendant and Detailed Descendant Book](wiki:Addon:Descendant_and_Detailed_Descendant_Book_Reports#Differences_to_Descendant_Reports) Rapporter - Tredjeparts-tilføjelse.

### <u>Efterkommerrapport</u>

[Efterkommerrapport](wiki:Da:Gramps_6.0_brugsanvisning_-_Rapporter_-_del_6#Efterkommerrapport) præsenterer efterkommerne af den aktive person med en kort beskrivelse i den tilsigtede stil.

### <u>Detaljeret slægtsrapport</u>

[Detaljeret slægtsrapport](wiki:Da:Gramps_6.0_brugsanvisning_-_Rapporter_-_del_6#Detaljeret_slægtsrapport) dækker detaljeret den aktive persons forfædre, inklusive en række vitale data samt ægteskaber.

### <u>Detaljeret efterkommerbog</u>

[Tilføjelse:Efterkommer og detaljeret efterkommerbog](wiki:Tilføjelse:Efterkommer_og_Detaljeret_efterkommerbog_rapporter#Forskelle_i_efterkommer_rapporter) Rapporter - Tredjepartstilføjelse.

### <u>Detaljeret efterkommerrapport</u>

[Detaljeret efterkommerrapport](wiki:Da:Gramps_6.0_brugsanvisning_-_Rapporter_-_del_6#Detaljeret_efterkommerrapport) dækker detaljeret den aktive persons efterkommere efter generation, i overensstemmelse med den genealogiske tradition med tekstuelle efterkommerrapporter efter generation. Den har til formål at levere alle vigtige funktioner, der forventes at findes i disse klassiske efterkommerformater, og har modtaget inspiration fra forskellige kilder.

### <u>Detaljeret efterkommerrapport med alle billeder</u>

[Addon:Detaljeret efterkommerrapport med alle billeder](wiki:Addon:Detailed_Descendant_Report_With_All_Images) - Tredjepartsudvidelse.

### <u>Dobbeltfætre</u>

[Addon:DoubleCousinReport](wiki:Addon:DoubleCousinReport) - Tredjepartsudvidelse.

### <u>Slut på linjerapport</u>

[Slut på linjerapport](wiki:Da:Gramps_6.0_brugsanvisning_-_Rapporter_-_del_6#Slut_på_linjerapport) indeholder en liste over personens sidst kendte forfædre med stamtavlen, sorteret efter generationer.

### <u>Familiegrupperapport</u>

[Familiegrupperapport](wiki:Da:Gramps_6.0_brugsanvisning_-_Rapporter_-_del_6#Familiegrupperapport) opretter en familiegrupperapport, der viser information om en gruppe forældre og deres børn.

### <u>Familiearkrapport</u>

[Tilføjelse:Familieark](wiki:Tilføjelse:Familieark) - Tredjepartstilføjelse.

### <u>Slægtskabsrapport</u>

[Slægtskabsrapport](wiki:Da:Gramps_6.0_brugsanvisning_-_Rapporter_-_del_6#Slægtskabsrapport) viser slægtskabet for den valgte person i henhold til det søgeniveau (højde, generationer ned), som brugeren har angivet.

### <u>Sidste ændringsrapport</u>

[Tilføjelse:Sidste ændring](wiki:Tilføjelse:Sidste_ændring) - Tredjepartstilføjelse.

### <u>Rapport over efterkommerlinjer</u>

[Addon:Rapport over efterkommerlinjer](wiki:Addon:Lines_of_Descendency_Report) - Tredjeparts-tilføjelse.

### <u>Medierapport</u>

[Addon:MediaReport](wiki:Addon:MediaReport) - Tredjeparts-tilføjelse.

### <u>Rapport over notelinks</u>

[Rapport over notelinks](wiki:Da:Gramps_6.0_brugsanvisning_-_Rapporter_-_del_6#Note_Link_Report) kontrollerer status for interne Gramps-links i noter.

### <u>Rapport over notelinks</u>

[Addon:Note_Report](wiki:Addon:Note_Report) - Tredjeparts-tilføjelse.

### <u>Rapport om antal forfædre</u>

[Rapport om antal forfædre](wiki:Da:Gramps_6.0_brugsanvisning_-_Rapporter_-_del_6#Rapport_om_antal_forfædre) viser antallet af forfædre til den aktive person. Formen er - generation x har y individer (z %).

### <u>PersonEverything-rapport</u>

[Addon:PersonEverything-rapport](wiki:Addon:PersonEverything_Report) - Tredjeparts-tilføjelse.

### <u>Stedsrapport</u>

[Stedsrapport](wiki:Da:Gramps_6.0_brugsanvisning_-_Rapporter_-_del_6#Stedsrapport) producerer en rapport i henhold til de steder, brugeren har valgt. Den vil liste relateret person og begivenhed til det valgte sted.

### <u>Optegnelsesrapport</u>

[Optegnelsesrapport](wiki:Da:Gramps_6.0_brugsanvisning_-_Rapporter_-_del_6#Optegnelsesrapport) viser en række interessante optegnelser (primært aldersrelaterede) i din database, såsom ældste levende person, yngste mor osv.

### <u>Optegnelsesdatabaserapport</u>

[Addon:Optegnelsesdatabaserapport](wiki:Addon:RepositoriesReport) - Tredjepartsudvidelse.

### <u>Optegnelsesindstillinger for lagringssteder</u>

[Addon:Optegnelsesindstillinger for lagringssteder](wiki:Addon:RepositoriesReport#Options_Report_Report) Tredjepartsudvidelse.

### <u><span title="Sandclock_Tree">Optegnelse over Sandclock-træ</span></u>

[Addon:GenealogyTree (underafsnit om Sandclock-træ) Rapport](wiki:Addon:GenealogyTree#Sandclock_tree) - Tredjepartsudvidelse.

### <u>Kilder og citater-rapport</u>

[Addon:Kilder Citations-rapport](wiki:Addon:SourcesCitationsReport) - Tredjeparts-tilføjelse.

### <u>Tag-rapport</u>

[Tag-rapport](wiki:Da:Gramps_6.0_brugsanvisning_-_Rapporter_-_del_6#Tag-rapport) viser primære objekter - personer, familier og noter - der matcher det valgte tag.

### <u>TinyTafel-rapport</u>

[Addon:TinyTafel](wiki:Addon:TinyTafel) - Tredjeparts-tilføjelse.

### <u>ToDo-rapport</u>

[Addon:ToDo-rapport](wiki:Addon:ToDoReport) - Tredjeparts-tilføjelse. {{-}}

## Websider

[Websider](wiki:Da:Gramps_6.0_brugsanvisning_-_Rapporter_-_del_7#Web_Pages) til brug på din personlige hjemmeside eller til at give væk som en separat rapport.

### <u>Fortalt hjemmeside</u>

Artiklen [om <strong>rapporten om fortalt hjemmeside</strong>](wiki:Da:Gramps_6.0_brugsanvisning_-_Rapporter_-_del_7#Fortalt_hjemmeside) beskriver rapporten med omfattende muligheder for at generere en hjemmeside (dvs. et sæt linkede websider) for en delmængde af udvalgte personer.

### <u>Webkalender</u>

[Webkalender](wiki:Da:Gramps_6.0_brugsanvisning_-_Rapporter_-_del_7#Webkalender) er en rapport, der opretter websider, der viser begivenheder for de udvalgte personer som et sæt månedlige kalendere.

### Network_Chart

- [Netværksdiagram](wiki:Addon:NetworkChart) Tredjepartstilføjelse.

### Se også

- [Web Solutions for Gramps](wiki:Web_Solutions_for_Gramps)

{{-}}

## Hurtig visninger

[Hurtig visninger](wiki:Da:Gramps_6.0_brugsanvisning_-_Rapporter_-_del_8#Hurtig_visninger) er rapporter, der er tilgængelige i kontekstmenuerne for personer, familier, ... De kan oprettes af brugere, selv med begrænset programmeringskendskab. {{-}}

[Category:Documentation](wiki:Category:Documentation) [Category:Plugins](wiki:Category:Plugins)
