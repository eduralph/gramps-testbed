---
title: Gramps 6.0 Wiki Manual - Probably Alive/sk
categories:
- Sk:Documentation
managed: false
source: wiki-scrape
wiki_revid: 111449
wiki_fetched_at: '2026-05-30T20:10:26Z'
lang: sk
---

{{#vardefine:chapter\|7}} {{#vardefine:figure\|0}}

Životný stav osôb v databáze Gramps je dôležitý, keď potrebujete zdieľať údaje s ostatnými, ale chcete chrániť údaje o žijúcich osobách. Používa sa aj v niektorých správach. Z týchto dôvodov má Gramps niekoľko nástrojov, ktoré vám pomôžu určiť, či je niekto nažive.

## Ako Gramps určí, či je niekto nažive?

![[_media/EditPreferences-Dates-tab-default-51.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Ponuka: "Upraviť&gt;Predvoľby..." - "Dátumy" - karta - predvolené nastavenia]]

Jednoduchý spôsob, ako zistiť, či je niekto nažive, je zistiť, či má udalosť úmrtia alebo udalosť súvisiacu s úmrtím (napríklad pohreb). Pravdepodobne však platí, že mnoho ľudí vo vašej databáze takéto udalosti nemá, pretože nemusíte poznať žiadne podrobnosti o ich úmrtí. Ak viete, že niekto zomrel, možno by bolo dobré vytvoriť udalosť úmrtia. Môžete sa tiež vrátiť späť a pridať užitočné podrobnosti (napríklad dátum a miesto úmrtia), keď sú známe. Pridávanie udalostí pre ľudí, o ktorých sa vie, že zomreli, aj keď neobsahujú žiadne presné podrobnosti, je do istej miery užitočné. Gramps však môže za vás pridať aj udalosti s odhadovanými dátumami (alebo bez nich) (opísané nižšie).

Vyžadovať od používateľa, aby ručne pridával udalosť úmrtia k osobe (aby nebola považovaná za živú), by bolo veľmi zdĺhavé --- človek by musel zadávať podrobnosti o mnohých osobách. Pripomeňme, že ak je niekto považovaný za živého, potom by sa malo zabrániť zdieľaniu jeho údajov pri exporte. Preto má Gramps funkciu, ktorá dokáže vypočítať, či je niekto pravdepodobne nažive na základe dátumov jeho udalostí alebo jeho vzťahov s ľuďmi, ktorí môžu mať dátumy udalostí. Ak napríklad osoba nemá žiadny dôkaz o smrti (napríklad udalosť úmrtia alebo pohrebu), potom Gramps bude priebežne kontrolovať rodičov, deti, súrodencov tejto osoby, kým sa nenájde nejaký dôkaz - alebo sa nevyčerpajú spojenia na kontrolu. Pomocou informácií o typických vekových intervaloch a udalostiach (ako sú typické vekové rozdiely medzi súrodencami, typický vek matiek v čase narodenia atď.) môže Gramps odhadnúť, či je osoba živá alebo mŕtva. Ako si viete predstaviť, vykonanie tejto funkcie môže byť časovo náročné, ale môže byť celkom užitočné. Hodnoty pre typický vek pri narodení, medzi generáciami atď. môžete nastaviť v .

Funkcia Pravdepodobne nažive môže skontrolovať, či bola osoba nažive v určitý dátum alebo počas určitého časového úseku. Používa sa v gramplete [Vek na dátum](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/sk#Vek_na_dátum). Za normálnych okolností systém odhadne udalosti narodenia a úmrtia a zistí, či dátum spadá medzi tieto dve udalosti.

Existuje však jeden špeciálny prípad: ak hľadáte ľudí, ktorí pravdepodobne žijú *dnes*, a majú udalosť úmrtia, potom sú bez ohľadu na to považovaní za mŕtvych (aj keď udalosť nemá dátum). Preto dostanete odlišné výsledky, ak si pozriete, kto bol pravdepodobne nažive včera (alebo minulý rok) v porovnaní s tým, kto je považovaný za živého dnes. Dôvodom je, že ak máte udalosť úmrtia, viete, že osoba zomrela v minulosti, ale neviete kedy. Ak hľadáte, či osoba žila v minulosti (včera a predtým), potom nemôžete s istotou povedať, či bola vtedy mŕtva bez toho, aby ste poznali dátum úmrtia.

Ak chcete vedieť podrobnosti o tom, prečo Gramps určil, či je osoba živá alebo mŕtva, môžete použiť [Výpočet odhadovaných dátumov](wiki:Výpočet_odhadovaných_dátumov). Doplnok nástroja, aby ste získali vysvetlenie. Zobrazia sa odhadované dátumy narodenia a úmrtia a vzťah k niekomu, kto má dátum udalosti, na ktorom sú založené.

## Náhrada Pravdepodobne nažive

Prvým nástrojom je náhrada "Pravdepodobne nažive". Používa sa automaticky vždy, keď exportujete údaje do formátu, ktorý podporuje možnosť obmedziť údaje o žijúcich osobách. Náhrada obalí databázu vrstvou, ktorá zabráni prístupu k citlivým údajom o žijúcich ľuďoch, ako je ich meno a udalosti.

## Filter Pravdepodobne nažive

Dnešný dátum je osobitne spracovaný v prípadoch udalostí bez dátumu a pri kontrole stavu živých v minulosti. Ak má napríklad osoba udalosť úmrtia bez dátumu, potom vieme, že osoba je mŕtva od dnešného dňa a vždy v budúcnosti. Avšak pri tých funkciách, pri ktorých je možné skontrolovať, či bola osoba živá k nejakému dátumu v minulosti, nevieme povedať, či bola k tomuto dátumu živá alebo mŕtva. Ak teda máte udalosť úmrtia bez dátumu a skontrolujete, či bola nažive práve včera, Gramps nebude schopný určiť stav žijúci/zomrelý.

Pozri:

- [Filter Ľudia pravdepodobne žijúci](wiki:Gramps_6.0_Wiki_Manual_-_Filters/sk#Ľudia_pravdepodobne_žijúci)

## Gramplet Kalendár

Pozri gramplet [Kalendár](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/sk#Kalendaár).

## Úprava dátumov

Pozri [Úprava dátumov](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1/sk#Úprava_dátumov).

[Category:Sk:Documentation](wiki:Category:Sk:Documentation)
