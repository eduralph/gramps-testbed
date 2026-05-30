---
title: Da:Gramps 6.0 brugsanvisning - CSV Import og Export
categories:
- Documentation
- Gramps Examples
managed: false
source: wiki-scrape
wiki_revid: 129350
wiki_fetched_at: '2026-05-30T16:35:50Z'
lang: da
---

{{#vardefine:chapter\|6}} {{#vardefine:figure\|0}} Dette afsnit omhandler brugen af ​​Gramps med formatet **Kommaseparerede værdier regneark (CSV)**.

- [Gramps CSV-import](wiki:Da:Gramps_6.0_brugsanvisning_-_Arbejd_med_slægtsbøger#Gramps_CSV_import)
- [Eksport af kommaseparerede værdier (CSV)](wiki:Da:Gramps_6.0_brugsanvisning_-_Arbejd_med_Slægtsbøger#Kommaseparerede_værdier_Regneark_(CSV)_eksport)

Du kan også [Eksportere](wiki:Da:Gramps_6.0_brugsanvisning_-_Indstillinger#Eksportere) den aktuelle listevisning til et regneark (\*.ODT) eller en CSV-fil.

## Gramps Regneark Import/Eksport <span id="Gramps Spreadsheet Import/Export"></span>

Dette format giver mulighed for at importere/eksportere et regneark med alle data på én gang. Som standard skal regnearket være i kommasepareret værdi (CSV)-format. (Selvom alternative seperatorer kan angives for [CSV-dialekten](wiki:Da:Gramps_6.0_brugsanvisning_-_Indstillinger#CSV_Dialect) i i listevisninger.) De fleste regnearksprogrammer kan læse og skrive i dette format. Det er også nemt at skrive i hånden. Dette er det eneste Gramps-importformat, der tillader sammenflettet data med eksisterende data.

Der er tre hovedanvendelser for dette format:

1.  Du kan eksportere dine kernedata fra Gramps til et regnearksformat, redigere dem med et tekst- eller regnearksprogram og importere ændringer og tilføjelser tilbage til Gramps. Dette er praktisk at sende til andre for at udfylde, eller at tage med på farten, når du ikke har din fulde Gramps-applikation.
2.  Du kan importere nye data til dit Gramps-slægtstræ (database). Hvis du for eksempel har en række nye personer, du vil føje til dit slægtstræ, men ikke ønsker at lede og rode dig vej for at finde, hvor de skal hen, kan det være nemmere at skrive dem ind i et regneark og derefter hurtigt hente dem alle ind på én gang. Dette er praktisk, hvis du har en stor mængde data, som du klipper og indsætter fra et andet program eller internettet. Et eksempel på dette er [gendannelse af dit Gramps-slægtstræ](wiki:Narrative_Website_Import) ved at indlæse Narrative Website i et regneark.
3.  Du kan også importere et sæt rettelser og tilføjelser. Lad os sige, at du har udskrevet en rapport, og du gennemgår den og markerer rettelser. Hvis du gør hver rettelse til en sektion i et regneark, kan du "skrive redigeringerne i et script" og derefter udføre dem alle på én gang.

{{-}}

## Eksport <span id="Export"></span>

### Eksportere en slægtsbog <span id="Exporting a Family Tree"></span>

![[_media/ExportAssistant-ExportOptions-CSV-defaults-60-da.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Eksportassistent - Eksportindstillinger - guidedialog (viser standardindstillinger for "Kommaseparerede værdier regneark (CSV)") med nederste sektion for filformatspecifikke indstillinger]]

Sådan eksporterer du dit slægtsbog:

1.  Start Gramps
2.  Indlæs den slægtsbog, der skal eksporteres
3.  Vælg fra menuen
4.  Vælg i vinduet .

<!-- -->

1.  Vælg **Regneark med kommaseparerede værdier (CSV)** i vinduet
2.  I vinduet :
    1.  I den øverste sektion skal du vælge, hvilke filtre der skal anvendes på din slægtsbog
    2.  Fra afkrydsningsfelterne skal du vælge, hvilke elementer der skal inkluderes i eksporten (personer, ægteskaber, børn, steder), og om overskrifterne skal oversættes til det sprog, der aktuelt bruges.
3.  I vinduet skal du vælge navnet og stien for udfilen
4.  I vinduet skal du bekræfte indstillingen og klikke på knappen for at starte den faktiske eksport.

{{-}}

Et udsnit af felter, der indeholder dine slægtsdata, gemmes i en .csv-fil i det format, der er beskrevet nedenfor. Personer og familier er annoteret på en sådan måde, at dataene kan redigeres og overskrives, når de importeres tilbage. Annotationerne giver mulighed for at opdatere slægtsbogsdatabasen via import.

Der er nogle kolonner, der vil være tomme, især note- og kildekolonnerne. Disse er angivet i regnearket, så du kan lave noter til importen, men noter eksporteres aldrig med dette værktøj.

Dine data er opdelt i fire sektioner, der repræsenterer steder, individer, ægteskaber og børn. De eksporterede felter og kolonnenavne er:

Steder  
Sted, Titel, Navn, Type, Breddegrad, Længdegrad, Kode, Omsluttet af, Dato

<!-- -->

Personer  
Person, Efternavn, Fornavn, Kaldenavn, Suffiks, Præfiks, Titel, Køn, Fødselsdato, Fødested (eller Fødesteds-id), Fødselskilde, Dåbsdato, Dåbssted (eller Dåbssteds-id), Dåbskilde, Dødsdato, Dødssted (eller Dødssteds-id), Dødskilde, Begravelsesdato, Begravelsessted (eller Begravelsessteds-id), Begravelseskilde, Note

<!-- -->

Ægteskaber  
Ægteskab, Mand, Hustru, Dato, Sted (eller Steds-id), Kilde, Note

<!-- -->

Familier  
Familie, Barn

Den første kolonne i hvert område er Gramps-ID. Det er det, der forbinder dine redigeringer tilbage til de relevante data, så ændr ikke disse ID'er. Indlæs denne fil i dit foretrukne regneark ved hjælp af kommasepareret, dobbelt anførselstegnssepareret tekst og tekstformat (enhver kodning for nu). Derefter kan du tilføje eller rette data og gemme det igen, mens du beholder det samme format. Du kan derefter importere dataene tilbage oven på dine gamle data, og de vil blive rettet.

. . {{-}}

### Eksportere en enkelt kategori <span id="Exporting a single category"></span>

Du kan eksportere alle data fra en enkelt kategori - f.eks. Steder - ved at vælge kategorivisningen og derefter bruge

![[_media/CategoryView-CSV-Export-Options-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Kategorivisning Konfigurer CSV-eksportmuligheder]] Før du eksporterer dataene, kan du vælge det CSV-format, der passer bedst til dit miljø eller formål.

Klik på ikonet ![[_media/Gramps-config.png]] på for at åbne dialogboksen .

Ved at bruge indstillingen kan du vælge et specifikt separatortegn mellem kolonnerne, f.eks. tabulator eller '\|'. {{-}}

## Import

Sådan importerer du dine CSV-data:

1.  Brug filen ovenfor, eller opret et regneark (beskrevet [nedenfor](wiki:Da:Gramps_6.0_brugsanvisning_-_CSV_Import_og_Export#Example_CSV_with_multiple_areas)) med genealogiske data
2.  Start Gramps
3.  Opret en ny slægtsbog
4.  Vælg fra menuen
5.  Vælg filen **Kommaseparerede værdier Regneark (CSV)**, og vælg derefter knappen

Flettedelen af ​​denne kode vil kun tilføje eller opdatere oplysninger til din slægtsbog, og det antages altid, at regnearksdataene er den korrekte version.

Hvis du indlæser dette regneark i LibreOffice Calc, skal du sørge for at vælge hver kolonne som typen **Tekst** i stedet for **Standard**. Standard vil omformatere dine datoer og tal. Hvis du bruger Excel, vil du sandsynligvis også gerne markere alle celler, når de er åbnet, og ændre formatet på cellerne til **Tekst**.

Regnearket består af data, der er opbygget af kolonner. Øverst i hver kolonne skal der stå navnet på den type data, der er i kolonnen. Den første kolonne i hvert område er Gramps ID-referencen. Du skal bruge særlige navne til kolonnerne. De er:

### Sted

    place - en reference til dette sted
    title - stedets titel
    name - stedets navn
    type - stedtype (f.eks. by, amt, stat osv.)
    latitude - stedets breddegrad
    longitude - stedets længdegrad
    code - postnummer osv.
    enclosed_by - referencen til et andet sted, der omslutter dette sted
    date - datoen, hvornår enclosed_by var gældende

### Personer

    person - en reference, der skal bruges til familier (ægteskaber og børn)
    grampsid - til at tildele et Gramps-id til personen
    firstname/first_name/given_name/given - en persons fornavn
    surname/lastname/last_name - en persons efternavn
    callname/call_name/call - et almindeligt navn (kælenavn) for personen
    prefix - efternavnspræfiks (von, de osv.)
    suffix - et suffiks af en persons navn (Jr., Sr.)
    title - en persons titel (Dr., Mr.)
    gender - mand eller kvinde (du bør bruge oversættelsen til dit sprog)
    source - kildetitel for personen
    note - en note til personens optegnelse

    birthdate - fødselsdato
    birthplace - fødested
    birthplaceid/birthplace_id/birth_place_id - fødesteds-id
    birthsource - kildetitel for fødsel

    baptismdate - dåbsdato
    baptismplace - dåbssted dåb
    baptismplaceid - sted-id for dåb
    baptismsource - kildetitel for dåb

    deathdate - dødsdato
    deathplace - dødssted
    deathplaceid - sted-id for død
    deathsource - kildetitel for død
    deathcause - dødsårsag

    burialdate - dato for begravelse
    burialplace - begravelsessted
    burialplaceid - sted-id for begravelse
    burialsource - kildetitel for begravelse

    occupationdate - dato for erhverv
    occupationplace - erhvervssted
    occupationplace_id - sted-id for erhverv
    occupationsource - kildetitel for erhverv
    occupationdescr - beskrivelse af erhverv

    residencedate - dato for bopæl
    residenceplace - bopælssted
    residenceplace_id - sted-id for bopæl
    residencesource - kildetitel for bopæl

    attributtype - type af attribut
    attributvalue - værdi af attribut
    attributsource - kildetitel for attribut

### Ægteskab

    marriage - hvis du vil referere til dette fra en familie, skal du bruge et matchende navn her
    husband/father/parent1 - referencen til ovenstående person, som er ægtemanden
    (for kvindelig parent1 skal du indtaste køn i personområdet,
    eller redigere det senere i Gramps)
    wife/mother/parent2 - referencen til ovenstående person, som er hustruen
    (for mandlig parent2 skal du indtaste køn i personområdet,
    eller redigere det senere i Gramps)
    date - datoen for ægteskabet
    place - stedet for ægteskabet
    placeid - sted-id'et for ægteskabet
    source - kildetitel på ægteskabet
    note - en note om ægteskabet/brylluppet

### Familie

    family - en reference til at knytte dette til et af ovenstående ægteskaber (påkrævet)
    child - referencen til ovenstående person, som er et barn
    source - kildetitel på ægteskabet
    note - en note om familien
    køn - mand eller kvinde (du skal bruge oversættelsen til dit sprog) [Du kan angive køn her eller personligt ovenfor]

{{-}}

## Detaljer

Kolonnenavne skelner ikke mellem store og små bogstaver. Du kan bruge en hvilken som helst kombination af kolonnerne i en hvilken som helst rækkefølge. (**Faktisk skal du som minimum have et efternavn og et fornavn, når du definerer en person, du skal have en kolonne for ægteskab og barn, når du definerer børn, og steder skal have en stedreference, men det er det.**) Kolonnenavnene er de engelske navne, der er angivet (for nu), men dataene skal være på dit sprog (inklusive ordene "mand" og "kvinde").

Rækkefølgen fra top til bund er vigtig, da definitionen SKAL komme først, hvis du vil referere til noget i ét område til et andet. Hvis du f.eks. vil definere familier af personer, skal individerne defineres før familierne. Det samme gælder for steder. Så det er normalt bedst at placere steddataene først, personer derefter og derefter ægteskaber og familier.

Hver af disse kan placeres i sit eget område i et regneark. Der er ingen grænse for antallet af områder i et ark, og hvert område kan have et vilkårligt antal rækker. Efterlad en tom række mellem "områder". Sørg blot for, at områderne ikke ligger ved siden af ​​hinanden; de skal være over og under hinanden.

Du kan have flere områder af hver slags i et regneark. Den eneste begrænsning er, at hvis du refererer til en person, skal du gøre det i en række lavere end hvor personen er beskrevet. Ligeledes, hvis du refererer til et ægteskab, skal du gøre det i en række lavere end hvor ægteskabet er beskrevet. Referencer til enclosed_by-pladser skal allerede findes i databasen eller være defineret i rækker ovenfor i regnearket.

Hvis du bruger 'grampsid' til at tildele specifikke id'er, skal du være *meget* forsigtig, når du importerer til en aktuel database. Alle data, du indtaster, vil **overskrive** de data, der er tildelt det pågældende grampsid. Hvis du bruger id'er i kolonnerne for sted, person, ægteskab eller familie, der er omgivet af firkantede parenteser (f.eks. '\[I0001\]'), vil de værdier, du bruger, også blive fortolket som grampsider. Hvis du tilføjer **nye** elementer, opfordres du til at undgå at bruge parentesformatet eller grampsid-kolonner for at undgå at overskrive dine data ved et uheld. Hvis du blander parentes- (eller grampsid-) metoder med almindelige referencer (ingen firkantede parenteser), skal du placere de almindeligt refererede data efter de parentesrefererede data.

Hvis du indtaster dataene i en tekstfil, og hvis du ønsker at have et komma inden i en af ​​værdierne, f.eks. "Clinton, Co., MO", skal du placere hele værdien i dobbelte anførselstegn og placere det første dobbelte anførselstegn lige efter det foregående komma. For eksempel:

    marriage, parent1, parent2, place
    m1, p1, p2,"Clinton, Co., MO"
    m2, p3, p4,"Havertown, PA"

Et regnearksprogram vil gøre dette automatisk for dig.

### Eksempel CSV

Her er et eksempel på et regneark i LibreOffice Calc, men ethvert regnearksprogram burde virke.

![[_media/Gramps-csv-example1.csv-LibreOffice-Calc--example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Eksempel på gramps-csv-example1.csv fil vist som et &quot;LibreOffice Calc&quot; regneark]] {{-}}

<hr>

Filnavn: `gramps-csv-example1.csv`

Filindhold:

    ,,,,,,,,,
    ,"Firstname","Surname","Callname","Gender","Prefix","Suffix","Title","Note","Grampsid"
    ,"Douglas","Test","Doug","male","Von","Sr.","Dr.","This is not related","I0007"
    ,"Laura","Test",,"female",,,,,

<hr>

{{-}} Bemærk, at CSV-dataene behøver ikke at starte i den første kolonne eller i den første række.

Når [imported](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees:_CSV_Import_and_Export#Import) er importeret i Gramps, vises de resulterende data som følger:

![[_media/FamilyTree-example-imported-gramps-csv-example1.csv-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Eksempel på importeret CSV-filresultat (Gramps 6.0.3; Microsoft Windows 10)(data fra gramps-csv-example1.csv-fil)]] {{-}}

### Eksempel CSV med flere områder

Her er et eksempel på et CSV-tekstregneark med flere områder:

Hvis du opretter, klipper og indsætter følgende i en fil, kan du importere det direkte.

<hr>

Filnavn: `gramps-csv-example2.csv`

Filindhold:

    Place, Title, Name, Type
    [P0001], Michigan, Michigan, State
    L1, Canada, Canada, Country
    L2, USA, USA, Country

    Firstname, Surname, Birthdate, Birth place id
    John,      Tester,  11/11/1965, L1
    Sally,     Tester,  01/26/1973, L1

    Person, Firstname, Surname, Birthdate,    Birth place id
    p1,     Tom,       Smith,   22 Jan 1970, [P0001]
    p2,     Mary,      Jones
    p3,     Jonnie,    Smith
    p5,     James,     Loucher
    p6,     Penny,     Armbruster
    [P0002],Tim,       Sparklet

    Marriage, Husband, Wife
    m1,       p1,      p2
    m2,       p5,      p6

    Family, Child
    m1,     p3
    m1,     p6
    m2,     [P0002]

<hr>

CSV-filen viser, at en dato kan være enhver gyldig Gramps-dato, inklusive datoformater som "26. JAN 1973" eller "26.1.1973".

Hvis du bruger dine referencer til at være Gramps-ID'er i firkantede parenteser, kan du henvise til personer, der allerede er i slægtsbogen, sådan her:

    Person,    Firstname, Lastname
    joe's boy, Harry,     Smith

    Family,  Child
    [F1524], joe's boy

    Husband, Wife
    [I0123], [I0562]

    firstname, surname
    Timothy, Jones

    place, enclosed_by
    [P0001], [P0002]

Dette eksempel ville oprette og tilføje Harry Smith til den tidligere eksisterende familie i Gramps, familie F1524.

Dette eksempel ville også gifte to tidligere eksisterende personer, I0123 og I0562.

Dette opretter også en person ved navn Timothy Jones, som ikke er i familie med nogen.

Endelig vil dette også gøre stedet P0001 omsluttet af stedet P0002. {{-}}

### Eksempel på CSV fra regneark

![[_media/Gramps-csv-example3.ods-LibreOffice-Calc-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Manuelt indtastede data i et regneark: <code>gramps-csv-example3.ods</code>]]

Brug af Gramps [Example.gramps](wiki:Example.gramps) til dette eksempel. Børnene findes allerede i slægtsbogen. Så du kan indtaste en hel generation (8 navne med vielsesdatoer) i et regneark i LibreOffice Calc.

Bemærk, at du kan bruge tal eller strenge som referencenavne mellem områder. I personområdet brugte jeg tallene 1 til 8. Det gjorde det nemt at henvise til dem i det andet område om ægteskaber. Ægteskaberne er mærket med bogstaverne A til D.

Bemærk også, at børnene i det tredje område i regnearket er eksisterende personer i Gramps, som angivet med de firkantede parenteser omkring Gramps-ID'erne.

Gemmer som en CSV-fil ved hjælp af LibreOffice Calc

<hr>

Filnavn: `gramps-csv-example3.csv`

Filindhold:

    ,,,
    ,,,
    "Person","Fornavn","Efternavn",
    1"Peter","Blank",
    2"Anna Maria","Kiefer",
    3"Georg","Schmidt",
    4"Barbara","Goering",
    5"Johann","Kiefer",
    6"Fides","Federer",
    7"Sebastian","Schelli",
    8"Magdelena","Schlegel",
    ,,,
    ,,,
    "Ægteskab","Mand","Kone","Dato"
    "A",1,2,"28. januar 1712"
    "B",3,4,"4. maj 1732"
    "C",5,6,02/07/1930
    "D",7,8,17/08/1927
    ,,,
    "Familie","Barn",,
    "A","[I0104]",,
    "B","[I0105]",,
    "C","[I0972]",,
    "D","[I0973]",,

<hr>

{{-}} Import fra CSV-filen til den eksisterende Gramps *Example.gramps*-slægtsbog producerer den yderste højre kolonne, der vises på skærmbilledet af stamtavletræet **Efter:**. ![[_media/ChartsCategory-Pedigree-view1-horizontal-right-standard-5gen-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Før: Stamtavlevisning]]

![[_media/FamilyTree-example-imported-gramps-csv-example3.csv-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Efter: Gemmer man som CSV og importerer man den yderste højre kolonne i stamtavlevisningen.]] {{-}}

### Se også

- Gramps forumdiskussion:
  - [CSV-skabelon til tekstimport](https://gramps.discourse.group/t/csv-template-for-text-import/5277/5)

<!-- -->

- [Addon:Import (text) Gramplet](wiki:Addon:ImportGramplet) Tredjepartstilføjelse af Doug Blank - en interaktiv version af [CSV Import](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees:_CSV_Import_and_Export)
- Python CSV-biblioteksdokumentation - [dialekter og formateringsparametre](https://docs.python.org/3/library/csv.html#dialects-and-formatting-parameters)

Eksempler på tilpasning af CSV-importkoden for at understøtte yderligere poster:

- Funktionsanmodning : \[CSV\] Import af komplekse Excel-tabeller til Gramps (såsom vidneoplysninger)
- [PR \#139](https://github.com/gramps-project/gramps/pull/139): Tilføj CSV-importunderstøttelse for AFN- og REFN-attributter
- [PR \#810](https://github.com/gramps-project/gramps/pull/810): Tilføj erhvervs- og bopælsbegivenheder + attributter i CSV-personimportøren

{{-}}

[C](wiki:Category:Documentation) [CSV import/Export](wiki:Category:Gramps_Examples)
