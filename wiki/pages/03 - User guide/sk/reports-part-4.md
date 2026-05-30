---
title: Gramps 6.0 Wiki Manual - Reports - part 4/sk
categories:
- Plugins
- Sk:Documentation
- Stub
managed: false
source: wiki-scrape
wiki_revid: 125649
wiki_fetched_at: '2026-05-30T20:11:00Z'
lang: sk
---

{{#vardefine:chapter\|13.4}} {{#vardefine:figure\|0}} Naspäť na [Register správ](wiki:Gramps_6.0_Wiki_Manual_-_Reports/sk).

<hr>

{{-}} ![[_media/MenuOverview-Reports-GraphicalReports-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}}  Prehľad ponuky]] V tejto časti sú popísané rôzne dostupné v programe Gramps.

## Grafické správy

Grafické zostavy predstavujú informácie vo forme tabuliek a grafov. Väčšina možností je pre grafické zostavy spoločná, preto budú opísané len raz, na konci tejto časti. Niekoľko možností, ktoré sú špecifické pre danú zostavu, bude opísaných priamo v položke danej zostavy. Pozri tiež [Zastupiteľné hodnoty](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_2#Zastupiteľné_hodnoty).

V programe Gramps sú k dispozícii nasledujúce grafické zostavy:

### Všeobecné možnosti

Bežné možnosti pre textové zostavy sú názov súboru výstupu, formát výstupu, zvolený štýl, veľkosť a orientácia strany. Pre HTML zostavy nie sú k dispozícii žiadne informácie o stránke. Namiesto toho možnosti HTML zahŕňajú výber šablóny HTML, ktorá je k dispozícii v programe Gramps alebo vami definovanú vlastnú šablónu. Voliteľne možno výkazy okamžite otvoriť pomocou predvolenej aplikácie.

Možnosti, ktoré sú špecifické pre danú zostavu, budú popísané priamo v položke tejto zostavy a na [Odkazy na príkazový riadok](wiki:Gramps_6.0_Wiki_Manual_-_Príkazový_riadok/sk#Opcie_akcie).

Pre každú zostavu je k dispozícii obrazovka, ktorá má v hornej časti záložky (ako Možnosti papiera...) a v dolnej časti **Možnosti dokumentu**. Počet záložiek sa líši v závislosti od zostavy.

#### Možnosti papiera

![[_media/TextReports-PaperOptions-tab-defaults-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Možnosti papiera - karta pre grafické zostavy]]

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

Pozri tiež dialógové okno, ktoré sa môže objaviť, ak je vaša vlastná veľkosť stránky príliš veľká. {{-}}

#### Možnosti dokumentu

Možnosti uvedené nižšie sa mierne zmenia v závislosti od zvoleného výstupného formátu. ![[_media/GraphicalReports-DocumentOptions-section-SVG-document-output-settings-example-60.png|figure {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Možnosti dokumentu - dokument SVG - vybraný výstup - príklad]]

- vyberte výstupný formát:

  - *Dokument SVG* : (Scalable Vector Graphics) na zobrazenie pomocou webového prehliadača alebo na úpravu pomocou vhodného grafického editora.
  - *PostScript*
  - *OpenDocument Text* (ak chcete správu upravovať pomocou Libreoffice/Openoffice)
  - *Dokument PDF*
  - *Tlačiť...*

- : môžete označiť, aby ste vytvorený dokument otvorili svojím predvoleným prehliadačom. otvorí vytvorenú správu pomocou akéhokoľvek programu, ktorý je definovaný vo vašom systéme na spracovanie vybraného formátu (zaškrtávacie políčko je predvolene nezaškrtnuté).

- predvolená hodnota je *<kód>/home/<užívateľské meno>/<názov rodinného stromu><názov správy>.<prípona výstupného formátu></kód>*. predvolene je názov súboru rovnaký ako typ správy a bude umiestnený vo vašom domovskom adresári. (V systéme Windows je to predvolene o jednu úroveň vyššie ako "Moje dokumenty").

- (predvolené nastavenie je *predvolené*). Pomocou tlačidla môžete pridávať štýly dokumentov.

- (**priehľadné pozadie**' predvolené)

{{-}}

#### Vyberte osobu pre výber správy

Selektor umožňuje vybrať už existujúcu osobu pre správu a po jej výbere bude umiestnená do ako Stredová osoba. ![[_media/SelectAPersonForTheReport-SelectorDialog-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;Výber osoby pre správu&quot; - dialógové okno výberu - príklad]]

V predvolenom nastavení je to aktuálna aktívna osoba.

Môžete začiarknúť políčko , aby sa zobrazil celý zoznam osôb v strome (políčko je predvolene nezačiarknuté). {{-}}

#### Možnosti zväčšenia a zmeny veľkosti

Strom sa najprv vytvorí na plátne, na ktoré sa zmestí strom ľubovoľnej veľkosti. Na tomto plátne môžete nasledujúcimi možnosťami zmeniť spôsob jeho konečného zobrazenia na stránke. {{-}}

##### :

Táto možnosť zväčší/zmenší veľkosť správy na plátne tak, aby sa zmestila na veľkosť strany (nastavenú v položke Paper Options (Možnosti papiera)), na ktorú chcete tlačiť. V súčasnosti môžete:

- **Neškálovať strom** (predvolené nastavenie)
- *Škálovať strom len na šírku stránky*
- *Škálovať strom tak, aby zodpovedal veľkosti stránky* (šírka aj výška)

Bez začiarknutia možnosti Začiarkavacie políčko: sa pri voľbách *Scale tree to fit* (Zmenšiť strom podľa veľkosti) vyskytnú nasledujúce situácie:

- *Neupravovať mierku stromu* vám môže poskytnúť správu, ktorá sa rozprestiera na viacerých stranách horizontálne a/alebo vertikálne.
- "Škálovať strom len na šírku stránky" môže stále poskytnúť zostavu, ktorá sa rozprestiera na viacerých stranách vertikálne. Žiadne stránky po stranách ostatných. Len jedna nad druhou.
- *Scale tree to fit the size of the page* (Zmenšiť strom tak, aby sa prispôsobil veľkosti stránky) vám poskytne správu len na jednu stranu. Správa sa vytlačí na stranu veľkosti nastavenej v položke Paper Options (Možnosti papiera).

##### 

Táto voľba určuje, na akú veľkú/malú stranu budeme meniť veľkosť strany, na ktorú sa bude tlačiť. **Pri nezačiarknutej tejto možnosti** sa použije veľkosť strany, ktorá je nastavená v položke Paper Option (Možnosti papiera). Pri začiarknutí tejto možnosti sa na základe troch možností v položke stane nasledovné.

Toto prepíše/ignoruje nastavenia v časti Možnosti papiera a vytlačí na stránku rovnaké rozmery, aké používa strom na plátne. Ak teda vezmeme tri vyššie uvedené možnosti, v položke Scale tree to fit (Mierka stromu podľa veľkosti) sa stane toto, ak vyberiete možnosť 'Resize Page to Fit Tree size (Zmeniť veľkosť stránky podľa veľkosti stromu)':

- Táto možnosť bude úplne ignorovať nastavenie v položke Paper Options (Možnosti papiera) a vytlačí sa na stránku, ktorá je dostatočne veľká na zobrazenie celého stromu.
- S voľbou *Scale tree to fit page width only* (Zmenšiť strom len na šírku stránky) bude táto voľba ignorovať iba výšku papiera, ktorá je nastavená v Paper Options (Možnosti papiera). Strom už bol zmenšený/zmenšený tak, aby sa prispôsobil šírke strany, takže je nastavený. Na základe výšky stromu, ktorý tlačíme, sa nastaví iba Výška strany.
- Pri funkcii *Scale tree to fit the size of the page* (Škálovať strom podľa veľkosti strany) už bol strom zmenšený na veľkosť strany. Ale ako je uvedené vyššie, buď šírka, alebo výška bude (s veľkou pravdepodobnosťou) obsahovať medzeru (prázdne biele miesto). Príkaz túto medzeru na stránke zmenší a odstráni ju.

##### inter-box Y scale factor

  
Zväčšiť alebo zmenšiť medzipriestor Y

##### box shadow scale factor

  
Zväčšite alebo zmenšite tieň boxu

##### Viete, na čo chcete tlačiť

Škálovanie stromu je pokročilá funkcia. Na to slúži . → nastavuje veľkosť textu, ktorý môžete tlačiť. Zmenšovanie nie je veľmi žiaduce, pretože text sa stáva ťažšie čitateľným. Zväčšenie je lepšie, ale môže mať určité problémy. Tu je teda niekoľko tipov, ako vytvoriť pekné tlačené dokumenty.

Po prvé. Na aké veľkosti papiera môžete tlačiť? Opýtajte sa a zistite, na aké veľkosti strán môžete ľahko tlačiť. Už len to, že viete, na aké veľkosti papiera môžete tlačiť, veľmi pomáha. V spoločnosti Kinkos (v USA) je k dispozícii tlačiareň so šírkou 3 stopy a papierom, ktorý je na rolke (ľubovoľnej dĺžky). Takže by sme na to mohli použiť "Scale report to fit page width only" (Škálovať zostavu tak, aby sa zmestila len na šírku strany) a "One page report" (Jednostranná zostava).

Za zmienku stojí aj to, aby ste najprv vytvorili zostavu pomocou možnosti *Nezmenšovať zostavu* a , aby ste vedeli, aké sú úplné rozmery zostavy (šírka a výška). To vám pomôže zistiť, ako lepšie umiestniť túto zostavu na stránky, ktoré môžete vytlačiť. Tu je niekoľko ďalších rýchlych vecí, ktoré treba vziať do úvahy.

- Správa, ktorá je veľmi vysoká a nie príliš široká, sa môže lepšie tlačiť len s možnosťou *Zmenšiť správu tak, aby sa zmestila len na šírku strany*.
- Pri normálnej šírke zostavy, ktorá sa bude tlačiť lepšie? Na šírku alebo na výšku?
- Keďže šírka každého políčka je nastavená podľa najširšieho políčka, môžete použiť možnosť Zostupné zostavy → Nahradiť na skrátenie alebo odstránenie veľmi dlhých častí, ktoré nie sú potrebné?
- Veľkosť názvu. Ak je v ňom miesto, môžete nadpis zväčšiť. A ak je príliš veľký, nastaví sa šírka zostavy.

{{-}}

<hr>

### <u>Strom predkov</u>

![[_media/GraphicalReports-AncestorTree-example-landscape-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Strom predkov - grafické prehľady - prehľad výstupných príkladov]]

Táto zostava generuje graf osôb, ktoré sú predkami Aktívnej osoby.

Report Strom predkov môžete vybrať pomocou }. {{-}} Pozri tiež [spoločné možnosti](wiki:Gramps_6.0_Wiki_Manuál_-_Reporty_-_časť_4#Spoločné_možnosti). {{-}}

#### Možnosti stromu

![[_media/AncestorTree-GraphicalReports-TreeOptions-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Strom predkov - Grafické prehľady - Možnosti stromu - predvolené možnosti karty]]

Tu sa vyberá . Aktívna osoba bude predvolená.

- 

Pomocou vstupného poľa môžete zmeniť počet zohľadnených generácií.

vám umožní vybrať, koľko generácií prázdnych polí sa má zobraziť, keď strom nie je úplne plný.

Tu sa nachádza aj začiarkávacie políčko .

{{-}}

#### Možnosti správy

![[_media/AncestorTree-GraphicalReports-ReportOptions-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Strom predkov - Grafické zostavy - Možnosti zostavy - predvolené možnosti karty]]

Táto karta poskytuje možnosť zahrnúť do správy ďalšie položky.

umožňuje vybrať názov správy.

- *Netlačiť názov*
- *Zahrnúť názov správy*

A táto karta obsahuje aj začiarkávacie políčka pre , a .

zväčší alebo zmenší strom tak, aby sa zmestil na stránku podľa potreby. Možnosti sú:

- Neškálovať strom
- Zmenšiť strom tak, aby sa prispôsobil iba šírke stránky
- Zmenšiť strom tak, aby sa prispôsobil veľkosti stránky

kde zväčší alebo zmenší stránku tak, aby sa prispôsobila stromu.

Ak sú vybrané obe možnosti, možnosti sa uskutočnia v tomto poradí; najprv sa škáluje strom a potom stránka.

Tieto dve možnosti sú lepšie popísané v [spoločné možnosti](wiki:Gramps_6.0_Wiki_Manuál_-_Reporty_-_časť_4#Spoločné_možnosti) s tipmi na vytvorenie krajších reportov. {{-}}

#### Možnosti správy (2)

![[_media/AncestorTree-GraphicalReports-ReportOptions2-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figurr|{{#expr:{{#var:figure}}+1}}}} Strom predkov - Grafické zostavy - Možnosti zostavy (2) - predvolené možnosti záložky]]

- Vyberte formát zobrazenia mien. Vyberte si z nasledujúcich možností

  - **Priezvisko, prípona** (predvolené)
  - Dané priezvisko s príponou
  - Dané priezvisko
  - Hlavné priezviská, daná patronymická prípona
  - Priezvisko, dané (bežné)

-   
  Vyberte, či chcete do správy zahrnúť alebo nezahrnúť žijúce osoby. Vyberte si z nasledujúcich možností

  - **Zahrnúť a všetky údaje** (predvolené)
  - Úplné mená, ale odstránené údaje
  - Nahradené mená a odstránené údaje
  - Úplné mená nahradené a údaje odstránené
  - Nezahŕňa sa

-   
  Vyberte počet rokov od úmrtia, za ktoré sa majú osoby v správe považovať. Umožňuje zahrnúť alebo vylúčiť nedávno zosnulé osoby do správy. Predvolená hodnota je 0 rokov.

  -  (predvolene začiarkávacie políčko začiarknuté)

-   
  Preklad, ktorý sa má použiť v správe.

  - Výber jazyka

-   
  Vyberte formát zobrazenia dátumov. Vyberte si z možností **RRRR-MM-DD (ISO)(2018-04-08)**(predvolené) / Číselné (8. 4. 2018) / Mesiac Deň, Rok (8. 4. 2018) / Po Deň, Rok (8. 4. 2018)/ Deň Mesiac Rok (8. 4. 2018)/ Deň Po Rok (8. 4. 2018)

{{-}}

#### Zobrazenie

![[_media/AncestorTree-GraphicalReports-Display-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Strom predkov - Grafické zostavy - Zobrazenie - predvolené možnosti karty]]

Táto záložka umožňuje určiť , ktorý sa má použiť pre správu. Tento formát budú používať všetci otcovia, starí otcovia atď.

, ktorý sa použije pre všetky matky, staré matky atď. bude používať tento formát.

Označenie {} okolo riadku s informáciami o úmrtí uvádza, že text "d. ' sa bude zobrazovať len vtedy, keď sa zobrazí informácia o úmrtí. Viac informácií vrátane spôsobu zahrnutia miest a atribútov a formátovania mien a dátumov a miest nájdete v časti [Substitučné hodnoty](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_2/sk).

umožňuje určiť, či stredová osoba používa formát zobrazenia otca alebo formát zobrazenia matky, ktorý sa nachádza na karte Zobrazenie.

určuje, či sa má medzi otcom a matkou zobraziť dodatočné pole, ktoré obsahuje informácie o manželstve. (pozri [Substitučné hodnoty](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_2/sk)) určuje, čo sa bude tlačiť v tomto rámčeku.

{{-}}

#### Rozšírené

![[_media/AncestorTree-GraphicalReports-Advanced-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Strom predkov - Grafické prehľady - Rozšírené - predvolené možnosti karty]]

- }: To vám umožňuje vložiť dvojice reťazcov oddelených znakom '/', ktoré určujú text, ktorý chcete nahradiť iným textom. Napríklad

      Spojené štáty americké/USA

  nahradí Spojené štáty americké textom USA.

  -  Môžete začiarknúť políčko Zahrnúť poznámku, ak chcete pridať poznámku (políčko je predvolene nezačiarknuté). určuje text, ktorý bude poznámka obsahovať.

-   
  Určte, kde na stránke sa má poznámka umiestniť (predvolene je vľavo dole).

"\$T" v rámci poznámky sa zobrazí deň, kedy bola správa vytvorená. Uplatní sa bežné formátovanie dátumu (pozri [Zástupné hodnoty](wiki:Gramps_6.0_Wiki_Manuál_-_Zoznamy_-_časť_2)). V súčasnosti sa k rohu pripojí poznámka. Ak sa cez ňu napíše políčko osoby, políčko poznámky sa nepresunie. Ak sa tak stane, vyberte iný roh, aby sa zobrazil záložka poznámky.

-   
  Zväčšite alebo zmenšite medzipoložku (predvolená hodnota je 1,00 in.).

-   
  Zväčšite alebo zmenšite tieň boxu (predvolená hodnota je 1,00 palca).

Tieto dve možnosti sú lepšie opísané v [Možnosti veľkosti](wiki:Gramps_6.0_Wiki_Manuál_-_Reporty_-_časť_4#Možnosti_rozmeru_a_veľkosti) s tipmi na vytvorenie krajších reportov.

{{-}}

### <u>Kalendár</u>

![[_media/GraphicalReports-Calendar-example-landscape-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Kalendár - Grafické zostavy - prehľad výstupov príkladov]]

Táto zostava vytvára kalendár s narodeninami a výročiami na stránke podľa mesiacov.

Správu Kalendár si môžete vybrať pomocou }.

Rovnaké informácie, ale v textovom formáte, môžete vytlačiť pomocou [Report narodenín a výročí](wiki:Gramps_6.0_Wiki_Manuál_-_Reporty_-_časť_6#Report_narodenín_a_výročí).

Vysvetlenie, ako pridať alebo zmeniť sviatky zobrazené na výstupe tohto kalendára, nájdete v časti [Calendar tools holidays](wiki:Calendar_tools_holidays). {{-}} Pozri tiež [Obecné možnosti](wiki:Gramatika_6.0_Wiki_Manuál_-_Zprávy_-_časť_4#Obecné_možnosti). {{-}}

#### Možnosti správy

![[_media/Calendar-GraphicalReports-ReportOptions-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Kalendár - Grafické zostavy - Možnosti zostavy - predvolené možnosti karty]]

- vybrať medzi

  - **Celá databáza** (predvolené nastavenie)
  - Potomkovia aktívnej osoby
  - Rodiny potomkov aktívnej osoby
  - Predkovia aktívnej osoby
  - Ľudia so spoločným predkom s aktívnou osobou

- Stredová osoba pre správu je zvyčajne aktívna osoba, pokiaľ nepoužijete :

  - tlačidlo na použitie dialógového okna výberu.

- (`Môj kalendár` predvolené) Prvý riadok textu v spodnej časti kalendára.

- (`Produced by Gramps` predvolené) Druhý riadok textu v spodnej časti kalendára.

- ([`http://gramps-project.org/`](http://gramps-project.org/) predvolené) Tretí riadok textu v spodnej časti kalendára.

{{-}}

#### Možnosti správy (2)

![[_media/Calendar-GraphicalReports-ReportOptions2-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Kalendár - Grafické zostavy - Možnosti zostavy (2) - predvolené možnosti karty]]

- Vyberte formát zobrazenia názvov. Vyberte si z nasledujúcich možností

  - **Priezvisko, prípona** (predvolené)

  - Dané priezvisko s príponou

  - Dané priezvisko

  - Hlavné priezviská, daná patronymická prípona

  - Priezvisko, dané (bežné)

  -  (predvolene začiarknuté políčko)

  -  (štandardne začiarknuté políčko)

- Preklad, ktorý sa má použiť pre správu.

  - Výber jazyka

{{-}}

#### Obsah

![[_media/Calendar-GraphicalReports-Content-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Kalendár - Grafické zostavy - Obsah - predvolené možnosti záložky]]

- vyplňte rok. Predvolené nastavenie je aktuálny rok.

- Vyberte krajinu, v ktorej sa majú zobraziť súvisiace sviatky.

- (Predvolené: **Pondelok**) Vyberte prvý deň v týždni pre správu.

- Vyberte zobrazené priezvisko vydatej ženy.

  - **Manželky používajú svoje vlastné priezvisko** (Predvolené)
  - Manželky používajú manželovo priezvisko (z prvej uvedenej rodiny)
  - Manželky používajú manželovo priezvisko (z poslednej uvedenej rodiny)

-  : zaradiť alebo nezaradiť narodeniny do kalendára (predvolene začiarknuté políčko)

-  : zahrnúť alebo nezahrnúť výročia do kalendára (štandardne začiarknuté políčko)

{{-}}

### <u>Strom potomkov</u>

![[_media/GraphicalReports-DescendantTree-example-portrait-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Strom potomkov - grafické zostavy - prehľad výstupných príkladov]]

Táto zostava generuje graf osôb, ktoré sú potomkami východiskovej osoby. Prípadne môže vygenerovať graf potomkov rodičov východiskovej osoby.

Report Strom potomkov môžete vybrať pomocou }. {{-}} Pozri tiež [spoločné možnosti](wiki:Gramps_6.0_Wiki_Manuál_-_Reporty_-_časť_4#Spoločné_možnosti) {{-}}

#### Možnosti stromu

![[_media/DescendantTree-GraphicalReports-TreeOptions-tab-52.png|vpravo\|thumb\|450px\|Fig. {{#var:chapter}}.{{#vardefineecho:figure\|{{#expr:{{#var:figure}}+1}}}} Strom potomkov - Grafické zostavy - Možnosti stromu - predvolené možnosti karty]] } vyberie východiskovú osobu pre správu. V predvolenom nastavení je to aktuálna aktívna osoba.

(<kód>10</kód> predvolené ). Počet generácií, ktoré sa majú zobraziť na grafe (vrátane domovskej osoby). Ak je vybratá možnosť , graf bude obsahovať o jednu generáciu viac. (Príklad 1 bol spustený s =3, príklad 2 s =2.)

určuje, ako hlboko sa majú manželia zobraziť.

vykreslí graf potomstva od rodičov východiskovej osoby, ak sa nachádzajú v databáze. Príklad [Example](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_4#Examples) je založený na rovnakej rodine ako prvý príklad a ukazuje výsledok začatia s "Dieťaťom 2 Davies" a zaškrtnutím tohto políčka.

{{-}} Príklad 1 bol získaný výberom Allana Daviesa ako východiskovej osoby a následným spustením správy bez zaškrtnutia tohto políčka, pričom všetky ostatné možnosti boli rovnaké okrem . Rozdiely medzi týmito dvoma príkladmi sú:

- Formát prvej generácie je zmenený. Keďže rodičia východiskovej osoby musia byť vedľa seba, manželia v prvej generácii môžu byť zobrazení mimo poradia.
- Na účely nastavenia sa obaja rodičia považujú za priamych potomkov, a nie za manželov. (Hoci matka používa na karte Zobrazenie).

To znamená, že ostatní manželia (ak existujú) oboch budú zobrazení do počtu úrovní, ktoré určuje . V príklade 2 je Mike Morris zobrazený napriek tomu, že je nastavená na 1.

- Názov správy (ak je vybraný na karte Zahrnúť) sa zmení tak, aby zahŕňal oboch rodičov východiskovej osoby. V názve sa zobrazia len dve osoby. V príklade 2 nie je Mike Morris uvedený v názve, hoci jeho potomkovia sú zobrazení.

V prípade príkladu:

- Abe je priamy potomok
  - Abe sa oženil/oženil s Barbrou a mal dve deti
  - Abe sa tiež oženil s Bridget a mal jedno dieťa
    - Bridget sa vydala za Carla.
      - Carl a Denise mali dieťa.

Vzhľadom na vyššie uvedený príklad sa toto zobrazí pre prvé tri možnosti .

- 0 znamená, že sa zobrazia len priami potomkovia. Na karte Sekundárne sa nezobrazí nič (informácie o manželoch alebo informácie o manželstve). V uvedenom príklade sa zobrazí iba Abe s tromi deťmi priamo pod ním
- 1 znamená, že sa zobrazia len manželia priamych potomkov. Pre uvedený príklad sa Abe zobrazí s dvoma informáciami o manželstve. Pod prvým budú dve deti a pod druhým jedno dieťa.
- 2 znamená, že sa zobrazia manželia manželských partnerov. To isté ako v prípade 1, ale u Bridget sa zobrazí aj jej druhé manželstvo. Ak mali nejaké deti, budú tiež zobrazené.
- 3 znamená, že sa zobrazia všetci z uvedeného príkladu.

Akákoľvek možnosť nad 1 je v správe veľmi ťažko čitateľná bez možnosti na karte Zobrazenie.

A v neposlednom rade je tu možnosť , ktorá sa snaží posunúť všetkých nahor tak, ako sa len dá (stlačiť) a stále mať čitateľnú správu. Ak je začiarknutá možnosť , nemá na prvú generáciu žiadny vplyv. {{-}}

#### Možnosti správy

![[_media/DescendantTree-GraphicalReports-ReportOptions-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Strom potomkov - Grafické zostavy - Možnosti zostavy - predvolené možnosti karty]]

umožňuje vybrať názov správy. Na výber sú tieto možnosti:

- *Neuvádzať názov*

- *Graf potomkov pre \[vybrané osoby\]*

- 

- 

Ak je na karte "Možnosti stromu" začiarknuté políčko "Začať od rodičov vybranej osoby", zobrazia sa obaja rodičia vybranej osoby. V záhlaví budú uvedené iba dve osoby. Ak je "úroveň manželov" dvaja alebo viac, potomkovia "manželov manželov" sú zahrnutí do tabuľky, ale nie sú uvedení v názve.

Funkcia Scale tree to fit (Zmenšiť strom podľa potreby) zväčší alebo zmenší strom tak, aby sa zmestil na stránku podľa potreby. Možnosti sú:

- *Neškálovať strom (predvolené nastavenie)*

- *Zmenšiť strom tak, aby sa prispôsobil iba šírke stránky*

- *Zmenšiť strom tak, aby sa prispôsobil veľkosti stránky*

- : Zmeniť veľkosť stránky podľa stromu (predvolene nezačiarknuté) zväčší alebo zmenší stránku tak, aby sa prispôsobila stromu. Ak je začiarknutá voľba "Zmenšiť strom tak, aby sa prispôsobil", možnosti sa uskutočnia v tomto poradí; najprv sa zmenší strom, potom stránka. Pri každej možnosti existuje kombinovaný účinok:

  - Pri voľbe "Neškálovať strom" sa šírka aj výška stránky zmení tak, aby sa prispôsobila stromu.
  - Pri voľbe "Škálovať strom len na šírku stránky" sa výška stránky prispôsobí výške stromu.
  - Pri voľbe "Scale tree to fit the size of the page" (Zmenšiť strom tak, aby sa prispôsobil veľkosti stránky) sa veľkosť stránky zmení tak, aby sa odstránila medzera vo výške aj šírke.

Tieto dve možnosti sú lepšie popísané v [spoločné možnosti](wiki:Gramps_6.0_Wiki_Manuál_-_Reporty_-_časť_4#Spoločné_možnosti) s tipmi na vytvorenie krajších reportov. Táto karta obsahuje aj začiarkávacie políčka , a .

{{-}}

#### Možnosti správy (2)

![[_media/DescendantTree-GraphicalReports-ReportOptions2-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Strom potomkov - Grafické zostavy - Možnosti zostavy (2) - predvolené možnosti karty]]

- Vyberte formát zobrazenia názvov. Vyberte si z nasledujúcich možností

  - **Priezvisko, prípona** (predvolené)

  - Dané priezvisko s príponou

  - Dané priezvisko

  - Hlavné priezviská, daná patronymická prípona

  - Priezvisko, dané (bežné)

  -  (predvolene začiarknuté políčko)

-   
  Vyberte, či chcete do správy zahrnúť alebo nezahrnúť žijúce osoby. Vyberte si z nasledujúcich možností

  - **Zahrnúť a všetky údaje** (predvolené)
  - Úplné mená, ale odstránené údaje
  - Nahradené mená a odstránené údaje
  - Úplné mená nahradené a údaje odstránené
  - Nezahŕňa sa

-   
  Vyberte počet rokov od úmrtia, za ktoré sa majú osoby v správe považovať. Umožňuje zahrnúť alebo vylúčiť nedávno zosnulé osoby do správy. Predvolená hodnota je 0 rokov.

-   
  Preklad, ktorý sa má použiť pre správu.

  - Výber jazyka

-   
  Vyberte formát zobrazenia dátumov. Vyberte si z možností **RRRR-MM-DD (ISO)(2018-04-08)**(predvolené) / Číselné (8. 4. 2018) / Mesiac Deň, Rok (8. 4. 2018) / Po Deň, Rok (8. 4. 2018)/ Deň Mesiac Rok (8. 4. 2018)/ Deň Po Rok (8. 4. 2018)

{{-}}

#### Zobrazenie

![[_media/DescendantTree-GraphicalReports-Display-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Strom potomkov - grafické zostavy - zobrazenie - predvolené možnosti karty]]

nastavuje zobrazenie pre všetkých potomkov v strome. Predvolené nastavenie je:

    $n
    b. $b
    {d. $d}

ktorý zobrazí meno, dátum narodenia a dátum úmrtia na po sebe idúcich riadkoch vo formátoch nastavených na karte Zobrazenie v predvoľbách programu Gramps. Písmeno {} na treťom riadku uvádza, že text "d. ' sa zobrazí LEN vtedy, keď \$d má hodnotu, t. j. v poli dátumu úmrtia v databáze je niečo pre túto osobu. Viac informácií nájdete v časti [Substitučné hodnoty](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_2/sk), kde sa dozviete, ako zahrnúť miesta a atribúty a vybrať rôzne formáty pre mená a dátumy a miesta.

Začiarkávacie políčko spôsobí, že mená a ďalšie informácie o priamych potomkoch budú uvedené tučným písmom zvoleným v editore štýlu.

určuje, čo sa zobrazí pre každého z manželov. Predvolené nastavenie je rovnaké ako pre potomkov. Ak si neželáte mať samostatné pole pre informácie o manželstve, môžu byť zobrazené v poli pre manželov, napríklad pridaním riadku s

    m. $m 

Ktorý zobrazuje dátum uzavretia manželstva.

odsadí políčka manželov a manželstiev od políčok potomkov. V tabuľke potomkov rodiny to nemá vplyv na východiskovú rodinu ani na rodičov východiskovej rodiny, ale má to vplyv na všetkých ostatných manželov týchto troch párov.

zobrazí v strome samostatné políčko pre každé manželstvo. Formát zobrazenia je nastavený v položke . Predvolené nastavenie je

    m. $m

ktorý zobrazuje dátum sobáša. Ak toto políčko nie je začiarknuté, informácie o manželstve sa nezobrazia, pokiaľ ich nezadáte vo formáte zobrazenia manželov, ako je opísané vyššie.

{{-}}

#### Rozšírené

![[_media/DescendantTree-GraphicalReports-Advanced-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Strom potomkov - grafické zostavy - rozšírené - predvolené možnosti karty]]

Dvojice reťazcov oddelených lomítkom '/' určujú, čo chcete nahradiť a čím to chcete nahradiť.

Príklad:

    Spojené štáty americké/USA
    Spojené kráľovstvo Veľkej Británie a Severného Írska/UK
    Llanfair&shy;pwllgwyn&shy;gyllgo&shy;gerychwyrn&shy;drobwll&shy;llanty&shy;silio&shy;gogogoch/Llanfairpwll

Šírka každého stĺpca je definovaná najširším políčkom v správe. Ak sa teda stane, že jedno políčko bude oveľa širšie ako ostatné, veľa miesta sa premárni. Možnosť nahradiť reťazec umožňuje odstrániť alebo skrátiť časti reťazca, ktoré nie sú potrebné alebo ktoré možno skrátiť, takže množstvo zbytočne využitého priestoru je minimálne.

Na tejto karte môžete tiež v jednom z rohov správy.

Napríklad pridaním premennej "\$T" do poľa s poznámkou sa zobrazí deň vytvorenia výkazu. Použije sa bežné formátovanie dátumu (pozri [Zástupné hodnoty](wiki:Gramps_6.0_Wiki_Manuál_-_Reporty_-_časť_2#Zástupné_hodnoty)).

{{-}}

#### Príklady

![[_media/Descendant_tree_example1.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Správa o stromoch potomkov, príklad 1. Allan Davies mal troch manželov]].

![[_media/Descendant_tree_example2.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Správa o stromoch potomkov, príklad 2.]]

{{-}} vyberie východiskovú osobu pre prehľad. V predvolenom nastavení je to aktuálna aktívna osoba.

vykreslí graf potomstva od rodičov východiskovej osoby, ak sa nachádzajú v databáze. Nasledujúci príklad je založený na rovnakej rodine ako prvý príklad a ukazuje výsledok začatia s "Dieťaťom 2 Davies" a zaškrtnutím tohto políčka.

{{-}} Príklad 1 bol získaný výberom Allana Daviesa ako východiskovej osoby a následným spustením správy bez začiarknutia tohto políčka, pričom všetky ostatné možnosti boli rovnaké okrem . Rozdiely medzi týmito dvoma príkladmi sú:

- Formát prvej generácie je zmenený. Keďže rodičia východiskovej osoby musia byť vedľa seba, manželia v prvej generácii môžu byť zobrazení mimo poradia.
- Na účely nastavenia sa obaja rodičia považujú za priamych potomkov, a nie za manželov. (Hoci matka používa na karte Zobrazenie).

To znamená, že ostatní manželia (ak existujú) oboch budú zobrazení do počtu úrovní, ktoré určuje . V príklade 2 je Mike Morris zobrazený napriek tomu, že je nastavená na 1.

- Názov správy (ak je vybraný na karte Zahrnúť) sa zmení tak, aby zahŕňal oboch rodičov východiskovej osoby. V názve sa zobrazia len dve osoby. V príklade 2 nie je Mike Morris uvedený v názve, hoci jeho potomkovia sú zobrazení.

Počet generácií, ktoré sa majú zobraziť v správe (vrátane východiskovej osoby). Ak je vybratá možnosť , graf bude obsahovať o jednu generáciu viac. (Príklad 1 bol spustený s =3, príklad 2 s =2.)

určuje, ako hlboko sa majú manželia zobraziť.

V prípade príkladu:

- Abe je priamy potomok
  - Abe sa oženil/oženil s Barbrou a mal dve deti
  - Abe sa oženil aj s Bridget a mal jedno dieťa
    - Bridget má/bola vydatá za Carla.
      - Carl a Denise mali dieťa.

Vzhľadom na uvedený príklad sa zobrazí toto pre prvé tri možnosti .

- 0 znamená, že sa zobrazia len priami potomkovia. Na karte Sekundárni sa nezobrazí nič (informácie o manželoch alebo informácie o manželstve). V uvedenom príklade sa zobrazí iba Abe s tromi deťmi priamo pod ním
- 1 znamená, že sa zobrazia len manželia priamych potomkov. Pre uvedený príklad sa Abe zobrazí s dvoma informáciami o manželstve. Pod prvým budú dve deti a pod druhým jedno dieťa.
- 2 znamená, že sa zobrazia manželia manželských partnerov. To isté ako v prípade 1, ale u Bridget sa zobrazí aj jej druhé manželstvo. Ak mali nejaké deti, budú tiež zobrazené.
- 3 znamená, že sa zobrazia všetci z uvedeného príkladu.

Akákoľvek možnosť nad 1 je v správe veľmi ťažko čitateľná bez možnosti na karte Zobrazenie.

A v neposlednom rade je tu možnosť , ktorá sa snaží posunúť všetkých nahor tak, ako sa len dá (stlačiť) a stále mať čitateľnú správu. Ak je začiarknutá možnosť , nemá na prvú generáciu žiadny vplyv. {{-}}

### <u>Strom potomkov rodiny</u>

![[_media/GraphicalReports-FamilyDescendantTree-example-portrait-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Rodokmeň - grafické prehľady - prehľad výstupných príkladov]]

Táto zostava generuje graf osôb, ktoré sú potomkami aktívnej rodiny.

Hlásenie Strom potomkov rodiny môžete vybrať pomocou }. {{-}} Pozri tiež [spoločné možnosti](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_4/sk#Spoločné_možnosti) {{-}}

#### Možnosti stromu

![[_media/FamilyDescendantTree-GraphicalReports-TreeOptions-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Rodokmeň - Grafické zostavy - Možnosti stromu - predvolené možnosti záložky]]

Tlačidlo vyberie východiskovú rodinu (Otec a Matka) pre túto správu. V predvolenom nastavení je to aktuálne aktívna rodina.

(<kód>10</kód> predvolené ). Počet generácií, ktoré sa majú zobraziť na grafe (vrátane východiskovej osoby). Ak je vybratá možnosť , graf bude obsahovať o jednu generáciu viac. (Príklad 1 bol spustený s =3, príklad 2 s =2.)

určuje, ako hlboko sa majú manželia zobraziť.

Ak je toto políčko začiarknuté, v správe sa zobrazia obaja rodičia začínajúceho otca a matky (ak sú v databáze), a všetkých potomkov oboch rodičovských skupín pre zvolený počet generácií. Celkový počet generácií v grafe je preto o 1 väčší ako počet vybraný v políčku generácií. (Uvedený príklad grafu bol vytvorený s počtom generácií = 2.)

Východiskový otec a matka musia byť v strede grafu. Nebudú preto zobrazení v poradí narodenia spolu so svojimi súrodencami - namiesto toho budú zobrazení ako posledný a prvý dieťa svojich rodičov. Toto je znázornené v tabuľke [Príklady](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_4/sk#Príklady), kde sú deti v oboch rodinách boli pomenované dieťa 1,2,3 v poradí ich narodenia. Okrem toho, ak majú začínajúci otec alebo matka ďalších manželov, budú zobrazení dvakrát. To platí aj pre rodičov východiskového otca alebo matky.

Ak toto políčko nie je začiarknuté, správa je rovnaká ako správa o stromoch potomkov, s výnimkou toho, že počet generácií je zvýšený o jednu, formát prvej generácie je iný, a získate ďalšie možnosti pre názov grafu.

{{-}}

#### Možnosti správy

![[_media/FamilyDescendantTree-GraphicalReports-ReportOptions-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Rodokmeň - Grafické zostavy - Možnosti zostavy - predvolené možnosti karty]] umožňuje vybrať názov správy. Na výber sú tieto možnosti:

- *Neuvádzať názov*
- *Graf potomkov pre \[vybrané osoby\]*

Ak je na karte "Možnosti stromu" začiarknuté políčko "Začať od rodičov vybranej osoby", zobrazia sa obaja rodičia vybranej osoby. V názve budú uvedené len dve osoby. Ak je "úroveň manželov" dvaja alebo viac, potomkovia "manželov manželov" sú zahrnutí do grafu, ale nie sú uvedení v názve.

Funkcia Scale tree to fit (Zmenšiť strom podľa potreby) zväčší alebo zmenší strom tak, aby sa zmestil na stránku podľa potreby. Možnosti sú:

- *Neškálovať strom (predvolené nastavenie)*

- *Zmenšiť strom tak, aby sa prispôsobil iba šírke stránky*

- *Zmenšiť strom tak, aby sa prispôsobil veľkosti stránky*

- : Zmeniť veľkosť stránky podľa stromu (predvolene nezačiarknuté) zväčší alebo zmenší stránku tak, aby sa prispôsobila stromu. Ak je začiarknutá voľba "Zmenšiť strom tak, aby sa prispôsobil", možnosti sa uskutočnia v tomto poradí; najprv sa zmenší strom, potom stránka. Pri každej možnosti existuje kombinovaný účinok:

  - Pri voľbe "Neškálovať strom" sa šírka aj výška stránky zmení tak, aby sa prispôsobila stromu.
  - Pri voľbe "Škálovať strom len na šírku stránky" sa výška stránky prispôsobí výške stromu.
  - Pri voľbe "Scale tree to fit the size of the page" (Zmenšiť strom tak, aby sa prispôsobil veľkosti stránky) sa veľkosť stránky zmení tak, aby sa odstránila medzera vo výške aj šírke.

Tieto dve možnosti sú lepšie popísané v [spoločné možnosti](wiki:Gramps_6.0_Wiki_Manuál_-_Reporty_-_časť_4#Spoločné_možnosti) s tipmi na vytvorenie krajších reportov. Táto karta obsahuje aj začiarkávacie políčka , a .

{{-}}

#### Možnosti správy (2)

![[_media/FamilyDescendantTree-GraphicalReports-ReportOptions2-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Rodokmeň - Grafické zostavy - Možnosti zostavy (2) - predvolené možnosti karty]]

- Vyberte formát zobrazenia mien. Vyberte si z nasledujúcich možností

  - **Priezvisko, prípona** (predvolené)

  - Dané priezvisko s príponou

  - Dané priezvisko

  - Hlavné priezviská, daná patronymická prípona

  - Priezvisko, dané (bežné)

  -  (predvolene začiarknuté políčko)

-   
  Vyberte, či chcete do správy zahrnúť alebo nezahrnúť žijúce osoby. Vyberte si z nasledujúcich možností

  - **Zahrnúť a všetky údaje** (predvolené)
  - Úplné mená, ale odstránené údaje
  - Nahradené mená a odstránené údaje
  - Úplné mená nahradené a údaje odstránené
  - Nezahŕňa sa

-   
  Vyberte počet rokov od úmrtia, za ktoré sa majú osoby v správe považovať. Umožňuje zahrnúť alebo vylúčiť nedávno zosnulé osoby do správy. Predvolená hodnota je 0 rokov.

-   
  Preklad, ktorý sa má použiť pre správu.

  - Výber jazyka

-   
  Vyberte formát zobrazenia dátumov. Vyberte si z možností **RRRR-MM-DD (ISO)(2018-04-08)**(predvolené) / Číselné (8. 4. 2018) / Mesiac Deň, Rok (8. 4. 2018) / Po Deň, Rok (8. 4. 2018)/ Deň Mesiac Rok (8. 4. 2018)/ Deň Po Rok (8. 4. 2018)

{{-}}

#### Zobraziť

![[_media/FamilyDescendantTree-GraphicalReports-Display-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Rodokmeň - Grafické zostavy - Zobrazenie - predvolené možnosti karty]]

nastavuje zobrazenie pre všetkých potomkov v strome. Predvolené nastavenie je:

    $n
    b. $b
    {d. $d}

ktorý zobrazí meno, dátum narodenia a dátum úmrtia na po sebe idúcich riadkoch vo formátoch nastavených na karte Zobrazenie v predvoľbách programu Gramps. Písmeno {} na treťom riadku uvádza, že text "d. ' sa zobrazí LEN vtedy, keď \$d má hodnotu, t. j. v poli dátumu úmrtia v databáze je niečo pre túto osobu. Viac informácií nájdete v časti [Substitučné hodnoty](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_2), kde sa dozviete, ako zahrnúť miesta a atribúty a vybrať rôzne formáty pre mená a dátumy a miesta.

určuje, čo sa zobrazí pre každého z manželov. Predvolené nastavenie je rovnaké ako pre potomkov. Ak si neželáte mať samostatné pole pre informácie o manželstve, môžu sa zobraziť v poli pre manželov, napríklad pridaním riadku s

    m. $m 

Ktorý zobrazuje dátum uzavretia manželstva.

odsadí políčka manželov a manželstiev od políčok potomkov. V tabuľke potomkov rodiny to nemá vplyv na východiskovú rodinu ani na rodičov východiskovej rodiny, ale má to vplyv na všetkých ostatných manželov týchto troch párov.

zobrazí v strome samostatné políčko pre každé manželstvo. Formát zobrazenia je nastavený v položke . Predvolené nastavenie je

    m. $m

ktorý zobrazuje dátum sobáša. Ak toto políčko nie je začiarknuté, informácie o manželstve sa nezobrazia, pokiaľ ich nezadáte vo formáte zobrazenia manželov, ako je opísané vyššie.

{{-}}

#### Rozšírené

![[_media/FamilyDescendantTree-GraphicalReports-Advanced-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Rodokmeň - Grafické zostavy - Rozšírené - predvolené možnosti karty]]

- }: To vám umožňuje vložiť dvojice reťazcov oddelených znakom '/', ktoré určujú text, ktorý chcete nahradiť iným textom. Napríklad

      Spojené štáty americké/USA

  nahradí Spojené štáty americké textom USA.

  -  Môžete zaškrtnúť políčko Zahrnúť poznámku, ak chcete pridať poznámku (políčko je predvolene nezaškrtnuté). určuje text, ktorý bude poznámka obsahovať.

-   
  Určte, kde na stránke sa má poznámka umiestniť (predvolene je vľavo dole).

-   
  Zväčší alebo zmenší medzipriestor (predvolená hodnota je 1,00 palca).

-   
  Zväčšite alebo zmenšite tieň boxu (predvolená hodnota je 1,00 palca).

Tieto dve možnosti sú lepšie popísané v [spoločné možnosti](wiki:Gramps_6.0_Wiki_Manuál_-_Reporty_-_časť_4#Spoločné_možnosti) s tipmi na vytvorenie krajších reportov.

{{-}}

### <u>Fan Chart</u>

![[_media/GraphicalReports-FanChart-example-landscape-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Ventilátorový diagram - grafické zostavy - prehľad výstupov príkladov]]

Táto zostava vytvára graf pripomínajúci vejár, pričom Aktívna osoba je v strede, rodičia v polkruhu vedľa nej, starí rodičia v ďalšom polkruhu a tak ďalej, celkovo päť generácií.

Hlásenie Vejárový graf môžete vybrať pomocou {{-}} Pozrite si tiež [spoločné možnosti](wiki:Gramps_6.0_Wiki_Manuál_-_Reporty_-_časť_4#Spoločné_možnosti). {{-}}

#### Možnosti správy

![[_media/FanChart-GraphicalReports-ReportOptions-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Ventilátorový diagram - Grafické zostavy - Možnosti zostavy - predvolené možnosti záložky]]

- Stredová osoba pre report.

}

- (`5` predvolené ) Počet generácií, ktoré sa majú zahrnúť do správy.

- Forma grafu.

  - Úplný kruh
  - **polkruh** (predvolené nastavenie)
  - štvrťkruh

- Farba pozadia je buď biela, alebo **závislá od generácie** (predvolené).

- Vytlačiť radiálny text **vzpriamene** (predvolené) alebo dookola.

- { : Kresliť pozadie, aj keď nie sú žiadne informácie (začiarkávacie políčko je predvolene začiarknuté).

-  : V editore štýlov môžete prispôsobiť písmo a farbu pre každú generáciu (predvolene začiarknuté políčko)

{{-}}

#### Možnosti správy (2)

![[_media/FanChart-GraphicalReports-ReportOptions2-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Ventilátorový diagram - Grafické zostavy - Možnosti zostavy (2) - predvolené možnosti karty]]

-  (štandardne začiarknuté políčko)

-   
  Vyberte, či chcete do správy zahrnúť alebo nezahrnúť žijúce osoby. Vyberte si z nasledujúcich možností

  - **Zahrnúť a všetky údaje** (predvolené)
  - Úplné mená, ale odstránené údaje
  - Nahradené mená a odstránené údaje
  - Úplné mená nahradené a údaje odstránené
  - Nezahŕňa sa

-   
  Vyberte počet rokov od úmrtia, za ktoré sa majú osoby v správe považovať. Umožňuje zahrnúť alebo vylúčiť nedávno zosnulé osoby do správy. Predvolená hodnota je 0 rokov.

-   
  Preklad, ktorý sa má použiť pre správu.

  - Výber jazyka

{{-}}

### <u>Štatistické grafy</u>

Táto zostava zobrazuje štatistické údaje o vašom rodokmeni.

<div>

- ![[_media/GraphicalReports-StatisticsCharts-Chart1-example-portrait-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Graf 1 (mesiac narodenia)]]

- ![[_media/GraphicalReports-StatisticsCharts-Chart3-Gender-example-portrait-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Graf 2 (Pohlavie)]]

- ![[_media/GraphicalReports-StatisticsCharts-Chart3-example-portrait-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Graf 3 (Počet detí) -]]

</div>

Správu Štatistické grafy môžete zvoliť pomocou }.

Konkrétne možnosti zahŕňajú filter, metódy triedenia a dodatočné obmedzenie na základe narodenia a pohlavia pre zahrnutie do štatistiky. Môžete tiež nastaviť minimálny počet položiek, ktoré majú byť zaradené do stĺpcového grafu, takže grafy s menším počtom položiek budú namiesto toho generovať koláčový graf. V tabuľkách , a }tabuľky vám umožňujú vybrať, ktoré dodatočné informácie sa majú zahrnúť do každého jednotlivého grafu vo vašej správe. {{-}} Pozrite si tiež [Obecné možnosti](wiki:Gramps_6.0_Wiki_Manuál_-_Reporty_-_časť_4#Obecné_možnosti) {{-}}

#### Možnosti správy

![[_media/StatisticsCharts-GraphicalReports-ReportOptions-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Štatistické grafy - Grafické zostavy - Možnosti zostavy - predvolené možnosti karty]]

- vybrať medzi

  - **Celá databáza** (predvolené nastavenie)
  - Potomkovia aktívnej osoby
  - Rodiny potomkov aktívnej osoby
  - Predkovia aktívnej osoby
  - Ľudia so spoločným predkom s aktívnou osobou

- Centrálna osoba pre správu.

- Vyberte spôsob triedenia štatistických údajov:

  - **Počet položiek** (predvolené)
  - Názov položky

-  (predvolene nezačiarknuté políčko)

- } (`1700` predvolené) Rok narodenia, od ktorého sa majú zahrnúť ľudia: vyplňte rok, od ktorého sa má začať

- (`Aktuálny rok` predvolené) Rok narodenia, do ktorého sa majú zahrnúť ľudia: vyplňte rok

-  (predvolene nezačiarknuté políčko)

- Vyberte, ktoré pohlavia sa zahrnú do štatistiky.

  - **Obe**' (predvolené)
  - Muži
  - Ženy

- (`8` predvolené) Pri menšom počte položiek sa namiesto stĺpcového grafu použije koláčový graf a legenda.

{{-}}

#### Možnosti správy (2)

![[_media/StatisticsCharts-GraphicalReports-ReportOptions2-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Štatistické grafy - Grafické zostavy - Možnosti zostavy (2) - predvolené možnosti karty]]

- Vyberte formát zobrazenia názvov. Vyberte si z nasledujúcich možností

  - **Priezvisko, prípona** (predvolené)

  - Dané priezvisko s príponou

  - Dané priezvisko

  - Hlavné priezviská, daná patronymická prípona

  - Priezvisko, dané (bežné)

  -  (predvolene začiarknuté políčko)

-   
  Vyberte, či chcete do správy zahrnúť alebo nezahrnúť žijúce osoby. Vyberte si z nasledujúcich možností

  - **Zahrnúť a všetky údaje** (predvolené)
  - Úplné mená, ale odstránené údaje
  - Nahradené mená a odstránené údaje
  - Úplné mená nahradené a údaje odstránené
  - Nezahŕňa sa

-   
  Vyberte počet rokov od úmrtia, za ktoré sa majú osoby v správe považovať. Umožňuje zahrnúť alebo vylúčiť nedávno zosnulé osoby do správy. Predvolená hodnota je 0 rokov.

-   
  Preklad, ktorý sa má použiť pre správu.

  - Výber jazyka

{{-}}

#### Charts 1

![[_media/StatisticsCharts-GraphicalReports-Charts1-tab-52.png|Obrázok {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Štatistické grafy - Grafické zostavy - Grafy 1 - predvolené možnosti karty]]

Zobrazuje štatistiky **Mesiac narodenia** v predvolenom nastavení a môžete do grafu zahrnúť ktorýkoľvek z nasledujúcich uvedených údajov:

-  (predvolene nezaškrtnuté políčko)

-  (políčko je predvolene nezačiarknuté)

-  (políčko je štandardne nezačiarknuté)

-  (políčko je štandardne nezačiarknuté)

-  (políčko je štandardne nezačiarknuté)

-  (políčko je štandardne začiarknuté)

{{-}}

#### Charts 2

![[_media/StatisticsCharts-GraphicalReports-Charts2-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Štatistické grafy - Grafické zostavy - Grafy 2 - predvolené možnosti karty]]

Zobrazuje štatistiku **Počet detí** v predvolenom nastavení a môžete do grafu zahrnúť ktorýkoľvek z nasledujúcich uvedených údajov:

-  (predvolene nezačiarknuté políčko)

-  (políčko je predvolene nezačiarknuté)

-  (políčko je štandardne nezačiarknuté)

-  (políčko je štandardne nezačiarknuté)

-  (políčko je štandardne nezačiarknuté)

-  (políčko je štandardne nezačiarknuté)

{{-}}

#### Charts 3

![[_media/StatisticsCharts-GraphicalReports-Charts3-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Štatistické grafy - Grafické zostavy - Grafy 3 - predvolené možnosti záložky]]

Zobrazuje štatistiky **Pohlavia** v predvolenom nastavení a môžete do grafu zahrnúť ktorýkoľvek z nasledujúcich uvedených údajov:

-  (predvolene nezačiarknuté políčko)

-  (políčko je predvolene začiarknuté)

-  (políčko je predvolene nezačiarknuté)

-  (políčko je štandardne začiarknuté)

-  (políčko je štandardne nezačiarknuté)

-  (políčko je štandardne nezačiarknuté)

-  (políčko je štandardne nezačiarknuté)

{{-}}

### <u>Časový graf</u>

![[_media/GraphicalReports-TimelineChart-example-landscape-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Časový graf - grafické zostavy - prehľad výstupov príkladov]]

Táto zostava vypisuje zoznam osôb s ich životmi reprezentovanými intervalmi na spoločnej chronologickej stupnici.

Hlásenie Časový graf môžete vybrať pomocou }. {{-}} Pozri tiež [spoločné možnosti](wiki:Gramps_6.0_Wiki_Manuál_-_Reporty_-_časť_4#Spoločné_možnosti) {{-}}

#### Možnosti zostáv

![[_media/TimelineChart-GraphicalReports-ReportOptions-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Časový graf - Grafické zostavy - Možnosti zostavy - predvolené možnosti karty]]

- vybrať medzi

  - **Celá databáza** (predvolené nastavenie)
  - Potomkovia aktívnej osoby
  - Rodiny potomkov aktívnej osoby
  - Predkovia aktívnej osoby
  - Ľudia so spoločným predkom s aktívnou osobou

- Centrálna osoba pre správu.

- Metóda triedenia, ktorá sa má použiť.

  - **Dátum narodenia** (predvolené)
  - Meno

{{-}}

#### Možnosti zostavy (2)

![[_media/TimelineChart-GraphicalReports-ReportOptions2-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Časový graf - Grafické zostavy - Možnosti zostavy (2) - predvolené možnosti karty]]

- } Vyberte formát zobrazenia názvov. Vyberte si z nasledujúcich možností

  - **Priezvisko, prípona** (predvolené)

  - Dané priezvisko s príponou

  - Dané priezvisko

  - Hlavné priezviská, daná patronymická prípona

  - Priezvisko, dané (bežné)

  -  (predvolene začiarknuté políčko)

-   
  Vyberte, či chcete do správy zahrnúť alebo nezahrnúť žijúce osoby. Vyberte si z nasledujúcich možností

  - **Zahrnúť a všetky údaje** (predvolené)
  - Úplné mená, ale odstránené údaje
  - Nahradené mená a odstránené údaje
  - Úplné mená nahradené a údaje odstránené
  - Nezahŕňa sa

-   
  Vyberte počet rokov od úmrtia, za ktoré sa majú osoby v správe považovať. Umožňuje zahrnúť alebo vylúčiť nedávno zosnulé osoby do správy. Predvolená hodnota je 0 rokov.

- } Preklad, ktorý sa má použiť pre správu.

  - Výber jazyka

{{-}}

<hr>

Späť na [Register správ](wiki:Gramps_6.0_Wiki_Manual_-_Reports/sk). {{-}}

[Category:Sk:Documentation](wiki:Category:Sk:Documentation) [Category:Plugins](wiki:Category:Plugins)
