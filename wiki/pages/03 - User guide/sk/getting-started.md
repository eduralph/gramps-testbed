---
title: Gramps 6.0 Wiki Manual - Getting started/sk
categories:
- Sk:Documentation
managed: false
source: wiki-scrape
wiki_revid: 112649
wiki_fetched_at: '2026-05-30T20:06:14Z'
lang: sk
---

{{#vardefine:chapter\|2}} {{#vardefine:figure\|0}} V tejto časti začneme so základmi. Najprv si popíšeme základné pojmy v programe Gramps. Potom vám ukážeme, ako spustiť program Gramps a ako získať pomoc, keď ju budete potrebovať. \_\_FORCETOC\_\_

## Prehľad Gramps

Gramps je bezplatný program s otvoreným zdrojovým kódom, ktorý bol navrhnutý ako flexibilný a výkonný genealogický nástroj. Je to rámec na zhromažďovanie genealogických údajov, zaznamenávanie vzájomných vzťahov medzi jednotlivými údajmi a prezentáciu týchto vzťahov.

Gramps sa dá vo všeobecnosti používať ľubovoľným spôsobom. Neexistuje jediný správny spôsob práce s údajmi alebo ich zaznamenávania. Ak však chcete spolupracovať s inými bádateľmi alebo programami, pomôže vám dodržiavať niektoré spoločné zásady. Aj keď poznáte bežné postupy genealogického výskumu, musíte pochopiť, ako program Gramps funguje. Potom sa môžete vrhnúť na to, ako používať program Gramps spôsobom, ktorý dopĺňa konkrétny štýl genealogického výskumu.

Program Gramps rozdeľuje všetky genealogické informácie do 9 základných kategórií položiek:

- [Ľudia](wiki:Gramps_Glossary#osoba)

- [Rodiny](wiki:Gramps_Glossary#rodina)

- [Udalosti](wiki:Gramps_Glossary#udalosť)

- [Miesta](wiki:Gramps_Glossary#miesto)

- [Poznámky](wiki:Gramps_Glossary#poznámka)

- [Médiá](wiki:Gramps_Glossary#médium)

- [Citácie](wiki:Gramps_Glossary#citácia)

- [Zdroje](wiki:Gramps_Glossary#zdroj)

- [Archívy](wiki:Gramps_Glossary#archív)

Každá z nich sa skladá zo samostatných položiek. To znamená, že do rodinného stromu môžete zadávať po jednej položke a v ľubovoľnom poradí. Jednotlivé položky môžete navzájom prepojiť alebo ich nechať nespojené (alebo dokonca chaoticky neusporiadané), ale vyhľadateľné. Alebo môžete začať s premysleným návrhom stromu a napĺňať ho smerom von, pričom budete pripájať nové položky priebežne.

Napríklad môžete chcieť najprv zadať jednotlivé položky Osoba a neskôr ich prepojiť vytvorením položiek Rodiny. Alebo môžete začať s Rodinou, ukotviť rodinu pridaním novej Osoby ako potomka alebo rodiča a potom pridať príbuzných, udalosti & zdrojové materiály do pripravených slotov rámca Rodiny. Alebo môžete začať s položkami zdrojov a položku Osoba vytvoriť až vtedy, keď váš výskum obsahuje zmienku o niekom. Alebo môžete tieto štýly zadávania údajov kombinovať tak, že pridáte niektoré položky Poznámka a Zdroj, potom položky Rodina a neskôr sa vrátite k položkám Poznámky a Zdroje. Stručne povedané, genealogický výskum si môžete robiť, ako chcete.

Ak máte ďalšie otázky, Gramps má komunitu používateľov a vývojárov. K dispozícii je [FAQ](wiki:Gramps_6.0_Wiki_Manual_-_FAQ/sk). (zoznam často kladených otázok); [mailing list](wiki:Contact#Mailing_lists); [sledovanie chýb, požiadaviek na funkcie a problémov](wiki:Using_the_bug_tracker); a môžete komunikovať pomocou on-line [chatovacích miestností](wiki:Contact#Chat_Room) alebo [komunitných fór](wiki:Contact#Forum).

### Pripojenia

Týchto 9 základných položiek je prepojených viacerými spôsobmi. Niektoré z týchto spojení sú udržiavané implicitne. Napríklad pridaním položky Osoba k položke Rodina ako rodiča alebo potomka sa automaticky vytvorí špeciálne spojenie nazývané **Odkaz**. Rodiny, ku ktorým je osoba pripojená, môžete vidieť na karte Odkazy v hlavnom okne Osoba. V programe Gramps sa tieto prepojenia vizualizujú aj mnohými ďalšími spôsobmi vrátane pohľadu Vzťah.

Aby sa informácie neopakovali, program Gramps umožňuje opakovane používať alebo zdieľať položky. Ide tiež o špeciálne spojenia, ktoré sa nazývajú **linky**. Napríklad položka Osoba môže byť prepojená s ľubovoľným počtom položiek Poznámka. Ak sa v poznámke spomínajú dvaja rôzni ľudia, potom môže mať zmysel zdieľať túto jedinú poznámku s oboma položkami ľudí.

Niektoré prepojenia obsahujú samotné informácie. Napríklad môžete prepojiť osobu so svadobnou udalosťou iného páru, napríklad preto, že osoba bola svedkom na ich svadbe. Manžel a manželka sú však prepojení so svadobnou udalosťou v **primárnej** roli, zatiaľ čo svedok plní inú rolu, napr. ako **svedok**. Tento typ informácie sa uchováva na samotnom prepojení vo vlastnosti roly.

### Ochrana osobných údajov

Program Gramps podporuje dva rôzne spôsoby ochrany súkromia citlivých údajov vo vašom rodinnom strome. Tieto metódy sa používajú pri zdieľaní vašich údajov s inými ľudmi, a to buď prostredníctvom vytvorenia správy, exportu údajov alebo vytvorenia webovej stránky.

Prvá metóda chráni informácie o ľuďoch, o ktorých sa Gramps domnieva, že sú nažive. Ak ste výslovne neoznačili, že osoba je mŕtva (pridaním udalosti úmrtia k položke Osoba), Gramps má sofistikovanú, automatickú funkciu na určenie, či je niekto nažive. Pri použití tejto metódy sú citlivé údaje žijúcich ľudí redigované. Napríklad osoba s menom "Smith, John" by sa mohla zobraziť ako "Smith, \[Žijúci\]".

Druhým spôsobom ochrany súkromia je zreteľná [vlajka "súkromia"](wiki:Gramps_Glossary#private_tag), ktorú môžete nastaviť na každej položke. Napríklad v poznámke môžete mať citlivé, osobné informácie. Ak takúto poznámku označíte ako súkromnú, potom sa táto poznámka nebude zobrazovať v textových a opisných správach alebo exportoch. Taktiež si uvedomte, že niektoré odkazy môžu byť označené ako súkromné. To je užitočné, ak chcete označiť prepojenie napríklad od osoby k udalosti ako súkromné, ale osoba a udalosť budú stále dostupné v správe, exporte alebo na webovej stránke.

![[_media/Include-data-marked-private-checkbox-example-60.png|Obrázok {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Prepísanie ochrany osobných údajov pre správy]]Aby ste mohli aktivovať tieto dva spôsoby ochrany súkromia, budete musieť pri vytváraní niektorých správ alebo pri exporte údajov uviesť ich použitie. {{-}}

### GEDCOM

Program Gramps odvodzuje svoju základnú štruktúru položiek zo štandardu nazývaného GEDCOM. Gramps však tento štandard rozširuje tam, kde to bolo považované za potrebné. Ak plánujete používať svoje rodinné údaje s iným systémom, ktorý používa GEDCOM, potom sa pravdepodobne budete chcieť pokúsiť obmedziť používanie funkcií, ktoré sú rozšíreniami len pre Gramps. Na druhej strane, ak nie ste obmedzení iným genealogickým softvérom, potom môžete svoje údaje zadávať akýmkoľvek spôsobom, ktorý vám dáva zmysel.

Podrobnejšie informácie o tejto problematike si môžete prečítať v časti [Gramps a GEDCOM](wiki:Gramps_and_GEDCOM).

## Spustenie Gramps

Najlepší spôsob, ako sa naučiť Gramps, je pracovať s vašimi údajmi. Začnime!

Spôsob spustenia programu Gramps závisí od operačného systému, ktorý používate.

Okrem spustenia programu Gramps pomocou bežného grafického používateľského rozhrania (GUI), ako je opísané nižšie, je možné spustiť program Gramps aj pomocou rozhrania príkazového riadka (CLI). Použitím CLI možno vytvárať zostavy, ktoré nie sú dostupné prostredníctvom grafického rozhrania, možno ho použiť na vytváranie správ, vykonávanie konverzií atď. bez otvorenia okna a v prípade problémov môže poskytnúť [extra informácie](wiki:Gramps_6.0_Wiki_Manual_-_Error_and_Warning_Reference/sk#Zobrazenie_všetkých_chybových_správ). Ďalšie informácie nájdete v [prílohe Príkazový riadok](wiki:Gramps_6.0_Wiki_Manual_-_Command_Line/sk).

### Linux

Oficiálne je podporovaná iba platforma Linux, pretože vývojári programu Gramps používajú a testujú zdrojový kód na tejto platforme a opravujú všetky problémy, ktoré vzniknú v dôsledku aktualizácií.

Za predpokladu, že ste pre svoju distribúciu Linuxu použili štandardného správcu balíkov (buď prostredníctvom CLI, alebo grafického rozhrania), spustíte Gramps bežným spôsobom pre svoju distribúciu. Napríklad v Ubuntu 18.04 je ikona umiestnená v spúšťacom programe alebo program môžete spustiť z Dash. V prípade iných distribúcií sa môže vytvoriť položka v ponuke aplikácií (zvyčajne v časti **Office**).

Spustenie programu Gramps prostredníctvom CLI v systéme Linux je popísané [tu](wiki:Gramps_6.0_Wiki_Manual_-_Command_Line/sk#Linux).

### MS Windows

MS(Microsoft) Windows je [komunitou podporovaná](wiki:Download#MS_Windows) platforma. Ak si nainštalujete [Windows AIO](wiki:All_In_One_Gramps_Software_Bundle_for_Windows) GrampsAIO32 alebo GrampsAIO64 spustiteľný súbor, potom sa na plochu umiestni ikona, ako aj položka v ponuke "Štart" a kliknutím na ňu spustíte program Gramps.

Spustenie programu Gramps prostredníctvom CLI v systéme MS Windows je popísané [tu](wiki:Gramps_6.0_Wiki_Manual_-_Command_Line/sk#MS_Windows).

Existujú aj iné spôsoby inštalácie programu Gramps pre MS Windows, ale tie sú oveľa zložitejšie a nie sú tu uvedené.

### Mac OS X

Apple Mac OS X (MacOS) je [komunitou podporovaná](wiki:Download#Mac_OS_X) platforma. Ak si stiahnete obraz disku Mac OS X (.dmg), potom jednoducho pretiahnete aplikáciu do priečinka aplikácií (alebo kamkoľvek inam, kde ju chcete uložiť) a spustíte Gramps dvojitým kliknutím na aplikáciu bežným spôsobom.

Spustenie programu Gramps prostredníctvom CLI v systéme Mac OS X je popísané [tu](wiki:Gramps_6.0_Wiki_Manual_-_Command_Line/sk#Mac_OS_X).

Existujú aj iné spôsoby inštalácie programu Gramps pre Mac OS X, ale tie sú oveľa zložitejšie a nie sú tu opísané.

## Výber rodinného stromu

![[_media/Dashboard-category-view-first-open-no-family-tree-loaded-52-sk.png|Fig {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Pohľad kategórie na informačnom paneli - prvé otvorenie programu Gramps bez načítaného rodinného stromu(Gramps 6.0.0; MS-Windows 10)]]

Ak sa program Gramps spustí bez vybratého rodinného stromu, úvodná obrazovka bude mať málo funkcií. Väčšina operácií nebude k dispozícii. Ak chcete načítať rodinný strom (označovaný aj ako *databáza*), výberom v ponuke otvorte správcu rodinných stromov alebo kliknite na ikonu na paneli nástrojov. Program Gramps sleduje vaše nedávno otvorené Rodinné stromy, ktoré môžete vybrať kliknutím na šípku vedľa tlačidla a výberom z rozbaľovacej ponuky.

Podrobnejšie informácie o správcovi rodinných stromov a ponuke Rodinné stromy nájdete v kapitole venovanej tejto problematike: [Správa rodinných stromov](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees/sk).

{{-}}

## Povedzte mi, ako začať hneď teraz!

Odporúčame všetkým, aby si prečítali príručku a dozvedeli sa všetko o používaní programu Gramps. Genealógia si vyžaduje čas, takže učenie sa nástrojov nie je stratený čas.

Ak však chcete na začiatok získať naozaj len minimum informácií, prečítajte si toto:

- [Gramps 6.0 Wiki Manual - Zadávanie a úprava údajov: stručne](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_brief/sk)
- [How-To start with Genealogy using Gramps](wiki:Start_with_Genealogy).

## Získanie pomoci

Gramps má ponuku , do ktorej môžete kedykoľvek nahliadnuť.

- Pozrite si časť .

{{-}}

[Category:Sk:Documentation](wiki:Category:Sk:Documentation)
