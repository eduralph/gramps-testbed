---
title: Gramps 6.0 Wiki Manual - Gramplets/sk
categories:
- Sk:Documentation
- Stub
managed: false
source: wiki-scrape
wiki_revid: 126611
wiki_fetched_at: '2026-05-30T20:06:27Z'
lang: sk
---

{{#vardefine:chapter\|12}} {{#vardefine:figure\|0}} Na tejto stránke nájdete podrobné informácie o funkciách Grampletov, ktoré sa dodávajú s programom Gramps.

# Čo je to gramplet?

<span id="definícia"> ![[_media/DashboardCategory-DashboardView-default-gramplets-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Kategória prístrojovej dosky (predvolené zobrazenie)]]

[Gramplet](wiki:Gramps_Glossary#gramplet) je rozšírenie jadra programu Gramps, ktoré **dúfajme** funguje bez problémov ako vstavaná funkcia. Gramplety poskytujú doplnkový pohľad na údaje stromu, ktorý sa buď: dynamicky mení počas navigácie v programe Gramps Tree, alebo; poskytuje interaktivitu vašich genealogických údajov.

Gramplety sú zásuvné moduly (nazývané aj [widgets](http://wikipedia.org/wiki/Widget_engine), pluginy, doplnky, pomocné komponenty), ktoré sa stávajú súčasťou programu Gramps a možno ich nájsť v kategórii **Informačný panel** ... alebo v **Bočné panely** a **Spodné panely** v iných kategóriách navigátora. Poskytujú všetky druhy funkcií, ktoré môžu byť užitočné pre bádateľa.</span>

## Nie sú všetky zásuvné moduly tiež Gramplety?

Aký je rozdiel medzi Grampletami, zostavami, rýchlymi zobrazeniami a nástrojmi?

Všetky tieto typy sú **zásuvné moduly**. Gramplety sú však podtypom zásuvných modulov s väčším dôrazom na používateľské rozhranie. Gramplety pridávajú **schopnosť** alebo **iný pohľad** do zobrazenia. Možno ich použiť na zlepšenie pracovného postupu zobrazenia View.

Ostatné zásuvné moduly majú tendenciu prerušiť bežný pracovný postup na vykonanie inej úlohy. Majú tiež tendenciu používať sa viac prerušovane. Zásuvný modul môže generovať statický (aj keď je prepojený za prevádzky) snímok údajov, môže byť spôsobom, ako vykonať hromadnú zmenu, alebo poskytovať alternatívny systém importu/exportu/výstupu.

Niektoré bežné [Typy pluginov](wiki:Gramps_6.0_Wiki_Manual_-_Plugin_Manager#Typy_pluginov) sú:

- Reporty - poskytujú statický výstupný formát vašich údajov, zvyčajne na prezentáciu
- [Quick Views](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_8#Quick_Views) - poskytuje zvyčajne krátky interaktívny výpis odvodený z vašich údajov
- Nástroje - poskytujú spôsob spracovania vašich údajov
- Gramplety - poskytujú dynamický pohľad a rozhranie na vaše údaje.

Hlbšie pochopenie rôznych typov doplnkov možno získať zoradením [Soznam doplnkov](wiki:6.0_Addons#Addon_List) podľa **Typu** a preskúmaním kontrastných **Popisov**.

Niektoré zo statickejších typov prídavných modulov možno rozšíriť tak, aby fungovali dynamicky ako Gramplet.

Niekoľko zásuvných modulov sa vyvinulo do viacerých typov. Niektoré zásuvné moduly sú škrupiny, ktoré vrstvia ďalšie možnosti okolo iných zásuvných modulov. **Rýchle zobrazenie** Gramplet nie je [typ zásuvného modulu Quick View](wiki:Gramps_6.0_Wiki_Manuál_-_Reporty_-_časť_8#Quick_Views). Namiesto toho je to dokovateľná schránka, ktorá zobrazuje zásuvný modul **Quick View** a tlačí na obnovenie zásuvného modulu pri zmene kontextu.

## Začíname s aplikáciou Gramplets

Pri prvom spustení [Dashboard Category](wiki:Gramps_6.0_Wiki_Manual_-_Categories#Dashboard_Category) sa zobrazia dva predvolené Gramplety; **** Gramplet a ****.

Keďže Gramps 4.2 rozšíril niektoré funkcie prístrojovej dosky na ďalšie kategórie navigátora, máme **spoločné** a **špecifické** Gramplets.

- Spoločné Gramplety sú použiteľné pre akýkoľvek Pohľad ... a pohľad na údaje je vzhľadom na Kontext Aktívnej osoby a/alebo Domácej osoby. Môžu byť zakotvené na ľubovoľnom Zobrazení kategórie Navigátora bez toho, aby sa Zobrazenie stalo jednoznačným.
- Špecifické Gramplety potrebujú kontext konkrétnych Pohľadov, aby poskytli kontext svojej perspektívy údajov. Zoznam ponuky Pridať Gramplety sa bude líšiť podľa aktívneho Zobrazenia kategórie a nainštalovaných Grampletov.

Tento zoznam zostal z predchádzajúcej revízie wiki. Nie je jasné, kam tieto položky v tejto diskusii patria.

- Spätné odkazy Gramplets - poskytujú okamžitú viditeľnosť údajov, ktoré bývajú zobrazované príležitostne a sú zahrabané v rozhraní... ako napríklad záložka v Editore objektov.
- Gramplety filtrov sú ako predchádzajúci bočný panel filtrov
- Spoločné modely pre poznámky, galériu, zdroje, citácie, udalosti
- Gramplety detí na zobrazeniach Osoby (tiež kategória grafy a kategória vzťahy), zobrazenie rodiny

## Všeobecné používanie a konfigurácia

![[_media/WelcomeToGramps-Gramplet-docked-in-dashboard-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Uvítací gramplet Informačného panela]] Ovládacie prvky kontajnera pre Gramplety sú v kategórii Dashboard View usporiadané trochu inak ako v bočnom a spodnom paneli. Uvedomenie si toho, ako sa tieto kontajnery Grampletu líšia (a sú si podobné), vám umožní sústrediť sa na dosiahnutie vysokorýchlostného výkonu namiesto toho, aby ste sa čudovali, prečo sa roztočil.

Gramplety, ktoré boli pôvodne pridané vo verzii 3, sú v zobrazení kategórie Dashboard View usporiadané do konfigurovateľného počtu stĺpcov. Bočný panel a Bottombar [rozdelené panely](wiki:Split_Views) boli vybrané spomedzi neskorších inovácií navrhnutých v [GEPS 19](wiki:GEPS_019:_Improved_Sidebar_and_Split_Views). Boli postavené na bočnom paneli filtra verzie 3.3. Filter bol prevedený na Gramplet'' a predinštalovaný v bočnom paneli.

![[_media/Welcome-to-Gramps-Gramplet-detached-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Odpojený bočný panel Uvítací gramplet]]Rozdelené panely poskytujú obmedzený priestor na obrazovke pre dokovanie grampletov v iných kategóriách Navigátora. Na rozdiel od mnohých stĺpcov v zobrazení Dashboard View je však každý nový rozdelený panel jediným stĺpcom, ktorý je vyplnený jedným Grampletom. (Podokno stále podporuje uloženie viacerých Grampletov, len na ich zobrazenie po jednom používa karty Tab).

Prístup rozdeleného podokna znižuje potrebu prepínania medzi Zobrazeniami kategórií... a to znižuje nároky na databázu.

![[_media/DashboardCategory-gramplet-detached-and-docked-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Odpojený gramplet v zobrazení prístrojovej dosky]] Gramplety však možno odpojiť (oddeliť, odtrhnúť) a vznášať sa voľne z ktoréhokoľvek z troch kontajnerov. Po odpojení sa v ľavom dolnom rohu otvorí dodatočné tlačidlo , ktoré otvorí stránku Grampletu na tejto webovej stránke. Kliknutím na tlačidlo  v pravom hornom rohu sa odpojený gramplet opäť pristaví. Kliknutím na podobné  tlačidlo odpojeného Grampletu ho odstránite z panela.

### Pohľad kategórie na informačnom paneli

V [Dashboard](wiki:Gramps_6.0_Wiki_Manual_-_Categories#Dashboard_Category) môžete ťahaním  tlačidla (vľavo hore) každého grampletu zmeniť jeho polohu v oblasti Dashboard View (Zobrazenie na prístrojovej doske). Kliknutím na tlačidlo  môžete gramplet odpojiť (alebo *‘undock’*) zo zobrazenia Dashboard View a umiestniť ho do vlastného okna. Okno zostane otvorené bez ohľadu na stránku (vzťahy, grafy atď.). Zatvorením odpojeného zobrazenia sa vráti späť do zobrazenia Dashboard. Ak ukončíte program Gramplet s otvoreným oknom Gramplet, pri opätovnom spustení programu Gramplet sa automaticky otvorí.

Keď je jeden alebo viacero grampletov odpojených od zobrazenia Dashboard (Informačný panel), zostanú viditeľné, keď sa prepnete do iného zobrazenia (napríklad do zobrazenia Ľudia alebo Grafy). Týmto spôsobom môžete tieto gramplety použiť na doplnenie konkrétneho Zobrazenia o ďalšie podrobnosti a funkcie, ktoré poskytuje gramplet.

Nové Gramplety môžete pridať kliknutím pravým tlačidlom myši na voľné miesto v zobrazení Dashboard (Informačný panel). Kliknutím na  tlačidlo nad Grampletom ho odstránite z Informačného panela.

#### ⚙ Konfigurovateľné možnosti

![[_media/Menubar-View-overview-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Zobraziť menu]] Počet stĺpcov môžete zmeniť aj zmenou nastavenia záložky *Rozloženie grafov* v okne *Konfigurácia ovládacieho panela*. Okno otvoríte kliknutím na ![[_media/Gramps-config.png]] tlačidlo, výberom z ponuky Pohľad alebo stlačením tlačidla *Konfigurovať aktívny pohľad* [klávesnice](wiki:Gramps_6.0_Wiki_Manuál_-_Keybindings#Common_keybindings). ![[_media/Whats-next-gramplet-configure-dashboard-60.png|Obrázok {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Karty konfigurácie grampletu]] Ku každému grampletu s dokom na ovládacom paneli sa pridá aj karta Konfigurácia. (Ale ten istý Gramplet nemusí mať žiadne možnosti Konfigurácia alebo kartu Konfigurácia, keď je zakotvený na bočnom paneli alebo na spodnom paneli.) Ovládací panel poskytuje dodatočné možnosti pre každý Gramplet, ktoré umožňujú jeho premenovanie, nastavenie pevnej vertikálnej veľkosti alebo jeho vertikálne maximalizovanie v stĺpci. Karta Konfigurácia pre Gramplety v doku v paneli Dashboard odráža aspoň tieto minimálne možnosti.

Dvojité kliknutie na názov grampletu zakotveného v kategórii Dashboard umožňuje zmeniť zobrazovaný názov.

### Rozdelený bočný panel & amp; spodný panel

![[_media/Bottombar-sidebar-drop-down-menu-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Rozdelené obrazovky Grampletu zobrazujúce Gramplet Bar Menu s neoznačeným tlačidlom Down Arrowhead  pull-down menu]]. Každá z týchto rozdelených obrazoviek je kontajnerom poskladaných kariet Gramplet. Podobne ako v systéme Windows so sekciou s kartami, každá z nich môže naraz zobraziť len jednu kartu. Karty sa však dajú pridávať, meniť ich poradie, odkrývať alebo vypínať podobne ako na prístrojovej doske. Namiesto kontextovej ponuky má však každá rozdelená plocha tlačidlo vysúvacieho menu, ktoré zobrazí rovnaký vyskakovací zoznam možností.

Ak chcete pridať gramplety na stohované karty, vyberte ich z podmenu.

<span id="undock gramplet">Aby ste odomkli záložku, uchopte jej názov a potiahnite ju von z rozdeleného panela. Ak chcete znova dokovať, kliknite na tlačidlo Zatvoriť alebo na tlačidlo "X".</span>

Ak chcete odstrániť kartu Gramplet zo zásobníka kariet, vyberte ju z ponuky podmenu. (Prípadne môžete použiť Tlačidlo zatvoriť bude prístupné, ak je začiarknuté políčko "Zobraziť tlačidlo zatvorenia na kartách grampletu" na karte [Zobrazenie](wiki:Gramps_6.0_Wiki_Manual_-_Settings/sk#Zobrazenie) v záložke Predvoľby).

Zaujímavé je, že tie isté gramplety môžu byť záložkami v inej časti rozdelenej obrazovky Zobrazenie, ale môžu byť nakonfigurované tak, aby sa informácie zobrazovali odlišne. Je dôležité si uvedomiť, že každý Gramplet (či už naskladaný ako karta alebo plávajúci odpojený) brzdí výkon programu Gramps. Používajte menej Grampletov, aby Gramps reagoval rýchlejšie.

Zoznamy Grampletov, ktoré možno pridať do zásobníka kariet v rozdelenom podokne, sú filtrované podľa tých, ktoré sú vhodné pre danú kategóriu.

#### ⚙ Konfigurovateľné možnosti

![[_media/Menubar-View-overview-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Zobraziť menu]]

Okrem toho existuje množstvo doplnkov tretích strán Gramplets, ktoré môžete jednoducho nainštalovať a používať. Patria medzi ne:

- Headline News Gramplet - aktuálne, mimoriadne správy z Grampletu
- Data Entry Gramplet - editácia mena aktívnej osoby, dátumu a miesta narodenia, dátumu a miesta úmrtia a pridávanie osôb
- Python Gramplet - shell v jazyku Python
- FAQ Gramplet - často kladené otázky
- Note Gramplet - zobrazenie a úprava primárnej poznámky aktívnej osoby

a mnoho ďalších. Viac informácií nájdete v časti [Doplnky tretích strán](wiki:Doplnky_tretích_strán).

# Prehľad zabudovaných grampletov

Zhrnutie všetkých predvolených vstavaných grampletov a kategórií pohľadov, v ktorých možno každý gramplet použiť.

Nezávisle pre každý kontajner režimu pohľadu Kategória možno gramplety pridávať alebo odoberať pomocou nasledujúcich ovládacích prvkov:

- V kategórii Informačný panel prostredníctvom kontextovej ponuky pravého tlačidla myši.
- Vo všetkých ostatných Kategóriách prostredníctvom rozbaľovacích ponúk pre výber grampletu (*Tlačidlo šípky nadol*) na spodnom alebo bočnom paneli.

*Neexistujú žiadne možnosti Menu na pridanie Grampletu. Je to preto, lebo by bolo nejednoznačné, či sa má Gramplet pridať na bočný panel alebo dolný panel daného režimu zobrazenia.* {{-}}

## Vstavaný zoznam grampletov

Kliknutím na záhlavie kategórie (dvakrát) sa zoznam zoradí a zobrazí sa ponuka dostupných zabudovaných možností Grampletu danej kategórie. (Aktuálna ponuka bude obsahovať aj nainštalované [doplnky tretích strán](wiki:6.0_Doplnky#Zoznam_doplnkov). Gramplets.)

| Gramplet | ![[_media/22x22-gramps-gramplet.png]] Informačný panel | ![[_media/22x22-gramps-person.png]] Ľudia | ![[_media/22x22-gramps-relation.png]] Vzťahy | ![[_media/22x22-gramps-family.png]] Rodiny | ![[_media/22x22-gramps-pedigree.png]] Grafy | ![[_media/22x22-gramps-event.png]] Udalosti | ![[_media/22x22-gramps-place.png]] Miesta | ![[_media/22x22-gramps-geo.png]] Zemepis | ![[_media/22x22-gramps-source.png]] Zdroje | ![[_media/22x22-gramps-citation.png]] Citácie | ![[_media/22x22-gramps-repository.png]] Archívy | ![[_media/22x22-gramps-media.png]] Médiá | ![[_media/22x22-gramps-notes.png]] Poznámky |
|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
| id="0" \| |  | ✔ | ✔ |  | ✔ |  |  | ✔ |  |  |  |  |  |
| id="1" \| | ♦ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| id="2" \| | ♦ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| id="3" \| |  | ✔ | ✔ |  | ✔ |  |  | ✔ |  |  |  |  |  |
| id="4" \| |  | ✔ | ✔ | ✔ | ✔ | ✔ |  | ✔ | ✔ | ✔ |  | ✔ |  |
| id="5" \| | ♦ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| id="6" \| |  | ✔ | ✔ | ✔ | ✔ |  |  | ✔ |  |  |  |  |  |
| id="7" \| |  | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |  |  |  | ✔ |  |
| id="8" \| |  | ✔ | ✔ |  | ✔ |  |  | ✔ |  |  |  |  |  |
| id="9" \| |  | ✔ | ✔ |  | ✔ |  |  | ✔ |  |  |  |  |  |
| id="10" \| |  | ✔ | ✔ |  | ✔ |  | ✔ | ✔ |  |  | ✔ |  |  |
| id="18a" \| |  |  |  |  |  |  | ✔ |  |  |  |  |  |  |
| id="18b" \| |  |  |  |  |  |  | ✔ |  |  |  |  |  |  |
| id="11" \| |  | ✔ | ✔ | ✔ | ✔ |  |  | ✔ |  |  |  |  |  |
| id="11a" \| |  | ✔ | ✔ | ✔ | ✔ |  |  | ✔ |  |  |  |  |  |
| id="12" \| | ♦ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| id="13" \| |  | ✔ | ✔ |  | ✔ |  |  | ✔ |  |  |  |  |  |
| id="14" \| |  |  | ✔ |  | ✔ |  |  |  |  |  |  |  |  |
| id="15" \| |  | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |  |  |  |
| id="16" \| | ♦ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| id="17" \| |  |  |  |  |  |  |  |  |  |  |  | ✔ |  |
| id="21" \| |  |  |  |  |  |  |  |  |  |  |  | ✔ |  |
| id="19" \| |  | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |  |
| id="20" \| |  | ✔ | ✔ |  | ✔ |  |  | ✔ |  |  |  |  |  |
| id="22" \| | ♦ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| id="23" \| | ♦ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| id="24" \| |  | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| id="25" \| |  | ✔ | ✔ |  | ✔ |  |  | ✔ |  |  |  |  |  |
| id="26" \| |  | ✔ | ✔ |  | ✔ |  |  | ✔ |  |  |  |  |  |
| id="27" \| | ♦ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| id="28" \| | ♦ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| id="29" \| | ♦ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| id="30" \| | ♦ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| id="31" \|} | ♦ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| id="32" \| | ♦ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| id="35" \|} | ⚠ | ⚠ | ⚠ |  | ⚠ | ⚠ | ⚠ | ⚠ | ⚠ | ⚠ | ⚠ | ⚠ | ⚠ |
| id="33" \| | ♦ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| id="34" \|} | ♦ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| id="xx" \| |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |

Podrobnejšie informácie o používaní nainštalovaného Grampletov nájdete v časti [Gramplety](wiki:Gramps_6.0_Wiki_manual_-_Gramplets/sk#Gramplety). {{-}}

# Gramplety

V nasledujúcich častiach sú popísané jednotlivé gramplety a ich základné funkcie. {{-}}

## 2-cestný graf ventilátora

![[_media/2-WayFanChart-detached-gramplet-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} 2-Way Fan Gramplet]]

**Pozri tiež:** {{-}}

## Vek na dátum

![[_media/AgeOnDate-Gramplet-detached-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Gramplety s vekom na dátum - oddelený príklad]]

Gramplet umožňuje zadať [Kalendárny dátum](https://en.wikipedia.org/wiki/Calendar_date) do vstupného poľa . Ak vyberiete , Gramplet vypočíta vek pre všetkých vo vašom rodokmeni žijúcich v tento Dátum a výsledky zobrazí v samostatnom dialógovom okne Rýchle zobrazenie správy. Dátum musí byť zadaný v kalendárnom formáte, ktorý Gramplet akceptuje, napr: RRRR-MM-DD .

- Pre tento gramplet nie sú k dispozícii žiadne možnosti konfigurácie.

{{-}} ![[_media/AgeOnDate-Gramplet-QuickView-example-result-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Vek v dátume Gramplet - rýchle zobrazenie - príklad výsledku]]

Vo výslednom dialógovom okne rýchleho zobrazenia správy môžete triediť podľa stĺpcov Osoba, Vek alebo Stav. Kliknutím pravým tlačidlom myši na riadok sa otvorí kontextové menu, ktoré umožňuje *skopírovať všetky* riadky do schránky; alebo *zobraziť podrobnosti o osobe* v editore osôb, alebo *urobiť osobu aktívnou*.

{{-}}

- Dátum môžete tiež pretiahnuť z [Kalendárny gramot](wiki:Gramy_6.0_Wiki_Manuál_-_Gramplets/sk#Gramplet_Kalendár) na Gramplets vstupného poľa, aby ste tento dátum zadali.
- Pozri tiež [Doplnok tretej strany](wiki:Doplnky_tretích_strán) [Kalkulátor dátumu Gramplet](wiki:Addon:DateCalculator), ktorý vám umožňuje počítať dátum.

{{-}}

## Štatistiky veku

![[_media/AgeStats-Gramplet-detached-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Štatistiky veku Gramplet - oddelený príklad]]

Gramplet zobrazuje štatistiky vo forme troch textových grafov zoskupených v členení podľa 5-ročného vekového rozpätia (na zobrazenie ďalších dvoch grafov použite zvislý posuvník):

- **Rozdelenie veku počas celého života** - pre všetkých ľudí s platnými dátumami narodenia a úmrtia.
- **Otec - *Rozdelenie veku dieťaťa*** - zobrazuje vekový rozdiel medzi dieťaťom a otcom, ak majú obe osoby platné dátumy narodenia.
- **Matka - *Child Age Diff Distribution*** - zobrazuje vekový rozdiel medzi dieťaťom a matkou, ak majú obe osoby platné dátumy narodenia.

Po prejdení na riadok grafu sa zobrazí nápoveda s počtom potomkov, ktorí zodpovedajú rozsahu riadku.

Dvojklikom na riadok v ktoromkoľvek z grafov štatistiky sa otvorí rýchla správa o potomkoch zaradených do kategórie podľa tohto riadku. Rýchlu správu môžete zoradiť podľa stĺpcov Meno, Dátum narodenia a Typ mena.

Kliknutím pravým tlačidlom myši na riadok rýchleho prehľadu sa zobrazí kontextová ponuka na kopírovanie zoznamu, otvorenie editora osôb alebo aktiváciu osoby.

#### ⚙ Konfigurovateľné možnosti

![[_media/AgeStats-Gramplet-configuration-tab-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Gramplety vekových štatistík - z predvolených nastavení karty Konfigurácia grafov]] Nastaviteľné limity škálovania grafu

- Maximálny vek 1-150; (*110 predvolené*)
- Maximálny vek matky pri narodení: 1-150; (*40 predvolené*)
- Maximálny vek otca pri narodení: 1-150; (*60 predvolené*)
- Šírka grafu: 1-150; ("'60 predvolené'')

V zobrazení Dashboard View (Ovládací panel) možno gramplety odpojiť kliknutím na tlačidlo .

### Pozri tiež

- Bola vyvinutá aktualizácia pre verziu Grampletu 6.0. Pozrite si [screen capture](wiki::File:AgeStats-Gramplet-detached-51.png#Summary)

{{-}}

## Predkovia

![[_media/Ancestors-Gramplet-detached-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Gramplety predkov - oddelený príklad]]

Gramplet zobrazujúci predkov aktívnej osoby. {{-}}

## Atribúty

![[_media/Attributes-Gramplet-detached-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Atribúty Gramplet]]

Gramplet atribútov zobrazuje všetky atribúty aktuálnej, aktívnej osoby. Dvakrát kliknite na názov atribútu a spustí sa rýchle zobrazenie, ktoré zobrazí všetky osoby, ktoré majú tento atribút, a jeho hodnoty. Rýchle zobrazenie môžete zoradiť podľa hodnoty atribútu kliknutím na názov stĺpca. {{-}} ![[_media/Atttribute-Gramplet-QuickView-example-result-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Atribúty Grampletu - Rýchle zobrazenie výsledku príkladu]]

V Rýchlom zobrazení zvýraznite položku, ktorá má zmeniť aktívnu osobu (čím sa zmení gramoplatňa Atribúty), a dvojklikom na položku Rýchle zobrazenie zobrazte dialógové okno Upraviť osobu. {{-}}

### Atribúty osoby

Pozri [Atribúty](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/sk#Atribúty). {{-}}

### Atribúty rodiny

Pozri [Atribúty](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/sk#Atribúty) {{-}}

### Atribúty udalosti

Pozri [Atribúty](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/sk#Atribúty) {{-}}

### Atribúty zdroja

Pozri [Atribúty](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/sk#Atribúty) {{-}}

### Atribúty citácie

Pozri [Atribúty](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/sk#Atribúty) {{-}}

### Atribúty médií

Pozri [Atribúty](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/sk#Atribúty) {{-}}

## Kalendár

![[_media/CalendarGramplet-detached-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Gramplety kalendára - oddelený príklad]]

Kalendárny gramplet zobrazuje mesačný kalendár. Dvojitým kliknutím na deň spustíte Rýchle zobrazenie.

Pomocou tlačidiel a v ľavom hornom rohu (mesiac) môžete prejsť na predchádzajúci a nasledujúci mesiac.

Pomocou tlačidiel a v pravom hornom rohu (rok) môžete prejsť na predchádzajúci a nasledujúci rok.

V okne Rýchle zobrazenie sa zobrazia **Udalosti** vybraného dňa: Udalosti v tento presný deň a Ďalšie udalosti v tomto mesiaci/deň v histórii, ako aj Ďalšie udalosti v tomto roku.

Informácie sú uvedené v tabuľke, ktorá zobrazuje:

- Dátum
- Typ
- Miesto
- Odkaz

Dátum môžete tiež pretiahnuť do poľa dátumu v gramplete [Vek na dátum](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/sk#Vek_na_dátum) a zadať tento dátum. {{-}}

## Deti

![[_media/ChildrenGramplet-PeopleCategoryView-detached-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Detský gramoplatňák - oddelený príklad]]

Gramplet zobrazujúci deti aktívnych osôb.

[Ako zmením poradie detí?](wiki:Gramps_6.0_Wiki_Manual_-_FAQ/sk#Ako_zmením_poradie_detí.3F) Použite:

- Na zmenu poradia detí v rodine použite kartu Editor rodiny [Deti](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1/sk#Deti).
- Doplnok tretej strany [Birth Order Tool](wiki:Addon:BirthOrderTool), ktorý umožňuje hromadnú aktualizáciu poradia detí.

{{-}}

### Osoba Deti

Pozri [Deti](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/sk#Deti).

Zobrazuje aj manželského partnera dieťaťa, ak je prítomný. {{-}}

### Deti rodiny

Pozri [Deti](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/sk#Deti) {{-}}

## Citácie

![[_media/Citation-Gramplet-detached-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Citačný gramoplat - oddelený príklad]]

Gramplet zobrazujúci citácie aktívnych osôb. {{-}}

### Citácie osôb

Pozri [Citácie](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/sk#Citácie). {{-}}

### Citácie rodín

Pozri [Citácie](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/sk#Citácie) {{-}}

### Citácie udalostí

Pozri [Citácie](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/sk#Citácie) {{-}}

### Citácie miest

Pozri [Citácie](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/sk#Citácie) {{-}}

### Mediálne citácie

Pozri [Citácie](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/sk#Citácie) {{-}}

## Graf potomkov

![[_media/DescendantFan-Gramplet-detached-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Descendentný vejár (graf) Gramplet - oddelený príklad]]

Gramplet zobrazujúci priamych potomkov aktívnej osoby vo forme vejárového grafu.

**Pozri tiež:** } Potomkovia Gramplet - oddelený príklad\]\]

Gramplet Potomkovia zobrazuje priamych potomkov aktívnej osoby.

Poradie manželov a detí je také, aké je uvedené v editore Gramplets. Ak chcete zmeniť poradie manželov, kliknite na *Poradie* v zobrazení Vzťahy. Ak chcete zmeniť poradie detí, [ich potiahnite a pustite](http://en.wikipedia.org/wiki/Drag-and-drop) v správnom poradí v okne Editor rodiny.

Tento gramopríbeh je založený na [Správa o potomkoch](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_6/sk#Správa_o_potomkoch), ktorý je k dispozícii v textových správach.

Gramplety potomkov sa aktualizujú pri zmene aktívnej osoby alebo pri zmene rodokmeňov. Neaktualizuje sa automaticky pri úpravách alebo pridávaní, pretože spustenie tejto správy je časovo náročné.

Minimalizácia grampletu zabráni jeho aktualizácii.

Po prejdení myšou nad osobou sa zobrazí prehľad s nápovedou, ktorý obsahuje dátum úmrtia. {{-}}

## Podrobnosti

![[_media/Details-Gramplet-detached-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Detaily Grampletu - oddelený príklad]]

Gramplet zobrazujúci podrobnosti o aktívnej osobe.

Poskytuje stručný neupraviteľný prehľad vybranej osoby, napríklad:

- *Meno*: osoby
- *Známy aj ako:*
- *Iné meno:*
- *Otec:*
- *Matka:*
- *Narodenie:*
- *Úmrtie:*
- *Pohreb:*

<!-- -->

- *Obrázok*: Ak je k dispozícii, primárny obrázok sa zobrazí napravo od podrobností, v opačnom prípade krížik označí, že obrázok chýba, obrázok môžete dvojklikom otvoriť v externom prehliadači. Ak chcete zmeniť primárny aktívny obrázok, pozrite si: [Editácia osôb - karta Galéria](wiki:Gramps_6.0_Wiki_Manual_-_Vedenie_a_úprava_údajov:_detail_-_časť_1#Galéria)

Jednotlivé textové polia môžete zvýrazniť a skopírovať. {{-}}

### Podrobnosti osoby

Pozri [Podrobnosti](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/sk#Podrobnosti). {{-}}

### Podrobnosti o mieste

Pozri [Podrobnosti](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/sk#Podrobnosti) {{-}}

### Podrobnosti o archíve

Pozri [Podrobnosti](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/sk#Podrobnosti) {{-}}

## Uzatvára

![[_media/Encloses-Gramplet-detached-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Uzatvára gramplety - oddelený príklad]]

Gramplet zobrazujúci umiestnenie miesta, ktoré ohraničuje, v priebehu času. {{-}}

- Pozri tiež [Priložené](wiki:Gramps_6.0_Wiki_Manuál_-_Zadávanie_a_editácia_údajov:_detail_-_časť_2#Priložené_By) záložka

### Obsahuje lokality miesta

Pozri [Enclosed By](wiki:Gramps_6.0_Wiki_Manuál_-_Gramplets#Enclosed_By) {{-}}

## Uzavreté podľa

![[_media/EnclosedBy-Gramplet-detached-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Uzavreté grampletom - oddelený príklad]]

Gramplet zobrazujúci miesta uzavreté miestom v priebehu času. {{-}}

- Pozri tiež [Pripojené by](wiki:Gramps_6.0_Wiki_Manuál_-_Vkladanie_a_úprava_údajov:_detail_-_časť_2#Pripojené_by) záložka

### Uzavreté miesta

Pozri [Encloses](wiki:Gramps_6.0_Wiki_Manuál_-_Gramplets#Encloses). {{-}}

## Udalosti

![[_media/Events-Gramplet-detached-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Udalosti Gramplet - oddelený príklad]]

Gramplet zobrazujúci udalosti pre aktívnu osobu.

Dvojklikom na riadok môžete upraviť udalosť. {{-}}

### Udalosti ľudí

Pozri [Udalosti](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/sk#Udalosti). {{-}}

### Udalosti rodiny

Pozri [Udalosti](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/sk#Udalosti) {{-}}

## Súradnice udalostí

![[_media/EventsCoordinates-Gramplet-detached-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Gramplety súradníc udalostí - oddelený príklad]]

Gramplet zobrazujúci súradnice udalostí pre aktívnu osobu.

Dvojklikom na riadok môžete upraviť udalosť. {{-}}

## Diagram ventilátora

![[_media/FanChart-detached-gramplet-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Ventilátorová schéma Gramplet]]

Gramplet vejárového grafu zobrazuje priamych predkov aktívnej osoby v kruhovom formáte. Je podobný zobrazeniu rodokmeňa, ale zobrazuje sa okolo stredu/aktívnej osoby a ďalšie generácie sa špirálovito rozchádzajú.

Kliknutím na rodiča v grafe sa rozšíri alebo zmenší nad jeho dieťaťom. Kliknutím pravým tlačidlom myši na osobu môžete:

- vybrať túto osobu ako aktívnu osobu
- upraviť osobu, čo umožňuje prostredníctvom Editora osôb pridať deti do rodín osoby
- vybrať spomedzi príbuzných osoby, ktorá má byť aktívnou osobou
- pridať partnerov (rodiny) k osobe
- skopírovať meno, narodenie a úmrtie osoby do schránky

Kliknutím do otvorenej oblasti (nie osoby) a potiahnutím myši môžete tabuľku otáčať okolo stredu. Kliknutím ľavým tlačidlom myši a ťahaním v strede môžete tiež zmeniť polohu vejárovej tabuľky.

Čierny okraj na vonkajšom polomere grafu označuje viac rodičov pre danú osobu. Čierny kruh v strede znamená, že osoba v strede má deti.

Gramplety vejárového grafu sa aktualizujú, keď zmeníte aktívnu osobu alebo zmeníte rodokmeň.

Ak gramplet minimalizujete, zabráni sa jeho aktualizácii.

**Pozri tiež:** {{-}}

## ČASTO KLADENÉ OTÁZKY

![[_media/FAQ-Gramplet-detached-50.png|Obrázok {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Často kladené otázky Gramplet - oddelený príklad]]

Na (často kladené otázky) sa zobrazuje zoznam bežných otázok a odkazy na odpovede na ne z Gramps Wiki (vyžaduje pripojenie na internet).

Tento gramplet zobrazuje ručne zostavený zoznam **Často kladených otázok** s hypertextovými odkazmi na odpovede v článkoch wiki Gramps. Zoznam je zostavený z nových príspevkov používateľov do [Gramps User maillist](wiki:Kontakt#Zasielanie_listov), na ktoré je potrebné opakovane odpovedať.

Zámerom je uľahčiť vyhľadávanie odpovedí na najčastejšie otázky, pričom hlavným cieľom je umožniť novým používateľom rýchlejšie začať používať Gramps.

### Pozri tiež

- Správa o chybe : Odkazy na často kladené otázky na prístrojovej doske sú zastarané (vyriešené)
- Hlásenie chyby : ako pridať/aktualizovať často kladené otázky

{{-}}

## Filter

Gramplet poskytuje filter špecifický pre kategóriu.

Pozri tiež [Ktoré filtre v ktorej kategórii?](wiki:Gramps_6.0_Wiki_Manual_-_Filters/sk#Ktoré_filtre_v_ktorej_kategórii.3F) {{-}}

### Filter osôb

![[_media/FilterGramplet-Person-detached-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Osoba - Filter Gramplet - odpojený - predvolený]]

Pozri [Filter](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/sk#Filter). {{-}}

### Filter rodiny

![[_media/FilterGramplet-Family-detached-default-60.png|Fig. {{#var:chapter}}.{{#vardefinition:figure|{{#expr:{{#var:figure}}+1}}}} Rodina - Filter Gramplet - odpojený - predvolený]]

Pozri [Filter](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/sk#Filter). {{-}}

### Filter udalostí

![[_media/FilterGramplet-Event-detached-default-60.png|Obrázok {{#var:kapitola}}.{{#vardefineecho:obrázok|{{#expr:{{#var:obrázok}}+1}}}} Udalosť - Filter Gramplet - detached - default]]

Pozri [Filter](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/sk#Filter). {{-}}

### Filter miesta

![[_media/FilterGramplet-Place-detached-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Miesto - Filter Gramplet - odpojený - predvolený]]

Pozri [Filter](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/sk#Filter). {{-}}

### Filter zdrojov

![[_media/FilterGramplet-Source-detached-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Zdroj - Filter Gramplet - odpojený - predvolený]]

Pozri [Filter](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/sk#Filter). {{-}}

### Citačný filter

![[_media/FilterGramplet-Citation-detached-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Citácia - Filter Gramplet - odpojený - predvolený]]

Pozri [Filter](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/sk#Filter). {{-}}

### Filter archívu

![[_media/FilterGramplet-Repository-detached-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Archív - Filter Gramplet - odpojený - predvolený]]

Pozri [Filter](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/sk#Filter). {{-}}

### Filter médií

![[_media/FilterGramplet-Media-detached-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Médiá - Filter Gramplet - odpojený - predvolený]]

Pozri [Filter](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/sk#Filter) {{-}}

### Filter poznámok

![[_media/FilterGramplet-Notes-detached-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Poznámky - Filter Gramplet - odpojený - predvolený]]

Pozri [Filter](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/sk#Filter). {{-}}

## Galéria

![[_media/Gallery-Gramplet-detached-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Galéria Gramplet - oddelený príklad]]

Gramplet zobrazujúci mediálne objekty. Na prvom obrázku je primárny aktívny mediálny objekt, ktorý sa používa v správach a v dialógovom okne Upraviť osobu.

Pozri tiež [Galéria](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1/sk#Galéria) záložka , kde môžete zmeniť, ktorý obrázok je primárnym aktívnym mediálnym objektom pre správy atď... {{-}}

### Galéria osôb

Pozri [Galéria](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/sk#Galéria). {{-}}

### Rodinná galéria

Pozri [Galéria](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/sk#Galéria) {{-}}

### Galéria udalostí

Pozri [Galéria](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/sk#Galéria) {{-}}

### Galéria miest

Pozri [Galéria](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/sk#Galéria) {{-}}

### Galéria zdrojov

Pozri [Galéria](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/sk#Galéria) {{-}}

### Galéria citácií

Pozri [Galéria](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/sk#Galéria). {{-}}

## Meno Cloud

![[_media/GivenNameCloud-Gramplet-detached-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Dané meno Oblak Gramplet - oddelený príklad]]

Podobne ako [Prízvisko Cloud Gramplet](#Prízvisko_Cloud), aj Given Name Cloud Gramplet zobrazuje najpopulárnejšie krstné mená vo vašom rodokmeni. Veľkosť mena udáva, aké je populárne. Prejdite myšou na meno, aby ste videli presný počet a percento ľudí v rodokmeni, ktorí majú toto meno.

Gramplet rozdeľuje krstné mená na slová (rozdelené medzerami). Napríklad "Sarah Elizabeth" by sa zobrazilo pod slovami "Sarah" aj "Elizabeth".

Dvojitým kliknutím na dané meno sa zobrazí rýchle zobrazenie všetkých zodpovedajúcich osôb. {{-}}

## Metadáta obrázkov

![[_media/ImageMetadata-Gramplet-detached-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Gramplety metadát obrázkov - príklad]]

Program Image Metadata Gramplet ponúka rozhranie na zobrazenie [Image Exif Metadata](https://en.wikipedia.org/wiki/Exchangeable_image_file_format) z vašich obrázkov (\*.jpg, \*.png. \*.tiff, \*.exv, \*.nef, \*.psd, \*.pgf). {{-}} Pozrite si tiež tretiu stranu:

- [Upraviť metadáta Exif obrázkov](wiki:Upraviť_metadáta_Exif_obrázkov) addon

### Predpoklady

Po nainštalovaní gexiv2 si pozrite vyššie pokyny na stiahnutie a inštaláciu tohto doplnku...

Pyexiv2 môžete používať aj z rozhrania príkazového riadka (cli) a zo skriptu jazyka Python:

1.  importovať knižnicu pyexiv2
      
    from pyexiv2 import ImageMetadata, ExifTag
2.  zadajte svoj obrázok
      
    image = ImageMetadata("/home/user/image.jpg")
3.  načítajte obrázok
      
    image.read()

Referenčné značky metadát Exif, IPTC, XMP nájdete [tu](http://www.exiv2.org/metadata.html).

Príklad:

1.  Umelec

  
Smith and Johnson's Photography Studio

<!-- -->

  
image\["Exif.Image.DateTime"\] \# DateTime

1826 Apr 12 14:00:00

<!-- -->

  
image\["Exif.Image.DateTime"\] = datetime.datetime.now() \# Pridať DateTime

<!-- -->

  
image.write() \# zapísať metaúdaje

### Scenár použitia

Uprednostňovaný spôsob použitia tohto doplnku je:

1.  nainštalovať pyexiv2
2.  Nainštalujte tento doplnok
3.  Reštartujte program Gramps
4.  Kliknite na položku Pohľady na paneli s ponukou a vyberte položku Zobrazenia médií
5.  Otvorte bočný panel
6.  Posuňte dostupné prázdne pravé zobrazenie približne na polovicu obrazovky.
7.  Kliknite pravým tlačidlom myši na text na karte Postranný panel a vyberte položku Pridať gramoplatňu
8.  Vyberte Gramplet s metaúdajmi o obrázku
9.  Vyberte obrázok z ľavého MediaView

{{-}}

## Náhľad média

![[_media/MediaPreview-Gramplet-detached-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Mediálny náhľad Gramplet - odpojený príklad]]

Gramplet zobrazuje náhľad jedného mediálneho objektu. {{-}} Pozrite si [Kategória médií](wiki:Gramps_6.0_Wiki_Manual_-_Categories#Media_Category)

## Poznámky

![[_media/Notes-Gramplet-detached-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Poznámky Gramplet - oddelený príklad]]

Gramplet zobrazujúci poznámky aktívnych osôb.

Pozri tiež: 1: Poznámky: \* [Note Gramplet](wiki:Addon:NoteGramplet) - doplnok tretej strany {{-}}

### Poznámky osôb

Pozri [Poznámky](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/sk#Poznámky). {{-}}

### Poznámky k rodine

Pozri [Poznámky](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/sk#Poznámky) {{-}}

### Poznámky k udalostiam

Pozri [Poznámky](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/sk#Poznámky) {{-}}

### Poznámky k miestam

Pozri [Poznámky](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/sk#Poznámky) {{-}}

### Poznámky k zdrojom

Pozri [Poznámky](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/sk#Poznámky) {{-}}

### Poznámky k citáciám

Pozri [Poznámky](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/sk#Poznámky). {{-}}

### Poznámky k archívu

Pozri [Poznámky](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/sk#Poznámky). {{-}}

### Poznámky k médiám

Pozri [Poznámky](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/sk#Poznámky). {{-}}

## Rodokmeň

![[_media/Pedigree-Gramplet-detached-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Rodokmeň Gramplet - oddelený príklad]]

Rodokmeňový gramplet zobrazuje komprimovaný pohľad na priamych predkov aktívnej osoby. V predvolenom nastavení sa vracia o 100 generácií späť. Kliknutím na mená môžete zmeniť aktívnu osobu, kliknutím pravým tlačidlom myši môžete osobu upraviť. V spodnej časti grampletu je uvedený počet osôb na generáciu. Dátumy narodenia a úmrtia sa zobrazujú vedľa mena každej osoby. Dvojitým kliknutím na číslo generácie zobrazíte zodpovedajúce osoby.

Používanie obsahu rodokmeňa v inom programe si vyžaduje trochu námahy Otvorte kontextovú kontextovú ponuku kliknutím pravým tlačidlom myši kdekoľvek v gramplete okrem odkazu. Alebo môžete začať výber ťahaním z tých istých inertných oblastí. Z tej istej kontextovej ponuky skopírujte zvýraznený text schránku operačného systému. (Väzba klávesov pre "Kopírovať" nebude fungovať.) Pri vkladaní textu do iného programu na úpravu textu môže byť potrebné zmeniť písmo na neproporcionálne písmo, aby sa zachovalo odsadenie. Niektoré online služby pri odosielaní časti textu zrážajú úvodné medzery. Zachovanie odsadenia pre takéto služby môže vyžadovať nahradenie zdvojených medzier zdvojenými zástupnými znakmi... ako sú bodky/úplné bodky.

#### ⚙ Konfigurovateľné možnosti

- Maximálne generácie: 1 až 100 limit; (*100*)
- Zobraziť dátumy zaškrtávacie políčko; (*odznačené*)
- Ponuka typu riadku: <abbr title="Unicode Transformation Format graphical symbols">UTF</abbr>, <abbr title="American Standard Code for Information Interchange text symbols">ASCII</abbr>; (*UTF*)

## Rýchly pohľad

![[_media/QuickView-Gramplet-Configuration-tab-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Rýchly pohľad grampletu - odpojený príklad]]

Gramplet Rýchly pohľad umožňuje spustiť rýchle zobrazenie, aktualizuje sa pri prechode od osoby k osobe. (Keď bol tento gramplet zavedený, podporoval iba spúšťanie Rýchlych pohľadov z kategórie Ľudia. Teraz sú podporované aj iné kategórie.)

Pre osobu môžete spustiť ktorýkoľvek z [Rýchlych pohľadov](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_8/sk#Rýchle_pohľady). {{-}} ![[_media/QuickView-Gramplet-detached-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Rýchly pohľad grampletu - zobrazená karta konfigurácie]]

Možnosti môžete zmeniť kliknutím na tlačidlo Option (ľavé horné tlačidlo Grampletu), čím sa Gramplet odpojí a zobrazí sa okno. V hornom riadku vyberte a zobrazí sa zoznam možností. Stlačením tlačidla aplikujte zmeny do rýchleho zobrazenia. Potom môžete okno zatvoriť a znovu pripojiť gramoplatňu.

{{-}} Ak máte záujem o vytvorenie vlastného, pozrite si nasledujúce informácie pre vývojárov:

- [Vytváranie vlastného Rýchleho_pohľadu](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_8#Vytváranie_vlastného_Rýchleho_pohľadu).

{{-}}

## Záznamy

![[_media/Records-Gramplet-detached-50.png|Fig {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Záznamy Gramplet - odpojený príklad]]

Gramplet záznamov zobrazuje množstvo zaujímavých faktov o záznamoch (väčšinou týkajúcich sa veku) z vašej databázy. V zozname sú uvedené tri najdôležitejšie pre každý prvok.

- Záznamy o osobách:
  - Najmladšia žijúca osoba
  - Najstaršia žijúca osoba
  - Osoba zomrela v najmladšom veku
  - Osoba zomrela v najstaršom veku
  - Osoba, ktorá uzavrela manželstvo v najmladšom veku
  - Osoba, ktorá uzavrela manželstvo v najstaršom veku
  - Osoba rozvedená v najmladšom veku
  - Osoba rozvedená v najstaršom veku
  - Najmladší otec
  - Najmladšia matka
  - Najstarší otec
  - Najstaršia matka
- Rodinné záznamy
  - Pár s najväčším počtom detí
  - Žijúci pár, ktorý sa zosobášil naposledy
  - Žijúci pár, ktorý sa zosobášil dávnejšie
  - Najkratšie minulé manželstvo
  - Najdlhšie manželstvo v minulosti

{{-}} Zoznam je zaujímavý nielen sám o sebe, ale je aj dobrou kontrolou správnosti údajov. Pri niektorých položkách je potrebné doplniť ďalšie informácie.

Nasledujúci príklad ukazuje, že došlo k sobášu (teda k výpočtu posunu), ale žiadna z osôb nemala udalosť úmrtia. Aj keď dátum nie je známy, stačí zadať udalosť úmrtia jedného z partnerov a zoznam sa opraví.

*'Žijúci pár, ktorý sa zosobášil pred najväčšou dobou*

1.  van Dosselaere, Egidius a Rechters, Petronella (382 rokov, 1 mesiac)
2.  de Richter, Petrus a Asscericx, Catharina (379 rokov, 9 mesiacov)

{{-}}

K dispozícii je aj identická [Records Report](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_6#Records_Report).

## Odkazy

![[_media/References-Gramplet-detached-50.png|Fig {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Odkazy Gramplet - oddelený príklad]] Gramplet zobrazujúci aktívne osoby Odkazy.

{{-}}

### Osobné odkazy

- Referencie osôb : Gramplet zobrazujúci spätné odkazy na osobu

Pozri [Odkazy](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/sk#Odkazy). {{-}}

### Rodinné odkazy

- Rodinné odkazy : Gramplet zobrazujúci spätné odkazy na rodinu

Pozri [Odkazy](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/sk#Odkazy). {{-}}

### Odkazy na udalosti

- Odkazy na udalosti : Gramplet zobrazujúci spätné odkazy na udalosť

Pozri [Odkazy](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/sk#Odkazy). {{-}}

### Odkazy na miesta

- Odkazy na miesta : Gramplet zobrazujúci spätné odkazy na miesto

Pozri [Odkazy](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/sk#Odkazy). {{-}}

### Odkazy na zdroje

- Zdrojové odkazy : Gramplet zobrazujúci spätné odkazy na zdroj

Pozri [Odkazy](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/sk#Odkazy). {{-}}

### Odkazy na citácie

- Odkazy na citácie : Gramplet zobrazujúci spätné odkazy na citáciu

Pozri [Odkazy](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/sk#Odkazy). {{-}}

### Odkazy na archív

- Odkazy na úložisko : Gramplet zobrazujúci spätné odkazy na archív

Pozri [Odkazy](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/sk#Odkazy). {{-}}

### Odkazy na médiá

- Odkazy na médiá : Gramplet zobrazujúci spätné odkazy na objekt médií

Pozri [Odkazy](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/sk#Odkazy). {{-}}

### Odkazy na poznámky

- Odkazy na poznámky : Gramplet zobrazujúci spätné odkazy na poznámku

Pozri [Odkazy](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/sk#Odkazy). {{-}}

## Príbuzní

![[_media/Relatives-Gramplet-detached-example-60.png|Fig {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Gramplety príbuzných - oddelený príklad]]

Tento gramplet zobrazuje všetkých priamych príbuzných aktívnej osoby. Je určený ako navigačná pomôcka, alternatívny spôsob pohybu v rodokmeni v programe Gramps . Ak odpojíte Gramplet a umiestnite ho vedľa Gramps, umožní vám to ľahko zmeniť obsah aktuálneho "zobrazenia osoby".

Ak pracujete v zobrazení rodokmeňa v kategórii diagramov, aktívna osoba je osoba, ktorá sa nachádza najviac vľavo. Kliknutím na meno v Gramplete príbuzných môžete ľahko zmeniť aktívnu osobu a všetky zobrazenia osôb v druhom okne sa aktualizujú. Keďže v okne Gramplet príbuzných sa zobrazujú všetci manželia, všetky deti a všetci rodičia, ponúka to alternatívny spôsob navigácie v údajoch.

Mená v tomto Gramplete umožňujú aj priame vyvolanie editora osôb kliknutím pravým tlačidlom myši na ktorékoľvek z mien.

Gramplet Príbuzní je možné pridať do nasledujúcich kategórií:

- Kategória Ľudia
- Kategória Vzťahy
- Kategória grafy
- Kategória Geografia (len vybrané zobrazenia)

{{-}}

## Sídlo

![[_media/ResidenceGramplet-Person-detached-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Osoba - bydlisko Gramplet - oddelený - príklad]]

Gramplet zobrazujúci udalosti pobytu pre aktívnu osobu {{-}}

### Pobyt osoby

Pozri [Residence](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Residence) {{-}}

## Protokol relácie

![[_media/SessionLog-Gramplet-detached-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Gramplety denníka relácií - odpojený príklad]]

Protokol relácie sleduje aktivity v tejto relácii. Obsahuje zoznam vybraných a upravených objektov.

Jedenkrát kliknite na meno, aby sa táto osoba stala aktívnou osobou. Dvojitým kliknutím na meno alebo rodinu sa zobrazí stránka pre tento objekt. Okrem toho, ak chcete upraviť osobu, ale nechcete zmeniť aktívnu osobu, môžete kliknúť pravým tlačidlom myši na meno osoby.

Tento gramplet je praktický, pretože môžete veľmi rýchlo zmeniť aktívnu osobu alebo upraviť objekt zo zoznamu relácií. {{-}}

## SoundEx

![[_media/SoundEx-Gramplet-detached-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} SoundEx Gramplet - oddelený príklad]]

Tento Gramplet generuje kódy SoundEx pre mená osôb v databáze.

V okne si môžete vybrať z kontextovej ponuky zobrazenej výberom tlačidla šípky nadol, (trojuholník) alebo môžete meno zadať do textového poľa.

Zadané meno môže byť ľubovoľné... dokonca aj meno, ktoré sa nenachádza vo vašom rodokmeni.

Výsledok sa zobrazí automaticky, napr.: Kód SoundEx pre *Simpson* je *S512*

K dispozícii je tlačidlo , ktoré vás prenesie na túto stránku. Tlačidlom (alebo pomocou klávesovej skratky ) zrušíte okno . {{-}}

#### Soundex čo je to?

Soundex je najznámejší zo všetkých [algoritmov](http://en.wikipedia.org/wiki/Phonetic_algorithmfonetických), ktoré umožňujú indexovanie slov podľa ich zvuku, ako sa vyslovujú v angličtine.

Ekvivalentom Soundexu je kódovaný index priezvisk (priezvisk) založený na tom, ako priezvisko znie, a nie na tom, ako sa píše. Priezviská, ktoré znejú rovnako, ale píšu sa inak, ako napríklad SMITH a SMYTH, majú rovnaký kód a sú uložené spolu. Systém kódovania Soundex bol vyvinutý tak, aby sa priezviská dali nájsť aj vtedy, keď sú zapísané pod rôznymi pravopisnými variantmi.

Soundex sa prvýkrát použil pri sčítaní ľudu v USA v roku 1880 a je to "zvukový index", nie striktne abecedný. Kľúčovou vlastnosťou je, že kóduje priezviská na základe toho, ako meno znie, a nie na základe toho, ako sa píše. Systém fonetického kódovania Soundex vznikol ešte pred počítačmi a mal pomôcť výskumníkom rýchlo nájsť priezvisko, aj keď sa mohlo prepisovať rôznymi spôsobmi.

Tí, ktorí vykonávajú vyhľadávanie v súpisoch, musia používať rovnakú metódu kódovania a tabuľkového spracovania priezvisk, ako to robili pracovníci sčítania ľudu pri vytváraní databázy.

Ak chcete vyhľadať konkrétne priezvisko, musíte najprv zistiť jeho kódový ekvivalent.

- **Základné pravidlo kódovania Soundexu:**

Každý kód Soundexu sa skladá z písmena a troch číslic, napríklad W-252. Písmeno je vždy prvé písmeno priezviska. Čísla sa priraďujú k zvyšným písmenám priezviska podľa nižšie uvedenej príručky Soundex. Ak je to potrebné, na konci sa pridajú nuly, aby vznikol štvormiestny kód. Ďalšie písmená sa neberú do úvahy. Príklady: Washington je kódovaný ako W-252 (W, 2 pre S, 5 pre N, 2 pre G, zvyšné písmená sa neberú do úvahy). Lee je kódovaný L-000 (L, pridané 000).

| Číslo | Predstavuje písmená    |
|-------|------------------------|
| 1     | B, F, P, V             |
| 2     | C, G, J, K, Q, S, X, Z |
| 3     | D, T                   |
| 4     | L                      |
| 5     | M, N                   |
| 6     | R                      |

Neberte do úvahy písmená A, E, I, O, U, H, W a Y.

- **Ďalšie pravidlá kódovania Soundexu:**
  - Mená s dvojitými písmenami: Ak má priezvisko dvojité písmená, malo by sa považovať za jedno písmeno. Napríklad:
    - Gutierrez sa kóduje ako G-362 (G, 3 pre T, 6 pre prvé R, druhé R sa ignoruje, 2 pre Z).
  - Mená s písmenami vedľa seba, ktoré majú rovnaké číslo kódu Soundex: Ak má priezvisko vedľa seba rôzne písmená, ktoré majú rovnaké číslo v príručke kódovania Soundex, mali by sa považovať za jedno písmeno. Príklady:
    - Pfister sa kóduje ako P-236 (P, F sa ignoruje, 2 pre S, 3 pre T, 6 pre R).
    - Jackson sa kóduje ako J-250 (J, 2 pre C, K sa ignoruje, S sa ignoruje, 5 pre N, pridaná 0).
    - Tymczak je kódovaný ako T-522 (T, 5 pre M, 2 pre C, Z sa ignoruje, 2 pre K). Keďže samohláska "A" oddeľuje Z a K, kóduje sa K.
  - Názvy s predponami: Ak má priezvisko predponu, napríklad Van, Con, De, Di, La alebo Le, kódujte s predponou aj bez nej, pretože priezvisko môže byť uvedené pod oboma kódmi. Všimnite si však, že Mc a Mac sa nepovažujú za predpony. napríklad priezvisko VanDeusen sa môže kódovať dvoma spôsobmi: V-532 (V, 5 pre N, 3 pre D, 2 pre S) alebo D-250 (D, 2 pre S, 5 pre N, 0 pridané).
  - Oddeľovače spoluhlások: Ak samohláska (A, E, I, O, U) oddeľuje dve spoluhlásky, ktoré majú rovnaký kód Soundexu, kóduje sa spoluhláska napravo od samohlásky. Príklad: Tymczak sa kóduje ako T-522 (T, 5 pre M, 2 pre C, Z sa ignoruje (pozri pravidlo "Side-by-Side" vyššie), 2 pre K). Keďže samohláska "A" oddeľuje Z a K, kóduje sa K. Ak "H" alebo "W" oddeľuje dve spoluhlásky, ktoré majú rovnaký kód Soundexu, spoluhláska napravo od samohlásky sa nekóduje. Príklad: Ashcraft má kód A-261 (A, 2 pre S, C sa ignoruje, 6 pre R, 1 pre F). Nie je kódované ako A-226.

Viac informácií o systéme indexovania Soundex nájdete na stránke [NARA Soundex Indexing page](http://www.archives.gov/research/census/soundex.html). {{-}}

## Štatistika

![[_media/Statistics-Gramplet-detached-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Štatistika Gramplet - oddelený príklad]]

Štatistický gramplet spúšťa štatistickú správu. Dvojitým kliknutím na výrazy sa zobrazia zodpovedajúce položky.

V tomto gramplete sú vám poskytnuté nasledujúce informácie:

- **Jednotlivci**
  - Počet jednotlivcov
  - Muži
  - Ženy
  - Osoby s neznámym pohlavím
  - Neúplné mená
  - Individuálne osoby s chýbajúcimi dátumami narodenia
  - Osoby bez spojenia
- **Rodinné informácie**
  - Počet rodín
  - Jedinečné priezviská
- **Mediálne objekty**
  - Individuálne osoby s mediálnymi objektmi
  - Celkový počet odkazov na mediálne objekty
  - Počet jedinečných mediálnych objektov
  - Celková veľkosť mediálnych objektov
  - Chýbajúce mediálne objekty

Ako pri všetkých Grampletoch, ak kliknete na ľavé tlačidlo , odpojíte okno a ak pridáte osoby do rodokmeňa, uvidíte, že počet osôb sa dynamicky mení.

Informácie uvedené v tomto gramplete sú rovnaké ako v [Súhrnná správa databázy](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_6#Database_Summary_Report). {{-}}

## Mrak priezvisk

![[_media/SurnameCloud-Gramplet-detached-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Priezvisko Cloud Gramplet - oddelený príklad]]

Oblak priezvisk Gramplet zobrazuje 100 najpoužívanejších (štandardne) priezvisk. Veľkosť písma mena je úmerná množstvu ľudí s rovnakým menom.

Dvojitým kliknutím na priezvisko spustíte . Otvorí sa okno , v ktorom môžete nájsť všetkých ľudí so zhodným alebo alternatívnym menom. Uvedie sa osoba, dátum narodenia a typ mena.

Ak myšou prejdete nad meno, zobrazí sa percento výskytu a celkový počet. {{-}} ![[_media/SurnameCloud-Gramplet-Configuration-tab-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Prímeno Cloud Gramplet - zobrazená konfiguračná karta]]

Počet zobrazených mien môžete zmeniť konfiguráciou zobrazenia tohto grampletu. {{-}}

## To Do

![[_media/ToDo-Gramplet-detached-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} To Do Gramplet - detašovaný príklad]]

**To Do Gramplet** zobrazuje voľnú textovú oblasť, v ktorej sa zobrazuje obsah objektov typu Poznámka "To Do".

Túto oblasť môžete použiť na vloženie niekoľkých poznámok, poznámok, vecí, ktoré by ste mali na začatie výskumu. Existuje niekoľko ďalších programov To Do (napr. Tomboy e.a.), ale tieto Gramplety sú užitočné, pretože informácie zostávajú v databáze Gramps.

Program To Do Gramplets umožňuje vytvárať poznámky a pripájať ich k objektom programu Gramps. Napríklad môžete pridať Gramplety To Do k bočnému panelu v zobrazení Person (Osoba). Poznámky pridané pomocou tohto grampletu budú pripojené k aktuálne aktívnej osobe. Pre každý typ primárneho objektu Gramps existuje Gramplet To Do (To Do). {{-}} Pozrite si tiež experimentálny [Doplnok tretej strany](wiki:Doplnky_tretích_strán):

- ToDoNotesGramplet\|ToDo Notes Gramplet\]\] dostupný pre Dashboard, ktorý obsahuje zoznam všetkých poznámok To Do v databáze spolu s objektom, ku ktorému sú pripojené.

{{-}}

### Osoba To Do

Pozri [To Do](wiki:Gramps_6.0_Wiki_Manuál_-_Gramplety#To_Do). {{-}}

### Rodina To Do

Pozri [To Do](wiki:Gramps_6.0_Wiki_Manuál_-_Gramplets#To_Do) {{-}}

### Udalosť, ktorú treba urobiť

Pozri [To Do](wiki:Gramps_6.0_Wiki_Manuál_-_Gramplets#To_Do) {{-}}

### Miesto, ktoré treba urobiť

Pozri [To Do](wiki:Gramps_6.0_Wiki_Manuál_-_Gramplets#To_Do) {{-}}

### Zdroj na robenie

Pozri [To Do](wiki:Gramps_6.0_Wiki_Manuál_-_Gramplets#To_Do) {{-}}

### Citácia To Do

Pozri [To Do](wiki:Gramps_6.0_Wiki_Manuál_-_Gramplets#To_Do). {{-}}

### Úložisko To Do

Pozri [To Do](wiki:Gramps_6.0_Wiki_Manuál_-_Gramplets#To_Do) {{-}}

### Médiá, ktoré treba urobiť

Pozri [To Do](wiki:Gramps_6.0_Wiki_Manuál_-_Gramplets#To_Do) {{-}}

## Top priezviská

![[_media/TopSurnames-Gramplet-detached-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Top priezviská Gramplet - odtrhnutý príklad]]

Gramplet Top Surnames zobrazuje 10 najpoužívanejších (štandardne) priezvisk.

Desiatka najčastejšie používaných priezvisk je prezentovaná nasledovne:

- Prízvisko
- percentuálny podiel
- výskytov

V zozname sa uvádza aj Celkový počet jedinečných priezvisk v databáze, ako aj celkový počet osôb vo vašej databáze.

Dvojitým kliknutím na priezvisko spustíte . Otvorí sa okno , v ktorom sú uvedené osoby s priezviskom, na ktoré ste dvakrát klikli.

Zobrazí sa tabuľka, v ktorej sú uvedení všetci ľudia so zhodným menom alebo alternatívnym menom. Je uvedené meno osoby, ID, dátum narodenia a typ mena. {{-}}

Pokročilé:

- Zmeňte počet zobrazených mien úpravou tejto časti v `~/.gramps/gramps50/gramplets.ini`

{{-}}

## Nezbierané objekty

![[_media/UncollectedObjects-Gramplet-detached-example-60.png|Fig {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Nezbierané objekty Gramplet - oddelený príklad]]

Gramplet je určený na zoznam nízkoúrovňových objektov jazyka Python, ktoré zostávajú v pamäti a nedajú sa (jednoducho) automaticky odstrániť, keď sa už nepoužívajú. Vývojári sa pomocou neho snažia identifikovať zdroj "únikov" pamäte, ktoré spôsobujú, že Gramplet neustále využíva viac a viac pamäte, čím dlhšie sa používa.

Keďže sa nástroj snaží zobraziť objekty, ktoré sa možno ešte stále odstraňujú, má niekedy problémy. {{-}}

## Vitajte

![[_media/Welcome-to-Gramps-Gramplet-detached-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Vitajte Gramplet - oddelený príklad]]

**Vitajte v Gramplete!** Gramplet poskytuje úvodnú správu novým používateľom a niekoľko základných pokynov.

Uvítacia správa opisuje, čo je Gramps, že program je softvér s otvoreným zdrojovým kódom a ako si založiť [Rodinný strom](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees). {{-}}

## Čo ďalej

![[_media/WhatsNext-Gramplet-detached-50.png|Fig. {{#var:chapter}}.{{#var:figure}}+1}}}} Čo bude nasledovať? Gramplet - oddelený príklad]]

Gramplet Čo ďalej zobrazuje zoznam "najnaliehavejších" informačných medzier vo vašom rodokmeni. Je založený na nasledujúcich predpokladoch:

- Chcete poznať meno a priezvisko, dátum a miesto narodenia a dátum a miesto úmrtia každej osoby.
- Chcete poznať otca, matku, dátum a miesto sobáša a - ak ste rozvedení - dátum a miesto rozvodu každej rodiny so zosobášenými rodičmi
- Chcete poznať aspoň matku každej rodiny so slobodnými rodičmi
- Čím bližší je príbuzenský vzťah k hlavnej osobe, tým "naliehavejšia" je informačná medzera.
- Čím bližší je spoločný predok od hlavnej osoby, tým "naliehavejšia" je informácia (napr. synovci sa považujú za "naliehavejšie" ako strýkovia, hoci obaja majú vzdialenosť 3 generácie, pretože v prípade synovcov je spoločným predkom otec/matka, zatiaľ čo v prípade strýkov je spoločným predkom starý otec/babka)
- Údaje o manželstve a osobné údaje manžela/manželky sú o niečo menej "naliehavé" ako osobné údaje priamo príbuznej osoby
- Poloviční súrodenci sú menej "naliehaví" ako súrodenci

Text z vnútra tohto grampletu môžete skopírovať tak, že ho vyberiete a vložíte do prázdneho dokumentu. {{-}} ![[_media/WhatsNext-Gramplet-Configuration-tab-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Čo bude nasledovať? Gramplet - zobrazená karta Konfigurácia]]

Gramplet môže ignorovať predtým overené udalosti pomocou niektorých vlastných značiek. Tagy sa vyberajú v konfigurácii Grampletu. Môžete napríklad označiť nasledujúce udalosti, ktoré sa majú ignorovať:

- že osoba je kompletná
- že rodina je úplná
- že osoba alebo rodina sa má ignorovať pri skracovaní zoznamov

{{-}}

[Category:Sk:Documentation](wiki:Category:Sk:Documentation)
