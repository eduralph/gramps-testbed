---
title: 'Fi:Gramps 6.0 Wiki-käyttöohje - Tietojen syöttäminen ja muokkaaminen: Tarkemmin
  - osa 2'
categories:
- Fi:Dokumentaatio
- Stub
managed: false
source: wiki-scrape
wiki_revid: 124084
wiki_fetched_at: '2026-05-30T18:31:41Z'
lang: fi
---

{{#vardefine:chapter\|7.2}} {{#vardefine:figure\|0}}

Edellisessä osassa oli tarkempi kuvaus siitä, kuinka henkilöitä ja heidän välisiä suhteitaan lisätään ja muokataan. Tässä osassa jatketaan Grampsin muilla tärkeillä perusolioilla.

## Tapahtumatietojen muokkaus

## Tapahtimien tietojen muokkaus

![[_media/EventsCategory-EventsListView-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Tapahtumat kategoria - Tapahtumat (lista) näkymä- esimerkki]]

Tapahtumalla voit tallentaa henkilöön löytämäsi informaation.

Lisättäessä tapahtuma avautuu ikkuna.

Tapahtuman lisäämiseksi tai päivittämiseksi siirry kategorian näkymään. Lisää uusi tapahtuma-painikkeella. {{-}} Olemassa oleva tapahtuma valitaan päivitykseen tapahtumien listasta. Napsauttamalla kahdesti sitä tai kerran painiketta avautuu tapahtuman muokkaus ikkuna. dialog. {{-}}

### Uusi tapahtuma ikkuna

![[_media/EditEvent-WindowFi-41.png|Kuva {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Tapahtumamuokkain]]

Tapahtumia muokataan dialogissa (Katso kuva. 7.2.1). Dialogi käynnistetään joko tai dialogista.

Voit syöttää tiedot suoraan ao. kenttiin.

Yläsassa ovat nähtävissä ja muokattavissa tapahtuman perustiedot:

1.  valitaan listavalikosta. Esim *Hautaus*, *Valmistuminen* jne.

2.  voi olla täsmällinen päivämäärä, väli (*jostakin...jonnekin, välillä...*), tai epätarkka päiväys (*noin...*).

3.  kenttään annetaan pidepi tapahtuman kuvaus. Jätä kenttä tyhjäksi, jos haluat täyttää sen automaattisesti [Extract Event Description](wiki:Gramps_6.0_Wiki_Manual_-_Tools#Extract_Event_Descriptions_from_Event_Data) työkalulla, joka tallentaa tiedon muodossa "Tapahtuman tyyppi, Sukunimi, Etunimi".

4.  on valittavissa aikaisemmin tallennetusita paikoista tai paikka voidaan syöttäämyös uutena. Myös paikan raahaaminen ja pudotus kenttän toimii.

5.  on tapahtuman ainutkertainen tunnus. Jätä kenttä tyhjäksi, jos haluat täyttää sen automaattisesti.

Yksityinen/julkinen painikkeesta tapahtuman saa yksityiseksi ja poistettavaksi raporteista.

Keskiosassa on lehtiö, jonka viidellä lehdellä on tietoja tapahtumasta. Napsauttamalla lehden kielekettä lehti avautuu ja tietoja voi katsella ja muokata.

### Uuden tapahtuman lehdet

Lehdet ovat seuraavat:

#### Lähteet ja lainaukset

  
lehdellä voi katsella ja muokata tapahtumaan liittyviä lähdetietoja listana. painikkeista voi lisätä, muokata ja poistaa lähdetietoon liittyvän viitteen. Huomaa että ja ovat käytettävissä vasta, kun listasta on valittu lähdeviite.

#### Lisätiedot

  
lehdellä voi katsella ja muokata tapahtumaan liittyviä lisätietoja. Lisätiedot kirjoitetaan tekstinsyöttökenttään, missä myös muokkaus tapahtuu.

#### Galleria

  
lehdellä on listattu tapahtumaan liitetyt mediatiedostot. Uuden lisäys avaa Mediaviitemuokkaimen, jossa muokata tiedoston metatietoja ja poistaa viittauksen tiedostoon. Huomaa Mediaviitemuokkaimen yäosassa oleva mahdollisuus rajata kuvasta näytettäväksi alue, joka on relevantti tässä tapahtumassa.

#### Ominaisuudet

  
lehdellä ovat tapahtumaan liitetyt tyyppi-arvo pareilla ilmaistut tiedot.

#### Viitteet

  
lehdellä ovat viittaukset tapahtumaan liitettyihin henkilöihin, paikkoihin jne.

Alimpana ovat ja painikkeet. Edellisen napsautus vie kaikki muutokset kantaan ja sulkee dialogin. Peruutus sulkee dialogin ja muutoksia ei viedä kantaan. Pressing painikkeesta mahdollisesti saatavilla olevaa ohjetietoa.

{{-}}

## Tapahtumaviitteiden muokkaus

Tapahtumaviitteet yhdistävät tapahtuman siihen liittyviin henkilöihin. Napsauttamalla kahdesti henkilöä avautuu Henkilösuhteiden dialogi, jossa voi katsella ja muokata henkilön suhdetta tapahtumaan.

### Tapahtumaviitteen muokkain

![[_media/PersonEventTab-EventReferenceEditorFi-41.png|Kuva {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Tapahtuman tietoja]]

Kun lisätään tapahtumaviite taphtumalehdellä, avautuu seuraava dialogi:

Dialogissa on kaksi pääotsikkoa, ja .

- osiossa on tiettyyn tapahtumaviitteeseen liittyvät tiedot: , , .

- osiossa on: , , , , , .

Aseta "Ensisijainen" henkilön rooliksi tässä tapahtumassa, jos hän on "päähenkilö", muuten kuvaava rooli kuten Todistaja,....

{{-}}

## Mediatiedostojen tietojen muokkaus

Median tietojen muokkaamiseksi siirry Media näkymään, valitse kohde ja napsauta kahdesti sitä tai kerran työkalupalkin painiketta, jolloin avautuu seuraava dialogi:

### Uusi mediatiedosto ikkuna

![[_media/EditMedia-MediaPropertiesEditorWindowFi-41.png|Kuva {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Mediaominaisuuksien muokain]]

Kohteen esikatselukuva ja sen ominaisuuksia (ID, Polku, Päivämäärä ja Kohteen tyyppi).

1.  Kuvaava tiedostolle.

2.  yksilöi kohteen ainutkertaisesti, jätä Grampsin muodostettavaksi.

    1.  Tämän median tietosuoja-kuvakkeesta (oletus) tai

3.  voi olla esim. kuvan ottopäivä.

    1.  painikkeella avataan **** ikkuna.

4.  kertoo mistä kohde löytyy koneeltasi. Gramps ei talleta kohdetta omaan kantaansa, se tallettaa vain saantopolun! Asetuksissa voit asettaa suhteellisen polun, ks. [Relative Path](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Preferences) , millä vältät toistuvasti syöttämästä kohteittesi saantopolun. [Media Manager](wiki:Gramps_6.0_Wiki_Manual_-_Tools#Media_Manager...) työkalusta voi olla apua mediatiedostojen polkujen hallinnassa.

5.  arvo osoittaa mediatiedoston tyypin.

Dialogin keskiosassa on lehtiö, jossa on viisi lehteä eri tietoja varten. Lehti avautuu napsauttamalla sen kielekettä. Dialogin alaosassa ovat ja painikkeet. painikkeesta viedään kaikki muutokset kantaan ja suljetaan dialogi. painike sulkee dialogin ilman että muutoksia talletettaisiin.

### Uuden mediaikkunan lehdet

Kielekkeet edustavat seuraavia mediatiedostojen tietoryhmiä:

#### Yleistä

lehdellä voit katsella ja muokatakohteen otsikkoa ja päivämäärää. Voit syöttää ne suoraan ao. kenttiin. Päivämääräkentän oikealla puolella on painike, josta avautuvalla **Päivämäärän valinta** dialogilla voi myös asettaa päivämäärän.

#### Ominaisuudet

lehdellä voit katsella ja muokata median tietoja, jotka on talletettu Ominaisuuksina. Lehden alaosassa on lista mediaan talletetuista ominaisuuksista. , , ja painikkeista voit lisätä, muokata ja poistaa ominaisuuden. Huomaa että ja ovat käytettävissä vain jos listasta on valittuna ominaisuus. Ominaisuuden napsauttaminen kahdesti avaa Ominaisuus-dialogin. Sen yläosasssa on valitusta omainaisuudesta perustiedot ja alaosassa lehtiö (lainaukset, ominaisuudet, lisätiedot ja viitteet).

#### Lisätiedot

lehdellä on tiedot, joiden tallettamiseen ei löydy muuta sopivampaa kohdetta. Lisätiedot sopivat erityisesti sellaisen informaation tallettamiseen, johon ei sovi ominaisuuksien "parametri-arvo" muoto. Tietojen tallentamiseksi on käytettävissä tekstinsyöttökenttä.

#### Viitteet

lehdeltä ilmenee, viittaavatko muut kohteet tähän mediaan. Viitelista on järjestettävissä sarakeotsikoista: , , tai . Viitteen napsauttaminen kahdesti avaa ao. toisen kohteen katselua ja päivitystä varten.

{{-}}

## Median viitteiden muokkaus

When Media Object references connect a Media Object to an other object on a tab, the file selector from the dialog appears so you can select the media object. {{-}}

### Valitse mediatiedosto ikkuna

![[_media/Select-a-media-object-file-selector-example_fi_-42.png|Kuva. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Uuden mediatiedoston valintaikkuna - esimerkki]]

voit esikatsella ja valita mediatiedoston jonka haluat liittää, ja samalla voit muokata ehdotettua (Oletusarvona tiedostonimi ilman tiedostopäätettä).

- (valintaruutu on oletusarvoisesti valitsematta ensimmäisellä kerralla ja valinta muistetaan seuraavan tiedoston valinnassa.)

{{-}}

### Medianviitteiden muokkaus ikkuna

![[_media/Mediaobj_refFi-41.png|Kuva {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Median viitteet]]

Viitteen yhdistäessä Median toiseen kohteeseen näkyy dialogissa:

- Alueen kulmat : x1, x2, y1, y2.

osiossa voi määrittää mediasta rajatun alueeen. Voi asettaa alueen vasemman yläkulman ja oikean alakulman hiirellä tai painikkeilla. Piste (0,0) on kuvan vasen yläkulma ja (100,100) oikea alakulma.

- Yksityisyys

painikkeella voit merkitä tiedot yksityisiksi tai julkisiksi.

{{-}}

## Paikkatietojen muokkaus

Muokataksesi paikkojen tietoja valitse vasemmasta reunasta Paikat kategoria ja valitse paikkojen listasta haluamasi paikkakohde. Napsauta kahdesti sitä tai napssauta kerran työkalupalkin painiketta, jolloin avautuu seuraava dialogi:

### Paikkamuokkain ikkuna

![[_media/PlaceEditor-dialog-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Paikka muokkain ikkuna]]

Dialogissa on kahdeksan kenttää:

1.    
    tämän paikan koko nimi.

2.    
    paikkakunnan tai paikan nimi.

3.    
    minkälainen paikka tämä on. Esim. "Kylä", "Kaupunki".

    1.  Pudotusvalikosta löytyvät vakiotyypit on suomennettu englanninkielisistä tyyppinimistä, jotka välittyvät sukupuun tietoja Grampsista tulostiedostoon vietäessä näillä engl. nimillä
    2.  Kenttään voi kirjoittaa myös muun paikkatyypin (esim. "Hautausmaa"). Tällainen käyttäjän nimeämä tyyppi sijoittuu tyyppien pudotusvalikkoon vakiotyyppien jälkeen ja se menee tietoja pois vietäessä suomenkielisenä tulostiedostoon.

4.    
    paikan sijainti päiväntasajan yläpuolella desimaali- tai astenotaatiolla. Kelvollisia arvoja ovat esim. 12.0154, 50°52'21.92"N, N50º52'21.92" tai 50:52:21.92. Voit asettaa arvot Kartat näkymässä hakemalla paikan tai karttapalvelussa Paikka näkymän kautta.

5.    
    paikan sijainti peruspiiriin (Greenwichiin, meridiaaniin) verrattuna desimaali- tai astenotaatiolla. Kelvollisia arvoja ovat esim. -124.3647, 124°52'21.92"E, E124º52'21.92" tai 124:52:21.92. Voit asettaa arvot Kartat näkymässä hakemalla paikan tai karttapalvelussa Paikka näkymän kautta.

6.    
    jos paikan leveys- ja pituuskoordinaatit saadaan kopioitua yhtenä tietona ja se pudotetaan tähän yhteiskopiokenttään, leveys- ja pituuskoordinaatit kopioituvat kumpikin siitä omaan kenttäänsä. Edellytys on, että yhteiskopiossa koordinaatit on erotettu toisistaan pilkulla (esim. Akaan kohdalla "61°10′00″N, 23°52′05″E".

7.    
    ainutkertainen tunnus paikan yksilöimiseksi. Jätä Grampsin muodostettavaksi.

8.    
    tähän paikkaan liittyvä koodi. Esim. suuntanumero tai postinumero.

{{-}}

Dialogin toisen osan muodostaa lehtiö, jossa on seitsemän kielekettä ja lehteä, joilla on eri informaatiota. Napsauta kielekettä informaation katsomiseksi tai muokkaamiseksi. Dialogin alaosassa ovat ja painikkeet. painikkeesta talletetaan kantaan kaikkien lehtien tietojen muutokset ja suljetetaan dialogi. painikkeesta suljetaan dialogi ilman muutosten tallentamista.

{{-}}

### Paikkalehtiön kielekkeet ja lehdet

Kielekkeet osoittavat seuravia paikkatietojen ryhmiä:

#### Ympärillä

![[_media/PlaceEditor-EnclosedBy-tab-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Ympärillä" lehti "Paikkamuokkain" - ikkunassa - esimerkki]]

  
Grampsin paikat tallennetaan hierarkisesti. lehdellä voit linkittää paikan toisiin, hierarkiassa ylempänä oleviin paikkoihin. Jokaisessa linkissä on ylempi paikka ja valinnaisesti aikamäärite. Painikkeilla , ja voit lisätä linkin, muokata sitä ja poistaa sen. Huomaa että ja painikkeet ovat käytettävissä vasta kun olet valinnut linkin listalta. Yleissääntönä "maa/valtio" on ylein taso hierarkiassa eikä sitä linkitetä enää muuhun ylempään paikkaan.

See also: [Enclosed By](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Enclosed_By) Gramplet {{-}}

##### Valitse paikka ikkuna

![[_media/SelectPlace-SelectorDialog-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Valitse paikka - ikkuna - esimerkki]]

valintaikkunassa voit valita olemassaolevan paikan ja avata paikan ikkunaan.

Pudotusvalikosta voit valita suodatusvaihtoehdon ja painikkeella suodattaa listan valittavissa olevista paikoista.

- **Nimi sisältää** (oletus)
- Nimi ei sisällä
- ID sisältää
- ID ei sisällä
- Tyyppi sisältää
- Tyyppi ei sisällä
- Nimike sisältää
- Nimike ei sisällä
- Viimeisin muutos sisältää
- Viimeisin muutos ei sisällä

{{-}}

##### Paikkaviite muokkain

![[_media/PlaceReferenceEditor-dialog-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Paikkaviite muokkain - ikkuna - esimerkki]]

ikkuna avautuu, kun paikkaan lisätään hierarkiaan ylempi paikka Ympärillä -kielekkeessä painikkeella. Ikkuna on sama kuin millä talletetaan uusi paikka, mutta ikkunan ylärivillä on lisäksi kenttä, johon voi syöttää hierarkialiitoksen aikamääritteen. Esim. "1859 jälkeen" tarkoittaa, että talo N on vuodesta 1859 sisältynyt kylään X.

{{-}}

#### Vaihtoehtoiset nimet

  
lehdellä voit hallinnoida nimen muita tunnettuja muotoja. Painikkeilla , ja voit lisätä lnimen, muokata sitä ja poistaa sen. Huomaa että ja painikkeet ovat käytettävissä vasta kun olet valinnut linkin listalta.

Painikkeet avaavat ikkunan.

#### Lähde Lainaukset

  
lehdellä voit katsella ja muokata paikkaan liittyviä lähteitä. Lehden pääosan vie lista, jossa on tietokantaan talletetetut lähteet paikalle. , ja painikkeilla listään, muokataan ja poistetaan paikkaan liittyviä viitteitä lähteisiin. Huomaa että ja painikkeet ovat käytetävissä vasta kun listalta on valittu lähdeviite.

#### Lisätiedot

  
lehdellä ovat paikkaan liittyvät kommentit tai lisätiedot. Niiden lisäämiseen ja muokkaamiseen on käytettävisä tekstin syöttökenttä.

#### Galleria

  
lehdellä voit tallettaa ja katsella paikkaan liittyviä kuvia ja muita mediatiedostoja. Lehden pääosan vie niiden lista esikatselukuvineen. Äänitteistä, viedeoista jne näytetään vain Grampsin yleinen kuvake. , , ja painikkeilla voi lisätä uuden median, lisätä viitteen mediaan, muokata kuva ja poistaa linkin paikkaan liitettyyn mediaan. Huomaa että ja painikkeet ovat käytetävissä vasta kun listalta on valittu media.

#### Internet

  
ovat paikkaan liittyvät olennaiset nettiosoitteet. Lehden pääosan vie niiden lista . Lehden alaosassa on yksityiskohtaisia tietoja listasta valitusta osoitteesta. , , ja painikkeilla voi lisätä , muokata ja poistaa nettiosoiteen. painike (kuvakkeessa on vihreä nuoli ja keltainen ympyrä) avaa valitun osoitteen sivun selaimeesi. Huomaa että ja painikkeet ovat käytetävissä vasta kun listalta on valittu nettiosoite.

#### Viitteet

  
lehdellä näkyvät kaikki viitteet valittuun paikkaan. Tätä informaatiota ei voi muuttaa dialogissa, vaan viittaus (esim. syntymätapahtuma) on avattava ja muokattava paikkaviittausta siellä.

{{-}}

### Paikannimi muokkain ikkuna

![[_media/Place_name_editor_fi-42.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Paikannimi muokkain]]

Voit käyttää , ikkunan muokkaa painikkeella.

ikkunassa voit lisätä / muokata seuraavia tietoja:

- paikan nimi

- Ajanjakso jonka nimi on voimassa

  - ![[_media/gramps-date-edit.png]] päivämäärä painikkeella

- Kieli, jolla nimi on kirjoitettu. Kelvolliset arvot ovat kaksi merkkiset

ISO-koodit esimerkiksi: fi, fr, de, nl ... Katso Wikipedian voimassaoleva luettelo [ISO 3166-1](https://en.wikipedia.org/wiki/ISO_3166-1#Current_codes) {{-}}

### Tuetut pituuspiiri/leveyspiiri muodot

Kun luot tai muokkaat paikkaa, pituus- ja leveyspiirien mahdolliset muodot ovat :

`       'D.D4'    : astenotaatio, 4 desimaalia`  
`                   esim. +12.0154 , -124.3647`  
`       'D.D8'    : astenotaatio, 8 desimaalia (tarkuus kuten ISO-DMS) `  
`                   esim. +12.01543265 , -124.36473268`  
`       'DEG'     : aste, minuutit, sekuntit notaatio`  
`                   esim. 50°52'21.92"N , 124°52'21.92"E ° on UTF-8 koodina c2b00a`  
`                   tai N50º52'21.92" , E124º52'21.92" º on UTF-8 koodina c2ba0a`  
`                   Sekunnit voivat olla kaksinkertaisten " tai yksinkertaisten  ' lainausmerkkien ympäröimät                    `  
`                   Ilmansuunnan ilmaisevat kirjaimet N/S/W/E voivat sijaita ennen numeroarvoa tai niiden`  
`                   jälkeen.`  
`       'DEG-:'   : aste, minuutit, sekuntit : erottimella`  
`                   esim. -50:52:21.92 , 124:52:21.92`  
`       'ISO-D'   : ISO 6709 astenotaatio mallia ±DD.DDDD±DDD.DDDD`  
`       'ISO-DM'  : ISO 6709 aste, minuutit notaatio mallia ±DDMM.MMM±DDDMM.MMM`  
`       'ISO-DMS' : ISO 6709 aste, minuutit,sekuntit notaatio mallia ±DDMMSS.SS±DDDMMSS.SS`

{{-}}

## Lähdetietojen muokkaus

### Uusi lähde Ikkuna

![[_media/EditSource-SourceEditorWindowFi-41.png|Kuva {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Lähdemuokkain]]

Dialogin yläosassa ovat lähteen perustiedot: , , , ja . Perustiedot syötetään kukin omaan kenttäänsä.

1.    
    Lähteen nimike.

2.    
    Lähteen tekijä tai tekijät.

3.    
    Lähteen julkaisutiedot kuten paikka, vuosi, kustantaja jne , ...

4.    
    Lyhennetty nimike lajitteluita ja lähteen hakemista varten.

    1.  Lukko-kuvake.

5.    
    Identifioi lähteen ainuskertaisesti. Jätä Grampsin määritettäväksi.

6.  :

    1.  

### Uuden lähteen kielekkeet

Dialogin alaosassa on lehtiö, jonka lehdillä on lisää tietoja kielekkeiden nimien mukaisesti :

#### Lisätiedot

  
lehdellä on paikka lähettä koskeville lisätiedoille tai kommenteille. Ne lisätään ja niitä muutetaan tekstinmuokkauskentässä. Lehdellä on kieleke, jossa näytetään vain ensisijaisia kohteita: Henkilö, Perhe, Tapahtuma, Paikka tai Media. Toissijaisiin kohteisin kuten nimiin tai ominaisuuksiin on mentävä ensisijaisten kohteiden kautta.

#### Galleria

  
lehdellä voi tallettaa ja katsella valokuvia ja muita mediatiedostoja, jotka liittyvät lähteeseen (esim. valokuva syntymätodistuksesta). Lehden keskeisen osan muodostaa lista näistä kohteista sekä myös kustakin esikatselukuva. Muista kohteista kuten äänitteistä ja videoista näytetään yleinen Grampsin kuvake. , , ja painikkeista voit lisätä uuden kuvan, lisätä kannassa olevaan kuvan viitteen, muokata kuvaa ja poistaa mediatiedoston viitteen. Huomaa että ja painikkeet ovat käytettävissä vasta kun listasta on valittuna kohde.

#### Ominaisuudet

  
lehdellä ovat lähteeseen liitetyt tyyppi-arvo pareilla ilmaistut tiedot. Ne ovat muuten samanlaisia kuin "Ominaisuudet" eräillä muilla Grampsin kohteilla. Erona niihin kuintekin, että näihin "Ominaisuuksiin" ei voi liittää viitteitä ja lisätietoja.

<!-- -->

  
Lehden keskeisen osan muodostaa lista tyyppi-arvopareista. ja painikkeista voit voit listä ja poistaa näitä pareja. Tyypin tai arvon päivittämiseksi valitse ensin arvopari ja napsauta sitten tyypin tai arvon solua. Muokkauksen jälkeen napsauta solun ulkopuolelle poistuaksesi muokkaustilasta.

#### Arkistot

![[_media/NewSource-Repositories-tab-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Arkistot" lehti "Uusi lähde" - ikkunassa - esimerkki]]

  
lehdellä ovat lista viitteistä arkistoihin, joista lähde sisältyy. Lista lajitellaan sarakeotsikoista: , , ja . Napsauttamalla viitettä kahdesti sitä voi katsella ja muokata. Käyttöön tulevat painikkeet uuden arkiston lisäämiseen, olemassa olevaan arkistoon linkittämiseen ja linkin muokkaamiseen ja poistamiseen.

##### Valitse arkisto

![[_media/SelectRepository-SelectorDialog-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Valitse arksito - ikkuna - esimerkki]]

ikkunassa voit linkittää lähteen jo sukupuussa oleviin arkistoihin ja valinnan tehtyäsi se avautuu omaan ikkunaansa.

Voit käyttää myös painiketta, kun olet antanut hakuehdot pudotusvalikosta ja hakusana-kentässä:

{{-}}

#### Viitteet

  
lehdellä on lista muista kohteita, joista viitataan tähän lähteeseen. Lista lajitellaan sarakeotsikoista: , tai . Napsauttamalla viitettä kahdesti voi katsella ja muokata viittaavaa kohdetta.

{{-}}

## Lähdelainausten muokkaus

Lainaukset yhdistävät lähteen toiseen kohteeseen ja niillä voi antaa lisää tietoa lähteestä. Lainauksia voi liittää suureen joukkoon kohteita,

- [Henkilötietojen muokkaaminen](wiki:Fi:Gramps_6.0_Wiki-käyttöohje_-_Tietojen_syöttäminen_ja_muokkaaminen:_Tarkemmin_-_osa_1#Tietojen_syöttäminen_ja_muokkaaminen) (kuten heidän nimensä, osoitteensa jne),
- [Perhetietojen ja muiden suhdetietojen muokkaaminen](wiki:Fi:Gramps_6.0_Wiki-käyttöohje_-_Tietojen_syöttäminen_ja_muokkaaminen:_Tarkemmin_-_osa_1#Tietojen_syöttäminen_ja_muokkaaminen),
- [Tapahtuma- ja muiden niihin liittyvien tietojen muokkaaminen](wiki:Fi:Gramps_6.0_Wiki-käyttöohje_-_Tietojen_syöttäminen_ja_muokkaaminen:_Tarkemmin_-_osa_1#Tietojen_syöttäminen_ja_muokkaaminen),
- [Mediatiedostojen_tietojen muokkaus](wiki:Fi:Gramps_6.0_Wiki-käyttöohje_-_Tietojen_syöttäminen_ja_muokkaaminen:_Tarkemmin_-_osa_2#Mediatiedostojen_tietojen_muokkaus),
- [Places and various information about places](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_2#Editing_information_about_places),
- [Addresses of repositories](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_2#Editing_information_about_repositories).

Jokaiselle kohteelle on tarjolla yhteinen painikkeiden joukko:

-  (Luo ja lisää uusi lainaus ja lähde. Tämä käynnistää Lainaus dialogin.

-  (Lisää kannassa jo oleva lainaus tai lähde). Tämä käynnistää lähteen tai lainauksen valintadialogin.

-  (Muokkaa valittua lainausta). Tämä käynnistää Lainaus dialogin, jossa on valmiina lainauksen ja lähteen tiedot.

-  (Poista valittu lainaus). Tämä poistaa kohteelta lainauksen. Lainaus ei itse poistu kannasta, vaan se on liitettävissä toiseen kohteeseen.

Huomaa että and painikkeet on käytettävissä vasta kun lainaus on valittuna.

{{-}}

### Valitse lähde tai lainaus ikkuna

olemassa olevista lainauksista tai lähteistä avaa seuraavan dialogin: ![[_media/Select-source-or-citation-selector_fi-42.png|Kuva {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Lähteen tai lainauksen valitsija]]

Dialogissa valitaan nykyinen lähde tai nykyinen lainaus (ja siihen liittyvä lähde). Napsauttamlla kahdesti Viitteet-kielekettä saa näkyviin lähteeseen viittaavat lainaukset. Jos esim. lähteesi on kirja, lainaukset viittaavat kirjassa oleviin sivuihin. Lainausten puu-painikkeesta kunkin lähteen vasemmalla puolelle tulevasta kolmiopainikkeesta saa myös näkyviin listan lähteeseen viittaavat lainaukset. Jos sinulla on kirjan tiettyyn sivuun viittaava lainaus, voit valita tämän lainauksen ja jakaa sen. Toisaalta, jos kohteesta on viitattava uuteen sivuun, valitse lähde ja syötä sitten uusi sivu avautuvassa dialogissa.

Voit painikkeella ja hakusanalla hakea lähdettä tai lainausta seuraavilla pudotusvalikosta löytyvillä tekijöillä:

- Lähde: Nimike tai lainaus: Osa/sivu sisältää'''(oletus)
- Lähde: Nimike tai lainaus: Osa/sivu ei sisällä
- ID sisältää
- ID ei sisällä
- Viimeisin muutos sisältää
- Viimeisin muutos ei sisällä

{{-}}

### Uusi lainaus ikkuna

Valittuasi lainauksen tai lähteen tai jos valitset tai painikkeen, seuraava Lainaus muokkaus-ikkuna avautuu: ![[_media/EditCitation-NewCitationWindowFi-41.png|Kuva {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Lähdelainauksen muokkain, versiosta 4.0.4 lähtien]] Dialogissa on kaksi otsikkoa, ja .

#### Lainauksen tiedot

osiossa ovat tähän lähteeseen viittauksesta tarkemmat tiedot: , , ja . Luotettavuuden taso on valittavissa pudotusvalikosta. Loput tiedot syötetään ao. tekstinsyöttökenttiinsä.

1.    
    Tähän lähdeviitteesen liittyvä päivämäärä. Käytetään tavallisesti sen päivämäärän tallettamiseen, jolloin tieto on viety alkuperäiseen asiakirjaan (eikä tapahtumapäivää).

2.    
    Yksilöity paikka viitatulle tiedolle. Painotuotteissa tässä voi olla moniosaisen teoksen osan numero ja sivunumerot). Akakausilehdessä vuosikerta, lehden numero ja sivunumerot. Sanomalehdessä myös palstan numeroa. Julkaisemattomassa lähteessä esim. lehden tai sivun numero, taulukon numero tms. Henkikirjassa sivunumeron lisäksi rivinumero, asunnon numero ja perheen numero.

3.    
    Tiedon luovuttajan määrällinen arviointi tiedon luotettavuudesta, perustuen siitä olevaan näyttöön. Arviointia ei ole tarkoitettu poistamaan tiedon vastaanottajan omaa tarvetta näytön arvioimiseen.

    1.  Erittäin matala = Epäluotettava näyttö tai arviotieto.
    2.  Matala= Näytön kyseenalainen luotettavuus (haastattelut, väestölaskennat, suulliset tiedot sukulaisuuksista tai mahdollisesti vääristynyt, esim. muistelma.
    3.  Korkea= Toissijainen näyttö, tieto on esim tallettu virallisesti vasta jonkin aikaa tapahtuneen jälkeen.
    4.  Erittäin korkea = Suora ja ensiluokkainen näyttö, tai näyttöjen vahvistama.

##### Valitse olemassa oleva lähde

![[_media/SelectSource-selector-dialog-example-50.PNG|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Valitse lähde - ikkuna - esimerkki]]

ikkunassa voit kytkeä lainauksen jo sukupuussa olevaan lähteeseen..

painikkeella ja hakusanan perusteella voit hakea lähdettä seuraavien pudotusvalikosta löytyvien valintojen perusteella:

- **Nimike sisältää** (oletus)
- jne

### Lainausosion lehdet

Kielekkeet osoittavat lainauksen tietoryhmät:

##### Lisätiedot

lehdellä voi tallentaa lainauksesta lisätietoja ja kommentteja. Lehden keskeisessä osassa on lista lainaukseen liittyvistä lisätedoista ja se näyttää myös alkuosan lisätiedon tekstistä. , , , , and painikkeilla voit lisätä lisätiedon, jakaa valitun lisätiedon, muokata valittua lisätietoa, poistaa valitun lisätiedon ja muuttaa lisätiedon paikkaa listassa ylös- tai alaspäin. Huomaa että , , , ja painikkeet ovat käytettävissä vasta kun media on valittu listasta. isätiedon poistaminen poistaa sen vain tästä lainauksesta, se ei poista lisätietoa kannasta. Tutustu [details on editing notes](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_2#Editing_information_about_notes).

##### Galleria

  
lehdellä voit katsella ja tallettaa lainaukseen liittyviä valokuvia photos, videoita ja muita mediatiedostoja. Lehden keskiosassa on lista näistä. Kaikista kelvollisista kuvista näytetään esikatselukuva. Muista kohteista kuten äänitteistä, videoista jne näytetään vain tiedostotyypin kuvake.

.

  
, ja painikkeilla voit lisätä kuvan tietokantaan, linkata jo kannasta löytyvään kuvaan, muokata kuvaa ja poistaa mediatiedoston lainauksen galleriasta. Huomaa että ja painikkeet ovat käytettävissä vain kun listalta on valittu mediatiedosto. Silloin avautuu [Media reference editor](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_Editing_Data:_Detailed_-_part_2#Editing_Media_Object_References)

##### Ominaisuudet

lehdellä on "Avain/Arvo" parit, jotka liittyvät lainaukseen. Parit ovat samanlaisia kuin "Ominaisuudet" muissa Grampsin tietueissa.

Lehden keskisessä osassa on listattuna Avain/Arvo-parit. ja painikkeilla voit lisätä ja poistaa pareja. Avaimen tai Arvon muokkaamiseksi valitse ensin ao. pari. Napsauta sitten painiketta Avaimen valitsemiseksi, tai napsauta joko Avainta tai Arvoa ja syötä sitten tekstisi. Kun olet valmis, napsauta solun ulkopuolella poistuaksesi muokkaustilasta.

##### Viitteet

lehdellä listataan kaikki tähän lähteseen viittaavat tietueet, jos niitä on. Listan järjestystä muutetaan sen sarakeotsikoista: , tai . Napsauttamalla kahdesti tietuetta voit katsella ja muokata sitä.

### Jaetun lähteen tiedot

osiossa näytetään Lähteen , sen , ja . Varoituskuvake näytetään lähteen ollessa jaettu. Lähdettä muokataan tässä dialogissa kuten on kuvattu [editing infomation about sources](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_2#Editing_information_about_sources) (q.v.).

## Arkistojen tietojen muokkaus

Once you have selected a source, or if you had chosen the or buttons, then the dialog appears.

### Uusi arkisto ikkuna

Dialogin yläosassaon kolme kenttää:

1.  Arkiston (lähteiden talletuspaikka).

2.    
    arkiston ainutkertainen tunnus. Jätä Grampsin määritettäväksi.

3.  Arkiston , esim. Kirjasto, Albumi, ...
    1.  Lukko-kuvake.

4.  :

    1.  

### Uuden arkiston kielekkeet

![[_media/EditRepository-AddRepositoryWindowFi-41.png|Kuva {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Arkistomuokkain]]

Neljä kielekettä osoittavat arkistoa koskevat muut tietoryhmät:

#### Osoitteet

  
lehdellä voit katsella ja tallettaa arkiston eri osoitteita.

<!-- -->

  
Osoitelistassa näkyy kustakin osoitteesta perustiedot. Napsauttamalla osoitetta avautuu Osoitemuokkain dialogi ja siinä näkyy lisää tietoja osoitteesta. , ja painikkeilla voit lisätä, muokata ja poistaa osoitteita kannasta. Huomaa että ja painikkeet ovat käytettävissä vasta kun listasta on valittu osoite.

#### Internet

  
lehdellä voit katsella ja tallettaa arkiston eri nettiosoitteita. Niiden listassa ovat seuraavat sarakkeet:

1.  (Pudotusvalikko, jossa vaihtoehdot FTP, Nettihaku, Nettikotisivu, Sähköposti ja Tuntematon)

2.  (Osoite tyypin mukaiseen palveluun, esim. WWW-osoite tai sähköpostiosoite)

3.  .

, ja painikkeilla voit lisätä, muokata ja poistaa nettiosoitteita kannasta. "Siirry.." painike (kuvakkeena vihreä nuoli ja keltainen ympyrä) avaa selaimeen osoitteen mukaisen sivun, jos tyyppi on nettihaku tai -kotisivu. Huomaa etä ja painikkeet on käytettävissä vain, jos listasta on valittu osoite.

#### Lisätiedot

  
lehdellä voi tallettaa ja katsella arkistoon liittyviä lisätietoja ja kommentteja. Ne kirjoitetaan tekstinsyöttökenttään.

#### Viitteet

  
lehdellä on listattuna viittaukset tietokannan muihin tietueisiin, joista on viittaus tähän arkistoon. Listan järjestystä voi muuttaa sen sarakeotsikoista: , tai . Ao. tietuetta voi katsella ja muokata napsauttamalla kahdesta listassa olevaa viittausta.

{{-}}

## Lisätietojen muokkaus

### Lisätiedot lehti

Henkilöiden, lähteiden, jne dialogeissa on kieleke, josta avautuvassa sivussa on listattuna ao. tietueeseen liitetyt lisätiedot ja kommentit. Listassa voi vaihtaa niiden näkymisjärjestyksen halutuksi. Kuten muissakin lehdissä, tietueen ao. listassa on mahdollista lisätä uusia lisätietoja, liittää olemassa olean lisätiedon tähän tietueeseen (ns. jakaa lisätietueen tällekin tietueelle) ja poistaa lisätiedot tästä tietueesta (mikä ei kuitenkaan poistaa lisätietoja kannasta. Poistetun lisätiedon saa näkyviin myöhemmin.).

### Lisätietomuokkain

![[_media/EditNotes-NoteEditorWindowFi-41.png|Kuva {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Lisätietomuokkain]]

Luotaessa uutta lisätietoa tai muokatessa olemassa olevaa lisätietoa avautuu lisätietomuokkain. Siinä on kaksi lehteä, "Lisätieto" ja "Viitteet".

### Lisätieto

Lisätietolehdellä on seuraavat elementit

:\* Työkalupainikkeet lisätiedon muokkaamiseen. Voit ottaa yhden tai useita työkaluja käyttöön joko ennen lisätiedon syöttämistä tai käyttää niitä jo syötettyyn tekstiin.

::\* Peru, Tee uudelleen:

::\* kursivoi, vahvenna, alleviivaa: tekstieditoreista tuttuja toiminnallisuuksia

::\* Kirjasinlajin valinta: tarjolla kaikki käyttöjärjestelmäsi fontit.

::\* Kirjasimen koko:

::\* Kirjasimen väri: väri valitaan valintakiekosta, pipetillä tai numeerisina arvoina (huomaa että Kylläisyys-arvon oltava nollasta selvästi poikkeava, jotta väri näkyy)

::\* Taustaväri: tekstin taustaväri valitaan kuten kirjasimen väri.

::\* Poista muotoilut: Peruuttaa tekstiin tehdyt muotoilut

::\* Linkki: Luo linkin toiseen kohteeseen Grampsissa, kuten Henkilöön, Perheeseen, Tapahtuman, Liätietoon, jne. (ts. lisätieto näkyy toisen kohteen lisätiedoissa)

{{-}}

:\* Tekstinäkymän kontekstivalikko.

  
  
kontekstivalikko tärkein valinta on Oikeinkirjoitus. Se on käytettävissä systeemisi niissä kielissä, joissa on aktivoitu oikeinkirjoitustoiminnallisuus.

:\* Tekstinäkymän muita ominaisuuksia

::\* : lisätiedon ainutkertainen tunnus. Jos jätetään tyhjäksi, tunnus määrätään Grampsin toimesta asetuksien mukaisesti

::\* : Valitaan pudotusvalikosta

::\* valintaruutu: Gramps muotoilee tekstin oletusarvoisesti raportteja varten; rivinvaihdot ja ylimääräiset välilyönnit ohitetaan ja kappaleiden väliin tulee tyhjä rivi. Jos on rastitettu, Gramps olettaa ylimääräisten välilyöntien ja muiden syöttämiesi merkkien olevan tarkoitettuja. Käytä rastia taulukoissa, kirjallisuusotteissa, ... . Käytä tasavälistä kirjasintyyppiä säilyttääksesi muotoilu. Yritä olla käyttämättä muotoilua, jos et tarvitse sitä, raporteista tulee niin kauniimpia.

::\* : kuten muissakin tietueissa voit yhdellä napsutuksella merkitä tämän lisätiedon yksityiseksi, jotta se jää pois raporteista.

### Viitteet

lehdellä on lista tähän lisätietoon viittaavista kaikista muista tietueista. Listan järjestystä voi muuttaa sarakeotsikoista: , tai . Napsauttamalla kahdesti viitettä voit katsella ja muokata ao.tietuetta.

##### Linkkimuokkain

![[_media/Link-editor-dialog-42.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Link Editor - dialog]]

on seuraavat vaihtoehdot:

- voit luoda sisäisen Gramps-linkin kohteille, kuten henkilö, perhe, tapahtuma, paikka, lisätieto, arkisto, lähde, media ja ulkoinen Internet-osoite.

  - painike

  - painike

- - painike

- 

Katso myös

- [Internet Address Editor](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1#Internet_Address_Editor)
- [Lisätietolinkki raportti](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_6#Note_Link_Report)

{{-}}

### Lisätietojen muotoilut raporteissa

Kirjasinmuotoiluja kuten **vahvennettu**, väri, <u>alleviivaus</u>, ... voidaan lisätä lisätiedon tekstiin. Lisätietoa voidaan muotoilla myös välilyöntien ja -rivien osalta. Muotoilujen vaikutus riippuu tulostetyypistä. Seuraavassa on yhteenveto siitä, mitä on odotettavissa.

1.  **Pdf** ja **tulosta tiedostoon** tukevat täysin muotoiluja
2.  **ascii** tulostus poistaa kaikki kirjasinmuotoilut ymmärrettävistä syistä
3.  **LaTeX** tulostus tulkitsee kirjasinmuotoilut parhaansa mukaan. Taitokielenä LaTeX ei kovin sopeudu käyttäjän määrityksiin, mikä pienentää LaTexin käytettävyyttä. Se kykenee kuitenkin seuraavaan:

:\* **vahvennettu**, <u>alleviivaus</u> and *kursiivi* on tuettuna

:\* kirjasinkoon LaTeX mäpää kokomääritteisiinsä epämääräisesti

:\* tasasuuret kirjasimet näytetään tasavälisinä

:\* väriä ja fonttia ei tueta

:\* välilyöntien ja -rivien muotoilua tuetaan

1.  **Kertova-nettisivusto**. Monet käyttävät Grampsin tuottamaa nettisivustoraporttia ainistonsa helppona työkaluna. Kertova-nettisivusto yrittää kunnioittaa lisätietojen muotoiluja. Kyseessä on kuitenkin tulkinta, ei yksi yhteen lopputulos.
2.  **ODF** tulostus ei tue kirjasinmuotoiluja toistaiseksi.
3.  **RTF** tulostus ei tue kirjasinmuotoiluja toistaiseksi.
4.  **HTML** tulostus ei tue kirjasinmuotoiluja toistaiseksi.

{{-}}

[Category:Fi:Dokumentaatio](wiki:Category:Fi:Dokumentaatio)
