---
title: Gramps 6.0 Wiki Manual - Command Line/sk
categories:
- Sk:Documentation
- Stub
managed: false
source: wiki-scrape
wiki_revid: 111213
wiki_fetched_at: '2026-05-30T20:02:33Z'
lang: sk
---

{{#vardefine:chapter\|C}} {{#vardefine:figure\|0}} Táto príloha poskytuje odkaz na možnosti príkazového riadka, ktoré sú k dispozícii pri spustení programu Gramps z terminálu.

## Spustenie programu Gramps cez príkazový riadok

Gramps sa zvyčajne spúšťa prostredníctvom grafického používateľského rozhrania (GUI) na [vašej platforme](wiki:Gramps_6.0_Wiki_Manual_-_Getting_started#Start_Gramps).

Program Gramps je možné spustiť aj pomocou rozhrania príkazového riadka (CLI). Použitie CLI môže

- vytvárať hlásenia, ktoré nie sú k dispozícii prostredníctvom grafického používateľského rozhrania,
- vytvárať zostavy, vykonávať konverzie atď. bez otvorenia okna a
- môže poskytnúť [extra informácie](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window#Seeing_all_the_error_messages) v prípade problémov.

V tejto časti používateľskej príručky je opísaný spôsob spustenia programu Gramps prostredníctvom CLI a funkcie, ktoré sú k dispozícii.

Spôsob spustenia programu Gramps prostredníctvom CLI závisí od operačného systému, ktorý používate.

Pre zjednodušenie opisu sú príklady použitia uvedené nižšie napísané z pohľadu spustenia programu Gramps v systéme Linux. Príklady by bolo potrebné zmeniť pre iné platformy.

### Linux

Oficiálne je podporovaná iba platforma Linux, pretože vývojári programu Gramps používajú a testujú zdrojový kód na tejto platforme a opravujú všetky problémy, ktoré vzniknú v dôsledku aktualizácií.

Za predpokladu, že ste pre svoju distribúciu Linuxu použili štandardného správcu balíkov (buď prostredníctvom CLI, alebo grafického rozhrania), spustíte Gramps prostredníctvom CLI zadaním

` gramps`

### MS Windows

MS Windows je platforma [podporovaná komunitou](wiki:Download/sk). Ak nainštalujete [Windows AIO](wiki:All_In_One_Gramps_Software_Bundle_for_Windows) GrampsAIO32 alebo GrampsAIO64 spustiteľný súbor, potom sa na plochu umiestni ikona a do ponuky "Štart" sa umiestni tiež.

Aký je najlepší spôsob, ako zistiť, aký príkaz zadať?

Spustenie programu Gramps z príkazového riadku (cmd.exe) závisí od toho, kde ste sa rozhodli program Gramps nainštalovať.

- Kliknite pravým tlačidlom myši na aplikáciu `GrampsAIO64 ``-console` alebo na príslušnú položku v ponuke Štart.
- Zapíšte si umiestnenie súboru (jeho adresár "Start in").
- Označte celý príkaz a skopírujte ho ().
- Z ponuky Štart spustite súbor cmd.exe.
- Zmeňte adresár na počiatočný adresár, ktorý ste si zapísali.
- Kliknite pravým tlačidlom myši a vyberte položku Vložiť.
- Stlačte .

Môže to byť napríklad:

` cd "\Program Files\GrampsAIO64"`  
` gramps`

Keď vám pokyny nižšie hovoria, aby ste niečo napísali po príkaze Start, stačí to napísať za posledný riadok, napr:

` cd "\Program Files\GrampsAIO64"`  
` gramps -L`

Existujú aj iné spôsoby inštalácie programu Gramps pre MS Windows, ale tie sú oveľa zložitejšie a nie sú tu opísané.

### MacOS

MacOS je platforma [podporovaná komunitou](wiki:Na_stiahnutie). Ak si stiahnete obraz disku MacOS (.dmg), potom jednoducho pretiahnete aplikáciu do priečinka aplikácií (alebo kamkoľvek inam, kde ju chcete uložiť) a spustíte Gramps dvojitým kliknutím na aplikáciu bežným spôsobom. Správca balíkov Homebrew[1](https://github.com/Homebrew) tiež umožňuje inštaláciu aplikácie do bežného priečinka Applications.

Ak chcete aplikáciu spustiť z príkazového riadka, musíte spustiť terminál, ktorý sa nachádza v priečinku Utilities hlavného priečinka Applications (/Applications/Utilities). Po otvorení okna terminálu zadajte na výzvu

`   /path/to/Gramps.app/Contents/MacOS/Gramps`

Ak ste nainštalovali Gramps do zložky Applications spolu s väčšinou ostatných aplikácií, ako je navrhnuté vyššie, bude to

`   /Applications/Gramps.app/Contents/MacOS/Gramps`

Spolu s tým môžete použiť ktorúkoľvek z možností príkazového riadka. Ak chcete napríklad získať podrobný zoznam všetkých databáz Family Tree vo vašom predvolenom priečinku Family Tree, použite

`   /Applications/Gramps.app/Contents/MacOS/Gramps -L`

Existujú aj iné spôsoby inštalácie programu Gramps pre systém MacOS, ale tie sú oveľa zložitejšie a nie sú tu opísané.

## Možnosti Pythonu

V príkladoch rôznych platforiem vyššie a tiež v príkazoch v rôznych súboroch môžete vidieť niektoré voľby za príkazom 'python', napríklad '-EO' v

` "python3 -EO ..\share\gramps\gramps.py -L`

V tomto prípade je dôležité rozlišovať medzi **možnosťami pythonu**:

` -EO`

a **možnosťami Gramps**, v tomto prípade

` -L`

**Možnosti pythonu**, s ktorými sa môžete stretnúť, sú:

- `-E` Ignorovať všetky premenné prostredia PYTHON\*, napr. `PYTHONPATH` a `PYTHONHOME`, ktoré môžu byť nastavené.
- `-O` Zapnite základné optimalizácie. Tým sa zmení prípona názvu skompilovaných súborov (bytecode) z `.pyc` na `.pyo`. Pozri tiež PYTHONOPTIMIZE.

Príznak `-O` optimalize má v programe Gramps niekoľko účinkov:

- Ak nie je zapnutá, v ponuke sa objaví ďalšia položka .
- Ak nie je zapnutá, vypíšu sa [informatívne logovacie správy](wiki:Logovanie_systému#So_ako_funguje_logovanie_v_gramoch_po_všetkom.3F).
- Ak nie je zapnutá, môže sa aktivovať [debugovacích hlásení](wiki:Ladenie_Gramps#Pridanie_debugovacích_hlásení).
- Ak nie je zapnutá, ďalšie funkcie sú dostupné v [Správca zásuvných modulov](wiki:Gramps_6.0_Wiki_Manual_-_Plugin_Manager/sk).

Možnosti **Gramps** sú opísané nižšie.

## Dostupné možnosti Gramps

Táto časť obsahuje referenčný zoznam všetkých možností príkazového riadka dostupných v programe Gramps. Ak chcete vedieť viac ako len zoznam možností, pozrite si ďalšie časti: [Operácie](#Operácie) a [Príklady](#Príklady). Nižšie uvedený súhrn sa vytlačí pomocou

` gramps -h`

alebo

` gramps --help`

    Použitie: gramps.py [OPTION...]
        --load-modules=MODULE1,MODULE2,...     Dynamické moduly na načítanie

    Možnosti nápovedy
        -?, --help Zobraziť túto nápovedu
        --usage Zobrazenie stručnej správy o použití

    Možnosti aplikácie
        -O, --open=FAMILY_TREE Otvoriť rodokmeň
        -U, --username=USERNAME Používateľské meno databázy
        -P, --password=PASSWORD Heslo databázy
        -C, --create=FAMILY_TREE Vytvoriť pri otvorení, ak je nový rodokmeň
        -i, --import=FILENAME Importovať súbor
        -e, --export=FILENAME Exportovať súbor
        -r, --remove=FAMILY_TREE_PATTERN Odstrániť zodpovedajúce rodinné stromy (použiť regulárne výrazy)
        -f, --format=FORMAT Určite formát rodokmeňa
        -a, --action=ACTION Určiť akciu
        -p, --options=OPTIONS_STRING Určiť možnosti
        -d, --debug=LOGGER_NAME Zapnúť protokoly ladenia
        -l [FAMILY_TREE_PATTERN...] Zoznam rodinných stromov
        -L [FAMILY_TREE_PATTERN...] Podrobný zoznam rodokmeňov
        -t [FAMILY_TREE_PATTERN...] Zoznam rodokmeňov, odlíšený v tabuľke
        -u, --force-unlock Vynútiť odomknutie rodokmeňa
        -s, --show Zobraziť konfiguračné nastavenia
        -c, --config=[config.setting[:value]]  Nastaviť konfiguračné nastavenie(-ia) a spustiť Gramps
        -y, --yes Nepýtať sa na potvrdenie nebezpečných akcií (len v režime bez GUI)
        -q, --quiet Potlačiť výstup indikácie priebehu (len v režime bez používateľského rozhrania)
        -v, --version Zobraziť verzie
        -S, --safe Spustiť Gramps v "bezpečnom režime
                                                                                        (dočasne použije predvolené nastavenia)
        -D, --default=[APXFE] Obnovenie predvolených nastavení;
                                      A - vymažú sa doplnky
                                      P - predvolené nastavenia
                                      X - vymažú sa knihy, správy a nastavenia nástrojov na predvolené
                                      F - filtre sa vymažú
                                      E - všetko je nastavené na predvolené alebo vymazané

Správa o použití je nasledovná:

` gramps --usage`

    Príklad použitia rozhrania príkazového riadka Gramps

    1. Import štyroch databáz (ktorých formáty možno určiť z ich názvov)
    a potom skontrolovať výslednú databázu na prítomnosť chýb, možno zadať:
    gramps -i file1.ged -i file2.gpkg -i ~/db3.gramps -i file4.wft -a tool -p name=check.

    2. Ak chcete explicitne špecifikovať formáty vo vyššie uvedenom príklade, pripojte názvy súborov s príslušnými možnosťami -f:
    gramps -i file1.ged -f gedcom -i file2.gpkg -f gramps-pkg -i ~/db3.gramps -f gramps-xml -i file4.wft -f wft -a tool -p name=check.

    3. Ak chcete zaznamenať databázu, ktorá je výsledkom všetkých importov, zadajte príznak -e
    (ak názov súboru neumožňuje programu Gramps odhadnúť formát, použite príznak -f):
    gramps -i file1.ged -i file2.gpkg -e ~/new-package -f gramps-pkg

    4. Ak chcete uložiť všetky chybové hlásenia vyššie uvedeného príkladu do súborov outfile a errfile, spustite:
    gramps -i file1.ged -i file2.dpkg -e ~/new-package -f gramps-pkg >outfile 2>errfile

    5. Import troch databáz a spustenie interaktívnej relácie Gramps s výsledkom:
    gramps -i file1.ged -i file2.gpkg -i ~/db3.gramps

    6. Otvorenie databázy a na základe týchto údajov vygenerovanie správy o časovej osi vo formáte PDF
    vložením výstupu do súboru my_timeline.pdf:
    gramps -O 'Family Tree 1' -a report -p name=timeline,off=pdf,of=my_timeline.pdf

    7. Generovanie súhrnu databázy:
    v prípade, že je to možné, môžete použiť príkaz: gramps -O 'Family Tree 1' -a report -p name=summary

    8. Výpis možností reportu
    Pomocou príkazu name=timeline,show=all zistíte všetky dostupné možnosti pre report časovej osi.
    Ak chcete zistiť podrobnosti o konkrétnej možnosti, použite show=option_name , napr. reťazec name=timeline,show=off.
    Ak sa chcete dozvedieť o dostupných názvoch zostavy, použite reťazec name=show.

    9. Ak chcete konvertovať rodokmeň za chodu do súboru .gramps xml:
    gramps -O 'Family Tree 1' -e output.gramps -f gramps-xml

    10. Ak chcete vygenerovať webovú stránku do iného lokálneho jazyka (v nemčine):
    LANGUAGE=de_DE; LANG=de_DE.UTF-8 gramps -O 'Family Tree 1' -a report -p name=navwebpage,target=/../de

    11. Nakoniec, ak chcete spustiť normálnu interaktívnu reláciu, zadajte:
    gramps

    Poznámka: Tieto príklady sú pre shell bash.
    Syntax sa môže líšiť pre iné shelly a pre Windows.

### Možnosti zoznamu

Vytlačiť zoznam známych rodokmeňov:

Sparse  

` -l, Zoznam rodokmeňov`

` gramps -l`

    Zoznam známych rodokmeňov v ceste k databáze

    /home/<~užívateľské meno>/.gramps/grampsdb/5a46c1c3 s názvom "Príklad Rodokmeňa"

{{-}}

Podrobné  

` -L, Podrobný zoznam rodokmeňov`

` gramps -L`

    Rodokmene Gramps:
    Rodokmeň "Príklad rodokmeňa":
          Databáza: SQLite
          Umiestnenie modulu databázy: /usr/lib/python3.6/sqlite3/__init__.py
          Verzia modulu databázy: 2.6.0
          Verzia databázy: 3.21.0
          Posledný prístup: 30/12/17 09:29:37
          Uzamknuté?: Nepravdivé
          Počet citácií: 2854
          Počet udalostí: 3432
          Počet rodín: 762
          Počet médií: 7
          Počet poznámok: 19
          Počet ľudí: 2157
          Počet miest: 1294
          Počet úložísk: 1294 3
          Počet zdrojov: 4
          Počet značiek: 4: 2
          Cesta: /home/<~username>/.gramps/grampsdb/5a46c1c3
          Verzia schémy: 18.0.0

{{-}}

### Možnosti verzie

` -v alebo --version vypíše verziu programu Gramps a závislostí,`  
`           informácie o nastaveniach prostredia a cestách k pythonu a systému`

` gramps -v`

    Nastavenia Gramps:
    ----------------
      python : 3.7.5
      gramps : 6.0.1
      gtk++ : 3.24.12
      pygobject : 3.34.0
      pango : 1.42.3
      cairo : 1.16.0
      pycairo : 1.16.2
      osmgpsmap : 1.0
      GExiv2 : 0.10
      ICU : 63.1
      PyICU : 2.2
      o.s. : linux
      kernel : 5.3.0-24-generic

    Nastavenia prostredia:
    ---------------------
      LANG : en_GB.UTF-8
      LANGUAGE : en_GB:en
      GRAMPSI18N: nie je nastavené
      GRAMPSHOME: nie je nastavené
      GRAMPSDIR : nie je nastavený
      PYTHONPATH:
            /usr/lib/python3/dist-packages/gramps
            /usr/bin
            /usr/lib/python37.zip
            /usr/lib/python3.7
            /usr/lib/python3.7/lib-dynload
            /usr/local/lib/python3.7/dist-packages
            /usr/lib/python3/dist-packages

    Závislosti, ktoré nie sú súčasťou Pythonu:
    ------------------------
      Graphviz : 2.40
      Ghostscr. : 9.27

    Systémová premenná env PATH:
    -------------------------
              /usr/local/sbin
              /usr/local/bin
              /usr/sbin
              /usr/bin
              /sbin
              /bin
              /usr/games
              /usr/local/games
              /snap/bin

    Databázy:
    -------------------------
      bsddb :
              verzia : 6.2.6
              db verzia : 5.3.28
              umiestnenie : /usr/lib/python3/dist-packages/bsddb3/__init__.py
      sqlite3 :
              verzia : 3.29.0
              py verzia : 2.6.0
              umiestnenie : /usr/lib/python3.7/sqlite3/__init__.py

{{-}}

### Možnosti formátu

Formát ľubovoľného súboru určeného na otvorenie, import alebo export možno určiť pomocou možnosti

    -f format

. Prípustné hodnoty *`format`* sú uvedené nižšie.

#### Úplná podpora rodokmeňa

Tieto formáty obsahujú všetky vaše údaje, ktoré sa nachádzajú v rodokmeni.

- **gramps** - formát Gramps XML: Tento formát je k dispozícii na import a export. Ak nie je uvedený, možno ho odhadnúť, ak názov súboru končí na .gramps
- **gpkg** - Formát XML balíka Gramps: Tento formát je k dispozícii na import a export. Ak nie je uvedený, možno ho odhadnúť, ak názov súboru končí na .gpkg. Tým sa vytvorí balík zip s vašimi údajmi vo formáte xml a so všetkými zahrnutými mediálnymi súbormi
- **grdb** - databáza pred verziou Gramps 3.x: Tento formát je k dispozícii na import na podporu starého formátu súborov Gramps. Všetko v súbore grdb sa importuje. Ak nie je zadaný, možno ho odhadnúť, ak názov súboru končí na .grdb
- **burn** - Vypálenie iso v prostredí GNOME: export, k dispozícii len v prostredí GNOME, kde existuje protokol burn

#### Znížená podpora rodokmeňa

Tieto formáty obsahujú väčšinu, ale nie všetky údaje, ktoré možno vytvoriť v programe Gramps

- **ged** - formát GEDCOM: Tento formát je k dispozícii na import a export. Ak nie je uvedený, možno ho odhadnúť, ak názov súboru končí na .ged
- **gw** - súbor GeneWeb: Tento formát je k dispozícii na import a export. Ak nie je uvedený, možno ho odhadnúť, ak názov súboru končí na .gw

#### Podskupina vašich údajov

Tieto formáty obsahujú špecifickú podmnožinu vašich údajov

- **csv** - hodnoty oddelené čiarkou: Tento formát je k dispozícii na import a export. Dávajte však pozor, import musí byť v podobe hodnôt vytvorených funkciou exportu. Vo výstupe je obsiahnutá len časť vašich údajov.
- **vcf** - formát VCard: import a export
- **vcs** - formát VCalandar: export
- **def** - starý formát Pro-Gen: import
- **wft** - webový rodokmeň: Tento formát je k dispozícii len na export. Ak nie je uvedený, možno ho odhadnúť, ak názov súboru končí na .wft

### Možnosti otvorenia

Môžete otvoriť rodokmeň alebo môžete *otvoriť* súbor jeho importovaním do prázdneho rodokmeňa.

Ak chcete, aby to program Gramps zvládol automaticky, stačí zadať rodokmeň alebo názov súboru, ktorý chcete otvoriť:

` python gramps.py 'My Fam Tree'`  
` python gramps.py JohnDoe.ged`

Prvý príkaz otvorí rodokmeň, druhý importuje GEDCOM do prázdneho rodokmeňa.

Okrem toho môžete programu Gramps odovzdať názov rodokmeňa, ktorý sa má otvoriť:

- použite túto možnosť : `-O famtree` alebo `--open=famtree`

`-O`, Otvoriť rodokmeň. Toto je možné vykonať aj jednoduchým zadaním názvu (mena alebo adresára databázy)

Príklady:

` python gramps.py 'Family Tree 1'`  
` python gramps.py /home/cristina/.gramps/grampsdb/47320f3d`  
` python gramps.py -O 'Family Tree 1'`  
` python gramps.py -O /home/cristina/.gramps/grampsdb/47320f3d`

### Možnosti importu

Súbory určené na import môžete určiť pomocou možnosti `-i meno súboru` alebo `--import=meno súboru`. Formát možno špecifikovať pomocou možnosti `-f format` alebo `--format=format`, ktorá nasleduje hneď za *menom súboru* . Ak nie je zadaný, pokus o odhad sa uskutoční na základe *názvu súboru*.

Príklad:

`     python gramps.py -i 'Family Tree 1' -i 'Family Tree 2'`  
`     python gramps.py -i test.grdb -i data.gramps`

Ak je zadaných viac vstupných súborov, každému musí predchádzať príznak `-i`. Súbory sa importujú v uvedenom poradí, t. j. `-i file1 -i file2` a `-i file2 -i file1` môžu vo výslednej databáze Gramps vytvoriť rôzne ID.

### Možnosti exportu

Súbory určené na export možno špecifikovať pomocou možnosti `-e filename (názov súboru)` alebo `--export=filename (názov súboru)`. Formát možno špecifikovať pomocou možnosti `-f` bezprostredne nasledujúcej za *názvom súboru* . Ak nie je zadaný, pokus o odhad sa uskutoční na základe parametra *meno súboru* . V prípade formátu iso je *meno súboru* vlastne názov adresára, do ktorého sa databáza Gramps zapíše. Pre gramps-xml, gpkg, gedcom, wft, geneweb a gramps-pkg je *meno súboru* názov výsledného súboru.

-e, exportuje rodokmeň v požadovanom formáte. Nie je možné exportovať do rodokmeňa.

Príklad:

`   python gramps.py -i 'Family Tree 1' -i test.grdb -f grdb -e mergedDB.gramps`

Všimnite si, že vyššie uvedené nezmení 'Rodokmeň 1', pretože všetko sa deje prostredníctvom dočasnej databázy, zatiaľ čo:

`   python gramps.py -O 'Family Tree 1' -i test.grdb -f grdb -e mergedDB.gramps`

importuje test.grdb do Family Tree 1 a potom exportuje do súboru !

.

Ak je zadaných viac ako jeden výstupný súbor, každému musí predchádzať príznak `-e`. Súbory sa zapisujú jeden po druhom v uvedenom poradí.

### Možnosti akcie

Akciu, ktorá sa má vykonať na importovaných údajoch, možno určiť pomocou možnosti `-a action` alebo `--action=action`. Vykoná sa po úspešnom dokončení všetkých importov.

Nasledujúce akcie zostávajú nezmenené:

- *report*': Táto akcia umožňuje vytvárať správy z príkazového riadka.

<!-- -->

- *tool*': Táto akcia umožňuje spustiť nástroj z príkazového riadka.

Reporty a nástroje majú vo všeobecnosti mnoho vlastných možností, preto by za týmito akciami mal nasledovať reťazec možností report/tool. Reťazec sa zadáva pomocou voľby `-p option_string` alebo `--options=option_string`.

Akcie dostupné v starších verziách programu Gramps, ktoré boli v programe Gramps 3.3 premiestnené, sú:

- *summary**: Táto akcia bola rovnaká ako . V programe Gramps 3.3 bola nahradená (alebo premenovaná na)**-a report -p name=summary*'.

<!-- -->

- *check**: Táto akcia bola rovnaká ako . V programe Gramps 3.3 bola nahradená (alebo premenovaná na)**-a tool -p name=check*'.

#### možnosť akcie hlásenia

Väčšinu zostáv môžete vytvárať z príkazového riadka pomocou akcie report.

Príklad:

` gramps -O "Family Tree 1" -a report -p "name=family_group,style=default,off=html,of=test.html"`

Tu môžete zadať štýl css, ktorý sa má použiť s možnosťou css:

` V tomto prípade môžete použiť štýly: gramps -O "Family Tree 1" -a report -p "name=family_group,style=default,off=html,of=test.html,css=Web_Nebraska.css"`

alebo bez css vo výstupe html:

` gramps -O "Family Tree 1" -a report -p "name=family_group,style=default,off=html,of=test.html,css="`

Väčšina možností zostavy je špecifická pre každú zostavu. Existujú však niektoré spoločné možnosti.

- `name=názov_správy`: Táto povinná možnosť určuje, ktorá správa sa bude generovať.

- `of=`: názov výstupného súboru a voliteľný cieľový priečinok/adresár napr: `of="C:\Users\`<užívateľské meno>`\Desktop\FamilyTree.odt"`
- `off=`: výstupný formát. Ide o rozšírenie, ktoré výstupný formát sprístupňuje, napr. pdf, html, doc, ...
- `style=`: v prípade textových správ súbor štýlov, ktorý sa má použiť. Predvolená hodnota je 'default'.
- `show=all`: Zobrazí zoznam názvov všetkých možností dostupných pre danú zostavu.
- `show=option_name`: Vypíše popis funkcie, ktorú poskytuje option_name, ako aj to, aké sú prípustné typy a hodnoty pre túto možnosť.

Ak sa teda chcete naučiť používať zostavu, vykonajte napr:

` gramps -O "Rodokmeň 1" -a report -p "name=rodinná_skupina,show=all"`

Ak je zadaná viac ako jedna výstupná akcia, každej z nich musí predchádzať príznak `-a`. Akcie sa vykonávajú jedna po druhej v uvedenom poradí.

V príkazovom riadku sa takéto zoznamy musia vždy začínať ľavou hranatou zátvorkou <kód>\[</kód> a musia sa vždy končiť pravou hranatou zátvorkou <kód>\]</kód>, ale keďže takéto hranaté zátvorky sú pre "shell" zvyčajne "špeciálne" (znamenajú niečo pre interpret príkazu ktorému zadávate príkaz), musíte ich "escapovať", aby ich shell ignoroval.

Podrobnosti sa líšia podľa jednotlivých shellov, ale (v Linuxe/UNIXe) zvyčajne môžete pred takúto hranatú zátvorku umiestniť spätné lomítko <kód>\\</kód> alebo okolo hranatej zátvorky umiestniť úvodzovky, zvyčajne buď "jednoduché", alebo "dvojité".

Správa Hourglass Graph umožňuje umiestniť "poznámku" na začiatok správy a takáto "poznámka" je príkladom možnosti "zoznam". Tu je uvedený príklad:

` gramps -O "Family Tree 1" -a report -p name=hourglass_graph,note='[line one,line two]'`

ktorý ukazuje, že vo vnútri takéhoto zoznamu sa rôzne riadky oddeľujú čiarkami a že medzery sú prípustné, pretože úvodzovky sú tam už pre hranaté zátvorky.

Ak však chcete mať vo vnútri správy čiarku, musíte Grampsu nejako povedať, že čiarka nie je tá, ktorá oddeľuje riadky. Urobíte to tak, že riadok s čiarkou uzavriete do úvodzoviek (jednoduchých alebo dvojitých).

Ak však už používate sadu úvodzoviek (na uzavretie hranatých zátvoriek), musíte použiť iný typ na uzavretie riadok s čiarkou. Tu je príklad:

` gramps -O "Family Tree 1" -a report -p name=hourglass_graph,note="['line one, also line one','line two, also line two']"`

Do zoznamu je možné zahrnúť ľubovoľný znak, ale podrobnosti presahujú rámec tohto úvodu do príkazového riadka programu Gramps.

Budete musieť poznať presné metódy, ktoré sú k dispozícii vo vašom konkrétnom interprete príkazového shellu, aby ste mohli zahrnúť znak, ktorý je "špeciálny" pre váš shell alebo "špeciálny" pre Gramps (ako napríklad čiarka vo vyššie uvedenom príklade), ale vo všeobecnosti ho budete musieť "escape" dvakrát, raz pre váš shell a raz pre Gramps, pretože nechcete, aby si váš shell myslel, že je to nejaká inštrukcia, ktorej by mal venovať pozornosť, a nechcete, aby si to myslel aj Gramps.

#### možnosť akcie nástroja

Väčšinu nástrojov môžete spustiť z príkazového riadka pomocou akcie 'tool'. Ak chcete zistiť, ktoré to sú, povedzte:

` gramps -O "Family Tree 1" -a tool -p show=all`

Ak chcete zobraziť dostupné možnosti nástroja, napríklad nástroja "verify":

` gramps -O "Family Tree 1" -a tool -p name=verify,show=all`

Spustenie nástroja, napríklad nástroja "verify":

` gramps -O "Family Tree 1" -a tool -p name=verify`

#### book action option

Knihy môžete spúšťať z príkazového riadka pomocou akcie 'book'. Ak chcete zistiť, ktoré to sú, povedzte:

` gramps -O "Family Tree 1" -a book`

Ak chcete zobraziť dostupné možnosti knihy, napríklad knihu s názvom "mybook":

` gramps -O "Family Tree 1" -a book -p name=mybook,show=all`

Spustenie knihy, napríklad knihy s názvom "mybook":

` gramps -O "Family Tree 1" -a book -p name=mybook`

### Možnosť vynúteného odomknutia

- `-u`: môžete rozšíriť príznak `-O` o `-u`, aby ste vynútili odomknutie zamknutej rodiny. To umožňuje obnoviť z príkazového riadku haváriu, ktorá zanechala rodokmeň (databázu) zamknutý.

Príklad (na odomknutie databázy "Rodokmeň 1"): `gramps -O "Family Tree 1" -a report -u > /dev/null`

Pozri tiež:

- [Správa rodinných stromov: Odomknutie rodinného stromu](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees/sk#Odomknutie_rodinného_stromu)

### Možnosť konfigurácie (config)

Keď sú nastavené všetky konfiguračné premenné, program Gramps sa spustí s týmito novými hodnotami.

Tieto možnosti môžu mať tri podoby: }

1\) Pozrite si všetky konfiguračné hodnoty  
`-s` alebo `--show`

  
Napr:

` gramps --show`

    Nastavenia konfigurácie gramps z /home/<~užívateľské meno>/.gramps/gramps50/gramps.ini:
    export.proxy-order=[["privacy", 0], ["living", 0], ["person", 0], ["note", 0], ["reference", 0]]

    database.compress-backup=True
    database.backend='bsddb'
    database.backup-path='/home/<~username>'
    database.port=''
    database.autobackup=0
    database.path='/home/<~username>/.gramps/grampsdb'
    database.host=''
    database.backup-on-exit=True

    geography.lock=False
    ....

{{-}}

2\) Zobraziť jednu konfiguračnú hodnotu  
`--config=database.path` alebo `-c database.path`

  
Napr:

` gramps --config=database.path`

    Aktuálne nastavenie konfigurácie Gramps: database.path:'/home/<~username>/.gramps/grampsdb'

3\) Nastavte hodnotu: `--config=behavior.database-path:'/media/mydb'` alebo `-c behavior.database-path:'/media/mydb'`  
Príklad:

3.1) Nastavte hodnotu na predvolenú hodnotu: `--config=behavior.database-path:DEFAULT` alebo `-c behavior.database-path:DEFAULT`  
Napr:

3.2) Nastavte viac ako jednu hodnotu: `--config=behavior.use-tips:False --config=behavior.autoload:True` alebo `-c behavior.use-tips:False -c behavior.autoload:True`  
Príklad:

### Bezpečný režim

`gramps -S` alebo `gramps --safe`

Tento CLI príkaz spustí Gramps, ako keby nikdy predtým nebol nainštalovaný. V tomto režime je možné stále načítať všetky predchádzajúce rodokmene, pokiaľ boli uložené v predvolenom priečinku. Všetky ostatné nastavenia, filtre, knihy, doplnky atď. sa buď vymažú, alebo sa vrátia na svoje predvolené hodnoty. Môžu sa použiť ďalšie príkazy CLI, alebo ak žiadne nie sú, Gramps spustí grafické rozhranie. Nič okrem skutočných údajov rodokmeňa sa neukladá.

Všimnite si, že toto sa zvyčajne používa na zistenie, či sa Gramps správa lepšie, keď je spustený ako pri úplne "čistej" inštalácii. NIE JE to trvalé (ak to chcete, pozrite si [predvolené nastavenia](#Predvolené_nastavenia) nižšie), ak po použití tohto príkazu spustíte Gramps normálne, všetky vaše predchádzajúce nastavenia atď. zostanú zachované.

V skutočnosti to funguje tak, že priečinok, ktorý Gramps používa na ukladanie svojich používateľských údajov (okrem rodokmeňov), sa nastaví do dočasného adresára, ktorý sa po zatvorení programu Gramps vymaže.

### Predvolené nastavenia

`gramps -D E` alebo `gramps --default=E`

Tento príkaz CLI spôsobí, že program Gramps vymaže alebo vráti na predvolené nastavenia požadované nastavenia. Databázy rodokmeňov sa NEvymažú ani neodstránia. Podpríkazy (nahraďte 'E' z vyššie uvedeného príkazového riadka jedným alebo viacerými príkazmi podpríkazov) sú:

- <kód>A</kód> Vymažú sa doplnky. Všetky nainštalované doplnky sa odstránia spolu s ich nastaveniami.
- `F` Filtre sú vymazané. Odstránia sa všetky vlastné filtre.
- `P` Predvoľby sa vrátia na svoje predvolené hodnoty.
- `X` Knihy sú vymazané, nastavenia zostáv a nástrojov sú vrátené na svoje predvolené hodnoty.
- `Z` Staré súbory '.zip' z aktualizácií verzií rodokmeňa sa odstránia.
- `E` Všetko okrem aktuálnych údajov rodokmeňa sa vráti na predvolené nastavenia. Tým sa vykoná všetko vyššie uvedené, ako aj niekoľko ďalších položiek; odstránia sa miniatúry, mapy a používateľské CSS (používané vo webových správach).

Napríklad:

` gramps -D AP`

spôsobí, že program Gramps odstráni všetky doplnky a obnoví Predvoľby na ich predvolené hodnoty.

## Operácia

Ak prvý argument v príkazovom riadku nezačína pomlčkou (t. j. bez príznaku), Gramps sa pokúsi otvoriť súbor s názvom uvedeným v prvom argumente a začne interaktívnu reláciu, pričom ostatné argumenty príkazového riadku ignoruje.

Ak je zadaný príznak <kód>-O</kód>, Gramps sa pokúsi otvoriť zadaný názov súboru a potom bude pracovať s týmito údajmi podľa pokynov ďalších parametrov príkazového riadka.

S príznakom `-O` alebo bez neho môže byť v príkazovom riadku ďalej špecifikovaných viac importov, exportov a akcií pomocou príznakov `-i` , `-e` a `-a`.

Na poradí volieb `-i` , `-e` alebo `-a` vzhľadom na každú z nich nezáleží. Skutočné poradie vykonávania je vždy: všetky importy (ak existujú) -\> všetky exporty (ak existujú) -\> všetky akcie (ak existujú).

Ak nie je zadaná žiadna voľba `-O` alebo `-i`, Gramps spustí svoje hlavné okno a začne obvyklú interaktívnu reláciu s prázdnou databázou, pretože aj tak nie sú žiadne údaje na spracovanie. (Pokiaľ ste už nevyjadrili "preferenciu", aby začal s poslednou použitou databázou.)

Ak nie sú zadané žiadne voľby `-e` alebo `-a`, Gramps spustí svoje hlavné okno a začne obvyklú interaktívnu reláciu s databázou, ktorá vznikla otvorením, a so všetkými importmi (ak existujú). Táto databáza sa nachádza v adresári pod adresárom *`~/.gramps/grampsdb/`*.

Všetky chyby, na ktoré sa počas importu, exportu alebo akcie narazí, sa vypíšu buď na stdout (ak ide o výnimky, ktoré Gramps spracuje), alebo na stderr (ak sa nespracujú). Na ukladanie správ a chýb do súborov použite obvyklé presmerovania shellu na stdout a stderr.

## Príklady

- Ak chcete importovať štyri databázy (ktorých formáty možno určiť z ich názvov) a potom skontrolovať výslednú databázu na chyby, môžete zadať:

`gramps -i file1.ged -i file2.gpkg -i ~/db3.gramps -i file4.wft -a check`

- Ak chcete explicitne špecifikovať formáty vo vyššie uvedenom príklade, pripojte názvy súborov s príslušnými možnosťami -f:

  
`gramps -i file1.ged -f gedcom -i file2.gpkg -f gramps-pkg -i ~/db3.gramps -f gramps-xml -i file4.wft -f wft -a check`

- Ak chcete zaznamenať databázu, ktorá je výsledkom všetkých importov, zadajte príznak -e (použite -f, ak názov súboru neumožňuje Gramps odhadnúť formát):

`gramps -i file1.ged -i file2.gpkg -e ~/new-package -f gramps-pkg`

- Ak chcete uložiť všetky chybové hlásenia vyššie uvedeného príkladu do súborov outfile a errfile, spustite:

`gramps -i file1.ged -i file2.dpkg -e ~/new-package -f gramps-pkg >outfile 2>errfile`

- Na import troch databáz a spustenie interaktívnej relácie Gramps s výsledkom:

`gramps -i file1.ged -i file2.gpkg -i ~/db3.gramps`

- Otvoriť databázu a na základe týchto údajov vygenerovať správu o časovej osi vo formáte PDF, pričom výstup vložíte do súboru my_timeline.pdf:

`gramps -O 'Family Tree 1' -a report -p name=timeline,off=pdf,of=my_timeline.pdf`

- Na konverziu databázy bsddb za chodu do súboru .gramps xml:

`gramps -O 'Family Tree 1' -e output.gramps -f gramps-xml`

- Ak chcete vygenerovať webovú lokalitu do iného lokálneho jazyka (v nemčine)::

de_DE; LANG=de_DE.UTF-8 gramps -O 'Family Tree 1' -a report -p name=navwebpage,target=/../de </code>

- Nakoniec na spustenie normálnej interaktívnej relácie zadajte:

`gramps`

## Premenné prostredia

### GRAMPSHOME

- **GRAMPSHOME** - ak je nastavené, [prepíše predvolenú cestu](wiki:Gramps_and_Windows#Nastavenie_konfiguračnej_cesty) k profilu umožňujúcemu používateľovi používať externý sieťový disk na ukladanie údajov a všetkých nastavení. Pre technicky pokročilých používateľov, ktorí používajú viacero verzií programu Gramps, je nastavenie iného \$GRAMPSHOME spôsobom, ako zabrániť vzájomnému ovplyvňovaniu rôznych verzií programu Gramps [User Directory](wiki:Gramps_Glossary#user_directory). Môže sa použiť aj na konfiguráciu programu Gramps na [spustiť z prenosného disku](wiki:Spustenie_Gramps_z_prenosného_pohonu) alebo na prípravu na [ručnú inštaláciu](wiki:Inštalácia). Cesta sa môže použiť aj na konfiguráciu cesty k [separate test Tree](wiki:Gramps_for_Windows_with_MSYS2#Keep_your_GRAMPSHOME_separate) alebo [development Tree](wiki:Getting_started_with_Gramps_development).

Napríklad

    GRAMPSHOME=$HOME/familytrees/paternal

### LANG, LANGUAGE, LC_MESSAGE, LC_TIME

- **LANG**, **LANGUAGE**, **LC_MESSAGES** a **LC_TIME** - Gramps ich používa na určenie, ktorý jazykový súbor (jazykové súbory) sa má načítať. Všeobecné informácie o **LANG**, **LC_MESSAGES** a **LC_TIME*nájdete v locale(1). Všimnite si, že okrem nastavenia formátov dátumov (ktoré sú v programe Gramps prepísané nastaveniami predvolieb) nastavuje **LC_TIME** aj jazyk používaný pre slová v dátumoch, ako sú názvy mesiacov a dní a*v kontexte dátumov*slová ako*o*,*medzi*a*pred*. **LANGUAGE** je čiarou oddelený zoznam kódov jazykov (*nie lokálnych jazykov'', hoci niektoré jazyky ako pt_BR alebo cn_TW sú regionálnymi variantmi), ktorý nastavuje zoznam požadovaných prekladov zoradených podľa preferencií. Prekoná**LANG**, ale nie**LC_MESSAGES**alebo**LC_TIME'''.

### GRAMPSI18N

- [$GRAMPSI18N (pre vaše locale)](wiki:Preklad_Gramps#.24GRAMPSI18N_.28for_your_locale.29) - LANG predpokladá, že preklady Gramps sú nainštalované globálne. Ak to tak nie je, musíte [uviesť adresár Gramps](wiki:Translating_Gramps#.24GRAMPSI18N_.28for_your_locale.29), kde sa budú preklady nachádzať. To môžete použiť na dočasnú [zmenu jazyka generovaných zostáv](wiki:Howto:Change_the_language_of_reports).

Preklad sa volá `gramps.mo`, v Linuxe ho nájdete príkazom locate. Ak máte napríklad švédčinu v adresári `/home/me/gramps/mo/sv/gramps.mo`, môžete tam Gramps nasmerovať pomocou:

` GRAMPSI18N=/home/me/gramps/mo LC_ALL=C.UTF-8 LANG="sv" python3 gramps`

### GRAMPSDIR

- Premenná prostredia GRAMPSDIR je cesta k adresáru [Gramps](wiki:Preklad_Gramps#gramps.sh).

### GRAMPS_RESOURCES

- Premenná prostredia GRAMPS_RESOURCES je cesta k zostaveným súborom zdrojov programu Gramps. Mali by ste ju zmeniť len vtedy, ak používate Gramps zo zdrojového kódu alebo vlastného prostredia. Indikátorom, že je potrebné nastaviť túto premennú, je, ak sa zobrazí jedna z nasledujúcich chýb:
  - *Chyba kódovania pri analyzovaní cesty k zdrojom*
  - *Nepodarilo sa otvoriť súbor so zdrojmi*
  - *Cesta k zdroju {invalid/path/to/resources} je neplatná*
  - *Nie je možné určiť cestu k zdroju*

Príklad [použitia](wiki:Linux:Build_from_source#Running_from_a_tarball_release):

` GRAMPS_RESOURCES=/home/username/gramps/branches/maintenance/gramps51/build/lib.linux-x86_64-2.7/ PYTHONPATH=$GRAMPS_RESOURCES:$PYTHONPATH ./gramps`

{{-}}

[Category:Sk:Documentation](wiki:Category:Sk:Documentation)
