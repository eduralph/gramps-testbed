---
title: 'Gramps 6.0 Wiki Manual - Entering and editing data: detailed - part 2/sk'
categories:
- Sk:Documentation
- Stub
managed: false
source: wiki-scrape
wiki_revid: 125068
wiki_fetched_at: '2026-05-30T20:03:47Z'
lang: sk
---

{{#vardefine:chapter\|9.2}} {{#vardefine:figure\|0}}

V predchádzajúcej časti ste získali podrobný prehľad o tom, ako zadávať a upravovať údaje o osobách, vzťahoch a dátumoch. Táto časť pokračuje ďalšími objektmi, s ktorými sa v programe Gramps stretnete.

## Úprava informácií o udalostiach

![[_media/EventsCategory-EventsListView-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Kategória Udalosti - Pohľad Udalosti (zoznam) - príklad]]

Pridanie Udalosti k osobe umožňuje zaznamenať nájdené informácie.

Pri pridávaní udalosti do sa zobrazí dialógové okno .

Ak chcete pridať alebo upraviť údaje o udalosti, prepnite na Pohľad kategórie a vyberte požadovanú položku v zozname udalostí. Dvakrát kliknite na túto položku alebo kliknite na na paneli nástrojov, čím vyvoláte nasledujúce dialógové okno . {{-}}

### Dialógové okno Nová udalosť

![[_media/EditEvent-dialog-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Úprava udalosti - dialógové okno - príklad]]

Udalosti sa upravujú prostredníctvom dialógového okna . Toto dialógové okno je prístupné buď z dialógového okna } alebo z dialógového okna .

Horná časť umožňuje zobraziť a upraviť základné informácie o udalosti:

- môžete vybrať z dostupných typov uvedených v rozbaľovacej ponuke Typ udalosti. Napríklad **Narodenie** (predvolené), Krst, Úmrtie, Pohreb atď. Môžete zadať vlastnú Udalosť [Vlastné typy](wiki:Gramps_Glossary#custom) zadaním priamo do tohto vstupného poľa.

- udalosti môže byť presný dátum, rozsah (*od ... do ..., medzi ...*) alebo nepresný dátum (*približne ...*).

  - Tlačidlo spustí dialógové okno .

- vám dáva možnosť uviesť dlhší popis, čo je to za udalosť.

  - \- Prepnutím zámku Súkromie označíte záznam udalosti ako súkromný, čo umožňuje jeho vynechanie v správach.

- môžete vybrať zo zoznamu predtým zadaných miest pomocou tlačidla alebo ho môžete zadať nanovo pomocou tlačidla . Okrem toho môžete do tohto poľa pretiahnuť položku miesta.

- je jedinečný identifikátor udalosti. Toto pole nechajte prázdne, aby program Gramps mohol túto hodnotu automaticky generovať pre nové udalosti.

- umožňuje vybrať existujúcu značku pomocou tlačidla .

### Stránky s kartami nových udalostí

V centrálnej časti okna sa zobrazujú karty obsahujúce rôzne kategórie informácií. Kliknutím na kartu zobrazíte alebo upravíte jej obsah. Karty poskytujú nasledujúce kategórie informácií o údajoch o udalosti:

#### Citácie zdrojov

  
Záložka umožňuje zobraziť a upraviť zdroje relevantné pre udalosť. V centrálnej časti okna sa nachádzajú všetky takéto odkazy na zdroje uložené v databáze. Tlačidlá umožňujú pridať, upraviť a odstrániť odkaz na zdroj súvisiaci s udalosťou. Všimnite si, že tlačidlá a sú dostupné len vtedy, keď je zdrojový odkaz vybraný zo zoznamu.

#### Poznámky

  
Záložka poskytuje miesto na zaznamenanie poznámok alebo komentárov k udalosti. Ak chcete pridať poznámku alebo upraviť existujúce poznámky, jednoducho upravte text v poli na zadávanie textu.

#### Galéria

  
Záložka

#### Atribúty

  
Záložka

#### Odkazy

  
Záložka

V spodnej časti okna sa nachádzajú tlačidlá a . Kliknutím na tlačidlo sa použijú všetky zmeny vykonané na všetkých kartách a dialógové okno sa zatvorí. Kliknutím na tlačidlo sa okno zatvorí bez uplatnenia akýchkoľvek zmien. Stlačením tlačidla sa zobrazí nápoveda, ak je k dispozícii.

{{-}}

## Úprava odkazov udalosti

Odkazy na udalosť spájajú udalosť s osobou a umožňujú poskytnúť ďalšie informácie o udalosti.

Pri pridávaní odkazov na udalosti na kartu sa na karte zobrazí dialógové okno .

{{-}}

### Dialógové okno Editor odkazu udalosti

![[_media/EventReferenceEditor-dialog-default-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Editor odkazu udalosti - dialógové okno - predvolené]]

Dialógové okno obsahuje dve časti: a .

- V časti sú uvedené podrobnosti súvisiace s konkrétnym odkazom na túto udalosť: , , .
- V časti sa zobrazujú : , , , , , .

{{-}}

#### Informácie odkazu

##### Stránky s kartou Informácie odkazu

###### Všeobecné

Pre } Editor nového média - dialógové okno - príklad zobrazujúci vlastnosti média\]\]

V hornej časti sa zobrazí miniatúrny náhľad objektu média, ak je k dispozícii, spolu so súhrnom jeho vlastností (ID, Dátum, Cesta a typ objektu), ktoré môžete zobraziť a upraviť. Tieto informácie môžete zadať priamo do príslušných polí. V prípade dátumu môžete informácie zadať aj kliknutím na tlačidlo , čím vyvoláte dialógové okno *'*.

- Popisný pre tento mediálny objekt.

- je jedinečný záznam na identifikáciu mediálneho objektu, ponechajte ho prázdny, ak ho má generovať program Gramps.

  - Prepínač súkromia pre tento mediálny objekt (predvolené) alebo .

- dátum spojený s mediálnym objektom, napr. pre obrázok to môže byť dátum jeho zhotovenia.

  - na vyvolanie dialógového okna *'*.

- } mediálneho objektu v počítači. Gramps neukladá médium interne, ukladá iba cestu! Nastavte [Relatívnu cestu](wiki:Gramps_6.0_Wiki_Manual_-_Settings/sk#Predvoľby) v záložke Predvoľby \> Všeobecné položku, aby ste nemuseli opakovane zadávať spoločný základný adresár, v ktorom sú uložené všetky vaše médiá. Nástroj [Správca médií](wiki:Gramps_6.0_Wiki_Manual_-_Tools/sk#Správca_médií) môže pomôcť pri správe ciest ku kolekcii objektov médií.

  - Tlačidlo .

- Tlačidlo .

V spodnej časti okna sa zobrazujú štyri záložky poznámkových blokov obsahujúce rôzne kategórie informácií. Kliknutím na kartu zobrazíte alebo upravíte jej obsah. V spodnej časti okna sa nachádzajú tlačidlá , a . Kliknutím na sa použijú všetky zmeny vykonané na všetkých kartách a dialógové okno sa zatvorí. Kliknutím na tlačidlo sa okno zatvorí bez uplatnenia akýchkoľvek zmien. Stlačením tlačidla sa dostanete sem.

### Nové stránky karty Médiá

Karty predstavujú nasledujúce kategórie údajov médií:

#### Zdroje citácií

#### Atribúty

Záložka umožňuje zobraziť a upraviť konkrétne informácie o mediálnom objekte, ktoré možno vyjadriť ako Atribúty. V spodnej časti sa zobrazuje zoznam všetkých takýchto atribútov uložených v databáze. V hornej časti sa zobrazujú podrobnosti o aktuálne vybranom atribúte v zozname (ak existuje). Tlačidlá , a umožňujú pridať, upraviť alebo odstrániť atribút. Všimnite si, že tlačidlá a sú dostupné len vtedy, keď je atribút vybraný zo zoznamu.

#### Poznámky

Záložka poskytuje miesto na zaznamenávanie rôznych informácií o zdroji, ktoré sa nedajú prehľadne zaradiť do iných kategórií. Táto oblasť je obzvlášť užitočná na zaznamenávanie informácií, ktoré sa prirodzene nezmestia do dvojíc "Parameter/Hodnota" dostupných pre atribúty. Ak chcete pridať poznámku alebo upraviť existujúce poznámky, jednoducho upravte text v poli na zadávanie textu.

#### Odkazy

Na karte sú uvedené všetky záznamy v databáze, ktoré sa vzťahujú na daný mediálny objekt. Zoznam je možné zoradiť podľa ľubovoľného nadpisu stĺpca: , alebo . Dvojkliknutím na záznam môžete zobraziť a upraviť príslušný záznam.

{{-}}

## Úprava odkazov mediálneho objektu

Keď odkazy mediálneho objektu spájajú mediálny objekt s iným objektom na karte , tlačidlo vyvolá [Výber_mediálneho_objektu selektor](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1/sk#Výber_mediálneho_objektu) a po výbere mediálneho objektu sa zobrazí dialógové okno

{{-}}

### Selektor Výber mediálneho objektu

![[_media/SelectAMediaObject-file-selector-dialog-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Výber mediálneho objektu - dialógové okno výberu (súboru) - príklad]]

Dialógové okno pre výber súboru umožňuje zobraziť náhľad a vybrať mediálny súbor, ktorý chcete pripojiť, a zároveň môžete upraviť zobrazený (Predvolené nastavenie je názov súboru bez prípony).

- (začiarkavacie políčko je predvolene nezačiarknuté, kým nie je začiarknuté prvýkrát, a pamätá si ho pri každom ďalšom výbere obrázka).

<!-- -->

- Pozri tiež: [Výber mediálneho objektu](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1/sk#Výber_mediálneho_objektu)

{{-}}

### Dialógové okno Editor odkazu média

![[_media/MediaReferenceEditor-dialog-collapsed-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Editor odkazu média - dialógové okno - zbalený predvolený príklad]]

Dialógové okno .

Pozri tiež [Ako vytvoriť odkazy oblasti obrázkov](wiki:Ako_vytvoriť_odkazy_oblasti_obrázkov) {{-}} ![[_media/MediaReferenceEditor-dialog-expanded-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Editor odkazu média - dialógové okno - príklad rozšírenej sekcie &quot;Zdieľané informácie&quot;]]

Sekciu **Zdieľané informácie** môžete tiež rozšíriť.

{{-}}

#### Začiatok sekcie

##### Stránky so záložkou Top sekcia

###### Všeobecné

- Rohy oblasti : x1, x2, y1, y2.

Časť umožňuje vybrať konkrétnu oblasť na objekte médií. Na výber oblasti môžete použiť kurzor myši na obrázku alebo pomocou týchto otočných tlačidiel nastaviť ľavý horný a pravý dolný roh odkazovanej oblasti. Bod (0,0) je ľavý horný roh obrázka a (100,100) pravý dolný roh.

- Súkromie

Tlačidlo vám umožňuje označiť, či sa záznam považuje za súkromný alebo nie. Začiarknutím políčka záznam označíte tento .

Pozrite si tiež [Naratívna webová stránka](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_7/sk#Generovanie_stránok). Záložka Galéria podporuje výstup týchto odkazovaných oblastí.

{{-}}

###### Zdroje citácií

{{-}}

###### Atribúty

{{-}}

###### Poznámky

{{-}}

#### Zdieľané informácie

##### Stránky karty Zdieľané informácie

###### Všeobecné

{{-}}

###### Odkazy

{{-}}

###### Zdroje citácií

{{-}}

###### Atribúty

{{-}}

###### Poznámky

{{-}}

## Úprava informácií o miestach

Ak chcete upraviť informácie o miestach, prepnite sa na Kategória a vyberte požadovanú položku zo zoznamu miest. Dvakrát kliknite na túto položku alebo kliknite na tlačidlo na paneli nástrojov, čím vyvoláte dialógové okno :

{{-}}

### Dialógové okno Editor miesta

![[_media/PlaceEditor-dialog-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Editor miesta - dialógové okno]]

Ak chcete upraviť informácie o miestach, prepnite sa do kategórie Miesta a vyberte požadovanú položku zo zoznamu miest. Dvakrát kliknite na túto položku alebo kliknite na tlačidlo na paneli nástrojov, čím sa zobrazí nasledujúce dialógové okno :

K dispozícii sú nasledujúce polia:

- Oblasť názvu v hornej časti zobrazuje opis tohto miesta, ktorý sa má použiť v správach. Gramps ho vytvorí za vás. Pozrite si [Predvoľby &gt; Zobrazenie &gt; Zapnúť automatické generovanie názvu miesta](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Zobrazenie).

- názov tohto miesta.

  - Tlačidlo otvorí dialógové okno , v ktorom môžete pridať/upraviť ďalšie informácie.

- typ miesta. Všetky **[Vlastné typy](wiki:Gramps_Glossary#custom)'' sú zobrazené v dolnej časti zoznamu. Vyberte si z nasledujúcich predvolených dostupných**Typov'''':

  - Budova
  - Obec
  - Krajina
  - Okres
  - Mesto
  - Oddelenie
  - Okres
  - Farma
  - Osada
  - Lokalita
  - Obec
  - Susedstvo
  - Číslo - pozri [formát Ulice:](wiki:Gramps_6.0_Wiki_Manual_-_Settings/sk#Editor_formátu_miesta)
  - Farnosť
  - Provincia
  - Región
  - Štát
  - Ulica
  - Mesto
  - **Neznámy** (predvolené)
  - Obec

- poloha vzhľadom na základný alebo greenwichský poludník miesta v desiatkovej alebo stupňovej sústave. Napríklad platné hodnoty sú 12.0154, 50°52'21.92\\S, S50º52'21.92\\ alebo 50:52:21.92. Tieto hodnoty môžete nastaviť prostredníctvom pohľadu Zemepis vyhľadaním miesta alebo prostredníctvom mapovej služby v zobrazení Miesto. Pozri: \[Gramps_6.0_Wiki_Manual\_-\_Vkladanie_a_editácia_údajov:\_podrobne\_-\_časť_2#Podporované_formáty_dĺžky.2Štátnej_plochy\|Podporované formáty zemepisnej dĺžky/šírky\]\]

- poloha vzhľadom na základný alebo greenwichský poludník miesta v desiatkovej alebo stupňovej sústave. Napríklad platné hodnoty sú -124.3647, 124°52'21.92\\V, V124º52'21.92\\ alebo 124:52:21.92. Tieto hodnoty môžete nastaviť prostredníctvom pohľadu Zemepis vyhľadaním miesta alebo prostredníctvom mapovej služby v zobrazení Miesto. Pozri: [Podporované formáty zemepisnej dĺžky/šírky](wiki:Gramps_6.0_Wiki_Manual_-_Vkladanie_a_úprava_údajov:_podrobné_-_časť_2#Podporované_formáty_dĺžky.2Štátnej_plochy)

  - 

- jedinečný záznam na identifikáciu miesta. Nechajte vygenerovať Gramps.

- kód tohto miesta. Napríklad smerové číslo oblasti alebo poštové smerovacie číslo.

- - 

{{-}}

### Stránky s kartami editora miest

}

Karty predstavujú nasledujúce kategórie údajov o mieste:

#### Zatvorené podľa

![[_media/PlaceEditor-EnclosedBy-tab-example-50.png|Obrázok {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Záložka "Uzavreté podľa" z dialógového okna "Editor miesta" - príklad]]

  
Miesta v programe Gramps sú uložené v hierarchii. Záložka umožňuje prepojiť toto miesto s inými miestami, vyššie v hierarchii, ktoré ho obklopujú. Každé prepojenie pozostáva z miesta a voliteľného rozsahu dátumu. Tlačidlá , a umožňujú pridať, upraviť a odstrániť prepojenie. Všimnite si, že tlačidlá a sú dostupné len vtedy, keď je odkaz vybraný zo zoznamu. Vo všeobecnosti bude krajina miestom najvyššej úrovne a nebude prepojená so žiadnym iným miestom.

Pozrite si tiež: \[Gramps_6.0_Wiki_Manual\_-\_Gramplets#Enclosed_By\|Pripojené podľa\]\] Gramplety {{-}}

##### Vyberte selektor miesta

![[_media/SelectPlace-SelectorDialog-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Výber miesta - dialógové okno výberového systému - príklad]]

Dialógové okno umožňuje prepojenie na už existujúce miesto a po jeho výbere sa otvorí v

Na filtrovanie zoznamu na základe jednej z možností z rozbaľovacieho zoznamu môžete použiť tlačidlo :

- **Názov obsahuje** (predvolené)

{{-}}

##### Editor odkazu miesta

![[_media/PlaceReferenceEditor-dialog-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Editor odkazu miesta - dialógové okno - príklad]]

V druhej časti okna je zobrazených sedem záložiek poznámkového bloku obsahujúcich rôzne kategórie informácií. Kliknutím na záložku zobrazíte alebo upravíte jej obsah. V spodnej časti okna sa nachádzajú tlačidlá a . Kliknutím na sa použijú všetky zmeny vykonané na všetkých kartách a dialógové okno sa zatvorí. Kliknutím na tlačidlo sa okno zatvorí bez uplatnenia akýchkoľvek zmien.

{{-}}

#### Alternatívne názvy

Záložka umožňuje zobraziť a upraviť iné názvy, pod ktorými môže byť miesto známe. Záložka obsahuje zoznam všetkých ostatných názvov miesta uložených v databáze. Tlačidlá , a umožňujú pridávať, upravovať a odstraňovať záznam o názve. Všimnite si, že tlačidlá a sú dostupné len vtedy, keď je názov vybraný zo zoznamu.

#### Citácie zdrojov

Záložka vám umožňuje zobraziť a upraviť zdroje relevantné pre dané miesto. V centrálnej časti okna sa nachádzajú všetky takéto odkazy na zdroje uložené v databáze. Tlačidlá , a umožňujú pridať, upraviť a odstrániť odkaz na zdroj súvisiaci s miestom. Všimnite si, že tlačidlá a sú dostupné len vtedy, keď je zdrojový odkaz vybraný zo zoznamu.

#### Poznámky

  
Na karte sa zobrazujú všetky komentáre alebo poznámky týkajúce sa miesta. Ak chcete pridať poznámku alebo upraviť existujúce poznámky, jednoducho upravte text v poli na zadávanie textu.

#### Galéria

  
Záložka umožňuje ukladať a zobrazovať fotografie a iné mediálne objekty súvisiace s daným miestom. V strednej časti okna sa nachádza zoznam všetkých takýchto mediálnych objektov a náhľad miniatúr obrázkových súborov. Ostatné objekty, ako sú zvukové súbory, filmové súbory atď. sú reprezentované všeobecnou ikonou Gramps. Tlačidlá , , a umožňujú pridať nový obrázok, pridať odkaz na existujúci obrázok, upraviť existujúci obrázok a odstrániť odkaz na miesto mediálneho objektu. Všimnite si, že tlačidlá a sú dostupné len vtedy, keď je mediálny objekt vybraný zo zoznamu.

#### Internet

  
Záložka obsahuje internetové adresy relevantné pre dané miesto. V spodnej časti okna sa nachádza zoznam všetkých takýchto internetových adries uložených v databáze. V hornej časti sa zobrazujú podrobnosti o aktuálne vybranej adrese v zozname (ak existuje). Tlačidlá , a umožňujú pridať, upraviť a odstrániť internetovú adresu. Tlačidlo (reprezentované ikonou so zelenou šípkou a žltým kruhom) otvorí prehliadač a prenesie vás na webovú stránku zodpovedajúcu zvýraznenej internetovej adrese. Všimnite si, že tlačidlo , a sa sprístupnia len vtedy, keď je adresa vybraná zo zoznamu.

#### Odkazy

  
Záložka označuje všetky záznamy v databáze (udalosti alebo obrady SPD), ktoré sa vzťahujú na dané miesto. Tieto informácie nie je možné upraviť z dialógového okna . Namiesto toho je potrebné vyvolať príslušný záznam databázy (napr. udalosť narodenia) a upraviť jeho odkaz na miesto.

{{-}}

### Dialógové okno Editor názvu miesta

![[_media/PlaceNameEditor-dialog-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Dialógové okno Editor názvu miesta - predvolené]]

K dialógovému oknu sa dostanete z dialógového okna .

Dialógové okno umožňuje pridať/upraviť nasledujúce informácie:

- názov miesta

- dátumový rozsah, v ktorom je miesto platné

  - Tlačidlo

- Jazyk, v ktorom je názov napísaný. Platné hodnoty sú dvojznakové kódy ISO, napríklad: en,fr, de, nl. Úplný zoznam platných kódov [1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes).

{{-}}

### Podporované formáty zemepisnej dĺžky/šírky

Pri vytváraní/úprave miesta sú možné formáty použité pre zemepisnú dĺžku/šírku :

<table>
<thead>
<tr>
<th colspan="2"><p>Formáty zemepisnej dĺžky a šírky</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p>D.D4</p></td>
<td><p>zápis stupňov, 4 desatinné miesta</p>
<dl>
<dt></dt>
<dd>
napr. +12.0154 , -124.3647
</dd>
<dd>
4 <a href="https://wikipedia.org/wiki/Decimal_degrees#Precision">desatinné miesta presnosti zemepisnej dĺžky</a> umožňuje aproximáciu 11,132 metra (36,5223097 stopy) na rovníku.
</dd>
</dl></td>
</tr>
<tr>
<td><p>D.D8</p></td>
<td><p>zápis stupňov, 8 desatinných miest (<a href="https://wikipedia.org/wiki/Decimal_degrees#Precision">presnosť</a> ako ISO-DMS)</p>
<dl>
<dt></dt>
<dd>
napr. +12,01543265 , -124,36473268
</dd>
</dl></td>
</tr>
<tr>
<td><p>DEG</p></td>
<td><p>zápis stupňov, minút, sekúnd</p>
<dl>
<dt></dt>
<dd>
napr. 50°52'21.92 "S , 124°52'21.92 "V (symbol ° má kód UTF-8 c2b00a)
</dd>
<dd>
alebo S50º52'21.92" , V124º52'21.92" (symbol º má kód UTF-8 c2ba0a)
</dd>
<dd>
Znak pre sekundy môže byť buď jedna dvojitá úvodzovka "
</dd>
<dd>
alebo dve jednoduché úvodzovky
</dd>
<dd>
Písmená S/J/Z/V sa môžu umiestniť pred alebo za číslice.
</dd>
</dl></td>
</tr>
<tr>
<td><p>DEG-</p></td>
<td><p>zápis stupňov, minút, sekúnd s :</p>
<dl>
<dt></dt>
<dd>
napr. -50:52:21.92 , 124:52:21.92
</dd>
</dl></td>
</tr>
<tr>
<td><p>ISO-D</p></td>
<td><p>ISO 6709 zápis stupňov</p>
<dl>
<dt></dt>
<dd>
t.j. ±DD.DDDD±DDD.DDDD
</dd>
</dl></td>
</tr>
<tr>
<td><p>ISO-DM</p></td>
<td><p>ISO 6709 zápis stupňov, minút</p>
<dl>
<dt></dt>
<dd>
t. j. ±DDMM.MMM±DDDMM.MMM
</dd>
</dl></td>
</tr>
<tr>
<td><p>ISO-DMS</p></td>
<td><p>ISO 6709 zápis stupňov, minút, sekúnd</p>
<dl>
<dt></dt>
<dd>
t. j. ±DDMMSS.SS±DDDMMSS.SS
</dd>
</dl></td>
</tr>
</tbody>
</table>

{{-}}

## Úprava informácií o zdrojoch

V niektorom z pohľadov kategórie môžete vybrať alebo vytvoriť nový zdroj, alebo ak ste zvolili alebo tlačidlá, potom sa zobrazí dialógové okno editora .

### Dialógové okno Nový zdroj

![[_media/NewSource-editor-dialog-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Nový zdroj - dialógové okno editora - príklad]]

V prípade dialógového okna editora vám všeobecné informácie v hornej časti okna umožňujú definovať základné informácie o zdroji: jeho , , a . Tieto informácie môžete zadať priamo do priľahlých polí.

- Názov zdroja.

- Autori zdroja.

- Informácie o publikácii, napríklad mesto a rok vydania, názov vydavateľa, ...

- Uveďte krátky názov, ktorý sa používa na triedenie, archiváciu a vyhľadávanie záznamov o zdroji.

  - Prepínač ikony zámku.

- jedinečný záznam na identifikáciu zdroja. Nechajte generovať Gramps.

- - 

{{-}}

### Nové stránky na karte Zdroj

Záložky poskytujú nasledujúce informačné kategórie zdrojových údajov:

#### Poznámky

  
Záložka poskytuje miesto na zaznamenanie poznámok alebo komentárov o zdroji. Ak chcete pridať poznámku alebo upraviť existujúce poznámky, jednoducho upravte text v poli na zadávanie textu. V záložke sa môžu zobrazovať len primárne objekty: Objekt Osoba, Rodina, Udalosť, Miesto alebo Médium. Sekundárne objekty, ako sú Názvy a Atribúty, sú prístupné len prostredníctvom primárnych objektov, ku ktorým patria.

#### Galéria

  
Záložka umožňuje ukladať a zobrazovať fotografie a iné mediálne objekty spojené s daným zdrojom (napríklad fotografiu rodného listu). V strednej časti okna sa nachádza zoznam všetkých takýchto objektov a náhľad miniatúr obrazových súborov. Ostatné objekty, ako sú zvukové súbory, filmové súbory atď. sú reprezentované všeobecnou ikonou Gramps. Tlačidlá , , a umožňujú pridať nový obrázok, pridať odkaz na existujúci obrázok, upraviť existujúci obrázok a odstrániť prepojenie mediálneho objektu so vzťahom. Všimnite si, že tlačidlá a sú dostupné len vtedy, keď je mediálny objekt vybraný zo zoznamu.

#### Atribúty

  
Na karte sa zobrazujú dvojice "Kľúč/Hodnota", ktoré môžu byť spojené so zdrojom. Tieto sú podobné ako "Atribúty" používané pre iné typy záznamov Gramps. Rozdiel medzi týmito dvojicami Kľúč/Hodnota a Atribútmi je v tom, že Atribúty môžu mať odkazy na zdroj a poznámky, zatiaľ čo údaje Kľúč/Hodnota nemusia.

<!-- -->

  
V strednej časti okna sa nachádza zoznam všetkých existujúcich dvojíc Kľúč/Hodnota. Tlačidlá a umožňujú pridávať a odstraňovať páry. Ak chcete upraviť text Kľúč alebo Hodnota, najprv vyberte požadovaný údaj. Potom kliknite do bunky Kľúč alebo Hodnota tejto položky a zadajte svoj text. Keď skončíte, kliknite mimo bunky, čím ukončíte režim úprav.

#### Archívy

![[_media/NewSource-Repositories-tab-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Záložka "Archívy" z dialógového okna "Nový zdroj" - príklad]]

  
Záložka zobrazuje odkazy na archívy, v ktorých sa zdroj nachádza. Zoznam je možné zoradiť podľa ľubovoľného nadpisu stĺpca: , , a . Dvojkliknutím na záznam môžete záznam zobraziť a upraviť. Môžete tiež upraviť odkaz. Tlačidlá na boku karty umožňujú pridať nový archív, prepojiť sa s existujúcim archívom (alebo ho zdieľať), upraviť odkaz na archív alebo odstrániť odkaz.

{{-}}

##### Selektor Výber archívu

![[_media/SelectRepository-SelectorDialog-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Výber archívu - dialógové okno selektora - príklad]]

Dialógové okno selektora umožňuje prepojenie na už existujúci archív a po jeho výbere sa otvorí v

Na filtrovanie zoznamu na základe jednej z možností z rozbaľovacieho zoznamu môžete použiť tlačidlo :

- **Názov obsahuje** (predvolené)
- *Názov neobsahuje*
- *ID obsahuje*
- *ID neobsahuje*
- *Posledná zmena obsahuje*
- *Posledná zmena neobsahuje*

{{-}}

#### Odkazy

  
Záložka obsahuje zoznam všetkých záznamov v databáze, ktoré odkazujú na tento zdroj, ak existujú. Zoznam je možné zoradiť podľa ľubovoľného nadpisu stĺpca: , alebo . Dvojkliknutím na záznam môžete zobraziť a upraviť záznam.

{{-}}

## Úprava zdrojových citácií

Citácie spájajú zdroj s iným objektom a umožňujú poskytnúť ďalšie informácie o zdroji. Citácie možno pripojiť k veľkému počtu objektov,

- [Ľudia a rôzne informácie o ľuďoch](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1/sk#Úprava_informácií_o_ľuďoch) (ako je ich meno, adresa atď.),
- [Relationships (Families) and various information about relationships](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1#Editing_information_about_relationships),
- [Events and various information about events](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_2/sk#Editing_information_about_events),
- [Mediálne objekty a atribúty mediálnych objektov](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_2/sk#Editing_information_about_media_objects),
- [Miesto a rôzne informácie o mieste](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_2/sk#Editing_information_about_places),
- [Adresy úložísk](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_2/sk#Editing_information_about_repositories).

Pre každý objekt je k dispozícii spoločná sada tlačidiel:

-  (Vytvorenie a pridanie novej citácie a nového zdroja). Zobrazí sa prázdne dialógové okno Citácie.

-  (Pridať existujúcu citáciu alebo zdroj). Zobrazí sa dialógové okno Výber zdroja alebo citácie.

-  (Upraviť vybranú citáciu). Tým sa vyvolá dialógové okno Citácia s predvyplnenými informáciami o citácii a zdroji.

-  (Odstráňte existujúcu citáciu). Týmto odstránite citáciu z objektu. Neodstráni samotnú citáciu, ktorá by potom mohla byť pripojená k inému objektu.

Všimnite si, že a sú k dispozícii len vtedy, keď bola citácia vybraná.

{{-}}

### Výber zdroja alebo výber citácie

![[_media/SelectSourceOrCitation-SelectorDialog-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Výber zdroja alebo citácie - dialógové okno selektora - príklad]]

Keď pridaní existujúcej citácie alebo zdroja sa zobrazí dialógové okno .

To umožňuje vybrať buď existujúci zdroj, alebo existujúcu citáciu (spolu s príslušným zdrojom). Kliknutím na odkrývací trojuholník vedľa zdroja sa zobrazia citácie spojené s týmto zdrojom. Ak by napríklad jedným z vašich zdrojov bola kniha, potom by sa citácie zvyčajne vzťahovali na stranu (alebo strany) v knihe. Ak už máte citáciu, ktorá odkazuje na konkrétnu stranu knihy, potom by ste mohli vybrať túto citáciu, ktorá by sa potom zdieľala. Na druhej strane, ak by tento objekt potreboval odkaz na novú stránku, potom by ste vybrali zdroj a v následnom dialógovom okne zadali novú stránku.

Na filtrovanie zoznamu na základe jednej z možností z rozbaľovacieho zoznamu môžete použiť tlačidlo :

- **Zdroj: Názov alebo citácia: Obsahuje zväzok/stranu**(predvolené nastavenie)
- *Zdroj: Názov alebo citácia: Zväzok/strana neobsahuje*
- *ID obsahuje*
- *ID neobsahuje*
- *Posledná zmena obsahuje*
- *Posledná zmena neobsahuje*

{{-}}

### Dialógové okno Nová citácia

![[_media/NewCitation-editor-dialog-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Nová citácia - dialógové okno editora - príklad]]

Po výbere citácie alebo zdroja, alebo ak ste vybrali tlačidlá alebo , zobrazí sa dialógové okno .

Dialógové okno obsahuje jednu časť s názvom . {{-}}

#### Citačné informácie

V časti sú uvedené podrobnosti súvisiace s konkrétnym odkazom na tento zdroj: , , a . Úroveň dôveryhodnosti môžete vybrať z rozbaľovacej ponuky . Ostatné údaje môžete zadať do príslušných polí na zadávanie textu.

- Dátum spojený s týmto odkazom na zdroj. Zvyčajne sa používa na uloženie dátumu, kedy boli údaje vložené do pôvodného zdrojového dokumentu (nie dátumu, kedy udalosť nastala).

- 

-   
  Konkrétne miesto v odkazovanej informácii. V prípade publikovaného diela to môže zahŕňať zväzok viaczväzkového diela a číslo strany (strán). V prípade periodika to môže zahŕňať číslo zväzku, čísla a strany. V prípade novín by to mohlo zahŕňať číslo stĺpca a číslo strany. V prípade nepublikovaného zdroja to môže byť číslo listu, číslo strany, číslo rámu atď. Sčítací záznam môže mať okrem čísla strany aj číslo riadku alebo číslo bytu a rodiny.

-   
  Vyjadruje kvantitatívne hodnotenie dôveryhodnosti informácie zo strany predkladateľa na základe podporných dôkazov. Nie je určený na to, aby eliminoval potrebu príjemcu vyhodnotiť dôkaz sám.

  - Veľmi nízka = nespoľahlivý dôkaz alebo odhadované údaje.
  - Nízka = pochybná spoľahlivosť dôkazov (rozhovory, sčítanie ľudu, ústne genealógie alebo možnosť zaujatosti, napríklad autobiografia).
  - Normálna - ??
  - Vysoká = Sekundárne dôkazy, údaje oficiálne zaznamenané niekedy po udalosti.
  - Veľmi vysoká = Použité priame a primárne dôkazy alebo podľa dominancie dôkazov.

Ak je citácia zdieľaná, zobrazí sa varovná ikona .  

{{-}}

##### Selektor Výber zdroja

![[_media/SelectSource-selector-dialog-example-50.PNG|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Výber zdroja - dialógové okno selektora - príklad]]

Dialógové okno umožňuje prepojenie na už existujúci zdroj.

Na filtrovanie zoznamu na základe jednej z možností z rozbaľovacieho zoznamu môžete použiť tlačidlo :

- **Názov obsahuje** (predvolené)
- *Názov neobsahuje*
- *Autor obsahuje*
- *Autor neobsahuje*
- *ID obsahuje*
- *ID neobsahuje*
- *Posledná zmena obsahuje*
- *Posledná zmena neobsahuje*

{{-}}

##### Stránky záložky sekcie s informáciami o citáciách

Záložky poskytujú nasledujúce informačné kategórie citačných údajov:

###### Poznámky

Záložka poskytuje miesto na zaznamenanie poznámok alebo komentárov k citácii. V strednej časti okna sú uvedené všetky poznámky k tejto citácii a je tu náhľad na začiatok poznámky. Tlačidlá , , , , a umožňujú pridať novú poznámku, zdieľať vybranú poznámku, upraviť vybranú poznámku, odstrániť vybranú poznámku a presunúť vybranú poznámku nahor alebo nadol v zozname poznámok. Všimnite si, že , , , a sa sprístupnia len vtedy, keď je zo zoznamu vybraný mediálny objekt. Odstránením poznámky sa z tejto citácie odstráni iba poznámka, samotná poznámka sa neodstráni. Pozrite si prosím [podrobnosti o úprave poznámok](wiki:Gramps_6.0_Wiki_Manual_-_Vkladanie_a_úprava_údajov:_podrobne_-_časť_2#Upravovanie_informácií_o_poznámkach).

###### Galéria

Záložka umožňuje ukladať a zobrazovať fotografie a iné mediálne objekty súvisiace s danou citáciou (napríklad fotografiu strany knihy alebo strany zo sčítania ľudu). V strednej časti okna sa nachádza zoznam všetkých takýchto objektov a náhľad miniatúr obrazových súborov. Ostatné objekty, ako sú zvukové súbory, filmové súbory atď. sú reprezentované všeobecnou ikonou Gramps. Tlačidlá , , a umožňujú pridať nový obrázok, pridať odkaz na existujúci obrázok, upraviť existujúci obrázok a odstrániť prepojenie mediálneho objektu s citáciou. Všimnite si, že tlačidlá a sú dostupné len vtedy, keď je mediálny objekt vybraný zo zoznamu. Pozrite si [podrobnosti o úprave odkazov na médiá](wiki:Gramps_6.0_Wiki_Manual_-_Vkladanie_a_úprava_údajov:_podrobne_-_časť_2/sk#Úprava_odkazov_na_mediálne_objekty).

###### Atribúty

Na karte sa zobrazujú dvojice "Kľúč/Hodnota", ktoré môžu byť spojené s citáciou. Sú podobné "Atribútom" používaným pre iné typy záznamov Gramps. Rozdiel medzi týmito dvojicami Kľúč/Hodnota a Atribútmi je v tom, že Atribúty môžu obsahovať citácie zdrojov a poznámky, zatiaľ čo údaje Kľúč/Hodnota nie.

V strednej časti okna sa nachádza zoznam všetkých existujúcich dvojíc Kľúč/Hodnota. Tlačidlá a umožňujú pridávať a odstraňovať páry. Ak chcete upraviť text Kľúč alebo Hodnota, najprv vyberte požadovanú položku. Potom stlačte tlačidlo . vybrať Kľúč, alebo kliknite do bunky Kľúč alebo Hodnota danej položky a napíšte svoj text. Keď skončíte, kliknite mimo bunky, čím ukončíte režim úprav.

###### Odkazy

Na karte sú uvedené všetky záznamy databázy, ktoré odkazujú na tento zdroj, ak existujú. Zoznam je možné zoradiť podľa ľubovoľného nadpisu stĺpca: , alebo . Dvojkliknutím na záznam môžete zobraziť a upraviť záznam.

{{-}}

## Úprava informácií o archívoch

Po výbere zdroja alebo ak ste zvolili tlačidlá alebo , zobrazí sa dialógové okno .

### Dialógové okno Nový archív

![[_media/NewRepository-editor-dialog-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Nový archív - dialógové okno editora - príklad]]

Zobrazujú sa nasledujúce polia:

-  archívu (kde sú uložené zdroje).

- archívu môžu byť fyzické alebo virtuálne štruktúry, kde sú uložené genealogické zdroje a zdroje rodinnej histórie:

  - *Album*
  - *Archív*
  - *Kníhkupectvo*
  - *Cintorín*
  - *Cirkev*
  - *Zbierka*
  - **Knižnica** (predvolené)
  - *Trezor*
  - *Neznámy*
  - *Webová stránka*

-   
  jedinečný záznam na identifikáciu archívu. Nechajte prázdny, aby ho vygeneroval Gramps.

- Prepínač ikony zámku.

- - 

{{-}}

### Nové stránky karty archívu

Záložky predstavujú nasledujúce kategórie údajov archívu:

#### Adresy

  
Záložka umožňuje zobrazovať a zaznamenávať rôzne adresy archívu.

<!-- -->

  
V spodnej časti okna sa nachádzajú všetky adresy uložené v databáze. V hornej časti sa zobrazujú podrobnosti o aktuálne vybranej adrese v zozname (ak existuje). Tlačidlá , a umožňujú zodpovedajúcim spôsobom pridať, upraviť a odstrániť záznam adresy z databázy. Všimnite si, že tlačidlá a sú dostupné len vtedy, keď je adresa vybraná zo zoznamu.

#### Internet

  
V záložke sa zobrazujú internetové adresy relevantné pre archív. V spodnej časti sa nachádzajú všetky takéto internetové adresy a sprievodné popisy. V hornej časti sa zobrazujú podrobnosti o aktuálne vybraných adresách v zozname (ak existujú). Tlačidlá , a umožňujú pridať, upraviť a odstrániť internetovú adresu. Tlačidlo "Prejsť" (reprezentované ikonou so zelenou šípkou a žltým kruhom) otvorí internetový prehliadač a prenesie vás priamo na zvýraznenú stránku. Všimnite si, že tlačidlá a sú k dispozícii len vtedy, keď je adresa vybraná zo zoznamu.

#### Poznámky

  
Záložka poskytuje miesto na zaznamenávanie poznámok alebo komentárov k archívu. Ak chcete pridať poznámku alebo upraviť existujúce poznámky, jednoducho upravte text v poli na zadávanie textu.

#### Odkazy

  
Na karte sú uvedené všetky záznamy v databáze, ktoré sa vzťahujú na daný archív. Zoznam je možné zoradiť podľa ľubovoľného nadpisu stĺpca: , alebo . Dvojkliknutím na záznam môžete zobraziť a upraviť príslušný záznam.

{{-}}

## Úprava informácií o poznámkach

Po výbere zdroja alebo ak ste vybrali možnosť alebo tlačidlá, zobrazí sa dialógové okno editora .

Pozrite si tiež: Poznámky: \* [Kategória Poznámky](wiki:Gramps_6.0_Wiki_Manual_-_Categories/sk#Kategória_Poznámky)

### Dialógové okno editora Nová poznámka

![[_media/NewNote-editor-dialog-example-with-context-menu-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Nová poznámka - dialógové okno editora - príklad]]

Pri vytváraní novej poznámky alebo pri úprave existujúcej poznámky sa zobrazí dialógové okno editora . Sú v ňom dve záložky, záložka **Poznámka** a záložka **Odkazy**.

#### Karta Poznámka

Karta je miestom na pridávanie poznámok k Osobám, Zdrojom atď. Karta umožňuje opätovne zoradiť poznámky v poradí, v akom ich chcete vidieť. Rovnako ako na ostatných kartách môžete pridávať nové záznamy (poznámky), zdieľať existujúce poznámky s iným objektom a odstraňovať poznámky z tohto objektu. Karta Poznámka má tieto prvky

:\* Panel nástrojov na použitie štýlov na poznámky. Môžete vybrať a použiť jeden z tlačidiel nástrojov alebo nastaviť požadované hodnoty a začať písať.

::\* Kurzíva : bežná funkcia známa z textových editorov

::\* Tučné písmo : bežná funkcia známa z textových editorov

::\* Podčiarknutie : bežná funkcia známa z textových editorov

::\* Späť : Vráti späť poslednú akciu.

::\* Znova : Opätovné použitie poslednej akcie.

::\* Rozbaľovací zoznam pre výber písma: základný výber písma zobrazujúci všetky písma nainštalované vo vašom operačnom systéme.

::\* Veľkosť písma: výber veľkosti písma, ktoré sa má použiť pre váš text.

::\* ![[_media/22x22-gramps-font-color.png]]Farba písma: výber farby písma.

::\* ![[_media/22x22-gramps-font-bgcolor.png]]Farba pozadia: pridá zadanému textu farbu pozadia.

::\* Odkaz: Otvorí , ktorý vám umožní vytvoriť interný odkaz na položku v programe Gramps, napríklad na osobu, rodinu, udalosť, poznámku atď.

::\* Vyčistiť označenie: Označte text, aby ste odstránili značky, ktoré ste umiestnili na poznámku.

:\* Kontextová ponuka na textovom zobrazení.

  
  
Najdôležitejšou položkou v tejto kontextovej ponuke je výber pravopisu. Ponúka sa vám výber jazykov nainštalovaných v systéme so zapnutou kontrolou pravopisu.

:\* Textový pohľad, v ktorom môžete písať svoju poznámku.

:\* Niektoré vlastnosti vašej poznámky

::\* Začiarkovacie políčko : Poznámky v programe Gramps sa považujú za preformátované, aby sa obsah prispôsobil veľkosti a formátovaniu stránky správy pre čo najharmonickejšiu prezentáciu. V predvolenom nastavení sa automaticky ignorujú nové riadky (riadkovanie & carriage returns) a biele medzery, aby sa vytvorili úplné odseky, ktoré sú definované prázdnym riadkom medzi dvoma blokmi textu.  
Pokiaľ je začiarknutá voľba , Gramps bude predpokladať, že biele miesta a nové riadky, ktoré ste do poznámok vložili, sú dôležité. Použite *Preformátované* pre tabuľky, doslovné prepisy a podobne. Použitie jednoliateho písma pomôže udržať šírku predformátovaných stĺpcov & okraje predvídateľné.  
Snažte sa nepoužívať preformátované, pokiaľ to nie je absolútne nevyhnutné, vytvorené správy budú plynúť prirodzenejšie.

::\* Súkromie je rovnaké ako pri ostatných objektoch. Jedným jednoduchým kliknutím môžete označiť poznámku, ktorá sa má považovať za súkromnú, takže Gramps môže túto poznámku odstrániť zo všetkých vytvorených výstupov.

::\* } Editor poznámky - prepojenie textu\]\] ![[_media/Note-LinkEditor-dialog-default-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Editor odkazu - dialógové okno - príklad]]

má nasledujúce možnosti:

- } umožňuje vytvoriť externý odkaz na internetovú adresu ([<abbr title="Uniform Resource Locator, tiež známy ako webová adresa">URL</abbr>](https://en.m.wikipedia.org/wiki/URL)) alebo položku v programe Gramps, napríklad [EVENT](wiki:Udalosti), Rodina, Médiá, Poznámka, Osoba, [Place](wiki:Miesta), Úložisko, [Source](wiki:Zdroje) alebo [Citation](wiki:Citácie).

- Tlačidlo : otvorí dialógové okno výberu existujúcich položiek v kategórii zadanej v poli Typ prepojenia.

  - 

- }

  - tlačidlo : otvorí dialógové okno editora pre zadanú položku Gramps

- 

Pozri tiež:

- [Editor internetovej adresy](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1/sk#Editor_internetovej_adresy)
- [Note Link Report](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_6#Note_Link_Report)

{{-}}

### Značenie a predformátovanie poznámok v správach

Do poznámok možno pridať značky ako **tučné**, farba, <u>podčiarknutie</u>, ... Poznámka môže byť predformátovaná alebo nie. Záleží na type výstupu, ako sa táto značka zobrazí. Tu je uvedený prehľad toho, čo môžete očakávať.

- **Pdf** a **priama tlač** (na tlačiareň alebo do súboru) plne podporujú označovanie a predformátované nastavenie
- **ascii** tlač z pochopiteľných dôvodov odstráni všetky značky z poznámok
- **LaTeX** výstup interpretuje značenie podľa svojich najlepších možností. LaTeX nie je ako typografický jazyk vhodný na pridávanie vlastných štýlov. To by narušilo výhody, ktoré LaTex ponúka. Preto sa robí nasledovné:

:\* Podporované je **tučné písmo**, <u>podčiarknutie</u> a *kurzíva*.

:\* veľkosť písma je mapovaná na ukazovatele veľkosti LaTeXu fuzzy spôsobom

:\* jednoliate písma sa zobrazujú ako jednoliate písmo

:\* farba a písmo nie sú podporované

:\* preformátovanie je spracované správne

- **Naratívny web**. Mnoho ľudí používa správu Narrative Web ako jednoduchý spôsob práce s údajmi. Táto zostava sa snaží rešpektovať značkovanie v poznámkach. Ide o interpretovaný preklad, nie je to preklad jedna k jednej.
- Výstup **ODF** v súčasnosti nepodporuje značkovanie.
- Výstup **RTF** v súčasnosti nepodporuje značkovanie.
- Výstup **html** momentálne nepodporuje značkovanie.

{{-}}

[Category:Sk:Documentation](wiki:Category:Sk:Documentation)
