---
title: Fi:Gramps 6.0 Wiki-käyttöohje - Asetukset
categories:
- Fi:Dokumentaatio
- Stub
managed: false
source: wiki-scrape
wiki_revid: 125635
wiki_fetched_at: '2026-05-30T18:15:13Z'
lang: fi
---

{{#vardefine:chapter\|13}} {{#vardefine:figure\|0}} Tämän osion aiheena ovat asetukset, joita voit hallinnoida Grampsissa.

## Asetukset

![[_media/EditPreferencesTabsOnly-overview-50-fi.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Asetuksien kaikki lehdet]]

Useimmat Grampsin asetukset määritetään ikkunassa. Se avataan valinnalla .

Yläosan lehdet on jaoteltu asetusryhmittäin. {{-}}

### Yleistä

![[_media/EditPreferences-General-tab-example-50-fi.png|Right|thumb|450px|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Yleistä-asetukset (Linux)]]

![[_media/Edit-preferences-general-tab-50-fi.png|Right|thumb|450px|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Yleistä-asetukset (Microsoft Windows 10)]]

Tällä lehdellä ovat ohjelman yleiseen käyttöön liittyvät asetukset. Ne ovat:

-   
  Tämä valintaruutu **näkyy vain ja vaikuttaa Microsoft Windows käyttöjärjestelmissä** Asetus vaikuttaa niiden Unicode-merkkien ulkoasuun, jotka eivät ole käytössä olevassa merkistössä. Microsoft Windowsin vakio merkkien käsittelijä näyttää korvaavia merkkejä, jos merkkiä ei ole käytettävissä. Eräille käyttäjille vaihtoehtoinen merkkien käsittelijä antaa paremman lopputuloksen. Jos näytössä tai raportissa näkyy virheellisiä merkkejä (tyypillisesti kuten [little box](https://en.wikipedia.org/wiki/Specials_(Unicode_block)#Replacement_character) with numbers in it), kokeile tätä asetusta. Asetuksen jälkeen Gramps on käynnistettävä uudelleen. (Katso Microsoftin tuen artikkeli: **[Why does some text display with square boxes in some apps on Windows 10?](https://support.microsoft.com/en-us/help/3083806/why-does-some-text-display-with-square-boxes-in-some-apps-on-windows-1)**

-   
  Tämä valintaruutu vaikuttaa [GEDCOM data](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees#GEDCOM_import) tuonnissa. Tällä asetuksella jokaisessa tuodussa kohteessa on lähdeviittaus tuontitiedostoon. **Huomaa - Oletuslähdeviite voi hidastaa merkittävästi GEDCOM datasi tuontia.**

-   
  Valintaruutu (Oletusarvo: `Tuotu %Y/%m/%d %H:%M:%S` ) **Huomaa - Oletustagi voi hidastaa merkittävästi GEDCOM datasi tuontia.**

-   
  Tällä valintaruudulla asetetaan päälle ja pois Lisätietojen oikoluku. Toiminto edellyttää **gtkspell** paketin lataamista.

-   
  Tällä valintaruudulla asetetaan päälle ja pois ikkunan näyttäminen ohjelman käynnistyksessä.

-   
  Tällä valintaruudulla asetetaan päälle ja pois viimeisen näkymän näyttäminen. Kun asetus on päällä, ohjelma avataan näkymään, jossa suljit edellisellä kerralla sen.

- Voit syöttää sukupolvien lukumäärän, jota käytetään sukulaisuussuhteissa. Oletusarvo on **`15`**.

- Tässä voit syöttää mediatiedostojen peruspolun. kuvakkeesta avautuu muokkain, jossa voit määrittää halutun polun.

- Valitse rytmi, jolla Gramps tarkistaa [Addons](wiki:6.0_Addons#Installing_Addons_in_Gramps) päivitykset. Oletusarvo: *Ei koskaan*

- Oletusarvo: *Vain uudet laajennukset*

- Oletusarvo: [`https://raw.githubusercontent.com/gramps-project/addons/master/gramps50`](https://raw.githubusercontent.com/gramps-project/addons/master/gramps50)

-   
  Valintaruutu on oletusarvoisesti päällä.

-   
  Painike käynnistää laajennusten tarkistuksen. Jos laajennuksia on saatavilla, ne näytetään ikkunassa, josta voit valita ja asentaa haluamasi.

{{-}}

##### Saatavilla olevat Grampsin laajennusten päivitykset

![[_media/AvailableGrampsUpdatesforAddons-example-listing-50-fi.png|Right|thumb|550px|"Saatavilla olevat laajennusten päivitykset Grampsiin" ikkuna , jossa on listattuna esimerkinluonteisesti Gramps 6.0 laajennuksia]]

ikkunan lista on ryhmitetty tyypeittäin, jotka voit laajentaa "Valitse" painikkeesta.

- Valitse kaikki-painikkeesta voit valita kerralla kaikki laajennukset asennettaviksi, mutta voit laajennuskohtaisista valintaruuduista valita ne yksitellenkin.

- Sitten painikkeella lataat päivitykset netistä.

- ikkuna suljetaan painikkeella

- ikkunasta poistutaan painikkeella.

- Laajennuksien käyttämiseksi sulje Gramps valinnalla ja käynnistä se uudelleen.

{{-}}

#### Päivän vihje ikkuna

![[_media/TipOfTheDay-dialog--example-keeping-good-records-50-fi.png|Right\|thumb\|400px\|Fig. {{#var:chapter}}.{{#vardefineecho:figure\|{{#expr:{{#var:figure}}+1}}}} Päivän vihje ikkuna]] ikkuna näyttää hyödyllisiä vihjeitä, jos se on aktivoitu valinnan lehdellä .

Seuraavat vaihtoehdot on käytettävissä:

-  (valintaruutu on valittuna oletusarvoisesti) - ota valinta pois lopettaaksesi vihjeiden näytön jatkossa.

- \- Siirry seuraavaan vihjeeseen.

- \- Poistu vihjeikkunasta kunnes käynnistät Grampsin uudelleen.

{{-}}

### Sukupuu

![[_media/EditPreferences-FamilyTree-tab-example-50-fi.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menu:  - "Sukupuu" - lehden esimerkki - oletusarvot]]

This tab contains preferences relevant to the Family Tree Database.

- \-

  - **BSDDB**(oletus) -
  - *Sqlite3* -

- \-

- \-

- Sukupuut tallennetaan oletusarvoisesti **kotihakemistoon`/.gramps/grampsdb`**. Jollet ehdottamasti halua muuttaa tätä, pidä oletuspolku. Polkuun vaikuttaa käyttöjärjestelmä, ks. [Käyttäjän hakemisto](wiki:Fi:Gramps_6.0_Wiki_Manual_-_User_Directory).

-   
  This checkbox option controls the enabling and disabling of the loading on start up of the last used database.

- \-

- 

- \-

  - **Ei koskaan**(oletusarvo)

{{-}}

Katso myös:

- Laajennus [PostgreSQL](wiki:Addon:PostgreSQL) - tämä lisää tuen PostgreSQL kannoille.

### Näyttö

![[_media/EditPreferences-Display-tab-default-50-fi.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menu: "Muokkaa&gt;Asetukset..." - "Näyttö" - lehti - oletusarvot]]

Tällä lehdellä ovat asetukset, jotka liittyvät tietojen ja nimien näyttämiseen. Vaihtoehdot ovat:

- Tämä valinta ohjaa nimien näyttämistä. Grampsissa on kaksi nimien näyttömuotoa: esimääritetyt muodot ja käyttäjän määrittämät muodot. Tarjolla on useita esimääritettyjä nimimuotoja: Etunimi - Etuliite Patronyymi, Jälkiliite Etunimi - Etuliite Sukunimi, Etunimi Patronyymi Jälkiliite jne.

  - Oikealla sivulla oleva painike avaa ikkunan, jossa näytetään lista valintamahdollisuuksia. Muodolle annetaan myös esimerkki. Kun esimääritetyistä muodoista ei ole tarpeen hoitamiseen, voit määrittää oman muotosi. painikkeella lisätään listaan uusi muoto. Listalta löytyy mm. muoto **SUKUNIMI,Etunimi Loppupääte(kutsuma)** ja sille esimerkki : **SMITH, Edwin Jose Sr (Ed)**. Jos lisäät uuden muodon, ja painikkeet aktivoituvat ja niillä voi muuttaa listaa.

<!-- -->

- -   
    Valintaruutu on oletusarvoisesti pois päältä. Aktivointi sallii Grampsia harkitsemaan patronyymisä tai matronyymisiä nimiä sukunimenä.

- Tämä valinta ohjaa päivämäärien näyttämistä. Tarjolla on useita muotoja, mutta ne saattavat riippua käyttöjärjestelmäsi paikallisista asetuksista. Oletusarvo: **YYYY-MM-DD (ISO)**

<!-- -->

- Tämä valinta ohjaa paikannimien näyttämistä.

  - painikkeesta avautuu

    - painikkeesta voi lisätä uuden paikannimimuodon ja painikkeesta voi poistaa jonkun muodon

    -  (paikan nimikkeen kääntö hierarkisesti ylemmästä alempaan -järjestykseen, esim. 'Helsinki, Töölö')

    - painikkeella suljetaan 'Paikan muoto muokkain'.

-  (valinta automaattisesti aktiivinen)

- **Vuodet**(oletusarvo)

<!-- -->

- **gregoriaarinen**(oletusarvo). Tämä valinta ohjaa kalenteria raporteissa, työkaluissa, grampleteissa ja näkymissä. Useita kalentereita on tarjolla (katso [Date Edition](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_Editing_Data:_Detailed_-_part_1#Editing_dates)). Eri kalenteista olevat kaksi päivämäärää eivät määritä kunnolla ajanjaksoa tai -jaksoa. (Gregoriaanisen kalenterin käyttö oletuksena antaa johdonmukaisempia ajanjaksojen näyttämisiä).

<!-- -->

- Tämä valinta vaikuttaa lapsen sukunimen lähtökohtaiseen sukunimen määräytymiseen lisättäessä lasta sukupuuhun. Oletusrvoinen käyttää isän sukunimeä. tarkoittaa, ettei ohjelmallista arvaamista tehdä. Valinta johtaa siihen, että lapsen sukunimi koostuu isän ja äidin sukunimistä, tässä järjestyksessä. Viimeisenä muodostaa lapssen sukunimen isän etunimestä "sson" päätteellä (esim.. the son of Edwinin pojan sukunimeksi arvataan *Edwinsson*).

- - **Tuntematon**(oletusarvo)
  - Avioliitto
  - Avoliitto
  - Rekisteröity parisuhde

<!-- -->

- Oletusarvo:**150**

<!-- -->

- Tämä valinta määrittää, mitä tietoa näytetään tilapalkissa. Vaihtoehdot ovat **Aktiivisen henkilön nimi ja ID**(oletusarvo) tai **Suhde kotihenkilöön (koettiin)**.

<!-- -->

- *päällä* (oletusarvo). Tämä valintalaatikko säätelee, näytetäänkö teksti navigointipalkin kuvakkeen yhteydessä. Valinta astuu voimaan ohjelman uudelleen käynnistyksellä.

<!-- -->

- *poissa päältä*(oletusarvo)

#### Näytä nimi muokkain

![[_media/EditPreferences-Display-tab-DisplayNameEditor-dialog-example-50-fi.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Näytä nimi muokkain - ikkuna (esimerkki) Menu: "Muokkaa&gt;Asetukset..." - "Näyttö" - lehti]]

Seuraavat avainsanat korvautuvat ao. nimenosilla:

- <b>Etunimi</b> - etunimi (ensimmäinen nimi)
- <b>Titteli</b> - titteli (Tri., Rva.)
- <b>Kutsuma</b> - kutsumanimi
- <b>Nimikirjaimet</b> - Etunimien alkukirjaimet
- <b>Päänimi, Päänimi\[etu\] tai \[suk\] tai \[yle\]</b> - koko päänimi, etuliite, vain sukunimi, liittäjä (espanjalaista nimikäytäntöä)
- <b>Patronyymi, tai \[etu\] tai \[suk\] tai \[yle\]</b> - koko pa/matronyymi sukunimi, etuliite, vain sukunimi, liittäjä (espanjalaista nimikäytäntöä)
- <b>Perhelempinimi</b> - perhelempinimi
- <b>Loputnimet</b> - muut sukunimet kuin ensisijainen
- <b>Rawsukunimet</b>- sukunimet (ilman etuliitteitä ja yhdistesanoja)
- <b>Sukunimi</b> - sukunimet (etuliitteineen ja yhdistesanoineen)
- <b>Jälkiliite</b> - jälkiliite (Jr., Sr.) , suomalaisessa käytännössä myös patronyymi ja matronyymi
- <b>Lempinimi</b> - lempinimi
- <b>Yleisnimi</b> - lempinimi, muuten 1. etunimistä
- <b>Etuliite</b> - kaikki etuliitteet (von, af, de)
- <b>Eipatronyymi</b>- kaikki sukunimet, patsi patro/matro & ensisijainen

Ylimääräiset lainausmerkit ja pilkut poistetaan. Muu teksti näkyy sellaisenaan.

Esimerkki: 'Dr. Edwin Jose von der Smith and Weston Wilson Sr ("Ed") - Underhills'  
<i>Edwin Jose</i> on etunimi, <i>von der</i> on etuliite, <i>Smith</i> ja <i>Weston</i> sukunimiä,  
<i>and</i> yhdistäjä, <i>Wilson</i> patronyyminen eli isänpuoleinen sukunimi, <i>Dr.</i> titteli, <i>Sr</i> jälkiliite, <i>Ed</i> lempinimi,  
<i>Underhills</i> perhelempinimi, <i>Jose</i> kutsumanimi. {{-}}

Lisää, Poista, Muokkaa -painikkeilla voi lisätä, poistaa ja muokata muotoiluja. Muokkaimesta poistutaan Sulje-painikkeella.

#### Paikan muoto muokkain

![[_media/EditPreferences-Display-tab-PlaceFormatEditor-dialog-example-50-fi.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Paikan muoto muokkain - ikkuna (esimerkki) Menu: "Muokkaa&gt;Asetukset..." - "Näytä" - lehti]]

Löytyy lehdelta [Näyttö](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Display) *Paikan muoto* valintana.

Lehdellä ovat paikan näyttämiseen liittyvät asetukset.

- Yksilöllinen nimi paikan muodolle.

- Näytettävät paikkojen nimet.

Hierarkiassa jokaista tasoa vastaa positiivinen kokonaisluku, alkaen "0" valitulle paikalle ja kasvaen "1":llä jokaisesta hierarkian tasosta. Tasoja voi kuvata myös negatiivisilla kokonaisluvuilla, alkaen "-1" ylimmälle tasolle (tavallisesti 'Maa') ja pienentyen "1":llä jokaista alempaa hierarkian tasoa kohti. Lisäksi asutuspaikkaa (Kaupunki, Kylä, Tila tai talo, Rakennus tai torppa) kuvataan kirjaimella "p"; tämä liitetään tasonumeron yhteyteen (esim. p+1 tai p-2).

Näytettävät nimet määritetään pilkkuerotettuina tasovälien listana. Väli voi olla yksittäinen taso tai lähtötason ja päätetason väli, pilkulla erotettuna. Lähtötason on oltava päätetasoa pienempi. Puuttuvan lähtötason oletusarvo on "0" ja puuttuvan päätetason arvo "-1".

- "Ei mitään" (Default), "Numero Katu" or "Katu Numero". Valinnalla koostetaan numero ja katu ilman pilkkuerotinta. Jotta vaihtoehto toimii, katutiedolla on oltava tyyppi "Katu" ja kadunnumeron tyyppiä "Numero".

- (oletuksena tyhjä) kielikoodi kahdella merkillä.

-  (oletuksena valinta pois päältä)

Katso myös:

- [Place Editor dialog](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_2#Place_Editor_dialog)
- [Place Name Editor dialog](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_2#Place_Name_Editor_dialog)

{{-}}

### Teksti

![[_media/EditPreferences-Text-tab-default-50-fi.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menu: "Muokkaa&gt;Asetukset..." - "Teksti" - lehti- oletusarvot]]

Tällä lehdellä on oletusarvot sille, kuinka näytetään puuttuvat tai ykstyiset henkilönimien osat ja muut puuttuvat tietueet.

- syöttökentässä voit määrittää, kuinka näytetään puuttuvat sukunimi. Oletusarvo on **`[Sukunimi puuttuu]`**. Voit vaihtaa sen tilalle esim. \[--\] tai muuta sinulle sopivaa.

- syöttökentässä voit määrittää, kuinka näytetään puuttuvat etunimi. Oletusarvo on **`[Etunimi puuttuu]`**. Voit vaihtaa sen tilalle esim. \[--\] tai muuta sinulle sopivaa.

- Oletusarvo: `[Tietue puuttuu]`

- Default: `[Elossa]`

- Default: `[Elossa]`

- Default: `[Yksityinen tietue]`

{{-}}

### ID muodot

![[_media/EditPreferences-IDFormats-tab-default-50-fi.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menu: "Muokkaa&gt;Asetukset..." - "ID muodot" - lehti- oletusarvot]]

Tällä lehdellä ovat Grampsin ID-tietojen automaattiseen generointiin oletusarvot.

- Oletussääntö henkilön ID:n generoinnille. Oletusarvo: `I%04d`

- Oletussääntö perheen ID:n generoinnille. Oletusarvo: `F%04d`

- Oletussääntö paikan ID:n generoinnille. Oletusarvo: `P%04d`

- Oletussääntö lähteen ID:n generoinnille. Oletusarvo: `S%04d`

- Oletussääntö lainauksen ID:n generoinnille. Oletusarvo: `C%04d`

- Oletussääntö mediatiedoston ID:n generoinnille. Oletusarvo: `O%04d`

- Oletussääntö tapahtuman ID:n generoinnille. Oletusarvo: `E%04d`

- Oletussääntö arkistonID:n generoinnille. Oletusarvo: `R%04d`

- Oletussääntö lisätiedon ID:n generoinnille. Oletusarvo: `N%04d`

Voit käyttää [Reorder Gramps ID](wiki:Gramps_6.0_Wiki_Manual_-_Tools#Reorder_Gramps_ID) työkalua muotojen muuttamiseen. {{-}}

### Päivämäärät

![[_media/EditPreferences-Dates-tab-default-50-fi.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menu: "Muokkaa&gt;Asetukset..." - "Päivämäärät " - lehti- oletusarvot]]

- Oletusarvo: `50`

- Oletusarvo: `50`

- Oletusarvo: `50`

- Oletusarvo: `110`

- Oletusarvo: `20`

- Oletusarvo: `13`

- Oletusarvo: `20`

- Oletusarvo: `<b>%s</b>`

  - Sopivia merkintömuotoja ovat:
    - <b>\<b\>Vahvennettu\</b\></b> (oletusarvo)
    - <big>\<big\>Kasvattaa fonttia\</big\></big>
    - <i>\<i\>Italic\</i\></i>
    - <s>\<s\>Yliviivaus\</s\></s>
    - <sub>\<sub\>Alennettu\</sub\></sub>
    - <sup>\<sup\>Korotettu\</sup\></sup>
    - <small>\<small\>Pienentää fonttia\</small\></small>
    - `<tt>Tasavälinen</tt>`
    - <u>\<u\>Alleviivaus\</u\></u>
      - Esimerkiksi: \<u\>\<b\>%s\</b\>\</u\> näyttää <u><b>Alleviivatun vahvennetun päivämäärän</b></u>.

{{-}}

### Tutkija

![[_media/EditPreferences-Researcher-tab-default-50-fi.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menu: "Muokkaa&gt;Asetukset..." - "Tutkija" - lehti- oledtusarvot]]

. Gramps käyttää tietoja vain korrektin Gedcom-tulostiedoston kirjoittamiseen. GEDCOM-tiedostossa on oltava sen luojan tiedot. Voit tietenkin jättää antamatta nämä tiedot, mutta silloin gedcom-tiedostosi jäävät tältä osin puutteellisiksi.

Syöttökentät ovat (oletusarvoisesti kaikki tyhjiä):

- 

- 

- 

- 

- 

- 

- 

- 

- 

Näitä oletusarvoisia tietoja voi muokata [Edit Database Owner Information](wiki:Gramps_6.0_Wiki_Manual_-_Tools#Edit_Database_Owner_Information) työkalulla. {{-}}

### Varoitukset

![[_media/EditPreferences-Warnings-tab-default-50-fi.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menu: "Muokkaa&gt;Asetukset..." - "Varoitukset" - lehti- oletusarvot]]

Tällä lehdellä määritetään, näytetäänkö eräitä varoituksia.

- Valinta oletusarvoisesti päällä (Katso [Dialog](wiki:Gramps_6.0_Wiki_Manual_-_Error_and_Warning_Reference#Suppress_warning_when_adding_parents_to_a_child))

- Valinta oletusarvoisesti päällä (Katso [Dialog](wiki:Gramps_6.0_Wiki_Manual_-_Error_and_Warning_Reference#Suppress_warning_when_cancelling_with_changed_data))

- Valinta oletusarvoisesti päällä (Katso [Dialog](wiki:Gramps_6.0_Wiki_Manual_-_Error_and_Warning_Reference#Suppress_warning_about_missing_researcher_when_exporting_to_GEDCOM))

- Valinta oletusarvoisesti päällä (Katso [Dialog](wiki:Gramps_6.0_Wiki_Manual_-_Error_and_Warning_Reference#Module_not_loaded_warnings))

Katso [Error and Warning Reference](wiki:Gramps_6.0_Wiki_Manual_-_Error_and_Warning_Reference) sivun esimerkkejä. {{-}}

### Värit

![[_media/EditPreferences-Colors-tab-default-50-fi.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menu: "Muokkaa&gt;Asetukset..." - "Värit " - lehti- oletusarvot]]

Tässä lehdessä asetetaan *Graafisten näkymien laatikoiden ja viivojen värit*

*Palauta oletusvärit* painikkeella voi aina palata turvallisesti perusvalikoimaan värejä, mutta omienkin värien asettaminen onnistuu. Painikkeella *Värijärjestelmä* voi aluksi valita vaaleat ja tummat värit. Edellinen tarjoaa monipuolisen värivalikoiman, jolla erotella graafisessa näkymässä eri statuksella olevien henkilöitä ja parisuhteita.

Seuraaville kohteille voi kullekin erikseen asettaa oman värinsä:

- Elävä mies
- Elävän miehen reunaviiva
- Kuollut mies
- Kuolleen miehen reunaviiva
- Kotihenkilö
- Perhe liitossa
- Perheen reunaviiva
- Perhe eronnut
- Eronneen perheen reunaviiva
- Elävä nainen
- Elävän naisen reunaviiva
- Kuollut nainen
- Kuolleen naisen reunaviiva
- Elossa sukupuoli tuntematon
- Elossa sukup. tuntem. reunaviiva
- Kuollut sukupuoli tuntematon
- Kuollut sukup. tuntem. reunaviiva

Väri asetetaan napsauttamalla kohteen oikealla puolella olevaan *väriruutua*, mikä avaa *Valitse väri* ikkunan, jossa on tarjolla valikoima perusvärejä.

{{-}}

#### Valitse väri ikkuna

![[_media/PickAColor-selector-dialog-50-fi.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Valitse väri" - ikkuna]]

asettamiseen pääsee painikkeesta. Valittu väri kuitataan *Valitse* painikkeella. Värin hexaarvo näkyy *väriruudun* oikealla puolella.

## Muut asetukset

Besides dialog, there are other settings available in Gramps. For various reasons they have been made more readily accessible, as listed below.

### Sarakemuokkain

![[_media/Column-editorFi-41.png|Kuva {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Sarakemuokkain -ikkuna]]

Oletusarvona kategorian näkymälistassa on useimmiten kategorian tietoja useassa sarakkeessa. Sarakkeita voi lisätä ja poistaa näkyvistä käyttämällä valikon kautta löytyvää dialogia tai napsauttamalla työkalupalkin painiketta ja sitten ruksimalla päälle tai pois sarakeruutuja. Muokkaimessa voi muuttaa sarakkeen paikkaa listassa valitsemalla sarake ja raahaamalla se uuteen paikkaan muokkaimessa (\[<http://fi.wikipedia.org/wiki/Copypaste>\| vedä ja raahaa\]). Tehtyäsi haluamasi muutokset napsauta painiketta poistuaksesi muokkaimesta ja nähdäksesi muutokset näkymässä. Muokkainikkuna sulkeutuu painikkeesta.

{{-}}

### Sarakkeiden lajittelu

![[_media/PeopleCategory-PeopleListView-SortedByBirthDateColumn-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Sorted by "Birth Date" column in People(List)View - People Category - example]]

Clicking once sorts in ascending order, clicking again sorts in descending order. The dialog can be used to add, remove and rearrange the displayed columns, or to change the default sorting of the view \[though always ascending\]. {{-}}

### Kotihenilön asettaminen

![[_media/MenuEdit-SetHomePerson-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menu showing <em>Set Home Person</em>]]

To set the Home person, select the People Category and make the desired person active and then choose via the menu .

The Home person is the default person who becomes active when one of the following occurs:

- the Family tree database is opened
- when the toolbar button is clicked
- the Home menu item is selected from either the menu or the right-click context menu in selected views
- the [keybinding](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings#15) is used to return to the **Home Person**.

The toolbar button is available in the People Category, Relationships Category, and Pedigree Category.

- [Setting the Home Person](wiki:Gramps_6.0_Wiki_Manual_-_Navigation#Setting_the_Home_Person)

{{-}}

### Näytön asetukset

Whether the toolbar, the sidebar, or the filter (not available on Pedigree and Relationships Views) are displayed in the main window is adjusted through the View menu.

In the different views clicking the menu will shows for boxes you can click:

- Navigator
- Toolbar
- Sidebar
- Bottombar
- Full Screen

Additionally, depending on the view you are in, other options will be available on .

- Gramplets:
  - Set Columns to 1
  - Set Columns to 2
  - Set Columns to 3
- Relationships:
  - Show Siblings
  - Show Details
- Geography:
  - Time period
  - Layout

All other Views: the [column editor](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Column_Editor).

### Vie näkymä

![[_media/Menubar-FamilyTrees-overview-FamilyTree-Loaded-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menubar - "Family Trees" - overview example showing "Export View" menu entry]]

On most Category List Views, displayed data maybe be exported, choose via the [menu](wiki:Gramps_6.0_Wiki_Manual_-_Navigation#Main_Menus) .

Menu only appears on most Views, if the displayed data can be exported. Gramps will export data on screen according your choice: **CSV** or **Open Document** spreadsheet format. {{-}}

#### Vie näkymä laskentataulukkona

![[_media/ExportViewAsSpreadsheet-CSV-file-dialog-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Export View as Spreadsheet" CSV(default) file-dialog - example]]

Gramps will then display the dialog where after choosing a file location to save to and a name for your file; export data on from the Category List View in one of two spreadsheet formats:

- **CSV** (default)
- **OpenDocument Spreadsheet** - ODS format.

{{-}} ![[_media/ExportViewAsSpreadsheet-ODS-Displayed-in-LibreOfficeCalc-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Example ODS Spreadsheet - Displayed in LibreOffice Calc]]

The example screenshot shows an export to the **OpenDocument Spreadsheet** (ODS format) displayed as a Spreadsheet in Libreoffice Calc.

{{-}}

### Modulaarisuus ja laajennukset

Katso [Plugin Manager](wiki:Gramps_6.0_Wiki_Manual_-_Plugin_Manager) ja [Third-Party Addons](wiki:6.0_Addons). {{-}}

### Muokkaa raportin tulostusmuotoja

![[_media/TextReports-DocumentOptions-section-PlainText-output-settings-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Document Options - tab defaults for Text Reports (Plain Text - output selected) example]]

What does it do? It allows you to change the fonts, font sizes, font color, background color of the text and alignment of paragraphs on the report.

For most report dialogs in the top part are options related that specific report and in the lower part you will see the section.

From the drop down list you can choose an existing custom style. Or to make your own select the button to show the dialog and then select the button to show the dialog.

{{-}}

#### Asiakirjatyylit

![[_media/DocumentStyles-dialog-50FI.png|Kuva. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Asiakirjatyylit - ikkuna]]

ikkunassa, luetellaan raportin *oletus* tyyli ja kaikki luomasi mukautetut tyylit, voit myös muokata tai poistaa luotuja tyylejä. Valitse painike avataksesi ikkunan. {{-}}

#### Tyylimuokkain

valintaikkunassa voit muokata kunkin raportin tyylejä.

Muuta `Uusi tyyli`(oletus) kenttä yksilölliseksi nimeksi, koska se näkyy valintaluettelossa.

Kun mukautetun tyylisi muutokset on viimeistelty, tallenna muutokset valitsemalla painike tai poistu valitsemalla .

{{-}}

##### Tyylimuokkaimen välilehdet

Vasemmalla puolella näet sarakkeen, jossa luetellaan kyseisen raportin valinnaisia osavaihtoehtoja, joita voit muokata. Esimerkiksi näyttää tyyli vaihtoehtoja AHN-Entry, AHN-Generation ja AHN-Title.

Oikealla puolella on kolme välilehteä, jotka liittyvät jokaiseen vasemmassa sarakkeessa lueteltuun tyyliin: {{-}}

###### Kuvaus

![[_media/StyleEditor-dialog-Description-tab-example-50FI.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Description options tab - Document Styles - dialog (default styles for Ahnentafel Report) (Gramps 4.2.0 Windows 7)]]

- : kuvaa, mitä kukin tyyli koskee. Tässä on esimerkiksi Sukupolviraportin (AHN-Entry) käyttämä tyyli.

{{-}}

###### Kirjasinvalinnat

![[_media/StyleEditor-dialog-FontOptions-tab-example-50FI.png|Kuva. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Asiakirjatyylit" (oletustyylit Sukupolviraportille) "Tyylimuokkain" ikkunan "Kirjasinvalinnat välilehdellä.]]

- : Tässä voit määrittää Roman tai Swiss, fontin pt., ja jonkin kuten Lihavoitu, Kursiivi tai Alleviivattu.

{{-}}

###### Kappaleen valinnat

![[_media/StyleEditor-dialog-ParagraphOptions-tab-example-50FI.png|Kuva. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Asiakirjatyylit" (oletustyylit Sukupolviraportille) "Tyylimuokkain" ikkunan "Kappaleen valinnat" välilehdellä.]]

- : Tässä asetetaan tyyliisi , , , and .

{{-}}

## Customizing

Here are some ways that you can customize Gramps.

### Preferences

See [Preferences](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Preferences)

### Language

Gramps has been translated into a number of [languages](wiki:Portal:Translators). Usually Gramps automatically starts in your local language, as chosen for other applications, but sometimes this may not be right for you.

'''

#### Linux

If you want to choose a locale 'variant' for sorting that is not the default variant, then you can start Gramps from the terminal (or console) with a different LC_COLLATE environment. For example, the default sorting (collation) variant for Swedish is "reformed", but you can instead choose "standard" by typing:

`export LC_COLLATE="sv_SE.UTF-8@collation=standard"`  
`python Gramps.py`

#### Mac OS X

For Mac OS X see [Advanced setup](wiki:Mac_OS_X:Application_package#Advanced_setup) for details on how the language is normally chosen, and how to choose a special, non-default setting for the language, the sorting order or the format of such things as day and month names and number separators.

#### MS Windows

### Add Windows OS Menu Item

To make Gramps work in your selected language (See table below for your language code), complete the following:

- Using your mouse right button click on the "GrampsAIOxx 5.x.x" icon on Desktop and from menu choose: Copy.
- Right click anywhere on Desktop and from menu choose: Paste shortcut
- New icon will be created with name: "GrampsAIOxx 5.x.x (2)"
- Right click on that and from menu choose: Properties
- A new window will open, click on first tab called General and change text from "GrampsAIOxx 5.x.x (2)" to something more descriptive like: "GrampsAIO Danish"
  - Click on second tab called Shortcut, change text in first entry called Target from (note path will vary depending on Gramps version used):
    - `"C:\Program Files(xxx)\GrampsAIOxx-5.x.x\grampsw.exe"` to:
    - `%comspec% /c set LANG=da_DK.UTF-8 && start grampsw.exe"`
- Click OK and now when you click on that icon Gramps will start in Danish.

### Change the windows LANG variables

Another option if you want Gramps to always load in say:French Canadian language, you can go to Windows \> System Properties, and add the LANG variable in the user section of the environment variables dialog with the appropriate Value.

The value to add is:

    Name: LANG
    Value: fr_CA.UTF-8

### Language codes

Select from the following table of [languages Gramps](wiki:Portal:Translators) has been translated into:

| Language          | ISO code    | Example | Notes |
|-------------------|-------------|---------|-------|
| Dutch             | nl_BE.UTF-8 |         |       |
| English (British) | en_GB.UTF-8 |         |       |
| Finnish           | fi-UTF-8    |         |       |
| French Canadian   | fr_CA.UTF-8 |         |       |
| Russian           | ru_RU.UTF-8 |         |       |
|                   |             |         |       |

- The language codes are two-letter lowercase ISO language codes (such as "da") as defined by [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes).
- The country codes are two-letter uppercase ISO country codes (such as "BE") as defined by [ISO 3166-1](https://en.wikipedia.org/wiki/ISO_3166-1).

### Advanced manipulation of settings

Beyond the settings in Preferences, you may also wish to explore the advanced settings.

Gramps uses **INI keys** for managing user preferences and program settings these are stored in the file *gramps.ini* under *.gramps* folder in your home or user directory.

The list has following sub-items:

- **behavior**: typical Key names are: betawarn, enable-autobackup, use-tips...
- **database**: related to database settings for the Family Tree.
- **export**: export and import dirs
- **interface**: a lot of keys regarding height and width of the different Views: e.g. event-height: 450, event-ref-height: 585, event-ref-width: 728, event-width: 712...
- **paths**: keys related to recent imported files and dirs
- **preferences**: keys related to preferences: all the common prefixes , todo -colors..
- **researcher**: all information regarding the researcher

Example contents of the `gramps.ini` file:

    ;; Gramps key file
    ;; Automatically created at 2017/12/30 09:54:12

    [behavior]
    ;;addmedia-image-dir=''
    ;;addmedia-relative-path=0
    ;;addons-url='https://raw.githubusercontent.com/gramps-project/addons/master/gramps50'
    ;;autoload=0
    ;;avg-generation-gap=20
    ;;betawarn=0
    ;;check-for-addon-update-types=['new']
    ;;check-for-addon-updates=0
    ;;date-about-range=50
    ;;date-after-range=50
    ;;date-before-range=50
    ...

{{-}}

[Category:Fi:Dokumentaatio](wiki:Category:Fi:Dokumentaatio)
