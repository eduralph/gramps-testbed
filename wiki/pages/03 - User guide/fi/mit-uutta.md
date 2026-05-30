---
title: Fi:Gramps 6.0 Wiki-käyttöohje - Mitä uutta
categories:
- Fi:Dokumentaatio
managed: false
source: wiki-scrape
wiki_revid: 119750
wiki_fetched_at: '2026-05-30T18:18:55Z'
lang: fi
---

Tässä on suomennos, joka on osin kesken:

Tässä sivussa kuvataan pääpiirtein Gramps 6.0 erot versioon 3.4 verrattuna. Muutokset on kuvattu tarkemmin myöhemmin tässä käyttöohjeessa. Versiosta 3.4 versioon 6.0 siirtyviä käyttäjiä kehotetaan perehtymään tähän sivuun sen varmistamiseksi, että käyttäjä osaa hyödyntää uusia omaisuuksia alkaessaan käyttämään versiota 6.0.

# Ennen version nostoa

Varmin tapa varmistaa tietojen säilyminen on varmuuskopiointi:

1.  Käynnistä Gramps 3.4 tai Gramps 4.1
2.  Avaa sukupuusi
3.  Varmuuskopioi sukupuusi "gramps xml" muotoon tai , jos haluat sukupuun mukaan valokuvasi ja muut mediatiedostosi, "gramps xml paketti" muotoon.
4.  Sulje sukupuu ja toista edellä oleva jokaiselle muulle sukupuullesi
5.  Vie tulostiedostot turvalliseen paikkaan

Lisätietoja löytyy [Sukupuun varmuuskopiointi](wiki:Fi:Gramps_6.0_Wiki-käyttöohje_-_Sukupuiden_hallinta#Sukupuun_varmuuskopiointi).

Tietojesi tultua varmistetuksi siirry Gramps versio 6.0 asennukseen. Käyttöjärjestelmäsi tavanomainen asennusprosessi varmistaa useimmiten, että vanhan ja uuden version kesken ei synny ristiriitaa. On kuitenkin varmempa ensin poistaa versio 3.4 koneelta pois ennen version 6.0 asentamista. Toinen tapa on asentaa 6.0 toiseen hakemistoon kuin missä 3.4 on. Näin onkin meneteltävä aina, jos asennat Grampsin lähdekoodista. Lisätietoja Gramps 6.0 asentamisesta löytyy (englanniksi) [Downloading the latest Gramps](wiki:Download).

Asennettuasi Gramps 6.0 version voit avata sukupuusi ja jatkaa työskentelyä. Jos avauksessa on ongelmia (esim. tietokoneesi tultua uudelleenasennetuksi) luo sukupuusi edellä tehdyistä varmuuskopioista.

# Perustoimintojen näkyvät muutokset

Päivityksen jälkeen näkyvät muutokset: käyttöliittymä, data

## Tietomalli

Tietomallia on muutettu:

1.  Uudet Päivämäärä ja Kieli -kentät Paikan nimessä

- Sukupuuta **ei voi avata** versioissa Gramps 3.4/4.0 ja Gramps 6.0 nostamatta tai alentamatta versiota.

<!-- -->

- Gramps XML tiedosto jonka Gramps 3.4/4.0 tuottaa **ei ole yhdenmukainen** Gramps 6.0. tuottaman kanssa

<!-- -->

- Gramps 6.0 käyttää nyt vain python3 versiota

Katso (engl.) [detailed changes](wiki:Database_Formats#Detailed_Changes) , jossa on yksityiskohtaisesti sisäisen tetokannan muutokset.

## Käyttöliittymä

- GtkBuilder tarkistettu, fiksattu Gtk3 varoituksia ja luovuttu vanhentuneiden metoodien käytöstä
- muutettu kuvakkeiden ja painikkeiden käsittelymetoodeja
- Uusi Paikka Muokkain

![[_media/Place_editor_42.png|Uusi Paikka muokkain paikan nimen käsittelyllä]] {{-}}

- Uusi widgetti: *[interactive searchbox](wiki:Gramps_6.0_Wiki_Manual_-_Navigation#Finding_records)*. Käytä interaktiivisen haun hakukenttää sen käyttämiseksi.

![[_media/Interactive_search.png|Uusi interaktiivinen hakukenttä]] {{-}}

1.  tehokkaampi (lajiteltujen kenttien binäärihaku).
2.  muokattava(150ms viivästys jotta teksti ei mene sekaisin)

- Kykenee [tuomaan KML](wiki:Gramps_6.0_Wiki_Manual_-_Categories#Adding_places_from_KML_files) dataa Geography näkymiin
- Parannettu useiden valittujen kohteiden poistamista Näkymistä (action group)

![[_media/Action_group_dialog.png|Ryhmätoimintoja koskeva kysymysdialogi]] {{-}}

- Sallitaan henkilön raahaus Perheen otsikosta tai Lisää, Muokkaa, Jaa -painikkeiden lähistöllä.

Add drag support on more Views, Selectors and Editors.

- Lisätty hiiren oikealla "Kopioi kaikki" kaikkiin PikaTauluihin (QuickTables).

Kaikki data TreeView -näkymästä, ml. piilossa olevat sarakkeet.

- Lisätty hiiren oikeaan API ListModel'iin

{{-}}

## Paikka

- Parannettu Paikka Muokkain and uusi Paikannimi Muokkain

![[_media/Place_name_editor.png|Uusi Paikannimi Muokkain]] {{-}}

- tarkistettu Paikan vaihtoehtoiset nimet -käsittelyä ja muokkausta
- Uusia asetuksia käyttäjän käyttöön - [](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Places) dialogin kielekevaihtoehdoissa

![[_media/Place_settings_42.png|Uusi Paikat kohde into Paikat dialogissa]] {{-}}

- Uusi suodatin: *ympärillä*

{{-}}

## Raportit, Työkalut, Grampletit

- **Yksityiseksi** merkittyjen valinnan johdonmukaistaminen raporteissa

![[_media/Include-data-marked-private-checkbox-example-60.png|Vakio*Yksityinen* valintaruutu]] {{-}}

- Nimen muotoilujen johdonmukaistaminen raporteissa
- Lisätty DeferredFilter luokka (GenericFilter'in aliluokka)
- Uusi tekstiraportti : Lisätietojen linkit
- Korjattu Kirjoissa aakkoshakemistojen ja sisällysluettelon virheitä
- Kehitetty Tyylit Muokkainta
- Kehitetty tekstiraporttien alaviiteitä
- Muutettu Täyttä henkilöraporttia
- Muutettu Esivanhempien puu -raporttia: Sisarukset mukana ja liikkuminen useassa suunnassa
- Lisätty nimen muodon valinta ja viivästetty käännös Records raporttiin
- Lisätty viivästetty käännös Aikajana-kaavioon
- Lisätty Lähteet ja Lainaukset näkymiin [Attribuutit gramplet](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Attributes_Gramplet)

![[_media/Attributes_gramplet_source_citation.png|Lisätty Lähteet ja Lainaukset Attribuutit grampletiin]] {{-}}

- Lisätty uusi paikan [sijainnit gramplet](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Location_Gramplet)

{{-}}

# Konepellin alla

Teknistä tietoa

## Riippuvuudet

- Tuettuna vain**python3**. ( python2 tuki lopetettu)
- Tarvitaan GTK+ 3.10 ja pygobject 3.12 tai uudemmat versiot niistä

## Lokalisointi

- Rajoita lyhenteiden käyttöä viesteihin, erota paremmin ssältö (str) ja tyylie (GUI).
- Uusi [Päivämäärä-käsittelijä](wiki:Päivämäärä-käsittelijä) modulissa [Japanese](https://github.com/gramps-project/gramps/blob/master/gramps/gen/datehandler/_date_ja.py)
- Tarkistettu Slovenian ja Tsekkien Päivämäärä-käsittelijät
- Uudet käännökset ja päivämäärien käsittelijät : toteutettu sekä "traditionaalinen" että "yksinkertaistettu" kiinalainen
- Tarkistettu Serbia

## Tiekartta

- [Roadmap](wiki:Roadmap): [6.0.0](http://www.gramps-project.org/bugs/roadmap_page.php?version_id=53)

## Muutoslogi

- [Changelog 6.0.0](http://www.gramps-project.org/bugs/changelog_page.php?version_id=53)

## Lokalisointi

- Käännöstiedostot huomioivat eräitä päivämäärätekstejä
- Rajoitettu muotoilun ohjausta viesteissä glade tiedostoihin, sisältö (str) ja tyyli (GUI) paremmin erillään.

## Database backend

- Enhancements on *to_struct()*, synchronisation?
- Uusi *handle* moduuli
- [GEPS 032: DB backend API](wiki:GEPS_032:_Database_Backend_API)
- [GEPS 033: Abstract DB API](wiki:GEPS_033:_Abstract_Database_API)

{{-}}

# Lisätietoa

## Sekalaista

Tietokannan version korotus rakentaa uudelleen käyttäjäkohtaisten tapahtumien listan.

## Tiekartta

- [Roadmap](wiki:Roadmap): [6.0.0](http://www.gramps-project.org/bugs/roadmap_page.php?version_id=34)

## Muutosloki

- [Changelog 6.0.0](http://www.gramps-project.org/bugs/changelog_page.php?version_id=34)

[Category:Fi:Dokumentaatio](wiki:Category:Fi:Dokumentaatio)
