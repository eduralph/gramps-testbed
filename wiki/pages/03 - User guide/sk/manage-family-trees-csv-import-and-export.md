---
title: 'Gramps 6.0 Wiki Manual - Manage Family Trees: CSV Import and Export/sk'
categories:
- Gramps Examples
- Sk:Documentation
- Stub
managed: false
source: wiki-scrape
wiki_revid: 119801
wiki_fetched_at: '2026-05-30T20:08:54Z'
lang: sk
---

{{#vardefine:chapter\|6}} {{#vardefine:figure\|0}} Táto časť sa týka používania programu Gramps s formátom **Tabuľka s hodnotami oddelenými čiarkou (CSV)**.

- [Gramps CSV import](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees#Gramps_CSV_import)
- [Comma Separated Values Spreadsheet(CSV) export](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees#Comma_Separated_Values_Spreadsheet.28CSV.29_export)

Môžete tiež [Exportovať](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Export_View) aktuálne zobrazenie zoznamu do tabuľky (\*.ODT) alebo súboru CSV.

## Import/export tabuľky Gramps

Tento formát umožňuje importovať/exportovať tabuľku s údajmi naraz. Tabuľka musí byť vo formáte CSV (Comma Separated Value). Väčšina tabuľkových programov dokáže tento formát čítať a zapisovať. Dá sa tiež ľahko zapísať ručne. Toto je jediný formát importu programu Gramps, ktorý umožňuje zlúčenie s existujúcimi údajmi.

Existujú tri hlavné spôsoby použitia tohto formátu:

1.  Môžete exportovať svoje základné údaje programu Gramps do formátu tabuľky, upraviť ich pomocou textového alebo tabuľkového programu a importovať zmeny a doplnenia späť do programu Gramps. To je vhodné na posielanie iným osobám na vyplnenie alebo na cesty, keď nemáte k dispozícii celú aplikáciu Gramps.
2.  Do databázy Gramps môžete importovať nové údaje. Ak máte napríklad súbor nových osôb, ktoré chcete pridať do svojej databázy, ale nechcete loviť a pátrať po tom, kde sa nachádzajú, môže byť jednoduchšie zadať ich do tabuľky a potom ich všetky naraz rýchlo vložiť. To je vhodné, ak máte veľké množstvo údajov, ktoré vyrezávate a vkladáte z inej aplikácie alebo z webu. Príkladom je [obnovenie databázy Gramps](wiki:Naratívna_Webová_stránka_Import) načítaním Naratívnej webovej stránky do tabuľky.
3.  Môžete tiež importovať súbor opráv a doplnení. Povedzme, že ste si vytlačili správu a prechádzate ňou a vyznačujete opravy. Ak z každej opravy vytvoríte časť tabuľky, môžete "naskriptovať úpravy" a potom ich vykonať všetky naraz.

## Export

![[_media/ExportAssistant-ExportOptions-CSV-defaults-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Asistent exportu - Možnosti exportu - dialógové okno sprievodcu (zobrazujúce predvolené nastavenia pre "Tabuľkový procesor s hodnotami oddelenými čiarkou(CSV)") so zvýraznenou spodnou časťou pre možnosti špecifické pre formát súboru]]

Ak chcete exportovať svoju databázu:

1.  Start Gramps
2.  Vyberte z ponuky
3.  Vyberte v okne .
4.  V okne vyberte **Tabuľka s hodnotami oddelenými čiarkami (CSV)**.
5.  V okne .
    1.  V hornej časti vyberte, ktoré filtre sa majú použiť na váš rodokmeň
    2.  V začiarkávacích políčkach vyberte, ktoré položky sa majú zahrnúť do exportu (osoby, manželstvá, deti, miesta) a či sa majú záhlavia preložiť do jazyka, ktorý používate.

{{-}}

Vybraný súbor polí vašich genealogických údajov sa uloží do súboru .csv v nižšie opísanom formáte. Okrem toho sa na osoby a rodiny odkazuje, aby bolo možné údaje upraviť a načítať späť, čím sa aktualizuje databáza.

Niektoré stĺpce budú prázdne, konkrétne stĺpce poznámka a zdroj. Tieto sú uvedené v tabuľke, aby ste si mohli urobiť poznámky pre import, ale poznámky sa nikdy neexportujú pomocou tohto nástroja.

Vaše údaje sú rozdelené do štyroch častí, ktoré predstavujú miesta, osoby, manželstvá a deti. Exportované polia a názvy stĺpcov sú:

Miesta  
Miesto, Názov, Názov, Typ, Zemepisná šírka, Zemepisná dĺžka, Kód, Pripojené_podľa, Dátum

<!-- -->

Jednotlivci  
Osoba, Priezvisko, Meno, Volanie, Prípona, Predpona, Titul, Pohlavie, Dátum narodenia, Miesto narodenia (alebo miesto narodeniaid), Zdroj narodenia, Dátum krstu, Miesto krstu (alebo miesto krstuid), Zdroj krstu, Dátum úmrtia, Miesto úmrtia (alebo miesto úmrtiaid), Zdroj úmrtia, Dátum pochovania, Miesto pochovania (alebo miesto pochovaniaid), Zdroj pochovania, Poznámka

<!-- -->

sobáše  
Manželstvo, Manžel, Manželka, Dátum, Miesto (alebo Placeid), Zdroj, Poznámka

<!-- -->

Rodiny  
Rodina, dieťa

Prvý stĺpec v každej oblasti je identifikátor dedka. Práve ten bude spájať vaše úpravy so správnymi údajmi, preto tieto údaje nemeňte. Tento súbor načítajte do svojho obľúbeného tabuľkového procesora s použitím oddeľovania čiarkou, dvojitých úvodzoviek a textového formátu (zatiaľ v ľubovoľnom kódovaní). Potom môžete pridať alebo opraviť údaje a uložiť ich späť von, pričom zachováte rovnaký formát. Potom môžete údaje importovať späť na staré údaje a budú opravené.

. .

## Import

Import údajov:

1.  Použite súbor z vyššie uvedeného alebo vytvorte tabuľku (popísanú [ďalej](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees:_CSV_Import_and_Export#Example_CSV_with_multiple_areas)) s genealogickými údajmi
2.  Spustite Gramps
3.  Vytvorte nový rodinný strom
4.  Vyberte z ponuky
5.  Vyberte súbor **Tabuľka s hodnotami oddelenými čiarkou (CSV)** a potom vyberte tlačidlo .

Časť tohto kódu na zlúčenie iba pridá alebo aktualizuje informácie do vašej databázy a vždy predpokladá, že údaje tabuľky sú správnou verziou.

Ak túto tabuľku načítate do LibreOffice, uistite sa, že ste každý stĺpec vybrali ako typ **Text** a nie **Štandardný**. Štandardný preformátuje vaše dátumy a čísla. Ak používate Excel, pravdepodobne budete chcieť vybrať všetky bunky po otvorení a zmeniť formát buniek na **Text**.

Tabuľka obsahuje údaje zložené zo stĺpcov. Každý stĺpec by mal mať v hornej časti názov, aký typ údajov sa v ňom nachádza. Prvý stĺpec v každej oblasti je odkaz na identifikačné číslo Gramps. Pre stĺpce musíte používať špeciálne názvy. Sú to:

### Miesto

    place (miesto) - odkaz na toto miesto
    title - názov miesta
    name - názov miesta
    type - typ miesta (napr. mesto, okres, štát atď.)
    latitude - zemepisná šírka miesta
    zemepisná dĺžka - zemepisná dĺžka miesta
    kód - poštové smerovacie číslo atď.
    enclosed_by - odkaz na iné miesto, ktoré obklopuje toto miesto
    date - dátum, kedy bolo miesto enclosed_by v platnosti

### Ľudia

    osoba - odkaz, ktorý sa použije pre rodiny (manželstvá a deti) 
    grampsid - na priradenie identifikátora Gramps k osobe
    firstname - dané (krstné) meno, prvé meno osoby
    priezvisko/posledné meno - priezvisko, posledné meno osoby
    callname (meno) - používané meno (prezývka) osoby
    predpona - predpona priezviska (von, de atď.)
    prípona - prípona mena osoby (Jr., Sr.)
    titul - titul osoby (Dr., Mr.)
    pohlavie - mužský alebo ženský rod (mali by ste použiť preklad pre váš jazyk)
    poznámka - poznámka pre záznam osoby

    dátum narodenia - dátum narodenia
    miesto narodenia - miesto narodenia
    birthplaceid - identifikátor miesta narodenia
    birthsource - názov zdroja narodenia

    baptismdate - dátum krstu
    baptismplace - miesto krstu
    baptismplaceid - identifikátor miesta krstu
    baptismsource - názov zdroja krstu

    deathdate - dátum úmrtia
    deathplace - miesto úmrtia
    deathplaceid - identifikátor miesta úmrtia
    deathsource - názov zdroja úmrtia
    deathcause - príčina smrti

    burialdate - dátum pohrebu
    burialplace - miesto pochovania
    burialplaceid - identifikátor miesta pochovania
    burialsource - názov zdroja pohrebu

    occupationdate - dátum zamestnania
    occupationplace - miesto výkonu povolania
    occupationplace_id - identifikátor miesta výkonu povolania
    occupationsource - zdrojový názov povolania
    occupationdescr - popis povolania

    residencedate - dátum bydliska
    residenceplace - miesto bydliska
    residenceplace_id - identifikátor miesta bydliska
    residencesource - názov zdroja bydliska

    attributetype - typ atribútu
    attributevalue - hodnota atribútu
    attributesource - názov zdroja atribútu

### Manželstvo

    manželstvo - ak sa chcete odvolať na tento atribút z rodiny, budete tu potrebovať zodpovedajúci názov
    manžel/otec/rodič1 - odkaz na vyššie uvedenú osobu, ktorá je manželom 
                                                      (v prípade rodiča1 ženského pohlavia budete musieť uviesť pohlavie v oblasti osoby, 
                                                      alebo ho upravte neskôr v gramatike)
    manželka/matka/rodič2 - odkaz na vyššie uvedenú osobu, ktorá je manželkou 
                                                      (v prípade mužského rodiča2 budete musieť uviesť pohlavie v oblasti osoby, 
                                                      alebo ho upravte neskôr v programe gramps)
    date (dátum) - dátum uzavretia manželstva
    miesto - miesto sobáša
    placeid - identifikátor miesta sobáša
    source - názov zdroja manželstva
    poznámka - poznámka o manželstve/svadbe

### Rodina

    rodina - odkaz na spojenie s vyššie uvedeným manželstvom (povinné)
    dieťa - odkaz na vyššie uvedenú osobu, ktorá je dieťaťom
    source - zdrojový názov manželstva
    poznámka - poznámka o rodine
    pohlavie - muž alebo žena (mali by ste použiť preklad pre váš jazyk) 
                      [Pohlavie môžete uviesť tu alebo v osobe vyššie]

## Podrobnosti

V názvoch stĺpcov sa nerozlišujú veľké a malé písmená. Môžete použiť ľubovoľnú kombináciu stĺpcov v ľubovoľnom poradí. (*'V skutočnosti musíte mať pri definovaní osoby aspoň priezvisko a meno, pri definovaní detí musíte mať stĺpce manželstvo a dieťa a miesta potrebujú odkaz na miesto, ale to je všetko."*) Názvy stĺpcov sú uvedené anglické názvy (zatiaľ), ale údaje by mali byť vo vašom jazyku (vrátane slov "muž" a "žena").

Poradie zhora nadol je dôležité v tom zmysle, že ak sa chcete na niečo v jednej oblasti odvolať na inú, definícia MUSÍ byť na prvom mieste. Napríklad, ak chcete definovať rodiny ľudí, osoby musia byť definované pred rodinami. To isté platí pre miesta. Preto je zvyčajne najlepšie najprv uviesť údaje o miestach, potom o ľuďoch, potom o manželstvách a rodinách.

Každý z týchto údajov môže ísť do vlastnej oblasti v tabuľke. Počet oblastí v hárku nie je obmedzený a každá oblasť môže mať ľubovoľný počet riadkov. Medzi "oblasťami" nechajte prázdny riadok. Dbajte len na to, aby oblasti neboli vedľa seba; musia byť nad a pod sebou.

V tabuľke môžete mať viacero oblastí každého druhu. Jediným obmedzením je, že ak sa odvolávate na osobu, musíte to urobiť v riadku nižšie, ako je miesto, kde je táto osoba opísaná. Podobne, ak odkazujete na manželstvo, musíte to urobiť v riadku nižšie, ako je miesto, kde je manželstvo opísané. Odkazy na miesta enclosed_by už musia existovať v databáze alebo musia byť definované v riadkoch vyššie v tabuľke.

Ak používate "grampsid" ako spôsob priradenia konkrétnych id, buďte *veľmi* opatrní pri importe do aktuálnej databázy. Akékoľvek údaje, ktoré zadáte, **prepíšu** údaje priradené k tomuto grampsid. Ak použijete id v stĺpcoch miesto, osoba, manželstvo alebo rodina, ktoré sú obklopené zátvorkami (napríklad '\[I0001\]'), budú sa použité hodnoty tiež interpretovať ako grampsid. Ak pridávate **nové** položky, odporúčame vám vyhnúť sa používaniu formátu zátvoriek alebo stĺpcov grampsid, aby ste sa vyhli náhodnému prepísaniu údajov. Ak miešate metódy so zátvorkami (alebo grampsid) s obyčajnými odkazmi (bez zátvoriek), umiestnite obyčajné odkazované údaje za údaje odkazované zátvorkami.

Ak zadávate údaje do textového súboru a ak chcete mať vo vnútri jednej z hodnôt čiarku, napríklad "Clinton, Co., MO", potom musíte celú hodnotu umiestniť do dvojitých úvodzoviek a prvú dvojitú úvodzovku umiestniť hneď za predchádzajúcu čiarku. Napríklad:

    manželstvo, rodič1, rodič2, miesto
    m1, p1, p2, "Clinton, Co., MO"
    m2, p3, p4, "Havertown, PA"

Tabuľkový program to urobí automaticky za vás.

Tu je príklad tabuľky v LibreOffice, ale mal by fungovať akýkoľvek tabuľkový program.

![[_media/Gramps-csv-example1.csv-LibreOffice-Calc--example-60.png|Obrázok {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}}]] {{-}}

    ,,,,,,,,,
    , "Meno", "Priezvisko", "Volanie", "Pohlavie", "Predpona", "Prípona", "Titul", "Poznámka", "Grampsid"
    , "Douglas", "Test", "Doug", "muž", "Von", "Sr.", "Dr.", "Toto nesúvisí", "I0007"
    , "Laura", "Test",, "žena",,,,,

{{-}} Všimnite si, že údaje nemusia začínať v prvom stĺpci, ani v prvom riadku.

A tu sú výsledné údaje v gramatike:

![[_media/FamilyTree-example-imported-gramps-csv-example1.csv-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}}]]

{{-}}

### Príklad CSV s viacerými oblasťami

Tu je príklad textovej tabuľky CSV s viacerými oblasťami:

    Miesto, Názov, Názov, Typ
    [P0001], Michigan, Michigan, Štát
    L1, Kanada, Kanada, Krajina
    L2, USA, USA, Štát

    Meno, Priezvisko, Dátum narodenia, Miesto narodenia id
    John, Tester, 11.11.1965, L1
    Sally, Tester, 26.1.1973, L1

    Osoba, meno, priezvisko, dátum narodenia, miesto narodenia id
    p1, Tom, Smith, 22. januára 1970, [P0001]
    p2, Mary, Jones
    p3, Jonnie, Smith
    p5, James, Loucher
    p6, Penny, Armbruster
    [P0002], Tim, Sparklet

    Manželstvo, manžel, manželka
    m1, p1, p2
    m2, p5, p6

    Rodina, dieťa
    m1, p3
    m1, p6
    m2, [P0002]

Ak to vystrihnete a vložíte do súboru (alebo použijete [Import Grampletu](wiki:Addon:ImportGramplet)), môžete ho priamo importovať.

Dátumom môže byť akýkoľvek platný dátum programu Gramplet, vrátane dátumov vo formátoch ako "26 JAN 1973" alebo "26.1.1973".

Ak vytvoríte odkazy ako ID Gramps v hranatých zátvorkách, potom môžete odkazovať na ľudí, ktorí už sú v databáze, napríklad takto:

    Osoba, meno, priezvisko
    Joe's boy, Harry, Smith

    Rodina, Dieťa
    [F1524], joe's boy

    Manžel, manželka
    [I0123], [I0562]

    meno, priezvisko
    Timothy, Jones

    place, enclosed_by
    [P0001], [P0002]

Tento príklad by vytvoril a pridal Harryho Smitha k už existujúcej rodine v Gramps, rodina F1524.

Tento príklad by tiež zosobášil dve predtým existujúce osoby, I0123 a I0562.

Vytvorí sa tiež osoba s menom Timothy Jones, ktorá nie je s nikým príbuzná.

Nakoniec sa týmto spôsobom miesto P0001 uzavrie do miesta P0002.

. === Príklad CSV z tabuľky ===

![[_media/Gramps-csv-example3.ods-LibreOffice-Calc-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}}]]

Použitie programu Gramps [Example.gramps](wiki:Example.gramps) pre tento príklad. Deti už existujú v rodinnom strome. Do programu LibreOffice Calc tak môžete zadať celú generáciu (8 mien s dátumami sobášov).

Všimnite si, že ako referenčné názvy medzi oblasťami môžete použiť čísla alebo reťazce. V oblasti osôb som použil čísla 1 až 8. To uľahčilo odkazovanie na ne v druhej oblasti manželstiev. Manželstvá sú označené písmenami A až D.

Všimnite si tiež, že v tabuľke sú deti v tretej oblasti existujúcimi osobami v Gramps, ako je uvedené v zátvorkách okolo identifikátorov Gramps.

Uložením do formátu CSV a importom do programu Gramps sa vytvorí pravý stĺpec v strome.

![[_media/FamilyTree-example-imported-gramps-csv-example3.csv-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Uložením ako CSV a importom do programu Gramps sa v strome vytvorí stĺpec úplne vpravo (zvýraznený žltou farbou)]]. {{-}} Obsah súboru CSV `gen4-test.csv`

    ,,,
    ,,,
    "Osoba", "Meno", "Priezvisko",
    1, "Peter", "Blank",
    2, "Anna Maria", "Kiefer",
    3, "Georg", "Schmidt",
    4, "Barbara", "Goering",
    5, "Johann", "Kiefer",
    6, "Fides", "Federer",
    7, "Sebastian", "Schelli",
    8, "Magdelena", "Schlegel",
    ,,,
    ,,,
    "Manželstvo", "Manžel", "Manželka", "Dátum"
    "A",1,2, "28 jan 1712"
    "B",3,4, "4. mája 1732"
    "C",5,6,02/07/1930
    "D",7,8,17/08/1927
    ,,,
    "Rodina", "Dieťa",,
    "A","[I0104]",,
    "B","[I0105]",,
    "C","[I0972]",,
    "D","[I0973]",,

### Pozri tiež

- [Import (text) Gramplet](wiki:Addon:ImportGramplet) Doplnok tretej strany od Douga Blanka - interaktívna verzia [CSV Import](wiki:Gramps_{{man_version}}_Wiki_Manual_-_Manage_Family_Trees:_CSV_Import_and_Export)

[C](wiki:Category:Sk:Documentation) [CSV import/Export](wiki:Category:Gramps_Examples)
