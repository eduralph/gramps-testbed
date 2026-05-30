---
title: Da:Gramps 6.0 brugsanvisning - Arbejd med slægtsbøger
categories:
- Documentation
- Stub
managed: false
source: wiki-scrape
wiki_revid: 129346
wiki_fetched_at: '2026-05-30T16:34:57Z'
lang: da
---

{{#vardefine:chapter\|5}} {{#vardefine:figure\|0}}

En detaljeret gennemgang af vedligeholdelse og flytning af data (i masseoperationer) i slægtsbogs-databaser.

I dette kapitel gennemgår vi mekanismerne bag administration af dine slægtsbøger (databaser) samt mulighederne for at dele dine data med andre slægtsforskere. Dette omfatter oprettelse af tomme slægtsbøger, konvertering af gamle databaseformater, oprettelse af sikkerhedskopier, omdøbning af slægtsbøger, sletning af slægtsbøger samt import og eksport af slægtsbøger.

## Håndtere slægtsbøger

**Slægtsbøger** er det, Gramps kalder den databasestruktur, der bruges til at gemme og organisere genealogiske data. Du skal oprette en slægtsbog, før genealogiske data kan indtastes, gendannes fra et backuparkiv eller importeres fra anden software.

**Slægtsbøger** kan omdøbes, konverteres til andre database-backends, repareres eller slettes. En 'fejl' her vil ikke være uoprettelig. (Den største potentielle fejl, en utilsigtet sletning, kræver en bekræftelse.)

For at åbne Slægtsbøger-vinduet benyt en af følgende metoder:

1.  vælg menu-punktet
2.  klik på værktøjslinie-ikonet
3.  brug [genvejstast](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings) /

![[_media/Menubar-FamilyTrees-overview-FamilyTree-Loaded-example-60-da.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Slægtsbøger" vinduet]]

I Slægtsbøger-vinduet kan man oprette nye slægtsbøger (også kaldet stamtræer), give en slægtsbog et nyt navn, slette en slægtsbog eller indlæse en anden slægtsbog. I **Slægtsbøger** vises alle oprettede slægtsbøger med navn og hvornår de sidst er blevet opdateret. En `åben mappe` ikon vises på linien for den slægtsbog, som er åbnet i Gramps. {{-}}

Knapper i Slægtsbøger vinduet:

- opretter en ny tom slægtsbog.

- viser om den valgte slægtsbog.

- den valgte slægtsbog, der vises en advarsel som skal bekræftes før slægtsbogen slettets.

- den valgte slægtsbog og giv den et nyt navn.

- den åbne slægtsbog.

- den valgte slægtsbog. Denne funktion er kun tilgængelig, hvis slægtsbogen er baseret på en anden database end standard **Database Typen** *SQLite*.

- den valgte slægtsbog. Denne funktion er kun tilgængelig, hvis Gramps har detekteret et problem.

<!-- -->

- \- åbner denne sektion af brugerhåndbogen i default browseren.

- \- afslutter vinduet.

- åbner den valgte slægtsbog og låser databasen, så andre brugere ikke kan opdatere slægtsbogen.

## Oprette en ny slægtsbog <span id="Starting a new Family Tree"></span>

For at oprette en ny slægtsbog åben slægtsbøger vinduet.

Vælg knappen for at oprette en ny slægtsbog i listen over slægtsbøger. Den nye slægtsbog får automatisk navnet *`Slægtsbog 1`*. For at ændre navnet vælg knappen og indtast derefter det nye navn.

For at åbne den nye tomme slægtsbog enten dobbelt-klik slægtsbogslinien eller tryk på knappen

{{-}}

## Åbne en slægtsbog

Når Gramps startes åbnes automatisk den sidst anvendte slægtsbog. For at åbne an anden slægtsbog enten vælg menuen eller klik på i værktøjslinien. I vinduet vises en liste over alle slægtsbøger i Gramps. Vælg en slægtsbog i listen og klik for at åbne den. Alternativt dobbelt-klik linien i listen over slægtsbøger.

### Opret forbindelse til nyligt anvendt database

![[_media/ConnectToARecentDatabase-icon-toolbar-60-da.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Nyligt anvendt slægtsbogs-ikon drop down liste på værktøjslinien.]]

For at åbne en nyligt anvendt slægtsbog klik <big>▼ </big> pil-ned knappen til højre for værktøjslinie knappen og vælg en slægtsbog fra listen. {{-}}

## Gemme ændringer i din slægtsbog

Gramps gemmer ændringer i slægtsbogen, så snart de er tilføjet. Det betyder f. eks. at hver gang man klikker på i Gramps, så er ændringer umiddelbart lagret i databasen. Derfor er der heller ikke nogen "Gem" knap.

Man kan fortryde ændringer, som er gemt, ved at vælge . Hvis man vælger denne kommando gentagne gange, vil de seneste ændringer blive tilbageført en ad gangen. For at fortryde adskillige ændringer på en gang, kan man benytte menu-punktet , som åbner et historik vindue.

Hvis du ønsker at føre slægtsbogen tilbage til som den så ud, da slægtsbogen blev åbnet, så vælg menu-punktet . Dette vil åbne et advarselsvindue.

Hvis du vil gemme en kopi af en slægtsbog med et andet navn, skal du først eksportere slægtsbogen og derefter importere den i en ny tom slægtsbog. *Gramps XML* database formatet anbefales til dette formål.

## Ændre navn på slægtsbog <span id="Renaming a Family Tree"></span>

I -vinduet vælg den slægtsbog, som skal have et andet navn, og klik knappen. Indtast det nye navn for slægtsbogen.

{{-}}

## Åbning af en GEDCOM- eller XML-database <span id="Opening a GEDCOM or XML database"></span>

Gramps giver dig mulighed for at åbne bestemte databaser, der ikke er gemt i Gramps eget filformat, fra kommandolinjen. Se [Kommandolinjereferencer](wiki:Gramps_6.0_Wiki_Manual_-_Command_Line/da#Opening_options). Disse inkluderer XML- og GEDCOM-databaser. Men du skal være opmærksom på, at hvis XML- eller GEDCOM-databasen er relativt stor, vil du støde på ydeevneproblemer, og i tilfælde af et nedbrud kan dine data blive beskadiget. Derfor er det normalt bedre at oprette et ny Gramps-slægtsbog (database) og importere dine XML/GEDCOM-data til det.

{{-}}

## Slette en slægtsbog <span id="Deleting a Family Tree"></span>

At slette en slægtsbog vil **fuldstændig** fjerne slægtsbogen uden mulighed for at hente de tilhørende data. Overvej derfor først at lave en sikkerhedskopi (backup) af data i slægtsbogen ved at eksportere til [Gramps XML format](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees#Gramps_XML_and_XML_Package_import) og gemme filen.

### Fjern slægtsbogen 'Slægtsbog-navn'? vindue

![[_media/Remove-the-family-tree-name-Family-Tree-dialog-60-da.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Fjern slægtsbog 'slægtsbog-navn'? dialog]]

I -vinduet vælg den slægtsbog, som skal slettes, og klik knappen og derefter i advarselsvinduet vælg eller .

{{-}}

## Sikkerhedskopi af slægtsbog <span id="Backing up a Family Tree"></span>

Den sikreste måde at lave en backup af Gramps slægtsbog er at eksportere uden privat optioner og filtre til **Gramps XML** format (eller **Gramps XML Package** for at inkludere billeder) og derefter kopiere filen til et sikkert sted, f.eks. i 'skyen' eller en anden bygning.

### Sikkerhedskopi-vinduet

![[_media/MakeBackup-GrampsXML-Backup-example-60-da.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Tag sikkerhedskopi]]

Fra menu-linien vælg

#### Gramps XML sikkerhedskopi vindue

vinduet vises.

Du kan indtaste en , hvor sikkerhedskopien vil blive gemt eller bruge knappen for at åbne dialog.

Du kan skrive navn eller anvende det automatisk genererede filnavn.

Du kan vælge om skal *Medtages* eller **Udelades**(default).

Klik for at afbryde eller for at starte sikkerhedskopieringen, og når udført vil statuslinjen vise en bekræftelse af, hvor sikkerhedskopien er gemt.

{{-}}

- Du kan bruge [Arkivfunktionen](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees#Archiving_a_Family_Tree) (se næste afsnit) til at gemme øjebliksbilleder af din slægtsbog. Disse øjebliksbilleder kan bruges som enkle sikkerhedskopier, hvilket er meget nyttigt, hvis du vil prøve noget, som du senere måske vil fortryde. Denne metode bør dog ikke bruges til standard sikkerhedskopier, da den ikke overlever et harddisknedbrud eller de fleste andre katastrofer, der kan ramme en computer.
- For avancerede brugere: Hver database gemmes i sin egen undermappe under din [brugermappe](wiki:Gramps_6.0_Wiki_Manual_-_User_Directory) i `~/.gramps` . Selvom der kan laves en manuel sikkerhedskopi ved at sikkerhedskopiere denne mappe, anbefales det ikke. Det anbefales på det kraftigste, at du i stedet bruger en Gramps XML-sikkerhedskopi.

### Sikkerhedskopi ved afslutning

I vinduet Indstillinger under fanen Slægtsbøger kan Gramps indstilles til at lave en sikkerhedskopi, når Gramps afsluttes. Hvis slægtsbogen er lukket inden Gramps afsluttes udføres der ingen sikkerhedskopi.

#### Automatisk sikkerhedskopi

I fanen Slægtsbøger under Indstillinger kan der indstilles et interval for automatisk sikkerhedskopiering. Der kontrolleres, om slægtsbogen er ændret i den igangværende redigeringssession, og laver en arkivkopi. Nedtællingen starter, når Gramps startes, eller når intervallet ændres. Nedtællingen til sikkerhedskopiering udsættes, hvis computeren har været i dvale og forsinkes under opvågningen.

Intervallerne for automatisk sikkerhedskopiering kan indstilles til hvert "Aldrig", 15., 30. minut eller "Hver time", "Hver 12. time" og "Hver dag".

Hver sikkerhedskopi (uden medie) gemmes i den mappe, der er angivet i **Sti til sikkerhedskopi**.

Filnavnet har mønstret:

- <small>*\<Slægtsbog-navn\>*</small>`-yyyy-mm-dd-hh-mm-ss.gramps`

{{-}}

## Arkivering <span id="Archiving"></span>

En hurtig og praktisk mulighed, der giver dig mulighed for at dine slægtsbøger på et bestemt tidspunkt for at beholde en kopi før større ændringer og for at kunne vende tilbage til en kendt version.

- [Arkivering af en slægtsbog](#Archiving_a_Family_Tree)
- [Udpakning af et slægtsbogsarkiv](#Extracting_a_Family_Tree_Archive)
- [Fjernelse af et slægtsbogsarkiv](#Removing_a_Family_Tree_Archive)

#### Arkiveringsforudsætning <span id="Archiving_Prerequisite"></span>

Kræver, at [GNU Revision Control System](http://www.gnu.org/software/rcs/) (RCS) er installeret, så Gramps kan bruge arkiveringsfunktionen.

{{-}}

### Arkivering af en slægtsbog <span id="Archiving_a_Family_Tree"></span>

![[_media/ManageFamilyTrees-Archive-RevisionComment-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Arkiver et eksempel på et slægtsbog]]

Du kan dine slægtsbøger med Gramps for at beholde en kopi før større ændringer og for at kunne vende tilbage til en kendt version.

Sådan opretter du et arkiv:

1.  indlæs dit slægtsbog.
2.  klik på værktøjslinjens -knap (den viser , når du holder musen over den).
3.  klik på den slægtsbog, du lige har indlæst: knappen skulle vises.
4.  klik på , og du vil kunne indtaste en *Versionsbeskrivelse* for dit arkiv i dialogboksen .

Efter arkivering viser listen over slægtsbøger nu din originale slægtsbog med en trekant, der peger til højre, til venstre.

- Klik på trekanten for at vise arkivnavnet. (Klik igen for at skjule arkivlisten).

Arkiver kan være , (d) og (ed).

### Udpakning af et slægtsbogsarkiv <span id="Extracting_a_Family_Tree_Archive"></span>

![[_media/ManageFamilyTrees-Archive-Selected-to-Extract-example-60.png|Fig. {{#var:kapitel}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Dialogboksen "Slægtsbøger" (Administrator) - Arkiv valgt klar til "Udpakning" - eksempel]]

For at hente en version af en tidligere arkiveret slægtsbog i *Slægtsbøger*-administratoren skal du markere det arkiv, du vil gendanne, og vælge knappen .

{{-}} ![højre\|450px\|Fig. {{#var:chapter}}.{{#vardefineecho:figure\|{{#expr:{{#var:figure}}+1}}}} "Slægtsbøger"(Administrator) dialogboks - Arkiveret version udtrukket og valgt - eksempel](AdministrerFamilyTrees-Arkiv-Udpakkede-version-selekteret-eksempel-60.png "højre|450px|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Slægtsbøger"(Administrator) dialogboks - Arkiveret version udtrukket og valgt - eksempel")

Arkivet vil derefter blive gendannet i et nyt slægtsbog og blive vist på listen *Slægtsbøger (administrator)*.

Det udtrukne slægtsbogsnavn er baseret på det oprindelige navn og arkivnavnet, der er samlet, f.eks.:

*<kode><navn på originalt slægtsbog>:<navn på arkiv></kode>*

(se også [Arkivering af en slægtsbog](#Arkivering_af_en_slægtsbog))

Dette kan være en nyttig måde at bevare et arkiv på, fordi arkiver forsvinder, hvis den oprindelige slægtsbog slettes; og *'de er ikke indarbejdet i en Gramps XML-eksport af slægtsbogen*. {{-}}

### Fjernelse af et slægtsbogsarkiv <span id="Removing_a_Family_Tree_Archive"></span>

![[_media/ManageFamilyTrees-Archive-Remove-dialog-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Slægtsbøger"(Administrator) dialogboks - Fjernelse af en arkiveret version - eksempel]]

For at fjerne en arkiveret version skal du vælge og derefter bruge knappen for at se dialogboksen , hvor du kan vælge enten at og afslutte eller knappen .

{{-}}

#### Fjern <navn på arkiv> versionen af ​​<navn på originalt slægtsbog> dialogboksen

*Fjernelse af denne version forhindrer dig i at udpakke den i fremtiden.*

{{-}}

## Oplåsning af en slægtsbog

![[_media/FamilyTreesManager-Dialog-ShowingLocked-Sample-50-da.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Slægtsbøger-vinduet - eksempel med låst "Example" slægtsbog]]

Gramps er et databaseprogram til enkeltbrugere og identificerer slægtsbogsfiler som optaget med en ![[_media/22x22-gramps-lock.png]]'Lås', når de er i brug. Når Gramps åbner en slægtsbog, placerer det en låsefil (som angiver brugernavnet og domænet) i slægtsbogens undermappe i grampsdb-mappen i brugerkataloget. Gramps nægter at lade dig (eller andre) åbne den pågældende slægtsbog på samme tid. En anden instans af Gramps vil kunne åbne en anden slægtsbog, men enhver slægtsbog, der allerede er åbent, vil blive vist med lås-ikonet i kolonnen Status i dialogboksen Administrer slægtsbøger. Hvis du lukker slægtsbogen i den første kopi af Gramps, slettes låsefilen, og slægtsbogen bliver tilgængeligt for åbning i den anden instans.

Hvis du kunne åbne den samme slægtsbog i to eksemplarer af Gramps på samme tid, ville dine data sandsynligvis blive beskadiget, da de to ville overskrive hinandens arbejde.

### Fjern låsen for slægtsbog-navn dialog

![[_media/ErrorParsingArguments-dialog-DatabaseIsLocked-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Error parsing arguments - dialog - Database is locked example]]

I det usandsynlige tilfælde, at Gramps går ned, vil slægtsbogen blive efterladt i en låst tilstand (angivet med et ![[_media/22x22-gramps-lock.png]] lås-ikon i kolonnen Status ved siden af slægtsbogens navn).

Sådan låser du slægtsbogen op under opstart

- Hvis slægtsbogsindstillingerne er indstillet til at åbne et slægtsbog automatisk ved opstart, vil du se dialogboksen **Fejl ved fortolkning af argumenter**, der angiver, at databasen er låst. Klik på knappen Luk, og vælg derefter i menuen Slægtsbøger.
- Ellers vises automatisk, når Gramps starter.

{{-}}

![[_media/Break-the-lock-on-the-database-Dialog-example-50-da.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Fjern låsen fra &quot;Example&quot; database? - dialog]]Vælg den låste slægtsbog og derefter klik knappen. **Fjern lås på databasen "\[Slægtsbogs-navn\]"?** dialogen vil blive vist.

Klik nu knappen og vinduet vil nu vise at låsen er væk.

Vælg slægtsbogen, der tidligere var låst, og klik derefter knappen for at forsætte med arbejde på slægtsbogen. {{-}}

### Databasen er låst dialogboks

![[_media/TheDatabaseIsLocked-dialog-example-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Databasen er låst - dialogboks - Brug --force unlock-funktionen - eksempel]]

Hvis du får dialogboksen, skal du bruge [kommandolinjen --force unlock-funktion](#Command_Line:Force_unlock_option), hvis du er sikker på, at databasen ikke er i brug.

#### Kommandolinje: Mulighed for tvungen oplåsning <span id="Command_Line:Force_unlock_option"></span>

- [Kommandolinje: Mulighed for tvungen oplåsning](wiki:Gramps_6.0_Wiki_Manual_-_Command_Line#Force_unlock_option) - Alternativt kan du forsøge at gendanne fra et nedbrud, der låser slægtsbogen (databasen), fra kommandolinjen.

{{-}}

## Reparation af et beskadiget slægtsbog <span id="Repairing a damaged Family Tree"></span>

![[_media/FamilyTreesManager-Dialog-ShowingRedErrorStatusIcon-Sample-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Slægtsbøger (Manager) - Dialog - Viser rødt fejlstatusikon for "Eksempel"-slægtsbog]]

Hvis din slægtsbog bliver beskadiget eller ødelagt på en eller anden måde, viser Gramps Slægtsbøger Manager et rødt fejlikon i kolonnen .

For at få Gramps til at forsøge at reparere skaden skal du vælge slægtsbogen og derefter klikke på knappen .

Dette vil forsøge at genopbygge din slægtsbog fra de sikkerhedskopier, der automatisk oprettes ved afslutning.

Se også:

- [Gendan beskadiget slægtsbog (engelsk)](wiki:Recover_corrupted_family_tree)

{{-}}

## Konvertering af en BSDDB-slægtsbog til SQLite <span id="Converting a BSDDB Family Tree to SQLite"></span>

![[_media/ManageFamilyTrees-Convert-the-database-dialog-example-51.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} <strong>Konverter 'Familiens navn'-databasen?</strong> dialogboksen med <em>Slægtsbøger (Administrator)</em> - Dialogboks vist i baggrunden]]

Hvis du har et ældre [BSDDB](wiki:Gramps_Glossary/da#bsddb) format **Databasetype** vist for et af dine slægtsbøger i dialogboksen *Slægtsbøger (Administrator)*, vil valg af en slægtsbog i dialogboksen *Slægtsbøger (Administrator)* vise knappen som tilgængelig.

Når du er klar, skal du vælge knappen , og dialogboksen vises med meddelelsen **Ønsker du at konvertere denne slægtsbog til en SQLite-database?**. Du kan vælge for at stoppe eller for at starte processen. Når dialogboksen *Slægtsbøger (Administrator)* er fuldført, viser den en ny post for den konverterede kopi af din slægtsbog, men med *Databasetypen* for SQLite skal du derefter åbne og sikkerhedskopiere den konverterede slægtsbog.

Du kan derefter omdøbe den originale BSDDB-slægtsbog med ordet **OLD**, eller du kan slette den for at undgå forvirring, hvorefter du kan omdøbe den nye SQLite-database.

{{-}}

## Import af data <span id="Importing data"></span>

![[_media/ImportFamilyTree-dialog-Select-file-type-default-list-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Importer slægtsbog - dialog - med standard rullemenuen "Vælg filtype:" vist]]

Import giver dig mulighed for at overføre data fra andre slægtsprogrammer til en Gramps-slægtsbog. Gramps inkluderer et kernesæt af import-plugins, der vælges automatisk baseret på den tilsvarende filtypenavn. Du kan også installere yderligere "Importer" [plugin-typen tredjepartsudvidelser](wiki:Third-party_Addons), og automatiseringen vil genkende de nye filtypenavne.

I dialogboksen skal du bruge rullemenuen til at vælge mellem følgende understøttede importfiltypeformater:

- **Automatisk registreret** *(standard)* - Denne automatiseringsindstilling kan tilsidesættes. Dette er nyttigt, når formater opdateres og gør de centrale plugins forældede.

<!-- -->

- [Kommaseparerede værdier regneark (CSV)](#Gramps_CSV_import) (`.csv` filtypenavn)
- [GEDCOM](#GEDCOM_import) (version 5.5.1 `.ged` filtypenavn) de facto standard filformat til dataudveksling mellem slægtsforskningsprogrammer.
- GeneWeb (`.gw` filtypenavn) - [GeneWeb](https://en.wikipedia.org/wiki/GeneWeb) er slægtsforskningssoftware med en webgrænseflade.
- [Gramps Package (bærbar XML)](#Gramps_XML_and_XML_Package_import) (`.gpkg` filtypenavn) Gramps [.tar.gz](https://wikipedia.org/wiki/.tar.gz) arkivkomprimeret backupformat. Understøtter inkludering af mediefiler.
- [Gramps XML Family Tree](#Gramps_XML_and_XML_Package_import) (filtypenavn `.gramps`) Gramps' oprindelige dataudvekslingsformat i ukomprimeret tekst og [gzip](https://wikipedia.org/wiki/Gzip) komprimeret
- [Pro-Gen](wiki:Import_from_another_genealogy_program#Pro-Gen) (filtypenavn `.def`) - [Pro-Gen](https://www.pro-gen.nl/gbhome.htm) har været meget populær i Holland og Nordvesttyskland. Det bruges ofte af folk, der begyndte at indsamle og lagre data allerede i 1989. Dette var et DOS-baseret program, der er blevet opdateret til at fungere med Win 10.

<!-- -->

- vCard (filtypenavn `.vcf`) - [Virtual Contact File](https://wikipedia.org/wiki/VCard) er et standardfilformat for elektroniske visitkort. Understøtter kun [version 3.0 format](https://wikipedia.org/wiki/VCard#Properties).

------------------------------------------------------------------------

Yderligere importformater kan installeres fra tilføjelser og vil også blive vist, for eksempel:

- [JSON Import](wiki:Addon:JSON_Export_Import) (filtypenavn `.json`) - [JavaScript Object Notation](https://www.json.org/) er et letvægtsformat til dataudveksling. ***tilføjelse***
- [SQLite Import](wiki:Tilføjelse:SQLite_Export_Import) (filtypenavn `.sql`) - [SQLite-databaseformat](https://www.sqlite.org/fileformat.html) **tilføjelse**

### Importér slægtsbog-dialogboks <span id="Import Family Tree dialog"></span>

![[_media/Importfamilytree-dialog-51.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Importér slægtsbog - eksempel på dialogboks]]

Opret først en [ny og tom slægtsbog](#Starting_a_new_Family_Tree). Vælg derefter menuen eller brug [tastaturgenvej](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings/da#2) for at importere data eller gendanne en tidligere gemt Gramps-slægtsbog (fra en ældre version af Gramps eller den nuværende version). Dialogboksen **** åbnes, hvor du bliver bedt om at angive den fil, du ønsker at importere.

Hvis du forsøger at importere til en slægtsbog, der ***ikke er tom***, åbnes dialogboksen . Dette minder dig om at lave en sikkerhedskopi, før du importerer. Opret i stedet en ny slægtsbog, medmindre du bevidst forsøger at flette data.

Gramps bruger en [GTK Filvælger](https://developer.gnome.org/gtk3/stable/GtkFileChooser.html) til at vælge den datafil, der skal importeres. De grundlæggende muligheder for at navigere til en fil er velkendte.

Standardvisningsindstillingen for filstien er at vise hvert mappeniveau som klikbart [breadcrumb navigation](https://en.wikipedia.org/wiki/Breadcrumb_navigation). Stien kan indtastes i en redigerbar tekstboks ved at trykke på -tasten.

Filtypeendelsen vil normalt tillade, at indstillingen forventer, at et bestemt datamønster konverteres til det oprindelige databaseformat. Du kan tilsidesætte dette ved at vælge en anden **** indstilling. Listen over filer kan filtreres ved at ændre fra indstillingen . Hvis du vælger indstillingen og derefter vælger en ikke-understøttet filimporttype, vil du blive vist advarselsdialogboksen . Når du planlægger at bruge importfunktionen gentagne gange (til løbende opdateringer eller inklusive slægtsforskning), kan du [tilpasse dialogboksen](https://gramps.discourse.group/t/need-help-doing-a-cross-os-linux-mac-verification/1068/5) ved at tilføje knapper til bogmærkede mappestier. Højreklik på et mappenavn og vælg fra pop op-menuen.

### Understøttede importfiltypeformater <span id="Supported import file type formats"></span>

#### Gramps XML og XML-pakkeimport <span id="Gramps XML and XML Package import"></span>

Gramps [XML](wiki:XML) og Gramps [XML](wiki:XML)-pakkedatabasen er de oprindelige arkivformater for Gramps. Der er ingen risiko for informationstab ved import (gendannelse) fra eller eksport til disse formater.

- Gramps [XML](wiki:XML) (.gramps): Gramps [XML](wiki:XML)-filen er standardformatet for dataudveksling og sikkerhedskopiering i Gramps og var også standardformatet for databaser i ældre (før 2.x) versioner af Gramps. I modsætning til grdb-formatet i GRAMPS V2.x (eller efterfølgende BSDDB- eller SQLite-formatfiler) er den arkitekturuafhængig og menneskeligt læsbar. Databasen kan også have referencer til ikke-lokale (eksterne) medieobjekter, derfor er det ikke garanteret, at den er fuldstændig bærbar (for fuld bærbarhed bør medieobjekter i Gramps [XML](wiki:XML)-pakken (.gpkg) anvendes). Gramps [XML](wiki:XML)-databasen oprettes ved at eksportere (Menu ) til det format.

<!-- -->

- Gramps [XML](wiki:XML)-pakke (.gpkg): Gramps [XML](wiki:XML)-pakken er et **komprimeret** arkiv, der indeholder Gramps [XML](wiki:XML)-filen og alle [medie](wiki:Gramps_Glossary/da#media)-objekter (billeder, lydfiler osv.), som databasen refererer til. Fordi den indeholder alle medieobjekterne, er dette format fuldstændigt bærbart. Gramps [XML](wiki:XML)-pakken oprettes ved at eksportere (Menu ) data i det format.

Hvis du importerer information fra en anden Gramps-database eller Gramps [XML](wiki:XML)-database, vil du se handlingens status i statuslinjen i Gramps hovedvindue. Når importen er færdig, viser et feedbackvindue antallet af importerede objekter. Hvis de importerede data stammer fra selve den slægtsbog, hvor du importerer dataene, giver importfeedbacken forslag til, hvad der kan flettes sammen; fletningen "**gøres** ikke automatisk for dig. Hvis du vil flette grundlæggende slægtsdata automatisk, kan du overveje CSV-regnearks eksport/import. {{-}}

#### Gramps CSV-import <span id="Gramps CSV import"></span>

Gramps CSV-regnearksformatet tillader import og eksport af en delmængde af dine Gramps-data i et simpelt regnearksformat. Se [CSV-import og -eksport](wiki:Da:Gramps_6.0_brugsanvisning_-_CSV_Import_og_Export) for mere information. {{-}}

#### GEDCOM-import <span id="GEDCOM import"></span>

Opret først en [ny tom slægtsbog](#Starting_a_new_Family_Tree). Vælg derefter menuen eller [keybinding](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings/da#2) , og brug derefter dialogboksen til at vælge den GEDCOM-fil, du vil importere. Afhængigt af GEDCOM-typen kan du derefter se dialogboksen . Når du importerer information fra GEDCOM, viser Gramps' hovedvindue dig en [statuslinje](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window/da#Status_Bar_and_Progress_Bar). Når GEDCOM-importen er færdig, viser vinduet og vinduerne **** eventuelle resultater eller advarsler.

- I sektionen [Importer Gramps-indstillinger](wiki:Gramps_6.0_Wiki_Manual_-_Settings/da#Import) under fanen Import i præferencer kan du også vælge at og også , hvilket begge kan forsinke importen af ​​dine data betydeligt.

{{-}}

##### GEDCOM-kodningsdialog <span id="GEDCOM Encoding dialog"></span>

![[_media/GEDCOM-Encoding-dialog-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} GEDCOM-kodning - dialog]]

Dialogboksen vises, når den GEDCOM-fil, du importerer, har identificeret sig selv som bruger ANSEL-kodningsformatet. Nogle gange er dette en fejl. Hvis du efter importen af ​​GEDCOM bemærker, at dine data indeholder usædvanlige tegn, skal du fortryde importen og tilsidesætte tegnsættet ved at vælge en anden kodning fra den tilgængelige liste.

- **standard**
- *ANSEL* (American National Standard Extended Latin)
- *ANSI* (American National Standards Institute; svarende til ISO-8859-1)
- *ASCII* (American Standard Code for Information Interchange)
- *UTF8* (Unicode Transformation Format 8-bit)

{{-}}

##### Dialogboks til import af statistik <span id="Import Statistics dialog"></span>

![[_media/ImportStatistics-dialog-example-GrampXML-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Importstatistik - dialogboks - Viser resultater for &quot;Example.gramps&quot; Gramps XML-filen]] Viser detaljer om importstatistikken afhængigt af den importerede filtype.

- Gramps XML - Viser importstatistik og meddelelsen:
  - 
- GEDCOM - ingen importstatistik (Kun rapporter hvis det lykkes)

{{-}}

##### GEDCOM import-rapport dialogboks <span id="GEDCOM import report dialog"></span>

![[_media/GEDCOM-import-report-result-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} GEDCOM importrapport - eksempelresultater.]]

**** beskriver de fleste af de GEDCOM-linjer, der enten blev ignoreret eller ikke kunne forstås. Disse skyldes sandsynligvis, at de ikke er en del af GEDCOM 5.5.1-standarden. (Se [Tilføjelse:GEDCOM-udvidelser](wiki:Addon:GEDCOM_Extensions).) Indholdet af GEDCOM-linjen (eller linjer, hvor der er fortsættelseslinjer) vises også. I nogle tilfælde er linjerne muligvis ikke præcis det, der er indeholdt i GEDCOM-filen, fordi linjen er rekonstrueret efter en vis bearbejdning.

{{-}}

###### Læsning af rapporten \<span id"Reading the report"\></span>

![[_media/Source-Note-GEDCOMImportNote-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} GEDCOM importnote, der angiver udeladte data, der er knyttet til "Source&gt;Note" (data fra "GEDitCOM" - "GEDCOM 5.5 Torture Test Files")]]

Gramps bruger en mere avanceret 'datamodel' end GEDCOM, derfor kan nogle data i GEDCOM ikke importeres til Gramps. (Se [Gramps and GEDCOM](wiki:Gramps_and_GEDCOM).) De vigtigste undtagelser er:

- Nogle GEDCOM-attributstrukturer behandles som Gramps , og derfor kan mange af de primitive GEDCOM-elementer ikke gemmes.
- DATA-elementerne i en SOURCE_RECORD (som angiver de registrerede begivenheder og den ansvarlige myndighed) ignoreres.
- Eventuelle kildehenvisninger i noter ignoreres.
- Mange primitive GEDCOM-elementer har ikke præcist tilsvarende dataelementer i Gramps, og de gemmes derfor som med passende navne, normalt GEDCOM-tagget. Dette gælder især for header, submitter og submission GEDCOM-poster og bestemte felter som REFN, RFN, RIN og AFN.

Hvor data er angivet som 'ignoreret', rapporteres udeladelsen i feedbacken ved importens afslutning, og den inkluderes i en , der er knyttet til et relevant objekt med en brugerdefineret type . Se for eksempel kildeobjektet i skærmbilledet.

Hvor data er angivet som 'lydløst ignoreret', rapporteres den ikke og inkluderes ikke i en note. I øjeblikket kan dette betragtes som noget, der er blevet overset af Gramps, og bør rejses som et problem . {{-}}

##### GEDCOM importbegrænsninger <span id="GEDCOM import limitations"></span>

Dette afsnit beskriver alle GEDCOM-data, der ikke kan repræsenteres direkte i Gramps, og hvordan de håndteres. For yderligere information om begrænsningerne for GEDCOM-import (og -eksport) henvises til afsnittet om [Gramps and GEDCOM](wiki:Gramps_and_GEDCOM).

###### HEADer, SUBmission og SUBMitter

Gramps har ingen direkte repræsentation af [HEADer](#HEADer), [SUBmission](#SUBmission) og [SUBMitter](#SUBMitter) data, og derfor skal al information deri gemmes i andre objekter. Afhængigt af en [Import preferences](wiki:Gramps_6.0_Wiki_Manual_-_Settings/da#Source_GEDCOM_import) indstilling kan et 'standardkilde'-objekt oprettes. Hvis dette oprettes, gemmes mange af dataene i den pågældende eller i , der er knyttet til den pågældende kilde.

###### HEADer

`   HEADER:=`  
`        n HEAD                                          {1:1}`  
`          +1 SOUR `<APPROVED_SYSTEM_ID>`                  {1:1}  (Data item of the 'default source')`  
`            +2 VERS `<VERSION_NUMBER>`                    {0:1}  (Data item of the 'default source')`  
`            +2 NAME `<NAME_OF_PRODUCT>`                   {0:1}  (Data item of the 'default source')`  
`            +2 CORP `<NAME_OF_BUSINESS>`                  {0:1}  (Repository of the 'default source')`  
`              +3 <`<ADDRESS_STRUCTURE>`>                  {0:1}  (Repository of the 'default source')`  
`            +2 DATA `<NAME_OF_SOURCE_DATA>`               {0:1}  (Data item of the 'default source')`  
`              +3 DATE `<PUBLICATION_DATE>`                {0:1}  (Data item of the 'default source')`  
`              +3 COPR `<COPYRIGHT_SOURCE_DATA>`           {0:1}  (Data item of the 'default source')`  
`          +1 DEST `<RECEIVING_SYSTEM_NAME>`               {0:1*} (Data item of the 'default source')`  
`          +1 DATE `<TRANSMISSION_DATE>`                   {0:1}  (Data item of the 'default source')`  
`            +2 TIME `<TIME_VALUE>`                        {0:1}  (Data item of the 'default source')`  
`          +1 SUBM @`<XREF:SUBM>`@                         {1:1}  (Data item of the 'default source')`  
`                                                               (Also used to determine the SUBMITTER_RECORD)`  
`                                                               (that should be stored as the database owner)`  
`          +1 SUBN @`<XREF:SUBN>`@                         {0:1}  (ignored)`  
`          +1 FILE `<FILE_NAME>`                           {0:1}  (Data item of the 'default source')`  
`          +1 COPR `<COPYRIGHT_GEDCOM_FILE>`               {0:1}  (stored as the Publication information of the 'default source')`  
`          +1 GEDC                                       {1:1}`  
`            +2 VERS `<VERSION_NUMBER>`                    {1:1}  (Data item of the 'default source')`  
`            +2 FORM `<GEDCOM_FORM>`                       {1:1}  (Data item of the 'default source')`  
`          +1 CHAR `<CHARACTER_SET>`                       {1:1}  (Data item of the 'default source')`  
`            +2 VERS `<VERSION_NUMBER>`                    {0:1}  (Data item of the 'default source')`  
`          +1 LANG `<LANGUAGE_OF_TEXT>`                    {0:1}  (Data item of the 'default source')`  
`          +1 PLAC                                       {0:1}`  
`            +2 FORM `<PLACE_HIERARCHY>`                   {1:1}  (see below)`  
`          +1 NOTE `<GEDCOM_CONTENT_DESCRIPTION>`          {0:1}  (note attached to the 'default source')`  
`            +2 [CONT|CONC] `<GEDCOM_CONTENT_DESCRIPTION>` {0:M}`  
`            `  
`   * NOTE: Submissions to the Family History Department for Ancestral`  
`     File submission or for clearing temple ordinances must use a`  
`     DESTination of ANSTFILE or TempleReady.`

The PLAC FORM is stored internally and used to govern the interpretation of places (in accordance with the GEDCOM specification).

###### SUBmissioN

The SUBMISSION_RECORD (there should be only one, but this is not checked) is stored as a item of the 'default source'

`    SUBMISSION_RECORD:=`  
`        n @`<XREF:SUBN>`@ SUBN                            {1:1]`  
`          +1 SUBM @`<XREF:SUBM>`@                         {0:1}`  
`          +1 FAMF `<NAME_OF_FAMILY_FILE>`                 {0:1}`  
`          +1 TEMP `<TEMPLE_CODE>`                         {0:1}`  
`          +1 ANCE `<GENERATIONS_OF_ANCESTORS>`            {0:1}`  
`          +1 DESC `<GENERATIONS_OF_DESCENDANTS>`          {0:1}`  
`          +1 ORDI `<ORDINANCE_PROCESS_FLAG>`              {0:1}`  
`          +1 RIN `<AUTOMATED_RECORD_ID>`                  {0:1}`

###### SUBMitter

SUBMITTER_RECORDs (there may be more than one) are stored as records attached to the 'default source' except as indicated in bold below. The SUBMITTER_RECORD that corresponds with the SUBM record in the HEADER is used to set the [database owner](wiki:Gramps_6.0_Wiki_Manual_-_Tools#Edit_Database_Owner_Information) and can be copied to the [Researcher Information](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Researcher) tab if required.

`   SUBMITTER_RECORD:=`  
`        n @`<XREF:SUBM>`@   SUBM                          {1:1}`  
`          +1 NAME `<SUBMITTER_NAME>`                      {1:1}`  
`          +1 <`<ADDRESS_STRUCTURE>`>                      {0:1}`  
`          `**`+1 <`<MULTIMEDIA_LINK>`> {0:M}`**  
`          `**`+1 LANG `<LANGUAGE_PREFERENCE>` {0:3}`**  
`          `**`+1 RFN `<SUBMITTER_REGISTERED_RFN>` {0:1}`**  
`          `**`+1 RIN `<AUTOMATED_RECORD_ID>` {0:1}`**  
`          +1 <`<CHANGE_DATE>`>                            {0:1}`

- Mutimedia link is ignored
- LANG is ignored
- RFN and RIN are ignored

###### INDIvidual

The INDIVIDUAL_RECORD is stored as a Gramps record, except as indicated in bold below.

`   INDIVIDUAL_RECORD: =`  
`        n @`<XREF:INDI>`@  INDI                           {1:1}`  
`          +1 RESN `<RESTRICTION_NOTICE>`                  {0:1}`  
`          +1 <`<PERSONAL_NAME_STRUCTURE>`>                {0:M}`  
`          +1 SEX `<SEX_VALUE>`                            {0:1}`  
`          +1 <`<INDIVIDUAL_EVENT_STRUCTURE>`>             {0:M}`  
`          `**`+1 <`<INDIVIDUAL_ATTRIBUTE_STRUCTURE>`> {0:M}`**  
`          +1 <`<LDS_INDIVIDUAL_ORDINANCE>`>               {0:M}`  
`          +1 <`<CHILD_TO_FAMILY_LINK>`>                   {0:M}`  
`          +1 <`<SPOUSE_TO_FAMILY_LINK>`>                  {0:M}`  
`          `**`+1 SUBM @`<XREF:SUBM>`@ {0:M}`**  
`          +1 <`<ASSOCIATION_STRUCTURE>`>                  {0:M}`  
`          +1 ALIA @`<XREF:INDI>`@                         {0:M}`  
`          `**`+1 ANCI @`<XREF:SUBM>`@ {0:M}`**  
`          `**`+1 DESI @`<XREF:SUBM>`@ {0:M}`**  
`          +1 <`<SOURCE_CITATION>`>                        {0:M}`  
`          +1 <`<MULTIMEDIA_LINK>`>                        {0:M}`  
`          +1 <`<NOTE_STRUCTURE>`>                         {0:M}`  
`          +1 RFN `<PERMANENT_RECORD_FILE_NUMBER>`         {0:1}`  
`          +1 AFN `<ANCESTRAL_FILE_NUMBER>`                {0:1}`  
`          +1 REFN `<USER_REFERENCE_NUMBER>`               {0:M}`  
`            `**`+2 TYPE `<USER_REFERENCE_TYPE>` {0:1}`**  
`          +1 RIN `<AUTOMATED_RECORD_ID>`                  {0:1}`  
`          +1 <`<CHANGE_DATE>`>                            {0:1}`  
`   `

- Link to submitter, ancestor interest and descendent interest indicators are silently ignored.
- The alias indicator ("An indicator to link different record descriptions of a person who may be the same person") is stored as an called 'Alias'.
- The REFN and REFN:TYPE are stored as of the , but if there is more than one REFN, it may not be clear which TYPE is associated with which REFN.

Handling of the INDIVIDUAL_ATTRIBUTE_STRUCTURE is rather complicated. The following tags:

- EDUC (Scholastic achievement),
- NMR (Count of marriages),
- OCCU (Occupation),
- PROP (Possessions),
- RELI (Religious affiliation),
- RESI and
- TITL (Nobility title)

are all treated as Gramps s and the associated information is stored in the event structure. The details following the main tag (shown in brackets in the list above) are stored as the of the . The <EVENT_DESCRIPTOR> following the TYPE tag will overwrite the if the <EVENT_DESCRIPTOR> is not the attribute name.

The following tags:

- CAST (Caste name),
- DSCR (Physical description),
- INDO (National ID Number),
- NATI (National or tribal origin),
- NCHI (Count of Children) and
- SSN (Social Security Number)

are all treated as Gramps s and most of the fields except the details following the main tag (shown in brackets in the list above), the source citation and the note structure are ignored, as indicated in bold below.

`   INDIVIDUAL_ATTRIBUTE_STRUCTURE: =`  
`        n  CAST `<CASTE_NAME>`                            {1:1}`  
`          +1 <`<EVENT_DETAIL>`>                           {0:1}`  
`             etc.`  
`   `  
`   EVENT_DETAIL: =`  
`        `**`n TYPE `<EVENT_DESCRIPTOR>` {0:1}`**  
`        `**`n DATE `<DATE_VALUE>` {0:1}`**  
`        `**`n <`<PLACE_STRUCTURE>`> {0:1}`**  
`        `**`n <`<ADDRESS_STRUCTURE>`> {0:1}`**  
`        `**`n AGE `<AGE_AT_EVENT>` {0:1}`**  
`        `**`n AGNC `<RESPONSIBLE_AGENCY>` {0:1}`**  
`        `**`n CAUS `<CAUSE_OF_EVENT>` {0:1}`**  
`        n  <`<SOURCE_CITATION>`>                          {0:M}`  
`          +1 <`<NOTE_STRUCTURE>`>                         {0:M}`  
`          +1 <`<MULTIMEDIA_LINK>`>                        {0:M}`  
`        `**`n <`<MULTIMEDIA_LINK>`> {0:M}`**  
`        n  <`<NOTE_STRUCTURE>`>                           {0:M}`  
`        `  
`        `

- Individual attribute structure, type, date, place structure, address structure, age, agency, cause and multimedia link are all ignored.

###### FAM_RECORD

The FAM_RECORD is stored as a Gramps record.

`   FAM_RECORD:=`  
`        n @`<XREF:FAM>`@   FAM                            {1:1}`  
`          +1 <`<FAMILY_EVENT_STRUCTURE>`>                 {0:M}`  
`          +1 HUSB @`<XREF:INDI>`@                         {0:1}`  
`          +1 WIFE @`<XREF:INDI>`@                         {0:1}`  
`          +1 CHIL @`<XREF:INDI>`@                         {0:M}`  
`          +1 NCHI `<COUNT_OF_CHILDREN>`                   {0:1}`  
`          +1 SUBM @`<XREF:SUBM>`@                         {0:M}`  
`          +1 <`<LDS_SPOUSE_SEALING>`>                     {0:M}`  
`          +1 <`<SOURCE_CITATION>`>                        {0:M}`  
`          +1 <`<MULTIMEDIA_LINK>`>                        {0:M}`  
`          +1 <`<NOTE_STRUCTURE>`>                         {0:M}`  
`          +1 REFN `<USER_REFERENCE_NUMBER>`               {0:M}`  
`            +2 TYPE `<USER_REFERENCE_TYPE>`               {0:1}`  
`          +1 RIN `<AUTOMATED_RECORD_ID>`                  {0:1}`  
`          +1 <`<CHANGE_DATE>`>                            {0:1}`

- The link to submitter is silently ignored.
- The REFN and REFN:TYPE are stored as of the , but if there is more than one REFN, it may not be clear which TYPE is associated with which REFN.

###### SOURCE_RECORD

The SOURCE_RECORD is stored as a Gramps record, except as indicated in bold below.

`   SOURCE_RECORD:=`  
`        n @`<XREF:SOUR>`@ SOUR                            {1:1}`  
`          `**`+1 DATA {0:1}`**  
`            `**`+2 EVEN `<EVENTS_RECORDED>` {0:M}`**  
`              `**`+3 DATE `<DATE_PERIOD>` {0:1}`**  
`              `**`+3 PLAC `<SOURCE_JURISDICTION_PLACE>` {0:1}`**  
`            `**`+2 AGNC `<RESPONSIBLE_AGENCY>` {0:1}`**  
`            `**`+2 <`<NOTE_STRUCTURE>`> {0:M}`**  
`          +1 AUTH `<SOURCE_ORIGINATOR>`                   {0:1}`  
`            +2 [CONT|CONC] `<SOURCE_ORIGINATOR>`          {0:M}`  
`          +1 TITL `<SOURCE_DESCRIPTIVE_TITLE>`            {0:1}`  
`            +2 [CONT|CONC] `<SOURCE_DESCRIPTIVE_TITLE>`   {0:M}`  
`          +1 ABBR `<SOURCE_FILED_BY_ENTRY>`               {0:1}`  
`          +1 PUBL `<SOURCE_PUBLICATION_FACTS>`            {0:1}`  
`            +2 [CONT|CONC] `<SOURCE_PUBLICATION_FACTS>`   {0:M}`  
`          +1 TEXT `<TEXT_FROM_SOURCE>`                    {0:1}`  
`            +2 [CONT|CONC] `<TEXT_FROM_SOURCE>`           {0:M}`  
`          +1 <`<SOURCE_REPOSITORY_CITATION>`>             {0:1}`  
`          +1 <`<MULTIMEDIA_LINK>`>                        {0:M}`  
`          +1 <`<NOTE_STRUCTURE>`>                         {0:M}`  
`          +1 REFN `<USER_REFERENCE_NUMBER>`               {0:M}`  
`            +2 TYPE `<USER_REFERENCE_TYPE>`               {0:1}`  
`          +1 RIN `<AUTOMATED_RECORD_ID>`                  {0:1}`  
`          +1 <`<CHANGE_DATE>`>                            {0:1}`

- DATA and its subsidiary records are ignored

###### REPOSITORY_RECORD

The REPOSITORY_RECORD is stored as a Gramps record, except as indicated in bold below.

`   REPOSITORY_RECORD: =`  
`        n @`<XREF:REPO>`@ REPO                            {1:1}`  
`          +1 NAME `<NAME_OF_REPOSITORY>`                  {0:1}`  
`          +1 <`<ADDRESS_STRUCTURE>`>                      {0:1}`  
`          +1 <`<NOTE_STRUCTURE>`>                         {0:M}`  
`          `**`+1 REFN `<USER_REFERENCE_NUMBER>` {0:M}`**  
`            `**`+2 TYPE `<USER_REFERENCE_TYPE>` {0:1}`**  
`          `**`+1 RIN `<AUTOMATED_RECORD_ID>` {0:1}`**  
`          +1 <`<CHANGE_DATE>`>                            {0:1}`

- REFN, REFN:TYPE and RIN are ignored

###### MULTIMEDIA_RECORD

The MULTIMEDIA_RECORD is stored as a Gramps record, except as indicated in bold below.

`   MULTIMEDIA_RECORD:=`  
`        n @`<XREF:OBJE>`@ OBJE                            {1:1}`  
`          +1 FORM `<MULTIMEDIA_FORMAT>`                   {1:1}`  
`          +1 TITL `<DESCRIPTIVE_TITLE>`                   {0:1}`  
`          +1 <`<NOTE_STRUCTURE>`>                         {0:M}`  
`          +1 <`<SOURCE_CITATION>`>                        {0:M}`  
`          `**`+1 BLOB {1:1}`**  
`            `**`+2 CONT `<ENCODED_MULTIMEDIA_LINE>` {1:M}`**  
`          +1 OBJE @`<XREF:OBJE>`@     /* chain to continued object */  {0:1}`  
`          `**`+1 REFN `<USER_REFERENCE_NUMBER>` {0:M}`**  
`            `**`+2 TYPE `<USER_REFERENCE_TYPE>` {0:1}`**  
`          `**`+1 RIN `<AUTOMATED_RECORD_ID>` {0:1}`**

- It is expected that there will be a 'FILE' tag to indicate the file holding the multimedia object. This usage is taken from GEDCOM 5.5.1, but the ability in GEDCOM 5.5.1 to have more than one <MUTIMEDIA_FILE_REFN> and having the FORM, TYPE and TITL subsidiary to the FILE gedcom_line is not supported (a later FILE may overwrite an earlier one - there is no error checking).
- BLOB is ignored
- REFN, REFN:TYPE and RIN are ignored

###### NOTE_RECORD

The NOTE_RECORD is stored as a Gramps record, except as indicated in bold below.

`   NOTE_RECORD:=`  
`        n @`<XREF:NOTE>`@ NOTE `<SUBMITTER_TEXT>`           {1:1}`  
`          +1 [ CONC | CONT] `<SUBMITTER_TEXT>`            {0:M}`  
`          `**`+1 <`<SOURCE_CITATION>`> {0:M}`**  
`          `**`+1 REFN `<USER_REFERENCE_NUMBER>` {0:M}`**  
`            `**`+2 TYPE `<USER_REFERENCE_TYPE>` {0:1}`**  
`          `**`+1 RIN `<AUTOMATED_RECORD_ID>` {0:1}`**  
`          +1 <`<CHANGE_DATE>`>                            {0:1}`

- source citation ignored
- REFN, REFN:TYPE and RIN are ignored

{{-}}

## Eksport af data <span id="Exporting data"></span>

For at eksportere data skal du vælge Menu eller [tastaturgenvej](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings/da#) eller på Apple Mac'er. Dette vil åbne dialogboksen .

Eksport giver dig mulighed for at dele enhver del af din Gramps-slægtsbog (database) med andre forskere, samt at overføre dine data til en anden computer. Gramps kan eksportere data til følgende filformater:

- [Kommaseparerede værdier regneark (CSV)](#Comma_Separated_Values_Spreadsheet.28CSV.29_export)
- [GEDCOM](#GEDCOM_export)
- [GeneWeb](#GeneWeb_export)
- Gramps [XML](wiki:Gramps_XML) (slægtsbog)
- Gramps [XML](wiki:Gramps_XML) Pakke (slægtsbog og medier)
- [Web-slægtsbog](#Web_Family_Tree_export)
- [vCalendar](#vCalendar_export)
- [vCard](#vCard_export)

Yderligere eksportformater kan installeres fra tilføjelser.

{{-}}

### Eksport-assistent dialogboks <span id="Export Assistant dialog"></span>

Siderne guider dig gennem [valg af outputfilformat](#Choose_the_output_format) og derefter de eksportmuligheder, der er specifikke for det pågældende filformat. Efter siden udføres eksporten i henhold til de valg, du har foretaget. Du kan til enhver tid klikke på knappen og rette eventuelle valg og derefter gå videre for at gentage eksporten.

- [Gemmer dine data](#Gemmer_dine_data)
- [Vælg outputformat](#Vælg_outputformat)
- [Eksportindstillinger](#Eksportindstillinger)
- [Vælg gem fil](#Vælg_gem_fil)
- [Endelig bekræftelse](#Endelig_bekræftelse)
- [Oversigt](#Oversigt)

#### Gemmer dine data <span id="Saving your data"></span>

![[_media/ExportAssistant-SavingYourData-wizard-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Eksportassistent: "Gemmer dine data" - guidens startside]]

Generelle oplysninger om eksport fra Gramps:

  
**Under normale omstændigheder kræver Gramps ikke, at du gemmer dine ændringer direkte. Alle ændringer, du foretager, gemmes straks i databasen.**

<!-- -->

  
**Denne proces hjælper dig med at gemme en kopi af dine data i et af de mange formater, der understøttes af Gramps. Dette kan bruges til at lave en kopi af dine data, sikkerhedskopiere dine data eller konvertere dem til et format, der giver dig mulighed for at overføre dem til et andet program.**

<!-- -->

  
**Hvis du ombestemmer dig under denne proces, kan du trygt trykke på knappen Annuller når som helst, og din nuværende database vil stadig være intakt.**

Vælg knappen for at fortsætte.

{{-}}

#### Vælg format for uddata <span id="Choose the output format"></span>

![[_media/ExportAssistant-ChooseTheOutputFormat-wizard-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Eksportassistent - Vælg outputformat - guidedialog]]

Vælg det filformat, dine data skal eksporteres til:

- [Regneark med kommaseparerede værdier (CSV)](#Comma_Separated_Values_Spreadsheet.28CSV.29_export)

- [GEDCOM](#GEDCOM_export)

- [GeneWeb](#GeneWeb_export)

- **Gramps [XML](wiki:Gramps_XML) (slægtsbog)**(standard)

- Gramps [XML](wiki:Gramps_XML) Pakke (slægtsbog og medier)

- [Web-slægtsbog](#Web_Family_Tree_export)

- [vCalendar](#vCalendar_export)

- [vCard](#vCard_export)

Vælg derefter knappen for at fortsætte. {{-}}

#### Eksport-indstillinger <span id="Export options"></span>

![[_media/ExportAssistant-ExportOptions-CSV-defaults-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Eksportassistent - Eksportindstillinger - guidedialog (viser standardindstillinger for "Kommaseparerede værdier Regneark (CSV)") med nederste sektion for filformatspecifikke indstillinger]]

Efter du har justeret dine indstillinger i de to sektioner.

- Øverste umærkede sektion: [Filtre og privatliv](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees#Filters_and_privacy)
- Nederste umærkede sektion: [Filformatspecifikke indstillinger](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees#File_format_specific_export_options)

Foretag de nødvendige ændringer, og vælg derefter knappen for at fortsætte.

{{-}}

##### Filtre og privatliv

I den øverste umærkede sektion giver Gramps dig mulighed for at eksportere din valgte slægtsbog til almindelige filformater.

Følgende filtre giver dig muligheder, der giver dig mulighed for at finjustere din eksport.

Filtre giver dig mulighed for at eksportere en begrænset mængde data baseret på de kriterier, du vælger.

###### Privatlivsfilter:

  
Markér dette felt for at forhindre, at ![[_media/22x22-gramps-lock.png]][private](wiki:Gramps_Glossary#private) poster inkluderes i den eksporterede fil. (Afkrydsningsfelt markeret som standard)

###### Levende filter:

Disse muligheder begrænser data og hjælper med at begrænse de oplysninger, der eksporteres for levende personer. Det betyder, at alle oplysninger om deres fødsel, død, adresser, vigtige begivenheder osv. vil blive udeladt i den eksporterede fil. For eksempel kan du vælge at erstatte ordet **Levende** med fornavnet (se dine [indstillinger](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Text)); du kan ekskludere noter; og du kan ekskludere kilder til [levende personer](wiki:Gramps_6.0_Wiki_Manual_-_Probably_Alive).

Nogle gange er det ikke altid tydeligt ud fra dataene, om nogen rent faktisk er i live. Gramps bruger en avanceret algoritme til at forsøge at bestemme [om en person stadig kunne være i live](wiki:Gramps_6.0_Wiki_Manual_-_Probably_Alive). Husk, at Gramps laver sit bedste gæt, og det er ikke altid muligt at gætte korrekt hele tiden. Dobbelttjek venligst dine data.

Vælg mellem følgende muligheder:

- (standard)

- 

- 

- 

###### Personfilter:

Vælg mellem følgende muligheder:

- (standard)

- 

- 

- 

- 

- Opret et brugerdefineret filter ved at vælge *Rediger-ikonet* for at vise dialogboksen .

###### Notefilter:

Vælg mellem følgende muligheder:

- (standard)

- Opret et brugerdefineret filter ved at vælge *Rediger-ikonet* for at vise dialogboksen .

###### Referencefilter:

Vælg mellem følgende muligheder:

- (standard)

- 

##### Filformatspecifikke eksportmuligheder

Den nederste umærkede sektion vises kun afhængigt af det valgte filformat. Du kan finde en række filformatspecifikke eksportmuligheder at vælge imellem under sektionen *[Filtre og privatliv](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees#Filters_and_privacy)*.

Se det relevante afsnit for hvert af de anførte filformater, der har specifikke eksportmuligheder:

- [Kommaseparerede værdier regneark (CSV)](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees#Comma_Separated_Values_Spreadsheet.28CSV.29_export)
- [Gramps XML (slægtsbog)](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees#Gramps_XML_.28family_tree.29_export)

#### Vælg en udfil <span id="Select save file"></span>

![[_media/ExportAssistant-SelectSaveFile-example-60.png|højre|tommelfinger|450px|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Eksportassistent - "Vælg gem fil" - guidedialog - eksempel]]

Indtast en eksportfil `Untitled_1.`<filformatudvidelse>(standard) og vælg den mappeplacering, hvor eksportfilen skal gemmes (normalt din **Dokumenter**-mappe).

Vælg derefter knappen for at fortsætte.

Hvis du ikke har tilladelse til at gemme filen på den placering, vil du se advarselsdialogboksen og derefter guidedialogboksen Eksportassistenter . Vælg knappen og start eksporten igen, denne gang med en passende mappe. {{-}}

#### Endelig bekræftelse <span id="Final confirmation"></span>

![[_media/ExportAssistant-FinalConfirmation-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Eksportassistent - Endelig bekræftelse - guidedialog - eksempel]]

Guiden Eksportassistenter giver dig mulighed for at kontrollere de opsummerede detaljer (Format/Navn/Mappe) for den eksportfil, der skal oprettes.

På dette tidspunkt kan du trykke på for at gennemgå dine muligheder igen eller for at afbryde.

Eller vælg knappen for at fortsætte. {{-}}

#### Opsummering <span id="Summary"></span>

![[_media/ExportAssistant-YourDataHasBeenSaved-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Eksportassistent - Oversigt - guidedialog - eksempel]]

Guiden Eksportassistenter viser *Filnavn:* og bekræfter, at dine eksporterede data er blevet gemt, og viser en påmindelse om den placering, hvor filen blev gemt.

Vælg knappen for at afslutte Eksportassistenten. {{-}}

### Kommaseparerede værdier Regneark (CSV) eksport <span id="Comma Separated Values Spreadsheet(CSV) export"></span>

![[_media/ExportAssistant-ExportOptions-CSV-defaults-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Eksportassistent - Eksportindstillinger - guidedialog (viser standardindstillinger for "Kommaseparerede værdier Regneark (CSV)") med nederste sektion for filformatspecifikke indstillinger]]

Kommaseparerede værdier Regneark (CSV): Tillader eksport (og import) af et delmængde af dine Gramps-data i et simpelt regnearksformat.

Se [CSV Import og eksport](wiki:Da:Gramps_6.0_brugsanvisning_-_CSV_Import_og_Export) for yderligere information og eksempler.

Kommaseparerede værdier Regneark (CSV) har følgende [filformatspecifikke eksportindstillinger](#File_format_specific_export_options):

- \-

- \-

- \-

- \-

- \- om overskrifter skal oversættes til det sprog, der aktuelt bruges.

{{-}} Se også [Eksporter (liste)visning](wiki:Gramps_6.0_Wiki_Manual_-_Settings/da#Export_View) som regneark.

### GEDCOM-eksport <span id="GEDCOM export"></span>

Gramps giver dig mulighed for at eksportere en database til det almindelige, ældre -format.

-eksport har ingen [filformatspecifikke eksportindstillinger](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees#File_format_specific_export_options), men du kan ændre følgende:

- Sørg for at tilføje dine oplysninger for at oprette en gyldig GEDCOM-fil. Dette kan også gøres med værktøjet .

For mere information om GEDCOM-formatet, se:

- <https://en.wikipedia.org/wiki/GEDCOM>
- <https://www.familysearch.org/developers/docs/guides/gedcom>
- <https://www.familysearch.org/developers/docs/gedcom/>

Se [Gramps og GEDCOM](wiki:Gramps_og_GEDCOM) for detaljer om data, der ikke eksporteres ved eksport til GEDCOM (). {{-}}

### GeneWeb-eksport <span id="GeneWeb export"></span>

-eksport gemmer en kopi af dine data i GeneWeb-slægtsbogsformatet.

For at finde ud af mere om GeneWeb og dets format, besøg:

- <http://www.geneweb.org>

har ingen [filformatspecifikke eksportmuligheder](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees#File_format_specific_export_options) {{-}}

<span id="Eksporter til Gramps-formater"></span>

### Gramps XML (slægtsbog) eksport <span id="Gramps XML (family tree) export"></span>

thumb\|450px\|Fig. {{#var:kapitel}}.{{#vardefineecho:figure\|{{#expr:{{#var:figure}}+1}}}} Eksportassistent - Eksportindstillinger - guide (viser standardindstillinger for "Gramps XML (slægtsbog)") Nederste sektion viser filformatspecifik indstilling "\[x\]Brug komprimering"\]\]

eksport (.gramps): Dette format er standardformatet til dataudveksling og sikkerhedskopier (se det relaterede .gpkg-format nedenfor for fuld portabilitet inklusive medieobjekter). Eksport til Gramps [XML](wiki:XML)-format vil producere en portabel database. Da XML er et tekstbaseret, menneskeligt læsbart format, kan du også bruge det til at se på dine data. Gramps garanterer, at du kan åbne XML-output fra ældre versioner af Gramps i nyere versioner af Gramps (dog ikke omvendt!).

Hvis en mediefil ikke findes under eksport, vil du se den samme dialogboks, som du støder på ved GEDCOM-eksport.

har følgende [filformatspecifikke eksportmuligheder](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees#File_format_specific_export_options):

- \- mulighed for at tillade Gramps at eksportere en .gramps-fil uden at komprimere filen. (Afkrydsningsfeltet er som standard markeret)

{{-}}

#### Hvad er ikke inkluderet: <span id="What's not included:"></span>

### Gramps XML-pakke (slægtsbog og medier) eksport <span id="Gramps XML Package (family tree and media) export "></span>

eksport (.gpkg): Eksport til Gramps-pakkeformatet opretter en komprimeret fil, der indeholder Gramps XML-databasen og kopier af alle tilknyttede mediefiler. Dette er nyttigt, hvis du vil flytte din database til en anden computer eller dele den med nogen.

Hvis en mediefil ikke findes under eksport, vil du se den samme dialogboks, som du støder på ved GEDCOM-eksport.

har ingen [filformatspecifikke eksportmuligheder](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees#File_format_specific_export_options)

#### Hvad er ikke inkluderet:

### Web Family Tree export

eksport opretter en tekstfil, der kan bruges af programmet **Web Family Tree**.

For at finde ud af mere om Web Family Tree og dets format, besøg

- [`http://www.simonward.com/cgi-bin/page.pl?family/tree`](http://www.simonward.com/cgi-bin/page.pl?family/tree) - [linkrot](https://wikipedia.org/wiki/Link_rot). *se* [2016 **Internet Archive** snapshot](https://web.archive.org/web/20160316080343/http://www.simonward.com/cgi-bin/page.pl?family/tree)

har ingen [filformatspecifikke eksportmuligheder](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees#File_format_specific_export_options) {{-}}

### vCalendar-eksport <span id="vCalendar export"></span>

-eksport gemmer oplysninger i det format, der bruges i mange kalenderprogrammer, nogle gange kaldet PIM for Personal Information Manager.

For mere information om vCalendar-formatet, se:

- <https://en.wikipedia.org/wiki/ICalendar#vCalendar_1.0>

har ingen [filformatspecifikke eksportmuligheder](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees#File_format_specific_export_options) {{-}}

### vCard-eksport <span id="vCard export"></span>

-eksport gemmer information i et format, der bruges i mange adressebogsprogrammer, nogle gange kaldet PIM for Personal Information Manager.

For mere information om vCard-formatet, se:

- <https://en.wikipedia.org/wiki/VCard>

har ingen [filformatspecifikke eksportmuligheder](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees#File_format_specific_export_options) {{-}}

[Category:Documentation](wiki:Category:Documentation)
