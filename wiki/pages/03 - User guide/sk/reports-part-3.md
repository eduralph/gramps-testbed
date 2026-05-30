---
title: Gramps 6.0 Wiki Manual - Reports - part 3/sk
categories:
- Plugins
- Sk:Documentation
managed: false
source: wiki-scrape
wiki_revid: 125658
wiki_fetched_at: '2026-05-30T20:10:47Z'
lang: sk
---

{{#vardefine:chapter\|13.3}} {{#vardefine:figure\|0}} Späť na [Register správ](wiki:Gramps_6.0_Wiki_Manual_-_Reports/sk).

<hr>

{{-}} ![[_media/Menubar-ReportsOverview-60.png|Obrázok {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Položka ponuky pre]] Táto časť popisuje správu Kniha, ktorá je k dispozícii v programe Gramps.

# Knihy

Správa Knihy umožňuje vytvoriť vlastnú **genealogickú knihu**, ktorá obsahuje zbierku textových a grafických správ o dedičstve v jednom dokumente (t. j. v knihe).

Jediná správa, ktorá je k dispozícii v rámci tejto správy, je správa Knihy.

Keď v ponuke vyberiete , zobrazí sa hlavné dialógové okno . {{-}}

## Dialógové okno Správa kníh

![[_media/ManageBooks-dialog-default-60.png|Obrázok {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Správa kníh - dialógové okno]]

Hlavné dialógové okno má tri časti , a

Ak chcete začať vytvárať vlastnú genealogickú knihu, kliknite na tlačidlo po vykonaní všetkých výberov správ, ktoré majú byť zahrnuté, a prípadne ich nakonfigurovaní (alebo prekonfigurovaní) alebo len na prijatie predvolených nastavení; zobrazí sa dialógové okno .

### Názov knihy

Názov (<kód>Nová kniha</kód>predvolené) textové vstupné pole zobrazuje názov aktuálnej knihy. Zmeňte ho a uložte si vlastnú knihu (súbor nakonfigurovaných výberov) na budúce použitie, pričom v takom prípade môžete pole najprv zmeniť tak, aby obsahovalo akýkoľvek názov. Ak načítate uloženú knihu (pozri nižšie), zobrazí sa názov tejto knihy - ktorý potom môžete zmeniť, ak chcete uložiť mierne odlišnú konfiguráciu.

#### Panel s názvom knihy

Horná horizontálna sada ikon panela nástrojov v blízkosti poľa pôsobí na celú knihu a umožňuje nasledujúce funkcie:

- Tlačidlo s ikonou vymaže všetky predtým vybrané položky z časti .
- Tlačidlo ikony uloží aktuálnu knihu (pod názvom, ktorý bol predtým zadaný do textového poľa ) pre budúce použitie, ak názov knihy už existuje, budete požiadaní, či chcete uložiť nad ním, alebo môžete a zadať iný názov.

{{-}} ![[_media/OpenPreviouslyCreatedBook-AvailableBooks-dialog-50.png|Obrázok {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Ikona &quot;Otvoriť predtým vytvorenú knihu&quot; a výsledná ikona &quot;Dostupné knihy&quot; - dialógové okno]]

- Výberom tlačidla ikony otvoríte okno , v ktorom sa zobrazia všetky vaše predtým uložené knihy. V tomto okne buď dvakrát kliknite na názov konkrétnej knihy, alebo ju najprv vyberte a potom stlačte , aby sa kniha následne načítala.

{{-}} ![[_media/ManagePreviouslyCreatedBooks-AvailableBooks-dialog-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Ikona &quot;Spravovať predtým vytvorené knihy&quot; a výsledná ikona &quot;Dostupné knihy&quot; - dialógové okno]]

- Tlačidlom ikony môžete otvoriť aj trochu iné okno , v ktorom sa zobrazí zoznam dostupných kníh, a pomocou tlačidla môžete vybranú knihu odstrániť.

{{-}}

### Dostupné položky

V strednej časti sa nachádza zoznam položiek, ktoré sú k dispozícii na zaradenie do knihy. {{-}}

### Dostupné položky výberu

Takmer všetky položky dostupné na zaradenie do knihy sú textové alebo grafické zostavy, a preto sú k dispozícii vo forme samostatných zostáv (ich jednotlivé dokumentácie nájdete v [Register správ](wiki:Gramps_6.0_Wiki_Manual_-_Reports/sk)). Výnimkou sú nasledujúce položky, ktoré sú k dispozícii len ako položky knihy, v knižnej zostave:

#### Abecedný register

![[_media/AlphabeticalIndex-book-item-BooksReport-options-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Abecedný zoznam - položka]]

Táto položka vytvorí stránku(-y) s abecedným registrom osôb zaznamenaných do vybraných textových správ.

Na karte *Možnosti správy* môžete z rozbaľovacieho zoznamu vybrať jazyk . {{-}}

#### Vlastný text

![[_media/CustomText-book-item-BooksReport-options-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Vlastný text - položka]]

Položka vytvorí stránku s tromi odsekmi, z ktorých každý obsahuje vlastný text:

- *Úvodný text:*
- *Stredný text:*
- *Záverečný text:*

Vstupné textové polia sú rozbaliteľné, takže tam môžete vložiť naozaj všetok text, ktorý chcete.

V spodnej časti okna sa zobrazia niektoré **Možnosti dokumentu**: tu môžete vybrať **Štýl**. Môžete si vybrať predvolený štýl alebo kliknúť na tlačidlo . Tým sa zobrazí okno , v ktorom môžete pridávať a odstraňovať štýly. Podrobnejšie informácie nájdete aj v [Editore štýlu](wiki:Gramps_6.0_Wiki_Manual_-_Settings/sk#Editor_štýlu). Táto položka bola určená na epigrafy, venovania, vysvetlivky, poznámky a podobne. {{-}}

#### Obsah

![[_media/TableOfContents-book-item-BooksReport-options-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Obsah - položka]]

Obsah sa vytvára pre knihu ako zoznam častí knihy alebo dokumentu usporiadaný v poradí, v akom sa jednotlivé časti objavujú.

Na karte *Možnosti zostavy* môžete z rozbaľovacieho zoznamu vybrať jazyk .

{{-}}

#### Titulná strana

![[_media/TitlePage-book-item-BooksReport-options-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Titulná strana - položka]]

  
Ak ste vybrali položku a kliknutím na tlačidlo vložíte túto položku do knihy a kliknete na tlačidlo (Konfigurácia aktuálne vybranej položky), zobrazí sa okno .

Na karte máte k dispozícii tri textové vstupné polia, v ktorých môžete zmeniť **Názov:**, **Podnadpis:** a **Pätičku:** z poskytnutého vzorového textu.

Medzi nadpis a pätičku môžete voliteľne umiestniť , a to výberom tlačidla , ktoré zobrazí výberové dialógové okno, v ktorom môžete vybrať existujúci obrázok, ktorý chcete.

Môžete tiež zmeniť z predvoleného nastavenia.

V spodnej časti okna sa zobrazujú niektoré **Možnosti dokumentu**: tu môžete vybrať **Štýl**. Môžete si vybrať predvolený štýl alebo kliknúť na tlačidlo . Tým sa zobrazí okno , v ktorom môžete pridávať a odstraňovať štýly. Podrobnejšie informácie nájdete aj v [Editore štýlu](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Editor_štýlu).

Keďže môžete konfigurovať rôzne prvky, túto položku môžete použiť na vytvorenie titulných stránok pre celú knihu, jej kapitolu alebo aj pre jednu položku. {{-}}

### Aktuálna kniha

V spodnej časti sú uvedené aktuálne vybrané položky v poradí, v akom sa budú zobrazovať v knihe. {{-}}

#### Pruh nástrojov Aktuálna kniha

Pravá spodná zvislá sada ikon na paneli nástrojov vedľa tabuľky oddielu pracuje s oddielmi a umožňuje nasledujúce funkcie:

- Pomocou ikony ikony pridáte vybranú položku z horného zoznamu sekcií do spodného zoznamu sekcií . Dvojklikom na vybranú položku (horného zoznamu) ju tiež pridáte.
- Pomocou tlačidla s ikonou odstránite položku zo spodného zoznamu sekcií .
- Pomocou ikony zmeníte poradie vybranej položky v zozname .
- Pomocou tlačidla ikony zmeníte poradie vybranej položky v .
- Pomocou ikonového tlačidla môžete konfigurovať možnosti vybranej **položky** v -- musíte však najprv vybrať položku. Dvojitým kliknutím na položku sa tiež spustí konfiguračné dialógové okno. Dialógové okno konfigurácie vyvolané tlačidlom ikony je špecifické pre danú položku. Ak sa rozhodnete položku nekonfigurovať, pre všetky potrebné možnosti sa použijú niektoré predvolené hodnoty. Spoločnou voľbou pre takmer všetky položky knihy je stredová osoba: osoba, na ktorej je položka vycentrovaná. Vďaka tejto možnosti môžete vytvoriť knihu s položkami sústredenými na rôzne osoby (napr. predkovia vašej mamy a otca ako samostatné kapitoly). V predvolenom nastavení je stredová osoba nastavená na .

{{-}}

## Dialógové okno Generovanie knihy

![[_media/GenerateBook-dialog-example-60.png|Obrázok {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Generovanie knihy - dialógové okno]]

Dialógové okno sa zobrazí po výbere dialógového okna tlačidla na prijatie predvolených nastavení a začatie tvorby vlastnej genealogickej knihy.

Sú tu dve časti a :

### Papierové možnosti

, kde môžete zmeniť veľkosť a orientáciu formátu papiera a všetky okraje. Namiesto toho je k dispozícii zaškrtávacie políčko na použitie metrických hodnôt.

### Možnosti dokumentu

V časti môžete zmeniť:

- pomocou rozbaľovacej ponuky môžete zmeniť výstupný formát:

  - *PDF dokument*
  - *PostScript*
  - *OpenDocument Text*
  - *Tlačiť...*

-  ak je začiarknuté, umožní vám otvoriť dokument v predvolenom prehliadači, napr. v [LibreOffice](http://www.libreoffice.org/download/) Word Processor. (v predvolenom nastavení políčko nie je začiarknuté)

- zadajte názov súboru, všimnite si, že prípona názvu súboru sa mení v závislosti od výstupného formátu. napr: Pre *PDF dokument* je predvolená hodnota `/yourhomedir/`<názov rodokmeňa>`_book.pdf` a *OpenDocument Text* je predvolená hodnota `/yourhomedir/`<názov rodokmeňa>`_book.odt` atď.

### Pozri tiež

- [Pridanie obsahu tabuľky alebo indexu do knihy správ](wiki:Add_Table_of_Contents_or_Index_to_reports)

{{-}}

<hr>

Späť na [Index of Reports](wiki:Gramps_6.0_Wiki_Manual_-_Reports/sk).

[Category:Sk:Documentation](wiki:Category:Sk:Documentation) [Category:Plugins](wiki:Category:Plugins)
