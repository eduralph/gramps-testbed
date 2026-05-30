---
title: Gramps 6.0 Wiki Manual - Navigation/sk
categories:
- Sk:Documentation
- Stub
managed: false
source: wiki-scrape
wiki_revid: 122698
wiki_fetched_at: '2026-05-30T20:09:06Z'
lang: sk
---

{{#vardefine:chapter\|10}} {{#vardefine:figure\|0}} Pokiaľ je otvorená akákoľvek databáza [Rodinný strom](wiki:Gramps_Glossary#family_tree), Gramps sa zameriava na jednu osobu, ktorá sa zvyčajne označuje ako [Aktívna osoba](wiki:Gramps_Glossary#active_person). To vám umožňuje prezerať alebo upravovať údaje týkajúce sa tejto osoby, jej najbližšej rodiny atď. [Prechod v rodinnom strome](wiki:Gramps_6.0_Wiki_Manual_-_Navigation/sk#Nastavenie_Aktívnej_osoby) databázy (t. j. prechod od osoby k osobe) nie je v skutočnosti nič iné ako zmena Aktívnej osoby.

V tejto časti je opísaných mnoho alternatívnych spôsobov navigácie v databáze pomocou zložitých aj pohodlných rozhraní, ktoré poskytuje program Gramps. Všetky tieto spôsoby v zásade dosahujú rovnaký výsledok, ale niektoré spôsoby navigácie budú pohodlnejšie ako iné... v závislosti od toho, čo v programe Gramps práve robíte.

## Používanie kategórie Ľudia

Najintuitívnejší spôsob, ako vybrať aktívnu osobu, je použiť [kategóriu Ľudia](wiki:Gramps_6.0_Wiki_Manual_-_Categories/sk#Kategória_Ľudia). Keď sa nachádzate v kategórii Ľudia, stačí vybrať meno požadovanej osoby zo zoznamu kliknutím na danú položku zoznamu. Vybraná osoba sa stane aktívnou. Stavový riadok sa aktualizuje tak, aby odrážal zmenu aktívnej osoby.

Pozrite si tiež

- [Úprava informácií o ľuďoch](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1/sk#Úprava_informácií_o_ľuďoch)

## Používanie kategórie Vzťahy

Keď sa nachádzate v [kategórii Vzťahy](wiki:Gramps_6.0_Wiki_Manual_-_Categories/sk#Kategória_Vzťahy), môžete jednoducho prechádzať medzi členmi zobrazenej rodiny nasledovne:

Kliknite na podčiarknuté meno osoby, ku ktorej chcete prejsť, a táto osoba sa stane novou aktívnou osobou kategórie Vzťahy.

Meno aktuálne aktívnej osoby nie je podčiarknuté.

Okrem toho program Gramps poskytuje rozsiahly súbor možností navigácie pomocou klávesnice. Podrobný odkaz na väzby klávesov nájdete v [Prílohe B: Odkaz na väzby klávesov](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings/sk).

## Používanie kategórie Rodiny

Keď sa nachádzate v [kategórii Rodiny](wiki:Gramps_6.0_Wiki_Manual_-_Categories/sk#Kategória_Rodiny), môžete ľahko prechádzať medzi zobrazenými rodinami.

## Používanie kategórie Grafy ![[_media/22x22-gramps-pedigree.png]]

![[_media/TimelinePedigreeView-Addon-Existing-Person-ContextMenu-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Zobrazenie časovej osi rodokmeňa - doplnok tretej strany pre kategóriu grafov - príklad kontextovej ponuky]] Gramps sa vo veľkej miere spolieha na formulárové rozloženie položiek prepojeného zoznamu. Tie naznačujú vzťahy medzi záznamami vo vašom rodinnom strome. Kategória **Grafy** poskytuje alternatívny, vizuálnejší spôsob reprezentácie týchto vzťahov. Pozície, tvary a farby kontajnerov spolu s ich spojovacími čiarami & šípkami možno zobraziť ďalšiu hĺbku vzájomných vzťahov s rôznymi faktormi. Kontajnery môžu byť jednoduché farebne vyplnené kolónky, oblúky, stuhy alebo mnohé iné tvary.

Ale [kategória Grafy](wiki:Gramps_6.0_Wiki_Manual_-_Categories/sk#Kategória_Grafy) poskytuje aj alternatívny spôsob navigácie v rodinnom atrome. Výhodou tohto spôsobu je, že môžete vidieť viac ako jednu generáciu rodinného stromu. Môžete teda prejsť priamo z pravnuka na prastarého otca bez toho, aby ste museli prechádzať cez medzigenerácie.

Všimnite si, že po zmene [Aktívnej osoby](wiki:Gramps_Glossary#active_person) v kategórii Grafy sa zobrazenie grafu znovu prispôsobí novozvolenej zameranej Aktívnej osobe. Keď sa nachádzate v kategórii Grafy, môžete jednoducho prechádzať medzi členmi zobrazeného rodinného stromu nasledujúcim spôsobom:

Ak chcete, aby sa niektorá zobrazená osoba stala zameranou Aktívnou osobou, kliknite ľavým tlačidlom myši na jej príslušný kontajner. Kliknutím pravým tlačidlom myši na kontajner sa vyvolá kontextová ponuka s možnosťami zodpovedajúcimi obsahu.

Kontextová ponuka pre kontajner Osoba môže obsahovať ▶podponuky so zoznamom všetkých manželov, súrodencov, detí a rodičov príslušnej Osoby. Prvou položkou v kontextovej ponuke bude zvyčajne meno Osoby v danom kontajneri. (Alternatívne to môže byť možnosť Upraviť.) Výberom mena Osoby sa presunie zameranie rovnakým spôsobom ako kliknutím ľavým tlačidlom myši na kontajner. Zameranie Aktívnej osoby môžete zmeniť aj na ktoréhokoľvek z manželov, súrodencov, detí alebo rodičov ktorejkoľvek zobrazenej osoby.

Niektoré zobrazenia grafov majú zjavnú navigačnú súvislosť. Pohyb po generáciách intuitívne zodpovedá pohybu v grafe doľava, doprava, nahor alebo nadol. Tieto môžu mať vlastné smerové navigačné tlačidlá, ktoré umožňujú navigáciu kliknutím namiesto ťahania.

Napríklad, ak chcete zmeniť zameranie [pohľadu Rodokmeň](wiki:Gramps_6.0_Wiki_Manual_-_Categories/sk#Pohľad_Rodokmeň) na dieťa (ak nejaké existuje) aktuálnej aktívnej osoby, kliknite na tlačidlo (*šípka vľavo*) naľavo od poľa tabuľky Aktívna osoba. Ak existuje len jedno dieťa, zameranie sa okamžite zmení. Ak má Aktívna osoba viac ako jedno dieťa, tlačidlom (*šípka vľavo*) sa rozbalí vyskakovacia ponuka s možnosťou výberu zoznamu detí. (Pre toto konkrétne tlačidlo (*šípka vľavo*) je zoznam detí vo vyskakovacej ponuke zoradený podľa poradia manželstva tohto rodiča a ďalej podľa poradia narodenia. Tieto [poradia možno zmeniť](wiki:Gramps_6.0_Wiki_Manual_-_FAQ/sk#Ako_zmeniť_poradie_detí.3F) globálne v kategórii Vzťahy).

Podobne ako kontajnery, aj tlačidlá môžu mať alternatívne funkcie prístupné kliknutím pravým tlačidlom myši a výberom z kontextovej vyskakovacej ponuky.

Ostatné tlačidlá sú menej zjavnými pomôckami na navigáciu nie k Ľuďom, ale k funkciám Gramos. Ak opäť použijeme príklad [pohľadu Rodokmeň](wiki:Gramps_6.0_Wiki_Manual_-_Categories/sk#Pohľad_Rodokmeň), prejdením po riadkoch medzi políčkami sa zobrazí nápoveda so všetkými známymi základnými údajmi o príbuzenskom vzťahu a dvojitým kliknutím na tieto riadky sa otvorí editor pre danú Rodinu. A dvojitým kliknutím na políčko Aktívna osoba sa otvorí editor pre túto osobu. Oplatí sa prečítať si podrobnú dokumentáciu ku každému pohĺadu grafu, aby ste objavili tieto skryté skratky k obľúbeným funkciám.

Zabudované Pohľady [kategórie Grafy](wiki:Gramps_6.0_Wiki_Manual_-_Categories/sk#Kategórie_Grafy) sú predstavené v odkazovanej časti [Kategórie](wiki:Gramps_6.0_Wiki_Manual_-_Categories/sk). Niektoré z nich sú podrobnejšie opísané v článkoch uvedených na konci úvodnej časti Pohľad’.

Zbierku pohľadov v kategórii Grafy možno rozšíriť o doplnky tretích strán pomocou funkcie [Správca zásuvných modulov](wiki:Gramps_6.0_Wiki_Manual_-_Plugin_Manager/sk) programu Gramps. Dostupné doplnky tretích strán nájdete v stĺpci **Pohľad** v tabuľke [Zoznam doplnkov](wiki:6.0_Doplnky#Zoznam_doplnkov). Údržbu niekoľkých doplnkových Pohľadov tretích strán si v priebehu rokov osvojil tím dobrovoľníkov programu Gramps. Tie sa stali "zabudovanými" po tom, ako boli preverené a následne zahrnuté do hlavných distribúcií programu Gramps. Články o používaní jednotlivých doplnkových pohľadov sú prepojené so stĺpcom **Zásuvný modul/Dokumentácia**. Kvalita dokumentácie týchto článkov sa výrazne líši.

## Používanie Grampletov

![[_media/DashboardCategory-DashboardView-default-gramplets-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Pohľad Kategórie na Informačnom paneli - so zobrazenými príkladmi Grampletov]]

Na [Sidebar and bottombar](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/sk#The_split-screen_Sidebar_.26_Bottombar) môžete pridať Gramplety a rozšíriť tak možnosti navigácie nad rámec vzdialenosti jednej generácie. Niektoré príklady sú:

- [Príbuzní](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/sk#Príbuzní)
- [Potomkovia](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/sk#Potomkivia)
- [Rodokmeň](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/sk#Rodokmeň)
- [Vejárový graf](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/sk#Vejárový_graf)

Tieto príklady poskytujú možnosť pohybovať sa v zameraní Aktívnej osoby s využitím perspektívy príbuzenského vzťahu... k blízkym príbuzným, potomkom alebo predkom. Budúce Gramplety by mohli umožniť navigáciu podľa geografickej blízkosti, [DNA matching](wiki:Addon:DNASegmentMapGramplet) alebo nejakého iného spojenia, o ktorom sme zatiaľ neuvažovali.

Textové Gramplety majú tendenciu mať názvy [hotlinked for navigation](#Hotlink_Navigation), zatiaľ čo grafické môžu používať [kontextové menu](#Contextual_Menu_Navigation). {{-}}

## Nastavenie Domovskej osoby

Jedna (a len jedna) osoba v databáze Rodinného sttomu môže byť určená ako [Domovská osoba](wiki:Gramps_Glossary#home_person). Po určení domovskej osoby je vrátenie zamerania [Aktívnej osoby](wiki:Gramps_Glossary#active_person) na túto osobu otázkou jedného kliknutia bez ohľadu na to, ktorá kategória sa práve používa.

Ak chcete nastaviť Domovskú osobu, najprv [navigujte](wiki:Gramps_6.0_Wiki_Manual_-_Navigation/sk#Nastavenie_Aktívnej_osoby) na túto osobu ľubovoľným spôsobom. Potom vyberte kategóriu Ľudia a zvoľte ponuku . Po vykonaní tohto kroku sa môžete na Domovskú osobu presunúť z ktoréhokoľvek miesta v databáze jednoduchým kliknutím na ikonu na paneli nástrojov . Môžete tiež zvoliť ponuku alebo vybrať položku z ľubovoľnej kontextovej ponuky dostupnej po kliknutí pravým tlačidlom myši alebo použiť klávesovú skratku .

- [Nastavenie Domovskej osoby](wiki:Gramps_6.0_Wiki_Manual_-_Settings/sk#Nastavenie_Domovskej_osoby)
- V dialógovom okne [Úprava osoby](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1/sk#Úprava_osoby) môžete z kontextového menu vybrať položku "Nastaviť Domovskú osobu".

## Nastavenie Aktívnej osoby

Očakáva sa, že [Aktívna osoba](wiki:Gramps_Glossary#active_person) bude kontextovým cieľom akcií, správ a úprav.

V pohľade Ľudia sa nachádza zvýraznenie výberu ako vizuálne upozornenie na Aktívnu osobu. V pohľade Vzťahy je Aktívna osoba zobrazená v samostatnej časti v hornej časti. Všetky ostatné osoby zobrazené nižšie majú bezprostredný (rodičovský, súrodenecký, manželský, detský) vzťah s Aktívnou osobou.

### Navigácia pomocou horúcich odkazov

Za normálnych okolností sa jednoduchým kliknutím na meno Osoby s horúcim odkazom vyberie táto osoba a presunie sa kontextové zameranie tejto Aktívnej osoby.

![[_media/Relationships-category-view-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Pohľad kategórie Vzťahy]]Každé meno osoby v pohľade kategórie Osoba a Vzťah je horúci odkaz. Zdá sa, že zmena zamerania Aktívnej osoby v pohľade Osoba iba mení, ktorý záznam je zvýraznený. To však spôsobí aj aktualizáciu obsahu Grampletov a opätovné zaostrenie pohľadov Vzťahy, Grafy a Zemepis na novú Aktívnu osobu.

Výber iného horúceho odkazu na meno v oohľade kategórie Vzťahy spôsobí menej jemnú zmenu. Pohľad na to, ako sú údaje o rodine reprezentované, sa zmení smerom k tomuto zameraniu. Ich údaje sa presunú do hornej časti a ich najbližšia rodina sa znovu usporiada pod nimi.

{{-}}

### Kontextová navigácia v menu

Mená s horúcim odkazom na karte Odkazy a Poznámky (a v niektorých grampletoch) však iba otvoria okno Editor osoby *bez* navigácie zamerania Aktívnej osoby na danú osobu. (Tieto odkazy sa správajú tak, ako keby ste klikli na tlačidlo namiesto na meno s horúcim odkazom.) To uľahčuje rýchlu úpravu osôb v okolí Aktívnej osoby bez dezorientácie z presúvania zamerania.

![[_media/QuickViewReport-EditPerson-context-menu-popup-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Kontextová ponuka v Editore osoby]] Zameranie na aktívnu osobu možno nastaviť počas pobytu v [dialógovom okne Úprava osoby](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1/sk#Dialógové_okno_Úprava_osoby) pomocou kontextovej ponuky (kliknutím pravým tlačidlom myši) v prázdnom priestore oblasti záhlavia. Voľba v tomto kontextovom menu zmení zameranie Aktívnej osoby na upravovanú osobu.

{{-}}

### Používanie navigácie založenej na histórii

![[_media/History-based-navigation-tools-Go-menu-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Príklad navigačných nástrojov založených na histórii]]

Program Gramps obsahuje aj výkonnú sadu navigačných nástrojov založených na histórii. Tieto nástroje sú podobné nástrojom bežne používaným vo webových prehliadačoch.

Patria medzi ne položky a dostupné z ponuky , kontextové ponuky (dostupné v kategóriách Ľudia, Rodina a Rodokmeň) a tlačidlá na paneli nástrojov. Zahŕňajú aj zoznam posledných výberov dostupný v ponuke , ktorá umožňuje priamy prechod na ktorýkoľvek z posledných výberov. A nakoniec, kliknutím pravým tlačidlom myši na tlačidlá a na paneli nástrojov sa vyvolá kontextové menu s príslušnou časťou histórie. Výberom ľubovoľnej položky z ponuky na ňu priamo prejdete. {{-}}

### Navigácia v záložkách

![[_media/Gramps_Go-Home48x48_win.png]] Tlačidlo Domov na paneli nástrojov je špeciálny prípad záložky. Presunie zameranie Aktívnej osoby na osobu, ktorá je aktuálne označená ako [Domovská osoba](wiki:Gramps_Glossary#Home_Person). Je to tak často užitočné, že táto funkcia má aj [klávesovú skratku](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings/sk#Bežné_klávesové_skratky).

Podobne ako pri nastavení Domovskej osoby môžete na zjednodušenie ďalšej navigácie zakladať ďalšie osoby z databázy. Ak chcete pridať záložku osoby, najprv prejdite na danú osobu a potom vyberte ponuku . Ak sa chcete presunúť na danú osobu inde v databáze, vyberte ponuku zo zobrazeného zoznamu mien záložiek. Ostatné kategórie majú vlastný zoznam Záložky.

![[_media/OrganizeBookmarks-dialog-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Usporiadať záložky]]

Záložky môžete spravovať výberom ponuky alebo stlačením [klávesovej skratky](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings/sk) . Tým sa otvorí dialógové okno so zoznamom záložiek a ovládacími prvkami na úpravu tohto zoznamu.

Pomocou tlačidiel a môžete meniť poradie zoznamu. Pomocou tlačidla odstránite záložku. Tlačidlom sa dostanete na túto stránku a okno zatvoríte tlačidlom .

Zoznam ľudí so záložkou je možné vybrať prostredníctvom kategórie Ľudia, ako je vysvetlené vyššie, ale je spoločný aj s kategóriami Vzťahy a Grafy.

Na podobnom princípe sa vedú samostatné zoznamy Záložiek v každej z nasledujúcich Kategórií: Rodiny, Udalosti, Miesta, Zdroje, Citácie, Archívy, Médiá a Poznámky.

{{-}}

### Poznámky ako navigačné skratky

![[_media/Note-showing-tooltip-for-link-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Editor poznámok - text prepojenia]] Existujú samostatné zoznamy záložiek v niekoľkých kategóriách. Stále sú to však len jednoduché zoznamy. Dlhé zoznamy záložiek sa rýchlo stanú neprehľadnými.

Trvalé odkazy je možné vytvárať v [Poznámkch](wiki:Gramps_Glossary#note). Pomocou [Editora prepojenia](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_2/sk#Editor_prepojenia) v Poznámkach môžete usporiadať navigačné odkazy na rôzne typy záznamov Gramps podľa vlastných organizačných metód. Po vytvorení prepojeného textu v poznámke možno tento prepojený záznam používať ako záložku. Na tento záznam prejdete podržaním klávesu a kliknutím na Prepojený text. Jedna poznámka sa môže použiť ako Prepojený register na iné Poznámky s rôznymi sadami prepojení.

Príkladom prepojenej poznámky môže byť nekrológ, v ktorom sú prepojené všetky Osoby, Miesta alebo aj Udalosti. To uľahčuje navigáciu k nepriamo súvisiacim (alebo aj nesúvisiacim) nosičom truhly, pohrebným [obradníkom](wiki:Gramps_Glossary#officiator) alebo účastníkom pohrebu.

Ďalšou poznámkou môže byť prepis bibliografie k publikovanému pôvodnému výskumu iného genealóga. Keď budete zhromažďovať digitálne kópie týchto pôvodne citovaných odkazov, prepojenú bibliografiu môžete použiť ako kontrolný zoznam na získanie zdrojov. Po úplnom prepojení možno Bibliografiu použiť na navigáciu v Zdrojoch pre každú citáciu pri hľadaní nepodložených záverov, nepresností alebo opomenutí.

{{-}}

## Vyhľadávanie záznamov

![[_media/Find-type-ahead-search-PeopleTreeView-list-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Zobrazenie zoznamu vyhľadaných ľudí pomocou interaktívneho typu vyhľadávania dopredu - príklad]]

Ak chcete nájsť záznam v jednom z pohľadov zoznamu kategórií, najprv sa prepnite do príslušnej kategórie, ktorá poskytuje zoznam požadovaných záznamov: Ľudia, Zdroje, Miesta alebo Médiá. Vyberte riadok v zozname, aby ste získali zaostrenie, a potom začnite písať meno osoby, resp. názov objektu Zdroj, Miesto alebo Médium, ktorý hľadáte.

Prípadne vyberte riadok v zozname, aby ste získali zameranie, a potom môžete stlačiť , aby ste zapli textové pole režimu vyhľadávania. Na otvorenie poľa aj na začatie zadávania hľadaného výrazu však stačí aj jednoduché začatie písania.

Počas písania sa prvý zodpovedajúci záznam v stĺpci triedenia zoznamu posunie do stredu zoznamu a vyberie sa. Keď zadáte ďalšie znaky, zhoda sa spresní. Kým je textové pole režimu vyhľadávania viditeľné, stlačením ovládacieho tlačidla so šípkou nadol sa presuniete na ďalšiu zhodu, zatiaľ čo stlačením ovládacieho tlačidla so šípkou nahor sa presuniete na predchádzajúcu zhodu. Po nečinnosti pole zmizne. (Keď neboli stlačené žiadne klávesy počas 5 až 15 sekúnd.) Bez aktívneho poľa Nájsť sa klávesy ovládania kurzora vrátia k posúvaniu výberu záznamov nahor a nadol v zozname.

Zmena stĺpca triedenia (kliknutím na záhlavie) zmení aj porovnávaný stĺpec. {{-}}

## Používanie Schránky

![[_media/Clipboard-dialog-example-context-menu-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Schránka - dialóg - Zobrazenie kontextovej ponuky (pravé tlačidlo myši) príklad]]

Pre program, ako je Gramps, je veľmi dôležitá, pretože pomôže znížiť počet opakovaných zadávaní údajov.

Nástroj poskytuje dočasný poznámkový blok na ukladanie záznamov z databázy na jednoduché opakované použitie počas jednej relácie programu Gramps, napr: kým neukončíte program Gramps. V skratke ide o akúsi funkciu kopíruj a vlož rozšírenú z textových objektov na iné typy záznamov používaných v programe Gramps. Schránka vo veľkej miere využíva techniku [*potiahni a pusť*](http://en.wikipedia.org/wiki/Drag-and-drop).

Ak chcete vyvolať , buď vyberte ponuku , alebo kliknite na tlačidlo na paneli nástrojov , alebo použite [Klávesovú skratku (kláves akcelerátora)](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings#8). .

{{-}}

podporuje adresy, atribúty (osobné aj rodinné), udalosti (osobné aj rodinné), mená, odkazy na mediálne objekty, citácie, adresy URL a samozrejme textové informácie poznámok a komentárov. Ak chcete uložiť akýkoľvek typ týchto záznamov, jednoducho pretiahnite existujúci záznam na bloku z príslušného dialógového okna editora. Ak chcete záznam znovu použiť, pretiahnite ho zo schránky na príslušné miesto v editore, napr. na kartu Adresa, kartu Atribút atď.

### Kontextová ponuka schránky

Výberom záznamu pomocou kontextového menu (kliknutím pravým tlačidlom myši) sa zobrazia nasledujúce tri možnosti pre každý typ záznamu:

- 

- 

- 

{{-}}

Jeden príklad  
Nájdete rodný list osoby. V tomto osvedčení sú uvedení aj svedkovia. A v rodnom liste je určený aj zdroj, kde boli informácie uložené. Najlepšie je otvoriť schránku a pretiahnuť tam zdroj, s ktorým chcete pracovať. Potom ho pomocou funkcie potiahni a pusť použite v nových položkách, ktoré používate.

Teraz môžete dokončiť informácie na obrazovke editora osoby. Túto informáciu tiež pretiahnite do Schránky.

Teraz pridajte dve nové osoby pre svedkov (za predpokladu, že ich ešte nemáte v databáze). Jednoducho pretiahnite informácie o narodení na obrazovku udalosti svedka. Potom sa zobrazí obrazovka, kde môžete zmeniť úlohu svedka na svedka pre túto udalosť narodenia. To isté urobíte s druhým svedkom.

Ušetríte si tak veľa písania a možných chýb.

## Hlavné ponuky

![[_media/Menubar-MainMenuOverview-NoFamilyTree-Loaded-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Panel ponuky - Prehľad hlavného menu - Nie je načítaný rodinný strom]] ![[_media/Menubar-MainMenuOverview-FamilyTree-Loaded-60.png|vpravo\|450px\|Fig. {{#var:chapter}}.{{#vardefineecho:figure\|{{#expr:{{#var:figure}}+1}}}} Panel ponuky - Prehľad hlavného menu - Rodinný strom načítaný]] ![[_media/Menubar-MainMenuOverview-FamilyTree-Loaded-Active-Go-Windows-menus-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Panel ponuky - Prehľad hlavného menu - Načítaný rodokmeň zobrazujúci používané položky menu &quot;Aktívne&quot; a &quot;Okná&quot;]]

Panel ponuky zobrazuje dostupné Gramps Menu, ktoré sa menia a zobrazujú v závislosti od použitej Kategórie napr: Upraviť / Pohľad.

{{-}}

### 

![[_media/Menubar-FamilyTrees-overview-FamilyTree-Loaded-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Panel ponuky - "Rodinné stromy" - príklad prehľadu]]

- } - otvorí [Okno správcu_rodinných_stromov](wiki:Gramps_6.0_Wiki_Manual_-_Správa_rodinných_stromov#Okno_správcu_rodinných_stromov)

- \- skratka na otvorenie nedávno rozpracovaného rodinného stromu

- \- zálohovanie a zatvorenie aktuálneho stromu

<hr>

- \- Preniesť údaje z iných [formátov](wiki:Gramps_6.0_Wiki_Manuál_-_Správa_Rodinných_stromov#Importovanie_údajov).  
  ''Pred importom si vytvorte zálohu! Existujú [import Preferences](wiki:Gramps_6.0_Wiki_Manual_-_Settings)sk#General_Gramps_settings) na označenie importovaných údajov atribútmi [Tag](wiki:Gramps_Glossary#tag) a/alebo [Source](wiki:Gramps_Glossary#source) s časovou značkou. Tieto možnosti výrazne spomaľujú proces importu, ale sú užitočné pri následnom čistení údajov.

- \- [Exporting data](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees#Exporting_data) vám umožňuje zdieľať akúkoľvek časť vášho rodinného stromu Gramps s inými bádateľmi, ako aj umožňuje preniesť vaše údaje na iný počítač.

<hr>

- \- Ponuka sa zobrazuje vo väčšine Pohľadov, len ak je možné exportovať zobrazené údaje. Gramps vyexportuje údaje na obrazovke podľa vášho výberu: **CSV** alebo **Open Document** formát tabuľky.

<hr>

- \- Umožňuje vytvoriť [Úplná záloha Gramps XML](wiki:Gramps_6.0_Wiki_Manuál_-_Správa_Rodinných_stromov#Zálohovanie_rodinného_stromu) vášho aktuálne otvoreného rodokmeňa. Všimnite si, že [niektoré položky konfigurácie a Médiá sú zo zálohy XML vynechané](wiki:Šablóna:Zálohovanie_Oprávnenia).

<hr>

- \-

- \-

{{-}}

### 

![[_media/Menubar-Add-a-new-object-overview-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Panel ponuky - Pridať prehľad]]

- \- nový [objekt](wiki:Gramps_Glossary#primary_object)  
  tiež pozri [klávesové skratky](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings/sk).

<hr>

- \- pridáva [Osoba](wiki:Gramps_Glossary#person) *([prim. obj.](wiki:Gramps_Glossary#primary_object))*

- \- pridá [Rodina](wiki:Gramps_Glossary#family) *([prim. obj.](wiki:Gramps_Glossary#primary_object))* - Zobrazí }

- \- pridáva [Udalosť](wiki:Gramps_Glossary#event) *([prim. obj.](wiki:Gramps_Glossary#primary_object))*

- \- pridá [Miesto](wiki:Gramps_Glossary#place) *([prim. obj.](wiki:Gramps_Glossary#primary_object))*

- \- pridá [Zdroj](wiki:Gramps_Glossary#source) *([prim. obj.](wiki:Gramps_Glossary#primary_object))*

- \- pridá [Citácia](wiki:Gramps_Glossary#citation) *([prim. obj.](wiki:Gramps_Glossary#primary_object))*

- \- pridáva [Archív](wiki:Gramps_Glossary#repository) *([prim. obj.](wiki:Gramps_Glossary#primary_object))*

- \- pridá [Médium](wiki:Gramps_Glossary#media) *([prim. obj.](wiki:Gramps_Glossary#primary_object))*

- \- pridá [Poznámka](wiki:Gramps_Glossary#note) *([prim. obj.](wiki:Gramps_Glossary#primary_object))*

<hr>

{{-}}

### 

![[_media/Menubar-Edit-defaults-family-tree-loaded-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:obrázok}}+1}}}} Menubar - Prehľad úprav]]

- \-

- \-

- } - Otvorenie dialógového okna

<hr>

Tu sa zobrazia ďalšie možnosti ponuky závislé od zobrazenia Kategória.

- \- Pozri [Označovanie](wiki:Gramps_6.0_Wiki_Manual_-_Filters/sk#Označovanie).

<hr>

- \- Nástroj schránka poskytuje dočasný poznámkový blok na ukladanie záznamov z databázy na jednoduché opätovné použitie.

<hr>

- \- Zobrazí dialógové okno . To vám umožňuje zmeniť väčšinu nastavení programu Gramps.

- Zobrazia sa tu ďalšie možnosti ponuky závislé od pohľadu Kategória.

{{-}}

### 

![[_media/Menubar-View-overview-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menubar - "Zobraziť" - príklad prehľadu]]

- } - Umožňuje konfigurovať aktívny pohľad. Poskytuje možnosti na skrytie, odhalenie a zmenu usporiadania prvkov.

- } - Navigátor je kontajner bočného panela pre ikony kategórie Navigátor. Keď je vybratý (predvolené nastavenie), bočný panel sa zobrazuje na ľavej strane aktívneho Zobrazenia. Zrušením výberu sa bočný panel Navigátor skryje. Ak sa všetky ikony Kategórie nezmestia do dostupného zvislého priestoru, vytvorí sa na pravej strane bočného panela skrytý posuvník, ktorý sa odkryje po prejdení (nabehnutí) naň.  
  Textové označenia ikon možno skryť pomocou voľby na karte [Zobrazenie](wiki:Gramps_6.0_Wiki_Manual_-_Settings/sk#Zobrazenie) v Nastaveniach. [Režimy pohľadu](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window/sk#Prepínanie_režimov_navigátora) možno vybrať z kontextového menu v dolnej časti bočného panela navigátora.

- \- zobrazí (alebo skryje) kontajner rozdelenej obrazovky pre (často používané) ikony akcií nad zobrazením kategórie. Výber ikon akcií sa mení podľa zobrazenia Kategórie.  
  Možno nainštalovať [Doplnky tretích strán](wiki:Doplnky_tretích_strán), ktoré doplnia Predvoľby o kartu [Téma](wiki:Doplnok:Témy) poskytujúcu možnosť zobrazenia textových štítkov pre každé tlačidlo panela nástrojov.

- \- Zobrazenie (alebo skrytie) kontajnera rozdelenej obrazovky pre Gramplety vpravo od zobrazenia kategórie.

- \- Zobrazenie (alebo skrytie) kontajnera rozdelenej obrazovky pre Gramplets v spodnej časti okna, tesne nad stavovým riadkom.

- \- Rozšírenie okna tak, aby sa využilo celé dostupné miesto na obrazovke, pričom sa vypnú ovládacie prvky preťahovania a zmeny veľkosti okna. Zrušením výberu sa obnoví predchádzajúca veľkosť, pričom sa opäť povolia ovládacie prvky na ťahanie a zmenu veľkosti okna.

<hr width=25%>

- V závislosti od toho, ktoré zobrazenie je aktívne, sa tu zobrazia ďalšie položky ponuky možností, ktoré môžu upraviť spôsob, akým Zobrazenie organizuje údaje.

{{-}}

### 

![[_media/Menubar-GoOverview-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menubar - Prehľad Go]]

- \- naviguje výber aktuálneho Zobrazenia späť na *predchádzajúcu* položku vo vašom [História navigácie](wiki:Gramps_6.0_Wiki_Manuál_-_Navigácia#Používanie_navigácie_založenej_na_histórii)

- \- naviguje výber aktuálneho Zobrazenia dopredu na *ďalšiu* položku vo vašej [Navigation history](wiki:Gramps_6.0_Wiki_Manual_-_Navigation#Using_history-based_Navigation)

<hr>

- \- naviguje zameranie [Aktívna osoba](wiki:Gramps_Glosár#active_person) na jednotlivé [nastavenie](wiki:Gramps_6.0_Wiki_Manual_-_Settings/sk#Nastavenie_Domovskej_osoby) ako [Domovská osoba](wiki:Gramps_Glosár#home_person).

<hr>

- Dynamický zoznam posledných 10 vybraných záznamov (Ľudia, Rodiny a pod.), zoznam závisí od pohľadu Kategórie.

{{-}}

### 

![[_media/Menubar-BookmarksOverview-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menubar - Prehľad záložiek]]

- \- Vytvorenie záložky z aktuálne vybranej položky napr: záložku: Osoba, Rodina atď..

- } - Otvorí okno [Usporiadanie záložiek](wiki:Gramps_6.0_Wiki_Manual_-_Navigation#Navigácia_záložiek).

<hr>

- Dynamická časť, v ktorej sa zobrazujú záložky

{{-}}

### 

![[_media/Menubar-ReportsOverview-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menubar - Prehľad zostáv]]

- \- Nástroj [Knižné správy](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_3/sk#Knihy) umožňuje vytvoriť vlastnú genealogickú knihu obsahujúcu zbierku textových a grafických správ Gramps v jednom dokumente (t. j. knihe)

<hr>

- \-

  - 

  - 

  - 

- } -

  - 

  - 

  - 

  - 

  - 

  - 

  - 

- } -

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

  - 

  - 

  - 

  - 

  - 

- \-

  - 

  - 

{{-}}

### 

![[_media/MenuOverview-Tools-default-60.png|vpravo|450px|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "" Menubar - Prehľad nástrojov]]

- \-

  - 

  - \-

- \-

  - 

  - 

  - 

  - 

  - \-

  - \-

- \-

  - 

  - 

  - 

  - 

  - }

  - }

  - 

  - 

  - 

  - 

- \-

  - 

  - 

  - 

  - 

  - 

- - 

  - 

  - 

  - 

{{-}}

### 

![[_media/Menubar-Windows-menu-overview-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menubar - "Windows" - prehľadný príklad]]

- \- Toto menu poskytuje rýchly prístup k otvoreným oknám, s ktorými pracujete.

{{-}}

### 

![[_media/Menubar-Help-overview-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menubar - "Pomoc" - prehľadný príklad]]

- \- Priamy odkaz na online používateľskú príručku programu Gramps, ktorú si práve prezeráte. Áno, na nahliadnutie do používateľskej príručky programu Gramps potrebujete internetové pripojenie.

- \- Odkaz na [Často kladené otázky](wiki:Gramps_6.0_Wiki_Manual_-_FAQ) o programe Gramps.

- \- Odkaz na [Odkaz na väzby klávesov](wiki:Gramps_6.0_Wiki_príručka_-_Väzby_klávesov) pre program Gramps. Známe aj ako Klávesové skratky.

- \- Zobrazí dialógové okno "Tip dňa".

- \- V tejto ponuke môžete spravovať vstavané zásuvné moduly, ako aj všetky [Doplnky tretích strán](wiki:6.0_Doplnky), ktoré môžete mať nainštalované.

- \- Táto položka otvorí váš webový prehliadač a pripojí vás na webovú stránku projektu Gramps.

- \- Táto položka otvorí váš webový prehliadač a otvorí stránku poštového zoznamu projektu Gramps. Na tejto stránke si môžete prezerať archívy poštovej konferencie a pripojiť sa k poštovej konferencii gramps-users, aby ste sa mohli podeliť o svoje skúsenosti s ostatnými používateľmi Gramps.

- \- Vyberte túto položku, ak chcete podať [hlásenie o chybe](wiki:Using_the_bug_tracker) v systéme sledovania chýb Gramps. (Toto si vyžaduje, aby ste mali zaregistrované konto v systéme hlásenia chýb Gramps.) (Nezabudnite, že Gramps je živý projekt. Chceme vedieť o všetkých problémoch, na ktoré narazíte, aby sme ich mohli vyriešiť pre vás a pre všetkých ostatných.)

- \- Odkaz na [Inštalácia doplnkov tretích strán v programe Gramps](wiki:6.0_Doplnky).

<!-- -->

- \- Táto položka zobrazí dialógové okno so všeobecnými informáciami o verzii programu Gramps, ktorú používate.

## Panel nástrojov

- Panel nástrojov: [Panel nástrojov](wiki:Gramps_Glossary#toolbar) sa nachádza priamo pod panelom ponuky. Umožňuje prístup k najčastejšie používaným funkciám programu Gramps.
- Sortiment zobrazených tlačidiel nástrojov závisí od toho, ktorá kategória [pohľadu](wiki:Gramps_Glossary#view) je aktívna
- ⚙ Konfigurovateľné možnosti: Väčšina pohľadov Kategórie má tlačidlo ![[_media/Gramps-config.png]]  ako alternatívu k výberu z ponuky Pohľad alebo stlačením tlačidla *Konfigurovať aktívny pohľad* [klávesnice](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings/sk#Obvyklé_klávesové_skratky). Táto možnosť otvorí dialógové okno s voľbami pre zobrazenie záznamov v pohľade. (Dialógové okno bude obsahovať aj záložky pre všetky pridané [Gramplets, ktoré majú konfigurovateľné možnosti](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#.E2.9A.99_Configurable_Options_2)).
- Podržaním kurzora nad ikonou panela nástrojov sa zobrazí tip na jej funkciu

![[_media/ToolbarIcon-OpenTheToolsDialog-60.png|Fig {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}} Tip pre tlačidlo Nástroje na paneli nástrojov kategórie Ovládací panel]] Panel nástrojov môžete skryť alebo odkryť pomocou voľby v ponuke .

`Doplnok `[<code>Themes</code>](wiki:Addon:ThemePreferences)` rozširuje dialógové okno `[<code>Predvoľby</code>](wiki:Gramps_6.0_Wiki_Manual_-_Settings/sk)` o kartu `*`Theme`*`. `

Jednou z možností karty Téma je zaškrtávacie políčko ☑ . Zaškrtnutie tohto políčka spôsobí, že sa zobrazia textové štítky.  
*Toto políčko je* ❏''štandardne odznačené. ![[_media/Preferences-Themes-addon.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}} Pridané možnosti karty Téma pre dialógové okno Predvoľby]]}}

{{-}} ![[_media/FamilyTrees-ManageDatabases-icon-toolbar-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure\|{{#expr:{{#var:figure}}+1}}}} Správa databáz - ikona na paneli nástrojov (Rovnaká ako pri použití ponuky]] {{-}} ![[_media/ConnectToARecentDatabase-icon-toolbar-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure\|{{#expr:{{#var:figure}}+1}}}} Pripojenie k nedávnej databáze - rozbaľovacia ikona v ponuke panela nástrojov]] {{-}}

{{-}}

[Category:Sk:Documentation](wiki:Category:Sk:Documentation)
