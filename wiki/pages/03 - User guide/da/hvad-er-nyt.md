---
title: Da:Gramps 6.0 brugsanvisning - Hvad er nyt?
categories:
- Documentation
managed: false
source: wiki-scrape
wiki_revid: 129342
wiki_fetched_at: '2026-05-30T16:58:50Z'
lang: da
---

{{#vardefine:chapter\|1}} {{#vardefine:figure\|0}}

Dette afsnit giver et overblik over ændringer siden Gramps 5.2-versionen. Dette er en forbedringsudgivelse. Så ændringerne omfatter både nye funktioner og fejlrettelser. Disse ændringer er også beskrevet senere i denne manual. Brugere af Gramps, der opgraderer fra tidligere versioner, opfordres til at gennemgå dette afsnit i ældre brugervejledninger for at være sikre på at få gavn af disse nye funktioner, når de begynder at bruge version 6.0. Søg efter lynet i "- ⚡nyt til version 6.0.0"-mærkede afsnit.

## Foreløbig ændringsliste <span id="Preliminary change list"></span>

Da Gramps-dokumentationen udarbejdes af frivillige, udgives brugerdokumentationen trinvist, efter at udgivelsen er blevet offentliggjort. (For udvalgte nøgleelementer vil dokumentationen være markeret med "''</small>" "- ⚡nyt til version 6.0.0" for at gøre det nemmere at søge). WikiBidragydere skriver ikke kun ud fra deres erfaring med at udforske funktionerne, men også ved at se på udviklingsmål, funktionsanmodninger, statusrapporter og Pull Request-noter. Hvis du også er en opdagelsesrejsende, er meddelelserne nedenfor delvist knyttet til disse referencedokumenter. Udforsk frit og del din erfaring for at hjælpe med at guide andre.

### Fra Annonceringerne <span id="From the Announcements"></span>

Fra **[Announcements](https://gramps.discourse.group/c/gramps-announce/5)** sektionen i **[Gramps community support Discourse forum](https://gramps.discourse.group/t/welcome-to-the-gramps-discourse-forum/7)**:

- [6.0.6](https://github.com/gramps-project/gramps/releases/tag/v6.0.6) - en ny vedligeholdelsesudgivelse, udgivet 2025-11-08.
- [6.0.5](https://github.com/gramps-project/gramps/releases/tag/v6.0.5) - en ny vedligeholdelsesudgivelse, udgivet 2025-09-06.
- [6.0.4](https://github.com/gramps-project/gramps/releases/tag/v6.0.4) - en ny vedligeholdelsesudgivelse, udgivet 2025-08-10.
- [6.0.3](https://github.com/gramps-project/gramps/releases/tag/v6.0.3) - en ny vedligeholdelsesudgivelse, udgivet 2025-06-18.
- [6.0.2](https://github.com/gramps-project/gramps/releases/tag/v6.0.2) - en ny vedligeholdelsesudgivelse, udgivet 2025-06-15.
- [6.0.1](https://github.com/gramps-project/gramps/releases/tag/v6.0.1) - en ny vedligeholdelsesudgivelse, udgivet 2025-04-18.
- [6.0.0](https://github.com/gramps-project/gramps/releases/tag/v6.0.0) - en ny større udgivelse, udgivet 2025-03-19.
- [v6.0.0-rc2](https://github.com/gramps-project/gramps/releases/tag/v6.0.0-rc2) - an experimental pre-release, released 2025-03-16
- [v6.0.0-rc1](https://github.com/gramps-project/gramps/releases/tag/v6.0.0-rc1) - an experimental pre-release, released 2025-03-03
- [v6.0.0-beta2](https://github.com/gramps-project/gramps/releases/tag/v6.0.0-beta2) - an experimental pre-release, released 2025-02-13
- [v6.0.0-beta1](https://github.com/gramps-project/gramps/releases/tag/v6.0.0-beta1) - an experimental pre-release, released 2025-02-05

Diskussioner fra udviklerne om fremtidige version 6.0 udgivelser:

- [Understanding Gramps 6.0](https://gramps.discourse.group/t/understanding-gramps-6-0/6652) By Doug Blank - Development - Roadmap

<!-- -->

- Værktøjslinje forbedring - viser nu tekst under ikoner som standard.[1](https://gramps.discourse.group/t/gramps-6-0-defaults/6990/3)

## Før du opgraderer <span id="Before you upgrade"></span>

Før du opgraderer, skal du sørge for, at dine slægtbogsdata er sikre. Den bedste måde at gøre dette på er:

1.  Start din eksisterende version af Gramps (Gramps 4.2 / 5.0 / 5.1 / 5.2)
2.  Åbn din slægtsbog
3.  Sikkerhedskopier slægtsbogen til gramps xml-formatet eller gramps xml-pakkeformatet (gramps xml-pakken indeholder dine fotografier og andre mediefiler, der er knyttet til dine slægtsdata). Tag sikkerhedskopi af dit slægtstræ via menuen
4.  Luk slægtsbogen, og gentag ovenstående trin for eventuelle andre slægtsbøger, du har
5.  Opbevar den/de resulterende fil(er) et sikkert sted

For mere information, se Backing up a Family Tree. Bemærk, hvad der ikke vil blive inkluderet i en sikkerhedskopi.

Når du har sikret dine data korrekt, skal du fortsætte med at installere Gramps 6.0 ved hjælp af dit operativsystems almindelige installationsproces. I de fleste tilfælde vil dette sikre, at den nye Gramps 6.0-installation ikke kolliderer med din ældre version af Gramps. Det kan dog være mere sikkert at afinstallere Gramps 3.4, før du installerer Gramps 6.0, eller sørge for at installere Gramps 6.0 et andet sted. Dette er altid nødvendigt, hvis du installerer fra kildekoden. For mere information om installation af Gramps 6.0, se [Download af den nyeste Gramps](wiki:Download)

Når du har installeret Gramps 6.0, kan du åbne dine eksisterende slægtsbøger og fortsætte med at arbejde. Hvis der opstår problemer (f.eks. efter en komplet systemopgradering), skal du importere den eller de sikkerhedskopier, der er oprettet ovenfor, for at genskabe dine slægtsbøger.

## Synlige ændringer i Gramps kernen <span id="Visible changes to the core"></span>

Ændringer som er synlige efter migrering: brugergrænseflade, data

### Data-model <span id="Data Model"></span>

Specifikke ændringer i [data-model](wiki:Gramps_Data_Model) (hvis nogen):

1.  Ingen ændringer

- En slægtsbog **kan ikke åbnes** i Gramps 3.4 / 4.0 / 4.1 / 4.2 og Gramps 6.0 uden opgradering.

<!-- -->

- En nedgradering kan kun ske ved at lave en XML eksport og importere denne i en tidligere version af Gramps

<!-- -->

- En Gramps XML fil dannet vha Gramps 3.4 / 4.0 / 4.1 er *'ikke identisk* med en dannet vha Gramps 6.0

<!-- -->

- Gramps 6.0 er nu **python3** udelukkende.

Se [detaljerede ændringer](wiki:Database_Formats#Detailed_Changes) for flere detaljer om den interne database.

### Primære ændringer <span id="Primary changes"></span>

- SQLite er nu standard database frem for BSDDB. Du kan stadig anvende [alternative databaser](wiki:Relational_database_comparison). BSDDB fortsætter med at være at standard alternativ. For "power users" PostgreSQL og MongoDB er mulige som eksperimentelle tredie-parts tilføjelser. Udviklerne mener, at SQLite har færre database fejl som forhindrer recovery.

### GUI

### Steder <span id="Place"></span>

- Mulighed for at søge efter alternative stednavne, når et sted vælges

### Rapporter, Værktøjer, Gramplets <span id="Reports, Tools, Gramplets"></span>

### Importér/Eksportér <span id="Import/Export"></span>

### Nye tilføjelser <span id="New Addons"></span>

## Ændringer i maskinrummet <span id="Under the hood changes"></span>

### Tekniske ændringer

- Mange ændringer i forbindelse med mulighed for at benytte andre database systemer (SQLite, PostgreSQL, MongoDB etc.).

### Afhængigheder <span id="Dependencies "></span>

## Yderligere oplysninger <span id="Further information"></span>

### Diverse <span id="Miscellaneous "></span>

### Lokalisering <span id="Localization "></span>

- Opdatering af oversættelser

#### Tredjepartstilføjelser <span id="Third-Party Addons"></span>

- [Weblate til oversættelse af tredjepartstilføjelser](https://gramps.discourse.group/t/weblate-translation-for-addons-experiment-needs-testers/6964)

### Køreplan <span id="Roadmap"></span>

- Udforsk udgivelsesnoterne for [tidligere udgivelser af Gramps](wiki:Previous_releases_of_Gramps)
- Se projekterede elementer relateret til Gramps [next version. næste version.](https://gramps-project.org/bugs/roadmap_page.php)
- [Gramps Enhancement Proposals (GEPS)](wiki::Category:GEPS) - Se kolonnen Udgivet for nye elementer, der er implementeret i Gramps
- [Version 6.0 Køreplan](wiki:6.0_Roadmap) - wiki

### Ændringslog <span id="Changelog "></span>

- Se emner relateret til Gramps [6.0](https://gramps-project.org/bugs/changelog_page.php) på Gramps issue tracker.

<!-- -->

- Se yderligere oplysninger i changelogs for vedligeholdelsesudgaverne af Gramps:
  - Gramps [6.0.6](https://github.com/gramps-project/gramps/releases/tag/v6.0.6)
  - Gramps [6.0.5](https://github.com/gramps-project/gramps/releases/tag/v6.0.5)
  - Gramps [6.0.4](https://github.com/gramps-project/gramps/releases/tag/v6.0.4)
  - Gramps [6.0.3](https://github.com/gramps-project/gramps/releases/tag/v6.0.3)
  - Gramps [6.0.2](https://github.com/gramps-project/gramps/releases/tag/v6.0.2)
  - Gramps [6.0.1](https://github.com/gramps-project/gramps/releases/tag/v6.0.1)
  - Gramps [6.0.0](https://github.com/gramps-project/gramps/releases/tag/v6.0.0)
  - Gramps [6.0.0-rc2](https://github.com/gramps-project/gramps/releases/tag/v6.0.0-rc2)
  - Gramps [6.0.0-rc1](https://github.com/gramps-project/gramps/releases/tag/v6.0.0-rc1)
  - Gramps [6.0.0-beta2](https://github.com/gramps-project/gramps/releases/tag/v6.0.0-beta2)
  - Gramps [6.0.0-beta1](https://github.com/gramps-project/gramps/releases/tag/v6.0.0-beta1)

Compare GitHub commits from \[<https://github.com/gramps-project/gramps/compare/v5.2.4>...v6.0.1 Gramps 5.2.4 to 6.0.1\] {{-}}

### Hvad var *engang* nyt <span id="What Was ''Once'' New"></span>

Siden [Forrige udgivelse](wiki:Forrige_udgivelse) indeholder links til punktlister over ændringer i større udgivelser og vedligeholdelsesudgivelser i årenes løb.

Men siderne **Hvad er nyt?** i den afløste version af wiki-manualen for hver større udgivelse kan give flere detaljer:

- [Version 5.2](wiki:Gramps_5.2_Wiki_Manual_-_What%27s_new%3F)
- [Version 5.1](wiki:Gramps_5.1_Wiki_Manual_-_What%27s_new%3F)
- [Version 5.0](wiki:Gramps_5.0_Wiki_Manual_-_What%27s_new%3F)
- [Version 4.2](wiki:Gramps_4.2_Wiki_Manual_-_What%27s_new%3F)
- [Version 4.1](wiki:Gramps_4.1_Wiki_Manual_-_What%27s_new%3F)
- [Version 4.0](wiki:Gramps_4.0_Wiki_Manual_-_What%27s_new%3F)
- [Version 3.4](wiki:Gramps_3.4_Wiki_Manual_-_What%27s_new%3F)
- [Version 3.3](wiki:Gramps_3.3_Wiki_Manual_-_What%27s_new%3F)
- [Version 3.2](wiki:Gramps_3.2_Wiki_Manual_-_What%27s_new%3F)

### Download manual (engelsk) <span id="Downloadable manual"></span>

Version 6.0 - downloadable manual

- - [English PDF](wiki::File:Gramps6.0UserManual.pdf)

Vi viser ikke hver eneste fejlrettelse eller mindre forbedring på denne side. For at få en mere komplet liste over ændringer bør du se på commit-historikken for hver udgivelse.

{{-}}

[Category:Documentation](wiki:Category:Documentation)
