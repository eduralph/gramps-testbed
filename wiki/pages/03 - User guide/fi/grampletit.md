---
title: Fi:Gramps 6.0 Wiki-käyttöohje - Grampletit
categories:
- Fi:Dokumentaatio
- Stub
managed: false
source: wiki-scrape
wiki_revid: 128698
wiki_fetched_at: '2026-05-30T18:16:08Z'
lang: fi
---

{{#vardefine:chapter\|10}} {{#vardefine:figure\|0}}

Tällä sivulla käydään läpi grampletien toiminnallisuus. Katso [Gramplets_development](wiki:Gramplets_development), jos haluat lukea teknisiä yksityiskohtia oman grampletin ohjelmoimiseksi. Katso [Third-party Addons](wiki:Third-party_Addons), josta löydät lisää grampletejä laajentamaan Grampsin toiminnallisuutta.

# Mikä on Gramplet

![[_media/GrampletsDefaultFi-41.png|Kuva {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Työpöytä (Default View)]]

Gramps Gramplet on näkymä tietoihin. Sen näyttämät tiedot muuttuvat ajantasalla tai se tarjoaa vuorovaikutteisuuden sukututkimustietoihisi. Grampletit ovat "widgetejä" (sovelmia), ks. (engl.) [widgets](http://en.wikipedia.org/wiki/Widget_engine) ja ne on nähtävissä Grampsissa kolmea kautta: Työpöydällä, Gramps käyttöliittymän Sivupalkissa ja muiden kategorioiden Alapalkissa. Grampletit tarjoavat monenlaista toiminnallisuutta, josta on hyötyä tutkijalle.

Mikä sitten erottaa grampletit, raportit, pikanäkymät ja työkalut?

- Raportit tarjoavat staattisen tulosteen tiedoistasi, käytettäväksi tyypillisesti esityksissä
- Pikanäkymä tarjoaa tyypillisesti lyhyen, interaktiivisen listauksen tiedoistasi
- Työkalut antavat tietojesi käsittelyyn menettelyn
- Grampletit tarjoavat ajantasaisen näkymän ja rajapinnan tietoihisi

{{-}} Kun käynnistät Grampsin, se avautuu Työpöytä-kategoriaan. Näet kaksi oletusgramplettia: Tervetuloa Grampsiin ja "Yleisimmät sukunimet".

Grampsin versiosta 6.0 meillä on yleis- ja erityisgramplettaja, riippuen mikä kategoria on aktiivisena.

- Viitteet Grampletit ovat samankaltaisia kuin Muokkain ikkunoiden Viitteet lehdet.
- Suodin Grampletit ovat samanlaisia kuin aikaisempi Sivupalkki
- Lisätietojen, Gallerian, Lähteiden, Lainausten ja Tapahtumien omat grampletit
- Henkilö näkymien (myös esivanempian ja suhteiden omat grampletit ja perhenäkymä

## Yleinen käyttö ja konfigurointi

![[_media/GrampletDetachedFi-41.png|Kuva {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Omassa ikkunassaan oleva gramplet]]

Työpöydällä kunkin Grampletin yläpalkissa on kolme painiketta ja Grampletin nimi. Vasemmanpuoleisesta painikkeesta voi raahata Grampletin toiseen paikkaan työpöydällä. Samasta painikkeesta napsauttamalla Gramplet irtoaa työpödältä omaksi ikkunakseen. Ikkuna pysyy auki riippumatta muusta navigoinnista. Ikkunan sulkeminen palauttaa grampletin työpöydälle. Jos gramplet on auki ja suljet Grampsin, käynnistettäessä Gramps uudelleen myös gramplet avautuu automaattisesti .

Kun grampleteja on avattuna omiin ikkunoihinsa, voit vaihtaa Grampsin listanäkymiä ja grampletit tarjoavat lisätietoja ja -toiminnallisuutta listanäkymien kohteille (riveille).

Työpöydällä voit lisätä uusia grampleteja napsauttamalla hiiren oikealla Työpöydän vapaata (harmaata) pohjaa , jolloin avautuu valittavissa olevien grampletien lista. Gramplet avautuu työpöydälle. Henkilö-ja muiden kategorioiden listanäkymien alapalkkiin voi vastaavasti lisätä grampleteja alapalkin oikeassa reunassa olevasta pudotusvalikosta. Valittu gramplet avautuu alapalkin lehdeksi. Samoin sivupalkissa, hakuosion yläpuolelta löytyy pudotusvalikko grampleteille.

Työpöydän ollessa auki työkalupalkin *Muokkaa valitun näkymän asetuksia* painikkeesta voit asettaa työpöydällä oleville grampleteille näytettävän sarakkeiden lukumäärän sekä gramplet-kohtaisesti korkeus- ja leveyskohtaisia asetuksia sekä mahdollisesti muitakin asetuksia. Jos grampletissa on linkki tiettyyn henkilöön, linkin napsauttaminen vaihta aktiivisen henkilön. Henkilön kaksoisnapsauttaminen avaa lisäksi henkilömuokkaimen ja perheen linkissä perhemuokkaimen. Hiiren oikealla napsautaminen avaa henkilömuokkaimen, mutta ei vaihda aktiivista henkilöä. Pikanäkymässä rivin napsauttaminen kahdesti näyttää tarkempia tietoja (drill down) tai avaa muokkaimen, riippuen näkymän kohteesta.

Grampletin otsikkonimen voi vaihtaa työpöydällä sijaitsevassa tai itsenäiseen ikkunaan avatussa grampletissä.

Lisäksi voit helposti ladata ja käyttää kolmansien tahojen tekemiä grampletteja. Näitä ovat mm.:

- Headline News Gramplet - tuoreet tärkeät Grampsin uutiset
- Data Entry Gramplet - näyttää aktiivisesta henkilöstä nimen, syntymäajan ja -paikan, kuolinajan sekä -paikan ja sallii lisätä henkilöitä
- Python Gramplet - Python shell
- FAQ Gramplet - UKK
- Note Gramplet - näyttää henkilön ensimmäisen Lisätiedot ja sallii sellaisen kirjoittamisen

ja monia muita. Katso [Third-party Addons](wiki:Third-party_Addons) lisätietojen vuoksi.

## Yhteenveto grampleteistä

Yhteenveto kaikista ydingrampleteista ja ja missä kategorioissa ne on käytettävissä.

Kategorista riippuu, onko grampletit lisättävissä tai poistettavissa

- Työpöytä kategoriassa hiiren oikealla avautuvasta valikosta.
- Muissa kategorioissa alapalkissa tai sivupalkissa löytyvästä pudotusvalikosta.

{{-}}

| Gramplet | Työpöytä kategoria | Henkilöt kategoria | Suhteet kategoria | Perheet kategoria | Kaaviot kategoria | Tapahtumat kategoria | Paikat kategoria | Kartat kategoria | Lähteet kategoria | Lainaukset kategoria | Arkistot kategoria | Media kategoria | Lisätiedot kategoria |
|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
| id="1" \| | X | X | X | X | X | X | X | X | X | X | X | X | X |
| id="2" \| | X | X | X | X | X | X | X | X | X | X | X | X | X |
| id="3" \| |  | X | X |  | X |  |  | X |  |  |  |  |  |
| id="4" \| |  | X | X | X | X | X |  | X | X | X |  | X |  |
| id="5" \| | X | X | X | X | X | X | X | X | X | X | X | X | X |
| id="6" \| |  | X | X | X | X |  |  | X |  |  |  |  |  |
| id="7" \| |  | X | X | X | X | X | X | X |  |  |  | X |  |
| id="8" \| |  | X | X |  | X |  |  | X |  |  |  |  |  |
| id="9" \| |  | X | X |  | X |  |  | X |  |  |  |  |  |
| id="10" \| |  | X | X |  | X |  | X | X |  |  | X |  |  |
| id="11" \| |  | X | X | X | X |  |  | X |  |  |  |  |  |
| id="12" \| | X | X | X | X | X | X | X | X | X | X | X | X | X |
| id="13" \| |  | X | X |  | X |  |  | X |  |  |  |  |  |
| id="14" \| |  |  | X |  | X |  |  |  |  |  |  |  |  |
| id="15" \| |  | X | X | X | X | X | X | X | X | X |  |  |  |
| id="16" \| | X | X | X | X | X | X | X | X | X | X | X | X | X |
| id="17" \| |  |  |  |  |  |  |  |  |  |  |  | X |  |
| id="18" \| |  |  |  |  |  |  | X |  |  |  |  |  |  |
| id="19" \| |  | X | X | X | X | X | X | X | X | X | X | X |  |
| id="20" \| |  | X | X |  | X |  |  | X |  |  |  |  |  |
| id="21" \| |  |  |  |  |  |  |  |  |  |  |  | X |  |
| id="22" \| | X | X | X | X | X | X | X | X | X | X | X | X | X |
| id="23" \| | X | X | X | X | X | X | X | X | X | X | X | X | X |
| id="24" \| |  | X | X | X | X | X | X | X | X | X | X | X | X |
| id="25" \| |  | X | X |  | X |  |  | X |  |  |  |  |  |
| id="26" \| |  | X | X |  | X |  |  | X |  |  |  |  |  |
| id="27" \| | X | X | X | X | X | X | X | X | X | X | X | X | X |
| id="28" \| | X | X | X | X | X | X | X | X | X | X | X | X | X |
| id="29" \| | X | X | X | X | X | X | X | X | X | X | X | X | X |
| id="30" \| | X | X | X | X | X | X | X | X | X | X | X | X | X |
| id="31" \| | X | X | X | X | X | X | X | X | X | X | X | X |  |
| id="32" \| | X | X | X | X | X | X | X | X | X | X | X | X | X |
| id="33" \| | X | X | X | X | X | X | X | X | X | X | X | X | X |
| id="34" \| | X | X | X | X | X | X | X | X | X | X | X | X | X |
| id="xx" \| |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |

Lisätietoja asennettujen gramplettien käytöstä, katso [Grampletit](wiki:Fi:Gramps_6.0_Wiki-käyttöohje_-_Grampletit).

{{-}}

# Grampletit

{{-}}

## Ikä määriteltynä päivänä

![[_media/AgeOnDate-detached-grampletFi-41.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Ikä määriteltynä päivänä Gramplet]] ![[_media/AgeOnDate-QV-ResultExample-grampletFi-41.png|Kuva {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Ikä määriteltynä päivänä pikaraportti]]

Voit antaa päivämäärän grampletin syöttökenttään. painikkeesta gramplet laskee jokaiselle sukupuussasi ao. päivänä. Päivämäärä on annettava Grampsin hyväksymässä muodossa.

Ikä-sarakkeella voi lajitella ja rivin kaksoisnapsauttaminen avaa rivin katseluun tai päivitykseen.

{{-}}

## Ikätilastot

![[_media/AgeStats-detached-grampletFi-41.png|Kuva {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Ikätilastot Gramplet]]

Ikätilastot gramplet näyttää henkilöiden ikäjakautuman ikäluokissa. Rivin napsauttaminen tuo esille siihen kuuluvat henkilöt.

Voit vaihtaa grampletin asetuksia valitsemalla työkalupalkista *Muokkaa valitun näkymän asetuksia* painikkeen.

![[_media/ToolbarConfigureTheView-AgeStats-Options-grampletFi-41.png|Kuva {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Ikätilastot Grampletin näkymäasetukset]]

{{-}}

## Esivanhemmat

![[_media/Ancestors-gramplet-42.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Ancestors Gramplet]]

Gramplet näyttää aktiivisen henkilön esivanhemmat. {{-}}

## Ominaisuudet

![[_media/Attributes-detached-grampletFi-41.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Ominaisuudet Gramplet]]

![[_media/AttributesQVFi-41.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Ominaisuuksien pikanäkymä]] {{-}} Ominaisuudet gramplet näyttää aktiivisen henkilön kaikki ominaisuudet. Kaksoisnapsautuksella ominaisuutta näet pikanäkymänä kaikki henkilöt, joilla on sama ominaisuus, ja heidän arvonsa siinä. Pikanäkymän sarakeotsikosta voi lajitella pikalistan sarakeen mukaiseen järjestykseen.

Rivin valitseminen pikanäkymässä vaihtaa aktiivisen henkilön ja hänen tietonsa ilmestyvät ao. muihin grampletteihin. Rivin kaksoisnapsauttaminen avaa henkilön muokkausikkunan.

### Henkilön ominaisuudet

Katso [Attributes](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Attributes) {{-}}

### Perheen ominaisudet

Katso [Attributes](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Attributes) {{-}}

### Tapahtuma ominaisuudet

Katso [Attributes](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Attributes) {{-}}

### Lähteen ominaisuudet

Katso [Attributes](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Attributes) {{-}}

### Lainauksen ominaisuudet

Katso [Attributes](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Attributes) {{-}}

### Median ominaisuudet

Katso [Attributes](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Attributes) {{-}}

## Kalenteri

![[_media/Calendar-detached-grampletFi-41.png|uva {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Kalenteri]]

Kalenteri gramplet näyttää kuukauden kattavan kalenterin. Päivää kaksoisnapsauttamalla saa aikaisesi pikanäkymän.

Kuukauden vasemmassa yläkulmassa olevilla ja painikkeilla voit siirtyä edelliseen ja seuraavaan kuukauteen.

Vuoden oikeassa yläkulmassa olevilla ja painikkeilla voit siirtyä edelliseen ja seuraavaan vuoteen.

Pikanäkymässä on valitun päivän **tapahtumat**: Tapahtumat juuri tänä päivänä ja muut tapahtumat tässä kuussa/tänä päivänä menneisyydessä ja myös muut tapahtumat tänä vuonna.

Tiedot näytetään taulukkona:

- päivämäärä
- tyyppi
- paikka
- viite

Voit myös raahata ja pudottaa päivämäärän [Ikä määriteltynä päivänä Gramplet](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Age_on_Date_Gramplet) sen päivämäärän syöttökenttään.

{{-}}

## Lapset

![[_media/Children-gramplet-42.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Lapset Gramplet]]

Gramplet näyttää henkilön tai perheen lapset, riippuen kumman alapalkkiin gramplet on lisätty. {{-}}

### Henkilön lapset

Katso [Children](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Children) {{-}}

### Perheen lapset

Katso [Children](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Children) {{-}}

## Lainaukset

![[_media/Citations-gramplet-42.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Citations Gramplet]]

Gramplet näyttää kohteeseen liitetyt lähde- ja lainaustiedot {{-}}

### Henkilön lainaukset

See [Citations](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Citations) {{-}}

### Perheen lainaukset

See [Citations](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Citations) {{-}}

### Tapahtuman lainaukset

See [Citations](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Citations) {{-}}

### Paikan lainaukset

See [Citations](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Citations) {{-}}

### Median lainaukset

See [Citations](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Citations) {{-}}

## Jälkeläisviuhka

![[_media/Descendant-fan-gramplet-42.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Descendant Fan (chart) Gramplet]]

Gramplet näyttää aktiivisen henkilön suorat jälkeläiset viuhkakaaviona. {{-}}

## Jälkeläiset

![[_media/Descendant-detached-grampletFi-41.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Jälkeläiset Gramplet]]

Jälkeläiset gramplet näyttää aktiivisen henkilön suorat jälkeläiset.

Puolisoiden ja jälkeläisten järjestys on sukupuun mukainen. Puolisoiden järjestyksen muuttamiseksi käytä Suhteen muokkausikkunassa valintaa "Muuta vanhempien ja perheiden järjestystä". Perheen lasten järjestyksen muuttamiseksi käytä Suhteen muokkausikkunassa valintaa "Muokkaa perhettä" valintaa, jonka jälkeen voit nuolinäppäimillä tai lasta raahaamalla siirtää lasta lapsikatraassa.

Tämä gramplet on toteutettu tekstiraporteista löytyvän Jälkeläisraportin pohjalta.

Jälkeläis grampletin näyttämä päivittyy, kun aktiivista henkilöä ja perhettä muutetaan. Suorituskyvyn vuoksi näyttämä ei muutu automaattisesti lapsia tai puolisoita päivitettäessä.

Grampletin minimointi estää näyttämän päivittämisen.

{{-}}

## Yksityiskohdat

Gramplet näyttää Grampletin kohteista perustietoja.

{{-}}

### Henkilön yksityiskohdat

![[_media/Details-gramplet-42.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Henkilön yksityiskohdat]]

Gramplet näyttää henkilöstä tietoja.

- Henkilön ensisijainen nimi
- Henkilön toisintonimet ja niiden typit
- Isän nimi
- Äidin nimi
- Syntymäaika ja -paikka
- Kasteaika ja -paikka
- Kuolinaika ja -paikka
- Hautausaika ja -paikkaSee
- *Kuva*: Henkilön Galleriassa oleva 1. kuva näytetään pienoiskuvana em. tietojen vasemmalla puolella. Kuvan kaksoinapsautus avaa sen omaan ikkunaansa.

{{-}}

### Paikan yksityiskohdat

Gramplet näyttää paikasta tiedot

- Lisätiedot.

{{-}}

### Suhteiden yksityiskohdat

Gramplet näyttää suhteet-ikkunan keskushenkilön (so. ylimpänä olevan henkilön) yksityiskohdat.

{{-}}

### Kaavioiden yksityiskohdat

Gramplet näyttää Kaaviot-ikkunan aktiivisen henkilön yksityiskohdat. Aktiivinen henkilö kaaviossa on esipolvien taulussa vasemmalla, viuhkakaavioissa keskellä, graafisessa näkymässä valittuna ylärivissä ja aikajanakaaviossa esi- ja jälkeläispolvien keskushenkilö.

{{-}}

### Kartan yksityiskohdat

Gramplet näyttää kartan yksityiskohtina aktiivisen henkilön yksityiskohdat.

{{-}}

### Arkiston yksityiskohdat

Gramplet näyttää arkistosta tiedot

- Osoite
- Internet

{{-}}

## Tapahtumat

![[_media/Events-gramplet-42.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Events Gramplet]]

Gramplet näyttää henkilöiden tapahtumia listana. Listan sarakeotsikot muuttavat lajittelujärjestyksen. {{-}}

### Henkilön tapahtumat

Gramplet näyttää valitun henkilön kaikista tapahumista seuraavat tiedot:

- tyyppi
- kuvaus
- päivämäärä
- henkilön ikä tapahtumahetkellä
- paikka
- pääosalliset
- heidän roolinsa

See [Events](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Events) {{-}}

### Suhteen tapahtumat

Gramplet näyttää suhteet-ikkunan keskushenkilön (so. ylimpänä olevan henkilön) yksityiskohdat. See [Events](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Events) {{-}}

### Perheen tapahtumat

Gramplet näyttää valittuun perheeseen liitetyt tapahtumat. . See [Events](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Events) {{-}}

### Kaavion tapahtumat

Gramplet näyttää Kaaviot-ikkunan aktiivisen henkilön tapahtumat. Aktiivinen henkilö kaaviossa on esipolvien taulussa vasemmalla, viuhkakaavioissa keskellä, graafisessa näkymässä valittuna ylärivissä ja aikajanakaaviossa esi- ja jälkeläispolvien keskushenkilö.. . See [Events](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Events) {{-}}

### Kartan tapahtumat

Gramplet näyttää valittuun henkilöön liitetyt tapahtumat. Perheen kartassa näkyy perheeseen liitetyt tapahtumat. . See [Events](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Events) {{-}}

## Viuhkakaavio

![[_media/FanChart-detached-gramplet-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Viuhkakaavio Gramplet]] Viuhkakaavio Gramplet näyttää aktiivisen henkilön suorat esivanhemmat ympyräkaaviona. Se on samanlainen kuin esipolvien näkymä, mutta aktiivinen henkilö keskellä ja muut sukupolvet ulkokehinä.

Napsauta vanhempaa kaaviossa ja ne laajentuvat tai supistuvat lapsiensa yläpuolella. Napsauta hiiren oikealla ja voit::

- valita tämän henkilön aktiiviseksi henkilöksi
- muokata henkilöä jolloin voit lisätä Henkilömuokkaimen kautta lapsia henkilön perheisiin
- valita henkilön sukulaisia aktiiviseksi henkilöksi
- lisätä kumppaneita (perheitä) henkilölle
- kopioida henkilön nimen, syntymän ja kuoleman leikepöydälle

Kaaviota voi pyörittää tarttumalla kaavion alueeseen, jossa ei ole henkilöit. *Gramps 6.0 :ssä voit tarttua hiiren vasemmalla kaavion keskustaan ja raahata kaavion uuteen paikkaan.*

Musta ulkokehän reuna ooittaa henkilöllä olevan lisää vanhempia. Musta ympyrä keskellä osoittaa henkilöllä olevan lapsia.

Viuhkakaavio päivittyy aktiivisen henkilön ja sukupuun vaihtamisesta.

Grampletin minimointi estää sen päivittymisen. {{-}}

## UKK

![[_media/Faq-gramplet-42.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} UKK Gramplet]]

Gramplet näyttää usein esitettyjä kysymyksiä

{{-}}

## Suodin

Gramplet tarjoaa kategoriakohtaisen suotimen. Katso myös [Which filters in which Category?](wiki:Gramps_6.0_Wiki_Manual_-_Filters#Which_filters_in_which_Category.3F) {{-}}

### Henkilösuodin

![[_media/Filter-person-gramplet-42.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Hekilösuodin- dialogi]]

Katso [Filter](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Filter) {{-}}

### Perhesuodin

![[_media/Filter-family-gramplet-42.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Perhesuodin- dialogi]]

Katso [Filter](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Filter) {{-}}

### Tapahtumasuodin

![[_media/Filter-event-gramplet-42.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Tapahtumasuodin - dialogi]]

Katso [Filter](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Filter) {{-}}

### Paikkasuodin

![[_media/Filter-place-gramplet-42.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Paikkasuodin - dialogi]]

Katso [Filter](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Filter) {{-}}

### Lähdesuodin

![[_media/Filter-source-gramplet-42.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Lähdesuodin - dialogi]]

Katso [Filter](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Filter) {{-}}

### Lainaussuodin

![[_media/Filter-citation-gramplet-42.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Lainaussuodin - dialogi]]

Katso [Filter](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Filter) {{-}}

### Arkistosuodin

![[_media/Filter-repository-gramplet-42.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Arkistosuodin - dialogi]]

Katso [Filter](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Filter) {{-}}

### Mediasuodin

![[_media/Filter-media-gramplet-42.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Mediasuodin - dialogi]]

Katso [Filter](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Filter) {{-}}

### Lisätiedotsuodin

![[_media/Filter-notes-gramplet-42.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Lisätiedotsuodin - dialogi]]

Katso [Filter](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Filter) {{-}}

## Galleria

Gramplet näyttää media objektit {{-}}

### Henkilön Galleria

Katso [Gallery](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Gallery) {{-}}

### Perheen Galleria

Katso [Gallery](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Gallery) {{-}}

### Tapahtuman Galleria

Katso [Gallery](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Gallery) {{-}}

### Paikan Galleria

Katso [Gallery](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Gallery) {{-}}

### Lähteen Galleria

Katso [Gallery](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Gallery) {{-}} Katso [Gallery](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Gallery) {{-}}

## Etunimipilvi

![[_media/GivenNameCloud-detached-grampletFi-41.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Given Name Cloud Gramplet]]

Kuten [Sukunimipilvi Gramplet](#Surname_Cloud_Gramplet) Etunimipilvi gramplet näyttää sukupuusi suosituimmat etunimet. Nimen koko perustuu sen yleisyyteen. Hiirenn vienti näyttää ko. etunimen tarkan lukumäärän ja sen kantajien prosenttiosuuden sukupuun kaikista henkilöistä.

Gramplet pilkkoo etunimen sanaosiinsa välilyöntien kohdalta. Esimerkiksi "Kalle Juhani" näkyy sekä "Kallena" että "Juhanina".

Etunimen kaksoisnapsautus avaa etunimen kaikki kantajat pikanäkymään.

{{-}}

## Image Metadata

![[_media/ImageMetadata-Gramplet-detached-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Image Metadata Gramplet]]

The Image Metadata Gramplet offers an interface to add, edit, and remove [Image Exif Metadata](https://en.wikipedia.org/wiki/Exchangeable_image_file_format) from your images (\*.jpg, \*.png. \*.tiff, \*.exv, \*.nef, \*.psd, \*.pgf). {{-}}

### The interface

#### Data Fields

Photographer  
The name of the person or company taking the image

<!-- -->

Select Date  
Will bring up a calendar, and double-click on a date. The time will be filled in as the current time

<!-- -->

Date  
The Date/ Time needs to be typed in as a very specific format:

Year Mon Day Hour:Minutes:Seconds

1826 Apr 12 14:06:00

<!-- -->

Copyright  
Can be anything that you please... Ex: (C) 2010 Smith and Wesson

<!-- -->

Subject  
Please enter keywords that describe the picture. Do NOT add a space after the comma. Ex. : Census,Milwaukee,Oregon

<!-- -->

Latitude/ Longitude  
Latitude/ Longitude data can be entered in one of two ways:

1.  Degrees Minutes Seconds Ex.: 10 59 14
      
    In this format, you will need to select latitude reference, and longitude reference

    If the Latitude begins with a negative number, select 'S' as Lat. Ref. or 'N' if a positive number. If the Longitude begins with a negative number, select 'W' as the Long. Ref. or 'E' if a positive number.
2.  Decimal, Ex. : -36.05954
      
    In this format, the Latitude and Longitude reference will be selected for you after you click Convert GPS Coordinates or press the Save button. For foreign countries that might use a ", " instead of a ".", please use the "."

<!-- -->

Description  
Type in something about the image, the people in it or the location of the image. Non-latin characters are NOT allowed. ASCII characters only...

#### Buttons

1.  Save
      
    Will write the metadata to the image, and convert latitude/ longitude if it is in decimal format.
2.  Clear
      
    Will clear all data fields
3.  Convert GPS Coordinates
      
    will convert Latitude/ Longitude if it is in decimal format

My favorite source for GPS Coordinates is: <http://www.gpsvisualizer.com/geocode>

### Prerequisites

Once you have installed gexiv2, see above for directions to download and install this addon...

Pyexiv2 can be used from the command line interface (cli) as well, and from within a python script:

1.  import the pyexiv2 library
      
    from pyexiv2 import ImageMetadata, ExifTag
2.  specify your image
      
    image = ImageMetadata("/home/user/image.jpg")
3.  read the image
      
    image.read()

Exif, IPTC, XMP metadata reference tags can be found [here](http://www.exiv2.org/metadata.html).

Example:

  
image\["Exif.Image.Artist"\] \# Artist

Smith and Johnson's Photography Studio

<!-- -->

  
image\["Exif.Image.DateTime"\] \# DateTime

1826 Apr 12 14:00:00

<!-- -->

  
image\["Exif.Image.DateTime"\] = datetime.datetime.now() \# Add DateTime

<!-- -->

  
image.write() \# write the Metadata

### Usage scenario

The preferred way to use this addon is:

1.  install pyexiv2
2.  Install this addon
3.  Restart Gramps
4.  Click Views from the Menu bar, and select Media Views
5.  Open the Side Bar
6.  Slide the available empty right view to about half the screen.
7.  Right click text to the Side Bar tab, and select Add a Gramplet
8.  Select Image Metadata Gramplet
9.  Select an image from the left hand MediaView

{{-}}

## Locations

![[_media/Locations-gramplet-42.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Locations Gramplet]]

Gramplet showing the locations of a place over time. {{-}}

### Place Locations

See [Locations](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Locations) {{-}}

## Notes

![[_media/Notes-gramplet-42.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Notes Gramplet]]

Gramplet showing the notes. {{-}}

### Person Notes

See [Notes](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Notes) {{-}}

### Family Notes

See [Notes](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Notes) {{-}}

### Event Notes

See [Notes](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Notes) {{-}}

### Place Notes

See [Notes](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Notes) {{-}}

### Source Notes

See [Notes](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Notes) {{-}}

### Citation Notes

See [Notes](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Notes) {{-}}

### Repository Notes

See [Notes](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Notes) {{-}}

### Media Notes

See [Notes](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Notes) {{-}}

## Pedigree

![[_media/Pedigree-detached-gramplet-40.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Pedigree Gramplet]]

The Pedigree Gramplet shows a compressed view of the active person's direct ancestors. It defaults to going back 100 generations. The names can be clicked to change the active person, right-click to edit the person. This Gramplet also shows at the bottom of the Gramplet the number of people per generation. Double-click the Generation number to see the matching individuals.

{{-}}

## Preview

![[_media/Preview-gramplet-42.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Preview Gramplet]]

Gramplet showing a preview of a media object. {{-}}

## Pikanäkymä

![[_media/QuickView-RelationToHomePersonQV-detached-grampletFi-41.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Pikanäkymä Gramplet]]

Pikanäkymä grampletilla tuotat pikanäkymän, joka päivittyy siirtyessäsi henkilöstä toiseen. (Toistaiseksi on käytettävissä vain henkilöiden pikanäkymiä).

Voit käynnistää henkilölle [Quick Views](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_8#Quick_Views).

You can change the options by clicking the Option button (top, left hand button of the Gramplet) which will detach the gramplet and bring it up an a window. Select on the top row, and a list of options will appear. Press to apply the changes to the Quick View. You may then close the window to reattach the gramplet.

See the following developer information if you are interested in creating your own [Quick Views](wiki:Quick_Views).

{{-}}

## Ennätykset

![[_media/Records-detached-grampletFi-41.png|Fig {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Records Gramplet]]

Ennätykset gramplet näyttää sukupuustasi mielenkiintoisia faktoja, jotka useimmiten liittyvät ikään. Gramplet listaa jokaisesta kolme johtavaa.

- Nuorin elossa oleva henkilö
- Vanhin elossa oleva henkilö
- Nuorin kuollut henkilö
- Vanhin kuollut henkilö
- Nuorin avioitunut henkilö
- Vanhin avioitunut henkilö
- Nuorin eronnut henkilö
- Vanhin eronnut henkilö
- Nuorin isä
- Nuorin äiti
- Vanhin isä
- Vanhin äiti
- Pariskunta jolla on eniten lapsia
- Viimeksi avioitunut elossa oleva pariskunta
- Varhemmin avioitunut elossa oleva pariskunta
- Lyhyin päättynyt avioliitto
- Pisin päättynyt avioliitto

{{-}}

Ennätys-tiedot voi hyvin tarkistaa sukupuun tietojen laatua. Voit ehkä joutua lisäämää siihen tietoja.

Seuraava esimerkki osoittaa, että löytyy avioliitto-tapahtuma mutta avioparista kummallakaan ei ole kuolema-tapahtumaa. Lisää ainakin toiselle se, ilman päivämäärääkin jos se ei ole tiedossa. Näin ennätystieto korjaantuu.

    Varhemmin avioitunut elossa oleva pariskunta
    # van Dosselaere, Egidius ja Rechters, Petronella (382 vuotta, 1 kuukautta)
    # de Richter, Petrus ja Asscericx, Catharina (379 vuotta, 9 kuukautta)

{{-}}

## References

Gramplet showing the References. {{-}}

### Person References

See [References](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#References) {{-}}

### Family References

See [References](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#References) {{-}}

### Event References

See [References](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#References) {{-}}

### Place References

See [References](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#References) {{-}}

### Source References

See [References](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#References) {{-}}

### Citation References

See [References](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#References) {{-}}

### Repository References

See [References](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#References) {{-}}

### Media References

See [References](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#References) {{-}}

### Note References

See [References](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#References) {{-}}

## Relatives

![[_media/Relatives-detached-gramplet-40.png|Fig {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Relatives Gramplet]]

This Gramplet shows all direct relatives of the active person. It's intended use is as a navigation help, an alternative way to move through your Gramps database. If you detach the Gramplet, and place it next to Gramps, it will allow you to use it to easily change the content of the current "person view".

If you are working in the ancestry views, the active person is the left-most person. By clicking a name in the relatives Gramplet, you can easily change the active person, and all person view in the other window will update. As the relatives Gramplet shows all spouses, all children and all parents, this offers an alternative way of navigating your data.

The names in this Gramplet also allow you to call up the person editor directly, by right-clicking on any of the names. {{-}}

## Residence

Gramplet showing residence events for a person {{-}}

### Person Residence

See [Residence](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Residence) {{-}}

## Istuntoloki Gramplet

![[_media/SessionLog-detached-grampletFi-41.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Session Log Gramplet]]

Istuntoloki pitää kirjaa istunnon aikaisista toimenpiteistä. Se listaa valitut ja muutetut kohteet.

Napsauta hiirellä kerran nimeä ja muutat ao. henkilön aktiiviseksi henkilöksi. Henkilön tai perheen kaksoisnapsautus käynnistää sen sivun. Jos haluat muokata henkilöä muuttamata häntä aktiiviseksi, napsauta nimeä hiiren oikealla.

Gramplet on kätevä, koska sillä voi nopeasti muuttaa aktiivista henkilöä tai muokata kohdetta, tämä kaikki istunnon listalta.

{{-}}

## SoundEx

![[_media/SoundEx-gramplet-example-42.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} SoundEx Gramplet]]

This Gramplet generates SoundEx codes for the names of people in the database.

From the window you can either choose a from the list by shown by selecting the down arrow, or you can type a name into the text field.

The name you type in can be any name even a name not present in your Family Tree.

The result is shown automatically eg:The SoundEx code for **Simpson** is S512

A button is available which brings you to this page. With the button (or using the keyboard shortcut ) you close the window. {{-}}

#### Soundex what is this?

Soundex is the most widely known of all [phonetic algorithms](http://en.wikipedia.org/wiki/Phonetic_algorithm) which allow indexing of words by their sound, as pronounced in English.

The Soundex is a coded surname (last name) index based on the way a surname sounds rather than the way it is spelled. Surnames that sound the same, but are spelled differently, like SMITH and SMYTH, have the same code and are filed together. The Soundex coding system was developed so that you can find a surname even though it may have been recorded under various spellings.

First applied to the 1880 census, Soundex is a phonetic index, not a strictly alphabetical one. Its key feature is that it codes surnames (last names) based on the way a name sounds rather than on how it is spelled. It was to help researchers find a surname quickly even though it may have received different spellings.

Those doing census lookups must use the same method to encode surnames as the census takers did when they generated the database.

To search for a particular surname, you must first work out its code.

- **Basic Soundex Coding Rule:**

Every Soundex code consists of a letter and three numbers, such as W-252. The letter is always the first letter of the surname. The numbers are assigned to the remaining letters of the surname according to the Soundex guide shown below. Zeroes are added at the end if necessary to produce a four-character code. Additional letters are disregarded. Examples: Washington is coded W-252 (W, 2 for the S, 5 for the N, 2 for the G, remaining letters disregarded). Lee is coded L-000 (L, 000 added).

| Number | Represents the Letters |
|--------|------------------------|
| 1      | B, F, P, V             |
| 2      | C, G, J, K, Q, S, X, Z |
| 3      | D, T                   |
| 4      | L                      |
| 5      | M, N                   |
| 6      | R                      |

Disregard the letters A, E, I, O, U, H, W, and Y.

- **Additional Soundex Coding Rules:**
  - Names With Double Letters: If the surname has any double letters, they should be treated as one letter. For example:
    - Gutierrez is coded G-362 (G, 3 for the T, 6 for the first R, second R ignored, 2 for the Z).
  - Names with Letters Side-by-Side that have the Same Soundex Code Number: If the surname has different letters side-by-side that have the same number in the Soundex coding guide, they should be treated as one letter. Examples:
    - Pfister is coded as P-236 (P, F ignored, 2 for the S, 3 for the T, 6 for the R).
    - Jackson is coded as J-250 (J, 2 for the C, K ignored, S ignored, 5 for the N, 0 added).
    - Tymczak is coded as T-522 (T, 5 for the M, 2 for the C, Z ignored, 2 for the K). Since the vowel "A" separates the Z and K, the K is coded.
  - Names with Prefixes: If a surname has a prefix, such as Van, Con, De, Di, La, or Le, code both with and without the prefix because the surname might be listed under either code. Note, however, that Mc and Mac are not considered prefixes.For example, VanDeusen might be coded two ways:V-532 (V, 5 for N, 3 for D, 2 for S) or D-250 (D, 2 for the S, 5 for the N, 0 added).
  - Consonant Separators: If a vowel (A, E, I, O, U) separates two consonants that have the same Soundex code, the consonant to the right of the vowel is coded. <Example:Tymczak> is coded as T-522 (T, 5 for the M, 2 for the C, Z ignored (see "Side-by-Side" rule above), 2 for the K). Since the vowel "A" separates the Z and K, the K is coded. If "H" or "W" separate two consonants that have the same Soundex code, the consonant to the right of the vowel is not coded. Example: Ashcraft is coded A-261 (A, 2 for the S, C ignored, 6 for the R, 1 for the F). It is not coded A-226.

Please visit the [NARA Soundex Indexing page](http://www.archives.gov/research/census/soundex.html) to learn more about Soundex Indexing System. {{-}}

## Tilastot

![[_media/Statistics-detached-grampletFi-41.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Statistics Gramplet]]

Tilastot gramplet tuottaa Tilastot-raportin. Sen rivitekstien tuplanapsautus listaa rivin taustalla olevat kohteet.

Gramplet tuottaa seuraavia tilastotietoja:

- Henkilöt
  - Henkilöiden lukumäärä
  - Miehet
  - Naiset
  - Tuntematonta sukupuolta olevat
  - Henkilöt puutteellislla nimillä
  - Henkilöt puutteellisilla syntymäajoilla
  - Henkilöt ilman sukulaisia
- Perheet
  - Perheiden lukumäärä
  - Sukunimien lukumäärä
- Media kohteet
  - Henkilöt joihin liitetty media kohteet
  - Media kohteiden viittausten kokonaismäärä
  - Media kohteiden lukumäärä
  - Media kohteiden koko yhteensä
  - Puuttuvat media kohteet

Voit työpöydällä irroittaa grampletin napsauttamalla hiiren vasemmalla. Kun lisäät ta poistat henkilöitä sukupuussa, grampletin näyttämä tilastotieto muuttuu samalla.

{{-}}

## Sukunimipilvi

![[_media/SurnameCloud-detached-grampletFi-41.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Surname Cloud]]

Sukunimipilvi Gramplet gramplet näyttää sukupuusi 100 (oletusarvo) suosituinta sukunimeä. Nimen koko perustuu sen yleisyyteen. Hiiren vienti nimen päälle näyttää ko. sukunimen tarkan lukumäärän ja sen kantajien prosenttiosuuden sukupuun kaikista henkilöistä.

Kaksoisnapsauta sukunimeä ja saat pikalistan henkilöistä, joilla on sama sukunimi varsinaisena tai vaihtoehtoisena nimenä. Hekilönimen ja ID:n lisäksi näet syntymäajan ja nimen tyypin. Pikalistassa olevasta henkilöstä avautuu hiiren oikealla valikko Kopioi kaikki, Katso henkilön lisätiedot ja Aktivoi henkilö. Kopiointi kopioi leikepöytään vain henkilörivit, mutta pikanäkymän otsikkotiedot. Katso avaa Henkilömuokkain-ikkunan. Aktivoinnin ansiosta henkilön tietoja näyttävien muiden grampletien tiedot päivittyvät samassa.

Näytettävien sukunimien määrän asetuksen voi muuttaa täällä: ~/.gramps/gramps40/gramplets.ini

{{-}}

## Tehtävät

![[_media/ToDoList-sidebar-grampletFi-41.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} To Do Gramplet]]

Tehtävät gramplet on vapaan tekstin alue. Voit käyttää sitä muistiinpanoihin ja huomautuksiin, joilla jatkat tutkimuksiasi sukupuussa. Samaan tarkoitukseen on itsenäisiäkin ohjelmia, mutta Tehtävät grampsin etu on, että se pitää tiedot sukupuun yhteydessä.

Tehtävät voidaan liittää Grampsin kohteisiin. Esimerkiksi jos avaat Henkilö-näkymän sivupalkkiin Tehtävät grampletin, Gramps liittää muistiinpanon kulloinkin aktiivisena olevaan henkilöön. Sama mahdollisuus on jokaisessa Gramps primäärikohteessa.

Työpöydän Tehtävät gramplet näyttää sukupuun kaikki tehtävät ja niihin liityvät kohteet.

{{-}}

## Suosituimmat sukunimet

![[_media/TopSurnames-detached-grampletFi-41.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Yleisimmät 10 sukunimeä]]

Suosituimmat sukunimet Gramplet listaa 10 yleisintä sukunimeä sukupuussa. Niistä kustakin näytetään:

- sukunimi
- prosenttiosuus
- nimenkantajien lukumäärä

Listassa on myös eri sukunimien ja henkilöiden lukumäärät sukupuussa

Sukunimen kaksoisnapsautus käynnistää pikanäkymän, jossa on kaikki tämän sukunimen kantajat. Nimen lisäksi näkymässä on henkilöiden ID, syntymäaika ja nimen tyyppi.

Suosituimpien sukunimien lukumäärän voi muuttaa tiedostossa ~/.gramps/gramplets.ini

{{-}}

## Tervetuloa

![[_media/Welcome-ToGramps-detached-grampletFi-41.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Welcome Gramplet]]

Tervetuloa gramplet antaa johdattelevan viestin uusille käyttäjille ja perusohjeita.

Tervetuloa viesti kuvaa sen, mikä Gramps on, ohjelman lähdekoodi on vapaa, ja sen kuinka käynnistetään Sukupuu [Family Tree](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees).

Sama informaatio löyty myös [Grampsin käynnistyssivulta](wiki:Main_page)

{{-}}

## Mitä seuraavaksi Gramplet

![[_media/WhatIsNext-detached-grampletFi-41.png|Fig {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Mitä seuraavaksi Gramplet]]

Mitä seuraavaksi Gramplet listaa sukupuusi "kiireisimpiä" puutteita. Listaus perustuu seuraaviin oletuksiin:

- haluat tietää henkilöiden etu- ja sukunimen, syntymäajan ja -paikan ja kuolinajan ja -paikan
- haluat tietää jokaisesta perheen avioparista isän, äidin, avioitumisen ajan ja paikan ja avioerosta sen ajan ja paikan
- haluat tietää ainakin äidin perheestä, joka ei perustu avioitumiseen
- mitä läheisempi henkilön suhde on keskushenkilöön, sitä "kiirellisempi" puute on.
- mitä läheisempi yhteinen esi-isä on keskushenkilön kanssa, sitä "kiirellisempi" puute on.(esim. serkut ovat kiireellisempiä kuin sedät, vaikka molemmilla etäisyys on 3 sukupolvea, koska serkkujen yhteinen esi-isä on isä/äiti,kun taas sedillä yhteinen esi-isä on isoisä/isoäiti)
- avioliiton ja puolison tiedot ovat hieman vähemmän "kiireisiä" kuin suoran sukulaisen tiedot
- velipuolet eivät ole niin "kiireisiä" kuin täysveljet

Tämän grampletin listan tekstin voi valita ja kopioida leikepöydän kautta muuhun dokumenttiin.

![[_media/Whats-next-gramplet-configure-dashboard-60.png|Fig {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} What's Next Gramplets configuration options]]

Gramplet voi ohittaa listauksessa tapahtumia hyödyntämällä tageja. Ohitettavat tagit valitaan Grampletin asetuksissa työkalupalkin kautta. Voit esimerkiksi ohittaa tapaukset, joissa on asetettu ao. tagi:

- henkilö on tutkittu loppuun
- perhe on tutkittu loppuun
- henkilö tai perhe ohitetaan vain, jota listat ovat lyhyempiä

{{-}}

{{-}}

# Muiden kategorioiden sivu- ja alapalkin grampletit

Since Gramps 6.0 we have common and specific gramplets according active view (navigation/category).

- Back references gramplets are like the tab on object Editor.
- Filter gramplet is like the previous filter sidebar
- Common models for Notes, Gallery, Sources, Citations, Events
- Children gramplet on Person views (also ancestry category and relations), family view

Henkilöt==

### Jälkeläiset

![[_media/Descendant-detached-grampletFi-41.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Descendant Gramplet]]

Jälkeläiset gramplet näyttää aktiivisen henkilön suorat jälkeläiset.

Puolisot ja lapset ovat Grampsin sukupuun mukaisessa järjestyksessä. Puolisoiden järjestys on muutettavissa Suhteet-muokkaimessa. Lasten järjestys on muutettavissa Perhe-muokkaimen Lapset-osiossa nuolinäppäimillä tai tarttumalla hiirellä ao. lapseen ja raahaamalla ao. lapsen riviä hiirellä.

Gramplet perustuu Jälkeläisten raporttiin, joka löytyy tekstiraporteista.

Jälkäläiset grampletin näyttämä päivittyy aktiivisen henkilön vaihtamisesta ja sukupuun vaihtamisesta. Sukupuun muut päivittämiset eivät automaattisesti muuta sisältöä, koska se veisi liikaa aikaa.

Grampletin minimointi estää sisällön päivittämisen.

{{-}}

### Henkilön tiedot

### Viuhkakaavio

![[_media/FanChart-detached-grampletFi-41.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Viuhkakaavio Gramplet]]

Viuhkakaavio gramplet näyttää aktivisen henkilön suorat esivanhemmat ympyräkaaviona. Se on samanlainen kuin Esipolvien taulu, mutta aktiivinen henkilö on keskustana ja muut sukupolvet ovat kehillä.

Napsauta kaaviossa vanhempaa ja hänen esivanhempansa laajenevat ulommille kehille. Oikean painikkeen napsautuksella voit:

- valita henkilön kaavion aktiiviseksi henkilöksi
- valita henkilöön liittyviä sukulaisia aktiiviseksi henkilöksi
- muokata henkilöä, jolloin avautuvassa henkilömuokkaimessa voi myös lisätä perheisiin lapsia
- lisätä uuden henkilön tietokantaan
- lisätä henkilölle uuden perheen ja sille lapsia
- kopioida henkilön nimen ja syntymä- ja kuolintiedot leikepöydälle

Napsauttamalla kaavion harmaata taustaa kaaviota voi pyörittää hiirellä keskustansa ympäri. Hiireen keskustasta tarttumalla voi siirtää kaavion paikkaa.

Ulomman kehän musta reuna ilmaisee, että henkilöllä on usea vanhempi. Musta napakymppi ilmaisee, että henkilöllä on lapsia.

Aktiivisen henkilön ja sukupuun vaihtaminen päivittää viuhkakaavion.

Grampletin sisältö ei päivity grampletin ollessa minimoituna.

{{-}}

### Esipolvien taulu

![[_media/Pedigree-detached-grampletFi-41.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Esipolvien taulu Gramplet]]

Esipolvien taulu Gramplet näyttää tiiviisti aktiivisen henkilön esivanhemmat, oletusarvoisesti 100 sukupolvia taaksepäin. Taulussa näkyy henkilön nimi, syntä- ja kuolinajat. Henkilön nimen napsauttaminen vaihtaa aktiivisen henkilön, nimen napsauttaminen okealla avaa Henkilömuokkaimen.

Gramplet näyttää alaosassaan kunkin henkilöiden lukumäärän sukupolvittain. Sukupolven numeron kaksoisnapsautus avaa pikanäkymään sukupolveen kuuluvat henkilöt. "Kaikista sukupolvista" kaksoisnapsauttamalla pikanäkymään tulevat henkilön kaikki esivanhemmat.

{{-}}

### Sukulaiset

![[_media/Relatives-detached-grampletFi-41.png|Fig {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Relatives Gramplet]]

This Gramplet shows all direct relatives of the active person. It's intended use is as a navigation help, an alternative way to move through your Gramps database. If you detach the gramplet, and place it next to Gramps, it will allow you to use it to easily change the content of the current "person view".

If you are working in the ancestry views, the active person is the left-most person. By clicking a name in the relatives gramplet, you can easily change the active person, and all person view in the other window will update. As the relatives gramplet shows all spouses, all children and all parents, this offers an alternative way of navigating your data.

The names in this gramplet also allow you to call up the person editor directly, by right-clicking on any of the names.

{{-}}

## Paikat kategoria

## Media kategoria

### Kuvan metadata

![[_media/ImageMetadata-detached-grampletFi-41.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Image Metadata Gramplet]]

The Image Metadata Gramplet offers an easy interface to add, edit, and remove Image Exif Metadata from your images (\*.jpg, \*.png. \*.tiff, \*.exv, \*.nef, \*.psd, \*.pgf).

{{-}}

Once you have installed pyexiv2, see above for directions to download and install this addon...

Pyexiv2 can be used from the command line interface (cli) as well, and from within a python script:

1.  import the pyexiv2 library
      
    from pyexiv2 import ImageMetadata, ExifTag
2.  specify your image
      
    image = ImageMetadata("/home/user/image.jpg")
3.  read the image
      
    image.read()

Exif, IPTC, XMP metadata reference tags can be found [here](http://www.exiv2.org/metadata.html).

Example:

  
image\["Exif.Image.Artist"\] \# Artist

Smith and Johnson's Photography Studio

<!-- -->

  
image\["Exif.Image.DateTime"\] \# DateTime

1826 Apr 12 14:00:00

<!-- -->

  
image\["Exif.Image.DateTime"\] = datetime.datetime.now() \# Add DateTime

<!-- -->

  
image.write() \# write the Metadata

#### Skenaario käytöstä

My perferred way to use this addon is:

1.  install pyexiv2
2.  Install this addon
3.  Restart Gramps
4.  Click Views from the Menu bar, and select Media Views
5.  Open the Side Bar
6.  Slide the available empty right view to about half the screen.
7.  Right click text to the Side Bar tab, and select Add a Gramplet
8.  Select Image Metadata Gramplet
9.  Select an image from the left hand MediaView

#### Käyttöliittymä

##### Tietokentät

Photographer  
The name of the person or company taking the image

<!-- -->

Select Date  
Will bring up a calendar, and double-click on a date. The time will be filled in as the current time

<!-- -->

Date  
The Date/ Time needs to be typed in as a very specific format:

Year Mon Day Hour:Minutes:Seconds

1826 Apr 12 14:06:00

<!-- -->

Copyright  
Can be anything that you please... Ex: (C) 2010 Smith and Wesson

<!-- -->

Subject  
Please enter keywords that describe the picture. Do NOT add a space after the comma. Ex. : Census,Milwaukee,Oregon

<!-- -->

Latitude/ Longitude  
Latitude/ Longitude data can be entered in one of two ways:

1.  Degrees Minutes Seconds Ex.: 10 59 14
      
    In this format, you will need to select latitude reference, and longitude reference

    If the Latitude begins with a negative number, select 'S' as Lat. Ref. or 'N' if a positive number. If the Longitude begins with a negative number, select 'W' as the Long. Ref. or 'E' if a positive number.
2.  Decimal, Ex. : -36.05954
      
    In this format, the Latitude and Longitude reference will be selected for you after you click Convert GPS Coordinates or press the Save button. For foreign countries that might use a ", " instead of a ".", please use the "."

<!-- -->

Description  
Type in something about the image, the people in it or the location of the image. Non-latin characters are NOT allowed. ASCII characters only...

##### Painikkeet

1.  Save
      
    Will write the metadata to the image, and convert latitude/ longitude if it is in decimal format.
2.  Clear
      
    Will clear all data fields
3.  Convert GPS Coordinates
      
    will convert Latitude/ Longitude if it is in decimal format

My favorite source for GPS Coordinates is: [GPS Visualizer](http://www.gpsvisualizer.com/geocode)

{{-}}

[Category:Fi:Dokumentaatio](wiki:Category:Fi:Dokumentaatio)
