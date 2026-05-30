---
title: Gramps 6.0 Wiki Manual - Plugin Manager/sk
categories:
- Plugins
- Sk:Documentation
managed: false
source: wiki-scrape
wiki_revid: 115703
wiki_fetched_at: '2026-05-30T20:09:55Z'
lang: sk
---

{{#vardefine:chapter\|11}} {{#vardefine:figure\|0}} Správca zásuvných modulov je dostupný v ponuke . Mnohé funkcie Správcu zásuvných modulov sú určené pre vývojárov a dialógové okná opísané nižšie sú tie, ktoré vidia vývojári. Funkcie pre bežných používateľov sú uvedené nižšie, ak sa líšia.

Program Gramps zisťuje, či je spustený v režime používateľa alebo vývojára, pomocou príznaku "optimalizovať":

- `python -O gramps.py`

Pozri [Ladenie programu Gramps](wiki:Ladenie_programu_Gramps).

Gramps sa skladá z jadra a mnohých zásuvných modulov. Pri spustení programu Gramps sa načíta jadro a načíta sa len obmedzený počet zásuvných modulov. Tým sa znižuje čas spustenia a pamäťové nároky programu Gramps. Následne sa mnohé zásuvné moduly automaticky načítajú systémom Gramps, keď sú potrebné, takže mnohí používatelia nebudú musieť vedieť o existencii zásuvných modulov alebo o ich oneskorenom načítaní.

Správca zásuvných modulov umožňuje ovládať, ako Gramps spravuje zásuvné moduly.

## Typy zásuvných modulov

V programe Gramps existujú dve hlavné kategórie zásuvných modulov: "používateľské zásuvné moduly" a "systémové zásuvné moduly". Používateľské zásuvné moduly sú tie, ktoré používate a ovládate, aby vám poskytovali rôzne funkcie. Systémové zásuvné moduly používa program Gramps.

V programe Gramps sa nachádzajú tieto typy **používateľských zásuvných modulov**:

1.  doc creators (tvorcovia dokumentov): Backendy, pre ktoré môže Gramps písať správy (pdf, odf, ascii text, ...)
2.  exportéry: formáty exportu, do ktorých môžete exportovať svoje údaje prostredníctvom ponuky
3.  gramplety: malé programy, ktoré môžete vložiť do pohľadu Informačný panel alebo odpojiť a používať ako bežné okno
4.  gramplety pohľadov: pohľady viditeľné v hlavnom okne programu Gramps
5.  importéry: importné formáty, z ktorých môže Gramps importovať údaje prostredníctvom ponuky
6.  mapová služba: ciele, ktoré možno použiť v pohľade miesta na prechod na internetovú mapovú službu (*Ísť* tlačidlo na paneli nástrojov)
7.  quickreport (rýchle prehľady): známe ako *Quick Views* (rýchle prehľady), sú to malé prehľady, ktoré sú k dispozícii v kontextovej ponuke na zoznamových prehľadoch alebo prostredníctvom grampletu Quick View (rýchleho prehľadu)
8.  reporty: Sú to textové alebo grafické prehľady, ktoré dokáže Gramps vytvoriť
9.  nástroje: Nástroje, ktoré môžete spustiť prostredníctvom ponuky

V programe Gramps sa nachádzajú nasledujúce typy **systémových zásuvných modulov**:

1.  databáza: Backendy, ktoré umožňujú programu Gramps podporovať [alternatívne typy databáz](wiki:Gramps_6.0_Wiki_Manual_-_Settings/sk#Rodinný_strom).
2.  plugin libs: Prítomné knižnice, ktoré poskytujú ďalšie funkcie.
3.  vzťahy: kalkulátory vzťahov pre rôzne jazyky
4.  Pravidlo (zavedené v programe Gramps 6.0.x a vyššej verzii)

Existuje mnoho zásuvných modulov, ktoré sa dodávajú s programom Gramps. Každý však môže napísať zásuvný modul a zdieľať ho. Tieto zásuvné moduly tretích strán sa nazývajú "doplnky". Veľmi odporúčame používateľom a vývojárom, aby sa o svoje výtvory podelili s ostatnými používateľmi programu Gramps.

## Registrácia a načítanie

Zásuvné moduly sú buď uložené lokálne v počítači a Gramps o nich vie, keď sa hovorí, že sú **Registrované**, alebo sú uložené na vzdialenom počítači a Gramps pozná len ich názov, typ a popis, keď sa hovorí, že sú **Doplnky**.

Pri spustení programu Gramps sa automaticky načítajú informácie o miestnych doplnkoch, takže sa stanú registrovanými. Správca zásuvných modulov sa môže použiť na stiahnutie vzdialených doplnkov, aby sa tiež zaregistrovali.

Registrované (t. j. lokálne) doplnky sú **načítané** programom Gramps v nasledujúcich situáciách:

1.  sú automaticky načítané pri spustení. Niektoré typy zásuvných modulov sa načítajú pri spustení (napr. neskryté pohľady), niektoré zásuvné moduly môžu mať príznak, ktorý vynúti načítanie pri spustení,
2.  sú automaticky načítané na základe toho, že používateľ klikne na zobrazenie alebo požiada o správu,
3.  sa načítajú tak, že používateľ výslovne požiada o načítanie v správcovi zásuvných modulov,
4.  vzdialené zásuvné moduly sa načítajú súčasne s ich registráciou pomocou [Install Addons](wiki:6.0_Addons#Installing_Addons_in_Gramps) v záložke **Všeobecné** v .

## Skrytie/odkrytie

Správca zásuvných modulov sa dá použiť na skrytie alebo odkrytie zásuvných modulov. V niektorých ponukách sa skryté doplnky nezobrazia, takže doplnok nie je možné vybrať. Ak je napríklad Gramplet skrytý, nezobrazí sa v kontextovej ponuke "Pridajte gramplet", ktorá sa zobrazí po kliknutí pravým tlačidlom myši na pozadí hlavnej karty Gramplety. Skrytie niektorých doplnkov (napríklad Vzťahov alebo Pohľadov Gramps) však nemá žiadny účinok a nemusí byť ani povolené.

## Akcie

Pre existujú dve záložky:

- a

- 

### Registrované zásuvné moduly

![[_media/PluginManager-RegisteredPlugins-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Registrované zásuvné moduly]]

Tu vidíte zoznam všetkých zásuvných modulov, ktoré našiel Gramps. Ide o zásuvné moduly, ktoré sú súčasťou programu Gramps, ako aj o zásuvné moduly nájdené v adresári `gramps51/plugins` v rámci [Adresára používateľov programu Gramps](wiki:Gramps_6.0_Wiki_Manual_-_User_Directory/sk). Typ zásuvného modulu je uvedený v prvom stĺpci.

Zásuvný modul môžete zobraziť alebo skryť tak, že vyberiete riadok a stlačíte tlačidlo . Toto je užitočné len pre zásuvné moduly používateľov.

Výberom riadku a dvojitým kliknutím alebo stlačením tlačidla sa zobrazí dialógové okno.

{{-}}

### Načítané zásuvné moduly

![[_media/PluginManager-LoadedPlugins-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Načítané zásuvné moduly]]

Tu sa zobrazí zoznam všetkých zásuvných modulov, ktoré sa pokúsili načítať. Za normálnych okolností sa načítajú všetky pohľady (ako napríklad Pohľad Vzťah) a automaticky sa načítajú všetky gramplety/správy/nástroje, ktoré ste použili.

Ak počas načítania zásuvného modulu došlo k chybe, na tejto karte sa zobrazí stĺpec **Stav**. Dvojitým kliknutím na riadok zobrazujúci chybu sa otvorí dialógové okno zobrazujúce podrobne chybu. Môžete ho použiť na kontaktovanie autora zásuvného modulu alebo zoznamu chýb programu Gramps.

Ak sa neskôr rozhodnete, že sa vám doplnok nepáči, môžete ho označiť ako "skrytý" a už sa nebude zobrazovať.

Doplnok môžete zobraziť alebo skryť tak, že vyberiete riadok a stlačíte tlačidlo . Toto je užitočné len pre používateľské doplnky.

Výberom riadku a stlačením tlačidla sa zobrazí dialógové okno .

{{-}}

## Dialógové okno Podrobné informácie

![[_media/Detailed-Info-dialog-plugin-example-with-context-menu-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Podrobné informácie - dialóg - príklad]]

V dialógovom okne sa zobrazia informácie o vybranom zásuvnom module/doplnku. Môžete ho použiť na kontaktovanie autora zásuvného modulu alebo zoznamu chýb programu Gramps.

- Názov zásuvného modulu:
- Popis
- Verzia:
- Autori:
- E-mail:
- Názov súboru:
- Umiestnenie:

{{-}}

[Category:Sk:Documentation](wiki:Category:Sk:Documentation) [Category:Plugins](wiki:Category:Plugins)
