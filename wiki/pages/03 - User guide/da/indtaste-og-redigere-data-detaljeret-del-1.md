---
title: 'Da:Gramps 6.0 brugsanvisning - Indtaste og redigere data: detaljeret - del
  1'
categories:
- Documentation
- Pages using invalid self-closed HTML tags
- Stub
managed: false
source: wiki-scrape
wiki_revid: 128975
wiki_fetched_at: '2026-05-30T17:07:10Z'
lang: da
---

{{#vardefine:chapter\|9.1}} {{#vardefine:figure\|0}} **<span style="font-size:120%">Indtastning og redigering af data: detaljeret Personer, Slægtsforhold, Datoer</span>**  
Afsnittet udvider den [korte oversigt](wiki:Da:Gramps_6.0_brugsanvisning_-_Indtaste_og_redigere_data:_kort) over, hvordan man indtaster og redigerer data i Gramps.

Gramps tilbyder dig en række visninger. Hver af disse visninger giver dig mulighed for at indtaste og redigere oplysninger. Faktisk kan du ofte få adgang til de samme oplysninger fra forskellige visninger.

I Gramps indtastes og redigeres information gennem det, vi kalder dialogbokse. Da vi bruger dette udtryk ofte, bør vi definere, hvad vi mener med det:

En dialogboks er et pop op-vindue, der indeholder en eller flere formularer til indtastning og redigering af data, der passer til en bestemt kategori. Eksempler i Gramps inkluderer dialogboksen og dialogboksen , blandt mange andre.

En dialogboks indeholder ofte en række "[notesbogsfaner](https://wikipedia.org/wiki/Tab_(interface))", der grupperer informationen i underkategorier. For eksempel har dialogboksen notesbogsfaner til underkategorier såsom begivenheder, attributter, adresser og noter, blandt andre.

## Redigering af oplysninger om personer <span id="Editing_information_about_people"/>

Oplysninger om personer indtastes og redigeres via dialogboksen . Denne dialogboks, også kaldet personredigeringsdialogboksen, kan vises fra forskellige visninger på følgende måder:

- Fra [Personkategori](wiki:Da:Gramps_6.0_brugsanvisning_-_Navigation#Brug_af_kategorien_Personer):

  
  
Dobbeltklik på navnet på den person, hvis data du vil redigere

Vælg navnet med et enkelt klik, og klik derefter på knappen på værktøjslinjen.

Vælg navnet, og tryk derefter på **Enter**.

Vælg Rediger... fra menuen Rediger i Gramps

Vælg Rediger fra den kontekstmenu, der vises, når du højreklikker på navnet.

- Fra [Slægtsforhold kategori](wiki:Da:Gramps_6.0_brugsanvisning_-_Navigation#Brug_af_kategorien_Slægtsforhold): For at redigere den aktive persons data skal du klikke på knappen ved siden af ​​den aktive persons navn.

<!-- -->

- Fra [Tavler kategori](wiki:Da:Gramps_6.0_brugsanvisning_-_Navigation#Brug_af_Tavler_kategorien): Dobbeltklik i feltet med navnet på den person, hvis data du vil redigere.

Enhver af disse metoder vil vise dialogboksen .

{{-}} <span id="Rediger person-dialog">

### Person-editor-dialog <span id="Edit_Person_dialog"/>

</span> ![[_media/Edit-person-window-new-person-example-60-da.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Rediger person - vindue - Standard Ny tom editor]]

![[_media/Edit-person-window-existing-person-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}}  dialogboks - viser eksempelperson]]

I dialogboksen kan du enten tilføje oplysninger om en ny person eller redigere en eksisterende person.

Toppen af ​​vinduet har to dele: De grundlæggende oplysninger om personens , og en sektion med privatlivsknappen (for at indstille posten som privat), kønsvælgeren, et ID, du kan give denne post, og et mærkat, du kan tildele personen, der angiver postens status (f.eks. fuldført, TODO, usikker, ....), hvilket vil give denne post en bestemt farve i personlistevisningen. {{-}}

Under denne øverste sektion er der flere "[faner](#Edit_Person_tab_pages)", der indeholder forskellige kategorier af tilgængelige oplysninger. Klik på en hvilken som helst fane for at se og redigere dens indhold.

Hvis du klikker på knappen nederst, anvendes alle ændringer foretaget i alle faner, og dialogboksen lukkes. Hvis du klikker på knappen , lukkes vinduet uden at anvende nogen ændringer.

{{-}} ![[_media/SaveChanges-alert-dialog-60-da.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;Gem ændringer?&quot; - advarselsdialog]]

Hvis data i faner er blevet ændret, vises et advarselsvindue, der beder dig om at vælge mellem følgende muligheder:

- \- ændringer.

- (standard) - den oprindelige anmodning om annullering.

- \- ændringerne.

samt et afkrydsningsfelt for at angive , som kan deaktiveres fra indstillingen i dialogboksen .

#### Person Editor kontekstmenu

![[_media/QuickViewReport-EditPerson-context-menu-popup-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}}  dialogboks - viser undermenuen for hurtig visning]] Ved at bruge kontekstmenuen (højreklikke) fra et tomt område i den øverste del af vinduet, f.eks.: nær feltet "Foretrukket navn" eller under "Foretrukket billede"; Du vil blive præsenteret for en kontekstmenu med følgende muligheder:

<hr>

- \-

- \-

<hr>

- rapporter er tilgængelige.

  - 

  - 

  - 

  - 

  - 

  - 

  - 

  - 

<hr>

Kvikoversikten kan indeholde flere rapporter afhængig af installerede gramplets.

{{-}}

### Foretrukket billede

![[_media/EditPerson-top-sections-image-with-context-menu-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Eksempel på "Billede"-sektion med kontekstmenu til dialogboksen "Rediger person"]]

Hvis der findes billeder, viser personeditoren et ekstra område i øverste venstre område (ellers er det skjult). Dette -område viser det første billede, der er tilgængeligt i fanen for denne person.

Se også

- [Ikon for 'brudt link' i manglende medieobjekter, der viser en boks med et rødt 'x'](wiki:Da:Gramps_6.0_brugsanvisning_-_Indstillinger#Manglende_medieobjekter_&#39;brudt_link&#39;_ikon_af_en_boks_med_et_rødt_&#39;x)

#### Kontekstmenu for personredigering af billeder

Du kan højreklikke på billedet for at vise følgende indstillinger i kontekstmenuen for billeder:

- \- åbner billedet i en eksternt tilknyttet billedfremviser.

- \- åbner dialogboksen .

{{-}}

### Foretrukket navn-sektion

![[_media/EditPerson-PreferredName-section-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Foretrukket navn"-sektion i "Rediger person" - dialogboks - standard]]

![[_media/Edit-person-window-existing-person-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Afsnittet "Foretrukket navn" (Ved siden af ​​billedet) i dialogboksen "Rediger person" - eksempel]]

Det foretrukne navn eller standardnavnet er det navn, der vil blive brugt i Gramps til personens '[navn](wiki:Names_in_Gramps)'. Du kan indstille i [Gramps-indstillinger](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Display_Options), hvordan et navn vises, og generelt behøver du kun at indtaste data i felterne vist i afsnittet for foretrukne navne.

Nogle detaljerede rapporter (tekstbaserede og fortællende webstedsgeneratorer) viser også de alternative navne. Bemærk dog, at søgning på et navn vil søge i alle navne, der er knyttet til en person, ikke kun det foretrukne navn.

Afsnittet for foretrukne navne indeholder de typiske navneoplysninger, du vil redigere ved oprettelse af en person. For at reducere rod er de mindre hyppigt nødvendige felter (for [Flere efternavne](wiki:D#Flere_efternavne) og [Alternative Navne](#Navne)) som standard skjult. For at udvide sektionen for flere efternavne skal du klikke på knappen   eller bruge dens [keybinding](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings#Editor_bindings). Med flere navne kan en forbindelse (såsom en bindestreg eller [non-breaking space](https://en.wikipedia.org/wiki/Non-breaking_space)) angives for at bygge bro mellem efternavnene for at skabe sammensatte (også kendt som "[double-barreled](https://en.wikipedia.org/wiki/Double-barreled_name)") efternavne. For at se hele udvalget af data, du kan gemme om et navn, skal du klikke på knappen   i nederste højre hjørne af sektionen eller bruge dens [keybinding](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings#Editor_bindings). Dette vil vise [Navneeditor](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_3#Name_Editor).

Navnefelterne for det foretrukne navn i er:

- af navnet. Foruddefinerede typer inkluderer: Også kendt som **Fødenavn** *(standard)*, Gift navn, Ukendt. Du kan også skrive oven i dette indtastningsfelt for at oprette dine egne [Brugerdefinerede typer](wiki:Gramps_Glossary/da#custom) (f.eks. kaldenavn, kort navn osv.).

Det anbefales, at det foretrukne navn er et registreret fødselsnavn eller et andet navn med juridisk status. Det er navne, der oftest findes på citerbare dokumenter. Du kan vælge at gemme andre navnetyper i fanen i .

- , personens fornavn(e)

- , et valgfrit suffiks til navnet, såsom *Jr.* eller *III*

- , den del af en persons navn, der angiver den familie, som personen tilhører.

  - Hvis du vælger knappen  , vises indtastningsfeltet i sektionen , hvor du kan indtaste sammensatte efternavne (f.eks. til patronymer eller sammensatte matrilineære-patriliniale navne).

- , et valgfrit præfiks for familienavnet, der ikke bruges i sortering, såsom *de* eller *van*.

- , navnets type [oprindelse](wiki:Gramps_Glossary/da#name_origin) identificerer det kulturelle navngivningssystem, der angiver, hvordan et bestemt efternavn blev valgt. Dette er metainformation om efternavnet, som kan være vigtig i slægtsforskning.

- , som er en titel (typisk i forkortet form), der bruges til at henvise til personen, såsom *Dr.* eller *Pastor*, selector,

- , er et beskrivende navn givet i stedet for eller i tillæg til det officielle fornavn. Hvis et kaldenavn er en fuld navnekonstruktion, skal du bruge en specifik navnetype *Også kendt som* i stedet for kaldenavnsfeltet.

<!-- -->

- , officielt er dette den del af fornavnet, der er det normalt anvendte navn. F.eks. kan en person have 3 fornavne som i *Jean Baptiste Jules*, hvor der i virkeligheden kun bruges *Baptiste*. I Tyskland og nogle andre steder var det almindeligt at understrege kaldenavnet blandt de forskellige fornavne, se også [her](wiki:Names_in_Gramps#Call_Name). Nogle personer vil forsøge at bruge dette felt også til kaldenavn eller ændringer af fornavnet (som Cristy for Cristina), men dette er ikke den tilsigtede anvendelse. Et kaldenavn er et korrekt juridisk navn. For kaldenavne eller korte navnevarianter bør du oprette et alternativt navn med en anden type.

På [Navneeditor](wiki:Da:Gramps_6.0_brugsanvisning_-_Indtaste_og_redigere_data:_detaljeret_-_del_3#Navneeditor) er der et ekstra felt tilgængeligt: ​​. Dette er et uofficielt navn, der gives til en familieudbrydergruppe for at skelne dem fra personer med samme efternavn. Ofte omtalt som gårdnavn og refererer typisk til et sted, hvor udbrydergruppen bor eller stammer fra. (også kendt som sept, sekt, lejr)

Felterne og giver en "[autocompletion](https://wikipedia.org/wiki/Autocomplete)"-funktion: Når du skriver i disse felter, vises en menu under feltet, der indeholder databaseposter, der matcher din delvise input. Dette giver dig en genvej ved at lade dig vælge en post, der allerede findes i databasen, i stedet for at skulle skrive det hele ud. Du kan vælge posten ved hjælp af musen eller ved hjælp af piletasterne og .

Søgning i de mange navnefelter kan være bredt eller præcist målrettet. Brug feltet Navn i kategorien Personer [Filter](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#People_Filter) gramplet til at søge i alle felterne samtidigt. Eller brug reglen [Personer med <navn>](wiki:Gramps_6.0_Wiki_Manual_-_Filters#People_with_the_.3Cname.3E) til at oprette et brugerdefineret filter til at søge efter hvert element individuelt. {{-}}

### Flere efternavne

![[_media/EditPerson-MultipleSurnames-entry-section-default-60.png|Fig. {{#var:kapitel}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Afsnittet "Flere efternavne" i dialogboksen "Rediger person" - standard]]

![[_media/Edit-person-window-existing-person-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Flere efternavne"-sektionen i dialogboksen "Rediger person" - eksempel]]

Når knappen tilføj (Brug flere efternavne) er blevet trykket yderst til højre for rækken i vinduet , vises et nyt indtastningsfelt i sektionen , hvor du kan indtaste sammensatte efternavne. Alternativt kan [Tilføj-knappens editor-tastebinding](wiki:Da:Gramps_6.0_brugsanvisning_-_Tastaturgenveje#Editor_bindings) bruges.

Du kan tilpasse højden på feltet i dialogboksen . Vælg fanen [](wiki:Da:Gramps_6.0_brugsanvisning_-_Indstillinger#Environment_Settings) og ret feltet **Højde på feltet flere efternavne**.

Funktionen [Flere efternavne](https://gramps-project.org/blog/2010/11/final-multiple-surnames/) kan bruges til patronymer eller sammensatte matrilineære og patrilineære navne. En anden variation ville være et skandinavisk navn som 'Syver Eriksen Skotterud', hvor det fulde navn er sammensat af et fornavn (Syver), en henvisning til hans far (Ericksen eller søn af Erick) sammen med et landsby- eller lokalitetsnavn. I et sådant tilfælde kan du tilføje 'Ericksen' med en [Origin](wiki:Names_in_Gramps#Origin_Attributes) på "Patronymic" og udvide til flere efternavne ved at tilføje 'Skotterud' med en oprindelse på "Location".

Hvis du ikke tilføjer nogen oplysninger i dette afsnit, vil det blive skjult, næste gang dialogboksen Rediger person åbnes. Tomme rækker gemmes ikke.

Se også:

- [Funktionen Flere efternavne](https://gramps-project.org/blog/2010/11/final-multiple-surnames/) - Introduktion til blogindlæg på Gramps' hjemmeside.

{{-}}

#### Kontekstmenu for afsnittet Flere efternavne

- \-

- \-

- \-

{{-}}

### Generelt sektion

![[_media/EditPerson-General-section-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Generelt"-sektionen i dialogboksen "Rediger person" - eksempel]]

Sektionen Generelt har følgende muligheder, du kan ændre:

- [Privatliv](#Privatliv)
- [Køn](#Køn)
- [ID](#ID)
- [Mærkater](#Mærkater)

#### Privatliv

- Privatlivsfunktionen Med hængelås-ikonet kan du markere, om personens optegnelse betragtes som offentlig eller privat.

Optegnelser vises med  
![[_media/22x22-gramps-unlock.png]] ulåst hængelås som standard, når den er offentlig; og en ![[_media/22x22-gramps-lock.png]] låst hængelås, når den er privat. Ved at klikke på hængelås-ikonet skiftes der mellem offentlige og private flag.

{{-}}

#### Køn

- Menuen giver mulighed for at vælge personens køn:
  - *kvinde*
  - *mand*
  - **ukendt** (Standard)
  - *andet*

Hvis kønnet efterlades som , vises dialogboksen .

Se værktøjet [Genopbyg kønsstatistik](wiki:Da:Gramps_6.0_brugsanvisning_-_Værktøjer#Genopbyg_kønsstatistik) og [Dump kønsstatistik](wiki:Da:Gramps_6.0_brugsanvisning_-_Værktøjer#Dump_kønsstatistik) fejlfinding.

##### Dialogboks med angivet ukendt køn

![[_media/Unknown-gender-specified-dialog-60-da.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Dialogboksen "Ukendt køn angivet"]]

Dialogboksen vil advare dig om, at personens køn i øjeblikket er ukendt. Normalt er dette en fejltagelse. Angiv venligst kønnet ved at vælge mellem , , , for at bekræfte. {{-}}

#### ID

- Feltet viser [Gramps ID](wiki:Da:Gramps_6.0_brugsanvisning_-_Indstillinger#Gramps_ID)-nummeret, som identificerer brugeren i slægtstræet unikt. Denne værdi hjælper dig med at skelne mellem personer, der har samme navn. Du kan indtaste en hvilken som helst unik værdi, du ønsker. Hvis du ikke angiver en værdi, vil Gramps automatisk vælge en værdi for dig, eller skabelonen til generering af ID'er kan ændres til et format, der passer.
  - Brug for at navigere.

#### Mærkater

- Området viser dine brugerdefinerede mærkater, der angiver grundlæggende oplysninger om status for din forskning.
  - Knappen åbner dialogboksen , der lader dig fjerne eller tildele eksisterende brugerdefinerede tags.

{{-}}

### Rediger Person faner

Fanerne afspejler følgende kategorier af personoplysninger:

- (standard)

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

#### Begivenheder <span id="Events"/>

![[_media/EditPerson-Events-tab-example-60-da.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Fanen "Begivenheder" fra "Rediger person" - dialog - eksempel]]

  
Fanen giver dig mulighed for at se og redigere alle begivenheder, der er relevante for personen. Den nederste del af vinduet viser alle sådanne begivenheder, der er gemt i databasen, og viser følgende kolonner: `Type, Beskrivelse, Dato, Sted, Primære deltagere, Kilde (bogikon), Privat (låseikon), Rolle, ID og Alder`. Den øverste del viser detaljerne for den aktuelt valgte begivenhed på listen (hvis nogen). Knapperne , og giver dig mulighed for at tilføje, ændre og fjerne en begivenhedspost fra databasen. Bemærk, at knapperne og kun bliver tilgængelige, når en begivenhed er valgt fra listen. Knapperne Op "^" eller Ned "v" giver dig mulighed for at "Flytte den valgte begivenhed opad/nedad eller ændre familiens rækkefølge" for den valgte linje. For familierelationer kan du også bruge dialogboksen .

<!-- -->

  
Når du bruger knappen , vises vælgerdialogboksen , der giver dig mulighed for at vælge en allerede eksisterende begivenhed og redigere den i dialogboksen .

Når du tilføjer en ny begivenhed eller redigerer en eksisterende begivenhed, vises dialogboksen . {{-}}

##### Vælg begivenhedsvælger

![[_media/SelectEvent-selector-dialog-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Vælg begivenhed - vælger - eksempel]]

Vælgerdialogboksen giver dig mulighed for at linke til en allerede eksisterende begivenhed, og når den er valgt, åbnes den i dialogboksen .

Følgende kolonner vises: `Type` (standard sortering for liste), `Hoveddeltagere`, `Dato`, `Sted`, `Beskrivelse`, `ID`, `Seneste ændring`.

Du kan bruge knappen til at filtrere listen baseret på en af ​​mulighederne fra rullelisten:

- **Typen indeholder** (standard)
- *Typen indeholder ikke*
- *Hoveddeltagere indeholder*
- *Hoveddeltagere indeholder ikke*
- *Dato indeholder ikke*
- *Dato indeholder ikke*
- *Sted indeholder*
- *Sted indeholder ikke*
- *Beskrivelse indeholder*
- *Beskrivelse indeholder ikke*
- *ID indeholder*
- *ID indeholder ikke*
- *Seneste ændring indeholder*
- *Seneste ændring indeholder ikke*

Brug knappen til at nulstille filteret. {{-}}

#### Navne <span id="Names"/>

![[_media/EditPerson-Names-tab-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Fanen "Navne" fra "Rediger person" - dialogboks - eksempel]]

  
Fanen giver mulighed for at se og redigere eventuelle alternative navne, som personen måtte have. Navnet, der vises øverst i dialogboksen [Rediger person](#Editing_information_about_people) er det og er normalt (men ikke nødvendigvis) fødenavnet. kan være andre [Navnetyper](wiki:Names_in_Gramps#Name_Types) for aliasser ('Også kendt som' navnetype) for adopterede navne, pen-navne, kunstnernavne eller juridiske navneændringer. (Fordi det er så almindeligt, er der en separat aliasnavnetype for "Gift navn".) Hvis der findes alternative navne, kan datointervaller indstilles for hvert. Så et "Fødenavn" kan bruge ét interval (før adoptionsdatoen), og et "Også kendt som" vil have et andet interval (efter adoptionsdatoen). Alternative navne kan også være stavevarianter, herunder engelske versioner af fødselsnavnet og almindelige stavefejl.

<!-- -->

  
Den nederste del af vinduet viser alle alternative navne for den person, der er gemt i databasen. Den øverste del viser detaljerne for det aktuelt valgte navn på listen (hvis nogen). Knapperne (add), (edit) og (remove) tillader tilføjelse, ændring og fjernelse af et alternativt navn fra databasen. Dobbeltklik på en række er det samme som at vælge og klikke på knappen (edit). Bemærk, at knapperne og kun bliver tilgængelige, når et alternativt navn er valgt fra listen.

<!-- -->

  
Enhver række i de alternative navne kan indstilles til det foretrukne navn fra kontekstmenuen. Højreklik på det alternative navn, og vælg menupunktet . Rækken med alternative navne vil blive byttet om til afsnittet med foretrukket navn, og det tidligere foretrukne navn vil blive degraderet til bunden af ​​listen over alternative navne.

Når du tilføjer et nyt navn eller redigerer et eksisterende navn, åbnes dialogboksen . Denne navnedialogboks er beskrevet i afsnittet [Navneeditor](#Name_Editor) {{-}}

#### Kildehenvisninger <span id="Source Citations"/>

![[_media/EditPerson-SourceCitations-tab-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Fanen "Kildehenvisninger" fra "Rediger person" - dialog - eksempel]]

  
Fanen giver dig mulighed for at se og dokumentere kildehenvisningerne til de oplysninger, du indsamler.

<!-- -->

  
Disse kan være generelle kilder, der ikke beskriver en specifik begivenhed, men som ikke desto mindre giver information om personen. Hvis tante Marthas erindringer f.eks. nævner hendes oldebarn Paul, kan forskeren antage, at denne Paul faktisk eksisterede, og citere tante Marthas erindringer som den kilde, der begrunder denne antagelse.

  
Den centrale del viser listen over alle kildehenvisninger, der er gemt i databasen i forhold til personen. Knapperne , og giver dig mulighed for at tilføje, ændre og fjerne en kildehenvisning til denne person tilsvarende. Bemærk at knapperne og kun bliver tilgængelige, når en kildehenvisning er valgt fra listen.

<!-- -->

  
Ved redigering kan du ændre dataene i citatet (unikke for denne person) samt det delte kildeobjekt, se [Redigering af citater](wiki:Da:Gramps_6.0_brugsanvisning_-_Indtaste_og_redigere_data:_detaljeret_-_del_2#Editing_source_citations).

{{-}}

#### Attributter <span id="Attributes"/>

![[_media/EditPerson-Attributes-tab-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Fanen "Attributter" fra "Rediger person" - dialogboks - eksempel]]

  
Fanen giver mulighed for at se og tildele attributter til personen. Du har fuld frihed til at definere og bruge attributter. For eksempel kan attributter tildeles for at beskrive personens fysiske egenskaber eller personlighedstræk.

<!-- -->

  
Bemærk, at hver attribut, der er angivet i dialogboksen , består af to dele: selve attributten og en værdi, der er knyttet til den attribut. Denne såkaldte "Parameter-Værdi"-parring kan hjælpe dig med at organisere og systematisere din research. Hvis du for eksempel definerer "Hårfarve" som en attribut for en person, bliver "Hårfarve" en valgbar attribut for alle andre personer. Værdien af ​​hårfarve for person A kan være rød og brun for person B. På lignende måde kan du definere en attribut som "Gavmildhed" og bruge værdien "Enorm" til at beskrive en særlig generøs person.

<!-- -->

  
Den nederste del af dialogvinduet viser en liste over alle attributter, der er gemt i databasen. Den øverste del viser detaljerne for den aktuelt valgte attribut på listen (hvis nogen). Knapperne , og giver dig mulighed for at tilføje, ændre og fjerne en attributpost fra databasen. Bemærk, at knapperne **Rediger** og **-** kun bliver tilgængelige, når en attribut er valgt fra listen. Hvis du redigerer en attribut, åbnes .

{{-}}

#### Adresser <span id="Addresses"/>

![[_media/EditPerson-Addresses-tab-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Fanen "Adresser" fra "Rediger person" - dialog - eksempel]]

  
Fanen giver mulighed for at se og registrere personens forskellige postadresser. Det anbefales at bruge en bopælsbegivenhed til at gemme oplysninger om en persons bopæl. Adressefanen tilbydes primært for kompatibilitet med GEDCOM-standarden, hvor adresser kun er adresseadresser.

<!-- -->

  
Den nederste del af vinduet viser adresser, der er gemt for den pågældende person i databasen. Den øverste del viser detaljerne for den aktuelt valgte adresse på listen (hvis nogen). Knapperne , og giver dig mulighed for at tilføje, ændre og fjerne en adressepost fra databasen. Bemærk, at knapperne og kun bliver tilgængelige, når en adresse er valgt fra listen.

<!-- -->

  
  
Hvis du redigerer en adresse, åbnes .

<!-- -->

  
Nogle rapporter giver dig mulighed for at begrænse data om levende personer. Især vil denne mulighed udelade deres adresser.

{{-}}

#### Noter \<sp<n id="Notes"/>

![[_media/EditPerson-Notes-tab-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Fanen "Noter" fra "Rediger person" - dialog - eksempel]]

  
Fanen giver et sted at registrere forskellige elementer om personen, der ikke passer pænt ind i andre kategorier, samt tekstuddrag, du vil tilføje til stamtræet. Du kan dele noter mellem forskellige poster i Gramps. Ikonlinjen på denne faneblad tilbyder de sædvanlige knapper: , , , , og omarranger knapper for at ændre rækkefølgen af ​​noterne.

<!-- -->

  
Hvis du redigerer en note, får du .

{{-}}

##### Vælg notevælger

![[_media/SelectNote-selector-dialog-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Vælg note - vælger - eksempel]]

Dialogboksen giver dig mulighed for at linke til en allerede eksisterende note.

Følgende kolonner vises: `Forhåndsvisning` (standard sortering for liste), `ID`, `Type`, `Tags`, `Seneste ændring`.

Du kan bruge knappen til at filtrere listen baseret på en af ​​mulighederne fra rullelisten:

- **Forhåndsvisning indeholder** (standard)
- *Forhåndsvisning indeholder ikke*
- *ID indeholder*
- *ID indeholder ikke*
- *Typen indeholder*
- *Typen indeholder ikke*
- *Tags indeholder*
- *Tags indeholder ikke*
- *Seneste ændring indeholder*
- *Seneste ændring indeholder ikke*

{{-}}

\<span id="Galleri_1\>

#### Galleri

</span>

![[_media/EditPerson-Gallery-tab-example-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Fanen "Galleri" fra "Rediger person" - dialog - eksempel]]

  
Fanen giver dig mulighed for at se og gemme fotos, videoer og andre medieobjekter, der er knyttet til personen. Den centrale del af vinduet viser alle sådanne medieobjekter. Ethvert objekt i form af en gyldig billedfil vil resultere i visning af en miniaturevisning af billedet. For andre objekter såsom lydfiler, filmfiler osv. vises et tilsvarende filtypeikon i stedet.

Følgende muligheder er tilgængelige:

- \- giver dig mulighed for at tilføje et nyt medieobjekt fra .

- \- åbner vælgerdialogboksen , der giver dig mulighed for at linke til et allerede eksisterende medieobjekt.

- \- giver dig mulighed for at ændre det valgte medieobjekt i . Denne knap bliver kun tilgængelig, når et medieobjekt er valgt fra listen.

<!-- -->

- \- fjern det valgte medieobjekt fra personens galleri. Denne knap bliver kun tilgængelig, når et medieobjekt er valgt fra listen.

<!-- -->

- Knapperne (Flyt til venstre pil) og (Flyt til højre pil) - giver dig mulighed for at omarrangere medieelementerne for at vælge et bestemt billede til hovedfotoet. Du kan også ændre rækkefølgen af ​​det primære (aktive) billede ved at vælge billedet og trække det til den første position.

{{-}}

###### Galleri-kontekstmenu

![[_media/EditPerson-Gallery-tab-example-with-context-menu-60.png|højre|450px|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Fanen "Galleri" fra "Rediger person" - dialogboks - eksempel med kontekstmenu]]

Hvis du vælger et medieobjekt i galleriet, er en kontekstmenu (højreklik) tilgængelig med følgende muligheder:

- 

- 

<hr>

- 

<hr>

- 

- 

- 

- 

##### Vælg medieobjekt selector

![[_media/SelectMediaObject-selector-dialog-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Vælg medieobjekt - selector - eksempel med flere valg]]

Vælgerdialogboksen giver dig mulighed for at linke til et allerede eksisterende medieobjekt, og når billedet er valgt, åbnes det i dialogboksen .

Når du har valgt et medieobjekt fra listen, vises der om muligt en forhåndsvisning i den øverste sektion.

Følgende kolonner vises: `Titel` (standard sortering for liste), `ID`, `Type`, `Seneste ændring`.

Du kan bruge knappen til at filtrere listen baseret på en af ​​mulighederne fra rullelisten:

- **Titel indeholder**(standard)
- *Titlen indeholder ikke*
- *ID indeholder*
- *ID indeholder ikke*
- *Typen indeholder*
- *Typen indeholder ikke*
- *Seneste ændring indeholder*
- *Seneste ændring indeholder ikke*

Se også filvælgerdialogboksen [Vælg et medieobjekt](wiki:Da:Gramps_6.0_brugsanvisning_-_Indtaste_og_redigere_data:_detaljeret_-_del_2#Select_a_media_object_selector).

{{-}}

#### Internet

![[_media/EditPerson-Internet-tab-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Fanen "Internet" fra "Rediger person" - dialog - eksempel]]

  
Fanen viser internetadresser, der er relevante for [Person](#Internet), [Sted](wiki:Da:Gramps_6.0_brugsanvisning_-_Indtaste_og_redigere_data:_detaljeret_-_del_2#Internet), eller [Arkivet](wiki:Da:Gramps_6.0_brugsanvisning_-_Indtaste_og_redigere_data:_detaljeret_-_del_2#Internet_2). En beskrivende billedtekst til den internetplacering, du gemmer. Indtast den internetadresse, du har brug for, for at navigere til den, f.eks. <http://gramps-project.org>, E-mail, Webside, ...

<!-- -->

  
Den nederste del viser alle sådanne internetadresser og tilhørende beskrivelser. Den øverste del viser detaljerne for de aktuelt valgte adresser på listen (hvis nogen). Knapperne , åbner dialogboksen for at tilføje eller redigere, og fjerner den valgte internetadresse. Knappen åbner din webbrowser og fører dig direkte til den markerede side.

Bemærk, at knapperne og kun bliver tilgængelige, når en webadresse er valgt fra listen.

{{-}}

##### Internetadresseredigering

![[_media/InternetAddressEditor-dialog-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Internetadresseredigering" - dialogboks - standard]]

Dialogboksen giver dig mulighed for at tilføje en ny internetadresse eller ændre den valgte internetadresse.

- Type af internetadresse:

  - *E-mail*
  - **Ukendt** <small>(standard)</small>
  - *FTP*
  - *Webstartside*
  - *Websøgning*
  - Enhver brugerdefineret type, du indtaster manuelt.

- skifter mellem postens privatlivsstatus.

- Den internetadresse, der er nødvendig for at navigere til den, f.eks.: <https://gramps-project.org>

  - åbne webadressen i standardbrowseren

- En beskrivende billedtekst til den internetplacering, du gemmer.

Se også

- [Link Editor](wiki:Da:Gramps_6.0_brugsanvisning_-_Indtaste_og_redigere_data:_detaljeret_-_del_2#Link_Editor)
- [Note Link Report](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_6#Note_Link_Report)
- Søg efter en persons internetadresse (Type, Webadresse eller Beskrivelse) med den brugerdefinerede filterregel [Personer med poster, der indeholder <substring>](wiki:Gramps_6.0_Wiki_Manual_-_Filters#People_with_records_containing_.3Csubstring.3E)
- Søg efter et arkivs internetadresse (Type, Webadresse eller Beskrivelse) med den brugerdefinerede filterregel [Arkiver, der matcher parametre](wiki:Gramps_6.0_Wiki_Manual_-_Filters#Repositories_matching_parameters)

{{-}}

#### Forbindelser <span id="Associations"/>

![[_media/EditPerson-Associations-tab-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Fanen "Associationer" fra "Rediger person" - dialog - eksempel]]

Fanen giver dig mulighed for at se og redigere oplysninger om relationsroller for to personer, der er eksplicit tilknyttet i databasen.

Forbindelserne er typisk roller, der ikke kan udledes af at være forbundet i en normal (eller blandet) familiestruktur eller gennem delte begivenhedsroller. For eksempel er fætter-kusine- eller søskendeforhold tydelige gennem, hvordan ægteskaber forbinder personerne. Relationer som faddere (en deltager i en dåb), en organdonor (deltager i en medicinsk procedure), kistebærer (deltager i en begravelse) og værge (deltager i en dødsbobehandling eller nævnt i et testamente) kan være roller, der oprettes ved at dele en begivenhed, der er oprettet for den primære rolleperson.

Så forbindelser-roller er mindre indlysende. De kan være familievenner, et eponym (den person, der hædres af en navnebror), en kollega, en brevven eller enhver anden type associationer, du måtte ønske at registrere. Hvis den nærmeste relation er 'Fadder', vil dette indikere, at fadderen til den person (der redigeres) er den person, hvis navn vises i fanen Associationer.

[*Associates* (ASSO) tagget i GEDCOM-standarden](http://wiki-en.genealogy.net/GEDCOM/ASSO-Tag) siger, at "en persons relation eller association er den person, der peges på." Du kan vælge at placere en gensidig association i den anden persons fane Forbindelser.

I den forbindelse, der er vist fra [example.gramps](wiki:Example.gramps), er Lewis Garners gudfar Anderson Garner. Brug i stedet Begivenheder til relationer, der er forbundet med specifikke tidsrammer eller begivenheder. Begivenheder kan deles mellem personer, hvor hver person angiver deres [rolle](wiki:Gramps_Glossary/da#role) i associationen.

Knappen åbner dialogboksen for at tilføje. Knappen giver dig mulighed for at redigere, og fjerner den valgte association. De andre knapper eller flytter kun den valgte posts position på listen.

Se også:

- [Roller, relationer og associationer](wiki:Roller,_relationer_og_associationer)
- [Tilføj en gudfar-gudmor](wiki:Tilføj_en_gudfar-gudmor) ***Bemærk:*** En "Guddommer"-rolle blev tilføjet til standardlisten over begivenhedsroller i 5.2 Gramps-versionen.

{{-}}

##### Personreference Editor

![[_media/PersonReferenceEditor-dialog-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Personreference Editor" - dialogboks - standard]]

Med kan du tilføje og redigere associationsposter. Du kan få adgang til den fra fanen s dialogboks .

- *For at vælge en person skal du bruge træk-og-slip eller knapperne*

  - knappen åbner vælgerdialogen .

  - \- tilføj en ny person

- du kan overskrive standardindtastningen med hvad som helst, du vælger som tilknytning, f.eks. *Ven*, *Nabo*.

  - **Gudfar** (Standard)

- \- posten er offentlig (Standard)

{{-}}

###### Fanen Kildehenvisninger

  
Fanen giver dig mulighed for at se og dokumentere kildehenvisningerne til de oplysninger, du indsamler.

<!-- -->

  
Disse kan være generelle kilder, der ikke beskriver en specifik begivenhed, men som ikke desto mindre giver information om personen. Hvis for eksempel tante Marthas erindringer nævner hendes oldebarn Paul, kan forskeren antage, at denne Paul faktisk eksisterede, og citere tante Marthas erindringer som den kilde, der begrunder denne antagelse.

  
Den centrale del viser listen over alle kildehenvisninger, der er gemt i databasen i forhold til personen. Knapperne , og giver dig mulighed for at tilføje, ændre og fjerne en kildehenvisning til denne person tilsvarende. Bemærk, at knapperne og kun bliver tilgængelige, når en kildehenvisning er valgt fra listen.

<!-- -->

  
Ved redigering kan du ændre dataene i citatet (unikke for denne person) samt det delte kildeobjekt, se [Redigering af citater](wiki:Da:Gramps_6.0_brugsanvisning_-_Indtaste_og_redigere_data:_detaljeret_-_del_2#Editing_source_citations).

{{-}}

###### Fanen Noter

  
Fanen giver dig mulighed for at se og redigere alle [Note](wiki:Gramps_Glossary/da#note), der er knyttet til relationen. Disse kan være kommentarer, der ikke naturligt passer ind i "Parameter-Værdi"-parrene, der er tilgængelige for attributter. For at tilføje en note eller ændre eksisterende noter skal du blot redigere teksten i tekstindtastningsfeltet.

Med indstillingen kan du indstille, hvordan noten skal vises i rapporter og på websider. Hvis du vælger Omløbende, vil den genererede tekst have enkelte mellemrum i stedet for alle mellemrum, tabulatorer og enkelte linjeafslutningstegn. En tom linje indsat mellem to tekstblokke signalerer et nyt afsnit; yderligere indsatte linjer ignoreres.

Hvis du vælger indstillingen Forformateret, vil teksten i rapporter og på websider vises præcis, som du indtaster den i dialogboksen .

{{-}}

###### Vælg person-vælger

![[_media/SelectPerson-selector-dialog-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Vælg person" - vælgerdialog - eksempel]]

Vælgerdialogen giver dig mulighed for at linke til en allerede eksisterende person.

Du kan vælge et hvilket som helst efternavn for at udvide og finde den ønskede person, derefter vælge dem og trykke på . {{-}} Se også:

- [Vælg en person til rapportvælgeren](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_4#Select_a_person_for_the_report_selector)

\<span id="SDH_1\>

#### SDH <span id="LDS"/>

</span> ![[_media/EditPerson-LDS-tab-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Fanen &quot;SDH&quot; fra &quot;Rediger person&quot; - dialog - eksempel]]

Fanen (Sidste Dages Hellige - Engelsk: Latter Days Saints) giver dig mulighed for at se og redigere oplysninger om personens SDH-ordinancer. Disse oplysninger er arvet fra LDS' GEDCOM-specifikation. SDH-fanerne i Familieeditoren og Personeditoren kan skjules via : Sidste Dages Hellige under afkrydsningsfeltet **** sektionen af ​​ fanen i .

Øverst på fanen kan du bruge følgende knapper til at eller for at åbne dialogboksen ; og eller på listen.

Følgende kolonner for listen vises: `Kilde` (ikon), `Privat` (låseikon), `Type`, `Dato`, `Status`, `Tempel`, `Sted`.

Se også:

- Personredigeringsdialogens faneblad
- Familieredigeringsdialogens faneblad  - viser kun information om SDH' forsegling til ægtefælle-forordning.
- Du kan skjule disse -faner ved at ændre den tilhørende indstilling i fanebladets **** sektion.

{{-}}

##### SDH fanebladets kontekstmenu

Du kan bruge kontekstmenuen på en valgt post til at:

- 

- 

- 

{{-}}

##### SDH Ordinance Editor

![[_media/LDSOrdinanceEditor-dialog-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "SDH Ordinance Editor" - dialogboks - standard]]

Brug dialogboksen til at tilføje eller redigere eksisterende LDS-ordinancer for personen.

Disse LDS er for:

- **Dåb** (standard)
- *Begavelse*
- *Bekræftelse*
- *Beseglet til forældre*

Hver ordinance er yderligere beskrevet af dens , , og samt en yderligere indgang for , der kun vises for ordinancen *Beseglet til forældre*.

Hver forordning kan beskrives yderligere gennem de valgmuligheder, der er tilgængelige i rullemenuen :

- **<Ingen status>** (standard)
- *Født i pagt*
- *Ryddet*
- *Afsluttet*
- *Forsegles ikke*
- *Før 1970*
- *Kvalificeret*
- *Dødfødt*
- *Indsendt*
- *Ikke ryddet*

I fanerne i den nederste sektion kan du også inkludere kildehenvisninger og noter:

- [Fanen Kildehenvisninger](#Source_Citations_tab_2)
- [Fanen Noter](#Notes_tab_2)

Se også:

- [SDH under Familieredigering](#SDH_2)
- [Forordning (Sidste Dages Hellige)](https://wikipedia.org/wiki/Ordinance_(Latter_Day_Saints)) på [Wikipedia](https://wiktionary.org/wiki/Wikipedia#Etymology).

{{-}}

###### Fanen Kildehenvisninger

{{-}}

###### Fanen Noter

{{-}}

#### Henvisninger

![[_media/EditPerson-References-tab-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Fanen "Henvisninger" fra "Rediger person" - dialog - eksempel]]

Fanen viser andre objekter, der eksplicit er linket tilbage til personen: Familier, hvor personen er en ægtefælle eller et barn, personer, der har en tilknytning, og noter, hvor personen er blevet linket.

Den viser ikke sekundære linkede objekter: objekter (som begivenheder, kildehenvisninger, medier, steder, mærkater), der er linket under personen.

Hvis du dobbeltklikker på en række i Henvisninger, åbnes editoren for det refererende objekt. {{-}}

## Redigering af oplysninger om slægtsforhold

Oplysninger om slægtsforhold indtastes og redigeres via dialogboksen .

Denne dialogboks kan åbnes på flere måder:

- Fra menuen : vælg eller brug dens [tastaturgenvej](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings#xx).

<!-- -->

- Fra [Relationskategori](wiki:Gramps_6.0_Wiki_Manual_-_Categories#Relationships_Category): klik på en -knap i den familie, du vil redigere. Eller fra skal du vælge: , eller .

<!-- -->

- Fra [Families Category](wiki:Gramps_6.0_Wiki_Manual_-_Categories#Families_Category): vælg familien på listen, og klik derefter på knappen på værktøjslinjen, eller dobbeltklik på familien. Eller fra skal du vælge .

<!-- -->

- Fra [Charts Category](wiki:Gramps_6.0_Wiki_Manual_-_Categories#Charts_Category): peg med musen over den sorte linje, der forbinder ægtefællerne, højreklik, og vælg fra kontekstmenuen, eller dobbeltklik på den sorte linje.

Enhver af disse metoder vil vise dig dialogboksen :

{{-}}

### Familieeditor-dialogboks <span id="Family_Editor_dialog"/>

![[_media/FamilyEditor-dialog-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}}  dialogboks - viser eksempelfamilie og &quot;Hurtigvisning&quot; kontekstmenu]] giver dig mulighed for at tilføje eller redigere alle aspekter af en familie: personerne (børn, forældre), deres forhold til hinanden, de roller de spiller i begivenheder. Familiestrukturen giver den kontekst, som Gramps har brug for, for lejlighedsvis at gætte sandsynlige efternavne, køn, roller og relations- eller begivenhedstyper.

Børn, der tilføjes til en familie, gættes til at være biologiske børn af (biologisk beslægtede med) forældrene og arve et efternavn, der er gættet fra forældrene. Men det kan ændres manuelt med [Reference Editor for børn](#Child_Reference_Editor). Denne editor vises, når et barn tilføjes til en familie. Og den kan kaldes for redigering bagefter ved at dobbeltklikke på et barn i [Familie Editor](#Family_Editor_dialog).

En forælder, der tilføjes til en familie, vil have et gættet køn fra rollen (Far/Partner1 eller Mor/Partner2) og muligvis et efternavn.

Familiebegivenheder med (standard [begivenhedsrollen](wiki:Gramps_Glossary/da#event_role) for Familie) gælder for begge ægtefæller/partnere i en familie. Dette eliminerer behovet for at oprette duplikerede begivenheder (og holde disse begivenheder harmoniserede) eller at dele en begivenhed mellem far/mor (Partner1/partner2) i en familie.

Familier har [standardrelationstyper](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Input_Options) og implicitte [eventroller](wiki:Gramps_Glossary/da#event_role). Når begivenheder tilføjes i familieeditoren, vil begivenhedsrollen som standard have rollen "Familie". Og den første tilføjede begivenhed vil være af typen [Ægteskab](#Ægteskab), og den anden vil være af typen [Skilsmisse](#Skilsmisse). Hvis begivenheder deles, vil begivenheden have rollen "Ukendt" og skal indstilles til den relevante rolle.

Den øverste del af vinduet viser navnene på de personer, hvis forhold redigeres, samt deres fødsels- og dødsoplysninger.

- - Knappen åbner dialogboksen
  - Knappen åbner dialogboksen . \*
  - Knappen åbner
  - Knappen åbner dialogboksen .

Knappen giver dig mulighed for at markere, om familieregistret betragtes som offentligt eller privat.

[Quick View](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_8#Quick_Views) rapporter er tilgængelige ved at bruge kontekstmenuen (højreklik) fra et tomt område i den øverste del af vinduet.

##### Kontekstmenu i Familieeditor

Følgende [Quick View](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_8#Quick_Views) rapporter er tilgængelige fra kontekstmenuen:

- 

- 

#### Slægtsforholdsoplysninger

Afsnittet viser tre felter med den grundlæggende beskrivelse af forholdet.

- Feltet viser det ID-nummer, der betegner dette forhold i databasen. Lad dette felt være tomt for at få Gramps til at generere et unikt ID-nummer.

<!-- -->

- viser en rulleliste over de tilgængelige typer familieforhold, såsom `Civil Union`, `Gift`, **`Ukendt`**(standard), `Ugift` osv.) eller tilføj en [Brugerdefineret type](wiki:Gramps_Glossary#custom).

<!-- -->

- - Du kan også indstille  - brugt af dialogboksen Familieredigering i
  - [Hvordan repræsenterer jeg en skilsmisse?](wiki:Indicate_a_divorce)
  - Du kan bruge tilføjelsen [](wiki:Addon:FamilyRelationship) til at ændre typen af ​​familieforhold for en valgt gruppe af filtrerede familier.

<!-- -->

- viser de [tags](wiki:Gramps_6.0_Wiki_Manual_-_Filters#Tagging), du har oprettet, for at vise nogle grundlæggende oplysninger om status for din research. Du kan tilføje yderligere tags ved at vælge knappen .

Nedenfor dem vises en række [notebook-faner](#Family_Editor_tab_pages), der repræsenterer forskellige kategorier af information om forholdet. Klik på en hvilken som helst fane for at se eller redigere de oplysninger, den indeholder.

I den nederste del af vinduet kan du til enhver tid klikke på knappen for at anvende alle de ændringer, der er foretaget i alle faner, og lukke dialogboksen. Hvis du klikker på knappen , lukkes vinduet uden at anvende nogen ændringer. Hvis nogen af ​​dataene i en hvilken som helst fane ændres, vises et advarselsvindue, der beder dig om at vælge mellem at lukke dialogboksen uden at gemme ændringerne, annullere den oprindelige annulleringsanmodning eller gemme ændringerne.

#### Vælg far dialogboks

![[_media/SelectFather-selector-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Vælg far - selector]] Vælgerdialogboksen giver dig mulighed for at linke til en allerede eksisterende person som far.

Du kan enten søge efter personen eller bruge

- : vælgeren filtreres til en person med et *Mandligt* køn. Personer med ukendt, andet og kvindeligt køn vil ikke blive vist. Hvis du vælger knappen og derefter , deaktiveres denne filtrering.

{{-}}

#### Vælg mor dialogboks

![[_media/SelectMother-selector-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Vælg mor - vælger]] Vælgerdialogboksen giver dig mulighed for at linke til en allerede eksisterende person som mor.

-   
  vælgeren filtreres til en person med et *kvindeligt* køn. Personer med ukendt, andet og mandligt køn vil ikke blive vist. Hvis du vælger knappen og derefter , deaktiveres denne filtrering.

{{-}} {{-}}

### Familie-editorens fanesider <span id="Family_Editor_tab_pages"/>

Fanerne indeholder følgende informationskategorier for relationsdata:

#### Børn

![[_media/FamilyEditor-dialog-Children-tab-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Fanen "Børn" fra "Familieeditor" - dialog - eksempel]]

  
Fanen giver mulighed for at se og redigere listen over børn, der er en del af dette forhold. Knappen giver dig mulighed for at indtaste en ny person i databasen og tilføje den person som et barn i dette forhold. Knappen giver dig mulighed for at vælge en eksisterende person til at være et barn i relationen. Knappen åbner dialogboksen , der giver mulighed for at redigere relationerne mellem det valgte barn og forældrene. Endelig giver dig mulighed for at fjerne det valgte barn fra relationen. Bemærk, at knapperne og kun bliver tilgængelige, når et barn er valgt fra listen.

[Hvordan ændrer jeg rækkefølgen af ​​børn?](wiki:Da:Gramps_6.0_brugsanvisning_-_FAQ#How_do_I_change_the_order_of_children.3F)

- Brug denne [Børn](#Børn) fane i Familieeditoren for at ændre rækkefølgen af ​​børn i den aktive familie.
- Brug tredjepartsværktøjet , som tillader masseopdateringer af børnenes rækkefølge.

Se også:

- Gramplet'en [Børn](wiki:Da:Gramps_6.0_brugsanvisning_-_Gramplets#Børn) i visningerne [Personkategori](wiki:Da:Gramps_6.0_brugsanvisning_-_Kategorier#Personkategori) viser alle børn fra **alle ægteskaber** for den aktive person. Børn vises som de er sorteret i familieregistreringen/-registreringerne.

{{-}}

###### Vælg børnevælger

![[_media/SelectChild-selector-dialog-example-60.png|højre|450px|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Vælg barn - vælger - eksempel]]

Vælgerdialogboksen giver dig mulighed for at linke til et allerede eksisterende barn, og når det er valgt, åbnes det i

Følgende kolonner vises: `Navn` (standard sortering for liste), `ID`, `Køn`, `Fødselsdato`, `Fødested`, `Dødsdato`, `Dødssted`, `Ægtefælle`, `Seneste ændring`. {{-}}

##### Reference Editor for børn

![[_media/ChildReferenceEditor-dialog-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;Reference Editor for underordnede&quot; - eksempel]] Dialogboksen tillader redigering af forholdet mellem det valgte underordnede element og forældrene i en familie. Dialogboksen vises, når en person første gang registreres som afkom i en familie. Det sidste trin ved at bruge knappen Del, knappen (Opret en ny person) eller bruge "træk og slip" til at tilføje nogen til familien er at bekræfte relationen.

Relationerne kan også redigeres for eksisterende børn, som vist i dialogboksen Rediger familie. Dobbeltklik på et eksisterende barn i en familie eller vælg kontekstmenupunktet for at åbne editoren for børnereferencer for det valgte barn. (Velg kontekstmenupunktet for at åbne dialogboksen Rediger person i stedet.)

Selvom en person kun har en fødselsrelation til begge forældre i en traditionel fødselsfamilie, kan de også være en del af flere blandede familier. I disse familier gifter en fødselsforælder sig igen, og den anden ægtefælle kan have et mere komplekst forhold til børn fra et tidligere ægteskab. Men hvis de er en del af husstanden, bør disse børn tilføjes til den nye familie med det passende forhold.

Følgende muligheder er tilgængelige:

- Navnet på barnet

  -  knap.

- Vælg fra rullelisten over mulige forholdstyper:

  - *Adopteret*
  - **Født** (standard)
  - *Plejefamilie*
  - *Ingen*
  - *Sponsoreret*
  - *Stedbarn*
  - *Ukendt*

- Vælg fra rullelisten over mulige forholdstyper:

  - *Adopteret*
  - **Født** (standard)
  - *Plejefamilie*
  - *Ingen*
  - *Sponsoreret*
  - *Stedbarn*
  - *Ukendt*

- privatlivsknap for dette forhold.

{{-}} Følgende faner er også tilgængelige:

- Kildehenvisninger
- Noter

###### Fanen Kildehenvisninger

  
Fanen giver dig mulighed for at se og dokumentere kildehenvisningerne til de oplysninger, du indsamler.

<!-- -->

  
Disse kan være generelle kilder, der ikke beskriver en specifik begivenhed, men som ikke desto mindre giver information om personen. Hvis for eksempel tante Marthas erindringer nævner hendes oldebarn Paul, kan forskeren antage, at denne Paul faktisk eksisterede, og citere tante Marthas erindringer som den kilde, der begrunder denne antagelse.

  
Den centrale del viser listen over alle kildehenvisninger, der er gemt i databasen i forhold til personen. Knapperne , og giver dig mulighed for at tilføje, ændre og fjerne en kildehenvisning til denne person. Bemærk, at knapperne og kun bliver tilgængelige, når en kildehenvisning er valgt fra listen.

<!-- -->

  
Ved redigering kan du ændre dataene i citatet (unikke for denne person) samt det delte kildeobjekt, se [Redigering af citater](wiki:Da:Gramps_6.0_brugsanvisning_-_Indtaste_og_redigere_data:_detaljeret_-_del_2#Editing_source_citations).

{{-}}

###### Fanen Noter

  
Fanen giver dig mulighed for at se og redigere alle [Note](wiki:Gramps_Glossary/da#note), der er knyttet til relationen. Disse kan være kommentarer, der ikke naturligt passer ind i "Parameter-Værdi"-parrene, der er tilgængelige for attributter. For at tilføje en note eller ændre eksisterende noter skal du blot redigere teksten i tekstindtastningsfeltet.

<!-- -->

  
Med indstillingen kan du indstille, hvordan noten skal vises i rapporter og på websider. Hvis du vælger Omløbende, vil den genererede tekst have enkelte mellemrum i stedet for alle mellemrum, tabulatorer og enkelte linjeafslutningstegn. En tom linje indsat mellem to tekstblokke signalerer et nyt afsnit; yderligere indsatte linjer ignoreres.

<!-- -->

  
Hvis du vælger indstillingen Forformateret, vil teksten i rapporter og på websider vises præcis, som du indtaster den i dialogboksen .

{{-}}

#### Begivenheder <span id="Events_2"/>

  
Fanen giver dig mulighed for at se og redigere listen over begivenheder, der er relevante for relationen. Knapperne , og giver dig mulighed for at tilføje, ændre eller fjerne en begivenhedspost fra databasen. Bemærk, at knapperne og kun bliver tilgængelige, når en begivenhed er valgt fra listen.

{{-}}

#### Kildehenvisninger

  
Fanen giver dig mulighed for at se og redigere en liste over referencer til de kilder, der giver bevis for forholdet. Disse kan være dokumenter, der refererer til forholdet, men som ikke nødvendigvis dokumenterer det officielt. Hvis tante Marthas erindringer for eksempel nævner, at hendes oldebarn Paul var gift, kan forskeren tage dette som bevis for, at forholdet mellem Paul og hans kone eksisterede, og citere erindringerne som kilde til denne antagelse.

  
Knapperne , og giver dig mulighed for at tilføje, ændre og fjerne en kildehenvisning til dette forhold. Bemærk, at knapperne og kun bliver tilgængelige, når en kildehenvisning er valgt fra listen.

{{-}}

#### Attributter

  
Fanen giver dig mulighed for at se og redigere specifikke oplysninger om forholdet, der kan udtrykkes som attributter. Knapperne , og giver dig mulighed for at tilføje, ændre eller fjerne en attribut. Bemærk, at knapperne og kun bliver tilgængelige, når en attribut er valgt fra listen.

{{-}}

#### Noter

  
Fanen giver dig mulighed for at se og redigere alle [Note](wiki:Gramps_Glossary#note), der er knyttet til relationen. Disse kan være kommentarer, der ikke naturligt passer ind i "Parameter-Værdi"-parrene, der er tilgængelige for attributter. For at tilføje en note eller ændre eksisterende noter skal du blot redigere teksten i tekstindtastningsfeltet.

<!-- -->

  
Med indstillingen kan du indstille, hvordan noten skal vises i rapporter og på websider. Hvis du vælger Omløbende, vil den genererede tekst have enkelte mellemrum i stedet for alle mellemrum, tabulatorer og enkelte linjeafslutningstegn. En tom linje indsat mellem to tekstblokke signalerer et nyt afsnit; yderligere indsatte linjer ignoreres.

<!-- -->

  
Hvis du vælger indstillingen Forformateret, vil teksten i rapporter og på websider vises præcis, som du indtaster den i dialogboksen .

{{-}}

#### Galleri <span id="Gallery"/><span id="Galleri_2"/>

  
Fanen giver dig mulighed for at gemme og vise fotos og andre medieobjekter, der er knyttet til relationen. Den centrale del af vinduet viser alle sådanne objekter og giver dig et miniaturebillede af billedfiler. Andre objekter, såsom lydfiler, filmfiler osv., er repræsenteret af et generisk Gramps-ikon. Knapperne , , og giver dig mulighed for at tilføje et nyt billede, tilføje en reference til et eksisterende billede, ændre et eksisterende billede og fjerne et medieobjekts link til relationen. Bemærk, at knapperne og kun bliver tilgængelige, når et medieobjekt er valgt fra listen.

{{-}}

#### SDH <span id="SDH_2"/>

![[_media/LDSOrdinanceEditor-dialog-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} <strong>Beseglet til ægtefælle</strong> ordinance editor af "Rediger familie" - dialog - eksempel]]

  
Fanen (Sidste Dages Hellige) i Familie Editor viser kun information om SDH **Beseglet til ægtefælle** . (Ordinancerne relateret til enkeltpersoner kan registreres i [SDH-fanen i <strong>Person</strong>-editoren](#LDS).) SDH-fanerne i familieeditoren og personeditoren kan skjules via afkrydsningsfeltet "Skjul SDH-fanen i person- og familieeditorer." under afsnittet **** i fanen i .

<!-- -->

  
Dataene kan også omfatte , , og .

<!-- -->

  
Hver ordinancepost kan også annoteres i de tilsvarende faner og .

Status for ordinancen kan beskrives via de tilgængelige muligheder i pop op-menuen .

Statustilstandene for ordinancen **Forseglet til ægtefælle** er:

- **<Ingen status>** *(standard)*
- Annulleret
- Ryddet
- Afsluttet
- Forsegles ikke
- Før 1970
- Kvalificeret
- Forsegles ikke/Annulleres ikke
- Indsendt
- Ikke ryddet

<!-- -->

  
For at redigere annotationsdata for kilde eller note skal du skifte til den tilsvarende fane i SDH Ordinations Editor og vælge den ønskede post på listen over poster. Dobbeltklik på den pågældende post, eller klik på ikonet på værktøjslinjen for at åbne følgende

<!-- -->

  
Hoveddelen af ​​Familieeditorens faneblad viser en tabel over de fem forskellige børn af data i hver post. Klik på en kolonneoverskrift for at vælge en række, eller dobbeltklik på en række for at redigere dens indhold. Den nederste del af vinduet har knapperne og . Hvis du klikker på , anvendes alle ændringer foretaget i alle faner, og dialogboksen lukkes. Hvis du klikker på knappen , lukkes vinduet uden at anvende nogen ændringer.

<!-- -->

  
Se også:

- Dialogboksen Personredigering, fanen
- Dialogboksen Familieredigering, fanen  - viser kun information om LDS' forseglede ægtefælleforordning.
- Du kan skjule disse -faner ved at ændre den tilhørende indstilling i afsnittet **** under fanen i menupunktet .

{{-}}

## Redigering af datoer

Dette afsnit beskriver, hvordan man indtaster og ændrer datoer. Da datoer er så vigtige i slægtsforskning, er Gramps særlig omhyggelig med at bevare og bruge alle tilgængelige datooplysninger.

Oplysninger kan indtastes i et datofelt ved at skrive det direkte eller ved at åbne dialogboksen ved at klikke på knappen ![[_media/22x22-gramps-date.png]] ved siden af ​​et hvilket som helst indtastningsfelt.

Se også:

- [Da:Gramps 6.0 brugsanvisning - Sandsynligvis i live](wiki:Da:Gramps_6.0_brugsanvisning_-_Sandsynligvis_i_live)

- i afsnittet **Beregningsgrænser** - For at ændre standardværdierne for de typiske aldre ved fødslen, mellem generationer osv.

### Dialogboks til datovalg

![[_media/DateSelection-dialog-defaults-60-da.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}}  - dialog - default]]

Selvom nedenstående [parsing rules](#Date_formats_and_parsing_rules) giver en vejledning til at indtaste de mest almindelige datoer, kan du også bruge dialogboksen . Dialogboksen er især nyttig til at opbygge en kompleks dato eller blot til at sikre, at dine oplysninger indtastes på en måde, som Gramps vil forstå. {{-}} Følgende felter er tilgængelige:

- Vælg en alternativ [kalendertype](#Calendars).

  - [**Gregoriansk**](https://wikipedia.org/wiki/Gregorian_calendar) (standard)
  - *[Julian](https://www.familysearch.org/wiki/da/Julian_and_Gregorian_Calendars) (inklusive [Blandet](wiki:Datoer#Dobbelt_Dateret)/[Dobbelte](#Dobbelt-daterede_datoer) datoer)*
  - *[Hebraisk](https://wikipedia.org/wiki/Hebrew_calendar)*
  - *[Fransk Republikansk](https://www.familysearch.org/wiki/da/French_Republican_Calendar)*
  - *[Persian](https://wikipedia.org/wiki/Iranian_calendars#Old_Persian_calendar)*
  - *[Islamisk](https://wikipedia.org/wiki/Islamic_calendar)*
  - *[Swedish](https://www.familysearch.org/wiki/en/Sweden_Feast_Day_Calendars)* - [Svensk kalender](#Swedish_calendar)

-  Dette felt kan vælges med det matchende felt, hvis det alternative understøtter [dobbelt datering](#Dual-dated_dates). (afkrydsningsfeltet er ikke markeret som standard)

  - (Tomt tekstfelt som standard)

- Indstil [datokvalitet](#Date_Quality).

  - *Normal*
  - *Anslået*
  - *Beregnet*

- Indstil intervalpræcisionen eller tidsrammen [datotype](#Date_Type).

  - **Normal**(standard) - intervallet, der strækker sig over en bestemt dag, måned eller år (uden hensyn til tidszone)
  - *Før*
  - *Efter*
  - *Omkring*
  - *Interval* - feltet vil være tilgængeligt til at indstille en dato.
  - *Fra*
  - *Til*
  - *Tidsrum* - feltet vil være tilgængeligt til at indstille en dato.
  - **Kun tekst** (standard)

- Vælg , og .

- Hvis din dato er *Interval* eller *Span*, vil denne mulighed være tilgængelig til at indstille en dato.

- Tekstindtastningsfeltet tillader lagring af en vilkårlig tekststreng sammen med datoen.

Nederst i dialogboksen finder du også knapperne , og ; samt et statuslinjeområde lige under knapperne, der giver feedback om eventuelle problemer med datoindtastningen.

{{-}}

### Indikatorer for datogyldighed

![[_media/DateSelection-dialog-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Dialogboksen "Datovalg" - eksempel]]

Gramps bruger en datovalidator.

Selvom delvise datoer ikke entydigt definerer dagen, tillader de i det mindste en form for sammenligning mellem datoerne.

Datofeltet vil fremhæves med rødt og vise et rødt symbol (f.eks. et stoptegn eller et kryds) for at angive, at den indtastede dato ikke genkendes som et genkendt og gyldigt format for en dato.

Eksempler på almindelige datoreferencer, der ikke er genkendelige Gramps-formater, kan være "Juleugen '61", "Efterår 1782" eller "sommeren, hvor jeg blev opereret". I et sådant tilfælde gemmes datoen som en streng og markeres som typen *Kun tekst*. Datoer af denne type sammenlignes ikke med andre datoer. Hvor det er muligt, foretrækkes det at undgå sådanne *Kun tekst*-datoindtastninger. Det kan f.eks. være bedre at indtaste datoen "December 1961" og derefter tilføje beskrivelsesannotationen "Juleugen '61". Det ville være mere præcist at tjekke en kalender for december 1961 og derefter indtaste det faktiske datointerval... men stadig inkludere annotationen. Annotationen er nødvendig, fordi du ikke kan antage, at 'Juleuge' betyder det samme antal dage for dig som for din kilde. Der kan være kulturel bias, der kan farve fortolkningen. Det kan betyde kalenderrækken, der indeholder juledag. Men amerikanske og europæiske kalenderrækker starter på forskellige ugedage. Eller det kan betyde de 7 dage, der starter med jul, eller endda de 7 dage op til jul. Så intervallet tillader søgninger og sammenligninger, men annotationen viser, at det faktiske interval kan fortolkes.

I de forskellige visninger (såsom ) vises ukendte datoer som standard med **fed**. Tekstmarkeringen (formateringsstil) for ukendte datoer kan ændres ved at ændre indstillingen i afsnittet i fanen [](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Environment_Settings) i [Preferences](wiki:Gramps_6.0_Wiki_Manual_-_Settings).

Når en fødsels- eller dødsdato mangler for en person, kan datoerne for eksisterende reservebegivenheder i samme kategori vises (og angives med kursiv med en forkortet titel) i stedet for at lade visningen være tom. Så vil en begravelses- eller kremeringsdato blive vist, hvis der endnu ikke er registreret en dødsdato.

{{-}}

### Dato kvalitet

- *Regulær*: En "regulær" dato er en dato med en eksplicit dag, måned eller år.

<!-- -->

- *Anslået*: En "anslået" dato er en dato baseret på antagelser om gennemsnitlige intervaller, der er forskudt fra en kendt referencedato. (Såsom det gennemsnitlige antal år mellem generationer, maksimal levetid eller længden af ​​sørejse.)

<!-- -->

- *Beregnet*: En "beregnet" dato er en dato baseret på et kendt interval fra en referencedato, men uden en kilde, der eksplicit nævner datoen. (Såsom en gravsten indgraveret med både en dødsdato og en præcis alder ved døden.)

Folketællingsdata er usædvanlige, idet de synes at være en kandidat til en beregnet dato, men det er det ikke. Folketællingen definerer ofte eksplicit intervallet (alder) og referencedatoen (folketællingens valgdato), men denne alder er ofte estimeret eller afrundet.

### Dato type

Til højre for vises vises.

Datoer i Gramps klassificeres efter følgende typer præcision (skala) af interval eller tidsramme:

- **Regulær**: En "regulær" dato er en dato, der inkluderer et interval, der strækker sig over en bestemt dag, måned eller år. Den kan være fuldstændig (eller 'fuldt kvalificeret' for et 24-timers interval som 6. juni 1990) eller delvis (som at udelade dagen for et interval på 1 måned som juli 1977 eller udelade dag og måned for et interval på 1 år).

<!-- -->

- **Før**: En "før"-dato er en, der kun kan identificeres som forekommende (i et [præferencer-defineret langt interval](wiki:Da:Gramps_6.0_brugsanvisning_-_Indstillinger#Datoer)) før en bestemt dag, måned eller år. *(Som standard er intervallet 50 år.)*

<!-- -->

- **Til**: En "til"-dato er en dato med åbent tidsrum, da den ligger før en bestemt dag, måned eller år. I modsætning til en "før"-datotype er intervallet ubegrænset ind i fortiden.

<!-- -->

- **Fra**: En "fra"-dato er en dato med åbent tidsrum, der følger efter en bestemt dag, måned eller år. I modsætning til en "efter"-datotype er intervallet ubegrænset ind i fremtiden.

<!-- -->

- **Efter**: En "efter"-dato er en dato, der ligger (i et [2. præferencedefineret langt interval](wiki:Da:Gramps_6.0_brugsanvisning_-_Indstillinger#Datoer)) efter en bestemt dag, måned eller år. *(Som standard er intervallet 50 år.)*

<!-- -->

- **Omkring**: En "omkring" (circa) dato er en dato, der forekommer (i [endnu et præferencedefineret ±årsinterval](wiki:Da:Gramps_6.0_brugsanvisning_-_Indstillinger#Datoer)) før **eller** efter en bestemt dag, måned eller år. *(Som standard er intervallet ±50 år.)*

<!-- -->

- **Interval**: Et "interval" beskriver en tidsperiode, hvor begivenheden fandt sted. Det kan være en tilbagevendende begivenhed i intervallet eller en enkeltstående forekomst, der menes at have fundet sted mellem kendte grænsedatoer.

  
For eksempel "mellem januar 1932 og marts 1932."

- **Tidsrum**: Et "tidsrum" beskriver en inkluderende tidsperiode, hvor en tilstand kontinuerligt eksisterede.

  
For eksempel "fra 12. maj 2000 til 2. februar 2002."

### Datoformater og fortolkningsregler

Dialogboksen hjælper med at formatere en dato i det standardformat, som Gramps kan fortolke. Det er nyttigt, hvis du ikke er fortrolig med indstillingerne, har brug for at bruge en alternativ kalender eller angive en dato for nytårsbegyndelsen.

Gramps genkender datoer indtastet i forskellige formater. Det numeriske standardformat er det, der er konventionelt for det miljø, Gramps opererer i, dvs. *DD.MM.ÅÅÅÅ* for de fleste europæiske lande, *MM/DD/ÅÅÅÅ* for USA osv. En måde at undgå denne tvetydighed på er altid at vælge formatet *d mmm åååå* eller *mmmn d åååå*. Det vil fortolke måneds- og månedsforkortelser indtastet på det aktuelt aktive sprog.

Det vil også fortolke datoer indtastet i kvartaler og konvertere dem til "mellem"-intervaller. F.eks. bliver »q2 1820« til »mellem 1. april 1820 og 30. juni 1820«.

Udover eksakte datoer genkender Gramps mange datotyper, der ikke er regelmæssige: før, til, fra, efter, omkring, intervaller og (fra/til eller mellem) perioder. Det forstår også kvaliteten: anslået eller beregnet. Endelig understøttes delvise datoer og mange alternative kalendere. Nedenfor er en liste over regler for datoindtastning, der muliggør præcis datoanalyse.

**Almindelige enkeltdatoer** kan indtastes, ligesom du ville skrive dem. Og hvis du skriver en skråstreg efter året efterfulgt af en værdi 1 år senere, oprettes en juliansk dobbeltdateret indtastning.

  
Eksempler: "24. maj 1961"; "31. dec. 1858/9" eller "1. januar 2004".

**Før den almindelige tidsregning** (BCE, BC og B.C.E.) og er notationer for de gregorianske eller julianske kalendere. "Common Era" og "Før den almindelige tidsregning" er religiøst neutrale alternativer til de velkendte Anno Domini (AD) og Før Kristus (BC) notationer, der bruges til den samme kalenderæra. Notationen vil blive harmoniseret med formen "B.C.E.". :Eksempler: "ca. 25. dec. 32 f.Kr. Julian" bliver til "omkring 25. dec. 32 f.Kr. (Julian)"

**Delvise datoer** indtastes blot ved at udelade ukendte oplysninger.

  
Eksempler: Maj 1961 og 2004.

Datoer, der ikke er almindelig , skal starte med -nøgleordene *anslået* eller *beregnet*, hvis det er relevant.

Eksempel: *anslået 1961* eller *beregnet 2005*. (Bemærk, at en ikke behøver at blive angivet for almindelige datoer.)

Menupunkterne kan også indstilles til *Før*, *Til*, *Fra* *Efter* eller *Omkring* ved blot at skrive "før", "til", "fra", "efter" eller "omkring" før en enkelt dato i dialogboksen Begivenhedsredigering.

Hvis den ønskede er et interval, skal du skrive "mellem DATO og DATO", og hvis er et tidsrum, skal du skrive "fra DATO til DATO". Eksempler: beregnet fra 2001 til 2003, før juni 1975, beregnet cirka 2000, beregnet mellem maj 1900 og 1. januar 1990.

Her er et par eksempler, du kan prøve:

Kaptajn John Smith har været stationeret i 1. Grenadierregiment mellem 13-5-1888 og 24-10-1902 ifølge hans militære baggrund (ordene "mellem" og "og" bruges bevidst, da det er sådan, vi taler i det daglige); Så skal datoen kodes "fra ... til ...", da dette er varigheden af ​​hans tjeneste.

Kaptajn John Smiths regiment blev udstationeret ved Escaut-floden ved Valenciennes ugen før våbenhvilen.  
*Så kan dette registreres som en begivenhed af typen "Militærtjeneste" med en dato på "mellem 4. november 1918 og 11. november 1918" (Gramps konverterer til et standard datoformat på trods af at der bruges 2 formater til indtastning) ved floden Escaut, Valenciennes, Nord-departementet, Frankrig... fordi den faktiske dato for denne "øjeblikkelige" begivenhed ikke er kendt i kilden.*

### Kalendere

Alternative kalendere er andre kalendere end den gregorianske kalender. I øjeblikket understøtter Gramps hebraiske, fransk-republikanske, julianske, islamiske, persiske og svenske alternative kalendere. For at angive en anden kalender end standard-gregorianske kalender, skal du tilføje kalenderens navn til datoen, f.eks. "9. januar 1905 (Juliansk)" eller bruge rullemenuen.

#### Svensk kalender

Den [Den svenske konge](wiki:Svenske_konger), Karl XII, besluttede, at Sverige skulle begynde at bruge den gregorianske kalender. Det var dog planlagt at ske gradvist ved at springe 11 skuddage over fra 29-02-1700 og slutte i 1744. Så 28-02-1700 blev efterfulgt af 01-03-1700. Dette fandt sted under den Store Nordiske Krig, og skudårsdagene blev beholdt i 1704 og 1708. I januar 1711 besluttede den samme konge, at Sverige skulle vende tilbage til den julianske kalender senest 1. marts 1712. For at være i fase blev der indsat en ekstra dag den 30. februar 1712. Og det var slutningen på den svenske kalender. Sverige konverterede til gregoriansk i 1. marts 1753 ved at springe datoer over mellem 18. februar 1752 og 28. februar 1753.

I Gramps kan du kun indtaste gyldige datoer for den svenske kalender fra 1. marts 1700 til 30. februar 1712. Alle andre datoer er markeret som ugyldige og skal rettes.

### Dobbeltdaterede datoer

Dobbeltdaterede datoer (også kaldet "dobbeltdatering", "skråstregsdatoer" og nogle gange "gammel stil/ny stil"-datoer) fremstår som "23. januar 1735/6". Dette forveksles ofte med en årsusikkerhed, men har faktisk en specifik historisk betydning. Den dobbeltdaterede dato repræsenterer et tidspunkt, hvor et område var i en overgang mellem at skifte til 1. januar som begyndelsen af ​​det nye år. Således er 23. januar 1735/6 en indikation for at gøre det klart, hvilken dato der refereres til. I dette eksempel kan "23. januar 1736" være indtruffet efter "23. juni 1736".

England og de amerikanske kolonier accepterede ikke officielt "1. januar" som nytårsdato før 1752. Før 1752 markerede den engelske regering stadig officielt den 25. marts som årets første dag, hvorimod størstedelen af ​​den engelske befolkning markerede den 1. januar som årets første dag. Mange skrev derfor datoer, der faldt mellem 1. januar og 25. marts, i dobbeltdateret format.

Nogle gange kan en dobbelt dato vises som en brøk, som på denne gravsten (170 og 3/4, hvilket betyder 1703 og 1704) (Se fig. {{#var:chapter}}.{{#expr:{{#var:figure}}+1}}):

![[_media/Gravestone.jpg|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Gravsten, der viser dobbelt dato som en brøk (170 og 3/4, hvilket betyder 1703 og 1704)]]

En dato kan markeres som dobbelt dateret ved blot at sætte et skråstreg `/` mellem årene. For eksempel:

- 1721/2
- 1719/20
- 1799/800

Disse skråstreg-år kan forekomme hvor som helst i en dato, hvor et almindeligt år kan forekomme.

Dobbeltdaterede datoer er i øjeblikket repræsenteret i den julianske kalender, så deres måned og dag vil være den samme som i den tekstuelle repræsentation. {{-}}

#### Alternativ nytårsdag

Med datoer med dobbeltdatering (og andre datoer) kan du vide, at det nye år blev fejret på en anden dag end 1. januar. For at angive dette i Gramps skal du sætte måned/dag-koden i parenteser eller runde parenteser `()` efter kalenderen (hvis en sådan findes). For eksempel:

- 20\. januar 1865 (`25. marts`)
- 20\. januar 1750 (`Julian`,`1. marts`)
- 23\. februar 1710/1 (`25. marts`)

For at angive begyndelsen af ​​et år, der er forskellig fra 1. januar, bruger du følgende datokoder :

- `1. januar`
- `1. marts`
- `25. marts`
- `1. september`

Du kan angive det som den eneste element i parentes eller lige efter et kalendernavn (komma og intet mellemrum).

Bemærk, at hvis nytårsdag ikke er 1. januar, så kommer januar efter december det år. Datoer med disse nytårsdagskoder vil blive sorteret korrekt.

{{-}}

[Category:Documentation](wiki:Category:Documentation)
