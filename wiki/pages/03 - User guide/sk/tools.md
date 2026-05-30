---
title: Gramps 6.0 Wiki Manual - Tools/sk
categories:
- Plugins
- Sk:Documentation
- Stub
- Tools
managed: false
source: wiki-scrape
wiki_revid: 128204
wiki_fetched_at: '2026-05-30T20:24:41Z'
lang: sk
---

{{#vardefine:chapter\|14}} {{#vardefine:figure\|0}} ![[_media/MenuOverview-Tools-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;&quot; Panel ponuky - Prehľad nástrojov]] Táto kapitola opisuje rôzne dostupné v programe Gramps.

Gramps vám umožňuje vykonávať rôzne typy analýz vašich genealogických údajov. Nástroje zvyčajne nevytvárajú výstup vo forme výtlačkov alebo súborov. Namiesto toho vytvárajú výstup na obrazovke, ktorý je okamžite k dispozícii bádateľovi. V prípade potreby však môžete výsledky spustenia nástroja uložiť do súboru.

# Nástroje

![[_media/ToolbarIcon-OpenTheToolsDialog-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Ikona panela nástrojov pre "Otvoriť dialógové okno nástrojov"]]

K nástrojom sa dostanete výberom ponuky .

Prípadne si môžete prezrieť kompletný výber dostupných nástrojov spolu s ich stručným popisom v dialógovom okne , ktoré vyvoláte kliknutím na ikonu na paneli nástrojov z ktorejkoľvek kategórie. {{-}}

## Dialógové okno Výber nástrojov

![[_media/ToolSelection-dialog-example-with-debug-menu-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Výber nástroja - dialógové okno - príklad zobrazujúci informácie "Nájsť možné duplicitné osoby"]]

Dialógové okno umožňuje prechádzať kompletný výber dostupných nástrojov spolu s ich stručným popisom, keď ho vyvoláte kliknutím na ikonu na paneli nástrojov z ktorejkoľvek kategórie a pomocou šípok rozbalíte zoznamy. {{-}}

## Analýza a prieskum

Táto časť obsahuje nástroje, ktoré analyzujú a skúmajú databázu, ale nemenia ju. V súčasnosti sú v programe Gramps k dispozícii nasledujúce nástroje na analýzu a prieskum:

### <u>Porovnanie jednotlivých udalostí</u>

![vpravo\|thumb\|450px\|Obrázok {{#var:chapter}}.{{#vardefineecho:figure\|{{#expr:{{#var:figure}}+1}}}} "Porovnanie jednotlivých udalostí" - "Výber filtra na porovnanie udalostí" - dialógové okno](CompareIndividualEvents-EventComparisonFilterSelection-dialog-default-60.png "vpravo|thumb|450px|Obrázok {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Porovnanie jednotlivých udalostí" - "Výber filtra na porovnanie udalostí" - dialógové okno") Tento nástroj porovnáva udalosti vo vybranej skupine osôb.

Tento nástroj môžete použiť prostredníctvom ponuky }, ktorá otvorí dialógové okno .

Osoby pre toto porovnanie môžete vybrať z predtým vytvorených vlastných filtrov výberom z rozbaľovacieho zoznamu , ktorý je predvolene nastavený na *Celá databáza*. Alebo výberom tlačidla , čím vytvoríte vlastné filtre v editore . Ak chcete správu spustiť, vyberte a výsledky sa zobrazia v dialógovom okne .

{{-}} V dialógovom okne môžete zobraziť výsledky alebo výslednú tabuľku ako tabuľku (formát ODS). Výberom ukončíte správu. {{-}} ![[_media/CompareIndividualEvents-EventComparisonResults-dialog-expanded-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;Porovnanie jednotlivých udalostí&quot; - &quot;Výsledky porovnania udalostí&quot; - dialógové okno - rozšírený príklad]] {{-}}

## Spracovanie rodokmeňa

Táto časť obsahuje nástroje, ktoré môžu upravovať vašu databázu. Nástroje z tejto časti sa používajú najmä na vyhľadávanie a opravu chýb v údajoch. V súčasnosti sú v programe Gramps k dispozícii nasledujúce nástroje na spracovanie rodokmeňa:

{}}} Úpravy sa vykonajú len na základe vášho výslovného súhlasu, s výnimkou automatických opráv vykonávaných nástrojom .

### <u>Upraviť informácie o vlastníkovi databázy</u>

![[_media/DatabaseOwnerEditor-dialog-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Editor vlastníka databázy" - dialógové okno - zobrazenie kontextového menu]]

Tento nástroj upravuje všetky existujúce [Informácie o vyhľadávači](wiki:Gramps_6.0_Wiki_Manuál_-_Nastavenia#Vyhľadávač).

Vyberte ponuku . Zobrazí sa okno , v ktorom môžete vyplniť potrebné informácie.

- 

- 

- 

- 

- 

- 

- 

- 

- 

Tieto informácie sú špecifické pre rodokmeň a použijú sa pri exporte údajov vo formáte GEDCOM.

V kontextovej ponuke (pravé tlačidlo myši) sú k dispozícii dve možnosti:

- \-

- \-

{{-}}

### <u>Opis extraktu udalosti</u>

![[_media/ExtractEventDescription-ModificationsMade-window-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Extract Event Description's - Modifications Made - window - example result]]

Extrahuje popisy udalostí z údajov o udalostiach pomocou modelu :

`{typ udalosti} z {Prímeno}, {Dané meno}`

Ak popis udalosti chýba, nástroj použije tento model poľa popisu udalosti.

Prístup k tomuto nástroju je možný cez ponuku }

Zobrazí sa upozornenie **Zrušiť históriu** a môžete buď alebo .

Keď , tento nástroj prehľadá a upraví váš rodokmeň a zobrazí vám okno s výsledkom, v ktorom je uvedený celkový počet pridaných opisov udalostí. {{-}}

### <u>Výber informácií z mien</u>

Tento nástroj prehľadáva celú databázu a pokúša sa extrahovať tituly a prezývky, ktoré môžu byť vložené v poli osoby. Ak sa podarilo vyextrahovať nejaké informácie, v tabuľke sa zobrazia kandidáti na opravu. Potom sa môžete rozhodnúť, ktoré z nich opravíte podľa návrhu a ktoré nie.

Prístup k tomuto nástroju je možný cez ponuku

Zobrazí sa dialógové okno a môžete buď alebo .

![[_media/ExtractInformationFromNames-DefaultPrefixAndConnectorSettings-dialog-60.png|vpravo|thumb|450px|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Predvolené nastavenia prefixu a konektora" - dialógové okno pre nástroj "Extrahovanie informácií z názvov"]]

Zobrazí sa dialógové okno , v ktorom môžete upraviť jednotlivé možnosti podľa potreby:

- } `de, van, von, di, le, du, dela, della, des, vande, ten, da, af, den, das, dello, del, en, ein, elet, les, lo, los, un, um, una, uno, der, ter, te, die` (predvolené)

- `e, y` (predvolené)

- `de, van` (predvolené)

Po dokončení vyberte na spustenie nástroja. {{-}}

![[_media/ExtractInformationFromNames-NameAndTitleExtractionTool-dialog-example-60.png|Fig. {{#var:chapter}}.{{#var:figure}}.{{#var:figure}}+1}}}} "Nástroj na extrakciu názvov a názvov" - okno s výsledkami dialógového okna pre nástroj "Extrakcia informácií z názvov"]]

Po dokončení správy sa zobrazí okno výsledkov dialógu . {{-}}

### <u>Extrahovať údaje o mieste z názvu miesta</u>

### <u>Vyhľadanie možných duplicitných osôb</u>

![[_media/FindPossibleDuplicatePeople-dialog-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Nájsť možných duplicitných ľudí - dialógové okno - predvolené]]

Tento nástroj prehľadáva celú databázu a hľadá záznamy, ktoré môžu predstavovať tú istú osobu.

Prístup k tomuto nástroju je možný cez ponuku .

Zobrazí sa dialógové okno , v ktorom môžete nastaviť nasledujúce možnosti:

- : z rozbaľovacej ponuky vyberte medzi možnosťami **Nízka**' (predvolené nastavenie), Stredná a Vysoká. (Poznámka:Toto vypočíta šancu na zhodu ako číslo s pohyblivou rádovou čiarkou. Pre každú zhodnú informáciu sa šanca zvyšuje. Ak je šanca väčšia ako prahová hodnota, potom sa oznámi zhoda. Prahové hodnoty sú Nízka=0,25, Stredná=1,0 a Vysoká=2,0. Takže s prahovou hodnotou nastavenou na High (Vysoká) sa očakáva menej zhody).

-  na porovnanie možných duplicitných osôb. (štandardne začiarknuté políčko)

K dispozícii sú nasledujúce tlačidlá: Tlačidlo vás prenesie na túto stránku, tlačidlo na zastavenie spracovania a tlačidlo na začatie spracovania údajov.

Výberom tlačidla spustíte nástroj a údaje sa spracujú v dvoch priechodoch.

- Prechod 1: Vytvorenie predbežných zoznamov
- Posun 2: Výpočet potenciálnych zhody.

Zobrazí sa ukazovateľ priebehu a v závislosti od rýchlosti vášho počítača a počtu osôb v databáze to môže trvať určitý čas.

{{-}} ![[_media/FindPossibleDuplicatePeople-PotentialMerges-result-dialog-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Dialógové okno výsledkov &quot;Potenciálne zlúčenia&quot; pre &quot;Nájsť možné duplicitné osoby&quot; - dialóg - príklad]]

Po dokončení hlásenia sa zobrazí okno zoznamu výsledkov s nasledujúcimi zobrazenými stĺpcami:

- : poskytuje predstavu o podobnosti medzi dvoma osobami. Čím vyššie je hodnotenie, tým vyššia je pravdepodobnosť, že ide o duplicitné osoby.

- 

- 

Na vybraný riadok môžete buď dvakrát kliknúť, alebo vybrať tlačidlo a skontrolovať podrobnosti.

K dispozícii sú tri tlačidlá: } "Zmeny písania veľkých písmen" - dialógové okno - príklad výsledkov pre nástroj "Oprava písania veľkých písmen v rodinných menách"\]\]

Ak došlo k zmenám v písaní veľkých písmen v niektorom z mien, zobrazí sa okno s výsledkami . V okne sa zobrazí zoznam rodinných mien, ktoré Gramps môže previesť na (podľa Gramps) správnu kapitalizáciu (skontrolujte, či je pre vás správna.). V zozname okna výsledkov sú k dispozícii nasledujúce stĺpce:

- \- začiarknite alebo zrušte začiarknutie týchto políčok na základe mena, ak sa rozhodnete neprijať odporúčanie (políčko je predvolene začiarknuté)

- \- Názov, ako je aktuálne zaznamenaný.

- \- Názov so zmenou, ak sa použije.

Vyberte názvy, ktoré chcete zmeniť, a potom vyberte tlačidlo . Alebo použite tlačidlo na zrušenie zmien. {{-}}

Môžete si tiež nainštalovať doplnok "[Opraviť písanie veľkých písmen v daných menách](wiki:Opraviť_písanie_veľkých_písmen_v_daných_menách)", ktorý po nainštalovaní funguje takmer identicky ako tento nástroj, ale funguje pre "Dané mená" {{-}}

### <u>Zlúčenie citácií</u>

Môžete ho vybrať prostredníctvom ponuky .

Zobrazí sa upozornenie **Zrušiť históriu** a môžete buď alebo . {{-}} ![[_media/MergeCitations-dialog-default-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;Zlúčiť citácie&quot; - dialógové okno - predvolené]]

Potom sa zobrazí dialógové okno (Názov dialógového okna zobrazuje:*Poznámky, mediálne objekty a dátové položky zhodných citácií sa spoja.*)

K dispozícii sú nasledujúce možnosti:

- rozbaľovací zoznam:

  - Zhoda na základe strany/zväzku, dátumu a dôveryhodnosti
  - **Ignorovať dátum** (predvolené)
  - Ignorovať dôveru
  - Ignorovať dátum a dôveru

- -  (predvolene nezačiarknuté políčko)

{{-}} ![[_media/NumberOfMergesDone-dialog-result-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Dialógové okno s výsledkom &quot;Počet vykonaných zlúčení&quot; pre &quot;Zlúčiť citácie&quot; - dialógové okno - Nástroj - príklad]]

Výberom spustíte nástroj a po dokončení vám oznámi celkový počet pomocou dialógového okna výsledku. {{-}} Pozrite si tiež možnosť [Zlúčenie citácií](wiki:Gramps_6.0_Wiki_Manuál_-_Vkladanie_a_úprava_údajov:_detail_-_časť_3#Zlúčenie_citácií) dostupnú v zobrazení zoznamu Kategória citácií {{-}}

### <u>Premenovať typy udalostí</u>

Tento nástroj premenuje všetky udalosti jedného typu na iný typ.

Prístup k tomuto nástroju je možný cez ponuku

Zobrazí sa upozornenie **Zrušiť históriu** a môžete buď alebo .

{{-}} ![[_media/RenameEventTypes-Tool-ChangeEventTypes-dialog-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;Zmena typov udalostí&quot; - dialógové okno - príklad pre nástroj &quot;Premenovanie typov udalostí&quot;]]

Zobrazí sa dialógové okno .

-   
  vyplňte textové pole alebo použite rozbaľovaciu ponuku a vyberte pôvodný typ udalosti.

-   
  vyplňte textové pole (môžete tu vytvoriť úplne nový typ) alebo použite rozbaľovaciu ponuku a vyberte nový typ

Príklad ukazuje premenovanie udalosti **Narodenie** na udalosť **Krst**'.

{{-}} ![vpravo\|thumb\|450px\|Fig. {{#var:chapter}}.{{#vardefineecho:figure\|{{#expr:{{#var:figure}}+1}}}} "Zmena typov" - dialógové okno s výsledkom - príklad pre nástroj "Premenovanie typov udalostí"](RenameEventTypes-Tool-ChangeTypes-result-dialog-example-50.png "vpravo|thumb|450px|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Zmena typov" - dialógové okno s výsledkom - príklad pre nástroj "Premenovanie typov udalostí"")

Nakoniec použite na ukončenie alebo vyberte na spustenie nástroja a po jeho dokončení sa zobrazí správa o celkovom počte zmenených udalostí s dialógovým oknom výsledkov. {{-}}

Pozri tiež:

- [Úprava informácií o udalostiach](wiki:Gramps_6.0_Wiki_Manuál_-_Vkladanie_a_úprava_údajov:_podrobne_-_časť_2#Upravovanie_informácií_o_udalostiach)

### <u>Zmena poradia Gramps ID</u>

Tento nástroj môžete použiť na zmenu poradia preukazov Gramps ID. K dispozícii je niekoľko možností.

![[_media/ReorderGrampsIDs-dialog-example-60.png|vpravo|thumb|400px|Obrázok {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} ID preusporiadania]]

Tento nástroj môžete použiť prostredníctvom ponuky }.

V stĺpci "Objekt" sa uvádza typ ID. Hneď naľavo od tohto stĺpca sa nachádzajú začiarkávacie políčka, ktoré umožňujú povoliť zmeny jednotlivých typov objektov. Po začiarknutí je možné zmeniť poradie typu. Označenie "Objekt" je vlastne tlačidlo, ktorým možno prepínať všetky začiarkávacie políčka naraz.

V stĺpci "Actual" (Skutočný) je uvedený príklad aktuálneho ID. V stĺpci "Množstvo" sa zobrazuje počet objektov.

Stĺpec "Formát" možno použiť na zmenu formátu ID pre každý typ objektu. Všimnite si, že formát sa skladá z prefixu, znaku "%04d" a prípony. MUSÍ existovať aspoň prefix alebo prípona, povolené sú oba. Odporúča sa, aby boli relatívne krátke. "%04d" definuje dĺžku číselnej časti ID, "4" sa môže meniť, povolené je čokoľvek od "3" (čo umožňuje čísla od 000-999) po "9" (000000000-999999999). Tu vykonané zmeny sú rovnaké ako zmeny vykonané v ponuke a potom vyberte záložku *'[ID Formats](wiki:Gramps_6.0_Wiki_Manual_-_Settings#ID_Formats)*. Štítok 'Formát' je v skutočnosti tlačidlo, ktoré môžete použiť na obnovenie všetkých formátov na poslednú použitú hodnotu.

Stĺpec 'Zmeniť' obsahuje začiarkávacie políčka pre každý typ objektu. Ak je začiarknuté, ID pre daný objekt sa nahradia novými ID štýlu 'Format' (Formát), pokiaľ nie je začiarknuté aj 'Keep' (Ponechať). Ak nie je začiarknuté žiadne políčko, formáty ID sa NEAKTUALIZUJÚ, ale číselné pole v rámci formátu sa prečísluje. Štítok "Zmeniť" je v skutočnosti tlačidlo, ktoré možno použiť na prepínanie všetkých zaškrtávacích polí naraz.

Pole "Začiatok" označuje počiatočné číslo použité počas operácie prečíslovania. Štítok "Začiatok" je vlastne tlačidlo, ktoré možno použiť na prepínanie medzi začiatkom od 0 a začiatkom za posledným aktuálnym číslom.

Pole "Krok" označuje interval medzi číslami počas prečíslovania, "1" je jednoduchý prírastok, "2" bude prírastok o 2 atď. Označenie "Krok" je vlastne tlačidlo, ktoré možno použiť na prepínanie medzi "1", "2", "5" a "10".

Stĺpec "Keep" (Zachovať) obsahuje zaškrtávacie políčka pre každý typ objektu. Ak je začiarknuté toto políčko a políčko "Zmeniť", formáty ID pre daný objekt sa zachovajú a číselné pole v rámci formátu sa prečísluje. Štítok "Zachovať" je v skutočnosti tlačidlo, ktorým možno prepínať všetky zaškrtávacie políčka naraz.

Zobrazí sa upozornenie **Zrušiť históriu** a môžete buď , alebo .

Keď kliknete na tlačidlo "OK", nástroj zobrazí ukazovateľ priebehu.

V rôznych fázach sa zmení poradie nasledujúcich ID': Preusporiadanie ID osôb", Preusporiadanie ID rodiny", Preusporiadanie ID udalosti", Preusporiadanie ID mediálneho objektu", Preusporiadanie ID zdroja", Preusporiadanie ID citácie", Preusporiadanie ID miesta", Preusporiadanie ID úložiska" a nakoniec Preusporiadanie ID poznámky".

V ďalšom kroku sa vyhľadajú a priradia nepoužívané ID.

Počas tohto procesu nástroj preskúma každé ID, aby zistil, či nevyzerá ako "prispôsobené", či nevyzerá ako predchádzajúci formát ID alebo predvolený formát ID. Môže to byť v prípade, ak používateľ pri úprave objektu zadal do poľa ID svoj vlastný text. Môže sa to vyskytnúť aj vtedy, ak bol použitý doplnok tretej strany [GetGOV Addon](wiki:Addon:GetGOV) alebo [GeoName Addon](wiki:Addon:GeoName), pretože tento nástroj ukladá ID GOV do poľa ID. Ak sa nájde "vlastné" ID, spýta sa používateľa, či chce ID naozaj nahradiť. Dialógové okno tiež umožňuje používateľovi použiť rovnakú odpoveď pre iné nájdené prispôsobené ID.

### <u>Triedenie udalostí</u>

Udalosti zobrazené na karte Udalosť v editore osôb alebo rodín nie sú zoradené v inom konkrétnom poradí ako v poradí, v akom boli udalosti pridané. Dôvodom nevynútenia žiadneho konkrétneho zoradenia, najmä zoradenia podľa dátumu, je umožniť situáciu, keď sa o udalosti vedelo, že sa stala, ale presná chronológia nie je známa. Importovanie alebo spájanie údajov z externého zdroja môže viesť k pridaniu ďalších udalostí do existujúceho súboru udalostí osoby alebo rodiny, ale mimo ich poradia.

Udalosti môžete ručne preusporiadať [*potiahnutím a pustením*](http://en.wikipedia.org/wiki/Drag-and-drop) alebo pomocou tlačidiel na preusporiadanie na karte . Tak či onak, udalosť možno v zozname udalostí presunúť nahor alebo nadol a program Gramps si po uložení zmien zapamätá nové poradie. Nové poradie sa použije všade tam, kde sa udalosti zobrazujú inde v programe Gramps, napríklad v správe.

Poradie všetkých udalostí na karte možno zmeniť aj kliknutím na názov stĺpca. Napríklad kliknutím na nadpis stĺpca "Dátum" sa všetky udalosti zoradia v poradí podľa dátumu. Tento spôsob zoradenia udalostí je však dočasný a zmeny poradia udalostí sa po zatvorení okna nezachovajú.

Prístup [*potiahni a pusť*](http://en.wikipedia.org/wiki/Drag-and-drop) k triedeniu udalostí je vhodný na presun malého počtu udalostí, ale nie je praktický na rozsiahle zmeny. Nástroj Triediť udalosti bol navrhnutý špeciálne na tento účel, pričom pretriedi všetky udalosti v databáze alebo len tie, ktoré sú spojené s cieleným výberom osôb vybraných pomocou filtra.

Tento nástroj môžete použiť prostredníctvom ponuky .

Zobrazí sa upozornenie **Zrušiť históriu** a môžete buď alebo .

{{-}} ![[_media/SortEvents-dialog-ToolOptions-tab-default-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;Triedenie udalostí&quot; - dialógové okno - zobrazenie karty &quot;Možnosti nástroja&quot; pre nástroj &quot;Triedenie udalostí&quot;]]

Prvá možnosť v dialógovom okne slúži na definovanie rozsahu osôb, ktorých udalosti sa majú triediť. Prvá voľba v zozname je použiť triedenie na všetkých ľudí v databáze. Alternatívne možnosti sú použiť triedenie na predkov a potomkov vybranej osoby alebo na rozsah osôb vybraných pomocou vlastného vytvoreného filtra osôb. Po výbere, na koho sa má triedenie použiť, je potrebné zvážiť, ako sa majú udalosti triediť. Prvou možnosťou je triedenie podľa dátumu. Je to pravdepodobne najpravdepodobnejšia voľba, ale je možné zvoliť aj iné atribúty udalostí. Poslednou voľbou je, či majú byť udalosti zoradené vzostupne alebo zostupne a či sa má triedenie aplikovať aj na rodinné udalosti, ku ktorým vybrané osoby patria.

{{-}}

## Oprava rodokmeňa

### <u>Kontrola a oprava databázy</u>

Tento nástroj kontroluje databázu na problémy s integritou a opravuje problémy, ktoré môže. Konkrétne nástroj kontroluje:

- Porušené rodinné väzby. Ide o prípady, keď záznam osoby odkazuje na rodinu, pričom záznam rodiny neodkazuje na túto osobu a naopak.

<!-- -->

- Chýbajúce mediálne objekty. Chýbajúci mediálny objekt je objekt, na ktorého súbor sa odkazuje v databáze, ale neexistuje. Môže sa to stať, keď sa súbor omylom vymaže, premenuje alebo presunie na iné miesto.

<!-- -->

- Prázdne rodiny. Ide o záznamy rodín, ktoré nemajú odkaz na žiadnu osobu ako svojho člena.

<!-- -->

- Vzťahy medzi rodičmi. Týmto sa kontrolujú všetky rodiny, aby sa zabezpečilo, že otec a matka nie sú zamenené. Kontroluje sa tiež, či rodičia majú rozdielne pohlavie. Ak majú spoločné pohlavie, ich vzťah sa premenuje na "Partneri".

Tento nástroj môžete použiť cez ponuku .

Zobrazí sa **Upozornenie na zrušenie histórie** a môžete buď alebo .

{{-}} ![[_media/IntegrityCheckResults-dialog-CheckAndRepairDatabase-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;Výsledky kontroly integrity&quot; - príklad dialógového okna s výsledkami - pre nástroj &quot;Kontrola a oprava databázy&quot;]]

Všetky nájdené problémy sa automaticky opravia a zobrazí sa dialógové okno } "Obnovené štatistiky pohlaví" - dialógové okno výsledku pre nástroj "Obnoviť štatistiky pohlaví"\]\]

Prebuduje rodové štatistiky pre odhadnutie pohlavia mena...

Tento nástroj môžete použiť cez ponuku .

Po dokončení sa zobrazí dialógové okno s výsledkom. {{-}}

### <u>Prestaviť referenčné mapy</u>

![[_media/ReferenceMapsRebuilt-dialog-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Referenčné mapy prebudované" - dialógové okno výsledku pre nástroj "Prebudovať referenčné mapy"]]

Tento nástroj prebuduje tabuľky referenčných máp. Tým sa riadi zoznam položiek *Referencie* v editoroch.

Tento nástroj môžete použiť prostredníctvom ponuky .

Po dokončení sa zobrazí dialógové okno s výsledkom.

#### Pozrite tiež

- Táto prestavba sa vykonáva aj ako súčasť }

{{-}}

### <u>Obnoviť sekundárne indexy</u>

![[_media/SecondaryIndexesRebuilt-dialog-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Prebudované sekundárne indexy" - dialógové okno s výsledkom pre nástroj "Prebudovať sekundárne indexy"]]

Tento nástroj prebuduje sekundárne indexy.

Tento nástroj môžete použiť prostredníctvom ponuky .

Po dokončení sa zobrazí dialógové okno s výsledkom.

V ponuke sa znovu skonštruujú sekundárne tabuľky v db Stromu. Tieto tabuľky obsahujú veci ako štatistiky pohlavia (Given Name versus gender), aby bolo možné odhadnúť pohlavie mien pri ich zadávaní, priezviská (pre rýchlejšie vyhľadávanie možných priezvisk a aby fungovalo zobrazenie stromu osôb), rôzne ID pre objekty (pre uľahčenie vyhľadávania podľa ID), tabuľky príloh miest, aby fungovalo zobrazenie stromu miest, a niekoľko ďalších.

Teoreticky sa tieto tabuľky neustále aktualizujú, keď sa niečo zmení. Preto by nemalo byť potrebné obnovovať referenčné mapy a sekundárne indexy. Ale najmä na začiatku histórie programu Gramps chyby niekedy bránili správnemu dokončeniu aktualizácií. Takže tieto nástroje zostávajú k dispozícii... ‘pre prípad’.

#### Pozrite si tiež

- Táto obnova sa vykonáva aj v rámci

{{-}}

### <u>Odstrániť nepoužívané objekty</u>

Tento nástroj vyhľadá vo vašej databáze časti informácií, ktoré nie sú spojené s ničím iným, a potom vám umožní upraviť a pripojiť informácie alebo ich odstrániť.

Tento nástroj môžete použiť prostredníctvom ponuky .

{{-}} ![[_media/UnusedObjects-dialog-example-results-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;Nepoužívané objekty&quot; - príklad výsledkov dialógového okna pre nástroj &quot;Odstrániť nepoužívané objekty&quot;]]

Zobrazí sa dialógové okno .

V hornej časti dialógového okna si môžete vybrať z možností vyhľadávania, ktoré chcete použiť:

-  (predvolene začiarknuté políčko)

-  (štandardne začiarknuté políčko)

-  (štandardne začiarknuté políčko)

-  (štandardne začiarknuté políčko)

-  (políčko je predvolene začiarknuté)

-  (štandardne začiarknuté políčko)

-  (políčko je predvolene začiarknuté)

Výberom tlačidla spustíte hlásenie a po dokončení sa prípadné výsledky zobrazia v dolnej časti dialógového okna s nasledujúcimi zobrazenými stĺpcami:

- Vyberte riadok, ak chcete objekt vymazať (začiarkávacie políčko je štandardne nezačiarknuté)

- \- Ikona reprezentujúca typ objektu.

- \- Interný názov objektu v gramatike.

- \- objektu.

Ak chcete preskúmať objekt, musíte dvakrát kliknúť na riadok a zobrazí sa príslušný editor pre objekt, ktorý vám v prípade potreby umožní úpravy.

objekty, ktoré chcete odstrániť, buď pomocou jednotlivých zaškrtávacích políčok, alebo pomocou príslušných tlačidiel:

- 

- 

- 

Po výbere možností vymazania vyberte tlačidlo , aby ste vymazali objekty.

Po dokončení môžete nástroj ukončiť pomocou tlačidla . {{-}}

## Nástroje

Táto časť obsahuje nástroje, ktoré vám umožňujú vykonať jednoduchú operáciu s časťou údajov. Výsledky môžete uložiť do databázy, ale nezmenia vaše existujúce údaje. V súčasnosti sú v programe Gramps k dispozícii nasledujúce nástroje:

- [Find database loop](wiki:Gramps_6.0_Wiki_Manual_-_Tools#Find_database_loop) -
- [Media Manager](wiki:Gramps_6.0_Wiki_Manual_-_Tools#Media_Manager) -
- [No Related](wiki:Gramps_6.0_Wiki_Manual_-_Tools#No_Related) -
- [Kalkulátor vzťahov](wiki:Gramps_6.0_Wiki_Manual_-_Tools#Kalkulátor_vzťahov) -
- [Overify the Data](wiki:Gramps_6.0_Wiki_Manual_-_Tools#Verify_the_Data) -

### <u>Čistenie vstupných údajov</u>

### <u>Odstrániť úvodné a koncové medzery</u>

![[_media/CleanInputData-dialog-tool-example-dialog-51.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Čisté vstupné údaje]]

Nástroj na potlačenie počiatočných a koncových medzier.    Nástroj vyhľadáva názvy miest s úvodnými a/alebo koncovými medzerami. Vyhľadáva tiež v mene a priezvisku.

Prístup k nemu je možný z ponuky }.

Pozrite si tiež:

- [Nový nástroj na potlačenie úvodných a končiacich medzier.](https://github.com/gramps-project/gramps/pull/783) - (pridané v programe Gramps 6.0.0)

### <u>Vyhľadanie slučky databázy</u>

![[_media/FindDatabaseLoop-dialog-example1-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Nájsť možnú slučku]]

Nástroj umožňuje overiť, či sa v databáze nachádzajú slučky predkov.

Ak ho vyberiete cez ponuku }, zobrazí sa okno . Okno má päť záložiek: , , , , .

1.  Prvé Gramps_ID je odkaz na Rodiča.
2.  Rodič (Predok na obrázku) je osoba, ktorej hľadáme slučku.
3.  Druhé ID_rodiča je odkaz na dieťa.
4.  Dieťa (Potomok) je pôvodca slučky.
5.  Family_ID je odkaz na príslušnú rodinu

{{-}}

![[_media/FindDatabaseLoop-dialog-example2-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Nájsť možnú slučku v zložitom príklade]]

V nasledujúcom zložitom príklade máme viacero predchodcovských slučiek :

Ak sa pozrieme na druhý riadok, máme :

1.  Prvé Gramps_ID : I0002
2.  Rodič je : Otec, Dieťa2
3.  Second Gramps_ID : I0001
4.  Child is : Otec, Otec
5.  Family_ID je : F0000

Aby ste pochopili, čo sa deje :

1.  začneme na \[I0002\] Otec, Dieťa2.
2.  Pokračujeme jeho synom \[I0003\] Otec, dieťa3.
3.  Pokračujeme jeho synom : \[I0000\] Dieťa, Dieťa.
4.  Pokračujeme jeho synom : \[I0001\] Otec, Otec.
5.  Pokračujeme jeho synom : \[I0002\] Otec, Dieťa2 ==\> **TU máme rodovú slučku**.

{{-}} Viac informácií o rodových slučkách nájdete na stránke:

- [Hľadanie predkovských slučiek : skúsenosti s moderným softvérom](https://www.tamurajones.net/FindingAncestralLoops.xhtml)
- [Ancestral Loops : Behold Blog Louisa Kesslera](http://www.beholdgenealogy.com/blog/?p=1309)

### <u>Mediálny manažér</u>

![[_media/Introduction-page-MediaManager-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Úvod - stránka pre "Gramps Media Manager" - Sprievodca nástrojmi]]

je skupina štyroch samostatných nástrojov prístupných prostredníctvom dialógového okna podobného sprievodcovi, ku ktorému sa dostanete cez menu , ktoré zobrazí prvú **Úvodnú**' dialógovú stránku s nasledujúcimi informáciami o schopnostiach nástrojov.

{{-}}

Na stránke **Úvod** sa výberom tlačidla (alebo použitím klávesovej skratky ) zobrazí okno stránky **Výber**.

![[_media/Selection-page-MediaManager-default-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Výber - stránka pre "Gramps Media Manager" - Sprievodca nástrojmi - predvolené]]

V okne stránky **Výber** vyberte zo štyroch možností jednu z akcií, ktoré chcete vykonať, a potom vyberte tlačidlo :

- } (predvolené)

- 

- }

- 

{{-}}

#### Nahradenie podreťazcov v ceste

![[_media/ReplaceSubstringSettings-page-MediaManager-default-50.png|Obrázok {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Nahradiť nastavenia podreťazca - stránka pre "Gramps Media Manager" - Sprievodca nástrojmi - predvolené]]

Tento nástroj umožňuje nahradiť zadaný podreťazec v ceste k mediálnym objektom iným podreťazcom. Môže to byť užitočné pri presúvaní mediálnych súborov z jedného adresára do druhého.

Výberom tohto prepínača sa zobrazí okno , v ktorom môžete do textového poľa a do textového poľa zadať ľubovoľný reťazec. Kedykoľvek môžete kliknúť na tlačidlo alebo na tlačidlo . Kliknutím na tlačidlo sa zobrazí okno .

{{-}}

#### Konverzia ciest z relatívnych na absolútne

![[_media/ConvertPathsFromRelativeToAbsolute-FinalConfirmation-page-MediaManager-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Convert paths from relative to absolute": "Final Confirmation" page for "Gramps Media Manager" - Tool wizard - example]]

Tento nástroj umožňuje konvertovať relatívne cesty k médiám na absolútne. Robí to tak, že predvyplní , ako je uvedené na karte [Upraviť &gt; Predvoľby &gt; Všeobecné](wiki:Gramps_6.0_Wiki_Manuál_-_Nastavenia#Všeobecné)\], alebo ak táto nie je nastavená, predvyplní predvolený [Adresár užívateľa](wiki:Gramps_6.0_Wiki_Manuál_-_Adresár_užívateľa).

- [Absolútne a relatívne cesty](https://en.wikipedia.org/wiki/Path_(computing)#Absolute_and_relative_paths), Z Wikipédie.
- [Absolútne, relatívne, UNC a URL cesty](https://desktop.arcgis.com/en/arcmap/latest/tools/supplement/pathnames-explained-absolute-relative-unc-and-url.htm) Pomocník programu ArcMap.

{{-}}

#### Konverzia ciest z absolútnych na relatívne

![[_media/ConvertPathsFromAbsoluteToRelative-FinalConfirmation-page-MediaManager-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Convert paths from absolute to relative": "Final Confirmation" page for "Gramps Media Manager" - Tool wizard - example]]

Tento nástroj umožňuje konvertovať absolútne cesty k médiám na relatívne cesty. Relatívna cesta je relatívna voči zadanej základnej ceste v nastavení ako z karty [Upraviť &gt; Predvoľby &gt; Všeobecné](wiki:Gramps_6.0_Wiki_Manuál_-_Nastavenia#Všeobecné), alebo ak nie je nastavená, použije sa adresár používateľa. Relatívna cesta umožňuje naviazať umiestnenie súboru na základnú cestu, ktorá sa môže meniť podľa vašich potrieb.

- [Absolútne a relatívne cesty](https://en.wikipedia.org/wiki/Path_(computing)#Absolute_and_relative_paths), Z Wikipédie.
- [Absolútne, relatívne, UNC a URL cesty](https://desktop.arcgis.com/en/arcmap/latest/tools/supplement/pathnames-explained-absolute-relative-unc-and-url.htm) Pomocník programu ArcMap.

{{-}}

#### Pridanie obrázkov, ktoré nie sú zahrnuté v databáze

![[_media/AddImagesNotIncludedInDatabase-FinalConfirmation-page-MediaManager-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Add images not included in database": "Final Confirmation" page for "Gramps Media Manager" - Tool wizard - example]]

Kontrola adresárov na obrázky, ktoré nie sú zahrnuté v databáze, tento nástroj pridáva obrázky do adresárov, na ktoré odkazujú existujúce obrázky v databáze. Budete musieť manuálne importovať jeden mediálny prvok z každého podadresára. Správca médií nezahŕňa podadresáre automaticky. Prehľadajú sa všetky cesty k adresárom zobrazené v nástroji. {{-}}

### <u>Nesúvisí</u>

![[_media/NotRelatedTo-dialog-NotRelated-Tool-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}}. "Nesúvisí s "..." - dialógové okno - zobrazenie výsledkov pre nástroj "Nesúvisí"]]

Tento nástroj zobrazí zoznam osôb, ktoré nie sú prepojené s vybranou aktívnou osobou. Spojenia môžu zahŕňať prepojenia v reťazci [referencie](wiki:Odkazy) alebo prepojenia vytvorené pomocou [editor odkazov v Poznámkach](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_2/sk#Editor_odkazov).

Tento nástroj môžete použiť prostredníctvom ponuky }.

Zobrazí sa dialógové okno výsledkov, v ktorom sa zobrazí zoznam všetkých osôb, ktoré nie sú **NESÚVISIACE** s vybranou osobou.

Tento zoznam vám poskytne:

- *Meno*
- *ID*
- *Rodičia*
- *Značky*

V stĺpci *Názov* môžete použiť tlačidlá a na zbalenie alebo rozbalenie zoskupeného zoznamu *Názov*. Dvojitým kliknutím na osobu sa zobrazí dialógové okno alebo .

Ak vyberiete osobu, môžete použiť textové pole (môžete vyplniť ľubovoľný vlastný názov značky, ktorý chcete použiť) alebo použiť rozbaľovací zoznam a vybrať existujúcu značku, napr. Pomocou tlačidla pridajte vybraný tag k osobe (osobám). Tento tag sa potom zobrazí v stĺpci *Tagy*. {{-}}

### <u>Kalkulátor vzťahov</u>

![[_media/RelationshipTo-dialog-RelationshipCalculator-Tool-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;Vzťah k &quot;... &quot; - dialógové okno - zobrazenie výsledkov pre nástroj &quot;Kalkulátor vzťahov&quot;]] Tento nástroj môžete použiť prostredníctvom ponuky .

Výberom nástroja Kalkulátor vzťahov sa otvorí zoznam filtrovaný na všetky osoby spojené, **ale nie nevyhnutne príbuzné**, s [Active Person](wiki:Gramps_Glossary#active_person). Ak chcete vypočítať vzťah k inej osobe, zatvorte okno, urobte túto osobu Aktívnou a znovu vyberte nástroj z ponuky.

Vyberte osobu z filtrovaného zoznamu, aby ste mohli oznámiť, či existuje vzťah. Presný vzťah sa zobrazí v dolnom paneli spolu so spoločnými predkami tohto nahláseného vzťahu. Zobrazia sa len pokrvné vzťahy (okrem vzťahov medzi manželom a manželkou). Všimnite si, že sa nezobrazia vzťahy "príbuzenský vzťah".

Filtrovaný zoznam bude zoskupený a abecedne zoradený podľa priezviska. (Bez ohľadu na to, či bolo nastavenie ponuky Zobraziť v kategórii Osoba nastavené na možnosť **Zoskupené**). Stĺpce zoznamu nie je možné opätovne zoradiť.

Stupeň oddelenia (generačná vzdialenosť), ktorý bude rozpoznaný, sa riadi hodnotou *Max. generácie pre vzťahy* v záložke [Všeobecné](wiki:Gramps_6.0_Wiki_Manual_-_Settings/sk#Všeobexné) v ponuke . (Predvolená hodnota 15 generácií oznámi vzťah 12 prarodičov, ale nie ich rodičov. Aktívna osoba sa počíta ako jedna z generácií.)

V podstate sú akékoľvek dve osoby priamo pokrvne príbuzné, ak majú spoločného predka. Jedna z týchto osôb môže byť v skutočnosti predkom druhej osoby - napríklad prastarým rodičom. Aj v prípadoch tiet a strýkov môžete príbuzenský vzťah vypočítať tak, že vyhľadáte spoločného predka. V tomto prípade bude otec alebo matka tety alebo strýka starým rodičom synovca alebo netere.

Najzákladnejším pokrvným príbuzenským vzťahom prostredníctvom spoločných predkov je príbuzenský vzťah súrodencov (bratov a sestier), ktorí sú od spoločného predka vzdialení len jednu generáciu. Ďalším osobitným vzťahom je vzťah jedného z týchto súrodencov k potomkom ostatných súrodencov. Ak je Aktívna osoba vnukom spoločného predka, súrodenec by bol tetou alebo strýkom. Okrem tejto generácie potomkov existujú dva rovnocenné spôsoby opisu vzťahu. Dcéra prastarých rodičov by sa mohla nazývať buď babička, alebo prateta. (V kalkulačke vzťahov sa používa variant "grand".) Táto osoba je prababičkou pre druhých prapravnukov, ktorí sú od spoločného predka vzdialení štyri generácie. (Môže sa nazývať aj druhá prateta.) Opačným príbuzenským vzťahom tety alebo strýka je synovec alebo neter.

Bratranci a sesternice (nazývaní aj "prví" bratranci a sesternice) sú vzdialení dve generácie od spoločného predka prostredníctvom rôznych súrodencov. "Druhí" bratranci a sesternice sú teda tri generácie po spoločnom predkovi - a tak ďalej.

Potom sa každý považuje za "bratranca a sesternicu", ale na označenie toho, že nie sú v rovnakej generácii, používame slovo "vzdialený", ktoré označuje počet generácií, ktoré sa medzi nimi líšia. Napríklad "prvý" bratranec môjho otca je aj môj "prvý" bratranec, ale "raz vzdialený" (rozdiel medzi nami je jedna generácia). "Prvý" bratranec môjho otca je "dvakrát vzdialený" bratranec môjho vlastného dieťaťa - rozdiel dvoch generácií.

Ak existuje viacero pokrvných príbuzenských vzťahov v dôsledku zrútenia rodokmeňa, všetky budú uvedené.

Úplný textový zoznam všetkých pokrvných príbuzných a ich manželských partnerov si môžete pozrieť pomocou [Správa o príbuzenstve](wiki:Gramps_6.0_Wiki_manual_-_Správy_-_časť_6#Správa_o_príbuzenstve).

#### Pozri tiež:

- Voľba **Vzťah k domovskej osobe** [Predvoľby zobrazenia](wiki:Gramps_6.0_Wiki_Manual_-_Settings/sk#Zobrazenie) pre stavový riadok
- **Vzťah k domovskej osobe** [Rýchle zobrazenie](wiki:Gramps_6.0_Wiki_Manuál_-_Príručka_-_Zprávy_-_časť_8#Rýchle_zobrazenie).
- *'[Hlboké spojenia](wiki:Hlboké_spojenia_grampletu)* gramplet: Ak je nainštalovaný tento doplnok tretej strany, zobrazí zoznam generácií, ktoré zasahujú do spoločného predka prostredníctvom súrodeneckých potomkov. (Nevypíše však spoločného predka ani to, či sú obe osoby prepojené cez toho istého manžela/manželku.) Gramplet uvádza aj podrobné údaje o nepriamych príbuzenských vzťahoch.

{{-}}

### <u>Overenie údajov</u>

![[_media/VerifyTheData-DataVerifyTool-dialog-General-tab-defaults-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Overenie údajov..." - Dialógové okno "Nástroj na overenie údajov" - karta "Všeobecné" - predvolené nastavenia]]

Tento nástroj umožňuje overiť databázu na základe súboru vami zadaných kritérií.

Môžete sa napríklad uistiť, že nikto vo vašej databáze nemal deti vo veku 98 rokov. Na základe zdravého rozumu by takýto záznam znamenal chybu. Nejde však o chybu konzistencie v databáze. Okrem toho niekto môže mať dieťa vo veku 98 rokov (hoci sa to stáva zriedkavo). Nástroj Overiť zobrazí všetko, čo porušuje vaše kritériá, aby ste mohli skontrolovať, či je záznam chybný alebo nie. Konečné rozhodnutie je na vás.

Ak ho vyberiete cez ponuku , zobrazí sa okno . Okno má štyri záložky: , , , . Na týchto záložkách sa zobrazuje zoznam s kritériami a vstupné pole, v ktorom môžete zmeniť hodnotu kritérií. V nasledujúcich zoznamoch uvádzam niektoré *použiteľné* hodnoty.

#### Overenie stránok karty Údaje

Z nasledujúcich kariet vyberte kritériá, s ktorými chcete nástroj spustiť. Ak sú kritériá v poriadku, kliknite na tlačidlo (alebo stlačte a zobrazí sa vám okno .

V závislosti od vašich kritérií a údajov sa zobrazí zoznam. Niektoré možnosti zistení sú uvedené nižšie. Existujú však aj ďalšie.

- Odpojené osoby (osoby bez rodiča alebo manžela/manželky, dieťaťa alebo súrodenca)
- Starý/mŕtvy otec
- manželstvo po smrti/pred narodením
- veľké rozpätie rokov pre všetky deti
- skoré/neskoré manželstvo
- mladá/nezadaná matka
- manžel a manželka s rovnakým priezviskom
- manželstvo rovnakého pohlavia/manželka
- ...

##### Všeobecné

-   
  90

-   
  17

-   
  50

-   
  3

-   
  30

-   
  99

Prvé začiarkávacie políčko: spôsobí, že nástroj akceptuje dátum krstu, ak nie je známy dátum narodenia, a akceptuje dátum pohrebu, ak nie je známy dátum úmrtia. Taktiež spôsobí, že nástroj akceptuje "nepresné" dátumy (t. j. akýkoľvek "zákonný" dátum Gramps, ktorý nie je plne špecifikovaný (s explicitným dňom a mesiacom a rokom)).

Druhé začiarkávacie políčko: skontroluje, či sú dátumy neplatné.

##### Ženy

-   
  17

-   
  48

-   
  12

##### Muž

-   
  18

-   
  65

-   
  15

##### Rodiny

-   
  30

-   
  8

-   
  25

{{-}}

#### Okienko s výsledkami overovania údajov

![[_media/DataVerificationResults-window-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Okno výsledkov overovania údajov]].

Po spustení nástroja sa vám zobrazí okno .

V spodnej časti okna sú k dispozícii štyri tlačidlá na uľahčenie výberu. Sú to , , a .

Dvojkliknutím na riadok získate možnosť zobraziť a prípadne upraviť údaje.

Pomocou tlačidla (alebo vyberte klávesovú skratku ) zatvoríte okno . {{-}}

#### Príklady

Dva príklady z používania skutočných údajov s týmto nástrojom:

- Pri kontrole údajov som našiel rodinu s otcom : Anna Roelants. Našťastie v som si prečítal: *Manželstvo Adama Roelantsa a Cornelie Crabbeovej*. Bol to zjavne preklep: Anna i.s.o. Adam. Bez tejto **pomôcky**' by sa to veľmi ťažko hľadalo.

\*:Upozornenie ukazovalo 'neskoré manželstvo': kontrola údajov: mužská osoba °1738 ženská osoba °1756 : sobáš X 1804 \[gregoriánsky kalendár\] : Všetko sa zdalo byť v poriadku: takže sa (znovu)vzali vo veku 66 a 48 rokov! Upozornenie sa objavilo, pretože **Všeobecné kritériá** boli nastavené na hodnotu **60**.

{{-}}

## Ladenie

![[_media/MenuOverview-Tools-Debug-menu-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "" Menubar - Nástroje - Prehľad menu Ladenie]]

Ak nie je zapnutý príznak optimalizácie pythonu `-O`, v ponuke sa objaví ďalšia položka .

Pozrite si [Príkazový riadok: Možnosti Pythonu](wiki:Gramps_6.0_Wiki_príručka_-_Príkazový_riadok#Možnosti_Pythonu). {{-}}

### Kontrola lokalizovaného zobrazovača a analyzátora dátumu

![[_media/StartDateTest-dialog-CheckLocalizedDateDisplayerAndParser-Tool-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figurr|{{#expr:{{#var:figure}}+1}}}} Dialógové okno "Spustiť test dátumu?" - pre "Kontrolu lokalizovaného zobrazovača a analyzátora dátumu" - nástroj]]

Tento testovací nástroj vytvorí mnoho ľudí, ktorí zobrazia všetky rôzne varianty dátumu ako narodenia. Dátum úmrtia sa vytvorí rozborom výsledku zobrazovača dátumu pre dátum narodenia. Týmto spôsobom sa môžete uistiť, že vytlačené dátumy sa dajú správne analyzovať späť.

{{-}}

### Výpis štatistiky pohlavia

![[_media/GenderStatisticsTool-dialog-DumpGenderStatistics-Tool-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Príklad výsledkov dialógového okna "Štatistiky pohlaví" - pre "Výpis štatistík pohlaví" - nástroj]]

Vypíše štatistiky pre pohlavie odhadované z krstného mena. {{-}}

### Generovanie testovacích prípadov pre osoby a rodiny

![[_media/GenerateTestcases-dialog-GenerateTestcasesForPersonsAndFamilies-Tool-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Dialógové okno "Generovanie testovacích prípadov" - pre "Generovanie testovacích prípadov pre osoby a rodiny" - nástroj - predvolené]]

Generátor testovacích prípadov vygeneruje niektoré osoby a rodiny, ktoré majú nefunkčné prepojenia v databáze alebo údaje, ktoré sú v rozpore so vzťahom.

Zobrazí sa dialógové okno a vy môžete buď alebo .

{{-}}

### Vyplnenie zdrojov a citácií

![[_media/PopulateSourcesAndCitationsTool-dialog-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Dialógové okno "Vyplniť nástroj zdroje a citácie" - predvolené]]

Tento nástroj generuje zdroje a citácie pre každý zdroj s cieľom naplniť databázu pre testovanie so značným počtom zdrojov a citácií.

{{-}}

[Category:Sk:Documentation](wiki:Category:Sk:Documentation) [Category:Tools](wiki:Category:Tools) [Category:Plugins](wiki:Category:Plugins)
