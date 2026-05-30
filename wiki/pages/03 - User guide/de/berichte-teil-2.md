---
title: De:Gramps 6.0 Wiki Handbuch - Berichte - Teil 2
categories:
- De:Dokumentation
- Plugins
managed: false
source: wiki-scrape (html-fallback)
wiki_revid: 117895
wiki_fetched_at: '2026-05-30T16:15:56Z'
lang: de
---

|  |  |  |
|:---|:--:|---:|
| [**Zurück**](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte_-_Teil_1) | [**Index**](wiki:De:Gramps_6.0_Wiki_Handbuch) | [**Nächste**](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte_-_Teil_3) |

<div class="LanguageLinks">

|  |  |  |
|----|----|----|
| ![[_media/Gramps-config-language.png]] | **[Sprachen](wiki:Portal:Translators):**  | [English](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_2)     • <span lang="da"><a href="/wiki/index.php/Gramps_6.0_Wiki_Manual_-_Reports_-_part_2/da" class="mw-redirect" title="Gramps 6.0 Wiki Manual - Reports - part 2/da">dansk</a></span>  • <span lang="de"><span class="mw-selflink selflink">Deutsch</span></span>  • <span lang="es">[español](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_2/es)</span>  • <span lang="fi"><a href="/wiki/index.php/Gramps_6.0_Wiki_Manual_-_Reports_-_part_2/fi" class="mw-redirect" title="Gramps 6.0 Wiki Manual - Reports - part 2/fi">suomi</a></span>  • <span lang="fr">[français](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_2/fr)</span>  • <span lang="he">[עברית](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_2/he)</span>      • <span lang="mk">[македонски](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_2/mk)</span>   • <span lang="nl"><a href="/wiki/index.php/Gramps_6.0_Wiki_Manual_-_Reports_-_part_2/nl" class="mw-redirect" title="Gramps 6.0 Wiki Manual - Reports - part 2/nl">Nederlands</a></span>      • <span lang="ru">[русский](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_2/ru)</span>   • <span lang="sq"><a href="/wiki/index.php/Gramps_6.0_Wiki_Manual_-_Reports_-_part_2/sq" class="mw-redirect" title="Gramps 6.0 Wiki Manual - Reports - part 2/sq">shqip</a></span>   • <span lang="sk">[slovenčina](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_2/sk)</span> |

</div>

  
Zurück zur [Übersicht der Berichte](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte).

------------------------------------------------------------------------

Dieser Abschnitt beschreibt die Platzhalter die in den Verschiedenen Berichten, die in Gramps verfügbar sind verwendet werden können.

- [<span class="tocnumber">1</span> <span class="toctext">Werte ersetzen</span>](#Werte_ersetzen)
  - [<span class="tocnumber">1.1</span> <span class="toctext">Die Platzhalter</span>](#Die_Platzhalter)
    - [<span class="tocnumber">1.1.1</span> <span class="toctext">Andere Platzhalter</span>](#Andere_Platzhalter)
    - [<span class="tocnumber">1.1.2</span> <span class="toctext">Standardanzeigeformate</span>](#Standardanzeigeformate)
    - [<span class="tocnumber">1.1.3</span> <span class="toctext">Veraltete Variablen</span>](#Veraltete_Variablen)
  - [<span class="tocnumber">1.2</span> <span class="toctext">Formatzeichenfolgen</span>](#Formatzeichenfolgen)
    - [<span class="tocnumber">1.2.1</span> <span class="toctext">Namen formatieren</span>](#Namen_formatieren)
    - [<span class="tocnumber">1.2.2</span> <span class="toctext">Daten formatieren</span>](#Daten_formatieren)
    - [<span class="tocnumber">1.2.3</span> <span class="toctext">Orte formatieren</span>](#Orte_formatieren)
    - [<span class="tocnumber">1.2.4</span> <span class="toctext">Regeln für Formatzeichenfolgen</span>](#Regeln_f.C3.BCr_Formatzeichenfolgen)
  - [<span class="tocnumber">1.3</span> <span class="toctext">Steuervariablen</span>](#Steuervariablen)
  - [<span class="tocnumber">1.4</span> <span class="toctext">Gruppieren</span>](#Gruppieren)
    - [<span class="tocnumber">1.4.1</span> <span class="toctext">Regeln für Gruppen</span>](#Regeln_f.C3.BCr_Gruppen)
    - [<span class="tocnumber">1.4.2</span> <span class="toctext">Beispiele:</span>](#Beispiele:)
  - [<span class="tocnumber">1.5</span> <span class="toctext">Attribute</span>](#Attribute)
  - [<span class="tocnumber">1.6</span> <span class="toctext">Ereignisse</span>](#Ereignisse)
    - [<span class="tocnumber">1.6.1</span> <span class="toctext">Ereignisformatzeichenfolgen</span>](#Ereignisformatzeichenfolgen)
    - [<span class="tocnumber">1.6.2</span> <span class="toctext">Anmerkungen zu Attributen und Ereignissen:</span>](#Anmerkungen_zu_Attributen_und_Ereignissen:)
  - [<span class="tocnumber">1.7</span> <span class="toctext">Trennzeichen</span>](#Trennzeichen)

## <span id="Werte_ersetzen" class="mw-headline">Werte ersetzen</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Viele der [grafischen Berichte](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte_-_Teil_4#Grafische_Berichte) erlauben dir die Informationen, die im Bericht angezeigt werden, anzupassen. Variablenersetzung ist die Methode, die verwendet wird, um ein bestimmtes Symbol (Schlüssel) für bestimmte Informationen über die Person aus der Datenbank zu ersetzen.

Zum Beispiel

<table class="wikitable sortable">
<tbody>
<tr>
<th colspan="2">Substitution Keys</th>
<th colspan="2">Wird gezeigt als: (die Person lebt)</th>
</tr>
&#10;<tr>
<th>Zeile 1</th>
<td><code>$n</code></td>
<td>Zeile 1</td>
<td>Smith, Edwin Michael</td>
</tr>
<tr>
<th>Zeile 2</th>
<td><code>* $b{ in $B}</code></td>
<td>Zeile 2</td>
<td>* 1961-05-24 in San Jose, Santa Clara Co., CA</td>
</tr>
<tr>
<th>Zeile 3</th>
<td><code>† $d&lt; in &gt;$D</code></td>
<td>Zeile 3</td>
<td>†</td>
</tr>
</tbody>
</table>

Im nächsten Abschnitt folgt eine Liste aller verfügbaren Variablen (den Platzhaltern).

- Wenn du Namen, Daten oder Orte anders angezeigt haben willst, kannst du [Formatzeichenfolgen](#Formatzeichenfolgen) verwenden um dies zu erreichen.
- Es gibt auch [Steuervariablen](#Steuervariablen) um spezielle Zeichen z.B. das Dollarzeichen darzustellen.
- Du kannst auch [Gruppieren](#Gruppieren) verwenden um Informationen oder ganze Zeilen optional anzuzeigen. **Zeile 2** oben verwendet Gruppierungen um `' in '` nur anzuzeigen, wenn der Geburtsort bekannt ist.
- Zusammen mit [Ereignissen](#Ereignisse) kannst du nahezu alles ausgeben.
- Zum Schluss [Trennzeichen](#Trennzeichen) um dein Leben zu vervollständigen. Im obigen Beispiel verwendet **Zeile 3** dies, um `' in '` nur anzuzeigen, wenn sowohl das Geburtsdatum als auch der Geburtsort bekannt sind.

### <span id="Die_Platzhalter" class="mw-headline">Die Platzhalter</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

<table class="wikitable sortable">
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<tbody>
<tr>
<th colspan="2"><strong>Persönliche Variablen</strong></th>
<th colspan="2"><strong>Ehevariablen</strong></th>
</tr>
&#10;<tr>
<th>$n</th>
<td>Zeigt den Namen der Person.</td>
<td>$s</td>
<td>Zeigt den Namen des/der Partner(in) der Person.</td>
</tr>
<tr>
<th>$i</th>
<td>Zeigt die Gramps ID der Person.</td>
<td>$j</td>
<td>Zeigt die Gramps ID für die Hochzeit.</td>
</tr>
<tr>
<th>$b</th>
<td>Zeigt das Geburtsdatum der Person.</td>
<td>$m</td>
<td>Zeigt das Hochzeitsdatum der Person und deren Partner(in).</td>
</tr>
<tr>
<th>$B</th>
<td>Zeigt den Geburtsort der Person.</td>
<td>$M</td>
<td>Zeigt den Hochzeitsort der Person und deren Partner(in).</td>
</tr>
<tr>
<th>$d</th>
<td>Zeigt das Todesdatum der Person.</td>
<td>$v</td>
<td>Zeigt das Scheidungsdatum der Person und deren Partner(in).</td>
</tr>
<tr>
<th>$D</th>
<td>Zeigt den Sterbeort der Person.</td>
<td>$V</td>
<td>Zeigt den Scheidungsort der Person und deren Partner(in).</td>
</tr>
<tr>
<th>$a</th>
<td>Zeigt ein Attribut der Person.
<p>Siehe <a href="#Attribute">Attribute</a> für mehr Details</p></td>
<td>$u</td>
<td>Zeigt ein Attribut der Heirat.
<p>Siehe <a href="#Attribute">Attribute</a> für mehr Details</p></td>
</tr>
<tr>
<th>$e</th>
<td>Zeigt Ereignis Informationen der Person.
<p>Siehe <a href="#Ereignisse">Ereignisse</a> für mehr Details</p></td>
<td>$t</td>
<td>Zeigt Ereignisinformationen der Hochzeit.
<p>Siehe <a href="#Ereignisse">Ereignisse</a> für mehr Details</p></td>
</tr>
</tbody>
</table>

Alle Variablen für die Ehe werden von dem bevorzugten Ehepartner der Person in Gramps definiert. Wenn die Person noch nie verheiratet war, zeigen diese Variablen nichts an.

#### <span id="Andere_Platzhalter" class="mw-headline">Andere Platzhalter</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

- `$T` Zeigt heutiges Datum.

#### <span id="Standardanzeigeformate" class="mw-headline">Standardanzeigeformate</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

|  |  |
|----|----|
| Variablen | Anzeigeformat |
| \$n \$s | Namen werden wie im 'Namensformat:' in den Gramps Präferenzen im Anzeigereiter eingestellt angezeigt. |
| \$B \$D \$M \$V | Orte zeigen standardmäßig den Ortstitel. |
| \$b \$d \$m \$v | Daten werden wie im 'Datumsformat:' in den Gramps Präferenzen im Anzeigereiter eingestellt angezeigt. |
| \$e \$t | Ereignisse zeigen standardmäßig die Beschreibung. |

#### <span id="Veraltete_Variablen" class="mw-headline">Veraltete Variablen</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Einige alte Variablen sind veraltet weil sie durch [Formatzeichenfolgen](#Formatzeichenfolgen) ersetzt wurden. Hier ist eine Liste dieser Variablen und wie man ihre Ergebnisse erreicht:

|  |  |  |
|----|----|----|
| Alte Variable | Wie es jetzt angezeigt wird | Was angezeigt wird |
| \$f | \$n | Name - wie bei Gramps in den Präferenzen festgelegt. |
| \$n | \$n(g f) | Name - Vorname Nachname |
| \$N | \$n(f, g) | Name - Nachname, Vorname (beachte das explizite Komma). |
| \$nC | \$n(g F) | Name - Vorname NACHNAME in Großbuchstaben |
| \$NC | \$n(F, g) | Name - NACHNAME in Großbuchstaben, Vorname |
| \$by | \$b(yyyy) | Datum der Geburt, nur das Jahr |
| \$dy | \$d(yyyy) | Todesdatum, nur das Jahr |
| \$my | \$m(yyyy) | Heiratsdatum der bevorzugten Ehe, nur das Jahr |
| \$p | \$s | Name des Partners anzeigen wie in Gramps unter Präferenzen angegeben. |
| \$s | \$s(g f) | Name des bevorzugten Partner- Vorname Nachname |
| \$S | \$s(f, g) | Name des bevorzugten Partner - Nachname, Vorname |
| \$sC | \$s(g F) | Name des bevorzugten Partner - Vorname NACHNAME in Großbuchstaben |
| \$SC | \$s(F, g) | Name des bevorzugten Partner - NACHNAME in Großbuchstaben, Vorname |

### <span id="Formatzeichenfolgen" class="mw-headline">Formatzeichenfolgen</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Formatzeichenfolgen werden verwendet, um Namen und Datumsangaben anders anzuzeigen als die, die in den Gramps-Einstellungen zugewiesen wurden. Hier ist die Syntax für eine Formatzeichenfolge:

\$***<span class="kbd" style="background:#D3D3D3; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">Schlüssel</span>***(Formatzeichenfolge)

       wobei:  Schlüssel eins der folgenden Zeichen ist: 'nsijbmBMdvDVauet'

Eine Formatzeichenfolge ist ein beliebiger Text, Trennzeichen oder Formatschlüssel (Festlegung weiter unten) um Informationen über die Person anzuzeigen.

#### <span id="Namen_formatieren" class="mw-headline">Namen formatieren</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Für Namen `($n $s)` kannst du folgende Formatschlüssel verwenden um den Namen verschieden darzustellen.

|  |  |  |  |
|----|----|----|----|
| t | Titel | f | Vorname |
| x | Gebräuchliche Name. Wenn vorhanden Rufname sonnst erste Vorname. | c | Rufname |
| n | Spitzname | s | Suffix |
| l | Nachname | g | Familienspitzname |

Diese Schlüssel können GROSS geschrieben werden um das Ergebnis in GROSSBUCHSTABEN zu erhalten.

Zum Beispiel:

<table class="wikitable sortable">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<th>Formatschlüssel</th>
<th>Zeigt</th>
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
<strong>Wenn du einen Buchstaben 'c' in deiner Formatzeichenfolge ausgeben willst (oder jeden anderen Formatschlüssel),</strong>
</div>
<hr />
<p>musst du erst ein <code>'\'</code> davor setzen. Siehe <a href="#Steuervariablen">Steuervariablen</a> für mehr Details.</p></td>
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
<strong>Die geschweiften Klammern <code>{ }</code> dienen dazu Informationen zu verstecken.</strong>
</div>
<hr />
<p>Hier wird es um <code>' ($n(c))'</code> verwendet um <code>' ()'</code> nicht anzuzeigen, wenn die Person keinen Rufnamen besitzt. Siehe <a href="#Gruppieren">Gruppieren</a> für mehr Details.</p></td>
</tr>
</tbody>
</table>

#### <span id="Daten_formatieren" class="mw-headline">Daten formatieren</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Für alle Datumsvariablen `($b $d $m $v)` kannst du die folgenden Formatschlüssel verwenden:

<table class="wikitable sortable">
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<tbody>
<tr>
<th>yyyy</th>
<td>Das Jahr als vierstellige Zahl</td>
<td>yyy</td>
<td>Das Jahr mit mindestens drei Stellen</td>
</tr>
<tr>
<th>yy</th>
<td>Das Jahr von 00 bis 99</td>
<td>y</td>
<td>Das Jahr von 0 bis 99</td>
</tr>
<tr>
<th>mmmm<br />
&#10;<p><strong>MMMM</strong></p></th>
<td>Der komplette Name des Monats<br />
&#10;<p>Der komplette Name des Monats in GROSSBUCHSTABEN</p></td>
<td>mmm<br />
&#10;<p><strong>MMM</strong></p></td>
<td>Der verkürzte Name des Monats<br />
&#10;<p>Der verkürzte Name des Monats in GROSSBUCHSTABEN</p></td>
</tr>
<tr>
<th>mm</th>
<td>Der Monat von 00 bis 11</td>
<td>m</td>
<td>Der Monat von 0 bis 12</td>
</tr>
<tr>
<th>dd</th>
<td>Der Tag von 00 bis 31</td>
<td>d</td>
<td>Der Tag von 0 bis 31</td>
</tr>
<tr>
<th>o</th>
<td>Der Datumstyp (Bestimmung)</td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

Zum Beispiel:

<table class="wikitable sortable">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<th>Formatschlüsselchlüssel</th>
<th>zeigt</th>
</tr>
&#10;<tr>
<td><pre><code>$b(mmm-dd yy)
$m(yyyy/mmm/d)
$b(mmm-dd yy)</code></pre></td>
<td><pre><code>May-24 61
1995/May/27
Jun-04 85</code></pre></td>
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
<strong>Für Datumstypen (Bestimmung)</strong>
</div>
<hr />
<p>Nur "vor", "nach" und "um" wird zur Zeit unterstützt. alles andere zeigt nichts an.<br />
Und für Zeitspannen und Zeiträume wird nur das Startdatum (erste) angezeigt.</p></td>
</tr>
</tbody>
</table>

#### <span id="Orte_formatieren" class="mw-headline">Orte formatieren</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Für alle Ortsvariablen `($B $D $M $V)`) kannst du die folgenden Formatschlüssel verwenden:

|     |            |     |              |
|-----|------------|-----|--------------|
| e   | Straße     | l   | Lokalität    |
| c   | Ort        | u   | Landkreis    |
| s   | Bundesland | p   | Postleitzahl |
| n   | Land       | t   | Titel        |
| x   | Längengrad | y   | Breitengrad  |

Diese Schlüssel können GROSS geschrieben werden um das Ergebnis in GROSSBUCHSTABEN zu erhalten.

Zum Beispiel:

<table class="wikitable sortable">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<th>Formatschlüssel</th>
<th>zeigt</th>
</tr>
&#10;<tr>
<td><pre><code>$B
$B(c, s, N)</code></pre></td>
<td><pre><code>St Judes Hospital
Carmel, IN, USA</code></pre></td>
</tr>
</tbody>
</table>

#### <span id="Regeln_für_Formatzeichenfolgen"></span><span id="Regeln_f.C3.BCr_Formatzeichenfolgen" class="mw-headline">Regeln für Formatzeichenfolgen</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

- Alles innerhalb einer Formatzeichenfolge wird ausgegeben.
- Du musst [Steuervariablen](#Steuervariablen) verwenden um Sachen wie `')'` und Formatschlüssel anzuzeigen.
- Trennzeichen können sich innerhalb von Formatzeichenfolgen befinden.
- Mindestens EIN Formatschlüssel muss etwas anzeigen damit die gesamte Formatzeichenfolge dargestellt wird.

Zum Beispiel:

<table class="wikitable sortable">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<th>Formatschlüssel</th>
<th>zeigt</th>
</tr>
&#10;<tr>
<td><pre><code>$n(f l)
b. $b {at $B}
{d. $d $D}</code></pre></td>
<td><pre><code>Edwin Michael Smith
b. 1961-05-24 at San Jose, Santa Clara Co., CA</code></pre>
<strong><kbd style="background:#D3D3D3; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">Die Person lebt (oder es waren keine Informationen verfügbar) also wurde die Zeile entfernt.</kbd></strong></td>
</tr>
</tbody>
</table>

### <span id="Steuervariablen" class="mw-headline">Steuervariablen</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Steuervariablen ermöglichen dir Zeichen auszugeben, die in der Ausgabe eine Ersetzungsfunktion haben.

Zum Beispiel wird das Dollarzeichen '\$' verwendet, um den Beginn einer Variable zu markieren. Wenn du ein Dollarzeichen ausgeben willst würdest du ein Steuerzeichen wie '\\' verwenden.

|  |  |  |  |  |
|----|----|----|----|----|
| Steuervariablen | Ergebnis |  |  |  |
| \\ | Zeigt ein einzelnes `'$'` |  | \\ | Zeigt einen einzelnen `'\'` |
| \\ | Zeigt eine einzelne `'('` |  |  |  |
| \\ | Zeigt eine einzelne `'{'` |  |  |  |
| \\ | Zeigt eine einzelne `'{'` |  |  |  |
| \\ | Zeigt eine einzelne `'}'` |  |  |  |
| \\ | Zeigt eine einzelnes `'<'` |  |  |  |
| \\ | Zeigt eine einzelnes `'>'` |  |  |  |

Grundsätzlich wird alles was direkt nach einem `'\'` folgt ausgegeben.

<table style="width:80%;margin-top:+.7em;margin-bottom:+.7em;background-color: #ddffcc85;border:1px solid #ccc; padding: 5px" data-align="center">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 60px">![[_media/Gramps-notes.png]]</td>
<td><div style="font-size:110%">
<strong>Wenn du dich in einer Formatzeichenfolge befindest,</strong>
</div>
<hr />
<p>kann es sein, das du den '\' benötigst, um ein Zeichen auszugeben, welches normalerweise ein Formatschlüssel ist.</p></td>
</tr>
</tbody>
</table>

Zum Beispiel:

<table class="wikitable sortable">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<th>Formatschlüssel:</th>
<th>zeigt</th>
</tr>
&#10;<tr>
<td><pre><code>$b(m hi mom)
$b(m hi \mo\m)</code></pre></td>
<td><pre><code>5 hi 5o5
5 hi mom</code></pre>
<strong><kbd style="background:#D3D3D3; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">Da diese Person im fünften Monat geboren wurde.</kbd></strong></td>
</tr>
</tbody>
</table>

### <span id="Gruppieren" class="mw-headline">Gruppieren</span>

Es gibt Umstände, in denen du nicht willst, das bestimmter Text angezeigt wird.

Nimm das Beispiel:

|  |  |  |
|----|----|----|
| Schlüssel | Nur Datum ist bekannt | Nur Ort ist bekannt |
| `starb{ am $d}{ in $D}` | `starb am 1975-06-26 in ` | `starb am in Reno, Washoe Co., NV` |

Keines dieser Anzeigeergebnisse ist sehr akzeptabel.

Aber mit Gruppen (gekennzeichnet durch **{}**) kannst du Informationen optional ausgeben, wenn die Variable innerhalb Daten enthält.

|  |  |  |
|----|----|----|
| Schlüssel | Nur Datum ist bekannt | Nur Ort ist bekannt |
| `starb {am $d }{in $D}` | `starb am 1975-06-26` | `starb in Reno, Washoe Co., NV` |

Was ein akzeptableres Ergebnis ist als im ersten Beispiel

#### <span id="Regeln_für_Gruppen"></span><span id="Regeln_f.C3.BCr_Gruppen" class="mw-headline">Regeln für Gruppen</span>

Eine Gruppe wird nur angezeigt, wenn sie mindestens eine Variable enthält, die etwas anzeigt. Wenn eine Gruppe nur Text und/oder Variablen mit unbekannten Informationen enthält, wird die komplette Gruppe nicht ausgegeben.

Gruppen können auch verschachtelt werden. Wenn dies passiert (wie unten), wird die äußere Gruppe nur angezeigt, wenn es mindestens eine Variable, die etwas anzeigt, in der äußeren oder einer der Untergruppen vorhanden ist.

Gruppen können auch verwendet werden, um Text zu entfernen. Wenn du eine Zeile nicht anzeigen willst, ein `'-'` am Beginn einer Zeile entfernt die gesamte Zeile von der Ausgabe, wenn die obere Regel wahr ist.

Wenn du nicht den Anzeigeschlüssel von oben (für Todesinformationen) angezeigt haben möchtest (die Person lebt oder du kennst die Informationen noch nicht), ändere den Schlüssel, das er wie folgt aussieht `{starb {am $d }{in $D}`

#### <span id="Beispiele:" class="mw-headline">Beispiele:</span>

Dies versteckt `'('` und `')'` wenn die Scheidungsinformationen nicht bekannt sind (oder noch verheiratet).

- `m. $m $M {- ($v(yyyy))`

Zeig nur ein paar Partnerinformationen wenn verheiratet oder entferne die komplette Zeile wenn nie verheiratet:

- `{$s $m(yyyy) {- $v(\(yyyy\))}}`

### <span id="Attribute" class="mw-headline">Attribute</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Attribute haben keine Formatzeichenkette. Stattdessen wird der Name des Attribut in `[]` gesetzt. Hier die Syntax für ein Attribut:

\$***<span class="kbd" style="background:#D3D3D3; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">Schlüssel</span>***\[Attributname\]  
wobei: ***<span class="kbd" style="background:#D3D3D3; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">Schlüssel</span>*** eines der folgenden Zeichen ist: 'au'

Zum Beispiel:

<table class="wikitable sortable">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<th>Formatschlüssel</th>
<th>zeigt</th>
</tr>
&#10;<tr>
<td><pre><code>$a[Beruf]
$a[Sozialversicherungsnummer]
$a[Gesamt \$ hinterlassen]</code></pre></td>
<td><pre><code>Programmierer
7A3-29-F1C6
3.00USD</code></pre></td>
</tr>
</tbody>
</table>

### <span id="Ereignisse" class="mw-headline">Ereignisse</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Ereignisse haben die selbe Struktur am Start wie Attribute `$e` oder `$t` und der Ereignisname in `[]` aber Ereignisse haben eine extra Formatzeichenkette nach dem Namen um die Beschreibung, Datum, Ort, ID und Attribute die mit ihnen verbunden sind anzuzeigen. Jedes dieser beiden kann mit einem 'n', 'd', 'D', 'i', und 'a' in der Formatzeichenkette dargestellt werden. Hier ist die Syntax für ein Ereignis:

\$***<span class="kbd" style="background:#D3D3D3; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">Schlüssel</span>***\[Attributname\](Formatzeichenfolge)  
wobei: ***<span class="kbd" style="background:#D3D3D3; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">Schlüssel</span>*** eines der folgenden Zeichen ist: 'et'

#### <span id="Ereignisformatzeichenfolgen" class="mw-headline">Ereignisformatzeichenfolgen</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Die Ereignisformatzeichenfolge wird verwendet, um Informationen über das Ereignis anzuzeigen. Hier die Formatschlüsse zum am Teile des Ereignis anzuzeigen:

|  |  |  |  |  |
|----|----|----|----|----|
| Formatschlüssel | zeigt |  | Formatschlüssel | zeigt |
| n | Beschreibung |  | i | Ereignis ID |
| d | Ereignis Datum\* |  | D | Ereignis Ort\* |
| a | Ein Attribut für ein Ereignis\*\* |  |  |  |

\*Diese Variablen können selbst Formatzeichenfolgen enthalten. Datum und Ort können wie in [Formatzeichenfolgen](#Formatzeichenfolgen) beschrieben formatiert werden.

\*\*Attribute benötigen den Attributnamen in \[\] und sind wie oben formatiert.

Zum Beispiel:

<table class="wikitable sortable">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<th>Formatschlüssel</th>
<th>zeigt</th>
</tr>
&#10;<tr>
<td><pre><code>$e[First Communion](d(yyyy-mm-d))
$e[Bar Mitzvah](n&lt; in &gt; D)
$e[Geburt](d(yyyy mm/dd) D)</code></pre></td>
<td><pre><code>2009-11-6
Jerry&#39;s Bar Mitzah in Opas house
2007 05/23 Grandmothers house</code></pre></td>
</tr>
</tbody>
</table>

Und:

<table class="wikitable sortable">
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<tbody>
<tr>
<th>Formatschlüssel</th>
<th></th>
<th>zeigt</th>
</tr>
&#10;<tr>
<td><pre><code>$b(yyyy-Mmm-dd)
$M</code></pre></td>
<td>ist das gleiche wie</td>
<td><pre><code>$e[Geburt](d(yyyy-Mmm-dd))
$t[Hochzeit](D)</code></pre></td>
</tr>
</tbody>
</table>

#### <span id="Anmerkungen_zu_Attributen_und_Ereignissen:" class="mw-headline">Anmerkungen zu Attributen und Ereignissen:</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Attribut- und Ereignisnamen sind obligatorisch. `'$a'` oder `'$a[]'` zeigen gar nichts.

Attribut- und Ereignisnamen können Sonderzeichen enthalten. Vor allem `']'` und `')'`'. Wenn dies der Fall ist, musst du [Steuervariablen](#Steuervariablen) verwenden.

### <span id="Trennzeichen" class="mw-headline">Trennzeichen</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Trennzeichen sind spezielle 'nur Text' Gruppen innerhalb von `'<'` und `'>'` die bedingte Trennzeichen (wie `', '` oder `' - '`) zwischen zwei Gruppen, Variablen, Formatschlüsseln oder Text anzuzeigen.

Trennzeichen werden bedingt abhängig von diesen Regeln angezeigt:

- Eine Variable die **nichts** anzeigt, entfernt nur sich selbst und ein Trennzeichen links von ihr aus der Anzeigezeile.
- Wenn sich kein Trennzeichen links von ihr befindet, entfernt die selbe Variable sich selbst und ein Trennzeichen rechts von sich aus der angezeigten Zeile.
- Wenn es zwei Trennzeichen zusammen gibt, wird das linke entfernt und das rechte in der Anzeigezeile beibehalten.
- Trennzeichen am Beginn oder Ende der Anzeigezeile (oder Formatzeichenkette) werden entfernt.

Nim das Beispiel für Formatschlüssel

- `$s(f|s)<, >$m(yyyy)< @ >$M< - >$v(\(yyyy\))`

  
Hier einige Dinge, die passieren können:

<table class="wikitable sortable">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<th>Möglichkeit</th>
<th>Ergebnis</th>
</tr>
&#10;<tr>
<td>Wenn <strong>keine</strong> der Variablen bekannt ist</td>
<td>Keines der Trennzeichen wird angezeigt.</td>
</tr>
<tr>
<td>Wenn nur eine Variable bekannt <strong>ist</strong></td>
<td>Nur die Variable wird ausgegeben. Es werden keine Trennzeichen ausgegeben.</td>
</tr>
<tr>
<td>Wenn nur der Partnername <strong>nicht bekannt</strong> ist</td>
<td>Das Erste Trennzeichen wird nicht angezeigt</td>
</tr>
<tr>
<td>Wenn nur das Hochzeitsdatum <strong>nicht bekannt</strong> ist</td>
<td>Das erste Trennzeichen wird nicht angezeigt. Es bleibt übrig::
<p>Lischen Müller&lt; - &gt;{ … }Und nur das Scheidungsdatum wird benötigt, um das zweite Trennzeichen auszugeben.</p></td>
</tr>
<tr>
<td>Wenn nur das Scheidungsdatum <strong>nicht bekannt</strong> ist</td>
<td>Das zweite Trennzeichen wird nicht angezeigt</td>
</tr>
</tbody>
</table>

  
Trennzeichen können sich innerhalb von Formatierungszeichenketten befinden:

- `$n(<0>T< >L<, >f< >s)`

Anders als Gruppen können Trennzeichen nicht über/aus Formatzeichenketten gehen. Also wird das Trennzeichen `<0>` NIE angezeigt. Egal was sich links oder in der Variable befindet.

Hier ein nützliches Beispiel:

- `{({b. $b}<, >{d. $d})}`

Dies wird:

<table class="wikitable sortable">
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td>Gibt nur die Sachen außerhalb von () aus, wenn entweder das Geburts- oder Todesdatum angezeigt wird</td>
</tr>
<tr>
<td>Zeigt die innere Trennung nur, wenn beide Daten bekannt sind.</td>
</tr>
<tr>
<td>Also hier einige Sachen, die angezeigt werden können
<table>
<tbody>
<tr>
<td><code>(* 8.6.0970)</code></td>
<td><code>(† 9.3.2012)</code></td>
<td><code>(* 8.6.0970, † 9.3.2012)</code></td>
<td>oder die Zeile wird nicht ausgegeben.</td>
</tr>
</tbody>
</table></td>
</tr>
<tr>
<td>Wir sehen nicht Sachen wie diese:
<table>
<tbody>
<tr>
<td><code>()</code></td>
<td><code>(, )</code></td>
<td><code>(*)</code></td>
<td><code>(*, )</code></td>
<td><code>(†)</code></td>
</tr>
<tr>
<td><code>(, †)</code></td>
<td><code>(* 8.6.0970, )</code></td>
<td><code>(* 8.6.0970, †)</code></td>
<td><code>(, † 9.3.2012)</code></td>
<td><code>(*, † 9.3.2012)</code></td>
</tr>
</tbody>
</table></td>
</tr>
</tbody>
</table>

  

------------------------------------------------------------------------

Zurück zur [Übersicht der Berichte](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte).

|  |  |  |
|:---|:--:|---:|
| [**Zurück**](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte_-_Teil_1) | [**Index**](wiki:De:Gramps_6.0_Wiki_Handbuch) | [**Nächste**](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Berichte_-_Teil_3) |

<div class="LanguageLinks">

|  |  |  |
|----|----|----|
| ![[_media/Gramps-config-language.png]] | **[Sprachen](wiki:Portal:Translators):**  | [English](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_2)     • <span lang="da"><a href="/wiki/index.php/Gramps_6.0_Wiki_Manual_-_Reports_-_part_2/da" class="mw-redirect" title="Gramps 6.0 Wiki Manual - Reports - part 2/da">dansk</a></span>  • <span lang="de"><span class="mw-selflink selflink">Deutsch</span></span>  • <span lang="es">[español](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_2/es)</span>  • <span lang="fi"><a href="/wiki/index.php/Gramps_6.0_Wiki_Manual_-_Reports_-_part_2/fi" class="mw-redirect" title="Gramps 6.0 Wiki Manual - Reports - part 2/fi">suomi</a></span>  • <span lang="fr">[français](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_2/fr)</span>  • <span lang="he">[עברית](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_2/he)</span>      • <span lang="mk">[македонски](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_2/mk)</span>   • <span lang="nl"><a href="/wiki/index.php/Gramps_6.0_Wiki_Manual_-_Reports_-_part_2/nl" class="mw-redirect" title="Gramps 6.0 Wiki Manual - Reports - part 2/nl">Nederlands</a></span>      • <span lang="ru">[русский](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_2/ru)</span>   • <span lang="sq"><a href="/wiki/index.php/Gramps_6.0_Wiki_Manual_-_Reports_-_part_2/sq" class="mw-redirect" title="Gramps 6.0 Wiki Manual - Reports - part 2/sq">shqip</a></span>   • <span lang="sk">[slovenčina](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_2/sk)</span> |

</div>

<table style="width:90%;margin-top:+.7em;margin-bottom:+.7em;background-color: #c0f0ff;border:1px solid #ccc; padding: 5px" data-align="center">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td>![[_media/Gnome-important.png]]</td>
<td style="text-align: left;"><strong>Spezielle Copyright Notiz:</strong> Alle Änderungen auf dieser Seite müssen unter zwei copyright Lizenzen stehen:
<ul>
<li>GNU Free Documentation License 1.2 - siehe <a href="/wiki/index.php/Gramps:Copyrights" title="Gramps:Copyrights">Wiki Copyright</a> (englisch)</li>
<li>GPL - siehe <a href="/wiki/index.php/Gramps:Manualcopyright" title="Gramps:Manualcopyright">Handbuch Copyright</a> (englisch)</li>
</ul>
<p>Diese Lizenzen ermöglichen es dem Gramps-Projekt die bestmögliche Verwendung dieses Handbuchs als freien Inhalt in zukünftigen Gramps Versionen. Wenn du mit dieser dual Lizenzierung nicht einverstanden bist, bearbeite diese Seite nicht. Du darfst zu anderen Seiten des Wiki die nur unter die GFDL Lizenz fallen nur über externe Links (verwende die Syntax: [http://www.gramps-project.org/...]), nicht über interne Links verlinken.<br />
Außerdem verwende nur die Bekannten <a href="/wiki/index.php/De:Gramps_6.0_Wiki_Handbuch_-_Einleitung#Drucktechnische_Konventionen" title="De:Gramps 6.0 Wiki Handbuch - Einleitung">Drucktechnische Konventionen</a></p></td>
</tr>
</tbody>
</table>
