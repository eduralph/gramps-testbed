---
title: Da:Gramps 6.0 brugsanvisning - Filtre
categories:
- Documentation
managed: false
source: wiki-scrape
wiki_revid: 129556
wiki_fetched_at: '2026-05-30T16:36:14Z'
lang: da
---

{{#vardefine:chapter\|16}} {{#vardefine:figure\|0}}

![[_media/DefineFilter-dialog-default-60-da.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}}  - dialog-vindue]]

Filtre giver Gramps mulighed for at begrænse operationer til en mindre del af en slægtsbog. Den filtrerede del af slægtsbogen deler en bestemt karakteristik til fælles. (f.eks. kvinder født i Frankrig mellem årene 1550 og 1575.) Filteret specificerer, hvilke karakteristika der er vigtige, og giver mulighed for at vælge værdier, der skal søges efter. (I eksemplet søger filteret efter personer af et bestemt køn, der har en begivenhed på et bestemt sted i løbet af en kort tidsperiode.)

Databaseforespørgsler kan være en udfordring at sammensætte uden fejl i syntaksen. Derfor leverer filtre strukturerede og forudtestede databaseforespørgsler, der skjuler det meste af syntakskompleksiteten, samtidig med at de giver nogle sikkerhedsnet for at undgå rutinemæssige fejl. Almindelige karakteristika, der bruges til filtrering, præsenteres normalt som "parameter"-felter i en formular. Derefter sammensætter formularen en korrekt skrevet forespørgsel omkring parameteren. Formularer med flere parameterfelter vil sammensætte komplekse forespørgsler.

Lister over alle de filtreringsforespørgselsregler, der i øjeblikket er defineret i Gramps. Hver af disse regler er tilgængelig til brug, når du opretter brugerdefinerede filtre.

Reglerne er opført efter deres [kategorier](wiki:Da:Gramps_6.0_brugsanvisning_-_Filtre#Which_filters_in_which_Category.3F).

## Filter vs. Søg <span id="Filter vs. Search"></span>

Der er to primære måder at finde data i Gramps: Søg og Filtrer.

- Søg bruger [Søgelinje](wiki:Da:Gramps_6.0_brugsanvisning_-_Hovedvindue#Søgelinje) over en listevisning (f.eks. Personer, Familier osv.).  
  [Søgelinje](wiki:Da:Gramps_6.0_brugsanvisning_-_Hovedvindue#Søgelinje) vises kun, når hele sidepanelet er lukket. Du kan vise eller skjule Gramplet-panelerne ved at ændre valget af menuerne eller .
- Brugerdefinerede filtre vælges fra pop op-menuer i Filter Gramplet, eksportindstillingen og i nogle rapporter. De kan bruges i kombination med Søg eller alene i sidepanelets/bundpanelets Gramplets. Brugerdefinerede filtre oprettes eller redigeres fra filteret Gramplet eller menuen .

(Der er også en grundlæggende *søg-mens-du-skriver* [Søg-boks](wiki:Gramps_6.0_Wiki_Manual_-_Navigation/da#Finding_records) til at navigere i det aktive postfokus i listevisning og objektvælgerlister.)

Søgning og filter fungerer helt anderledes, og det er nyttigt at forstå disse forskelle:

- *Søgning* - [Søgelinje](wiki:Da:Gramps_6.0_brugsanvisning_-_Hovedvindue#Søgelinje) gennemgår databasen, som den vises i rækkerne og kolonnerne på skærmen. Søgefunktionen er sandsynligvis den, du vil bruge det meste af tiden, da den er hurtig og mest ligetil. Men hastighed og enkelhed pålægger nogle begrænsninger (se nedenfor).

  
For eksempel, hvis du har Navnevisning i Indstillinger indstillet til at vise "Efternavn, Fornavn", kan du matche navne som "Smith, J", og alle de korrekte rækker vil matche. Hvis du ændrer den måde, navne vises på (i Indstillinger), kan du matche det format (for eksempel "John Smith").

![[_media/wiki:Da:Gramps_6.0_brugsanvisning_-_Hovedvindue#Søgelinje|[_media/MainWindow-SearchBar-sidebar-hidden-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Gramps Hovedvindue visende [Søgelinje]]]]

- *Filter* - Filtre bruger et mere avanceret system. Det er ikke begrænset til, hvad du ser på skærmen, men ser på de faktiske data i alle navnefelter i stedet for blot det, der vises i visningen. Indtastning af flere ord udfører sætningsmatchning for de fleste tekstfelter. Navnefilterlinjen er dog langt mere kraftfuld. Hvert ord i navnesøgningen håndteres separat, som om det var en undersøgning på de poster, der blev fundet med det forrige søgeord. Og den søger samtidig i ***alle*** navnefelterne.

F.eks. finder en navnesøgning på "geo r." i [eksempel-slægtsbog](wiki:Example.gramps)-databasen 5 personer: med varianten 'Jr.' & 'Sr.' som suffiks og 'George's som for- og mellemnavne. Eller søgning på "garn ski ph" finder Phoebe Emily, der har fødenavnet Zieliński og det alternative giftenavn Garner.

![[_media/da#tag|[_media/Sidebar-PeopleTreeView-Filter-TagDropDownList-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Gramps Filter SideBar til Personvisning - [Mærkat]] rullelisteeksempel]]

Filtre kan oprettes og styres fra menuen eller fra en speciel sidebar/bundbar Gramplet. Filter-grampletterne tillader nogle hurtige filtre, der ligner [Søgelinjen](wiki:Da:Gramps_6.0_brugsanvisning_-_Hovedvindue#Søgelinje), men alle filtre følger den sondring, der er beskrevet her.

Nogle yderligere punkter:

- Filteret vil også søge efter alternative og flere navne; [Søgelinjen](wiki:Da:Gramps_6.0_brugsanvisning_-_Hovedvindue#Søgelinje) ser kun på det primære navn... det, der vises i Person-visningen. Derfor kan et filter på "Smith" vise personer, der overfladisk set ikke ser ud til at matche. Men hvis du går i dybden med personens oplysninger med [Navneredigering](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_3#Name_Editor), kan du muligvis se, at de har et alternativt navn, der indeholder "smith".

<!-- -->

- Filteret tillader "regulære udtryk". Så du kan finde alle navne, der starter med "B" og slutter på "ship": "B.\*ship". Det kan du ikke gøre med [Søgelinjen](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window#Search_bar).
- Søgningen vil kun finde det, der er synligt. Hvis et navn eller en tekst er for stor til at se i listen nedenfor [Søgelinjen](wiki:Da:Gramps_6.0_brugsanvisning_-_Hovedvindue#Søgelinje), finder du det ikke. Dette er noget, du skal huske på, når du søger i noter. Det er bedst at bruge Filter til noter og andre lange tekstfelter.

<!-- -->

- Alle filtre bruger som standard ikke-sanskel i søgeresultater; "Ship" vil finde "ship", "SHIP" eller "ShIp". Som forklaret nedenfor under Regulære udtryk, giver brugen af ​​regulære udtryk i øjeblikket ikke mulighed for at ændre standardindstillingen.

### Se også

- [Find en post](wiki:Da:Gramps_6.0_brugsanvisning_-_Navigation#Find_en_post) - (også kendt som: "interaktiv søgning med indtastning" eller "søg mens du skriver")
- [Filter](wiki:Gramps_Glossary/da#filter) - en definition
- [Introduktion til filtre](wiki:Da:Gramps_6.0_brugsanvisning_-_Filtre) i Gramps Manual
- [Hvilke filterregler gælder i hvilken kategori?](wiki:Da:Gramps_6.0_brugsanvisning_-_Filtre#Hvilke_filterregler_gælder_i_hvilken_kategori?)
- [Filter](wiki:Filter)
- [Example filters](wiki:Example_filters) - Flertrinsfiltre (engelsk)
- [Rules](wiki:Gramps_Glossary/da#rule) - en definition
- [Addon list - Regler](wiki:6.0_Addons#Addon_List)
- [Expanding the Filter rulebook](wiki:Addon:Rule_expansions) med tilføjelser
- [Kategori: Filtre](wiki::Category:Filters) (engelsk)
- [Custom Filter migration](wiki:Template:Backup_Omissions) - sikkerhedskopiering af en Gramps slægtsbog inkluderer ikke nogen filtertilpasninger (engelsk)

{{-}}

## Regulære udtryk <span id="Regular Expressions"></span>

Et [Regulært udtryk](https://da.wikipedia.org/wiki/Regulært_udtryk) (engelsk: *regular expressions* ofte forkortet som *regex*, *regexp*) er en følge af tegn, der definerer et mønster til søgning/matchning.

Design af et effektivt søgemønster kan være formelbaseret. Ligesom matematiske formler kan et søgemønster hurtigt sammensættes, som finder en delmængde af poster, men gør det meget groft og langsomt. Elegante og effektive RegEx-fraser indsamles af optimeringseksperter i datamanipulationer. Der findes mange ressourcer (bøger, websteder, professionel træning) til RegEx-design og -strategi.

Gramps bruger RegEx som en matchningsmulighed, der kan aktiveres for brugerdefinerede filtre og i filtergrampletterne i hver kategorivisning.

RegEx-mønstermatchning er en avanceret funktion, og derfor er dens afkrydsningsfelt ikke markeret som standard. For brugerdefinerede filtre har hver enkelt regel et afkrydsningsfelt med muligheden i dialogboksen Rediger regel. Filtergrampletterne har også afkrydsningsfelter med muligheden , der tillader, at regexp-udtryk bruges direkte til at matche strenge i deres tekstbokse.

Hvis du for eksempel ledte efter et efternavn, der startede med et "B" og sluttede med "ship", kunne du bruge regulære udtryk til at beskrive dette mønster. Det ville være **`^B.*ship`**:

- **`^B`** angiver tekst, der starter med B
- **`.`** angiver et hvilket som helst enkelt tegn (bogstav, tal eller hvad som helst)
- **`*`** angiver nul eller flere af de foregående (i dette tilfælde et hvilket som helst enkelt tegn)
- **`ship`** matcher de nøjagtige bogstaver s, h, i, p i den rækkefølge.

Regulære udtryk er ret effektive, og der er mange muligheder. Vi bruger [Python Regular Expression](https://docs.python.org/3/library/re.html)-systemet, og vi vil dokumentere det her. Derudover kan du bruge enhver Python Regular Expression-ressource.

Gramps er i øjeblikket implementeret til at gøre al strengmatchning ufølsom over for store og små bogstaver (hvilket er det modsatte af den sædvanlige standard i Python). Der er i øjeblikket ingen nem måde at tilsidesætte denne adfærd med det relativt usædvanlige formål at matche strenge, der er indtastet i databasen i et bestemt format for store og små bogstaver. Regulære udtryk i Gramps giver i øjeblikket identiske resultater, uanset om målstrengen indtastes med store bogstaver, titelbogstaver, små bogstaver eller en blanding.

*mellemrum* - Udtrykket "mellemrum" bruges nedenfor til at betegne et eller flere tegn, som du ikke ser. For eksempel omfatter mellemrum tabulatorer, mellemrum og nye linjer.

Der er nogle tegn, der har en særlig betydning med regulære udtryk. De er:

- **<kode>. ^ \$ \* + ? { } \[ \] \\ \| ( )</kode>**  
  decimaltegn (punktum), cirkumflekstegn, dollartegn, stjerne, plustegn, spørgsmålstegn, venstre og højre krøllede parenteser, venstre og højre firkantede parenteser, omvendt skråstreg, lodret streg (pipe), venstre og højre parenteser

De kan bruges som beskrevet:

- '`.`' matcher et hvilket som helst tegn (bogstav, tal eller andet)
- '`^`' matcher starten af ​​teksten
- '`$`' matcher slutningen af ​​teksten
- '`*`' matcher nul eller flere af de foregående elementer
- '`+`' matcher et eller flere af de foregående elementer
- '`?`' matcher nul eller et af de foregående elementer (gør det valgfrit)
- '`{`' - definerer et antal match
- '`}`' - afslutter antallet af match
- '`[`' - starten af ​​sættet
- '`]`' - slutningen af ​​sættet
- '`\`' - næste tegn er en speciel sekvens
- '`|`' - eller
- '`(`' - starten af ​​en gruppe
- '`)`' - slutningen af en gruppe

Nogle af de specialsekvenser, der starter med '`\`', repræsenterer foruddefinerede sæt af tegn, der ofte er nyttige, såsom cifre, bogstaver eller alt, der ikke er mellemrum. Følgende foruddefinerede specialsekvenser er en delmængde af dem, der er tilgængelige.

- `\d` Matcher ethvert decimaltal; dette svarer til klassen `[0-9]`.
- `\D` Matcher ethvert ikke-cifret tegn; dette svarer til klassen `[^0-9]`.
- `\s` Matcher ethvert mellemrumstegn; dette svarer til klassen `[ \t\n\r\f\v]`.
- `\S` Matcher ethvert ikke-mellemrumstegn; dette svarer til klassen `[^ \t\n\r\f\v]`.

<!-- -->

- `\w` Matcher ethvert alfanumerisk tegn; dette svarer til klassen `[a-zA-Z0-9_]`.

<!-- -->

- `\W` Matcher ethvert ikke-alfanumerisk tegn; dette svarer til klassen `[^a-zA-Z0-9_]`.

Den mest komplicerede gentagne kvalifikator er `{m,n`, hvor `m` og `n` er decimaltal. Denne kvalifikator betyder, at der skal være mindst `m` gentagelser og højst `n`.

### Find alle definerede værdier eller mellemrum <span id="Find all defined values or blanks"></span>

<span id="regex_all">For at finde alle værdier, vil `(.|\s)*` matche: ethvert tegn eller ethvert mellemrumstegn; og nul eller flere gentagelser af disse.</span>

<span id="regex_null">For at finde tomme (blanke eller nul) strenge, leder `^.{0}$` fra starten af ​​matchen `^` efter ethvert tegn (undtagen ny linje) `.`, der forekommer præcis nul gange `{0}` før slutningen af ​​matchen `$`</span>

### Grupper og sæt <span id="Groups and Sets"></span>

Grupper er markeret med metategnene '`('`, '`)`'. '`(`' og '`)`' har stort set samme betydning som i matematiske udtryk; De grupperer de udtryk, der er indeholdt i dem, og du kan gentage indholdet af en gruppe med en gentagende kvalifikator, såsom `*, +, ? eller {m,n}`. For eksempel vil `(ab)*` matche nul eller flere gentagelser af `ab`.

Sæt er markeret med metategnene '`[`' og '`]`'.

Du kan tænke på grupper som en liste over alternativer adskilt af metategnet '`|`', hvor hvert alternativ består af et, flere eller nul tegn, og sæt som en liste over alternativer, hvor hvert alternativ er et enkelt tegn.

### Eksempler

- **`^B.*ship$`** - matcher al tekst, der starter med '`B`', efterfulgt af hvad som helst, og som slutter med '`ship`'.
  - matcher: **`Blankenship`**, **`Blueship`**, **`Beeship`**
  - matcher ikke: **`Blankenships`**
- **`^B.*ship`** - matcher al tekst, der starter med '`B`', efterfulgt af hvad som helst, efterfulgt af '`ship`' (kunne efterfølges af mere).
  - matcher: **`Blankenship`**, **`Blankenships`**, **`Blueship`**, **`Blueshipman`**, **`Beeship`**, **`Beeshipness`**
  - matcher ikke: **`Blankenschips`**

#### Almindelige variationer af et efternavn

Eksempel 1  
Ved at bruge udtrykket **`Eri(ch|ck|k|c)(ss|s)on`** matches følgende:

<!-- -->

    Erikson
    Eriksson
    Ericson
    Ericsson
    Erickson
    Ericksson
    Erichson
    Erichsson

**Forklaring**: På grund af følgende

- **`Eri`** = Eri
- **`(ch|ck|k|c)`** = gruppematchning **`ch`**, **`ck`**, **`k`** eller **`c`**. Den forsøger at lave det længste match først.
- **`(ss|s)`** = gruppematchning **`ss`** eller **`s`**. Den forsøger at lave det længste match først
- **`on`** = on

<hr>

Eksempel 2  
Ved at bruge udtrykket **`Ba(in|yn|m|n)bri(dge|cke|g(g|e|))`** matches følgende:

<!-- -->

    Bainbricke
    Bainbridge
    Bainbrig
    Bainbrigg
    Bambridge
    Banbrig
    Banbrige
    Baynbrige

**Forklaring:** På grund af følgende

- **`Ba`** = Ba
- **`(in|yn|m|n)`** = gruppematchning **in**, **yn**, **m** eller **n**. Den forsøger at lave det længste match først.
- **`bri`** = bri
- **`(dge|cke|g(g|e|))`** = gruppe der matcher **dge**, **cke** eller (**g** med **g**, **g** med **e** eller **g** uden noget)

<hr>

Eksempel 3  
Ved at bruge udtrykket **`n(es|oua|oai|o[iya]|a[iy])r(r|)(on|((e|)au(x|t|d|lt|)))`** matches følgende:

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
    noirault
    noiraut
    noirraux
    noirreau
    noirreaud
    nouarault
    noyraud
    noyrault

**Forklaring:** På grund af følgende

- **`n`** = n
- **`(es|oua|oai|set1|sæt2)`** = gruppe, der matcher **es**, **oua**, **oai**, **sæt1** eller **sæt2**
- **`sæt1`** er **`o[iya]`** = sæt matchende **o** OG **i**, **y** eller **a**. Med andre ord **oi**, **oy** eller **oa**
- **`sæt2`** er **`a[iy]`** = sæt der matcher **a** OG **i** eller **y**. Med andre ord **ai** eller **ay**
- **`r`** = r
- **`(r|)`** = gruppematchning **r** eller ingenting
- **`(on|(undergruppe1)`** = gruppematchning **on** eller **undergruppe1**.
- **undergruppe1** er gruppematchning (**undergruppe2 au undergruppe3**)
- **undergruppe2** er **(e\|)** = gruppematchning **e** eller ingenting
- **`au`** = au
- **undergruppe3** er **(x\|t\|d\|lt)** = gruppematchning **x**, **t**, **d** eller **lt**

#### Test af regulære udtryk

Testværktøjer til regulære udtryk kan findes online via Google. <https://www.regexr.com/> er enkelt og bekvemt

### Se også

Regulære udtryk har været i vid udstrækning brugt i computerindustrien siden 1950'erne. Men de er "ekspertværktøjer", der er designet til kraft og effektivitet snarere end intuitivitet. Som et resultat er der blevet udviklet mange ressourcer på nettet.

Nogle af disse ressourcer har fremragende vejledninger. Nogle har snydeark. Nogle har "sandkasser", hvor regulære udtryk kan udforskes i realtid.

Et udpluk af RegEx-referencewebsteder:

- [1](http://rexegg.com/rexegg.com) (vejledninger)
- [2](https://www.regular-expressions.info/RegexBuddy)
- [3](https://regex101.com/regex101.com) (sandkasse med feedback)

{{-}}

## Brugerdefinerede filtre <span id="Custom Filters"></span>

Du kan udføre en betydelig mængde udvælgelse af personer, begivenheder, steder osv. blot ved at bruge sidepanel filter-Gramplet i Person-, Begivenheds-, Sted-osv.-visninger; Bemærk dog, at indstillingen 'Brug regulære udtryk' kun **virker med bestemte felter** i hver visning.

Hvis filter-Grampletten i sidepanelet ikke er tilstrækkelig til dit formål, skal du oprette brugerdefinerede filtre. <span id="CategoryName Filters dialog"></span>

### <kategori> Filter editor dialog

Der er en -mulighed i menuen for hver kategori. (dvs. '<Kategori>' er en pladsholder. Vi mener, at den står for den person, begivenhed, kilder eller andre kategorier, der i øjeblikket er aktive.) Denne dialogboks viser en liste over alle de brugerdefinerede filtre, der er specifikke for den aktuelle kategori, og giver dig mulighed for at administrere disse brugerdefinerede filtre. (Ligesom [dialogboksen Organiser mærkater](wiki:Da:Gramps_6.0_brugsanvisning_-_Filtre#Vindue_til_organisering_af_mærkater) tillader administration af mærkater.) Der er ingen mulighed for at organisere de brugerdefinerede filtre i alle kategorier samtidigt.

![[_media/PersonFilters-dialog-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Personfiltre - dialogboks - eksempel]]

For at oprette nye eller vise tidligere oprettede brugerdefinerede filtre skal du bruge editor-dialogboksen , hvor navnet *<kategori>* ændres baseret på den kategori, der aktuelt er valgt i Navigatoren:

-  Personfiltre

-  Familiefiltre

-  Begivenhedsfiltre

-  Stedfiltre

-  Kildefiltre

-  Kildehenvisningsfiltre

-  Arkivfiltre

-  Mediefiltre

-  Notefiltre

Når du er i dialogboksen , har du følgende muligheder fra ikonerne i højre side:

-  

  
viser dialogboksen og tilføjer et nyt (endnu unavngivet) brugerdefineret filterframework.

-  

  
åbner dialogboksen og indlæser dit eksisterende brugerdefinerede filter til redigering.

-  

  
laver en nøjagtig kopi af det valgte filter

-  

  
åbner resultatdialogboksen , der indeholder en liste over matches efter en vellykket test. Hvis filtertesten er ugyldig, kan der vises en fejl i stedet.

-  :

  
fjerner det valgte filter fra Gramps-samlingen af ​​brugerdefinerede filtre.

{{-}}

#### Filtertestdialog

![[_media/FilterTest-results-for-TestTheSelectedFilter-button-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Filtertest - eksempel på resultatliste fra personfiltre]]

Resultatlisten for en vellykket -dialogboks kan være tom, og et gyldigt brugerdefineret filter matcher muligvis ikke nogen poster.

{{-}}

### Definer filter-dialog

![[_media/DefineFilter-dialog-default-60-da.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Definer filter - dialogboks - standard]]

Dialogboksen giver dig mulighed for at oprette brugerdefinerede filtre, der kan bruges til at vælge personer, der er inkluderet i rapporter, eksport og andre værktøjer og hjælpeprogrammer. Dette er faktisk et meget kraftfuldt værktøj inden for genealogisk analyse.

For at liste alle de filtre (hvis nogen), du tidligere har defineret, skal du åbne dialogboksen fra:

- Filtre i sidepanel/bundpanel
- I de fleste kategorier via menuen , som åbner dialogboksen , hvor du kan vælge knappen eller knappen .

I afsnittet **Definition** skal du skrive for dit nye filter og tilføje en , der kan hjælpe dig med at identificere dette filter i fremtiden. Tilføj så mange regler til , som du ønsker, ved hjælp af knappen .

<span ID="multiple_rule_options">Hvis filteret har mere end én regel, skal du vælge en af ​​ fra rullelisten, som giver dig mulighed for at vælge, om

- **Alle regler skal gælde**(standard)
- Mindst én regel skal gælde
- Præcis én regel skal gælde

for at filteret kan generere et match. Hvis dit filter kun har én regel, har dette valg ingen effekt.

- Vælg for at invertere filterreglen. For eksempel vil invertering af reglen **"har en fælles forfader med I1"** matche alle, der ikke har en fælles forfader med den pågældende person). (Markeringsfeltet er ikke markeret som standard)</span>

{{-}}

### Tilføj regel-dialog

![[_media/AddRule-selector-dialog-PersonFilters-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Tilføj regel" - vælgerdialog - tilgængelig for personfiltre - eksempel]]

For at definere et nyt filter skal du klikke på knappen fra dialogboksen , da dette åbner dialogboksen .

Ruden i venstre side viser tilgængelige filterregler arrangeret efter deres kategorier i et udvideligt træ.

For detaljeret reference til filterregler kan du enten bruge søgefeltet til at finde reglen eller:

- Klik på pilene for at folde/udfolde den relevante kategori.
- Vælg reglen fra træet ved at klikke på dens navn. Højre side viser navnet, beskrivelsen og værdierne for den aktuelt valgte regel.

Når du er tilfreds med dit regelvalg og dets værdier, skal du klikke på for at tilføje denne regel til regellisten for det aktuelt redigerede filter. Hvis du klikker på , afbrydes tilføjelsen af ​​reglen til filteret.

Se også [Hvilke filtre i hvilken kategori?](wiki:Da:Gramps_6.0_brugsanvisning_-_Filtre#Hvilke_filtre_i_hvilken_kategori?) {{-}}

<span id="Hvilke filtre i hvilken kategori?">

## Hvilke filterregler gælder i hvilken kategori?

Afhængigt af den anvendte [Kategori](wiki:Da:Gramps_6.0_brugsanvisning_-_Kategorier), vil du få et andet sæt [filter](wiki:Da:Gramps_6.0_brugsanvisning_-_Gramplets#Filter) regler. Se også [Oversigt over Gramplets](wiki:Da:Gramps_6.0_brugsanvisning_-_Gramplets#Oversigt_over_Gramplets).

\*; Kontrolpanelkategori: ingen filterregler tilgængelige

\*; Kategori for personer, relationer og diagrammer: regler for [Forfædrefiltre](#Forfædrefiltre), [Kildehenvisning-filtre](#Kildehenvisning-filtre), [Efterkommerfiltre](#Efterkommerfiltre), [Begivenhedsfiltre](#Begivenhedsfiltre), [Familiefiltre](#Familiefiltre), [Generelle filtre](#Generelle_filtre), og [Slægtsforholdfiltre](#Slægtsforholdfiltre).

\*; Kategori for familier: regler for [Børnefiltre](#Børnefiltre), [Kildehenvisning-filtre](#Kildehenvisning-filtre), [Begivenhedsfiltre](#Begivenhedsfiltre), [Faderfiltre](#Faderfiltre), [Generelle filtre](#Generelle_filtre), og [Moderfiltre](#Moderfiltre)

\*; Kategori for tavler: regler for [Forfædrefiltre](#Forfædrefiltre), [Kildehenvisning-filtre](#Kildehenvisning-filtre), [Efterkommerfiltre](#Efterkommerfiltre), [Begivenhedsfiltre](#Begivenhedsfiltre), [Familiefiltre](#Familiefiltre), [Generelle filtre](#Generelle_filtre) og [Slægtsforholdfiltre](#Slægtsforholdfiltre)

\*; Begivenheder og Mediekategori: regler for [Kildehenvisning-filtre](#Kildehenvisning-filtre) og [Generelle filtre](#Generelle_filtre).

\*; Stederkategori: regler for [Kildehenvisning-filtre](#Kildehenvisning-filtre), [Generelle filtre](#Generelle_filtre) og [Stedfiltre](#Stedfiltre).

\*; Geografisk kategori: regler for [Forfædrefiltre](#Forfædrefiltre), [Kildehenvisning-filtre](#Kildehenvisning-filtre), [Efterkommerfiltre](#Efterkommerfiltre), [Begivenhedsfiltre](#Begivenhedsfiltre), [Family filters](#Family_filters), [Generelle filtre](#Generelle_filtre) og [Slægtsforholdfiltre](#Slægtsforholdfiltre).

\*; Kilder, arkiver og noter kategori: regler for kun [General filters](#General_filters) tilgængelige

\*; Kildehenvisning kategori: regler for [Generelle filtre](#Generelle_filtre) og [Kildefiltre](#Kildefiltre)

\*; Arkiver kategori: regler for [Generelle filtre](#Generelle_filtre)

\*; Mediekategori: regler for [Kildehenvisning-filtre](#Kildehenvisning-filtre) og [Generelle filtre](#Generelle_filtre)

\*; Noter Kategori: regler for [Generelle filtre](#Generelle_filtre) {{-}}

## Forfædrefiltre

Denne regelkategori inkluderer følgende regler, der matcher personer baseret på deres forfædreforhold til andre personer:

### Forfædre til <filter> matcher

Denne regel matcher personer, der er forfædre til en person, der matches af det angivne filter. Det angivne filternavn skal vælges fra menuen.

### Forfædre til <person>

Denne regel matcher personer, der er forfædre til den angivne person. Indstillingen Inkluder bestemmer, om den angivne person skal betragtes som sin egen forfader (nyttigt til at opbygge rapporter). Du kan enten indtaste ID'et i et tekstfelt eller vælge en person fra listen ved at klikke på knappen . I sidstnævnte tilfælde vises ID'et i tekstfeltet, efter at valget er foretaget.

### Forfædre til <person> mindst <N> generationer væk

Denne regel matcher personer, der er forfædre til den angivne person og er mindst N generationer væk fra den person i deres slægt. For eksempel, hvis du bruger denne regel med værdien 2 for antallet af generationer, vil det matche bedsteforældre, oldeforældre osv., men ikke forældrene til den angivne person.

### Forfader til <person> ikke mere end <N> generationer væk

Denne regel matcher personer, der er forfædre til den angivne person og ikke er mere end N generationer væk fra den person i deres slægt. For eksempel, hvis du bruger denne regel med værdien 2 for antallet af generationer, vil det matche forældre og bedsteforældre, men ikke oldeforældre osv. til den angivne person.

### Forfader til bogmærkede personer ikke mere end <N> generationer væk

Matcher det antal generationer, der kræves for forfædre (defineret af <n>) for hver person på bogmærkelisten.

### Forfader til standardpersonen ikke mere end <N> generationer væk

"Standardpersonen" er den person, der er defineret som "Hjemmeperson". ("Standard" er et ældre udtryk i Gramps, der forårsagede mindre forvirring, da ordet bruges i så mange forskellige dele af wikien til at beskrive forskellige ting.)

### Duplikerede forfædre til <person>

Matcher personer, der er forfædre to gange eller mere til en bestemt person

### Personer med en fælles forfader med <filter> match

Denne regel matcher personer, der har fælles forfædre, med en person, der matches af det angivne filter. Det angivne filternavn skal vælges fra menuen.

### Personer med en fælles forfader med <person>

Denne regel matcher personer, der har fælles forfædre med den angivne person.

## Børnefiltre

Denne regelkategori finder familier med børn, der matcher reglen:

### Familier med børn med id, der indeholder <tekst>

Matcher familier, hvor barnet har et angivet Gramps-ID

### Familier med børn med <navn>

Matcher familier, hvor barnet har et angivet (delvis) navn

### Familier med tvillinger

Matcher familier med to (eller flere) børn, der har en ['Fødsels'-rolle for forholdet til moderen](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1#Child_Reference_Editor) og samme fødselsdato. {{-}}

## Kildehenvisning-filtre

Disse filterregler er afhængige af den valgte kategori:

- [Personer og Slægtsforhold](#Personer_og_Slægtsforhold_1)
- [Familier](#Familier_1)
- [Begivenheder](#Begivenheder_1)
- [Steder](#Steder_1)
- [Medier](#Medier_1)

<span id="Personer og Slægtsforhold_1">

### Personer og Slægtsforhold

</span>

Denne kategori indeholder følgende kildehenvisnings- og kilderegler:

#### Personer med <antal> kilder

Matcher personer med et bestemt antal elementer i kilden. Værdier: Antal forekomster -- Tallet skal være større end/mindre/lig med

#### Personer med <kildehenvisning>

Matcher personer med en kildehenvisning af en bestemt værdi

#### Personer med <kilde>

Matcher personer, der har en bestemt kilde. værdier: Kilde-ID

====Person med mindst én direkte kilde \>= <konfidensniveau>==== Matcher personer, der har en kildehenvisning knyttet direkte til Person-objektet. Kildehenvisninger til Familien eller sekundære objekter såsom Begivenheder ignoreres.

Den minimale acceptable konfidensgrænse kan vælges: Meget lav, Lav, Normal, Høj, Meget høj

\<span id="Familier_1\>

### Familier

</span>

Denne kategori inkluderer følgende kildehenvisnings- og kilderegler:

#### Familier med <antal> kilder

Matcher familier med et bestemt antal elementer i kilden. Værdier: Antal forekomster -- Tallet skal være større end/mindre/lig med

====Familier med mindst én direkte kilde \>= <konfidensniveau>==== Matcher familier, der har en kildehenvisning knyttet direkte til Familie-objektet. Kildehenvisninger til Personen eller sekundære objekter såsom Begivenheder ignoreres.

Den minimale acceptable konfidensgrænse kan vælges: Meget lav, Lav, Normal, Høj, Meget høj

#### Familier med <kildehenvisning>

Matcher familier med en kildehenvisning af en bestemt værdi

#### Familier med <kilde>

Matcher familier, der har en bestemt kilde. værdier: Kilde-ID

<span id="Begivenheder_1">

### Begivenheder

</span>

Denne kategori indeholder følgende kildehenvisnings- og kilderegler:

#### Begivenheder med <antal> kilde

Matcher begivenheder med et bestemt antal elementer i kilden. Værdier: Antal forekomster -- Tallet skal være større end/mindre end/lig med

==== Begivenheder med mindst én direkte kilde \>= <konfidensniveau>==== Matcher begivenheder, der har en kildehenvisning knyttet direkte til begivenhedsobjektet. Kildehenvisninger til familien eller sekundære objekter såsom noter ignoreres.

Den minimale acceptable konfidensgrænse kan vælges: Meget lav, Lav, Normal, Høj, Meget høj

#### Begivenheder med kilde, der matcher <kildefilteret>

Matcher begivenheder med enhver kilde (eller kildehenvisning under en kilde), der matcher en specificeret kildefilter og er direkte knyttet til begivenhedsobjektet. Kilder, der er knyttet til begivenhedens medier eller attributter, ignoreres.

#### Begivenheder med <kildehenvisning>

Matcher begivenheder med en kildehenvisning af en bestemt værdi

<span id="Steder_1">

### Steder

</span>

Denne kategori inkluderer følgende kildehenvisnings- og kilderegler:

#### Sted med <antal> kilder

Matcher steder med et bestemt antal elementer i kilden. Værdier: Antal forekomster -- Tallet skal være større end/mindre/lig med

====Sted med en direkte kilde \>= <konfidensniveau>==== Matcher steder, der har en kildehenvisning knyttet direkte til stedsobjektet. Kildehenvisninger til sekundære objekter såsom noter ignoreres.

Den minimale acceptable konfidensgrænse kan vælges: Meget lav, Lav, Normal, Høj, Meget høj

#### Sted med <kildehenvisning>

Matcher steder med en kildehenvisning af en bestemt værdi

#### Steder med <kilde>

Matcher steder, der har en bestemt kilde. værdier: Kilde-ID

<span id="Medier_1">

### Medier

</span>

Denne kategori indeholder følgende kildehenvisnings- og kilderegler:

#### Medier med <antal> kilder

Matcher medier med et bestemt antal elementer i kilden. Værdier: Antal forekomster -- Tallet skal være større end/mindre/lig med

====Medier med en direkte kilde \>= <konfidensniveau>==== Matcher medier, der har en kildehenvisning knyttet direkte til medieobjektet. Kildehenvisninger til de sekundære objekter, såsom begivenheder, ignoreres.

Den minimale acceptable konfidensgrænse kan vælges: Meget lav, Lav, Normal, Høj, Meget høj

#### Medier med <kildehenvisning>

Matcher medier med en kildehenvisning af en bestemt værdi

#### Medier med <kilde>

Matcher medier, der har en bestemt kilde. værdier: Kilde-ID {{-}}

## Efterkommerfiltre

Denne kategori for efterkommerfiltre inkluderer følgende regler, der matcher personer baseret på deres efterkommerrelationer til andre personer:

### Efterkommer familiemedlem af <filter> match

Matcher personer, der er efterkommere eller ægtefælle til enhver, der matches af et filter

### Efterkommer familiemedlem af <person>

Denne regel matcher ikke kun personer, der er efterkommere af den angivne person, men også disse efterkommeres ægtefæller.

### Efterkommer af <filter> match

Denne regel matcher personer, der er efterkommere af en person, der matches af det angivne filter. Det angivne filternavn skal vælges fra menuen.

### Efterkommer af <person>

Denne regel matcher personer, der er efterkommere af den angivne person. Indstillingen Inkluder bestemmer, om den angivne person skal betragtes som sin egen efterkommer (nyttigt til at opbygge rapporter). Du kan enten indtaste ID'et i et tekstfelt eller vælge en person fra listen ved at klikke på knappen . I sidstnævnte tilfælde vises ID'et i tekstfeltet, efter at valget er foretaget.

### Efterkommer af <person> mindst <N> generationer væk

Denne regel matcher personer, der er efterkommere af den angivne person og er mindst N generationer væk fra den person i deres slægt. For eksempel vil brug af denne regel med værdien 2 for antallet af generationer matche børnebørn, oldebørn osv., men ikke børnene af den angivne person.

### Efterkommer af <person> ikke mere end <N> generationer væk

Denne regel matcher personer, der er efterkommere af den angivne person og er højst N generationer væk fra den person i deres slægt. For eksempel vil brug af denne regel med værdien 2 for antallet af generationer matche børn og børnebørn, men ikke oldebørn osv. af den angivne person. {{-}}

## Begivenhedsfiltre

### Begivenhedsmatchningsparametre

Generel filterregel, der matcher begivenheder med bestemte parametre:

- 

- 

- 

- 

- 

Tilbyder også muligheden for at .

### Disse filterregler er afhængige af valgt kategori

- [Personer og Slægtsforhold](#Personer_og_Slægtsforhold_2)
- [Familier](#Familier_2)

<span id="Personer og Slægtsforhold_2">

### Personer og Slægtsforhold

</span>

Denne kategori indeholder følgende regler, der matcher personer baseret på deres registrerede begivenheder:

#### Familier med ufuldstændige begivenheder

Denne regel matcher personer, der mangler dato eller sted i enhver familiebegivenhed i enhver af deres familier.

#### Personer med ufuldstændige begivenheder

Denne regel matcher personer, der mangler dato eller sted i en personlig begivenhed.

#### Personer med <fødselsdata>

Denne regel matcher personer, hvis fødselsbegivenhed matcher angivne værdier for Dato, Sted og Beskrivelse. Reglen returnerer et match, selvom personens fødselsbegivenhed matcher værdien delvist. Matchreglerne er ikke-skelværdier for store og små bogstaver. For eksempel vil alle, der er født i Sverige, blive matchet af reglen ved hjælp af værdien "sw" for stedet. Reglen returnerer et match, hvis, og kun hvis, alle ikke-tomme værdier (delvist) matches af en persons fødsel. For kun at bruge én værdi skal du lade de andre værdier være tomme.

#### Personer med <dødsdata>

Denne regel matcher personer, hvis dødsbegivenhed matcher angivne værdier for Dato, Sted og Beskrivelse. Reglen returnerer et match, selvom personens dødsbegivenhed matcher værdien delvist. Matchreglerne er ikke-skelværdier for store og små bogstaver. For eksempel vil alle, der døde i Sverige, blive matchet af reglen ved hjælp af værdien "sw" for stedet. Reglen returnerer et match, hvis og kun hvis alle ikke-tomme værdier (delvist) matches af en persons død. Hvis du kun vil bruge én værdi, skal du lade de andre værdier være tomme.

#### Personer med familien <begivenhed>

Denne regel matcher personer, der har en familiebegivenhed, der matcher angivne værdier for begivenhedstype, dato, sted og beskrivelse. Reglen returnerer et match, selvom personens begivenhed matcher værdien delvist. Matchreglerne skelner ikke mellem store og små bogstaver. For eksempel vil enhver, der blev gift i Sverige, blive matchet af reglen ved hjælp af ægteskabshændelsen og værdien "sw" for stedet. Familiebegivenhederne skal vælges fra en rullemenu. Reglen returnerer et match, hvis og kun hvis alle ikke-tomme værdier (delvist) matches af den personlige begivenhed. Hvis du kun vil bruge én værdi, skal du lade de andre værdier være tomme.

#### Personer med den personlige <begivenhed>

Denne regel matcher personer, der har en personlig begivenhed, der matcher angivne værdier for begivenhedstype, dato, sted og beskrivelse. Reglen returnerer et match, selvom personens begivenhed delvist matcher værdien. Matchreglerne skelner ikke mellem store og små bogstaver. For eksempel vil enhver, der dimitterede i Sverige, blive matchet af reglen ved hjælp af gradueringsbegivenheden og værdien "sw" for stedet. De personlige begivenheder skal vælges fra en rullemenu. Reglen returnerer et match, hvis, og kun hvis, alle ikke-tomme værdier (delvist) matches af den personlige begivenhed. For kun at bruge én værdi skal du lade de andre værdier være tomme.

#### Personer med begivenheder, der matcher <begivenhedsfilter>

Matcher personer, der har begivenheder, der matcher et bestemt begivenhedsfilter. Værdier: Navn på begivenhedsfilter.

#### Vidner

Denne regel matcher personer, der er i et "Vidne" [Begivenhedsrolle](wiki:Gramps_Glossary/da#event_role). Hvis begivenhedstypen (personlig eller familie) er angivet, søges der kun efter begivenheder af denne type.

##### Se også

[FilterRules](wiki:Addon:Rule_expansions#FilterRules_:_Plugin_Manager_Rulebook_Collection) : Plugin Manager Regelbogssamlingen indeholder regler til at søge efter personer eller familier med begivenheder med specifikke roller:

- [Personer med begivenheder med en valgt rolle](wiki:Addon:Rule_expansions#People_with_events_with_a_selected_role) : Regel for personfilter
- [Familier med begivenheder med en valgt rolle](wiki:Addon:Rule_expansions#Families_with_Events_with_a_selected_role) : Regel for familiefilter

<span id="Familier_2">

### Familier

</span>

Denne kategori indeholder følgende regler, der matcher familier baseret på deres registrerede begivenheder:

#### Familier med <begivenhed>

Denne regel matcher familier, der har en begivenhed, der matcher angivne værdier for begivenhedstype, dato, sted og beskrivelse. Reglen returnerer et match, selvom personens begivenhed delvist matcher værdien. Matchreglerne skelner ikke mellem store og små bogstaver. For eksempel vil enhver, der blev gift i Sverige, blive matchet af reglen ved hjælp af ægteskabshændelsen og værdien "sw" for stedet. Familiehændelser skal vælges fra en rullemenu. Reglen returnerer et match, hvis, og kun hvis, alle ikke-tomme værdier (delvist) matches af den personlige begivenhed. Hvis du kun vil bruge én værdi, skal du lade de andre værdier være tomme. {{-}}

## Familiefiltre

Denne kategori indeholder følgende regler, der matcher personer baseret på deres familieforhold:

### Adopterede personer

Denne regel matcher adopterede personer.

### Børn af <filter> matcher

Denne regel matcher personer, for hvem en af ​​forældrene matches af det angivne filter. Det angivne filternavn skal vælges fra menuen.

### Forældre af <filter> matcher

Denne regel matcher personer, hvis barn matches af det angivne filter. Det angivne filternavn skal vælges fra menuen.

### Personer, der mangler forældre

Matcher personer, der er børn i en familie med færre end to forældre eller ikke er børn i nogen familie.

### Personer med børn

Denne regel matcher personer med børn.

### Personer med flere vielsesregistre

Denne regel matcher personer med mere end én ægtefælle.

### Personer uden vielsesregistre

Denne regel matcher personer uden ægtefæller.

### Personer med <forhold>

Denne regel matcher personer med et bestemt forhold. Relationen skal matche den type, der er valgt i menuen. Antallet af relationer og antallet af børn kan eventuelt angives. Reglen returnerer et match, hvis, og kun hvis, alle ikke-tomme værdier (delvist) matches af en persons relation. For kun at bruge én værdi skal de andre værdier være tomme.

### Søskende af <filter> match

Denne regel matcher personer, hvis søskende matches af det angivne filter. Det angivne filternavn skal vælges i menuen.

### Ægtefæller af <filter> match

Denne regel matcher personer, der er gift med en person, der matches af det angivne filter. Det angivne filternavn skal vælges i menuen. {{-}}

## Faderfiltre

Denne regelkategori finder familier med fædre, der matcher reglen:

### Familier med far med et id, der indeholder <tekst>

Matcher familier, hvis far har et angivet bedstefar-ID

### Familier med far med <navn>

Matcher familier, hvis far har et angivet (delvis) navn {{-}}

## Generelle filtre

Disse filterregler er afhængige af valgt kategori:

- [Personer og Slægtsforhold](#Personer_og_Slægtsforhold_3)
- [Familier](#Familier_3)
- [Begivenheder](#Begivenheder_3)
- [Steder](#Steder_3)
- [Kilder](#Kilder_3)
- [Kildehenvisning](#Kildehenvisning_3)
- [Arkiver](#Arkiver_3)
- [Medier](#Medier_3)
- [Noter](#Noter_3)

<span id="Personer og Slægtsforhold_3">

### Personer og Slægtsforhold

</span>

Denne kategori indeholder følgende generelle regler:

#### Bogmærkede personer

Matcher personerne på bogmærkelisten.

<span id="Standardperson">

#### Hjemmeperson

</span> Matcher [Hjemmeperson](wiki:Gramps_Glossary/da#home_person).

#### Frakoblede personer

Matcher personer, der ikke har familieforhold til nogen anden person i databasen.

#### Alle

Matcher alle i slægtsbogsdatabasen.

#### Kvinder

Matcher alle kvinder.

#### Mænd

Matcher alle mænd.

#### Personer med <count> noter

Matcher personer med et bestemt antal noter: Værdier: Antal forekomster -- Tallet skal være større end/mindre/lig med

#### Personer med noter, der indeholder <text>

Matcher personer, hvis noter indeholder tekst, der matcher et regulært udtryk

#### Personer markeret som private

Matcher personer, der er angivet som private.

#### Personer, der matcher <filter>

Matcher personer, der matcher det angivne filternavn. Værdier: Filternavn. Det angivne filternavn skal vælges fra menuen.

#### Personer, der ikke er markeret som private

Matcher personer, der ikke er angivet som private

#### Personer sandsynligvis i live

Matcher personer uden indikationer af død inden en bestemt dato. Hvis den angivne værdi for "På dato" er tom, skal du sammenligne med "i dag()". Sandsynligvis i live tager højde for de datotilnærmelser og levetidslængder, der er angivet i indstillingerne.

For mere detaljerede oplysninger om denne beregning, læs afsnittet "[Sandsynligvis i live](wiki:Gramps_6.0_Wiki_Manual_-_Probably_Alive)".

- [Sandsynligvis i live-filter](wiki:Gramps_6.0_Wiki_Manual_-_Probably_Alive#Probably_Alive_Filter)

#### Personer med <antal> LDS-begivenheder

Matcher personer med et bestemt antal LDS-begivenheder. Værdier: Antal forekomster -- Tallet skal være større end/mindre end/lig med

#### Personer med <count> adresser

Matcher personer med et bestemt antal personlige adresser. Værdier: Antal forekomster -- Tallet skal være større end/mindre end/lig med

#### Personer med <count> tilknytninger

Matcher personer med et bestemt antal tilknytninger. Værdier: Antal forekomster -- Tallet skal være større end/mindre end/lig med

#### Personer med <count> medier

Matcher personer med et bestemt antal elementer i galleriet. Værdier: Antal forekomster -- Tallet skal være større end/mindre end/lig med

#### Personer med id, der indeholder <tekst>

Matcher personer, hvis Gramps-ID matcher det regulære udtryk

#### Personer med et navn, der matcher <tekst>

Matcher personers navne, der indeholder en delstreng eller matcher et [regulært udtryk](wiki:Gramps_Glossary/da#regex)

#### Personer med et kaldenavn

Matcher personer med et kaldenavn

#### Personer med et alternativt navn

Matcher personer med et alternativt navn

#### Personer med ufuldstændige navne

Matcher personer, hvis for- eller efternavn mangler.

#### Personer med poster, der indeholder <delstreng>

Matcher personer, hvis poster indeholder tekst, der matcher en delstreng. Værdier: Delstreng -- Store/småbogstavsfølsom eller ej -- Matcher regulære udtryk eller ej

*Filteret søger ikke i noter.*

#### Personer med <Navnetypen>

Matcher personer med en bestemt navnetype

#### Personer med <Efternavnsoprindelsestypen>

Matcher personer med en efternavnsoprindelse

#### Personer med <navn>

![[_media/Rule_Person_with_the_name-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Personer med -filterreglen - med f.eks. RegEx-søgning efter ikke-blanke felter]] Matcher personer med et angivet (delvis) navn.

Værdier:

- Fornavn
- Fulde efternavn: søger præfiks, efternavn og forbindelser med flere efternavne
- Titel
- Suffiks
- Kaldenavn
- Kælenavn
- Præfiks
- Enkelt efternavn: søger kun i [Foretrukket navn](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1#Preferred_name_section)
- Forbindelse: søg i forbindelser efter [flere efternavne](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1#Multiple_Surnames)
- Patronym
- Efternavn

Valgmuligheder:

- Brug [regulære udtryk](wiki:Gramps_Glossary/da#regex) - eksemplet på skærmbilledet bruger udtrykket `(.|\s)*\S(.|\s)*` til at finde ikke-tomme felter præfikser
- Skelner mellem store og små bogstaver

{{-}}

##### Se også

- [Personer med et navn, der matcher <text>](wiki:Gramps_6.0_Wiki_Manual_-_Filters#People_with_a_name_matching_.3Ctext.3E)
- [Personer med et kaldenavn](wiki:Gramps_6.0_Wiki_Manual_-_Filters#People_with_a_nickname)
- [Personer med et alternativt navn](wiki:Gramps_6.0_Wiki_Manual_-_Filters#People_with_an_alternate_name)
- [Personer med ufuldstændige navne](wiki:Gramps_6.0_Wiki_Manual_-_Filters#People_with_incomplete_names)
- [Personer med <Name-typen>](wiki:Gramps_6.0_Wiki_Manual_-_Filters#People_with_the_.3CName_type.3E)
- [Personer med <Surname oprindelsestype>](wiki:Gramps_6.0_Wiki_Manual_-_Filters#People_with_the_.3CSurname_origin_type.3E)
- [Personer med <name>](wiki:Gramps_6.0_Wiki_Manual_-_Filters#People_with_the_.3Cname.3E)
- [Soundex-match af Personer med <name>](wiki:Gramps_6.0_Wiki_Manual_-_Filters#Soundex_match_of_People_with_the_.3Cname.3E)
- [Familier med barn med <name>](wiki:Gramps_6.0_Wiki_Manual_-_Filters#Families_with_child_with_the_.3Cname.3E)
- [Familier med far med <navn>](wiki:Gramps_6.0_Wiki_Manual_-_Filters#Families_with_father_with_the_.3Cname.3E)
- [Familier med mor med <navn>](wiki:Gramps_6.0_Wiki_Manual_-_Filters#Families_with_mother_with_the_.3Cname.3E)
- [Søgefelt](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window#Search_bar) (Navne indeholder, Navn indeholder ikke)
- [Personfilter](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#People_Filter) gramplet (Navn)
- Isotammi [Personfilter+](wiki:Addon:Isotammi_addons#Filter.2B) addon gramplet (Navn)
- Isotammi [SuperTool](wiki:Addon:Isotammi_addons#SuperTool) forespørgselsværktøj (kategori Personer)

{{-}}

#### Personer med <mærkat>

Matcher personer med et mærkat med en bestemt værdi. Værdier: Mærkatnavn.

#### Personer med familie <attribut>

Matcher personer med familieattributten med en bestemt værdi. Brug RegEx-mønstermatchning til at søge efter [all values](wiki:Gramps_6.0_Wiki_Manual_-_Filters#regex_all) eller attributter, der er blevet [efterladt blanke](wiki:Gramps_6.0_Wiki_Manual_-_Filters#regex_null). Værdier: Familieattribut: Identifikationsnummer -- Alder ...

#### Personer med den personlige <attribut>

Matcher personer med den personlige attribut med en bestemt værdi. Brug RegEx-mønstermatchning til at søge efter [all values](wiki:Gramps_6.0_Wiki_Manual_-_Filters#regex_all) eller attributter, der er blevet [efterladt blankt](wiki:Gramps_6.0_Wiki_Manual_-_Filters#regex_null). Værdier: Personlig egenskab: Identifikationsnummer -- Alder ...

#### Personer med ukendt køn

Matcher alle personer med ukendt køn.

#### Personer uden kendt fødselsdato

Dette generelle filter i kategorien Personer matcher personer uden kendt fødselsdato.

Denne regel inkluderer både personer uden fødselstypebegivenhed og personer med udaterede fødselstypebegivenheder.

#### Personer uden kendt dødsdato

Matcher personer uden kendt dødsdato.

#### Personer med <id>

Matcher personer med Gramps ID. Reglen returnerer kun et match, hvis ID'et matcher nøjagtigt. Du kan enten indtaste ID'et i et tekstfelt eller vælge et objekt fra listen ved at klikke på knappen . I sidstnævnte tilfælde vises ID'et i tekstfeltet, efter at valget er foretaget.

#### Personer ændret efter <date time>

Matcher personregistreringer, der er ændret i en bestemt tidsperiode. Bruges til at identificere registreringer, der blev importeret eller ændret under bestemte arbejdssessioner.

Filtrering baseret på den angivne dato og tidsstempel, der er efter et bestemt tidsstempel i formatet `yyyy-mm-dd tt:mm:ss`. Denne filterregel vil søge efter registreringer, der er ændret inden for et datointerval, hvis der er angivet et andet dato-tidspunkt.

Værdier: Ændret efter: men før:

Værdier skal være efter 1. januar 1970 ved UTC. Fremtidige datoer indtil `3001-01-01 01:59:59` er gyldige.

Filterreglerne er tilgængelige i afsnittet for brugerdefinerede regler i visningerne Personer, Relationer, Diagrammer og Geografi.

Tilsvarende regler findes for poster af den tilsvarende kategoritype i kategorivisningerne Personer, Familier, Begivenheder, Steder, Kilder, Kildehenvisninger, Arkiv, Medier og Noter.

#### Soundex-match af Personer med <navn>

Soundex-match af personer med et bestemt navn. Fornavn, Efternavn, Kaldenavn og Øjenavn søges i primære og alternative navne.

Denne regel sammenligner navne på personer med et fonetisk mønster. Den bruger den fonetiske algoritme [Soundex](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Soundex_what_is_this.3F) til at indeksere navne efter lyd, som de udtales på engelsk.

Matchkriterier kan være en Soundex-kode (som kan findes med Soundex Gramplet) bestående af et bogstav efterfulgt af tre numeriske cifre: bogstavet er det første bogstav i navnet, og cifrene koder de resterende konsonanter. Men hvis matchkriteriet ikke er en gyldig Soundex-kode, vil filteret blot generere Soundex-kode for det indtastede ord.

Alle navnefelter (og de separate ord i disse felter) søges individuelt mod Soundex-koden.

\<span id="Familier_3\>

### Familier

</span>

Denne kategori inkluderer følgende generelle regler:

#### Forfædrefamilier til <familie>

Matcher familier, der er forfædrefamilier til partnerne i en bestemt familie. Der er mulighed for at inkludere en bestemt familie i resultaterne. Inkluderer blandede familier og familier uden fødselsrelationer.

#### Bogmærkede familier

Matcher familierne på bogmærkelisten.

#### Efterkommerfamilier til <familie>

Matcher familieobjektet, der stammer fra en bestemt familie. (Ingen personobjekter er inkluderet.)

Se også:

- Efterkommerfamiliemedlem til <filter> match
- Efterkommerfamiliemedlem til <person>

#### Hver familie

Matcher alle familier i databasen.

#### Familier ændret efter <dato-tidspunkt>

Matcher familieposter ændret efter en angivet dato-tidspunkt (ååå-mm-dd tt:mm:ss) eller i intervallet, hvis en anden dato-tidspunkt er angivet: Værdier: Ændret efter: -- men før:.

#### Familier med <antal> noter

Matcher familier med et bestemt antal noter: Værdier: Antal forekomster -- Tallet skal være større end/mindre/lig med

#### Familier med noter, der indeholder <tekst>

Matcher familier, hvis noter indeholder tekst, der matcher et regulært udtryk

#### Familier markeret som private

Matcher familier, der er angivet som private.

#### Familier, der matcher <filteret>

Matcher familier, der matcher det angivne filternavn. Værdier: Filternavn. Det angivne filternavn skal vælges fra menuen.

#### Familier med <antal> LDS-begivenheder

Matcher familier med et bestemt antal LDS-begivenheder. Værdier: Antal forekomster -- Tallet skal være større end/mindre/lig med

#### Familier med <count> media

Matcher familier med et bestemt antal elementer i galleriet. Værdier: Antal forekomster -- Tallet skal være større end/mindre/lig med

#### Familier med id, der indeholder <text>

Matcher familier, hvis Gramps ID matcher det regulære udtryk

#### Familier med et referenceantal på <count>

Matcher familier med et bestemt antal referencer. Værdier: Antal referencer -- Tallet skal være større end/mindre/lig med

#### Familier med <mærkat>

Matcher familier med et mærkat med en bestemt værdi. Værdier: Mærkatnavn.

#### Familier med family <attribute>

Matcher familier med family-attributten med en bestemt værdi. Værdier: Familieattribut: Identifikationsnummer -- Alder ...

#### Familier med relationstypen

Matcher familier med relationstypen for en bestemt værdi

#### Familier med <id>

Matcher familier med bedstefar-ID. Reglen returnerer kun et match, hvis ID'et matcher præcist. Du kan enten indtaste ID'et i et tekstfelt eller vælge et objekt fra listen ved at klikke på knappen . I sidstnævnte tilfælde vises ID'et i tekstfeltet, efter at valget er foretaget.

<span id="Begivenheder_3" >

### Begivenheder

</span>

Denne kategori indeholder følgende generelle regler:

#### Begivenhed med <id>

Matcher begivenheder med Gramps ID. Reglen returnerer kun et match, hvis ID'et matcher præcist. Du kan enten indtaste ID'et i et tekstfelt eller vælge et objekt fra listen ved at klikke på knappen . I sidstnævnte tilfælde vises ID'et i tekstfeltet, efter at valget er foretaget.

#### Begivenheder ændret efter <dato-tidspunkt>

Matcher begivenhedsposter, der er ændret efter en bestemt dato-tidspunkt (ååå-mm-dd tt:mm:ss) eller i intervallet, hvis en anden dato-tidspunkt er angivet: Værdier: Ændret efter: -- men før:.

#### Begivenheder med <antal> noter

Matcher begivenheder med et bestemt antal noter: Værdier: Antal forekomster -- Tallet skal være større end/mindre/lig med

#### Begivenheder med noter, der indeholder <tekst>

Matcher begivenheder, hvis noter indeholder tekst, der matcher et regulært udtryk

#### Begivenheder markeret som private

Matcher begivenheder, der er angivet som private.

#### Begivenheder, der matcher <filter>

Matcher begivenheder, der matcher det angivne filternavn. Værdier: Filternavn. Det angivne filternavn skal vælges fra menuen.

#### Begivenheder, der finder sted på en bestemt ugedag

Matcher begivenheder, der finder sted på en bestemt ugedag

#### Begivenheder for personer, der matcher <personfilter>

Matcher begivenheder for personer, der matcher det angivne personfilternavn

#### Begivenheder for steder, der matcher <stedfilter>

Matcher begivenheder, der fandt sted på steder, der matcher det angivne stedfilternavn

#### Begivenheder med <antal> medier

Matcher begivenheder med et bestemt antal elementer i galleriet. Værdier: Antal forekomster -- Tallet skal være større end/mindre end/lig med

#### Begivenheder med \<data\>

Matcher begivenheder med data af en bestemt værdi

#### Begivenheder med Id, der indeholder <tekst>

Matcher begivenheder, hvis Gramps ID matcher det regulære udtryk

#### Begivenheder med et referenceantal på <antal>

Matcher begivenheder med et bestemt antal referencer. Værdier: Antal referencer -- Tallet skal være større end/mindre end/lig med

#### Begivenheder med <mærkat>

Matcher begivenheder med et mærkat af en bestemt værdi. Værdier: Mærkatnavn.

#### Begivenheder med attributten <attribut>

Matcher begivenheder med attributten af ​​en bestemt værdi. Værdier: Familie Attribut: Identifikationsnummer -- Alder ...

#### Begivenheder med den bestemte type

Matcher begivenheder med den bestemte type

#### Hver begivenhed

Matcher hver begivenhed i databasen.

<span id="Steder_3" >

### Steder

</span>

Denne kategori inkluderer følgende generelle regler:

#### Hvert sted

Matcher alle steder i databasen.

#### Sted med <Id>

Matcher steder med Gramps ID. Reglen returnerer kun et match, hvis ID'et matcher præcist. Du kan enten indtaste ID'et i et tekstfelt eller vælge et objekt fra listen ved at klikke på knappen . I sidstnævnte tilfælde vises ID'et i tekstfeltet, efter at valget er foretaget.

#### Steder ændret efter <dato-tidspunkt>

Matcher steder, der er ændret efter en angivet dato-tidspunkt (åååå-mm-dd tt:mm:ss) eller i intervallet, hvis en anden dato-tidspunkt er angivet: Værdier: Ændret efter: -- men før:.

#### Steder omsluttet af et andet sted

Matcher steder under den hierarkiske struktur for et angivet sted. Inkluderer ikke det omsluttende sted og ignorerer datoer.

#### Steder med <count> noter

Matcher steder med et bestemt antal noter: Værdier: Antal forekomster -- Tallet skal være større end/mindre end/lig med

#### Steder med noter, der indeholder <text>

Matcher steder, hvis noter indeholder tekst, der matcher et regulært udtryk

#### Steder markeret som private

Matcher steder, der er angivet som private.

#### Steder, der matcher en titel

Matcher steder med en bestemt titel

#### Steder, der matcher parametre

Generel filterregel, der matcher steder med bestemte parametre:

- 

- 

- 

Tilbyder også muligheden for at .

#### Steder, der matcher <filteret>

Matcher steder, der matcher det angivne filternavn. Værdier: Filternavn. Det angivne filternavn skal vælges fra menuen.

#### Steder for begivenheder, der matcher <event filter>

Matcher steder, hvor begivenheder fandt sted, der matcher det angivne begivenhedsfilternavn

#### Steder med <count> media

Matcher steder med et bestemt antal elementer i galleriet. Værdier: Antal forekomster -- Tallet skal være større end/mindre/lig med

#### Steder med Id, der indeholder <text>

Matcher steder, hvis Gramps ID matcher det regulære udtryk

#### Steder med et referenceantal på <count>

Matcher steder med et bestemt antal referencer. Værdier: Antal referencer -- Tallet skal være større end/mindre/lig med

#### Steder med <mærkat>

Matcher steder med et mærkat med en bestemt værdi. Værdier: Mærkatnavn.

<span id="Kilder_3" >

### Kilder

</span>

Denne kategori inkluderer følgende generelle regler:

#### Hver kilde

Matcher alle kilder i databasen.

#### Kilde med <Id>

Matcher kilder med Gramps ID. Reglen returnerer kun et match, hvis ID'et matcher præcist. Du kan enten indtaste ID'et i et tekstfelt eller vælge et objekt fra listen ved at klikke på knappen . I sidstnævnte tilfælde vises ID'et i tekstfeltet, efter at valget er foretaget.

#### Kilder ændret efter <dato-tidspunkt>

Matcher kildeposter, der er ændret efter en angivet dato-tidspunkt (ååå-mm-dd tt:mm:ss) eller i intervallet, hvis en anden dato-tidspunkt er angivet: Værdier: Ændret efter: -- men før:.

#### Kilder med <count> noter

Matcher kilder med et bestemt antal noter: Værdier: Antal forekomster -- Tallet skal være større end/mindre end/lig med

#### Kilder med noter, der indeholder <text>

Matcher kilder, hvis noter indeholder tekst, der matcher et regulært udtryk

#### Kilder markeret som private

Matcher kilder, der er angivet som private.

#### Kilder, der matcher <filteret>

Matcher kilder, der matcher det angivne filternavn. Værdier: Filternavn. Det angivne filternavn skal vælges fra menuen.

#### Kilder med <count> Arkivreferencer

Matcher kilder med et bestemt antal arkivreferencer

#### Kilder med <count> medier

Matcher kilder med et bestemt antal elementer i galleriet. Værdier: Antal forekomster -- Tallet skal være større end/mindre end/lig med

#### Kilder med Id, der indeholder <tekst>

Matcher kilder, hvis Gramps ID matcher det regulære udtryk

#### Kilder med et referenceantal på <antal>

Matcher kilder med et bestemt antal referencer. Værdier: Antal referencer -- Tallet skal være større end/mindre end/lig med

#### Kilder med repositoryreference, der indeholder <tekst> i "Call Number"

Matcher kilder med en repositoryreference, der indeholder en delstreng i 'Call Number'

#### Kilder med repositoryreference, der matcher <repositoryfilteret>

Matcher kilder med en repositoryreference, der matcher et bestemt repositoryfilter

#### Kilder med <mærkat>

Matcher kilder med et mærkater med en bestemt værdi. Værdier: Mærkatnavn.

#### Kilder med titel, der indeholder <tekst>

Matcher kilder, hvis titel indeholder en bestemt delstreng

<span id="Kildehenvisning_3" >

### Kildehenvisning

</span>

Denne kategori inkluderer følgende generelle regler:

#### Kildehenvisning med <Id>

Matcher kildehenvisninger med Gramps ID. Reglen returnerer kun et match, hvis ID'et matcher præcist. Du kan enten indtaste ID'et i et tekstfelt eller vælge et objekt fra listen ved at klikke på knappen . I sidstnævnte tilfælde vises ID'et i tekstfeltet, efter at valget er foretaget.

#### Kildehenvisninger ændret efter <dato- og klokkeslæt>

Matcher kildehenvisning-poster, der er ændret efter en bestemt dato- og klokkeslæt (ååå-mm-dd tt:mm:ss) eller i intervallet, hvis en anden dato- og klokkeslæt er angivet: Værdier: Ændret efter: -- men før:.

#### Kildehenvisninger med <count> noter

Matcher kildehenvisninger med et bestemt antal noter: Værdier: Antal forekomster -- Tallet skal være større end/mindre/lig med

#### Kildehenvisninger med noter, der indeholder <tekst>

Matcher kildehenvisninger, hvis noter indeholder tekst, der matcher et regulært udtryk

#### Kildehenvisninger markeret som private

Matcher kildehenvisninger, der er angivet som private.

#### Kildehenvisninger, der matcher parametre

Generel filterregel, der matcher kildehenvisninger med bestemte parametre:

- 

- 

- 

Tilbyder også muligheden for at .

#### Kildehenvisninger, der matcher <filteret>

Matcher kildehenvisninger, der matcher det angivne filternavn. Værdier: Filternavn. Det angivne filternavn skal vælges fra menuen.

#### Kildehenvisninger med <count> media

Matcher kildehenvisninger med et bestemt antal elementer i galleriet. Værdier: Antal forekomster -- Tallet skal være større end/mindre end/lig med

#### Kildehenvisninger med Id, der indeholder <text>

Matcher kildehenvisninger, hvis Gramps ID matcher det regulære udtryk

#### Kildehenvisninger med Volumen/Side, der indeholder <text>

Matcher kildehenvisninger, hvis Volumen/Side indeholder en bestemt delstreng

#### Kildehenvisninger med et referenceantal på <count>

Matcher kildehenvisninger med et bestemt antal referencer. Værdier: Antal referencer -- Tallet skal være større end/mindre end/lig med

#### Kildehenvisninger med en kilde med en repository-reference, der matcher <repository-filteret>

Matcher kildehenvisninger med en kilde med en repository-reference, der matcher et bestemt repository-filter

#### Kildehenvisninger med kilde, der matcher <source-filteret>

Matcher kildehenvisninger med kilder, der matcher det angivne kildefilternavn

#### Kildehenvisninger med <mærkat>

Matcher kildehenvisninger med et mærkat med en bestemt værdi. Værdier: Mærkatnavn.

#### Hver Kildehenvisning

Matcher alle kildehenvisninger i databasen.

<span id="Arkiver_3" >

### Arkiver

</span>

Denne kategori indeholder følgende generelle regler:

#### Hvert arkiv

Matcher alle arkiver i databasen.

#### Arkiver ændret efter <dato-tidspunkt>

Matcher arkivposter ændret efter en angivet dato-tidspunkt (ååå-mm-dd tt:mm:ss) eller i intervallet, hvis en anden dato-tidspunkt er angivet: Værdier: Ændret efter: -- men før:.

#### Arkiver med noter, der indeholder <tekst>

Matcher arkiver, hvis noter indeholder tekst, der matcher et regulært udtryk

#### Arkiver markeret som private

Matcher arkiver, der er angivet som private.

#### Parametre for datalagre der matcher

Generel filterregel, der matcher datalagre med bestemte parametre:

- 

- 

-   
  søger i alle tekstfelter i alle postadresser

-   
  søger i alle tekstfelter i alle URL'er (Se fejl )

Tilbyder også muligheden for at .

#### Datalagre der matcher <filter>

Matcher datalagre der matcher det angivne filternavn. Værdier: Filternavn. Det angivne filternavn skal vælges fra menuen.

#### Datalagre med id der indeholder <tekst>

Matcher datalagre hvis Gramps ID matcher det regulære udtryk

#### Datalagre med et referenceantal på <count>

Matcher datalagre med et bestemt antal referencer. Værdier: Antal referencer -- Tallet skal være større end/mindre end/lig med

#### Arkiver med navn, der indeholder <tekst>

Matcher arkiver, hvis navn indeholder en delstreng

#### Arkiver med <mærkat>

Matcher arkiver med et mærkat med en bestemt værdi. Værdier: Mærkatnavn.

#### Arkiver med <Id>

Matcher arkiver med Gramps ID. Reglen returnerer kun et match, hvis ID'et matcher præcist. Du kan enten indtaste ID'et i et tekstfelt eller vælge et objekt fra listen ved at klikke på knappen . I sidstnævnte tilfælde vises ID'et i tekstfeltet, efter at valget er foretaget.

<span id="Medier_3">

### Medier

</span>

Denne kategori indeholder følgende generelle regler:

#### Hvert medieobjekt

Matcher alle medieobjekter i databasen.

#### Medieobjekt med <Id>

Matcher medieobjekter med Gramps ID. Reglen returnerer kun et match, hvis ID'et matcher præcist. Du kan enten indtaste ID'et i et tekstfelt eller vælge et objekt fra listen ved at klikke på knappen . I sidstnævnte tilfælde vises ID'et i tekstfeltet, efter at valget er foretaget.

#### Medieobjekter ændret efter <dato-tidspunkt>

Matcher medieobjektposter, der er ændret efter en angivet dato-tidspunkt (ååå-mm-dd tt:mm:ss) eller i intervallet, hvis en anden dato-tidspunkt er angivet: Værdier: Ændret efter: -- men før:.

#### Medieobjekter med noter, der indeholder <tekst>

Matcher medieobjekter, hvis noter indeholder tekst, der matcher et regulært udtryk

#### Medieobjekter markeret som private

Matcher medieobjekter, der er angivet som private.

#### Parametre for matchende medieobjekter

Generel filterregel, der matcher medieobjekter med bestemte parametre:

- 

- 

Tilbyder også muligheden at .

#### Medieobjekter, der matcher <filter>

Matcher medieobjekter, der matcher det angivne filternavn. Værdier: Filternavn. Det angivne filternavn skal vælges fra menuen.

#### Medieobjekter med et id, der indeholder <tekst>

Matcher medieobjekter, hvis Gramps ID matcher det regulære udtryk

#### Medieobjekter med et referenceantal på <count>

Matcher medieobjekter med et bestemt antal referencer. Værdier: Antal referencer -- Tallet skal være større end/mindre end/lig med

#### Medieobjekter med <mærkat>

Matcher medieobjekter med et mærkat med en bestemt værdi. Værdier: Mærkatnavn.

#### Medieobjekter med attributten <attribut>

Matcher medieobjekter med attributten for en bestemt værdi

<span id="Noter_3" >

### Noter

</span>

Denne kategori inkluderer følgende generelle regler:

#### Hver note

Matcher alle note i databasen.

#### Note med <Id>

Matcher noter med Gramps ID. Reglen returnerer kun et match, hvis ID'et matcher præcist. Du kan enten indtaste ID'et i et tekstfelt eller vælge et objekt fra listen ved at klikke på knappen . I sidstnævnte tilfælde vises ID'et i tekstfeltet, efter at valget er foretaget.

#### Noter ændret efter <dato-tidspunkt>

Matcher noteposter ændret efter en angivet dato-tidspunkt (ååå-mm-dd tt:mm:ss) eller i intervallet, hvis en anden dato-tidspunkt er angivet: Værdier: Ændret efter: -- men før:.

#### Noter, der indeholder <tekst>

Matcher noter, der indeholder tekst, der matcher et regulært udtryk

#### Noter markeret som private

Matcher noter, der er angivet som private.

#### Noter der matcher parametre

Matcher noter med bestemte parametre

- 

- 

Tilbyder også muligheden at .

#### Noter der matcher <filter>

Matcher noter der matcher det angivne filternavn. Værdier: Filternavn. Det angivne filternavn skal vælges fra menuen.

#### Noter med id der indeholder <tekst>

Matcher noter hvis Gramps ID matcher det regulære udtryk

#### Noter med et referenceantal på <count>

Matcher noter med et bestemt antal referencer. Værdier: Antal referencer -- Tallet skal være større end/mindre end/lig med

#### Noter med <mærkat>

Matcher noter med et mærkat med en bestemt værdi. Værdier: Mærkatnavn.

#### Noter med den bestemte type

Matcher noter med den bestemte type {{-}}

## Moderfiltre

Denne regelkategori finder familier med mødre, der matcher reglen:

### Familier med mor med et id, der indeholder <tekst>

Matcher familier, hvis mor har et angivet bedstefar-ID

### Familier med mor med <navn>

Matcher familier, hvis mor har et angivet (delvis) navn {{-}}

## Positionsfiltre

Denne regelkategori finder steder ud fra deres nærhed i GPS-koordinater:

### Steder i nærheden af ​​en given position

Matcher steder med breddegrad eller længdegrad i et rektangel med en given højde og bredde (i grader), og med midterpunktet den givne breddegrad og længdegrad.

### Steder uden angivet breddegrad eller længdegrad

Matcher steder med tom breddegrad eller længdegrad

### Steder inden for et område

Matcher steder inden for en given afstand fra et bestemt sted.

Efter at have valgt et sted (som skal have et gyldigt sæt koordinater), matches ethvert sted, hvis koordinater ligger inden for en cirkel på kloden (en ellipse på et fladt kort) centreret omkring koordinaterne med en bestemt radius.

Afstandsenhederne kan vælges: kilometer (lineær måling), grader (vinkelmål) og miles (lineær måling). {{-}}

## Kildefiltre

Denne regelkategori finder kildehenvisninger, der matcher reglen:

### Kildehenvisning med kilde <Id>

Matcher en Kildehenvisning med en kilde med et angivet Gramps-ID

### Kildehenvisninger med kildenoter, der indeholder <tekst>

Matcher kildehenvisninger, hvis kildenoter indeholder en delstreng eller matcher et regulært udtryk

### Kildehenvisninger med kilde-ID, der indeholder <tekst>

Matcher kildehenvisninger, hvis kilde har et Gramps-ID, der matcher det regulære udtryk

### Kilder, der matcher parametre

Generel filterregel, der matcher kilder med en kilde med en bestemt værdi:

- 

- 

- 

- 

Tilbyder også muligheden for at . {{-}}

## Slægtsforholdfiltre

Denne kategori inkluderer følgende regler, der matcher personer baseret på deres gensidige forhold:

### Personer relateret til <Person>

Matcher personer relateret til en bestemt person

### Relationssti mellem <person> og personer, der matcher <filter>

Søger i databasen startende fra en bestemt person og returnerer alle mellem den person og et sæt af målpersoner angivet med et filter. Dette producerer et sæt af relationsstier (inklusive via ægteskab) mellem den angivne person og målpersonerne. Hver sti er ikke nødvendigvis den korteste sti.

### Relationssti mellem <personer>

Denne regel matcher alle forfædre til begge personer tilbage til deres fælles forfædre (hvis en sådan findes). Dette producerer "relationsstien" mellem disse to personer gennem deres fælles forfædre. Du kan enten indtaste ID'et for hver person i de relevante tekstfelter eller vælge personer fra listen ved at klikke på deres -knapper. I sidstnævnte tilfælde vises ID'et i tekstfeltet, efter at valget er foretaget.

### Slægtssti mellem bogmærkede personer

Matcher forfædrene til bogmærkede personer tilbage til fælles forfædre, hvilket producerer slægtsstien(erne) mellem bogmærkede personer. {{-}}

## Mærkater

![[_media/gramps-tag.png]]Et [Mærkat](wiki:Gramps_Glossary/da#tag) er en brugerdefineret titel- og farvekodet etiket, der kan oprettes med dialogboksen og vedhæftes til den valgte [Kildehenvisning](#Kildehenvisning), [Event](#event), [Familie](#Familie), [Media](#media), [Note](#Note), [Person](#person), [Sted](#Sted), [Arkiv](#Arkiv) eller [Kilde](#Kilde) objekter med henblik på nem identifikation og filtrering.

Et brugerdefineret navngivet søgeord eller en sætning kan bruges til at gruppere samlingen for at producere en rapport. Flere mærkater kan bruges til at mærke og kategorisere objekter i flere grupper, når filtrering efter andre attributter ikke er mulig.

For eksempel, når du har et stort slægtsbog, kan du lave delmængder af slægtsbogen, og disse delmængder kan overlappe hinanden. For eksempel delmængderne af din fars familie og din mors familie, en delmængde af din familie, der emigrerede til Australien. Ideen ville være at tildele et forskelligt mærkat til hvert delmængde: *Faderlig*, *Moderlig*, *Australien* og *ToDo* for at identificere hver gruppe.

Teknisk: For dem af jer, der bruger e-mailprogrammerne *Gmail* eller *Thunderbird*, vil funktionen [Mærkat](wiki:Gramps_Glossary/da#tag) virke ret velkendt. Hvor e-mails i stedet for at klassificere dem i mapper som i *Outlook* (Windows) eller *Evolution* (Linux), klassificeres de ved at tildele dem mærkater. Så i stedet for at have en usammenhængende N:1-klassificering (en e-mail kan være i én og kun én mappe, og en mappe kan indeholde mange e-mails), er der i *Gmail* eller *Thunderbird* en N:M-klassificering (hvor en e-mail kan have flere mærkater, og et mærkat kan anvendes på flere e-mails). {{-}}

### Mærkat-menu

![[_media/Menu-Edit-Tag-Options-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Mærkat-handlinger fra Rediger-menuen]]

Fra menuen kan du vælge mellem følgende muligheder:

- dialogboks

- Vindue

- En liste over tidligere oprettede mærkater, som du kan vælge til følgende handlinger:
  - 

  - 

{{-}}

### Ikon for mærkat af valgte rækker i værktøjslinjen

![[_media/Toolbar-TagSelectedRows-Icon-DropDownMenu-overview-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Tilgængelige tag-handlinger fra "Mærkat valgte rækker" værktøjslinjeikon - oversigt over rullemenu - eksempel]]

Eller klik på knappen ![[_media/16x16-gramps-tag.png]] i værktøjslinjen for at få adgang til de samme muligheder som i menuen .

{{-}} Se også:

- [Mærkatrapport](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_6#Tag_Report), der viser primære objekter (person, familie, noter), der matcher det valgte mærkat.

{{-}}

### Ny mærkatdialog

![[_media/NewTag-dialog-ShowingMultipleListSelection-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Tilføjelse af et "Nyt mærkat" til flere listeposter - eksempel med dialogboksen "Nyt mærkat"]]

Du kan tilføje et nyt mærkat til enten et enkelt listepost eller flere listeposter fra en hvilken som helst af kategorilistevisningerne ved at foretage valget og derefter bruge dialogboksen Nyt mærkat til at indtaste navnet på mærkatet og om ønsket vælge en farve til tagget ved hjælp af vælgeren . Bemærk, at rækkefølgen af ​​mærkaterne i listen Organiser mærkat definerer prioriteten for farvelægning af rækker i kategorilistevisningerne.

Mærkater kan bruges med alle [primære objekter](wiki:Gramps_Glossary/da#primary_object). {{-}}

##### Påsætning af mærkat på et udvalg af objekter

På grund af mærkaters **statiske** natur kan det være nyttigt at tilføje et mærkat til et udvalg af objekter. For eksempel skal man kunne vælge et antal personer i [Person (liste) Visning](wiki:Gramps_6.0_Wiki_Manual_-_Categories#People_Category) og tilføje et nyt mærkat eller et eksisterende til dem. {{-}}

### Vindue til organisering af mærkater

![[_media/MenuEditTag-OrganizeTags-dialog-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Organiser mærkater - dialogboks - eksempel]]

I dialogboksen vises mærkater på en liste, der viser `Navn` og `Farve`, hvor rækkefølgen af ​​mærkat på listen definerer prioriteten for farvelægning af rækker i kategorivisningerne. Du kan også ændre rækkefølgen af ​​mærkater ved at vælge et og bruge knapperne eller , eller et mærkat eller få adgang til denne -side. Når du er færdig, kan du dialogboksen.

{{-}}

### Dialog til valg af mærkater

![[_media/TagSelection-dialog-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Valg af mærkater i personeditoren]]

Når du bruger knappen ![[_media/16x16-gramps-tag.png]] fra en af ​​editordialogerne, f.eks. , vises en dialogliste , som giver dig mulighed for at fjerne eller tildele eksisterende brugerdefinerede mærkater. Mærkaterne vises i alfabetisk rækkefølge og ikke i den rækkefølge, der vises i vinduet Organiser mærkater. {{-}}

### Brug af mærkater

Her er nogle ideer til handlinger, der kan udføres med mærkater

#### Filtrering

![[_media/Sidebar-PeopleTreeView-Filter-TagDropDownList-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Gramps Filter SideBar - Eksempel på mærkat-liste]]

Den mest oplagte anvendelse er filtrering.

- Mærkater og filtre opretter begge delmængder af træet. De har dog praktiske forskelle i brugen.

At angive din fars familie ved hjælp af filtre er en nem ting; der findes allerede filtre baseret på en vis logikker, der gør det. På den anden side er det sværere at angive de personer, der emigrerede til USA, mens det for de berømte personer i din familie simpelthen er umuligt, da der ikke er nogen logisk regel. Mærkater er meget mere praktiske her.

Filtre har dog den fordel, at de er **dynamiske**. Hvis du tilføjer en forfader til din far i slægtsbogen, vil den automatisk blive tilføjet til filteret.

På den anden side er mærkater **statiske**. Når du tilføjer en berømt person til træet, skal du eksplicit tilføje mærkatet dem som *BERØMT*.

- Det mest umiddelbare objekt, der kommer i tanke, er individerne, og det er også det mest nyttige. Andre objekter kan dog også påsættes mærkat:
  - Steder: For eksempel "steder at besøge",
  - Kilde: For eksempel "kilder på tysk",
  - Noter: For eksempel "noter under udarbejdelse" eller "noter på tysk",
  - Medier: For eksempel "Billede, der tilhører onkel Alfred".

Mærkater kan bruges med **alle primære objekter**. {{-}}

#### Mærkater-kolonne

![[_media/PeopleListView-ExampleTagColoredRows-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Personvisning (liste) - Viser kolonnen "Mærkat" og farvede mærkat-rækker - eksempel]]

Brug til at tilføje kolonnen til listevisningerne af objekter for nemt at se dine mærkater. Indholdet af Mærkater-kolonnen vises derefter som en kommasepareret liste over de mærkater, der er knyttet til objekterne. Bemærk rækkefølgen af ​​mærkater i dialogboksen definerer prioriteten for farvelægning af rækker i kategorilistevisningerne.

#### Rapport over mærkat anvendelse

[Rapport over mærkatbrug](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_6#Tag_Report) viser [primære objekter](wiki:Gramps_Glossary/da#primary_object) (person, familie, noter) med det valgte mærkat.

### Se også

- [Mærkater i Gramps](wiki:Tags_in_Gramps) - en introduktion
- Automatisk [Import af tidsstempeltags](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Import)
- filtreret [Tilføj/fjern tagværktøj](wiki:Addon:AddRemoveTagTool) (Tredjepartstilføjelse til Gramps)

{{-}}

[Category:Documentation](wiki:Category:Documentation)
