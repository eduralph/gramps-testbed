---
title: 'Da:Gramps 6.0 brugsanvisning - Indtaste og redigere data: detaljeret - del
  2'
categories:
- Documentation
- Pages using invalid self-closed HTML tags
- Stub
managed: false
source: wiki-scrape
wiki_revid: 129105
wiki_fetched_at: '2026-05-30T17:28:44Z'
lang: da
---

{{#vardefine:chapter\|9.2}} {{#vardefine:figure\|0}} **<span style="font-size:120%">Indtaste og redigere data: detaljeret Begivenheder, Medier, Steder, Kilder, Kildehenvisninger, Arkiver og Noter</span>**  
Det forrige afsnit gav dig en detaljeret oversigt over, hvordan du indtaster og redigerer data for personer, slægtsforhold og datoer. Dette afsnit fortsætter med andre objekter, du støder på i Gramps.

## Redigering af oplysninger om begivenheder <span id="Editing information about events"/>

![[_media/EventsCategory-EventsListView-example-60-da.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Begivenhedskategori - Begivenhedsvisning (Liste) - eksempel]]

Hvis du tilføjer en begivenhed til en person, kan du registrere oplysninger, du har fundet.

Når du tilføjer en begivenhed til , vises dialogboksen .

For at tilføje eller redigere begivenhedsdata skal du skifte til kategorivisningen og vælge den ønskede post på listen over begivenheder. Dobbeltklik på den post, eller klik på på værktøjslinjen for at åbne følgende dialogboks. {{-}}

### Ny begivenhed dialog <span id="New Event dialog"/>

![[_media/EditEvent-dialog-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Rediger begivenhed - dialogboks - eksempel]] Begivenheder redigeres via dialogboksen . Denne dialogboks kan tilgås ved at dobbeltklikke på en række i kategorivisningen Begivenhed. Begivenheder kan også redigeres via fanen [](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1/da#Events) i dialogboksen , eller via fanen [](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1/da#Events_2) i dialogboksen. Når begivenheder redigeres fra Person editoren eller Familie editoren benyttes dialogboksen [Redigering af begivenhedshenvisninger](#Event_Reference_Editor_dialog).

Den øverste del lader dig se og redigere grundlæggende oplysninger om begivenheden:

- kan vælges fra de tilgængelige typer, der er angivet i rullemenuen Begivenhedstype. f.eks. **Fødsel** (*standard*), Dåb, Død, Begravelse osv. Gramps  
  Du kan indtaste din egen begivenhed [Brugerdefinerede typer](wiki:Gramps_Glossary/da#custom) ved at skrive direkte i tekstboksdelen af ​​[kombinationsboksen](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window/da#Selector_Combo_Boxes).

- Begivenhedens kan være en præcis dato, et interval (*fra ... til ..., mellem ...*) eller en upræcis dato (*omkring ...*).
  - Knappen ![[_media/22x22-gramps-date.png]] starter dialogboksen .

- Feltet giver dig mulighed for at give en længere beskrivelse af, hvad denne begivenhed er.
  - \- Slå privatlivslåsen til/fra for at markere begivenhedsposten som privat, hvilket gør det muligt at udelade den fra rapporter.

- kan vælges fra en liste over tidligere indtastede steder ved hjælp af knappen eller indtastes på ny ved hjælp af knappen . Derudover kan du trække og slippe en stedpost i dette felt.

- er en unik identifikator for begivenheden. Lad dette felt stå tomt for at tillade Gramps at generere denne værdi automatisk for nye begivenheder.

<!-- -->

- giver dig mulighed for at vælge et eksisterende tag ved hjælp af knappen .

Nederst i vinduet er knapperne og . Hvis du klikker på , anvendes alle ændringer foretaget i alle faner, og dialogvinduet lukkes. Medmindre du ikke har indtastet data, vil du få vist advarslen . Hvis du klikker på knappen , lukkes vinduet uden at anvende nogen ændringer. Hvis du vælger , kommer du hertil.

#### Ny begivenhed fanesider <span id="New Event tab pages"/>

Den centrale del af vinduet viser faner, der indeholder forskellige kategorier af information. Klik på en fane for at se eller redigere dens indhold. Fanerne indeholder følgende informationskategorier for begivenhedsdataene:

##### Kildehenvisninger <span id="Source Citations"/>

  
Fanen giver dig mulighed for at se og redigere kilder, der er relevante for en begivenhed. Den centrale del af vinduet viser alle sådanne kildehenvisninger, der er gemt i databasen. Knapperne , og giver dig mulighed for at tilføje, ændre og fjerne en kildehenvisning, der er knyttet til en begivenhed. Bemærk, at knapperne og kun bliver tilgængelige, når en kildehenvisning er valgt fra listen.

##### Noter <span id="Notes"/>

  
Fanen giver et sted at registrere noter eller kommentarer om begivenheden. For at tilføje en note eller ændre eksisterende noter skal du blot redigere teksten i tekstindtastningsfeltet.

##### Galleri <span id="Gallery"/>

  
Fanen

#### Attributter <span id="Attributes"/>

=

  
Fanen

##### Henvisninger <span id="References"/>

  
Fanen

{{-}}

#### Kan ikke gemme begivenhed advarselsboksen <span id="Cannot save event warning dialog"/>

![[_media/Cannot-save-event-warning-dialog-60-da.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Begivenheden kan ikke gemmes - advarselsdialogboks]]

Advarselsboksen . Der findes ingen data for denne begivenhed. Indtast venligst data eller annuller redigeringen. Tryk på for at vende tilbage til . {{-}}

## Redigering af begivenhedshenvisninger <span id="Editing event references"/>

Begivenhedshenvisninger forbinder en begivenhed med en person og giver dig mulighed for at give yderligere oplysninger om begivenheden.

Når du tilføjer begivenhedshenvisninger til en fanen, vises dialogboksen .

{{-}}

### Begivenhedshenvisning editor dialogboks <span id="Event Reference Editor dialog"/>

Tilgang til [referenceobjekteditoren](wiki:Gramps_Glossary/da#reference_object_editor).

![[_media/EventReferenceEditor-dialog-default-60-da.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Begivenhedsreferenceeditor - dialog]]

Dialogboksen indeholder to sektioner, og .

- Sektionen angiver detaljerne knyttet til den specifikke reference til denne begivenhed. Sektionen har fanerne: , , og .
- Sektionen har fanerne: , , , og , .

{{-}}

#### Oplysning om henvisning <span id="Reference Information"/>

##### Oplysning om henvisning faner

###### Generelt <span id="General"/>

For personens i denne begivenhed skal du bruge rollefeltet [vælger-kombinationsboks](wiki:Gramps_Glossary/da#selector_combo_box). Vælg **[Primær](wiki:Gramps_Glossary/da#primary)** (som er *standard* under en Tilføj Begivenhed) mulighed for den primære modtager. Vælg en beskrivende Begivenhedsrolle (f.eks. [Hjælper](wiki:Gramps_Glossary/da#aide), [Brud](wiki:Gramps_Glossary/da#bride), [Celebrant](wiki:Gramps_Glossary/da#celebrant), [Præster](wiki:Gramps_Glossary/da#clergy), [Familie](wiki:Gramps_Glossary/da#family_role), [Gudforælder](wiki:Gramps_Glossary/da#godparent), [Brudgom](wiki:Gramps_Glossary/da#groom), [Informant](wiki:Gramps_Glossary/da#informant), [Vidne](wiki:Gramps_Glossary/da#witness)) for en Begivenhed, hvor Personen ikke er den Primære Deltager.

Begivenheder, der tilføjes til en person via deling eller ved træk og slip, vil som standard blive tildelt begivenhedsrollen **[Ukendt](wiki:Gramps_Glossary/da#unknown)**. Hvis personen har en tilsvarende rolle, skal deres rolle også indstilles til Primær.

Hvis ingen af ​​de foruddefinerede roller er passende, skal du tilføje en rolle *[Brugerdefinerede typer](wiki:Gramps_Glossary/da#custom)* i tekstboksdelen af ​​[vælger-kombinationsboksen](wiki:Gramps_Glossary/da#selector_combo_box). Ved at indtaste det nye, unikke rollenavn (i stedet for at vælge et fra rullemenuen) oprettes en ny brugerdefineret rolletype. Nye brugerdefinerede rolletyper vil blive tilføjet til rullemenulisten. Den forbliver der, indtil træet eksporteres og genimporteres eller renses via et [Tredjepartstilføjelse](wiki:Third-party_Addons)-værktøj som [Type Cleanup](wiki:Addon:Types_Cleanup_Tool).

Nogle eksempler på brugerdefinerede typer til begivenhedsroller foreslås i artiklen [Roles, Relations and Associations](wiki:Roles,_Relationships_%26_Associations). {{-}}

###### Kildehenvisninger

###### Attributter

###### Noter

{{-}}

#### Delte oplysninger

{{-}}

##### Delte oplysninger faner

###### Generelt

###### Kildehenvisninger

###### Attributter

###### Noter

###### Galleri

###### Henvisninger

{{-}}

## Redigering af oplysninger om medieobjekter <span id="Editing information about media objects"/>

For at tilføje eller redigere mediedataobjekter skal du skifte til kategorivisningen og for et eksisterende medieobjekt vælge den ønskede post i medielisten. Dobbeltklik på den post, eller klik på på værktøjslinjen for at åbne editordialogboksen for at redigere eksisterende oplysninger. Eller vælg knappen på værktøjslinjen for at se både editordialogboksen og dialogboksen for at vælge og derefter ændre medieobjektdetaljerne, før du tilføjer dem.

### Nyt Medie dialogboks <span id="New Media dialog"/>

![[_media/NewMediaEditor-dialog-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Nyt Medie Editor - dialog]]

Den øverste sektion viser et miniaturebillede af medieobjektet, hvis det er tilgængeligt, sammen med en oversigt over dets egenskaber (ID, dato, sti og *objekttype*), som du kan se og redigere. Du kan indtaste disse oplysninger direkte i de tilsvarende felter.

- En beskrivende for dette medieobjekt. Enten genereret automatisk baseret på medieobjektets filnavn eller indtastet manuelt.

<!-- -->

- er en unik post til at identificere medieobjektet. Lad feltet stå tomt for at få det genereret af Gramps.

  - Privatlivsknapper for dette medieobjekt
    - (standard) eller

    - 

- indtast en dato tilknyttet medieobjektet (f.eks.: for et billede kan det være den dato, det blev taget). Du kan også bruge:

  - ![[_media/22x22-gramps-date.png]] knappen for at åbne dialogboksen .

- til medieobjektet på din computer. Gramps gemmer ikke mediet internt, det gemmer kun stien! Indstil i 's sektion for at undgå at genindtaste den fælles basismappe, hvor alle dine medier er gemt. Værktøjet kan hjælpe med at administrere stier til en samling af medieobjekter.

<!-- -->

- - knap.

  - knap åbner dialogboksen , der lader dig fjerne eller tildele eksisterende brugerdefinerede mærkater.

Den nederste del af vinduet viser fire notesbogsfaner, der indeholder forskellige kategorier af information. Klik på en fane for at se eller redigere dens indhold. Den nederste del af vinduet har knappen , der bringer dig hertil. Knappen lukker vinduet uden at gemme ændringer, og knappen gemmer alle ændringer foretaget i alle faner og lukker dialogvinduet.

Dobbeltklik på miniaturebilledet åbner medieobjektet i en ekstern fremviser, hvis tilgængelig.

#### Kan ikke gemme medieobjekt advarselsdialogboks<span id="Cannot save media object warning dialog"/>

![[_media/Cannot-save-media-object-warning-dialog-60-da.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Kan ikke gemme medieobjekt - advarselsdialog]]

Advarselsdialogen vises, når du ikke har indtastet nok information om det nye medieobjekt. Indtast venligst data eller annuller redigeringen. {{-}}

### Nyt Medie fanesider <span id="New Media tab pages"/>

Fanerne repræsenterer følgende kategorier af mediedata:

- 

- 

- 

- 

#### Kildehenvisninger <span id="Source Citations"/>

Fanen giver dig mulighed for...

#### Attributter <span id="Attributes_4"/>

Fanen giver dig mulighed for at se og redigere bestemte oplysninger om medieobjektet, der kan udtrykkes som attributter. Den nederste del viser listen over alle sådanne attributter gemt i databasen. Den øverste del viser detaljerne for den aktuelt valgte attribut på listen (hvis nogen). Knapperne , og lader dig tilføje, ændre eller fjerne en attribut. Bemærk, at knapperne og kun bliver tilgængelige, når en attribut er valgt fra listen.

#### Noter <span id="Notes_4"/>

Fanen giver et sted til at registrere forskellige oplysninger om kilden, som ikke passer pænt ind i andre kategorier. Dette område er især nyttigt til registrering af information, der ikke naturligt passer ind i "Parameter/Værdi"-parrene, der er tilgængelige for attributter. For at tilføje en note eller ændre eksisterende noter skal du blot redigere teksten i tekstindtastningsfeltet.

#### Henvisninger <span id="References_3"/>

Fanen angiver alle databaseposter, der refererer til et givet medieobjekt. Listen kan sorteres efter en hvilken som helst af dens kolonneoverskrifter: `Type`, `ID` eller `Navn`. Dobbeltklik på en post giver dig mulighed for at se og redigere den tilsvarende post.

{{-}}

## Redigering af medieobjekthenvisninger <span id="Editing media object references"/>

Når medieobjekthenvisninger forbinder et medieobjekt til et andet objekt på en fane, vil knappen vise -knappen filvælger, og når du har valgt et medieobjekt, vises dialogboksen .

{{-}}

### Vælg et medieobjekt filvælger <span id="Select a media object file chooser"/>

![[_media/SelectAMediaObject-file-selector-dialog-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Vælg et medieobjekt - (Fil)vælger Dialog - eksempel]]

[filvælger](wiki:Gramps_6.0_Wiki_Manual_-_Settings/da#File_Chooser) giver dig mulighed for at forhåndsvise og vælge en mediefil, du vil vedhæfte, og samtidig kan du redigere den viste (Standard til filtypenavnet uden filnavnet).

- (afkrydsningsfeltet er ikke markeret som standard, indtil det er markeret første gang og huskes for hvert efterfølgende billedvalg.)

Se også:

- [Vælg medieobjektvælger](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1/da#Select_Media_Object_selector)
- [Slægtsbogens mediesti &gt; Basismediesti:](wiki:Gramps_6.0_Wiki_Manual_-_Settings/da#Family_Tree.27s_Media_path)

<!-- -->

- [](wiki:Gramps_6.0_Wiki_Manual_-_Tools/da#Media_Manager) en gruppe af fire separate værktøjer, hvoraf to giver dig mulighed for at:
  - 

  - 

{{-}}

### Redigering af Mediehenvisning editor <span id="Media Reference Editor dialog"/>

![[_media/MediaReferenceEditor-dialog-collapsed-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Redigering af mediehenvisning editor - dialogboks]]

Dialogen .

Se også [Sådan opretter du billedreferenceområder](wiki:Sådan_opretter_du_billedreferenceområder) {{-}} ![[_media/MediaReferenceEditor-dialog-expanded-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Mediereferenceeditor - dialogboks - &quot;Delt information&quot; udvidet eksempel]]

Du kan også udvide sektionen **Delt information**.

{{-}}

#### Øverste sektion <span id="Top section"/>

##### Øverste sektions fanesider <span id="Top section tab pages"/>

###### Generelt

- Regions hjørner: x1, x2, y1, y2.

-delen gør det muligt at vælge et specifikt område på medieobjektet. Du kan bruge musemarkøren på billedet til at vælge en region, eller bruge disse spin-knapper til at indstille det øverste venstre og nederste højre hjørne af det refererede område. Punkt (0,0) er det øverste venstre hjørne af billedet og (100.100) det nederste højre hjørne.

- Fortrolighed

-knappen lader dig markere, om posten anses for at være privat eller ej. Marker feltet for at markere denne .

Se også [Fortalt websted](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_7#Page_Generation) Galleri-fanen understøtter output fra disse refererede områder.

{{-}}

###### Kildehenvisninger

###### Attributter

###### Bemærkninger

{{-}}

#### Delt information

##### Fanerne Delt information

###### Generelt

###### Henvisninger

###### Kildehenvisninger

###### Attributter

###### Noter

{{-}}

## Redigering af oplysninger om steder

For at redigere oplysninger om steder, skift til kategorien i Navigator sidepanelet og vælg den ønskede post fra listen over steder. Dobbeltklik på denne post, eller klik på knappen på værktøjslinjen for at åbne dialogen .

{{-}}

### Stedredigering-dialog <span id="Place_Editor_dialog"/>

![[_media/PlaceEditor-dialog-example-60-da.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Stedseditor - dialog - eksisterende stedseksempel]]

For at tilføje et nyt sted eller redigere oplysninger om eksisterende steder skal du skifte til kategorien Steder og vælge den ønskede post fra listen over steder. Dobbeltklik på denne post, eller klik på knappen på værktøjslinjen for at få -dialogen frem:

Følgende felter er tilgængelige:

- Titelområdet øverst viser beskrivelsen af dette sted, der skal bruges i rapporter. Gramps vil konstruere dette for dig. Se sektion \> generationsmulighed.

- 

  - -knappen åbner -dialogen, hvor du kan tilføje/redigere yderligere information.

- . Alle **[Tilpassede typer](wiki:Gramps_Glossary#custom)** vises nederst på listen. Vælg mellem følgende standard tilgængelige sted **Typer**:

  - *Amt*
  - *Antal* (fejloversættelse - skal være nummer, som i husnummer)
  - *By*
  - *Bydistrikt*
  - *Bygning*
  - *Departement*
  - *Distrikt*
  - *Gade*
  - *Gård*
  - *Kommune*
  - *Land*
  - *Landsby*
  - *Mindre by*
  - *Mindre landsby*
  - *Nabolag*
  - *Nummer* - Se valgmuligheden for \*\* *Område*
  - *Provins*
  - *Sogn*
  - *Stat*
  - *Stedsangivelse*
  - **Ukendt** (*standard*)

<hr>

- positionen for stedet nord eller syd for den geografiske ækvator angivet i decimal- eller gradnotation. Gyldige værdier er f.eks. 12.0154, 50°52'21.92\\N, N50º52'21.92\\ eller 50:52:21.92. Du kan indstille disse værdier via Geografivisningen ved at søge på stedet eller via en korttjeneste i Stedsvisningen. Se: [Understøttede længde-/breddegradsformater](#Supported_longitude.2Flatitude_formats) Se: [Koordinatformat:](wiki:Gramps_6.0_Wiki_Manual_-_Settings/da#Display_Options) i Indstillinger, da denne indstilling styrer visningen af ​​koordinater.

<!-- -->

- positionen for stedet i forhold til nul-meridianen (Greenwich i London) i decimal- eller gradnotation. Gyldige værdier er f.eks. -124.3647, 124°52'21.92\\E, E124º52'21.92\\ eller 124:52:21.92. Du kan indstille disse værdier via Geografivisningen ved at søge på stedet eller via en korttjeneste i Stedsvisningen. Se: [Understøttede længde-/breddegradsformater](#Supported_longitude.2Flatitude_formats) Se: [Koordinatformat:](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Display_Options) i præferencer Vises, da denne mulighed styrer visningen af ​​koordinater.

- 

### Stedredigering fanesider <span id="Place editor tab pages"/>

Fanerne repræsenterer følgende kategorier af steddata:

- 

- 

- 

- 

- 

- 

- 

#### Omsluttet af <span id="Enclosed By"/>

![[_media/PlaceEditor-EnclosedBy-tab-example-60-da.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Fanen "Omsluttet af" fra "Stedsredigering" - dialog - eksempel]]

Steder i Gramps gemmes i et hierarki. Fanen giver dig mulighed for at linke dette sted til andre steder, højere i hierarkiet, som omslutter det. Hvert link består af et sted og et valgfrit datointerval.

For at omslutte et eksisterende sted skal du bruge knappen til at vælge et sted fra [Stedsvælger](#Select_Place_selector). Alternativt kan du trække et sted (fra Udklipsholder, Stederkategorivisning eller en Begivenhedsredigering) ned i bunden af ​​fanen .

Knapperne , og giver dig mulighed for at tilføje et nyt sted som et omsluttende hierarkisk niveau, ændre det valgte omsluttende sted og fjerne et valgt link til et omsluttende sted.

Bemærk, at knapperne , og knapperne til ændring af rækkefølge (op, ned) kun bliver tilgængelige, når et link findes og er valgt fra listen. Generelt vil et land være et sted på topniveau og vil ikke være knyttet til noget andet sted.

**Se også:**

- [Enclosed By](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/da#Enclosed_By) Gramplet
- [Brug af udklipsholderen](wiki:Gramps_6.0_Wiki_Manual_-_Navigation/da#Using_the_Clipboard)

##### Vælg stedsvælger <span id="Select Place selector"/>

![[_media/SelectPlace-SelectorDialog-example-60-da.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Vælg sted - Valgdialog - eksempel]] ![[_media/SelectPlace-SelectorDialog-Alternate-Search-60-da.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Vælg sted - alternativ søgning eksempel]] Vælgerdialogen giver dig mulighed for at linke til et allerede eksisterende sted, og når det er valgt, åbnes det i .

Dialogen har to forskellige søge muligheder:

- Du kan bruge knappen til at filtrere listen baseret på en af ​​mulighederne fra rullelisten:
  - **Navn indeholder** (standard)
  - **Navn indeholder ikke**
  - **ID indeholder**
  - **ID indeholder ikke**
  - **Type indeholder**
  - **Type indeholder**
  - **Titel indeholder**
  - **Titel indeholder**
  - **Seneste ændring indeholder**
  - **Seneste ændring indeholder ikke**

<!-- -->

- Skriv navnet på det søgte - ikke i Find feltet. Den indtastede tekst vises i et felt, som dækker og knapperne. Så snart indtastningen starter vises det første sted, som matcher søgestrengen. Søgningen skelner ikke mellem store og små bogstaver.

{{-}} Se også:

- [Vælgerdialoger](wiki:Gramps_6.0_Wiki_Manual_-_Settings/da#Selector_dialogs)

##### Stedreferenceeditor

![[_media/PlaceReferenceEditor-dialog-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Stedsreferenceeditor - Dialog - eksempel]]

Den anden del af vinduet viser syv notesbogsfaner, der indeholder forskellige kategorier af information. Klik på en fane for at se eller redigere dens indhold. Den nederste del af vinduet har knapperne og . Hvis du klikker på , anvendes alle ændringer foretaget i alle faner, og dialogvinduet lukkes. Hvis du klikker på knappen , lukkes vinduet uden at anvende nogen ændringer.

{{-}}

#### Alternative Navne <span id="Alternative Names"/>

  
Fanen giver dig mulighed for at se og redigere andre navne, som stedet muligvis er kendt under. Fanen viser alle andre navne på stedet, der er gemt i databasen. Knapperne , og giver dig mulighed for at tilføje, ændre og fjerne en navnepost. Bemærk, at knapperne og kun bliver tilgængelige, når et navn er valgt fra listen.

#### Kildehenvisninger <span id="Source Citations"/>

  
Fanen giver dig mulighed for at se og redigere kilder, der er relevante for et sted. Den centrale del af vinduet viser alle sådanne kildehenvisninger, der er gemt i databasen. Knapperne , og giver dig mulighed for at tilføje, ændre og fjerne en kildehenvisning, der er knyttet til et sted. Bemærk, at knapperne og kun bliver tilgængelige, når en kildehenvisning er valgt fra listen.

#### Noter <span id="Notes"/>

  
Fanen viser eventuelle kommentarer eller noter vedrørende stedet. For at tilføje en note eller ændre eksisterende noter skal du blot redigere teksten i tekstindtastningsfeltet.

#### Galleri <span id="Gallery"/>

  
Fanen giver dig mulighed for at gemme og vise fotos og andre medieobjekter, der er knyttet til et givet sted. Den centrale del af vinduet viser alle sådanne medieobjekter og giver dig et miniaturebillede af billedfiler. Andre objekter, såsom lydfiler, filmfiler osv., er repræsenteret af et generisk Gramps-ikon. Knapperne , , og giver dig mulighed for at tilføje et nyt billede, tilføje en reference til et eksisterende billede, ændre et eksisterende billede og fjerne et medieobjekts link til stedet. Bemærk, at knapperne og kun bliver tilgængelige, når et medieobjekt er valgt fra listen.

#### Internet

  
Fanen indeholder internetadresser, der er relevante for stedet. (Denne fane udviser identisk funktionalitet som [Fanen Internet](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1/da#Internet) for Person-editoren, og dens [Internetadresseeditor](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1/da#Internet_Address_Editor) er også den samme.)

<!-- -->

  
Den nederste del af vinduet viser alle sådanne internetadresser, der er gemt i databasen. Den øverste del viser detaljerne for den aktuelt valgte adresse på listen (hvis nogen). Knapperne , og giver dig mulighed for at tilføje, ændre og fjerne en internetadresse. Knappen (repræsenteret af et ikon med en grøn pil og en gul cirkel) åbner din browser og fører dig til den webside, der svarer til den fremhævede internetadresse. Bemærk, at knapperne , og kun bliver tilgængelige, når en adresse er valgt fra listen.

#### Henvisninger <span id="References"/>

  
Fanen angiver alle databaseposter (begivenheder eller LDS-ordinancer), der refererer til et sted. Disse oplysninger kan ikke ændres fra dialogboksen . I stedet skal den tilsvarende begivenhedspost (f.eks. en fødselsbegivenhed) åbnes, og dens stedreference redigeres.

{{-}}

### Redigering af stednavne dialogboks <span id="Place Name Editor dialog"/>

![[_media/PlaceNameEditor-dialog-default-60-da.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Dialogboksen "Redigering af stednavne" - standard]]

Dialogboksen tilgås fra knappen i dialogboksen eller fra fanen .

Dialogboksen giver dig mulighed for at tilføje/redigere følgende oplysninger:

- stedets navn

- Datointerval, hvor stedet er gyldigt

  - ![[_media/22x22-gramps-date.png]] knap

- Sprog, hvor navnet er skrevet. Gyldige værdier er ISO-koder på to tegn, f.eks.: en, fr, de, nl. Se Wikipedia for den fulde liste over gyldige [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes)-koder.

{{-}}

### Understøttede længdegrad/breddegradsformater <span id="Supported longitude/latitude formats"/>

Når du opretter/ændrer et sted, er de mulige formater, der bruges til længdegrads-/breddegradskoordinater:

<table>
<thead>
<tr>
<th colspan="2"><p>Længdegrads- og breddegradsformater</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p>D.D4</p></td>
<td><p>gradnotation, 4 decimaler</p>
<dl>
<dt></dt>
<dd>
f.eks. +12.0154, -124.3647
</dd>
<dd>
4 <a href="https://wikipedia.org/wiki/Decimal_degrees#Precision">decimals of longitude precision</a> tillader en tilnærmelse på 11.132 meter (36.5223097 fod) ved ækvator.
</dd>
</dl></td>
</tr>
<tr>
<td><p>D.D8</p></td>
<td><p>gradnotation, 8 decimaler (<a href="https://wikipedia.org/wiki/Decimal_degrees#Precision">precision</a> ligesom ISO-DMS)</p>
<dl>
<dt></dt>
<dd>
f.eks. +12.01543265, -124.36473268
</dd>
</dl></td>
</tr>
<tr>
<td><p>DEG</p></td>
<td><p>Grad-, minut- og sekundnotation</p>
<dl>
<dt></dt>
<dd>
f.eks. 50°52'21.92"N, 124°52'21.92"Ø (°-symbolet har UTF-8-kode c2b00a)
</dd>
<dd>
eller N50º52'21.92", Ø124º52'21.92" (º-symbolet har UTF-8-kode c2ba0a)
</dd>
<dd>
Tegnet for sekunder kan enten være et dobbelt anførselstegn "
</dd>
<dd>
eller to enkelte anførselstegn '
</dd>
<dd>
Bogstaverne N/S/V/Ø kan placeres før eller efter cifrene.
</dd>
</dl></td>
</tr>
<tr>
<td><p>DEG-</p></td>
<td><p>grad-, minut- og sekundnotation med:</p>
<dl>
<dt></dt>
<dd>
f.eks. -50:52:21.92, 124:52:21.92
</dd>
</dl></td>
</tr>
<tr>
<td><p>ISO-D</p></td>
<td><p>ISO 6709 gradnotation</p>
<dl>
<dt></dt>
<dd>
dvs. ±DD.DDDD±DDD.DDDD
</dd>
</dl></td>
</tr>
<tr>
<td><p>ISO-DM</p></td>
<td><p>ISO 6709 grader, minutnotation</p>
<dl>
<dt></dt>
<dd>
dvs. ±DDMM.MMM±DDDDMM.MMM
</dd>
</dl></td>
</tr>
<tr>
<td><p>ISO-DMS</p></td>
<td><p>ISO 6709 grader, minutter, sekunder notation</p>
<dl>
<dt></dt>
<dd>
dvs. ±DDMMSS.SS±DDDMMSS.SS
</dd>
</dl></td>
</tr>
</tbody>
</table>

{{-}}

Se: [Koordinatformat:](wiki:Gramps_6.0_Wiki_Manual_-_Settings/da#Display_Options) i indstillingerne Vis, da denne indstilling styrer visningen af ​​koordinater.

## Redigering af information om kilder <span id="Editing information about sources"/>

Fra en af ​​kategorivisningerne kan du vælge eller oprette en ny kilde, eller hvis du har valgt knapperne eller , vises editordialogboksen .

### Dialogboks Ny kilde <span id="New Source dialog"/>

![[_media/NewSource-editor-dialog-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Ny kilde - editordialog - eksempel]]

I editordialogen giver de generelle oplysninger i den øverste del af vinduet dig mulighed for at definere grundlæggende oplysninger om kilden: dens , , og . Du kan indtaste disse oplysninger direkte i de tilhørende felter.

- Kildens titel.

- Kildens forfattere.

- Publikationsoplysninger, såsom by og udgivelsesår, udgiverens navn, ...

- Angiv en kort titel, der bruges til sortering, arkivering og hentning af kildeposter.

  - Låseikon til/fra.

- en unik post til at identificere kilden. Genereres af Gramps, når feltet er tomt.

- - 

{{-}}

### Ny kilde fanesider <span id="New Source tab pages"/>

Fanerne indeholder følgende informationskategorier for kildedata:

#### Noter <span id="Notes"/>

  
Fanen giver et sted at registrere noter eller kommentarer om kilden. For at tilføje en note eller ændre eksisterende noter skal du blot redigere teksten i tekstindtastningsfeltet. Kun primære objekter kan vises i fanen : Person, Familie, Begivenhed, Sted eller Medieobjekt. Sekundære objekter såsom Navne og Attributter kan kun tilgås via de primære objekter, de tilhører.

#### Galleri <span id="Gallery"/>

  
Fanen giver dig mulighed for at gemme og vise fotos og andre medieobjekter, der er knyttet til en given kilde (f.eks. et foto af en fødselsattest). Den centrale del af vinduet viser alle sådanne objekter og giver dig et miniaturebillede af billedfiler. Andre objekter, såsom lydfiler, filmfiler osv., er repræsenteret af et generisk Gramps-ikon. Knapperne , , og giver dig mulighed for at tilføje et nyt billede, tilføje en reference til et eksisterende billede, ændre et eksisterende billede og fjerne et medieobjekts link til relationen. Bemærk, at knapperne og kun bliver tilgængelige, når et medieobjekt er valgt fra listen.

#### Attributter <span id="Attributes"/>

  
Fanen viser "Nøgle/Værdi"-par, der kan være knyttet til kilden. Disse ligner de "Attributter", der bruges til andre typer Gramps-poster. Forskellen mellem disse nøgle/værdi-par og attributter er, at attributter kan have kildereferencer og noter, mens nøgle/værdi-data muligvis ikke har det.

<!-- -->

  
Den centrale del af vinduet viser alle eksisterende nøgle/værdi-par. Knapperne og giver dig mulighed for at tilføje og fjerne par. For at ændre teksten i nøgle eller værdi skal du først vælge den ønskede post. Klik derefter i enten nøgle- eller værdicellen for den post og skriv din tekst. Når du er færdig, skal du klikke uden for cellen for at afslutte redigeringstilstand.

#### Arkiver <span id="Repositories"/>

![[_media/NewSource-Repositories-tab-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Arkiver" tab from "Ny kilde" - dialog - eksempel]]

  
Fanen viser referencerne til de arkiver, hvor kilden findes. Listen kan sorteres efter en af ​​dens kolonneoverskrifter: , , og . Ved at dobbeltklikke på en post kan du se og redigere posten i . Du kan også redigere referencen. Knapperne på siden af ​​fanen giver dig mulighed for at tilføje et nyt arkiv, linke til (eller dele) et eksisterende arkiv, redigere referencen til arkivet eller fjerne referencen.

##### Redigering af arkivhenvisning <span id="Repository Reference Editor"/>

![[_media/Repository-Reference-Editor-example-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Redigering af arkivhenvisning - Dialog - eksempel]] Dialogboksen **Redigering af arkivhenvisning** åbnes ved at dobbeltklikke på en post i fanen i dialogboksen [Kilderedigering](#Editing_information_about_sources).

Den giver mulighed for at gemme type og kaldenummer for en kilde i et bestemt arkiv. Da en kilde kan findes i flere arkiver. (Jeg har muligvis en fotokopi i mit personlige bibliotek. En kopi af den originale bog kan være i <abbr title="Allen County Public Library">ACPL</abbr> Genealogy Center i Ft. Wayne, Indiana. Mikrofilmen kan være i FamilySearch Library i Salt Lake City, Utah. Hver kan findes ved hjælp af forskellige kaldenummer.)

###### Oplysning om henvisning <span id="Reference information"/>

Afsnittet Oplysning om henvisning har fanerne og . Fanen Generelt har et tekstfelt til og en [rullemenu](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window/da#Combo_Boxes).

Valg af medietype: Lyd, **Bog** *(standard)*, Kort, Elektronisk, Kort, Film, Magasin, Manuskript, Kort, Avis, Foto, Gravsten, Ukendt, Video samt eventuelle [brugerdefinerede typer](wiki:Gramps_Glossary/da#custom).

###### Delte oplysninger <span id="Shared information"/>

Afsnittet tilbyder alle mulighederne i dialogboksene [Arkiv Editor](#New_Repository_dialog) med fanerne Generelt, Adresser, Internet, Noter og Referencer. {{-}}

##### Vælg Arkiv-vælger <span id="Select Repository selector"/>

![[_media/SelectRepository-SelectorDialog-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Vælg arkiv - vælger - eksempel]]

Dialogboksen giver dig mulighed for at linke til et allerede eksisterende arkiv, og når det er valgt, åbnes det i <span id="Repository_Reference_Editor"></span>

Du kan bruge knappen til at filtrere listen baseret på en af ​​mulighederne fra rullelisten:

- **Titel indeholder** (standard)
- *Titel indeholder ikke*
- *ID indeholder*
- *ID indeholder ikke*
- *Seneste ændring indeholder*
- *Seneste ændring indeholder ikke*

{{-}}

#### Henvisninger <span id="References"/>

  
Fanen viser alle databaseposter, der refererer til denne kilde, hvis der er nogen. Listen kan sorteres efter en hvilken som helst af dens kolonneoverskrifter: , eller . Ved at dobbeltklikke på en post kan du se og redigere posten.

{{-}}

## Redigering af kildehenvisninger <span id="Editing source citations"/>

Kildehenvisninger forbinder en kilde med et andet objekt og giver mulighed for at give yderligere oplysninger om kilden. Kildehenvisninger kan knyttes til et stort antal objekter,

- [Personer og forskellige oplysninger om personer](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1/da#Editing_information_about_people) (såsom deres navn, adresse osv.),
- [Slægtsforhold (familier) og forskellige oplysninger om relationer](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1/da#Editing_information_about_relationships),
- [Begivenheder og forskellige oplysninger om begivenheder](#Editing_information_about_events),
- [Medieobjekter og attributter for medieobjekter](#Editing_information_about_media_objects),
- [Steder og forskellige oplysninger om steder](#Editing_information_about_places),
- [Adresser på repositorier](#Editing_information_about_repositories).

For hvert objekt findes et fælles sæt knapper:

-  (Opret og tilføj en ny kildehenvisninger og en ny kilde). Dette åbner en tom kildehenvisningsdialogboks.

<!-- -->

-  (Tilføj en eksisterende kildehenvisning eller kilde). Dette åbner dialogboksen Kilde eller Kildehenvisning.

<!-- -->

-  (Rediger den valgte kildehenvisning). Dette åbner kildehenvisningsdialogboksen, der er forudfyldt med kildehenvisnings- og kildeoplysninger.

<!-- -->

-  (Fjern den eksisterende kildehenvisning). Dette fjerner kildehenvisningen fra objektet. Det sletter ikke selve kildehenvisningen, som derefter kan forbindes med et andet objekt.

Bemærk, at knapperne og kun bliver tilgængelige, når en kildehenvisning er valgt.

{{-}}

### Vælg kilde eller citatvælger <span id="Select Source or Citation selector"/>

![[_media/SelectSourceOrCitation-SelectorDialog-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Vælg kilde eller kildehenvisning - Valgdialog - eksempel]]

Når tilføjer en eksisterende kildehenvisning eller kilde, vises dialogboksen [vælger](wiki:Gramps_Glossary/da#selector).

Dette giver mulighed for at vælge enten en eksisterende kilde eller en eksisterende kildehenvisning (sammen med den tilhørende kilde). Klik på afsløringstrekanten ud for en kilde for at se de kildehenvisninger, der er knyttet til den pågældende kilde. Hvis en af ​​dine kilder f.eks. var en bog, ville kildehenvisningerne normalt henvise til en side (eller sider) i bogen. Hvis du allerede har en kildehenvisning, der refererer til den specifikke side i bogen, kan du vælge den kildehenvisning, som derefter deles. Hvis dette objekt derimod skal referere til en ny side, skal du vælge kilden og indtaste den nye side i den efterfølgende dialogboks.

Du kan bruge knappen til at filtrere listen baseret på en af ​​mulighederne fra rullelisten:

- **Kilde: Titel eller henvisning: Bind/side indeholder**(standard)
- *Kilde: Titel eller henvisning: Bind/side indeholder ikke*
- *ID indeholder*
- *ID indeholder ikke*
- *Seneste ændring indeholder*
- *Seneste ændring indeholder ikke*

{{-}}

### Ny kildehenvisningsdialogboks <span id="New Citation dialog"/>

![[_media/NewCitation-editor-dialog-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Ny kildehenvisning - editordialog - eksempel]]

Når du har valgt en kildehenvisning eller en kilde, eller hvis du har valgt knapperne eller , vises dialogboksen .

Dialogboksen indeholder en sektion kaldet samt sektion med faner. {{-}}

#### Kildehenvisningsoplysninger <span id="Citation information"/>

Afsnittet angiver de detaljer, der er knyttet til den specifikke reference til denne kilde: , og samt fanerne , , og . Du kan vælge troværdighedsniveauet fra rullemenuen . De resterende detaljer kan indtastes i de tilsvarende tekstfelter.

- Dato knyttet til denne kildehenvisning. Bruges typisk til at gemme den dato, hvor dataene blev indtastet i det originale kildedokument (ikke datoen, hvor begivenheden fandt sted).

  - ![[_media/22x22-gramps-date.png]] -knappen starter dialogboksen .

-   
  Specifik placering i de refererede oplysninger. For et udgivet værk kan dette omfatte bindet af et flerbindsværk og sidetal(ler). For et tidsskrift kan det omfatte bind-, nummer- og sidetal. For en avis kan det omfatte et spaltenummer og et sidetal. For en upubliceret kilde kan dette være et arknummer, sidetal, rammenummer osv. En folketællingsoptegnelse kan have et linjenummer eller bolig- og familienumre ud over sidetallet.

<!-- -->

-   
  Niveauet formidler afsenderens kvantitative evaluering af troværdigheden af ​​en information baseret på dens understøttende beviser. Det er ikke hensigten at eliminere modtagerens behov for selv at evaluere beviserne. (Vist i som -kolonnen)

  - *Meget lav* = Upålidelig dokumentation eller estimerede data.

<!-- -->

- - *Meget lav* = Upålidelig dokumentation eller estimerede data.
  - \*\**Lav* = Tvivlsom pålidelighed af bevismateriale (interviews, folketælling, mundtlige slægtsforskninger eller potentiale for bias, f.eks. en selvbiografi).
  - **Normal** - (standard) Bevismaterialet har muligvis ingen problemer eller er ikke blevet vurderet. Ikke valideret endnu.
  - *Høj* = Sekundært bevismateriale, data officielt registreret engang efter begivenheden.
  - *Meget høj* = Direkte og primære bevismaterialer anvendt, eller ved bevismaterialets dominans.

- Udfyldes automatisk af Gramps, når feltet er tomt

- 

Et advarselsikon  vises, hvis citatet deles.  

{{-}}

##### Vælg kildevælger <span id="Select Source selector"/>

![[_media/SelectSource-selector-dialog-example-50.PNG|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Vælg kilde - Vælgerdialog - eksempel]]

Vælgerdialogen giver dig mulighed for at linke til en allerede eksisterende kilde.

Du kan bruge knappen til at filtrere listen baseret på en af ​​mulighederne fra rullelisten:

- **Titel indeholder** (standard)
- *Titel indeholder ikke*
- *Forkortelse indeholder*
- *Forkortelse indeholder ikke*
- *Ophavsmand indeholder*
- *Ophavsmand indeholder ikke*
- *ID indeholder*
- *ID indeholder ikke*
- *Seneste ændring indeholder*
- *Seneste ændring indeholder ikke*

{{-}}

##### Kildehenvisningsoplysninger faner <span id="Citation information section tab pages"/>

Fane-sektionen indeholder følgende informationskategorier for Kildehenvisningsdata:

###### Noter <span id="Notes"/>

Fanen giver et sted at registrere noter eller kommentarer om kildehenvisningen. Den centrale del af vinduet viser alle noter til denne kildehenvisning og giver dig et eksempel på begyndelsen af ​​noten. Knapperne , , , , og giver dig mulighed for at tilføje en ny note, dele den valgte note, redigere den valgte note, fjerne den valgte note og flytte den valgte note op eller ned på listen over noter. Bemærk, at knapperne , , , og kun bliver tilgængelige, når et medieobjekt er valgt fra listen. Fjernelse af en note fjerner kun noten fra denne kildehenvisning, det sletter ikke selve noten. Se [detaljer om redigering af noter](#Editing_information_about_notes).

###### Galleri <span id="Gallery"/>

Fanen giver dig mulighed for at gemme og vise fotos og andre medieobjekter, der er knyttet til en given citat (f.eks. et foto af en side i en bog eller en side i en folketælling). Den centrale del af vinduet viser alle sådanne objekter og giver dig et miniaturebillede af billedfiler. Andre objekter såsom lydfiler, filmfiler osv. er repræsenteret af et generisk Gramps-ikon. Knapperne , , og giver dig mulighed for at tilføje et nyt billede, tilføje en reference til et eksisterende billede, ændre et eksisterende billede og fjerne et medieobjekts link til citatet. Bemærk, at knapperne og kun bliver tilgængelige, når et medieobjekt er valgt fra listen. Se [detaljer om redigering af mediereferencer](#Editing_media_object_references).

###### Attributter <span id="Attributes"/>

Fanen viser "Nøgle/Værdi"-par, der kan være knyttet til kildehenvisningen. Disse ligner de "Attributter", der bruges til andre typer Gramps-poster. Forskellen mellem disse nøgle/værdi-par og attributter er, at attributter kan have kildehenvisninger og noter, mens nøgle/værdi-data ikke kan.

Den centrale del af vinduet viser alle eksisterende nøgle/værdi-par. Knapperne og giver dig mulighed for at tilføje og fjerne par. For at ændre teksten i nøgle eller værdi skal du først vælge den ønskede post. Tryk derefter på knappen for at vælge nøglen, eller klik i enten nøgle- eller værdicellen for den pågældende post og skriv din tekst. Når du er færdig, skal du klikke uden for cellen for at afslutte redigeringstilstand.

##### Henvisninger <span id="Referencer"/>

=

Fanen viser alle databaseposter, der refererer til denne kilde, hvis nogen. Listen kan sorteres efter en hvilken som helst af dens kolonneoverskrifter: , eller . Dobbeltklik på en post giver dig mulighed for at se og redigere posten.

{{-}}

## Redigering af oplysninger om arkiver <span id="Editing information about repositories"/>

Når du har valgt en kilde, eller hvis du har valgt knapperne eller , vises dialogboksen .

Se også:

- [Kategorien Arkiver](wiki:Gramps_6.0_Wiki_Manual_-_Categories/da#Repositories_Category)

### Dialogboks for nyt arkiv <span id="New Repository dialog"/>

![[_media/NewRepository-editor-dialog-example-60-da.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Nyt arkiv - editordialogboks]]

Følgende felter vises:

- for arkivet (hvor kilder er gemt).

<!-- -->

- af arkivet kan være fysiske eller virtuelle strukturer, hvor genealogiske og familiehistoriske kilder er gemt:

  - *Album*
  - *Arkiv*
  - *Boghandel*
  - *Kirkegård*
  - *Kirke*
  - *Samling*
  - **Bibliotek** (standard)
  - *Pengeskab*
  - *Ukendt*
  - *Websted*

-   
  en entydig registrering til at identificere arkivet. Lad feltet stå tomt for at blive genereret af Gramps.

- Låseikon til/fra.

- - 

{{-}}

### Arkiv fanesider <span id="Repository tab pages"/>

Fanerne repræsenterer følgende kategorier af arkivdata:

- 

- 

- 

- 

#### Adresser <span id="Addresses"/>

Fanen giver dig mulighed for at se og registrere de forskellige adresser i arkivet.

Den nederste del af vinduet viser alle adresser, der er gemt i databasen. Den øverste del viser detaljerne for den aktuelt valgte adresse på listen (hvis nogen). Knapperne , og giver dig mulighed for at tilføje, ændre og fjerne en adressepost fra databasen. Bemærk, at knapperne og kun bliver tilgængelige, når en adresse er valgt fra listen.

#### Internet <span id="Internet_2"/>

Fanen viser internetadresser, der er relevante for arkivet. (Denne fane udviser identisk funktion som [Fanen Internet](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1#Internet) for Person-editoren, og dens [Internetadresseeditor](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1#Internet_Address_Editor) er også den samme.)

Den nederste del viser alle sådanne internetadresser og tilhørende beskrivelser. Den øverste del viser detaljerne for de aktuelt valgte adresser på listen (hvis nogen). Knapperne , og giver dig mulighed for at tilføje, ændre og fjerne en internetadresse. Knappen "Gå" (repræsenteret af et ikon med en grøn pil og en gul cirkel) åbner din webbrowser og fører dig direkte til den fremhævede side. Bemærk, at knapperne og kun bliver tilgængelige, når en adresse er valgt fra listen.

#### Noter <span id="Notes_10"/>

  
Fanen giver et sted at registrere noter eller kommentarer om arkivet. For at tilføje en note eller ændre eksisterende noter skal du blot redigere teksten i tekstindtastningsfeltet.

#### Henvisninger <span id="References_8"/>

  
Fanen angiver alle databaseposter, der refererer til et givet arkiv. Listen kan sorteres efter en hvilken som helst af dens kolonneoverskrifter: , eller . Dobbeltklik på en post giver dig mulighed for at se og redigere den tilsvarende post.

{{-}}

## Redigering af noter <span id="Editing information about notes"/>

Se også:

- [Kategorien Noter](wiki:Gramps_6.0_Wiki_Manual_-_Categories/da#Notes_Category)

### Note editor dialog <span id="Note editor dialog"/>

![[_media/NewNote-editor-dialog-example-with-context-menu-60-da.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Ny Note - editor dialog]] Når du opretter en ny note, eller når du redigerer en eksisterende note, vises dialogboksen . Der er to faner, fanen **** og fanen ****.

#### Note-fanen <span id="Note tab"/>

Fanen er det område, hvor tekst tilføjes. Teksten kan formateres ved hjælp af mange standard tekstredigeringsværktøjer.

##### Note værktøjslinje

:\* En værktøjslinje til at anvende stilarter (eller skrifttypedekorationer) på tekst i dine noter. Du kan vælge og anvende en af ​​værktøjsknapperne eller indstille de ønskede værdier og begynde at skrive.

::\* : Skrår teksten for at fremhæve den, almindeligt i de fleste teksteditorer

::\* : Gør teksten mørkere for at fremhæve den, almindeligt i de fleste teksteditorer

::\* : Tegner en linje under teksten, almindeligt i de fleste teksteditorer

::\* : Tegner en linje igennem, bruges ofte til at angive tekst, der skal slettes

::\* : Hæver teksten en smule, bruges ofte til fodnoter (f.eks. Wikipedia<sup>2</sup>)

::\* : Sænker teksten en smule, bruges ofte i formler (f.eks. H<sub>2</sub>O)

::\* : Rullemenu, en grundlæggende skrifttypevælger, der viser alle skrifttyper, der er installeret på dit operativsystem.

::\* : Rullemenu, vælg størrelsen på den skrifttype, der skal bruges til din tekst.

::\* : Fortryder sidste handling.

::\* : Genanvender sidste "Fortryd" handling.

::\* : Vælg farven på din skrifttype.

::\* : Tilføjer en baggrundsfarve til den tekst, du indtaster.

::\* : Åbner , så du kan oprette et internt link til et element i Gramps, såsom en person, familie, begivenhed, note osv. Eksterne URL-links kan også oprettes.

::\* : Returnerer markeret tekst til almindelig tekst. Fjerner eventuelle links.

##### Kontekstmenu i tekstvisning <span id="Textview context menu"/>

:\* Højreklik på tekstarealet for at vise kontekstmenuen:

<hr>

::\*  - valgt, eller alternativt kan du trykke på og højreklikke med museknappen - *Vises kun, når et link er valgt i tekstvisningen*

::\*  - og du kan indsætte indholdet et andet sted - *Vises kun, når et link er valgt i tekstvisningen*

::\*  - Åbner , så du kan oprette og ændre det valgte link. - *Vises kun, når et link er valgt i tekstvisningen*

::\*  - Den vigtigste post i denne kontekstmenu er stavekontrol. Du får tilbudt et udvalg af installerede sprog på dit system med stavekontrol aktiveret. En [stavekontrol](wiki:Gramps_6.0_Wiki_Manual_-_Settings/da#Environment_Settings) er tilgængelig for *engelsk* og dit installerede lokale sprog (Bemærk i afsnittet at aktivere indstillingen for global engelsk som standard eller det sprog, din Gramps kører på, og notekontekstmenuen er pr. note på det valgte sprog efter eget valg)

:::\*

:::\*  - (standard)

::\*  - den markerede tekst.

::\*  - den markerede tekst.

::\*  - den tidligere klippede eller kopierede tekst.

::\*  - den markerede tekst.

<hr>

::\*  - teksten i tekstvisningen.

::\* -

::\* -

<hr>

##### Note-egenskaber <span id="Note proberties"/>

:\* Nogle egenskaber for en note

::\* afkrydsningsfelt: Noter i Gramps betragtes som ombrydelige for at give indholdet mulighed for at tilpasse sig rapportens sidestørrelse og formatering for den mest harmoniske præsentation. I standardindstillingen ignoreres linjeskift (linjeskift og linjeretur) og mellemrum automatisk, så der dannes komplette afsnit, som er defineret af en tom linje mellem to tekstblokke.  
Når er markeret, antager Gramps, at de mellemrum og linjer, du indtastede i noterne, er vigtige. Brug *Præformateret* til tabeller, bogstavelige transskriptioner osv. Brug af en monospace-skrifttype vil hjælpe med at holde forudsigelige kolonnebredder og marginer ved forudsigelige.  
Prøv ikke at bruge præformateret, medmindre det er absolut nødvendigt, da de oprettede rapporter vil flyde mere naturligt.

::\* Privatliv er det samme som på de andre objekter. Med et enkelt klik kan du angive, at en note skal betragtes som privat, så Gramps kan fjerne den fra alt oprettet output.

::\* et unikt ID for noten. Hvis feltet ikke er angivet, genereres der automatisk et ID i henhold til indstillingerne i præferencerne.

<div id="note_type">

::\* (`Generelt` standard) Notetypen. Du kan tilføje din egen [brugerdefinerede type](wiki:Gramps_Glossary/da#custom) ved at indtaste den direkte. Tilføjelse af en note vil automatisk indstille typen, så den matcher det objekt, den tilføjes til. (f.eks. vil en note, der tilføjes via fanen Noter i Person-editoren, som standard have typen *Personnote*.)

  
  
{\|class="wikitable"

! style="text-align:left;"\| Type ! Genkendt for funktioner i \|- \|*[<primært objekt>](wiki:Gramps_Glossary/da#primary_object)* Note \| \|- \|*[<sekundært objekt>](wiki:Gramps_Glossary/da#secondary_object)* Note \| \|- \|Kildehenvisning \| \|- \|Generelt \|*(standard)* \|- \|Html-kode \|[Fortalt websted](wiki:Gramps_6.0_Wiki_Manual_-_Reports#Narrated_Web_Site) rapportinkluderinger; eksporter til GEDCOM \|- \|Link \| \|- \|Rapport \| \|- \|Forskning \| \|- \|Kildetekst \| \|- \|To Do \|[To Do](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/da#To_Do) Gramplet, [ToDo Notes Gramplet](wiki:Addon:ToDoNotesGramplet) Addon. *Ikke at forveksle med ToDo-tagbaserede rapporter.* \|- \|Transskription \| \|- \|Ukendt \| \|}

</div>

::\* Vælg et mærkat til noten: f.eks. Færdig, Todo osv... Du kan tilføje dine egne mærkater ved at skrive det. Rapporter baseret på mærkater inkluderer: [Mærkater-rapport](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_6#Tag_Report), [Todo-rapport](wiki:Addon:ToDoReport)

:::\* Knappen åbner dialogboksen , der lader dig fjerne eller tildele eksisterende brugerdefinerede mærkater. {{-}}

#### Fanen Henvisninger <span id="References tab"/>

Fanen angiver alle objekter, der refererer til en given note. Listen kan sorteres efter en hvilken som helst af dens kolonneoverskrifter: `Type`, `ID` eller `Navn`. Dobbeltklik på en post eller vælg en post og brug knappen for at se og redigere den tilsvarende post.

### Link-editor <span id="Link Editor"/>

![[_media/Note-LinkEditor-dialog-default-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Note "Link Editor" - dialog - standardindstilling aktiv person - eksempel]]

For at oprette et link i en note skal **en blok med notetekst først markeres for at link-editoren kan være aktiv**, og når ikonet for knappen [Noteværktøjslinjens](#Note_Toolbar) er valgt, vil du blive vist . Der er ingen visuel indikator, når knappen i noteværktøjslinjen er inaktiv.

De links, der er oprettet i noten, bliver blå og viser en understregning, når du holder musen over den linkede tekst. Mens du arbejder i Gramps-noten, kan du enten trykke på  + venstreklik på museknappen eller fra højreklik på [Textview kontekstmenu](#Textview_context_menu) vælge , hvilket tillader enten redigeringsvinduet for det valgte objekt at åbne eller åbne HTML URL-linket i din standardinternetbrowser.

Den sande kraft af links vises, når en [Narrated Web Site](wiki:Gramps_6.0_Wiki_Manual_-_Reports#Narrated_Web_Site) eller [Dynamic Web](wiki:Addon:DynamicWeb_report) webstedsrapport oprettes. De oprettede links bliver til ægte navigationslinks til andre sider i webrapporten.

#### Note-linkredigeringsdialog <span id="Note Link Editor dialog"/>

![[_media/Note-LinkEditor-dialog-InternetAddress-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Note "Linkredigering" - dialog - viser linktypen: Internetadresse - eksempel]]

Note-dialogen viser som standard den aktive *Person*, og når den er valgt for hvert af de andre objekter, det relevante aktive objekt. Eller du kan vælge linktypen *Internetadresse*.

Følgende muligheder vises:

- angiver linktypen for enten et af de ni aktive Gramps-elementer/objekter som standard den aktive *Person* eller en *Internetadresse*, du indtaster manuelt.

<!-- -->

- - *Internetadresse* - ([<abbr title="Uniform Resource Locator, også kendt som en webadresse">URL</abbr>](https://en.m.wikipedia.org/wiki/URL)) - hvis valgt, bliver feltet tilgængeligt for dataindtastning.
  - *[Begivenhed](wiki:Events)*
  - *Familie*
  - *Medier*
  - *Note*
  - **Person** (standard)
  - *[Sted](wiki:Places)*
  - *Arkiver*
  - *[Kilde](wiki:Sources)*
  - *[Kildehenvisninger](wiki:Citations)*
    -  knap: åbner den relevante [vælgerdialog](wiki:Gramps_6.0_Wiki_Manual_-_Settings/da#Selector_dialogs) for eksisterende elementer i den kategori, der er angivet i linktypen. **Ikke relevant for valg af internetadresse.**

    - -knap: åbner et vindue til at oprette et nyt element for det angivne Gramps-element. Hvis et nyt element oprettes, udfyldes Gramps-elementfeltet og internetadressefeltet automatisk med de relevante data.

- viser det valgte element, f.eks.: Hvis Person er valgt, og den aktive persons navn derefter vises, se skærmbilledet. **Ikke relevant for valg af internetadresse.**

  - Dette felt genereres automatisk ved valg af knappen /knappen /knappen .

- -knap: åbner editordialogboksen for det angivne Gramps-element. Det valgte element udfylder automatisk Gramps-elementfeltet og internetadressefeltet med de relevante data.

- - for = Gramps-typen vil automatisk udfylde denne boks, men indholdet vil være gråtonet
  - for = *Internetadresse* (standard er: [`https://`](https://) ) sletter du standardindstillingen fra Gramps og indtaster den fulde internetadresse enten manuelt eller via kopier og indsæt.

![[_media/Note-showing-tooltip-for-link-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Notes Editor - Lænket tekst med værktøjstip - eksempel]]

Se også:

- [Internetadresse Editor](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1/da#Internet_Address_Editor)
- [Note Link Report](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_6/da#Note_Link_Report)

{{-}}

### Note tekstmarkering og præformatering i rapporter

Tekstmarkering som **fed**, farve, <u>understregning</u>, ... kan tilføjes til noter. En note kan være præformateret eller ej. Det afhænger af outputtypen, hvordan denne tekstmarkering vil se ud. Her gives en oversigt over, hvad du kan forvente.

- **PDF** og **direkte udskrivning** (til printer eller til fil) understøtter fuldt ud tekstmarkering og den præformaterede indstilling
- **ascii** udskrivning fjerner al tekstmarkering fra noterne af indlysende årsager

<!-- -->

- **LaTeX** understøtter den præformaterede indstilling og understøtter delvist fontfremhævelsesstile og størrelsesmarkering;  
  output understøtter ikke skrifttypefamilie- eller farvemarkering.
- **Narrative Web**. Mange bruger Narrative Web-rapporten som en nem måde at arbejde med deres data på. Denne rapport forsøger at respektere tekstmarkering i noterne. Dette er en fortolket oversættelse, den er ikke en-til-en.
- **ODF** output understøtter ikke tekstmarkering.
- **RTF** output understøtter ikke tekstmarkering.
- **html** output understøtter ikke tekstmarkering.

{{-}}

[Category:Documentation](wiki:Category:Documentation)
