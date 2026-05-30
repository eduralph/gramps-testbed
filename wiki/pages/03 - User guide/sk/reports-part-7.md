---
title: Gramps 6.0 Wiki Manual - Reports - part 7/sk
categories:
- Plugins
- Sk:Documentation
- Stub
managed: false
source: wiki-scrape
wiki_revid: 117788
wiki_fetched_at: '2026-05-30T20:23:23Z'
lang: sk
---

{{#vardefine:chapter\|13.7}} {{#vardefine:figure\|0}} Naspäť na [Register správ](wiki:Gramps_6.0_Wiki_Manual_-_Reports/sk).

<hr>

{{-}} ![[_media/MenuOverview-Reports-WebPages-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}}  Prehľad ponuky]] V tejto časti sú popísané zostavy , Naratívna webová stránka a Webový kalendár ako súčasť rôznych zostáv dostupných v programe Gramps.

## Webové stránky

### <u>Prehľadná webová stránka</u>

![[_media/NarratedWebSite-WebPages-Individuals-index-page-example-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Rozprávané webové sídlo - Webové stránky - Stránka jednotlivcov - predvolený výstup HTML - príklad]]

Správa Narrated Web Site (Rozprávaná webová stránka) generuje webovú stránku (t. j. súbor prepojených webových stránok), pre súbor vybraných jednotlivcov a poskytuje používateľovi možnosti, ktoré umožňujú širokú škálu prispôsobení. Túto zostavu môžete spustiť cez ponuku .

Správa Narrated Web Site (Rozprávané webové sídlo) vytvára stránky, ktoré dôsledne dodržiavajú odporúčania World Wide Web Consortium’ pre XHTML 1.0 Strict a CSS 1. Tieto odporúčania zahŕňajú oddelenie obsahu od prezentácie. Vďaka tomuto postupu možno štýl a vzhľad nových webových stránok úplne ovládať z jedného súboru štýlov CSS bez toho, aby sa museli meniť jednotlivé stránky.

Na poskytnutie ďalších informácií, napríklad rodinnej histórie, možno pridať úvodné stránky.

Genealogické záznamy môžu generovať veľa súborov. Mnohé webové servery majú problém s veľkým počtom súborov v jednom adresári. Správa Narrated Web sa snaží udržať počet súborov v jednom adresári na zvládnuteľnej úrovni. Na tento účel sa vytvára hierarchia adresárov. Vygenerované názvy súborov nie sú intuitívne, ale sú jedinečné pre každú osobu. Pri ďalších spusteniach sa vygenerujú identické názvy súborov, čo uľahčuje aktualizáciu konkrétnych súborov.

<span id="HTML kód">**Poznámky typu HTML kód**</span>

''V tejto podkapitole sa slovo **značka** nevzťahuje na značky Gramps, ale na formátovacie značky HTML!

Poznámky nastavené na typ **HTML kód**' [typ](wiki:Gramps_6.0_Wiki_Manuál_-_Vkladanie_a_editácia_údajov:_detail_-_časť_2#typ_poznámky) sa vložia pod objekt, ku ktorému sú pripojené. To umožňuje špeciálne

Kúsky HTML musia byť dobre formované, so všetkými značkami správne uzavretými, aby sa predišlo konfliktom so zvyškom webovej stránky generovanej správou. Do poznámky typu **HTML kód** vkladajte iba značky, ktoré by sa za normálnych okolností nachádzali v tele dokumentu HTML.

The following tags will always be ignored: `html`, `meta`, `doctype`, `head`, `meta`, `title`, `link`, `script`, `body`

all other tags will be available : `i`, `a`, `p`, `ol`, `ul`, `div`, `h1`-`h7`, `button`, `svg`, `table`, `tr`, `td`, …

{{-}}

#### Dialog tabs

The report dialog has the following tabs: {{-}}

##### Report Options

![[_media/NarratedWebSite-WebPages-ReportOptions-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Narrated Web Site - Web Pages - Report Options - tab default options]]

- { (Začiarkávacie políčko v predvolenom nastavení nezačiarknuté) Ak máte problémy s prenosom súborov na externého webového hostiteľa, môžete vytvoriť jeden tar súbor s gzipom, aby ste mohli údaje ľahšie nahrať. Veľký počet súborov a adresárov v tomto webovom výstupe môže spôsobiť ťažkosti pri prenose súborov na externého webového hostiteľa. Program Gramps má možnosť uložiť všetky vaše súbory Narrative Web do jedného komprimovaného archívu pomocou formátov gzip a tar (neformálne známeho ako ‘tarball’). Tento jediný súbor môžete rýchlo preniesť na server a rozkomprimovať na hostiteľovi webovej stránky. ****

- } (`~/yourhomedirectory/`<názov rodokmeňa>`+NAVWEB` predvolené) Cieľový adresár pre webové súbory.

- (`My Family Tree` predvolené) Názov webového sídla. V tejto možnosti môžete zadať vlastný názov stránky. .

- (Každá osoba, ktorá vyhovuje tomuto filtru a nie je vylúčená z dôvodu pravidiel ochrany osobných údajov, bude zahrnutá do výstupu.

  - **Celá databáza** (predvolené nastavenie)
  - Rodiny potomkov aktívnej osoby
  - Predkovia aktívnej osoby
  - Osoby so spoločným predkom s aktívnou osobou

- Centrálna osoba pre správu. (predvolené nastavenie je Aktívna osoba)

  -  (predvolene nezačiarknuté políčko) - Pre každú stránku osoby.

- Ako zaobchádzať so živými ľuďmi. Môžete kontrolovať zobrazovanie citlivých informácií na základe toho, či osoba je alebo nie je aktuálne nažive. Keďže však Gramps je výskumný nástroj, je pravdepodobné, že vo vašej databáze sú osoby bez známeho dátumu úmrtia. Na odvodenie toho, či je jednotlivec *pravdepodobne ešte nažive*, používa Gramps algoritmus, ktorý porovnáva dátumy úmrtia, dátumy narodenia, dátumy krstu/krstu, dátumy úmrtia predkov a dátumy narodenia predkov. Algoritmus predpokladá, že každý jednotlivec je "pravdepodobne stále nažive", pokiaľ porovnávané dátumy neznemožňujú, aby bol jednotlivec "pravdepodobne nažive".

  - **Vylúčiť** – (Predvolené nastavenie) Vylúči všetky informácie o všetkých jednotlivcoch, ktorí sú *[pravdepodobne ešte nažive](wiki:Gramps_6.0_Wiki_Manual_-_Probably_Alive/sk)*
  - **Zahrnúť len priezvisko**
  - **Zahrnúť iba celé meno**
  - **Zahrnúť** – Zahrnúť všetky informácie o všetkých osobách, aj keď sú *pravdepodobne ešte nažive*

- (<kód>30</kód> predvolené) Táto možnosť je neaktívna, ak je možnosť "Žijúci ľudia" nastavená na **Zahrnúť**'.

- : Či sa majú zahrnúť súkromné objekty. Ak je vaším zámerom poskytnúť úplný záznam o vašom výskume, zaškrtnutím tohto políčka sa spolu so zvyškom databázy zahrnú všetky záznamy označené ako **súkromné**. (v predvolenom nastavení políčko nie je začiarknuté)

{{-}}

##### HTML Options

![[_media/NarratedWebSite-WebPages-HTMLOptions-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Naratívny web - Webové stránky - Možnosti Html - predvolené možnosti záložky]]

- Prípona, ktorá sa má použiť pre webové súbory.

  - **.html** (Predvolené)
  - .htm
  - .shtml
  - .php
  - .php3
  - .cgi

- (**Štandardné autorské práva** predvolené) Pri vytváraní verejnej webovej stránky je dôležité určiť podmienky autorských práv, za ktorých zverejňujete svoje údaje. Medzinárodné autorské právo vyhradzuje všetky práva na vaše údaje podľa vášho uváženia. Údaje vlastníte vy a jednotlivci musia mať vaše povolenie, ak chcú tieto údaje opätovne použiť. V genealogickom výskume je zdieľanie údajov s inými bádateľmi bežnou praxou. Medzi ďalšie možnosti patria licencie Creative Commons, ktoré ponúkajú širokú škálu obmedzení použitia alebo neponúkajú žiadne. Viac informácií o licenciách Creative Commons nájdete na adrese <http://creativecommons.org/>.

- Gramps poskytuje sedem vstavaných súborov štýlov, z ktorých si môžete vybrať na určenie vzhľadu alebo vašich webových stránok. Vyberte si medzi **Základným** (jaseň, modrá, cyprus, lila, broskyňa alebo smrek), **Mainz** alebo **Nebraska** štýly. K dispozícii je aj možnosť nezahrnúť súbor štýlov (**Bez súboru štýlov**). Bez ohľadu na to, aký štýl si vyberiete, súbor štýlov sa nachádza v súbore *`css/narrative-screen.css`*. Tento súbor môžete upravovať, aby ste si ďalej prispôsobili vzhľad svojich webových stránok. Ak vykonáte úpravy v súbore štýlov, majte na pamäti, že pri regenerácii stránok s rovnakým výstupným cieľom sa prepíše váš vlastný súbor štýlov. Ak chcete zachovať svoj vlastný súbor štýlov pri ďalších aktualizáciách webových stránok, vyberte . Ak chcete vlastný súbor štýlov, môžete skopírovať jeden z existujúcich súborov štýlov v *\$HOME/.gramps/css/*. Tento adresár neexistuje. Musíte ho vytvoriť pred skopírovaním svojho budúceho súboru štýlov. Zmeňte jeho názov. Ak požiadate o novú správu, tento nový súbor štýlov bude pridaný do zoznamu už existujúcich súborov štýlov.

- Vyberte, aké rozloženie má mať navigačné menu. (K dispozícii len pre vybrané súbory štýlov)

  - **Horizontálne -- predvolené**
  - Vertikálne -- ľavá strana
  - Fade -- iba prehliadače [Webkit](https://en.wikipedia.org/wiki/WebKit)
  - Rozbaľovací panel -- iba prehliadače Webkit

- Určuje predvolené rozvrhnutie sekcie odkazov na citácie na zdrojovej stránke

  - **Normálny štýl osnovy** (predvolené nastavenie)
  - Rozbaľovací zoznam -- len pre prehliadače Webkit

- : Začiarknutím tohto políčka sa na stránke s podrobnosťami každého jednotlivca’zahrnie graf predkov, ak má definovaných predkov vo vašej databáze. (políčko je predvolene začiarknuté) ( Poznámka: [Vytvára kompaktné stromy predkov pomocou Buchheimovho/Walkerovho algoritmu](wiki:Poznámky_k_návrhu_stromu_predkov_na_webovej_stránke))

  - Počet zobrazených generácií môžete zmeniť v záložke *[Generácie:](wiki:Gramps_6.0_Wiki_Manuál_-_Zprávy_-_časť_7#Zobrazenie)*.

-  (predvolene nezačiarknuté políčko) - pridá odkazy do navigačného panela.

-  (začiarkávacie políčko v predvolenom nastavení nezačiarknuté)

{{-}}

##### Zobraziť

![[_media/NarratedWebSite-WebPages-Display-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Naratívny web - Webové stránky - Zobrazenie - predvolené možnosti karty]]

- Vyberte formát zobrazenia názvov. Vyberte si z možností **Priezvisko, prípona** / Given Surname Suffix / Given / Main Surnames, Given Patronymic Suffix / SURNAME, Given (Common)

- \- Preklad, ktorý sa má použiť v správe.

- \- Formát a jazyk pre dátumy s príkladmi.

- \- Voľba určuje, či sa má vo výstupe webovej stránky skryť alebo zobraziť identifikátor Gramps ID objektov.

  - **Neobsahovať** (predvolené)
  - Zahrnúť

- (predvolene nezačiarknuté políčko) - či sa majú deti zobrazovať v poradí podľa narodenia alebo v poradí podľa zápisu?

- }(zaškrtávacie políčko predvolene nezačiarknuté) - Či sa má v zozname miest zobrazovať zemepisná šírka/dĺžka?

- (začiarkávacie políčko je predvolene nezačiarknuté) - Triediť odkazy na miesta podľa dátumu alebo podľa názvu. Nenastavené znamená podľa dátumu.

- :Táto možnosť je neaktívna, ak nie je začiarknutá možnosť *[Include ancestor graph](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_7/sk#Html_options)* na karte *Html options*. Predvolený počet generácií zobrazených v grafoch predkov je `4` s možnosťami 2, 3, 4 alebo 5. Jedinci znázornení v grafoch predkov sú tí istí jedinci, ktorých informácie sú uvedené na iných miestach vašich webových stránok.

- (predvolene začiarkávacie políčko začiarknuté) - nezačiarknuté ich zobrazí hneď pred atribútmi.

{{-}}

##### Page Generation

![[_media/NarratedWebSite-WebPages-PageGeneration-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Naratívny web - Webové stránky - Generovanie stránok - predvolené možnosti záložky]]

Záložka *Generovanie stránok* poskytuje možnosti pre vytvorenie bežne očakávaných doplnkových webových stránok & anotácií spoločných pre všetky webové stránky v rámci celej generovanej webovej stránky.

Prvé možnosti slúžia na ovládanie generovania troch doplnkových stránok: **Home** ([Home](https://en.wikipedia.org/wiki/Home_page) webová stránka), **Introduction** ([FAQ](https://wikipedia.org/wiki/FAQ#In_web_design) alebo [About Us](https://www.searchenginejournal.com/about-us-page-examples/250967/amp/) webová stránka) a **Publisher Contact** ([Contact Us](https://wikipedia.org/wiki/Contact_page) webová stránka).

Ku každej z doplnkových stránok možno priradiť konkrétnu položku [Media](wiki:Gramps_Glossary#media) alebo [Note](wiki:Gramps_Glossary#note). V predvolenom nastavení nie je týmto stránkam priradený žiadny obsah (ani médiá, ani text z poznámky).

Obsah týchto stránok ***must*** pochádza z položiek Médiá alebo Poznámky, ktoré boli vytvorené pred spustením správy. Po pridaní požadovaných položiek do stromu ich budete môcť vybrať zo zoznamu objektov Poznámky alebo Médiá.

- Zobrazí individuálnu poznámku podľa vášho výberu.

- Zobrazí individuálny mediálny objekt podľa vášho výberu.

- Zobrazte individuálnu poznámku podľa vášho výberu.

- Zobrazí individuálny mediálny objekt podľa vášho výberu.

- Zobrazte individuálnu poznámku podľa vášho výberu.

- Zobrazte individuálny mediálny objekt podľa vášho výberu.

- Zobrazte individuálnu poznámku podľa vlastného výberu. Tento text poznámky sa zobrazí priamo pod názvom stránky na každej webovej stránke.

- Zobrazí individuálnu poznámku podľa vášho výberu. Tento text anotácie sa zobrazí v pätičke nad vyhlásením o autorských právach na každej webovej stránke.

{{-}}

##### Dalšie stránky

![[_media/NarratedWebSite-WebPages-ExtraPages-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Naratívny web - Webové stránky - Extra stránky - predvolené možnosti záložky]]

- (prázdne) - Váš názov extra stránky, ako sa zobrazuje v paneli ponúk.

- (prázdne) - Vaša cesta k extra stránke bez prípony.

  - 

{{-}}

##### Generovanie obrázkov

![[_media/NarratedWebSite-WebPages-ImageGeneration-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Narrated Web Site - Web Pages - Image Generation - tab default options]]

- { Táto možnosť určuje, či sa má na webovej stránke zahrnúť/vylúčiť galéria mediálnych objektov. (začiarkavacie políčko je predvolene začiarknuté)

-  Táto možnosť určuje, či sa má na vašej webovej lokalite zahrnúť/vylúčiť galéria nepoužitých mediálnych objektov. (v predvolenom nastavení je začiarkavacie políčko začiarknuté)

-  : Táto možnosť umožňuje vytvárať na stránke médií iba miniatúry namiesto obrázkov v plnej veľkosti. Umožní vám to oveľa menšiu celkovú veľkosť nahraných obrázkov na webovú hostingovú lokalitu. (v predvolenom nastavení nie je začiarkavacie políčko začiarknuté)

- (<kód>800</kód> predvolené nastavenie) Umožňuje nastaviť maximálnu šírku obrázka (v pixeloch) zobrazeného na stránke médií. Nastavte na 0, aby ste nemali žiadne obmedzenie.

- (`600` predvolené) Umožňuje nastaviť maximálnu výšku obrázka (v pixeloch) zobrazeného na stránke médií. Nastavte na 0 pre žiadny limit.

{{-}}

![[_media/wiki:Ako_vytvoriť_obrázkové_referenčné_oblasti|[_media/NarrativeWeb-Media-tab-ImageReferenceRegions-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Príklad [obrázkové referenčné oblasti]] - Záložka Médiá výstupu HTML pre správu "Naratívny web"]]

Všimnite si, že [image reference regions](wiki:How_to_create_image_reference_regions) sa zobrazujú aj na HTML stránkach Narrative Web vytvorených pomocou programu Gramps. Pre túto funkciu nie sú potrebné žiadne špeciálne možnosti okrem existencie referenčných oblastí pre 1 alebo viac obrázkov. Narrative Web zobrazuje referenčné oblasti len pre osoby a objekty miesta. {{-}}

##### Stiahnutie

![[_media/NarratedWebSite-WebPages-Download-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Naratívny web - Webové stránky - Stiahnutie - predvolené možnosti karty]]

- : Či sa má zahrnúť možnosť stiahnutia databázy. (zaškrtávacie políčko v predvolenom nastavení nie je začiarknuté)

- } Vyberte súbor, ktorý sa má použiť na stiahnutie databázy.

- } (<kód>Smith Family Tree</kód> predvolené) Uveďte popis tohto súboru.

- Vyberte súbor, ktorý sa má použiť na stiahnutie databázy.

- (`Johnson Family Tree` predvolené) Uveďte popis tohto súboru.

{{-}}

##### Rozšírené možnosti

![[_media/NarratedWebSite-WebPages-AdvancedOptions-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Naratívny web - Webové stránky - Rozšírené možnosti - predvolené možnosti karty]]

Tieto nastavenia sa týkajú množstva informácií zobrazených na webových stránkach s podrobnými informáciami o priezvisku a individuálnym indexom.

- Kódovanie, ktoré sa má použiť pre webové súbory.

  - **Unicode UTF-8 (odporúčané)** (predvolené)
  - ISO-8859-1 *- [ISO/IEC štandard znakovej sady:](https://wikipedia.org/wiki/ISO/IEC_8859) Časť 1 (Latin 1: Západoeurópska)*
  - ISO-8859-2
  - ISO-8859-3
  - ISO-8859-4
  - ISO-8859-5
  - ISO-8859-6
  - ISO-8859-7
  - ISO-8859-8
  - ISO-8859-9
  - ISO-8859-10
  - ISO-8859-13
  - ISO-8859-14
  - ISO-8859-15
  - koi8_r ''- [Kod Obmena Informatsiey, 8 bit ("Kód pre výmenu informácií - 8 bitov")''](https://wikipedia.org/wiki/KOI8-R)

- : (Ak majú webovú stránku) (začiarkávacie políčko je štandardne nezačiarknuté)

-  (štandardne začiarknuté políčko)

-  (políčko je štandardne nezačiarknuté)

- (štandardne políčko nezačiarknuté)

- (políčko je štandardne nezačiarknuté)

- (políčko je štandardne nezačiarknuté)

{{-}}

##### Include

![[_media/NarratedWebSite-WebPages-Include-tab-52.png|Obrázok {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Naratívny web - Webové stránky - Zahrnúť - predvolené možnosti karty]]

- (štandardne políčko nezačiarknuté)

- (políčko je štandardne nezačiarknuté)

- (políčko je štandardne nezačiarknuté)

- (štandardne políčko nezačiarknuté)

- (štandardne políčko nezačiarknuté)

- . Táto možnosť vytvorí súbor GENDEX umiestnený na začiatku webovej stránky. Môžete si pozrieť stránky, ktoré tento formát podporujú, a prečítať si o ňom viac v článku [GENDEX na Wikipédii](http://en.wikipedia.org/wiki/GENDEX).(zaškrtávacie políčko v predvolenom nastavení nezačiarknuté)

- (predvolene nezačiarknuté políčko)

- (políčko je predvolene nezačiarknuté)

{{-}}

##### Miestna mapa Možnosti

![[_media/NarratedWebSite-WebPages-PlaceMapOptions-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Naratívna webová stránka - Webové stránky - Možnosti mapy miesta - predvolené možnosti karty]]

- } Vyberte si mapovú službu na vytvorenie stránok mapy miesta

  - **OpenStreetMap** (predvolené)
  - Google : Aby táto možnosť fungovala, je potrebné zadať . Ak chcete oň požiadať, prejdite na platformu Google maps ( <https://cloud.google.com/maps-platform/> ) a vyberte položku "Get Started" (v pravom hornom rohu) a postupujte podľa pokynov (môžu zahŕňať kreditnú kartu) a potom vyberte možnosť "Credentials" (Poverenia) v ponuke "API Manager" (Správca API) . Potom kliknite na tlačidlo "Create Credentials" (Vytvoriť poverenia) v okne "Credentials" (Poverenia). V ďalšom vyskakovacom okne kliknite na položku "API Key" (Kľúč API). Skopírujte vygenerovaný kľúč API do schránky a vložte ho do poľa Gramps "Google maps API key:". Dôrazne odporúčam, aby ste sa po vygenerovaní a umiestnení správy online vrátili na platformu Google Maps a klikli na tlačidlo "Obmedziť kľúč" vo vytvorenom okne API a pridali svoju doménu (to zabráni tomu, aby iné webové stránky uniesli váš kľúč API a prinútili vás platiť! Tieto nové zmeny v rozhraní API Google Maps vstúpili do platnosti od 11. júna 2018. pozri cenovú tabuľku <https://cloud.google.com/maps-platform/pricing/sheet/> "Každý mesiac tiež získate opakujúci sa kredit vo výške 200 dolárov na svojom fakturačnom účte, ktorý kompenzuje vaše náklady na používanie, a môžete si nastaviť limity používania na ochranu pred neočakávaným zvýšením nákladov."

- : (v predvolenom nastavení políčko nie je začiarknuté)

- : Či sa má alebo nemá pridať mapa jednotlivých stránok zobrazujúca všetky miesta na tejto stránke. To vám umožní vidieť, ako vaša rodina cestovala po krajine. (v predvolenom nastavení políčko nezačiarknuté)

- } Vyberte možnosť, ktorú chcete mať pre stránky s rodinnými mapami Google Maps...

  - **Rodinné odkazy** (predvolené)
  - Kvapka
  - Značky

- 

{{-}}

##### Ďalšie začlenenie (CMS, webový kalendár, Php)

![[_media/NarratedWebSite-WebPages-OtherInclusionCMSWebCalendarPHP-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Rozprávané webové sídlo - webové stránky - iné začlenenie (CMS, webový kalendár, Php) - predvolené možnosti záložky]]

-  (Zaškrtávacie políčko v predvolenom nastavení nie je začiarknuté)
  - `/NAVWEB` (predvolené nastavenie) - Kam umiestnite svoju webovú stránku ?

<!-- -->

-  (Zaškrtávacie políčko v predvolenom nastavení nie je začiarknuté)

  - `/WEBCAL` (predvolené) - Kam umiestnite svoju webovú stránku ?

{{-}} Pozrite si tiež:

- [Howto:_Make_a_genealogy_website_with_Gramps#Integration_of_NarrativeWeb_in_a_CMS_or_MVS](wiki:Howto:_Make_a_genealogy_website_with_Gramps#Integration_of_NarrativeWeb_in_a_CMS_or_MVS)
- Žiadosť o funkciu Integrácia naratívneho webu do CMS alebo MVC

{{-}}

#### Výstupné údaje o vzorovom webovom sídle

Nasledujúce časti zobrazujú predvolený vzhľad webových stránok správy Naratívna webová stránka. {{-}}

##### Home

(voliteľná stránka) {{-}}

##### Introduction

(nepovinná stránka) {{-}}

##### Individuals

(predvolená stránka) {{-}}

##### Priezvisko

(predvolená stránka) {{-}}

##### Rodiny

(voliteľná stránka) {{-}}

##### Udalosti

(nepovinná stránka) {{-}}

##### Miesto

(predvolená stránka) {{-}}

##### Zdroje

(predvolená stránka) {{-}}

##### Repositories

(voliteľná stránka) {{-}}

##### Media

(predvolená stránka) {{-}}

##### Thumbnails

(predvolená stránka) {{-}}

##### Sťahovanie

(voliteľná stránka) {{-}}

##### Adresár

(nepovinná stránka) {{-}}

##### Kontakt

(nepovinná stránka) {{-}}

### <u>Webový kalendár</u>

![[_media/WebCalendar-WebPages-example-DecemberCalendar2018-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Správa o webovom kalendári - webové stránky - predvolený kalendár na december 2018 - výstup HTML]]

Webový kalendár zobrazuje udalosti pre vybrané osoby v súbore mesačných kalendárov. Túto zostavu môžete spustiť prostredníctvom ponuky .

K dispozícii sú možnosti filtrovania osôb, výberu rokov, ktoré sa majú zahrnúť (štandardne je zahrnutý len aktuálny rok); či sa majú zahrnúť len žijúce osoby a či sa majú zahrnúť narodeniny alebo výročia alebo oboje; na mesačných stránkach sa môžu zahrnúť poznámky a skrátené stránky.

Správa je navrhnutá tak, aby spolupracovala s [Narrative Web Site Report](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_7#Narrated_Web_Site). Na každej stránke sa nachádza odkaz "Domov", ktorý vedie na domovskú stránku správy Narrative Web Site Report (Správa o naratívnom webovom sídle). K dispozícii je aj možnosť zahrnúť odkazy z osôb v kalendári na tú istú osobu na Narrated Web Site (Naratívnom webovom sídle).

Práca so správou Narrated Web Site Report (Rozprávaná webová stránka) vyžaduje, aby používateľ vytvoril tieto dve správy kompatibilným spôsobom. Neexistuje žiadna automatická kontrola, či sú tieto dve správy kompatibilné. Ak stránky nie sú kompatibilné, používateľovi sa pravdepodobne zobrazí chyba "Stránka nebola nájdená".

Kompatibilita závisí od:

1.  Zahrnutí tých istých osôb do oboch správ,
2.  uložení stránok v kompatibilných adresároch.

Na zahrnutie rovnakých osôb do oboch správ by sa mali použiť rovnaké filtre a podobné možnosti, pokiaľ ide o zahrnutie žijúcich osôb (webový kalendár nemá možnosť odstrániť "súkromné" informácie).

V predvolenom nastavení je správa o webových stránkach s rozprávaním uložená v adresári "`~/`<Názov rodokmeňa>`+NAVWEB`" a v predvolenom nastavení je webový kalendár uložený v adresári "`~/`<Názov rodokmeňa>`+WEBCAL`". Ak sa tieto predvolené nastavenia zachovajú, rôzne odkazy by mali fungovať správne. Ak boli adresáre zmenené, potom bude potrebné zodpovedajúcim spôsobom zmeniť "Domovský odkaz" v časti "Možnosti obsahu" a "Predpona odkazu" v časti "Rozšírené možnosti".

Ak sa má webový kalendár používať bez pridruženej webovej lokality Narrative Web Site, potom by sa mal text v položke "Home link" (Domovský odkaz) v časti "Content Options" (Možnosti obsahu) vymazať, aby sa zabezpečilo, že sa nevytvorí žiadny odkaz "Home".

#### Záložky dialógu

Dialógové okno správy Webový kalendár má päť záložiek, z ktorých každá je preskúmaná nižšie. {{-}}

##### Možnosti správy

![[_media/WebCalendar-WebPages-ReportOptions-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Webový kalendár - Webové stránky - Možnosti zostavy - predvolené možnosti záložky]]

- `~/yourhomedirectory/`<názov rodokmeňa>`+WEBCAL` Cieľový adresár pre webové súbory.

- (`My Family Calendar` predvolené) Názov kalendára.

- vyberte medzi

  - **Celá databáza** (predvolené nastavenie)
  - Potomkovia aktívnej osoby
  - Rodiny potomkov aktívnej osoby
  - Predkovia aktívnej osoby
  - Ľudia so spoločným predkom s aktívnou osobou

- Centrálna osoba pre filter. (Predvolené: Aktívna osoba)

- Prípona, ktorá sa má použiť pre webové súbory.

  - **.html** (Predvolené)
  - .htm
  - .shtml
  - .php
  - .php3
  - .cgi

- Autorské práva, ktoré sa majú použiť pre webové súbory.

  - **Štandardný copyright** (predvolené nastavenie)
  - Creative Commons - podľa autorstva
  - Creative Commons - podľa autorstva, bez odvodenín
  - Creative Commons - Podľa autorstva, Zdieľať podobné
  - Creative Commons - Podľa autorstva, Nekomerčné
  - Creative Commons - Podľa autorstva, Nekomerčné, Bez odvodenín
  - Creative Commons - Na základe autorstva, Nekomerčné, Zdieľanie a pod.
  - Bez upozornenia na autorské práva

- Súbor štýlov, ktorý sa má použiť pre webové stránky.

  - **Basic-Ash** (predvolené nastavenie)
  - Basic-Blue
  - Basic-Cypress
  - Basic-Lilac
  - Basic-Peach
  - Basic-Spruce
  - Mainz
  - Nebraska
  - Bez štýlového listu
  - Zrakovo postihnutí

{{-}}

##### Možnosti správy (2)

![[_media/WebCalendar-WebPages-ReportOptions2-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Webový kalendár - Webové stránky - Možnosti správy (2) - predvolené možnosti záložky]]

- \- Vyberte formát zobrazenia mien. Tento výber sa zvyčajne preberá z predvoleného nastavenia v [Upraviť &gt; Zobrazenie](wiki:Gramps_6.0_Wiki_Manual_-_Settings/sk#Zobrazenie) záložke . Alebo ak chcete prepísať toto nastavenie pre správu, vyberte z:

  - **Predvolené** - (v novom rodokmeni je to zvyčajne *Priezvisko, daná prípona* )
  - Priezvisko, daná prípona
  - Daná prípona priezviska
  - Dané priezvisko
  - Hlavné priezviská, daná patronymická prípona
  - Priezvisko, dané (bežné)

-  (predvolene nezačiarknuté políčko)

-  (políčko je predvolene začiarknuté)

- Preklad, ktorý sa má použiť pre správu. Výber jazyka zobrazujúci všetky jazyky podporované programom Gramps. Predvolené nastavenie je jazyk, v ktorom používate program Gramps.

- Formát a jazyk pre dátumy s príkladmi.

  - Predvolené - Vyberte túto možnosť, ak chcete použiť predvolené nastavenie v [Edit &gt; Display](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Display) na karte .
  - **RRRR-MM-DD(ISO)(2018-03-14)** (predvolené pre správu)
  - Číselný(14/3/2018)
  - Mesiac Deň, Rok(14. marec 2018)
  - DEŇ MESIACA, ROK(14.3.2018)
  - Deň Mesiac Rok(14. marec 2018)
  - DEŇ MESIAC ROK(14. marca 2018)

{{-}}

##### Možnosti obsahu

![[_media/WebCalendar-WebPages-ContentOptions-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Webový kalendár - Webové stránky - Možnosti obsahu - predvolené možnosti karty]]

-  (predvolene nezačiarknuté políčko)

  - (predvolené nastavenie je aktuálny rok)

  - (Predvolené nastavenie je aktuálny rok)

- Vyberte krajinu, v ktorej sa zobrazia súvisiace sviatky. (Predvolené nastavenie je prázdne)

- Vyberte prvý deň v týždni pre kalendár. (Predvolené: **Nedeľa**)

- Vyberte zobrazené priezvisko vydatej ženy.

  - **Manželky používajú svoje vlastné priezvisko** (Predvolené nastavenie)
  - Manželky používajú manželovo priezvisko (z prvej uvedenej rodiny)
  - Manželky používajú manželovo priezvisko (z poslednej uvedenej rodiny)

- (**`../../Family Tree 1_NAVWEB/index.html`** predvolené) Odkaz, ktorý sa má uviesť, aby používateľa presmeroval na hlavnú stránku webového sídla.

{{-}}

##### Jan - Jun Poznámky

![[_media/WebCalendar-WebPages-Jan-JunNotes-tab-52.png|Obrázok {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Webový kalendár - Webové stránky - Poznámky január-jún - predvolené možnosti záložky]]

Vyberte existujúcu poznámku pre daný mesiac.

- 

- 

- 

- 

- 

- 

{{-}}

##### Jul - Dec Poznámky

![[_media/WebCalendar-WebPages-Jul-DecNotes-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Webový kalendár - Webové stránky - Poznámky k júlu a decembru - predvolené možnosti karty]]

Vyberte existujúcu poznámku pre daný mesiac:

- }

- }

- 

- 

- 

- 

{{-}}

##### Rozšírené možnosti

![[_media/WebCalendar-WebPages-AdvancedOptions-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Webový kalendár - Webové stránky - Rozšírené možnosti - predvolené možnosti karty]]

- Kódovanie, ktoré sa má použiť pre webové súbory

  - **Unicode UTF-8 (odporúčané)** (predvolené)
  - ISO-8859-1
  - ISO-8859-2
  - ISO-8859-3
  - ISO-8859-4
  - ISO-8859-5
  - ISO-8859-6
  - ISO-8859-7
  - ISO-8859-8
  - ISO-8859-9
  - ISO-8859-10
  - ISO-8859-13
  - ISO-8859-14
  - ISO-8859-15
  - koi8_r

-  (predvolene nezačiarknuté políčko)

-  (políčko je predvolene začiarknuté)

-  (políčko je predvolene začiarknuté)

-  (políčko je predvolene nezačiarknuté)

  - **`../../Family Tree 1_NAVWEB/`** Predpona na odkazoch, ktorá vás presmeruje na nahovorenú webovú správu.

{{-}}

#### Príklad výstupu z webového sídla

{{-}}

<hr>

Naspäť na [Register správ](wiki:Gramps_6.0_Wiki_Manual_-_Reports/sk).

[Category:Sk:Documentation](wiki:Category:Sk:Documentation) [Category:Plugins](wiki:Category:Plugins)
