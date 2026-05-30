---
title: Gramps 6.0 Wiki Manual - What's new?/sk
categories:
- Sk:Documentation
managed: false
source: wiki-scrape
wiki_revid: 111411
wiki_fetched_at: '2026-05-30T20:25:44Z'
lang: sk
---

V tejto časti je uvedený prehľad zmien od verzie 5.0 programu Gramps. Tieto zmeny sú podrobne opísané aj ďalej v tejto príručke. Používateľom programu Gramps, ktorí prešli z predchádzajúcich verzií, odporúčame, aby si prečítali túto časť starších [užívateľských príručiek](wiki:User_manual), aby si boli istí, že tieto nové funkcie využijú, keď začnú používať verziu 6.0.

# Pred aktualizáciou

***Pred*** aktualizáciou sa uistite, že sú údaje vášho rodinného stromu zabezpečené. Najlepší spôsob, ako to urobiť, je:

1.  Spustite svoju existujúcu verziu programu Gramps (Gramps 3.4 alebo Gramps 4.2 alebo Gramps 5.0)
2.  Otvorte svoj rodinný strom
3.  Zálohujte rodinný strom do formátu *gramps xml* alebo do formátu *gramps xml package* (balík *gramps xml* obsahuje vaše fotografie a iné mediálne súbory spojené s údajmi rodinného stromu). Zálohujte svoj strom prostredníctvom ponuky .
4.  Zatvorte tento rodinný strom a zopakujte vyššie uvedené kroky pre všetky ostatné rodinné stromy, ktoré máte
5.  Výsledný súbor (súbory) uložte na bezpečné miesto

Ďalšie informácie nájdete v [Zálohovaní rodinného stromu](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees/sk#Zálohovanie_rodinného_stromu). Všimnite si [čo nebude zahrnuté počas zálohovania](wiki:Template:Backup_Omissions).

Po správnom zabezpečení údajov pokračujte v inštalácii programu Gramps 6.0 pomocou bežného inštalačného procesu vášho operačného systému. Vo väčšine prípadov sa tým zabezpečí, že nová inštalácia programu Gramps 6.0 nebude kolidovať s vašou staršou verziou programu Gramps. Môže však byť bezpečnejšie odinštalovať Gramps 3.4 pred inštaláciou Gramps 6.0 alebo sa uistite, že ste nainštalovali Gramps 6.0 na iné miesto. Toto je vždy potrebné, ak inštalujete zo zdrojového kódu. Viac informácií o inštalácii programu Gramps 6.0 nájdete v časti [Stiahnutie najnovšej verzie programu Gramps](wiki:Download).

Po nainštalovaní programu Gramps 6.0 môžete otvoriť svoje existujúce rodinné stromy a pokračovať v práci. V prípade problémov (napr. po úplnej aktualizácii systému) importujte vyššie vytvorený(-é) záložný(-é) súbor(-y) a obnovte tak svoj(-e) rodinný(-é) strom(-y).

# Viditeľné zmeny jadra

Viditeľné zmeny po migrácii: rozhranie, údaje.

## Dátový model

Podrobnosti o zmenách dátového modelu (ak existujú):

1.  Žiadne zmeny

<hr>

- Rodinný strom **nemožno otvoriť** v programe Gramps 3.4/4.0/4.1/4.2 a Gramps 6.0 bez aktualizácie.

<!-- -->

- Downgrade je možné vykonať len exportom XML a importom do predchádzajúcej verzie.

<!-- -->

- Súbor XML programu Gramps vytvorený programom Gramps 3.4/4.0/4.1 nie je **identický** so súborom vytvoreným programom Gramps 6.0.

<!-- -->

- Gramps 6.0 je teraz **len pre Python3**

Viac informácií o internej databáze nájdete v časti [podrobné zmeny](wiki:Database_Formats#Detailed_Changes).

## Primárne zmeny

- SQLite je teraz predvolený databázový backend namiesto BSDDB. Stále sa môžete rozhodnúť používať [alternatívne databázové](wiki:Relational_database_comparison) backendy. BSDDB zostáva k dispozícii ako štandardná alternatíva. Pre náročných používateľov sú k dispozícii PostgreSQL a MongoDB ako experimentálne doplnky tretích strán.

Vývojári sa domnievajú, že SQLite môže mať menej poškodení databázy, ktoré bránia jednoduchej obnove.

- Možnosti automatického pravidelného zálohovania a zálohovania pri ukončení. Zálohovanie pri ukončení je predvolené.
- Konfigurácia: nová možnosť databáza-zálohovanie-použiť-kompresiu

## GUI

- Nové farebné schémy umožňujú výber svetlej a tmavej farby.
- Dodatočné farebné označenia v grafoch pre Domovskú osobu, Neznámeho žijúceho, Rodinu, Rozvedenú rodinu.
- Pridanie filtra "do <n> km/ míľ/stupňov"
- Možnosť zadávať dvojice zemepisná šírka/dĺžka oddelené čiarkou

<!-- -->

- Bočný panel lepšie mení veľkosť, pozícia sa pamätá
- Editor mena(priezviska) osoby sa používa intuitívnejšie.
- Poradie tlačidiel zobrazenia sa už nemení pri rôznom spustení.
- Lepšia indikácia priebehu pri dlho prebiehajúcich operáciách
- Okná si pamätajú veľkosť/pozíciu
- Pridanie 2-cestného vejárového grafu
- Pridanie bodov kml pre miesta v zemepisnom pohľade.

## Miesto

- možnosť vyhľadávania alternatívnych názvov miest pri výbere miesta

## Správy, nástroje, gramplety

- Nová správa o rodinnom strome
- Editor formátu miesta a možnosť pre mnohé správy
- Editor formátu dátumu a možnosť pre mnohé správy
- možnosť, ako nahlasovať žijúce osoby pre mnohé správy

<!-- -->

- Nástroj Zmena poradia ID bol aktualizovaný; teraz môže pracovať s vlastnými ID (ako GetGov ID).
- Naratívny web má ďalšie možnosti a zmeny vzhľadu.
  - Umožňuje výstup v rôznych jazykoch
  - Možnosť výstupu dátumu
  - Stránka so štatistikami
  - Pridaná možnosť Zahrnúť všetky / neodkazované mediálne objekty
  - vzťah k stredovej osobe na jednotlivých stránkach
- Pridanie možnosti veľkosti miniatúry do grafu Rodinné línie
- Vylepšenie správy o potomkoch a podrobnej správy o potomkoch
- Pridané nastavenia do Kompletnej správy o jedincovi
  - možnosť zahrnúť alebo vylúčiť poznámky o osobách a rodinách
  - pridaná možnosť zahrnúť alebo vylúčiť údaje zo sčítania ľudu
  - možnosť zahrnúť vzťah k stredovej osobe
  - možnosti zahrnúť identifikátor otca, značky, atribúty
- zahrnúť všetky typy miest do správy o mieste
- možnosti týkajúce sa vzťahov, rodinných línií a grafu presýpacie hodiny, ako sa kreslia línie

<!-- -->

- Novinka: [Clean input data](wiki:Gramps_6.0_Wiki_Manual_-_Tools#Clean_input_data) Nástroj - Odstrániť úvodné a koncové medzery.

## Import/Export

- Gedcom podporuje viac neštandardných "značiek" a ďalšie štandardné značky
- GEDCOM 5.6.0 Podpora vlastnej udalosti pri exporte
- Nová možnosť kompresie pri exporte XML

## Nové doplnky

- Pohľad Quilt Chart: Pohľad zobrazuje vizualizáciu prikrývkového grafu rodinného stromu
- Vylepšený správca zásuvných modulov: Addon/Plugin Manager s niekoľkými ďalšími možnosťami
- Strom pieskové hodiny: Strom Sandclock s použitím LaTeX genealogytree
- Nástroj na import a zlúčenie: Porovnáva databázu Gramps XML s aktuálnou databázou a umožňuje zlúčiť rozdiely.
- Kontrola údajov o asociáciách: Skontroluje údaje o asociáciách pre ľudí.

# Zmeny pod kapotou

Technické zmeny.

- Početné zmeny týkajúce sa podpory iných databázových backendov (SQLite, PostgreSQL, MongoDB atď.).
- Upozornenia na určité poškodenia databázy (väzby na neexistujúce objekty), ktoré boli predtým potlačené, sa teraz považujú za chyby. Na opravu výnimiek s poškodenou databázou môže byť potrebné spustiť nástroj Kontrola a oprava.
- Opravy, ktoré zabraňujú používateľovi zatvárať alebo meniť databázu počas dlho prebiehajúcich operácií.

## Závislosti

- Podporuje iba **python3**. (Podpora Pythonu2 bola zrušená pred januárom 2020 <ABBR title="End Of Life (discontinuation)">EOL</ABBR> nultou hodinou).
- Potrebujete GTK+ 3.10 a PyGObject 3.12 alebo novšie verzie

# Ďalšie informácie

## Rôzne

## Lokalizácia

- Aktualizácia prekladov: ca, cs, da, de, en_GB, eo, fr, fi, hu, is, it, lt, nb, nl, pt_BR, pt_PT, ru, sk, sl, uk, vi

## Cestovná mapa

- Preskúmajte poznámky k vydaniu pre [predchádzajúce vydania Gramps](wiki:Previous_releases_of_Gramps)
- Pozrite si plánované položky týkajúce sa [ďalšej verzie.](https://gramps-project.org/bugs/roadmap_page.php) Gramps
- [Návrhy na vylepšenie programu Gramps (GEPS)](wiki::Category:GEPS) - Nové položky implementované v programe Gramps 6.0 nájdete v stĺpci **Released**
- [6.0 Cestovná mapa](wiki:6.0_Roadmap) - wiki

## Zoznam zmien

- Pozrite si položky týkajúce sa programu Gramps [6.0](https://gramps-project.org/bugs/changelog_page.php) v nástroji na sledovanie problémov programu Gramps.

<!-- -->

- Ďalšie informácie nájdete v zoznamoch zmien testovacích verzií programu Gramps:
  - Gramps [6.0.0](https://github.com/gramps-project/gramps/releases/tag/v6.0.0)\].
  - Gramps [6.0.1](https://github.com/gramps-project/gramps/releases/tag/v6.0.1)
  - Gramps [6.0.2](https://github.com/gramps-project/gramps/releases/tag/v6.0.2)
  - Gramps [6.0.3](https://github.com/gramps-project/gramps/releases/tag/v6.0.3)

{{-}}

## Čo bolo *kedysi* nové

Stránka [Predchádzajúce vydanie](wiki:Previous_releases_of_Gramps) obsahuje odkazy na zoznamy zmien v hlavných vydaniach a udržiavacích vydaniach v priebehu rokov.

Avšak stránky **Čo je nové?** v nahradenej verzii príručky wiki pre každé hlavné vydanie môžu poskytnúť podrobnejšie informácie:

- [Verzia 5.0](wiki:Gramps_5.0_Wiki_Manual_-_What%27s_new%3F)
- [Verzia 4.2](wiki:Gramps_4.2_Wiki_Manual_-_What%27s_new%3F)
- [Verzia 4.1](wiki:Gramps_4.1_Wiki_Manual_-_What%27s_new%3F)
- [Verzia 4.0](wiki:Gramps_4.0_Wiki_Manual_-_What%27s_new%3F)
- [Verzia 3.4](wiki:Gramps_3.4_Wiki_Manual_-_What%27s_new%3F)
- [Verzia 3.3](wiki:Gramps_3.3_Wiki_Manual_-_What%27s_new%3F)
- [Verzia 3.2](wiki:Gramps_3.2_Wiki_Manual_-_What%27s_new%3F)

Kompaktný prehľad vylepšení bol prvýkrát pridaný do príručky v roku 2010. Počas prvých troch rokov fungovania wiki bolo potrebné preskúmať celú príručku.

- [Verzia 3.1 - Úplný manuál](wiki:Gramps_3.1_Wiki_Manual)
- [Verzia 3.0 - Úplný manuál](wiki:Gramps_3.0_Wiki_Manual)

Pôvodná dokumentácia MediaWiki sa začala vytvárať v roku 2006. Pred vydaním príručky 2.9 bola dokumentácia distribuovaná spolu so softvérom Gramps. Príručka na stiahnutie bola zrušená s verziou Gramps 3.0.

- [Gramps 2.2 (verzia manuálu 2.9)](https://gramps-project.org/gramps-manual/2.2/en/index.html)

{{-}}

[Category:Sk:Documentation](wiki:Category:Sk:Documentation)
