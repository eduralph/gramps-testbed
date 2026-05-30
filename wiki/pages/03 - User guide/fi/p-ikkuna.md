---
title: Fi:Gramps 6.0 Wiki-käyttöohje - Pääikkuna
categories:
- Fi:Dokumentaatio
managed: false
source: wiki-scrape
wiki_revid: 122210
wiki_fetched_at: '2026-05-30T18:19:37Z'
lang: fi
---

{{#vardefine:chapter\|2}} {{#vardefine:figure\|0}} \_\_FORCETOC\_\_ Grampsin pääikkunan elementit. Kuvitettu opas Grampsin käyttöliittymään.

## Pääikkuna

Kun avaat tietokannan, joko olemassa olevan tai uuden, avautuu seuraava ikkuna: (Kuva {{#var:chapter}}.{{#expr:{{#var:figure}}+1}}):

![[_media/MainwinannotatedFi-41.png|Kuva {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Grampsin pääikkuna]]

{{-}}

Gramps:in pääikkuna sisältää seuraavat elementit:

### Ikkunan otsikkopalkki

- Otsikkopalkki sijaitsee ylimmäisenä Grampsin pääikkunassa. Otsikkopalkissa näkyy valitun sukupuun nimi, Gramps sovellusnimi ja painikkeet Grampsin minimointiin, maksimointiin ja sulkemiseen. Pääikkunaa voi myös raahata otsikkopalkista.

### Valikkopalkki

- Valikkopalkki: Valikkopalkki (Menubar) sijaitsee ylimmäisenä ikkunassa (heti ikkunan otsikon alapuolella) ja tarjoaa pääsyn kaikkiin Gramps:in toiminnallisuuksiin.
- Valikot riippuvat siitä, mikä Kategoria on aktiivinen
- Valikon napsauttaminen avaa sille alavalikon.

### Työkalupalkki

- Työkalupalkki: Työkalupalkki (Toolbar) sijaitsee heti valikkopalkin alapuolella. Se tarjoaa useimmiten käytetyt Gramps:in toiminnallisuudet.
- Näytetyt työkalut riippuvat siitä, mikä Kategoria on aktiivinen.
- Viemällä hiiren osoittimen työkalun päälle tulee näkyviin teksti työkalun tehtävästä.

Voit myös poistaa työkalupalkin näytöltä valikosta .

### Näkymätila/Navigaattori

- Näkymätila: Näkymätila sijaitsee ikkunan vasemmassa sivussa ja sillä valitaan eri kategoriat. Katso [Näkymätilan kategoriat](wiki:Gramps_6.0_Wiki_Manual_-_Categories#Categories_of_the_Navigator)

Navigaattori voidaan piilottaa tai saada esille valikossa tai [pikanäppäimet](wiki:Fi:Gramps_6.0_Wiki_Manual_-_Keybindings#7) .

### Näyttöalue

- Näyttöalue: Suurin osa ikkunasta on näyttöaluetta (Display area). Mitä se näyttää, riippuu valitusta näkymästä. Näkymät käydään läpi seuraavaksi.

### Alapalkki, Sivupalkki ja Hakupalkki

- Alapalkki: Alapalkki sijaitsee näyttöalueen alapuolella.

<!-- -->

- Sivupalkki: Sivupalkki sijaitsee oikealla näyttöalueesta.

Molemmat palkit sallivat [grampletien](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets) ja [suotimien](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window#Filters) näyttämisen näkymän yhteydessä.

Molemmat palkit voidaan erikseen piilottaa ja saada näkyville valikosta. Sivupalkin ollessa piilotettuna näytetään sen sijalla .

![[_media/MainwinSearchbarannotatedFi-41.png|Kuva {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Grampsin pääikkunassa näkyvissä hakupalkki]]

### Edistymispalkki ja Tilarivi

- Edistymispalkki: Edistymispalkki (Progress Bar) sijaitsee ikkunan vasemmassa alakulmassa. Se näyttää edistymisen aikaavievissä tapahtumissa, kuten suuren tietokannan avaaminen ja tallettaminen, tuonti ja vienti toisiin tiedostomuotoihin, nettisivujen luonti jne. Kun et ole tekemässä tämän tyyppisiä tapahtumia, edistymispalkkia ei näytetä.
- Tilarivi: Tilarivi (Status Bar) sijaitsee oikealle edistymispalkista. Se näyttää tietoja nykyisestä toiminnasta ja valittuun kohteeseen liittyvää tietoa.

{{-}}

  

## Näkymätilan vaihtaminen

![[_media/Viewing_mode_selectionFi-41.png|Kuva {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Näkymätilan valinta pudotusvalikosta]] Jos Grampsiin on asennettu usea näyttötila, tila on valittavissa pudotusvalikosta.

- **"Kategoria"**(Oletus)
- Pudotusvalikosta
- Laajennettu

{{-}} Näkymätilat ovat "Kategoria", "Pudotusvalikosta" ja"Laajennettu " {{-}} ![[_media/KategoriaFi-41.png|Kuva {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Kategoria näyttötila]]

![[_media/Drop-DownFi-41.png|Kuva {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Pudotusvalikko näyttötila]]

![[_media/ExpanderFi-41.png|Kuva {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Laajennettu näyttötila]] {{-}}

{{-}}

## Kategorioiden vaihtaminen

Grampsissa on vakiona joukko erilaisia kategorioita. Ne on kuvattu käyttöohjeessa [Kategoriat](wiki:Fi:Gramps_6.0_Wiki-k%C3%A4ytt%C3%B6ohje_-_Kategoriat). Voit ladata Gramps näkymiä (ks. [lisäosien hallinta](wiki:Fi:Gramps_6.0_Wiki_k%C3%A4ytt%C3%B6ohje_-_Lis%C3%A4osien_hallinta)) Ohjeet-valinnan kautta. Jos näkymä on uusi tai nykyisen kategorian päivitetty, näkymä lisätään kategoriaan. Kuitenkin, jos näkymä liittyy kokonaan *uuteen* kategoriaan, silloin uusi kategoria lisätään navigaattoriin.

Näkymätilasta riippuu se, miten muutat parhaillaan käytettävää kategoriaa. Normaalisti (pätee useimpiin näyttötiloihin) voit valita haluamasi kategorian napsauttamalla kategorian kuvaketta.

Vaihtoehtoisesti voit käyttää näppäin pikavalikkoja ja siirtymiseksi edelliseen tai seuraavaan kategoriaan. Jos olet kytkenyt [näkymätilan](wiki:Fi:Gramps_6.0_Wiki-käyttöohje_-_Pääikkuna#N.C3.A4kym.C3.A4tila) pois käytöstä, tänä on ainoa keino vaihtaa kategoriaa (jollet ota sitä taas käyttöön).

{{-}}

## Näkymien vaihtaminen

Kategoriassa voi olla erilaisia tapoja tietojen näyttämiseksi, niitä kutsutaan näkymiksi (views). Jos näkymiä on useita, näkymää voi vaihtaa. Vaihtotapa riippuu näkymätilasta. Joissakin tiloissa on kuvakepainike työkalupalkissa näkymän vaihtamiseen. Vaihdon voi tehdä myös valikosta, tai näppäilemällä , missä <numero> on näkymä, johon siirryt tässä kategoriassa.

{{-}}

## Suotimet

![[_media/SidebarFilterFi-41.png|Kuva {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Suotimet näytettynä henkilölistan vieressä]]

Sukutietokannoissa voi olla tietoja monista henkilöistä, perheistä, paikoista ja muista kohteista. Näkymässä voi siten olla pitkä lista tietoja, jolloin työskentely niiden kanssa on vaikeaa. Gramps antaa kaksi eri keinoa tämä tilanteen hallitsemiseen suodattamalla listaa hallittavamman kokoiseksi.

Nämä keinot ovat **Etsi** and **Suodata**.

Etsi hakee listassa näytettyä tekstiä, kun taasen suotimet näyttävät ne henkilöt, joiden tiedot ovat suotimen ehtojen mukaiset.

Etsi on yksinkertainen ja tehokas keino suorittaa haku näytössä olevista sarakkeista. Kun [sivupalkkia](wiki:Fi:Gramps_6.0_Wiki-käyttöohje_-_Pääikkuna#Alapalkki_ja_Sivupalkki) **ei** ole näkyvillä, on näkyvillä. Näppäilemällä merkkejä and napsauttamalla painiketta näytetään vain ne rivit, jotka vastaavat tekstiä.

Vaihtoehtoisesti, voit ottaa suotimen [alapalkissa tai sivupalkissa](wiki:Fi:Gramps_6.0_Wiki-käyttöohje_-_Pääikkuna#Alapalkki_ja_Sivupalkki). Kun suotimien sivupalkki on näkyvillä, ei näytetä. Suodattimella voit vuorovaikuttaisesti rakentaa joukon suodinsääntöjä, joita käytetään näyttämiseen. Suodatin kohdistuu tietokantaan, ei siihen mitä on näytössä näkyvissä. Käsiteltävän kategorian suotimia voi rakentaa myös napsauttamalla vastaavaa "muokkain" painiketta valikossa.

Lisätietoja suotimien toiminnasta engl. [täältä](wiki:Gramps_6.0_Wiki_Manual_-_Filters)

{{-}}

Kun Gramps avaa tietokannan, mitään suodatusta ei ole päällä. Esim. Henkilöt-näkymässä listataan oletusarvoisesti kaikki tietokannan henkilöt.

{{-}}

[Category:Fi:Dokumentaatio](wiki:Category:Fi:Dokumentaatio)
