---
title: Da:Gramps 6.0 brugsanvisning - Kom i gang
categories:
- Documentation
managed: false
source: wiki-scrape
wiki_revid: 129343
wiki_fetched_at: '2026-05-30T17:03:40Z'
lang: da
---

{{#vardefine:chapter\|2}} {{#vardefine:figure\|0}}

I dette afsnit begynder vi med det grundlæggende. Først beskriver vi de grundlæggende begreber i Gramps. Derefter viser vi dig, hvordan du starter Gramps, og hvordan du får hjælp, når du har brug for det. \_\_FORCETOC\_\_

## Oversigt over Gramps <span id="Overview of Gramps"></span>

Gramps er et gratis open source-program, der er designet til at være et fleksibelt og kraftfuldt slægtsforskningsværktøj. Det er en ramme til at indsamle slægtsdata, notere, hvordan hvert stykke data hænger sammen, og præsentere disse forhold.

Man kan generelt bruge Gramps, som man vil. Der er ikke nogen enkelt, korrekt metode til at arbejde med eller registrere dine data. Men hvis du ønsker at samarbejde med andre forskere eller programmer, hjælper det at følge nogle fælles retningslinjer. Selv om du er fortrolig med almindelig praksis inden for slægtsforskning, er du stadig nødt til at forstå, hvordan Gramps fungerer. Derefter kan du gå i gang med at bruge Gramps-programmet på en måde, der supplerer en bestemt slægtsforskningsstil.

Gramps opdeler alle slægtshistoriske oplysninger i 9 primære kategorier af emner:

- [Personer](wiki:Gramps_Glossary/da#person)

- [Familier](wiki:Gramps_Glossary/da#familie)

- [Begivenheder](wiki:Gramps_Glossary/da#event)

- [Steder](wiki:Gramps_Glossary/da#place)

- [Kilder](wiki:Gramps_Glossary/da#source)

- [Kildehenvisninger](wiki:Gramps_Glossary/da#citation)

- [Arkiver](wiki:Gramps_Glossary/da#repository)

- [Medier](wiki:Gramps_Glossary/da#media)

- [Noter](wiki:Gramps_Glossary/da#note)

Hver af disse består af selvstændige elementer. Det betyder, at du kan indtaste et element ad gangen i din slægtsbog og i den rækkefølge, du ønsker. Du kan forbinde elementerne med hinanden eller lade dem være adskilte (eller endda kaotisk uorganiserede), men søgbare. Eller du kan starte med et trædesign i tankerne og fylde det udad og forbinde nye elementer undervejs.

For eksempel vil du måske indtaste hvert personelement først og derefter forbinde dem ved at oprette familieelementer senere. Eller du kan starte med en familie, forankre familien ved at tilføje en ny person som barn eller forælder og derefter tilføje slægtninge, begivenheder og kildematerialer på de forberedte pladser i familierammen. Eller du kan starte med kildeelementer og kun oprette et personelement, når din forskning indeholder en omtale af en person. Eller du kan blande disse måder at indtaste data på ved at tilføje nogle note- og kildeelementer, derefter familieelementer og senere vende tilbage til noter og kilder. Kort sagt, du laver din slægtsforskning, som du vil.

Hvis du har yderligere spørgsmål, har Gramps et fællesskab af brugere og udviklere. Der er en [FAQ](wiki:Gramps_6.0_Wiki_Manual_-_FAQ/da) (liste over ofte stillede spørgsmål), en [mailingliste](wiki:Contact#Mailing_lists); [en bug-, feature request- og issue tracker](wiki:Using_the_bug_tracker); og du kan interagere via online [chatrum](wiki:Contact#Chat_Room) eller [community-fora](wiki:Contact#Forum).

### Forbindelser <span id="Connections"></span>

Disse 9 primære elementer er forbundet på en række måder. Nogle af disse forbindelser opretholdes implicit. Hvis man f.eks. tilføjer et personelement til et familieelement som forælder eller barn, oprettes der automatisk en særlig forbindelse, som kaldes en **Reference**. Du kan se de familier, som en person er forbundet med, på fanen Referencer i hovedvinduet Person. Der er også mange andre måder at visualisere disse forbindelser på i Gramps, herunder Relationship View.

For at undgå at gentage oplysninger giver Gramps dig mulighed for at genbruge eller dele elementer. Det er også særlige forbindelser, der kaldes **links**. For eksempel kan et Person-element linkes til et vilkårligt antal Note-elementer. Hvis en note nævner to forskellige personer, kan det give mening at dele den enkelte note med begge personelementer.

Nogle links har oplysninger i sig selv. Du kan f.eks. linke en person til et andet pars bryllup, f.eks. fordi personen var vidne til deres bryllup. Men manden og konen er knyttet til ægteskabsbegivenheden i en **primær** rolle, mens et vidne udfylder en anden rolle, f.eks. som **vidne**. Denne type information opbevares på selve linket i rolleegenskaben.

### Privatliv <span id="Privacy "></span>

Gramps understøtter to forskellige metoder til at beskytte privatlivets fred for følsomme data i din slægtsbog. Disse metoder bruges, når du deler dine data med andre, enten ved at oprette en rapport, eksportere data eller ved at oprette en hjemmeside.

Den første metode beskytter oplysninger om personer, som Gramps tror er i live. Hvis du ikke specifikt har angivet, at en person er død (ved at tilføje en dødshændelse til et personelement), så har Gramps en sofistikeret, automatisk funktion til at afgøre, om en person er i live. Levende personer får redigeret deres følsomme data, når man bruger denne metode. En person ved navn "Smith, John" kan f.eks. vises som "Smith, \[Levende\]".

Den anden metode til beskyttelse af personlige oplysninger er et eksplicit ["privat"-flag](wiki:Gramps_Glossary/da#private_tag), som du kan sætte på hvert element. Du kan f.eks. have følsomme, personlige oplysninger i en note. Hvis du markerer en sådan note som privat, vil den ikke blive vist i tekstuelle og narrative rapporter eller eksporter. Vær også opmærksom på, at nogle links selv kan markeres som private. Det er nyttigt, når du vil markere forbindelsen fra f.eks. en person til en begivenhed som privat, men stadig have personen og begivenheden tilgængelig i rapporten, eksporten eller på websitet.

![[_media/Include-data-marked-private-checkbox-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Fortrolighedstilsidesættelser for rapporter]]

For at aktivere disse to metoder til beskyttelse af personlige oplysninger skal du angive, at de skal bruges, når du opretter nogle rapporter eller eksporterer dine data.

### GEDCOM

Gramps henter sin kernestruktur af elementer fra en standard, der hedder GEDCOM. Gramps udvider dog denne standard, hvor det er blevet anset for nødvendigt. Hvis du planlægger at bruge dine slægtsdata i et andet system, der bruger GEDCOM, vil du sandsynligvis forsøge at begrænse din brug af funktioner, der kun er Gramps-udvidelser. På den anden side, hvis du ikke er begrænset af anden slægtsforskningssoftware, kan du indtaste dine data på de måder, der giver mening for dig.

Du kan læse flere detaljer om dette spørgsmål i afsnittet om [Gramps og GEDCOM](wiki:Gramps_og_GEDCOM).

## Start Gramps

Den bedste måde at lære Gramps på er ved at arbejde med dine data. Lad os komme i gang!

Den måde, du starter Gramps på, afhænger af det operativsystem, du bruger.

Ud over at starte Gramps ved hjælp af den normale grafiske brugergrænseflade (GUI) som beskrevet nedenfor, er det også muligt at starte Gramps ved hjælp af en kommandolinjegrænseflade (CLI). Brug af CLI kan producere rapporter, som ikke er tilgængelige via GUI, det kan bruges til at oprette rapporter, foretage konverteringer osv. uden at åbne et vindue, og det kan give [ekstra information](wiki:Gramps_6.0_Wiki_Manual_-_Error_and_Warning_Reference#Seeing_all_the_error_messages) i tilfælde af problemer. Se [appendiks om kommandolinjen](wiki:Gramps_6.0_Wiki_Manual_-_Command_Line/da) for mere information.

### Linux

Kun Linux-platformen er officielt understøttet, da Gramps-udviklerne bruger og tester kildekoden på den platform og løser eventuelle problemer, der opstår på grund af opgraderinger.

Hvis du har brugt standardpakkehåndteringen (enten via en CLI eller en GUI) til din Linux-distribution, vil du starte Gramps på den normale måde for din distribution. I Ubuntu 18.04 er der f.eks. et ikon i launcheren, eller programmet kan startes fra Dash. I andre distributioner kan der oprettes en post i programmenuen (normalt i **Office**-sektionen).

Start af Gramps via CLI på Linux er beskrevet [her](wiki:Gramps_6.0_Wiki_Manual_-_Command_Line/da#Linux).

### MS Windows

MS(Microsoft) Windows er en [fællesskabsunderstøttet](wiki:Download#MS_Windows) platform. Hvis du installerer den eksekverbare [Windows AIO](wiki:All_In_One_Gramps_Software_Bundle_for_Windows) GrampsAIO64, vil den placere et ikon på skrivebordet samt et menupunkt i menuen 'Start', og du skal klikke på det for at starte Gramps.

Start af Gramps via CLI på MS Windows er beskrevet [her](wiki:Gramps_6.0_Wiki_Manual_-_Command_Line/da#MS_Windows).

Der er andre måder at installere Gramps til MS Windows på, men de er meget mere komplicerede og beskrives ikke her.

### macOS

Apple macOS (oprindeligt Mac OS X forkortet OS X) er en [fællesskabsunderstøttet](wiki:Download#MS_Windows) platform. Hvis du downloader macOS-installationsfilen (.dmg), skal du blot trække programmet til din programmappe (eller hvor du ellers vil gemme det) og starte Gramps ved at dobbeltklikke på programmet på normal vis.

Start af Gramps via CLI på macOS er beskrevet [her](wiki:Gramps_6.0_Wiki_Manual_-_Command_Line/da#macOS).

Der er andre måder at installere Gramps til macOS på, men de er meget mere komplicerede og er ikke beskrevet her.

## Valg af slægtsbog <span id="Choosing a Family Tree"></span>

![[_media/Dashboard-category-view-first-open-no-family-tree-loaded-60.png|Fig {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Dashboard Category View - Første åbning af Gramps uden indlæst slægtsbog (Gramps 6.0.0; MS-Windows 10)))]]

Hvis Gramps startes, uden at der er valgt en slægtsbog, vil det første skærmbillede have ringe funktionalitet. De fleste operationer vil ikke være tilgængelige. For at indlæse en slægtsbog (også kaldet database) skal du vælge i menuen for at åbne slægtsbog-manageren eller klikke på -ikonet på værktøjslinjen. Gramps holder styr på dine nyligt åbnede slægtsbøger, og disse kan vælges ved at klikke på pilen ved siden af -knappen og vælge fra rullemenuen.

For mere detaljeret information om slægtsbog-manageren og menuen Slægtsbøger, se kapitlet dedikeret til dette: [Administrer slægtsbøger](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees/da).

## Fortæl mig, hvordan jeg kommer i gang lige nu! <span id="Tell me how to start right now!"></span>

Vi anbefaler alle at læse manualen for at lære alt om at bruge Gramps. Slægtsforskning tager tid, så det er ikke spild af tid at lære værktøjerne.

Men hvis du virkelig vil have det absolutte minimum for at komme i gang, så læs dette:

- [Gramps redigering af data (kort)](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_brief/da)
- [How-To start med slægtsforskning ved hjælp af Gramps](wiki:Start_with_Genealogy).

## Få hjælp <span id="Obtaining Help"></span>

Gramps har en , som du altid kan slå op i.

- Se afsnittet .

{{-}}

[Category:Documentation](wiki:Category:Documentation)
