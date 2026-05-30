---
title: 'Gramps 6.0 Wiki Manual - Entering and editing data: brief/sk'
categories:
- Sk:Documentation
- Stub
managed: false
source: wiki-scrape
wiki_revid: 120903
wiki_fetched_at: '2026-05-30T20:02:37Z'
lang: sk
---

{{#vardefine:chapter\|8}} {{#vardefine:figure\|0}}

Táto časť poskytuje základné poznatky potrebné na začatie zadávania genealogických informácií do programu Gramps. Vysvetľuje, ako zadávať osoby do rodinného stromu (nazývaného aj databáza) a ako špecifikovať ich rodinné vzťahy. (Podrobnejšie vysvetlenie bude nasledovať v ďalšej kapitole: [Gramps 6.0 Wiki Manual - Entering and editing data: detailed](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed).)

Najprv si určíme typy informácií, ktoré môžete do svojho rodinného stromu zadávať pomocou programu Gramps. Medzi ne patria:

- Osobné informácie o jedincovi (mená, adresy, dátumy narodenia a úmrtia atď.)
- Informácie o príbuzenských vzťahoch jedinca (manželstvá, rozvody, civilné zväzky atď.)
- Informácie o rodičoch a deťoch jedinca
- Zdroje, ktoré dokumentujú váš výskum

Teraz preskúmame, ako môžete zadávať a upravovať tieto rôzne typy genealogických informácií.

## Pridanie alebo úprava osoby

Do rodinného stromu môžete pridať novú osobu viacerými spôsobmi. Niektorým z nich sa budeme venovať v ďalšom texte. {{-}}

### Pridanie novej osoby

![[_media/PeopleTreeView-GroupedPeople-example-with-context-menu-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Kategória Ľudia - Stromový pohľad - Zoskupení ľudia]]

Najjednoduchší spôsob, ako zadať osobu, je pridať ju z pohľadu . Keď ste v pohľade , kliknite na tlačidlo Panela nástrojov .

{{-}} ![[_media/Edit-person-window-new-person-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Úprava osoby - okno - Nový prázdny editor]]

Zobrazí sa dialógové okno , do ktorého môžete zadať všetky údaje, ktoré o tejto osobe viete, potom vyberte , aby ste novú osobu uložili.

{{-}}

### Úprava existujúcej osoby

![[_media/Edit-person-window-existing-person-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Úprava osoby - okno - príklad existujúcej osoby]]

Ak chcete upraviť informácie o osobe, ktorá sa už nachádza v rodinnom strome, vyberte osobu v pohľade }\]\]

Ak chcete zadať nový vzťah k [Aktívnej osobe](wiki:Gramps_Glossary#active_person), prepnite na pohľad a uvidíte túto osobu označenú ako "Aktívna osoba". Vedľa označenia sa nachádza tlačidlo (zvyčajne reprezentované znakom ).

{{-}}

![[_media/FamilyEditor-dialog-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Úprava rodiny]]

Kliknutím na tlačidlo sa zobrazí dialógové okno s Aktívnou osobou nastavenou ako otec alebo matka.

{{-}}

![[_media/SelectMother-selector-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Výber matky - dialógové okno]]

Teraz otázka ?: Existuje už v rodinnom strome osoba, ktorá bude vytvárať vzťah s Aktívnou osobou? Ak áno, kliknite na tlačidlo k ďalšej osobe. Potom budete môcť listovať v zozname osôb v rodinnom strome a vybrať požadovanú osobu. Ak nie, kliknite na tlačidlo . To vám umožní pridať novú osobu do rodinného stromu a určiť vzťah, ktorý má táto osoba k Aktívnej osobe.

Ak chcete upraviť existujúci vzťah z pohľadu , kliknite na tlačidlo vedľa príslušného záznamu Rodina. Ak je v zozname viac ako jeden vzťah, môžete vybrať požadovaného manžela alebo partnera kliknutím na príslušné tlačidlo vedľa vzťahu.

{{-}}

### Zadanie vzťahu pomocou pohľadu Zoznam rodín

Zadanie nového vzťahu v pohľade , kliknite na tlačidlo na paneli nástrojov a otvorí sa prázdne dialógové okno . V tomto okamihu môžete do rodiny pridať ľudí.

{{-}}

## Zadanie rodičov

Rodičov aktívnej osoby môžete určiť v pohľade (pozri } - selektor). Je potrebná malá opatrnosť, aby sa zabránilo vytvoreniu . Ak chcete pridať Aktívnu osobu do už existujúcej rodiny, mali by ste kliknúť na tlačidlo . Ak rodina vrátane rodičov ešte neexistuje, mali by ste kliknúť na tlačidlo .

{{-}} ![[_media/SelectFamily-SelectorDialog-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Výber rodiny - príklad dialógového okna výberu]]

Ak kliknete na tlačidlo , zobrazí sa dialógové okno . To vám umožní vybrať existujúcu rodinu a potom sa Aktívna osoba pridá ako potomok do rodiny.

Ak kliknete na tlačidlo , zobrazí sa nové dialógové okno s Aktívnou osobou uvedenou ako dieťa novej rodiny. Rodičov môžete do rodiny pridať buď pridaním nových ľudí ako rodičov, alebo výberom existujúcich ľudí ako rodičov.

{{-}} Rodičov osoby môžete určiť aj v pohľade . Ak rodina už existuje, kliknite na tlačidlo na paneli nástrojov a po zobrazení dialógového okna pridajte osobu ako dieťa. Ak rodina ešte neexistuje, kliknutím na tlačidlo vytvorte novú rodinu a pridajte príslušných rodičov a deti.

{{-}}

## Zadanie detí

Pridanie detí do vzťahu sa vykonáva podobným postupom. Z pohľadu alebo pohľadu vyberte existujúcu rodinu alebo vytvorte novú rodinu. Deti môžete pridať výberom tlačidla alebo napravo od zoznamu detí.

Kliknutím na tlačidlo sa zobrazí dialógové okno , ktoré vám umožní zadať novú osobu. Kliknutím na tlačidlo umožníte vybrať existujúcu osobu zo zoznamu. V predvolenom nastavení sa dieťa pridá s typom vzťahu **narodenie** k obom rodičom.

{{-}} ![[_media/ChildReferenceEditor-dialog-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Editor odkazu na dieťa]]

Ak chcete zmeniť vzťah rodič/dieťa z predvoleného nastavenia **Narodenie**, v dialógovom okne vyberte dieťa a kliknite na . Tým sa zobrazí dialógové okno .

{{-}} Ak chcete zmeniť poradie detí v rodine, použite šípky alebo funkciu [*potiahni a pusť*](http://en.wikipedia.org/wiki/Drag_and_drop) na karte . {{-}}

## Pridávanie fotografií a iných mediálnych objektov

Fotografie a iné mediálne objekty môžete pridávať k jednotlivým osobám, udalostiam, zdrojom a miestam. Môžete tiež pridávať obrázky, ktoré nemusia byť obmedzené na jednu osobu alebo udalosť (napríklad skupinové rodinné fotografie).

{{-}} ![[_media/PersonView-PeopleListView-example-with-context-menu-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Kategória Ľudia - Stromové zobrazenie - Zobrazenie zoznamu ľudí ( mainwin-fig)]] ![[_media/Edit-person-window-existing-person-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} edit-pers-fig]]

Ak chcete pridať obrázok k jednej osobe, prepnite na pohľad (mainwin-fig), vyberte osobu a potom kliknite na ikonu na paneli nástrojov. Tým sa zobrazí dialógové okno (edit-pers-fig). Ďalej vyberte kartu a kliknite na tlačidlo , čím vyvoláte dialógové okno . Zadajte názov súboru alebo vyhľadajte požadovaný súbor s obrázkom a potom zadajte názov tohto obrázka. Pokračujte v pridávaní obrázkov, kým neskončíte.

{{-}} ![[_media/Families-category-list-view-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} family-fig]]

Ak chcete pridať obrázky týkajúce sa vzťahu (napríklad manželstvo), prepnite na pohľad (family-fig) a dvakrát kliknite na pole Manželia. Tým sa vyvolá dialógové okno . Vyberte kartu a kliknutím na tlačidlo pridajte obrázok. {{-}}

![[_media/SourcesCategory-Sources-ListView-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} sources-fig]] ![[_media/PlacesCategory-PlaceView-list-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} places-fig]]

Ak chcete pridať obrázky súvisiace so zdrojom alebo miestom, najprv sa prepnite na pohľad (sources-fig) alebo pohľad (places-fig). Vyberte požadovaný zdroj alebo miesto a potom naň buď dvakrát kliknite, alebo kliknite na ikonu na paneli nástrojov. Vyberte kartu a kliknutím na tlačidlo pridajte obrázok. {{-}}

![[_media/MediaCategory-Media-ListView-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} media-fig]]

Nakoniec, ak chcete pridať obrázky, ktoré chcete zahrnúť do rodinného stromu, ale obrázok nie je obmedzený na jednu konkrétnu osobu, vzťah, zdroj alebo miesto, prepnite na pohľad (media-fig). Potom kliknite na ikonu na paneli nástrojov a pridajte obrázok. Ak ste už pridali nejaké obrázky do jednotlivých galérií, nájdete ich tiež uvedené v pohľade .

.{{#vardefineecho:figure\|{{#expr:{{#var:figure}}+1}}}} places-fig\]\] ![[_media/RepositoriesCategory-Repositories-ListView-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} repository-fig]]

Ak chcete do rodinného stromu pridať udalosť, citáciu/zdroj, miesto alebo archív, prepnite na príslušný pohľad ( events-fig), pohľad , pohľad (sources-fig), pohľad (places-fig) alebo pohľad (repository-fig). Potom kliknite na ikonu na paneli nástrojov, aby ste pridali príslušný objekt. Zadajte informácie v dialógovom okne ( , , alebo ).

Ak chcete upraviť informácie o udalostiach, zdrojoch, miestach a archívoch, ktoré sa už nachádzajú v rodinnom strome, prepnite sa do príslušného pohľadu, vyberte položku, ktorú chcete zobraziť/zmeniť, a potom kliknite na ikonu na paneli nástrojov. Prípadne môžete na záznam dvakrát kliknúť a upraviť ho.

[Category:Sk:Documentation](wiki:Category:Sk:Documentation)
