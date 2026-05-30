---
title: Da:Gramps 6.0 brugsanvisning - FAQ
categories:
- Documentation
managed: false
source: wiki-scrape
wiki_revid: 129586
wiki_fetched_at: '2026-05-30T16:36:06Z'
lang: da
---

{{#vardefine:chapter\|A}} {{#vardefine:figure\|0}}

Appendiks A: FAQ

Dette bilag indeholder listen over **Ofte Stillede Spørgsmål** (FAQ), der gentagne gange dukker op på mailinglister og diskussionsfora.

Denne liste er på ingen måde komplet. Hvis du ønsker at tilføje spørgsmål/svar til denne liste, bedes du [tilmelde dig](wiki:Kontakt#Mailing_lister) og sende dine forslag til mailinglisten `gramps-devel@lists.sourceforge.net`.

Overvej også at se på følgende kategorier på Gramps-wikien:

- [Hvordan gør jeg...](wiki::Category:How_do_I...)
- [Gramps-vejledninger](wiki::Category:Tutorials)

Du kan finde det nyttigt at gennemgå

- [Gramps Ordliste](wiki::Gramps_Glossary/da) - giver et overblik over termer, der forekommer i Gramps
- [Genealogisk Ordliste](wiki::Genealogy_Glossary/da) - genealogiske termer og betydninger.

## Generelt <span id="General"></span>

### Hvad er Gramps? <span id="What is Gramps?"></span>

Gramps er en pakke af personlige slægtsforskningsværktøjer, der giver dig mulighed for at gemme, redigere og undersøge slægtsforskningsdata. Det hjælper dig med at sortere de komplekse relationer mellem forskellige personer, steder og begivenheder. Gramps giver dig mange forskellige måder at registrere de mange detaljer i en persons liv, og al din forskning holdes organiseret og søgbar. Se [Om](wiki:Gramps:Om).

### Hvor får jeg det, og hvor meget koster det?

Gramps kan [installeres](wiki:Installation) gratis. Gramps er et Open Source-projekt, der er dækket af GNU General Public License. Du har fuld adgang til kildekoden og har tilladelse til at distribuere programmet og kildekoden frit.

### Skal jeg registrere mig som bruger for at bruge Gramps? Jeg er ikke programmør?

Nej, registrering er kun nødvendig, hvis du vil indsende en fejlrapport (eller en funktionsanmodning) eller redigere/skrive en wikiside.

Ingen programmeringsfærdigheder kræves til det.

### Findes Gramps på andre sprog?

Ja, ved udgivelsen af ​​Gramps 6.0 er det blevet oversat til 28 sprog, se [Gramps translations](wiki:Gramps_translations).

### Hvordan opbevarer jeg sikkerhedskopier?

Automatisk sikkerhedskopiering er en standardfunktion, der beskytter dine genealogiske data i Gramps. (Den blev automatiseret i 2018 med udgivelsen af ​​version 6.0.) Intervallet, stien til sikkerhedskopieringsfilen og muligheden for at sikkerhedskopiere, når Gramps-indstillingerne forlades, findes i fanen i menuen . Derudover kan en sikkerhedskopi manuelt vælges fra vinduet .

Det er ekstremt vigtigt at opbevare sikkerhedskopier af dine data og opbevare dem et sikkert sted. Gramps har et specifikt bærbart filformat, der er lille og menneskeligt læsbart, betegnet med `.gramps`. Se afsnittet "[sikkerhedskopier en slægtsbog](wiki:Gramps_6.0_Wiki_Manual_-_Administrer_Familietræer#Sikkerhedskopier_en_slægtsbog)" i manualen. Det er også vigtigt at være opmærksom på [hvad der udelades fra en Gramps-sikkerhedskopi](wiki:Template:Backup_Omissions).

Du kan kopiere denne sikkerhedskopifil fra tid til anden til et sikkert sted (<abbr title="exempli gratia - latinsk frase, der betyder 'for eksempel'">f.eks.</abbr> et USB-stik). \[Bemærk: `.gramps`-filerne er som standard komprimerede. Hvis du klikker på dem, åbnes Gramps. For at se XML-filen skal du vælge `.gramps`-filen og åbne den med et dekomprimeringsværktøj (som ark, gunzip, 7-zip), hvorefter du kan udpakke XML-tekstfilen, som er menneskelig læsbar. Se [details](wiki:Generate_XML#How_do_I_uncompress_the_file?).

Gramps laver en hurtig skjult binær backup for at tillade gendannelse, hvis der opdages en fejl. Hvis den korrekte pakke er installeret, kan du bruge et revisionssystem.

En anden metode er at sikkerhedskopiere den skjulte mappe *`/.gramps`*. Denne undermappe er placeret i din [brugermappe](wiki:Gramps_6.0_Wiki_Manual_-_User_Directory). Sikkerhedskopiering af denne mappe vil sikkerhedskopiere dine databaser og revisioner. (På Windows 10 er det *`/Brugere/`<dit brugernavn>`/AppData/Roaming/gramps`*)

**Gem ikke sikkerhedskopier i GEDCOM-format**. Ikke alle oplysninger, som Gramps gemmer, kan skrives i GEDCOM. Derfor vil en eksport/import-handling fra Gramps, der eksporteres til GEDCOM og genimporteres til Gramps, betyde, at du **mister** [data](wiki:Gramps_og_GEDCOM). Brug filformatet `.gramps` til sikkerhedskopier!

**Gem ikke sikkerhedskopier i GRDB-format**. GRDB er en database, som kan være computerafhængig (læses, fungerer ikke på en anden pc). Små skader på en GRDB-fil kan heller ikke repareres. Brug filformatet `.gramps` til sikkerhedskopier!

### Understøtter Gramps Unicode-skrifttyper?

Især, understøttes ikke-romerske Unicode-skrifttyper? Ja. Gramps fungerer internt med Unicode (UTF-8), så alle alfabeter kan bruges i alle indtastningsfelter.

Der er ingen særlig hjælp til at indtaste Unicode-symboler (glyffer), der ikke er direkte markeret på dit tastatur. Hjælpemidler til [prækomponerede tegn](https://wikipedia.org/wiki/Precomposed_character) (også kendt som sammensatte tegn eller dekomponerbare tegn) med diakritiske tegn er tilgængelige uden for programmet. Du kan finde de forskellige sprogspecifikke [flersprogede virtuelle tastaturer på Lexilogos' hjemmeside](https://www.lexilogos.com/keyboard/latin_alphabet.htm) nyttige.

Alle rapporter understøtter fuldt ud Unicode, [selvom du for PDF/PS](#Why_are_non-Latin_characters_displayed_as_garbage_in_PDF.2FPS_reports.3F) skal arbejde med gnome-print eller [1](http://www.documentfoundation.org/download/LibreOffice).

## Installation

### Hvad skal der bruges til at installere Gramps under Linux, Solaris eller FreeBSD?

Gramps er et [GTK](http://en.wikipedia.org/wiki/Gtk)-program. Gramps skal have [PyGObject](http://en.wikipedia.org/wiki/PyGObject)-bibliotekerne installeret på systemet. Så længe disse biblioteker er installeret, burde Gramps fungere. Det vil fungere under GNOME-skrivebordet, KDE-skrivebordet eller ethvert andet skrivebord. Hvis GNOME-bindingerne til Python er installeret på systemet, vil Gramps have yderligere funktionalitet. Kontroller venligst, at det overholder Gramps-projektets anbefalinger vedrørende den GTK-version, der skal bruges.

### Virker Gramps på Windows?

Ja, Windows er en fællesskabsstøttet platform til Gramps.

Du kan [downloade](wiki:Download#MS_Windows) [All In One Gramps Software Bundle for Windows](wiki:All_In_One_Gramps_Software_Bundle_for_Windows) (GrampsAIO).

Vi vil gøre vores bedste for at løse alle rapporterede Windows-relaterede problemer. Se [her](wiki:Contact).

### Virker Gramps på Mac?

Ja, macOS er en fællesskabsstøttet platform til Gramps.

Du kan [downloade](wiki:Download#macOS) macOS-versionen.

Vi vil gøre vores bedste for at løse alle rapporterede Apple macOS-relaterede problemer. Se [Kontakt Gramps](wiki:Contact).

Se også [macOS programpakke](wiki:Mac_OS_X:Application_package).

### Virker Gramps på min mobilenhed?

Det korte svar er nej, Gramps kan ikke installeres på din mobiltelefon eller tablet ([Google Android](https://en.wikipedia.org/wiki/Android_(operating_system)) eller [Apple iOS](https://wikipedia.org/wiki/IOS))

Det mere tekniske svar er 'ja', men ***ikke**' som en***native**' applikation. Brug af Gramps kræver enten:

:# installer en version af Linux-operativsystemer på den mobile enhed sammen med alle supportpakkerne, eller

:# opsæt en lokal eller online server med en fork af [Gramps designet til samarbejde](wiki:Web_Solutions_for_Gramps#Interactive_web_apps) (såsom [Gramps Web](wiki:Web_Solutions_for_Gramps#GrampsWeb)) og arbejd derefter med Gramps via browsing

### Virker Gramps på min Google Chromebook?

Du kan, men med et par problemer, installere Gramps på din [Chromebook](https://en.wikipedia.org/wiki/Chromebook) ([ChromeOS](https://en.wikipedia.org/wiki/ChromeOS)).

Se:

- Træk og slip virker ikke i Crostini\[Linux\] på en Pixelbook

### Hvad er minimumskravene for at køre Gramps?

Vi vil anbefale mindst en 1920x1080 videoskærm. De tidlige hukommelseskrav til Gramps er blevet reduceret, og Gramps var ret høje. Fra og med Gramps 3.0 kunne softwaren køre ret effektivt på et 256 MB system og rumme betydeligt flere personer. Et system med 512 MB burde kunne rumme omkring 200.000 personer. Diskpladskravene til databaser er dog betydeligt større, idet en typisk database er flere megabyte stor. For 120.000 personer skal du allerede overveje 530 MB til databasen. Billeder gemmes separat på disken, så en stor harddisk er nødvendig.

<span id="Hvordan opgraderer jeg GRAMPS?">

### Hvordan opgraderer jeg Gramps?

</span> Opgraderinger starter med at lave [sikkerhedskopier](wiki:Sådan_gør_du_sikkerhedskopi) af ALLE dine træer. Men derudover skal du se på listen [Udeladelse af_sikkerhedskopi](wiki:Skabelon:Udeladelser_af_sikkerhedskopi) for at bestemme de tilføjelser, du måske vil arkivere. (De vigtigste punkter er at notere databasestien, sikkerhedskopiestien og den relative mediesti i Indstillinger. Hvis du ikke kan finde dine data efter en opgradering, vil du være meget utilfreds.)

Når sikkerhedskopier er gemt sikkert, er den sikreste fremgangsmåde til opgradering: at downloade det nyeste installationsprogram, afinstallere det eksisterende Gramps og geninstallere fra installationsprogrammet.

Start Gramps (den første indlæsning vil være langsom, da den genkompilerer og cacher Python-kildekodefilerne). I "Rediger -\> Indstillinger..." skal du indtaste din mediesti på fanen Generelt, databasestien på fanen Slægtstræ, sikkerhedskopi på fanen Slægtstræ. Prøv at indlæse dit træ via menuen Slægtstræer.

Hvis dette var en 'mindre' opdatering (som kun indeholdt fejlrettelser), burde opdateringen finde din konfiguration og dine tilføjelser uden yderligere besvær. Hvis det var en opgradering, skal du nulstille alle dine konfigurationstilpasninger og downloade de kompatible tilføjelser.

## Præferencer <span id="Preferences"></span>

### Kan jeg ændre datoerne i rapporter til 'dag måned år'?

Ja, i indstillingerne ( fanen) skal du ændre indstillingen for Gramps til det ønskede format (f.eks. ÅÅÅÅ-MM-DD eller dag måned år), og oprette rapporten. Dine globale datoindstillinger vil blive brugt.

### Er der en mørk tilstand?

Kun ved at installere [Tema-tilføjelsen](wiki:Addon:ThemePreferences), der tilføjer en -fane til . Denne tilføjelse er nyttig, hvis du har problemer med lysfølsomhed, og/eller hvis du foretrækker en mørk tilstand til natbrug eller bare generelt. I fanen Tema kan du aktivere indstillingen "", som er tilgængelig for de fleste temaer. Du kan også øge skriftstørrelsen for at minimere træthed under læsning.

## Samarbejde - Portabilitet <span id="Collaboration-Portability"></span>

### Er Gramps kompatibel med anden genealogisk software?

Gramps gør alt for at opretholde kompatibilitet med [GEDCOM](wiki:GEDCOM), den generelle standard for registrering af genealogisk information. Vi har import- og eksportfiltre, der gør det muligt for Gramps at læse og skrive GEDCOM-filer.

Det er vigtigt at forstå, at GEDCOM-standarden er dårligt implementeret -- stort set al genealogisk software har sin egen "variant" af GEDCOM. Efterhånden som vi lærer om nye varianter, kan import-/eksportfiltrene oprettes meget hurtigt. Det kræver dog [brugerfeedback](wiki:Contact) at finde ud af mere om de ukendte varianter. Du er velkommen til at informere os om enhver GEDCOM-variant, der ikke understøttes af Gramps, og vi vil gøre vores bedste for at understøtte den!

Der er en specifik artikel på denne wiki, der diskuterer [Gramps og GEDCOM](wiki:Gramps_and_GEDCOM). Der er også en artikel om de kendte særheder ved [GEDCOM-dialekter, når man importerer fra et andet program](wiki:Import_from_another_genealogy_program).

### Kan Gramps læse filer oprettet af andre slægtsforskningsprogrammer?

Ja, Gramps kan læse GEDCOM-filer oprettet af andre slægtsforskningsprogrammer.

- [Se ovenfor.](wiki:Da:Gramps_6.0_brugsanvisning_-_FAQ#Er_Gramps_kompatibel_med_anden_genealogisk_software.3F)

### Kan Gramps skrive filer, der kan læses af andre slægtsforskningsprogrammer?

Ja, Gramps kan skrive GEDCOM-filer, der skal læses af andre slægtsforskningsprogrammer.

- [Se ovenfor.](wiki:Gramps_6.0_Wiki_Manual_-_FAQ#Is_Gramps_compatible_with_other_genealogical_software.3F)

### Hvilke standarder understøtter Gramps?

Det gode ved standarder er, at der aldrig er mangel på dem. Gramps er testet til at understøtte følgende varianter af GEDCOM 5.6.0, Brother's Keeper, Family Origins, Family Tree Maker, Ftree, GeneWeb, Legacy, Personal Ancestral File, Pro-Gen, Reunion og Visual Genealogie.

### Hvordan importerer jeg data fra et andet slægtsforskningsprogram til Gramps?

Den bedste måde er at oprette et nyt slægtstræ og vælge importindstillingen i filmenuen. Her vælger du den GEDCOM, du genererede med det andet program, og importerer den.

### Kan jeg installere Gramps på en Linux-webserver og bruge den via en webbrowser?

Dette ville gøre det muligt for mine slægtninge verden over at få adgang til og opdatere den.

Selvom Gramps kan generere websteder, tilbyder den ikke en webgrænseflade, der tillader redigering. Hvis dette er et krav, er [GeneWeb](http://geneweb.org) eller [webtrees](http://www.webtrees.net/) programmer, der er mere tilbøjelige til at opfylde dine behov. Se også på eksperimentelle [gramps-online](https://github.com/gramps-project/gramps-online). Du kan dog stille dig selv følgende spørgsmål:

1.  Ønsker jeg virkelig, at slægtninge eller andre personer direkte redigerer min slægtsdatabase?
2.  Stoler jeg implicit, uden verifikation, på data, som folk måtte indtaste?
3.  Har disse personer den samme forståelse af god slægtsforskningspraksis, som jeg har?

En bedre fremgangsmåde kan være at tilbyde en webformulargrænseflade, der giver andre mulighed for at indtaste data, som derefter opbevares til din undersøgelse. Du kan derefter beslutte, om oplysningerne skal indtastes i din database.

Du kan også overveje virkningerne af mulig nedetid på dit websted, hvis du ikke har råd til en premium webhosting-tjeneste.

## Rapporter <span id="Reports"></span>

### Kan Gramps udskrive et slægtstræ for min familie?

Ja. Forskellige mennesker har forskellige ideer om, hvad et slægtstræ er. Nogle tænker på det som et diagram, der går fra den fjerne forfader og viser alle hans/hendes efterkommere og deres familier. Andre mener, at det skal være et diagram, der går fra personen tilbage i tiden og viser forfædrene og deres familier. Andre igen tænker på en tabel, tekstrapport osv.

Bestefar kan producere alle ovenstående og mange flere forskellige diagrammer og rapporter. Desuden giver plugin-arkitekturen brugerne (dig) mulighed for at oprette deres egne plugins, som kan være nye rapporter, diagrammer eller forskningsværktøjer.

### Hvordan kan forholdet mellem personer på træet bestemmes?

Nogle brugere er interesserede i kun at vise direkte genetiske relationer mellem forfædre eller efterkommere. Andre brugere er også interesserede i sidelinjer (kusiner!) eller nærmeste svigerfamilie. Og andre brugere er interesserede i, hvordan de mest indirekte forbindelser påvirker et fællesskab.

Gramps tilbyder derfor et konstant voksende udvalg af værktøjer, rapporter og metoder til at bestemme, hvordan personer er forbundet i et træs database. Efter en diskussion på Gramps-brugeren [Mailliste](wiki:Kontakt#Mailinglister) er de indsendte forslag blevet samlet og uddybet i artiklen "[Sådan finder du forholdet mellem personer](wiki:Sådan_finder_du_forholdet_mellem_personer)" i wikikategorien "[Hvordan...](wiki::Kategori:Hvordan...)".

### I hvilke formater kan Gramps udskrive sine rapporter?

Tekstrapporter er tilgængelige i HTML-, PDF-, ODT-, LaTeX- og RTF-formater. Grafiske rapporter (diagrammer og diagrammer) er tilgængelige i PostScript-, PDF-, SVG-, ODS- og [GraphViz](wiki:Output_formats#Graphviz)-formater.

### Hvordan kan jeg ændre standardsproget i rapporter?

Rapporterne er på det sprog, der er anvendt i din installation. De fleste rapporter giver dig mulighed for at vælge det sprog, der skal vises, for at søge efter muligheden for at vælge den oversættelse, der skal bruges til rapporten. Du kan ændre det ved at installere ekstra sprogpakker, se [Sådan:Skift sprog i rapporter](wiki:Sådan:Skift_sprog_i_rapporter).

### Er Gramps kompatibel med internettet?

Ja, på en række forskellige måder. Der er funktioner til at referere til hot-linkede eksterne data, arkiveringsværktøjer til at indsamle dem til intern lagring, og selvom Gramps er designet til at være en lokal applikation, er der skabt et omfattende sæt værktøjer til at udgive noget af eller al din forskning på internettet.

Gramps kan gemme webadresser og dirigere din browser til dem. Det kan importere data, som du downloader fra internettet. Det kan eksportere data, som du kan sende via internettet. Gramps er bekendt med de standardfilformater, der er meget udbredt på internettet (<abbr title="exempli gratia - latinsk frase, der betyder 'for eksempel'">f.eks.</abbr> JPEG-, PNG- og GIF-billeder, MP3-, OGG- og WAV-lydfiler, QuickTime-, MPEG- og AVI-filmfiler osv.). Hvis din browser er konfigureret til at få adgang til andre filtyper, vil Gramps arve denne mulighed.

Der findes tilføjelsesværktøjer til Finding Aid, der kan hjælpe med at søge efter poster i onlinekilder. Der er et stigende udvalg af andre [Webløsninger til Gramps](wiki:Web_Solutions_for_Gramps).

Rapporterne kan eventuelt generere indhold i formater, der er egnede til offentliggørelse som websider eller endda som hele websteder. Og der findes udviklingsforks, der udvider Gramps til online genealogiske indholdsstyringssystemer. Nogle er dynamiske præsentationssystemer til offentliggørelse af forskning, andre tilbyder begrænset samarbejdsredigering.

#### Se også

- [Webløsninger til Gramps](wiki:Web_Solutions_for_Gramps)

### Kan jeg oprette brugerdefinerede rapporter/filtre/hvad som helst?

Ja. Der er mange niveauer af tilpasning. Et er at oprette eller ændre de skabeloner, der bruges til rapporterne. Dette giver dig en vis kontrol over skrifttyper, farver og layout i rapporterne. Du kan også bruge Gramps-kontroller i rapportdialogboksene til at angive, hvilket indhold der skal bruges til en bestemt rapport. Derudover har du mulighed for at oprette dine egne filtre -- dette er nyttigt til at vælge personer baseret på kriterier, du har angivet. Du kan kombinere disse filtre for at oprette nye, mere komplekse filtre. Endelig har du mulighed for at oprette dine egne plugins. Disse kan være nye rapporter, forskningsværktøjer, import-/eksportfiltre osv. Dette forudsætter en vis viden om programmering i Python.

### Hvorfor vises ikke-latinske tegn som skrald i PDF/PS-rapporter?

Dette er en begrænsning af de indbyggede skrifttyper i PS- og PDF-formater. For at udskrive ikke-latinsk tekst skal du bruge Udskriv... i formatvalgsmenuen i rapportdialogboksen. Dette vil bruge `gnome-print`-backend, som understøtter PS- og PDF-oprettelse samt direkte udskrivning. (Bemærk: Du skal muligvis installere gnome-print separat, da det ikke er påkrævet for Gramps).

Hvis du kun har latinsk tekst, vil PDF-indstillingen producere en mindre PDF sammenlignet med den, der oprettes af gnome-print, simpelthen fordi der ikke vil blive integreret nogen skrifttypeoplysninger.

### Jeg vil gerne bidrage til Gramps ved at skrive min yndlingsrapport. Hvordan gør jeg det?

Den nemmeste måde at bidrage til rapporter, filtre, værktøjer osv. er at kopiere en eksisterende Gramps-rapport, et filter eller et eksisterende Gramps-værktøj. Hvis du kan oprette det, du ønsker, ved at ændre eksisterende kode -- fantastisk! Hvis din idé ikke passer ind i logikken i et eksisterende Gramps-værktøj, skal du skrive dit eget plugin fra bunden. Hjælp er tilgængelig på [Developers Portal](wiki:Portal:Developers) eller på [Developers mailinglisten](wiki:Contact): gramps-devel@lists.sourceforge.net.

For at teste dit igangværende arbejde kan du gemme dit plugin under mappen `$HOME/.gramps/plugins`, og det burde blive fundet og importeret ved opstart. Det korrekt skrevne tilføjelses-/plugin vil registrere sig selv hos Gramps, oprette et menupunkt osv.

Hvis du er tilfreds med dit tilføjelses-/plugin og gerne vil bidrage med din kode tilbage til Gramps-projektet, er du meget velkommen til at gøre det ved at tilmelde dig og kontakte os på mailinglisten gramps-devel@lists.sourceforge.net.

## Database - Gramps filformater <span id="Database - Gramps file formats"></span>

Standardfilformatet er [Gramps XML](wiki:Gramps_XML). Det bruges til eksport, sikkerhedskopiering og import, og det bevarer dine indtastede genealogiske data uden datatab sammenlignet med GEDCOM-formatet.

### Hvad er den maksimale databasestørrelse (bytes), som Gramps kan håndtere?

Gramps har ingen hårde grænser for størrelsen på en database, den kan håndtere. Fra og med 2.0.0-udgivelsen indlæser Gramps ikke længere alle data i hukommelsen, hvilket gør det muligt at arbejde med en meget større database end før. I virkeligheden er der dog praktiske begrænsninger. De vigtigste begrænsende faktorer er den tilgængelige hukommelse på systemet og cachestørrelsen, der bruges til BSDDB-databaseadgang. Med almindelige hukommelsesstørrelser i disse dage burde Gramps ikke have noget problem med at bruge databaser med [Millioner af mennesker](wiki:Gramps_Performance#JohnBoyTheGreat_2019-12.2C_version_6.0.1).

### Hvor mange mennesker kan Gramps-databasen håndtere?

Se ovenfor. Igen afhænger dette af, hvor meget hukommelse og lagerplads din computer har. Se [Gramps Performance](wiki:Gramps_Performance).

### Min database er virkelig stor. Er der en måde at undgå at indlæse alle data i hukommelsen?

Fra og med version 2.0.0 indlæser Gramps ikke længere alle data i hukommelsen, hvilket gør det muligt at arbejde med en meget større database end før. Det anvendte filformat er `.grdb`, hvilket betyder Gramps-database.

### Kan jeg køre Gramps fra en database på et NFS-share?

Ja, du kan køre en Gramps-database fra et [NFS(NetworkFile System)](https://en.wikipedia.org/wiki/Network_File_System)-share.

### Hvad betyder "bærbar"?

En Gramps 3-database (og enhver .grdb-fil) er meget afhængig af de softwareversioner, der har oprettet den. For eksempel kan du ikke bare flytte dine Gramps-data i disse formater til et andet operativsystem (eller endda en anden version af et operativsystem) og forvente, at du vil være i stand til at læse dine data. Dataene er ikke "bærbare". Derfor kan du ikke bare stole på sikkerhedskopier af disse formater, men du bør også lejlighedsvis eksportere til et format, der er bærbart. Der er to mulige bærbare formater: GEDCOM og Gramps XML (.gramps eller .gpkg). Men kun Gramps XML anbefales, da det gemmer alle dine data troværdigt.

### Hvorfor er databaseformatet (GRDB) ikke portabelt?

Det største problem med Gramps portabilitet ligger i 'transaktioner'. Med Gramps 2.2 har vi tilføjet understøttelse af atomare transaktioner for at beskytte data. Med atomare transaktioner foretages flere ændringer som en enkelt enhed. Enten foretager alle ændringerne det, eller også foretager ingen af ​​ændringerne det. Du er aldrig efterladt i en situation med et delvist sæt ændringer. En sidefordel ved at bruge transaktioner er, at databaseadgang (læsning og skrivning) er hurtigere.

Problemet med transaktioner (i det mindste ved brug af BSDDB) er, at det ikke tillader, at alle data gemmes i en enkelt fil. Logfiler er nødvendige for at holde styr på tingene. Disse logfiler opbevares i en databasemiljømappe. Vi har brug for en separat mappe til hver fil, ellers kan logfilerne forstyrre hinanden.

I 2.2 opbevarer vi logfilerne under mappen `~/.gramps/`, hvilket skaber en unik mappe for hver database. Problemet er, at din GRDB-fil har brug for logfilerne, som er i en anden mappe.

Kopiering af GRDB-filen kopierer kun en del af databasen.

### Har Gramps en eksempel-slægtsbog?

Ja, det har den. Adskillige eksempler på stamtrædatabaser er [inkluderet i de fleste installationer af Gramps og kan importeres](wiki:Example.gramps#Load_example.gramps) til at arbejde med vejledninger og til sikker udforskning af værktøjer eller funktioner.

Eksempeldatabasen med slægtsbogen (**`example.gramps`**-filen) forsøger idealet om at have mindst ét ​​eksempel på selv de obskure ting, som Gramps gør. Du kan importere eksemplet til et tomt træ og derefter sikkert lave destruktive udforskningsfejl på en engangsdatabase. Og når du har mistanke om, at du har opdaget et problem (også kendt som 'fejl') i Gramps, kan du først prøve den samme operation med eksempelslægtsbogen og derefter [indgive en fejlrapport](wiki:How_to_create_a_good_bug_report).

- Wiki-artiklen [<code>Example.gramps</code>](wiki:Example.gramps) beskriver, hvor man kan finde eksempel-slægtsbogsarkivfilen, hvordan man bruger den, og foreslår nogle alternative filer.

## Fejl og anmodninger <span id="Bugs and requests"></span>

### Hvad gør jeg, hvis jeg har fundet en fejl?

Du kan [indsende en fejlrapport.](wiki:Using_the_bug_tracker)

En god fejlrapport vil indeholde:

1.  Version af Gramps, du brugte, da du stødte på fejlen (tilgængelig via Hjælp → Om menupunktet).
2.  Sprog, som Gramps blev kørt under (tilgængelig ved at udføre `echo $LANG` i din terminal).
3.  Symptomer, der indikerer, at dette faktisk er en fejl.
4.  Eventuelle sporingsmeddelelser, fejlmeddelelser, advarsler osv., der blev vist i din terminal eller i et separat sporingsvindue.

De fleste problemer kan løses hurtigt, forudsat at der er tilstrækkelig information. For at sikre dette, bedes du følge op på dine fejlrapporter. Så vil vi have en måde at kontakte dig på, hvis vi har brug for flere oplysninger.

### Anmodninger

- Gramps bør være en ... type applikation

Det er indlysende, at Gramps absolut skal blive en (klient-server/webbaseret/PHP/weblog/Javascript/C++/distribueret/KDE/Motif/Tcl/Win32/C#/Du-nævner-det) applikation. Hvornår vil dette ske?

Den sikreste måde at se det ske på er at få det gjort selv. Da Gramps er gratis/open source, forhindrer ingen dig i at tage al koden og fortsætte dens udvikling i den retning, du finder passende. I den forbindelse kan du overveje at give dit nye projekt et andet navn for at undgå forvirring med den fortsatte Gramps-udvikling. Hvis du ønsker, at Gramps-projektet skal yde rådgivning, ekspertise, filtre osv., samarbejder vi gerne med dit nye projekt for at sikre kompatibilitet eller import-/eksportmuligheder til dit nye projektformat.

Hvis du derimod ønsker, at Gramps-projektet skal anvende din strategi, skal du overbevise Gramps-udviklerne om, at din strategi er god for Gramps og bedre end den nuværende udviklingsstrategi.

## Tilføjelse til og redigering af min database <span id="Adding to and editing my database"></span>

### Hvad er forskellen på en bopæl og en adresse?

En bopæl er et sted, hvor en person har boet i en periode. En adresse er navnet på en bopæl, formateret på den måde, der forventes af postsystemet. Derfor kan hver bopæl også have en adresse, hvis det er nyttigt. Se også: [Hvorfor bopælsbegivenhed og ikke Adresse?](wiki:Why_residence_event_and_not_Address%3F)

### Hvordan ændrer jeg rækkefølgen af ​​børn?

Børn kan flyttes i [Familie Editor](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1#Editing_information_about_relationships)'s [Børn](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1#Editing_information_about_relationships#Children) fanen ved at [trække og slippe](http://en.wikipedia.org/wiki/Drag-and-drop) eller bruge knapperne og .

### Hvordan ændrer jeg rækkefølgen af ​​ægtefæller?

Ægtefæller (også angivet som deres forhold eller som en familie i forskellige dele af wikien) kan omarrangeres fra visningen [Relationskategori](wiki:Gramps_6.0_Wiki_Manual_-_Categories#Reorder_Relationships_dialog) ved at vælge knappen i værktøjslinjen eller ved at vælge menupunktet . Alternativt viser fanen Begivenheder en sammenklappelig familie for hver ægtefælle, når du redigerer en person. Når der er flere familier, vil valg af en familie og klik på knappen Opad eller Nedad under fanebladsoverskrifterne omarrangere den valgte familie.

### Hvordan tilføjer jeg en ekstra ægtefælle?

Se [Tilføj en ægtefælle](wiki:Add_a_spouse)

### Hvordan fjerner jeg en ægtefælle?

Fjernelse af en ægtefælle (uden at slette personprofilen fra træet) kræver blot et enkelt klik i dialogboksen [Rediger familie](wiki:Gramps_Glossary/da#family). Klik blot på knappen "Fjern person som mor/far" (-) lige over ægtefællens navn.

*Navn, fødsel og død vil blive ryddet, og knapperne "Tilføj en ny person som mor/far" (+) og "Delt personvalg" vil erstatte knapperne (-) og "Rediger".*

For at fjerne ægtefællen helt fra træet skal du vælge personen i personvisningen og klikke på værktøjslinjens knap "Slet den valgte person" (-). En bekræftelsesdialogboks vises. Bekræft ved at klikke på knappen "Slet person".

*Personen vil blive fjernet fra alle familier, hvor de er en ægtefælle eller et barn. De vedhæftede begivenheder, citater, noter og medier vil blive forældreløse. De andre sekundære objekter vil blive slettet sammen med deres Person.*

### Hvordan tilføjer du fotos til et element?

Se [Tilføjelse af fotos og andre medieobjekter](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_brief#Adding_photos_and_other_media_objects).

### Hvordan finder du ubrugte medier?

Medier, der ikke er blevet tilknyttet nogen objekter, kan findes ved at oprette et [Brugerdefineret filter](wiki:Gramps_6.0_Wiki_Manual_-_Filters#Custom_Filters) i visningen Mediekategori. Brug reglen [Medieobjekter med et referenceantal på <count>](wiki:Gramps_6.0_Wiki_Manual_-_Filters#Media_objects_with_a_reference_count_of_.3Ccount.3E) til at finde medier med færre end 1 reference.

### Hvordan kan jeg udgive en slægtsforskningshjemmeside med Gramps?

<span id="Hvordan kan jeg udgive hjemmesider genereret af GRAMPS?"> Gramps har flere muligheder i rapportmenuen til at oprette websider baseret på dine trædata.

Tutorialen [Howto: Make a genealogy website with Gramps](wiki:Howto:_Make_a_genealogy_website_with_Gramps) beskriver brugen af ​​rapporten [Narrated Web Site](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_7#Narrated_Web_Site) (også kendt som NarrativeWeb). I den lærer du at generere en hjemmeside omkring en gruppe personer i dit slægtstræ.

Når de er genereret, kan du uploade webfilerne til en hostingtjeneste. Du kan også distribuere dem på et bærbart USB-drev eller andre medier.

#### Se også

- [Webløsninger til Gramps](wiki:Web_Solutions_for_Gramps)

</span>

- Du kan også installere tredjeparts tilføjelsesrapporter for at oprette andre typer webindhold. Se [Tilføjelsesliste](wiki:6.0_Addons#Addon_List).

{{-}}

## Denne FAQ løser ikke mit problem. <span id="The FAQ does not solve my problem."></span>

Du er velkommen til at kontakte os via en af ​​de officielle metoder, der er angivet på siden “[Contact](wiki:Contact)”. {{-}}

[Category:Documentation](wiki:Category:Documentation)
