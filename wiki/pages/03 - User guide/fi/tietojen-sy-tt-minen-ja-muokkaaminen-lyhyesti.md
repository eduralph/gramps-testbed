---
title: 'Fi:Gramps 6.0 Wiki-käyttöohje - Tietojen syöttäminen ja muokkaaminen: Lyhyesti'
categories:
- Fi:Dokumentaatio
managed: false
source: wiki-scrape
wiki_revid: 120646
wiki_fetched_at: '2026-05-30T18:29:42Z'
lang: fi
---

{{#vardefine:chapter\|8}} {{#vardefine:figure\|0}}

Tämä luku antaa sinulle välttämättömimmät perustiedot sukututkimustietojesi syöttämisestä Grampsiin. Siinä esitellään miten syötät henkilön tietokantaan ja miten määrittelet perhesuhteet. (Tarkempi selitys löytyy seuraavasta [luvusta](wiki:Fi:Gramps_6.0_Wiki-käyttöohje_-_Tietojen_syöttäminen_ja_muokkaaminen:_Tarkemmin).)

Tunnistakaamme aluksi tietojen tyypit, joita voidaan syöttää Gramps tietokantaan. Näitä ovat:

- Henkilöiden yksilölliset tiedot (nimet, osoitteet, syntymä- ja kuolinpäivät, jne.)

<!-- -->

- Tiedot henkilöiden suhteista (avioliitot, avioerot, rekisteröidyt parisuhteet, jne.)

<!-- -->

- Tiedot henkilöiden vanhemmista ja lapsista

<!-- -->

- Tutkimuksen lähdeaineisto

Nyt katsomme lyhyesti, miten voit syöttää ja muokata näitä tietoja.

## Henkilön lisääminen ja muokkaaminen

![[_media/People-tree-view-grouped-people_fi-42.png|Kuva. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Henkilöt kategoria - Puunäkymä - Ryhmitetyt henkilöt]]

![[_media/Edit-person-person-window_fi-42.png|Kuva. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Muokkaa henkilöä - ikkuna]]

{{-}}

On olemassa monta tapaa lisätä henkilö tietokantaan. Mainitsemme niistä joitakin, kun menemme eteenpäin. Yksinkertaisin tapa on lisätä henkilö Henkilöt näkymässä. Kun olet Henkilöt näkymässä (katso [kuva](wiki:Media:People-tree-view-grouped-people_fi-42.png)), napsauta painiketta työkalurivillä. Syötä kaikki tietämäsi tieto henkilöstä ikkunassa (katso [kuva](wiki:Media:Edit-person-person-window_fi-42.png)).

Muokataksesi tietokannassa olevan henkilön tietoja, valitse henkilö Henkilöt näkymässä ja napsauta painiketta työkaluriviltä.

Henkilö voidaan myös lisätä tietokantaan Suhteet näkymässä, ikkunassa ja muissa paikoissa missä se on mahdollista.

## Suhteen määrittely

Henkilöiden välille voidaan määritellä suhteita kahdella tavalla - käyttämällä Suhteet näkymää tai käyttämällä ikkunaa Perheet näkymästä. Perheet näkymää käytetään tavallisesti luotaessa suhde kerrallaan yhden perheen sisällä. Suhteet näkymää käytetään tavallisesti luotaessa monta suhdetta yhdelle henkilölle.

### Suhteet-näkymässä

![[_media/Relationships-category-view_fi-42.png|Kuva. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Suhteet näkymä]]

Suhteiden lisäämiseksi aktiiviselle henkilölle siirrytään hänen näkymäänsä. Siinä aktiivinen henkilö on ylimpänä. Työkalupalkissa on kolme kuvaketta, joista hänelle voi lisätä suhteita

- Lisää henkilölle uudet vanhemmat
- Lisää henkilö sukupuussa jo olevan perheen lapseksi
- Lisää perhe jossa henkilö on vanhempana

Kun henkilölle on lisätty vanhemmat tai oma perhe, niitä ja kaikkia suhteissa näkyviä henkilöitä voidaan lisätä, muokata ja poistaa niiden vieressä olevista painikkeista.

Henkilöä napsauttamalla hänestä tulee aktiivinen henkilö ja suhteet näytetään hänen kannaltaan.

{{-}}

![[_media/Family-editor-dialog-example-family_fi-42.png|Kuva. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Muokkaa perhettä - ikkuna]]

Muokkaa perhettä ikkunassa aktiivinen henkilö voi olla isänä tai äitinä.

{{-}}

![[_media/SelectPerson-dialog_fi-41.png|Kuva. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Valitse henkilö - ikkuna]]

Kysymys ?: Löytyykö aktiiviseen henkilöön suhteella lisättävä henkilö jo tietokannasta? Jos näin on, henkilöä lisätään painikkeella. Gramps generoi henkilölistan, josta voit valita haluamasi liitettävän henkilön. Jollei löydy, liitettävä henkilä lisätään painikkeella.

Suhteen muokkaamiseksi näkymässä napsautetaan painiketta halutun perheen kohdalla. Jos näkymässä on useita suhteita, voit valita haluamasi puolison tai partnerin napsauttamalla painiketta ao. suhteen kohdalla.

{{-}}

### Perheet listanäkymässä

Avaa lista, napsauta painiketta työkaluista. Tyhjä ikkuna avautuu. Voit lisätä ikkunassa perheeseen henkilöitä.

Muokkaa perhettä-ikkuna avautuu Perheet listasta, Suhteet näkymän sekä painikkeista.

{{-}}

## Vanhempien määrittely

![[_media/sSelectFamily-dialog_fi-42.png|Kuva {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Valitse perhe - ikkuna]]

Voit määritellä aktiiviselle henkilölle vanhemmat näkymässä ([suhteet-kuva](wiki:Media:Relationships-category-view_fi-42.png)). Pieni varovaisuus on paikallaan ehkäisemään saman perheen luonnin kahteen kertaan. Jos haluat lisätä aktiivisen henkilön olemassa olevaan perheeseen, napsauta ![[_media/gramps-parents-open.png]] painiketta. Jos perhettä ei ole vielä luotu, napsauta ![[_media/gramps-parents-add.png]] painiketta.

Jos napsautat ![[_media/gramps-parents-open.png]] painikketta, näytetään ikkuna. Ikkunasta voit valita olemassa olevan perheen ja aktiivinen henkilö lisätään perheen lapseksi.

Jos napsautat ![[_media/gramps-parents-add.png]] painikkeen, uusi ikkunassa näytetään aktiivinen henkilö uuden perheen lapsena. Voit lisätä vanhemmat, joko valitsemalla olemassa olevan perheen henkilön vanhemmiksi tai lisäämällä henkille uudet vanhemmat.

![[_media/Family-warn_fi-42.png|Kuva {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Perhe kahteen kertaan]]

Voit myös määritellä henkilön vanhemmat Perheet näkymässä. Jos perhe on jo olemassa, napsauttamalla painiketta työkalurivillä ja lisäämällä henkilön lapseksi ikkunassa. Jos perhettä ei ole vielä olemassa, napsauta painiketta luodaksesi uuden perheen ja lisää oikeat vanhemmat ja lapset.

## Lapsen määrittely

![[_media/Child-ref_fi-42.png|Kuva {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Lapsiviite muokkain - ikkuna]]

Lapsen suhteen lisääminen on samanlainen toimenpide. Valitse ja näkymissä olemassa oleva perhe tai luo uusi perhe. Lapsi voidaan lisätä valitsemalla lapsi välilehden työkaluriviltä tai painikkeella.

Napsauttaminen painiketta näyttää ennen lapsiviite ikkunaa ikkunan, jossa voit lisätä uuden henkilön. Napsauttaminen painikkeesta mahdollistaa olemassa olevan henkilön valinnan listalta. Oletuksena lapsella on valittu syntymäsuhde molempiin vanhempiin.

Jos haluat vaihtaa vanhempien ja lapsen välistä suhdetta oletuksena olevasta syntymäsuhteesta, valitse lapsi ja napsauta painiketta. Tämä näyttää ikkunan.

Jos haluat vaihtaa perheen lasten järjestystä, käytä nuolinäppäimiä tai raahaamista (ks. [*drag and drop*](http://en.wikipedia.org/wiki/Drag_and_drop)).

{{-}}

## Kuvien ja muiden media tiedostojen lisääminen

Voit lisätä valokuvia ja muita media tiedostoja yksittäiselle henkilölle, tapahtumille, lähteille ja paikoille. Voit myös lisätä kuvan joka ei rajoitu yhteen henkilöön tai tapahtumaan (esimerkiksi perhekuvat).

Jos haluat lisätä kuvan henkilölle, vaihda näkymään ([Pääikkuna](wiki:Media:Mainwin_Fi-42.png)), valitse henkilö ja napsauta painiketa työkaluriviltä. Tämä avaa ikkunan ([Muokkaa henkilöä](wiki:Media:Edit-person-person-window_fi-42.png)). Seuraavaksi valitse välilehti ja napsauta painiketta avataksesi ikkuna. Kirjoita tiedostonimi tai selaa löytääksesi haluamasi kuvatiedoston ja syötä otsikko kuvalle.

Lisätäksesi tapahtumaan liittyvän kuvan (esimerkiksi avioliitto), vaihda Perheet näkymään ([Perheet näkymä](wiki:Media:Family_ListFi-41.png)) ja kaksoisnapsauta puolison nimeä. Tämä avaa ikkunan. Valitse välilehti ja napsauta painiketta ja lisää kuva.

Lisätäksesi lähteesen tai paikkaan liittyvän kuvan, vaihda näkymään tai näkymään. Valitse haluamasi lähde tai paikka ja kaksoisnapsauta sitä tai napsauta kuvaketta työkalurivillä. Valitse välilehti ja napsauta painiketta ja lisää kuva.

Lopuksi, lisätäksesi kuvan jonka haluat kuuluvan tietokantaan, mutta ei ole rajattu yhteenkään erityiseen henkilöön, suhteeseen, lähteeseen tai paikkaan, vaihda näkymään. Sitten napsauta kuvaketta työkaluriviltä lisätäksesi kuvan. Jos olet jo lisännyt kuvia yhteenkään yksittäiseen galleriaan, löydät ne myös listattuna Media näkymästä.

Missä tahansa galleriassa, voit myös käyttää painiketta muokataksesi kuvan tietoja ja painiketta poistaaksesi kuvaviittauksen kyseisestä galleriasta.

## Tapahtumien, lähteiden, paikkojen ja arkistojen muokkaaminen

Lisätäksesi tapahtuman, lähteen, paikan, tai arkiston tietokantaan, vaihda näkymään ( [Tapahtumat näkymä](wiki:Media:EventsCategoryViewFi-41.png)), näkymään, näkymään ([Lähteet näkymä](wiki:Media:SourcesFi-41.png)), näkymään ([Paikat näkymä](wiki:Media:PlacesCategoryViewFi-41.png)) tai näkymään ([Arkistot näkymä](wiki:Media:RepositoriesCategoryViewFi-41.png)). Sitten napsauta kuvaketta työkaluriviltä lisätäksesi vastaavan tiedon. Syötä tiedot ( , tai ) ikkunassa.

Muokataksesi jo tietokannassa olevan tapahtuman, lähteen, paikan tai arkiston tietoja, vaihda oikeaan näkymään, valitse kohde jota haluat katsoa/muokata ja sitten napsauta painiketta työkaluriviltä. Vaihtoehtoisesti voit kaksoisnapsauttaa kohdetta muokataksesi sitä.

![[_media/EventsCategoryViewFi-41.png|Kuva. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Tapahtumat - näkymä]] ![[_media/PlacesCategoryViewFi-41.png|Kuva. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Paikat - näkymä]] ![[_media/RepositoriesCategoryViewFi-41.png|Kuva. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Arkisto - näkymä]]

{{-}}

[Category:Fi:Dokumentaatio](wiki:Category:Fi:Dokumentaatio)
