---
title: 'Da:Gramps 6.0 brugsanvisning - Indtaste og redigere data: detaljeret - del
  3'
categories:
- Documentation
- Pages using invalid self-closed HTML tags
- Stub
managed: false
source: wiki-scrape
wiki_revid: 128953
wiki_fetched_at: '2026-05-30T17:29:34Z'
lang: da
---

{{#vardefine:chapter\|9.3}} {{#vardefine:figure\|0}} **<span style="font-size:120%">Indtaste og redigere data: detaljeret Navne, Attributter, Adresser, Sammenfletning af data</span>**  
Det forrige afsnit gav dig en detaljeret oversigt over, hvordan du indtaster og redigerer de vigtigste objekter, du ser i Gramps. Dette afsnit fortsætter med andre objekter, du støder på i Gramps.

## Redigering af navne <span id="Name Editor"/>

Navne redigeres via dialogboksen , som er tilgængelig fra fanen i dialogboksen eller på samme vindue vha ikonet til højre for feltet . Udover at redigere navnet tillader navneredigering: definition af flere efternavne, aliasser, valg af foretrukket navn (evt. tidsbestemt) og tilsidesættelse af visningsformat, grupper og sortering. Navne overalt i Gramps vises i det format, der er valgt i afsnittet *Visningsindstillinger* i fanen [](wiki:Da:Gramps_6.0_brugsanvisning_-_Indstillinger#Display_Options) i dialogboksen . Andre foruddefinerede visningsformater kan vælges fra pop op-menuen . Nye navneformater kan oprettes med ved at klikke på knappen . {{-}}

### Redigering af navne dialog <span id="Name Editor dialog"/>

![[_media/NameEditor-dialog-example-60-da.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;Redigering af navne&quot; - dialog - eksempel]] Øverst i dialogvinduet kan du vælge [navnetypen](#Navnetype) (f.eks. fødselsnavn, giftenavn osv.) fra en rulleliste. Dernæst er der elementer af det personnavn, der oftest grupperes som fornavnselementer. Efter afsnittet fornavn er der afsnittet efternavne. Nederst er der elementer, der giver mulighed for tilpasning af navnesortering, datoer for navne, navnekilder og noter til navne. {{-}}

#### Navnetype <span id="Type"/>

- (`Navn ved fødslen`standard) Rullelisten Navnetype giver dig mulighed for at vælge den type navn, der indtastes. Du kan også indtaste [Brugerdefineret type](wiki:Gramps_Glossary/da#custom) direkte i dette felt.

<!-- -->

- . Klik ikonet i øverste højre hjørne for at markere denne navnepost som privat eller offentlig. Navne, som markeres privat, giver mulighed for at udelade disse fra at blive medtaget i rapporter, hvis du vælger det blandt rapportgenereringsmulighederne.

{{-}}

#### Fornavne sektion <span id="Given Name(s) Section"/>

Sektionen **Fornavne** indeholder alle dele af et personnavn, som du kan gemme i Gramps:

- Personens fornavne skal alle indtastes her.

- Personens rigtige juridiske navn, der blev brugt mest af personen, skal indtastes her. For eksempel skal en person ved navn John Raymond Smith, der bruger navnet Raymond, have *Raymond* indtastet her. Hvis denne person bruger *Ray* ofte, skal dette indtastes som et kaldenavn, da Ray ikke er det rigtige juridiske navn (se følgende). I Tyskland og nogle andre steder var det almindeligt at understrege kaldenavnet blandt de forskellige fornavne (se også [her](wiki:Names_in_Gramps#Call_Name)).

- Personens titel, såsom Doktor (eller Dr.), kan indtastes her.

- Personens navnesuffiks, f.eks. Junior (Jr.) eller III, skal indtastes her.

- Personens tilnavn/kælenavn skal indtastes her. Tilnavne omfatter forkortelser af juridiske navne, f.eks. Greg for Gregory (jf. Kaldenavn ovenfor).

{{-}}

#### Efternavne sektion <span id="Family Names Section"/>

Sektionen **Efternavne** indeholder personens efternavne. Gramps tillader flere efternavne samt flere typer familienavne.

- Værktøjslinje - / / / /

Følgende kolonner vises:

- En forstavelse for efternavnet, der ikke bruges i sortering (f.eks. "de" eller "van").

- for hoveddelen af ​​ens familienavn.

- bruges ofte i matronymiske eller patronymiske navneordninger, f.eks. *dotter*.

- angiver typen af ​​efternavn og dets afledning.

- Radioboks, der angiver, om efternavnet er det primære.

Følgende felt vises:

- for familier, der almindeligvis omtales ved hjælp af et mere folkeligt kaldenavn.

Se også: [Names in Gramps](wiki:Names_in_Gramps) - wikiartikel. {{-}}

### Faneblade i Navneredigering <span id="Name Editor tab pages"/>

Følgende faner er tilgængelige:

- 

- 

- 

#### Generelt \<span id"General"/\>

Indstillinger, der giver mulighed for at justere specifikke grupperinger, sorteringer og visningsegenskaber for dette navn, samt at angive datoen, der svarer til navnet:

- Feltet giver en alternativ grupperingsnode for et navn i personvisningen, der tilsidesætter standardgrupperingen baseret på efternavnet. Dette kan være nødvendigt med lignende efternavne, der skal grupperes -- for eksempel betragtes de russiske navne Ivanov og Ivanova som de samme, men forskellen i køn afspejles i forskellig stavemåde. Se [Gruppering af efternavne](wiki:Gruppering_af_efternavne).
  -  Markér dette afkrydsningsfelt for at aktivere indtastning i dette felt. (afkrydsningsfelt er ikke markeret som standard)

  
Personer vises i henhold til det navneformat, der er angivet i indstillingerne (standard).

Her kan du sikre dig, at denne person vises i henhold til et brugerdefineret navneformat. *(Flere navneformater kan vælges i fanen eller tilpasses ved hjælp af fanen [Display_Name_Editor](wiki:Da:Gramps_6.0_brugsanvisning_-_Indstillinger#Display_Name_Editor).)*

- og bestemmer, hvordan navnet vises i personvisningen og rapporterne. Sorteringen giver dig mulighed for at tilsidesætte navnemønsteret, der er angivet i Gramps-indstillingerne, i sorteringen af ​​navnet. For eksempel har du pludselig en gren af ​​svenske navne med fornavn og patronym, men resten af ​​din database sorterer navne efter Efternavn, Fornavn. Du kan her angive, at dette navn altid skal sorteres som patronym, Fornavn.

  
Her kan du sikre dig, at denne person er sorteret efter et brugerdefineret navneformat. *(Flere navneformater kan vælges i fanen eller tilpasses ved hjælp af fanen [Display_Name_Editor](wiki:Da:Gramps_6.0_brugsanvisning_-_Indstillinger#Display_Name_Editor).)*.

giver dig mulighed for at angive, hvordan navnet vises. Du kan for eksempel sortere et navn baseret på en persons fornavn eller efternavn, men stadig have visningen til at vise en ærestitel før navnet. *(Flere navneformater kan vælges i fanen eller tilpasses ved hjælp af [Display_Name_Editor](wiki:Da:Gramps_6.0_brugsanvisning_-_Indstillinger#Display_Name_Editor).)*

Persontrævisningen grupperer personer under det primære efternavn. Du kan tilsidesætte dette ved at angive en gruppeværdi her. Du vil blive spurgt, om du kun vil gruppere denne person eller alle personer med dette specifikke primære efternavn.

- kan give information om gyldigheden af ​​dette navn -- brug datointervaller efter behov. Ikonet for redigering af dato åbner [Datoredigering](wiki:Da:Gramps_6.0_brugsanvisning_-_Indtaste_og_redigere_data:_detaljeret_-_del_1#Editing_dates). F.eks. For et gift navn skal du indtaste datoen, hvor navnet først bruges, eller vielsesdatoen.

#### Kildehenvisninger <span id="Source Citations"/>

Fanen viser information om kilder og kildehenvisninger, der er relevante for dette navn, og styrer, hvordan det kan ændres. Den centrale del viser en liste over alle sådanne kildehenvisninger og kilder, der er gemt i databasen. Knapperne , og giver dig mulighed for at tilføje, ændre og fjerne en henvisning til dette navn. Bemærk, at knapperne og kun bliver tilgængelige, når en kildehenvisning er valgt fra listen.

Mere information: [Redigering af kildehenvisninger](wiki:Da:Gramps_6.0_brugsanvisning_-_Indtaste_og_redigere_data:_detaljeret_-_del_2#Editing_source_citations)

#### Noter <span id="Notes"/>

Fanen viser eventuelle noter vedrørende navnet. For at tilføje en note eller ændre eksisterende noter skal du blot redigere teksten i tekstindtastningsfeltet.

Mere information: [Noteredigering](wiki:Da:Gramps_6.0_brugsanvisning_-_Indtaste_og_redigere_data:_detaljeret_-_del_2#Editing_information_about_notes)

## Attributter <span id="Attributes"/>

Når du tilføjer eller redigerer [attributter](wiki:Attributes_in_Gramps) fra dialogboksen via fanen , vises dialogboksen . {{-}}

### Attribut-editor dialogboks <span id="Attribute Editor dialog"/>

![[_media/AttributeEditor-dialog-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;Attribut-editor&quot; - dialog - standard]] Øverst i dialogvinduet vises dialogtitlen inklusive navnet på den person, hvis attribut redigeres. Den centrale del af vinduet viser tre notesbogsfaner, der indeholder forskellige kategorier af tilgængelige oplysninger. Du kan bringe enhver fane til toppen for visning eller redigering ved at klikke på den relevante faneoverskrift. Den nederste del har knapperne og . Hvis du klikker på knappen når som helst, anvendes alle ændringer foretaget i alle faner, og dialogvinduet lukkes. Hvis du klikker på knappen når som helst, lukkes vinduet uden at foretage ændringer.

Den øverste sektion giver mulighed for redigering af de mest generelle oplysninger om attributten:

- (`Identifikationsnummer`standard) Navnet på en attribut, du vil bruge. For eksempel: *Højde* (for en person), *Vejret på denne dag* (for en begivenhed), ... Brug dette til at gemme uddrag af information, du indsamler og ønsker at linke korrekt til kilder. Attributter kan bruges til personer, familier, begivenheder og medier. Oplysningerne kan indtastes i de relevante tekstfelter. Attributnavnet kan også vælges fra tilgængelige valg (hvis nogen) i rullemenuen .

  - Slå dette til/fra for at markere denne attributpost som privat eller offentlig. Dette giver dig mulighed for at udelade denne attribut fra at blive inkluderet i rapporterne, hvis du vælger det blandt rapportgenereringsmulighederne.

- Almindelig tekstbeskrivelse af attributten. F.eks. *1,8 m, solrig eller blå øjne*.

{{-}}

#### Attribut-editor kontekstuel menu <span id="Attribute Editor context menu"/>

{{-}}

### Attribut-editorens fane sider <span id="Attribute Editor tab pages"/>

Følgende faner findes:

- [Noter](#Notes_2)
- [Kildehenvisninger](#Source_Citations_2)

#### Kildehenvisninger <span id="Source Citations"/>

  
Fanen viser oplysninger om citater og kilder, der er relevante for denne attribut, og styrer, hvordan den kan ændres. Den centrale del viser en liste over alle sådanne kilder og kildehenvisninger, der er gemt i databasen. Knapperne , og giver dig mulighed for at tilføje, ændre og fjerne en kildehenvisning til denne attribut. Bemærk, at knapperne og kun bliver tilgængelige, når en kilde/kildehenvisning er valgt fra listen.

#### Noter <span id="Notes"/>

  
Fanen viser eventuelle noter vedrørende attributten. For at tilføje en note eller ændre eksisterende noter skal du blot redigere teksten i tekstindtastningsfeltet.

{{-}}

## Adresser <span id="Addresses"/>

Når du tilføjer eller redigerer en adresse fra dialogboksen via fanen , vises dialogboksen . {{-}}

### Adresse-editor dialogboks <span id="Address Editor dialog"/>

![[_media/AddressEditor-dialog-default-60-da.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;Adresse-editor: - dialog - default]] Dialogboksen giver mulighed for at registrere en aktuel adresse ved at registrere oplysningerne i de relevante tekstfelter.

Den øverste del af dialogboksen giver mulighed for redigering og indtastning af oplysninger om adressen:

- Dato, hvor adressen er gyldig.

  - Knappen ![[_media/22x22-gramps-date.png]] starter dialogboksen .

- Gaden for adressen.

- Knappen . Slå denne knap til/fra for at markere denne adressepost som privat eller offentlig. Dette giver dig mulighed for at udelade denne adresse fra at blive inkluderet i rapporter, hvis du vælger det blandt rapportgenereringsmulighederne.

- Adressens lokalitetsnavn.

- Staten eller amtet for adressen, hvis en adresse skal indeholde dette.

- Landsbyen eller byen for adressen.

- Land for adressen.

- Postnummer.

- Telefonnummer knyttet til adressen.

Nederst i dialogboksen finder du knapperne , og . Hvis du klikker på knappen når som helst, anvendes alle ændringer foretaget i alle faner, og dialogboksvinduet lukkes. Hvis du klikker på knappen når som helst, lukkes vinduet uden at anvende nogen ændringer. {{-}}

### Adresse-editorens fane sider <span id="Address Editor tab pages"/>

De følgende faner indeholder forskellige kategorier af tilgængelige oplysninger. Du kan bringe enhver fane øverst til visning eller redigering ved at klikke på den relevante fanebladoverskrift.

#### Kildehenvisninger <span id="Source Citations"/>

  
Fanen viser oplysninger om kilder, der er relevante for denne adresse, og styrer, hvordan den kan ændres. Den centrale del viser en liste over alle sådanne kilder og citater, der er gemt i databasen. Knapperne , og giver dig mulighed for at tilføje, ændre og fjerne en citat/kildehenvisning til denne adresse. Bemærk, at knapperne og kun bliver tilgængelige, når en kildehenvisning er valgt fra listen.

#### Noter <span id="Notes"/>

  
Fanen viser eventuelle noter vedrørende adressen. For at tilføje en note eller ændre eksisterende noter skal du blot redigere teksten i tekstindtastningsfeltet.

{{-}}

## Sammefletning af poster <span id="Merging records"/>

![[_media/PeopleCategory-Toolbar-MergeTheSelectedPersons-icon-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;Merge the Selected Persons&quot; - Toolbar &quot;Merge...&quot; icon - example]] Nogle gange viser det sig, at flere poster i din slægtsbog beskriver det samme objekt: samme person, samme sted eller samme kildehenvisning eller kilde. Det kan ske enten når dataene indtastes to gange ved en fejl, eller når nye oplysninger afslører, at de to poster refererer til den samme person. Det kan også ske efter import af en GEDCOM fra en slægtning, hvis database overlapper med dine eksisterende data.

Når du finder dubletter, er det en nyttig måde at rette op på situationen ved at sammenlægge dem.

Generel brug: Sammenlægning af to poster udføres ved at vælge én post og derefter vælge en anden post, mens du holder Ctrl-tasten nede og enten vælger ikonet eller værktøjslinjens eller kontekstmenuen .

Følgende flettemuligheder er tilgængelige:

- [Sammenflet Personer](#Merge_Personer)
- [Sammenflet Familier](#Merge_Families)
- [Sammenflet Begivenheder](#Merge_Events)
- [Sammenflet Steder](#Merge_Places)
- [Sammenflet Kilder](#Merge_Sources)
- [Sammenflet Kildehenvisninger](#Merge_Citations)
- [Sammenflet Arkiver](#Merge_Repositories)
- [Sammenflet Medieobjekter](#Merge_Media_Objects)
- [Sammenflet Noter](#Merge_Notes)

{{-}}

### Sammenflet personer <span id="Merge People"/>

![[_media/MergePeople-dialog-default-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Merge People" dialog - with "Context Information" section expanded by default - example]]

Når præcis to personer er valgt, skal du vælge for at åbne dialogboksen .

Dialogboksen giver dig mulighed for at beslutte, om de valgte poster skal flettes sammen. Hvis du beslutter, at posterne ikke skal flettes sammen, på trods af lignende navne, kan du klikke på knappen for at lukke dialogboksen uden at foretage ændringer.

Du kan udvide felterne nederst til venstre for at vise flere oplysninger, som du yderligere kan bestemme, hvilke oplysninger der skal beholdes i fletningen.

Feltet nederst til venstre viser flere oplysninger om de personer, der skal flettes sammen.

Hvis du beslutter dig for at fortsætte med sammenlægningen, skal du vælge den relevante persons ![[_media/RadioButton_Selected.png]] radioknap for at angive den post

- Navn
- Køn
- Gramps ID

der skal bruges som kilde til primære data, og derefter klikke på . Dataene fra den anden post vil blive gemt som alternative data.

Specifikt vil alle navne fra den anden post blive alternative navne for den sammenflettede post. Tilsvarende vil forældre, ægtefæller og børn i den anden post blive alternative forældre, ægtefæller og børn i den sammenlagte post osv.

Se også:

- [Find mulige dubletter](wiki:Gramps_6.0_Wiki_Manual_-_Tools/da#Find_Possible_Duplicate_People)
- [Merging people](wiki:Merging_people)

{{-}} ![[_media/MergePeople-dialog-sections-expanded-example-60.png|Fig. {{#var:kapitel}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Dialogboksen &quot;Flet personer&quot; - med sektionerne &quot;Detaljeret valg&quot; og &quot;Kontekstoplysninger&quot; udvidet - eksempel]] {{-}}

### Sammenflet familier <span id="Merge Families"/>

![[_media/MergeFamilies-dialog-default-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Merge Families" - dialog - default example]]

Når præcis to familier er valgt, skal du vælge for at åbne dialogboksen .

Dialogboksen giver dig mulighed for at beslutte, om de valgte poster skal flettes sammen. Hvis du beslutter, at posterne ikke skal flettes sammen, på trods af at de ligner hinanden, kan du klikke på for at lukke dialogboksen uden at foretage ændringer.

Du kan enten vælge en af ​​de to familier som kilde til de primære data for den nye familie, eller ved at udvide feltet kan du individuelt vælge, hvilken far der er kilden til de primære data, hvilken mor der er kilden til de primære data, og hvilken familie (valgt af Gramps ID) der er kilden til de andre primære data.

Hvis du beslutter dig for at fortsætte med sammenlægningen, skal du vælge den/de relevante familie-radioknap(per) ![[_media/RadioButton_Selected.png]] for at angive kilden(erne) til de primære data

- Far
- Mor
- Forhold
- Gamps ID

som skal bruges til den sammenflettede familieregistrering, og derefter klikke på .

Børnene fra begge ægteskaber fusioneres ind i den nye familie. De to fædre fusioneres, og begivenhederne fra den sekundære far knyttes til den primære far. Navnene fra den sekundære far bliver alternative navne for den primære far. Det samme sker med de to mødre. Begivenhederne relateret til den sekundære familie (f.eks. ægteskab og enhver skilsmisse) overføres til den primære familie. Den sekundære familie og personregistreringen for den sekundære far og mor slettes fra databasen. ![[_media/MergeFamilies-dialog-DetailedSelection-section-expanded-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;Sammenflet Familier&quot; - dialog - med &quot;Detaljeret udvalg&quot; sektionen ekspanderet - eksempel data]] {{-}}

### Sammenflet begivenheder <span id="Merge Events"/>

![[_media/MergeEvents-dialog-example-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;Sammenflet begivenheder&quot; - dialogboks - standardeksempel]] Når præcis to begivenheder er valgt, skal du vælge for at åbne dialogboksen .

Dialogboksen giver dig mulighed for at beslutte, om de valgte poster skal flettes eller ej.

Ved at udvide feltet kan du se yderligere oplysninger om fletningen.

Hvis du beslutter, at posterne ikke skal flettes, på trods af lignende titler, kan du klikke på for at lukke dialogboksen uden at foretage nogen ændringer.

Hvis du beslutter dig for at fortsætte med fletningen, skal du vælge den relevante ![[_media/RadioButton_Selected.png]] radioknap for at angive:

- Type
- Dato
- Sted
- Beskrivelse
- Gramps ID

som skal bruges til den flettede post, og derefter klikke på {{-}} ![[_media/MergeEvents-dialog-DetailedSelection-section-expanded-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Dialogboksen &quot;Sammenflet begivenheder&quot; - med afsnittet &quot;Detaljeret udvalg&quot; udvidet - eksempel]] {{-}}

### Sammenflet steder <span id="Merge Places"/>

![[_media/MergePlaces-dialog-example-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;Sammenflet steder&quot; - dialogboks - standardeksempel]] Når præcis to steder er valgt, skal du vælge for at åbne dialogboksen .

Dialogboksen giver dig mulighed for at beslutte, om de valgte poster skal flettes eller ej.

Ved at udvide feltet kan du se yderligere oplysninger om fletningen.

Hvis du beslutter, at posterne ikke skal flettes, på trods af lignende titler, kan du klikke på for at lukke dialogboksen uden at foretage nogen ændringer.

Hvis du beslutter dig for at fortsætte med fletningen, skal du vælge den relevante ![[_media/RadioButton_Selected.png]] radioknap for at angive:

- Navn
- Type
- Kode
- Breddegrad
- Længdegrad
- Gramps ID

som skal bruges til den sammenflettede post, og derefter klikke på . {{-}} ![[_media/MergePlaces-dialog-DetailedSelection-section-expanded-example-60.png|Fig. {{#var:kapitel}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Dialogboksen &quot;Sammenflet steder&quot; - med sektionen &quot;Detaljeret udvalg&quot; udvidet - eksempel]] {{-}}

#### Kan ikke flette steder - cyklus i stedhierarkiet - advarselsdialogboks

Hvis du forsøger at flette to (2) steder, der ville resultere i en løkke i stedhierarkiet, vil du blive vist advarselsdialogboksen med meddelelsen *Sammenfletning af disse steder ville oprette en uendelig løkke i stedhierarkiet.* For eksempel ville et forsøg på at flette et land på øverste niveau med en af ​​de tilknyttede byer vise: ![[_media/Cannot-merge-places-cycle-in-place-hierarchy-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}}  advarselsdialog med meddelelsen Fletning af disse steder ville oprette en løkke i stedhierarkiet. eksempel]] {{-}}

### Sammenflet kilder <span id="Merge Sources"/>

![[_media/MergeSources-dialog-example-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;Sammenflet kilder&quot; - dialogboks - standardeksempel]] Når præcis to kilder er valgt, skal du vælge for at åbne dialogboksen .

Ved at udvide feltet kan du se yderligere oplysninger om fletningen.

Dialogboksen giver dig mulighed for at beslutte, om de valgte poster skal flettes eller ej.

Hvis du beslutter, at posterne ikke skal flettes, på trods af lignende titler, kan du klikke på for at lukke dialogboksen uden at foretage nogen ændringer.

Hvis du beslutter dig for at fortsætte med fletningen, skal du vælge den relevante ![[_media/RadioButton_Selected.png]] radioknap for at angive:

- Titel
- Forfatter
- Forkortet - titel
- Publikation - information
- Gramps ID

som skal bruges til den flettede post, og derefter klikke på . {{-}} ![[_media/MergeSources-dialog-DetailedSelection-section-expanded-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;Sammenflet kilder&quot; - med afsnittet &quot;Detaljeret udvalg&quot; udvidet - dialog - eksempel]] {{-}}

### Sammenflet kildehenvisninger <span id="Merge Citations"/>

![[_media/MergeCitations-dialog-example-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;Sammenflet kildehenvisninger&quot; - dialogboks - standardeksempel]] Når præcis to kildehenvisninger er valgt [med identiske kilder](#Cannot_merge_citations._with_different_sources_warning_dialog), skal du vælge for at åbne dialogboksen .

Ved at udvide feltet kan du se yderligere oplysninger om fletningen.

Dialogboksen giver dig mulighed for at beslutte, om de valgte poster skal flettes eller ej.

Hvis du beslutter, at posterne ikke skal flettes, på trods af lignende titler, kan du klikke på for at lukke dialogboksen uden at foretage ændringer.

Hvis du beslutter dig for at fortsætte med sammenfletteningen, skal du vælge den relevante ![[_media/RadioButton_Selected.png]] radioknap for at angive:

- Volumen/Side
- Dato
- Konfidens
- Gramps ID

der skal bruges til den flettede post, og derefter klikke på . {{-}} ![[_media/MergeCitations-dialog-DetailedSelection-section-expanded-example-60.png|Fig. {{#var:kapitel}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;Sammenflet kildehenvisninger&quot; - med sektionen &quot;Detaljeret valg&quot; udvidet - dialogboks - eksempel]] {{-}} Se også:

- [Flet citater...](wiki:Gramps_6.0_Wiki_Manual_-_Tools#Merge_citations) Værktøj.

#### Kan ikke flette kildehenvisninger. med advarselsdialogboks om forskellige kilder <span id="Cannot_merge_citations._with_different_sources_warning_dialog"/>

![[_media/Cannot-merge-citations-with-different-sources-warning-dialog-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}}  -med-forskellige-kilder- advarselsdialogboks - eksempel]]

Bemærk, at de to valgte kildehenvisninger enten skal dele den samme kilde, eller at kun én eller ingen af ​​kildehenvisningerne har en tilknyttet kilde. Ellers vil du, når du vælger at flette, blive vist advarselsdialogboksen med rådet *Hvis du vil flette disse to kildehenvisninger, skal du først flette kilderne.*. {{-}}

### Sammenflet arkiver <span id="Merge Repositories"/>

![[_media/MergeRepositories-dialog-example-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;Sammenflet arkiver&quot; - dialogboks - standardeksempel]] Når præcis to arkiver er valgt, skal du vælge for at åbne dialogboksen .

Ved at udvide feltet kan du se yderligere oplysninger om fletningen.

Dialogboksen giver dig mulighed for at beslutte, om de valgte poster skal flettes eller ej.

Hvis du beslutter, at posterne ikke skal flettes, på trods af lignende titler, kan du klikke på for at lukke dialogboksen uden at foretage nogen ændringer.

Hvis du beslutter dig for at fortsætte med fletningen, skal du vælge den relevante ![[_media/RadioButton_Selected.png]] radioknap for at angive:

- Navn
- Type
- Gramps ID

som skal bruges til den flettede post, og derefter klikke på {{-}} ![[_media/MergeRepositories-dialog-DetailedSelection-section-expanded-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;Sammenflet arkiver&quot; - med sektionen &quot;Detaljeret udvalg&quot; udvidet - dialog - eksempel]] {{-}}

### Sammeflet medie objekter <span id="Merge Media Objects"/>

![[_media/MergeMediaObjects-dialog-example-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;Sammeflet medieobjekter&quot; - dialogboks - standardeksempel]] Når præcis to medieobjekter er valgt, skal du vælge for at åbne dialogboksen .

Ved at udvide feltet kan du se yderligere oplysninger om fletningen.

Dialogboksen giver dig mulighed for at beslutte, om de valgte poster skal flettes eller ej.

Hvis du beslutter, at posterne ikke skal flettes, på trods af lignende titler, kan du klikke på for at lukke dialogboksen uden at foretage nogen ændringer.

Hvis du beslutter dig for at fortsætte med fletningen, skal du vælge den relevante ![[_media/RadioButton_Selected.png]] radioknap for at angive:

- Titel
- Sti
- Dato
- Gramps ID

som skal bruges til den flettede post, og derefter klikke på {{-}} ![[_media/MergeMediaObjects-dialog-DetailedSelection-section-expanded-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;Sammeflet medieobjekter&quot; - med sektionen &quot;Detaljeret udvalg&quot; udvidet - dialog - eksempel]] {{-}}

### Sammenflet noter <span id="Merge Notes"/>

![[_media/MergeNotes-dialog-example-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;Sammenflet noter&quot; - dialogboks - standardeksempel]] Når præcis to noter er valgt, skal du vælge for at åbne dialogboksen .

Ved at udvide feltet kan du se yderligere oplysninger om fletningen.

Dialogboksen giver dig mulighed for at beslutte, om de valgte poster skal flettes eller ej.

Hvis du beslutter, at posterne ikke skal flettes, på trods af lignende titler, kan du klikke på for at lukke dialogboksen uden at foretage nogen ændringer.

Hvis du beslutter dig for at fortsætte med fletningen, skal du vælge den relevante ![[_media/RadioButton_Selected.png]] radioknap for at angive:

- Tekst
- Type
- Format
- Gramps ID

som skal bruges til den sammenflettede post, og derefter klikke på {{-}} ![[_media/MergeNotes-dialog-DetailedSelection-section-expanded-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Dialogboksen &quot;Sammenflet noter&quot; - med sektionen &quot;Detaljeret udvalg&quot; udvidet - eksempel]]

{{-}}

[Category:Documentation](wiki:Category:Documentation)
