---
title: Gramps 6.0 Wiki Manual - Filters/sk
categories:
- Filters
- Sk:Documentation
- Stub
managed: false
source: wiki-scrape
wiki_revid: 127090
wiki_fetched_at: '2026-05-30T20:05:46Z'
lang: sk
---

{{#vardefine:chapter\|16}} {{#vardefine:figure\|0}} ![[_media/DefineFilter-dialog-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}}  - dialógové okno - predvolené]] Zoznamy všetkých pravidiel filtrovania aktuálne definovaných v programe Gramps. Každé z týchto pravidiel je k dispozícii na použitie pri vytváraní vlastných filtrov.

Pravidlá sú uvedené podľa ich [kategórie](wiki:Gramps_6.0_Wiki_Manual_-_Filters/sk#Ktoré_filtre_v_ktorej_kategórii.3F).

## Filter vs. vyhľadávanie

V programe Gramps môžete údaje vyhľadávať dvoma spôsobmi: Vyhľadávanie a Filter. Vyhľadávanie používa [Search Bar](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window#Search_bar) nad zobrazením zoznamu (napríklad Ľudia, Rodiny atď.). Filter sa môže používať v kombinácii s funkciou Vyhľadávanie alebo samostatne v bočnom/spodnom paneli Gramplets. [Search Bar](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window#Search_bar) sa zobrazí len vtedy, keď je celý bočný panel zatvorený. Lišty Grampletu môžete zobraziť alebo skryť zmenou výberu v ponukách alebo . Vyhľadávanie a filter fungujú úplne odlišne a je užitočné tieto rozdiely pochopiť:

- *Vyhľadávanie*' - [Search Bar](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window#Search_bar) prehľadáva databázu tak, ako sa zobrazuje v riadkoch a stĺpcoch na obrazovke. Funkciu Vyhľadávanie budete pravdepodobne chcieť používať najčastejšie, pretože je rýchla a najjednoduchšia. Rýchlosť a jednoduchosť si však vyžaduje určité obmedzenia (pozri nižšie).

  
Napríklad, ak máte v Nastaveniach nastavené Zobrazenie mena na zobrazenie "Priezvisko, Dané", potom môžete priradiť mená ako "Smith, J" a všetky správne riadky budú zodpovedať. Ak zmeníte spôsob zobrazovania mien (v Nastaveniach), potom môžete porovnať tento formát (napríklad "John Smith").

![[_media/wiki:Gramps_6.0_Wiki_Manual_-_Main_Window#Search_bar|[_media/MainWindow-SearchBar-sidebar-hidden-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Hlavné okno programu Gramps zobrazujúce [Vyhľadávací panel]]]]

- *Filter**- Filtre používajú prepracovanejší systém. Neobmedzuje sa na to, čo vidíte na obrazovke, ale skúma skutočné údaje vo všetkých menných poliach, a nie len to, čo sa zobrazuje v zobrazení. Zadaním viacerých slov sa vykoná porovnávanie fráz pre väčšinu textových polí. Riadok filtru Názov je však oveľa výkonnejší. S každým slovom vo vyhľadávaní v poli Názov sa pracuje samostatne, ako keby išlo o čiastkové vyhľadávanie v záznamoch nájdených pomocou predchádzajúceho vyhľadávaného slova. A súčasne sa vyhľadáva***all''''' v poliach Názov.

  
napr. vyhľadávanie mena "geo r." v databáze [príkladový strom](wiki:príklad.gramps) nájde 5 osôb: s rôznym "Jr." a "Sr." ako príponou a "George's" ako krstným a stredným menom. Alebo vyhľadávanie "garn ski ph" nájde Phoebe Emily, ktorá má rodné priezvisko Zieliński a náhradné manželské priezvisko Garner.

![[_media/wiki:Gramps_Glossary#tag|[_media/Sidebar-PeopleTreeView-Filter-TagDropDownList-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Bočný panel filtra Gramps pre zobrazenie Ľudia - [Tag]] príklad pop-up menu]]

Filtre je možné vytvárať a ovládať z ponuky } Filtre osôb - dialóg - príklad\]\]

Na vytvorenie nových alebo zobrazenie predtým vytvorených vlastných filtrov použite dialógový zoznam , kde sa *Názov kategórie* mení podľa kategórie, v ktorej sa nachádzate, napr:

-  Filtre osôb

-  Rodinné filtre

-  Filtre udalostí

-  Filtre miest

-  Filtre zdrojov

-  Filtre médií

-  Filtre archívov

-  Filtre poznámok

-  Filtre citácií

Keď sa v dialógovom okne nachádzate, máte k dispozícii nasledujúce možnosti z ikon na pravej strane:

-  

  
zobrazí dialógové okno a pridá nový (zatiaľ nepomenovaný) rámec vlastného filtra.

-  

  
otvorí dialógové okno a načíta existujúci vlastný filter na úpravu.

-  

  
vytvorí presnú kópiu vybraného filtra

-  

  
vyvolá dialógové okno s výsledkami, ktoré obsahuje zoznam zhody po úspešnom teste. Ak je test filtra neplatný, namiesto toho sa môže zobraziť chyba.

-  :

  
odstráni vybraný filter z kolekcie vlastných filtrov Gramps.

{{-}}

#### Dialógové okno Test filtra

![[_media/FilterTest-results-for-TestTheSelectedFilter-button-example-50.png|vpravo|thumb|450px|Obrázok {{#var:chapter}}.{{#var:figure}}.{{#var:figure}}+1}}}} Test filtra - príklad zoznamu výsledkov z filtrov osôb]]

Zoznam výsledkov úspešného dialógového okna môže byť prázdny, platný vlastný filter nemusí vyhovovať žiadnym záznamom. {{-}}

### Dialógové okno Definovať filter

![[_media/DefineFilter-dialog-default-60.png|vpravo|thumb|450px|Obrázok {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Definovať filter - dialóg - predvolený]]

Dialógové okno umožňuje vytvárať vlastné filtre, ktoré možno použiť na výber osôb zahrnutých do prehľadov, exportov a iných nástrojov a pomôcok. V skutočnosti ide o veľmi silný nástroj pri genealogickej analýze.

Ak chcete zobraziť zoznam všetkých filtrov (ak nejaké máte), ktoré ste predtým definovali, prejdite do dialógového okna z:

- Filtre na bočnom/dolnom paneli
- Vo väčšine kategórií cez menu , ktoré vyvolá dialógové okno , v ktorom môžete vybrať tlačidlo alebo .

V časti **Definícia** zadajte pre váš nový filter a pridajte , ktorý vám pomôže identifikovať tento filter v budúcnosti. Pomocou tlačidla pridajte do toľko pravidiel, koľko by ste chceli do svojho filtra.

<span ID="multiple_rule_options">Ak má filter viac ako jedno pravidlo, vyberte jedno z z rozbaľovacieho zoznamu, ktorý vám umožní vybrať, či

- **Musia sa použiť všetky pravidlá**(predvolené)
- Musí platiť aspoň jedno pravidlo
- Musí sa použiť presne jedno pravidlo

aby filter vytvoril zhodu. Ak má váš filter len jedno pravidlo, táto voľba nemá žiadny účinok.

- Zvoľte , aby sa pravidlo filtra obrátilo. Napríklad invertovanie pravidla **"má spoločného predka s I1"** bude vyhovovať všetkým, ktorí nemajú spoločného predka s touto osobou). (Začiarkavacie políčko nie je predvolene začiarknuté)</span>

{{-}}

### Dialógové okno Pridať pravidlo

.

![[_media/AddRule-selector-dialog-PersonFilters-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Pridať pravidlo - dialógové okno výberu - dostupné pre filtre osôb - príklad]]

Ak chcete definovať nový filter, kliknite na tlačidlo z dialógového okna , pretože to vyvolá dialógové okno

V podokne na ľavej strane sa zobrazujú dostupné pravidlá filtrovania usporiadané podľa kategórií v rozbaľovacom strome.

Pre podrobný odkaz na pravidlo filtra môžete buď použiť vyhľadávacie pole na vyhľadanie pravidla, alebo:

- Kliknutím na šípky zložíte/rozložíte príslušnú kategóriu.
- Vybrať pravidlo zo stromu kliknutím na jeho názov. Na pravej strane sa zobrazí názov, popis a hodnoty aktuálne vybraného pravidla.

Keď ste spokojní s výberom pravidla a jeho hodnotami, kliknutím na pridáte toto pravidlo do zoznamu pravidiel aktuálne upravovaného filtra. Kliknutím na tlačidlo sa pridanie pravidla do filtra zruší.

Pozri tiež \[\[Gramps_6.0_Wiki_Manuál\_-\_Filtre#Ktoré_filtre_v_ktorej_kategórii.3F\|Ktoré filtre v ktorej kategórii?\] {{-}}

<span id="Ktoré filtre v ktorej kategórii?">

## Ktoré filtrovacie pravidlá v ktorej kategórii?

V závislosti od použitej [Kategórie](wiki:Gramps_6.0_Wiki_Manual_-_Categories) sa vám zobrazí iná sada [filtra](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Filter) pravidiel. Pozrite si tiež [Summary of Gramplets](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Summary_of_Gramplets).

\*; Kategória Informačný panel: nie sú k dispozícii žiadne pravidlá filtrovania

\*; Kategória Ľudia, Vzťahy a Grafy: pravidlá pre [Filtre predkov](#Filtre_predkov), [Filtre citácií/zdrojov](#Filtre_citácií/zdrojov), [Filtre potomkov](#Filtre_potomkov), [Filtre udalostí](#Filtre_udalostí), [Family filters](#Family_filters), [Filtre všeobecných údajov](#Filtre_všeobecných_údajov) a [Filtre vzťahov](#Filtre_vzťahov).

\*; Kategória Rodiny: pravidlá pre [Filtre detí](#Filtre_detí), [Filtre citácií/zdrojov](#Filtre_citácií/zdrojov), [Filtre udalostí](#Filtre_udalostí), [Filtre otcov](#Filtre_otcov), [Všeobecné filtre](#Všeobecné_filtre) a [Filtre matiek](#Filtre_matiek).

\*; Udalosti a kategória Médiá: pravidlá pre [Citácie/filtre zdrojov](#Citácie/filtre_zdrojov) a [Všeobecné filtre](#Všeobecné_filtre).

\*; Kategória Miesta: pravidlá pre [Citácie/filtre zdrojov](#Citácie/filtre_zdrojov), [Všeobecné filtre](#Všeobecné_filtre) a [Pozičné filtre](#Pozičné_filtre).

\*; Kategória Zemepis (iba z bočného/spodného panela filtrov): pravidlá pre [Filtre predkov](#Filtre_predkov), [Filtre citácií/zdrojov](#Filtre_citácií/zdrojov), [Filtre potomkov](#Filtre_potomkov), [Filtre udalostí](#Filtre_udalostí), [Family filters](#Family_filters), [Všeobecné filtre](#General_filters) a [Filtre vzťahov](#Filtre_vzťahov).

\*; Kategória Zdroje, Archívy a Poznámky: k dispozícii sú pravidlá len pre [Všeobecné filtre](#General_filters).

\*; Kategória Citácie: pravidlá pre [Všeobecné filtre](#Všeobecné_filtre) a [Filtre zdrojov](#Filtre_zdrojov).

## Filtre predkov

Táto kategória pravidiel zahŕňa nasledujúce pravidlá, ktoré porovnávajú ľudí na základe ich rodových vzťahov s inými ľuďmi:

### Predok <filter> zodpovedá

Toto pravidlo priraďuje ľudí, ktorí sú predkami niekoho, komu zodpovedá zadaný filter. Zadaný názov filtra by sa mal vybrať z ponuky.

### Predok <osoby>

Toto pravidlo zodpovedá ľuďom, ktorí sú predkami zadanej osoby. Možnosť Inkluzívne určuje, či sa má zadaná osoba považovať za svojho vlastného predka (užitočné pri vytváraní prehľadov). ID môžete zadať do textového poľa alebo vybrať osobu zo zoznamu kliknutím na tlačidlo . V druhom prípade sa ID zobrazí v textovom poli po vykonaní výberu.

### Predok <osoby> vzdialený aspoň <N> generácií

Toto pravidlo porovnáva osoby, ktoré sú predkami zadanej osoby a sú od nej vzdialené aspoň N generácií v rodokmeni. Napríklad pri použití tohto pravidla s hodnotou 2 pre počet generácií sa nájde zhoda so starými rodičmi, prastarými rodičmi atď. ale nie s rodičmi zadanej osoby.

### Predok <osoby> nie je vzdialený viac ako <N> generácií

Toto pravidlo zodpovedá osobám, ktoré sú predkami zadanej osoby a nie sú od nej vzdialené viac ako N generácií v rodinnom strome. Napríklad pri použití tohto pravidla s hodnotou 2 pre počet generácií sa priradia rodičia a starí rodičia, ale nie prastarí rodičia atď. zadanej osoby.

### Predok záložiek osôb, ktoré nie sú vzdialené viac ako <N> generácií

### Predok predvolenej osoby nie vzdialenejší ako <N> generácií

### Duplicitní predkovia <osoby>

Zodpovedá osobám, ktoré sú dvojnásobnými alebo viacnásobnými predkami zadanej osoby

### Zhodujú sa osoby so spoločným predkom s <filter>

Toto pravidlo porovnáva ľudí, ktorí majú spoločných predkov s osobou, ktorej zodpovedá zadaný filter. Zadaný názov filtra by mal byť vybraný z ponuky.

### Ľudia so spoločným predkom s <osoba>

Toto pravidlo zodpovedá ľuďom, ktorí majú spoločných predkov so zadanou osobou.

## Filtre detí

Táto kategória pravidiel nájde rodiny, ktoré majú deti zodpovedajúce tomuto pravidlu:

### Rodiny, ktoré majú dieťa s id obsahujúcim <text>

Zodpovedá rodinám, v ktorých má dieťa zadané ID Gramps

### Rodiny s dieťaťom, ktoré obsahuje <meno>

Zodpovedá rodinám, v ktorých má dieťa zadané (čiastočné) meno

### Rodiny s dvojčatami

Zodpovedá rodinám s dvomi (alebo viacerými) deťmi, ktoré majú [rolu "Narodenie" pre vzťah k matke](wiki:Gramps_6.0_Wiki_Manual_-_Zadávanie_a_editácia_údajov:_detail_-_časť_1#Rozdelenie_detí) a rovnaké dátumy narodenia.

## Filtre citácií/zdrojov

Tieto pravidlá filtrovania závisia od zobrazenia

- [Kategória "Ľudia a vzťahy"](#People-.2C_and_Relationships_Category)
- [kategória Rodiny](#Families_Category)
- [Kategória udalostí](#Events_Category)
- [kategória miest](#Kategória_miest)
- [Kategória médií](#Media_Category)

### Kategória Ľudia a Vzťahy

Táto kategória obsahuje nasledujúce pravidlá citovania a zdroja:

#### Ľudia s <počet> zdroj

Zodpovedá ľuďom s určitým počtom položiek v zdroji. Hodnoty: Počet prípadov -- Počet musí byť väčší/menší/rovnaký ako

#### Ľudia s <citát>

Zodpovedá ľuďom s citáciou určitej hodnoty

#### Ľudia s <zdroj>

Zodpovedá ľuďom, ktorí majú zdroj s konkrétnou hodnotou. values: ID zdroja

====Osoby s aspoň jedným priamym zdrojom \>= <úroveň spoľahlivosti>====

### Kategória rodín

Táto kategória zahŕňa nasledujúce pravidlá citovania a zdrojov:

#### Rodiny s <počet> zdrojov

Zodpovedá rodinám s určitým počtom položiek v zdroji. Hodnoty: Počet výskytov -- Počet musí byť väčší/menší/rovnaký ako

====Rodiny s aspoň jedným priamym zdrojom \>= <úroveň spoľahlivosti>==== Zodpovedá rodinám s aspoň jedným priamym zdrojom s úrovňou(-ami) spoľahlivosti

#### Rodiny s <citáciou>

Zodpovedá rodinám s citáciou určitej hodnoty

#### Rodiny s <zdroj>

Zodpovedá rodinám, ktoré majú zdroj s konkrétnou hodnotou: ID zdroja

### Kategória udalostí

Táto kategória zahŕňa nasledujúce pravidlá citovania a zdroja:

#### Udalosti so zdrojom <počet>

Zodpovedá udalostiam s určitým počtom položiek v zdroji. Hodnoty: Počet prípadov -- Počet musí byť väčší/menší/rovnaký ako

====Udalosti s aspoň jedným priamym zdrojom \>= <úroveň spoľahlivosti>==== Zodpovedá udalostiam s aspoň jedným priamym zdrojom s úrovňou(-ami) spoľahlivosti

#### Udalosti so zdrojom zodpovedajúcim <filtru zdrojov>

#### Udalosti s <citátom>

Zodpovedá udalostiam s citáciou určitej hodnoty

### Kategória miest

Táto kategória zahŕňa nasledujúce pravidlá citácií a zdrojov:

#### Miesto s <počet> zdrojov

Zodpovedá miestam s určitým počtom položiek v zdroji. Hodnoty: Počet inštancií -- Počet musí byť väčší/menší/rovnaký ako

====Miesto s priamym zdrojom \>= <úroveň spoľahlivosti>==== Zodpovedá miestam s aspoň jedným priamym zdrojom s úrovňou(-ami) spoľahlivosti

#### Miesto s <citáciou>

Zodpovedá miestam s citáciou určitej hodnoty

#### Miest s <zdroj>

Zodpovedá miestam, ktoré majú zdroj s konkrétnou hodnotou: ID zdroja

### Kategória médií

Táto kategória zahŕňa nasledujúce pravidlá citovania a zdroja:

#### Médiá s <počet> zdrojov

Zodpovedá médiám s určitým počtom položiek v zdroji. Hodnoty: Počet inštancií -- Počet musí byť väčší/menší/rovnaký ako

====Médiá s priamym zdrojom \>= <úroveň spoľahlivosti>==== Zodpovedá médiám s aspoň jedným priamym zdrojom s úrovňou(-ami) dôveryhodnosti

#### Médiá s <citáciou>

Zodpovedá médiám s citáciou určitej hodnoty

#### Médiá s <zdroj>

Zodpovedá médiám, ktoré majú zdroj s konkrétnou hodnotou: ID zdroja

## Filtre potomkov

Táto kategória filtrov potomkov zahŕňa nasledujúce pravidlá, ktoré porovnávajú osoby na základe ich vzťahov potomkov s inými osobami:

### Potomok rodinného príslušníka <filter> zodpovedá

Zodpovedá ľuďom, ktorí sú potomkami alebo manželmi niekoho, komu zodpovedá filter

### Potomok rodinného príslušníka <osoba>

Toto pravidlo zodpovedá nielen ľuďom, ktorí sú potomkami zadanej osoby, ale aj manželom týchto potomkov.

### Potomok <filtra> zodpovedá

Toto pravidlo zodpovedá ľuďom, ktorí sú potomkami osoby, ktorej zodpovedá zadaný filter. Zadaný názov filtra by mal byť vybraný z ponuky.

### Potomok <osoby>

Toto pravidlo zodpovedá ľuďom, ktorí sú potomkami zadanej osoby. Možnosť Inkluzívne určuje, či sa má zadaná osoba považovať za svojho potomka (užitočné pri vytváraní prehľadov). ID môžete zadať do textového poľa alebo vybrať osobu zo zoznamu kliknutím na tlačidlo . V druhom prípade sa ID zobrazí v textovom poli po vykonaní výberu.

### Potomok <osoby> vzdialený aspoň <N> generácií

Toto pravidlo porovnáva osoby, ktoré sú potomkami zadanej osoby a sú od nej vzdialené aspoň N generácií v rodokmeni. Napríklad pri použití tohto pravidla s hodnotou 2 pre počet generácií sa priradia vnuci, pravnuci atď. ale nie deti zadanej osoby.

### Potomok <osoby> nie vzdialenejší ako <N> generácií

Toto pravidlo zodpovedá osobám, ktoré sú potomkami zadanej osoby a nie sú od nej vzdialené viac ako N generácií v rodokmeni. Napríklad pri použití tohto pravidla s hodnotou 2 pre počet generácií sa priradia deti a vnuci, ale nie pravnuci atď. zadanej osoby.

## Filtre udalostí

Tieto pravidlá filtrovania závisia od zobrazenia

- [Kategória Ľudia-, a vzťahy](#Ľudia-.2C_a_vzťahy_kategória_2)
- [kategória Rodiny](#Rodiny_kategória_2)

### Ľudia-, a vzťahy Kategória

Táto kategória zahŕňa nasledujúce pravidlá, ktoré priraďujú osoby na základe ich zaznamenaných udalostí:

#### Rodiny s neúplnými udalosťami

Toto pravidlo priraďuje ľudí, ktorým chýba dátum alebo miesto v akejkoľvek rodinnej udalosti niektorej z ich rodín.

#### Ľudia s neúplnými udalosťami

Toto pravidlo zodpovedá ľuďom, ktorým chýba dátum alebo miesto v akejkoľvek osobnej udalosti.

#### Ľudia s údajmi o <narodení>

Toto pravidlo zodpovedá ľuďom, ktorých udalosť narodenia zodpovedá zadaným hodnotám pre dátum, miesto a opis. Pravidlo vráti zhodu, aj keď sa udalosť narodenia osoby zhoduje s danou hodnotou čiastočne. Pri porovnávaní pravidiel sa nerozlišujú veľké a malé písmená. Napríklad každému, kto sa narodil vo Švédsku, bude pravidlo priradené pomocou hodnoty "sw" pre Miesto. Pravidlo vráti zhodu vtedy a len vtedy, ak sa všetky neprázdne hodnoty (čiastočne) zhodujú s narodením osoby. Ak chcete použiť len jednu hodnotu, nechajte ostatné hodnoty prázdne.

#### Osoby s údajmi <úmrtie>

Toto pravidlo zodpovedá osobám, ktorých udalosť úmrtia sa zhoduje so zadanými hodnotami pre Dátum, Miesto a Popis. Pravidlo vráti zhodu, aj keď sa udalosť úmrtia osoby zhoduje s hodnotou čiastočne. Pri porovnávaní pravidiel sa nerozlišujú veľké a malé písmená. Napríklad každému, kto zomrel vo Švédsku, bude pravidlo priradené pomocou hodnoty "sw" pre Miesto. Pravidlo vráti zhodu vtedy a len vtedy, ak sa všetky neprázdne hodnoty (čiastočne) zhodujú s udalosťou úmrtia osoby. Ak chcete použiť len jednu hodnotu, nechajte ostatné hodnoty prázdne.

#### Osoby s rodinou <udalosť>

Toto pravidlo zodpovedá osobám, ktoré majú rodinnú udalosť zodpovedajúcu zadaným hodnotám pre typ udalosti, dátum, miesto a opis. Pravidlo vráti zhodu, aj keď sa udalosť osoby zhoduje s hodnotou čiastočne. Pravidlá porovnávania nerozlišujú veľké a malé písmená. Napríklad každému, kto sa oženil vo Švédsku, bude pravidlo priradené pomocou udalosti Manželstvo a hodnoty "sw" pre Miesto. Rodinné udalosti by sa mali vyberať z rozbaľovacej ponuky. Pravidlo vráti zhodu vtedy a len vtedy, ak sa všetky neprázdne hodnoty (čiastočne) zhodujú s osobnou udalosťou. Ak chcete použiť len jednu hodnotu, ostatné hodnoty nechajte prázdne.

#### Osoby s osobnou <udalosťou>

Toto pravidlo zodpovedá ľuďom, ktorí majú osobnú udalosť zodpovedajúcu zadaným hodnotám pre typ udalosti, dátum, miesto a opis. Pravidlo vráti zhodu aj vtedy, ak sa udalosť osoby zhoduje s hodnotou čiastočne. Pri pravidlách porovnávania sa nerozlišujú veľké a malé písmená. Napríklad každému, kto absolvoval štúdium vo Švédsku, bude pravidlo priradené pomocou udalosti Absolvovanie štúdia a hodnoty "sw" pre Miesto. Osobné udalosti by sa mali vyberať z rozbaľovacej ponuky. Pravidlo vráti zhodu vtedy a len vtedy, ak sa všetky neprázdne hodnoty (čiastočne) zhodujú s osobnou udalosťou. Ak chcete použiť len jednu hodnotu, ostatné hodnoty nechajte prázdne.

#### Svedkovia

Toto pravidlo zodpovedá osobám, ktoré sú prítomné ako svedkovia v udalosti. Ak je zadaný typ osobnej alebo rodinnej udalosti, budú sa vyhľadávať len udalosti tohto typu.

### Kategória rodiny

Táto kategória obsahuje nasledujúce pravidlá, ktoré priraďujú rodiny na základe ich zaznamenaných udalostí:

#### Rodiny s <udalosťou>

Toto pravidlo vyhľadáva rodiny, ktoré majú udalosť zodpovedajúcu zadaným hodnotám pre typ udalosti, dátum, miesto a opis. Pravidlo vráti zhodu aj vtedy, ak sa udalosť osoby zhoduje s hodnotou čiastočne. Pri pravidlách porovnávania sa nerozlišujú veľké a malé písmená. Napríklad každému, kto sa oženil vo Švédsku, bude pravidlo priradené pomocou udalosti Manželstvo a hodnoty "sw" pre Miesto. Rodinné udalosti by sa mali vyberať z rozbaľovacej ponuky. Pravidlo vráti zhodu vtedy a len vtedy, ak sa všetky neprázdne hodnoty (čiastočne) zhodujú s osobnou udalosťou. Ak chcete použiť len jednu hodnotu, ostatné hodnoty nechajte prázdne.

## Filtre rodín

Táto kategória zahŕňa nasledujúce pravidlá, ktoré priraďujú osoby na základe ich rodinných vzťahov:

### Adoptovaní ľudia

Toto pravidlo zodpovedá adoptovaným ľuďom.

### Zodpovedajú deti <filter>

Toto pravidlo zodpovedá ľuďom, ktorých jeden z rodičov zodpovedá zadanému filtru. Zadaný názov filtra by sa mal vybrať z ponuky.

### Zodpovedajú rodičia <filter>

Toto pravidlo zodpovedá ľuďom, ktorých dieťaťu zodpovedá zadaný filter. Zadaný názov filtra by mal byť vybraný z ponuky.

### Ľuďom chýbajú rodičia

Zodpovedá osobám, ktoré sú deťmi v rodine s menej ako dvoma rodičmi alebo nie sú deťmi v žiadnej rodine.

### Osoby s deťmi

Toto pravidlo zodpovedá ľuďom s deťmi.

### Ľudia s viacerými záznamami o manželstve

Toto pravidlo zodpovedá ľuďom s viac ako jedným manželským partnerom.

### Osoby bez záznamov o manželstve

Toto pravidlo zodpovedá ľuďom bez manželov.

### Osoby so záznamom <vzťahy>

Toto pravidlo zodpovedá ľuďom s konkrétnym vzťahom. Vzťah musí zodpovedať typu vybranému z ponuky. Voliteľne možno zadať počet vzťahov a počet detí. Pravidlo vráti zhodu vtedy a len vtedy, ak všetky neprázdne hodnoty (čiastočne) zodpovedajú vzťahu osoby. Ak chcete použiť len jednu hodnotu, nechajte ostatné hodnoty prázdne.

### Zodpovedajú súrodenci <filter>

Toto pravidlo zodpovedá osobám, ktorých súrodencom zodpovedá zadaný filter. Zadaný názov filtra by mal byť vybraný z ponuky.

### Manželia <filter> vyhovujú

Toto pravidlo zodpovedá ľuďom, ktorí sú manželmi niekoho, komu zodpovedá zadaný filter. Zadaný názov filtra by mal byť vybraný z ponuky.

## Filtre otca

Táto kategória pravidiel nájde rodiny, ktorých otcovia vyhovujú tomuto pravidlu:

### Rodiny, ktoré majú otca s Id obsahujúcim <text>

Zodpovedá rodinám, ktorých otec má zadaný Gramps ID

### Rodiny s otcom, ktorý obsahuje <meno>

Zodpovedá rodinám, ktorých otec má zadané (čiastočné) meno

## Všeobecné filtre

Tieto pravidlá filtrovania závisia od pohľadu

- [kategória Ľudia-, a vzťahy](#Ľudia-.2C_a_vzťahy_kategória_3)
- [kategória Rodiny](#Rodiny_kategória_3)
- [kategória Udalosti](#Udalosti_kategória_2)
- [kategória Miesta](#Miesto_kategória_2)
- [Kategória zdrojov](#Sources_Category)
- [Kategória citácie](#Citácie_kategória)
- [kategória Repositories](#Repositories_Category)
- [Kategória médií](#Media_Category_2)
- [Kategória poznámok](#Notes_Category)

### Ľudia-, a vzťahy Kategória

Táto kategória obsahuje nasledujúce všeobecné pravidlá:

#### Označení ľudia

Zodpovedá ľuďom v zozname záložiek.

<span id="Predvolená osoba">

#### Domovská osoba

</span> Zodpovedá [Domovská osoba](wiki:Gramps_Glossary#home_person).

#### Odpojené osoby

Zodpovedá osobám, ktoré nemajú žiadny príbuzenský vzťah k žiadnej inej osobe v databáze.

#### Každý

Zodpovedá všetkým osobám v databáze rodinného stromu.

#### Ženy

Zodpovedá všetkým ženám.

#### Muži

Zodpovedá všetkým mužom.

#### Osoby, ktoré majú <počet> poznámok

Zodpovedá ľuďom, ktorí majú určitý počet poznámok: Hodnoty: Počet prípadov -- Počet musí byť väčší/menší/rovnaký ako

#### Ľudia, ktorí majú poznámky obsahujúce <text>

Zodpovedá ľuďom, ktorých poznámky obsahujú text zodpovedajúci regulárnemu výrazu

#### Ľudia označení ako súkromní

Zodpovedá osobám, ktoré sú označené ako súkromné.

#### Ľudia, ktorí zodpovedajú <filtru>

Zodpovedá ľuďom, ktorým zodpovedá zadaný názov filtra. Hodnoty: Názov filtra. Zadaný názov filtra by mal byť vybraný z ponuky.

#### Ľudia neoznačení ako súkromní

Zodpovedá osobám, ktoré nie sú označené ako súkromné

#### Ľudia pravdepodobne žijúci

Zodpovedá ľuďom bez označenia smrti, ktorí nie sú príliš starí. Hodnoty: V deň

- [Filter pravdepodobne žijúcich](wiki:Gramps_6.0_Wiki_Manual_-_Probably_Alive#Probably_Alive_Filter)

#### Ľudia s <počet> udalostí LDS

Zodpovedá ľuďom s určitým počtom udalostí LDS. Hodnoty: Počet udalostí -- Číslo musí byť väčšie/menšie/rovné ako

#### Ľudia s <počet> adries

Zodpovedá ľuďom s určitým počtom osobných adries. Hodnoty: Počet prípadov -- Číslo musí byť väčšie/menšie/rovné ako

#### Ľudia s <počet> asociácií

Zodpovedá ľuďom s určitým počtom asociácií. Hodnoty: Počet prípadov -- Číslo musí byť väčšie ako/menšie alebo rovné

#### Ľudia s <počet> médií

Zodpovedá ľuďom s určitým počtom položiek v galérii. Hodnoty: Počet inštancií -- Číslo musí byť väčšie ako/menšie alebo rovné

#### Ľudia s id obsahujúcim <text>

Zodpovedá ľuďom, ktorých ID Gramps zodpovedá regulárnemu výrazu

#### Ľudia s prezývkou

Zodpovedá ľuďom s prezývkou

#### Ľudia s alternatívnym menom

Zodpovedá ľuďom s alternatívnym menom

#### Ľudia s neúplnými menami

Zodpovedá ľuďom s chýbajúcim menom alebo priezviskom.

#### Ľudia so záznamami obsahujúcimi <substring>

Zodpovedá ľuďom, ktorých záznamy obsahujú text zodpovedajúci podreťazcu. Hodnoty: Podreťazec -- Rozlišuje veľké a malé písmená alebo nie -- Zodpovedá regulárnemu výrazu alebo nie

#### Ľudia so záznamom <typ mena>

Zodpovedá ľuďom s typom mena

#### Ľudia s typom <Pôvod priezviska>

Zodpovedá ľuďom s pôvodom priezviska

#### Ľudia s typom <meno>

Zodpovedá ľuďom so zadaným (čiastočným) menom. Hodnoty: meno -- priezvisko -- prípona -- titul -- predpona -- patronymum -- volanie

#### Ľudia s <značkou>

Zodpovedá ľuďom s príznakom určitej hodnoty. Hodnoty: Názov značky.

#### Ľudia s <príznakom>

Zodpovedá ľuďom s atribútom rodina určitej hodnoty. Na vyhľadávanie [všetky hodnoty](wiki:Gramps_6.0_Wiki_Manual_-_Filters#regex_all) alebo atribútov, ktoré boli [opustené prázdne](wiki:Gramps_6.0_Wiki_Manual_-_Filters#regex_null), použite porovnávanie vzorov RegEx. Hodnoty: Rodinný atribút: Identifikačné číslo -- Vek ...

#### Osoby s osobným <atribútom>

Zodpovedá osobám s osobným atribútom konkrétnej hodnoty. Na vyhľadávanie [všetkých hodnôt](wiki:Gramps_6.0_Wiki_Manual_-_Filters#regex_all) alebo atribútov, ktoré boli [opustené prázdne](wiki:Gramps_6.0_Wiki_Manual_-_Filters#regex_null), použite porovnávanie vzorov RegEx. Hodnoty: Rodinný atribút: Identifikačné číslo -- Vek ...

#### Osoby s neznámym pohlavím

Zodpovedá všetkým osobám s neznámym pohlavím.

#### Osoby bez známeho dátumu narodenia

Zodpovedá osobám bez známeho dátumu narodenia.

#### Ľudia bez známeho dátumu úmrtia

Zodpovedá ľuďom bez známeho dátumu úmrtia.

#### Ľudia s <id>

Zodpovedá ľuďom s identifikačným číslom Gramps. Pravidlo vráti zhodu len vtedy, ak sa ID zhoduje presne. ID môžete zadať do poľa na zadávanie textu alebo vybrať objekt zo zoznamu kliknutím na tlačidlo . V druhom prípade sa ID zobrazí v textovom poli po vykonaní výberu.

#### Ľudia sa zmenili po <dátum čas>

Zodpovedá záznamom o osobách zmenených počas určitého časového obdobia. Slúži na identifikáciu záznamov, ktoré boli importované alebo zmenené počas konkrétnych pracovných relácií.

Filtrovanie na základe zadaného dátumu a časovej pečiatky, ktorá je po konkrétnom časovom údaji vo formáte `yyyy-mm-dd hh:mm:ss`. Toto pravidlo filtrovania vyhľadá záznamy upravené v rámci rozsahu dátumov, ak je zadaný druhý dátum-čas.

Hodnoty:

`   Zmenené po: `  
`   ale pred: `

Hodnoty musia byť po 1. januári 1970 v UTC. Budúce dátumy do `3001-01-01 01:59:59` sú platné.

Pravidlá filtrovania sú k dispozícii v časti pre vlastné pravidlá v zobrazeniach Ľudia, Vzťahy, Grafy a Zemepis.

Rovnaké pravidlá existujú pre záznamy príslušného typu kategórie v zobrazeniach kategórií Ľudia, Rodiny, Udalosti, Miesta, Zdroje, Citácie, Repozitáre, Médiá a Poznámky.

#### Osoby s udalosťami zodpovedajúcimi filtru <udalosť>

Zodpovedá osobám, ktoré majú udalosti zodpovedajúce určitému filtru udalostí. Hodnoty: Názov filtra udalostí.

#### Súlad osôb s udalosťou <názov>

### Kategória rodín

Táto kategória zahŕňa nasledujúce všeobecné pravidlá:

#### Rodiny predkov <rodina>

Rodina s rodokmeňom

#### Rodiny označené záložkou

Zodpovedá rodinám v zozname záložiek.

#### Pokračujúce rodiny <rodiny>

#### Každá rodina

Zodpovedá každej rodine v databáze.

#### Rodiny zmenené po <dátum čas>

Zodpovedá záznamom o rodinách zmenených po zadanom dátume-čase (rrrr-mm-dd hh:mm:ss) alebo v rozsahu, ak je uvedený druhý dátum-čas: Hodnoty: Zmenené po: -- ale pred:.

#### Rodiny, ktoré majú <počet> poznámok

Zodpovedá rodinám, ktoré majú určitý počet poznámok: Hodnoty: Počet prípadov -- Počet musí byť väčší/menší/rovnaký ako

#### Rodiny, ktoré majú poznámky obsahujúce <text>

Zodpovedá rodinám, ktorých poznámky obsahujú text zodpovedajúci regulárnemu výrazu

#### Rodiny označené ako súkromné

Zodpovedá rodinám, ktoré sú označené ako súkromné.

#### Rodiny zodpovedajúce <filter>

Zodpovedá rodinám, ktorým zodpovedá zadaný názov filtra. Hodnoty: Názov filtra. Zadaný názov filtra by mal byť vybraný z ponuky.

#### Rodiny s <počet> udalostí SPD

Zodpovedá rodinám s určitým počtom udalostí SPD. Hodnoty: Počet prípadov -- číslo musí byť väčšie/menšie/rovné ako

#### Rodiny s <počet> médií

Zodpovedá rodinám s určitým počtom položiek v galérii. Hodnoty: Počet inštancií -- Číslo musí byť väčšie/menšie/rovné ako

#### Rodiny s id obsahujúcim <text>

Zodpovedá rodinám, ktorých identifikátor Gramps zodpovedá regulárnemu výrazu

#### Rodiny s počtom odkazov <count>

Zodpovedá rodinám s určitým počtom odkazov. Hodnoty: Počet odkazov -- Počet musí byť väčší/menší/rovnaký ako

#### Rodiny s <značkou>

Zodpovedá rodinám so značkou určitej hodnoty. Hodnoty: Názov značky.

#### Rodiny s rodinou <príznak>

Zodpovedá rodinám s atribútom family určitej hodnoty. Hodnoty: Atribút rodiny: Identifikačné číslo -- Vek ...

#### Rodiny s typom vzťahu

Zodpovedá rodinám s typom vzťahu určitej hodnoty.

#### Rodiny s <id>

Zodpovedá rodinám s identifikátorom Gramps. Pravidlo vráti zhodu len vtedy, ak sa presne zhoduje s ID. ID môžete zadať do poľa na zadávanie textu alebo vybrať objekt zo zoznamu kliknutím na tlačidlo . V druhom prípade sa ID zobrazí v textovom poli po vykonaní výberu.

### Kategória udalostí

Táto kategória obsahuje nasledujúce všeobecné pravidlá:

#### Udalosť s <id>

Zodpovedá udalostiam s identifikátorom Gramps. Pravidlo vráti zhodu len vtedy, ak sa ID zhoduje presne. ID môžete zadať do poľa na zadávanie textu alebo vybrať objekt zo zoznamu kliknutím na tlačidlo . V druhom prípade sa ID zobrazí v textovom poli po vykonaní výberu.

#### Udalosti zmenené po <dátum čas>

Zodpovedá záznamom o udalostiach zmenených po zadanom dátume-čase (rrrr-mm-dd hh:mm:ss) alebo v rozsahu, ak je zadaný druhý dátum-čas: Hodnoty: Zmenené po: -- ale pred:.

#### Udalosti, ktoré majú <počet> poznámok

Zodpovedá udalostiam, ktoré majú určitý počet poznámok: Hodnoty: Počet prípadov -- Počet musí byť väčší/menší/rovnaký ako

#### Udalosti, ktoré majú poznámky obsahujúce <text>

Zodpovedá udalostiam, ktorých poznámky obsahujú text zodpovedajúci regulárnemu výrazu

#### Udalosti označené ako súkromné

Zodpovedá udalostiam, ktoré sú označené ako súkromné.

#### Udalosti zodpovedajúce <filter>

Zodpovedá udalostiam, ktorým zodpovedá zadaný názov filtra. Hodnoty: Názov filtra. Zadaný názov filtra by sa mal vybrať z ponuky.

#### Udalosti, ktoré sa vyskytli v určitý deň v týždni

Zodpovedá udalostiam, ktoré sa vyskytli v určitý deň v týždni.

#### Udalosti osôb zodpovedajúcich filtru <osoba>

Zodpovedá udalostiam osôb, ktorým zodpovedá zadaný názov filtra osôb

#### Udalosti miest zodpovedajúce filtru <miesto>

Zodpovedá udalostiam, ktoré sa vyskytli na miestach zodpovedajúcich zadanému názvu filtra miesta

#### Udalosti s <počet> médií

Zodpovedá udalostiam s určitým počtom položiek v galérii. Hodnoty: Počet prípadov -- Číslo musí byť väčšie/menšie/rovné ako

#### Udalosti s <údajmi>

Zodpovedá udalostiam s údajmi určitej hodnoty

#### Udalosti s Id obsahujúcim <text>

Zodpovedá udalostiam, ktorých ID Gramps zodpovedá regulárnemu výrazu

#### Udalosti s počtom odkazov <count>

Zodpovedá udalostiam s určitým počtom odkazov. Hodnoty: Počet odkazov -- Počet musí byť väčší/menší/rovnaký ako

#### Udalosti s <značkou>

Zodpovedá udalostiam so značkou určitej hodnoty. Hodnoty: Názov značky.

#### Udalosti s atribútom <atribút>

Zodpovedá udalostiam s atribútom určitej hodnoty. Hodnoty: Atribút rodiny: Identifikačné číslo -- Vek ...

#### Udalosti s konkrétnym typom

Zodpovedá udalostiam s konkrétnym typom

#### Každá udalosť

Zodpovedá každej udalosti v databáze.

### Kategória miest

Táto kategória obsahuje nasledujúce všeobecné pravidlá:

#### Každé miesto

Zodpovedá každému miestu v databáze.

#### Miesto s <Id>

Zodpovedá miestam s identifikátorom Gramps. Pravidlo vráti zhodu len vtedy, ak sa ID zhoduje presne. ID môžete zadať do textového poľa alebo vybrať objekt zo zoznamu kliknutím na tlačidlo . V druhom prípade sa ID zobrazí v textovom poli po vykonaní výberu.

#### Miesto zmenené po <dátum čas>

Zodpovedá záznamom o miestach zmenených po zadanom dátume-čase (rrrr-mm-dd hh:mm:ss) alebo v rozsahu, ak je zadaný druhý dátum-čas: Hodnoty: Zmenené po: -- ale pred:.

#### Miesto uzavreté iným miestom

#### Miest, ktoré majú <počet> poznámok

Zodpovedá miestam, ktoré majú určitý počet poznámok: Hodnoty: Počet výskytov -- Počet musí byť väčší/menší/rovnaký ako

#### Miest, ktoré majú poznámky obsahujúce <text>

Označuje miesta, ktorých poznámky obsahujú text zodpovedajúci regulárnemu výrazu

#### Miesto označené ako private

Zodpovedá miestam, ktoré sú označené ako súkromné.

#### Miest, ktoré zodpovedajú názvu

Zodpovedá miestam s konkrétnym názvom

#### Miesto zodpovedajúce parametrom

Zodpovedá miestam s konkrétnymi parametrami

#### Miesto zodpovedajúce <filter>

Zodpovedá miestam, ktorým zodpovedá zadaný názov filtra. Hodnoty: Názov filtra. Z ponuky by sa mal vybrať zadaný názov filtra.

#### Miestami udalostí zodpovedajúcimi <filtru udalostí>

Zodpovedá miestam, kde sa stali udalosti zodpovedajúce zadanému názvu filtra udalostí.

#### Miest s <počet> médií

Zodpovedá miestam s určitým počtom položiek v galérii. Hodnoty: Počet prípadov -- Číslo musí byť väčšie/menšie/rovné ako

#### Miest s Id obsahujúcim <text>

Zodpovedá miestam, ktorých ID Gramps zodpovedá regulárnemu výrazu

#### Miest, ktorých počet odkazov obsahuje <počet>

Zodpovedá miestam s určitým počtom odkazov. Hodnoty: Počet odkazov -- Počet musí byť väčší/menší/rovnaký ako

#### Miest s <značkou>

Zodpovedá miestam so značkou určitej hodnoty. Hodnoty: Názov značky.

### Kategória zdrojov

Táto kategória zahŕňa nasledujúce všeobecné pravidlá:

#### Každý zdroj

Zodpovedá každému zdroju v databáze.

#### Zdroj s <Id>

Zodpovedá zdrojom s identifikátorom Gramps. Pravidlo vráti zhodu len vtedy, ak sa ID zhoduje presne. ID môžete zadať do poľa na zadávanie textu alebo vybrať objekt zo zoznamu kliknutím na tlačidlo . V druhom prípade sa ID zobrazí v textovom poli po vykonaní výberu.

#### Zdroje zmenené po <dátum čas>

Zodpovedá záznamom o zdrojoch zmenených po zadanom dátume-čase (rrrr-mm-dd hh:mm:ss) alebo v rozsahu, ak je zadaný druhý dátum-čas: Hodnoty: Zmenené po: -- ale pred:.

#### Sources having <count> notes

Zodpovedá zdrojom, ktoré majú určitý počet poznámok: Hodnoty: Počet výskytov -- Počet musí byť väčší/menší/rovnaký ako

#### Zdroje, ktoré majú poznámky obsahujúce <text>

Zodpovedá zdrojom, ktorých poznámky obsahujú text zodpovedajúci regulárnemu výrazu

#### Zdroje označené ako súkromné

Zodpovedá zdrojom, ktoré sú označené ako súkromné.

#### Zdroje zodpovedajúce <filter>

Zodpovedá zdrojom, ktorým zodpovedá zadaný názov filtra. Hodnoty: Názov filtra. Zadaný názov filtra by mal byť vybraný z ponuky.

#### Zdroje s referenciami na úložisko <počet>

Zodpovedá zdrojom s určitým počtom odkazov na úložisko.

#### Sources with <count> media

Zodpovedá zdrojom s určitým počtom položiek v galérii. Hodnoty: Počet inštancií -- Číslo musí byť väčšie/menšie/rovné ako

#### Zdroje s Id obsahujúcim <text>

Zodpovedá zdrojom, ktorých Gramps ID zodpovedá regulárnemu výrazu

#### Zdroje s počtom odkazov <count>

Zodpovedá zdrojom s určitým počtom odkazov. Hodnoty: Počet odkazov -- Číslo musí byť väčšie/menšie/rovné ako

#### Zdroje s odkazom na úložisko obsahujúcim <text> v položke "Call Number"

Zodpovedá zdrojom s odkazom na úložisko obsahujúcim podreťazec v "Call Number

#### Zdroje s odkazom na úložisko zodpovedajúcim <filtru úložiska>

Zodpovedá zdrojom s odkazom na úložisko, ktoré zodpovedajú určitému filtru úložiska

#### Zdroje s <značkou>

Zodpovedá zdrojom s tagom určitej hodnoty. Hodnoty: Názov značky.

#### Zdroje s názvom obsahujúcim <text>

Zodpovedá zdrojom, ktorých názov obsahuje určitý podreťazec

### Kategória citácií

Táto kategória zahŕňa nasledujúce všeobecné pravidlá:

#### Citácie obsahujúce <Id>

Zodpovedá citáciám s ID Gramps. Pravidlo vráti zhodu len vtedy, ak sa ID zhoduje presne. ID môžete zadať do textového poľa alebo vybrať objekt zo zoznamu kliknutím na tlačidlo . V druhom prípade sa ID zobrazí v textovom poli po vykonaní výberu.

#### Citácie zmenené po <dátum čas>

Zodpovedá záznamom citácií zmenených po zadanom dátume-čase (rrrr-mm-dd hh:mm:ss) alebo v rozsahu, ak je zadaný druhý dátum-čas: Hodnoty: Zmenené po: -- ale pred:.

#### Citácie, ktoré majú <počet> poznámok

Zodpovedá citáciám, ktoré majú určitý počet poznámok: Hodnoty: Počet výskytov -- Počet musí byť väčší/menší/rovnaký ako

#### Citácie obsahujúce poznámky <text>

Zodpovedá citáciám, ktorých poznámky obsahujú text zodpovedajúci regulárnemu výrazu

#### Citácie označené ako súkromné

Zodpovedá citáciám, ktoré sú označené ako súkromné.

#### Citácie zodpovedajúce parametrom

Zodpovedá citáciám s konkrétnymi parametrami

#### Citácie zodpovedajúce <filter>

Zodpovedá citáciám, ktorým zodpovedá zadaný názov filtra. Hodnoty: Názov filtra. Zadaný názov filtra by mal byť vybraný z ponuky.

#### Citácie s <počet> médií

Zodpovedá citáciám s určitým počtom položiek v galérii. Hodnoty: Počet exemplárov -- Číslo musí byť väčšie/menšie/rovné ako

#### Citácie s Id obsahujúcim <text>

Zodpovedá citáciám, ktorých ID Gramps sa zhoduje s regulárnym výrazom

#### Citácie so zväzkom/stránkou obsahujúcou <text>

Zodpovedá citáciám, ktorých Volume/Page obsahuje určitý podreťazec

#### Citácie s počtom odkazov <count>

Zodpovedá citáciám s určitým počtom odkazov. Hodnoty: Počet odkazov -- počet musí byť väčší/menší/rovnaký ako

#### Citácie so zdrojom s odkazom na úložisko, ktorý zodpovedá filtru <úložisko>

Zodpovedá citáciám so zdrojom s odkazom na repozitár, ktoré zodpovedajú určitému filtru repozitára

#### Citácie so zdrojom, ktorý zodpovedá <filtru zdroja>

Zodpovedá citáciám so zdrojmi, ktoré zodpovedajú určitému názvu filtra zdrojov

#### Citácie s <značkou>

Zodpovedá citáciám s tagom určitej hodnoty. Hodnoty: Názov značky.

#### Každá citácia

Zodpovedá každej citácii v databáze.

### Kategória repozitárov

Táto kategória zahŕňa nasledujúce všeobecné pravidlá:

#### Každý repozitár

Zodpovedá každému úložisku v databáze.

#### Úložiská zmenené po <dátum čas>

Zodpovedá záznamom o úložisku zmeneným po zadanom dátume-čase (rrrr-mm-dd hh:mm:ss) alebo v rozsahu, ak je uvedený druhý dátum-čas: Hodnoty: Zmenené po: -- ale pred:.

#### Úložiská, ktoré majú poznámky obsahujúce <text>

Zodpovedá úložiskám, ktorých poznámky obsahujú text zodpovedajúci regulárnemu výrazu

#### Úložiská označené ako súkromné

Zodpovedá úložiskám, ktoré sú označené ako súkromné.

#### Úložiská zodpovedajúce <filter>

Zodpovedá úložiskám, ktoré sa zhodujú so zadaným názvom filtra. Hodnoty: Názov filtra. Zadaný názov filtra by sa mal vybrať z ponuky.

#### Úložiská s Id obsahujúcim <text>

Zodpovedá úložiskám, ktorých ID Gramps zodpovedá regulárnemu výrazu

#### Repozitáre s počtom odkazov obsahujúcim <počet>

Zodpovedá repozitárom s určitým počtom odkazov. Hodnoty: Počet odkazov -- Počet musí byť väčší/menší/rovnaký ako

#### Úložiská s názvom obsahujúcim <text>

Zodpovedá repozitárom, ktorých názov obsahuje podreťazec

#### Úložiská s <značkou>

Zodpovedá repozitárom s tagom určitej hodnoty. Hodnoty: Názov tagu.

#### Repository s <Id>

Zodpovedá úložiskám s identifikátorom Gramps. Pravidlo vráti zhodu len vtedy, ak sa ID zhoduje presne. ID môžete zadať do poľa na zadávanie textu alebo vybrať objekt zo zoznamu kliknutím na tlačidlo . V druhom prípade sa ID zobrazí v textovom poli po vykonaní výberu.

### Kategória médií

Táto kategória obsahuje nasledujúce všeobecné pravidlá:

#### Každý mediálny objekt

Zodpovedá každému mediálnemu objektu v databáze.

#### Mediálny objekt s <Id>

Zodpovedá mediálnym objektom s ID Gramps. Pravidlo vráti zhodu len vtedy, ak sa ID zhoduje presne. ID môžete zadať do poľa na zadávanie textu alebo vybrať objekt zo zoznamu kliknutím na tlačidlo . V druhom prípade sa ID zobrazí v textovom poli po vykonaní výberu.

#### Mediálne objekty zmenené po <dátum čas>

Zodpovedá záznamom mediálnych objektov zmenených po zadanom dátume-čase (rrrr-mm-dd hh:mm:ss) alebo v rozsahu, ak je zadaný druhý dátum-čas: Hodnoty: Zmenené po: -- ale pred:.

#### Mediálne objekty, ktoré majú poznámky obsahujúce <text>

Zodpovedá mediálnym objektom, ktorých poznámky obsahujú text zodpovedajúci regulárnemu výrazu

#### Mediálne objekty označené ako súkromné

Zodpovedá mediálnym objektom, ktoré sú označené ako súkromné.

#### Mediálne objekty zodpovedajúce <filter>

Zodpovedá mediálnym objektom, ktorým zodpovedá zadaný názov filtra. Hodnoty: Názov filtra. Zadaný názov filtra by mal byť vybraný z ponuky.

#### Mediálne objekty s Id obsahujúcim <text>

Zodpovedá mediálnym objektom, ktorých ID Gramps zodpovedá regulárnemu výrazu

#### Mediálne objekty, ktorých počet odkazov obsahuje <počet>

Zodpovedá mediálnym objektom s určitým počtom odkazov. Hodnoty: Počet odkazov -- Počet musí byť väčší/menší/rovnaký ako

#### Mediálne objekty s <značkou>

Zodpovedá mediálnym objektom s tagom určitej hodnoty. Hodnoty: Názov značky.

#### Mediálne objekty s atribútom <atribút>

Zodpovedá mediálnym objektom s atribútom určitej hodnoty

### Kategória Poznámky

Táto kategória zahŕňa nasledujúce všeobecné pravidlá:

#### Každá poznámka

Zodpovedá každej poznámke v databáze.

#### Poznámky s <Id>

Zodpovedá poznámkam s identifikátorom Gramps. Pravidlo vráti zhodu len vtedy, ak sa ID zhoduje presne. ID môžete zadať do poľa na zadávanie textu alebo vybrať objekt zo zoznamu kliknutím na tlačidlo . V druhom prípade sa ID zobrazí v textovom poli po vykonaní výberu.

#### Poznámky zmenené po <dátum čas>

Zodpovedá záznamom poznámok zmeneným po zadanom dátume-čase (rrrr-mm-dd hh:mm:ss) alebo v rozsahu, ak je zadaný druhý dátum-čas: Hodnoty: Zmenené po: -- ale pred:.

#### Poznámky obsahujúce <text>

Zodpovedá poznámkam obsahujúcim text zodpovedajúci regulárnemu výrazu

#### Poznámky označenie ako súkromné

Zodpovedá poznámkam, ktoré sú označené ako súkromné.

#### Poznámky zodpovedajú parametrom

Zodpovedá poznámkam s konkrétnymi parametrami

#### Notes matching the <filter>

Zodpovedá poznámkam, ktorým zodpovedá zadaný názov filtra. Hodnoty: Názov filtra. Zadaný názov filtra by mal byť vybraný z ponuky.

#### Notes with Id containing <text>

Zodpovedá poznámkam, ktorých ID Gramps zodpovedá regulárnemu výrazu

#### Notes with the reference count of <count>

(Poznámky s počtom odkazov obsahujúcim <count>====) Zodpovedá poznámkam s určitým počtom odkazov. Hodnoty: Počet odkazov -- Počet musí byť väčší/menší/rovnaký ako

#### Notes with <tag>

Zodpovedá poznámkam s tagom určitej hodnoty. Hodnoty: Názov značky.

#### Notes with a particular type

Zodpovedá poznámkam s konkrétnym typom

## Filtre matky

Táto kategória pravidiel nájde rodiny, ktorých matky vyhovujú tomuto pravidlu:

### Rodiny, ktoré majú matku s Id obsahujúcim <text>

Zodpovedá rodinám, ktorých matka má zadané ID Gramps

### Rodiny s matkou, ktorá obsahuje <meno>

Zodpovedá rodinám, ktorých matka má zadané (čiastočné) meno

## Filtre polohy

Táto kategória pravidiel vyhľadáva miesta podľa blízkosti súradníc globálneho polohového systému (GPS):

### Miesta v blízkosti danej polohy

Zodpovedá miestam s polohou v obdĺžniku s danou výškou a šírkou (v stupňoch) a so stredným bodom danej zemepisnej šírky a dĺžky.

### Miesta bez zadanej zemepisnej šírky alebo dĺžky

Zodpovedá miestam s prázdnou zemepisnou šírkou alebo dĺžkou

### Miesta v rámci oblasti

## Filtre zdrojov

Táto kategória pravidiel nájde citácie, ktoré zodpovedajú pravidlu:

### Citácie so zdrojom <Id>

Zodpovedá citácii so zdrojom so zadaným ID Gramps

### Citácie, ktoré majú poznámky k zdroju obsahujúce <text>

Zodpovedá citáciám, ktorých zdrojové poznámky obsahujú podreťazec alebo zodpovedajú regulárnemu výrazu

### Citácie s identifikátorom zdroja obsahujúcim <text>

Zodpovedá citáciám, ktorých zdroj má Gramps ID, ktoré zodpovedá regulárnemu výrazu

### Zdroje zodpovedajúce parametrom

Zodpovedá citáciám, ktorých zdroj má určitú hodnotu

## Filtre vzťahov

Táto kategória zahŕňa nasledujúce pravidlá, ktoré spájajú osoby na základe ich vzájomného vzťahu:

### Osoby súvisiace s <Osoba>

Zodpovedá ľuďom, ktorí sú príbuzní zadanej osobe

### Cesta vzťahu medzi <osoba> a ľuďmi zodpovedajúcimi <filter>

Prehľadáva databázu počnúc zadanou osobou a vráti všetkých medzi touto osobou a množinou cieľových osôb zadaných pomocou filtra. Tým sa vytvorí súbor ciest vzťahov (vrátane manželských) medzi zadanou osobou a cieľovými ľuďmi. Každá cesta nemusí byť nevyhnutne najkratšia.

### Cesta vzťahu medzi <osobami>

Toto pravidlo porovnáva všetkých predkov oboch osôb späť k ich spoločným predkom (ak existujú). Tým sa vytvorí "cesta vzťahu" medzi týmito dvoma osobami prostredníctvom ich spoločných predkov. ID každej osoby môžete zadať do príslušných polí na zadávanie textu alebo vybrať osoby zo zoznamu kliknutím na ich tlačidlá . V druhom prípade sa ID zobrazí v textovom poli po vykonaní výberu.

### Cesta vzťahu medzi osobami so záložkami

Priradí predkov záložkovaných osôb späť k spoločným predkom, čím vytvorí cestu(y) vzťahu medzi záložkovanými osobami.

## Označovanie

Koncept označovania pre väčšinu ľudí, ktorí používajú *gmail* alebo *thunderbird*, bude funkcia [Tag](wiki:Gramps_Glossary#tag) celkom známa. Namiesto klasifikácie e-mailov do priečinkov ako v *Outlooku* (Windows) alebo *Evolution* (Linux) sa e-maily klasifikujú priradením značiek. Takže namiesto nesúvislej klasifikácie N:1 (e-mail môže byť v jednom a len v jednom priečinku a priečinok môže obsahovať mnoho e-mailov), v *gmaile* alebo *thunderbirde* existuje klasifikácia N:M (kde e-mail môže mať niekoľko značiek a jedna značka môže byť použitá na niekoľko e-mailov)

Podobne, keď máte veľký strom, môžete chcieť vytvoriť podmnožiny stromu a tieto podmnožiny sa môžu prekrývať. Napríklad podmnožiny rodiny vášho otca a rodiny vašej matky, niektoré podmnožiny vašej rodiny, ktorá emigrovala do Austrálie.

![[_media/gramps-tag.png]]Ide o to, aby ste každej podmnožine priradili inú značku: napríklad *Otec*, *Matka*, *Austrália* a *Úloha*.

Rozdiely oproti predchádzajúcim **Značkám** od Gramps sú ako priečinky pre e-maily. Osoba môže mať pridelenú najviac jednu značku. Značky sú teda ako značky s viacerými hodnotami. {{-}}

Prejdite do ponuky .

![[_media/Menu-Edit-Tag-Options-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Akcie značkovania z ponuky Úpravy]]

{{-}}

Alebo kliknite na tlačidlo na paneli nástrojov ![[_media/16x16-gramps-tag.png]].

![[_media/Toolbar-TagSelectedRows-Icon-DropDownMenu-overview-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Dostupné akcie značkovania z ikony panela nástrojov &quot;Označiť vybrané riadky&quot; - prehľad rozbaľovacej ponuky - príklad]] {{-}} Pozri tiež [Tag Report](wiki:Gramps_6.0_Wiki_Manuál_-_Reporty_-_časť_6#Tag_Report). {{-}}

### Dialógové okno Nová značka

![[_media/NewTag-dialog-ShowingMultipleListSelection-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Pripojenie "Novej značky" k výberu viacerých položiek zoznamu - príklad s dialógovým oknom "Nová značka"]]

Novú značku môžete pridať buď jednej, alebo viacerým položkám zoznamu z ktoréhokoľvek pohľadu zoznamu, a to tak, že vykonáte výber a potom použijete dialógové okno "Nová značka".

{{-}}

##### Označenie výberu objektov

Vzhľadom na **statickú** povahu značiek môže byť užitočné pridať značku k výberu objektov. Napríklad by sa malo dať vybrať niekoľko osôb v [pohľade Osoba](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window/sk#Kategória_Ľudia) a pridať im novú alebo existujúcu značku. {{-}}

### Okno Usporiadajte značky

![[_media/MenuEditTag-OrganizeTags-dialog-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Usporiadajte značky - dialógové okno - príklad]]

Poradie v dialógovom okne definuje prioritu pre vyfarbenie riadkov v pohľadoch kategórií.

{{-}}

### Dialógové okno Výber značky

![[_media/TagSelection-dialog-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Výber značky v Editore osoby]]

Keď použijete tlačidlo ![[_media/16x16-gramps-tag.png]] z niektorého z dialógových okien Editora, ako napríklad , zobrazí sa dialógový zoznam, ktorý vám umožní odstrániť alebo priradiť existujúce vlastné značky. Značky sa zobrazujú v abecednom poradí. {{-}}

### Používanie značiek

Tu je niekoľko nápadov na operácie, ktoré sa dajú vykonať so značkami

#### Filtrovanie

![[_media/Sidebar-PeopleTreeView-Filter-TagDropDownList-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Bočný panel filtra Gramps - príklad zoznamu značiek]]

Najzrejmejšie použitie je filtrovanie.

- Značky aj filtre vytvárajú podmnožiny stromu. Majú však praktické rozdiely v použití.

Určenie rodiny otcov pomocou filtrov je jednoduchá vec; už existujú filtre založené na nejakej logike, ktoré to robia. Na druhej strane špecifikovať ľudí, ktorí emigrovali do USA, je ťažšie, pričom v prípade slávnych ľudí vo vašej rodine je to jednoducho nemožné, pretože neexistuje žiadne logické pravidlo. Značky sú tu oveľa praktickejšie.

Filtre však majú tú výhodu, že sú **dynamické**. Ak do databázy pridáte predka svojho otca, automaticky sa pridá do filtra.

Na druhej strane značky sú **statické**. Pri pridávaní slávnej osoby do stromu ju musíte explicitne označiť ako *FAMOUS*.

- Najbezprostrednejším objektom, ktorý vám napadne, sú jednotlivci, a to je aj najužitočnejšie. Mohli by sa však označiť aj iné objekty:
  - Miesta: Napríklad "miesta, ktoré treba navštíviť",
  - Zdroj: \*\* Zdroj, ktorý sa nachádza na mieste, kde sa dá navštíviť: Napríklad "zdroje v nemčine",
  - Poznámky: Napríklad "notes in progess" alebo "notes in german",
  - Médiá: Napríklad "obraz patriaci strýkovi Alfredovi".

Značky je možné používať so **všetkými primárnymi objektmi**. {{-}}

#### Stĺpec značiek

![[_media/PeopleListView-ExampleTagColoredRows-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Pohľad Ľudia (zoznam) - Zobrazenie stĺpca "Značka" a farebných riadkov so značkami - príklad]]

Ak chcete ľahko zobraziť značky, môžete použiť na pridanie stĺpca do zobrazenia zoznamu objektov. Obsah sa potom zobrazí ako zoznam značiek objektov oddelených čiarkami.

#### Správa o používaní značiek

V [Tag Usage Report](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_6/sk#Tag_Report) je uvedený zoznam [primárne objekty](wiki:Gramps_Glossary#primary_object). (osoba, rodina, poznámky), ktoré majú zvolenú Značku.

### Pozri tiež

- [Značky v programe Gramps](wiki:Značky_v_programe_Gramps) - úvod
- Automatické [Importovanie časových značiek Tagov](wiki:Gramps_6.0_Wiki_Manual_-_Settings/sk#General_Gramps_settings)
- filtrovaný [Nástroj na pridávanie/odstraňovanie značiek](wiki:Addon:AddRemoveTagTool) (Doplnok tretej strany pre Gramps)

{{-}}

[Category:Sk:Documentation](wiki:Category:Sk:Documentation) [Category:Filters](wiki:Category:Filters)
