---
title: Fi:Gramps 6.0 Wiki-käyttöohje - Lisäosien hallinta
categories:
- Fi:Dokumentaatio
managed: false
source: wiki-scrape
wiki_revid: 111221
wiki_fetched_at: '2026-05-30T18:33:49Z'
lang: fi
---

{{#vardefine:chapter\|9}} {{#vardefine:figure\|0}}

Lisäosien hallinta löytyy valikosta . Sen monet piirteet on tarkoitettu kehittäjille ja he näkevät alla kuvatut dialogit. Alla mainitaan, milloin loppukäyttäjän toiminnallisuuksissa on eroa.

Gramps havaitsee 'optimise' flagista, ajetaanko sitä Käyttäjän vai Kehittäjän moodissa:

`python -O gramps.py`

Katso [Debugging Gramps](wiki:Debugging_Gramps).

Gramps koostuu ytimestä (core) ja monista lisäosista (plugins). Ydin Grampsin käynnistyessä ladataan ydin ja vain suppea määrä lisäosia. Näin käynnistysaika lyhenee ja muistin tarve pienenee. Gramps lataa monet lisäosat vasta niitä tarvittaessa, joten monenkaan käyttäjän ei tarvitse olla tietoisia niiden olemassaolosta tai niidn viivästetystä latauksesta.

Lisäosien hallinnalla voit kontrolloida, kuinka Gramps hallinnoi lisäosia.

## Lisäosien tyypit

Grampsin lisäosat jaetaan kahteen pääryhmään: "käyttäjän lisäosat" ja "järjestelmän lisäosat". Käyttäjän lisäosatovat niitä, joita käytät ja säädät antamaan itsellesi eri toiminnallisuuksia. Gramps käyttää itse järjestelmän lisäosia.

**Käyttäjän lisäosien** tyypit Grampsissa ovat seuraavat:

1.  dokumenttien luojat: Gramps kirjoittaa näillä raportteja (pdf, odf, ascii text, ...)
2.  viejät: Gramps muodostaa näillä valikossa tarjottavat tiedostotyypit
3.  grampletit: pikku ohjelmia lisättäväksi Grampsin työpöydälle tai irrotettavaksi normaaliksi ikkunakseen
4.  grampsin näkymät: Grampsin pääikkunannäkymät eri kategorioille
5.  tuojat: Gramps tuo näillä valikossa tarjottavat tiedostotyypit
6.  karttapalvelut: Gramps käyttää näitä Paikka-näkymässä valittuun karttapalveluun siirtymisessä (*Siirry* työkalupainike)
7.  pikaraportit: pieniä raportteja listamuotoisten näkyminen konteksivalikossa tai Pikaraportti grampletissa
8.  raportit: Grampsin tarjoamat teksti- ja graafiset raportit
9.  työkalut: valikosta käynnistettävät työkalut

Grampsissa tarjolla olevat **järjestelmälisäosat** ovat:

1.  plugin libs: ohjelmakirjastot, jotka antaat lisätoiminnallisuutta.
2.  relationships: kielikohtaiset suhdelaskurit

Grampsin mukana tulee paljon lisäosia. Kuka tahansa voi kuitenkin kirjoittaa lisäosan ja jakaa sen. Näitä kolmannen osapuolen lisäosia kutsuaan laajennuksiksi ("addons"). Kannustamme käyttäjiä ja kehittäjiä jakamaan tekemänsä muiden Gramps käyttäjien kanssa.

## Rekisteröinti ja lataus

Laajennukset voivat sijaita työasemassa ja Grampsin tuntemia, jolloin ne ovat **rekisteröityjä**, tai niitä pidetään palvelimella ja Gramps tietää niistä vain nimen, tyypin ja kuvauksen, jolloin ne ovat **laajennuksia**.

Grampsin käynnistyessä se lukee atomaattisesti paikalliset laajennukset ja ne rekisteröityvät. Lisäosien hallinnolla voidaan ladata työasemaan laajennuksia, jotta ne tulevat siten rekisteröidyksi.

Gramps **lataa** paikallisia lisäosia seuraavissa tilanteissa:

1.  niitä ladataan Grampsin käynnistyessä. Jotkut lisäosat ladataan aina (esim. ei-piilotetut näkymät), eräisiin lisäosiin voi asetettuna flagi, että lisäosa on ladattava,
2.  jotkut ladataan lennosta, kun käyttäjä napsauttaa näkymää tai haluaa jonkun raportin,
3.  käyttäjä vaatii lisäosien hallinnassa lisäosan lataamista

## Piiloon/Esille

Lisäosien hallinnassa voi piilottaa tai tuoda esille laajennuksia. JOtkut valikot eivät näytä piilotettuja laajennuksia, jolloin niitä ei voi valita. Jos esim. jokin gramplet on piilotettuna, sitä ei näy konteksivalikossa "Lisää gramplet" , joka tulee esille napsautettaessa oikealla painikkeella Työpöydän taustaa. Piilottamisella ei ole mitään vaikutusta eräissä laajennuksissa kuten Suhteet tai Näkymät tai piilottaminen ei ole edes mahdollista.

## Toimenpiteet

LIsäosien hallinta -ikkunassa on kaksi lehteä: Rekisteröidyt lisäosat ja Ladatut lisäosat.

### Rekisteröidyt lisäosat

![[_media/Registered-pluginsFi-41.png|Kuva {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Rekisteröidyt lisäosat]]

Tässä on listattuna kaikki Grampsin löytämät lisäosat. Ne ovat joko osa Grampsia tai ne sijaitsevat gramps41/plugins hakemistossa [Gramps User Directory](wiki:ks._Gramps_6.0_Wiki_Manual_-_User_Directory). Lisäosan tyyppi on listan ensimmäisenä sarakkeena.

Lisäosan voi piilottaa tai kätkeä. Tämä on käyttökelpoista vain käyttäjän lisäosien kohdalla.

{{-}}

### Ladatut lisäosat

![[_media/Loaded-pluginsFi-41.png|Kuva {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Ladatut lisäosat]]

Tässä on listattuna kaikki liäosat, jotka on aiottu ladata. Normaalisista kaikki näkymät (kuten Suhteet) ladataan, kuten myös kaikki käyttämäsi grampleti/raportit/työkalut.

Jos lisäosan latauksessa tulee virhe, sen status näytetään tällä lehdellä. Napsauttamalla kahdesti riviä saat yksityiskohtaiset tiedot virheestä. Käytä niitä ottaesasi yhteyttä lisäosan kirjoittajaan tai Grampsin bugilistaan.

Jos myöhemmin et enää pidäkään laajennuksesta, merkitse se "piilotetuksi" ja sitä ei enää näytetä.

{{-}}

[Category:Fi:Dokumentaatio](wiki:Category:Fi:Dokumentaatio)
