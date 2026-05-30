---
title: Fi:Gramps 6.0 Wiki-käyttöohje - Todennäköisesti elossa
categories:
- Fi:Dokumentaatio
managed: false
source: wiki-scrape
wiki_revid: 120645
wiki_fetched_at: '2026-05-30T18:32:52Z'
lang: fi
---

{{#vardefine:chapter\|5}} {{#vardefine:figure\|0}} Tieto henkilöiden elossa olemisesta Grampsin sukupuussa on tärkeää, kun haluat jakaa tietojasi toisten kanssa mutta samalla suojella elossa olevien henkilöiden yksityiskohtaisia tietoja. Elossa olemista hyödynnetään myös joissakin raporteissa. Gramps tarjoaa tästä syystä joitakin työkaluja auttamaan sinua sen päättelemisesssä, onko joku henkilö elossa. Työkaluja kuvataan seuraavaksi.

## Kuinka Gramps tietää henkilön olevan elossa?

Yksinkertainen tapa on tarkistaa, löytyykö henkilöstä kuolintietoa tai siihen liittyvää tapahtumaa kuten hautaustietoa. Kuitenkin on todennäköistä, että tietokannassasi ole useinkaan näitä tapahtumia, koska sinulla ei ole mitään tietoa monien henkilöiden kuolemasta. Jos sinulla on tämä tieto, saattaa ola hyvä ajatus rekisteröidä hänelle kuolintapahtuma. Voit lisätä myös hyödyllisiä tietoja kuten päiväyksen ja tapahtumapaikan, kun saat ne tietää. Pelkän tapahtumankin lisääminen ilman tarkkoja tietoja on hyödyksi. Gramps voi myös lisätä tapahtumia puolestasi, arvioiduilla päiväyksillä tai ilman niitä (kuvattu jäljempänä).

Vaatimus rekisteröidä manuaalisesti kaikille henkilöille kuolintapahtuma (jotta heitä ei pidettäisi elossa oleviksi) olisi hyvin työlästä---tieto olisi lisätty suurelle joukolle henkilöille. Tavoitehan on suojata elossa olevien tietoja niiden luovutuksessa ja tulostuksesssa. Grampsissa onkin toiminto henkilön todennäköisen elossa olemisen laskemiseksi, perustuen hänen itsensä muihin tapahtumiin tai häneen suhteessa olevien muiden henkilöiden tapahtumien päivämääriin. Gramps tutkii henkilön vanhempia, lapsia ja sisaruksia, ja jatkaen heistä samaten eteenpäin, kunnes löytyy jotain näyttöä kuolemasta - tai sukujohdot päättyvät. Tyypillisestä iän tai elinkaaren keston perusteella (kuten ikäeroista sisarusten välillä, ensisynnyttäjän iästä jne) Gramps arvaa onko henkilö elossa vai ei. Menettely voi vaatia paljon aikaa mutta on sangen hyödyllinen. Tyypilliset arvot synnytysiälle, sukupolvien eroille jne voidaan antaa valikossa.

Elossaolo-toiminto voi tarkistaa,oliko henkilö elossa tiettynä hetkenä tai aikavälinä. Toiminto on käytössä Ikä tiettynä päivänä grampletissa, kuvattu alla. Tavallisesti ohjelma arvoi syntymä- ja kuolintapahtumat ja katsoo, sattuuko jokin päivämäärä niiden väliin.

Huomaa erityinen tilanne: jos haet "tänään" todennäköisesti elossa olevia ja henkilöllä on kuolintapahtuma, hänet tulkitaan kuolleeksi, vaikkei kuolinpäivää ole annettuna. Saat siksi eri tulokset, jos haet "eilen" (tai "vuosi sitten") todennäköisesti elossa olevia verrattuna siihen, keitä pidetään "tänään" todennäköisesti elossa oleviksi. Ethän tiedä kuolintapahtuman ajankohtaa.

Työkalulla "Laske arvioidut päivämäärät" saat perustelut, miksi Gramps arvioi henkilön olevan elossa tai kuolleen. Työkalu näyttää arvioidut syntymä- ja kuolinajat ja suhteen toiseen henkilöön, jonka johonkin tapahtumapäivään ne perustuvat.

## Todennäköisesti elossa proxy

Ensimmäinen työkalu on "Todennäköisesti elossa" proxy. Sitä käytetään automaattisesti aina kuten viet tietojasi muodossa, jossa on mahdollista rajoittaa elossa olevien henkilöiden tietoja. Proxy (edusohjelma) ei päästä lävitseen sukupuun elossa olevien henkilöiden arkoja tietoja kuten heidän etunimeään tai heidän tapahtumiaan.

## Ikä tiettynä päivänä Gramplet

Katso [Age on Date gramplet](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Age_on_Date_Gramplet).

## Kalenteri Gramplet

Katso [Calendar gramplet](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Calendar_Gramplet).

## Todennäköisesti elossa suodin

"Tänään" on päivämääränä käsitelty erityisesti tapahtumissa, joissa ei ole päivämäärää, ja tutkittaessa elossa oloa menneisyydessä. Esimerkiksi, jos henkilön kuolintapahtumassa ei ole päivämäärää, tiedämme henkilön olevan kuollut tänään ja aina tulevaisuudessa. Kuitenkin, käytettävissä olevat toiminnallisuudet eivät todenna, oliko henkilö elossa jonakin päivänä menneisyydessä. Niinpä päivämäärättömästä kuolintapahtumasta ei voida päätellä, mikä oli eilen henkilön elossaolon tila.

## Laskemalla arvioitujen päivämäärien työkalu

See [Calculate Estimated Dates addon](wiki:Addon:Calculate_Estimated_Dates).

{{-}}

[Category:Fi:Dokumentaatio](wiki:Category:Fi:Dokumentaatio)
