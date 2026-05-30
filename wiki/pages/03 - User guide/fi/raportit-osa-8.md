---
title: Fi:Gramps 6.0 Wiki-käyttöohje - Raportit Osa 8
categories:
- Fi:Dokumentaatio
- Plugins
- Stub
managed: false
source: wiki-scrape
wiki_revid: 126268
wiki_fetched_at: '2026-05-30T18:28:46Z'
lang: fi
---

{{#vardefine:chapter\|11.8}} {{#vardefine:figure\|0}} Takaisin [Raportit](wiki:Fi:Gramps_6.0_Wiki-käyttöohje_-_Raportit) -osion alkuun.

<hr>

{{-}} ![[_media/QuickViewReport-EditPerson-context-menu-popup-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Quick View context menu on Edit Person]] This section describes the Quick Views as part of the different reports available in Gramps.

## Quick Views

![[_media/QuickViewReport-people-context-menu-popup-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Quick View context menu on the People Category - Person (List) View]]

![[_media/QuickViewReport-SameSurname-PeopleView-example-popup-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Quick View Report - People view - Same Surname - example popup window, showing right-click context menu]]

**Quick Views** are popup window reports available in the context menu's of the most of the category views and some of the edit dialogs.

The following Quick view reports are available:

- *Dashboard view* - **Not available**
  - Note that you can use the [Quick View Gramplet](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_8#Quick_View_Gramplet)

<!-- -->

- *People view* and *Person Edit dialog*
  - [All Events](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_8#All_Events)
  - [Father linage](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_8#Father_linage)
  - [Mother linage](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_8#Mother_linage)
  - [Person References](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_8#Person_References)
  - [Relation to Home Person](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_8#Relation_to_Home_Person)
  - [Same Given Names](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_8#Same_Given_Names)
  - [Same Surnames](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_8#Same_Surnames)
  - [Siblings](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_8#Siblings)

<!-- -->

- *Relationship view* - **Not available**

<!-- -->

- *Families view* and *Family Edit dialog*
  - [All Family Events](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_8#All_Family_Events)
  - [Family References](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_8#Family_References)

<!-- -->

- *Chart view* - **Not available**

<!-- -->

- *Events view*
  - [Event References](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_8#Event_References)
  - [On This Day](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_8#On_This_Day)

<!-- -->

- *Places view*
  - [Place References](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_8#Place_References)

<!-- -->

- *Geography view* - **Not available**

<!-- -->

- *Sources view*
  - [Source References](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_8#Source_References)

<!-- -->

- *Citations view*
  - [Citation References](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_8#Citation_References)

<!-- -->

- *Repository view*
  - [Repository References](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_8#Repository_References)

<!-- -->

- *Media view*
  - [Media References](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_8#Media_References)

<!-- -->

- *Notes view*
  - [Link References](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_8#Link_References)
  - [Note References](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_8#Note_References)

{{-}}

#### All Events

#### All Family Events

#### On This Day

#### Father linage

#### Mother linage

#### Siblings

#### Relation to Home Person

#### Same Given Names

#### Same Surnames

#### Person References

#### Family References

#### Event References

#### Place References

#### Source References

#### Citation References

#### Repository References

#### Media References

#### Link References

#### Note References

{{-}}

## Quick View Gramplet

Configurable to show the Quick View you want to see.

Available for use from the and each of the category view sidebars and bottombars.

See: [Gramplets &gt; Quick View](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Quick_View) {{-}}

## Making your own Quick view

You can create your own Quick view, even with limited programming/coding knowledge.

Many users want to produce a view quickly for their specific needs, but are hindered by the fact they do not want to learn python fully, nor the intricacies of a complicated program like Gramps.

These views are short textual reports that the user can register with Gramps, so they automatically appear in the context menu's.

Accompanying this, the [simple database access](wiki:Simple_Access_API) and [simple document interface](wiki:Report_API)'s have been constructed, so as to hide as much complexity as possible.

See the [Quick Views Coding page](wiki:Quick_Views) to make your own.

{{-}}

<hr>

Back to [Index of Reports](wiki:Gramps_6.0_Wiki_Manual_-_Reports).

[Category:Fi:Dokumentaatio](wiki:Category:Fi:Dokumentaatio) [Category:Plugins](wiki:Category:Plugins)
