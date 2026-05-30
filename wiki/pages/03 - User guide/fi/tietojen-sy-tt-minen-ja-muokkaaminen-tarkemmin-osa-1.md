---
title: 'Fi:Gramps 6.0 Wiki-käyttöohje - Tietojen syöttäminen ja muokkaaminen: Tarkemmin
  - osa 1'
categories:
- Fi:Dokumentaatio
- Stub
managed: false
source: wiki-scrape
wiki_revid: 120897
wiki_fetched_at: '2026-05-30T18:30:46Z'
lang: fi
---

{{#vardefine:chapter\|7.1}} {{#vardefine:figure\|0}}

Edellisessa osassa sait lyhyen katsauksen, kuinka Grampsiin syötetään ja siinä muokataan tietoja. Täsä osassa paneudutaan näihin asioihin pajon tarkemmin.

Kuten edellä havaittiin, Gramps tarjoaa joukoittain näkymiä. Niistä jokaisessa voit syöttää ja muokata tietoja. Itse asiassa samaa informaatiota saa usein eri näkymien kautta.

Grampsissa tietoja syötetään ja muokataan dialogi-ikkunoissa. Koska käytämme tätä käsitettä usein, on syytä määritellä se:

Dialogi on ponnahdusikkuna, joka tarjoaa yhden tai useita lomakkeita tietyyn kategoriaan sopivan tiedon syöttämiseen ja muokkaamiseen. Esimerkkeinä Grampsin ja dialogit.

Dialogi on usein "lehtiö", jossa on useita "kielekkeitä" (tabs) tietoen ryhmittelemiseksi. Esim. Muokkaa henkilöä -dialogissa on kielekkeet mm. Tapahtumille, Ominaisuuksille, Osoitteille ja Lisätiedoille.

## Henkilötietojen muokkaus

Katsaus elementteihin

![[_media/Edit-person-window-new-person-example-60.png|Kuva {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Muokkaa henkilöä]]

Henkilön tiedot tallennetaan ja muokataan dialogissa. Sen voi käynnistää eri näkymissä seuraavilla tavoilla:

- [Henkilöt](wiki:Fi:Gramps_6.0_Wiki-käyttöohje_-_Kategoriat#Henkilöt_kategoria) kategoriassa:
  - Kaksoisnapsauta sen henkilön nimeä, jonka tietoja haluat muokata
  - Valitse nimi yhdellä napsautuksella ja napsauta sen jälkeen työkalupalkissa ![[_media/Gramps-notes.png]] (Muokkaa) painiketta.
  - Valitse nimi ja paina **Enter** .
  - Valitse Grampsin Päivitä -valikossa
  - Valitse valikosta, joka avautuu napsauttamalla nimeä oikealla painikkeella.

<!-- -->

- [Suhteet](wiki:Fi:Gramps_6.0_Wiki-käyttöohje_-_Kategoriat#Suhteet_kategoria) kategoriassa: Aktiivisen henkilön tietojen muokkaamiseksi napsauta henkilön nimen vieresäolevaa Muokkaa painiketta.

<!-- -->

- [Kaaviot](wiki:Fi:Gramps_6.0_Wiki-käyttöohje_-_Kategoriat#Kaaviot_kategoria) kategoriassa: Kaksoisnapsauta laatikkoa, jossa on sen henkilön nimi, jota haluat muokata.

Kaikissa edellä olevissa tapauksissa avautuu dialogi.

### Henkilömuokkain

Dialogi-ikkunan yläosassa on kaksi osiota: Perustiedot henkilön ja toinen osio , jossa on Yksityisyys painike tietojen rajoittamiseksi viennissä ja tulosteissa, sukupuolen valitsin ja tunnuksen syöttökenttä. Toisessa osiossa voi lisäksi asettaa henkilön tiedoille tageja.

Yläosion alla on , jonka lehdillä (tabs) on eri tietoryhmiä. Lehden napsautuksella lehti avautuu ja sen sisältö on muokattavissa.

Alhaalla olevasta painikkeesta kaikki muutokset päivittyvät kantaan ja dialogi sulkeutuu. painikkeesta dialogi sulkeutuu ilman muutoksien talletusta. Jos lehtiössä on muutettu jollakin lehdellä jotain tietoa, varoitusikkunassa annetaan seuraavat vaihtoehdot: sulje ilman muutoksien talletusta, peruuta peruuttaminen tai talleta muutokset.

### Ensisijainen nimi osio

![[_media/EditPerson-top-sections-highlighted-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Ensisijainen nimi" osio (kororstettu keltaisella) Henkilömuokkaimessa" - ikkuna - esimerkki]]

Ensisijainen nimi on käytössä Grampsin henkilön "nimenä". Voit määrittää asetuksissa, miten jokin nimi näytetään, ks. [Gramps Preferences](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Display). Useimmiten näet Grampsissa vain ensisijaisen nimen. Vain ykstyiskohtaisissa raporteissa ja Grampsin tuottamassa nettisivustossa näytetään myös muut, vaihtoehtoiset nimet.

Ensisijainen nimi osiossa näytetään tyypilliset henkilön perustamisessa annettavat tiedot henkilön nimestä. Nähdäksesi kaikki talletettavissa olevat tiedot nimestä napsauta painiketta jälkeen. Se avaa [Nimimuokkain](wiki:Fi:Gramps_6.0_Wiki-käyttöohje_-_Tietojen_syöttäminen_ja_muokkaaminen:_Tarkemmin_-_osa_3#Nimimuokkain) dialogin.

Ensisijaisen nimen kentät ovat dialogissa:

- Tällä kentällä erotetaan syntymänimi, avionimi, lempinimi, nimilyhenne jne). Suosittelemme, että ensisijaisena nimenä käytetään asiakirjoista useiimiten löytyvää virallisyhteyksissä käytettyä nimeä ja tallentamaan muut nimityypit lehtiön lehdellä.

- , henkilön etunimi

- , se osa henkilön nimestä, joka osoittaa perheen (suvun) johon henkilö kuuluu

  - Käyttämällä painiketta avautuu ikkuna, jossa **Perhenimi** osiossa käsitellään mm. toisintonimet ja espanjalaiseen nimikäytäntöön kuuluvat isän- ja äidin sukunimiosat sisältävät nimikoosteet

- , valinnainen osa sukunimessä, ei käytetä lajitteluissa; kuten *de* tai *van*

- , valinnainen osa nimessä, kuten *nuorempi* (Johann Strauss nuorempi) tai *III*

  - jälkiliite on suomalaisessa sukututkimuksessa hyvin harvoin tässä käytössä, joten Suomen Sukututkimusseuran Suomi-tietokanta-hankkeessa tähän Gramps-kenttään kirjataan henkilön patro- tai matronyymitieto.

- , henkilön isästä tai muusta esivanhemmasta johdettu nimi ja , joka liitetään viittavaan henkilönimeen, kuten "tohtori" (Tohtori John H. Watson Sherlock Holmes-kirjoissa), valitsin,

- , se etunimistä jota virallisesti käytetään henkilöstä. Esim. henkilöstä etunimiltään *Jean Baptiste Jules* käytettiin vain *Baptiste* etunimeä. Saksassa ja eräissä muissa paikoissa kutsumanimi oli alleviivattuna etunimistä, ks. myös [täällä](wiki:Names_in_Gramps#Call_Name). Jotkut tutkijat käyttävät tätä kenttää myös lempinimen tai muokkaantuneen etunimen (Cristy vs.Cristina) rekisteröintiin, mutta tämä ei ole kutsumanimi-kentän oikeaa käyttöä. Kutsumanimi on käypä laillinen nimi. Luo lempinimet ja muut lyhyet nimimuunnokset vaihtoehtoisena nimenä, eri tyypillä.

<!-- -->

- and kentät tarjoavat "automaattitäydennys" toiminnallisuuden: kirjoitaessasi kenttiin niiden alle ilmestyy valikko, jossa on kaikki sukupuussa olevat tapaukset, jotka vastaavat jo osittainkin antamaasi tietoa. On nopeampaa valita kannasta jo löytyvä kohde hiirellä tai nuolinäppäimillä kuin kirjoittaa pitkäkin teksti kokonaan.

<!-- -->

- on kuvaava nimi, jota käytetään virallisen etunimeen sijasta tai täydentäjänä. on epävirallinen perheen nimi, jolla eriytetään saman sukunimen kantajista henkilöryhmiä. Perheen lempinimi viittaa usein mm. tilan tai maakunnan nimeen.

### Multiple Surnames

![[_media/EditPerson-top-sections-highlighted-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Nimet" osio (korostettu sinisellä) "Henkilömuokkain" - ikkunassa - esimerkki]]

Kun Henkilömuokkaimessa on napautettu painiketta Lisää, uusi ikkuna avautuu.

Jos et syötä mitään tähän ikkunaan, se jää piilotetuksi kun avaat seuraavan kerran Henkilömuokkaimen.

{{-}}

### Yleistä osio

![[_media/EditPerson-General-section-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Yleistä" osio "Henkilömuokkain" - ikkuna - esimerkki]]

- valikossa valitaan henkilön sukupuoli : , ja .

<!-- -->

- Kenttä näyttää Gramps tunnuksen, jolla tunnistetaan henkilö yksikäsitteisesti sukupuussa. Se auttaa erottamaan samannimiset henkilöt. Voit itse syöttää minkä tahansa ainutkertaisen tunnuksen. Jos et itse anna arvoa, valitsee Gramps puolestasi arvon.

<!-- -->

- painikkeella voit merkitä henkilön tiedot yksityisiksi.

<!-- -->

- listalla voit asettaa omia tagejasi ja hyödyntää niitä mm. suodatuksissa.

  - The painike avaa ikkunan, jossa voit poistaa ja lisätä henkilöön tageja.

### Ensisijainen kuva

![[_media/EditPerson-PreferredName-section-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Kuva" osio (korostettu punaisella) "Henkilömuokkain" - ikkunassa - esimerkki]]

Henkilömuokkaimesa on oikeassa yläosassa kuva-alue. alue näyttää henkilöstä löytyvän ensimmäisen kuvan (jos sellainen löytyy).

### Henkilömuokkaimen "lehtiö"

![[_media/EditPerson-Events-tab-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Tapahtumat" lehti "Henkilömuokkain" - ikkunassa - esimerkki]]

Henkilömuokkaimen alaosassa olevat kielekkeistä avautuu otsikkonsa mukaisia lehtiä, joissa on henkilöön liittyviä tietoryhmiä. Kielekkeiden välillä voi siirtyä niiden vasemmalla ja oikealla puolella olevilla nuolipainikkeilla. Kielekkeen otsikon napsautus avaa lehden. Kunkin lehden yläosassa on työkalupainikkeet, joilla voi

- luoda uusia tietoja , muokata ![[_media/Gramps-notes.png]] ja poistaa tietoja (ei kuitenkin Viitteet lehdellä)
- liittää henkilöön eli jakaa tietokannassa jo olevia tietoja (ei kuitenkaan Ominaisuudet, Osoitteet, Internet, Map ja Viitteet -lehdillä)
- muuttaa tietorivien järjestyksen nuolipainikkeilla tai raahaamalla

####  Tapahtumat -lehti

{{-}}

![[_media/EditPerson-EventsTabFi-41.png|Kuva {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Tapahtumat lehti]]

- lehdellä voi katsella ja muokata henkilöön liittyviä tapahtumia. Ensin on listattu **Henkilökohtainen** otsikon alle muut kuin perheisiin liittyvät tapahtumat. Sitten on **perheittäin** perhekohtaiset tapahtumat, ei kuitenkin henkilön lapsuusperheestä.

<!-- -->

- Perheen otsikkorivin tai tapahtumarivin kaksoisnapsautus avaa ao. perhemuokkaimen.

<!-- -->

- painikkeella avautuu tyhjä Tapahtumamuokkain, jolla voi kirjata henkilölle uuden henkilökohtaisen tapahtuman.

##### Valitse tapahtuma

![[_media/SelectEvent-selector-dialog-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Valitse tapahtuma - ikkuna - esimerkki]]

- painikkeella avautuu valintaikkunaan luettelo kaikista tietokannassa olevista tapahtumista. Valintaikkunan kautta niistä valitaan se, joka halutaan liittää käsiteltävään henkilöön erikseen määriteltävällä roolilla (esim. henkilö rekisteröidään kummina jonkun lapsen kastetapahtumaan.)

<!-- -->

- - Tyyppi -pudotusvalikossa voi antaa hakuehdon (0letusarvo Tyyppi sisältää) ja sen vieraan kirjoitetaan hakusana. Haku käynnistetään Etsi-painikkeella. Tuloslistasta valitaan haettu tapahtuma ja vahvistetaan valinta OK-painikkeella.

<!-- -->

- Henkilökohtaisen tapahtuman kaksoisnapsautuksella tai ![[_media/Gramps-notes.png]] (Muokkaa) painikkeella ko. tapahtuma avautuu Tapahtumamuokkaimeen.

{{-}}

#### Nimet -lehti

![[_media/EditPerson-NamesTabFi-41.png|Kuva {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Nimet lehti]]

  
lehdellä voi katsella ja muokata henkilöön liittyviä valinnaisia nimiä. Sivun alaosassa listataan kaikki sellaiset sukupuuhun talletetut valinnaiset nimet. Yläosassa näytetään valittuna olevasta valinnaisesta nimestä tarkemmat tiedot, jos niitä löytyy. , ja painikkeilla voit lisätä, muokata ja poistaa vaihtoehtoisen nimen sukupuusta. Huomaa että ja painikkeet ovat käytettävissä vain, jos listasta on valittu vaihtoehtoinen nimi.

<!-- -->

  
Kun lisäät uuden nimen tai päivität nimeä, dialogi tulee käytettäväksi. Nimimuokkaimen kuvaus, ks. [Name Editor section](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_Editing_Data:_Detailed_-_part_3#Name_Editor)

{{-}}

#### Lähteet ja lainaukset -lehti

![[_media/EditPerson-SourceCitationsTabFi-41.png|Kuva {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Lähteet ja lainaukset lehti]]

  
lehdellä voit katsella ja dokumentoida keräämiäsi lähteitä ja niistä otettuja lainauksia.

<!-- -->

  
Lähteet voivat yleisiä, ja eivät sellaisenaan liity yksittäiseen tapahtumaan, mutta antavat kuitenkin tietoa henkilöstä. Esmerkiksi, jos Martta-tädin muistlmat mainitsevat pojanpojan lapsen Paavon, tutkija voi hällä syyllä olettaa Paavon todella olleen olemassa. Tutkija kirjaa Martta-tädin muistelmat lähteenä, joka oikeuttaa tähän päätelmään.

  
Keskiosassa on listattuna viittaukset kaikkiin sukupuun lähteisiin, jotka liittyvät ao. henkilöön. , ja painikkeilla voit lisätä, muokata ja poistaa lähdeviittauksia henkilöön. Huomaa että ja painikkeet ovat käytettävissä vain, jos listasta on valittu lähdeviittaus.

<!-- -->

  
Muokkauksen yhteydessä voit muuttaa lainauksessa olevia tietoja (ainutkertaisia tälle henkilölle) kuin myös jaettuja lähdekohteita, ks. [Editing Citations](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_Editing_Data:_Detailed_-_part_2#Editing_source_citations).

{{-}}

#### Ominaisuudet -lehti

![[_media/EditPerson-AttributesTabFi-41.png|Kuva {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Ominaisuudet lehti]]

  
voit katsella ja asettaa henkilölle ominaisuuksia. Voit täysin vapaasti määritellä ja käyttää ominaisuuksia. Ominaisuuksia voidaan esimerkiksi asettaa kuvaamaan henkilön fyysisiä tai luonteen piirteitä.

<!-- -->

  
Huomaa että jokainen dialogissa listattu ominaisuus koostuu kahdesta osasta : ominauudesta itsestään ja siihen liitetystä arvosta. Tämä ns. "Parametri-Arvo" parittaminen voi helpottaa sinua tutkimuksesi organisoimisessa ja systematisoinnissa. Jos esimerkiksi määrität "Hiusväri" ominaisuuden henkilölle, "Hiusväri" on sen jälkeen valittavissa kaikkien mudienkin henkilöiden ominaisuudeksi. Henkilölle A Hiusvärin arvo vo olla "punainen", henkilölle B "ruskea" jne. Samalla tavalla voit määrittää ominaisuuden "Puheliaisuus" ja käyttää arvoa "valtava" erityisen puheliaan henkilön kohdalla.

<!-- -->

  
Dialogin alaosassa listataan kaikki sukupuuhun tallennetut ominaisuudet. Listan yläpuolella näytetään valittuna olevasta ominaisuudesta tarkemmat tiedot, jos niitä löytyy. , ja painikkeilla voit lisätä, muokata ja poistaa ominaisuuden sukupuusta. Huomaa että ja painikkeet ovat käytettävissä vain, jos listasta on valittu ominaisuus.

<!-- -->

  
Jos muokkaat ominaisuutta, avautuu [Ominaisuusmuokkain](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_Editing_Data:_Detailed_-_part_3#Attributes) dialogi.

{{-}}

#### Osoitteet -lehti

![[_media/EditPerson-AddressesTabFi-41.png|Kuva {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Osoitteet lehti]]

  
lehdellä voit katsella henkilön eri osoitteita. Suosittelemme, että käytät henkilön asuinpaikan tallentamiseen Asuinpaikka-tapahtumaa. Osoitteet-lehti on Grapsissa tarjolla lähinnä GEDCOM standardin noudattamisen vuoksi, osoitteiden käyttötarkoitus liittyy vain postittamiseen.

<!-- -->

  
Lehdellä on listattuna kaikki sukupuuhun talletetut osoitteet. Lehden alaosassa näytetään valitusta osoitteesta tarkemmat tiedot. , ja painikkeilla voit lisätä, muokata ja poistaa osoitteen sukupuusta. Huomaa että ja painikkeet ovat käytettävissä vain, kun listasta on valittuna osoite.

  
Osoitetta muokataan [Osoitemuokkauksen dialogissa](wiki:Fi:Gramps_6.0_Wiki-käyttöohje_-_Tietojen_syöttäminen_ja_muokkaaminen:_Tarkemmin_-_osa_2#Arkistojen_tietojen_muokkaus) .

<!-- -->

  
Joissakin raporteissa voi rajoittaa elossa olevien henkilöiden tietojen näyttämistä. Erityisesti osoitteet piilotetaan.

{{-}}

#### Lisätiedot -lehti

![[_media/EditPerson-NotesTabFi-41.png|Kuva {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Lisätiedot lehti]]

  
lehdellä voi tallentaa henkilöstä sellaista tietoa, joka ei luontevasti sovi muihin tietojen tallennustapoihin Grampsissa. Lehdellä voi myös lisätä tekstejä, jotka haluat lisätä sukupuuhusi. Lisätiedot on myös linkitetävissä useaan kohteeseen. Lehdellä on tavanomaiset painikekuvakkeet: lisää, valitse nykyinen lisättäväksi, muokkaa valittua, poista ja vaihda lisätietojen järjestystä.

<!-- -->

  
Kun muokkaat lisätietoa, käyttöösi avautuu [Lisätietomuokkain](wiki:Fi:Gramps_6.0_Wiki-käyttöohje_-_Tietojen_syöttäminen_ja_muokkaaminen:_Tarkemmin_-_osa_2#Lis.C3.A4tietomuokkain).

##### Valitse lisätieto

![[_media/SelectNote-selector-dialog-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Valitse lisätieto - ikkuna - esimerkki]]

painikkeella voit avata valintaikkunan ja linkittää jo olemassaolevan lisätiedon. Pudotusvalikosta voit valita suodatusvaihtoehdon ja painikeella suodattaa listan valittavissa olevista lisätiedoista.

**Suodatus vaihtoehdot:**

- **Esikatselu sisältää** (oletus)
- Esikatselu ei sisällä
- ID sisältää
- ID ei sisällä
- Tyyppi sisältää
- Tyyppi ei sisällä
- Tagit sisältää
- Tagit ei sisällä
- Viimeisin muutos sisältää
- Viimeisin muutos ei sisällä

{{-}}

#### Galleria -lehti

![[_media/EditPerson-GalleryTabFi-41.png|Kuva {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Galleria lehti]]

  
lehdellä voit katsella ja tallettaa henkilöön liittyviä valokuvia photos, videoita ja muita mediatiedostoja. Lehden keskiosassa on lista näistä. Kaikista kelvollisista kuvista näytetään esikatselukuva. Muista kohteista kuten äänitteistä, videoista jne näytetään vain tiedostotyypin kuvake.

.

  
, ja painikkeilla voit lisätä kuvan tietokantaan, linkata jo kannasta löytyvään kuvaan, muokata kuvaa ja poistaa medietiedston henkilön galleriasta. Huomaa että ja painikkeet ovat käytettävissä vain kun listalta on valittu mediatiedosto. Silloin avautuu [Mediaviitteiden muokkain](wiki:Fi:Gramps_6.0_Wiki-käyttöohje_-_Tietojen_syöttäminen_ja_muokkaaminen:_Tarkemmin_-_osa_2#Median_viitteiden_muokkaus)

{{-}}

##### Valitse mediatiedosto

![[_media/SelectMediaObject-selector-dialog-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Valitse mediatiedosto - ikkuna - esimerkki]]

The ikkunassa voit linkittää kannassa jo olevaan tiedostoon ja kun se on valittuna, avata sen ikkunassa.

Valittuasi mediatiedoston listalta sen esikatselukuva näytetään ikkunan yläosassa, jos mahdollista.

Ikkunan sarakkeet ovat: Nimike (oletuksena listan lajitteluavain), ID, Tyyppi, Viimeinen muutos.

**Suodatus vaihtoehdot:**

- **Esikatselu sisältää** (oletus)
- Nimike sisältää
- Nimike ei sisällä
- ID sisältää
- ID ei sisällä
- Tyyppi sisältää
- Tyyppi ei sisällä
- Viimeisin muutos sisältää
- Viimeisin muutos ei sisällä

See also [Valitse mediatiedosto valitsin selector](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_2#Select_a_media_object_selector) {{-}}

#### Internet -lehti

![[_media/EditPerson-InternetTabFi-41.png|Kuva {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Internet lehti]]

  
lehti näyttää henkilön kannalta olennaiset nettiosoitteet ja kuvaavan otsikon osoitteelle.. Osoite tallennetaan tavanomaisessa muodossaan, esim. <http://gramps-project.org>, sähköposti, nettisivu, ...

<!-- -->

  
Lehden alaosassa on listattuna nettiosoitteet kuvauksineen. Yläosassa näytetään listassa valitun osoitteen tarkentavia tietoja (jos löytyy). , , ja painikkeilla voit lisätä, muokata ja poistaa nettiosoitteita. "Siiry" painike (jonka kuvakkeessa on vihreä nuoli ja keltainen ympyrä ) avaa selaimesi ja siirtää sinut valitulle sivulle.

Huomaa että ja painikkeet ovat käytettävissä vasta kun listalta on valittu osoite.

##### Internet-osoite muokkain

![[_media/Internet-address-editor-dialog-default_fi-42.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Internet Address Editor]]

voit lisätä uuden Internet-osoitteen tai muuttaa valittua Internet-osoitetta.

- Internet-osoitteen tyyppi: **Tuntematon**(oletus)/Sähköposti/FTP/Netti kotisivu/Nettihaku

  - (lukko) vaihtaa tiedon yksityisyyden tilan.

- Internet-osoite tarvitaan sivun aukaisuun esim: <https://gramps-project.org>

  - painike avaa sivun oletusselaimeen

- Tallennettua internet-osoitetta kuvaava teksti.

Katso myös [Linkki muokkain](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_2#Link_Editor) {{-}} {{-}}

#### Liitokset -lehti

![[_media/EditPerson-AssociationsTabFi-41.png|Kuva {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Liitokset lehti]]

  
lehdellä voit katsella ja päivättää sukupuussa olevien henkilöiden välisiä suhteita. Suhteissa voi olla kummit, perheystävät ja kaikki muutkin suhteet, joita haluat tallentaa. Kummisuhde viittaa kummiin, joka löytyy myös kannasta. GEDCOM standardikin toteaa "A word or phrase that states object 1's relation is object 2". Esimerkkikuvassa Lewis Garnerin kummi on John Adkins. Jos suhde liittyy tiettyyn ajanjaksoon tai tapahtumaan, käytä suhteen sijaan Tapahtumaa. Useita henkilöitä voidaan liittää tapahtumaan ja kukin omassa roolissaan.

{{-}}

##### Henkilöviite muokkain

![[_media/Person-reference-editor-42.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Person Reference Editor]]

{{-}}

###### Valitse henkilö

![[_media/SelectPerson-selector-dialog-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Valitse henkilö" - valintaikkuna - esimerkki]]

{{-}}

#### MAP -lehti

![[_media/EditPerson-LDSTabFi-41.png|Kuva {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} MAP lehti]]

  
lehdellä voidaan katsella ja muokata mormoniuskontokunnan sakramentteihin liittyvää tietoa. Tieto seuraa GEDCOM standardia.

<!-- -->

  
Sakramentteja ovat LDS Baptism, Endowment, ja Sealed to Parents ordinances, kuten näkyy kielekkeissä. Jokainen toimitus kuvataan päivämäärällä, LDS temppelillä ja tapahtumapaikalla.

<!-- -->

  
Sealed to Parents ordinancelle on lisänä pop-up valinta "Parents". Lisäkuvauksia on annettavissa jokaiselle toimenpiteelle Status pop-up valikossa. Myös lisätietoja ja lähdetietoja on lisättävissä ao. ja painikkeilla.

{{-}}

##### MAP toimituksen valinta

![[_media/LDSOrdinanceEditor-dialog-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "MAP toimituksen valinta" - ikkuna - oletus]]

Käytä tai painikkeita avaamaan ikkuna, jossa voit lisätä tai muokata henkilön MAP toimituyksia.

- Katso [Ordinance (Latter Day Saints)](https://en.wikipedia.org/wiki/Ordinance_(Latter_Day_Saints)) Wikipediassa, vapaassa tietosanakirjassa

{{-}}

#### Viitteet -lehti

![[_media/EditPerson-ReferencesTabFi-41.png|Kuva {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Viitteet lehti]]

  
lehden toiminnallisuus dokumentoitava!

{{-}}

## Suhdetietojen muokkaus

Tiedot suhteista talletetaan ja muokataan ikkunassa. Ikkunan saa esille usealla tavalla:

[Suhteet kategoriassa](wiki:Fi:Gramps_6.0_Wiki-käyttöohje_-_Kategoriat#Suhteet_kategoria): napsauta painiketta perheessä, jota haluat muokata.

[Perheet kategoriassa](wiki:Fi:Gramps_6.0_Wiki-käyttöohje_-_Kategoriat#Perheet_kategoria): valitse listasta perhe, napsauta sitten työkalupalkin painiketta tai napsauta kahdesti perhettä.

[Kaaviot kategoriassa](wiki:Fi:Gramps_6.0_Wiki-käyttöohje_-_Kategoriat#Kaaviot_kategoria): osoita hiirellä puolisot yhdistävää mustaa viivaa, napsauta hiiren oikealla ja valitse avautuvasta valikosta tai napsauta kahdesti mustaa viivaa (vakio ja laajennettu tilassa).

Kaikki nämä menetelyt avaavat ikkunan:

{{-}}

### Perhemuokkain ikkuna

![[_media/Edit-family-WindowFi-41.png|Kuva {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Perhemuokkain]]

Ikkunan yläosassa on perheen muodostavasta "pariskunnasta" nimet, syntymä- ja kuolintiedot. Yläosassa on myös painikkeet isän/äidin lisäämiseen ja poistamiseen perheestä sekä molempien muokkaamiseen, sekä kentät perhetunnuksen ja parisuhteen tyypin muokkaamiseen. Myös perheeseen liittyvät tagit on lisättävissä ja muokattavissa täällä.

Pääosan näkymästä vie lehtiö, jonka lehdillä on niiden kielekkeiden nimien mukaisissa ryhmissä perhesuhteisiin liittyvät muut tiedot. Sivulle pääsee napsauttamalla kielekettä. Alimpana ovat ja painikkeet. painikkeesta tallentuvat kaikkien lehtien muutokset ja ikkuna sulkeutuu. painike sulkee ikkunan ilman tietojen tallentamista. Jos tässä tapauksessa oli jollakin lehdellä tallentamatonta tietoa, sovellus kysyy vielä varmistuksen. jatkaa poistumista, peruuttaa sulkemisen ja tallettaa muutokset.

{{-}}

osassa on perustiedot suhteista. kentässä on tunnus, jolla suhde on talletettu kantaan. Anna Grampsin muodostaa tunnukset. Tyypit (kuten Naimaton, Naimisissa jne.) valitaan pudostusvalikosta.

{{-}}

##### Valitse isä/kumppani

![[_media/SelectFather-selector-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Valitse isä/kumppani - valitsin]]

The antaa mahdollisuuden valita jo sukupuussa oleva henkilö isäksi/kumppaniksi. {{-}}

painikkeella aukeavassa ikkunassa voit valita jo olemassa olevan henkilön isäksi/kumppaniksi.

##### Valitse äiti/kumppani

![[_media/SelectMother-selector-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Valitse åiti/kumppani - valitsin]]

The ikkunassa voit valita jo olemassa olevan henkilön äidiksi/kumppaniksi. {{-}}

painikkeella aukeavassa ikkunassa voit valita jo olemassa olevan henkilön äidiksi/kumppaniksi.

{{-}}

### Perheen muokkauslomakkeen lehdet

Lehtiön lehdille on ryhmitetty tiedot suhteesta:

#### Lapset

![[_media/Edit-family-ChildenTabFi-41.png|Kuva {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Lapset lehti]]

  
lehdellä voit katsella ja muokata perheen lapsiasuhteita. painikkeella lisätään uusi henkilö kantaan ja lapseksi tähän perheeseen. painikkeella valitaan kannassa oleva henkilö lapseksi perheeseen. painikkeella muokataan lapsen ja vanhempien suhdetta. painikkeella poistaan henkilön lapsisuhde perheeseen. ja painikkeet ovat käytettävissä vasta kun lapsi on valittu listasta.

Lisäksi

- kolmannen osapuolen laajennuksella [Birth Order Tool](wiki:Addon:BirthOrderTool) voit kerralla lajitella sukupuun kaikki lapset.

{{-}}

{{-}}

##### Valitse lapsi ikkuna

![[_media/SelectChild-selector-dialog-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Valitse lapsi - ikkuna - esimerkki]]

painikkeella avataan ikkuna josta voidaan valita henkilö perheen lapseksi. Lapsen valinta avaa ikkunan. {{-}}

##### Lapsiviite muokkain

![[_media/ChildReferenceEditor-dialog-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Lapsiviite muokkain]]

ikkunan avulla muokkataan valitun lapsen ja vanhempien suhdetta. . Seuraavat vaihtoehdot ovat käytettävissä:

- Lapsen nimi

  - painike.

- (**Syntymä**(oletus)) pudotusvalikosta valitaan mahdolliset suhde vaihtoehdot.

  - Adoptoitu
  - **Syntymä**(oletus)
  - Kasvattilapsi
  - Ei mitään
  - Kummilapsi
  - Lapsipuoli
  - Tuntematon

- (**Syntymä**(oletus)) pudotusvalikosta valitaan mahdolliset suhde vaihtoehdot, jotka samat kuin isällä.

- yksityisyyden valinta lapsen kuulumisesta perheeseen.

{{-}}

Myös seuraavat välilehdet ovat käytettävissä.

###### Lähde Lainaukset

![[_media/Edit-family-SourceCitationsTabFi-41.png|Kuva {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Lähdelainaukset lehti]]

  
lehdellä voit katsella ja muokata listaa viittauksista lähteisiin, jotka todentavat suhteita. Ne saattavat olla myös epävirallisia näyttöjä, ei virallisia dokumentteja. Esimerkiksi jos Maija-tädin muistelmissa mainitaan hänen pojanpoikansa pojan Paavon avioituneen, sukututkija voi pitää tätä näyttönä Paavon aviosuhteesta ja mainita tädin muistelmat tämän johtopäätöksen lähteeksi.

painikkeella lisätään uusi lähdelainaus tähän perheeseen. painikkeella valitaan kannassa oleva lähdelainaus. painikkeella muokataan lähdelainausta. painikkeella poistaan lähdelainaus kannasta. ja painikkeet ovat käytettävissä vasta, kun tapahtuma on valittu listasta.

{{-}}

###### Lisätiedot

![[_media/Edit-family-NotesTabFi-41.png|Kuva {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Lisätiedot lehti]]

  
lehdellä voi katsella ja kirjata perhesuhteisiin liittyviä lisäetoja,kun ne eivät sovellu ominaisuuksien tarjoamaan "parametri-arvo" tyyppiseen tallentamiseen. Lisätiedot on normaali tekstinsyöttöalue..

valinnalla voit määrittää, mite teksti näkyy raporteissa ja nettisivuilla. Jos valitset "Siirretty" , generoituun tekstiin on vaihdettu yksi ainoa välilyönti usean välilyönnin sijaan ja vain yksi rivinpäättymismerkki. Yksi tyhjä välirivi tulkitaan kappaleen vaihdoksi, useammat tyhjät rivit ohitetan.

Jos valitset "Muotoiltu"vaihtoehdon, teksti näkyy raporteissa ja nettisivuilla juuri siinä muodossa kuin se näkyy dialogissa.

{{-}}

###### Tapahtumat

![[_media/Edit-family-EventsTabFi-41.png|Kuva {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Tapahtumat lehti]]

  
lehdellä voit katsella ja muokata perheeseen liittyviä tapahtumia. painikkeella lisätään uusi tapahtuma kantaan ja tähän perheeseen. painikkeella valitaan kannassa oleva henkilö lapseksi perheeseen. painikkeella muokataan lapsen ja vanhempien suhdetta. painikkeella poistaan tapahtuma kannasta. ja painikkeet ovat käytettävissä vasta, kun tapahtuma on valittu listasta.

{{-}}

###### Ominaisuudet

![[_media/Edit-family-AttibutesTabFi-41.png|Kuva {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Ominaisuudet lehti]]

  
lehdellä voit katsella ja muokata perheeseen liittyviä ominaisuuksina tallettavia tietoja. painikkeella lisätään uusi ominaisuus kantaan ja tähän perheeseen. painikkeella valitaan kannassa oleva ominaisuus perheeseen. painikkeella muokataan ominaisuutta. painikkeella poistaan ominaisuus kannasta. ja painikkeet ovat käytettävissä vasta, kun tapahtuma on valittu listasta.

{{-}}

- Galleria

![[_media/Edit-family-GalleryTabFi-41.png|Kuva {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Galleria lehti]]

  
kielekkeessä voit tallentaa ja katsella valokuvia ja muita mediatiedostoja, jotka liittyvät suhteeseen. Ikkunan keskeisessä osassa listataan ne kaikki ja kuvatiedostojen pikakuvat. Muista tidostoista kuten äänitteistä ja videoista näytetään vain Grampsin oletuskuvake. , , ja painikkeilla lisäät uuden kuvan, lisäät viitteen nykyiseen kuvaan, muokkaat kuvaa ja poistat viitteen mediatiedostoon. ja painikkeet ovat käytettävissä vasta, kun tapahtuma on valittu listasta..

{{-}}

#### MAP sakramentti muokkain

![[_media/Edit-family-LDSTabFi-41.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} MAP lehti]]

  
The (Latter Days Saints) lehdellä on informaatiota MAP kirkon **Sealed to Spouse** toimenpiteestä. Tietoja on päivämäärä, MAP temppeli ja Paikka date, LDS temple, and Place. Toimenpiteen tilalle voidaan antaa arvoja **Status** pop-up valikossa. Myös Lähteet...''' ja painikkeet on käytettävissä.

To edit source data, switch to the Sources View and select the desired entry in the list of sources. Double-click that entry or click the icon on the toolbar to invoke the following The main part of the window displays four notebook tabs containing different categories of information. Click a tab to view or edit its contents. The bottom part of the window has and buttons. Clicking will apply all the changes made in all tabs and close the dialog window. Clicking the button will close the window without applying any changes.

{{-}}

## Päivämäärien muokkaus

![[_media/DateSelection-dialog-defaults-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}}  - ikkuna - oletus]]

Kuvassa olevat säännöt riittävät tavallisimpiin päivämäärän tarpeisiin, mutta ikkuna on käyttökelpoinen, kun päivämäärä on monimutkainen tai pelkästään sen tarkistamiseen, että päiväys syötettiin Grampsin kannalta oikeassa muodossa. Ikkunassa voi valita myös käytettävän kalenterin. Tosin Suomessa oletuskalenteri "Gregoriaaninen" on lähes aina oikea.

- **Gregorian**(default)
- Julian
- Hebrew
- French Republican
- Persian
- Islamic
- Swedish

Tässä osiossa kuvataan päivämäärien tallentaminen ja muokkaaminen. Päivämäärät ovat niin tärkeitä sukututkimuksessa, että Gramps näkee erityistä vaivaa säilyttääkseen ja hyödyntääkseen kaikkea saatavilla olevaa päivämäärätietoa.

Tieto voidaan syöttää päivämääräkenttään tai käynnistämällä dialogin. Molempia menettelyitä kuvataan alla, mutta ensin käydään läpi joitain tärkeitä päivämäärien ominaisuuksia Grampsissa.

**Päivämäärätyypit**

Päivämäärät on Grampsissa luokiteltu seuraaviin tyyppeihin:

- Tavanomainen: Tavanomaisessa (regular) päivämäärässä on määritelty päivä. kuukausi vuosi. Se voi olla täydellinen (esim englanniksi June 6, 1990 tai suomeksi 6.6.1990, 6. kesäkuuta 1990 tai osittainen July 1977 suomeksi heinäkuussa 1977.

<!-- -->

- Ennen: Ennen "before" päiväys todentaa tapahtuman tapahtuneen ennen tiettyä päivämäärää (täydellistä tai osittaista).

<!-- -->

- Jälkeen : Jälkeen "after" päiväys todentaa tapahtuman tapahtuneen tietyn päivämäärän (täydellisen tai osittaisen) jälkeen.

<!-- -->

- Aikavälillä: "range" kuvaa aikavälin, jolloin tapahtuma tapahtui.

Esim. "between January 1932 and March 1932." , suomeksi "tammikuun 1932 ja maaliskuun 1932 välillä"

- Ajanjaksona: "span" kuvaa aikajakson, jolloin tietty olotila oli voimassa.

Esim. "from May 12, 2000 to February 2, 2002." , suomeksi "12. maaliskuuta 2000 - 2. helmikuuta 2002".

**Päivämäärän muodot ja parserointi**

Päivämäärät voi siis syöttää Grampsiin eri muodoissa. Numeerinen oletusmuoto määräytyy tietokoneen maa-asetuksista; DD.MM.YYYY on käytössä laajasti Euroopassa, MM/DD/YYYY Yhdysvalloissa jne.

Tavanomaisten päivämäärien lisäksi Gramps tunnistaa muitakin ilmauksia: ennen, jälkeen, noin, välillä ja kestäen. Se ymmärtää myös laadun: arvioitu tai laskettu. Se tukee siis myös osittaisia päivämääriä ja vaihtoehtoisia ajanlaskujärjestelmiä eli kalentereita. Alempana on lista päiväyksien syöttämissäännöistä, joilla onnistuu tarkka päivämäärien parserointi.

Tavanomaiset päiväykset kirjoitetaan suurin piirtein kuten kirjoittaisit ne auki:

- Englanniksi: May 24, 1961 or January 1, 2004.
- Suomeksi kelpaavat muodot 24.6.0991, 24 touko 1991, 24 toukokuuta 1991, 24. toukokuuta 1991, touko 24 1991 ja toukokuu 24 1991.

Muut kuin tavanomaiset päiväykset alkavat laatumääritteellä:

- Englanniksi or . Example: est. 1961, or calc 2005.
- Suomeksi tai

Huomaa, että määritettä ei tarvita tavanomaisissa päiväyksissä.

Mahdollisen laadun jälkeen annetaan tyyppimäärite:

- Englanniksi: If the type is , , or , you scan specify the type by writing "before", "after" or "about". If the type is a range, write "between DATE and DATE", and if the type is a span, write "from DATE to DATE". patterns, where DATE is a single date.
- Examples: est from 2001 to 2003, before June 1975, est about 2000, calc between May 1900 and January 1, 1990.

<!-- -->

- Suomeksi toimitaan: Jos tyyppi on , tai voit määrittää tyypin kirjoittamalla "ennen", "jälkeen" tai "noin".
- Esimerkkejä: ennen 1996, 1870 jälkeen
- Jos tyyppi on aikaväli, kirjoita "päiväys1 ja päiväys2 välillä", ja jos tyyppi jakso, kirjoita "päiväys1 - päiväys2".

Osittaiset päiväykset kirjoitetaan jättämällä yksinkertaisesti pois tuntematon tieto (esim. kun päivää ei tiedetä, 3.1995 talletetaan 3.1995 tiedoksi. Samaten 6.0961 - 2004 kelpaa.)

**Kalenterit**

Grampsin oletus on gregoriaaninen kalenteri, joka on käytössä Suomessakin. Tällä hetkellä Gramps tukee vaihtoehtoisina kalentereina: Julian, Hebrew, French Republican, Julian, Islamic, Persian ja Swedish alternate calendars. Jos haluat ilmoittaa päivämäärän olevan jostain vaihtoehtoisesta kalenterista, lisää kalenterin nimi tekstimuotoisen päiväyksen perään, esim. "January 9, 1905 (julian)".

**Ruotsalainen kalenteri**

[Ruotsin kuningas](wiki:Swedish_kings) Karl XII päätti Ruotsin siirtyvän gregoriaaniseen kalenteriin. Siirtyminen suunniteltiin tapahtuvan vaiheittain 11 karkauspäiällä alkaen 29.2.1700 ja päättyen 1744. Näin päivää 28.2.1700 seurasi 1.3.1700. Näin toimittiin Suuren pohjansodan aikana ja karkauspäiviä pidettiin 1704 ja 1708. Tammikuussa 1711 sama kuningas päätti, että Ruotsi palaa juliaaniseen kalenteriin 1.3.1712. Jotta vaiheistus ei mennyt sekaisin, lisättiin ylimääräinen päivä 30.2.1712. Tähän päättyi ruotsalainen kalenteri. Ruotsi siirtyi gregoriaaniseen kalenteriin 1.3.1753 jättämällä väliin 18.2.1752-02-18 ja 28.2.1753 väliset päivät.

Voit syöttää ruotsalaisen kalenterin mukaisia päivämääriä vain jaksolle 1.3.1700 - 30.2.1712. Tämän kalenterin ollessa päällä muut päivämäärät merkitään epäkelvoiksi ja ne on korjattava.

**Rinnakkaiset päivämäärät**

Suomentamatta, koska koskevat vain vanhaa Englantia ja Amerikan siirtokuntia.

Dual-dated dates (also called "double dating", "slash dates", and sometimes "Old Style/New Style" dates) appear like "Jan 23, 1735/6". Often mistaken as a year uncertainty, this actually has a specific historic meaning. The dual dated date represents a time when an area was in a transition between moving to January 1 as the beginning of the new year. Thus Jan 23, 1735/6 is an indication to make it clear what date is being referred to. In this example, "Jan 23, 1736" might have occurred after "Jun 23, 1736".

England and the American colonies didn't officially accept the "Jan 1" as the new year date until 1752. Before 1752, the English government still officially observed March 25 as the first of the year, whereas most of the English population observed January 1 as the first of the year. Many people therefore wrote dates falling between January 1 and March 25 in the dual-dated format.

Sometimes, a dual date may appear as a fraction, as in this grave stone (170 and 3/4, which means 1703 and 1704):

![[_media/Gravestone.jpg|Kuva {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Hautakivi]]

{{-}}

Marking a date as dual dated can be done by simply putting a slash between the years. For example:

- 1721/2
- 1719/20
- 1799/800

These slash-years can appear anywhere in a date that a regular year can appear.

Dual-dated dates are currently represented in the Julian calendar so their month and day will be the same as that in the textual representation.

**Uudenvuoden juhlapäivä**

With dual-dated dates (and other dates) you may know that the new year was celebrated on a day other than January 1. To indicate this in Gramps, put the month/day code in parentheses, after the calendar (if one). For example:

- Jan 20, 1865 (Mar25)
- Jan 20, 1750 (Julian,Mar1)
- Feb 23, 1710/1 (Mar25)

To indicate the beginning of a year that is different from that of January 1, you use the following codes:

- Jan1
- Mar1
- Mar25
- Sep1

You can put that as the only item in parenthesis, or right after a calendar name (comma, and no space).

Note that if new year's day is not Jan 1, then January will come after December that year. Dates with new year day codes will be sorted appropriately.

{{-}}

### Päivämäärän kelvollisuuden osoittimet

![[_media/DateSelection-dialogFi-41.png|Kuva {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Päiväyksen valinta dialog]]

Gramps tarkistaa päivämäärät.

Vaikka osittaiset päiväykset eivät täysin määritä päivämäärää, ne sallivat ainakin jonkun tyyppisiä päiväysvertailuita.

Punainen ruksi päivämäärän vieressä osoittaa, että sitä ei ole hyväksytty kelvolliseksi päivämääräksi (esim. ("juhannus 1930") tai "Helsingin olympiavuonna". Täsätapauksessa päiväys talletetaan tekstinä eikä se siten ole käytettävissä päivämäärien vertailuissa. Onkin parasta välttää sellaisten päiväystietojen syöttämistä. Olisikin parempi syöttää ensin "joulukuu 1961" ja sitten sen lisätiedoksi "jouluviikolla 1961".

näyttää oletusarvoisesti kelpaamattoman päiväyksen "vahvennettuna". Tyylin voi muuttaa, ks. [Preferences](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Dates).

{{-}}

### Päivämäärien syöttö graafisessa käyttöliittymässä

Yllä selvitetyt ksäittelysäännöt riittävät useimpiin tavallisiin päiväyksiin, mutta voit käyttää myös dialogia. Siitä on hyötyä erityisesti monimutkaisten päivämäärien rakentamisessa siten, että Grams ymmärtää tarkoituksesi. dialogin saa käyttöön napsauttamalla päivämäärän vieressä olevaa painiketta.

valikossa voit valita oletuksena olevan gregoriaanisen kalenterin sijaan toisen kalenterin. valikossa voit valita vaihtoehdoista Tavanomainen, Arvioitu ja Laskettu. The valikossa voit määrittää päiväyksen tarkan tyypin: Tavanomainen, ennen, jälkeen, noin, väli, jakso ja tekstinä. rakennetaan asettamalla päivä, kuukausi ja vuosi. Jos tyyppi on väli tai jakso, tulee näkyviin. Viimeisenä vaihtoehtona anta tallettaa vapaamuotoisen tekstitiedon päivämäärän kanssa.

{{-}}

[Category:Fi:Dokumentaatio](wiki:Category:Fi:Dokumentaatio)
