---
title: 'Gramps 6.0 Wiki Manual - Entering and editing data: detailed - part 1/sk'
categories:
- Sk:Documentation
- Stub
managed: false
source: wiki-scrape
wiki_revid: 120919
wiki_fetched_at: '2026-05-30T20:03:05Z'
lang: sk
---

{{#vardefine:chapter\|9.1}} {{#vardefine:figure\|0}} Táto časť rozširuje [stručný prehľad](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_brief/sk) o tom, ako zadávať a upravovať údaje v programe Gramps.

Program Gramps vám ponúka sériu Pohľadov. Každý z týchto Pohľadov vám poskytuje možnosti na zadávanie a úpravu informácií. V skutočnosti sa často môžete dostať k tým istým informáciám z rôznych Pohľadov.

V programe Gramps sa informácie zadávajú a upravujú prostredníctvom tzv. dialógových okien. Keďže tento termín používame často, mali by sme definovať, čo tým myslíme:

Dialógové okno je vyskakovacie okno, ktoré poskytuje jeden alebo viacero formulárov na zadávanie a úpravu údajov, ktoré patria do určitej kategórie. Medzi príklady v programe Gramps patrí dialógové okno a , okrem mnohých iných.

Dialógové okno často obsahuje sériu "kariet poznámkového bloku", ktoré zoskupujú informácie do podkategórií. Napríklad dialógové okno má okrem iného karty poznámkového bloku pre podkategórie, ako sú Udalosti, Atribúty, Adresy a Poznámky.

## Úprava informácií o ľuďoch

Informácie o ľuďoch sa zadávajú a upravujú prostredníctvom dialógového okna }. Toto dialógové okno možno vyvolať z rôznych Zobrazení nasledujúcimi spôsobmi:

- Z [Kategória_ľudí](wiki:Gramps_6.0_Wiki_Manuál_-_Navigácia#Použitie_kategórie_ľudí):

  
  
Dvakrát kliknite na meno osoby, ktorej údaje chcete upraviť

Vyberte meno jedným kliknutím a potom kliknite na tlačidlo na paneli nástrojov.

Vyberte meno a potom stlačte **Enter**' .

Vyberte položku Upraviť... z ponuky Úpravy v časti Dedina

Vyberte položku Upraviť z kontextovej ponuky, ktorá sa zobrazí po kliknutí pravým tlačidlom myši na meno.

- Z [kategórie_vzťahov](wiki:Gramps_6.0_Wiki_Manuál_-_Navigácia#Použitie_kategórie_vzťahov): Ak chcete upraviť údaje Aktívnej osoby, kliknite na tlačidlo vedľa mena Aktívnej osoby.

<!-- -->

- Z [kategórie_gramov](wiki:Gramps_6.0_Wiki_Manual_-_Navigácia#Používanie_kategórie_gramov): Dvakrát kliknite do poľa s menom osoby, ktorej údaje chcete upraviť.

Ktorýkoľvek z týchto spôsobov vám ponúkne dialógové okno . {{-}}

### Dialógové okno Úprava osoby

![[_media/Edit-person-window-new-person-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Upraviť osobu - okno - Predvolený nový prázdny editor]]

![[_media/Edit-person-window-existing-person-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Dialógové okno  - zobrazenie príkladu osoby]]

V dialógovom okne sa pridávajú informácie o novej osobe alebo sa upravujú informácie o existujúcej osobe.

Horná časť okna má dve časti: Základné informácie o osobe a časť s tlačidlom súkromia (na nastavenie záznamu ako súkromného), výberom pohlavia, identifikátorom, ktorý môžete tomuto záznamu priradiť, a značkou, ktorú môžete priradiť osobe a ktorá označuje stav záznamu (dokončený, TODO, neistý, ....), čo tomuto záznamu dodá špecifickú farbu v zobrazení osoby.

Pomocou kontextovej ponuky(kliknutím pravým tlačidlom myši) z prázdnej oblasti v hornej časti okna, napr:v blízkosti poľa "Preferované meno", sa vám zobrazí kontextová ponuka troch možností:

- \-

- \-

- sú k dispozícii prehľady.

Pod touto hornou časťou sa nachádza niekoľko "[tabuliek](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1/sk#Editácia_osoby_stránky)" obsahujúcich rôzne kategórie dostupných informácií. Kliknutím na ľubovoľnú kartu zobrazíte a upravíte jej obsah.

Kliknutím na tlačidlo v spodnej časti sa použijú všetky zmeny vykonané vo všetkých kartách a dialógové okno sa zatvorí. Kliknutím na tlačidlo sa okno zatvorí bez uplatnenia akýchkoľvek zmien.

{{-}} ![[_media/SaveChanges-alert-dialog-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;Uložiť zmeny?&quot; - dialógové okno s upozornením]]

Ak boli zmenené údaje v ktorejkoľvek karte, zobrazí sa } okno s upozornením, ktoré vás vyzve na výber z nasledujúcich možností:

- *Zatvoriť bez uloženia* - zmeny.
- **Zrušiť** (predvolené) - pôvodná požiadavka na zrušenie.
- *Uložiť* - zmeny.

ako aj začiarkávacie políčko na označenie možnosti *Nežiadať znova*. Taktiež sa dá vypnúť z možnosti } v dialógovom okne [Predvoľby &gt; Upozornenia](wiki:Gramps_6.0_Wiki_Manual_-_Settings/sk#Upozornenia).

### Sekcia preferovaných názvov

![[_media/EditPerson-PreferredName-section-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Sekcia "Preferované meno" (zvýraznená žltou farbou) dialógového okna "Upraviť osobu" - príklad]]

Uprednostňované alebo predvolené meno je meno, ktoré sa použije v gramatike pre '[meno](wiki:Mená_v_gramatike)" osoby. V [Gramps Preferences](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Display) môžete nastaviť, ako sa bude meno zobrazovať, a vo všeobecnosti stačí, ak údaje vložíte do polí zobrazených v časti preferované meno.

Iba v podrobných zostavách (textových a v generátore naratívnych webových stránok) sa zobrazujú aj alternatívne názvy. Všimnite si však, že pri vyhľadávaní mena sa budú vyhľadávať všetky mená pripojené k osobe, nielen preferované meno.

Sekcia preferovaného mena obsahuje typické informácie o mene, ktoré budete upravovať pri vytváraní osoby. Na zníženie neprehľadnosti sú menej často potrebné polia (pre Viacnásobné priezviská a Alternatívne mená) predvolene skryté. Ak chcete rozbaliť sekciu pre Viacnásobné priezviská, kliknite na tlačidlo   alebo použite jej [keybinding](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings#Editor_bindings). Ak chcete zobraziť celý rozsah údajov, ktoré môžete o názve uložiť, kliknite na tlačidlo   v pravom dolnom rohu sekcie alebo použite jeho [klávesovú skratku](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings/sk#Editor_bindings/sk). Tým sa zobrazí [Editor_názvu](wiki:Gramps_6.0_Wiki_Manuál_-_Zadávanie_a_editácia_údajov:_detail_-_časť_3#Editor_názvu).

Polia preferovaného mena v sú:

- mena. Medzi preddefinované typy patria: Známe aj ako, **Rodné meno** *(predvolené)*, Manželské meno, Neznáme. Do tohto vstupného poľa môžete tiež prepísať a vytvoriť si vlastné [Vlastné typy](wiki:Gramatika_Glosár#vlastné). (napr. prezývka, krátke meno atď.).

  
Odporúča sa, aby preferované meno bolo registrované rodné meno alebo iné meno s právnou subjektivitou. Sú to mená, ktoré sa budú najčastejšie vyskytovať v citovateľných dokumentoch. Na karte Editora môžete uložiť aj iné typy mien.

- , krstné meno (mená) osoby

- , voliteľná prípona k menu, napríklad *Jr.* alebo *III*

- , časť mena osoby označujúca rodinu, do ktorej osoba patrí.

  - Výberom tlačidla   tlačidlo, zobrazí sa pole pre zadanie časti, ktoré vám umožní zadať zložené priezviská (napríklad pre patronymické alebo zložené matrilineárno-patrilineárne mená)

- , voliteľná predpona pre priezvisko, ktorá sa nepoužíva pri triedení, napríklad *de* alebo *van*

- , typ [pôvod](wiki:Gramps_Glossary#name_origin) mena identifikuje kultúrny systém pomenovania, ktorý určuje, ako bolo zvolené konkrétne priezvisko. Ide o metainformáciu o priezvisku, ktorá môže byť dôležitá pri genealogickom výskume.

- , čo je titul (zvyčajne v skrátenej podobe) používaný na označenie osoby, napríklad *Dr.* alebo *Páter*, selektor,

- , je opisné meno uvedené namiesto oficiálneho mena alebo ako doplnok k nemu. Ak je Nick name konštrukcia celého mena, namiesto poľa Nick použite špecifický typ mena *Also known as* (tiež známy ako).

- , oficiálne je to časť daného mena, ktorá je bežne používaným menom. Napr. osoba môže mať 3 krstné mená, ako v prípade *Jean Baptiste Jules*, pričom v skutočnosti sa používa len *Baptiste*. V Nemecku a na niektorých iných miestach bolo zvykom medzi rôznymi krstnými menami podčiarknuť krstné meno, pozri tiež [zde](wiki:Mená_v_gramoch#Krstné_meno). Niektorí ľudia sa pokúsia použiť toto pole aj pre prezývku alebo zmenu krstného mena (napríklad Cristy pre Cristinu), ale toto nie je zamýšľané použitie. Volacie meno je vlastné zákonné meno. Pre prezývky alebo krátke varianty mien by ste mali vytvoriť alternatívne meno s iným typom.

V [Name Editor](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_3#Name_Editor) je k dispozícii ďalšie pole: . Ide o neoficiálny názov, ktorý sa dáva odštiepeneckej skupine rodiny, aby sa odlíšila od ľudí s rovnakým priezviskom. Často sa označuje ako názov farmy a zvyčajne odkazuje na miesto, kde odštiepená skupina býva alebo odkiaľ pochádza. (alias sept, sekta, tábor)

Polia a poskytujú funkciu "automatického dopĺňania": pri písaní do týchto polí sa pod poľom zobrazí ponuka obsahujúca záznamy z databázy, ktoré zodpovedajú vášmu čiastočnému vstupu. To vám umožní vybrať záznam, ktorý už v databáze existuje, namiesto toho, aby ste ho museli celý napísať. Záznam môžete vybrať pomocou myši alebo pomocou klávesov so šípkami a **Enter**.

{{-}}

### Viacnásobné priezviská

![[_media/EditPerson-top-sections-highlighted-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Sekcia "Viacnásobné priezviská" (zvýraznená modrou farbou) dialógového okna "Upraviť osobu" - príklad]]

Po stlačení tlačidla pridať sa zobrazí nové vstupné pole sekcie , ktoré umožňuje zadávať zložené priezviská.

Funkcia Viacnásobné priezviská sa môže použiť pre patronymické alebo zložené matrilineárno-patrilineárne mená. Ďalšou variantou by bolo škandinávske meno ako "Syver Ericksen Skotterud", kde sa celé meno skladá z krstného mena (Syver), odkazu na jeho otca (Ericksen alebo syn Erick) spolu s názvom obce alebo lokality. V takomto prípade môžete pridať "Ericksen" s [Origin](wiki:Names_in_Gramps#Origin_Attributes) "Patronymic" a rozšíriť na viacnásobné priezvisko pridaním "Skotterud" s pôvodom "Location".

Ak do tejto časti nepridáte žiadne informácie, pri ďalšom otvorení dialógového okna Upraviť osobu bude skrytá. Akékoľvek prázdne riadky sa neuložia.

{{-}}

### Všeobecné

![[_media/EditPerson-General-section-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Časť "Všeobecné" dialógového okna "Upraviť osobu" - príklad]]

- Ponuka ponúka výber pohlavia osoby :
  - 

  - 

  - (Predvolené)

<!-- -->

- V poli sa zobrazuje identifikačné číslo Gramps, ktoré jednoznačne identifikuje používateľa v rodinnom strome. Táto hodnota pomáha rozlišovať medzi ľuďmi, ktorí majú rovnaké meno. Môžete zadať ľubovoľnú jedinečnú hodnotu. Ak hodnotu neuvediete, Gramps automaticky vyberie hodnotu za vás.

<!-- -->

- V oblasti sa zobrazujú vami priradené vlastné značky, ktoré určujú niektoré základné informácie o stave vášho výskumu.
  - Tlačidlo vyvolá dialógový zoznam, ktorý vám umožní odstrániť alebo priradiť existujúce vlastné značky.

<!-- -->

- Tlačidlo vám umožňuje označiť, či sa záznam osoby považuje za súkromný alebo nie.

{{-}}

### Predvolený obrázok

![[_media/EditPerson-top-sections-image-with-context-menu-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Sekcia "Obrázok" (zvýraznená červenou farbou) dialógového okna "Úprava osoby" - príklad]]

Ak existujú nejaké obrázky, editor osoby zobrazí dodatočnú oblasť v ľavej hornej oblasti (inak je skrytá). Táto oblasť zobrazuje prvý obrázok dostupný v tejto osoby. {{-}}

### Stránky s kartou Upraviť osobu

Karty odrážajú nasledujúce kategórie osobných údajov:

#### Udalosti

![[_media/EditPerson-Events-tab-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Karta "Udalosti" z dialógového okna "Upraviť osobu" - príklad]]

  
Karta umožňuje zobraziť a upraviť všetky udalosti, ktoré sa týkajú danej osoby. V spodnej časti okna sa nachádza zoznam všetkých takýchto udalostí uložených v databáze a zobrazujú sa v ňom nasledujúce stĺpce: `Typ, Popis, Dátum, Miesto, Hlavní účastníci, Súkromné(ikona zámku), Úloha, ID, Vek`. V hornej časti sa zobrazujú podrobnosti o aktuálne vybranej udalosti v zozname (ak existuje). Tlačidlá , a umožňujú pridať, upraviť a odstrániť záznam o udalosti z databázy. Všimnite si, že tlačidlá a sú dostupné len vtedy, keď je udalosť vybraná zo zoznamu.

<!-- -->

  
Keď použijete tlačidlo , zobrazí sa dialógové okno , ktoré vám umožní vybrať už existujúcu udalosť a upraviť ju v dialógovom okne .

<!-- -->

  
Keď pridáte novú udalosť alebo upravíte existujúcu udalosť, vyvolá sa dialógové okno . Dialógové okno je opísané v [sekcia Odkaz na_udalosť](wiki:Gramps_6.0_Wiki_Manuál_-_Vkladanie_a_editácia_údajov:_podrobne_-_časť_2#Editácia_odkazov_na_udalosti).

{{-}}

##### Vyberte selektor udalostí

![[_media/SelectEvent-selector-dialog-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Výber udalosti - selektor - príklad]]

Dialógové okno selektor umožňuje prepojiť sa s už existujúcou udalosťou a po jej výbere sa otvorí v dialógovom okne .

Zobrazujú sa nasledujúce stĺpce: Typ(predvolené triedenie pre zoznam), Hlavní účastníci, Dátum, Miesto, Popis, ID, Posledná zmena.

Pomocou tlačidla môžete zoznam filtrovať na základe jednej z možností z rozbaľovacieho zoznamu:

- **Typ obsahuje** (predvolené nastavenie)
- *Typ neobsahuje*
- *Hlavní účastníci obsahuje*
- *Hlavní účastníci neobsahuje*
- *Dátum obsahuje*
- *Dátum neobsahuje*
- *Miesto obsahuje*
- *Miesto neobsahuje*
- *Popis obsahuje*
- *Opis neobsahuje*
- *ID obsahuje*
- *ID neobsahuje*
- *Posledná zmena obsahuje*
- *Posledná zmena neobsahuje*

{{-}}

#### Mená

![[_media/EditPerson-Names-tab-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Záložka "Mená" z dialógového okna "Upraviť osobu" - príklad]]

  
Karta { umožňuje zobraziť a upraviť všetky alternatívne mená, ktoré osoba môže mať. V spodnej časti okna sa nachádza zoznam všetkých alternatívnych mien osoby uložených v databáze. V hornej časti sa zobrazujú podrobnosti o aktuálne vybranom mene v zozname (ak existuje). Tlačidlá , a umožňujú pridanie, úpravu a odstránenie alternatívneho mena z databázy. Všimnite si, že tlačidlá Upraviť a - sa sprístupnia len vtedy, keď je náhradný názov vybraný zo zoznamu.

<!-- -->

  
Pri pridávaní nového názvu alebo úprave existujúceho názvu sa vyvolá dialógové okno . Toto dialógové okno Názvy je opísané v časti [Upravovač_názov](wiki:Gramps_6.0_Wiki_Manuál_-_Zadávanie_a_úprava_údajov:_Podrobne_-_časť_3#Dialógové_okno_Názvy).

{{-}}

#### Zdroje Citácie

![[_media/EditPerson-SourceCitations-tab-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Záložka "Citácie zdrojov" z dialógového okna "Upraviť osobu" - príklad]]

  
Karta vám umožňuje zobraziť a zdokumentovať citácie zdrojov informácií, ktoré ste zhromaždili.

<!-- -->

  
Môže ísť o všeobecné zdroje, ktoré nepopisujú konkrétnu udalosť, ale napriek tomu poskytujú informácie o osobe. Napríklad, ak sa v spomienkach tety Marty spomína jej pravnuk Paul, bádateľ môže predpokladať, že tento Paul skutočne existoval a citovať spomienky tety Marty ako zdroj, ktorý tento predpoklad odôvodňuje.

  
V strednej časti sa zobrazuje zoznam všetkých zdrojových odkazov uložených v databáze vo vzťahu k osobe. Tlačidlá , a umožňujú zodpovedajúcim spôsobom pridať, upraviť a odstrániť zdrojový odkaz na túto osobu. Všimnite si, že tlačidlo a sú k dispozícii len vtedy, keď je v zozname vybraný odkaz na zdroj.

<!-- -->

  
Pri úprave môžete meniť údaje v citácii (jedinečné pre túto osobu), ako aj zdieľaný objekt zdroja, pozri [Editácia citácií](wiki:Gramps_6.0_Wiki_Manuál_-_Vkladanie_a_editácia_údajov:_podrobne_-_časť_2#Editácia_citácií_zdroja).

{{-}}

#### Atribúty

![[_media/EditPerson-Attributes-tab-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Záložka "Atribúty" z dialógového okna "Upraviť osobu" - príklad]]

  
Karta umožňuje zobraziť a priradiť osobe atribúty. Máte úplnú voľnosť pri definovaní a používaní atribútov. Atribúty môžete priradiť napríklad na opis fyzických vlastností osoby alebo jej osobnostných vlastností.

<!-- -->

  
Všimnite si, že každý atribút uvedený v dialógovom okne sa skladá z dvoch častí: samotného atribútu a hodnoty priradenej k tomuto atribútu. Toto takzvané párovanie "Parameter - Hodnota" vám môže pomôcť pri organizácii a systematizácii vášho výskumu. Ak napríklad definujete "Farba vlasov" ako Atribút pre osobu, "Farba vlasov" sa stane vyberateľným Atribútom pre všetky ostatné osoby. Hodnota Farby vlasov pre osobu A môže byť červená a pre osobu B hnedá. Podobným spôsobom môžete definovať Atribút ako "Veľkorysosť" a použiť Hodnotu "Obrovská" na opis mimoriadne štedrej osoby.

<!-- -->

  
V spodnej časti dialógového okna sa zobrazí zoznam všetkých Atribútov uložených v databáze. V hornej časti sa zobrazujú podrobnosti o aktuálne vybranom atribúte v zozname (ak existuje). Tlačidlá , a umožňujú pridať, upraviť a odstrániť záznam atribútu z databázy. Všimnite si, že tlačidlá **Upraviť**' a **-**' sú dostupné len vtedy, keď je atribút vybraný zo zoznamu.

Ak upravujete atribút, otvorí sa .

{{-}}

#### Adresy

![[_media/EditPerson-Addresses-tab-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Karta "Adresy" z dialógového okna "Upraviť osobu" - príklad]]

  
Karta { umožňuje zobraziť a zaznamenať rôzne poštové adresy osoby. Na uloženie informácií o bydlisku osoby sa odporúča použiť udalosť bydliska. Karta adresy sa ponúka hlavne kvôli kompatibilite so štandardom GEDCOM, kde je zdôvodnenie adries len poštové.

<!-- -->

  
V spodnej časti okna sa nachádzajú adresy uložené pre danú osobu v databáze. V hornej časti sa zobrazujú podrobnosti o aktuálne vybranej adrese v zozname (ak existuje). Tlačidlá , a umožňujú zodpovedajúcim spôsobom pridať, upraviť a odstrániť záznam adresy z databázy. Všimnite si, že tlačidlá a sú dostupné len vtedy, keď je adresa vybraná zo zoznamu.

  
Ak upravujete adresu, otvorí sa .

<!-- -->

  
Niektoré zostavy umožňujú obmedziť údaje o žijúcich osobách. Táto možnosť vynechá najmä ich adresy.

{{-}}

#### Poznámky

![[_media/EditPerson-Notes-tab-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Karta "Poznámky" z dialógového okna "Upraviť osobu" - príklad]]

  
Karta { poskytuje miesto na zaznamenávanie rôznych položiek o osobe, ktoré sa nedajú prehľadne zaradiť do iných kategórií, ako aj úryvkov textu, ktoré chcete pridať do rodinného stromu. Poznámky môžete zdieľať medzi rôznymi záznamami v programe Gramps. Panel ikon na tejto karte ponúka obvyklé tlačidlá: , , , a tlačidlá na zmenu poradia poznámok.

<!-- -->

  
Ak upravíte poznámku, získate }.

{{-}}

##### Vyberte selektor poznámok

![[_media/SelectNote-selector-dialog-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Poznámka k výberu - selektor - príklad]]

Dialógové okno selektor umožňuje prepojenie na už existujúcu poznámku.

Zobrazujú sa nasledujúce stĺpce: Náhľad(predvolené triedenie pre zoznam), ID, Typ, Značky, Posledná zmena.

Pomocou tlačidla môžete zoznam filtrovať na základe jednej z možností z rozbaľovacieho zoznamu:

- **Náhľad obsahuje** (predvolené nastavenie)
- *Náhľad neobsahuje*
- *ID obsahuje*
- *ID neobsahuje*
- *Typ obsahuje*
- *Typ neobsahuje*
- *Značky obsahuje*
- *Značky neobsahuje*
- *Posledná zmena obsahuje*
- *Posledná zmena neobsahuje*

{{-}}

#### Galéria

![[_media/EditPerson-Gallery-tab-example-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Záložka "Galéria" z dialógového okna "Upraviť osobu" - príklad]]

  
Záložka { umožňuje zobrazovať a ukladať fotografie, videá a iné mediálne objekty, ktoré sú spojené s osobou. V strednej časti okna sa nachádza zoznam všetkých takýchto mediálnych objektov. Každý objekt vo forme platného obrazového súboru spôsobí zobrazenie miniatúry obrázka. V prípade iných objektov, ako sú zvukové súbory, filmové súbory atď. sa namiesto nich zobrazí ikona príslušného typu súboru.

<!-- -->

  
K dispozícii sú nasledujúce možnosti:

- \- umožňuje pridať nový mediálny objekt z .

- \- vyvolá dialógové okno } selektora, ktoré vám umožní odkazovať na už existujúci mediálny objekt.

- \- umožňuje upraviť vybraný mediálny objekt v . Toto tlačidlo sa sprístupní len vtedy, keď je zo zoznamu vybraný mediálny objekt.

- \- odstráni vybraný mediálny objekt z galérie osôb. Toto tlačidlo sa sprístupní len vtedy, keď je mediálny objekt vybraný zo zoznamu.

Poradie primárneho (aktívneho) obrázka môžete zmeniť tak, že ho vyberiete a potiahnete na prvú pozíciu.

Ak vyberiete mediálny objekt, je k dispozícii kontextová ponuka (kliknutie pravým tlačidlom myši) s nasledujúcimi možnosťami:

- Zobraziť
- Otvoriť obsahujúci_zložku
- Urobiť aktívne médium
- Pridať
- Zdieľať
- Upraviť
- Odstrániť

##### Selektor Výber mediálneho objektu

![[_media/SelectMediaObject-selector-dialog-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Výber mediálneho objektu - selektor - príklad]]

Dialógové okno selektor umožňuje prepojenie na už existujúci mediálny objekt a po výbere obrázka sa otvorí v dialógovom okne .

Po výbere mediálneho objektu zo zoznamu sa v hornej časti zobrazí náhľad, ak je to možné.

Zobrazia sa nasledujúce stĺpce: Názov (predvolené triedenie zoznamu), ID, Typ, Posledná zmena.

Na filtrovanie zoznamu na základe jednej z možností z rozbaľovacieho zoznamu môžete použiť tlačidlo :

- **Názov obsahuje**(predvolené)
- *Názov neobsahuje*
- *ID obsahuje*
- *ID neobsahuje*
- *Typ obsahuje*
- *Typ neobsahuje*
- *Posledná zmena obsahuje*
- *Posledná zmena neobsahuje*

Pozri tiež [Selektor Výber mediálneho objektu](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_2/sk#Selektor_Výber_mediálneho_objektu) {{-}}

#### Internet

![[_media/EditPerson-Internet-tab-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Záložka "Internet" z dialógového okna "Upraviť osobu" - príklad]]

  
V záložke sa zobrazujú internetové adresy relevantné pre danú osobu. Popisný nadpis internetového miesta, ktoré ukladáte. Typ internetovej adresy podľa potreby navigácie na ňu, napr. <http://gramps-project.org>, E-mail, Webová stránka, ...

<!-- -->

  
V spodnej časti sa nachádzajú všetky takéto internetové adresy a sprievodné popisy. V hornej časti sa zobrazujú podrobnosti o aktuálne vybraných adresách v zozname (ak existujú). Tlačidlá , otvorí dialógové okno na pridanie alebo úpravu a odstráni vybranú internetovú adresu. Tlačidlo "Prejsť na" otvorí internetový prehliadač a prenesie vás priamo na označenú stránku.

Všimnite si, že tlačidlá , a sa sprístupnia len vtedy, keď je zo zoznamu vybraná internetová adresa. {{-}}

##### Internetový editor adries

![[_media/InternetAddressEditor-dialog-default-60.png|Obrázok {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Editor internetových adries" - dialógové okno - predvolené]]

Dialógové okno umožňuje pridať novú internetovú adresu alebo upraviť vybranú internetovú adresu.

- Typ internetovej adresy:

  - *E-mail*
  - **Neznáma** <small>(predvolené)</small>
  - *FTP*
  - *Web Home*
  - *Webové vyhľadávanie*

- prepína stav súkromia záznamu.

- Internetová adresa podľa potreby na navigáciu, napr.: <https://gramps-project.org>

  - otvorenie internetovej adresy v predvolenom prehliadači

- Popisný nadpis internetového miesta, ktoré ukladáte.

Pozri tiež

- [Editor odkazu](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_2/sk#Editor_odkazu)
- [Note Link Report](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_6/sk#Note_Link_Report)

{{-}}

#### Asociácie

![[_media/EditPerson-Associations-tab-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Záložka "Asociácie" z dialógového okna "Upraviť osobu" - príklad]]

Záložka umožňuje zobrazovať a upravovať informácie o asociáciách medzi osobami v databáze. Združenia môžu zahŕňať krstných rodičov, rodinných priateľov, pall bearer (nosič pohára), spolupracovníka alebo akýkoľvek iný typ združení, ktoré si môžete želať zaznamenať. Ak je najbližší vzťah "krstný rodič", potom to znamená, že krstným rodičom osoby (ktorá sa upravuje) je osoba, ktorej meno je zobrazené na karte Asociácie.

Značka [*Associates* (ASSO) v štandarde GEDCOM](http://wiki-en.genealogy.net/GEDCOM/ASSO-Tag) hovorí, že "príbuzný alebo asociácia osoby je osoba, na ktorú sa ukazuje". Môžete sa rozhodnúť, že na karte Associations (Asociácie) tejto inej osoby uvediete vzájomnú asociáciu.

V uvedenej asociácii z [example.gramps](wiki:Example.gramps) je krstným otcom Lewisa Garnera Anderson Garner. Pre vzťahy spojené s konkrétnymi časovými rámcami alebo príležitosťami použite namiesto toho položku Udalosti. Udalosti môžu byť zdieľané medzi ľuďmi, pričom každý z nich uvedie svoju [rolu](wiki:Gramps_Glossary#role) v udalosti.

Tlačidlo otvorí dialógové okno na pridanie. Tlačidlo umožňuje upraviť a tlačidlo odstráni vybranú asociáciu. Ostatné tlačidlá alebo posúvajú iba pozíciu vybranej položky v zozname.

Pozrite si tiež: V prípade, že je asociácia v zozname asociácií, je možné ju vybrať:

- [Roles, Relationships &amp; Associations](wiki:Roles,_Relationships_&amp;_Associations)
- [Pridať krstného otca-kmotru](wiki:Pridať_krstného_otca-kmotru)

{{-}}

##### Editor odkazov na osoby

![[_media/PersonReferenceEditor-dialog-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Editor odkazov na osoby" - dialógové okno - predvolené]]

Dialógové okno umožňuje pridávať a upravovať záznamy o asociáciách. Môžete sa k nemu dostať z dialógového okna záložky.

- - Tlačidlo vyvolá dialógové okno selektora.

- *Krstný otec* (Predvolené) môžete prepísať predvolenú položku čímkoľvek, čo si vyberiete.

  - záznam je verejný (Predvolené)

<!-- -->

- Záložka Citácie zdrojov

<!-- -->

- Záložka Poznámky

{{-}}

###### Vyberte selektor osôb

![[_media/SelectPerson-selector-dialog-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Výber osoby" - dialógové okno výberu - príklad]]

{{-}}

#### SPD

![[_media/EditPerson-LDS-tab-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Záložka "SPD" z dialógového okna "Upraviť osobu" - príklad]]

  
Označenie (Svätí posledných dní) umožňuje zobraziť a upraviť informácie o nariadeniach SPD danej osoby. Tieto informácie sú zdedené zo špecifikácie GEDCOM.

<!-- -->

  
Ide o obrady SPD Baptism (Krst), Endowment (Obdarovanie) a Sealed to Parents (Zapečatenie rodičom), ako sú označené vo vnútri karty. Každé nariadenie je popísané dátumom, chrámom LDS a miestom, kde sa uskutočnilo.

<!-- -->

  
Pre ordináciu Sealed to Parents (Zapečatený rodičom) je k dispozícii ďalšia rozbaľovacia ponuka "Parents" (Rodičia). Každú ordináciu možno ďalej opísať prostredníctvom výberov dostupných vo vyskakovacom menu "Stav". Môže tiež obsahovať poznámky a odkazy na zdroje prostredníctvom príslušných tlačidiel a .

Pozri: [Family Editor dialog&gt;Tab&gt;LDS](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1#LDS_2)

{{-}}

##### LDS Editor vyhlášky

![[_media/LDSOrdinanceEditor-dialog-default-60.png|Obrázok {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "LDS Ordinance Editor" - dialógové okno - predvolené]]

Pomocou tlačidiel alebo vyvoláte dialógové okno , v ktorom môžete pridať alebo upraviť existujúce nariadenia LDS danej osoby.

- Pozri [Ordinance (Latter Day Saints)](https://wikipedia.org/wiki/Ordinance_(Latter_Day_Saints)) na [Wikipedia](https://en.wiktionary.org/wiki/Wikipedia#Etymology).

{{-}}

#### Referencie

![[_media/EditPerson-References-tab-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Záložka "Referencie" z dialógového okna "Upraviť osobu" - príklad]]

  
Záložka

{{-}}

## Úprava informácií o vzťahoch

Informácie o vzťahoch sa zadávajú a upravujú prostredníctvom dialógového okna .

Toto dialógové okno možno vyvolať viacerými spôsobmi:

- Z [kategórie Vzťahy](wiki:Gramps_6.0_Wiki_Manual_-_Categories/sk#Kategória_Vzťahy): kliknite na tlačidlo v rodine, ktorú chcete upraviť.

<!-- -->

- Z [kategórie Rodiny](wiki:Gramps_6.0_Wiki_Manual_-_Categories/sk#Kategória_Rodiny): vyberte rodinu v zozname a potom kliknite na tlačidlo na paneli nástrojov alebo dvakrát kliknite na rodinu.

<!-- -->

- Z [kategórie Grafy](wiki:Gramps_6.0_Wiki_Manual_-_Categories/sk#Kategória_Grafy): nabehnite myšou na čiernu čiaru spájajúcu manželov, kliknite pravým tlačidlom myši a z kontextovej ponuky vyberte alebo dvakrát kliknite na čiernu čiaru.

Ktorýkoľvek z týchto spôsobov vám ponúkne dialógové okno }:

{{-}}

### Dialógové okno Editor rodiny

![[_media/FamilyEditor-dialog-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Dialógové okno]]

V hornej časti okna sa zobrazujú mená osôb, ktorých príbuzenský vzťah sa upravuje, ako aj informácie o ich narodení a úmrtí.

- 

- 

[Rýchly pohľad](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_8/sk#Quick_Views/sk) správy sú dostupné pomocou kontextovej ponuky(kliknutím pravým tlačidlom myši) z prázdnej oblasti v hornej časti okna.

V časti sa zobrazujú tri polia a niekoľko [kariet zápisníka](wiki:Gramps_6.0_Wiki_Manuál_-_Vkladanie_a_editácia_údajov:_podrobné_-_časť_1#Stránky_záložky_Editora_rodiny), ktoré predstavujú rôzne kategórie informácií o vzťahu. Kliknutím na ktorúkoľvek kartu zobrazíte alebo upravíte informácie, ktoré obsahuje. V spodnej časti sa nachádzajú tlačidlá a . Kliknutím na tlačidlo sa kedykoľvek použijú všetky zmeny vykonané na všetkých kartách a dialógové okno sa zatvorí. Kliknutím na tlačidlo sa okno kedykoľvek zatvorí bez uplatnenia akýchkoľvek zmien. Ak sa zmení ktorýkoľvek údaj na ktorejkoľvek karte, zobrazí sa okno s upozornením, ktoré vás vyzve na výber medzi zatvorením dialógového okna bez uloženia zmien, zrušením pôvodnej požiadavky na zrušenie alebo uložením zmien.

V poliach sekcie sa nachádza základný opis vzťahu. V poli sa zobrazuje identifikačné číslo, ktoré označuje tento vzťah v databáze, toto pole nechajte prázdne, aby program Gramps vygeneroval jedinečné identifikačné číslo. Z rozbaľovacieho zoznamu } môžete vybrať dostupné typy rodinných vzťahov, ako napríklad <kód>Občiansky zväzok</kód>, <kód>Sobášený</kód>, **<kód>Neznámy</kód>** (predvolené), <kód>Nezosobášený</kód> atď.

Pozri tiež:

- Ako znázorniť rozvod?

zobrazí [značky](wiki:Gramps_6.0_Wiki_Manual_-_Filters/sk#Značky), ktoré ste vytvorili na zobrazenie základných informácií o stave vášho výskumu. Ďalšie značky môžete pridať výberom tlačidla .

##### Vyberte selektor otca

![[_media/SelectFather-selector-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Vybrať otca - selektor]]

Dialógové okno selektor umožňuje prepojenie na už existujúceho otca. {{-}}

##### Vybrať matku selektor

![[_media/SelectMother-selector-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Výber matky - selektor]]

Dialógové okno selektor umožňuje prepojenie na už existujúcu matku. {{-}}

### Stránky karty Editor rodiny

Karty poskytujú nasledujúce informačné kategórie údajov o príbuzenských vzťahoch:

#### Deti

![[_media/FamilyEditor-dialog-Children-tab-example-50.png|Obrázok {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Karta "Deti" z dialógového okna "Editor rodiny" - príklad]]

  
Karta umožňuje zobraziť a upraviť zoznam detí, ktoré sú súčasťou tohto vzťahu. Tlačidlo umožňuje zadať novú osobu do databázy a pridať túto osobu ako dieťa v tomto vzťahu. Tlačidlo umožňuje vybrať existujúcu osobu, ktorá má byť dieťaťom v tomto vzťahu. Tlačidlo otvorí dialógové okno , ktoré umožňuje upravovať vzťahy medzi vybraným dieťaťom a rodičmi. Nakoniec tlačidlo umožňuje odstrániť vybrané dieťa zo vzťahu. Všimnite si, že tlačidlá a sú dostupné len vtedy, keď je dieťa vybrané zo zoznamu.

[Ako zmením poradie detí?](wiki:Gramps_6.0_Wiki_Manual_-_FAQ#Ako_zmením_pořadí_detí.3F) Použite:

- Túto [Deti](wiki:Gramps_6.0_Wiki_Manuál_-_Vkladanie_a_úprava_údajov:_detail_-_časť_1#Deti) kartu v Editore rodiny, ak chcete zmeniť poradie detí v rodine.
- Doplnok tretej strany [Birth Order Tool](wiki:Addon:BirthOrderTool), ktorý umožňuje hromadnú aktualizáciu poradia detí.

{{-}}

##### Výber dieťaťa

![[_media/SelectChild-selector-dialog-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Výber dieťaťa - selektor - príklad]]

Dialógové okno selektor umožňuje prepojenie na už existujúce dieťa a po jeho výbere sa otvorí v

Zobrazujú sa nasledujúce stĺpce: Meno(predvolené triedenie pre zoznam), ID, Pohlavie, Dátum narodenia, Miesto narodenia, Dátum úmrtia, Miesto úmrtia, Manžel/manželka, Posledná zmena. {{-}}

##### Editor odkazu na dieťa

![[_media/ChildReferenceEditor-dialog-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Editor odkazu na dieťa]]

Dialógové okno umožňuje upravovať vzťah medzi vybraným dieťaťom a rodičmi.

K dispozícii sú nasledujúce možnosti:

- } Meno dieťaťa

  - tohto dieťaťa.

- Vyberte z rozbaľovacieho zoznamu možných typov vzťahov:

  - Adoptované
  - **Narodenie** (predvolené)
  - V pestúnskej starostlivosti
  - Žiadny
  - Sponzorovaný
  - Nevlastné dieťa
  - Neznámy

- Vyberte z rozbaľovacieho zoznamu možných typov vzťahu:

  - Adoptované
  - **Narodenie** (predvolené)
  - V pestúnskej starostlivosti
  - Žiadny
  - Sponzorovaný
  - Nevlastné dieťa
  - Neznámy

- Tlačidlo prepínač súkromia pre tento vzťah.

{{-}} K dispozícii sú aj nasledujúce karty.

###### Karta Citácie zdrojov

{{-}}

###### Karta Poznámky

{{-}}

#### Udalosti

  
Karta umožňuje zobraziť a upraviť zoznam udalostí relevantných pre daný vzťah. Tlačidlá , a umožňujú pridať, upraviť alebo odstrániť záznam o udalosti z databázy. Všimnite si, že tlačidlá a sú dostupné len vtedy, keď je udalosť vybraná zo zoznamu.

{Odstránením udalosti zo zoznamu sa táto udalosť z databázy neodstráni. Jednoducho sa odstráni odkaz na udalosť z tohto vzťahu.}}}

{{-}}

#### Zdroje Citácie

Karta vám umožňuje zobraziť a upraviť zoznam odkazov na zdroje, ktoré poskytujú dôkazy pre daný vzťah. Môžu to byť dokumenty, ktoré odkazujú na vzťah, ale ktoré ho nemusia nevyhnutne oficiálne dokumentovať. Napríklad, ak sa v memoároch tety Marty spomína, že jej pravnuk Paul bol ženatý, bádateľ to môže považovať za dôkaz existencie vzťahu medzi Paulom a jeho manželkou a uviesť memoáre ako zdroj tohto predpokladu.

Tlačidlá , a umožňujú pridať, upraviť a odstrániť odkaz na zdroj k tomuto vzťahu. Všimnite si, že tlačidlá a sú dostupné len vtedy, keď je zdrojový odkaz vybraný zo zoznamu.

{{-}}

#### Atribúty

Karta umožňuje zobraziť a upraviť konkrétne informácie o vzťahu, ktoré možno vyjadriť ako atribúty. Tlačidlá , a umožňujú pridať, upraviť alebo odstrániť atribút. Všimnite si, že tlačidlá a sú dostupné len vtedy, keď je atribút vybraný zo zoznamu.

{{-}}

#### Poznámky

  
Karta { umožňuje zobraziť a upraviť všetky [poznámky](wiki:Gramps_Glossary#note) súvisiace so vzťahom. Môžu to byť akékoľvek poznámky, ktoré sa prirodzene nezmestia do dvojíc "Parameter-Value" (Parameter-hodnota), ktoré sú k dispozícii pre atribúty. Ak chcete pridať poznámku alebo upraviť existujúce poznámky, jednoducho upravte text v poli na zadávanie textu.

Možnosť vám umožňuje nastaviť spôsob, akým sa poznámka zobrazí v správach a na webových stránkach. Ak vyberiete možnosť Flowed (Plynúci), vygenerovaný text bude mať namiesto všetkých viacnásobných medzier, tabulátorov a jednotlivých znakov na konci riadku vložené jednoduché medzery. Prázdny riadok vložený medzi dva bloky textu bude signalizovať nový odsek; ďalšie vložené riadky sa budú ignorovať.

Ak vyberiete možnosť Preformátované, text v správach a na webových stránkach sa bude zobrazovať presne tak, ako ste ho zadali v dialógovom okne .

{{-}}

#### Galéria

  
Karta umožňuje ukladať a zobrazovať fotografie a iné mediálne objekty súvisiace so vzťahom. V strednej časti okna sa nachádza zoznam všetkých takýchto objektov a náhľad miniatúr obrazových súborov. Ostatné objekty, ako sú zvukové súbory, filmové súbory atď. sú reprezentované všeobecnou ikonou Gramps. Tlačidlá , , a umožňujú pridať nový obrázok, pridať odkaz na existujúci obrázok, upraviť existujúci obrázok a odstrániť prepojenie mediálneho objektu so vzťahom. Všimnite si, že tlačidlá a sú dostupné len vtedy, keď je mediálny objekt vybraný zo zoznamu.

{{-}}

#### SPD

![[_media/EditFamily-LDS-tab-example-51.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Zapečatené manželom&#39; ordinácia editora &quot;Edit Family&quot; - dialóg - príklad]] Označenie (Svätí posledných dní) v karte Editor rodiny sa zobrazujú iba informácie o **Uzavretí manželovi**' SPD. (Obrady týkajúce sa jednotlivcov možno zaznamenať v [SPD karte Editor <strong>Osoby</strong>'](wiki:Gramps_6.0_Wiki_Manuál_-_Vkladanie_a_editácia_údajov:_detail_-_časť_1#LDS)).

Údaje môžu obsahovať aj , , a .

Každý záznam o obrade môže byť tiež opatrený poznámkami v príslušných kartách a . Stav obradu možno opísať prostredníctvom možností dostupných vo vyskakovacom menu .

  
Stavy stavu pre obrad **Zapečatené manželovi** sú:

- **<Nie je stav>** *(predvolené)*
- Zrušené
- Zrušené
- Ukončené
- Nezapečatiť
- Pred rokom 1970
- Kvalifikované
- Nezapečatiť/Zrušiť
- Predložené
- Nevyčistené

Ak chcete upraviť anotačné údaje o zdroji alebo poznámke, prepnite sa na príslušnú kartu Editora SPD a vyberte požadovaný záznam v zozname záznamov. Dvakrát kliknite na tento záznam alebo kliknite na ikonu na paneli nástrojov, čím vyvoláte nasledujúce dialógové okno

V hlavnej časti Editora rodín’na karte sa zobrazí tabuľka piatich rôznych údajov detí v každom zázname. Kliknutím na záhlavie stĺpca na riadok alebo dvojitým kliknutím na riadok upravte jeho obsah. V spodnej časti okna sa nachádzajú tlačidlá a . Kliknutím na tlačidlo sa použijú všetky zmeny vykonané na všetkých kartách a dialógové okno sa zatvorí. Kliknutím na tlačidlo sa okno zatvorí bez uplatnenia akýchkoľvek zmien. {{-}}

## Úprava dátumov

Táto časť popisuje, ako zadávať a upravovať dátumy. Keďže dátumy sú pri genealogickom výskume veľmi dôležité, Gramps venuje osobitnú pozornosť zachovaniu a používaniu všetkých dostupných informácií o dátumoch.

Informácie môžete do poľa dátumu zadať priamym zadaním alebo vyvolaním dialógového okna kliknutím na tlačidlo vedľa ľubovoľného poľa .

Pozri tiež: Príručka Wiki k aplikácii Gramps 6.0 - Pravdepodobne žije\]\]: \* [Gramps 6.0 - Príručka Wiki - Pravdepodobne žije](wiki:Gramps_6.0_-_Príručka_Wiki_-_Pravdepodobne_žije)

- \- Ak chcete zmeniť predvolené hodnoty pre typický vek pri narodení, medzi generáciami atď.

### Dialógové okno Výber dátumu

![[_media/DateSelection-dialog-defaults-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}}  - dialógové okno - predvolené]]

Hoci vyššie uvedené pravidlá rozboru poskytujú návod na zadanie najbežnejších dátumov, môžete použiť aj dialóg. Dialógové okno je obzvlášť užitočné na zostavenie zložitého dátumu alebo jednoducho na zabezpečenie toho, aby boli vaše informácie zadané spôsobom, ktorému bude Gramps rozumieť.

- Vyberte alternatívny [typ kalendára](wiki:Gramps_6.0_Wiki_Manuál_-_Vkladanie_a_úprava_údajov:_detail_-_časť_1#Kalendáre).

  - [**Gregoriánsky**](https://en.wikipedia.org/wiki/Gregorian_calendar)(predvolené)
  - [Juliánsky](https://www.familysearch.org/wiki/en/Julian_and_Gregorian_Calendars) (vrátane [Mixed](wiki:Dates#Dual_Dated)/[Dual](#Dual-date) dátumov)
  - [Hebrejské](https://en.wikipedia.org/wiki/Hebrew_calendar)
  - [Francúzske republikánske](https://www.familysearch.org/wiki/en/French_Republican_Calendar)
  - [Perzský](https://en.wikipedia.org/wiki/Iranian_calendars#Old_Persian_calendar)
  - [Islamské](https://en.wikipedia.org/wiki/Islamic_calendar)
  - [švédsky](https://www.familysearch.org/wiki/en/Sweden_Feast_Day_Calendars)

-  Toto pole je možné vybrať spolu so zodpovedajúcim poľom, ak alternatívne podporuje [dvojité datovanie](wiki:Gramps_5._1_Wiki_Manuál_-_Zadávanie_a_editácia_údajov:_detail_-_časť_1#Dvojité_dátum). (začiarkávacie políčko nie je štandardne začiarknuté)

  - (v predvolenom nastavení prázdne textové pole)

- Nastavte [kvalita_dátovania](wiki:Gramps_6.0_Wiki_Manuál_-_Vkladanie_a_úprava_údajov:_detail_-_časť_1#Kvalita_dátovania).

  - **Bežný** (predvolené nastavenie)
  - Odhadovaný
  - Vypočítaná

- Nastavte presnosť intervalu alebo časový rámec [typ dátumu](wiki:Gramps_6.0_Wiki_Manuál_-_Zadávanie_a_úprava_údajov:_detailed_-_part_1#Date_formats_and_parsing_rules).

  - **Bežný**(predvolené nastavenie) - interval pokrývajúci konkrétny deň, mesiac alebo rok (bez ohľadu na časové pásmo)
  - Pred
  - Po
  - O
  - Rozsah
  - Rozsah
  - Len text

- Vyberte , a .

- Ak je váš dátum *Rozsah* alebo *Rozpätie*, táto možnosť bude k dispozícii na nastavenie dátumu.

- pole pre zadanie textu umožňuje spolu s dátumom uložiť ľubovoľný textový reťazec.

{{-}}

### Indikátory platnosti dátumu

![[_media/DateSelection-dialog-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Dialógové okno výberu dátumu - príklad]]

Gramps používa validátor dátumu.

Hoci čiastkové dátumy nedefinujú jednoznačne deň, umožňujú aspoň určitý typ porovnania medzi dátumami.

Pole dátumu sa zvýrazní červenou farbou a zobrazí sa červený symbol (napríklad stopka alebo krížik), ktorý signalizuje, že zadaný dátum nie je uznaný ako uznaný a platný formát dátumu.

Príkladmi bežných odkazov na dátumy, ktoré nie sú rozpoznateľnými formátmi Gramps, môžu byť "vianočný týždeň '61", "jeseň 1782" alebo "leto, keď som bol na operácii". V takom prípade sa dátum uloží ako reťazec a označí sa ako typ *Len text*. Všetky dátumy tohto typu sa nebudú porovnávať s inými dátumami. Ak je to možné, je vhodnejšie vyhnúť sa takýmto dátumovým záznamom typu *Text Only*. Lepšie by bolo napríklad zadať dátum "december 1961" a potom pridať poznámku Opis "Vianočný týždeň '61". Presnejšie by bolo skontrolovať v kalendári december 1961 a potom zadať skutočné rozpätie dátumu... ale stále uviesť anotáciu. Anotácia je potrebná, pretože nemôžete predpokladať, že "vianočný týždeň" pre vás znamená rovnaké rozpätie dní ako pre váš zdroj. Mohlo by dôjsť ku kultúrnemu skresleniu interpretácie. Mohlo by to znamenať riadok kalendára, ktorý obsahuje deň Vianoc. Ale americké a európske kalendárne riadky začínajú rôznymi dňami v týždni. Alebo by to mohlo znamenať 7 dní začínajúcich sa Vianocami alebo dokonca 7 dní predchádzajúcich Vianociam. Rozpätie teda umožňuje vyhľadávanie a porovnávanie, ale anotácia ukazuje, že skutočný interval podlieha interpretácii.

V rôznych zobrazeniach (ako napríklad ) sa nerozpoznané dátumy štandardne zobrazujú **tučným písmom**. Označenie textu (štýl formátovania) pre nerozpoznané dátumy je možné zmeniť zmenou možnosti } v [záložke](wiki:Gramps_6.0_Wiki_Manual_-_Settings/sk#Dates) [Predvoľby](wiki:Gramps_6.0_Wiki_Manual_-_Settings/sk).

Ak pri Osobe chýba dátum narodenia alebo úmrtia, môžu sa zobraziť dátumy existujúcich náhradných Udalostí v tej istej kategórii (a označiť kurzívou so skráteným názvom), namiesto toho, aby sa zobrazenie ponechalo prázdne. Dátum pohrebu alebo kremácie sa teda zobrazí, ak dátum úmrtia ešte nebol zaznamenaný.

{{-}}

### Kvalita dátumu

- Pravidelná: Bežný" dátum je dátum s explicitne uvedeným dňom, mesiacom alebo rokom.

<!-- -->

- Odhadovaný: Odhadovaný" dátum je dátum založený na predpokladoch priemerného intervalu posunutého od známeho referenčného dátumu. (Napríklad priemerný počet rokov medzi generáciami, maximálna dĺžka života alebo dĺžka námornej plavby.)

<!-- -->

- Vypočítaný: "Vypočítaný" dátum je dátum založený na známom intervale od referenčného dátumu, ale bez zdroja, ktorý by tento dátum výslovne uvádzal. (Napríklad náhrobný kameň s vyrytým dátumom úmrtia aj presným vekom pri úmrtí.)

Údaje zo sčítania ľudu sú nezvyčajné v tom, že sa zdajú byť kandidátom na vypočítaný dátum, ale nie sú. Sčítanie často explicitne definuje interval (vek) a referenčný dátum (dátum sčítania ľudu), ale tento vek je často odhadnutý alebo zaokrúhlený.

### Typ dátumu

Napravo od by sa mala objaviť vysúvacia ponuka.

Dátumy v programe Gramps sa klasifikujú podľa nasledujúcich typov presnosti (mierky) intervalu alebo časového rámca:

- Pravidelné: Bežný" dátum je taký, ktorý obsahuje interval pokrývajúci určitý deň, mesiac alebo rok. Môže byť úplný (alebo "plne kvalifikovaný" pre 24-hodinový interval, ako napríklad 6. jún 1990) alebo čiastočný (napríklad vynechanie dňa pre interval 1 mesiaca, ako napríklad júl 1977, alebo vynechanie dňa a mesiaca pre interval 1 roka).

<!-- -->

- Pred: Dátum "pred" je dátum, ktorý možno identifikovať ako dátum, ktorý sa vyskytuje (v [preferences-defined long interval](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Dates)) pred určitým dňom, mesiacom alebo rokom. *(V predvolenom nastavení je interval 50 rokov.)*

<!-- -->

- Po: Dátum "po" je dátum, ktorý nastane (v [2. predvoľbami definovaný dlhý interval](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Dates)) po určitom dni, mesiaci alebo roku. *(V predvolenom nastavení je interval 50 rokov.)*

<!-- -->

- O: Dátum "okolo" (circa) je dátum, ktorý sa vyskytuje (v [ďalší interval definovaný preferenciami ±rokov](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Dates)) pred **alebo** po určitom dni, mesiaci alebo roku. *(V predvolenom nastavení je interval ±50 rokov.)*

<!-- -->

- Rozsah: Rozsah" opisuje časové obdobie, počas ktorého sa udalosť vyskytla. Môže ísť o opakovanú udalosť počas intervalu alebo o jediný prípad, o ktorom sa predpokladá, že sa vyskytol medzi známymi hraničnými dátumami.

  
Napríklad "medzi januárom 1932 a marcom 1932".

- Priestor: "Rozpätie" opisuje obdobie, počas ktorého stav nepretržite existoval.

  
Napríklad "od 12. mája 2000 do 2. februára 2002".

### Formáty dátumov a pravidlá ich rozboru

Dialógové okno Výber dátumu len pomáha rozvrhnúť dátum v štandardnom formáte, ktorý Gramps vie analyzovať. Je užitočné, keď nepoznáte možnosti, potrebujete použiť alternatívny kalendár alebo zadať dátum začiatku nového roka.

Gramps rozpozná dátumy zadané v rôznych formátoch. Predvolený číselný formát je ten, ktorý je bežný pre prostredie, v ktorom Gramps pracuje; to znamená DD.MM.RRRR pre väčšinu európskych krajín, MM/DD/RRRR pre USA atď. Spôsob, ako sa vyhnúť tejto nejednoznačnosti, je vždy zvoliť formát d mmmnbsp;rrrr alebo mmmnbsp;d rrrr.

Okrem presných dátumov Gramps rozpoznáva mnoho typov dátumov, ktoré nie sú pravidelné: pred, po, o, rozsahy a rozpätia. Rozumie aj kvalite: odhadovaná alebo vypočítaná. Nakoniec podporuje čiastočné dátumy a mnohé alternatívne kalendáre. Nižšie je uvedený zoznam pravidiel pre zadávanie dátumov, ktoré umožňujú presné analyzovanie dátumov.

Bežné jednotlivé dátumy môžete zadávať rovnako, ako by ste ich písali. A zadaním lomítka za rokom a následnej hodnoty o 1 rok neskôr sa vytvorí záznam s juliánskym dvojitým dátumom.

  
Príklady: V prípade, že dátumy sú uvedené v tabuľke, je možné ich použiť ako dátumy: Príklady: 24. máj 1961, 31. december 1858/9 alebo 1. január 2004.

Čiastkové dátumy sa zadávajú jednoducho vynechaním neznámych informácií.

  
Príklady: Máj 1961 a 2004.

Dátumy, ktoré nie sú Pravidelné , by mali začínať kľúčovými slovami *Odhadované* alebo *Vypočítané* , ak je to vhodné.

  
Príklad: Est. 1961 alebo calc 2005. (Všimnite si, že sa nemusí uvádzať pre bežné dátumy.)

Možnosti ponuky možno nastaviť aj na *Pred*, *Po* alebo *O* jednoduchým zadaním "pred", "po" alebo "o" pred jednotlivým dátumom v dialógovom okne Úprava udalosti.

Ak je požadovaný rozsah, napíšte "medzi DÁTUM a DÁTUM", a ak je rozpätie, napíšte "od DÁTUM do DÁTUM".

  
Príklady: est od 2001 do 2003, pred júnom 1975, est okolo 2000, calc od mája 1900 do 1. januára 1990.

Tu je niekoľko príkladov na vyskúšanie:

  
Kapitán John Smith bol podľa vojenského záznamu umiestnený v 1. granátnickom pluku v období od 1888-5-13 do 1902-10-24 (slová "medzi" a "a" sú použité zámerne, pretože takto hovoríme v každodennom živote); potom by sa dátum mal kódovať "od ... do ...", pretože ide o trvanie jeho služby.

<!-- -->

  
Pluk kapitána Johna Smitha bol vyslaný na rieku Escaut vo Valenciennes týždeň pred prímerím.  
''Potom to možno zaznamenať ako typ udalosti "Vojenská služba" s dátumom "od 4. 11. 1918 do 11. 11. 1918" (Gramps prevedie na štandardný formát dátumu napriek tomu, že sa na zápis používajú 2 formáty) na rieke Escaut, Valenciennes, departement Noord, Francúzsko..., pretože skutočný dátum tejto "okamžitej" udalosti nie je v zdroji známy.

### Kalendáre

Alternatívne kalendáre sú kalendáre iné ako gregoriánsky kalendár. V súčasnosti Gramps podporuje hebrejský, francúzsky republikánsky, juliánsky, islamský, perzský a švédsky alternatívny kalendár. Ak chcete určiť iný kalendár ako predvolený gregoriánsky, pridajte názov kalendára k reťazcu dátumu, napríklad "9. január 1905 (juliánsky)", alebo použite rozbaľovaciu ponuku.

#### Švédsky kalendár

[Švédsky kráľ](wiki:Swedish_kings) Karol XII. rozhodol, že Švédsko by malo začať používať gregoriánsky kalendár. Plánovalo sa však, že sa to uskutoční postupne vynechaním 11 priestupných dní počnúc rokom 1700-02-29 a skončí do roku 1744. Po roku 1700-02-28 nasledoval rok 1700-03-01. Uskutočnilo sa to počas Veľkej severskej vojny a priestupné dni boli zachované 1704 a 1708. V januári 1711 ten istý kráľ rozhodol, že Švédsko sa má vrátiť k juliánskemu kalendáru do 1712-03-01. Aby to bolo v súlade s fázou, bol vložený dodatočný deň 1712-02-30. A to bol koniec švédskeho kalendára. Švédsko prešlo na gregoriánsky kalendár v roku 1753-03-01 vynechaním dátumov medzi 1752-02-18 a 1753-02-28. V programe Gramps môžete zadať platné dátumy švédskeho kalendára len od 1700-03-01 do 1712-02-30. Všetky ostatné dátumy sú označené ako neplatné a je potrebné ich opraviť.

### Dvojité dátumy

Dátumy s dvojitým datovaním (nazývané aj "dvojité datovanie", "dátumy s lomítkom" a niekedy "dátumy starého štýlu/nového štýlu") sa zobrazujú ako "23. januára 1735/6". Často sa mylne považujú za neurčitosť roku, v skutočnosti majú špecifický historický význam. Dvojité datovanie predstavuje obdobie, keď sa oblasť nachádzala v prechodnom období medzi prechodom na 1. január ako začiatok nového roka. Preto je 23. január 1735/6 údajom, aby bolo jasné, o aký dátum ide. V tomto príklade mohol dátum "23. januára 1736" nastať po dátume "23. júna 1736".

Anglicko a americké kolónie oficiálne prijali "1. január" ako dátum nového roka až v roku 1752. Pred rokom 1752 anglická vláda stále oficiálne dodržiavala 25. marec ako prvý deň v roku, zatiaľ čo väčšina anglického obyvateľstva dodržiavala 1. január ako prvý deň v roku. Mnohí ľudia preto písali dátumy spadajúce medzi 1. január a 25. marec vo formáte s dvojitým dátumom.

Niekedy sa dvojitý dátum môže objaviť ako zlomok, ako na tomto náhrobnom kameni (170 a 3/4, čo znamená 1703 a 1704):

![[_media/Gravestone.jpg|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Náhrobný kameň zobrazujúci dvojitý dátum ako zlomok (170 a 3/4, čo znamená 1703 a 1704)]]

{{-}}

Označenie dátumu ako dvojitého dátumu možno vykonať jednoduchým vložením lomky medzi roky. Napríklad:

- 1721/2
- 1719/20
- 1799/800

Tieto roky s lomítkom sa môžu objaviť kdekoľvek v dátume, kde sa môže objaviť bežný rok.

Dátumy s dvojitým dátumom sú v súčasnosti reprezentované v juliánskom kalendári, takže ich mesiac a deň budú rovnaké ako v textovej reprezentácii.

#### Alternatívny deň nového roka

Pri dátumoch s dvojitým dátumom (a iných dátumoch) môžete vedieť, že nový rok sa oslavoval v iný deň ako 1. januára. Ak to chcete v programe Gramps uviesť, uveďte kód mesiaca/deň v zátvorke za kalendárom (ak je). Napríklad:

- (25. marca).
- 20\. január 1750 (juliánsky,1. marec)
- 23\. február 1710/1 (Mar25)

Ak chcete označiť začiatok roka, ktorý je iný ako 1. január, použite nasledujúce kódy:

- Jan1
- Mar1
- Mar25
- Sep1

Môžete to uviesť ako jedinú položku v zátvorke alebo hneď za názvom kalendára (čiarka a bez medzery).

Všimnite si, že ak deň nového roka nie je 1. január, potom január príde po decembri toho roka. Dátumy s kódmi dní nového roka budú vhodne zoradené.

{{-}}

[Category:Sk:Documentation](wiki:Category:Sk:Documentation)
