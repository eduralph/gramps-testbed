---
title: Gramps 6.0 Wiki Manual - Settings/sk
categories:
- Sk:Documentation
- Stub
managed: false
source: wiki-scrape
wiki_revid: 125637
wiki_fetched_at: '2026-05-30T20:23:59Z'
lang: sk
---

{{#vardefine:chapter\|15}} {{#vardefine:figure\|0}} Táto časť sa zaoberá rôznymi nastaveniami, ktoré môžete v programe Gramps spravovať.

## Predvoľby

![[_media/EditPreferencesTabsOnly-overview-51.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Prehľad všetkých záložiek Predvoľby]]

Väčšina nastavení v programe Gramps sa konfiguruje v dialógovom okne . Ak ho chcete vyvolať, vyberte ponuku }.

Na záložkách v hornej časti sa zobrazujú dostupné kategórie možností nasledovne:

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

Taktiež *iné* dodatočné záložky sa môžu zobraziť z [doplnkov](wiki:6.0_Addons#Addon_List), ktoré môžete mať nainštalované. {{-}}

### Všeobecné

![[_media/EditPreferences-General-tab-example-51.png|Right|thumb|450px|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Všeobecné predvoľby (Linux)]]

Táto záložka obsahuje dve časti obsahujúce predvoľby dôležité pre všeobecné fungovanie programu. Sekcie a možnosti sú nasledovné:

#### Všeobecné nastavenia programu Gramps

- \[ \]: Táto voľba začiarķovacieho políčka ovplyvňuje import [údajov GEDCOM](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees#GEDCOM_import). Ak je táto možnosť nastavená, každá importovaná položka bude obsahovať [zdrojový](wiki:Gramps_Glossary#source) odkaz na importovaný súbor. '''Poznámka - Pridanie predvoleného zdroja môže výrazne spomaliť importovanie údajov GEDCOM.

- \[ \]: (Predvolené: `Importované %Y/%m/%d %H:%M:%S` ) **Poznámka - Pridanie [Tag](wiki:Gramps_Glossary#tag) pri importe môže výrazne spomaliť import vašich údajov.**

- \[ \]: Táto možnosť začiarkovacieho políčka ovláda zapnutie a vypnutie kontroly pravopisu pre poznámky. Aby sa táto funkcia prejavila, musí byť načítaný balík **gtkspell**.

-   
  Táto možnosť zaškrtávacieho políčka ovláda zapnutie a vypnutie dialógového okna pri spustení.

-   
  Táto možnosť začiarkovacieho políčka ovláda zapnutie a vypnutie zobrazenia posledného [Pohľadu](wiki:Gramps_Glossary#view). Povolením sa zobrazí pohľad, v ktorom ste naposledy zastavili program.

- Môžete zadať počet generácií použitých na určenie vzťahov. Predvolená hodnota je **`15`**.

- Tu môžete vyplniť základnú cestu pre objekty médií. Výberom tlačidla sa zobrazí editor , v ktorom môžete vyplniť požadovanú cestu.

#### Správa doplnkov tretích strán

- Vyberte frekvenciu, s akou má program Gramps kontrolovať aktualizácie [Doplnky](wiki:6.0_Doplnky#Inštalácia_doplnkov_v_Gramps). Predvolené nastavenie: *Nikdy*

- Predvolené: *Len nové doplnky*

- Predvolené nastavenie: [`https://raw.githubusercontent.com/gramps-project/addons/master/gramps51`](https://raw.githubusercontent.com/gramps-project/addons/master/gramps51)

-   
  Začiarkovacie políčko je predvolene začiarknuté

-   
  Tlačidlo na vynútenie kontroly doplnkov, ak sú doplnky k dispozícii, zobrazí sa okno, v ktorom si ich vyberiete a nainštalujete.

{{-}}

###### Dostupné aktualizácie Gramps pre doplnky

![[_media/AvailableGrampsUpdatesforAddons-example-listing-60.png|Right|thumb|550px| "Available Gramps Updates for Addons" okno zobrazujúce výstup príkladu zoznamu pre Gramps 6.0]]

V okne sa vám zobrazí zoznam rozdelený podľa **Typu**, ktorý si môžete zobraziť výberom stĺpca "Vybrať" rozbaľte každý "Typ".

- Potom môžete začiarknuť políčko tých doplnkov, ktoré chcete nainštalovať.
- Potom vyberte tlačidlo , aby ste si tieto doplnky stiahli z *internetu*.
- Po stiahnutí z dialógového okna vyberte tlačidlo .
- V dialógovom okne vyberte tlačidlo .
- Ak chcete používať doplnky, musíte a reštartovať program Gramps.

{{-}}

#### Dialógové okno Tip dňa

![[_media/TipOfTheDay-dialog--example-keeping-good-records-50.png|Right|thumb|400px|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Dialógové okno Tip dňa]]

Po zapnutí v záložke dialógové okno zobrazuje užitočné rady.

K dispozícii sú nasledujúce možnosti:

-  (políčko je predvolene začiarknuté - po zapnutí) - zrušením začiarknutia sa ďalšie tipy nebudú zobrazovať.

- \- posunie na ďalšiu radu.

- \- ukončí túto reláciu, kým sa program Gramps znovu nespustí.

{{-}}

### Rodinný strom

![[_media/EditPreferences-FamilyTree-tab-example-51.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Ponuka: }}  - "Rodokmeň" - karta - príklad - predvolené nastavenia Ubuntu]]

Táto karta obsahuje predvoľby relevantné pre **Nastavenia databázy rodokmeňa a správu záloh**.

- \-

  - *[BSDDB](wiki:Gramps_Glossary#bsddb)* - Starší backend databázy. Nahradená vo verzii Gramps 6.0.
  - *'[SQLite](wiki:Gramps_Glossary#sqlite)* (*default*) - [DB-API Database Backend](wiki:DB-API_Database_Backend) - [DB-API Database Backend](wiki:DB-API_Database_Backend)
  - ... Ak sú nainštalované ďalšie doplnky databázových backendov, pridajú sa do zoznamu <abbr title="exempli gratia - latinská fráza znamenajúca 'napríklad'">napr. </abbr>: [PostgreSQL](wiki:Addon:PostgreSQL) backend

- \- Adresa servera alebo IP adresa iného počítača, na ktorom sa nachádza databáza.

- \- Číslo portu na prístup k databáze Host

- Ak nemáte konkrétny dôvod na zmenu, zostaňte pri predvolenej ceste. Táto cesta bude v rámci [User Directory](wiki:Gramps_6.0_Wiki_Manual_-_User_Directory) operačných systémov miestneho počítača.  
  Východisková cesta, kde sú uložené databázy, je:

  
  
`/home/`<small>***<username>***</small>`/.gramps/grampsdb`'' <small>(Linux a macOS)</small>

`C:\Users\`<small>***\<~username\>***</small>`\AppData\Roaming\gramps\grampsdb`''' <small>(Windows)</small>

-   
  Začiarknutím tejto možnosti sa pri spustení načíta posledná použitá databáza. Obchádza dialógové okno **Spravovať rodokmene**.

- } - Umiestnenie, do ktorého sa majú uložiť záložné archívne súbory programu Gramps.

- \- Výber tejto možnosti spôsobí zálohovanie vášho rodokmeňa po výbere možnosti ukončenia programu Gramps. Súbor sa uloží do cesty Zálohovanie uvedenej vyššie. Názov súboru zálohy bude zodpovedať Rodokmeňu doplnenému o dátum a čas.

- časový interval na spustenie úplného zálohovania počas relácií úprav programu Gramps.

  - **Nikdy** (*predvolené*)
  - Každých 15 minút
  - Každých 30 minút
  - Každú hodinu

{{-}}

Pozri tiež:

- [Zálohovanie rodokmeňa](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees#Backing_up_a_Family_Tree) - ďalšie informácie o zálohovaní
- [Zálohovanie opomenutí](wiki:Template:Backup_Omissions) - čo nie je zahrnuté počas zálohovania
- Addon [PostgreSQL](wiki:Addon:PostgreSQL) - pridáva podporu pre databázy PostgreSQL.

### Zobrazenie

![[_media/EditPreferences-Display-tab-default-51.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Ponuka: "Upraviť&gt;Predvoľby..." - "Zobrazenie" - karta - predvolené nastavenia]]

Záložka obsahuje predvoľby týkajúce sa zobrazovania údajov a názvov, **Nastavenia vzhľadu a formátu**. K dispozícii sú tieto možnosti:

- } Táto možnosť riadi zobrazovanie názvov v aktuálnej databáze (nastavenie je uložené v databáze a nie je systémové). V programe Gramps existujú dva typy formátov zobrazenia mien: preddefinované formáty a používateľom definované vlastné formáty. K dispozícii je niekoľko rôznych preddefinovaných formátov názvov: Given - Prefix Patronymic, Suffix Given - Prefix Surname, Given Patronymic Suffix atď.

  - Kliknutím na pravé tlačidlo sa zobrazí okno, v ktorom sa zobrazí dostupný zoznam možností. Uvedený je jeho formát, ako aj príklad. Ak preddefinované formáty nevyhovujú, je možné definovať vlastný formát. Na pridanie formátu názvu do zoznamu môžete použiť tlačidlo . Po jednom kliknutí sa zobrazí formát **SURNAME,Given Suffix(call)** a ako príklad : **SMITH, Edwin Jose Sr (Ed)**. Ak ste do zoznamu pridali nové formáty mien, na zmenu zoznamu formátov mien sa sprístupnia tlačidlá a .
    -   
      Začiarkávacie políčko predvolene nezačiarknuté. Ak je začiarknuté, umožňuje Gramps považovať patronymické a matronymické mená za priezviská.

- Táto voľba riadi zobrazovanie dátumov. Je to globálne nastavenie, ktoré si vyžaduje reštart programu Gramps, aby sa prejavilo, a vzťahuje sa na zobrazovanie dátumov vo všetkých databázach načítaných v programe Gramps, kým sa formát zobrazovania dátumu opäť nezmení. K dispozícii je niekoľko rôznych formátov, ktoré môžu závisieť od vášho lokálneho prostredia.

  - **RRRR-MM-DD (ISO)** (Predvolené nastavenie) - Príklad 2020-09-30 - Zobrazuje dátum pomocou medzinárodnej normy [ISO 8601 Dátové prvky a formáty výmeny - Výmena informácií](https://wikipedia.org/wiki/ISO_8601), ktorá je obzvlášť užitočná pri zdieľaní údajov medzi krajinami s rôznymi konvenciami pre zápis číselných dátumov a časov.
  - Číselný
  - Mesiac Deň, Rok
  - MESIAC DEŇ, ROK
  - Deň Mesiac Rok
  - DEŇ MES. ROK

<!-- -->

- Táto možnosť riadi zobrazovanie miest.

  - **Úplný** (predvolené nastavenie)
    - Výberom tlačidla sa zobrazí

<!-- -->

- - **Roky**(predvolené)
  - Roky, mesiace
  - Roky, mesiace, dni

- **Gregoriánsky** (predvolené nastavenie). Táto voľba riadi zobrazovanie kalendára na zostavách, nástrojoch, gramatikách, pohľadoch. K dispozícii je niekoľko rôznych kalendárov (pozri [Vydanie dátumu](wiki:Gramps_6.0_Wiki_Manual_-_Zadávanie_a_editácia_údajov:_Podrobné_-_časť_1#Editácia_dátum)). Dva dátumy s dvoma rôznymi kalendármi nebudú správne zobrazovať časovú os alebo periódu, (napr. použitím gregoriánskeho kalendára ako predvoleného zobrazeného kalendára budú mať používatelia lepšiu súdržnosť pri zobrazovaní dátumov na perióde).

<!-- -->

- <span id="hádanie priezviska"><span> Táto možnosť ovplyvňuje počiatočné priezvisko dieťaťa pri jeho pridaní do databázy. V predvolenom nastavení sa použije priezvisko otca. Výber možnosti znamená, že sa nebude hádať žiadne priezvisko. Výberom možnosti sa použije meno otca, za ktorým nasleduje meno matky. A nakoniec použije meno otca nasledované príponou "sson" (napr. syn Edwin bude hádaný ako Edwin*sson*).

- - **Neznámy**(predvolené)
  - Ženatý
  - Nezosobášený
  - Civilný zväzok

<!-- -->

- Predvolené:**150**

<!-- -->

- Táto možnosť riadi informácie zobrazené v stavovom riadku. Môže to byť buď **Meno a ID aktívnej osoby** (predvolené), alebo **Vzťah k domovskej osobe**.

<!-- -->

- *začiarknuté* (predvolené) Toto začiarkávacie políčko ovláda, či sa v [Navigátore](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window/sk#Navigátor) v [Hlavného okna](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window/sk#Main_Window) zobrazí textový popis vedľa ikony. Táto voľba sa prejaví po reštartovaní programu.

<!-- -->

- *nezačiarknuté*(predvolené)

#### Zobraziť Editor mena

![[_media/EditPreferences-Display-tab-DisplayNameEditor-dialog-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Display Name Editor - dialógové okno (príklad) z Menu: &quot;Upraviť&gt;Predvoľby...&quot; - &quot;Zobrazenie&quot; - karta]] Nasledujúce kľúčové slová sa nahradia príslušnými časťami názvu:

- <b>Dané</b> - krstné meno (meno)
- <b>Titul</b> - titul (Dr., pani)
- <b>Call</b> - meno, na ktoré sa volá
- <b>Initials</b> - prvé písmená mena Given
- <b>Primárne, primárne\[pre\] alebo \[sur\] alebo \[con\]</b> - úplné primárne priezvisko, predpriezvisko, iba priezvisko, konektor
- <b>Patronymické, alebo \[pre\] alebo \[sur\] alebo \[con\]</b> - úplné pa/matronymické priezvisko, prefix, len priezvisko, konektor
- <b>Familynick</b> - rodinný pseudonym
- <b>Ostatné</b> - neprirodzené priezviská
- <b>Rawsurnames</b> - priezviská (bez prefixu a konektora)
- <b>Priezvisko</b> - priezviská (s predponami a konektormi)
- <b>Prípona</b> - prípony (ml., st.)
- <b>Priezvisko</b> - prezývka
- <b>Prezývkové meno</b> - prezývka, inak prvé z daných
- <b>Prefix</b> - všetky prefixy (von, de)
- <b>Nepatronymické</b> - všetky priezviská, okrem pa/matronymických & primárne

Extra zátvorky, čiarky sú odstránené. Ostatné texty sa zobrazujú doslovne.

![[_media/NameEditor-format_reference_example-51.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Zobrazenie mena Editor - referenčná osoba]]

**Príklad:** Dr. Edwin Jose von der Smith a Weston Wilson Sr ("Ed") - Underhills

`von der`*`: Smith`*` a `*`Weston`*`: "a": "Weston", "Weston", "Weston", "Weston", "Weston", "Weston": `<abbr title="a connector">`[con]`</abbr>`, `*`Wilson`*`: (Wilson), patronymum,`

*Dr.*: "Dr.": titul, *Sr*: prívlastok, *Ed*: *Underhills* <abbr title="rodinný pseudonym">rodinný pseudonym</abbr>, Jose <abbr title="volaný (preferované krstné meno)">volaný</abbr>.

Všetky polia v príklade okrem Rodinného priezviska môžete pridať v štandardnom dialógovom okne Editor osôb. Dvojitým kliknutím na preferované meno v záložke Mená editora osôb získate prístup k ďalším poliam vrátane: Rodinného priezviska, ovládacích prvkov zoskupovania, ovládacích prvkov triedenia a zobrazovania výnimiek, ovládacích prvkov rozsahu dátumov pre použitie konkrétneho mena. {{-}}

#### Editor formátu miesta

![[_media/EditPreferences-Display-tab-PlaceFormatEditor-dialog-example-50.png|vpravo|thumb|450px|Obrázok {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Umiestnite Editor formátu - dialógové okno (príklad) z ponuky Menu: "Upraviť&gt;Predvoľby..." - "Zobrazenie" - karta]]

Prístupné z [Zobrazenie](wiki:Gramps_6.0_Wiki_Manual_-_Settings/sk#Display) záložky Formát miesta.

Táto karta obsahuje predvoľby týkajúce sa spôsobu zobrazenia Miesta.

- Jedinečný názov pre formát miesta.

- Názvy miest, ktoré sa majú zobrazovať.

Každá úroveň v hierarchii je reprezentovaná kladným celým číslom, začínajúcim od 0 pre vybrané miesto a zvyšujúcim sa o 1 pre každú vyššiu úroveň hierarchie. Úrovne môžu byť reprezentované aj zápornými celými číslami, začínajúcimi číslom -1 pre najvyššiu úroveň (zvyčajne krajina) a klesajúcimi o 1 pre každú nižšiu úroveň v hierarchii. Okrem toho je obývané miesto (mesto, obec, dedina alebo dedina) reprezentované písmenom p; to sa môže použiť s posunom (napr. p+1 alebo p-2).

Názvy, ktoré sa majú zobraziť, sú definované ako zoznam rozsahov oddelených čiarkou. Rozsah môže byť buď jedna úroveň, alebo počiatočná úroveň a koncová úroveň oddelené dvojbodkou. Počiatočná úroveň musí byť nižšia ako koncová úroveň rozsahu. Ak začiatočná a koncová úroveň chýbajú, sú predvolené hodnoty 0 a -1.

- "Žiadne" (predvolené), "Číslo ulice" alebo "Číslo ulice". Možnosť spojiť číslo a ulicu s cieľom potlačiť čiarku. Aby táto možnosť fungovala, ulica musí mať [<strong>Type</strong>](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_2/sk#Place_Editor_dialog) *Ulica**a číslo domu musí mať**Type*' *Číslo*'.

- (Predvolene prázdne) Dvojmiestny kód jazyka.

-  (štandardne nezačiarknuté)

Pozri tiež:

- [Dialógové okno Editor miesta](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_2/sk#Dialógové_okno_Editor_miesta)
- [Dialógové okno Editor názvu miesta](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_2/sk#Dialógové_okno_Editor_názvu_miesta)

{{-}}

### Text

![[_media/EditPreferences-Text-tab-default-51.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Ponuka: "Upraviť&gt;Predvoľby..." - "Text" - karta - predvolené nastavenia]]

Táto karta obsahuje predvoľby týkajúce sa spôsobu zobrazovania chýbajúcich a súkromných mien a záznamov.

- vo vstupnom poli môžete určiť, ako sa má chýbajúce priezvisko zobraziť. Predvolená hodnota je **`[Chýbajúce priezvisko]`**. Môžete ju zmeniť na \[--\] alebo na akúkoľvek inú hodnotu, ktorá vám najviac vyhovuje.

- vo vstupnom poli môžete určiť, ako sa má zobrazovať chýbajúce krstné meno. Predvolená hodnota je **`[Chýbajúce dané meno]`**. Túto hodnotu môžete zmeniť na akúkoľvek chcete.

- } Predvolené nastavenie: `[Chýbajúci záznam]`

- Predvolené nastavenie: `[Živý]`

- Predvolené: `[Žijúci]`

- Predvolené: `[Súkromný záznam]`

{{-}}

### Formáty ID

![[_media/EditPreferences-IDFormats-tab-default-51.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Ponuka: "Upraviť&gt;Predvoľby..." - "Formáty ID" - karta - predvolené nastavenia]]

Táto záložka obsahuje predvoľby relevantné pre automatické generovanie identifikátorov Gramps.

- } Poskytuje šablónu na generovanie ID pre Osobu. Predvolená hodnota: `I%04d`

- Poskytuje šablónu na generovanie ID pre rodinu. Predvolená hodnota: `F%04d`

- Poskytuje šablónu na generovanie ID pre miesto. Predvolená hodnota: `P%04d`

- Poskytuje šablónu na generovanie ID pre zdroj. Predvolená hodnota: `S%04d`

- Poskytuje šablónu na generovanie ID pre citáciu. Predvolená hodnota: `C%04d`

- Poskytuje šablónu na generovanie ID pre mediálny objekt. Predvolená hodnota: `O%04d`

- Poskytuje šablónu na generovanie ID pre udalosť. Predvolená hodnota: `E%04d`

- Poskytuje šablónu na generovanie ID pre archív. Predvolená hodnota: `R%04d`

- Poskytuje šablónu na generovanie ID pre poznámku. Predvolená hodnota: `N%04d`

Na zmenu formátu môžete použiť nástroj [Zmena poradia Gramps ID](wiki:Gramps_6.0_Wiki_Manual_-_Tools/sk#Zmena_poradia_Gramps_ID). {{-}}

### Dátumy

![[_media/EditPreferences-Dates-tab-default-51.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Ponuka: "Upraviť&gt;Predvoľby..." - "Dátumy" - karta - predvolené nastavenia]]

Nastavenia dátumu používané pre výpočtové operácie.

- Predvolené nastavenie: `<b>%s</b>`

  - Pohodlné značky sú:
    - <b>\<b\>Bold\</b\></b> (predvolené)
    - <big>\<big\>Relatívne zväčší písmo\</big\></big>
    - <i>\<i\>Kurzíva\</i\></i>
    - <s>\<s\>Prečiarknutie\</s\></s>
    - <sub>\<sub\>Podčiarkovanie\</sub\></sub>
    - <sup>\<sup\>Superscript\</sup\></sup>
    - <small>\<small\>Relatívne zmenší písmo\</small\></small>
    - `<tt>Monospace font</tt>`
    - <u>\<u\>Podčiarknutie\</u\></u>
      - Napríklad: \<u\>\<b\>%s\</b\>\</u\> zobrazí <u><b>podčiarknutý tučný dátum</b></u>.

- Predvolené nastavenie: `50`

  - Určuje počet rokov +/- od dátumu udalosti "`o `<date>", ktoré udalosť vráti ako platné pre filter.
  - Používa sa pri výpočte veku osoby.

- Predvolené nastavenie: `50`

  - Určuje počet rokov po dátume udalosti "`po `<date>", ktoré udalosť vráti ako platné pre filter.
  - Používa sa pri výpočte veku osoby.

- Predvolené nastavenie: `50`

  - Určuje počet rokov pred dátumom udalosti "`pred `<dátum>", ktoré udalosť vráti ako platné pre filter.
  - Používa sa pri výpočte veku osoby.

- Predvolené nastavenie: `110`

  - V prípade absencie udalosti Úmrtie vek, pri ktorom bude Gramps považovať osobu za už nežijúcu.

- Predvolené nastavenie: `20`

- Predvolené: `13`

- Predvolené: `20`

{{-}} Pozri tiež:

- [Gramps 6.0 Wiki manual - Pravdepodobne nažive](wiki:Gramps_6.0_Wiki_manual_-_Pravdepodobne_nažive)
- [Gramps 6.0 Wiki Manual - Probably Alive](wiki:Gramps_6.0_Wiki_Manual_-_Probably_Alive)
- [Editing dates](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1/sk#Editing_dates)
- Ručné nastavenie [date approximation .ini](wiki:Match_dates#Changing_after.2Fbefore.2Fabout_range)

{{-}}

### Bádateľ

![[_media/EditPreferences-Researcher-tab-default-51.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Ponuka: "Upraviť&gt;Predvoľby..." - "Bádateľ" - karta - predvolené nastavenia]]

Umožňuje vám do príslušných polí na zadávanie textu. Hoci program Gramps požaduje informácie o vás, tieto informácie sa používajú len preto, aby program Gramps mohol vytvoriť platné výstupné súbory GEDCOM. Platný súbor GEDCOM vyžaduje informácie o tvorcovi súboru. Ak sa rozhodnete, môžete tieto informácie nechať prázdne, avšak žiadny z vašich exportovaných súborov GEDCOM nebude platný.

K dispozícii sú tieto polia na zadávanie textu (všetky sú predvolene prázdne):

- 

- 

- 

- 

- 

- 

- 

- 

- 

Informácie zadané v tejto preferencii slúžia ako predvolená hodnota pre špecifické hodnoty rodokmeňa, ktoré možno upraviť pomocou nástroja [Edit Database Owner Information](wiki:Gramps_6.0_Wiki_Manual_-_Tools#Edit_Database_Owner_Information). {{-}}

### Upozornenia

![[_media/EditPreferences-Warnings-tab-default-51.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Ponuka: "Upraviť&gt;Predvoľby..." - "Upozornenia" - karta - predvolené nastavenia]]

Táto karta ovláda zobrazovanie dialógových okien s upozorneniami a umožňuje opätovné zapnutie dialógových okien, ktoré boli vypnuté.

- Štandardne začiarknuté políčko (pozri [Dialog](wiki:Gramps_6.0_Wiki_Manuál_-_Error_and_Warning_Reference#Suppress_warning_when_adding_parents_to_a_child))

- Štandardne nezačiarknuté políčko (pozri [Dialog](wiki:Gramps_6.0_Wiki_Manuál_-_Error_and_Warning_Reference#Suppress_warning_when_cancelling_with_changed_data))

- Štandardne nezačiarknuté políčko (pozri [Dialog](wiki:Gramps_6.0_Wiki_Manuál_-_Error_and_Warning_Reference#Suppress_warning_about_missing_researcher_when_exporting_to_GEDCOM))

- Štandardne nezačiarknuté políčko (pozri [Dialog](wiki:Gramps_6.0_Wiki_Manuál_-_Error_and_Warning_Reference#Module_not_loaded_warnings))

Príklady nájdete na stránke [Error and Warning Reference](wiki:Gramps_6.0_Wiki_Manual_-_Error_and_Warning_Reference). {{-}}

### Farby

![[_media/EditPreferences-Colors-tab-default-51.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Ponuka: "Upraviť&gt;Predvoľby..." - "Farby" - záložka - predvolené nastavenia]]

Táto karta umožňuje nastaviť **farby používané pre políčka v grafických zobrazeniach**.

Môžete vybrať

- *Svetlé farby* (predvolené) alebo *Tmavé farby*

  - \- obnoví predvolené farby tém.

- Farby pre mužské osoby

- Farby pre osoby ženského pohlavia

- Farby pre neznáme osoby

- Farby pre rodinné uzly

- Ostatné farby

{{-}}

#### Výber farby

![[_media/PickAColor-selector-dialog-50.png|vpravo|thumb|450px|Obrázok {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Vyberte farbu" - dialógové okno výberu]]

Vyberte farbu z oblasti palety farieb alebo vyberte tlačidlo na vytvorenie vlastnej farby buď prostredníctvom priameho "kódu farby Hex"; posuvníka alebo kliknutím myšou. {{-}}

### Genealogické symboly

![[_media/EditPreferences-GenealogicalSymbols-tab-default-60.png|Obrázok {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Genealogické symboly" - karta Predvoľby - aktivované predvolené nastavenia]]

Umožňuje používať genealogické symboly namiesto textových skratiek v správach, grafoch a v rozhraní Gramps.

Táto karta vám dáva možnosť použiť jedno písmo, ktoré dokáže zobraziť všetky genealogické symboly. (Po konfigurácii pozri: \[Predpoklad_používania_Genealogických_Symbolov\|Predpoklad používania genealogických symbolov\]\])

Ak zaškrtnete políčko "používať symboly", Gramps použije vybrané písmo, ak existuje.

To môže byť užitočné, ak chcete do poznámky pridať fonetiku, aby ste ukázali, ako sa meno vyslovuje, alebo ak miešate viacero jazykov, napríklad gréčtinu a ruštinu.

Na tejto karte môžete konfigurovať iba symbol smrti.

  
Zoznam zobrazených genealogických symbolov (zoradených v poradí uvedenom na spodnej snímke obrazovky):

- Žena
- Mužský
- Asexualita, bez pohlavia, bez pohlavia
- Lesbickosť
- Mužská homosexualita
- Heterosexualita
- Transgender, hermafrodit (v entomológii)
- Transgender
- Neuterita

<!-- -->

- nelegitímny
- Narodenie
- Krst/krstiny
- Zasnúbený
- Manželstvo
- rozvod
- Nezosobášené partnerstvo
- Pochovaný
- kremácia/pohrebná urna
- Zabitý v boji
- Vyhynutý

<!-- -->

- Smrť

{{-}}

|  | symbol | Kódový bod(y) Unicode | názov |
|----|----|----|----|
| male | ♂ | U+2642 | Mužský znak |
| žena | ♀ | U+2640 | Ženský znak |
| neznámy | ⚪︎ | U+26AA | Stredný biely kruh |
| hermafrodit | ⚥ | U+26A4 | Prepojený mužský a ženský znak |
| neuter | ⚲ | U+26B2 | Neuter |
| narodenie | \* | U+002A | Hviezdička |
| krst, krstiny | ~ | U+007E | Tilda |
| smrť | ✝︎ | U+271D | Latinský kríž |
| pohreb | ⚰︎ | U+26B0 | Rakva |
| kremácia | ⚱︎ | U+26B1 | Pohrebná urna |
| mŕtvo narodený | ✝︎\* | U+0086 U+002A | Latinský kríž, hviezdička |
| narodený nezákonne | \*⃝ | U+002A U+20DD | Hviezdička v kruhu |
| narodený nelegitímne | ⊛ | U+229B | Operátor s kruhovou hviezdičkou |
| zabitý v akcii | ⚔︎ | U+2694 | Skrížené meče |
| táto línia zanikla | ‡ | U+2021 | Dvojitá dýka |
| aproximate(ly) | ± | U+00B1 | Plus-mínus |
| pred | \< | U+003C | Symbol Less-Than |
| za | \> | U+003E | Symbol väčší ako |
|  | ⚬ | U+26AC | Stredný malý biely kruh |
| vydatá | ⚭ | U+26AD | Symbol manželstva |
| rozvedený | ⚮ | U+26AE | Symbol rozvodu |
| slobodný | ⚯ | U+26AF | Symbol partnerstva nezosobášených |

{{-}}

#### Predpoklad používania genealogických symbolov

![[_media/EditPreferences-GenealogicalSymbols-tab-default-51.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Genealogické symboly" - karta Predvoľby - predvolené nastavenia]]

##### Počiatočné nastavenie

Ak bol nainštalovaný fontconfig [predpoklad](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Predpoklad), potom na záložke vyberte tlačidlo , Gramps sa pokúsi zistiť všetky vhodné unicode textové fonty, ktoré možno použiť.

![[_media/EditPreferences-GenealogicalSymbols-FindFont-51.png|Obrázok {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Genealogické symboly" - Vyhľadávanie písma]]

Po dokončení vyhľadávania vyberte jedno z písiem zo zoznamu a potom zaškrtnite políčko:

##### Prerequisite

Predpoklad : **python-fontconfig** : Na zobrazenie genealogických symbolov sa vyžaduje väzba fontconfig na Python a jeho závislosti

Pozrite si tiež:

- Tamura Jones vysvetľuje na [Genealogické symboly](https://www.tamurajones.net/GenealogySymbols.xhtml) ''(časť 'Unicode' je obzvlášť dôležitá)'
- [GEPS 039: Genealogické symboly v gramatike](wiki:GEPS_039:_Genealogické_symboly_v_gramatike)
- Žiadosť o funkciu: Gramps by mal byť schopný používať genealogické symboly všade.
- [Prispôsobenie vyhľadávacej tabuľky Genealogické symboly](wiki:Prispôsobenie_vyhľadávacej_tabuľky_Genealogické_symboly), ktorá sa nachádza v [Gramps user directory](wiki:Gramps_6.0_Wiki_Manual_-_User_Directory/sk#MS_Windows) na adrese: [gramps\gen\utils\symbols.py](https://github.com/gramps-project/gramps/blob/maintenance/gramps51/gramps/gen/utils/symbols.py)\].

{{-}}

## Ďalšie nastavenia

Okrem dialógového okna sú v programe Gramps k dispozícii aj ďalšie nastavenia. Z rôznych dôvodov boli ľahšie dostupné, ako je uvedené nižšie. {{-}}

### Editor stĺpcov

![[_media/ConfigureTheActiveView-icon-on-toolbar-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Výber tlačidla]]

![[_media/ColumnsEditorTab-dialog-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Editor stĺpcov - dialóg - príklad ľudí]]

Stĺpce zobrazenia zoznamu možno pridávať, odstraňovať alebo meniť ich poradie v dialógovom okne .

Ak chcete použiť dialógové okno pre aktuálne zobrazenie, vyberte prostredníctvom ponuky , kliknite na ![[_media/Gramps-config.png]] tlačidlo na paneli nástrojov alebo stlačte tlačidlo *Konfigurovať aktívne zobrazenie* [viazanie klávesnice](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings/sk#Common_keybindings).

V zobrazení sa zobrazia len stĺpce so zaškrtnutým políčkom. Pozíciu stĺpca v zobrazení môžete zmeniť aj kliknutím a pretiahnutím na novú pozíciu v Editore ([*potiahni a pusť*](https://wikipedia.org/wiki/Drag-and-drop)). Po vykonaní požadovaných zmien kliknite na , potom kliknite na , aby ste opustili Editor a zobrazili svoje zmeny v Zobrazení.

V predvolenom nastavení sa v Zozname zobrazení zobrazuje niekoľko stĺpcov s informáciami o príslušnej kategórii. Stĺpce môžete pridávať alebo odstraňovať zo zobrazenia

Predvoleným kľúčom na triedenie zobrazenia \[vždy vzostupne\] je najľavšie pole \[t. j. hore v Editore stĺpcov\], takže zmena toho, ktoré pole je na tejto pozícii, ovplyvňuje predvolené triedenie.

![[_media/ConfigurePersonView-51.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Editor stĺpcov - dialógové okno - príklad miest]]Dialógové okno bude mať pre každú kategóriu Zobrazenia, ktoré zobrazuje jednoduchú tabuľku, iný výber stĺpcov.

Zmeny sa prejavia až po kliknutí na tlačidlo .

Po aplikovaní zmien stĺpcov Zobrazenia sa po jednom kliknutí na záhlavie stĺpca zoradí vzostupne, po ďalšom kliknutí sa zoradí zostupne.

Podskupina stĺpcov a aktuálne [filtre](wiki:Gramps_6.0_Wiki_Manual_-_Filtre) obmedzia aj údaje exportované prostredníctvom operácie } Zoradenie podľa stĺpca "Dátum narodenia" v režime zoznamu v zobrazení kategórie Ľudia - príklad\]\]

V predvolenom nastavení každé Zobrazenie kategórie, ktoré prezentuje údaje v stĺpcovom usporiadaní tabuľky, zoradí riadky vzostupne na základe údajov v prvom (najľavejšom) stĺpci. Ak má tabuľka zoskupené riadky, zoskupené údaje sa budú triediť ďalej. ''(Podobne budú fungovať aj tabuľky v podskupinách údajov v záložkách, Editory a Selektory.)

Kliknutím raz na záhlavie iného stĺpca sa údaje tohto stĺpca zoradia vzostupne. Opätovným kliknutím na záhlavie sa údaje zoradia v opačnom poradí.

Dialógové okno možno použiť na pridávanie, odstraňovanie a zmenu poradia zobrazených stĺpcov. Výberom iného prvého stĺpca sa tento stĺpec stane novým predvoleným stĺpcom triedenia pohľadu \[hoci vždy vzostupne\]. {{-}}

### Nastavenie domovskej osoby

![[_media/MenuEdit-SetHomePerson-60.png|Obrázok {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Ponuka zobrazujúca <em>Nastaviť domovskú osobu</em>]]

Ak chcete nastaviť (určiť) [Domovskú osobu](wiki:Gramps_Glossary#home_person), vyberte kategóriu Ľudia a vyberte požadovanú osobu, aby sa z nej stala [Aktívna osoba](wiki:Gramps_Glossary#active_person), a potom cez menu vyberte .

Prípadne pri úprave ľubovoľnej Osoby kliknite pravým tlačidlom myši na neaktívne oblasti (oblasti bez poľa na zadávanie textu) hornej časti, čím sa zobrazí kontextové menu, ktoré obsahuje možnosť daného profilu.

Domovská osoba je trvalo určená osoba, ktorá sa stáva [Aktívnou osobou](wiki:Gramps_Glossary#active_person), keď nastane jedna z nasledujúcich situácií:

- Predvolene pri otvorení databázy rodinného stromu  
  *(Nastavenie [Všeobecné](wiki:Gramps_6.0_Wiki_Manual_-_Settings/sk#General_Gramps_settings) v [Predvoľby](wiki:Gramps_6.0_Wiki_Manual_-_Settings/sk#Predvoľby) môže toto predvolené správanie zmeniť. "Zapamätať si posledný zobrazený pohľad" vráti na poslednú [Aktívnu osobu](wiki:Gramps_Glossary#active_person) z predchádzajúcej relácie.")*
- Po kliknutí na tlačidlo na paneli nástrojov
- Keď sa vyberie položka Domov z ponuky alebo z kontextovej ponuky pravého tlačidla myši vo vybraných zobrazeniach
- Ak sa [keybinding](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings#15) sa stlačí na návrat na **Domovskú osobu**.

Tlačidlo na paneli nástrojov je k dispozícii v kategórii Ľudia, kategórii Vzťahy a kategórii Rodinný strom. ![[_media/Gramps_Go-Home48x48_win.png]]

#### Pozrite tiež

- [Nastavenie domovskej osoby](wiki:Gramps_6.0_Wiki_Manual_-_Navigation/sk#Nastavenie_domovskej_osoby)

{{-}}

### Nastavenie ovládacích prvkov pohľadu

To, či sa v hlavnom okne zobrazí panel nástrojov, bočný panel alebo filter (nie je k dispozícii v pohľadoch Rodinný strom a Vzťahy), sa nastavuje prostredníctvom ponuky Pohľad.

V rôznych pohľadoch sa po kliknutí na ponuku zobrazia políčka, na ktoré môžete kliknúť:

- Navigátor
- Panel nástrojov
- Bočný panel
- Dolný panel
- Celá obrazovka

Okrem toho budú v závislosti od pohľadu, v ktorom sa nachádzate, k dispozícii ďalšie možnosti na .

- Príklady:
  - Nastavte hodnotu stĺpcov na 1
  - Nastavenie stĺpcov na 2
  - Nastaviť stĺpce na 3
- Vzťahy:
  - Zobraziť súrodencov
  - Zobraziť podrobnosti
- Zemepis:
  - Časové obdobie
  - Rozloženie

Všetky ostatné pohľady: [Editor stĺpcov](wiki:Gramps_6.0_Wiki_Manual_-_Settings/sk#Editor_stĺpcov).

### Exportné zobrazenie

![[_media/Menubar-FamilyTrees-overview-FamilyTree-Loaded-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menubar - "Rodinné stromy" - prehľadný príklad zobrazujúci položku ponuky "Exportovať zobrazenie"]]

Vo väčšine [Zobrazenia zoznamu kategórií](wiki:Gramps_6.0_Wiki_Manual_-_Categories/sk#Kategórie_navigátora) je možné zobrazené údaje exportovať, vyberte si ich cez [menu](wiki:Gramps_6.0_Wiki_Manual_-_Navigation/sk#Hlavné_Menu) príkaz.

Tento príkaz Menu sa zobrazí len vtedy, ak je možné exportovať zobrazené údaje. Gramps vyexportuje údaje na obrazovke podľa vášho výberu: **CSV** alebo **Open Document** formát tabuľky.

Všimnite si, že aktuálna konfigurácia stĺpcov Zobrazenia bude riadiť, aké údaje sa budú exportovať. Export bude obsahovať len zobrazené údaje stĺpcov (v rovnakom poradí) a bude obmedzený na záznamy, ktoré vyhovujú všetkým [filterom](wiki:Gramps_6.0_Wiki_Manual_-_Filters), ktoré ste použili. {{-}}

#### Dialógové okno Exportovať zobrazenie ako tabuľku

![[_media/ExportViewAsSpreadsheet-CSV-file-dialog-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Exportovať zobrazenie ako tabuľku" CSV(predvolený) súbor-dialóg - príklad]]

Gramps potom zobrazí dialógové okno, v ktorom po výbere umiestnenia súboru na uloženie a názvu súboru; exportujte údaje zo zobrazenia zoznamu kategórií v jednom z dvoch formátov tabuľkového procesora:

- **CSV** (predvolený)
- **OpenDocument Spreadsheet** - formát ODS.

{{-}} ![[_media/ExportViewAsSpreadsheet-ODS-Displayed-in-LibreOfficeCalc-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Príklad tabuľky ODS - zobrazenie v LibreOffice Calc]]

Na ukážkovom obrázku je zobrazený export do **OpenDocument Spreadsheet** (formát ODS) zobrazený ako tabuľka v programe Libreoffice Calc.

{{-}}

### Modularita a zásuvné moduly

Program Gramps bol navrhnutý na rozšírenie. Rámec zásuvných modulov (tzv. plug-in, addon, doplnok, rozšírenie) poskytuje cestu pre vývoj tretích strán mimo bežných distribúcií vydania Gramps.

Dokumentácia pre každý doplnok je udržiavaná mimo toku týchto hlavných kapitol wiki. Rozhranie a funkčnosť softvéru a dokumentácie nemusia byť v súlade so štýlmi, ktoré sú viditeľné vo zvyšku Gramps... hoci vyzývame vývojárov, aby sa snažili, aby ich doplnky boli čo najplynulejšie.

Stručný opis a snímku obrazovky každého doplnku nájdete v časti [Zoznam doplnkov](wiki:6.0_Doplnky#Soznam_doplnkov) príručky wiki. Na samostatne udržiavanú stránku s dokumentáciou k doplnku vedie odkaz z 1. stĺpca tohto zoznamu.

Pozri [Správca doplnkov](wiki:Gramps_6.0_Wiki_Manuál_-_Plugin_Manager) a [Doplnky tretích strán](wiki:6.0_Addons). {{-}}

### Prispôsobenie výstupných formátov zostáv

![[_media/TextReports-DocumentOptions-section-PlainText-output-settings-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Príklad Možnosti dokumentu - predvolené nastavenia záložky pre textové správy (Plain Text - vybraný výstup)]]

Aký druh prispôsobenia výstupu je k dispozícii? Toto dialógové okno umožňuje zmeniť písmo, veľkosť písma, farbu písma, farbu pozadia textu a zarovnanie odsekov v správe.

Pri väčšine dialógových okien zostavy sa v hornej časti nachádzajú karty možností, ktoré sa konkrétne týkajú danej zostavy. Spodná časť bude obsahovať širšie opakovane použiteľné funkcie a nazýva sa časť.

Z rozbaľovacieho zoznamu môžete vybrať existujúci vlastný štýl. Alebo ak si chcete vytvoriť vlastný , vyberte tlačidlo , čím sa zobrazí a potom vyberte tlačidlo , aby sa zobrazilo dialógové okno .

{{-}}

#### Dialógové okno Štýly dokumentu

![[_media/DocumentStyles-dialog-50.png|Obrázok {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Štýly dokumentu - dialógové okno - predvolené]]

V dialógovom okne sa zobrazí zoznam *predvolených* štýlov a všetkých vlastných štýlov pre danú zostavu a umožní vám upraviť alebo odstrániť všetky vytvorené vlastné štýly. Výberom tlačidla sa zobrazí dialógové okno . {{-}}

#### Dialógové okno Editor štýlu

Dialógové okno umožňuje prispôsobiť štýl dokumentu špecifický pre každú správu.

Zmeňte (<kód>Nový štýl</kód> predvolený) na jedinečný názov, ako sa bude zobrazovať v rozbaľovacom zozname.

Po dokončení zmien vlastného štýlu vyberte tlačidlo na uloženie zmien alebo na ukončenie.

{{-}}

##### Dialógové karty editora štýlov

Na ľavej strane uvidíte stĺpec , v ktorom sú uvedené možnosti odsekov špecifické pre danú zostavu, ktoré môžete upravovať. Napríklad } zobrazuje možnosti štýlu pre AHN-Entry, AHN-Generation a AHN-Title.

Na pravej strane sú tri záložky súvisiace s každým štýlom uvedeným v ľavom stĺpci: {{-}}

###### Description

![[_media/StyleEditor-dialog-Description-tab-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Karta Možnosti opisu - Štýly dokumentu - dialógové okno (predvolené štýly pre správu Ahnentafel) (Gramps 4.2.0 Windows 7)]]

- : Popis opisuje, čoho sa týka každý odsek. Tu je napríklad uvedený štýl použitý pre správu Ahnentafel Report ( AHN-Entry ).

{{-}}

###### Možnosti písma

![[_media/StyleEditor-dialog-FontOptions-tab-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Karta "Možnosti písma" - dialógové okno "Editor štýlov" pre "Štýly dokumentu" (predvolené štýly pre Ahnentafel Report)]]

- : Tu môžete nastaviť Roman alebo Swiss, písma v bodoch, písma a niektoré ako napríklad tučné písmo, kurzíva alebo podčiarknutie.

{{-}}

###### Možnosti odseku

![[_media/StyleEditor-dialog-ParagraphOptions-tab-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Karta "Možnosti odseku" - dialógové okno "Editor štýlov" pre "Štýly dokumentu" (predvolené štýly pre Ahnentafel Report)]]

- : Tu nastavíte , , , a vášho štýlu.

{{-}}

### Kontextové menu

Používa sa na rôznych miestach programu Gramps; spôsob prístupu ku kontextovej ponuke závisí od operačných systémov:

- V oknách Microsoft sa kontextová ponuka zobrazí spravidla pravým tlačidlom myši alebo pomocou klávesovej skratky +. pozri [Používanie kontextových ponúk - Dokumenty Microsoft](https://docs.microsoft.com/en-us/previous-versions/windows/desktop/mpc/using-context-menus).
- V systéme Apple macOS spravidla stlačíte a zároveň kliknete na tlačidlo myši, aby ste zobrazili kontextovú ponuku. pozri: [Kontextové ponuky - Menu - macOS - Human Interface Guidelines - Apple Developer](https://developer.apple.com/design/human-interface-guidelines/macos/menus/contextual-menus/).

Pozri tiež:

- [Keybindings](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings/sk)

## Prispôsobenie

Tu je niekoľko spôsobov, ako si môžete prispôsobiť Grampa.

### Predvoľby

Pozri [Predvoľby](wiki:Gramps_6.0_Wiki_Manual_-_Settings/sk#Predvoľby).

### Jazyk

Program Gramps bol preložený do viacerých [jazykov](wiki:Portal:Translators). Zvyčajne sa Gramps automaticky spustí vo vašom miestnom jazyku, ako je zvolený pre iné aplikácie, ale niekedy to nemusí byť pre vás správne. A v iných prípadoch modul alebo doplnok ešte nebude preložený a zobrazí sa dialógové okno s upozornením, v ktorom sa píše niečo ako “Upozornenie: zásuvný modul XYZ nemá preklad pre žiadny z vašich nastavených jazykov, namiesto toho použite americkú angličtinu”. (Všimnite si, že americký dialekt angličtiny je predvolený, a nie britský.) To môže byť otravné alebo rušivé.

Najideálnejšou situáciou je, že americkú angličtinu ovládate rovnako dobre ako jazyk zvolený pre grafické rozhranie operačného systému vo vašom počítači. A že by ste využili možnosť preložiť túto funkciu Gramps pre používateľov, ktorí nehovoria po anglicky.

Ak je váš systém nakonfigurovaný tak, aby zobrazoval iný jazyk ako angličtinu, môžete to pre funkciu Gramps prepísať.

Ako príklad predpokladajme, že počítač v Holandsku je predvolene nakonfigurovaný na holandský jazyk Unicode 8: "LANG: nl_NL.UTF-8". Môžete buď resetovať jazyk operačného systému

V systéme Windows použiť príkaz SET na obnovenie premennej LAN env na "en_GB.UTF-8" pre britskú angličtinu. Môžete to urobiť z rozhrania príkazového riadka alebo [vytvoriť zástupcu pri spustení s nasledujúcim cieľom](https://gramps-project.org/bugs/view.php?id=11009): `C:\Windows\System32\cmd.exe /c "SET LANG=en_GB.UTF-8 && START /D ^"C:\Program Files\GrampsAIO64-6.0.3^" gramps.exe"`

'''

#### Linux

Ak chcete vybrať "variant" lokálneho jazyka pre triedenie, ktorý nie je predvoleným variantom, potom môžete spustiť Gramps z terminálu (alebo konzoly) s iným prostredím LC_COLLATE. Napríklad predvolený variant triedenia (collation) pre švédčinu je "reformed", ale namiesto toho môžete zvoliť "standard" zadaním:

` export LC_COLLATE="sv_SE.UTF-8@collation=standard"`  
` python Gramps.py`

#### Mac OS X

Pre Mac OS X si pozrite [Pokročilé nastavenie](wiki:Mac_OS_X:Application_package#Advanced_setup), kde nájdete podrobnosti o tom, ako sa bežne vyberá jazyk a ako si vybrať špeciálne, nepredvolené nastavenie jazyka, poradia triedenia alebo formátu takých vecí, ako sú názvy dní a mesiacov a oddeľovače čísel.

#### MS Windows

![[_media/MicrosoftWindowGrampsAIO-Installer-ChooseComponents-Selection-example-60.png|Okno Microsoft Window Gramps AIO Installer Choose Components-Selection]]. Ak chcete spustiť program Gramps v inom jazyku ako v angličtine pomocou inštalačného programu Gramps AIO, musíte ho vybrať počas procesu inštalácie.

V opačnom prípade nebude k dispozícii.

Viac informácií nájdete na stránke [Download#MS_Windows](wiki:Download#MS_Windows).

{{-}}

### Pridať položku ponuky operačného systému Windows

Ak chcete, aby program Gramps fungoval vo vami vybranom jazyku (Kód jazyka nájdete v tabuľke nižšie), vyplňte nasledujúce údaje:

- Pomocou pravého tlačidla myši kliknite na ikonu "GrampsAIOxx 5.x.x" na pracovnej ploche a z ponuky vyberte: Vyberte položku Kopírovať.
- Kliknite pravým tlačidlom myši kdekoľvek na pracovnej ploche a z ponuky vyberte: Vložiť zástupcu
- Vytvorí sa nová ikona s názvom: "GrampsAIOxx 5.x.x (2)".
- Kliknite na ňu pravým tlačidlom myši a z ponuky vyberte: Vlastnosti
- Otvorí sa nové okno, kliknite na prvú kartu s názvom Všeobecné a zmeňte text z "GrampsAIOxx 5.x.x (2)" na niečo opisnejšie, napr: "GrampsAIO dánsky".
  - Kliknite na druhú kartu s názvom Skratka, zmeňte text v prvej položke s názvom Cieľ z (pozn. cesta sa bude líšiť v závislosti od použitej verzie Gramps):
    - \<Program Files(xxx)\GrampsAIOxx-5.x.x\grampsw.exe"</code> na:
    - `%comspec% /c set LANG=da_DK.UTF-8 && start grampsw.exe"`
- Kliknite na tlačidlo OK a teraz sa po kliknutí na túto ikonu spustí program Gramps v dánčine.

### Zmena premenných LANG okna

Ďalšia možnosť, ak chcete, aby sa program Gramps vždy načítaval povedzme v kanadskej francúzštine, môžete ísť do okna Windows \> Vlastnosti systému a pridať premennú LANG v používateľskej časti dialógového okna premenných prostredia s príslušnou hodnotou.

Hodnota, ktorú treba pridať, je:

    Názov: LANG
    Hodnota: fr_CA.UTF-8

### Jazykové kódy

Vyberte si z nasledujúcej tabuľky [jazykov, do ktorých bol preložený Gramps](wiki:Portál:Prekladatelia):

| Jazyk                 | ISO kód     | Príklad | Poznámky |
|-----------------------|-------------|---------|----------|
| Holandčina            | nl_BE.UTF-8 |         |          |
| Angličtina (britská)  | en_GB.UTF-8 |         |          |
| fínčina               | fi-UTF-8    |         |          |
| Kanadská francúzština | fr_CA.UTF-8 |         |          |
| Ruský                 | ru_RU.UTF-8 |         |          |
|                       |             |         |          |

- Kódy jazykov sú dvojmiestne kódy jazykov ISO s malými písmenami (napríklad "da"), ako sú definované v [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes).
- Kódy krajín sú dvojpísmenové veľké ISO kódy krajín (ako napríklad "BE"), ako je definované v [ISO 3166-1](https://en.wikipedia.org/wiki/ISO_3166-1).

### Pokročilá manipulácia s nastaveniami

Okrem nastavení, ktoré sú k dispozícii v Nastaveniach, môžete preskúmať aj rozšírené nastavenia.

Program Gramps používa **[INI keys](https://en.wikipedia.org/wiki/INI_file#Keys_(properties))** a [INI sections](https://en.wikipedia.org/wiki/INI_file#Sections) na správu používateľských predvolieb a nastavení programu tieto sú uložené v textovom súbore `gramps.ini` v priečinku `.gramps/gramps[XX]` vo vašom domovskom alebo používateľskom adresári.

Súbor `gramps.ini` má nasledujúce časti:

- \[správanie\] : typické názvy kľúčov sú: [betawarn](https://github.com/gramps-project/gramps/blob/master/gramps/gui/grampsgui.py#L502), enable-autobackup, use-tips...
- \[farby\] :
- \[database\] : súvisí s nastaveniami databázy pre rodokmeň.
- \[export\] : export a import priečinkov/adresárov
- \[geografia\] :
- \[rozhranie\] : množstvo kľúčov týkajúcich sa výšky a šírky rôznych zobrazení: napr. event-height (výška udalosti): 450, event-ref-height (výška udalosti): 585, event-ref-width (šírka udalosti): 728, event-width (šírka udalosti): 712...
- \[paths\] : kľúče týkajúce sa nedávno importovaných súborov a priečinkov/adresárov
- \[plugin\] :
- \[preferences\] : kľúče týkajúce sa preferencií: všetky bežné predvoľby , todo -colors..
- \[researcher\] : všetky informácie týkajúce sa výskumníka
- \[utf8\] :

#### Príklad `gramps.ini` súbor

Príklad obsahu súboru `gramps.ini`:

    ;; Súbor s kľúčom Gramps
    ;; Automaticky vytvorený v 2020/05/17 15:15:34

    [správanie]
    ;;addmedia-image-dir=''
    ;;addmedia-relative-path=0
    ;;addons-url='https://raw.githubusercontent.com/gramps-project/addons/master/gramps51'
    ;;autoload=0
    ;;avg-generation-gap=20
    ;;betawarn=0
    ;;check-for-addon-update-types=['new']
    ;;check-for-addon-updates=0
    ;;date-about-range=50
    ;;date-after-range=50
    ;;date-before-range=50
    ;;do-not-show-previously-seen-addon-updates=1
    ;;generation-depth=15
    ;;last-check-for-addon-updates='1970/01/01'
    ;;max-age-prob-alive=110
    ;;max-sib-age-diff=20
    ;;min-generation-years=13
    ;;owner-warn=0
    ;;pop-plugin-status=0
    ;;previously-seen-addon-updates=[]
    ;;recent-export-type=3
    ;;runcheck=0
    ;;spellcheck=0
    ;;startup=0
    ;;surname-guessing=0
    translator-needed=0
    ;;use-tips=0
    ;;web-search-url='http://google.com/#&q=%(text)s'
    ;;welcome=100

    [farby]
    ;;border-family=['#cccccc', '#252525']
    ;;border-family-divorced=['#ff7373', '#720b0b']
    ;;border-female-alive=['#861f69', '#261111']
    ;;border-female-dead=['#000000', '#000000']
    ;;border-male-alive=['#1f4986', '#171d26']
    ;;border-male-dead=['#000000', '#000000']
    ;;border-unknown-alive=['#8e5801', '#8e5801']
    ;;border-unknown-dead=['#000000', '#000000']
    ;;family=['#eeeeee', '#454545']
    ;;family-civil-union=['#eeeeee', '#454545']
    ;;rodina-rozvedený=['#ffdede', '#5c3636']
    ;;rodina-manželstvo=['#eeeeee', '#454545']
    ;;rodina-neznáma=['#eeeeee', '#454545']
    ;;rodina-nezosobášená=['#eeeeee', '#454545']
    ;;žena-živá=['#feccf0', '#62242D']
    ;;žena-mŕtva=['#feccf0', '#3a292b']
    ;;home-person=['#bbe68a', '#304918']
    ;;male-alive=['#b8cee6', '#1f344a']
    ;;male-dead=['#b8cee6', '#2d3039']
    ;;scheme=0
    ;;unknown-alive=['#f3dbb6', '#75507B']
    ;;unknown-dead=['#f3dbb6', '#35103b']

    [databáza]
    ;;autobackup=0
    ;;backend='sqlite'
    ;;backup-on-exit=1
    ;;backup-path='C:\\Users\\[username]\\Documents\\GrampsBackup'
    ;;compress-backup=1
    ;;host=''
    ;;path='C:\\Users\\[username]\\Documents\\\gramps\\grampsdb'
    ;;port=''

    [export]
    ;;proxy-order=[["privacy", 0], ["living", 0], ["person", 0], ["note", 0], ["reference", 0]]

    [geografia]
    ;;center-lat=0,0
    ;;center-lon=0,0
    ;;lock=0
    ;;map='person'
    ;;map_service=1
    ;;path=''
    ;;show_cross=0
    ;;use-keypad=1
    ;;zoom=0
    ;;zoom_when_center=12

    [rozhranie]
    ;;dbmanager-height=350
    ;;dbmanager-horiz-position=12
    ;;dbmanager-vert-position=85
    ;;dbmanager-width=780
    ;;dont-ask=0
    ;;filter=0
    ;;fullscreen=0
    ;;grampletbar-close=0
    ;;ignore-gexiv2=0
    ;;ignore-osmgpsmap=0
    ;;ignore-pil=0
    ;;main-window-height=500
    ;;main-window-horiz-position=15
    ;;main-window-vert-position=10
    ;;main-window-width=775
    ;;mapservice='OpenStreetMap'
    ;;open-with-default-viewer=0
    ;;pedview-layout=0
    ;;pedview-show-images=1
    ;;pedview-show-marriage=0
    ;;pedview-show-unknown-people=0
    ;;pedview-tree-direction=2
    ;;pedview-tree-size=5
    ;;place-name-height=100
    ;;place-name-width=450
    ;;sidebar-text=1
    ;;size-checked=0
    ;;statusbar=1
    ;;surname-box-height=150
    ;;toolbar-on=1
    ;;toolbar-text=0
    ;;treemodel-cache-size=1000
    ;;view=1
    ;;view-categories=['Dashboard', 'People', 'Relationships', 'Families', 'Ancestry', 'Events', 'Places', 'Geography', 'Sources', 'Citations', 'Repositories', 'Media', 'Notes']

    [cesty]
    ;;quick-backup-directory='C:\\Users\\[username]\\Documents\\gramps'
    ;;quick-backup-filename='%(filename)s_%(year)d-%(month)02d-%(day)02d.%(extension)s'
    ;;recent-export-dir='C:\\Users\\[username]\\Documents\\gramps'
    ;;recent-file=''
    ;;recent-import-dir='C:\\Users\[username]\\Documents\\gramps'
    ;;report-directory='C:\\Users\[username]\\Documents\\gramps'
    ;;website-cal-uri=''
    ;;website-cms-uri=''
    ;;website-directory='C:\\Users\[username]\\Documents\\gramps'
    ;;website-extra-page-name=''
    ;;website-extra-page-uri=''

    [plugin]
    ;;addonplugins=[]
    ;;hiddenplugins=[]

    [preferences]
    ;;age-display-precision=1
    ;;calendar-format-report=0
    ;;cprefix='C%04d'
    ;;date-format=0
    ;;default-source=0
    ;;eprefix='E%04d'
    ;;family-relation-type=3
    ;;family-warn=1
    ;;fprefix='F%04d'
    ;;hide-ep-msg=0
    ;;invalid-date-format='<b>%s</b>'
    ;;iprefix='I%04d'
    last-view='dashboardview'
    last-views=['dashboardview', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
    ;;name-format=1
    ;;no-given-text="[Chýba uvedené meno]
    ;;no-record-text="[Chýbajúci záznam]
    ;;no-surname-text="[Chýbajúce priezvisko]
    ;;nprefix="N%04d
    ;;online-maps=0
    ;;oprefix='O%04d'
    ;;paper-metric=0
    ;;paper-preference="Letter
    ;;patronimic-surname=0
    ;;place-auto=1
    ;;place-format=0
    ;;pprefix="P%04d
    ;;private-given-text="[Living]
    ;;private-record-text="[Private Record]
    ;;private-surname-text="[Living]
    ;;quick-backup-include-mode=0
    ;;rprefix="R%04d
    ;;sprefix='S%04d'
    ;;tag-on-import=0
    ;;tag-on-import-format='Importované %Y/%m/%d %H:%M:%S'
    ;;use-last-view=0

    [výskumník]
    ;;researcher-addr=''
    ;;researcher-city=''
    ;;researcher-country=''
    ;;researcher-email=''
    ;;researcher-locality=''
    ;;researcher-name="''
    ;;researcher-phone=''
    ;;researcher-postal="''
    ;;researcher-state=''

    [utf8]
    ;;available-fonts=[]
    ;;death-symbol=13
    ;;in-use=0
    ;;selected-font=''

#### Pokročilé nastavenie názvu záložného súboru

Vzor pomenovania názvu záložného súboru môžete definovať aj nastavením *`paths.quick-backup-filename`* v kľúčovom súbore `~/.gramps/gramps51/gramps.ini` nasledovne: {{-}}

` [paths]`  
` ;;quick-backup-filename='%(filename)s_%(year)d-%(month)02d-%(day)02d.%(extension)s'`

odstránením dvoch stredníkov(`;;`) z prednej časti riadku kľúča INI a použitím niektorého z nasledujúcich kľúčových slov pre vzor filenam: Názov súboru: \*názov súboru

- rok
- mesiac
- deň
- hodina
- minút
- sekúnd
- rozšírenie :
  - **.gpkg**(predvolené), ak zahrniete médiá.
  - *.gramps*, ak vylúčite médiá.

Použite príslušný súbor s kľúčom ~/.gramps/gramps{XX}/gramps.ini.

- Gramps verzia 6.0 :

` ~/.gramps/gramps51/gramps.ini`

Pozrite si tiež: 1:

- [Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees/sk#Backup_dialog](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees/sk#Backup_dialog)
- [Gramps_6.0_Wiki_Manual_-_Command_Line/sk#Configuration_.28config.29_option](wiki:Gramps_6.0_Wiki_Manual_-_Command_Line/sk#Configuration_.28config.29_option)
- [Install_latest_BSDDB#Make_Gramps_use_bsddb3](wiki:Install_latest_BSDDB#Make_Gramps_use_bsddb3)
- [Prispôsobiť_tabuľku_genealogických_symbolov#Genealogické_symboly_preferencie](wiki:Prispôsobiť_tabuľku_genealogických_symbolov#Genealogické_symboly_preferencie)

### Téma

Vzhľad programu Gramps je možné zmeniť.

- [Addon:Theme Preferences](wiki:Addon:ThemePreferences)
- [Windows_AIO_themes](wiki:Windows_AIO_themes)
- [Téma GTK 3 - GEPS 029: GTK3-GObject introspection Conversion](wiki:GEPS_029:_GTK3-GObject_introspection_Conversion#GTK_3_theme)
- [Overrule_Gramps_Icons](wiki:Overrule_Gramps_Icons) - pre staršie verzie Gramps.
- [UI style](wiki:UI_style)

Niektoré hlásenia je možné tiež zmeniť:

- [Webové správy Témy](wiki:Webové_správy_Témy)

{{-}}

[Category:Sk:Documentation](wiki:Category:Sk:Documentation)
