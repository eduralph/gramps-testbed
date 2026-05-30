---
title: Fi:Gramps 6.0 Wiki-käyttöohje - CSV vienti ja tuonti
categories:
- Fi:Dokumentaatio
managed: false
source: wiki-scrape
wiki_revid: 120644
wiki_fetched_at: '2026-05-30T18:15:54Z'
lang: fi
---

# Gramps laskentalomake vienti ja tuonti

Tässä muodossa voit tuoda kerralla laskentalomakkeella olevat tiedot. Laskentalomakkeen täytyy olla luetteloerotin (CSV) muodossa. Useimmat laskentalomakeohjelmat kirjoittavat ja lukevat tätä. Sitä on helppo kirjoittaa myös manuaalisesti. Tämä on ainoa Grampsin tukema muoto, jolla voi yhdistää tietoja sukupuussa jo oleviin tietoihin.

Tällä muodolla on kolme pääkäyttöä:

1.  Viet Grampsistä keskeiset tietosi laskentalomakemuodolla, muokkaat tietoja laskentalomakeohjelmassa ja tuot muutokset ja lisäykset takaisin Grampsiin. Tämä on kätevää, kun lähetät tietoja toiselle niiden täydentämiseksi tai kun olet itse liikkeellä niin, että sinulla ei silloin ole käytössäsi Gramps-ohjelmaa.
2.  Tuot uusia tietoja Grampsiin sukupuuhusi. Voit esim. lisätä isomman joukon henkilöitä Grampsiin tutkimatta laajemmin heidän elinkaartaan. Laskentalomakkeella heidät voi lisätä nopeasti kerralla sukupuuhun. Erityisen kätevää on luettelomuotoisten tietojen kopiointi muista sovelluksista tai netistä löytyvistä sivuista.
3.  Tuot korjauksa ja lisäyksiä. Sanokaamme että tulostat raportin ja merkitset siihen muutoksesi. Kun teet mutoksista oman "osion" laskentalomakkeelle, ne on tuotavissa kerralla siitä sukupuuhun.

## Vienti

Viedäksesi sukupuusi:

1.  Käynnistä Gramps
2.  Valitse "Vienti" Sukupuut-valikosta
3.  Valitse "Pilkuilla eroteltu taulukkomuotoinen tekstitiedosto (CSV)"
4.  Valitse tiedot jotka viedään (henkilöt, avioliitot, perheet ja/tai paikat)

Valikoitu joukko sukupuusi kenttia tallentuu .csv tiedostoon edellä kuvatussa muodossa. Lisäksi henkilöihin ja perheisiin lisätyt viitteet mahdollistavat muokattujen tietojen palautuksen siten, että sukupuu päivittyy.

Jotkut sarakkeet ovat tyhjiä, erityisesti lisätiedot ja lähteet. Ne ovat laskentalomakkeella mukana, jotta voit tehdä niihin muistiinpanoja, mutta niitä ei koskaan tuoda Grampsiin tällä työkalulla. **Gramps 3.3 versiosta eteenpäin kuitenkin lähteiden nimikkeet viedään mukaan.**

Tietosi jaetaan neljään osioon; henkilöihin, avioliittoihin, lapsiin ja paikkoihin. Vietävien kenttien ja sarakkeiden nimet ovat:

Henkilöt  
Person, Lastname, Firstname, Callname, Suffix, Prefix, Title, Gender, Birthdate, Birthplace (tai Birthplaceid), Birthsource, Baptismdate, Baptismplace (tai Baptismplaceid), Baptismsource, Deathdate, Deathplace (tai Deathplaceid), Deathsource, Burialdate, Burialplace (tai Burialplaceid), Burialsource, Note

<!-- -->

Avioliitot  
Marriage, Husband, Wife, Date, Place (or Placeid), Source, Note

<!-- -->

Perheet  
Family, Child

<!-- -->

Paikat  
Place, Title, Name, Type, Latitude, Longitude, Code, Enclosed_by, Date

Kunkin osion 1. sarake on Grampsin ID tunnus. Sillä liitetään muokkauksesi korjattaviin tietoihin sukupuussa, joten älä muuta tämän sarakkeen tietoja. Lataa tama tiedosto laskentalomakeohjelmaasi käyttäen pilkulla erotettua, tuplalainausmerkeillä ympäröityä tekstimuotoa. Sitten voit lisätä ja muokata tietojasi ja tallentaa ne takaisin samassa muodossa. Lopuksi tuot tiedot korjaamaan sukupuutasi.

.

## Tuonti

Tietojen tuomiseksi:

1.  käytä edellä olevaa tiedostoa tai luo alla kuvattavalla tavalla laskentalomake sukututkimustiedoillesi
2.  käynnistä Gramps
3.  tuo tiedosto auki olevaan sukupuuhusi

Yhdistely vain lisää tai päivittää sukupuutasi. Yhdistely olettaa, että lasketalomakkeesi on oikeaa versiota.

Jos lataat lomakkeen Open/Libre Officeen, varmista että sarakkeiden tyyppi on **text** eikä **standart**. Standard muotoilee uusiksi päivämääräsi ja numerosi. Myös Excelissä on parempi valita kaikki solut kerralla ja muuttaa niiden muodoksi **Text**.

Lomake koostuu sarakkeista. Sarakeotsikko kertoo sarakkeessa olevan tiedon tyypin. Vain etukäteen määritetyt otsikot ovat sallittuja. Tällä hetkellä ne ovat:

### Henkilöt

    person -  viitettä käytetään myös avioissa ja lapsissa 
    grampsid - henkilöön liitetty gramps id tunnus
    firstname - henkilön etunimi
    surname/lastname - henkilön sukunimi
    callname - henkilön lempinimi (nickname)
    prefix - sukunimen etuliite (von, de, etc)
    suffix - a henkilön nimen jälkiliite (Jr., Sr.)
    title - henkilön titteli (Dr., Mr.)
    gender - mies tai nainen (käytä suomenkielisiä, jos Grampsisi on suomenkielinen, muuten ''male'' tai ''female'')
    note - henkilöön liittyvät lisätiedot

    birthdate - syntymäpäivä
    birthplace - syntymäpaikka
    birthplaceid - syntymäpaikan ID
    birthsource - syntymän lähteen otsikko

    baptismdate - kastepäivä
    baptismplace - kastepaikka
    baptismplaceid - kastepaikan ID
    baptismsource - kasteen lähteen otsikko

    deathdate - kuolinpäivä
    deathplace - kuolinpaikka
    deathplaceid - kuolinpaikan ID
    deathsource - kuoleman lähteen otsikko
    deathcause - kuolinsyy

    burialdate - hautauspäivä
    burialplace - hautauspaikka
    burialplaceid - hautauspaikan ID
    burialsource - hautauksen lähteen otsikko

    occupationdate - ammatin päivä
    occupationplace - ammatin paikka
    occupationplace_id - ammatin paikan id
    occupationsource - ammatin lähteen otsikko
    occupationdescr - ammatin kuvaus (nimi)

    residencedate - asuinpaikan päivä
    residenceplace - asuinpaikan paikka
    residenceplace_id - asuinpaikan paikan id
    residencesource - asuinpaikan lähteen otsikko

    attributetype - ominaisuuden tyyppi
    attributevalue - ominaisuuden arvo
    attributesource - ominaisuuden lähteen otsikko

### Aviot

    marriage - jos haluat viitata tähän perheestä, tarvitsen vastaavan nimen tässä
    husband/father/parent1 - viite yllä olevaan henkilöön, joka on aviomies 
                             (naispuoliselle parent1 henkilölle on annettava sukupuoli henkilön tiedoissa tai päivitettävä se myöhemmin Grampsissä)
    wife/mother/parent2 - viite yllä olevaan henkilöön, joka on vaimo 
                             (miespuoliselle parent2 henkilölle on annettava sukupuoli henkilön tiedoissa tai päivitettävä se myöhemmin Grampsissä )
    date - vihkipäivä
    place - vihkipaikka
    placeid - vihkipaikan ID
    source - vihkimisen lähteen nimike
    note - lisätietoja vihkimisestä tai avioliitosta

### Perheet

    family - viite joka sitoo tämän perheen edellä kuvattuun avioliittoon (pakollinen)
    child - viite yllä olevaan henkilöön joka on lapsi
    source - avioliiton lähteen nimike
    note - lisätiedot perheestä
    gender - mies tai nainen (käytetään oman kielen mukaisia sanoja) 
             [sukupuolen voi laittaa tässä tai yllä olevassa henkilössä]

### Paikat

        
    place - referenssi tähän paikkaan
    title - paikan otsikko
    name - paikan nimi
    type - paikan tyyppi (esim. Paikkakunta, Kunta, Valtio jne.)
    latitude - paikan leveyspiiri
    longitude - paikan pituuspiiri
    code - postinumero tms.
    enclosed_by - viite toiseen paikkaan, joka ympäröi tämän paikan
    date - päivämäärä(t) jolloin ympäröinti oli voimassa

## Yksityiskohdat

Kirjaimen koolla ei ole merkitystä. Huomaa, nimissä ei ole alaviivoja. Voit yhdistellä nimen osia miten haluat ja haluamassasi järjestyksessä. Itse asiassa, sinun on vähintään käytettävä sukunimeä ja yhtä etunimeä henkilön määrittelyyn, ja sinulla on oltava avioliiton ja lasten sarakkeet, kun määrität lapsia, ja paikat tarvitsevat paikkareferenssin, mutta se riittää. Sarakkeiden nimet (ja sanat "mies" ja "nainen") ovat sen kielisiä, millä käytät Grampsia.

Näistä jokainen voi mennä omalle alueelleen laskentalomakkeella. Alueitten määrää ei ole rajoitettu ja kullakin alueella voi olla rajaton määrä rivejä. Jätä alueitten väliin tyhjä rivi. Varmista, ettäalueet eivät sivua toisiaan; niiden täytyy olla toisensa ylä- ja alapuolella.

Sinulla voi olla useita alueita saman lajisiin tietoihin. Ainoa rajoitus on, että jos viittaa henkilöön,viittaus on tehtävä alemmalta riviltä kuin missä henkilö on kuvattu. Samaten, viittaus avioliittoon on tehtävä alemmlta riviltä kuin missä avioliitto on kuvattu. Ympäröivien paikkojen referenssien on löydyttävä entuudestaan sukupuusta tai ne on määriteltyvä aikaisemmi laskentalomakkeella.

Kun syötät tietoja tekstitiedostoon ja kun haluat pilkun jonkun arvon sisään (kuten "Clinton, Co., MO") , on koko arvo ympäröitävä kaksoislainausmerkkeillä, joista ensimmäinen juuri edeltävän pilkun jälkeen. Esimerkiksi:

    avioliitto, vanhempi1, vanhempi2, paikka
    m1, p1, p2,"Clinton, Co., MO"
    m2, p3, p4,"Havertown, PA"

Laskentataulukko-ohjelma tekee tämän automaattisesti puolestasi.

Tässä on esimerkkinä Open/Libre Officen laskentalomake, mutta minkä tahansa laskentalomakeohjelman pitäisi toimia.

![[_media/Gramps-csv-example1.csv-LibreOffice-Calc--example-60.png|Kuva {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}}]]

{{-}} Huomioi, että tietojen ei tarvitse alkaa ensimmäisestä sarakkeesta tai riviltä.

Ja tässä ovat tiedot Grampsiin vietynä:

![[_media/FamilyTree-example-imported-gramps-csv-example1.csv-60.png|Kuva {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}}]]

{{-}}

### Esimerkki CSV jossa useita alueita

Tässä on esimerkki CSV tekstimuotoisesta laskentataulusta, jossa on useita alueita:

    Etunimi, Sukunimi, Syntymäpäivä
    John,      Tester,  11/11/1965
    Sally,     Tester,  01/26/1973

    Henkilö, Etunimi, Sukunimi
    p1,     Tom,       Smith
    p2,     Mary,      Jones
    p3,     Jonnie,    Smith
    p5,     James,     Loucher
    p6,     Penny,     Armbruster
    p7,     Tim,       Sparklet

    Avioliitto, Mies, Vaimo
    m1,       p1,      p2
    m2,       p5,      p6

    Perhe, Lapsi
    m1,     p3
    m1,     p6
    m2,     p7

    Paikka, Nimike, Nimi, Tyyppi
    p1, Canada, Canada, Country
    p2, USA, USA, Country

Jos leikkaat ja liität sen tiedostoon (tai käytät [Import Grampletia](wiki:Addon:ImportGramplet)), voit tuoda sen suoraan Grampsiin.

Huomaa, että päivämäärän voi antaa minä tahansa validina Gramps päivämääränä, ml. including myös muodoissa "26.1.1955" ja "26 JAN 1955".

Jos viittaat jo Grampsista löytyviin kohteisiin laita viitteet hakasulkuihin, tähän tapaan:

    Henkilö,    Etunimi, Sukunimi
    joe's boy, Harry,     Smith

    Perhe,  Lapsi
    [F1524], joe's boy

    Mies, Vaimo
    [I0123], [I0562]

    etunimi, sukunimi
    Timothy, Jones

    Paikka, Ympärillä
    [P0001], [P0002]

Tämä esimerkki loisi ja lisäisi Harry Smithin aikaisempaan perheeseen Grampsissa, F1524.

Esimerkki muodosti myös avioparin kahdesta, Grampsin sukupuusta löytyvästä henkilöstä, I0123, ja I0562.

Lopuksi luotiin henkilö nimeltään Timothy Jones, jolla ei ole suhdetta muihin.

Lopuksi, paikka P0001 laitetaan paikan P0002 ympyröimäksi.

### Tosimaailman esimerkki

![[_media/Gramps-csv-example3.ods-LibreOffice-Calc-example-60.png|Kuva {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}}]]

Tässä esimerkissä minun oli syötettävä kokonainen sukupolvi, 16 nimeä ja vihkipäivää. Lapset minulla oli jo tietokannassa. Syötin ne Open/Libre Office ohjelmassa:

Huomaa, että voit käyttää numeroita tai aakkostietoa viitteenä alueiden välillä. Henkilöalueella käytin numeroita 1-16. Näin niihin oli helppo viitata toisella, avioliittojen alueella. Avioliitot otsikoitiin kirjaimila A-H.

{{-}}

#### Vinkki

.}}

Huomaa myös että 3. alueen lapset ovat olemassa olevia henkilöitä, minkä osoittavat sulut Gramps tunnuksen ympärillä.

Tallentaminen CSV muooon ja tuominen Grampsiin luo puuhun äärimmäisenä oikealla olevan sarakkeen:

![[_media/FamilyTree-example-imported-gramps-csv-example3.csv-60.png|Kuva {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Oikealla oleva puusarake muodostuu CSV tallentamisesta ja tuomisesta Grampsiin.]]

[Category:Fi:Dokumentaatio](wiki:Category:Fi:Dokumentaatio)
