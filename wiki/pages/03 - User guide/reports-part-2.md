---
title: Gramps 6.0 Wiki Manual - Reports - part 2
categories:
- Documentation
- Plugins
managed: false
source: wiki-scrape
wiki_revid: 117450
wiki_fetched_at: '2026-05-30T11:37:38Z'
---

{{#vardefine:chapter\|13.2}} {{#vardefine:figure\|0}} Back to [Index of Reports](wiki:Gramps_6.0_Wiki_Manual_-_Reports).

<hr>

This section describes the substitution values that can be used in the different reports available in Gramps.

## Substitution Values

Many of the [graphical reports](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_4#Graphical_Reports) allow you to customize the information that is displayed on the reports. Variable substitution is the method that is used to substitute a particular symbol (key) for specific information about the person in the database.

For example:

<table>
<thead>
<tr>
<th colspan="2"><p>Substitution Keys</p></th>
<th colspan="2"><p>Will show as: (the person is alive)</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p>Line 1</p></td>
<td><p><code>$n</code></p></td>
<td><p>Line 1</p></td>
<td><p>Smith, Edwin Michael</p></td>
</tr>
<tr>
<td><p>Line 2</p></td>
<td><p><code>b. $b{ at $B}</code></p></td>
<td><p>Line 2</p></td>
<td><p>b. 1961-05-24 at San Jose, Santa Clara Co., CA</p></td>
</tr>
<tr>
<td><p>Line 3</p></td>
<td><p><code>d. $d&lt; at &gt;$D</code></p></td>
<td><p>Line 3</p></td>
<td><p>d.</p></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

In the next section a list of all available variables (The Substitution Keys) follows.

- If you wish to display names, date, or place information differently, you may use [Format Strings](#Format_Strings) to accomplish this.
- There are also [Control Variables](#Control_Variables) to display special characters (like the dollar sign).
- You can also use [Grouping](#Grouping) to optionally display information. In the example above **Line 2**, uses grouping to display `' at '` only when the birth place is known.
- Along with [Events](#Events) you can print almost anything.
- Finally, [Separators](#Separators), to make your life complete. In the example above **Line 3**, uses this to display `' at '` only when both the birth date and place is known.

### The Substitution Keys

<table>
<thead>
<tr>
<th colspan="2"><p>Personal variables</p></th>
<th colspan="2"><p>Marital variables</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p>$n</p></td>
<td><p>Displays the person's name</p></td>
<td><p>$s</p></td>
<td><p>Displays the name of the person's spouse</p></td>
</tr>
<tr>
<td><p>$i</p></td>
<td><p>Displays the Gramps ID for the person.</p></td>
<td><p>$j</p></td>
<td><p>Displays the Gramps ID for the marriage.</p></td>
</tr>
<tr>
<td><p>$b</p></td>
<td><p>Displays the person's date of birth</p></td>
<td><p>$m</p></td>
<td><p>Displays the marriage date of the person and the spouse.</p></td>
</tr>
<tr>
<td><p>$B</p></td>
<td><p>Displays the person's place of birth</p></td>
<td><p>$M</p></td>
<td><p>Displays the place of the marriage of the person and the spouse.</p></td>
</tr>
<tr>
<td><p>$d</p></td>
<td><p>Displays the person's date of death</p></td>
<td><p>$v</p></td>
<td><p>Displays the divorce date of the person and the spouse.</p></td>
</tr>
<tr>
<td><p>$D</p></td>
<td><p>Displays the person's place of death</p></td>
<td><p>$V</p></td>
<td><p>Displays the place of the divorce of the person and the spouse.</p></td>
</tr>
<tr>
<td><p>$a</p></td>
<td><p>Displays an attribute about the person. see [Attributes](#Attributes) for more</p></td>
<td><p>$u</p></td>
<td><p>Displays an attribute about the marriage. see [Attributes](#Attributes) for more</p></td>
</tr>
<tr>
<td><p>$e</p></td>
<td><p>Displays event information about the person. See [Events](#Events) for more</p></td>
<td><p>$t</p></td>
<td><p>Displays an event information about the marriage. See [Events](#Events) for more</p></td>
</tr>
</tbody>
</table>

All of the Marital variables are defined by the person's preferred spouse in Gramps. If the person has never been married, then these variables will not display anything.

#### Other Substitution Keys

- `$T` Displays Todays date.

#### Default displayed formats

| Variables | Display format |
|----|----|
| \$n \$s | Names will be displayed as set in 'Name format:' on the Display tab in Gramps preferences |
| \$B \$D \$M \$V | Places will display the Place title by default |
| \$b \$d \$m \$v \$T | Dates will be displayed as set in 'Date format:' on the Display tab in Gramps preferences |
| \$e \$t | Events will display the description by default |

#### Deprecated variables

Some of the old variables were deprecated because [Format Strings](#Format_Strings) have replaced them. So here is a list of those variables and how to achieve their results:

| Old Variable | How to display it now | What is displayed |
|----|----|----|
| \$f | \$n | Name - as by Gramps name display under Preferences |
| \$n | \$n(g f) | Name - FirstName LastName |
| \$N | \$n(f, g) | Name - LastName, FirstName (note the explicit comma) |
| \$nC | \$n(g F) | Name - FirstName LastName in UPPER case |
| \$NC | \$n(F, g) | Name - LastName in UPPER case, FirstName |
| \$by | \$b(yyyy) | Date of birth, year only |
| \$dy | \$d(yyyy) | Date of death, year only |
| \$my | \$m(yyyy) | Date of preferred marriage, year only |
| \$p | \$s | Preferred spouse's name as by Gramps name display under Preferences |
| \$s | \$s(g f) | Preferred spouse's name - FirstName LastName |
| \$S | \$s(f, g) | Preferred spouse's name - LastName, FirstName |
| \$sC | \$s(g F) | Preferred spouse's name - FirstName LastName in UPPER case |
| \$SC | \$s(F, g) | Preferred spouse's name - LastName in UPPER case, FirstName |

### Format Strings

Format strings are used to display names and dates differently than those assigned under Gramps Preferences. Here is the syntax for a format string:

\$**(format string)  
where: ** is one of the following characters: '`nsijbmBMdvDVauet`'

A format string is any text, separators or format codes (defined below) to display information about the person.

#### Formatting names

For names `($n $s)` you may use the following formatting codes to display the name differently.

| t | Title | f | Given name |
|----|----|----|----|
| x | Common name. Call name if existing, otherwise first first name | c | Call name |
| n | Nick name | s | Suffix |
| l | Surname | g | Family nickname |

These codes can be upper-cased to uppercase the result.

For example:

<table>
<thead>
<tr>
<th><p>Formatting code</p></th>
<th><p>Displays</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><pre><code>$n(L, f) ($n(c)), $n(L, f){ ($n(c))}
$s(f l s)</code></pre></td>
<td><pre><code>SMITH, Edwin Michael (), SMITH, Edwin Michael
Janice Ann Adams</code></pre></td>
</tr>
</tbody>
</table>

#### Formatting Dates

For all of the date variables `($b $d $m $v)` you may use the following formatting codes:

<table>
<thead>
<tr>
<th><p>yyyy</p></th>
<th><p>The year as a four digit number</p></th>
<th><p>yyy</p></th>
<th><p>The year, with a minimum of three digits</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p>yy</p></td>
<td><p>The year, from 00 to 99</p></td>
<td><p>y</p></td>
<td><p>The year, from 0 to 99</p></td>
</tr>
<tr>
<td><p>mmmm<br />
<strong>MMMM</strong></p></td>
<td><p>The full name of the month<br />
The full name IN CAPS</p></td>
<td><p>mmm<br />
<strong>MMM</strong></p></td>
<td><p>The abbreviated name of the month<br />
The abbreviated name IN CAPS</p></td>
</tr>
<tr>
<td><p>mm</p></td>
<td><p>The month, from 00 to 12</p></td>
<td><p>m</p></td>
<td><p>The month, from 0 to 12</p></td>
</tr>
<tr>
<td><p>dd</p></td>
<td><p>The day, from 00 to 31</p></td>
<td><p>d</p></td>
<td><p>The day, from 0 to 31</p></td>
</tr>
<tr>
<td><p>o</p></td>
<td><p>The date type (modifier)</p></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

For example:

<table>
<thead>
<tr>
<th><p>Formatting code</p></th>
<th><p>displays</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><pre><code>$b(mmm-dd yy)
$m(yyyy/mmm/d)
$b(mmm-dd yy)</code></pre></td>
<td><pre><code>May-24 61
1995/May/27
Jun-04 85</code></pre></td>
</tr>
</tbody>
</table>

#### Formatting Places

For all of the place variables `($B $D $M $V)` you may use the following formatting codes:

| e   | Street    | l   | Locality    |
|-----|-----------|-----|-------------|
| c   | City      | u   | County      |
| s   | State     | p   | Postal Code |
| n   | Country   | t   | Title       |
| x   | Longitude | y   | Latitude    |

These codes can be upper-cased to uppercase the result.

For example:

<table>
<thead>
<tr>
<th><p>Formatting code</p></th>
<th><p>displays</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><pre><code>$B
$B(c, s, N)</code></pre></td>
<td><pre><code>St Judes Hospital
Carmel, IN, USA</code></pre></td>
</tr>
</tbody>
</table>

#### Rules for format strings

- Anything will print inside a format string
- You need to use [Control Variables](#Control_Variables) to display things like `')'` and format codes
- Separators can be within format strings.
- At least ONE format code has to display something for the ENTIRE format string to display

For examples:

<table>
<thead>
<tr>
<th><p>Formatting code</p></th>
<th><p>displays</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><pre><code>$n(f l)
b. $b {at $B
{d. $d $D</code></pre></td>
<td><pre><code>Edwin Michael Smith
b. 1961-05-24 at San Jose, Santa Clara Co., CA</code></pre></td>
</tr>
</tbody>
</table>

### Control Variables

Control variables allow you to print characters that are special to Substitution values within a display.

For example the dollar character '\$' is used to note the start of a variable. If you wish to print a dollar character you would use a control character like '\\'

| Control Variables | Result                  |
|-------------------|-------------------------|
| \\                | Displays a single `'$'` |
| \\                | Displays a single `'\'` |
| \\                | Displays a single `'('` |
| \\                | Displays a single `')'` |
| \\                | Displays a single `'{'` |
| \\                | Displays a single `'}'` |
| \\                | Displays a single `'<'` |
| \\                | Displays a single `'>'` |

Basically anything that comes after a `'\'` will be printed.

For example:

<table>
<thead>
<tr>
<th><p>Formatting code:</p></th>
<th><p>displays</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><pre><code>$b(m hi mom)
$b(m hi \mo\m)</code></pre></td>
<td><pre><code>5 hi 5o5
5 hi mom</code></pre></td>
</tr>
</tbody>
</table>

### Grouping

There are instances where you do not want certain text to be displayed.

Take the example:

| Formatting Code | Only date is known | Only place is known |
|----|----|----|
| `died on $d at $D` | `died on 1975-06-26 at` | <code>died on at Reno, Washoe Co., NV<code> |
|  |  |  |

Neither of these displayed results are very acceptable.

But with groups (denoted by **{}**), you can optionally print information if a variable within contains information.

| Formatting Code        | Only date is known   | Only place is known            |
|------------------------|----------------------|--------------------------------|
| `died{ on $d}{ at $D}` | `died on 1975-06-26` | `died at Reno, Washoe Co., NV` |

Which is a more preferable displayed result than in the first example.

#### Rules for groups

A group will only display if there is at least one variable that displays something. So if a group only has text and/or variables where the information is not known, the entire group will not print.

Groups can also be nested. If this happens (like below), the outer group will only display if there is at least one variable that displays something within the outer group or any of the sub groups.

Groups can also be used to remove text. If you wish to not display the entire line, `'-'` at the start of a line will remove the entire line from the display if the above rule is true.

If you do not wish to have the display code above (for death information) displayed (the person is alive, or you do not yet know the information), modify the code to look like:

- `-{died{ on $d}{ at $D}`

#### Examples

This will hide `'('` and `')'` if the divorce information is not known (or still married).

- `m. $m $M {- ($v(yyyy))`

Only display some spouse information if married or remove the entire line if never married:

- `{$s $m(yyyy) {- $v(`$`yyyy`$`)}}`

### Attributes

Attributes do not have a format string. Instead the attribute name is placed inside `[]`. Here is the syntax for an attribute:

\$**\[attribute name\]  
where: ** is one of the following characters: 'au'

For example:

<table>
<thead>
<tr>
<th><p>Formatting code</p></th>
<th><p>displays</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><pre><code>$a[Profession]
$a[Social Security Number]
$a[Total \$ bequeathed]</code></pre></td>
<td><pre><code>Programmer
7A3-29-F1C6
3.00USD</code></pre></td>
</tr>
</tbody>
</table>

### Events

Events have the same starting structure as attributes, `$e` or `$t` and the event name in `[]` but events have an extra format string after the name to display the description, date, place, id, and attributes associated with it. Each of these items can be displayed with a , a 'n', 'd', 'D', 'i', and 'a' respectively in the format string. Here is the syntax for an event:

\$**\[attribute name\](format string)  
where: ** is one of the following characters: 'et'

#### Event format strings

The Event format string is used to display information about the event. Here are the format codes to display parts of the event:

| Formatting code | displays |  | Formatting code | displays |
|----|----|----|----|----|
| n | Description |  | i | Event ID |
| d | Event Date\* |  | D | Event Place\* |
| a | An attributes for the event\*\* |  |  |  |

\*These variables can themselves have format strings. Date and a place can be formatted with format string as defined in [Format strings](#Format_strings).

\*\*Attribute needs to have the attribute name in \[\] and are formatted as above.

For example:

<table>
<thead>
<tr>
<th><p>Formatting code</p></th>
<th><p>displays</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><pre><code>$e[First Communion](d(yyyy-mm-d))
$e[Bar Mitzvah](n&amp;lt; at &amp;gt; D)
$e[Birth](d(yyyy mm/dd) D)</code></pre></td>
<td><pre><code>2009-11-6
Jerry&#39;s Bar Mitzah at Opas house
2007 05/23 Grandmothers house</code></pre></td>
</tr>
</tbody>
</table>

And:

<table>
<thead>
<tr>
<th><p>Formatting code</p></th>
<th></th>
<th><p>displays</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><pre><code>$b(yyyy-Mmm-dd)
$M</code></pre></td>
<td><p>is the same as</p></td>
<td><pre><code>$e[Birth](d(yyyy-Mmm-dd))
$t[Marriage](D)</code></pre></td>
</tr>
</tbody>
</table>

#### Notes for attributes and events

Attribute and event names are mandatory. `'$a'` or `'$a[]'` will not display anything.

Attributes and event names may have special characters within them. Most notably `']'` and `')'`. If this is the case, you will need to use [Control Variables](#Control_Variables)

### Separators

Separators are special 'text only' groups inside `'<'` and `'>'` that conditionally display a separator (like `', '` or `' - '`) between two groups, variables, format codes or text.

Separators are displayed conditionally depending on these rules:

- A variable that does **not** display anything will remove itself and a separator that is to the left of it from the display line only.
- If there is not a separator to the left, the same variable will remove itself and a separator that is to the right of it from the displayed line.
- If there are two separators together, the left one will be removed from the display line and the right is kept.
- Separators at the start or end of the display line (or format strings) are removed.

Take this example formatting code:

- `$s(f l s)<, >$m(yyyy)< @ >$M< - >$v(\(yyyy\))`

Here are some things that may happen:

| Possibility | Outcome |
|----|----|
| If **none** of the variables are known | None of the separators will display |
| If only one variable **is** known | Only that variable will print. No separators will print. |
| If only the spouse's name **is not** known | The first separator will not display |
| If only the marriage date **is not** known | The first separator does not display. We will be left with: Jane Doe\< - \>{ … }And only the divorce date needs to be known to print the second separator. |
| If only the divorce date **is not** known | the second separator will not display |

Separators can be inside format strings:

- `$n(<0>T< >L<, >f< >s)`

Unlike groups, separators can not cross over/out of format strings. So the separator `<0>` will NEVER display. No matter what is on the left hand side of the variable.

Here is a useful example:

- `{({b. $b}<, >{d. $d})}`

This will:

<table>
<tbody>
<tr>
<td><p>Only print the outside () if either the birth or death date displays<br />
Only displays the center separator if both dates are known.<br />
So here are some thing that could display</p>
<table>
<tbody>
<tr>
<td><p><code>(b. 1970-4-8)</code></p></td>
<td><p><code>(d. 2012-3-9)</code></p></td>
<td><p><code>(b. 1970-4-8, d. 2012-3-9)</code></p></td>
<td><p>or the line does not print at all.</p></td>
</tr>
</tbody>
</table></td>
</tr>
<tr>
<td><p>We will not see things like:</p>
<table>
<tbody>
<tr>
<td><p><code>()</code></p></td>
<td><p><code>(, )</code></p></td>
<td><p><code>(b.)</code></p></td>
<td><p><code>(b., )</code></p></td>
<td><p><code>(d.)</code></p></td>
</tr>
<tr>
<td><p><code>(, d.)</code></p></td>
<td><p><code>(b. 1970-4-8, )</code></p></td>
<td><p><code>(b. 1970-4-8, d.)</code></p></td>
<td><p><code>(, d. 2012-3-9)</code></p></td>
<td><p><code>(b., d. 2012-3-9)</code></p></td>
</tr>
</tbody>
</table></td>
</tr>
</tbody>
</table>

{{-}}

<hr>

Back to [Index of Reports](wiki:Gramps_6.0_Wiki_Manual_-_Reports).

[Category:Documentation](wiki:Category:Documentation) [Category:Plugins](wiki:Category:Plugins)
