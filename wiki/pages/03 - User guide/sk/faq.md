---
title: Gramps 6.0 Wiki Manual - FAQ/sk
categories:
- Sk:Documentation
- Stub
managed: false
source: wiki-scrape
wiki_revid: 111297
wiki_fetched_at: '2026-05-30T20:05:42Z'
lang: sk
---

{{#vardefine:chapter\|A}} {{#vardefine:figure\|0}} Táto príloha obsahuje zoznam **Často kladených otázok** (FAQ), ktoré sa opakovane objavujú v poštových konferenciách a na diskusných fórach.

Tento zoznam nie je v žiadnom prípade úplný. Ak by ste chceli do tohto zoznamu pridať otázky/odpovede, prosím [pripojte sa](wiki:Kontakt#Mailing_lists) a pošlite svoje návrhy na adresu `gramps-devel@lists.sourceforge.net` mailing listu.

Zvážte tiež možnosť pozrieť si nasledujúce Kategórie na wiki Gramps: \]\]: \*[How do I...](wiki:[:Category:How_do_I...)

- [Návody na gramce](wiki::Kategória:Návody)

Možno vám bude užitočné prezrieť si

- [[:Slovník Gramps](wiki:[:Slovník_Gramps) - poskytuje prehľad pojmov, ktoré sa vyskytujú v programe Gramps
- [:Genealogický slovník](wiki::Genealogický_slovník) - genealogické termíny a ich významy.

## Všeobecne

### Čo je Gramps?

Gramps je programový systém pre správu genealogického výskumu a analýzy. Inými slovami, je to osobný genealogický program, ktorý vám umožňuje ukladať, upravovať a skúmať genealogické údaje pomocou výkonu vášho počítača, pozri [O programe](wiki:Gramps:O_programe).

=== Kde ho získam a koľko stojí? Program Gramps je možné [inštalovať](wiki:Inštalácia) bezplatne. Gramps je projekt s otvoreným zdrojovým kódom, na ktorý sa vzťahuje všeobecná verejná licencia GNU. Máte úplný prístup k zdrojovému kódu a môžete program a zdrojový kód voľne šíriť.

### Musím sa zaregistrovať ako používateľ, aby som mohol používať program Gramps, nie som programátor?

Nie, registrácia je potrebná len vtedy, ak chcete podať hlásenie o chybe (alebo požiadavku na funkciu) alebo upraviť/napísať stránku wiki.

Na to nie sú potrebné žiadne programátorské zručnosti.

=== Existuje Gramps aj v iných jazykoch? Áno, pri vydaní verzie 6.0 bol Gramps preložený do 28 jazykov, pozrite si [Preklady Gramps](wiki:Preklady_Gramps).

### Ako uchovávam zálohy?

Automatické zálohovanie je predvolená funkcia, ktorá chráni vaše genealogické údaje v programe Gramps. (Automatickou sa stala v roku 2018 s vydaním verzie 6.0.) Interval, cesta k záložnému súboru a možnosť zálohovania pri ukončení nastavení programu Gramps sa nachádzajú na karte v ponuke . Okrem toho je možné zálohu vybrať ručne v okne .

Je mimoriadne dôležité uchovávať zálohy svojich údajov a uchovávať ich na bezpečnom mieste. Program Gramps má špecifický prenosný formát súborov, ktorý je malý a čitateľný pre človeka, označený <kód>.gramps</kód>. Pozri časť "[zálohovanie rodinného stromu](wiki:Gramps_6.0_Wiki_Manuál_-_Správa_rodinných_stromov#Zálohovanie_rodinného_stromu)" v príručke. Je tiež dôležité uvedomiť si, [čo sa zo zálohy programu Gramps vynecháva](wiki:Šablóna:Zálohovanie_Oprávnenia).

Tento záložný súbor môžete z času na čas skopírovať na bezpečné miesto (napr. na USB kľúč). \[Poznámka: Súbory `.gramps` sú v predvolenom nastavení komprimované. Kliknutím na ne sa otvorí súbor Gramps. Ak chcete zobraziť XML, vyberte súbor `.gramps` a otvorte ho pomocou dekompresného nástroja (napr. ark, gunzip, 7-zip), po ktorom môžete extrahovať textový súbor XML, ktorý je čitateľný pre človeka, pozri [details](wiki:Generate_XML#How_do_I_uncompress_the_file?).

Program Gramps vykonáva rýchlu skrytú binárnu zálohu, ktorá umožňuje obnovu v prípade zistenia chyby. Ak je nainštalovaný správny balík, môžete použiť systém revízií.

Ďalšou metódou je zálohovanie skrytého adresára *`/.gramps`*. Tento podadresár sa nachádza vo vašom [adresári používateľa](wiki:Gramps_6.0_Wiki_Manual_-_User_Directory/sk). Zálohovaním tohto adresára sa zálohujú vaše databázy a revízie. (V systéme Windows 10 je to *`/Users/`<vaše užívateľské meno>`/AppData/Roaming/gramy`*)

**Neuchovávajte zálohy vo formáte GEDCOM**. Nie všetky informácie, ktoré program Gramps uchováva, sa dajú zapísať do formátu GEDCOM. Preto operácia exportu/importu z programu Gramps vyexportovaného do formátu GEDCOM a opätovne importovaného do programu Gramps bude znamenať, že **stratíte** [údaje](wiki:Gramps_a_GEDCOM). Na zálohovanie používajte formát súboru `.gramps`!

**Neuchovávajte zálohy vo formáte GRDB**. GRDB je databáza, ktorá môže byť závislá od počítača (čítaj, nefunguje na inom počítači). Malé poškodenie súboru GRDB sa tiež nedá opraviť. Na zálohovanie používajte formát súboru `.gramps`!

### Podporuje program Gramps písma Unicode?

Podporuje najmä iné ako rímske písma Unicode? Áno. Gramps interne pracuje s Unicode (UTF-8), takže všetky abecedy možno použiť na všetkých vstupných poliach. Všetky zostavy to plne podporujú, hoci pre PDF/PS musíte pracovať s gnome-print alebo [LibreOffice](http://www.documentfoundation.org/download/).

## Inštalácia

=== Čo je potrebné na inštaláciu programu Gramps pod Linuxom, Solarisom alebo FreeBSD?

Gramps je aplikácia [GTK](http://en.wikipedia.org/wiki/Gtk). Gramps potrebuje mať v systéme nainštalované knižnice [PyGObject](http://en.wikipedia.org/wiki/PyGObject). Pokiaľ sú tieto knižnice nainštalované, Gramps by mal fungovať. Bude fungovať pod pracovným prostredím GNOME, KDE alebo akýmkoľvek iným pracovným prostredím. Ak sú v systéme nainštalované väzby GNOME pre Python, Gramps bude mať ďalšie funkcie. Skontrolujte, či spĺňa odporúčania projektu Gramps týkajúce sa verzie GTK, ktorú treba použiť.

=== Funguje Gramps v systéme Windows?

Áno, Windows je platforma podporovaná komunitou pre Gramps.

Môžete si stiahnuť [download](wiki:Download#MS_Windows) [All In One Gramps Software Bundle for Windows](wiki:All_In_One_Gramps_Software_Bundle_for_Windows) (GrampsAIO).

Urobíme všetko pre to, aby sme vyriešili všetky nahlásené problémy súvisiace so systémom Windows. Pozrite si [tu](wiki:Kontakt).

### Funguje program Gramps na počítači Mac?

Áno, MacOS je komunitou podporovaná platforma pre Gramps.

Môžete si stiahnuť [download](wiki:Download#macOS) verziu pre macOS.

Urobíme všetko, čo je v našich silách, aby sme vyriešili všetky nahlásené problémy týkajúce sa systému Apple macOS. Pozrite si [tu](wiki:Kontakt).

Pozrite si [zde](wiki:Mac_OS_X:Balík_aplikácií).

### Funguje aplikácia Gramps na mojom mobilnom zariadení?

Krátka odpoveď znie nie, program Gramps nie je možné nainštalovať na váš mobilný telefón alebo tablet( [Google Android](https://en.wikipedia.org/wiki/Android_(operating_system)) alebo [Apple iOS](https://en.wikipedia.org/wiki/IOS) ).

Technickejšia odpoveď je áno, ak môžete na mobilné zariadenie nainštalovať verziu operačného systému Linux spolu so všetkými podpornými balíkmi.

### Funguje program Gramps na mojom počítači Google Chromebook?

Môžete, ale s niekoľkými problémami nainštalovať Gramps na váš [Chromebook](https://en.wikipedia.org/wiki/Chromebook) pozri [\#11058](https://gramps-project.org/bugs/view.php?id=11058).

=== Aké sú minimálne špecifikácie na spustenie programu Gramps? Odporúčali by sme aspoň 1920x1080 video displej. Počiatočné požiadavky na pamäť pre Gramps, boli znížené a Gramps boli pomerne vysoké. Počnúc verziou Gramps 3.0 mohol softvér bežať celkom efektívne na systéme s 256 MB, ktorý pojal podstatne viac ľudí. Systém s 512 MB by mal byť schopný pojať približne 200 000 osôb. Požiadavky na diskový priestor pre databázy sú však podstatne väčšie, pričom typická databáza má veľkosť niekoľko megabajtov. Pre 120 000 osôb musíte počítať už s 530 MB pre databázu. Obrázky sa ukladajú na disk samostatne, preto je potrebný veľký pevný disk.

<span id="Ako aktualizovať GRAMPS?">

### Ako aktualizovať program Gramps?

</span> Operačné systémy GNU/Linux zvyčajne riešia problémy s aktualizáciou za vás. Ak tak neurobia, musíte sa opýtať používateľov vašej preferovanej distribúcie GNU/Linux.

## Predvoľby

=== Môžem zmeniť dátumy v prehľadoch na 'deň mesiac rok'?

Áno, v predvoľbách ( }) zmeňte nastavenie Gramps na požadovaný formát (napr. RRRR-MM-DD alebo deň mesiac rok) a vytvorte správu. Použijú sa vaše globálne nastavenia dátumu.

## Spolupráca-Prenosnosť

=== Je Gramps kompatibilný s iným genealogickým softvérom?

Gramps sa snaží zachovať kompatibilitu s [GEDCOM](wiki:GEDCOM), všeobecným štandardom pre záznam genealogických informácií. Máme importné a exportné filtre, ktoré umožňujú programu Gramps čítať a zapisovať súbory GEDCOM.

Je dôležité pochopiť, že štandard GEDCOM je implementovaný nedostatočne - prakticky každý genealogický softvér má svoju vlastnú "príchuť" GEDCOM. Keď sa dozvieme o novej príchuti, filtre na import/export sa dajú vytvoriť veľmi rýchlo. Zistenie neznámych príchutí si však vyžaduje [spätnú väzbu od používateľov](wiki:Kontakt). Neváhajte nás informovať o akejkoľvek príchuti GEDCOM, ktorú Gramps nepodporuje, a my urobíme všetko pre to, aby sme ju podporovali!

Na tejto wiki je osobitná časť, ktorá sa zaoberá [Gramps a GEDCOM](wiki:Gramps_a_GEDCOM).

### Môže program Gramps čítať súbory vytvorené inými genealogickými programami?

Áno, dokáže čítať súbory GEDCOM vytvorené inými genealogickými programami.

- [Viz vyššie.](wiki:Gramps_6.0_Wiki_Manual_-_FAQ#Is_Gramps_compatible_with_other_genealogical_software.3F)

### Môže Gramps zapisovať súbory čitateľné inými genealogickými programami?

Áno, dokáže zapisovať súbory GEDCOM, ktoré môžu čítať iné genealogické programy.

- [Viz vyššie.](wiki:Gramps_6.0_Wiki_Manual_-_FAQ#Is_Gramps_compatible_with_other_genealogical_software.3F)

### Aké štandardy Gramps podporuje?

Na štandardoch je pekné to, že ich nikdy nie je nedostatok. Program Gramps je testovaný na podporu nasledujúcich verzií GEDCOM 5.6.0, Brother's Keeper, Family Origins, Family Tree Maker, Ftree, GeneWeb, Legacy, Personal Ancestral File, Pro-Gen, Reunion a Visual Genealogie.

===Ako môžem do programu Gramps importovať údaje z iného genealogického programu?

Najlepší spôsob je vytvoriť nový rodokmeň a v ponuke súborov vybrať možnosť importovať. Tu vyberiete GEDCOM, ktorý ste vytvorili v inom programe, a importujete ho.

### Môžem nainštalovať program Gramps na webový server Linux a používať ho prostredníctvom webového prehliadača?

To by umožnilo mojim príbuzným po celom svete prístup k nemu a jeho aktualizáciu.

Program Gramps síce dokáže generovať webové stránky, ale neposkytuje webové rozhranie, ktoré by umožňovalo editáciu. Ak je to požiadavka, potom [GeneWeb](http://geneweb.org) alebo [webtrees](http://www.webtrees.net/) sú programy, ktoré skôr vyhovujú vašim potrebám. Pozrite si aj experimentálny [gramps-online](https://github.com/gramps-project/gramps-online). Možno si však budete chcieť položiť nasledujúce otázky:

1.  Naozaj chcem, aby moji príbuzní alebo iní ľudia priamo upravovali moju genealogickú databázu?
2.  Dôverujem implicitne, bez overenia, akýmkoľvek údajom, ktoré môžu ľudia zadávať?
3.  Majú títo ľudia rovnaké chápanie správnej genealogickej praxe ako ja?

Lepším prístupom môže byť poskytnutie rozhrania webového formulára, ktoré umožní ostatným zadávať údaje, ktoré sa potom uchovávajú na preskúmanie. Vy sa potom môžete rozhodnúť, či sa tieto informácie majú vložiť do vašej databázy.

Možno budete chcieť zvážiť aj dôsledky možných výpadkov vašej stránky, ak si nemôžete dovoliť prémiovú webhostingovú službu.

## Správy

### Môže Gramps vytlačiť genealogický strom pre moju rodinu?

Áno. Rôzni ľudia majú rôzne predstavy o tom, čo je genealogický strom. Niektorí si ho predstavujú ako tabuľku, ktorá vychádza zo vzdialeného predka a uvádza všetkých jeho potomkov a ich rodiny. Iní si myslia, že by to mala byť tabuľka idúca od osoby späť v čase, v ktorej sú uvedení predkovia a ich rodiny. Ďalší ľudia si myslia, že ide o tabuľku, textovú správu atď.

Gramps dokáže vytvoriť ktorýkoľvek z uvedených typov a mnoho ďalších rôznych grafov a správ. Architektúra zásuvných modulov navyše umožňuje používateľom (vám) vytvárať vlastné zásuvné moduly, ktorými môžu byť nové zostavy, grafy alebo výskumné nástroje.

===Ako možno určiť príbuzenské vzťahy medzi osobami v strome?

Niektorí používatelia majú záujem o zobrazenie len priamych genetických vzťahov predkov alebo potomkov. Iných používateľov zaujímajú aj vedľajšie (bratranci a sesternice!) línie alebo priami príbuzní. A ešte iných používateľov zaujíma, ako najviac nepriame spojenia ovplyvňujú spoločenstvo.

Gramps preto ponúka neustále sa rozširujúcu škálu nástrojov, prehľadov a metód na určenie toho, ako sú ľudia prepojení v rámci databázy stromu. Na základe diskusie na stránke Gramps-User [Maillist](wiki:Contact#Mailing_lists) boli zverejnené návrhy zhromaždené a rozpracované v článku "[How to find the relationship between people](wiki:How_to_find_the_relationship_between_people)" v kategórii wiki "[How do I...](wiki::Category:How_do_I...)".

=== Do akých formátov môže Gramps vypisovať svoje správy?

Textové správy sú k dispozícii vo formátoch HTML, PDF, ODT, LaTeX a RTF. Grafické správy (grafy a diagramy) sú k dispozícii vo formátoch PostScript, PDF, SVG, ODS a [GraphViz](wiki:Output_formats#Graphviz).

### Ako môžem zmeniť predvolený jazyk v správach?

Správy sú v jazyku vašej inštalácie. Väčšina zostáv umožňuje vybrať Jazyk výstupu, aby ste mohli vyhľadať možnosť na výber prekladu, ktorý sa má použiť pre danú zostavu. Môžete ho zmeniť nainštalovaním ďalších jazykových balíkov, pozri [Howto: Zmena jazyka zostáv](wiki:Howto:_Zmena_jazyka_zostáv).

### Je program Gramps kompatibilný s internetom?

Program Gramps dokáže ukladať webové adresy a presmerovať na ne váš prehliadač. Dokáže importovať údaje, ktoré stiahnete z internetu. Dokáže exportovať údaje, ktoré by ste mohli odoslať cez internet. Gramps pozná štandardné formáty súborov, ktoré sa bežne používajú na internete (napr. obrázky JPEG, PNG a GIF, zvukové súbory MP3, OGG a WAV, filmové súbory QuickTime, MPEG a AVI atď.) Okrem toho je len málo vecí, ktoré môže genealogický program urobiť s internetom.

### Môžem vytvárať vlastné správy/filtre/čokoľvek?

Áno. Existuje mnoho úrovní prispôsobenia. Jednou z nich je vytváranie alebo úprava šablón používaných pre správy. Tým získate určitú kontrolu nad písmami, farbami a určitým rozložením správ. Môžete tiež použiť ovládacie prvky Gramps v dialógových oknách zostáv, aby ste určili, aký obsah sa má použiť pre konkrétnu zostavu. Okrem toho máte možnosť vytvárať vlastné filtre -- to je užitočné pri výbere osôb na základe vami stanovených kritérií. Tieto filtre môžete kombinovať a vytvárať tak nové, zložitejšie filtre. Nakoniec máte možnosť vytvárať vlastné zásuvné moduly. Môžu to byť nové zostavy, nástroje na výskum, filtre na import/export atď. To predpokladá určité znalosti programovania v jazyku Python.

### Prečo sa v správach PDF/PS zobrazujú nelatinkové znaky ako odpad?

Ide o obmedzenie zabudovaných fontov formátov PS a PDF. Ak chcete vytlačiť nelatinkový text, použite Tlač... v ponuke výberu formátu v dialógovom okne zostavy. Použije sa pritom backend `gnome-print`, ktorý podporuje vytváranie súborov PS a PDF, ako aj priamu tlač. (Poznámka: možno budete musieť nainštalovať gnome-print samostatne, pretože pre program Gramps nie je potrebný).

Ak máte iba latinský text, možnosť PDF vytvorí menšie PDF v porovnaní s PDF vytvoreným pomocou gnome-print jednoducho preto, že nebudú vložené žiadne informácie o písme.

### Rád by som prispel do programu Gramps napísaním svojej obľúbenej správy. Ako to mám urobiť?

Najjednoduchší spôsob, ako prispieť do zostáv, filtrov, nástrojov atď. je skopírovať existujúcu zostavu, filter alebo nástroj Gramps. Ak dokážete vytvoriť to, čo chcete, úpravou existujúceho kódu -- výborne! Ak váš nápad nezapadá do logiky žiadneho existujúceho nástroja Gramps, budete musieť napísať vlastný doplnok od začiatku. Pomoc je k dispozícii na [Portál pre vývojárov](wiki:Portál:Vývojári) alebo na [Zoznam vývojárov](wiki:Kontakt): gramps-devel@lists.sourceforge.net.

Ak chcete otestovať svoju rozpracovanú prácu, môžete svoj zásuvný modul uložiť do adresára `$HOME/.gramps/plugins` a mal by sa nájsť a importovať pri spustení. Správne napísaný doplnok/plugin sa zaregistruje v programe Gramps, vytvorí položku menu atď.

Ak ste so svojím doplnkom/pluginom spokojní a chceli by ste svojím kódom prispieť späť do projektu Gramps, ste veľmi vítaní, ak sa pridáte a napíšete nám na adresu gramps-devel@lists.sourceforge.net mailing list.

## Databáza - formáty súborov Gramps

Predvolený formát súborov je [Gramps XML](wiki:Gramps_XML), ktorý sa používa na export, zálohovanie a import a zachováva zadané genealogické údaje bez straty údajov v porovnaní s formátom GEDCOM. === Akú maximálnu veľkosť databázy (v bajtoch) dokáže Gramps spracovať?

Program Gramps nemá žiadne pevné obmedzenia na veľkosť databázy, ktorú dokáže spracovať. Od verzie 2.0.0 Gramps už nenačíta všetky údaje do pamäte, čo mu umožňuje pracovať s oveľa väčšou databázou ako predtým. V skutočnosti však existujú praktické obmedzenia. Hlavnými obmedzujúcimi faktormi sú dostupná pamäť systému a veľkosť vyrovnávacej pamäte používanej na prístup k databáze BSDDB. Pri dnešných bežných veľkostiach pamäte by Gramps nemal mať problém s používaním databáz s [Miliónmi ľudí](wiki:Gramps_Performance#JohnBoyTheGreat_2019-12.2C_version_6.0.1).

### Koľko ľudí zvládne databáza Gramps?

Pozri vyššie. Opäť to závisí od toho, koľko pamäte a úložného priestoru má váš počítač, pozrite si [Gramps Performance](wiki:Gramps_Performance).

### Moja databáza je naozaj veľká. Dá sa nejakým spôsobom obísť načítanie všetkých údajov do pamäte?

Od verzie 2.0.0 už Gramps nenačíta všetky údaje do pamäte, čo mu umožňuje pracovať s oveľa väčšou databázou ako predtým. Používaný formát súboru je `.grdb`, čo znamená databáza Gramps.

=== Môžem spustiť program Gramps z databázy na zdieľanom disku NFS?

Áno, databázu Gramps môžete spustiť zo zdieľanej zložky [NFS(NetworkFile System)](https://en.wikipedia.org/wiki/Network_File_System).

### Čo znamená "prenosný"?

Databáza Gramps 3 (a akýkoľvek súbor .grdb) je veľmi závislá od verzie softvéru, ktorý ju vytvoril. Nemôžete napríklad len tak preniesť svoje údaje Gramps v týchto formátoch do iného operačného systému (alebo dokonca do inej verzie operačného systému) a očakávať, že budete môcť svoje údaje prečítať. Údaje nie sú "prenosné". Preto sa nemôžete spoliehať len na zálohy týchto formátov, ale mali by ste ich občas aj exportovať do formátu, ktorý je prenosný. Existujú dva možné prenosné formáty: GEDCOM a Gramps XML (.gramps alebo .gpkg). Odporúča sa však iba formát Gramps XML, pretože verne ukladá všetky vaše údaje.

### Prečo nie je formát databázy (GRDB) prenosný?

Najväčší problém s prenositeľnosťou formátu Gramps spočíva v "transakciách". Vo verzii Gramps 2.2 sme pridali podporu atomických transakcií na ochranu údajov. Pri atomických transakciách sa viacero zmien odovzdáva ako jeden celok. Buď sa to podarí všetkým zmenám, alebo sa to nepodarí žiadnej zo zmien. Nikdy sa nestane, že by ste mali k dispozícii len čiastočný súbor zmien. Vedľajšou výhodou používania transakcií je rýchlejší prístup k databáze (čítanie a zápis).

Problémom transakcií (aspoň pri použití BSDDB) je, že neumožňujú uložiť všetky údaje do jedného súboru. Na udržanie prehľadu sú potrebné logovacie súbory. Tieto logovacie súbory sa uchovávajú v adresári DB Environment. Pre každý súbor potrebujeme samostatný adresár, inak by sa logovacie súbory mohli navzájom rušiť.

Vo verzii 2.2 uchovávame logovacie súbory v adresári `~/.gramps/`, pričom pre každú databázu vytvárame jedinečný adresár. Problémom je, že váš súbor GRDB potrebuje súbory denníka, ktoré sú v inom adresári.

Kopírovaním súboru GRDB sa kopíruje len časť databázy.

## Chyby a požiadavky

### Čo mám robiť, ak som našiel chybu?

Môžete [odoslať hlásenie o chybe.](wiki:Ako_nahlásiť_chyby)

Dobré hlásenie chyby by malo obsahovať:

1.  Verziu programu Gramps, ktorú ste používali, keď ste narazili na chybu (dostupná cez položku menu Pomoc → O programe).
2.  Jazyk, pod ktorým bol program Gramps spustený (dostupné vykonaním príkazu `echo $LANG` v termináli).
3.  Príznaky naznačujúce, že ide skutočne o chybu.
4.  Všetky spätné hlásenia, chybové hlásenia, varovania atď. ktoré sa objavili vo vašom termináli alebo v samostatnom okne spätného sledovania.

Väčšinu problémov je možné rýchlo odstrániť za predpokladu, že je k dispozícii dostatok informácií. Aby ste to zabezpečili, sledujte svoje hlásenia o chybách. Potom vás budeme môcť kontaktovať, ak budeme potrebovať ďalšie informácie.

### Požiadavky

- Gramps by mal byť typom programu ....

Je zrejmé, že Gramps sa bezpodmienečne musí stať programom typu (klient-server/web/PHP/weblog/Javascript/C++/distribuovaná/KDE/Motif/Tcl/Win32/C#/vy-menujte-jeho). Kedy sa to stane?

Najistejší spôsob, ako sa to stane, je, že si to urobíte sami. Keďže Gramps je free/open source, nikto vám nebráni vziať si celý kód a pokračovať v jeho vývoji smerom, ktorý uznáte za vhodný. Pritom môžete zvážiť, či svojmu novému projektu nedáte iný názov, aby ste sa vyhli zámene s pokračujúcim vývojom Gramps. Ak by ste chceli, aby vám projekt Gramps poskytol rady, odborné znalosti, filtre atď. radi budeme s vaším novým projektom spolupracovať, aby sme zabezpečili kompatibilitu alebo možnosti importu/exportu do vášho nového formátu projektu.

Ak by ste však chceli, aby projekt Gramps prijal vašu stratégiu, museli by ste presvedčiť vývojárov Gramps, že vaša stratégia je pre Gramps dobrá a lepšia ako súčasná stratégia vývoja.

## Pridávanie a úprava mojej databázy

=== Aký je rozdiel medzi bydliskom a adresou?

Bydlisko je miesto, kde niekto určitý čas žil. Adresa je názov bydliska naformátovaný spôsobom, ktorý očakáva poštový systém. Preto môže mať každé bydlisko aj adresu, ak je to užitočné. Pozrite si tiež: \[Prečo udalosť_obyvateľstva_a_nie_adresa%3F \| Prečo udalosť_obyvateľstva a nie adresa?\]\]

### Ako zmeniť poradie detí?

Deti môžete presúvať v [Rodinný editor](wiki:Gramps_6.0_Wiki_Manuál_-_Zadávanie_a_úprava_údajov:_Detail_-_časť_1#Upravovanie_informácií_o_vzťahoch) v [Deti](wiki:Gramps_5._1_Wiki_Manuál_-_Vedenie_a_úprava_údajov:_detail_-_časť_1#Deti) záložkou [ťahaním a púšťaním](http://en.wikipedia.org/wiki/Drag-and-drop) alebo pomocou tlačidiel a .

### Ako zmením poradie manželov?

Poradie manželov môžete zmeniť v [Kategória vzťahov](wiki:Gramps_6.0_Wiki_Manual_-_Categories#Reorder_Relationships_dialog) výberom tlačidla na paneli nástrojov.

### Ako pridám ďalšieho manžela/manželku?

Pozrite si [Pridať manžela/manželku](wiki:Pridať_manžela/manželku)

### Ako odstránim manžela/manželku?

### Ako pridáte fotografie k položke?

Pozri [Pridávanie fotografií a iných mediálnych objektov](wiki:Gramps_6.0_Wiki_Manuál_-_Vkladanie_a_úprava_údajov:_brief#Pridávanie_fotografií_a_iných_mediálnych_objektov).

### Ako nájdete nepoužité médiá?

Médiá, ktoré neboli priradené k žiadnym objektom, môžete nájsť vytvorením [Vlastný filter](wiki:Gramps_6.0_Wiki_Manual_-_Filters#Custom_Filters) v zobrazení kategórie médií. Na vyhľadanie médií s počtom odkazov menším ako 1 použite pravidlo [Media objects with reference count of &lt;count&gt;](wiki:Gramps_6.0_Wiki_Manual_-_Filters#Media_objects_with_a_reference_count_of_.3Ccount.3E).

===Ako môžem publikovať genealogickú webovú lokalitu pomocou programu Gramps? <span id="Ako môžem publikovať webové stránky vytvorené programom GRAMPS?"> Program Gramps má v ponuke Reports (Správy) viacero možností na vytváranie webových stránok na základe údajov vášho stromu.

Na stránke [Howto: Vytvoriť genealogickú webovú stránku pomocou programu Gramps](wiki:Howto:_Make_a_genealogy_website_with_Gramps) návod opisuje použitie [Narrated Web Site](wiki:Gramps_6.0_Wiki_Manuál_-_Reports_-_part_7#Narrated_Web_Site). (alias NarrativeWeb). Naučíte sa v nej vytvárať webové stránky okolo súboru osôb vo vašom rodokmeni.

Po vygenerovaní môžete webové súbory nahrať na hostingovú službu. Môžete ich tiež distribuovať na prenosnom flash disku alebo inom médiu. </span>

Môžete si tiež nainštalovať doplnkové správy tretích strán na vytvorenie iných štýlov webového obsahu. Pozrite si [Zoznam doplnkov](wiki:6.0_Addons/sk#Zoznam_doplnkov). {{-}}

[Category:Sk:Documentation](wiki:Category:Sk:Documentation)
