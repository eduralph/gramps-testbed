---
title: Fi:Gramps 6.0 Wiki-käyttöohje - Työkalut
categories:
- Fi:Dokumentaatio
- Plugins
- Stub
managed: false
source: wiki-scrape
wiki_revid: 122601
wiki_fetched_at: '2026-05-30T18:32:55Z'
lang: fi
---

{{#vardefine:chapter\|12}} {{#vardefine:figure\|0}} ![[_media/MenuOverview-Tools-50-fi.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;&quot; Menubar - Tools Overview]] Tämän luvun aiheena ovat Grampsin tarjoamat .

Gramps voi analysoida eri tavoilla sukututkimusdataa. Yleensä työkalut eivät tuota tuloksia raporttien tai tiedostojen muodossa. Sen sijaan ne näyttävät tulokset välittömästi tietokoneen näytössä. Kuitenkin työkalun ajotuloksia voi tietyissä tilanteissa siirtää myös tiedostoon.

# Työkalut

![[_media/ToolbarIcon-OpenTheToolsDialog-50-fi.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Työkalujen kuvake "Avaa työkalujen ikkuna"]]

Työkaluja valitaan polulla .

Vaihtoehtoisesti voit selata kaikkia työkaluja läpi lyhyine kuvauksineen kuvaketta napsauttamalla, mikä avaa ikkunan. {{-}}

## Työkalun valinta ikkuna

![[_media/ToolSelection-dialog-example-50-fi.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Työkalun valinta - ikkuna - esimerkkinä "Etsi mahdolliset henkilöiden kahdennukset" informaatio]]

The ikkunassa voi selata kaikissa kategorioissa tarjolla olevien työkalujen valikoimaa lyhyine kuvauksineen. Ikkuna avautuu ikonista työkalupalkista. {{-}}

## Analysointi ja tutkimus

Tässä ryhmässä olevilla työkaluilla analysoidaan ja tutkitaan sukupuuta muuttamatta sitä. Gramps tarjoaa tällä hetkellä seuraavat Analysoinnin ja tutkimuksen työkalut:

### <u>Vertaa henkilöiden tapahtumia</u>

![[_media/CompareIndividualEvents-EventComparisonFilterSelection-dialog-default-50-fi.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Vertaa henkilöiden tapahtumia" - "Tapahtumien vertailusuotimen valinta" - ikkuna]]

Työkalu tekee vertailun valitulle henkilöryhmälle.

Voit käyttää tätä työkalua valinnalla , joka avaa ikkunan.

Henkilöryhmä valitaan joko aikaisemmin luoduilla käyttäjäkohtaisilla suotimilla käyttämällä pudotusvalikkoa, jossa oletusarvo on *Koko tietokanta* Tai luomalla painikkeen kautta ikkunassa uusi suodin. Työkalu ajetaan ja tulokset näytetään ikkunassa.

{{-}} ikkunassa voit tarkastella tuloksia tai painikkeelle viedä tulokset laskentalomakkeeseen (ODS muotoiseen). painikkeella suljet raportin. {{-}} ![[_media/CompareIndividualEvents-EventComparisonResults-dialog-expanded-example-50-fi.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;Vertaa henkilöiden tapahtumia&quot; - &quot; vertailutulokset&quot; - ikkuna- laajennettu esimerkki]] {{-}}

## Sukupuun käsittely

Tässä ryhmässä olevilla työkaluilla muutetaan tietokantaa. Niillä enimmäkseen haetaan ja korjataan tiedoissa olevia virheitä. Gramps tarjoaa tällä hetkellä seuraavia työkaluja sukupuun käsittelyyn:

### <u>Muokkaa tietokannan ylläpitäjän tietoja</u>

![[_media/DatabaseOwnerEditor-dialog-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Tietokannan ylläpitäjä" - ikkuna- näyttää hiiren oikealla avautuvan valikon]]

Tämä työkalu muuttaa tutkijan tietoja, ks. [Researcher Information](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Researcher).

Valitse polku . Tämä avaa ikkunan, johon voit syöttää haluamasi tiedot.

- 

- 

- 

- 

- 

- 

- 

- 

- 

Nämä tiedot ovat sukupuukohtaisia ja niitä käytetään tulostettaessa tietoja GEDCOM muodossa.

Hiiren oikealla avautuvassa valikossa on kaksi valintaa:

- \-

- \-

{{-}}

### <u>Etsi tapahtumien kuvauksia</u>

![[_media/ModificationsMade-window-example-50-fi.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Etsi tapahtumien kuvauksia - Muutokset tehty - ikkuna- esimerkki tuloksesta]]

Tapahtumakuvaus muodostetaan tapahtuman tiedoista seuraavalla mallilla:

`{tapahtuman tyyppi} {Sukunimi}, {Etunimi}`

Työkalu käyttää tätä kuvaustapaa, jos tapahtumassa ei ole ennestään kuvausta.

Työkalu löytyy polulla

**Varoitus muokkaushistoriasta** avautuu ensin ja valittavana ovat vaihtoehdot ja .

Kun valintasi on , työkalu käy läpi sukupuusi ja näyttää sinulle tulosikkunan, jossa on lisättyjen tapahtumakuvausten kokonaismäärä. {{-}}

### <u>Etsi tietoja nimistä</u>

Tämä työkalu käy läpi koko sukupuun ja yrittää löytää tittelit ja lempinimet, jotka voisi liittää henkilön -kenttään. Jos liitettäviä tietoja löytyi, nämä tapaukset esitetään taulukkona. Voit sitten päättää, minkä ehdotuksen hyväksyt ja mitä et.

Työkalu löytyy polulla

**Varoitus muokkaushistoriasta** avautuu ensin ja valittavana ovat vaihtoehdot ja .

![[_media/ExtractInformationFromNames-DefaultPrefixAndConnectorSettings-dialog-50-fi.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Etsi tietoja nimistä" työkalun "Etuliitteiden ja liittäjien oletusasetukset" - ikkuna]]

The ikkuna avautuu ja voit siinä muokata seuraavia:

- `de, van, von, di, le, du, dela, della, des, vande, ten, da, af, den, das, dello, del, en, ein, elet, les, lo, los, un, um, una, uno, der, ter, te, die` (default)

- `e, y` (default)

- `de, van` (default)

Lopetettuasi käynnistä työkalu painikkeella. {{-}}

![[_media/ExtractInformationFromNames-NameAndTitleExtractionTool-dialog-example-50-fi.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Etsi tietoja nimistä" työkalun "Etsi nimiä ja titteleitä työkalu" - tulosikkuna]]

Raportin valmistuttua näytetään  - tulosikkuna.

Työkalun käyttötapa ei ole suomalaiselle tutkijalle aivan selvä.

{{-}}

### <u>Extract Place Data from a Place Title</u>

### <u>Etsi mahdolliset henkilöiden kahdennukset</u>

![[_media/FindPossibleDuplicatePeople-dialog-default-50-fi.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Etsi mahdolliset henkilöiden kahdennukset - ikkuna- oletusarvo]]

Tämä työkalu etsii koko sukupuun ja hakee samaa henkilöä mahdollisesti esittäviä tapauksia.

Työkalu löytyy polulla .

ikkuna avautuu ja siinä tehdään seuraavia valintoja:

- : valitse pudotusvalikosta **Matala**(oletusarvo), Normaaali ja Korkea välillä. (Huomaa:Työkalu laskee kahdentumisen mahdollisuuksia desimaalilukuina. Jokainen samanlainen tieto nostaa mahdollisuutta. Jos mahdollisuus on raja-arvoa korkeampi, tapaus raportoidaan. Raja-arvot ovat Matala=0.25, Normaali=1.0 ja Korkea=2.0. Korkealla raja-arvolla tulee todennäköisesti vähemmän osumia.

-  hakemaan mahdollisia kahdennuksia. (valiontaruutu päällä oletusarvona)

Lisäksi käytettävissä on seuraavat painikkeet: tuo sinut tälle sivulle, pysäyttää käsittelyn ja aloittaa tietojen käsittelyn.

Valitse käynnistääksesi työkalun ja tiedot käsitellään kahdessa vaihteessa.

- Vaihe 1: Rakennetaan alkuperäiset listat
- Vaihe 2: Lasketaan mahdolliset kahdennukset

Käsittelystä näytetään tilannepalkki ja riippuu koneestasi ja henkilöiden lukumäärästä käsittely voi kestää jonkin aikaa.

{{-}} ![[_media/FindPossibleDuplicatePeople-PotentialMerges-result-dialog-example-50-fi.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;Mahdolliset sulautukset&quot; tulosikkuna &quot;Löydä mahdolliset henkilöiden kahdennukset&quot; - työkalusta- esimerkki]]

Kun työkalun ajo päättyy tuloslistan ikkuna näytetään seuraavan sarakkein:

- : tästä saat käsityksen henkilöiden samaisuudesta. Mitä korkeampi arvo, sitä todennäköisemmin he ovat yksi ja sama henkilö.

- 

- 

Voit kaksoisnapsauttaa valittua riviä tai valita painikkeen tarkastaaksesi yksityiskohdat.

Lisäksi käytettävissä on kolme painiketta: tuo sinut tälle sivulle, joka sulkee ikkunan ja palaat {man label\|Etsi mahdolliset henkilöiden kahdennukset}} ikkunaan ja painike jolla siirryt ikkunaan. Se on selitetty tarkemmin [Sulauta henkilöt](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_Editing_Data:_Detailed_-_part_3#Merge_People) ikkunassa. Siinä voit valita radiopainikkeella yhden henkilöistä ja sulauttaa mahdollisesti tiedot painikkeella, jos henkilöt ovat mielestäsi samoja.

painikkeella palaat tuloslistan ikkunaan. {{-}}

### <u>Korjaa sukunimien isot alkukirjaimet</u>

Työkalu käy läpi koko sukupuun ja aikoo korjata sukunimissä olevat isoja kirjaimia koskevat virheet.

Korjauksissa pyritään tavanomaiseen käytäntöön: sukunimen ensimmäinen kirjain on iso ja loput kirjaimet pieniä. Tästä säännöstä poikkeavat tapaukset esitetään taulukkona.

Voit sitten päättää, tapahtuuko korjaus ehdotetulla tavalla vai ei.

Työkalu löytyy polusta .

**Varoitus muokkaushistoriasta** näytetään ja voit painikkeella lopettaa työkalun käytön tai edetä työkalun käytössä.

{{-}} ![[_media/FixCapitalizationofFamilyNames-CapitalizationChanges-dialog-results-example-50-fi.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Esimerkki &quot;Fix Capitalization of Family Names&quot; työkalun tuloksista &quot;Ison alkukirjaimen muutokset&quot; - ikkunassa&quot;]]

\- ikkunassa näytetään nimille muutosehdotukset. Ikkunan listassa on sukunimet, joissa Gramps voi itse muuttaa etukirjaimen oikeaksi (tarkistathan että olet samaa mieltä niistä.). In the tuloslistassa ovat seuraavat sarakkeet:

- \- Valintaruuduista hyväksyt tai hylkäät kunkin muutoksen (oletusarvona valinta on päällä)

- \- Nimi sukupuussa olevassa muodossa.

- \- Nimi muutetussa muodossa.

Valitse siis muutettavat nimet valintaruuduilla ja käytä sitten painiketta. painikkeella hylkäät kaikki muutokset. painike avaa ao. henkilön muokkauslehtiön lisätarkastelua ja kohdennettuja muutoksia varten, {{-}}

Voit asentaa myös "[Addon:Fix Capitalization of Given Names](wiki:Addon:Fix_Capitalization_of_Given_Names)" työkalulaajennuksen, joka toimii samoin periaattein etunimien kanssa. {{-}}

### <u>Sulauta lainaukset</u>

Tämä työkalu löytyy polusta .

**Varoitus muutoshistoriasta** näytetään ja pysäyttää työkalun käytön painikkeella tai edetä sen käytössä painikkeella. {{-}} ![[_media/MergeCitations-dialog-default-50-fi.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;Sulauta lainaukset&quot; - ikkuna- oletusarvot]]

Sitten avautuu ikkuna, jonka otsikko on:*Yhteensopivien lainausten lisätiedot ja mediatiedostot kootaan yhteen.*

Seuraavat vaihtoehdot on tarjolla:

- pudotusvalikossa:

  - Sovita yhteen sivun/osan, päivämäärän ja luotettavuustason perusteella
  - **Ohita päivämäärä** (oletusarvo)
  - Ohita luotettavuus
  - Ohita päivämäärä ja luotettavuus

- -  (valintaruutu pois päältä oletusarvoisesti)

{{-}} ![[_media/NumberOfMergesDone-dialog-result-example-50-fi.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;Sulauta&quot; - ikkuna - työkalun tuloksista esimerkki &quot;Tehtyjen sulautusten määrä&quot; ikkuna]]

painikkeella ajat työkalun ja kun se on tehnyt työnsä, se raportoi sulautusten kokonaismäärän ikkunassa. {{-}} Katso myös [Sulauta lainaukset](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_3#Merge_Citations) valinta, joka on käytettävissä Lainaukset-kategorian listanäkymässä {{-}}

### <u>Uudelleen nimeä tapahtumatyyppejä</u>

Tämä työkalu vaihtaa nimettyä tyyppiä olevien tapahtumien tyypin toiseksi.

Työkalu on käytettävissä polulla

**Varoitus muutoshistoriasta** näytetään ensin ja voit painikkeella poistua työkalusta tai edetä painikkeella muuttamisessa.

{{-}} ![[_media/RenameEventTypes-Tool-ChangeEventTypes-dialog-example-50-fi.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;Uudelleen nimeä tapahtumatyyppejä&quot; - ikkuna - esimerkki &quot;Uudelleen nimeä tapahtumatyyppejä&quot; työkalusta]]

ikkuna avautuu:

-   
  syötä tyyppi tekstikenttään tai valitse alkupäinen tapahtuman tyyppi pudotusvalikosta

-   
  syötä tyyppi tekstikenttään (voit luoda tässä täysin uuden tyypinkin) tai valitse uusi tapahtuman tyyppi pudotusvalikosta

Esimerkissä muutetaan **Syntymä** tapahtumatyyppi **Kaste** tapahtumiksi.

{{-}} ![[_media/RenameEventTypes-Tool-ChangeTypes-result-dialog-example-50-fi.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;Muuta tyyppejä&quot; - tulosikkuna - esimerkki &quot;Muuta tapahtumatyyppejä&quot; työkalusta]]

Voit painikkeella lopettaa työkalun käytön. painikkeella ajat työkalun ja kun se on tehnyt työnsä, se raportoi muutettujen tapahtumien kokonaismäärän. {{-}}

Katso myös:

- [Tapahtumatietojen muuttaminen](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_2#Editing_information_about_events)

### <u>Järjestä uudelleen Gramps ID:t</u>

Reorder Gramps ID

Tällä työkalulla järjestellään uudelleen Grampsin primääriobjektien ID:t. Useita vaihtoehtoja on tarjolla.

![[_media/ReorderGrampsIDs-dialog-example-50-fi.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Järjestä uudelleen Gramps ID:t]]

Työkalu on käytettävissä valikosta .

Kohde-sarakkeessa ovat primääriobjektien tyypit. Siitä vasempaan ovat valintaruudut sille, päivitetäänkö ao. tyypin muutokset. Kun valittuna, ao. tyypin id:t järjestellään uudelleen. 'Kohde' sarakeotsikko on itse asiassa painike, jolla asetetaan kaikkien valintaruutujen arvo yhdellä kerralla.

'Nykyinen' sarakkeessa on esimerkki kustakin ID-tyypistä. 'Määrä" sarakkeessa on kunkin tyypin objektien lukumäärä.

"Muotoilu" sarakkeessa muutetaan objektityyppien ID:ien muoto. Huomaa, että muodossa on alkumäärite, '%04d' ja loppumäärite. Määritteistä vähintään toinen on PAKOLLINEN, molemmat voivat olla mukana. Suositus on, että pidät ne suhteellisen lyhyinä. '%04d' määrittää ID:n numeerisen osan pituuden, '4' voidaan muuttaa arvojen '3' (antaa arvojoukon 000-999) ja '9' (000000000-999999999) välillä. Samoja muutoksia voi tehdä valikossa ja sitten valitsemalla **[Fi:Gramps_6.0_Wiki-käyttöohje_-_Asetukset#ID_muodot](wiki:Fi:Gramps_6.0_Wiki-käyttöohje_-_Asetukset#ID_muodot)** lehden. 'Muotoilu' sarakeotsikko on painike, jolla kaikki muodot voidaan asettaa yhdellä kertaa viimeeksi käytettyyn arvoon.

'Muutos" sarakkeessa on valintaruudut kullekin objektityypille. Kun ruutu on valittuna, ao. objektin ID:t päivitetään uusiksi 'Muotoilu' määritteen mukaisesti, jollei myös 'Pidä" ruutu ole valittuna. Jollei jälkimmäistä ole valittuna, tyypin muotoa ei päivitetä, mutta numero-osuus päivitetään. 'Muutos' sarakeotsikko on painike, jolla kaikki valinnat voidaan asettaa yhdellä kertaa päälle tai pois päältä.

'Aloita' kentässä on uudelleen numeroinnin alkuarvo. 'Aloita' sarakeotsikko on painike, jolla kaikki alkuarvot voidaan asettaa yhdellä kertaa alkuarvoon '0" tai viimeisen käytetyn numeron jälkeiseen arvoon.

The 'Jakso' kentässä on muutosarvo, jolla numeroita kasvatetaan, '1' kasvattaa yhdellä, '2' kasvattaa kahdella jne. 'Jakso" sarakeotsikko on painike, jolla muutosarvoa muutetaan arvojen '1', '2', '5' ja '10' välillä.

'Pidä' sarakkeessa on valintaruudut kullekin objektityypille. Jos tämä ruutu ja 'Muutos' ruutu ovat valittuina, ID muoto pidetään ennallaan ja ID:n numero-osuus numeroidaan uudelleen. 'Pidä' sarakeotsikko on painike, jolla kaikki valinnat voidaan asettaa yhdellä kertaa päälle tai pois päältä.

**Varoitus muutoshistoriasta** näytetään ja voit valita joko tai vaihtoehdoista.

'OK'-painikkeesta työkaluajo käynnistyy ja ajon edistymisen palkki näytetään.

Eri objektityyppien ID:t järjestellään seuraavissa vaiheissa: Henkilöiden ID:t, Perheiden ID:t, Tapahtumien ID:t, Mediatiedostojen ID:t, Lähteiden ID:t, Lainausten ID:t, Paikkojen ID;t, Arkistojen ID:t ja lopuksi Lisätietojen ID:t.

Seuraavaksi haetaan käyttämättömät ID:t ja otetaan käyttöön.

Ajon kestäessä työkalu tutkii jokaisen ID:n, onko se käyttäjän muokkaama eli se ei ole edellisen ID-muotomäärityksen tai oletusmuodon mukainen. Näinhän voi olla, jos käyttäjä itse tai kolmas osapuoli on kirjoittanut ID-kenttään omaa tietoaan. Jälkimmäisestä esimerkkinä [GetGOV laajennus](wiki:Addon:GetGOV) tallentaa oman GOV ID -tietonsa Grampsin ID kenttään. Käyttäjän muokkaaman ID:n kohdalla työkalu kysyy käyttäjältä varmistuksen, haluaako hän todella korvata ID:n. Kuittauksessa on antaa myös ohjeen, miten menetellään muiden käyttäjän muokkaamien ID:ien kohdalla.

### <u>Lajittele tapahtumat</u>

Henkilö- ja perhemuokkaimen Tapahtumat-lehtiä ei ole lajiteltu muuhun kuin tapahtumien syöttöjärjestykseen. Syynä siihen, ettei tapahtumia lajitella tapahtumapäivän mukaan, on monesta tapahtumasta mahdollisesti puuttuva aikatieto. Myös tietojen tuonti sukupuuhun voi lisätä tapahtumia ao. lehtien loppuun ilman aikamääreen huomioimista.

Tapahtumien järjestystä voi muuttaa manuaalisesti raahaamalla tai käyttämällä nuolinäppäimiä, Gramps muistaa uuden järjestyksen. Uutta järjestystä käytetään esim. raporteissa.

Lehdellä voi muuttaa tapahtumien järjestystä myös napsauttamalla sarakeotsikkoa. Tällainen muutos ei säily muokkausikkunan sulkemisessa.

Raahaa ja pudota-tekniikka toimii hyvin, kun siirrettäviä tapahtumia on pieni määrä, mutta se ei ole käyttökelpoinen suurissa tapahtumamäärissä. Lajittele tapahtumat-työkalu on tehty juuri tähän tarkoitukseen, koko sukupuun tai siitä suodattamalla valitun osan kaikkien tapahtumien lajitteluun kerralla..

Työkalu löytyy valinnalla .

**Varoitus muokkaushistoriasta** näytetään ja voit joko poistua tai edetä .

{{-}} ![[_media/SortEvents-dialog-ToolOptions-tab-default-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;Lajittelu tapahtumat&quot; - ikkuna - näyttäen &quot;Työkalun valinnat&quot; lehden &quot;Lajittelee tapahtumat&quot; työkalussa]]

Ensimmäisenä valintana ikkunassa rajataan henkilöt, joiden tapahtumiin työkalu vaikuttaa. Perusvaihtoehto on ottaa mukaan sukupuun kaikki henkilöt. Toisekseen valinta voi kohdistua tietyn henkilön esivanhempiin tai jälkeläisiin. Vaihtoehtona on myös käyttäjäkohtaisen henkilösuodattimen käyttö. Vaihtoehtojen jälkeen määritetään, miten lahjittelu tapahtuu. Todennäköisin valinta on aikamääreen mukainen, mutta lajitteluun voidaan ottaa vaikuttavina tekijöinä tapahtumien muitakin ominaisuuksia. Lajittelu voi tapahtua nousevaan tai laskevaan järjestykseen. Edelleen voidaan valita, lajitellaanko myös perhetapahtumat.

{{-}

## Sukupuun korjaus

### <u>Tarkista ja korjaa tietokanta</u>

Työkalu tarkistaa eheysongelmat ja korjaa ne mikäli mahdollista. Työkalu tarkistaa erityisesti:

- Katkenneet perhelinkit. Niissä henkilöstä on linkki perheeseen tähän henkilöön, ja toisinpäinkin.

<!-- -->

- Puuttuvat mediat. Media-tietueesta on linkki mediatiedostoon, jota ei löydy. Näin voi käydä, jos tiedosto on deletoitu, nimetty uudelleen tai siirrytty toiseen paikkaan.

<!-- -->

- Tyhjät perheet. Perhetietueesta ei ole viittausta yhteenkään henkilöön.

<!-- -->

- Puolisoiden suhteet. Tarkistaa kaikista perheistä, ettei isän ja äidin suhteen ole sekaannusta. Puolisoista tarkistetaan myös, että he ovat eri sukupuolta. Jos sukupuoli on sama, suhde nimitetään "Kumppaneiksi".

Työkalua käytetään valinnalla .

**Varoitus muokkaushistoriasta** näytetään ja vaihtoehtosi ovat joko tai .

{{-}} ![[_media/IntegrityCheckResults-dialog-CheckAndRepairDatabase-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;Integrity Check Results&quot; - example result dialog - for the &quot;Check and Repair Database&quot; tool]]

Ongelmat löytyvät automaattisesti ja dialogi näyttää yhteenvedon tehdyistä toimenpiteistä. {{-}} Muuten näet dialogi, joka toteaa *Tietokanta on läpäissyt sisäisen tarkastuksen*. {{-}}

### <u>Rebuild Gender Statistics</u>

![[_media/GenderStatisticsRebuilt-dialog-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Gender statistics rebuilt" - result dialog for "Rebuild Gender Statistics" tool]]

Rebuilds gender statistics for name gender guessing...

You can use this tool via menu .

Once completed the result dialog will be shown. {{-}}

### <u>Rebuild Reference Maps</u>

![[_media/ReferenceMapsRebuilt-dialog-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Reference maps rebuilt" - result dialog for "Rebuild Reference Maps" tool]]

This tool rebuilds reference map tables (*References* items on editors).

You can use this tool via menu .

Once completed the result dialog will be shown. {{-}}

### <u>Rebuild Secondary Indexes</u>

![[_media/SecondaryIndexesRebuilt-dialog-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Secondary indexes rebuilt" - result dialog for "Rebuild Secondary Indexes" tool]]

This tool rebuilds secondary indices.

You can use this tool via menu .

Once completed the result dialog will be shown. {{-}}

### <u>Remove Unused Objects</u>

This tool will search your database for pieces of information which are not connected to anything else, and then allow you to edit and attach the information or remove them.

You can use this tool via menu .

{{-}} ![[_media/UnusedObjects-dialog-example-results-50-fi.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;Unused Objects&quot; - dialog example results for &quot;Remove Unused Objects&quot; tool]]

The dialog is presented.

You can choose from the search option you want to use from the top section of the dialog:

-  (checkbox checked by default)

-  (checkbox checked by default)

-  (checkbox checked by default)

-  (checkbox checked by default)

-  (checkbox checked by default)

-  (checkbox checked by default)

-  (checkbox checked by default)

Select the button to run the report, and once completed the results if any will show in the bottom section of the dialog with the following columns shown:

- Select the row if you want to delete the object (checkbox unchecked by default)

- \- Icon representing the type of object.

- \- Gramps internal name for the object.

- \- of the object.

To examine the object you must double-click on the row and it will show the appropriate editor for the object allowing you to edit if required.

the objects you want to delete either using the individual checkboxes or using the associated buttons:

- 

- 

- 

Once your deletion choices have been made select the button to delete the objects.

When finished you may then use the button to exit the tool. {{-}}

## Apuvälineet

This section contains tools allowing you to perform a simple operation on a portion of data. The results can be saved in your database, but they will not modify your existing data. The following utilities are currently available in Gramps:

- [Find database loop](wiki:Gramps_6.0_Wiki_Manual_-_Tools#Find_database_loop) -
- [Media Manager](wiki:Gramps_6.0_Wiki_Manual_-_Tools#Media_Manager) -
- [Not Related](wiki:Gramps_6.0_Wiki_Manual_-_Tools#Not_Related) -
- [Relationship Calculator](wiki:Gramps_6.0_Wiki_Manual_-_Tools#Relationship_Calculator) -
- [Verify the Data](wiki:Gramps_6.0_Wiki_Manual_-_Tools#Verify_the_Data) -

### <u>Etsi tietokanta silmukka</u>

Find database loop

![[_media/FindDatabaseLoop-dialog-example1-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Find possible loop]]

The utility allows you to verify if you have ancestral loops in the database.

Select this via the menu you will get a window. The window has five tabs; ,, , , .

1.  First Gramps_ID is a reference to the Parent.
2.  Parent (Ancestor on the image) is the person we are looking for a loop.
3.  Second Gramps_ID is a reference to the Child.
4.  Child (Descendant) is the origin of the loop.
5.  Family_ID is a reference to the associated family

{{-}}

![[_media/FindDatabaseLoop-dialog-example2-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Find possible loop in a complex example]]

In the following complex example, we have multiple ancestral loops :

If we look at the second line, we have :

1.  First Gramps_ID : I0002
2.  Parent is : Father, Child2
3.  Second Gramps_ID : I0001
4.  Child is : Father, Father
5.  Family_ID is : F0000

To understand what happens :

1.  we start at \[I0002\] Father, Child2.
2.  We continue with his son \[I0003\] Father, Child3.
3.  We continue with his son : \[I0000\] Child, Child.
4.  We continue with his son : \[I0001\] Father, Father.
5.  We continue with his son : \[I0002\] Father, Child2 ==\> **HERE, we have a ancestral loop**.

{{-}} To read more about ancestral loops see:

- [Finding Ancestral Loops : Modern Software Experience](https://www.tamurajones.net/FindingAncestralLoops.xhtml)
- [Ancestral Loops : Louis Kessler's Behold Blog](http://www.beholdgenealogy.com/blog/?p=1309)

### <u>Media Manager</u>

![[_media/Introduction-page-MediaManager-50-fi.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Introduction - page for "Gramps Media Manager" - Tool wizard]]

The is a group of four separate tools accessed via a wizard like dialog that you can access via the menu which will show the first **Introduction** dialog page with the following information on the tools abilities.

{{-}}

From the **Introduction** page selecting the button (or using the keyboard shortcut ) you will be shown the **Selection** page window.

![[_media/Selection-page-MediaManager-default-50-fi.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Selection - page for "Gramps Media Manager" - Tool wizard - default]]

From the **Selection** page window select from one the four options the actions you want to take and then select the button:

- (default)

- 

- 

- 

{{-}}

#### Replace substrings in the path

![[_media/ReplaceSubstringSettings-page-MediaManager-default-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Replace substring settings - page for "Gramps Media Manager" - Tool wizard - default]]

This tool allows replacing specified substring in the path of media objects with another substring. This can be useful when you move your media files from one directory to another.

Selecting this radio button will bring up a window where you can type in any string in the text field and the text field. At any time you can click on the button or the button. Clicking the button will bring up the window.

{{-}}

#### Convert paths from relative to absolute

![[_media/ConvertPathsFromRelativeToAbsolute-FinalConfirmation-page-MediaManager-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} 'Convert paths from relative to absolute':"Final Confirmation" page for "Gramps Media Manager" - Tool wizard - example]]

This tool allows converting relative media paths to the absolute ones. It does this by prepending the as given in the [Edit &gt; Preferences &gt; General](wiki:Gramps_6.0_Wiki_Manual_-_Settings#General) tab, or if that is not set, it prepends the default [User's Directory](wiki:Gramps_6.0_Wiki_Manual_-_User_Directory). {{-}}

#### Convert paths from absolute to relative

![[_media/ConvertPathsFromAbsoluteToRelative-FinalConfirmation-page-MediaManager-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} 'Convert paths from absolute to relative':"Final Confirmation" page for "Gramps Media Manager" - Tool wizard - example]]

This tool allows converting absolute media paths to a relative path. The relative path is relative viz-a-viz the base path as given in the Preferences, or if that is not set, user's directory. A relative path allows to tie the file location to a base path that can change to your needs. {{-}}

#### Add images not included in database

![[_media/AddImagesNotIncludedInDatabase-FinalConfirmation-page-MediaManager-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} 'Add images not included in database':"Final Confirmation" page for "Gramps Media Manager" - Tool wizard - example]]

Check directories for images not included in database, this tool adds images in directories that are referenced by existing images in the database. You will have to import one media item from each sub directory manually. Media Manager does not include sub-directories automatically. All the directory paths shown in the tool will be searched through. {{-}}

### <u>Ei sukua</u>

![[_media/NotRelatedTo-dialog-NotRelated-Tool-example-50-fi.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}}. "Not related to '...'" - dialog - showing results for "Not Related" Tool]]

Raportissa on henkilöitä, jotka eivät ole sukua valituna olevalle aktiiviselle henkilölle. Työkalu löytyy polusta .

tuottaa valintaikkunan, joka näyttää luettelon kaikista ihmisistä, jotka **EIVÄT** ole sukua valittulle henkilölle.

Luettelo sisältää sarakkeet:

- *Nimi*
- *ID*
- *Vanhemmat*
- *Tagit*

"Nimi" -sarakkeessa voit käyttää -painiketta ja painikkeita laajentamaan tai supistamaan *nimilistan* ryhmittelyä. Henkilön kaksoisnapsauttaminen tuo esiin -valintaikkunan tai -valintaikkunan.

Kun valitset henkilön, voit käyttää -teksti -kenttää (voit täyttää siihen haluamasi mukautetun tagi nimen) tai valita pudotusluettelosta olemassa olevan tagin esim. TODO, Ei sukua. painikkeella lisäät valitun tagin henkilö(i)lle. Joka näkyy sitten *Tagit* -sarakkeessa. {{-}}

### <u>Relationship Calculator</u>

![[_media/RelationshipTo-dialog-RelationshipCalculator-Tool-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Relationship to '...' " - dialog - showing results for "Relationship Calculator" Tool]]

The Relationship Calculator when opened will list all people connected, **but not necessarily related**, to the active person. Select the individual to check if an relationship exist it will be shown in the lower panel. Only blood relationships will display (except for husband-wife relationships). Note "in-law" relationships cannot be displayed.

You can use this tool via menu .

Basically, any two people are related if they have an ancestor in common. One of these individuals may actually be an ancestor of the other - such as a great grandparent. Even in the cases of aunts and uncles, you still can calculate the relationship by searching for the common ancestor. In this case, the father or mother of the aunt or uncle will be a grandparent to the nephew or niece.

Basically, siblings (brothers and sisters) are only one generation down from the common ancestor. Cousins (also called "first" cousins) are two generations down from the common ancestor. "Second" cousins are thus, three generations down from the common ancestor - and so on. But when the two people are in different generations, the relationship becomes an aunt or uncle, if that person is only one generation down from the common ancestor. The reverse of an aunt and uncle is a nephew and niece.

After that, everyone is considered a "cousin", but to indicate that they are not in the same generation we use the word "removed" to indicate the number of generations different between the two. For example, my father's "first" cousin is also my "first" cousin but "once removed" (one generation difference between us). My fathers "first" cousin is my own child's "first cousin twice removed" - two generations different.

A full text list of all blood relations and their spouses can be viewed using a [Kinship Report](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_6#Kinship_Report). {{-}}

### <u>Tarkista tiedot</u>

![[_media/VerifyTheData-DataVerifyTool-dialog-General-tab-defaults-50-fi.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Verify the Data..." - "Data Verify tool" dialog - "General" tab - defaults]]

This utility allows you to verify the database based on the set of criteria specified by you.

For example, you may want to make sure that nobody in your database had children at the age of 98. Based on common sense, such a record would indicate an error. However, it is not a consistency error in the database. Besides, someone might have a child at the age of 98 (although this rarely happens). The Verify tool will display everything that violates your criteria so that you can check whether the record is erroneous or not. The ultimate decision is yours.

Select this via the menu you will get a window. The window has four tabs; , , , . Those tabs show a list with criteria and a input field where you can alter the criteria value. In the lists below I show some *workable* values.

#### Verify the Data tab pages

Select the criteria you want to run the tool with from the following tabs. If you are OK with the criteria click the button (or hit and you will be presented with a window.

Depending on your criteria and your data a list will be shown. Some possibilities of findings are listed below. But there are others.

- Disconnected individuals (ones with no parent or spouse or child or sibling)
- old/dead father
- marriage after death/ before birth
- large year span for all children
- early/late marriage
- young/unborn mother
- husband and wife with the same surname
- same sex marriage/ female husband
- ...

##### General

-   
  90

-   
  17

-   
  50

-   
  3

-   
  30

-   
  99

The first check box: causes the tool to accept a baptism date if a birth date is not known, and to accept a burial date if a death date is not known. In addition, starting in Gramps version 3.3, it also causes the tool to accept "inexact" dates (i.e., any "legal" Gramps date which is not a fully-specified one (with an explicit day and month and year)).

The second check box: will check if the dates are invalid.

##### Women

-   
  17

-   
  48

-   
  12

##### Men

-   
  18

-   
  65

-   
  15

##### Families

-   
  30

-   
  8

-   
  25

{{-}}

#### Data Verification Results window

![[_media/DataVerificationResults-window-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Data Verification Results window.]]

After you run the tool you will be presented with the window.

On the bottom of the window four buttons are available to make a selection easier. Those are , , , and .

Double-clicking on a row will give you a possibility to view and or edit the data.

With the button (or select the keyboard shortcut ) you close the window. {{-}}

#### Examples

Two examples from using real data with this tool:

\*:The warning showed 'female husband': checking the data I found a family with father : Anna Roelants. Luckily in the I read: *The marriage of Adam Roelants and Cornelia Crabbe*. It was clearly a typo: Anna i.s.o. Adam. Without this **Tool** it would be very hard to find.

\*:The warning showed 'late marriage': checking the data: male person °1738 female person °1756 : marriage X 1804 \[Gregorian Calendar\] : Everything seemed to be OK: so they (re)married at the age of 66 and 48 years! The warning showed up because the **General criteria** was set to **60**.

{{-}}

## Debug

![[_media/MenuOverview-Tools-Debug-menu-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "" Menubar - Tools - Debug menu Overview]]

When the python `-O` optimise flag is not turned on, an additional entry appears in the menu.

See [Command Line: Python options](wiki:Gramps_6.0_Wiki_Manual_-_Command_Line#Python_options) {{-}}

### Check Localized Date Displayer and Parser

![[_media/StartDateTest-dialog-CheckLocalizedDateDisplayerAndParser-Tool-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Start date test?" dialog - for "Check Localized Date Displayer and Parser" - Tool]]

This test tool will create many people showing all different date variants as birth. The death date is created by parsing the result of the date displayer for the birth date. This way you can ensure that dates printed can be parsed back in correctly.

{{-}}

### Dump Gender Statistics

![[_media/GenderStatisticsTool-dialog-DumpGenderStatistics-Tool-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Gender Statistics tool" dialog results example - for "Dump Gender Statistics" - Tool]]

Will dump the statistics for the gender guessing from the first name. {{-}}

### Generate Testcases for Persons and Families

![[_media/GenerateTestcases-dialog-GenerateTestcasesForPersonsAndFamilies-Tool-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Generate testcases" dialog - for "Generate Testcases for Persons and Families" - Tool - default]]

The testcase generator will generate some persons and families that have broken links in the database or data that is in conflict to a relation.

The dialog will be shown and you can either or .

{{-}}

### Populate Sources and Citations

![[_media/PopulateSourcesAndCitationsTool-dialog-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Populate sources and citations tool" dialog - default]]

This tool generates sources and citations for each source in order to populate the database for testing with significant numbers of sources and citations.

{{-}}

[Category:Fi:Dokumentaatio](wiki:Category:Fi:Dokumentaatio) [Category:Plugins](wiki:Category:Plugins)
