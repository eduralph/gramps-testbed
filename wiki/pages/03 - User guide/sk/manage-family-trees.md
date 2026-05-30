---
title: Gramps 6.0 Wiki Manual - Manage Family Trees/sk
categories:
- Sk/Documentation
- Sk:Documentation
- Stub
managed: false
source: wiki-scrape
wiki_revid: 127179
wiki_fetched_at: '2026-05-30T20:08:27Z'
lang: sk
---

{{#vardefine:chapter\|5}} {{#vardefine:figure\|0}} Podrobný prieskum každodenného používania aplikácie Gramps. V tejto kapitole poskytujeme podrobný prehľad o tom, ako môžete spravovať svoje rodinné stromy, ako aj zdieľať svoje údaje s inými genealógmi.

## Založenie nového rodinného stromu

![[_media/Menubar-FamilyTrees-overview-FamilyTree-Loaded-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Panel ponuky - "Rodinné stromy" - príklad prehľadu]]

Ak chcete spustiť nový Rodinný strom, vyberte } alebo vyberte tlačidlo na paneli nástrojov alebo použite [klávesovú skratku](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings/sk) . Tým sa otvorí okno správcu .

Vyberte tlačidlo a do zoznamu Rodinných stromov pridajte novú položku Rodinný strom. Ak chcete zmeniť jeho názov z predvoleného *<kód>Rodinný strom 1</kód>*, vyberte názov a stlačte tlačidlo a potom zadajte nový názov.

Ak chcete otvoriť nový, prázdny Rodinný strom, vyberte ho a buď dvakrát kliknite naň, alebo stlačte tlačidlo . {{-}} ![[_media/FamilyTrees-ManageDatabases-icon-toolbar-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure\|{{#expr:{{#var:figure}}+1}}}} Správa databáz - ikona na paneli nástrojov (Rovnaká ako pri použití ponuky]] {{-}} ![[_media/ConnectToARecentDatabase-icon-toolbar-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure\|{{#expr:{{#var:figure}}+1}}}} Pripojenie k nedávnej databáze - rozbaľovacia ikona v ponuke panela nástrojov]] {{-}}

### Okno správcu rodinných stromov

Rodinné stromy sú to, čo Gramps nazýva databázovou štruktúrou používanou na ukladanie a organizáciu genealogických údajov. Rodinný strom je potrebné vytvoriť predtým, ako je možné vložiť akékoľvek genealogické údaje, [obnoviť zo zálohy archívu](wiki:Ako_obnoviť_zálohu) alebo [importovaných z iného softvéru](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees/sk#Import_údajov).

Rodinné stromy možno premenovať, previesť do iných databázových backendov, opraviť alebo vymazať. Tu sa "chyba" nebude dať napraviť. (Najväčšia potenciálna chyba, náhodné vymazanie, si vyžaduje potvrdenie.)

![[_media/FamilyTreesManager-window-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Okno správcu "Rodinné stromy"]]

Kliknutím na tlačidlo sa zobrazí okno správcu , ktoré umožňuje pracovať a spravovať rodinné stromy nachádzajúce sa v konkrétnom [Cesta k databáze rodinných stromov](wiki:Gramps_6.0_Wiki_Manual_-_Setting/sk#Rodinný_strom) adresári Gramps.

Okno Správca rodinných stromov umožňuje vytvoriť nový rodinný strom, premenovať existujúci rodinný strom, vymazať rodinný strom, načítať rodinný strom alebo skontrolovať informácie o rodinnom strome. V zozname sa zobrazujú všetky názvy vašich Rodinných stromov. Ak je Rodinný strom otvorený, v stĺpci so stavom sa vedľa jeho názvu zobrazí ikona . Zobrazí sa typ databázy, ako aj údaj o dátume a čase, kedy bol váš rodinný strom *naposledy otvorený*.

- vytvorí nový rodinný strom.

- zobrazí informácie o vybranom rodinnom strome.

- vybraný rodinný strom, zobrazí sa upozornenie s konečným potvrdením, ktoré si môžete vybrať.

- vybraný existujúci Rodinný strom.

- vybraný existujúci rodokmeň.

- vybraný rodinný strom. Táto možnosť sa zobrazí len vtedy, keď je databáza stromu iná ako databáza . Pozri: \[\[Gramps_6.0_Wiki_Manual\_-\_Manage_Family_Trees#Converting_a_BSDDB_Family_Tree_to_SQlite\|Converting a legacy [BSDDB](wiki:Gramps_Glossary#bsddb) Rodinný strom do [SQlite](wiki:Gramps_Glossary#sqlite).

- vybraný existujúci Rodinný strom, dostupné len vtedy, ak Gramps zistí problém.

- Možnosť je prítomná len vtedy, ak je nainštalovaný [GNU Revision Control System](http://www.gnu.org/software/rcs/) (RCS).

- Možnosť sa používa s tlačidlom a táto možnosť je prítomná len vtedy, ak je nainštalovaný [GNU Revision Control System](http://www.gnu.org/software/rcs/) (RCS).

- \- otvorí predvolené okno prehliadača zobrazujúce túto časť online príručky.

- \- zruší okno správcu .

- otvorí vybraný existujúci rodinný strom do pracovnej pamäte a uzamkne databázový súbor, aby ostatní používatelia nemohli vykonať konfliktné úpravy.

{{-}}

## Otvorenie rodinného stromu

Ak chcete otvoriť rodinný strom, vyberte ponuku } alebo kliknite na tlačidlo na paneli nástrojov . Zobrazí sa a zobrazí sa zoznam všetkých rodinných stromov, ktoré sú Gramps známe. V stĺpci sa pri každom práve otvorenom Rodinnom strome zobrazí ikona (vyzerá ako otvorený priečinok). Vyberte strom, ktorý chcete otvoriť, a otvorte ho výberom tlačidla . Prípadne môžete dvakrát kliknúť na požadovaný Rodinný strom.

Ak chcete otvoriť nedávno otvorený Rodinný strom, vyberte buď ponuku alebo šípku nadol vedľa tlačidla na paneli nástrojov a vyberte Rodinný strom zo zoznamu.

### Režim len na čítanie

Ponuka Nástroje nebude k dispozícii.

## Uloženie zmien v rodinnom strome

Gramps uloží vaše zmeny hneď, ako ich aplikujete. To napríklad znamená, že kedykoľvek pri používaní programu Gramps kliknete na , vaše zmeny sa okamžite zaznamenajú a uložia. Neexistuje žiadny samostatný príkaz "uložiť".

Vykonané zmeny môžete vrátiť späť výberom ponuky . Ak tento príkaz vyberiete opakovane, vaše posledné zmeny budú zrušené postupne. Ak chcete vrátiť späť viacero príkazov naraz, môžete použiť dialóg ponuky .

Ak chcete svoj rodinný strom vrátiť do stavu, v akom bol pri otvorení, vyberte ponuku . (Je to rovnaké ako ukončenie bez uloženia v iných programoch.)

Ak chcete uložiť kópiu svojho rodinného stromu pod iným názvom, musíte ho exportovať a potom importovať do nového rodinného stromu. Na tento účel sa odporúča formát databázy *Gramps XML*.

## Otvorenie databázy GEDCOM alebo XML

Program Gramps umožňuje otvoriť niektoré databázy, ktoré neboli uložené vo vlastnom formáte programu Gramps, z príkazového riadku, pozri [Command line references](wiki:Gramps_6.0_Wiki_Manual_-_Command_Line/sk#Opening_options). Patria medzi ne databázy XML a GEDCOM. Mali by ste si však uvedomiť, že ak je databáza XML alebo GEDCOM relatívne veľká, narazíte na problémy s výkonom a v prípade havárie sa vaše údaje môžu poškodiť. Preto je zvyčajne lepšie vytvoriť nový rodinný strom (databázu) Gramps a importovať do nej údaje XML/GEDCOM.

## Odstránenie rodinného stromu

Vyberte rodinný strom, ktorý chcete odstrániť, a kliknite na tlačidlo .

Tým sa strom **úplne** odstráni bez možnosti obnovenia údajov. Zvážte vytvorenie zálohy údajov exportom do formátu GRAMPS XML a uložením tohto súboru.

## Premenovanie rodinného stromu

Rodinný strom (alebo jeho archív) môžete premenovať tak, že vyberiete strom, ktorý chcete premenovať, a kliknete na tlačidlo . Môžete tiež kliknúť na názov v zozname stromov.

V oboch prípadoch stačí zadať nový názov, aby sa začal uplatňovať.

## Zálohovanie rodinného stromu

Najbezpečnejším spôsobom zálohovania vášho rodinného stromu Gramps je export bez možností ochrany osobných údajov a filtrov do formátu **Gramps XML** (alebo **Gramps XML Package**, ak chcete zahrnúť položky z vašej galérie) a skopírovanie výsledného súboru na bezpečné miesto, najlepšie do inej budovy.

### Dialógové okno Zálohovanie

![[_media/MakeBackup-GrampsXML-Backup-example-60.png|Obrázok {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Vytváranie zálohy]]

V ponuke vyberte }

Zobrazí sa okno .

Môžete zadať }, kam sa má záloha uložiť ručne alebo pomocou tlačidla vyvolať dialógové okno .

Názov môžete zadať ručne alebo použiť automaticky vygenerovaný názov súboru.

Môžete si vybrať, či chcete *Zahrnúť* alebo **Vylúčiť** (predvolené nastavenie) .

{{-}}

- Na ukladanie snímok rodinného stromu môžete použiť funkciu Archív (pozri nasledujúcu časť). Tieto snímky môžete použiť ako jednoduché zálohy, čo je veľmi užitočné, ak chcete vyskúšať niečo, čo by ste neskôr chceli vrátiť späť. Táto metóda by sa však nemala používať na štandardné zálohovanie, pretože neprežijú haváriu pevného disku ani väčšinu iných katastrof, ktoré môžu postihnúť počítač.

<!-- -->

- *Pre pokročilých používateľov:* každá databáza je uložená vo vlastnom podadresári v adresári ~/.gramps. Hoci je možné vytvoriť ručnú zálohu zálohovaním tohto adresára, neodporúča sa to. Dôrazne sa odporúča, aby ste namiesto toho použili zálohu Gramps XML.

### Zálohovanie pri ukončení

V predvoľbách karty je možné nastaviť, aby sa pri ukončení programu Gramps vytvorila záloha. Všimnite si, že sa tým vytvorí záloha len pre otvorený rodinný strom. Ak je strom zatvorený pred ukončením programu Gramps, nevytvorí sa žiadna záloha.

- [Nastavenia rodinného stromu](wiki:Gramps_6.0_Wiki_Manual_-_Settings/sk#Rodinný_strom)

### Automatické zálohovanie

V predvoľbách karty je možné nastaviť, aby program Gramps vytváral zálohu každých 15, 30 alebo 60 minút.

Pozri tiež:

- [Nastavenia rodinného stromu](wiki:Gramps_6.0_Wiki_Manual_-_Settings/sk#Rodinný_strom)
- [Advanced backup filename setting](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Advanced_backup_filename_setting) - Kde môžete definovať aj vzor pomenovania názvu záložného súboru.
- [Zálohovanie vynechaných súborov](wiki:Template:Backup_Omissions) - čo nie je zahrnuté počas zálohovania

## Archivácia rodinného stromu

Pomocou programu Gramps môžete svoje rodinné stromy, zachovať ako kópiu pred akýmikoľvek väčšími zmenami a mať možnosť vrátiť sa k známej verzii.

Ak chcete vytvoriť archív :

![[_media/ManageFamilyTrees-Archive-RevisionComment-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Príklad archivácie rodinného stromu]]

1.  načítajte svoj Rodinný strom.
2.  kliknite na tlačidlo na paneli nástrojov (po nabehnutí naň sa zobrazí ).
3.  Kliknite na rodinný strom, ktorý ste práve načítali: malo by sa zobraziť tlačidlo .
4.  kliknite na a v dialógovom okne budete môcť zadať *Popis verzie* vášho archívu.

Po archivácii sa teraz v zozname rodinných stromov zobrazí váš pôvodný rodinný strom s trojuholníkom smerujúcim doprava na jeho ľavej strane.

- Kliknutím na trojuholník sa zobrazí názov archívu (opätovným kliknutím sa zoznam archívu zbalí).

Archívy je možné , a .

{{-}}

## Extrahovanie archívu rodinného stromu

![[_media/ManageFamilyTrees-Archive-Selected-to-Extract-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Dialógové okno (Správca) "Rodinné stromy" - vybraný archív pripravený "Extrahovať" - príklad]]

Ak chcete získať verziu predtým archivovaného rodinného stromu, v správcovi "Rodinného stromu" zvýraznite archív, ktorý chcete obnoviť, a vyberte tlačidlo .

{{-}} ![[_media/ManageFamilyTrees-Archive-Extracted-version-selected-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Dialógové okno (Správca) &quot;Rodinné stromy&quot; - vyextrahovaná a vybraná archívna verzia - príklad]]

Archív sa potom obnoví do nového rodinného stromu a bude uvedený v správcovi rodinných stromov.

Názov rodinného stromu je založený na pôvodnom názve a názve archívu, napr: *<názov pôvodného stromu>`:`<názov archívu>* (pozri tiež [Archivácia rodinného stromu](#Archiving_a_Family_Tree))

Toto môže byť užitočný spôsob uchovania archívu, pretože archívy zmiznú, ak sa pôvodný strom odstráni; a **nie sú zahrnuté do exportu rodinného stromu Gramps XML**. {{-}}

## Odomknutie rodinného stromu

![[_media/FamilyTreesManager-Dialog-ShowingLocked-Sample-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Rodinné stromy (Správca) - dialógové okno - zobrazenie uzamknutého &quot;vzorového&quot; rodinného stromu]] Program Gramps je databázová aplikácia pre jedného používateľa a pri používaní identifikuje súbory databázy Strom ako obsadené ![[_media/22x22-gramps-lock.png]]'zámkom'. Keď program Gramps otvorí strom, vypustí súbor `lock` (v ktorom je uvedené používateľské meno a doména) do podpriečinka stromu v priečinku `grampsdb` v [Adresári používateľa](wiki:Gramps_6.0_Wiki_Manual_-_User_Directory/sk). Gramps vám (ani nikomu inému) nedovolí otvoriť tento strom v rovnakom čase. Druhá inštancia programu Gramps bude môcť otvoriť iný rodinný strom, ale každý už otvorený rodinný strom sa zobrazí s ikonou zámku v stĺpci Stav v dialógovom okne Správa rodinných stromov. Zatvorením stromu v prvej kópii programu Gramps sa odstráni súbor zámku a strom sa sprístupní na otvorenie v druhej inštancii.

Ak by ste *mohli* otvoriť ten istý rodinný strom v dvoch inštanciách programu Gramps naraz, je pravdepodobné, že by sa vaše údaje poškodili, pretože by si tieto dve inštancie navzájom prepísali prácu.

#### Pozrite tiež:

- [Command Line:Force unlock option](wiki:Gramps_6.0_Wiki_Manual_-_Command_Line/sk#Force_unlock_option)

### Dialógové okno Prelomenie uzamknutia databázy "Názov rodinného stromu"?

![[_media/ErrorParsingArguments-dialog-DatabaseIsLocked-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}}Chyba pri analyzovaní argumentov - dialóg - Databáza je uzamknutá príklad]] V nepravdepodobnom prípade, že sa Gramps zrúti, rodinný strom zostane v uzamknutom stave (indikovaný ikonou ![[_media/22x22-gramps-lock.png]]zámku v stĺpci vedľa názvu rodinného stromu)

Odomknutie rodinného stromu počas spustenia

- Ak je v [predvoľbách rodinného stromu](wiki:Gramps_6.0_Wiki_Manual_-_Settings/sk#Rodinný_sttom) nastavené automatické otváranie stromu pri spustení, zobrazí sa dialógové okno **Chyba pri analyzovaní argumentov**, ktoré upozorňuje, že **Databáza je uzamknutá**. Kliknite na tlačidlo a potom z ponuky vyberte .
- V opačnom prípade sa pri spustení programu Gramps automaticky zobrazí .

{{-}} ![[_media/Break-the-lock-on-the-database-Dialog-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Prelomiť uzamknutie databázy &quot;Ukážka&quot;? - Dialógové okno - príklad]]Vyberte uzamknutý rodinný strom a potom kliknite na tlačidlo . Zobrazí sa dialógové okno *'Prelomiť uzamknutie databázy '\[Názov rodinného stromu\]*?

Kliknite na tlačidlo a v okne by sa malo zobraziť, že ikona zámku zmizla.

Vyberte predtým uzamknutý rodinný strom a potom kliknite na tlačidlo a pokračujte v práci. {{-}}

## Oprava poškodeného rodinného stromu

![[_media/FamilyTreesManager-Dialog-ShowingRedErrorStatusIcon-Sample-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Rodinné stromy (Správca) - dialógové okno - zobrazenie červenej ikony stavu Chyba pre "Ukážkový" rodinný strom]]

Ak by sa váš rodinný strom nejakým spôsobom poškodil alebo znehodnotil, Správca rodinného stromu Gramps zobrazí v stĺpci červenú ikonu Chyba.

Ak chcete, aby sa program Gramps pokúsil poškodenie opraviť, vyberte Rodinný strom a potom kliknite na tlačidlo .

Tým sa pokúsite obnoviť Rodinný strom zo záložných súborov, ktoré sa automaticky vytvoria pri ukončení.

Pozrite si tiež:

- [Obnova poškodeného rodinného stromu](wiki:Obnova_poškodeného_rodinného_stromu)

{{-}}

## Konverzia rodinného stromu BSDDB do SQLite

![[_media/ManageFamilyTrees-Convert-the-database-dialog-example-51.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} <strong>Konvertovať databázu 'Názov rodinného stromu'?</strong> dialóg s <em>Rodinnými stromami (Správca)</em>' - Dialóg zobrazený na pozadí]]

Ak máte v dialógovom okne *Rodinné stromy (Správca)* - Dialóg zobrazený starší formát [BSDDB](wiki:Gramps_Glossary#bsddb) **Typ databázy**' pre niektorý z vašich rodinných stromov, potom sa výberom rodinného stromu v dialógovom okne *Rodinné stromy (Správca)* - Dialóg zobrazí tlačidlo ako dostupné.

Keď ste pripravení, vyberte tlačidlo a zobrazí sa dialógové okno s hlásením **Chcete previesť tento rodinný strom do databázy SQLite?** môžete vybrať na zastavenie alebo na spustenie procesu, po dokončení sa v dialógovom okne *Rodinné stromy (Správca)* - zobrazí nový záznam pre konvertovanú kópiu vášho rodinného stromu, ale s typom databázy *SQLite*, potom by ste mali otvoriť a zálohovať skonvertovaný rodinný strom.

Potom môžete premenovať pôvodný rodinný strom BSDDB so slovom **STARÝ** alebo ho môžete Vymazať, aby nedošlo k zámene. Následne môžete premenovať novú databázu SQLite.

{{-}}

## Importovanie údajov

Importovanie vám umožňuje preniesť údaje z iných genealogických programov do Rodinného stromu Gramps. Gramps dokáže importovať údaje z nasledujúcich formátov:

- [Gramps XML](#Gramps_XML_and_XML_Package_import) (prípona súboru `.gramps`) natívny formát výmeny údajov Gramps v nekomprimovanom textovom formáte a [gzip](https://wikipedia.org/wiki/Gzip) komprimovanom formáte
- [Gramps XML Package](#Gramps_XML_and_XML_Package_import) (prípona súboru `.gpkg`) Gramps [.tar.gz](https://wikipedia.org/wiki/.tar.gz) archív v komprimovanom formáte zálohy
- [Databáza Gramps V2.x](#GRAMPS_V2.x_database_import) (prípona súboru `.grdb`)
- [CSV tabuľka](#Gramps_CSV_import) - hodnoty oddelené čiarkou (prípona súboru `.csv`)
- [GEDCOM](#GEDCOM_import) (prípona súboru `.ged`) de facto štandardný formát súboru na výmenu údajov medzi genealogickými programami
- GeneWeb (prípona súboru `.gw`) - [GeneWeb](https://en.wikipedia.org/wiki/GeneWeb) je genealogický softvér s webovým rozhraním.
- Pro-Gen (prípona súboru `.def`) - [Pro-Gen](https://www.pro-gen.nl/gbhome.htm) je veľmi populárny v Holandsku a severozápadnom Nemecku. Často ho používajú ľudia, ktorí začali zbierať a ukladať údaje už v roku 1989. Išlo o program založený na systéme DOS, ktorý bol opravený tak, aby fungoval s operačným systémom Win 10.
- vCard (prípona súboru `.vcf`) - [Virtual Contact File](https://wikipedia.org/wiki/VCard) je štandardný formát súboru pre elektronické vizitky.
- Import JSON (prípona súboru `.json`) - [JavaScript Object Notation](https://www.json.org/) je odľahčený formát na výmenu údajov.
- Import SQLite (prípona súboru `.sql`) - [Formát databázy SQLite](https://www.sqlite.org/fileformat.html).

### Dialógové okno Import rodinného stromu

![[_media/Importfamilytree-dialog-51.png|Obrázok {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Import rodinného stromu - príklad dialógu]]

Najprv vytvorte [nový a prázdny Rodinný strom](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees/sk#Starting_a_new_Family_Tree). Potom vyberte ponuku alebo použite [klávesovú skratku](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings#2) na import údajov alebo obnovenie predtým uloženého Rodinného stromu Gramps (zo staršej verzie programu Gramps alebo aktuálnej verzie) sa otvorí dialógové okno *'*, v ktorom budete požiadaní o zadanie súboru, ktorý chcete importovať.

![[_media/UndoHistoryWarning-Import-dialog-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Dialógové okno s upozornením na import]]Pri pokuse o import do rodinného stromu, ktorý je ***neprázdny***, sa otvorí dialógové okno . To vám pripomenie, aby ste si pred importom vytvorili zálohu. Namiesto toho vytvorte nový Rodinný strom, pokiaľ sa vedome nepokúšate zlúčiť údaje.

Program Gramps používa [GTK File Chooser](https://developer.gnome.org/gtk3/stable/GtkFileChooser.html) na výber súboru údajov, ktorý sa má exportovať. Základné možnosti prechodu na súbor sú známe a zrejmé.

Predvolenou možnosťou zobrazenia cesty k súboru je zobrazenie každej úrovne priečinka ako klikateľnej [breadcrumb navigation](https://en.wikipedia.org/wiki/Breadcrumb_navigation). Cestu možno zadať do editovateľného textového poľa stlačením klávesovej akratky .

Príponu typu súboru zvyčajne umožní voľba , ktorá očakáva konkrétny vzor údajov, ktoré sa majú previesť do natívneho formátu databázy. Toto môžete potlačiť výberom inej **** možnosti. Zoznam súborov možno filtrovať zmenou z možnosti .

Ak plánujete používať import opakovane (na priebežné aktualizácie alebo vrátane genealogického výskumu), môžete [prispôsobiť dialógové okno](https://gramps.discourse.group/t/need-help-doing-a-cross-os-linux-mac-verification/1068/5) pridaním tlačidiel pre cesty k priečinkom so záložkami. Kliknite pravým tlačidlom myši na názov priečinka a z kontextového menu vyberte .

### Import databázy GRAMPS V2.x

Databáza GRAMPS V2.x (.grdb): Pred verziou Gramps 3.0 bol tento natívny formát databázy Gramps špecifickou formou databázy Berkeley (BSDDB) so špeciálnou štruktúrou dátových tabuliek. Tento formát bol binárny a závislý od architektúry. Bol veľmi rýchly a efektívny, ale nebol všeobecne prenosný medzi počítačmi s rôznou binárnou architektúrou (napr. i386 vs. alpha).

Import z formátu databázy GRAMPS V2.x je podporovaný len verziou Gramps 3.0.x. Importom z formátu V2.x do formátu Gramps V3.0.x sa nestratia žiadne údaje.

#### Presun databázy Gramps 2.2 do databázy Gramps 3.x

Ak chcete presunúť údaje programu Gramps z verzie 2.x do verzie 6.0.x, musíte databázu v2.x importovať do skoršej verzie programu Gramps v3.0.x a potom buď databázu uložiť a importovať do programu Gramps 6.0.x, alebo databázu exportovať vo formáte [XML](wiki:XML) zo skoršej verzie programu Gramps a importovať ju do programu Gramps 6.0.x.

Pokyny na import databáz verzie v2.x do programu Gramps v3.x nájdete v [používateľskej príručke](wiki:User_manual_translations) pre staršie verzie programu Gramps.

{{-}}

### Import súborov Gramps XML a XML Package

Gramps [XML](wiki:XML) a Gramps [XML](wiki:XML) Package sú natívne formáty programu Gramps. Pri importe (obnove) z týchto formátov alebo exporte do nich nehrozí strata informácií.

- Gramps [XML](wiki:XML) (.gramps): Súbor Gramps [XML](wiki:XML) je štandardným formátom Gramps na výmenu údajov a zálohovanie a bol tiež predvoleným formátom pracovnej databázy pre staršie verzie Gramps (pred verziou 2.x). Na rozdiel od formátu GRAMPS V2.x grdb je nezávislý od architektúry a čitateľný pre človeka. Databáza môže obsahovať aj odkazy na nelokálne (externé) mediálne objekty, preto nie je zaručená jej úplná prenosnosť (pre úplnú prenosnosť vrátane mediálnych objektov v balíku Gramps [XML](wiki:XML) (.gpkg) by sa mal používať). Databáza Gramps [XML](wiki:XML) sa vytvorí exportom (Menu ) do tohto formátu.

<!-- -->

- Balík Gramps [XML](wiki:XML) (.gpkg): Balík Gramps [XML](wiki:XML) je **komprimovaný** archív obsahujúci súbor Gramps [XML](wiki:XML) a všetky [mediálne](wiki:Gramps_Glossary#media) objekty (obrázky, zvukové súbory atď.), na ktoré sa databáza odvoláva. Keďže obsahuje všetky mediálne objekty, tento formát je úplne prenosný. Balík Gramps [XML](wiki:XML) sa vytvorí exportom ( v ponuke ) údajov v tomto formáte.

Ak importujete informácie z inej databázy Gramps alebo databázy Gramps [XML](wiki:XML), priebeh operácie sa zobrazí na riadku priebehu hlavného okna programu Gramps. Po dokončení importu sa v okne spätnej väzby zobrazí počet importovaných objektov. Ak importované údaje pochádzajú zo samotného rodinného stromu, do ktorého údaje importujete, spätná väzba importu poskytuje návrhy, čo by sa mohlo zlúčiť; zlúčenie sa **nevykoná** automaticky za vás. Ak chcete automaticky zlúčiť základné genealogické údaje, zvážte export/import tabuľky CSV.

### Import CSV programu Gramps

- Formát tabuľky Gramps CSV umožňuje importovať a exportovať podmnožinu vašich údajov Gramps v jednoduchom tabuľkovom formáte. Pozri [Import a export CSV](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees:_CSV_Import_and_Export/sk), kde nájdete ďalšie informácie.

### Import GEDCOM

Najprv vytvorte [nový prázdny Rodinný strom](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees#Starting_a_new_Family_Tree). Potom vyberte ponuku alebo [keybinding](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings#2) potom použite dialógové okno na výber súboru GEDCOM, ktorý chcete importovať, v závislosti od typu GEDCOM sa potom môže zobraziť dialógové okno .

Keď importujete informácie z GEDCOM, v hlavnom okne programu Gramps sa zobrazí [priebehový riadok](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window#Status_Bar_and_Progress_Bar). Po dokončení importu GEDCOM sa v okne } a v okne **** zobrazia všetky výsledky alebo varovania.

{{-}}

#### Dialógové okno Kódovanie GEDCOM

![[_media/GEDCOM-Encoding-dialog-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Kódovanie GEDCOM - dialóg]]

Dialógové okno sa zobrazí, keď sa importovaný súbor GEDCOM identifikoval ako súbor používajúci formát kódovania ANSEL. Niekedy je to chybné. Ak po importovaní súboru GEDCOM zistíte, že vaše údaje obsahujú nezvyčajné znaky, vráťte import späť a prepíšte znakovú sadu výberom iného kódovania z dostupného zoznamu.

- **predvolené**
- ANSEL
- ANSI (iso-8859-1)
- ASCII
- UTF8

{{-}}

#### Dialógové okno Import štatistiky

![[_media/ImportStatistics-dialog-example-GrampXML-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Import štatistík - dialógové okno]] Zobrazí podrobnosti o štatistikách importu. {{-}}

#### Dialógové okno Správa o importe GEDCOM

![[_media/GEDCOM-import-report-result-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Správa o importe GEDCOM - príklad výsledkov]].

V '''} Poznámka k importu GEDCOM s uvedením vynechaných údajov pripojená k "Source\>Note" (údaje z "GEDitCOM" - "GEDCOM 5.5 Torture Test Files")\]\]

Program Gramps používa pokročilejší "dátový model" ako program GEDCOM, preto niektoré údaje v programe GEDCOM nemožno importovať do programu Gramps. (Pozri [Gramps a GEDCOM](wiki:Gramps_a_GEDCOM).) Hlavné výnimky sú:

- Niektoré štruktúry atribútov GEDCOM sa považujú za štruktúry Gramps , a preto mnohé z primitívnych prvkov GEDCOM nemožno uložiť.
- Prvky DATA v SOURCE_RECORD (označujúce zaznamenané udalosti a zodpovednú agentúru) sa ignorujú.
- Všetky citácie zdrojov v poznámkach sa ignorujú.
- Mnohé primitívne prvky GEDCOM nemajú presne zodpovedajúce dátové prvky v programe Gramps, a preto sa ukladajú ako s príslušnými názvami, zvyčajne značkou GEDCOM. Týka sa to najmä záhlavia, odosielateľa a podania záznamov GEDCOM a konkrétnych polí, ako sú REFN, RFN, RIN a AFN.

Ak sú údaje uvedené ako "ignorované", ich vynechanie sa oznámi v spätnej väzbe na konci importu a zahrnie sa do pripojenej k príslušnému objektu s vlastným typom . Pozri napríklad objekt Zdroj na ukážke obrazovky.

Ak sú údaje uvedené ako "ticho ignorované", nie sú nahlásené a nie sú zahrnuté do poznámky. V súčasnosti to možno považovať za niečo, čo bolo prehliadnuté programom Gramps a malo by sa to uviesť ako problém . {{-}}

#### Obmedzenia importu GEDCOM

This section describes any GEDCOM data that cannot be directly represented in Gramps, and how it is handled. For additional information on the limits of GEDCOM imports (and exports), please read the section on [Gramps and GEDCOM](wiki:Gramps_and_GEDCOM).

##### HEADer, SUBMitter and SUBmissioN

Gramps has no direct representation of this data, and hence all information there has to be stored in other objects. Depending on a [General preferences](wiki:Gramps_6.0_Wiki_Manual_-_Settings#General) setting, a 'default source' object may be created. If this is created, then much of the data is stored in that , or in attached to that source.

###### HEADer

`   HEADER:=`  
`        n HEAD                                          {1:1}`  
`          +1 SOUR `<APPROVED_SYSTEM_ID>`                  {1:1}  (Data item of the 'default source')`  
`            +2 VERS `<VERSION_NUMBER>`                    {0:1}  (Data item of the 'default source')`  
`            +2 NAME `<NAME_OF_PRODUCT>`                   {0:1}  (Data item of the 'default source')`  
`            +2 CORP `<NAME_OF_BUSINESS>`                  {0:1}  (Repository of the 'default source')`  
`              +3 <`<ADDRESS_STRUCTURE>`>                  {0:1}  (Repository of the 'default source')`  
`            +2 DATA `<NAME_OF_SOURCE_DATA>`               {0:1}  (Data item of the 'default source')`  
`              +3 DATE `<PUBLICATION_DATE>`                {0:1}  (Data item of the 'default source')`  
`              +3 COPR `<COPYRIGHT_SOURCE_DATA>`           {0:1}  (Data item of the 'default source')`  
`          +1 DEST `<RECEIVING_SYSTEM_NAME>`               {0:1*} (Data item of the 'default source')`  
`          +1 DATE `<TRANSMISSION_DATE>`                   {0:1}  (Data item of the 'default source')`  
`            +2 TIME `<TIME_VALUE>`                        {0:1}  (Data item of the 'default source')`  
`          +1 SUBM @`<XREF:SUBM>`@                         {1:1}  (Data item of the 'default source')`  
`                                                               (Also used to determine the SUBMITTER_RECORD)`  
`                                                               (that should be stored as the database owner)`  
`          +1 SUBN @`<XREF:SUBN>`@                         {0:1}  (ignored)`  
`          +1 FILE `<FILE_NAME>`                           {0:1}  (Data item of the 'default source')`  
`          +1 COPR `<COPYRIGHT_GEDCOM_FILE>`               {0:1}  (stored as the Publication information of the 'default source')`  
`          +1 GEDC                                       {1:1}`  
`            +2 VERS `<VERSION_NUMBER>`                    {1:1}  (Data item of the 'default source')`  
`            +2 FORM `<GEDCOM_FORM>`                       {1:1}  (Data item of the 'default source')`  
`          +1 CHAR `<CHARACTER_SET>`                       {1:1}  (Data item of the 'default source')`  
`            +2 VERS `<VERSION_NUMBER>`                    {0:1}  (Data item of the 'default source')`  
`          +1 LANG `<LANGUAGE_OF_TEXT>`                    {0:1}  (Data item of the 'default source')`  
`          +1 PLAC                                       {0:1}`  
`            +2 FORM `<PLACE_HIERARCHY>`                   {1:1}  (see below)`  
`          +1 NOTE `<GEDCOM_CONTENT_DESCRIPTION>`          {0:1}  (note attached to the 'default source')`  
`            +2 [CONT|CONC] `<GEDCOM_CONTENT_DESCRIPTION>` {0:M}`  
`            `  
`   * NOTE: Submissions to the Family History Department for Ancestral`  
`     File submission or for clearing temple ordinances must use a`  
`     DESTination of ANSTFILE or TempleReady.`

The PLAC FORM is stored internally and used to govern the interpretation of places (in accordance with the GEDCOM specification).

###### SUBmissioN

The SUBMISSION_RECORD (there should be only one, but this is not checked) is stored as a item of the 'default source'

`    SUBMISSION_RECORD:=`  
`        n @`<XREF:SUBN>`@ SUBN                            {1:1]`  
`          +1 SUBM @`<XREF:SUBM>`@                         {0:1}`  
`          +1 FAMF `<NAME_OF_FAMILY_FILE>`                 {0:1}`  
`          +1 TEMP `<TEMPLE_CODE>`                         {0:1}`  
`          +1 ANCE `<GENERATIONS_OF_ANCESTORS>`            {0:1}`  
`          +1 DESC `<GENERATIONS_OF_DESCENDANTS>`          {0:1}`  
`          +1 ORDI `<ORDINANCE_PROCESS_FLAG>`              {0:1}`  
`          +1 RIN `<AUTOMATED_RECORD_ID>`                  {0:1}`

###### SUBMitter

SUBMITTER_RECORDs (there may be more than one) are stored as records attached to the 'default source' except as indicated in bold below. The SUBMITTER_RECORD that corresponds with the SUBM record in the HEADER is used to set the [database owner](wiki:Gramps_6.0_Wiki_Manual_-_Tools#Edit_Database_Owner_Information) and can be copied to the [Researcher Information](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Researcher) tab if required.

`   SUBMITTER_RECORD:=`  
`        n @`<XREF:SUBM>`@   SUBM                          {1:1}`  
`          +1 NAME `<SUBMITTER_NAME>`                      {1:1}`  
`          +1 <`<ADDRESS_STRUCTURE>`>                      {0:1}`  
`          `**`+1 <`<MULTIMEDIA_LINK>`> {0:M}`**  
`          `**`+1 LANG `<LANGUAGE_PREFERENCE>` {0:3}`**  
`          `**`+1 RFN `<SUBMITTER_REGISTERED_RFN>` {0:1}`**  
`          `**`+1 RIN `<AUTOMATED_RECORD_ID>` {0:1}`**  
`          +1 <`<CHANGE_DATE>`>                            {0:1}`

- Mutimedia link is ignored
- LANG is ignored
- RFN and RIN are ignored

##### INDIvidual

The INDIVIDUAL_RECORD is stored as a Gramps record, except as indicated in bold below.

`   INDIVIDUAL_RECORD: =`  
`        n @`<XREF:INDI>`@  INDI                           {1:1}`  
`          +1 RESN `<RESTRICTION_NOTICE>`                  {0:1}`  
`          +1 <`<PERSONAL_NAME_STRUCTURE>`>                {0:M}`  
`          +1 SEX `<SEX_VALUE>`                            {0:1}`  
`          +1 <`<INDIVIDUAL_EVENT_STRUCTURE>`>             {0:M}`  
`          `**`+1 <`<INDIVIDUAL_ATTRIBUTE_STRUCTURE>`> {0:M}`**  
`          +1 <`<LDS_INDIVIDUAL_ORDINANCE>`>               {0:M}`  
`          +1 <`<CHILD_TO_FAMILY_LINK>`>                   {0:M}`  
`          +1 <`<SPOUSE_TO_FAMILY_LINK>`>                  {0:M}`  
`          `**`+1 SUBM @`<XREF:SUBM>`@ {0:M}`**  
`          +1 <`<ASSOCIATION_STRUCTURE>`>                  {0:M}`  
`          +1 ALIA @`<XREF:INDI>`@                         {0:M}`  
`          `**`+1 ANCI @`<XREF:SUBM>`@ {0:M}`**  
`          `**`+1 DESI @`<XREF:SUBM>`@ {0:M}`**  
`          +1 <`<SOURCE_CITATION>`>                        {0:M}`  
`          +1 <`<MULTIMEDIA_LINK>`>                        {0:M}`  
`          +1 <`<NOTE_STRUCTURE>`>                         {0:M}`  
`          +1 RFN `<PERMANENT_RECORD_FILE_NUMBER>`         {0:1}`  
`          +1 AFN `<ANCESTRAL_FILE_NUMBER>`                {0:1}`  
`          +1 REFN `<USER_REFERENCE_NUMBER>`               {0:M}`  
`            `**`+2 TYPE `<USER_REFERENCE_TYPE>` {0:1}`**  
`          +1 RIN `<AUTOMATED_RECORD_ID>`                  {0:1}`  
`          +1 <`<CHANGE_DATE>`>                            {0:1}`  
`   `

- Link to submitter, ancestor interest and descendent interest indicators are silently ignored.
- The alias indicator ("An indicator to link different record descriptions of a person who may be the same person") is stored as an called 'Alias'.
- The REFN and REFN:TYPE are stored as of the , but if there is more than one REFN, it may not be clear which TYPE is associated with which REFN.

Handling of the INDIVIDUAL_ATTRIBUTE_STRUCTURE is rather complicated. The following tags:

- EDUC (Scholastic achievement),
- NMR (Count of marriages),
- OCCU (Occupation),
- PROP (Possessions),
- RELI (Religious affiliation),
- RESI and
- TITL (Nobility title)

are all treated as Gramps s and the associated information is stored in the event structure. The details following the main tag (shown in brackets in the list above) are stored as the of the . The <EVENT_DESCRIPTOR> following the TYPE tag will overwrite the if the <EVENT_DESCRIPTOR> is not the attribute name.

The following tags:

- CAST (Caste name),
- DSCR (Physical description),
- INDO (National ID Number),
- NATI (National or tribal origin),
- NCHI (Count of Children) and
- SSN (Social Security Number)

are all treated as Gramps s and most of the fields except the details following the main tag (shown in brackets in the list above), the source citation and the note structure are ignored, as indicated in bold below.

`   INDIVIDUAL_ATTRIBUTE_STRUCTURE: =`  
`        n  CAST `<CASTE_NAME>`                            {1:1}`  
`          +1 <`<EVENT_DETAIL>`>                           {0:1}`  
`             etc.`  
`   `  
`   EVENT_DETAIL: =`  
`        `**`n TYPE `<EVENT_DESCRIPTOR>` {0:1}`**  
`        `**`n DATE `<DATE_VALUE>` {0:1}`**  
`        `**`n <`<PLACE_STRUCTURE>`> {0:1}`**  
`        `**`n <`<ADDRESS_STRUCTURE>`> {0:1}`**  
`        `**`n AGE `<AGE_AT_EVENT>` {0:1}`**  
`        `**`n AGNC `<RESPONSIBLE_AGENCY>` {0:1}`**  
`        `**`n CAUS `<CAUSE_OF_EVENT>` {0:1}`**  
`        n  <`<SOURCE_CITATION>`>                          {0:M}`  
`          +1 <`<NOTE_STRUCTURE>`>                         {0:M}`  
`          +1 <`<MULTIMEDIA_LINK>`>                        {0:M}`  
`        `**`n <`<MULTIMEDIA_LINK>`> {0:M}`**  
`        n  <`<NOTE_STRUCTURE>`>                           {0:M}`  
`        `  
`        `

- Individual attribute structure, type, date, place structure, address structure, age, agency, cause and multimedia link are all ignored.

##### FAM_RECORD

The FAM_RECORD is stored as a Gramps record.

`   FAM_RECORD:=`  
`        n @`<XREF:FAM>`@   FAM                            {1:1}`  
`          +1 <`<FAMILY_EVENT_STRUCTURE>`>                 {0:M}`  
`          +1 HUSB @`<XREF:INDI>`@                         {0:1}`  
`          +1 WIFE @`<XREF:INDI>`@                         {0:1}`  
`          +1 CHIL @`<XREF:INDI>`@                         {0:M}`  
`          +1 NCHI `<COUNT_OF_CHILDREN>`                   {0:1}`  
`          +1 SUBM @`<XREF:SUBM>`@                         {0:M}`  
`          +1 <`<LDS_SPOUSE_SEALING>`>                     {0:M}`  
`          +1 <`<SOURCE_CITATION>`>                        {0:M}`  
`          +1 <`<MULTIMEDIA_LINK>`>                        {0:M}`  
`          +1 <`<NOTE_STRUCTURE>`>                         {0:M}`  
`          +1 REFN `<USER_REFERENCE_NUMBER>`               {0:M}`  
`            +2 TYPE `<USER_REFERENCE_TYPE>`               {0:1}`  
`          +1 RIN `<AUTOMATED_RECORD_ID>`                  {0:1}`  
`          +1 <`<CHANGE_DATE>`>                            {0:1}`

- The link to submitter is silently ignored.
- The REFN and REFN:TYPE are stored as of the , but if there is more than one REFN, it may not be clear which TYPE is associated with which REFN.

##### SOURCE_RECORD

The SOURCE_RECORD is stored as a Gramps record, except as indicated in bold below.

`   SOURCE_RECORD:=`  
`        n @`<XREF:SOUR>`@ SOUR                            {1:1}`  
`          `**`+1 DATA {0:1}`**  
`            `**`+2 EVEN `<EVENTS_RECORDED>` {0:M}`**  
`              `**`+3 DATE `<DATE_PERIOD>` {0:1}`**  
`              `**`+3 PLAC `<SOURCE_JURISDICTION_PLACE>` {0:1}`**  
`            `**`+2 AGNC `<RESPONSIBLE_AGENCY>` {0:1}`**  
`            `**`+2 <`<NOTE_STRUCTURE>`> {0:M}`**  
`          +1 AUTH `<SOURCE_ORIGINATOR>`                   {0:1}`  
`            +2 [CONT|CONC] `<SOURCE_ORIGINATOR>`          {0:M}`  
`          +1 TITL `<SOURCE_DESCRIPTIVE_TITLE>`            {0:1}`  
`            +2 [CONT|CONC] `<SOURCE_DESCRIPTIVE_TITLE>`   {0:M}`  
`          +1 ABBR `<SOURCE_FILED_BY_ENTRY>`               {0:1}`  
`          +1 PUBL `<SOURCE_PUBLICATION_FACTS>`            {0:1}`  
`            +2 [CONT|CONC] `<SOURCE_PUBLICATION_FACTS>`   {0:M}`  
`          +1 TEXT `<TEXT_FROM_SOURCE>`                    {0:1}`  
`            +2 [CONT|CONC] `<TEXT_FROM_SOURCE>`           {0:M}`  
`          +1 <`<SOURCE_REPOSITORY_CITATION>`>             {0:1}`  
`          +1 <`<MULTIMEDIA_LINK>`>                        {0:M}`  
`          +1 <`<NOTE_STRUCTURE>`>                         {0:M}`  
`          +1 REFN `<USER_REFERENCE_NUMBER>`               {0:M}`  
`            +2 TYPE `<USER_REFERENCE_TYPE>`               {0:1}`  
`          +1 RIN `<AUTOMATED_RECORD_ID>`                  {0:1}`  
`          +1 <`<CHANGE_DATE>`>                            {0:1}`

- DATA and its subsidiary records are ignored

##### REPOSITORY_RECORD

The REPOSITORY_RECORD is stored as a Gramps record, except as indicated in bold below.

`   REPOSITORY_RECORD: =`  
`        n @`<XREF:REPO>`@ REPO                            {1:1}`  
`          +1 NAME `<NAME_OF_REPOSITORY>`                  {0:1}`  
`          +1 <`<ADDRESS_STRUCTURE>`>                      {0:1}`  
`          +1 <`<NOTE_STRUCTURE>`>                         {0:M}`  
`          `**`+1 REFN `<USER_REFERENCE_NUMBER>` {0:M}`**  
`            `**`+2 TYPE `<USER_REFERENCE_TYPE>` {0:1}`**  
`          `**`+1 RIN `<AUTOMATED_RECORD_ID>` {0:1}`**  
`          +1 <`<CHANGE_DATE>`>                            {0:1}`

- REFN, REFN:TYPE and RIN are ignored

##### MULTIMEDIA_RECORD

The MULTIMEDIA_RECORD is stored as a Gramps record, except as indicated in bold below.

`   MULTIMEDIA_RECORD:=`  
`        n @`<XREF:OBJE>`@ OBJE                            {1:1}`  
`          +1 FORM `<MULTIMEDIA_FORMAT>`                   {1:1}`  
`          +1 TITL `<DESCRIPTIVE_TITLE>`                   {0:1}`  
`          +1 <`<NOTE_STRUCTURE>`>                         {0:M}`  
`          +1 <`<SOURCE_CITATION>`>                        {0:M}`  
`          `**`+1 BLOB {1:1}`**  
`            `**`+2 CONT `<ENCODED_MULTIMEDIA_LINE>` {1:M}`**  
`          +1 OBJE @`<XREF:OBJE>`@     /* chain to continued object */  {0:1}`  
`          `**`+1 REFN `<USER_REFERENCE_NUMBER>` {0:M}`**  
`            `**`+2 TYPE `<USER_REFERENCE_TYPE>` {0:1}`**  
`          `**`+1 RIN `<AUTOMATED_RECORD_ID>` {0:1}`**

- It is expected that there will be a 'FILE' tag to indicate the file holding the multimedia object. This usage is taken from GEDCOM 5.6.0, but the ability in GEDCOM 5.6.0 to have more than one <MUTIMEDIA_FILE_REFN> and having the FORM, TYPE and TITL subsidiary to the FILE gedcom_line is not supported (a later FILE may overwrite an earlier one - there is no error checking).
- BLOB is ignored
- REFN, REFN:TYPE and RIN are ignored

##### NOTE_RECORD

The NOTE_RECORD is stored as a Gramps record, except as indicated in bold below.

`   NOTE_RECORD:=`  
`        n @`<XREF:NOTE>`@ NOTE `<SUBMITTER_TEXT>`           {1:1}`  
`          +1 [ CONC | CONT] `<SUBMITTER_TEXT>`            {0:M}`  
`          `**`+1 <`<SOURCE_CITATION>`> {0:M}`**  
`          `**`+1 REFN `<USER_REFERENCE_NUMBER>` {0:M}`**  
`            `**`+2 TYPE `<USER_REFERENCE_TYPE>` {0:1}`**  
`          `**`+1 RIN `<AUTOMATED_RECORD_ID>` {0:1}`**  
`          +1 <`<CHANGE_DATE>`>                            {0:1}`

- source citation ignored
- REFN, REFN:TYPE and RIN are ignored

## Exportovanie údajov

Ak chcete exportovať údaje, vyberte položku Menu alebo [klávesová skratka](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings/sk#). alebo na počítačoch Apple Mac. Tým sa zobrazí dialógové okno .

Export vám umožňuje zdieľať akúkoľvek časť vášho rodinného stromu Gramps (databázy) s inými výskumníkmi, ako aj vám umožňuje preniesť vaše údaje na iný počítač.

Program Gramps dokáže exportovať údaje do nasledujúcich formátov súborov:

- [Comma Separated Values Spreadsheet (CSV)](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees#Comma_Separated_Values_Spreadsheet.28CSV.29_export)
- [GEDCOM](#GEDCOM_export)
- GeneWeb
- Gramps [XML](wiki:Gramps_XML) (rodokmeň)
- Gramps [XML](wiki:Gramps_XML) Balík (rodokmeň a médiá)
- Web Family Tree
- vCalendar
- vCard

{{-}}

### Dialógové okno Pomocník pri exporte

![[_media/ExportAssistant-SavingYourData-wizard-60.png|Obrázok {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Pomocník exportu: Uloženie údajov - úvodná stránka sprievodcu]]Stránky vás prevedú [výberom formátu výstupného súboru](#Vyberte_výstupný_formát) a potom možnosťami exportu špecifickými pre tento formát súboru. Po zobrazení stránky sa export vykoná podľa vami vykonaných volieb. Kedykoľvek môžete kliknúť na tlačidlo a opraviť akýkoľvek výber a potom prejsť ďalej a zopakovať export. {{-}}

#### Uloženie údajov

Všeobecné informácie o exporte z programu Gramps.

Ak chcete pokračovať, vyberte tlačidlo . {{-}}

#### Výber výstupného formátu

![[_media/ExportAssistant-ChooseTheOutputFormat-wizard-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Asistent exportu - výber výstupného formátu - dialógové okno sprievodcu]]Vyberte formát súboru, do ktorého chcete exportovať údaje:

- [Comma Separated Values Spreadsheet (CSV)](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees#Comma_Separated_Values_Spreadsheet.28CSV.29_export)
- [GEDCOM](#GEDCOM_export)
- GeneWeb
- **Gramps [XML](wiki:Gramps_XML) (rodokmeň)**(predvolené)
- Gramps [XML](wiki:Gramps_XML) Balík (rodokmeň a médiá)
- Web Family Tree
- vCalendar
- vCard

Potom vyberte tlačidlo a pokračujte. {{-}}

#### Možnosti exportu

![[_media/ExportAssistant-ExportOptions-CSV-defaults-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Asistent exportu - Možnosti exportu - dialógové okno sprievodcu (zobrazujúce predvolené nastavenia pre "Tabuľkový procesor s hodnotami oddelenými čiarkou(CSV)") so zvýraznenou spodnou časťou pre možnosti špecifické pre formát súboru]]

Po nastavení možností v týchto dvoch sekciách.

- Horná časť bez označenia: [Filtre a súkromie](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees#Filters_and_privacy)
- Spodná časť bez označenia: [Možnosti špecifického formátu súboru](wiki:Gramps_6.0_Wiki_Manuall_-_Manage_Family_Trees/sk#Možnosti_exportu_špecifického_formátu_súboru)

Ak chcete pokračovať, vyberte tlačidlo . {{-}}

##### Filtre a súkromie

Program Gramps umožňuje exportovať vybraný rodinný strom do bežných formátov súborov.

Nasledujúce filtre poskytujú možnosti, ktoré vám umožnia jemne doladiť váš export.

Filtre umožňujú exportovať obmedzené množstvo údajov na základe zvolených kritérií.

###### Filter súkromia:

  
Začiarknite toto políčko, aby sa do exportovaného súboru nezahrnuli súkromné záznamy. (Štandardne je políčko začiarknuté)

###### Životný filter:

Táto možnosť obmedzuje údaje a pomáha obmedziť exportované informácie o žijúcich osobách. To znamená, že všetky informácie týkajúce sa ich narodenia, úmrtia, adresy, významných udalostí atď. budú v exportovanom súbore vynechané. Môžete sa napríklad rozhodnúť nahradiť slovo **Žijúci** krstným menom (pozrite si svoje [nastavenia](wiki:Gramps_6.0_Wiki_Manual_-_Settings/sk#Text)); môžete vylúčiť poznámky; a môžete vylúčiť zdroje pre [živých ľudí](wiki:Gramps_6.0_Wiki_Manual_-_Probably_Žijúci).

Niekedy nie je z údajov vždy zrejmé, či je niekto skutočne nažive. Gramps používa pokročilý algoritmus, ktorý sa snaží určiť [či by osoba mohla byť ešte nažive](wiki:Gramps_6.0_Wiki_Manuál_-_Pravdepodobne_Žijúci). Pamätajte, že Gramps robí svoj najlepší odhad a nemusí sa mu vždy podariť odhadnúť to správne. Svoje údaje si prosím dvakrát skontrolujte.

Vyberte si z nasledujúcich možností:

- (predvolené)

- 

- 

- 

###### Filter ľudí:

Vyberte z nasledujúcich možností:

- (predvolené)

- }

- }

- 

- 

- Vytvorte vlastný filter výberom ikony *Upraviť*, čím zobrazíte dialógové okno .

###### Filter poznámky:

Vyberte si z nasledujúcich možností:

- (predvolené)

- Vytvorte vlastný filter výberom ikony *Upraviť*, čím zobrazíte dialógové okno .

###### Referenčný filter:

Vyberte si z nasledujúcich možností:

- (predvolené)

- 

##### Možnosti exportu špecifické pre formát súboru

V závislosti od zvoleného formátu súboru môžete nájsť niekoľko možností exportu špecifických pre daný formát súboru, z ktorých si môžete vybrať a ktoré sú uvedené pod oddielom "Filtre a ochrana osobných údajov".

Pozrite si príslušnú časť pre každý z uvedených formátov súborov, ktoré majú špecifické možnosti exportu:

- [Comma Separated Values Spreadsheet (CSV)](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees/sk#Comma_Separated_Values_Spreadsheet.28CSV.29_export)
- [Gramps XML (rodokmeň)](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees/sk#Gramps_XML_.28family_tree.29_export)

#### Vyberte súbor na uloženie

![[_media/ExportAssistant-SelectSaveFile-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Asistent exportu - výber súboru na uloženie - dialógové okno sprievodcu - príklad]]

Zadajte exportný súbor <kód>Názov_1.<prípona formátu súboru></kód>(predvolené) a vyberte umiestnenie priečinka, do ktorého sa má exportný súbor uložiť (zvyčajne je to váš priečinok **Dokumenty**.

Potom vyberte tlačidlo a pokračujte.

Ak nemáte povolenie na uloženie súboru do tohto umiestnenia, zobrazí sa varovné dialógové okno a potom dialógové okno Sprievodca exportom Asistenti , vyberte tlačidlo a spustite export znova, tentoraz výberom vhodného priečinka. {{-}}

#### Záverečné potvrdenie

![[_media/ExportAssistant-FinalConfirmation-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Asistent exportu - konečné potvrdenie - dialógové okno sprievodcu - príklad]]

Dialógové okno sprievodcu Asistentom exportu umožňuje skontrolovať súhrnné údaje (Formát/Názov/Priečinok) vytváraného exportného súboru.

V tomto okamihu môžete stlačiť na opätovnú kontrolu možností alebo na prerušenie.

Alebo vyberte tlačidlo , ak chcete pokračovať. {{-}}

#### Súhrn

![[_media/ExportAssistant-YourDataHasBeenSaved-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Asistent exportu - Súhrn - dialógové okno sprievodcu - príklad]]

V dialógovom okne sprievodcu Asistentom exportu sa zobrazí *Názov súboru:* a potvrdí sa, že exportované údaje boli úspešne uložené.

Výberom tlačidla ukončíte okno Pomocník exportu. {{-}}

### Export tabuľky s hodnotami oddelenými čiarkou (CSV)

=

![[_media/ExportAssistant-ExportOptions-CSV-defaults-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Asistent exportu - Možnosti exportu - dialógové okno sprievodcu (zobrazujúce predvolené nastavenia pre "Tabuľkový procesor s hodnotami oddelenými čiarkou(CSV)") so zvýraznenou spodnou časťou pre možnosti špecifické pre formát súboru]]

Tabuľka s hodnotami oddelenými čiarkami(CSV): Umožňuje exportovať (a importovať) podmnožinu údajov programu Gramps v jednoduchom tabuľkovom formáte.

Pozri [Import a export CSV](wiki:Gramps_6.0_Wiki_manuál_-_Správa_rodokmeňov:_Import_a_export_CSV), kde nájdete ďalšie informácie a príklady.

Tabuľka s tabuľkami oddelenými čiarkami(CSV) má nasledujúce [Možnosti exportu špecifické pre formát súboru](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees/sk#Možnosti_exportu_špecifického_formátu_súboru):

- Zahrnúť ľudí -
- Zahrnúť manželstvá -
- Zahrnúť deti -
- Zahrnúť miesta -
- Preložiť záhlavia -

{{-}} Pozrite si tiež [Export (List) View](wiki:Gramps_6.0_Wiki_Manual_-_Settings/sk#Export_View) ako tabuľkový procesor.

### Export GEDCOM

.

Program Gramps umožňuje exportovať databázu do bežného staršieho formátu .

Export nemá žiadne [file format specific export options](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees/sk#File_format_specific_export_options), ale môžete zmeniť nasledujúce možnosti:

- Uistite sa, že ste pridali svoje informácie, aby ste vytvorili platný súbor GEDCOM, môžete to urobiť aj pomocou nástroja .

<!-- -->

- V [Všeobecné nastavenia programu Gramps](wiki:Gramps_6.0_Wiki_Manual_-_Settings/sk#Všeobecné) v časti General (Všeobecné nastavenia) na karte Predvoľby môžete tiež zvoliť a tiež Obe môžu výrazne spomaliť import vašich údajov.

Viac informácií o formáte GEDCOM nájdete na: :

- <https://en.wikipedia.org/wiki/GEDCOM>
- <https://www.familysearch.org/developers/docs/guides/gedcom>
- <https://www.familysearch.org/developers/docs/gedcom/>

Podrobnosti o údajoch, ktoré sa pri exporte do formátu GEDCOM neexportujú, nájdete v časti [Gramps a GEDCOM](wiki:Gramps_a_GEDCOM) (). {{-}}

### Export do GeneWebu

export uloží kópiu vašich údajov do genealogického formátu GeneWeb.

Viac informácií o GeneWeb a jeho formáte nájdete na stránke:

- <http://www.geneweb.org>

nemá žiadne [možnosti exportu špecifického formátu súboru](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees/sk#Možnosti_exportu_špecifického_formátu_súboru) {{-}}

### Gramps XML (rodinný strom) export

![[_media/ExportAssistant-ExportOptions-GrampsXMLFamilyTree-defaults-60.png|Fig. {{#var:chapter}}.{{#var:figure|{{#expr:{{#var:figure}}+1}}}} Pomocník pri exporte - Možnosti exportu - sprievodca (zobrazujúci predvolené nastavenia pre "Gramps XML (rodokmeň)") so zvýraznenou spodnou časťou pre Možnosti špecifického formátu súboru]]

export (.gramps): Tento formát je štandardným formátom na výmenu údajov a zálohovanie (pozri súvisiaci formát .gpkg nižšie pre úplnú prenosnosť vrátane mediálnych objektov). Exportom do formátu Gramps [XML](wiki:XML) sa vytvorí prenosná databáza. Keďže XML je textový formát čitateľný človekom, môžete ho použiť aj na nahliadnutie do svojich údajov. Program Gramps zaručuje, že výstup XML starších verzií programu Gramps môžete otvoriť v novšej verzii programu Gramps (nie však naopak!).

Ak sa pri exporte nenájde mediálny súbor, zobrazí sa rovnaké dialógové okno , s akým sa stretávate pri exporte GEDCOM.

má nasledujúce [možnosti exportu špecifické pre formát súboru](wiki:Gramps_6.0_Wiki_Manuál_-_Správa_Rodokmeňov#Možnosti_exportu_špecifického_formátu_súboru):

- Použiť kompresiu -

{{-}}

#### Čo nie je zahrnuté:

### Export balíka Gramps XML (rodinný strom a médiá)

export (.gpkg): Export do formátu balíka Gramps vytvorí komprimovaný súbor, ktorý obsahuje databázu Gramps XML a kópie všetkých súvisiacich mediálnych súborov. Je to užitočné, ak chcete databázu preniesť na iný počítač alebo ju s niekým zdieľať.

Ak sa mediálny súbor počas exportu nenájde, zobrazí sa rovnaké dialógové okno , s akým sa stretávate pri exporte GEDCOM.

nemá žiadne [možnosti exportu špecifické pre formát súboru](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees/sk#Možnosti_exportu_špecifické_pre_formát_súboru)

#### Čo nie je súčasťou:

### Export Web Family Tree

export vytvorí textový súbor, ktorý môže byť použitý programom **Web Family Tree**.

Ak sa chcete dozvedieť viac o programe Web Family Tree a jeho formáte, navštívte stránku

- [`http://www.simonward.com/cgi-bin/page.pl?family/tree`](http://www.simonward.com/cgi-bin/page.pl?family/tree) - [linkrot](https://wikipedia.org/wiki/Link_rot). *pozri* [2016 **Internet Archive** snímka](https://web.archive.org/web/20160316080343/http://www.simonward.com/cgi-bin/page.pl?family/tree).

nemá [možnosti exportu špecifické pre formát súboru](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees/sk#File_format_specific_export_options) {{-}}

### Export vCalendar

export ukladá informácie vo formáte používanom v mnohých aplikáciách na tvorbu kalendárov, niekedy nazývanom PIM pre Personal Information Manager.

Viac informácií o formáte vCalendar nájdete na:

- <https://en.wikipedia.org/wiki/ICalendar#vCalendar_1.0>

nemá žiadne [možnosti exportu špecifické pre formát súboru](wiki:Gramps_6.0_Wiki_Manuál_-_Manage_Family_Trees/sk#Možnosti_exportu_špecifického_formátu_súboru) {{-}}

### Export vCard

export ukladá informácie vo formáte používanom v mnohých aplikáciách adresárov, niekedy nazývanom PIM pre Personal Information Manager.

Viac informácií o formáte vCard nájdete na stránke:

- <https://en.wikipedia.org/wiki/VCard>

nemá žiadne [možnosti exportu špecifické pre formát súboru](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees/sk#Možnosti_exportu_špecifického_formátu_súboru) {{-}}

[Category:Sk/Documentation](wiki:Category:Sk/Documentation)
