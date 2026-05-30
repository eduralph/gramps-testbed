---
title: Gramps 6.0 Wiki Manual - Main Window/sk
categories:
- Sk:Documentation
- Sk:Gramps terminology
managed: false
source: wiki-scrape
wiki_revid: 118898
wiki_fetched_at: '2026-05-30T20:08:10Z'
lang: sk
---

{{#vardefine:chapter\|3}}{{#vardefine:figure\|0}} ![[_media/MainWindow-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Example of a Gramps Main Windows]] **<span style="font-size:120%">Prvky hlavného okna programu Gramps</span>**  
*or*  
**<span style="font-size:120%">Vizuálny sprievodca rozhraním programu Gramps</span>**.

Grafické používateľské rozhranie (GUI) je spôsob usporiadania informácií na obrazovke počítača, ktorý je ľahko pochopiteľný a použiteľný, pretože používa ikony, ponuky a myš, a nie iba text.

Hoci je GUI oveľa intuitívnejšie ako zapamätanie si príkazov z klávesnice, je ťažké naučiť sa z dokumentácie funkcie bez toho, aby ste poznali názov funkcie, ktorú chcete vyhľadať. Mnohé prvky nie sú v programe Gramps označené, aby sa znížila neprehľadnosť a maximalizoval priestor na zobrazenie genealogických informácií. Existujú dokonca [nastavenia predvolieb](wiki:Gramps_6.0_Wiki_Manual_-_Settings/sk#Zobrazenie), ktoré nezobrazujú textové označenia tlačidiel (ikon) na paneli Navigátora kategórií.

V tejto časti príručky Wiki sú teda uvedené štandardizované názvy prvkov obrazovky Gramps. Vyzbrojení štandardnými názvami môžete efektívnejšie použiť vyhľadávač (napríklad Google) na nájdenie stránok v online príručke, ktoré sa zaoberajú daným prvkom. Ako príklad, na vyhľadanie stránok príručky Gramps Wiki o fráze ["Režim navigátora"](https://www.google.com/search?q=navigator%20mode+site%3Agramps-project.org%2Fwiki) použite nasledujúce vyhľadávacie výrazy Google:

`     "režim navigátora" site:gramps-project.org/wiki`

Toto konkrétne vyhľadávanie dokonca nájde popisne pomenované ilustrácie výberu režimov pre bočný panel Navigátora. Výberom jedného z týchto obrázkov sa zobrazí webová stránka o danej ilustrácii a o tom, kde je použitá v dokumentácii. Tieto ilustrované stránky majú zvyčajne väčší úvodný materiál.

Ak sa konkrétny prvok obrazovky neobjaví medzi nižšie uvedenými obrázkami, prezrite si [Galériu snímok obrazovky Gramps](wiki:screenshots). Na tejto stránke sú zobrazené miniatúry snímok obrazovky programu Gramps, ktoré sú použité v celej dokumentácii. Kliknutím na miniatúru obrázka sa zobrazí obrázok v plnej veľkosti a varianty tohto obrázka, potom prejdite do časti "Použitie súborov", kde nájdete stránky Wiki, ktoré ilustrujú možnosti použitia tejto [snímky obrazovky](wiki:screenshots). Podobne [Galéria ikon Gramps](wiki:Gramps_icon_set) identifikuje správne názvy ikon používaných v celom programe Gramps.

Keď sa zoznámite s prvkami obrazovky, preskúmajte [Klávesové skratky](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings/sk), aby ste sa naučili skratky pre často používané funkcie.

## Hlavné okno

Pri otvorení (novej alebo existujúcej) databázy rodinného stromu sa v "Zobrazovacej oblasti" zobrazí úvodné okno Gramps [Informačný panel](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/sk#Čo_je_Gramplet) so skrytým bočným a spodným panelom. Po výbere [Kategória Ľudia](wiki:Gramps_6.0_Wiki_Manual_-_Categories/sk#Kategórie_navigátora) z okna Navigátora sa rozloženie Hlavného okna aktualizuje tak, že sa v "Zobrazovacej oblasti" zobrazí "Pohľad Osoba (zoznam)". Pozri obr. {{#var:chapter}}.{{#expr:{{#var:figure}}+1}}: {{-}} ![[_media/MainWindow-PeopleCategory-PeopleTreeView-annotated-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Anotované časti hlavného okna Gramps, zobrazujúce kategóriu Ľudia - Pohľad Strom ľudí - príklad použitia možnosti Zoskupení ľudia]] {{-}}

Hlavné okno Gramps obsahuje nasledujúce prvky: {{-}}

### Titulný riadok okna

- Titulný riadok okna zobrazuje názov vybraného rodinného stromu, názov pohľadu Kategória, názov programu Gramps a tlačidlá na minimalizáciu, maximalizáciu a zatvorenie programu Gramps. Okno je možné z Titulného riadku aj pretiahnuť.

### Ponuka

- Panel ponuky: Panel ponuky ([Hlavné ponuky](wiki:Gramps_6.0_Wiki_Manual_-_Navigation/sk#Hlavné_ponuky)) sa nachádza úplne navrchu okna (hneď pod názvom okna) a poskytuje prístup ku všetkým funkciám programu Gramps.
- Ponuky sú kontextové - zobrazené možnosti závisia od toho, ktorá kategória je aktívna.
- Kliknutím na označenie záhlavia ponuky sa otvorí konkrétna podponuka. Položky podponuky môžu byť stlmené (nedostupné), ak nie sú použiteľné s aktívnou položkou.

[Typograficky](wiki:Gramps_6.0_Wiki_Manual_-_Preface/sk#Typografické_konvencie_v_Gramps_Wiki_manuáli), Výbery Menu budú v príručke wiki vyzerať takto: .

#### Vysúvacie ponuky

![[_media/Bottombar-sidebar-drop-down-menu-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}}  neoznačené tlačidlo šípka nadol  vysúvacieho menu]] Mimo panela ponuky, v prípade sa vyskytuje neoznačené tlačidlo *šípka nadol* **vysúvacej ponuky**, ktoré signalizuje, že pre položku rozhrania naľavo od neho sú k dispozícii ďalšie možnosti. {{-}}

#### Vyskakovacie ponuky

![[_media/Clipboard-dialog-example-context-menu-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Schránka - s príkladom kontextového vyskakovacieho menu po kliknutí pravým tlačidlom myši na položku Rodina]]Najneviditeľnejšou možnosťou rozhrania môže byť **kontextová vyskakovacia ponuka**.

Kliknutím pravým tlačidlom myši na položku rozhrania sa zobrazia skratky k niektorým často užitočným funkciám pre danú položku. {{-}} ![[_media/QuickViewReport-EditPerson-context-menu-popup-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Editor osoby - s príkladom kontextovej vyskakovacej ponuky po kliknutí pravým tlačidlom myši na prázdne miesto v záhlaví]]Kliknutie pravým tlačidlom myši na objekty je v GUI známe. Ale kliknutie pravým tlačidlom myši do prázdneho priestoru záhlavia akéhokoľvek Editora objektu je menej samozrejmé. Odhalí sa však iná kontextová ponuka s ďalšími skratkami k užitočným možnostiam hlásenia a navigácie. {{-}}

### Panel nástrojov

- [Panel nástrojov](wiki:Gramps_6.0_Wiki_Manual_-_Navigation/sk#Panel_nástrojov) sa nachádza priamo pod panelom menu. Jeho tlačidlá umožňujú rýchlejší prístup k najčastejšie používaným funkciám pre aktívnu obrazovku programu Gramps.
- Sortiment tlačidiel panela nástrojov je [kontextovo citlivý](https://wikipedia.org/wiki/Context-sensitive_user_interface). Ktoré nástroje sa zobrazia, závisí od toho, ktorá kategória je aktívna. A na paneli nástrojov sú zahrnuté len tlačidlá pre podrežimy aktuálne zvolenej kategórie zobrazenia.
- ⚙ Konfigurovateľné možnosti: Väčšina pohľadov Kategórie má tlačidlo ![[_media/Gramps-config.png]]  ako alternatívu k výberu z menu Pohľad alebo stlačenie tlačidla *Konfigurovať aktívny pohľad* [klávesové skratky](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings/sk#Common_keybindings). Táto možnosť otvorí dialógové okno s voľbami na prispôsobenie zobrazenia záznamov v Pohľade. Základné prispôsobenia môžu zahŕňať voľbu postupnosti zoradenia a voľbu, či sa majú zobrazovať konkrétne podrobnosti.
- *Prispôsobenia konfigurácie sú trvalé*. Prenášajú sa do budúcich relácií pomocou programu Gramps.
- Po nabehnutí na ikonu panela nástrojov sa zobrazí tip na jej funkciu

![[_media/ToolbarIcon-OpenTheToolsDialog-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Tip pre tlačidlo Nástroje na paneli nástrojov kategórie Ovládací panel]] Panel nástrojov môžete skryť alebo odkryť pomocou voľby v menu .

`Doplnok `[<code>Themes</code>](wiki:Addon:ThemePreferences)` rozširuje dialógové okno `[<code>Predvoľby</code>](wiki:Gramps_6.0_Wiki_Manual_-_Settings/sk)` o kartu `*`Theme`*`. `

Jednou z možností karty Téma je začiarkovacie políčko ☑ . Začiarknutie tohto políčka spôsobí, že sa zobrazia textové označenia.  
*Toto políčko je* ❏''štandardne odznačené. ![[_media/Preferences-Themes-addon.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Pridané možnosti karty Téma pre dialógové okno Predvoľby]]

### Navigátor

- Navigátor: Navigátor je voliteľný bočný panel umiestnený v ľavej časti okna a umožňuje výber rôznych kategórií. Pozri [Kategórie navigátora](wiki:Gramps_6.0_Wiki_Manual_-_Categories/sk#Kategórie_navigátora).

  
Navigátor je zobrazený v predvolenom nastavení, ale tento bočný panel možno voliteľne skryť alebo odkryť pomocou ponuky alebo [klávesovej skratky](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings/sk#7) . ( v systéme MacOS).

Pozrite si tiež:

- [Prepínanie režimov navigátora](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window/sk#Prepínanie_režimov_navigátora)
- Textové označenia môžete skryť zrušením výberu možnosti ☑ v [Zobrazenie](wiki:Gramps_6.0_Wiki_Manual_-_Settings/sk#Zobrazenie).
- Funkcie bočného panela Navigátora (Kategórie pohľadov, Režimy zobrazenia a štýly rozhrania Navigátora) môžete pridať, odstrániť, skryť alebo odhaliť pomocou Správcu zásuvných modulov.

### Zobrazovacia oblasť

- Zobrazovacia oblasť: Oblasť v strede okna programu Gramps je zobrazovacia oblasť. To, čo sa v nej zobrazuje, závisí od aktuálne zvolenej kategórie pohľadu. [We will discuss Views in detail below](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window/sk#Prepínanie_pohľadov).

### Stavový riadok a ukazovateľ priebehu

- Stavový riadok a ukazovateľ priebehu: Nachádzajú sa úplne dole v okne Gramps.
  - Ukazovateľ priebehu sa nachádza v ľavom dolnom rohu okna Gramps. Zobrazuje priebeh časovo náročných operácií, ako je otváranie a ukladanie veľkých databáz rodinného stromu, import a export do iných formátov, generovanie webových stránok atď. Keď nevykonávate tieto typy operácií, ukazovateľ priebehu sa nezobrazuje.
  - Stavový riadok sa nachádza napravo od ukazovateľa priebehu. Zobrazuje informácie o aktuálnej činnosti programu Gramps a kontextové informácie o vybraných položkách. (Môžete tiež upraviť [Predvoľby zobrazenia](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Display), aby sa zobrazoval **Vzťah [Aktívnej osoby](wiki:Gramps_Glossary#active_person) k [domovskej osobe](wiki:Gramps_Glossary#home_person)**.
  - V stavovom riadku sa môže občas zobraziť prechodné upozornenie, [varovanie](wiki:Gramps_6.0_Wiki_Manuál_-_Error_and_Warning_Reference#Warnings) na neobvyklé stavy. Na ľavej strane stavového riadka sa na tri minúty zobrazí informatívne tlačidlo so stručným zhrnutím (ako je uvedené nižšie). Kliknutím na túto ikonu žiarovky sa zobrazia podrobnosti o týchto menších upozorneniach.

![[_media/Status-bar-warning-button-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Hlavné okno programu Gramps zobrazujúce tlačidlo Varovanie v stavovom riadku]]

{{-}}

### Spodný a bočný panel

} Umiestnenie **Ponuky grampletov** neoznačenou *šípkou nadol* (∨) Pridať/odstrániť/obnoviť ponuku grampletov\]\]

Pridávať/odstraňovať a obnovovať predvolené gramplety môžete aj kliknutím na tlačidlo (*šípka nadol*), známeho aj ako **Ponuka grampletov** v pravom hornom rohu názvov panelov, a potom použiť jednu z možností z rozbaľovacej ponuky, napr:

- **Ponuka grampletov**
  - \- Zobrazí zoznam grampletov, ktoré sú k dispozícii na použitie v tejto **Ponuke grampletov**

  - \- Zobrazí zoznam grampletov, ktoré sú v súčasnosti zobrazené v **Ponuke grampletov** a ktoré je možné odstrániť.

  - \- Zobrazí } potvrdzovacie dialógové okno, ktoré umožňuje obnoviť predvolené gramplety v ponuke grampletov.

{{-}}

##### Obnoviť predvolené nastavenia? dialóg

![[_media/GrampletBar-Restore-to-defaults-dialog-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Obnoviť predvolené nastavenia? dialóg]]

, umožňuje obnoviť Ponuku grampletov na predvolené nastavenia. Túto akciu nie je možné vrátiť späť. Výberom potvrďte alebo vyberte . {{-}}

<span id="Vyhľadávací panel">

#### Vyhľadávací panel

</span> ![[_media/MainWindow-SearchBar-sidebar-hidden-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Pohľad kategórie Ľudia - zobrazenie vyhľadávacieho panela po skrytí bočného panela]]

Ak sa v zobrazení Kategória so zoznamom nezobrazuje bočný panel, namiesto neho sa zobrazí . Dostupné možnosti vyhľadávania sa líšia v závislosti od kategórie Pohľadu, v ktorej sa nachádzate. Viditeľný bočný panel však spôsobuje, že Vyhľadávací panel je neviditeľný. ![[_media/PeopleCategory-sidebar-filter-enabled-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Pohľad kategórie Rodiny - zobrazenie bočného panela nahrádzajúceho vyhľadávací panel]]

je k dispozícii v nasledujúcich Pohľadoch a výberových oknách pre nasledujúce Kategórie: Ľudia, Vzťahy, Rodiny, Udalosti, Miesta, Zdroje, Citácie, Archívy, Médiá, Poznámky. *Nie je k dispozícii v nasledujúcich kategóriách Pohľadov:* v kategóriách: Informačný panel, Vzťahy, Grafy, Zemepis.

Zadaním znakov do a kliknutím na tlačidlo sa zobrazia len riadky, ktoré zodpovedajú textu.

{{-}} Všimnite si, že rôzne majú tiež vyhľadávacie panely:

- [Selektor Výber rodiny](wiki:Gramps_6.0_Wiki_Manual_-_Categories/sk#Selektor_Výber_rodiny)

![[_media/SelectFamily-SelectorDialog-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Selektor Výber rodiny - zobrazenie vyhľadávacieho panela]] {{-}}

## Prepínanie režimov navigátora

![[_media/Navigator-mode-selection-dropdownlist-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Rozbaľovací zoznam pre výber režimu navigátora]]

Režim [navigátora](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window#Navigator) môžete vybrať z rozbaľovacieho zoznamu na bočnom paneli :

- [<strong>Kategória</strong>](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window#Category_navigator_mode_.28default.29) (Predvolené)
- [Rozpínač](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window#Expander_navigator_mode)
- [Rozbaľovač](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window#Drop-Down_navigator_mode)

Ak boli v Predvoľbách vypnuté označenia pre Navigátor, tento ovládací prvok rozbaľovacieho zoznamu Kategória sa stane najširším objektom. Jeho šírka obmedzuje, ako úzko môže byť bočný panel zmenený. Tento ovládací prvok môžete nechať zmiznúť pomocou Správcu zásuvných modulov, aby ste skryli (alebo odstránili) všetky okrem jediného preferovaného režimu *bočného panela* Navigátora. (Ak zostane neskrytý iba jeden režim, nie je potrebné používať menu a to sa tiež skryje.) {{-}}

### **Režim navigátora Kategória** (predvolený)

![[_media/Navigator-mode-selection-category-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Kategória (predvolený) režim navigátora]]

Bočný panel kategórie - Bočný panel umožňujúci výber kategórií pohľadu. {{-}}

### Režim navigátora **Rozpínač**

![[_media/Navigator-mode-selection-expander-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Režim navigátora Rozpínač]]

Bočný panel Rozpínač - Výber zobrazení zo zoznamov pomocou rozpínačov šípok. {{-}}

### Režim navigátora **Rozbaľovač**

![[_media/Navigator-mode-selection-drop-down-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Režim navigátora Rozbaľovač]]

Bočný panel Rozbaľovač - Výber kategórií a zobrazení z rozbaľovacích zoznamov. {{-}}

## Prepínanie kategórií

Gramps obsahuje niekoľko rôznych štandardných [kategórií Pohľadu](wiki:Gramps_Glossary#viewcategory), z ktorých každá má jeden alebo viac štandardných [režimov Pohľadu](wiki:Gramps_Glossary#viewmode). Vstavané kategórie sú opísané v úvode [Kategórií navigátora](wiki:Gramps_6.0_Wiki_Manual_-_Categories#Categories_of_the_Navigator).

Spôsob zmeny aktuálne zobrazenej kategórie závisí od režimu navigátora. Za normálnych okolností (pre väčšinu režimov navigátora) môžete požadovanú kategóriu vybrať kliknutím na jednu z ikon navigátora.

Prípadne môžete použiť [klávesové skratky](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings#4). a ( a na Macu) prejsť na ďalšiu, resp. predchádzajúcu kategóriu alebo použiť [klávesové skratky](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings#45) ( na Macu) Skratky sú k dispozícii len pre prvých 10 kategórií (napr. kategórie Archívy/Médiá/Poznámky chýbajú.) Ak ste skryli [Navigátor](wiki:Gramps_5._1_Wiki_Manuál_-_Main_Window#Navigator), potom budú skratky jediným spôsobom zmeny kategórií, kým znovu[nezapnete Navigátor](wiki:Gramps_6.0_Wiki_Manuál_-_Navigatin#View). {{-}}

## Prepínanie pohľadov

[Kategória pohľadu](wiki:Gramps_Glossary#kategória_pohľadu) môže obsahovať rôzne spôsoby prezentácie údajov, nazývané [režim pohľadu](wiki:Gramps_Glossary#režim_pohľadu). Ak existuje niekoľko režimov zobrazenia, môžete medzi nimi interaktívne prepínať. Spôsob prepínania medzi režimami závisí od kategórie pohľadu. Možnosti konfigurácie pre každý režim sa ovládajú nezávisle.

V pohľadoch štylizovaných do tabuliek údajov s riadkami a stĺpcami sa režimy zvyčajne pohybujú medzi hierarchicky zoskupeným náčrtom alebo jednoduchým jednoúrovňovým triedeným zoznamom. Režimy pohľadu v štýle tabuliek sa konfigurujú pomocou [Editora stĺpcov](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Column_Editor) a majú možnosti [zoradenia](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Sorting_columns).

V niektorých grafických pohľadoch kategórií (ako napríklad [Grafy](wiki:Gramps_6.0_Wiki_Manual_-_Categories#Charts_Category) a [Zemepis](wiki:Gramps_6.0_Wiki_Manual_-_Categories#Geography_Category)) môžu byť rôzne režimy zobrazenia.

![[_media/Navigator-mode-selection-expander-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Bočný panel navigátora v režime Rozpínač]]Ak existuje viacero režimov zobrazenia, budú na paneli nástrojov ďalšie tlačidlá ikon na prepínanie medzi týmito rôznymi režimami zobrazenia.

Prepínať môžete aj prostredníctvom menu alebo menu Pohľad [klávesové skratky](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings#6) stlačením (pre Linux a Windows) alebo } (pre MacOS), kde *<číslo>* zodpovedá poradiu režimov zobrazenia uvedených v menu kategórie Pohľadu.

Režimy je možné vyberať aj z bočného panela Navigátor pri použití usporiadania Rozbaľovač alebo Rozpínač. V bočnom paneli Navigátora je predvolené [usporiadanie Kategória](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window#Prepínanie_režimov_Navigátora), ktoré nemá žiadny výber režimu. Použitie režimu Rozbaľovača alebo Rozpínača sprístupní ďalšie režimy zobrazenia ako ikony Navigátora. {{-}}

## Filtre

![[_media/PeopleCategory-sidebar-filter-enabled-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Zobrazené ovládacie prvky filtra]]

Genealogické databázy môžu obsahovať informácie o ***mnohých*** osobách, rodinách, miestach a objektoch. To znamená, že je možné, aby Pohľad obsahoval taký dlhý zoznam údajov, že je ťažké sa v ňom orientovať. Okrem základného [Nájsť políčko](wiki:Gramps_6.0_Wiki_Manual_-_Navigation/sk#Hľadanie_záznamov) *vyhľadávania podľa typu* na presnú navigáciu v zozname vám Gramps poskytuje dva rôzne prostriedky na filtrovanie zoznamu na zvládnuteľnejšiu veľkosť.

Tieto metódy sú **Vyhľadávanie** a **Filtrovanie**.

Vyľadávanie prehľadáva text zobrazený v zozname, zatiaľ čo filtre zobrazujú ľudí, ktorých údaje zodpovedajú kritériám filtra.

Vyhľadávanie je jednoduchá, ale rýchla metóda prehľadávania stĺpcov zobrazených na obrazovke. Keď [bočný panel](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window/sk#Spodný_panel_a_bočný_panel) nie je **zobrazený**, zobrazí sa . Zadaním znakov do a kliknutím na tlačidlo sa zobrazia len riadky, ktoré zodpovedajú textu.

Prípadne môžete zapnúť filter buď v [spodnom paneli alebo bočnom paneli](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window/sk#Spodný_panel_a_bočný_panel). Keď je zobrazený bočný panel filtra, sa nezobrazuje. Filter umožňuje interaktívne vytvoriť súbor pravidiel filtrovania, ktoré možno aplikovať na zobrazenie. Filter sa aplikuje na základe pravidiel a údajov, nie na základe zobrazenia na obrazovke. Filtre zobrazenej kategórie je možné zostaviť aj kliknutím na príslušné tlačidlo "editor" v menu .

Ďalšie podrobnosti o fungovaní filtrov sú uvedené v [kapitole Filtre](wiki:Gramps_6.0_Wiki_Manual_-_Filters/sk).

{{-}}

Keď Gramps otvorí Rodinný strom, žiadne filtrovanie sa neuplatňuje. Napríklad v pohľade Ľudia sú predvolene uvedené všetky osoby v Rodinnom strome.

## Riešenie problémov s nesprávne fungujúcim rozhraním

Ak sa vaše grafické rozhranie Gramps správa inak, ako je popísané v tejto príručke, môže ísť o problém s inštaláciou alebo menší problém s kompatibilitou.

Je pravdepodobné, že takéto správanie sa už vyskytlo a bolo nájdené riešenie.

Pozrite si prosím [Stránky s riešením problémov](wiki::Category:Troubleshooting). Ak sa vám tam nepodarí objaviť riešenie, pošlite opis problému všeobecnej komunite Gramps na náš [user maillist](wiki:Contact#Mailing_lists). Tam si navzájom neustále pomáhame. {{-}}

[Category:Sk:Documentation](wiki:Category:Sk:Documentation) [Visual Guide to the Gramps Interface](wiki:Category:Sk:Gramps_terminology)
