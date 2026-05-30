---
title: Gramps 6.0 Wiki Manual - Reports - part 2/sk
categories:
- Plugins
- Sk:Documentation
managed: false
source: wiki-scrape (html-fallback)
wiki_revid: 111328
wiki_fetched_at: '2026-05-30T20:10:44Z'
lang: sk
---

|  |  |  |
|:---|:--:|---:|
| [**Predchádzajúca**](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_1/sk) | [**Index**](wiki:Gramps_6.0_Wiki_Manual/sk) | [**Nasledujúca**](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_3/sk) |

<div class="LanguageLinks">

|  |  |  |
|----|----|----|
| ![[_media/Gramps-config-language.png]] | **[Languages](wiki:Portal:Translators):**  | [English](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_2)     • <span lang="da"><a href="/wiki/index.php/Gramps_6.0_Wiki_Manual_-_Reports_-_part_2/da" class="mw-redirect" title="Gramps 6.0 Wiki Manual - Reports - part 2/da">dansk</a></span>  • <span lang="de"><a href="/wiki/index.php/Gramps_6.0_Wiki_Manual_-_Reports_-_part_2/de" class="mw-redirect" title="Gramps 6.0 Wiki Manual - Reports - part 2/de">Deutsch</a></span>  • <span lang="es">[español](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_2/es)</span>  • <span lang="fi"><a href="/wiki/index.php/Gramps_6.0_Wiki_Manual_-_Reports_-_part_2/fi" class="mw-redirect" title="Gramps 6.0 Wiki Manual - Reports - part 2/fi">suomi</a></span>  • <span lang="fr">[français](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_2/fr)</span>  • <span lang="he">[עברית](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_2/he)</span>      • <span lang="mk">[македонски](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_2/mk)</span>   • <span lang="nl"><a href="/wiki/index.php/Gramps_6.0_Wiki_Manual_-_Reports_-_part_2/nl" class="mw-redirect" title="Gramps 6.0 Wiki Manual - Reports - part 2/nl">Nederlands</a></span>     • <span lang="ru">[русский](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_2/ru)</span>   • <span lang="sq"><a href="/wiki/index.php/Gramps_6.0_Wiki_Manual_-_Reports_-_part_2/sq" class="mw-redirect" title="Gramps 6.0 Wiki Manual - Reports - part 2/sq">shqip</a></span>   • <span lang="sk"><span class="mw-selflink selflink">slovenčina</span></span> |

</div>

  
Naspäť na [Register správ](wiki:Gramps_6.0_Wiki_Manual_-_Reports/sk).

------------------------------------------------------------------------

Táto časť opisuje zastupiteľné hodnoty, ktoré možno použiť v rôznych správach dostupných v programe Gramps.

- [<span class="tocnumber">1</span> <span class="toctext">Zastupiteľné hodnoty</span>](#Zastupite.C4.BEn.C3.A9_hodnoty)
  - [<span class="tocnumber">1.1</span> <span class="toctext">Substitučné klávesy</span>](#Substitu.C4.8Dn.C3.A9_kl.C3.A1vesy)
    - [<span class="tocnumber">1.1.1</span> <span class="toctext">Ďalšie substitučné kľúče</span>](#.C4.8Eal.C5.A1ie_substitu.C4.8Dn.C3.A9_k.C4.BE.C3.BA.C4.8De)
    - [<span class="tocnumber">1.1.2</span> <span class="toctext">Predvolené zobrazené formáty</span>](#Predvolen.C3.A9_zobrazen.C3.A9_form.C3.A1ty)
    - [<span class="tocnumber">1.1.3</span> <span class="toctext">Vyradené premenné</span>](#Vyraden.C3.A9_premenn.C3.A9)
  - [<span class="tocnumber">1.2</span> <span class="toctext">Formát reťazcov</span>](#Form.C3.A1t_re.C5.A5azcov)
    - [<span class="tocnumber">1.2.1</span> <span class="toctext">Formátovanie mien</span>](#Form.C3.A1tovanie_mien)
    - [<span class="tocnumber">1.2.2</span> <span class="toctext">Formátovanie dátumov</span>](#Form.C3.A1tovanie_d.C3.A1tumov)
    - [<span class="tocnumber">1.2.3</span> <span class="toctext">Formátovanie miest</span>](#Form.C3.A1tovanie_miest)
    - [<span class="tocnumber">1.2.4</span> <span class="toctext">Pravidlá pre formátovacie reťazce</span>](#Pravidl.C3.A1_pre_form.C3.A1tovacie_re.C5.A5azce)
  - [<span class="tocnumber">1.3</span> <span class="toctext">Kontrolné premenné</span>](#Kontroln.C3.A9_premenn.C3.A9)
  - [<span class="tocnumber">1.4</span> <span class="toctext">Zoskupovanie</span>](#Zoskupovanie)
    - [<span class="tocnumber">1.4.1</span> <span class="toctext">Pravidlá pre skupiny</span>](#Pravidl.C3.A1_pre_skupiny)
    - [<span class="tocnumber">1.4.2</span> <span class="toctext">Príklady</span>](#Pr.C3.ADklady)
  - [<span class="tocnumber">1.5</span> <span class="toctext">Atribúty</span>](#Atrib.C3.BAty)
  - [<span class="tocnumber">1.6</span> <span class="toctext">Udalosti</span>](#Udalosti)
    - [<span class="tocnumber">1.6.1</span> <span class="toctext">Reťazce formátu udalosti</span>](#Re.C5.A5azce_form.C3.A1tu_udalosti)
    - [<span class="tocnumber">1.6.2</span> <span class="toctext">Poznámky k atribútom a udalostiam</span>](#Pozn.C3.A1mky_k_atrib.C3.BAtom_a_udalostiam)
  - [<span class="tocnumber">1.7</span> <span class="toctext">Oddeľovače</span>](#Odde.C4.BEova.C4.8De)

# <span id="Zastupiteľné_hodnoty"></span><span id="Zastupite.C4.BEn.C3.A9_hodnoty" class="mw-headline">Zastupiteľné hodnoty</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Mnohé z [grafické reporty](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_4#Graphical_Reports) umožňujú prispôsobiť informácie, ktoré sa v nich zobrazujú. Nahradenie premennej je metóda, ktorá sa používa na nahradenie konkrétneho symbolu (kľúča) špecifickými informáciami o osobe v databáze.

Napríklad:

<table>
<tbody>
<tr>
<th colspan="2">Substitučné kľúče</th>
<th colspan="2">Zobrazí sa ako: (osoba je živá)</th>
</tr>
&#10;<tr>
<th>Riadok 1</th>
<td><code>$n</code></td>
<td>Riadok 1</td>
<td>Smith, Edwin Michael</td>
</tr>
<tr>
<th>Riadok 2</th>
<td><code>b. $b{ na $B}</code></td>
<td>Riadok 2</td>
<td>b. 1961-05-24 v San Jose, Santa Clara Co., CA</td>
</tr>
<tr>
<th>Riadok 3</th>
<td><code>d. $d&lt; na &gt;$D</code></td>
<td>Riadok 3</td>
<td>d.</td>
</tr>
</tbody>
</table>

V ďalšej časti nasleduje zoznam všetkých dostupných premenných (The Substitution Keys).

- Ak si želáte zobrazovať mená, dátum alebo informácie o mieste inak, môžete na to použiť [Format Strings](#Format_Strings).
- Existujú aj [Kontrolné premenné](#Kontroln.C3.A9_premenn.C3.A9) na zobrazenie špeciálnych znakov (napríklad znaku dolára).
- Na voliteľné zobrazenie informácií môžete použiť aj [Skupiny](#Grouping). Vo vyššie uvedenom príklade **Riadok 2** používa zoskupovanie na zobrazenie `' na '` len vtedy, keď je známe miesto narodenia.
- Spolu s [Udalosti](#Events) môžete vypísať takmer čokoľvek.
- A nakoniec [Oddeľovače](#Separators), aby bol váš život kompletný. Vo vyššie uvedenom príklade **Riadok 3'**, používa toto na zobrazenie `' na '` len vtedy, keď je známy dátum aj miesto narodenia.

## <span id="Substitučné_klávesy"></span><span id="Substitu.C4.8Dn.C3.A9_kl.C3.A1vesy" class="mw-headline">Substitučné klávesy</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

<table class="wikitable sortable">
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<tbody>
<tr>
<th colspan="2">Osobné premenné</th>
<th colspan="2">Manželské premenné</th>
</tr>
&#10;<tr>
<th>$n</th>
<td>Zobrazí meno osoby</td>
<td>$s</td>
<td>Zobrazí meno manžela/manželky osoby</td>
</tr>
<tr>
<th>$i</th>
<td>Zobrazí identifikátor Gramps pre danú osobu.</td>
<td>$j</td>
<td>Zobrazí ID Gramps pre manželstvo.</td>
</tr>
<tr>
<th>$b</th>
<td>Zobrazí dátum narodenia osoby</td>
<td>$m</td>
<td>Zobrazí dátum sobáša osoby a manžela/manželky.</td>
</tr>
<tr>
<th>$B</th>
<td>Zobrazuje miesto narodenia osoby</td>
<td>$M</td>
<td>Zobrazuje miesto sobáša osoby a manžela/manželky.</td>
</tr>
<tr>
<th>$d</th>
<td>Zobrazuje dátum úmrtia osoby</td>
<td>$v</td>
<td>Zobrazí dátum rozvodu osoby a manžela/manželky.</td>
</tr>
<tr>
<th>$D</th>
<td>Zobrazí miesto úmrtia osoby</td>
<td>$V</td>
<td>Zobrazí miesto rozvodu osoby a manžela/manželky.</td>
</tr>
<tr>
<th>$a</th>
<td>Zobrazí atribút o osobe.
<p>Viac informácií nájdete v <a href="#Attributes">Attributes</a>.</p></td>
<td>$u</td>
<td>Zobrazí atribút o manželstve.
<p>Viac pozri <a href="#Attrib.C3.BAty">Attribúty</a>.</p></td>
</tr>
<tr>
<th>$e</th>
<td>Zobrazí informácie o udalosti o osobe.
<p>Viac informácií nájdete v <a href="#Events">Events</a>.</p></td>
<td>$t</td>
<td>Zobrazí informácie o udalosti o manželstve.
<p>Viac informácií nájdete v <a href="#Events">Events</a>.</p></td>
</tr>
</tbody>
</table>

Všetky premenné Manželstvo sú definované preferovaným manželským partnerom osoby v programe Gramps. Ak osoba nikdy nebola vydatá, tieto premenné nezobrazia nič.

#### <span id="Ďalšie_substitučné_kľúče"></span><span id=".C4.8Eal.C5.A1ie_substitu.C4.8Dn.C3.A9_k.C4.BE.C3.BA.C4.8De" class="mw-headline">Ďalšie substitučné kľúče</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

- `$T` Zobrazí dnešný dátum.

### <span id="Predvolené_zobrazené_formáty"></span><span id="Predvolen.C3.A9_zobrazen.C3.A9_form.C3.A1ty" class="mw-headline">Predvolené zobrazené formáty</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

|  |  |
|----|----|
| \$n \$s | Mená sa zobrazia tak, ako je nastavené v položke "Formát mena:" na karte Zobrazenie v predvoľbách Gramps |
| \$B \$D \$M \$V | Miesto bude štandardne zobrazovať názov miesta |
| \$b \$d \$m \$v \$T | Dátumy sa budú zobrazovať tak, ako je nastavené vo "Formáte dátumu:" na karte Zobrazenie v predvoľbách programu Gramps |
| \$e \$t | Udalosti budú štandardne zobrazovať popis |

### <span id="Vyradené_premenné"></span><span id="Vyraden.C3.A9_premenn.C3.A9" class="mw-headline">Vyradené premenné</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Niektoré staré premenné boli zrušené, pretože ich nahradili [Format Strings](#Format_Strings). Tu je teda zoznam týchto premenných a spôsob, ako dosiahnuť ich výsledky:

|  |  |  |
|----|----|----|
| Stará premenná | Ako ju zobraziť teraz | Čo sa zobrazí |
| \$f | \$n | Názov - ako pri zobrazení mena dedka v časti Predvoľby |
| \$n | \$n(g f) | Name - FirstName LastName |
| \$N | \$n(f, g) | Name - LastName, FirstName (všimnite si výslovnej čiarky) |
| \$nC | \$n(g F) | Name - FirstName LastName vo veľkých písmenách |
| \$NC | \$n(F, g) | Name - LastName in UPPER case, FirstName |
| \$by | \$b(yyyy) | Dátum narodenia, len rok |
| \$dy | \$d(rrrr) | Dátum úmrtia, len rok |
| \$my | \$m(rrrr) | Dátum preferovaného manželstva, len rok |
| \$p | \$s | Preferované meno manžela/manželky podľa zobrazenia mena dedka v časti Predvoľby |
| \$s | \$s(g f) | Preferované meno manžela/manželky - Krstné meno Priezvisko |
| \$S | \$s(f, g) | Preferované meno manžela/manželky - priezvisko, meno |
| \$sC | \$s(g F) | Preferované meno manžela/manželky - FirstName LastName vo veľkých písmenách |
| \$SC | \$s(F, g) | Preferované meno manžela/manželky - Priezvisko v hornom riadku, Meno |

## <span id="Formát_reťazcov"></span><span id="Form.C3.A1t_re.C5.A5azcov" class="mw-headline">Formát reťazcov</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Formátovacie reťazce sa používajú na zobrazenie mien a dátumov inak, ako sú priradené v časti Predvoľby gramatiky. Tu je syntax formátovacieho reťazca:

\$***<span class="kbd" style="background:#D3D3D3; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">key</span>***(formátovací reťazec)  
kde: ***<span class="kbd" style="background:#D3D3D3; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">key</span>*** je jeden z nasledujúcich znakov: 'nsijbmBMdvDVauet'

Formátovací reťazec je akýkoľvek text, oddeľovače alebo formátovacie kódy (definované nižšie) na zobrazenie informácií o osobe.

### <span id="Formátovanie_mien"></span><span id="Form.C3.A1tovanie_mien" class="mw-headline">Formátovanie mien</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Pre mená `($n $s)` môžete použiť nasledujúce formátovacie kódy na rôzne zobrazenie mena.

|  |  |  |  |
|----|----|----|----|
| t | Title | f | Dané meno |
| x | Obvyklé meno. Volacie meno, ak existuje, inak krstné meno | c | Volacie meno |
| n | Nick meno | s | Suffix |
| l | Prímeno | g | Prezývka rodiny |

Tieto kódy možno písať veľkými písmenami, aby sa výsledok zobrazil veľkými písmenami.

Napríklad:

<table class="wikitable sortable">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<th>Kód formátovania</th>
<th>Zobrazuje</th>
</tr>
&#10;<tr>
<td><pre><code>$n(L, f) ($n(c)), $n(L, f){ ($n(c))}
$s(f l s)</code></pre></td>
<td><pre><code>SMITH, Edwin Michael (), SMITH, Edwin Michael
Janice Ann Adams</code></pre></td>
</tr>
</tbody>
</table>

<table style="width:80%;margin-top:+.7em;margin-bottom:+.7em;background-color: #ddffcc85;border:1px solid #ccc; padding: 5px" data-align="center">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 60px">![[_media/Gramps-notes.png]]</td>
<td><div style="font-size:110%">
<strong>Poznámka:</strong>
</div>
<hr />
<p>Ak chcete vo formátovacom reťazci vypísať znak 'c' (alebo niektorý z ďalších formátovacích kódov), musíte predň najprv pridať &lt;kód&gt;'\'&lt;/kód&gt;. Viac informácií nájdete v časti <a href="#Kontroln.C3.A9_premenn.C3.A9">Kontrolné premenné</a>.</p></td>
</tr>
</tbody>
</table>

<table style="width:80%;margin-top:+.7em;margin-bottom:+.7em;background-color: #ddffcc85;border:1px solid #ccc; padding: 5px" data-align="center">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 60px">![[_media/Gramps-notes.png]]</td>
<td><div style="font-size:110%">
<strong>Poznámka:</strong>
</div>
<hr />
<p>Vlnité zátvorky <code>{ }</code> sa používajú na skrytie informácií. Tu sa používa okolo <code>' ($n(c))'</code>, aby sa nezobrazovalo <code>' ()'</code>, ak osoba nemá meno volajúceho. Viac informácií nájdete v časti <a href="#Zoskupovanie">Zoskupovanie</a>.</p></td>
</tr>
</tbody>
</table>

### <span id="Formátovanie_dátumov"></span><span id="Form.C3.A1tovanie_d.C3.A1tumov" class="mw-headline">Formátovanie dátumov</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Pre všetky dátumové premenné `($b $d $m $v)` môžete použiť nasledujúce formátovacie kódy:

{class="wikitable sortable"

\|- !yyyy \|Rok ako štvormiestne číslo !yyy \|Rok s minimálne tromi číslicami \|- !yy \|Rok od 00 do 99 !y \|Rok, od 0 do 99 \|- !mmmm  
**MMMM** \|Plný názov mesiaca  
Celý názov V KAPITÁLKÁCH !mmm  
**MMM'** \|Zkrátený názov mesiaca  
Skrátený názov V KAPITÁLKACH \|- !mm \|Mesiac, od 00 do 12 !m \|Mesiac, od 0 do 12 \|- !dd \|Deň, od 00 do 31 !d \|Deň, od 0 do 31 \|- !o \|Typ dátumu (modifikátor) ! \| \|}

Napríklad:

<table class="wikitable sortable">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<th>Formátovací kód</th>
<th>zobrazuje</th>
</tr>
&#10;<tr>
<td><pre><code>$b(mmm-dd rr)
$m(rrrr/mmm/d)
$b(mmm-dd rrr)</code></pre></td>
<td><pre><code>24. mája 61
1995/Máj/27
Jun-04 85</code></pre></td>
</tr>
</tbody>
</table>

<table style="width:80%;margin-top:+.7em;margin-bottom:+.7em;background-color: #ffeeaa85;border:1px solid #ccc; padding: 5px" data-align="center">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 60px">![[_media/Gnome-important.png]]</td>
<td><div style="font-size:110%">
<strong>Pre typy dátumov (modifikátor)</strong>
</div>
<hr />
<p>V tejto chvíli sú podporované len "Pred", "Po" a "O". všetky ostatné nezobrazia nič.<br />
A pre dátumové rozpätie a dátumové rozsahy sa zobrazí len počiatočný (prvý) dátum.</p></td>
</tr>
</tbody>
</table>

### <span id="Formátovanie_miest"></span><span id="Form.C3.A1tovanie_miest" class="mw-headline">Formátovanie miest</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Pre všetky premenné miesta `($B $D $M $V)` môžete použiť nasledujúce formátovacie kódy:

|     |         |     |     |             |
|-----|---------|-----|-----|-------------|
| e   | Street  |     | l   | Lokalita    |
| c   | City    |     | u   | Kraj        |
| s   | Stát    |     | p   | Postal Code |
| n   | Krajina |     | t   | Titul       |
| x   | Dĺžka   |     | y   | Šírka       |

Tieto kódy možno písať veľkými písmenami, aby sa výsledok zobrazil veľkými písmenami.

Napríklad:

<table class="wikitable sortable">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<th>Kód formátovania</th>
<th>zobrazuje</th>
</tr>
&#10;<tr>
<td><pre><code>$B
$B(c, s, N)</code></pre></td>
<td><pre><code>Nemocnica sv.
Carmel, IN, USA</code></pre></td>
</tr>
</tbody>
</table>

### <span id="Pravidlá_pre_formátovacie_reťazce"></span><span id="Pravidl.C3.A1_pre_form.C3.A1tovacie_re.C5.A5azce" class="mw-headline">Pravidlá pre formátovacie reťazce</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

- Vo vnútri formátovacieho reťazca sa vypíše čokoľvek
- Na zobrazenie vecí ako `')'` a formátovacích kódov je potrebné použiť [Control Variables](#Control_Variables).
- Oddeľovače môžu byť vo vnútri formátovacích reťazcov.
- Aspoň JEDEN formátovací kód musí niečo zobrazovať, aby sa zobrazil CELÝ formátovací reťazec

Príklady:

<table class="wikitable sortable">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<th>Formátovací kód</th>
<th>zobrazuje</th>
</tr>
&#10;<tr>
<td><pre><code>$n(f l)
b. $b {at $B
{d. $d $D</code></pre></td>
<td><pre><code>Edwin Michael Smith
b. 1961-05-24 v San Jose, Santa Clara Co., CA</code></pre>
<strong><kbd style="background:#D3D3D3; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">Osoba je stále nažive (alebo nie sú prítomné žiadne informácie), takže riadok bol odstránený.</kbd></strong></td>
</tr>
</tbody>
</table>

## <span id="Kontrolné_premenné"></span><span id="Kontroln.C3.A9_premenn.C3.A9" class="mw-headline">Kontrolné premenné</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Riadiace premenné umožňujú vytlačiť znaky, ktoré sú špeciálne pre hodnoty Substitution v rámci zobrazenia.

Napríklad znak dolára "\$" sa používa na zaznamenanie začiatku premennej. Ak chcete vytlačiť znak dolára, použijete riadiaci znak, napríklad '\\'

|                   |                                   |
|-------------------|-----------------------------------|
| Riadiace premenné | Výsledok                          |
| \\                | Zobrazí jeden \<kód\>'\$'\</kód\> |
| \\                | Zobrazí jeden \<kód\>'\\          |
| \\                | Zobrazí jeden `'('`               |
| \\                | Zobrazí jeden \<kód\>')'          |
| \\                | Zobrazí jeden `'{'`               |
| \\                | Zobrazí jeden `'}'`               |
| \\                | Zobrazí jeden \<kód\>'\<'         |
| \\                | Zobrazí jeden \<kód\>'\>'         |

V podstate sa vypíše všetko, čo nasleduje za `'\'`.

<table style="width:80%;margin-top:+.7em;margin-bottom:+.7em;background-color: #ddffcc85;border:1px solid #ccc; padding: 5px" data-align="center">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 60px">![[_media/Gramps-notes.png]]</td>
<td><div style="font-size:110%">
<strong>Poznámka:</strong>
</div>
<hr />
<p>Keď sa nachádzate vo vnútri formátovacieho reťazca, možno budete musieť použiť tento spôsob na zobrazenie znaku, ktorý by za normálnych okolností bol formátovacím kódom.</p></td>
</tr>
</tbody>
</table>

Napríklad:

<table class="wikitable sortable">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<th>Formátovací kód:</th>
<th>zobrazí</th>
</tr>
&#10;<tr>
<td><pre><code>$b(m hi mama)
$b(m hi \mo\m)</code></pre></td>
<td><pre><code>5 hi 5o5
5 hi mama</code></pre>
<strong><kbd style="background:#D3D3D3; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">ako sa táto osoba narodila v piatom mesiaci.</kbd></strong></td>
</tr>
</tbody>
</table>

## <span id="Zoskupovanie" class="mw-headline">Zoskupovanie</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Existujú prípady, keď nechcete, aby sa určitý text zobrazoval.

Vezmite si príklad:

|  |  |  |
|----|----|----|
| Kód formátovania | Známy je len dátum | Známe je len miesto |
| \<kód\>zomrel dňa \$d v \$D\</kód\> | `zomrel dňa 1975-06-26 v` | `zomrel dňa v Reno, Washoe Co., NV`` ` |

Ani jeden z týchto zobrazených výsledkov nie je veľmi prijateľný.

Ale pri skupinách (označených **{}**) môžete voliteľne vypísať informácie, ak premenná v nich obsahuje informácie.

|  |  |  |
|----|----|----|
| Kód formátovania | Známy je len dátum | Známe je len miesto |
| `died{ on $d}{ at $D}` | `zomrel dňa 1975-06-26` | `zomrel v Reno, Washoe Co., NV` |

Čo je vhodnejší zobrazený výsledok ako v prvom príklade.

### <span id="Pravidlá_pre_skupiny"></span><span id="Pravidl.C3.A1_pre_skupiny" class="mw-headline">Pravidlá pre skupiny</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Skupina sa zobrazí len vtedy, ak existuje aspoň jedna premenná, ktorá niečo zobrazuje. Ak teda skupina obsahuje iba text a/alebo premenné, pri ktorých nie sú známe informácie, celá skupina sa nevypíše.

Skupiny môžu byť aj vnorené. V takom prípade (ako je uvedené nižšie) sa vonkajšia skupina zobrazí len vtedy, ak existuje aspoň jedna premenná, ktorá niečo zobrazuje vo vonkajšej skupine alebo v niektorej z podskupín.

Skupiny možno použiť aj na odstránenie textu. Ak si želáte nezobraziť celý riadok, \<kód\>'-'\</kód\> na začiatku riadku odstráni celý riadok zo zobrazenia, ak platí vyššie uvedené pravidlo.

Ak si neželáte, aby sa zobrazil vyššie uvedený kód (pre informácie o úmrtí) (osoba je nažive alebo ešte nepoznáte informácie), upravte kód tak, aby vyzeral nasledovne:

- `-{died{ on $d}{ at $D}`

### <span id="Príklady"></span><span id="Pr.C3.ADklady" class="mw-headline">Príklady</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Toto skryje `'('` a `')'`, ak informácie o rozvode nie sú známe (alebo ešte nie sú manželia).

- `m. $m $M {- ($v(rrrr))`

Zobrazte len niektoré informácie o manželovi, ak je ženatý, alebo odstráňte celý riadok, ak nikdy nebol ženatý:

- `{$s $m(rrrr) {- $v(\(rrrr))}}`

## <span id="Atribúty"></span><span id="Atrib.C3.BAty" class="mw-headline">Atribúty</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Atribúty nemajú formátovací reťazec. Namiesto toho je názov atribútu umiestnený vo vnútri `[]`. Tu je syntax pre atribút:

\$***<span class="kbd" style="background:#D3D3D3; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">key</span>***\[názov atribútu\]  
kde: ***<span class="kbd" style="background:#D3D3D3; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">key</span>*** je jeden z nasledujúcich znakov: 'au'

Napríklad:

<table class="wikitable sortable">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<th>Kód formátovania</th>
<th>zobrazuje</th>
</tr>
&#10;<tr>
<td><pre><code>$a[Profesia]
$a[Číslo sociálneho poistenia]
$a[Odkázaná celková suma \$]</code></pre></td>
<td><pre><code>Programátor
7A3-29-F1C6
3.00USD</code></pre></td>
</tr>
</tbody>
</table>

## <span id="Udalosti" class="mw-headline">Udalosti</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Udalosti majú rovnakú počiatočnú štruktúru ako atribúty, `$e` alebo `$t` a názov udalosti v `[]`, ale udalosti majú za názvom ďalší formátovací reťazec na zobrazenie popisu, dátumu, miesta, id a atribútov, ktoré sú s ňou spojené. Každú z týchto položiek možno vo formátovacom reťazci zobraziť pomocou a , a "n", "d", "D", "i" a "a" v uvedenom poradí. Tu je syntax pre udalosť:

\$***<span class="kbd" style="background:#D3D3D3; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">key</span>***\[názov atribútu\](formátovací reťazec)  
kde: ***<span class="kbd" style="background:#D3D3D3; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">key</span>*** je jeden z nasledujúcich znakov: 'et'

### <span id="Reťazce_formátu_udalosti"></span><span id="Re.C5.A5azce_form.C3.A1tu_udalosti" class="mw-headline">Reťazce formátu udalosti</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Reťazec formátu udalosti sa používa na zobrazenie informácií o udalosti. Tu sú uvedené kódy formátu na zobrazenie častí udalosti:

|  |  |  |  |  |
|----|----|----|----|----|
| Kód formátovania | zobrazí |  | Formátovací kód | zobrazuje |
| n | Popis |  | i | Identifikátor udalosti |
| d | Dátum udalosti\* |  | D | Miesto udalosti\* |
| a | Atribúty udalosti\*\* |  |  |  |

\*Tieto premenné môžu mať samy o sebe formátovacie reťazce. Dátum a miesto môžu byť formátované pomocou formátovacieho reťazca, ako je definované v [Formátové reťazce](#Form.C3.A1tov.C3.A9_re.C5.A5azce).

\*\*Atribút musí mať názov atribútu v \[\] a je formátovaný podľa vyššie uvedeného.

Napríklad:

<table class="wikitable sortable">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<th>Kód formátovania</th>
<th>zobrazuje</th>
</tr>
&#10;<tr>
<td><pre><code>$e[Prvé sväté prijímanie](d(rrrr-mm-d))
$e[Bar micva](n&lt; at &gt; D)
$e[Narodenie](d(rrrr mm/dd) D)</code></pre></td>
<td><pre><code>2009-11-6
Jerryho bar micva v Opasovom dome
2007 05/23 Dom babičky</code></pre></td>
</tr>
</tbody>
</table>

A:

<table class="wikitable sortable">
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<tbody>
<tr>
<th>Formátovací kód</th>
<th></th>
<th>zobrazuje</th>
</tr>
&#10;<tr>
<td><pre><code>$b(rrrr-Mmm-dd)
$M</code></pre></td>
<td>je rovnaký ako</td>
<td><pre><code>$e[Narodenie](d(rrrr-Mmm-dd))
$t[Manželstvo](D)</code></pre></td>
</tr>
</tbody>
</table>

### <span id="Poznámky_k_atribútom_a_udalostiam"></span><span id="Pozn.C3.A1mky_k_atrib.C3.BAtom_a_udalostiam" class="mw-headline">Poznámky k atribútom a udalostiam</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Názvy atribútov a udalostí sú povinné. `'$a'` alebo `'$a[]'` nezobrazí nič.

Názvy atribútov a udalostí môžu mať v sebe špeciálne znaky. Najmä `']'` a `')'`. V takom prípade budete musieť použiť [Control Variables](#Control_Variables).

## <span id="Oddeľovače"></span><span id="Odde.C4.BEova.C4.8De" class="mw-headline">Oddeľovače</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Oddeľovače sú špeciálne skupiny "iba textové" vnútri `'<'` a `'>'`, ktoré podmienečne zobrazujú oddeľovač (ako `', '` alebo `' - '`) medzi dvoma skupinami, premennými, formátovacími kódmi alebo textom.

Oddeľovače sa zobrazujú podmienečne v závislosti od týchto pravidiel:

- Premenná, ktorá **nezobrazuje** nič, odstráni zo zobrazovacieho riadku iba seba a oddeľovač, ktorý je naľavo od nej.
- Ak sa vľavo nenachádza žiadny oddeľovač, tá istá premenná odstráni seba a oddeľovač, ktorý je vpravo od nej, zo zobrazeného riadku.
- Ak sú dva oddeľovače spolu, zo zobrazeného riadku sa odstráni ľavý a pravý sa ponechá.
- Oddelovače na začiatku alebo na konci zobrazeného riadka (alebo formátovacích reťazcov) sa odstránia.

Vezmite si tento príklad formátovacieho kódu:

- `$s(f l s)<, >$m(yyyy)< @ >$M< - >$v(\(yyyy\))`

Tu sú niektoré veci, ktoré sa môžu stať:

<table class="wikitable sortable">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<th>Možnosť</th>
<th>Výsledok</th>
</tr>
&#10;<tr>
<td>Ak <strong>žiadna</strong> z premenných nie je známa</td>
<td>Nijaký z oddeľovačov sa nezobrazí</td>
</tr>
<tr>
<td>Ak je známa len jedna premenná <strong>je</strong></td>
<td>Vytlačí sa len táto premenná. Nevypíšu sa žiadne oddeľovače.</td>
</tr>
<tr>
<td>Ak je známe iba meno manžela alebo manželky <strong>nie je</strong></td>
<td>Prvý oddeľovač sa nezobrazí</td>
</tr>
<tr>
<td>Ak nie je známy iba dátum sobáša <strong>nie je'</strong></td>
<td>Prvý oddeľovač sa nezobrazí. Zostane nám:
<p>A na vypísanie druhého oddeľovača musí byť známy len dátum rozvodu.</p></td>
</tr>
<tr>
<td>Ak nie je známy iba dátum rozvodu <strong>nie je'</strong></td>
<td>druhý oddeľovač sa nezobrazí</td>
</tr>
</tbody>
</table>

Oddeľovače môžu byť vnútri formátovacích reťazcov:

- `$n(<0>T< >L<, >f< >s)`

Na rozdiel od skupín nemôžu oddeľovače prechádzať cez/zvonku formátovacích reťazcov. Takže oddeľovač `<0>` sa NIKDY nezobrazí. Bez ohľadu na to, čo sa nachádza na ľavej strane premennej.

Tu je užitočný príklad:

- `{({b. $b}<, >{d. $d})}`

Toto spôsobí:

<table class="wikitable sortable">
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td>Vonkajší () vypíšte len vtedy, ak sa zobrazí dátum narodenia alebo úmrtia<br />
&#10;<p>Stredový oddeľovač sa zobrazí len vtedy, ak sú známe oba dátumy.<br />
Takže tu sú niektoré veci, ktoré by sa mohli zobraziť</p>
<table>
<tbody>
<tr>
<td>&lt;kód&gt;(nar. 1970-4-8)&lt;/kód&gt;</td>
<td><code>(d. 2012-3-9)</code></td>
<td><code>(nar. 1970-4-8, z. 2012-3-9)</code></td>
<td>alebo sa riadok vôbec nevytlačí.</td>
</tr>
</tbody>
</table></td>
</tr>
<tr>
<td>Nebudeme vidieť veci ako napr:
<table>
<tbody>
<tr>
<td><code>()</code></td>
<td><code>(, )</code></td>
<td><code>(b.)</code></td>
<td><code>(b., )</code></td>
<td><code>(d.)</code></td>
</tr>
<tr>
<td><code>(, d.)</code></td>
<td><code>(b. 1970-4-8, )</code></td>
<td><code>(b. 1970-4-8, d.)</code></td>
<td><code>(, d. 2012-3-9)</code></td>
<td><code>(b., d. 2012-3-9)</code></td>
</tr>
</tbody>
</table></td>
</tr>
</tbody>
</table>

  

------------------------------------------------------------------------

Naspäť na [Register správ](wiki:Gramps_6.0_Wiki_Manual_-_Reports/sk).

|  |  |  |
|:---|:--:|---:|
| [**Predchádzajúca**](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_1/sk) | [**Index**](wiki:Gramps_6.0_Wiki_Manual/sk) | [**Nasledujúca**](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_3/sk) |

<div class="LanguageLinks">

|  |  |  |
|----|----|----|
| ![[_media/Gramps-config-language.png]] | **[Languages](wiki:Portal:Translators):**  | [English](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_2)     • <span lang="da"><a href="/wiki/index.php/Gramps_6.0_Wiki_Manual_-_Reports_-_part_2/da" class="mw-redirect" title="Gramps 6.0 Wiki Manual - Reports - part 2/da">dansk</a></span>  • <span lang="de"><a href="/wiki/index.php/Gramps_6.0_Wiki_Manual_-_Reports_-_part_2/de" class="mw-redirect" title="Gramps 6.0 Wiki Manual - Reports - part 2/de">Deutsch</a></span>  • <span lang="es">[español](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_2/es)</span>  • <span lang="fi"><a href="/wiki/index.php/Gramps_6.0_Wiki_Manual_-_Reports_-_part_2/fi" class="mw-redirect" title="Gramps 6.0 Wiki Manual - Reports - part 2/fi">suomi</a></span>  • <span lang="fr">[français](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_2/fr)</span>  • <span lang="he">[עברית](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_2/he)</span>      • <span lang="mk">[македонски](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_2/mk)</span>   • <span lang="nl"><a href="/wiki/index.php/Gramps_6.0_Wiki_Manual_-_Reports_-_part_2/nl" class="mw-redirect" title="Gramps 6.0 Wiki Manual - Reports - part 2/nl">Nederlands</a></span>     • <span lang="ru">[русский](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_2/ru)</span>   • <span lang="sq"><a href="/wiki/index.php/Gramps_6.0_Wiki_Manual_-_Reports_-_part_2/sq" class="mw-redirect" title="Gramps 6.0 Wiki Manual - Reports - part 2/sq">shqip</a></span>   • <span lang="sk"><span class="mw-selflink selflink">slovenčina</span></span> |

</div>

<table style="width:90%;margin-top:+.7em;margin-bottom:+.7em;background-color: #c0f0ff;border:1px solid #ccc; padding: 5px" data-align="center">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td>![[_media/Gnome-important.png]]</td>
<td style="text-align: left;"><strong>Special copyright notice:</strong> All edits to this page need to be under two different copyright licenses:
<ul>
<li>GNU Free Documentation License 1.2 - see <a href="/wiki/index.php/Gramps:Copyrights" title="Gramps:Copyrights">wiki copyright</a></li>
<li>GPL - see <a href="/wiki/index.php/Gramps:Manualcopyright" title="Gramps:Manualcopyright">manual copyright</a></li>
</ul>
<p>These licenses allow the Gramps project to maximally use this wiki manual as free content in future Gramps versions. If you do not agree with this dual license, then do not edit this page. You may only link to other pages within the wiki which fall only under the GFDL license via external links (using the syntax: [https://www.gramps-project.org/...]), not via internal links.<br />
Also, only use the known <a href="/wiki/index.php/Gramps_6.0_Wiki_Manual_-_Preface#Typographical_conventions" title="Gramps 6.0 Wiki Manual - Preface">Typographical conventions</a></p></td>
</tr>
</tbody>
</table>
