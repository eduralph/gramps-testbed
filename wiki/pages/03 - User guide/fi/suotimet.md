---
title: Fi:Gramps 6.0 Wiki-käyttöohje - Suotimet
categories:
- Fi:Dokumentaatio
- Filters
- Stub
managed: false
source: wiki-scrape (html-fallback)
wiki_revid: 127086
wiki_fetched_at: '2026-05-30T18:29:27Z'
lang: fi
---

|  |  |  |
|:---|:--:|---:|
| <a href="/wiki/index.php/Gramps_6.0_Wiki_Manual_-_Settings/fi" class="mw-redirect" title="Gramps 6.0 Wiki Manual - Settings/fi"><strong>Edellinen</strong></a> | [**Hakemisto**](wiki:Fi:Gramps_6.0_Wiki-k%C3%A4ytt%C3%B6ohje) | <a href="/wiki/index.php/Gramps_6.0_Wiki_Manual_-_FAQ/fi" class="mw-redirect" title="Gramps 6.0 Wiki Manual - FAQ/fi"><strong>Seuraava</strong></a> |

<div class="LanguageLinks">

|  |  |  |
|----|----|----|
| ![[_media/Gramps-config-language.png]] | **[Languages](wiki:Portal:Translators):**  | [English](wiki:Gramps_6.0_Wiki_Manual_-_Filters)     • <span lang="da"><a href="/wiki/index.php/Gramps_6.0_Wiki_Manual_-_Filters/da" class="mw-redirect" title="Gramps 6.0 Wiki Manual - Filters/da">dansk</a></span>  • <span lang="de"><a href="/wiki/index.php/Gramps_6.0_Wiki_Manual_-_Filters/de" class="mw-redirect" title="Gramps 6.0 Wiki Manual - Filters/de">Deutsch</a></span>  • <span lang="es"><a href="/wiki/index.php/Gramps_6.0_Wiki_Manual_-_Filters/es" class="mw-redirect" title="Gramps 6.0 Wiki Manual - Filters/es">español</a></span>  • <span lang="fi"><a href="/wiki/index.php/Gramps_6.0_Wiki_Manual_-_Filters/fi" class="mw-redirect" title="Gramps 6.0 Wiki Manual - Filters/fi">suomi</a></span>  • <span lang="fr"><a href="/wiki/index.php/Gramps_6.0_Wiki_Manual_-_Filters/fr" class="mw-redirect" title="Gramps 6.0 Wiki Manual - Filters/fr">français</a></span>  • <span lang="he">[עברית](wiki:Gramps_6.0_Wiki_Manual_-_Filters/he)</span>      • <span lang="mk"><a href="/wiki/index.php/Gramps_6.0_Wiki_Manual_-_Filters/mk" class="mw-redirect" title="Gramps 6.0 Wiki Manual - Filters/mk">македонски</a></span>   • <span lang="nl"><a href="/wiki/index.php/Gramps_6.0_Wiki_Manual_-_Filters/nl" class="mw-redirect" title="Gramps 6.0 Wiki Manual - Filters/nl">Nederlands</a></span>      • <span lang="ru"><a href="/wiki/index.php/Gramps_6.0_Wiki_Manual_-_Filters/ru" class="mw-redirect" title="Gramps 6.0 Wiki Manual - Filters/ru">русский</a></span>   • <span lang="sq"><a href="/wiki/index.php/Gramps_6.0_Wiki_Manual_-_Filters/sq" class="mw-redirect" title="Gramps 6.0 Wiki Manual - Filters/sq">shqip</a></span>   • <span lang="sk">[slovenčina](wiki:Gramps_6.0_Wiki_Manual_-_Filters/sk)</span>   • <span lang="tr">[Türkçe](wiki:Gramps_6.0_Wiki_Manual_-_Filters/tr)</span> |

</div>

  

<div class="thumb tright">

<div class="thumbinner" style="width:398px;">

![[_media/DefineFilter-dialog-default-60.png]]

<div class="thumbcaption">

<div class="magnify">

<a href="/wiki/index.php/File:DefineFilter-dialog-default-60.png" class="internal" title="Enlarge"></a>

</div>

Fig. 14.1 **<span class="kbd" style="background:#D3D3D3; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">[Define filter](wiki:Gramps_6.0_Wiki_Manual_-_Filters#Define_Filter_dialog)</span>** - dialog - default

</div>

</div>

</div>

Listaa kaikki tällä hetkellä Grampsiin määritetyt suodinsäännöt. Ne ovat käytettävissä, kun luodaan Käyttäjän suotimia.

Säännöt on listattu kategorioittain.

- [<span class="tocnumber">1</span> <span class="toctext">Suodin vs. Haku</span>](#Suodin_vs._Haku)
- [<span class="tocnumber">2</span> <span class="toctext">Säännölliset lausekkeet</span>](#S.C3.A4.C3.A4nn.C3.B6lliset_lausekkeet)
  - [<span class="tocnumber">2.1</span> <span class="toctext">Ryhmät ja Sarjat</span>](#Ryhm.C3.A4t_ja_Sarjat)
  - [<span class="tocnumber">2.2</span> <span class="toctext">Esimerkkejä</span>](#Esimerkkej.C3.A4)
    - [<span class="tocnumber">2.2.1</span> <span class="toctext">Sukunimen vaihtelut</span>](#Sukunimen_vaihtelut)
    - [<span class="tocnumber">2.2.2</span> <span class="toctext">Säännöllisten ryhmien testaus</span>](#S.C3.A4.C3.A4nn.C3.B6llisten_ryhmien_testaus)
- [<span class="tocnumber">3</span> <span class="toctext">Käyttäjän suotimet</span>](#K.C3.A4ytt.C3.A4j.C3.A4n_suotimet)
  - [<span class="tocnumber">3.1</span> <span class="toctext">Kategoriakohtainen suotimien rakennusikkuna</span>](#Kategoriakohtainen_suotimien_rakennusikkuna)
    - [<span class="tocnumber">3.1.1</span> <span class="toctext">Suotimen testin ikkuna</span>](#Suotimen_testin_ikkuna)
  - [<span class="tocnumber">3.2</span> <span class="toctext">Suotimen määrittely ikkuna</span>](#Suotimen_m.C3.A4.C3.A4rittely_ikkuna)
  - [<span class="tocnumber">3.3</span> <span class="toctext">Lisää sääntö ikkuna</span>](#Lis.C3.A4.C3.A4_s.C3.A4.C3.A4nt.C3.B6_ikkuna)
- [<span class="tocnumber">4</span> <span class="toctext">Suotimet kateorioittain</span>](#Suotimet_kateorioittain)
- [<span class="tocnumber">5</span> <span class="toctext">Esivanhempien suotimet</span>](#Esivanhempien_suotimet)
- [<span class="tocnumber">6</span> <span class="toctext">Lapsisuotimet</span>](#Lapsisuotimet)
- [<span class="tocnumber">7</span> <span class="toctext">Citation/source filters</span>](#Citation.2Fsource_filters)
  - [<span class="tocnumber">7.1</span> <span class="toctext">Lainaus/lähde kategoria</span>](#Lainaus.2Fl.C3.A4hde_kategoria)
  - [<span class="tocnumber">7.2</span> <span class="toctext">Perheet kategoria</span>](#Perheet_kategoria)
  - [<span class="tocnumber">7.3</span> <span class="toctext">Tapahtumat kategoria</span>](#Tapahtumat_kategoria)
  - [<span class="tocnumber">7.4</span> <span class="toctext">Paikat kategoria</span>](#Paikat_kategoria)
  - [<span class="tocnumber">7.5</span> <span class="toctext">Media kategoria</span>](#Media_kategoria)
- [<span class="tocnumber">8</span> <span class="toctext">Jälkeläissuodattimet</span>](#J.C3.A4lkel.C3.A4issuodattimet)
- [<span class="tocnumber">9</span> <span class="toctext">Tapahtumasuotimet</span>](#Tapahtumasuotimet)
  - [<span class="tocnumber">9.1</span> <span class="toctext">Henkilöitä koostavat suotimet</span>](#Henkil.C3.B6it.C3.A4_koostavat_suotimet)
  - [<span class="tocnumber">9.2</span> <span class="toctext">Families Category</span>](#Families_Category)
- [<span class="tocnumber">10</span> <span class="toctext">Family filters</span>](#Family_filters)
- [<span class="tocnumber">11</span> <span class="toctext">Father filters</span>](#Father_filters)
- [<span class="tocnumber">12</span> <span class="toctext">General filters</span>](#General_filters)
  - [<span class="tocnumber">12.1</span> <span class="toctext">Persons-, and Relationship Category</span>](#Persons-.2C_and_Relationship_Category)
  - [<span class="tocnumber">12.2</span> <span class="toctext">Families Category</span>](#Families_Category_2)
  - [<span class="tocnumber">12.3</span> <span class="toctext">Events Category</span>](#Events_Category)
  - [<span class="tocnumber">12.4</span> <span class="toctext">Places Category</span>](#Places_Category)
  - [<span class="tocnumber">12.5</span> <span class="toctext">Sources Category</span>](#Sources_Category)
  - [<span class="tocnumber">12.6</span> <span class="toctext">Citations Category</span>](#Citations_Category)
  - [<span class="tocnumber">12.7</span> <span class="toctext">Repositories Category</span>](#Repositories_Category)
  - [<span class="tocnumber">12.8</span> <span class="toctext">Media Category</span>](#Media_Category)
  - [<span class="tocnumber">12.9</span> <span class="toctext">Notes Category</span>](#Notes_Category)
- [<span class="tocnumber">13</span> <span class="toctext">Mother filters</span>](#Mother_filters)
- [<span class="tocnumber">14</span> <span class="toctext">Position filters</span>](#Position_filters)
- [<span class="tocnumber">15</span> <span class="toctext">Source filters</span>](#Source_filters)
- [<span class="tocnumber">16</span> <span class="toctext">Relationship filters</span>](#Relationship_filters)
- [<span class="tocnumber">17</span> <span class="toctext">Tagging</span>](#Tagging)
  - [<span class="tocnumber">17.1</span> <span class="toctext">New Tag dialog</span>](#New_Tag_dialog)
    - [<span class="tocnumber">17.1.1</span> <span class="toctext">Tagging a selection of objects</span>](#Tagging_a_selection_of_objects)
  - [<span class="tocnumber">17.2</span> <span class="toctext">Organize Tags Window</span>](#Organize_Tags_Window)
  - [<span class="tocnumber">17.3</span> <span class="toctext">Tag selection dialog</span>](#Tag_selection_dialog)
  - [<span class="tocnumber">17.4</span> <span class="toctext">Usage of tags</span>](#Usage_of_tags)
    - [<span class="tocnumber">17.4.1</span> <span class="toctext">Filtering</span>](#Filtering)
    - [<span class="tocnumber">17.4.2</span> <span class="toctext">Tagit sarake</span>](#Tagit_sarake)

## <span id="Suodin_vs._Haku" class="mw-headline">Suodin vs. Haku</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Gampsissa haetaan tietoja kahdella tavalla: Hae and Suodata. Haku käyttää listanäkymän (kuten Henkilöt, Perheet jne) yläpuolella olevaa palkkia. Suodinta voi käyttää haun keralla tai yksinään Sivu- ja Alapalkeissa. Haku Yläpalkissa näkyy vain, jos Sivupalkki on suljettu kokonaan. Sivu- ja Alalkin voi sulkea/avata valinnalla **-\> Näytä**.

Haku ja Suodin toimivat aivan eri tavoin. On hyödyllistä ymmärtää niiden erot:

- *Etsi* - yläpalkin haku kohdistuu näytössä oleviin riveihin ja sarakkeisiin. Esimerkiksi jos Asetuksissa on Näyttö\>Nimen asetukset-kohdassa valittuna "Sukunimi, Etunimi", silloin haku "Smith, J" toimii ja näyttää sen mukaiset rivit. Nimen asetuksen muutoksella voit käyttää esim. hakuehtoa "John Smith". Haku-toiminnallisuutta käytetään todennäköisesti useimmiten, koska se on suoraviivaisin, mutta siinä on rajoitteensa (katso alla).

<div class="thumb tright">

<div class="thumbinner" style="width:452px;">

![[_media/MainWindow-SearchBar-sidebar-hidden-example-60.png]]

<div class="thumbcaption">

<div class="magnify">

<a href="/wiki/index.php/File:MainWindow-SearchBar-sidebar-hidden-example-60.png" class="internal" title="Enlarge"></a>

</div>

Fig. 14.2 Grampsin pääikkuna näyttää Haku-palkin

</div>

</div>

</div>

- *Suodin* - Suotimet ovat monimutkaisempi kokonaisuus. Ne eivät rajoitu vain mitä näkyy näytöllä, vaan kohdistuvat kaikkeen tietoaineistoon sukupuussa. Nimi-suodin hakee osumia nimen osilla (etunimi, sukunimi, etuliite jne) ensisijaisessa ja vaihtoehtoisissa henkilön nimissä, mutta et voi rajoittaa hakua joko ensi- tai toissijaiseen nimeen. Esim. jos hakuehto on "John", osumiin tulevat ehnkilöt, joilla on se etunimenä tai sukunimessä. Etunimen ja Sukunimen ehtojen yhdistelmään on käytettävä myös Käyttäjäsuodinta.

<div class="thumb tright">

<div class="thumbinner" style="width:372px;">

![[_media/Sidebar-PeopleTreeView-Filter-TagDropDownList-example-60.png]]

<div class="thumbcaption">

<div class="magnify">

<a href="/wiki/index.php/File:Sidebar-PeopleTreeView-Filter-TagDropDownList-example-60.png" class="internal" title="Enlarge"></a>

</div>

Fig. 14.3 Grampsin Suodin-sivupalkki - Tagien listaus esimerkkinä

</div>

</div>

</div>

Suotimia ja luodaan ja hallinnoidaan valinnalla **Muokkaa -\> ..suodin muokkain** tai sivu- ja alapalkin erityisellä grampletilla (laajennuksella). Suodin-grampletilla voi tehdä Yläpalkin kaltaisia pikasuotimia, mutta ne toimivat tässä kuvatulla erolla.

Eräitä lisänäkökohtia:

- Suodin hakee vaihtoehtoisistakin nimistä; Haku kohdistuu vain näytössä oelviin ensisijaisiin nimiin. Tämän johdosta et välttämättä löydä kaikkia "Smithejä". Kuitenkin havaitset henkilön muokkaimessa, että hänellä on "Smith" vaihtoehtoisissa nimissä.
- Suodin sallii "säännöllisten sääntöjen" "regular expressions" käytön. Voit niiden avulla esim. löytää nimet, jotka alkavat B-kirjaimella ja päättyvät "ship" tekstiin. Tätä mahdollisuutta ei ole yläpalkin haussa.
- The Haku kohdistuu vain siihen, mikä on näkyvissä. Jos nimi tai teksti on liian iso näkymään kokonaan listassa, silloin et löydä sen avulla. Tämä on syytä pitää mielessä etenkin Lisätietojen hauissa. Parasta onkin käyttää suotimia lisätietojen ja muiden pitkien tekstikenttien hakemisessa.
- Kaikki suotimet ovat tarkkoja kirjainten koolle; "Ship" ei löydä "ship", "SHIP" tai "ShIp" arvoja.

Enemmän tietoja suodinten laatimisesta [Example filters](wiki:Example_filters).  

## <span id="Säännölliset_lausekkeet"></span><span id="S.C3.A4.C3.A4nn.C3.B6lliset_lausekkeet" class="mw-headline">Säännölliset lausekkeet</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

<a href="https://fi.wikipedia.org/wiki/Säännöllinen_lauseke" class="external text" rel="nofollow">Säännölliset lausekkeet</a>(ts. *regex*) ovat nopea ja voimakas tapa mallintaa tekstiä, jota käytämme suotimissa.

- <div style="float:left; width:.9em; height:.9em; margin-right:0.5em; vertical-align:-.1em; border:1px solid #111; background:#666;">

  </div>

  <span style=""></span>**<span class="kbd" style="background:#D3D3D3; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">Käytä säännöllisiä lausekkeita</span>** valinnan täytyy olla päällä.

Esimerkiksi, jos haet sukunimeä, joka alkaa "B" kirjaimella ja päättyy tekstiin "ship", voit käyttää säännöölistä lauseketta sen kuvaamiseen. Näin: **`^B.*ship`**:

- **`^B`** ilmaisee tekstin alkavan B:llä
- **`.`** vastaa mitä tahansa merkkiä (kirjainta, numeroa tai muuta)
- **`*`** vastaa nollaa tai useaa edellistä (tässä tapauksessa mitä tahansa yksittäistä merkkiä)
- **`ship`** vastaa nimettyjä merkkejä s, h, i, p ja tässä järjestyksessä.

Säännölliset lausekkeet ovat melko vahvoja ja niillä on monia vaihtoehtoja. Me käytämme Python Regular Expression systeemiä ja dokumentoimme sen tässä. Voit käyttää lisäksi mitä tahansa siihen liittyvää resurssia.

*whitespace* - "whitespace" käsite vastaa alempana yhtä tai useampaa merkkiä, jota et näe. Esim, whitespace kattaa tabulaattorit, välilyönnit ja rivinvaihdot.

Joillakin merkeillä on erityinen merkitys säännöllisissä lausekkeissa. Ne ovat:

- **`. ^ $ * + ? { } [ ] \ | ( )`**

Niitä käytetään näin:

- '`.`' kuvaa mitä tahansa symbolia eli merkkiä (kirjainta, numeroa tai muuta)
- '`^`' kuvaa tekstin alkua
- '`$`' kuvaa tekstin loppua
- '`*`' toisto, edeltävä symboli 0-n kertaa

<!-- -->

- '`+`' toisto, edeltävä symboli 1-n kertaa
- '`?`' toisto, edeltävä symboli 0-1 kertaa (tekee vaihtoehtoiseksi)
- '`{`' - kuvaa osumien lukumäärän
- '`}`' - päättää osumien lukumäärän
- '`[`' - merkkiluokan alku
- '`]`' - merkkiluokan loppu
- '`\`' - seuraava merkki on erityinen järjestys
- '`|`' - tai (vaihtelun symboli)
- '`(`' - ryhmän alku
- '`)`' - ryhmän loppu

Eräät yhdistelmät (ns. pakoluokat), jotka alkavat '`\`' kuvaavat usein hyödyllisiä ennalta määriteltyjä merkkien joukkoja. Näitä ovat mm. lukujen sarjat, kirjainten sarjat tai sarja, joka ei ole whitespace. Seuraavat esimääritetyt joukot ovat niiden tarjolla olevia osajoukkoja.

- `\d` mikä tahansa numero eli on sama kuin luokka `[0-9]`.
- `\D` äskeisen vastakohta; mikä tahansa ei-numero eli on sama kuin luokka `[^0-9]`.
- `\s` mikä tahansa tyhjä merkki (esim. välilyönti tai tabulaattori) on sama kuin luokka `[ \t\n\r\f\v]`.
- `\S` äskeisen vastakohta; mikä tahansa ei-tyhjä merkki eli on sama kuin luokka `[^ \t\n\r\f\v]`.
- `\w` mikä tahansa aakkonen a-z, numero tai alaviiva \_. eli on sama kuin luokka `[a-zA-Z0-9_]`.
- `\W` äskeisen vastakohta; mikä tahansa muu kuin aakkonen a-z, numero tai alaviiva eli on sama kuin luokka `[^a-zA-Z0-9_]`.

Monimutkaisin toistettu määrite on `{m,n}`, jossa `m` ja `n` ovat kokonaislukuja. Tämä määrittää, että toistoja on vähintään `m` ja enintään `n`.

### <span id="Ryhmät_ja_Sarjat"></span><span id="Ryhm.C3.A4t_ja_Sarjat" class="mw-headline">Ryhmät ja Sarjat</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Ryhmät merkitään '`('` ja'`)`' operaatiomerkeillä. '`(`' ja '`)`' merkinnöillä on pitkälti sama merkitys kuin matematiikassa; ne ryhmittävät niiden sisällä olevat ilmaukset ja voit toistaa ryhmän sisältöä toiston määritteillä kuten `*, +, ?, tai {m,n}`. Esim. `(ab)*` vastaa 0-n toistoa `ab` ryhmälle.

Sarjat merkitään '`[`' ja '`]`' operaatiomerkeillä.

Voit ajatella ryhmiä '`|`' operaatiomerkillä erotettujen vaihtoehtojen joukkona, jossa jokainen vaihtoehto koostuu yhdestä, useasta tai nollasta merkistä ja sarjoja vaihtoehtojen joukkona, jossa jokainen vaihtoehto on yksittäinen merkki.

### <span id="Esimerkkejä"></span><span id="Esimerkkej.C3.A4" class="mw-headline">Esimerkkejä</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

- **`^B.*ship$`** - vastaa tekstejä, jotka alkavat '`B`', seuraten millä tahansa ja päättyen '`ship`'.
  - vastaa: **`Blankenship`**, **`Blueship`**, **`Beeship`**
  - ei vastaa: **`Blankenships`**
- **`^B.*ship`** - vastaa tekstejä, jotka alkavat '`B`', seuraten millä tahansa ja seuraten '`ship`' (voi olla muutakin sen jälkeen).
  - vastaa: **`Blankenship`**, **`Blankenships`**, **`Blueship`**, **`Blueshipman`**, **`Beeship`**, **`Beeshipness`**
  - ei vastaa: **`Blankenschips`**

#### <span id="Sukunimen_vaihtelut" class="mw-headline">Sukunimen vaihtelut</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Esimerkki 1  
Käyttämällä **`Eri(ch|ck|k|c)(ss|s)on`** seuraavat vastaavuudet osuvat

<!-- -->

    Erikson
    Eriksson
    Ericson
    Ericsson
    Erickson
    Ericksson
    Erichson
    Erichsson

**Selitys**: Johtuen seuraavista

- **`Eri`** = Eri
- **`(ch|ck|k|c)`** = ryhmittää **`ch`**, **`ck`**, **`k`** tai **`c`**. Yrittää ottaa ensiksi pisimmän vastaavuuden
- **`(ss|s)`** = ryhmittää**`ss`** tai**`s`**. Yrittää ottaa ensiksi pisimmän vastaavuuden
- **`on`** = on

------------------------------------------------------------------------

Esimerkki 2  
Käyttämällä **`Ba(in|yn|m|n)bri(dge|cke|g(g|e|))`** seuraavat vastaavuudet osuvat

<!-- -->

    Bainbricke
    Bainbridge
    Bainbrig
    Bainbrigg
    Bambridge
    Banbrig
    Banbrige
    Baynbrige

**Selitys:** Johtuen seuraavista

- **`Ba`** = Ba
- **`(in|yn|m|n)`** = ryhmittää **in**, **yn**, **m** tai **n**. Yrittää ottaa ensiksi pisimmän vastaavuuden.
- **`bri`** = bri
- **`(dge|cke|g(g|e|))`** = ryhmittää **dge**, **cke** or (**g** ja**g**, **g** ja**e** tai**g** ilman paria)

------------------------------------------------------------------------

Esimerkki 3  
Käyttämällä **`n(es|oua|oai|o[iya]|a[iy])r(r|)(on|((e|)au(x|t|d|lt|)))`** seuraavat vastaavuudet osuvat

<!-- -->

    nairaud
    nairault
    naireaud
    nayrault
    nesrau                
    nesrault
    nesreau
    nesreaud
    noirau
    noiraud
    noirauld
    noirault
    noiraut
    noiraux
    noireau
    noireaud
    noireault
    noireaut
    noirraux
    noirreau
    noirreaud
    nouarault
    noyraud
    noyrault 

**Selitys:** Johtuen seuraavista

- **`n`** = n
- **`(es|oua|oai|set1|set2)`** = ryhmittää **es**, **oua**, **oai**, **set1** tai **set2**
- **`set1`** on **`o[iya]`** = on sarja **o** JA **i**, **y** or **a**. Toisin sanoen **oi**, **oy** tai **oa**
- **`set2`** on **`a[iy]`** = on sarja **a** JA **i** or **y**. Toisin sanoen **ai** or **ay**
- **`r`** = r
- **`(r|)`** = ryhmittää **r** tai ei mitään
- **`(on|(subgroup1)`** = ryhmittää **on** tai **subgroup1**.
- **subgroup1** on ryhmä (**subgroup2 au subgroup3**)
- **subgroup2** on **(e\|)** = on ryhmä **e** or nothing
- **`au`** = au
- **subgroup3** is **(x\|t\|d\|lt)** = on ryhmä **x**, **t**, **d** or **lt**

#### <span id="Säännöllisten_ryhmien_testaus"></span><span id="S.C3.A4.C3.A4nn.C3.B6llisten_ryhmien_testaus" class="mw-headline">Säännöllisten ryhmien testaus</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Apuneuvoja säännöllisten lausekkeiden testaamiseen löytyy googlaamalla. <a href="http://www.regexr.com/" class="external free" rel="nofollow">http://www.regexr.com/</a> on helppo ja käytännöllinen.

## <span id="Käyttäjän_suotimet"></span><span id="K.C3.A4ytt.C3.A4j.C3.A4n_suotimet" class="mw-headline">Käyttäjän suotimet</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

<table style="width:80%;margin-top:+.7em;margin-bottom:+.7em;background-color: #ffeeaa85;border:1px solid #ccc; padding: 5px" data-align="center">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 60px">![[_media/Gnome-important.png]]</td>
<td><div style="font-size:110%">
<strong>Käyttäjän suotimien siirto</strong>
</div>
<hr />
<p>Välttääksesi ei-toivottuja seuraamuksia Grampsin pääversion korotuksen yhteydessä (esim. versiosta 3.2.x versioon 6.0.x), voit tarvittaessa kopioida itse tiedostosi <em>custom_filter.xml</em> kansiosta <a href="/wiki/index.php/Gramps_User_Directory" class="mw-redirect" title="Gramps User Directory">Gramps User Directory</a> uuteen <em>gramps_version_number</em>.</p></td>
</tr>
</tbody>
</table>

Jo käyttämällä sivupalkin suotimia Henkilöt, Tapahtumat, Paikat näkymissä voit tehdä merkittävän määrän suodatuksia henkilöille, tapahtumille, paikoille jne. Huomaa kuitenkin, että 'säännöllisten lauseiden' valinta **toimii vain sarakkeissa**, jotka ovat mukana näkymässä.

Jos sivupalkin suotimet eivät riitä tarpeeseesi, on sinun rakennettava käyttäjän suotimia.

### <span id="Kategoriakohtainen_suotimien_rakennusikkuna" class="mw-headline">Kategoriakohtainen suotimien rakennusikkuna</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

<table style="width:80%;margin-top:+.7em;margin-bottom:+.7em;background-color: #ddffcc85;border:1px solid #ccc; padding: 5px" data-align="center">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 60px">![[_media/Gramps-notes.png]]</td>
<td><div style="font-size:110%">
<strong>Huomattavaa:Suotimien muutokset</strong>
</div>
<hr />
<p>Suotimiin tehdyt muutokset astuvat voimaan vasta kun suljet sen määrittelyikkunan <kbd style="border: 1px solid; color:#5e4638; background-color: #f9f9f9; border-bottom-width: 2px; -moz-border-radius: 3px; -webkit-border-radius: 3px; border-radius: 3px; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">OK</kbd> painikkeella.</p></td>
</tr>
</tbody>
</table>

<div class="thumb tright">

<div class="thumbinner" style="width:400px;">

![[_media/PersonFilters-dialog-example-50.png]]

<div class="thumbcaption">

<div class="magnify">

<a href="/wiki/index.php/File:PersonFilters-dialog-example-50.png" class="internal" title="Enlarge"></a>

</div>

Fig. 14.4 Esimerkki Henkilön suodin-ikkunasta

</div>

</div>

</div>

Luodaksesi uuden tai nähdäksesi aikaisemmat käyttäjän suotimet käytä **<span class="kbd" style="background:#D3D3D3; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">*kategoriannimi* suotimet</span>** listaa jossa *kategoriannimi* muuttuu sen mukaan, missä kategorissa olet. Esim.:

- Henkilösuotimet
- Perhesuotimet
- Tapahtumasuotimet
- Paikkasuotimet
- Lähdesuotimet
- Mediasuotimet
- Arkistosuotimet
- Lisätietosuotimet
- Lainaussuotimet

**Muokkaa\>** *valinnassa on alimpana **<span class="kbd" style="background:#D3D3D3; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;"></span>*****kategorianimi *suodin*** *kohta, josta avautuvassa ikkunassa on oikeassa reunassa kuvakkeet:*

- <span class="kbd" style="border: 1px solid; color:#5e4638; background-color: #f9f9f9; border-bottom-width: 2px; -moz-border-radius: 3px; -webkit-border-radius: 3px; border-radius: 3px; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">+ (Lisää sääntö suotimeen)</span> painike avaa **<span class="kbd" style="background:#D3D3D3; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">Määritä suodin</span>** ikkunan, jossa lisätä uusi käyttäjäsuotimesi.
- <span class="kbd" style="border: 1px solid; color:#5e4638; background-color: #f9f9f9; border-bottom-width: 2px; -moz-border-radius: 3px; -webkit-border-radius: 3px; border-radius: 3px; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">Muokkaa valittua sääntöä</span> painike avaa **<span class="kbd" style="background:#D3D3D3; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">Muokkaa sääntöä</span>** ikkunan, jossa päivität aikaisempaa käyttäjäsuodintasi.
- <span class="kbd" style="border: 1px solid; color:#5e4638; background-color: #f9f9f9; border-bottom-width: 2px; -moz-border-radius: 3px; -webkit-border-radius: 3px; border-radius: 3px; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">Kopioi valittu suodin</span> tekee tarkan kopion valitusta suotimesta.
- <span class="kbd" style="border: 1px solid; color:#5e4638; background-color: #f9f9f9; border-bottom-width: 2px; -moz-border-radius: 3px; -webkit-border-radius: 3px; border-radius: 3px; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">Testaa valittua suodinta</span> avaa **<span class="kbd" style="background:#D3D3D3; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">Suodintesti</span>** ikkunassa listan, jossa näkyy tai ei näy suodatustuloksia.
- <span class="kbd" style="border: 1px solid; color:#5e4638; background-color: #f9f9f9; border-bottom-width: 2px; -moz-border-radius: 3px; -webkit-border-radius: 3px; border-radius: 3px; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">Poista valittu suodin</span>

  

#### <span id="Suotimen_testin_ikkuna" class="mw-headline">Suotimen testin ikkuna</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

<div class="thumb tright">

<div class="thumbinner" style="width:452px;">

![[_media/FilterTest-results-for-TestTheSelectedFilter-button-example-50.png]]

<div class="thumbcaption">

<div class="magnify">

<a href="/wiki/index.php/File:FilterTest-results-for-TestTheSelectedFilter-button-example-50.png" class="internal" title="Enlarge"></a>

</div>

Fig. 14.5 Suotimen testi - tuloslistan esimerkki henkilösuotimista

</div>

</div>

</div>

The **<span class="kbd" style="background:#D3D3D3; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">Suotimen testi</span>** ikkunan tuloslistassa voi näkyä tuloksia tai ei riippuen suotimesi osuvuudesta.  

### <span id="Suotimen_määrittely_ikkuna"></span><span id="Suotimen_m.C3.A4.C3.A4rittely_ikkuna" class="mw-headline">Suotimen määrittely ikkuna</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

<div class="thumb tright">

<div class="thumbinner" style="width:398px;">

![[_media/DefineFilter-dialog-default-60.png]]

<div class="thumbcaption">

<div class="magnify">

<a href="/wiki/index.php/File:DefineFilter-dialog-default-60.png" class="internal" title="Enlarge"></a>

</div>

Fig. 14.6 Määrittely suodin - ikkuna- oletusmuodossa

</div>

</div>

</div>

**<span class="kbd" style="background:#D3D3D3; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">Määrittele suodin</span>** ikkunassa voi määrittää käyttäjäsuotimia, joilla valitaan henkilöt rarpotteja, vientiä ja muita työkaluja ja apuneuvoja varten. Tämä mahdollisuus on itse asiassa hyvin tehokas työkalu sukututkimuksen analyyseissa.

Listataksesi aikaisemmin määrittelemäsi suotimet (jos niitä on) avaa **<span class="kbd" style="background:#D3D3D3; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">Määritä suodin</span>** ikkuna:

- Sivupalkin alaosassa
- useimmissa kategorioissa valinnalla **Muokkaa\> *kategoriannimi* suotimen muokkain** , joka avaa **<span class="kbd" style="background:#D3D3D3; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">*kategoriannimi* suotimet</span>** ikkunan. Siinä on valittavana <span class="kbd" style="border: 1px solid; color:#5e4638; background-color: #f9f9f9; border-bottom-width: 2px; -moz-border-radius: 3px; -webkit-border-radius: 3px; border-radius: 3px; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">+ (Lisää sääntö suotimeen)</span> painike tai <span class="kbd" style="border: 1px solid; color:#5e4638; background-color: #f9f9f9; border-bottom-width: 2px; -moz-border-radius: 3px; -webkit-border-radius: 3px; border-radius: 3px; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">Muokkaa valittua suodinta</span> painike.

**Määrittely** osioon syötetään **<span class="kbd" style="background:#D3D3D3; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">Nimi:</span>** uudelle suotimellesi ja lisätään **<span class="kbd" style="background:#D3D3D3; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">Kommentti:</span>** se auttaa erottamaan tämän suotimen tulevaisuudessa. Lisää tarvitsemasi määrä sääntöjä **<span class="kbd" style="background:#D3D3D3; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">Sääntölistaan</span>** käyttämällä <span class="kbd" style="border: 1px solid; color:#5e4638; background-color: #f9f9f9; border-bottom-width: 2px; -moz-border-radius: 3px; -webkit-border-radius: 3px; border-radius: 3px; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">+</span> painiketta.

Jos suotimessa on enemmän kuin yksi sääntö, **<span class="kbd" style="background:#D3D3D3; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">Asetukset</span>** -pudotusvalikosta voi valita

- **Kaikkia sääntöjä noudatettava**(oletus)
- Ainakin yhden säännön toteuduttava
- Vain yhden säännön toteuduttava

I, kun suodin hakee osumia. Pudotusvalinnalla ei ole vaikutusta, jos sääntöjä on vain yksi.

- Valitse
  <div style="float:left; width:.9em; height:.9em; margin-right:0.5em; vertical-align:-.1em; border:1px solid #111; background:#EEE;">

  </div>

  <span style=""></span> **<span class="kbd" style="background:#D3D3D3; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">Listaa vain arvot jotka eivät täsmää suodinsääntöihin</span>** kääntääksesi suotimen säännön. Esimerkiksi, **"on yhteinen esi-isä I1:lle"** sääntö käännettynä täsmää henkilöihin, jotka eivät ole hänen esi-isiään). (Valintaruutu ei ole oletusarvoisesti päällä)

  

### <span id="Lisää_sääntö_ikkuna"></span><span id="Lis.C3.A4.C3.A4_s.C3.A4.C3.A4nt.C3.B6_ikkuna" class="mw-headline">Lisää sääntö ikkuna</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

<table style="width:80%;margin-top:+.7em;margin-bottom:+.7em;background-color: #c0f0ff85;border:1px solid #ccc; padding: 5px" data-align="center">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 60px">![[_media/Tango-Dialog-information.png]]</td>
<td><div style="font-size:110%">
<strong>Suodintasi voidaan käyttää toisen suotimen sisältämänä suotimena.</strong>
</div>
<hr />
<p>Tämä antaa lähes rajoittaman joustavuuden rakentaa suotimia, esim. vertailla henkilökohtaisia tapahtumia.<br />
Katso: <a href="/wiki/index.php/Example_filters" title="Example filters">Example filters</a></p></td>
</tr>
</tbody>
</table>

  

<div class="thumb tright">

<div class="thumbinner" style="width:452px;">

![[_media/AddRule-selector-dialog-PersonFilters-example-60.png]]

<div class="thumbcaption">

<div class="magnify">

<a href="/wiki/index.php/File:AddRule-selector-dialog-PersonFilters-example-60.png" class="internal" title="Enlarge"></a>

</div>

Fig. 14.7 Lisää sääntö - valintaikkuna - käytettävissä henkilösuotimille - esimerkki

</div>

</div>

</div>

Uusi suodin lisätään <span class="kbd" style="border: 1px solid; color:#5e4638; background-color: #f9f9f9; border-bottom-width: 2px; -moz-border-radius: 3px; -webkit-border-radius: 3px; border-radius: 3px; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">+ (Lisää sääntö suodattimeen)</span> painikkeesta **<span class="kbd" style="background:#D3D3D3; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">Määrittele suodin</span>** ikkunassa, mikä avaa **<span class="kbd" style="background:#D3D3D3; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">Lisää sääntö</span>** ikkunan.

Vasemmassa palstassa ovat käytettävissä olevat säännöt, ryhmiteltynä aihealueittain. Ryhmät laajenevat ja supistuvat kolmio-kuvakkeestaan.

Sääntö lisätään seuraavasti:

- Napsauta sopivan aihealueen kolmio-kuvaketta.
- Valitse puusta sääntö napsauttamalla sen nimeä. Oikeassa palstassa näytetään säännön nimi, kuvaus ja mahdolliset arvokentät.

Kun olet tyytyväinen sääntöösi ja sen arvokenttien arvoihin, napsauta <span class="kbd" style="border: 1px solid; color:#5e4638; background-color: #f9f9f9; border-bottom-width: 2px; -moz-border-radius: 3px; -webkit-border-radius: 3px; border-radius: 3px; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">OK</span> , mikä lisää tämän säännön muokattavana olevaan suotimeen. <span class="kbd" style="border: 1px solid; color:#5e4638; background-color: #f9f9f9; border-bottom-width: 2px; -moz-border-radius: 3px; -webkit-border-radius: 3px; border-radius: 3px; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">Peru</span> painikkeella peruutat säännön lisäämisen suotimeeen.

Katso myös [Which filters in which Category?](wiki:Gramps_6.0_Wiki_Manual_-_Filters#Which_filters_in_which_Category.3F)  

## <span id="Suotimet_kateorioittain" class="mw-headline">Suotimet kateorioittain</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Valitusta [kategoriasta](wiki:Gramps_6.0_Wiki_Manual_-_Categories) saat eri valikoiman[suotimia](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Filter). Katso myös [Summary of Gramplets](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Summary_of_Gramplets).

- Työpöytä kategoria  
  tarjolla ei ole suotimia

<!-- -->

- Henkilöt, Suhteet ja Kaaviot kategoriat  
  [Esivanhempien suotimet](#Ancestral_filters), [Lainaus/lähdesuotimet](#Citation.2Fsource_filters), [Jälkeläissuotimet](#Descendant_filters), [Tapahtumasuotimet](#Event_filters), [Perhesuotimet](#Family_filters), [Yleiset suotimet](#General_filters), and [Suhdesuotimet](#Relationship_filters).

<!-- -->

- Perheet kategoria  
  [Lapsisuotimet](#Child_filters), [Lainaus/lähdesuotimet](#Citation.2Fsource_filters), [Tapahtumasuotimet](#Event_filters), [Isäsuotimet](#Father_filters), [Yleiset suotimet](#General_filters), and [Äitisuotimet](#Mother_filters)

<!-- -->

- Tapahtumat ja Media kategoriat  
  [Lainaus/lähdesuotimet](#Citation.2Fsource_filters), and [Yleiset suotimet](#General_filters).

<!-- -->

- Paikat kategoria  
  [Lainaus/lähdesuotimet](#Citation.2Fsource_filters), [Yleiset suotimet](#General_filters), and [Sijaintisuotimet](#Position_filters).

<!-- -->

- Kartat kategoria (Vain Sivupalkissa ja Alapalkissa)  
  [Esivanhempien suotimet](#Ancestral_filters), [Lainaus/lähdesuotimet](#Citation.2Fsource_filters), [Jälkeläissuotimet](#Descendant_filters), [Tapahtumasuotimet](#Event_filters), [Perhesuotimet](#Family_filters), [Yleiset suotimet](#General_filters), and [Suhdesuotimet](#Relationship_filters).

<!-- -->

- Lähteet, Arkistot ja Lisätiedot kategoriat  
  only [Yleiset suotimet](#General_filters) tarjolla

  Lainaukset kategoria  
  [Yleiset suotimet](#General_filters) ja [Lähdesuotimet](#Source_filters)

## <span id="Esivanhempien_suotimet" class="mw-headline">Esivanhempien suotimet</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Tässä kategoriassa ovat seuraavat säännöt, joilla haetaan henkilöitä heidän suhteellaan esivanhempana toisiin henkilöihin:

- \<Suotimen\> hyväksymien henkilöiden esivanhemmat  
  Tällä suotimella löydetään henkilöt, jotka ovat esivanhempia annetun Suotimen mukaisille henkilöille. Annettu suodin valitaan oikeasta reunasta Arvot\>Suotimen nimi-pudotusvalikosta.

<!-- -->

- \<Henkilön\> esivanhemmat  
  Tällä suotimella löydetään henkilöt, jotka ovat määritellyn henkilön esivanhempia. "Sisältäen: Lisää valittu GrampsID" lisävalinta" määrittää, otetaanko. määritelty henkilö itsekin mukaan tuloksiin (hyödyksi raporttien tulostuksessa). Voit syöttää henkilön ID:n ao. tekstikenttään tai valita hänet listasta <span class="kbd" style="border: 1px solid; color:#5e4638; background-color: #f9f9f9; border-bottom-width: 2px; -moz-border-radius: 3px; -webkit-border-radius: 3px; border-radius: 3px; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">Valitse...</span> painikkeella. Jälkimmäisessä tapauksessa valitun henkilön ID tulee näkyviin tekstikenttään.

<!-- -->

- Esivanhemmat \<Henkilölle\> vähintään \<N\> sukupolven päässä  
  Tällä suotimella löydetään henkilöt, jotka ovat määritellyn henkilön esivanhempia vähintään \<N\> sukupolven päässä sukulinjassa. Esimerkiksi käyttämällä tätä sääntöä 2 sukupolven ehdolla tuloksiin tulevat isovanhemmat, heidän vanhempansa jne mutta ei valitun henkilön omia vanhempia.

<!-- -->

- Esivanhemmat \<Henkilölle\> enintään \<N\> sukupolven päässä  
  Tällä suotimella löydetään henkilöt, jotka ovat määritellyn henkilön esivanhempia enintään \<N\> sukupolven päässä sukulinjassa. Esimerkiksi käyttämällä tätä sääntöä 2 sukupolven ehdolla tuloksiin tulevat valitun henkilön vanhemmat ja isovanhemmat, mutta ei enää heidän esivanhempiaan.

<!-- -->

- \<Henkilön\> tuplana olevat esivanhemmat  
  Tällä suotimella löydetään henkilöt, jotka ovat henkilön esivanhempia kaksi tai useamman kerran.

<!-- -->

- Henkilöt joilla on yhteinen esivanhempi \<Suotimen\> hyväksymien henkilöiden kanssa. Suodin valitaan pudotusvalikosta.

<!-- -->

- Henkilöt joilla on yhteinen esivanhempi \<Henkilön\> kanssa  
  Tällä suotimella löydetään henkilöt, jotka ovat yhteinen esivanhempi määrätyn henkilön kanssa.

<!-- -->

- Esivanhemmat kirjanmerkityille henkilöille enintään \<N\> sukupolven päässä  
  Tällä suotimella löydetään henkilöt, jotka ovat kirjanmerkittyjen henkilöiden esivanhempia enintään \<N\> sukupolven päässä sukulinjassa. Esimerkiksi käyttämällä tätä sääntöä 2 sukupolven ehdolla tuloksiin tulevat näiden henkilöiden vanhemmat ja isovanhemmat, mutta ei enää heidän esivanhempiaan.

<!-- -->

- Esivanhemmat kotihenkilölle enintään \<N\> sukupolven päässä  
  Tällä suotimella löydetään henkilöt, jotka ovat kotihenkilön esivanhempia enintään \<N\> sukupolven päässä sukulinjassa. Esimerkiksi käyttämällä tätä sääntöä 2 sukupolven ehdolla tuloksiin tulevat kotihenkilön vanhemmat ja isovanhemmat, mutta ei enää heidän esivanhempiaan.

## <span id="Lapsisuotimet" class="mw-headline">Lapsisuotimet</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

- Perheet, joilla lapsen ID sisältää \<tekstin\>  
  Poimii perheet, joissa lapsella on määritetty Gramps ID

  Perheet, joiden jollakin lapsella on \<nimi\>  
  Poimii perheet, oissa lapsella on määritetty nimi (nimenosa)

  Perheet, joilla on kaksoset  
  Poimii perheet, joilla on kaksoset

## <span id="Citation/source_filters"></span><span id="Citation.2Fsource_filters" class="mw-headline">Citation/source filters</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Nämä suotimet riippuvat näkymästä

### <span id="Lainaus/lähde_kategoria"></span><span id="Lainaus.2Fl.C3.A4hde_kategoria" class="mw-headline">Lainaus/lähde kategoria</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Tässä kategoriassa on seuraavat lainausten ja lähteiden säännöt:

- Henkilöt, joilla lähteitä \<lukumäärä\>  
  Poimii henkilöt, joilla on tietty määrä kohteita lähteinä. Lukumäärä: Kohteiden määrä -- Luvun oltava suurempi kuin/vähemmän kuin/yhtä suuri kuin

<!-- -->

- Henkilöt, joilla on \<lainaus\>  
  Poimii henkilöt, joilla on arvoiltaan tietty lainaus

<!-- -->

- Henkilöt, joilla on \<lähde\>  
  Poimii henkilöt, joilla on tietyn ID:n lähde

<!-- -->

- Henkilöt, joilla vähintään yhdessä suorassa lähteessä on \>=\> \<luotettavuustaso\>

### <span id="Perheet_kategoria" class="mw-headline">Perheet kategoria</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Tässä kategoriassa on seuraavat lainausten ja lähteiden säännöt:

- Perheet, joilla lähteitä \<lukumäärä\>  
  Poimii Perheet, joilla on tietty määrä kohteita lähteinä. Lukumäärä: Kohteiden määrä -- Luvun oltava suurempi kuin/vähemmän kuin/yhtä suuri kuin

<!-- -->

- Perheet, joilla on \<lainaus\>  
  Poimii Perheet, joilla on arvoiltaan tietty lainaus

<!-- -->

- Perheet, joilla on \<lähde\>  
  Poimii Perheet, joilla on tietyn ID:n lähde

<!-- -->

- Perheet, joilla vähintään yhdessä suorassa lähteessä on \>=\> \<luotettavuustaso\>

### <span id="Tapahtumat_kategoria" class="mw-headline">Tapahtumat kategoria</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Tässä kategoriassa on seuraavat lainausten ja lähteiden säännöt:

- Tapahtumat, joiden lähteen \<lähdesuodin\> hyväksyy

<!-- -->

- Tapahtumat, joihin on liitetty \<lainaus\>  
  Poimii tapahtumat, joilla on arvoiltaan tietty lainaus

<!-- -->

- Tapahtumat, joilla lähteitä on \<lukumäärä\>  
  Kohteiden määrä -- Luvun oltava suurempi kuin/vähemmän kuin/yhtä suuri kuin

<!-- -->

- Tapahtumat, joilla vähintään yhdessä suorassa lähteessä on \>=\> \<luotettavuustaso\>

### <span id="Paikat_kategoria" class="mw-headline">Paikat kategoria</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Tässä kategoriassa on seuraavat lainausten ja lähteiden säännöt:

- Paikat, joilla lähteitä on \<lukumäärä\>  
  Kohteiden määrä -- Luvun oltava suurempi kuin/vähemmän kuin/yhtä suuri kuin

<!-- -->

- Paikat, joilla vähintään yhdessä suorassa lähteessä on \>=\> \<luotettavuustaso\>

<!-- -->

- Paikat, joihin on liitetty \<lainaus\>  
  Poimii paikat, joilla on arvoiltaan tietty lainaus

<!-- -->

- Paikat, joilla on \<lähde\>  
  Poimii paikat, joilla on tietyn ID:n lähde

### <span id="Media_kategoria" class="mw-headline">Media kategoria</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Tässä kategoriassa on seuraavat lainausten ja lähteiden säännöt:

- Mediat, joilla lähteitä on \<lukumäärä\>  
  Kohteiden määrä -- Luvun oltava suurempi kuin/vähemmän kuin/yhtä suuri kuin

<!-- -->

- Mediat, joilla vähintään yhdessä suorassa lähteessä on \>=\> \<luotettavuustaso\>

<!-- -->

- Mediat, joihin on liitetty \<lainaus\>  
  Poimii Mediat, joilla on arvoiltaan tietty lainaus

<!-- -->

- Mediat, joilla on \<lähde\>  
  Poimii Mediat, joilla on tietyn ID:n lähde

## <span id="Jälkeläissuodattimet"></span><span id="J.C3.A4lkel.C3.A4issuodattimet" class="mw-headline">Jälkeläissuodattimet</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Tämä luokka sisältää seuraavat säännöt, jotka yhdistävät ihmisiä heidän jälkeläissuhteidensa perusteella muihin henkilöihin:

- \<Henkilön\> jälkeläiset  
  Tämä sääntö yhdistää henkilöt, jotka ovat suodattimen avulla osuvan henkilön jälkeläisiä tai puoliso. Voit joko kirjoittaa ID-tunnuksen tekstikenttään tai valita henkilön luettelosta napsauttamalla <span class="kbd" style="border: 1px solid; color:#5e4638; background-color: #f9f9f9; border-bottom-width: 2px; -moz-border-radius: 3px; -webkit-border-radius: 3px; border-radius: 3px; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;"> Valitse...</span> -painiketta. Jälkimmäisessä tapauksessa tunnus näkyy tekstikentässä valinnan jälkeen.Lisää valittu Gramps ID -valinta ottaa \<Henkilön\> mukaan.

<!-- -->

- \<Henkilön\> jälkeläiset perheineen  
  Tämä sääntö yhdistää henkilöt, jotka ovat määritetyn henkilön jälkeläisiä, sekä heidän puolisonsa. Lisää valittu Gramps ID -valinta ottaa \<Henkilön\> mukaan. Voit joko kirjoittaa ID-tunnuksen tekstikenttään tai valita henkilön luettelosta napsauttamalla <span class="kbd" style="border: 1px solid; color:#5e4638; background-color: #f9f9f9; border-bottom-width: 2px; -moz-border-radius: 3px; -webkit-border-radius: 3px; border-radius: 3px; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;"> Valitse...</span> -painiketta. Jälkimmäisessä tapauksessa tunnus näkyy tekstikentässä valinnan jälkeen. Lisää valittu Gramps ID -valinta ottaa \<Henkilön\> mukaan.

<!-- -->

- \<Suotimen\> hyväksymien henkilöiden jälkeläiset  
  Tämä sääntö yhdistää henkilöt, jotka ovat määritetyn suodattimen avulla osuvan henkilön jälkeläisiä. Määritetty suodattimen nimi tulee valita valikosta.

<!-- -->

- \<Suotimen\> hyväksymien henkilöiden jälkeläiset perheineen\>  
  Tämä sääntö yhdistää henkilöt, jotka ovat määritetyn suodattimen avulla osuvan henkilön jälkeläisiä. Määritetty suodattimen nimi tulee valita valikosta.

<!-- -->

- Jälkeläiset \<Henkilölle\> enintään \<N\> sukupolven päässä  
  Tämä sääntö yhdistää henkilöt, jotka ovat määritetyn suodattimen avulla osuvan henkilön jälkeläisiä ja enintään N:n sukupolven päässä tästä henkilöstä. Esimerkiksi tämän säännön käyttäminen sukupolvien lukumäärän arvolla 2 löytää haun tuloksena lapset ja lapsenlapset.

<!-- -->

- Jälkeläiset \<Henkilölle\> vähintään \<N\> sukupolven päässä  
  Tämä sääntö yhdistää henkilöt, jotka ovat määritetyn suodattimen avulla osuvan henkilön jälkeläisiä ja vähintään N:n sukupolven päässä tästä henkilöstä. Esimerkiksi tämän säännön käyttäminen sukupolvien lukumäärän arvolla 2 löytää haun tuloksena lapsenlapset.

## <span id="Tapahtumasuotimet" class="mw-headline">Tapahtumasuotimet</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Nämä suotimet riippuvat näkymäkategoriasta.

### <span id="Henkilöitä_koostavat_suotimet"></span><span id="Henkil.C3.B6it.C3.A4_koostavat_suotimet" class="mw-headline">Henkilöitä koostavat suotimet</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Tämä luokka sisältää seuraavat säännöt, jotka yhdistävät ihmisiä heidän tallennettujen tapahtumiensa perusteella:

- Henkilöt epätäydellisillä tapahtumilla  
  Tämä sääntö yhdistää henkilöt, joilta puuttuu päivämäärä tai paikka missä tahansa henkilökohtaisessa tapahtumassa.

<!-- -->

- Henkilöt, joilla on \<syntymätieto\>  
  Tämä sääntö yhdistää henkilöt, joiden syntymätapahtuma vastaa määritettyjä arvoja Päivämäärä, Paikka ja Kuvaus. Sääntö palauttaa osuman, vaikka henkilön syntymätapahtuma vastaisi arvoa osittain. Yhteensovitus eivät riipu kirjainkoosta. Esimerkiksi kaikki Ruotsissa syntyneet yhdistetään säännön avulla käyttämällä paikka-arvoa "sw". Sääntö palauttaa osuman vain, jos kaikki ei-tyhjät arvot vastaavat osittainkin henkilön syntymää. Jos haluat käyttää vain yhtä arvoa, jätä muut arvot tyhjiksi.

<!-- -->

- Henkilöt, joilla on \<kuolintieto\>  
  Tämä sääntö yhdistää henkilöt, joiden kuolintapahtuma vastaa määritettyjä arvoja Päivämäärä, Paikka ja Kuvaus. Sääntö palauttaa osuman, vaikka henkilön kuolintapahtuma vastaisi arvoa osittain. Yhteensovitus eivät riipu kirjainkoosta. Esimerkiksi kaikki Loviisan kaupungissa tai mlk:ssa kuolleet tunnistetaan säännön mukaan käyttämällä paikkaan arvoa "lovi". Sääntö palauttaa osuman vain, jos kaikki ei-tyhjät arvot vastaavat (osittain) henkilön kuolemaa. Jos haluat käyttää vain yhtä arvoa, jätä muut arvot tyhjiksi.

<!-- -->

- Henkilöt, joilla on \<perhetapahtuma\>  
  Tämä sääntö yhdistää henkilöt, joilla on perhetapahtuma, joka vastaa määritettyjä tapahtumatyypin, päivämäärän, paikan ja kuvauksen arvoja. Sääntö palauttaa osuman, vaikka henkilön tapahtuma vastaisi arvoa osittainkin. Täsmäytys eivät riipu kirjainkoosta. Esimerkiksi kaikki Loviisassa tai Loviisan srk:ssa avioituneet henkilöt tunnistetaan säännön mukaan käyttämällä Avioliitto-tapahtumaa ja paikkaan arvoa "lovi". Perhetapahtumat tulee valita alasvedettävästä valikosta. Sääntö palauttaa osuman vain, jos kaikki ei-tyhjät arvot vastaavat (osittain) henkilökohtaista tapahtumaa. Jos haluat käyttää vain yhtä arvoa, jätä muut arvot tyhjiksi.

<!-- -->

- Henkilöt, joilla on henkilökohtainen \<tapahtuma\>  
  Tämä sääntö yhdistää henkilöt, joilla on henkilökohtainen tapahtuma, joka vastaa määritettyjä tapahtumatyypin, päivämäärän, paikan ja kuvauksen arvoja. Sääntö palauttaa osuman, vaikka henkilön tapahtuma vastaisi arvoa osittain. Täsmäytys eivät riipu kirjainkoosta. Esimerkiksi kaikki Ruotsissa valmistuneet henkilöt täsmäävät säännön mukaan käyttämällä Valmistuminen-tapahtumaa ja Paikan arvoa "sver". Henkilökohtaiset tapahtumat tulee valita alasvetovalikosta. Sääntö palauttaa osuman, jos ja vain jos kaikki ei-tyhjät arvot vastaavat (osittain) henkilökohtaista tapahtumaa. Jos haluat käyttää vain yhtä arvoa, jätä muut arvot tyhjiksi.

<!-- -->

- Henkilöt, joilla on \<Lukumäärä\> \<Tapahtumaa\>  
  Tämä sääntö yhdistää henkilöt, joilla on henkilökohtainen tapahtuma, joka vastaa määritettyjä tapahtumatyypin ja lukumäärän arvoja. Tyyppi tulee valita alasvedettävästä valikosta. Lukumäärälle annetaan pudotusvalikosta ehto "vähemmän, sama, enemmän kuin". Lisäksi voi antaa lisäehdon, valitaanko mukaan vain roolin Päähenkilö tapahtumat.

<!-- -->

- Perheet epätäydellisillä tapahtumilla  
  Tämä sääntö yhdistää henkilöt, joilta puuttuu päivämäärä tai paikka missä tahansa perheen perhetapahtumassa.

<!-- -->

- Todistaja  
  Tämä sääntö yhdistää henkilöt, jotka ovat läsnä todistajina tapahtumassa. Jos henkilökohtaisen tai perhetapahtuman tyyppi on määritetty, haetaan vain tämän tyyppisiä tapahtumia.

### <span id="Families_Category" class="mw-headline">Families Category</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

This category includes the following rules that match families based on their recorded events:

- Families with the \<event\>  
  This rule matches famikies that have a event matching specified values for the Event type, Date, Place, and Description. The rule returns a match even if the person's event matches the value partially. The matching rules are case-insensitive. For example, anyone who was married in Sweden will be matched by the rule using the Marriage event and the value "sw" for the Place. The family events should be selected from a pull-down menu. The rule returns a match if, and only if, all non-empty values are (partially) matched by the personal event. To use just one value, leave the other values empty.

## <span id="Family_filters" class="mw-headline">Family filters</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

This category includes the following rules that match people based on their family relationships:

- Adopted people  
  This rule matches adopted people.

<!-- -->

- Child of \<filter\> match  
  This rule matches people for whom either parent is matched by the specified filter. The specified filter name should be selected from the menu.

<!-- -->

- Parents of \<filter\> match  
  This rule matches people whose child is matched by the specified filter. The specified filter name should be selected from the menu.

<!-- -->

- People missing parents  
  Matches people that are children in a family with less than two parents or are not children in any family.

<!-- -->

- People with children  
  This rule matches people with children.

<!-- -->

- People with multiple marriage records  
  This rule matches people with more than one spouse.

<!-- -->

- People with no marriage records  
  This rule matches people with no spouses.

<!-- -->

- People with the \<relationships\>  
  This rule matches people with a particular relationship. The relationship must match the type selected from the menu. Optionally, the number of relationships and the number of children can be specified. The rule returns a match if, and only if, all non-empty values are (partially) matched by a person's relationship. To use just one value, leave the other values empty.

<!-- -->

- Siblings of \<filter\> match  
  This rule matches people whose sibling is matched by the specified filter. The specified filter name should be selected from the menu.

<!-- -->

- Spouses of \<filter\> match  
  This rule matches people married to someone who is matched by the specified filter. The specified filter name should be selected from the menu.

## <span id="Father_filters" class="mw-headline">Father filters</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

- Families having father with id containing \<text\>  
  Matches families whose father has a specified Gramps ID

<!-- -->

- Families with father with the \<name\>  
  Matches families whose father has a specified (partial) name

## <span id="General_filters" class="mw-headline">General filters</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

These filters are view dependent

### <span id="Persons-,_and_Relationship_Category"></span><span id="Persons-.2C_and_Relationship_Category" class="mw-headline">Persons-, and Relationship Category</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

This category includes the following general rules:

- Bookmarked people  
  Matches the people on the bookmark list.

<!-- -->

- Default person  
  Matches the default person.

<!-- -->

- Disconnected People  
  Matches people that have no family relationships to any other person in the database.

<!-- -->

- Everyone  
  Matches everyone in the database.

<!-- -->

- Females  
  Matches all females.

<!-- -->

- Males  
  Matches all males.

<!-- -->

- People having \<count\> notes  
  Matches people having a certain number of notes: Values: Number of instances -- Number must be greater than/lesser/equal to

<!-- -->

- People having notes containing \<text\>  
  Matches people whose notes contain text matching a regular expression

<!-- -->

- People marked private  
  Matches people that are indicated as private.

<!-- -->

- People matching the \<filter\>  
  Matches people matched by the specified filter name. Values: Filter name. The specified filter name should be selected from the menu.

<!-- -->

- People not marked private  
  Matches people that are not indicated as private

<!-- -->

- People probably alive  
  Matches people without indications of death that are not too old. Values: On Date

<!-- -->

- People with \<count\> LDS events  
  Matches people with a certain number of LDS events. Values: Number of instances -- Number must be greater than/lesser/equal to

<!-- -->

- People with \<count\> addresses  
  Matches people with a certain number of personal addresses. Values: Number of instances -- Number must be greater than/lesser/equal to

<!-- -->

- People with \<count\> associations  
  Matches people with a certain number of associations. Values: Number of instances -- Number must be greater than/lesser/equal to

<!-- -->

- People with \<count\> media  
  Matches people with a certain number of items in the gallery. Values: Number of instances -- Number must be greater than/lesser/equal to

<!-- -->

- People with id containing \<text\>  
  Matches people whose Gramps ID matches the regular expression

<!-- -->

- People with a nickname  
  Matches people with a nickname

<!-- -->

- People with an alternate name  
  Matches people with an alternate name

<!-- -->

- People with incomplete names  
  Matches people with first-name or last-name missing.

<!-- -->

- People with records containing \<substring\>  
  Matches people whose records contain text matching a substring. Values: Substring -- Case Sensitive or not -- Regular-Expression matching or not

<!-- -->

- People with the \<Name type\>  
  Matches people with a type of name

<!-- -->

- People with the \<Surname origin type\>  
  Matches people with a surname origin

<!-- -->

- People with the \<name\>  
  Matches people with a specified (partial) name. Values: Given Name -- Family Name -- Suffix -- Title -- Prefix -- Patronymic -- Call Name

<!-- -->

- People with \<tag\>  
  Matches people with a tag of a particular value. Values: Tag name.

<!-- -->

- People with the family \<attribute\>  
  Matches people with the family attribute of a particular value. Values: Family Attribute: Identification Number -- Age ...

<!-- -->

- People with the personal \<attribute\>  
  Matches people with the personal attribute of a particular value. Values: Family Attribute: Identification Number -- Age ...

<!-- -->

- People with unknown gender  
  Matches all people with unknown gender.

<!-- -->

- People without a known birth date  
  Matches people without a known birth date.

<!-- -->

- People without a known death date  
  Matches people without a known death date.

<!-- -->

- People with \<id\>  
  Matches people with Gramps ID. The rule returns a match only if the ID is matched exactly. You can either enter the ID into a text entry field, or select an object from the list by clicking <span class="kbd" style="border: 1px solid; color:#5e4638; background-color: #f9f9f9; border-bottom-width: 2px; -moz-border-radius: 3px; -webkit-border-radius: 3px; border-radius: 3px; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">Select...</span> button. In the latter case, the ID will appear in the text field after the selection was made.

<!-- -->

- People changed after \<date time\>  
  Matches person records changed after a specified date-time (yyy-mm-dd hh:mm:ss) or in the range, if a second date-time is given: Values: Changed after: -- but before:.

<!-- -->

- Persons with events matching the \<event filter\>  
  Matches persons who have events that match a certain event filter. Values: Event filter name.

### <span id="Families_Category_2" class="mw-headline">Families Category</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

This category includes the following general rules:

- Bookmarked families  
  Matches the families on the bookmark list.

<!-- -->

- Every family  
  Matches every family in the database.

<!-- -->

- Families changed after \<date time\>  
  Matches families records changed after a specified date-time (yyy-mm-dd hh:mm:ss) or in the range, if a second date-time is given: Values: Changed after: -- but before:.

<!-- -->

- Families having \<count\> notes  
  Matches families having a certain number of notes: Values: Number of instances -- Number must be greater than/lesser/equal to

<!-- -->

- Families having notes containing \<text\>  
  Matches families whose notes contain text matching a regular expression

<!-- -->

- Families marked private  
  Matches families that are indicated as private.

<!-- -->

- Families matching the \<filter\>  
  Matches families matched by the specified filter name. Values: Filter name. The specified filter name should be selected from the menu.

<!-- -->

- Families with \<count\> LDS events  
  Matches families with a certain number of LDS events. Values: Number of instances -- Number must be greater than/lesser/equal to

<!-- -->

- Families with \<count\> media  
  Matches families with a certain number of items in the gallery. Values: Number of instances -- Number must be greater than/lesser/equal to

<!-- -->

- Families with id containing \<text\>  
  Matches families whose Gramps ID matches the regular expression

<!-- -->

- Families with a reference count of \<count\>  
  Matches families with a certain number of references. Values: Number of references -- Number must be greater than/lesser/equal to

<!-- -->

- Families with the \<tag\>  
  Matches families with a tag of a particular value. Values: Tag name.

<!-- -->

- Families with the family \<attribute\>  
  Matches families with the family attribute of a particular value. Values: Family Attribute: Identification Number -- Age ...

<!-- -->

- Families with the relationship type  
  Matches families with the relationship type of a particular value

<!-- -->

- Families with \<id\>  
  Matches families with Gramps ID. The rule returns a match only if the ID is matched exactly. You can either enter the ID into a text entry field, or select an object from the list by clicking <span class="kbd" style="border: 1px solid; color:#5e4638; background-color: #f9f9f9; border-bottom-width: 2px; -moz-border-radius: 3px; -webkit-border-radius: 3px; border-radius: 3px; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">Select...</span> button. In the latter case, the ID will appear in the text field after the selection was made.

### <span id="Events_Category" class="mw-headline">Events Category</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

This category includes the following general rules:

- Event with \<id\>  
  Matches events with Gramps ID. The rule returns a match only if the ID is matched exactly. You can either enter the ID into a text entry field, or select an object from the list by clicking <span class="kbd" style="border: 1px solid; color:#5e4638; background-color: #f9f9f9; border-bottom-width: 2px; -moz-border-radius: 3px; -webkit-border-radius: 3px; border-radius: 3px; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">Select...</span> button. In the latter case, the ID will appear in the text field after the selection was made.

<!-- -->

- Events changed after \<date time\>  
  Matches events records changed after a specified date-time (yyy-mm-dd hh:mm:ss) or in the range, if a second date-time is given: Values: Changed after: -- but before:.

<!-- -->

- Events having \<count\> notes  
  Matches events having a certain number of notes: Values: Number of instances -- Number must be greater than/lesser/equal to

<!-- -->

- Events having notes containing \<text\>  
  Matches events whose notes contain text matching a regular expression

<!-- -->

- Events marked private  
  Matches events that are indicated as private.

<!-- -->

- Events matching the \<filter\>  
  Matches events matched by the specified filter name. Values: Filter name. The specified filter name should be selected from the menu.

<!-- -->

- Events occurring on a particular day of the week  
  Matches events occurring on a particular day of the week

<!-- -->

- Events of persons matching the \<person filter\>  
  Matches events of person matched by the specified person filter name

<!-- -->

- Events of places matching the \<place filter\>  
  Matches events that occurred at places that match the specified place filter name

<!-- -->

- Events with \<count\> media  
  Matches events with a certain number of items in the gallery. Values: Number of instances -- Number must be greater than/lesser/equal to

<!-- -->

- Events with \<date\>  
  Matches events with data of a particular value

<!-- -->

- Events with id containing \<text\>  
  Matches events whose Gramps ID matches the regular expression

<!-- -->

- Events with a reference count of \<count\>  
  Matches events with a certain number of references. Values: Number of references -- Number must be greater than/lesser/equal to

<!-- -->

- Events with the \<tag\>  
  Matches events with a tag of a particular value. Values: Tag name.

<!-- -->

- Events with the \<attribute\>  
  Matches events with the attribute of a particular value. Values: Family Attribute: Identification Number -- Age ...

<!-- -->

- Events with the particular type  
  Matches events with the particular type

<!-- -->

- Every event  
  Matches every event in the database.

### <span id="Places_Category" class="mw-headline">Places Category</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

This category includes the following general rules:

- Every place  
  Matches every place in the database.

<!-- -->

- Place with \<id\>  
  Matches places with Gramps ID. The rule returns a match only if the ID is matched exactly. You can either enter the ID into a text entry field, or select an object from the list by clicking <span class="kbd" style="border: 1px solid; color:#5e4638; background-color: #f9f9f9; border-bottom-width: 2px; -moz-border-radius: 3px; -webkit-border-radius: 3px; border-radius: 3px; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">Select...</span> button. In the latter case, the ID will appear in the text field after the selection was made.

<!-- -->

- Places changed after \<date time\>  
  Matches places records changed after a specified date-time (yyy-mm-dd hh:mm:ss) or in the range, if a second date-time is given: Values: Changed after: -- but before:.

<!-- -->

- Places having \<count\> notes  
  Matches places having a certain number of notes: Values: Number of instances -- Number must be greater than/lesser/equal to

<!-- -->

- Places having notes containing \<text\>  
  Matches places whose notes contain text matching a regular expression

<!-- -->

- Places marked private  
  Matches places that are indicated as private.

<!-- -->

- Places matching a title  
  Matches places with a particular title

<!-- -->

- Places matching parameters  
  Matches places with particular parameters

<!-- -->

- Places matching the \<filter\>  
  Matches places matched by the specified filter name. Values: Filter name. The specified filter name should be selected from the menu.

<!-- -->

- Places of events matching the \<event filter\>  
  Matches places where events happened that match the specified event filter name

<!-- -->

- Places with \<count\> media  
  Matches places with a certain number of items in the gallery. Values: Number of instances -- Number must be greater than/lesser/equal to

<!-- -->

- Places with id containing \<text\>  
  Matches places whose Gramps ID matches the regular expression

<!-- -->

- Places with a reference count of \<count\>  
  Matches places with a certain number of references. Values: Number of references -- Number must be greater than/lesser/equal to

<!-- -->

- Places with the \<tag\>  
  Matches places with a tag of a particular value. Values: Tag name.

### <span id="Sources_Category" class="mw-headline">Sources Category</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

This category includes the following general rules:

- Every source  
  Matches every source in the database.

<!-- -->

- Sources with \<id\>  
  Matches sources with Gramps ID. The rule returns a match only if the ID is matched exactly. You can either enter the ID into a text entry field, or select an object from the list by clicking <span class="kbd" style="border: 1px solid; color:#5e4638; background-color: #f9f9f9; border-bottom-width: 2px; -moz-border-radius: 3px; -webkit-border-radius: 3px; border-radius: 3px; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">Select...</span> button. In the latter case, the ID will appear in the text field after the selection was made.

<!-- -->

- Sources changed after \<date time\>  
  Matches sources records changed after a specified date-time (yyy-mm-dd hh:mm:ss) or in the range, if a second date-time is given: Values: Changed after: -- but before:.

<!-- -->

- Sources having \<count\> notes  
  Matches sources having a certain number of notes: Values: Number of instances -- Number must be greater than/lesser/equal to

<!-- -->

- Sources having notes containing \<text\>  
  Matches sources whose notes contain text matching a regular expression

<!-- -->

- Sources marked private  
  Matches sources that are indicated as private.

<!-- -->

- Sources matching the \<filter\>  
  Matches sources matched by the specified filter name. Values: Filter name. The specified filter name should be selected from the menu.

<!-- -->

- Sources with \<count\> Repository references  
  Matches sources with a certain number of repository references

<!-- -->

- Sources with \<count\> media  
  Matches sources with a certain number of items in the gallery. Values: Number of instances -- Number must be greater than/lesser/equal to

<!-- -->

- Sources with id containing \<text\>  
  Matches sources whose Gramps ID matches the regular expression

<!-- -->

- Sources with a reference count of \<count\>  
  Matches sources with a certain number of references. Values: Number of references -- Number must be greater than/lesser/equal to

<!-- -->

- Sources with repository reference containing \<text\> in 'Call Number'  
  Matches sources with a repository reference containing a substring in 'Call Number'

<!-- -->

- Sources with repository reference matching the \<repository filter\>  
  Matches sources with a repository reference that match a certain repository filter

<!-- -->

- Sources with the \<tag\>  
  Matches sources with a tag of a particular value. Values: Tag name.

<!-- -->

- Sources with title containing \<text\>  
  Matches sources whose title contains a certain substring

### <span id="Citations_Category" class="mw-headline">Citations Category</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

This category includes the following general rules:

- Citation with \<id\>  
  Matches citations with Gramps ID. The rule returns a match only if the ID is matched exactly. You can either enter the ID into a text entry field, or select an object from the list by clicking <span class="kbd" style="border: 1px solid; color:#5e4638; background-color: #f9f9f9; border-bottom-width: 2px; -moz-border-radius: 3px; -webkit-border-radius: 3px; border-radius: 3px; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">Select...</span> button. In the latter case, the ID will appear in the text field after the selection was made.

<!-- -->

- Citations changed after \<date time\>  
  Matches citations records changed after a specified date-time (yyy-mm-dd hh:mm:ss) or in the range, if a second date-time is given: Values: Changed after: -- but before:.

<!-- -->

- Citations having \<count\> notes  
  Matches citations having a certain number of notes: Values: Number of instances -- Number must be greater than/lesser/equal to

<!-- -->

- Citations having notes containing \<text\>  
  Matches citations whose notes contain text matching a regular expression

<!-- -->

- Citations marked private  
  Matches citations that are indicated as private.

<!-- -->

- Citations matching parameters  
  Matches citations with particular parameters

<!-- -->

- Citations matching the \<filter\>  
  Matches citations matched by the specified filter name. Values: Filter name. The specified filter name should be selected from the menu.

<!-- -->

- Citations with \<count\> media  
  Matches citations with a certain number of items in the gallery. Values: Number of instances -- Number must be greater than/lesser/equal to

<!-- -->

- Citations with id containing \<text\>  
  Matches citations whose Gramps ID matches the regular expression

<!-- -->

- Citations with Volume/Page containing \<text\>  
  Matches citations whose Volume/Page contains a certain substring

<!-- -->

- Citations with a reference count of \<count\>  
  Matches citations with a certain number of references. Values: Number of references -- Number must be greater than/lesser/equal to

<!-- -->

- Citations with a source with a repository reference matching the \<repository filter\>  
  Matches citations with a source with a repository reference that match a certain repository filter

<!-- -->

- Citations with source matching the \<source filter\>  
  Matches citations with sources that match the specified source filter name

<!-- -->

- Citations with the \<tag\>  
  Matches citations with a tag of a particular value. Values: Tag name.

<!-- -->

- Every citation  
  Matches every citation in the database.

### <span id="Repositories_Category" class="mw-headline">Repositories Category</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

This category includes the following general rules:

- Every repository  
  Matches every repository in the database.

<!-- -->

- Repositories changed after \<date time\>  
  Matches repository records changed after a specified date-time (yyy-mm-dd hh:mm:ss) or in the range, if a second date-time is given: Values: Changed after: -- but before:.

<!-- -->

- Repositories having notes containing \<text\>  
  Matches repositories whose notes contain text matching a regular expression

<!-- -->

- Repositories marked private  
  Matches repositories that are indicated as private.

<!-- -->

- Repositories matching the \<filter\>  
  Matches repositories matched by the specified filter name. Values: Filter name. The specified filter name should be selected from the menu.

<!-- -->

- Repositories with id containing \<text\>  
  Matches repositories whose Gramps ID matches the regular expression

<!-- -->

- Repositories with a reference count of \<count\>  
  Matches repositories with a certain number of references. Values: Number of references -- Number must be greater than/lesser/equal to

<!-- -->

- Repositories with name containing \<text\>  
  Matches repositories whose name contains substring

<!-- -->

- Repositories with the \<tag\>  
  Matches repositories with a tag of a particular value. Values: Tag name.

<!-- -->

- Repository with \<id\>  
  Matches repositories with Gramps ID. The rule returns a match only if the ID is matched exactly. You can either enter the ID into a text entry field, or select an object from the list by clicking <span class="kbd" style="border: 1px solid; color:#5e4638; background-color: #f9f9f9; border-bottom-width: 2px; -moz-border-radius: 3px; -webkit-border-radius: 3px; border-radius: 3px; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">Select...</span> button. In the latter case, the ID will appear in the text field after the selection was made.

### <span id="Media_Category" class="mw-headline">Media Category</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

This category includes the following general rules:

- Every media object  
  Matches every media object in the database.

<!-- -->

- Media object with \<id\>  
  Matches media objects with Gramps ID. The rule returns a match only if the ID is matched exactly. You can either enter the ID into a text entry field, or select an object from the list by clicking <span class="kbd" style="border: 1px solid; color:#5e4638; background-color: #f9f9f9; border-bottom-width: 2px; -moz-border-radius: 3px; -webkit-border-radius: 3px; border-radius: 3px; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">Select...</span> button. In the latter case, the ID will appear in the text field after the selection was made.

<!-- -->

- Media objects changed after \<date time\>  
  Matches media object records changed after a specified date-time (yyy-mm-dd hh:mm:ss) or in the range, if a second date-time is given: Values: Changed after: -- but before:.

<!-- -->

- Media objects having notes containing \<text\>  
  Matches media objects whose notes contain text matching a regular expression

<!-- -->

- Media objects marked private  
  Matches media objects that are indicated as private.

<!-- -->

- Media objects matching the \<filter\>  
  Matches media objects matched by the specified filter name. Values: Filter name. The specified filter name should be selected from the menu.

<!-- -->

- Media objects with id containing \<text\>  
  Matches media objects whose Gramps ID matches the regular expression

<!-- -->

- Media objects with a reference count of \<count\>  
  Matches media objects with a certain number of references. Values: Number of references -- Number must be greater than/lesser/equal to

<!-- -->

- Media objects with the \<tag\>  
  Matches media objects with a tag of a particular value. Values: Tag name.

<!-- -->

- Media objects with the attribute \<attribute\>  
  Matches media objects with the attribute of a particular value

### <span id="Notes_Category" class="mw-headline">Notes Category</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

This category includes the following general rules:

- Every note  
  Matches every note in the database.

<!-- -->

- Note with \<id\>  
  Matches notes with Gramps ID. The rule returns a match only if the ID is matched exactly. You can either enter the ID into a text entry field, or select an object from the list by clicking <span class="kbd" style="border: 1px solid; color:#5e4638; background-color: #f9f9f9; border-bottom-width: 2px; -moz-border-radius: 3px; -webkit-border-radius: 3px; border-radius: 3px; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">Select...</span> button. In the latter case, the ID will appear in the text field after the selection was made.

<!-- -->

- Notes changed after \<date time\>  
  Matches notes records changed after a specified date-time (yyy-mm-dd hh:mm:ss) or in the range, if a second date-time is given: Values: Changed after: -- but before:.

<!-- -->

- Notes containing \<text\>  
  Matches notes contain text matching a regular expression

<!-- -->

- Notes marked private  
  Matches notes that are indicated as private.

<!-- -->

- Notes matching parameters  
  Matches notes with particular parameters

<!-- -->

- Notes matching the \<filter\>  
  Matches notes matched by the specified filter name. Values: Filter name. The specified filter name should be selected from the menu.

<!-- -->

- Notes with id containing \<text\>  
  Matches notes whose Gramps ID matches the regular expression

<!-- -->

- Notes with a reference count of \<count\>  
  Matches notes with a certain number of references. Values: Number of references -- Number must be greater than/lesser/equal to

<!-- -->

- Notes with the \<tag\>  
  Matches notes with a tag of a particular value. Values: Tag name.

<!-- -->

- Notes with the particular type  
  Matches notes with the particular type

## <span id="Mother_filters" class="mw-headline">Mother filters</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

- Families having mother with id containing \<text\>  
  Matches families whose mother has a specified Gramps ID

<!-- -->

- Families with mother with the \<name\>  
  Matches families whose mother has a specified (partial) name

## <span id="Position_filters" class="mw-headline">Position filters</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

- Places in neighborhood of given position  
  Matches places with latitude or longitude position in a rectangle of given height and width (in degrees), and with middle point the given latitude and longitude.

<!-- -->

- Places with no latitude or longitude given  
  Matches places with empty latitude or longitude

## <span id="Source_filters" class="mw-headline">Source filters</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

- Citation with Source \<id\>  
  Matches a citation with a source with a specified Gramps ID

<!-- -->

- Citations having source notes containing \<text\>  
  Matches citations whose source notes contain a substring or match a regular expression

<!-- -->

- Citations with Source Id containing \<text\>  
  Matches citations whose source has a Gramps ID that matches the regular expression

<!-- -->

- Sources matching parameters  
  Matches citations with a source of a particular value

## <span id="Relationship_filters" class="mw-headline">Relationship filters</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

This category includes the following rules that match people based on their mutual relationship:

- People related to \<Person\>  
  Matches people related to a specified person

<!-- -->

- Relationship path between \<person\> and people matching \<filter\>  
  Searches over the database starting from a specified person and returns everyone between that person and a set of target people specified with a filter. This produces a set of relationship paths (including by marriage) between the specified person and the target people. Each path is not necessarily the shortest path.

<!-- -->

- Relationship path between \<persons\>  
  This rule matches all ancestors of both people back to their common ancestors (if exist). This produces the "relationship path" between these two people, through their common ancestors. You can either enter the ID of each person into the appropriate text entry fields, or select people from the list by clicking their <span class="kbd" style="border: 1px solid; color:#5e4638; background-color: #f9f9f9; border-bottom-width: 2px; -moz-border-radius: 3px; -webkit-border-radius: 3px; border-radius: 3px; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">Select...</span> buttons. In the latter case, the ID will appear in the text field after the selection was made.

<!-- -->

- Relationship path between bookmarked persons  
  Matches the ancestors of bookmarked individuals back to common ancestors, producing the relationship path(s) between bookmarked persons.

## <span id="Tagging" class="mw-headline">Tagging</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

<table style="width:40%;margin-top:+.7em;margin-bottom:+.7em;background-color: #ffd43385;border:1px solid #cccccc85; padding: 5px" data-align="left">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td>![[_media/Gramps-notes.png]]</td>
<td><p>This article's content is incomplete or a placeholder stub.<br />
Please update or expand this section.</p></td>
</tr>
</tbody>
</table>

  

The concept of tagging for most people using *gmail* or *thunderbird*, tags will not be something new. Instead of classifying emails into folders like in *Outlook* (Windows) or *Evolution* (Linux), emails are classified by assigning tags to them. So instead of having a disjoint N:1 classification (a email can be in one and only one folder, and a folder can contain many emails), in *gmail* or *thunderbird* there is a N:M classification (a email can have several tags, and a tag can be applied to several emails)

See also:

- [Tags in Gramps](wiki:Tags_in_Gramps)

  
Likewise, when you have a big tree, you might want to make subsets of the tree, and these subsets might be overlapping. For example, the subsets of your fathers family and your mothers family, some subset of your family that emigrated to Australia.

The idea is to assign a different tag to each subset: *Paternal*, *Maternal*, *Australia* and *ToDo* for example.

The differences with Gramps previous **Markers** are like the folders for emails. A person can be given at most one marker. Tags are thus are like multiple-valued markers.  

Go to the Menu **Edit -\>Tag**.

<div class="thumb tright">

<div class="thumbinner" style="width:302px;">

![[_media/Menu-Edit-Tag-Options-60.png]]

<div class="thumbcaption">

<div class="magnify">

<a href="/wiki/index.php/File:Menu-Edit-Tag-Options-60.png" class="internal" title="Enlarge"></a>

</div>

Fig. 14.8 Tag actions from Edit menu

</div>

</div>

</div>

  

Or click the Toolbar <span class="kbd" style="border: 1px solid; color:#5e4638; background-color: #f9f9f9; border-bottom-width: 2px; -moz-border-radius: 3px; -webkit-border-radius: 3px; border-radius: 3px; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">Tag</span> button.

<div class="thumb tright">

<div class="thumbinner" style="width:283px;">

![[_media/Toolbar-TagSelectedRows-Icon-DropDownMenu-overview-example-60.png]]

<div class="thumbcaption">

<div class="magnify">

<a href="/wiki/index.php/File:Toolbar-TagSelectedRows-Icon-DropDownMenu-overview-example-60.png" class="internal" title="Enlarge"></a>

</div>

Fig. 14.9 Available Tag actions from "Tag selected rows" Toolbar icon - drop down menu overview - example

</div>

</div>

</div>

  
See also [Tag Report](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_6#Tag_Report)  

### <span id="New_Tag_dialog" class="mw-headline">New Tag dialog</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

<div class="thumb tright">

<div class="thumbinner" style="width:452px;">

![[_media/NewTag-dialog-ShowingMultipleListSelection-example-50.png]]

<div class="thumbcaption">

<div class="magnify">

<a href="/wiki/index.php/File:NewTag-dialog-ShowingMultipleListSelection-example-50.png" class="internal" title="Enlarge"></a>

</div>

Fig. 14.10 Attaching a "New Tag" to multiple list entry selections - example with "New Tag" dialog

</div>

</div>

</div>

You are able to add a new tag either a single or multiple list entries from any of the list views, by making the selection and then using the New Tag dialog.

<table style="width:40%;margin-top:+.7em;margin-bottom:+.7em;background-color: #ffd43385;border:1px solid #cccccc85; padding: 5px" data-align="left">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td>![[_media/Gramps-notes.png]]</td>
<td><p>This article's content is incomplete or a placeholder stub.<br />
Please update or expand this section.</p></td>
</tr>
</tbody>
</table>

  

  

##### <span id="Tagging_a_selection_of_objects" class="mw-headline">Tagging a selection of objects</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Due to the **static** nature of tags, it might be useful to add a tag to a selection of objects. For example one should be able to select a number of person in the [Person View](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window#People_Category), and add them a new tag or an existing one.  

  

### <span id="Organize_Tags_Window" class="mw-headline">Organize Tags Window</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

<div class="thumb tright">

<div class="thumbinner" style="width:418px;">

![[_media/MenuEditTag-OrganizeTags-dialog-example-60.png]]

<div class="thumbcaption">

<div class="magnify">

<a href="/wiki/index.php/File:MenuEditTag-OrganizeTags-dialog-example-60.png" class="internal" title="Enlarge"></a>

</div>

Fig. 14.11 Organize Tags - dialog - example

</div>

</div>

</div>

The order in the **<span class="kbd" style="background:#D3D3D3; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">Organize Tags</span>** dialog defines the priority for coloring rows in the category views.

<table style="width:40%;margin-top:+.7em;margin-bottom:+.7em;background-color: #ffd43385;border:1px solid #cccccc85; padding: 5px" data-align="left">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td>![[_media/Gramps-notes.png]]</td>
<td><p>This article's content is incomplete or a placeholder stub.<br />
Please update or expand this section.</p></td>
</tr>
</tbody>
</table>

  

  

### <span id="Tag_selection_dialog" class="mw-headline">Tag selection dialog</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

<div class="thumb tright">

<div class="thumbinner" style="width:307px;">

![[_media/TagSelection-dialog-example-60.png]]

<div class="thumbcaption">

<div class="magnify">

<a href="/wiki/index.php/File:TagSelection-dialog-example-60.png" class="internal" title="Enlarge"></a>

</div>

Fig. 14.12 Tag selection in the Person Editor

</div>

</div>

</div>

When you use <span class="kbd" style="border: 1px solid; color:#5e4638; background-color: #f9f9f9; border-bottom-width: 2px; -moz-border-radius: 3px; -webkit-border-radius: 3px; border-radius: 3px; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">Edit the tag list</span> button from any of the Editor dialogs like **<span class="kbd" style="background:#D3D3D3; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">Person Edit</span>** the **<span class="kbd" style="background:#D3D3D3; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">[Tag selection](wiki:Gramps_6.0_Wiki_Manual_-_Filters#Tag_selection_dialog)</span>** dialog list is shown that lets you remove or assign existing custom tags. The tags are shown in alphabetical order.  

### <span id="Usage_of_tags" class="mw-headline">Usage of tags</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Here are a some ideas of operations that can be done with tags

#### <span id="Filtering" class="mw-headline">Filtering</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

<div class="thumb tright">

<div class="thumbinner" style="width:372px;">

![[_media/Sidebar-PeopleTreeView-Filter-TagDropDownList-example-60.png]]

<div class="thumbcaption">

<div class="magnify">

<a href="/wiki/index.php/File:Sidebar-PeopleTreeView-Filter-TagDropDownList-example-60.png" class="internal" title="Enlarge"></a>

</div>

Fig. 14.13 Gramps Filter SideBar - Tag list example

</div>

</div>

</div>

The most obvious use is that of filtering.

- Tags and filters both create subsets of the tree. However they have practical differences in usage.

Specifying your fathers family using filters is an easy thing; there are already filters based on some logic's that do it. On the other hand, specifying the people that emigrated to the USA is harder, while for the famous people in your family it is simply impossible as there is no logical rule. Tags are much more practical here.

However filters have the advantage of being **dynamical**. If you add an ancestor of your father in the database, it will be automatically added to the filter.

On the other hand, tags are **static**. When adding a famous person in the tree, you have to explicitly tag them as *FAMOUS*.

- The most immediate object that comes to mind are the individuals, and that is also the most useful. However, other objects could be tagged:
  - Places: For example "places to visit",
  - Lähde: Esim. "Lähteet saksaksi",
  - Lisätiedot: Esim. "lisätiedot kesken" tai "lisätiedot saksaksi",
  - Media: Esim. "Uncle Alfredin kuva".

Tagit on käytettävissä **päätietolajeissa**.

  

#### <span id="Tagit_sarake" class="mw-headline">Tagit sarake</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

<div class="thumb tright">

<div class="thumbinner" style="width:452px;">

![[_media/PeopleListView-ExampleTagColoredRows-50.png]]

<div class="thumbcaption">

<div class="magnify">

<a href="/wiki/index.php/File:PeopleListView-ExampleTagColoredRows-50.png" class="internal" title="Enlarge"></a>

</div>

Fig. 14.14 People (List) View - Showing "Tag" column and colored tag rows - example

</div>

</div>

</div>

Näet helposti tagisi lisäämällä valinnalla **Muokkaa valitun näkymän asetuksia** **<span class="kbd" style="background:#D3D3D3; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">[Sarakkeiden muokkaus](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Column_Editor)</span>** ikkunassa **<span class="kbd" style="background:#D3D3D3; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">Tagit</span>** sarakkeen listattavien kohteiden näkymään. Tagit näytetään sarakkeessa pilkulla erotettuna.

  
  

|  |  |  |
|:---|:--:|---:|
| <a href="/wiki/index.php/Gramps_6.0_Wiki_Manual_-_Settings/fi" class="mw-redirect" title="Gramps 6.0 Wiki Manual - Settings/fi"><strong>Edellinen</strong></a> | [**Hakemisto**](wiki:Fi:Gramps_6.0_Wiki-k%C3%A4ytt%C3%B6ohje) | <a href="/wiki/index.php/Gramps_6.0_Wiki_Manual_-_FAQ/fi" class="mw-redirect" title="Gramps 6.0 Wiki Manual - FAQ/fi"><strong>Seuraava</strong></a> |

<div class="LanguageLinks">

|  |  |  |
|----|----|----|
| ![[_media/Gramps-config-language.png]] | **[Languages](wiki:Portal:Translators):**  | [English](wiki:Gramps_6.0_Wiki_Manual_-_Filters)     • <span lang="da"><a href="/wiki/index.php/Gramps_6.0_Wiki_Manual_-_Filters/da" class="mw-redirect" title="Gramps 6.0 Wiki Manual - Filters/da">dansk</a></span>  • <span lang="de"><a href="/wiki/index.php/Gramps_6.0_Wiki_Manual_-_Filters/de" class="mw-redirect" title="Gramps 6.0 Wiki Manual - Filters/de">Deutsch</a></span>  • <span lang="es"><a href="/wiki/index.php/Gramps_6.0_Wiki_Manual_-_Filters/es" class="mw-redirect" title="Gramps 6.0 Wiki Manual - Filters/es">español</a></span>  • <span lang="fi"><a href="/wiki/index.php/Gramps_6.0_Wiki_Manual_-_Filters/fi" class="mw-redirect" title="Gramps 6.0 Wiki Manual - Filters/fi">suomi</a></span>  • <span lang="fr"><a href="/wiki/index.php/Gramps_6.0_Wiki_Manual_-_Filters/fr" class="mw-redirect" title="Gramps 6.0 Wiki Manual - Filters/fr">français</a></span>  • <span lang="he">[עברית](wiki:Gramps_6.0_Wiki_Manual_-_Filters/he)</span>      • <span lang="mk"><a href="/wiki/index.php/Gramps_6.0_Wiki_Manual_-_Filters/mk" class="mw-redirect" title="Gramps 6.0 Wiki Manual - Filters/mk">македонски</a></span>   • <span lang="nl"><a href="/wiki/index.php/Gramps_6.0_Wiki_Manual_-_Filters/nl" class="mw-redirect" title="Gramps 6.0 Wiki Manual - Filters/nl">Nederlands</a></span>      • <span lang="ru"><a href="/wiki/index.php/Gramps_6.0_Wiki_Manual_-_Filters/ru" class="mw-redirect" title="Gramps 6.0 Wiki Manual - Filters/ru">русский</a></span>   • <span lang="sq"><a href="/wiki/index.php/Gramps_6.0_Wiki_Manual_-_Filters/sq" class="mw-redirect" title="Gramps 6.0 Wiki Manual - Filters/sq">shqip</a></span>   • <span lang="sk">[slovenčina](wiki:Gramps_6.0_Wiki_Manual_-_Filters/sk)</span>   • <span lang="tr">[Türkçe](wiki:Gramps_6.0_Wiki_Manual_-_Filters/tr)</span> |

</div>

<table style="width:90%;margin-top:+.7em;margin-bottom:+.7em;background-color: #c0f0ff;border:1px solid #ccc; padding: 5px" data-align="center">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td>![[_media/Gnome-important.png]]</td>
<td style="text-align: left;"><strong>Special copyright notice:</strong> All edits to this page need to be under two different copyright licenses:
<ul>
<li>GNU Free Documentation License 1.2 - see <a href="/wiki/index.php/Gramps:Copyrights" title="Gramps:Copyrights">wiki copyright</a></li>
<li>GPL - see <a href="/wiki/index.php/Gramps:Manualcopyright" title="Gramps:Manualcopyright">manual copyright</a></li>
</ul>
<p>These licenses allow the Gramps project to maximally use this wiki manual as free content in future Gramps versions. If you do not agree with this dual license, then do not edit this page. You may only link to other pages within the wiki which fall only under the GFDL license via external links (using the syntax: [https://www.gramps-project.org/...]), not via internal links.<br />
Also, only use the known <a href="/wiki/index.php/Gramps_6.0_Wiki_Manual_-_Preface#Typographical_conventions" title="Gramps 6.0 Wiki Manual - Preface">Typographical conventions</a></p></td>
</tr>
</tbody>
</table>
