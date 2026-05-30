---
title: 'Gramps 6.0 Wiki Manual - Entering and editing data: detailed - part 3/sk'
categories:
- Sk:Documentation
- Stub
managed: false
source: wiki-scrape
wiki_revid: 120624
wiki_fetched_at: '2026-05-30T20:04:18Z'
lang: sk
---

{{#vardefine:chapter\|9.3}} {{#vardefine:figure\|0}} V predchádzajúcej časti ste získali podrobný prehľad o tom, ako zadávať a upravovať hlavné objekty, ktoré sa zobrazujú v programe Gramps. Táto časť pokračuje ďalšími objektmi, s ktorými sa v programe Gramps stretnete.

## Editor mena

Mená sa upravujú prostredníctvom dialógového okna , ktoré je dostupné z dialógového okna dialógového okna . {{-}}

### Dialógové okno Editor mena

![[_media/NameEditor-dialog-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Editor názvov - dialóg - príklad]] Horná časť okna umožňuje z rozbaľovacieho zoznamu zadať typ mena (napr. Rodné meno, Manželské meno atď.). Ďalej sa nachádzajú prvky osobného mena najčastejšie zoskupené ako prvky Given Name (Dané meno). Za sekciou Given Name (Dané meno) nasleduje sekcia Family Names (Rodinné mená). V spodnej časti sa nachádzajú prvky umožňujúce prispôsobenie triedenia mien, dátumy mien, zdroje mien a poznámky k menám. {{-}}

#### Typ

- (`Rodné meno` predvolené) Rozbaľovací zoznam Typ mena umožňuje vybrať typ zadávaného mena. Do tohto poľa môžete tiež priamo zadať [Vlastný typ](wiki:Gramps_Glossary#custom).

- Tlačidlo prepína ikonu v pravom hornom rohu na označenie tohto záznamu mena ako súkromného. Tým získate možnosť vynechať tento názov zo zahrnutia do správ, ak si to vyberiete medzi možnosťami generovania správ.

{{-}}

#### Sekcia Dané meno(á)

Sekcia **Dané meno(á)** obsahuje všetky časti osobného mena, ktoré môžete uložiť v programe Gramps:

- Tu by mali byť zadané všetky dané (krstné) mená osoby.

- Tu by sa malo zadať vlastné zákonné meno osoby, ktoré osoba používala najčastejšie. Napríklad osoba menom John Raymond Smith, ktorá používa meno Raymond, by tu mala mať uvedené *Raymond*. Ak táto osoba bežne používa meno *Ray*, malo by sa uviesť ako prezývka, keďže Ray nie je vlastné zákonné meno (pozri nasledujúce). V Nemecku a na niektorých iných miestach bolo zvykom medzi rôznymi danými (krstnými) menami podčiarknuť volacie meno (pozri tiež [tu](wiki:Names_in_Gramps#Call_Name)).

- Tu sa môže uviesť titul osoby, napríklad doktor (alebo Dr.).

- Tu sa zadáva prípona mena osoby, napríklad Junior (Jr.) alebo III.

- Tu by sa mala uviesť prezývka osoby. Prezývky zahŕňajú skratky vlastných zákonných mien, ako napríklad Greg pre Gregory (pozri vyššie volacie meno).

{{-}}

#### Sekcia Rodové mená

Sekcia **Rodové mená** obsahuje prvky rodinného mena osoby. Gramps umožňuje používať viacero rodinných mien, ako aj viacero druhov rodinných mien.

- Panel nástrojov - **+** / **Upraviť** / **Odstrániť** / **Posunúť nahor v zozname** / **Posunúť v zozname nadol**

Zobrazujú sa nasledujúce stĺpce:

- Predpona pre priezvisko, ktorá sa nepoužíva pri triedení (napríklad "de" alebo "van").

- pre hlavnú časť priezviska.

- často používaný v matronymických alebo patronymických pomenovacích schémach, napríklad *dotter*.

- označujúci typ rodového mena a jeho odvodenie.

- Radiobox označujúci, či je priezvisko primárne.

Zobrazuje sa nasledujúce pole:

- pre rodiny, ktoré sa bežne označujú ľudovejším pseudonymom.

Pozri tiež: [Names in Gramps](wiki:Names_in_Gramps) - článok na wiki. {{-}}

### Stránky s kartou Editor mien

#### Všeobecné

Možnosti umožňujúce upraviť špecifické vlastnosti zoskupovania, triedenia a zobrazovania tohto názvu, ako aj uviesť dátum zodpovedajúci názvu:

- Pole poskytuje alternatívny uzol zoskupenia pre meno v zobrazení osoby, ktorý nahrádza predvolené zoskupenie založené na rodnom mene. Môže to byť potrebné pri podobných priezviskách, ktoré je potrebné zoskupiť -- napríklad ruské mená Ivanov a Ivanova sa považujú za rovnaké, ale rozdiel v rode sa prejavuje v odlišnom písaní. Pozrite si časť [Zoskupovanie priezvisk](wiki:Zoskupovanie_priezvisk).
  -  Začiarknutím tohto políčka povolíte písanie do tohto poľa. (v predvolenom nastavení políčko nie je začiarknuté)

  
Ľudia sa zobrazujú podľa formátu mena uvedeného v Predvoľbách (predvolené nastavenie).

Tu môžete zabezpečiť, aby sa táto osoba zobrazovala podľa vlastného formátu mena. *(Ďalšie formáty mien môžete vybrať v . } alebo prispôsobiť pomocou [Display_Name_Editor](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Display_Name_Editor))*.

- Polohy a určujú, ako sa meno zobrazí v zobrazení Ľudia a v prehľadoch. Triedenie umožňuje pri triedení mena potlačiť vzor mena nastavený v predvoľbách Gramps. Napríklad zrazu máte vetvu švédskych mien s given a patronymic, ale zvyšok vašej databázy triedi mená na Family name, Given. Tu môžete uviesť, aby sa toto meno triedilo vždy ako Patronymic, Given (Rodné meno, Dané).

  
Tu môžete zabezpečiť, aby sa táto osoba triedila podľa vlastného formátu mena. *(Ďalšie formáty mien môžete vybrať v }. } alebo prispôsobiť pomocou [Display_Name_Editor](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Display_Name_Editor))*.

Pomocou môžete určiť, ako sa bude meno zobrazovať. Môžete napríklad chcieť zoradiť meno na základe mena alebo priezviska osoby, ale stále mať na displeji zobrazený čestný titul pred týmto menom. *(Ďalšie formáty mien môžete vybrať v }. } alebo prispôsobiť pomocou [Display_Name_Editor](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Display_Name_Editor).)*

Zobrazenie Strom osôb zoskupuje ľudí pod primárnym priezviskom. Toto môžete prepísať tak, že tu nastavíte hodnotu skupiny. Zobrazí sa otázka, či chcete zoskupiť len túto osobu alebo všetky osoby s týmto konkrétnym primárnym priezviskom.

- môže poskytnúť informácie o platnosti tohto mena -- podľa potreby použite dátumové rozpätie. Ikona úpravy dátumu otvorí [Upravovač_dátumu](wiki:Gramps_6.0_Wiki_Manuál_-_Vkladanie_a_úprava_údajov:_Detail_-_časť_1#Úprava_dátumu). Napr. pri manželskom mene zadajte dátum prvého použitia mena alebo dátum sobáša.

#### Zdroje citácií

Na záložke sa zobrazujú informácie o zdrojoch a citáciách relevantných pre toto meno a ovládacie prvky umožňujúce ich úpravu. V strednej časti sa zobrazuje zoznam všetkých takýchto citácií a zdrojov uložených v databáze. Tlačidlá , a umožňujú zodpovedajúcim spôsobom pridať, upraviť a odstrániť citáciu k tomuto názvu. Všimnite si, že tlačidlá a sú dostupné len vtedy, keď je v zozname vybraný odkaz na zdroj.

Viac informácií: [Editor citácií](wiki:Gramps_6.0_Wiki_Manuál_-_Vkladanie_a_úprava_údajov:_Podrobne_-_časť_2#Upravovanie_citácií_zdrojov)

#### Notes

Na záložke sa zobrazia všetky poznámky týkajúce sa názvu. Ak chcete pridať poznámku alebo upraviť existujúce poznámky, jednoducho upravte text v poli na zadávanie textu.

Viac informácií: [Editátor poznámok](wiki:Gramps_6.0_Wiki_Manuál_-_Vkladanie_a_úprava_údajov:_Podrobne_-_časť_2#Upravovanie_informácií_o_poznámkach)

## Atribúty

Keď pridávate alebo upravujete [Atribúty](wiki:Atribúty_v_Gramps) z dialógových okien sa zobrazí dialógové okno . {{-}}

### Dialóg Editor atribútov

![[_media/AttributeEditor-dialog-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Editor atribútov - dialógové okno - predvolené]] V hornej časti okna sa zobrazuje názov dialógu vrátane mena osoby, ktorej atribút sa upravuje. V strednej časti okna sa zobrazujú tri záložky poznámkového bloku obsahujúce rôzne kategórie dostupných informácií. Ktorúkoľvek záložku môžete vyniesť nahor na prezeranie alebo úpravu kliknutím na príslušný nadpis záložky. V dolnej časti sú tlačidlá a . Kliknutím na tlačidlo sa kedykoľvek použijú všetky zmeny vykonané na všetkých kartách a dialógové okno sa zatvorí. Kliknutím na tlačidlo sa okno kedykoľvek zatvorí bez uplatnenia akýchkoľvek zmien.

Horná časť umožňuje upravovať najvšeobecnejšie informácie o atribúte:

- (`Identifikačné číslo`predvolené) Názov atribútu, ktorý chcete použiť. Napríklad: *Výška* (pre osobu), *Počasie v tento deň* (pre udalosť), ... Použite ho na ukladanie útržkov informácií, ktoré zhromažďujete a ktoré chcete správne prepojiť so zdrojmi. Atribúty možno použiť pre osoby, rodiny, udalosti a médiá. Informácie možno zadať do príslušných polí na zadávanie textu. Názov atribútu možno tiež vybrať z dostupných možností (ak existujú) uvedených v rozbaľovacej ponuke .

- Prepínačom označíte tento záznam atribútu ako súkromný alebo verejný. Tým získate možnosť vynechať tento atribút zo zahrnutia do výkazov, ak si to vyberiete medzi možnosťami generovania výkazov.

- Textový záznam popisu atribútu. Napr. *1,8 m, slnečný alebo modré oči*.

{{-}}

### Stránky karty Editor atribútu

#### Zdroje Citácie

  
Na karte sa zobrazujú informácie o citáciách a zdrojoch relevantných pre tento atribút a ovládacie prvky umožňujúce ich úpravu. V strednej časti sa zobrazuje zoznam všetkých takýchto zdrojov a citácií odkazov uložených v databáze. Tlačidlá , a umožňujú zodpovedajúcim spôsobom pridať, upraviť a odstrániť odkaz na zdroj k tomuto atribútu. Všimnite si, že tlačidlá a sú dostupné len vtedy, keď je citácia/odkaz na zdroj vybraná zo zoznamu.

#### Poznámky

  
Na karte sa zobrazujú všetky poznámky týkajúce sa atribútu. Ak chcete pridať poznámku alebo upraviť existujúce poznámky, jednoducho upravte text v poli na zadávanie textu.

{{-}}

## Adresy

Keď pridávate alebo upravujete adresu z dialógových okien sa zobrazí dialógové okno . {{-}}

### Dialóg Editor adries

![[_media/AddressEditor-dialog-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Editor adresy - dialógové okno - predvolené]] Dialógové okno umožňuje zaznamenať aktuálnu adresu zaznamenaním informácií do príslušných polí na zadávanie textu.

Horná časť dialógového okna umožňuje upravovať a zadávať informácie o adrese:

- } Dátum, ku ktorému je adresa platná.

  - tlačidlo

- Ulica adresy.

- Tlačidlo . Prepnutím tohto tlačidla označíte tento záznam adresy ako súkromný alebo verejný. To vám umožní vynechať túto adresu zo zahrnutia do správ, ak si to vyberiete medzi možnosťami generovania správ.

- } Názov lokality adresy.

- Štát alebo okres adresy v prípade, že ju musí obsahovať poštová adresa.

- Obec alebo mesto adresy.

- Krajina adresy.

- Poštové smerovacie číslo.

- Telefónne číslo spojené s adresou.

V spodnej časti dialógového okna sa nachádzajú tlačidlá , a . Kliknutím na tlačidlo sa kedykoľvek použijú všetky zmeny vykonané na všetkých kartách a dialógové okno sa zatvorí. Kliknutím na tlačidlo sa okno kedykoľvek zatvorí bez uplatnenia akýchkoľvek zmien. {{-}}

### Stránky karty Editor adresy

Nasledujúce karty obsahujú rôzne kategórie dostupných informácií. Ktorúkoľvek kartu môžete vyvolať na začiatok na zobrazenie alebo úpravu kliknutím na príslušný nadpis karty.

#### Zdroje Citácie

  
Na záložke sa zobrazujú informácie o zdrojoch relevantných pre túto adresu a ovládacie prvky umožňujúce ich úpravu. V strednej časti sa zobrazuje zoznam všetkých takýchto zdrojov a odkazov na citácie uložených v databáze. Tlačidlá , a umožňujú zodpovedajúcim spôsobom pridať, upraviť a odstrániť odkaz na citáciu/zdroj k tejto adrese. Všimnite si, že tlačidlá a sú dostupné len vtedy, keď je v zozname vybraný odkaz na zdroj.

#### Poznámky

  
Na karte sa zobrazujú všetky poznámky týkajúce sa adresy. Ak chcete pridať poznámku alebo upraviť existujúce poznámky, jednoducho upravte text v poli na zadávanie textu.

{{-}}

## Zlučovanie záznamov

![[_media/PeopleCategory-Toolbar-MergeTheSelectedPersons-icon-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Zlúčenie vybraných osôb - zvýraznená ikona na paneli nástrojov - príklad]] Niekedy sa ukáže, že niekoľko záznamov vo vašom rodokmeni opisuje ten istý objekt: tú istú osobu, to isté miesto alebo tú istú citáciu/zdroj. Môže sa to stať buď vtedy, keď sú údaje omylom zadané dvakrát, alebo keď sa na základe nových informácií zistí, že oba záznamy sa týkajú tej istej osoby. Môže sa to stať aj po importovaní GEDCOM získaného od príbuzného, ktorého databáza sa prekrýva s vašimi existujúcimi údajmi.

Vždy, keď zistíte duplicitné záznamy, je ich zlúčenie užitočným spôsobom nápravy situácie. {{-}}

### Zlúčenie ľudí

![[_media/MergePeople-dialog-default-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Zlúčenie ľudí - rozšírené sekcie &quot;Kontextové informácie&quot; - dialógové okno - predvolený príklad]]

Keď sú vybraté presne dve osoby, výberom } vyvoláte dialógové okno .

Dialógové okno umožňuje rozhodnúť o tom, či sa vybrané záznamy majú zlúčiť alebo nie. Ak sa rozhodnete, že záznamy by sa nemali zlúčiť napriek podobným menám, môžete kliknutím na tlačidlo zavrieť dialógové okno bez vykonania akýchkoľvek zmien.

Rozbalením polí a {man label\|kontextové informácie}} v ľavom dolnom rohu sa zobrazia ďalšie informácie o osobách, ktoré sa majú zlúčiť.

Ak sa rozhodnete pokračovať v zlučovaní, vyberte príslušné prepínacie tlačidlo , aby ste určili záznam, ktorý sa má použiť ako zdroj primárnych údajov, a potom kliknite na tlačidlo . Údaje z druhého záznamu sa ponechajú ako náhradné údaje.

Konkrétne, všetky názvy z druhého záznamu sa stanú alternatívnymi názvami zlúčeného záznamu. Podobne rodičia, manželia a deti druhého záznamu sa stanú alternatívnymi rodičmi, manželmi a deťmi zlúčeného záznamu atď. {{-}} ![[_media/MergePeople-dialog-sections-expanded-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Zlúčenie ľudí - sekcie &quot;Podrobný výber&quot; a &quot;Kontextové informácie&quot; rozšírené - dialóg - príklad]] {{-}}

### Zlúčenie rodín

![[_media/MergeFamilies-dialog-default-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Zlúčenie rodín - dialógové okno - predvolený príklad]]

Keď sú vybrané presne dve rodiny, výberom } vyvoláte dialógové okno.

Dialógové okno umožňuje rozhodnúť, či sa majú vybrané záznamy zlúčiť alebo nie. Ak sa rozhodnete, že záznamy by sa nemali zlúčiť napriek tomu, že sú podobné, môžete kliknutím na zavrieť dialógové okno bez vykonania akýchkoľvek zmien.

Môžete vybrať jednu z dvoch rodín, ktorá bude zdrojom primárnych údajov pre novú rodinu, alebo rozbalením poľa môžete individuálne vybrať, ktorý otec je zdrojom primárnych údajov, ktorá matka je zdrojom primárnych údajov a ktorá rodina (vybraná podľa ID Gramps) je zdrojom ostatných primárnych údajov.

Ak sa rozhodnete pokračovať v zlučovaní, vyberte príslušné prepínacie tlačidlo (tlačidlá) , aby ste určili zdroj (zdroje) primárnych údajov, ktoré sa majú použiť pre zlúčený rodinný záznam, a potom kliknite na tlačidlo . Deti z oboch manželstiev sa zlúčia do novej rodiny. Obaja otcovia sa zlúčia a udalosti od sekundárneho otca sa pripoja k primárnemu otcovi. Mená z vedľajšieho otca sa stanú alternatívnymi menami pre primárneho otca. To isté sa deje s oboma matkami. Udalosti týkajúce sa sekundárnej rodiny (napr. manželstvo a prípadný rozvod) sa prenesú do primárnej rodiny. Sekundárna rodina a záznam o osobe sekundárneho otca a matky sa z databázy vymažú. {{-}} ![[_media/MergeFamilies-dialog-DetailedSelection-section-expanded-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Zlúčenie rodín - sekcie &quot;Podrobný výber&quot; a &quot;Kontextové informácie&quot; rozšírené - dialóg - príklad]] {{-}}

### Zlúčenie udalostí

![[_media/MergeEvents-dialog-example-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Zlúčenie udalostí - dialóg - predvolený príklad]] Keď sú vybrané presne dve udalosti, výberom } vyvoláte dialógové okno.

Dialógové okno umožňuje rozhodnúť, či sa vybrané záznamy majú zlúčiť alebo nie.

Rozbalením poľa môžete zobraziť ďalšie informácie o zlúčení.

Ak sa napriek podobným názvom rozhodnete, že záznamy by sa nemali zlúčiť, môžete kliknutím na zavrieť dialógové okno bez vykonania akýchkoľvek zmien.

Ak sa rozhodnete pokračovať v zlučovaní, vyberte príslušné prepínacie tlačidlo, ktoré určíte:

- Typ
- Dátum
- Miesto
- Popis
- Identifikátor starého otca

ktorý sa má použiť pre zlúčený záznam, potom kliknite na {{-}} ![[_media/MergeEvents-dialog-DetailedSelection-section-expanded-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Zlúčenie udalostí - rozšírená časť &quot;Podrobný výber&quot; - dialóg - príklad]] {{-}}

### Zlúčenie miest

![[_media/MergePlaces-dialog-example-default-60.png|Obrázok {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Zlúčenie miest - dialógové okno - predvolený príklad]] Keď sú vybrané presne dve miesta, výberom } vyvoláte dialógové okno.

Rozbalením poľa } Zlúčenie miest - rozšírená časť "Podrobný výber" - dialógové okno - príklad\]\] {{-}}

### Zlúčenie zdrojov

![[_media/MergeSources-dialog-example-default-60.png|Obrázok {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Zlúčenie zdrojov - dialógové okno - predvolený príklad]] Keď sú vybrané presne dva zdroje, výberom } vyvoláte dialógové okno.

Rozbalením poľa } Zlúčenie zdrojov - rozšírená časť "Podrobný výber" - dialógové okno - príklad\]\] {{-}}

### Zlúčenie citácií

![[_media/MergeCitations-dialog-example-default-60.png|Obrázok {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Zlúčenie citácií - dialógové okno - predvolený príklad]] Keď sú vybrané presne dve citácie, výberom } vyvoláte dialógové okno.

Rozbalením poľa môžete zobraziť ďalšie informácie o zlúčení.

Dialógové okno umožňuje rozhodnúť, či sa vybrané záznamy majú zlúčiť alebo nie.

Ak sa napriek podobným názvom rozhodnete, že záznamy by sa nemali zlúčiť, môžete kliknutím na zavrieť dialógové okno bez vykonania akýchkoľvek zmien.

Ak sa rozhodnete pokračovať v zlučovaní, vyberte príslušné prepínacie tlačidlo, ktoré určíte:

- Zväzok/strana
- Dátum
- Dôvera
- ID gramatiky

ktoré sa majú použiť pre zlúčený záznam, a potom kliknite na tlačidlo .

Pozri tiež [Merge Citations...](wiki:Gramps_6.0_Wiki_Manual_-_Tools#Merge_citations) Nástroj. {{-}} ![[_media/MergeCitations-dialog-DetailedSelection-section-expanded-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Zlúčenie citácií - rozšírená časť &quot;Podrobný výber&quot; - dialógové okno - príklad]] {{-}}

### Zlúčenie archívov

![[_media/MergeRepositories-dialog-example-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Zlúčenie archívov - dialógové okno - predvolený príklad]] Keď sú vybrané presne dva repozitáre, výberom } vyvoláte dialógové okno.

Rozbalením poľa môžete zobraziť ďalšie informácie o zlúčení.

Dialógové okno vám umožňuje rozhodnúť, či sa vybrané záznamy majú zlúčiť alebo nie.

Ak sa napriek podobným názvom rozhodnete, že záznamy by sa nemali zlúčiť, môžete kliknutím na zavrieť dialógové okno bez vykonania akýchkoľvek zmien.

Ak sa rozhodnete pokračovať v zlučovaní, vyberte príslušné prepínacie tlačidlo, ktoré určíte:

- Názov
- Typ
- Identifikátor gramotnosti

ktoré sa majú použiť pre zlúčený záznam, a potom kliknite na tlačidlo . {{-}} ![[_media/MergeRepositories-dialog-DetailedSelection-section-expanded-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Zlúčenie archívov - rozšírená časť &quot;Podrobný výber&quot; - dialóg - príklad]] {{-}}

### Zlúčenie mediálnych objektov

![[_media/MergeMediaObjects-dialog-example-default-60.png|vpravo|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Zlúčenie mediálnych objektov - dialógové okno - predvolený príklad]] Keď sú vybrané presne dva Mediálne objekty, výberom } vyvoláte dialógové okno.

Rozbalením poľa môžete zobraziť ďalšie informácie o zlúčení.

Dialógové okno umožňuje rozhodnúť, či sa vybrané záznamy majú zlúčiť alebo nie.

Ak sa napriek podobným názvom rozhodnete, že záznamy by sa nemali zlúčiť, môžete kliknutím na zavrieť dialógové okno bez vykonania akýchkoľvek zmien.

Ak sa rozhodnete pokračovať v zlučovaní, vyberte príslušné prepínacie tlačidlo, ktoré určíte:

- Názov
- Cesta
- Dátum
- Identifikátor gramatiky

ktoré sa majú použiť pre zlúčený záznam, potom kliknite na tlačidlo {{-}} ![[_media/MergeMediaObjects-dialog-DetailedSelection-section-expanded-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Zlúčenie mediálnych objektov - rozšírená časť &quot;Podrobný výber&quot; - dialógové okno - príklad]] {{-}}

### Poznámky k zlúčeniu

![[_media/MergeNotes-dialog-example-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Zlúčenie poznámok - dialógové okno - predvolený príklad]] Keď sú vybrané presne dve poznámky, výberom vyvoláte dialógové okno.

Rozbalením poľa môžete zobraziť ďalšie informácie o zlúčení.

Dialógové okno umožňuje rozhodnúť, či sa vybrané záznamy majú zlúčiť alebo nie.

Ak sa rozhodnete, že záznamy by sa nemali zlúčiť napriek podobným názvom, môžete kliknutím na zavrieť dialógové okno bez vykonania akýchkoľvek zmien.

Ak sa rozhodnete pokračovať v zlučovaní, vyberte príslušné prepínacie tlačidlo, ktoré určíte:

- Text
- Typ
- Formát
- Identifikátor Gramps

ktorý sa má použiť pre zlúčený záznam, potom kliknite na tlačidlo {{-}} ![[_media/MergeNotes-dialog-DetailedSelection-section-expanded-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Zlúčenie poznámok - rozšírená časť &quot;Podrobný výber&quot; - dialóg - príklad]]

{{-}}

[Category:Sk:Documentation](wiki:Category:Sk:Documentation)
