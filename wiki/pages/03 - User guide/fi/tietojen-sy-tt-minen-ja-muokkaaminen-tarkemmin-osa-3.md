---
title: 'Fi:Gramps 6.0 Wiki-käyttöohje - Tietojen syöttäminen ja muokkaaminen: Tarkemmin
  - osa 3'
categories:
- Fi:Dokumentaatio
managed: false
source: wiki-scrape
wiki_revid: 120117
wiki_fetched_at: '2026-05-30T18:32:17Z'
lang: fi
---

{{#vardefine:chapter\|7.3}} {{#vardefine:figure\|0}}

Edellisessä osassa annettiin tarkempi katsaus, kuinka Grampsissa luodaan ja muokataan tärkeimpiä kohteita. Tässä osassa jatketaan syventymistä mm. lähteisiin, henkilöihin...

## Nimimuokkain

Nimiä muokataan dialogissa:

### Nimimuokkain ikkuna

![[_media/EditPerson-NameEditorWindowFi-41.png|Kuva {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Nimimuokkain]]

Ikkunan yläosassa voi valita nimelle tyypin (esim. syntymänimi, avionimi jne) ja syöttää nimen osissa. Ensin etunimeen liittyvät osat, sitten sukunimeen liittyvät. Alimpana dialogissa on lehtiö, jonka sivuilla annetaan nimilajittelua vaikuttavia ohjaustietoja ja nimeen liittyviä päivämääriä, lähteitä ja lisätietoja.

{{-}}

#### Tyyppi

Pudotusvalikko nimen tyypin valitsemiseen. Huomaa, että Gedcom-tuonnin kautta valikkoon tulee muitakin kuin Grampsiin määritellyt perustyypit.

#### Etunimien osio

Etunimimet osiossa ovat kaikki etunimeen liittyvät tiedot, joita voit syöttää etunimen puitteissa.

- , Henkilön viralliset etunimet syötetään tähän.

- , ensijaisesti käytetty etunimistä. Esim. "Mailis", jos Liisa Mailis Niemi käyttää ainoana etunimenään sitä. Huomaa että etunimilyhenteet ja muut "mukaelmat" kirjataan Lempinimeksi. Saksassa ja muuallakin on tapana alleviivata kutsumanimi etunimistä (ks.myös [here](http://www.gramps-project.org/wiki/index.php?title=CallName)).

- , henkilökohtainen titteli, kuten Tohtori tai Tri voidaan tallettaa tähän.

- , Henkilönimen henkilöön liittyvä liite kuten Junior (Jr.) tai III, pitäisi tallettaa täällä.

- , Henkilön etunimilyhenteet ja muut "mukaelmat" talletetaan tähän. Esim. Nikke, jos Niiloa kutsutaan siten.

#### Sukunimien osio

Dialogin keskiosassa olevassa Sukunimien osiossa ovat kaikki sukunimiin liittyvät tiedot, joita voit syöttää sukunimien puitteissa. Grampsiin voi talletaa useita sukunimiä kuten monenlaatuisia sukunimiä.

- etuliite (kuten "de" tai"van") ei vaikuta lajitteluissa.

- sukunimen perusosa.

- usein käytetty matronyymisissä tai patronyymisissä sukunimirakenteissa , kuten *dotter* (tiettävästi käytössä espanjalaisissa nimissä, ei liene sovellu suolaisiin nimiin?).

- nimen alkuperä, huomaa että kenttään voi syöttää muunkin vaihtoehdon kuin mitävalintalistasta löytyy (esim. Sotilasnimi on suomalaisessa sukututkimuksessa tärkeä alkuperä.

- on radiopainike, jolla voi valita henkilön useista sukunimistä ensisijaisesti käytettävän sukunimen.

Sukunimien listan alapuolella on kenttä \* tiedolle. Se osoittaa kansanomaisemman nimen, jolla perhe tavallisesti tunnetaan.

Katso myös: [Names wiki entry](wiki:Names_in_Gramps)

Dialogin oikeassa yläkulmassa olevasta kuvakkeesta voi asettaa nimitietueen yksityiseksi. Tällä voit ohittaa nimen raporteista, mikäli olet raportin asetuksissa asettanut tämän valinnan päälle.

### Nimi muokkaimen välilehtiä

#### Yleiset

Alimpana dialogissa on lehtiö, jonka sivuilla annetaan nimilajittelua vaikuttavia ohjaustietoja ja nimeen liittyviä päivämääriä, lähteitä ja lisätietoja.

- kenttä tarjoaa vaihtoehtoisen mahdollisuuden ryhmittää nimi muutenkin kuin sen sukunimen perusteella. Tätä voidaan tarvita esim. savolaisessa sukunimen naismuodossa "Lapitar", jos henkilö halutaan "Lappalainen" ryhmään.

  - Kenttään voi kirjoittaa, kun äärimmäisenä oikealla valinta on tehty.

  
Henkilöt näytetään siinä nimimuodossa, joka on määritetty Asetuksissa (oletusarvo).

Tässä osiossa voit kuitenkin varmistaa henkilön näkymisen muussa nimimuodossa. Huomaa myös Muokkaa\>Asetukset\>Näyttö ja \>Teksti valintojen mahdollisuudet.

- ja määrittävät sen, miten nimi näkyy Henkilöt listassa ja raporteilla. Järjestä menee Grampsin asetuksissa olevan nimilajittelun edelle. Esim. täällä voit määrittää, että sukunimetön mutta patronyyminiminen henkilö lajitellaan patronyyminimi, etunimi-järjestykseen, kun muut menevät sukunimi, etunimi järjestykseen.

  
mahdollistaa sen, että vaikka lajittelut menevät muokatulla tavalla, niin näkymissä nimet näytetään kuten Asetuksissa on määritelty.

Ryhmitetyt henkilöt-näkymässä henkilöt on ryhmitetty sukunimitäin ensisijaisen sukunimensä perusteella. Tämän edelle menee henkilön Nimi-dialogissa asetettu Ryhmitä-tieto. Gramps kysyy, haluatko ryhmittää uudelleen vain ao. henkilön vai kaikki henkilöt, joilla on sama ensisijainen sukunimi.

- tiedolla voi antaa informaatiota tämän nimen voimassaoloajasta - käytä aikavälejä jos tarpeen. Päivämäärä kuvake avaa päivämäärämuokkaimen, ks. [Päivämäärien muokkaus](wiki:Fi:Gramps_6.0_Wiki-käyttöohje_-_Tietojen_syöttäminen_ja_muokkaaminen:_Tarkemmin_-_osa_1#P.C3.A4iv.C3.A4m.C3.A4.C3.A4rien_muokkaus). Esim. Avionimelle nimen päivämäärä on ensimmäinen päivämäärä, jolloin avionimeä käytettiin.

#### Lähde Lainaukset

lehdellä näkyvät tiedot tähän nimeen liitetyistä lähteistä ja lainauksista ja painikkeet niiden käsittelyyn. Lehden keskeisen paikan vie lista lähteistä ja lainauksista. , ja painikkeilla voi lisätä, muokata ja poistaa tähän nimeen liittyvän lainauksen. Huomaa että ja painikkeet ovat käytettävissä vasta kun listasta on valittu lainaus.

Lisätietoa: [Lainausmuokkain](wiki:Fi:Gramps_6.0_Wiki-käyttöohje_-_Tietojen_syöttäminen_ja_muokkaaminen:_Tarkemmin_-_osa_2#L.C3.A4hdelainausten_muokkaus)

#### Lisätiedot

lehdellä ovat nimeen liittyvät lisätiedot ja kommentit. Se lisätään ja niitä muokataan lehdllä olevassa tekstinsyöttökentässä.

Katso: [Lisätietomuokkain](wiki:Fi:Gramps_6.0_Wiki-käyttöohje_-_Tietojen_syöttäminen_ja_muokkaaminen:_Tarkemmin_-_osa_2#Lis.C3.A4tietomuokkain)

## Ominaisuudet

Kun lisäät tai muokkaat [Ominaisuuksia](wiki:Attributes_in_Gramps) ikkunan välilehdessä, ikkuna pitää valita. {{-}}

### Ominaisuusmuokkain ikkuna

![[_media/EditPerson-AttributeTab-AttributeEditorWindowFi-41.png|Kuva {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Ominaisuusmuokkain]]

Ikkunan yläosassa on kentät ominaisuuden nimelle ja arvolle. Ikkunan alaosassa on lehtiö, jossa ovat ominaisuuden tarkennuksia varten ja lehdet. painikkeella tietopari tallentuu kantaan ja ikkuna sulkeutuu. painike sulkee ikkunan tallentamatta tietoja.

- (`tunnistenumero` oletus) nimi ja arvo syötetään ao. kenttään. Pudotusvalikon kautta voi valita sukupuuhun jo määritellyn ominaisuuden. Ominaisuuksia käytetään henkilöiden, perheiden, taphtumien ja median yhteydessä. Käyttäjä päättää vapaasti, mitä ominaisuuksia ja niiden arvoja antaa:

- Esimerkkejä: "Pituus" ja "183", "Päivän lämpötila" ja "16", "Hiustenväri" ja "Ruskea), jne. .

<!-- -->

- Ominaisuuden nimen oikealla puolella olevasta kuvakkeesta voi asettaa tämän ominaisuuden yksityiseksi tai julkiseksi. Tämä mahdollistaa ominaisuuden ohittamisen raporteissa, mikäli valitset tämän vaihtoehdon myös raportin asetuksista.

### Ominaisuusmuokkaimen välitehtiä

#### Lähde Lainaukset

  
lehdellä on ominaisuuteen liitettyjä lainauksia ja lähteitä ja painikkeet niiden hallinnointiin. Lehden keskeinen osa on viitelista em. lainauksista ja lähteistä. , ja painikkeilla voi lisätä, muokata ja poistaa näitä viitteitä. Lisäksi on nuolipainikket vitteiden järjestyksen muuttamiseen. Huomaa että ja painikkeet ovat käytettävissä vasta kun listasta on valittu lainaus / viite.

#### Lisätiedot

  
lehdellä ovat ominaisuuteen liittyvät lisätiedot ja kommentit. Ks. tarkemmin esim. [Lisätietomuokkain](wiki:Fi:Gramps_6.0_Wiki-käyttöohje_-_Tietojen_syöttäminen_ja_muokkaaminen:_Tarkemmin_-_osa_2#Lis.C3.A4tietomuokkain)

## Osoitteet

Kun lisäät tai muokkaat osoitetta Ikkunan välilehdessä, ikkuna pitää valita. {{-}}

### Osoitemuokkain ikkuna

![[_media/Edit-person-addresses-tab-address-editor-default-dialogi_fi-42.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Osoitemuokkain - ikkuna]]

Ikkunan yläosassa on muokattavan henkilön osoitetietoja.Tiedot voidaan kirjoittaa tekstikenttiin sopivassa muodossa.

Ikkunan yläosaan kirjoitetaan osoitteissa useimmin tarvittavat tiedot:

- Jonka osoite on voimassa.

  - ![[_media/gramps-date-edit.png]] päivämäärä painikkeella

- Katu osoite.

  - painikkeella osoitekentän oikealla puolella voit määritellä osoitetietueen julkikeksi tai yksityiseksi. Tämä mahdollistaa osoitteen ohittamisen raporteissa, mikäli valitset tämän vaihtoehdon myös raportin asetuksista.

- Osoitteessa oleva taajama.

- Osoitteessa oleva paikkakunta.

- Sähköpostiosoitteessa on jossain tapauksessa sijaintia tarkentava osio (lääni, maakunta tms.).

- Osoitteessa oleva valtio.

- Postinumero.

- Osoitteeseen liitetty puhelin.

Alaosassa on , ja painikkeet. Napsauttamalla painikketta tietot tallentuu tietokantaan ja ikkuna sulkeutuu. Napsauttamalla painiketta ikkuna sulkeutuu tallentamatta tietoja. {{-}}

### Osoitemuokkaimen välilehtiä

Seuraavat välilehdet sisältävät vaihoehdot käytettävissä olevista tiedoista. Voit valita minkä tahansa välilehden sivulle katseltavaksi tai editoida napaauttamalla haluamaasi välilehden otsikkoa.

#### Lähde Lainaukset

välitehti näyttää osoitteeseen liittyviä lähteiden tietoja ja niiden muutoksia. Keskiosa näyttää luettelon kaikista tällaisista lähteistä ja lainauksista jotka on tallennettu tietokantaan. Painikkeilla , , ja voit lisätä, muokata ja poistaa osoitteeseen liittyviä lähde ja lainaus tietoja. Huomaa että ja painikkeet ovat käytettävissä vain, kun lähdeviite on valittu luettelosta.

#### Lisätiedot

lehdellä ovat osoitteeseen liittyvät lisätiedot ja kommentit. Se lisätään ja niitä muokataan lehdellä olevassa tekstinsyöttökentässä.

{{-}}

## Tietueiden sulauttaminen

![[_media/PeopleCategory-Toolbar-MergeTheSelectedPersons-icon-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Valittujen henkilöiden sulauttaminen - Työkalun kuvake korostettuna - esimerkki]]

Joskus tietokannassa voi olla useita tietueita, jotka kuvaavat samaa kohdetta: sama henkilö, sama paikka tai sama lainaus/lähde. Näin voi käydä, jos sama tietoa on erehdyksestä talletettu kahdesti tai jos uusi informaatio osoittaa, että kaksi kohdetta viittaa esim. samaan henkilöön. Muuta taholta saadun GEDCOM-tiedoston tuominen kantaan voi johtaa myös päällekkäisyyksiin.

Johtuipa päällekkäisyys mistä syystä tahansa, sulauttaminen on kätevä keino korjata tilanne.

### Sulauta henkilöt

Henkilöitä sulautetaan Muokkaa-valikosta.

![[_media/Edit-MergePeople-DefaultWindowFi-41.png|Kuva {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Sulauta henkilöt (perus)]] ![[_media/Edit-MergePeople-ExpandedWindowFi-41.png|Kuva {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Sulauta henkilöt (tapahtumat ja perhe)]]

  
Kahden henkilön valinnan jälkeen valitse **Muokkaa-\>Sulauta...** , jolloin käynnistyy dialogi.

Dialogissa voi tehdä päätöksen, sulautetaanko valitut henkilöt vai ei. Päätöksen tueksi voi avata laajennetun osion, jossa ovat henkilön ensisijainen nimi, sukupuoli ja ID, ja tapahtumat/perhe osion.

Jos päätät olla sulauttamatta, vaikka nimet ovat samat, napsauta painiketta sulkeaksesi dialogin ilman muutoksia kannassa.

Jos päätät jatkaa sulauttamista, valitse tarvittaessa laajennetussa valinnassa radiopainikkeilla kummasta tietueesta:

- Nimi
- Sukupuoli
- Gramps ID

tiedot tulevat mukaan sulautettuun tietueeseen, ja napsauta joka tapauksessa painiketta.

![[_media/MergePeople-dialog-sections-expanded-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Sulauta henkilöt - "Laajennettu valinta" &amp; "Tapahtuma ja perhe" osiot avattuna - ikkuna- esimerkki]]

### Sulauta perheet

![[_media/Edit-MergeFamily-DefaultWindowFi-41.png|Kuva {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Sulauta perheet(perus)]] ![[_media/Edit-MergeFamily-ExpandedWindowFi-41.png|Kuva {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Sulauta perheet (laajennettu)]]

  
Kahden perheen valinnan jälkeen valitse **Muokkaa-\>Sulauta...** , jolloin käynnistyy dialogi.

Dialogissa voi tehdä päätöksen, sulautetaanko valitut perheet vai ei. Päätöksen tueksi voi avata laajennetun osion, jossa ovat perheiden isät, äidit, heidän suhteensa ja tunnukset.

Jos päätät olla sulauttamatta perheitä, napsauta painiketta sulkeaksesi dialogin ilman muutoksia kannassa.

Jos päätät jatkaa sulauttamista, valitse tarvittaessa laajennetussa valinnassa radiopainikkeilla kummasta tietueesta:

- Isä
- Äiti
- Edellisten suhde
- Gramps ID

tiedot tulevat mukaan sulautettuun tietueeseen, ja napsauta joka tapauksessa painiketta.

Molempien perheiden lapset tulevat sulautettuun perheeseen mukaan. Isät yhdistetään ja toissijaisen isän tapahtumat liitetään ensisijaiseen isään. Toissijaisen isän nimet liitetään ensisijaiseen isään vaihtoehtoisiksi nimiksi. Kahden äidin kanssa menetellään kuin isien kohdallakin. Toissijaisen perheen tapahtat (kuten avioituminen ja eroaminen) liitetään ensisijaiseen perheeseen. Toissijainen perhetietue ja tämän perheen isän ja äidin tietueet poistetaan kannasta.

Sulautettuun perheeseen tulevat mukaan myös alkuperäisiin perheisiin kuuluvat tapahtumat, lähdelainaukset, ominaisuudet, lisätiedot, mediat, MAP:t ja tagit.

### Sulauta tapahtumat

![[_media/Edit-MergeEvent-DefaultWindowFi-41.png|Kuva {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Sulauta tapahtumat (perus)]] ![[_media/Edit-MergeEvent-ExpandedWindowFi-41.png|Kuva {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Sulauta tapahtumat (laajennettu)]]

  
Kahden tapahtuman valinnan jälkeen valitse **Muokkaa-\>Sulauta...** , jolloin käynnistyy dialogi.

Dialogissa voi tehdä päätöksen, sulautetaanko valitut tapahtumat vai ei. Päätöksen tueksi voi avata laajennetun osion, jossa ovat tapahtumia tarkentavaa tietoa.

Jos päätät olla sulauttamatta tapahtumia, napsauta painiketta sulkeaksesi dialogin ilman muutoksia kannassa.

Jos päätät jatkaa sulauttamista, valitse tarvittaessa laajennetussa valinnassa radiopainikkeilla kummasta tietueesta:

- Tyyppi
- Päivämäärä
- Paikka
- Kuvaus
- Gramps ID

tiedot tulevat mukaan sulautettuun tietueeseen, ja napsauta joka tapauksessa painiketta.

Molempien tapahtumien ominaisuudet, lisätiedot, mediat ja viitteet tulevat sulautettuun tapahtumaan mukaan. Toissijainen tapahtumatietue poistetaan kannasta.

{{-}}

### Sulauta lähteet

![[_media/Edit-MergeSources-DefaultWindowFi-41.png|Kuva {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Sulauta lähteet (perus)]]

![[_media/Edit-MergeSources-ExpandedWindowFi-41.png|Kuva {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Sulauta lähteet (laajennettu valinta)]]

Kahden lähteen valinnan jälkeen valitse , jolloin käynnistyy dialogi.

Dialogissa voi tehdä päätöksen, sulautetaanko valitut lähteet vai ei.

Jos päätät olla sulauttamatta, vaikka nimikkeet ovat samat, napsauta painiketta sulkeaksesi dialogin ilman muutoksia kannassa.

Jos päätät jatkaa sulauttamista, valitse radiopainikkeilla kummasta tietueesta:

- Nimike
- Tekijä
- Lyhennelmä
- Julkaisu
- Gramps ID

tiedot tulevat mukaan sulautettuun tietueeseen, ja napsauta painiketta.

Molempien lähteiden mediat, ominaisuudet, lisätiedot, arkistot ja viitteet tulevat sulautettuun lähteeseen mukaan. Toissijainen lähdetietue poistetaan kannasta.

{{-}}

### Sulauta lainaukset

![[_media/Merge-citations-default-dialogi_fi-42.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Sulauta lainaukset (perus)]]

Kahden lainauksen valinnan jälkeen valitse , jolloin käynnistyy dialogi.

Dialogissa voi tehdä päätöksen, sulautetaanko valitut lainaukset vai ei.

Jos päätät olla sulauttamatta, vaikka nimikkeet ovat samat, napsauta painiketta sulkeaksesi dialogin ilman muutoksia kannassa.

Jos päätät jatkaa sulauttamista, valitse radiopainikkeilla kummasta tietueesta:

- Osa/Sivu
- Päivämäärä
- Luotettavuus
- Gramps ID

tiedot tulevat mukaan sulautettuun tietueeseen, ja napsauta painiketta.

Katso myös [Sulauta lainaukset...](wiki:Gramps_6.0_Wiki_Manual_-_Tools#Merge_citations...) työkalu (Englanniksi). {{-}} ![[_media/Merge-citations-expanded-dialogi_fi-42.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Sulauta lainaukset (laajennettu valinta)]] {{-}}

### Sulauta paikat

![[_media/Edit-MergePlaces-DefaultWindowFi-41.png|Kuva {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Sulauta paikat (perus)]]

![[_media/Edit-MergePlaces-ExpandedWindowFi-41.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Sulauta paikat (laajennettu valinta)]]

Kahden paikan valinnan jälkeen valitse **Muokkaa-\>Sulauta...** , jolloin käynnistyy dialogi.

Dialogissa voi tehdä päätöksen, sulautetaanko valitut paikat vai ei.

Jos päätät olla sulauttamatta, vaikka nimikkeet ovat samat, napsauta painiketta sulkeaksesi dialogin ilman muutoksia kannassa.

Jos päätät jatkaa sulauttamista, valitse radiopainikkeilla kummasta tietueesta:

- Nimike
- Paikannimi
- Tyyppi
- Koodi
- Leveysaste
- Pituusaste
- Sijainti
- Gramps ID

tiedot tulevat mukaan sulautettuun tietueeseen, ja napsauta painiketta.

Molempien paikkojen lähdelainaukset, lisätiedot, mediat, internet ja viitteet tulevat sulautettuun paikkaan mukaan. Toissijaisen paikan sijaintitiedot tulevat myös mukaan,mutta vaihtoehtoisina sijainteina. Toissijainen paikkatietue poistetaan kannasta.

{{-}}

### Sulauta mediat

![[_media/Edit-MergeMedia-DefaultWindowFi-41.png|Kuva {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Sulauta mediat(perus)]] ![[_media/Edit-MergeMedia-ExpandedWindowFi-41.png|Kuva {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Sulauta mediat(laajennettu)]]

  
Kahden median valinnan jälkeen valitse **Muokkaa-\>Sulauta...** , jolloin käynnistyy dialogi.

Dialogissa voi tehdä päätöksen, sulautetaanko valitut mediat vai ei. Päätöksen tueksi voi avata laajennetun osion, jossa ovat medioista lisää tietoja.

Jos päätät olla sulauttamatta medioita, napsauta painiketta sulkeaksesi dialogin ilman muutoksia kannassa.

Jos päätät jatkaa sulauttamista, valitse tarvittaessa laajennetussa valinnassa radiopainikkeilla kummasta tietueesta:

- Nimike
- Polku
- Päivämäärä
- Gramps ID

tiedot tulevat mukaan sulautettuun tietueeseen, ja napsauta joka tapauksessa painiketta.

Molempien medioitten ominaisuudet, lähteet ja tagit tulevat sulautettuun mediaan mukaan. Toissijainen media poistetaan kannasta.

{{-}}

### Sulauta arkistot

![[_media/Edit-MergeRepository-DefaultWindowFi-41.png|Kuva {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Sulauta arkistot (perus)]] ![[_media/Edit-MergeRepository-ExpandedWindowFi-41.png|Kuva {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Sulauta arkistot (laajennettu)]]

  
Kahden arkiston valinnan jälkeen valitse **Muokkaa-\>Sulauta...** , jolloin käynnistyy dialogi.

Dialogissa voi tehdä päätöksen, sulautetaanko valitut arkistot vai ei. Päätöksen tueksi voi avata laajennetun osion, jossa ovat arkistoista lisää tietoja.

Jos päätät olla sulauttamatta arkistoja, napsauta painiketta sulkeaksesi dialogin ilman muutoksia kannassa.

Jos päätät jatkaa sulauttamista, valitse tarvittaessa laajennetussa valinnassa radiopainikkeilla kummasta tietueesta:

- Nimi
- Tyyppi
- Gramps ID

tiedot tulevat mukaan sulautettuun tietueeseen, ja napsauta joka tapauksessa painiketta.

Molempien arkistojen osoitteet, nettisoitteet, lisätiedot ja viitteet tulevat sulautettuun arkistoon mukaan. Toissijainen arkistotietue poistetaan kannasta. {{-}}

### Sulauta lisätiedot

![[_media/Edit-MergeNote-DefaultWindowFi-41.png|Kuva {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Sulauta lisätiedot(perus)]] ![[_media/Edit-MergeNote-ExpandedWindowFi-41.png|Kuva {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Sulauta lisätiedot (laajennettu)]]

  
Kahden lisätietojen tietueen valinnan jälkeen valitse **Muokkaa-\>Sulauta...** , jolloin käynnistyy dialogi.

Dialogissa voi tehdä päätöksen, sulautetaanko valitut lisätiedot vai ei. Päätöksen tueksi voi avata laajennetun osion, jossa ovat lisätiedoista lisää tietoja.

Jos päätät olla sulauttamatta lisätietoja, napsauta painiketta sulkeaksesi dialogin ilman muutoksia kannassa.

Jos päätät jatkaa sulauttamista, valitse tarvittaessa laajennetussa valinnassa radiopainikkeilla kummasta tietueesta:

- Teksti
- Tyyppi
- Muotoiltu-määreet
- Grampd ID

tiedot tulevat mukaan sulautettuun tietueeseen, ja napsauta joka tapauksessa painiketta.

Molempien lisätietojen tekstit ja viitteet tulevat sulautettuun lisätietotietueeseen mukaan. Toissijaisten lisätietojen tietue poistetaan kannasta.

{{-}}

[Category:Fi:Dokumentaatio](wiki:Category:Fi:Dokumentaatio)
