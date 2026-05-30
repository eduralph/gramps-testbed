---
title: Da:Gramps 6.0 brugsanvisning - Indstillinger
categories:
- Documentation
- Stub
managed: false
source: wiki-scrape
wiki_revid: 129503
wiki_fetched_at: '2026-05-30T16:58:54Z'
lang: da
---

{{#vardefine:chapter\|15}} {{#vardefine:figure\|0}}

Dette afsnit omhandler indstillinger, du kan administrere i Gramps enten i dialogboksen eller [andre forskellige indstillinger](wiki:Da:Gramps_6.0_brugsanvisning_-_Indstillinger#Andre_indstillinger). Desuden forskellige måder at [tilpasse](wiki:Da:Gramps_6.0_brugsanvisning_-_Indstillinger#Tilpasning) Gramps på.

## ![[_media/Gramps-preferences.png]] Dialogboksen Indstillinger <span id="Preferences"></span>

![[_media/EditPreferencesTabsOnly-overview-60-da.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Oversigt over alle standardindstillinger]]

De fleste af de indstillinger, der påvirker hele Gramps-programmet, konfigureres i dialogboksen . For at åbne den skal du vælge menuen (på macOS ) eller vælge ikonet på værktøjslinjen.

Der er nogle få konfigureringer, der kan indstilles *før* kørsel af Gramps (f.eks. indstilling af sproget vist i brugerfladerne eller for rapporter), som kan indstilles midlertidigt eller permanent fra [kommandolinjegrænsefladen](wiki:Gramps_6.0_Wiki_Manual_-_Command_Line).

For konfigurationsmuligheder, der er begrænset til den aktuelle visning eller Grampletter, skal du vælge enten via menuen , klikke på værktøjslinjeknappen ![[_media/Gramps-config.png]] eller trykke på *Konfigurer aktiv visning* [tastaturgenvej](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings#Common_keybindings).

Fanerne øverst viser de tilgængelige valgkategorier som følger:

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

- 

Andre ekstra faner kan også vises fra eventuelle tilføjelser, du måtte have installeret.

### Data

![[_media/EditPreferences-Data-tab-default-60-da.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menu: &quot;Rediger -&gt; Indstillinger...&quot; Standardindstillinger for fanen &quot;Data&quot;]] Fanen indeholder indstillinger, der er relevante for følgende to sektioner:

- 

- 

{{-}}

#### Visningsvalg <span id="Display Options"></span>

![[_media/EditPreferences-Data-tab-DisplayOptions-section-default-60-da.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menu: &quot;Redigér -&gt; Indstillinger&quot; &quot;Data&quot; fane &quot;Visningsvalg&quot; sektion standardværdier]] Sektionen har følgende muligheder:

- Denne indstilling styrer visningen af ​​steder. Denne funktion blev mærket som "Aktiver automatisk generering af stedtitler" i 5.0-versionen og som "Stedformat (automatisk stedtitel)" i 5.1-versionen. [hierarkiet af steder](wiki:Gramps_4.1_Wiki_Manual_-_What%27s_new%3F#Place_hierarchies) var nyt i [4.1.0](wiki:Template:Releases/4.1.0)-versionen, og [fanen Steder](wiki:Gramps_4.2_Wiki_Manual_-_Settings#Places) under Præferencer eksisterede kun i 4.2-versionen. Større revisioner forventes for stedhierarkier, så disse grænseflader vil sandsynligvis blive flyttet og omdøbt igen. \*\* **Fuld** (standard)

  - - Hvis du vælger knappen , vises

<!-- -->

- Denne indstilling styrer visningen af ​​koordinater. (Se [Understøttede længdegrad/breddegradsformater](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_2/da#Supported_longitude.2Flatitude_formats))

  - **DEG Grad, minutter, sekunder notation** (standard)
  - DEG-: grader, minutter, sekunder notation med:
  - D.D4 grader notation, 4 decimaler
  - D.D8 grader notation, 8 decimaler (præcision som ISO-DMS)
  - RT90 Outputformat for det [svenske koordinatsystem RT90](https://en.wikipedia.org/wiki/Swedish_grid)

<!-- -->

- Denne indstilling styrer visningen af ​​navne i den aktuelle slægtsbog (database). (Indstillingen gemmes i databasen og er ikke systemomfattende). I Gramps er der to typer navnevisningsformater: de foruddefinerede formater og de brugerdefinerede brugerdefinerede formater.. Flere forskellige foruddefinerede navneformater er tilgængelige: **"Efternavn, Fornavn suffiks"** (standard), *"Fornavn Efternavn suffiks"*, *"Fornavn"*, *"Primær\[efter\] Primær\[for\] Ikke-patronymisk, Fornavn patronymisk\[efter\] suffiks Primær\[bin\]"*

  - Hvis du klikker på knappen i højre side, åbnes et vindue , hvor den tilgængelige liste over muligheder vises. Formatet er givet samt et eksempel. Når foruddefinerede formater ikke er egnede, kan man definere sit eget format. Du kan bruge knappen til at tilføje et navneformat til listen. Hvis du klikker én gang, får du formatet **EFTERNAVN, Fornavn suffiks(kald)**, f.eks.: **SMITH, Edwin Jose Sr (Ed)**. Hvis du har tilføjet nye navneformater til listen, bliver knapperne og tilgængelige til at ændre listen over navneformater.

<!-- -->

- -   
    Afkrydsningsfeltet er som standard ikke markeret. Hvis dette er markeret, kan Gramps betragte patronym- og matronymnavne som efternavne.

- Denne indstilling styrer visningen af ​​datoer. Det er en global indstilling, der kræver en genstart af Gramps for at træde i kraft, og den gælder for visning af datoer i alle databaser, der er indlæst i Gramps, indtil datovisningsformatet ændres igen. Der findes flere forskellige formater, som kan afhænge af din lokale indstilling.

  - **ÅÅÅÅ-MM-DD (ISO)** (standard) - Eksempel 2020-09-30 - Viser datoen ved hjælp af den internationale standard [ISO 8601 Data elements and interchange formats – Information interchange](https://wikipedia.org/wiki/ISO_8601) er især nyttig, når man deler data mellem lande med forskellige konventioner for at skrive numeriske datoer og klokkeslæt.
  - Numerisk
  - Måned Dag, År
  - MAN DAG, ÅR
  - Dag Måned År
  - DAG MAN ÅR

<!-- -->

- 

  - **År** (standard)
  - År, Måneder
  - År, Måneder, Dage

- 

- 

<!-- -->

- **Gregoriansk** (standard). Denne indstilling styrer visningen af ​​kalenderen på rapporter, værktøjer, gramplets og visninger. Der findes flere forskellige kalendere (se [Date Edition](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_Editing_Data:_Detailed_-_part_1#Editing_dates)). To datoer med to forskellige kalendere vil ikke vise tidslinje eller periode korrekt (f.eks. hvis man bruger den gregorianske kalender som standardkalender, vil brugerne have en bedre sammenhæng i visningen af ​​datoer i perioden).

- **Gregoriansk** (standard).

- **På den foregående dag** (standard).

<!-- -->

- Denne indstilling styrer de oplysninger, der vises i statuslinjen. Dette kan enten være **[Aktiv persons](wiki:Gramps_Glossary/da#active_person) navn og ID** (standard) eller **Forhold til [home person](wiki:Gramps_Glossary/da#home_person)**.

<!-- -->

- **Legacy** (standard). Vælg mellem de tilgængelige plugins til at sammensætte og vise kildehenvisningsdata. Det indbyggede "Legacy" [CITE-plugin](wiki:Addon_list_legend#cite) er kompatibelt med version 5.1.6 og tidligere.

{{-}}

##### Redigering af stedformat <span id="Place Format Editor"></span>

![[_media/EditPreferences-Data-tab-DisplayOptions-section-PlaceFormatEditor-dialog-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Redigering af stedformat - dialog (default) fra Menu: "Redigér &gt; Indstillinger" - "Data" fane "Visningsvalg" sektion]]

Dialogboksen indeholder præferencer, der er relevante for, hvordan steder skal vises.

Dialogboksen kan tilgås fra fanen  - "Data" i sektionen [Displayindstillinger](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Display_Options) via knappen på indstillingen .

Dialogboksen giver dig mulighed for at oprette brugerdefinerede stedsformater ved at bruge knappen i venstre kolonne og vælge, hvordan hver del af det viste sted skal vises, baseret på følgende indstillinger:

- `Ny` (som standard) - Et navn til stedsformatet anbefales kraftigt, at du ændrer dette til at være unikt.

- `:` (standard kolon ":" betyder visning af alle stednavne) - Vælg hierarkiets niveauer for de stednavne, der skal vises.

  - Hvert niveau i hierarkiet er repræsenteret af et positivt heltal, startende med 0 for det valgte sted og stigende med 1 for hvert niveau op i hierarkiet. Niveauerne kan også repræsenteres af negative heltal, startende med -1 for det øverste niveau (normalt et land) og faldende med 1 for hvert niveau lavere i hierarkiet. Derudover er det befolkede sted (by, landsby eller landsby) repræsenteret af bogstavet p; dette kan bruges med en forskydning (f.eks. p+1 eller p-2).
  - De navne, der skal vises, er defineret som en kommasepareret liste over intervaller. Et interval kan enten være et enkelt niveau eller et startniveau og et slutniveau adskilt af et kolon. Startniveauet skal være mindre end slutniveauet i et interval. Start- og slutniveauerne er som standard 0 og -1, hvis de mangler.

- \- Saml nummer og gade for at undertrykke kommaet.

  - **Ingen** (standard) - Vis som den er.
  - *Gadenummer* - For at disse muligheder kan virke, skal gaden have [<strong>Type</strong>](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_2#Place_Editor_dialog) *Gade* og husnummeret skal have **Type** *Nummer*.
  - *Gadenummer* - i henhold til *Gadenummer*

- (Tom som standard) En [tocifret sprogkode](https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes).

-  (afkrydsningsfeltet er ikke markeret som standard)

Du kan fjerne et brugerdefineret stedformat ved hjælp af knappen .

har som standard et foruddefineret format med navnet **Fuld**.

Se også (engelsk):

- [Implement place formats \#368](https://github.com/gramps-project/gramps/pull/368)
- [Hierarchical Place Structure](wiki:Hierarchical_Place_Structure)
- <https://gramps-project.org/wiki/index.php/GEPS_045:_Place_Model_Enhancements_-_Place_Changes_Screenshots#Enhanced_Place_Format_Editor>
- [(Gramps-users) Proposed place formatting dialogs](https://sourceforge.net/p/gramps/mailman/message/36637553/) From: Nick Hall. - 2019-04-11
- <https://sourceforge.net/p/gramps/mailman/message/36422019/>
- <https://sourceforge.net/p/gramps/mailman/message/36363239/>
- <https://sourceforge.net/p/gramps/mailman/message/35694337/>
- [Place Editor dialog](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_2#Place_Editor_dialog)
- [Place Name Editor dialog](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_2#Place_Name_Editor_dialog)

{{-}}

###### Eksempel på stedformater <span id="Example Place Formats"></span>

Editoren har et felt kaldet "niveauer". Det giver brugerne mulighed for at vælge hierarki-niveauer på stedet løst baseret på python-strengudskæringssyntaksen. Et antal kolonintervaller kan angives i en kommasepareret liste. "0" repræsenterer det laveste niveau - typisk en bygning eller gade. "-1" repræsenterer det højeste niveau - typisk et land. Det befolkede sted er repræsenteret som "p".

For eksempel: "p:" = Befolket sted og opefter. "p,-1" = Befolket sted og land.

Gyldige muligheder:

- `0 - 9` - Hierarkiniveau
- `-` - Negativ
- `:` - ??
- `p` - Befolket sted
- `,` - komma

Eksempler på stedformater

- \["p:" = Befolket sted og opefter\]
- \["p,-1" = Befolket sted og land.\]
- \[1,p Hus og by\],\[p,1 By og hus\]

Det giver dig mulighed for at begrænse lange stedbeskrivelser i rapporter og visninger. [1](https://github.com/gramps-project/gramps/pull/368#issuecomment-290886087)

##### Vis navneredigering <span id="Display Name Editor"></span>

![[_media/EditPreferences-Data-tab-DisplayOptions-section-DisplayNameEditor-dialog-default-60-da.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;Vis navneredigering&quot; - dialogboks (standard) fra menuen: &quot;Rediger&gt;Indstillinger...&quot; - fanen &quot;Data&quot; &gt; sektionen &quot;Visningsvalg&quot;]] Med kan du definere brugerdefinerede navneformater, der kan vises i rapporter og diagrammer på globalt niveau eller pr. person-niveau.

har to sektioner:

- sektion vist øverst

- tabelsektion

kan tilgås fra menuen:  - fanen \> sektionen knappen. {{-}}

###### Hjælpereference <span id="Help Reference"></span>

![[_media/EditPreferences-Data-tab-DisplayOptions-section-DisplayNameEditor-dialog-default-60-da.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Øverste del af vinduet viser de forskellige navnedele.]]

Hjælpereference over 'Navnedele':

<hr>

Følgende nøgleord erstattes med de relevante navnedele:

- **Fornavn** - fornavn (first name)
- **Titel** - titel (Hr., Dr.)
- **Kaldenavn** - kaldenavn
- **Initialer** - forbogstav i fornavn
- **Forstavelse** - forstavelser (præfix) (von, de)
- **Efternavn** - efternavne (med forstavelse og bindeled)
- **Suffix** - suffix (Jr., Sr.)
- **Tilnavn** - tilnavn
- **Almindelig** - tilnavn som første option hvis det findes, kaldenavn som sekundær option, ellers det første fornavn

<hr>

  
Efternavne:

- **Resten** - ikke-primære efternavne
- **Familietilnavn** - familiekælenavn
- **Primært, Primært\[for\] eller \[efter\] eller \[bin\]**- fuldt primært efternavn, præfiks, kun efternavn, forbindelse
- **Patronym, eller \[for\] eller \[efter\] eller \[bin\]** - fuldt pa/matronymt efternavn, præfiks, kun efternavn, bindeled
- **Ikke patronym**- alle efternavne, undtagen pa/matronym og primært
- **Rå efternavne**- efternavne (ingen præfikser og forbindelser)

<hr>

Ekstra parenteser og kommaer fjernes. Anden tekst vises som indtastet.

<hr>

  
**Eksempel:** Dr. Edwin Jose von der Smith and Weston Wilson Sr (“Ed”) - Underhills  

*Edwin Jose*: **Fornavne**, *von der*: **Prefix**, *Smith* og *Weston*: **Primary**, *and*: <abbr title="a connector">**\[con\]**</abbr>, *Wilson*: **Patronym**,  

*Dr.*: **Titel**, *Sr*: **Suffix**, *Ed*: **Tilnavn**, *Underhills* <abbr title="family nick name">**Familie-tilnavn**</abbr>, Jose <abbr title="called (preferred given name)">**Kaldenavn**</abbr>.

<hr>

{{-}}

###### Hjælpereference Eksempel person <span id="Help Reference Example person"></span>

![[_media/wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_3#Name_Editor|[_media/NameEditor-format_reference_example-51.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Redigering af navne - referenceperson vist i dialogboksen [Redigering af navne]]]]

Alle felterne for hjælpereferencepersonen **Eksempel** undtagen familiens kaldenavn kan tilføjes i standarddialogboksen Personredigering. Dobbeltklik på det foretrukne navn under fanen Navne i Personredigering for at få adgang til yderligere felter, herunder: familiens kaldenavn, grupperingskontroller, undtagelsessorterings- og visningskontroller, datointervalkontroller for brug af et bestemt navn. {{-}}

###### Liste over navneformater <span id="Display Name list"></span>

![[_media/EditPreferences-Data-tab-DisplayOptions-section-DisplayNameEditor-dialog-default-60-da.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Nederste del af vinduet viser listen over definerede navneformater]]

I dette afsnit kan du tilføje, fjerne eller redigere eksisterende navneformater samt se et eksempel på det formaterede navn.

Tabellen viser to overskrifter og

- \- Baseret på de viste navnedele

- \- Viser det navneformat, der er anvendt på en ? [indbygget referenceperson](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Help_Reference_Example_person) ?

Listen viser fire standard visningsnavneformater, de er:

- *Efternavn, givet suffiks* - viser navnet som:
- *Givent efternavnssuffiks* - viser navnet som:
- *Given* - viser navnet som: *Edwin Jose*
- *xxx*' - viser navnet som:

<!-- -->

- \- et nyt navneformat, skriv de nødvendige nøgleord efter behov, og tryk på -tasten for at se det resulterende

- \- et eksisterende navneformat (undtagen de fire standardnavneformater)

- \- et eksisterende navneformat (undtagen de fire standardnavneformater )

{{-}}

#### Indtastningsvalg <span id="Input Options"></span>

![[_media/EditPreferences-Data-tab-InputOptions-section-default-60-da.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menu: &quot;Rediger -&gt; Indstillinger...&quot; fanen &quot;Data&quot; sektionen &quot;Indtastningsvalg&quot;]] {{-}}

- <span id="surname guessing"></span> Denne indstilling påvirker et barns oprindelige efternavn, når de tilføjes til slægtsbogen.
  - **Faders efternavn** (standard) - bruger faderens efternavn.
  - *Ingen* - betyder, at der ikke vil blive forsøgt at gætte efternavnet.
  - *Kombination af moders og faders efternavn* - bruger faderens navn efterfulgt af mors navn.
  - *[Islandsk stil](https://wikipedia.org/wiki/Icelandic_name)* - vil bruge faderens fornavn efterfulgt af suffikset "sson" (f.eks. vil Edwins søn blive gættet som Edwin*sson*).

- \- brugt af dialogboksen . \*\* **Ukendt** (standard)

  - *Gift*
  - *Ugift*
  - *Borgerlig vielse*

<!-- -->

-   
  Sidste Dages Hellige

{{-}}

### Generelt <span id="General"></span>

![[_media/EditPreferences-General-tab-EnviromentSettings-section-default-60-da.png|Right|thumb|450px|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menu: "Rediger -&gt; Indstillinger..." Fanen "Generelt" "Miljøindstillinger" sektionens standardindstillinger]]

Denne fane indeholder en sektion med indstillinger, der er relevante for programmets generelle drift.

#### Miljøindstillinger <span id="Environment Settings"></span>

-   
  Denne afkrydsningsboks styrer aktivering og deaktivering af dialogboksen ved opstart.

-   
  Hvis du vælger denne afkrydsningsboks, indlæses den sidst brugte database ved opstart. Det omgår dialogboksen **Administrer slægtsbøger**.

-   
  Denne afkrydsningsboks styrer aktivering og deaktivering af visningen af ​​den sidste [Visning](wiki:Gramps_Glossary/da#view). Aktivering bringer dig til den visning, hvor du stoppede programmet sidst.

-   
  Denne afkrydsningsfeltfunktion styrer aktivering og deaktivering af den globale stavekontrol for noter. Pakken **[gspell](https://gitlab.gnome.org/GNOME/gspell)** skal indlæses, for at dette kan have en effekt.[2](https://github.com/gramps-project/gramps/pull/1450) (Se: [Fejlfinding af stavekontrol](wiki:Fejlfinding_af_stavekontrol)) (Bemærk, at indstillingen Rediger\>præferencer aktiverer global engelsk eller det sprog, din Gramps kører på, og at notekontekstmenuen er pr. note på det valgte sprog efter eget valg)

- *markeret* (standard) Denne checkbox styrer, om en tekstbeskrivelse vises ved siden af ​​ikonet i [Navigator](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window#Navigator) i [Hovedvindue](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window#Main_Window). Denne indstilling træder i kraft, når programmet er blevet genstartet.

<!-- -->

- 

- 

- 

- 

- 

- 

  - **Både tekst og ikoner** (standard)
  - *Kun tekst*
  - *Udelukkende ikoner*

- *checked*(standard)

<!-- -->

- Standard: `<b>%s</b>`

  - Praktiske markup er:
    - <b>\<b\>Fed\</b\></b> (Standard)
    - <big>\<big\>Gør skrifttypen relativt større\</big\></big>
    - <i>\<i\>Kursiv\</i\></i>
    - <s>\<s\>Gennemstreget\</s\></s>
    - <sub>\<sub\>Subscript\</sub\></sub>
    - <sup>\<sup\>Superscript\</sup\></sup>
    - <small>\<small\>Gør skrifttypen relativt mindre\</small\></small>
    - `<tt>Monospace-skrifttype</tt>`
    - <u>\<u\>Understreg\</u\></u>
      - For eksempel: \<u\>\<b\>%s\</b\>\</u\> viser <u><b>Understreget fed dato</b></u>.

<!-- -->

- Standard: `150` Pixels

#### Dagens tip-dialogboks <span id="Tip of the Day dialog"></span>

![[_media/TipOfTheDay-dialog--example-PrivacyInGramps-60.png|Right|thumb|400px|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Dagens tip-dialogboks - eksempel]]

Når den er aktiveret i fanen , viser dialogboksen nyttige tips.

Følgende muligheder er tilgængelige:

-  (afkrydsningsfelt markeret som standard - når aktiveret) - fjern markeringen for at forhindre yderligere tips i at blive vist.

- \- Gå videre til næste tip.

- \- afslut denne session, indtil Gramps-programmet genstartes.

{{-}}

### Slægtsbog <span id="Family Tree"></span>

![[_media/EditPreferences-FamilyTree-tab-default-60-da.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menu:  - fanen &quot;Slægtsbog&quot; - standardindstillinger]] Fanen indeholder følgende fire sektioner:

- 

- 

- 

- 

Se også:

- [Sikkerhedskopiering af en slægtsbog](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees#Backing_up_a_Family_Tree) - mere information om sikkerhedskopier
- [Backup omissions](wiki:Template:Backup_Omissions) - what is not included during a backup

{{-}}

#### Databaseindstillinger <span id="Database Settings"></span>

![[_media/EditPreferences-FamilyTree-tab-DatabaseSetting-section-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menu:  - "Slægtsbog" - fane - "Databaseindstillinger" sektionens standardindstillinger]]

- \-

  - **[SQLite](wiki:Gramps_Glossary/da#sqlite)** (*standard*) - [DB-API Database Backend](wiki:DB-API_Database_Backend)
  - ... Hvis andre database backend-tilføjelser er installeret, vil de blive tilføjet til listen <abbr title="exempli gratia - latinsk frase, der betyder 'for eksempel'">f.eks.</abbr>: [PostgreSQL](wiki:Addon:PostgreSQL) backend

Se også:

- Tilføjelse [PostgreSQL](wiki:Addon:PostgreSQL) - dette tilføjer eksperimentel understøttelse af PostgreSQL-databaser. Anbefales kun til eksperter!

{{-}}

#### Database placering <span id="Database Location"></span>

![[_media/EditPreferences-FamilyTree-tab-DatabaseLocation-section-default-60-da.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menu:  - fanen "Slægtsbog" - sektionen "Database placering"]]

- \- Serveradresse eller anden computer-IP-adresse for databasens placering.

- \- Portnummer for at få adgang til værtsdatabasen

- Medmindre du har en bestemt grund til at ændre dette, skal du beholde standardstien. Standardstien, hvor databaser gemmes, er `grampsdb` i [Brugermappen](wiki:Gramps_6.0_Wiki_Manual_-_User_Directory).

{{-}}

#### Håndtering af backup <span id="Backup Management"></span>

![[_media/EditPreferences-FamilyTree-tab-BackupManagement-section-default-60-da.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menu:  - fanen "Slægtsbog" - sektionen "Håndtering af backup"]]

- \- Placering, hvor dine Gramps sikkerhedskopieringsarkivfiler skal gemmes.

- \- Hvis du vælger denne indstilling, sikkerhedskopieres dit slægtsbog, når du vælger at afslutte bedstefar. Filen gemmes i den sikkerhedskopieringssti, der er angivet ovenfor. Filnavnet på sikkerhedskopien vil matche den tilføjede slægtsbog med en dato og et klokkeslæt.

- Tidsinterval til udløsning af fulde sikkerhedskopier under Gramps redigeringssessioner.

  - **Aldrig** (*standard*)
  - Hvert 15. minut
  - Hvert 30. minut
  - Hver time
  - Hver 12. time
  - Hver dag

{{-}}

#### Søgesti til slægtsbogen <span id="Family Tree's Media path"></span>

![[_media/EditPreferences-FamilyTree-tab-FamilyTreesMediaPath-section-default-60-da.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menu:  - fanen "Slægtsbog" - sektionen "Søgesti til slægtsbogen"]]

- Her kan du udfylde en basissti til medieobjekterne.

  - Hvis du vælger knappen , får du en dialogboks, hvor du kan udfylde den nødvendige sti.

Se også:

- [](wiki:Gramps_6.0_Wiki_Manual_-_Tools#Media_Manager) en gruppe af fire separate værktøjer, hvoraf to giver dig mulighed for at:
  - 

  - 

{{-}}

##### Vælg mediemappe-dialogboks <span id="Select media directory dialog"></span>

Se [Da:Gramps 6.0 brugsanvisning - Indstillinger#File_Chooser](wiki:Da:Gramps_6.0_brugsanvisning_-_Indstillinger#File_Chooser) {{-}}

##### Manglende medieobjekter 'brudt link' ikon af en boks med et rødt 'x'

![[_media/BrokenMediaPath-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Medieobjekt med en brudt filsti]]

Hvis forhåndsvisningsminiaturebillederne viser et 'brudt link' ikon af en boks med et rødt 'x', skal du rette for din slægtsbog i sektionen .

Se også:

- Example.gramps - [Forbinder til eksemplets medieobjekter](wiki:Example.gramps#Connecting_to_the_example_Media_Objects)
- [Media Verify Tool](wiki:Addon:Media_Verify_Tool) tilføjelsesværktøj til revalidering af mediestier

{{-}}

### Importér <span id="Import"></span>

![[_media/EditPreferences-Import-tab-default-60-da.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menu: "Rediger&gt;Indstillinger" - fanen "Importér"]]

Fanen har to sektioner som følger:

- 

- 

#### Mærkatposter <span id="Tag Records"></span>

-   
  Afkrydsningsfelt (Standard: `Importeret %Y/%m/%d %H:%M:%S` ) **Bemærk - Tilføjelse af et tidsstemplet [mærkat](wiki:Gramps_Glossary/da#tag) ved import kan forsinke importen af ​​dine data betydeligt, men det er nyttigt til den efterfølgende dataoprydning.**

#### Kilde ved GEDCOM import <span id="Source GEDCOM import"></span>

-   
  Dette afkrydsningsfelt påvirker importen af ​​[GEDCOM data](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees#GEDCOM_import). Hvis dette er angivet, vil hvert element, der importeres, indeholde en [Kilde](wiki:Gramps_Glossary/da#source) reference til den importerede fil. **Bemærk - Tilføjelse af en forvalgt kilde kan forsinke importen af ​​dine GEDCOM data betydeligt, men det er nyttigt til den efterfølgende dataoprydning.**

{{-}}

### Grænser <span id="Limits"></span>

![[_media/EditPreferences-Limits-tab-default-60-da.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menu: "Rediger&gt;Indstillinger" - fanen "Grænser"]]

Indstillinger brugt til beregning af datoer, aldre og generationer.

Se også:

- [Gramps 6.0 Wiki Manual - Probably Alive](wiki:Gramps_6.0_Wiki_Manual_-_Probably_Alive)
- [Redigering af datoer](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1#Editing_dates)
- Indstilling af [date approximation .ini](wiki:Match_dates#Changing_after.2Fbefore.2Fabout_range) manuelt

#### Beregningsgrænser <span id="Calculation limits"></span>

- Standard: `50`

  - Definerer antallet af år +/- af begivenhedsdatoen "`omkring `<date>", som begivenheden vil returnere som gyldig for et filter.
  - Bruges i beregningen af ​​personens alder.

- Standard: `50`

  - Definerer antallet af år efter begivenhedsdatoen "`efter `<date>", som begivenheden vil returnere som gyldig for et filter.
  - Bruges i beregningen af ​​personens alder.

<!-- -->

- Standard: `50`

  - Definerer antallet af år før begivenhedsdatoen "`før `<date>", som begivenheden vil returnere som gyldig for et filter.
  - Bruges i beregningen af ​​personens alder.

<!-- -->

- Standard: `110`

  - Uden en dødshændelse, den alder, hvormed bedstefar vil anse personen for ikke længere i live.

- Standard: `20`

- Standard: `13`

- Standard: `20`

- Du kan indtaste antallet af generationer, der bruges til at bestemme relationer. Standardværdien er **`15`**. Begrænser omfanget af funktioner baseret på [Relationsberegner](wiki:Gramps_6.0_Wiki_Manual_-_Tools#Relationship_Calculator).

{{-}}

### Farver <span id="Colors"></span>

![[_media/EditPreferences-Colors-tab-default-60-da.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menu: "Redigér&gt;Indstillinger" - fanen "Faver" standardværdier]]

Denne fane har syv sektioner, der giver dig mulighed for at indstille **farverne, der bruges til bokse i de grafiske visninger**. {{-}}

Hver af farverne kan tilpasses ved hjælp af .

#### Farver brugt til bokse i de grafiske visninger

Du kan vælge

- - **Lyse farver** (standard)
  - *Mørke farver*
    - \- gendanner temaernes standardfarver.

#### Farver for mandlige personer

- \[ \] \#b8cee6

- \[ \] \#1f4986

- \[ \] \#b8cee6

- \[ \] \#000000

#### Farver for kvindelige personer

- \[ \] \#feccf0

- \[ \] \#861f69

- \[ \] \#feccf0

- \[ \] \#000000

#### Farver for personer, der hverken er kvinder eller mænd

- \[ \] \#94ef9e

- \[ \] \#2a5d16

- \[ \] \#94ef9e

- \[ \] \#000000

#### Farver for ukendte personer

- \[ \] \#f3dbb6

- \[ \] \#8e5801

- \[ \] \#f3dbb6

- \[ \] \#000000

#### Farver for Familienoder

- \[ \] \#eeeeee

- \[ \] \#cccccc

- \[ \] \#eeeeee

- \[ \] \#eeeeee

- \[ \] \#eeeeee

- \[ \] \#eeeeee

- \[ \] \#eeeeee

- \[ \] \#ff7373

#### Andre farver

- \[ \] \#bbe68a

{{-}}

### Slægtsforskningssymboler

![[_media/EditPreferences-GenealogicalSymbols-tab-default-60-da.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menu: "Redigér&gt;Indstillinger" - fanen "Slægtforskningssymboler" standardværdier]]

Giver dig mulighed for at bruge genealogiske symboler i stedet for tekstforkortelser i rapporter, diagrammer og Gramps brugergrænseflade.

Denne fane giver dig mulighed for at bruge én skrifttype, der kan vise alle genealogiske symboler. (Når den er konfigureret, se: [Forudsætning for at bruge genealogiske symboler](#Prerequisite_to_use_Genealogical_Symbols))

Hvis du markerer afkrydsningsfeltet "", bruger Gramps den valgte skrifttype, hvis den findes.

Dette kan være nyttigt, hvis du vil tilføje fonetisk information i en note for at vise, hvordan et navn udtales, eller hvis du blander flere sprog som græsk og russisk.

Du kan kun konfigurere dødssymbolet fra denne fane.

  
Liste over viste genealogiske symboler (angivet i rækkefølge vist nederst på skærmbilledet):

- Kvinde
- Mand
- Aseksualitet, kønsløs, kønsløs
- Lesbianisme
- Mandlig homoseksualitet
- Heteroseksualitet
- Transkønnet, hermafrodit (i entomologi)
- Transkønnet
- Kastration

<!-- -->

- Uægteskabelig partner
- Fødsel
- Dåb/Barnedåb
- Forlovet
- Ægteskab
- Skilsmisse
- Ugift partnerskab
- Begravet
- Kremeret/Begravelsesurne
- Dræbt i kamp
- Uddød

<!-- -->

- Død

{{-}}

| Betydning | Symbol | Unicode-værdi | Navn |
|----|----|----|----|
| mand | ♂ | U+2642 | Mandligt tegn |
| kvinde | ♀ | U+2640 | Kvindeligt tegn |
| ukendt | ⚪︎ | U+26AA | Mellem hvid cirkel |
| hermafrodit | ⚥ | U+26A5 | Sammenlåst mandligt og kvindeligt tegn |
| neutral | ⚲ | U+26B2 | Neutral |
| fødsel | \* | U+002A | Asterisk |
| dåb, barnedåb | ~ | U+007E | Tilde |
| død | ✝︎ | U+271D | Latinsk Kors |
| begravelse | ⚰︎ | U+26B0 | Kiste |
| kremering | ⚱︎ | U+26B1 | Begravelsesurne |
| dødfødt | ✝︎\* | U+0086 U+002A | Latinsk Kors, Asterisk |
| født uægte | \*⃝ | U+002A U+20DD | Omkredset Asterisk |
| født uægte | ⊛ | U+229B | Omkredset Asterisk Operator |
| dræbt i kamp | ⚔︎ | U+2694 | Krydsede Sværd |
| denne linje uddød | ‡ | U+2021 | Dobbelt Dolk |
| omtrentlig(lig) | ± | U+00B1 | Plus-Minus |
| før | \< | U+003C | Mindre-end-symbol |
| efter | \> | U+003E | Større-end-symbol |
| forlovet | ⚬ | U+26AC | Mellem Lille Hvid Cirkel |
| gift | ⚭ | U+26AD | Ægteskabssymbol |
| skilt | ⚮ | U+26AE | Skilsmissesymbol |
| ugift | ⚯ | U+26AF | Ugift Partnerskabssymbol |

{{-}}

#### Prerequisite to use Genealogical Symbols <span id="Prerequisite to use Genealogical Symbols"></span>

![[_media/EditPreferences-GenealogicalSymbols-tab-default-51.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Genealogical Symbols" - Preferences tab - defaults]]

##### Initial setup

If the fontconfig [prerequisite has been installed](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Prerequisite), then on the tab select the button, Gramps will attempt to detect any suitable unicode text fonts that can be used.

![[_media/EditPreferences-GenealogicalSymbols-FindFont-51.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Genealogical Symbols" - Finding fonts]]

When the search has completed select one of the fonts from the list and then select the checkbox:

##### Prerequisite

Prerequisite : **python-fontconfig** : Python bindings of fontconfig and its dependencies are required for displaying genealogical symbols

See also:

- Tamura Jones expounds on [Genealogical Symbols](https://www.tamurajones.net/GenealogySymbols.xhtml) *(the 'Unicode' section is particularly relevant)*
- [GEPS 039: Genealogical symbols in gramps](wiki:GEPS_039:_Genealogical_symbols_in_gramps)
- Feature request: Gramps should be able to use genealogy symbols everywhere.
- [Customize the Genealogical Symbols lookup table](wiki:Customize_the_Genealogical_Symbols_lookup_table) located in the [Gramps user directory](wiki:Gramps_6.0_Wiki_Manual_-_User_Directory#MS_Windows) at: [gramps\gen\utils\symbols.py](https://github.com/gramps-project/gramps/blob/maintenance/gramps51/gramps/gen/utils/symbols.py)

{{-}}

### ID-formater <span id="ID Formats"></span>

![[_media/EditPreferences-IDFormats-tab-default-60-da.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menu: "Redigér&gt;Indstillinger" - fanen "ID-formater" - standardværdier]]

Denne fane indeholder præferencer, der er relevante for automatisk generering af Gramps ID'er.

- Angiver skabelonen til generering af ID'er for en person. Standardværdi: `I%04d`

- Angiver skabelonen til generering af ID'er for en familie. Standardværdi: `F%04d`

- Angiver skabelonen til generering af ID'er for et sted. Standardværdi: `P%04d`

- Angiver skabelonen til generering af ID'er for en kilde. Standardværdi: `S%04d`

- Angiver skabelonen til generering af ID'er for en kildehenvisning. Standardværdi: `C%04d`

- Angiver skabelonen til generering af ID'er for et medieobjekt. Standardværdi: `O%04d`

- Angiver skabelonen til generering af ID'er til en begivenhed. Standardværdi: `E%04d`

- Angiver skabelonen til generering af ID'er til et arkiv. Standardværdi: `R%04d`

- Angiver skabelonen til generering af ID'er til en note. Standardværdi: `N%04d`

Du kan bruge værktøjet [Reorder Gramps ID](wiki:Gramps_6.0_Wiki_Manual_-_Tools#Reorder_Gramps_ID) til at ændre formatet. {{-}}

### Tekst <span id="Text"></span>

![[_media/EditPreferences-Text-tab-default-60-da.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menu: "Redigér&gt;Indstillinger" - fanen "Tekst" - standardværdier]]

Denne fane indeholder sektionen med præferencer, der er relevante for, hvordan manglende og private navne og optegnelser vises. {{-}}

#### Betingede teksterstatninger <span id="Conditional Text Replacements"></span>

- I inputfeltet kan du bestemme, hvordan et manglende efternavn skal vises. Standardværdien er **`[Manglende efternavn]`**. Du kan ændre dette til \[--\] eller hvad der passer dig bedst.

<!-- -->

- I inputfeltet kan du bestemme, hvordan et manglende fornavn skal vises. Standardværdien er **`[Manglende fornavn]`**. Du kan ændre dette til hvad du vil.

<!-- -->

- Standard: `[Manglende optegnelse]`

- Standard: `[Nulevende]`

- Standard: `[Nulevende]`

- Standard: `[Privat optegnelse]`

{{-}}

### Advarsler <span id="Warnings"></span>

![[_media/EditPreferences-Warnings-tab-default-60-da.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menu: "Redigér&gt;Indstillinger" - fanen "Advarsler" - standardværdier]]

Denne fane har en sektion , der styrer visningen af ​​advarselsdialoger, hvilket tillader genaktivering af dialoger, der er blevet deaktiveret.

Se siden [Fejl- og advarselsreference](wiki:Gramps_6.0_Wiki_Manual_-_Error_and_Warning_Reference) for eksempler.

#### Advarsler og Fejl dialog <span id="!Warnings and Error dialogs"></span>

- Afkrydsningsfelt er som standard ikke markeret (Se [Dialog](wiki:Gramps_6.0_Wiki_Manual_-_Error_and_Warning_Reference#Suppress_warning_when_adding_parents_to_a_child))

- Afkrydsningsfelt er som standard ikke markeret (Se [Dialog](wiki:Gramps_6.0_Wiki_Manual_-_Error_and_Warning_Reference#Suppress_warning_when_cancelling_with_changed_data))

- Afkrydsningsfelt er som standard ikke markeret (Se [Dialog](wiki:Gramps_6.0_Wiki_Manual_-_Error_and_Warning_Reference#Suppress_warning_about_missing_researcher_when_exporting_to_GEDCOM))

- Afkrydsningsfelt er ikke markeret som standard

- Afkrydsningsfelt er ikke markeret som standard (Se [Dialog](wiki:Gramps_6.0_Wiki_Manual_-_Error_and_Warning_Reference#Module_not_loaded_warnings))

{{-}}

### Slægtsforsker <span id="Researcher"></span>

![[_media/EditPreferences-Researcher-tab-default-60-da.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menu: "Redigér&gt;Indstillinger" - fanen "Slægtsforsker" - standardværdier]]

Giver dig mulighed for at i de tilsvarende tekstfelter. Selvom Gramps anmoder om oplysninger om dig, bruges disse oplysninger kun, så Gramps kan oprette gyldige GEDCOM-outputfiler. En gyldig GEDCOM-fil kræver oplysninger om filens skaber. Hvis du ønsker det, kan du lade oplysningerne stå tomme, men ingen af ​​dine eksporterede GEDCOM-filer vil være gyldige. {{-}} De tilgængelige tekstfelter er (alle tomme som standard):

- 

- 

- 

- 

- 

- 

- 

- 

- 

Oplysningerne, der indtastes under denne præference, fungerer som standardværdi for slægtsbogsspecifikke værdier, der kan justeres med . {{-}}

## Andre indstillinger <span oid="Other settings"></span>

Udover dialogboksen er der andre indstillinger tilgængelige i Gramps. Af forskellige årsager er de blevet gjort mere tilgængelige, som anført nedenfor. {{-}}

### Kolonneeditor <span id="Columns editor"></span>

![[_media/ColumnsEditorTab-dialog-example-60-da.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} fanen <strong>Kolonner</strong> - dialog - Personoversigt]]

Kolonnerne i listevisningerne kan tilføjes, fjernes eller omarrangeres i en editordialog.

For at bruge editordialogen til den aktuelle visning, skal du vælge via menuen, klikke på værktøjslinjens knap ![[_media/Gramps-config.png]] eller trykke på *Konfigurer aktiv oversigt* [tastaturgenveje](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings#Common_keybindings).

Kun kolonner med et markeret afkrydsningsfelt vises i oversigten. Du kan også ændre positionen af ​​en kolonne i oversigten ved at klikke og trække den til en ny position i editoren ([*træk og slip*](https://wikipedia.org/wiki/Drag-and-drop)). Når du har foretaget de ønskede ændringer, skal du klikke på og derefter på for at afslutte editoren og se dine ændringer i oversigten.

Som standard viser oversigten flere kolonner med information om den respektive kategori. Du kan tilføje eller fjerne kolonner til og fra visningen.

Standard sorteringsnøglen for visningen \[altid stigende\] er feltet yderst til venstre \[dvs. øverst i kolonneeditoren\], så ændring af hvilket felt der er på den position påvirker standard sortering. For nogle oversigter kan det første felt ikke ændres, og årsagen vil blive nævnt øverst i kolonneeditoren.

Dialogboksen vil have et forskelligt udvalg af kolonner for hver kategori af oversigt, der viser en simpel tabel.

Ændringer træder kun i kraft, når du klikker på knappen .

Når ændringerne i visningskolonnerne er anvendt, sorteres der i stigende rækkefølge ved at klikke én gang på kolonneoverskriften, og ved at klikke igen sorteres der i faldende rækkefølge.

Delmængden af ​​kolonner og de nuværende [filtre](wiki:Gramps_6.0_Wiki_Manual_-_Filters) vil også begrænse de data, der eksporteres via funktionen. Skjulte kolonner og poster vil ikke blive eksporteret. {{-}}

### Sortering af kolonner <span id="Sorting columns"></span>

![[_media/PersonView-PeopleListView-example-with-context-menu-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} <strong>Før</strong> - standard sortering efter "Navn" kolonne "Personer" Kategori - "Person" (Liste) Visning]]

![[_media/PeopleCategory-PeopleListView-SortedByBirthDateColumn-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} <strong>Efter</strong> - Sorteret efter kolonnen "Fødselsdato" i listetilstanden i personkategorivisningen - eksempel]]

Som standard sorterer hver kategorivisning, der præsenterer data i et kolonneopdelt tabellayout, rækkerne i stigende rækkefølge baseret på dataene i den første (venstre) kolonne. Hvis tabellen har grupperede rækker, vil de grupperede data blive undersorteret. *(Tabeller i fanebladede delmængder af data, editorer og selektorer fungerer på samme måde.)*

Klik én gang på en anden kolonneoverskrift for at sortere dataene i den kolonne i stigende rækkefølge. Klik på overskriften igen for at sortere i omvendt rækkefølge.

Dialogboksen kan bruges til at tilføje, fjerne og omarrangere de viste kolonner. Hvis du vælger en anden første kolonne, bliver den den nye standard sorteringskolonne i visningen \[dog altid stigende\]. {{-}}

### Indstilling af proband <span id="Setting Home person"></span>

![[_media/MenuEdit-SetHomePerson-60-da.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menu der viser <em>Gør til proband</em>]]

For at indstille (udpege) [Proband](wiki:Gramps_Glossary/da#home_person), skal du vælge kategorien Personer og vælge den ønskede person for at tilføje dem til [Aktiv person](wiki:Gramps_Glossary/da#active_person) og derefter vælge via menuerne.

Alternativt, når du redigerer en person, kan du højreklikke på inaktive områder (områder uden en tekstboks) i den øverste sektion for at vise en pop op-menu, der inkluderer en mulighed for at for den profil.

Probanden er den vedvarende udpegede person, der bliver [Aktiv person](wiki:Gramps_Glossary/da#active_person), når et af følgende sker:

- Som standard, når slægtsbogen åbnes  
  *(Indstillingen [General](wiki:Da:Gramps_6.0_brugsanvisning_-_Indstillinger#General_Gramps_settings) i [Indstillinger](wiki:Da:Gramps_6.0_brugsanvisning_-_Indstillinger#Indstillinger) kan ændre denne standardadfærd. "Husk sidst viste visning" vender tilbage til den sidste [Aktiv person](wiki:Gramps_Glossary/da#active_person) fra den forrige session.)*
- Når der klikkes på knappen på værktøjslinjen
- Når menupunktet Hjem vælges fra enten menuen eller højreklik-kontekstmenuen i valgte visninger
- Som [tastaturgenvejen](wiki:Da:Gramps_6.0_brugsanvisning_-_Tastaturgenveje#15) trykkes for at vende tilbage til **Probanden**.

Værktøjslinjens knap ![[_media/Gramps_Go-Home48x48_win.png]] er tilgængelig i kategorierne Personer, Slægtsforhold og Tavler.

#### Se også

- [Indstilling af proband](wiki:Da:Gramps_6.0_brugsanvisning_-_Navigation#Indstilling_af_proband) i kapitlet [Navigation](wiki:Da:Gramps_6.0_brugsanvisning_-_Navigation)

{{-}}

### Justering af visningskontroller <span id="Adjusting viewing controls"></span>

Hvorvidt værktøjslinjen, sidepanelet eller filteret (ikke tilgængeligt i tavle- og slægtsforldsvisninger) vises i hovedvinduet, justeres via menuen Vis.

I de forskellige visninger vil det at klikke på menuen vise bokse, du kan klikke på:

- Navigator
- Værktøjslinje
- Sidepanel
- Bundpanel
- Fuld skærm

Afhængigt af den visning, du er i, vil der desuden være andre muligheder tilgængelige på .

- Gramplets:
  - Sæt kolonner til 1
  - Sæt kolonner til 2
  - Sæt kolonner til 3
- Slægtsforhold:
  - Vis søskende
  - Vis detaljer
  - Geografi:
  - Tidsperiode
  - Layout

Alle andre visninger: [Kolonneeditoren](wiki:Da:Gramps_6.0_brugsanvisning_-_Indstillinger#Kolonneeditor). {{-}}

### Eksportvisning <span id="Export View"></span>

![[_media/Menubar-FamilyTrees-overview-FamilyTree-Loaded-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menulinje - "Slægtstræer" - oversigtseksempel, der viser menupunktet "Eksportvisning"]]

På de fleste [Kategorilistevisninger](wiki:Gramps_6.0_Wiki_Manual_-_Categories#Categories_of_the_Navigator) kan viste data muligvis eksporteres, vælg via kommandoen [menu](wiki:Gramps_6.0_Wiki_Manual_-_Navigation#Main_Menus).

Denne menukommando vises kun, hvis de viste data kan eksporteres. Gramps eksporterer data på skærmen efter dit valg: **CSV** eller **Åbn dokument** regnearksformat.

Bemærk, at den aktuelle konfiguration af visningens kolonner styrer, hvilke data der eksporteres. Eksporten vil kun indeholde de viste kolonnedata (i samme rækkefølge) og være begrænset til poster, der matcher alle de [filtre](wiki:Gramps_6.0_Wiki_Manual_-_Filters), du har anvendt.

Brug fanen Visninger [CSV Dialect](wiki:Gramps_6.0_Wiki_Manual_-_Settings#CSV_Dialect) til at styre typen af ​​CSV, der skal oprettes. {{-}}

#### Eksporter visning som regneark-dialogboks <span id="Export View as Spreadsheet dialog"></span>

![[_media/ExportViewAsSpreadsheet-CSV-file-dialog-example-60.png|Fig. {{#var:kapitel}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Eksporter visning som regneark" CSV(standard) filtype - dialogboks - eksempel]]

Gramps viser derefter dialogboksen , hvor du efter at have valgt en filplacering, hvor filen skal gemmes, og et navn til den, kan eksportere data fra kategorilistevisningen i et af to regnearksformater:

- - **CSV** (standard)
  - **OpenDocument-regneark** - ODS-format.

{{-}} ![[_media/ExportViewAsSpreadsheet-ODS-Displayed-in-LibreOfficeCalc-example-60.png|højre\|mingle\|450px\|Fig. {{#var:kapitel}}.{{#vardefineecho:figure\|{{#expr:{{#var:figure}}+1}}}} Eksempel på ODS-regneark - Vist i LibreOffice Calc]]

Eksempelskærmbilledet viser en eksport til **OpenDocument-regnearket** (ODS-format), der vises som et regneark i LibreOffice Calc.

{{-}}

#### CSV-dialekt <span id="CSV Dialect"></span>

![[_media/CSV-Dialect-Tab-dialog-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Fanen "CSV Dialect" - dialogboks - eksempel]]

Alle listetabelvisninger har en -fane i dialogboksen for menuen . Du kan vælge CSV-formatets afgrænser, der skal bruges, når du eksporterer og importerer data i Gramps.

*Vælg din dialekt* fra:

- 

- 

- 

- - - ',' (standard)
    - ';'
    - ':'
    - '\|'
    - 'tab'

CSV står for **[​​kommaseparerede værdier](https://wikipedia.org/wiki/Comma-separated_values)**. Det er et almindeligt tekstfilformat, der adskiller data i kolonner og rækker for en nem måde at udveksle data på. Oprindeligt var data begrænset ved at blive adskilt i kolonner med faste positioner i `.txt` tekstfiler. Da der var behov for mere fleksibilitet, blev kommaet valgt som afgrænser for at markere kolonnernes grænser, og `.csv` formatet for en tekstfil blev etableret. For at komplicere tingene markerede forskellige operativsystemer deres linjeafslutning og filafslutning med forskellige afslutningskoder.

Da komma var nødvendigt for ofte i selve dataene, blev et `.tsv` filformat (tabulatorsepareret værdi) populært. Da andre afgrænsere begyndte at blive taget i brug, blev CSV synonymt med ethvert tekstformat med afgrænsermarkerede kolonner i stedet for at bruge flere filtypenavne. De var blot forskellige 'dialekter' af "CSV".

[Pythons `csv`-modul](https://docs.python.org/3/library/csv.html) tilbyder adskillige foruddefinerede dialekter for at forenkle læsning og skrivning af CSV-filer. Disse dialekter specificerer regler for parsing og formatering af data. Standarddialekterne inkluderer , og . De følgende afsnit beskriver hver dialekts karakteristika, herunder dens separator, linjeafslutning og citeringsadfærd.

##### Excel-dialekt <span id="Excel Dialect"></span>

Dialekten er designet til at være kompatibel med CSV-filer genereret af Microsoft Excel. Den er egnet til data, der er gemt fra Excel som kommaseparerede værdier. \*Separator:\*\* Komma (`,`\`)

- Linjeafslutning: Vognretur og linjeskift (`\r\n`)
- Citat:
  - Dobbelte anførselstegn (`"`\`) bruges til at omslutte felter, der indeholder separatoren eller andre specialtegn.
  - For at inkludere et dobbelt anførselstegn i et felt i anførselstegn, escapes det ved at fordoble det (f.eks. `""example""`).

##### Excel-tab dialekt <span id="Excel-tab Dialect"></span>

Dialekten ligner \`excel\`-dialekten, men bruger tabulatorer i stedet for kommaer som separator. Dette format ses ofte, når man kopierer celledata fra Excel til OS-udklipsholderen. At indsætte tabulatorseparerede data i [Import Text](wiki:Addon:Import_Text_Gramplet)-tilføjelsesgrammetten er en af ​​de hurtigste måder at udfylde dele af dit træ.

- Separator: Tab (`\t`)
- Linjeafslutning: Vognretur og linjeskift (`\r\n`)
- Citat:
  - Dobbelte anførselstegn (`"`) bruges til at omslutte felter, der indeholder separatoren eller andre specialtegn.
  - For at inkludere et dobbelt anførselstegn i et felt i anførselstegn, escapes det ved at fordoble det (f.eks. `""example""`).

##### Unix-dialekt <span id="Unix Dialect"></span>

Dialekten er designet til brug i Unix-lignende miljøer. Den bruger et linjeskifttegn som linjeafslutning og citerer altid alle felter.

- Separator: Komma (`,`)
- Linjeafslutning: Linjeskift (`\n`)
- Citat:
  - Alle felter er omsluttet af dobbelte anførselstegn (`"`).
  - For at inkludere et dobbelt anførselstegn i et felt i anførselstegn, escapes det ved at fordoble det (f.eks. `""example""`).

##### Se også:

- [CSV: mulighed for at vælge dialekt. \#1314](https://github.com/gramps-project/gramps/pull/1314)

{{-}}

### Modularitet og plugins <span id="Modularity and plugins"></span>

Gramps er designet til udvidelse. Plugin-rammeværket (også kendt som Plug-in, addon, extension) giver en vej til tredjepartsudvikling uden for de normale Gramps-udgivelsesdistributioner.

Dokumentationen for hvert addon vedligeholdes uden for flowet i disse hovedwikikapitler. Grænsefladen og funktionaliteten af ​​softwaren og dokumentationen stemmer muligvis ikke overens med de stilarter, der ses i resten af ​​Gramps... selvom vi opfordrer udviklere til at forsøge at gøre deres tilføjelser så problemfri som muligt.

En kort beskrivelse og et skærmbillede af hvert addon kan findes i afsnittet [Addon List](wiki:6.0_Addons#Addon_List) i wikimanualen. Den separat vedligeholdte dokumentationsside for addonet er linket fra den første kolonne på denne liste.

Se [Plugin Manager](wiki:Gramps_6.0_Wiki_Manual_-_Plugin_Manager) og [Tredjepartstilføjelser](wiki:6.0_Addons). {{-}}

### Tilpas rapportoutputformater <span id="Customize report output formats"></span>

![[_media/TextReports-DocumentOptions-section-PlainText-output-settings-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Dokumentindstillinger - standardfaneblade for tekstrapporter (Almindelig tekst - output valgt) eksempel]]

Hvilken slags outputtilpasning er tilgængelig? Denne dialogboks giver dig mulighed for at ændre skrifttyper, skriftstørrelser, skriftfarve, baggrundsfarve på teksten og justering af afsnit i rapporten.

For de fleste rapportdialogbokse er der i den øverste del faneblade med indstillinger, der specifikt er relateret til den pågældende rapport. Den nederste del vil have mere bredt genanvendelige funktioner og kaldes sektionen .

Fra rullemenuen kan du vælge en eksisterende brugerdefineret stil. Eller for at lave din egen skal du vælge knappen for at vise dialogboksen og derefter vælge knappen for at vise dialogboksen .

{{-}}

#### Dialogboksen Dokumentstile <span id="Document Styles dialog"></span>

![[_media/DocumentStyles-dialog-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Dokumentstile - dialogboks - standard]]

Dialogboksen viser *standard*-stilen og eventuelle brugerdefinerede stile for den pågældende rapport, og giver dig mulighed for at redigere eller slette alle brugerdefinerede stile, du har oprettet. Vælg knappen for at vise dialogboksen . {{-}}

#### Stilredigeringsdialogboks <span id="Style editor dialog"></span>

![[_media/StyleEditor-dialog-Description-tab-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Fanen Beskrivelsesindstillinger - Dokumentstile - dialogboks - standardstile for Ahnentafel-rapport]]

Dialogboksen giver dig mulighed for at tilpasse dokumentstilen specifikt for hver rapport.

Skift feltet `Ny stil` (standard) til et unikt navn, som det vil vises i rullemenuen .

Når ændringerne til din brugerdefinerede stil er færdiggjort, skal du vælge knappen for at gemme ændringerne eller for at afslutte.

##### Faner i dialogboksen Stilredigering <span id="Style editor dialog tabs"></span>

I venstre side ser du kolonnen , der viser de afsnitsindstillinger, der er specifikke for den pågældende rapport, og som du kan ændre. For eksempel viser stilindstillingerne for `AHN-Entry`, `AHN-Generation` og `AHN-Title`.

I højre side er der tre faner, der er knyttet til hver stil, og som er angivet i venstre kolonne:

- [Description](#Description)
- [Skriftindstillinger](#Font_options)
- [Afsnitsindstillinger](#Paragraph_options)

{{-}}

###### Beskrivelse <span id="Description"></span>

![[_media/StyleEditor-dialog-Description-tab-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Fanen Beskrivelsesindstillinger - Dokumentstile - dialogboks - standardstile for Ahnentafel-rapport]]

- Fanen beskriver, hvad hvert afsnit handler om. Her vises eksempelvis den stil, der bruges til Ahnentafel-rapporten ( `AHN-Entry` ) med beskrivelsen: *Den grundlæggende stil, der bruges til tekstvisningen.*

{{-}}

###### Skriftindstillinger <span id="Font options"></span>

![[_media/StyleEditor-dialog-FontOptions-tab-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Fanen "Skriftindstillinger" - dialogboksen "Stilredigering" for "Dokumentstile" (standardstile for Ahnentafel-rapport)]]

- Fanen giver dig mulighed for at indstille *Roman* eller *Swiss*, for skrifttypen i pt.(point), for skrifttypen og nogle som *Fed*, *Kursiv* eller *Understregning*.

{{-}}

###### Afsnitsindstillinger <span id="Paragraph options"></span>

![[_media/StyleEditor-dialog-ParagraphOptions-tab-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Fanen "Afsnitsindstillinger" - dialogboksen "Stilredigering" for "Dokumentstile" (standardstile for Ahnentafel-rapport)]]

- Fanen giver dig mulighed for at indstille , , , og for din stil.

{{-}}

### Kontekstmenu <span id="Context menu"></span>

![[_media/Clipboard-dialog-example-context-menu-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Udklipsholder - med eksempel på kontekstmenu ved højreklik på en stedsangivelse]] [Pop-up-menuer](wiki:Da:Gramps_6.0_brugsanvisning_-_Hovedvindue#Pop-up_menuer) bruges forskellige steder i Gramps; hvordan du får adgang til kontekstmenuen afhænger af dine operativsystemer:

- I Microsoft Windows bruger du generelt højre museknap til at vise kontekstmenuen eller bruger tastaturgenvejen +. Se [Brug af kontekstmenuer - Microsoft Docs](https://docs.microsoft.com/en-us/previous-versions/windows/desktop/mpc/using-context-menus)
- På Apple macOS trykker du generelt på , mens du klikker på museknappen for at vise kontekstmenuen. Se: [Kontekstmenuer - Menuer - macOS - Retningslinjer for menneskelig grænseflade - Apple Developer](https://developer.apple.com/design/human-interface-guidelines/macos/menus/contextual-menus/)

Liste over kendte kontekstmenuer i Gramps:

- Kontekstmenuer til stamtavlevisning
- Kontekstmenu til udklipsholder
- Filvælger - Kontekstmenuindstillinger
- Kontekstmenuer til <Kategorivisning>
- Dialogboksen Administrer bøger
- ... og mange flere

Se også:

- [Tastaturgenveje](wiki:Da:Gramps_6.0_brugsanvisning_-_Tastaturgenveje)

{{-}}

### Vælgerdialoger <span id="Selector dialogs"></span>

![[_media/wiki:Da:Gramps_6.0_brugsanvisning_-_Kategorier#Select_Family_selector|[_media/SelectFamily-SelectorDialog-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} [Vælg familie-vælger]] - viser søgelinje]]

Vælgerdialoger er en kombinationsgrænsefladeboks, og du bruger dem generelt til at vælge et objekt (Person/Familie/Begivenheder osv.). Diverse har også søgefelter:

- [Vælg familievælger](wiki:Gramps_6.0_Wiki_Manual_-_Categories#Select_Family_selector)
- [Vælg begivenhedsvælger](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1#Select_Event_selector)
- [Vælg notevælger](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1#Select_Note_selector)
- [Vælg person vælger](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1#Select_Person_selector)
- [Vælg en person til rapportvælgeren](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_4#Vælg_en_person_til_rapportvælgeren)
- [Vælg Far-vælger](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1#Vælg_Father_selector) (filtreret til Far)
- [Vælg Mor-vælger](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1#Vælg_Mother_selector) (filtreret til Mor)
- [Vælg Barn-vælger](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1#Vælg_Barn-selector)
- [Vælg medieobjektvælger](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1#Select_Media_Object_selector)
- [Vælg stedvælger](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_2#Select_Place_selector)
- [Vælg arkivvælger](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_2#Select_Repository_selector)
- [Vælg kilde- eller citatvælger](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_2#Select_Source_or_Citation_selector)
- [Vælg kildevælger](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_2#Select_Source_selector)

{{-}} Se også

- [GEPS_041:\_New_Selector](https://gramps-project.org/wiki/index.php/GEPS_041:_New_Selector)
- [Vælg en farvevælger](wiki:Da:Gramps_6.0_brugsanvisning_-_Indstillinger#Vælg_en_farvevælger)

## Tilpasning <span id="Customizing"></span>

Her er nogle måder, du kan tilpasse Gramps på.

### Indstillinger af navneformat <span id="Preferences"></span>

I afsnittet "Visningsvalg" under fanen Rediger\>Indstillinger kan du vælge det navneformat, der bruges som standard i hele Gramps. Knappen Rediger for åbner , hvilket giver mulighed for at oprette brugerdefinerede (brugerdefinerede) stilarter ud over de foruddefinerede (indbyggede) navneformatvalg.

Se [Indstillinger](wiki:Da:Gramps_6.0_brugsanvisning_-_Indstillinger#Indstillinger)

Knappen Rediger for en persons foretrukne og alternative navne åbner , der giver mulighed for at vælge undtagelser for navneformat, der tilsidesætter det format, der er valgt i fanen Vis i Indstillinger for hele træet.

Navneformatet, grupperingen og sorteringen kan tilsidesættes for valgte individer og efternavne. Dialogboksene Rediger person har to Rediger-knapper til at få adgang til denne funktion. Knappen for Foretrukket navn er til højre for feltet Suffiks. For ethvert valgt navn (Foretrukket eller Alternativt) i fanen Navne, der åbner Navneeditoren, kan de indbyggede og brugerdefinerede visningsnavneformater vælges som undtagelser til indstillingerne "Gruppér som:" og "Sorter som:", der som standard bruger det navneformat, der er valgt i Indstillinger.

### Vælg en farvevælger

Fanen [Farver](wiki:Da:Gramps_6.0_brugsanvisning_-_Indstillinger#Farver) i Indstillingerne giver mulighed for at tilpasse farven på forskellige elementer i diagrammer i de grafiske visninger i kategorien Diagrammer.

#### Farvepalet <span id="Color Palette"></span>

![højre\|thumb\|450px\|Fig. {{#var:kapitel}}.{{#vardefineecho:figure\|{{#expr:{{#var:figure}}+1}}}} "Vælg en farve" - ​​paletvælgerdialog](PickAColor-selector-dialog-52.png "højre|thumb|450px|Fig. {{#var:kapitel}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Vælg en farve" - ​​paletvælgerdialog") Vælg en farve fra de 45 [farveprøver](wiki:Gramps_Glossary/da#swatch) i det foruddefinerede farvepaletområde. Eller vælg fra de senest brugte farveprøver. Eller klik på knappen for at oprette din egen brugerdefinerede farve. Højreklik på en hvilken som helst farveprøve for at tilføje en anden brugerdefineret farve og åbne gradientvælgeren.

Du kan trække en hvilken som helst farveprøve til en hvilken som helst farveprøve i præference- (eller konfigurations-) dialogboksen.

{{-}}

#### Farvegradient <span id="Color Gradient"></span>

![højre\|thumb\|436px\|Fig. {{#var:chapter}}.{{#vardefineecho:figure\|{{#expr:{{#var:figure}}+1}}}} "Vælg en farve" - ​​dialogboks til gradientvælger](PickAColor-gradient-dialog-52.png "højre|thumb|436px|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Vælg en farve" - ​​dialogboks til gradientvælger") Dialogboksen til gradientvælger bruges til at justere [farveprøven](wiki:Gramps_Glossary/da#swatch) øverst i dialogboksen. Når den er ændret, skal du enten klikke på knappen for at anvende farven. Træk den enkelte gradientdialogboksprøve til en hvilken som helst farveprøve i præference- (eller konfigurations-) dialogboksen.

Specifikke farver i farveprøven kan ændres på flere måder:

- via direkte indtastning 'farve hexagonal farvekode'
- farvetone-skyderen (med en numerisk finkontrol
- venstreklik med musen i den 1-dimensionelle (farvetone) regnbuegradient eller den 2-dimensionelle (lysstyrke og mætning) farvetonegradient.
- højreklik med musen i en af ​​gradienterne for at vise den numeriske kontrol for gradientens dimension(er)
- venstreklik med musen på pipettens farvevælger for at vælge fra enhver pixel, der vises på skærmen(e)

{{-}}

### Filvælger <span id="File Chooser"></span>

![[_media/FileChooser_Bookmarks_Breadcrumbs.png|højre\|tommelfinger\|400px\|Fig. {{#var:chapter}}.{{#vardefineecho:figure\|{{#expr:{{#var:figure}}+1}}}} Linux GTK Filvælger: fremhævning af brødkrummer og bogmærkning]] ![[_media/FileChooser_Bookmarks_Breadcrumbs_mac.png|højre\|tommelfinger\|400px\|Fig. {{#var:chapter}}.{{#vardefineecho:figure\|{{#expr:{{#var:figure}}+1}}}} macOS GTK Filvælger: fremhævning af brødkrummer og bogmærkning]] ![[_media/FileChooser_Bookmarks_Breadcrumbs_win.png|højre\|tommelfinger\|400px\|Fig. {{#var:kapitel}}.{{#vardefineecho:figure\|{{#expr:{{#var:figure}}+1}}}} Windows GTK Filvælger: fremhævning af brødkrummer og bogmærkning]] Dialogboksene Åbn og Gem (Filvælger) til Gramps er baseret på [GTK Filvælger](https://docs.gtk.org/gtk3/iface.FileChooser.html). Hvert operativsystem har forventede adfærdsmønstre for klik, dobbeltklik, sortering, [tastebindinger](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings#Handy_Shortcuts), miljøvariabler og standardfilplaceringer, der er karakteristiske for Filvælger-dialogbokse, der er native til operativsystemet. Nogle af disse kan tilpasses via brugergrænsefladen, så de ligner mere de operativsystem-native Filvælgere. Imidlertid betyder de forskellige operativsystemers særpræg, at delte netværksmapper og URI-understøttelse muligvis ikke er lige så lette at gennemse, som når man bruger de operativsystem-native Filvælgere.

[GtkFileChooser](https://developer-old.gnome.org/gtk4/stable/GtkFileChooser.html) giver mulighed for at tilføje hurtige navigationslinks til almindeligt anvendte steder i filsystemet. I standardimplementeringen vises disse i navigationsruden i venstre sidepanel. Det kan være lidt uklart i starten, at disse genveje kommer fra forskellige kilder og i forskellige varianter, så lad os forklare terminologien her:

- **[Bogmærker](#Bookmarking_file_folders)**: oprettes af brugeren ved at trække mapper fra højre rude til venstre rude eller ved at bruge "Tilføj". Bogmærker kan omdøbes og slettes af brugeren.
- **Genveje**: kan leveres af Gramps-applikationen. For eksempel kan programmet ønske at tilføje en genvej til en mappe med downloads eller dokumenter. Genveje *kan ikke* tilføjes eller fjernes af brugeren. Kontekstmenuen 'Omdøb...' giver mulighed for at omdøbe dem.
- **Volumener**: leveres af den underliggende filsystemabstraktion. De er filsystemets "rødder". Hjemmeside- og Downloads-hotlinks er almindelige "rødder". Volumener kan ikke ændres af brugeren.

#### Kontekstmenuer for Filvælger <span id="File Chooser context menus"></span>

Højreklik på en hvilken som helst fil eller mappe i den aktuelle mappe for at åbne en kontekstmenu med følgende muligheder:

<hr>

- 

<hr>

- 

- 

<hr>

- 

- 

- 

- 

- 

<hr>

Højreklik i navigationssidelinjen for at åbne en kontekstmenu med følgende muligheder:

<hr>

- 

- 

- 

<hr>

#### Breadcrumbs og tekstindtastningsadresselinje <span id="Breadcrumbs and text-entry address bar"></span>

Som standard er filmappe-navigationen i Filvælgeren ved at browse. Der er også nogle genveje til venstre og breadcrumbs (fremhævet med grønt i dialogboksillustrationen) til hurtig navigation op og ned ad stien. Eventuelt kan en tekstindtastningsadresselinje bruges til direkte at indtaste eller indsætte en sti. Skift mellem at vise breadcrumbs og tekstindtastningsadresselinjen med [tastaturgenvej](wiki:Da:Gramps_6.0_brugsanvisning_-_Tastaturgenveje).

#### Bogmærkning af filmapper <span id="Bookmarking file folders"></span>

Bogmærker til filmapper kan brugerdefineres for at gøre det nemmere at finde standardplaceringer. Disse bogmærker huskes mellem sessioner og uanset hvilket Family Tree der er blevet indlæst.

Med en hvilken som helst Åbn- eller Gem-dialogboks åben, naviger til den filplacering, der indeholder den mappe, der skal bogmærkes. Opret bogmærket ved enten at: trække mappeikonet til navigationskolonnen til venstre; eller højreklikke på den mappe for at bruge kontekstmenuen .

Højreklik på et eksisterende bogmærke giver mulighed for at omdøbe eller fjerne bogmærket.

#### Filformater <span id="File Formats"></span>

Understøttelse af flere filformater er indbygget i standarddistributionen af ​​Gramps. Import plugin og Export Plugin Addons kan installeres via Plugin Manager eller Indstillinger for at udvide mulighederne.

Se artiklen [Output Format](wiki:Output_formats) for en liste over filformater.

#### Se også

- [Sådan viser du adresselinjen til tekstindtastning eller "Breadcrumbs" (navigationsknapper)](https://ubuntugenius.wordpress.com/2010/05/14/how-to-show-text-entry-address-bar-or-breadcrumbs-navigation-buttons-in-nautilus-after-ubuntu-10-04-upgrade/) i Nautilus efter Ubuntu 10.04-opgradering

<!-- -->

- Diskussioner om GTK-filvælgeren:
  - [Dokumentation af filvælgeren i wikien](https://gramps.discourse.group/t/need-suggestions-for-documenting-the-gtk-file-chooser/1820/8)
  - [Illustration af filvælgeren i wikien](https://gramps.discourse.group/t/macos-and-windows-gtk-file-chooser-dialog-capture-request/3364)
  - [Filvælger: Sortering af filer og mapper](https://gramps.discourse.group/t/can-i-cause-folders-to-sort-to-the-top-of-the-list-when-presented-with-the-folder-contents/1708/14)

### Sprog <span id="Language"></span>

Gramps er blevet oversat til en række [sprog](wiki:Portal:Translators). Normalt starter Gramps automatisk på dit lokale sprog, som det er valgt til andre applikationer, men nogle gange er dette måske ikke det rigtige for dig. Og i andre tilfælde vil et modul eller et tilføjelsesprogram endnu ikke være blevet oversat, og en advarselsdialog vises, der siger noget i retning af "Advarsel: plugin XYZ har ingen oversættelse til nogen af ​​dine konfigurerede sprog, bruger i stedet amerikansk engelsk". (Bemærk, at den amerikanske dialekt af engelsk er standard i stedet for britisk.) Dette kan blive irriterende eller påtrængende.

Den mest idealistiske situation er, at du er lige så flydende i amerikansk engelsk som det sprog, der er valgt til operativsystemets brugergrænseflade på din computer. Og at du ville benytte lejligheden til at oversætte Gramps-funktionen til brugere, der ikke taler engelsk.

Hvis dit system er konfigureret til at vise et andet sprog end engelsk, kan du tilsidesætte dette for Gramps.

Antag som et eksempel, at en computer i Holland er konfigureret til standard Unicode 8 hollandsk: "LANG: nl_NL.UTF-8". Du kan enten nulstille operativsystemets sprog

I Windows skal du bruge SET-kommandoen til at ændre LANG-miljøvariablen til "en_GB.UTF-8" for britisk engelsk. Du kan gøre dette fra kommandolinjegrænsefladen eller [oprette en opstartsgenvej med følgende Target](https://gramps-project.org/bugs/view.php?id=11009): `C:\Windows\System32\cmd.exe /c "SET LANG=en_GB.UTF-8 && START /D ^"C:\Program Files\GrampsAIO64-6.0.5^" gramps.exe"`

'''

#### Linux

Hvis du vil vælge en lokal 'variant' til sortering, der ikke er standardvarianten, kan du starte Gramps fra terminalen (eller konsollen) med et andet LC_COLLATE-miljø. For eksempel er standard sorterings- (kollations-) varianten for svensk "reformed", men du kan i stedet vælge "standard" ved at skrive: export LC_COLLATE="sv_SE.UTF-8@collation=standard" python Gramps.py

#### macOS

For macOS, se [Avanceret opsætning](wiki:Mac_OS_X:Application_package#Advanced_setup) for detaljer om, hvordan sproget normalt vælges, og hvordan man vælger en særlig, ikke-standardindstilling for sproget, sorteringsrækkefølgen eller formatet for ting som dag- og månedsnavne og talseparatorer.

#### MS Windows

![[_media/MicrosoftWindowGrampsAIO-Installer-ChooseComponents-Selection-example-60.png|Fig. {{#var:kapitel}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Gramps 6.0.3 AIO 64 bit til Microsoft Windows-installationsprogram - &quot;Vælg komponenter&quot;-siden viser valg af &quot;de&quot; (tysk) oversættelse]] Hvis du vil køre Gramps på et andet sprog end engelsk ved hjælp af Gramps AIO-installationsprogrammet, skal du vælge det under installationsprocessen.

Ellers vil det ikke være tilgængeligt.

Mere information kan findes på siden [Installing_Gramps_for_Windows_computers#Missing_other_languages](wiki:Installing_Gramps_for_Windows_computers#Missing_other_languages).

{{-}}

### Tilføj Windows OS-menuelement <span id="Add Windows OS Menu Item"></span>

![[_media/Edit-Target-GrampsAIO64-Properties-Danish-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Edit-Target-GrampsAIO64-Properties for eksempel på dansk genvej.]]

For at få Gramps til at fungere på dit valgte sprog (se tabellen nedenfor for din [sprogkode](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Language_codes)), skal du gøre følgende:

- Brug musens højreknap til at klikke på ikonet "" på skrivebordet, og vælg fra menuen: .
- Højreklik et vilkårligt sted på skrivebordet, og vælg i menuen:
- Et nyt ikon oprettes med navnet: ""
- Højreklik på det, og vælg i menuen:
- Et nyt vindue åbnes. Klik på den første fane kaldet , og skift tekst fra "" til noget mere beskrivende, som f.eks.: ""
  - Klik på den anden fane kaldet , skift tekst i den første post kaldet fra (bemærk, at stien varierer afhængigt af den anvendte Gramps-version):
    - `"C:\Program Files\GrampsAIO64-6.x.x\grampsw.exe"` til:
    - `%comspec% /c set LANG=da_DK.UTF-8 && start grampsw.exe"`
- Klik på

Når du klikker på ikonet, starter Gramps på dansk.

{{-}} {{-}}

### Skift Windows LANG-variablerne <span id="Change the windows LANG variables"></span>

En anden mulighed, hvis du vil have Gramps altid til at indlæses, f.eks. i fransk-canadisk sprog, er at gå til Windows \> Systemegenskaber og tilføje LANG-variablen i brugersektionen i dialogboksen for miljøvariabler med den relevante værdi.

Værdien, der skal tilføjes, er (for fransk canadisk):

    Navn: LANG
    Værdi: fr_CA.UTF-8

- [Sådan indstiller du miljøvariabler i Microsoft Windows](https://fullscale.io/blog/how-to-set-the-windows-path/)

### Sprogkoder <span id="Language codes"></span>

Vælg fra denne tabel over [sprog](wiki:Portal:Translators), som Gramps er blevet oversat til:

| Language | ISO code | Example | Notes |
|----|----|----|----|
| Afrikaans | af_ZA.UTF-8 |  |  |
| Albanian | sq_AL.UTF-8 | %comspec% /c set LANG=sq_AL.UTF-8 && start grampsw.exe" |  |
| Arabic (Saudi Arabia) | ar_SA.UTF-8 | %comspec% /c set LANG=ar_SA.UTF-8 && start grampsw.exe" |  |
| Chinese (Simplified) | zh_CN.UTF-8 | %comspec% /c set LANG=zh_CN.UTF-8 && start grampsw.exe" |  |
| Chinese (Hong Kong) | zh_HK.UTF-8 ??? |  |  |
| Chinese (Traditional) | zh_TW.UTF-8 | %comspec% /c set LANG=zh_TW.UTF-8 && start grampsw.exe" |  |
| Danish | da_DK.UTF-8 | %comspec% /c set LANG=da_DK.UTF-8 && start grampsw.exe" |  |
| Dutch | nl_BE.UTF-8 | %comspec% /c set LANG=nl_BE.UTF-8 && start grampsw.exe" |  |
| English-USA (Default) | en_US.UTF-8 | %comspec% /c set LANG=en_US.UTF-8 && start grampsw.exe" |  |
| English (British) | en_GB.UTF-8 | %comspec% /c set LANG=en_GB.UTF-8 && start grampsw.exe" |  |
| Esperanto | eo.UTF-8 ??? |  |  |
| Finnish | fi.UTF-8 | %comspec% /c set LANG=fi.UTF-8 && start grampsw.exe" |  |
| French | fr_FR.UTF-8 | %comspec% /c set LANG=fr_FR.UTF-8 && start grampsw.exe" |  |
| French Canadian | fr_CA.UTF-8 | %comspec% /c set LANG=fr_CA.UTF-8 && start grampsw.exe" |  |
| German | de_DE.UTF-8 | %comspec% /c set LANG=de_DE.UTF-8 && start grampsw.exe" |  |
| Greek | el_GR.UTF-8 | %comspec% /c set LANG=el_GR.UTF-8 && start grampsw.exe" |  |
| Hebrew | he_IL.UTF-8 | %comspec% /c set LANG=he_IL.UTF-8 && start grampsw.exe" |  |
| Italian | it_IT.UTF-8 | %comspec% /c set LANG=it_IT.UTF-8 && start grampsw.exe" |  |
| Japanese | ja_JP.UTF-8 | %comspec% /c set LANG=ja_JP.UTF-8 && start grampsw.exe" |  |
| Macedonian | mk_MK.UTF-8 ??? |  |  |
| Nederlands (Dutch) | nl_NL.UTF-8 | %comspec% /c set LANG=nl_NL.UTF-8 && start grampsw.exe" |  |
| Norwegian Bokmål | nb_NO.UTF-8 | %comspec% /c set LANG=nb_NO.UTF-8 && start grampsw.exe" |  |
| Norwegian Nynorsk | nn_NO.UTF-8 | %comspec% /c set LANG=nn_NO.UTF-8 && start grampsw.exe" |  |
| Polish | pl_PL.UTF-8 | %comspec% /c set LANG=pl_PL.UTF-8 && start grampsw.exe" |  |
| Portuguese | pt_PT.UTF-8 | %comspec% /c set LANG=pt_PT.UTF-8 && start grampsw.exe" |  |
| Portuguese (Brazil) | pt_BR.UTF-8 | %comspec% /c set LANG=pt_BR.UTF-8 && start grampsw.exe" |  |
| Russian | ru_RU.UTF-8 | %comspec% /c set LANG=ru_RU.UTF-8 && start grampsw.exe" |  |
| Slovak | sk_SK.UTF-8 | %comspec% /c set LANG=sk_SK.UTF-8 && start grampsw.exe" |  |
| Slovenian | sl_SI.UTF-8 | %comspec% /c set LANG=sl_SI.UTF-8 && start grampsw.exe" |  |
| Spanish | es_ES.UTF-8 | %comspec% /c set LANG=es_ES.UTF-8 && start grampsw.exe" |  |
| Turkish | tr_TR.UTF-8 | %comspec% /c set LANG=tr_TR.UTF-8 && start grampsw.exe" |  |
| Ukrainian | uk_UA.UTF-8 | %comspec% /c set LANG=uk_UA.UTF-8 && start grampsw.exe" |  |
|  |  |  |  |
|  |  |  |  |

- Sprogkoderne er ISO-sprogkoder med to små bogstaver (f.eks. "da") som defineret af [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes).
- Landekoderne er ISO-landekoder med to store bogstaver (f.eks. "DK") som defineret af [ISO 3166-1](https://en.wikipedia.org/wiki/ISO_3166-1).

### Avanceret ændring af indstillinger <span id="Advanced manipulation of settings"></span>

Udover de indstillinger, der er tilgængelige i Indstillinger, kan du også udforske de avancerede indstillinger.

Gramps bruger **[INI keys](https://en.wikipedia.org/wiki/INI_file#Keys_(properties))** og [INI sections](https://en.wikipedia.org/wiki/INI_file#Sections) til at administrere brugerpræferencer og programindstillinger. Disse gemmes i tekstfilen `gramps.ini` under mappen `.gramps/gramps[XX]` i din hjemme- eller brugermappe.

Filen `gramps.ini` har følgende afsnit:

- \[behavior\] : typiske nøglenavne er: [betawarn](https://github.com/gramps-project/gramps/blob/master/gramps/gui/grampsgui.py#L502), enable-autobackup, use-tips...
- \[colors\] :
- \[csv\] :
- \[database\] : relateret til databaseindstillinger for stamtræet.
- \[export\] : eksporter og importer mapper/kataloger
- \[geography\] :
- \[interface\] : mange nøgler vedrørende højde og bredde af de forskellige visninger: f.eks. event-height: 450, event-ref-height: 585, event-ref-width: 728, event-width: 712...
- \[paths\] : nøgler relateret til nyligt importerede filer og mapper/kataloger
- \[plugin\] :
- \[preferences\] : nøgler relateret til præferencer: alle de almindelige præfikser , todo -colors..
- \[researcher\] : alle oplysninger om forskeren
- \[spacing\] :
- \[test\] :
- \[utf8\] :

#### Eksempel på `gramps.ini` fil

Eksempel på indhold af `gramps.ini` filen:

    ;; Gramps key file
    ;; Automatically created at 2025/05/24 08:49:41

    [behavior]
    ;;addmedia-image-dir=''
    ;;addmedia-relative-path=0
    ;;addons-allow-install=0
    ;;addons-projects=[['Gramps', 'https://raw.githubusercontent.com/gramps-project/addons/master/gramps60', True]]
    ;;addons-url='https://raw.githubusercontent.com/gramps-project/addons/master/gramps60'
    ;;autoload=0
    ;;avg-generation-gap=20
    ;;check-for-addon-update-types=['new']
    ;;check-for-addon-updates=0
    ;;date-about-range=50
    ;;date-after-range=50
    ;;date-before-range=50
    ;;do-not-show-previously-seen-addon-updates=1
    ;;generation-depth=15
    ;;immediate-warn=0
    ;;last-check-for-addon-updates='1970/01/01'
    ;;max-age-prob-alive=110
    ;;max-sib-age-diff=20
    ;;min-generation-years=13
    ;;owner-warn=0
    ;;pop-plugin-status=0
    ;;previously-seen-addon-updates=[]
    ;;recent-export-type=3
    ;;runcheck=0
    ;;spellcheck=0
    ;;startup=0
    ;;surname-guessing=0
    translator-needed=0
    ;;use-tips=1
    ;;web-search-url='https://google.com/search?q=%(text)s'
    ;;welcome=100

    [colors]
    ;;border-family=['#cccccc', '#252525']
    ;;border-family-divorced=['#ff7373', '#720b0b']
    ;;border-female-alive=['#861f69', '#261111']
    ;;border-female-dead=['#000000', '#000000']
    ;;border-male-alive=['#1f4986', '#171d26']
    ;;border-male-dead=['#000000', '#000000']
    ;;border-other-alive=['#2a5f16', '#26a269']
    ;;border-other-dead=['#000000', '#000000']
    ;;border-unknown-alive=['#8e5801', '#8e5801']
    ;;border-unknown-dead=['#000000', '#000000']
    ;;family=['#eeeeee', '#454545']
    ;;family-civil-union=['#eeeeee', '#454545']
    ;;family-divorced=['#ffdede', '#5c3636']
    ;;family-married=['#eeeeee', '#454545']
    ;;family-unknown=['#eeeeee', '#454545']
    ;;family-unmarried=['#eeeeee', '#454545']
    ;;female-alive=['#feccf0', '#62242D']
    ;;female-dead=['#feccf0', '#3a292b']
    ;;home-person=['#bbe68a', '#304918']
    ;;male-alive=['#b8cee6', '#1f344a']
    ;;male-dead=['#b8cee6', '#2d3039']
    ;;other-alive=['#94ef9e', '#285b27']
    ;;other-dead=['#94ef9e', '#062304']
    ;;scheme=0
    ;;unknown-alive=['#f3dbb6', '#75507B']
    ;;unknown-dead=['#f3dbb6', '#35103b']

    [csv]
    ;;delimiter=','
    ;;dialect='excel'

    [database]
    ;;autobackup=0
    ;;backend='sqlite'
    ;;backup-on-exit=1
    ;;backup-path='C:\\Users\\[username]'
    ;;compress-backup=1
    ;;host=''
    ;;path='C:\\Users\\[username]\\AppData\\Roaming\\gramps\\grampsdb'
    ;;port=''

    [export]
    ;;proxy-order=[['privacy', 0], ['living', 0], ['person', 0], ['note', 0], ['reference', 0]]

    [geography]
    ;;center-lat=0.0
    ;;center-lon=0.0
    ;;lock=0
    ;;map_service=1
    ;;path=''
    ;;personal-map=''
    ;;show_cross=0
    ;;use-keypad=1
    ;;zoom=0
    ;;zoom_when_center=12

    [interface]
    dbmanager-height=370
    ;;dbmanager-horiz-position=12
    ;;dbmanager-vert-position=85
    ;;dbmanager-width=780
    ;;dont-ask=0
    ;;filter=0
    ;;fullscreen=0
    ;;grampletbar-close=1
    ;;hide-lds=0
    ;;ignore-gexiv2=0
    ;;ignore-osmgpsmap=0
    ;;ignore-pil=0
    ;;main-window-height=500
    ;;main-window-horiz-position=15
    ;;main-window-vert-position=10
    ;;main-window-width=775
    ;;mapservice='OpenStreetMap'
    ;;open-with-default-viewer=0
    ;;pedview-layout=0
    ;;pedview-show-images=1
    ;;pedview-show-marriage=0
    ;;pedview-show-unknown-people=0
    ;;pedview-tree-direction=2
    ;;pedview-tree-size=5
    ;;place-name-height=100
    ;;place-name-width=450
    ;;sidebar-text=1
    ;;size-checked=0
    ;;statusbar=1
    ;;surname-box-height=150
    ;;tipofday-height=350
    tipofday-horiz-position=-49
    tipofday-vert-position=84
    ;;tipofday-width=550
    ;;toolbar-addons=1
    ;;toolbar-clipboard=1
    ;;toolbar-on=1
    ;;toolbar-preference=1
    ;;toolbar-reports=1
    ;;toolbar-style=0
    ;;toolbar-tools=1
    ;;treemodel-cache-size=1000
    ;;view=1
    ;;view-categories=['Dashboard', 'People', 'Relationships', 'Families', 'Ancestry', 'Events', 'Places', 'Geography', 'Sources', 'Citations', 'Repositories', 'Media', 'Notes']

    [paths]
    ;;quick-backup-directory='C:\\Users\\[username]'
    ;;quick-backup-filename='%(filename)s_%(year)d-%(month)02d-%(day)02d.%(extension)s'
    ;;recent-export-dir='C:\\Users\\[username]'
    ;;recent-file=''
    ;;recent-import-dir='C:\\Users\\[username]'
    ;;report-directory='C:\\Users\\[username]'
    ;;website-cal-uri=''
    ;;website-cms-uri=''
    ;;website-directory='C:\\Users\\[username]'
    ;;website-extra-page-name=''
    ;;website-extra-page-uri=''

    [plugin]
    ;;addonplugins=[]
    ;;hiddenplugins=[]

    [preferences]
    ;;age-after-death=1
    ;;age-display-precision=1
    ;;age-rounded-year=1
    ;;calendar-format-input=0
    ;;calendar-format-report=0
    ;;cite-plugin='cite-legacy'
    ;;coord-format=0
    ;;cprefix='C%04d'
    ;;date-format=0
    ;;default-source=0
    ;;eprefix='E%04d'
    ;;family-relation-type=3
    ;;family-warn=0
    ;;february-29=0
    ;;fprefix='F%04d'
    ;;hide-ep-msg=0
    ;;invalid-date-format='<b>%s</b>'
    ;;iprefix='I%04d'
    last-view='dashboardview'
    last-views=['dashboardview', '', '', '', '', '', '', '', '', '', '', '', '']
    ;;name-format=1
    ;;no-given-text='[Missing Given Name]'
    ;;no-record-text='[Missing Record]'
    ;;no-surname-text='[Missing Surname]'
    ;;nprefix='N%04d'
    ;;online-maps=0
    ;;oprefix='O%04d'
    ;;paper-metric=0
    ;;paper-preference='Letter'
    ;;patronimic-surname=0
    ;;place-auto=1
    ;;place-format=0
    ;;pprefix='P%04d'
    ;;private-given-text='[Living]'
    ;;private-record-text='[Private Record]'
    ;;private-surname-text='[Living]'
    ;;quick-backup-include-mode=0
    ;;rprefix='R%04d'
    ;;sprefix='S%04d'
    ;;tag-on-import=0
    ;;tag-on-import-format='Imported %Y/%m/%d %H:%M:%S'
    ;;use-last-view=0

    [researcher]
    ;;researcher-addr=''
    ;;researcher-city=''
    ;;researcher-country=''
    ;;researcher-email=''
    ;;researcher-locality=''
    ;;researcher-name=''
    ;;researcher-phone=''
    ;;researcher-postal=''
    ;;researcher-state=''

    [spacing]
    dbman=[22.605613425925927, 5.877459490740741, 9.856047453703704]

    [test]
    ;;january='January'

    [utf8]
    ;;baptism-symbol='~'
    ;;birth-symbol='*'
    ;;buried-symbol='[]'
    ;;cremated-symbol='⚱'
    ;;dead-symbol='✝'
    ;;death-symbol=2
    ;;divorce-symbol='o|o'
    ;;engaged-symbol='o'
    ;;in-use=0
    ;;killed-symbol='x'
    ;;marriage-symbol='oo'
    ;;partner-symbol='o-o'
    ;;selected-font=''

#### Avanceret indstilling af backup-filnavn <span id="Advanced backup filename setting"></span>

Du kan også definere navngivningsmønsteret for backup-filnavnet ved at indstille *`paths.quick-backup-filename`* i `~/.gramps/gramps60/gramps.ini` nøglefilen som følger: {{-}} \[paths\]

;quick-backup-filename='%(filename)s\_%(year)d-%(month)02d-%(day)02d.%(extension)s'  

ved at fjerne de to semikolon(`;;`) fra starten af ​​INI-nøglelinjen og bruge et af følgende nøgleord til filnavnemønsteret:

- filename
- year
- month
- day
- hour
- minutes
- extension :
  - **.gpkg**(standard) hvis du inkluderer medier.
  - *.gramps* hvis du udelukker medier.

Brug den relevante ~/.gramps/gramps{XX}/gramps.ini nøglefil.

- Gramps version 6.0:

~/.gramps/gramps60/gramps.ini

Se også:

- [Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees#Backup_dialog](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees#Backup_dialog)
- [Gramps_6.0_Wiki_Manual_-_Command_Line#Configuration_.28config.29_option](wiki:Gramps_6.0_Wiki_Manual_-_Command_Line#Configuration_.28config.29_option)
- [Install_latest_BSDDB#Make_Gramps_use_bsddb3](wiki:Install_latest_BSDDB#Make_Gramps_use_bsddb3)
- [Customize_the_Genealogical_Symbols_lookup_table#Genealogy_symbols_preferences](wiki:Customize_the_Genealogical_Symbols_lookup_table#Genealogy_symbols_preferences)

### Tema <span id="Theme"></span>

Udseendet af Gramps kan ændres.

- [Tilføjelse:Temaindstillinger](wiki:Addon:ThemePreferences)
- [Windows_AIO_themes](wiki:Windows_AIO_themes)
- [GTK 3 tema - GEPS 029: GTK3-GObject introspection konvertering](wiki:GEPS_029:_GTK3-GObject_introspection_Conversion#GTK_3_theme)
- [Overrule_Gramps_Icons](wiki:Overrule_Gramps_Icons) - til ældre Gramps-versioner.
- [UI style](wiki:UI_style)

Nogle rapporter kan også ændres:

- [Website report Themes](wiki:Website_report_Themes)

{{-}}

[Category:Documentation](wiki:Category:Documentation)
