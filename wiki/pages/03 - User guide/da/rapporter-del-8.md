---
title: Da:Gramps 6.0 brugsanvisning - Rapporter - del 8
categories:
- Documentation
- Plugins
- Stub
managed: false
source: wiki-scrape
wiki_revid: 129294
wiki_fetched_at: '2026-05-30T17:34:34Z'
lang: da
---

{{#vardefine:chapter\|13.8}} {{#vardefine:figure\|0}} Tilbage [Indeks over Rapporter](wiki:Da:Gramps_6.0_brugsanvisning_-_Rapporter). {{-}}

<hr>

{{-}}

![[_media/QuickViewReport-EditPerson-context-menu-popup-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Quick View context menu on Edit Person]] This section describes the [Quick Views](wiki:Quick_Views) as part of the different reports available in Gramps.

## Quick Views

![[_media/QuickViewReport-SameSurname-PeopleView-example-popup-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Quick View Report - People view -  - example popup window, showing right-click context menu for result table]]

**Quick View**(s) are report windows available via the [context menu](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window#Pop-up_menus) of the most of the category views and *some* of the edit dialogs.

These **Quick View**(s) are generated reports based on the first selected record and have no options to confuse the process. However, like the main views, the user defined formats selected in the Display tab of the Preferences will carry through in these reports.

**Quick View** reports are static. The contents of these floating windows will not update as the object focus changes nor when the record data is edited. If you want a more dynamic version of the Report, a can be added to the sidebar or bottombar. The report will be regenerated as the object focus shifts. The Configure toolbar tool (or View menu "Configure... option) will have a Quick View tab to select the Object type and report being displayed.

### Clipboarding Quick View data

Use the Quick View table context menu (Right-click) option for to highlight Quick View content that is *not* contained in a formatted table. Then use the context menu again to the selected content to the OS Clipboard.

For Quick Views that have lists of records in tabular format, copy Quick View table row data to the OS Clipboard by using the context menu (Right-click) option within a table row to choose the menu option. If the Quick View has multiple tables, they must be copied individually.

#### Quick View table context menu

- 

- 

{{-}}

### Accessing Quick Views

![[_media/PersonView-PeopleListView-example-with-context-menu-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Quick View context menu on the People Category - Person (List) View]]

The Quick Views can be difficult to locate. The directly accessible interface is via context menus rather than by icons, menu items or being explicitly listed in dialogs. And the indirect access is even more transparent: it is from hotlinks or context menus in gramplets or dialogs.

The following builtin Quick View reports are available via context menus per category:

- *[Dashboard view](wiki:Gramps_6.0_Wiki_Manual_-_Categories#Dashboard_Category)* - **Not available**

  - Note that you can use the

<!-- -->

- *[People view](wiki:Gramps_6.0_Wiki_Manual_-_Categories#People_Category)* and *dialog*

  - [All Events](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_8#All_Events) : Display a person's events, both personal and family
  - [Father lineage](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_8#Father_lineage) : Display father lineage
  - [Mother lineage](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_8#Mother_lineage) : Display mother lineage
  - [Person References](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_8#Person_References) : Display references for an *\<object type\>*
  - [Relation to Home Person](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_8#Relation_to_Home_Person) : All person related to Home Person
  - [Same Given Names](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_8#Same_Given_Names) : Display people with the same given name as a person
  - [Same Surnames](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_8#Same_Surnames) : Display people with the same surname as a person
  - [Siblings](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_8#Siblings) : Display a person's siblings

<!-- -->

- *[Relationships](wiki:Gramps_6.0_Wiki_Manual_-_Categories#Relationships_Category) view* - **Not available**

<!-- -->

- *[Families view](wiki:Gramps_6.0_Wiki_Manual_-_Categories#Families_Category)* and *dialog*

  - [All Family Events](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_8#All_Family_Events) : Display the family and family members events
  - [Family References](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_8#Family_References): Display references for an *\<object type\>*

<!-- -->

- *[Charts view](wiki:Gramps_6.0_Wiki_Manual_-_Categories#Charts_Category)* - **Not available**

<!-- -->

- *[Events view](wiki:Gramps_6.0_Wiki_Manual_-_Categories#Events_Category)*

  - [Event References](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_8#Event_References) : Display references for an *\<object type\>*
  - [On This Day](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_8#On_This_Day) : Display events on a particular day

<!-- -->

- *[Places view](wiki:Gramps_6.0_Wiki_Manual_-_Categories#Places_Category)*

  - [Place References](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_8#Place_References) : Display references for an *\<object type\>*

<!-- -->

- *[Geography view](wiki:Gramps_6.0_Wiki_Manual_-_Categories#Geography_Category)* - **Not available**

<!-- -->

- *[Sources view](wiki:Gramps_6.0_Wiki_Manual_-_Categories#Sources_Category)*

  - [Source References](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_8#Source_References) : Display references for an *\<object type\>*

<!-- -->

- *[Citations view](wiki:Gramps_6.0_Wiki_Manual_-_Categories#Citations_Category)*

  - [Citation References](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_8#Citation_References) : Display references for an *\<object type\>*

<!-- -->

- *[Repositories view](wiki:Gramps_6.0_Wiki_Manual_-_Categories#Repositories_Category)*

  - [Repository References](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_8#Repository_References) : Display references for an *\<object type\>*

<!-- -->

- *[Media view](wiki:Gramps_6.0_Wiki_Manual_-_Categories#Media_Category)*

  - [Media References](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_8#Media_References) : Display references for an *\<object type\>*

<!-- -->

- *[Notes view](wiki:Gramps_6.0_Wiki_Manual_-_Categories#Notes_Category)*

  - [Link References](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_8#Link_References) : Display link references within a note
  - [Note References](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_8#Note_References) : Display references for an *\<object type\>*

The following builtin "Miscellaneous" Quick View reports are available indirectly: via context menus in gramplets and dialogs:

- Age on Date : Display people probably alive and their ages on a particular date of an event
  - Accessed from the [Calendar gramplet](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Calendar). Double-click on a Calendar day opens the [On This Day](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_8#On_This_Day) Quick View
- Attribute match : Display people with an Attribute matching an identifier
  - Accessed from the [Attributes gramplet](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Attributes)
- Filter by \[custom filter\] name :
  - All
  - All people
  - All families
  - All events
  - All places
  - All sources
  - All repositories
  - All media
  - All notes
  - Inverse Person
  - Inverse Family
  - Inverse Event
  - Inverse Place
  - Inverse Source
  - Inverse Repository
  - Inverse Media
  - Inverse Note
  - males
  - females
  - people with other gender
  - people with unknown gender
  - people with missing birth dates
  - people with media
  - media by size
  - incomplete names
  - disconnected people
  - unique surnames
  - list of people
    - Accessed from the [Pedigree gramplet](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Pedigree) and [Age Stats](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Age_Stats) gramplet

{{-}}

### Builtin Quick Views

#### All Events

Example "All Events" quick view report from the People view:

<center>

**Sorted events of Big Louie (Big Louie) Garner von Zieliński Sr**

| Event Type            | Event Date     | Event Place                     |
|-----------------------|----------------|---------------------------------|
| Birth \[E0001656\]    | Jun 21, 1855   | Great Falls, MT, USA            |
| Marriage \[E0002815\] | Apr 1, 1875    | Paragould, Greene, AR, USA      |
| Death \[E0001657\]    | Jun 28, 1911   | Twin Falls, Twin Falls, ID, USA |
| Burial \[E0001658\]   | Jul 1, 1911    | Twin Falls, Twin Falls, ID, USA |

</center>

#### All Family Events

Example "All Family Events" quick view report from the Families view:

<center>

**Sorted events of family  
 Big Louie (Big Louie) Garner von Zieliński Sr - Luella Martel**

| Family Members     | Event Type     | Event Date     | Event Place     |
|----|----|----|----|
| Luella Martel \[I0000045\] | Birth | Jan 23, 1852 | Eureka, Humboldt, CA, USA |
| Big Louie (Big Louie) Garner von Zieliński Sr \[I0000044\] | Birth | Jun 21, 1855 | Great Falls, MT, USA, 2398756 |
| Family | Marriage | Apr 1, 1875 | Paragould, Greene, AR, USA |
| Big Louie (Big Louie) Garner von Zieliński Sr \[I0000044\]   | Death | Jun 28, 1911 | Twin Falls, Twin Falls, ID, USA |
| Big Louie (Big Louie) Garner von Zieliński Sr \[I0000044\] | Burial | Jul 1, 1911 | Twin Falls, Twin Falls, ID, USA |
| Luella Martel \[I0000045\] | Death | Apr 28, 1921 | Myrtle Beach, SC, USA |
| Luella Martel \[I0000045\] | Burial | Apr 30, 1921 | Myrtle Beach, SC, USA |

**Personal events of the children**

| Family Members     | Event Type     | Event Date     | Event Place     |
|----|----|----|----|
| Jesse Garner \[I0000623\] | Birth | Jun 18, 1876 | Paragould, Greene, AR |
| Raymond Garner \[I0000624\] | Birth | Sep 16, 1878 | Paragould, Greene, AR |
| Jennie Garner \[I0000625\] | Birth | Sep 11, 1880 | Paragould, Greene, AR |
| Walter Garner \[I0000626\] | Birth | Feb 17, 1882 | Paragould, Greene, AR |
| Elizabeth Garner \[I0000629\] | Birth | 1883 |  |
| Daniel Garner \[I0000627\] | Birth | Sep 30, 1883 | Hood River, OR, USA |
| Bertha Garner \[I0000628\] | Birth | Mar 13, 1888 | Hagerstown, MD, USA |
| Eugene Garner \[I0000046\] | Birth | Dec 1, 1895 | Portsmouth, OH |
| Raymond Garner \[I0000624\]   | Birth | Jul 12, 1911 |  |
| Bertha Garner \[I0000628\] | Burial | Apr 1918 | Sterling, Whiteside, IL, USA |
| Jesse Garner \[I0000623\] | Burial | 1929 | Sterling, Whiteside, IL, USA |
| Daniel Garner \[I0000627\] | Burial | Mar 4, 1936 | Sterling, Whiteside, IL, USA |
| Walter Garner \[I0000626\] | Burial | Oct 1946 | Sterling, Whiteside, IL, USA |
| Jennie Garner \[I0000625\] | Burial | Jun 1964 | Sterling, Whiteside, IL, USA |
| Eugene Garner \[I0000046\] | Burial | Mar 3, 1984 | Twin Falls, Twin Falls, ID, USA |
| Bertha Garner \[I0000628\] | Death | Apr 5, 1918 | Columbus, Bartholomew, IN, USA |
| Raymond Garner \[I0000624\] | Death | May 2, 1921 | Astoria, OR, USA |
| Jesse Garner \[I0000623\] | Death | Jan 21, 1929 | Cedar City, UT, USA |
| Daniel Garner \[I0000627\] | Death | Mar 2, 1936 | Gary, Lake, IN, USA |
| Walter Garner \[I0000626\] | Death | Oct 23, 1946 | Battle Creek, MI, USA |
| Jennie Garner \[I0000625\] | Death | Jun 20, 1964 | Columbus, Bartholomew, IN, USA |
| Eugene Garner \[I0000046\] | Death | Mar 1, 1984 | Twin Falls, Twin Falls, ID, USA |

</center>

#### On This Day

![[_media/QuickViewReport-OnThisDay-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "On This Day" - Quick View eaxmple]]

Right-click on a selected record in the Event view to select from the context menu or, Double-click a day in the [Calendar Gramplet](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Calendar) to run the Quick View. The Quick View window shows the **Events of** the selected day: *Events on this exact date* and *Other events on this Month/day in history* as well as *Other events in that year*.

The information is presented in a table showing:

- Date
- Type
- Place
- Reference

Select a Quick View entry and use the context menu to edit. You can also drag a reference to the Clipboard. {{-}}

#### Father lineage

Example "Father lineage" quick view report from the People view:

<center>

<big>**Father lineage for Big Louie (Big Louie) Garner von Zieliński Sr**</big>

This report shows the father lineage, also called the patrilineal lineage or Y-line. People in this lineage all share the same Y-chromosomes.

| Name Father     | Birth Date     | Death Date     | Remarks     |
|----|----|----|----|
| Big Louie (Big Louie) Garner von Zieliński Sr \[I0000044\] | Jun 21, 1855 | Jun 28, 1911 |  |
| Robert Garner \[I0000106\] | Apr 24, 1826/7 (Julian) | Feb 3, 1916 | No birth relation with child |
| Joseph Garner \[I0000104\] | 1792 |  |  |

<table>
<tbody>
<tr>
<td><p><strong>Direct line male descendants</strong><br />
Big Louie (Big Louie) Garner von Zieliński Sr (Jun 21, 1855 - Jun 28, 1911)<br />
  |-Eugene Garner (Dec 1, 1895 - Mar 1, 1984)<br />
  |  |-Howard Garner (Jul 9, 1928 - )<br />
  |  |  |-Barry Garner (Dec 14, 1948 - )<br />
  |  |  |  |-Andrew Garner (Apr 11, 1999 - )<br />
  |  |  |-Gerard Garner (Jul 31, 1955 - )<br />
  |  |  |  |-Stephen Garner (Oct 5, 1983 - )<br />
  |  |  |  |-Daniel Garner (Feb 11, 1985 - )<br />
  |  |  |-David Garner (Dec 21, 1956 - )<br />
  |  |  |-Thomas Garner (Dec 10, 1965 - )<br />
  |  |-Eugene Garner ( - )<br />
  |  |  |-Francis Garner (Jan 3, 1945 - )<br />
  |  |  |-Richard Garner (Feb 28, 1947 - )<br />
  |  |  |  |-Jason Garner (Oct 20, 1975 - )<br />
  |  |  |-Michael Garner (Jun 12, 1948 - )<br />
  |  |  |  |-Michael Garner (Jun 1, 1975 - )<br />
  |  |  |-Peter Garner (Aug 5, 1954 - )<br />
  |  |  |-Mark Garner (Oct 16, 1962 - )<br />
  |  |  |-John Garner (Aug 15, 1961 - )<br />
  |  |-John Garner (Oct 29, 1925 - )<br />
  |-Jesse Garner (Jun 18, 1876 - Jan 21, 1929)<br />
  |  |-Victor Garner ( - )<br />
  |-Raymond Garner (Sep 16, 1878 - May 2, 1921)<br />
  |-Walter Garner (Feb 17, 1882 - Oct 23, 1946)<br />
  |-Daniel Garner (Sep 30, 1883 - Mar 2, 1936)</p></td>
</tr>
</tbody>
</table>

</center>

#### Mother lineage

Similar to Father lineage quick view report from the People view as described above.

#### Siblings

![[_media/QuickViewReport-Siblings-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Quick View Report for Siblings]] Siblings of current person with Name, Gender, Birth Date and relationship type (relative to the current person). {{-}}

#### Relation to Home Person

![[_media/QuickViewReport-RelationToHomePerson-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;Relationship to Home Person&quot; - Quick View - example (with context menu shown)]] The Quick View report can be selected from the People view. {{-}}

#### Same Given Names

**Same Given Names** quick view report from the People view will show a dialog with the information in the following format:

        People with the given name *\<Given Name\>*

        There are *\<count\>* people with a matching name, or alternate name.

</center>

| Person     | Birth Date     | Name type     |
|----|----|----|
| Webb, Lewis I. \[I0193\] | March 31, 1903 | Birth Name |
| Warner, Lewis \[I1253\] |  | Birth Name |
| Garner von Zieliński, Lewis Anderson Sr \[I0044\]   | June 21, 1855 | Birth Name |
| Garner, Lewis \[I1105\] | November 18, 1823 | Birth Name |

</center>

The 'Copy All' context menu will include the table data without headers and 2 extra columns for sorting data:  
original row number , Name (in the Preferences format) \[*\<Gramps ID\>*\], birth date (in the Preferences format), Name type, Julian day number (continuous count of days since January 1, 4713 BCE in the proleptic Julian calendar)

    1, Webb, Lewis I. [I0193], March 31, 1903, Birth Name, 2416205
    0, Warner, Lewis [I1253], , Birth Name, 0
    2, Garner von Zieliński, Lewis Anderson Sr [I0044], June 21, 1855, Birth Name, 2398756
    3, Garner, Lewis [I1105], November 18, 1823, Birth Name, 2387218

{{-}}

#### Same Surnames

![[_media/QuickViewReport-SameSurname-PeopleView-example-popup-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Quick View Report - People view -  - example popup window, showing right-click context menu for results table]]

**Same Surnames** quick view report from the People view will show a dialog with a list of the people with the surname. Uses the same format as the [Same Given Name](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_8#Same_Given_Names) Person category Quick View.

See: [Top Surnames](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Top_Surnames) and [Surname Cloud](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Surname_Cloud) Gramplets {{-}}

#### Category References

##### Person References

- Person References Quick View : Display showing the backlink references for the active person

##### Family References

- Family References Quick View : Display showing the backlink references for a family

##### Event References

- Event References Quick View : Display showing the backlink references for an event

##### Place References

- Place References Quick View : Display showing the backlink references for a place

##### Source References

- Source References Quick View : Display backlink references for a Source
- Source or Citation References Quick View : Display backlink references for a Source or Citation

##### Citation References

- Citation References Quickreport : Display backlink references for a Source or Citation

##### Repository References

![[_media/QuickViewReport-RepositoryReferences-example-60.png|Fig {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Repository References" Quick View - example]]

Quick View : Displays the repository backlink references for sources related to the active repository.

- See [Repositories Report](wiki:Addon:RepositoriesReport) addon

{{-}}

##### Media References

- Media References Quick View : Display showing the backlink references for a media object

##### Note References

- Note References Quick View : Display showing the backlink references for a note

#### Link References

**Link Reference** quick view report from the People view will show a dialog with the information in the following format:

        Link References for this note

</center>

| Type     | Reference     | Link check     |
|----|----|----|
| Family | Garner, Rita Marie/Warner, Allen Carl \[F0001\] | Ok |
| Media | Media, 1897_expeditionsmannschaft_rio_a \[O0010\]     | Ok |
| Internet     | relative://relative.archive.tgz |  |
| Internet | relative://relative.archive.zip |  |

</center>

The context menu will vary, based upon the link type of the indicated row.

Link that reference a Gramps object record will offer to "See the *\<object type\>* details". This opens the Object Editor. Rows with Person object types will offer an option to **Make the person active.**. Internet object types have no context menu options.

The context menu will include the table data without headers and an extra columns for sorting data:

**original row number**, **object type**, **reference** (link target), **Link check**

    0, Family, Garner, Rita Marie/Warner, Allen Carl [F0001], Ok
    1, Media, 1897_expeditionsmannschaft_rio_a [O0010], Ok
    ⋮
    8, Internet, relative://relative.archive.tgz, 
    9, Internet, relative://relative.archive.zip, 

{{-}}

### Quick View Gramplet

Configurable to show the Quick View report you want to see.

Available for use from the and each of the category view sidebars and bottombars.

See:

- 

{{-}}

<hr />

### Quick Views Addons

Sort the [Addons list table](wiki:6.0_Addons#Addon_List) on the **Type** column and scroll to the **Quickview** grouping.

Available addon Quick Views (in the People category view) include:

- [All Names of All People](wiki:Addon:All_Names_Quickview)
- [Biography](wiki:Addon:Biography_Quickview)
- [Number of ancestors](wiki:Addon:NumberOfAncestorsQuickView) (by generation)
- [Number of descendants](wiki:Addon:Number_of_Descendants_Quickview) (totals broken down by generation and timeline overlaps) \[<abbr title="sic erat scriptum, recte ____ - Latin phrase meaning 'thus it was written, rightly ____'">[recte](wiki:Genealogy_Glossary#recte)</abbr>: not the [Descendant Count](wiki:Addon:Descendant_Count_Gramplet) gramplet\]
- [Timeline](wiki:Addon:Timeline_Quickview) (events of immediate family)

### Making your own Quick Views

You can create your own Quick Views, even with limited programming/coding knowledge.

Many users want to produce a view quickly for their specific needs, but are hindered by the fact they do not want to learn python fully, nor the intricacies of a complicated program like Gramps.

These views are short textual reports that the user can register with Gramps, so they automatically appear in the context menu's.

Accompanying this, the [simple database access](wiki:Simple_Access_API) and [simple document interface](wiki:Report_API)'s have been constructed, so as to hide as much complexity as possible.

See the [Quick Views development page](wiki:Quick_Views) to make your own. {{-}}

<hr>

Tilbage til [Indeks over Rapporter](wiki:Da:Gramps_6.0_brugsanvisning_-_Rapporter). {{-}}

[Category:Documentation](wiki:Category:Documentation) [Category:Plugins](wiki:Category:Plugins)
