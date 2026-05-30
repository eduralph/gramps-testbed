---
title: Gramps 6.0 Wiki Manual - Reports - part 6/sk
categories:
- Plugins
- Sk:Documentation
managed: false
source: wiki-scrape
wiki_revid: 125640
wiki_fetched_at: '2026-05-30T20:12:32Z'
lang: sk
---

{{#vardefine:chapter\|13.6}} {{#vardefine:figure\|0}} Naspäť na [Register správ](wiki:Gramps_6.0_Wiki_Manual_-_Reports/sk).

<hr>

{{-}} ![[_media/MenuOverview-Reports-TextReports-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}}  Prehľad ponuky]] V tejto časti sú popísané rôzne dostupné v programe Gramps.

## Textové správy

Textové zostavy predstavujú požadované informácie ako formátovaný text. Väčšina možností je pre textové zostavy spoločná, preto budú opísané v časti Spoločné možnosti.

### Spoločné možnosti

Spoločné možnosti pre textové zostavy sú názov súboru výstupu, formát výstupu, zvolený štýl, veľkosť a orientácia strany. V prípade HTML zostáv nie sú k dispozícii žiadne informácie o stránke. Namiesto toho možnosti HTML zahŕňajú výber šablóny HTML, ktorá je k dispozícii v programe Gramps alebo vami definovanú vlastnú šablónu. Voliteľne možno výkazy okamžite otvoriť pomocou predvolenej aplikácie.

Možnosti, ktoré sú špecifické pre danú zostavu, budú popísané priamo v položke danej zostavy a na [Odkazy na príkazový riadok](wiki:Gramps_6.0_Wiki_Manuál_-_Príkazový_riadok#Opcie_akcie).

Pre každú zostavu je k dispozícii obrazovka, ktorá má v hornej časti záložky (ako Možnosti papiera...) a v dolnej časti **Možnosti dokumentu**. Počet záložiek sa líši v závislosti od zostavy.

#### Možnosti papiera

![[_media/TextReports-PaperOptions-tab-defaults-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Možnosti papiera - karta pre textové správy]]

Pomocou záložky môžete zmeniť:

- - **List**' (predvolené nastavenie)

  - (<kód>8,50</kód> v predvolenom nastavení)

  - (`11.00` in. default)

  - **Na výšku**' (predvolené)

- - (`1.00` in. default)

  - (`1.00` in. default)

  - (`1.00` in. default)

  - (`1.00` in. default)

- { : či sa majú použiť metrické hodnoty alebo nie (in. alebo cm.). (začiarkávacie políčko v predvolenom nastavení nie je začiarknuté)

{{-}}

#### Možnosti dokumentu

![[_media/TextReports-DocumentOptions-section-PlainText-output-settings-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Možnosti dokumentu - predvolené nastavenia karty pre textové správy (Plain Text - vybraný výstup)]] Nižšie uvedené možnosti sa mierne zmenia v závislosti od zvoleného výstupného formátu.

- vyberte výstupný formát:

  - Tlač...
  - PDF dokument
  - HTML
  - Otvoriť text dokumentu
  - PostScript
  - Dokument RTF
  - LaTex
  - Obyčajný text

- : môžete označiť, že chcete otvoriť vytvorený dokument vo vašom predvolenom prehliadači. (začiarkávacie políčko je v predvolenom nastavení nezačiarknuté)

- } predvolená hodnota je *`/home/`<užívateľské meno>`/`<názov rodokmeňa><názov správy>`.txt`*.

- (predvolená hodnota je *predvolené*). Pomocou tlačidla môžete pridávať štýly dokumentov.

- (<kód>72</kód> predvolené)

{{-}}

### <u>Správa o hlásení</u>

![[_media/TextReports-AhnentafelReport-example-overview-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Ahnentafel Report - Textové reporty - prehľad výstupných príkladov]]

Táto správa obsahuje zoznam Aktívnej osoby a jej predkov spolu s ich životnými údajmi.

Správu Ahnentafel môžete vybrať pomocou }

Osoby sú číslované špeciálnym spôsobom, ktorý je zavedeným štandardným [Genealogický číslovací systém](wiki:Genealogické_číslovacie_systémy) nazývaným [Ahnentafel](wiki:Genealogické_číslovacie_systémy#ahnentafel). Táto správa má niektoré [Ahnentafel špecifické možnosti štýlu](wiki:Gramps_6.0_Wiki_Manual_-_Settings/sk#Style_editor_dialog) v Editore štýlov prístupnom cez tlačidlo .

Aktívna osoba má číslo 1. Jeho otec a matka majú čísla 2 a 3.

Toto pravidlo platí pre každú osobu pri postupe v generáciách späť: rodičia otca majú čísla 4 a 5 a rodičia matky majú čísla 6 a 7, otcovia majú vždy párne a matky nepárne čísla.

Preto pre každú osobu s číslom N v tomto strome sú čísla otca 2N a matky 2N+1.

`       osoba = n`  
`       otec = 2n`  
`       matka = 2n+1`

Každý záznam bude pozostávať z jedného odseku a mal by obsahovať nasledujúci obsah:

- Číslo osoby.
- Meno osoby.
- Údaje o narodení, ak sú k dispozícii.
- Informácie o úmrtí, ak sú k dispozícii.
- Informácie o pohrebe, ak sú k dispozícii

Pozri tiež [common options](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_6#Common_options) {{-}}

#### Možnosti správy

![[_media/AhnentafelReport-TextReports-ReportOptions-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Ahnentafel Report - Textové reporty - Možnosti reportu - predvolené možnosti karty]]

- { stredová osoba pre správu, predvolené nastavenie je aktuálna aktívna osoba.
  - Tlačidlo . - Zmena stredovej osoby.

- `10` predvolené) Počet generácií, ktoré sa majú zahrnúť do správy.

- či sa má zahrnúť identifikátor rodiny.

  - **Nezahŕňať**' predvolené
  - zahrnúť

- { Či sa má po každej generácii začať nová stránka (začiarkávacie políčko je predvolene nezačiarknuté).

- { Označuje, či má za názvom nasledovať zalomenie riadku (zaškrtávacie políčko je predvolene nezačiarknuté).

{{-}}

#### Možnosti správy (2)

![[_media/AhnentafelReport-TextReports-ReportOptions2-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Ahnentafel Report - Textové reporty - Možnosti reportu (2) - predvolené možnosti karty]]

- \- Vyberte formát zobrazenia názvov. Tento výber sa zvyčajne preberá z predvoleného nastavenia v [Upraviť &gt; Zobrazenie](wiki:Gramps_6.0_Wiki_Manual_-_Settings/sk#Zobrazenie) záložke . Alebo ak chcete prepísať toto nastavenie pre správu, vyberte z:

  - **Predvolené** - (v novom rodokmeni je to zvyčajne *Priezvisko, daná prípona* )
  - Priezvisko, daná prípona
  - Daná prípona priezviska
  - Dané priezvisko
  - Hlavné priezviská, daná patronymická prípona
  - Priezvisko, dané (bežné)

-  (predvolene začiarkávacie políčko začiarknuté) - či sa majú zahrnúť súkromné údaje.

- \- Ako spracovať (informácie o) žijúcich ľuďoch

  - **Zahrnuté a všetky údaje** (predvolené)
  - Úplné mená, ale odstránené údaje
  - Nahradené mená a odstránené údaje
  - Úplné mená sa nahradia a údaje sa odstránia
  - Nezahŕňa sa

- `0`(predvolené) - či sa majú obmedziť údaje o nedávno zomrelých osobách.

- Preklad, ktorý sa má použiť pre správu. Výber jazyka zobrazujúci všetky jazyky podporované programom Gramps. Predvolené nastavenie je jazyk, v ktorom používate program Gramps.

- Formát a jazyk pre dátumy s príkladmi.

  - Predvolené - Vyberte túto možnosť, ak chcete použiť predvolené nastavenie v [Edit &gt; Display](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Display) na karte .
  - **RRRR-MM-DD(ISO)(2018-03-14)** (predvolené pre správu)
  - Číselný(14/3/2018)
  - Mesiac Deň, Rok(14. marec 2018)
  - DEŇ MESIACA, ROK(14.3.2018)
  - Deň Mesiac Rok(14. marec 2018)
  - DEŇ MESIAC ROK(14. marca 2018)

{{-}}

### <u>Hlásenie o narodeninách a výročiach</u>

![[_media/TextReports-BirthdayAndAnniversaryReport-example-overview-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Správa o narodeninách a výročiach - textové správy - prehľad príkladu výstupu]]

Táto správa poskytuje rovnaké informácie ako [Calendar report](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_4/sk#Kalendár), ale v textovom formáte.

Správu o narodeninách a výročiach si môžete vybrať pomocou {{-}} Pozri tiež [Obecné možnosti](wiki:Gramatika_6.0_Wiki_Manuál_-_Reporty_-_časť_6#Obecné_možnosti). {{-}}

#### Možnosti správy

![[_media/BirthdayAndAnniversaryReport-TextReports-ReportOptions-tab-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Správa o narodeninách a výročiach - Textové správy - Možnosti správy - predvolené možnosti karty]]

- \- Vyberte filter, ktorý sa má použiť na správu. Vyberte si z nasledujúcich možností:

  - **Celá databáza** (predvolené nastavenie)
  - Potomkovia aktívnej osoby
  - Rodiny potomkov aktívnej osoby
  - Predkovia aktívnej osoby
  - Osoby so spoločným predkom s aktívnou osobou
  - *Každý vlastný filter, ktorý ste vytvorili, bude uvedený pod ostatnými možnosťami.*

- Centrálna osoba pre filter. Predvolené nastavenie je Aktívna osoba.

  - Tlačidlo . - Zmena osoby filtra.

- <kód>Hlásenie o narodeninách a výročí</kód> (predvolené) - Názov hlásenia

- `Hlásenie o mojich narodeninách` (predvolené) - Prvý riadok textu v spodnej časti hlásenia

- `Produced with Gramps` (predvolené) - Druhý riadok textu v spodnej časti správy

- [`http://gramps-project.org/`](http://gramps-project.org/) (predvolené) - Tretí riadok textu v spodnej časti správy

{{-}}

#### Možnosti správy (2)

![[_media/BirthdayAndAnniversaryReport-TextReports-ReportOptions2-tab-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Správa o narodeninách a výročiach - Textové správy - Možnosti správy (2) - predvolené možnosti karty]]

- \- Vyberte formát zobrazenia mien. Tento výber sa zvyčajne preberá z predvoleného nastavenia v [Upraviť &gt; Zobrazenie](wiki:Gramps_6.0_Wiki_Manual_-_Settings/sk#Zobrazenie) záložke . Alebo ak chcete prepísať toto nastavenie pre správu, vyberte z:

  - **Predvolené** - (v novom rodokmeni je to zvyčajne *Priezvisko, daná prípona* )
  - Priezvisko, daná prípona
  - Daná prípona priezviska
  - Dané priezvisko
  - Hlavné priezviská, daná patronymická prípona
  - Priezvisko, dané (bežné)

-  (predvolene začiarkávacie políčko začiarknuté) - či sa majú zahrnúť súkromné údaje.

-  (začiarkávacie políčko predvolene začiarknuté) Zahrnúť do správy len žijúce osoby.

- } Preklad, ktorý sa má použiť pre správu. Výber jazyka zobrazujúci všetky jazyky podporované programom Gramps. Predvolené nastavenie je jazyk, v ktorom používate program Gramps.

{{-}}

#### Obsah

![[_media/BirthdayAndAnniversaryReport-TextReports-Content-tab-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Správa o narodeninách a výročiach - textové správy - obsah - predvolené možnosti karty]]

- vyplňte rok. Predvolené nastavenie je aktuálny rok.

- Vyberte krajinu, v ktorej sa majú zobraziť súvisiace sviatky. V predvolenom nastavení sa nezobrazujú žiadne.

- Vyberte zobrazené priezvisko vydatej ženy.

  - **Manželky používajú svoje vlastné priezvisko** (predvolené)
  - Manželky používajú manželovo priezvisko (z prvej uvedenej rodiny)
  - Manželky používajú manželovo priezvisko (z poslednej uvedenej rodiny)

-  Či sa majú do kalendára zahrnúť narodeniny (začiarkávacie políčko je predvolene začiarknuté)

-  Či sa majú do kalendára zahrnúť výročia (začiarkávacie políčko je predvolene začiarknuté)

-  Či sa majú zahrnúť vzťahy k filtrujúcej osobe (Poznámka: pomalšie vytváranie správy) (začiarkávacie políčko predvolene nezačiarknuté)

{{-}}

### <u>Kompletná správa o jedincovi</u>

![[_media/TextReports-CompleteIndividualReport-example-overview-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Kompletná správa o jedincovi - textové správy - prehľad výstupných príkladov]]

Táto správa poskytuje individuálne súhrny.

Úplný individuálny výkaz si môžete vybrať pomocou }

Pozri tiež [spoločné možnosti](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_6#Common_options). {{-}}

#### Možnosti správy

![[_media/CompleteIndividualReport-TextReports-ReportOptions-tab-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Kompletná individuálna správa - Textové správy - Možnosti správy - predvolené možnosti karty]]

Výhodou tejto zostavy je možnosť špecifického filtrovania. V závislosti od voľby filtra (len aktívna osoba, jej potomkovia, jej predkovia alebo celá databáza) môže správa obsahovať jeden až mnoho jednotlivých súhrnov. Ďalšou možnosťou tejto zostavy je zahrnutie informácií o zdroji pri výpise udalostí.

-   
  vyberte si medzi

  - **Celá databáza** (predvolené nastavenie)
  - Potomkovia aktívnej osoby
  - Rodiny potomkov aktívnej osoby
  - Predkovia aktívnej osoby
  - Ľudia so spoločným predkom s aktívnou osobou

-   
  Centrálna osoba pre správu.

-  (štandardne začiarknuté políčko)

-  (predvolene nezačiarknuté políčko)

{{-}}

#### Možnosti správy (2)

![[_media/CompleteIndividualReport-TextReports-ReportOptions2-tab-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Kompletná individuálna správa - Textové správy - Možnosti správy (2) - predvolené možnosti karty]]

-   
  Vyberte formát zobrazenia názvov. Vyberte si z možností **Priezvisko, daná prípona** (predvolené) / daná prípona priezviska / daná / hlavné priezviská, daná patronymická prípona / PRIEZVISKO, dané (bežné)

-  (predvolene začiarknuté políčko)

- \- Ako spracovať (informácie o) žijúcich osobách

  - **Zahrnuté a všetky údaje** (predvolené)
  - Úplné mená, ale odstránené údaje
  - Nahradené mená a odstránené údaje
  - Úplné mená sa nahradia a údaje sa odstránia
  - Nezahŕňa sa

- `0`(predvolené) - či sa majú obmedziť údaje o nedávno zomrelých osobách.

- Preklad, ktorý sa má použiť v správe. Výber jazyka zobrazujúci všetky jazyky podporované programom Gramps. Predvolené nastavenie je jazyk, v ktorom používate program Gramps.

- Formát a jazyk pre dátumy s príkladmi.

  - Predvolené - Vyberte túto možnosť, ak chcete použiť predvolené nastavenie v [Edit &gt; Display](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Display) na karte .
  - **RRRR-MM-DD(ISO)(2018-03-14)** (predvolené pre správu)
  - Číselný(14/3/2018)
  - Mesiac Deň, Rok(14. marec 2018)
  - DEŇ MESIACA, ROK(14.3.2018)
  - Deň Mesiac Rok(14. marec 2018)
  - DEŇ MESIAC ROK(14. marca 2018)

{{-}}

#### Include

![[_media/CompleteIndividualReport-TextReports-Include-tab-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Kompletná individuálna správa - Textové správy - Zahrnúť - predvolené možnosti karty]]

-  (štandardne začiarknuté políčko)

-  (štandardne začiarknuté políčko)

-  (políčko je predvolene nezačiarknuté)

-  (políčko je predvolene začiarknuté)

{{-}}

#### Include (2)

![[_media/CompleteIndividualReport-TextReports-Include2-tab-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Kompletná individuálna správa - Textové správy - Zahrnúť (2) - predvolené možnosti karty]]

- {, či sa majú zahrnúť identifikátory gramoplatne.
  - **Nezahŕňať**' predvolené nastavenie
  - zahrnúť

-  (predvolene začiarknuté políčko)

-  (štandardne začiarknuté políčko)

-  (štandardne začiarknuté políčko)

-  Či sa majú zahrnúť vzťahy k filtrujúcej osobe (Poznámka: pomalšie vytváranie správy) (zaškrtávacie políčko je predvolene nezačiarknuté)

{{-}}

#### Sekcie

![[_media/CompleteIndividualReport-TextReports-Sections-tab-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Kompletná individuálna správa - textové správy - sekcie - predvolené možnosti karty]]

Používa sa, ak sa vyžaduje samostatná sekcia.

- -  (štandardne začiarknuté políčko)

  -  (Štandardne začiarknuté políčko)

  -  (políčko je štandardne začiarknuté)

  -  (políčko je štandardne začiarknuté)

  -  (políčko je štandardne začiarknuté)

  -  (políčko je štandardne začiarknuté)

  -  (Štandardne začiarknuté políčko)

  -  (Štandardne začiarknuté políčko)

  -  (Štandardne začiarknuté políčko)

{{-}}

### <u>Súhrnná správa o databáze</u>

![[_media/TextReports-DatabaseSummaryReport-example-overview-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Súhrnná správa o databáze - textové správy - prehľad výstupných príkladov]]

Táto zostava zobrazuje celkové štatistiky týkajúce sa počtu osôb každého pohlavia, rôzne štatistiky neúplných záznamov, ako aj štatistiky rodín a médií.

Súhrnnú správu databázy môžete vybrať pomocou }.

Správa zobrazuje rozpis nasledujúcich informácií pre otvorený rodokmeň

Zobrazujú sa čísla v jednotlivých kategóriách

- **Jednotlivci**:
  - Počet jednotlivcov:

<!-- -->

- - Ženy:
  - Jedinci s neznámym pohlavím:
  - Neúplné mená:
  - Jednotlivci, u ktorých chýba dátum narodenia:
  - Odpojené osoby:
  - Jedinečné priezviská:

Jednotlivci s mediálnymi objektmi: \*\* Jednotlivci s mediálnymi objektmi: \*\* Jednotlivci s mediálnymi objektmi:

- **Rodinné informácie**:
  - Počet rodín:

<!-- -->

- **Mediálne objekty**:
  - Počet jedinečných mediálnych objektov:
  - Celková veľkosť mediálnych objektov: v MB(megabajtoch)

<!-- -->

- Chýbajúce mediálne objekty: zobrazia sa názvy súborov všetkých chýbajúcich mediálnych objektov.

Informácie uvedené v tejto správe sú rovnaké ako v [Statistics Gramplet](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Statistics).

Pozri tiež [obvyklé možnosti](wiki:Gramps_6.0_Wiki_Manuál_-_Pohľady_-_časť_6#Obvyklé_možnosti). {{-}}

#### Možnosti hlásenia

![[_media/DatabaseSummaryReport-TextReports-ReportOptions-tab-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Súhrnná správa databázy - Textové správy - Možnosti správy - predvolené možnosti záložky]]

-  (štandardne zaškrtnuté políčko)

- \- Ako spracovať (informácie o) žijúcich osobách

  - **Zahrnuté a všetky údaje** (predvolené)
  - Úplné mená, ale odstránené údaje
  - Nahradené mená a odstránené údaje
  - Úplné mená sa nahradia a údaje sa odstránia
  - Nezahŕňa sa

- `0`(predvolené) - Či sa majú obmedziť údaje o nedávno zomrelých ľuďoch.

- Preklad, ktorý sa má použiť pre správu. Výber jazyka zobrazujúci všetky jazyky podporované programom Gramps. Predvolené nastavenie je jazyk, v ktorom používate program Gramps.

{{-}}

### <u>Správy o potomkoch</u>

![[_media/TextReports-DescendantReport-example-overview-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Zostupná správa - textové zostavy - prehľad výstupných príkladov]]

Táto zostava prezentuje potomkov Aktívnej osoby so stručným popisom v odsadenom štýle.

Správu o potomkoch môžete vybrať pomocou }. {{-}} Pozri tiež [spoločné možnosti](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_6#Spoločné_možnosti) {{-}}

#### Možnosti správy

![[_media/DescendantReport-TextReports-ReportOptions-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Zostupná správa - Textové zostavy - Možnosti zostavy - predvolené možnosti záložky]]

Jediná špecifická možnosť sa týka počtu generácií dopredu, ktoré sa majú zohľadniť.

- stredová osoba pre správu, predvolene je to aktuálna aktívna osoba.

  - Tlačidlo . - Zmena stredovej osoby.

- [číselný systém](wiki:Genealogické_číslovacie_systémy), ktorý sa má použiť.

  - *'[Jednoduché číslovanie](wiki:Genealogické_číslovacie_systémy#jednoduché_číslovanie)* (predvolené)
  - [d'Aboville](wiki:Genealogické_číslovacie_Systémy#d.27Aboville) číslovanie
  - [Henry](wiki:Genealogické_číslovanie_Systémy#Henry) číslovanie
  - [Zmenené Henry](wiki:Genealogické_číslovanie_Systémy#zmenené_henry) číslovanie
  - [de Villiers](wiki:Genealogické_číslovacie_systémy#de_Villiers)/[Pama](wiki:Genealogické_číslovacie_systémy#pama) číslovanie
  - [Meurgey de Tupigny](wiki:Genealogické_číslovacie_systémy#meurgey_de_tupigny) číslovanie

- (<kód>10</kód> predvolené) Počet generácií, ktoré sa majú zahrnúť do správy.

-  Či sa majú v správe zobrazovať informácie o manželstve. (začiarkávacie políčko je predvolene nezaškrtnuté)

-  Či sa majú v správe zobrazovať informácie o rozvode. (v predvolenom nastavení políčko nie je začiarknuté)

-  Či sa majú v správe zobrazovať informácie o duplicitných rodokmeňoch. (v predvolenom nastavení je začiarkávacie políčko začiarknuté)

{{-}}

#### Možnosti správy (2)

![[_media/DescendantReport-TextReports-ReportOptions2-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Správa potomka - Textové správy - Možnosti správy (2) - predvolené možnosti záložky]]

- \- Vyberte formát zobrazenia mien. Tento výber sa zvyčajne preberá z predvoleného nastavenia v [Upraviť &gt; Zobrazenie](wiki:Gramps_6.0_Wiki_Manual_-_Settings/sk#Zobrazenie) záložke . Alebo ak chcete prepísať toto nastavenie pre správu, vyberte z:

  - **Predvolené** - (v novom rodokmeni je to zvyčajne *Priezvisko, daná prípona* )
  - Priezvisko, daná prípona
  - Daná prípona priezviska
  - Dané priezvisko
  - Hlavné priezviská, daná patronymická prípona
  - Priezvisko, dané (bežné)

-  (predvolene začiarkávacie políčko začiarknuté) - či sa majú zahrnúť súkromné údaje.

- \- Ako spracovať (informácie o) žijúcich ľuďoch

  - **Zahrnuté a všetky údaje** (predvolené)
  - Úplné mená, ale odstránené údaje
  - Nahradené mená a odstránené údaje
  - Úplné mená sa nahradia a údaje sa odstránia
  - Nezahŕňa sa

- `0`(predvolené) - či sa majú obmedziť údaje o nedávno zomrelých osobách.

- Preklad, ktorý sa má použiť pre správu. Výber jazyka zobrazujúci všetky jazyky podporované programom Gramps. Predvolené nastavenie je jazyk, v ktorom používate program Gramps.

- Formát a jazyk pre dátumy s príkladmi.

  - Predvolené - Vyberte túto možnosť, ak chcete použiť predvolené nastavenie v [Edit &gt; Display](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Display) na karte .
  - **RRRR-MM-DD(ISO)(2018-03-14)** (predvolené pre správu)
  - Číselný(14/3/2018)
  - Mesiac Deň, Rok(14. marec 2018)
  - DEŇ MESIACA, ROK(14.3.2018)
  - Deň Mesiac Rok(14. marec 2018)
  - DEŇ MESIAC ROK(14. marca 2018)

{{-}}

### <u>Podrobná správa o predkoch</u>

![[_media/TextReports-DetailedAncestralReport-example-overview-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Podrobná správa o predkoch - textové správy - prehľad príkladu výstupu]]

Táto správa sa podrobne zaoberá predkami aktívnej osoby, vrátane celého radu životných údajov, ako aj sobášov, podľa číslovania [Sosa-Stradonitz](wiki:Genealogické_číslovacie_systémy#sosa-stradonitz)/[Ahnentafel](wiki:Genealogické_číslovacie_systémy#ahnentafel). Má mnoho spoločných vlastností s Podrobnou správou o potomkoch (pozri nižšie).

Podrobnú správu o predkoch môžete vybrať pomocou {{-}} Pozrite si tiež [spoločné možnosti](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_6#Spoločné_možnosti). {{-}}

#### Možnosti správy

![[_media/DetailedAncestralReport-TextReports-ReportOptions-tab-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Podrobná správa o predkoch - Textové správy - Možnosti správy - predvolené možnosti karty]]

Správa je štruktúrovaná pomocou [Ahnentafel](wiki:Genealogické_číslovacie_systémy#ahnentafel) štandardného číslovania.

- stredná osoba pre správu, predvolene je to aktuálna aktívna osoba.

  - Tlačidlo . - Zmena stredovej osoby.

- (`1` predvolené) Číslo [Sosa-Stradonitz](wiki:Genealogické_číslovacie_systémy#sosa-stradonitz) centrálnej osoby.

- (`10` predvolené) Počet generácií, ktoré sa majú zahrnúť do správy.

- či sa majú zahrnúť identifikátory gramov.

  - **Nezahŕňať**' predvolené
  - zahrnúť

- { : Či sa má po každej generácii začať nová stránka. (v predvolenom nastavení políčko nie je začiarknuté)

- : či sa má začať nová stránka pred koncovými poznámkami (políčko je štandardne nezačiarknuté)

{{-}}

#### Možnosti správy (2)

![[_media/DetailedAncestralReport-TextReports-ReportOptions2-tab-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Podrobná správa o predkoch - Textové správy - Možnosti správy (2) - predvolené možnosti karty]]

- \- Vyberte formát zobrazenia mien. Tento výber sa zvyčajne preberá z predvoleného nastavenia v [Edit &gt; Display](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Display) na karte . Alebo ak chcete prepísať toto nastavenie pre správu, vyberte z:

  - **Predvolené** - (v novom rodokmeni je to zvyčajne *Priezvisko, daná prípona* )
  - Priezvisko, daná prípona
  - Daná prípona priezviska
  - Dané priezvisko
  - Hlavné priezviská, daná patronymická prípona
  - Priezvisko, dané (bežné)

-  (predvolene začiarkávacie políčko začiarknuté) - či sa majú zahrnúť súkromné údaje.

- \- Ako spracovať (informácie o) žijúcich ľuďoch

  - **Zahrnuté a všetky údaje** (predvolené)
  - Úplné mená, ale odstránené údaje
  - Nahradené mená a odstránené údaje
  - Úplné mená sa nahradia a údaje sa odstránia
  - Nezahŕňa sa

- `0`(predvolené) - či sa majú obmedziť údaje o nedávno zomrelých osobách.

- Preklad, ktorý sa má použiť pre správu. Výber jazyka zobrazujúci všetky jazyky podporované programom Gramps. Predvolené nastavenie je jazyk, v ktorom používate program Gramps.

- Formát a jazyk pre dátumy s príkladmi.

  - Predvolené - Vyberte túto možnosť, ak chcete použiť predvolené nastavenie v [Edit &gt; Display](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Display) na karte .
  - **RRRR-MM-DD(ISO)(2018-03-14)** (predvolené pre správu)
  - Číselný(14/3/2018)
  - Mesiac Deň, Rok(14. marec 2018)
  - DEŇ MESIACA, ROK(14.3.2018)
  - Deň Mesiac Rok(14. marec 2018)
  - DEŇ MESIAC ROK(14. marca 2018)

{{-}}

#### Content

![[_media/DetailedAncestralReport-TextReports-Content-tab-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Podrobná správa o predkoch - textové správy - obsah - predvolené možnosti karty]]

- { : či sa majú používať úplné vety alebo stručný jazyk (začiarkávacie políčko je predvolene začiarknuté).

- { : či sa majú namiesto roku používať celé dátumy (začiarkávacie políčko je predvolene začiarknuté).

- : či sa má vypočítať vek osoby pri úmrtí (predvolene začiarknuté políčko)

- : či sa majú vynechať duplicitní predkovia (štandardne začiarknuté políčko)

- : či sa má ako meno použiť meno volaného. (začiarkávacie políčko je predvolene nezačiarknuté)

{{-}}

#### Include

![[_media/DetailedAncestralReport-TextReports-Include-tab-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Podrobná správa o predkoch - Textové správy - Zahrnúť - predvolené možnosti karty]]

- : či sa majú uviesť deti (zaškrtávacie políčko je predvolene začiarknuté)

- : či sa majú uviesť manželia/manželky detí (zaškrtávacie políčko je predvolene začiarknuté)

- : Či sa majú zahrnúť udalosti. (zaškrtávacie políčko v predvolenom nastavení nie je začiarknuté)

- : Či sa majú zahrnúť aj iné udalosti, na ktorých sa ľudia zúčastnili (políčko je predvolene nezačiarknuté).

- : či sa majú do zoznamu detí pridať odkazy na potomkov (začiarkávacie políčko je predvolene začiarknuté).

-  (začiarkávacie políčko je predvolene nezaškrtnuté)

{{-}}

#### Include (2)

![[_media/DetailedAncestralReport-TextReports-Include2-tab-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Podrobná správa o predkoch - Textové správy - Zahrnúť (2) - predvolené možnosti karty]]

-  (štandardne začiarknuté políčko)

-  (štandardne políčko nezačiarknuté)

-  (políčko je štandardne nezačiarknuté)

-  (políčko je štandardne nezačiarknuté)

-  (políčko je štandardne nezačiarknuté)

-  (začiarkávacie políčko je predvolene nezačiarknuté)

{{-}}

#### Chýbajúce informácie

![[_media/DetailedAncestralReport-TextReports-MissingInformation-tab-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Podrobná správa o predkoch - textové správy - chýbajúce informácie - predvolené možnosti karty]]

- {: (začiarkávacie políčko je predvolene nezačiarknuté)

-   
  (začiarkávacie políčko je predvolene nezačiarknuté)

{{-}}

### <u>Podrobná správa o potomkoch</u>

![[_media/TextReports-DetailedDescendantReport-example-overview-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Podrobná správa o potomkovi - textové správy - prehľad výstupných príkladov]]

Táto správa sa podrobne zaoberá potomkami aktívnej osoby podľa generácií, pričom nadväzuje na genealogickú tradíciu textových správ o potomkoch podľa generácií. Jej cieľom je poskytnúť všetky dôležité funkcie, ktoré sa očakávajú v týchto klasických formátoch potomkov, a získala vplyv z rôznych zdrojov. Tím Gramps považuje za jeden zo svojich cieľov životaschopnosť prijatia tejto správy profesionálnymi genealogickými inštitúciami na celom svete. V dôsledku toho ide o správu, ktorá sa dá do veľkej miery prispôsobiť.

Správa obsahuje celý rad životných informácií, sobášov a (voliteľne) poznámok a informácií o manželoch. Medzi početné možnosti patrí počet generácií dopredu, ktoré sa majú zohľadniť, či sa má vypočítať vek, štýl textu medzi úplným a stručným a či sa majú zahrnúť obrázky. Správa štandardne využíva číslovanie [Henryho štýlu](wiki:Genealogické_číslovacie_systémy#henry) a ako možnosti ponúka [d'Abovilleho štýlu číslovania](wiki:Genealogické_číslovacie_systémy#d&#39;aboville) a [Registrového štýlu číslovania](wiki:Genealogické_číslovacie_systémy#register).

Podrobnú správu o potomkoch môžete vybrať pomocou {{-}} Pozri tiež [bežné voľby](wiki:Gramps_6.0_Wiki_Manuál_-_Reporty_-_časť_6#Božné_voľby). {{-}}

#### Možnosti správy

![[_media/DetailedDescendantReport-TextReports-ReportOptions-tab-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Podrobná správa o potomkoch - Textové správy - Možnosti správy - predvolené možnosti karty]]

- centrálna osoba pre správu, predvolene je to aktuálna aktívna osoba.

  - tlačidlo. - Zmena stredovej osoby.

- [číslovací systém](http://en.wikipedia.org/wiki/Genealogical_numbering_systems#Register_System), ktorý sa má použiť.

  - **Henryho číslovanie** (predvolené)
  - Číslovanie d'Aboville
  - Číslovanie záznamov (upravený register)

- Ako sú ľudia usporiadaní v správe

  - **Zobraziť osoby podľa generácií** (predvolené)
  - zobrazovať osoby podľa rodokmeňa

- (`10` predvolené) Počet generácií, ktoré sa majú zahrnúť do správy.

- či sa majú zahrnúť identifikácie rodov.

  - **Nezahŕňať**' predvolené
  - zahrnúť

- {: Či sa má po každej generácii začať nová stránka. (zaškrtávacie políčko v predvolenom nastavení nezačiarknuté)

-   
  či sa má začať nová stránka pred koncovými poznámkami (zaškrtávacie políčko je štandardne nezaškrtnuté)

{{-}}

#### Možnosti správy (2)

![[_media/DetailedDescendantReport-TextReports-ReportOptions2-tab-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Podrobná správa o potomkoch - Textové správy - Možnosti správy (2) - predvolené možnosti karty]]

- \- Vyberte formát zobrazenia mien. Tento výber sa zvyčajne preberá z predvoleného nastavenia v [Upraviť &gt; Zobrazenie](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Zobrazenie) záložke . Alebo ak chcete prepísať toto nastavenie pre správu, vyberte z:

  - **Predvolené** - (v novom rodokmeni je to zvyčajne *Priezvisko, daná prípona* )
  - Priezvisko, daná prípona
  - Daná prípona priezviska
  - Dané priezvisko
  - Hlavné priezviská, daná patronymická prípona
  - Priezvisko, dané (bežné)

-  (predvolene začiarkavacie políčko začiarknuté) - či sa majú zahrnúť súkromné údaje.

- \- Ako spracovať (informácie o) žijúcich ľuďoch

  - **Zahrnuté a všetky údaje** (predvolené)
  - Úplné mená, ale odstránené údaje
  - Nahradené mená a odstránené údaje
  - Úplné mená sa nahradia a údaje sa odstránia
  - Nezahŕňa sa

- `0`(predvolené) - či sa majú obmedziť údaje o nedávno zomrelých osobách.

- Preklad, ktorý sa má použiť pre správu. Výber jazyka zobrazujúci všetky jazyky podporované programom Gramps. Predvolené nastavenie je jazyk, v ktorom používate program Gramps.

- Formát a jazyk pre dátumy s príkladmi.

  - Predvolené - Vyberte túto možnosť, ak chcete použiť predvolené nastavenie v [Edit &gt; Display](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Display) na karte .
  - **RRRR-MM-DD(ISO)(2018-03-14)** (predvolené pre správu)
  - Číselný(14/3/2018)
  - Mesiac Deň, Rok(14. marec 2018)
  - DEŇ MESIACA, ROK(14.3.2018)
  - Deň Mesiac Rok(14. marec 2018)
  - DEŇ MESIAC ROK(14. marca 2018)

{{-}}

#### Content

![[_media/DetailedDescendantReport-TextReports-Content-tab-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Podrobná správa o potomkoch - textové správy - obsah - predvolené možnosti záložky]]

- {: či sa majú používať úplné vety alebo stručný jazyk (predvolené začiarkavacie políčko je začiarknuté).

-   
  či sa majú namiesto roku používať celé dátumy (predvolene zaškrtnuté políčko).

-   
  či sa má vypočítať vek osoby pri úmrtí (predvolene začiarknuté políčko)

-   
  či sa má meno volajúceho použiť ako meno. (zaškrtávacie políčko je predvolene nezačiarknuté)

{{-}}

#### Include

![[_media/DetailedDescendantReport-TextReports-Include-tab-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Podrobná správa o potomkoch - textové správy - zahrnúť - predvolené možnosti karty]]

- {: či sa majú uviesť deti (zaškrtávacie políčko je predvolene začiarknuté).

-   
  či sa majú uviesť manželia detí (začiarkavacie políčko je predvolene nezačiarknuté)

- { (zaškrtávacie políčko je štandardne nezaškrtnuté)

-  (zaškrtávacie políčko v predvolenom nastavení nezačiarknuté)

-  (políčko je štandardne nezačiarknuté)

- : či sa majú do zoznamu potomkov zahrnúť odkazy na potomkov (políčko je predvolene začiarknuté)

-  (zaškrtávacie políčko je predvolene nezaškrtnuté)

{{-}}

#### Include (2)

![[_media/DetailedDescendantReport-TextReports-Include2-tab-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Podrobná správa o potomkoch - Textové správy - Zahrnúť (2) - predvolené možnosti karty]]

-  (štandardne zaškrtnuté políčko)

-  (štandardne políčko nezačiarknuté)

-  (políčko je štandardne nezačiarknuté)

-  (štandardne políčko nezačiarknuté)

-  (políčko je štandardne nezačiarknuté)

-  (zaškrtávacie políčko je predvolene nezaškrtnuté)

-  (políčko je predvolene začiarknuté)

-  (políčko je predvolene nezačiarknuté)

{{-}}

#### Chýbajúce informácie

![[_media/DetailedDescendantReport-TextReports-MissingInformation-tab-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Podrobná správa o potomkoch - textové správy - chýbajúce informácie - predvolené možnosti záložky]]

-   
  (začiarkávacie políčko je predvolene nezaškrtnuté)

-   
  (začiarkávacie políčko je predvolene nezačiarknuté)

{{-}}

### <u>Správa o konci línie</u>

![[_media/TextReports-EndOfLineReport-example-overview-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Správa na konci riadku - textové správy - prehľad príkladu výstupu]]

Toto poskytuje zoznam posledných známych predkov osoby s rodokmeňom zoradených podľa generácií.

Správu o konci línie môžete vybrať pomocou }. {{-}} Pozrite si tiež [spoločné možnosti](wiki:Gramps_6.0_Wiki_Manuál_-_Reporty_-_časť_6#Spoločné_možnosti) {{-}}

#### Možnosti správy

![[_media/EndOfLineReport-TextReports-ReportOptions-tab-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Správa o konci línie - Textové správy - Možnosti správy - predvolené možnosti karty]]

- centrálna osoba pre správu, predvolene je to aktuálna aktívna osoba.

  - Tlačidlo . - Zmena stredovej osoby.

- \- Vyberte formát zobrazenia mien. Tento výber sa zvyčajne preberá z predvoleného nastavenia v [Upraviť &gt; Zobrazenie](wiki:Gramps_6.0_Wiki_Manual_-_Settings/sk#Zobrazenie) na karte . Alebo na prepísanie tohto nastavenia pre správu vyberte z:

  - **Predvolené** - (v novom rodokmeni je to zvyčajne *Priezvisko, daná prípona* )
  - Priezvisko, daná prípona
  - Daná prípona priezviska
  - Dané priezvisko
  - Hlavné priezviská, daná patronymická prípona
  - Priezvisko, dané (bežné)

-  (začiarkávacie políčko je predvolene začiarknuté) - či sa majú zahrnúť súkromné údaje.

- \- Ako spracovať (informácie o) žijúcich ľuďoch

  - **Zahrnuté a všetky údaje** (predvolené)
  - Úplné mená, ale odstránené údaje
  - Nahradené mená a odstránené údaje
  - Úplné mená nahradené a údaje odstránené
  - Nie je zahrnuté

- `0`(predvolené) - či sa majú obmedziť údaje o nedávno zomrelých osobách.

- Preklad, ktorý sa má použiť pre správu. Výber jazyka zobrazujúci všetky jazyky podporované programom Gramps. Predvolené nastavenie je jazyk, v ktorom používate program Gramps.

- Formát a jazyk pre dátumy s príkladmi.

  - Predvolené - Vyberte túto možnosť, ak chcete použiť predvolené nastavenie v [Edit &gt; Display](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Display) záložke pre možnosť .
  - **YYYY-MM-DD(ISO)(2018-03-14)** (predvolené pre správu)
  - Číselný(14/3/2018)
  - Mesiac Deň, Rok(14.3.2018)
  - DEŇ MESIACA, ROK(14.3.2018)
  - Deň Mesiac Rok(14. marec 2018)
  - DEŇ MESIAC ROK(14. marca 2018)

{{-}}

### <u>Správa o rodinnej skupine</u>

![[_media/TextReports-FamilyGroupReport-example-overview-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Správa o skupine rodín - textové správy - prehľad výstupov príkladov]]

Týmto sa vytvorí správa o rodinnej skupine, v ktorej sa zobrazia informácie o súbore rodičov a ich detí.

Hlásenie o rodinnej skupine môžete vybrať pomocou }. {{-}} Pozri tiež [spoločné možnosti](wiki:Gramps_6.0_Wiki_Manuál_-_Reporty_-_časť_6#Spoločné_možnosti). {{-}}

#### Možnosti správy

![[_media/FamilyGroupReport-TextReports-ReportOptions-tab-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Správa o skupine rodín - textové správy - možnosti správy - predvolené možnosti záložky]]

- \- Vyberte filter, ktorý sa má použiť na správu. Vyberte si z nasledujúcich možností:

  - **Predvolené** - Predvolené nastavenie na Aktívnu rodinu pre aktuálnu aktívnu osobu.
  - Každá rodina
  - Potomkovia rodiny - aktívnej rodiny
  - Rodiny predkov - aktívnej rodiny

- Centrálna rodina pre filter. Predvolené nastavenie je Aktívna rodina pre aktuálnu aktívnu osobu.

  - Tlačidlo . - Zmena rodiny filtra.

- { : Vytvárať hlásenia pre všetkých potomkov tejto rodiny (začiarkavacie políčko je predvolene nezačiarknuté).

{{-}}

#### Možnosti správy (2)

![[_media/FamilyGroupReport-TextReports-ReportOptions2-tab-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Správa o skupine rodín - Textové správy - Možnosti správy (2) - predvolené možnosti karty]]

- } - Vyberte formát zobrazenia mien. Tento výber sa zvyčajne preberá z predvoleného nastavenia v [Upraviť &gt; Zobrazenie](wiki:Gramps_6.0_Wiki_Manual_-_Settings/sk#Zobrazenie) záložke . Alebo ak chcete prepísať toto nastavenie pre správu, vyberte z:

  - **Predvolené** - (v novom rodokmeni je to zvyčajne *Priezvisko, daná prípona* )
  - Priezvisko, daná prípona
  - Daná prípona priezviska
  - Dané priezvisko
  - Hlavné priezviská, daná patronymická prípona
  - Priezvisko, dané (bežné)

-  (začiarkávacie políčko je predvolene začiarknuté) - či sa majú zahrnúť súkromné údaje.

- \- Ako spracovať (informácie o) žijúcich ľuďoch

  - **Zahrnuté a všetky údaje** (predvolené)
  - Úplné mená, ale odstránené údaje
  - Nahradené mená a odstránené údaje
  - Úplné mená nahradené a údaje odstránené
  - Nie je zahrnuté

- `0`(predvolené) - či sa majú obmedziť údaje o nedávno zomrelých osobách.

- Preklad, ktorý sa má použiť pre správu. Výber jazyka zobrazujúci všetky jazyky podporované programom Gramps. Predvolené nastavenie je jazyk, v ktorom používate program Gramps.

- Formát a jazyk pre dátumy s príkladmi.

  - Predvolené - Vyberte túto možnosť, ak chcete použiť predvolené nastavenie v [Edit &gt; Display](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Display) na karte .
  - **YYYY-MM-DD(ISO)(2018-03-14)** (predvolené pre správu)
  - Číselný(14/3/2018)
  - Mesiac Deň, Rok(14.3.2018)
  - DEŇ MESIACA, ROK(14.3.2018)
  - Deň Mesiac Rok(14. marec 2018)
  - DEŇ MESIAC ROK(14. marca 2018)

{{-}}

#### Include

![[_media/FamilyGroupReport-TextReports-Include-tab-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Správa o skupine rodín - textové správy - zahrnúť - predvolené možnosti karty]]

- { : Či sa majú zahrnúť informácie o manželstve rodiča. (začiarkávacie políčko je predvolene začiarknuté)

- : Či sa majú zahrnúť udalosti pre rodičov. (začiarkávacie políčko v predvolenom nastavení nezačiarknuté)

- : Či sa majú zahrnúť adresy rodičov. (v predvolenom nastavení políčko nie je začiarknuté)

- : Či má obsahovať poznámky pre rodičov. (v predvolenom nastavení políčko nie je začiarknuté)

- : Či sa majú zahrnúť atribúty. (v predvolenom nastavení políčko nie je začiarknuté)

- : Či sa má zahrnúť alternatívne meno. (v predvolenom nastavení políčko nie je začiarknuté)

{{-}}

#### Zaradiť (2)

![[_media/FamilyGroupReport-TextReports-Include2-tab-50.png|Obrázok {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Správa o skupine rodín - textové správy - zahrnúť (2) - predvolené možnosti karty]]

- , či sa majú zahrnúť identifikátory starých rodičov.
  - **Nezahŕňať**' predvolené nastavenie
  - zahrnúť

- : (štandardne políčko nezačiarknuté)

- : Či sa majú zahrnúť dátumy príbuzných. (v predvolenom nastavení políčko nie je začiarknuté)

- : Či sa majú zahrnúť informácie o manželstvách detí (políčko je predvolene začiarknuté).

- : Či sa má zahrnúť generácia pri každom z nich (zaškrtávacie políčko je predvolene nezaškrtnuté).

- : Či sa majú zahrnúť polia pre chýbajúce informácie. (začiarkávacie políčko je predvolene začiarknuté)

{{-}}

### <u>Správa o príbuzenstve</u>

![[_media/TextReports-KinshipReport-example-overview-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Správa o príbuznosti - textové správy - prehľad príkladu výstupu]]

Toto poskytuje príbuzenské vzťahy vybranej osoby podľa úrovne vyhľadávania (výška, zostupné generácie) nastavenej používateľom.

Správu o príbuznosti môžete vybrať pomocou . {{-}} Pozri tiež [spoločné možnosti](wiki:Gramatika_6.0_Wiki_Manuál_-_Reporty_-_časť_6#Spoločné_možnosti). {{-}}

#### Možnosti správy

![[_media/KinshipReport-TextReports-ReportOptions-tab-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Správa o príbuzenstve - Textové správy - Možnosti správy - predvolené možnosti karty]]

- centrálna osoba pre správu, predvolené nastavenie je aktuálna aktívna osoba.

  - tlačidlo. - Zmena stredovej osoby.

- (`2`predvolené) Maximálny počet generácií potomkov. V prípade potreby môžete zadať väčšie číslo.

- (`2`default) Maximálny počet generácií predkov. V prípade potreby môžete zadať väčšie číslo.

- { : Či sa majú zahrnúť manželia. (začiarkávacie políčko je predvolene začiarknuté)

- : Či sa majú zahrnúť bratranci a sesternice. (štandardne začiarknuté políčko)

- : Či sa majú zahrnúť tety/strýkovia/tetičky/nerčatá. (štandardne začiarknuté políčko)

{{-}}

#### Možnosti správy (2)

![[_media/KinshipReport-TextReports-ReportOptions2-tab-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Správa o príbuzenstve - Textové správy - Možnosti správy (2) - predvolené možnosti karty]]

- } - Vyberte formát zobrazenia mien. Tento výber sa zvyčajne preberá z predvoleného nastavenia v [Edit &gt; Display](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Display) záložke . Alebo ak chcete prepísať toto nastavenie pre správu, vyberte z:

  - **Predvolené** - (v novom rodokmeni je to zvyčajne *Priezvisko, daná prípona* )
  - Priezvisko, daná prípona
  - Daná prípona priezviska
  - Dané priezvisko
  - Hlavné priezviská, daná patronymická prípona
  - Priezvisko, dané (bežné)

-  (predvolene začiarkávacie políčko začiarknuté) - či sa majú zahrnúť súkromné údaje.

- \- Ako spracovať (informácie o) žijúcich ľuďoch

  - **Zahrnuté a všetky údaje** (predvolené)
  - Úplné mená, ale odstránené údaje
  - Nahradené mená a odstránené údaje
  - Úplné mená sa nahradia a údaje sa odstránia
  - Nezahŕňa sa

- `0`(predvolené) - či sa majú obmedziť údaje o nedávno zomrelých osobách.

- Preklad, ktorý sa má použiť pre správu. Výber jazyka zobrazujúci všetky jazyky podporované programom Gramps. Predvolené nastavenie je jazyk, v ktorom používate program Gramps.

- Formát a jazyk pre dátumy s príkladmi.

  - Predvolené - Vyberte túto možnosť, ak chcete použiť predvolené nastavenie v [Edit &gt; Display](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Display) na karte .
  - **RRRR-MM-DD(ISO)(2018-03-14)** (predvolené pre správu)
  - Číselný(14/3/2018)
  - Mesiac Deň, Rok(14. marec 2018)
  - DEŇ MESIACA, ROK(14.3.2018)
  - Deň Mesiac Rok(14. marec 2018)
  - DEŇ MESIAC ROK(14. marca 2018)

{{-}}

### <u>Správa o prepojení poznámok</u>

![[_media/TextReports-NoteLinkReport-example-overview-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Správa o prepojení poznámok - textové správy - prehľad príkladu výstupu]]

Táto zostava zobrazuje a kontroluje stav konzistencie *interného odkazu* v poznámkach Gramps vytvorených pomocou [Odkaz Editor](wiki:Gramps_6.0_Wiki_Manuál_-_Vkladanie_a_úprava_údajov:_podrobne_-_časť_2#Odkaz_Editor) a uvádza iba externé internetové adresy vytvorené pomocou [Internet Address Editor](wiki:Gramps_5._1_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1#Internet_Address_Editor) bez ich kontroly.

Hlásenie o prepojení poznámok môžete vybrať pomocou

Pre túto zostavu nie sú k dispozícii žiadne možnosti.[1](http://gramps.1791082.n4.nabble.com/Privacy-td4671118.html#a4671131)

Pozrite si tiež: V prípade, že ste sa rozhodli použiť odkaz na odkaz, môžete ho použiť:

- [spoločné možnosti](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_6#Common_options)
- [Editor_odkazov](wiki:Gramps_6.0_Wiki_Manuál_-_Vkladanie_a_úprava_údajov:_podrobne_-_časť_2#Editor_odkazov)
- [Internet Address Editor](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1#Internet_Address_Editor).

{{-}}

### <u>Správa o počte predkov</u>

![[_media/TextReports-NumberOfAncestorsReport-example-overview-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Správa o počte predkov - textové správy - prehľad príkladu výstupu]]

Táto správa zobrazuje počet predkov aktívnej osoby.

Hlásenie Počet predkov môžete vybrať pomocou }.

Správa zobrazuje nasledujúce údaje:

  
generácia 1 má 1 jedinca: 100% : toto je osoba, s ktorou ste začali

generácia 2 má 2 osoby : 100% : obaja rodičia sú známi

.....

8\. generácia má 35 jedincov : 27,34 % **to znamená, že z (2\*\*7) 128 možných predkov v 8. generácii je známych 27 %.**

Celkový počet predkov v generácii 2 až ... je tiež uvedený v číslach a percentách. {{-}} Pozri tiež [spoločné možnosti](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_6#Common_options). {{-}}

#### Možnosti hlásenia

![[_media/NumberOfAncestorsReport-TextReports-ReportOptions-tab-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Správa o počte predkov - textové správy - možnosti správy - predvolené možnosti záložky]]

- { stredná osoba pre správu, predvolené nastavenie je aktuálna aktívna osoba.
  - tlačidlo. - Zmena stredovej osoby.

- \- Vyberte formát zobrazenia mien. Tento výber sa zvyčajne preberá z predvoleného nastavenia v [Upraviť &gt; Zobrazenie](wiki:Gramps_6.0_Wiki_Manual_-_Settings/sk#Zobrazenie) na karte . Alebo ak chcete prepísať toto nastavenie pre správu, vyberte z:

  - **Predvolené** - (v novom rodokmeni je to zvyčajne *Priezvisko, daná prípona* )
  - Priezvisko, daná prípona
  - Daná prípona priezviska
  - Dané priezvisko
  - Hlavné priezviská, daná patronymická prípona
  - Priezvisko, dané (bežné)

-  (predvolene začiarkávacie políčko začiarknuté) - či sa majú zahrnúť súkromné údaje.

- Preklad, ktorý sa má použiť pre správu. Výber jazyka zobrazujúci všetky jazyky podporované programom Gramps. Predvolené nastavenie je jazyk, v ktorom používate program Gramps.

{{-}}

### <u>Správa o mieste</u>

![[_media/TextReports-PlaceReport-example-overview-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Správa o mieste - textové správy - prehľad výstupov príkladov]]

Vytvára report podľa miest vybraných používateľom.

Uvedie zoznam súvisiacich osôb a udalostí k vybranému miestu.

Hlásenie o mieste môžete vybrať pomocou }

Pozri tiež [spoločné možnosti](wiki:Gramps_6.0_Wiki_Manuál_-_Reporty_-_časť_6#Spoločné_možnosti). {{-}}

#### Možnosti hlásenia

![[_media/PlaceReport-TextReports-ReportOptions-tab-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Miesto zostavy - Textové zostavy - Možnosti zostavy - predvolené možnosti záložky]]

- Vyberte miesta pomocou vlastného filtra, ktorý ste vytvorili skôr.

- Zoznam miest, o ktorých sa má podať správa.

  - Tlačidlo  - Zobrazí dialógové okno , v ktorom môžete vybrať miesto.
  - Tlačidlo  - Vyberte miesto v zozname a potom stlačte toto tlačidlo na odstránenie miesta.

- \- Ak je správa sústredená na udalosť alebo osobu.

  - **Udalosť** (predvolené)
  - Osoba

{{-}}

#### Možnosti správy (2)

![[_media/PlaceReport-TextReports-ReportOptions2-tab-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Miesto správy - Textové správy - Možnosti správy (2) - predvolené možnosti záložky]]

- \- Vyberte formát zobrazenia názvov. Tento výber sa zvyčajne preberá z predvoleného nastavenia v [Upraviť &gt; Zobrazenie](wiki:Gramps_6.0_Wiki_Manual_-_Settings/sk#Zobrazenie) záložke . Alebo ak chcete prepísať toto nastavenie pre správu, vyberte z:

  - **Predvolené** - (v novom rodokmeni je to zvyčajne *Priezvisko, daná prípona* )
  - Priezvisko, daná prípona
  - Daná prípona priezviska
  - Dané priezvisko
  - Hlavné priezviská, daná patronymická prípona
  - Priezvisko, dané (bežné)

- \- Vyberte formát zobrazenia miest. Tento výber sa zvyčajne preberá z predvoleného nastavenia v [Upraviť &gt; Zobrazenie](wiki:Gramps_6.0_Wiki_Manual_-_Settings/sk#Zobrazenie) na karte . Alebo ak chcete prepísať toto nastavenie pre správu, vyberte z:

  - Predvolené
  - Úplné

-  (štandardne začiarknuté políčko) - či sa majú zahrnúť súkromné údaje.

- \- Ako spracovať (informácie o) žijúcich osobách

  - **Zahrnuté a všetky údaje** (predvolené)
  - Úplné mená, ale odstránené údaje
  - Nahradené mená a odstránené údaje
  - Úplné mená sa nahradia a údaje sa odstránia
  - Nezahŕňa sa

- `0`(predvolené) - či sa majú obmedziť údaje o nedávno zomrelých osobách.

- Preklad, ktorý sa má použiť pre správu. Výber jazyka zobrazujúci všetky jazyky podporované programom Gramps. Predvolené nastavenie je jazyk, v ktorom používate program Gramps.

- Formát a jazyk pre dátumy s príkladmi

  - Predvolené - Vyberte túto možnosť, ak chcete použiť predvolené nastavenie v [Upraviť &gt; Zobrazenie](wiki:Gramps_6.0_Wiki_Manual_-_Settings/sk#Zobrazenie) karte pre možnosť .
  - **RRRR-MM-DD(ISO)(2018-03-14)** (predvolené pre správu)
  - Číselný(14/3/2018)
  - Mesiac Deň, Rok(14. marec 2018)
  - DEŇ MESIACA, ROK(14.3.2018)
  - Deň Mesiac Rok(14. marec 2018)
  - DEŇ MESIAC ROK(14. marca 2018)

{{-}}

### <u>Záznamová správa</u>

![[_media/TextReports-RecordsReport-example-overview-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Správa o záznamoch - textové správy - prehľad príkladu výstupu]]

Report Records (Záznamy) zobrazuje množstvo zaujímavých záznamov (väčšinou súvisiacich s vekom) vo vašej databáze, ako napríklad najstaršia žijúca osoba, najmladšia matka atď.

Hlásenie o záznamoch môžete vybrať pomocou }

K dispozícii je aj identický [Records Gramplet](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Records).

Pozri tiež [spoločné možnosti](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_6#Common_options). {{-}}

#### Možnosti hlásenia

![[_media/RecordsReport-TextReports-ReportOptions-tab-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Záznamová zostava - Textové zostavy - Možnosti zostavy - predvolené možnosti záložky]]

Výber záznamov, ktoré sa majú vytlačiť, je možný a predvolený je primeraný zoznam "pozitívnych záznamov" (väčšina ľudí by napríklad dlhé manželstvo považovala za pozitívny záznam, zatiaľ čo skorý rozvod by skôr považovala za negatívny záznam).

- \- Vyberte filter, ktorý sa má použiť na správu. Vyberte si z nasledujúcich možností:

  - **Celá databáza** (predvolené nastavenie)
  - Potomkovia aktívnej osoby
  - Rodiny potomkov aktívnej osoby
  - Predkovia aktívnej osoby
  - Osoby so spoločným predkom s aktívnou osobou
  - *Každý vlastný filter, ktorý ste vytvorili, bude uvedený pod ostatnými možnosťami.*

- Centrálna osoba pre filter. Predvolené nastavenie je Aktívna osoba.

  - Tlačidlo . - Zmena osoby filtra.

- <kód>3</kód> (predvolené)

- - **Nepoužívať meno volajúceho** (predvolené)
  - Nahraďte krstné mená menom povolania - (pozri Upozornenia)
  - Podčiarknite meno volajúceho v krstných menách / pridajte meno volajúceho ku krstnému menu

- predvolené = prázdne pole

{{-}}

#### Možnosti správy (2)

![[_media/RecordsReport-TextReports-ReportOptions2-tab-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Správa záznamov - Textové správy - Možnosti správy (2) - predvolené možnosti záložky]]

- \- Vyberte formát zobrazenia mien. Tento výber sa zvyčajne preberá z predvoleného nastavenia v [Upraviť &gt; Zobrazenie](wiki:Gramps_6.0_Wiki_Manual_-_Settings/sk#Zobrazenie) záložke . Alebo ak chcete prepísať toto nastavenie pre správu, vyberte z:

  - **Predvolené** - (v novom rodokmeni je to zvyčajne *Priezvisko, daná prípona* )
  - Priezvisko, daná prípona
  - Daná prípona priezviska
  - Dané priezvisko
  - Hlavné priezviská, daná patronymická prípona
  - Priezvisko, dané (bežné)

-  (predvolene začiarkávacie políčko začiarknuté) - či sa majú zahrnúť súkromné údaje.

- \- Ako spracovať (informácie o) žijúcich ľuďoch

  - **Zahrnuté a všetky údaje** (predvolené)
  - Úplné mená, ale odstránené údaje
  - Nahradené mená a odstránené údaje
  - Úplné mená sa nahradia a údaje sa odstránia
  - Nezahŕňa sa

- `0`(predvolené) - či sa majú obmedziť údaje o nedávno zomrelých osobách.

- Preklad, ktorý sa má použiť pre správu. Výber jazyka zobrazujúci všetky jazyky podporované programom Gramps. Predvolené nastavenie je jazyk, v ktorom používate program Gramps.

{{-}}

#### Osoba 1

![[_media/RecordsReport-TextReports-Person1-tab-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Správa záznamov - Textové správy - Osoba 1 - predvolené možnosti záložky]]

-  (štandardne začiarkávacie políčko začiarknuté)

-  (štandardne začiarknuté políčko)

-  (políčko je predvolene nezačiarknuté)

-  (políčko je predvolene začiarknuté)

-  (políčko je predvolene začiarknuté)

-  (políčko je predvolene začiarknuté)

-  (políčko je predvolene nezačiarknuté)

-  (políčko je štandardne nezačiarknuté)

{{-}}

#### Osoba 2

![[_media/RecordsReport-TextReports-Person2-tab-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Správa záznamov - Textové správy - Osoba 2 - predvolené možnosti záložky]]

-  (štandardne začiarkávacie políčko začiarknuté)

-  (štandardne začiarknuté políčko)

-  (políčko je predvolene začiarknuté)

-  (políčko je štandardne začiarknuté)

-  (políčko je predvolene nezačiarknuté)

-  (políčko je štandardne nezačiarknuté)

-  (políčko je štandardne nezačiarknuté)

-  (políčko je štandardne nezačiarknuté)

{{-}}

#### Rodina

![[_media/RecordsReport-TextReports-Family-tab-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Správa záznamov - Textové správy - Rodina - predvolené možnosti záložky]]

-  (štandardne začiarkavacie políčko začiarknuté)

-  (štandardne začiarknuté políčko)

-  (políčko je predvolene začiarknuté)

-  (políčko je štandardne nezačiarknuté)

-  (políčko je štandardne začiarknuté)

-  (políčko je predvolene začiarknuté)

-  (políčko je predvolene začiarknuté)

{{-}}

### <u>Správa o značkách</u>

![[_media/TextReports-TagReport-example-overview-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Tag Report - Textové reporty - prehľad výstupných príkladov]]

Zobrazí zoznam primárnych objektov (osoba, rodina, poznámky), ktoré zodpovedajú vybranému [Tag](wiki:Gramps_6.0_Wiki_Manual_-_Filters#Tagging).

Správu o značkách môžete vybrať pomocou }.

Táto zostava sa predtým v programe Gramps 3.2 nazývala "zostava značiek".

Pozri tiež [spoločné možnosti](wiki:Gramps_6.0_Wiki_Manuál_-_Reporty_-_časť_6#Spoločné_možnosti). {{-}}

#### Možnosti správy

![[_media/TagReport-TextReports-ReportOptions-tab-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Tag Report - Textové reporty - Možnosti reportu - predvolené možnosti karty]]

-   
  Vyberte [Tag](wiki:Gramps_6.0_Wiki_Manual_-_Filters#Tagging), ktorý sa má pre správu použiť.

- } - Vyberte formát zobrazenia názvov. Tento výber sa zvyčajne preberá z predvoleného nastavenia v [Upraviť &gt; Zobrazenie](wiki:Gramps_6.0_Wiki_Manual_-_Settings/sk#Zobrazenie) na karte . Alebo na prepísanie tohto nastavenia pre správu vyberte z:

  - **Predvolené** - (v novom rodokmeni je to zvyčajne *Priezvisko, daná prípona* )
  - Priezvisko, daná prípona
  - Daná prípona priezviska
  - Dané priezvisko
  - Hlavné priezviská, daná patronymická prípona
  - Priezvisko, dané (bežné)

- \- Vyberte formát zobrazenia miest. Tento výber sa zvyčajne preberá z predvoleného nastavenia v [Upraviť &gt; Zobrazenie](wiki:Gramps_6.0_Wiki_Manual_-_Settings/sk#Zobrazenie) na karte . Alebo ak chcete prepísať toto nastavenie pre správu, vyberte z:

  - Predvolené
  - Úplné

-  (štandardne začiarknuté políčko) - či sa majú zahrnúť súkromné údaje.

- \- Ako spracovať (informácie o) žijúcich osobách

  - **Zahrnuté a všetky údaje** (predvolené)
  - Úplné mená, ale odstránené údaje
  - Nahradené mená a odstránené údaje
  - Úplné mená sa nahradia a údaje sa odstránia
  - Nezahŕňa sa

- `0`(predvolené) - či sa majú obmedziť údaje o nedávno zomrelých osobách.

- Preklad, ktorý sa má použiť pre správu. Výber jazyka zobrazujúci všetky jazyky podporované programom Gramps. Predvolené nastavenie je jazyk, v ktorom používate program Gramps.

- Formát a jazyk pre dátumy s príkladmi.

  - Predvolené - Vyberte túto možnosť, ak chcete použiť predvolené nastavenie v [Edit &gt; Display](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Display) na karte .
  - **RRRR-MM-DD(ISO)(2018-03-14)** (predvolené pre správu)
  - Číselný(14/3/2018)
  - Mesiac Deň, Rok(14. marec 2018)
  - DEŇ MESIACA, ROK(14.3.2018)
  - Deň Mesiac Rok(14. marec 2018)
  - DEŇ MESIAC ROK(14. marca 2018)

{{-}}

<hr>

Späť na [Register správ](wiki:Gramps_6.0_Wiki_Manual_-_Reports/sk).

[Category:Sk:Documentation](wiki:Category:Sk:Documentation) [Category:Plugins](wiki:Category:Plugins)
