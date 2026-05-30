---
title: Gramps 6.0 Wiki Manual - Reports - part 5/sk
categories:
- Plugins
- Sk:Documentation
managed: false
source: wiki-scrape
wiki_revid: 117775
wiki_fetched_at: '2026-05-30T20:12:04Z'
lang: sk
---

{{#vardefine:chapter\|13.5}} {{#vardefine:figure\|0}} Naspäť na [Register správ](wiki:Gramps_6.0_Wiki_Manual_-_Reports).

<hr>

{{-}} ![[_media/MenuOverview-Reports-Graphs-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}}  Prehľad menu]] V tejto časti sú popísané rôzne dostupné v programe Gramps.

## Grafy

Tieto zostavy sa vytvárajú pomocou programu [GraphViz](wiki:Výstupné_formáty#Graphviz). Preto je dôležité, aby bol na vašom počítači nainštalovaný program **Graphviz**.

Všetky tri grafické zostavy: Rodinné línie, presýpacie hodiny a grafy vzťahov majú spoločné možnosti: , a .

Taktiež majú spoločné možnosti s ostatnými zostavami [spoločné možnosti](wiki:Gramps_6.0_Wiki_Manuál_-_Zostavy_-_časť_4#Spoločné_možnosti): a .

### Obvyklé možnosti

Existuje aj niekoľko [GraphViz](wiki:Output_formats#Graphviz) špecifických možností týkajúcich sa stránkovania, farby a detailov grafu.

Tento doplnok používa softvér na vizualizáciu grafov Graphviz. Graphviz preberá vygenerované [<code>.gv</code>](wiki:Output_formats#Graphviz) súbory a vytvára z nich konečné súbory, ako napríklad `.gif`, `.png`, `.pdf`, `.ps` atď.

#### Rozloženie Graphviz

![[_media/FamilyLinesGraph-Graphs-GraphvizLayout-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Graf rodinných línií - Grafy - Rozloženie Graphviz - predvolené možnosti karty]]

- } Vyberte rodinu písma. Ak sa medzinárodné znaky nezobrazujú, použite písmo **FreeSans**. FreeSans je k dispozícii z [the NonGNU org](http://www.nongnu.org/freefont/).

  - **Predvolené**
  - PostScript/ Helvetica
  - True Type/ FreeSans

- (`14` predvolené) Veľkosť písma v [bodoch](https://wikipedia.org/wiki/Point_(typografia)).

- Či ide graf zhora nadol alebo zľava doprava

  - **Vertikálne (zhora nadol)** (Predvolené)
  - Vertikálne (zdola nahor)
  - Horizontálne (zľava doprava)
  - Horizontálne (sprava doľava)

- (<kód>1</kód> predvolené) Graphviz dokáže vytvoriť veľmi veľké grafy rozložením grafu na obdĺžnikové pole stránok. Týmto sa riadi počet strán v poli vo vodorovnom smere. **Platí len pre dot a pdf prostredníctvom Ghostscript**.

- (`1` predvolené) Graphviz môže vytvárať veľmi veľké grafy rozložením grafu na obdĺžnikové pole strán. Týmto sa riadi počet strán v poli na výšku. **Platí len pre dot a pdf prostredníctvom Ghostscript**.

- (*Dole, vľavo* predvolené) Poradie, v ktorom sa stránky grafu vypíšu. Táto voľba platí len vtedy, ak je počet horizontálnych strán alebo vertikálnych strán väčší ako 1.

- \- Ako sa budú kresliť čiary medzi objektmi. Vyberte si z nasledujúcich možností:

  - *Rovné*
  - **Zakrivené** (predvolené)
  - *Ortogonálne*

{{-}}

#### Možnosti Graphviz

![[_media/FamilyLinesGraph-Graphs-GraphvizOptions-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Graf rodinných línií - Grafy - Možnosti Graphviz - predvolené možnosti karty]]

- } Výrazne ovplyvňuje, ako je graf rozložený na stránke. Konkrétne rozmiestnenie uzlov a škálovanie grafu( pozri *Rada 1:*).

  - *Komprimovať na minimálnu veľkosť*
  - **Vyplniť danú oblasť** (predvolené)
  - *Rozšíriť rovnomerne*

<hr>

**Rada 1:**

Ak je graf menší ako oblasť tlače:

- *Komprimovať na minimálnu minimálnu veľkosť* nezmení rozstupy medzi uzlami.
- *Vyplniť danú oblasť* zväčší rozstupy uzlov tak, aby sa zmestili do oblasti tlače na šírku aj na výšku.
- *Rozšíriť rovnomerne* rovnomerne zväčší rozstup uzlov, aby sa zachoval pomer strán.

Ak je graf väčší ako oblasť tlače:

- *Komprimovať na minimálnu veľkosť* zmenší graf, aby sa dosiahlo tesné balenie na úkor symetrie.
- *Vyplniť danú oblasť* zmenší graf tak, aby sa zmestil do oblasti tlače po predchádzajúcom zväčšení rozstupu uzlov.
- *Rozšíriť rovnomerne* zmenší graf rovnomerne, aby sa zmestil do oblasti tlače.

<hr>

- (<kód>72</kód> predvolené) bodov na palec. Pri vytváraní PostScriptu alebo PDF použite 72 DPI. Zvyčajne medzi 75 a 120, ak vytvárate súbory .png alebo .gif, ale 300 alebo 600, ak vytvárate súbory určené na tlač. Pri vytváraní obrázkov, napríklad súborov .gif alebo .png pre web, skúste čísla ako 100 alebo 300 DPI.

- (`0,20` predvolené) Minimálne množstvo voľného priestoru v palcoch medzi jednotlivými uzlami. Pri vertikálnych grafoch to zodpovedá odstupu medzi stĺpcami. Pre horizontálne grafy to zodpovedá vzdialenosti medzi riadkami.

- (`0.20` predvolené) Minimálne množstvo voľného priestoru v palcoch medzi radmi. Pre vertikálne grafy to zodpovedá odstupu medzi riadkami. Pre horizontálne grafy to zodpovedá rozstupu medzi stĺpcami.

-  (začiarkavacie políčko je predvolene začiarknuté) Podgrafy môžu pomôcť programu Graphviz umiestniť spoje spolu, ale pri netriviálnych grafoch budú mať za následok dlhšie riadky a väčšie grafy.

#### Poznámka

![[_media/FamilyLinesGraph-Graphs-Note-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Graf rodinných línií - Grafy - Poznámka - predvolené možnosti záložky]]

- (Predvolene prázdne) Tento text sa pridá do grafu

- \- Či sa poznámka zobrazí v hornej alebo dolnej časti stránky.

  - **Horná časť** (predvolené)
  - *Spodná časť*

- (`32` predvolené) Veľkosť textu poznámky v bodoch.

{{-}}

### <u>Graf rodinných línií</u>

![[_media/Graphs-FamilyLinesGraph-example-overview-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Graf rodinných línií - grafy - prehľad výstupov príkladov]]

Vygenerujte pomocou generátora [GraphViz](wiki:Output_formats#Graphviz).

Typickým použitím tejto zostavy je generovanie zjednodušených grafov na tlač na *veľkoformátových tlačových plotroch*.

Ak chcete vytvoriť , z ponuky vyberte a potom z } vyberte aspoň jednu osobu z dialógového okna a správa navrhne, ak je to možné, druhú príbuznú osobu prostredníctvom dialógové okno vyberte alebo podľa toho, ako sa rozhodnete, a potom vyberte na vygenerovanie správy. {{-}} Pozri tiež [obvyklé možnosti](wiki:Gramps_6.0_Wiki_Manuál_-_Reporty_-_časť_5#Obvyklé_možnosti) {{-}}

#### Možnosti správy

![[_media/FamilyLinesGraph-Graphs-ReportOptions-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Graf rodinných línií - Grafy - Možnosti zostavy - predvolené možnosti karty]]

-  Pri určovaní "Rodinných línií" sa budú brať do úvahy rodičia a ich predkovia(zaškrtávacie políčko je predvolene začiarknuté)

- { (štandardne začiarknuté políčko)

-  Ľudia a rodiny, ktoré priamo nesúvisia so záujmovými osobami, budú pri určovaní "rodinných línií" odstránené (začiarkavacie políčko je predvolene začiarknuté).

-   
  Vyberte smer, ktorým budú smerovať šípky:

  - **Potomkovia \<- Predkovia** (predvolené nastavenie) - šípky smerujú k potomkom.
  - *Potomkovia -\> Predkovia* - šípky smerujú k Predkom.
  - *Potomkovia \<-\> Predkovia* - šípky ukazujú na oboch.
  - *Potomkovia - Predkovia* - žiadne (šípky sa nezobrazujú)

- \- Muži sa zobrazia modrou farbou, ženy červenou, ak nie je vyššie nastavené inak pre vyplnené. Ak pohlavie jedinca nie je známe, zobrazí sa sivou farbou.

  - *B&W outline* - Čiernobiely obrys
  - *Farebný obrys*
  - **Farebná výplň** (predvolené nastavenie)

-  na rozlíšenie žien a mužov (predvolene nezačiarknuté políčko)

- , či má obsahovať identifikátory Gramps.

  - **Nezahŕňať**' predvolené nastavenie
  - zahrnúť

{{-}}

#### Možnosti správy (2)

![[_media/FamilyLinesGraph-Graphs-ReportOptions2-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Graf rodinných línií - Grafy - Možnosti zostavy (2) - predvolené možnosti karty]]

- } - Vyberte formát zobrazenia mien. Tento výber sa zvyčajne preberá z predvoleného nastavenia v [Upraviť &gt; Zobrazenie](wiki:Gramps_6.0_Wiki_Manual_-_Settings/sk#Zobrazenie) záložke . Alebo ak chcete prepísať toto nastavenie pre správu, vyberte z:

  - **Predvolené** - (v novom rodinnom strome je to zvyčajne *Priezvisko, daná prípona* )
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
  - Úplné mená nahradené a údaje odstránené
  - Nezahŕňa sa

- `0`(predvolené) - či sa majú obmedziť údaje o nedávno zomrelých osobách.

- Preklad, ktorý sa má použiť pre správu. Výber jazyka zobrazujúci všetky jazyky podporované programom Gramps. Predvolené nastavenie je jazyk, v ktorom používate program Gramps.

- Formát a jazyk pre dátumy s príkladmi.

  - Predvolené - Vyberte túto možnosť, ak chcete použiť predvolené nastavenie v [Upraviť &gt; Zobrazenie](wiki:Gramps_6.0_Wiki_Manual_-_Settings/sk#Zobrazenie) na karte .
  - **RRRR-MM-DD(ISO)(2018-03-14)** (predvolené pre správu)
  - Číselný(14/3/2018)
  - Mesiac Deň, Rok(14. marec 2018)
  - DEŇ MESIACA, ROK(14.3.2018)
  - Deň Mesiac Rok(14. marec 2018)
  - DEŇ MESIAC ROK(14. marca 2018)

{{-}}

#### Osoby záujmu

![[_media/FamilyLinesGraph-Graphs-PeopleOfInterest-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Graf rodinných línií - grafy - záujmové osoby - predvolené možnosti karty]]

Graf funguje tak, že začína zoznamom "osôb záujmu". Tento počiatočný zoznam ľudí sa potom použije na vyhľadanie predkov aj potomkov.

- kliknutím na a pridáte/odstránite osoby záujmu. Ak máte pochybnosti, skúste na začiatok pridať svojich starých rodičov.

-  (zaškrtávacie políčko je štandardne nezaškrtnuté)

  - `50` predvolené nastavenie. Maximálny počet predkov, ktorý sa má zahrnúť. Maximálny počet sa týka celkového počtu osôb, nie generácií, ktoré sa majú zobraziť v grafe.

-  (začiarkavacie políčko predvolene nezačiarknuté)

  - `50` predvolené nastavenie. Maximálny počet potomkov, ktorý sa má zahrnúť. Maximálny počet sa týka celkového počtu osôb, nie generácií, ktoré sa majú zobraziť v grafe.

{{-}}

#### Include

![[_media/FamilyLinesGraph-Graphs-Include-tab-52.png|Obrázok {{#var:kapitola}}.{{#vardefineecho:obrázok|{{#expr:{{#var:obrázok}}+1}}}} Graf rodinných línií - Grafy - Zahrnúť - predvolené možnosti karty]]

- { : dátum narodenia, dátum úmrtia a dátumy sobáša budú zahrnuté do grafu, ak je táto možnosť zvolená. (začiarkavacie políčko je predvolene začiarknuté)

- : z vyššie uvedeného sa zobrazia len roky (zaškrtávacie políčko je predvolene nezačiarknuté).

- : miesto narodenia, miesto úmrtia a miesto sobáša budú zahrnuté do grafu, ak je táto možnosť zaškrtnutá (políčko je štandardne zaškrtnuté).

- : text manželstva bude obsahovať celkový počet detí, keď je táto možnosť zaškrtnutá (zaškrtávacie políčko je štandardne nezaškrtnuté).

-  (začiarkavacie políčko je predvolene začiarknuté)

- - **Nad menom**' (predvolené nastavenie)
  - Vedľa mena

- - **Normálne** (predvolené)
  - Veľký

{{-}}

#### Farby rodiny

![[_media/FamilyLinesGraph-Graphs-FamilyColours-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}}} Graf rodinných línií - Grafy - Farby rodiny - predvolené možnosti karty]]

- } Vyberte farbu, ktorá sa má použiť pre ľudí s konkrétnym priezviskom. K dispozícii sú dva stĺpce: *Priezvisko* a *Farba*. Kliknutím na alebo pridáte priezvisko z okna , vyberiete priezvisko a stlačíte . Ak chcete upraviť farbu priezviska, dvakrát kliknite na priezvisko a v okne vyberte jednu zo zobrazených farieb a potom vyberte .

{{-}}

#### Individuals

![[_media/FamilyLinesGraph-Graphs-Individuals-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Graf rodinných línií - Grafy - Jednotlivci - predvolené možnosti karty]]

V okne môžete vybrať farbu pre každú z nasledujúcich možností a potom vybrať tlačidlo .

- farbu, ktorá sa má použiť pre mužov.

- farbu, ktorá sa použije pre ženy.

- { farba, ktorá sa použije, ak nie je známe pohlavie (a pre ľudí, ktorých priezvisko sa nezhoduje so žiadnym z mien na karte "Farby rodiny").

- farba, ktorá sa použije pre rodiny (svadby).

{{-}}

### <u>Graf presýpacích hodín</u>

![[_media/Graphs-HourglassGraph-example-overview-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Graf presýpacích hodín - grafy - prehľad výstupov príkladov]]

Vygenerujte graf presýpacích hodín pomocou generátora [GraphViz](wiki:Output_formats#Graphviz). Prejdite na }. {{-}} Pozrite si tiež [Obecné možnosti](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_5/sk#Obecné_možnosti) {{-}}

#### Možnosti správy

![[_media/HourglassGraph-Graphs-ReportOptions-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Graf presýpacích hodín - Grafy - Možnosti zostavy - predvolené možnosti karty]]

- { stredová osoba pre report, predvolene je to aktuálna aktívna osoba.
  - tlačidlo. - Zmena stredovej osoby.

- Predvolené `10`

- predvolené `10`

-   
  Vyberte smer, ktorým budú smerovať šípky:

  - (predvolené) - šípky smerujú na potomkov.
  - *Potomkovia -\> Predkovia* - šípky smerujú k Predkom.
  - *Potomkovia \<-\> Predkovia* - šípky ukazujú na oboch.
  - *Potomkovia - Predkovia* - žiadne (šípky sa nezobrazujú)

- \- Muži sa zobrazia modrou farbou, ženy červenou, ak nie je vyššie nastavené inak pre vyplnené. Ak pohlavie jedinca nie je známe, zobrazí sa sivou farbou.

  - *B&W outline* - Čiernobiely obrys
  - *Farebný obrys*
  - **Farebná výplň** (predvolené nastavenie)

-  na rozlíšenie žien a mužov (predvolene nezačiarknuté políčko)

- , či má obsahovať identifikátory Gramps.

  - **Nezahŕňať**' predvolené nastavenie
  - zahrnúť

{{-}}

#### Možnosti správy (2)

![[_media/HourglassGraph-Graphs-ReportOptions2-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Graf presýpacích hodín - Grafy - Možnosti zostavy (2) - predvolené možnosti karty]]

- } - Vyberte formát zobrazenia názvov. Tento výber sa zvyčajne preberá z predvoleného nastavenia v [Upraviť &gt; Zobrazenie](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Zobrazenie) záložke . Alebo na prepísanie tohto nastavenia pre správu vyberte z:

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

  - Predvolené - Vyberte túto možnosť, ak chcete použiť predvolené nastavenie v [Upraviť &gt; Zobrazenie](wiki:Gramps_6.0_Wiki_Manual_-_Settings/sk#Zobrazenie) na karte .
  - **RRRR-MM-DD(ISO)(2018-03-14)** (predvolené pre správu)
  - Číselný(14/3/2018)
  - Mesiac Deň, Rok(14. marec 2018)
  - DEŇ MESIACA, ROK(14.3.2018)
  - Deň Mesiac Rok(14. marec 2018)
  - DEŇ MESIAC ROK(14. marca 2018)

{{-}}

#### Graph Style

![[_media/HourglassGraph-Graphs-GraphStyle-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}}} Graf presýpacích hodín - Grafy - Štýl grafu - predvolené možnosti karty]]

V okne môžete vybrať farbu pre každú z nasledujúcich možností a potom vybrať tlačidlo .

- farbu, ktorá sa má použiť pre mužov.

- farbu, ktorá sa použije pre ženy.

- { farba, ktorá sa použije, ak nie je známe pohlavie (a pre ľudí, ktorých priezvisko sa nezhoduje so žiadnym z mien na karte "Farby rodiny").

- farba, ktorá sa použije pre rodiny (svadby).

{{-}}

### <u>Graf vzťahov</u>

![[_media/Graphs-RelationshipGraph-example-overview-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Graf vzťahov - grafy - prehľad výstupov príkladov]]

Graf vzťahov vytvára komplexný graf vzťahov vo formáte [GraphViz](wiki:Output_formats#Graphviz).

Prostredníctvom ponuky: {Graf vzťahov...}}. Zobrazí sa okno , v ktorom môžete zmeniť všetky nastavenia. {{-}} Pozri tiež [Obecné možnosti](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_5/sk#Obecné_možnosti). {{-}}

#### Možnosti správy

![[_media/RelationshipGraph-Graphs-ReportOptions-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Graf vzťahov - Grafy - Možnosti zostavy - predvolené možnosti karty]]

- \- Vyberte filter, ktorý sa má použiť na správu. Vyberte si z nasledujúcich možností:

  - (Predvolené) ()
  - Potomkovia aktívnej osoby
  - Rodiny potomkov aktívnej osoby
  - Predkovia aktívnej osoby
  - Osoby so spoločným predkom s aktívnou osobou
  - *Každý vlastný filter, ktorý ste vytvorili, bude uvedený pod ostatnými možnosťami.*

- Centrálna osoba pre filter. Predvolené nastavenie je Aktívna osoba. Ak používate vlastný filter, nie je možné vybrať žiadnu osobu.

  - Tlačidlo . - Zmena osoby filtra.

-   
  Vyberte smer, ktorým smerujú šípky:

  - **Potomkovia \<- Predkovia** (predvolené nastavenie) - šípky smerujú na Potomkov.
  - *Potomkovia -\> Predkovia* - šípky smerujú k Predkom.
  - *Potomkovia \<-\> Predkovia* - šípky ukazujú na oboch.
  - *Potomkovia - Predkovia* - žiadne (šípky sa nezobrazujú)

- \- Muži sa zobrazia modrou farbou, ženy červenou, ak nie je vyššie nastavené inak pre vyplnené. Ak pohlavie jedinca nie je známe, zobrazí sa sivou farbou.

  - *B&W outline* - Čiernobiely obrys
  - *Farebný obrys*
  - **Farebná výplň** (predvolené nastavenie)

-  Použiť zaoblené rohy na rozlíšenie žien a mužov (začiarkavacie políčko je predvolene nezačiarknuté)

- či má obsahovať identifikátory Gramps.

  - **Nezahŕňať**' predvolené nastavenie
  - zahrnúť

{{-}}

#### Možnosti správy (2)

![[_media/RelationshipGraph-Graphs-ReportOptions2-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Graf vzťahov - Grafy - Možnosti zostavy (2) - predvolené možnosti karty]]

- } - Vyberte formát zobrazenia mena. Tento výber sa zvyčajne preberá z predvoleného nastavenia v [Upraviť &gt; Zobrazenie](wiki:Gramps_6.0_Wiki_Manual_-_Settings/sk#Zobrazenie) záložke . Alebo ak chcete prepísať toto nastavenie pre správu, vyberte z:

  - **Predvolené** - (v novom rodinnom strome je to zvyčajne *Priezvisko, daná prípona* )
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

  - Predvolené - Vyberte túto možnosť, ak chcete použiť predvolené nastavenie v [Upraviť &gt; Zobrazenie](wiki:Gramps_6.0_Wiki_Manual_-_Settings/sk#Zobrazenie) na karte .
  - **RRRR-MM-DD(ISO)(2018-03-14)** (predvolené pre správu)
  - Číselný(14/3/2018)
  - Mesiac Deň, Rok(14. marec 2018)
  - DEŇ MESIACA, ROK(14.3.2018)
  - Deň Mesiac Rok(14. marec 2018)
  - DEŇ MESIAC ROK(14. marca 2018)

{{-}}

#### Include

![[_media/RelationshipGraph-Graphs-Include-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Graf vzťahov - Grafy - Zahrnúť - predvolené možnosti karty]]

- \- Či sa majú zahrnúť dátumy a/alebo miesta

  - **Neobsahovať žiadne dátumy ani miesta** (predvolené)
  - Zahrnúť dátumy (narodenia, sobáša, úmrtia), ale žiadne miesta
  - Zahrnúť dátumy (narodenia, sobáša, úmrtia) a miesto
  - Zahrnúť dátumy (narodenia, sobáša, úmrtia) a miesto, ak nie sú uvedené žiadne dátumy
  - Zahrnúť roky (narodenia, sobáša, úmrtia), ale bez miest
  - Uveďte roky (narodenia, sobáša, úmrtia) a miesta
  - Zahrnúť miesta (narodenie, sobáš, úmrtie), ale bez dátumov
  - Zahrnúť dátumy (narodenia, sobáša, úmrtia) a miesta na tom istom riadku

-  (predvolene nezačiarknuté políčko)

-  (predvolene nezačiarknuté políčko)

-  (políčko je predvolene nezačiarknuté)

- Kde sa má obrázok miniatúry zobraziť vzhľadom na meno

  - **Nad menom** (predvolené nastavenie)
  - Vedľa mena

- Či sa má zahrnúť posledné povolanie

  - **Neuvádzať žiadne povolanie** (predvolené)
  - Zahrnúť opis posledného povolania
  - Zahrnúť dátum, opis a miesto všetkých zamestnaní

{{-}}

#### Grafický štýl

![[_media/RelationshipGraph-Graphs-GraphStyle-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Graf vzťahov - Grafy - Štýl grafu - predvolené možnosti karty]]

V okne môžete vybrať farbu pre každú z nasledujúcich možností a potom vybrať tlačidlo .

- farbu, ktorá sa má použiť pre mužov.

- farbu, ktorá sa použije pre ženy.

- farba, ktorá sa použije, ak nie je známe pohlavie (a pre ľudí, ktorých priezvisko sa nezhoduje so žiadnym z mien na karte "Farby rodiny").

- farba, ktorá sa použije pre rodiny (svadby).

-  (predvolene zaškrtnuté políčko) - Zobrazuje adoptované vzťahy.

-  (štandardne začiarknuté políčko)

{{-}}

#### Príklad

![[_media/Graphs-RelationshipGraph-example-overview-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Graf vzťahov - grafy - prehľad výstupov príkladov]]

Urobme si jednoduchý príklad. Chceme graf vzťahov s Rodinami potomkov určitej osoby.

1.  Najprv skontrolujte, či je táto osoba *aktívna osoba*. (Neskôr to môžete zmeniť, ale takto je to praktickejšie)
2.  Prejdite cez ponuku
3.  Veľkosť papiera : A4 metrická krajina: vieme, že na grafe nebude príliš veľa ľudí, takže to je v poriadku
4.  Možnosti správy: filter: Potomkovia rodín..., Farebná výplň, Použiť zaoblené rohy
5.  Štýl grafu: Zobraziť uzly rodiny
6.  Graphviz Layout: Rozloženie grafu: V prípade, že je to možné, je potrebné, aby sa rodokmene nachádzali v rodinných domoch: Veľkosť písma: 15 pts FreeSans Smer: zhora nadol
7.  Možnosti grafického zobrazenia: Zvoľte, či sa má používať: Vyplniť danú oblasť dpi 133
8.  Poznámka : pridávame nadpis na hornú časť veľkosť: 18 pts
9.  Výstupný formát: chceme súbor JPEG.

Výsledok je podobný obrázku zobrazenému vpravo odtiaľto. {{-}} Pozrite si tiež:

- Podrobný návod [Ako vytvoriť graf vzťahov](wiki:Howto:_Make_a_relationship_chart)

{{-}}

<hr>

Späť na [Register správ](wiki:Gramps_6.0_Wiki_Manual_-_Reports/sk).

[Category:Sk:Documentation](wiki:Category:Sk:Documentation) [Category:Plugins](wiki:Category:Plugins)
