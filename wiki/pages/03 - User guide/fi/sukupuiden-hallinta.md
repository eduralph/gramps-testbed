---
title: Fi:Gramps 6.0 Wiki-käyttöohje - Sukupuiden hallinta
categories:
- Fi:Dokumentaatio
- Stub
managed: false
source: wiki-scrape
wiki_revid: 127181
wiki_fetched_at: '2026-05-30T18:28:53Z'
lang: fi
---

{{#vardefine:chapter\|5}} {{#vardefine:figure\|0}} Nyt suuntaamme yksityiskohtaiselle tutkimusmatkalle päivittäiseen Gramps:in käyttöön. Tässä kappaleessa esitämme yksityiskohtaisen katsauksen miten voit hallita sukupuitasi ja miten jaat tietosi muiden sukututkijoiden kanssa.

## Uuden sukupuun aloittaminen

Aloittaaksesi uuden sukupuun, valitse tai valitse painike työkaluriviltä tai käytä [keybinding](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings) . Tämä avaa .

Valitse ja Gramps luo uuden sukupuun sukupuiden listalle. Vaihtaaksesi nimen oletusnimestä *Sukupuu 1* napauta nimeä, paina painiketta ja kirjoita uusi nimi.

Valitse ladataksesi uuden tyhjän sukupuun.

{{-}}

### Sukupuiden hallinnointi ikkuna

![[_media/ManageFamilyTrees-50FI.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Sukupuut" hallinnointi ikkuna]]

Napsauttamalla Sukupuut\>Sukupuiden hallinnointi painiketta avautuu ikkuna, jossa voit hallinnoida kaikkia sukupuitasi.

Sukupuiden hallinnointi-ikkunassa voit luoda uuden sukupuun, muuttaa sukupuiden nimiä, poistaa sukupuun, tuoda sukupuun tai tarkistaa sukupuun tietoja. Kaikki sukupuut ovat lastattuna. Jos sukupuu on avattuna, siitä on kuvake tila-sarakkeessa. {{-}}

## Sukupuun avaaminen

Avataksesi sukupuun valitse joko menu tai napsauta painiketta työkaluriviltä. ikkuna tulee näkyviin ja näet listan kaikista Gramps:in tuntemista sukupuista. Kuvake näyttää sarakkeessa sukupuun vieressä, mikäli sukupuu on avoimena. Valitse haluamasi sukupuu ja avaa se painikkeella. Vaihtoehtoisesti voit kaksoisnapsauttaa haluttua puuta.

Viimeksi käytetyn sukupuun avaamiseksi valitse joko ' tai nuoli alaspäin seuraavana painikkeesta tai sen vieressä olevasta nuoli alaspäin painikkeesta haluamasi sukupuu.

## GEDCOM tai XML tietokannan avaaminen

Jos tietokanta ei ole tallennettu Grampsin omaan tiedostomuotoon, se on kuitenkin avattavissa Grampsissa komentorivin kautta. Katso [Command line references](wiki:Gramps_6.0_Wiki_Manual_-_Command_Line#Opening_options). Tällaisia ovat esim. XML ja GEDCOM tietokannat. Katso lisäohjeita [Command line references](wiki:Gramps_6.0_Wiki_Manual_-_Command_Line#Opening_options). Huomioi kuitenkin se, että jos XML tai GEDCOM tietokanta on suhteellisen suuri, tulee suorituskyvyn ongelmia ja tietosi voivat korruptoitua kaatumisen tapahtuessa . Siksi on tavallisesti parempi luoda uusi Gramps sukupuu (tietokanta) ja tuoda XML/GEDCOM tiedot siihen.

## Sukupuun poistaminen

Valitse sukupuu jonka haluat poistaa ja napauta painiketta.

Tämä poistaa **kokonaan** puun, ilman mahdollisuutta palauttaa tietoja. Harkitse varmuuskopion ottamista viemällä tietosi Gramps XML-muotoon ja säilyttämällä tiedosto.

## Sukupuun uudelleen nimeäminen

Voit uudelleen nimetä sukupuusi (tai sen arkistoidun version) valitsemalla puun ja napsauttamalla . Voit myös napsauttaa nimeä puiden listassa.

Molemmissa tapauksissa kirjoita vain uusi haluamasi nimi.

## Sukupuun varmuuskopiointi

Turvallisin tapa varmuuskopioida Gramps sukupuusi on viedä se **Gramps XML** muotoon (tai **Gramps paketiksi** joka sisältää myös tiedostot galleriasta) ja kopioida syntynyt tiedosto turvalliseen paikkaan, mieluummin eri rakennukseen tai pilveen.

Voit käyttää arkistointia tallentaaksesi tilannekuvan puustasi. Näitä tilannekuvia voi käyttää yksinkertaisina varmuuskopioina. Se on käyttökelpoinen tapa, jos haluat kokeilla jotakin minkä myöhemmin saatat haluta perua. Kuitenkin tätä tapaa ei tule käyttää normaaliin varmuuskopiointiin. Arkistokopio ei selviä kiintolevyn rikosta eikä useimmista muistakaan tuhoista, joita voi tapahtua tietokoneelle.

**Kokeneille käyttäjille:** jokainen tietokanta on talletettu omaan alihakemistoonsa hakemiston ~/.gramps alle. Käsin tehtävä varmuuskopiointi voidaan tehdä varmistamalla tämä hakemisto.

### Varmuuskopioinnin ikkuna

![[_media/MakeBackup-GrampsXMLBackupFi-41.png|Kuva. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Varmuuskopiointi]]

Valitse .

ikkuna avautuu.

Kopion tallennuspolku voidaan syöttää suoraan tai valita tiedostohakemiston kautta..

Sukupuun otetaan oletusarvoisesti mukaan, mutta voit jättää ne poiskin.

  

### Vaativammat asetukset

Varmuuskopiotiedoston nimen rakenne asetetaan *paths.quick-backup-filename* vakiossa ~/.gramps/gramps60/gramps.ini tiedostossa seuraavasti:

`[paths]`  
`quick-backup-filename='%(filename)s_%(year)d-%(month)02d-%(day)02d.%(extension)s'`

Seuraavat vakiosanat on käytettävissä rakenteessa:

- filename
- year
- month
- day
- hour
- minutes
- seconds
- extension:
  - .gpkg'''(oletusarvo) jos mediat mukana.
  - .gramps'' jos mediat jätetään pois.

Käytä sopivaa ~/.gramps/gramps{XX}/gramps.ini avaintiedostoa.

- Gramps versio 6.0 :

`~/.gramps/gramps42/gramps.ini`

- Voit arkistoida (katso seuraava luku) sukupuusi tilanteita. Niitä voidaan käyttää, kun yrität sukupuussasi jotakin, minkä haluat myöhemmin peruuttaa. Menettely ei kuitenkaan sovellu varmuuskopiointin, koska ne eivät säily kovalevysi rikkoutuessa tai muissa tietokonettasi kohtaavissa onnettomuuksissa.

<!-- -->

- *Edistyneille käyttäjille:* jokainen sukupuu talletetaan omaan alihakemistoonsa ~/.gramps hakemistossa. Manuaalisen vamuuskopion saa tehdyksi ottamalla tästä hakemistosta kopion.

## Sukupuun arkistointi

<center>

</center>

RCS:n avulla voidaan helposti arkistoida ja aikaleimata sukupuut.

Arkiston tekemiseksi:

![[_media/ManageFamilyTrees-ArchiveEnterVersionDescriptionFi-41.png|Kuva {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Sukupuun arkistoinnista esimerkki]]

1.  lataa sukupuusi.
2.  napsauta työkalupalkissa painiketta (se näyttää vihjetekstin kun viet osoittimen sen päälle).
3.  napsauta lataamaasi sukupuuta: painikkeen pitäisi tulla esille.
4.  napsauta painiketta, jolloin sinua pyydetään syöttämään "versiokommentti ja kuvaus" arkistollesi.

Arkistoinnin jälkeen sukupuiden listassa on alkuperäisen sukupuun vasemmalla puolella oikealle osoittava kolmio.

- napsauta kolmiota, jolloin näkyville tulee arkiston nimi (uudelleen napsautus supistaa arkistolistan).

Arkistoja voidaan poistaa, nimetä uudelleen ja ottaa niiden tiedot käyttöön.

{{-}}

## Sukupuun arkiston palauttaminen

![[_media/ManageFamilyTrees-ArchiveSelectToExtractFi-41.png|Kuva {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Palautettavan version valinta]]

Kun napsautat arkistoa, painike tulee näkyviin. Sitä napsauttamalla arkistoitu sukupuuversio palautetaan tavallisten joukkoon. Se näkyy sitten sukupuiden listassa *<alkuperäisen puun nimi>:<arkistonimi>* nimisenä ja se on itsenäinen sukupuu. Tämä on hyödyllinen tapa saada arkisto talteen, koska alkuperäisen sukupuun poistaminen hävittää myös sen arkistokopiot ja arkistoja ei oteta mukaan myöskään Portable Gramps XML -muotoisessa viennissä.

![[_media/ManageFamilyTrees-ArchiveExtractedVersionShownFi-41.png|Kuva {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Palautettu arkisto]]

(katso myös [Sukupuun arkistointi](wiki:Fi:Gramps_6.0_Wiki-käyttöohje_-_Sukupuiden_hallinta#Sukupuun_arkistointi)).

{{-}}

## Sukupuun lukon avaaminen

![[_media/Locked-Family-Trees-Dialog_fi-42.png|Kuva. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Lukitun sukupuun - esimerkki-ikkuna]]

Kun Gramps avaa puun, se lukitsee sen estääkseen sinua tai ketään muuta avaamasta sitä samanaikaisesti. Toisella käynnissä olevalla Grampsilla voit avata toisen sukupuun, mutta avoinna oleva puu näkyy "lukittu" kuvakkeella, osoittaen että et voi avata sitä. Puun sulkeminen toisessa Grampsissa antaa mahdollisuuden avata se toisessa käynnissä olevassa Grampsissa.

Jos voisit avata sukupuun kahdessa Grampsissa yhtaikaa, se todennäköisesti vioittaisi tietojasi. {{-}}

Epätodennäköisessä Grampsin kaatumisessa sukupuu jää lukituksi. Puun lukon avaamiseksi: {{-}} ![[_media/Database_is_locked2_fi-42.png|Kuva. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Sukupuu on lukittu]]

- Jos Gramps on asetettu avaamaan käynnistyessään sukupuun automaattisesti, näet 'Sukupuu on lukittu' ilmoituksen. Napsauta painiketta aktivoimiseksi. Valitse lukittu sukupuu ja napsauta sitten painiketta. 'Rikotaanko lukitus' ikkuna käynnistyy.

{{-}} ![[_media/Break-the-lock-on-the-database-Dialog_a_fi-42.png|Kuva. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Rikotaanko sukupuun &quot;Gramps malli&quot; lukitus]]

- valitse lukittu sukupuu ja napsauta näkyville tulevaa painiketta. Avaa lukko vain ollessasi varma, ettei sukupuuta käytetä toisessa Grampsissa..

{{-}}

## Vioittuneen sukupuun korjaaminen

![[_media/FamilyTreesManager-Dialog-ShowingRedErrorStatusIcon-Sample-50.png|Kuva 6.0 Sukupuun korjaaminen]]

Jos sukupuusi vaurioitui jostakin syystä, Grampsin sukupuiden hallinta ikkunassa näet punaisen virhekuvakkeen sarakkeessa.

Saadaksesi Grampsin yrittämään viottuneen korjausta, valitse puu ja sitten napsauta painiketta.

Tämä yrittää korjata puun varmuuskopiosta, joka luotiin automaattisesti poistuttaessa.

## Muutosten tallettaminen sukupuuhun

Gramps tallettaa muutokset heti hyväksyttyäsi ne. Tämä tarkoittaa esimerkiksi, että käyttäessäsi Grampsia joka kerta kun napsautat painiketta muutokset on kirjattu ja talletettu välittömästi. Erillistä "tallenna" komentoa ei ole.

Voit peruuttaa tekemäsi muutokset valitsemalla **Muokkaa -\> Peru**. Jos valitset komennon toistuvasti, uusimmat muutokset perutaan yksittäin. Palataksesi useampia komentoja kerrallaan voit käyttää ikkunaa, joka löytyy valikosta.

Jos haluat palauttaa sukupuusi sen avaustilaan, valitse **Sukupuut -\> Hylkää muutokset ja lopeta**. (Tämä toimii samoin kuin lopettaminen ilman tallennusta muissa ohjelmissa.)

Jos haluat tallettaa kopion sukupuustasi eri nimellä, sinun tarvitsee viedä sukupuu ja sitten tuoda se sitten uuteen sukupuuhun. *Gramps XML tietokanta* on suositeltavin tähän tarkoitukseen.

## Tietojen tuonti

Tuonti sallii siirtää tietoja muista sukututkimusohjelmista Gramps tietokantaan. Tällä hetkellä Gramps voi tuoda tietoja seuraavissa tiedostomuodoissa:

- [Gramps XML](#Gramps_XML_and_XML_Package_import) (`.gramps` erotin)
- [Gramps XML paketti](#Gramps_XML_and_XML_Package_import) (`.gpkg` erotin)
- [Gramps CSV laskentalomake](#Gramps_CSV_import) - pilkkuerotetut (`.csv` erotin)
- [GRAMPS V2.x tietokanta](#GRAMPS_V2.x_database_import) (`.grdb` erotin)
- [GEDCOM](#GEDCOM_import) (`.ged` erotin)
- GeneWeb (`.gw` erotin)
- Pro-Gen (`.def` erotin)

Tuodaksi tiedot valitse **Sukupuut -\> Tuonti**. **Tuo tietokanta** ikkuna aukeaa ja pyytää valitsemaan tiedoston, jonka haluat tuoda. Huomaa että voit tuoda vain tietoja olemassa olevaan tietokantaan. Jos olet siirtämässä tietoja toisesta ohjelmasta tai vanhemmasta Gramps versiosta, niin ensin luo tyhjä tietokanta ja tuo sitten tiedot siihen.

Tuodessasi tietoja jo olevaan sukupuuhun ikkuna avautuu antaen sinulle mahdollisuuden myös luoda ensin uuden sukupuun, ennen tietojen yhdistämistä jo olevaan puuhun..

Gramps V2.x tietokannat, Gramps XML ja Gramps paketit ovat kaikki alkuperäisiä Gramps tiedostomuotoja. Tietojen katoamisesta ei ole vaaraa, kun tuodaan tai viedään näihin tiedostomuotoihin.

### Gramps V2.x tietokannan tuonti

- Gramps V2.x tietokanta (grdb): Tämä alkuperäinen Gramps tietokantamuoto oli ennen Grampsin 4 versiota käytössä ollut Berkeley tietokanta (BSDDB) , jossa on erikoisrakenne tietotauluissa. Tiedostokantamuoto oli binäärinen ja arkkitehtuuririippuva. Se oli erittäin nopea ja tehokas. Se ei ollut yleisesti siirrettävissä erilaisen binääriarkkitehtuurin (esim. i386 tai alpha) tietokoneiden välillä.

Vain Gramps version 3.0.x tukee Gramps V2.x muotoisen tietokannan tuontia. Tuonti tapahtuu siihen ilman tietojen menetyksiä.

#### Gramps 2.2 tietokantojen siirto versioon Gramps 3.x

Jos siirrät dataa versiosta 2.x versioon 6.0.x on sinun ensin vietävä v2.x tietokanta aikaisempaan Gramps v3.0.x ohjelmaan ja sitten joko talletettava tietokanta tai tuotava se versioon Gramps 6.0.x, tai tuotava tietokanta [XML](wiki:XML) muotoisena ja tuotava se sitten Gramps versioon 6.0.x.

Aikaisempien Gramps versioiden [Käyttöohjeet](wiki:User_manual) antavat tarkemmat ohjeet v2.x tietokantojen siirrosta Gramps versioon v3.x.

{{-}}

### Gramps XML and XML paketin tuonti

Gramps [XML](wiki:XML) and Gramps [XML](wiki:XML) Package ovat Grampsin nykyisin käytettäviä alkuperäisiä tietokantamuotoja. Niissä ei ole vaaraa tietojen menettämiselle.

- Gramps XML: Gramps XML on tietojen siirrossa ja varmuuskopioissa käytettävä Gramps 4:n vakio tietokantamuoto. Toisin kuin Gramps V2.x tiedostomuoto, Gramps XML on arkkitehtuuririippumaton ja ihmisluettava. Tietokannassa voi olla myös viittauksia ulkoisiin mediatiedostoihin, jolloin ei ole varmuutta täydellisestä siirrettävyydestä (mediatiedostojen saamiseksi mukaan on käytettävä Gramps XML pakettia). Gramps XML tietokanta luodaan viemällä (*'Sukupuut -\> Vienti*) valinnassa tiedot tähän tiedostomuotoon.

<!-- -->

- Gramps XML paketti: Gramps XML paketti on koostetiedosto. Se sisältää Gramps XML tiedoston ja kaikki mediatiedostot (kuvat, äänet, jne.) joihin tietokanta viittaa. Koska paketti sisältää kaikki mediatiedostot, tämä tiedostomuoto on täysin siirrettävä. Gramps XML paketti luodaan viemällä (**Sukupuut -\> Vienti**) valinnassa tiedot tähän tiedostomuotoon.

Jos tuot tiedot toisessa Gramps tietokannasta tai Gramps XML tietokannasta, näet tapahtuman edistymisen Grampsin pääikkunan edistymispalkissa. Tuonnin päätyttyä palauteikkuna näyttää tuotujen kohteiden lukumäärän. Jos data on alunperin lähtöisin tietokannasta, johon tuodaan, Gramps tekee ehdotuksia siitä mitä kaikkea voitaisiin sulauttaa; sulautuksia **ei** tehdä puolestasi automaattisesti. Harkitse CSV-muotoista vientiä/tuontia, jos haluat perustason automaattista sulauttamista.

### Gramps CSV tuonti

- Gramps CSV taulukkolaskenta tiedostomuoto tuo ja vie osan Gramps tiedoista yksinkertaiseen taulukkolaskentamuotoon. Katso lisätietoja [CSV Import and Export](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees:_CSV_Import_and_Export).

### GEDCOM tuonti

![[_media/GEDCOM-import-reportFi-41.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Import report]]

Kun tuot tietoja GEDCOM-tiedostona, tuonnin eteneminen näkyy Grampsin pääikkunan tilapalkissa. Tuonnin päätyttyä palauteikkuna näyttää tiedot, joita ei tuotu. Raportti (see fig 4.6) näyttää useimmat rivit, jotka joko hylättiin tai joita ymmärretty. Rivin (tai usean rivin jos tieto jatkui niille) sisältö näytetään myös. Joissakin tapauksissa rivit eivät ole täsmälleen samoja kuin GEDCOM-tiedostossa oli, koska rivit rakennetaan tietyillä säännöillä.

Kun tuot tietoja GEDCOM-muodossa, Grampsin pääikkuna näyttää edistymisen, ks. [edistymismittari](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window#Status_Bar_and_Progress_Bar). Gedcom-tuonnin päätyttyä ikkuna ja ikkuna näyttävät tulokset tai varoitukset.

{{-}}

#### GEDCOM Merkkikoodaus ikkuna

![[_media/GEDCOM-Encoding-dialog-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} GEDCOM Merkkikoodaus - ikkuna]]

ikkuna näytetään, jos tuotava GEDCOM tiedosto kertoo olevansa ANSEL koodausta. Joskus tämä on virhe. Jos GEDCOM:n tuonnin jälkeen huomaat sen sisältävän epätavallisia merkkejä, peruuta tuonti ja suorita uuskoodaus valintalistasta.

- **oletus**
- ANSEL
- ANSI (iso-8859-1)
- ASCII
- UTF8

{{-}}

#### Tuontitilasto ikkuna

![[_media/ImportStatistics-dialog-example-GrampXML-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Tuontitilasto ikkuna]] {{-}}

#### GEDCOM tuonti raportti ikkuna

![[_media/GEDCOM-import-report-result-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} GEDCOM tuonti raportti - esimerkkitulokset.]]

**** näyttää yksityiskohtia useimmista GEDCOM riveistä, jotka ohitettiin tai jotka eivät olleet ymmärrettäviä (useimmiten eivät olleet GEDCOM 5.6.0 standardin mukaisia. Katso [Addon:GEDCOM Extensions](wiki:Addon:GEDCOM_Extensions)). GEDCOM rivi (tai rivejä jos olivat jatkorivejä) näytetään myös. Eräissä tapauksissa rivi ei ole täsmälleen se mikä luettiin GEDCOM-tiedostosta, vaan se on tietyn jatkokäsittelyn tulos. Katso **Raportin lukeminen** {{-}}

##### Raportin lukeminen

![[_media/Source-Note-GEDCOMImportNote-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} GEDCOM tuonti lisätieto eräästä &quot;Source&gt;Note&quot; tapauksesta(saatu &quot;GEDitCOM&quot; - &quot;GEDCOM 5.5 Torture Test Files&quot;]].

Grampsin tietomalli eroaa GEDCOMin tietomallista. Tästä johtuen joitain tietoja ei saa tuoduksi Grampsiin.

Pääpoikkeamat ovat:

- Joitain GEDCOM tietorakenteita käsitellään Grampsin ja siksi monet GEDCOM perustietoelementit eivät tallennu.
- SOURCE_RECORDin tiedot (osoittaen missä tapahtumat on kirjattu ja kenen toimesta) ohitetaan.
- lisätietojen lähdetiedot ohitetaan.
- monilla GEDCOM perustietoelementeilla ei ole täysin vastaavaa paria Grampsissä, siksi ne talletetaan, and they are therefore stored as tai sopivilla, yleensä Gedcomin tagi-nimillä. Tämä pätee etenkin header, submitter ja submission GEDCOM tietueisiin ja etenkin kenttiin kuten REFN, RFN, RIN ja AFN.

![[_media/Top_level_noteFi-41.png|Kuva {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Tuontiraportti: Esimerkki ohitettujen tietojen ylätasoista]] ![[_media/Note_text_exampleFi-41.png|Kuva {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Tuontiraportti: Esimerkki ohitetun datan huomautuksesta]]

Kun tieto on 'ohitettu', ohitus raportoidaan palautteena tuonnin loputtua ja siitä kerrotaan myös ao. kohteeseen lisättävässä lisätiedossa. Tieto lisätään ao. päätietoonsa erityisellä informaatiolla , esim. .

Tällä hetkellä tapahtuu myös tietojen ohittamista ilman Grampsin tekemää raportointia, mitä voidaan pitää toiminnallisena puutteena.

{{-}}

#### GEDCOM tuonnin rajoitukset

Tässä osassa kuvataan GEDCOM tiedot joita ei voida suoraan siirtää Grampsiin, ja niiden käsittely. Lisätietoa GEDCOM tuonnin (ja viennin) rajoituksista on luettavissa [Gramps ja GEDCOM](wiki:Gramps_ja_GEDCOM) osassa.

#### HEADer, SUBMitter ja SUBmissioN

Grampsissa ei ole suoraan vastinetta näille ja ne on siksi talletettava toisella tavalla. Riippuen [General preferences](wiki:Gramps_6.0_Wiki_Manual_-_Settings#General) asetuksista, voidaan luoda 'oletuslähde' objekti. Silloin paljon tietoa on talletettu , tai siihen liitettyihin .

`   HEADER:=`  
`        n HEAD                                          {1:1}`  
`          +1 SOUR `<APPROVED_SYSTEM_ID>`                  {1:1}  ('oletuslähteen' tietoja)`  
`            +2 VERS `<VERSION_NUMBER>`                    {0:1}  ('oletuslähteen' tietoja)`  
`            +2 NAME `<NAME_OF_PRODUCT>`                   {0:1}  ('oletuslähteen' tietoja)`  
`            +2 CORP `<NAME_OF_BUSINESS>`                  {0:1}  ('oletuslähteen' tietoja)`  
`              +3 <`<ADDRESS_STRUCTURE>`>                  {0:1}  ('oletuslähteen' tietoja)`  
`            +2 DATA `<NAME_OF_SOURCE_DATA>`               {0:1}  ('oletuslähteen' tietoja)`  
`              +3 DATE `<PUBLICATION_DATE>`                {0:1}  ('oletuslähteen' tietoja)`  
`              +3 COPR `<COPYRIGHT_SOURCE_DATA>`           {0:1}  ('oletuslähteen' tietoja)`  
`          +1 DEST `<RECEIVING_SYSTEM_NAME>`               {0:1*} ('oletuslähteen' tietoja)`  
`          +1 DATE `<TRANSMISSION_DATE>`                   {0:1}  ('oletuslähteen' tietoja)`  
`            +2 TIME `<TIME_VALUE>`                        {0:1}  ('oletuslähteen' tietoja)`  
`          +1 SUBM @`<XREF:SUBM>`@                         {1:1}  ('oletuslähteen' tietoja)`  
`                                                               (käytetään myös SUBMITTER_RECORD määrittelyyn)`  
`                                                               (tämä tulisi tallettaa sukupuun omistajaksi)`  
`          +1 SUBN @`<XREF:SUBN>`@                         {0:1}  (ohitettu)`  
`          +1 FILE `<FILE_NAME>`                           {0:1}  ('oletuslähteen' tietoja)`  
`          +1 COPR `<COPYRIGHT_GEDCOM_FILE>`               {0:1}  (talletetaan "oletuslähteen" Publication tietona)`  
`          +1 GEDC                                       {1:1}`  
`            +2 VERS `<VERSION_NUMBER>`                    {1:1}  ('oletuslähteen' tietoja)`  
`            +2 FORM `<GEDCOM_FORM>`                       {1:1}  ('oletuslähteen' tietoja)`  
`          +1 CHAR `<CHARACTER_SET>`                       {1:1}  ('oletuslähteen' tietoja)`  
`            +2 VERS `<VERSION_NUMBER>`                    {0:1}  (('oletuslähteen' tietoja)`  
`          +1 LANG `<LANGUAGE_OF_TEXT>`                    {0:1}  ('oletuslähteen' tietoja)`  
`          +1 PLAC                                       {0:1}`  
`            +2 FORM `<PLACE_HIERARCHY>`                   {1:1}  (katso alla)`  
`          +1 NOTE `<GEDCOM_CONTENT_DESCRIPTION>`          {0:1}  ("oletuslähteen" lisätieto)`  
`            +2 [CONT|CONC] `<GEDCOM_CONTENT_DESCRIPTION>` {0:M}`  
`            `  
`   * HUOMAA: Submissions to the Family History Department for Ancestral`  
`     File submission or for clearing temple ordinances must use a`  
`     DESTination of ANSTFILE or TempleReady.`

PLAC FORM talletetaan ja käytetään paikkojen tulkitsemiseen (GEDCOM määritysten mukaisesti).

SUBMISSION_RECORD (jota pitäisi olla vain yksi, mitä ei kuitenkaan tarkasteta) talletetaan 'oletuslähteen'

`    SUBMISSION_RECORD:=`  
`        n @`<XREF:SUBN>`@ SUBN                            {1:1]`  
`          +1 SUBM @`<XREF:SUBM>`@                         {0:1}`  
`          +1 FAMF `<NAME_OF_FAMILY_FILE>`                 {0:1}`  
`          +1 TEMP `<TEMPLE_CODE>`                         {0:1}`  
`          +1 ANCE `<GENERATIONS_OF_ANCESTORS>`            {0:1}`  
`          +1 DESC `<GENERATIONS_OF_DESCENDANTS>`          {0:1}`  
`          +1 ORDI `<ORDINANCE_PROCESS_FLAG>`              {0:1}`  
`          +1 RIN `<AUTOMATED_RECORD_ID>`                  {0:1}`

SUBMITTER_RECORD:it (voi olla useampia) talletetaan "oletuslähteen" paitsi alla vahvennuksela osoitetuissa tilanteissa. SUBMITTER_RECORD , joka vastaa HEADER:in SUBM tietoa , viedään [sukupuun omistajaksi](wiki:Gramps_6.0_Wiki_Manual_-_Tools#Edit_Database_Owner_Information...) esim.

`   SUBMITTER_RECORD:=`  
`        n @`<XREF:SUBM>`@   SUBM                          {1:1}`  
`          +1 NAME `<SUBMITTER_NAME>`                      {1:1}`  
`          +1 <`<ADDRESS_STRUCTURE>`>                      {0:1}`  
`          `**`+1 <`<MULTIMEDIA_LINK>`> {0:M}`**  
`          `**`+1 LANG `<LANGUAGE_PREFERENCE>` {0:3}`**  
`          `**`+1 RFN `<SUBMITTER_REGISTERED_RFN>` {0:1}`**  
`          `**`+1 RIN `<AUTOMATED_RECORD_ID>` {0:1}`**  
`          +1 <`<CHANGE_DATE>`>                            {0:1}`

- Multimedia linkki ohitetaan
- LANG ohitetaan
- RFN ja RIN ohitetaan

#### INDIvidual

INDIVIDUAL_RECORD talletetaan Grampsin (Person) tietueeksi, paitsi vahvennetulla tekstillä alla osoitetut.

`   INDIVIDUAL_RECORD: =`  
`        n @`<XREF:INDI>`@  INDI                           {1:1}`  
`          +1 RESN `<RESTRICTION_NOTICE>`                  {0:1}`  
`          +1 <`<PERSONAL_NAME_STRUCTURE>`>                {0:M}`  
`          +1 SEX `<SEX_VALUE>`                            {0:1}`  
`          +1 <`<INDIVIDUAL_EVENT_STRUCTURE>`>             {0:M}`  
`          `**`+1 <`<INDIVIDUAL_ATTRIBUTE_STRUCTURE>`> {0:M}`**  
`          +1 <`<LDS_INDIVIDUAL_ORDINANCE>`>               {0:M}`  
`          +1 <`<CHILD_TO_FAMILY_LINK>`>                   {0:M}`  
`          +1 <`<SPOUSE_TO_FAMILY_LINK>`>                  {0:M}`  
`          `**`+1 SUBM @`<XREF:SUBM>`@ {0:M}`**  
`          +1 <`<ASSOCIATION_STRUCTURE>`>                  {0:M}`  
`          +1 ALIA @`<XREF:INDI>`@                         {0:M}`  
`          `**`+1 ANCI @`<XREF:SUBM>`@ {0:M}`**  
`          `**`+1 DESI @`<XREF:SUBM>`@ {0:M}`**  
`          +1 <`<SOURCE_CITATION>`>                        {0:M}`  
`          +1 <`<MULTIMEDIA_LINK>`>                        {0:M}`  
`          +1 <`<NOTE_STRUCTURE>`>                         {0:M}`  
`          +1 RFN `<PERMANENT_RECORD_FILE_NUMBER>`         {0:1}`  
`          +1 AFN `<ANCESTRAL_FILE_NUMBER>`                {0:1}`  
`          +1 REFN `<USER_REFERENCE_NUMBER>`               {0:M}`  
`            `**`+2 TYPE `<USER_REFERENCE_TYPE>` {0:1}`**  
`          +1 RIN `<AUTOMATED_RECORD_ID>`                  {0:1}`  
`          +1 <`<CHANGE_DATE>`>                            {0:1}`  
`   `

- Linkit (submitter, ancestor interest ja descendent interest indicator) ohitetaan ilman ilmoitusta.
- Alias indikaattori ("Linkittää mahdollisesti samoja henkilöitä") talletetaan nimeltään 'Alias'.
- REFN ja REFN:TYPE talletetaan , mutta usean REFN:in tapauksessa ei välttämättä ole selvää, mikä TYPE liittyy mihinkin REFN:ään.

INDIVIDUAL_ATTRIBUTE_STRUCTURE:n käsittely on melko mutkikasta. Seuraavia tageja:

- EDUC (opillinen saavutus),
- NMR (avioiden lukumäärä),
- OCCU (ammatti),
- PROP (omistukset),
- RELI (uskontokunta),
- RESI (asuinpaikka) ja
- TITL (titteli)

käsitellään Grampsissa s ja niihin liittyvät tiedot talletetaan tapahtumarakenteeseen. Ylätason tagille (osoitettu yllä listassa suluilla) alisteiset tarkemmat tiedot talletetaan . TYPE tagia seuraava <EVENT_DESCRIPTOR> menee kuitenkin edelle jos <EVENT_DESCRIPTOR> ei ole attribuutin nimi.

Seuraavia tageja:

- CAST (kasti),
- DSCR (fyysinen kuvaus),
- INDO (kansallinen ID numero),
- NATI (kansanryhmä tai heimo),
- NCHI (lasten lukumäärä) ja
- SSN (sosiaaliturvatunnus)

käsitellään Grampsin ja ylätason tagille (osoitettu yllä listassa suluilla) alisteisia tarkempia tietoja lukuunottamatta ohitetuksi tulevat useimat kentät, lähde- ja lainaustiedot ja lisätietojen rakenneryhmä, kuten osoitetaan alla vahvennetulla tekstillä.

`   INDIVIDUAL_ATTRIBUTE_STRUCTURE: =`  
`        n  CAST `<CASTE_NAME>`                            {1:1}`  
`          +1 <`<EVENT_DETAIL>`>                           {0:1}`  
`             etc.`  
`   `  
`   EVENT_DETAIL: =`  
`        `**`n TYPE `<EVENT_DESCRIPTOR>` {0:1}`**  
`        `**`n DATE `<DATE_VALUE>` {0:1}`**  
`        `**`n <`<PLACE_STRUCTURE>`> {0:1}`**  
`        `**`n <`<ADDRESS_STRUCTURE>`> {0:1}`**  
`        `**`n AGE `<AGE_AT_EVENT>` {0:1}`**  
`        `**`n AGNC `<RESPONSIBLE_AGENCY>` {0:1}`**  
`        `**`n CAUS `<CAUSE_OF_EVENT>` {0:1}`**  
`        n  <`<SOURCE_CITATION>`>                          {0:M}`  
`          +1 <`<NOTE_STRUCTURE>`>                         {0:M}`  
`          +1 <`<MULTIMEDIA_LINK>`>                        {0:M}`  
`        `**`n <`<MULTIMEDIA_LINK>`> {0:M}`**  
`        n  <`<NOTE_STRUCTURE>`>                           {0:M}`  
`        `  
`        `

- Individual attribuutin rakenne, tyyppi, päivämäärä, paikkarakenne, osoiterakenne, ikä, agentti, syy ja multimedian linkit ohitetaan.

#### FAM_RECORD

FAM_RECORD talletetaan Grampsin (Family) tietueeksi.

`   FAM_RECORD:=`  
`        n @`<XREF:FAM>`@   FAM                            {1:1}`  
`          +1 <`<FAMILY_EVENT_STRUCTURE>`>                 {0:M}`  
`          +1 HUSB @`<XREF:INDI>`@                         {0:1}`  
`          +1 WIFE @`<XREF:INDI>`@                         {0:1}`  
`          +1 CHIL @`<XREF:INDI>`@                         {0:M}`  
`          +1 NCHI `<COUNT_OF_CHILDREN>`                   {0:1}`  
`          +1 SUBM @`<XREF:SUBM>`@                         {0:M}`  
`          +1 <`<LDS_SPOUSE_SEALING>`>                     {0:M}`  
`          +1 <`<SOURCE_CITATION>`>                        {0:M}`  
`          +1 <`<MULTIMEDIA_LINK>`>                        {0:M}`  
`          +1 <`<NOTE_STRUCTURE>`>                         {0:M}`  
`          +1 REFN `<USER_REFERENCE_NUMBER>`               {0:M}`  
`            +2 TYPE `<USER_REFERENCE_TYPE>`               {0:1}`  
`          +1 RIN `<AUTOMATED_RECORD_ID>`                  {0:1}`  
`          +1 <`<CHANGE_DATE>`>                            {0:1}`

- Linkki submitteriin ohitetaan ohitetaan ilman ilmoitusta.
- REFN ja REFN:TYPE talletetaan , mutta usean REFN:in tapauksessa ei välttämättä ole selvää, mikä TYPE liittyy mihinkin REFN:ään.

#### SOURCE_RECORD

SOURCE_RECORD talletetaan Grampsin (Source) tietueeksi, paitsi mitä on alla osoitettu vahvennetulla tekstillä.

`   SOURCE_RECORD:=`  
`        n @`<XREF:SOUR>`@ SOUR                            {1:1}`  
`          `**`+1 DATA {0:1}`**  
`            `**`+2 EVEN `<EVENTS_RECORDED>` {0:M}`**  
`              `**`+3 DATE `<DATE_PERIOD>` {0:1}`**  
`              `**`+3 PLAC `<SOURCE_JURISDICTION_PLACE>` {0:1}`**  
`            `**`+2 AGNC `<RESPONSIBLE_AGENCY>` {0:1}`**  
`            `**`+2 <`<NOTE_STRUCTURE>`> {0:M}`**  
`          +1 AUTH `<SOURCE_ORIGINATOR>`                   {0:1}`  
`            +2 [CONT|CONC] `<SOURCE_ORIGINATOR>`          {0:M}`  
`          +1 TITL `<SOURCE_DESCRIPTIVE_TITLE>`            {0:1}`  
`            +2 [CONT|CONC] `<SOURCE_DESCRIPTIVE_TITLE>`   {0:M}`  
`          +1 ABBR `<SOURCE_FILED_BY_ENTRY>`               {0:1}`  
`          +1 PUBL `<SOURCE_PUBLICATION_FACTS>`            {0:1}`  
`            +2 [CONT|CONC] `<SOURCE_PUBLICATION_FACTS>`   {0:M}`  
`          +1 TEXT `<TEXT_FROM_SOURCE>`                    {0:1}`  
`            +2 [CONT|CONC] `<TEXT_FROM_SOURCE>`           {0:M}`  
`          +1 <`<SOURCE_REPOSITORY_CITATION>`>             {0:1}`  
`          +1 <`<MULTIMEDIA_LINK>`>                        {0:M}`  
`          +1 <`<NOTE_STRUCTURE>`>                         {0:M}`  
`          +1 REFN `<USER_REFERENCE_NUMBER>`               {0:M}`  
`            +2 TYPE `<USER_REFERENCE_TYPE>`               {0:1}`  
`          +1 RIN `<AUTOMATED_RECORD_ID>`                  {0:1}`  
`          +1 <`<CHANGE_DATE>`>                            {0:1}`

- DATA siihen liittyvine tietoineen ohitetaan

#### REPOSITORY_RECORD

REPOSITORY_RECORD talletetaan Grampsin (Repository) tietueeksi, paitsi mitä alla osoitetaan vahvennetulla tekstillä.

`   REPOSITORY_RECORD: =`  
`        n @`<XREF:REPO>`@ REPO                            {1:1}`  
`          +1 NAME `<NAME_OF_REPOSITORY>`                  {0:1}`  
`          +1 <`<ADDRESS_STRUCTURE>`>                      {0:1}`  
`          +1 <`<NOTE_STRUCTURE>`>                         {0:M}`  
`          `**`+1 REFN `<USER_REFERENCE_NUMBER>` {0:M}`**  
`            `**`+2 TYPE `<USER_REFERENCE_TYPE>` {0:1}`**  
`          `**`+1 RIN `<AUTOMATED_RECORD_ID>` {0:1}`**  
`          +1 <`<CHANGE_DATE>`>                            {0:1}`

- REFN, REFN:TYPE ja RIN ohitetaan

#### MULTIMEDIA_RECORD

MULTIMEDIA_RECORD talletetaan Grampsin tietueeksi, paitsi mitä alla osoitetaan vahvennetulla tekstillä.

`   MULTIMEDIA_RECORD:=`  
`        n @`<XREF:OBJE>`@ OBJE                            {1:1}`  
`          +1 FORM `<MULTIMEDIA_FORMAT>`                   {1:1}`  
`          +1 TITL `<DESCRIPTIVE_TITLE>`                   {0:1}`  
`          +1 <`<NOTE_STRUCTURE>`>                         {0:M}`  
`          +1 <`<SOURCE_CITATION>`>                        {0:M}`  
`          `**`+1 BLOB {1:1}`**  
`            `**`+2 CONT `<ENCODED_MULTIMEDIA_LINE>` {1:M}`**  
`          +1 OBJE @`<XREF:OBJE>`@     /* chain to continued object */  {0:1}`  
`          `**`+1 REFN `<USER_REFERENCE_NUMBER>` {0:M}`**  
`            `**`+2 TYPE `<USER_REFERENCE_TYPE>` {0:1}`**  
`          `**`+1 RIN `<AUTOMATED_RECORD_ID>` {0:1}`**

- Oletaan 'FILE' tagin mukanaoloa osoittamaan multimedia-objektin tiedostoa. Tämä on GEDCOM 5.6.0 -version mukaista, mutta Gramps ei kuitenkaan tue GEDCOM 5.6.0:ssa mahdollisuutta useaan <MUTIMEDIA_FILE_REFN> viittauksiin eikä FILE gedcom riville alisteisia FORM, TYPE and TITL tietoja (myöhempi FILE voi kirjoittaa edellisen päälle - ilman virhetarkistusta).
- BLOB ohitetaan
- REFN, REFN:TYPE ja RIN ohitetaan

#### NOTE_RECORD

NOTE_RECORD talletetaan Grampsin tietueeksi, paitsi mitä alla osoitetaan vahvennetulla tekstillä.

`   NOTE_RECORD:=`  
`        n @`<XREF:NOTE>`@ NOTE `<SUBMITTER_TEXT>`           {1:1}`  
`          +1 [ CONC | CONT] `<SUBMITTER_TEXT>`            {0:M}`  
`          `**`+1 <`<SOURCE_CITATION>`> {0:M}`**  
`          `**`+1 REFN `<USER_REFERENCE_NUMBER>` {0:M}`**  
`            `**`+2 TYPE `<USER_REFERENCE_TYPE>` {0:1}`**  
`          `**`+1 RIN `<AUTOMATED_RECORD_ID>` {0:1}`**  
`          +1 <`<CHANGE_DATE>`>                            {0:1}`

- Lähde ja lainaus (source citation) ohitetaan
- REFN, REFN:TYPE ja RIN ohitetaan

## Tietojen vienti

![[_media/ExportAssistantStartFi-41.png|Kuva {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Vientiavustimen avausikkuna]]

![[_media/ExportAssistantChooseFi-41.png|Kuva {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Vientiavustin: Vientitiedoston muodon valintaikkuna]]

Tietojen viennillä voit jakaa sukupuusi minkä tahansa osan toisille tutkijoille ja siirtää sen myös toiseen tietokoneeseesi. Tällä hetkellä Gramps tukee seuraavia vientimuotoja: Gramps [XML](wiki:XML), GEDCOM, Gramps [XML](wiki:XML) Package, Web Family Tree, GeneWeb, ja CSV.

Tietojen viemiseksi valitse tai [pikavalinta](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings#) . Tämä käynnistää ikkunan. Sen sivujen kautta valitset muodon, tiedoston ja muotosidonnaiset muut ominaisuudet. Lopullisen vahvistuksen jälkeen vienti tapahtuu valintojesi mukaisesti. Milloin tahansa voit palata painikkeella ja muuttaa valintojasi ja sitten palata viennin uuteen toteutukseen.

Gramps tukee vientiä seuraavissa muodoissa:

- pilkkuerotettu laskentalomake (CSV)
- GEDCOM
- GeneWeb
- Gramps [XML](wiki:XML) (sukupuu)
- Gramps [XML](wiki:XML) paketti(sukupuu medioineen)
- Web Family Tree
- vCalendar
- vCard

#### Viennin lisävalinnat

![[_media/ExportAssistant-ExportOptions-CSV-defaults-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Viennin avustin - Viennin lisävalinnat - velho (näyttää oletukset CSV:lle korostettuna alaosan osio, jossa vaihtoehdot tiedostomuodolle]]

Säädettyäsi valintasi kahdessa osiossa:

- Yläosassa: [Suotimet ja yksityisyys](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees#Filters_and_privacy)
- Alaosassa: [Tiedostomuodon erityisvalinnat](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees#File_format_specific_export_options)

etene painikkeella. {{-}}

### Suotimet ja yksityisyys

Grampsilla voit viedä sukupuusi ulos tavanomaisiin tiedostomuotoihin .

Tarjolla on valintoja viennin täsmäsäätelyyn.

- Henkilöiden ja lisätietojen suotimet: Suotimilla voit rajata siirrettävien tietojen määrää, asettamiesi kriteerien perusteella.

###### Yksityisyyssuodin

Älä lisää tietoja, jotka on merkitty yksityisiksi: Valitse tämä estääksesi yksityiseksi merkittyjen tietojen kirjoitus siirtotiedostoon.

###### Elävien suodin

Valitse seuraavista:

- (oletus)

- 

- 

- 

Rajoita elossa olevien tietoja: Valitse tämä estääksesi elossa olevien henkilöiden tietojen kirjoitusta siirtotiedostoon. Tämän seurauksena kaikki henkilöiden syntymää, kuolemaa, osoitteita, merkittäviä tapahtumia koskevat tiedot jätetään pois siirtotiedostosta. Jos teet tämän valinnan, voit rajoittaa vielä lisääkin elossa olevien henkilöiden tietoja. Voit esim. korvata etunimen **Elossa** tekstillä ks. (see your [settings](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Text)); voit jättää lisätiedot pois ja ohittaa lähdetiedot, ks. [living people](wiki:Gramps_6.0_Wiki_Manual_-_Probably_Alive).

- Jätä pois henkilöön liittymättömät tiedot: Valitse tämä estääksesi valittuihin henkilöihin liittymättömien tietojen kirjoitus siirtotiedostoon.

Henkilön elossaolo ei ole joskus selkeästi pääteltävissä tiedoista. Gramps käyttää kehittynyttä algoritmia määrittelemään elossaoloa, ks. [if a person could still be alive](wiki:Gramps_6.0_Wiki_Manual_-_Probably_Alive). Muistathan, että Gramps tekee parhaan arvauksen muttei aina onnistu arvaamaan oikein. Tarkista velä kerran sukupuusi tiedot.

###### Henkilösuodin:

Valittavissa on vaihtoehdot:

- (oletus)

- 

- 

- 

- 

- Luo käyttäjän suodin valitsemalla *Päivitä kuvake* , jotta näet ikkunan.

###### Lisätietosuodin:

Valittavissa on vaihtoehdot:

- (oletus)

- Luo käyttäjän suodin valitsemalla *Päivitä kuvake* , jotta näet ikkunan.

###### Viitesuodin:

Valittavissa on vaihtoehdot:

- (oletus)

- 

##### Valitse vientimuoto

Riippuen valitusta tiedostomuodosta sinulla on käytettävissä joukko vaihtoehtoja, useat niistä on kuvattu "Suotimet ja tietosuoja" osiossa.

Tiedostomuotoja ovat:

- GEDCOM
- GEDCOM Laajennukset (GED2)
- GeneWeb
- Gramps XML (sukupuu)
- Gramps XML paketti (sukupuu medioilla)
- JSON Export
- Nettisukupuu (Web Family Tree ohjelmaan)
- CSV
- Prolog Export
- Raw Export
- SQLite Export
- vCalendar
- vCard

Katso erityisesti:

- [(CSV) pilkkuerotettu](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees#Comma_Separated_Values_Spreadsheet.28CSV.29_export)
- [Gramps XML (sukupuu)](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees#Gramps_XML_.28family_tree.29_export)

#### GeneWeb vienti

tallentaa datan erityisessä GeneWeb ohjelman muodossa, mutta sillä ei ole Grampsissa omia vientiehtoja.

GeneWebistä ja sen muodosta lisää tietoa:

- <http://www.geneweb.org>

{{-}}

### Gramps XML (sukupuu) vienti

![[_media/ExportAssistant-ExportOptions-GrampsXMLFamilyTree-defaults-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Vientiavustaja - Viennin valinnat - velho (näyttää oletusarvoilla "Gramps XML (sukupuu)") viennin, aliosiossa tiedostomuodon erityisvalinnat]]

vienti(.gramps): tämä on tietojenvaihdon ja varmuuskopioinnin vakiomuoto (tämä .gpkg päätteisen tiedostomuoto soveltuu täydellisesti tietojen vaihtoon, koska mediatiedostot ovat siinä mukana. Koska XML on tekstimuotoinen siitä voi silmämääräisesti varmistaa tietoja. Gramps takaa, että alemman Gramps version tuottaman .gpkg tiedoston voi aina tuoda ylempään Gramps version ei kuitenkaan päinvastaisessa suunnassa!).

Jos mediatiedostoa ei löydy viennissä, näet saman ikkunan kuin GEDCOM viennissä.

viennissä on huomioitava [tiedostomuodon erityiset valinnat](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees#File_format_specific_export_options):

- Tiivistä (kompressoi)

{{-}} Mukana viennissä ei ole:

- Raporttien käyttäjäasetukset.
- Käyttäjäsuotimet.
- Mitkään tekemäsi muutokset [<code>gramp.ini</code>](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees#Advanced_settings) tiedostoon

{{-}}

### Gramps XML paketti(sukupuu medioilla) vienti

vienti(.gpkg): Gramps paketti muoto tuottaa tiivistetyn tiedoston, jossa on Gramps XML sukupuu ja kaikkien liittyvien mediatiedostojen kopiot. Tämä soveltuu siihen, jos siirrät sukupuusi toiseen tietokoneeseen tai jaat sen toiselle henkilölle.

Jos mediatiedostoa ei löydy viennissä, näet saman ikkunan kuin GEDCOM viennissä.

.gpkg viennissä ei ole muita tiedoston muotoon liittyviä valintoja.

Mukana viennissä ei ole:

- Raporttien käyttäjäasetukset.
- Käyttäjäsuotimet.
- Mitkään tekemäsi muutokset [<code>gramp.ini</code>](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees#Advanced_settings) tiedostoon

{{-}}

### Web Family Tree vienti

vienti tuottaa tekstitiedoston, jota käyttää **Web Family Tree** ohjelma. Saat siitä lisää tietoja

- <http://www.simonward.com/cgi-bin/page.pl?family/tree>

.gpkg viennissä ei ole muita tiedoston muotoon liittyviä valintoja.

{{-}}

### vCalendar vienti

tallentaa sukupuun monen kalenteriohjelman tiedostomuodossa. Joskus sen nimi on PIM for Personal Information Manager.

vCalendar muodosta lisää:

- <https://en.wikipedia.org/wiki/ICalendar#vCalendar_1.0>

vCalendar viennissä ei ole muita tiedoston muotoon liittyviä valintoja. {{-}}

### vCard vienti

tallentaa tiedot monen osoitekirja-sovelluksen käyttämässä muodossa.

Lisää vCard muodosta:

- <https://en.wikipedia.org/wiki/VCard>

vCard viennissä ei ole muita tiedoston muotoon liittyviä valintoja. {{-}}

## Vahvista tiedot

![[_media/ExportAssistant-FinalConfirmation-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Vientiavustaja - Vahvista tiedot - velho - esimerkki]]

Vientiavustajan velholla voit varmistaa vietävän tiedoston yhtenvetotiedot muodosta, Nimestä ja kansiosta.

Tässä vaiheessa painat vaihtaaksesi valintojasi tai hylätäksesi kokonaan viennin.

tai valitse painiketta jatkaaksesi vientiä. {{-}}

## Valitse talletettava tiedosto

![[_media/ExportAssistant-SelectSaveFile-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Vientiavustaja - Valitse talletettava tiedosto - velho - esimerkki]]

Sitten jatka painikkeella.

Jos sinulla ei ole kirjoitusoikeuksia em. vientikansioon, näet varoituksen ja sitten Vientiavustajan ikkunan Assistants ikkunan, jolloin valitse painike ja ala vienti uudelleen sopivaan kansioon. {{-}}

## Yhteenveto

![[_media/ExportAssistant-YourDataHasBeenSaved-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Vientiavustaja - Yhteenveto- velho - esimerkki]]

Vientiavustajan velho näyttää Tiedostonimi:'' ja vahvistaa tietojen viennin onnistumisen.

Valitse painike poistuaksesi Vientiavustajasta.

{{-}}

### Vienti GEDCOM muotoon

Sukupuun tiedot voi viedä Grampsilla GEDCOM-muotoiseen tiedostoon. Vientiä ohjataan valinnoilla (katso [Fig.x.x. Vienti gedcom-muotoon-fig](wiki:Media:ExportAssistantGEDCOM-ExportOptionsFi-41.png) ).

- Suodin: Suodattamalla saat vientiin mukaan vain ne tiedot, jotka ovat suodatusehtojen mukaiset.

<!-- -->

- Kohde: Vaikka GEDCOM ymmärretään standardiksi, sitä noudatetaan eri ohjelmissa vaihtelevalla tavalla. Tämä voi johtaa tietojen menetyksiin siirrossa. Gramps voi pienentää menetyksiä joissakin tapauksissa. Voit kertoa Grampsille, mikä on tiedot vastaanottava sovellus ja Gramps mukauttaa vientiä tämän ohjelman mukaan. Jos vastaanottavaa ohjelmaa ei ole Grampsin ao.ohjelmalistassa, valitse "GEDCOM 5.5 Standard".

- Yksityiset tiedot ohitetaan: Rastita tämä vaihtoehto, jotta yksityisiksi merkityt tiedot eivät tule mukaan vientiin.

<!-- -->

- Rajoita elossa olevien tietoja: Rastita tämä vaihtoehto, jotta elossa olevienhenkilöiden tietoja rajoitetaan viennissä. Tämän seurauksena henkilöiden syntymään, kuolemaan,osoitteeseen, merkittäviin taphtumiin liittyviä tietoja ei otetan mukaan siirtotiedostoon. Tässä vaihtoehdossa on lisävalintoja tietojen edelleen rajoittamiseksi. Voit esim.valita henkilön etunimen vaihdettavaksi "Elossa" vakiotiedolla, tai jättää pois lisätiedot ja lähteet, jotka on liitetty elossa olevaan henkilöön.

Joskus ei ole ilmeistä, onko joku henkilö elossa. Gramps käyttää kehittynyttä algoritmia tämän päättelemisesksi. Muista, Gramps tekee arvauksensa parhaan taitonsa mukaan ja arvaus ei aina osu oikeaan. Tarkista toisensa kerran tiedot, jotka olet luovuttamassa GEDCOM:n kautta.

- Viite kuvien polkuun: Rastita tämä vaihtoehto, jotta Gramps kirjoittaisi kuvillesi tietyn saantipolun.

Tämä vaihtoehto sallii määrittää, missä kuvasi sijaitsevat. Tämä on hyödyllistä siirrettäessä GEDCOM-tiedosto koneelta toiselle. Vastaanottava sovellus saa näin tiedon, missä sukupuuhun liittyvät kuvat ovat.

### Muihin muotoihin vienti

- Web Family Tree: Vienti Web Family Tree muotoon luo tekstitiedoston, jota Web Family Tree ohjelma voi käyttää. Viennin valinnoissa on suotimenvalinta ja elävien ihmisten tietojen rajoittaminen heidän sukuyhteyksissään.

<!-- -->

- GeneWeb: Vienti GeneWeb muotoon kopioi tietosi suosittuun muotoon käytettäväksi netissä. Tästä muodosta enemmän <http://cristal.inria.fr/~ddr/GeneWeb/en/>.

<!-- -->

- vCalendar ja vCard: Vienti vCalendar tai vCard muotoon tallentaa tiedot muotoon, jota käyttävät monet kalenteri- ja kontaktihenkilösovellukset, joskus tunnettuja myös nimellä PIM (Personal Information Manager).

<!-- -->

- Gramps CSV Spreadsheet format: Gramps tietojesi rajoitettu vienti (ja tuonti) yksinkertaiseen laskentataulukon muotoon. Ks. lisätietoja [CSV Import and Export](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees:_CSV_Import_and_Export). Myös ks. [Export Display](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Export_the_screen).

{{-}}

[Category:Fi:Dokumentaatio](wiki:Category:Fi:Dokumentaatio)
