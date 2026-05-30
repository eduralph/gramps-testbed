---
title: Fi:Gramps 6.0 Wiki-käyttöohje - Aluksi
categories:
- Fi:Dokumentaatio
managed: false
source: wiki-scrape
wiki_revid: 122048
wiki_fetched_at: '2026-05-30T18:14:56Z'
lang: fi
---

{{#vardefine:chapter\|2}} {{#vardefine:figure\|0}} \_\_FORCETOC\_\_ Tässä kappaleessa aloitamme perusasioista. Näytämme miten käynnistät Gramps:in ja mistä löydät tarvittaessa apua.

## Yleistä Grampsista

Gramps on suunniteltu joustavaksi ja monipuoliseksi työkaluksi sukututkimukseen. Monipuolisuuden ja joustavuuden vuoksi on hyvä saada kokonaiskuva Grampsin toimintaperiaatteista ennen siirtymistä ohjelman käyttöohjeisiin.

Gramps jakaa kaiken sukututkimustiedon 9 ensisijaiseen kohteeseen:

- henkilöt
- perheet
- tapahtumat
- lisätiedot
- media
- lainaukset
- lähteet
- paikat
- arkistot

Kukin näistä koostuu itsenäisistä kohteista. Tämä tarkoittaa sitä, että voit lisätä sukupuuhusi yhden kohteen kerrallaan ja haluamassasi järjestyksessä. Esimerkiksi haluat ehkä ensin syöttää henkilöt ja sitten myöhemmin yhdistää heidät luomalla perheitä. Tai aloitat lähteillä ja lisäät henkilön vasta kun siihen on tarvetta. Tai voit yhdistellä toimintatapoja lisäämällä lisätietoja ja lähteitä, sitten perheitä ja palata myöhemmin lisätietoihin ja lähteisin. Toisin sanoen teet sukututkimusta oman mielesi mukaan.

Lisäkysymyksiin saa vastauksia Grampsin käyttäjien ja khittäjien yhteisöltä. Löytyy myös [FAQ](wiki:Gramps_6.0_Wiki_Manual_-_FAQ) (usein esitettyjen kysymysten lista); a postituslista; [virheilmoitusten ja kehitysehdotusten tekemiseen ja niiden seuraamiseen](http://www.gramps-project.org/bugs/); ja on-line keskustelutila.

### Yhteydet

Ensisijaisia yhdeksää kohdetta yhdistetään useilla tavoilla. Joitakin yhteyksiä pidetään yllä taustalla. Esimerkiksi henkilön lisääminen perheeseen vanhempana tai lapsena luo automaattisesti erityisen yhteyden, nimeltään **Viite**. Henkilö-dialogin viitteet-lehdellä voit nähdä perheet, joihin henkilö on yhdistetty. Grampsissa on monia muita tapoja yhteyksien visualisointiin, mukaan lukien Suhteet-näkymä.

Tietojen toistamisen välttämiseksi Gramps sallii käyttää uudelleen tai jakaa kohteita. Tämä tapahtuu myös erityisillä yhteyksllä, joita kutsutaan **Linkeiksi**. Esimerkiksi henkilö on voitu linkittää rajoittamattomaan joukkoon lisätietoja. Jos lisätieto mainitsee kaksi eri henkilöä, saattaa olla mielekästä jakaa yksi lisätietokohde kummankin henkilön kesken.

Joissakin linkeissä on itsessään informaatiota. Voit esimerkiksi linkittää henkilön toisen pariskunnan avioliittotapahtumaan, vaikkapa vihkimisen todistajaksi. Mies ja vaimo on linkitetty avioliittotapahtumaan **päähenkilö** roolilla, kun taasen todistaja on toisessa roolissa, esim. **todistaja**. Tällainen informaatio on linkissä itsessään, rooli-ominaisuutena.

### Yksityisyys

Gramps tukee erilaisia menettelyitä sukupuusi arkaluonteisen tiedon suojelemiseksi. Menettelyitä käytetään, kun jaat tietoja muille, joku luomalla raportin, viemällä tietoja ohjelmassa tai luomalla nettisivuston. Ensimmäinen menettely suojaa niiden henkilöiden tietoja, jotka Gramps olettaa elossa oleviksi. Jos et ole nimenomaan ilmoittanut henkilön kuolleen (lisäämällä henkilölle kuolintapahtuman), silloin Grampsilla on kehittynyt automaattinen toiminto sen päättelemiseksi, onko hän elossa. Elossa olevien henkilöiden arkaluonteiset tiedot karsitaan tätä menettelyä käytettäessä. Esimerkiksi henkilö "Nieminen, Liisa" näytetään muodosssa "Nieminen, \[elossa\]".

Toinen yksityisyysmenettely on asettaa nimenomainen "yksityinen" tagi, joka voidaan liittää kaikkiin kohteisiin. Sinulla voi esimerkiksi olla arkaluonteista informaatiota jossakin lisätiedossa. Jos merkitset tämän lisätiedon yksityiseksi, lisätietoa ei näytetä tekstiraporteissa eikä viedä ulos Grampsista. Huomioi myös, että jotkut linkit itsessään voidaan määrittää yksityisiksi. Tätä voit hyödyntää, kun haluat merkitä esimerkiksi henkilön liittymisen johonkin tapahtumaan yksityiseksi, mutta kuitenkin säilyttää henkilön ja tapahtuman raporttien, viennin tai nettisivuston ulottuvilla.

Näiden menettelyiden aktivoimiseksi suojelemaan yksityisyyttä on tarpeen ilmoittaa siitä, kun raportteja luodaan tai tietoja viedään.

### GEDCOM

Grampsin tietorakenteen ydin periytyy GEDCOM standardista. Gramps laajentaa kuitenkin tätä standardia missä näkee tarpeelliseksi. Jos suunnittelet käyttäväsi Grampsin tietoja sukupuusta jossain muussa sovelluksessa, joka käyttää GEDCOMia, silloin todennäköisesti kannattaa rajata Grampsin omien laajennusten käyttöä. Toisaalta, jos sinua ei rajoita muut sovellukset, voit kirjata tietojasi Grampsiin niin kuin haluat.

Tästä aiheesta voit lukea enemmän täältä: [Gramps and GEDCOM](wiki:Gramps_and_GEDCOM).

## Käynnistä Gramps

Tapa käynnistää Gramps riippuu käyttämästäsi käyttöjärjestelmästä.

Grampsin voi käynnistää normaalilla graafisella käyttöliittymällä (GUI) kuten alla kuvataan, mutta sen voi käynnistää myös komentoriviltä (CLI). CLI:n käyttäminen voi tuottaa raportteja, joita ei saa GUI:n kautta, komentoriviä voi käyttää raporttien luomiseen, konversioiden tekemiseen jne ilman ohjelman avaamista näyttöön sekä [lisätietojen saamiseen](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window#Seeing_all_the_error_messages) ongelmatilanteissa. Liätietoja katso [the Command Line appendix](wiki:Gramps_6.0_Wiki_Manual_-_Command_Line).

### Linux

Only the Linux platform is officially supported as Gramps developers use and test the source code on that platform, fixing any problems that arise due to upgrades.

Edellyttäen että olet käyttänyt vakio Package Manageria (joko CLI:n tai GUI:n kautta) Linux jakelussasi, käynnistät Grampsin kuten muutkin sovellukset. Esimerkiksi Ubuntu 18.4:ssa on kuvake launcherissa, tai ohjelman voi käynnistää Dash:stä. Muissa jakeluissa käynnistys voi tapahtua Application valikosta (tavallsesti **Office** osiossa).

Grampsin käynnistys CLI:stä Linuxissa on kuvattu [täällä](wiki:Gramps_6.0_Wiki_Manual_-_Command_Line#Linux).

### MS Windows

MS (Microsoft) Windows on [Gramps yhteisön tukema](wiki:Download#Community_supported) alusta. Jos asennat[Windows AIO](wiki:All_In_One_Gramps_Software_Bundle_for_Windows) GrampsAIO32 tai GrampsAIO64 käännetyn ohjelman, sille on kuvake työpöydällä ja myös valinta 'Käynnistä' valikossa, ja niistä napsauttamalla käynnistät Grampsin.

Tutki myös Käynnistä-menua, jossa on useita valintoja mm. ohjelman poistamiseen. Mihin käyttäisit eri vaihtoehtoja?

Grampsin käynnistys CLI:stä MS Windowsissa on kuvattu [täällä](wiki:Gramps_6.0_Wiki_Manual_-_Command_Line#MS_Windows).

On muitakin tapoja asentaa \_Gramps MS Windowsissa, mutta ne ovat paljon monimutkaisempia eikä niitä kuvata tässä enempää.

### Mac OS X

Apple Mac OS X (MacOS) is a [Gramps yhteisön tukema](wiki:Download#Comunity_supported) alusta. Jos lataat Mac OS X disk imagen (.dmg), voit yksinkertaisesti raahata sen sovelluskansioosi (tai minne tahansa haluamaasi paikkaan) ja käynnistää Grampsin kaksoisnapsauttamalla kuten muutkin sovellukset.

Grampsin käynnistys CLI:stä Mac OS X on kuvattu [täällä](wiki:Gramps_6.0_Wiki_Manual_-_Command_Line#Mac_OS_X).

On muitakin tapoja asentaa \_Gramps Mac OS X:ssa, mutta ne ovat paljon monimutkaisempia eikä niitä kuvata tässä enempää.

## Kielet

Gramps on käännetty usealle kielelle: [languages](wiki:Portal:Translators). Gramps käynnistyy tavallisesti automaattisesti oman kielisenäsi kuten muissakin sovelluksessa voi valita, mutta joskus tämä ei haluamasi .

(kesken) Describe for each main platform how the normal language is determined and how the user can [choose a different language](wiki:Howto:Change_the_language_of_reports#Run_Gramps_in_a_different_language).

### Linux

(kesken)

Jos haluat oletusarvosta poikkeavan paikallisen version lajitteluista, voit käynnistää Grampsin konsolilta erilaisella LC_COLLATE ympäristömuuttujalla. Esimerkiksi oletusarvoinen lajittelu (collation) versio Ruotsille on "reformed", mutta voit valita "standardin" näppäilemällä:

`export LC_COLLATE="sv_SE.UTF-8@collation=standard"`  
`python Gramps.py`

### MS Windows

Näppäilemällä seuraavat rivit komentotiedostoon, nimenä esim. Gramps_fi.cmd , saat Grampsin käynnistymään halutun kielisenä. Esimerkissä Gramps 6.0 suomeksi:

GrampsAIO-6.0.1-1_win32

`*Echo off`  
`REM it's to switch Gramps 6.0.1 to FINNISH in Windows 7 (10)`  
`SET LANG=fi_FI.UTF-8 `  
`SET LANGUAGE=fi_FI.UTF-8 `  
`cd "C:\Program Files (x86)\GrampsAIO32-6.0.1\bin" `  
`grampsw.exe `

GrampsAIO-6.0.1-2_win64

`*Echo off`  
`REM it's to switch Gramps 6.0.1 to FINNISH in Windows 7 (10) `  
`SET LANG=fi_FI.UTF-8 `  
`SET LANGUAGE=fi_FI.UTF-8 `  
`cd "C:\Program Files\GrampsAIO64-6.0.1\bin" `  
`grampsw.exe `

Tallenna tiedosto työpöydälle. Tuplanapsauttamalla tiedostoa Gramps avautuu suomeksi. Jos muutat riveillä fi_FI :n esim de_DE :ksi, se avautuu saksankielisenä.

### Mac OS X

Mac OS X:lle katso [Advanced setup](wiki:Mac_OS_X:Application_package#Advanced_setup) saadaksesi tarkemmat tiedot miten kieli valitaan normaalisti ja kuinka valitaan erityinen, vakiosta poikkeava kieliasetus, lajittelujärjestys ja mm. päivien ja kuukausien nimet ja numeroiden erotusmerkit.

## Sukupuun valitseminen

![[_media/Dashboard-category-view-first-open-no-family-tree-loadedFi-50.png|Kuva {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Aloitusikkuna kun sukupuuta ei ole valittu]]

Jos Gramps on käynnistetty ilman sukupuun valintaa, aloitusikkunassa on vähän toiminnallisuutta. Useimmat toimenpiteet eivät ole käytettävissä. Sukupuun (jota kutsutaan myös 'tietokannaksi') lataamiseksi valitse avataksesi sukupuiden hallinnan, tai napsauta kuvaketta työkalupalkissa. Gramps muistaa sinun viimeksi avaamasi sukupuusi ja ne on valittavissa napsauttamalla nuolta painikkeen vieressä ja valitsemalla sukupuu pudotusvalikosta.

Lisää tietoja sukupuiden hallinnasta ja sukupuiden valikosta saat täältä: [Hallinnoi sukupuita](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees).

{{-}}

## Kerro miten aloitan juuri nyt!

Neuvomme jokaista lukemaan käyttöohjeen Grampsin kaikkien piirteiden oppimiseksi. Sukututkimus vie aikaa, joten työkalujen opiskelu ei ole hukkaan heitettyä aikaa.

Kuitenkin jos haluat päästä pikaisesti liikeelle, niin lue nämä:

- [Tietojen syöttäminen ja muokkaaminen: Lyhyesti](wiki:Fi:Gramps_6.0_Wiki-k%C3%A4ytt%C3%B6ohje_-_Tietojen_sy%C3%B6tt%C3%A4minen_ja_muokkaaminen:_Lyhyesti)
- [How-To start with Genealogy using Gramps](wiki:Start_with_Genealogy).

## Avun saaminen

Grampsissa on valinta, johon voit turvautua aina tarvittaessa. {{-}}

[Category:Fi:Dokumentaatio](wiki:Category:Fi:Dokumentaatio)
